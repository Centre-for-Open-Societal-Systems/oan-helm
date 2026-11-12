# OAN Sandbox

OpenAgriNet (OAN) developer sandbox, developed in the OAN
repositories: a public site with the API catalogue, a participant
portal (sign-up, environment access, try-it console, API history, support) and an
admin console (participants, products and end-points, CMS, masters, queries).

| Source | GitHub repository |
| --- | --- |
| OAN application | [sandbox-platform](https://github.com/Centre-for-Open-Societal-Systems/sandbox-platform) |
| OAN Helm sources | [oan-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/oan-sandbox) |

Chart version **1.0.0-dev.16**. It has no OpenG2P dependency and owns no existing
release, so installing it changes no other chart's resources.

## What it installs

| Workload | Values key | Image | Default |
| --- | --- | --- | --- |
| API (FastAPI, port 8000, health `/oan/health`); uploads PVC | `api` | `docker/sandbox-api/Dockerfile` in sandbox-platform | Disabled until a verified image is set |
| Web (Next.js, port 3000) | `web` | `ui/Dockerfile` in sandbox-platform | Disabled until a verified image is set |
| Istio VirtualService: `/oan` to the API, the rest to the web app | `virtualService` | | Disabled |

Kong or APISIX is not part of this chart: try-it calls for gateway products go to
the environment's existing gateway (`config.gateway.uatUrl`, `prodUrl`; `sandboxUrl` is
the fallback). If that URL is cluster-internal, set `config.gateway.uatPublicUrl` /
`prodPublicUrl` to the gateway's public URL: code samples and the try-it URL that
partners copy into Postman use it.

### Participant apps, Keycloak and the gateway

| Values | What it turns on |
| --- | --- |
| `config.gateway.appSync.enabled` | Apps follow the gateway (`config.gateway.sync.adminUrl`, key `GATEWAY_ADMIN_TOKEN`). `apikey` / `keycloak` mode: every app is written to the APISIX Admin API as a consumer (needs the **admin** key). `oauth` mode: the routes are only read (their ids go into the app tokens; the **viewer** key is enough) and nothing is written to the gateway. |
| `config.keycloak.enabled` | Participants become Keycloak users in `config.keycloak.realm` (default `partner`); with `participantAuth: keycloak` Keycloak checks the portal password. Secrets `KEYCLOAK_ADMIN_CLIENT_SECRET`, `KEYCLOAK_LOGIN_CLIENT_SECRET`. |
| `config.gateway.partnerAuth: oauth` | OAuth 2.0 client credentials: every app key is also a Keycloak client (client_id = API key, client_secret = API secret). Partners get a token from the realm's token endpoint and send only that token in `X-Partner-Token`; the portal's try-it page has **Get token**. Needs `keycloak.enabled`, `appSync.enabled` (the chart refuses otherwise) and the partner routes of chart `oan-partner-gateway` ([sandbox-platform `deploy/apisix-partner-gateway`](https://github.com/Centre-for-Open-Societal-Systems/sandbox-platform/tree/develop/deploy/apisix-partner-gateway)) on the gateway. |
| `config.keycloak.prod.*`, `config.gateway.prodAdminUrl` | Production's own Keycloak and APISIX Admin API (each cluster has its own). All optional: **empty = production apps use the main Keycloak / gateway**, still with their own keys and a token naming only `production`. With `keycloak.prod.url` set, the Secret needs `KEYCLOAK_PROD_ADMIN_CLIENT_SECRET` (that Keycloak's `oan-sandbox-provisioner`, made with `setup_partner_realm.py`); with `gateway.prodAdminUrl`, `GATEWAY_PROD_ADMIN_TOKEN`. Participants and portal sign-in stay on the main Keycloak. |
| `config.apps.*` | Per-participant app and key limits, and the life of API keys: `keyLifetimeDays` (0 = never expire), `keyRotationGraceDays` (a rotated key keeps working this long), `keyExpiryWarnDays`, `keyMaintenanceMinutes`. A partner sees a key's secret once; rotating gives a new one. |
| `config.support.slaHours`, `config.audit.retentionDays` | Hours before an unanswered support query shows as overdue (0 = no SLA); days after which audit entries are deleted (0 = keep forever). |
| `config.partnerPortal.clientId` | OpenG2P Consent Manager partner portal: approved participants get its role and `partner_id`. |
| `config.partnerManagement.enabled` | Approved participants are onboarded in OpenG2P Partner Management. Secret `PM_CLIENT_SECRET`. |

The realm's clients (`oan-partner-api`, `oan-sandbox-provisioner` with manage-clients,
`oan-sandbox-portal`) and the `participant_uid` attribute are made once with
`backend/scripts/keycloak/setup_partner_realm.py` in sandbox-platform. Dev values:
[environments/dev/values/sandbox.yaml](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/environments/dev/values/sandbox.yaml).

