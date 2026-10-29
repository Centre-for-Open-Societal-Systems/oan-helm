# Changelog

Chart releases, newest first. Each entry is written by `scripts/release.py`
when a merge to `main` changes a chart: the chart gets its next version, its
archive is added to `repository/`, and the commits that touched it are listed
here. Releases up to `1.0.0-dev.16` were published as one release train; their
notes are under `releases/<version>.yaml`.

<!-- Releases are inserted below this line by scripts/release.py. -->

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
