# Operations runbook

Procedures that were checked against the repository, the Jenkins configuration or the live clusters on
5 and 6 November 2026. Where a step could not be checked it says "Not verified:".

Access used for the checks: SSH to `new-gen2-development` (New Dev) and `openg2p-gen2-staging` (staging), with
`sudo kubectl --kubeconfig /etc/rancher/rke2/rke2.yaml` and `sudo helm --kubeconfig /etc/rancher/rke2/rke2.yaml`.
On staging the `kubectl` binary is `/var/lib/rancher/rke2/bin/kubectl`. Read commands only were used for this
document. Never print the data of a Secret.

## 1. Check health

| Question | Command (add `-n <namespace>`) | Source of the command |
| --- | --- | --- |
| What is installed and in which state? | `helm list -A` (look for any status other than `deployed`) | live reading |
| What happened to a release? | `helm history <release> -n <namespace>` | `docs/rollback.md` |
| Which pods are unhealthy? | `kubectl get pods -A --no-headers \| grep -v -E "Running\|Completed"` | live reading |
| Which images run? | `kubectl -n <namespace> get deploy -o jsonpath` over `.spec.template.spec.containers[*].image` | live reading, [versions.md](versions.md) |
| Why did a pod not start? | `kubectl -n <namespace> describe pod <pod>` (events at the end) | live reading |
| Did the last pipeline run pass? | Jenkins job page, or the Jenkins API path `job/<folder>/job/<repo>/job/<branch>/lastBuild/consoleText` | Jenkins reading |

At the time of reading the unhealthy items were:

| Environment | Item | State |
| --- | --- | --- |
| Staging | Release `cropsown-registry` in `crop` | `failed`; three pods `ImagePullBackOff`; a seed job `cropsown-stg-db-seed` stuck in `Init:0/2` for 43 days |
| Staging | Job `da-registry-db-seed` in `da-registry` | `Init:1/2` for more than 30 minutes |
| Staging | Job `farmer-registry-fr-dashboards-qcqsb` in `farmer` | `Init:0/1` for more than 6 hours |
| New Dev | Job `commons-services-master-data-geo-seed-ci-43-8cbsb` in `commons` | `Error` |
| New Dev | Pod `oan-native-rehearsal-806d49558e1c-trm9m` in `farmer` | `Error`, 10 days old |

Smoke test of the public hosts: request the host list of [environments.md](environments.md), section 3.
Not verified: a standard smoke-test script. `docs/automated-staff-test.md` describes an automated staff
regression against New Dev only.

## 2. Deploy

Deploy by merging; do not run Helm by hand on the servers.

1. Merge the pull request into `develop` of the registry repository. Jenkins builds and upgrades the New Dev
   release ([delivery-pipeline.md](delivery-pipeline.md), section 2).
2. Check the build result and `helm history <release> -n <namespace>` on New Dev. The new revision must be
   `deployed`.
3. Open a pull request with head `develop` and base `staging`; merge it after review. Jenkins promotes the chart
   to staging.
4. Check `helm history` on staging.

For the dashboards and the Farmer connector on staging the deployment is a script run from a checkout of this
repository: `scripts/ci/deliver_staging_dashboards.sh` and `scripts/ci/deliver_staging_farmer_connector.sh`.
Not verified: who runs them and from where.

Commons services are upgraded from Rancher: choose the published chart version and press Upgrade
(`docs/commons-upgrades.md`). Back up the affected databases first (section 8).

Actions that drop data (`fresh-install`) are not part of a normal deploy. They are operator actions
([delivery-pipeline.md](delivery-pipeline.md), section 4, pending merge).

## 3. Roll back a release

Source: `docs/rollback.md`; the behavior of `scripts/ci/deliver_staging.sh`.

1. Read the history entries between the installed version and the target, especially the upgrade notes
   (`releases/history/<channel>/<chart>.md`, `CHANGELOG.md`).
