"""Index the chart archives that registry pipelines add to repository/develop, staging and release.

Runs on main after scripts/ci/publish_chart.py adds an archive
(.github/workflows/publish-channels.yaml). For each channel it checks every new archive, seals it in
releases/channels.json, rebuilds index.yaml from the archives present and writes SHA256SUMS, then
adds a CHANGELOG.md entry. The index is rebuilt, not merged: `helm repo index --merge` appends and
leaves duplicate entries. A sealed archive that changed or disappeared fails the run.

Pipelines describe the source in the chart annotations oan.org/source-repository,
oan.org/source-commit and oan.org/source-subject; the changelog line is built from them.
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
CHANNELS = {
    "develop": re.compile(r"0\.0\.0-develop\.\d+"),
    "staging": re.compile(r"\d+\.\d+\.\d+-rc\.\d+"),
    "release": re.compile(r"\d+\.\d+\.\d+"),
}


def chart_metadata(archive):
    with tarfile.open(archive) as tar:
        for member in tar.getmembers():
            if member.name.count("/") == 1 and member.name.endswith("/Chart.yaml"):
                return yaml.safe_load(tar.extractfile(member))
    raise AssertionError(f"{archive.name} has no Chart.yaml")


def check_archive(channel, archive):
    metadata = chart_metadata(archive)
    name, version = metadata["name"], metadata["version"]
    assert archive.name == f"{name}-{version}.tgz", f"{archive.name} holds chart {name} {version}"
    assert CHANNELS[channel].fullmatch(version), f"{archive.name}: version {version} does not belong in {channel}"
    return metadata


def check_seals(seals):
    for key, sealed in seals.items():
        path = PUBLIC / key
        assert path.exists(), f"repository/{key} was published and must not disappear"
        assert digest(path) == sealed, f"repository/{key} changed after it was published"


def changelog_entry(published, today):
    lines = [f"## {today}", ""]
    for channel, metadata in published:
        notes = metadata.get("annotations") or {}
        source = notes.get("oan.org/source-repository", "unknown source")
        commit = notes.get("oan.org/source-commit", "unknown")[:12]
        subject = notes.get("oan.org/source-subject", "No description recorded.")
        lines += [f"### {metadata['name']} {metadata['version']} ({channel})", "", f"- {subject} ({source}@{commit})", ""]
    return "\n".join(lines)


def main():
    seals = json.loads(SEALS.read_text(encoding="utf-8")) if SEALS.exists() else {}
    check_seals(seals)
    published = []
    for channel in CHANNELS:
        folder = PUBLIC / channel
        folder.mkdir(parents=True, exist_ok=True)
        archives = sorted(folder.glob("*.tgz"))
        new = [archive for archive in archives if f"{channel}/{archive.name}" not in seals]
        if not new and (folder / "index.yaml").exists():
            continue
        for archive in new:
            published.append((channel, check_archive(channel, archive)))
            seals[f"{channel}/{archive.name}"] = digest(archive)
        subprocess.run([HELM, "repo", "index", str(folder)], check=True)
        (folder / "SHA256SUMS").write_bytes("".join(f"{digest(p)}  {p.name}\n" for p in archives).encode("utf-8"))
    SEALS.write_bytes((json.dumps(seals, indent=2, sort_keys=True) + "\n").encode("utf-8"))
    out = ROOT / ".build"
    out.mkdir(exist_ok=True)
    tags = "".join(f"{metadata['name']}-{metadata['version']}\n" for _, metadata in published)
    (out / "channel-tags.txt").write_text(tags, encoding="utf-8")
    if published:
        write_changelog(changelog_entry(published, datetime.datetime.now(datetime.timezone.utc).date().isoformat()))
    return published


if __name__ == "__main__":
    for channel, metadata in main():
        print(f"{channel}: {metadata['name']} {metadata['version']}")
