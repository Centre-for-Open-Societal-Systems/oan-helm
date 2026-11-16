"""Make sure each declared partner exists and is active in Partner Management.

Uses Partner Management's documented admin API (openg2p-documentation
platform/platform-services/partner-management/api-reference.md):
  GET  /partners/{partner_id}                      present?
  POST /partners/requests/onboarding               create it (status created, request created)
  POST /partners/requests/{request_id}/approve     activate it
  GET  /partners/requests?status=created&request_type=onboarding&partner_id=...
                                                   finish an onboarding a previous run left unapproved

A partner that is already active is left alone. A disabled partner, or one whose onboarding was rejected, stops the
Job: turning it back on is a partner manager's decision. No keys or policies are added; a partner that signs requests
gets its key from its own chart (for example addons/farmer-connector partnerRegistration).
"""
import json
import os
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


class Retry(RuntimeError):
    """Partner Management or Keycloak is not answering yet; try again."""


class Refused(RuntimeError):
    """A definite answer that another attempt will not change."""


def send(method, url, body=None, headers=None, form=False):
    data = None
    headers = dict(headers or {})
    if body is not None:
        if form:
            data = urlencode(body).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        else:
            data = json.dumps(body).encode()
            headers["Content-Type"] = "application/json"
    try:
        with urlopen(Request(url, data=data, method=method, headers=headers), timeout=30) as response:
            raw = response.read()
            return response.status, json.loads(raw) if raw else None
    except HTTPError as error:
        if error.code >= 500 or error.code in (401, 403, 429):
            error.close()
            raise Retry(f"{method} {url.split('?')[0]}: HTTP {error.code}") from None
        try:
            payload = json.loads(error.read() or b"null")
        except ValueError:
            payload = None
        return error.code, payload
    except (URLError, TimeoutError, ValueError):
        raise Retry(f"{method} {url.split('?')[0]}: unavailable or invalid JSON") from None


def error_codes(payload):
    """Partner Management puts its real error code in the body, e.g. HTTP 400 with PM-PRT-409 for already exists."""
    if isinstance(payload, dict):
        return {str(item.get("code")) for item in payload.get("errors") or [] if isinstance(item, dict)}
    return set()


def items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("items", "data", "requests"):
            if isinstance(payload.get(key), list):
                return payload[key]
    return []


class PartnerManager:
    def __init__(self, config, secret):
        self.base = config["partnerManagerUrl"].rstrip("/")
        self.config = config
        self.secret = secret
        self.token = None

    def sign_in(self):
        status, payload = send("POST", self.config["tokenUrl"], {
            "grant_type": "client_credentials", "client_id": self.config["clientId"], "client_secret": self.secret,
        }, form=True)
        token = (payload or {}).get("access_token") if status == 200 else None
        if not isinstance(token, str) or not token:
            raise Retry(f"no token for client {self.config['clientId']} (HTTP {status})")
        self.token = token

    def call(self, method, path, body=None):
        return send(method, self.base + path, body, {"Authorization": "Bearer " + self.token})

    def partner(self, partner_id):
        status, payload = self.call("GET", "/partners/" + quote(partner_id, safe=""))
        if status == 404:
            return None
        if status != 200 or not isinstance(payload, dict):
            raise Refused(f"lookup of {partner_id} answered HTTP {status}")
        return payload

    def approve(self, partner_id, request_id):
        status, payload = self.call("POST", f"/partners/requests/{quote(str(request_id), safe='')}/approve", {})
        if status >= 300:
            raise Refused(f"approval of the onboarding of {partner_id} answered HTTP {status} {sorted(error_codes(payload))}")

    def open_onboarding(self, partner_id):
        query = urlencode({"status": "created", "request_type": "onboarding", "partner_id": partner_id})
        status, payload = self.call("GET", "/partners/requests?" + query)
        if status != 200:
            raise Refused(f"request lookup for {partner_id} answered HTTP {status}")
        return [item for item in items(payload) if item.get("partner_id") in (None, partner_id)]

    def ensure(self, wanted):
        partner_id = wanted["partner_id"]
        found = self.partner(partner_id)
        if found is None:
            status, payload = self.call("POST", "/partners/requests/onboarding", {
                "partner_id": partner_id, "name": wanted["name"], "org_name": wanted["org_name"],
                "description": wanted["description"], "keys": []})
            if status < 300 and isinstance(payload, dict) and payload.get("id"):
                self.approve(partner_id, payload["id"])
                return "onboarded and approved"
            if "PM-PRT-409" not in error_codes(payload):
                raise Refused(f"onboarding of {partner_id} answered HTTP {status} {sorted(error_codes(payload))}")
            found = self.partner(partner_id)  # created meanwhile by someone else
            if found is None:
                raise Retry(f"{partner_id} reported as existing but not found")
        state = found.get("status")
        if state == "active":
            return "already active"
        if state == "created":
            pending = self.open_onboarding(partner_id)
            if not pending:
                raise Refused(f"{partner_id} is not active and has no open onboarding request (rejected?)")
            self.approve(partner_id, pending[0]["id"])
            return "open onboarding approved"
        raise Refused(f"{partner_id} is {state}; a partner manager has to enable it")


def run(config, secret, out=print):
    manager = PartnerManager(config, secret)
    remaining = list(config["partners"])
    attempts = int(config.get("attempts", 30))
    for attempt in range(1, attempts + 1):
        try:
            manager.sign_in()
            while remaining:
                out(f"{remaining[0]['partner_id']}: {manager.ensure(remaining[0])}")
                remaining.pop(0)
            return
        except Retry as reason:
            if attempt == attempts:
                raise Refused(f"gave up after {attempts} attempts: {reason}") from None
            out(f"attempt {attempt}: {reason}; retrying")
            time.sleep(float(config.get("retrySeconds", 10)))


if __name__ == "__main__":
    try:
        with open(sys.argv[1], encoding="utf-8") as source:
            run(json.load(source), os.environ["CLIENT_SECRET"])
    except Refused as reason:
        raise SystemExit(f"Partner onboarding failed: {reason}") from None
    except (KeyError, OSError, ValueError):
        raise SystemExit("Partner onboarding failed: configuration or secret missing") from None
