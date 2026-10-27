import tempfile
import unittest
from pathlib import Path

from release import CHANGELOG_MARKER, next_version, set_version
from validate import is_subchart_doc


class ReleaseVersioningTest(unittest.TestCase):
    def test_prerelease_counter_increments(self):
        self.assertEqual(next_version('1.0.0-dev.16'), '1.0.0-dev.17')
        self.assertEqual(next_version('0.1.0-dev.9'), '0.1.0-dev.10')
        self.assertEqual(next_version('1.0.0-rc.1'), '1.0.0-rc.2')

    def test_prerelease_without_counter_gains_one(self):
        self.assertEqual(next_version('1.0.0-dev'), '1.0.0-dev.1')

    def test_stable_version_gets_a_patch(self):
        self.assertEqual(next_version('0.1.2'), '0.1.3')
        self.assertEqual(next_version('1.0.0'), '1.0.1')

    def test_rejects_non_semver(self):
        for bad in ('1.0', '1.0.0.dev1', 'v1.0.0', '01.0.0'):
            with self.subTest(bad=bad), self.assertRaises(AssertionError):
                next_version(bad)

    def test_set_version_changes_only_the_chart_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            metadata = Path(tmp) / 'Chart.yaml'
            metadata.write_bytes(b'apiVersion: v2\nname: x\nversion: 1.0.0-dev.1\ndependencies:\n- name: y\n  version: 2.0.0\n')
            set_version(metadata, '1.0.0-dev.2')
            self.assertEqual(metadata.read_bytes(),
                             b'apiVersion: v2\nname: x\nversion: 1.0.0-dev.2\ndependencies:\n- name: y\n  version: 2.0.0\n')

    def test_changelog_keeps_its_marker(self):
        changelog = Path(__file__).resolve().parents[1] / 'CHANGELOG.md'
        self.assertIn(CHANGELOG_MARKER, changelog.read_text(encoding='utf-8'))

    def test_only_bundled_dependency_docs_are_dropped(self):
        for kept in ('c/README.md', 'c/templates/NOTES.txt', 'c/charts/kafka/values.yaml',
                     'c/charts/kafka/templates/ci.yaml', 'c/charts/kafka/files/payload.json'):
            with self.subTest(kept=kept):
                self.assertFalse(is_subchart_doc(kept))
        for dropped in ('c/charts/kafka/README.md', 'c/charts/websub/charts/kafka/README.md',
                        'c/charts/kafka/ci/values-test.yaml', 'c/charts/kafka/CHANGELOG.md'):
            with self.subTest(dropped=dropped):
                self.assertTrue(is_subchart_doc(dropped))


if __name__ == '__main__':
    unittest.main()
