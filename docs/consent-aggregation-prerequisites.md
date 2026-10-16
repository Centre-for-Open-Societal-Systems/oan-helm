# Prepare Consent Manager and Aggregation for new dev

Prepare Consent first, then Aggregation. Keep `aggregationApi.enabled: false`
until every Aggregation prerequisite below is resolved. This guide does not
deploy workloads, create identities or run database migrations.

## Current readiness and compatibility

| Item | Evidence / remaining work |
| --- | --- |
| COSS Consent images | API/UI/sanity `develop-5361069` images are verified and digest-pinned in Commons values; pull access and runtime compatibility still need checking |
| Aggregation image | No published image was verified during preparation; publish an approved build and record its source revision and digest |
| Consent/Aggregation compatibility | **Not established.** The pinned Consent source `536106974a7f6d67501a45dfc02cb9da95348f37` lacks the `subject_consent_enabled` / `subject_consent_required` settings required by the Aggregation contract inspected at `8fe3bf97030bb0b3f6283c2123ad58026af6cc50` |
| Consent API routing | Current chart serves staff and partner APIs separately; beneficiary API is disabled. Aggregation has one `cm_base_url` for all required CM paths |
| Aggregation public route | Unconfirmed; chart creates only a ClusterIP Service |

Image availability is not proof that these versions work together. Select and
publish compatible Consent API/UI images before enabling the Aggregation flow.
Confirm the required endpoints and response fields against that exact image.
Setting an environment variable cannot add behavior missing from an older image.
Changing the shared Consent build requires migration and existing-client review.

