// Reuse the application's versioned Python fixtures as the stand-ins.
// No deployed Partner Management, registry or partner callback is contacted.
const http = require('http');
http.createServer((req, res) => {
  const allowed = /^\/(keys\/[^/]+|dci\/registry\/sync\/search|callback|received|searches)(\?.*)?$/;
  if (!allowed.test(req.url)) {
    res.writeHead(501, { 'content-type': 'application/json' });
    return res.end(JSON.stringify({ error: 'Endpoint not modeled by source fixtures' }));
  }
  const send = (body) => {
    const headers = { ...req.headers };
    delete headers.host;
    delete headers['content-length'];
    if (body.length) headers['content-length'] = Buffer.byteLength(body);
    const forward = http.request({ hostname: '127.0.0.1', port: 18909,
      path: req.url, method: req.method, headers }, (upstream) => {
      res.writeHead(upstream.statusCode, upstream.headers);
      upstream.pipe(res);
    });
    forward.on('error', () => {
      res.writeHead(502, { 'content-type': 'application/json' });
      res.end(JSON.stringify({ error: 'Local source fixture unavailable' }));
    });
    forward.end(body);
  };
  if (req.body !== undefined) return send(typeof req.body === 'string' ? req.body : JSON.stringify(req.body));
  const chunks = [];
  req.on('data', (chunk) => chunks.push(chunk));
  req.on('end', () => send(Buffer.concat(chunks)));
}).listen(process.env.PORT);
