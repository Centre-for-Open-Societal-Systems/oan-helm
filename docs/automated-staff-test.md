# Automated new-dev staff regression

The saved collection is
[`COSS-Automated-Staff.postman_collection.json`](../postman/COSS-Automated-Staff.postman_collection.json).
It tests the real development Aggregation service and all three real registry
staff APIs, plus Consent routing and access rejection. No application deployment
or chart upgrade is performed. It does not establish the partner OTP workflow.

On the authorized operator workspace, run this existing private launcher:

```powershell
py D:\WORK\Protean\Temp\consent-aggregation-rancher-20261019\e2e-test-kit\run-automated-test.py
```

`Run-Automated-Test.cmd` and `Run-Automated-Test.ps1` in that directory run the same
test. No browser sign-in, token copying, ID selection or Postman imports are
needed. Exit 0 means every required scenario executed and every assertion passed.
Prerequisite or assertion failures exit nonzero. The local launcher uses the
already authorized Jenkins/SSH transport; it does not contain its credentials.

Every run:

1. Checks the expected new-dev issuer and Aggregation route before preparation.
2. Creates/verifies three dedicated confidential service clients: viewer, peer
   viewer and a caller without that role. Password and browser grants are off.
   Viewer accounts have only `AGGREGATION_STAFF_VIEWER`; they receive no registry
   client roles or Consent admin permissions. Human accounts are untouched.
3. Obtains short-lived tokens through client credentials on the server. Secrets
   stay on the server. An ephemeral RSA/AES-GCM envelope protects the tokens in
   transit through Jenkins; the private key exists only in the local process.
4. Creates/verifies the four deterministic fixture rows in
   [`staff-e2e-fixtures.json`](../postman/staff-e2e-fixtures.json): Farmer, CropSown,
   and Livestock's Farmer and Livestock registers. The subject is
   `OAN-E2E-UIN-0001`, with `created_by=oan-aggregation-e2e`, deterministic UUIDs,
   technical labels, and no contacts, biographic attributes, images or geography.
   SQL prepares already-approved read fixtures, independently of the registry's
   separate change-request/approval workflow. It is not an approval-flow test.
5. Refuses collisions or changed fixture values. Inserts are transactional per
   database with `ON CONFLICT DO NOTHING`; existing rows are never updated. A
   partial setup can be rerun. Server preparation evidence is retained under
   `/var/lib/oan-aggregation-development/e2e/last-preparation.json`.
6. Updates the private Postman environment with tokens, expiry and subject, then
   runs the complete saved collection with cloud run events disabled. The token
   now represents `service-account-oan-aggregation-e2e`, rather than a human.
7. Saves sanitized `report.json`, setup hashes and detailed private CLI output
   beneath `e2e-test-kit/runs/<UTC timestamp>/`. The top-level `report.json` holds
   the latest outcome, including setup failures, and `last-run.json` points to
   its run directory. Windows ACLs on that private directory allow the operator and
   SYSTEM. Never publish the environment or detailed responses.

The fixtures and clients remain for inspection and reruns. Do not remove records
from another test suite or the `sanity-e2e` user. Remove these dedicated clients
and only these deterministic fixture IDs/owner markers when retiring this test;
preserve audit history according to the environment's retention policy.

## Assertions

- Public health/catalog and Consent UI/partner routing; internal service URLs
  stay out of the public catalog.
- Missing/invalid tokens return 401; a valid caller lacking the viewer role gets
  403. An Aggregation viewer cannot administer Consent.
- Missing identifiers and unknown registries are rejected.
- An absent synthetic ID and an inexact substring produce complete `not_found`
  results from every registry, with no hidden registry errors.
- The exact ID returns precisely the four expected UUIDs and functional IDs,
  complete results and a fresh search ticket.
- Every offered tab is opened from its returned request body. Assertions check
  schema, record/ticket binding, section/field shape, fixture values, pagination,
  execution count and visibility of every expected root fixture. Every returned
  row must belong to the marked fixture set; unexpected data fails the test.
- A second viewer cannot reuse the first viewer's ticket. Tampered tickets,
  changed record IDs and unknown tabs are rejected.

Initial live result on 19 October 2026: **107/107 assertions, 39 requests, 20
scenarios and 20 tabs passed**. Repeated preparation inserted zero duplicates.
These results exercise service authentication and synthetic reads, not human
browser login, change-request approvals, deployment or load/availability behavior.

## Consent partner flow remains a separate prerequisite

`report.json` explicitly marks the combined partner/Consent/registry test blocked
until partner realm/client claims, reviewed bindings/PM signing-key registration
and SMS delivery are configured. OTP remains disabled as requested. Health and
access-denial checks do not prove consent issuance, withdrawal, expiry, signed
partner responses or callbacks. No existing policy is weakened for this test.

For another authorized runner, provide the same private environment to:

```powershell
py scripts/run-staff-e2e.py --environment <private-environment.json> --output <private-report-directory>
```

That lower-level command does not refresh tokens or provision fixtures. Use the
operator launcher for a complete unattended run. Public artifacts contain no
client secrets, bearer tokens or live personal records.
