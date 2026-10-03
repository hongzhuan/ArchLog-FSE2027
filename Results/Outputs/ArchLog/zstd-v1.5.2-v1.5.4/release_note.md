# Release Note

## Important Changes

### Core Compression Engine
- Added lib/common/bits.h file, centralized scattered bit operation inline functions here, and updated all call points to use unified implementation. (Architecture event: bits.h was added and bit operation centralized)
  ↳ [#3045](https://github.com/facebook/zstd/pull/3045): [db2f4a6](https://github.com/facebook/zstd/commit/db2f4a6532532b9d532d7db34212fea3b1fc02f9)
- Refactored the fuzz testing of the sequence compression API and added support for explicit delimiter mode. (Architecture-related: sequence compression API changes)
  ↳ [#3023](https://github.com/facebook/zstd/pull/3023): [fc2ea97](https://github.com/facebook/zstd/commit/fc2ea97442460158a92d1e7b7c26e7486e45a605)
- Added experimental parameter ZSTD_c_prefetchCDictTables, which is used to prefetch dictionary tables in cold CDict scenarios to improve compression speed. (Architecture-related: public API: new experimental parameter)
  ↳ [#3177](https://github.com/facebook/zstd/pull/3177): [2a12811](https://github.com/facebook/zstd/commit/2a128110d05aa5f67c9faee55a4fc538c169c16b), [cb9e341](https://github.com/facebook/zstd/commit/cb9e3411292133c4e2b96ef331760eefdf895f23), [6bd5ac6](https://github.com/facebook/zstd/commit/6bd5ac671352801cd249576d94606bdc0ef235ec), [747e06f](https://github.com/facebook/zstd/commit/747e06f4f6db99d7f4a05f6a0d4a5490da7c944f), [93b89fb](https://github.com/facebook/zstd/commit/93b89fb24b1e019ffc2df027993d04e4c0cadfef)
- Added maxBlockSize parameter, allowing users to control the maximum block size, and supports setting it to 0 to use the default value. (Architecture-related: public API: new maxBlockSize parameter)
  ↳ [#3418](https://github.com/facebook/zstd/pull/3418): [908e812](https://github.com/facebook/zstd/commit/908e8127335ccc6acf23fbaec601aecfba30e96f), [fe08137](https://github.com/facebook/zstd/commit/fe08137d9abbf72bcb01740c7b398179ac5cb85e), [1fffcfe](https://github.com/facebook/zstd/commit/1fffcfe01d56b69d8ab09b79e4dbe37c9a091dda), [06b096d](https://github.com/facebook/zstd/commit/06b096db473ef28fe58e34d75d30825970c403fe)
- Added a generic C version of the fast decoding loop for architectures without assembly implementation, and added the ZSTD_d_disableHuffmanAssembly parameter to allow selection of the C decoding loop. (Architecture-related: Platform compatibility: Generic C decoding loop)
  ↳ [#3449](https://github.com/facebook/zstd/pull/3449): [8957fef](https://github.com/facebook/zstd/commit/8957fef554e844ef724022075ffdf740464aa515)
- Adjusted the HUF optimal depth threshold, and added the HUF_cardinality function to optimize the table depth selection under high compression levels and improve the compression ratio. (Architecture-related: public API: new HUF_cardinality function)
  ↳ [#3285](https://github.com/facebook/zstd/pull/3285): [e60cae3](https://github.com/facebook/zstd/commit/e60cae33cf88b035380aa6d953e08c01f5cbff96), [75cd42a](https://github.com/facebook/zstd/commit/75cd42afd71daaef691f2c890e77ed22650f29cb)
- Added in-place decompression support, including functions and macros for calculating decompression boundaries to ensure that the output buffer does not overlap the input. (Architecture-related: public API)
  ↳ [#3421](https://github.com/facebook/zstd/pull/3421): [5b26619](https://github.com/facebook/zstd/commit/5b266196a41e6a15e21bd4f0eeab43b938db1d90)
- Support decompression of empty data blocks, adjust the minimum compression block size from 3 to 2, and fix the related verification logic. (Architecture-related: core behavior)
  ↳ [#3118](https://github.com/facebook/zstd/pull/3118): [43f21a6](https://github.com/facebook/zstd/commit/43f21a600ec431aa615b09868f1f586b949607fb)
- Fixed slight compression differences in the btlazy2 parser due to sumtype numerical representation dependency, and unified offBase representation. (Architecture-related: core compression module)
  ↳ [#2965](https://github.com/facebook/zstd/pull/2965): [03903f5](https://github.com/facebook/zstd/commit/03903f57012054852c0c26daca7131a130bb5cbf), [f92ec5e](https://github.com/facebook/zstd/commit/f92ec5ea54d64207f5ffd30b5c746367a6e75dc4), [7a18d70](https://github.com/facebook/zstd/commit/7a18d709ae5a8ba53c5199adb2e8461cb216fb00)
- Move the HufLog macro definition from the public header file to the decompressed internal header file, and fix the return value type conversion of several parameter setting functions. (Architecture-related: public API)
  ↳ [#3019](https://github.com/facebook/zstd/pull/3019): [32a5d95](https://github.com/facebook/zstd/commit/32a5d95dcb873044cb6af4921772510e619ac9e7), [2d154e6](https://github.com/facebook/zstd/commit/2d154e627a9961b728ee5943076c639b3942bbaa)
- Introduced the LitHufLog constant to correctly represent the maximum bit size of compressed literals (11), replaced the original default values ​​in many places in the code, and fixed several type conversion warnings. (Architecture-related: core compression module)
  ↳ [#3019](https://github.com/facebook/zstd/pull/3019): [a66e8bb](https://github.com/facebook/zstd/commit/a66e8bb437203df68910f9d898dd9434bbf8f08a)
- Fix the processing logic of zero-valued input in the bit operation inline function, and adjust the conditional compilation details. (Architecture-related: public API)
  ↳ [#3045](https://github.com/facebook/zstd/pull/3045): [529cd7b](https://github.com/facebook/zstd/commit/529cd7b82174cde8a6ad62a8d6ec666b530cb3ac)
- Reconstruct the bit operation inline functions in bits.h to implement unified implementation and fix the STATIC_BMI2 check and _BitScanReverse return value calculation errors under MSVC. (Architecture-related: public API)
  ↳ [#3045](https://github.com/facebook/zstd/pull/3045): [6994a9f](https://github.com/facebook/zstd/commit/6994a9f99c97f817e42f638840b65c53cad2479b), [7961826](https://github.com/facebook/zstd/commit/796182652d652d57fca9ece6c63715db2d0e0858), [856c7dc](https://github.com/facebook/zstd/commit/856c7dc51dcccc0c6f31a48e42a7a29475351828)
- Fix the compatibility issue of NEON path under big-endian ARM architecture and ensure that NEON acceleration is only enabled in little endian environment. (Architecture-related: platform compatibility)
  ↳ [#3160](https://github.com/facebook/zstd/pull/3160): [05f3f41](https://github.com/facebook/zstd/commit/05f3f415ce3ca73abc82936752829a3ee75242e2)
- Streaming decompression now detects incorrect header IDs as soon as the first byte is supplied, instead of waiting for at least 5 bytes before reporting an error. (Architecture-related: external behavior)
  ↳ [#3175](https://github.com/facebook/zstd/pull/3175): [91aeade](https://github.com/facebook/zstd/commit/91aeade7352a31b96944ee68112e748d0c42635c)
- Fixed the memory read byte order problem of the ZSTD_hash4Ptr function on big-endian systems. (Architecture-related: platform compatibility)
  ↳ [#3227](https://github.com/facebook/zstd/pull/3227): [1b445c1](https://github.com/facebook/zstd/commit/1b445c1c2e89982ad7be6b7fa13a9a1bdc658cb2)
- Fixed the C4267 warning caused by size_t to int conversion when compiling MSVC (C2220 error under ARM64), changed the type of local variable chunkSize from size_t to int. (Architecture-related: platform compatibility)
  ↳ [#3320](https://github.com/facebook/zstd/pull/3320): [0168914](https://github.com/facebook/zstd/commit/016891449033a3f0aa5ca9ac84dd84d607cdafb3)
- Updated the specification to require that 4-streams mode requires at least 6 literals to trigger, and added corresponding checks in the decoder. (Architecture-related: decoding behavior)
  ↳ [#3398](https://github.com/facebook/zstd/pull/3398): [6a9c525](https://github.com/facebook/zstd/commit/6a9c525903ca65aad61b50381b5781c1187143d1)
- Fixed the data corruption bug caused by incorrect threshold judgment in literal compression, replaced the heuristic judgment by adding actual byte consistency check, and adjusted the minimum literal compression threshold logic. (Architecture-related: public API)
  ↳ [#3419](https://github.com/facebook/zstd/pull/3419): [796699c](https://github.com/facebook/zstd/commit/796699c0bc12ae1efa405418b14cb6dd0101cc6f)
- Fixed C89 compatibility warning introduced by parallel merge. (Architecture-related: platform compatibility)
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [d9280af](https://github.com/facebook/zstd/commit/d9280afb7dfb39aa6417e7465c3905f2de864bbd)
- Fixed long offset parsing issue, allocating extra space for long offsets in memory estimation. (Architecture-related: public API)
  ↳ [#3460](https://github.com/facebook/zstd/pull/3460): [814f4bf](https://github.com/facebook/zstd/commit/814f4bfb993c6a1a171b2321f69afcd0dea01f1b)
- Fixed long offset processing logic on 32-bit systems, including multiple scenarios in compression and decompression to avoid data corruption. (Architecture-related: core compression behavior)
  ↳ [#3460](https://github.com/facebook/zstd/pull/3460): [2bde9fb](https://github.com/facebook/zstd/commit/2bde9fbf85d5044b0c95938f8a976420f0022945) | [#3467](https://github.com/facebook/zstd/pull/3467): [2f74507](https://github.com/facebook/zstd/commit/2f74507bbd0e8aca907a2842a311cc24ec815cf2) | [#3472](https://github.com/facebook/zstd/pull/3472): [cc3e3ac](https://github.com/facebook/zstd/commit/cc3e3acd3415cfb14aad5fbe4e819fcf20760e8f)
- Fixed buffer overflow and bounds checking issues in multiple legacy format decoders to enhance security and stability. (Architecture-related: backward compatibility)
  ↳ [#3476](https://github.com/facebook/zstd/pull/3476): [e04706c](https://github.com/facebook/zstd/commit/e04706c58cc462cc771292c01abc66caaebe57a6), [cfec005](https://github.com/facebook/zstd/commit/cfec005efd13b45433210ad8db543de3440fe2ad), [7eb4471](https://github.com/facebook/zstd/commit/7eb4471fec8807b67a8475ad13cdf0310f2fad81), [b20e4e9](https://github.com/facebook/zstd/commit/b20e4e95f2a9295adf82c4fdb13bcb1864983fd9), [7a1a171](https://github.com/facebook/zstd/commit/7a1a1716587c7e600e7c1759daccf5c679b6d961), [67d7a65](https://github.com/facebook/zstd/commit/67d7a659f871a1bfbd99e82ad5036e619b7ca758), [9419747](https://github.com/facebook/zstd/commit/94197471719757d9dcf7aca10705d829a45817c8), [c5bf6b8](https://github.com/facebook/zstd/commit/c5bf6b8b88456804b480176c6183a893ca01bf15)
- Fixed potential buffer overflow and error propagation issues caused by invalid sequences generated by external matchfinders. (Architecture-related: external matchfinder security)
  ↳ [#3465](https://github.com/facebook/zstd/pull/3465): [64052ef](https://github.com/facebook/zstd/commit/64052ef57d09a9117ccf1c535d3387f0d5270ca9)
- Replaced multiple Boolean parameters of the Huffman function with the flags bit field, added a new flag to disable the assembly decoder, and deleted unused functions and old suffix functions. (Architecture event: Core_Compression module change)
  ↳ [#3434](https://github.com/facebook/zstd/pull/3434): [0cc1b0c](https://github.com/facebook/zstd/commit/0cc1b0cb224041b33eaef1ca97e1711fd5181b6a), [3291691](https://github.com/facebook/zstd/commit/329169189c248696c197ef9b88eb97c315bfb831)
- Uniformly use memcpy for unaligned memory access in the legacy code base, and remove other non-memcpy implementations. (Architecture-related: platform compatibility)
  ↳ [#3355](https://github.com/facebook/zstd/pull/3355): [728e73e](https://github.com/facebook/zstd/commit/728e73ebb49e316233cc79f8afe79209eb2a5e90)
- Remove all unused FSE functions, remove dead code and avoid stack usage confusion. (Architecture-related: public API)
  ↳ [#3462](https://github.com/facebook/zstd/pull/3462): [423a749](https://github.com/facebook/zstd/commit/423a74986f7416ca8f54b20d0fe880f2d232b213)
- Changed the implementation of unaligned memory access from packed attribute to aligned attribute, improved code generation on ARMv6, ARMv7 and aarch64, and cleaned up duplicate implementation in legacy code. (Architecture-related: Platform compatibility)
  ↳ [#2881](https://github.com/facebook/zstd/pull/2881): [a78c91a](https://github.com/facebook/zstd/commit/a78c91ae59b9487fc32224b67c4a854dc3720367)
- Replace the bit operations in BIT_addBits with the BIT_getLowerBits helper function, and add conditional compilation protection supported by the BMI2 instruction to it to improve code clarity and reduce data cache pressure. (Architecture-related: platform compatibility)
  ↳ [#3075](https://github.com/facebook/zstd/pull/3075): [0178c12](https://github.com/facebook/zstd/commit/0178c12dd98ad5e63968b12eaaf32e3162a0ffee)
- On the aarch64 architecture, replace the memory copy method of ZSTD_wildcopy from a simple loop to an optimized two-stage copy to improve performance. (Architecture-related: Platform compatibility: aarch64)
  ↳ [#3145](https://github.com/facebook/zstd/pull/3145): [d7249da](https://github.com/facebook/zstd/commit/d7249dafb43825dc2048a6bdce4e3c9b7606e0ae)
- In the decompression process of aarch64 architecture, add L1 prefetching for matching locations that will be used for sequence replication to reduce cache misses and improve performance. (Architecture-related: platform compatibility)
  ↳ [#3164](https://github.com/facebook/zstd/pull/3164): [558cf20](https://github.com/facebook/zstd/commit/558cf20d0dacf9436959ec1ec6a5acb60152ebbb)
- Fixed the out-of-bounds access problem caused by improper offset calculation in the FSE decompression function, and changed the assertion to conditional judgment in the dictionary training function to eliminate null pointer false positives. (Architecture-related: public API)
  ↳ [#3020](https://github.com/facebook/zstd/pull/3020): [8d65f87](https://github.com/facebook/zstd/commit/8d65f87416740444da4a713d2778b78c11c6b38b)
- Rewrite the boundary check logic of the old version v0.7, no longer rely on address space overflow, and fix potential security issues discovered by oss-fuzz. (Architecture-related: legacy format backward compatibility)
  ↳ [#3476](https://github.com/facebook/zstd/pull/3476): [c689310](https://github.com/facebook/zstd/commit/c689310b2544c1eee6002bb4fa9a7ed8c7609dd1)
- Fix CI failure, correct type conversion and error message display level, improve command line parameter parsing, and add HUF minimum table log calculation function. (Architecture-related: public API)
  ↳ [#3285](https://github.com/facebook/zstd/pull/3285): [8888a2d](https://github.com/facebook/zstd/commit/8888a2ddcc3c242db4b3ea8086605ab71d2cfc0d)
- Enable the STATIC_BMI2 macro for the GCC and Clang compilers to use the BMI2 directive on x86_64 platforms that support BMI2, and add corresponding compilation condition checks. (Architecture-related: Platform compatibility)
  ↳ [#3080](https://github.com/facebook/zstd/pull/3080): [7c3d1cb](https://github.com/facebook/zstd/commit/7c3d1cb3ab9b43745c65bb1796960dbbaa237a02)

### Platform Adaptation Layer
- Added fileio_asyncio module, separated asynchronous I/O code from fileio.c, and created public header files fileio_common.h and fileio_types.h. (Architecture-related: Separation of module responsibilities)
  ↳ [#3021](https://github.com/facebook/zstd/pull/3021): [70df5de](https://github.com/facebook/zstd/commit/70df5de1b2fc291a58c1b3199dde11b353ccad8f)
- Added zstd_common kernel module, changed the kernel-specific code to external mode, and updated the test header file to support GPL symbol export. (Architecture-related: kernel module and GPL export)
  ↳ [#3292](https://github.com/facebook/zstd/pull/3292): [330558a](https://github.com/facebook/zstd/commit/330558ad52d24875c8260670b42eeb75dbef7161)
- Refactor the timefn interface to make timer storage types independent of operating system features, and restore clock_gettime() high-resolution timer support on POSIX systems. (Architecture-related: platform compatibility)
  ↳ [#3423](https://github.com/facebook/zstd/pull/3423): [bcfb7ad](https://github.com/facebook/zstd/commit/bcfb7ad03c47d3018eeaec2c68be9d37dc114151), [a2ef23d](https://github.com/facebook/zstd/commit/a2ef23dec03a18978dc945cee557d280160f8cb6) | [#3447](https://github.com/facebook/zstd/pull/3447): [638d502](https://github.com/facebook/zstd/commit/638d502002b6fbecb3e8ccc79b159766e1244a83)
- Enabled Intel CET support for x86-64 ELF targets, added .note.gnu.property section in assembly source files. (Architecture-related: Platform compatibility)
  ↳ [#2992](https://github.com/facebook/zstd/pull/2992): [51ab182](https://github.com/facebook/zstd/commit/51ab182bd4af347b08fd1b9df179078c4f596e24) | [#3015](https://github.com/facebook/zstd/pull/3015): [7cf80cb](https://github.com/facebook/zstd/commit/7cf80cb94c23867f7496f6a847f7d4e712dafb86)
- Added asynchronous I/O support for compression and decompression, including asynchronous reading and writing, and added the --[no-]asyncio command line option. (Architecture-related: asynchronous I/O support)
  ↳ [#2975](https://github.com/facebook/zstd/pull/2975): [1598e6c](https://github.com/facebook/zstd/commit/1598e6c634ac041c1928c1be00dfa3484d282397) | [#3022](https://github.com/facebook/zstd/pull/3022): [cc0657f](https://github.com/facebook/zstd/commit/cc0657f27d81da8a7db3aa199d24a566b95c4dfe)
- Add aarch64 to the list of supported architectures for zstd_trace. (Architecture-related: Platform compatibility)
  ↳ [#3054](https://github.com/facebook/zstd/pull/3054): [fede1d3](https://github.com/facebook/zstd/commit/fede1d3abe08f52ab981eefa5c87208334933f36)
- Added the --trace-file-stat option, which is used to output trace information of file metadata read and write operations on stderr. (Architecture-related: CLI interface)
  ↳ [#3394](https://github.com/facebook/zstd/pull/3394): [b6e8112](https://github.com/facebook/zstd/commit/b6e8112261a0d60476d52a10be8fd3be0287996d)
- Reconstruct the progress bar and summary row display logic, centralize control of display conditions, make the --progress option effective for non-zstd compressors, and fix several edge cases. (Architecture-related: public API)
  ↳ [#2984](https://github.com/facebook/zstd/pull/2984): [fbff782](https://github.com/facebook/zstd/commit/fbff7827faba30df7c49992cb39dc00ce36c6a06)
- Fixed the issue where the --auto-threads option was ignored when multi-threading was not enabled. Now even if ZSTD_MULTITHREAD is not defined, this option will be parsed normally. (Architecture-related: build and installation methods)
  ↳ [#3020](https://github.com/facebook/zstd/pull/3020): [495dcb8](https://github.com/facebook/zstd/commit/495dcb839ab6ab40c4156b99be16b010389f2214)
- When using the -c or --stdout option, zstd no longer deletes the original file to be compatible with gzip(1) behavior. (Architecture-related: public API)
  ↳ [#3052](https://github.com/facebook/zstd/pull/3052): [3f4f8b0](https://github.com/facebook/zstd/commit/3f4f8b04ed2d318536c9f54e0c575603ed75d92f)
- Fixed pointer invalidation and return value errors caused by thread rearrangement in the Windows thread/pthread conversion layer, and removed the return value support of ZSTD_pthread_join. (Architecture-related: public API)
  ↳ [#3364](https://github.com/facebook/zstd/pull/3364): [500f02e](https://github.com/facebook/zstd/commit/500f02eb66419d399a521e685825846c4da0acf2), [26f1bf7](https://github.com/facebook/zstd/commit/26f1bf7d70f8cb484e8f68c0410818767cfc4f8c)
- Fixed a race condition in the Windows thread/pthread translation layer, introduced a synchronization structure to ensure thread safety, and simplified the ZSTD_pthread_t type from a structure to a HANDLE. (Architecture-related: public API)
  ↳ [#3364](https://github.com/facebook/zstd/pull/3364): [ec42c92](https://github.com/facebook/zstd/commit/ec42c92aaa13815164bb0ecb6e2483aff2fc78d9)
- Fixed the problem that --adapt failed when --no-progress was used, and separated the parameter adaptation logic from the display update rate. (Architecture-related: public API)
  ↳ [#3354](https://github.com/facebook/zstd/pull/3354): [15f32ad](https://github.com/facebook/zstd/commit/15f32ad74ccf1f10efc93fdc4a180e7eba3e387e)
- Fixed pzstd compilation issues under Windows, including adding header files to resolve min/max macro conflicts, fixing type conversion warnings, and adding assertion checks for windowLog and compression size. (Architecture-related: platform compatibility)
  ↳ [#3380](https://github.com/facebook/zstd/pull/3380): [e9797b5](https://github.com/facebook/zstd/commit/e9797b5dc5c4a703fd13cf2e86d278b275825bb3)
- Remove fileio_types.h's dependency on mem.h, and fix related type conversion warnings. (Architecture-related: internal dependency cleanup)
  ↳ [#3232](https://github.com/facebook/zstd/pull/3232): [3dfcafa](https://github.com/facebook/zstd/commit/3dfcafacd74e5b36fad1191dc8b3a1e1cdcbcb8c)
- When the poisoning function of memory or address sanitizer is disabled, the corresponding poisoning function is no longer declared. (Architecture-related: build requirements)
  ↳ [#3424](https://github.com/facebook/zstd/pull/3424): [d78fbed](https://github.com/facebook/zstd/commit/d78fbedd968988270c27c215ae5f592990f0bc1d)
- Add missing time.h header include in test files for Windows platform. (Architecture-related: platform compatibility)
  ↳ [#3423](https://github.com/facebook/zstd/pull/3423): [2086e73](https://github.com/facebook/zstd/commit/2086e7396e659143dfe0c6d292e63f1332ec496d)
- Add conditionals to the build system, and append Intel CET detection linker flags when the compiler supports it, to detect missing CET flags when -fcf-protection is enabled. (Architecture-related: Platform compatibility)
  ↳ [#2994](https://github.com/facebook/zstd/pull/2994): [d6fcdd1](https://github.com/facebook/zstd/commit/d6fcdd123cbf05735c894c81599a0926c3427d4f)
- Fixed the problem of missing the correct include directory when compiling resource files in Meson build on Windows. (Architecture-related: platform compatibility)
  ↳ [#3039](https://github.com/facebook/zstd/pull/3039): [5b2c6c7](https://github.com/facebook/zstd/commit/5b2c6c776acadcd86247fdaa3e48c11c6848263e)
- The search for the libm library in the build system is no longer mandatory and becomes optional to support Windows platforms without independent libm. (Architecture-related: platform compatibility)
  ↳ [#3039](https://github.com/facebook/zstd/pull/3039): [84c0545](https://github.com/facebook/zstd/commit/84c05453db61a5c518bda486ea36b0c00fc645a1)
- Changed legacy support level to be configurable via CMake cache variables, allowing default values to be overridden from the command line. (Architecture-related: build and installation methods)
  ↳ [#3050](https://github.com/facebook/zstd/pull/3050): [317bd10](https://github.com/facebook/zstd/commit/317bd108fe7b75ac426ad7ff95f9ca48536f0b03)
- Enable ZSTD legacy format support by default in CMake builds, and simultaneously update the sample configuration in the build documentation. (Architecture-related: build and installation methods)
  ↳ [#3079](https://github.com/facebook/zstd/pull/3079): [03bba1b](https://github.com/facebook/zstd/commit/03bba1b0bfe3d877be354d9ba6b29532a1751e9e)
- Add missing util.h header file reference in fileio.h to fix compilation order issue. (Architecture-related: public API)
  ↳ [#3231](https://github.com/facebook/zstd/pull/3231): [a925362](https://github.com/facebook/zstd/commit/a92536253418e1e406c21269d87bb511edea3ee9)
- Improved pkg-config generation for the CMake build system, populating Libs.private, using the JoinPaths module, and always generating .pc files. (Architecture-related: pkg-config configuration)
  ↳ [#3252](https://github.com/facebook/zstd/pull/3252): [a0b09d0](https://github.com/facebook/zstd/commit/a0b09d0ff735d34fd99029bb59ffff2874565b42) | [#3267](https://github.com/facebook/zstd/pull/3267): [966ac9d](https://github.com/facebook/zstd/commit/966ac9d200a9753225625f8cea2bf65f72d0c961)
- Fix pzstd build on MSVC, by conditionalizing compiler options and adjusting NDEBUG handling. (Architecture-related: Platform compatibility)
  ↳ [#3357](https://github.com/facebook/zstd/pull/3357): [e0ef09d](https://github.com/facebook/zstd/commit/e0ef09ddba8ebe0cde6786bc3305b43438de0baf)
- Update CircleCI base image to focal, and re-enable aarch64 build. (Architecture-related: platform compatibility)
  ↳ [#3367](https://github.com/facebook/zstd/pull/3367): [ef566c8](https://github.com/facebook/zstd/commit/ef566c8d683212a04174124ef3c0d34cdfb583b5)
- Add noexecstack flag to compiler and linker in CMake build, and extend compile flag function to support checking and setting of linker flag. (Architecture-related: platform compatibility)
  ↳ [#3392](https://github.com/facebook/zstd/pull/3392): [31a703e](https://github.com/facebook/zstd/commit/31a703ec13c197d1ec0939855bb31599ae9be1c8)
- Disable custom ASAN/MSAN taint for MinGW builds. (Architecture-related: Platform compatibility)
  ↳ [#3424](https://github.com/facebook/zstd/pull/3424): [f10922a](https://github.com/facebook/zstd/commit/f10922a8fa84d332a4d001bc2a1f659a00ae0213)

### High-Level API & Mode Layer
- Add two reserved fields to the ZSTD_frameHeader structure for future expansion. (Architecture-related: public API)
  ↳ [#3349](https://github.com/facebook/zstd/pull/3349): [e1e82f7](https://github.com/facebook/zstd/commit/e1e82f74f1f992acb6d98577e167d2e7cfe45f70)
- Relaxed the usage restrictions of stable input/output buffer mode, making it compatible with regular streaming compression API, and added error codes when stability conditions are not followed. (Architecture-related: public API and error codes)
  ↳ [#2974](https://github.com/facebook/zstd/pull/2974): [c0c5ffa](https://github.com/facebook/zstd/commit/c0c5ffa97385063ce9b24432e7c0c4130ed26e27), [37b87ad](https://github.com/facebook/zstd/commit/37b87add7a158deee06a12743aac11c36c352340), [27d336b](https://github.com/facebook/zstd/commit/27d336b099d3e4b19969a24e7425a14af86d4879), [8296be4](https://github.com/facebook/zstd/commit/8296be4a0a25b6e2f74f1cdd7bd4ae04981f6a45), [cbff372](https://github.com/facebook/zstd/commit/cbff372d105cb0593af24aba780481c83ef8d2ab), [b99ece9](https://github.com/facebook/zstd/commit/b99ece96b99b7015169d5e11d45078f21bfa6bd4), [dda4c10](https://github.com/facebook/zstd/commit/dda4c10f0710d24685ee8490e9715d18300665f1), [270f9bf](https://github.com/facebook/zstd/commit/270f9bf00595160933652d92a809a2dab61cfeed)
- Introduced block-level external sequence generator API, added ZSTD_sequenceBound function to calculate the upper limit of the number of sequences, and ZSTD_c_searchForExternalRepcodes parameter to control duplicate code search. (Architecture-related: public API: New external sequence generator API)
  ↳ [#3333](https://github.com/facebook/zstd/pull/3333): [2a40262](https://github.com/facebook/zstd/commit/2a402626dd046bf17e6172fe8d829ed5a443fbe3) | [#3471](https://github.com/facebook/zstd/pull/3471): [7f8189c](https://github.com/facebook/zstd/commit/7f8189ca57741f89b98b06fabfeffb2c8b8683b5), [3fe5f1f](https://github.com/facebook/zstd/commit/3fe5f1fbb9fde42d50cbe35f89775d284663da99) | [#3262](https://github.com/facebook/zstd/pull/3262): [aa82998](https://github.com/facebook/zstd/commit/aa829988215273f8c8b1423e1a924b326168e09f), [1613caf](https://github.com/facebook/zstd/commit/1613caf8bd1994c41728e43de75638ac79003164) | [#3437](https://github.com/facebook/zstd/pull/3437): [3f9f568](https://github.com/facebook/zstd/commit/3f9f568aa6401c1902138012760d4c53780f7bb4)
- Added ZSTD_CCtx_setCParams() function, allowing to set all compression parameters with one call. (Architecture-related: public API)
  ↳ [#3403](https://github.com/facebook/zstd/pull/3403): [89342d1](https://github.com/facebook/zstd/commit/89342d1e076e86e59d143ce2fa3b8e8af6f65b03) | [#3487](https://github.com/facebook/zstd/pull/3487): [00c85b2](https://github.com/facebook/zstd/commit/00c85b28e724dca2ceeac8ac8ef319c282ad3f5c)
- Added two new error codes for the busy loop scenario, respectively indicating that the output buffer is full and the input cannot be advanced due to empty input. (Architecture-related: public API)
  ↳ [#3455](https://github.com/facebook/zstd/pull/3455): [db18a62](https://github.com/facebook/zstd/commit/db18a62f8994a091a746d64001b7c767fae64545)
- Fixed the problem of missing ZSTD MAGIC header when compressing empty strings in seekable format. (Architecture event: seekable format module change)
  ↳ [#3346](https://github.com/facebook/zstd/pull/3346): [f176529](https://github.com/facebook/zstd/commit/f17652931c4f8cebeecebbc4f4a45c47eb81ffca)
- Fixed the block boundary selection problem of the sequence compression API in Explicit Delimiter mode, now allowing the caller to arbitrarily specify the block boundary. (Architecture-related: public API)
  ↳ [#3023](https://github.com/facebook/zstd/pull/3023): [87dcd33](https://github.com/facebook/zstd/commit/87dcd3326a587c7e9d61c2910f38337aa014355d)
- Fix the extension used in conjunction with continue() and flush() modes when ZSTD_c_stableInBuffer is enabled, making it compatible with these modes in the streaming interface. (Architecture-related: public API)
  ↳ [#2974](https://github.com/facebook/zstd/pull/2974): [c1668a0](https://github.com/facebook/zstd/commit/c1668a00d2d71915582a22c3c0082f59cfee53bd)
- Fixed an issue in the Sequence Compression API where the buffer size was not checked due to too small dstCapacity. This is a security fix. (Architecture-related: public API)
  ↳ [#3040](https://github.com/facebook/zstd/pull/3040): [cad9f8d](https://github.com/facebook/zstd/commit/cad9f8d5f9c451b1cc8ce00a16c125e3d2ffc418) | [#3036](https://github.com/facebook/zstd/pull/3036): [9a758ce](https://github.com/facebook/zstd/commit/9a758ce52068b2daffd36a6ae9af16adf5791f14)
- Fixed compilation warnings and C++ compatibility warnings caused by the use of deprecated APIs in the Linux kernel Zstd compression module, and replaced them with recommended APIs to ensure consistent functionality. (Architecture-related: public API)
  ↳ [#3088](https://github.com/facebook/zstd/pull/3088): [e470c94](https://github.com/facebook/zstd/commit/e470c940f6cb6cfff4b27d595ec651a3c1c2cc15), [8ff20c2](https://github.com/facebook/zstd/commit/8ff20c25f38f62cd1e898cf81173e280f42327f5), [498ac82](https://github.com/facebook/zstd/commit/498ac8238d98cc5f7153fa58a5e0a5222ffd88be)
- Update zlibWrapper to be compatible with zlib 1.2.12, replace macros and add backward compatibility definitions. (Architecture-related: platform compatibility)
  ↳ [#3217](https://github.com/facebook/zstd/pull/3217): [1e09cff](https://github.com/facebook/zstd/commit/1e09cffd9b15b39379810a39ffae182b4a7e7b78)
- Adjust the position of the ZSTD_DEPRECATED macro in the function declaration, and fix compilation errors in C++14 and C++17 modes under the Clang compiler. (Architecture-related: platform compatibility)
  ↳ [#3273](https://github.com/facebook/zstd/pull/3273): [5635827](https://github.com/facebook/zstd/commit/5635827ede68d3774f70144fcd39589a2d8d5a15)
- Optimize the ZSTD_getDictID_fromDDict function to directly read the dictionary ID in the DDict structure, avoid re-parsing the dictionary buffer, improve efficiency and return the correct ID when memory is damaged. (Architecture-related: public API)
  ↳ [#3290](https://github.com/facebook/zstd/pull/3290): [d7841d1](https://github.com/facebook/zstd/commit/d7841d150be6355d9dd06ccc433589c81a8fb1f8)
- Fix the pointer operation problem of NULL + 0 in ZSTD_decompressStream, and improve the stream_decompress fuzzer to support empty buffer input. (Architecture-related: public API)
  ↳ [#3356](https://github.com/facebook/zstd/pull/3356): [f31b83f](https://github.com/facebook/zstd/commit/f31b83ff34236b4c8ec7dc5332c52a7e67952215) | [#3258](https://github.com/facebook/zstd/pull/3258): [69022ad](https://github.com/facebook/zstd/commit/69022ad886ccf2fa9498baefe860c37e37c638ea), [282a955](https://github.com/facebook/zstd/commit/282a955d33afbb5c318e9f2cb48a07ad104aad17)
- Fixed the problem in ZSTD_compressBound that may cause overflow due to srcSize error, and updated related comments. (Architecture-related: public API)
  ↳ [#3362](https://github.com/facebook/zstd/pull/3362): [45ed0df](https://github.com/facebook/zstd/commit/45ed0df18a24430875fb4e90378b150e15c200f7), [97f63ce](https://github.com/facebook/zstd/commit/97f63ce2b558edb44c290b0d3a3385f7abe809c4)
- Fixed the intermediate result overflow problem of ZSTD_decompressBound on 32-bit platforms. (Architecture-related: public API)
  ↳ [#3373](https://github.com/facebook/zstd/pull/3373): [ea24b88](https://github.com/facebook/zstd/commit/ea24b886673a1e154a81d71222d130f65da7a0ed)
- Fixed the compatibility issue of ZSTD_COMPRESSBOUND macro when the input size is 0. (Architecture-related: public API)
  ↳ [#3373](https://github.com/facebook/zstd/pull/3373): [2f4238e](https://github.com/facebook/zstd/commit/2f4238e47ac6dcf923dcf95f129a283cb1cfa642)
- Adjust the position of the deprecation mark so that it is before the static API macro to solve the compatibility issue when clang compiles C++ code. (Architecture-related: platform compatibility)
  ↳ [#3400](https://github.com/facebook/zstd/pull/3400): [48f4aa7](https://github.com/facebook/zstd/commit/48f4aa7307003bbe496fad4cd4090b7fa93df6f0)
- Fix the inclusion guard of zdict.h to ensure that static link special symbols can still be exposed correctly when included multiple times. (Architecture-related: public API)
  ↳ [#3372](https://github.com/facebook/zstd/pull/3372): [2f7b8d4](https://github.com/facebook/zstd/commit/2f7b8d47fb580ab931a67d2b323f0883395a0ab9)
- Added invalid external sequence error code, and renamed related errors to externalSequences_invalid. (Architecture-related: public API)
  ↳ [#3439](https://github.com/facebook/zstd/pull/3439): [1b65727](https://github.com/facebook/zstd/commit/1b65727e7451d6cff83b6a96364ffedfef251fb7), [815d1d4](https://github.com/facebook/zstd/commit/815d1d4edaf8d69a73fdbc59dd6caf3c5f71cf43)
- Fixed multiple issues with the external matcher API: corrected memory space estimation, removed incorrect assertions, prohibited simultaneous use with multiple threads, supported clearing matchers by passing in NULL. (Architecture-related: public API)
  ↳ [#3433](https://github.com/facebook/zstd/pull/3433): [bce0382](https://github.com/facebook/zstd/commit/bce0382c828b502e5d9db6e58f43c25abf16ea02)
- Limit the upper limit of hashLog and chainLog, ensure that only 32-bit hashes are used, and adjust the window size judgment condition to use memory more accurately. (Architecture-related: public API)
  ↳ [#3438](https://github.com/facebook/zstd/pull/3438): [666944f](https://github.com/facebook/zstd/commit/666944fbe6bb5e6d84a343ad4df525af79720165)
- Fixed the problem that when attaching a dictionary in the unbuffered API, the dictionary was not correctly invalidated because non-contiguous segments were not detected. (Architecture-related: public API)
  ↳ [#3441](https://github.com/facebook/zstd/pull/3441): [b4467c1](https://github.com/facebook/zstd/commit/b4467c10611018eef3189ffc6faf681c8b4eca6b)
- Fix the build error of zstd seekable format on 32-bit platform, add explicit size_t type conversion in ZSTD_seekable_decompress function. (Architecture-related: platform compatibility)
  ↳ [#3452](https://github.com/facebook/zstd/pull/3452): [63042f1](https://github.com/facebook/zstd/commit/63042f1f11b72da52f137d46ad9ffca772a9ac1c)
- Roll back the deprecation marks for ZSTD_copyCCtx and ZSTD_copyDCtx, and reconstruct the positions of relevant function declarations and deprecated macros to improve code clarity. (Architecture-related: public API)
  ↳ [#3196](https://github.com/facebook/zstd/pull/3196): [a5655e4](https://github.com/facebook/zstd/commit/a5655e4017c223081b0345710bfef85972f4bd87) | [#3274](https://github.com/facebook/zstd/pull/3274): [434ffe9](https://github.com/facebook/zstd/commit/434ffe979cbf6fdf20aa5458766fb5bc0847aa74)
- Unified the visibility macro name to *_VISIBLE and maintained backward compatibility; added ZDICTLIB_STATIC_API macro to the zdict library. (Architecture-related: public API)
  ↳ [#3363](https://github.com/facebook/zstd/pull/3363): [358a237](https://github.com/facebook/zstd/commit/358a2374848d6b9c4fb20a254c038e27bb1527ac)
- Deprecated high-level streaming functions and removed their internal use. (Architecture-related: public API)
  ↳ [#3408](https://github.com/facebook/zstd/pull/3408): [5d8cfa6](https://github.com/facebook/zstd/commit/5d8cfa6b96a6442ab1251f9de3b47a0eb12561a0)
- Renamed External Matchfinder to Block-Level Sequence Producer, and updated all related function names, type names, parameter names, error codes and test cases. (Architecture-related: public API)
  ↳ [#3484](https://github.com/facebook/zstd/pull/3484): [ff42ed1](https://github.com/facebook/zstd/commit/ff42ed1582bf15fbeb1585df71e42676a7d49da7)
- Move the ZSTD_BLOCKSIZE_MAX_MIN macro definition to the static link dedicated area. (Architecture-related: public API)
  ↳ [#3418](https://github.com/facebook/zstd/pull/3418): [14b8def](https://github.com/facebook/zstd/commit/14b8defb86b3e25086fafb720a4b90048a7bd779)
- Added basic functional tests for the maxBlockSize parameter, and corrected related macro definitions and comments. (Architecture-related: public API)
  ↳ [#3418](https://github.com/facebook/zstd/pull/3418): [53eb5a7](https://github.com/facebook/zstd/commit/53eb5a758c4e618c106eebafa49abde5845f96ef)
- Remove the deprecated API in the longmatch.c test and use the new API instead. (Architecture-related: API migration)
  ↳ [#3395](https://github.com/facebook/zstd/pull/3395): [4b40e40](https://github.com/facebook/zstd/commit/4b40e405d355f67cac166db8fdd901c34b9a228e)
- Fixed the problem of inconsistency between the match length check and the context in the sequence verification logic, and corrected the seqStore boundary check to prevent out-of-bounds writing. (Architecture-related: public API)
  ↳ [#3439](https://github.com/facebook/zstd/pull/3439): [aa385ec](https://github.com/facebook/zstd/commit/aa385ece13b0a847380303a3918609213eea45e0)
- Fixed documentation errors for ZSTD_estimate* and ZSTD_initCStream(), removed the error warning that the old streaming API is incompatible with advanced parameters and dictionary compression, added a description that ZSTD_initCStream() will clear the dictionary, and noted that the ZSTD_estimate* function does not support external matchfinder API and multi-threading. (Architecture-related: public API documentation correction)
  ↳ [#3448](https://github.com/facebook/zstd/pull/3448): [3bfd3be](https://github.com/facebook/zstd/commit/3bfd3be5fb0d11813a57c10bf947224b998e696c)
- Clarified the documentation for dictionary loading, emphasizing that loading a new dictionary will clear the current dictionary (except in multi-dictionary mode), and updated the description of dictionary stickiness and reference behavior. (Architecture-related: public API: dictionary loading behavior)
  ↳ [#3381](https://github.com/facebook/zstd/pull/3381): [e4018c4](https://github.com/facebook/zstd/commit/e4018c4e7fa8dd90d65262a78ed9b54469e2a73b)
- Upgrade the version number to v1.5.4 and start preparing for release. (Architecture-related: version and compatibility)
  ↳ [#3469](https://github.com/facebook/zstd/pull/3469): [39ceef2](https://github.com/facebook/zstd/commit/39ceef27f92f09fa3131e89cff083c7623d0d0a1)
- The ZSTD_copyCCtx and ZSTD_copyDCtx functions have been marked as deprecated, and related documentation comments have been updated simultaneously. (Architecture-related: public API deprecated)
  ↳ [#3196](https://github.com/facebook/zstd/pull/3196): [962746e](https://github.com/facebook/zstd/commit/962746edffa5340315136af34ac3331eba82c3c8), [6b233d5](https://github.com/facebook/zstd/commit/6b233d5d41d65f00ff830abf846d2939f5812f56), [c450f9f](https://github.com/facebook/zstd/commit/c450f9f952d22033919c71a6279b55adeb343e8e)
- Introduced general deprecation macros and marked some functions. (Architecture-related: public API deprecation)
  ↳ [#3225](https://github.com/facebook/zstd/pull/3225): [0f4fd28](https://github.com/facebook/zstd/commit/0f4fd28a64880bdd1c14847983d5a7561950d8d5)
- Updated the version number to 1.5.3. (Architecture-related: version and compatibility)
  ↳ [#3179](https://github.com/facebook/zstd/pull/3179): [5c382bf](https://github.com/facebook/zstd/commit/5c382bf1104109de88dbde534ab7ba384773c1df)

### Application & Tool Layer
- Added --[no-]pass-through flag, and enabled pass-through mode for zstdcat, zcat, gzcat by default. (Architecture-related: CLI interface)
  ↳ [#3223](https://github.com/facebook/zstd/pull/3223): [03cc84f](https://github.com/facebook/zstd/commit/03cc84fddb9747ddc63f76b6f3171cd8f66da202) | [#3242](https://github.com/facebook/zstd/pull/3242): [3b4e470](https://github.com/facebook/zstd/commit/3b4e47092ea3e6c6d36b5e71d1f930ace4870e51)
- Fix the behavior of the --rm option in stdout and -o scenarios: silently ignore --rm when outputting to stdout, disable the --rm option on the -o command, and update the man page description. (Architecture-related: public API)
  ↳ [#3443](https://github.com/facebook/zstd/pull/3443): [cee6bec](https://github.com/facebook/zstd/commit/cee6bec9fa6aa249f2df9f84165b682eb793eab4), [b6fd91b](https://github.com/facebook/zstd/commit/b6fd91ba84633f1e077f98a2df69bab8b430600e) | [#3450](https://github.com/facebook/zstd/pull/3450): [8c85b29](https://github.com/facebook/zstd/commit/8c85b29e3236d0f0be00e59de004d7297c4fddf0)
- Improved behavior and error handling of benchmark mode, restricting running to zstd format only, returning non-zero error codes and more accurate error messages on failure. (Architecture-related: Benchmark behavior)
  ↳ [#3470](https://github.com/facebook/zstd/pull/3470): [af09777](https://github.com/facebook/zstd/commit/af09777b2488ec3af191e541ebe4fc220316ffa8) | [#3480](https://github.com/facebook/zstd/pull/3480): [9cabd15](https://github.com/facebook/zstd/commit/9cabd155fdf14b9ba8d240b42b2403e1da178a92), [58e7067](https://github.com/facebook/zstd/commit/58e7067c7d500537bfdccc5ee4707ac0154656d7), [6740f8f](https://github.com/facebook/zstd/commit/6740f8f0b8720ded3e8fa35f546115ac29c60e2e)
- Fixed small file asynchronous IO performance regression, dynamically enable or disable asynchronous IO based on file size. (Architecture-related: asynchronous IO behavior)
  ↳ [#3474](https://github.com/facebook/zstd/pull/3474): [79bdb8c](https://github.com/facebook/zstd/commit/79bdb8cbb6232370336c2da0d1cc7610b67bb35d)

### Cross-cutting / Other Architecture-related Changes
- Comprehensive reconstruction of Windows CI: upgrade to Visual Studio 2022, update msys2 configuration, and optimize the test matrix. (Architecture-related: platform compatibility)
  ↳ [#3410](https://github.com/facebook/zstd/pull/3410): [4f7183d](https://github.com/facebook/zstd/commit/4f7183d887789d4d2bb2e5af850c427f1df725ff) | [#3374](https://github.com/facebook/zstd/pull/3374): [3867c41](https://github.com/facebook/zstd/commit/3867c41552ee648bfe0cc63407ab39dc1d2adc1d)
- Added C89 build tests in CI, and fixed compilation warnings that are incompatible with C89 in the code. (Architecture-related: platform compatibility)
  ↳ [#3435](https://github.com/facebook/zstd/pull/3435): [ea684c3](https://github.com/facebook/zstd/commit/ea684c335ab54bafa967a290a92d66b3d8f80648)
- Change the backtrace option to feature type, and add detection of the execinfo.h header file so that it is only enabled when the header file exists. (Architecture-related: Build and platform compatibility)
  ↳ [#3276](https://github.com/facebook/zstd/pull/3276): [031de3c](https://github.com/facebook/zstd/commit/031de3c69ccbf3282ed02fb49369b476730aeca8)
- Added Meson build and test CI on Linux to GitHub Actions workflow. (Architecture-related: Build and platform compatibility)
  ↳ [#3120](https://github.com/facebook/zstd/pull/3120): [7f29c18](https://github.com/facebook/zstd/commit/7f29c1847d5b36908f13592c31fa178072b4db0f)
- Added Meson build and test CI tasks for Windows platform. (Architecture-related: Build and platform compatibility)
  ↳ [#3120](https://github.com/facebook/zstd/pull/3120): [937e9d3](https://github.com/facebook/zstd/commit/937e9d3b6257304e1533e9e6104ecff8e8dd5a30)
- Increase the Meson minimum version requirement from 0.48.0 to 0.50.0 to eliminate compilation warnings caused by using new features. (Architecture-related: Build requirements)
  ↳ [#3368](https://github.com/facebook/zstd/pull/3368): [626425d](https://github.com/facebook/zstd/commit/626425dce0bfda5be67b96b61d09b11173c5e436)
- Added Cygwin test task. (Architecture-related: platform compatibility)
  ↳ [#3431](https://github.com/facebook/zstd/pull/3431): [cd272d7](https://github.com/facebook/zstd/commit/cd272d7a2d832aec3c4332b32eeeffe29916fbfc)

## Routine Changes

### New features
- Added --fake-stdin-is-console, --fake-stdout-is-console and --fake-stderr-is-console command line options for simulating the console in tests.
  ↳ [#2984](https://github.com/facebook/zstd/pull/2984): [e58a39f](https://github.com/facebook/zstd/commit/e58a39f84e988e4229067372b4f30601dcfc484b)
- Added version information of zlib, lz4, lzma libraries to be displayed in the detailed version output.
  ↳ [#3030](https://github.com/facebook/zstd/pull/3030): [e60eba5](https://github.com/facebook/zstd/commit/e60eba58bf83979e92de487a87c0829a7bd60f92)
- Implemented more gzip compatibility: implemented --best as an alias for -9 and -n/--no-name as a no-op.
  ↳ [#3059](https://github.com/facebook/zstd/pull/3059): [e653e97](https://github.com/facebook/zstd/commit/e653e97f77e7e53867e39ed6ce11dbbde6617337)
- Support advanced API to make forceCopy/forceAttach function work properly.
  ↳ [#3161](https://github.com/facebook/zstd/pull/3161): [f7ebbcd](https://github.com/facebook/zstd/commit/f7ebbcd0cc090d8012c906a009521558f70245a7)
- When using C90 clock_t for multi-thread speed measurement, a warning message is displayed, indicating that the measurement results may be inaccurate in this mode.
  ↳ [#3166](https://github.com/facebook/zstd/pull/3166): [574ecbb](https://github.com/facebook/zstd/commit/574ecbb0fcbddd1937d104d199247052042d9a16)
- Added the ability to display dictionary IDs in the zstd -lv command. When a file contains multiple frames with different dictionary IDs, a warning will be displayed and the dictionary ID will be set to 0.
  ↳ [#3184](https://github.com/facebook/zstd/pull/3184): [cc8c984](https://github.com/facebook/zstd/commit/cc8c98485a7c1f9837e13662649711dc842f2c02), [d7eb829](https://github.com/facebook/zstd/commit/d7eb829af5428f62b9308917232207d0dc92292c)
- When using the -v -l option in the command line tool to list single-frame file information, the specific value of the checksum will now be output.
  ↳ [#3332](https://github.com/facebook/zstd/pull/3332): [dc39409](https://github.com/facebook/zstd/commit/dc39409a03079b0f55979dd72e892069c474425a)
- During compression and decompression operations, copy the source file's permissions, ownership and timestamps to the output file, and create the output file with temporary restricted permissions instead.
  ↳ [#3432](https://github.com/facebook/zstd/pull/3432): [1e3eba6](https://github.com/facebook/zstd/commit/1e3eba65a647dbd35739f82b9afc2021af7542f3), [5653f96](https://github.com/facebook/zstd/commit/5653f96776640421783af3fe379741a1a2486706)
- Fixed largeNbDicts benchmark crash, and added --dict-content-type, --dict-attach-pref and --prefetch-cdict-tables command line options.
  ↳ [#3063](https://github.com/facebook/zstd/pull/3063): [762898f](https://github.com/facebook/zstd/commit/762898f5e4424a72bdbb3d3847abd598c8be1846)
- When decompression and multi-threading parameters are specified at the same time, a warning message is printed, indicating that multi-thread decompression is not supported.
  ↳ [#3208](https://github.com/facebook/zstd/pull/3208): [d4a5bc4](https://github.com/facebook/zstd/commit/d4a5bc4efc40e090bf55a1a9221b6ab26b17b302)

### bug fixes
- Fixed the problem of incorrectly waiting for standard input when processing an empty directory in recursive mode, instead printing a warning and exiting normally.
  ↳ [#3027](https://github.com/facebook/zstd/pull/3027): [4021b78](https://github.com/facebook/zstd/commit/4021b784376c3790c077e9b8deedbb6a4f016687), [beb4872](https://github.com/facebook/zstd/commit/beb48722411b53f36387c5c88ba9a9c7671c5c12)
- Fixed the issue where the DiB_shuffle function triggers an assertion when the input quantity is 0 and returns directly instead.
  ↳ [#3020](https://github.com/facebook/zstd/pull/3020): [246982e](https://github.com/facebook/zstd/commit/246982e782849d8646b2d5df6648319935669228)
- Removed the new Huffman depth heuristic algorithm to make the compression results consistent with those before PR, and adjusted the function declaration format.
  ↳ [#3019](https://github.com/facebook/zstd/pull/3019): [8b46895](https://github.com/facebook/zstd/commit/8b46895588c6a199d6fa674752b51dd547f0addf)
- Changed to use the more accurate error code stabilityCondition_notRespected in the stability buffer check, and updated the relevant test cases simultaneously.
  ↳ [#2974](https://github.com/facebook/zstd/pull/2974): [f2d9652](https://github.com/facebook/zstd/commit/f2d9652ad82c5ead0665bea428215eaf027de933)
- Removed an incorrect assertion that could trigger when the block splitter cuts a block at the start of repcode, resulting in invalid offsets, but subsequent logic handles it correctly.
  ↳ [#3033](https://github.com/facebook/zstd/pull/3033): [8df1257](https://github.com/facebook/zstd/commit/8df1257c3cd70341307b87bffccbb334a10db5a1)
- Fix insufficient compression bounds when using Explicit Block Delimiters, allocate larger buffers for this mode in fuzz tests.
  ↳ [#3036](https://github.com/facebook/zstd/pull/3036): [637b2d7](https://github.com/facebook/zstd/commit/637b2d7a24faf32b3cd465b6d46d890ed1e8ff6d) | [#3034](https://github.com/facebook/zstd/pull/3034): [d64d5dd](https://github.com/facebook/zstd/commit/d64d5ddc57ac58f3bcff2bd531cbe1e71bc4e356) | [#3103](https://github.com/facebook/zstd/pull/3103): [678bfff](https://github.com/facebook/zstd/commit/678bfff4fed62b8d1076f7388343338acef2b4c4)
- Fixed the problem of inaccurate decompression memory requirements reported when -vv is used with --long, and the default value is used when the window size is not specified in long mode.
  ↳ [#3042](https://github.com/facebook/zstd/pull/3042): [470eb83](https://github.com/facebook/zstd/commit/470eb8330a9821c334df7efe66945a63d1faf017)
- Fixed and clarified repcode offset history logic in compressed blocks, corrected offset saving and rotation logic and validity check conditions.
  ↳ [#3127](https://github.com/facebook/zstd/pull/3127): [97aabc4](https://github.com/facebook/zstd/commit/97aabc496e57821cb46893bd0a73f48ff6bc20b7), [3620a0a](https://github.com/facebook/zstd/commit/3620a0a56589c952d248dfccdc96a86b948e9432) | [#3114](https://github.com/facebook/zstd/pull/3114): [2820efe](https://github.com/facebook/zstd/commit/2820efe7ec931906ce052771afc04ddd12a8cfa8)
- Added input non-zero check in bit manipulation functions on Win32 platform to avoid static analysis warnings.
  ↳ [#3045](https://github.com/facebook/zstd/pull/3045): [00f2acb](https://github.com/facebook/zstd/commit/00f2acba36bfe882e8e64a0115d6da31922bab91)
- Fixed an issue where the dictionary trainer got stuck in an infinite loop when processing empty input files.
  ↳ [#3081](https://github.com/facebook/zstd/pull/3081): [da737c7](https://github.com/facebook/zstd/commit/da737c7ab89f61f1ea7c392299137f6ffe6f9733)
- Hardcode repcode security checks in extDict fast compression path, and fix coding style issues.
  ↳ [#3114](https://github.com/facebook/zstd/pull/3114): [518cb83](https://github.com/facebook/zstd/commit/518cb83833074d304dfcaa93cfc16039ea4683c8), [6a2e1f7](https://github.com/facebook/zstd/commit/6a2e1f7c69f32427afc2f0273d3f4fe923a98a94)
- Fixed zstreamtest segfault in MALLOC_PERTURB_ environment and changed thread pool memory allocation from malloc to calloc.
  ↳ [#3288](https://github.com/facebook/zstd/pull/3288): [b7d55cf](https://github.com/facebook/zstd/commit/b7d55cfa0d0942c2cb74d47076847c401653f9ed)
- Fixed the Windows platform thread handle leak problem, explicitly close the handle after waiting for the thread to end.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [95073b1](https://github.com/facebook/zstd/commit/95073b1af1c15a9c3a5344d2e98ff27f41c1d872)
- Fix the evaluation order of loop conditions in ZSTD_copySequencesToSeqStoreExplicitBlockDelim to avoid accessing sequence data even after the index is out of bounds.
  ↳ [#3148](https://github.com/facebook/zstd/pull/3148): [5081ccb](https://github.com/facebook/zstd/commit/5081ccb05620bdec6e07464213f871bc0381a63f)
- Fixed the boundary condition of window overflow correction when loading a large dictionary to avoid triggering assertion failure.
  ↳ [#3157](https://github.com/facebook/zstd/pull/3157): [31bd640](https://github.com/facebook/zstd/commit/31bd6402c63a33e81513de6511c6447c63456625)
- Fix segfault caused by createCompressInstructions being called when doing decompression-only benchmarks.
  ↳ [#3205](https://github.com/facebook/zstd/pull/3205): [d0c88af](https://github.com/facebook/zstd/commit/d0c88afe6d5c0a29274df735a044154c6bf6deaa)
- Fixed buffer underflow when the directory parameter is empty and optimized memory allocation failure error handling.
  ↳ [#3220](https://github.com/facebook/zstd/pull/3220): [e1873ad](https://github.com/facebook/zstd/commit/e1873ad576cb478fff0e6e44ad99599cd5fd2846)
- Disable empty strings as arguments to --output-dir-flat and --output-dir-mirror.
  ↳ [#3220](https://github.com/facebook/zstd/pull/3220): [f9f27de](https://github.com/facebook/zstd/commit/f9f27de91c89d826c6a39c3ef44fb1b02f9a43aa)
- Fixed the problem that short files cannot be output directly through passthrough mode.
  ↳ [#3215](https://github.com/facebook/zstd/pull/3215): [2b9fde9](https://github.com/facebook/zstd/commit/2b9fde932b53502ca6fb59d9a9d7ca781ffeae55)
- Fix bug when handling standard input as one of multiple files.
  ↳ [#3222](https://github.com/facebook/zstd/pull/3222): [ae46704](https://github.com/facebook/zstd/commit/ae4670466c5db56493f356c1a81e8cbefef3271e)
- Fixed off-by-one bug of long literals and match length in superblock mode, and added golden compression test.
  ↳ [#3221](https://github.com/facebook/zstd/pull/3221): [a70ca2b](https://github.com/facebook/zstd/commit/a70ca2bd7dbc74d3c9db173e3682532e18565246)
- Fixed the issue where windowLog was not correctly set to the default value when the --long parameter was not set.
  ↳ [#3226](https://github.com/facebook/zstd/pull/3226): [d0dcc9d](https://github.com/facebook/zstd/commit/d0dcc9d775789af73f44accb318579465ccdada4)
- Fixed multiple null pointers and undefined behavior issues in ZSTD_decompressStream function.
  ↳ [#3258](https://github.com/facebook/zstd/pull/3258): [0288427](https://github.com/facebook/zstd/commit/028842788beb134490d8d09ee931603433c5d62f), [f3ddaad](https://github.com/facebook/zstd/commit/f3ddaaddd610c574e5e46ce183cd70fd70ba3278), [3d7f9a9](https://github.com/facebook/zstd/commit/3d7f9a90dff02561558f99f074c22cdba9ee4dd9) | [#3263](https://github.com/facebook/zstd/pull/3263): [a1d8942](https://github.com/facebook/zstd/commit/a1d89424c2f4755ed2f62f7fc707d24845cb8139), [e46b12e](https://github.com/facebook/zstd/commit/e46b12e1b46554ddf8711c5c60ae3aa461c214aa)
- Fixed the problem of numeric parameters in zstd CLI accepting illegal values. Now only numbers and optional suffixes are allowed, and numeric format verification has been enhanced.
  ↳ [#3268](https://github.com/facebook/zstd/pull/3268): [3587877](https://github.com/facebook/zstd/commit/358787764f140d035b56863a9e2c20a3c5f0f7d9)
- Fixed bounds error in buffer overflow check in UTIL_mergeFileNamesTable function, corrected assertion condition from <= to <.
  ↳ [#3300](https://github.com/facebook/zstd/pull/3300): [361d869](https://github.com/facebook/zstd/commit/361d86998ad877a678c5ffead30ecaf0c815c9aa)
- Fixed an off-by-one bug that could trigger data corruption when windowLog=25 in 32-bit mode.
  ↳ [#3361](https://github.com/facebook/zstd/pull/3361): [a91e7ec](https://github.com/facebook/zstd/commit/a91e7ec175d4f73b54a2d7ebf22d86d262ffb01d)
- Now supports decompression of compressed blocks with a size of exactly ZSTD_BLOCKSIZE_MAX, relaxing the compression block size check conditions.
  ↳ [#3399](https://github.com/facebook/zstd/pull/3399): [ea2895c](https://github.com/facebook/zstd/commit/ea2895cef46d5850b00a9fde57e4e250df680bd3)
- Fixed error messages and support for updating compression parameters and signaling changes during multi-threaded compression.
  ↳ [#3403](https://github.com/facebook/zstd/pull/3403): [b17743e](https://github.com/facebook/zstd/commit/b17743e41b4aae01991285d4958b1b727a516008)
- Fixed window resizing edge case: when the input size is equal to the maximum window size, the window is now also resized correctly to save memory.
  ↳ [#3345](https://github.com/facebook/zstd/pull/3345): [69ec75f](https://github.com/facebook/zstd/commit/69ec75f0d5e028aa34b3b51f990f38a18a0b7783)
- Fixed missing brackets in macro definition and corrected BIT_highbit32 call to ZSTD_highbit32.
  ↳ [#3365](https://github.com/facebook/zstd/pull/3365): [ee6475c](https://github.com/facebook/zstd/commit/ee6475cbbd04408e721c4daa87d993faf3b3c1cf)
- Fixed an issue where parameters in macro definitions were not bracketed, and fixed an incorrect assertion in the ZSTD_fracWeight function.
  ↳ [#3248](https://github.com/facebook/zstd/pull/3248): [d07e72b](https://github.com/facebook/zstd/commit/d07e72bb13f6baab0ba33929c332699b78ca9955)
- Fixed type conversion warning, changed ZSTD_fCost function parameter type from U32 to int, and adjusted related assertions.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [71dbe8f](https://github.com/facebook/zstd/commit/71dbe8f9d40ee16c3bbefe52ccfae410ccfda934)
- Fixed parsing problem of maxBlockSize parameter in estimation function.
  ↳ [#3418](https://github.com/facebook/zstd/pull/3418): [8353a4b](https://github.com/facebook/zstd/commit/8353a4b095ca71dcf64a1507952001c8fa34cbee)
- Adjusted the order of setting file permissions, setting group permissions first and then setting user permissions to eliminate race conditions.
  ↳ [#3432](https://github.com/facebook/zstd/pull/3432): [0d2d460](https://github.com/facebook/zstd/commit/0d2d46022336b267e87d6bfb078ccc34d0ca8aad)
- Fixed bounds check on sequence index in ZSTD_copySequencesToSeqStoreNoBlockDelim, only incrementing index when non-final split sequence.
  ↳ [#3447](https://github.com/facebook/zstd/pull/3447): [7d600c6](https://github.com/facebook/zstd/commit/7d600c628afcc59dd9768c28ffcd56b48a919f05)
- Fixed the bug of redzone depoisoning. Now only the expected buffer is depoisoned, and subsequent redzone depoisoning is no longer detoxified.
  ↳ [#3451](https://github.com/facebook/zstd/pull/3451): [1d636b4](https://github.com/facebook/zstd/commit/1d636b4ba0bd105eaf7c2427aa6b4b147bdd3035)
- In scenarios where the input file should not be deleted, change the assertion to a hard failure and directly exit with an error to protect user data.
  ↳ [#3450](https://github.com/facebook/zstd/pull/3450): [02434e0](https://github.com/facebook/zstd/commit/02434e0867695db62ade7a94852dfeae1b630e75)
- Fixed a bug where the --row-match-finder and --no-row-match-finder command line options behaved reversely, now the options correctly enable or disable the row match finder.
  ↳ [#3457](https://github.com/facebook/zstd/pull/3457): [6422d1d](https://github.com/facebook/zstd/commit/6422d1d7a85182e983b361a20bbe2064611680fc)
- When standard error output is not the console, only progress updates are disabled, warnings and final action summaries are preserved.
  ↳ [#3458](https://github.com/facebook/zstd/pull/3458): [82ca008](https://github.com/facebook/zstd/commit/82ca00811aa297c1f00f549facc70787fdb59d64)
- Fixed the bug of input boundary checking in the fast C decoder, and changed the break of the inner loop to goto _out to correctly jump out of the outer loop.
  ↳ [#3459](https://github.com/facebook/zstd/pull/3459): [bda947e](https://github.com/facebook/zstd/commit/bda947e17a61b9f7434ea878dff04a409a2ff772)
- Fixed the incorrect return value of ZSTD_getOffsetInfo() when nbSeq is 0 because the offset table is not initialized.
  ↳ [#3473](https://github.com/facebook/zstd/pull/3473): [71a0259](https://github.com/facebook/zstd/commit/71a0259247829546cd639e379a8c47384ed96a26)
- Fixed datagen still printing extra newlines when there is no other output.
  ↳ [#3020](https://github.com/facebook/zstd/pull/3020): [f088c43](https://github.com/facebook/zstd/commit/f088c430e35d8b97d11aa38c5c78a72931ec7bad)
- Fixed an issue in readLinesFromFile where the assertion condition was too strict when the file did not end with a newline character.
  ↳ [#3084](https://github.com/facebook/zstd/pull/3084): [d109cef](https://github.com/facebook/zstd/commit/d109cef2012b1e0ca7a6f47278a2838f68bbc196)
- Fixed memory estimation error and added the ability to output benchmark results to a CSV file.
  ↳ [#3161](https://github.com/facebook/zstd/pull/3161): [e0c4863](https://github.com/facebook/zstd/commit/e0c4863c5c81c7aecdb7e1560e081346747a495b)
- Fix file handle leak problem in largeNbDicts.
  ↳ [#3161](https://github.com/facebook/zstd/pull/3161): [2bbdc9f](https://github.com/facebook/zstd/commit/2bbdc9f40e6663311028dec241cdc6ab3b5c7e33)
- Fix segfault when decompressing in largeNbDicts.
  ↳ [#3209](https://github.com/facebook/zstd/pull/3209): [6255f99](https://github.com/facebook/zstd/commit/6255f994d35219b60d3df21535c72675d5d6a98f)
- Fix C90 compatibility issue, explicitly initialize all fields of ZSTD_frameHeader in ZSTD_getDictID_fromFrame.
  ↳ [#3349](https://github.com/facebook/zstd/pull/3349): [c43da3d](https://github.com/facebook/zstd/commit/c43da3d6059a277ab5d76236bdb66ba2b36264a1)
- Fixed an invalid assertion in 32-bit decoding, which is now only enabled in fuzz mode.
  ↳ [#3461](https://github.com/facebook/zstd/pull/3461): [b3b43f2](https://github.com/facebook/zstd/commit/b3b43f2893fa03da3b8004b449a7ec590f0e1e5b)
- Fixed CI bug, moved variable declaration from inside for loop to outside to be compatible with C90 standard.
  ↳ [#3302](https://github.com/facebook/zstd/pull/3302): [c26f348](https://github.com/facebook/zstd/commit/c26f348dc810ae536a63f088b380b5e6b341b45a)
- Fixed -Wdocumentation and -Wconversion warnings when making clangbuild, and made explicit type conversion.
  ↳ [#3393](https://github.com/facebook/zstd/pull/3393): [40a7188](https://github.com/facebook/zstd/commit/40a718813070e23c3c7a437477a9e984d4de3f8b)

### Refactoring optimization
- Adjusted the threshold of the optimal Huffman table depth so that the optimal table depth can be automatically selected under high compression levels.
  ↳ [#3285](https://github.com/facebook/zstd/pull/3285): [fa7d9c1](https://github.com/facebook/zstd/commit/fa7d9c11394aa4951610669a64397ca6a5950ce5), [c4853e1](https://github.com/facebook/zstd/commit/c4853e1553b9582e5c230b8b2621fc6983814cec)
- Removed the srcSize parameter in the HUF_minTableLog function and moved related assertions to the caller, simplifying function implementation.
  ↳ [#3285](https://github.com/facebook/zstd/pull/3285): [a910489](https://github.com/facebook/zstd/commit/a910489ff52a7238de99327eed498e3c3f4a6e6b), [b347290](https://github.com/facebook/zstd/commit/b34729018cd4a38d8e3efdc604d30ec9c3081f24)
- Refactored UTIL_getSpanTimeMicro into a generic implementation based on UTIL_getSpanTimeNano, removing platform-specific duplicate code.
  ↳ [#3413](https://github.com/facebook/zstd/pull/3413): [8b13000](https://github.com/facebook/zstd/commit/8b130009e3246098acbf659e8622034bd9e20efd)
- Modified the FIO_openSrcFile function to return file status information through parameters, reducing the number of stat() calls.
  ↳ [#3432](https://github.com/facebook/zstd/pull/3432): [2ad6855](https://github.com/facebook/zstd/commit/2ad6855ac1b90516b1670684bb20126f7b17ef4b), [a5ed28f](https://github.com/facebook/zstd/commit/a5ed28f1fb35bfd29053d5bc4d5ec7c8c1d25b83)
- Internally refactored the streaming compression and literal compression modules, and added debug logs.
  ↳ [#2974](https://github.com/facebook/zstd/pull/2974): [5684bae](https://github.com/facebook/zstd/commit/5684bae4f666f2730f2121048b0aa8472ac30457) | [#3019](https://github.com/facebook/zstd/pull/3019): [7616e39](https://github.com/facebook/zstd/commit/7616e39f3b5618a20d2c8d059f1369283838cbce), [e9dd923](https://github.com/facebook/zstd/commit/e9dd923fa4b87db64ff6c3681194967d5eaaa264)
- Reconstructed the chunk splitting logic, simplified the ZSTD_deriveSeqStoreChunk function and adjusted the debug log level.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [9a68840](https://github.com/facebook/zstd/commit/9a68840176ec9334060b2379f204ada59408bfd1)
- Added bounds assertion checks in Huffman table log calculations.
  ↳ [#3047](https://github.com/facebook/zstd/pull/3047): [b9566fc](https://github.com/facebook/zstd/commit/b9566fc558830de2a3fd486961b674774c17b74e)
- Removed hasStep variant to reduce code size.
  ↳ [#3114](https://github.com/facebook/zstd/pull/3114): [ac371be](https://github.com/facebook/zstd/commit/ac371be27b443e488de824a7a0e365fd6d4ac536)
- Advance hash table write operations into each branch found for matching, and optimize the recovery logic for invalid offsets.
  ↳ [#3129](https://github.com/facebook/zstd/pull/3129): [cd1f582](https://github.com/facebook/zstd/commit/cd1f5829432c6df1a47c26cf9be75495fb2fdb94)
- Extracted the NEON version's matching mask logic into a separate function, and fixed the indentation format of related code.
  ↳ [#3139](https://github.com/facebook/zstd/pull/3139): [6b561d2](https://github.com/facebook/zstd/commit/6b561d230fd71de732346838752051c349c52f2e)
- Improved the validation logic of long-distance matching parameters, extended the parameter range to a three-state enumeration and added bounds checking.
  ↳ [#3321](https://github.com/facebook/zstd/pull/3321): [c8d870f](https://github.com/facebook/zstd/commit/c8d870fe52b043828f1f59b8976b4d7c55865289)
- Maintenance improvements such as code formatting, const correctness, adding assertions and comments, etc. to the block splitter.
  ↳ [#3376](https://github.com/facebook/zstd/pull/3376): [832c1a6](https://github.com/facebook/zstd/commit/832c1a6a1c4dfea4c5dd78074226e656b2cd3d56)
- Migrate long offset flag from seqStore structure to ZSTD_symbolEncodingTypeStats_t.
  ↳ [#3460](https://github.com/facebook/zstd/pull/3460): [9e4c66b](https://github.com/facebook/zstd/commit/9e4c66b9e92df871c8e0da61c1796d402874fed6)
- Fixed the lint problem where parameters in macro definitions are not bracketed.
  ↳ [#3016](https://github.com/facebook/zstd/pull/3016): [f936dd8](https://github.com/facebook/zstd/commit/f936dd89cb6fcf5dd2b03db0ca93dc76181838a9)
- Changed several helper functions in common.h from static to using the HEADER_FUNCTION macro.
  ↳ [#3235](https://github.com/facebook/zstd/pull/3235): [3f7a1b1](https://github.com/facebook/zstd/commit/3f7a1b13285aa3bcd5b733dd804dbc81a45fa77d)

### Test related
- Added CLI test platform, including test framework and documentation.
  ↳ [#3020](https://github.com/facebook/zstd/pull/3020): [f3096ff](https://github.com/facebook/zstd/commit/f3096ff6d1fcf87eeec876da13c06a97343ed6cf)
- Add debug tracing in regression testing, and optimize log calculation of Huffman coding.
  ↳ [#3019](https://github.com/facebook/zstd/pull/3019): [4684836](https://github.com/facebook/zstd/commit/4684836f4fbaea1d5416306173306bac56361d83)
- Added test cases starting from a non-zero starting position in the streaming compression test.
  ↳ [#2974](https://github.com/facebook/zstd/pull/2974): [af3d9c5](https://github.com/facebook/zstd/commit/af3d9c506e5bbfdbf78ce35fe62501c4ae0e19a7)
- Add unit tests for bitwise operation built-in functions.
  ↳ [#3045](https://github.com/facebook/zstd/pull/3045): [7c674a0](https://github.com/facebook/zstd/commit/7c674a09199f1c47b88116e67f0d749ce8373a1f)
- Remove unused variables in test files and adjust loop logic to solve CI issues.
  ↳ [#3272](https://github.com/facebook/zstd/pull/3272): [21bd8c3](https://github.com/facebook/zstd/commit/21bd8c3b3c844ce18281de4f2975d66da330aee0)
- Fixed the compatibility issue of fuzz testing when multi-threading is not available.
  ↳ [#3291](https://github.com/facebook/zstd/pull/3291): [1d153c9](https://github.com/facebook/zstd/commit/1d153c923c158c245812618e047d762ec4a6a6f9) | [#3417](https://github.com/facebook/zstd/pull/3417): [3ac0b91](https://github.com/facebook/zstd/commit/3ac0b913024af5b9adea8e626bd62f951080498e)
- Fix the range of long-distance matching parameter settings in fuzzer tests to make it comply with the new enumeration value range.
  ↳ [#3321](https://github.com/facebook/zstd/pull/3321): [3720910](https://github.com/facebook/zstd/commit/3720910d060a42f53f72252ecc188c9f9b33740e)
- Migrate boolean LDM flags in test code to ZSTD_paramSwitch_e enumeration values.
  ↳ [#3321](https://github.com/facebook/zstd/pull/3321): [bb3c01c](https://github.com/facebook/zstd/commit/bb3c01c8539ecc85f0884dd709767de915fb0d72)
- Fixed the problem of memory not being released when compressing empty strings in test cases, and adjusted the buffer size.
  ↳ [#3346](https://github.com/facebook/zstd/pull/3346): [aece0f2](https://github.com/facebook/zstd/commit/aece0f258adfbd72401707d39094a477106af07a)
- Fixed the issue where memset() is omitted in stack detection due to optimization of the new version of GCC.
  ↳ [#3348](https://github.com/facebook/zstd/pull/3348): [e767d5c](https://github.com/facebook/zstd/commit/e767d5c7c144ab911842229a9a8fee527d9616e9)
- Extract parameter value generation logic into independent functions to improve the reproducibility of fuzz testing inputs.
  ↳ [#3417](https://github.com/facebook/zstd/pull/3417): [ca2ff78](https://github.com/facebook/zstd/commit/ca2ff788df535bc339338b5ec4b198335a264490)
- Adjust the condition value of external matcher registration in fuzz testing to adjust the test trigger probability.
  ↳ [#3437](https://github.com/facebook/zstd/pull/3437): [f593e54](https://github.com/facebook/zstd/commit/f593e54ee18dcceb2c0d4529e1edfe4e6ea823eb)
- In sequence compression fuzz testing, change the dictionary generation method from random buffer to calloc allocation, and remove related file I/O logic.
  ↳ [#3447](https://github.com/facebook/zstd/pull/3447): [7fc00c1](https://github.com/facebook/zstd/commit/7fc00c18b8e7fc8644f46f5bc16587f5b7861cff)
- Initialize long offset fields in the test harness decodecorpus to support correct parsing of long offsets.
  ↳ [#3460](https://github.com/facebook/zstd/pull/3460): [d210628](https://github.com/facebook/zstd/commit/d210628b0b01d4447de2b9e4404d2bf557b40217)
- Adjust how big tests are executed: add --big-tests option and remove conditions to make tests always run.
  ↳ [#3460](https://github.com/facebook/zstd/pull/3460): [da589a1](https://github.com/facebook/zstd/commit/da589a134a40a19103458a6ccb8ada7bb09eea5d), [66fae56](https://github.com/facebook/zstd/commit/66fae56c860fdbf195a45c2b2372692460f07fa7)

### Performance optimization
- In the optimal parsing stage, each literal is forced to cost at least 1 bit to be consistent with the subsequent Huffman compression stage and slightly improve the compression ratio.
  ↳ [#2983](https://github.com/facebook/zstd/pull/2983): [ca0135c](https://github.com/facebook/zstd/commit/ca0135c2fd562058a099a20bb0c2e569d354f08b)
- Enable 1MB buffer mode for output files to improve performance, and optimize the error prompt level for file name conflict detection.
  ↳ [#2985](https://github.com/facebook/zstd/pull/2985): [df5013b](https://github.com/facebook/zstd/commit/df5013b4632eda82a0cc745969ca305ac55dfe36)
- Improved the heuristic algorithm for Huffman tree depth selection to avoid over-adjustment in certain boundary cases, thus improving the compression ratio.
  ↳ [#3019](https://github.com/facebook/zstd/pull/3019): [51da2d2](https://github.com/facebook/zstd/commit/51da2d2ff245be6bcd719ee1f3d4c23225d4e653)
- Changed the threshold for automatic tree depth adjustment from maximum to default to improve compression ratio in certain situations.
  ↳ [#3019](https://github.com/facebook/zstd/pull/3019): [5db717a](https://github.com/facebook/zstd/commit/5db717af10bebadcc08fe13abe00ddba24b83b3d)
- Introduce software pipeline optimization to the ZSTD_compressBlock_fast_dictMatchState function to improve compression speed through dual pointers and prefetching technology.
  ↳ [#3086](https://github.com/facebook/zstd/pull/3086): [64efba4](https://github.com/facebook/zstd/commit/64efba4c5ee1e8c9afe92873f79424c9955b82ba)
- Migrate the noDict pipeline into the ZSTD_compressBlock_fast_extDict function to improve performance with dictionary compression.
  ↳ [#3114](https://github.com/facebook/zstd/pull/3114): [3536262](https://github.com/facebook/zstd/commit/3536262f70abddae45f45455d3735d29282100f6)
- Optimize the repcode predicate, hardcode the hasStep == 0 scenario, and fix several code appearance issues.
  ↳ [#3114](https://github.com/facebook/zstd/pull/3114): [809f652](https://github.com/facebook/zstd/commit/809f65291266de966ba4262220992f5f7e7903a0)
- Optimize the security check of hash table writing in fast compression mode to avoid unnecessary checks in partial matching paths, thereby increasing the compression speed by about 0.5%.
  ↳ [#3129](https://github.com/facebook/zstd/pull/3129): [040986a](https://github.com/facebook/zstd/commit/040986a4f4a2ba64a3ad9dc76646d8fab4472b37)
- Optimized the movemask simulation of ZSTD_row_getMatchMask on ARM, improving the performance of compression levels 8-10 through grouped bit operations. Levels 8-9 are improved by 3-5%, and level 10 is improved by 1.5%.
  ↳ [#3139](https://github.com/facebook/zstd/pull/3139): [e11783b](https://github.com/facebook/zstd/commit/e11783b04d1c49678bb4f95a4ecaa26323bd823d)
- Optimize the loading method of the ZSTD_seqSymbol structure in the ZSTD_decodeSequence function on the aarch64 architecture, and avoid GCC from generating redundant loading instructions through a memory copy, thereby improving decoding performance.
  ↳ [#3141](https://github.com/facebook/zstd/pull/3141): [2491c65](https://github.com/facebook/zstd/commit/2491c65937d42561ef9238422929213751adcc10)
- Removed expensive assertions in --rsyncable hot loops to improve performance, and added equivalent assertions at the beginning and end of the loop to maintain coverage.
  ↳ [#3154](https://github.com/facebook/zstd/pull/3154): [7c05b9a](https://github.com/facebook/zstd/commit/7c05b9aec3e18bf733cccff6dda97ea269bb8594)
- Introduced short cache optimization for dictionary matching state (DMS) at level 1-4, which avoids unnecessary dictionary memory loading by packing tags in hash table entries, thereby increasing compression speed by 5-30%.
  ↳ [#3152](https://github.com/facebook/zstd/pull/3152): [f6ef143](https://github.com/facebook/zstd/commit/f6ef14329f396eb8b2c1290790e7547d070d9511)
- In dictionary-less mode, change the match check from single-byte comparison to 4-byte comparison to reduce the number of calls to ZSTD_count.
  ↳ [#3199](https://github.com/facebook/zstd/pull/3199): [ce52acd](https://github.com/facebook/zstd/commit/ce52acd7dc7a7afc83433f0f2212942eb3160abb)
- Optimize the HUF_optimalTableLog function to improve the speed of Huffman depth selection by adjusting the search strategy and introducing early termination conditions.
  ↳ [#3302](https://github.com/facebook/zstd/pull/3302): [a08fabd](https://github.com/facebook/zstd/commit/a08fabd51a4191b9b1a2d580454ae6b7b805ee35)
- Change the search function selection in lazy compression from indirect function calls to switch statements to improve performance.
  ↳ [#3295](https://github.com/facebook/zstd/pull/3295): [dcc7228](https://github.com/facebook/zstd/commit/dcc7228de92a6a2aa505f12cbf9e929e0879d44d)
- Optimize the search strategy of Huffman table depth in the HUF_optimalTableLog function, adjust the minimum table depth calculation and add comments.
  ↳ [#3302](https://github.com/facebook/zstd/pull/3302): [4013319](https://github.com/facebook/zstd/commit/401331909e85a5590d03786130187545fe1e12df)
- Remove the virtual function table of the search function to improve performance, optimize Huffman depth selection, adjust macro definition and memory allocation.
  ↳ [#3302](https://github.com/facebook/zstd/pull/3302): [db74d04](https://github.com/facebook/zstd/commit/db74d043d6de8268d7c23c8781c26ecef60a86b7)
- Adjust the optimal Huffman depth selection threshold from ZSTD_btultra to 3, affecting the balance between performance and compression ratio.
  ↳ [#3302](https://github.com/facebook/zstd/pull/3302): [c263821](https://github.com/facebook/zstd/commit/c2638212af253e8d9c9161743812b5e39056e0f5)
- Optimize the Huffman table depth search algorithm (one-way scan, early interruption), and fix the boundary check error and realloc null pointer handling in the file list merging function.
  ↳ [#3302](https://github.com/facebook/zstd/pull/3302): [482689b](https://github.com/facebook/zstd/commit/482689b995bd6afb4a7b335bb80b9e60f501e3c2)
- Optimize the compression rate in small alphabet scenarios, and fix the problem of inaccurate initial literal cost evaluation resulting in low compression efficiency for small files.
  ↳ [#3391](https://github.com/facebook/zstd/pull/3391): [5434de0](https://github.com/facebook/zstd/commit/5434de01e21672cdd3ac111a99a969d8c5079297)
- Perform speed optimization on Huffman's optimal table depth selection algorithm, adjust initial values, early termination conditions and update logic.
  ↳ [#3302](https://github.com/facebook/zstd/pull/3302): [df714dd](https://github.com/facebook/zstd/commit/df714ddb0f2dc076dc841d10c8b72f66ef5af937)
- Optimize the HUF_optimalTableLog function, using FSE to cheaply evaluate and adjust the optimal depth search logic in advance in small alphabet scenarios.
  ↳ [#3391](https://github.com/facebook/zstd/pull/3391): [ebba9ff](https://github.com/facebook/zstd/commit/ebba9ff4259d874030cce14c6a34e988e5679a50)
- Reuse existing stat_t structures in file operations, reduce the number of stat() calls, and add debug tracing and output buffer optimization.
  ↳ [#3432](https://github.com/facebook/zstd/pull/3432): [0382076](https://github.com/facebook/zstd/commit/0382076af716e78f86a764475eece59a8eeb6272)
- Add branch prediction hints on low-probability paths to help the compiler generate more efficient pipeline code.
  ↳ [#3138](https://github.com/facebook/zstd/pull/3138): [ec5fdcd](https://github.com/facebook/zstd/commit/ec5fdcde198b4653ef94bbdf4cbadd1656cbcbcb)
- Added a CSV output field and -p option to the largeNbDicts benchmark tool, which supports selecting the output speed type and adding corresponding indicator columns.
  ↳ [#3205](https://github.com/facebook/zstd/pull/3205): [b550f9b](https://github.com/facebook/zstd/commit/b550f9b77e9fa11d11078735c32ba9847e5df773), [d993a28](https://github.com/facebook/zstd/commit/d993a288e067ea55d406f8fc547d55b9ad6e725b)

### Security related
- Added Scorecards supply chain security analysis workflow, and fixed actions/checkout dependencies to specific commit hashes.
  ↳ [#3277](https://github.com/facebook/zstd/pull/3277): [79729f8](https://github.com/facebook/zstd/commit/79729f8a2dc15d45a805e1c2f408f739958518b6) | [#3384](https://github.com/facebook/zstd/pull/3384): [e3f2c8b](https://github.com/facebook/zstd/commit/e3f2c8b11c09c6dfd0b86c03bb36906750235ce1)
- Fixed -Wstringop-overflow compiler warning in HUF_fillDTableX2 function, and adjusted parameter types.
  ↳ [#3440](https://github.com/facebook/zstd/pull/3440): [dc2b3e8](https://github.com/facebook/zstd/commit/dc2b3e887607fed7545f3003ce755e918d75999a)

### Documentation
- Fixed the formatting problem of missing line breaks in the help page.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [4de9d63](https://github.com/facebook/zstd/commit/4de9d637e86ea7963225d1a87d2d26f0e1e039fe)
- Added compilation option descriptions to README.md, and directed users to consult lib/README.md and programs/README.md to learn about advanced compilation flags; also updated the build system documentation to clarify that make is an officially maintained build system.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [6be3181](https://github.com/facebook/zstd/commit/6be3181307f6bb3824eb322db67675f393671266), [b33ef91](https://github.com/facebook/zstd/commit/b33ef91694f0b8b13471da0a39e584c4000f89fe), [515266e](https://github.com/facebook/zstd/commit/515266e31b2369f82594d47ff4666f0612382bb7)
- Added instructions for using the --set-exact-output option in the README of cli-tests.
  ↳ [#3394](https://github.com/facebook/zstd/pull/3394): [7df6e25](https://github.com/facebook/zstd/commit/7df6e25b8530392d121e73ba5cfaf71b3c0ec3ef)
- Updated CHANGELOG in preparation for v1.5.4 release.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [4aa3bc4](https://github.com/facebook/zstd/commit/4aa3bc49da8608c0cc921fbc49b703addb6cffa8)
- Added decompressor errata document, recording known decoder errors and repair versions.
  ↳ [#3092](https://github.com/facebook/zstd/pull/3092): [696fa25](https://github.com/facebook/zstd/commit/696fa2524a584d4e77c55d3a639d2e0283bd919f)
- Updated the man page to provide more detailed instructions for the --train mode and --single-thread options.
  ↳ [#3112](https://github.com/facebook/zstd/pull/3112): [0df2fd6](https://github.com/facebook/zstd/commit/0df2fd6088a02cfce7305ccd44874fa9d94cbbb3) | [#3487](https://github.com/facebook/zstd/pull/3487): [27bf96e](https://github.com/facebook/zstd/commit/27bf96e72bb786a94f7fef13b7f2e5d7ee1d6d48)
- Updated the fuzzer's README document, adding command instructions for running all targets in parallel and checking for crashes.
  ↳ [#3174](https://github.com/facebook/zstd/pull/3174): [bb4a3c7](https://github.com/facebook/zstd/commit/bb4a3c71ef352d2fdb5bb5bfa9b11b72bb3d28d5)
- Rewritten the CLI help output, unified the format, punctuation and capitalization, cleaned up the welcome message, and updated the CLI name and version display format.
  ↳ [#3385](https://github.com/facebook/zstd/pull/3385): [678335c](https://github.com/facebook/zstd/commit/678335c4f30a05857a94ac285c1d2eb6ce52cb88), [9c93dd7](https://github.com/facebook/zstd/commit/9c93dd71cdb301595a8a9e364348967a173c010c)

### Build/CI
- Changed the workflow trigger condition for release product generation from release creation to release release to solve the problem that draft release cannot be triggered.
  ↳ [#3018](https://github.com/facebook/zstd/pull/3018): [fa9cb45](https://github.com/facebook/zstd/commit/fa9cb4510ac26cdad607e19c72133e4c4961b189)
- In the Meson build system, valgrind testing is made optional and installation of valgrind is no longer mandatory.
  ↳ [#3120](https://github.com/facebook/zstd/pull/3120): [26134b4](https://github.com/facebook/zstd/commit/26134b4565a85e133f6f77b16b4fe9cd0c530a07)
- In the Meson build system, for non-MSVC builds, the shared libraries and static libraries of libzstd are linked simultaneously to solve the problem of private symbol reuse and simplify dependency management (MSVC builds still use the complete static library), and the practice of manually extracting object files is removed, making the zstd program slightly smaller.
  ↳ [#3122](https://github.com/facebook/zstd/pull/3122): [6548ec7](https://github.com/facebook/zstd/commit/6548ec7440712eb531f4148ed0568cf90fa1e523)
- Removed explicit specification of C++11 and C99 compilation standards in CMake scripts to avoid potential side effects.
  ↳ [#3167](https://github.com/facebook/zstd/pull/3167): [eceecc5](https://github.com/facebook/zstd/commit/eceecc5b2cade40e2ffe7e4ff4c7d2e16883961a)
- Added UBSan test target and removed pointer-overflow recovery option for tighter detection of pointer overflow undefined behavior.
  ↳ [#3258](https://github.com/facebook/zstd/pull/3258): [bc7492c](https://github.com/facebook/zstd/commit/bc7492cefa7251a3cc4d4e8a844be115c77e745c), [ca78d10](https://github.com/facebook/zstd/commit/ca78d101f78b40c024f150f84915b531fb800858), [66ed3df](https://github.com/facebook/zstd/commit/66ed3df0967c3cb6446ca5d1b8920f5f4d0170e6), [cf255cc](https://github.com/facebook/zstd/commit/cf255cc5e096db94154623e98d8e7387bba92429)
- Removed setting in Meson build configuration to force use of gnu99 C standard.
  ↳ [#3170](https://github.com/facebook/zstd/pull/3170): [15f3605](https://github.com/facebook/zstd/commit/15f3605135ef7647402c1639af3b50de30e613af)
- Fixed build errors caused by incompatible test compilation options under MSVC.
  ↳ [#3180](https://github.com/facebook/zstd/pull/3180): [cd9d0a7](https://github.com/facebook/zstd/commit/cd9d0a7e6e5aa770b377d738eb94de6671c5487e)
- Removed use of sed -E flag in build scripts to be compatible with sed versions that do not support this flag.
  ↳ [#3245](https://github.com/facebook/zstd/pull/3245): [ae5f273](https://github.com/facebook/zstd/commit/ae5f273a92cdb8c95dde0167690c266dfbbfd2b2)
- Introduced the CLEAN variable in the Makefile to simplify make clean maintenance, and renamed valgrindTest to test-valgrind to unify the naming convention.
  ↳ [#3256](https://github.com/facebook/zstd/pull/3256): [c0b4673](https://github.com/facebook/zstd/commit/c0b46738b4bae20ff0c316fa3f1c4b02c9c2b088), [5129b4a](https://github.com/facebook/zstd/commit/5129b4ab101165ee04104436a7202a6a4be6106a)
- In the Meson build system, the project version number is changed from hard-coded to dynamically obtained from the header file, and repeated logic is removed to simplify the build configuration.
  ↳ [#3327](https://github.com/facebook/zstd/pull/3327): [6c3ed93](https://github.com/facebook/zstd/commit/6c3ed93c2761cebe46d581e40695c5d4370fca58)
- Add Ubuntu focal software source in CI workflow, fix build failure of gcc-7 and gcc-8.
  ↳ [#3331](https://github.com/facebook/zstd/pull/3331): [3f0b912](https://github.com/facebook/zstd/commit/3f0b912a8009b127a7446120cfbcdc2ff8aeed7f)
- Change the CI test running environment from ubuntu-latest to ubuntu-20.04 to avoid m68k test failure caused by the qemu version.
  ↳ [#3347](https://github.com/facebook/zstd/pull/3347): [d081d98](https://github.com/facebook/zstd/commit/d081d98ae7239385fe5e62d41898ef4b3c5e06ea)
- Fixed the ZSTD_LIB_MINIFY build option, reduced the static library size from about 600K to 324K, and added a new CI test monitoring library size.
  ↳ [#3366](https://github.com/facebook/zstd/pull/3366): [0c42424](https://github.com/facebook/zstd/commit/0c42424a1ed73555906cd10e9c40e8316c8584e2)
- Fix the return type checking error in the Meson build script and solve the problem that zstd cannot be built.
  ↳ [#3368](https://github.com/facebook/zstd/pull/3368): [e8401e9](https://github.com/facebook/zstd/commit/e8401e9e8d84c7dab40677cc1687138135e86901)
- Added PGO build support, including configurable LLVM profdata tool path and PGO build tasks in CI.
  ↳ [#3442](https://github.com/facebook/zstd/pull/3442): [87e169d](https://github.com/facebook/zstd/commit/87e169d05d75db5112df20361de33f7398ef27d5), [aab3dd4](https://github.com/facebook/zstd/commit/aab3dd4312d98b2eff868012a50b1523f41a1a9a) | [#3281](https://github.com/facebook/zstd/pull/3281): [2ffcb2d](https://github.com/facebook/zstd/commit/2ffcb2d6a882626d831b88d26e4c653c53efc38e), [2bd70ef](https://github.com/facebook/zstd/commit/2bd70eff06630d4bd4a8e2efe09b97aec809b3de)
- Fixed issue with custom assembler in CMake builds, explicitly compiling assembly files as C code.
  ↳ [#3382](https://github.com/facebook/zstd/pull/3382): [651a381](https://github.com/facebook/zstd/commit/651a38106095dd27ec149d64f2f6876802fca06c)
- Upgraded GitHub CodeQL Action from 2.1.37 to 2.1.38.
  ↳ [#3428](https://github.com/facebook/zstd/pull/3428): [3add5ca](https://github.com/facebook/zstd/commit/3add5ca3ef874483cf50ef134eb8477d0300c95a)
- Optimize Meson build, avoid repeated compilation of libzstd private symbols and test program poolTests, and reduce compilation steps.
  ↳ [#3122](https://github.com/facebook/zstd/pull/3122): [8d522b8](https://github.com/facebook/zstd/commit/8d522b8a9da21edc7b3b85faa4daeb495ff56a85), [df6eefb](https://github.com/facebook/zstd/commit/df6eefb3bbe18901875ffb7eef5bdb5e84066d7e)
- Integrate the CLI test suite into make test and add the test-cli-tests target.
  ↳ [#3020](https://github.com/facebook/zstd/pull/3020): [1fc42de](https://github.com/facebook/zstd/commit/1fc42de86a53320c056c9a3ca9847eae7ce1262b)
- Updated the Travis CI environment to Focal and fixed the pip installation script to resolve build failures caused by Python 3.6 stopping support.
  ↳ [#3039](https://github.com/facebook/zstd/pull/3039): [c01582d](https://github.com/facebook/zstd/commit/c01582dc8aee541171089fa2979c890752365104) | [#3041](https://github.com/facebook/zstd/pull/3041): [4b24ebd](https://github.com/facebook/zstd/commit/4b24ebdcf33cc5c2819272278e2d742b9d0f72fe)
- Fixed Windows runtime environment in CI workflow from windows-latest to windows-2019.
  ↳ [#3061](https://github.com/facebook/zstd/pull/3061): [9caabc0](https://github.com/facebook/zstd/commit/9caabc01c412ab3bd3f6a34c34efd59c0fc659ac)
- Add apt-get update command to GitHub Actions workflow to fix installation failure caused by expired package index.
  ↳ [#3082](https://github.com/facebook/zstd/pull/3082): [0c386af](https://github.com/facebook/zstd/commit/0c386afbfd07b3f914a00ab5a2a0cbf3f7af0d66)
- Disable test tasks for Visual Studio 2015.
  ↳ [#3106](https://github.com/facebook/zstd/pull/3106): [3e6bbdd](https://github.com/facebook/zstd/commit/3e6bbdd8473a753d2047969ac0053fb2cb4dda23)
- Mark test-zstream-3 tests in the Meson build system as expected to fail on Windows.
  ↳ [#3120](https://github.com/facebook/zstd/pull/3120): [6747ba4](https://github.com/facebook/zstd/commit/6747ba4ef5c5ff10e567fe6becf41436a745d0a1)
- Fixed the variable reference syntax error in the Makefile, and adjusted the compilation options of the uasan target.
  ↳ [#3247](https://github.com/facebook/zstd/pull/3247): [efef80b](https://github.com/facebook/zstd/commit/efef80b75e3029d4c7fcd681dd86a6e9a1c45477) | [#3258](https://github.com/facebook/zstd/pull/3258): [fe22e8c](https://github.com/facebook/zstd/commit/fe22e8c5386a7efbfb32f4ea9c9d8438b7d639f0)
- Enable playTests.sh tests in CMake builds only when a Unix shell environment is detected.
  ↳ [#3289](https://github.com/facebook/zstd/pull/3289): [b87f310](https://github.com/facebook/zstd/commit/b87f3102fff25cce98b1d3ef17a4a9a9748c8ea1)
- Temporarily disable assembly optimization in Linux kernel module builds, and adjust cleanup rules to correctly remove test artifacts.
  ↳ [#3292](https://github.com/facebook/zstd/pull/3292): [43de2aa](https://github.com/facebook/zstd/commit/43de2aa17d5817bc566f0b8ed13c6c8283b1d8d4)
- Added the --spdx option to the freestanding script to automatically insert the SPDX license identification line in the generated file.
  ↳ [#3294](https://github.com/facebook/zstd/pull/3294): [5c1cdba](https://github.com/facebook/zstd/commit/5c1cdba7dd7c8cf1d7913e9593517ec2e663bced)
- Upgrade multiple GitHub Actions dependencies: Scorecard v2.0.6, setup-msbuild v1.1.3, publish-binaries v2.0, upload-artifact v3.
  ↳ [#3309](https://github.com/facebook/zstd/pull/3309): [a8f8dc8](https://github.com/facebook/zstd/commit/a8f8dc8c5cbd91350a4f69147b2f79f8e04dbf56) | [#3337](https://github.com/facebook/zstd/pull/3337): [91c7547](https://github.com/facebook/zstd/commit/91c7547fb503eec03f5765d1f1953bb54c39274a) | [#3339](https://github.com/facebook/zstd/pull/3339): [8864748](https://github.com/facebook/zstd/commit/88647489d499ce36c10d437c4aa17ce94ca11f25) | [#3340](https://github.com/facebook/zstd/pull/3340): [9730aa4](https://github.com/facebook/zstd/commit/9730aa432697ecc15014c2006e26c8e3778e1bd2)
- Re-enable version compatibility testing.
  ↳ [#3371](https://github.com/facebook/zstd/pull/3371): [5850839](https://github.com/facebook/zstd/commit/58508398f4121f2a84092ac771db0f2b0fbb3b1a)
- Removed expected failure flag from zstream test on Windows platform so that the test now passes normally.
  ↳ [#3364](https://github.com/facebook/zstd/pull/3364): [aaa38b2](https://github.com/facebook/zstd/commit/aaa38b29bbd91592c866917aefca10eb71c645c7)
- Enable building of programs and contrib directories in Meson builds for Windows CI.
  ↳ [#3380](https://github.com/facebook/zstd/pull/3380): [3cee69a](https://github.com/facebook/zstd/commit/3cee69a1cc536a5ff88fd81288e6eab3b2140049), [67cd24b](https://github.com/facebook/zstd/commit/67cd24b25b997f6e9f3e1aac7e38579b932d9d47)
- Upgrade CodeQL Action to v2.1.39.
  ↳ [#3378](https://github.com/facebook/zstd/pull/3378): [79a00f8](https://github.com/facebook/zstd/commit/79a00f8dcfb7a1e528f026b5e08a071a2b965574) | [#3446](https://github.com/facebook/zstd/pull/3446): [3663faa](https://github.com/facebook/zstd/commit/3663faa05abd2527ec1ec27723aca698265a1a61)
- Fix test failure caused by symbolic links in MSYS2 environment: set MSYS="" environment variable to let MSYS2 replace symbolic links with file copy.
  ↳ [#3429](https://github.com/facebook/zstd/pull/3429): [018b68f](https://github.com/facebook/zstd/commit/018b68f332213e75aaf8fb20524c4306dad6b1aa)
- Divide Meson tests into two suites, fast and slow, and only run fast tests by default.
  ↳ [#3120](https://github.com/facebook/zstd/pull/3120): [9c3e18f](https://github.com/facebook/zstd/commit/9c3e18f7feff00b6d816a6c4cbea906e0ef1fd93)
- Upgrade ossf/scorecard-action to v2.1.0.
  ↳ [#3377](https://github.com/facebook/zstd/pull/3377): [6554596](https://github.com/facebook/zstd/commit/65545969d56d8eaad448732becd36e23a4ccd425)

### Maintenance
- Add comments to the detection logic of single-symbol alphabets when compressing literals to clarify how edge cases are handled.
  ↳ [#3419](https://github.com/facebook/zstd/pull/3419): [ac45e07](https://github.com/facebook/zstd/commit/ac45e078a5bc22e06d1be1375c25795b7ef3c1ff)
- Upgraded multiple GitHub Actions dependency versions.
  ↳ [#3265](https://github.com/facebook/zstd/pull/3265): [b1b1e3a](https://github.com/facebook/zstd/commit/b1b1e3aa53eaffb296cb878d1651c96d85682867) | [#3402](https://github.com/facebook/zstd/pull/3402): [1f72dca](https://github.com/facebook/zstd/commit/1f72dca0ff07e00c1805b9bd58b1ae460f29b677) | [#3414](https://github.com/facebook/zstd/pull/3414): [6f17a5d](https://github.com/facebook/zstd/commit/6f17a5d8df75c639f30dde6ebd58f11b9f32242e) | [#3415](https://github.com/facebook/zstd/pull/3415): [59a536a](https://github.com/facebook/zstd/commit/59a536aa01f825bab50bc2aa2e9e12109912588e) | [#3464](https://github.com/facebook/zstd/pull/3464): [dd7fdc9](https://github.com/facebook/zstd/commit/dd7fdc98c8196dfd12594fc5349d8c260b150d0b) | [#3477](https://github.com/facebook/zstd/pull/3477): [35835f4](https://github.com/facebook/zstd/commit/35835f4126270a413ac2a28fb4981cc842ce62c0)
- Enhanced the security of GitHub Actions workflows, including adding permission declarations, fixed dependency hashes and limiting run scope.
  ↳ [#3264](https://github.com/facebook/zstd/pull/3264): [091917a](https://github.com/facebook/zstd/commit/091917a4a1ef1b5f57ea1fd96034cd13dcf6c68d) | [#3386](https://github.com/facebook/zstd/pull/3386): [150aa23](https://github.com/facebook/zstd/commit/150aa23ef47b5b0fcab425ae3d6679f252b14e1c) | [#3277](https://github.com/facebook/zstd/pull/3277): [de9a450](https://github.com/facebook/zstd/commit/de9a450c00639a759c97860dcb60f4afda3e7d16)
- Added rules to automatically update GitHub Actions weekly in Dependabot configuration.
  ↳ [#3284](https://github.com/facebook/zstd/pull/3284): [bc1b401](https://github.com/facebook/zstd/commit/bc1b40166d21737bb5a93018dfa021533f86ea4c)
- Fixed compiler warnings caused by unused variables and unused parameters.
  ↳ [#3139](https://github.com/facebook/zstd/pull/3139): [9166c6a](https://github.com/facebook/zstd/commit/9166c6ae204950b22c8fd5c0fb0cd2ee4c4b5abf) | [#3219](https://github.com/facebook/zstd/pull/3219): [b1bbb0e](https://github.com/facebook/zstd/commit/b1bbb0eb4c91d8e5d170b0cf732daacd0252e459)
- Enforce a minimum literal cost of 1 bit in optimal parsers.
  ↳ [#2983](https://github.com/facebook/zstd/pull/2983): [9e1b482](https://github.com/facebook/zstd/commit/9e1b4828e56a028efa0efdd7c30a58e6dd48c8c1)
- Added seqBench benchmark program under contrib/ for evaluating sequence compression API performance.
  ↳ [#3257](https://github.com/facebook/zstd/pull/3257): [61c79bf](https://github.com/facebook/zstd/commit/61c79bf0d63e4b3e9ecbc610900a14eefa4cd746)
- Shortened display width of status and summary lines in very verbose mode.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [feaaf7a](https://github.com/facebook/zstd/commit/feaaf7a6b1d1301e99634951d6ab3e20625e9a4a)
- Add comments, improve test case titles and remove apt-get in clang tasks.
  ↳ [#3258](https://github.com/facebook/zstd/pull/3258): [a06e953](https://github.com/facebook/zstd/commit/a06e953db94deb60615cd54255cdc60b533d913c)
- Rewritten the null value checking logic of bufStart pointer.
  ↳ [#3304](https://github.com/facebook/zstd/pull/3304): [5334339](https://github.com/facebook/zstd/commit/533433942134bdf1016eebfcc205012e66d6537c)
- Rearranged the order of options in the command line help information to make the logical grouping more reasonable.
  ↳ [#3487](https://github.com/facebook/zstd/pull/3487): [4d82a4d](https://github.com/facebook/zstd/commit/4d82a4d3f227bb6ed369f1a179a6736b913a05e1)

### Others
- Fixed spelling and grammatical errors in multiple source files and documentation.
  ↳ [#3046](https://github.com/facebook/zstd/pull/3046): [4c4d403](https://github.com/facebook/zstd/commit/4c4d403ecba80e372e413b219e44df2ff7339a52) | [#3060](https://github.com/facebook/zstd/pull/3060): [cf1894b](https://github.com/facebook/zstd/commit/cf1894b3243f5510c34b871f6d6e6b8321de01f8) | [#3095](https://github.com/facebook/zstd/pull/3095): [3a64aa2](https://github.com/facebook/zstd/commit/3a64aa29a641f861c94387da209715a641f26447), [b772f53](https://github.com/facebook/zstd/commit/b772f53952fa167e3c8d5630b26397e8d4fb4c5b) | [#3117](https://github.com/facebook/zstd/pull/3117): [0579679](https://github.com/facebook/zstd/commit/05796796fd0a9bc972abf3097557f68d6ae93ef4)
- Fixed errors in comments, repeated words and inconsistent variable names.
  ↳ [#2974](https://github.com/facebook/zstd/pull/2974): [4b9d1dd](https://github.com/facebook/zstd/commit/4b9d1dd9ffc882ff9ac57e2363a411591a27b886) | [#3026](https://github.com/facebook/zstd/pull/3026): [2b957af](https://github.com/facebook/zstd/commit/2b957afec7b43afa2884441856c0d7277bdecb49) | [#3127](https://github.com/facebook/zstd/pull/3127): [22875ec](https://github.com/facebook/zstd/commit/22875ece616624215ecb86211c4256c39a710a82)
- Adjusted the format of help information and progress output.
  ↳ [#3094](https://github.com/facebook/zstd/pull/3094): [7fbe60d](https://github.com/facebook/zstd/commit/7fbe60d577802394137201b689263e8aa9a62080) | [#3487](https://github.com/facebook/zstd/pull/3487): [2431809](https://github.com/facebook/zstd/commit/24318093cce0ae0fc55922a55761bf5389d7384d)
- Adjusted the format of conditional expressions to improve code readability.
  ↳ [#3114](https://github.com/facebook/zstd/pull/3114): [ce6b69f](https://github.com/facebook/zstd/commit/ce6b69f5c593a4ee06f8a09517141dbd1ee12621)
- Updated comments for the single-file library generation script, added examples, and updated command names and copyright years.
  ↳ [#3005](https://github.com/facebook/zstd/pull/3005): [7d90f0b](https://github.com/facebook/zstd/commit/7d90f0b520fda6cd9def6cd248c54b075717e948), [3f181b6](https://github.com/facebook/zstd/commit/3f181b61927b0f517b11ddec2ca43490b6de693f)
- Updated merge script example in README, and corrected man page description.
  ↳ [#3005](https://github.com/facebook/zstd/pull/3005): [dd7d29a](https://github.com/facebook/zstd/commit/dd7d29a19c7ac00f02f524c0f8822c691b7ed64c) | [#3108](https://github.com/facebook/zstd/pull/3108): [f133bc8](https://github.com/facebook/zstd/commit/f133bc8c9c345fac5c28b6758e1f133b8b6280fd)
- Added comments to optimal parser code to improve readability.
  ↳ [#3248](https://github.com/facebook/zstd/pull/3248): [4a1a79a](https://github.com/facebook/zstd/commit/4a1a79a51229bafbd89964043af236ebd4707b38)
- Add zstreamtest_ubsan to .gitignore.
  ↳ [#3258](https://github.com/facebook/zstd/pull/3258): [4a6783b](https://github.com/facebook/zstd/commit/4a6783bbbb78418a1b23f2bc16814c9206425c0a)
- Adjusted the handling of symlinks in CLI tests.
  ↳ [#3055](https://github.com/facebook/zstd/pull/3055): [169f8c1](https://github.com/facebook/zstd/commit/169f8c11fff94c7cb2280efb1b5ae3c8fb3a7c5c)
- Replaced XOR in bitwise operations with subtraction to improve code readability, and fixed typos in tests.
  ↳ [#3045](https://github.com/facebook/zstd/pull/3045): [71d9dab](https://github.com/facebook/zstd/commit/71d9dab76f6c496a39356f4d5e984525f2050373)
- Fixed multiple typos in documentation and code.
  ↳ [#3135](https://github.com/facebook/zstd/pull/3135): [14894d6](https://github.com/facebook/zstd/commit/14894d63c1d96667e7bb62666a52f3e20e63e23d) | [#3161](https://github.com/facebook/zstd/pull/3161): [2436405](https://github.com/facebook/zstd/commit/24364057bcb6b29a65c6ab91a3da6a32add141eb) | [#3259](https://github.com/facebook/zstd/pull/3259): [0015308](https://github.com/facebook/zstd/commit/0015308c0f294e0e04a426064be5c41778fe8107) | [#3487](https://github.com/facebook/zstd/pull/3487): [6640377](https://github.com/facebook/zstd/commit/6640377783e73211d1afd440550f8587dd9de75c)
- Updated links in the document, changed HTTP references to HTTPS, and fixed broken links.
  ↳ [#3352](https://github.com/facebook/zstd/pull/3352): [4dffc35](https://github.com/facebook/zstd/commit/4dffc35f2edf2e5fa53c3ea9c5c975fe2f1d6ebc) | [#3487](https://github.com/facebook/zstd/pull/3487): [1bc9dfe](https://github.com/facebook/zstd/commit/1bc9dfe46eda467203fb046cf36a8be17d4576a3)
- Updated the copyright statement, changed the copyright owner to Meta Platforms, and unified the copyright year.
  ↳ [#3173](https://github.com/facebook/zstd/pull/3173): [8927f98](https://github.com/facebook/zstd/commit/8927f985ffed45101f9c6c95ac26cd1f6018ecb7), [36d5c2f](https://github.com/facebook/zstd/commit/36d5c2f32621c7e434640006960c77dac3e83eb0), [7f12f24](https://github.com/facebook/zstd/commit/7f12f24cf47416fee0f1e84e4c57feb60e1bed0d), [5d693cc](https://github.com/facebook/zstd/commit/5d693cc38cd7866c525ef6101c35f20e15514a6b)
- Eliminated compilation warnings by handling unused variables.
  ↳ [#3139](https://github.com/facebook/zstd/pull/3139): [778f639](https://github.com/facebook/zstd/commit/778f639be961ab6c83ab84e0f3fd3ecb0fd09f4f)
- Removed an empty line to retrigger CI.
  ↳ [#3320](https://github.com/facebook/zstd/pull/3320): [0547c3d](https://github.com/facebook/zstd/commit/0547c3d3f89d6b4785cf095bd07cd4cad9c576a9)
- Updated comments and debug logs in the code to make them more accurate and readable.
  ↳ [#3129](https://github.com/facebook/zstd/pull/3129): [1dd046a](https://github.com/facebook/zstd/commit/1dd046a50783ebc4d0eb10928e71b2dd7c71cd4c) | [#3230](https://github.com/facebook/zstd/pull/3230): [1c847e2](https://github.com/facebook/zstd/commit/1c847e2e32f3c2203a9b81b6081b53f9275ec438) | [#3487](https://github.com/facebook/zstd/pull/3487): [ecd7601](https://github.com/facebook/zstd/commit/ecd7601c36e8dc788c37121648c1769c7e8b4733)
- Fixed many errors in the documentation, including format documentation examples, command line option descriptions, and man page terminology and formatting.
  ↳ [#3143](https://github.com/facebook/zstd/pull/3143): [f33ccd2](https://github.com/facebook/zstd/commit/f33ccd2d1b7e7a1b20ca721c5d05193b2eb5e637) | [#3197](https://github.com/facebook/zstd/pull/3197): [6d75b36](https://github.com/facebook/zstd/commit/6d75b36b7f80c6289d2ec44e63986c0cbdadf03e) | [#3487](https://github.com/facebook/zstd/pull/3487): [9abecfb](https://github.com/facebook/zstd/commit/9abecfbb7ec41172d5e3f3de82b38cd3324e6f08) | [#3397](https://github.com/facebook/zstd/pull/3397): [382026f](https://github.com/facebook/zstd/commit/382026f09646867500819652ff27cfa47e1e0768)
- Change the permission mode in the chmod() trace log to output in octal format.
  ↳ [#3432](https://github.com/facebook/zstd/pull/3432): [7a8c8f3](https://github.com/facebook/zstd/commit/7a8c8f3fe7477b3c12b03999f38f1034b278ff93)
- Fixed typo in variable names for test commands in CI workflows.
  ↳ [#3460](https://github.com/facebook/zstd/pull/3460): [295724b](https://github.com/facebook/zstd/commit/295724b515c01beb6e3583404854681d4eb3869b)
