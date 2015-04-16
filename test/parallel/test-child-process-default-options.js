var common = require('../common');
var assert = require('assert');

var spawn = require('child_process').spawn;

var isWindows = process.platform === 'win32';
var isAndroid = process.platform === 'android';

process.env.HELLO = 'WORLD';

if (isWindows) {
  var child = spawn('cmd.exe', ['/c', 'set'], {});
} else if (isAndroid) {
  var child = spawn('/system/bin/printenv', [], {});
} else {
  var child = spawn('/usr/bin/env', [], {});
}

var response = '';

child.stdout.setEncoding('utf8');

child.stdout.on('data', function(chunk) {
  console.log('stdout: ' + chunk);
  response += chunk;
});

process.on('exit', function() {
  assert.ok(response.indexOf('HELLO=WORLD') >= 0,
            'spawn did not use process.env as default');
});
