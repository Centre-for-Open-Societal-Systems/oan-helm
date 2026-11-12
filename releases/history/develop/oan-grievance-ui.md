# oan-grievance-ui: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.0-develop.48

<!-- source-commit: 4d374c7e7b10af450fe20dfaf816d22bbefeb1c3 version: 0.0.0-develop.48 -->
Published 2026-11-12. Archive SHA-256 `0a604220145b2d64b5b2c1bd07c76d3385ca622c621674a9399fa1e3d1c28e26`.

- Change: Merge pull request #71 from arnavam/fix/helm-ingress-paths
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@4d374c7e7b10](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/4d374c7e7b10af450fe20dfaf816d22bbefeb1c3)

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/oan/oan-grievance-ui/grievance-ui:0.0.0-develop.48` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.0-develop.48.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

