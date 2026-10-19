# OAN Consent and Aggregation local image-pair check

> Historical image-pair evidence. For current dev.5 images and prerequisites, see
> [the current setup guide](consent-aggregation-prerequisites.md).

The exact published Consent API and Aggregation API candidates passed **30/30**
source-owned end-to-end checks on 16 October 2026. Both applications ran as real
containers with separate fresh PostgreSQL databases. Their migrations ran before
the checks. [Sanitized evidence](../releases/consent-aggregation-integration.json)
records image digests, source revision, suite checksum and limits.

| Application | Source / published candidate |
| --- | --- |
| OAN Consent Manager | COSS `consent-management` at `d6ce86b9e3f904ee668d913fd06835e8f70e7f64`; [exact image records](../releases/consent-candidate.json) |
| OAN Aggregation API | COSS `oan-aggregation-api` at `8fe3bf97030bb0b3f6283c2123ad58026af6cc50`; [exact image record](../releases/aggregation-candidate.json) |

The checks cover discovery, invalid query/subject/section rejection, OTP consent,
registry search, bene360 response schema, field/scope filtering, approval polling,
withdrawal, denial, and replay-window expiry/re-seek. Postman simulation recorded
14 calls to the HTTP dependency stand-ins.

Partner Management keys, registry results and partner callbacks came from the
Aggregation repository's versioned `test/e2e/fakes.py`, reused as the owner's
fixture rather than inventing a separate service contract. A local Postman
[simulation](../postman/simulations/consent-aggregation.sim.yaml) routes those
calls through a [fixture adapter](../postman/mocks/aggregation-fixtures/default.js).
Unmodeled endpoints return 501. The application pair itself is not mocked.

The first run passed 28/30: the harness serialized YAML with sorted keys and
changed the catalog scope order. Preserving the source order fixed the harness;
the unchanged source scenarios then passed 30/30 against fresh databases.

## Repeat locally

Use Windows Docker Desktop with Linux containers, Python 3.12+, PyYAML and
Postman CLI 1.73+. Have the two exact candidate images available locally or
authenticate Docker to ECR using your authorized credentials. Also pull
`postgres:16`; the runner records its resolved digest. A clean Aggregation
checkout must be at the exact source revision above. Ports 18900, 18901, 18909
and 18910 must be free.

```powershell
py -m pip install -r requirements.txt
docker pull postgres:16
py scripts/verify-consent-aggregation.py --aggregation-source D:/path/to/oan-aggregation-api
```

The harness builds a separate test-tooling image, creates a uniquely named
Docker network, databases and ephemeral test keys, and runs the source-owned
`test/e2e/e2e.py` unchanged. It changes only test endpoint URLs and preserves
catalog ordering. It removes its containers/network and stops its own Postman
process on exit. Diagnostic logs and test keys stay in ignored `.build/`; do not
publish raw request logs or use these keys in an environment. No Postman cloud
upload, Kubernetes access, IAM changes or application CI changes are involved.

## What still requires environment verification

This run used authentication disabled, an all-audience Consent API, debug OTP,
and source-owned PM/registry/callback stand-ins. It did not test Keycloak roles,
Istio split staff/partner/beneficiary routing, AWE, Kafka, real SMS, live registry
contracts, an existing database upgrade or cluster ECR pull permissions. The
separately built UI and sanity image were not part of this pair run.

Keep Aggregation disabled until the [runtime prerequisites](consent-aggregation-prerequisites.md)
are prepared. Select the candidate image overlays explicitly; chart version
`1.0.0-dev.3` changes OAN identity metadata and embedded documentation while
retaining `1.0.0-dev.2` runtime defaults. Helm rollback cannot undo migrations.
