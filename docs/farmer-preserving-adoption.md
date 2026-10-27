# Farmer preserving New Dev adoption

Farmer source PR124 and publication follow-up PR127 are merged. Jenkins31
published all six images from afdbf75a73227ef0e3a0dfe6824918aee04b70a1, with
the native worker SAVE/parent/finance/rollback test passing in that exact image.
The published staff API and seed images were then rehearsed against isolated
fresh and original restored databases and a real restored MinIO service.
Migration ran twice per database; the full shipped seed entrypoint ran twice
per database with zero SQL errors. All 73 original business tables and 581
unrelated objects were unchanged; six uploaded templates matched their source
bytes. Original AWE rows survived except the native callback metadata timestamp.
This is preparation evidence, not a live application upgrade.

The dev.16 Farmer chart adds one narrow admission path. Default renders and
fresh installs remain blocked, as do Crop and Livestock candidates.
Only an upgrade named farmer-registry in namespace farmer may request
farmerAdoption.mode=preserving-upgrade. The chart reads the live ConfigMap
registry-preserve-farmer; a user value cannot manufacture that receipt.
The locked NATIVE_READY receipt must identify the exact New Dev cluster,
source commit, dev.16 chart version/archive hash, all six image digests,
verified backup and preserved business records. Admission expires after the
controller's bounded cutover window. Every application/hook image must match
the receipt. The original dev.14 archive remains immutable and blocked.

The existing Farmer Jenkins deployment pipeline owns preparation and receipt
creation. It must pause the discovered Farmer writers/producers, take a fresh
coordinated configuration/database/filestore backup and verify restoration,
run native additive migration and the shipped seed with existing credentials,
verify original business values, and compare the candidate manifest with the
installed release. Only then may it persist NATIVE_READY and call Helm.
First-install reset receipts do not authorize this adoption. Existing databases,
documents, history, pending approvals, checkpoints and identity grants are
preserved. No upstream platform code or worker is replaced.

The receipt is an operational lock, not a general promotion flag. If an
operation fails, keep writers paused and the protected recovery evidence;
never retry a database drop, forge a completed receipt, or automatically roll
back a schema change. Staging requires a separate rehearsal and release gate.
