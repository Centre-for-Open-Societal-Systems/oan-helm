"""Commons setup hooks re-run only when their inputs changed (charts/openg2p-commons-services/templates/_hook_stamps.tpl).

Client-side renders have no lookup, so the live stamps are stood in for by hookStamps.renderTestStamps.
"""
import importlib.util
import io
import json
import os
import shutil
import subprocess
import tempfile
import threading
import unittest
from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest import mock

import yaml

ROOT = Path(__file__).resolve().parents[1]
CHART = ROOT / "charts/openg2p-commons-services"
VALUES = ROOT / "environments/dev/values/commons-services.yaml"
HELM = os.environ.get("HELM") or shutil.which("helm")
RELEASE = "commons-services"
WRITER = f"{RELEASE}-hook-stamps"
ROLLOUT = f"{RELEASE}-configmap-change-pod-rollout"
STAMPED = ("aggregation-staff-client-secret", "aggregation-staff-grant", "consent-staff-portal-tile", "iam-bene-portal-api",
           "iam-login-provider-issuer-sync", "keycloak-public-client-urls", "mock-identities")


def render(values=None):
    command = [HELM, "template", RELEASE, str(CHART), "-n", "commons", "-f", str(VALUES)]
    with tempfile.TemporaryDirectory() as tmp:
        if values:
            extra = Path(tmp) / "values.yaml"
            extra.write_text(yaml.safe_dump(values), encoding="utf-8")
            command += ["-f", str(extra)]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=300)
    if result.returncode:
        raise AssertionError(result.stderr)
    return [d for d in yaml.safe_load_all(result.stdout) if d]


def hooks(docs):
    return {(d["kind"], d["metadata"]["name"]) for d in docs if "helm.sh/hook" in (d["metadata"].get("annotations") or {})}


def stamps(docs):
    """The {hook: sha256} the stamp writer records, or None when it is not rendered."""
    writer = [d for d in docs if d["kind"] == "Job" and d["metadata"]["name"] == WRITER]
    if not writer:
        return None
    env = {e["name"]: e for e in writer[0]["spec"]["template"]["spec"]["containers"][0]["env"]}
    return json.loads(env["STAMPS"]["value"])


def ours(names):
    """The hook documents rendered by the stamped templates (their names start with the hook's)."""
    return {n for n in names if any(n[1].startswith(f"{RELEASE}-{hook}") for hook in STAMPED)}


