import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/ci"))
SPEC = importlib.util.spec_from_file_location("promote_chart_under_test", ROOT / "scripts/ci/promote_chart.py")
promote_chart = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(promote_chart)

DIGEST = "sha256:" + "a" * 64
REPOSITORY = "123456789012.dkr.ecr.ap-south-1.amazonaws.com/openg2p/farmer-registry/staff-api"
VALUES = """registry:
  staffApi:
    image:
      repository: "%s"
      # pinned by the build
      tag: "develop-1@%s"
  other:
    image:
      repository: openg2p/other
      tag: 1.2.3
""" % (REPOSITORY, DIGEST)
INDEX = """apiVersion: v1
entries:
  openg2p-crop:
  - annotations:
      oan.org/source-commit: ccc
    digest: d3
    name: openg2p-crop
    version: 0.0.0-develop.9
  openg2p-farmer:
  - annotations:
      oan.org/source-commit: aaa
    digest: d1
    name: openg2p-farmer
    version: 0.0.0-develop.9
  - annotations:
      oan.org/source-commit: bbb
    dependencies:
    - name: postgresql
      repository: https://example.org
      version: 1.2.3
    digest: d2
    name: openg2p-farmer
    version: 0.0.0-develop.10
generated: "2026-11-05T00:00:00Z"
"""


class IndexTests(unittest.TestCase):
    def test_only_the_named_chart_is_read_newest_first(self):
        entries = promote_chart.index_entries(INDEX, "openg2p-farmer")
        self.assertEqual([item["version"] for item in entries], ["0.0.0-develop.10", "0.0.0-develop.9"])
        self.assertEqual(entries[0], {"version": "0.0.0-develop.10", "commit": "bbb", "digest": "d2"})

    def test_a_chart_that_is_not_listed_has_no_entries(self):
        self.assertEqual(promote_chart.index_entries(INDEX, "openg2p-da"), [])

    def test_channel_is_read_at_a_commit_and_not_through_the_branch_cache(self):
        real = promote_chart.run
        commands = []
        promote_chart.run = lambda command: commands.append(command) or "abc123\trefs/heads/main\n"
        try:
            self.assertIn("/oan-helm/abc123/repository/develop/", promote_chart.channel())
            self.assertEqual(commands, [["git", "ls-remote", promote_chart.CHART_SOURCE, "refs/heads/main"]])
            self.assertIsInstance(promote_chart.CHART_SOURCE, str)
        finally:
            promote_chart.run = real


class TreeTests(unittest.TestCase):
    ENTRIES = [{"version": "2", "commit": "b"}, {"version": "1", "commit": "a"}]

    def test_the_chart_of_the_same_tree_is_chosen(self):
        entry = promote_chart.built_from_tree(self.ENTRIES, "tree-a", {"a": "tree-a", "b": "tree-b"}.get)
        self.assertEqual(entry["version"], "1")

    def test_a_tree_develop_never_built_is_refused(self):
        with self.assertRaises(ValueError):
            promote_chart.built_from_tree(self.ENTRIES, "tree-c", {"a": "tree-a", "b": "tree-b"}.get)


class ImageTests(unittest.TestCase):
    def test_only_images_pinned_to_a_digest_are_listed(self):
        self.assertEqual(promote_chart.pinned_images(VALUES), [(REPOSITORY, "develop-1", DIGEST)])

    def test_a_pinned_tag_without_repository_is_refused(self):
        with self.assertRaises(ValueError):
            promote_chart.pinned_images('tag: "x@%s"\n' % DIGEST)

    def test_the_tag_changes_and_the_digest_does_not(self):
        result = promote_chart.with_version_tag(VALUES, "1.0.0-rc.5")
        self.assertIn('      tag: "1.0.0-rc.5@%s"\n' % DIGEST, result)
        self.assertIn("      # pinned by the build\n", result)
        self.assertIn("      tag: 1.2.3\n", result)

    def test_an_image_outside_ecr_is_not_tagged(self):
        self.assertFalse(promote_chart.add_tag("docker.io/openg2p/other", DIGEST, "staging"))


if __name__ == "__main__":
    unittest.main()
