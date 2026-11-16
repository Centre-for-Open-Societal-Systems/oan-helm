"""Exercise the partner onboarding job against a fake Partner Management, without a live cluster."""
import importlib.util
import json
import sys
import threading
import unittest
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

source = Path(__file__).resolve().parents[1] / "addons/commons-partners/files/onboard_partners.py"
spec = importlib.util.spec_from_file_location("onboard_partners", source)
onboard = importlib.util.module_from_spec(spec)
previous_bytecode_setting = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(onboard)
finally:
    sys.dont_write_bytecode = previous_bytecode_setting


class FakePartnerManager:
    """The answers Partner Management gives (shapes taken from a live staff-portal-api)."""

    def __init__(self):
        self.partners = {}
        self.requests = {}
        self.calls = []
        self.unavailable = 0
        self.race = False


class OnboardingTests(unittest.TestCase):
    def setUp(self):
        pm = self.pm = FakePartnerManager()
        owner = self

        class Fixture(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                pass

            def reply(self, status, payload):
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(payload).encode())

            def do_GET(self):
                url = urlsplit(self.path)
                pm.calls.append(("GET", url.path))
                owner.assertEqual(self.headers["Authorization"], "Bearer fixture-token")
                if pm.unavailable:
                    pm.unavailable -= 1
                    return self.reply(503, {})
                if url.path == "/partners/requests":
                    query = {k: v[0] for k, v in parse_qs(url.query).items()}
                    found = [r for r in pm.requests.values()
                             if all(r.get(k) == v for k, v in query.items())]
                    return self.reply(200, {"count": len(found), "requests": found})
                partner_id = url.path.removeprefix("/partners/")
                if partner_id in pm.partners:
                    return self.reply(200, pm.partners[partner_id])
                self.reply(404, {"errors": [{"code": "PM-PRT-404", "message": "not found"}]})

            def do_POST(self):
                body = self.rfile.read(int(self.headers["Content-Length"]))
                pm.calls.append(("POST", self.path))
                if self.path == "/token":
                    form = parse_qs(body.decode())
                    owner.assertEqual(form["client_id"], ["commons-services-staff-portal"])
                    owner.assertEqual(form["client_secret"], ["fixture-secret"])
                    return self.reply(200, {"access_token": "fixture-token"})
                owner.assertEqual(self.headers["Authorization"], "Bearer fixture-token")
                if self.path == "/partners/requests/onboarding":
                    wanted = json.loads(body)
                    owner.assertEqual(wanted["keys"], [])
                    if pm.race:
                        pm.partners[wanted["partner_id"]] = {"partner_id": wanted["partner_id"], "status": "active"}
                    if wanted["partner_id"] in pm.partners:
                        return self.reply(400, {"errors": [{"code": "PM-PRT-409", "message": "already exists"}]})
                    request_id = str(uuid.uuid4())
                    pm.partners[wanted["partner_id"]] = {"partner_id": wanted["partner_id"], "status": "created"}
                    pm.requests[request_id] = {"id": request_id, "partner_id": wanted["partner_id"],
                                               "request_type": "onboarding", "status": "created"}
                    return self.reply(201, pm.requests[request_id])
                if self.path.startswith("/partners/requests/") and self.path.endswith("/approve"):
                    request = pm.requests[self.path.split("/")[3]]
                    request["status"] = "approved"
                    pm.partners[request["partner_id"]]["status"] = "active"
                    return self.reply(200, request)
                owner.fail("unexpected call " + self.path)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        base = f"http://127.0.0.1:{self.server.server_port}"
        self.config = {
            "partnerManagerUrl": base, "tokenUrl": base + "/token", "clientId": "commons-services-staff-portal",
            "attempts": 3, "retrySeconds": 0,
            "partners": [{"partner_id": "PARTNER_STAFF_PORTAL", "name": "Staff Portal (file import)",
                          "org_name": "OpenAgriNet", "description": "Sender of staff portal file imports"}],
        }
        self.lines = []

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def run_job(self):
        onboard.run(self.config, "fixture-secret", out=self.lines.append)

    def writes(self):
        return [path for method, path in self.pm.calls if method == "POST" and path != "/token"]

    def test_missing_partner_is_onboarded_and_approved(self):
        self.run_job()
        self.assertEqual(self.pm.partners["PARTNER_STAFF_PORTAL"]["status"], "active")
        self.assertEqual(self.lines, ["PARTNER_STAFF_PORTAL: onboarded and approved"])

    def test_second_run_changes_nothing(self):
        self.run_job()
        before = len(self.writes())
        self.run_job()
        self.assertEqual(len(self.writes()), before)
        self.assertEqual(self.lines[-1], "PARTNER_STAFF_PORTAL: already active")

    def test_hand_made_active_partner_is_accepted(self):
        self.pm.partners["PARTNER_STAFF_PORTAL"] = {"partner_id": "PARTNER_STAFF_PORTAL", "status": "active",
                                                    "name": "Staff Portal (DA bulk import)"}
        self.run_job()
        self.assertEqual(self.writes(), [])

    def test_unapproved_onboarding_from_an_earlier_run_is_approved(self):
        self.pm.partners["PARTNER_STAFF_PORTAL"] = {"partner_id": "PARTNER_STAFF_PORTAL", "status": "created"}
        self.pm.requests["r1"] = {"id": "r1", "partner_id": "PARTNER_STAFF_PORTAL",
                                  "request_type": "onboarding", "status": "created"}
        self.run_job()
        self.assertEqual(self.writes(), ["/partners/requests/r1/approve"])

    def test_disabled_partner_stops_the_job(self):
        self.pm.partners["PARTNER_STAFF_PORTAL"] = {"partner_id": "PARTNER_STAFF_PORTAL", "status": "disabled"}
        with self.assertRaisesRegex(onboard.Refused, "disabled"):
            self.run_job()
        self.assertEqual(self.writes(), [])

    def test_partner_created_meanwhile_is_accepted(self):
        self.pm.race = True
        self.run_job()
        self.assertEqual(self.lines, ["PARTNER_STAFF_PORTAL: already active"])

    def test_unavailable_partner_manager_is_retried_then_gives_up(self):
        self.pm.unavailable = 1
        self.run_job()
        self.assertEqual(self.pm.partners["PARTNER_STAFF_PORTAL"]["status"], "active")
        self.pm.unavailable = 10
        with self.assertRaisesRegex(onboard.Refused, "gave up after 3 attempts"):
            self.run_job()


if __name__ == "__main__":
    unittest.main()
