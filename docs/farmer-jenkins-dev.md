# Farmer dev deployment profile

[The public profile](../environments/dev/farmer-jenkins.json) approves only
`farmer-registry` in namespace `farmer`, chart `1.0.0-dev.5`, platform
`1.2.2-rc.544`. Download the archive directly from the COSS `main/repository/`
URL in that profile. Verify SHA256 before parsing it; verify the parent
dependency and the packaged child version too. Use that same archive for lint,
server render and upgrade. Do not rebuild dependencies, resolve a moving index,
use a fork, or fall back to Farmer's local chart.

Farmer Jenkins owns application builds. Each build publishes and verifies six
ECR component digests: staff-api, staff-ui, partner-api, celery, db-seed and
sanity-tests. Both Celery workloads use the celery digest; seed, sanity and
analytics workloads use the corresponding build digests. Optional components
retain their installed images. No Helm PR or package bump is needed for an
application-only build. A different approved pin requires a reviewed profile
change in both repositories; template/dependency changes require an OAN release.

## First cutover

Keep the existing Helm release, namespace, ownership, selectors, Services,
PVCs, routes, credentials, dashboard configuration and images. Commons and
connectors remain separate releases. Staging keeps its application-local chart,
namespace `far`, credentials, rehearsal gates and migration controls.

After both implementation PRs merge, use Farmer's
`ci/deploy/cutover-dev.sh` on the trusted VPN Jenkins agent. Do not merge those
PRs automatically. The first upgrade must keep installed application images.
Normal dev builds refuse to upgrade until the approved OAN chart is installed.

1. Pause normal Farmer dev deployment scheduling. Privately back up the release,
   saved values, manifests, hooks, registry DB and connector DB; verify checksums
   and restoration. Preserve the current connector settings and checkpoints.
2. Create fresh private evidence as described in Farmer's
   `docs/oan-dev-chart.md`. Review the exact completed Job records removed from
   Helm tracking. An active or unfinished affected Job blocks the cutover.
3. Download and verify the approved package, reconcile installed literals and
   Secret references through supported values, lint and render with cluster
   lookups. Compare named environments in application and init containers.
4. Cutover suppresses all hooks with `--no-hooks` and removes all ordinary Jobs
   through a post-renderer, so TTL cleanup cannot cause initialization, IAM,
   seeding or reporting import to replay. It retains persistent configuration
   resources. Only the `helm.sh/chart` metadata label may differ. Stop if the
   package cannot represent installed configuration; do not weaken preservation.
5. Immediately recheck backup evidence, release revision and affected Jobs.
   Upgrade the same archive, verify the live chart version and manifest, and
   archive only sanitized chart/image/revision results in Jenkins.
6. Complete canonical and legacy URL, staff login, API and dashboard health
   checks. Confirm unchanged connector settings/checkpoints, then submit one
   marked synthetic Farmer record through ingestion, authorized approval and
   register promotion. Do not replay historical submissions. Enable normal
   builds only after this acceptance passes.

Normal builds retain schema, seed, provenance and readiness gates. Migrations
remain explicit and separately recoverable. Helm rollback cannot restore a DB;
never automatically roll back across an unreviewed migration.

## Current compatibility blocker

A read-only server render of this exact public archive against Farmer dev
revision **39**, inspected on **2026-10-21**, was rejected by the metadata-only
guard. The chart adds environment defaults in four API/Celery workloads,
including their postgres-checker init containers. Its reporting refresh CronJob
also changes an embedded command's Unicode em-dash encoding. There is no public
values field to replace that command. Saved values and exact installed image
pins alone therefore do not establish a safe metadata-only cutover.

No upgrade was performed. This profile documents the requested pin, but is not
evidence that live cutover is ready. Resolve this incompatibility through a
reviewed decision before merging/enabling the Farmer integration; the current
plan disallows both chart-source changes and nonmetadata cutover differences.
Do not use the pending dev.6 package as an implicit replacement.
