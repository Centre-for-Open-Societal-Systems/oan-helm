"""Version, package and record every chart whose source changed since its last release.

Runs on main after a merge (.github/workflows/release.yaml). Each chart under
charts/ and addons/registry-dashboards/ is fingerprinted and compared with the
fingerprint recorded for its current version's archive in releases/artifacts.json.
A changed chart gets the next version (1.0.0-dev.16 -> 1.0.0-dev.17, stable
1.0.0 -> 1.0.1), is packaged into repository/, added to index.yaml and
SHA256SUMS, and gets a CHANGELOG.md entry from the commits that touched it.
A version already raised by hand in the PR is packaged as it is.
Published archives are never rewritten.
"""
import argparse
import datetime
import io
import json
import re
import shutil
import subprocess
import tarfile

from validate import ROOT, build_directory, digest, fingerprint, merge_index, read, run

CHARTS = sorted(ROOT.glob("charts/*/Chart.yaml")) + sorted(ROOT.glob("addons/registry-dashboards/*/Chart.yaml"))
PUBLIC = ROOT / "repository"
ARTIFACTS = ROOT / "releases/artifacts.json"
CHANGELOG = ROOT / "CHANGELOG.md"
CHANGELOG_MARKER = "<!-- Releases are inserted below this line by scripts/release.py. -->"
RELEASE_SUBJECT = "chore(release):"
SEMVER = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True, encoding="utf-8").stdout.strip()


def next_version(version):
    match = SEMVER.fullmatch(version)
    assert match, f"Chart version is not Semantic Versioning: {version}"
    major, minor, patch, prerelease = match.groups()
    if prerelease is None:
        return f"{major}.{minor}.{int(patch) + 1}"
    parts = prerelease.split(".")
    if parts[-1].isdigit():
        parts[-1] = str(int(parts[-1]) + 1)
    else:
        parts.append("1")
    return f"{major}.{minor}.{patch}-{'.'.join(parts)}"


def set_version(metadata, version):
    text = metadata.read_text(encoding="utf-8")
    updated, count = re.subn(r"(?m)^version:[ \t]*\S+[ \t]*$", f"version: {version}", text)
    assert count == 1, f"Expected one top-level version in {metadata}"
    metadata.write_bytes(updated.encode("utf-8"))


def archive_commit(archive_name):
    return git("log", "-1", "--diff-filter=A", "--format=%H", "--", f"repository/{archive_name}") or None


def recorded_source(chart, archive_name, artifacts):
    """Fingerprint of the source the published archive was built from, or None if unpublished."""
    if archive_name in artifacts:
        return artifacts[archive_name]["sourceSha256"]
    archive = PUBLIC / archive_name
    if not archive.exists():
        return None
    # The archive predates source sealing: seal the chart as committed with it.
    commit = archive_commit(archive_name)
    assert commit, f"{archive_name} exists but was never committed"
    relative = chart.relative_to(ROOT).as_posix()
    data = subprocess.run(["git", "archive", "--format=tar", commit, relative], cwd=ROOT, check=True, capture_output=True).stdout
    with build_directory() as temp:
        with tarfile.open(fileobj=io.BytesIO(data)) as tar:
            tar.extractall(temp, filter="data")
        artifacts[archive_name] = {"sha256": digest(archive), "sourceSha256": fingerprint(temp / relative)}
    return artifacts[archive_name]["sourceSha256"]


def published_versions(name):
    index = read(PUBLIC / "index.yaml")
    return [entry["version"] for entry in index["entries"].get(name, [])]


def changes(chart, previous):
    """Commit subjects that touched the chart since its previous archive was committed."""
    since = archive_commit(f"{chart.name}-{previous}.tgz") if previous else None
    revisions = [f"{since}..HEAD"] if since else ["HEAD"]
    log = git("log", "--no-merges", "--format=%h%x09%s", *revisions, "--", chart.relative_to(ROOT).as_posix())
    lines = [line.split("\t", 1) for line in log.splitlines() if line]
    return [(sha, subject) for sha, subject in lines if not subject.startswith(RELEASE_SUBJECT)]


