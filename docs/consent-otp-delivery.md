# Consent Manager OTP delivery (AWS bucket, Garage bucket, OAN SMS and 8028 SMS)

Where the consent OTP goes, how to switch it, and what has to exist outside Git for each
choice. Applies to `openg2p-commons-services` (`openg2p-consent-manager.consentManagerApi`).

**New Dev today:** each OTP is written as a JSON object to the bucket `a2c-webhook` on
**AWS S3 (ap-south-1)**, the A2C OTP bucket. SMS through OAN is built but off.
Garage is the alternative for environments that keep their own object store.

## Why this changed

On 20 Nov 2026 the object store in New Dev moved from MinIO to Garage. Consent Manager
still pointed at the removed MinIO service for its OTP test copy, with the old MinIO keys.
An OTP that cannot be written is **not** an error: the request is accepted and only the log
line `OTP publisher: could not write ...` appears. So the symptom was "consent raised, no
OTP anywhere". The OTP test copy now goes to the A2C bucket on AWS, which already has the
`otp/` prefix and a browser page.

## What changed

| File | Setting | Before | Now |
|---|---|---|---|
| `environments/dev/values/commons-services.yaml` | `CONSENT_MANAGER_OTP_PUBLISH_ENDPOINT_URL` | Garage `http://commons-garage...:3900` | `''` (empty means AWS) |
| `environments/dev/values/commons-services.yaml` | `CONSENT_MANAGER_OTP_PUBLISH_REGION` | chart default `us-east-1` | `ap-south-1` |
| `charts/openg2p-commons-services/values.yaml` | `CONSENT_MANAGER_OTP_PUBLISH_ENDPOINT_URL` (chart default) | `http://commons-minio...:9000` | `http://commons-garage.commons.svc.cluster.local:3900` |
| `charts/openg2p-commons-services/values.yaml` | `CONSENT_MANAGER_OAN_DELIVERY_ENABLED` | not set | `'false'` |
| `charts/openg2p-commons-services/values.yaml` | `CONSENT_MANAGER_OAN_BASE_URL` | not set | `''` |
| `charts/openg2p-commons-services/values.yaml` | `CONSENT_MANAGER_OAN_PHONE_RESOLVER` | not set | `map` |
| `charts/openg2p-commons-services/values.yaml` | `CONSENT_MANAGER_OAN_TOKEN` | not set | Secret `oan-caller-dpi-consent`, key `token` (optional) |
| `charts/openg2p-commons-services/values.yaml` | `CONSENT_MANAGER_OAN_OTP_PHONE_MAP` | not set | Secret `consent-manager-otp-dev`, key `oan-phone-map` (optional) |
| `releases/resource-baselines-current.json` | `openg2p-commons-services` Secret references | 42 | 44 (the two optional OAN references) |

The bucket name stays `a2c-webhook` and `OTP_PUBLISH_ENABLED` stays `'true'`. No chart
version, `CHANGELOG.md` or other `releases/` file is edited by hand; the release script does
that after the PR merges.

## Choosing where the OTP goes

