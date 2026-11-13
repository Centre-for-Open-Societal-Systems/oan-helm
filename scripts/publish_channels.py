"""Index the chart archives that registry pipelines add to repository/develop, staging and release.

Runs on main after scripts/ci/publish_chart.py adds an archive
(.github/workflows/publish-channels.yaml). For each channel it checks every new archive, seals it in
releases/channels.json, rebuilds index.yaml from the archives present and writes SHA256SUMS. The index
is rebuilt, not merged: `helm repo index --merge` appends and leaves duplicate entries. A sealed archive
that changed or disappeared fails the run.

Every new version is recorded for rollback: releases/history/<channel>/<chart>.md gets the source commit,
a compare link, the image digests read from the archive and the command that returns to that version.
CHANGELOG.md gets a summary line and releases/channels-current.yaml the latest version per channel.

Pipelines describe a version in chart annotations: oan.org/source-repository, oan.org/source-commit,
oan.org/source-subject, oan.org/release-name, oan.org/release-namespace, oan.org/values-overlay and,
when an upgrade needs care, oan.org/upgrade-notes.
"""
import datetime
import json
import re
import subprocess
import tarfile

import yaml

from release import write_changelog
from validate import HELM, ROOT, digest

PUBLIC = ROOT / "repository"
SEALS = ROOT / "releases/channels.json"
HISTORY = ROOT / "releases/history"
CURRENT = ROOT / "releases/channels-current.yaml"
RAW_URL = "https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository"
CHANNELS = {
    "develop": re.compile(r"\d+\.\d+\.\d+-develop\.\d+"),
    "staging": re.compile(r"\d+\.\d+\.\d+-rc\.\d+"),
    "release": re.compile(r"\d+\.\d+\.\d+"),
}
ENVIRONMENT = {"develop": "dev", "staging": "staging", "release": "production"}
SOURCE_MARK = re.compile(r"<!-- source-commit: ([0-9a-f]+) version: (\S+) -->")


def archive_file(archive, name):
    with tarfile.open(archive) as tar:
        for member in tar.getmembers():
            if member.name.count("/") == 1 and member.name.endswith("/" + name):
                return yaml.safe_load(tar.extractfile(member))
    return None


def version_key(version):
    return [int(part) for part in re.findall(r"\d+", version)]


def check_archive(channel, archive):
    metadata = archive_file(archive, "Chart.yaml")
    assert metadata, f"{archive.name} has no Chart.yaml"
    name, version = metadata["name"], metadata["version"]
    assert archive.name == f"{name}-{version}.tgz", f"{archive.name} holds chart {name} {version}"
    assert CHANNELS[channel].fullmatch(version), f"{archive.name}: version {version} does not belong in {channel}"
    return metadata


def check_seals(seals):
    for key, sealed in seals.items():
        path = PUBLIC / key
        assert path.exists(), f"repository/{key} was published and must not disappear"
        assert digest(path) == sealed, f"repository/{key} changed after it was published"


def images(values, path=""):
    """Every image a chart's values pin, as (values path, reference)."""
    found = []
    if not isinstance(values, dict):
        return found
    repository = values.get("repository")
    pin = values.get("tag") or values.get("digest")
    if isinstance(repository, str) and repository and pin and "://" not in repository:
        tag, sha = str(values.get("tag") or ""), str(values.get("digest") or "")
        reference = repository + (":" + tag if tag else "") + ("@" + sha if sha and sha not in tag else "")
        found.append((path, reference))
    for key, value in values.items():
        found += images(value, f"{path}.{key}" if path else str(key))
    return found


def rollback_command(channel, metadata):
    notes = metadata.get("annotations") or {}
    release = notes.get("oan.org/release-name", "<release>")
    namespace = notes.get("oan.org/release-namespace", "<namespace>")
    overlay = notes.get("oan.org/values-overlay", f"helm/environments/{ENVIRONMENT[channel]}/values.yaml")
    url = f"{RAW_URL}/{channel}/{metadata['name']}-{metadata['version']}.tgz"
    return f"helm upgrade {release} {url} -n {namespace} --reset-values -f {overlay} --wait --timeout 15m"


