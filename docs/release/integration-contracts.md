# Integration contracts

Every data flow between systems. Facts as of 5 and 6 November 2026.

Sources: values files in `environments/dev/values/` and `environments/staging/values/` of this repository
(`main`, commit `7db1f6a`); `integrations/farmer-reference/` and `docs/` of `farmer-registry`,
`cropsown-regsitry` and `livestock-registry` at `origin/develop`; live reading of Partner Management and the
Approval Workflow Engine databases; OpenG2P documentation pages linked in the text.

No secret value is written here. Files and Secret names are named only where they are part of the contract.

## 1. Flow list

| # | Source | Target | Transport | Name of the message or call | Authentication |
| --- | --- | --- | --- | --- | --- |
| 1 | Farmer registry | Crop sown and Livestock (through their connectors) | WebSub topic, delivered by Kafka-backed hub, then the receiving connector | event `farmer_reference.changed.v1` | Signed payload; callback with a hash-based message signature (HMAC); hub only inside the cluster |
| 2 | Crop sown, Livestock registries | Farmer registry partner API | Synchronous HTTP, DCI search | `POST /dci/sync/search` on `farmer-registry-partner-api.farmer` | Signed request, signed response, consent from Consent Manager |
| 3 | ODK Central | Registry connector | ODK Central API read by the connector | form submissions | Not verified: how the connector signs in to ODK Central |
| 4 | Registry connector | Registry partner API | HTTPS | `/partner/ingest_data?data_model=dcivc` | RS256 signed envelope per partner identity |
| 5 | Registry (staff, intake, change request) | Approval Workflow Engine | HTTP | policies `registry.change_request.<entity>`, `registry.intake_form.<entity>` | Keycloak client; approval callback secret |
| 6 | Registry dashboard API | Dashboard user interface, shared dashboard | HTTP | dashboard chart API (path Not verified; the shared dashboard uses `/v1/charts` for Access to Credit) | Token with role `charts:read`, checked by the identity staff API |
| 7 | Registries | Master Data | HTTP | geography and list reads | Keycloak client |
| 8 | Registries | Consent Manager | HTTP | consent check and record | Keycloak client and partner key |
| 9 | Registries, services | Partner Management | HTTP | partner and key lookup | Keycloak client |

Rows 7 to 9 are listed from the service URLs in the values files (`masterDataApiUrl`, `consentManagerUrl`,
`consentManagerStaffUrl`, `partnerManagementApiUrl`). Not verified: the exact paths and payloads of rows 7 to 9.

## 2. Farmer change notice (flow 1)

| Item | Value today | Source |
| --- | --- | --- |
| Event type | `farmer_reference.changed.v1` | `integrations/farmer-reference/config.yaml` in Farmer |
| WebSub topic | `oan.farmer-reference.changed.v1` | same file |
| Kafka storage name | `oan_farmer_reference_changed_v1` | `integrations/farmer-reference/README.md` in Crop sown |
| Data model mnemonic | `FARMER_REFERENCE_CHANGED_V1` | same |
| Publisher | Farmer registry outgestion (topic id `farmer_reference_changed_v1_topic`, template `farmer_reference_changed_v1_template`) | Farmer `config.yaml` |
| Payload | Farmer ID and the Fayda ID (a 16-digit FAN or a 12-digit FIN), a stable event identifier; no demographic fields | Farmer README, Crop sown README |
| Hub | `http://commons-services-websub.commons.svc.cluster.local`, internal only | `docs/websub-new-dev.md` |
| Kafka | the hub stores its own metadata topics in the Commons Kafka; Celery does not use Kafka (Redis brokers Celery) | Farmer README, `docs/websub-new-dev.md` |
| Receiver | connector that explicitly selects `FARMER_REFERENCE_CHANGED_V1` and validates with `notification.schema.json` | Crop sown README |
| Accepted names at the receiver | `farmer_reference.changed.v1` and `farmer-registry.farmer.changed.v1` | Crop sown README |

What the receiver does: it validates the notice, confirms the Farmer ID and Fayda ID pair against its own
approved reference, repeats the signed, consented lookup (flow 2), and creates or reuses a change request that
goes through the normal two-stage approval. A notice never writes demographic data by itself.

Rename (pending merge): the naming plan renames the event to `farmer-registry.farmer-profile.changed.v1`, the
WebSub topic the same, the Kafka storage name to `farmer_registry_farmer_profile_changed_v1` and the mnemonic to
`FARMER_REGISTRY_FARMER_PROFILE_CHANGED_V1`. Order: receivers accept both names, then the Farmer registry
publishes the new topic only, then connectors subscribe to the new topic, then the old topic is deactivated once
its Kafka lag is zero. Source: [naming-standard.md](naming-standard.md), section 3. The stage 2 pull requests are
not on a default branch at the time of writing. Not verified: their numbers and state.

