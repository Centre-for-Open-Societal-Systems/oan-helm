# Dev Consent and Aggregation: installed status

Portal rollout verified 21 October 2026 on `13.201.58.55`.

| Rancher location | Current state |
| --- | --- |
| Apps > Repositories > `oan-coss-preview` | Downloaded; raw GitHub fork preview includes dev.6. Stable `oan-coss` gets dev.6 after the upstream PR is merged. No Pages required. |
| Apps > Installed Apps > namespace `commons` > `commons-services` | Chart `openg2p-commons-services` **1.0.0-dev.6**, Helm revision **18**, deployed |
| Workloads > Deployments > `commons-services-cm-api` | New COSS Consent API, ready |
| Workloads > Deployments > `commons-services-cm-partner-api` | Same new API image, partner audience, ready |
| Workloads > Deployments > `commons-services-cm-ui` | New COSS Consent UI, ready |
| Workloads > Deployments > `commons-services-cm-partner-portal` | OAN Consent Partner Portal, ready; partner-realm PKCE login verified |
| Workloads > Deployments > `commons-services-aggregation-api` | New stateless COSS Aggregation API, enabled and ready |
| VirtualServices > `commons-services-aggregation-api` | `aggregation.development.oanstaging.com` through `istio-system/development` |

URLs:

- Consent UI: <https://consent-manager.development.oanstaging.com/>
- Partner portal: <https://consent-partner-portal.development.oanstaging.com/>
- Aggregation API docs: <https://aggregation.development.oanstaging.com/docs>
- Aggregation health: <https://aggregation.development.oanstaging.com/ping>
- Public catalog: <https://aggregation.development.oanstaging.com/aggregation/v1/registries>

Aggregation is an API, with no separate UI at `/`. Chart defaults stay disabled
for new installations; the reviewed private values enable the existing dev release.
Old URL compatibility stays active. Existing release names, dependencies, Secret
payloads and unrelated workload images were preserved.

## Remaining functional prerequisites

- The selected staff users `admin` and `nina.patel` have
  `AGGREGATION_STAFF_VIEWER`, reverified on 21 October. The separate service identity has
  `Data Supervisor` on the three registry clients; all three metadata checks pass.
- Register Aggregation's persistent public key in Partner Management and review
  the corresponding CM bindings, scopes, controllers, purposes and current
  `consent_method`. No existing partner policies were widened or self-approved.
- Partner realm, portal client and administrator-controlled `partner_id` claims
  are prepared. Aggregation's partner issuer/JWKS and integration identities still
  need review before using stored `authorize.consent_id`. The isolated portal
  test partner has no approved bindings or grants.
- Signed-form evidence uploads need private S3 configuration, currently unset.
- OTP remains unavailable pending SMS, as requested. No OTP logs or bucket
  publishing were enabled. Do not weaken an OTP policy to bypass this prerequisite.
- Verify catalog field allowlists and identity matching before partner data
  release. Synthetic staff search/tabs pass; this does not establish consent-based
  partner data release.
- Consent still uses its original demo receipt key for compatibility. Activating
  the previously prepared private key needs a separate trust/retention plan.

## Upgrade controls still required

The rollout used the existing release, saved private values, **`--no-hooks` and
the reviewed initialization-Job suppression post-renderer**. The current saved
legacy values still require the URL/Gateway compatibility renderer. A native
render without it contains bootstrap Jobs and old Gateway overrides: turning off
hooks alone does not suppress the non-hook Jobs. Do not click through another
Rancher upgrade until these controls are reproduced or its native values/resource
retention plan is reviewed. Current Commons Services is already at dev.6.

The portal upgrade added four resources and propagated only three reviewed
partner-auth variables through the existing Consent API/init/expiry containers.
The private comparison found no removed resources, unrelated changes or existing
image changes. The database and release values/manifests were backed up at
`/var/backups/oan-consent-partner-portal/upgrade-20261021T043152Z`; reviewed files
are in `/var/lib/oan-aggregation-development/partner-portal`.

Private recovery and reviewed files are on the server:

- `/var/backups/oan-consent-aggregation/20261019T105654Z`
- `/var/lib/oan-aggregation-development/helm-preparation`

Keep these outside Git. Before another upgrade, refresh the backup and comparison.
Helm rollback does not undo DB schema changes. Both CM audiences migrate at start;
one staff Pod hit a concurrent migration uniqueness error and restarted once,
then recovered. Verify migration behavior when planning later restarts/upgrades.

## Verification scope

- All **70** application Deployments/StatefulSets ready; Istio analysis passes.
- Normal partner browser PKCE login and Requests/Consents/Access pages pass.
- Portal Postman **25/25** assertions pass, including correct partner identity,
  empty isolated lists, deep links and missing/invalid/staff-token rejection.
- Staff search/tab regression **107/107** assertions pass across three real
  registries, four marked synthetic fixtures and **20** returned tabs.
- **12/12** live Postman health/catalog/missing-or-invalid-token assertions pass.
- Actual Aggregation service credentials reach registry metadata in all **3**
  registries; no personal records were read.
- All **32/32** canonical URL checks pass after repairing Crop's separate URL
  regression (revision 13 to 14; exact chart retained, URL-only change).
- Aggregation **171** unit tests; Consent **195** tests with disposable PostgreSQL.
- A fresh live DB copy passed migration twice, preserving table row counts/IDs.
- Five new packages plus 20 historical archives verified from GitHub; CI passes.

The browser test uses an isolated synthetic partner account. Real beneficiary
search, OTP delivery, stored-consent release and signed partner callbacks remain
outside these checks. Current evidence:
[`live-consent-partner-portal-20261021.json`](../releases/live-consent-partner-portal-20261021.json).
Earlier rollout evidence:
[`live-consent-aggregation-20261019.json`](../releases/live-consent-aggregation-20261019.json).
