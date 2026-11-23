"""New Dev follows the newest released commons-services chart: python -m unittest scripts/test_pin_dev_chart.py"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "ci"))
import pin_dev_chart  # noqa: E402

CHART = "openg2p-commons-services"


def tree(version="1.0.0-dev.52", pin="1.0.0-dev.51", archive=True, listed=True):
    root = Path(tempfile.mkdtemp())
    (root / "charts" / CHART).mkdir(parents=True)
    (root / "charts" / CHART / "Chart.yaml").write_bytes(f"name: {CHART}\nversion: {version}\n".encode())
    (root / "repository").mkdir()
    if archive:
        (root / "repository" / f"{CHART}-{version}.tgz").write_bytes(b"x")
    sums = f"{'a' * 64}  {CHART}-{version}.tgz\n" if listed else f"{'a' * 64}  other-1.0.0.tgz\n"
    (root / "repository" / "SHA256SUMS").write_bytes(sums.encode())
    (root / "environments" / "dev").mkdir(parents=True)
    if pin is not None:
        (root / "environments/dev/commons-services.chart").write_bytes((pin + "\n").encode())
    return root


def pinned(root):
    return (root / "environments/dev/commons-services.chart").read_bytes().decode()


class PinDevChart(unittest.TestCase):
    def test_moves_to_the_released_chart(self):
        root = tree()
        self.assertEqual(pin_dev_chart.run(root), "pinned 1.0.0-dev.52")
        self.assertEqual(pinned(root), "1.0.0-dev.52\n")

    def test_creates_the_pin_when_missing(self):
        root = tree(pin=None)
        self.assertEqual(pin_dev_chart.run(root), "pinned 1.0.0-dev.52")

    def test_same_version_changes_nothing(self):
        root = tree(pin="1.0.0-dev.52")
        self.assertTrue(pin_dev_chart.run(root).startswith("unchanged"))
        self.assertEqual(pinned(root), "1.0.0-dev.52\n")

    def test_never_moves_back(self):
        root = tree(version="1.0.0-dev.52", pin="1.0.0-dev.60")
        self.assertTrue(pin_dev_chart.run(root).startswith("unchanged"))
        self.assertEqual(pinned(root), "1.0.0-dev.60\n")

    def test_compares_numbers_not_text(self):
        root = tree(version="1.0.0-dev.100", pin="1.0.0-dev.99")
        self.assertEqual(pin_dev_chart.run(root), "pinned 1.0.0-dev.100")

    def test_needs_the_archive_and_its_checksum(self):
        for kwargs in ({"archive": False}, {"listed": False}):
            root = tree(**kwargs)
            self.assertTrue(pin_dev_chart.run(root).startswith("unchanged"), kwargs)
            self.assertEqual(pinned(root), "1.0.0-dev.51\n")

    def test_only_the_dev_series(self):
        for version in ("1.0.0", "1.0.1-dev.1", "2.0.0-dev.3", "1.0.0-rc.4"):
            root = tree(version=version)
            self.assertTrue(pin_dev_chart.run(root).startswith("unchanged"), version)
            self.assertEqual(pinned(root), "1.0.0-dev.51\n")

    def test_the_real_repository_pin_is_consistent(self):
        root = Path(__file__).resolve().parents[1]
        pin = (root / "environments/dev/commons-services.chart").read_text(encoding="utf-8").strip()
        self.assertRegex(pin, r"1\.0\.0-dev\.\d+")
        self.assertTrue((root / "repository" / f"{CHART}-{pin}.tgz").is_file(), "the pinned chart is not in repository/")


if __name__ == "__main__":
    unittest.main()
