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

Chart version **1.0.0-dev.4** uses the wildcard development domain and shared Istio Gateway.
Application images remain unchanged, including the recorded older OAN Consent build. To select
the newly published candidates, merge the reviewed
[Consent image override](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/examples/dev/consent-image-values.yaml)
and [Aggregation image override](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/examples/dev/aggregation-image.yaml)
with your private values. The image overrides do not prepare databases, signing
keys, identity, policy bindings or routing. Aggregation stays disabled.

Upgrade the existing `commons-services` release in namespace `commons`. Review
all shared-service changes and backups. Helm rollback does not reverse database
migrations. Follow the
[component prerequisites](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/consent-aggregation-prerequisites.md)
and [Rancher guide](https://github.com/Centre-for-Open-Societal-Systems/oan-helm/blob/main/docs/rancher-dev.md).

Dev URLs use `<service>.development.oanstaging.com`. The environment-owned
wildcard DNS/TLS and `istio-system/development` Gateway must be prepared first.
See the service onboarding and enablement guide in `docs/service-onboarding.md`.
