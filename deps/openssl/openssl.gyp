# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'is_clang': 0,
    'gcc_version': 0,
    'openssl_no_asm%': 0
  },
  'includes': ['openssl.gypi'],
  'targets': [
    {
      'target_name': 'openssl',
      'type': '<(library)',
      'sources': ['<@(openssl_sources)'],
      'sources/': [
        ['exclude', 'md2/.*$'],
        ['exclude', 'store/.*$']
      ],
      'conditions': [
        ['openssl_no_asm!=0', {
          # Disable asm
          'defines': [
            'OPENSSL_NO_ASM',
          ],
          'sources': ['<@(openssl_sources_no_asm)'],
        }, {
          # "else if" was supported in https://codereview.chromium.org/601353002
          'conditions': [
            ['target_arch=="arm"', {
              'defines': ['<@(openssl_defines_asm)'],
              'sources': ['<@(openssl_sources_arm_elf_gas)'],
            }, 'target_arch=="ia32" and OS=="mac"', {
              'defines': [
                '<@(openssl_defines_asm)',
                '<@(openssl_defines_x86_mac)',
              ],
              'sources': ['<@(openssl_sources_x86_macosx_gas)'],
            }, 'target_arch=="ia32" and OS=="win"', {
              'defines': [
                '<@(openssl_defines_asm)',
                '<@(openssl_defines_x86_win)',
              ],
              'sources': ['<@(openssl_sources_x86_win32_masm)'],
            }, 'target_arch=="ia32"', {
              # Linux or others
              'defines': [
                '<@(openssl_defines_asm)',
                '<@(openssl_defines_x86_elf)',
              ],
              'sources': ['<@(openssl_sources_x86_elf_gas)'],
            }, 'target_arch=="x64" and OS=="mac"', {
              'defines': [
                '<@(openssl_defines_asm)',
                '<@(openssl_defines_x64_mac)',
              ],
              'sources': ['<@(openssl_sources_x64_macosx_gas)'],
            }, 'target_arch=="x64" and OS=="win"', {
              'defines': [
                '<@(openssl_defines_asm)',
                '<@(openssl_defines_x64_win)',
              ],
              'sources': ['<@(openssl_sources_x64_win32_masm)'],
            }, 'target_arch=="x64"', {
              # Linux or others
              'defines': [
                '<@(openssl_defines_asm)',
                '<@(openssl_defines_x64_elf)',
              ],
              'sources': ['<@(openssl_sources_x64_elf_gas)'],
            }, { # else other archtectures does not use asm
              'defines': [
                'OPENSSL_NO_ASM',
              ],
              'sources': ['<@(openssl_sources_no_asm)'],
            }],
          ],
        }], # end of conditions of openssl_no_asm
        ['OS=="win"', {
          'defines' : ['<@(openssl_defines_all_win)'],
          'conditions': [
            ['target_arch=="ia32"', {
              'rules': [
                {
                  'rule_name': 'Assemble',
                  'extension': 'asm',
                  'inputs': [],
                  'outputs': [
                    '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
                  ],
                  'action': [
                    'ml.exe',
                    '/Zi',
                    '/safeseh',
                    '/Fo', '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
                    '/c', '<(RULE_INPUT_PATH)',
                  ],
                  'process_outputs_as_sources': 0,
                  'message': 'Assembling <(RULE_INPUT_PATH) to <(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj.',
                }
              ],
            }, 'target_arch=="x64"', {
              'rules': [
                {
                  'rule_name': 'Assemble',
                  'extension': 'asm',
                  'inputs': [],
                  'outputs': [
                    '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
                  ],
                  'action': [
                    'ml64.exe',
                    '/Zi',
                    '/Fo', '<(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj',
                    '/c', '<(RULE_INPUT_PATH)',
                  ],
                  'process_outputs_as_sources': 0,
                  'message': 'Assembling <(RULE_INPUT_PATH) to <(INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).obj.',
                }
              ],
            }],
          ],
        }, {
          'defines' : ['<@(openssl_defines_all_non_win)']
        }]
      ],
      'include_dirs': ['<@(openssl_include_dirs)'],
      'direct_dependent_settings': {
        'include_dirs': [
          'openssl/include'
        ],
      },
    },
    {
      'target_name': 'openssl-cli',
      'type': 'executable',
      'dependencies': ['openssl'],
      'defines': [
        'MONOLITH'
      ],
      'sources': ['<@(openssl_cli_sources)'],
      'conditions': [
        ['OS=="solaris"', {
          'libraries': ['<@(openssl_cli_libraries_solaris)']
        }, 'OS=="win"', {
          'link_settings': {
            'libraries': ['<@(openssl_cli_libraries_win)'],
          },
        }, 'OS in "linux android"', {
          'link_settings': {
            'libraries': [
              '-ldl',
            ],
          },
        }],
      ]
    }
  ],
  'target_defaults': {
    'include_dirs': ['<@(openssl_default_include_dirs)'],
    'defines': ['<@(openssl_default_defines_all)'],
    'conditions': [
      ['OS=="win"', {
        'defines': ['<@(openssl_default_defines_win)'],
        'link_settings': {
          'libraries': ['<@(openssl_default_libraries_win)'],
        },
      }, {
        'defines': ['<@(openssl_default_defines_not_win)'],
        'cflags': [
          '-Wno-missing-field-initializers',
        ],
        'conditions': [
          ['OS=="mac"', {
            'defines': ['<@(openssl_default_defines_mac)'],
          }, {
            'defines': ['<@(openssl_default_defines_linux_others)'],
          }],
        ]
      }],
      ['is_clang==1 or gcc_version>=43', {
        'cflags': ['-Wno-old-style-declaration'],
      }],
      ['OS=="solaris"', {
        'defines': ['__EXTENSIONS__'],
      }],
    ],
  },
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
