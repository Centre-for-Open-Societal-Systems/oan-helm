# oan-grievance-ui: develop history

Newest first. Written by scripts/publish_channels.py. See docs/rollback.md before rolling back.

## 0.0.1-develop.64

<!-- source-commit: b6f5a923acc59d9de4b1f2ef65f9b60f7a5b4665 version: 0.0.1-develop.64 -->
Published 2026-11-25. Archive SHA-256 `344f2db4ff5fa6245a65137f0281e3963e6e830d5d634ec69c22db6e0908738d`.

- Change: Merge pull request #92 from arnavam/resync/staging-into-develop
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@b6f5a923acc5](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/b6f5a923acc59d9de4b1f2ef65f9b60f7a5b4665)
- Changes since 0.0.1-develop.63: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/a0f5e1c445e20305507d435cbb405191c4ad5946...b6f5a923acc59d9de4b1f2ef65f9b60f7a5b4665

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.64@sha256:3fa9d014368f3ccafa0707fddd3c666a2e9c64067f9e38650203152d0416ba68` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.64.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.63

<!-- source-commit: a0f5e1c445e20305507d435cbb405191c4ad5946 version: 0.0.1-develop.63 -->
Published 2026-11-25. Archive SHA-256 `ff83368d6ca7659222d4e2437e1727f144f8392b8ab7d9059979b1ba4ab17a83`.

- Change: ci: use oan-helm's app_chart for the chart steps and register promote (#91)
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@a0f5e1c445e2](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/a0f5e1c445e20305507d435cbb405191c4ad5946)
- Changes since 0.0.1-develop.62: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/6e0e0e83fafdcf990692eb5767706de075127b95...a0f5e1c445e20305507d435cbb405191c4ad5946

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.63@sha256:2ac6dd79cb2895a82fed33c43692d8e0d3c5c1c049f950aa7a3b4d71cfabbb46` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.63.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.62

<!-- source-commit: 6e0e0e83fafdcf990692eb5767706de075127b95 version: 0.0.1-develop.62 -->
Published 2026-11-24. Archive SHA-256 `a394b2209c84d64bea134d11077737652a90a4a1ca85d6764169fbc7f280d87b`.

- Change: Merge pull request #89 from apoorvanengineer-cpu/feature/officer-category-coverage
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@6e0e0e83fafd](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/6e0e0e83fafdcf990692eb5767706de075127b95)
- Changes since 0.0.1-develop.61: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/3797c2b33aa89cf1efee58e06d0298b48625cc6b...6e0e0e83fafdcf990692eb5767706de075127b95

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.62` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.62.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.61

<!-- source-commit: 3797c2b33aa89cf1efee58e06d0298b48625cc6b version: 0.0.1-develop.61 -->
Published 2026-11-24. Archive SHA-256 `340a2f2b611be652fca44dabd2b4ab87ff96f9c49e884c1676bc2831bae20bae`.

- Change: feat(admin): add an SLA Rules tab, and drop SLA settings from the category cards (#82)
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@3797c2b33aa8](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/3797c2b33aa89cf1efee58e06d0298b48625cc6b)
- Changes since 0.0.1-develop.60: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/1e491eefd2c978f1f2883e9af4b82d4dc9aca490...3797c2b33aa89cf1efee58e06d0298b48625cc6b

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.61` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.61.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.60

<!-- source-commit: 1e491eefd2c978f1f2883e9af4b82d4dc9aca490 version: 0.0.1-develop.60 -->
Published 2026-11-24. Archive SHA-256 `520a8c4a4d07aaa84bc53c42a77f635f4d7328257691403a4c939f4df8a55de2`.

