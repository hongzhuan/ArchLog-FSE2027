# Release Note

## Important Changes

### Platform Abstraction Layer

- Improved TSD atomic state and global slow path, added nominal TSD fork support; probe 8-bit atomic capability, fall back to 32-bit TSD atomics on unsupported platforms. [commit](https://github.com/jemalloc/jemalloc/commit/e74a1a37c82fa3a44cee1002d9d8957bcc8274a7) [commit](https://github.com/jemalloc/jemalloc/commit/982c10de3566f38628770e57c62d1a6cdc5a09f9) [commit](https://github.com/jemalloc/jemalloc/commit/39d6420c0c39619176af3477b827e8a92442b768) [commit](https://github.com/jemalloc/jemalloc/commit/feff510b9f938ae1b4e2f43815bc7b10f70fac12) [commit](https://github.com/jemalloc/jemalloc/commit/e870829e645bfd6d54e4a2d4cacce39478216a1e) [commit](https://github.com/jemalloc/jemalloc/commit/06f0850427e26cb24950de60bbe70bc192ffce6a) [commit](https://github.com/jemalloc/jemalloc/commit/b804d0f019df87d8cc96e3c812e98793256cb418)
- FreeBSD improvements to mmap/page size handling and allow building and running tests; added readlinkat support, FreeBSD pthread naming, and corresponding deferred cleanup adaptation. [commit](https://github.com/jemalloc/jemalloc/commit/50b473c8839f5408df179bdf6f2b3fd2cf5c3b2f) [commit](https://github.com/jemalloc/jemalloc/commit/a4c6b9ae011628d012dd8eaab39fb60aa595b922)

### API & Integration Layer

- Added experimental.hooks.install/remove control interface and hook module, can intercept pure allocation, deallocation, expansion, and realloc paths; added common no-hook fast path, reentrancy protection, and coverage tests. [commit](https://github.com/jemalloc/jemalloc/commit/5ae6e7cbfa6d6788340cc87d7717548f4d7960fe) [commit](https://github.com/jemalloc/jemalloc/commit/fe0e39938593b5fb16dc09fcdbe29d6ad7b3cf05) [commit](https://github.com/jemalloc/jemalloc/commit/226327cf66f6e1fb1aed24ed3e2e9c291d1843b7) [commit](https://github.com/jemalloc/jemalloc/commit/c154f5881b72c52a131e88ade6108d663ac03700) [commit](https://github.com/jemalloc/jemalloc/commit/83e516154cfacfc1e010a03f2f420bf79913944a) [commit](https://github.com/jemalloc/jemalloc/commit/67270040a56d8658ce6aec81b15d78571e0e9198) [commit](https://github.com/jemalloc/jemalloc/commit/cb0707c0fc948875876b93514938646455650e2b) [commit](https://github.com/jemalloc/jemalloc/commit/126e9a84a5a793fb0d53ca4656a91889b3ae40e8) [commit](https://github.com/jemalloc/jemalloc/commit/bb071db92ee8368fb6e64ef328d49fae6ba48089) [commit](https://github.com/jemalloc/jemalloc/commit/59e371f46331a3f4b688d6622a0af7ccc4f96be6) [commit](https://github.com/jemalloc/jemalloc/commit/0379235f47585ac8f583ba85aab9d294abfa44b5) [commit](https://github.com/jemalloc/jemalloc/commit/a7f749c9af0d5ca51b5b5eaf35c2c2913d8a77e1)
- Added experimental smallocx(size, flags) interface and version-related symbol names, and supplemented integration/CI tests; when experimental configuration is enabled, the symbol is still hidden outside the public library API. [commit](https://github.com/jemalloc/jemalloc/commit/08260a6b944a67a3d9f63e7eb738718fc760e0ea) [commit](https://github.com/jemalloc/jemalloc/commit/730e57b08fe5bd6bdc38ca4ff6a73959984d8ef0) [commit](https://github.com/jemalloc/jemalloc/commit/741fca1bb7773e14cf929824b94506eb9f545e5e) [commit](https://github.com/jemalloc/jemalloc/commit/837de32496b1f20524c723516775a11bf236f891) [commit](https://github.com/jemalloc/jemalloc/commit/01e2a38e5a5523350496b11af46cf1d4c1d74e4c)
- configure supports --disable-libdl; background threads still work without depending on libdl, and fall back to default pthread_create when RTLD_NEXT lookup fails. [commit](https://github.com/jemalloc/jemalloc/commit/1f55a15467357bb559701687dbef1be84047ddfe) [commit](https://github.com/jemalloc/jemalloc/commit/2db2d2ef5e1cf2eb2c0de362c916d0f7a2f1a9ef) [commit](https://github.com/jemalloc/jemalloc/commit/23b15e764b3d87c8e69a348d60d13e7e44f137b5)

### Profiling & Statistics Layer

- Adjusted sampling allocation fast path, moved bytes-until-sample state into TSD to avoid loading tdata when not sampling; added sampled allocation logging and fixed profiling memory regression. [commit](https://github.com/jemalloc/jemalloc/commit/b664bd79356d7f6da6f413023f9aef014b85c145) [commit](https://github.com/jemalloc/jemalloc/commit/9ed3bdc8484049bd304c771a1b10070d5d7c95db) [commit](https://github.com/jemalloc/jemalloc/commit/0ac524308d3f636d1a4b5149fa7adf24cf426d9c) [commit](https://github.com/jemalloc/jemalloc/commit/997d86acc6d2cc632b79669ebf3f938290e9f5da) [commit](https://github.com/jemalloc/jemalloc/commit/325e3305fc7563600a710341d1f98cb8e04caaba) [commit](https://github.com/jemalloc/jemalloc/commit/936bc2aa15504076f884ed97a51e169924fe4a89)
- Added extents and extent_avail heap size information to mallocstats output, and supplemented sampled allocation logging unit tests. [commit](https://github.com/jemalloc/jemalloc/commit/c14e6c08192034d9140d61197d7c4981ca293610) [commit](https://github.com/jemalloc/jemalloc/commit/126252a7e6bd098d649f6a82a947c7c056816c2c)

### Cross-cutting / Other Architecture-related Changes

- Introduced huge arena and opt.huge_threshold, moving allocations exceeding the threshold into a separate arena; supplemented mallctl and statistics, and evolved this experimental option into oversize_threshold, with default value 8 MiB, allowing low thresholds to be disabled. [commit](https://github.com/jemalloc/jemalloc/commit/94a88c26f4d9cffd884a349201e7605f13495f3f) [commit](https://github.com/jemalloc/jemalloc/commit/79522b2fc225f709a4ca7503c00f56df5d667160) [commit](https://github.com/jemalloc/jemalloc/commit/1302af4c43e031304b422e36fcbb9e159804e0ac) [commit](https://github.com/jemalloc/jemalloc/commit/cdf15b458a1c348722fa43cb1813ac3a93fdc634) [commit](https://github.com/jemalloc/jemalloc/commit/7a815c1b7c796ef35e7ede60cb2dd44aba9626b4) [commit](https://github.com/jemalloc/jemalloc/commit/350809dc5d43ea994de04f7a970b6978a8fec6d2) [commit](https://github.com/jemalloc/jemalloc/commit/e3db480f6f3c147a8630c0ec45fde1da5764270b) [commit](https://github.com/jemalloc/jemalloc/commit/788a657cee745c1f827ddf1db50d580bd5e4347b)
- Migrated size class calculation from shell script to C module, removed --with-lg-page-sizes option, and support configuring page/slab sizes via MALLOC_CONF. [commit](https://github.com/jemalloc/jemalloc/commit/2f07e92adb7060045e9e8601126e5ec071091c42) [commit](https://github.com/jemalloc/jemalloc/commit/4f55c0ec220ae97eb5bc7e2bebc07d5c6100fa83) [commit](https://github.com/jemalloc/jemalloc/commit/0552aad91b955db7ad1806907255e943af2fdb88) [commit](https://github.com/jemalloc/jemalloc/commit/5b7fc9056c8114d0774282d293cd5c9cce4ff931) [commit](https://github.com/jemalloc/jemalloc/commit/017dca198c74792967771d00b7501beade5b6fd0) [commit](https://github.com/jemalloc/jemalloc/commit/a7f68aed3ef53a194f6b932b92bddd8c84c43de4) [commit](https://github.com/jemalloc/jemalloc/commit/4610ffa942a00d80a8e8af2365069bed7d561415) [commit](https://github.com/jemalloc/jemalloc/commit/5112d9e5fd2a15d6b75523a3a4122b726fbae479) [commit](https://github.com/jemalloc/jemalloc/commit/55e5cc1341de87ad06254d719946a5ecd05f06ab)
- Added Seq module, providing lightweight seqlock implementation. [commit](https://github.com/jemalloc/jemalloc/commit/06a8c40b36403e902748d3f2a14e6dd43488ae89)
- Support sharded bins within arena, configure shard count via opt.bin_shards and provide shard statistics; cache shard selection in TSD, supplement concurrency tests and fix statistics merging. [commit](https://github.com/jemalloc/jemalloc/commit/37b89139252db18c95ebce3e0eac67817fa4a8ab) [commit](https://github.com/jemalloc/jemalloc/commit/3f9f2833f6228e07673d75c9bce6f5fb58c5f3b0) [commit](https://github.com/jemalloc/jemalloc/commit/45bb4483baef0f9bb1362349d9838ee041c42754) [commit](https://github.com/jemalloc/jemalloc/commit/711a61f3b41880718eb23fcfdd572d0daa5fb6ca)
- Added special handling for retain, purge, decay, and extent reclamation paths for oversize/huge allocations, avoiding incorrect dalloc, delayed purge, or zero-fill issues. [commit](https://github.com/jemalloc/jemalloc/commit/0ecd5addb1215f5ae9fad2b9cb4cf91ed5376ee8) [commit](https://github.com/jemalloc/jemalloc/commit/f459454afe019251712728b983d2eed0b03f5c80)

## Routine Changelog

### New Features

- Added smallocx zero-size and alignment allocation tests, and support size2index handling of zero size. [commit](https://github.com/jemalloc/jemalloc/commit/2b112ea5932d280288882d8bb38e7942b166fe5a) [commit](https://github.com/jemalloc/jemalloc/commit/4edbb7c64c83aa2059ade469bc798dadf3da194c)
- Default background thread count adjusted to 4. [commit](https://github.com/jemalloc/jemalloc/commit/c4063ce439523d382f2dfbbc5bf6da657e6badb0)
- Muzzy decay disabled by default. [commit](https://github.com/jemalloc/jemalloc/commit/8e9a613122251d4c519059f8e1e11f27f6572b4c)

### Bug Fixes

- Fixed index boundary for background thread maximum count configuration and corresponding tests, and corrected erroneous assertions. [commit](https://github.com/jemalloc/jemalloc/commit/e8a63b87c36ac814272d73b503658431d2000055) [commit](https://github.com/jemalloc/jemalloc/commit/312352faa89a39ff1e690d709d7d6f852f89d61d) [commit](https://github.com/jemalloc/jemalloc/commit/b293a3eb86a32b9c242ac39d88312c0a9d317b8b)
- Fixed arena lock handling in tcache_bin_flush_large, and supplemented remote deallocation tests. [commit](https://github.com/jemalloc/jemalloc/commit/fec1ef7c91b5368ad0d6f0c84bc77fa71d9dc949) [commit](https://github.com/jemalloc/jemalloc/commit/50820010fef8f40e1221360ef745d9bb5fa93364)
- Fall back to default pthread_create implementation when RTLD_NEXT cannot find pthread_create. [commit](https://github.com/jemalloc/jemalloc/commit/77a71ef2b76c2e858c81e10349f28534307f1c91)
- Fixed stats output for opt.lg_extent_max_active_fit. [commit](https://github.com/jemalloc/jemalloc/commit/9bd8deb26044b7a3f056f8995aae95ffe86d19ed)
- Detect states that should not exist in tsd_nominal_list, and add TSD fork cleanup support. [commit](https://github.com/jemalloc/jemalloc/commit/013ab26c8674e07d40098f7385e570c6d8b0dee9) [commit](https://github.com/jemalloc/jemalloc/commit/41b7372eadee941b9164751b8d4963f915d3ceae)
- Fixed issue where MALLOC_CONF overrides opt_prof_prefix at startup. [commit](https://github.com/jemalloc/jemalloc/commit/88771fa0138c75a2d29601cc33025d81822b082a)
- Fixed bit_util path on s390x where __builtin_clz cannot be used. [commit](https://github.com/jemalloc/jemalloc/commit/115ce93562ab76f90a2509bf0640bc7df6b2d48f)
- Check return value of malloc_read_fd(). [commit](https://github.com/jemalloc/jemalloc/commit/856319dc8a3d15c3eddf83d106e01e6f63c349a7)
- Fixed spin-wait race in mutex trylock. [commit](https://github.com/jemalloc/jemalloc/commit/b23336af96e6ef9efb47591ce7bf2c8a1eab866b)
- Fixed arena statistics merging error under sharded bins. [commit](https://github.com/jemalloc/jemalloc/commit/99f4eefb61ae1f13e47af6eac34748fd0a789404)
- Fixed total request rate calculation in stats and spacing of total_wait_time/nrequests output. [commit](https://github.com/jemalloc/jemalloc/commit/8c9571376e65c8099ea315261c24e940410386c8) [commit](https://github.com/jemalloc/jemalloc/commit/522d1e7b4b603d9ddc11c684c16d37113a9c0c12) [commit](https://github.com/jemalloc/jemalloc/commit/b33eb26dee1c161572b209a8fe3f58419ce4874f)
- Check szind during tcache flush, and fix missing diagnostic output when tcache size matching check fails. [commit](https://github.com/jemalloc/jemalloc/commit/e13400c919e6b6730284ff011875bbcdd6821f1c) [commit](https://github.com/jemalloc/jemalloc/commit/a4d017f5e5aea12b745e67679ba40753f6d7a778)
- Fixed missing unlock in extent_register error path. [commit](https://github.com/jemalloc/jemalloc/commit/59d98919482b2a101c4092428a4c0092abb797a1)
- Reduced ineffective checks in low-value scenarios of opt.oversize_threshold. [commit](https://github.com/jemalloc/jemalloc/commit/0101d5ebef7230ef5aa1597be425e2a60e92f348)

### Refactoring

- Adjusted positions of tsd link and in_hook fields. [commit](https://github.com/jemalloc/jemalloc/commit/d1e11d48d4c706e17ef3508e2ddb910f109b779f)
- Hid size class calculation behind an indirection layer, and split quantum detection separately. [commit](https://github.com/jemalloc/jemalloc/commit/e904f813b40b4286e10172163c880fd9e1d0608a) [commit](https://github.com/jemalloc/jemalloc/commit/07b89c76736313159e952648a9df3bdcfe57eda2)
- Minor cleanup of emitter module. [commit](https://github.com/jemalloc/jemalloc/commit/eb261e53a6bfaef9797395fe09d6a425b11acb42)
- Refactored jemalloc's use of mmap() on FreeBSD. [commit](https://github.com/jemalloc/jemalloc/commit/f80c97e477d1b3fe7778c65d9439d673738b4131)
- Removed bump_empty_alloc configuration, now handled by size class lookup for empty allocations. [commit](https://github.com/jemalloc/jemalloc/commit/ac34afb4037d7e9e87efde2b8e913d87aae131da)
- Use extent retain fast path for large object reclamation, and optimize tcache large block batch filling and slab batch registration allocation. [commit](https://github.com/jemalloc/jemalloc/commit/8dabf81df1b7db0fd16903abab889dfd61b4c07f) [commit](https://github.com/jemalloc/jemalloc/commit/d66f97662879a1a0c61ee12ba4b760fa6f458eef) [commit](https://github.com/jemalloc/jemalloc/commit/17aa470760cefb3057be746f7022196035f0cfbe) [commit](https://github.com/jemalloc/jemalloc/commit/13c237c7ef5baa63c820539e0cfef4c4c5c74ea2)

### Tests

- Added unit tests for huge arena threshold control. [commit](https://github.com/jemalloc/jemalloc/commit/ff622eeab51325979226d5430c68a08d3e00b26b)
- Simplified gen_travis.py output and verify generated .travis.yml in CI. [commit](https://github.com/jemalloc/jemalloc/commit/0eb0641cac0c3031f84469953b5e75b380867ccb) [commit](https://github.com/jemalloc/jemalloc/commit/6deed86deb48d3b432d972a139a413a9fb38283b)
- Added unit tests for logging functionality. [commit](https://github.com/jemalloc/jemalloc/commit/5e23f96dd4e4ff2847a85d44a01b66e4ed2da21f)
- Alignment and OOM tests explicitly use arena 0. [commit](https://github.com/jemalloc/jemalloc/commit/d3145014a00d6420824a45bb24fa9237a553d8dc)
- Fixed binshard unit test, and use iallocztm in profiling tests. [commit](https://github.com/jemalloc/jemalloc/commit/6fe11633b066d74bdbb0f037a373af6e12a8b6c2) [commit](https://github.com/jemalloc/jemalloc/commit/978a7a21ae5fe8e5367732b2dba9f92742aef9f1)

### Performance

- Automatic arena no longer acquires large_mtx; ixalloc avoids duplicate size queries. [commit](https://github.com/jemalloc/jemalloc/commit/c834912aa9503d470c3dae2b2b7840607f0d6e34) [commit](https://github.com/jemalloc/jemalloc/commit/0ff7ff3ec7b322881fff3bd6d4861fda6e9331d9)
- Added microbenchmark for hooks. [commit](https://github.com/jemalloc/jemalloc/commit/1f71e1ca4319de7788d53d1d0ba905995c7f52bd)
- Use intrinsics for pow2_ceil when platform builtins are available. [commit](https://github.com/jemalloc/jemalloc/commit/4c548a61c89b0472b9952fcc4090eb00c2a88870)
- Removed a branch in cache_bin_alloc_easy fast path. [commit](https://github.com/jemalloc/jemalloc/commit/09adf18f1aefcee71cc716f4f366c7e2e889b7fa)
- Use extent arena information in tcache to optimize tcache flush and small object deallocation paths. [commit](https://github.com/jemalloc/jemalloc/commit/d1a861fa80c66221be8c4d94e51128a4641809da) [commit](https://github.com/jemalloc/jemalloc/commit/5e795297b33f25329a034fd898ee7d80c57b9a8f) [commit](https://github.com/jemalloc/jemalloc/commit/e2ab215324d7d19e37f4be87beb7a179528a300f)
- Added ticker_trytick and fastpath for malloc; also fixed tcache destroy decay triggering, flush, and large object reclamation. [commit](https://github.com/jemalloc/jemalloc/commit/0ec656eb7117127602f295510de694083353f23e) [commit](https://github.com/jemalloc/jemalloc/commit/0f8313659e93379d930995ea2d2af0a079cc422e) [commit](https://github.com/jemalloc/jemalloc/commit/7ee0b6cc37ecbecf8f53ba46326258275053ca50) [commit](https://github.com/jemalloc/jemalloc/commit/cd2931ad9bbd78208565716ab102e86d858c2fff) [commit](https://github.com/jemalloc/jemalloc/commit/794e29c0abbd77624d1e5599313ebd77bdc17ccc) [commit](https://github.com/jemalloc/jemalloc/commit/1f561157042a779be12a2159a385de0416133f6b)
- Reduced ineffective operations in profiling/extent state access, and limit fast path debug builds from touching all pages. [commit](https://github.com/jemalloc/jemalloc/commit/57553c3b1a5592dc4c03f3c6831d9b794e523865) [commit](https://github.com/jemalloc/jemalloc/commit/7241bf5b745ba5ec24b26b0ef2bd30b1c0a428dc)
- Let TSD store shard selection, and optimize arena bin batch filling. [commit](https://github.com/jemalloc/jemalloc/commit/98b56ab23dd4d3dc826f06906e6c51c9c9d4d52a) [commit](https://github.com/jemalloc/jemalloc/commit/4b82872ebf5e8b701e8b37c6d1297ceb88405df8)
- Stats added rate counters, and supplemented producer-consumer pattern unit tests. [commit](https://github.com/jemalloc/jemalloc/commit/36de5189c70fee959ebcdfadd8dfa374ff430de5) [commit](https://github.com/jemalloc/jemalloc/commit/441335d924984022a3e17c3f013a0ad33806a5ff)
- Fixed case where huge arena creates too many background threads. [commit](https://github.com/jemalloc/jemalloc/commit/bbe8e6a9097203c7b29140b5410c787a6e204593)
- Purge merged oversized extents early. [commit](https://github.com/jemalloc/jemalloc/commit/fb56766ca9b398d07e2def5ead75a021fc08da03)
- Skip acquiring extents_muzzy mutex when muzzy decay is disabled. [commit](https://github.com/jemalloc/jemalloc/commit/d22e150320801c114b3694e860195254bad1ef0f)

### Documentation

- Fixed SC_NPSIZES comment in documentation. [commit](https://github.com/jemalloc/jemalloc/commit/33f1aa5badd2f9caf91991bab60df64a37c394bb)
- Clarified differences in mmap behavior under retain:true. [commit](https://github.com/jemalloc/jemalloc/commit/a7b0a124c3ebe505cfd8c2d5cc797b8f0c96fbc6)
- Documented opt.oversize_threshold configuration and improved related description. [commit](https://github.com/jemalloc/jemalloc/commit/ce03e4c7b8ddeaec5e72c8fb160e378f418ed651) [commit](https://github.com/jemalloc/jemalloc/commit/064d6e570e7073096471413f6a5159541478eb01)

### Build / CI

- Fixed MSVC build, cleaned -Wextra warnings, and only suppress missing-field-initializer warnings for compilers with the defect. [commit](https://github.com/jemalloc/jemalloc/commit/ce5c073fe5017e802d1e272a9e057f7b631da345) [commit](https://github.com/jemalloc/jemalloc/commit/3d29d11ac2c1583b9959f73c0548545018d31c8a) [commit](https://github.com/jemalloc/jemalloc/commit/fb924dd7bf5e765ffcb273b6b88a515fea54fea8)
- Make abort_conf tolerate experimental configuration items. [commit](https://github.com/jemalloc/jemalloc/commit/4bc48718b2eb98e3646a86af816f9c6db29d1612)
- FreeBSD uses readlink compatible path, and fixes FreeBSD build and test configuration. [commit](https://github.com/jemalloc/jemalloc/commit/e8ec9528abac90efe4e0cc3a29da8d7aea59f23d) [commit](https://github.com/jemalloc/jemalloc/commit/0771ff2cea6dc18fcd3f6bf452b4224a4e17ae38)
- CI adds Valgrind build task. [commit](https://github.com/jemalloc/jemalloc/commit/36eb0b3d77404f389cfddad6675fe1f479e76be7)
- Adds SC module files to MSVC project. [commit](https://github.com/jemalloc/jemalloc/commit/9f43defb6eac30c36dbde25d82e88be23f97309f)
- FreeBSD disables unsuitable lazy-purge runtime detection. [commit](https://github.com/jemalloc/jemalloc/commit/676cdd66792ccb629a978837ea2a066d5db342cc)
- Use lwsync only on PowerPC64. [commit](https://github.com/jemalloc/jemalloc/commit/be0749f59151ffecbdf7d9f82193350f018904dd)
- configure adds --enable/--disable-static and --enable/--disable-shared options, and implements malloc_getcpu on Windows. [commit](https://github.com/jemalloc/jemalloc/commit/4e920d2c9d5aecc9dec7069a0c9736b1f14eead9)
- Adds FreeBSD Cirrus-CI configuration. [commit](https://github.com/jemalloc/jemalloc/commit/6910fcb208e2703f72bcbfbd1db22426d02b1e27)
- Replaces -lpthread linking method, and implements malloc_getcpu on Windows. [commit](https://github.com/jemalloc/jemalloc/commit/daa0e436ba232d67b832e1b270b13c5061eebfe9) [commit](https://github.com/jemalloc/jemalloc/commit/471191075d6a88eb1364fb5f332237eb3d512872)
- Builds documentation by default. [commit](https://github.com/jemalloc/jemalloc/commit/9015deb126d7b2b90ef822cf0183f96abb9b97f9)
- Avoids duplicate definition of tsd_t, and initializes libgcc unwind only when profiling is enabled. [commit](https://github.com/jemalloc/jemalloc/commit/dca7060d5e49b8a07179a1f13bf39f6d30e709c8) [commit](https://github.com/jemalloc/jemalloc/commit/18450d0abe36757fe6e4eb08f6b15f8ce943f9cb)
- Changes TLS callback linker directive to string form. [commit](https://github.com/jemalloc/jemalloc/commit/cbdb1807cea6828d0f61e1a0516613efc3e7189e)
- Removes old compare-and-swap forced macros, and fixes configure.ac syntax errors. [commit](https://github.com/jemalloc/jemalloc/commit/775fe302a75c4770edd9708e7348e626c96dfe58) [commit](https://github.com/jemalloc/jemalloc/commit/ac24ffb21e28ba1ed86250fa6a6dcaf02b43f7da)
- Uses GCC diagnostic pragma only outside the supported old GCC range. [commit](https://github.com/jemalloc/jemalloc/commit/14d3686c9f3ed28f1ef4c9ec5f7bde945473194b)

### Maintenance

- Adjusts output format of per-arena summary. [commit](https://github.com/jemalloc/jemalloc/commit/09edea3f5c98dae3f298b7ac9f5adad13e528bc9)
- Removes global data of SC module. [commit](https://github.com/jemalloc/jemalloc/commit/3aba072cef71d0f2bacc4ef10932a46f1df43192)
- FreeBSD uses pthread_set_name_np to set thread names. [commit](https://github.com/jemalloc/jemalloc/commit/ceba1dde2774e4eae659a548263970cd9b74d319)
- Deprecates OSSpinLock. [commit](https://github.com/jemalloc/jemalloc/commit/43f3b1ad0cd0900797688aa8b52b1face6416999)

