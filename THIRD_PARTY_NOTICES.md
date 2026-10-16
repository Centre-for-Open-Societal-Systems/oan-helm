# Imported sources

Repository integration files use the root MIT license. Imported chart sources
retain their own licenses; the root license does not replace them.

| Chart | Source | Included license |
| --- | --- | --- |
| Farmer | COSS `farmer-registry` | MPL-2.0, `charts/openg2p-farmer-registry/LICENSE` |
| Crop Sown | COSS `cropsown-regsitry` | MIT, `charts/openg2p-cropsown-registry/LICENSE` |
| Livestock | COSS `livestock-registry` | MIT, `charts/openg2p-livestock-registry/LICENSE` |
| DA | COSS `da-registry` | MPL-2.0, `charts/openg2p-da-registry/LICENSE` |
| Commons Services | OpenG2P `commons` | MPL-2.0, `charts/openg2p-commons-services/LICENSE` |

Bundled dependencies retain their upstream notices. Source commits, dependency
versions and original-file hashes are in `releases/provenance.json`. COSS changes
set repository chart versions, pin verified component images, add disabled
optional workloads and image/Secret configuration, correct DA's UI values key,
and exclude environment captures from packages. Source code remains available
in this repository and at the recorded upstream commits.
