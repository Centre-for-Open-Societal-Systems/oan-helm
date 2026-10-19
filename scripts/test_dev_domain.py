"""Safety checks for the legacy URL-only Helm post-renderer."""
import base64
import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('renderer',Path(__file__).with_name('dev-domain-post-renderer.py'))
renderer=importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class DomainMigrationTests(unittest.TestCase):
    def test_private_route_stays_private(self):
        original={'kind':'VirtualService','spec':{'hosts':['dashboard-api.crop.openg2p.test'],'gateways':['crop/internal'],'http':[{'route':[{'destination':{'host':'cropsown-registry-dashboard-api','port':{'number':80}}}]}]}}
        self.assertEqual(renderer.transform(original),original)

    def test_public_route_changes_host_and_gateway_preserving_destination(self):
        old={'kind':'VirtualService','spec':{'hosts':['staff-farmer-development.oanstaging.com'],'gateways':['internal'],'http':[{'route':[{'destination':{'host':'farmer-registry-staff-portal-api','port':{'number':80}}}]}]}}
        migrated=renderer.transform(old)
        self.assertEqual(migrated['spec']['hosts'],['staff-farmer.development.oanstaging.com'])
        self.assertEqual(migrated['spec']['gateways'],['istio-system/development'])
        self.assertEqual(migrated['spec']['http'],old['spec']['http'])

    def test_mixed_private_public_hosts_are_rejected(self):
        with self.assertRaises(AssertionError):
            renderer.transform({'kind':'VirtualService','spec':{'hosts':['staff-farmer-development.oanstaging.com','dashboard-api.crop.openg2p.test'],'gateways':['internal']}})

    def test_cookie_scope_and_images(self):
        old={'image':'registry.example/component:keep-this-tag','env':[{'name':'IAM_STAFF_AUTH_COOKIE_DOMAIN','value':'.oanstaging.com'},{'name':'UNCHANGED','value':'custom-value'}]}
        migrated=renderer.transform(old)
        self.assertEqual(migrated['image'],old['image'])
        self.assertEqual(migrated['env'][0]['value'],'.development.oanstaging.com')
        self.assertEqual(migrated['env'][1],old['env'][1])

    def test_encoded_login_config_and_binary_secret(self):
        login=base64.b64encode(b'{"issuer":"https://keycloak-development.oanstaging.com/realms/staff"}').decode()
        binary=base64.b64encode(b'\xff\x00\x80test').decode()
        migrated=renderer.transform({'kind':'Secret','data':{'login.json':login,'binary':binary}})
        self.assertIn(b'https://keycloak.development.oanstaging.com/realms/staff',base64.b64decode(migrated['data']['login.json']))
        self.assertEqual(migrated['data']['binary'],binary)
        self.assertEqual(renderer.transform({'kind':'Secret','data':None})['data'],None)


if __name__=='__main__':unittest.main()
