import base64
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("vendor_subchart_under_test", ROOT / "scripts/ci/vendor_subchart.py")
vendor_subchart = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vendor_subchart)

COMMONS = ROOT / "charts/openg2p-commons-services"
PARENT = "charts/openg2p-commons-services"


class LockDigest(unittest.TestCase):
    def test_matches_the_digest_helm_wrote_for_commons(self):
        lock = (COMMONS / "Chart.lock").read_text(encoding="utf-8")
        recorded = next(line for line in lock.splitlines() if line.startswith("digest: "))[len("digest: "):]
        self.assertEqual(vendor_subchart.lock_digest((COMMONS / "Chart.yaml").read_text(encoding="utf-8"), lock),
                         recorded)

    def test_refuses_fields_it_cannot_hash_like_helm(self):
        chart = "dependencies:\n- name: a\n  repository: r\n  tags:\n  - x\n"
        with self.assertRaises(ValueError):
            vendor_subchart.lock_digest(chart, "dependencies:\n- name: a\n  repository: r\n")


class Bump(unittest.TestCase):
    def setUp(self):
        self.chart = (COMMONS / "Chart.yaml").read_text(encoding="utf-8")
        self.lock = (COMMONS / "Chart.lock").read_text(encoding="utf-8")

    def test_changes_only_that_dependency_and_reseals_the_lock(self):
        # Whatever version is bundled now: the pipeline's pull requests move it.
        current = vendor_subchart.dependency_version(self.chart, "oan-aggregation-api")
        chart, lock = vendor_subchart.bump(self.chart, self.lock, "oan-aggregation-api", "0.0.0-develop.99")
        self.assertEqual(vendor_subchart.dependency_version(chart, "oan-aggregation-api"), "0.0.0-develop.99")
        self.assertEqual(vendor_subchart.dependency_version(lock, "oan-aggregation-api"), "0.0.0-develop.99")
        changed = [(a, b) for a, b in zip(self.chart.split("\n"), chart.split("\n")) if a != b]
        self.assertEqual(changed, [("  version: " + current, "  version: 0.0.0-develop.99")])
        digest = next(l for l in lock.splitlines() if l.startswith("digest: "))[len("digest: "):]
        self.assertEqual(digest, vendor_subchart.lock_digest(chart, lock))
        self.assertNotEqual(digest, vendor_subchart.lock_digest(self.chart, self.lock))

    def test_other_dependencies_keep_their_versions(self):
        chart, lock = vendor_subchart.bump(self.chart, self.lock, "oan-aggregation-api", "0.0.0-develop.99")
        for text in (chart, lock):
            self.assertEqual(vendor_subchart.dependency_version(text, "openg2p-master-data"), "0.0.0-develop.121")

    def test_a_chart_the_parent_does_not_depend_on_is_refused(self):
        with self.assertRaises(ValueError):
            vendor_subchart.bump(self.chart, self.lock, "oan-unknown", "0.0.0-develop.1")


class FakeGitHub:
    """The GitHub API calls the script makes, against an in-memory main branch."""

    def __init__(self, chart, lock, files, branches=(), pulls=()):
        self.files = {PARENT + "/Chart.yaml": chart, PARENT + "/Chart.lock": lock}
        self.listing = [{"name": n, "path": PARENT + "/charts/" + n, "type": "file"} for n in files]
        self.branches = set(branches)
        self.pulls = [dict(p) for p in pulls]
        self.writes = []

    def __call__(self, method, path, body=None):
        if method != "GET":
            self.writes.append((method, path, body))
        if method == "GET" and path.startswith("contents/%s/charts?" % PARENT):
            return self.listing
        if method == "GET" and path.startswith("contents/"):
            return {"content": base64.b64encode(self.files[path[len("contents/"):].split("?")[0]].encode()).decode()}
        if method == "GET" and path.startswith("git/ref/heads/"):
            branch = path[len("git/ref/heads/"):]
            if branch == "main":
                return {"object": {"sha": "main-sha"}}
            if branch in self.branches:
                return {"object": {"sha": "x"}}
            raise vendor_subchart.NotFound(path)
        if method == "GET" and path == "git/commits/main-sha":
            return {"tree": {"sha": "main-tree"}}
        if method == "GET" and path.startswith("pulls?"):
            return self.pulls
        if method == "POST" and path == "git/blobs":
            return {"sha": "blob-%d" % len(self.writes)}
        if method == "POST" and path == "git/trees":
            return {"sha": "new-tree"}
        if method == "POST" and path == "git/commits":
            return {"sha": "new-commit"}
        if method == "POST" and path == "pulls":
            return {"number": 77, "html_url": "https://github.com/x/pull/77"}
        if method in ("POST", "PATCH", "DELETE"):
            return {}
        raise AssertionError("unexpected call %s %s" % (method, path))

    def written(self, method, path):
        return [body for m, p, body in self.writes if m == method and p == path]


