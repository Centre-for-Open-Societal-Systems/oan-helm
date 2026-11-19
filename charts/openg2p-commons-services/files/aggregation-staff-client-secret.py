"""Give the Aggregation API the staff client's secret that Keycloak holds after this release.

keycloak-init declares the aggregation-layer-staff client. For a client that already exists it sets
the secret to the one in the Secret it renders (a new random value the first time), and
client-secrets-sync copies Keycloak's secret into that Secret. Both are plain Jobs of this release,
so their order is not fixed. The Aggregation API reads the secret from its runtime Secret (envFrom),
which nothing else updates.

This hook runs after both Jobs of this release have finished, reads the client's secret from Keycloak
(the value the client really has now) and writes it into the runtime Secret's key and into the
client's own Secret, so the next release renders the same value and Keycloak keeps it. When the
runtime Secret changed, the Aggregation API Deployment is restarted. Secret values are never printed.

Input (environment): KEYCLOAK_URL, KEYCLOAK_USER, KEYCLOAK_PASSWORD (master realm, admin-cli); REALM,
CLIENT_ID; NAMESPACE; RELEASE, REVISION, SYNC_JOB (the Jobs to wait for); RUNTIME_SECRET, RUNTIME_KEY;
DEPLOYMENT. The pod's service account token is used for the Kubernetes API.
"""
import base64
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SA = "/var/run/secrets/kubernetes.io/serviceaccount"


def call(method, url, token=None, form=None, body=None, content_type="application/json", context=None):
    headers = {}
    data = None
    if form is not None:
        data = urllib.parse.urlencode(form).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    elif body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = content_type
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=30, context=context) as response:
        raw = response.read()
    return json.loads(raw) if raw else None


class Kubernetes:
    def __init__(self, base, token, namespace, context=None):
        self.base, self.token, self.namespace, self.context = base.rstrip("/"), token, namespace, context

    def _url(self, path):
        return f"{self.base}{path}"

    def get(self, path):
        return call("GET", self._url(path), self.token, context=self.context)

    def patch(self, path, body):
        return call("PATCH", self._url(path), self.token, body=body,
                    content_type="application/strategic-merge-patch+json", context=self.context)

    def secret(self, name):
        try:
            return self.get(f"/api/v1/namespaces/{self.namespace}/secrets/{name}")
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            raise

    def jobs(self):
        return self.get(f"/apis/batch/v1/namespaces/{self.namespace}/jobs").get("items", [])


def release_jobs(jobs, release, revision, sync_job=None):
    """This release's keycloak-init and client-secrets-sync Jobs, by the names their charts give them.

    client-secrets-sync is named by the hash of its inputs (SYNC_JOB), so the Job of an earlier revision is this
    revision's when nothing it reads changed; without SYNC_JOB the older name <release>-client-secrets-sync-<revision>."""
    names = {job["metadata"]["name"]: job for job in jobs}
    init = [job for name, job in names.items() if name.startswith(f"{release}-keycloak-init-{revision}-")]
    sync_name = sync_job or f"{release}-client-secrets-sync-{revision}"
    sync = [job for name, job in names.items() if name == sync_name]
    return init, sync


def finished(job):
    status = job.get("status") or {}
    if status.get("succeeded"):
        return "succeeded"
    for condition in status.get("conditions") or []:
        if condition.get("type") == "Failed" and condition.get("status") == "True":
            return "failed"
    return None


def wait_for_jobs(kube, release, revision, attempts, delay, sync_job=None):
    # Helm creates both Jobs before it runs post hooks. A missing sync Job has finished (an older chart deleted it
    # 600 s after it finished); keycloak-init is kept for a day and must be found.
    for attempt in range(1, attempts + 1):
        init, sync = release_jobs(kube.jobs(), release, revision, sync_job)
        states = [finished(job) for job in init + sync]
        if init and all(states):
            if "failed" in states:
                raise SystemExit("keycloak-init or client-secrets-sync failed in this release; the runtime Secret is left as it is")
            return
        print(f"Waiting for keycloak-init and client-secrets-sync of revision {revision} (attempt {attempt}/{attempts})", flush=True)
        time.sleep(delay)
    raise SystemExit(f"keycloak-init and client-secrets-sync of revision {revision} did not finish")


