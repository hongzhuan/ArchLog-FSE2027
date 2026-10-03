# Release Note

## Important Changes

### Allocation Policy & Management Layer

- Added opt.metadata_thp configuration to control transparent huge page usage for base allocator metadata, providing disabled/auto/always modes, related statistics, and fixing auto mode handling of a0 allocation, locking, and statistics. [commit](https://github.com/jemalloc/jemalloc/commit/8fdd9a579779b84d6af27f94c295f82a4df8e5be) [commit](https://github.com/jemalloc/jemalloc/commit/47b20bb6544de9cdd4ca7ab870d6ad257c0ce4ff) [commit](https://github.com/jemalloc/jemalloc/commit/e55c3ca26758bcb7f6f1621fd690caa245f16942) [commit](https://github.com/jemalloc/jemalloc/commit/79e83451ff262fbc4bf66059eae672286b5eb9f0) [commit](https://github.com/jemalloc/jemalloc/commit/58eba024c0fbda463eaf8b42772407894dba6eff) [commit](https://github.com/jemalloc/jemalloc/commit/cb3b72b9756d124565ed12e005065ad6f0769568)
- Added opt.thp configuration to explicitly select always/never transparent huge page policy for user mappings; removed unused config.thp. [commit](https://github.com/jemalloc/jemalloc/commit/efa40532dc0fc000345086757ecaf8875313a012) [commit](https://github.com/jemalloc/jemalloc/commit/e4f090e8df5adf180662c5eeac2af214f9594de4)
- Added arena.i.retain_grow_limit mallctl to allow limiting the growth of retained extents. [commit](https://github.com/jemalloc/jemalloc/commit/e422fa8e7ea749ab8c4783e405c0f4b19ac25db9)
- Added opt.lg_extent_max_active_fit configuration and report this value in statistics output. [commit](https://github.com/jemalloc/jemalloc/commit/fac706836ffda46759914508b918e8b54c8020c8) [commit](https://github.com/jemalloc/jemalloc/commit/5e0332890f8e553e148b8c4b0130d84037339e6a)
- Added maximum number of background threads configuration. [commit](https://github.com/jemalloc/jemalloc/commit/8b14f3abc05f01419f9321a6a65ab9dd68dcebac)
- Extent allocator now uses pairing heap to maintain available extents and supports best-fit search; improved matching for aligned allocations. [commit](https://github.com/jemalloc/jemalloc/commit/282a3faa1784783e2e2cb3698183927b3927b950) [commit](https://github.com/jemalloc/jemalloc/commit/ba5992fe9ac1708c812ec65bff3270bba17f1e1b)
- Fixed extent coalesce, split/recycle, leak, and purge boundary issues; improved eager coalesce for large extents and avoided purging one extra extent. [commit](https://github.com/jemalloc/jemalloc/commit/eb1b08daaea57d16ce720d97847d94cee2f867cc) [commit](https://github.com/jemalloc/jemalloc/commit/3e64dae802b9f7cd4f860b0d29126cd727d5166b) [commit](https://github.com/jemalloc/jemalloc/commit/e475d03752d53e198143fdf58e7d0e2e14e5f1a2) [commit](https://github.com/jemalloc/jemalloc/commit/26a8f82c484eada4188e56daad32ed6a16b4b585) [commit](https://github.com/jemalloc/jemalloc/commit/955b1d9cc574647d3d3dfb474b47b51b3a81453d) [commit](https://github.com/jemalloc/jemalloc/commit/740bdd68b1d4b9c39c68432e06deb70ad4da3210) [commit](https://github.com/jemalloc/jemalloc/commit/c95284df1ab77f233562d9bc826523cfaaf7f41e)
- Allow setting extent hooks on uninitialized automatic arenas and relax reentrancy restrictions for extent hooks; document the lifetime requirements of extent_hooks_t objects. [commit](https://github.com/jemalloc/jemalloc/commit/a315688be0f38188f16fe89ee1657c7f596f8cbb) [commit](https://github.com/jemalloc/jemalloc/commit/02585420c34e08db1de4c26f3d5bc808d6910131) [commit](https://github.com/jemalloc/jemalloc/commit/3f0dc64c6b8c1fd77c819028013dacbc6d2ad6b6)

### Cross-cutting / Other Architecture-related Changes

- Added MADV_DONTDUMP detection and pages_dontdump/pages_dodump interfaces to control whether jemalloc pages are written to core dumps via extent dumpable state. [commit](https://github.com/jemalloc/jemalloc/commit/ccd09050aa53d083fe0b45d4704b1fe95fb00c92) [commit](https://github.com/jemalloc/jemalloc/commit/bbaa72422bb086933890a125fd58bf199fe26f2d) [commit](https://github.com/jemalloc/jemalloc/commit/d14bbf8d8190df411f0daf182f73f7b7786288c4)
- Added architecture recognition support for m68k, nios2, SH3, and RISC-V, and added ILP32 address space configuration for AArch64. [commit](https://github.com/jemalloc/jemalloc/commit/82d1a3fb318fb086cd4207ca03dbdd5b0e3bbb26) [commit](https://github.com/jemalloc/jemalloc/commit/749caf14ae73a9ab1c48e538a8af09addbb35ee7) [commit](https://github.com/jemalloc/jemalloc/commit/6df90600a7e4df51b06efe2d47df211cba5935a7)

### User-Facing Interface Layer

- Introduced hierarchical logging facility to record entry and exit in core allocation/deallocation APIs, and improved empty variadic arguments, variable name output, and log macro naming. [commit](https://github.com/jemalloc/jemalloc/commit/9761b449c8c6b70abdb4cfa953e59847a84af406) [commit](https://github.com/jemalloc/jemalloc/commit/e215a7bc18a2c3263a6fcca37c1ec53af6c4babd) [commit](https://github.com/jemalloc/jemalloc/commit/a9f7732d45c22ca7d22bed6ff2eaeb702356884e) [commit](https://github.com/jemalloc/jemalloc/commit/e6aeceb6068ace14ca530506fdfeb5f1cadd9a19) [commit](https://github.com/jemalloc/jemalloc/commit/8a7ee3014cea09e13e605bf47c11943df5a5eb2b)
- Introduced emitter structured output module and migrated stats printing to emitter, supporting JSON and table row output. [commit](https://github.com/jemalloc/jemalloc/commit/27a8fe6780cb901668489495b2fc302a2d071d8c) [commit](https://github.com/jemalloc/jemalloc/commit/b646f89173be53d4f5eb59a894dbcdd64b457bee) [commit](https://github.com/jemalloc/jemalloc/commit/4a335e0c6f6fa371edcd7663eebfe11cf93a1f17) [commit](https://github.com/jemalloc/jemalloc/commit/e5acc3540011fc6c3cec6aa97c567ff280617b74) [commit](https://github.com/jemalloc/jemalloc/commit/ec31d476ffa36885182f2b569ee518d3dfd54761) [commit](https://github.com/jemalloc/jemalloc/commit/0d20eda127c4f35c16cfffad15857d3b286166ba) [commit](https://github.com/jemalloc/jemalloc/commit/8076b28721e16d14a8a81bb6c17fba804812e110) [commit](https://github.com/jemalloc/jemalloc/commit/9e1846b0041e29a331ecf76e9b23ddb730bc352f) [commit](https://github.com/jemalloc/jemalloc/commit/ebe0b5f8283b542f59cbe77f69e24935ebb5f866) [commit](https://github.com/jemalloc/jemalloc/commit/86c61d4a575e7eb57ade8a39e9d552d95c63aa31) [commit](https://github.com/jemalloc/jemalloc/commit/cbde666d9a5a2bf1cb741661aebec228aa9f5827) [commit](https://github.com/jemalloc/jemalloc/commit/a6ef061c4309852a8bb27c5374edb1bc6980ac06) [commit](https://github.com/jemalloc/jemalloc/commit/bc6620f73e205004b2dfaf0438daeab617609295) [commit](https://github.com/jemalloc/jemalloc/commit/8fc850695dc70958cfeffd53e9d5df261697cff5) [commit](https://github.com/jemalloc/jemalloc/commit/07fb707623de5da5b58c448683a3f71df67531c9) [commit](https://github.com/jemalloc/jemalloc/commit/a1738f4efd7cfdaec576e54df90422e36cc6a8df) [commit](https://github.com/jemalloc/jemalloc/commit/a9f3cedc6ed6e923854edc5feddd42a39941f01c) [commit](https://github.com/jemalloc/jemalloc/commit/4eed989bbfb7c56bdea97169ca07f9a7b7f14f27) [commit](https://github.com/jemalloc/jemalloc/commit/4c36cd2cc5c6ac7f27354b84606b0ca4d6178791)
- Added --with-lg-vaddr configure option to override virtual address bit configuration, and supplemented INSTALL instructions and corresponding tests. [commit](https://github.com/jemalloc/jemalloc/commit/63712b4c4e046e9d91807d0e1b5c890c52925379) [commit](https://github.com/jemalloc/jemalloc/commit/b001e6e7407cd7e07bad533445eee7f0224cb268) [commit](https://github.com/jemalloc/jemalloc/commit/4c8829e6924ee7abae6f41ca57303a88dd6f1315)
- Added TUNING.md documenting jemalloc usage and tuning recommendations. [commit](https://github.com/jemalloc/jemalloc/commit/2e7af1af733144b58e4977f526f11d015d8457b0)

## Routine Changelog

### New Features

- Added --disable-initial-exec-tls configure option to allow disabling the initial-exec TLS model. [commit](https://github.com/jemalloc/jemalloc/commit/a62e42baebe09dc84aaff731faa6ff87fde6bc4e)

### Bug Fixes

- Fixed deadlock on macOS when forking multithreaded processes and added corresponding behavior tests. [commit](https://github.com/jemalloc/jemalloc/commit/0a4f5a7eea5e42292cea95fd30a88201c8d4a1ca) [commit](https://github.com/jemalloc/jemalloc/commit/fb6787a78c3a1e3a4868520d0531fc2ebdda21d8)
- When O_CLOEXEC is unavailable, fall back to fcntl to set FD_CLOEXEC, and check the file descriptor before calling fcntl. [commit](https://github.com/jemalloc/jemalloc/commit/0975b88dfd3a890f469c8c282a5140013af85ab2) [commit](https://github.com/jemalloc/jemalloc/commit/aa6c2821374f6dd6ed2e628c06bc08b0c4bc485c)
- Fixed jemalloc_mangle.sh incorrectly calling the extent wrapper path when no_move_expand is configured. [commit](https://github.com/jemalloc/jemalloc/commit/3800e55a2c6f4ffb03242db06437ad371db4ccd8)
- Fixed sdallocx handling of szind for page-aligned pointers. [commit](https://github.com/jemalloc/jemalloc/commit/1ab2ab294c8f29a6f314f3ff30fbf4cdb2f01af6)
- After fork, clear the cache bin queue to fix errors caused by leftover cache state. [commit](https://github.com/jemalloc/jemalloc/commit/9b20a4bf70efd675604985ca37335f8b0136a289)
- At runtime, detect whether the system supports lazy purge and correctly fall back when not supported. [commit](https://github.com/jemalloc/jemalloc/commit/0720192a323f5dd2dd27828c6ab3061f8f039416)
- Fixed ARM high address bit calculation to avoid incorrect sign extension. [commit](https://github.com/jemalloc/jemalloc/commit/7a8bc7172b17e219b3603e99c8da44efb283e652)
- Adjusted the initialization timing of background thread control and explicitly maintain isthreaded state to avoid dependencies during initialization. [commit](https://github.com/jemalloc/jemalloc/commit/a2e6eb2c226ff63397220517883e13717f97da05) [commit](https://github.com/jemalloc/jemalloc/commit/7e74093c96c019ce52aee9a03fc745647d79ca5f)
- Fixed unbounded growth of stash_decayed. [commit](https://github.com/jemalloc/jemalloc/commit/b5d071c26697813bcceae320ba88dee2a2a73e51)
- Handle 32-bit mutex profile counting and refactor extent_t bit packing logic. [commit](https://github.com/jemalloc/jemalloc/commit/f47e39d11a0e7ef4201a1ac18efa7604c5152aa3) [commit](https://github.com/jemalloc/jemalloc/commit/72bdbc35e3231db91def5f466d41778ee04d7e64)
- Avoid checking lock rank in reentrancy scenarios and verify tsdn_null before reading reentrancy level. [commit](https://github.com/jemalloc/jemalloc/commit/91b247d311ce6837aa93d4315f5f7680abd8a11a) [commit](https://github.com/jemalloc/jemalloc/commit/41790f4fa475434ea84b8509b9a68e63d9a86f95)
- Fixed background thread index errors and synchronization issues during shutdown. [commit](https://github.com/jemalloc/jemalloc/commit/26b1c1398264dec25bf998f6bec21799ad4513da) [commit](https://github.com/jemalloc/jemalloc/commit/21eb0d15a6cfdaee3aa78f724838b503053d7f00)
- Only execute idump/gdump control logic when prof_active is effective. [commit](https://github.com/jemalloc/jemalloc/commit/2dccf4564016233bd4ef7772b43ec8423b8c44df)
- Corrected extent_init parameters and removed erroneous assertions in the paused state of background threads without global locks. [commit](https://github.com/jemalloc/jemalloc/commit/4df483f0fd76a64e116b1c4f316f8b941078114d) [commit](https://github.com/jemalloc/jemalloc/commit/b8f4c730eff28edee4b583ff5b6ee1fac0f26c27)
- Fixed the issue of sorting mutexes by stack address to avoid unstable address ordering. [commit](https://github.com/jemalloc/jemalloc/commit/5f51882a0a7d529c90bbb15ccbabb064b0a11e80)
- Fixed the issue where abort_conf configuration did not guarantee exiting with an error. [commit](https://github.com/jemalloc/jemalloc/commit/e40b2f75bdfc830a9a53b2cad4fb7261d39cec93)
- Fixed spelling errors in stats output and fixed stringify compatibility for mutable option output. [commit](https://github.com/jemalloc/jemalloc/commit/baffeb1d0ab45e0bcaad7f326d9028372e2cb000) [commit](https://github.com/jemalloc/jemalloc/commit/956c4ad6b57318bc7b6cd02bf9bfeb45afc4e3e2)

### Refactoring

- Moved bin cache to a separate cache_bin module and let arena stats be collected through cache bins. [commit](https://github.com/jemalloc/jemalloc/commit/f3170baa30654b2f62547fa1ac80707d396e1245) [commit](https://github.com/jemalloc/jemalloc/commit/9c0549007dcb64f4ff35d37390a9a6a8d3cea880)
- Split the core extent split logic from extent lifecycle management. [commit](https://github.com/jemalloc/jemalloc/commit/211b1f3c7de23b1915f1ce8f9277e6c1ff60cfde)
- Use TSD offset_state instead of atomic variables. [commit](https://github.com/jemalloc/jemalloc/commit/d6feed6e6631d00806607cfe16a796e337752044)
- Split arena bin type, initialization, fork, and statistics logic into a separate bin module and unified cache-bin/stat naming. [commit](https://github.com/jemalloc/jemalloc/commit/4bf4a1c4ea418ba490d35d23aee0f535e96ddd23) [commit](https://github.com/jemalloc/jemalloc/commit/a8dd8876fb483f402833fa05f0fb46fe7c5416e1) [commit](https://github.com/jemalloc/jemalloc/commit/48bb4a056be97214fa049f21bead9618429c807a) [commit](https://github.com/jemalloc/jemalloc/commit/8aafa270fd56c36db374fa9f294217fa80151b3d) [commit](https://github.com/jemalloc/jemalloc/commit/901d94a2b06df09c960836901f6a81a0d3d00732) [commit](https://github.com/jemalloc/jemalloc/commit/7f1b02e3fa9de7e0bb5e2562994b5ab3b82c0ec3)

### Tests

- Fixed pages unit tests and correctly handle test scenarios when huge pages are unavailable. [commit](https://github.com/jemalloc/jemalloc/commit/3ec279ba1c702286b2a7d4ce7aaf48d7905f1c5b) [commit](https://github.com/jemalloc/jemalloc/commit/886053b966f4108e4b9ee5e29a0a708e91bc72f8)
- Restricted sdallocx integration tests to non-reentrant runs as a temporary workaround for the current test environment. [commit](https://github.com/jemalloc/jemalloc/commit/7c22ea7a93f16c90f49de8ee226e3bcd1521c93e)
- Added abort_conf mallctl unit tests. [commit](https://github.com/jemalloc/jemalloc/commit/b0825351d9eb49976164cff969a93877ac11f2c0)
- Added coverage for extent hooks failure paths and fixed extent integration tests. [commit](https://github.com/jemalloc/jemalloc/commit/6e841f618a5ff99001a9578e9ff73602e7a94620) [commit](https://github.com/jemalloc/jemalloc/commit/b5ab3f91ea60b16819563b09aa01a0d339aa40b4)
- Skip inapplicable pack unit tests when profiling is enabled. [commit](https://github.com/jemalloc/jemalloc/commit/f70785de91ee14e8034f9bd64bf6590199c89e65)
- Removed unused thread_tcache_enabled test code; skip high memory overhead alignment/size tests when percpu_arena is enabled. [commit](https://github.com/jemalloc/jemalloc/commit/6b35366ef55bb5987c7ac91e1c100e9e55ef15cc)
- Added mallctl unit tests for arenas.lookup. [commit](https://github.com/jemalloc/jemalloc/commit/a32b7bd5676e669821d15d319f686c3add451f4b)
- In 32-bit tests, skip unsupported large virtual address configurations. [commit](https://github.com/jemalloc/jemalloc/commit/e94ca7f3e2b0ef393d713e7287b7f6b61645322b)

### Performance

- Split the OOM cold path of newImpl to avoid inlining the entire function. [commit](https://github.com/jemalloc/jemalloc/commit/b28f31e7ed6c987bdbf3bdd9ce4aa63245926b4d)
- Replace the red-black tree of available extents with a pairing heap, and use the heap head for best-fit search. [commit](https://github.com/jemalloc/jemalloc/commit/7c6c99b8295829580c506067495a23c07436e266)
- Disable the inapplicable CPU_SPINWAIT macro on Power architecture. [commit](https://github.com/jemalloc/jemalloc/commit/1245faae9052350a96dbcb22de7979bca566dbec)
- Output all statistics counters of the bin mutex. [commit](https://github.com/jemalloc/jemalloc/commit/47203d5f422452def4cb29c0b7128cc068031100)
- Align the base allocator to hugepage boundaries. [commit](https://github.com/jemalloc/jemalloc/commit/6dd5681ab787b4153ad2fa425be72efece42d3c7)
- Add a dynamic division div module and use it for arena region index calculation. [commit](https://github.com/jemalloc/jemalloc/commit/21f7c13d0b172dac6ea76236bbe0a2f3ee4bcb7b) [commit](https://github.com/jemalloc/jemalloc/commit/d41b19f9c70c9dd8244e0879c7aef7943a34c750)
- Adjust the ticker path to help GCC generate more efficient code. [commit](https://github.com/jemalloc/jemalloc/commit/dd7e283b6f7f18054af3e14457251757945ab17d)
- Merge two memory loads in the rtree slab size-index fast path. [commit](https://github.com/jemalloc/jemalloc/commit/4be74d51121e8772d356e8be088dc93f927fd709)
- Call dlsym() only when needed, avoiding pthread_create symbol resolution when lazy lock or background threads are not enabled. [commit](https://github.com/jemalloc/jemalloc/commit/dedfeecc4e69545efb2974ae42589985ed420821)

### Documentation

- Clarify the abbreviation of the internal ialloc function. [commit](https://github.com/jemalloc/jemalloc/commit/ea91dfa58e11373748f747041c3041f72c9a7658)
- Fix the link for dirty_decay_ms in the manual. [commit](https://github.com/jemalloc/jemalloc/commit/cf4738455d990918914cdc8608936433ef897a6e)
- Clarify potential issues with opt.background_thread. [commit](https://github.com/jemalloc/jemalloc/commit/fc83de0384a2ad87cf5059d4345acf014c77e6e4)
- Add explanations for internal extent functions. [commit](https://github.com/jemalloc/jemalloc/commit/5bad01c38ed0b1f647a6984c5f830b124cafdc94)
- Fix the INSTALL document regarding the removed --disable-thp option. [commit](https://github.com/jemalloc/jemalloc/commit/3bcaedeea285edcf6006cbd12b906bd3dc11a8ba)

### Build / CI

- Fix the configuration that incorrectly depends on dumpbin under MinGW, and allow the toolchain to select nm; the latter two identical patches are treated as the same configuration fix. [commit](https://github.com/jemalloc/jemalloc/commit/ef55006c1d324692408eed87421f486812d3645d) [commit](https://github.com/jemalloc/jemalloc/commit/3f5049340e66c6929c3270f7359617f62e053b11) [commit](https://github.com/jemalloc/jemalloc/commit/24766ccd5bcc379b7d518b3ec2480d2d146873ac) [commit](https://github.com/jemalloc/jemalloc/commit/a545f1804a19f48244ee5e328e32e2d036ffea0d)
- Support GNU/kFreeBSD configuration. [commit](https://github.com/jemalloc/jemalloc/commit/8da69b69e6c4cd951832138780ac632e57987b7c)
- Pin Travis CI to Ubuntu precise to avoid anomalies from CI environment upgrades. [commit](https://github.com/jemalloc/jemalloc/commit/9e39425bf1653e4bebb7b377dd716f98cab069ff)
- Complete missing fields in rtree cache initialization, and fix declaration order, fall-through, negative left shift, and other compilation warnings/undefined behavior. [commit](https://github.com/jemalloc/jemalloc/commit/d60f3bac1237666922c16e7a1b281a2c7721863c) [commit](https://github.com/jemalloc/jemalloc/commit/eaa58a50267df6f5f2a5da38d654fd98fc4a1136) [commit](https://github.com/jemalloc/jemalloc/commit/56f0e57844bc1d2c806738860bf93e2ccee135b5) [commit](https://github.com/jemalloc/jemalloc/commit/3959a9fe1973a7d7ddbbd99056c22e9b684a3275)
- Provide MADV_FREE when system headers lack the definition, and remove the default value for the purge madvise behavior macro. [commit](https://github.com/jemalloc/jemalloc/commit/31ab38be5f3c4b826db89ff3cd4f32f988747f06) [commit](https://github.com/jemalloc/jemalloc/commit/f4f814cd4cca4be270c22c4e943cd5ae6c40fea9)
- Fix the MSVC 2015 project and add a Visual Studio 2017 solution. [commit](https://github.com/jemalloc/jemalloc/commit/33df2fa1694c9fdc1912aecaa19babc194f377ac)
- Use getpagesize() on FreeBSD, and prefer sysctl() to read page configuration. [commit](https://github.com/jemalloc/jemalloc/commit/d591df05c86e89c0a5db98274bc7f280f910a0de) [commit](https://github.com/jemalloc/jemalloc/commit/9f455e2786685b443201c33119765c8093461174)
- Enable shell strict mode in jemalloc_mangle.sh. [commit](https://github.com/jemalloc/jemalloc/commit/22460cbebd2b7343319d9a8425f593c92facacab)
- Disable MADV_HUGEPAGE detection on ARM architecture, and ensure JE_CXXFLAGS_ADD uses the C++ compiler. [commit](https://github.com/jemalloc/jemalloc/commit/433c2edabc5c03ae069ac652857c05c673807d0c) [commit](https://github.com/jemalloc/jemalloc/commit/78a87e4a80e9bf379c0dc660374173ef394252f6)
- Configure the adaptation implementation based on the return type of strerror_r(). [commit](https://github.com/jemalloc/jemalloc/commit/f78d4ca3fbff6cab0c704c787706a53ddafcbe13)
- Fix Visual Studio x86 private namespace settings and generated header x86/x64 compatibility, and fix MSVC build. [commit](https://github.com/jemalloc/jemalloc/commit/ed52d24f740ddf42b78c59ad0fdc8cd0ffe5c376) [commit](https://github.com/jemalloc/jemalloc/commit/83aa9880b706ab185aa84f2bf6057477efdd5fd6) [commit](https://github.com/jemalloc/jemalloc/commit/a3abbb4bdf168dbaa32938a2e995005a65d142ba)
- Remove the unused preserve_lru extents feature implementation. [commit](https://github.com/jemalloc/jemalloc/commit/6d02421730e2f2dc6985da699b8e10b3ed4061b6)
- Fix Windows type warnings, const qualifier warnings, emitter formatting warnings, and other compiler UNUSED/static analysis warnings. [commit](https://github.com/jemalloc/jemalloc/commit/d3e0976a2c1591b9fe433e7a383d8825683995f0) [commit](https://github.com/jemalloc/jemalloc/commit/cf2f4aac1ca8c7d48a61a3921335fb411a3943a4) [commit](https://github.com/jemalloc/jemalloc/commit/49373096206964c3d60c1deaa75dcab6e90b7f59) [commit](https://github.com/jemalloc/jemalloc/commit/2a80d6f15b18de2ef17b310e995af366cc20034c) [commit](https://github.com/jemalloc/jemalloc/commit/0fadf4a2e3e629b9fa43888f9754aea5327d038f)
- Add the install_lib_pc installation control option. [commit](https://github.com/jemalloc/jemalloc/commit/39b1b2049934be5be7e5b1b6f77ff31cd02398c5)
- Adjust the version string format in jemalloc.pc.in. [commit](https://github.com/jemalloc/jemalloc/commit/a308af360ca8fccb31f9dcdb0654b0d4cf6f776c)
- Fix include search order for out-of-tree builds; allow cross-compilation to prefer headers generated in the build directory. [commit](https://github.com/jemalloc/jemalloc/commit/b73380bee0abde8e74f43d19d099cc151f51eb58)

### Maintenance

- Adjust jeprof's filtering of newImpl symbols to avoid this implementation detail interfering with profile output. [commit](https://github.com/jemalloc/jemalloc/commit/2d2fa72647e0e535088793a0335d0294277d2f09) [commit](https://github.com/jemalloc/jemalloc/commit/d157864027562dc17475edfd1bc6dce559b7ac4b)
- Change spin_adaptive to internal linkage to avoid exporting unused symbols. [commit](https://github.com/jemalloc/jemalloc/commit/048c6679cd0ef1500d0609dce48fcd823d15d93b)

