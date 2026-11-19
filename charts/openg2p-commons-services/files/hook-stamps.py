"""Record the input hashes of the setup hooks that ran in this revision (templates/_hook_stamps.tpl).

Runs as the last post-install/post-upgrade hook, so only after every earlier hook succeeded. Merges STAMPS
({hook: sha256}) into the data of the ConfigMap CONFIGMAP in NAMESPACE; the stamps of hooks that did not run are
left as they are. The service account may only get and patch that one ConfigMap.
"""
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

API = "https://kubernetes.default.svc"
ACCOUNT = "/var/run/secrets/kubernetes.io/serviceaccount"


def patch(api, namespace, name, stamps, token, context):
    body = json.dumps({"data": stamps}).encode()
    request = urllib.request.Request(
        f"{api}/api/v1/namespaces/{namespace}/configmaps/{name}", data=body, method="PATCH",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/merge-patch+json"})
    with urllib.request.urlopen(request, context=context, timeout=30) as response:
        return json.load(response).get("data") or {}


def main():
    stamps = json.loads(os.environ["STAMPS"])
    if not isinstance(stamps, dict) or not all(isinstance(v, str) and len(v) == 64 for v in stamps.values()):
        sys.exit("STAMPS must be {hook: sha256}")
    namespace, name = os.environ["NAMESPACE"], os.environ["CONFIGMAP"]
    api = os.environ.get("KUBERNETES_API", API)
    if "KUBERNETES_TOKEN" in os.environ:  # render and fixture tests
        token, context = os.environ["KUBERNETES_TOKEN"], None
    else:
        with open(f"{ACCOUNT}/token", encoding="utf-8") as handle:
            token = handle.read().strip()
        context = ssl.create_default_context(cafile=f"{ACCOUNT}/ca.crt")
    try:
        data = patch(api, namespace, name, stamps, token, context)
    except urllib.error.HTTPError as error:
        sys.exit(f"Could not record the hook stamps: HTTP {error.code} from the Kubernetes API")
    missing = sorted(hook for hook, digest in stamps.items() if data.get(hook) != digest)
    if missing:
        sys.exit("The hook stamps were not recorded for: " + ", ".join(missing))
    print("Recorded the stamps of: " + (", ".join(sorted(stamps)) or "no hook"))


if __name__ == "__main__":
    main()
