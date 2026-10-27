# Logs: OpenTelemetry, Loki and Grafana

Container stdout is collected on each node, redacted, stored in Loki and read in Grafana
(Explore). This is the pipeline OpenG2P describes in
[View System Logs in Grafana (Loki)](https://docs.openg2p.org/operations/deployment/deployment-guide/view-system-logs-in-grafana-loki):
an OpenTelemetry agent on each node, a gateway, Loki with its own object store, Grafana.
Sentry is not part of it.

Rendered with `helm template` only. Nothing here has been installed. The redaction rules
are ours and untested.

```
Pod stdout -> node log file -> OTel agent (DaemonSet): read, label, redact
  -> OTel gateway (Deployment): batch -> Loki (single binary) -> MinIO bucket
Grafana (Loki data source) -> Explore
```

## 1. Files

| File | Chart | Release | Namespace |
|---|---|---|---|
| [loki.yaml](../environments/dev/values/loki.yaml) | `grafana/loki` 7.5.0 | `loki` | `observability` |
| [otel-gateway.yaml](../environments/dev/values/otel-gateway.yaml) | `open-telemetry/opentelemetry-collector` 0.177.0 | `otel-gateway` | `observability` |
| [otel-agent.yaml](../environments/dev/values/otel-agent.yaml) | same chart | `otel-agent` | `observability` (one per cluster) |
| [grafana.yaml](../environments/dev/values/grafana.yaml) | `grafana/grafana` 10.5.15 | `grafana` | `observability` |

Repositories:

```sh
helm repo add grafana https://grafana.github.io/helm-charts
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm repo update
```

## 2. Storage

Loki keeps chunks in an S3-compatible bucket in every environment, so the values do not
change between a lab and production. `loki.yaml` turns on the MinIO sub-chart of the Loki
chart. Only the endpoint and credentials differ if production uses another object store:
set `minio.enabled=false` and `loki.storage.s3.endpoint`, `accessKeyId`,
`secretAccessKey`.

- The sub-chart's own notes call it a test setup. Its image is a community fork
  (`pgsty/silo`) because the upstream MinIO images are no longer maintained. Decide with
  ASMIT which object store production uses.
- The chart puts the S3 credentials into the Loki ConfigMap. They are not in Git: pass them
  with `--set-string` (below). Treat them as visible to anyone who can read the namespace.
- Retention is 14 days (`limits_config.retention_period: 336h`).
- Sizes (5 Gi Loki volume, 10 Gi MinIO volume) are guesses. Measure before relying on them.

## 3. Install

```sh
kubectl create namespace observability
kubectl -n observability create secret generic grafana-admin \
  --from-literal=admin-user=admin --from-literal=admin-password='<password>'

helm upgrade --install loki grafana/loki --version 7.5.0 -n observability \
  -f environments/dev/values/loki.yaml \
  --set-string minio.rootPassword='<root password>' \
  --set-string 'minio.users[0].accessKey=logs-user' \
  --set-string 'minio.users[0].secretKey=<logs password>' --wait

helm upgrade --install otel-gateway open-telemetry/opentelemetry-collector --version 0.177.0 \
  -n observability -f environments/dev/values/otel-gateway.yaml --wait
helm upgrade --install otel-agent open-telemetry/opentelemetry-collector --version 0.177.0 \
  -n observability -f environments/dev/values/otel-agent.yaml --wait
helm upgrade --install grafana grafana/grafana --version 10.5.15 -n observability \
  -f environments/dev/values/grafana.yaml --wait
```

The chart uses `rootUser`/`rootPassword` for Loki's own S3 access, so the root password
matters most. Both passwords must be set.

Another cluster (an app cluster) installs only `otel-agent`. Point it at the gateway
address of the log cluster:

```sh
--set 'config.exporters.otlp_grpc.endpoint=<gateway address>:4317'
```

Use a network the clusters share, and note that the agent talks to the gateway without
TLS (`tls.insecure: true`). That is acceptable on a private network, not across the
internet.

## 4. See the logs

```sh
kubectl -n observability port-forward svc/grafana 3000:80
```

Open http://localhost:3000, Explore, data source Loki. Examples (the label names are what
the agent adds; confirm them in the label browser):

```
{k8s_namespace_name="develop"} |= "error"
{k8s_namespace_name="apisix"}
```

A shared setup needs an APISIX route and a login for Grafana. Not done.

## 5. Redaction

The `transform/redact` rules in `otel-agent.yaml` replace email addresses, phone-number
shapes and `password`/`token`/`bearer`/`authorization` values in the log line before it
leaves the node. OpenG2P does not publish its rules. Test these on realistic lines
(grievance text can contain names and IDs the rules do not catch). Names and national
IDs need rules we have not written.

## 6. Not covered

- Frappe files under `sites/<site>/logs` that are not on stdout.
- JSON logging in the apps (it would allow `| json | field=value` filters).
- Alerts, dashboards, metrics and traces.
- Loki and Grafana sizes, and Loki with a shared (non-test) object store.
- Applying a `NetworkPolicy` to limit who can reach Loki.
