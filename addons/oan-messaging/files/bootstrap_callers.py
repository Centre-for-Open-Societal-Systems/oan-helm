"""Register the release's callers and keep their tokens in Secrets, once. Never prints a token.

Runs in the service image as a Helm hook after the migrations and grants. For each caller in
CALLERS (JSON list of {caller, secret, kind: "messages-reader" | "sender", channels, purposes})
it upserts the caller with the runtime CLI and, only when its token Secret does not exist yet,
issues a credential and stores the token in that Secret (key: token). The token is shown once
by the CLI, alone on stdout, and goes straight into the Secret.
"""

from __future__ import annotations

import base64
import json
import os
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


def call(method: str, path: str, body: dict | None = None) -> int:
    req = urllib.request.Request(
        API + path, method=method, data=json.dumps(body).encode() if body else None,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=20) as r:  # noqa: S310 - in-cluster API
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def cli(*args: str) -> str:
    done = subprocess.run([sys.executable, "-m", "oan_messaging.runtime", *args],
                          capture_output=True, text=True, check=False)
    if done.returncode:
        sys.exit(f"oan_messaging.runtime {args[0]} failed (exit {done.returncode})")
    return done.stdout.strip()


for c in json.loads(os.environ["CALLERS"]):
    args = ["caller", "--caller", c["caller"]]
    if c["kind"] == "messages-reader":
        args += ["--messages-reader"]
    else:
        args += ["--channels", ",".join(c["channels"]), "--purposes", ",".join(c["purposes"])]
    cli(*args)
    print(f"caller {c['caller']} registered")
    if call("GET", f"/api/v1/namespaces/{NS}/secrets/{c['secret']}") == 200:
        print(f"Secret {c['secret']} exists; no new token")
        continue
    token = cli("issue-credential", "--caller", c["caller"]).splitlines()[-1].strip()
    if not token.startswith("oanmsg_"):
        sys.exit("issue-credential did not return a token")
    status = call("POST", f"/api/v1/namespaces/{NS}/secrets", {
        "apiVersion": "v1", "kind": "Secret", "type": "Opaque",
        "metadata": {"name": c["secret"], "labels": {"app.kubernetes.io/part-of": "oan-messaging"}},
        "data": {"token": base64.b64encode(token.encode()).decode()}})
    if status not in (200, 201):
        sys.exit(f"creating Secret {c['secret']} failed: HTTP {status}")
    print(f"Secret {c['secret']} created")
