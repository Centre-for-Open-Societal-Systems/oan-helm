import os
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "ci" / "derive-version.sh"


class DeriveVersionTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.git("init", "-q", "-b", "develop")
        self.git("commit", "-q", "--allow-empty", "-m", "one")
        self.git("commit", "-q", "--allow-empty", "-m", "two")

    def git(self, *args):
        env = dict(os.environ, GIT_AUTHOR_NAME="a", GIT_AUTHOR_EMAIL="a@example.invalid",
                   GIT_COMMITTER_NAME="a", GIT_COMMITTER_EMAIL="a@example.invalid")
        subprocess.run(["git", *args], cwd=self.tmp.name, check=True, env=env)

    def derive(self, ref, ref_type="branch", **extra):
        env = {k: v for k, v in os.environ.items() if not k.startswith("GITHUB_")}
        env.update(REF_NAME=ref, REF_TYPE=ref_type, **extra)
        out = subprocess.run(["bash", SCRIPT.as_posix()], cwd=self.tmp.name, check=True, capture_output=True, text=True, env=env).stdout
        return dict(line.split("=", 1) for line in out.splitlines())

    def test_develop(self):
        result = self.derive("develop")
        self.assertEqual(result["version"], "0.0.0-develop.2")
        self.assertEqual(result["publish_chart"], "true")

    def test_staging_is_the_release_line(self):
        self.assertEqual(self.derive("staging")["version"], "1.0.0-rc.2")
        self.assertEqual(self.derive("staging", RELEASE_LINE="1.3")["version"], "1.3.0-rc.2")

    def test_staging_moves_to_the_next_patch_after_a_release(self):
        self.git("tag", "1.0.0")
        self.git("commit", "-q", "--allow-empty", "-m", "three")
        self.assertEqual(self.derive("staging")["version"], "1.0.1-rc.3")

    def test_release_tag_is_frozen_and_promoted_from_the_candidate(self):
        result = self.derive("1.0.0", "tag")
        self.assertEqual(result["version"], "1.0.0")
        self.assertEqual(result["frozen"], "true")
        self.assertIn("1.0.0-rc.2", result["promote_from"])

    def test_other_branches_do_not_publish_a_chart(self):
        for ref in ("release", "fix/form"):
            self.assertEqual(self.derive(ref)["publish_chart"], "false")


if __name__ == "__main__":
    unittest.main()
