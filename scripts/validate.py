"""Validate and optionally package the OAN charts without accessing Kubernetes.

An offline mirror is derived only from bundled dependency sources. Resolving
against it checks Helm's locks without claiming a fresh upstream download.
Use --online to also resolve the locks against their original repositories.
"""
import argparse
import base64
from contextlib import contextmanager
import functools
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import re
from pathlib import Path
import shutil
import subprocess
import tarfile
import threading
import uuid
from urllib.request import urlopen
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?")
HELM = os.environ.get("HELM", "helm")
BLOCKED_REGISTRIES = set()
REFACTOR_GATE = "develop-refactor is incomplete:"
ADDON_RENDER_ARGS = ("--set","image.repository=example.invalid/verification-dashboard","--set","image.tag=verification",
    "--set","ecrPullSecret.enabled=false","--set","iam.url=https://iam.verification.invalid",
    "--set","iam.cookieDomain=.verification.invalid","--set","domain=verification.invalid")
SYNTHETIC_IMAGE = {"repository": "example.invalid/render-only", "digest": "sha256:" + "a" * 64}
COSS = "https://github.com/Centre-for-Open-Societal-Systems/"
APPLICATION_SOURCES = {
    "openg2p-farmer-registry": [COSS + "farmer-registry"],
    "openg2p-cropsown-registry": [COSS + "cropsown-regsitry"],
    "openg2p-livestock-registry": [COSS + "livestock-registry"],
    "openg2p-da-registry": [COSS + "da-registry"],
    "openg2p-commons-services": [COSS + "consent-management", COSS + "oan-aggregation-api"],
    "oan-sandbox": [COSS + "sandbox-platform"],
}
EXPECTED = set(APPLICATION_SOURCES)
CHARTS = [m for m in sorted((ROOT / "charts").glob("*/Chart.yaml")) if m.parent.name in EXPECTED]


def check_oan_metadata(info, chart):
    annotations = info["annotations"]
    assert annotations["catalog.cattle.io/display-name"].startswith("OAN ")
    assert annotations["oan.org/owner"] == "OpenAgriNet (OAN) / COSS"
    assert annotations["oan.org/chart-source"] == COSS + "oan-helm/tree/main/charts/" + chart.name
    assert info["home"].startswith(COSS)
    assert "OAN" in info["description"]
    for url in APPLICATION_SOURCES[chart.name]:
        assert url in info["sources"], "Application GitHub source missing"
        for filename in ["README.md", "app-readme.md"]:
            content = (chart / filename).read_text(encoding="utf-8")
            assert content.startswith("# OAN ") and url in content


def run(*args, env=None):
    result = subprocess.run([HELM, *map(str, args)], cwd=ROOT, text=True, encoding="utf-8", capture_output=True, env=env)
    if result.returncode:
        raise RuntimeError(f"helm {' '.join(map(str, args))}:\n{result.stdout}\n{result.stderr}")
    return result.stdout


def verify_refactor_gate(chart, namespace="verify-a", env=None):
    result = subprocess.run([HELM,"template","verify",str(chart),"--namespace",namespace],
                            cwd=ROOT,capture_output=True,text=True,encoding="utf-8",env=env)
    assert result.returncode != 0 and REFACTOR_GATE in result.stderr, "Candidate must fail at the explicit promotion gate"
    assert not result.stdout.strip(), "Blocked candidate emitted workload manifests"


