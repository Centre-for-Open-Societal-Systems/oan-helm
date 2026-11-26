"""Fake 8028 SMS gateway for the local integration trial. NOT the real gateway.

* ``https://fake-8028:8443/sms-api/v1/sms/send-sms``: mTLS (the client certificate must
  chain to the trial CA), ``clientSecret`` checked, one recipient per request, 8028-shaped
  success body with a fresh ``sms_id``.
* Then it calls back the OAN receipt ingress as 8028 guide v1.1 describes:
  ``POST https://oan-receipts:8443/sms-status-receiver/v1/update-status`` with a client
  certificate issued by the trial CA and ``{"clientSecret", "sms_id" (a number),
  "phone_number" (251...), "status", "event_time"}``: first ``Pending``, then
  ``Delivered``. It expects ``200 {"success": true}``.
* ``http://<host>:8080/inbox`` (trial network and 127.0.0.1 only) lists what it
  "sent", so tests can read an OTP like a handset would. ``DELETE /inbox`` clears it.

Nothing leaves the Docker network. Message text is never logged.
"""

from __future__ import annotations

import itertools
import json
import os
import ssl
import threading
import time
import urllib.request
from datetime import UTC, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

CERTS = os.environ.get("CERTS_DIR", "/certs")
SECRET = os.environ["FAKE8028_CLIENT_SECRET"]
CALLBACK_URL = os.environ.get(
    "FAKE8028_CALLBACK_URL", "https://oan-receipts:8443/sms-status-receiver/v1/update-status"
)
if not CALLBACK_URL.startswith("https://"):
    raise SystemExit("FAKE8028_CALLBACK_URL must be an https URL")
CALLBACK_SECRET = os.environ["FAKE8028_CALLBACK_SECRET"]
CALLBACK_DELAY = float(os.environ.get("FAKE8028_CALLBACK_DELAY", "1.0"))
MODE = os.environ.get("FAKE8028_MODE", "ok")  # ok | http503 | http401
EAT = timedelta(hours=3)

INBOX: list[dict[str, str]] = []
LOCK = threading.Lock()
# Unique across restarts (8028 sms_ids must never repeat; OAN matches receipts by them).
IDS = itertools.count(int(time.time() * 1000))


def callback(sms_id: str, phone: str) -> None:
    time.sleep(CALLBACK_DELAY)
    for status in ("Pending", "Delivered"):
        send_status(sms_id, phone, status)


def send_status(sms_id: str, phone: str, status: str) -> None:
    ctx = ssl.create_default_context(cafile=f"{CERTS}/ca.crt")
    ctx.load_cert_chain(f"{CERTS}/callback-client.crt", f"{CERTS}/callback-client.key")
    body = json.dumps(
        {
            "clientSecret": CALLBACK_SECRET,
            "sms_id": int(sms_id),  # 8028 may send it as a number (guide 8.1)
            "phone_number": "251" + phone[1:],  # international form in callbacks (guide 5.3)
            "status": status,
            "event_time": (datetime.now(UTC) + EAT).strftime("%Y-%m-%d %H:%M:%S"),
        }
    ).encode()
    req = urllib.request.Request(  # noqa: S310 - CALLBACK_URL is checked to be https at start
        CALLBACK_URL,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    for attempt in range(5):
        try:
            # nosemgrep: dynamic-urllib-use-detected -- fixed https callback URL (checked at start)
            with urllib.request.urlopen(req, context=ctx, timeout=5) as r:  # noqa: S310
                ok = json.loads(r.read()).get("success") is True
                print(
                    f"fake8028 callback sms_id={sms_id} status={status} http={r.status} "
                    f"success={ok}",
                    flush=True,
                )
                return
        except Exception as exc:  # retry like a gateway would
            print(f"fake8028 callback sms_id={sms_id} error={type(exc).__name__}", flush=True)
            time.sleep(1 + attempt)


class Gateway(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *_a: object) -> None:
        return

    def reply(self, code: int, payload: object) -> None:
        raw = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_POST(self) -> None:  # noqa: N802
        n = int(self.headers.get("Content-Length", "0"))
        try:
            body = json.loads(self.rfile.read(n))
        except ValueError:
            return self.reply(400, {"success": False, "message": "invalid json"})
        if self.path != "/sms-api/v1/sms/send-sms":
            return self.reply(404, {"success": False})
        if MODE == "http503":
            return self.reply(503, {"success": False, "message": "unavailable"})
        if MODE == "http401" or body.get("clientSecret") != SECRET:
            return self.reply(401, {"success": False, "message": "unauthorized"})
        phones, text = body.get("phonenums"), body.get("smstext")
        if not (isinstance(phones, list) and len(phones) == 1 and isinstance(text, str)):
            return self.reply(400, {"success": False, "message": "invalid request"})
        sms_id = str(next(IDS))
        with LOCK:
            INBOX.append(
                {
                    "sms_id": sms_id,
                    "phone": phones[0],
                    "text": text,
                    "pushdatetime": str(body.get("pushdatetime")),
                    "received_at": datetime.now(UTC).isoformat(),
                }
            )
        print(f"fake8028 accepted sms_id={sms_id} chars={len(text)}", flush=True)
        self.reply(
            201,
            {
                "success": True,
                "message": "SMS records queued successfully.",
                "data": [{"phone_number": phones[0], "sms_id": sms_id}],
            },
        )
        threading.Thread(target=callback, args=(sms_id, phones[0]), daemon=True).start()


class Inbox(BaseHTTPRequestHandler):
    def log_message(self, *_a: object) -> None:
        return

    def do_GET(self) -> None:  # noqa: N802
        q = parse_qs(urlparse(self.path).query)
        with LOCK:
            rows = [r for r in INBOX if "phone" not in q or r["phone"] in q["phone"]]
        raw = json.dumps(rows).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_DELETE(self) -> None:  # noqa: N802
        with LOCK:
            INBOX.clear()
        self.send_response(204)
        self.end_headers()


def main() -> None:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.load_cert_chain(f"{CERTS}/fake8028-server.crt", f"{CERTS}/fake8028-server.key")
    ctx.verify_mode = ssl.CERT_REQUIRED  # 8028 mTLS
    ctx.load_verify_locations(cafile=f"{CERTS}/ca.crt")
    gw = ThreadingHTTPServer(("0.0.0.0", 8443), Gateway)  # noqa: S104
    gw.socket = ctx.wrap_socket(gw.socket, server_side=True)
    inbox = ThreadingHTTPServer(("0.0.0.0", 8080), Inbox)  # noqa: S104
    threading.Thread(target=inbox.serve_forever, daemon=True).start()
    print(f"fake8028 listening mode={MODE}", flush=True)
    gw.serve_forever()


if __name__ == "__main__":
    main()
