# Kafka and WebSub in New Dev

Phase one prepares shared delivery infrastructure. It does not activate registry
outgestion, replay records, or change Crop/Livestock enrichment.

The opt-in `websub` dependency is pinned to 1.3.2. The New Dev overlay enables
one hub and one consolidator, reusing `commons-kafka:9092`; it installs no broker.
Both services are internal, with no ingress or Istio route. Registry's future
hub root is `http://commons-services-websub.commons.svc.cluster.local`.
MOSIP cookie authentication is disabled because current Registry publishers do
not acquire MOSIP auth-manager cookies. Callback challenge and HMAC verification
remain required. Do not expose this configuration publicly.

The New Dev overlay references immutable Secret `commons-websub-encryption`,
key `encryption-key`. Generate its 16-character random value once on the server
before the first upgrade. Retain it across hub/consolidator upgrades and rollback;
do not put the key in Git, public overlays, evidence or terminal output.

The regular Helm Job provisions four metadata topics with one partition and
replication factor one. `retention.ms=-1` and `retention.bytes=-1` prevent the
broker's two-hour default from erasing subscriptions. No existing topic or
broker defaults change. Monitor broker disk usage and metadata growth; unlimited
metadata retention requires an explicit future retention/compaction design.
Application WebSub topic names are values in metadata messages, not separate
Kafka topics containing Farmer changes.

## Upgrade and recovery

Use the existing `commons-services/commons` release with its saved private values.
Layer only `websub` and `websubTopicProvisioning` from the New Dev overlay for this
infrastructure change; do not inadvertently migrate other live values.
Retain the current compatibility renderer and its sibling cookie-guard files.
Use `--no-hooks` and `--skip-initialization-jobs`; the renderer permits only the
labelled WebSub topic Job in Commons. Render with the current release revision
and compare every existing resource before applying. Unrelated manifests,
images, Secrets, routes, selectors and ownership must remain unchanged apart
from chart-version labels. Preserve any live manual patches in the renderer.

Wait for the provisioning Job, hub and consolidator. Check their health paths
`/hub/actuator/health` and `/consolidator/actuator/health`, then test a synthetic
topic, challenge response, signed callback and recovery after each component
restarts. Reject `hub.mode=denied` even if HTTP is 200. Remove the synthetic
subscription/callback afterwards; never log its secret.

Back up release values, manifests and cluster resources privately before upgrade.
Rollback to the previous Commons revision restores application manifests; keep
the Kafka metadata topics and broker storage. Do not delete them as rollback.

References: [outgestion](https://docs.openg2p.org/products/registry/registry/design/outgestion-pipeline),
[upstream WebSub contract](https://github.com/OpenG2P/openg2p-documentation/tree/latest/platform/platform-services/websub).
