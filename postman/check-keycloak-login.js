pm.test('Keycloak authorization renders successfully', () => pm.response.to.have.status(200));
pm.test('Login response is HTML', () => pm.expect(pm.response.headers.get('Content-Type')).to.include('text/html'));
const html = pm.response.text();
pm.test('Login form is present', () => pm.expect(html).to.include('id="kc-form-login"'));
pm.test('Login action uses the canonical Keycloak host', () => pm.expect(html).to.match(/action="https:\/\/keycloak\.development\.oanstaging\.com\/realms\/staff\/login-actions\/authenticate\?/));
const headerBytes = pm.response.headers.all().reduce((total, h) => total + h.key.length + h.value.length + 4, 0);
pm.test('Regression exercises response headers larger than 4 KiB', () => pm.expect(headerBytes).to.be.above(4096));
