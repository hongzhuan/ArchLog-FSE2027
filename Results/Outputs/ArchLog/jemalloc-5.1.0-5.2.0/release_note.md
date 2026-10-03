# Release Note

## Important Changes

### Platform Abstraction Layer
- Support zero size in size2index lookups and path calculations, and remove unnecessary zero size branch checks in fast paths. (Architecture-related: core module sz zero size support)
  ↳ [#1341](https://github.com/jemalloc/jemalloc/pull/1341): [4edbb7c](https://github.com/jemalloc/jemalloc/commit/4edbb7c64c83aa2059ade469bc798dadf3da194c)
- Introduce a new module sc.h, hide the size class calculation behind a layer of indirect access, remove the dependence on global configuration data, instead pass the configuration information through the pointer on the stack during initialization, and adjust the initialization order. At the same time, the slab size selection is migrated from compile-time calculation to run-time calculation, and the run-time calculation function and assertion verification of the compile-time result are added to prepare for subsequent run-time calculation. (Architecture-related: size class calculation reconstruction)
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [e904f81](https://github.com/jemalloc/jemalloc/commit/e904f813b40b4286e10172163c880fd9e1d0608a), [4f55c0e](https://github.com/jemalloc/jemalloc/commit/4f55c0ec220ae97eb5bc7e2bebc07d5c6100fa83) | [#1288](https://github.com/jemalloc/jemalloc/pull/1288): [3aba072](https://github.com/jemalloc/jemalloc/commit/3aba072cef71d0f2bacc4ef10932a46f1df43192)
- Added a new global slow path mechanism, allowing any thread to force other threads to enter the slow path the next time they obtain TSD; at the same time, the TSD state access method was restructured, using atomic operations and encapsulated functions instead. (Architecture-related: internal mechanism)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [e870829](https://github.com/jemalloc/jemalloc/commit/e870829e645bfd6d54e4a2d4cacce39478216a1e), [0379235](https://github.com/jemalloc/jemalloc/commit/0379235f47585ac8f583ba85aab9d294abfa44b5)
- Added Seq module to implement a simple seqlock to provide fast read and write concurrency support when there are few write operations. (Architecture-related: concurrency primitives)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [06a8c40](https://github.com/jemalloc/jemalloc/commit/06a8c40b36403e902748d3f2a14e6dd43488ae89)
- Make background_thread no longer dependent on libdl. This function can still be enabled when libdl is not used. (Architecture-related: build dependencies)
  ↳ [#1244](https://github.com/jemalloc/jemalloc/pull/1244): [2db2d2e](https://github.com/jemalloc/jemalloc/commit/2db2d2ef5e1cf2eb2c0de362c916d0f7a2f1a9ef)
- Add TSD support for multi-threaded fork scenarios to ensure that the tsd_nominal_tsds list in the child process is in a reasonable state. (Architecture-related: fork compatibility)
  ↳ [#1293](https://github.com/jemalloc/jemalloc/pull/1293): [41b7372](https://github.com/jemalloc/jemalloc/commit/41b7372eadee941b9164751b8d4963f915d3ceae)
- Introduced the sharded bin mechanism, added the opt.bin_shards option, supported specifying the number of shards for different bin sizes, and stored the shard selection results in TSD to improve the scalability of arena. (Architecture-related: allocator architecture)
  ↳ [#1378](https://github.com/jemalloc/jemalloc/pull/1378): [37b8913](https://github.com/jemalloc/jemalloc/commit/37b89139252db18c95ebce3e0eac67817fa4a8ab), [3f9f283](https://github.com/jemalloc/jemalloc/commit/3f9f2833f6228e07673d75c9bce6f5fb58c5f3b0), [98b56ab](https://github.com/jemalloc/jemalloc/commit/98b56ab23dd4d3dc826f06906e6c51c9c9d4d52a), [45bb448](https://github.com/jemalloc/jemalloc/commit/45bb4483baef0f9bb1362349d9838ee041c42754), [711a61f](https://github.com/jemalloc/jemalloc/commit/711a61f3b41880718eb23fcfdd572d0daa5fb6ca) | [#1396](https://github.com/jemalloc/jemalloc/pull/1396): [441335d](https://github.com/jemalloc/jemalloc/commit/441335d924984022a3e17c3f013a0ad33806a5ff) | [#1476](https://github.com/jemalloc/jemalloc/pull/1476): [6fe1163](https://github.com/jemalloc/jemalloc/commit/6fe11633b066d74bdbb0f037a373af6e12a8b6c2)
- Add platform-specific thread or CPU related support for FreeBSD and Windows platforms: use pthread_set_name_np on FreeBSD to set the name for the background thread; implement the malloc_getcpu function for Windows platforms, use GetCurrentProcessorNumber to get the current processor number. (Architecture-related: platform compatibility)
  ↳ [#1354](https://github.com/jemalloc/jemalloc/pull/1354): [ceba1dd](https://github.com/jemalloc/jemalloc/commit/ceba1dde2774e4eae659a548263970cd9b74d319) | [#1360](https://github.com/jemalloc/jemalloc/pull/1360): [daa0e43](https://github.com/jemalloc/jemalloc/commit/daa0e436ba232d67b832e1b270b13c5061eebfe9)
- When dlsym(RTLD_NEXT, "pthread_create") fails, it no longer returns an error, but falls back to the default pthread_create implementation. (Architecture-related: core module behavior)
  ↳ [#1242](https://github.com/jemalloc/jemalloc/pull/1242): [77a71ef](https://github.com/jemalloc/jemalloc/commit/77a71ef2b76c2e858c81e10349f28534307f1c91)
- Adjust the mutex initialization macro under FreeBSD to support debug mode, and remove the FreeBSD-specific page size detection code. (Architecture-related: platform compatibility)
  ↳ [#1301](https://github.com/jemalloc/jemalloc/pull/1301): [0771ff2](https://github.com/jemalloc/jemalloc/commit/0771ff2cea6dc18fcd3f6bf452b4224a4e17ae38)
- Fixed the problem that the zero page may not be obtained when refilling when using custom extent hooks or transparent huge pages, added manual clearing judgment logic and adjusted the clearing behavior accordingly. (Architecture-related: external behavior)
  ↳ [#1302](https://github.com/jemalloc/jemalloc/pull/1302): [f459454](https://github.com/jemalloc/jemalloc/commit/f459454afe019251712728b983d2eed0b03f5c80)
- Fix optimizer bug on s390x platform, disable __builtin_clz in pow2_ceil_u32 to avoid test failure. (Architecture-related: platform compatibility)
  ↳ [#1315](https://github.com/jemalloc/jemalloc/pull/1315): [115ce93](https://github.com/jemalloc/jemalloc/commit/115ce93562ab76f90a2509bf0640bc7df6b2d48f)
- Restrict the lwsync instruction to only use on the powerpc64 architecture, 32-bit powerpc uses the sync instruction instead to avoid triggering illegal instruction traps on some cores. (Architecture-related: platform compatibility)
  ↳ [#1352](https://github.com/jemalloc/jemalloc/pull/1352): [be0749f](https://github.com/jemalloc/jemalloc/commit/be0749f59151ffecbdf7d9f82193350f018904dd)
- Fixed a regression issue where mmap did not correctly set the commit attribute when overcommit was enabled on FreeBSD. (Architecture-related: Platform compatibility)
  ↳ [#1362](https://github.com/jemalloc/jemalloc/pull/1362): [50b473c](https://github.com/jemalloc/jemalloc/commit/50b473c8839f5408df179bdf6f2b3fd2cf5c3b2f)
- Fix the bug of tcache_flush, and add detection of invalid tcache id. When encountering an invalid id, the program will be terminated directly. (Architecture-related: public API)
  ↳ [#1369](https://github.com/jemalloc/jemalloc/pull/1369): [1f56115](https://github.com/jemalloc/jemalloc/commit/1f561157042a779be12a2159a385de0416133f6b)
- Avoid creating unnecessary background threads for huge arenas that perform eager purging by default, while retaining the ability to create background threads when the user explicitly sets a non-zero decay time. (Architecture-related: public API)
  ↳ [#1409](https://github.com/jemalloc/jemalloc/pull/1409): [bbe8e6a](https://github.com/jemalloc/jemalloc/commit/bbe8e6a9097203c7b29140b5410c787a6e204593)
- Adjusted the default value of huge_threshold from 0 to 8MB, and updated the comment to indicate that this option is still experimental. (Architecture-related: Configuration item changes)
  ↳ [#1412](https://github.com/jemalloc/jemalloc/pull/1412): [350809d](https://github.com/jemalloc/jemalloc/commit/350809dc5d43ea994de04f7a970b6978a8fec6d2)
- Avoid repeated definition of tsd_t type, fix build failure when integrating with FreeBSD libc. (Architecture-related: platform compatibility)
  ↳ [#1442](https://github.com/jemalloc/jemalloc/pull/1442): [dca7060](https://github.com/jemalloc/jemalloc/commit/dca7060d5e49b8a07179a1f13bf39f6d30e709c8)
- Fixed a compilation regression caused by using #pragma GCC diagnostic in versions below GCC 4.6, and added a version check to avoid using this directive for older versions of GCC. (Architecture-related: platform compatibility)
  ↳ [#1452](https://github.com/jemalloc/jemalloc/pull/1452): [14d3686](https://github.com/jemalloc/jemalloc/commit/14d3686c9f3ed28f1ef4c9ec5f7bde945473194b)
- Fixed the issue of tls_callback not correctly adding prefix in #pragma comment(linker) directive. (Architecture-related: platform compatibility)
  ↳ [#1445](https://github.com/jemalloc/jemalloc/pull/1445): [cbdb180](https://github.com/jemalloc/jemalloc/commit/cbdb1807cea6828d0f61e1a0516613efc3e7189e)
- Fallback to 32-bit atomic operations when 8-bit atomic operations are not available to avoid thread-specific data state setting failures. (Architecture-related: platform compatibility)
  ↳ [#1449](https://github.com/jemalloc/jemalloc/pull/1449): [b804d0f](https://github.com/jemalloc/jemalloc/commit/b804d0f019df87d8cc96e3c812e98793256cb418)
- Change the state access of thread local storage (TSD) to a functional interface, and change the status field to an atomic type to prepare for subsequent remote modification of the thread state. (Architecture-related: TSD state interface)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [982c10d](https://github.com/jemalloc/jemalloc/commit/982c10de3566f38628770e57c62d1a6cdc5a09f9), [39d6420](https://github.com/jemalloc/jemalloc/commit/39d6420c0c39619176af3477b827e8a92442b768)
- Changed the inlining mode of atomic operations from static inline to forced inlining. (Architecture-related: public API inlining mode)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [e74a1a3](https://github.com/jemalloc/jemalloc/commit/e74a1a37c82fa3a44cee1002d9d8957bcc8274a7)
- Disable runtime lazy cleanup support detection on FreeBSD to reduce the number of system calls at startup. (Architecture-related: Platform compatibility: FreeBSD)
  ↳ [#1251](https://github.com/jemalloc/jemalloc/pull/1251): [676cdd6](https://github.com/jemalloc/jemalloc/commit/676cdd66792ccb629a978837ea2a066d5db342cc)
- Switch to using MAP_EXCL and MAP_ALIGNED on FreeBSD for direct memory mapping, replacing the previous complicated workaround. (Architecture-related: Platform compatibility: FreeBSD memory mapping)
  ↳ [#1251](https://github.com/jemalloc/jemalloc/pull/1251): [f80c97e](https://github.com/jemalloc/jemalloc/commit/f80c97e477d1b3fe7778c65d9439d673738b4131)
- Optimized the implementation of pow2_ceil_u64 and pow2_ceil_u32 using built-in functions or assembly instructions on supported platforms, and excluded the s390 architecture. (Architecture-related: Platform compatibility: exclude s390)
  ↳ [#1303](https://github.com/jemalloc/jemalloc/pull/1303): [4c548a6](https://github.com/jemalloc/jemalloc/commit/4c548a61c89b0472b9952fcc4090eb00c2a88870)
- Allows you to choose to use readlinkat instead of readlink through the macro JEMALLOC_READLINKAT at compile time. (Architecture-related: platform compatibility)
  ↳ [#1300](https://github.com/jemalloc/jemalloc/pull/1300): [e8ec952](https://github.com/jemalloc/jemalloc/commit/e8ec9528abac90efe4e0cc3a29da8d7aea59f23d)
- Deprecate OSSpinLock and use os_unfair_lock to implement mutex locks. (Architecture-related: mutex lock implementation)
  ↳ [#1367](https://github.com/jemalloc/jemalloc/pull/1367): [43f3b1a](https://github.com/jemalloc/jemalloc/commit/43f3b1ad0cd0900797688aa8b52b1face6416999)
- Detect the availability of 8-bit atomic operations and perform fallback processing when unavailable. (Architecture-related: platform compatibility)
  ↳ [#1449](https://github.com/jemalloc/jemalloc/pull/1449): [06f0850](https://github.com/jemalloc/jemalloc/commit/06f0850427e26cb24950de60bbe70bc192ffce6a)

### API & Integration Layer
- Added experimental API smallocx, returns pointer and actual available size when allocating memory, and changes symbol name to version-dependent hash form. (Architecture-related: public API)
  ↳ [#1270](https://github.com/jemalloc/jemalloc/pull/1270): [08260a6](https://github.com/jemalloc/jemalloc/commit/08260a6b944a67a3d9f63e7eb738718fc760e0ea), [01e2a38](https://github.com/jemalloc/jemalloc/commit/01e2a38e5a5523350496b11af46cf1d4c1d74e4c), [730e57b](https://github.com/jemalloc/jemalloc/commit/730e57b08fe5bd6bdc38ca4ff6a73959984d8ef0)
- Added a new hook module to provide a low-overhead hook installation and removal mechanism, and access hook calls in allocation, release, expansion and other paths; at the same time, the experimental.hooks.install and experimental.hooks.remove control items are exposed through the mallctl interface. (Architecture-related: public API)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [5ae6e7c](https://github.com/jemalloc/jemalloc/commit/5ae6e7cbfa6d6788340cc87d7717548f4d7960fe), [226327c](https://github.com/jemalloc/jemalloc/commit/226327cf66f6e1fb1aed24ed3e2e9c291d1843b7), [c154f58](https://github.com/jemalloc/jemalloc/commit/c154f5881b72c52a131e88ade6108d663ac03700), [83e5161](https://github.com/jemalloc/jemalloc/commit/83e516154cfacfc1e010a03f2f420bf79913944a), [6727004](https://github.com/jemalloc/jemalloc/commit/67270040a56d8658ce6aec81b15d78571e0e9198), [cb0707c](https://github.com/jemalloc/jemalloc/commit/cb0707c0fc948875876b93514938646455650e2b), [bb071db](https://github.com/jemalloc/jemalloc/commit/bb071db92ee8368fb6e64ef328d49fae6ba48089), [fe0e399](https://github.com/jemalloc/jemalloc/commit/fe0e39938593b5fb16dc09fcdbe29d6ad7b3cf05), [59e371f](https://github.com/jemalloc/jemalloc/commit/59e371f46331a3f4b688d6622a0af7ccc4f96be6)
- Added MALLOC_CONF parsing to support dynamic slab size configuration, and added corresponding integration tests. (Architecture-related: configuration items)
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [5112d9e](https://github.com/jemalloc/jemalloc/commit/5112d9e5fd2a15d6b75523a3a4122b726fbae479)
- Implement the large memory dedicated arena function, add the opt.huge_threshold option, and route large memory allocations that exceed the threshold to independent arenas to reduce fragmentation and improve reuse. (Architecture-related: configuration items)
  ↳ [#1235](https://github.com/jemalloc/jemalloc/pull/1235): [94a88c2](https://github.com/jemalloc/jemalloc/commit/94a88c26f4d9cffd884a349201e7605f13495f3f), [1302af4](https://github.com/jemalloc/jemalloc/commit/1302af4c43e031304b422e36fcbb9e159804e0ac), [ff622ee](https://github.com/jemalloc/jemalloc/commit/ff622eeab51325979226d5430c68a08d3e00b26b)
- Refactor the emitter API to make it clearer as a standalone JSON emitter, and add support for outputting raw values and nested arrays in arrays. (Architecture-related: public API)
  ↳ [#1267](https://github.com/jemalloc/jemalloc/pull/1267): [eb261e5](https://github.com/jemalloc/jemalloc/commit/eb261e53a6bfaef9797395fe09d6a425b11acb42)
- Add logging function for sampling allocation, support automatic start logging at runtime through prof_opt_log flag, and manual control through prof_log_start and prof_log_stop mallctl interface. (Architecture-related: public API)
  ↳ [#1267](https://github.com/jemalloc/jemalloc/pull/1267): [b664bd7](https://github.com/jemalloc/jemalloc/commit/b664bd79356d7f6da6f413023f9aef014b85c145), [5e23f96](https://github.com/jemalloc/jemalloc/commit/5e23f96dd4e4ff2847a85d44a01b66e4ed2da21f)
- Add extents information to malloc statistics output, including the number and bytes of dirty, muzzy, retained extents for each size category. (Architecture-related: public API)
  ↳ [#1298](https://github.com/jemalloc/jemalloc/pull/1298): [c14e6c0](https://github.com/jemalloc/jemalloc/commit/c14e6c08192034d9140d61197d7c4981ca293610)
- Rename experimental_huge_threshold to oversize_threshold, and allow setting to low values (including 0) to disable the feature. (Architecture-related: public API)
  ↳ [#1411](https://github.com/jemalloc/jemalloc/pull/1411): [7a815c1](https://github.com/jemalloc/jemalloc/commit/7a815c1b7c796ef35e7ede60cb2dd44aba9626b4) | [#1416](https://github.com/jemalloc/jemalloc/pull/1416): [e3db480](https://github.com/jemalloc/jemalloc/commit/e3db480f6f3c147a8630c0ec45fde1da5764270b) | [#1469](https://github.com/jemalloc/jemalloc/pull/1469): [788a657](https://github.com/jemalloc/jemalloc/commit/788a657cee745c1f827ddf1db50d580bd5e4347b)
- Added a rate counter in the statistical output to display the number of allocation, release and other operations per second. (Architecture-related: public API)
  ↳ [#1388](https://github.com/jemalloc/jemalloc/pull/1388): [36de518](https://github.com/jemalloc/jemalloc/commit/36de5189c70fee959ebcdfadd8dfa374ff430de5)
- Fixed the background thread index calculation error, changed the modulo base from ncpus to max_background_threads, and added an auxiliary function to unify the index logic. (Architecture-related: public API)
  ↳ [#1220](https://github.com/jemalloc/jemalloc/pull/1220): [312352f](https://github.com/jemalloc/jemalloc/commit/312352faa89a39ff1e690d709d7d6f852f89d61d)
- Add reentrancy protection to the hook function to prevent recursion caused by triggering again during hook execution. (Architecture-related: public API)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [a7f749c](https://github.com/jemalloc/jemalloc/commit/a7f749c9af0d5ca51b5b5eaf35c2c2913d8a77e1)
- When abort_conf is enabled, it will no longer abort due to unrecognized experimental options, allowing experimental functions to be tested normally. (Architecture-related: configuration behavior)
  ↳ [#1285](https://github.com/jemalloc/jemalloc/pull/1285): [4bc4871](https://github.com/jemalloc/jemalloc/commit/4bc48718b2eb98e3646a86af816f9c6db29d1612)
- Muzzy memory decay is disabled by default. (Architecture-related: configuration item changes)
  ↳ [#1421](https://github.com/jemalloc/jemalloc/pull/1421): [8e9a613](https://github.com/jemalloc/jemalloc/commit/8e9a613122251d4c519059f8e1e11f27f6572b4c)
- Renamed hooks module to test_hooks, this is a breaking change. (Architecture-related: module rename)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [c7a87e0](https://github.com/jemalloc/jemalloc/commit/c7a87e0e0bd02cf278760f3c22615d3129dc1ae2)
- Move the extra pointer into the hook_t structure and simplify the hook_install calling interface. (Architecture-related: public API simplification)
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [126e9a8](https://github.com/jemalloc/jemalloc/commit/126e9a84a5a793fb0d53ca4656a91889b3ae40e8)
- Renamed the configuration option huge_threshold to experimental_huge_threshold, and marked it as an experimental feature. (Architecture-related: Configuration option renamed)
  ↳ [#1235](https://github.com/jemalloc/jemalloc/pull/1235): [cdf15b4](https://github.com/jemalloc/jemalloc/commit/cdf15b458a1c348722fa43cb1813ac3a93fdc634)
- Remove the experimental smallocx API from the public header file, users need to add external declarations to use it. (Architecture-related: public API removal)
  ↳ [#1270](https://github.com/jemalloc/jemalloc/pull/1270): [741fca1](https://github.com/jemalloc/jemalloc/commit/741fca1bb7773e14cf929824b94506eb9f545e5e)
- Set the default number of background threads to 4, and adjust the checking logic for the upper limit of the number of threads. At the same time, related tests have been fixed so that they no longer assume the default number of threads. (Architecture-related: background thread configuration)
  ↳ [#1374](https://github.com/jemalloc/jemalloc/pull/1374): [c4063ce](https://github.com/jemalloc/jemalloc/commit/c4063ce439523d382f2dfbbc5bf6da657e6badb0) | [#1218](https://github.com/jemalloc/jemalloc/pull/1218): [b293a3e](https://github.com/jemalloc/jemalloc/commit/b293a3eb86a32b9c242ac39d88312c0a9d317b8b)

### Profiling & Statistics Layer
- Fixed the sampling count memory regression caused by reconstruction, and added a fast path check function to ensure that the sampling count is correct when tdata is empty. (Architecture-related: public API)
  ↳ [#1351](https://github.com/jemalloc/jemalloc/pull/1351): [936bc2a](https://github.com/jemalloc/jemalloc/commit/936bc2aa15504076f884ed97a51e169924fe4a89)
- Change bytes_until_sample type from uint64_t to int64_t to optimize assembly generation on x86 architecture and adjust sampling accumulation logic. (Architecture-related: public API)
  ↳ [#1342](https://github.com/jemalloc/jemalloc/pull/1342): [997d86a](https://github.com/jemalloc/jemalloc/commit/997d86acc6d2cc632b79669ebf3f938290e9f5da)

### Cross-cutting / Other Architecture-related Changes
- Added fast paths for free() and sdallocx(): added rtree_szind_slab_read_fast function, which is used to quickly read szind and slab information from the L1 cache, and removed frame operations in most calls. (Architecture-related: public API: added rtree_szind_slab_read_fast)
  ↳ [#1365](https://github.com/jemalloc/jemalloc/pull/1365): [5e79529](https://github.com/jemalloc/jemalloc/commit/5e795297b33f25329a034fd898ee7d80c57b9a8f), [794e29c](https://github.com/jemalloc/jemalloc/commit/794e29c0abbd77624d1e5599313ebd77bdc17ccc) | No PR: [09adf18](https://github.com/jemalloc/jemalloc/commit/09adf18f1aefcee71cc716f4f366c7e2e889b7fa)
- Added extent_arena_ind_get function in the tcache refresh path, which is used to directly obtain the arena index; at the same time, modify the extent_arena_get function to avoid loading the actual arena pointer when only checking arena matching. (Architecture-related: public API: new extent_arena_ind_get)
  ↳ [#1386](https://github.com/jemalloc/jemalloc/pull/1386): [7241bf5](https://github.com/jemalloc/jemalloc/commit/7241bf5b745ba5ec24b26b0ef2bd30b1c0a428dc)
- Clean up compilation warnings so that jemalloc has no warnings under -Wextra; add diagnostic macros and fallthrough macros, remove UNUSED parameters, globally disable -Wunused-parameter, locally suppress specific warnings, and add a CI build robot. (Architecture-related: build and platform compatibility)
  ↳ [#1200](https://github.com/jemalloc/jemalloc/pull/1200): [3d29d11](https://github.com/jemalloc/jemalloc/commit/3d29d11ac2c1583b9959f73c0548545018d31c8a)
- Added --disable-libdl configuration option to allow disabling libdl to support building completely static binaries, and updated related documentation. (Architecture-related: Build and platform compatibility)
  ↳ [#1244](https://github.com/jemalloc/jemalloc/pull/1244): [1f55a15](https://github.com/jemalloc/jemalloc/commit/1f55a15467357bb559701687dbef1be84047ddfe), [23b15e7](https://github.com/jemalloc/jemalloc/commit/23b15e764b3d87c8e69a348d60d13e7e44f137b5)
- Restrict suppression of -Wmissing-field-initializer warnings to only compiler versions where the warning bug exists (GCC < 5.1 and all clang versions). (Architecture-related: Build and Platform Compatibility)
  ↳ [#1273](https://github.com/jemalloc/jemalloc/pull/1273): [fb924dd](https://github.com/jemalloc/jemalloc/commit/fb924dd7bf5e765ffcb273b6b88a515fea54fea8)
- Add --enable-shared and --enable-static options to the configure script, allowing users to control whether shared libraries and static libraries are built. (Architecture-related: build and installation methods)
  ↳ [#1394](https://github.com/jemalloc/jemalloc/pull/1394): [4e920d2](https://github.com/jemalloc/jemalloc/commit/4e920d2c9d5aecc9dec7069a0c9736b1f14eead9)
- Replaced link options in the build system from -lpthread to -pthread so that -latomic is automatically added when needed, e.g. on riscv64 systems. (Architecture-related: Platform compatibility)
  ↳ [#1402](https://github.com/jemalloc/jemalloc/pull/1402): [4711910](https://github.com/jemalloc/jemalloc/commit/471191075d6a88eb1364fb5f332237eb3d512872)
- Enable document building by default, and skip building and output warnings when XML support is missing, so that make install can succeed without first executing make dist. (Architecture-related: build and installation methods)
  ↳ [#1430](https://github.com/jemalloc/jemalloc/pull/1430): [9015deb](https://github.com/jemalloc/jemalloc/commit/9015deb126d7b2b90ef822cf0183f96abb9b97f9)
- Adjust the startup sequence of the memory allocator, advance MALLOC_CONF parsing before size class initialization, so that subsequent modules can use configuration parameters. (Architecture-related: initialization sequence)
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [4610ffa](https://github.com/jemalloc/jemalloc/commit/4610ffa942a00d80a8e8af2365069bed7d561415)

## Routine Changes

### New features
- Added lg_ceil function, added corresponding unit test, and re-added bit_util test to Makefile.
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [2f07e92](https://github.com/jemalloc/jemalloc/commit/2f07e92adb7060045e9e8601126e5ec071091c42)
- Added page customization function and added corresponding unit tests.
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [a7f68ae](https://github.com/jemalloc/jemalloc/commit/a7f68aed3ef53a194f6b932b92bddd8c84c43de4)
- Add size statistics counter for each arena's extent_avail heap.
  ↳ [#1298](https://github.com/jemalloc/jemalloc/pull/1298): [126252a](https://github.com/jemalloc/jemalloc/commit/126252a7e6bd098d649f6a82a947c7c056816c2c)
- Remove bump_empty_alloc option, integrate zero size allocation check into size class lookup, and simplify lock operations during initialization.
  ↳ [#1341](https://github.com/jemalloc/jemalloc/pull/1341): [ac34afb](https://github.com/jemalloc/jemalloc/commit/ac34afb4037d7e9e87efde2b8e913d87aae131da)
- Added ticker_trytick function, which is used to try to perform tick operations in the fast path.
  ↳ [#1345](https://github.com/jemalloc/jemalloc/pull/1345): [0ec656e](https://github.com/jemalloc/jemalloc/commit/0ec656eb7117127602f295510de694083353f23e)

### bug fixes
- Fixed the assertion error in the page cleanup function: when the configured page size is larger than the system page size, the assertion is no longer falsely triggered, and instead checks whether the address is aligned with the system page size.
  ↳ [#1217](https://github.com/jemalloc/jemalloc/pull/1217): [e8a63b8](https://github.com/jemalloc/jemalloc/commit/e8a63b87c36ac814272d73b503658431d2000055)
- Fix the format of opt.lg_extent_max_active_fit in statistics output: change it from unsigned integer to size_t type output.
  ↳ [#1239](https://github.com/jemalloc/jemalloc/pull/1239): [9bd8deb](https://github.com/jemalloc/jemalloc/commit/9bd8deb26044b7a3f056f8995aae95ffe86d19ed)
- Fixed a regression in tcache_bin_flush_large where incorrect lock operations were caused by using the wrong arena variable.
  ↳ [#1258](https://github.com/jemalloc/jemalloc/pull/1258): [fec1ef7](https://github.com/jemalloc/jemalloc/commit/fec1ef7c91b5368ad0d6f0c84bc77fa71d9dc949)
- Adjust the calling timing of prof_boot0 to avoid opt_prof_prefix being overwritten during the boot process.
  ↳ [#1325](https://github.com/jemalloc/jemalloc/pull/1325): [88771fa](https://github.com/jemalloc/jemalloc/commit/88771fa0138c75a2d29601cc33025d81822b082a)
- Explicitly trigger arena decay when destroying tcache to avoid decay not being triggered due to non-nominal tsd; at the same time, update the bin count macro in tcache_flush_cache from NBINS to SC_NBINS.
  ↳ [#1366](https://github.com/jemalloc/jemalloc/pull/1366): [7ee0b6c](https://github.com/jemalloc/jemalloc/commit/7ee0b6cc37ecbecf8f53ba46326258275053ca50)
- Fixed the problem of incorrect calling of tcache_destroy in the tcaches_flush function, and instead used tcache_flush_cache for correct cache flushing.
  ↳ [#1368](https://github.com/jemalloc/jemalloc/pull/1368): [cd2931a](https://github.com/jemalloc/jemalloc/commit/cd2931ad9bbd78208565716ab102e86d858c2fff)
- Fixed bug in merging statistics in sharded bins: Adjusted merging logic to avoid double counting when all items in the same arena are not refreshed.
  ↳ [#1389](https://github.com/jemalloc/jemalloc/pull/1389): [99f4eef](https://github.com/jemalloc/jemalloc/commit/99f4eefb61ae1f13e47af6eac34748fd0a789404)
- Fixed missing rate calculation for the total number of row requests in the statistics output.
  ↳ [#1413](https://github.com/jemalloc/jemalloc/pull/1413): [8c95713](https://github.com/jemalloc/jemalloc/commit/8c9571376e65c8099ea315261c24e940410386c8)
- Trigger backtracking initialization of libgcc only when profiling is enabled, to resolve issues during boot.
  ↳ [#1441](https://github.com/jemalloc/jemalloc/pull/1441): [18450d0](https://github.com/jemalloc/jemalloc/commit/18450d0abe36757fe6e4eb08f6b15f8ce943f9cb)
- Fix missing unlock operation in extent_register_impl function error path.
  ↳ [#1472](https://github.com/jemalloc/jemalloc/pull/1472): [59d9891](https://github.com/jemalloc/jemalloc/commit/59d98919482b2a101c4092428a4c0092abb797a1)
- Fix compilation warning: In configuration processing, change the check parameter of opt_lg_extent_max_active_fit from yes to no to avoid performing minimum value check on it.
  ↳ [#1472](https://github.com/jemalloc/jemalloc/pull/1472): [0101d5e](https://github.com/jemalloc/jemalloc/commit/0101d5ebef7230ef5aa1597be425e2a60e92f348)
- In prof_log related functions, change internal memory allocation from ialloc to iallocztm to avoid potential lock order reversal issues.
  ↳ [#1476](https://github.com/jemalloc/jemalloc/pull/1476): [978a7a2](https://github.com/jemalloc/jemalloc/commit/978a7a21ae5fe8e5367732b2dba9f92742aef9f1)

### Refactoring optimization
- Move the link fields in the TSD linked list inside the tcache structure to optimize cache utilization.
  ↳ [#1261](https://github.com/jemalloc/jemalloc/pull/1261): [d1e11d4](https://github.com/jemalloc/jemalloc/commit/d1e11d48d4c706e17ef3508e2ddb910f109b779f)
- Migrate quantum detection-related macro definitions to a separate quantum.h file to simplify the header file structure.
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [07b89c7](https://github.com/jemalloc/jemalloc/commit/07b89c76736313159e952648a9df3bdcfe57eda2)
- Extract TSD field name obfuscation logic into macros to uniformly manage indirect access to TSD members.
  ↳ [#1163](https://github.com/jemalloc/jemalloc/pull/1163): [feff510](https://github.com/jemalloc/jemalloc/commit/feff510b9f938ae1b4e2f43815bc7b10f70fac12)
- Reconstruct the arena_is_auto function and introduce the manual_arena_base variable to replace the original offset calculation.
  ↳ [#1235](https://github.com/jemalloc/jemalloc/pull/1235): [79522b2](https://github.com/jemalloc/jemalloc/commit/79522b2fc225f709a4ca7503c00f56df5d667160)
- Migrate the sampling related field bytes_until_sample from tdata to tsd, and optimize the sampling accumulation logic to reduce fast path branch judgment.
  ↳ [#1342](https://github.com/jemalloc/jemalloc/pull/1342): [9ed3bdc](https://github.com/jemalloc/jemalloc/commit/9ed3bdc8484049bd304c771a1b10070d5d7c95db), [0ac5243](https://github.com/jemalloc/jemalloc/commit/0ac524308d3f636d1a4b5149fa7adf24cf426d9c)

### Test related
- Added a new remote release test, and added allocation calls for specified arena in existing tests.
  ↳ [#1258](https://github.com/jemalloc/jemalloc/pull/1258): [5082001](https://github.com/jemalloc/jemalloc/commit/50820010fef8f40e1221360ef745d9bb5fa93364)
- Added hook micro-benchmark test to measure hook execution overhead.
  ↳ [#1297](https://github.com/jemalloc/jemalloc/pull/1297): [1f71e1c](https://github.com/jemalloc/jemalloc/commit/1f71e1ca4319de7788d53d1d0ba905995c7f52bd)
- Add test cases for zero size allocation and aligned allocation.
  ↳ [#1341](https://github.com/jemalloc/jemalloc/pull/1341): [2b112ea](https://github.com/jemalloc/jemalloc/commit/2b112ea5932d280288882d8bb38e7942b166fe5a)
- Explicitly specify arena 0 in OOM tests and alignment tests to avoid size routing problems caused by the huge_threshold feature; add a new remote release test.
  ↳ [#1412](https://github.com/jemalloc/jemalloc/pull/1412): [d314501](https://github.com/jemalloc/jemalloc/commit/d3145014a00d6420824a45bb24fa9237a553d8dc)

### Performance optimization
- When muzzy decay is disabled, allocations from extents_muzzy are skipped to reduce unnecessary mutex operations.
  ↳ [#1226](https://github.com/jemalloc/jemalloc/pull/1226): [d22e150](https://github.com/jemalloc/jemalloc/commit/d22e150320801c114b3694e860195254bad1ef0f)
- In tcache flush path, avoid acquiring large_mtx lock for automatic arena, only hold the lock when needed.
  ↳ [#1228](https://github.com/jemalloc/jemalloc/pull/1228): [c834912](https://github.com/jemalloc/jemalloc/commit/c834912aa9503d470c3dae2b2b7840607f0d6e34)
- Optimize the ixalloc function to avoid re-querying the allocation size by adding new output parameters, thus improving performance.
  ↳ [#1240](https://github.com/jemalloc/jemalloc/pull/1240): [0ff7ff3](https://github.com/jemalloc/jemalloc/commit/0ff7ff3ec7b322881fff3bd6d4861fda6e9331d9)
- Changed critical size classes (max_small_class, min_large_class, max_large_class) to static constants to avoid accessing extra cache lines in the fast path.
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [55e5cc1](https://github.com/jemalloc/jemalloc/commit/55e5cc1341de87ad06254d719946a5ecd05f06ab)
- Add a fast path for malloc: assuming the size is within the search range and hits tcache, otherwise fall back to the default path; malloc is treated as a leaf function through tail call optimization, reducing the caller's overhead of saving registers.
  ↳ [#1345](https://github.com/jemalloc/jemalloc/pull/1345): [0f83136](https://github.com/jemalloc/jemalloc/commit/0f8313659e93379d930995ea2d2af0a079cc422e) | [#1340](https://github.com/jemalloc/jemalloc/pull/1340): [325e330](https://github.com/jemalloc/jemalloc/commit/325e3305fc7563600a710341d1f98cb8e04caaba)
- Optimize the merging logic when releasing large blocks of memory, reducing lock overhead by avoiding locking active adjacent memory blocks, improving large block release performance by about 20%.
  ↳ [#1356](https://github.com/jemalloc/jemalloc/pull/1356): [d66f976](https://github.com/jemalloc/jemalloc/commit/d66f97662879a1a0c61ee12ba4b760fa6f458eef)
- When retain is enabled, the default extent release process is skipped to avoid unnecessary lock and metadata operations.
  ↳ [#1361](https://github.com/jemalloc/jemalloc/pull/1361): [8dabf81](https://github.com/jemalloc/jemalloc/commit/8dabf81df1b7db0fd16903abab889dfd61b4c07f)
- Fixed cache line contention caused by frequent CAS operations when multiple threads compete for the same mutex, and reduced trylock calls in spin waits by adding a lock status flag.
  ↳ [#1382](https://github.com/jemalloc/jemalloc/pull/1382): [b23336a](https://github.com/jemalloc/jemalloc/commit/b23336af96e6ef9efb47591ce7bf2c8a1eab866b)
- Optimize batch allocation paths, add fast paths and reduce the number of atomic operations.
  ↳ [#1359](https://github.com/jemalloc/jemalloc/pull/1359): [13c237c](https://github.com/jemalloc/jemalloc/commit/13c237c7ef5baa63c820539e0cfef4c4c5c74ea2), [4b82872](https://github.com/jemalloc/jemalloc/commit/4b82872ebf5e8b701e8b37c6d1297ceb88405df8), [17aa470](https://github.com/jemalloc/jemalloc/commit/17aa470760cefb3057be746f7022196035f0cfbe)
- Immediately clear excessively large merge extents to optimize memory usage.
  ↳ [#1458](https://github.com/jemalloc/jemalloc/pull/1458): [fb56766](https://github.com/jemalloc/jemalloc/commit/fb56766ca9b398d07e2def5ead75a021fc08da03)
- Add assertion in allocation fast path to ensure maximum allocation size is less than SSIZE_MAX.
  ↳ [#1342](https://github.com/jemalloc/jemalloc/pull/1342): [d1a861f](https://github.com/jemalloc/jemalloc/commit/d1a861fa80c66221be8c4d94e51128a4641809da)
- Added cache_bin_dalloc_easy helper function and refactored tcache_dalloc_small.
  ↳ [#1365](https://github.com/jemalloc/jemalloc/pull/1365): [e2ab215](https://github.com/jemalloc/jemalloc/commit/e2ab215324d7d19e37f4be87beb7a179528a300f)
- Restore the optimization of getpagesize() on FreeBSD to avoid unnecessary system calls.
  ↳ [#1355](https://github.com/jemalloc/jemalloc/pull/1355): [a4c6b9a](https://github.com/jemalloc/jemalloc/commit/a4c6b9ae011628d012dd8eaab39fb60aa595b922)
- Optimize extent_recycle function in debug build to only check if the first page is zero.
  ↳ [#1371](https://github.com/jemalloc/jemalloc/pull/1371): [57553c3](https://github.com/jemalloc/jemalloc/commit/57553c3b1a5592dc4c03f3c6831d9b794e523865)
- When a thread is destroyed, memory is forced to be cleaned only when there are no background threads.
  ↳ [#1405](https://github.com/jemalloc/jemalloc/pull/1405): [0ecd5ad](https://github.com/jemalloc/jemalloc/commit/0ecd5addb1215f5ae9fad2b9cb4cf91ed5376ee8)

### Security related
- Add a check on the return value of malloc_read_fd in pages.c to avoid security issues caused by out-of-bounds memory access after negative values are converted to unsigned types.
  ↳ [#1337](https://github.com/jemalloc/jemalloc/pull/1337): [856319d](https://github.com/jemalloc/jemalloc/commit/856319dc8a3d15c3eddf83d106e01e6f63c349a7)

### Documentation
- Added instructions to the documentation for jemalloc's greedier use of mmap when retain:true is enabled.
  ↳ [#1383](https://github.com/jemalloc/jemalloc/pull/1383): [a7b0a12](https://github.com/jemalloc/jemalloc/commit/a7b0a124c3ebe505cfd8c2d5cc797b8f0c96fbc6)

### Build/CI
- Removed unused --with-lg-page-sizes configuration option and its related documentation.
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [5b7fc90](https://github.com/jemalloc/jemalloc/commit/5b7fc9056c8114d0774282d293cd5c9cce4ff931)
- Fixed syntax error in configure.ac.
  ↳ [#1447](https://github.com/jemalloc/jemalloc/pull/1447): [ac24ffb](https://github.com/jemalloc/jemalloc/commit/ac24ffb21e28ba1ed86250fa6a6dcaf02b43f7da)
- Removed unused macros JE_FORCE_SYNC_COMPARE_AND_SWAP_4 and JE_FORCE_SYNC_COMPARE_AND_SWAP_8 and their configuration checks.
  ↳ [#1446](https://github.com/jemalloc/jemalloc/pull/1446): [775fe30](https://github.com/jemalloc/jemalloc/commit/775fe302a75c4770edd9708e7348e626c96dfe58)
- Added valgrind test builds in Linux CI and commented out valgrind configurations that were not working due to issues on macOS.
  ↳ [#1271](https://github.com/jemalloc/jemalloc/pull/1271): [36eb0b3](https://github.com/jemalloc/jemalloc/commit/36eb0b3d77404f389cfddad6675fe1f479e76be7)
- Simplified the output of gen_travis.py script and streamlined .travis.yml by reusing addons configuration.
  ↳ [#1272](https://github.com/jemalloc/jemalloc/pull/1272): [0eb0641](https://github.com/jemalloc/jemalloc/commit/0eb0641cac0c3031f84469953b5e75b380867ccb)
- Added a new build task in Travis CI for testing the experimental smallocx API.
  ↳ [#1270](https://github.com/jemalloc/jemalloc/pull/1270): [837de32](https://github.com/jemalloc/jemalloc/commit/837de32496b1f20524c723516775a11bf236f891)
- Added CI consistency check to ensure that .travis.yml is consistent with the output generated by gen_travis.py, and updated .travis.yml accordingly.
  ↳ [#1272](https://github.com/jemalloc/jemalloc/pull/1272): [6deed86](https://github.com/jemalloc/jemalloc/commit/6deed86deb48d3b432d972a139a413a9fb38283b)

### Maintenance
- Added code style comments in SC module.
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [017dca1](https://github.com/jemalloc/jemalloc/commit/017dca198c74792967771d00b7501beade5b6fd0)
- Added optional size check in tcache flush path, and added error message output.
  ↳ [#1427](https://github.com/jemalloc/jemalloc/pull/1427): [e13400c](https://github.com/jemalloc/jemalloc/commit/e13400c919e6b6730284ff011875bbcdd6821f1c) | [#1469](https://github.com/jemalloc/jemalloc/pull/1469): [a4d017f](https://github.com/jemalloc/jemalloc/commit/a4d017f5e5aea12b745e67679ba40753f6d7a778)
- Added check that thread has left nominal state in thread death assertion.
  ↳ [#1293](https://github.com/jemalloc/jemalloc/pull/1293): [013ab26](https://github.com/jemalloc/jemalloc/commit/013ab26c8674e07d40098f7385e570c6d8b0dee9)
- Removed the no longer needed size_classes.sh script and cleaned up the corresponding static assertion code in sc.c.
  ↳ [#1104](https://github.com/jemalloc/jemalloc/pull/1104): [0552aad](https://github.com/jemalloc/jemalloc/commit/0552aad91b955db7ad1806907255e943af2fdb88)
- Adjusted the statistics output format, increasing column width and spacing to improve readability.
  ↳ [#1221](https://github.com/jemalloc/jemalloc/pull/1221): [09edea3](https://github.com/jemalloc/jemalloc/commit/09edea3f5c98dae3f298b7ac9f5adad13e528bc9) | [#1413](https://github.com/jemalloc/jemalloc/pull/1413): [522d1e7](https://github.com/jemalloc/jemalloc/commit/522d1e7b4b603d9ddc11c684c16d37113a9c0c12) | [#1420](https://github.com/jemalloc/jemalloc/pull/1420): [b33eb26](https://github.com/jemalloc/jemalloc/commit/b33eb26dee1c161572b209a8fe3f58419ce4874f)

### Others
- Corrected the comment of the SC_NPSIZES macro to accurately indicate that the macro represents the number of size classes that are integer multiples of the page size.
  ↳ [#1298](https://github.com/jemalloc/jemalloc/pull/1298): [33f1aa5](https://github.com/jemalloc/jemalloc/commit/33f1aa5badd2f9caf91991bab60df64a37c394bb)
- Updated copyright date, changing the year range to last to the present.
  ↳ [#1417](https://github.com/jemalloc/jemalloc/pull/1417): [374dc30](https://github.com/jemalloc/jemalloc/commit/374dc30d3dc6c5b664fda9b1fa0510559e568b6a)
- Remove unused comments in header files.
  ↳ [#1458](https://github.com/jemalloc/jemalloc/pull/1458): [f6c30cb](https://github.com/jemalloc/jemalloc/commit/f6c30cbafab1a841dd08f00541ed9651054bbe4a)
- Updated changelog for version 5.2.0.
  ↳ [#1473](https://github.com/jemalloc/jemalloc/pull/1473): [f7489dc](https://github.com/jemalloc/jemalloc/commit/f7489dc8f1fac233b0cd4e40331de8b738b1f2e2)
- Added a description of the opt.oversize_threshold configuration item in the document, and corrected the type descriptions of opt.background_thread and opt.max_background_threads.
  ↳ [#1471](https://github.com/jemalloc/jemalloc/pull/1471): [ce03e4c](https://github.com/jemalloc/jemalloc/commit/ce03e4c7b8ddeaec5e72c8fb160e378f418ed651)
- Adjust documentation wording for oversize_threshold.
  ↳ [#1474](https://github.com/jemalloc/jemalloc/pull/1474): [064d6e5](https://github.com/jemalloc/jemalloc/commit/064d6e570e7073096471413f6a5159541478eb01)
