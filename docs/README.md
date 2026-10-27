# Documentation index

Start with the [repository README](../README.md) for how charts are changed, released
and deployed, and [CONTRIBUTING.md](../CONTRIBUTING.md) for the pull-request rules.

## Releasing and operating charts

| Guide | Use it for |
| --- | --- |
| [versioning.md](versioning.md) | Version rules and the automatic release workflow |
| [publication.md](publication.md) | How GitHub serves `repository/` to Rancher and Helm |
| [rancher-dev.md](rancher-dev.md) | Installing and upgrading releases in Rancher, ownership and rollback rules |
| [rancher-consent-aggregation-status.md](rancher-consent-aggregation-status.md) | Installed Commons Services release in dev and its upgrade controls |
| [readiness.md](readiness.md) | Per-component readiness and image provenance |
| [service-catalog.md](service-catalog.md) | Every COSS service, its chart, values key and source |
| [service-onboarding.md](service-onboarding.md) | Adding or enabling a service in dev without new DNS, Nginx or certificates |
| [dev-urls.md](dev-urls.md) | Development wildcard URLs and the legacy-URL migration |
| [request-flow.md](request-flow.md) | Request path, load balancing, logging and Rancher in one picture |
| [existing-architecture-diagram.md](existing-architecture-diagram.md) | Production-like AWS deployment architecture |
| [logging.md](logging.md) | OpenTelemetry, Loki and Grafana |

## Registries

| Guide | Use it for |
| --- | --- |
| [registry-refactor.md](registry-refactor.md) | Refactor candidates, their promotion gate and central chart ownership |
| [refactor-location-and-ownership.md](refactor-location-and-ownership.md) | Master Data location contract and the ETH-OAN seed image |
| [farmer-jenkins-dev.md](farmer-jenkins-dev.md) | Farmer's pinned Jenkins dev deployment |
| [farmer-preserving-adoption.md](farmer-preserving-adoption.md) | Guarded Farmer adoption in New Dev |
| [farmer-reporting.md](farmer-reporting.md) | Farmer reporting views and their owner |
| [registry-esignet-onboarding.md](registry-esignet-onboarding.md) | eSignet provider and callback per registry |
| [registry-staff-access.md](registry-staff-access.md) | Dedicated registry staff accounts |
| [staff-portal-tiles.md](staff-portal-tiles.md) | Staff portal application tiles |
| [automated-staff-test.md](automated-staff-test.md) | Automated staff regression against New Dev |

## Commons Services: Consent, Aggregation, Partner Management, WebSub

| Guide | Use it for |
| --- | --- |
| [consent-aggregation-prerequisites.md](consent-aggregation-prerequisites.md) | What must exist before enabling Aggregation |
| [consent-partner-portal.md](consent-partner-portal.md) | The optional Consent Partner Portal workload |
| [consent-candidate-build.md](consent-candidate-build.md) | Published COSS Consent candidate images |
| [consent-aggregation-local-check.md](consent-aggregation-local-check.md) | Local check of a Consent and Aggregation image pair |
| [ecr-pull-access.md](ecr-pull-access.md) | Letting New Dev pull the Aggregation image |
| [partner-session-cookie-guard.md](partner-session-cookie-guard.md) | Partner Management session cookie guard in dev |
| [websub-new-dev.md](websub-new-dev.md) | Kafka-backed WebSub in New Dev |

## Grievance, A2C and the API gateway

| Guide | Use it for |
| --- | --- |
| [grievance-service.md](grievance-service.md) | Grievance service on Kubernetes |
| [a2c.md](a2c.md) | A2C on Kubernetes |
| [apisix-gateway.md](apisix-gateway.md) | APISIX gateway design, install, cutover and rollback |
| [external-db-and-nfs.md](external-db-and-nfs.md) | MariaDB outside the cluster and the sites volume on NFS |

## Environment notes

- Commons Services was imported from OpenG2P `openg2p-commons-services` `2.3.4-rc.247`.
  Commons Base is a separate upstream release, pinned to `2.3.4-rc.245` for new
  installations; dev runs `2.3.3`, and upgrading it needs separate preparation.
  Connectors, the shared OAN dashboard and the independent dashboards keep their own
  Helm owners.
- Optional workloads (dashboard UIs, DA backend and dashboard, Aggregation, Sandbox)
  default to disabled until their images and runtime configuration exist. Private
  pull credentials and live values stay outside Git.
- OTP remains unavailable until SMS delivery exists; do not weaken OTP policies to
  work around it.
- Old application URLs stay compatible until the URL migration is completed; see
  [dev-urls.md](dev-urls.md) and `releases/live-domain-migration.json`.

## Records

[PR-CONSOLIDATION-20261027.md](PR-CONSOLIDATION-20261027.md) records how the October 2026
proposals were consolidated into `1.0.0-dev.16`. Release-train manifests up to
`1.0.0-dev.16` are in `../releases/<version>.yaml`; later releases are in
[CHANGELOG.md](../CHANGELOG.md).
