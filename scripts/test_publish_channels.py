import importlib.util
import io
import json
import shutil
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

import publish_channels

CI = Path(__file__).resolve().parent / "ci" / "publish_chart.py"
spec = importlib.util.spec_from_file_location("publish_chart", CI)
publish_chart = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publish_chart)


def write_archive(path, name, version):
    path.parent.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump({"apiVersion": "v2", "name": name, "version": version, "annotations": {
        "oan.org/source-repository": "example/repo", "oan.org/source-commit": "a" * 40,
        "oan.org/source-subject": "Change the form"}}).encode()
    with tarfile.open(path, "w:gz") as tar:
        info = tarfile.TarInfo(f"{name}/Chart.yaml")
        info.size = len(body)
        tar.addfile(info, io.BytesIO(body))


class PublishChannelsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "releases").mkdir()
        self.changelog = []
        for patcher in (
            mock.patch.object(publish_channels, "ROOT", self.root),
            mock.patch.object(publish_channels, "PUBLIC", self.root / "repository"),
            mock.patch.object(publish_channels, "SEALS", self.root / "releases/channels.json"),
            mock.patch.object(publish_channels, "write_changelog", self.changelog.append),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)
        self.addCleanup(self.tmp.cleanup)

    def archive(self, channel, version, name="farmer"):
        path = self.root / "repository" / channel / f"{name}-{version}.tgz"
        write_archive(path, name, version)
        return path

    def test_empty_channels_get_an_index(self):
        self.assertEqual(publish_channels.main(), [])
        for channel in publish_channels.CHANNELS:
            self.assertTrue((self.root / "repository" / channel / "index.yaml").exists())

    def test_new_archive_is_indexed_sealed_and_logged(self):
        self.archive("develop", "0.0.0-develop.7")
        published = publish_channels.main()
        self.assertEqual(len(published), 1)
        index = yaml.safe_load((self.root / "repository/develop/index.yaml").read_text())
        self.assertEqual(index["entries"]["farmer"][0]["urls"], ["farmer-0.0.0-develop.7.tgz"])
        seals = json.loads((self.root / "releases/channels.json").read_text())
        self.assertIn("develop/farmer-0.0.0-develop.7.tgz", seals)
        self.assertIn("Change the form (example/repo@aaaaaaaaaaaa)", self.changelog[0])

    def test_second_run_changes_nothing(self):
        self.archive("staging", "1.0.0-rc.9")
        publish_channels.main()
        index = (self.root / "repository/staging/index.yaml").read_bytes()
        self.assertEqual(publish_channels.main(), [])
        self.assertEqual((self.root / "repository/staging/index.yaml").read_bytes(), index)

    def test_version_must_belong_to_its_channel(self):
        self.archive("release", "1.0.0-rc.9")
        with self.assertRaisesRegex(AssertionError, "does not belong"):
            publish_channels.main()

    def test_file_name_must_match_the_chart(self):
        path = self.archive("develop", "0.0.0-develop.7")
        shutil.move(path, path.with_name("farmer-0.0.0-develop.8.tgz"))
        with self.assertRaisesRegex(AssertionError, "holds chart"):
            publish_channels.main()

    def test_published_archive_cannot_change_or_disappear(self):
        path = self.archive("release", "1.0.0")
        publish_channels.main()
        path.write_bytes(b"other")
        with self.assertRaisesRegex(AssertionError, "changed after"):
            publish_channels.main()
        path.unlink()
        with self.assertRaisesRegex(AssertionError, "must not disappear"):
            publish_channels.main()


class PublishChartTest(unittest.TestCase):
    def test_channel_follows_from_the_version(self):
        for file_name, expected in (
            ("openg2p-farmer-registry-0.0.0-develop.812.tgz", "repository/develop/"),
            ("openg2p-farmer-registry-1.0.2-rc.812.tgz", "repository/staging/"),
            ("openg2p-farmer-registry-1.0.2.tgz", "repository/release/"),
        ):
            self.assertEqual(publish_chart.target_path(file_name)[0], expected + file_name)

    def test_feature_versions_are_not_published(self):
        for file_name in ("x-0.0.0-fix-form.12.tgz", "x-1.0.0-dev.5.tgz", "readme.txt"):
            with self.assertRaises(ValueError):
                publish_chart.target_path(file_name)

    def test_missing_token_stops_before_any_request(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "x-1.0.0.tgz"
            archive.write_bytes(b"chart")
            with mock.patch.dict("os.environ", {}, clear=True), mock.patch("sys.stderr", io.StringIO()):
                self.assertEqual(publish_chart.main(["publish_chart.py", str(archive)]), 3)


if __name__ == "__main__":
    unittest.main()