## Before enabling

1. **Images.** Build and push both images; set `api.image` and `web.image`
   (digest preferred). The web image has the browser API URL built in: build it
   with `NEXT_PUBLIC_API_BASE_URL=https://<global.hostname>/oan`, one image per
   environment. The API image is the same everywhere.
2. **Database.** On the shared PostgreSQL (`config.db.host`), create the database
   `config.db.name` and the user `config.db.user`. The API applies its migrations
   on start.
3. **Secret.** Create a Secret in the release namespace and set `secret.name`.
   Required keys: `DB_PASSWORD`, `JWT_ACCESS_TOKEN_KEY`, `JWT_REFRESH_TOKEN_KEY`
   (two different long random values). With participant apps also
   `APP_CREDENTIAL_ENCRYPTION_KEY` (Fernet key; never change it once keys exist).
   Optional: `SMTP_PASSWORD`, `GATEWAY_ADMIN_TOKEN` (APISIX Admin API key: viewer for
   "Pull from gateway" and oauth mode, admin for app sync in apikey / keycloak mode), `KEYCLOAK_ADMIN_CLIENT_SECRET` and
   `KEYCLOAK_LOGIN_CLIENT_SECRET` (Keycloak), `GATEWAY_LOG_INGEST_TOKEN`,
   `PM_CLIENT_SECRET`, `KEYCLOAK_PROD_ADMIN_CLIENT_SECRET` and `GATEWAY_PROD_ADMIN_TOKEN` (only with
   a production Keycloak / gateway of its own), `SEED_ADMIN_PASSWORD` with `config.seed.adminEmail` (first start
   on an empty database: master administrator, masters, CMS content).
4. **Route.** Set `global.hostname` (one wildcard name such as
   `sandbox.development.oanstaging.com`) and enable `virtualService` on the shared
   Gateway `istio-system/development`.
5. **Mail.** Turn `config.mail` on for any shared environment; keep
   `config.devFixedOtp` empty.
6. **Gateway (app sync / oauth).** The APISIX Admin API must admit the cluster's
   egress IP (its `ip-restriction` whitelist), and the partner routes
   (`oan-partner-gateway`) must be installed with the same Keycloak issuer as
   `config.keycloak`.

After install: `GET https://<hostname>/oan/health` answers `200` with
`"database": "up"`; the web app opens on `https://<hostname>`; change the
seeded administrator password; try-it for a gateway product reaches the gateway.
With `partnerAuth: oauth`: a new participant appears in the Keycloak realm after
approval; an approved app's API key appears there as a client; **Get token** on the
try-it page returns a token, and try-it with it passes the gateway (a call without it
gets `401` "Missing app token").

See [included services](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/service-catalog.md),
the [service onboarding guide](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/service-onboarding.md)
and the sandbox [deployment checklist](https://github.com/Centre-for-Open-Societal-Systems/sandbox-platform#deployment-devops-checklist).
