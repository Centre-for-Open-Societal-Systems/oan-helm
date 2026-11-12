"""Roll a Deployment when a ConfigMap it reads has changed.

For subchart Deployments whose templates take no pod annotations, so podAnnotations cannot carry a checksum. Per
Deployment in DEPLOYMENTS (JSON list): read the ConfigMaps its pod template references (volumes, projected volumes,
envFrom, env valueFrom), hash their data, and compare with the pod template annotation oan.org/configmap-checksum.
Only a different hash patches the annotation, which rolls the pods; an unchanged ConfigMap changes nothing. A
missing Deployment or ConfigMap is reported and skipped (component disabled); any other API error fails the Job.
"""
import hashlib
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

ANNOTATION = "oan.org/configmap-checksum"
# In the cluster these are the defaults; the tests point them at a fixture API.
API = os.environ.get("KUBERNETES_API", "https://kubernetes.default.svc")
SA = os.environ.get("SERVICEACCOUNT_DIR", "/var/run/secrets/kubernetes.io/serviceaccount")
session = {}


def call(method, path, body=None, content_type="application/json"):
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(API + path, data=data, method=method, headers={
        "Authorization": f"Bearer {session['token']}", "Accept": "application/json", "Content-Type": content_type})
    try:
        with urllib.request.urlopen(request, context=session["tls"], timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise SystemExit(f"{method} {path}: HTTP {error.code} {error.read()[:300]!r}")


def configmap_names(pod_spec):
    names = set()
    for volume in pod_spec.get("volumes") or []:
        if "configMap" in volume:
            names.add(volume["configMap"]["name"])
        for source in (volume.get("projected") or {}).get("sources") or []:
            if "configMap" in source:
                names.add(source["configMap"]["name"])
    for container in (pod_spec.get("containers") or []) + (pod_spec.get("initContainers") or []):
        for item in container.get("envFrom") or []:
            if "configMapRef" in item:
                names.add(item["configMapRef"]["name"])
        for item in container.get("env") or []:
            ref = (item.get("valueFrom") or {}).get("configMapKeyRef")
            if ref:
                names.add(ref["name"])
    return sorted(names)


def main():
    with open(f"{SA}/token", encoding="utf-8") as token:
        session["token"] = token.read().strip()
    session["tls"] = ssl.create_default_context(cafile=f"{SA}/ca.crt") if API.startswith("https:") else None
    namespace = os.environ["NAMESPACE"]
    apps = f"/apis/apps/v1/namespaces/{namespace}/deployments"
    for name in json.loads(os.environ["DEPLOYMENTS"]):
        deployment = call("GET", f"{apps}/{name}")
        if deployment is None:
            print(f"{name}: no such Deployment, skipped")
            continue
        template = deployment["spec"]["template"]
        digest = hashlib.sha256()
        for cm_name in configmap_names(template["spec"]):
            configmap = call("GET", f"/api/v1/namespaces/{namespace}/configmaps/{cm_name}")
            if configmap is None:
                print(f"{name}: ConfigMap {cm_name} not found, left out of the hash")
                continue
            content = {"data": configmap.get("data") or {}, "binaryData": configmap.get("binaryData") or {}}
            digest.update(cm_name.encode() + b"\0" + json.dumps(content, sort_keys=True).encode() + b"\0")
        checksum = digest.hexdigest()
        current = (template["metadata"].get("annotations") or {}).get(ANNOTATION)
        if current == checksum:
            print(f"{name}: ConfigMaps unchanged, not rolled")
            continue
        call("PATCH", f"{apps}/{name}", {"spec": {"template": {"metadata": {"annotations": {ANNOTATION: checksum}}}}},
             "application/strategic-merge-patch+json")
        print(f"{name}: ConfigMaps changed ({(current or 'none')[:12]} -> {checksum[:12]}), rolling the pods")
    return 0


if __name__ == "__main__":
    sys.exit(main())
