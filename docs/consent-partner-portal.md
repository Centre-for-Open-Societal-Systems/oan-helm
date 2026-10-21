# OAN Consent Partner Portal

Chart **1.0.0-dev.6** adds the COSS partner browser portal to the existing
Commons Services chart. The pinned `openg2p-consent-manager:1.0.2` child remains
unchanged; a local parent template owns the additional workload. Defaults keep
the portal disabled for environments without partner authentication.

The new-dev target is:

<https://consent-partner-portal.development.oanstaging.com/>

The separate `consent-manager-partner.development.oanstaging.com` host remains
the partner API for validation, receipts and JWKS. It is not the browser portal.

## Components and source

- Values: `consentPartnerPortal` in Commons Services.
- Resources: `commons-services-cm-partner-portal` Deployment, Service and
  VirtualService, plus `commons-services-cm-partner-portal-config` ConfigMap.
- Source: COSS `consent-management` commit
  `d911269106b0d09b6308124c451642ab05087efc`, directory `partner-portal`.
- Image: `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/commons/consent-partner-portal`,
  pinned by digest in the chart and [build evidence](../releases/consent-partner-portal-20261019.json).
- Route: the shared `istio-system/development` Gateway serves the UI and forwards
  `/consent/v1/partner-portal/` directly to the existing `commons-services-cm-api`.
  This uses wildcard DNS/TLS and requires no individual Route 53 record.

The image is a static React application served by a non-root Nginx container.
Public runtime configuration is mounted at `/config.json`; it contains no client
secret or bearer token. The deployment has a read-only filesystem, writable
temporary volume, no Kubernetes service-account token and HTTP health probes.

## Login and prerequisites

Use the **partner** Keycloak realm and public client `consent-partner-portal`,
with authorization-code flow and mandatory PKCE S256. Password grants, implicit
flow and self-registration stay disabled. Redirects and origins are restricted
to the portal host. Staff realm accounts do not automatically become partner
accounts.

Each operator needs `PARTNER_OPERATOR` or `PARTNER_ADMIN` and an administrator-set
`partner_id` matching its approved partner identity. That attribute must not be
user-editable. The access-token mapper must include it. The staff Consent API
needs the matching `CONSENT_MANAGER_PARTNER_AUTH_ISSUER` and internal JWKS URL.

New-dev preparation creates only the isolated `oan-partner-e2e` browser test user
and synthetic partner identifier. Its generated credentials stay in the
`commons/oan-partner-portal-test-user` Secret. Existing staff users, real partner
identities and Consent bindings are preserved. In Rancher, select the `commons`
namespace and open that Secret to retrieve test credentials privately.

Real partner use also needs approved Partner Management/Consent bindings, scopes,
controllers and purposes. An isolated test account without bindings should see
empty lists, never another partner's records. Signed-form evidence uploads need
separately configured private S3 storage. Subject national-ID authentication
requires its own eSignet setup when enabled.

**OTP remains unavailable pending SMS.** This portal rollout does not enable OTP
logging, bucket publishing, SMS workarounds or a weaker consent method. Portal
availability and successful login do not establish OTP consent issuance or a
complete partner data-release workflow.

## Upgrade and verification

Merge the [public portal overlay](../examples/dev/consent-partner-portal.yaml) into
the existing release's private values after preparing authentication. Keep the
existing release name `commons-services` and namespace `commons`, Secrets,
dependency pins and shared-service settings. Do not install a second Commons
release. Preserve the current URL compatibility and initialization-Job suppression
renderer; `--no-hooks` alone does not suppress non-hook bootstrap Jobs.

Before upgrading, back up release values/manifests, identity configuration and
the Consent database privately. Compare the complete proposed manifest against
the installed release. Only the new portal resources and the staff Consent API's
partner-auth configuration should change. Helm rollback does not undo database
migrations or separately prepared identity resources.

Verify HTTPS UI and deep links, noncached runtime configuration, PKCE sign-in,
`/me`, requests/consents/bindings and denial of missing or staff-realm tokens.
Check Pod readiness and the exact image digest, then rerun the
[automated staff regression](automated-staff-test.md) to catch regressions in
existing Consent and Aggregation endpoints. Keep browser traces, credentials and
raw response bodies private.
