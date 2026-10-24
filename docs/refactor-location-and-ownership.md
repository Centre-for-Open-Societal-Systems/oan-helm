# COSS refactor candidate ownership and location support

Crop and Livestock core charts and all three registry dashboard release charts
are maintained here. Registries consume a commit, chart version and archive
SHA-256; they do not resolve dependencies or mutate chart versions in Jenkins.
Dashboard applications retain independent COSS source repositories and
registry-owned CI, ECR, releases, authentication and reporting views.

Candidate 1.0.0-dev.10 keeps the registry platform at rc.557 and incorporates
Farmer's native Master Data develop.118 location contract. The exact unmodified
upstream chart snapshot, source hashes and resolved image digests are recorded in
`upstream-snapshots/master-data-location/SOURCE.json`. The upstream checkout and
Farmer checkout were not changed. The snapshot has a source-chart version of
0.0.0-develop; there is no claim of a published develop.118 Helm chart.

Commons, Crop and Livestock candidates refuse to render workloads while their
acceptance remains incomplete. Local dependency, archive, routing and isolated
template checks are not a restored-data preservation rehearsal or a deployment.
Previously published dev.8 archives remain unchanged. Unrelated Commons bundled
dependency bytes are retained from dev.8 rather than refreshed incidentally.

Geo seeding is disabled. Geography, country-pack catalogue values, existing
geographic assignments, identity policies and open AWE tasks must be reconciled
through supported administration and tested on restored copies before promotion.
ETH-OAN with agriculture is the intended configuration; existing data must not be
replaced by a demo seed. Crop's historic lookup SQL is retained under `reference/`
for that reconciliation and is never executed against a registry database.

Dashboard API templates retain the required auth configuration and reject
reserved AUTH_* overrides. Digest images, image-pull Secrets, envFrom and the
reporting database Secret contracts are preserved. Public environment overlays
are central; credential values stay outside this repository.

Validation: 20 unit tests, six core package/index checks (three fail-closed
candidates), three independent dashboard source/package renders, two namespaces,
and exact snapshot file hashes. No Kubernetes environment was changed.

Hosted Linux CI rejected the dev.9 Commons source seal because the Windows
working copy contained CRLF while Git stored LF. Dev.10 fixes the source and
checks repository LF bytes before packaging. Published dev.9 archives and their
SHA-256 records are retained; no immutable artifact was overwritten.
