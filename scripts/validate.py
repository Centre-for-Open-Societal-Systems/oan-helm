"""Validate and optionally package the five charts without accessing Kubernetes.

An offline mirror is derived only from bundled dependency sources. Resolving
against it checks Helm's locks without claiming a fresh upstream download.
Use --online to also resolve the locks against their original repositories.
"""
import argparse
from contextlib import contextmanager
import functools
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import threading
import uuid
from urllib.request import urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
HELM = os.environ.get("HELM", "helm")
CHARTS = sorted((ROOT / "charts").glob("*/Chart.yaml"))
EXPECTED = {f"openg2p-{x}-registry" for x in ["farmer", "cropsown", "livestock", "da"]} | {"openg2p-commons-services"}
SYNTHETIC_IMAGE = {"repository": "example.invalid/render-only", "digest": "sha256:" + "a" * 64}


def run(*args, env=None):
    result = subprocess.run([HELM, *map(str, args)], cwd=ROOT, text=True, encoding="utf-8", capture_output=True, env=env)
    if result.returncode:
        raise RuntimeError(f"helm {' '.join(map(str, args))}:\n{result.stdout}\n{result.stderr}")
    return result.stdout


def read(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint(chart):
    h = hashlib.sha256()
    for path in sorted(chart.rglob("*")):
        if path.is_file():
            h.update(path.relative_to(chart).as_posix().encode() + b"\0" + path.read_bytes() + b"\0")
    return h.hexdigest()


@contextmanager
def build_directory():
    # Normal directory permissions also work in Windows managed workspaces.
    # Keep diagnostics under the ignored .build directory for inspection.
    path = ROOT / ".build" / ("run-" + uuid.uuid4().hex)
    path.mkdir(parents=True)
    yield path


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


@contextmanager
def server(directory):
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(directory)))
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{httpd.server_port}"
    finally:
        httpd.shutdown()
        thread.join()
        httpd.server_close()


def documents(rendered, namespace):
    docs = [x for x in yaml.safe_load_all(rendered) if x]
    identities = []
    for doc in docs:
        meta = doc.get("metadata", {})
        if doc["kind"] != "Namespace":
            assert meta.get("namespace", namespace) == namespace, (doc["kind"], meta)
        identities.append((doc["apiVersion"], doc["kind"], meta.get("namespace", namespace), meta["name"]))
    assert len(identities) == len(set(identities)), "Duplicate resource identity"
    return docs, set(identities)


