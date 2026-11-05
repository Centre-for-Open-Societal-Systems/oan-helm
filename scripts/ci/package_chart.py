"""Package helm/<chart> of a registry repository with the images of one build. Run by registry Jenkins pipelines.

Run it in the checkout of the registry, before the deploy. The deploy installs the archive, and publish_chart.py
adds that same archive to repository/<channel>/ afterwards, so an environment runs exactly what this repository lists.

  python3 package_chart.py --chart helm/openg2p-cropsown-registry --images images.tsv --output built-chart \
      --source-repository Centre-for-Open-Societal-Systems/cropsown-regsitry --source-commit <sha> \
      --subject "<commit subject>" --release cropsown-registry --namespace crop \
      --overlay environments/dev/values/cropsown.yaml --branch develop

--images is a tab separated file, one line per image: the values path of the image block, the repository and the
tag. The tag should carry the digest, as <tag>@sha256:<digest>. For example:

  registry.staffApi.image<TAB>123.dkr.ecr.ap-south-1.amazonaws.com/openg2p/cropsown-registry/staff-api<TAB>...

The version comes from git (derive-version.sh), so a shallow clone is refused. Only the packaged copy changes; nothing
is committed back to the registry. The annotations written here feed CHANGELOG.md and the rollback history.

Prints the archive path. Standard library only; runs on the stock Python 3.7 of the Jenkins agents.
Exit codes: 0 packaged, 1 failure.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
HELM_REPOSITORY = "https://openg2p.github.io/openg2p-helm"


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def is_content(line):
    return bool(line.strip()) and not line.lstrip().startswith("#")


def block_end(lines, start, indent):
    """The index after the block opened at `start`: the next content line indented `indent` or less."""
    for index in range(start + 1, len(lines)):
        if is_content(lines[index]) and indent_of(lines[index]) <= indent:
            return index
    return len(lines)


def find_key(lines, key, start, end):
    """The index of `key:` directly in lines[start:end], which is one mapping block."""
    depth = None
    for index in range(start, end):
        if not is_content(lines[index]):
            continue
        depth = indent_of(lines[index]) if depth is None else depth
        if indent_of(lines[index]) == depth and re.match(r"\s*%s:(\s|$)" % re.escape(key), lines[index]):
            return index
    return None


def set_image(text, path, repository, tag):
    """The values text with `repository` and `tag` of the image block at the dotted `path`. Comments stay as they are."""
    lines = text.split("\n")
    start, end = 0, len(lines)
    for key in path.split("."):
        at = find_key(lines, key, start, end)
        if at is None:
            raise ValueError("values have no %s (looking for %s)" % (path, key))
        start, end = at + 1, block_end(lines, at, indent_of(lines[at]))
    for key, value in (("repository", repository), ("tag", tag)):
        at = find_key(lines, key, start, end)
        if at is None:
            raise ValueError("values have no %s.%s" % (path, key))
        lines[at] = "%s%s: %s" % (" " * indent_of(lines[at]), key, json.dumps(value))
    return "\n".join(lines)


def read_images(text):
    images = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        fields = line.split("\t")
        if len(fields) != 3 or not all(fields):
            raise ValueError("images line %d is not <values path><TAB><repository><TAB><tag>" % number)
        images.append(fields)
    if not images:
        raise ValueError("no images: this build has nothing to package")
    return images


def annotate(text, notes):
    """The Chart.yaml text with `notes` added under annotations:, values quoted."""
    lines = text.split("\n")
    if "annotations:" not in lines:
        raise ValueError("Chart.yaml has no annotations block")
    at = lines.index("annotations:") + 1
    lines[at:at] = ["  %s: %s" % (key, json.dumps(value)) for key, value in sorted(notes.items())]
    return "\n".join(lines)


def run(command, cwd=None, env=None):
    return subprocess.run([str(part) for part in command], cwd=cwd and str(cwd), env=env, check=True,
                          stdout=subprocess.PIPE, universal_newlines=True).stdout


def derive_version(branch):
    if run(["git", "rev-parse", "--is-shallow-repository"]).strip() != "false":
        raise ValueError("a shallow clone cannot give the commit count the version needs")
    out = run(["bash", HERE / "derive-version.sh"], env=dict(os.environ, REF_NAME=branch, REF_TYPE="branch"))
    return re.search(r"(?m)^version=(\S+)$", out).group(1)


def remove_leftovers(chart):
    """Jenkins workspaces outlive builds: an ignored Chart.lock or downloaded subchart may be from an older chart."""
    lock = chart / "Chart.lock"
    if lock.exists():
        lock.unlink()
    shutil.rmtree(str(chart / "charts"), ignore_errors=True)


def package(args):
    source = Path(args.chart)
    version = args.version or derive_version(args.branch)
    images = read_images(Path(args.images).read_text(encoding="utf-8"))
    work = Path(tempfile.mkdtemp(prefix="chart-"))
    output = Path(args.output)
    try:
        chart = work / source.name
        shutil.copytree(str(source), str(chart))
        remove_leftovers(chart)
        values = chart / "values.yaml"
        text = values.read_text(encoding="utf-8")
        for path, repository, tag in images:
            text = set_image(text, path, repository, tag)
        values.write_text(text, encoding="utf-8")
        metadata = chart / "Chart.yaml"
        metadata.write_text(annotate(metadata.read_text(encoding="utf-8"), {
            "oan.org/source-repository": args.source_repository,
            "oan.org/source-commit": args.source_commit,
            "oan.org/source-subject": args.subject[:200],
            "oan.org/release-name": args.release,
            "oan.org/release-namespace": args.namespace,
            "oan.org/values-overlay": args.overlay,
        }), encoding="utf-8")
        run(["helm", "repo", "add", "--force-update", "openg2p", HELM_REPOSITORY])
        run(["helm", "dependency", "build", chart])
        shutil.rmtree(str(output), ignore_errors=True)
        output.mkdir(parents=True)
        run(["helm", "package", chart, "--version", version, "--destination", output])
    finally:
        shutil.rmtree(str(work), ignore_errors=True)
    return output / ("%s-%s.tgz" % (source.name, version))


def parser():
    result = argparse.ArgumentParser(description="Package a registry chart with the images of one build.")
    for name in ("chart", "images", "output", "source-repository", "source-commit", "release", "namespace", "overlay"):
        result.add_argument("--" + name, required=True)
    result.add_argument("--subject", default="")
    result.add_argument("--branch", default="develop")
    result.add_argument("--version", help="for tests; pipelines leave this out and the version comes from git")
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        print(package(args))
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print("FAIL: %s: %s" % (error.__class__.__name__, error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
