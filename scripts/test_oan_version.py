import importlib.util
import io
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("oan_version_under_test", ROOT / "scripts/ci/oan_version.py")
oan_version = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(oan_version)

INIT = """# The release this repository works towards; the build adds the branch and build number.
version: 1.0.0
rpVersion: 1.2.2-rc.625   # OpenG2P registry platform
rpCommit: 0123456789abcdef0123456789abcdef01234567
"""


class OanVersionTest(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)

    def init(self, text):
        (self.root / "init.yaml").write_text(text, encoding="utf-8")

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = oan_version.main(["--root", str(self.root)] + list(argv))
        return code, out.getvalue().strip(), err.getvalue()

    def test_fields_are_read_with_comments_and_quotes(self):
        self.init(INIT.replace("1.2.2-rc.625", '"1.2.2-rc.625"'))
        self.assertEqual(oan_version.read(self.root), {
            "version": "1.0.0", "rpVersion": "1.2.2-rc.625", "rpCommit": "0123456789abcdef0123456789abcdef01234567"})

    def test_develop_and_staging_builds(self):
        self.init(INIT)
        self.assertEqual(self.run_main("--branch", "develop", "--build", "57"), (0, "1.0.0-develop.57", ""))
        self.assertEqual(self.run_main("--branch", "staging", "--build", "12")[1], "1.0.0-staging.12")

    def test_jenkins_environment_is_the_default(self):
        self.init(INIT)
        env = {"BRANCH_NAME": "develop", "BUILD_NUMBER": "212"}
        self.assertEqual(oan_version.current(self.root, env=env), "1.0.0-develop.212")
        with self.assertRaises(ValueError):
            oan_version.current(self.root, env={"BRANCH_NAME": "develop"})

    def test_other_branches_get_a_slug_no_channel_accepts(self):
        self.assertEqual(oan_version.build_version("1.0.0", "feature/G2R_Naming", "3"), "1.0.0-feature-g2r-naming.3")
        self.assertEqual(oan_version.build_version("1.0.0", "PR-42", "1"), "1.0.0-pr-42.1")
        self.assertEqual(oan_version.build_version("1.0.0", "123", "1"), "1.0.0-b123.1")

    def test_one_field(self):
        self.init(INIT)
        self.assertEqual(self.run_main("--field", "rpVersion"), (0, "1.2.2-rc.625", ""))
        self.init("version: 1.0.0\n")
        code, _, err = self.run_main("--field", "rpVersion")
        self.assertEqual(code, 1)
        self.assertIn("has no rpVersion", err)

    def test_bad_files_are_refused(self):
        for text, message in (
            ("version: 1.0.0-develop.3\n", "is not N.N.N"),
            ("version: 1.0\n", "is not N.N.N"),
            ("version: 01.0.0\n", "is not N.N.N"),
            ("rpVersion: 1.2.2\n", "has no version"),
            ("version: 1.0.0\nversion: 1.0.1\n", "twice"),
            ("version: 1.0.0\nimage:\n  tag: x\n", "is not `key: value`"),
            ("version: 1.0.0\nrpVersion: latest\n", "not a SemVer"),
            ("version: 1.0.0\nrpVersion: 1.2.2\nrpCommit: main\n", "not a git commit"),
            ("version: 1.0.0\nrpCommit: 0123abc\n", "without rpVersion"),
            ("version: 1.0.0\nchannel: develop\n", "unknown fields: channel"),
        ):
            self.init(text)
            code, out, err = self.run_main("--branch", "develop", "--build", "1")
            self.assertEqual((code, out), (1, ""), text)
            self.assertIn(message, err, text)

    def test_missing_file_and_bad_build_number(self):
        code, _, err = self.run_main("--branch", "develop", "--build", "1")
        self.assertEqual(code, 1)
        self.assertIn("init.yaml is missing", err)
        self.init(INIT)
        for build in ("0", "07", "x", "-1"):
            self.assertEqual(self.run_main("--branch", "develop", "--build", build)[0], 1, build)

    def test_semver_order(self):
        ordered = ["0.0.0-develop.893", "1.0.0-develop.9", "1.0.0-develop.10", "1.0.0-rc.553", "1.0.0-staging.1",
                   "1.0.0-staging.12", "1.0.0", "1.0.1-develop.1", "1.0.1"]
        self.assertEqual(sorted(reversed(ordered), key=oan_version.semver_key), ordered)
        self.assertEqual(oan_version.semver_key("1.0.0+build.5"), oan_version.semver_key("1.0.0"))


if __name__ == "__main__":
    unittest.main()
