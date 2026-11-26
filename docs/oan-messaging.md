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
2. The same build then pins the image in this repository: one commit by `oan-image-pinner`, made through the GitHub
   API with the credential `oan-helm-fork-token`, that changes only the image `tag:` line in
   `environments/dev/values/oan-messaging.yaml` to `<version>-develop.<build>@sha256:<digest>` (the same exception the
   chart publisher and the seed pinner have; human and agent changes still go fork, pull request, review).
3. That commit starts `oan-helm-dev-commons`, whose last stage `Deliver OAN Messaging` runs
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

## Staging (qa.oanstaging.com)

Staging runs the same release, delivered by `oan-helm-staging-commons` (last stage `Deliver OAN Messaging`,
`scripts/ci/deliver_staging_oan_messaging.sh`, record ConfigMap `oan-messaging-delivery`) with
`environments/staging/values/oan-messaging.yaml`. Nothing is rebuilt: the image pins there are the digests New Dev runs,
and are moved by pull request after New Dev is verified. Console: `https://messaging.qa.oanstaging.com`, open to the same
three users (they exist in the staging `staff` realm). The release still uses the fake 8028 gateway.

**Before the console is reachable:** `*.qa.oanstaging.com` resolves to the APISIX gateway (13.127.77.101), which has one
route per host and answers any host without a route with `404` (`Server: APISIX`). The new host
`messaging.qa.oanstaging.com` needs a route to the staging Istio gateway like the existing QA hosts have. APISIX is
managed outside this repository.