Reference sources: [pinned Consent configuration](https://github.com/Centre-for-Open-Societal-Systems/consent-management/blob/536106974a7f6d67501a45dfc02cb9da95348f37/backend/src/openg2p_consent_manager/config.py),
[Aggregation's CM contract](https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api/blob/8fe3bf97030bb0b3f6283c2123ad58026af6cc50/docs/CM-API-CONTRACT.md)
and [Aggregation settings](https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api/blob/8fe3bf97030bb0b3f6283c2123ad58026af6cc50/backend/src/openg2p_aggregation_layer/config.py).

## 1. Prepare the existing Consent release

Use release `commons-services`, namespace `commons`. Save its current chart,
Helm revision and private values, and back up the Consent database before the
shared-platform upgrade. Preserve other Commons service settings and owners.

| Prerequisite | What to check / Rancher values |
| --- | --- |
| PostgreSQL | Preserve `openg2p-consent-manager.global.consentDB: consent_manager` and `consentDBUser: consent_manager_user`, unless reviewed live values differ. Verify DB access and migration privileges |
| Database Secret | Existing default is Secret `consent-manager-db`, key `consent-manager-db-user`, in `commons`. Do not replace an existing password with an example |
| Image pulls | Confirm nodes or the workload ServiceAccount can pull the private ECR images, including seed/sanity Jobs. Check the rendered Pod/ServiceAccount configuration; the reused API templates do not directly consume a generic `global.imagePullSecrets` setting |
| Receipt signing | Preserve the existing signing key and key id. For a separately managed key, use `openg2p-consent-manager.consentManagerApi.signingKey.mode: existing` and point its Secret/key/password references to that key. Default names are `consent-manager-signing`, `cm_signing.p12`, and `password`. The inherited default is a public demo key; it is not a private environment key |
| Keycloak | Verify external issuer `https://keycloak-development.oanstaging.com/realms/staff`, reachable JWKS, the `consent-manager` client and appropriate admin/approver roles. Preserve client Secrets and the existing user login flow |
| Partner Management | Verify access to `commons-services-pm-partner-api` and that each partner's registered public key/reference matches its signed requests |
| AWE, when enabled | Verify approval policy `consent-manager.policy_change.v1`, service credentials, callback HMAC registration, and callback to `http://commons-services-cm-api.commons.svc.cluster.local/consent/v1/awe/webhooks/decision`. Preserve the existing enabled state; do not enable AWE without its policy/Secret setup |
| Public routes | Preserve working TLS/routing for `consent-manager-development.oanstaging.com` and `consent-manager-partner-development.oanstaging.com`; review UI login/API configuration |
| Upgrade values | Explicitly merge reviewed image overrides and `environments/dev/values/commons-services.yaml` into saved private values. The URL overlay does not select new image versions |

If a signing Secret is currently Helm-managed, changing its management mode or
replacing the key needs a separate retention/rotation plan. Do not switch modes
blindly: an upgrade can remove a resource that disappears from the chart.

For the eventual compatible Consent image, verify subject-consent narrowing,
strict subject consent, withdrawal handling and OTP behavior required by the
Aggregation contract. Configure `CONSENT_MANAGER_SUBJECT_CONSENT_ENABLED=true`
and `CONSENT_MANAGER_SUBJECT_CONSENT_REQUIRED=true` only after reviewing their
effect on all existing registry/partner clients. Both belong under
`openg2p-consent-manager.consentManagerApi.envVars`; these flags alone do not
make the currently pinned image compatible.

## 2. Prepare Aggregation resources outside Helm values

1. **Publish the image.** Use the approved Aggregation source revision and pin
   the framework dependency during the build. Supply its real repository and
   digest through `aggregationApi.image`. The application image serves port
   `8100`; no image build or application CI changes are part of this PR.
2. **Provision its own database/user.** It can use the existing PostgreSQL
   server, but must have a separate database and credentials. It must not use
   the Consent database as its store. Store credentials in a Secret in `commons`.
   The image entrypoint runs migrations before starting the API; review and
   back up data before first start or a version change.
3. **Provision its own persistent signing key.** Put the `.p12` and password in
   a namespace-local Secret, distinct from Consent's receipt key. Register the
   corresponding public key in Partner Management. The default sender id
   `aggregation-layer` maps to PM reference `PARTNER_AGGREGATION_LAYER`.
   All API workers/replicas must share the same key and key id.
4. **Prepare the registry catalog ConfigMap.** Start from the application's
   `deploy/registries.yaml`, replacing local Docker URLs with the actual
   cross-namespace partner Service URLs. Specify controller ids, binding
   audiences, identity matching, scopes and reviewed field allowlists. Confirm
   each registry can find and return the beneficiary's foundational ID.
5. **Register identities and policies.** Create a Keycloak client such as
   `aggregation-layer` with client-credentials access. At the inspected contract
   revision its service account needs `CONSENT_MANAGER_ADMIN` for CM policy
   reads. Keep its Secret private. Register partner-to-Aggregation and
   Aggregation-to-registry bindings with matching scopes/purposes/public keys;
   the inspected design uses `legitimate_interest` on registry hops. Obtain
   required policy approval when AWE is enabled. Helm does not create these
   bindings. The source registration script performs writes and self-approval;
   review it before adapting it to shared dev.
6. **Resolve CM routing.** The inspected Aggregation client appends every path
   to one `AGGREGATION_LAYER_CM_BASE_URL`: staff policy/list endpoints, partner
   validation/status endpoints and beneficiary consent-request endpoints.
   A URL pointing only to `cm-api` or only to `cm-partner-api` is insufficient.
   Prepare a reviewed internal gateway to the split audiences, or a separately
   reviewed CM deployment serving `apiAudience: all`. Enable/configure the
   beneficiary endpoints and their token validation as part of that decision;
   do not expose staff operations through the public partner route.
7. **Prepare subject authentication and OTP.** Set a real issuer, JWKS URL,
   expected audience and subject-id claims that match the registry identity.
   An unset issuer causes the inspected code to skip signature verification
   even when `AUTH_ENABLED=true`. Supply an environment-specific OTP salt and
   review how test subjects receive OTPs. The inspected Fayda provider applies
   rules locally; it is not a live SMS/Fayda integration. Debug OTP/bucket
   publishing require an explicit dev-only decision.
8. **Prepare routing/network access.** Allow Aggregation to reach CM, Keycloak,
   registry partner APIs, PostgreSQL and the partner's `on-search` callback.
   Provide environment-owned ingress/TLS only after confirming an Aggregation
   hostname. The chart does not create an ingress or gateway for Aggregation.

## 3. Map prepared configuration into Rancher

Keep the image and credentials private as appropriate. These are the exact
environment names in the inspected Aggregation application; use `aggregationApi.env`
for public configuration and `envFrom` / `env[].valueFrom.secretKeyRef` for secrets.

| Purpose | Environment variables |
| --- | --- |
| Own PostgreSQL DB | `AGGREGATION_LAYER_DB_HOSTNAME`, `AGGREGATION_LAYER_DB_PORT`, `AGGREGATION_LAYER_DB_DBNAME`, `AGGREGATION_LAYER_DB_USERNAME`, `AGGREGATION_LAYER_DB_PASSWORD` |
| CM routing/auth | `AGGREGATION_LAYER_CM_BASE_URL`, `AGGREGATION_LAYER_CM_TOKEN_URL`, `AGGREGATION_LAYER_CM_CLIENT_ID`, `AGGREGATION_LAYER_CM_CLIENT_SECRET` |
| Persistent signing | `AGGREGATION_LAYER_SIGNING_P12_PATH`, `AGGREGATION_LAYER_SIGNING_P12_PASSWORD`, `AGGREGATION_LAYER_SIGNING_KID` |
| Registry catalog | `AGGREGATION_LAYER_REGISTRY_CATALOG_PATH` |
| Subject token validation | `AGGREGATION_LAYER_AUTH_ENABLED`, `AGGREGATION_LAYER_AUTH_ISSUER`, `AGGREGATION_LAYER_AUTH_JWKS_URL`, `AGGREGATION_LAYER_AUTH_AUDIENCE` |
| Consent screen | `AGGREGATION_LAYER_CONSENT_UI_BASE_URL` (confirm the compatible subject consent UI, not just an admin page) |
| OTP | `AGGREGATION_LAYER_OTP_SALT`, `AGGREGATION_LAYER_OTP_DEBUG_ENABLED`, `AGGREGATION_LAYER_OTP_PUBLISH_ENABLED` |
| Initial dev execution | `AGGREGATION_LAYER_KAFKA_ENABLED=false`, `AGGREGATION_LAYER_CM_POLL_IN_APP=true` |

Example wiring shape, **incomplete and deliberately disabled**. The resource
names below are proposed names, not a claim that the Secrets/ConfigMap exist:

```yaml
aggregationApi:
  enabled: false
  image:
    repository: '' # Supply an actual published repository before enabling.
    digest: ''     # Supply its verified sha256 digest.
  envFrom:
    - secretRef:
        name: aggregation-api-runtime
  env:
    - name: AGGREGATION_LAYER_SIGNING_P12_PATH
      value: /app/keys/aggregation.p12
    - name: AGGREGATION_LAYER_SIGNING_P12_PASSWORD
      valueFrom:
        secretKeyRef:
          name: aggregation-api-signing
          key: password
    - name: AGGREGATION_LAYER_REGISTRY_CATALOG_PATH
      value: /app/config/registries.yaml
    - name: AGGREGATION_LAYER_KAFKA_ENABLED
      value: 'false'
    - name: AGGREGATION_LAYER_CM_POLL_IN_APP
      value: 'true'
  volumes:
    - name: signing
      secret:
        secretName: aggregation-api-signing
        items:
          - key: aggregation.p12
            path: aggregation.p12
    - name: catalog
      configMap:
        name: aggregation-api-catalog
  volumeMounts:
    - name: signing
      mountPath: /app/keys
      readOnly: true
    - name: catalog
      mountPath: /app/config
      readOnly: true
```

`aggregation-api-runtime` must provide the remaining required environment
variables above, including the DB password, CM client secret and OTP salt.
Add `aggregationApi.imagePullSecrets` when using private registry pull Secrets.
The initial dev profile uses in-process execution; it does not provide durable
callback delivery. Kafka/worker/reaper operation needs separate preparation;
this chart currently defines only the Aggregation API Deployment and Service.

## 4. Check before enabling, then verify the manual rollout

Before upgrading, review the rendered manifests: images/digests, private Secret
references, mounts, namespace, shared-service changes and API routing. Upgrade
the existing owner; do not install another Commons release over its resources.

Acceptance checks for the eventual rollout: database migration succeeds; Pods
pull the approved images; invalid tokens are rejected; a request without subject
consent makes no registry calls; approval and any required OTP release only the
allowed fields; denial/withdrawal stops release; signed registry hops and the
partner callback verify against the registered key. Test the exact image pair.
A ready Pod or a successful Helm render is not evidence of this behavior.

These are required future acceptance checks, not reported test results. No
cluster rollout or API calls were performed to write this guide. Helm rollback
does not undo database migrations, policy registrations or external IAM changes.
