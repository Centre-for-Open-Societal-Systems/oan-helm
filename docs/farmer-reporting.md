# Farmer reporting ownership

The Farmer registry seed image ships OAN reporting SQL and its geography-label
synchronizer. The central chart creates views in an explicit post-install/upgrade
hook, after schema and metadata seed. Its normal refresh CronJob retains the
existing dependency order and reporting API view names.

`fr_rpt_farmer`, `fr_rpt_land` and `fr_rpt_farmer_main_crop` keep their reporting
contracts. Native Farmer crop children contribute registration commodities;
retained legacy main-crop declarations remain readable. Plural coded answers
remain available as JSON lists. View replacement is transactional, restores
reader ACLs/owners, and refuses unknown dependents instead of cascading them.

`fr_rpt_geo_levels(depth, level_name)` is synchronized through the supported
Master Data `/geo/get_all_geo_levels` HTTP contract, with client credentials.
Labels come from the configured hierarchy even on an empty registry. Missing,
ambiguous or unavailable definitions block the hook; no country or level fallback
is invented. The reporting client defaults to the existing registry-owned analytics API client;
configure an IAM-managed read-only reporting account/Secret when provisioned.
No Master Data database credentials are passed to this job. Registry DB and MDS
credentials use separate existing Secret references. Configure
`analytics.imagePullSecrets` when the seed image requires namespace pull access.

Local native PostgreSQL checks cover two complete metadata passes, additive list
backfill across register/history/intake, reporting replay, aggregate relationships,
reader-grant preservation and concurrent refresh. The real HTTP client also ran
against a Postman stand-in for OAuth and the native MDS envelope, including
unavailability/refusal cases. These checks do not establish a deployed hook,
current MDS service-account grants or authenticated live dashboard acceptance.
Farmer/Crop/Livestock promotion gates remain closed.
