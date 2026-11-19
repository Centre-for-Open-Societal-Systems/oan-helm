"""Exercise the aggregation staff client secret hook against a fixture Keycloak and Kubernetes API."""
import base64
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
source = ROOT / "charts/openg2p-commons-services/files/aggregation-staff-client-secret.py"
spec = importlib.util.spec_from_file_location("aggregation_staff_client_secret", source)
job = importlib.util.module_from_spec(spec)
previous_bytecode_setting = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(job)
finally:
    sys.dont_write_bytecode = previous_bytecode_setting

NS = "commons"
KEY = "AGGREGATION_LAYER_STAFF_API_CLIENT_SECRET"


def b64(value):
    return base64.b64encode(value.encode()).decode()


def succeeded(name):
    return {"metadata": {"name": name}, "status": {"succeeded": 1}}


class ClientSecretHookTests(unittest.TestCase):
    def setUp(self):
        # New Dev before the first release with the client declared: Keycloak holds the secret that
        # keycloak-init has just set from its rendered Secret; client-secrets-sync ran first and copied
        # the old one into that Secret; the runtime Secret still has the old one.
        self.keycloak_secret = "new-rendered"
        self.secrets = {
            "aggregation-layer-staff": {"client_secret": b64("old-hand-made")},
            "aggregation-api-runtime": {KEY: b64("old-hand-made"), "AGGREGATION_LAYER_STAFF_SEARCH_TICKET_SECRET": b64("t")},
        }
        self.job_states = [[succeeded("commons-services-keycloak-init-7-0b7e6b8e"),
                            succeeded("commons-services-client-secrets-sync-7"),
                            succeeded("commons-services-keycloak-init-6-aaaaaaaa")]]
        self.patches = []
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
                owner.assertEqual(self.path, "/realms/master/protocol/openid-connect/token")
                owner.assertEqual(parse_qs(self.body())["client_id"], ["admin-cli"])
                self.reply(200, {"access_token": "kc"})

            def do_GET(self):
                url = urlparse(self.path)
                if url.path.startswith("/admin/realms/staff/"):
                    owner.assertEqual(self.headers["Authorization"], "Bearer kc")
                    if url.path.endswith("/clients"):
                        owner.assertEqual(parse_qs(url.query)["clientId"], ["aggregation-layer-staff"])
                        return self.reply(200, [{"id": "c1", "clientId": "aggregation-layer-staff", "publicClient": False}])
                    return self.reply(200, {"type": "secret", "value": owner.keycloak_secret})
                owner.assertEqual(self.headers["Authorization"], "Bearer sa")
                if url.path == f"/apis/batch/v1/namespaces/{NS}/jobs":
                    states = owner.job_states.pop(0) if len(owner.job_states) > 1 else owner.job_states[0]
                    return self.reply(200, {"items": states})
                name = url.path.rsplit("/", 1)[1]
                if name in owner.secrets:
                    return self.reply(200, {"metadata": {"name": name}, "data": dict(owner.secrets[name])})
                return self.reply(404, {"reason": "NotFound"})

            def do_PATCH(self):
                owner.assertEqual(self.headers["Authorization"], "Bearer sa")
                owner.assertEqual(self.headers["Content-Type"], "application/strategic-merge-patch+json")
                body = json.loads(self.body())
                owner.patches.append((self.path, body))
                name = self.path.rsplit("/", 1)[1]
                if "/secrets/" in self.path:
                    owner.secrets[name].update(body["data"])
                self.reply(200, {})

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def run_hook(self):
        environment = {"KEYCLOAK_URL": self.base, "KEYCLOAK_USER": "admin", "KEYCLOAK_PASSWORD": "fixture",
                       "REALM": "staff", "CLIENT_ID": "aggregation-layer-staff", "NAMESPACE": NS,
                       "RELEASE": "commons-services", "REVISION": "7", "RUNTIME_SECRET": "aggregation-api-runtime",
                       "RUNTIME_KEY": KEY, "DEPLOYMENT": "commons-services-aggregation-api",
                       "KUBERNETES_API": self.base, "KUBERNETES_TOKEN": "sa", "ATTEMPTS": "5", "DELAY_SECONDS": "0"}
        if getattr(self, "sync_job", None):
            environment["SYNC_JOB"] = self.sync_job
        output = io.StringIO()
        with mock.patch.dict(os.environ, environment, clear=False), redirect_stdout(output):
            job.main()
        text = output.getvalue()
        self.assertNotIn("new-rendered", text)
        self.assertNotIn("old-hand-made", text)
        return json.loads(text.strip().splitlines()[-1])

    def value(self, secret, key):
        return base64.b64decode(self.secrets[secret][key]).decode()

    def test_an_adopted_client_gets_keycloaks_secret_in_both_secrets_and_the_api_restarts(self):
        result = self.run_hook()
        self.assertEqual(self.value("aggregation-api-runtime", KEY), "new-rendered")
        self.assertEqual(self.value("aggregation-layer-staff", "client_secret"), "new-rendered")
        self.assertEqual(self.value("aggregation-api-runtime", "AGGREGATION_LAYER_STAFF_SEARCH_TICKET_SECRET"), "t")
        restarts = [p for p, _ in self.patches if p.endswith("/deployments/commons-services-aggregation-api")]
        self.assertEqual(len(restarts), 1)
        self.assertEqual(result["secrets"]["aggregation-api-runtime"], "updated; deployment restarted")

    def test_the_next_release_changes_nothing(self):
        self.run_hook()
        self.patches.clear()
        result = self.run_hook()
        self.assertEqual(self.patches, [])
        self.assertEqual(set(result["secrets"].values()), {"unchanged"})

    def test_it_waits_for_this_releases_keycloak_init(self):
        running = {"metadata": {"name": "commons-services-keycloak-init-7-0b7e6b8e"}, "status": {"active": 1}}
        self.job_states = [[running, succeeded("commons-services-client-secrets-sync-7")]] + self.job_states
        self.run_hook()
        self.assertEqual(self.value("aggregation-api-runtime", KEY), "new-rendered")

    def test_a_sync_job_already_removed_by_its_ttl_does_not_block(self):
        self.job_states = [[succeeded("commons-services-keycloak-init-7-0b7e6b8e")]]
        self.run_hook()
        self.assertEqual(self.value("aggregation-api-runtime", KEY), "new-rendered")

    def test_a_failed_keycloak_init_leaves_the_runtime_secret_alone(self):
        failed = {"metadata": {"name": "commons-services-keycloak-init-7-0b7e6b8e"},
                  "status": {"conditions": [{"type": "Failed", "status": "True"}]}}
        self.job_states = [[failed, succeeded("commons-services-client-secrets-sync-7")]]
        with self.assertRaises(SystemExit):
            self.run_hook()
        self.assertEqual(self.patches, [])
        self.assertEqual(self.value("aggregation-api-runtime", KEY), "old-hand-made")

    def test_the_sync_job_named_by_its_inputs_is_waited_on_whatever_its_revision(self):
        # client-secrets-sync is named by the hash of its inputs: unchanged inputs keep the Job of an earlier revision.
        self.sync_job = "commons-services-client-secrets-sync-6809f1bf"
        running = {"metadata": {"name": self.sync_job}, "status": {"active": 1}}
        self.job_states = [[succeeded("commons-services-keycloak-init-7-0b7e6b8e"), running],
                           [succeeded("commons-services-keycloak-init-7-0b7e6b8e"), succeeded(self.sync_job)]]
        self.run_hook()
        self.assertEqual(self.value("aggregation-api-runtime", KEY), "new-rendered")

    def test_a_failed_sync_job_named_by_its_inputs_leaves_the_runtime_secret_alone(self):
        self.sync_job = "commons-services-client-secrets-sync-6809f1bf"
        failed = {"metadata": {"name": self.sync_job}, "status": {"conditions": [{"type": "Failed", "status": "True"}]}}
        self.job_states = [[succeeded("commons-services-keycloak-init-7-0b7e6b8e"), failed,
                            succeeded("commons-services-client-secrets-sync-7")]]
        with self.assertRaises(SystemExit):
            self.run_hook()
        self.assertEqual(self.patches, [])

    def test_an_earlier_revisions_jobs_are_not_waited_on(self):
        self.job_states = [[succeeded("commons-services-keycloak-init-6-aaaaaaaa")]]
        with self.assertRaises(SystemExit):
            self.run_hook()
        self.assertEqual(self.patches, [])


if __name__ == "__main__":
    unittest.main()
