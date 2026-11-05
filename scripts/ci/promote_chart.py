"""Promote a develop chart to staging: the same images under a release candidate version, nothing rebuilt.

Run it by a registry Jenkins pipeline in a full checkout of the staging branch, before the deploy:

  python3 promote_chart.py --chart openg2p-cropsown-registry --release cropsown-registry --namespace crop \
      --overlay environments/staging/values/cropsown.yaml --output built-chart

The chart is the one in repository/develop/ whose source commit has exactly the source tree of this checkout. If develop
never built that tree the promotion fails: staging only ever runs what New Dev ran first. Every ECR image of the chart
gets the rc tag and the moving staging tag on the same digest, and the chart is packaged again with the rc version.
Dependencies stay as they were vendored. publish_chart.py then adds the archive to repository/staging/.

Needs the aws CLI with credentials for ECR. DRY_RUN=1 tags nothing. Standard library only: it runs on the stock
Python 3.7 of the Jenkins agents. Exit codes: 0 promoted, 1 failure.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from package_chart import annotate, derive_version  # noqa: E402

REPOSITORY = "https://github.com/Centre-for-Open-Societal-Systems/oan-helm.git"
CHANNEL = "https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/%s/repository/develop/"
MOVING_TAG = "staging"
ECR = re.compile(r"^(?P<host>\d{12}\.dkr\.ecr\.(?P<region>[a-z0-9-]+)\.amazonaws\.com)/(?P<name>.+)$")
PINNED_TAG = re.compile(r"""^(?P<lead>\s*tag:\s*)["']?(?P<tag>[^"'@\s]+)@(?P<digest>sha256:[0-9a-f]{64})["']?\s*$""")
REPOSITORY = re.compile(r"""^\s*repository:\s*["']?(?P<repository>[^"'\s]+)["']?\s*$""")


def index_entries(text, chart):
    """The entries of `chart` in a Helm index, newest first, as {version, commit, digest}."""
    entries, entry, inside = [], None, False
    for line in text.splitlines():
        if re.match(r"  [^\s-].*:$", line):
            inside = line.strip() == chart + ":"
            continue
        if not inside:
            continue
        if line.startswith("  - "):
            entry = {}
            entries.append(entry)
        # Exact indents: each dependency of an entry has a version of its own, one level deeper.
        found = re.match(r"(?:      (oan\.org/source-commit)|    (version|digest)): ['\"]?([^'\"\s]+)", line)
        if found and entry is not None:
            entry["commit" if found.group(1) else found.group(2)] = found.group(3)
    entries = [item for item in entries if {"version", "commit", "digest"} <= set(item)]
    return sorted(entries, key=lambda item: int(item["version"].rsplit(".", 1)[1]), reverse=True)


def channel():
    """repository/develop/ at the newest commit of main. A branch URL is served from a cache for minutes after a publish."""
    return CHANNEL % run(["git", "ls-remote", REPOSITORY, "refs/heads/main"]).split()[0]


def built_from_tree(entries, tree, tree_of):
    """The newest entry whose commit has source tree `tree`, or an error: staging runs nothing develop did not build."""
    for entry in entries:
        if tree_of(entry["commit"]) == tree:
            return entry
    raise ValueError("no develop chart was built from this source tree: run the develop build first, nothing is rebuilt here")


def pinned_images(values):
    """The (repository, tag, digest) of every image in the values that is pinned to a digest."""
    images, repository = [], None
    for line in values.splitlines():
        found = REPOSITORY.match(line)
        if found:
            repository = found.group("repository")
            continue
        found = PINNED_TAG.match(line)
        if found:
            if repository is None:
                raise ValueError("a pinned tag has no repository: %s" % line.strip())
            images.append((repository, found.group("tag"), found.group("digest")))
    return images


def with_version_tag(values, version):
    """The values with each pinned tag renamed to `version`. The digests stay, so the images cannot change."""
    lines = []
    for line in values.split("\n"):
        found = PINNED_TAG.match(line)
        lines.append("%s%s" % (found.group("lead"), json.dumps("%s@%s" % (version, found.group("digest")))) if found else line)
    return "\n".join(lines)


def run(command, cwd=None):
    return subprocess.run([str(part) for part in command], cwd=cwd and str(cwd), check=True,
                          stdout=subprocess.PIPE, universal_newlines=True).stdout


def add_tag(repository, digest, tag):
    """Add `tag` to the image at `digest` in ECR. An image that already has the tag is left alone."""
    found = ECR.match(repository)
    if found is None:
        return False
    base = ["aws", "ecr", "--region", found.group("region")]
    name = ["--repository-name", found.group("name")]
    manifest = run(base + ["batch-get-image"] + name + ["--image-ids", "imageDigest=" + digest, "--query",
                                                        "images[0].imageManifest", "--output", "text"]).rstrip("\n")
    if not manifest or manifest == "None":
        raise ValueError("%s has no image %s" % (repository, digest))
    result = subprocess.run(base + ["put-image"] + name + ["--image-tag", tag, "--image-manifest", manifest],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode and "ImageAlreadyExistsException" not in result.stderr:
        raise ValueError("%s: could not add tag %s: %s" % (repository, tag, result.stderr.strip()[:300]))
    return True


def download(url, target, digest):
    data = urllib.request.urlopen(url, timeout=120).read()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError("%s does not match the digest in the index" % url)
    target.write_bytes(data)


def promote(args):
    version = derive_version("staging")
    tree = run(["git", "rev-parse", "HEAD^{tree}"]).strip()
    source = channel()
    index = urllib.request.urlopen(source + "index.yaml", timeout=60).read().decode("utf-8")

    def tree_of(commit):
        try:
            return run(["git", "rev-parse", commit + "^{tree}"]).strip()
        except subprocess.CalledProcessError:
            return None

    entry = built_from_tree(index_entries(index, args.chart), tree, tree_of)
    work = Path(tempfile.mkdtemp(prefix="promote-"))
    output = Path(args.output)
    try:
        archive = work / "develop.tgz"
        download("%s%s-%s.tgz" % (source, args.chart, entry["version"]), archive, entry["digest"])
        with tarfile.open(str(archive)) as bundle:
            bundle.extractall(str(work))
        chart = work / args.chart
        values = (chart / "values.yaml").read_text(encoding="utf-8")
        images = pinned_images(values)
        if not images:
            raise ValueError("%s %s has no images pinned to a digest" % (args.chart, entry["version"]))
        for repository, _, digest in images:
            print("%s@%s -> %s, %s" % (repository, digest, version, MOVING_TAG))
            if os.environ.get("DRY_RUN") != "1":
                for tag in (version, MOVING_TAG):
                    add_tag(repository, digest, tag)
        (chart / "values.yaml").write_text(with_version_tag(values, version), encoding="utf-8")
        metadata = chart / "Chart.yaml"
        text = metadata.read_text(encoding="utf-8")
        for key in ("release-name", "release-namespace", "values-overlay"):
            text = re.sub(r"(?m)^\s*oan\.org/%s:.*\n" % key, "", text)
        metadata.write_text(annotate(text, {
            "oan.org/promoted-from": entry["version"],
            "oan.org/release-name": args.release,
            "oan.org/release-namespace": args.namespace,
            "oan.org/values-overlay": args.overlay,
        }), encoding="utf-8")
        shutil.rmtree(str(output), ignore_errors=True)
        output.mkdir(parents=True)
        run(["helm", "package", chart, "--version", version, "--destination", output])
    finally:
        shutil.rmtree(str(work), ignore_errors=True)
    return output / ("%s-%s.tgz" % (args.chart, version))


def parser():
    result = argparse.ArgumentParser(description="Promote a develop chart to staging without rebuilding it.")
    for name in ("chart", "release", "namespace", "overlay", "output"):
        result.add_argument("--" + name, required=True)
    return result


def main(argv=None):
    try:
        print(promote(parser().parse_args(argv)))
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print("FAIL: %s: %s" % (error.__class__.__name__, error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
