# eSignet (Fayda) sign-in for a registry

Deploying eSignet in Commons does not by itself let a registry verify a
registrant. Each registry needs two rows that no seed writes: an active
`g2p_registrant_authentication_providers` row for its domain register, and its
Staff API callback among the redirect URIs of the OIDC client in eSignet. Both
are chart configuration.

## Registry side: `registrantAuth`

The farmer chart (`charts/openg2p-farmer-registry`, values `registrantAuth`) has
a post-install/post-upgrade hook that:

1. ensures the client's RSA key exists in the Secret `registrantAuth.keySecret`
   (generated on first run, reused after; never printed or committed) and
   derives its public JWK;
2. upserts the provider row for `registrantAuth.registerId`: adapter `esignet`,
   the eSignet endpoints under `esignetBaseUrl`, `private_key_jwt` with the PEM
   key as text bytes (what iam_core expects), the callback, and a provider
   configuration with the issuer, the client id as audience, the canonical token
   URL as `jwt_assertion_aud`, and the `individual_id` and `name` userinfo claims
   marked essential;
3. upserts the shared `oan-registry-intake` client in eSignet's database, with
   this registry's callback added to the redirect URIs the other registries
   already registered.

Per environment, set `registrantAuth.enabled`, `esignetBaseUrl` (the public
eSignet URL) and `callbackUrl` (`https://<staff api host>/registrant-auth/callback`).
New Dev: `environments/dev/values/farmer.yaml`. The register must carry
`requires_registrant_authentication`, which the OAN metadata seed sets.

The hook runs in the registry namespace with that namespace's copy of the
Commons PostgreSQL Secret, so it needs no access to Commons pods. eSignet caches
client details in its Redis after first use; when an existing client's name or
redirect URIs change, restart it:
`kubectl -n commons rollout restart deployment commons-services-esignet`.

Crop Sown and Livestock get the same block when their charts adopt it; the
client is shared and each registry adds only its own callback.

## Commons side: identities and PIN

Sign-in on New Dev uses the mock identity system. Two things decide whether a
tester can sign in:

- `mock-identity-system.identitySeed.defaultPin` must be 4 digits. eSignet's
  auth-challenge rule for PIN is length 4; the subchart default `222222` is
  refused. New Dev sets `"2222"`.
- People must exist. `identitySeed` loads Master Data's `g2p_sample_individuals`;
  where that table is empty (New Dev), `mockIdentities.people` lists the test
  people explicitly and `templates/mock-identities.yaml` creates them once
  through the identity API (no update exists: a changed person must be removed
  first). New Dev lists the people on the mock Fayda page, all with PIN 2222.

## Checking

Without printing private settings: the provider count for the register is 1,
the client's redirect URIs include the callback, and starting *Verify with
Fayda* in the intake returns an authorize URL. The complete proof is a sign-in
that returns through `/registrant-auth/callback` and binds the signed identity to
the intake; an authorize URL alone is not it. FIN and FAN remain separate
identifiers; verification neither approves a farmer nor changes identity grants.
