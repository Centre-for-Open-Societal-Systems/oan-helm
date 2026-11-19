import importlib.util
import io
import os
import tarfile
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent / "ci" / "publish_chart.py"
spec = importlib.util.spec_from_file_location("publish_chart", SCRIPT)
publish_chart = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publish_chart)


def chart_archive(commit):
    """A packaged chart whose Chart.yaml carries `commit` as its source-commit annotation (none when None)."""
    text = "apiVersion: v2\nname: openg2p-livestock-registry\nversion: 0.0.0-develop.452\n"
    if commit:
        text += "annotations:\n  oan.org/source-commit: %s\n" % commit
    data = text.encode("utf-8")
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as bundle:
        member = tarfile.TarInfo("openg2p-livestock-registry/Chart.yaml")
        member.size = len(data)
        bundle.addfile(member, io.BytesIO(data))
    return buffer.getvalue()


def http_error(code):
    return urllib.error.HTTPError("https://api.github.com/x", code, "status %d" % code, {}, io.BytesIO(b"{}"))


class PublishChartTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.archive = Path(tmp.name) / "openg2p-livestock-registry-0.0.0-develop.452.tgz"
        self.archive.write_bytes(b"chart")
        patches = [
            mock.patch.dict(os.environ, {"GH_TOKEN": "t"}, clear=False),
            mock.patch.object(publish_chart.time, "sleep"),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)
        os.environ.pop("DRY_RUN", None)

    def run_with(self, *outcomes):
        def urlopen(request, timeout):
            outcome = next(responses)
            if isinstance(outcome, Exception):
                raise outcome
            return outcome
        responses = iter(outcomes)
        with mock.patch.object(publish_chart.urllib.request, "urlopen", side_effect=urlopen) as opened:
            code = publish_chart.main(["publish_chart.py", str(self.archive)])
        return code, opened.call_count

    def test_conflict_is_retried_until_the_write_lands(self):
        self.assertEqual(self.run_with(http_error(409), http_error(409), object()), (0, 3))

    def test_conflict_that_never_clears_fails_after_the_attempts(self):
        code, calls = self.run_with(*[http_error(409)] * publish_chart.CONFLICT_ATTEMPTS)
        self.assertEqual((code, calls), (1, publish_chart.CONFLICT_ATTEMPTS))

    def published(self, commit):
        response = mock.Mock()
        response.read.return_value = chart_archive(commit)
        return response

    def test_a_version_published_from_the_same_commit_is_a_rerun(self):
        self.archive.write_bytes(chart_archive("a" * 40))
        self.assertEqual(self.run_with(http_error(422), self.published("a" * 40)), (4, 2))

    def test_a_version_published_from_another_commit_is_refused(self):
        self.archive.write_bytes(chart_archive("a" * 40))
        stderr = io.StringIO()
        with mock.patch.object(publish_chart.sys, "stderr", stderr):
            self.assertEqual(self.run_with(http_error(422), self.published("b" * 40)), (5, 2))
        self.assertIn("bump version in init.yaml", stderr.getvalue())

    def test_a_taken_version_that_cannot_be_compared_is_refused(self):
        self.archive.write_bytes(chart_archive(None))
        self.assertEqual(self.run_with(http_error(422), self.published(None)), (5, 2))
        self.archive.write_bytes(chart_archive("a" * 40))
        self.assertEqual(self.run_with(http_error(422), http_error(404)), (5, 2))

    def test_staging_versions_go_to_the_staging_channel(self):
        self.assertEqual(publish_chart.target_path("openg2p-farmer-registry-1.0.0-staging.12.tgz")[0],
                         "repository/staging/openg2p-farmer-registry-1.0.0-staging.12.tgz")
        self.assertEqual(publish_chart.target_path("openg2p-farmer-registry-1.0.0-rc.3.tgz")[0],
                         "repository/staging/openg2p-farmer-registry-1.0.0-rc.3.tgz")
        with self.assertRaises(ValueError):
            publish_chart.target_path("openg2p-farmer-registry-1.0.0-feature-x.3.tgz")

    def test_other_refusals_are_not_retried(self):
        self.assertEqual(self.run_with(http_error(403)), (1, 1))


if __name__ == "__main__":
    unittest.main()
