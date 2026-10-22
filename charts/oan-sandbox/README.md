# OAN Sandbox

OpenAgriNet (OAN) developer sandbox, developed in the Centre for Open Societal
Systems (COSS) repositories: a public site with the API catalogue, a participant
portal (sign-up, environment access, try-it console, API history, support) and an
admin console (participants, products and end-points, CMS, masters, queries).

| Source | GitHub repository |
| --- | --- |
| OAN application | [sandbox-platform](https://github.com/Centre-for-Open-Societal-Systems/sandbox-platform) |
| OAN Helm sources | [oan-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/oan-sandbox) |

Chart version **1.0.0-dev.7**. It has no OpenG2P dependency and owns no existing
release, so installing it changes no other chart's resources.

## What it installs

| Workload | Values key | Image | Default |
| --- | --- | --- | --- |
| API (FastAPI, port 8000, health `/oan/health`); uploads PVC | `api` | `docker/sandbox-api/Dockerfile` in sandbox-platform | Disabled until a verified image is set |
| Web (Next.js, port 3000) | `web` | `ui/Dockerfile` in sandbox-platform | Disabled until a verified image is set |
| Istio VirtualService: `/oan` to the API, the rest to the web app | `virtualService` | | Disabled |

Kong or APISIX is not part of this chart: try-it calls for gateway products go to
the environment's existing gateway (`config.gateway.sandboxUrl`).

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
   (two different long random values). Optional: `SMTP_PASSWORD`,
   `GATEWAY_ADMIN_TOKEN` (gateway Admin API key for "Pull from gateway"),
   `SEED_ADMIN_PASSWORD` with `config.seed.adminEmail` (first start on an empty
   database: master administrator, masters, CMS content).
4. **Route.** Set `global.hostname` (one wildcard name such as
   `sandbox.development.oanstaging.com`) and enable `virtualService` on the shared
   Gateway `istio-system/development`.
5. **Mail.** Turn `config.mail` on for any shared environment; keep
   `config.devFixedOtp` empty.

After install: `GET https://<hostname>/oan/health` answers `200` with
`"database": "up"`; the web app opens on `https://<hostname>`; change the
seeded administrator password; try-it for a gateway product reaches the gateway.

See [included services](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/service-catalog.md),
the [service onboarding guide](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/service-onboarding.md)
and the sandbox [deployment checklist](https://github.com/Centre-for-Open-Societal-Systems/sandbox-platform#deployment-devops-checklist).
