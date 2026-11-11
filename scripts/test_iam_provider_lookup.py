"""The public IAM staff API never resolves token issuers through itself.

OpenG2P's iam_core falls back to {auth provider URL}/identity-providers/get_provider_by_issuer
when an issuer is missing from login_providers, and does not cache the miss. Pointing that URL
at the same IAM makes every unknown issuer recurse without end, so the public IAM asks an
internal copy whose own URL is empty.
"""
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CHART = ROOT / 'charts/openg2p-commons-services'
PUBLIC = 'http://commons-services-iam-staff-portal-api'
INTERNAL = PUBLIC + '-internal'


class IamProviderLookup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.values = yaml.safe_load((CHART / 'values.yaml').read_text(encoding='utf-8'))

    def test_public_iam_asks_the_internal_copy(self):
        env = self.values['openg2p-iam-service']['iamStaffPortalApi']['envVars']
        self.assertEqual(env['IAM_STAFF_AUTH_PROVIDER_API_URL'], INTERNAL)
        # Inside the IAM, iam_core reads the IAM's own settings (IAM_STAFF_ prefix); a COMMON_ value is never used.
        self.assertNotIn('COMMON_AUTH_PROVIDER_API_URL', env)

    def test_internal_copy_has_no_fallback_route_or_init(self):
        internal = self.values['openg2p-iam-service-internal']
        api = internal['iamStaffPortalApi']
        self.assertEqual(api['envVars']['IAM_STAFF_AUTH_PROVIDER_API_URL'], '')
        self.assertEqual(api['nameOverride'], 'iam-staff-portal-api-internal')
        self.assertIs(api['istio']['enabled'], False)
        self.assertEqual(api['loginProviders'], [])
        # The public instance runs migrations and the data loader; the copy only serves.
        self.assertNotIn('migrate', ' '.join(api['command']))
        for part in ('iamAgentPortalApi', 'iamStaffUi', 'keycloak-init', 'postgres-init'):
            self.assertIs(internal[part]['enabled'], False, part)
        self.assertEqual(internal['global'], self.values['openg2p-iam-service']['global'])

    def test_internal_copy_is_the_same_upstream_chart(self):
        deps = yaml.safe_load((CHART / 'Chart.yaml').read_text(encoding='utf-8'))['dependencies']
        public = next(d for d in deps if d['name'] == 'openg2p-iam-service' and 'alias' not in d)
        internal = next(d for d in deps if d.get('alias') == 'openg2p-iam-service-internal')
        self.assertEqual((internal['name'], internal['repository'], internal['version']),
                         (public['name'], public['repository'], public['version']))

    def test_environment_overlays_give_the_copy_the_same_urls(self):
        for env in ('dev', 'staging'):
            overlay = yaml.safe_load((ROOT / f'environments/{env}/values/commons-services.yaml').read_text(encoding='utf-8'))
            self.assertEqual(overlay['openg2p-iam-service-internal']['global'],
                             overlay['openg2p-iam-service']['global'], env)


if __name__ == '__main__':
    unittest.main()
