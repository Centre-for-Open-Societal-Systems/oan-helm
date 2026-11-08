# Changelog

Chart releases, newest first. Each entry is written by `scripts/release.py`
when a merge to `main` changes a chart: the chart gets its next version, its
archive is added to `repository/`, and the commits that touched it are listed
here. Releases up to `1.0.0-dev.16` were published as one release train; their
notes are under `releases/<version>.yaml`.

<!-- Releases are inserted below this line by scripts/release.py. -->

## 2026-11-08

### openg2p-cropsown-registry 0.0.0-develop.500 (develop)

- Operator job: a parameter to accept a deliberate connector chart change (#253) (Centre-for-Open-Societal-Systems/cropsown-regsitry@97e9a92e1fb8)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-08

### openg2p-farmer-registry 0.0.0-develop.825 (develop)

- Create a missing role image repository like the component's own, then push again (#242) (Centre-for-Open-Societal-Systems/farmer-registry@eeafa8593de1)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-08

### openg2p-cropsown-registry 0.0.0-develop.499 (develop)

- Wait for every table the crop reporting views read before applying them (#252) (Centre-for-Open-Societal-Systems/cropsown-regsitry@5287a40657f0)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-08

### openg2p-farmer-registry 0.0.0-develop.824 (develop)

- Name the docker step that failed and catch a missing ECR repository on push (#241) (Centre-for-Open-Societal-Systems/farmer-registry@a7a37ef1d37a)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-08

### openg2p-farmer-registry 0.0.0-develop.823 (develop)

- Keep publishing the earlier farmer change topic until the receivers move (#240) (Centre-for-Open-Societal-Systems/farmer-registry@60169129495d)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-08

### openg2p-da-registry 1.0.0-rc.87 (staging)

- DA staging deploys on merge with no Build with Parameters (#47) (Centre-for-Open-Societal-Systems/da-registry@acf5e374a852)
- Images and rollback: [releases/history/staging/openg2p-da-registry.md](releases/history/staging/openg2p-da-registry.md)

## 2026-11-08

### openg2p-farmer-registry 0.0.0-develop.822 (develop)

- Publish the farmer change notice as farmer-registry.farmer-profile.changed.v1 (#236) (Centre-for-Open-Societal-Systems/farmer-registry@14982326968d)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-08

### openg2p-livestock-registry 0.0.0-develop.435 (develop)

- Seed renames the Farmer-reference tables before it writes the archive (#210) (Centre-for-Open-Societal-Systems/livestock-registry@cd63c4c20c63)
- Images and rollback: [releases/history/develop/openg2p-livestock-registry.md](releases/history/develop/openg2p-livestock-registry.md)

## 2026-11-08

### openg2p-cropsown-registry 0.0.0-develop.498 (develop)

- Seed renames the Farmer-reference tables before it writes the archive (#251) (Centre-for-Open-Societal-Systems/cropsown-regsitry@e1fa219edac4)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-08

### openg2p-farmer-registry 0.0.0-develop.819 (develop)

- Add required chart check and failure mail on staging builds (#237) (Centre-for-Open-Societal-Systems/farmer-registry@c15d5c18f2cc)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-08

### openg2p-commons-services 1.0.0-dev.37

Previous version: 1.0.0-dev.36.

- Master Data seed image with the crop theme and the cluster status list (#139) (c012fdf)

## 2026-11-08

### openg2p-cropsown-registry 1.0.0-dev.23

Previous version: 1.0.0-dev.22.

- Name the Farmer reference settings after the registry, not the delivery team (#129) (af00768)

### openg2p-livestock-registry 1.0.0-dev.25

Previous version: 1.0.0-dev.24.

- Name the Farmer reference settings after the registry, not the delivery team (#129) (af00768)

## 2026-11-08

### openg2p-livestock-registry 0.0.0-develop.433 (develop)

- Replace the stale parameter test with a check that the pipeline takes no parameters (#211) (Centre-for-Open-Societal-Systems/livestock-registry@455e6ec2eac4)
- Images and rollback: [releases/history/develop/openg2p-livestock-registry.md](releases/history/develop/openg2p-livestock-registry.md)

## 2026-11-08

### oan-a2c 0.1.0-dev.3

Previous version: 0.1.0-dev.2.

- feat(a2c,grievance): vendor the frappe chart archive without a repository (28d0641)
- feat(a2c,grievance): depend on the OAN frappe chart with PostgreSQL and Redis (20453a9)

### oan-clamav 0.1.0-dev.1

First published version.

- feat(a2c,grievance): depend on the OAN frappe chart with PostgreSQL and Redis (20453a9)

### oan-grievance-service 0.1.0-dev.3

Previous version: 0.1.0-dev.2.

- chore(grievance): drop site config keys the auth and grievance apps no longer read (2e12ec4)
- feat(a2c,grievance): vendor the frappe chart archive without a repository (28d0641)
- feat(a2c,grievance): depend on the OAN frappe chart with PostgreSQL and Redis (20453a9)

## 2026-11-08

### openg2p-farmer-registry 0.0.0-develop.818 (develop)

- Deploy on merge without Build with Parameters (#235) (Centre-for-Open-Societal-Systems/farmer-registry@7daff6e3d2a5)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-08

### openg2p-da-registry 0.0.0-develop.85 (develop)

- DA staging deploys on merge with no Build with Parameters (#47) (Centre-for-Open-Societal-Systems/da-registry@acf5e374a852)
- Images and rollback: [releases/history/develop/openg2p-da-registry.md](releases/history/develop/openg2p-da-registry.md)

## 2026-11-08

### openg2p-cropsown-registry 0.0.0-develop.496 (develop)

- Upgrade the staging crop connector to the registry-connector image from the pipeline (#246) (Centre-for-Open-Societal-Systems/cropsown-regsitry@bad56edad2ed)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-06

### openg2p-cropsown-registry 0.0.0-develop.494 (develop)

- Crop chart refreshes its own ECR pull secret and stops loading seed images (#247) (Centre-for-Open-Societal-Systems/cropsown-regsitry@3ee052a6b0de)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-06

### openg2p-cropsown-registry 0.0.0-develop.493 (develop)

- Declare crop connector definitions in git and apply them with a Helm hook (#245) (Centre-for-Open-Societal-Systems/cropsown-regsitry@4a4c2fa3a91e)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-06

### openg2p-cropsown-registry 0.0.0-develop.489 (develop)

- Run the browser tests on Ubuntu 24.04 (#244) (Centre-for-Open-Societal-Systems/cropsown-regsitry@deabbfe47dca)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-06

### oan-a2c 0.1.0-dev.2

Previous version: 0.1.0-dev.1.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

### oan-grievance-service 0.1.0-dev.2

Previous version: 0.1.0-dev.1.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

### oan-sandbox 1.0.0-dev.18

Previous version: 1.0.0-dev.17.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

### openg2p-commons-services 1.0.0-dev.36

Previous version: 1.0.0-dev.35.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

### openg2p-cropsown-registry 1.0.0-dev.22

Previous version: 1.0.0-dev.21.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

### openg2p-da-registry 1.0.0-dev.23

Previous version: 1.0.0-dev.22.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

### openg2p-farmer-registry 1.0.0-dev.24

Previous version: 1.0.0-dev.23.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

### openg2p-livestock-registry 1.0.0-dev.24

Previous version: 1.0.0-dev.23.

- Rename COSS to OAN in chart names, annotations, helpers, scripts and docs (#127) (5982df6)

## 2026-11-06

### openg2p-da-registry 1.0.0-dev.22

Previous version: 1.0.0-dev.21.

- DA staging reaches the Commons approval engine by its short name (e8a8018)

## 2026-11-06

### openg2p-cropsown-registry 1.0.0-dev.21

Previous version: 1.0.0-dev.20.

- Crop seed stops loading profile images it does not ship (18f4da6)
- Registry charts create and refresh their own ECR pull secret (590000c)

### openg2p-da-registry 1.0.0-dev.21

Previous version: 1.0.0-dev.20.

- Registry charts create and refresh their own ECR pull secret (590000c)

### openg2p-farmer-registry 1.0.0-dev.23

Previous version: 1.0.0-dev.22.

- Registry charts create and refresh their own ECR pull secret (590000c)

### openg2p-livestock-registry 1.0.0-dev.23

Previous version: 1.0.0-dev.22.

- Registry charts create and refresh their own ECR pull secret (590000c)

## 2026-11-05

### openg2p-da-registry 1.0.0-rc.84 (staging)

- Merge pull request #43 from asmitonweb/promote-staging-without-rebuilding (Centre-for-Open-Societal-Systems/da-registry@9dc1ebfea870)
- Images and rollback: [releases/history/staging/openg2p-da-registry.md](releases/history/staging/openg2p-da-registry.md)

## 2026-11-05

### openg2p-cropsown-registry 0.0.0-develop.488 (develop)

- Merge pull request #239 from asmitonweb/use-pack-codes-for-growth-stage-and-severity (Centre-for-Open-Societal-Systems/cropsown-regsitry@fbe5a37e41f2)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-05

### openg2p-farmer-registry 1.0.0-rc.813 (staging)

- Merge pull request #228 from asmitonweb/promote-staging-automatically (Centre-for-Open-Societal-Systems/farmer-registry@90b2649a7b10)
- Images and rollback: [releases/history/staging/openg2p-farmer-registry.md](releases/history/staging/openg2p-farmer-registry.md)

## 2026-11-05

### openg2p-cropsown-registry 0.0.0-develop.485 (develop)

- Merge pull request #235 from asmitonweb/record-staging-history (Centre-for-Open-Societal-Systems/cropsown-regsitry@51d9894158b1)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-05

### openg2p-livestock-registry 1.0.0-rc.432 (staging)

- Merge pull request #199 from asmitonweb/promote-staging-without-rebuilding (Centre-for-Open-Societal-Systems/livestock-registry@cc5b130f5aea)
- Images and rollback: [releases/history/staging/openg2p-livestock-registry.md](releases/history/staging/openg2p-livestock-registry.md)

## 2026-11-05

### openg2p-cropsown-registry 0.0.0-develop.469 (develop)

- Merge pull request #234 from asmitonweb/promote-staging-without-rebuilding (Centre-for-Open-Societal-Systems/cropsown-regsitry@e591be837fad)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-05

### openg2p-farmer-registry 0.0.0-develop.803 (develop)

- Merge pull request #228 from asmitonweb/promote-staging-automatically (Centre-for-Open-Societal-Systems/farmer-registry@90b2649a7b10)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-05

### openg2p-livestock-registry 0.0.0-develop.426 (develop)

- Merge pull request #199 from asmitonweb/promote-staging-without-rebuilding (Centre-for-Open-Societal-Systems/livestock-registry@cc5b130f5aea)
- Images and rollback: [releases/history/develop/openg2p-livestock-registry.md](releases/history/develop/openg2p-livestock-registry.md)

## 2026-11-05

### openg2p-da-registry 0.0.0-develop.83 (develop)

- Merge pull request #43 from asmitonweb/promote-staging-without-rebuilding (Centre-for-Open-Societal-Systems/da-registry@9dc1ebfea870)
- Images and rollback: [releases/history/develop/openg2p-da-registry.md](releases/history/develop/openg2p-da-registry.md)

## 2026-11-05

### oan-sandbox 1.0.0-dev.17

Previous version: 1.0.0-dev.16.

- feat(oan-sandbox): Keycloak, OAuth app tokens and partner gateway val… (#102) (5dcaa12)

## 2026-11-05

### openg2p-livestock-registry 0.0.0-develop.424 (develop)

- Move the Livestock chart into this repository and deploy the chart each build packages (Centre-for-Open-Societal-Systems/livestock-registry@e5082c54e7ab)
- Images and rollback: [releases/history/develop/openg2p-livestock-registry.md](releases/history/develop/openg2p-livestock-registry.md)

## 2026-11-05

### openg2p-cropsown-registry 0.0.0-develop.467 (develop)

- Move the Crop chart into this repository and deploy the chart each build packages (Centre-for-Open-Societal-Systems/cropsown-regsitry@791c66f9d008)
- Images and rollback: [releases/history/develop/openg2p-cropsown-registry.md](releases/history/develop/openg2p-cropsown-registry.md)

## 2026-11-05

### openg2p-da-registry 0.0.0-develop.81 (develop)

- Move the DA chart into this repository and deploy the chart each build packages (Centre-for-Open-Societal-Systems/da-registry@4ad52ab0f375)
- Images and rollback: [releases/history/develop/openg2p-da-registry.md](releases/history/develop/openg2p-da-registry.md)

## 2026-11-05

### openg2p-farmer-registry 0.0.0-develop.801 (develop)

- Deploy the chart each develop build packages, and publish that same archive (Centre-for-Open-Societal-Systems/farmer-registry@3337c093d42e)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-05

### openg2p-farmer-registry 0.0.0-develop.800 (develop)

- Publish the Farmer chart from this repository after each deploy (#226) (Centre-for-Open-Societal-Systems/farmer-registry@a9128872b86d)
- Images and rollback: [releases/history/develop/openg2p-farmer-registry.md](releases/history/develop/openg2p-farmer-registry.md)

## 2026-11-04

### openg2p-farmer-registry 1.0.0-dev.22

Previous version: 1.0.0-dev.21.

- Farmer registry images 262e0d949a99 on platform 1.2.2-rc.625 (#94) (274ee86)

## 2026-11-04

### openg2p-commons-services 1.0.0-dev.35

Previous version: 1.0.0-dev.34.

- Point the Master Data staff-portal tile at the UI (#92) (0071008)

## 2026-11-04

### openg2p-commons-services 1.0.0-dev.34

Previous version: 1.0.0-dev.33.

- Master Data seed image with the livestock species and breeds (#89) (e2360eb)

## 2026-11-04

### openg2p-farmer-registry 1.0.0-dev.21

Previous version: 1.0.0-dev.20.

- Move the Farmer registry to the OpenG2P registry chart 1.2.2-rc.625 (#79) (10eff85)

## 2026-11-03

### openg2p-cropsown-registry 1.0.0-dev.20

Previous version: 1.0.0-dev.19.

- Map every source of income for Crop Sown and Livestock (#80) (180c9b8)

### openg2p-livestock-registry 1.0.0-dev.22

Previous version: 1.0.0-dev.21.

- Map every source of income for Crop Sown and Livestock (#80) (180c9b8)

## 2026-11-03

### openg2p-cropsown-registry 1.0.0-dev.19

Previous version: 1.0.0-dev.18.

- Map every Farmer-tab field and the photo for Crop Sown and Livestock (#76) (2d0d359)

### openg2p-livestock-registry 1.0.0-dev.21

Previous version: 1.0.0-dev.20.

- Map every Farmer-tab field and the photo for Crop Sown and Livestock (#76) (2d0d359)

## 2026-11-02

### openg2p-commons-services 1.0.0-dev.33

Previous version: 1.0.0-dev.32.

- Master Data seed image with Mixed / Not Applicable in the livestock sex list (#72) (c07a692)

## 2026-11-02

### openg2p-livestock-registry 1.0.0-dev.20

Previous version: 1.0.0-dev.19.

- Livestock: application reference format and reporting labels from Master Data (#71) (76f764c)

## 2026-11-02

### openg2p-commons-services 1.0.0-dev.32

Previous version: 1.0.0-dev.31.

- Master Data seed image with the livestock event and status lists (356e643)

## 2026-11-02

### openg2p-commons-services 1.0.0-dev.31

Previous version: 1.0.0-dev.30.

- Create the DA Services backend Keycloak client with its DA registry roles (b91170d)

## 2026-10-30

### openg2p-commons-services 1.0.0-dev.30

Previous version: 1.0.0-dev.29.

- feat(commons-services): add iam-bene-portal-api (image 1.1.0) (#59) (7fb788d)

## 2026-10-30

### openg2p-commons-services 1.0.0-dev.29

Previous version: 1.0.0-dev.28.

- Derive chart default hosts from global.baseDomain (#57) (5d8630e)

### openg2p-farmer-registry 1.0.0-dev.20

Previous version: 1.0.0-dev.19.

- Derive chart default hosts from global.baseDomain (#57) (5d8630e)

## 2026-10-30

### openg2p-commons-services 1.0.0-dev.28

Previous version: 1.0.0-dev.27.

- Create the registry connector's Keycloak clients and admin role in Commons (7a1d776)

## 2026-10-29

### openg2p-livestock-registry 1.0.0-dev.19

Previous version: 1.0.0-dev.18.

- Run the Livestock schema and data migrations as an upgrade hook (#50) (9ab4814)

## 2026-10-29

### openg2p-da-registry 1.0.0-dev.20

Previous version: 1.0.0-dev.19.

- Drop the retired DA import auto-approve switch from the DA registry chart values (#48) (7470500)

## 2026-10-29

### openg2p-cropsown-registry 1.0.0-dev.18

Previous version: 1.0.0-dev.17.

- Move the Farmer, Crop Sown, Livestock and DA registries to the OpenG2P registry chart 1.2.2-rc.614 (4071396)

### openg2p-da-registry 1.0.0-dev.19

Previous version: 1.0.0-dev.18.

- Move the Farmer, Crop Sown, Livestock and DA registries to the OpenG2P registry chart 1.2.2-rc.614 (4071396)

### openg2p-farmer-registry 1.0.0-dev.19

Previous version: 1.0.0-dev.18.

- Move the Farmer, Crop Sown, Livestock and DA registries to the OpenG2P registry chart 1.2.2-rc.614 (4071396)

### openg2p-livestock-registry 1.0.0-dev.18

Previous version: 1.0.0-dev.17.

- Move the Farmer, Crop Sown, Livestock and DA registries to the OpenG2P registry chart 1.2.2-rc.614 (4071396)

## 2026-10-29

### openg2p-da-registry 1.0.0-dev.18

Previous version: 1.0.0-dev.17.

- Give the DA chart the platform version as its app version, as the other registry charts have (#41) (dd414b9)

## 2026-10-29

### openg2p-da-registry 1.0.0-dev.17

Previous version: 1.0.0-dev.16.

- Move the DA chart to registry platform 1.2.2-rc.557 and pin the live dev settings (#39) (1160613)

## 2026-10-28

### openg2p-commons-services 1.0.0-dev.27

Previous version: 1.0.0-dev.26.

- Seed Master Data from the unified ETH-OAN pack (61a191e)

## 2026-10-28

### openg2p-commons-services 1.0.0-dev.26

Previous version: 1.0.0-dev.25.

- Run the Commons upgrade gate on OpenG2P's released sanity image (#32) (23ec863)

## 2026-10-27

### openg2p-livestock-registry 1.0.0-dev.17

Previous version: 1.0.0-dev.16.

- Wire the Farmer reference on New Dev for Crop Sown and Livestock (74761c9)

## 2026-10-27

### openg2p-cropsown-registry 1.0.0-dev.17

Previous version: 1.0.0-dev.16.

- Let the Crop Sown chart install and carry the Farmer-reference configuration (6af1b72)

### openg2p-farmer-registry 1.0.0-dev.18

Previous version: 1.0.0-dev.17.

- Let the Crop Sown chart install and carry the Farmer-reference configuration (6af1b72)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.25

Previous version: 1.0.0-dev.24.

- Commons: seed the farmer registry's document, phone and finance lists (1654d38)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.24

Previous version: 1.0.0-dev.23.

- feat(commons): make every Job safe for one-click Rancher upgrades (754a463)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.23

Previous version: 1.0.0-dev.22.

- feat(commons): carry the PM session-cookie guard in the chart (da85a05)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.22

Previous version: 1.0.0-dev.21.

- feat(commons): make the chart defaults the dev configuration (3448835)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.21

Previous version: 1.0.0-dev.20.

- Configure Fayda (eSignet) sign-in from values for the farmer registry and New Dev (7d2c2af)

### openg2p-farmer-registry 1.0.0-dev.17

Previous version: 1.0.0-dev.16.

- Configure Fayda (eSignet) sign-in from values for the farmer registry and New Dev (7d2c2af)
- Let the farmer chart render and install without the preserving-adoption gate (14d75c1)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.20

Previous version: 1.0.0-dev.19.

- feat(commons): promote Commons Services with Master Data 0.0.0-develop.118 (d6b6b67)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.19

Previous version: 1.0.0-dev.18.

- fix: keep chart archives small enough for Rancher (5137428)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.18

Previous version: 1.0.0-dev.17.

- chore: remove the Master Data snapshot and Crop lookup reference (a7c0f1d)

## 2026-10-27

### openg2p-commons-services 1.0.0-dev.17

Previous version: 1.0.0-dev.16.

- fix(commons): vendor the published Master Data develop.118 dependency (2008980)
- Change repository and version for master-data dependency (e5e405f)
