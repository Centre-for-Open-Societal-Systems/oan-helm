"""Add the declared redirect URIs and web origins to existing public Keycloak clients.

keycloak-init creates a client once; on later runs it rewrites only clients it holds a secret for
(confidential clients), so a public client keeps the URLs it was created with when the hosts change.
This adds the URLs from values next to the ones the client already has. It never removes a URL, unless
the client entry sets prune: true, which replaces the lists with exactly the declared ones.

Input: CLIENTS_JSON, a list of {realm, clientId, redirectUris, webOrigins, prune}; KEYCLOAK_URL; the
admin user and password in KEYCLOAK_USER and KEYCLOAK_PASSWORD (master realm, admin-cli).
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


def call(method, url, token=None, form=None, body=None):
    headers = {}
    data = None
    if form is not None:
        data = urllib.parse.urlencode(form).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    elif body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
    return json.loads(raw) if raw else None


def admin_token(base, user, password, attempts, delay):
    url = f"{base}/realms/master/protocol/openid-connect/token"
    form = {"grant_type": "password", "client_id": "admin-cli", "username": user, "password": password}
    for attempt in range(1, attempts + 1):
        try:
            return call("POST", url, form=form)["access_token"]
        except (urllib.error.URLError, KeyError, ValueError) as error:
            print(f"Keycloak token not ready (attempt {attempt}/{attempts}): {error}", flush=True)
            time.sleep(delay)
    raise SystemExit("Could not get a Keycloak admin token")


def merged(current, declared, prune):
    if prune:
        return list(dict.fromkeys(declared))
    return list(dict.fromkeys([*current, *declared]))


def reconcile(base, token, entry):
    realm, client_id = entry["realm"], entry["clientId"]
    clients_url = f"{base}/admin/realms/{urllib.parse.quote(realm)}/clients"
    found = call("GET", f"{clients_url}?{urllib.parse.urlencode({'clientId': client_id})}", token)
    if not found:
        print(f"{realm}/{client_id}: not found; keycloak-init creates it with the declared URLs", flush=True)
        return "missing"
    client = found[0]
    if not client.get("publicClient"):
        print(f"{realm}/{client_id}: confidential; keycloak-init keeps it in step, skipped", flush=True)
        return "skipped"
    prune = bool(entry.get("prune"))
    redirects = merged(client.get("redirectUris") or [], entry.get("redirectUris") or [], prune)
    origins = merged(client.get("webOrigins") or [], entry.get("webOrigins") or [], prune)
    if redirects == (client.get("redirectUris") or []) and origins == (client.get("webOrigins") or []):
        print(f"{realm}/{client_id}: already has the declared URLs", flush=True)
        return "unchanged"
    client["redirectUris"], client["webOrigins"] = redirects, origins
    call("PUT", f"{clients_url}/{client['id']}", token, body=client)
    print(f"{realm}/{client_id}: redirectUris={redirects} webOrigins={origins}", flush=True)
    return "updated"


def main():
    base = os.environ["KEYCLOAK_URL"].rstrip("/")
    entries = json.loads(os.environ["CLIENTS_JSON"])
    attempts = int(os.environ.get("TOKEN_ATTEMPTS", "30"))
    delay = float(os.environ.get("TOKEN_DELAY_SECONDS", "5"))
    token = admin_token(base, os.environ["KEYCLOAK_USER"], os.environ["KEYCLOAK_PASSWORD"], attempts, delay)
    results = {f"{e['realm']}/{e['clientId']}": reconcile(base, token, e) for e in entries}
    print(json.dumps(results), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
