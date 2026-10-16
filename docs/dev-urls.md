# New-dev URL migration

Use chart version **`1.0.0-dev.2`**. Version `1.0.0-dev.1` is retained unchanged
as a historical artifact and contains the original environment defaults.

The canonical hosts below were confirmed from the new server's Helm endpoint
configuration, Istio routes and Nginx mappings on 16 October 2026. The new-dev
server is `13.201.58.55`. Public endpoint metadata is in
[`environments/dev/endpoints.yaml`](../environments/dev/endpoints.yaml).

| Service | Canonical URL |
| --- | --- |
| Farmer Registry | `https://farmer-registry-development.oanstaging.com` |
| Farmer staff / partner API | `https://staff-farmer-development.oanstaging.com` / `https://partner-farmer-development.oanstaging.com` |
| Crop Registry | `https://crop-registry-development.oanstaging.com` |
| Crop staff / partner API | `https://staff-crop-development.oanstaging.com` / `https://partner-crop-development.oanstaging.com` |
| Livestock Registry | `https://livestock-registry-development.oanstaging.com` |
| Livestock staff / partner API | `https://staff-livestock-development.oanstaging.com` / `https://partner-livestock-development.oanstaging.com` |
| Keycloak | `https://keycloak-development.oanstaging.com` |
| Staff IAM / agent IAM API | `https://staff-iam-development.oanstaging.com` / `https://agent-iam-development.oanstaging.com` |
| Staff portal / IAM UI | `https://staff-portal-development.oanstaging.com` / `https://iam-staff-ui-development.oanstaging.com` |
| Master Data API / UI | `https://master-data-development.oanstaging.com` / `https://master-data-ui-development.oanstaging.com` |
| COSS Consent / partner API | `https://consent-manager-development.oanstaging.com` / `https://consent-manager-partner-development.oanstaging.com` |
| Partner Management / partner API | `https://partner-management-development.oanstaging.com` / `https://partner-management-partner-api-development.oanstaging.com` |
| Approval Workflow / Audit | `https://awe-development.oanstaging.com` / `https://auditmanager-development.oanstaging.com` |
| ODK Central | `https://odk-central-development.oanstaging.com` |
| MinIO API / console | `https://minio-farmer-development.oanstaging.com` / `https://minio-console-development.oanstaging.com` |
| eSignet | `https://esignet-development.oanstaging.com` |

API path prefixes remain controlled by their existing charts. Public staff
cookies use `.oanstaging.com`. Staff logout and issuer URLs use the public
Keycloak host and `/realms/staff`; internal JWKS/service communication can use
`commons-keycloak.commons.svc.cluster.local` without changing the public issuer.

Registry-to-Commons calls explicitly use `*.commons.svc.cluster.local` for
PostgreSQL, IAM, Master Data, Consent, Partner Management, AWE, audit and shared
cache endpoints. AWE callbacks target the existing registry API in its own
release namespace. The Consent callback targets `<release>-cm-api`, rather than
the nonexistent `<release>-api` service. Crop ID Generator uses its namespace's
internal Service because no canonical public route was confirmed.

## Apply to an existing dev release

Changing chart defaults alone does not replace literal URLs saved in an
existing release. Reconcile private values, then apply the corresponding
public migration overlay from [`environments/dev/values/`](../environments/dev/values/).
Those files contain URL/configuration changes, not passwords or live values.

```sh
helm upgrade farmer-registry coss/openg2p-farmer-registry \
  --namespace farmer --version 1.0.0-dev.2 --reuse-values \
  -f /private/reviewed-values.yaml \
  -f environments/dev/values/farmer.yaml --wait --timeout 15m
```

Use the existing release and namespace for every upgrade. For Rancher, merge
the same overlay into the installed app's values while selecting the exact
version. Render and inspect the combined result first. Saved lists such as
Keycloak clients, login providers, extra APIs or custom env arrays may contain
their own literal URLs; preserve their other entries and replace those URLs
privately. Whole-list replacement can discard existing clients or settings.

Superset, Inji Certify, the agent portal UI, notifications, DA, Aggregation and
standalone registry dashboards have no confirmed new-dev public URLs. None were
guessed. Superset and Certify defaults are disabled, matching the inspected dev
release; notifications are disabled pending endpoints. The Superset client
identity is retained with an empty redirect list. Agent portal redirect is
unset. Other unavailable workloads remain disabled. Their future enablement
requires explicit hosts, routes, authentication and the existing component
prerequisites. Review these choices before applying an overlay to a differently
configured environment.

The validator checks current renders, including encoded login-provider data,
for old environment hostnames and unconfirmed public addresses. It preserves
stable resource names, selectors and Secret references. Upstream Keycloak Job
names include a configuration hash, so their suffix changes with new URLs.
No server, DNS, cluster or identity-provider configuration is changed by this PR.
