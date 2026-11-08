# Delivery pipeline

How a change becomes a running release. Facts as of 5 November 2026.

Sources: `Jenkinsfile`, `ci/pipelines/dev.groovy` and `ci/pipelines/staging.groovy` of each registry at
`origin/develop`; `docs/chart-channels.md`, `docs/versioning.md`, `scripts/ci/deliver_staging.sh` and
`.github/workflows/` of this repository at `main` commit `7db1f6a`; Jenkins job configuration and console text;
`gh pr view` for the open pull requests; `gh api` for branch protection.

## 1. The two branches

| Branch of a registry repository | Target | What a build does |
| --- | --- | --- |
| `develop` | New Dev | Tests, builds the images, pushes them to the Amazon container registry (ECR), packages the chart with those images, upgrades the New Dev release, publishes the chart to `repository/develop/` of this repository |
| `staging` | staging | Builds nothing. Promotes the chart `develop` already built from the same source tree (same image digests, new release-candidate tag), upgrades the staging release, publishes the chart to `repository/staging/` |

Staging is reached only by a pull request from `develop` into `staging` (head `develop`, base `staging`). The
promotion fails if `develop` never built that exact source tree. Anything for staging therefore passes New Dev
first. Environment settings are not in the source tree; they are in `environments/staging/values/` of this
repository.

Source: `docs/chart-channels.md` (Promotion), `scripts/ci/deliver_staging.sh`, `ci/pipelines/staging.groovy`.

## 2. Flow for one registry change

| Step | Where | What happens |
| --- | --- | --- |
| 1 | GitHub, registry repository | A pull request is merged into `develop`. The pull request build only validates; it does not publish or deploy |
| 2 | Jenkins job of the repository | The `develop` build runs: Test, Build, Publish (images to ECR), Package chart, Deploy to New Dev, Publish chart |
| 3 | Helm on New Dev | `helm upgrade` of the release with the packaged chart. If the upgrade fails, Helm returns to the previous revision |
| 4 | This repository | The publish step adds one archive to `repository/develop/`. After the push to `main`, the workflow `publish-channels.yaml` seals it in `releases/channels.json`, rebuilds `index.yaml` and `SHA256SUMS`, writes `releases/history/develop/<chart>.md`, adds a `CHANGELOG.md` entry and tags `<chart>-<version>` |
| 5 | GitHub | After New Dev is verified, a pull request from `develop` into `staging` is opened and merged |
| 6 | Jenkins job, `staging` branch | `scripts/ci/deliver_staging.sh` runs `promote_chart.py`, then `helm upgrade --install --reset-values` with only the staging values file, then `publish_chart.py` |
| 7 | Helm on staging | If the upgrade fails and an earlier revision was deployed, the script runs `helm rollback` to the last deployed or superseded revision. Nothing is published after a failure |

The staging upgrade waits up to 30 minutes (`HELM_TIMEOUT`, default `30m`) and the rollback up to 15 minutes.

The `develop` build of Farmer also builds, and upgrades, the optional services (dashboards and connector)
unless told not to. The Crop sown build also builds the dashboard API and dashboard user interface.

Image-pin pull requests: bot-opened pull requests with names like "Livestock registry images 0bba361834eb"
are open in this repository (numbers 64 to 95 at the time of reading). Not verified: whether these pins are
still required now that the chart is packaged with the build's own images.

## 3. Chart channels in this repository

| Registry ref | Chart version | Published to |
| --- | --- | --- |
| `develop` | `0.0.0-develop.<n>` | `repository/develop/` |
| `staging` | `<line>.<next>-rc.<n>` | `repository/staging/` |
| tag `N.N.N` | `N.N.N` | `repository/release/` (the `release` branch does not exist yet) |

`<n>` is the commit count of the registry branch. A published version is never replaced. Each channel folder
is its own Helm repository. Latest per channel on `main`: develop has Crop sown 0.0.0-develop.488, Development
Agent develop.83, Farmer develop.803, Livestock develop.426; staging has Development Agent 1.0.0-rc.84,
Farmer 1.0.0-rc.813, Livestock 1.0.0-rc.432; release is empty (`releases/channels-current.yaml`).

Commons services is not in this flow. Its chart source is in `charts/` and is released by
`.github/workflows/release.yaml` on every push to `main` that touches `charts/` (see `docs/versioning.md`).

The pipelines publish as the `oan-ci-integration` GitHub App (Jenkins credential `oan-ci-app`); a pipeline that has not
moved yet still uses `oan-helm-fork-token`, the token of a maintainer account.
`main` has no ruleset, so the rule that this account may only add new archives is checked after the push
(`docs/chart-channels.md`, Publishing credential).

## 4. The no-click rule

Rule: nobody presses "Build with Parameters" and nobody clicks a manual deploy. A merge to `develop` or
`staging` builds and deploys by itself.

State on the default branches today:

