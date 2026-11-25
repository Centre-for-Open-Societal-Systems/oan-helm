# oan-grievance-ui: staging history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-staging.7

<!-- source-commit: b6f5a923acc59d9de4b1f2ef65f9b60f7a5b4665 version: 0.0.1-staging.7 -->
Published 2026-11-25. Archive SHA-256 `2457f0dedfe3f2f3cb10137e110d94a595c0c5f0ea16804a60746dad078bd282`.

- Change: Merge pull request #92 from arnavam/resync/staging-into-develop
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@b6f5a923acc5](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/b6f5a923acc59d9de4b1f2ef65f9b60f7a5b4665)

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-staging.7@sha256:3fa9d014368f3ccafa0707fddd3c666a2e9c64067f9e38650203152d0416ba68` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/staging/oan-grievance-ui-0.0.1-staging.7.tgz -n grievance --reset-values -f helm/environments/staging/oan-grievance-ui.yaml --wait --timeout 15m
```

