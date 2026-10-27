# Security

Report a vulnerability in these charts privately, never in a public issue: use
*Report a vulnerability* on the repository's Security tab when it is enabled, or
contact the COSS maintainers directly. Vulnerabilities in a deployed application belong to that
application's COSS repository, linked from the chart's README.

The charts never carry credentials. They reference existing Kubernetes Secrets by name
and key; passwords, tokens, kubeconfigs and exported live values stay outside Git. If a
secret is committed by mistake, rotate it first: removing it from history does not
revoke it.
