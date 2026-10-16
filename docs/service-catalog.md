# Included services and their Helm owners

Start with the editable sources in [`charts/`](../charts/). This repository has
five charts. Each registry owns its domain services; Commons Services owns the
shared applications. `repository/*.tgz` are the packaged downloads used by Rancher.
They are generated from these sources, not replacements for the source trees.

| Chart source | What it installs | Existing dev release / namespace |
| --- | --- | --- |
| [Farmer](../charts/openg2p-farmer-registry/) | Farmer APIs/UI, workers, registry seed/test jobs, reporting, configurable dashboard API/UI | `farmer-registry` / `farmer` |
| [Crop Sown](../charts/openg2p-cropsown-registry/) | Crop APIs/UI, workers, seed/test jobs, reporting, configurable dashboard API/UI | `cropsown-registry` / `crop` |
| [Livestock](../charts/openg2p-livestock-registry/) | Livestock APIs/UI, workers, seed/test jobs, reporting, configurable dashboard API/UI | `livestock-registry` / `livestock` |
| [DA](../charts/openg2p-da-registry/) | DA APIs/UI, workers and initialization, plus configurable dashboard API/UI | Namespace unconfirmed; components disabled pending images/configuration |
| [Commons Services](../charts/openg2p-commons-services/) | Shared application services, including COSS Consent and configurable Aggregation | `commons-services` / `commons` |

## COSS repository-to-service map

| COSS repository | Included services | Source/configuration in this repository | Status |
| --- | --- | --- | --- |
| `farmer-registry` | Staff API, partner API, staff UI, Celery worker/beat, DB seed, sanity suite | [Farmer values](../charts/openg2p-farmer-registry/values.yaml), `registry.*`; platform templates from the pinned dependency | Verified COSS images, individually pinned digests |
| `cropsown-regsitry` | Same services for Crop Sown | [Crop values](../charts/openg2p-cropsown-registry/values.yaml), `registry.*` | Verified COSS images, individually pinned digests |
| `livestock-registry` | Same services for Livestock | [Livestock values](../charts/openg2p-livestock-registry/values.yaml), `registry.*` | Verified COSS images, individually pinned digests |
| `da-registry` | DA registry domain services | [DA values](../charts/openg2p-da-registry/values.yaml), `registry.*` | Source included; unavailable backend images keep workloads/initialization disabled |
| `farmer-registry-dashboard-api` | Farmer chart-data API | [API template](../charts/openg2p-farmer-registry/templates/dashboard-api.yaml), `dashboardApi.*` | Verified image; configurable; dev example enabled after reporting/identity prerequisites |
| `cropsown-registry-dashboard-api` | Crop chart-data API | [API template](../charts/openg2p-cropsown-registry/templates/dashboard-api.yaml), `dashboardApi.*` | Verified image; configurable; dev example enabled after reporting/identity prerequisites |
| `livestock-registry-dashbaord-api` | Livestock chart-data API (upstream repository spelling retained) | [API template](../charts/openg2p-livestock-registry/templates/dashboard-api.yaml), `dashboardApi.*` | Verified image; disabled pending reporting preparation |
| `oan_farmerregistry_dashboard` | Farmer dashboard UI | [UI template](../charts/openg2p-farmer-registry/templates/dashboard-ui.yaml), `dashboardUi.*` | Configurable workload included; matching published image unavailable; disabled |
| `oan_cropsown_dashboard` | Crop dashboard UI | [UI template](../charts/openg2p-cropsown-registry/templates/dashboard-ui.yaml), `dashboardUi.*` | Configurable workload included; current published image unavailable; disabled; legacy database-based UI is not substituted |
| `oan_livestock_dashboard` | Livestock dashboard UI | [UI template](../charts/openg2p-livestock-registry/templates/dashboard-ui.yaml), `dashboardUi.*` | Configurable workload included; matching published image unavailable; disabled |
| `consent-management` | Consent staff API, partner API, UI, expiry CronJob, seed/sanity and initialization | [Commons values](../charts/openg2p-commons-services/values.yaml), `openg2p-consent-manager.*`; bundled `openg2p-consent-manager:1.0.2` templates | COSS `develop-5361069` API/UI/sanity images verified and pinned to separate digests; beneficiary API remains disabled |
| `oan-aggregation-api` | Aggregation API Deployment and ClusterIP Service | [Aggregation template](../charts/openg2p-commons-services/templates/aggregation-api.yaml), `aggregationApi.*` in Commons values | Port 8100, env/Secret/config/key mounts included; disabled pending image, DB, catalog, bindings and route |
| No DA dashboard repository identified | Optional DA API/UI workload definitions | [DA templates](../charts/openg2p-da-registry/templates/), `dashboardApi.*`, `dashboardUi.*` | Explicit placeholders for future verified components; disabled; no source/image equivalence claimed |

