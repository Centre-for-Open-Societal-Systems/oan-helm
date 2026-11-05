"""Make sure the signing partner exists in Partner Manager and holds this connector's public key."""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

from cryptography.hazmat.primitives import serialization

BASE = os.environ["PARTNER_MANAGER_URL"].rstrip("/")
PARTNER = os.environ["PARTNER_ID"]
KEY_ID = os.environ["KEY_ID"]


def token():
    body = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": os.environ["CLIENT_ID"],
        "client_secret": os.environ["CLIENT_SECRET"],
    }).encode()
    with urllib.request.urlopen(urllib.request.Request(os.environ["TOKEN_URL"], data=body), timeout=30) as response:
        return json.load(response)["access_token"]


BEARER = token()


def call(method, path, body=None):
    request = urllib.request.Request(
        BASE + path, method=method, data=None if body is None else json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + BEARER, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, json.loads(response.read() or b"null")
    except urllib.error.HTTPError as error:
        return error.code, None


def approve(created):
    status, _ = call("POST", "/partners/requests/%s/approve" % created["id"], {})
    if status >= 300:
        raise SystemExit("Partner Manager refused the approval: %s" % status)


private = serialization.load_pem_private_key(os.environ["PRIVATE_KEY_PEM"].encode(), password=None)
public = private.public_key().public_bytes(
    serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo).decode()
key = {"public_key": public, "kid": KEY_ID, "algorithm": "RS256"}

status, _ = call("GET", "/partners/" + PARTNER)
if status == 404:
    status, created = call("POST", "/partners/requests/onboarding", {
        "partner_id": PARTNER, "name": os.environ["PARTNER_NAME"], "org_name": "OpenAgriNet",
        "description": "Signs connector requests.", "keys": [key]})
    if status >= 300:
        raise SystemExit("Partner Manager refused the onboarding: %s" % status)
    approve(created)
    print("Partner created with key", KEY_ID)
    raise SystemExit(0)
if status >= 300:
    raise SystemExit("Partner Manager lookup failed: %s" % status)

status, keys = call("GET", "/partners/%s/keys" % PARTNER)
if status >= 300:
    raise SystemExit("Partner Manager key lookup failed: %s" % status)
if any(item.get("kid") == KEY_ID for item in keys):
    print("Key", KEY_ID, "is already registered")
    raise SystemExit(0)
status, created = call("POST", "/partners/requests/key-update", {
    "partner_id": PARTNER, "description": "Connector signing key", "keys": [key]})
if status >= 300:
    raise SystemExit("Partner Manager refused the key update: %s" % status)
approve(created)
print("Key", KEY_ID, "registered")
