#!/usr/bin/env python3
"""Point New Dev at the newest released commons-services chart.

    python scripts/ci/pin_dev_chart.py [repository root]

Run by the release workflow after it has released and validated the charts. New Dev
follows environments/dev/commons-services.chart, so without this every chart change
needs a second pull request that only edits that file. Now the release commit moves
the pin itself, and ci/jenkins/dev-commons.Jenkinsfile delivers it.

The pin moves only to the commons-services chart version in charts/ when
  - it is in the 1.0.0-dev.<n> series,
  - its archive is in repository/ and listed in repository/SHA256SUMS (what the
    delivery verifies), and
  - it is newer than the current pin.
Otherwise nothing changes. Prints 'pinned <version>' or 'unchanged <reason>'.
Staging is not touched: it is promoted by hand after New Dev is verified.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CHART = "openg2p-commons-services"
SERIES = re.compile(r"1\.0\.0-dev\.(\d+)")


def chart_version(root: Path) -> str:
    text = (root / "charts" / CHART / "Chart.yaml").read_text(encoding="utf-8")
    m = re.search(r"^version:\s*(\S+)\s*$", text, re.M)
    if not m:
        raise SystemExit(f"no version in charts/{CHART}/Chart.yaml")
    return m.group(1)


def run(root: Path) -> str:
    version = chart_version(root)
    m = SERIES.fullmatch(version)
    if not m:
        return f"unchanged {version} is not in the 1.0.0-dev series"
    archive = f"{CHART}-{version}.tgz"
    if not (root / "repository" / archive).is_file():
        return f"unchanged {archive} is not in repository/"
    sums = (root / "repository" / "SHA256SUMS").read_text(encoding="utf-8")
    if not re.search(rf"^[0-9a-f]{{64}}\s+\*?{re.escape(archive)}$", sums, re.M):
        return f"unchanged {archive} is not in repository/SHA256SUMS"
    pin = root / "environments" / "dev" / "commons-services.chart"
    current = pin.read_text(encoding="utf-8").strip() if pin.exists() else ""
    cm = SERIES.fullmatch(current)
    if cm and int(cm.group(1)) >= int(m.group(1)):
        return f"unchanged New Dev already follows {current}"
    pin.write_text(version + "\n", encoding="utf-8", newline="")
    return f"pinned {version}"


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parents[2]
    print(run(root))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
