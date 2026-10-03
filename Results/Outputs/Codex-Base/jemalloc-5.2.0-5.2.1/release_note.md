# Release Note

## Important Changes

### Debugging & Profiling Layer

- Adds optional lightweight safety check configuration `--enable-opt-safety-checks`, and controls checks such as size matching at runtime via the safety check configuration; adds read-only `config.opt_safety_checks` and statistics output fields to confirm whether it is enabled. [commit](https://github.com/jemalloc/jemalloc/commit/f4d24f05e1f270c43bc4129c0d18d673b8ac85b8) [commit](https://github.com/jemalloc/jemalloc/commit/f95a88fcd92e8ead1a6c5c8b2ca8c401c6eba162)

- Extracts the failure handling for thread cache size mismatch into `safety_check_fail`, uniformly formatting diagnostic information and terminating the process under default handling. [commit](https://github.com/jemalloc/jemalloc/commit/b92c9a1a81f3f68da87afe5887d8450fef0700d3)

- When profiling and safety checks are enabled, sets and verifies a redzone of up to 32 bytes for sampled small objects to detect out-of-bounds writes; safety check failure handling can also be set via test callbacks. [commit](https://github.com/jemalloc/jemalloc/commit/33e1dad6803ea3e20971b46baa299045f736d22a)

### User API Layer

- Adds experimental mallctl utilization query interfaces `experimental.utilization.query` and `experimental.utilization.batch_query`, which can return the free region, region count, and size of the extent containing the object; single-item queries can also return slab and bin statistics and the current slab address. [commit](https://github.com/jemalloc/jemalloc/commit/9aab3f2be041b09f42375d3bf173d1a8795a1ee9)

- C++ sized `delete` / `delete[]` switch to a dedicated internal deallocation entry without flags, avoiding passing fixed zero flags through the generic `sdallocx` entry. [commit](https://github.com/jemalloc/jemalloc/commit/d3d7a8ef09b6fa79109e8930aaba7a677f8b24ac)

- Adds experimental `experimental.arenas.<i>.pactivep` control item, returning the address of the arena active page counter on supported atomic implementations for fast reads. [commit](https://github.com/jemalloc/jemalloc/commit/e13cf65a5f37bbd9b44badb198ccc138cbacc219)

### Platform Abstraction Layer

- Implements split and merge constraints for retained extents on Windows: marks VirtualAlloc region headers, allows merging only within the same retained region, and uses the corresponding release path under opt.retain. [commit](https://github.com/jemalloc/jemalloc/commit/9a86c65abc2cf242efe9354c9ce16901673eeb0c)

- On 64-bit Windows, `opt.retain` is set to enabled by default; 32-bit Windows remains disabled by default. [commit](https://github.com/jemalloc/jemalloc/commit/badf8d95f11cf8ead0f8b7192663002d1d4dc4b2)

### Cross-cutting / Other Architecture-related Changes

- The extent first-fit strategy adds a `lg_extent_max_active_fit` limit, avoiding splitting overly large extents for smaller requests; subsequently removes the independent best-fit search and optimizes early termination for over-limit candidates in first-fit search. [commit](https://github.com/jemalloc/jemalloc/commit/b62d126df894dac00772eb5f3d170a1c1d3d1614) [commit](https://github.com/jemalloc/jemalloc/commit/56797512083fe1457163170dfa44ee5ec12abe5f) [commit](https://github.com/jemalloc/jemalloc/commit/1d148f353a2c71bc12fd066e467649fd17df3c95)

## Routine Changelog

### Bug Fixes

- Both extent allocation and custom extent hooks receive alignment rounded up to at least page size, fixing alignment handling when non-page-aligned values are passed. [commit](https://github.com/jemalloc/jemalloc/commit/93084cdc8960935d0acc93424dddd3a79a86e2da)

- Fixes jeprof passing the fixed string `image` when calling `nm --demangle`, changing it to use the image path to be analyzed. [commit](https://github.com/jemalloc/jemalloc/commit/498f47e1ec83431426cdff256c23eceade41b4ef)

- Fixes the size class page multiple statistics formula: calculates the number of excluded classes according to `SC_LG_NGROUP * SC_NGROUP`, and corrects related comments. [commit](https://github.com/jemalloc/jemalloc/commit/ae124b86849bb5464940db6731183dede6a70873)

- Moves the size-class assertion in the free fastpath to after the allocated context lookup is completed, avoiding premature assertion on uninitialized contexts. [commit](https://github.com/jemalloc/jemalloc/commit/13e88ae9700416b43bf88c596ea15c85bdb9f9e7)

- Fixes the redzone setting and verification loop always accessing the first byte, changing it to write and check byte by byte. [commit](https://github.com/jemalloc/jemalloc/commit/7720b6e3851d200449914448c7163f7af92cd63f)

- Fixed the logic in `malloc_vcprintf` that cleared `cbopaque` when falling back to `je_malloc_message` output, and synchronously corrected the interface comments. [commit](https://github.com/jemalloc/jemalloc/commit/d26636d566167a439ea18da7a234f9040668023b)

- Fixed the remaining space check in the prof dump buffer, determining whether the write can complete within the buffer based on the not-yet-written `slen - i`. [commit](https://github.com/jemalloc/jemalloc/commit/e0a0c8d4bf512283e8c85fb4a51761fce5e0c08f)

- Standardized zero-length aligned allocation to be calculated as 1 bytes, avoiding `posix_memalign` / `aligned_alloc` zero-length inputs hitting error handling; added zero-length coverage in integration tests. [commit](https://github.com/jemalloc/jemalloc/commit/f32f23d6cc3ac9e663983ae62371acd47405c886)

- When the platform does not support extent splitting and retain is not enabled, the reclamation path disables unsplittable extents, avoiding leaving extents and virtual memory space as leaks. [commit](https://github.com/jemalloc/jemalloc/commit/57dbab5d6bc764a8b971334ec80977d6333688af)

- When extent metadata registration fails, the extent release path is now called instead of leaving extents on the grow, normal allocation, and gap paths as leaks. [commit](https://github.com/jemalloc/jemalloc/commit/42807fcd9ed68c78f660c6dd85bcf9d82e134244)

- In the no-tcache deallocation path, when encountering small-sized objects promoted to large by profiling, correctly call promoted deallocation; only write back to tcache when tcache is non-empty. [commit](https://github.com/jemalloc/jemalloc/commit/bc0998a9052957584b6944b6f43fffe0648f603e)

- On Windows, when retain is not enabled and regions cannot be split/merged, first-fit only accepts extents of exact size, avoiding returning candidates that cannot satisfy split conditions. [commit](https://github.com/jemalloc/jemalloc/commit/c9cdc1b27f8aa9c1e81e733e60d470c04be960b3)

- Fixed the top-level emitter start/end calls in profiling log JSON, using generic `emitter_begin` / `emitter_end` to wrap the log object. [commit](https://github.com/jemalloc/jemalloc/commit/82b8aaaeb68ccb65ca52532f4806a43fbdb26b7a)

- Added assertions to the profiling dump write loop, confirming that the number of characters processed matches the length to be written this time. [commit](https://github.com/jemalloc/jemalloc/commit/8a94ac25d597e439b05b38c013e4cb2d1169c681)

### Refactoring

- Added `stats.arenas.<i>.bins.<j>.nonfull_slabs` read-only statistics, and included the current size of non-full slab heaps in arena summaries, text, and JSON statistics output. [commit](https://github.com/jemalloc/jemalloc/commit/7fc4f2a32c74701e40e98c8ac05aa7cf12d876c9)

- Simplified the naming and invocation of configuration value bounds-checking macros in `malloc_conf_init`, improving readability of validation logic. [commit](https://github.com/jemalloc/jemalloc/commit/259b15dec5bff8b67b331b63703aa8511c759077)

- Added tcache fill/flush counts to arena small and large allocation statistics, and output them in mallctl, statistics tables, and per-second rates. [commit](https://github.com/jemalloc/jemalloc/commit/07c44847c24634d0d11f9ceab7318400ffc1a16e)

- Added `stats.arenas.<i>.abandoned_vm` statistics, accumulating the number of virtual memory bytes that had to be abandoned due to failures such as extent metadata allocation failure. [commit](https://github.com/jemalloc/jemalloc/commit/4e36ce34c1e6a6f470a9355b90b0a757c6fdb0b5)

- Extracted a shared `arena_dalloc_large` path for normal deallocation and sized deallocation to handle large categories and profiling-promoted objects. [commit](https://github.com/jemalloc/jemalloc/commit/a3fa597921987709eb0aa2258f1b35cc433ae5d4)

### Tests

- Relaxed the prof_log backtrace count test: compiler optimizations like loop unrolling may increase call sites, so changed to require at least 8 backtraces. [commit](https://github.com/jemalloc/jemalloc/commit/c2a3a7cd3f3cbc177d677101be85a31a39c26bd0)

- Moved the single-item and batch query tests for the experimental extent utilization interface from the mallctl test file to a separate `extent_util.c`, and added a separate test target. [commit](https://github.com/jemalloc/jemalloc/commit/7ee3897740aabdccb2381b7b6ab68fff0aac3ec4)

- Extended extent utilization query tests to cover multiple small/large allocation sizes, page alignment, and return fields for two size classes; also clarified that related field values are undefined when stats are not enabled. [commit](https://github.com/jemalloc/jemalloc/commit/4c63b0e76a693b0cfdf209cb4f8fbd1ed74453b0)

- On 32-bit platforms, set the retained test thread count upper limit to 16, reducing the risk of test OOM due to insufficient virtual address space. [commit](https://github.com/jemalloc/jemalloc/commit/10fcff6c38c08bc2b1a672ff92701012944d843a)

### Performance

- Changed to trylock when reading background thread statistics; skip threads when the lock is unavailable because the thread is executing a time-consuming task, avoiding waits in statistics reads. [commit](https://github.com/jemalloc/jemalloc/commit/1a71533511027dbe3f9d989659efeec446915d6b)

- Removed the unused `prof_accumbytes` 64 bit field in arena, reducing metadata usage per arena. [commit](https://github.com/jemalloc/jemalloc/commit/a2a693e722d3ec0f0fb7dfcac54e775b1837efda)

### Documentation

- Added `opt.confirm_conf` documentation: when enabled, display malloc configuration by source and output setting values item by item; this option is off by default. [commit](https://github.com/jemalloc/jemalloc/commit/c92ac306013bc95cd5f34de421b1aa5eb1f28971)

- Updated the `opt.retain` manual to explain that Windows 64-bit defaults to retaining virtual memory and the different default policies on Windows / Linux. [commit](https://github.com/jemalloc/jemalloc/commit/9f6a9f4c1f78fd61297e01ae1521af9696d2023b)

### Build / CI

- Marked emitter format generation functions with the `format_arg` attribute and adjusted format strings so the compiler can check parameter types for generated formats. [commit](https://github.com/jemalloc/jemalloc/commit/020b5dc7ac5138a347e5462508b2b5e4ecd6bc52)

- Fixed the declaration macro for the extent available tree to avoid missing-prototype warnings when compiling with warnings enabled. [commit](https://github.com/jemalloc/jemalloc/commit/14e4176758379875c4ef486d6c57327ed07edd86)

- Added Autoconf capability detection for the compiler `format_arg` attribute, and provided cross-compiler compatible macros. [commit](https://github.com/jemalloc/jemalloc/commit/7f7935cf7805036d42fb510592ab8b40bcfb0690)

- Added opt safety checks combinations to test generation configurations, covering compilation and testing scenarios with safety checks enabled. [commit](https://github.com/jemalloc/jemalloc/commit/21cfe59ff7b10a61dabe26cd3dbfb7a255e1f5e8)

- Unified the `JEMALLOC_TLS_MODEL` attribute on TLS thread-local variable declarations and definitions to avoid attribute inconsistency. [commit](https://github.com/jemalloc/jemalloc/commit/1aabab5fdca1cd76be3900e9272ef83549006ac0)

- Added a configure option to disable documentation building and installation, and display the documentation switch status in the configure summary. [commit](https://github.com/jemalloc/jemalloc/commit/702d76dbd03e4fe7347399e1e322c80102c95544)

- Fixed the switch parameter type conversion in `GET_ARG_NUMERIC`, resolving GCC 9.1 compilation warnings for that macro. [commit](https://github.com/jemalloc/jemalloc/commit/2d6d099fed05b1509e81e54458516528bfbbf38d)

- Added `safety_check.c` to Visual Studio 2015 and 2017 projects and corresponding filters, fixing the issue where MSBuild projects missed compiling this source file. [commit](https://github.com/jemalloc/jemalloc/commit/40a3435b8dc225ad61329aca89d9c8d0dfbc03ab)

- Adjusted the order of MSYS2 / MSVC configuration items and debug parameter assignment in AppVeyor. [commit](https://github.com/jemalloc/jemalloc/commit/34e75630cc512423b4f227338056a2f5d7e81740)

- Marked the possibly unused `expected` parameter in the GCC atomic compare-exchange implementation as `UNUSED`, eliminating g++ unused parameter warnings. [commit](https://github.com/jemalloc/jemalloc/commit/9344d25488b626739c9080eb471d1bd15eeb046b)

### Maintenance

- Adjusted the `confirm_conf` output format, adding a `--` marker before item-by-item configuration. [commit](https://github.com/jemalloc/jemalloc/commit/85f0cb2d0c0a05e9fc926544c65ca784c03ab239)

