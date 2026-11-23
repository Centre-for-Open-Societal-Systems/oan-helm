# Consent Manager OTP delivery (Garage bucket and OAN SMS)

Where the consent OTP goes in New Dev, how to switch it, and what has to exist
in the cluster for each choice. Applies to `openg2p-commons-services`
(`openg2p-consent-manager.consentManagerApi`).

## Why this changed

On 20 Nov 2026 the object store in New Dev moved from MinIO to Garage
(`commons-garage`, S3 API on port 3900). Consent Manager still pointed at the
removed MinIO service for its OTP test copy, and its upload credentials were
the old MinIO keys. An OTP that cannot be written is **not** an error: the
request is accepted and only the log line `OTP publisher: could not write ...`
appears. So the symptom was "consent raised, no OTP anywhere".

## What changed

Only `charts/openg2p-commons-services/values.yaml`, in the
`openg2p-consent-manager` → `consentManagerApi` block:

| Setting | Before | Now |
|---|---|---|
| `CONSENT_MANAGER_OTP_PUBLISH_ENDPOINT_URL` | `http://commons-minio.commons.svc.cluster.local:9000` | `http://commons-garage.commons.svc.cluster.local:3900` |
| `CONSENT_MANAGER_OAN_DELIVERY_ENABLED` | not set | `'false'` |
| `CONSENT_MANAGER_OAN_BASE_URL` | not set | `''` |
| `CONSENT_MANAGER_OAN_PHONE_RESOLVER` | not set | `map` |
| `CONSENT_MANAGER_OAN_TOKEN` | not set | from Secret `oan-caller-dpi-consent`, key `token` (optional) |
| `CONSENT_MANAGER_OAN_OTP_PHONE_MAP` | not set | from Secret `consent-manager-otp-dev`, key `oan-phone-map` (optional) |

No chart version, `CHANGELOG.md` or `releases/` file is edited by hand; the
release script does that after the PR merges.

## Choosing where the OTP goes

The code is in the consent-management repository (`services/otp_provider.py`,
`otp_delivery.py`, `otp_publisher.py`; SMS added in PR #16).

| Goal | `OTP_PUBLISH_ENABLED` | `OAN_DELIVERY_ENABLED` |
|---|---|---|
| Garage bucket only (current dev, A2C reads it) | `'true'` | `'false'` |
| SMS only | `'false'` | `'true'` and `OAN_BASE_URL` set |
| Neither | `'false'` | `'false'` |

When SMS is switched on and complete (enabled, base URL and token all set), the
code is sent by SMS **instead of** being written to the bucket, even if
`OTP_PUBLISH_ENABLED` is `'true'`. Set it to `'false'` when moving to SMS so the
configuration says what happens.

A code that cannot be sent by SMS is refused to the caller (422 no phone, 502
refused, 503 unavailable, 500 misconfigured). The bucket copy never refuses:
it only logs a warning.

## Where the OTP can be seen

There is no API that returns an OTP, by design. Only the hash is stored.

- **Garage bucket:** object `a2c-webhook/otp/<UTC time>_<id>.json` with
  `otp`, `individualId`, `individualIdType` (FIN), `transactionID`,
  `requestId`. A2C reads the newest object for a FIN holder. Garage has no
  console; use an S3 client with the keys from Secret `commons-minio`, or a
  presigned link.
- **SMS:** the subject's phone. Test numbers come from the `oan-phone-map` secret key.
- **Request status:** `GET /consent/v1/partner-portal/consent-requests/{id}`
  shows `otp_channel`, `otp_expires_at` and `otp_attempts_left`, never the code.

## What must exist in the cluster (not in Git)

Secrets are never committed (see CONTRIBUTING). Create or update them in the
`commons` namespace:

1. **`consent-manager-otp-dev`**: `minio-access-key` and `minio-secret-key`
   must hold the **Garage** keys (the same keys as Secret `commons-minio`),
   `otp-salt` is unchanged.
2. **Garage bucket `a2c-webhook`** exists. Consent Manager tries to create it
   at start-up and only logs a warning if it cannot.
3. **Region:** `CONSENT_MANAGER_OTP_PUBLISH_REGION` (`us-east-1`) must match the
   Garage region setting, or uploads are rejected as a signature error.
4. **For SMS only:**
   - Secret `oan-caller-dpi-consent` with key `token` (the OAN caller credential
     issued by the OAN operator). This is the name the OAN test setup already uses.
   - Key `oan-phone-map` in `consent-manager-otp-dev`, JSON `{"<FIN>": "<phone>"}`, for
     dev and staging test numbers. It is a Secret key, not a plain value, because phone
     numbers are personal data.
   - `OAN_BASE_URL` must be `https`, no path.
   - Both references are optional, so the pod starts without them while SMS is off.
5. **Image:** the running consent image must include the SMS change (consent-management
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
| `OTP publisher: wrote otp/... to bucket` | Written to Garage. |
| `OTP publisher: could not write ...` | Wrong endpoint, keys, bucket or region. |
| `OTP handed to OAN for consent request ...` | Sent by SMS. |
| 422 `otp_destination_unknown` | SMS is on but the subject has no entry in the phone map. |
| 503 `otp_unavailable` | Neither Garage publish nor SMS is on, so no code can be delivered. |

For a quick look in dev only, `CONSENT_MANAGER_OTP_LOG_CODES: 'true'` writes
the code to the service log. Turn it off again: anyone who can read the log can
use the code.

## What has been verified, and where

Verified:

- Consent OTP unit tests (SMS text, OAN client, delivery): 14 pass. The 33
  integration tests need Postgres and were skipped.
- The OTP publisher against a local S3-compatible server using these same
  variable names: object written under `otp/`, path-style URL, bucket created,
  payload as above. With an unreachable endpoint nothing is written and only a
  warning is logged.
- `values.yaml` parses and every `CONSENT_MANAGER_*` name maps to a real
  consent setting.
- **SMS flow, on the OAN test cluster (`registry-test`, namespace `consent-sms`), not New Dev:**
  the consent image `oan-sms` runs with `OAN_DELIVERY_ENABLED=true`, an https
  `OAN_BASE_URL`, the token from `oan-caller-dpi-consent` key `token`,
  `OTP_PUBLISH_ENABLED=false`, `OTP_LOG_CODES=false` and a phone map. Its log shows
  `OTP handed to OAN for consent request ... (message ...)` and
  `... code sent`, against the fake OAN gateway in namespace `oan-messaging`.

**Not verified. Confirm each on New Dev before relying on it:**

- `commons-garage` and its S3 port 3900 (taken from the 21 Nov Confluence page and
  the chart's `objectStore` templates).
- Whether the `commons-minio:9000` compatibility Service is enabled
  (`objectStore.compatService.enabled`). If it is, the old endpoint may have worked
  and the keys in `consent-manager-otp-dev` are the more likely cause.
- The keys in `consent-manager-otp-dev`, bucket `a2c-webhook` and the Garage region.
- Which consent image is running, and that it contains the SMS change.
- A real Garage (region and signature behaviour) and `helm template` (no Helm in the
  local environment; the PR `validate` check covers it).

## Open items

- The phone map is for test numbers. Production needs a phone resolver approved
  by the identity owner, plugged in at `resolve_phone` in `otp_delivery.py`.
- A failed bucket write is only a warning. If it should fail the request,
  that is a consent-management code change.
- `pytest-asyncio` is missing from consent-management's `[test]` extras.