def history_entry(channel, metadata, archive, today, previous):
    notes = metadata.get("annotations") or {}
    source = notes.get("oan.org/source-repository", "")
    commit = notes.get("oan.org/source-commit", "")
    version = metadata["version"]
    lines = [f"## {version}", "", f"<!-- source-commit: {commit or '0'} version: {version} -->",
             f"Published {today}. Archive SHA-256 `{digest(archive)}`.", ""]
    lines.append(f"- Change: {notes.get('oan.org/source-subject', 'No description recorded.')}")
    if source and commit:
        lines.append(f"- Source: [{source}@{commit[:12]}](https://github.com/{source}/commit/{commit})")
        if previous:
            lines.append(f"- Changes since {previous[1]}: https://github.com/{source}/compare/{previous[0]}...{commit}")
    if notes.get("oan.org/upgrade-notes"):
        lines.append(f"- **Upgrade notes:** {notes['oan.org/upgrade-notes']}")
    pinned = images(archive_file(archive, "values.yaml") or {})
    if pinned:
        lines += ["", "| Values path | Image |", "| --- | --- |"]
        lines += [f"| `{path}` | `{reference}` |" for path, reference in pinned]
    lines += ["", "Return to this version:", "", "```sh", rollback_command(channel, metadata), "```", "", ""]
    return "\n".join(lines)


def write_history(channel, metadata, archive, today):
    path = HISTORY / channel / f"{metadata['name']}.md"
    title = (f"# {metadata['name']}: {channel} history\n\nNewest first. Written by scripts/publish_channels.py. "
             "See docs/rollback.md before rolling back.\n\n")
    text = path.read_text(encoding="utf-8") if path.exists() else title
    marks = SOURCE_MARK.findall(text)
    previous = marks[0] if marks and marks[0][0] != "0" else None
    entry = history_entry(channel, metadata, archive, today, previous)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((title + entry + text[len(title):]).encode("utf-8"))


def changelog_entry(published, today):
    lines = [f"## {today}", ""]
    for channel, metadata in published:
        notes = metadata.get("annotations") or {}
        source = notes.get("oan.org/source-repository", "unknown source")
        commit = notes.get("oan.org/source-commit", "unknown")[:12]
        subject = notes.get("oan.org/source-subject", "No description recorded.")
        lines += [f"### {metadata['name']} {metadata['version']} ({channel})", "", f"- {subject} ({source}@{commit})",
                  f"- Images and rollback: [releases/history/{channel}/{metadata['name']}.md]"
                  f"(releases/history/{channel}/{metadata['name']}.md)", ""]
    return "\n".join(lines)


def write_current():
    current = {}
    for channel in CHANNELS:
        latest = {}
        for archive in (PUBLIC / channel).glob("*.tgz"):
            metadata = archive_file(archive, "Chart.yaml")
            if metadata["name"] not in latest or version_key(metadata["version"]) > version_key(latest[metadata["name"]]):
                latest[metadata["name"]] = metadata["version"]
        current[channel] = dict(sorted(latest.items()))
    body = "# Latest version of every chart per channel; maintained by scripts/publish_channels.py.\n"
    CURRENT.write_bytes((body + yaml.safe_dump(current, sort_keys=False)).encode("utf-8"))


def main():
    seals = json.loads(SEALS.read_text(encoding="utf-8")) if SEALS.exists() else {}
    check_seals(seals)
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    published = []
    for channel in CHANNELS:
        folder = PUBLIC / channel
        folder.mkdir(parents=True, exist_ok=True)
        archives = sorted(folder.glob("*.tgz"))
        new = [archive for archive in archives if f"{channel}/{archive.name}" not in seals]
        if not new and (folder / "index.yaml").exists():
            continue
        checked = sorted(((check_archive(channel, archive), archive) for archive in new),
                         key=lambda item: version_key(item[0]["version"]))
        for metadata, archive in checked:
            published.append((channel, metadata))
            seals[f"{channel}/{archive.name}"] = digest(archive)
            write_history(channel, metadata, archive, today)
        subprocess.run([HELM, "repo", "index", str(folder)], check=True)
        (folder / "SHA256SUMS").write_bytes("".join(f"{digest(p)}  {p.name}\n" for p in archives).encode("utf-8"))
    SEALS.write_bytes((json.dumps(seals, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    write_current()
    out = ROOT / ".build"
    out.mkdir(exist_ok=True)
    tags = "".join(f"{metadata['name']}-{metadata['version']}\n" for _, metadata in published)
    (out / "channel-tags.txt").write_text(tags, encoding="utf-8")
    if published:
        write_changelog(changelog_entry(published, today))
    return published


if __name__ == "__main__":
    for channel, metadata in main():
        print(f"{channel}: {metadata['name']} {metadata['version']}")
