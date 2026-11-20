"""New Dev Master Data serves its public catalogue in the cluster only.

The registry dashboards read the map boundaries and the location units from
Master Data's public catalogue (MASTER_DATA_URL, GET /public/geography/...).
With the catalogue off, every /public route answers 404 and the dashboards show
"Error loading map". The catalogue stays reachable in the cluster only: no
public host is added.
"""
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VALUES = ROOT / 'environments/dev/values/commons-services.yaml'


class DevMasterDataCatalogue(unittest.TestCase):
    def setUp(self):
        values = yaml.safe_load(VALUES.read_text(encoding='utf-8'))
        self.catalogue = values['master-data']['masterDataAPI']['catalogue']

    def test_the_public_catalogue_is_on(self):
        self.assertIs(self.catalogue['public']['enabled'], True)

    def test_no_public_host_is_added(self):
        public = self.catalogue['public']
        self.assertNotIn('istio', public)
        self.assertNotIn('baseUrl', public)

    def test_approval_and_boundary_settings_stay_the_chart_defaults(self):
        # The one change: the boundary store is Garage (the Commons object store) instead of MinIO's default endpoint.
        self.assertEqual(set(self.catalogue), {'public', 'boundaryStore'})
        self.assertEqual(self.catalogue['boundaryStore'], {'endpoint': 'http://commons-garage:3900'})


if __name__ == '__main__':
    unittest.main()
