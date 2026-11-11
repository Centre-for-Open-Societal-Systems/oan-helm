"""Exercise the public-client URL job against a fixture Keycloak admin API."""
import importlib.util
import json
import sys
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "charts/openg2p-commons-services/files/keycloak-public-client-urls.py"
spec = importlib.util.spec_from_file_location("keycloak_public_client_urls", source)
job = importlib.util.module_from_spec(spec)
previous_bytecode_setting = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(job)
finally:
    sys.dont_write_bytecode = previous_bytecode_setting

OLD = "https://connector-farmer-registry.oanstaging.com"
NEW = "https://connector-farmer-registry.qa.oanstaging.com"


class PublicClientUrlTests(unittest.TestCase):
    def setUp(self):
        self.clients = {
            "registry-connector-ui": {"id": "u1", "clientId": "registry-connector-ui", "publicClient": True,
                                      "redirectUris": [OLD + "/*"], "webOrigins": [OLD], "attributes": {"keep": "me"}},
            "registry-connector": {"id": "c1", "clientId": "registry-connector", "publicClient": False,
                                   "redirectUris": [], "webOrigins": []},
        }
        self.puts = []
        owner = self

        class Fixture(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                pass

            def reply(self, status, body=None):
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                if body is not None:
                    self.wfile.write(json.dumps(body).encode())

            def do_POST(self):
                body = parse_qs(self.rfile.read(int(self.headers["Content-Length"])).decode())
                owner.assertEqual(self.path, "/realms/master/protocol/openid-connect/token")
                owner.assertEqual(body["client_id"], ["admin-cli"])
                self.reply(200, {"access_token": "fixture"})

            def do_GET(self):
                owner.assertEqual(self.headers["Authorization"], "Bearer fixture")
                url = urlparse(self.path)
                owner.assertEqual(url.path, "/admin/realms/staff/clients")
                client = owner.clients.get(parse_qs(url.query)["clientId"][0])
                self.reply(200, [client] if client else [])

            def do_PUT(self):
                owner.assertEqual(self.headers["Authorization"], "Bearer fixture")
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                owner.puts.append((self.path, body))
                owner.clients[body["clientId"]] = body
                self.reply(204)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def entry(self, client_id="registry-connector-ui", prune=False):
        return {"realm": "staff", "clientId": client_id, "redirectUris": [NEW + "/*"], "webOrigins": [NEW], "prune": prune}

    def test_adds_the_new_urls_next_to_the_old_ones_and_keeps_the_rest_of_the_client(self):
        self.assertEqual(job.reconcile(self.base, "fixture", self.entry()), "updated")
        ((path, body),) = self.puts
        self.assertEqual(path, "/admin/realms/staff/clients/u1")
        self.assertEqual(body["redirectUris"], [OLD + "/*", NEW + "/*"])
        self.assertEqual(body["webOrigins"], [OLD, NEW])
        self.assertEqual(body["attributes"], {"keep": "me"})

    def test_second_run_changes_nothing(self):
        job.reconcile(self.base, "fixture", self.entry())
        self.assertEqual(job.reconcile(self.base, "fixture", self.entry()), "unchanged")
        self.assertEqual(len(self.puts), 1)

    def test_prune_keeps_exactly_the_declared_urls(self):
        self.assertEqual(job.reconcile(self.base, "fixture", self.entry(prune=True)), "updated")
        self.assertEqual(self.clients["registry-connector-ui"]["redirectUris"], [NEW + "/*"])
        self.assertEqual(self.clients["registry-connector-ui"]["webOrigins"], [NEW])

    def test_confidential_clients_are_left_to_keycloak_init(self):
        self.assertEqual(job.reconcile(self.base, "fixture", self.entry("registry-connector")), "skipped")
        self.assertEqual(self.puts, [])

    def test_a_missing_client_is_not_created(self):
        self.assertEqual(job.reconcile(self.base, "fixture", self.entry("consent-manager-ui")), "missing")
        self.assertEqual(self.puts, [])

    def test_admin_token_from_the_master_realm(self):
        self.assertEqual(job.admin_token(self.base, "admin", "fixture-password", 1, 0), "fixture")


if __name__ == "__main__":
    unittest.main()
