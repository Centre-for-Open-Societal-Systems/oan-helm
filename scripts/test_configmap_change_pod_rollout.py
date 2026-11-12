"""Exercise the ConfigMap-change rollout job against a fixture Kubernetes API."""
import contextlib
import copy
import importlib.util
import io
import json
import os
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "charts/openg2p-commons-services/files/configmap-change-pod-rollout.py"
spec = importlib.util.spec_from_file_location("configmap_change_pod_rollout", source)
job = importlib.util.module_from_spec(spec)
previous_bytecode_setting = sys.dont_write_bytecode
try:
    sys.dont_write_bytecode = True
    spec.loader.exec_module(job)
finally:
    sys.dont_write_bytecode = previous_bytecode_setting

NS = "commons"
APPS = f"/apis/apps/v1/namespaces/{NS}/deployments/"
CMS = f"/api/v1/namespaces/{NS}/configmaps/"


def deployment(configmap):
    return {"spec": {"template": {"metadata": {"labels": {"app": "awe-ui"}}, "spec": {
        "containers": [{"name": "ui", "envFrom": [{"configMapRef": {"name": "env-" + configmap}}]}],
        "volumes": [{"name": "config", "configMap": {"name": configmap}}]}}}}


class RolloutTests(unittest.TestCase):
    def setUp(self):
        self.deployments = {"commons-services-awe-ui": deployment("awe-ui-config")}
        self.configmaps = {"awe-ui-config": {"data": {"config.json": '{"issuer": "https://keycloak.qa/realms/staff"}'}},
                           "env-awe-ui-config": {"data": {"BASE": "/"}}}
        self.patches = []
        owner = self

        class Fixture(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                pass

            def reply(self, status, body=None):
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(body or {}).encode())

            def do_GET(self):
                owner.assertEqual(self.headers["Authorization"], "Bearer fixture-token")
                if self.path.startswith(APPS):
                    found = owner.deployments.get(self.path[len(APPS):])
                elif self.path.startswith(CMS):
                    found = owner.configmaps.get(self.path[len(CMS):])
                else:
                    found = None
                self.reply(200, found) if found is not None else self.reply(404)

            def do_PATCH(self):
                owner.assertEqual(self.headers["Content-Type"], "application/strategic-merge-patch+json")
                name = self.path[len(APPS):]
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                owner.patches.append((name, body))
                annotations = body["spec"]["template"]["metadata"]["annotations"]
                meta = owner.deployments[name]["spec"]["template"]["metadata"]
                meta.setdefault("annotations", {}).update(annotations)
                self.reply(200, owner.deployments[name])

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        sa = tempfile.TemporaryDirectory()
        self.addCleanup(sa.cleanup)
        Path(sa.name, "token").write_text("fixture-token\n", encoding="utf-8")
        job.API = f"http://127.0.0.1:{self.server.server_port}"
        job.SA = sa.name

    def run_job(self, *names):
        env = {"NAMESPACE": NS, "DEPLOYMENTS": json.dumps(list(names))}
        out = io.StringIO()
        with mock.patch.dict(os.environ, env), contextlib.redirect_stdout(out):
            self.assertEqual(job.main(), 0)
        return out.getvalue()

    def checksum(self, name="commons-services-awe-ui"):
        return self.deployments[name]["spec"]["template"]["metadata"]["annotations"][job.ANNOTATION]

    def test_first_run_stamps_the_checksum_and_rolls_once(self):
        out = self.run_job("commons-services-awe-ui")
        self.assertEqual(len(self.patches), 1)
        self.assertIn("none -> ", out)
        first = self.checksum()
        self.assertEqual(len(first), 64)

    def test_unchanged_configmaps_do_not_roll_again(self):
        self.run_job("commons-services-awe-ui")
        out = self.run_job("commons-services-awe-ui")
        self.assertEqual(len(self.patches), 1)
        self.assertIn("ConfigMaps unchanged, not rolled", out)

    def test_a_changed_configmap_rolls_the_pods(self):
        self.run_job("commons-services-awe-ui")
        first = self.checksum()
        self.configmaps["awe-ui-config"]["data"]["config.json"] = '{"issuer": "https://keycloak.other/realms/staff"}'
        self.run_job("commons-services-awe-ui")
        self.assertEqual(len(self.patches), 2)
        self.assertNotEqual(self.checksum(), first)

    def test_env_from_configmaps_count_too(self):
        self.run_job("commons-services-awe-ui")
        first = self.checksum()
        self.configmaps["env-awe-ui-config"]["data"]["BASE"] = "/awe"
        self.run_job("commons-services-awe-ui")
        self.assertNotEqual(self.checksum(), first)

    def test_a_missing_deployment_is_skipped(self):
        out = self.run_job("commons-services-cm-ui", "commons-services-awe-ui")
        self.assertIn("commons-services-cm-ui: no such Deployment, skipped", out)
        self.assertEqual([name for name, _ in self.patches], ["commons-services-awe-ui"])

    def test_only_the_annotation_is_patched(self):
        before = copy.deepcopy(self.deployments["commons-services-awe-ui"])
        self.run_job("commons-services-awe-ui")
        _, body = self.patches[0]
        self.assertEqual(body, {"spec": {"template": {"metadata": {"annotations": {job.ANNOTATION: self.checksum()}}}}})
        after = self.deployments["commons-services-awe-ui"]
        after["spec"]["template"]["metadata"].pop("annotations")
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
