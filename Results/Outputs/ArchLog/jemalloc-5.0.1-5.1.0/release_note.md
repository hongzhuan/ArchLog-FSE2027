# Release Note

## Important Changes

### Allocation Policy & Management Layer
- Separated bin management-related types, functions, global arrays, and initialization and fork processing logic from the arena module into independent bin modules, and renamed related types and global arrays. (Architecture event: bin module separation)
  ↳ [#1093](https://github.com/jemalloc/jemalloc/pull/1093): [4bf4a1c](https://github.com/jemalloc/jemalloc/commit/4bf4a1c4ea418ba490d35d23aee0f535e96ddd23), [a8dd887](https://github.com/jemalloc/jemalloc/commit/a8dd8876fb483f402833fa05f0fb46fe7c5416e1), [48bb4a0](https://github.com/jemalloc/jemalloc/commit/48bb4a056be97214fa049f21bead9618429c807a)
- Migrate bin statistics related code from arena module to bin module, and add bin_stats_merge function. (Architecture event: jemalloc_Core_Internal module change)
  ↳ [#1093](https://github.com/jemalloc/jemalloc/pull/1093): [8aafa27](https://github.com/jemalloc/jemalloc/commit/8aafa270fd56c36db374fa9f294217fa80151b3d)
- Added a new div module to support fast division operations of dynamic values through precalculation. (Architecture event: A new div module was added to the core internal module)
  ↳ [#1095](https://github.com/jemalloc/jemalloc/pull/1095): [21f7c13](https://github.com/jemalloc/jemalloc/commit/21f7c13d0b172dac6ea76236bbe0a2f3ee4bcb7b), [d41b19f](https://github.com/jemalloc/jemalloc/commit/d41b19f9c70c9dd8244e0879c7aef7943a34c750)
- Relax the reentrancy constraints of extent hooks, remove non-arena 0 assertions, and increase the reentrancy level upper limit check. (Architecture-related: public API)
  ↳ [#1010](https://github.com/jemalloc/jemalloc/pull/1010): [a315688](https://github.com/jemalloc/jemalloc/commit/a315688be0f38188f16fe89ee1657c7f596f8cbb)
- Added address space dump control function, supports setting the dumpable attribute of extent. (Architecture-related: public API)
  ↳ [#1052](https://github.com/jemalloc/jemalloc/pull/1052): [bbaa724](https://github.com/jemalloc/jemalloc/commit/bbaa72422bb086933890a125fd58bf199fe26f2d) | No PR: [d14bbf8](https://github.com/jemalloc/jemalloc/commit/d14bbf8d8190df411f0daf182f73f7b7786288c4)
- Added runtime detection of lazy purging support, and defined this constant on systems that lack MADV_FREE. (Architecture-related: platform compatibility)
  ↳ [#1034](https://github.com/jemalloc/jemalloc/pull/1034): [0720192](https://github.com/jemalloc/jemalloc/commit/0720192a323f5dd2dd27828c6ab3061f8f039416) | [#1048](https://github.com/jemalloc/jemalloc/pull/1048): [31ab38b](https://github.com/jemalloc/jemalloc/commit/31ab38be5f3c4b826db89ff3cd4f32f988747f06)

### Cross-cutting / Other Architecture-related Changes
- Added ILP32 support for aarch64 architecture, and added the --with-lg-vaddr option to allow users to specify the number of virtual address bits, and updated related documentation and test configurations. (Architecture-related: Platform compatibility: aarch64 ILP32)
  ↳ [#1193](https://github.com/jemalloc/jemalloc/pull/1193): [6df9060](https://github.com/jemalloc/jemalloc/commit/6df90600a7e4df51b06efe2d47df211cba5935a7) | [#1206](https://github.com/jemalloc/jemalloc/pull/1206): [63712b4](https://github.com/jemalloc/jemalloc/commit/63712b4c4e046e9d91807d0e1b5c890c52925379) | [#1207](https://github.com/jemalloc/jemalloc/pull/1207): [4c8829e](https://github.com/jemalloc/jemalloc/commit/4c8829e6924ee7abae6f41ca57303a88dd6f1315), [b001e6e](https://github.com/jemalloc/jemalloc/commit/b001e6e7407cd7e07bad533445eee7f0224cb268)
- Supports both __riscv and __riscv__ preprocessor definitions in RISC-V detection. (Architecture-related: Platform compatibility: RISC-V preprocessor definition)
  ↳ [#1081](https://github.com/jemalloc/jemalloc/pull/1081): [749caf1](https://github.com/jemalloc/jemalloc/commit/749caf14ae73a9ab1c48e538a8af09addbb35ee7)
- Disable JEMALLOC_HAVE_MADVISE_HUGE macro for arm* CPU architecture. (Architecture-related: Platform compatibility: arm disable MADVISE_HUGE)
  ↳ [#1102](https://github.com/jemalloc/jemalloc/pull/1102): [433c2ed](https://github.com/jemalloc/jemalloc/commit/433c2edabc5c03ae069ac652857c05c673807d0c)
- Added hierarchical logging function, supports fine control of log output through configuration items, simplified log interface, and added entry and exit logging for core memory allocation and release functions. (Architecture event: jemalloc_Core_Internal module change)
  ↳ [#958](https://github.com/jemalloc/jemalloc/pull/958): [9761b44](https://github.com/jemalloc/jemalloc/commit/9761b449c8c6b70abdb4cfa953e59847a84af406), [e215a7b](https://github.com/jemalloc/jemalloc/commit/e215a7bc18a2c3263a6fcca37c1ec53af6c4babd) | [#962](https://github.com/jemalloc/jemalloc/pull/962): [a9f7732](https://github.com/jemalloc/jemalloc/commit/a9f7732d45c22ca7d22bed6ff2eaeb702356884e) | [#964](https://github.com/jemalloc/jemalloc/pull/964): [e6aeceb](https://github.com/jemalloc/jemalloc/commit/e6aeceb6068ace14ca530506fdfeb5f1cadd9a19)
- Add minimum alignment support for m68k, nios2 and SH3 architectures. (Architecture event: jemalloc_Core_Internal module change)
  ↳ [#985](https://github.com/jemalloc/jemalloc/pull/985): [82d1a3f](https://github.com/jemalloc/jemalloc/commit/82d1a3fb318fb086cd4207ca03dbdd5b0e3bbb26)
- Added FreeBSD platform support and is compatible with old systems lacking O_CLOEXEC. (Architecture-related: platform compatibility)
  ↳ [#959](https://github.com/jemalloc/jemalloc/pull/959): [0975b88](https://github.com/jemalloc/jemalloc/commit/0975b88dfd3a890f469c8c282a5140013af85ab2) | [#985](https://github.com/jemalloc/jemalloc/pull/985): [8da69b6](https://github.com/jemalloc/jemalloc/commit/8da69b69e6c4cd951832138780ac632e57987b7c)
- Added --disable-initial-exec-tls configuration option to allow disabling the initial-exec TLS model during compilation. (Architecture-related: build and installation methods)
  ↳ [#1180](https://github.com/jemalloc/jemalloc/pull/1180): [a62e42b](https://github.com/jemalloc/jemalloc/commit/a62e42baebe09dc84aaff731faa6ff87fde6bc4e)
- In test generation scripts, skip use cases for testing large virtual address spaces in 32-bit mode. (Architecture-related: Platform compatibility)
  ↳ [#1215](https://github.com/jemalloc/jemalloc/pull/1215): [e94ca7f](https://github.com/jemalloc/jemalloc/commit/e94ca7f3e2b0ef393d713e7287b7f6b61645322b)
- The build system now allows the tool chain to determine the nm tool path by itself, ensuring that the symbol list is generated correctly when cross-compiling. (Architecture-related: build and installation methods)
  ↳ [#1024](https://github.com/jemalloc/jemalloc/pull/1024): [24766cc](https://github.com/jemalloc/jemalloc/commit/24766ccd5bcc379b7d518b3ec2480d2d146873ac) | [#949](https://github.com/jemalloc/jemalloc/pull/949): [3f50493](https://github.com/jemalloc/jemalloc/commit/3f5049340e66c6929c3270f7359617f62e053b11)
- Fixed the problem that the symbol list failed due to the lack of the dumpbin tool in the MinGW environment. Now only dumpbin is used for symbol export on the Cygwin platform. (Architecture-related: platform compatibility)
  ↳ [#1024](https://github.com/jemalloc/jemalloc/pull/1024): [a545f18](https://github.com/jemalloc/jemalloc/commit/a545f1804a19f48244ee5e328e32e2d036ffea0d) | [#949](https://github.com/jemalloc/jemalloc/pull/949): [ef55006](https://github.com/jemalloc/jemalloc/commit/ef55006c1d324692408eed87421f486812d3645d)
- Reformatted the version number format in jemalloc.pc.in. (Architecture-related: pkg-config configuration)
  ↳ [#1214](https://github.com/jemalloc/jemalloc/pull/1214): [a308af3](https://github.com/jemalloc/jemalloc/commit/a308af360ca8fccb31f9dcdb0654b0d4cf6f776c)
- Adjusted the order of include paths in the Makefile, and fixed the header file search problem during out-of-tree building and cross-compiling. (Architecture-related: build and installation methods)
  ↳ [#1211](https://github.com/jemalloc/jemalloc/pull/1211): [b73380b](https://github.com/jemalloc/jemalloc/commit/b73380bee0abde8e74f43d19d099cc151f51eb58)

### User-Facing Interface Layer
- Added a new emitter module to support structured output (JSON/table), and enhanced the row-level output and title printing functions of table mode. (Architecture events: A new emitter module was added to the core internal module)
  ↳ [#1144](https://github.com/jemalloc/jemalloc/pull/1144): [27a8fe6](https://github.com/jemalloc/jemalloc/commit/27a8fe6780cb901668489495b2fc302a2d071d8c), [ebe0b5f](https://github.com/jemalloc/jemalloc/commit/ebe0b5f8283b542f59cbe77f69e24935ebb5f866)
- Added support for transparent large pages, including opt.metadata_thp and opt.thp configuration options, supports multiple modes, and optimizes automatic triggering logic and statistics. (Architecture-related: public API)
  ↳ [#983](https://github.com/jemalloc/jemalloc/pull/983): [8fdd9a5](https://github.com/jemalloc/jemalloc/commit/8fdd9a579779b84d6af27f94c295f82a4df8e5be) | [#998](https://github.com/jemalloc/jemalloc/pull/998): [47b20bb](https://github.com/jemalloc/jemalloc/commit/47b20bb6544de9cdd4ca7ab870d6ad257c0ce4ff), [e55c3ca](https://github.com/jemalloc/jemalloc/commit/e55c3ca26758bcb7f6f1621fd690caa245f16942) | [#1046](https://github.com/jemalloc/jemalloc/pull/1046): [79e8345](https://github.com/jemalloc/jemalloc/commit/79e83451ff262fbc4bf66059eae672286b5eb9f0) | [#1134](https://github.com/jemalloc/jemalloc/pull/1134): [e4f090e](https://github.com/jemalloc/jemalloc/commit/e4f090e8df5adf180662c5eeac2af214f9594de4)
- Added arena.i.retain_grow_limit option, used to control the maximum size of retained memory growth. (Architecture-related: public API)
  ↳ [#1064](https://github.com/jemalloc/jemalloc/pull/1064): [e422fa8](https://github.com/jemalloc/jemalloc/commit/e422fa8e7ea749ab8c4783e405c0f4b19ac25db9)
- Added opt.lg_extent_max_active_fit option to control the allocation from dirty extent to avoid splitting too large active extent. (Architecture-related: public API)
  ↳ [#1071](https://github.com/jemalloc/jemalloc/pull/1071): [fac7068](https://github.com/jemalloc/jemalloc/commit/fac706836ffda46759914508b918e8b54c8020c8)
- Added a new configuration option for the maximum number of background threads, allowing users to limit the number of background threads. (Architecture-related: public API)
  ↳ [#1156](https://github.com/jemalloc/jemalloc/pull/1156): [8b14f3a](https://github.com/jemalloc/jemalloc/commit/8b14f3abc05f01419f9321a6a65ab9dd68dcebac)
- Use prof_active to control the trigger conditions of idump and gdump. (Architecture-related: prof_active controls idump/gdump)
  ↳ [#1160](https://github.com/jemalloc/jemalloc/pull/1160): [2dccf45](https://github.com/jemalloc/jemalloc/commit/2dccf4564016233bd4ef7772b43ec8423b8c44df)
- Allow setting extent hooks on uninitialized automatic arena. If the automatic arena has not been initialized, its initialization will be triggered. (Architecture-related: extent hooks setting behavior)
  ↳ [#1173](https://github.com/jemalloc/jemalloc/pull/1173): [3f0dc64](https://github.com/jemalloc/jemalloc/commit/3f0dc64c6b8c1fd77c819028013dacbc6d2ad6b6)
- Added arenas.lookup mallctl operation and stats_metadata_thp statistics configuration item. (Architecture-related: public API)
  ↳ [#1194](https://github.com/jemalloc/jemalloc/pull/1194): [a32b7bd](https://github.com/jemalloc/jemalloc/commit/a32b7bd5676e669821d15d319f686c3add451f4b)
- Fixed the deadlock problem caused by incorrect mutex lock status when multi-threaded fork on OS
  ↳ [#954](https://github.com/jemalloc/jemalloc/pull/954): [0a4f5a7](https://github.com/jemalloc/jemalloc/commit/0a4f5a7eea5e42292cea95fd30a88201c8d4a1ca), [fb6787a](https://github.com/jemalloc/jemalloc/commit/fb6787a78c3a1e3a4868520d0531fc2ebdda21d8)
- Change spin_adaptive to a static inline function to fix compilation warnings on FreeBSD. (Architecture-related: platform compatibility)
  ↳ [#980](https://github.com/jemalloc/jemalloc/pull/980): [048c667](https://github.com/jemalloc/jemalloc/commit/048c6679cd0ef1500d0609dce48fcd823d15d93b)
- Fixed the regression problem of cache bin queue not being cleared after fork and re-initialized in the child process. (Architecture-related: platform compatibility)
  ↳ [#1020](https://github.com/jemalloc/jemalloc/pull/1020): [9b20a4b](https://github.com/jemalloc/jemalloc/commit/9b20a4bf70efd675604985ca37335f8b0136a289)
- Add configure detection to determine strerror_r return value type, support more libc implementations. (Architecture-related: platform compatibility)
  ↳ [#1109](https://github.com/jemalloc/jemalloc/pull/1109): [f78d4ca](https://github.com/jemalloc/jemalloc/commit/f78d4ca3fbff6cab0c704c787706a53ddafcbe13)
- Fixed -Wshift-negative-value warning caused by left-shifting negative values. (Architecture-related: public API)
  ↳ [#1029](https://github.com/jemalloc/jemalloc/pull/1029): [3959a9f](https://github.com/jemalloc/jemalloc/commit/3959a9fe1973a7d7ddbbd99056c22e9b684a3275)
- Fixed the calculation error of the high bits of virtual address under ARM architecture. (Architecture-related: platform compatibility)
  ↳ [#1035](https://github.com/jemalloc/jemalloc/pull/1035): [7a8bc71](https://github.com/jemalloc/jemalloc/commit/7a8bc7172b17e219b3603e99c8da44efb283e652)
- Capitalize the log macro name to avoid conflict with the logarithmic function name in math.h. (Architecture-related: public API)
  ↳ [#1041](https://github.com/jemalloc/jemalloc/pull/1041): [8a7ee30](https://github.com/jemalloc/jemalloc/commit/8a7ee3014cea09e13e605bf47c11943df5a5eb2b)
- Disable the CPU_SPINWAIT macro and use the custom spin_cpu_spinwait function instead. (Architecture-related: public API)
  ↳ No PR: [1245faa](https://github.com/jemalloc/jemalloc/commit/1245faae9052350a96dbcb22de7979bca566dbec)
- Fix the problem of infinite growth of stash_decayed and add an upper limit on the number of pages. (Architecture-related: public API)
  ↳ [#1069](https://github.com/jemalloc/jemalloc/pull/1069): [b5d071c](https://github.com/jemalloc/jemalloc/commit/b5d071c26697813bcceae320ba88dee2a2a73e51)
- Check lock level only in non-reentrant state in iallocztm function. (architecture-related: core allocator behavior)
  ↳ [#1097](https://github.com/jemalloc/jemalloc/pull/1097): [91b247d](https://github.com/jemalloc/jemalloc/commit/91b247d311ce6837aa93d4315f5f7680abd8a11a)
- Fixed the read/write function return type warning on the Windows platform, and added a new encapsulation function. (Architecture-related: platform compatibility)
  ↳ No PR: [d3e0976](https://github.com/jemalloc/jemalloc/commit/d3e0976a2c1591b9fe433e7a383d8825683995f0)
- Unified the output of general arena statistics, per-arena statistics, arena mutex statistics and arena bin statistics to the structured text emitter, completed the structural transformation of the core statistical output, and unified the readable and JSON output formats. (Architecture event: Unified statistical output to emitter)
  ↳ [#1144](https://github.com/jemalloc/jemalloc/pull/1144): [e5acc35](https://github.com/jemalloc/jemalloc/commit/e5acc3540011fc6c3cec6aa97c567ff280617b74), [07fb707](https://github.com/jemalloc/jemalloc/commit/07fb707623de5da5b58c448683a3f71df67531c9), [a1738f4](https://github.com/jemalloc/jemalloc/commit/a1738f4efd7cfdaec576e54df90422e36cc6a8df), [4eed989](https://github.com/jemalloc/jemalloc/commit/4eed989bbfb7c56bdea97169ca07f9a7b7f14f27), [b646f89](https://github.com/jemalloc/jemalloc/commit/b646f89173be53d4f5eb59a894dbcdd64b457bee), [4a335e0](https://github.com/jemalloc/jemalloc/commit/4a335e0c6f6fa371edcd7663eebfe11cf93a1f17), [ec31d47](https://github.com/jemalloc/jemalloc/commit/ec31d476ffa36885182f2b569ee518d3dfd54761), [0d20eda](https://github.com/jemalloc/jemalloc/commit/0d20eda127c4f35c16cfffad15857d3b286166ba), [8076b28](https://github.com/jemalloc/jemalloc/commit/8076b28721e16d14a8a81bb6c17fba804812e110), [9e1846b](https://github.com/jemalloc/jemalloc/commit/9e1846b0041e29a331ecf76e9b23ddb730bc352f), [86c61d4](https://github.com/jemalloc/jemalloc/commit/86c61d4a575e7eb57ade8a39e9d552d95c63aa31), [cbde666](https://github.com/jemalloc/jemalloc/commit/cbde666d9a5a2bf1cb741661aebec228aa9f5827), [a6ef061](https://github.com/jemalloc/jemalloc/commit/a6ef061c4309852a8bb27c5374edb1bc6980ac06), [bc6620f](https://github.com/jemalloc/jemalloc/commit/bc6620f73e205004b2dfaf0438daeab617609295), [8fc8506](https://github.com/jemalloc/jemalloc/commit/8fc850695dc70958cfeffd53e9d5df261697cff5), [4c36cd2](https://github.com/jemalloc/jemalloc/commit/4c36cd2cc5c6ac7f27354b84606b0ca4d6178791)
- Rename the bin cache data structure in tcache to the general cache_bin type, and extract relevant functions to prepare for the subsequent separation of the cache logic of tcache and arena. (Architecture event: The cache data structure is unified into cache_bin)
  ↳ [#989](https://github.com/jemalloc/jemalloc/pull/989): [f3170ba](https://github.com/jemalloc/jemalloc/commit/f3170baa30654b2f62547fa1ac80707d396e1245) | [#1093](https://github.com/jemalloc/jemalloc/pull/1093): [901d94a](https://github.com/jemalloc/jemalloc/commit/901d94a2b06df09c960836901f6a81a0d3d00732)
- Arena statistics collection is changed to be carried out through cache bin. It is no longer necessary to understand the internal structure of tcache, which reduces module coupling. (Architecture event: Statistics collection is decoupled through cache bin)
  ↳ [#989](https://github.com/jemalloc/jemalloc/pull/989): [9c05490](https://github.com/jemalloc/jemalloc/commit/9c0549007dcb64f4ff35d37390a9a6a8d3cea880)
- Split arena statistics-related functions and types into independent files, unify naming conventions, and optimize the module structure. (Architecture event: Split statistics-related functions into independent files)
  ↳ [#1093](https://github.com/jemalloc/jemalloc/pull/1093): [7f1b02e](https://github.com/jemalloc/jemalloc/commit/7f1b02e3fa9de7e0bb5e2562994b5ab3b82c0ec3)
- Simplified the extent eviction logic, always evict one more extent, and removed the npages_max parameter. (Architecture-related: public API: extents_evict removes the npages_max parameter)
  ↳ [#1092](https://github.com/jemalloc/jemalloc/pull/1092): [740bdd6](https://github.com/jemalloc/jemalloc/commit/740bdd68b1d4b9c39c68432e06deb70ad4da3210)
- Fixed the printf format specifier warning that may appear when compiling gcc under FreeBSD system. (Architecture-related: platform compatibility)
  ↳ [#1177](https://github.com/jemalloc/jemalloc/pull/1177): [2a80d6f](https://github.com/jemalloc/jemalloc/commit/2a80d6f15b18de2ef17b310e995af366cc20034c)
- Separate the mutex lock statistics counter into 64-bit and 32-bit types, and adjust the corresponding reading and output logic. (Architecture-related: public API)
  ↳ [#1100](https://github.com/jemalloc/jemalloc/pull/1100): [f47e39d](https://github.com/jemalloc/jemalloc/commit/f47e39d11a0e7ef4201a1ac18efa7604c5152aa3)
- Make the header files generated by Visual Studio compatible with x86 and x64 modes, and automatically adjust the number of virtual address bits. (Architecture-related: platform compatibility)
  ↳ [#1117](https://github.com/jemalloc/jemalloc/pull/1117): [83aa988](https://github.com/jemalloc/jemalloc/commit/83aa9880b706ab185aa84f2bf6057477efdd5fd6)

## Routine Changes

### New features
- Filter out newImpl function in profiling output.
  ↳ [#968](https://github.com/jemalloc/jemalloc/pull/968): [2d2fa72](https://github.com/jemalloc/jemalloc/commit/2d2fa72647e0e535088793a0335d0294277d2f09)
- Skip mmap attempts when retain is enabled and in-place expansion is done.
  ↳ [#971](https://github.com/jemalloc/jemalloc/pull/971): [3800e55](https://github.com/jemalloc/jemalloc/commit/3800e55a2c6f4ffb03242db06437ad371db4ccd8)
- Added additional adaptation step for aligned allocations, searching across all potential size classes to improve memory reuse.
  ↳ [#1096](https://github.com/jemalloc/jemalloc/pull/1096): [ba5992f](https://github.com/jemalloc/jemalloc/commit/ba5992fe9ac1708c812ec65bff3270bba17f1e1b)
- Changed dlsym calls to be executed on demand to avoid being called at startup when lazy locks or background threads are not enabled.
  ↳ [#1171](https://github.com/jemalloc/jemalloc/pull/1171): [dedfeec](https://github.com/jemalloc/jemalloc/commit/dedfeecc4e69545efb2974ae42589985ed420821)

### bug fixes
- Fix test/unit/pages test to use runtime variables to check for MADV_HUGEPAGE support instead.
  ↳ [#986](https://github.com/jemalloc/jemalloc/pull/986): [3ec279b](https://github.com/jemalloc/jemalloc/commit/3ec279ba1c702286b2a7d4ce7aaf48d7905f1c5b) | [#1017](https://github.com/jemalloc/jemalloc/pull/1017): [886053b](https://github.com/jemalloc/jemalloc/commit/886053b966f4108e4b9ee5e29a0a708e91bc72f8)
- Fix compilation warning due to missing fields in rtree cache initializer.
  ↳ [#1022](https://github.com/jemalloc/jemalloc/pull/1022): [d60f3ba](https://github.com/jemalloc/jemalloc/commit/d60f3bac1237666922c16e7a1b281a2c7721863c)
- Delay the execution of background_thread_ctl_init and add lock-free assertion.
  ↳ [#1047](https://github.com/jemalloc/jemalloc/pull/1047): [a2e6eb2](https://github.com/jemalloc/jemalloc/commit/a2e6eb2c226ff63397220517883e13717f97da05)
- Fixed the synchronization problem of the base allocator when switching to THP in automatic mode, and corrected the statistics.
  ↳ [#1068](https://github.com/jemalloc/jemalloc/pull/1068): [cb3b72b](https://github.com/jemalloc/jemalloc/commit/cb3b72b9756d124565ed12e005065ad6f0769568)
- Fixed an issue where two extents were not correctly removed from the LRU list when merging extents.
  ↳ [#1071](https://github.com/jemalloc/jemalloc/pull/1071): [eb1b08d](https://github.com/jemalloc/jemalloc/commit/eb1b08daaea57d16ce720d97847d94cee2f867cc)
- Avoid incorrectly setting zero and commit flags when split fails in extent_recycle.
  ↳ [#1075](https://github.com/jemalloc/jemalloc/pull/1075): [e475d03](https://github.com/jemalloc/jemalloc/commit/e475d03752d53e198143fdf58e7d0e2e14e5f1a2)
- Fixed a regression problem that caused leakage due to not logging out the extent first when the extent was recycled and split.
  ↳ [#1076](https://github.com/jemalloc/jemalloc/pull/1076): [26a8f82](https://github.com/jemalloc/jemalloc/commit/26a8f82c484eada4188e56daad32ed6a16b4b585)
- Fix for incorrectly adjusting gdump counts on leak paths.
  ↳ [#1084](https://github.com/jemalloc/jemalloc/pull/1084): [955b1d9](https://github.com/jemalloc/jemalloc/commit/955b1d9cc574647d3d3dfb474b47b51b3a81453d)
- Add check whether tsdn is empty before reading reentrancy level.
  ↳ [#1097](https://github.com/jemalloc/jemalloc/pull/1097): [41790f4](https://github.com/jemalloc/jemalloc/commit/41790f4fa475434ea84b8509b9a68e63d9a86f95)
- Fixed the buffer overflow problem caused by index out-of-bounds in the background thread.
  ↳ [#1140](https://github.com/jemalloc/jemalloc/pull/1140): [26b1c13](https://github.com/jemalloc/jemalloc/commit/26b1c1398264dec25bf998f6bec21799ad4513da)
- Fix the background thread closing problem, ensure that thread 0 is always created, and correct the synchronization logic.
  ↳ [#1155](https://github.com/jemalloc/jemalloc/pull/1155): [21eb0d1](https://github.com/jemalloc/jemalloc/commit/21eb0d15a6cfdaee3aa78f724838b503053d7f00)
- Fixed the problem of using stack address to sort mutex locks, instead passing the pointer directly.
  ↳ [#1165](https://github.com/jemalloc/jemalloc/pull/1165): [5f51882](https://github.com/jemalloc/jemalloc/commit/5f51882a0a7d529c90bbb15ccbabb064b0a11e80)
- Fixed the resource leak problem in the path where extent split failed.
  ↳ [#1181](https://github.com/jemalloc/jemalloc/pull/1181): [c95284d](https://github.com/jemalloc/jemalloc/commit/c95284df1ab77f233562d9bc826523cfaaf7f41e)
- Fix abort_conf processing logic to ensure that an error is always reported and exited at the end of the option processing loop.
  ↳ [#1182](https://github.com/jemalloc/jemalloc/pull/1182): [e40b2f7](https://github.com/jemalloc/jemalloc/commit/e40b2f75bdfc830a9a53b2cad4fb7261d39cec93) | [#987](https://github.com/jemalloc/jemalloc/pull/987): [b082535](https://github.com/jemalloc/jemalloc/commit/b0825351d9eb49976164cff969a93877ac11f2c0)
- Removed false assertions to allow delayed creation of background threads in paused state.
  ↳ [#1185](https://github.com/jemalloc/jemalloc/pull/1185): [b8f4c73](https://github.com/jemalloc/jemalloc/commit/b8f4c730eff28edee4b583ff5b6ee1fac0f26c27)
- Fixed parameter passing error in extent_init call.
  ↳ [#1159](https://github.com/jemalloc/jemalloc/pull/1159): [4df483f](https://github.com/jemalloc/jemalloc/commit/4df483f0fd76a64e116b1c4f316f8b941078114d)
- Add falls through annotation in hash_x64_128 function to fix compilation warning.
  ↳ [#1029](https://github.com/jemalloc/jemalloc/pull/1029): [56f0e57](https://github.com/jemalloc/jemalloc/commit/56f0e57844bc1d2c806738860bf93e2ccee135b5)
- Adjust the order of keywords in static variable declaration and fix compilation warnings.
  ↳ [#1022](https://github.com/jemalloc/jemalloc/pull/1022): [eaa58a5](https://github.com/jemalloc/jemalloc/commit/eaa58a50267df6f5f2a5da38d654fd98fc4a1136)
- Modify the display of variable options in statistics output.
  ↳ [#1146](https://github.com/jemalloc/jemalloc/pull/1146): [956c4ad](https://github.com/jemalloc/jemalloc/commit/956c4ad6b57318bc7b6cd02bf9bfeb45afc4e3e2)

### Refactoring optimization
- Separated OOM processing logic from the hot path and optimized the inlining strategy.
  ↳ [#963](https://github.com/jemalloc/jemalloc/pull/963): [b28f31e](https://github.com/jemalloc/jemalloc/commit/b28f31e7ed6c987bdbf3bdd9ce4aa63245926b4d)
- Extract the core logic of extent splitting into independent functions, separating the responsibilities of splitting and returning.
  ↳ [#1052](https://github.com/jemalloc/jemalloc/pull/1052): [211b1f3](https://github.com/jemalloc/jemalloc/commit/211b1f3c7de23b1915f1ce8f9277e6c1ff60cfde)
- Replaced extents_avail_ data structure from red-black tree to paired heap, simplifying implementation.
  ↳ [#1039](https://github.com/jemalloc/jemalloc/pull/1039): [7c6c99b](https://github.com/jemalloc/jemalloc/commit/7c6c99b8295829580c506067495a23c07436e266)
- Manually set the isthreaded variable to avoid pthread_once initialization dependency issues.
  ↳ [#1047](https://github.com/jemalloc/jemalloc/pull/1047): [7e74093](https://github.com/jemalloc/jemalloc/commit/7e74093c96c019ce52aee9a03fc745647d79ca5f)
- Optimize the dirty page allocation strategy and use the first element of the heap to reduce memory fragmentation.
  ↳ [#1071](https://github.com/jemalloc/jemalloc/pull/1071): [282a3fa](https://github.com/jemalloc/jemalloc/commit/282a3faa1784783e2e2cb3698183927b3927b950)
- Reconstruct extent_t bit packing logic and use macro definition based on preorder field width and shift instead.
  ↳ [#1103](https://github.com/jemalloc/jemalloc/pull/1103): [72bdbc3](https://github.com/jemalloc/jemalloc/commit/72bdbc35e3231db91def5f466d41778ee04d7e64)
- Removed preserve_lru feature, merged extents are now always added to the LRU list.
  ↳ [#1154](https://github.com/jemalloc/jemalloc/pull/1154): [6d02421](https://github.com/jemalloc/jemalloc/commit/6d02421730e2f2dc6985da699b8e10b3ed4061b6)
- Added comment documentation for the internal extent function and renamed extent_deregister to extent_deregister_impl.
  ↳ [#1052](https://github.com/jemalloc/jemalloc/pull/1052): [5bad01c](https://github.com/jemalloc/jemalloc/commit/5bad01c38ed0b1f647a6984c5f830b124cafdc94)
- Fixed compiler warnings and adjusted parameter passing of memory release related functions.
  ↳ [#1167](https://github.com/jemalloc/jemalloc/pull/1167): [4937309](https://github.com/jemalloc/jemalloc/commit/49373096206964c3d60c1deaa75dcab6e90b7f59)

### Test related
- Change sdallocx in integration tests to run in non-reentrant mode to avoid running out of memory.
  ↳ [#965](https://github.com/jemalloc/jemalloc/pull/965): [7c22ea7](https://github.com/jemalloc/jemalloc/commit/7c22ea7a93f16c90f49de8ee226e3bcd1521c93e)
- Added new tests for failure paths of extent hooks, added address continuity assertions, and expanded manual hook tests to cover multiple failure scenarios.
  ↳ [#1079](https://github.com/jemalloc/jemalloc/pull/1079): [6e841f6](https://github.com/jemalloc/jemalloc/commit/6e841f618a5ff99001a9578e9ff73602e7a94620)
- Fix the condition of the extent test in the integration test to ensure that the hook test only runs when the background thread is not enabled.
  ↳ [#1084](https://github.com/jemalloc/jemalloc/pull/1084): [b5ab3f9](https://github.com/jemalloc/jemalloc/commit/b5ab3f91ea60b16819563b09aa01a0d339aa40b4)
- Skip test/unit/pack test when profiling is enabled, as this test assumes no sample distribution.
  ↳ [#1086](https://github.com/jemalloc/jemalloc/pull/1086): [f70785d](https://github.com/jemalloc/jemalloc/commit/f70785de91ee14e8034f9bd64bf6590199c89e65)
- Removed unused code in test file thread_tcache_enabled.c.
  ↳ [#1110](https://github.com/jemalloc/jemalloc/pull/1110): [548153e](https://github.com/jemalloc/jemalloc/commit/548153e789580a3a943cc564c7d95fb0523e8b19)
- Add conditional judgment in test_alignment_and_size test, skip this test when percpu_arena is enabled to avoid insufficient memory.
  ↳ [#1110](https://github.com/jemalloc/jemalloc/pull/1110): [6b35366](https://github.com/jemalloc/jemalloc/commit/6b35366ef55bb5987c7ac91e1c100e9e55ef15cc)
- Fixed compilation warnings caused by mismatched const qualifiers and added explicit type conversion in mallctl calls.
  ↳ [#1158](https://github.com/jemalloc/jemalloc/pull/1158): [cf2f4aa](https://github.com/jemalloc/jemalloc/commit/cf2f4aac1ca8c7d48a61a3921335fb411a3943a4)

### Performance optimization
- Use getpagesize(3) and sysctl(3) on FreeBSD to replace old system calls, reduce the number of system calls during binary startup, and improve startup performance.
  ↳ [#1061](https://github.com/jemalloc/jemalloc/pull/1061): [d591df0](https://github.com/jemalloc/jemalloc/commit/d591df05c86e89c0a5db98274bc7f280f910a0de), [9f455e2](https://github.com/jemalloc/jemalloc/commit/9f455e2786685b443201c33119765c8093461174)
- Changed PRNG status from atomic variables to thread-local variables to reduce cache line contention.
  ↳ [#1070](https://github.com/jemalloc/jemalloc/pull/1070): [d6feed6](https://github.com/jemalloc/jemalloc/commit/d6feed6e6631d00806607cfe16a796e337752044)
- Adjust the ticker path, which will fix the logic outsourcing to help GCC generate better code.
  ↳ [#1131](https://github.com/jemalloc/jemalloc/pull/1131): [dd7e283](https://github.com/jemalloc/jemalloc/commit/dd7e283b6f7f18054af3e14457251757945ab17d)
- Combine two memory reads in rtree_szind_slab_read(), manually manipulate bits to avoid extra memory loading, and optimize fast path performance.
  ↳ [#1157](https://github.com/jemalloc/jemalloc/pull/1157): [4be74d5](https://github.com/jemalloc/jemalloc/commit/4be74d51121e8772d356e8be088dc93f927fd709)

### Security related
- Added file descriptor validity check before calling fcntl.
  ↳ [#961](https://github.com/jemalloc/jemalloc/pull/961): [aa6c282](https://github.com/jemalloc/jemalloc/commit/aa6c2821374f6dd6ed2e628c06bc08b0c4bc485c)

### Documentation
- Added documentation comments for naming abbreviations for the ialloc family of functions, and corrected comments on cache exhaustion status in cache_bin.
  ↳ [#989](https://github.com/jemalloc/jemalloc/pull/989): [ea91dfa](https://github.com/jemalloc/jemalloc/commit/ea91dfa58e11373748f747041c3041f72c9a7658)
- Supplementary note: Enabling the opt.background_thread option may cause initialization crashes or deadlocks due to cyclic dependencies. It is recommended to use dynamic control instead.
  ↳ [#1050](https://github.com/jemalloc/jemalloc/pull/1050): [fc83de0](https://github.com/jemalloc/jemalloc/commit/fc83de0384a2ad87cf5059d4345acf014c77e6e4)
- Removed documentation for the deleted --disable-thp option.
  ↳ [#1179](https://github.com/jemalloc/jemalloc/pull/1179): [3bcaede](https://github.com/jemalloc/jemalloc/commit/3bcaedeea285edcf6006cbd12b906bd3dc11a8ba)
- Documented that the extent_hooks_t structure must remain valid throughout the lifetime of the associated arena.
  ↳ [#1172](https://github.com/jemalloc/jemalloc/pull/1172): [0258542](https://github.com/jemalloc/jemalloc/commit/02585420c34e08db1de4c26f3d5bc808d6910131)
- Added performance tuning document TUNING.md.
  ↳ [#1179](https://github.com/jemalloc/jemalloc/pull/1179): [2e7af1a](https://github.com/jemalloc/jemalloc/commit/2e7af1af733144b58e4977f526f11d015d8457b0)
- Updated ChangeLog to record release notes for version 5.1.0.
  ↳ [#1204](https://github.com/jemalloc/jemalloc/pull/1204): [1c51381](https://github.com/jemalloc/jemalloc/commit/1c51381b7cc62b6e0e77d02c42925c3776dbc4a2)

### Build/CI
- Adjusted the processing of catgets dependencies in the AppVeyor CI configuration, and fixed the configuration error in the msys2 environment.
  ↳ [#1132](https://github.com/jemalloc/jemalloc/pull/1132): [ae0f5d5](https://github.com/jemalloc/jemalloc/commit/ae0f5d5c3f29beb9977148dedb58575757139586) | [#1147](https://github.com/jemalloc/jemalloc/pull/1147): [742416f](https://github.com/jemalloc/jemalloc/commit/742416f64571e7a0b1d75ad116bc9f1794e67c1c)
- The build system has added compile-time detection of madvise's MADV_DONTDUMP and MADV_DODUMP parameters.
  ↳ [#1052](https://github.com/jemalloc/jemalloc/pull/1052): [ccd0905](https://github.com/jemalloc/jemalloc/commit/ccd09050aa53d083fe0b45d4704b1fe95fb00c92)
- Travis CI environment forces Ubuntu precise to resolve build errors.
  ↳ [#1025](https://github.com/jemalloc/jemalloc/pull/1025): [9e39425](https://github.com/jemalloc/jemalloc/commit/9e39425bf1653e4bebb7b377dd716f98cab069ff)
- Removed default value for JEMALLOC_PURGE_MADVISE_DONTNEED_ZEROS macro.
  ↳ [#1048](https://github.com/jemalloc/jemalloc/pull/1048): [f4f814c](https://github.com/jemalloc/jemalloc/commit/f4f814cd4cca4be270c22c4e943cd5ae6c40fea9)
- Fixed an issue where the JE_CXXFLAGS_ADD macro was not being used by the C++ compiler when compiling the check.
  ↳ [#1101](https://github.com/jemalloc/jemalloc/pull/1101): [78a87e4](https://github.com/jemalloc/jemalloc/commit/78a87e4a80e9bf379c0dc660374173ef394252f6)
- Added install_lib_pc installation target to the installation documentation.
  ↳ [#1188](https://github.com/jemalloc/jemalloc/pull/1188): [39b1b20](https://github.com/jemalloc/jemalloc/commit/39b1b2049934be5be7e5b1b6f77ff31cd02398c5)

### Maintenance
- Adjusted the metadata huge page alignment strategy of the base allocator, set a higher switching threshold for arena 0 (the 5th base block), and simplified the alignment judgment method of metadata allocation.
  ↳ [#1062](https://github.com/jemalloc/jemalloc/pull/1062): [58eba02](https://github.com/jemalloc/jemalloc/commit/58eba024c0fbda463eaf8b42772407894dba6eff) | [#1065](https://github.com/jemalloc/jemalloc/pull/1065): [6dd5681](https://github.com/jemalloc/jemalloc/commit/6dd5681ab787b4153ad2fa425be72efece42d3c7)
- Updated MSVC project files to support Visual Studio 2017, and updated build instructions.
  ↳ [#1053](https://github.com/jemalloc/jemalloc/pull/1053): [33df2fa](https://github.com/jemalloc/jemalloc/commit/33df2fa1694c9fdc1912aecaa19babc194f377ac)
- Added UNUSED flags to multiple function parameters to avoid compiler warnings, and cleaned up parameter lists for some functions.
  ↳ [#1178](https://github.com/jemalloc/jemalloc/pull/1178): [0fadf4a](https://github.com/jemalloc/jemalloc/commit/0fadf4a2e3e629b9fa43888f9754aea5327d038f)
- bin mutex statistics now output all counters, including the previously omitted owner_switch and max_num_thds fields.
  ↳ [#1055](https://github.com/jemalloc/jemalloc/pull/1055): [47203d5](https://github.com/jemalloc/jemalloc/commit/47203d5f422452def4cb29c0b7128cc068031100)
- Removed unused config.thp configuration items and related code.
  ↳ [#1134](https://github.com/jemalloc/jemalloc/pull/1134): [efa4053](https://github.com/jemalloc/jemalloc/commit/efa40532dc0fc000345086757ecaf8875313a012)

### Others
- Optimized the release performance of unpage-aligned pointers to avoid unnecessary rtree access.
  ↳ [#972](https://github.com/jemalloc/jemalloc/pull/972): [1ab2ab2](https://github.com/jemalloc/jemalloc/commit/1ab2ab294c8f29a6f314f3ff30fbf4cdb2f01af6)
- Aggressively merge large extents to reduce fragmentation and improve locality.
  ↳ [#1071](https://github.com/jemalloc/jemalloc/pull/1071): [3e64dae](https://github.com/jemalloc/jemalloc/commit/3e64dae802b9f7cd4f860b0d29126cd727d5166b)
- Filter out void *newImpl in profiling output.
  ↳ [#977](https://github.com/jemalloc/jemalloc/pull/977): [d157864](https://github.com/jemalloc/jemalloc/commit/d157864027562dc17475edfd1bc6dce559b7ac4b)
- Added opt.lg_extent_max_active_fit option to statistics output.
  ↳ [#1089](https://github.com/jemalloc/jemalloc/pull/1089): [5e03328](https://github.com/jemalloc/jemalloc/commit/5e0332890f8e553e148b8c4b0130d84037339e6a)
- Removed an extra newline character in statistics printing.
  ↳ [#1144](https://github.com/jemalloc/jemalloc/pull/1144): [a9f3ced](https://github.com/jemalloc/jemalloc/commit/a9f3cedc6ed6e923854edc5feddd42a39941f01c)
- Fixed two spelling errors in ChangeLog.
  ↳ [#947](https://github.com/jemalloc/jemalloc/pull/947): [aa44ddb](https://github.com/jemalloc/jemalloc/commit/aa44ddbcdd43cc8a8352b654f4a003d83b9c15b7) | [#1166](https://github.com/jemalloc/jemalloc/pull/1166): [cad27a8](https://github.com/jemalloc/jemalloc/commit/cad27a894a2e043f3c1189201d6ff34a195dc658)
- Clean up extra whitespace characters in configure.ac.
  ↳ [#1024](https://github.com/jemalloc/jemalloc/pull/1024): [96f1468](https://github.com/jemalloc/jemalloc/commit/96f1468221b9e846dd70eb7e65634a41e6804c20) | No PR: [f9dfb8d](https://github.com/jemalloc/jemalloc/commit/f9dfb8db73064e2bb3735d4b288168e722191fdd)
- Removed duplicate test configuration options in test script gen_run_tests.py.
  ↳ [#973](https://github.com/jemalloc/jemalloc/pull/973): [9a39b23](https://github.com/jemalloc/jemalloc/commit/9a39b23c9c823e8157e2e6850014fa67c09f9351)
- Fix wrong link for dirty_decay_ms in manual.
  ↳ [#1012](https://github.com/jemalloc/jemalloc/pull/1012): [cf47384](https://github.com/jemalloc/jemalloc/commit/cf4738455d990918914cdc8608936433ef897a6e)
- Fixed a typo in a key name in statistics output.
  ↳ [#1146](https://github.com/jemalloc/jemalloc/pull/1146): [baffeb1](https://github.com/jemalloc/jemalloc/commit/baffeb1d0ab45e0bcaad7f326d9028372e2cb000)
- Fixed a typo in configure.ac file.
  ↳ [#1170](https://github.com/jemalloc/jemalloc/pull/1170): [f0b146a](https://github.com/jemalloc/jemalloc/commit/f0b146acc4d48d1d829a8099aee7bc91267d8209)
- Fixed a spelling error in INSTALL.md.
  ↳ [#1197](https://github.com/jemalloc/jemalloc/pull/1197): [c5b72a9](https://github.com/jemalloc/jemalloc/commit/c5b72a92cc40a0f95e13cb3e3bb4fba0f7ef36c3)
- Update copyright year in COPYING files.
  ↳ [#1205](https://github.com/jemalloc/jemalloc/pull/1205): [95789a2](https://github.com/jemalloc/jemalloc/commit/95789a24fab056e7a1ddc66e2366b1ec88aa2bcd)
