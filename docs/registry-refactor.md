# Registry refactor candidates and central chart ownership

`develop-refactor` prepares central chart `1.0.0-dev.8`. Crop and Livestock use
the unchanged published OpenG2P registry dependency `1.2.2-rc.557`, matching their
extension image bases. Other existing chart dependencies remain unchanged.
Earlier published packages are retained byte-for-byte. This branch does not
upgrade New Dev or staging and does not replace a Helm owner.

Crop and Livestock deliberately fail before emitting workload manifests. Their
application/domain/source-contract and restored-data acceptance is incomplete.
Candidate validation proves package integrity, dependency resolution and that
blocking behavior; it does not claim successful application deployment or
preservation. `--release-ready` continues to reject this candidate.

Registry repositories own domain models, schemas, registered services/widgets,
metadata, translations, templates, native import mappings, thin images and
their existing guarded CI. Editable Helm source belongs here. Consumers use a
specific central archive, SHA-256 and platform pin, with no local-chart fallback.
Normal image updates retain the approved chart package and record image digests.

## Independent dashboard releases

`addons/registry-dashboards/` contains the preserved Farmer, Crop and Livestock
dashboard-release charts, now version `0.1.2`. Existing chart/release names,
selectors, Services, IAM/Secret references and auth contracts are retained.
They remain independent releases; moving source does not adopt their resources
into the core registry release. Each existing registry pipeline can consume its
exact archive from the same central repository.

Dashboard application/API source remains in the six existing COSS repositories.
Humans retain `Dashboard Viewer`; service accounts use `charts:read`. The addon
checks use synthetic values, compare source and packaged resource identities,
selectors/images/Secret references and exercise two namespaces without Kubernetes.
Live login, chart data, release ownership and preservation still require their
own evidence. Registry CI retains delivery ownership and existing ECR names.

## Shared Master Data prerequisite

`reference/cropsown-master-data/` preserves the complete original lookup catalog
and its source hashes. It is an administration input, not a registry SQL seed or
an automatically executed chart hook. Existing Master Data values are unchanged.
Migrate missing values through supported Master Data administration, preserving
codes and relationships. Do not recreate legacy lookup tables inside a registry
or read Master Data's database directly from a registry extension.

## Connectors

Removing vendored connector source/build steps from a registry must not stop,
replace, re-own or rewind its existing external connector. Preserve deployed
images, subscriptions/checkpoints, source signatures and native ingestion/event
contracts. The advertised upstream connector source URLs returned 404 during
analysis, and live Rancher ownership access was unavailable. Independent
connector source/artifact/operational ownership remains a promotion prerequisite;
do not replace it with an assumed image or claim a live handoff from source cleanup.
