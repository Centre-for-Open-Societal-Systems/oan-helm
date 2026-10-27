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


if __name__ == '__main__':
    unittest.main()
