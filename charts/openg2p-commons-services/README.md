# OAN Commons Services: Consent Manager and Aggregation

This is the OpenAgriNet (OAN) shared-services chart maintained in the OAN repositories.

| OAN component | Application source | Helm implementation |
| --- | --- | --- |
| OAN Consent Manager | [Centre-for-Open-Societal-Systems/consent-management](https://github.com/Centre-for-Open-Societal-Systems/consent-management) | Reuses the `openg2p-consent-manager:1.0.2` template dependency; OAN image overrides under `openg2p-consent-manager` in values.yaml |
| OAN Aggregation API | [Centre-for-Open-Societal-Systems/oan-aggregation-api](https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api) | `oan-aggregation-api` subchart (alias `aggregation-api`), bundled in `charts/` by the oan-aggregation-api pipeline; configured by `aggregation-api`, enabled |
| OAN Helm chart | [Centre-for-Open-Societal-Systems/oan-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/openg2p-commons-services) | Editable sources and immutable packages |

## Why is the dependency still named openg2p-consent-manager?

It identifies the reused OpenG2P Helm templates. The OAN application source and
image selection are recorded separately. Keeping the chart, release and resource
names preserves existing Helm ownership and saved values. Aggregation is the
`oan-aggregation-api` dependency (alias `aggregation-api`), keeping the former resource names.
The other shared applications remain pinned upstream dependencies with their
original provenance; this chart does not claim they were all authored by OAN.

## Select the images deliberately

Chart version **1.0.0-dev.5** uses the wildcard development domain and shared Istio Gateway.
Consent images are pinned to OAN commit `48e64c249056`, and Aggregation to
`a5fa17fd7e7f`, using verified ECR digests. Aggregation is now stateless: it needs
no database, queue or migration. Its own signing key, registry catalog, protected
staff authentication and partner/policy bindings still need preparation.
The optional VirtualService selects `aggregation.development.oanstaging.com`.
OTP log/bucket publishing remain disabled pending SMS. See the current
[setup guide](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/consent-aggregation-prerequisites.md).
Aggregation is enabled by default; its image is the one in the bundled
`oan-aggregation-api` archive, and its Secrets and catalog must exist in the namespace.

Upgrade the existing `commons-services` release in namespace `commons`. Review
all shared-service changes and backups. Helm rollback does not reverse database
migrations. Follow the
[component prerequisites](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/consent-aggregation-prerequisites.md)
and [Rancher guide](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/rancher-dev.md).

Dev URLs use `<service>.development.oanstaging.com`. The environment-owned
wildcard DNS/TLS and `istio-system/development` Gateway must be prepared first.
See the service onboarding and enablement guide in `docs/service-onboarding.md`.

## OAN Consent Partner Portal

The OAN browser portal is included through `consentPartnerPortal`, alongside the
existing Consent staff UI and partner API. Enable it with the reviewed
`examples/dev/consent-partner-portal.yaml` overlay after preparing partner login.
Its image is built from the recorded OAN Consent source and pinned by ECR digest.
OTP stays unavailable pending SMS; enabling the UI does not enable OTP delivery.
