import importlib.util
import io
import os
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parent / "ci" / "publish_chart.py"
spec = importlib.util.spec_from_file_location("publish_chart", SCRIPT)
publish_chart = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publish_chart)


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

    def test_already_published_is_not_retried(self):
        self.assertEqual(self.run_with(http_error(422)), (4, 1))

    def test_other_refusals_are_not_retried(self):
        self.assertEqual(self.run_with(http_error(403)), (1, 1))


if __name__ == "__main__":
    unittest.main()
