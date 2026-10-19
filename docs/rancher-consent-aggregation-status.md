# Dev Consent and Aggregation: installed status

Verified 19 October 2026 on `13.201.58.55`.

| Rancher location | Current state |
| --- | --- |
| Apps > Repositories > `oan-coss-preview` | Downloaded; raw GitHub fork preview, no Pages required |
| Apps > Installed Apps > namespace `commons` > `commons-services` | Chart `openg2p-commons-services` **1.0.0-dev.5**, Helm revision **17**, deployed |
| Workloads > Deployments > `commons-services-cm-api` | New COSS Consent API, ready |
| Workloads > Deployments > `commons-services-cm-partner-api` | Same new API image, partner audience, ready |
| Workloads > Deployments > `commons-services-cm-ui` | New COSS Consent UI, ready |
| Workloads > Deployments > `commons-services-aggregation-api` | New stateless COSS Aggregation API, enabled and ready |
| VirtualServices > `commons-services-aggregation-api` | `aggregation.development.oanstaging.com` through `istio-system/development` |

URLs:

- Consent UI: <https://consent-manager.development.oanstaging.com/>
- Aggregation API docs: <https://aggregation.development.oanstaging.com/docs>
- Aggregation health: <https://aggregation.development.oanstaging.com/ping>
- Public catalog: <https://aggregation.development.oanstaging.com/aggregation/v1/registries>

Aggregation is an API, with no separate UI at `/`. Chart defaults stay disabled
for new installations; the reviewed private values enable the existing dev release.
Old URL compatibility stays active. Existing release names, dependencies, Secret
payloads and unrelated workload images were preserved.

## Remaining functional prerequisites

- Assign `AGGREGATION_STAFF_VIEWER` to the intended **staff users**. No human
  account was granted access automatically. The separate service identity has
  `Data Supervisor` on the three registry clients; all three metadata checks pass.
- Register Aggregation's persistent public key in Partner Management and review
  the corresponding CM bindings, scopes, controllers, purposes and current
  `consent_method`. No existing partner policies were widened or self-approved.
- Configure the partner realm/client/`partner_id` claims before using stored
  `authorize.consent_id`. The environment has no partner realm yet.
- OTP remains unavailable pending SMS, as requested. No OTP logs or bucket
  publishing were enabled. Do not weaken an OTP policy to bypass this prerequisite.
- Verify catalog field allowlists and identity matching before partner data
  release. Metadata/health checks do not establish a beneficiary search workflow.
- Consent still uses its original demo receipt key for compatibility. Activating
  the previously prepared private key needs a separate trust/retention plan.

## Upgrade controls still required

The rollout used the existing release, saved private values, **`--no-hooks` and
the reviewed initialization-Job suppression post-renderer**. The current saved
legacy values still require the URL/Gateway compatibility renderer. A native
render without it contains bootstrap Jobs and old Gateway overrides: turning off
hooks alone does not suppress the non-hook Jobs. Do not click through another
Rancher upgrade until these controls are reproduced or its native values/resource
retention plan is reviewed. Current installed workloads are already at dev.5.

Private recovery and reviewed files are on the server:

- `/var/backups/oan-consent-aggregation/20261019T105654Z`
- `/var/lib/oan-aggregation-development/helm-preparation`

Keep these outside Git. Before another upgrade, refresh the backup and comparison.
Helm rollback does not undo DB schema changes. Both CM audiences migrate at start;
one staff Pod hit a concurrent migration uniqueness error and restarted once,
then recovered. Verify migration behavior when planning later restarts/upgrades.

## Verification scope

- All **69** application Deployments/StatefulSets ready.
- **12/12** live Postman health/catalog/missing-or-invalid-token assertions pass.
- Actual Aggregation service credentials reach registry metadata in all **3**
  registries; no personal records were read.
- All **32/32** canonical URL checks pass after repairing Crop's separate URL
  regression (revision 13 to 14; exact chart retained, URL-only change).
- Aggregation **171** unit tests; Consent **195** tests with disposable PostgreSQL.
- A fresh live DB copy passed migration twice, preserving table row counts/IDs.
- Five new packages plus 20 historical archives verified from GitHub; CI passes.

No authorized-human login, real beneficiary search, OTP delivery, stored-consent
flow or signed partner callback was tested. Full evidence:
[`live-consent-aggregation-20261019.json`](../releases/live-consent-aggregation-20261019.json).
