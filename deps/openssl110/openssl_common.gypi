{
  'include_dirs': [
    'openssl/',
    'openssl/include/',
    'openssl/crypto/',
    'openssl/crypto/include/',
    'openssl/crypto/modes/',
  ],
  # build options specific to OS
  'conditions': [
    [ 'OS=="aix"', {
      # AIX is missing /usr/include/endian.h
      'defines': [
        '__LITTLE_ENDIAN=1234',
        '__BIG_ENDIAN=4321',
        '__BYTE_ORDER=__BIG_ENDIAN',
        '__FLOAT_WORD_ORDER=__BIG_ENDIAN',
        'OPENSSLDIR="/etc/ssl"',
        'ENGINESDIR="/dev/null"',
      ],
    }, 'OS=="win"', {
      'defines': [
        ## default of Win. See INSTALL in openssl repo.
        'OPENSSLDIR="C:\Program Files\Common Files\SSL"',
        'ENGINESDIR="NUL"',
      ],
      'link_settings': {
        'libraries': [
          '-lws2_32.lib',
          '-lgdi32.lib',
          '-ladvapi32.lib',
          '-lcrypt32.lib',
          '-luser32.lib',
        ],
      },
    }, 'OS=="mac"', {
      'xcode_settings': {
        'WARNING_CFLAGS': ['-Wno-missing-field-initializers']
      },
      'defines': [
        'OPENSSLDIR="/System/Library/OpenSSL/"',
        'ENGINESDIR="/dev/null"',
      ],
    }, 'OS=="solaris"', {
      'defines': [
        'OPENSSLDIR="/etc/ssl"',
        'ENGINESDIR="/dev/null"',
        '__EXTENSIONS__'
      ],
    }, {
      # linux and others
      'cflags': ['-Wno-missing-field-initializers',
                 ## TODO: check gcc_version>=4.3
                 '-Wno-old-style-declaration'],
      'defines': [
        'OPENSSLDIR="/etc/ssl"',
        'ENGINESDIR="/dev/null"',
        'TERMIOS',
      ],
    }],
  ]
}