class Main(unittest.TestCase):
    def setUp(self):
        self.chart = (COMMONS / "Chart.yaml").read_text(encoding="utf-8")
        self.lock = (COMMONS / "Chart.lock").read_text(encoding="utf-8")
        self.current = vendor_subchart.dependency_version(self.chart, "oan-aggregation-api")
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.archive = Path(tmp.name) / "oan-aggregation-api-0.0.0-develop.42.tgz"
        self.archive.write_bytes(b"chart bytes")
        env = mock.patch.dict(os.environ, {"GH_TOKEN": "t"}, clear=False)
        env.start()
        self.addCleanup(env.stop)
        os.environ.pop("DRY_RUN", None)

    def github(self, **kwargs):
        files = ["openg2p-master-data-0.0.0-develop.121.tgz", "oan-aggregation-api-%s.tgz" % self.current]
        return FakeGitHub(self.chart, self.lock, files, **kwargs)

    def run_main(self, github, archive=None):
        with mock.patch.object(vendor_subchart, "github_api", return_value=github):
            return vendor_subchart.main(["--parent", "openg2p-commons-services", str(archive or self.archive)])

    def test_opens_a_pull_request_that_swaps_the_archive_and_bumps_the_parent(self):
        github = self.github()
        self.assertEqual(self.run_main(github), 0)
        blobs = github.written("POST", "git/blobs")
        self.assertIn({"content": base64.b64encode(b"chart bytes").decode(), "encoding": "base64"}, blobs)
        tree = github.written("POST", "git/trees")[0]
        self.assertEqual(tree["base_tree"], "main-tree")
        entries = {e["path"]: e for e in tree["tree"]}
        self.assertEqual(sorted(entries), sorted([
            PARENT + "/Chart.yaml", PARENT + "/Chart.lock",
            PARENT + "/charts/oan-aggregation-api-%s.tgz" % self.current,
            PARENT + "/charts/oan-aggregation-api-0.0.0-develop.42.tgz"]))
        self.assertIsNone(entries[PARENT + "/charts/oan-aggregation-api-%s.tgz" % self.current]["sha"])
        chart = next(b["content"] for b in blobs if b["content"].startswith("annotations:"))
        self.assertEqual(vendor_subchart.dependency_version(chart, "oan-aggregation-api"), "0.0.0-develop.42")
        self.assertEqual(github.written("POST", "git/commits")[0]["parents"], ["main-sha"])
        self.assertEqual(github.written("POST", "git/refs"),
                         [{"ref": "refs/heads/vendor/oan-aggregation-api-0.0.0-develop.42", "sha": "new-commit"}])
        pull = github.written("POST", "pulls")[0]
        self.assertEqual((pull["head"], pull["base"]), ("vendor/oan-aggregation-api-0.0.0-develop.42", "main"))

    def test_an_older_open_proposal_for_the_chart_is_closed_as_superseded(self):
        pulls = [{"number": 5, "head": {"ref": "vendor/oan-aggregation-api-0.0.0-develop.40"}},
                 {"number": 6, "head": {"ref": "vendor/openg2p-master-data-0.0.0-develop.119"}},
                 {"number": 7, "head": {"ref": "feature/other"}}]
        github = self.github(pulls=pulls)
        self.assertEqual(self.run_main(github), 0)
        self.assertEqual(github.written("PATCH", "pulls/5"), [{"state": "closed"}])
        self.assertEqual(github.written("PATCH", "pulls/6") + github.written("PATCH", "pulls/7"), [])
        self.assertEqual(len(github.written("DELETE", "git/refs/heads/vendor/oan-aggregation-api-0.0.0-develop.40")), 1)

    def test_the_version_already_bundled_changes_nothing(self):
        archive = self.archive.with_name("oan-aggregation-api-%s.tgz" % self.current)
        archive.write_bytes(b"x")
        github = self.github()
        self.assertEqual(self.run_main(github, archive), 4)
        self.assertEqual(github.writes, [])

    def test_a_version_already_proposed_changes_nothing(self):
        github = self.github(branches={"vendor/oan-aggregation-api-0.0.0-develop.42"})
        self.assertEqual(self.run_main(github), 4)
        self.assertEqual(github.writes, [])

    def test_a_parent_without_the_dependency_is_bad_input(self):
        archive = self.archive.with_name("oan-unknown-0.0.0-develop.1.tgz")
        archive.write_bytes(b"x")
        github = self.github()
        self.assertEqual(self.run_main(github, archive), 2)
        self.assertEqual(github.writes, [])

    def test_no_token(self):
        os.environ.pop("GH_TOKEN")
        self.assertEqual(vendor_subchart.main(["--parent", "openg2p-commons-services", str(self.archive)]), 3)

    def test_not_an_archive_name(self):
        bad = self.archive.with_name("chart.tgz")
        bad.write_bytes(b"x")
        self.assertEqual(vendor_subchart.main(["--parent", "openg2p-commons-services", str(bad)]), 2)


if __name__ == "__main__":
    unittest.main()
