# Consolidated Helm review

PR16 is the single review for the author's six previously open proposals.
All original heads are retained through normal merge commits; no branch was
force-pushed and no source branch was deleted. PR15 is by another author and
is outside this consolidation.

| Original PR | Original head | Combined treatment |
| --- | --- | --- |
| 7: Consent staff tile | 3f576fc199b4e6bc0a660122dd5abc10304a81a4 | Retain catalog hook, Secret reference, HTTP regressions and bytecode-safe package seals. No user grants. |
| 8: Registry staff hooks | 541884c79e308a634dbc2953c15f29431b40f141 | Retain proposal disabled, adapt image lookup to the native registry alias, document unavailable legacy seed script. Reject this hook during preserving adoption. |
| 11: ETH-OAN seed | 2ec64ff39f715f12febb2871189b92d236eb2f79 | Existing current image/digest, pack, questions and preservation gates retained; original review history joined. |
| 12: Registrant Redis | 75790a116163c8dbe83cfe2408cda6195c3cf540 | Existing four registry defaults/dev settings retained without deleting Farmer validation. |
| 13: Coded-value validation | 569e975760909a373d5e406543b4b89e565cb6bf | Existing Farmer flag retained. Verify code-valued selects/current Master Data before live acceptance; do not rewrite original records to satisfy validation. |
| 16: Farmer adoption | 2131656b0c24ddd5bcdb4544b129acc9832a78a0 | Retain server-generated expiring receipt, exact source/chart/image binding, fresh backup and record-preservation requirements. |

The immutable release train advances to dev.16. Existing canonical archives,
including dev.7/dev.8 variants already in main and dev.15, are preserved byte
for byte. Different historical proposal builds with the same package filename
remain recoverable from their original parent commits; they do not overwrite
the canonical repository artifact. The cumulative index contains one selected
digest per name/version.

The later merged validation workflow is retained rather than reintroducing an
old branch-name-only rule. Candidate tests/package checks still run, while a
stable main release still requires its release-ready evidence. Candidate
publication does not claim application or preservation acceptance.

Farmer-first deployment remains separate from review consolidation. Crop,
Livestock and Commons default promotion gates remain closed. The Consent tile
is default-off in the shared chart and enabled only by the existing dev overlay.
No Helm/Kubernetes upgrade or identity assignment is performed by this merge.
