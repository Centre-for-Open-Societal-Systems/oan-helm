"""Commons staging delivery: the pinned chart exists and is sealed, and the guard names every saved key that would drop."""
import hashlib
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts/ci'))
import commons_values_guard as guard


class DeliverStagingCommons(unittest.TestCase):
    def test_pinned_chart_is_in_the_repository_and_sealed(self):
        version = (ROOT / 'environments/staging/commons-services.chart').read_text(encoding='utf-8').strip()
        archive = f'openg2p-commons-services-{version}.tgz'
        sums = dict(line.split('  ', 1)[::-1] for line in
                    (ROOT / 'repository/SHA256SUMS').read_text(encoding='utf-8').splitlines() if '  ' in line)
        self.assertIn(archive, sums)
        self.assertEqual(hashlib.sha256((ROOT / 'repository' / archive).read_bytes()).hexdigest(), sums[archive])

    def test_guard_names_saved_keys_no_file_sets(self):
        saved = {'keymanager': {'p12KeystorePass': 'x'}, 'master-data': {'geoSeed': {'load': {'samples': False}}}}
        overlay = {'master-data': {'geoSeed': {'load': {'samples': True}}}}
        self.assertEqual(guard.missing(saved, [overlay]), ['keymanager.p12KeystorePass'])
        self.assertEqual(guard.missing(saved, [overlay, {'keymanager': {'p12KeystorePass': 'y'}}]), [])
        self.assertEqual(guard.missing(None, [overlay]), [])

    def test_delivery_never_reuses_saved_values(self):
        script = (ROOT / 'scripts/ci/deliver_staging_commons.sh').read_text(encoding='utf-8')
        self.assertIn('--reset-values', script)
        self.assertIn('--atomic', script)
        self.assertNotIn('--reuse-values', script)
        self.assertIn('commons_values_guard.py', script)


if __name__ == '__main__':
    unittest.main()
