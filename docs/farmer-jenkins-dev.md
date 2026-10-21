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
3. First run Farmer's `ci/deploy/cutover-dev.sh --rehearse` for read-only
   preflight without a backup assertion. Download and verify the approved package, reconcile installed literals and
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

## Verified compatibility, 2026-10-21

A corrected read-only server rehearsal of this exact public archive against
Farmer dev revision **39** passes metadata-only preservation of all **32**
persistent resources and installed images. Helm reintroduces some nulled
environment defaults during parent/child values coalescing. Farmer's reviewed
deployment adapter removes only a fixed allowlist of those defaults when both
prepared environment maps explicitly suppress the name. It applies to app/init
containers during both dev rendering and upgrade; unknown changes remain
rejected by the independent preservation guard. It does not alter commands,
images, routes, credentials or chart sources/packages.

The initially reported command-encoding mismatch came from Windows subprocess
decoding in the rehearsal tool. With explicit UTF-8 decoding, the reporting
refresh command matches exactly. No command rewrite or guard exception is used.

No upgrade was performed. The production rehearsal shell passed using a
host-Python container adapter because the dev host lacks Docker; CI separately
verifies container helpers. Backup recovery and live operational acceptance
remain required. Merge the OAN profile first, pause automatic Farmer dev deploys,
then merge Farmer, perform the backup-gated chart-only cutover, complete
acceptance and resume normal builds. Dev.5 remains pinned independently of
newer packages on `main`.
