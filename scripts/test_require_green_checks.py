"""scripts/ci/require_green_checks.sh with a stand-in curl (no network) and a throwaway git repository: green delivers,
failed and pending-too-long stop, release-bot commits are walked past, and both Commons jobs run the gate first."""
import json
import os
import re
import shutil
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/ci/require_green_checks.sh"
BOT = "41898282+github-actions[bot]@users.noreply.github.com"
# Answers in order from $ANSWERS/<n>.runs and <n>.status; the last pair repeats. Records each URL and header line.
CURL = r"""#!/usr/bin/env bash
url=${@: -1}
printf '%s\n' "$*" >> "$ANSWERS/calls"
case "$url" in
  */check-runs*) kind=runs; n=$(( $(cat "$ANSWERS/n" 2>/dev/null || echo 0) + 1 )); echo $n > "$ANSWERS/n" ;;
  */status) kind=status; n=$(cat "$ANSWERS/n") ;;
esac
while [ ! -f "$ANSWERS/$n.$kind" ]; do n=$((n - 1)); done
out=
while [ $# -gt 0 ]; do [ "$1" = -o ] && out=$2; shift; done
cat "$ANSWERS/$n.$kind" > "${out:-/dev/stdout}"
"""


def run(name, status="completed", conclusion="success"):
    return {"name": name, "status": status, "conclusion": conclusion if status == "completed" else None}


@unittest.skipUnless(shutil.which("bash") and shutil.which("python3"), "needs bash and python3")
class RequireGreenChecks(unittest.TestCase):
    def gate(self, *answers, token="", wait="30", authors=("dev@example.org",)):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            repo = tmp / "repo"
            repo.mkdir()
            git = ["git", "-C", str(repo), "-c", "commit.gpgsign=false"]
            subprocess.run(git + ["init", "-q"], check=True)
            for n, author in enumerate(authors):
                subprocess.run(git + ["-c", "user.name=x", "-c", f"user.email={author}", "commit", "-q",
                                      "--allow-empty", "-m", f"c{n}"], check=True)
            log = subprocess.run(git + ["log", "--format=%H"], capture_output=True, text=True, check=True).stdout.split()
            (tmp / "bin").mkdir()
            curl = tmp / "bin/curl"
            curl.write_text(CURL, newline="\n")
            curl.chmod(curl.stat().st_mode | stat.S_IXUSR)
            for n, (runs, statuses) in enumerate(answers, 1):
                (tmp / f"{n}.runs").write_text(json.dumps({"total_count": len(runs), "check_runs": runs}))
                (tmp / f"{n}.status").write_text(json.dumps({"statuses": statuses}))
            env = dict(os.environ, PATH=f"{tmp / 'bin'}{os.pathsep}{os.environ['PATH']}", ANSWERS=str(tmp),
                       GH_TOKEN=token, WAIT_MINUTES=wait, POLL_SECONDS="0")
            done = subprocess.run(["bash", str(SCRIPT), "Centre-for-Open-Societal-Systems/oan-helm", "HEAD"],
                                  cwd=str(repo), env=env, capture_output=True, text=True, timeout=60)
            calls = (tmp / "calls").read_text() if (tmp / "calls").exists() else ""
            self.commits = log  # newest first
            return done.returncode, done.stdout + done.stderr, calls

    def test_all_green_deploys(self):
        code, out, calls = self.gate(([run("contracts"), run("chart"), run("build", conclusion="skipped")], []))
        self.assertEqual(code, 0, out)
        self.assertIn("green 3 check run(s): build, chart, contracts", out)
        self.assertIn(f"/commits/{self.commits[0]}/check-runs", calls)

    def test_a_failed_check_stops_at_once(self):
        code, out, _ = self.gate(([run("contracts", conclusion="failure"), run("chart", status="in_progress")], []))
        self.assertEqual(code, 1)
        self.assertIn("not green: contracts=failure; nothing is deployed", out)

    def test_a_failed_status_stops(self):
        code, out, _ = self.gate(([run("contracts")], [{"context": "ci/other", "state": "error"}]))
        self.assertEqual(code, 1)
        self.assertIn("ci/other=error", out)

    def test_pending_is_read_again_until_green(self):
        code, out, _ = self.gate(([], []), ([run("chart", status="queued")], []), ([run("chart")], []))
        self.assertEqual(code, 0, out)
        self.assertIn("waiting for checks", out)
        self.assertIn("no check runs reported yet", out)

    def test_pending_too_long_never_deploys(self):
        code, out, _ = self.gate(([run("chart", status="in_progress")], []), wait="0")
        self.assertEqual(code, 1)
        self.assertIn("still pending after 0 min (chart); nothing is deployed", out)

    def test_the_token_is_sent_but_never_printed(self):
        code, out, calls = self.gate(([run("chart")], []), token="t0ken-value")
        self.assertEqual(code, 0, out)
        self.assertIn("Authorization: Bearer t0ken-value", calls)
        self.assertNotIn("t0ken-value", out)

    def test_release_bot_commits_are_walked_past(self):
        code, out, calls = self.gate(([run("validate")], []), authors=("dev@example.org", BOT, BOT))
        self.assertEqual(code, 0, out)
        self.assertIn("HEAD: 2 release-bot commit(s) carry no checks", out)
        self.assertIn(f"/commits/{self.commits[2]}/check-runs", calls)
        self.assertNotIn(self.commits[0], calls)

    def test_only_release_bot_commits_is_refused(self):
        code, out, _ = self.gate(([run("validate")], []), authors=(BOT,))
        self.assertEqual(code, 2)
        self.assertIn("not a release-bot commit", out)


class CommonsJobsRunTheGateFirst(unittest.TestCase):
    def test_both_jobs_gate_before_any_delivery(self):
        for name in ("staging-commons", "dev-commons"):
            text = (ROOT / f"ci/jenkins/{name}.Jenkinsfile").read_text(encoding="utf-8")
            stages = re.findall(r"stage\('([^']+)'\)", text)
            self.assertEqual(stages[0], "Checks green", name)
            self.assertIn("sh 'bash scripts/ci/require_green_checks.sh Centre-for-Open-Societal-Systems/oan-helm HEAD'", text)
            self.assertIn("credentialsId: 'oan-helm-fork-token'", text)


if __name__ == "__main__":
    unittest.main()
