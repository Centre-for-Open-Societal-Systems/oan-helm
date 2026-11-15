"""Bundle one packaged chart into a parent chart of oan-helm, through a pull request. Run by Jenkins pipelines.

The archive is the one publish_chart.py just added to repository/<channel>/. The pull request swaps it in for the
older archive in charts/<parent>/charts/, sets the dependency version in the parent's Chart.yaml and Chart.lock and
reseals the lock digest, the change `helm dependency update` would make. Nothing is checked out: the commit is made
through the GitHub git data API on a branch vendor/<chart>-<version>, from the head of main. An older open proposal
for the same chart is closed as superseded, so only the newest build waits for review.

  GH_TOKEN=<token> python3 vendor_subchart.py --parent openg2p-commons-services built-chart/oan-aggregation-api-0.0.0-develop.42.tgz

The parent must already depend on the chart (the first bundling is a reviewed change by hand). Same token as
publish_chart.py; OAN_HELM_REPOSITORY selects another repository. DRY_RUN=1 prints the target and writes nothing.
Exit codes: 0 proposed, 1 unexpected failure, 2 bad input, 3 no token, 4 that version is already bundled or proposed.

Standard library only; runs on the stock Python 3.7 of the Jenkins agents.
"""
import argparse
import base64
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request

REPOSITORY = os.environ.get("OAN_HELM_REPOSITORY", "Centre-for-Open-Societal-Systems/oan-helm")
PUBLISHER = {"name": "oan-chart-publisher", "email": "oan-chart-publisher@users.noreply.github.com"}
ARCHIVE = re.compile(r"(?P<chart>[a-z0-9-]+?)-(?P<version>\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)\.tgz")
# Helm's chart.Dependency fields, in its JSON order. name and repository are always written; the rest only when set.
DEPENDENCY_FIELDS = ("name", "version", "repository", "condition", "tags", "enabled", "import-values", "alias")


class NotFound(Exception):
    pass


class GitHubError(Exception):
    pass


def dependency_blocks(text):
    """(first line, end line, fields) of each entry of the dependencies: list of a Chart.yaml or Chart.lock."""
    lines = text.split("\n")
    at = lines.index("dependencies:") + 1
    blocks = []
    while at < len(lines) and lines[at].startswith(("- ", "  ")):
        if lines[at].startswith("- "):
            blocks.append([at, at, {}])
        key, _, value = lines[at][2:].partition(":")
        value = value.strip().strip("'\"")
        if not value or lines[at][2:].startswith(("- ", " ")):
            # tags, import-values and the like: Helm hashes them as lists, which this reader does not.
            raise ValueError("dependency field %r is not a scalar; update the lock with helm" % key.strip())
        blocks[-1][2][key.strip()] = value
        at += 1
        blocks[-1][1] = at
    return blocks


def dependency_version(text, name):
    return next((fields.get("version") for _, _, fields in dependency_blocks(text) if fields["name"] == name), None)


def lock_digest(chart_yaml, chart_lock):
    """The digest Helm records in Chart.lock: sha256 of the JSON of [Chart.yaml dependencies, Chart.lock dependencies]."""
    def helm_json(text):
        return [{key: fields.get(key, "") for key in DEPENDENCY_FIELDS if key in ("name", "repository") or fields.get(key)}
                for _, _, fields in dependency_blocks(text)]
    data = json.dumps([helm_json(chart_yaml), helm_json(chart_lock)], separators=(",", ":"), ensure_ascii=False)
    # Go's encoding/json escapes these.
    data = data.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return "sha256:" + hashlib.sha256(data.encode("utf-8")).hexdigest()


def set_version(text, name, version):
    lines = text.split("\n")
    for start, end, fields in dependency_blocks(text):
        if fields["name"] == name:
            at = next(i for i in range(start, end) if lines[i][2:].startswith("version:"))
            lines[at] = lines[at][:2] + "version: " + version
            return "\n".join(lines)
    raise ValueError("the parent chart does not depend on %s" % name)


def bump(chart_yaml, chart_lock, name, version):
    """Chart.yaml and Chart.lock with dependency `name` at `version`, the lock resealed."""
    chart_yaml = set_version(chart_yaml, name, version)
    chart_lock = set_version(chart_lock, name, version)
    digest = lock_digest(chart_yaml, chart_lock)
    generated = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    lines = []
    for line in chart_lock.split("\n"):
        if line.startswith("digest: "):
            line = "digest: " + digest
        elif line.startswith("generated: "):
            line = 'generated: "%s"' % generated
        lines.append(line)
    return chart_yaml, "\n".join(lines)


def github_api(repository, token):
    """A call(method, path, body) on https://api.github.com/repos/<repository>/<path>, answering the decoded JSON."""
    def call(method, path, body=None):
        request = urllib.request.Request(
            "https://api.github.com/repos/%s/%s" % (repository, path), method=method,
            data=None if body is None else json.dumps(body).encode("utf-8"),
            headers={"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json"})
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                text = response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            if error.code == 404:
                raise NotFound(path)
            raise GitHubError("%s %s: HTTP %s %s" % (method, path, error.code, error.read()[:300]))
        return json.loads(text) if text else {}
    return call


