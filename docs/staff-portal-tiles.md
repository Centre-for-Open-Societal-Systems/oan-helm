# Staff portal application tiles

The staff portal reads `GET /user-access/get_staff_portal_applications` from
its configured IAM. A Git merge does not publish a tile: an owning deployment
must register the application catalog. The mnemonic must match the Keycloak
client ID used for the application's roles. Registered applications without
client roles in the current user's token appear disabled; assign approved
roles in IAM/Keycloak and sign in again to refresh the staff session.

## Consent Manager

Enable `consentStaffPortalTile.enabled` in the existing Commons Services release
when the Consent UI is enabled. The development overlay enables it. Its
post-install/upgrade Job uses the existing `consent-manager` service credentials
from the namespace-local Secret, posts only that application's IAM catalog and
maps the existing `CONSENT_MANAGER_ADMIN` and `CONSENT_MANAGER_APPROVER` roles.
It does not create users, assign roles or change Keycloak clients. The tile
opens the Consent staff console, not the partner portal or partner API.

The URL is derived from `openg2p-consent-manager.global.consentManagerHostname`.
IAM URL, token endpoint, client ID, Secret reference, image and tile order are
Helm values under `consentStaffPortalTile`. Keep the mnemonic/client ID aligned
with the existing Consent authorization configuration. Never commit tokens or
client secret values. The selected IAM must trust the token's issuer.

The registration is an idempotent upsert. Failures stop the Helm hook rather
than reporting an installed-but-unregistered tile. Rehearse install, rerun and
failure recovery against the intended environment before a Commons upgrade;
retain the existing release, private values and unrelated image/resource pins.
Default installations keep this optional Job disabled. Dev.8 adds this feature
without modifying any previously published chart archive.

## Registry dashboards

Each owning registry chart deploys its UI and runs the dashboard image's
`iam/keycloak-setup.mjs` followed by `iam/register.mjs`. These register a tile
under `farmer-registry-dashboard`, `cropsown-registry-dashboard` or
`livestock-registry-dashboard`; staff require that client's `Dashboard Viewer`
role. The UI BFF uses a separate service identity for chart API calls.

The UI/API source PRs were merged on 21 October. At the live read-only check,
the three registry delivery PRs remained open and none of the three dashboard
UIs was deployed. IAM therefore had no registry-dashboard entries. Complete
the owning registry build/deployment and its IAM and authenticated-chart smoke
hooks; do not register dead links as proof of a working dashboard. Existing
Farmer ownership/image-only and hook-rehearsal gates remain mandatory.

Use the central `staff-portal.development.oanstaging.com` and shared development
IAM cookie domain `.development.oanstaging.com`; the registry overlays own
these addresses. Dashboard routes use the existing `istio-system/development`
Gateway without taking ownership of it.

## Verification

After rollout, sign in to the central staff portal with an approved account.
Confirm the tile label and URL, enabled state for assigned users, disabled
state for unassigned users and the destination's own authorization. A tile or
an open health endpoint alone does not prove dashboard chart access. No default
staff grants are added by this integration.

The dev.8 package excludes Python bytecode caches from both source seals and
chart archives. Test imports therefore do not change package provenance on
another Python version or checkout. Earlier archives remain unchanged.
