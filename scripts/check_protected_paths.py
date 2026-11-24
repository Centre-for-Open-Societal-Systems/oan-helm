"""Reject changes to release outputs that only the release workflow may write.

repository/ is what Rancher and `helm repo add` read, so its archives and
index change only through scripts/release.py on main. A pull request that
touches a protected path fails; on main, any non-merge commit in the pushed
range that touches one must come from the release bot. The one exception is the
registry pipelines' publisher, which may add a new archive to a channel folder
(scripts/ci/publish_chart.py) and nothing else. The openg2p-data pipeline's seed pinner
may move the seed image pin in the commons-services values and add one release record,
and nothing else (see seed_pinner_errors).

  check_protected_paths.py --base <ref>             # pull request: diff base...HEAD
  check_protected_paths.py --range <before>..<after>  # push to main: check authors
"""
import argparse
import re
import subprocess
import sys

PROTECTED = (
    "repository/",
    "releases/artifacts.json",
    "releases/current.yaml",
    "releases/channels.json",
    "releases/channels-current.yaml",
    "releases/history/",
    "CHANGELOG.md",
)
RELEASE_BOT = "github-actions[bot]"
CHANNEL_PUBLISHER = "oan-chart-publisher"
CHANNEL_ARCHIVE = re.compile(r"repository/(develop|staging|release)/[^/]+\.tgz")
# The openg2p-data develop build moves the Master Data seed image pin: two lines of the chart values
# and one new release record. Any commit under this name that does anything else is an error, so the
# credential it pushes with can do no more than this without the push check failing.
SEED_PINNER = "oan-seed-pinner"
SEED_VALUES = "charts/openg2p-commons-services/values.yaml"
SEED_RECORD = re.compile(r"releases/1\.0\.0-dev\.\d+\.yaml")
SEED_LINE_OLD = re.compile(r"-      (repository|tag): \S+")
SEED_LINE_NEW = re.compile(
    r"\+      (repository: \S+/eoan/openg2p-data/master-data-db-seed"
    r"|tag: \d+\.\d+\.\d+-develop\.\d+@sha256:[0-9a-f]{64})"
)


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True, encoding="utf-8").stdout


def protected(paths):
    return sorted(p for p in paths if p.startswith(PROTECTED))


def check_pull_request(base):
    changed = git("diff", "--name-only", f"{base}...HEAD").splitlines()
    return [f"{path}: written only by the release workflow after merge" for path in protected(changed)]


def seed_pinner_errors(sha):
    """What a commit by the seed pinner may change: the two seed lines and one new release record."""
    errors = []
    records = 0
    for change in git("diff-tree", "--no-commit-id", "--name-status", "-r", sha).splitlines():
        status, path = change.split("\t")[0], change.split("\t")[-1]
        if status == "A" and SEED_RECORD.fullmatch(path):
            records += 1
            errors += seed_record_errors(sha, path, records)
            continue
        if status == "M" and path == SEED_VALUES:
            diff = git("diff-tree", "--no-commit-id", "-p", "-U0", "-r", sha, "--", SEED_VALUES).splitlines()
            lines = [d for d in diff if d[:1] in "+-" and not d.startswith(("+++", "---"))]
            bad = [d for d in lines if not (SEED_LINE_NEW.fullmatch(d) or SEED_LINE_OLD.fullmatch(d))]
            if bad or len(lines) > 4:
                errors.append(f"{sha[:12]} by {SEED_PINNER} changed more than the seed image lines of {path}")
            continue
        errors.append(f"{sha[:12]} by {SEED_PINNER} changed {path} ({status}); it may only move the seed "
                      f"pin in {SEED_VALUES} and add a releases/1.0.0-dev.<n>.yaml record")
    return errors


def seed_record_errors(sha, path, count):
    """A record added by the seed pinner: one per commit, numbered after every existing record, and
    its chartVersion is its own file name."""
    n = int(re.fullmatch(r"releases/1\.0\.0-dev\.(\d+)\.yaml", path).group(1))
    errors = []
    if count > 1:
        errors.append(f"{sha[:12]} by {SEED_PINNER} added more than one release record")
    text = git("show", f"{sha}:{path}")
    first = text.splitlines()[0].strip() if text.strip() else ""
    if first != f"chartVersion: 1.0.0-dev.{n}":
        errors.append(f"{sha[:12]} {path}: the first line must be 'chartVersion: 1.0.0-dev.{n}', not {first!r}")
    existing = [int(m.group(1)) for m in
                (re.fullmatch(r"1\.0\.0-dev\.(\d+)\.yaml", f.rsplit("/", 1)[-1])
                 for f in git("ls-tree", "--name-only", f"{sha}~1", "releases/").splitlines()) if m]
    if existing and n <= max(existing):
        errors.append(f"{sha[:12]} {path}: a new record must be numbered after the newest existing one "
                      f"(1.0.0-dev.{max(existing)})")
    return errors


def check_push(revisions):
    errors = []
    for line in git("log", "--no-merges", "--format=%H%x09%an", revisions).splitlines():
        sha, author = line.split("\t", 1)
        if author == RELEASE_BOT:
            continue
        if author == SEED_PINNER:
            errors += seed_pinner_errors(sha)
            continue
        for change in git("diff-tree", "--no-commit-id", "--name-status", "-r", sha).splitlines():
            status, path = change.split("\t")[0], change.split("\t")[-1]
            if not protected([path]):
                continue
            if author == CHANNEL_PUBLISHER and status == "A" and CHANNEL_ARCHIVE.fullmatch(path):
                continue
            errors.append(f"{sha[:12]} by {author} changed {path}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--base", help="pull request base ref, e.g. origin/main")
    target.add_argument("--range", help="pushed commit range, e.g. <before>..<after>")
    args = parser.parse_args(argv)
    errors = check_pull_request(args.base) if args.base else check_push(args.range)
    if errors:
        print("Changes outside what their author may write:", *errors, sep="\n  ", file=sys.stderr)
        print("Change the chart source under charts/ or addons/ instead; scripts/release.py "
              "versions, packages and indexes it after merge. See CONTRIBUTING.md.", file=sys.stderr)
        return 1
    print("No protected release path changed outside the release workflow.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
