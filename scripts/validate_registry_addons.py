"""Validate preserved independent dashboard release charts without Kubernetes."""
import argparse
import json
import shutil
import tarfile

from validate import (ROOT, ADDON_RENDER_ARGS, SEMVER, build_directory, digest, documents,
                      fingerprint, image_refs, merge_index, package_chart, read, run, secret_refs)

CHARTS = sorted((ROOT / "addons/registry-dashboards").glob("*/Chart.yaml"))

def selectors(docs):
    return {(doc["kind"],doc["metadata"]["name"]):doc["spec"].get("selector") for doc in docs
            if doc["kind"] in {"Deployment","StatefulSet","Service"}}

def main(package=False):
    assert {path.parent.name for path in CHARTS} == {f"{name}-registry-dashboard" for name in ("farmer","cropsown","livestock")}
    report = {"clusterAccess":False,"liveOwnershipVerified":False,"charts":{}}
    artifacts_path = ROOT / "releases/artifacts.json"
    artifacts = json.loads(artifacts_path.read_text(encoding="utf-8"))
    added, unreleased = [], []
    with build_directory() as build:
        for metadata in CHARTS:
            chart = metadata.parent
            info = read(metadata)
            assert info["name"] == chart.name and SEMVER.fullmatch(info["version"])
            assert info["annotations"]["oan.org/chart-owner"] == "oan-helm"
            defaults = read(chart / "values.yaml")
            assert defaults["access"]["role"] == "Dashboard Viewer"
            assert defaults["dashboardApi"]["auth"]["role"] == "charts:read"
            assert defaults["dashboardApi"]["auth"]["enabled"] is True
            assert not defaults["iamSetup"]["grantUsers"]
            run("lint",chart,"--strict",*ADDON_RENDER_ARGS)
            source_docs, identities = documents(run("template","verify",chart,"--namespace","verify-a",*ADDON_RENDER_ARGS),"verify-a")
            documents(run("template","verify",chart,"--namespace","verify-b",*ADDON_RENDER_ARGS),"verify-b")
            if package:
                filename = f"{chart.name}-{info['version']}.tgz"
                destination = ROOT / "repository" / filename
                source_sha = fingerprint(chart)
                if destination.exists():
                    assert artifacts[filename]["sha256"] == digest(destination)
                    if artifacts[filename]["sourceSha256"] != source_sha:
                        # Versioned on merge by scripts/release.py; verify a scratch package.
                        destination = package_chart(chart,build)
                        unreleased.append(chart.name)
                else:
                    shutil.copy2(package_chart(chart,build),destination)
                    artifacts[filename] = {"sha256":digest(destination),"sourceSha256":source_sha}
                    added.append(destination)
                packaged_docs, packaged_ids = documents(run("template","verify",destination,"--namespace","verify-a",*ADDON_RENDER_ARGS),"verify-a")
                assert identities == packaged_ids
                assert selectors(source_docs) == selectors(packaged_docs)
                assert image_refs(source_docs) == image_refs(packaged_docs)
                assert secret_refs(source_docs) == secret_refs(packaged_docs)
                with tarfile.open(destination) as archive:
                    assert not any(part in member.name.lower() for member in archive.getmembers()
                                   for part in ("values-live", "private-values", "/.env"))
            report["charts"][chart.name] = {"version":info["version"],"strictLint":"PASS",
                "namespaces":["verify-a","verify-b"],"sourcePackageIdentitiesSelectorsImagesSecrets":"PASS" if package else "NOT RUN",
                "authentication":"Dashboard Viewer for humans; charts:read for service accounts; existing Secret references",
                "existingReleaseNames":"unchanged; no ownership adoption or runtime change"}
        if package:
            public = ROOT / "repository"
            merge_index(public,added)
            artifacts_path.write_text(json.dumps(artifacts,indent=2)+"\n",encoding="utf-8",newline="\n")
            (public / "SHA256SUMS").write_text("".join(f"{digest(path)}  {path.name}\n" for path in sorted(public.glob("*.tgz"))),encoding="utf-8",newline="\n")
    (ROOT / "releases/registry-addon-validation.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"registry_dashboard_charts":len(CHARTS),"source_package_verification":package,"unreleased":unreleased,"cluster_access":False}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package",action="store_true")
    main(parser.parse_args().package)
