# OAN naming standard

Rule: nothing in OAN is named after the old organisation short name. Every name follows OpenG2P where OpenG2P
has a convention, and says what it is (source to target, entity, action) where OpenG2P leaves the name free.
The GitHub organisation `Centre-for-Open-Societal-Systems` and its URLs stay as they are.

In this document `<old-prefix>` stands for the old short name of the organisation. It is not written out, so
that this file follows its own rule.

Owner: ASMIT. Adapted from the workspace naming standard of 5 November 2026. Live identifiers were read back
from New Dev and staging on 5 November 2026.

Evidence: OpenG2P `registry-platform` branch 1.2, `farmer-registry` branch 1.2, `registry-connector` branch
`develop`, `partner-management`, `openg2p-packaging` tag `v1`, and OpenG2P versions branch `develop` at
`e3ea94b`. Charts are published at https://openg2p.github.io/openg2p-helm. The docs.openg2p.org statements below
were obtained through the documentation's search endpoint and are paraphrased: confirm them on the page before
citing them as authoritative. The repository statements are direct.

## 1. Rules taken from OpenG2P

| Concept | OpenG2P rule | Evidence |
| --- | --- | --- |
| Extension folder | `<domain>-extension` | `farmer-registry@1.2:farmer-extension/` |
| Extension package | module `openg2p_registry_<domain>_extension`, distribution `openg2p-registry-<domain>-extension`; no implementer prefix | `farmer-registry@1.2:farmer-extension/pyproject.toml` line 6; `registry-platform@1.2:reference-extension/pyproject.toml` |
| Extension selection | environment variable `REGISTRY_EXTENSION_MODULE=openg2p_registry_<domain>_extension` | `registry-platform@1.2:docker/README.md` ("The extension contract") |
| Images | `<org>/openg2p-<variant>-<role>`; roles staff-ui, staff-api, partner-api, celery, db-seed, sanity-tests | `farmer-registry@1.2:helm/openg2p-farmer-registry/values.yaml`; `openg2p-packaging@v1` |
| Chart | `openg2p-<variant>-registry` is a thin wrapper that depends on `openg2p-registry` with alias `registry`; value `global.registryVariant` | `farmer-registry@1.2:helm/openg2p-farmer-registry/Chart.yaml` |
| Service environment variables | `REGISTRY_STAFF_PORTAL_API_*`, `REGISTRY_PARTNER_API_*`, `REGISTRY_CELERY_WORKERS_*`, `REGISTRY_CELERY_BEAT_*`; chart values in camelCase under `global.` | `registry-platform@1.2:helm/openg2p-registry/values.yaml` |
| Connector environment variables | `CONNECTOR_*` (not `REGISTRY_CONNECTOR_*`) | `registry-connector@develop:api/.env.example` |
| Connector artefacts | distribution `openg2p-connector-service`, module `openg2p_connector_service`, images `openg2p/registry-connector-api` and `-ui` | `registry-connector@develop:api/pyproject.toml` |
| Tables | prefix `g2p_` even in extensions (`g2p_register_farmers`); constraints and indexes `ck_`, `uix_`, `ix_` | `farmer-registry@1.2` `register_domain/models/farmer.py`; registry-core outgestion models |
| Database and client names | database name is the release name with `-` changed to `_`; Keycloak client `<release>-staff-portal` | `registry-platform@1.2` `values.yaml` |
| Seed layout | `meta_data/<folder>/g2p_*.sql` and `awe_meta_data/10_approval_policy.sql`, `20_approval_stage.sql`, `30_approver_rule.sql` (the number is the apply order) | `farmer-registry@1.2:farmer-extension/src/.../meta_data` |
| Approval policy keys | `registry.change_request.<entity>` and `registry.intake_form.<entity>` | `farmer-registry@1.2` `awe_meta_data/10_approval_policy.sql` |
| Outgestion topic | `outgoing_topics.websub_topic` is a free string; the platform has no Kafka outgestion (the WebSub hub stores each topic in Kafka with `.` and `-` changed to `_`) | registry-core `outgestion_configuration.py` |
| Partner topic id | `PARTNER_<UPPER_SNAKE>` from the sender name | `partner-api` `g2p_dci_controller.py` line 162 |
| Partner ids and key ids | free strings | `partner-management` `core/api/README.md` |
| Event type strings, Kafka topic names, validation rule names | no OpenG2P convention found (searched registry-platform 1.2 core, apis, celery, reference extension, functional tests, and registry-connector) | search of those repositories |

Version context (OpenG2P versions, 5 November 2026): `registry-platform` latest `1.2.2-rc.681`;
`farmer-registry` `1.2.1-rc.326`. The registry chart 1.2 depends on common 2.30.0, postgres-init 1.2.0,
redis 19.6.4, id generator 1.1.2, keycloak-init 1.2.0 and registry-connector 0.0.0-develop.9.

## 2. OAN rules where OpenG2P leaves names free

- Event type and WebSub topic: `<source-registry>.<entity>.<action>.v<N>`, lowercase, with a hyphen inside a
  part. The Kafka topic is derived by the hub, so it reads the same with underscores.
- Data model mnemonic: the event name in upper snake case.
- Validation message keys: `validation_<field>` for format and `validation_<field>_min` for the earliest date.
- Organisation-level names (CI image namespace, chart annotations, helper templates, test labels) use `oan`.
- Write words in full. No abbreviations for registries (not `far`, `lr`, `live`), no environment names inside
  names, no ticket keys.