def admin_token(base, user, password, attempts, delay):
    url = f"{base}/realms/master/protocol/openid-connect/token"
    form = {"grant_type": "password", "client_id": "admin-cli", "username": user, "password": password}
    for attempt in range(1, attempts + 1):
        try:
            return call("POST", url, form=form)["access_token"]
        except (urllib.error.URLError, KeyError, ValueError) as error:
            print(f"Keycloak token not ready (attempt {attempt}/{attempts}): {error}", flush=True)
            time.sleep(delay)
    raise SystemExit("Could not get a Keycloak admin token")


def client_secret(base, token, realm, client_id):
    admin = f"{base}/admin/realms/{urllib.parse.quote(realm, safe='')}"
    found = call("GET", f"{admin}/clients?{urllib.parse.urlencode({'clientId': client_id})}", token)
    if not found or found[0].get("publicClient"):
        raise SystemExit(f"{realm}/{client_id}: no confidential client; keycloak-init should have created it")
    value = (call("GET", f"{admin}/clients/{found[0]['id']}/client-secret", token) or {}).get("value")
    if not value:
        raise SystemExit(f"{realm}/{client_id}: Keycloak returned no client secret")
    return value


def decoded(secret, key):
    raw = ((secret or {}).get("data") or {}).get(key)
    return base64.b64decode(raw).decode() if raw else None


def main():
    namespace, release, revision = os.environ["NAMESPACE"], os.environ["RELEASE"], os.environ["REVISION"]
    realm, client_id = os.environ["REALM"], os.environ["CLIENT_ID"]
    runtime, key, deployment = os.environ["RUNTIME_SECRET"], os.environ["RUNTIME_KEY"], os.environ["DEPLOYMENT"]
    attempts = int(os.environ.get("ATTEMPTS", "60"))
    delay = float(os.environ.get("DELAY_SECONDS", "10"))
    api = os.environ.get("KUBERNETES_API", "https://kubernetes.default.svc")
    if "KUBERNETES_TOKEN" in os.environ:
        kube = Kubernetes(api, os.environ["KUBERNETES_TOKEN"], namespace)
    else:
        with open(f"{SA}/token", encoding="utf-8") as handle:
            kube = Kubernetes(api, handle.read().strip(), namespace, ssl.create_default_context(cafile=f"{SA}/ca.crt"))

    wait_for_jobs(kube, release, revision, attempts, delay, os.environ.get("SYNC_JOB") or None)
    base = os.environ["KEYCLOAK_URL"].rstrip("/")
    token = admin_token(base, os.environ["KEYCLOAK_USER"], os.environ["KEYCLOAK_PASSWORD"], attempts, delay)
    value = client_secret(base, token, realm, client_id)
    encoded = base64.b64encode(value.encode()).decode()
    result = {}

    # The client's own Secret: what keycloak-init renders (and so sets in Keycloak) next time.
    if decoded(kube.secret(client_id), "client_secret") != value:
        kube.patch(f"/api/v1/namespaces/{namespace}/secrets/{client_id}", {"data": {"client_secret": encoded}})
        result[client_id] = "updated"
    else:
        result[client_id] = "unchanged"

    current = kube.secret(runtime)
    if current is None:
        raise SystemExit(f"Secret {runtime} is missing; the Aggregation API needs it (aggregation-api.runtimeSecret)")
    if decoded(current, key) != value:
        kube.patch(f"/api/v1/namespaces/{namespace}/secrets/{runtime}", {"data": {key: encoded}})
        stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        kube.patch(f"/apis/apps/v1/namespaces/{namespace}/deployments/{deployment}",
                   {"spec": {"template": {"metadata": {"annotations": {"aggregation-staff-client-secret/restartedAt": stamp}}}}})
        result[runtime] = "updated; deployment restarted"
    else:
        result[runtime] = "unchanged"
    print(json.dumps({"client": f"{realm}/{client_id}", "secrets": result}), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