OpenG2P references: outgestion
https://docs.openg2p.org/products/registry/registry/design/outgestion-pipeline and ingestion
https://docs.openg2p.org/products/registry/registry/design/ingestion-pipeline.

## 3. Farmer lookup by Crop sown and Livestock (flow 2)

| Item | Crop sown | Livestock |
| --- | --- | --- |
| Endpoint | `http://farmer-registry-partner-api.farmer.svc.cluster.local/dci/sync/search` | same |
| Partner identity used | `Crop_sown_partner_internal` | `Live_stock_partner_internal` |
| Consent audience | `crop-registry` | `farmer-registry` |
| Consent controller | `farmer-registry` | Not verified (line not read) |
| Consent purpose | `registry_intake` | Not verified |
| Consent scopes | `farmer_personal_details,farmer_reference` | `farmer_personal_details,farmer_reference` |
| Response signature | RS256, key id `farmer-registry-dci-rsa`, public key mounted from the ConfigMap `farmer-registry-dci-signing-public` of the namespace `farmer` | same key id |
| Request signature | private key from a mounted Secret (`crop-farmer-lookup-signing-ed25519` exists in staging `crop`) | Not verified |

Source: `environments/staging/values/cropsown.yaml` lines 131 to 155 and 253 to 256;
`environments/staging/values/livestock.yaml` and `environments/dev/values/livestock.yaml`. The Farmer ID
format, `FR-` followed by 12 digits, and the Fayda ID rule are in `docs/refactor/FARMER-LOOKUP.md` of Crop sown.

The setting names carry a prefix that the naming plan renames to `REGISTRY_FARMER_REFERENCE_`; the plan lists
the current mount paths and the new ones in [naming-standard.md](naming-standard.md).

## 4. ODK Central to the registry (flows 3 and 4)

1. Field staff submit forms in ODK Central (`odk-central.<domain>`).
2. A registry connector (releases `farmer-registry-connector`, `cropsown-connector`, `livestock-connector`) reads
   the submissions. Each connector has its own database and queue (Farmer on New Dev: database
   `farmer_connector_v2`, queue `farmer-registry-connector-v2`; source `docs/operations/connector.md` in Farmer).
3. The connector posts the data to the partner API of its registry:
   `https://partner-farmer.<domain>/partner/ingest_data?data_model=dcivc` and the same path on
   `partner-crop` and `partner-livestock` (the `PARTNER_INGEST_URL` value in each values file).
4. The envelope is signed with RS256. It binds partner and message identifiers, the hash of the payload, the issue
   time and the expiry. Unsigned, altered, wrong-key and expired envelopes are rejected; an exact retry returns
   the original correlation identifier. The Farmer connector signs as the partner `farmer-partner`; its private
   key is in the retained Secret `farmer-connector-v2-signing`, never in Git.
5. The registry puts the submission through intake and the two-stage approval (flow 5) before it reaches the
   register.

Image used by the connector: see [versions.md](versions.md), section 3. The connector is the OpenG2P
`registry-connector` (names and environment prefix `CONNECTOR_*`; evidence in
[naming-standard.md](naming-standard.md)).

Known gap: pull request 232 of Farmer (merged 5 November 2026) adds an admin login to the Farmer connector image.
New Dev runs that image; staging runs an older one (see [versions.md](versions.md)). Not verified: whether the
Crop sown and Livestock connectors have an admin login.

## 5. Dashboards (flow 6)

| Part | Detail | Source |
| --- | --- | --- |
| Dashboard API per registry | runs with the registry release; authentication on (`AUTH_ENABLED: 'true'`), audience `<registry>-dashboard-api`, issuer URL `http://commons-services-iam-staff-portal-api.commons.svc.cluster.local`, required role `charts:read` | `environments/staging/values/farmer.yaml` |
| Dashboard user interface per registry | its own release, calls its dashboard API | `docs/registry-refactor.md` |
| Shared dashboard `oan-dashboards` | reads `http://farmer-registry-dashboard-api.farmer`, `http://cropsown-registry-dashboard-api.crop`, `http://livestock-registry-dashboard-api.live`, and for Access to Credit `https://a2c-develop-gateway.oanstaging.com` path `/v1/charts` | `environments/staging/values/oan-dashboards.yaml` |
| People vs services | people keep the role `Dashboard Viewer`; service accounts use `charts:read` | `docs/registry-refactor.md` |

Drift: on staging the Crop sown dashboard API does not exist (see [versions.md](versions.md), section 6, item 8).

## 6. Approvals (flow 5)

