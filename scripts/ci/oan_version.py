"""The version of a build, read from init.yaml at the root of the repository that builds it.

    init.yaml
        version: 1.0.0           # the release being worked towards

The registry-platform version is not here: as in OpenG2P it is the ARG default of the registry's Dockerfiles
(docs/release/naming-standard.md, section 6). rpVersion and rpCommit are still accepted as optional fields.

A build is <version>-<branch>.<BUILD_NUMBER>: develop builds 1.0.0-develop.57; a staging promotion gives the same
digests 1.0.0-staging.12 (promote_chart.py); a release is 1.0.0. That string is the image tag of every image the build
pushes and the version of the chart it packages (docs/release/naming-standard.md). Any other branch gives
<version>-<slug>.<BUILD_NUMBER>, which publish_chart.py refuses, so a feature branch never reaches a channel.

    python3 oan_version.py                         <version>-<BRANCH_NAME>.<BUILD_NUMBER>
    python3 oan_version.py --branch staging        the same for another branch
    python3 oan_version.py --field rpVersion       one field of init.yaml (version, rpVersion or rpCommit)
    python3 oan_version.py --root <dir>            init.yaml of another directory (default: the current one)

Needs BRANCH_NAME and BUILD_NUMBER (Jenkins sets both) unless given as --branch and --build.
Standard library only; runs on the stock Python 3.7 of the Jenkins agents. Exit codes: 0 printed, 1 bad input.
"""
import argparse
import os
from pathlib import Path
import re
import sys

FILE = "init.yaml"
FIELDS = ("version", "rpVersion", "rpCommit")
COMMIT = re.compile(r"[0-9a-f]{7,40}")
VERSION = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)")
# The SemVer pre-release grammar, so rpVersion may be any OpenG2P version (1.2.2-rc.625).
PRERELEASE = r"(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*"
RP_VERSION = re.compile(VERSION.pattern + r"(?:-" + PRERELEASE + r")?")
PUBLISHED_BRANCHES = ("develop", "staging")
LINE = re.compile(r"""^(?P<key>[A-Za-z][A-Za-z0-9_]*)\s*:\s*(?P<value>"[^"]*"|'[^']*'|[^#\s]+)?\s*(?:#.*)?$""")


def read(root="."):
    """init.yaml as {field: value}. Only flat `key: value` lines and comments are allowed."""
    path = Path(root) / FILE
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        raise ValueError("%s is missing: every repository that builds images keeps its version there" % path)
    fields = {}
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        found = LINE.match(line)
        if not found or not found.group("value"):
            raise ValueError("%s line %d is not `key: value`" % (path, number))
        key, value = found.group("key"), found.group("value").strip("\"'")
        if key in fields:
            raise ValueError("%s sets %s twice" % (path, key))
        fields[key] = value
    if "version" not in fields:
        raise ValueError("%s has no version" % path)
    if not VERSION.fullmatch(fields["version"]):
        raise ValueError("%s version %r is not N.N.N: branch words and build numbers are added by the build"
                         % (path, fields["version"]))
    if "rpVersion" in fields and not RP_VERSION.fullmatch(fields["rpVersion"]):
        raise ValueError("%s rpVersion %r is not a SemVer version" % (path, fields["rpVersion"]))
    if "rpCommit" in fields and not COMMIT.fullmatch(fields["rpCommit"]):
        raise ValueError("%s rpCommit %r is not a git commit (7 to 40 lowercase hex digits)" % (path, fields["rpCommit"]))
    if "rpCommit" in fields and "rpVersion" not in fields:
        raise ValueError("%s has rpCommit without rpVersion" % path)
    unknown = sorted(set(fields) - set(FIELDS))
    if unknown:
        raise ValueError("%s has unknown fields: %s" % (path, ", ".join(unknown)))
    return fields


def semver_key(version):
    """A sort key that orders versions as SemVer 2.0.0 does: 1.0.0-develop.9 < 1.0.0-develop.10 < 1.0.0-rc.553
    < 1.0.0-staging.1 < 1.0.0. Build metadata (+...) is ignored."""
    core, _, prerelease = version.split("+", 1)[0].partition("-")
    numbers = tuple(int(part) for part in core.split("."))
    if not prerelease:
        return numbers + (1, ())
    words = tuple((0, int(word), "") if word.isdigit() else (1, 0, word) for word in prerelease.split("."))
    return numbers + (0, words)


def slug(branch):
    """A branch name as a SemVer pre-release word: feature/G2R-590 -> feature-g2r-590."""
    word = re.sub(r"-+", "-", re.sub(r"[^a-z0-9-]+", "-", branch.lower())).strip("-")
    if not word:
        raise ValueError("branch %r gives no version word" % branch)
    return "b" + word if word.isdigit() else word


def build_version(version, branch, build):
    """<version>-<branch>.<build>, e.g. 1.0.0-develop.57. The build number is Jenkins' BUILD_NUMBER of that job."""
    if not VERSION.fullmatch(version):
        raise ValueError("version %r is not N.N.N" % version)
    if not re.fullmatch(r"[1-9]\d*", str(build)):
        raise ValueError("build number %r is not a positive integer" % build)
    word = branch if branch in PUBLISHED_BRANCHES else slug(branch)
    return "%s-%s.%s" % (version, word, build)


def current(root=".", branch=None, build=None, env=None):
    env = os.environ if env is None else env
    branch = branch or env.get("BRANCH_NAME")
    build = build or env.get("BUILD_NUMBER")
    if not branch or not build:
        raise ValueError("BRANCH_NAME and BUILD_NUMBER are required (or --branch and --build)")
    return build_version(read(root)["version"], branch, build)


def parser():
    result = argparse.ArgumentParser(description="Print the version of this build from init.yaml.")
    result.add_argument("--root", default=".")
    result.add_argument("--branch")
    result.add_argument("--build")
    result.add_argument("--field", choices=FIELDS)
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.field:
            value = read(args.root).get(args.field)
            if value is None:
                raise ValueError("%s has no %s" % (Path(args.root) / FILE, args.field))
            print(value)
        else:
            print(current(args.root, args.branch, args.build))
        return 0
    except ValueError as error:
        print("FAIL: %s" % error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
