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

1. A registry pipeline runs `scripts/ci/derive-version.sh`, packages `helm/<chart>` with that version
   and writes the image digests of the build into the packaged values.
2. The pipeline runs `scripts/ci/publish_chart.py`, which adds that one archive to `repository/<channel>/`.
   A version that already exists is refused.
3. `.github/workflows/publish-channels.yaml` runs `scripts/publish_channels.py`: it checks the archive,
   seals it in `releases/channels.json`, rebuilds `index.yaml` and `SHA256SUMS`, adds a `CHANGELOG.md`
   entry and tags `<chart>-<version>`.

Chart annotations `oan.org/source-repository`, `oan.org/source-commit` and `oan.org/source-subject`
become the changelog line.

The pipeline token belongs to the GitHub App named in `CHANNEL_PUBLISHER` in
`scripts/check_protected_paths.py`. On `main` it may only add new archives to channel folders.

The flat `repository/` folder stays as it is until no cluster or pin reads it.