def changelog_entry(released, today):
    lines = [f"## {today}", ""]
    for chart, previous, version in released:
        lines.append(f"### {chart.name} {version}")
        lines.append("")
        lines.append(f"Previous version: {previous}." if previous else "First published version.")
        lines.append("")
        entries = changes(chart, previous)
        lines.extend(f"- {subject} ({sha})" for sha, subject in entries[:50])
        if len(entries) > 50:
            lines.append(f"- ...and {len(entries) - 50} earlier commits")
        if not entries:
            lines.append("- No commit touched the chart source since the previous version.")
        lines.append("")
    return "\n".join(lines)


def write_changelog(entry):
    text = CHANGELOG.read_text(encoding="utf-8")
    assert CHANGELOG_MARKER in text, f"{CHANGELOG.name} lost its release marker"
    CHANGELOG.write_bytes(text.replace(CHANGELOG_MARKER, CHANGELOG_MARKER + "\n\n" + entry.rstrip("\n"), 1).encode("utf-8"))


def write_current():
    versions = {read(m)["name"]: read(m)["version"] for m in CHARTS}
    body = "# Latest version of every chart; maintained by scripts/release.py.\ncharts:\n"
    body += "".join(f"  {name}: {version}\n" for name, version in sorted(versions.items()))
    (ROOT / "releases/current.yaml").write_bytes(body.encode("utf-8"))


def main(dry_run=False):
    artifacts = json.loads(ARTIFACTS.read_text(encoding="utf-8"))
    sealed = len(artifacts)
    released = []
    for metadata in CHARTS:
        chart = metadata.parent
        info = read(metadata)
        name, version = info["name"], info["version"]
        assert name == chart.name, f"{metadata}: chart name must match its directory"
        recorded = recorded_source(chart, f"{name}-{version}.tgz", artifacts)
        if recorded == fingerprint(chart):
            continue
        if recorded is None:
            # Version raised by hand in the PR: publish it as it is.
            earlier = [v for v in published_versions(name) if v != version]
            previous = earlier[0] if earlier else None
        else:
            previous = version
            version = next_version(version)
            assert not (PUBLIC / f"{name}-{version}.tgz").exists(), f"{name}-{version}.tgz already published"
        released.append((chart, previous, version))
        print(f"{name}: {previous or '(new)'} -> {version}")
    if dry_run:
        return released
    if not released:
        if len(artifacts) != sealed:
            ARTIFACTS.write_text(json.dumps(artifacts, indent=2) + "\n", encoding="utf-8", newline="\n")
        print("No chart source changed since its published version.")
        return released
    archives = []
    with build_directory() as temp:
        for chart, previous, version in released:
            if read(chart / "Chart.yaml")["version"] != version:
                set_version(chart / "Chart.yaml", version)
            archive_name = f"{chart.name}-{version}.tgz"
            run("package", chart, "--destination", temp)
            shutil.copy2(temp / archive_name, PUBLIC / archive_name)
            artifacts[archive_name] = {"sha256": digest(PUBLIC / archive_name), "sourceSha256": fingerprint(chart)}
            archives.append(PUBLIC / archive_name)
    merge_index(PUBLIC, archives)
    (PUBLIC / "SHA256SUMS").write_bytes("".join(f"{digest(p)}  {p.name}\n" for p in sorted(PUBLIC.glob("*.tgz"))).encode("utf-8"))
    ARTIFACTS.write_text(json.dumps(artifacts, indent=2) + "\n", encoding="utf-8", newline="\n")
    write_current()
    write_changelog(changelog_entry(released, datetime.datetime.now(datetime.timezone.utc).date().isoformat()))
    summary = ", ".join(f"{chart.name} {version}" for chart, _, version in released)
    out = ROOT / ".build"
    out.mkdir(exist_ok=True)
    (out / "release-message.txt").write_text(f"{RELEASE_SUBJECT} {summary}\n\n" + "\n".join(
        f"- {chart.name}: {previous or '(new)'} -> {version}" for chart, previous, version in released) + "\n", encoding="utf-8")
    (out / "release-tags.txt").write_text("".join(f"{chart.name}-{version}\n" for chart, _, version in released), encoding="utf-8")
    return released


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="only print which charts would be released")
    main(parser.parse_args().dry_run)
