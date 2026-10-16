# Dev readiness and provenance

All five charts are packageable. Installing a package still requires the
environment's private values, pull credentials and service prerequisites.
Rendering does not prove runtime compatibility or migration safety.

| Component | Available evidence | Prerequisites / default behavior |
| --- | --- | --- |
| Farmer Registry | Source `90811b6`, platform `1.2.2-rc.544`; core images `90811b61a59f` verified in ECR | Retain current release values, database/identity/Secret wiring and reporting preparation |
| Crop Sown Registry | Source `f5be6d2`, platform `1.2.2-rc.544`; core images `develop-88` verified in ECR | Retain current values and inspect platform/schema migration if installed dependency differs |
| Livestock Registry | Source `bf78e69`, platform `1.2.2-rc.544`; core images `bf78e69a5fd6` verified in ECR | Preserve Master Data/registry Secret wiring; select exact chart version even though current chart numbering is higher |
| DA Registry | Full chart verified at `9714c3c5307a7e61f4379b613229837a4b76e952`; platform `1.2.2-rc.544` | No verified backend images; application/initialization components disabled. Confirm namespace, images, DB and IAM before enabling |
| Commons Services | Latest published upstream `2.3.4-rc.247`, checksum verified | Shared-platform upgrade from dev `2.3.4-rc.245`; reconcile every saved shared-service setting |
| Farmer/Crop/Livestock dashboard API | Three published digests verified in ECR; Farmer/Crop currently deployed | Disabled by default; Farmer needs `analytics.reportingViews`, Crop/Livestock need `reporting.views`, DB Secrets and authentication settings |
| Registry dashboard UI | Configurable Deployment/ClusterIP Service in every registry | Disabled; current standalone dashboard images unavailable. Confirm IAM URL/domain/provider/client roles/Secrets and routing |
| DA dashboard API/UI | Optional configurable workloads included | Disabled pending images and confirmed runtime/database contracts |
| COSS Consent API/UI/sanity | Default `develop-5361069` retained; new `dev-d6ce86b9e3f9` candidates published with [image overlay](../examples/dev/consent-image-values.yaml) and [evidence](../releases/consent-candidate.json) | Candidate import/schema/signing/UI checks and 30/30 local pair scenarios pass; seven sanity-image tests collected, not run. Existing-database upgrades and authenticated split routing remain unverified |
| Aggregation API | Source `8fe3bf9`; published ECR candidate `oan/commons/aggregation-api:dev-8fe3bf97030b`, digest verified; 96 unit tests and 30/30 local pair scenarios passed; [evidence](../releases/aggregation-candidate.json) | Disabled: cluster pull credential gets 403 for the new repository; pinned Consent build predates required subject-consent settings. Resolve pull access, compatible Consent, split CM routing/beneficiary API, own DB, key, catalog, bindings and auth; see [preparation guide](consent-aggregation-prerequisites.md) |
| Connectors / shared OAN dashboard | Existing independent releases confirmed in dev | Remain outside these five charts; keep current owners |
| Commons Base | New preparation pin `2.3.4-rc.245`; dev currently `commons/commons` at `2.3.3` | Install directly from OpenG2P under existing owner; infrastructure upgrade is separate work |

`releases/provenance.json` records commits, imported-file hashes, dependency pins
and archive checksums. `releases/components.json` records image tags/digests and
unavailable components. No synchronized component build number is claimed.
Registry core/seed/sanity values use valid `repository:tag@sha256:...` references
because some pinned templates only support tags. Optional workloads additionally
support `image.digest` directly.

Commons Services archive SHA-256:
`96ab00f327652a4cc3d511525e1ac5260813d744a11620054e2491b698206272`.
The fresh index and downloaded archive matched on 16 October 2026. Consent
dependency versions remain as published. The dev profile now uses verified
canonical URLs; Superset/Certify are disabled as observed, and unconfirmed
notification/browser endpoints remain unset. Private live
values and Secret payloads are excluded.

## Comparison with the current dev deployment

The initial read-only inspection on 16 October 2026 recorded these releases/owners.
`releases/dev-inventory.json` contains the sanitized comparison, with no raw
release values or Secret payloads.

| Existing release / namespace | Observed chart version / revision | Guidance |
| --- | --- | --- |
| `farmer-registry` / `farmer` | `0.0.0-rc.0`, revision 28 | Upgrade same release. Dashboard API belongs to it; retain its enabled state and authenticated configuration |
| `cropsown-registry` / `crop` | `0.0.0-develop`, revision 10 | Upgrade same release. Dashboard API belongs to it and uses the registry's DB Secret |
| `livestock-registry` / `livestock` | `1.2.0+bf78e69`, revision 12 | Select `1.0.0-dev.3` explicitly; independent chart numbering, not an application downgrade. Dashboard API currently absent |
| `commons-services` / `commons` | `2.3.4-rc.245`, revision 13 | Same owner for `cm-api`, `cm-partner-api`, `cm-ui` and expiry CronJob. Customized chart numbering is independent of upstream |
| `commons` / `commons` | `2.3.3`, revision 3 | Preserve; no Base upgrade included |
| `oan-dashboards` / `commons` | `0.1.0`, revision 1 | Shared dashboard remains independent |
| Farmer/Crop/Livestock connectors | `farmer-registry-connector`, `cropsown-connector`, `livestock-connector` | Keep independent owners; credentials chart also remains separate |
| DA | No DA release in inspected target namespace | Namespace remains unconfirmed; separate install preparation required |

The current defaults/examples use the confirmed canonical hosts:
`farmer-registry-development.oanstaging.com`, `crop-registry-development.oanstaging.com`
and `livestock-registry-development.oanstaging.com`. The initial redirect aliases
were replaced in `1.0.0-dev.2`; see [the complete URL map](dev-urls.md).
Reconcile private settings before use. Staging has
different namespaces (`far`, `crop`, `live`); do not reuse dev values.

An old `gen2/cropsown-registry/dashboard-ui` image exists but reads the database
directly and differs from the current IAM dashboard; it was not substituted.
The published `da-registry-frontend` is also a different app, not a backend or
dashboard substitute. Unavailable components received no guessed image tags.

The upstream DA overlay used `staffPortalUi`, while pinned platform templates
consume `staffUi`; that key was corrected with the workload disabled pending an
image. Automatic initialization components are disabled to avoid a partial
deployment. Names remain controlled by the original platform templates when
those components are deliberately enabled.

## Separate preparation before upgrades

Inspect current private values/rendered changes, confirm Secret keys, retain the
old chart/version and back up affected data. Platform changes, reporting/seed
Jobs, shared IAM changes and ownership transfers need separate preparation.
Commons Services updates a shared platform. Existing dashboards retain their
owners unless a separate migration is agreed. **Helm rollback does not reverse
database migrations, seed data or external IAM changes.** No rollout, migration
or ownership change was performed.

Version `1.0.0-dev.3` adds OAN display names and COSS source links; runtime values
are unchanged from `1.0.0-dev.2`. Local pair results and their limits are in
[the isolated check guide](consent-aggregation-local-check.md).
