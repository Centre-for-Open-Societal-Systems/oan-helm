# Rolling back a chart

Use this for any chart published to `repository/develop`, `staging` or `release`.

## Find the version

| Question | Where |
| --- | --- |
| What is the latest version per channel? | `releases/channels-current.yaml` |
| What changed, when, from which commit? | `CHANGELOG.md` |
| Which images does a version pin, and how do I return to it? | `releases/history/<channel>/<chart>.md` |
| What is installed? | `helm -n <namespace> history <release>` |

Each history entry has the source commit, a compare link to the previous version, image digests, upgrade
notes when there are any, and the exact command that returns to that version.

## Before rolling back

1. Read the history entries between the installed version and the target, especially **Upgrade notes**.
2. Record the current state:
   ```sh
   helm -n <namespace> history <release>
   helm -n <namespace> get values <release> -o yaml > /private/<release>-values.yaml
   ```
3. Decide whether the data must go back too. **A rollback does not undo database migrations, seed data,
   IAM changes or Kafka messages.** If a newer version migrated the schema, restore the backup taken
   before that upgrade, or roll forward with a fix.

## Roll back

Fastest, when the target is a recent Helm revision of the same release:

```sh
helm -n <namespace> rollback <release> <revision> --wait --timeout 15m
```

Or in Rancher: Apps, Installed Apps, the release, the menu, Rollback.

To any published version, including one no longer in the Helm history, run the command from its history
entry. It uses `--reset-values` with the environment overlay, so saved values cannot keep a newer image.

Published versions are never replaced or removed, and ECR keeps every image a published `staging` or
`release` chart references, so the target stays installable.

## After rolling back

1. Confirm the running digests match the history entry:
   ```sh
   kubectl -n <namespace> get pods -o jsonpath='{range .items[*]}{.status.containerStatuses[*].imageID}{"\n"}{end}' | sort -u
   ```
2. Run the application health checks and a smoke test.
3. Record the rollback and its reason in the Jira ticket.
4. On a hands-free channel, the next pipeline run deploys again. Fix or revert the commit on the registry
   branch first, or hold the pipeline.
