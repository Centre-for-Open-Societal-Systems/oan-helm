# OAN Commons Services: Consent Manager and Aggregation

This is the OpenAgriNet (OAN) shared-services chart maintained in COSS.

| OAN component | Application source | Helm implementation |
| --- | --- | --- |
| OAN Consent Manager | [COSS/consent-management](https://github.com/Centre-for-Open-Societal-Systems/consent-management) | Reuses the `openg2p-consent-manager:1.0.2` template dependency; OAN image overrides under `openg2p-consent-manager` in values.yaml |
| OAN Aggregation API | [COSS/oan-aggregation-api](https://github.com/Centre-for-Open-Societal-Systems/oan-aggregation-api) | Local `templates/aggregation-api.yaml`; configured by `aggregationApi`, disabled pending runtime preparation |
| OAN Helm chart | [COSS/oan-helm](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/tree/main/charts/openg2p-commons-services) | Editable sources and immutable packages |

## Why is the dependency still named openg2p-consent-manager?

It identifies the reused OpenG2P Helm templates. The OAN application source and
image selection are recorded separately. Keeping the chart, release and resource
names preserves existing Helm ownership and saved values. Aggregation is a local
parent-chart template and therefore has no separate Chart.yaml dependency entry.
The other shared applications remain pinned upstream dependencies with their
original provenance; this chart does not claim they were all authored by OAN.

## Select the images deliberately

Chart version **1.0.0-dev.5** uses the wildcard development domain and shared Istio Gateway.
Consent images are pinned to COSS commit `48e64c249056`, and Aggregation to
`a5fa17fd7e7f`, using verified ECR digests. Aggregation is now stateless: it needs
no database, queue or migration. Its own signing key, registry catalog, protected
staff authentication and partner/policy bindings still need preparation.
The optional VirtualService selects `aggregation.development.oanstaging.com`.
OTP log/bucket publishing remain disabled pending SMS. See the current
[setup guide](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/consent-aggregation-prerequisites.md).
Default Aggregation enablement remains false; use a complete reviewed runtime
overlay when upgrading the existing release.

Upgrade the existing `commons-services` release in namespace `commons`. Review
all shared-service changes and backups. Helm rollback does not reverse database
migrations. Follow the
[component prerequisites](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/consent-aggregation-prerequisites.md)
and [Rancher guide](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/rancher-dev.md).

Dev URLs use `<service>.development.oanstaging.com`. The environment-owned
wildcard DNS/TLS and `istio-system/development` Gateway must be prepared first.
See the service onboarding and enablement guide in `docs/service-onboarding.md`.