def read_file(api, path):
    return base64.b64decode(api("GET", "contents/%s?ref=main" % path)["content"]).decode("utf-8")


def exists(api, path):
    try:
        api("GET", path)
        return True
    except NotFound:
        return False


def propose(api, parent, archive, chart, version):
    base = "charts/%s" % parent
    chart_yaml, chart_lock = read_file(api, base + "/Chart.yaml"), read_file(api, base + "/Chart.lock")
    current = dependency_version(chart_yaml, chart)
    if current is None:
        print("%s does not depend on %s; bundle its first version by hand" % (parent, chart), file=sys.stderr)
        return 2
    if current == version:
        print("%s already bundles %s %s" % (parent, chart, version), file=sys.stderr)
        return 4
    branch = "vendor/%s-%s" % (chart, version)
    if exists(api, "git/ref/heads/" + branch):
        print("%s %s is already proposed on %s" % (chart, version, branch), file=sys.stderr)
        return 4
    chart_yaml, chart_lock = bump(chart_yaml, chart_lock, chart, version)

    head = api("GET", "git/ref/heads/main")["object"]["sha"]
    tree = api("GET", "git/commits/" + head)["tree"]["sha"]
    old = []
    for entry in api("GET", "contents/%s/charts?ref=main" % base):
        found = ARCHIVE.fullmatch(entry["name"])
        if entry["type"] == "file" and found and found.group("chart") == chart:
            old.append(entry["path"])

    def blob(body):
        return api("POST", "git/blobs", body)["sha"]
    entries = [{"path": "%s/charts/%s" % (base, archive.name), "mode": "100644", "type": "blob",
                "sha": blob({"content": base64.b64encode(archive.read_bytes()).decode("ascii"), "encoding": "base64"})}]
    for path, text in ((base + "/Chart.yaml", chart_yaml), (base + "/Chart.lock", chart_lock)):
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob({"content": text, "encoding": "utf-8"})})
    entries += [{"path": path, "mode": "100644", "type": "blob", "sha": None} for path in old]
    tree = api("POST", "git/trees", {"base_tree": tree, "tree": entries})["sha"]
    title = "chore(%s): bundle %s %s" % (parent, chart, version)
    commit = api("POST", "git/commits", {"message": title, "tree": tree, "parents": [head],
                                         "author": PUBLISHER, "committer": PUBLISHER})["sha"]
    api("POST", "git/refs", {"ref": "refs/heads/" + branch, "sha": commit})
    pull = api("POST", "pulls", {
        "title": title, "head": branch, "base": "main",
        "body": "Bundles `%s` %s (was %s) in `%s`: the archive published to repository/, Chart.yaml and Chart.lock "
                "with the resealed digest. Opened by vendor_subchart.py." % (chart, version, current, parent)})
    print("proposed %s %s in %s: %s" % (chart, version, parent, pull.get("html_url")))

    # Older proposals for this chart: the newest build supersedes them.
    prefix = "vendor/%s-" % chart
    for other in api("GET", "pulls?state=open&per_page=100"):
        ref = other["head"]["ref"]
        if ref == branch or not ref.startswith(prefix) or not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?",
                                                                          ref[len(prefix):]):
            continue
        api("POST", "issues/%d/comments" % other["number"], {"body": "Superseded by #%s." % pull.get("number")})
        api("PATCH", "pulls/%d" % other["number"], {"state": "closed"})
        api("DELETE", "git/refs/heads/" + ref)
        print("closed #%d (%s) as superseded" % (other["number"], ref))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Propose bundling a packaged chart into a parent chart of oan-helm.")
    parser.add_argument("--parent", required=True, help="the parent chart directory under charts/")
    parser.add_argument("archive")
    args = parser.parse_args(argv)
    archive = Path(args.archive)
    match = ARCHIVE.fullmatch(archive.name)
    if not match or not archive.is_file():
        print("%s is not a <chart>-<version>.tgz file" % archive, file=sys.stderr)
        return 2
    chart, version = match.group("chart"), match.group("version")
    if os.environ.get("DRY_RUN") == "1":
        print("would propose %s %s in charts/%s of %s" % (chart, version, args.parent, REPOSITORY))
        return 0
    token = os.environ.get("GH_TOKEN")
    if not token:
        print("GH_TOKEN is required", file=sys.stderr)
        return 3
    try:
        return propose(github_api(REPOSITORY, token), args.parent, archive, chart, version)
    except (ValueError, NotFound) as error:
        print("FAIL: %s: %s" % (error.__class__.__name__, error), file=sys.stderr)
        return 2 if isinstance(error, ValueError) else 1
    except (GitHubError, OSError) as error:
        print("FAIL: %s: %s" % (error.__class__.__name__, error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