def read(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint(chart):
    h = hashlib.sha256()
    # pathlib uses platform-specific ordering (Windows compares case-insensitively).
    # Hash portable relative strings so a fresh Linux checkout has the same seal.
    for path in sorted(chart.rglob("*"), key=lambda p: p.relative_to(chart).as_posix()):
        if path.is_file() and "__pycache__" not in path.relative_to(chart).parts and path.suffix != ".pyc":
            data = path.read_bytes()
            if path.suffix in {".yaml", ".yml", ".tpl", ".md", ".json", ".sh", ".lock"} or path.name == ".helmignore":
                assert b"\r\n" not in data, f"Chart source must use repository LF line endings before packaging: {path}"
            h.update(path.relative_to(chart).as_posix().encode() + b"\0" + data + b"\0")
    return h.hexdigest()


# Rancher stores the chart archive and the release's saved values together in one
# helm-operation Secret, which Kubernetes caps at 1 MiB. Keep room for the values.
MAX_ARCHIVE_BYTES = 900 * 1024


def is_subchart_doc(member):
    """Documentation inside a bundled dependency: never rendered, only package weight."""
    parts = member.split("/")
    if "charts" not in parts[1:-1]:
        return False
    inner = parts[parts.index("charts", 1) + 1:]
    return parts[-1].lower().endswith(".md") or "ci" in inner[1:-1]


def package_chart(chart, destination):
    """helm package, minus bundled dependencies' docs; returns the archive path."""
    run("package", chart, "--destination", destination)
    info = read(chart / "Chart.yaml")
    archive = Path(destination) / f'{info["name"]}-{info["version"]}.tgz'
    slim = archive.with_suffix(".slim")
    with tarfile.open(archive) as source, tarfile.open(slim, "w:gz") as target:
        for member in source.getmembers():
            if not is_subchart_doc(member.name):
                target.addfile(member, source.extractfile(member) if member.isfile() else None)
    slim.replace(archive)
    size = archive.stat().st_size
    assert size <= MAX_ARCHIVE_BYTES, (
        f"{archive.name} is {size} bytes; Rancher cannot install archives over "
        f"{MAX_ARCHIVE_BYTES} bytes together with saved values (1 MiB Secret limit)")
    return archive


def merge_index(public, archives):
    """Add only the given new archives to public/index.yaml; existing entries keep their bytes."""
    if not archives:
        return
    with build_directory() as temp:
        for archive in archives:
            shutil.copy2(archive, temp / archive.name)
        # Helm emits relative archive URLs when --url is omitted. Entries already
        # in the merged index are kept as they are, including their timestamps.
        run("repo", "index", temp, "--merge", public / "index.yaml")
        shutil.copy2(temp / "index.yaml", public / "index.yaml")


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


def stable_identities(identities):
    # Upstream includes a settings hash in Keycloak initialization Job names.
    # URL changes intentionally change that hash; stable workload owners do not.
    return {(api, kind, namespace, re.sub(r"(-keycloak-init-\d+|-schema-init)-[a-f0-9]{8}$", r"\1-<settings-hash>", name) if kind == "Job" else name) for api, kind, namespace, name in identities}


def check_upgrade_safe_jobs(docs):
    # Rancher runs a real helm upgrade: hooks run, and Jobs that deleted
    # themselves after finishing are recreated. Every Job must survive that.
    for doc in docs:
        if doc["kind"] != "Job":
            continue
        meta, spec = doc["metadata"], doc["spec"]
        annotations = meta.get("annotations") or {}
        if annotations.get("helm.sh/hook"):
            assert "before-hook-creation" in annotations.get("helm.sh/hook-delete-policy", ""), meta["name"]
        else:
            assert "ttlSecondsAfterFinished" in spec or re.search(r"-\d+$", meta["name"]), f"{meta['name']}: plain Job neither expires nor carries the revision"
        pod = json.dumps(spec["template"]["spec"])
        if "postgres-init.sh" in pod and "mosipid/" in pod:
            assert "skipping (deploy.sh drops the database)" in pod, f"{meta['name']}: MOSIP deploy.sh drops the database; guard it"


def check_dev_endpoints(docs):
    policy = read(ROOT / "environments/dev/endpoints.yaml")
    allowed = set(policy["publicHosts"].values())
    texts = [json.dumps(docs)]
    for doc in docs:
        if doc["kind"] == "Secret":
            for value in doc.get("data", {}).values():
                try:
                    texts.append(base64.b64decode(value).decode("utf-8"))
                except (ValueError, UnicodeDecodeError):
                    pass
    bad = set()
    for text in texts:
        for url in re.findall(r'https?://[^\s"\'<>\\]+', text):
            host = urlsplit(url).hostname or ""
            if host.endswith((".openg2p.org", ".openg2p.test", ".commons-dev.oanstaging.com", ".farmer-dev.oanstaging.com", ".crop-dev.oanstaging.com", ".livestock-dev.oanstaging.com")):
                bad.add(host)
            if host.endswith(".oanstaging.com") and host not in allowed:
                bad.add(host)
    # Report hostnames only, never decoded Secret contents.
    assert not bad, "Unmigrated or unconfirmed dev endpoint hostnames: " + ", ".join(sorted(bad))
    for doc in docs:
        if doc["kind"] == "VirtualService":
            assert all(not host.endswith((".openg2p.org", ".openg2p.test")) for host in doc["spec"]["hosts"])
            public_hosts = [host for host in doc["spec"]["hosts"] if host.endswith(".oanstaging.com")]
            if public_hosts:
                assert all(host.endswith(".development.oanstaging.com") for host in public_hosts), "Public chart route outside the development domain"
                assert doc["spec"]["gateways"] == ["istio-system/development"], "Public route does not use the environment Gateway"


def deployment_env(docs, name):
    deployment = next(x for x in docs if x["kind"] == "Deployment" and x["metadata"]["name"] == name)
    return {item["name"]: item.get("value") for container in deployment["spec"]["template"]["spec"]["containers"] for item in container.get("env", [])}


def check_url_contract(chart, docs):
    hosts = read(ROOT / "environments/dev/endpoints.yaml")["publicHosts"]
    if chart.name in {"openg2p-farmer-registry", "openg2p-cropsown-registry", "openg2p-livestock-registry"}:
        name = chart.name.removeprefix("openg2p-").removesuffix("-registry")
        env = deployment_env(docs, "verify-staff-portal-ui")
        assert env["APP_URL"] == "https://" + hosts[name]
        assert env["IAM_URL"] == "https://" + hosts["iam"]
        assert env["COOKIE_DOMAIN"] == ".development.oanstaging.com"
        assert env["KEYCLOAK_LOGOUT_URL"] == "https://" + hosts["keycloak"] + "/realms/staff/protocol/openid-connect/logout"
        env = deployment_env(docs, "verify-staff-portal-api")
        assert env["REGISTRY_STAFF_PORTAL_API_AWE_BASE_URL"] == "http://commons-services-awe.commons.svc.cluster.local"
        env = deployment_env(docs, "verify-partner-api")
        assert env["REGISTRY_PARTNER_API_CONSENT_MANAGER_URL"] == "http://commons-services-cm-partner-api.commons.svc.cluster.local"
    elif chart.name == "openg2p-commons-services":
        env = deployment_env(docs, "verify-cm-api")
        assert env["CONSENT_MANAGER_AUTH_ISSUER"] == "https://" + hosts["keycloak"] + "/realms/staff"
        assert env["CONSENT_MANAGER_AUTH_JWKS_URL"] == "http://commons-keycloak.commons.svc.cluster.local:80/realms/staff/protocol/openid-connect/certs"
        assert env["CONSENT_MANAGER_AWE_CALLBACK_URL"] == "http://verify-cm-api.verify-a.svc.cluster.local/consent/v1/awe/webhooks/decision"
        env = deployment_env(docs, "verify-pm-staff-portal-ui")
        assert env["IAM_URL"] == "https://" + hosts["iam"]
        assert env["KEYCLOAK_LOGOUT_URL"] == "https://" + hosts["keycloak"] + "/realms/staff/protocol/openid-connect/logout"


def check_sandbox(chart, values, build, migration):
    """OAN Sandbox: everything off by default; enabled API/web/route render correctly."""
    hosts = read(ROOT / "environments/dev/endpoints.yaml")["publicHosts"]
    for key in ["api", "web", "virtualService"]:
        assert values[key]["enabled"] is False, f"oan-sandbox {key} must be disabled by default"
    fixture = {
        "secret": {"name": "render-only-config"},
        "virtualService": {"enabled": True},
        **{key: {"enabled": True, "image": dict(SYNTHETIC_IMAGE), "imagePullSecrets": [{"name": "render-only-pull"}]} for key in ["api", "web"]},
    }
    sandbox_values = build / "sandbox.yaml"
    sandbox_values.write_text(yaml.safe_dump(fixture))
    for namespace in ["verify-a", "verify-b"]:
        docs, ids = documents(run("template", "verify", chart, "--namespace", namespace, "-f", migration, "-f", sandbox_values), namespace)
        check_dev_endpoints(docs)
        assert {kind + "/" + name for _, kind, _, name in ids} == {
            "PersistentVolumeClaim/verify-api-uploads", "Deployment/verify-api", "Service/verify-api",
            "Deployment/verify-web", "Service/verify-web", "VirtualService/verify",
        }
        route = next(doc for doc in docs if doc["kind"] == "VirtualService")
        assert route["spec"]["hosts"] == [hosts["sandbox"]]
        assert route["spec"]["gateways"] == ["istio-system/development"]
        api_route, web_route = route["spec"]["http"]
        assert {"uri": {"prefix": "/oan/"}} in api_route["match"]
        assert api_route["route"][0]["destination"] == {"host": "verify-api", "port": {"number": 80}}
        assert web_route["route"][0]["destination"] == {"host": "verify-web", "port": {"number": 80}}
        api = deployment_env(docs, "verify-api")
        assert api["ALLOWED_ORIGINS"] == api["PORTAL_URL"] == "https://" + hosts["sandbox"]
        assert api["DB_HOST"] == "commons-postgresql.commons.svc.cluster.local"
        assert deployment_env(docs, "verify-web")["API_INTERNAL_URL"] == f"http://verify-api.{namespace}.svc.cluster.local:80/oan"
        for name in ["verify-api", "verify-web"]:
            pod = next(doc for doc in docs if doc["kind"] == "Deployment" and doc["metadata"]["name"] == name)["spec"]["template"]["spec"]
            assert pod["automountServiceAccountToken"] is False
            assert pod["securityContext"]["runAsNonRoot"] is True
            assert pod["imagePullSecrets"] == [{"name": "render-only-pull"}]
            assert pod["containers"][0]["image"].startswith("example.invalid/render-only@sha256:")
        api_pod = next(doc for doc in docs if doc["kind"] == "Deployment" and doc["metadata"]["name"] == "verify-api")["spec"]["template"]["spec"]
        assert api_pod["containers"][0]["envFrom"][0] == {"secretRef": {"name": "render-only-config"}}
        assert api_pod["containers"][0]["readinessProbe"]["httpGet"] == {"path": "/oan/health", "port": "http"}
    for setting in ["api.image.repository=", "api.image.digest=sha256:invalid", "web.image.repository=", "secret.name=", "web.enabled=false"]:
        bad = subprocess.run([HELM, "template", "verify", str(chart), "-f", str(sandbox_values), "--set", setting], capture_output=True)
        assert bad.returncode != 0, "oan-sandbox accepts invalid settings: " + setting


def offline_resolution(build):
    mirror = build / "mirror"
    mirror.mkdir()
    urls = set()
    for metadata in CHARTS:
        chart = metadata.parent
        config = read(metadata)
        for dep in config.get("dependencies", []):
            if dep["repository"].startswith("file://"):
                continue
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
            # A chart without dependencies (oan-sandbox) has no lock to compare.
            if read(metadata).get("dependencies"):
                assert read(target / "Chart.lock") == read(metadata.parent / "Chart.lock")
            for ns in ["verify-a", "verify-b"]:
                if metadata.parent.name in BLOCKED_REGISTRIES:
                    verify_refactor_gate(target, ns)
                    verify_refactor_gate(metadata.parent, ns)
                    continue
                original, identities = documents(run("template", "verify", metadata.parent, "--namespace", ns), ns)
                resolved, new_identities = documents(run("template", "verify", target, "--namespace", ns), ns)
                assert identities == new_identities
                assert image_refs(original) == image_refs(resolved)
                assert secret_refs(original) == secret_refs(resolved)


def package(report):
    public = ROOT / "repository"
    public.mkdir(exist_ok=True)
    recorded = ROOT / "releases/artifacts.json"
    prior = json.loads(recorded.read_text()) if recorded.exists() else {}
    added, unreleased = [], []
    with build_directory() as temp:
        for metadata in CHARTS:
            chart = metadata.parent
            info = read(metadata)
            archive_name = f'{info["name"]}-{info["version"]}.tgz'
            archive = public / archive_name
            source_sha = fingerprint(chart)
            if archive.exists():
                assert prior[archive_name]["sha256"] == digest(archive), f"Immutable archive bytes changed: {archive_name}"
                if prior[archive_name]["sourceSha256"] != source_sha:
                    # Changed since its version was published: scripts/release.py
                    # gives it the next version after merge. Verify a scratch package.
                    archive = package_chart(chart, temp)
                    unreleased.append(chart.name)
            else:
                shutil.copy2(package_chart(chart, temp), archive)
                prior[archive_name] = {"sha256": digest(archive), "sourceSha256": source_sha}
                added.append(archive)
            for ns in ["verify-a", "verify-b"]:
                if chart.name in BLOCKED_REGISTRIES:
                    verify_refactor_gate(archive, ns)
                    verify_refactor_gate(chart, ns)
                    continue
                packaged_docs, from_package = documents(run("template", "verify", archive, "--namespace", ns), ns)
                source_docs, from_source = documents(run("template", "verify", chart, "--namespace", ns), ns)
                assert from_package == from_source
                assert image_refs(packaged_docs) == image_refs(source_docs)
                assert secret_refs(packaged_docs) == secret_refs(source_docs)
            with tarfile.open(archive) as tar:
                assert not any(Path(member.name).name in {"values-live.yaml", "values-dev.yaml", "values-new-dev.yaml"} or Path(member.name).name.startswith(("private-values", ".env")) for member in tar.getmembers()), "Private/environment capture in package"
                packaged_info = yaml.safe_load(tar.extractfile(chart.name + "/Chart.yaml").read())
                assert packaged_info["annotations"] == info["annotations"]
                assert packaged_info["sources"] == info["sources"]
                for filename in ["README.md", "app-readme.md"]:
                    assert tar.extractfile(chart.name + "/" + filename).read() == (chart / filename).read_bytes()
    merge_index(public, added)
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
                    if entry["name"] not in EXPECTED:
                        continue
                    if selected.get("annotations", {}).get("oan.org/promotion-ready") == "false":
                        verify_refactor_gate(public / Path(url).name, "http-check")
                    elif (ROOT / "addons/registry-dashboards" / entry["name"] / "Chart.yaml").exists():
                        documents(run("template", "http-check", "coss/" + entry["name"], "--version", entry["version"], "--namespace", "http-check", *ADDON_RENDER_ARGS, env=env), "http-check")
                    else:
                        documents(run("template", "http-check", "coss/" + entry["name"], "--version", entry["version"], "--namespace", "http-check", env=env), "http-check")
    recorded.write_text(json.dumps(prior, indent=2) + "\n")
    (public / "SHA256SUMS").write_text("".join(f"{digest(p)}  {p.name}\n" for p in sorted(public.glob("*.tgz"))), encoding="utf-8")
    report["packages"] = len(list(public.glob("*.tgz")))
    report["currentPackages"] = len(CHARTS)
    report["historicalPackages"] = report["packages"] - len(CHARTS)
    report["unreleasedCharts"] = unreleased
    report["index"] = "Relative URLs, SHA-256, HTTP download, exact Helm version selection and repository-based renders verified against loopback server"


def check_farmer_jenkins_profile():
    pin = json.loads((ROOT / 'environments/dev/farmer-jenkins.json').read_text(encoding='utf-8'))
    assert (pin['environment'], pin['namespace'], pin['release']) == ('dev', 'farmer', 'farmer-registry')
    assert pin['repository'] == 'https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/'
    archive = ROOT / 'repository' / (pin['name'] + '-' + pin['version'] + '.tgz')
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == pin['sha256']
    with tarfile.open(archive) as chart:
        def metadata(path):
            return yaml.safe_load(chart.extractfile(pin['name'] + '/' + path))
        parent = metadata('Chart.yaml')
        child = metadata('charts/openg2p-registry/Chart.yaml')
    assert (parent['name'], parent['version'], parent['appVersion']) == (pin['name'], pin['version'], pin['platformVersion'])
    assert parent['dependencies'] == [{'alias': 'registry', 'name': 'openg2p-registry',
                                      'version': pin['platformVersion'], 'repository': 'https://openg2p.github.io/openg2p-helm'}]
    assert (child['name'], child['version']) == ('openg2p-registry', pin['platformVersion'])


def main():
    check_farmer_jenkins_profile()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", action="store_true")
    parser.add_argument("--online", action="store_true")
    args = parser.parse_args()
    assert {m.parent.name for m in CHARTS} == EXPECTED
    build_root = ROOT / ".build"
    build_root.mkdir(exist_ok=True)
    report = {"helm": run("version", "--short").strip(), "chartVersions": {m.parent.name: read(m)["version"] for m in CHARTS}, "clusterAccess": False, "charts": {}, "upstreamResolution": "not attempted"}
    baselines = json.loads((ROOT / "releases/resource-baselines-current.json").read_text())
    with build_directory() as build:
        offline_resolution(build)
        report["offlineResolution"] = "All chart locks resolved from dependencies bundled with verified source packages"
        for metadata in CHARTS:
            chart = metadata.parent
            info = read(metadata)
            assert SEMVER.fullmatch(info["version"]), f"{chart.name} version is not Semantic Versioning"
            check_oan_metadata(info, chart)
            values = read(chart / "values.yaml")
            if chart.name == "openg2p-commons-services":
                master_data = next(dep for dep in info["dependencies"] if dep["name"] == "openg2p-master-data")
                assert master_data["version"] == "0.0.0-develop.118"
                assert master_data["repository"] == "https://openg2p.github.io/openg2p-helm"
                for component in ("masterDataAPI", "masterDataUi"):
                    assert values["master-data"][component]["image"]["tag"] == "0.0.0-develop.118"
                    assert re.fullmatch(r"sha256:[0-9a-f]{64}", values["master-data"][component]["image"]["digest"])
                # The seed image is upstream's develop.118 with the ETH-OAN pack, by digest.
                seed = values["master-data"]["geoSeed"]["image"]
                assert seed["repository"] == "ghcr.io/asmitonweb/master-data-db-seed"
                assert re.fullmatch(r"0\.0\.0-develop\.118-oan\.\d+@sha256:[0-9a-f]{64}", seed["tag"])
                assert values["master-data"]["geoSeed"]["countryPack"] == "ETH-OAN"
                assert values["master-data"]["geoSeed"]["enabled"] is False
                assert info["annotations"]["oan.org/promotion-ready"] == "true"
            if chart.name in BLOCKED_REGISTRIES:
                assert info["appVersion"] == "1.2.2-rc.557"
                assert info["dependencies"][0]["version"] == info["appVersion"]
                assert info["annotations"]["oan.org/promotion-ready"] == "false"
                for ns in ("verify-a","verify-b"):
                    verify_refactor_gate(chart,ns)
                report["charts"][chart.name] = {"promotionReady":False,
                    "platformVersion":info.get("appVersion", "Commons 2.3.4-rc.247 / Master Data develop.118"),"validation":"dependency resolution and explicit fail-closed render gate verified",
                    "preservation":"NOT VERIFIED; full application/restored-data acceptance required before gate removal"}
                continue
            run("lint", chart, "--strict")
            example_name = {"openg2p-commons-services": "commons-services", "oan-sandbox": "sandbox"}.get(chart.name) or chart.name.removeprefix("openg2p-").removesuffix("-registry")
            example = ROOT / "examples/dev" / (example_name + ".yaml")
            run("lint", chart, "--strict", "-f", example)
            example_docs, _ = documents(run("template", "verify", chart, "--namespace", "verify-a", "-f", example), "verify-a")
            check_dev_endpoints(example_docs)
            baseline, identities = documents(run("template", "verify", chart, "--namespace", "verify-a"), "verify-a")
            upstream = baselines[chart.name]
            assert stable_identities(identities) == stable_identities({tuple(x) for x in upstream["resourceIdentities"]}), "Upstream resource names changed"
            check_dev_endpoints(baseline)
            check_url_contract(chart, baseline)
            check_upgrade_safe_jobs(baseline)
            assert secret_refs(baseline) == {tuple(x) for x in upstream["secretKeyReferences"]}, "Upstream Secret references changed"
            selectors = {doc["kind"] + "/" + doc["metadata"]["name"]: doc["spec"].get("selector") for doc in baseline if doc["kind"] in ["Deployment", "StatefulSet", "Service"]}
            assert selectors == upstream["selectors"], "Upstream selectors changed"
            documents(run("template", "verify", chart, "--namespace", "verify-b"), "verify-b")
            migration = ROOT / "environments/dev/values" / (example_name + ".yaml")
            migrated, _ = documents(run("template", "verify", chart, "--namespace", "verify-a", "-f", migration), "verify-a")
            check_dev_endpoints(migrated)
            check_url_contract(chart, migrated)
            if chart.name in {"openg2p-farmer-registry", "openg2p-cropsown-registry", "openg2p-livestock-registry"}:
                saved = build / "synthetic-saved-values.yaml"
                saved.write_text(yaml.safe_dump({"global": {"keycloakBaseUrl": "https://keycloak.old.openg2p.test", "registryHostname": "registry.old.openg2p.test", "registryDBSecret": "render-only-private-db", "registryDBUserPasswordKey": "password"}, "registry": {"staffUi": {"envVars": {"APP_URL": "https://registry.old.openg2p.test", "IAM_URL": "https://iam.old.openg2p.test", "COOKIE_DOMAIN": ".old.openg2p.test", "MIGRATION_PRESERVES_CUSTOM_SETTING": "render-only"}}}}))
                upgraded, _ = documents(run("template", "verify", chart, "--namespace", "verify-a", "-f", saved, "-f", migration), "verify-a")
                check_dev_endpoints(upgraded)
                check_url_contract(chart, upgraded)
                assert ("render-only-private-db", "password") in secret_refs(upgraded)
                assert deployment_env(upgraded, "verify-staff-portal-ui")["MIGRATION_PRESERVES_CUSTOM_SETTING"] == "render-only"
            components = {"openg2p-commons-services": ["aggregationApi"], "oan-sandbox": []}.get(chart.name, ["dashboardApi", "dashboardUi"])
            # Commons' Aggregation API runs in dev; its Secrets are provisioned in the namespace.
            default_on = {"openg2p-commons-services": {"aggregationApi"}}.get(chart.name, set())
            for component in components:
                assert values[component]["enabled"] is (component in default_on)
                fixture = {component: {"enabled": True, "image": dict(SYNTHETIC_IMAGE), "envFrom": [{"secretRef": {"name": "render-only-config"}}], "imagePullSecrets": [{"name": "render-only-pull"}]}}
                test_values = build / "values.yaml"
                test_values.write_text(yaml.safe_dump(fixture))
                enabled, enabled_ids = documents(run("template", "verify", chart, "--namespace", "verify-a", "-f", test_values), "verify-a")
                check_dev_endpoints(enabled)
                assert identities <= enabled_ids, "Enabling an add-on removed an existing resource"
                assert any(ref.startswith("example.invalid/render-only@sha256:") for ref in image_refs(enabled))
                deployment = next(x for x in enabled if x["kind"] == "Deployment" and x["metadata"]["name"] == "verify-" + {"dashboardApi": "dashboard-api", "dashboardUi": "dashboard-ui", "aggregationApi": "aggregation-api"}[component])
                pod = deployment["spec"]["template"]["spec"]
                assert pod["imagePullSecrets"] == [{"name": "render-only-pull"}]
                assert pod["containers"][0]["envFrom"] == fixture[component]["envFrom"]
                if component == "aggregationApi":
                    assert pod["containers"][0]["ports"][0]["containerPort"] == 8100
                    for probe in ["startupProbe", "readinessProbe", "livenessProbe"]:
                        assert pod["containers"][0][probe]["httpGet"] == {"path": "/ping", "port": "http"}
                    fixture[component]["virtualService"] = {"enabled": True, "host": "aggregation.development.oanstaging.com", "gateway": "istio-system/development"}
                    test_values.write_text(yaml.safe_dump(fixture))
                    routed, routed_ids = documents(run("template", "verify", chart, "--namespace", "verify-a", "-f", test_values), "verify-a")
                    route = next(x for x in routed if x["kind"] == "VirtualService" and x["metadata"]["name"] == "verify-aggregation-api")
                    assert route["spec"]["hosts"] == [fixture[component]["virtualService"]["host"]]
                    assert route["spec"]["gateways"] == ["istio-system/development"]
                    assert route["spec"]["http"][0]["route"][0]["destination"] == {"host": "verify-aggregation-api", "port": {"number": 80}}
                    assert enabled_ids <= routed_ids
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
            if chart.name == "openg2p-commons-services":
                # Runs in dev by default; the checks below cover its rendered contract.
                assert values["consentPartnerPortal"]["enabled"] is True
                portal_values = build / "partner-portal.yaml"
                portal_values.write_text(yaml.safe_dump({"consentPartnerPortal": {
                    "enabled": True, "image": dict(SYNTHETIC_IMAGE),
                    "imagePullSecrets": [{"name": "render-only-pull"}]
                }}))
                for namespace in ["verify-a", "verify-b"]:
                    portal_docs, portal_ids = documents(run("template", "verify", chart, "--namespace", namespace, "-f", portal_values), namespace)
                    check_dev_endpoints(portal_docs)
                    assert stable_identities({(api, kind, namespace, name) for api, kind, _, name in identities}) <= stable_identities(portal_ids)
                    added = [doc for doc in portal_docs if doc["metadata"]["name"].startswith("verify-cm-partner-portal")]
                    assert {doc["kind"] for doc in added} == {"Deployment", "Service", "ConfigMap", "VirtualService"}
                    route = next(doc for doc in added if doc["kind"] == "VirtualService")
                    assert route["spec"]["gateways"] == ["istio-system/development"]
                    api_route, ui_route = route["spec"]["http"]
                    assert api_route["match"] == [{"uri": {"prefix": "/consent/v1/partner-portal/"}}]
                    assert api_route["route"][0]["destination"]["host"] == "verify-cm-api"
                    assert ui_route["route"][0]["destination"]["host"] == "verify-cm-partner-portal"
                    pod = next(doc for doc in added if doc["kind"] == "Deployment")["spec"]["template"]["spec"]
                    assert pod["imagePullSecrets"] == [{"name": "render-only-pull"}]
                    assert pod["automountServiceAccountToken"] is False
                    assert pod["containers"][0]["securityContext"]["readOnlyRootFilesystem"] is True
                    config = json.loads(next(doc for doc in added if doc["kind"] == "ConfigMap")["data"]["config.json"])
                    assert config["apiBaseUrl"] == ""
                    assert config["keycloak"] == {"url": "https://keycloak.development.oanstaging.com", "realm": "partner", "clientId": "consent-partner-portal"}
                for setting in ["consentPartnerPortal.image.repository=", "consentPartnerPortal.image.digest=sha256:invalid", "consentPartnerPortal.keycloak.url=", "openg2p-consent-manager.enabled=false"]:
                    bad = subprocess.run([HELM, "template", "verify", str(chart), "--set", "consentPartnerPortal.enabled=true", "--set", setting], capture_output=True)
                    assert bad.returncode != 0, "Portal accepts invalid prerequisites: " + setting
            if chart.name == "oan-sandbox":
                check_sandbox(chart, values, build, migration)
            report["charts"][chart.name] = {"lint": "strict passed", "resources": len(identities), "namespaces": ["verify-a", "verify-b"], "preservation": "upstream resource identities, selectors and Secret references match baseline", "baselineScope": upstream["scope"], "optionalWorkloads": "enabled/disabled, digest, pull Secret, envFrom and missing-image/invalid-digest rejection passed", "defaultImageReferences": image_refs(baseline)}
            report["charts"][chart.name]["devExample"] = str(example.relative_to(ROOT)) + ": strict lint and render passed"
            report["charts"][chart.name]["devEndpointMigration"] = "canonical verified hosts; no legacy environment hosts in workloads, routes or encoded login-provider configuration"
        if args.online:
            online_cache = build / "online-cache"
            online_cache.mkdir()
            online_config = build / "online-repositories.yaml"
            env = dict(os.environ, HELM_REPOSITORY_CONFIG=str(online_config), HELM_REPOSITORY_CACHE=str(online_cache))
            urls = sorted({dep["repository"] for metadata in CHARTS for dep in read(metadata).get("dependencies", []) if not dep["repository"].startswith("file://")})
            for i, url in enumerate(urls):
                run("repo", "add", f"upstream-{i}", url, env=env)
            for metadata in CHARTS:
                target = build / "online" / metadata.parent.name
                shutil.copytree(metadata.parent, target)
                run("dependency", "build", target, env=env)
                if read(metadata).get("dependencies"):
                    assert read(target / "Chart.lock") == read(metadata.parent / "Chart.lock")
                if metadata.parent.name in BLOCKED_REGISTRIES:
                    verify_refactor_gate(target)
                    verify_refactor_gate(metadata.parent)
                    continue
                actual, actual_ids = documents(run("template", "verify", target, "--namespace", "verify-a"), "verify-a")
                bundled, bundled_ids = documents(run("template", "verify", metadata.parent, "--namespace", "verify-a"), "verify-a")
                assert actual_ids == bundled_ids
                assert image_refs(actual) == image_refs(bundled)
                assert secret_refs(actual) == secret_refs(bundled)
            report["upstreamResolution"] = "passed"
        if args.package:
            package(report)
    (ROOT / "releases/validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Validated {len(CHARTS)-len(BLOCKED_REGISTRIES)} existing charts and {len(BLOCKED_REGISTRIES)} blocked refactor candidates; candidate workload/preservation acceptance is NOT VERIFIED.")
    if args.package:
        print(f"Packaged {len(CHARTS)} charts; archives and relative Helm index verified over local HTTP.")
        if report["unreleasedCharts"]:
            print("Changed since their published version (versioned on merge by scripts/release.py): " + ", ".join(report["unreleasedCharts"]))


if __name__ == "__main__":
    main()
