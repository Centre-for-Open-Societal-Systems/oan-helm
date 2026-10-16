# Repository publication

The branch is based on COSS `oan-helm/main` and pushed only to
`asmitonweb/oan-helm`. The PR targets COSS `main`; merging remains manual.

PR validation checks locks, strict linting, original names/selectors/Secret
references, namespace isolation, optional workloads, packages and HTTP index
downloads. It has read-only repository permissions and does not publish/deploy.

After merge, the Pages workflow repeats validation, checks release readiness,
uploads `docs/` and deploys Pages. Configure **Settings → Pages → Source: GitHub
Actions** first. A fork preview uses the same setting on the fork and a reviewed
merge into its `main`; pushing the feature branch alone does not publish. No
application/cluster deployment or image build-number synchronization is included.

Retain published `.tgz` bytes and cumulative index entries. The artifact manifest
binds archive checksums to source fingerprints; validation rejects source changes
under an existing version. Use a new version for future chart changes. Relative
archive URLs let the exact same packages work under both Pages hostnames.

- COSS: `https://centre-for-open-societal-systems.github.io/oan-helm/`
- Fork: `https://asmitonweb.github.io/oan-helm/`

Empty `publicationBlockers` in the release manifest allows chart publication.
Installation prerequisites are recorded separately: publishing does not make DA
or unavailable optional images ready to run. Follow the
[readiness table](readiness.md) and [Rancher guide](rancher-dev.md).
