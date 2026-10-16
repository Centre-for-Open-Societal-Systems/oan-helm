"""Local image-pair check using source-owned fixtures and Postman simulation.

Requires Docker Desktop (Linux containers), Postman CLI 1.73+, and a clean
oan-aggregation-api checkout at the recorded revision. Never accesses Kubernetes.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import time
import uuid
from urllib.request import urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
AGG_COMMIT = '8fe3bf97030bb0b3f6283c2123ad58026af6cc50'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--aggregation-source', type=Path, required=True)
    args = parser.parse_args()
    source_repo = args.aggregation_source.resolve()
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=source_repo, text=True).strip() == AGG_COMMIT
    assert subprocess.check_output(['git', 'status', '--porcelain'], cwd=source_repo) == b''
    run_id = 'oan-pair-' + uuid.uuid4().hex[:10]
    work = ROOT / '.build' / run_id
    work.mkdir(parents=True)
    source = work / 'source'
    source.mkdir()
    with (work / 'source.tar').open('wb') as out:
        subprocess.run(['git', 'archive', '--format=tar', AGG_COMMIT], cwd=source_repo, stdout=out, check=True)
    with tarfile.open(work / 'source.tar') as tar:
        tar.extractall(source, filter='data')
    cm_record = json.loads((ROOT / 'releases/consent-candidate.json').read_text(encoding='utf-8'))
    agg_record = json.loads((ROOT / 'releases/aggregation-candidate.json').read_text(encoding='utf-8'))
    cm = next(i['publishedReference'] for i in cm_record['images'] if i['component'] == 'consent-manager-api')
    agg = agg_record['publishedReference']
    # Only test tooling is layered above Aggregation; the two application
    # containers below run the exact published image references.
    runner = 'oan-aggregation-e2e-tooling:8fe3bf97030b'
    (work / 'Dockerfile.tooling').write_text(
        'FROM ' + agg + '\nUSER root\nRUN pip install --no-cache-dir pytest==9.0.2 jsonschema==4.26.0\n',
        encoding='utf-8')
    subprocess.run(['docker', 'build', '-f', str(work / 'Dockerfile.tooling'), '-t', runner, str(work)], check=True)
    postgres = json.loads(subprocess.check_output(['docker', 'image', 'inspect', 'postgres:16'], text=True))[0]
    pg_image = next(d for d in postgres['RepoDigests'] if d.startswith('postgres@'))
    names = []
    simulation = None
    simout = simerr = None
    report = {'checkedAtUtc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'consentImage': cm, 'aggregationImage': agg, 'postgresImage': pg_image,
              'sourceFixturesCommit': AGG_COMMIT, 'environment': 'disposable local Docker network/databases',
              'authenticationEnabled': False, 'aweEnabled': False, 'kafkaEnabled': False,
              'fixtureSource': 'COSS oan-aggregation-api test/e2e/fakes.py; owner-provided local fixture reused',
              'postmanSimulation': 'postman/simulations/consent-aggregation.sim.yaml',
              'clusterChanges': False, 'productionServicesContacted': False,
              'status': 'running', 'logDirectory': str(work.relative_to(ROOT))}

    def command(args, log=None, timeout=90):
        result = subprocess.run(args, capture_output=True, timeout=timeout)
        if log:
            (work / log).write_bytes(result.stdout + b'\n' + result.stderr)
        if result.returncode:
            raise RuntimeError('Local check command failed; inspect ' + str(work / (log or 'container logs')))
        return result.stdout

    def container(name, image, *, env=None, mounts=(), ports=(), detach=False):
        full = run_id + '-' + name
        docker = ['docker', 'run', '--name', full, '--network', run_id]
        if detach:
            docker += ['-d']
        else:
            docker += ['--rm']
        for key, value in (env or {}).items():
            docker += ['-e', key + '=' + str(value)]
        for mount in mounts:
            docker += ['--mount', mount]
        for port in ports:
            docker += ['-p', port]
        return full, docker, image

    def start(name, image, *, env=None, mounts=(), ports=(), entrypoint=None, command_args=()):
        full, docker, image = container(name, image, env=env, mounts=mounts, ports=ports, detach=True)
        docker += ['--network-alias', name]
        if entrypoint:
            docker += ['--entrypoint', entrypoint]
        names.append(full)
        command(docker + [image, *command_args], name + '-start.log')
        return full

    def task(name, image, command_args, *, env=None, mounts=(), entrypoint='python'):
        full, docker, image = container(name, image, env=env, mounts=mounts)
        return command(docker + ['--entrypoint', entrypoint, image, *command_args], name + '.log', timeout=180)

    def wait_url(url, attempts=60):
        for _ in range(attempts):
            try:
                with urlopen(url, timeout=2) as response:
                    if response.status == 200:
                        return
            except Exception:
                pass
            time.sleep(0.5)
        raise RuntimeError('Local service did not become ready: ' + url)

    try:
        command(['docker', 'network', 'create', '--label', 'org.coss.local-check=' + run_id, run_id])
        db = start('db', pg_image, env={'POSTGRES_PASSWORD': 'local-test-only'})
        for _ in range(60):
            ready = subprocess.run(['docker', 'exec', db, 'pg_isready', '-U', 'postgres'], capture_output=True)
            if ready.returncode == 0:
                break
            time.sleep(0.5)
        else:
            raise RuntimeError('Local PostgreSQL unavailable')
        for database in ['consent_manager_db', 'aggregation_layer_db']:
            command(['docker', 'exec', db, 'createdb', '-U', 'postgres', database])
        keys = work / 'keys'
        keys.mkdir()
        key_mount = 'type=bind,source=' + str(keys) + ',target=/keys'
        task('generate-keys', agg, ['-c', "from pathlib import Path; from cryptography.hazmat.primitives import serialization as s; from cryptography.hazmat.primitives.asymmetric import ed25519; p=Path('/keys');\nfor ref in ['PARTNER_X','PARTNER_Y','PARTNER_AGGREGATION_LAYER']:\n k=ed25519.Ed25519PrivateKey.generate();(p/(ref+'.pem')).write_bytes(k.private_bytes(s.Encoding.PEM,s.PrivateFormat.PKCS8,s.NoEncryption()));(p/(ref+'.pub.pem')).write_bytes(k.public_key().public_bytes(s.Encoding.PEM,s.PublicFormat.SubjectPublicKeyInfo))"], mounts=[key_mount])
        simulation_url = 'http://host.docker.internal:18910/fixtures'
        catalog = yaml.safe_load((source / 'test/e2e/registries.yaml').read_text(encoding='utf-8'))
        catalog['registries']['FARMER_REGISTRY']['partner_api']['base_url'] = simulation_url
        # Discovery and acknowledgements preserve the owner's catalog order.
        (work / 'registries.yaml').write_text(yaml.safe_dump(catalog, sort_keys=False), encoding='utf-8')
        source_mount = 'type=bind,source=' + str(source) + ',target=/review,readonly'
        key_ro = key_mount + ',readonly'
        cm_env = {'CONSENT_MANAGER_DB_HOSTNAME': 'db', 'CONSENT_MANAGER_DB_USERNAME': 'postgres',
                  'CONSENT_MANAGER_DB_PASSWORD': 'local-test-only', 'CONSENT_MANAGER_DB_DBNAME': 'consent_manager_db',
                  'CONSENT_MANAGER_AUTH_ENABLED': 'false', 'CONSENT_MANAGER_API_AUDIENCE': 'all',
                  'CONSENT_MANAGER_PARTNER_MGMT_API_URL': simulation_url,
                  'CONSENT_MANAGER_CRYPTO_BACKEND': 'partner-mgmt', 'CONSENT_MANAGER_SUBJECT_CONSENT_REQUIRED': 'true',
                  'CONSENT_MANAGER_OTP_DEBUG_ENABLED': 'true', 'CONSENT_MANAGER_PARTNER_CACHE_TTL_SEC': '1',
                  'CONSENT_MANAGER_REPLAY_FRESHNESS_WINDOW_SEC': '8',
                  'CONSENT_MANAGER_CM_SIGNING_PRIVATE_KEY_PEM': (keys / 'PARTNER_X.pem').read_text()}
        task('cm-migrate', cm, ['-m', 'openg2p_consent_manager.main', 'migrate'], env=cm_env)
        start('cm', cm, env=cm_env, ports=['127.0.0.1:18900:8000'], entrypoint='python',
              command_args=['-m', 'uvicorn', 'openg2p_consent_manager.main:app', '--host', '0.0.0.0', '--port', '8000'])
        start('fixtures', runner, env={'E2E_KEYS': '/keys', 'E2E_CM': 'http://cm:8000', 'PYTHONPATH': '/review/test/e2e'},
              mounts=[source_mount, key_ro], ports=['127.0.0.1:18909:18090'], entrypoint='python',
              command_args=['-m', 'uvicorn', 'fakes:app', '--host', '0.0.0.0', '--port', '18090'])
        wait_url('http://127.0.0.1:18909/received')
        simout = (work / 'simulation.ndjson').open('wb')
        simerr = (work / 'simulation.err').open('wb')
        simulation = subprocess.Popen(['postman', 'simulation', 'run', str(ROOT / report['postmanSimulation']),
            '--port', '18910', '--no-history', '--output', 'ndjson'], stdout=simout, stderr=simerr)
        wait_url('http://127.0.0.1:18910/fixtures/received')
        # Confirms Docker can reach Postman's host-side loopback listener.
        task('simulation-reachability', runner, ['-c', "import urllib.request; print(urllib.request.urlopen('" + simulation_url + "/received',timeout=10).status)"])
        agg_env = {'AGGREGATION_LAYER_DB_HOSTNAME': 'db', 'AGGREGATION_LAYER_DB_USERNAME': 'postgres',
                   'AGGREGATION_LAYER_DB_PASSWORD': 'local-test-only', 'AGGREGATION_LAYER_DB_DBNAME': 'aggregation_layer_db',
                   'AGGREGATION_LAYER_AUTH_ENABLED': 'false', 'AGGREGATION_LAYER_REGISTRY_CATALOG_PATH': '/config/registries.yaml',
                   'AGGREGATION_LAYER_CM_BASE_URL': 'http://cm:8000', 'AGGREGATION_LAYER_CM_POLL_INTERVAL_SEC': '1',
                   'AGGREGATION_LAYER_OTP_DEBUG_ENABLED': 'true',
                   'AGGREGATION_LAYER_SIGNING_PRIVATE_KEY_PEM': (keys / 'PARTNER_AGGREGATION_LAYER.pem').read_text()}
        catalog_mount = 'type=bind,source=' + str(work / 'registries.yaml') + ',target=/config/registries.yaml,readonly'
        task('agg-migrate', agg, ['-m', 'openg2p_aggregation_layer.main', 'migrate'], env=agg_env, mounts=[catalog_mount])
        start('agg', agg, env=agg_env, mounts=[catalog_mount], ports=['127.0.0.1:18901:8100'], entrypoint='python',
              command_args=['-m', 'uvicorn', 'openg2p_aggregation_layer.main:app', '--host', '0.0.0.0', '--port', '8100'])
        wait_url('http://127.0.0.1:18900/ping')
        wait_url('http://127.0.0.1:18901/ping')
        # Reuse the owner's scenarios unchanged; only URLs/test keys differ.
        output = task('end-to-end', runner, ['/review/test/e2e/e2e.py'], env={
            'E2E_CM': 'http://cm:8000', 'E2E_AGG': 'http://agg:8100', 'E2E_FAKES': simulation_url,
            'E2E_KEYS': '/keys', 'E2E_REPLAY_WINDOW': '8'}, mounts=[source_mount, key_ro])
        text = output.decode()
        match = re.search(r'(\d+)/(\d+) passed', text)
        assert match and match[1] == match[2], 'End-to-end scenarios did not all pass'
        events = [json.loads(l) for l in (work / 'simulation.ndjson').read_text().splitlines() if l.startswith('{')]
        requests = [e for e in events if e.get('event') == 'request']
        assert requests, 'No HTTP dependency calls recorded by simulation'
        report.update({'status': 'passed', 'checksPassed': int(match[1]), 'checksTotal': int(match[2]),
                       'simulationDependencyRequests': len(requests), 'suiteSha256': hashlib.sha256((source / 'test/e2e/e2e.py').read_bytes()).hexdigest(),
                       'limits': 'Local auth-disabled/all-audience/in-process profile; source-owned PM/registry/callback fixtures. No Keycloak, Istio split routing, AWE, Kafka, live data or production database migration test.'})
    except Exception as error:
        report.update({'status': 'failed', 'error': str(error)})
        output_log = work / 'end-to-end.log'
        if output_log.exists():
            match = re.search(r'(\d+)/(\d+) passed', output_log.read_text(encoding='utf-8'))
            if match:
                report.update({'checksPassed': int(match[1]), 'checksTotal': int(match[2])})
        raise
    finally:
        for name in names:
            result = subprocess.run(['docker', 'logs', name], capture_output=True)
            (work / (name + '.log')).write_bytes(result.stdout + b'\n' + result.stderr)
            subprocess.run(['docker', 'rm', '-f', name], capture_output=True)
        subprocess.run(['docker', 'network', 'rm', run_id], capture_output=True)
        if simulation and simulation.poll() is None:
            if os.name == 'nt':
                subprocess.run(['taskkill', '/PID', str(simulation.pid), '/T', '/F'], capture_output=True)
            else:
                simulation.terminate()
        if simout:
            simout.close()
            simerr.close()
        (work / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
