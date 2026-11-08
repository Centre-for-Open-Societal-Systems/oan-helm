# OAN registries release documentation

This folder describes the OpenAgriNet (OAN) registries release as it runs today. Every fact has a source.
Where a fact could not be checked, the text says "Not verified:" and names what is missing.

All live readings were taken on 5 November 2026, between 20:45 and 20:55 UTC, with read-only commands on
New Dev and on staging. Repository readings are from `main` of this repository at commit `7db1f6a` and from
the `develop` branch of each registry repository on the same day.

## System in one paragraph

Four registries run on OpenG2P Registry 1.2: Farmer, Crop sown, Livestock and Development Agent. Each is one
Helm release that wraps the OpenG2P `openg2p-registry` chart and adds an OAN extension. They share the Commons
services in the namespace `commons`: Keycloak (sign-in), Partner Management (partner identities and keys),
Consent Manager, Master Data (lists and geography), the Approval Workflow Engine (two-stage approvals),
WebSub with Kafka (change notices), the aggregation service, ODK Central (field forms) and MinIO (files).
Each registry has a dashboard (a user interface plus a dashboard API that reads reporting views), and the
shared `oan-dashboards` service reads each dashboard API. Data enters a registry by web intake or by a
connector that reads ODK Central submissions and posts them to the registry's partner API. Crop sown and
Livestock look up the farmer in the Farmer registry through a signed, consented search, and the Farmer
registry tells them about changes through a WebSub notice. Two environments exist: New Dev and staging.

## Contents

| Document | What it answers |
| --- | --- |
| [versions.md](versions.md) | Which chart and which images run on New Dev and on staging, which OpenG2P versions they pin, and where the two environments differ |
| [environments.md](environments.md) | Namespaces, release names, public hostnames and the Jenkins job that deploys each part |
| [delivery-pipeline.md](delivery-pipeline.md) | How a merge becomes a running release, the chart channels, the no-click rule and branch protection |
| [operations-runbook.md](operations-runbook.md) | How to check health, deploy, roll back, recover a stuck release, refresh pull secrets, find logs and back up |
| [integration-contracts.md](integration-contracts.md) | Every data flow between systems: source, target, transport, name and authentication |
| [naming-standard.md](naming-standard.md) | The naming rules, the evidence from OpenG2P and the rename plan |

## Source references used in this folder

Each table in this folder ends with a line "Source:". The short names mean:

| Short name | Meaning |
| --- | --- |
| live reading | A read-only command on the cluster: `helm list -A`, `helm history`, `kubectl get` or `kubectl describe` |
| Jenkins reading | A read-only request to the Jenkins API: job list, job configuration or console text |
| repository file | A file read with `git show <branch>:<path>` or from a checkout at the stated commit |
| OpenG2P versions | https://github.com/OpenG2P/versions at commit `e3ea94b` (5 November 2026) |
| OpenG2P documentation | https://docs.openg2p.org |

## Open problems found while writing

These are also repeated in the document where they belong.

| Problem | Where |
| --- | --- |
| Crop sown on staging: the Helm release is in state `failed` and three pods cannot pull images | [operations-runbook.md](operations-runbook.md) |
| Development Agent on staging: only the id generator and Redis run; the registry workloads were rolled back | [environments.md](environments.md) |
| The Farmer connector on staging runs an older image than New Dev (no admin login) | [versions.md](versions.md) |
| Staging host routing is one nginx file per host; the wildcard site is not installed | [operations-runbook.md](operations-runbook.md) |
| No branch protection on any repository | [delivery-pipeline.md](delivery-pipeline.md) |
