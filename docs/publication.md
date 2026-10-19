# Repository publication

The branch is based on COSS `oan-helm/main` and pushed only to
`asmitonweb/oan-helm`. The PR targets COSS `main`; merging remains manual.

PR validation checks locks, strict linting, original names/selectors/Secret
references, namespace isolation, optional workloads, packages and HTTP index
downloads. It has read-only repository permissions and does not publish/deploy.

GitHub itself serves the committed `repository/index.yaml` and chart archives
through `raw.githubusercontent.com`. No Pages setup or publication deployment
is required. PR/push validation checks release readiness and all packages.
After a reviewed merge, the upstream `main` URL serves those files. The fork
preview points to the feature branch and is usable before merge. No
application rollout is triggered by publication. The separately authorized live URL
migration is recorded in `releases/live-domain-migration.json`; build-number
synchronization remains deferred.

Retain published `.tgz` bytes and cumulative index entries. The artifact manifest
binds archive checksums to source fingerprints; validation rejects source changes
under an existing version. Use a new version for future chart changes. Relative
archive URLs let the exact same packages work under both raw GitHub directory URLs.

- COSS after merge: `https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/`
- Current fork preview: `https://raw.githubusercontent.com/asmitonweb/oan-helm/feat/dev-wildcard-domain/repository/`

Use the directory URL above in Rancher or `helm repo add`. Do not use a GitHub
HTML `tree`/`blob` URL. The repository must remain publicly readable for this
unauthenticated setup, and Rancher's server must be able to reach
`raw.githubusercontent.com` over HTTPS. Refresh the Rancher repository after a
merge; client/GitHub caching may delay visibility. Select the exact chart version.

```sh
helm repo add coss https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/
helm repo update coss
helm show chart coss/openg2p-commons-services --version 1.0.0-dev.4
```

For preview, substitute the fork URL. Future releases must commit their new
packages, checksums, cumulative index and release metadata together. GitHub
serves committed bytes; validation does not commit or upload generated files.

Empty `publicationBlockers` in the release manifest allows chart publication.
Installation prerequisites are recorded separately: publishing does not make DA
or unavailable optional images ready to run. Follow the
[readiness table](readiness.md) and [Rancher guide](rancher-dev.md).

The current version comes from `releases/current.yaml`. `1.0.0-dev.4` adds the
wildcard development domain and shared Gateway. All fifteen prior archives remain
unchanged. Live URL migration uses installed chart versions and does not implicitly
upgrade application images. See [the URL guide](dev-urls.md) and
[service onboarding](service-onboarding.md).
