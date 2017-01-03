/*
  In OpenSSL, opensslconf.h was generated by Configure script with
  specifying a target argument, where it includes several defines that
  depend on OS and architecture platform.

  In node, we statically mapped --dest-os and --dest-cpu options in
  configure to the target of Configure in OpenSSL and make
  `deps/openssl/conf/openssconf.h` so as to include each file
  according to its target by checking pre-defined compiler macros.

  Included opnesslconf.h files for supported target architectures can
  be generated by `Makefile` and stored under
  `archs/{target}/opensslconf.h`. The Makefile also fixes several
  defines to meet node build requirements.

  Here is a map table of configure options in node, target arch of
  Configure in OpenSSL and CI support.

  | --dest-os | --dest-cpu | OpenSSL target arch  | CI  |
  | --------- | ---------- | -------------------- | --- |
  | aix       | ppc        | aix-gcc              | o   |
  | aix       | ppc64      | aix64-gcc            | o   |
  | linux     | ia32       | linux-elf            | o   |
  | linux     | x32        | linux-x32            | -   |
  | linux     | x64        | linux-x86_64         | o   |
  | linux     | arm        | linux-armv4          | o   |
  | linux     | arm64      | linux-aarch64        | o   |
  | linux     | ppc        | linux-ppc            | o   |
  | linux     | ppc64      | linux-ppc64          | o   |
  | linux     | s390       | linux32-s390x        | o   |
  | linux     | s390x      | linux64-s390x        | o   |
  | mac       | ia32       | darwin-i386-cc       | o   |
  | mac       | x64        | darwin64-x86-cc      | o   |
  | win       | ia32       | VC-WIN32             | -   |
  | win       | x64        | VC-WIN64A            | o   |
  | solaris   | ia32       | solaris-x86-gcc      | o   |
  | solaris   | x64        | solaris64-x86_64-gcc | o   |
  | freebsd   | ia32       | BSD-x86              | o   |
  | freebsd   | x64        | BSD-x86_64           | o   |
  | openbsd   | ia32       | BSD-x86              | -   |
  | openbsd   | x64        | BSD-x86_64           | -   |
  | others    | others     | linux-elf            | -   |

  --dest-os and --dest-cpu are mapped to pre-defined macros.

  | --dest-os          | pre-defined macro         |
  | ------------------ | ------------------------- |
  | aix                | _AIX                      |
  | win                | _WIN32                    |
  | win(64bit)         | _WIN64                    |
  | mac                | __APPLE__ && __MACH__     |
  | solaris            | __sun                     |
  | freebsd            | __FreeBSD__               |
  | openbsd            | __OpenBSD__               |
  | linux (not andorid)| __linux__ && !__ANDROID__ |
  | android            | __ANDROID__               |

  | --dest-cpu | pre-defined macro |
  | ---------- | ----------------- |
  | arm        | __arm__           |
  | arm64      | __aarch64__       |
  | ia32       | __i386__          |
  | ia32(win)  | _M_IX86           |
  | mips       | __mips__          |
  | mipsel     | __MIPSEL__        |
  | x32        | __ILP32__         |
  | x64        | __x86_64__        |
  | x64(win)   | _M_X64            |
  | ppc        | __PPC__           |
  |            | _ARCH_PPC         |
  | ppc64      | __PPC64__         |
  |            | _ARCH_PPC64       |
  | s390       | __s390__          |
  | s390x      | __s390x__         |

  These are the list which is not implemented yet.

  | --dest-os | --dest-cpu | OpenSSL target arch  | CI  |
  | --------- | ---------- | -------------------- | --- |
  | linux     | mips       | linux-mips32,linux-mips64,linux64-mips64? | --- |
  | linux     | mipsel     | ?                    | --- |
  | android   | ia32       | android-x86          | --- |
  | android   | arm        | android-armv7        | --- |
  | android   | mips       | android-mips         | --- |
  | android   | mipsel     | ?                    | --- |

  Supported target arch list in OpenSSL can be obtained by typing
  `deps/openssl/openssl/Configure LIST`.

*/

#undef OPENSSL_LINUX
#if defined(__linux) && !defined(__ANDROID__)
# define OPENSSL_LINUX 1
#endif

#if defined(OPENSSL_LINUX) && defined(__i386__)
# include "./archs/linux-elf/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && defined(__ILP32__)
# include "./archs/linux-x32/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && defined(__x86_64__)
# include "./archs/linux-x86_64/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && defined(__arm__)
# include "./archs/linux-armv4/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && defined(__aarch64__)
# include "./archs/linux-aarch64/asm/include/openssl/opensslconf.h"
#elif defined(__APPLE__) && defined(__MACH__) && defined(__i386__)
# include "./archs/darwin-i386-cc/asm/include/openssl/opensslconf.h"
#elif defined(__APPLE__) && defined(__MACH__) && defined(__x86_64__)
# include "./archs/darwin64-x86_64-cc/asm/include/openssl/opensslconf.h"
#elif defined(_WIN32) && defined(_M_IX86)
# include "./archs/VC-WIN32/asm/include/openssl/opensslconf.h"
#elif defined(_WIN32) && defined(_M_X64)
# include "./archs/VC-WIN64A/asm/include/openssl/opensslconf.h"
#elif (defined(__FreeBSD__) || defined(__OpenBSD__)) && defined(__i386__)
# include "./archs/BSD-x86/asm/include/openssl/opensslconf.h"
#elif (defined(__FreeBSD__) || defined(__OpenBSD__)) && defined(__x86_64__)
# include "./archs/BSD-x86_64/asm/include/openssl/opensslconf.h"
#elif defined(__sun) && defined(__i386__)
# include "./archs/solaris-x86-gcc/asm/include/openssl/opensslconf.h"
#elif defined(__sun) && defined(__x86_64__)
# include "./archs/solaris64-x86_64-gcc/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && defined(__PPC64__)
# include "./archs/linux-ppc64/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && !defined(__PPC64__) && defined(__ppc__)
# include "./archs/linux-ppc/asm/include/openssl/opensslconf.h"
#elif defined(_AIX) && defined(_ARCH_PPC64)
# include "./archs/aix64-gcc/asm/include/openssl/opensslconf.h"
#elif defined(_AIX) && !defined(_ARCH_PPC64) && defined(_ARCH_PPC)
# include "./archs/aix-gcc/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && defined(__s390x__)
# include "./archs/linux64-s390x/asm/include/openssl/opensslconf.h"
#elif defined(OPENSSL_LINUX) && defined(__s390__)
# include "./archs/linux32-s390x/asm/include/openssl/opensslconf.h"
#else
# include "./archs/linux-elf/asm/include/openssl/opensslconf.h"
#endif

/* GOST is not included in all platform */
#ifndef OPENSSL_NO_GOST
# define OPENSSL_NO_GOST
#endif
/* HW_PADLOCK is not included in all platform */
#ifndef OPENSSL_NO_HW_PADLOCK
# define OPENSSL_NO_HW_PADLOCK
#endif
