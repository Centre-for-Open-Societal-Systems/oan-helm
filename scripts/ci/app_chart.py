"""Version, package and publish the develop chart of an application repository. Run by that repository's Jenkins pipeline.

Every application repository (the Frappe services and their user interfaces) packages helm/<chart> with the image of
the build and publishes that archive to repository/develop/ of this repository. The steps are the same everywhere, so
they live here and each repository keeps only its constants in ci/package_chart.py, a short script that loads this
file at a pinned commit of oan-helm and calls main(config, root):

    package_chart.py version           prints the chart version, which is also the image tag of the build:
                                       <version of the app>-develop.<BUILD_NUMBER>, e.g. 0.0.1-develop.57 (develop only)
    package_chart.py package           writes built-chart/<chart>-<version>.tgz
    package_chart.py publish           adds that archive to repository/develop/ of oan-helm
    package_chart.py gateway-package   writes built-gateway-chart/<gateway chart>-<version>.tgz, the routes chart
    package_chart.py gateway-publish   adds that archive to repository/develop/ of oan-helm

The gateway actions exist only for a repository whose config has a "gateway" entry.

config, a dict:

    chart               chart name, also the directory name under helm/
    source_repository   owner/repository of the source, written to the chart annotations
    release_name        Helm release the chart is installed as (annotation)
    release_namespace   namespace of that release (annotation)
    values_overlay      environment values of the release (annotation)
    image_path          values path of the image block that gets the build's repository and tag, e.g. frappe.image
    version             {"file": path in the repository, "pattern": regex with one group "N.N.N"}
                        or {"fixed": "N.N.N"}
    gateway (optional)  {"chart", "source" (directory of the routes chart), "release_name", "values_overlay"}

version needs BRANCH_NAME (develop) and BUILD_NUMBER. package needs IMAGE_REPOSITORY (registry/repository, no tag),
IMAGE_TAG, SOURCE_COMMIT, BRANCH_NAME and COMMIT_SUBJECT. publish needs GH_TOKEN with push access to oan-helm.
DRY_RUN=1 publishes nothing. Standard library only; helm must be on the PATH for package.

Exit codes: 0 done (or already published by an earlier run of this commit), 1 failure, 3 no credential.
"""

import importlib.util
import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OAN_HELM_SLUG = "Centre-for-Open-Societal-Systems/oan-helm"
ALREADY_PUBLISHED = 4


