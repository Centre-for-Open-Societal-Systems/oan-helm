# Staging URLs and environment

Staging uses the base domain `qa.oanstaging.com`. Each service host is the New Dev host
(`<service>.development.oanstaging.com`) with `.qa` in place of `.development`. Staging's cookies are scoped to
`.qa.oanstaging.com`, so they never reach New Dev; the previous scope `.oanstaging.com` contained
`.development.oanstaging.com` and sent staging tokens to New Dev's IAM. The values are in
`environments/staging/values/` (`farmer.yaml`, `commons-services.yaml`); the Gateway, proxy and
host list are in `environments/staging/ingress/` and `environments/staging/endpoints.yaml`.
Anything marked `# staging: confirm` is not yet decided (see [Open points](#open-points)).

## Hosts

| Service | Canonical URL |
| --- | --- |
| keycloak | `https://keycloak.qa.oanstaging.com` |
| iam | `https://staff-iam.qa.oanstaging.com` |
| agentIam | `https://agent-iam.qa.oanstaging.com` |
| staffPortal | `https://staff-portal.qa.oanstaging.com` |
| iamUi | `https://iam-staff-ui.qa.oanstaging.com` |
| awe | `https://awe.qa.oanstaging.com` |
| masterData | `https://master-data.qa.oanstaging.com` |
| masterDataUi | `https://master-data-ui.qa.oanstaging.com` |
| consent | `https://consent-manager.qa.oanstaging.com` |
| consentPartner | `https://consent-manager-partner.qa.oanstaging.com` |
| consentPartnerPortal | `https://consent-partner-portal.qa.oanstaging.com` |
| aggregation | `https://aggregation.qa.oanstaging.com` |
| partnerManagement | `https://partner-management.qa.oanstaging.com` |
| partnerManagementApi | `https://partner-management-partner-api.qa.oanstaging.com` |
| odk | `https://odk-central.qa.oanstaging.com` |
| minio | `https://minio-farmer.qa.oanstaging.com` |
| minioConsole | `https://minio-console.qa.oanstaging.com` |
| audit | `https://auditmanager.qa.oanstaging.com` |
| esignet | `https://esignet.qa.oanstaging.com` |
| farmer | `https://farmer-registry.qa.oanstaging.com` |
| farmerStaff | `https://staff-farmer.qa.oanstaging.com` |
| farmerPartner | `https://partner-farmer.qa.oanstaging.com` |
| farmerId | `https://idgenerator-farmer.qa.oanstaging.com` |
| farmerConnector | `https://connector-farmer-registry.qa.oanstaging.com` |

Hosts that already exist on staging today (`farmer-registry`, `keycloak`, `odk-central`, the Crop and
Livestock registries) keep their names. `odk-central.oanstaging.com` pointed at the retired
ODK VM; it moves to the Commons ODK Central when the fresh install switches the public hosts.

## What runs on staging

- Commons (`openg2p-commons-services`, namespace `commons`): master data with the ETH-OAN pack,
  partner management, consent manager and partner portal, aggregation API, WebSub hub, keymanager, AWE,
  IAM, audit manager, eSignet mock, and ODK Central. ODK Central authenticates through Keycloak realm
  `staff`, client `openg2p-odk`, redirect `https://odk-central.qa.oanstaging.com/*`. The Keycloak clients
  `registry-connector` and `registry-connector-ui` get the staging connector hosts as redirect URIs.
- Farmer registry (`openg2p-farmer-registry`, release `farmer-registry`, namespace `farmer`), installed
  fresh beside the legacy `far` release. Sample data and images are off; the db-seed image supplies
  configuration and the ETH-OAN pack only.

The Keycloak client redirect URIs are applied when a client is first created (`keycloak-init` skips a
client that exists). On a rebuilt Commons that is correct; on a Keycloak that already has clients,
change redirect URIs in Keycloak.

## Cutover and rollback

The farmer values use the final public hosts (`farmer-registry.qa.oanstaging.com`,
`connector-farmer-registry.qa.oanstaging.com`). The legacy `far/internal` gateway serves them today, so the
fresh `farmer` install is applied only in the runbook's cutover step: a cluster admin exports the `far`
VirtualServices for those two hosts (`kubectl get vs -n far -o yaml`) as the rollback artefact, deletes
them, then installs `farmer`. Rollback is re-applying the export.

The Commons hosts are taken over by the Option C rebuild by design: keycloak, staff-iam, staff-portal,
partner-management, iam-staff-ui, master-data-ui, consent-manager, and odk-central (from the retired VM).

## Out of scope here

Hosts in `endpoints.yaml` and the Keycloak redirects but not in the table above are promoted later:
crop-registry, livestock-registry, da-registry, the idgenerator-, partner- and staff- hosts for crop, da
and livestock, and the cropsown and livestock connector hosts.

## Chart prerequisite

Aggregation API, consent partner portal and the connector Keycloak clients take their hosts from
`global.baseDomain` in the chart defaults, so the staging Commons overlay needs the chart release that
derives them (PR "Derive chart default hosts from global.baseDomain"). Installing an older Commons chart
with this overlay would leave those hosts on `development.oanstaging.com`.

## Secrets the install needs (names only)

In namespace `commons`: `commons-websub-encryption` (key `encryption-key`), `aggregation-api-runtime`,
`aggregation-api-signing-rsa-20261023` (key `password`, file `aggregation.p12`), `aggregation-api-catalog`
ConfigMap, `ecr-pull-secret`. In namespace `farmer`: `ecr-pull-secret`, `farmer-registry-dci-signing`,
the registrant-auth key Secret, `commons-postgresql` copied from Commons. Create them outside Git as
described in `docs/service-onboarding.md` and `docs/consent-aggregation-prerequisites.md`.

## db-seed environment

The farmer db-seed Job comes from the upstream platform chart (`openg2p-registry` 1.2.2-rc.614), which
this repository does not modify. Its template renders a fixed list of env vars from `dbSeed.*` and
`global.*` and never renders `dbSeed.envVars`, so a value such as `REGISTRY_FARMER_REFERENCE_SOURCE_ID` or
`APPROVER_RESOLVER_SECRET` set under `registry.dbSeed.envVars` is silently ignored. There is no other
values key that reaches the Job's container env (`dbSeed.resources` is the only free-form field and it
only renders under `resources:`).

What staging needs, if the seed image reads extra env (the Farmer values set none today, so nothing is
lost until one is added):

1. Keep upstream untouched and add the env at render time with a Helm post-renderer that patches the
   hook Job `farmer-registry-db-seed`, container `db-seed`, appending `env` entries. Deploys run by
   Jenkins with `helm` can use `--post-renderer`; a Rancher UI upgrade cannot.
2. Or ship a chart-owned copy of the Job in `charts/openg2p-farmer-registry/templates/` (about 170 lines,
   same name and hook annotations) rendering `registry.dbSeed.envVars`, and set
   `registry.dbSeed.enabled: false` for the upstream one. It works from Rancher too but must be diffed
   against upstream on every platform version bump, which is why it is not included here.
3. Or ask OpenG2P to render `dbSeed.envVars` upstream (not done: the platform is not modified).

Verify any option with `helm template` and check `env:` on the `farmer-registry-db-seed` Job, then run
the seed metadata checks (`90_checks.sql`, `check_native_metadata.py`) against the fresh database.

## Open points

- Gateway: all public VirtualServices use `istio-system/staging`, defined in `environments/staging/ingress/gateway.yaml` (hosts `*.qa.oanstaging.com`).
- Master Data geography: `master-data.geoSeed.load.geo: true` is for a fresh Commons only; set it false for any upgrade of an existing one.
  (`master-data.geoSeed.load.geo: true`); New Dev keeps it off to protect a migrated catalogue.
- eSignet mock for Fayda verification is kept as on New Dev; confirm that is wanted on staging.
- Server address in `endpoints.yaml` is a placeholder to confirm. TLS: `ingress/nginx.conf` is installed and its certificate names every host in `ingress/certificate-names.txt`; add a new staging host there and re-issue.
