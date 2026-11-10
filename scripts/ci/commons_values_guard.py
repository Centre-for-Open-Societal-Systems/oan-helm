"""Fail if a release's saved values hold a key that the delivery's values do not set.

--reset-values replaces the saved values with the files given, so a key set only by an earlier hand upgrade would be
dropped silently. Both inputs are JSON: the saved values from `helm get values -o json`, and the merged value files
rendered by helm itself (deliver_staging_commons.sh), so this needs no YAML library. Only key names are printed.

    commons_values_guard.py <saved values json> <merged values json>
"""
import json
import sys


def keys(document, prefix=""):
    if isinstance(document, dict) and document:
        for name, value in document.items():
            yield from keys(value, f"{prefix}.{name}" if prefix else str(name))
    elif prefix:
        yield prefix


def missing(saved, given):
    have = set(keys(given or {}))
    return sorted(k for k in keys(saved or {}) if k not in have)


def main(argv):
    documents = []
    for path in argv[1:3]:
        with open(path, encoding="utf-8") as handle:
            documents.append(json.load(handle))
    lost = missing(*documents)
    if lost:
        print("FAIL: --reset-values would drop saved keys that no value file sets: " + ", ".join(lost), file=sys.stderr)
        return 1
    print("saved values are all set by the value files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
