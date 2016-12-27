'use strict';
const common = require('../common');

if (!common.hasCrypto) {
  common.skip('missing crypto');
  return;
}

const assert = require('assert');
const https = require('https');
const net = require('net');

const server = net.createServer(function(s) {
  s.once('data', function() {
    s.end('I was waiting for you, hello!', function() {
      s.destroy();
    });
  });
});

const expected_err = common.isOpenSSL10 ? /unknown protocol/ :
  /wrong version number/;

server.listen(0, function() {
  const req = https.request({ port: this.address().port });
  req.end();

  req.once('error', common.mustCall(function(err) {
    assert(expected_err.test(err.message));
    server.close();
  }));
});
