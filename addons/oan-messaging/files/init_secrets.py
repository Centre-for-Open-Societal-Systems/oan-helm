"""Create the Secrets an OAN Messaging release needs, once. Never prints a value.

Runs in the service image as a Helm pre-install/pre-upgrade hook, with a ServiceAccount that
may only get and create Secrets in its own namespace. A Secret that exists is never touched,
so upgrades keep the generated passwords, keys and certificates; to regenerate one, delete it
(and, for the database Secret, run the release's db-init Job again).

  oan-messaging-database      runtime-url, migration-url, owner-password, runtime-password
  oan-messaging-core          content-keys, fingerprint-keys, credential-pepper

With FAKE8028=true (New Dev has no 8028 credentials) it also makes the fake gateway's test
material, signed by a throwaway CA from gen_certs.py:

  oan-messaging-sms8028, oan-messaging-sms8028-client-tls, oan-messaging-8028-callback,
  oan-messaging-8028-callback-ca, oan-messaging-receipts-server-tls, oan-messaging-fake8028

Environment: DB_HOST, DB_NAME, DB_OWNER, DB_RUNTIME, FAKE8028 (true/false), RECEIPTS_HOST,
FAKE8028_HOST (certificate names; gen_certs.py reads them too).
"""

from __future__ import annotations

import base64
import json
import os
import secrets
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

SA = Path("/var/run/secrets/kubernetes.io/serviceaccount")
NS = (SA / "namespace").read_text().strip()
TOKEN = (SA / "token").read_text().strip()
API = f"https://{os.environ['KUBERNETES_SERVICE_HOST']}:{os.environ['KUBERNETES_SERVICE_PORT']}"
CTX = ssl.create_default_context(cafile=str(SA / "ca.crt"))
DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ.get("DB_NAME", "oan_messaging")
DB_OWNER = os.environ.get("DB_OWNER", "oan_msg_owner")
DB_RUNTIME = os.environ.get("DB_RUNTIME", "oan_msg_runtime")
FAKE = os.environ.get("FAKE8028", "false").lower() == "true"
CERTS = Path("/tmp/certs")


def call(method: str, path: str, body: dict | None = None) -> int:
    req = urllib.request.Request(
        API + path,
        method=method,
        data=json.dumps(body).encode() if body else None,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=20) as r:  # noqa: S310 - in-cluster API
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def exists(name: str) -> bool:
    return call("GET", f"/api/v1/namespaces/{NS}/secrets/{name}") == 200


def create(name: str, data: dict[str, str | bytes], kind: str = "Opaque") -> None:
    enc = {
        k: base64.b64encode(v if isinstance(v, bytes) else v.encode()).decode()
        for k, v in data.items()
    }
    status = call(
        "POST",
        f"/api/v1/namespaces/{NS}/secrets",
        {
            "apiVersion": "v1",
            "kind": "Secret",
            "type": kind,
            "metadata": {"name": name, "labels": {"app.kubernetes.io/part-of": "oan-messaging"}},
            "data": enc,
        },
    )
    if status not in (200, 201):
        sys.exit(f"creating Secret {name} failed: HTTP {status}")
    print(f"created Secret {name} (keys: {', '.join(sorted(data))})")


def b64(n: int) -> str:
    return base64.b64encode(secrets.token_bytes(n)).decode()


def cert_files() -> dict[str, bytes]:
    if not (CERTS / "ca.crt").exists():
        subprocess.run([sys.executable, "/scripts/gen_certs.py", str(CERTS)], check=True)
    return {p.name: p.read_bytes() for p in CERTS.iterdir()}


FAKE_GROUP = (
    "oan-messaging-sms8028", "oan-messaging-sms8028-client-tls", "oan-messaging-8028-callback",
    "oan-messaging-8028-callback-ca", "oan-messaging-receipts-server-tls",
    "oan-messaging-fake8028",
)

if not exists("oan-messaging-database"):
    owner, runtime = secrets.token_urlsafe(24), secrets.token_urlsafe(24)
    # token_urlsafe is [A-Za-z0-9_-]: safe in a URL userinfo and in a SQL literal.
    create("oan-messaging-database", {
        "owner-password": owner,
        "runtime-password": runtime,
        "runtime-url": f"postgresql+psycopg://{DB_RUNTIME}:{runtime}@{DB_HOST}:5432/{DB_NAME}",
        "migration-url": f"postgresql+psycopg://{DB_OWNER}:{owner}@{DB_HOST}:5432/{DB_NAME}",
    })
if not exists("oan-messaging-core"):
    create("oan-messaging-core", {
        "content-keys": "v1:" + b64(32),
        "fingerprint-keys": "k1:" + b64(32),
        "credential-pepper": b64(32),
    })

if FAKE:
    present = [n for n in FAKE_GROUP if exists(n)]
    if present and len(present) != len(FAKE_GROUP):
        sys.exit("some fake-gateway Secrets exist and some do not (present: " + ", ".join(present)
                 + "). Delete them all to regenerate.")
    if not present:
        f = cert_files()
        client_secret, callback_secret = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
        create("oan-messaging-sms8028", {"client-secret": client_secret})
        create("oan-messaging-sms8028-client-tls", {
            "tls.crt": f["oan-8028-client.crt"], "tls.key": f["oan-8028-client.key"],
            "ca.crt": f["ca.crt"]}, "kubernetes.io/tls")
        create("oan-messaging-8028-callback", {"callback-secret": callback_secret})
        create("oan-messaging-8028-callback-ca", {"ca.crt": f["ca.crt"]})
        create("oan-messaging-receipts-server-tls", {
            "tls.crt": f["receipts-server.crt"], "tls.key": f["receipts-server.key"]},
            "kubernetes.io/tls")
        create("oan-messaging-fake8028", {
            "ca.crt": f["ca.crt"], "fake8028-server.crt": f["fake8028-server.crt"],
            "fake8028-server.key": f["fake8028-server.key"],
            "callback-client.crt": f["callback-client.crt"],
            "callback-client.key": f["callback-client.key"],
            "client-secret": client_secret, "callback-secret": callback_secret})
print("secrets ready")
