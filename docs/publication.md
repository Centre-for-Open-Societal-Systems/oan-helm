# Repository publication

GitHub serves the committed `repository/` directory, `index.yaml` and chart archives,
through `raw.githubusercontent.com`. That directory is the Helm repository Rancher and
`helm repo add` use:

```
https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/
```

No GitHub Pages or other publication service is involved. Archive URLs in `index.yaml`
are relative, so the same files work from any raw directory URL.

## Who writes `repository/`

Only the release workflow (`.github/workflows/release.yaml`). After a merge to `main`
that changes a chart, it packages the chart's next version, adds the archive and its
`index.yaml` entry, regenerates `SHA256SUMS`, seals the archive in
`releases/artifacts.json` and commits as `github-actions[bot]`. The `protected-paths`
check in `.github/workflows/validate.yaml` fails any pull request that edits
`repository/` and flags any commit on `main` that touches it without coming from the
release bot. See [versioning.md](versioning.md#automatic-release).

## Guarantees

- **Immutable archives.** A published `.tgz` never changes: validation compares every
  archive with its recorded SHA-256, and a changed chart always gets a new version.
- **Stable index.** A release adds entries; existing entries, including their
  `created` timestamps, are left as they are.
- **Verified before commit.** The release workflow reruns the full validation,
  including installing every index entry over HTTP from a loopback server, before it
  commits.
- **Publishing is not deploying.** A new version appears in Rancher after a repository
  refresh; installed releases change only when an operator upgrades them.

## Requirements

The repository must stay publicly readable, and Rancher's server must reach
`raw.githubusercontent.com` over HTTPS. Client or CDN caching can delay a new version
by a few minutes; refresh the Rancher repository, or run `helm repo update`, and select
the exact version.

```sh
helm repo add oan https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/
helm repo update oan
helm search repo oan --versions --devel | head
```

Installation prerequisites are separate from publication: a published chart can still
need images, Secrets or configuration before it runs. See [readiness.md](readiness.md)
and [rancher-dev.md](rancher-dev.md).
