# Development wildcard URLs

The dev environment uses `<service>.development.oanstaging.com`. New chart
version **`1.0.0-dev.4`** contains the new URL defaults and shared Gateway settings;
older archives retain their historical configuration.

The migration keeps installed chart/image versions intact using URL-only private
values and the compatibility post-renderer. Selecting a new chart is a separate
review: installing new chart defaults must not replace current live application
images or settings accidentally. Current live results are recorded in
`releases/live-domain-migration.json`.

| Service | Canonical URL |
| --- | --- |
| keycloak | `https://keycloak.development.oanstaging.com` |
| iam | `https://staff-iam.development.oanstaging.com` |
| agentIam | `https://agent-iam.development.oanstaging.com` |
| staffPortal | `https://staff-portal.development.oanstaging.com` |
| iamUi | `https://iam-staff-ui.development.oanstaging.com` |
| awe | `https://awe.development.oanstaging.com` |
| masterData | `https://master-data.development.oanstaging.com` |
| masterDataUi | `https://master-data-ui.development.oanstaging.com` |
| consent | `https://consent-manager.development.oanstaging.com` |
| consentPartner | `https://consent-manager-partner.development.oanstaging.com` |
| partnerManagement | `https://partner-management.development.oanstaging.com` |
| partnerManagementApi | `https://partner-management-partner-api.development.oanstaging.com` |
| odk | `https://odk-central.development.oanstaging.com` |
| minio | `https://minio-farmer.development.oanstaging.com` |
| minioConsole | `https://minio-console.development.oanstaging.com` |
| audit | `https://auditmanager.development.oanstaging.com` |
| esignet | `https://esignet.development.oanstaging.com` |
| farmer | `https://farmer-registry.development.oanstaging.com` |
| farmerStaff | `https://staff-farmer.development.oanstaging.com` |
| farmerPartner | `https://partner-farmer.development.oanstaging.com` |
| farmerId | `https://idgenerator-farmer.development.oanstaging.com` |
| cropsown | `https://crop-registry.development.oanstaging.com` |
| cropsownStaff | `https://staff-crop.development.oanstaging.com` |
| cropsownPartner | `https://partner-crop.development.oanstaging.com` |
| livestock | `https://livestock-registry.development.oanstaging.com` |
| livestockStaff | `https://staff-livestock.development.oanstaging.com` |
| livestockPartner | `https://partner-livestock.development.oanstaging.com` |
| livestockId | `https://idgenerator-livestock.development.oanstaging.com` |

Connectors use `connector-farmer-registry.development.oanstaging.com`,
`connector-cropsown-registry.development.oanstaging.com` and
`connector-livestock-registry.development.oanstaging.com`. The shared dashboard is
`oan-dashboard.development.oanstaging.com`; Kafka UI is
`kafka.development.oanstaging.com`. Preserve their existing access restrictions.

The environment has one wildcard DNS record and certificate, Nginx forwards to
Istio, and public VirtualServices use `istio-system/development`. Rancher and
Jenkins retain their existing management URLs. Exact DNS records override the
wildcard and must be checked when troubleshooting unexpected destinations.

## Login and application settings

The staff issuer is `https://keycloak.development.oanstaging.com/realms/staff`.
Application cookies use `.development.oanstaging.com`. Exact client redirects,
web origins, logout URLs, IAM login-provider records and application links must
be migrated together. Users must sign in again; old tokens may carry the former
issuer. Internal Service/JWKS/database addresses retain their existing namespaces.

The URL overlays under `environments/dev/values/` are public configuration only.
Saved private lists, clients and custom environment values require reconciliation;
replacing an entire list can discard existing settings. The legacy compatibility
renderer migrates literal URLs and encoded configuration, retains private/test
route gateways, and can suppress initialization Jobs for this URL-only operation.
Use `--no-hooks` and `--post-renderer-args --skip-initialization-jobs` only for the
reviewed URL migration, not as a general substitute for required initialization.

## Cutover and recovery

Both URL schemes remain available during completion of the migration. The
`*-development.oanstaging.com` records and original TLS certificates are restored.
HTML GET/HEAD browser navigation gets a temporary 307 redirect to the matching
canonical hostname, preserving path and query. API/JSON requests and POSTs are
proxied through temporary environment-owned aliases without changing method,
body or original Host. The MinIO object API always proxies, including browser
requests, to preserve signed download URLs. Keycloak continues to advertise the
new issuer.

The compatibility configuration is in `environments/dev/legacy/`; refresh its
aliases when canonical service routing changes. Retain old DNS/TLS and renew the
legacy certificates until the user explicitly confirms completion. Do not remove
compatibility on a timer. Other servers and Rancher/Jenkins management URLs remain
outside this change. Private backups retain the exact pre-cutover records and
identity/release settings for recovery.

The migration does not enable Aggregation, DA or unavailable components. Reserved
future hostnames are not evidence of running services. Use the
[service onboarding and enablement guide](service-onboarding.md) for new services.
