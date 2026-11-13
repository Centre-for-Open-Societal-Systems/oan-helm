# Rotating the Commons Postgres superuser password

The Commons Postgres superuser (role `postgres`) password lives in Secret `commons/commons-postgresql`, key
`postgres-password`. The Bitnami chart in release `commons` generated it on first install and keeps it by looking the
Secret up on every upgrade (`postgresql.auth.postgresPassword` is empty in the saved values). No values file and no
Jenkins credential holds it.

Changing that Secret alone does not change the password: Bitnami runs `ALTER ROLE postgres` only on first boot, with an
empty data directory. Every consumer would then be locked out. The upstream `db-password-sync` hook signs in as the
superuser and resets only the PM role, so it cannot rotate the superuser either.

Rotation is therefore its own OAN chart, `addons/commons-postgres-superuser-rotation`, delivered by Jenkins. Nobody
types, copies or sees the new password.

## How to rotate

1. Set a new `rotation.id` in `environments/<env>/values/commons-postgres-superuser-rotation.yaml` (for example
   `2026-12-01-1`) and say why in the comment above it. Open a pull request. Merge it once it is green.
2. The staging Commons job (`ci/jenkins/staging-commons.Jenkinsfile`, stage "Rotate Commons Postgres superuser") runs
   `scripts/ci/deliver_staging_commons_postgres_superuser_rotation.sh`, between the Commons base release and Commons
   services.
3. Read the build log. The Job prints, and only prints:
   - `generated the new password ...` (or `resuming ...`)
   - `ALTER ROLE postgres done`
   - `check: new password accepted`, `check: old password refused`
   - `wrote commons/commons-postgresql` and one `wrote copy <ns>/commons-postgresql` per namespace
   - `recorded rotation <id>`, then the restarts
4. Prove the platform still works: every registry staff API and partner API answers, and one Farmer change event
   reaches Crop and Livestock.

Redelivering the same id does nothing: ConfigMap `commons/commons-postgres-superuser-rotation-record` holds the last
done id.

## What the Job does

| Step | Image | Does |
| --- | --- | --- |
| `prepare` | alpine/k8s | Stops if the id is already done. Otherwise generates 32 random `[A-Za-z0-9]` characters, or reuses the ones an earlier failed run kept, and stores them in Secret `commons-postgres-superuser-rotation-pending` **before** anything changes |
| `apply` | openg2p/postgresql | Signs in with the current Secret value, turns statement logging and pgaudit off for its session, runs `ALTER ROLE postgres PASSWORD ...` (through stdin, never an argument), then checks that the new password signs in and the old one is refused |
| `publish` | alpine/k8s | Writes the new value to `commons/commons-postgresql` and to each namespace in `copyTo`, removes the kubectl `last-applied-configuration` annotation (it held the old value) and the false Helm annotations on copies, records the id, deletes the pending Secret, restarts `restart.deployments` and `restart.statefulsets` |

The password passes between the steps on an in-memory volume only.

## Failure and resume

- Fails in `prepare` or before `ALTER ROLE`: nothing changed. Fix the cause and rerun the build.
- Fails after `ALTER ROLE`: the database already has the new password and the Secret still has the old one, so
  consumers that open new connections fail until the rerun. Rerun the build at once. The Job finds the pending
  password already active and only checks and publishes.
- `Secret ...-pending belongs to rotation X`: an earlier rotation never finished. Rerun with that id first.

Helm's `--atomic` rolls back the release objects, never the database. The pending Secret is what makes a rerun safe.
Do not delete it by hand while a rotation is unfinished.

## Who reads the password

Checked on staging on 13 Nov 2026 with a `secretKeyRef` scan of every Deployment, StatefulSet, Job and CronJob:

| Consumer | Reads it | After a rotation |
| --- | --- | --- |
| `commons/commons-postgresql` (StatefulSet) | `POSTGRES_PASSWORD`, at first boot only | Nothing needed; restart only for tidiness (all registries lose connections for about a minute) |
| `commons/commons-services-keymanager` | init container `postgres-init`, at pod start | Restarted by the Job |
| `commons/commons-services-db-password-sync` | pre-upgrade hook of commons-services | Reads the new value on its next run |
| `farmer/farmer-registry-registrant-auth` | the `farmer` copy, when the Farmer chart is delivered | Copy updated by the Job |
| registry-connector `postgres-init` | the copy in its namespace | Copy updated by the Job |

The copies in `crop`, `live`, `farmer` and `da-registry` were made by hand with kubectl. The Job keeps them in step
from now on. Its rights there come from `environments/staging/rbac/commons-postgres-superuser-copies-rbac.yaml`
(get and patch on that one Secret), applied once by the cluster admin like the Commons deployer's RBAC.

Helm release records of `commons` keep the rendered Secret of each revision, so older revisions still contain the old
value. That value no longer signs in.
