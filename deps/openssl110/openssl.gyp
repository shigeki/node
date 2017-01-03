{
  'targets': [
    {
      'target_name': 'openssl',
      'type': '<(library)',
      'include_dirs': [
        'openssl/',
        'openssl/include/',
        'openssl/crypto/',
        'openssl/crypto/include/',
        'openssl/crypto/modes/',
      ],
      'defines': [
        'ENGINESDIR="/dev/null"',
        'OPENSSLDIR="/etc/ssl"',
      ],
      'conditions': [
        [ 'OS=="aix"', {
          # AIX is missing /usr/include/endian.h
          'defines': [
            '__LITTLE_ENDIAN=1234',
            '__BIG_ENDIAN=4321',
            '__BYTE_ORDER=__BIG_ENDIAN',
            '__FLOAT_WORD_ORDER=__BIG_ENDIAN'],
        }],
      ],
      'conditions': [
        ['openssl_no_asm==0 or target_arch!="s390x" or OS!="win"', {
          'includes': ['./openssl_asm.gypi'],
        }, {
          'includes': ['./openssl_no_asm.gypi'],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'openssl/include'
        ],
      }
    },
    {
      # openssl-cli target
      'target_name': 'openssl-cli',
      'type': 'executable',
      'dependencies': ['openssl'],
      'include_dirs': [
        'openssl/',
        'openssl/include/'
      ],
      'conditions': [
        ['openssl_no_asm==0 or target_arch!="s390x" or OS!="win"', {
          'includes': ['./openssl-cl_asm.gypi'],
        }, {
          'includes': ['./openssl-cl_no_asm.gypi'],
        }],
      ],
    },
  ],
}
