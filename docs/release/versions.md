# Release bill of materials

What runs on New Dev and on staging, read on 5 November 2026 between 20:45 and 20:55 UTC.

Source for every table in this document unless a table says otherwise:
live reading (`helm list -A`, `helm history`, `kubectl get deploy,statefulset -o jsonpath` for images) on
`new-gen2-development` and `openg2p-gen2-staging`; chart contents from the chart archives in `repository/develop/`
and `repository/staging/` of this repository at commit `7db1f6a`.

Digests are written as the first 12 characters after `sha256:`. A digest appears only where the running
Deployment names one. "tag only" means the Deployment names a tag and no digest, so the exact image bytes are
not shown by the Deployment.

## 1. Registry charts

| Registry | Release name | New Dev chart | New Dev revision | Staging chart | Staging revision | Staging status |
| --- | --- | --- | --- | --- | --- | --- |
| Farmer | `farmer-registry` | `openg2p-farmer-registry-0.0.0-develop.803` | 47 | `openg2p-farmer-registry-1.0.0-rc.813` | 4 | deployed |
| Crop sown | `cropsown-registry` | `openg2p-cropsown-registry-0.0.0-develop.488` | 82 | `openg2p-farmer-registry-1.2.0` (an old chart under the Crop sown release name) | 21 | failed |
| Livestock | `livestock-registry` | `openg2p-livestock-registry-0.0.0-develop.426` | 62 | `openg2p-livestock-registry-1.0.0-rc.432` | 57 | deployed |
| Development Agent | `da-registry` | `openg2p-da-registry-0.0.0-develop.83` | 29 | `openg2p-da-registry-1.0.0-rc.84` | 3 | deployed, but see section 6 |

Source: live reading `helm list -A`. Chart channel versions: `releases/channels-current.yaml`.

Each staging chart is promoted from the New Dev chart of the same source tree. The chart annotation
`oan.org/promoted-from` records it: rc.813 from develop.803, rc.432 from develop.426, rc.84 from develop.83
(chart archives in `repository/staging/`). Staging has no chart for Crop sown yet: the pipeline built
`1.0.0-rc.486` but its installation timed out (see [operations-runbook.md](operations-runbook.md)).

Source commits recorded in the chart annotation `oan.org/source-commit`:

| Registry | New Dev chart source commit | Staging chart source commit |
| --- | --- | --- |
| Farmer | `90b2649a7b10` | `90b2649a7b10` |
| Crop sown | `fbe5a37e41f2` | not published |
| Livestock | `cc5b130f5aea` | `cc5b130f5aea` |
| Development Agent | `9dc1ebfea870` | `9dc1ebfea870` |

## 2. OpenG2P versions the charts pin

