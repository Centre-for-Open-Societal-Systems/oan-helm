"""Add one packaged chart to repository/<channel>/ of oan-helm. Run by registry Jenkins pipelines.

The channel follows from the version: 0.0.0-develop.N goes to develop, N.N.N-rc.N to staging and
N.N.N to release. The archive is created through the GitHub contents API, so a file that already
exists is refused and a published version can never be replaced. Only this new file is written;
.github/workflows/publish-channels.yaml then updates the index, checksums and CHANGELOG.md, so
pipelines of different registries never conflict with each other.

  GH_TOKEN=<token> python3 publish_chart.py dist/openg2p-farmer-registry-0.0.0-develop.812.tgz

Needs GH_TOKEN with push access to OAN_HELM_REPOSITORY (default the OAN oan-helm repository). For now that is
the token of a maintainer account, Jenkins credential oan-helm-fork-token. A GitHub App will replace it once its
configuration is done; only the credential changes, since commits always carry the PUBLISHER name below.
DRY_RUN=1 prints the target and writes nothing.
Exit codes: 0 published, 1 unexpected failure, 2 bad input, 3 no token, 4 version already published.
HTTP 409 means another commit moved main while GitHub wrote this one (two pipelines, or the index workflow, at the
same moment). The write is retried a few times; that is safe because the file is new and creation-only.

Standard library only; runs on the stock Python 3.7 of the Jenkins agents.
"""
import base64
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request

REPOSITORY = os.environ.get("OAN_HELM_REPOSITORY", "Centre-for-Open-Societal-Systems/oan-helm")
CHANNELS = (
    ("develop", re.compile(r"0\.0\.0-develop\.\d+")),
    ("staging", re.compile(r"\d+\.\d+\.\d+-rc\.\d+")),
    ("release", re.compile(r"\d+\.\d+\.\d+")),
)
PUBLISHER = {"name": "oan-chart-publisher", "email": "oan-chart-publisher@users.noreply.github.com"}
CONFLICT_ATTEMPTS = 5
CONFLICT_BACKOFF_SECONDS = 5
ARCHIVE = re.compile(r"(?P<chart>[a-z0-9-]+?)-(?P<version>\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)\.tgz")


def channel_of(version):
    for channel, pattern in CHANNELS:
        if pattern.fullmatch(version):
            return channel
    return None


def target_path(file_name):
    match = ARCHIVE.fullmatch(file_name)
    channel = channel_of(match.group("version")) if match else None
    if channel is None:
        raise ValueError("%s is not <chart>-<version>.tgz with a develop, rc or release version" % file_name)
    return "repository/%s/%s" % (channel, file_name), match


def main(argv):
    if len(argv) != 2 or not Path(argv[1]).is_file():
        print("usage: publish_chart.py <chart archive>", file=sys.stderr)
        return 2
    archive = Path(argv[1])
    try:
        path, match = target_path(archive.name)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    if os.environ.get("DRY_RUN") == "1":
        print("would publish %s to %s" % (path, REPOSITORY))
        return 0
    token = os.environ.get("GH_TOKEN")
    if not token:
        print("GH_TOKEN is required", file=sys.stderr)
        return 3
    body = {
        "message": "publish %s %s" % (match.group("chart"), match.group("version")),
        "content": base64.b64encode(archive.read_bytes()).decode("ascii"),
        "branch": "main",
        "author": PUBLISHER,
        "committer": PUBLISHER,
    }
    data = json.dumps(body).encode("utf-8")
    for attempt in range(1, CONFLICT_ATTEMPTS + 1):
        request = urllib.request.Request(
            "https://api.github.com/repos/%s/contents/%s" % (REPOSITORY, path), method="PUT", data=data,
            headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json"})
        try:
            urllib.request.urlopen(request, timeout=60)
        except urllib.error.HTTPError as error:
            if error.code == 422:
                print("%s is already published; a version is never replaced" % path, file=sys.stderr)
                return 4
            if error.code == 409 and attempt < CONFLICT_ATTEMPTS:
                wait = CONFLICT_BACKOFF_SECONDS * attempt
                print("GitHub answered HTTP 409 for %s (main moved during the write); retry %d of %d in %ds"
                      % (path, attempt, CONFLICT_ATTEMPTS - 1, wait), file=sys.stderr)
                time.sleep(wait)
                continue
            print("GitHub refused %s: HTTP %s" % (path, error.code), file=sys.stderr)
            return 1
        print("published %s" % path)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
