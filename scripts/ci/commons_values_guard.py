"""Fail if a release's saved values hold a key that the delivery's values do not set.

--reset-values replaces the saved values with the files given, so a key set only by an earlier hand upgrade would be
dropped silently. Both inputs are JSON: the saved values from `helm get values -o json`, and the merged value files
rendered by helm itself (deliver_staging_commons.sh), so this needs no YAML library. Only key names are printed.

A key that was renamed or removed on purpose is listed, with its reason, in the release's retired-keys file
(environments/staging/<release>.retired-keys: one key per line, `#` comments). A listed key, and every key under it,
may be dropped; anything else still fails.

    commons_values_guard.py <saved values json> <merged values json> [retired-keys file]
"""
import json
import sys


def keys(document, prefix=""):
    if isinstance(document, dict) and document:
        for name, value in document.items():
            yield from keys(value, f"{prefix}.{name}" if prefix else str(name))
    elif prefix:
        yield prefix


def retired_keys(path):
    if not path:
        return []
    with open(path, encoding="utf-8") as handle:
        return [line.split("#", 1)[0].strip() for line in handle if line.split("#", 1)[0].strip()]


def missing(saved, given, retired=()):
    have = set(keys(given or {}))
    def is_retired(key):
        return any(key == r or key.startswith(r + ".") for r in retired)
    return sorted(k for k in keys(saved or {}) if k not in have and not is_retired(k))


def main(argv):
    documents = []
    for path in argv[1:3]:
        with open(path, encoding="utf-8") as handle:
            documents.append(json.load(handle))
    retired = retired_keys(argv[3] if len(argv) > 3 else None)
    lost = missing(*documents, retired)
    if lost:
        print("FAIL: --reset-values would drop saved keys that no value file sets: " + ", ".join(lost), file=sys.stderr)
        return 1
    print("saved values are all set by the value files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