def load_generic():
    """package_chart.py next to this file: set_image and annotate. Loaded by path, because the repository's own
    ci/package_chart.py has the same module name."""
    spec = importlib.util.spec_from_file_location("oan_package_chart", HERE / "package_chart.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(command, cwd):
    return subprocess.run(
        [str(part) for part in command], cwd=str(cwd), check=True, stdout=subprocess.PIPE, universal_newlines=True
    ).stdout


def app_version(config, root):
    version = config["version"]
    if "fixed" in version:
        return version["fixed"]
    match = re.search(version["pattern"], (root / version["file"]).read_text(encoding="utf-8"))
    if not match:
        raise ValueError("no version matching %s in %s" % (version["pattern"], version["file"]))
    return match.group(1)


def chart_version(config, root, env):
    """<version of the app>-develop.<BUILD_NUMBER>, a version publish_chart.py puts in repository/develop/."""
    if env["BRANCH_NAME"] != "develop":
        raise ValueError("only develop packages the chart, not %s" % env["BRANCH_NAME"])
    return "%s-develop.%s" % (app_version(config, root), env["BUILD_NUMBER"])


def annotations(config, env, release_name, overlay):
    return {
        "oan.org/source-repository": config["source_repository"],
        "oan.org/source-commit": env["SOURCE_COMMIT"],
        "oan.org/source-subject": env.get("COMMIT_SUBJECT", "")[:200],
        "oan.org/release-name": release_name,
        "oan.org/release-namespace": config["release_namespace"],
        "oan.org/values-overlay": overlay,
    }


def package_directory(root, work, name, source, version, notes, output, image=None):
    """Copy `source` to work/name, annotate (and pin the image of) its files, and helm package it into output."""
    generic = load_generic()
    chart = work / name
    shutil.copytree(str(source), str(chart))
    if image:
        values = chart / "values.yaml"
        values.write_text(generic.set_image(values.read_text(encoding="utf-8"), *image), encoding="utf-8")
    metadata = chart / "Chart.yaml"
    metadata.write_text(generic.annotate(metadata.read_text(encoding="utf-8"), notes), encoding="utf-8")
    shutil.rmtree(str(output), ignore_errors=True)
    output.mkdir()
    run(["helm", "package", chart, "--version", version, "--destination", output], root)
    print("packaged %s-%s.tgz" % (name, version))


def version_build(config, root, env, work):
    print(chart_version(config, root, env))
    return 0


def package_build(config, root, env, work):
    version = chart_version(config, root, env)
    if env["IMAGE_TAG"] != version:
        raise ValueError("image tag %s is not the chart version %s" % (env["IMAGE_TAG"], version))
    name = config["chart"]
    package_directory(
        root,
        work,
        name,
        root / "helm" / name,
        version,
        annotations(config, env, config["release_name"], config["values_overlay"]),
        root / "built-chart",
        image=(config["image_path"], env["IMAGE_REPOSITORY"], env["IMAGE_TAG"]),
    )
    return 0


def gateway_package_build(config, root, env, work):
    """The routes of the service as a chart of its own, versioned like the app chart and annotated with this commit."""
    gateway = config["gateway"]
    package_directory(
        root,
        work,
        gateway["chart"],
        root / gateway["source"],
        chart_version(config, root, env),
        annotations(config, env, gateway["release_name"], gateway["values_overlay"]),
        root / "built-gateway-chart",
    )
    return 0


def same_commit(a, b):
    """True if one hex SHA prefixes the other and both have at least 7 characters."""
    return bool(a and b and len(a) >= 7 and len(b) >= 7 and (a.startswith(b) or b.startswith(a)))


def published_commit(env, name, chart):
    """oan.org/source-commit of the archive already in repository/develop/ of oan-helm: (commit, None) or (None, error)."""
    request = urllib.request.Request(
        "https://api.github.com/repos/%s/contents/repository/develop/%s" % (OAN_HELM_SLUG, name),
        headers={"Accept": "application/vnd.github.raw", "Authorization": "Bearer " + env.get("GH_TOKEN", "")},
    )
    try:
        with urllib.request.urlopen(request) as response:
            data = response.read()
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
            text = archive.extractfile("%s/Chart.yaml" % chart).read().decode("utf-8")
    except (OSError, KeyError, tarfile.TarError) as error:
        return None, error
    match = re.search(r"oan\.org/source-commit: *\"?([0-9a-f]{7,40})", text)
    return (match.group(1) if match else None), None


def publish_directory(env, output, chart):
    if env.get("DRY_RUN") != "1" and not env.get("GH_TOKEN"):
        print("FAIL: no GitHub credential: the chart was not published.")
        return 3
    archives = sorted(output.glob("*.tgz"))
    if len(archives) != 1:
        raise ValueError("expected the one archive of this build in %s" % output)
    result = subprocess.run([sys.executable, str(HERE / "publish_chart.py"), str(archives[0])], env=env)
    if result.returncode == ALREADY_PUBLISHED:
        # Build numbers can repeat (job recreated), so a taken version is only fine if it holds this commit.
        outcome = published_commit(env, archives[0].name, chart)
        if isinstance(outcome, tuple):
            commit, error = outcome
        elif isinstance(outcome, Exception):
            commit, error = None, outcome
        else:
            commit, error = outcome, None
        if error:
            print("FAIL: could not read the published archive %s: %s" % (archives[0].name, error))
            return 1
        if same_commit(commit, env.get("SOURCE_COMMIT")):
            print("%s was published by an earlier run of this commit." % archives[0].name)
            return 0
        print("FAIL: %s is already published for another commit; the chart was not published." % archives[0].name)
        return 1
    return result.returncode


def publish_build(config, root, env, work):
    return publish_directory(env, root / "built-chart", config["chart"])


def gateway_publish_build(config, root, env, work):
    return publish_directory(env, root / "built-gateway-chart", config["gateway"]["chart"])


def main(config, root, argv=None, env=None):
    argv = sys.argv[1:] if argv is None else argv
    env = dict(os.environ if env is None else env)
    root = Path(root)
    actions = {"version": version_build, "package": package_build, "publish": publish_build}
    if "gateway" in config:
        actions.update({"gateway-package": gateway_package_build, "gateway-publish": gateway_publish_build})
    if len(argv) != 1 or argv[0] not in actions:
        print("usage: package_chart.py " + "|".join(actions))
        return 1
    work = Path(tempfile.mkdtemp(prefix="%s-chart-" % config["chart"]))
    try:
        return actions[argv[0]](config, root, env, work)
    except (KeyError, ValueError, OSError, subprocess.CalledProcessError) as error:
        print("FAIL: %s: %s" % (error.__class__.__name__, error))
        return 1
    finally:
        shutil.rmtree(str(work), ignore_errors=True)
