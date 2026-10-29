# OAN Livestock Registry

OpenAgriNet (OAN) application developed in the Centre for Open Societal Systems
(COSS) repositories. This chart reuses the pinned OpenG2P registry platform.

| Source | GitHub repository |
| --- | --- |
| OAN application | [livestock-registry](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry) |
| OAN Helm sources | [oan-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/openg2p-livestock-registry) |
| OAN dashboard component | [livestock-registry-dashbaord-api](https://github.com/Centre-for-Open-Societal-Systems/livestock-registry-dashbaord-api) |
| OAN dashboard component | [oan_livestock_dashboard](https://github.com/Centre-for-Open-Societal-Systems/oan_livestock_dashboard) |

The Helm chart name retains its `openg2p-` prefix to preserve the existing release
and resource names. It does not identify the application source owner. The
OpenG2P dependency repository contains reused platform templates; application
images and provenance are configured by this OAN chart.

Use chart version **1.0.0-dev.5** and upgrade the current release in its current
namespace. Review private values, image digests and namespace-local Secret
references before applying changes. Optional dashboard components remain at
their explicit enablement settings; DA workloads await verified images/config.

See [included services](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/service-catalog.md),
[readiness](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/readiness.md) and
[Rancher instructions](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/rancher-dev.md).

Dev URLs use `<service>.development.oanstaging.com`. The environment-owned
wildcard DNS/TLS and `istio-system/development` Gateway must be prepared first.
See the service onboarding and enablement guide in `docs/service-onboarding.md`.

## Farmer reference

The Livestock extension resolves the Farmer named on an intake with a signed,
consent-enforced DCI lookup of the Farmer registry, creates the local Farmer
reference through its own change request and AWE approval, and receives later
Farmer updates through Farmer outgestion (Kafka/WebSub) and the Livestock connector
as local UPDATE change requests. It is configured by `COSS_FARMER_*` variables
and read-only files, never by values carrying private material:

- `farmerReference` renders ConfigMap `<release>-farmer-reference` with the
  server-owned `record-contract.json` and the Farmer partner API's
  response-signing `source-public-key.pem` (from `openg2p-farmer-registry`'s
  `dciSigning` ConfigMap `<farmer release>-dci-signing-public`).
- The Livestock lookup key stays in a Secret provisioned in the namespace (on New
  Dev `livestock-farmer-lookup-signing-ed25519`, key `private-key.pem`, registered
  in Partner Management under `Live_stock_partner_internal`); the AWE client
  secret is the chart's own `<release>-staff-portal` Secret.
- `registry.staffApi`, `partnerApi`, `celeryWorker` and `celeryBeat` mount the
  three read-only and carry the variables; the celery worker also needs
  `REGISTRY_CELERY_WORKERS_AWE_ENABLED` and `_AWE_CALLBACK_SECRET_ID` because
  the extension's worker starts the Farmer change-request workflow.

`environments/dev/values/livestock.yaml` is the New Dev wiring. The extension's
deployment guard (`ci/refactor/deployment_guard.py` in the registry repository)
checks the rendered workloads for exactly this shape before every deploy.

## Registry Connector

`registry.registryConnector` is the OpenG2P Registry Connector subchart (API, worker,
beat, optional consumer and UI). It is off in the chart and on in the dev values.

- Image: one image serves API, worker, beat and consumer, built from
  `docker/registry-connector/Dockerfile` in the livestock-registry repository.
  `registry.registryConnector.image.tag` ships unpinned; set it to
  `<12-character commit>@sha256:<digest>` before enabling the connector anywhere.
- Database: `global.connectorDB` is `livestock_connector_livestock`, the database the
  existing Livestock connector uses. The connector's postgres-init creates neither the
  database nor the role when they exist; it only sets the role password to the value in
  the Secret `global.connectorDBSecret` (key `global.connectorDBUserPasswordKey`). If
  that Secret does not exist, it is generated with a random password and the role
  password is reset to it, which logs the old connector out of the database. Confirm
  the role and Secret names on the namespace before the cutover.
- Redis: `global.redisDb` is 3 on the shared commons Redis (0 serves the auth stores).
  Confirm that database is unused by the existing connectors before the cutover.
- Names: the subchart is aliased `registryConnector` and would name resources with the
  alias, which Kubernetes rejects, so `nameOverride: registry-connector` restores the
  chart name. The API Service becomes
  `livestock-registry-registry-connector-api` (the old release's is
  `livestock-connector-api`).
- Access: `connectorAccess.enabled` renders an Istio AuthorizationPolicy per API/UI
  workload. Webhook paths are accepted only from the `connectorAccess.hubNamespace`
  namespace; every other path only through the ingress gateway and only for
  `global.connectorHostname`.

### Cutover from the standalone connector release

1. Pin the image tag and merge; do not deploy while the old release owns the host.
2. Update the connector's WebSub subscription `callback_url` to
   `http://livestock-registry-registry-connector-api.livestock.svc.cluster.local/webhook/by-slug/farmer-reference-v1`
   and trigger a hub sync.
3. Remove the old `livestock-connector` release (it owns the VirtualService for
   `connector-livestock-registry.development.oanstaging.com`), then upgrade
   `livestock-registry` so this chart's VirtualService takes the host.

### WebSub lease renewal

Neither the Registry Connector nor the connector image renews a WebSub subscription, and
the commons hub rejects a second subscribe for a subscriber that is still registered
("Subscriber has already registered with the Hub"). `connectorLeaseRenewal` (off by
default) renders one weekly CronJob per listed connector that renews the lease in two
steps: `hub.mode=unsubscribe` with the connector's callback, topic and webhook secret,
then, after `verifyWaitSeconds`, `POST /connectors/{id}/websub/sync-subscriptions`
(which re-subscribes with the 10-day lease). The webhook secret and the OAuth client
secrets are read from Secrets named in values, never carried in them. The connector is
unsubscribed for about 20 seconds per run; a notice published in that window is lost.
If the unsubscribe is refused nothing changed and the job fails; if the re-subscribe
fails the job retries and then fails, leaving the connector unsubscribed until the next
run or a manual sync. Weekly runs leave a 3-day margin on a 10-day lease. The Secret
holding the `registry-connector` client credentials (`client_secret`) is created in the
commons namespace and must also exist in this release's namespace.
