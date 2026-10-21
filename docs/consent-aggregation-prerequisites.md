# Consent Manager and Aggregation: current dev setup

Current chart: **1.0.0-dev.6**. Consent comes from COSS commit
`48e64c249056a1aed3ce728c61c1bc059a288a50`; Aggregation comes from
`a5fa17fd7e7f50eb9a8649c267a9cc59223c934c`. Four images are published to the
existing ECR repositories and selected by digest. See [current evidence](../releases/consent-aggregation-20261019.json).
Historical candidate/integration reports describe older images only. The optional
[partner portal](consent-partner-portal.md) adds an independently pinned image
from merged commit `d911269106b0`; that merge changes documentation only relative
to the current API source.

The existing dev release is now upgraded, with Aggregation enabled. Runtime
Secrets, catalog and registry service identity are prepared; see
[installed status and remaining functional prerequisites](rancher-consent-aggregation-status.md).
The checklist below also applies when preparing another environment.

## Current application contract

Aggregation is stateless: **no database, migration, Kafka, worker, reaper or OTP
storage**. Remove old Aggregation DB/OTP/poll configuration. It calls the existing
Consent **partner** API for `/consent/v1/validate` and
`/consent/v1/consents/{id}/status`. No all-audience internal router is needed.

The latest Consent settings no longer define global `subject_consent_enabled`
or `subject_consent_required`. Policies use per-binding `consent_method`
(`partner_signed`, `otp`, or `internal`). Existing clients that omit it retain
their binding's current method. Signature/policy acceptance alone is not proof
of an OTP grant. Do not run historical registration scripts using `lawful_basis`
or self-approval unchanged against this version.

**User decision: keep OTP unavailable pending SMS.** Neither provider in the
inspected source delivers SMS. Keep `CONSENT_MANAGER_OTP_LOG_CODES=false` and
`CONSENT_MANAGER_OTP_PUBLISH_ENABLED=false`. Without delivery, issuance fails
closed with 503. Do not enable logging/bucket workarounds or weaken an `otp`
binding to make a demo pass.

## Preparation and remaining prerequisites

| Item | Configuration and verification |
| --- | --- |
| Existing owner | Upgrade `commons-services` in `commons`; preserve other shared service settings, resource names and ownership. Never install a second Commons release. |
| ECR | Existing `commons/ecr-pull-secret` can read both repositories. Verify exact new digests and Pod pulls; retain its refresh mechanism. |
| Consent DB | Preserve `consent_manager`, user `consent_manager_user`, Secret `consent-manager-db`, key `consent-manager-db-user`. A fresh live copy passed migration twice with table row counts/IDs preserved; back up again immediately before deployment. |
| Consent signing | Retain the existing key/Secret. The current release still uses its bundled demo key; an earlier prepared private key is not active. Rotation needs a separate retention/trust plan, including the old Helm-managed Secret. |
| Staff caller | Verified staff issuer/JWKS, default role `AGGREGATION_STAFF_VIEWER`. Grant it only to intended users. |
| Registry staff identity | `aggregation-layer-staff` client-credentials identity with a verified view-only role on each registry. Put its secret in `aggregation-api-runtime`; do not reuse an admin credential. |
| Aggregation signing | Persistent Secret `aggregation-api-signing`, shared by all workers. Register its public key in Partner Management as `PARTNER_AGGREGATION_LAYER` for sender `aggregation-layer`. Distinct from Consent's receipt key. |
| Registry catalog | `aggregation-api-catalog`: actual cross-namespace partner/staff Services, controller IDs, scope names, identity matching and reviewed field allowlists. Verify source mappings against each environment before data release. |
| Partner bindings | PM identity/key registration and explicit CM bindings matching catalog audience/controller/scopes/purposes and current `consent_method`. Do not widen existing partner policies. |
| Stored consent | `authorize.consent_id` requires a verified partner-realm issuer/JWKS, correct `partner_id` claim and stored grant for `aggregation_layer`. The partner realm and portal browser client are prepared. Aggregation partner issuer/JWKS and the appropriate integration identities/bindings still need configuration; an empty issuer refuses this path. |
| Partner portal / OTP | Portal is deployed on new-dev using dev.6, with partner realm/client/roles/claims and same-origin routing. Prepare those resources before enabling another environment. SMS remains a separate prerequisite for OTP; see the [portal guide](consent-partner-portal.md). |
| Public route | Optional `aggregationApi.virtualService` uses `aggregation.development.oanstaging.com` and `istio-system/development`. Existing wildcard DNS/TLS handles it. |

## Rancher values

Defaults keep `aggregationApi.enabled: false`. A published image does not supply
runtime resources. See [the runtime overlay](../examples/dev/aggregation-runtime.yaml);
create and verify referenced Secrets/ConfigMap before enabling. Credentials stay
outside Git.

| Purpose | Current Aggregation variables |
| --- | --- |
| CM routing | `AGGREGATION_LAYER_CM_BASE_URL=http://commons-services-cm-partner-api.commons.svc.cluster.local` |
| Staff verification | `AGGREGATION_LAYER_AUTH_ENABLED=true`, `AGGREGATION_LAYER_AUTH_ISSUER`, `AGGREGATION_LAYER_AUTH_JWKS_URL`, optional audience |
| Staff caller roles | `AGGREGATION_LAYER_STAFF_SEARCH_ROLES` (JSON list) |
| Registry staff identity | `AGGREGATION_LAYER_STAFF_API_TOKEN_URL`, `AGGREGATION_LAYER_STAFF_API_CLIENT_ID`, `AGGREGATION_LAYER_STAFF_API_CLIENT_SECRET` |
| Signing | `AGGREGATION_LAYER_SIGNING_P12_PATH`, `AGGREGATION_LAYER_SIGNING_P12_PASSWORD`, `AGGREGATION_LAYER_SIGNING_KID` |
| Catalog | `AGGREGATION_LAYER_REGISTRY_CATALOG_PATH` |
| Partner verification | `AGGREGATION_LAYER_PARTNER_AUTH_ISSUER`, `AGGREGATION_LAYER_PARTNER_AUTH_JWKS_URL`, optional audience/partner claim |

CM partner validation/status need no CM admin role. Keep staff and partner
authentication separate. An unset partner issuer refuses stored-consent calls.

## Upgrade and acceptance

1. Add/refresh the raw GitHub repository using [the Rancher guide](rancher-dev.md)
   and select the exact prerelease version.
2. Retain package/revision, private values, live overrides, Secrets and DB backup.
   Compare rendered resources with live resources, including unrelated services.
3. Upgrade the existing `commons-services/commons` owner with reviewed values.
   Suppress initialization/seed Jobs. Consent's entrypoint migrates its DB.
4. Check running digests, Secret mounts, `/ping`, missing/invalid-token rejection,
   UI login and old/new URL compatibility. Verify registry staff access using an
   intended authorized caller, not an admin impersonation.
5. Keep partner data searches pending until PM keys, CM policies, partner auth and
   usable consent are verified. OTP remains pending SMS. Health checks do not
   establish these workflows.

Helm rollback does **not** reverse database migrations, policy/IAM writes or key
rotation. This migration removes old columns and changes constraints: retain
the private backup and prepared DB recovery procedure. Old URL compatibility
remains until the user confirms completion.
