# oan-grievance-gateway: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.14

<!-- source-commit: f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93 version: 0.0.1-staging.14 -->
Published 2026-11-24. Archive SHA-256 `86fd58d26ce2f863bbed8b1ec2b2c39feddd478c369212e25a6447ba5f7c721c`.

- Change: Merge pull request #151 from arnavam/resync/staging-into-develop
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_service@f4b2bda4b44a](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_service/commit/f4b2bda4b44a3a4e012d74b94fa8cc09c238ea93)

Return to this version:

```sh
helm upgrade grievance-gateway https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-grievance-gateway-0.0.1-staging.14.tgz -n grievance --reset-values -f helm/environments/staging/oan-grievance-gateway.yaml --wait --timeout 15m
```