2. Save the current state: `helm -n <namespace> history <release>` and
   `helm -n <namespace> get values <release> -o yaml` written to a private file (the values can hold secrets;
   do not commit or paste them).
3. Decide about data. A rollback does not undo database migrations, seed data, identity changes or Kafka messages.
   If a newer version changed the schema, restore the backup taken before the upgrade, or roll forward with a fix.
4. Roll back: `helm -n <namespace> rollback <release> <revision> --wait --timeout 15m`, or in Rancher: Apps,
   Installed Apps, the release, menu, Rollback. To a published version no longer in the history, use the command
   in its history entry; it uses `--reset-values` with the environment overlay.
5. Confirm the running digests equal the history entry, run the health checks, record the reason.
6. On a branch that deploys on merge, the next pipeline run deploys again. Revert or fix the commit on the
   registry branch first.

Automatic rollback: `deliver_staging.sh` rolls back to the last `deployed` or `superseded` revision when a
staging upgrade fails. On 5 November 2026 this worked for Development Agent (rolled back to revision 1, "Rollback
was a success") and did not work for Crop sown (section 5).

Dashboards on staging: each is its own release; use `helm rollback <release> -n <namespace>`. The Farmer
connector: `helm rollback farmer-registry-connector -n farmer`; leave `farmer-connector-credentials` in place
(`docs/rollback.md`).

## 4. A release that does not finish (timeout, failed, or pending)

Helm reports a release as `failed` when an upgrade or a rollback ends with an error, for example
`context deadline exceeded`. Helm reports `pending-upgrade` or `pending-rollback` when the operation was
interrupted before it finished. Not verified: any `pending-*` state on these clusters. In the history read on
5 November 2026 every unfinished operation ended as `failed`, not `pending-*`.

Diagnose in this order:

1. `helm history <release> -n <namespace>`: which revisions failed, with which chart.
2. `kubectl -n <namespace> get pods`: which pods wait and why (`ImagePullBackOff`, `Init`, `CrashLoopBackOff`).
3. `kubectl -n <namespace> describe pod <pod>`: the events at the end name the cause. Events expire after about an
   hour, so read them early.
4. `kubectl -n <namespace> get job`: a seed or hook job that never ends keeps a `--wait` upgrade waiting.
5. The Jenkins console text of the build: it prints the pod list at the failure and whether the rollback worked.

Do not delete the Helm release secrets and do not patch Deployments by hand without the owner's approval.
Not verified: a tested procedure to clear a `pending-*` state on these clusters.

## 5. What happened to Crop sown on staging (5 November 2026)

Facts from `helm history cropsown-registry -n crop` on staging, the Jenkins console of
`Gen2-Package/cropsown-regsitry` `staging` build 28 and the pod events:

| Time (UTC) | Revision | Chart | Result |
| --- | --- | --- | --- |
| 23 September 2026 | 14, 15 | `openg2p-farmer-registry-1.2.0` | revision 15 `deployed`: the last good state, an old chart from the earlier pipeline (images `gen2/cropsown-registry/*:staging-14`) |
| 15:28 | 16 | `openg2p-cropsown-registry-1.0.0-rc.486` | failed: `context deadline exceeded` |
| 15:58 | 17 | `openg2p-farmer-registry-1.2.0` | failed: the rollback to revision 15 also timed out |
| 17:35, 18:06 | 18, 19 | rc.486, then 1.2.0 | the same pair of failures |
| 19:16, 19:46 | 20, 21 | rc.486, then 1.2.0 | the same pair of failures; revision 21 is the current one, status `failed` |

What the evidence shows:

- Build 28 promoted the Crop sown chart to `1.0.0-rc.486` (images retagged `1.0.0-rc.486` and `staging`, same
  digests) and ran `helm upgrade`. The upgrade waited 30 minutes and failed with `context deadline exceeded`.
- The script then rolled back to revision 15. The rollback waited 15 minutes and failed too. Pods of the old chart
  (`staff-api`, `staff-ui`, `celery-beat-producer` with `...:staging-14`) are in `ImagePullBackOff`. The older pods
  from 17 days ago are still `Running`, so the old Crop sown keeps serving.
- The release uses the pull secret `cropsown-ecr` (created 23 September 2026), and the namespace `crop` has no
  pull-secret refresh job. Not verified: the lifetime of the ECR login token (it is commonly 12 hours); the secret creation date is the only fact read.

Not verified: the reason the rc.486 upgrade did not become ready. The pod events of that time had expired, and the
console shows only the failure. Not verified: why the `staging-14` images cannot be pulled (the events that carry
the message had expired). A missing or expired pull secret, or an image removed from ECR, are the candidates;
neither was checked because it needs the owner's approval to read the registry.

State at reading: the release is `failed` at revision 21, the registry still serves from the 17-day-old pods, and
the fix has not been applied. The fix needs these decisions, each by the owner: (1) a working pull secret in
`crop` (pull request 128 gives each release its own refreshed secret, see section 6), (2) a clean upgrade to
`1.0.0-rc.486` once images can be pulled, (3) removal of the stuck seed job `cropsown-stg-db-seed`. Do not retry
the pipeline before step 1: the same timeout will repeat and each attempt adds two `failed` revisions.

The same pattern applies to any registry: an upgrade that fails before pods become ready leaves the release in
`failed`, and an automatic rollback to a chart whose images cannot be pulled fails as well.

## 6. Pull secrets for the container registry (ECR)

Registry images are in the Amazon container registry account `379220350808`, region `ap-south-1`. A pull secret
holds a login token that expires, so it must be refreshed (Not verified: the exact lifetime).

| Where | Refresher found on 5 November 2026 |
| --- | --- |
| New Dev, namespaces `commons`, `farmer`, `livestock`, `crop`, `da-registry` | CronJob `ecr-pull-secret-refresh` in each |
| New Dev, dashboards | CronJobs `farmer-registry-dashboard-ecr-refresh`, `cropsown-registry-dashboard-ecr-refresh`, `livestock-registry-dashboard-ecr-refresh` |
| Staging, `live` | CronJob `ecr-secret-refresh`, schedule `0 */6 * * *`, image `amazon/aws-cli:2.17.62`; and `livestock-registry-dashboard-ecr-refresh` |
| Staging, `commons` | CronJob `oan-dashboards-ecr-refresh` |
| Staging, `farmer` | CronJob `farmer-registry-dashboard-ecr-refresh` only |
| Staging, `crop` and `da-registry` | none (`crop` holds the secrets `cropsown-ecr` and `ecr-pull-secret`) |

Source: `kubectl get cronjob -A`, `kubectl -n crop get secret` (names only).

Pull request 128 (open): each registry chart creates its own pull secret before the seed hooks run, and a CronJob
(default `0 */6 * * *`) refreshes it, using the node's cloud role. It is off unless `ecrPullSecret` is enabled;
the staging and New Dev values of Farmer, Crop sown, Livestock and Development Agent enable it. Until it is
merged and deployed, the per-release refresher does not exist.

Access rule: the node role `openg2p-dev-sandbox-dns` pulls the images. A new repository needs an added
read policy (`docs/ecr-pull-access.md` records the case of `oan/commons/aggregation-api`, which was denied until
a policy was added). Changing it needs an authorized AWS administrator.

## 7. Hostnames, certificates and routing

Path of a request: browser, host nginx, Istio ingress gateway, VirtualService, Service, pod
(`docs/request-flow.md`).

| Environment | Host nginx | Istio |
| --- | --- | --- |
| New Dev | `/etc/nginx/sites-enabled/oan-development-wildcard.conf` with `server_name development.oanstaging.com *.development.oanstaging.com`, plus a legacy compatibility file | Gateway `istio-system/development` for `*.development.oanstaging.com`; Gateway `istio-system/development-legacy` for the old names |
| Staging | one file per host in `/etc/nginx/sites-enabled/` (for example `farmer-registry-oanstaging.conf` with `server_name farmer-registry.oanstaging.com`) | Gateway `istio-system/staging` for `*.oanstaging.com`; some namespaces use their own gateway named `internal` |

Source: live reading of `/etc/nginx/sites-enabled`, `kubectl get gateway -A`.

Not verified: the wildcard nginx site for staging. The proposal is `environments/staging/ingress/nginx.conf`
(server name `oanstaging.com *.oanstaging.com`, certificate `wildcard.oanstaging.com`, proxy to `istio_ingress`
with `Host` forwarded). On 5 November 2026 no file under `/etc/nginx` on staging contained `*.oanstaging.com`.
Consequence: every new staging host needs its own nginx file until the wildcard site is installed and the wildcard
certificate is in place. Not verified: certificate paths, issuer and expiry dates (not read).

To add a host: create the VirtualService through the chart values (`docs/service-onboarding.md`), and on staging
add the nginx file; on New Dev nothing else is needed because the wildcard covers it.

## 8. Logs

Source: `docs/logging.md`; `helm list -A`.

- Path: container output, then the OpenTelemetry agent on each node, then the OpenTelemetry gateway, then Loki
  (object store MinIO), then Grafana, "Explore".
- New Dev: Grafana at `logs.development.oanstaging.com` (VirtualService `grafana-logs`).
- Staging: Loki and the OpenTelemetry releases exist; there is no Grafana release, so there is no viewer.
  Read container logs with `kubectl -n <namespace> logs <pod>`.
- Retention in `docs/logging.md` is 14 days (`limits_config.retention_period: 336h`).
- Mismatch to be aware of: `docs/logging.md` says it names chart versions Loki 7.5.0 and OpenTelemetry 0.177.0 and
  that "nothing here has been installed". The clusters run Loki 6.24.0 and OpenTelemetry collector 0.111.0 (live
  reading). Treat the file as a design, not as a record of what runs.
- The audit manager keeps its own audit records (`auditmanager.<host>`). Not verified: what it stores for the
  registries.

## 9. Backups before data changes

Rule from `docs/rollback.md` and `docs/commons-upgrades.md`: a rollback restores manifests only. Back up before
any change that touches a database.

1. Databases live in `commons-postgresql-0` in the namespace `commons`. Names seen on New Dev include
   `farmer_registry`, `cropsown_registry`, `livestock_registry`, `da_registry`, `partner_management`,
   `master_data`, `awe`, `keycloak`, `consent_manager`, `farmer_connector_v2`, `cropsown_connector`,
   `livestock_connector_livestock`, `odkdb` (live reading of `pg_database`).
2. Dump the affected databases with `pg_dump` (`docs/commons-upgrades.md`, "Back up the databases first").
   Not verified: a tested dump procedure with sizes and target path.
3. Keep `helm get values` of the release in a private file (never in Git).
4. The operator action `fresh-install` backs up the registry databases before it drops them (description in the
   Farmer `dev.groovy` parameter text); it is pending merge as an operator-only pipeline.
5. Several test databases exist on New Dev (`oan_rehearsal_*`, `oan_preserve_*`). Not verified: whether they are
   safe to delete.

## 10. Known risks to keep in view

| Risk | Evidence |
| --- | --- |
| No branch protection; a red pull request can merge | [delivery-pipeline.md](delivery-pipeline.md), section 5 |
| A failed automatic rollback leaves the release `failed` | section 5 |
| Staging has no wildcard nginx site and no Grafana | sections 7 and 8 |
| Connectors on staging (Crop sown, Livestock) are old images | [versions.md](versions.md) |
| Image pulls depend on expiring tokens refreshed by per-namespace jobs, absent in some staging namespaces | section 6 |
