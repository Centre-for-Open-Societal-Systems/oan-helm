"""Give the aggregation search's staff role to the users named in values.

The Aggregation API lets a staff user search only with one of its staff search roles
(aggregation-api env AGGREGATION_LAYER_STAFF_SEARCH_ROLES, realm roles of the staff realm). This
Job makes that role exist in the realm and adds it to each user in aggregationStaffGrant.users, the
way the registry dashboards' iamSetup.grantUsers does for their client role: each name must be
exactly one existing staff user (not a service account), the role is only added, and the user's
other roles are read back unchanged. Users are never created, changed or removed, and the role is
never taken away from anyone; removing a name from values leaves the grant in place.

Input: REALM, ROLE, ROLE_DESCRIPTION, USERS (space separated); KEYCLOAK_URL; the admin user and
password in KEYCLOAK_USER and KEYCLOAK_PASSWORD (master realm, admin-cli, as the chart's other
Keycloak Jobs).
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


def realm_role(admin, token, role, description):
    """The realm role, created first if the realm does not have it."""
    url = f"{admin}/roles/{urllib.parse.quote(role, safe='')}"
    try:
        return call("GET", url, token), "present"
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
    call("POST", f"{admin}/roles", token, body={"name": role, "description": description})
    return call("GET", url, token), "created"


def staff_user(admin, token, username, realm):
    query = urllib.parse.urlencode({"username": username, "exact": "true"})
    matches = call("GET", f"{admin}/users?{query}", token)
    if (not isinstance(matches, list) or len(matches) != 1 or not matches[0].get("id")
            or matches[0].get("username") != username or matches[0].get("serviceAccountClientId")):
        raise SystemExit(f"{username} must be exactly one staff user in realm {realm}")
    return matches[0]


def grant(admin, token, user, role):
    """Add the role; fail if it is not there afterwards or another realm role went missing."""
    path = f"{admin}/users/{urllib.parse.quote(user['id'], safe='')}/role-mappings/realm"
    before = call("GET", path, token)
    if not isinstance(before, list) or not role.get("id"):
        raise SystemExit(f"{user['username']}: cannot read the realm role mappings")
    if any(existing.get("id") == role["id"] for existing in before):
        return "unchanged"
    call("POST", path, token, body=[{"id": role["id"], "name": role["name"]}])
    after = {mapping.get("id") for mapping in (call("GET", path, token) or [])}
    if not {role["id"], *(existing.get("id") for existing in before)} <= after:
        raise SystemExit(f"{user['username']}: the grant could not be verified, or another role was removed")
    return "granted"


def main():
    base = os.environ["KEYCLOAK_URL"].rstrip("/")
    realm, role_name = os.environ["REALM"], os.environ["ROLE"]
    users = list(dict.fromkeys(os.environ.get("USERS", "").split()))
    attempts = int(os.environ.get("TOKEN_ATTEMPTS", "30"))
    delay = float(os.environ.get("TOKEN_DELAY_SECONDS", "5"))
    token = admin_token(base, os.environ["KEYCLOAK_USER"], os.environ["KEYCLOAK_PASSWORD"], attempts, delay)
    admin = f"{base}/admin/realms/{urllib.parse.quote(realm, safe='')}"
    role, state = realm_role(admin, token, role_name, os.environ.get("ROLE_DESCRIPTION", ""))
    print(f"{realm}/{role_name}: {state}", flush=True)
    # Every name is checked before anything is granted, so a typo grants nobody.
    resolved = [staff_user(admin, token, username, realm) for username in users]
    results = {user["username"]: grant(admin, token, user, role) for user in resolved}
    print(json.dumps({"realm": realm, "role": role_name, "users": results}), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
