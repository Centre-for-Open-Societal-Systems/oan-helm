pm.test('Discovery endpoint succeeds', () => pm.response.to.have.status(200));
const discovery = pm.response.json();
const issuer = 'https://keycloak.development.oanstaging.com/realms/staff';
pm.test('Canonical development issuer', () => pm.expect(discovery.issuer).to.equal(issuer));
for (const field of ['authorization_endpoint', 'token_endpoint', 'userinfo_endpoint', 'jwks_uri', 'end_session_endpoint']) {
  pm.test(field + ' uses canonical issuer', () => pm.expect(discovery[field]).to.match(new RegExp('^' + issuer.replace(/\./g, '\\.') + '/')));
}
