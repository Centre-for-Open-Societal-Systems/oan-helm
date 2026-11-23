import os
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

import check_protected_paths


class ProtectedPathsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.cwd = os.getcwd()
        os.chdir(self.tmp.name)
        self.git('init', '-q', '-b', 'main')
        self.commit('Human', {'charts/x/Chart.yaml': 'version: 1.0.0\n', 'repository/index.yaml': 'entries: {}\n'})

    def tearDown(self):
        os.chdir(self.cwd)
        self.tmp.cleanup()

    def git(self, *args, author='Human'):
        env = dict(os.environ, GIT_AUTHOR_NAME=author, GIT_AUTHOR_EMAIL='a@example.invalid',
                   GIT_COMMITTER_NAME=author, GIT_COMMITTER_EMAIL='a@example.invalid')
        return subprocess.run(['git', *args], check=True, capture_output=True, text=True, env=env).stdout.strip()

    def commit(self, author, files):
        for name, content in files.items():
            Path(name).parent.mkdir(parents=True, exist_ok=True)
            Path(name).write_text(content)
        self.git('add', '-A', author=author)
        self.git('commit', '-q', '-m', 'change', author=author)
        return self.git('rev-parse', 'HEAD')

    def run_check(self, *args):
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            return check_protected_paths.main(list(args))

    def test_pull_request_may_change_chart_source(self):
        self.git('checkout', '-q', '-b', 'feature')
        self.commit('Human', {'charts/x/values.yaml': 'a: 1\n'})
        self.assertEqual(self.run_check('--base', 'main'), 0)

    def test_pull_request_may_not_change_repository(self):
        self.git('checkout', '-q', '-b', 'feature')
        self.commit('Human', {'repository/x-1.0.1.tgz': 'archive'})
        self.assertEqual(self.run_check('--base', 'main'), 1)

    def test_pull_request_may_not_edit_changelog_or_seals(self):
        for path in ('CHANGELOG.md', 'releases/artifacts.json', 'releases/current.yaml'):
            with self.subTest(path=path):
                self.git('checkout', '-q', '-B', 'feature', 'main')
                self.commit('Human', {path: 'edited\n'})
                self.assertEqual(self.run_check('--base', 'main'), 1)

    def test_release_bot_may_write_repository_on_main(self):
        before = self.git('rev-parse', 'HEAD')
        after = self.commit('github-actions[bot]', {'repository/x-1.0.1.tgz': 'archive'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 0)

    def test_direct_human_push_to_repository_fails(self):
        before = self.git('rev-parse', 'HEAD')
        after = self.commit('Human', {'repository/index.yaml': 'entries: {x: []}\n'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)

    def test_channel_publisher_may_add_an_archive(self):
        before = self.git('rev-parse', 'HEAD')
        after = self.commit('oan-chart-publisher', {'repository/develop/x-0.0.0-develop.5.tgz': 'archive'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 0)

    def test_channel_publisher_may_not_replace_an_archive(self):
        self.commit('oan-chart-publisher', {'repository/release/x-1.0.0.tgz': 'archive'})
        before = self.git('rev-parse', 'HEAD')
        after = self.commit('oan-chart-publisher', {'repository/release/x-1.0.0.tgz': 'other'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)

    def test_channel_publisher_may_not_write_the_index(self):
        before = self.git('rev-parse', 'HEAD')
        after = self.commit('oan-chart-publisher', {'repository/develop/index.yaml': 'entries: {}\n'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)

    def test_channel_archive_from_a_person_fails(self):
        before = self.git('rev-parse', 'HEAD')
        after = self.commit('Human', {'repository/develop/x-0.0.0-develop.5.tgz': 'archive'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)


    # --- the seed pinner (openg2p-data develop build) ---
    SEED_REPO = '379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/openg2p-data/master-data-db-seed'
    OLD = '1.0.0-develop.67@sha256:' + 'a' * 64
    NEW = '1.0.0-develop.70@sha256:' + 'b' * 64

    def seed_values(self, tag, extra=''):
        return (f"master-data:\n  geoSeed:\n    image:\n      repository: {self.SEED_REPO}\n"
                f"      tag: {tag}\n    enabled: false\n{extra}")

    def seed_base(self):
        self.commit('Human', {'charts/openg2p-commons-services/values.yaml': self.seed_values(self.OLD),
                              'releases/1.0.0-dev.51.yaml': 'chartVersion: 1.0.0-dev.51\n'})
        return self.git('rev-parse', 'HEAD')

    def test_seed_pinner_may_move_the_pin_and_add_a_record(self):
        before = self.seed_base()
        after = self.commit('oan-seed-pinner', {
            'charts/openg2p-commons-services/values.yaml': self.seed_values(self.NEW),
            'releases/1.0.0-dev.52.yaml': 'chartVersion: 1.0.0-dev.52\n'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 0)

    def test_seed_pinner_may_not_change_other_lines_of_the_values(self):
        before = self.seed_base()
        after = self.commit('oan-seed-pinner', {
            'charts/openg2p-commons-services/values.yaml': self.seed_values(self.NEW).replace('enabled: false', 'enabled: true')})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)

    def test_seed_pinner_may_not_pin_another_repository(self):
        before = self.seed_base()
        bad = self.seed_values(self.NEW).replace('/eoan/openg2p-data/master-data-db-seed', '/evil/image')
        after = self.commit('oan-seed-pinner', {'charts/openg2p-commons-services/values.yaml': bad})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)

    def test_seed_pinner_may_not_pin_a_floating_tag(self):
        before = self.seed_base()
        after = self.commit('oan-seed-pinner', {'charts/openg2p-commons-services/values.yaml': self.seed_values('latest')})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)

    def test_seed_pinner_may_not_touch_any_other_file(self):
        before = self.seed_base()
        for files in ({'charts/x/values.yaml': 'a: 1\n'}, {'environments/dev/values/commons-services.yaml': 'a: 1\n'},
                      {'repository/develop/x-0.0.0-develop.5.tgz': 'archive'}, {'CHANGELOG.md': 'x\n'},
                      {'.github/workflows/release.yaml': 'x\n'}, {'scripts/ci/deliver_dev_commons.sh': 'x\n'}):
            with self.subTest(files=list(files)):
                after = self.commit('oan-seed-pinner', files)
                self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)
                self.git('reset', '-q', '--hard', before)

    def test_seed_pinner_may_not_rewrite_an_existing_record(self):
        before = self.seed_base()
        after = self.commit('oan-seed-pinner', {'releases/1.0.0-dev.51.yaml': 'chartVersion: 1.0.0-dev.51\nx: 1\n'})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)

    def test_seed_pinner_record_must_match_its_name_and_come_after_the_others(self):
        before = self.seed_base()
        values = {'charts/openg2p-commons-services/values.yaml': self.seed_values(self.NEW)}
        nl = chr(10)
        cases = {
            'wrong first line': {'releases/1.0.0-dev.52.yaml': 'chartVersion: 1.0.0-dev.99' + nl},
            'not a chartVersion': {'releases/1.0.0-dev.52.yaml': 'x: 1' + nl},
            'not after the newest': {'releases/1.0.0-dev.40.yaml': 'chartVersion: 1.0.0-dev.40' + nl},
            'two records': {'releases/1.0.0-dev.52.yaml': 'chartVersion: 1.0.0-dev.52' + nl,
                            'releases/1.0.0-dev.53.yaml': 'chartVersion: 1.0.0-dev.53' + nl},
        }
        for name, record in cases.items():
            with self.subTest(case=name):
                after = self.commit('oan-seed-pinner', {**values, **record})
                self.assertEqual(self.run_check('--range', f'{before}..{after}'), 1)
                self.git('reset', '-q', '--hard', before)

    def test_other_authors_are_not_limited_to_the_seed_lines(self):
        before = self.seed_base()
        after = self.commit('Human', {'charts/openg2p-commons-services/values.yaml': self.seed_values(self.OLD, 'x: 1\n')})
        self.assertEqual(self.run_check('--range', f'{before}..{after}'), 0)


if __name__ == '__main__':
    unittest.main()