- OpenG2P has no implementer prefix. So the Python package, the distribution, `REGISTRY_EXTENSION_MODULE` and
  the `g2p_` table prefix do not become `oan_`.

## 3. Rename table (stage 2: names stored in live systems)

Status: planned. The stage 1 pull request in this repository is number 127 (open). Stage 2 is not on a default
branch at the time of writing.

| Today | New | Where | Migration |
| --- | --- | --- | --- |
| Event `farmer_reference.changed.v1`; WebSub topic `oan.farmer-reference.changed.v1`; Kafka `oan_farmer_reference_changed_v1`; mnemonic `FARMER_REFERENCE_CHANGED_V1` | Event and topic `farmer-registry.farmer-profile.changed.v1`; Kafka `farmer_registry_farmer_profile_changed_v1`; mnemonic `FARMER_REGISTRY_FARMER_PROFILE_CHANGED_V1` | Farmer outgestion (sender); Crop sown and Livestock receivers and connectors | E1 receivers accept both names; E2 Farmer publishes the new topic only; E3 connectors subscribe to the new topic; E4 the old topic is deactivated after its Kafka lag is 0 |
| Settings `<old-prefix>_FARMER_<NAME>` | `REGISTRY_FARMER_REFERENCE_<NAME>` | Crop sown and Livestock staff API, partner API, celery | code reads the new name and falls back to the old for one release; this repository's values switch; the fallback is removed the next release |
| Mount paths `/etc/<old-prefix>-farmer`, `/etc/<old-prefix>-farmer-key`, `/etc/<old-prefix>-farmer-awe` | `/etc/farmer-reference/source`, `/etc/farmer-reference/lookup-signing-key`, `/etc/farmer-reference/awe-client` | this repository's values | same release as the settings |
| Tables `<old-prefix>_farmer_references`, `..._farmer_reference_requests`, `..._farmer_submission_dependencies`, `..._farmer_workflow_outbox`, `..._farmer_pending_lookups`, `..._approval_binding_archive` and one index on pending lookups | `g2p_farmer_references`, `g2p_farmer_reference_requests`, `g2p_farmer_submission_dependencies`, `g2p_farmer_reference_awe_outbox`, `g2p_farmer_pending_lookups`, `g2p_approval_binding_archive`, `ix_g2p_farmer_pending_lookups_state` | Crop sown and Livestock databases | idempotent `ALTER TABLE IF EXISTS ... RENAME TO ...` in the extension schema migration, run before the new code starts; back up first |
| Message keys `<old-prefix>_input_<field>[_min]` | `validation_<field>[_min]` | section user-interface schema and the translation table | the seed writes new keys and removes the old (seed wins) |
| Rule ids `<old-prefix>_field_*`, `<old-prefix>_code_choice` and one location panel | `validation_rule_*`, `validation_code_choice`, `location_widgets` | section schema, metadata seed | seed rewrite; the same seed removes old rows |
| Approval policy key `<old-prefix>.<variant>.farmer-reference.v1` | nothing live: live keys already follow OpenG2P (`registry.change_request.cropsown-farmer.default`, `registry.change_request.livestock-farmer.default`, `...verified-update-skips-review`) | tests, a Postman mock and one deferred document only | code-only change, no data migration |
| Celery task `<old-prefix>.farmer_reference.deliver_workflows`; beat entry `<old-prefix>-farmer-reference-workflows` | `farmer_reference_awe_outbox_worker`; `farmer-reference-awe-outbox-beat-producer` | Crop sown and Livestock celery | the worker registers both names for one release; beat sends the new name |
| Sender mnemonic `<old-prefix>_REFACTOR_AUDIT` | `OAN_METADATA_AUDIT` | New Dev metadata | seed |

## 4. Live identifiers (read 5 November 2026)

Live check of New Dev and staging (Partner Management table `pm_partners`, Keycloak clients, Approval Workflow
Engine table `approval_policy`): no partner id, key id, client or policy key contains the old prefix. Stage 2
therefore has no Commons data migration. The partner ids are listed in
[integration-contracts.md](integration-contracts.md), section 7.

Partner ids that do not follow one convention (stage 3, a separate plan; each is a key re-registration plus a
connector and consent change): `Crop_sown_partner_internal`, `Crop_sown_partner_local`,
`Live_stock_partner_internal`, `CropSown`, `farmer-partner`, `A2C Service`, `COOP_BANK`, `PARTNER_AGGRAGATION`
(misspelt) and the derived `PARTNER_<UPPER_SNAKE>` twins. OpenG2P leaves partner ids free and derives the registry
partner topic id as `PARTNER_<UPPER_SNAKE>`. The OAN target is a lowercase hyphenated id that says who calls whom,
for example `cropsown-registry-farmer-lookup` (Crop sown calls the Farmer search).

Test partners to remove: `synthetic-connector-*` and `POSTMAN_AGG_INTERNAL_*` (New Dev), `PARTNER_TEST_PROTEAN`
(staging).

## 5. Order of work

1. Stage 1 (names stored nowhere live): pull requests in `farmer-registry`, `oan-helm`, `cropsown-regsitry`,
   `livestock-registry`.
2. Stage 2a: code accepts old and new names (settings fallback, both event names, both celery task names, table
   rename migration).
3. Stage 2b: this repository's values switch the settings and mounts; Farmer publishes the new event; seeds write
   the new keys.
4. Stage 2c: remove fallbacks; deactivate the old topic and policy.

Each step: `develop`, then New Dev (deploys on merge), then verified, then the pull request `develop` into
`staging`.
