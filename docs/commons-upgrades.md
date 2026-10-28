# Upgrading Commons Services from Rancher

A Commons Services upgrade is one action in Rancher: choose the published version
and click **Upgrade**. Nothing else sits between the merged chart and the cluster:

- no Helm CLI, post-renderer or `--no-hooks`;
- no hand-patched resources or hand-run Keycloak/database commands;
- no edits to the saved values, which hold only private literals.

Every setting comes from a reviewed pull request, and every Job and hook in the
chart is safe to run on every upgrade. CI enforces both.

## The OpenG2P standard this follows

OpenG2P's charts and documentation define how initialization works. These
behaviours, not hand-written exceptions, are what make repeated upgrades safe:

| Rule | Source |
| --- | --- |
| Database setup (`postgres-init`) is a regular Job, not a hook. A hook would run before PostgreSQL exists (pre-upgrade) or deadlock behind `--wait` (post-upgrade). | `postgres-init` 1.2.0 changelog and `values.yaml` |
| `postgres-init` is idempotent: an existing database and user are left alone, and since 1.2.0 the user's password is re-synced to its Secret on every run. Password Secrets are created once (`lookup`) and kept. | [Postgres Init Helm Chart](https://docs.openg2p.org/operations/deployment/deployment-guide/postgres-init-helm-chart) |
| `keycloak-init` is idempotent: existing realms, clients, roles, secrets and users are not modified. | [Keycloak Init Automation](https://docs.openg2p.org/operations/deployment/deployment-guide/keycloak/keycloak-init-automation) |
| Client secrets are generated on first install and reused on upgrades. | [AWE deployment](https://docs.openg2p.org/platform/platform-services/approval-workflow-engine/deployment) |
| Init Jobs delete themselves after finishing (`ttlSecondsAfterFinished`), so each upgrade creates them again and they re-check their state. | `postgres-init`, `keycloak-init` charts |
| Inside the Commons umbrella, IAM registration runs as a regular Job named with the release revision, so one failing hook cannot leave an application unregistered. | OpenG2P `openg2p-commons-services` `values.yaml` (`iamRegister.runAsHook: false`) |
| Hooks use `before-hook-creation`, so a new run replaces the previous Job. | All OpenG2P charts |
| The Rancher UI is the recommended way to deploy; pin immutable versions. | [Registry deployment](https://docs.openg2p.org/products/registry/registry/deployment), [versioning](https://docs.openg2p.org/operations/deployment/helm-docker-versioning-and-ci) |

## What runs on each upgrade

| Job | Kind | Why it is safe to repeat |
| --- | --- | --- |
| `*-pg-init-*`, `postgres-init-master-data` | Regular, expires after 100 s | Skips an existing database and user; re-syncs the password from the kept Secret |
| `*-kc-init-1-<hash>`, `keycloak-init-1-<hash>` | Regular, expires after 600 s / 1 day | Skips existing realms, clients and roles; a configuration change changes the hash, giving a new Job |
| `client-secrets-sync-<revision>` | Regular, expires after 600 s | Copies the unchanged client secrets from Keycloak into the same Secrets, then restarts their consumers |
| `kc-sa-role-<revision>` | Regular, expires after 600 s | Grants the PM service-account role; granting an existing role is a no-op |
| `master-data-iam-register-<revision>` | Regular, expires after 600 s | Posts the same application, roles and permissions to IAM |
| `esignet-schema-init-<hash>`, `mock-identity-system-schema-init-<hash>` | Regular, expires after 600 s | Skips when the schema already has tables (see below) |
| `websub-topics-<revision>` | Regular | Creates missing Kafka topics only |
| `auditmanager-topic-init` | Pre-upgrade hook | `--create --if-not-exists`; only ever grows partitions |
| `db-password-sync` | Pre-upgrade hook | Sets the PM role's password to its Secret; no-op when absent |
| `openg2p-awe-iam-register-<revision>`, `partner-management-iam-register-<revision>` | Post-upgrade hooks | Same registration as Master Data. These subchart versions cannot yet run it as a regular Job. |
| `mock-identity-system-identity-seed` | Post-upgrade hook | Looks each identity up and creates only missing ones |
| `cm-sanity` | Post-upgrade hook | Read-only smoke test (`SANITY_RUN_E2E=false`). It is the upgrade's acceptance gate: a failure marks the release failed. |

Keymanager's database setup and key generation run as init containers guarded by a
marker on its persistent volume, so they run once.

### The MOSIP exception

The eSignet and mock-identity schema Jobs use MOSIP's `postgres-init.sh`. Its
`deploy.sh` starts by terminating connections and running `DROP DATABASE` and
`DROP ROLE`. Re-running it unguarded deletes eSignet's key aliases and the mock
identities. This was reproduced against a scratch PostgreSQL: a marker row survived
the guarded re-run and was gone after the unguarded one.

`templates/esignet-mock-schema-init.yaml` therefore checks the schema first. When
the database exists and the schema has tables, the Job logs
`... already has N tables; skipping (deploy.sh drops the database).` and exits.
Only a missing or empty schema is created. To rebuild one deliberately, drop its
database by hand first. That is a reviewed recovery action, never part of an upgrade.

### What CI checks

`scripts/validate.py` renders the chart and fails when:

- a hook lacks `before-hook-creation`;
- a regular Job neither expires nor carries the release revision in its name, which
  would make a later upgrade patch an immutable Job;
- a MOSIP `postgres-init.sh` Job lacks the skip guard.

## Before you click

These hold once and stay true; check them when something changed:

1. **Saved values hold only private literals.** For Commons in dev these are the four
   listed in [rancher-dev.md](rancher-dev.md#commons-services-chart-defaults-are-the-dev-configuration).
   Anything else in Rancher's saved values overrides the chart and must be moved into
   a pull request instead. Rancher also stores the values in the same 1 MiB Secret as
   the chart, so extra values can make the upgrade fail with `Too long`.
2. **Namespace Secrets exist:** `commons-postgresql`, `commons-keycloak`, the database
   user Secrets and the image pull Secrets. A missing one shows as
   `CreateContainerConfigError` on the init pods; Rancher does not pre-check them.
3. **The target version is published.** Merged pull requests are released by the
   workflow in [versioning.md](versioning.md); refresh the repository in Rancher.
4. **The CHANGELOG between the installed and target versions names no manual step.**
   A release that needs one is not a one-click release and must say so.

Back up the databases first (`pg_dump` of the affected databases) when the
CHANGELOG mentions a migration. A rollback does not undo migrations.

## Upgrade

1. Rancher → **Apps → Repositories** → `oan` → ⋮ → **Refresh**.
2. **Apps → Installed Apps** → `commons/commons-services` → ⋮ → **Upgrade**.
3. Choose the exact target version. Leave the values unchanged.
4. Under **Helm options**, set **Timeout** to `900` seconds and keep **Wait** on.
   First starts of Keycloak-dependent services exceed Rancher's default of 600.
5. Click **Upgrade** and follow the `helm-operation` log until it reports success.

## Verify

- **Installed Apps** shows `Deployed` at the target version.
- **Workloads → Jobs:** every Job completed. A schema-init log shows `skipping`.
- **Workloads → Deployments:** all ready; no pod in `CrashLoopBackOff`.
- The `cm-sanity` hook passed, since the operation reported success.
- Sign in to the staff portal; open Master Data, Partner Management and Consent.

## Roll back

**Installed Apps** → `commons-services` → ⋮ → **Rollback** to the previous revision.
Rollback restores manifests only. Restore database changes from the backup.

## Known limit: new Keycloak roles or redirects

`keycloak-init` creates a client with everything declared for it, but does not add
roles, redirect URIs or other settings to a client that already exists. A chart
version that adds a role to an existing client (as Master Data `develop.118` did with
`MASTER_DATA_APPROVER`) needs that role created once in Keycloak. Its CHANGELOG entry
must say so, and the release is then not one-click. Closing this gap belongs in our
chart (a reconciling Job), not in OpenG2P's.

## One-time step: the first one-click upgrade from a CLI-installed release

From `1.0.0-dev.24`, Master Data's IAM registration runs as a regular Job
(`iamRegister.runAsHook: false`), so its payload ConfigMap
`commons-services-master-data-iam-register-payload` is a release resource.
A release installed earlier, or upgraded with `--no-hooks` (dev revision 26),
still holds that ConfigMap as a leftover hook resource without Helm's ownership
annotations. The first upgrade to `1.0.0-dev.24` or later, from Rancher or the
CLI, then stops before changing anything:

```text
ConfigMap "commons-services-master-data-iam-register-payload" in namespace "commons"
exists and cannot be imported into the current release: invalid ownership metadata
```

Adopt it into the release once, then upgrade as above. The ConfigMap only holds
the catalog the registration Job posts, and the upgrade rewrites its contents:

```sh
kubectl -n commons annotate configmap commons-services-master-data-iam-register-payload \
  meta.helm.sh/release-name=commons-services meta.helm.sh/release-namespace=commons --overwrite
kubectl -n commons annotate configmap commons-services-master-data-iam-register-payload \
  helm.sh/hook- helm.sh/hook-delete-policy- helm.sh/hook-weight-
```

A server-side dry run of the upgrade (`helm upgrade --dry-run=server ...`) names
every resource it cannot import; run it first to confirm this is the only one.
The other `*-iam-register-payload` ConfigMaps (AWE, Partner Management) are still
hooks in these versions and need nothing. `commons-services-masterdata-iam-register-payload`
belongs to an older chart, is no longer rendered, and is left alone.

## Releases still on older charts

Charts before this version do not carry their whole dev configuration and cannot be
upgraded natively. Their recorded procedures (`--no-hooks`, the dev post-renderer
with `--skip-initialization-jobs`) apply only to them. See [dev-urls.md](dev-urls.md)
and [rancher-consent-aggregation-status.md](rancher-consent-aggregation-status.md).
