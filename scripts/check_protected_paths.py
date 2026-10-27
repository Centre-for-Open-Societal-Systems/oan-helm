"""Reject changes to release outputs that only the release workflow may write.

repository/ is what Rancher and `helm repo add` read, so its archives and
index change only through scripts/release.py on main. A pull request that
touches a protected path fails; on main, any non-merge commit in the pushed
range that touches one must come from the release bot.

  check_protected_paths.py --base <ref>             # pull request: diff base...HEAD
  check_protected_paths.py --range <before>..<after>  # push to main: check authors
"""
import argparse
import subprocess
import sys

PROTECTED = (
    "repository/",
    "releases/artifacts.json",
    "releases/current.yaml",
    "CHANGELOG.md",
)
RELEASE_BOT = "github-actions[bot]"


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True, encoding="utf-8").stdout


def protected(paths):
    return sorted(p for p in paths if p.startswith(PROTECTED))


def check_pull_request(base):
    changed = git("diff", "--name-only", f"{base}...HEAD").splitlines()
    return [f"{path}: written only by the release workflow after merge" for path in protected(changed)]


def check_push(revisions):
    errors = []
    for line in git("log", "--no-merges", "--format=%H%x09%an", revisions).splitlines():
        sha, author = line.split("\t", 1)
        if author == RELEASE_BOT:
            continue
        touched = protected(git("diff-tree", "--no-commit-id", "--name-only", "-r", sha).splitlines())
        errors += [f"{sha[:12]} by {author} changed {path}" for path in touched]
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--base", help="pull request base ref, e.g. origin/main")
    target.add_argument("--range", help="pushed commit range, e.g. <before>..<after>")
    args = parser.parse_args(argv)
    errors = check_pull_request(args.base) if args.base else check_push(args.range)
    if errors:
        print("Protected release paths changed outside the release workflow:", *errors, sep="\n  ", file=sys.stderr)
        print("Change the chart source under charts/ or addons/ instead; scripts/release.py "
              "versions, packages and indexes it after merge. See CONTRIBUTING.md.", file=sys.stderr)
        return 1
    print("No protected release path changed outside the release workflow.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
