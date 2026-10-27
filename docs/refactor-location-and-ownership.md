# COSS refactor candidate ownership and location support

Crop and Livestock core charts and all three registry dashboard release charts
are maintained here. Registries consume a commit, chart version and archive
SHA-256; they do not resolve dependencies or mutate chart versions in Jenkins.
Dashboard applications retain independent COSS source repositories and
registry-owned CI, ECR, releases, authentication and reporting views.

Candidate 1.0.0-dev.11 keeps the registry platform at rc.557 and incorporates
Farmer's native Master Data develop.118 location contract. Commons depends on
OpenG2P's published `openg2p-master-data` chart `0.0.0-develop.118` (vendored under
`charts/openg2p-commons-services/charts/`), and its values pin the API and UI images
by digest. Earlier candidates bundled an unmodified upstream snapshot of the same
chart; it was removed once the chart was published.

Commons, Crop and Livestock candidates refuse to render workloads while their
acceptance remains incomplete. Local dependency, archive, routing and isolated
template checks are not a restored-data preservation rehearsal or a deployment.
Previously published dev.8 archives remain unchanged. Unrelated Commons bundled
dependency bytes are retained from dev.8 rather than refreshed incidentally.

Geo seeding is disabled. Geography, country-pack catalogue values, existing
geographic assignments, identity policies and open AWE tasks must be reconciled
through supported administration and tested on restored copies before promotion.
ETH-OAN with agriculture is the intended configuration; existing data must not be
replaced by a demo seed.

Upstream's develop.118 seed image carries only ETH and XKM, so `geoSeed.image` pins
`ghcr.io/asmitonweb/master-data-db-seed:0.0.0-develop.118-oan.1` by digest: the
upstream image, by digest, with `/openg2p-data` replaced by the OAN openg2p-data
fork at the commit recorded in `releases/1.0.0-dev.11.yaml`. Its loader, scripts
and packages are upstream's, byte for byte. The fork builds it from
`docker/master-data-db-seed/Dockerfile` when a `master-data-db-seed/<tag>` tag is
pushed. ETH-OAN passes the pack's `validate_pack.py`, and seeding it into an empty
Master Data develop.118 database published 21,037 units and 74 lists as version 1;
a second run changed nothing. Moving the API to another build means a seed image on
that build's base digest. Crop's historic lookup SQL, the input for that
reconciliation, is in the Crop repository at commit `4ed8a1f`
(`cropsown-extension/src/openg2p_registry_cropsown_extension/meta_data/lookup-data/`);
it is never executed against a registry database.

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
