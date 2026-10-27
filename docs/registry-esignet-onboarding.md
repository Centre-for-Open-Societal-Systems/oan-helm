# eSignet setup for each registry

Deploying eSignet in Commons does not configure the authentication provider in
each registry database. Farmer, Crop Sown and Livestock each need an active
`g2p_registrant_authentication_providers` row for their own domain register,
plus that registry's Staff API callback in the eSignet client.

These rows and their private provider settings are **deployment data**. Do not
put them in recurring registry metadata seeds, chart defaults or Git. A seed
rerun must not replace credentials or another environment's callback. Charts
provide application configuration and secret references; they do not establish
that a registry's provider row exists.

## Local callback inventory

| Registry | Domain register | Callback |
| --- | --- | --- |
| Farmer | `a1a4d25a-1cd4-4356-abac-985a0b3c6bcd` | `http://staff-farmer-registry.openg2p.localtest.me/registrant-auth/callback` |
| Crop Sown | `6b06a95a-9a6c-5a33-a33d-c1625716c59c` | `http://staff-crop-registry.openg2p.localtest.me/registrant-auth/callback` |
| Livestock | `997676d3-7008-59f9-b23e-613ad79bbb08` | `http://staff-livestock-registry.openg2p.localtest.me/registrant-auth/callback` |

This is the local environment inventory, not production values. For another
environment discover the deployed register and its canonical Staff API host.
Register the exact callback in both the provider configuration and the eSignet
client; the Staff UI URL is not the callback. Preserve issuer, audience, signing,
PKCE and claim mapping settings supplied by the identity owner.

## Deployment administration

1. Preserve the target registry's existing provider rows and the eSignet client's
   current callback list before making an additive change. Reuse a matching
   active provider; do not create duplicate rows or overwrite conflicting
   settings without resolving their ownership.
2. Through secure deployment administration, provision the target register's
   `esignet` row using the reviewed provider configuration and its own callback.
   Private keys and client secrets must travel through secret mounts or a secure
   administrative channel, never terminal output, reports or committed SQL.
   A provider row in Farmer does not automatically configure Crop or Livestock.
3. Add the exact target callback to the authorized eSignet client. The local
   shared client is `oan-registry-intake`; retain the other registries' callbacks.
   If the identity service caches client details, invalidate only the changed
   client's entry through its deployment administration. Do not flush Redis.
4. Read back provider availability for the target register and callback membership
   without printing private settings. Starting Verify must return an authorize
   URL. A complete test must also return through the target registry's callback
   and verify the signed identity against the intended intake. An authorize URL
   alone does not prove successful identity verification.

Fayda FIN and FAN remain separate identifiers. Neither provider provisioning nor
successful verification creates an approved Farmer reference, changes identity
grants, or bypasses the separate Farmer/domain approvals.

## Local serial testing

Run Commons + Farmer + Crop, then Commons + Farmer + Livestock. Do not start
Livestock while Crop is running. Provision and verify Livestock's provider when
that runtime is started; a future setup note is not proof of a deployed row.
Provider availability, successful callback binding, source lookup and approval
acceptance are separate checks.
