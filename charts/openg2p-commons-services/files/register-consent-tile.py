"""Register the Consent staff console with IAM using its existing service identity.

No database writes, Keycloak administration or user role assignments are performed.
IAM upserts this application's catalog by its Keycloak client ID.
"""
import json
import os
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen


class RegistrationError(RuntimeError):
    pass


def request_json(url, body, headers):
    try:
        with urlopen(Request(url, data=body, headers=headers), timeout=20) as response:
            return json.load(response)
    except HTTPError as error:
        # Upstream bodies can contain sensitive identity or credential details.
        raise RegistrationError(f"HTTP {error.code}") from None
    except (URLError, TimeoutError, ValueError):
        raise RegistrationError("service unavailable or invalid JSON") from None


def register(config, secret):
    mnemonic = config["application"]["application_mnemonic"]
    if mnemonic != config["clientId"]:
        raise RegistrationError("tile mnemonic must match the Keycloak client ID")
    if urlsplit(config["application"]["application_url"]).scheme != "https":
        raise RegistrationError("tile URL must use HTTPS")
    for attempt in range(config.get("attempts", 40)):
        try:
            # Acquire a fresh token on retries, including after a delayed IAM start.
            credentials = urlencode({"grant_type": "client_credentials",
                                     "client_id": config["clientId"], "client_secret": secret}).encode()
            token = request_json(config["tokenUrl"], credentials,
                                 {"Content-Type": "application/x-www-form-urlencoded"}).get("access_token")
            if not isinstance(token, str) or not token:
                raise RegistrationError("token response has no access token")
            result = request_json(config["iamUrl"].rstrip("/") + "/user-access/staff_portal_applications",
                                  json.dumps(config["application"]).encode(),
                                  {"Authorization": "Bearer " + token, "Content-Type": "application/json"})
            if result.get("application_mnemonic") != mnemonic:
                raise RegistrationError("registration response does not match the requested application")
            print("Registered staff portal tile: " + mnemonic)
            return result
        except RegistrationError:
            if attempt + 1 == config.get("attempts", 40):
                raise
            time.sleep(config.get("retrySeconds", 5))


if __name__ == "__main__":
    try:
        with open("/catalog/application.json", encoding="utf-8") as source:
            register(json.load(source), os.environ["CLIENT_SECRET"])
    except (RegistrationError, KeyError, OSError):
        raise SystemExit("Consent staff portal tile registration failed; private details withheld") from None
