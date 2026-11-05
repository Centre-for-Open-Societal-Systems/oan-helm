# Chart channels

Registry charts are moving out of this repository into `helm/` on each registry branch. This
repository keeps publishing them. Chart source for Commons Services stays here.

| Registry ref | Version | Published to |
| --- | --- | --- |
| `develop` | `0.0.0-develop.<n>` | `repository/develop/` |
| `staging` | `<line>.<next>-rc.<n>` | `repository/staging/` |
| tag `N.N.N` | `N.N.N` | `repository/release/` |

`<n>` is the commit count of the registry branch. The chart and all images of a commit share one
version. This follows OpenG2P's policy in `openg2p-packaging`, with one difference: OpenG2P names the
release line `N.N`, and OAN names it `staging`. See `scripts/ci/derive-version.sh`.

Each folder is its own Helm repository. In Rancher, add one repository per environment with the raw
URL of that folder.

## How a chart is published

1. A registry pipeline runs `scripts/ci/package_chart.py`, which takes the version from
   `scripts/ci/derive-version.sh`, packages `helm/<chart>` and writes the images of the build into the
   packaged values. The pipeline deploys this archive, and step 2 publishes the same file. Farmer has
   its own `ci/deploy/package_chart.py` with the same result.
2. The pipeline runs `scripts/ci/publish_chart.py`, which adds that one archive to `repository/<channel>/`.
   A version that already exists is refused.
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
`repository/develop/`, adds the rc tag and the `staging` alias to the same ECR digests, and packages the chart again with
the rc version. The annotation `oan.org/promoted-from` names the develop chart. The promotion fails if develop never built
that tree, so anything that must reach staging goes through develop and New Dev first. Environment settings are not part
of the tree: they are in `environments/staging/values/`.

A release tag does the same from the rc. The `release` branch does not exist yet; it arrives with production.

## Publishing credential

Pipelines use the token of a maintainer account, Jenkins credential `oan-helm-fork-token`. Configuration of the
GitHub App that will replace it is pending; only the Jenkins credential changes when it is ready. Commits always
carry the name in `CHANNEL_PUBLISHER` in `scripts/check_protected_paths.py`, and on `main` that name may only add
new archives to channel folders.

`main` has no ruleset yet, so this is checked after the push, not blocked before it. Add a ruleset when the App
is configured.

The flat `repository/` folder stays as it is until no cluster or pin reads it.
