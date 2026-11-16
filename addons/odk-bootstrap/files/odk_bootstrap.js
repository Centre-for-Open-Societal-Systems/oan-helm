'use strict';
// Brings ODK Central to the state the registries rely on, from values, idempotently:
//   1. the Job signs in as a local account whose password it sets to a fresh random value on every run, through
//      Central's own account task (lib/task/account, the code behind Central's CLI), and signs out at the end; the
//      password is never stored or printed;
//   2. each registry's project exists (found by name, created when missing);
//   3. each registry has one project app user for test submissions, with the app-user role on the declared forms;
//   4. the app user's token is kept in a Secret in this namespace, written only when it changes.
// Central API: https://docs.getodk.org/central-api (sessions, projects, app users, form assignments).
// Prints project names, form ids, counts and HTTP codes only: never a password or a token.
const crypto = require('crypto');
const fs = require('fs');
const http = require('http');
const https = require('https');

class Retry extends Error {}
class Refused extends Error {}

const SA = process.env.KUBE_SA_DIR || '/var/run/secrets/kubernetes.io/serviceaccount';
const KUBE = process.env.KUBE_API || 'https://kubernetes.default.svc';

function send(base, method, path, { body, token, ca } = {}) {
  const url = new URL(path, base);
  const data = body === undefined ? undefined : JSON.stringify(body);
  const client = url.protocol === 'https:' ? https : http;
  return new Promise((resolve, reject) => {
    const req = client.request(url, {
      method, ca, timeout: 30000,
      headers: {
        Accept: 'application/json',
        ...(data === undefined ? {} : { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(data) }),
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
    }, (res) => {
      let raw = '';
      res.setEncoding('utf8');
      res.on('data', (chunk) => { raw += chunk; });
      res.on('end', () => {
        let parsed = null;
        try { parsed = raw ? JSON.parse(raw) : null; } catch (e) { parsed = null; }
        resolve({ status: res.statusCode, body: parsed });
      });
    });
    req.on('timeout', () => req.destroy(new Error('timeout')));
    req.on('error', () => reject(new Retry(`${method} ${url.pathname}: unavailable`)));
    if (data !== undefined) req.write(data);
    req.end();
  });
}

function must(res, what) {
  if (res.status >= 500 || res.status === 429) throw new Retry(`${what}: HTTP ${res.status}`);
  if (res.status >= 300) throw new Refused(`${what}: HTTP ${res.status}${res.body && res.body.code ? ` (${res.body.code})` : ''}`);
  return res.body;
}

// ---- Kubernetes: the token Secrets, in this namespace only
function kube() {
  const token = fs.readFileSync(`${SA}/token`, 'utf8');
  const ca = fs.existsSync(`${SA}/ca.crt`) ? fs.readFileSync(`${SA}/ca.crt`) : undefined;
  return (method, path, body) => send(KUBE, method, path, { body, token, ca });
}

async function keepSecret(k8s, namespace, name, values) {
  const path = `/api/v1/namespaces/${namespace}/secrets/${name}`;
  const data = Object.fromEntries(Object.entries(values).map(([key, v]) => [key, Buffer.from(String(v)).toString('base64')]));
  const found = await k8s('GET', path);
  if (found.status === 200) {
    const current = (found.body && found.body.data) || {};
    if (Object.keys(data).every((key) => current[key] === data[key])) return 'unchanged';
    must(await k8s('PUT', path, { ...found.body, data: { ...current, ...data } }), `update of Secret ${name}`);
    return 'updated';
  }
  if (found.status !== 404) must(found, `lookup of Secret ${name}`);
  must(await k8s('POST', `/api/v1/namespaces/${namespace}/secrets`, {
    apiVersion: 'v1', kind: 'Secret', type: 'Opaque',
    metadata: { name, namespace, labels: { 'app.kubernetes.io/managed-by': 'odk-bootstrap' } }, data,
  }), `creation of Secret ${name}`);
  return 'created';
}

// ---- Central's own account task, over Central's database
function accountTask() {
  const module = process.env.ODK_ACCOUNT_MODULE || '/usr/odk/lib/task/account';
  if (!process.env.ODK_ACCOUNT_MODULE) {
    // Central reads its settings with the config package; NODE_CONFIG overrides the files, so nothing is written.
    process.env.NODE_CONFIG = JSON.stringify({ default: {
      database: { host: process.env.DB_HOST, database: process.env.DB_NAME, user: process.env.DB_USER,
                  password: process.env.DB_PASSWORD },
    } });
  }
  return require(module);
}

async function signInAccount(account, email) {
  const password = crypto.randomBytes(32).toString('base64url');
  try { await account.createUser(email, null); } catch (e) { /* the account exists already */ }
  await account.setUserPassword(email, password);
  try {
    await account.promoteUser(email);
  } catch (e) {
    // Central inserts the grant without a conflict clause: an account promoted by an earlier run is already admin.
    if (!/unique|duplicate|409/i.test(`${e && e.message} ${e && e.problemCode}`)) throw e;
  }
  return password;
}

// ---- Central API
async function ensureProject(api, name) {
  const projects = must(await api('GET', '/v1/projects'), 'project list');
  const found = projects.find((p) => p.name === name && !p.archived);
  if (found) return { id: found.id, state: 'present' };
  return { id: must(await api('POST', '/v1/projects', { name }), `creation of project ${name}`).id, state: 'created' };
}

async function ensureAppUser(api, projectId, displayName) {
  const users = must(await api('GET', `/v1/projects/${projectId}/app-users`), 'app user list');
  const live = users.find((u) => u.displayName === displayName && u.token);
  if (live) return { id: live.id, token: live.token, state: 'present' };
  const made = must(await api('POST', `/v1/projects/${projectId}/app-users`, { displayName }), 'creation of the app user');
  return { id: made.id, token: made.token, state: 'created' };
}

async function grantForms(api, projectId, project, forms, actorId) {
  let granted = 0;
  for (const form of forms) {
    const id = encodeURIComponent(form);
    const exists = await api('GET', `/v1/projects/${projectId}/forms/${id}`);
    if (exists.status === 404) throw new Refused(`form ${form} is not published in project ${project}`);
    must(exists, `lookup of form ${form}`);
    const holders = must(await api('GET', `/v1/projects/${projectId}/forms/${id}/assignments/app-user`), `assignments of ${form}`);
    if (holders.some((a) => (a.actorId ?? a.id) === actorId)) continue;
    must(await api('POST', `/v1/projects/${projectId}/forms/${id}/assignments/app-user/${actorId}`), `access to form ${form}`);
    granted += 1;
  }
  return granted;
}

async function once(config, account, k8s, out) {
  const password = await signInAccount(account, config.bootstrapAccount);
  const call = (token) => (method, path, body) => send(config.centralUrl, method, path, { body, token });
  const session = must(await call()('POST', '/v1/sessions', { email: config.bootstrapAccount, password }), 'sign-in');
  const api = call(session.token);
  try {
    for (const registry of config.registries) {
      const project = await ensureProject(api, registry.project);
      const user = await ensureAppUser(api, project.id, registry.appUser);
      const granted = await grantForms(api, project.id, registry.project, registry.forms, user.id);
      const secret = await keepSecret(k8s, config.namespace, registry.secretName, {
        token: user.token, project_id: project.id, central_url: config.publicUrl, app_user: registry.appUser,
      });
      out(`${registry.name}: project "${registry.project}" ${project.state}, app user ${user.state}, `
        + `${granted} of ${registry.forms.length} form(s) newly granted, Secret ${registry.secretName} ${secret}`);
    }
  } finally {
    await api('DELETE', `/v1/sessions/${session.token}`).catch(() => {});
  }
}

async function run(config, { account, k8s, out = console.log, sleep } = {}) {
  const attempts = Number(config.attempts || 30);
  const pause = sleep || ((s) => new Promise((r) => setTimeout(r, s * 1000)));
  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    try {
      await once(config, account, k8s, out);
      return;
    } catch (e) {
      if (!(e instanceof Retry)) throw e;
      if (attempt === attempts) throw new Refused(`gave up after ${attempts} attempts: ${e.message}`);
      out(`attempt ${attempt}: ${e.message}; retrying`);
      await pause(Number(config.retrySeconds ?? 10));
    }
  }
}

module.exports = { run, Refused, Retry };

if (require.main === module) {
  let config;
  try {
    config = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  } catch (e) {
    console.error('ODK bootstrap failed: configuration missing or not JSON');
    process.exit(1);
  }
  run(config, { account: accountTask(), k8s: kube() })
    .then(() => process.exit(0))
    .catch((e) => {
      console.error(`ODK bootstrap failed: ${e instanceof Refused || e instanceof Retry ? e.message : `unexpected error: ${String(e && e.message).slice(0, 300)}`}`);
      process.exit(1);
    });
}
