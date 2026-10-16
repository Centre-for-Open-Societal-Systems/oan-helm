# Published COSS Consent candidate images

The three images tagged `dev-d6ce86b9e3f9` were manually built from COSS
`consent-management` commit `d6ce86b9e3f904ee668d913fd06835e8f70e7f64` and
published through the existing Jenkins AWS credential. Actual image digests,
source/build settings and checks are in [consent-candidate.json](../releases/consent-candidate.json).
Use the [image-only values overlay](../examples/dev/consent-image-values.yaml)
when preparing the existing Commons release. It does not enable Aggregation,
subject-consent policy changes, beneficiary routing or the prepared signing key.

## Build adjustments

The COSS API Dockerfile defaults to framework ref `1.2.0`. Building it as-is
failed image import checks: Consent imports
`openg2p_fastapi_common.utils.crypto`, absent in that framework release. The API
candidate instead pins framework commit
`164f07f7e7f38944b60cb1528d2582d025b830b5`, which supplies that module. Its runtime
layer explicitly installs `SQLAlchemy[asyncio]==2.0.54` and `greenlet==3.5.6`.
Without greenlet, the source Dockerfile image failed the runtime import check.
Application source and application CI files were not edited.

Example build recipe (run from a clean checkout of the exact COSS commit):

```sh
docker build --platform linux/amd64 \
  --build-arg FASTAPI_COMMON_REF=164f07f7e7f38944b60cb1528d2582d025b830b5 \
  --label org.opencontainers.image.source=https://github.com/Centre-for-Open-Societal-Systems/consent-management \
  --label org.opencontainers.image.revision=d6ce86b9e3f904ee668d913fd06835e8f70e7f64 \
  -f docker/consent-manager-api/Dockerfile \
  -t coss-consent-api-source-build:d6ce86b9e3f9-framework-164f07f .
```

The runtime Dockerfile used after that source build:

```dockerfile
FROM coss-consent-api-source-build:d6ce86b9e3f9-framework-164f07f
RUN pip install --no-cache-dir "SQLAlchemy[asyncio]==2.0.54" "greenlet==3.5.6"
```

Build this runtime layer under the API target tag. UI uses `ui/Dockerfile` with
context `ui/`; sanity uses `docker/consent-manager-sanity/Dockerfile` with the
repository root context. All images override OCI source/revision labels to the
COSS repository and exact source commit. The UI also receives `GIT_COMMIT` and
`BUILD_TIME` build arguments. Keep the recorded digests as deployment references:
base tags and other unpinned package inputs mean a future rebuild need not
produce identical bytes. Existing ECR repositories are mutable; the publication
checked that these tags were unused and did not overwrite existing images.

Aggregation's already-published candidate uses a different framework commit,
`2926e24b19fb04dba31b40d326d6ad59b2ad30b7`. Each container carries its own runtime;
framework pins need not match. The exact published pair subsequently passed
[30 isolated HTTP/database checks](consent-aggregation-local-check.md).

## Verification and remaining work

Checks in disposable containers without networking passed:

- API imports, async dependencies, strict subject-consent settings, OTP response
  fields, all six CM endpoint paths required by Aggregation in generated OpenAPI,
  signing operation and public JWKS generation.
- Separate staff/partner/beneficiary schema checks confirmed expected route
  presence and exclusion of another audience's route.
- UI TypeScript/Vite build, compiled index and nginx configuration.
- Sanity image collection of seven tests. Those tests were **not executed**
  against services.

ECR `DescribeImages` digests match each local image manifest. The subsequent
[local pair check](consent-aggregation-local-check.md) ran fresh-database migrations,
approval, OTP, filtering, withdrawal, denial and replay scenarios: **30/30 passed**.
It used authentication disabled, an all-audience Consent API and source-owned
PM/registry/callback stand-ins. Existing-database upgrades, Keycloak authorization,
split routing and live service interoperability remain unverified.
Keep Aggregation disabled and complete
[runtime prerequisites](consent-aggregation-prerequisites.md). Pull access is
being handled separately by the environment owner; it has not been reverified.