The code is in the consent-management repository (`services/otp_provider.py`,
`otp_delivery.py`, `otp_publisher.py`; SMS added in PR #16).

| Goal | `OTP_PUBLISH_ENABLED` | `OTP_PUBLISH_ENDPOINT_URL` | `OAN_DELIVERY_ENABLED` |
|---|---|---|---|
| AWS bucket (New Dev now) | `'true'` | `''`, region `ap-south-1` | `'false'` |
| Garage bucket | `'true'` | `http://commons-garage...:3900` | `'false'` |
| SMS only | `'false'` | n/a | `'true'` and `OAN_BASE_URL` set |
| Neither | `'false'` | n/a | `'false'` |

When SMS is switched on and complete (enabled, base URL and token all set), the code is sent
by SMS **instead of** being written to the bucket, even if `OTP_PUBLISH_ENABLED` is `'true'`.
Set it to `'false'` when moving to SMS so the configuration says what happens.

A code that cannot be sent by SMS is refused to the caller (422 no phone, 502 refused, 503
unavailable, 500 misconfigured). The bucket copy never refuses: it only logs a warning.

## SMS straight to the 8028 gateway

A second SMS transport for the consent OTP, with no OAN Messaging Service in between
(consent-management PR #17). Everything is set through this chart; nothing is set on the
cluster by hand.

| What | Where |
|---|---|
| Switch | `CONSENT_MANAGER_SMS8028_ENABLED` (`'false'` in the chart, `'true'` in `environments/dev/values/commons-services.yaml`) |
| Gateway URL | `CONSENT_MANAGER_SMS8028_BASE_URL`, default `https://8028.et:3400/sms-api/v1` |
| Client secret, client certificate and key | Secret **`consent-sms8028`**, keys `client-secret`, `client.crt`, `client.key` (all optional references: the pod starts without them and 8028 delivery stays off) |
| Test number | Secret `consent-manager-otp-dev`, key `oan-phone-map`: JSON `{"<FIN>": "09XXXXXXXX"}` (personal data, so a Secret) |

It applies to both Consent Manager API deployments (`cm-api` and `cm-partner-api`, which is the
one that raises requests). Never enable it together with `OAN_DELIVERY_ENABLED`: the code would
be sent twice, so the Consent Manager refuses that combination.

### Behaviour (from the 8028 Integration Guide v1.1)

- One `POST /sms/send-sms` per code, with mutual TLS (the certificate 8028 registered for us,
  by CN and SHA-256 fingerprint) **and** the client secret in the body. HTTP 201 means queued,
  not delivered; 8028 sends status callbacks to the one URL registered with it, so this path
  confirms "queued" and the handset, not delivery.
- 8028 has no idempotency key. A request that may have reached it is **never repeated**: a
  timeout after the write, any 5xx or an unreadable answer is not retried (503
  `otp_delivery_unavailable`, and it counts against the resend budgets). Only "nothing was
  sent" (connection refused, DNS, TLS handshake) is retried. HTTP 401 means the secret is wrong
  or the certificate is not registered.
- When it is on and complete, the code is sent by SMS instead of being written to the bucket.
  When it is on but the Secret is missing or incomplete, the Consent Manager does not send by
  SMS and falls back to the bucket copy while `OTP_PUBLISH_ENABLED` is `'true'`.
- Outbound TCP 3400 to `8028.et` must be allowed, and 8028 must accept the environment's egress
  IP (New Dev: `13.201.58.55`).

### Creating the Secret (once, not in Git)

From the files 8028 supplied (never paste them into a chat, a ticket or Git):

```
kubectl -n commons create secret generic consent-sms8028   --from-literal=client-secret="$(cat <file holding the client secret>)"   --from-file=client.crt=<client certificate PEM>   --from-file=client.key=<client private key PEM>
```

The certificate and key are loaded from memory at the first send and are never written to the
image. After 8028 issues a new certificate, register it with them first, then replace the
Secret and restart `cm-api` and `cm-partner-api`.

## New Dev: the AWS bucket

Bucket `a2c-webhook`, region `ap-south-1`. Objects: `otp/<UTC time>_<id>.json`, with
`otp`, `individualId`, `individualIdType` (FIN), `transactionID`, `requestId`. The key
format is A2C's, so A2C reads it unchanged. The bucket's website root shows a bucket browser
page; `otp/` already exists, so no folder has to be created (S3 creates the prefix with the
first object).

### Warning: this bucket is public

Listing and reading of this bucket needs no login (checked with anonymous requests). Every
OTP object holds the **code in plain text next to the FIN**, so anyone who knows the URL can
read a live code. Use it only with **test subjects**. Do not raise consents for real
farmers' FINs while OTP publishing to this bucket is on. A private bucket or SMS is the way
to production.

### What devops adds (not in Git)

1. **An IAM user** for Consent Manager with only this permission:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ConsentOtpPublish",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::a2c-webhook/otp/*"
    },
    {
      "Sid": "OptionalStartupCheck",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::a2c-webhook"
    }
  ]
}
```

   The second statement only silences a start-up warning (Consent Manager checks the bucket
   exists). Writing works without it.
2. **Put that IAM user's keys in Secret `consent-manager-otp-dev`** in the `commons`
   namespace: `minio-access-key` = access key ID, `minio-secret-key` = secret access key.
   The key names say "minio" for historical reasons and are unchanged. `otp-salt` stays as it
   is. Never put the keys in Git, chat, Jira or Confluence.
3. **Outbound HTTPS** from the `commons` namespace to `s3.ap-south-1.amazonaws.com`.
4. **Upgrade the `openg2p-commons-services` release** (Rancher or `helm upgrade`) so the
   overlay values apply. The Consent Manager Jenkins deploy only changes images and keeps the
   other values (`--reuse-values`), so it does not apply this change. Then restart `cm-api`
   so it reads the new Secret.

### Test it

1. Raise an OTP consent for a **test** subject through the partner API
   (`POST /consent/v1/partner-portal/consent-requests` with `"method": "otp"`).
2. Open the bucket in the AWS console, or in the A2C bucket browser page (ask the A2C team
   for its address), and look under `otp/`. The newest object (the name starts with the UTC time) holds the code for that request.
3. Submit the code to `POST .../consent-requests/{id}/verify-otp`; the consent becomes active.
4. No object appears: read the log line (see "Check it").

### Roll back

Set the overlay back to `CONSENT_MANAGER_OTP_PUBLISH_ENDPOINT_URL:
http://commons-garage.commons.svc.cluster.local:3900` and remove the region line, or set
`CONSENT_MANAGER_OTP_PUBLISH_ENABLED: 'false'`, and upgrade the release.

## Where the OTP can be seen

There is no API that returns an OTP, by design. Only the hash is stored.

- **Bucket (AWS or Garage):** the object described above. Garage has no console; use an S3
  client with the keys from Secret `commons-minio`.
- **SMS:** the subject's phone. Test numbers come from the `oan-phone-map` secret key.
- **Request status:** `GET /consent/v1/partner-portal/consent-requests/{id}` shows
  `otp_channel`, `otp_expires_at` and `otp_attempts_left`, never the code.

## What must exist outside Git

