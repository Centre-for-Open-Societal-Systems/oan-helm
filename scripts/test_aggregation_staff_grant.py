"""Exercise the aggregation staff grant job against a fixture Keycloak admin API."""
import importlib.util
import io
import json
import os
import sys
import threading
import unittest
from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest import mock
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "charts/openg2p-commons-services/files/aggregation-staff-grant.py"
spec = importlib.util.spec_from_file_location("aggregation_staff_grant", source)
job = importlib.util.module_from_spec(spec)
previous_bytecode_setting = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(job)
finally:
    sys.dont_write_bytecode = previous_bytecode_setting

ROLE = "AGGREGATION_STAFF_VIEWER"
PREFIX = "/admin/realms/staff"


class AggregationStaffGrantTests(unittest.TestCase):
    def setUp(self):
        self.roles = {"offline_access": {"id": "r0", "name": "offline_access"}}
        self.users = [
            {"id": "u1", "username": "nina.patel"},
            {"id": "u2", "username": "admin"},
            {"id": "s1", "username": "service-account-x", "serviceAccountClientId": "x"},
        ]
        self.mappings = {"u1": [self.roles["offline_access"]], "u2": []}
        self.writes = []
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

            def body(self):
                return self.rfile.read(int(self.headers["Content-Length"])).decode()

            def do_POST(self):
                if self.path == "/realms/master/protocol/openid-connect/token":
                    owner.assertEqual(parse_qs(self.body())["client_id"], ["admin-cli"])
                    return self.reply(200, {"access_token": "fixture"})
                owner.assertEqual(self.headers["Authorization"], "Bearer fixture")
                payload = json.loads(self.body())
                owner.writes.append((self.path, payload))
                if self.path == f"{PREFIX}/roles":
                    owner.roles[payload["name"]] = {"id": "r-new", **payload}
                    return self.reply(201)
                user_id = self.path.split("/")[-3]
                owner.mappings[user_id] += [owner.roles[r["name"]] for r in payload]
                return self.reply(204)

            def do_GET(self):
                owner.assertEqual(self.headers["Authorization"], "Bearer fixture")
                url = urlparse(self.path)
                if url.path.startswith(f"{PREFIX}/roles/"):
                    role = owner.roles.get(url.path.rsplit("/", 1)[1])
                    return self.reply(200, role) if role else self.reply(404, {"error": "Could not find role"})
                if url.path == f"{PREFIX}/users":
                    query = parse_qs(url.query)
                    owner.assertEqual(query["exact"], ["true"])
                    return self.reply(200, [u for u in owner.users if u["username"] == query["username"][0]])
                user_id = url.path.split("/")[-3]
                return self.reply(200, owner.mappings[user_id])

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def run_job(self, users):
        environment = {"KEYCLOAK_URL": self.base, "KEYCLOAK_USER": "admin", "KEYCLOAK_PASSWORD": "fixture",
                       "REALM": "staff", "ROLE": ROLE, "ROLE_DESCRIPTION": "Search", "USERS": users,
                       "TOKEN_ATTEMPTS": "1", "TOKEN_DELAY_SECONDS": "0"}
        output = io.StringIO()
        with mock.patch.dict(os.environ, environment, clear=False), redirect_stdout(output):
            job.main()
        return json.loads(output.getvalue().strip().splitlines()[-1])

    def test_creates_the_missing_role_and_grants_it_keeping_other_roles(self):
        result = self.run_job("nina.patel admin nina.patel")
        self.assertEqual(result["users"], {"nina.patel": "granted", "admin": "granted"})
        self.assertEqual(self.writes[0], (f"{PREFIX}/roles", {"name": ROLE, "description": "Search"}))
        self.assertEqual({r["name"] for r in self.mappings["u1"]}, {"offline_access", ROLE})
        self.assertEqual([r["name"] for r in self.mappings["u2"]], [ROLE])

    def test_a_second_run_changes_nothing(self):
        self.run_job("nina.patel")
        writes = len(self.writes)
        self.assertEqual(self.run_job("nina.patel")["users"], {"nina.patel": "unchanged"})
        self.assertEqual(len(self.writes), writes)

    def test_an_unknown_name_or_a_service_account_grants_nobody(self):
        for users in ("nina.patel nobody", "nina.patel service-account-x"):
            with self.subTest(users=users), self.assertRaises(SystemExit):
                self.run_job(users)
        self.assertNotIn(ROLE, {r["name"] for r in self.mappings["u1"]})
        self.assertTrue(all(path == f"{PREFIX}/roles" for path, _ in self.writes))


if __name__ == "__main__":
    unittest.main()
