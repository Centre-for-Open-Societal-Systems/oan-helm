"""Tests for scripts/ci/app_chart.py."""

import importlib.util
import io
import os
from pathlib import Path
import stat
import sys
import tarfile
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/ci"))
SPEC = importlib.util.spec_from_file_location("app_chart_under_test", ROOT / "scripts/ci/app_chart.py")
app_chart = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(app_chart)


class ChartVersionTests(unittest.TestCase):
    def test_develop_gives_app_develop_build_number(self):
        config = {"version": {"fixed": "0.0.1"}}
        env = {"BRANCH_NAME": "develop", "BUILD_NUMBER": "57"}
        self.assertEqual(app_chart.chart_version(config, Path("."), env), "0.0.1-develop.57")

    def test_any_other_branch_is_refused(self):
        config = {"version": {"fixed": "0.0.1"}}
        for branch in ["main", "feature/my-feature", "master", "release"]:
            with self.subTest(branch=branch):
                with self.assertRaises(ValueError) as ctx:
                    app_chart.chart_version(config, Path("."), {"BRANCH_NAME": branch, "BUILD_NUMBER": "1"})
                self.assertIn("only develop packages the chart", str(ctx.exception))

    def test_file_pattern_and_fixed_versions_both_work(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            # Fixed version
            self.assertEqual(
                app_chart.chart_version(
                    {"version": {"fixed": "1.2.3"}}, root, {"BRANCH_NAME": "develop", "BUILD_NUMBER": "10"}
                ),
                "1.2.3-develop.10",
            )
            # File pattern
            (root / "version.txt").write_text('__version__ = "2.3.4"\n', encoding="utf-8")
            config = {"version": {"file": "version.txt", "pattern": r'__version__ = "([^"]+)"'}}
            self.assertEqual(
                app_chart.chart_version(config, root, {"BRANCH_NAME": "develop", "BUILD_NUMBER": "10"}),
                "2.3.4-develop.10",
            )

    def test_pattern_matching_nothing_fails(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            (root / "version.txt").write_text("no version here\n", encoding="utf-8")
            config = {"version": {"file": "version.txt", "pattern": r'version = "([^"]+)"'}}
            with self.assertRaises(ValueError) as ctx:
                app_chart.chart_version(config, root, {"BRANCH_NAME": "develop", "BUILD_NUMBER": "10"})
            self.assertIn("no version matching", str(ctx.exception))


class PackageBuildTests(unittest.TestCase):
    def test_package_build_refuses_image_tag_that_is_not_chart_version(self):
        config = {
            "chart": "my-app",
            "version": {"fixed": "0.0.1"},
            "source_repository": "oan/my-app",
            "release_name": "my-app",
            "release_namespace": "default",
            "values_overlay": "dev",
            "image_path": "image",
        }
        env = {
            "BRANCH_NAME": "develop",
            "BUILD_NUMBER": "1",
            "IMAGE_TAG": "different-tag-1.0",
            "IMAGE_REPOSITORY": "repo/app",
            "SOURCE_COMMIT": "abc1234567890",
        }
        with self.assertRaises(ValueError) as ctx:
            app_chart.package_build(config, Path("."), env, Path("."))
        self.assertIn("is not the chart version", str(ctx.exception))


class PackageTests(unittest.TestCase):
    def test_package_with_standin_helm_holds_annotations_and_image(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            bin_dir = root / "bin"
            bin_dir.mkdir()

            # Stand-in helm executable
            helm = bin_dir / "helm"
            helm.write_text(
                "#!/usr/bin/env python3\n"
                "import sys, tarfile\n"
                "from pathlib import Path\n"
                "args = sys.argv[1:]\n"
                "if args[0] == 'package':\n"
                "    chart_dir = Path(args[1])\n"
                "    dest_dir = Path(args[args.index('--destination') + 1])\n"
                "    version = args[args.index('--version') + 1]\n"
                "    archive_path = dest_dir / f'{chart_dir.name}-{version}.tgz'\n"
                "    with tarfile.open(archive_path, 'w:gz') as tar:\n"
                "        tar.add(chart_dir, arcname=chart_dir.name)\n"
            )
            helm.chmod(helm.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

            # Sample chart
            chart_source = root / "helm" / "test-app"
            chart_source.mkdir(parents=True)
            (chart_source / "Chart.yaml").write_text(
                "apiVersion: v2\nname: test-app\nversion: 0.0.1\nannotations:\n  oan.org/existing: kept\n",
                encoding="utf-8",
            )
            (chart_source / "values.yaml").write_text(
                "app:\n  image:\n    repository: old/repo\n    tag: old-tag\n", encoding="utf-8"
            )

            config = {
                "chart": "test-app",
                "source_repository": "oan/test-app",
                "release_name": "test-app-rel",
                "release_namespace": "test-ns",
                "values_overlay": "dev-values",
                "image_path": "app.image",
                "version": {"fixed": "0.0.1"},
            }
            env = {
                "BRANCH_NAME": "develop",
                "BUILD_NUMBER": "42",
                "IMAGE_TAG": "0.0.1-develop.42",
                "IMAGE_REPOSITORY": "myregistry.ecr/test-app",
                "SOURCE_COMMIT": "1234567890abcdef1234567890abcdef12345678",
                "COMMIT_SUBJECT": "feat: test feature",
            }

            orig_path = os.environ.get("PATH", "")
            with mock.patch.dict(os.environ, {"PATH": f"{bin_dir}:{orig_path}"}):
                ret = app_chart.main(config, root, argv=["package"], env=env)
                self.assertEqual(ret, 0)

            archive = root / "built-chart" / "test-app-0.0.1-develop.42.tgz"
            self.assertTrue(archive.is_file())

            with tarfile.open(archive, "r:gz") as tar:
                chart_yaml = tar.extractfile("test-app/Chart.yaml").read().decode("utf-8")
                values_yaml = tar.extractfile("test-app/values.yaml").read().decode("utf-8")

            self.assertIn('oan.org/source-repository: "oan/test-app"', chart_yaml)
            self.assertIn('oan.org/source-commit: "1234567890abcdef1234567890abcdef12345678"', chart_yaml)
            self.assertIn('oan.org/release-name: "test-app-rel"', chart_yaml)
            self.assertIn('oan.org/release-namespace: "test-ns"', chart_yaml)
            self.assertIn('oan.org/values-overlay: "dev-values"', chart_yaml)

            self.assertIn('    repository: "myregistry.ecr/test-app"\n    tag: "0.0.1-develop.42"', values_yaml)


class PublishDirectoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.built_dir = self.root / "built-chart"
        self.built_dir.mkdir()
        self.archive = self.built_dir / "test-app-0.0.1-develop.1.tgz"
        self.archive.write_bytes(b"dummy archive")

    def test_no_gh_token_gives_3(self):
        code = app_chart.publish_directory({}, self.built_dir, "test-app")
        self.assertEqual(code, 3)

    def test_dry_run_publishes_nothing(self):
        with mock.patch.object(app_chart.subprocess, "run", return_value=mock.Mock(returncode=0)) as run_mock:
            code = app_chart.publish_directory({"DRY_RUN": "1"}, self.built_dir, "test-app")
            self.assertEqual(code, 0)
            self.assertEqual(run_mock.call_count, 1)

    def test_already_published_for_same_commit_gives_0(self):
        mock_sub = mock.Mock(returncode=app_chart.ALREADY_PUBLISHED)
        commit = "1234567890abcdef1234567890abcdef12345678"
        env = {"GH_TOKEN": "token", "SOURCE_COMMIT": commit}
        with mock.patch.object(app_chart.subprocess, "run", return_value=mock_sub):
            with mock.patch.object(app_chart, "published_commit", return_value=(commit, None)):
                code = app_chart.publish_directory(env, self.built_dir, "test-app")
                self.assertEqual(code, 0)

    def test_already_published_for_another_commit_gives_1(self):
        mock_sub = mock.Mock(returncode=app_chart.ALREADY_PUBLISHED)
        env = {"GH_TOKEN": "token", "SOURCE_COMMIT": "11111111111111"}
        with mock.patch.object(app_chart.subprocess, "run", return_value=mock_sub):
            with mock.patch.object(app_chart, "published_commit", return_value=("22222222222222", None)):
                code = app_chart.publish_directory(env, self.built_dir, "test-app")
                self.assertEqual(code, 1)

    def test_already_published_matches_prefix_commit_hashes(self):
        mock_sub = mock.Mock(returncode=app_chart.ALREADY_PUBLISHED)
        full_commit = "1234567890abcdef1234567890abcdef12345678"
        short_commit = "1234567"
        # Full SOURCE_COMMIT vs short published commit
        env = {"GH_TOKEN": "token", "SOURCE_COMMIT": full_commit}
        with mock.patch.object(app_chart.subprocess, "run", return_value=mock_sub):
            with mock.patch.object(app_chart, "published_commit", return_value=(short_commit, None)):
                code = app_chart.publish_directory(env, self.built_dir, "test-app")
                self.assertEqual(code, 0)

        # Short SOURCE_COMMIT vs full published commit
        env = {"GH_TOKEN": "token", "SOURCE_COMMIT": short_commit}
        with mock.patch.object(app_chart.subprocess, "run", return_value=mock_sub):
            with mock.patch.object(app_chart, "published_commit", return_value=(full_commit, None)):
                code = app_chart.publish_directory(env, self.built_dir, "test-app")
                self.assertEqual(code, 0)

    def test_already_published_read_archive_failure_gives_1_and_distinct_error(self):
        mock_sub = mock.Mock(returncode=app_chart.ALREADY_PUBLISHED)
        env = {"GH_TOKEN": "token", "SOURCE_COMMIT": "1234567890abcdef"}
        with mock.patch.object(app_chart.subprocess, "run", return_value=mock_sub):
            with mock.patch.object(app_chart, "published_commit", return_value=(None, OSError("HTTP 403 Forbidden"))):
                with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
                    code = app_chart.publish_directory(env, self.built_dir, "test-app")
                    self.assertEqual(code, 1)
                    self.assertIn("could not read the published archive", out.getvalue())
                    self.assertNotIn("already published for another commit", out.getvalue())


class MainActionTests(unittest.TestCase):
    def test_unknown_action_prints_usage_and_returns_1(self):
        config = {"chart": "test-app"}
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            code = app_chart.main(config, Path("."), argv=["unknown-action"])
            self.assertEqual(code, 1)
            self.assertIn("usage: package_chart.py", out.getvalue())

    def test_gateway_actions_only_when_config_has_gateway(self):
        config_no_gw = {"chart": "test-app"}
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            code = app_chart.main(config_no_gw, Path("."), argv=["gateway-package"])
            self.assertEqual(code, 1)
            self.assertIn("usage: package_chart.py", out.getvalue())
            self.assertNotIn("gateway-package", out.getvalue())

        config_gw = {
            "chart": "test-app",
            "gateway": {
                "chart": "test-app-gateway",
                "source": "helm/test-app-gateway",
                "release_name": "gw-rel",
                "values_overlay": "gw-overlay",
            },
        }
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            code = app_chart.main(config_gw, Path("."), argv=["invalid"])
            self.assertEqual(code, 1)
            self.assertIn("gateway-package", out.getvalue())
            self.assertIn("gateway-publish", out.getvalue())


if __name__ == "__main__":
    unittest.main()