def image_refs(docs):
    refs = set()
    def visit(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "image" and isinstance(value, str):
                    refs.add(value)
                else:
                    visit(value)
        elif isinstance(obj, list):
            for value in obj:
                visit(value)
    visit(docs)
    return sorted(refs)


def secret_refs(docs):
    refs = set()
    def visit(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "secretKeyRef":
                    refs.add((value["name"], value["key"]))
                else:
                    visit(value)
        elif isinstance(obj, list):
            for value in obj:
                visit(value)
    visit(docs)
    return refs


def offline_resolution(build):
    mirror = build / "mirror"
    mirror.mkdir()
    urls = set()
    for metadata in CHARTS:
        chart = metadata.parent
        config = read(metadata)
        for dep in config.get("dependencies", []):
            urls.add(dep["repository"])
            dest = mirror / f'{dep["name"]}-{dep["version"]}.tgz'
            if dest.exists():
                continue
            archive = chart / "charts" / dest.name
            if archive.exists():
                shutil.copy2(archive, dest)
            else:
                source = chart / "charts" / dep["name"]
                assert source.is_dir(), f"Missing bundled dependency {source}"
                run("package", source, "--destination", mirror)
    with server(mirror) as mirror_url:
        run("repo", "index", mirror, "--url", mirror_url)
        cache = build / "repository-cache"
        cache.mkdir()
        entries = []
        for i, url in enumerate(sorted(urls)):
            name = f"offline-{i}"
            entries.append({"name": name, "url": url})
            shutil.copy2(mirror / "index.yaml", cache / f"{name}-index.yaml")
        config = build / "repositories.yaml"
        config.write_text(yaml.safe_dump({"apiVersion": "v1", "repositories": entries}))
        env = dict(os.environ, HELM_REPOSITORY_CONFIG=str(config), HELM_REPOSITORY_CACHE=str(cache))
        for metadata in CHARTS:
            target = build / "resolved" / metadata.parent.name
            shutil.copytree(metadata.parent, target)
            # Helm validates the dependency digest and downloads locked packages
            # from this loopback mirror. Original chart URLs are unchanged.
            run("dependency", "build", target, "--skip-refresh", env=env)
            assert read(target / "Chart.lock") == read(metadata.parent / "Chart.lock")
            for ns in ["verify-a", "verify-b"]:
                original, identities = documents(run("template", "verify", metadata.parent, "--namespace", ns), ns)
                resolved, new_identities = documents(run("template", "verify", target, "--namespace", ns), ns)
                assert identities == new_identities
                assert image_refs(original) == image_refs(resolved)
                assert secret_refs(original) == secret_refs(resolved)


def package(report):
    public = ROOT / "docs"
    public.mkdir(exist_ok=True)
    recorded = ROOT / "releases/artifacts.json"
    prior = json.loads(recorded.read_text()) if recorded.exists() else {}
    with build_directory() as temp:
        for metadata in CHARTS:
            chart = metadata.parent
            info = read(metadata)
            archive_name = f'{info["name"]}-{info["version"]}.tgz'
            archive = public / archive_name
            source_sha = fingerprint(chart)
            if archive.exists():
                assert prior[archive_name]["sourceSha256"] == source_sha, f"Immutable archive source changed: {archive_name}"
                assert prior[archive_name]["sha256"] == digest(archive), f"Immutable archive bytes changed: {archive_name}"
            else:
                run("package", chart, "--destination", temp)
                shutil.copy2(temp / archive_name, archive)
                prior[archive_name] = {"sha256": digest(archive), "sourceSha256": source_sha}
            for ns in ["verify-a", "verify-b"]:
                packaged_docs, from_package = documents(run("template", "verify", archive, "--namespace", ns), ns)
                source_docs, from_source = documents(run("template", "verify", chart, "--namespace", ns), ns)
                assert from_package == from_source
                assert image_refs(packaged_docs) == image_refs(source_docs)
                assert secret_refs(packaged_docs) == secret_refs(source_docs)
            with tarfile.open(archive) as tar:
                assert not any(Path(member.name).name in {"values-live.yaml", "values-dev.yaml", "values-new-dev.yaml"} or Path(member.name).name.startswith(("private-values", ".env")) for member in tar.getmembers()), "Private/environment capture in package"
        old_index = public / "index.yaml"
        if old_index.exists():
            previous = temp / "index.yaml"
            shutil.copy2(old_index, previous)
            run("repo", "index", public, "--merge", previous)
        else:
            run("repo", "index", public)
    # Helm emits relative archive URLs when --url is omitted.
    index = read(public / "index.yaml")
    with server(public) as base:
        published = yaml.safe_load(urlopen(f"{base}/index.yaml").read())
        assert published == index
        helm_cache = ROOT / ".build/http-repository-cache"
        helm_cache.mkdir(exist_ok=True)
        env = dict(os.environ, HELM_REPOSITORY_CACHE=str(helm_cache), HELM_REPOSITORY_CONFIG=str(ROOT / ".build/http-repositories.yaml"))
        run("repo", "add", "coss", base, "--force-update", env=env)
        for entries in index["entries"].values():
            for entry in entries:
                for url in entry["urls"]:
                    assert url == Path(url).name and url.endswith(".tgz"), url
                    data = urlopen(f"{base}/{url}").read()
                    assert hashlib.sha256(data).hexdigest() == entry["digest"]
                    selected = yaml.safe_load(run("show", "chart", "coss/" + entry["name"], "--version", entry["version"], env=env))
                    assert selected["name"] == entry["name"] and selected["version"] == entry["version"]
                    documents(run("template", "http-check", "coss/" + entry["name"], "--version", entry["version"], "--namespace", "http-check", env=env), "http-check")
    recorded.write_text(json.dumps(prior, indent=2) + "\n")
    (public / "SHA256SUMS").write_text("".join(f"{digest(p)}  {p.name}\n" for p in sorted(public.glob("*.tgz"))), encoding="utf-8")
    report["packages"] = len(list(public.glob("*.tgz")))
    report["index"] = "Relative URLs, SHA-256, HTTP download, exact Helm version selection and repository-based renders verified against loopback server"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", action="store_true")
    parser.add_argument("--online", action="store_true")
    parser.add_argument("--release-ready", action="store_true")
    args = parser.parse_args()
    assert {m.parent.name for m in CHARTS} == EXPECTED
    build_root = ROOT / ".build"
    build_root.mkdir(exist_ok=True)
    report = {"helm": run("version", "--short").strip(), "clusterAccess": False, "charts": {}, "upstreamResolution": "not attempted"}
    baselines = json.loads((ROOT / "releases/resource-baselines.json").read_text())
    with build_directory() as build:
        offline_resolution(build)
        report["offlineResolution"] = "All five locks resolved from dependencies bundled with verified source packages"
        for metadata in CHARTS:
            chart = metadata.parent
            info = read(metadata)
            assert info["version"] == "1.0.0-dev.1"
            values = read(chart / "values.yaml")
            run("lint", chart, "--strict")
            example_name = "commons-services" if chart.name == "openg2p-commons-services" else chart.name.removeprefix("openg2p-").removesuffix("-registry")
            example = ROOT / "examples/dev" / (example_name + ".yaml")
            run("lint", chart, "--strict", "-f", example)
            documents(run("template", "verify", chart, "--namespace", "verify-a", "-f", example), "verify-a")
            baseline, identities = documents(run("template", "verify", chart, "--namespace", "verify-a"), "verify-a")
            upstream = baselines[chart.name]
            assert identities == {tuple(x) for x in upstream["resourceIdentities"]}, "Upstream resource names changed"
            assert secret_refs(baseline) == {tuple(x) for x in upstream["secretKeyReferences"]}, "Upstream Secret references changed"
            selectors = {doc["kind"] + "/" + doc["metadata"]["name"]: doc["spec"].get("selector") for doc in baseline if doc["kind"] in ["Deployment", "StatefulSet", "Service"]}
            assert selectors == upstream["selectors"], "Upstream selectors changed"
            documents(run("template", "verify", chart, "--namespace", "verify-b"), "verify-b")
            components = ["aggregationApi"] if chart.name == "openg2p-commons-services" else ["dashboardApi", "dashboardUi"]
            for component in components:
                assert values[component]["enabled"] is False
                fixture = {component: {"enabled": True, "image": dict(SYNTHETIC_IMAGE), "envFrom": [{"secretRef": {"name": "render-only-config"}}], "imagePullSecrets": [{"name": "render-only-pull"}]}}
                test_values = build / "values.yaml"
                test_values.write_text(yaml.safe_dump(fixture))
                enabled, enabled_ids = documents(run("template", "verify", chart, "--namespace", "verify-a", "-f", test_values), "verify-a")
                assert identities <= enabled_ids, "Enabling an add-on removed an existing resource"
                assert any(ref.startswith("example.invalid/render-only@sha256:") for ref in image_refs(enabled))
                deployment = next(x for x in enabled if x["kind"] == "Deployment" and x["metadata"]["name"] == "verify-" + {"dashboardApi": "dashboard-api", "dashboardUi": "dashboard-ui", "aggregationApi": "aggregation-api"}[component])
                pod = deployment["spec"]["template"]["spec"]
                assert pod["imagePullSecrets"] == [{"name": "render-only-pull"}]
                assert pod["containers"][0]["envFrom"] == fixture[component]["envFrom"]
                if component == "aggregationApi":
                    assert pod["containers"][0]["ports"][0]["containerPort"] == 8100
                if component == "dashboardApi" and chart.name != "openg2p-da-registry":
                    password = next(x for x in pod["containers"][0]["env"] if x["name"] == "PGPASSWORD")
                    assert password["valueFrom"] == {"secretKeyRef": {"name": "verify", "key": "verify-db-user"}}
                # Default empty images must not render enabled add-ons.
                bad = subprocess.run([HELM, "template", "verify", str(chart), "--set", f"{component}.enabled=true", "--set", f"{component}.image.repository=", "--set", f"{component}.image.tag=", "--set", f"{component}.image.digest="], capture_output=True)
                assert bad.returncode != 0, f"{component} accepts a missing image"
                fixture[component]["image"]["digest"] = "sha256:invalid"
                test_values.write_text(yaml.safe_dump(fixture))
                bad = subprocess.run([HELM, "template", "verify", str(chart), "-f", str(test_values)], capture_output=True)
                assert bad.returncode != 0, f"{component} accepts an invalid digest"
                # Existing API DB Secret references must remain present.
                assert secret_refs(baseline) <= secret_refs(enabled)
            report["charts"][chart.name] = {"lint": "strict passed", "resources": len(identities), "namespaces": ["verify-a", "verify-b"], "preservation": "upstream resource identities, selectors and Secret references match baseline", "baselineScope": upstream["scope"], "optionalWorkloads": "enabled/disabled, digest, pull Secret, envFrom and missing-image/invalid-digest rejection passed", "defaultImageReferences": image_refs(baseline)}
            report["charts"][chart.name]["devExample"] = str(example.relative_to(ROOT)) + ": strict lint and render passed"
        if args.online:
            online_cache = build / "online-cache"
            online_cache.mkdir()
            online_config = build / "online-repositories.yaml"
            env = dict(os.environ, HELM_REPOSITORY_CONFIG=str(online_config), HELM_REPOSITORY_CACHE=str(online_cache))
            urls = sorted({dep["repository"] for metadata in CHARTS for dep in read(metadata).get("dependencies", [])})
            for i, url in enumerate(urls):
                run("repo", "add", f"upstream-{i}", url, env=env)
            for metadata in CHARTS:
                target = build / "online" / metadata.parent.name
                shutil.copytree(metadata.parent, target)
                run("dependency", "build", target, env=env)
                assert read(target / "Chart.lock") == read(metadata.parent / "Chart.lock")
                actual, actual_ids = documents(run("template", "verify", target, "--namespace", "verify-a"), "verify-a")
                bundled, bundled_ids = documents(run("template", "verify", metadata.parent, "--namespace", "verify-a"), "verify-a")
                assert actual_ids == bundled_ids
                assert image_refs(actual) == image_refs(bundled)
                assert secret_refs(actual) == secret_refs(bundled)
            report["upstreamResolution"] = "passed"
        if args.package:
            package(report)
    (ROOT / "releases/validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Validated {len(CHARTS)} charts: strict lint, locked dependencies, namespaces and optional workloads.")
    if args.package:
        print("Packaged five charts; archives and relative Helm index verified over local HTTP.")
    if args.release_ready:
        release = read(ROOT / "releases/1.0.0-dev.1.yaml")
        assert release["readyForPublication"] is True
        assert not release["publicationBlockers"], "Publication blocked: " + "; ".join(release["publicationBlockers"])


if __name__ == "__main__":
    main()
