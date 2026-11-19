import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_chart_under_test", ROOT / "scripts/ci/package_chart.py")
package_chart = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(package_chart)

VALUES = """global:
  name: x
registry:
  # the staff API
  staffApi:
    image:
      repository: old/staff-api
      # pinned by the build
      tag: develop-1
    envVars:
      image: other
  partnerApi:
    image:
      repository: old/partner-api
      tag: develop-1
dashboardUi:
  image:
    repository: ''
    tag: ''
"""


class SetImageTests(unittest.TestCase):
    def test_only_the_named_image_changes(self):
        result = package_chart.set_image(VALUES, "registry.staffApi.image", "new/staff-api", "abc@sha256:1")
        self.assertIn('      repository: "new/staff-api"\n      # pinned by the build\n      tag: "abc@sha256:1"\n', result)
        self.assertIn("repository: old/partner-api\n      tag: develop-1\n", result)
        self.assertIn("      image: other\n", result)

    def test_a_digest_of_its_own_follows_the_new_tag(self):
        values = "dashboardApi:\n  enabled: false\n  image:\n    digest: sha256:old\n    repository: old/api\n    tag: develop-1\n  replicas: 1\n"
        result = package_chart.set_image(values, "dashboardApi.image", "new/api", "develop-2@sha256:new")
        self.assertIn('    digest: "sha256:new"\n    repository: "new/api"\n    tag: "develop-2@sha256:new"\n', result)

    def test_a_tag_without_a_digest_clears_an_old_digest(self):
        values = "api:\n  image:\n    repository: old/api\n    tag: develop-1\n    digest: sha256:old\n"
        result = package_chart.set_image(values, "api.image", "new/api", "develop-2")
        self.assertIn('    digest: ""\n', result)

    def test_empty_values_are_filled(self):
        result = package_chart.set_image(VALUES, "dashboardUi.image", "new/ui", "abc")
        self.assertIn('  image:\n    repository: "new/ui"\n    tag: "abc"\n', result)

    def test_a_missing_path_is_refused(self):
        with self.assertRaises(ValueError):
            package_chart.set_image(VALUES, "registry.beneApi.image", "new/x", "abc")

    def test_a_nested_key_is_not_taken_for_a_direct_one(self):
        with self.assertRaises(ValueError):
            package_chart.set_image(VALUES, "registry.image", "new/x", "abc")

    def test_a_block_without_repository_is_refused(self):
        with self.assertRaises(ValueError):
            package_chart.set_image(VALUES, "registry.staffApi.envVars", "new/x", "abc")


class ImagesFileTests(unittest.TestCase):
    def test_lines_are_read(self):
        self.assertEqual(package_chart.read_images("a.image\trepo\ttag\n\n"), [["a.image", "repo", "tag"]])

    def test_a_short_line_is_refused(self):
        with self.assertRaises(ValueError):
            package_chart.read_images("a.image\trepo\n")

    def test_no_images_is_refused(self):
        with self.assertRaises(ValueError):
            package_chart.read_images("\n")


class AnnotateTests(unittest.TestCase):
    def test_values_are_quoted(self):
        text = package_chart.annotate("name: x\nannotations:\n  a: b\n", {"oan.org/source-subject": 'Say "hi"'})
        self.assertEqual(text, 'name: x\nannotations:\n  oan.org/source-subject: "Say \\"hi\\""\n  a: b\n')

    def test_a_chart_without_annotations_is_refused(self):
        with self.assertRaises(ValueError):
            package_chart.annotate("name: x\n", {"a": "b"})


class LeftoverTests(unittest.TestCase):
    def test_an_old_lock_and_subcharts_are_removed_from_the_copy(self):
        with tempfile.TemporaryDirectory() as folder:
            chart = Path(folder)
            (chart / "Chart.yaml").write_text("name: x")
            (chart / "Chart.lock").write_text("old")
            (chart / "charts").mkdir()
            (chart / "charts/old.tgz").write_text("old")
            package_chart.remove_leftovers(chart)
            self.assertEqual([path.name for path in chart.iterdir()], ["Chart.yaml"])



class VersionTests(unittest.TestCase):
    def test_init_yaml_gives_the_version_and_git_is_not_asked(self):
        import os
        from unittest import mock
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, "init.yaml").write_text("version: 1.0.0\n", encoding="utf-8")
            with mock.patch.dict(os.environ, {"BUILD_NUMBER": "57"}), \
                    mock.patch.object(package_chart, "derive_version") as older:
                self.assertEqual(package_chart.chart_version("develop", folder), "1.0.0-develop.57")
            older.assert_not_called()

    def test_without_init_yaml_the_version_comes_from_git(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as folder, \
                mock.patch.object(package_chart, "derive_version", return_value="0.0.0-develop.900") as older:
            self.assertEqual(package_chart.chart_version("develop", folder), "0.0.0-develop.900")
        older.assert_called_once_with("develop")

    def test_every_image_tag_must_be_the_chart_version(self):
        digest = "@sha256:" + "a" * 64
        good = [("registry.staffApi.image", "ecr/eoan/farmer-registry/staff-api-1.2.2-rc.625", "1.0.0-develop.57" + digest)]
        package_chart.check_image_tags(good, "1.0.0-develop.57")
        bad = good + [("dashboard.image", "ecr/eoan/farmer-registry/dashboard-api", "develop-57" + digest)]
        with self.assertRaises(ValueError) as raised:
            package_chart.check_image_tags(bad, "1.0.0-develop.57")
        self.assertIn("dashboard-api:develop-57", str(raised.exception))
        self.assertNotIn("staff-api", str(raised.exception))

if __name__ == "__main__":
    unittest.main()
