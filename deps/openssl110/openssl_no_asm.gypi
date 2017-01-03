{
  'defines': ['OPENSSL_NO_ASM'],
  'conditions': [
    ['target_arch=="ppc" and OS=="aix"', {
      'includes': ['config/archs/aix-gcc/no-asm/openssl.gypi'],
    }, 'target_arch=="ppc" and OS=="linux"', {
      'includes': ['config/archs/linux-ppc/no-asm/openssl.gypi'],
    }, 'target_arch=="ppc64" and OS=="aix"', {
      'includes': ['config/archs/aix64-gcc/no-asm/openssl.gypi'],
    }, 'target_arch=="ppc64" and OS=="linux"', {
      'includes': ['config/archs/linux-ppc64/no-asm/openssl.gypi'],
    }, 'target_arch=="s390" and OS=="linux"', {
      'includes': ['config/archs/linux32-s390x/no-asm/openssl.gypi'],
    }, 'target_arch=="s390x" and OS=="linux"', {
      'includes': ['config/archs/linux64-s390x/no-asm/openssl.gypi'],
    }, 'target_arch=="arm" and OS=="linux"', {
      'includes': ['config/archs/linux-armv4/no-asm/openssl.gypi'],
    }, 'target_arch=="arm64" and OS=="linux"', {
      'includes': ['config/archs/linux-aarch64/no-asm/openssl.gypi'],
    }, 'target_arch=="ia32" and OS=="linux"', {
      'includes': ['config/archs/linux-elf/no-asm/openssl.gypi'],
    }, 'target_arch=="ia32" and OS=="mac"', {
      'includes': ['config/archs/darwin-i386-cc/no-asm/openssl.gypi'],
    }, 'target_arch=="ia32" and OS=="solaris"', {
      'includes': ['config/archs/solaris-x86-gcc/no-asm/openssl.gypi'],
    }, 'target_arch=="ia32" and OS=="win"', {
      # 'includes': ['config/archs/VC-WIN32/no-asm/openssl.gypi'],
    }, 'target_arch=="ia32"', {
      # noasm linux-elf for other ia32 platforms
      'includes': ['config/archs/linux-elf/no-asm/openssl.gypi'],
    }, 'target_arch=="x64" and OS=="freebsd"', {
      'includes': ['config/archs/BSD-x86_64/no-asm/openssl.gypi'],
    }, 'target_arch=="x64" and OS=="mac"', {
      'includes': ['config/archs/darwin64-x86_64-cc/no-asm/openssl.gypi'],
    }, 'target_arch=="x64" and OS=="solaris"', {
      'includes': ['config/archs/solaris64-x86_64-gcc/no-asm/openssl.gypi'],
    }, 'target_arch=="x64" and OS=="win"', {
      # 'includes': ['config/archs/VC-WIN64A/no-asm/openssl.gypi'],
    }, 'target_arch=="x64" and OS=="linux"', {
      'includes': ['config/archs/linux-x86_64/no-asm/openssl.gypi'],
    }, {
      # Other architectures don't use assembly
      'includes': ['config/archs/linux-x86_64/no-asm/openssl.gypi'],
    }],
  ],
}