Application source code stays in those repositories. These charts configure
their published containers. Chart source commits and actual component image
versions are separate records in [`provenance.json`](../releases/provenance.json)
and [`components.json`](../releases/components.json).

## Other resources inside each registry chart

The locked `openg2p-registry:1.2.2-rc.544` dependency supplies common templates for
staff/partner APIs, staff UI, Celery worker/beat, DB seed and sanity Jobs, IAM
registration, PostgreSQL initialization, Keycloak initialization, ID Generator
and the release-local Redis cache. Beneficiary services remain at their explicit
enablement settings. It does not install Commons Base infrastructure.

Farmer additionally owns [analytics/reporting Jobs](../charts/openg2p-farmer-registry/templates/analytics-jobs.yaml),
the reporting refresh CronJob, Maps content, dashboard-import configuration and
optional public staff UI. Crop and Livestock own their reporting-view Job and
refresh CronJob under their `templates/` directories. Existing names, selectors
and Secret references are validated; initialization Job names include upstream
configuration hashes and change when their URLs change.

## Every Commons Services dependency

These are application dependencies declared in [Chart.yaml](../charts/openg2p-commons-services/Chart.yaml),
not a whole-cluster installation. Their original pins and source notices remain
in the bundled archives under `charts/openg2p-commons-services/charts/`.

| Dependency / values key | Included services | New-dev defaults |
| --- | --- | --- |
| `master-data` | Master Data API/UI, geography seed, DB/Keycloak initialization and IAM registration | Enabled; canonical API/UI routes |
| `artifactory` | Shared artifact service | Enabled; internal service settings preserved |
| `keymanager` | Cryptographic key management | Enabled; internal service settings preserved |
| `superset` | Superset web/worker/init and integration | Disabled, matching inspected dev configuration; public URL unconfirmed |
| `esignet` | eSignet authentication components | Enabled; verified development route |
| `mock-identity-system` | eSignet mock identity integration | Enabled; existing shared eSignet route preserved |
| `odk-central` | ODK Central frontend/backend, Enketo and form conversion | Enabled; canonical `odk-central-development.oanstaging.com` |
| `openg2p-iam-service` | Staff IAM API, agent IAM API, staff IAM UI, login provider and initialization configuration | Enabled; confirmed API/UI routes; agent portal redirect unset pending a confirmed URL |
| `openg2p-inji-certify` | Credential issuing and initialization | Disabled, matching inspected dev configuration; public URL unconfirmed |
| `openg2p-audit-manager` | Shared audit API | Enabled; canonical development route |
| `openg2p-staff-portal-ui` | Shared staff portal UI | Enabled; canonical portal/IAM URLs and cookie domain |
| `openg2p-awe` | Approval API/UI, resolver/identity and DB setup | Enabled; canonical public route, internal service communication |
| `partner-management` | Partner staff API, partner API, staff UI, DB/identity setup | Enabled; canonical public routes and logout URL |
| `openg2p-consent-manager` | COSS Consent services listed above | Enabled with verified COSS image digests; existing service names/owners |
| `keycloak-init` | Shared OIDC clients, roles and client Secret configuration | Enabled; confirmed redirect URLs; Superset client retained with an empty redirect list until configured |

To inspect the dependency source stored in an archive:

```sh
helm show values charts/openg2p-commons-services/charts/openg2p-consent-manager-1.0.2.tgz
tar -tzf charts/openg2p-commons-services/charts/openg2p-consent-manager-1.0.2.tgz
```

Commons Base remains upstream and separate. Connectors, the existing shared
`oan-dashboards` release and unrelated COSS applications are outside these five
charts. Existing independent Helm owners are retained. See the
[readiness table](readiness.md), [URL migration](dev-urls.md) and
[Rancher guide](rancher-dev.md) for manual use.
