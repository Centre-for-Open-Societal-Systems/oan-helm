# OAN editable chart sources

**Commons COSS components:** [Consent image overrides](openg2p-commons-services/values.yaml)
use the retained `openg2p-consent-manager` dependency; [Aggregation's Deployment/Service](openg2p-commons-services/templates/aggregation-api.yaml)
is a local template controlled by `aggregationApi.enabled` (default `false`).
See [the inclusion details](../docs/service-catalog.md#where-are-coss-consent-manager-and-aggregation).

| Chart | Source metadata | Runtime configuration | Local workload templates |
| --- | --- | --- | --- |
| Farmer | [Chart.yaml](openg2p-farmer-registry/Chart.yaml) | [values.yaml](openg2p-farmer-registry/values.yaml) | [templates/](openg2p-farmer-registry/templates/) |
| Crop Sown | [Chart.yaml](openg2p-cropsown-registry/Chart.yaml) | [values.yaml](openg2p-cropsown-registry/values.yaml) | [templates/](openg2p-cropsown-registry/templates/) |
| Livestock | [Chart.yaml](openg2p-livestock-registry/Chart.yaml) | [values.yaml](openg2p-livestock-registry/values.yaml) | [templates/](openg2p-livestock-registry/templates/) |
| DA | [Chart.yaml](openg2p-da-registry/Chart.yaml) | [values.yaml](openg2p-da-registry/values.yaml) | [templates/](openg2p-da-registry/templates/) |
| Commons Services, including COSS Consent/Aggregation | [Chart.yaml](openg2p-commons-services/Chart.yaml) | [values.yaml](openg2p-commons-services/values.yaml) | [Aggregation](openg2p-commons-services/templates/aggregation-api.yaml) and [other templates](openg2p-commons-services/templates/) |
| OAN Sandbox (developer portal; no OpenG2P dependency) | [Chart.yaml](oan-sandbox/Chart.yaml) | [values.yaml](oan-sandbox/values.yaml) | [API](oan-sandbox/templates/api.yaml), [web](oan-sandbox/templates/web.yaml), [route](oan-sandbox/templates/virtualservice.yaml) |

[The service catalog](../docs/service-catalog.md) maps every included COSS
repository and shared service to its chart, values key, source and enablement.
Pinned dependencies under each chart's `charts/` directory contain reused
upstream templates. Rancher downloads the generated archives under `repository/`.

Every chart embeds an OAN README with direct COSS GitHub links. Version `1.0.0-dev.3`
adds OAN Rancher display names while retaining existing Helm names for upgrades.
