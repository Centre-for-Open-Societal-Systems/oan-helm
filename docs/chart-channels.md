# Chart channels

Registry charts are moving out of this repository into `helm/` on each registry branch. This
repository keeps publishing them. Chart source for Commons Services stays here.

| Registry ref | Version | Published to |
| --- | --- | --- |
| `develop` | `<version>-develop.<BUILD_NUMBER>` | `repository/develop/` |
| `staging` | `<version>-staging.<BUILD_NUMBER>` | `repository/staging/` |
| tag `N.N.N` | `N.N.N` | `repository/release/` |

`<version>` is `version` in the registry's `init.yaml` and `<BUILD_NUMBER>` the Jenkins build number
(`scripts/ci/oan_version.py`). The chart and all images of a build share that one version, and the images are
tagged with it. Section 6 of [naming-standard.md](release/naming-standard.md) has the full rule, image paths
included.

A registry without `init.yaml` keeps the older versions until it adopts the standard: `0.0.0-develop.<n>` on
develop and `<line>.<next>-rc.<n>` on staging, `<n>` being the commit count of the branch
(`scripts/ci/derive-version.sh`: OpenG2P's policy from `openg2p-packaging`, with the release line named
`staging`). `repository/staging/` accepts both forms. Versions are ordered as SemVer, so `1.0.0-staging.1` is
newer than `1.0.0-rc.553`.

Each folder is its own Helm repository. In Rancher, add one repository per environment with the raw
URL of that folder.

## How a chart is published

1. A registry pipeline runs `scripts/ci/package_chart.py`, which takes the version from
   `scripts/ci/derive-version.sh`, packages `helm/<chart>` and writes the images of the build into the
   packaged values. The pipeline deploys this archive, and step 2 publishes the same file. The
   application repositories (the Frappe services and their user interfaces) keep only their constants in
   `ci/package_chart.py`; the steps are `scripts/ci/app_chart.py`, which that script loads at a pinned
   commit of this repository (`OAN_HELM_REF`). A change to `app_chart.py` reaches a repository when it
   moves its pin.
2. The pipeline runs `scripts/ci/publish_chart.py`, which adds that one archive to `repository/<channel>/`.
   A published version is never replaced: exit 4 when it was published from the same source commit (a re-run,
   treated as success), exit 5 when it holds another commit. Exit 5 fails the build: bump `version` in `init.yaml`.
3. `.github/workflows/publish-channels.yaml` runs `scripts/publish_channels.py`: it checks the archive,
   seals it in `releases/channels.json`, rebuilds `index.yaml` and `SHA256SUMS`, records the version in
   `releases/history/<channel>/<chart>.md`, adds a `CHANGELOG.md` entry and tags `<chart>-<version>`.

Pipelines describe a version in chart annotations:

| Annotation | Meaning |
| --- | --- |
| `oan.org/source-repository` | `owner/repository` of the source |
| `oan.org/source-commit` | Full commit |
| `oan.org/source-subject` | Commit subject, used as the changelog line |
| `oan.org/release-name`, `oan.org/release-namespace` | Used in the rollback command |
| `oan.org/values-overlay` | Overlay path, default `helm/environments/<env>/values.yaml` |
| `oan.org/upgrade-notes` | Optional. Migrations or steps an operator must know about |

[rollback.md](rollback.md) explains how to use this record.

## Promotion

Staging is promoted from develop, never rebuilt. A pull request brings develop into `staging`, so the source tree of
`staging` equals a commit develop already built. `scripts/ci/promote_chart.py` then finds the chart of that tree in
`repository/develop/`, adds the staging version as a tag to the same ECR digests, and packages the chart again with
that version. There is no moving `staging` tag. The annotation `oan.org/promoted-from` names the develop chart. The promotion fails if develop never built
that tree, so anything that must reach staging goes through develop and New Dev first. Environment settings are not part
of the tree: they are in `environments/staging/values/`.

A release tag does the same from the staging version. The `release` branch does not exist yet; it arrives with production.

## Publishing credential

Pipelines use the token of a maintainer account, Jenkins credential `oan-helm-fork-token`. Configuration of the
GitHub App that will replace it is pending; only the Jenkins credential changes when it is ready. Commits always
carry the name in `CHANNEL_PUBLISHER` in `scripts/check_protected_paths.py`, and on `main` that name may only add
new archives to channel folders.

`main` has no ruleset yet, so this is checked after the push, not blocked before it. Add a ruleset when the App
is configured.

The openg2p-data develop build uses the same credential for one more write: it moves the Master Data seed image pin.
Its commits carry the name `oan-seed-pinner` (`SEED_PINNER` in `scripts/check_protected_paths.py`). On `main` that name
may only change the `repository:` and `tag:` lines of `master-data.geoSeed.image` in
`charts/openg2p-commons-services/values.yaml` (a tag of the form `N.N.N-develop.N@sha256:<digest>` for the
`eoan/openg2p-data/master-data-db-seed` repository) and add a `releases/1.0.0-dev.<n>.yaml` record. Any other change
under that name fails the push check, the commit has no green checks, and the New Dev delivery does not run from it.

The flat `repository/` folder stays as it is until no cluster or pin reads it.