- Change: fix(ci): fetch develop so the staging promote can read the chart's source trees (#86)
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@1e491eefd2c9](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/1e491eefd2c978f1f2883e9af4b82d4dc9aca490)
- Changes since 0.0.1-develop.53: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/3138291549c0f26021874e37c10b316db1137fc4...1e491eefd2c978f1f2883e9af4b82d4dc9aca490

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.60` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.60.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.53

<!-- source-commit: 3138291549c0f26021874e37c10b316db1137fc4 version: 0.0.1-develop.53 -->
Published 2026-11-17. Archive SHA-256 `9d40467f566d17f592931bdd78421a15a6843afed615d483dd85b285cf416c88`.

- Change: Merge pull request #76 from arnavam/chore/develop-chart-version
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@3138291549c0](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/3138291549c0f26021874e37c10b316db1137fc4)
- Changes since 0.0.1-develop.52: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/1c44b323a577f2ea10a277f7bd3180812dabf3d1...3138291549c0f26021874e37c10b316db1137fc4

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.53` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.53.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.52

<!-- source-commit: 1c44b323a577f2ea10a277f7bd3180812dabf3d1 version: 0.0.1-develop.52 -->
Published 2026-11-15. Archive SHA-256 `07d2c4074e0f13a50e1610e5755532a7820b467e630815e69f991c6dc864bf8c`.

- Change: Merge pull request #75 from arnavam/feat/api-path-prefix
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@1c44b323a577](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/1c44b323a577f2ea10a277f7bd3180812dabf3d1)
- Changes since 0.0.1-develop.51: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/cb77b4bc47820935ff1f8f06babf8717cc806fd7...1c44b323a577f2ea10a277f7bd3180812dabf3d1

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.52` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.52.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.51

<!-- source-commit: cb77b4bc47820935ff1f8f06babf8717cc806fd7 version: 0.0.1-develop.51 -->
Published 2026-11-15. Archive SHA-256 `db7d2d7895ffec41486c0c903718336a561c9bf07a9c8398c7d42b73ea78502c`.

- Change: Merge pull request #74 from arnavam/chore/disable-ui-autoscaling
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@cb77b4bc4782](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/cb77b4bc47820935ff1f8f06babf8717cc806fd7)
- Changes since 0.0.1-develop.50: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/06f5f2994638b1f4dd13743f909eeaac59020467...cb77b4bc47820935ff1f8f06babf8717cc806fd7

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.51` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.51.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.50

<!-- source-commit: 06f5f2994638b1f4dd13743f909eeaac59020467 version: 0.0.1-develop.50 -->
Published 2026-11-13. Archive SHA-256 `df69433d717213301c0a6cbfc4f8f994662455378dd729ba85727b9f2164337f`.

- Change: Merge pull request #73 from apoorvanengineer-cpu/feature/feedback-and-field-validations
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@06f5f2994638](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/06f5f2994638b1f4dd13743f909eeaac59020467)
- Changes since 0.0.1-develop.49: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/f9a3e9978dfa271114d4431c17223fbb9c0e6319...06f5f2994638b1f4dd13743f909eeaac59020467

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.50` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.50.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

## 0.0.1-develop.49

<!-- source-commit: f9a3e9978dfa271114d4431c17223fbb9c0e6319 version: 0.0.1-develop.49 -->
Published 2026-11-13. Archive SHA-256 `d8a6ccf477617b7ccfd30d412f4c6e41aeda137771fe85485f9a28104fef5c65`.

- Change: Merge pull request #72 from arnavam/chore/eoan-ecr-path
- Source: [Centre-for-Open-Societal-Systems/oan_grievance_ui@f9a3e9978dfa](https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/commit/f9a3e9978dfa271114d4431c17223fbb9c0e6319)
- Changes since 0.0.0-develop.48: https://github.com/Centre-for-Open-Societal-Systems/oan_grievance_ui/compare/4d374c7e7b10af450fe20dfaf816d22bbefeb1c3...f9a3e9978dfa271114d4431c17223fbb9c0e6319

| Values path | Image |
| --- | --- |
| `ui.image` | `379220350808.dkr.ecr.ap-south-1.amazonaws.com/eoan/oan-grievance-ui/grievance-ui:0.0.1-develop.49` |

Return to this version:

```sh
helm upgrade grievance-ui https://raw.githubusercontent.com/Centre-for-Open-Societal-Systems/oan-helm/main/repository/develop/oan-grievance-ui-0.0.1-develop.49.tgz -n grievance --reset-values -f helm/environments/dev/oan-grievance-ui.yaml --wait --timeout 15m
```

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

