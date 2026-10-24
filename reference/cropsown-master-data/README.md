# Preserved Crop lookup catalog

These two files are copied without modification from the recorded Crop source;
`source.json` pins their hashes and source commit. They retain all attribute and
option IDs, codes, labels and hierarchy relationships for reconciliation.

They are not included in registry seeding or executed by any chart. The native
registry uses the Master Data service API and does not own these legacy tables.
Use supported Master Data administration to reconcile/import missing catalog
values after comparing the existing environment. Never execute this reference
SQL against a registry or recreate a local platform lookup implementation.