| Pipeline | Parameters still defined | Source |
| --- | --- | --- |
| Farmer `develop` | `DELIVERY_ACTION` (deploy, fresh-install), `COORDINATE_SERVICES`, `APPLY_COMMONS_IDENTITY` | `ci/pipelines/dev.groovy` |
| Farmer `staging` | `DELIVERY_ACTION` (promote, validate-only, fresh-install, deploy), `DEPLOY_STAGING`, `COORDINATE_SERVICES` | `ci/pipelines/staging.groovy` |
| Crop sown `develop` | `NEW_DEV_DELIVERY_ACTION`, `CONNECTOR_IMAGE_TAG` | `ci/pipelines/dev.groovy` |
| Livestock `develop` | `NEW_DEV_DELIVERY_ACTION` | `ci/pipelines/dev.groovy` |
| Crop sown, Livestock, Development Agent `staging` | `DEPLOY_STAGING` | `ci/pipelines/staging.groovy` |

All the latest staging builds read in Jenkins were started by the user `admin`, not by a merge
(see [environments.md](environments.md), section 4).

### Pending merge: the operator pipeline

Three open pull requests remove the parameters from the merge pipelines and move the manual actions into a
separate pipeline that only the user `admin` can run:

| Repository | Pull request | State on 5 November 2026 |
| --- | --- | --- |
| `farmer-registry` | 235 | open, pending merge |
| `cropsown-regsitry` | 242 | open, pending merge |
| `livestock-registry` | 203 | open, pending merge |

Everything in the rest of this section is pending merge and is not on any default branch yet. It is read from
the description of pull request 235 (`gh pr view 235 --repo Centre-for-Open-Societal-Systems/farmer-registry`).

- A merge to `develop` or `staging` takes the default path: for `develop`, build, publish, deploy and (Farmer)
  coordinate services; for `staging`, promote.
- The file `Jenkinsfile.operator` declares `OPERATOR_ACTION`, waits for an approval limited to the user
  `admin`, sets the old choices as environment variables, then loads the same `dev.groovy` or `staging.groovy`.
  No stage is copied. It refuses pull requests and builds not started by a person.
- Actions that move out of the merge path: `fresh-install` (backs up, drops and rebuilds the registry databases),
  `deploy-without-services`, `deploy-with-commons-identity`, `validate-only`, `deploy-with-services`.
- A person must create the Jenkins job once, for example `farmer-registry-operator`: a multibranch pipeline on the
  repository, script path `Jenkinsfile.operator`, with automatic triggering suppressed. The first run only
  registers the parameters and ends `NOT_BUILT`.

Not verified: that the operator Jenkins job exists today. The Jenkins job tree on 5 November 2026 has no job
named like an operator job.

## 5. Branch protection

Read with `gh api repos/<owner>/<repo>/branches/<branch>` (field `protected`) and
`gh api repos/<owner>/<repo>/rulesets` on 6 November 2026.

| Repository | `main` | `develop` | `staging` | Rulesets |
| --- | --- | --- | --- | --- |
| `oan-helm` | not protected | not protected | branch does not exist | none |
| `farmer-registry` | not protected | not protected | not protected | none |
| `cropsown-regsitry` | not protected | not protected | not protected | none |
| `livestock-registry` | not protected | not protected | not protected | none |
| `da-registry` | not protected | not protected | not protected | none |
| `openg2p-data` | branch does not exist | not protected | branch does not exist | none |

So a pull request with failing checks can be merged today.

Plan to fix this (from the rollout plan of 3 November 2026, section M, updated 5 November 2026). The status
column is the plan's own status; it was not re-checked except M1, which the table above shows is not done.

| Step | Action | Status in the plan |
| --- | --- | --- |
| M1 | Branch protection with required checks on all repositories, for `develop` and `staging` | Blocked, waiting for ASMIT's approval |
| M2 | Fix the `popup-browser` check (Playwright install on the runner) so it can be required | Not started |
| M3 | Required `helm lint` and `helm template` check on every chart pull request | Not started |
| M4 | `--atomic` rollback in the staging dashboard and connector scripts | Not started |
| M5 | Jenkins failure alerts on every pipeline | Not started |

Related facts read from the repositories: the staging dashboard script `scripts/ci/deliver_staging_dashboards.sh`
and connector script `scripts/ci/deliver_staging_farmer_connector.sh` call `helm upgrade --install --wait`
without `--atomic`, so a failure leaves the release as it stopped (M4). `.github/workflows/validate.yaml` of this
repository runs on pull requests; it is not a required check because there is no protection.

## 6. Pull requests waiting in this repository

| Pull request | What it does | State |
| --- | --- | --- |
| 128 | Registry charts create and refresh their own ECR pull secret (a hook job plus a six-hourly CronJob per release) | open |
| 127 | Naming stage 1: renames in this repository (see [naming-standard.md](naming-standard.md)) | open |
| 125 | Keeps an image's own digest in step with its tag when packaging a chart | open |
| 55, 47 | Connector secret sync, and running the Livestock connector from the registry chart | open since 29 October 2026 |

Source: `gh pr list --repo Centre-for-Open-Societal-Systems/oan-helm --state open`.
