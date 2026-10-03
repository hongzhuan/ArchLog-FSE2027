# Release Note

## Important Changes

### Debugging & Profiling Layer
- Made architectural adjustments to the profiling module: first tried to split the core data management and logging functions into independent modules, then rolled back these splits, restored the original module structure, and adjusted the visibility of related functions and variables. (Architecture-related: public API and module responsibilities)
  ↳ [#1556](https://github.com/jemalloc/jemalloc/pull/1556): [0b46240](https://github.com/jemalloc/jemalloc/commit/0b462407ae84a62b3c097f0e9f18df487a47d9a7) | [#1574](https://github.com/jemalloc/jemalloc/pull/1574): [1a05033](https://github.com/jemalloc/jemalloc/commit/1a0503367be5950a8da648996ba7ae2620e39393), [5742473](https://github.com/jemalloc/jemalloc/commit/5742473cc87558b4655064ebacfd837119673928)
- Added a new red zone check function for small sample allocation, and supports custom abort processing through the configurable abort function. (Architecture-related: public API: redzone check and abort configuration)
  ↳ [#1465](https://github.com/jemalloc/jemalloc/pull/1465): [33e1dad](https://github.com/jemalloc/jemalloc/commit/33e1dad6803ea3e20971b46baa299045f736d22a), [b92c9a1](https://github.com/jemalloc/jemalloc/commit/b92c9a1a81f3f68da87afe5887d8450fef0700d3), [21cfe59](https://github.com/jemalloc/jemalloc/commit/21cfe59ff7b10a61dabe26cd3dbfb7a255e1f5e8) | [#1539](https://github.com/jemalloc/jemalloc/pull/1539): [7720b6e](https://github.com/jemalloc/jemalloc/commit/7720b6e3851d200449914448c7163f7af92cd63f)
- Added nonfull_slabs counter to bin statistics and displayed in statistical output. (Architecture-related: public API: nonfull_slabs statistics)
  ↳ [#1486](https://github.com/jemalloc/jemalloc/pull/1486): [7fc4f2a](https://github.com/jemalloc/jemalloc/commit/7fc4f2a32c74701e40e98c8ac05aa7cf12d876c9)
- Added confirm_conf option. When enabled, all configuration strings and the setting process of each option will be printed at startup. (Architecture-related: public API: confirm_conf)
  ↳ [#1498](https://github.com/jemalloc/jemalloc/pull/1498): [c92ac30](https://github.com/jemalloc/jemalloc/commit/c92ac306013bc95cd5f34de421b1aa5eb1f28971) | [#1568](https://github.com/jemalloc/jemalloc/pull/1568): [85f0cb2](https://github.com/jemalloc/jemalloc/commit/85f0cb2d0c0a05e9fc926544c65ca784c03ab239)
- Add nfills and nflushes tracking and output for arena's small and large allocation statistics. (Architecture-related: public API: nfills/nflushes statistics)
  ↳ [#1501](https://github.com/jemalloc/jemalloc/pull/1501): [07c4484](https://github.com/jemalloc/jemalloc/commit/07c44847c24634d0d11f9ceab7318400ffc1a16e)
- Added abandoned_vm counter, used to track virtual memory space leaked due to metadata allocation failure (OOM), and expose this indicator in the statistical output. (Architecture-related: public API)
  ↳ [#1553](https://github.com/jemalloc/jemalloc/pull/1553): [4e36ce3](https://github.com/jemalloc/jemalloc/commit/4e36ce34c1e6a6f470a9355b90b0a757c6fdb0b5)
- Fixed a memory leak caused by not supporting split when retain is disabled on the Windows platform, and adjusted the allocation strategy to only perform exact matches to avoid split and merge operations. (Architecture-related: platform compatibility)
  ↳ [#1545](https://github.com/jemalloc/jemalloc/pull/1545): [57dbab5](https://github.com/jemalloc/jemalloc/commit/57dbab5d6bc764a8b971334ec80977d6333688af) | [#1573](https://github.com/jemalloc/jemalloc/pull/1573): [c9cdc1b](https://github.com/jemalloc/jemalloc/commit/c9cdc1b27f8aa9c1e81e733e60d470c04be960b3)
- Fixed the boundary condition error in buffer writing in the prof module to avoid memory out-of-bounds; also fixed the problem of using the wrong emitter API when printing prof log, resulting in redundant lines being output. (Architecture-related: public API)
  ↳ [#1521](https://github.com/jemalloc/jemalloc/pull/1521): [e0a0c8d](https://github.com/jemalloc/jemalloc/commit/e0a0c8d4bf512283e8c85fb4a51761fce5e0c08f) | [#1576](https://github.com/jemalloc/jemalloc/pull/1576): [82b8aaa](https://github.com/jemalloc/jemalloc/commit/82b8aaaeb68ccb65ca52532f4806a43fbdb26b7a) | [#1520](https://github.com/jemalloc/jemalloc/pull/1520): [d26636d](https://github.com/jemalloc/jemalloc/commit/d26636d566167a439ea18da7a234f9040668023b) | [#1478](https://github.com/jemalloc/jemalloc/pull/1478): [c2a3a7c](https://github.com/jemalloc/jemalloc/commit/c2a3a7cd3f3cbc177d677101be85a31a39c26bd0)
- Reconstructed the performance analysis log module, split the internal data structure management logic into new files, and adjusted some log output interfaces; at the same time, the format_arg attribute annotation was added to the format generation function, and autoconf feature detection was added to support the jemalloc special macro. (Architecture-related: public API, build requirements)
  ↳ [#1556](https://github.com/jemalloc/jemalloc/pull/1556): [7618b0b](https://github.com/jemalloc/jemalloc/commit/7618b0b8e458d9c0db6e4b05ccbe6c6308952890) | [#1460](https://github.com/jemalloc/jemalloc/pull/1460): [020b5dc](https://github.com/jemalloc/jemalloc/commit/020b5dc7ac5138a347e5462508b2b5e4ecd6bc52), [7f7935c](https://github.com/jemalloc/jemalloc/commit/7f7935cf7805036d42fb510592ab8b40bcfb0690)
- Removed the deprecated prof_accumbytes field from the arena structure. (Architecture-related: ABI compatibility)
  ↳ [#1522](https://github.com/jemalloc/jemalloc/pull/1522): [a2a693e](https://github.com/jemalloc/jemalloc/commit/a2a693e722d3ec0f0fb7dfcac54e775b1837efda)

### User API Layer
- Add a flag-free version of the sdallocx function for C++ operator delete and delete[], eliminating unnecessary flag checking branches in the fast path. (Architecture-related: public API: sdallocx)
  ↳ [#1451](https://github.com/jemalloc/jemalloc/pull/1451): [d3d7a8e](https://github.com/jemalloc/jemalloc/commit/d3d7a8ef09b6fa79109e8930aaba7a677f8b24ac)
- Added experimental.utilization namespace to provide memory utilization analysis function, support input of single pointer or pointer array, and output memory utilization statistics. (Architecture-related: public API: experimental.utilization)
  ↳ [#1463](https://github.com/jemalloc/jemalloc/pull/1463): [9aab3f2](https://github.com/jemalloc/jemalloc/commit/9aab3f2be041b09f42375d3bf173d1a8795a1ee9) | [#1480](https://github.com/jemalloc/jemalloc/pull/1480): [7ee3897](https://github.com/jemalloc/jemalloc/commit/7ee3897740aabdccb2381b7b6ab68fff0aac3ec4) | [#1505](https://github.com/jemalloc/jemalloc/pull/1505): [4c63b0e](https://github.com/jemalloc/jemalloc/commit/4c63b0e76a693b0cfdf209cb4f8fbd1ed74453b0)
- Expose the opt_safety_checks configuration item through the mallctl interface, and output the configuration value in statistical information. (Architecture-related: public API: opt_safety_checks)
  ↳ [#1465](https://github.com/jemalloc/jemalloc/pull/1465): [f95a88f](https://github.com/jemalloc/jemalloc/commit/f95a88fcd92e8ead1a6c5c8b2ca8c401c6eba162)
- Added experimental mallctl experimental.arenas.i.pactivep, which is used to quickly read the pactive counter of arena and avoid going through the mallctl/epoch step. (Architecture-related: public API: experimental.arenas.i.pactivep)
  ↳ [#1508](https://github.com/jemalloc/jemalloc/pull/1508): [e13cf65](https://github.com/jemalloc/jemalloc/commit/e13cf65a5f37bbd9b44badb198ccc138cbacc219)
- Fixed the problem of posix_memalign triggering assertion failure when the input size is 0, and instead returns a valid pointer. (Architecture-related: public API)
  ↳ [#1554](https://github.com/jemalloc/jemalloc/pull/1554): [f32f23d](https://github.com/jemalloc/jemalloc/commit/f32f23d6cc3ac9e663983ae62371acd47405c886)

### Platform Abstraction Layer
- Implemented retain function on Windows, by tracking the header extent state of each VirtualAlloc region, restricting merge and split operations to only be performed in the same region, to correctly support MEM_DECOMMIT. (Architecture-related: platform compatibility)
  ↳ [#1545](https://github.com/jemalloc/jemalloc/pull/1545): [9a86c65](https://github.com/jemalloc/jemalloc/commit/9a86c65abc2cf242efe9354c9ce16901673eeb0c)

### Cross-cutting / Other Architecture-related Changes
- Fixed the problem of address not forcing page alignment when using custom extent hooks, and improved error handling when registration failed. (Architecture-related: extent hooks alignment requirements)
  ↳ [#1470](https://github.com/jemalloc/jemalloc/pull/1470): [93084cd](https://github.com/jemalloc/jemalloc/commit/93084cdc8960935d0acc93424dddd3a79a86e2da)
- Fixed the issue where arena_dalloc_promoted is not correctly called when releasing large objects when tcache is disabled. (Architecture-related: core allocation path)
  ↳ [#1564](https://github.com/jemalloc/jemalloc/pull/1564): [bc0998a](https://github.com/jemalloc/jemalloc/commit/bc0998a9052957584b6944b6f43fffe0648f603e)
- Force the use of the TLS_MODEL attribute in header files and source files, and unify the declaration method of thread-local storage variables. (Architecture-related: platform compatibility)
  ↳ [#1482](https://github.com/jemalloc/jemalloc/pull/1482): [1aabab5](https://github.com/jemalloc/jemalloc/commit/1aabab5fdca1cd76be3900e9272ef83549006ac0)
- Added --enable-documentation build option, allowing users to disable document building; the installation target will conditionally include documentation installation based on this option. (Architecture-related: build and installation methods)
  ↳ [#1488](https://github.com/jemalloc/jemalloc/pull/1488): [702d76d](https://github.com/jemalloc/jemalloc/commit/702d76dbd03e4fe7347399e1e322c80102c95544)
- Enable the opt.retain option by default on Windows platforms, and update related documentation. (Architecture-related: platform compatibility)
  ↳ [#1545](https://github.com/jemalloc/jemalloc/pull/1545): [badf8d9](https://github.com/jemalloc/jemalloc/commit/badf8d95f11cf8ead0f8b7192663002d1d4dc4b2) | [#1567](https://github.com/jemalloc/jemalloc/pull/1567): [9f6a9f4](https://github.com/jemalloc/jemalloc/commit/9f6a9f4c1f78fd61297e01ae1521af9696d2023b)

## Routine Changes

### New features
- No significant changes.

### bug fixes
- Fix GCC-9.1 compilation warning, explicitly convert variable type in macro GET_ARG_NUMERIC.
  ↳ [#1509](https://github.com/jemalloc/jemalloc/pull/1509): [2d6d099](https://github.com/jemalloc/jemalloc/commit/2d6d099fed05b1509e81e54458516528bfbbf38d)
- Fixed an issue in the release fast path that may cause assertions to be triggered incorrectly due to uninitialization, and moved assertions to after confirming successful rtree reading.
  ↳ [#1506](https://github.com/jemalloc/jemalloc/pull/1506): [13e88ae](https://github.com/jemalloc/jemalloc/commit/13e88ae9700416b43bf88c596ea15c85bdb9f9e7)
- Add UNUSED attribute to expected parameter in atomic operation macro to avoid compilation warning of g++ 5.5.0+.
  ↳ [#1571](https://github.com/jemalloc/jemalloc/pull/1571): [9344d25](https://github.com/jemalloc/jemalloc/commit/9344d25488b626739c9080eb471d1bd15eeb046b)

### Refactoring optimization
- Removed best-fit memory allocation strategy, unified use of first-fit to reduce memory fragmentation, and optimized the fragmentation avoidance logic in first-fit.
  ↳ No PR: [5679751](https://github.com/jemalloc/jemalloc/commit/56797512083fe1457163170dfa44ee5ec12abe5f)
- When extent registration fails, extent_dalloc is used instead of extents_leak to avoid unnecessary purging of the area.
  ↳ [#1552](https://github.com/jemalloc/jemalloc/pull/1552): [42807fc](https://github.com/jemalloc/jemalloc/commit/42807fcd9ed68c78f660c6dd85bcf9d82e134244)
- Reconstructed the large object release logic, extracted the common code to the new function arena_dalloc_large, and simplified the implementation of arena_dalloc, arena_sdalloc_no_tcache and arena_sdalloc.
  ↳ [#1564](https://github.com/jemalloc/jemalloc/pull/1564): [a3fa597](https://github.com/jemalloc/jemalloc/commit/a3fa597921987709eb0aa2258f1b35cc433ae5d4)
- Rename macros in configuration initialization to more readable names, replacing the original yes and no.
  ↳ [#1499](https://github.com/jemalloc/jemalloc/pull/1499): [259b15d](https://github.com/jemalloc/jemalloc/commit/259b15dec5bff8b67b331b63703aa8511c759077)

### Test related
- Reduce the number of test threads on 32-bit platforms.
  ↳ [#1566](https://github.com/jemalloc/jemalloc/pull/1566): [10fcff6](https://github.com/jemalloc/jemalloc/commit/10fcff6c38c08bc2b1a672ff92701012944d843a)

### Performance optimization
- Optimize the first_fit allocation strategy: add max_active_fit check and stop scanning after finding the first extent that meets the conditions, thereby reducing fragmentation and improving performance.
  ↳ [#1562](https://github.com/jemalloc/jemalloc/pull/1562): [1d148f3](https://github.com/jemalloc/jemalloc/commit/1d148f353a2c71bc12fd066e467649fd17df3c95) | No PR: [b62d126](https://github.com/jemalloc/jemalloc/commit/b62d126df894dac00772eb5f3d170a1c1d3d1614)
- Changed extra size checks in thread cache to be controlled by runtime configuration flags.
  ↳ [#1465](https://github.com/jemalloc/jemalloc/pull/1465): [f4d24f0](https://github.com/jemalloc/jemalloc/commit/f4d24f05e1f270c43bc4129c0d18d673b8ac85b8)

### Security related
- No significant changes.

### Documentation
- Updated changelog for version 5.2.1.
  ↳ [#1580](https://github.com/jemalloc/jemalloc/pull/1580): [0cfa36a](https://github.com/jemalloc/jemalloc/commit/0cfa36a58a91b30996b30c948d67e1daf184c663)

### Build/CI
- Adjust the order of AppVeyor CI tasks to advance debug build and 64-bit build tasks.
  ↳ [#1547](https://github.com/jemalloc/jemalloc/pull/1547): [34e7563](https://github.com/jemalloc/jemalloc/commit/34e75630cc512423b4f227338056a2f5d7e81740)

### Maintenance
- Added sanity check to prof dump buffer size.
  ↳ [#1579](https://github.com/jemalloc/jemalloc/pull/1579): [8a94ac2](https://github.com/jemalloc/jemalloc/commit/8a94ac25d597e439b05b38c013e4cb2d1169c681)

### Others
- Optimize background thread statistics reading performance, change mutex waiting to try to acquire to reduce blocking.
  ↳ [#1510](https://github.com/jemalloc/jemalloc/pull/1510): [1a71533](https://github.com/jemalloc/jemalloc/commit/1a71533511027dbe3f9d989659efeec446915d6b)
- Fixed typos in macro names: replace rb_proto with ph_proto to eliminate compilation warnings.
  ↳ [#1460](https://github.com/jemalloc/jemalloc/pull/1460): [14e4176](https://github.com/jemalloc/jemalloc/commit/14e4176758379875c4ef486d6c57327ed07edd86)
- Fix typos in size class header file, and adjust SC_NPSIZES calculation method.
  ↳ [#1487](https://github.com/jemalloc/jemalloc/pull/1487): [ae124b8](https://github.com/jemalloc/jemalloc/commit/ae124b86849bb5464940db6731183dede6a70873)
- Fixed typos in variable names in jeprof script.
  ↳ [#1490](https://github.com/jemalloc/jemalloc/pull/1490): [498f47e](https://github.com/jemalloc/jemalloc/commit/498f47e1ec83431426cdff256c23eceade41b4ef)
