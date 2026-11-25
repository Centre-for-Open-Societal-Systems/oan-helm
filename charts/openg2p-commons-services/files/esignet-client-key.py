"""Make sure the IAM beneficiary portal API's eSignet signing key exists and write its public JWK.

The portal authenticates to eSignet with private_key_jwt, so eSignet's client_detail row needs the public
half of the key that the portal API's login_providers row holds the private half of. This step keeps the
private half in a Secret: it is created once with a new RSA 2048 key (PKCS#8 PEM) and never replaced, so
the portal and eSignet keep agreeing across upgrades. The public JWK is derived from whatever the Secret
holds now and written to OUT for the next step, which registers it in eSignet. The key is never printed.

Input (environment): NAMESPACE, SECRET, KEY (the Secret and its key), CLIENT_ID (the JWK kid), OUT.
The pod's service account token is used for the Kubernetes API.
"""
import base64
import json
import os
import re
import ssl
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

API = "https://kubernetes.default.svc"
SA = "/var/run/secrets/kubernetes.io/serviceaccount"
NAMESPACE = os.environ["NAMESPACE"]
SECRET = os.environ["SECRET"]
KEY = os.environ["KEY"]
CLIENT_ID = os.environ["CLIENT_ID"]
OUT = os.environ["OUT"]

TOKEN = open(f"{SA}/token").read().strip()
CONTEXT = ssl.create_default_context(cafile=f"{SA}/ca.crt")
URL = f"{API}/api/v1/namespaces/{NAMESPACE}/secrets"


def call(method, url, body=None, content_type="application/json"):
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {TOKEN}", "Content-Type": content_type, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, context=CONTEXT, timeout=30) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, None


def openssl(*args):
    return subprocess.run(["openssl", *args], check=True, capture_output=True, text=True).stdout


def new_key():
    return openssl("genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048")


def b64url(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def stored_pem():
    """The PEM in the Secret, creating the Secret or the key when missing; None when another job won the race."""
    status, secret = call("GET", f"{URL}/{SECRET}")
    if status == 200:
        value = (secret.get("data") or {}).get(KEY)
        if value:
            return base64.b64decode(value).decode()
        pem = new_key()
        status, _ = call("PATCH", f"{URL}/{SECRET}", {"data": {KEY: base64.b64encode(pem.encode()).decode()}},
                         "application/merge-patch+json")
        if status != 200:
            sys.exit(f"patching Secret {SECRET} failed: HTTP {status}")
        print(f"added key {KEY} to Secret {SECRET}")
        return pem
    if status != 404:
        sys.exit(f"reading Secret {SECRET} failed: HTTP {status}")
    pem = new_key()
    status, _ = call("POST", URL, {
        "apiVersion": "v1", "kind": "Secret", "metadata": {"name": SECRET}, "type": "Opaque",
        "data": {KEY: base64.b64encode(pem.encode()).decode()}})
    if status == 409:
        return None
    if status not in (200, 201):
        sys.exit(f"creating Secret {SECRET} failed: HTTP {status}")
    print(f"created Secret {SECRET} with a new signing key")
    return pem


def jwk(pem):
    with tempfile.NamedTemporaryFile("w", dir=os.path.dirname(OUT)) as key_file:
        key_file.write(pem)
        key_file.flush()
        text = openssl("rsa", "-in", key_file.name, "-noout", "-text", "-modulus")
    modulus = re.search(r"^Modulus=([0-9A-Fa-f]+)$", text, re.M).group(1)
    exponent = int(re.search(r"publicExponent:\s*(\d+)", text).group(1))
    return {
        "kty": "RSA", "alg": "RS256", "use": "sig", "kid": CLIENT_ID,
        "n": b64url(bytes.fromhex(modulus)),
        "e": b64url(exponent.to_bytes((exponent.bit_length() + 7) // 8, "big")),
    }


pem = stored_pem() or stored_pem()
if not pem:
    sys.exit(f"Secret {SECRET} appeared while it was being created; retry")
with open(OUT, "w") as out:
    json.dump(jwk(pem), out, separators=(",", ":"))
print(f"public JWK for {CLIENT_ID} written")
