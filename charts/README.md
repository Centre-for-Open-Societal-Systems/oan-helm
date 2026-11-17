# OAN editable chart sources

**Commons OAN components:** [Consent image overrides](openg2p-commons-services/values.yaml)
use the retained `openg2p-consent-manager` dependency; Aggregation is the `oan-aggregation-api` subchart (alias
`aggregation-api`, bundled in [charts/](openg2p-commons-services/charts/)), controlled by `aggregation-api.enabled` (default `true`).
See [the inclusion details](../docs/service-catalog.md#where-are-oan-consent-manager-and-aggregation).

| Chart | Source metadata | Runtime configuration | Local workload templates |
| --- | --- | --- | --- |
| Farmer | [Chart.yaml](openg2p-farmer-registry/Chart.yaml) | [values.yaml](openg2p-farmer-registry/values.yaml) | [templates/](openg2p-farmer-registry/templates/) |
| Crop Sown | [Chart.yaml](openg2p-cropsown-registry/Chart.yaml) | [values.yaml](openg2p-cropsown-registry/values.yaml) | [templates/](openg2p-cropsown-registry/templates/) |
| Livestock | [Chart.yaml](openg2p-livestock-registry/Chart.yaml) | [values.yaml](openg2p-livestock-registry/values.yaml) | [templates/](openg2p-livestock-registry/templates/) |
| DA | [Chart.yaml](openg2p-da-registry/Chart.yaml) | [values.yaml](openg2p-da-registry/values.yaml) | [templates/](openg2p-da-registry/templates/) |
| Commons Services, including OAN Consent/Aggregation | [Chart.yaml](openg2p-commons-services/Chart.yaml) | [values.yaml](openg2p-commons-services/values.yaml) | [templates/](openg2p-commons-services/templates/); Aggregation is a bundled subchart |
| OAN Sandbox (developer portal; no OpenG2P dependency) | [Chart.yaml](oan-sandbox/Chart.yaml) | [values.yaml](oan-sandbox/values.yaml) | [API](oan-sandbox/templates/api.yaml), [web](oan-sandbox/templates/web.yaml), [route](oan-sandbox/templates/virtualservice.yaml) |
| OAN A2C | [Chart.yaml](oan-a2c/Chart.yaml) | [values.yaml](oan-a2c/values.yaml) | None; all from the `frappe` dependency (`oan-service-helm`) |
| OAN Grievance Service | [Chart.yaml](oan-grievance-service/Chart.yaml) | [values.yaml](oan-grievance-service/values.yaml) | None; all from the `frappe` dependency (`oan-service-helm`) |
| OAN APISIX Gateway | [Chart.yaml](oan-apisix-gateway/Chart.yaml) | [values.yaml](oan-apisix-gateway/values.yaml) | None; all from the vendored `apisix` and `redis` dependencies |
| OAN Logging | [Chart.yaml](oan-logging/Chart.yaml) | [values.yaml](oan-logging/values.yaml) | None; all from the vendored `loki`, `opentelemetry-collector` and `grafana` dependencies |
| OAN Cluster Access (CI deploy identity; [guide](../docs/cluster-access.md)) | [Chart.yaml](oan-cluster-access/Chart.yaml) | [values.yaml](oan-cluster-access/values.yaml) | [ServiceAccount](oan-cluster-access/templates/serviceaccount.yaml), [RBAC](oan-cluster-access/templates/rbac.yaml) |
| OAN Leads API ([README](oan-leads-api/README.md)) | [Chart.yaml](oan-leads-api/Chart.yaml) | [values.yaml](oan-leads-api/values.yaml) | [API](oan-leads-api/templates/api.yaml), [Redis](oan-leads-api/templates/redis.yaml), [external DB](oan-leads-api/templates/external-db.yaml), [route](oan-leads-api/templates/virtualservice.yaml) |

[The service catalog](../docs/service-catalog.md) maps every included OAN
repository and shared service to its chart, values key, source and enablement.
Pinned dependencies under each chart's `charts/` directory contain reused
upstream templates. Rancher downloads the generated archives under `repository/`.

Every chart embeds an OAN README with direct OAN GitHub links. Version `1.0.0-dev.3`
adds OAN Rancher display names while retaining existing Helm names for upgrades.
