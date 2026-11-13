# Partner routes on a new gateway

Starting points for the `oan-partner-gateway` values of a gateway that does not exist yet.
They are checklists, not live values: every `<...>` must be replaced.

| File | Gateway |
|---|---|
| `oan-partner-gateway.uat.yaml` | UAT: accepts tokens of UAT apps (`environmentRole: uat`) |
| `oan-partner-gateway.production.yaml` | Production: accepts tokens of production apps (`environmentRole: production`) |

UAT and production are two gateways, each with its own Keycloak, so they are two releases
with two values files. The two files differ only in `environmentRole`; the hosts and the
Keycloak realm are yours to fill in. The install steps are in
[docs/apisix-gateway.md](../../docs/apisix-gateway.md), section 8c.