Policy keys follow `registry.change_request.<entity>` for changes to register records and
`registry.intake_form.<entity>` for intake forms. This is the OpenG2P rule (see
[naming-standard.md](naming-standard.md)). Keys found in the Approval Workflow Engine database (table
`approval_policy`):

| Registry | Keys on New Dev | Keys on staging |
| --- | --- | --- |
| Farmer | `registry.change_request.farmer`, `.farmer.default`, `.household`, `.household.default`; `registry.intake_form.farmer`, `.farmer.default`, `.household`, `.household.default` | same keys |
| Crop sown | `registry.change_request.cropsown`, `.cropsown.default`, `.cropsown-farmer.default`, `.cropsown-farmer.verified-update-skips-review`, `.devcropsown`, `.devcropfarmer`; `registry.intake_form.cropsown`, `.cropsown.default`, `.planning_cropsown`, `.cultivation_cropsown`, `.sowing_cropsown`, `.harvesting_cropsown` and `dev...` variants | `registry.change_request.cropsown`, `.stgserver_cropsown`; intake keys for the four forms and `...stgserver_cropsown` variants; no `cropsown-farmer` key |
| Livestock | `registry.change_request.livestock`, `.livestock.default`, `.livestock-farmer.default`, `.livestock-farmer.verified-update-skips-review`; `registry.intake_form.livestock`, `.livestock.default` | same keys |
| Development Agent | `registry.change_request.da`, `registry.intake_form.da` | none |

Source: live read-only query `select policy_key from approval_policy` in the database `awe`.

Rules (from the Farmer, Crop sown and Livestock documentation): a change goes through two stages; an update that
comes from a verified Farmer notice can skip review under the `verified-update-skips-review` policy; the
reviewer is chosen from the receiving registry's own approved Woreda, so a proposed location cannot choose its own
reviewer (`integrations/farmer-reference/README.md`, Crop sown). Register records are never written directly:
every change goes through a change request or an intake form.

Drift: staging lacks the Development Agent policies and the Crop sown Farmer policies, and carries
`...stgserver_cropsown` keys that New Dev does not have. The Crop sown flow 1 and 2 cannot approve on staging
until the `cropsown-farmer` policy exists there. Not verified: that this is the cause of any failure.

## 7. Partner ids in Partner Management (table `pm_partners`)

Read with a SELECT of `partner_id` on 5 November 2026.

New Dev (20): `A2C Service`, `COOP_BANK`, `Crop_sown_partner_internal`, `Crop_sown_partner_local`,
`farmer-partner`, `Live_stock_partner_internal`, `PARTNER_ABC_BANK`, `PARTNER_AGGRAGATION`,
`PARTNER_AGGREGATION_LAYER`, `PARTNER_COOP_BANK`, `PARTNER_CROPSOWN`, `PARTNER_CROP_SOWN_PARTNER_INTERNAL`,
`PARTNER_CROP_SOWN_PARTNER_LOCAL`, `PARTNER_DA_SERVICES`, `PARTNER_LIVESTOCK`,
`PARTNER_LIVE_STOCK_PARTNER_INTERNAL`, `PARTNER_STAFF_PORTAL`, `POSTMAN_AGG_INTERNAL_MVW8HIM8`,
`synthetic-connector-6055a69ff1ac`, `synthetic-connector-b48e4b61d67f`.

Staging (8): `CropSown`, `Crop_sown_partner_internal`, `farmer-partner`, `Live_stock_partner_internal`,
`PARTNER_CROP_SOWN_PARTNER_INTERNAL`, `PARTNER_LIVESTOCK`, `PARTNER_LIVE_STOCK_PARTNER_INTERNAL`,
`PARTNER_TEST_PROTEAN`.

Meaning of the ids that matter:

| Partner id | Used by |
| --- | --- |
| `farmer-partner` | The Farmer connector signs ingest envelopes with it (Farmer `docs/operations/connector.md`) |
| `Crop_sown_partner_internal` | Crop sown, as the source partner for the Farmer lookup (staging values) |
| `Live_stock_partner_internal` | Livestock, as the source partner for the Farmer lookup (staging and dev values) |
| `PARTNER_<NAME>` ids | The registry derives a partner topic id as `PARTNER_` plus the sender name in capitals (OpenG2P partner API, `g2p_dci_controller.py` line 162); these rows are the derived twins |

Test and mistaken ids: `synthetic-connector-*` and `POSTMAN_AGG_INTERNAL_*` (New Dev), `PARTNER_TEST_PROTEAN`
(staging), `PARTNER_AGGRAGATION` (misspelt). Not verified: that they are unused and safe to remove. Removing a
partner id is a key re-registration and a consent change; follow the naming plan, stage 3.

Not verified: which partner id the Development Agent services and the aggregation service use.
