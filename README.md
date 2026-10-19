# OpenAgriNet (OAN) Helm repository

Start with the [service catalog](docs/service-catalog.md): it maps every included
COSS service to its chart, source/configuration and enablement status. The
[five editable source charts](charts/README.md) are Farmer, Crop Sown, Livestock,
DA and Commons Services, which contains COSS Consent and Aggregation.

For those two components, start at
[where COSS Consent Manager and Aggregation are included](docs/service-catalog.md#where-are-coss-consent-manager-and-aggregation).
Consent reuses the `openg2p-consent-manager` child chart with COSS image overrides;
Aggregation is a local Commons template, disabled pending runtime preparation.
New [Consent candidate images](docs/consent-candidate-build.md) and the
[Aggregation image override](examples/dev/aggregation-image.yaml) are recorded
separately from the immutable chart defaults.

Current chart version is **`1.0.0-dev.3`**, with OAN Rancher display names,
direct COSS GitHub source links and embedded component READMEs in all five charts.
It retains the migrated new-dev URLs and runtime settings from `1.0.0-dev.2`.
Both earlier versions remain available unchanged. Component versions
and image digests are separate; automatic build-number synchronization is deferred.

| Location | Contents |
| --- | --- |
| `charts/` | Five editable source trees; start at [charts/README.md](charts/README.md) |
| `docs/service-catalog.md` | Every included service, its COSS repository, owning chart and status |
| `environments/dev/` | Canonical endpoint inventory and public URL migration overlays, plus APISIX gateway values; see [the APISIX gateway guide](docs/apisix-gateway.md) |
| `examples/dev/` | Public dev configuration checklists; no private live values |
| `releases/` | Release manifest, provenance, deployment comparison and validation evidence |
| `repository/` | Generated Rancher downloads, SHA256SUMS and cumulative Helm index, including historical versions |
| `docs/` | Readable service catalog, URL migration and Rancher guides |
| `scripts/validate.py` | Dependency, render, packaging and repository validation |

## APISIX gateway

The OAN API gateway is Apache APISIX, installed from Apache's upstream chart and configured
through the APISIX Ingress Controller. This repository holds only its values under
`environments/dev/values/` (`apisix.yaml`, `oan-grievance-gateway.yaml`,
`oan-a2c-gateway.yaml`), not charts. Each app's route chart is generated from its OpenAPI
spec and lives in the app repository. The values target the separate grievance cluster, not
the OpenG2P cluster the five charts above deploy to. Start at the
[APISIX gateway guide](docs/apisix-gateway.md): it covers the design, the dev-cluster
install, testing, the traffic cutover and rollback.

Rancher repository URLs served directly by GitHub:

- COSS after merge: `https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/`
- Current fork preview: `https://raw.githubusercontent.com/asmitonweb/oan-helm/feat/coss-rancher-charts/repository/`

GitHub serves the committed `repository/index.yaml` and archives directly;
GitHub Pages is not required. Validation runs on PRs and pushes. Merging the
reviewed files into `main` makes the COSS URL available; this change does not
merge the PR or deploy to Kubernetes.

Use the [Rancher guide](docs/rancher-dev.md) and
[new-dev URL migration guide](docs/dev-urls.md), plus the
[readiness table](docs/readiness.md). Published COSS core/Consent images are
pinned by digest. Optional dashboard APIs also have verified images but remain
opt-in for reporting/identity preparation. Dashboard UIs, DA backend/dashboard
workloads and Aggregation remain disabled pending images or configuration.
Private registry pull credentials and live values stay outside Git.
Unconfirmed public endpoints stay unset. Superset/Certify defaults match their
disabled state in the inspected dev release; notifications await confirmed routes.

Follow the [Consent and Aggregation prerequisites](docs/consent-aggregation-prerequisites.md)
before enabling Aggregation. The pinned Consent build predates the inspected
Aggregation version's subject-consent requirements. The new candidate overlay
provides the required settings and endpoint schema. The exact published API pair
passed [30 local integration checks](docs/consent-aggregation-local-check.md)
against source-owned stand-ins. Authenticated split routing and existing-database
upgrades still require environment verification.

Commons Services was imported from the latest published OpenG2P package at
verification time, `2.3.4-rc.247`, with its published SHA-256 verified. All registry
charts retain their source pins to platform `1.2.2-rc.544`. Commons Base remains a
separate upstream installation, pinned to `2.3.4-rc.245` for new preparations;
the current dev release is `2.3.3` and upgrading it requires separate preparation.
Connectors, the shared OAN dashboard and existing independent dashboards keep
their Helm owners.

```sh
python -m pip install -r requirements.txt
python scripts/validate.py --package
# Also verify locked dependencies against upstream repositories:
python scripts/validate.py --online
```

Requires Helm `3.19.0`; set `HELM` if the executable is not on PATH. Validation
uses no Kubernetes credentials. It resolves locks through a local HTTP mirror of
bundled sources, strictly lints all charts, compares original resource names,
selectors and Secret references, renders two namespaces and optional workloads,
and verifies package rendering plus relative index/archive URLs over HTTP.
Synthetic render fixtures use `example.invalid`; installation examples never do.

Archives are immutable. Packaging rejects changed source bytes for an existing
archive/version. Keep historical archives and index entries; future releases
require a new chart version and manifest. No application-repository CI changes
or cluster deployment are included.
