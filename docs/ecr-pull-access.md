# Allow new-dev to pull the Aggregation image

The Aggregation candidate is published in account `379220350808`, region
`ap-south-1`, repository `oan/commons/aggregation-api`.

## Observed denial

The existing `commons/ecr-pull-secret` token identifies the EC2 role
`arn:aws:iam::379220350808:role/openg2p-dev-sandbox-dns`.
Authenticated registry requests with that same token can read the existing
Consent image manifest (HTTP 200), but the Aggregation request returns HTTP 403
`DENIED`. AWS reports no identity-based policy allows `ecr:BatchGetImage` on
`arn:aws:ecr:ap-south-1:379220350808:repository/oan/commons/aggregation-api`.
The error does not indicate token expiry or an explicit deny.

Neither repository had a resource policy at inspection time. The Jenkins AWS
identity can read the role metadata, but `iam:ListRolePolicies` returned
`AccessDenied`; a complete policy review or policy simulation was not performed.
Do not interpret this evidence as a complete IAM analysis.

## Proposed additive identity policy

Use [aggregation-pull-policy.json](../examples/aws/aggregation-pull-policy.json).
It grants only `ecr:BatchCheckLayerAvailability`, `ecr:BatchGetImage` and
`ecr:GetDownloadUrlForLayer`, restricted to this repository ARN. It grants no
push, repository-management or unrelated AWS actions. The role already obtains
ECR authorization tokens; this proposal does not change that permission.

Apply through an authorized IAM administrator:

1. Confirm AWS account `379220350808`.
2. Open **IAM → Roles → openg2p-dev-sandbox-dns → Permissions**.
3. Choose **Add permissions → Create inline policy → JSON**.
4. Paste the exact JSON from the linked policy file; review its actions/resource.
5. Name it `PullOanCommonsAggregationApi`, then create the policy. If that name
   already exists, inspect it first; do not overwrite an existing policy blindly.

CLI equivalent for an authorized administrator, after confirming the policy
name is unused:

```sh
aws iam put-role-policy \
  --role-name openg2p-dev-sandbox-dns \
  --policy-name PullOanCommonsAggregationApi \
  --policy-document file://examples/aws/aggregation-pull-policy.json
```

This is a proposed access change. No IAM policy, ECR repository policy or
cluster Secret has been changed by preparing these files. If permissions
boundaries, organization controls or session policies restrict access further,
an authorized administrator must reconcile those restrictions separately.

## Verify after applying

Repeat the authenticated manifest request using the existing namespace-local
pull Secret. Check both the OCI index and its `linux/amd64` child manifest,
then check permission to download image layers without exposing signed URLs or
credentials. A successful manifest request alone is not proof of layer-download
permissions or Kubernetes readiness. Refresh the token through the existing
process if AWS reports expiry; do not paste credentials into chat or Git.

No workload restart or Aggregation deployment is needed to test registry access.
Aggregation remains disabled until compatible Consent images and runtime
configuration are ready. See [component prerequisites](consent-aggregation-prerequisites.md).

The action names and repository scoping follow the
[AWS ECR policy examples](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html).

## Registry images under `eoan/`

The naming standard moves registry images to `eoan/<repository>/<image>[-<rpVersion>]`
([naming-standard.md](release/naming-standard.md), section 6), for example
`eoan/farmer-registry/staff-api-1.2.2-rc.625`. CI creates each repository on its first push, and every
`rpVersion` bump adds new ones, so pull access must cover the prefix rather than single repository ARNs.

Read on 19 November 2026 (pods on both clusters, `kubectl get pods -A`, image references only):

- New Dev and staging pull registry images only from `openg2p/<repository>/*` (and `openg2p/oan-dashboards`) in
  account `379220350808`; no `eoan/*` repository is referenced yet.
- Pull Secrets: `ecr-pull-secret` in `commons`, `farmer`, `crop`, `da-registry`, `reports` and the livestock
  namespace (`livestock` on New Dev, `live` on staging), plus the per-registry `<registry>-ecr-pull-secret` and
  `<registry>-dashboard-ecr` Secrets. They hold short-lived ECR tokens of the node role.
- The Aggregation denial above shows that the New Dev role's identity policy is scoped per repository. Whether it
  (and the staging role) allows `eoan/*` has **not** been confirmed: the role's policies cannot be listed with the
  credentials available here.

Before the first registry deploys from `eoan/<repository>/*`, an authorized IAM administrator confirms (or adds)
pull on `arn:aws:ecr:ap-south-1:379220350808:repository/eoan/*` for the New Dev and staging node roles, with the
same three actions as [aggregation-pull-policy.json](../examples/aws/aggregation-pull-policy.json). The first
develop deploy of each registry then proves it: its pods start from the new paths. A path that cannot be pulled
shows as `ImagePullBackOff` and fails that deploy; check this on New Dev before the first staging promotion.
