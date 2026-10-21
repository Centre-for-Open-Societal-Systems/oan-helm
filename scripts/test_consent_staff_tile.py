"""Exercise the registration job over HTTP without a live IAM or Keycloak."""
import importlib.util
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs

source = Path(__file__).resolve().parents[1] / "charts/openg2p-commons-services/files/register-consent-tile.py"
spec = importlib.util.spec_from_file_location("consent_tile", source)
tile = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tile)


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.tokens = 0
        self.reject_once = False
        self.catalog = {}
        self.requests = []
        owner = self

        class Fixture(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                pass

            def do_POST(self):
                body = self.rfile.read(int(self.headers["Content-Length"]))
                owner.requests.append(self.path)
                self.send_response(401 if self.path == "/user-access/staff_portal_applications" and owner.reject_once else 200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                if self.path == "/token":
                    owner.assertEqual(parse_qs(body.decode())["client_id"], ["consent-manager"])
                    owner.assertEqual(parse_qs(body.decode())["grant_type"], ["client_credentials"])
                    owner.tokens += 1
                    self.wfile.write(json.dumps({"access_token": f"fixture-{owner.tokens}"}).encode())
                elif self.path == "/user-access/staff_portal_applications":
                    owner.assertEqual(self.headers["Authorization"], f"Bearer fixture-{owner.tokens}")
                    if owner.reject_once:
                        owner.reject_once = False
                        self.wfile.write(b'{"detail":"expired"}')
                        return
                    application = json.loads(body)
                    owner.catalog[application["application_mnemonic"]] = application
                    self.wfile.write(json.dumps({"id": 1, "application_mnemonic": application["application_mnemonic"]}).encode())
                else:
                    owner.fail("Registration must not call Keycloak admin or user role APIs")

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        base = f"http://127.0.0.1:{self.server.server_port}"
        self.config = {
            "clientId": "consent-manager", "tokenUrl": base + "/token", "iamUrl": base,
            "attempts": 2, "retrySeconds": 0,
            "application": {
                "application_mnemonic": "consent-manager", "active": True,
                "application_url": "https://consent.example.org",
                "roles": [{"role_mnemonic": "CONSENT_MANAGER_ADMIN"},
                          {"role_mnemonic": "CONSENT_MANAGER_APPROVER"}],
            },
        }

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_rerun_upserts_same_identity_without_role_grants(self):
        tile.register(self.config, "fixture-only")
        self.config["application"]["application_url"] = "https://new-consent.example.org"
        tile.register(self.config, "fixture-only")
        self.assertEqual(len(self.catalog), 1)
        self.assertEqual(self.catalog["consent-manager"]["application_url"], "https://new-consent.example.org")
        self.assertEqual(self.tokens, 2)

    def test_auth_retry_obtains_fresh_service_token(self):
        self.reject_once = True
        tile.register(self.config, "fixture-only")
        self.assertEqual(self.tokens, 2)
        self.assertIn("consent-manager", self.catalog)

    def test_client_and_tile_identity_must_match_before_http(self):
        self.config["application"]["application_mnemonic"] = "consent-manager-ui"
        with self.assertRaisesRegex(tile.RegistrationError, "mnemonic must match"):
            tile.register(self.config, "fixture-only")
        self.assertEqual(self.requests, [])


if __name__ == "__main__":
    unittest.main()