@unittest.skipUnless(HELM, "helm is not installed")
class HookStampRenders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.first = render()
        cls.recorded = stamps(cls.first)

    def test_without_stamps_every_hook_renders_and_is_recorded(self):
        self.assertTrue(self.recorded)
        self.assertLessEqual(set(self.recorded), set(STAMPED))
        self.assertTrue(all(len(h) == 64 for h in self.recorded.values()))
        self.assertTrue(ours(hooks(self.first)))

    def test_matching_stamps_skip_our_hooks_and_the_writer_but_not_the_rollout(self):
        second = render({"hookStamps": {"renderTestStamps": self.recorded}})
        self.assertEqual(ours(hooks(second)), set())
        self.assertIsNone(stamps(second))
        self.assertIn(("Job", ROLLOUT), hooks(second))
        # Upstream hooks are not ours to skip.
        self.assertEqual(hooks(self.first) - ours(hooks(self.first)) - {("Job", WRITER)}, hooks(second))

    def test_plain_resources_of_a_skipped_hook_stay_so_nothing_is_pruned(self):
        second = render({"hookStamps": {"renderTestStamps": self.recorded}})
        plain = lambda docs: {(d["kind"], d["metadata"]["name"]) for d in docs} - hooks(docs)
        self.assertEqual(plain(self.first), plain(second))

    def test_a_changed_input_reruns_only_that_hook(self):
        values = {"hookStamps": {"renderTestStamps": self.recorded},
                  "keycloakPublicClientUrls": {"extraClients": [{"realm": "staff", "clientId": "x-ui",
                                                                 "redirectUris": ["https://x.example/*"],
                                                                 "webOrigins": ["https://x.example"]}]}}
        changed = render(values)
        self.assertEqual(ours(hooks(changed)), {("Job", f"{RELEASE}-keycloak-public-client-urls")})
        self.assertEqual(set(stamps(changed)), {"keycloak-public-client-urls"})
        self.assertNotEqual(stamps(changed)["keycloak-public-client-urls"], self.recorded["keycloak-public-client-urls"])

    def test_force_and_force_all(self):
        forced = render({"hookStamps": {"renderTestStamps": self.recorded, "force": ["aggregation-staff-grant"]}})
        self.assertEqual(set(stamps(forced)), {"aggregation-staff-grant"})
        everything = render({"hookStamps": {"renderTestStamps": self.recorded, "forceAll": True}})
        self.assertEqual(ours(hooks(everything)), ours(hooks(self.first)))

    def test_disabled_stamps_render_every_hook_and_no_stamp_resources(self):
        off = render({"hookStamps": {"enabled": False, "renderTestStamps": self.recorded}})
        self.assertEqual(ours(hooks(off)), ours(hooks(self.first)))
        self.assertFalse([d for d in off if d["metadata"]["name"].startswith(WRITER)])

    def test_the_stamp_configmap_keeps_what_the_writer_recorded(self):
        (configmap,) = [d for d in self.first if d["kind"] == "ConfigMap" and d["metadata"]["name"] == WRITER]
        self.assertEqual(configmap["metadata"]["annotations"]["helm.sh/resource-policy"], "keep")
        (role,) = [d for d in self.first if d["kind"] == "Role" and d["metadata"]["name"] == WRITER]
        self.assertEqual(role["rules"], [{"apiGroups": [""], "resources": ["configmaps"],
                                          "resourceNames": [WRITER], "verbs": ["get", "patch"]}])
        (writer,) = [d for d in self.first if d["kind"] == "Job" and d["metadata"]["name"] == WRITER]
        self.assertEqual(writer["metadata"]["annotations"]["helm.sh/hook-weight"], "100")
        weights = [int(d["metadata"]["annotations"].get("helm.sh/hook-weight", "0")) for d in self.first
                   if d is not writer and "post-upgrade" in (d["metadata"].get("annotations") or {}).get("helm.sh/hook", "")]
        self.assertLess(max(weights), 100)

    def test_the_revision_is_not_an_input(self):
        (job,) = [d for d in self.first if d["kind"] == "Job" and d["metadata"]["name"] == f"{RELEASE}-aggregation-staff-client-secret"]
        env = {e["name"]: e["value"] for e in job["spec"]["template"]["spec"]["containers"][0]["env"] if "value" in e}
        self.assertEqual(env["SYNC_JOB"], self.plain_job("client-secrets-sync"))
        source = (CHART / "templates/aggregation-staff-client-secret.yaml").read_text(encoding="utf-8")
        revision = [line for line in source.splitlines() if "name: REVISION" in line]
        self.assertEqual(len(revision), 1)
        self.assertTrue(revision[0].rstrip().endswith("# oan-hook-volatile"))

    def plain_job(self, name):
        (job,) = [d["metadata"]["name"] for d in self.first if d["kind"] == "Job" and d["metadata"]["name"].startswith(f"{RELEASE}-{name}-")]
        return job

    def test_plain_jobs_are_named_by_their_inputs_and_kept(self):
        for name in ("client-secrets-sync", "websub-topics"):
            job_name = self.plain_job(name)
            self.assertRegex(job_name, rf"^{RELEASE}-{name}-[0-9a-f]{{8}}$")
            (job,) = [d for d in self.first if d["metadata"]["name"] == job_name]
            self.assertNotIn("ttlSecondsAfterFinished", job["spec"])
        again = render()
        self.assertEqual(self.plain_job("websub-topics"),
                         [d["metadata"]["name"] for d in again if d["metadata"]["name"].startswith(f"{RELEASE}-websub-topics-")][0])
        topics = render({"websubTopicProvisioning": {"topics": ["registered-websub-topics"]}})
        self.assertNotIn(self.plain_job("websub-topics"), {d["metadata"]["name"] for d in topics})


source = CHART / "files/hook-stamps.py"
spec = importlib.util.spec_from_file_location("hook_stamps", source)
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)


class StampWriter(unittest.TestCase):
    def setUp(self):
        self.data = {"mock-identities": "a" * 64}
        self.requests = []
        owner = self

        class Fixture(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                pass

            def do_PATCH(self):
                owner.requests.append((self.path, self.headers["Content-Type"], self.headers["Authorization"]))
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                owner.data.update(body["data"])
                reply = json.dumps({"data": owner.data}).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(reply)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Fixture)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def write(self, stamps):
        environment = {"STAMPS": json.dumps(stamps), "NAMESPACE": "commons", "CONFIGMAP": WRITER,
                       "KUBERNETES_API": f"http://127.0.0.1:{self.server.server_port}", "KUBERNETES_TOKEN": "sa"}
        with mock.patch.dict(os.environ, environment), redirect_stdout(io.StringIO()) as output:
            writer.main()
        return output.getvalue()

    def test_only_the_hooks_that_ran_are_recorded_and_the_others_kept(self):
        self.write({"aggregation-staff-grant": "b" * 64})
        self.assertEqual(self.data, {"mock-identities": "a" * 64, "aggregation-staff-grant": "b" * 64})
        self.assertEqual(self.requests, [(f"/api/v1/namespaces/commons/configmaps/{WRITER}",
                                          "application/merge-patch+json", "Bearer sa")])

    def test_a_malformed_stamp_is_refused_before_any_write(self):
        with self.assertRaises(SystemExit):
            self.write({"aggregation-staff-grant": "not-a-hash"})
        self.assertEqual(self.requests, [])


if __name__ == "__main__":
    unittest.main()