| Item | Farmer | Crop sown | Livestock | Development Agent |
| --- | --- | --- | --- | --- |
| `openg2p-registry` chart (dependency alias `registry`, repository https://openg2p.github.io/openg2p-helm) | 1.2.2-rc.625 | 1.2.2-rc.614 | 1.2.2-rc.614 | 1.2.2-rc.614 |

Source: `Chart.yaml` inside the chart archives listed in section 1 (`dependencies` and `appVersion`).

Latest published `registry-platform` versions in OpenG2P versions (`registry-platform/CHANGELOG.md`):

| Version | Date |
| --- | --- |
| 1.2.2-rc.681 | 4 November 2026 (latest) |
| 1.2.2-rc.677 | 4 November 2026 |
| 1.2.2-rc.625 | 29 October 2026 (pinned by Farmer) |
| 1.2.2-rc.614 | 28 October 2026 (pinned by Crop sown, Livestock and Development Agent) |

Drift: all four registries are behind the latest release candidate. Farmer is on a newer one than the other
three. The next platform upgrade must move all four together. Reason to keep them equal: the same
`openg2p-registry` chart renders every registry.

Other latest versions in OpenG2P versions, for comparison with section 4:
`registry-connector` 0.0.0-develop.11 (the registry chart depends on 0.0.0-develop.9),
`farmer-registry` 1.2.1-rc.326, `iam` 1.4.4-rc.142, `master-data-service` 1.1.4-rc.108, `id-generator` 1.1.2,
`awe` 0.0.0-develop.95, `consent-manager` 0.0.0-develop.91, `partner-management` 0.0.0-develop.35.

## 3. Registry images

Registry images live in the Amazon container registry (ECR) account `379220350808`, region `ap-south-1`.
The table shows the path below `379220350808.dkr.ecr.ap-south-1.amazonaws.com/`.

### Farmer

| Component | Image path | New Dev tag | New Dev digest | Staging tag | Staging digest |
| --- | --- | --- | --- | --- | --- |
| Staff user interface | `openg2p/farmer-registry/staff-ui` | `90b2649a7b10` | `6092fc7a640a` | `1.0.0-rc.813` | `6092fc7a640a` |
| Staff API | `openg2p/farmer-registry/staff-api` | `90b2649a7b10` | `cb47eea3ae97` | `1.0.0-rc.813` | `cb47eea3ae97` |
| Partner API | `openg2p/farmer-registry/partner-api` | `90b2649a7b10` | `c9aaecb15edc` | `1.0.0-rc.813` | `c9aaecb15edc` |
| Celery worker and beat producer | `openg2p/farmer-registry/celery` | `90b2649a7b10` | `77c260d130c5` | `1.0.0-rc.813` | `77c260d130c5` |
| Dashboard API | `openg2p/farmer-registry/dashboard-api` | `f584b8e53bc0` | `7148aa301190` | digest only | `7148aa301190` |
| Dashboard user interface | `oan/farmer-registry/dashboard-ui` | `8aa8dd8ab773` | `948811f5b98a` | `8aa8dd8ab773` | `948811f5b98a` |
| Connector API, worker, beat | New Dev `openg2p/registry-connector-api`; staging `openg2p/farmer-registry/registry-connector` | `bc565efd47c1-158e11f710bd` | `3a042f7a2d04` | `90b2649a7b10` | `347e5f45bb07` |
| Connector user interface | New Dev `openg2p/registry-connector-ui`; staging `openg2p/farmer-registry/registry-connector-ui` | `bc565efd47c1-158e11f710bd` | `05a7e2c2e7de` | `90b2649a7b10` | `773fc2f67b43` |

Drift: the Farmer registry images are the same bytes on both environments (same digests), which shows the
promotion keeps the digests. The Farmer connector is different. New Dev runs the connector image built after
the admin-login change (farmer-registry pull request 232, merged 5 November 2026 19:47 UTC). Staging still runs
the connector image built from the older commit `90b2649a7b10` (the merge of pull request 228, which is before
pull request 232). So the staging connector does not have the admin login. Source for the pull requests:
`gh pr view 232` and the chart annotation `oan.org/source-subject`.

### Crop sown

| Component | Image path | New Dev tag | New Dev digest | Staging tag (running) |
| --- | --- | --- | --- | --- |
| Staff user interface | `openg2p/cropsown-registry/staff-ui` | `develop-255` | tag only | `gen2/cropsown-registry/staff-ui:staging-14` (old build; new pods cannot pull it) |
| Staff API | `openg2p/cropsown-registry/staff-api` | `develop-255` | tag only | `gen2/cropsown-registry/staff-api:staging-14` |
| Partner API | `openg2p/cropsown-registry/partner-api` | `develop-255` | tag only | `gen2/cropsown-registry/partner-api:staging-14` |
| Celery | `openg2p/cropsown-registry/celery` | `develop-255` | tag only | `gen2/cropsown-registry/celery:staging-14` |
| Dashboard API | `openg2p/cropsown-registry/dashboard-api` | by digest `397cef051fa9` | `397cef051fa9` | none running |
| Dashboard user interface | `oan/cropsown-registry/dashboard-ui` | `1027e7775505` | tag only | none running |
| Connector API, worker, beat | `openg2p/cropsown-registry/registry-connector` | by digest `532b6d9c19bc` | `532b6d9c19bc` | `gen2/cropsown-registry/connector-service:staging-22` |
| Connector user interface | `openg2p/cropsown-registry/registry-connector-ui` | by digest `675af2073a58` | `675af2073a58` | `gen2/cropsown-registry/connector-ui:staging-22` |

The New Dev tag `develop-255` is the Jenkins build number of the `develop` branch build 255 (Jenkins reading:
`Gen2-Package/cropsown-regsitry/develop`, build 255, success, push event). The pipeline built these images for
staging as `1.0.0-rc.486` with these digests (Jenkins console of `Gen2-Package/cropsown-regsitry/staging`
build 28): staff-api `1464abb0a75e`, partner-api `45174ab70ddd`, celery `9c2b4e5e17d9`, staff-ui `0a3887b60ca8`,
db-seed `9606ad96110f`, sanity-tests `5b18400399c3`, dashboard-api `1cdc73b004c0`, dashboard-ui `b1a283783430`.
Not verified: whether those digests equal the digests New Dev runs, because the New Dev Deployments name tags
without digests.

### Livestock

| Component | Image path | New Dev tag | Staging tag | Staging digest |
| --- | --- | --- | --- | --- |
| Staff user interface | `openg2p/livestock-registry/staff-ui` | `cc5b130f5aea` (tag only) | `1.0.0-rc.432` | `9e1a17531f33` |
| Staff API | `openg2p/livestock-registry/staff-api` | `cc5b130f5aea` (tag only) | `1.0.0-rc.432` | `5c6c14ea7011` |
| Partner API | `openg2p/livestock-registry/partner-api` | `cc5b130f5aea` (tag only) | `1.0.0-rc.432` | `7678c266d04b` |
| Celery | `openg2p/livestock-registry/celery` | `cc5b130f5aea` (tag only) | `1.0.0-rc.432` | `a3378894d49c` |
| Dashboard API | `openg2p/livestock-registry/dashboard-api` | digest `f105a023e2cf` | digest `0e6a34e3413b` | `0e6a34e3413b` |
| Dashboard user interface | `oan/livestock-registry/dashboard-ui` | `829c1d3abd03` | `829c1d3abd03` | tag only |
| Connector API, worker, beat | `openg2p/livestock-registry/registry-connector` on New Dev; `openg2p/livestock-registry/connector-service:live-20260930-0024` on staging | digest `138d7ec30196` | `live-20260930-0024` | tag only |
| Connector user interface | `.../registry-connector-ui` on New Dev; `.../connector-ui:live-20260930-0452` on staging | digest `9b49598c2f02` | `live-20260930-0452` | tag only |

Drift: the Livestock dashboard API has a different digest on New Dev and on staging. The connector images on
staging are from 30 September 2026 and use different image names from New Dev. Staging also runs a second
dashboard user interface, Deployment `livestock-dashboard-ui`, from a Docker Hub image
`docker.io/nahom25/livestock-dashboard-ui:0.2.0` that is not built by the OAN pipeline. Not verified: who owns
that Deployment and whether it serves traffic (a VirtualService `livestock-dashboard-ui` for host
`livestock-dashboard.oanstaging.com` exists).

### Development Agent

| Component | Image path | New Dev tag | Staging |
| --- | --- | --- | --- |
| Staff user interface, staff API, partner API, celery | `openg2p/da-registry/<role>` | `9dc1ebfea870` (tag only) | no Deployment running (section 6 of [environments.md](environments.md)) |
| Seed job | `openg2p/da-registry/db-seed` | pods show `4ad52ab0f375` from an earlier run | pinned `1.0.0-rc.84@sha256:0bf44c81d90d` |

### Id generator and Redis

| Environment | Id generator image | Redis image |
| --- | --- | --- |
| New Dev (Farmer, Crop sown, Livestock) | `registry.gitlab.com/openg2p/platform-services/id-generator/openg2p-id-generator:0.0.0-develop.42` | `docker.io/openg2p/redis:7.2.5-debian-12-r4` |
| New Dev (Development Agent) | `openg2p/openg2p-id-generator:1.1.2` | same |
| Staging (Farmer, Livestock, Development Agent) | `openg2p/openg2p-id-generator:1.1.2` | same |
| Staging (Crop sown) | `registry.gitlab.com/openg2p/platform-services/id-generator/openg2p-id-generator:0.0.0-develop.42` | same |

Drift: three New Dev registries and staging Crop sown pull the id generator from GitLab. Staging
Farmer, Livestock and Development Agent, and New Dev Development Agent, use the published
`openg2p/openg2p-id-generator:1.1.2`. The OpenG2P versions repository lists `id-generator` 1.1.2 as the latest
release. The GitLab path depends on a registry the project no longer controls; moving to 1.1.2 removes that
dependency. Not verified: whether the two images behave the same.

## 4. Commons services

Commons has two Helm releases per environment, both in the namespace `commons`:

| Release | Chart | New Dev revision | Staging revision |
| --- | --- | --- | --- |
| `commons` (base: PostgreSQL, Keycloak, Kafka, Redis, MinIO) | `openg2p-commons-base-2.3.3` | 4 | 6 |
| `commons-services` | `openg2p-commons-services-1.0.0-dev.35` (application version 2.3.4-rc.247) | 36 | 16 |

Source: live reading `helm list -A`; the image lists of both environments were compared line by line.
Result: every image in the namespace `commons` is the same on both environments. The only difference is the
name of the pull-secret refresh job (New Dev `ecr-pull-secret-refresh`, staging `oan-dashboards-ecr-refresh`).

| Service | Deployment or StatefulSet | Image (same on both environments) |
| --- | --- | --- |
| Keycloak | StatefulSet `commons-keycloak` | `docker.io/openg2p/keycloak:24.0.5-debian-12-r1-g2p1` |
| PostgreSQL | StatefulSet `commons-postgresql` | `docker.io/openg2p/postgresql:16.4.0-debian-12-r14` |
| Kafka | StatefulSet `commons-kafka-controller` | `docker.io/openg2p/kafka:3.7.1-debian-12-r4` |
| Redis | StatefulSets `commons-redis-master`, `commons-redis-auth-master` | `docker.io/openg2p/redis:7.2.5-debian-12-r4` |
| MinIO | `commons-minio` | `docker.io/openg2p/minio:2023.12.23-debian-11-r2` |
| Partner Management (API, staff API, staff UI) | `commons-services-pm-*` | `openg2p/partner-management-*:1.0.2` |
| Consent Manager (API, partner API, UI) | `commons-services-cm-*` | `.../openg2p/commons/consent-manager-api:dev-48e64c249056@sha256:cca3273868b8`, `.../consent-manager-ui:dev-48e64c249056@sha256:423f78a0d99b` |
| Consent partner portal | `commons-services-cm-partner-portal` | `.../oan/commons/consent-partner-portal@sha256:26f091206956` |
| Master Data (API, UI) | `commons-services-master-data-api`, `-ui` | `openg2p/master-data-api@sha256:3bc3f9d8db1e`, `openg2p/master-data-ui@sha256:98a0f4fac7a7` |
| Approval Workflow Engine (service, UI) | `commons-services-awe`, `-awe-ui` | `openg2p/openg2p-awe:1.2.2`, `openg2p/openg2p-awe-ui:1.2.2` |
| WebSub hub and consolidator | `commons-services-websub`, `-websub-consolidator` | `docker.io/mosipid/websub-service:1.3.2`, `docker.io/mosipid/consolidator-websub-service:1.3.2` |
| Aggregation | `commons-services-aggregation-api` | `.../oan/commons/aggregation-api@sha256:3bd17245a752` |
| Identity and access (staff portal API, staff UI, agent portal API) | `commons-services-iam-*` | `openg2p/iam-staff-portal-api:1.4.4-rc.125`, `iam-staff-ui:1.4.4-rc.125`, `iam-agent-portal-api:1.4.4-rc.125`; beneficiary API `1.1.0` |
| Staff portal | `commons-services-staff-portal-ui` | `openg2p/openg2p-staff-portal-ui:1.2.0` |
| ODK Central (backend, front end, Enketo, pyxform) | `commons-services-odk-central-*` | `openg2p/odk-central-backend:v2025.2.1`, `ghcr.io/getodk/central-nginx:v2025.2.1`, `ghcr.io/enketo/enketo:7.5.1`, `ghcr.io/getodk/pyxform-http:v3.1.0` |
| Shared dashboard | `oan-dashboards` | `.../openg2p/oan-dashboards:3aecc3171303` |
| eSignet, mock identity, key manager, audit manager | `commons-services-esignet*`, `-mock-identity-system`, `-keymanager`, `-auditmanager` | `mosipid/esignet:1.4.1`, `mosipid/mock-identity-system:0.9.3`, `mosipid/kernel-keymanager-service:1.2.1.0`, `openg2p/openg2p-audit-manager:1.2.0` |

Comparison with OpenG2P versions (latest published, 5 November 2026): `iam` 1.4.4-rc.142 (running rc.125),
`awe` 0.0.0-develop.95 (running 1.2.2), `consent-manager` 0.0.0-develop.91 (running a build tagged
`dev-48e64c249056`), `master-data-service` 1.1.4-rc.108 (running image pinned by digest only).
Not verified: the version number inside the digest-pinned Master Data and Consent images.

## 5. Other releases

| Release | Chart | New Dev | Staging |
| --- | --- | --- | --- |
| Registry dashboards (Farmer, Crop sown, Livestock) | `farmer-registry-dashboard`, `cropsown-registry-dashboard`, `livestock-registry-dashboard` | 0.1.1 (Farmer rev 5, Crop sown rev 15, Livestock rev 6) | Farmer 0.1.2 (rev 1), Livestock 0.1.2 (rev 4), Crop sown not installed |
| `oan-dashboards` | `oan-dashboards-0.1.0` | rev 2 | rev 1 |
| Connectors | `openg2p-connector-0.1.0` (releases `farmer-registry-connector`, `cropsown-connector`, `livestock-connector`) | Farmer rev 13, Crop sown rev 8, Livestock rev 7 | Farmer rev 4, Crop sown rev 2, Livestock rev 2 |
| `farmer-connector-credentials` | 0.1.0 | rev 2 | rev 1 |
| `da` (in namespace `commons`) | `openg2p-da-registry-1.0.0-dev.5` | rev 1, installed 20 October 2026 | not present |
| Logs | Loki 6.24.0, OpenTelemetry collector 0.111.0 (`otel-agent`, `otel-gateway`) | present; Grafana 10.5.15 present | Loki and OpenTelemetry present; no Grafana release |
| Platform | Rancher | 2.15.1 | 2.12.3 |
| Platform | Kubernetes (RKE2) | v1.35.8+rke2r1 | v1.33.6+rke2r1 |

Drift: staging is two Kubernetes minor versions and three Rancher minor versions behind New Dev. Staging has
no Grafana release, so staging logs have no viewer in the cluster (see [operations-runbook.md](operations-runbook.md)).
Not verified: what the New Dev release `da` in the namespace `commons` runs. No Development Agent Deployment
exists in `commons`, and the live registry is the release `da-registry` in the namespace `da-registry`.

## 6. Summary of drift

| # | Difference | Risk |
| --- | --- | --- |
| 1 | Crop sown on staging is failed and runs images from an old pipeline (`gen2/...:staging-14`) | Staging has no current Crop sown |
| 2 | Development Agent on staging: only id generator and Redis run | Staging has no Development Agent |
| 3 | Farmer connector: staging image older than New Dev | Staging connector lacks the admin login |
| 4 | Platform pin: Farmer rc.625, others rc.614, latest rc.681 | Registries diverge in platform behavior |
| 5 | Id generator: GitLab image on New Dev and staging Crop sown | Dependency on a registry outside the project |
| 6 | Livestock dashboard API digest differs; staging runs a Docker Hub dashboard user interface | Unreviewed image on staging |
| 7 | Rancher and Kubernetes versions differ | Staging rehearsals do not prove New Dev behavior for platform changes |
| 8 | Staging has no Crop sown dashboard, yet `oan-dashboards` on staging is configured to read the Crop sown dashboard API | The Crop sown tile on the staging shared dashboard has no source |

Item 8 source: `environments/staging/values/oan-dashboards.yaml` (key `CROPSOWN_REGISTRY_DASHBOARD_API_URL`)
and the Deployment list of the namespace `crop` on staging, which has no dashboard API.