1. **AWS bucket (New Dev):** see "What devops adds" above.
2. **Garage bucket (instead of AWS):** bucket `a2c-webhook` created in Garage, and the key in
   `consent-manager-otp-dev` given **read and write** on it (`garage bucket allow --read
   --write a2c-webhook --key <key>`). Garage permissions are per key and per bucket; a key
   without them gets `AccessDenied`, and one that cannot create buckets gets `NoSuchBucket`.
3. **SMS only:**
   - Secret `oan-caller-dpi-consent` with key `token` (the OAN caller credential issued by the
     OAN operator; the name the OAN test setup already uses).
   - Key `oan-phone-map` in `consent-manager-otp-dev`, JSON `{"<FIN>": "<phone>"}`, for dev
     and staging test numbers. It is a Secret key because phone numbers are personal data.
   - `OAN_BASE_URL` must be `https`, no path. Both references are optional, so the pod starts
     without them while SMS is off.
4. **Image:** the running consent image must include the SMS change (consent-management
   PR #16). An older image ignores the `OAN_*` settings.

## Check it

```bash
# which image is running
kubectl -n commons get deploy -o wide | grep cm-api

# what the pod got (names and flags only; do not print the secrets)
kubectl -n commons exec deploy/<release>-cm-api -- env | grep -E "OTP_PUBLISH_(ENABLED|ENDPOINT|BUCKET|REGION)|OAN_DELIVERY_ENABLED"

# what happened after raising a consent
kubectl -n commons logs deploy/<release>-cm-api --since=30m | grep -i otp
```

| Log line | Meaning |
|---|---|
| `OTP publisher: wrote otp/... to bucket` | Written to the bucket. |
| `... could not write ... AccessDenied` | AWS: the IAM user lacks `s3:PutObject` on `a2c-webhook/otp/*`. Garage: the key has no permission on the bucket. |
| `... could not write ... InvalidAccessKeyId` or `SignatureDoesNotMatch` | The keys in `consent-manager-otp-dev` are wrong or still the old MinIO keys. |
| `... could not write ... NoSuchBucket` | Garage: the bucket does not exist. |
| `... could not write ... EndpointConnectionError` | No route to the endpoint (AWS egress blocked, or a wrong endpoint). |
| `OTP handed to OAN for consent request ...` | Sent by SMS. |
| 422 `otp_destination_unknown` | SMS is on but the subject has no entry in the phone map. |
| 503 `otp_unavailable` | Neither bucket publishing nor SMS is on, so no code can be delivered. |

For a quick look in dev only, `CONSENT_MANAGER_OTP_LOG_CODES: 'true'` writes the code to the
service log. Turn it off again: anyone who can read the log can use the code.

## What has been verified, and where

Verified:

- Consent OTP unit tests (SMS text, OAN client, delivery): 14 pass. The 33 integration tests
  need Postgres and were skipped.
- The OTP publisher against a **real Garage** (local container) using these variable names:
  with a key that has read and write on the bucket the object is written under `otp/`; a key
  with no bucket, or no permission on it, writes nothing and only logs a warning.
- The AWS bucket exists, the `otp/` prefix exists, and anonymous listing works (anonymous
  GET requests only; no object content read).
- `helm template` of the chart with the New Dev overlay renders, in every Consent Manager
  container, `OTP_PUBLISH_ENDPOINT_URL=""`, `OTP_PUBLISH_REGION=ap-south-1`,
  `OTP_PUBLISH_ENABLED=true` and bucket `a2c-webhook`. `scripts/validate.py --package` passes.
- **SMS flow, on the OAN test cluster (`registry-test`, namespace `consent-sms`), not New
  Dev:** consent image `oan-sms` runs with `OAN_DELIVERY_ENABLED=true`, an https
  `OAN_BASE_URL`, the token from `oan-caller-dpi-consent` key `token`, and a phone map. Its
  log shows `OTP handed to OAN for consent request ... (message ...)`, against the fake OAN
  gateway.

**Not verified. Confirm each on New Dev before relying on it:**

- A **write to the AWS bucket** from Consent Manager, and the IAM policy above (no AWS
  credentials were available).
- That New Dev pods can reach `s3.ap-south-1.amazonaws.com`.
- That A2C in New Dev reads OTPs from this AWS bucket. The previous overlay comment said
  A2C reads `a2c-webhook` from Garage; confirm with the A2C team before merging, and use the
  Garage setting above if so.
- The keys currently in `consent-manager-otp-dev`, and which consent image is running.

## Open items

- Other docs (`docs/rancher-dev.md`, `docs/rancher-consent-aggregation-status.md`) still say
  OTP bucket publishing is disabled pending SMS; the chart default has it on.
- The bucket is public and holds live codes with FINs. Test subjects only until the bucket is
  private or SMS replaces it.
- The phone map is for test numbers. Production needs a phone resolver approved by the
  identity owner, plugged in at `resolve_phone` in `otp_delivery.py`.
- A failed bucket write is only a warning. If it should fail the request, that is a
  consent-management code change.
- `pytest-asyncio` is missing from consent-management's `[test]` extras.
