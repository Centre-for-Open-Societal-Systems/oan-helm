"""Exercise the ODK bootstrap Job against a fake ODK Central and a fake Kubernetes API, without a cluster.

Runs addons/odk-bootstrap/files/odk_bootstrap.js with Node.js (skipped where Node.js is missing). Central's account task
is replaced by a stub module that records the calls.
"""
import base64
import json
import os
import shutil
import subprocess
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CHART = ROOT / 'addons/odk-bootstrap'
SCRIPT = CHART / 'files/odk_bootstrap.js'
NODE = shutil.which('node')

STUB = """
const fs = require('fs');
const log = (line) => fs.appendFileSync(process.env.ACCOUNT_LOG, line + '\\n');
module.exports = {
  createUser: async (email) => { log('create ' + email); if (fs.existsSync(process.env.ACCOUNT_LOG + '.exists')) throw new Error('exists'); fs.writeFileSync(process.env.ACCOUNT_LOG + '.exists', ''); },
  setUserPassword: async (email, password) => { log('password ' + email); fs.writeFileSync(process.env.ACCOUNT_LOG + '.password', password); },
  promoteUser: async (email) => { log('promote ' + email); if (fs.existsSync(process.env.ACCOUNT_LOG + '.admin')) throw new Error('duplicate key value violates unique constraint "assignments_pkey"'); fs.writeFileSync(process.env.ACCOUNT_LOG + '.admin', ''); },
};
"""


class FakeWorld:
    def __init__(self):
        self.projects = {1: {'id': 1, 'name': 'Farmer Registry', 'archived': False}}
        self.forms = {(1, 'farmer_profile')}
        self.app_users = {}
        self.assignments = set()
        self.secrets = {}
        self.sessions = set()
        self.calls = []
        self.next_id = 100
        self.unavailable = 0


def serve(handler):
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


class OdkBootstrapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not NODE:
            raise unittest.SkipTest('Node.js is not installed')

    def setUp(self):
        world = self.world = FakeWorld()
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        owner = self

        class Central(BaseHTTPRequestHandler):
            def log_message(self, *_):
                pass

            def reply(self, status, payload=None):
                body = json.dumps(payload).encode() if payload is not None else b''
                self.send_response(status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def body(self):
                n = int(self.headers.get('Content-Length') or 0)
                return json.loads(self.rfile.read(n)) if n else None

            def authorised(self):
                token = (self.headers.get('Authorization') or '').removeprefix('Bearer ')
                return token in world.sessions

            def handle_any(self, method):
                path = unquote(urlsplit(self.path).path)
                world.calls.append((method, path))
                body = self.body()
                if world.unavailable:
                    world.unavailable -= 1
                    return self.reply(503, {})
                parts = path.strip('/').split('/')
                if method == 'POST' and path == '/v1/sessions':
                    expected = Path(owner.tmp, 'account.log.password').read_text()
                    if body != {'email': 'oan-bootstrap@odk.test', 'password': expected}:
                        return self.reply(401, {'code': 401.2})
                    token = f'session-{len(world.sessions) + 1}'
                    world.sessions.add(token)
                    return self.reply(200, {'token': token})
                if method == 'DELETE' and parts[:2] == ['v1', 'sessions']:
                    world.sessions.discard(parts[2])
                    return self.reply(200, {'success': True})
                if not self.authorised():
                    return self.reply(403, {'code': 403.1})
                if path == '/v1/projects':
                    if method == 'GET':
                        return self.reply(200, list(world.projects.values()))
                    world.next_id += 1
                    world.projects[world.next_id] = {'id': world.next_id, 'name': body['name'], 'archived': False}
                    return self.reply(200, world.projects[world.next_id])
                project = int(parts[2])
                if parts[3] == 'app-users':
                    if method == 'GET':
                        return self.reply(200, [u for u in world.app_users.values() if u['projectId'] == project])
                    world.next_id += 1
                    user = {'id': world.next_id, 'projectId': project, 'displayName': body['displayName'],
                            'token': f'tok{world.next_id}'}
                    world.app_users[world.next_id] = user
                    return self.reply(200, user)
                form = parts[4]
                if (project, form) not in world.forms:
                    return self.reply(404, {'code': 404.1})
                if len(parts) == 5:
                    return self.reply(200, {'xmlFormId': form})
                if method == 'GET':
                    return self.reply(200, [{'actorId': a} for (p, f, a) in world.assignments if (p, f) == (project, form)])
                world.assignments.add((project, form, int(parts[7])))
                return self.reply(200, {'success': True})

            def do_GET(self):
                self.handle_any('GET')

            def do_POST(self):
                self.handle_any('POST')

            def do_DELETE(self):
                self.handle_any('DELETE')

        class Kube(BaseHTTPRequestHandler):
            def log_message(self, *_):
                pass

            def reply(self, status, payload):
                body = json.dumps(payload).encode()
                self.send_response(status)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                owner.assertEqual(self.headers['Authorization'], 'Bearer sa-token')
                name = self.path.rsplit('/', 1)[1]
                if name in world.secrets:
                    return self.reply(200, world.secrets[name])
                self.reply(404, {'kind': 'Status'})

            def do_POST(self):
                secret = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
                owner.assertTrue(self.path.startswith('/api/v1/namespaces/commons/secrets'))
                world.secrets[secret['metadata']['name']] = secret
                world.calls.append(('SECRET', 'create'))
                self.reply(201, secret)

            def do_PUT(self):
                secret = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
                world.secrets[secret['metadata']['name']] = secret
                world.calls.append(('SECRET', 'update'))
                self.reply(200, secret)

        self.central = serve(Central)
        self.kube = serve(Kube)
        self.addCleanup(self.central.shutdown)
        self.addCleanup(self.kube.shutdown)
        sa = Path(self.tmp, 'sa')
        sa.mkdir()
        (sa / 'token').write_text('sa-token')
        Path(self.tmp, 'account.js').write_text(STUB)
        self.config = {
            'centralUrl': f'http://127.0.0.1:{self.central.server_port}', 'publicUrl': 'https://odk.test',
            'bootstrapAccount': 'oan-bootstrap@odk.test', 'namespace': 'commons', 'attempts': 3, 'retrySeconds': 0,
            'registries': [{'name': 'farmer', 'project': 'Farmer Registry', 'forms': ['farmer_profile'],
                            'appUser': 'OAN test submitter', 'secretName': 'odk-test-submitter-farmer'}],
        }

    def run_job(self):
        config = Path(self.tmp, 'bootstrap.json')
        config.write_text(json.dumps(self.config))
        env = {**os.environ, 'ODK_ACCOUNT_MODULE': str(Path(self.tmp, 'account.js')),
               'ACCOUNT_LOG': str(Path(self.tmp, 'account.log')), 'KUBE_SA_DIR': str(Path(self.tmp, 'sa')),
               'KUBE_API': f'http://127.0.0.1:{self.kube.server_port}'}
        return subprocess.run([NODE, str(SCRIPT), str(config)], env=env, capture_output=True, text=True, timeout=60)

    def secret(self, name):
        return {k: base64.b64decode(v).decode() for k, v in self.world.secrets[name]['data'].items()}

    def test_first_run_makes_the_app_user_grants_the_form_and_keeps_the_token(self):
        done = self.run_job()
        self.assertEqual(done.returncode, 0, done.stderr)
        user = next(iter(self.world.app_users.values()))
        self.assertEqual(user['displayName'], 'OAN test submitter')
        self.assertIn((1, 'farmer_profile', user['id']), self.world.assignments)
        self.assertEqual(self.secret('odk-test-submitter-farmer'),
                         {'token': user['token'], 'project_id': '1', 'central_url': 'https://odk.test',
                          'app_user': 'OAN test submitter'})
        self.assertIn('farmer: project "Farmer Registry" present, app user created, 1 of 1 form(s) newly granted, '
                      'Secret odk-test-submitter-farmer created', done.stdout)
        # Signed out at the end; no token or password in the log.
        self.assertEqual(self.world.sessions, set())
        password = Path(self.tmp, 'account.log.password').read_text()
        self.assertNotIn(password, done.stdout + done.stderr)
        self.assertNotIn(user['token'], done.stdout + done.stderr)

    def test_second_run_changes_nothing_but_the_sign_in_password(self):
        self.run_job()
        first = Path(self.tmp, 'account.log.password').read_text()
        writes = [c for c in self.world.calls if c[0] in ('POST', 'SECRET') and c[1] != '/v1/sessions']
        done = self.run_job()
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual([c for c in self.world.calls if c[0] in ('POST', 'SECRET') and c[1] != '/v1/sessions'], writes)
        self.assertEqual(len(self.world.app_users), 1)
        self.assertIn('app user present, 0 of 1 form(s) newly granted, Secret odk-test-submitter-farmer unchanged',
                      done.stdout)
        self.assertNotEqual(Path(self.tmp, 'account.log.password').read_text(), first)

    def test_missing_project_is_created(self):
        self.config['registries'][0]['project'] = 'Crop Sown Registry'
        self.world.forms.add((101, 'farmer_profile'))
        done = self.run_job()
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn('Crop Sown Registry', [p['name'] for p in self.world.projects.values()])
        self.assertIn('project "Crop Sown Registry" created', done.stdout)

    def test_unpublished_form_stops_the_job(self):
        self.config['registries'][0]['forms'] = ['farmer_profile', 'not_published']
        done = self.run_job()
        self.assertEqual(done.returncode, 1)
        self.assertIn('ODK bootstrap failed: form not_published is not published in project Farmer Registry', done.stderr)
        self.assertNotIn('odk-test-submitter-farmer', self.world.secrets)
        self.assertEqual(self.world.sessions, set())

    def test_revoked_app_user_is_replaced_and_the_secret_updated(self):
        self.run_job()
        for user in self.world.app_users.values():
            user['token'] = None
        done = self.run_job()
        self.assertEqual(done.returncode, 0, done.stderr)
        live = [u for u in self.world.app_users.values() if u['token']]
        self.assertEqual(len(live), 1)
        self.assertEqual(self.secret('odk-test-submitter-farmer')['token'], live[0]['token'])
        self.assertIn('Secret odk-test-submitter-farmer updated', done.stdout)

    def test_unavailable_central_is_retried_then_gives_up(self):
        self.world.unavailable = 1
        self.assertEqual(self.run_job().returncode, 0)
        self.world.unavailable = 10
        done = self.run_job()
        self.assertEqual(done.returncode, 1)
        self.assertIn('gave up after 3 attempts', done.stderr)


class OdkBootstrapChartTests(unittest.TestCase):
    def test_job_keeps_its_log_and_rights_are_limited_to_the_token_secrets(self):
        job = (CHART / 'templates/job.yaml').read_text(encoding='utf-8')
        self.assertNotIn('hook-succeeded', job)
        self.assertIn('resourceNames: {{ toJson $secrets }}', job)
        self.assertNotIn('ClusterRole', job)
        self.assertIn('odk-db-user', (CHART / 'values.yaml').read_text(encoding='utf-8'))

    def test_environment_values_name_the_published_forms(self):
        values = (ROOT / 'environments/dev/values/odk-bootstrap.yaml').read_text(encoding='utf-8')
        for form in ('farmer_profile', 'livestock_registry', 'crop_sown_registry_plan', 'crop_sown_registry_prep',
                     'crop_sown_registry_sown', 'crop_sown_registry_harvest'):
            self.assertIn(form, values)
        self.assertIn('publicUrl: https://odk-central.development.oanstaging.com', values)


if __name__ == '__main__':
    unittest.main()
