# OAN Messaging on New Dev

`addons/oan-messaging` is one Helm release (`oan-messaging`, namespace `commons`) holding the messaging
service, its database, the staff console and the console's staff-portal integration. It is separate from the
`commons-services` release, so installing or upgrading it never touches Commons. No cache and no queue.

| Part | What |
| --- | --- |
| Service | Vendored subchart `charts/oan-messaging-service` (see its `VENDORED.md`): API, worker, receipt ingress, cleanup and statistics jobs, migration hook. Image `eoan/oan_messaging_service/oan-messaging` |
| Database | Role `oan_msg_owner` (migrations), role `oan_msg_runtime` (least privilege, `grants.sql`) and database `oan_messaging` on the shared `commons-postgresql`, made by the `db-init` hook with the existing superuser Secret. Passwords are generated once into Secret `oan-messaging-database` |
| 8028 | New Dev cannot reach 8028. `fake8028.enabled` runs the service repository's fake gateway (mTLS send endpoint, delivery callbacks) with a throwaway CA. Turn it off and supply the real Secrets where the real gateway is used |
| Console | `oan_messaging_ui` image `eoan/oan_messaging_ui/oan-messaging-ui` at `https://messaging.development.oanstaging.com`. Its server holds the reader token; browsers never see it |
| Reader token | Caller `staff-console`, created with `caller --messages-reader` (no channels, cannot send), token kept in Secret `oan-messaging-ui-reader` |
| Staff portal | Keycloak client `oan-messaging-ui`, client role `Messaging Viewer`, tile "OAN Messaging" registered with IAM, exactly as the registry dashboards do (`iam/keycloak-setup.mjs`, `iam/register.mjs`) |
| Access | `ui.grantUsers`: `admin`, `alex.carter`, `nina.patel`. The setup Job adds the role to those users and removes nothing; nobody else is granted |

## Hooks

Pre-install/pre-upgrade, by weight: init-secrets (-20), db-init (-15), migration (0), grants (3), callers
(8). Post: iam-setup (5), ui-smoke (10). Do not install with `--wait`: the hooks must run first.

## Delivery (no hand-run Helm)

1. A merge to `develop` of `oan_messaging_service` or `oan_messaging_ui` starts that repository's Jenkins job
   (`oan-messaging-service`, `oan-messaging-ui`). It tests, builds and pushes the image to ECR.
2. The same build then opens a pull request into this repository, from a branch on the pipeline account's fork
   (`bot/oan-messaging-<service|ui>-<tag>`), that changes only the image `tag:` line in
   `environments/dev/values/oan-messaging.yaml` to `<version>-develop.<build>@sha256:<digest>`. An older open pin PR
   for the same image is closed.
3. Merging that PR into oan-helm starts `oan-helm-dev-commons`, whose last stage `Deliver OAN Messaging` runs
   `scripts/ci/deliver_dev_oan_messaging.sh`: server-side dry run, then `helm upgrade --install --reset-values
   --atomic --wait`, then the record in ConfigMap `oan-messaging-delivery`. Unchanged chart and values: nothing runs.

## Manual install or upgrade (recovery only)

```sh
helm upgrade --install oan-messaging addons/oan-messaging -n commons \
  -f environments/dev/values/oan-messaging.yaml          # set the two image tags first
```

Dry-run first: `helm upgrade --install ... --dry-run=server`. Rollback does not reverse database migrations.

## Test send

The `console-smoke` caller (sms, purpose `transactional`) exists for test sends on New Dev; its token is in
Secret `oan-messaging-smoke-sender`. Send from inside the cluster to `http://oan-messaging-api`
(`POST /api/v1/messages/sms`, header `Idempotency-Key`). The fake gateway answers and calls back; the console
then shows the message and its callbacks.
