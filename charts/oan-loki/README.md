# OAN Loki

Log store for OpenAgriNet (OAN) central application logs. Wraps
[`grafana-community/loki`](https://github.com/grafana-community/helm-charts) **21.0.0**
([Grafana Loki](https://github.com/grafana/loki) 3.7.9) in monolithic mode, following
<https://grafana.com/docs/loki/latest/setup/install/helm/>.

| File | Use |
|---|---|
| `values.yaml` | Default: 1 pod, chunks on a 50Gi PVC, 14-day retention, no auth, caches/canary/test/exporter off, images pinned by digest |
| `values-s3.yaml` | Overlay: S3 buckets in ap-south-1, 3 replicas, `replication_factor: 3` |
| `templates/grafana-datasource.yaml` | Loki datasource ConfigMap for the Grafana sidecar (`grafana_datasource: "1"`) |

The upstream chart moved to the Grafana Community repository in March 2026, and 21.x no
longer ships the MinIO subchart, so the earlier `grafana/loki` 7.5.0 + bundled MinIO
setup cannot be carried forward. Use the filesystem default or S3.

## Install

From the published repository (the release workflow packages it after merge):

```sh
helm upgrade --install loki <oan-helm repo>/oan-loki -n observability --create-namespace --wait
```

From a checkout:

```sh
helm upgrade --install loki charts/oan-loki -n observability --create-namespace --wait
# or S3 + 3 replicas (set the bucket names first)
helm upgrade --install loki charts/oan-loki -n observability \
  -f charts/oan-loki/values-s3.yaml --wait
```

`values-s3.yaml` needs S3 access for the pods: an IRSA role on the service account
(`loki.serviceAccount.annotations`) or a Secret referenced through
`loki.singleBinary.extraEnvFrom` with `-config.expand-env=true`. No credentials belong in
this chart.

## Endpoints

In cluster: `http://loki-gateway.<namespace>.svc.cluster.local`

- OTLP logs: `/otlp/v1/logs` (OpenTelemetry Collector `otlphttp` exporter endpoint:
  `http://loki-gateway.observability.svc.cluster.local/otlp`)
- Push API: `/loki/api/v1/push`
- Grafana datasource: created automatically when Grafana runs with
  `sidecar.datasources.enabled=true`; disable with `grafanaDatasource.enabled=false`.

## Check

```sh
kubectl -n observability get pods -l app.kubernetes.io/instance=loki
kubectl -n observability port-forward svc/loki-gateway 3100:80
curl -s localhost:3100/ready
curl -s localhost:3100/loki/api/v1/labels
```

## Upgrading the Loki dependency

Change `dependencies[0].version` in `Chart.yaml`, run `helm dependency update charts/oan-loki`,
commit `Chart.lock` and the new archive, and update the image digests in `values.yaml` to
the new `appVersion`. Simple scalable mode is deprecated upstream (removal before Loki 4.0);
for production scale switch `loki.deploymentMode` to `Distributed` with object storage.
