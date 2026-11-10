"""Fail if a release's saved values hold a key that the delivery's value files do not set.

--reset-values replaces the saved values with the files given, so a key set only by an earlier hand upgrade would be
dropped silently. Only key names are printed, never values.

    commons_values_guard.py <saved values json> <values file> [<values file> ...]
"""
import json
import sys

import yaml


def keys(document, prefix=""):
    if isinstance(document, dict) and document:
        for name, value in document.items():
            yield from keys(value, f"{prefix}.{name}" if prefix else str(name))
    elif prefix:
        yield prefix


def missing(saved, files):
    given = set()
    for document in files:
        given |= set(keys(document or {}))
    return sorted(k for k in keys(saved or {}) if k not in given)


def main(argv):
    with open(argv[1], encoding="utf-8") as handle:
        saved = json.load(handle)
    files = []
    for path in argv[2:]:
        with open(path, encoding="utf-8") as handle:
            files.append(yaml.safe_load(handle))
    lost = missing(saved, files)
    if lost:
        print("FAIL: --reset-values would drop saved keys that no value file sets: " + ", ".join(lost), file=sys.stderr)
        return 1
    print("saved values are all set by the value files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
