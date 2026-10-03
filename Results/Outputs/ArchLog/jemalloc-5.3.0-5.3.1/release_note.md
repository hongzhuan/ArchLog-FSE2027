# Release Note

## Important Changes

### public API Layer
- The experimental thread activity callback function has been removed, and the related code has been cleaned up. (Architecture-related: public API removed)
  ↳ [#2876](https://github.com/jemalloc/jemalloc/pull/2876): [176ea0a](https://github.com/jemalloc/jemalloc/commit/176ea0a801338cae1b938c47f0d7dba7ffef0d25)
- Change tcache_max and nhbins to per-thread, allow each thread to set its own tcache_max via mallctl, store the maximum number of items per bin thread-local, and rename global variables to emphasize that they should not be modified directly. (Architecture-related: public API)
  ↳ [#2493](https://github.com/jemalloc/jemalloc/pull/2493): [a442d9b](https://github.com/jemalloc/jemalloc/commit/a442d9b895935ac872e7ccc705213537bc747c19)
- Removed the build-time configuration config_limit_usize_gap, and simplified the conditional judgment in related functions. (Architecture-related: build configuration)
  ↳ [#2835](https://github.com/jemalloc/jemalloc/pull/2835): [01e9ecb](https://github.com/jemalloc/jemalloc/commit/01e9ecbeb2fa69ae8e9f3e1013c9f7d44f6d033e)
- Added user event support to the thread event system when statistics are enabled. (Architecture-related: public API)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [015b017](https://github.com/jemalloc/jemalloc/commit/015b017973d47f3047f8f4d7349c937fefd30f99)
- Added mallctl interface, allowing users to obtain the approximate number of active bytes. (Architecture-related: public API)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [0988583](https://github.com/jemalloc/jemalloc/commit/0988583d7cd67cb9a5327c5e326b56d63f89cf16)
- Handle tcache initialization failure gracefully: disable tcache and log an error when it fails, and abort if opt_abort is true. (Architecture-related: behavioral contract)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [a056c20](https://github.com/jemalloc/jemalloc/commit/a056c20d671e5d001d9d232a7c6d9bb30288e9ef)
- Implemented malloc_getcpu function on amd64 and arm64 architectures of macOS, and enabled per-CPU area allocation. (Architecture-related: public API)
  ↳ [#2291](https://github.com/jemalloc/jemalloc/pull/2291): [4e12d21](https://github.com/jemalloc/jemalloc/commit/4e12d21c8ddb9a70a12c8194c8b6c331fad7154a) | No PR: [df8f7d1](https://github.com/jemalloc/jemalloc/commit/df8f7d10af15d549ab73ba807b2e14a9d7fe1cc2)
- Implemented the C23 standard free_sized and free_aligned_sized functions, and added the corresponding libc alias. (Architecture-related: public API)
  ↳ [#2482](https://github.com/jemalloc/jemalloc/pull/2482): [cdb2c0e](https://github.com/jemalloc/jemalloc/commit/cdb2c0e02fc303fd56aa525ef63eb71136e62b2d)
- Added compile-time malloc_conf override support in jemalloc_internal_overrides.h. (Architecture-related: compile-time configuration override)
  ↳ [#2499](https://github.com/jemalloc/jemalloc/pull/2499): [b01d496](https://github.com/jemalloc/jemalloc/commit/b01d49664651f239fdf76774cb6de05ed7e63f4a) | [#2453](https://github.com/jemalloc/jemalloc/pull/2453): [a2259f9](https://github.com/jemalloc/jemalloc/commit/a2259f9fa6c9a82cacf1d85cf7d92a1a44484a97)
- Added support for the deprecated attribute, and added diagnostic macros for suppressing deprecated declaration warnings. (Architecture-related: public API)
  ↳ [#2506](https://github.com/jemalloc/jemalloc/pull/2506): [120abd7](https://github.com/jemalloc/jemalloc/commit/120abd703addce50fb9105ee4f7e42c3612c3774)
- Added the function of setting and obtaining ncached_max of each cache bin through the mallctl interface, and supports setting the default value through malloc_conf. (Architecture-related: public API)
  ↳ [#2530](https://github.com/jemalloc/jemalloc/pull/2530): [630f7de](https://github.com/jemalloc/jemalloc/commit/630f7de9520efeec096a604ce02bc7aef7b46a94) | [#2555](https://github.com/jemalloc/jemalloc/pull/2555): [8a22d10](https://github.com/jemalloc/jemalloc/commit/8a22d10b834cb66cce3e62dfc7606d8a491fe50b)
- Added replacement support for the deprecated function pvalloc to ensure that jemalloc can correctly handle this function when replacing the GLIBC allocator. (Architecture-related: public API compatibility)
  ↳ [#2257](https://github.com/jemalloc/jemalloc/pull/2257): [5b1f2cc](https://github.com/jemalloc/jemalloc/commit/5b1f2cc5d79672e0d8852da1b705d68a74d22cd4)
- Added double release detection for the thread cache in the debug build, and added a new runtime option debug_double_free_max_scan to control the scan depth. (Architecture-related: public API: New runtime option)
  ↳ No PR: [36366f3](https://github.com/jemalloc/jemalloc/commit/36366f3c4c741723369853c923e56999716398fc)
- Fixed compilation errors caused by exception specification mismatch on the musl C library system, by adjusting the conditional macro so that the musl system does not define JEMALLOC_SYS_NOTHROW. (Architecture-related: platform compatibility)
  ↳ [#2338](https://github.com/jemalloc/jemalloc/pull/2338): [45249cf](https://github.com/jemalloc/jemalloc/commit/45249cf5a9cfa13c2c62e68e272a391721523b4b)
- Fixed a possible segmentation fault caused by a null pointer in mallctl("prof.prefix", ...), and added a check to see if prefix is NULL. (Architecture-related: public API)
  ↳ [#2436](https://github.com/jemalloc/jemalloc/pull/2436): [0288126](https://github.com/jemalloc/jemalloc/commit/0288126d9cc0d061766e37cbbaabaa78aff3aff5)
- Removed the incorrectly introduced intermediate generated header file inclusion in the public header file jemalloc.h (architecture-related: public API)
  ↳ [#2492](https://github.com/jemalloc/jemalloc/pull/2492): [8ff7e7d](https://github.com/jemalloc/jemalloc/commit/8ff7e7d6c33fd18a9f8c9f086e027dd0edfc27f0)
- Allow zero-sized memalign allocations to pass and no longer trigger assertion failures. (Architecture-related: public API)
  ↳ [#2606](https://github.com/jemalloc/jemalloc/pull/2606): [1aba4f4](https://github.com/jemalloc/jemalloc/commit/1aba4f41a3fef53fa913e655444dbba53a0c82df)
- Fixed the problem of incorrectly setting errno when memory allocation fails, ensuring that realloc() sets errno to ENOMEM in OOM. (Architecture-related: external behavior)
  ↳ [#2620](https://github.com/jemalloc/jemalloc/pull/2620): [38056fe](https://github.com/jemalloc/jemalloc/commit/38056fea64c34ca4fef0a16212776eaa4de80b78) | [#2633](https://github.com/jemalloc/jemalloc/pull/2633): [83b0757](https://github.com/jemalloc/jemalloc/commit/83b075789b4239035931c1ee212576d00153bbf0)
- Fixed and removed the temporary option experimental_hpa_strict_min_purge_interval, so that the minimum purge interval check always takes effect, and fixed the logic error that caused this option to only purge one page at a time, instead purging multiple pages at once after the minimum interval is met. (Architecture-related: public API)
  ↳ [#2686](https://github.com/jemalloc/jemalloc/pull/2686): [143f458](https://github.com/jemalloc/jemalloc/commit/143f458188d2d5a02418e7f72e56152dab118786) | [#2701](https://github.com/jemalloc/jemalloc/pull/2701): [4f4fd42](https://github.com/jemalloc/jemalloc/commit/4f4fd424477142ee9962fcf4e4cd0349d4e6e4d3)
- Updated the JEMALLOC_CXX_THROW macro definition from throw() to noexcept(true) to be compatible with C++17 and newer versions. (Architecture-related: public API)
  ↳ [#2656](https://github.com/jemalloc/jemalloc/pull/2656): [21bcc0a](https://github.com/jemalloc/jemalloc/commit/21bcc0a8d49ab2944ae53c7e43f5c84fc8a34322)
- Fixed the problem of not checking the input to be 0 when setting max_background_threads through mallctl. Now the 0 value will be rejected and an error will be returned. (Architecture-related: external behavior)
  ↳ [#2787](https://github.com/jemalloc/jemalloc/pull/2787): [607b866](https://github.com/jemalloc/jemalloc/commit/607b86603532b59c35cfdf9abd61a0c14966092b)
- Moved extern "C" declarations to only required locations, fixed error in compiling C++ code when clang enabled modules. (Architecture-related: public API)
  ↳ [#2821](https://github.com/jemalloc/jemalloc/pull/2821): [80e9001](https://github.com/jemalloc/jemalloc/commit/80e9001af33558c4ea991fcf5a715f3a7942a40e)
- Fixed the return value error caused by the lack of inversion operation when usize_min was rolled back in the large_ralloc_no_move function, and added corresponding unit tests. (Architecture-related: public API)
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [a0f2bdf](https://github.com/jemalloc/jemalloc/commit/a0f2bdf91ddd4e5662790c7cd877052c9009441d)
- Fixed an issue where conf_handle_char_p could incorrectly modify the buffer when the target buffer size is zero, and removed the unused conf_handle_unsigned function. (Architecture-related: Configuration processing behavior)
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [b507644](https://github.com/jemalloc/jemalloc/commit/b507644cb084d095917aea6e2573c702caff3e5a)
- Reconstructed the tcache initialization logic, precalculated and stored the default ncached_max value of all bins at startup, added an interface to obtain the default ncached_max, and unified the initialization process to support the tunable experience of tcache_max. (Architecture-related: public API)
  ↳ [#2530](https://github.com/jemalloc/jemalloc/pull/2530): [6b197fd](https://github.com/jemalloc/jemalloc/commit/6b197fdd460be8bf3379da91d42e677dd5b5437a) | [#2555](https://github.com/jemalloc/jemalloc/pull/2555): [6fb3b6a](https://github.com/jemalloc/jemalloc/commit/6fb3b6a8e45d3e5f83b331ce8a1d41c5e5da3f4c)
- Remove unnecessary parameters in the cache_bin_postincrement function call, and adjust related code formats. (Architecture-related: public API)
  ↳ [#2493](https://github.com/jemalloc/jemalloc/pull/2493): [fbca96c](https://github.com/jemalloc/jemalloc/commit/fbca96c4332380c5799dcc804365ac6e93d7db2f)
- Rename option hpa_strict_min_purge_interval to experimental_hpa_strict_min_purge_interval to clarify its experimental nature. (Architecture-related: public API)
  ↳ [#2686](https://github.com/jemalloc/jemalloc/pull/2686): [c7ccb8d](https://github.com/jemalloc/jemalloc/commit/c7ccb8d7e99a1c3f1ba3cc3e465bc6dd1b0fbe0b)
- Rename the runtime option opt.limit_usize_gap to opt.disable_large_size_classes, and update the conditional judgments and comments in related internal functions. (Architecture-related: public API)
  ↳ [#2835](https://github.com/jemalloc/jemalloc/pull/2835): [8347f10](https://github.com/jemalloc/jemalloc/commit/8347f1045aaf975192b06c3168a40a05ae8c206a)
- Added test cases to verify that there are no race conditions in background thread initialization. (Architecture-related: background thread initialization)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [4d0ffa0](https://github.com/jemalloc/jemalloc/commit/4d0ffa075b93fe9263cfd5f11467b2e8df44ed93)
- Added a new test to verify the consistency of JSON statistical output and mallctl results. (Architecture-related: JSON statistical output)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [c73ab1c](https://github.com/jemalloc/jemalloc/commit/c73ab1c2ff9c47ad56c2d550b7481bbc80119bcb)
- Add explicit unsigned type conversion to MALLOCX_ARENA and MALLOCX_TCACHE macros. (Architecture-related: public API)
  ↳ [#2445](https://github.com/jemalloc/jemalloc/pull/2445): [d577e9b](https://github.com/jemalloc/jemalloc/commit/d577e9b5880906dbd4ab04fb61de5650170ac08b)
- Introduced a new usize calculation strategy, rounding up large size allocations to page multiples to reduce memory waste, and added build-time and run-time configuration options. (Architecture-related: public API)
  ↳ [#2646](https://github.com/jemalloc/jemalloc/pull/2646): [c067a55](https://github.com/jemalloc/jemalloc/commit/c067a55c790bebd69fd6d87935f8c353524ef814)
- Introduced the runtime option opt_calloc_madvise_threshold, which uses memset to clear when the allocation size is less than the threshold, as an experimental calloc implementation. (Architecture-related: public API)
  ↳ [#2631](https://github.com/jemalloc/jemalloc/pull/2631): [5081c16](https://github.com/jemalloc/jemalloc/commit/5081c16bb49a0c9d1dde3cbd7dfb2e97c2827ea4)
- Added arenas.hugepage control interface, used to export hugepage size and output the value in statistics. (Architecture-related: public API)
  ↳ [#2652](https://github.com/jemalloc/jemalloc/pull/2652): [90c627e](https://github.com/jemalloc/jemalloc/commit/90c627edb70e081e1298b79010478d2f804467f1)
- Added hpa_strict_min_purge_interval option, which is used to control whether the minimum purge interval is strictly followed. It is turned off by default to maintain backward compatibility. (Architecture-related: public API)
  ↳ [#2658](https://github.com/jemalloc/jemalloc/pull/2658): [867c6dd](https://github.com/jemalloc/jemalloc/commit/867c6dd7dc88adb0489b8b815dd70c68807325fc)
- Added hpa_hugify_sync option to support synchronous transparent huge page folding and fall back to asynchronous mode in case of failure. (Architecture-related: public API)
  ↳ [#2750](https://github.com/jemalloc/jemalloc/pull/2750): [0ce13c6](https://github.com/jemalloc/jemalloc/commit/0ce13c6fb5ae3bd837f5a7314bd580070bb408da)

### Instrumentation & Profiling Layer
- Split the TSD implementation details into a new tsd_internals.h file, so that each TSD implementation header file explicitly includes its dependencies, and the header file is self-contained. (Architecture event: core internal module reorganization)
  ↳ [#2463](https://github.com/jemalloc/jemalloc/pull/2463): [856db56](https://github.com/jemalloc/jemalloc/commit/856db56f6ec54f59491fa7897dab9a23d5bf9ff4)
- Separate the code related to configuration parsing and initialization from src/jemalloc.c and separate it into the src/conf.c file. (Architecture event: core internal module reorganization)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [ad726ad](https://github.com/jemalloc/jemalloc/commit/ad726adf7539f78bf652db04f215333f1536bf85)
- Remove the macro definition in thread_event, use dynamic event objects instead, and reconstruct the event processing mechanism. (Architecture events: Reconstruction of the core internal module event processing mechanism)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [e6864c6](https://github.com/jemalloc/jemalloc/commit/e6864c6075a9fdeea56f788588652f2cefb996b6)
- Added prof_threshold allocation callback to provide a low-overhead threshold notification mechanism. (Architecture-related: public API)
  ↳ [#2773](https://github.com/jemalloc/jemalloc/pull/2773): [257e64b](https://github.com/jemalloc/jemalloc/commit/257e64b968ec40c285331dfb6e3db8a2b34999d1)
- Add HPA slab retention statistics in JSON output. (Architecture-related: JSON output)
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [f265645](https://github.com/jemalloc/jemalloc/commit/f265645d02f0bde59833c46977b66acd94dec42e)
- Added experimental USDT SystemTap probe support, and added multiple tracking points in HPA, sec and other modules. (Architecture event: USDT probe support)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [711fff7](https://github.com/jemalloc/jemalloc/commit/711fff750ce904d0b881a6fe534732dcb75874e6), [f87bbab](https://github.com/jemalloc/jemalloc/commit/f87bbab22cf5a81dd314c7811867edc5c69025d2), [d70882a](https://github.com/jemalloc/jemalloc/commit/d70882a05d02e21c27990d4c6deb5c5bf614d9ec)
- Change the maximum stack depth of jemalloc's backtrace to a runtime configurable option. (Architecture-related: public API)
  ↳ [#2319](https://github.com/jemalloc/jemalloc/pull/2319): [a0734fd](https://github.com/jemalloc/jemalloc/commit/a0734fd6ee326cd2059edbe4bca7092988a63684)
- Add name setting and reading functions for arena, and add explicit names for dedicated oversized arenas to make malloc_stats output more readable. (Architecture-related: public API)
  ↳ [#2325](https://github.com/jemalloc/jemalloc/pull/2325): [ba19d2c](https://github.com/jemalloc/jemalloc/commit/ba19d2cb78176ef715aca461c7a7a7b2afb35772) | [#2381](https://github.com/jemalloc/jemalloc/pull/2381): [b612512](https://github.com/jemalloc/jemalloc/commit/b6125120ac22c2c7e7cd36df114a2b280dcc33e7)
- Add experimental prof_sample and prof_sample_free hooks, allowing advanced users to track additional information when allocating and freeing sample objects. (Architecture-related: public API)
  ↳ [#2360](https://github.com/jemalloc/jemalloc/pull/2360): [8580c65](https://github.com/jemalloc/jemalloc/commit/8580c65f81c5252e493da656a448ec3a8571dab7)
- Enable heap analysis on MacOS, add Mach-O image address handling code to support memory map dumps. (Architecture-related: platform compatibility)
  ↳ [#2610](https://github.com/jemalloc/jemalloc/pull/2610): [4b555c1](https://github.com/jemalloc/jemalloc/commit/4b555c11a54d31ba941d996011c7063b2083a12e)
- Add pid namespace support to the heap profile file name. When this option is enabled, the file name contains the namespace identifier to distinguish processes in different namespaces. (Architecture-related: public API)
  ↳ [#2636](https://github.com/jemalloc/jemalloc/pull/2636): [11038ff](https://github.com/jemalloc/jemalloc/commit/11038ff762a2ba11eec26d3ffb32026424d2ccfe)
- Expand the public API of page allocator sharding statistics, add three getter functions pa_shard_nactive, pa_shard_ndirty and pa_shard_nmuzzy, and expose psset internal status statistics to mallctl and malloc statistical output. (Architecture-related: public API)
  ↳ [#2622](https://github.com/jemalloc/jemalloc/pull/2622): [b2e59a9](https://github.com/jemalloc/jemalloc/commit/b2e59a96e1ffc953300c5b69ffae934a63de38c0) | [#2761](https://github.com/jemalloc/jemalloc/pull/2761): [6092c98](https://github.com/jemalloc/jemalloc/commit/6092c980a6d02b34bc7b3ed0c2ad923d0a5d2970)
- Optimize time-related functions, add support for clock_gettime_nsec_np to replace mach_absolute_time, and add nstime_ms_since function, which will be abbreviated to nstime_ms. (Architecture-related: public API)
  ↳ [#2733](https://github.com/jemalloc/jemalloc/pull/2733): [6d625d5](https://github.com/jemalloc/jemalloc/commit/6d625d5e5e06b5a07ab90c37ef6b03b55ca1c00a) | [#2746](https://github.com/jemalloc/jemalloc/pull/2746): [b9758af](https://github.com/jemalloc/jemalloc/commit/b9758afff037fb074a440bb5590ed113cad78bd3)
- Change the platform condition for setting the background thread name to use the configuration macro JEMALLOC_HAVE_PTHREAD_SET_NAME_NP to improve cross-platform compatibility. (Architecture-related: platform compatibility)
  ↳ [#2435](https://github.com/jemalloc/jemalloc/pull/2435): [6ea8a7e](https://github.com/jemalloc/jemalloc/commit/6ea8a7e928c86f7976c5e1356a22292509f8705b)
- Fix the macro definition of PowerPC architecture in quantum.h, expand the detection conditions to support more PowerPC variants, and ensure correct compilation on platforms such as Darwin PPC. (Architecture-related: platform compatibility)
  ↳ [#2281](https://github.com/jemalloc/jemalloc/pull/2281): [70e3735](https://github.com/jemalloc/jemalloc/commit/70e3735f3a71d3e05faa05c58ff3ca82ebaad908)
- Fix build issues for the OpenBSD platform, enable pthread name related APIs, and disable per-thread CPU affinity handling that is not supported by this platform. (Architecture-related: Platform compatibility)
  ↳ No PR: [5847841](https://github.com/jemalloc/jemalloc/commit/58478412be842e140cc03dbb0c6ce84b2b8d096e)
- Fix the compilation error of the implicit declaration of the pthread_create_fptr_init function, advance its definition and adjust the conditional compilation indentation, and add dlsym fallback logic and affinity setting processing of the OpenBSD platform. (Architecture-related: platform compatibility)
  ↳ [#2322](https://github.com/jemalloc/jemalloc/pull/2322): [56ddbea](https://github.com/jemalloc/jemalloc/commit/56ddbea270e5c73ba5a4977550e02c2b3706ae80)
- Fixed build issues on non-Linux/BSD platforms and adjusted the conditional judgment of thread affinity settings. (Architecture-related: platform compatibility)
  ↳ [#2341](https://github.com/jemalloc/jemalloc/pull/2341): [4c95c95](https://github.com/jemalloc/jemalloc/commit/4c95c953e2c4b443d930d3b41abb17eb38f075f5)
- In jemalloc_internal_types.h, when the compiler does not support variable-length arrays (such as __STDC_NO_VLA__ is defined), fall back to using alloca() to be compatible with compilers such as MSVC. (Architecture-related: platform compatibility)
  ↳ [#2347](https://github.com/jemalloc/jemalloc/pull/2347): [be65438](https://github.com/jemalloc/jemalloc/commit/be65438f20a5fe4fdc5c5bb2cfa7ba3f0e9da378)
- Inline the storage of thread names into the prof_tdata_t structure to solve race conditions caused by separate buffers and avoid internal memory allocation and release during the sampling process; at the same time, rearrange the Boolean fields to optimize the structure size. (Architecture-related: public API behavior changes)
  ↳ [#2407](https://github.com/jemalloc/jemalloc/pull/2407): [ce0b7ab](https://github.com/jemalloc/jemalloc/commit/ce0b7ab6c8d7a3579d012c227013f5143d9bc8c6), [6cab460](https://github.com/jemalloc/jemalloc/commit/6cab460a45411316426fb44bd476214d6af36d47), [e62aa47](https://github.com/jemalloc/jemalloc/commit/e62aa478c79865242363d3531fc58c4c7f65a1b4)
- Fixed the segmentation fault caused by empty nodes in the red-black tree deletion operation, and adjusted the parameter type of the large memory release safety check function and added the upper limit check. (Architecture-related: public API)
  ↳ [#2433](https://github.com/jemalloc/jemalloc/pull/2433): [90176f8](https://github.com/jemalloc/jemalloc/commit/90176f8a87a0b5bdb0ac4c1a515b1d9c58dc5a82)
- Fixed the problem that oversize_arena cannot create background threads when background_thread is enabled, ensuring that the cleanup operation does not stall under low arena numbers. (Architecture-related: public API)
  ↳ [#2642](https://github.com/jemalloc/jemalloc/pull/2642): [8d8379d](https://github.com/jemalloc/jemalloc/commit/8d8379da443f46dc976252b968cb9ca8e63ec974)
- Fix the NSTIME_MONOTONIC flag in the Win32 implementation and set it to false to avoid crashes caused by system time adjustment. (Architecture-related: platform compatibility)
  ↳ [#2669](https://github.com/jemalloc/jemalloc/pull/2669): [8dc97b1](https://github.com/jemalloc/jemalloc/commit/8dc97b11089be6d58a52009ea3da610bf90331d3)
- Add configure to check whether the gettid() function exists, and add conditional compilation in prof_stack_range.c, and fix macro definition errors to ensure compatibility on old glibc versions. (Architecture-related: platform compatibility)
  ↳ [#2754](https://github.com/jemalloc/jemalloc/pull/2754): [17881eb](https://github.com/jemalloc/jemalloc/commit/17881ebbfd76529904e826f425f3266834cf3a75) | [#2786](https://github.com/jemalloc/jemalloc/pull/2786): [20cc983](https://github.com/jemalloc/jemalloc/commit/20cc983314ecf14ac08ccf0d60ce7e41f88babf6)
- Added RTLD_DEFAULT fallback to pthread_create's dlsym lookup to address possible failure of RTLD_NEXT in shared libraries. (Architecture-related: Platform compatibility)
  ↳ [#2812](https://github.com/jemalloc/jemalloc/pull/2812): [86bbaba](https://github.com/jemalloc/jemalloc/commit/86bbabac32775bdf414318e57e626febb9b6eac1)
- On non-Windows platforms, an interrupt retry mechanism is added to the read and write system calls to avoid failure of read and write operations due to signal interruption. (Architecture-related: platform compatibility)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [9fdc116](https://github.com/jemalloc/jemalloc/commit/9fdc1160c5793d99f26192aee0406c653affb484)
- Fixed an issue where large object allocation request count nrequests was undercounted on cache miss. (Architecture-related: allocation counting behavior)
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [3cc56d3](https://github.com/jemalloc/jemalloc/commit/3cc56d325c15cdb7d6047ed513ab908121c66698)
- Removed the built-in prof_threshold event and related configurations, hook functions and tests. This function can be easily implemented as a user event. (Architecture event: core internal module changes)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [34ace91](https://github.com/jemalloc/jemalloc/commit/34ace9169bad794cea6f8639e188d83b42310762)
- Optimize the lock acquisition logic, no longer set the locked flag when acquisition fails, avoid unnecessary spin, and improve concurrency performance. (Architecture-related: external behavior)
  ↳ [#2371](https://github.com/jemalloc/jemalloc/pull/2371): [5f64ad6](https://github.com/jemalloc/jemalloc/commit/5f64ad60cdd2359249c863c2a01f8555672d7c35)
- Rollback changes to the experimental configuration option "prefetch from cache_bin fast path". (Architecture-related: configuration interface)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [d4908fe](https://github.com/jemalloc/jemalloc/commit/d4908fe44a869858840fc7b9d4d3e69a3629a25f)
- Use cache_bin_sz_t type alias instead of directly using uint16_t. (architecture-related: public API)
  ↳ [#2847](https://github.com/jemalloc/jemalloc/pull/2847): [5e460bf](https://github.com/jemalloc/jemalloc/commit/5e460bfea25c39d9bf8ea0077c3b6740e9515487)
- Change the small allocation memory alignment of heap analysis sampling from rounding up to SC_LARGE_MINCLASS to rounding up to PAGE, reducing memory overhead, by 4 times in extreme cases. (Architecture-related: Heap analysis sampling alignment)
  ↳ [#2459](https://github.com/jemalloc/jemalloc/pull/2459): [5a858c6](https://github.com/jemalloc/jemalloc/commit/5a858c64d6f049c64c11baf907ab8655e6ed72a3)
- Add experimental configuration options for prefetching data from the cache bin in the fast path. (Architecture-related: Experimental configuration options)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [d73de95](https://github.com/jemalloc/jemalloc/commit/d73de95f722247a56b5266a27267cd24668081e9)
- Added usize field to prof_sample_hook_t, and added corresponding verification logic in the test. (Architecture-related: public API)
  ↳ [#2682](https://github.com/jemalloc/jemalloc/pull/2682): [bc32ddf](https://github.com/jemalloc/jemalloc/commit/bc32ddff2da6e58df90b1762f17519a2c04b26b0)

### Extent & Page Management Layer
- Extract the hpa_central component from the HPA source file and migrate it to the new file src/hpa_central.c. (Architecture event: core internal module reorganization)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [8a06b08](https://github.com/jemalloc/jemalloc/commit/8a06b086f3b514764c1924451ec453a67444470b)
- Transfer the ownership of the SEC cache to the HPA shard, simplify the code implementation, add fine-grained statistical information for each bin, and introduce a per-bin granular locking mechanism. (Architecture-related: Module responsibility changes)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [6016d86](https://github.com/jemalloc/jemalloc/commit/6016d86c187ce01ef8cbe1c3023a3ca394c9b47f) | [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [6281482](https://github.com/jemalloc/jemalloc/commit/6281482c395fdbf721ff1f09f531315744446b35)
- Add transparent huge page (THP) automatic enablement support for huge arena in PAC. (Architecture-related: transparent huge page support)
  ↳ [#2810](https://github.com/jemalloc/jemalloc/pull/2810): [e1a77ec](https://github.com/jemalloc/jemalloc/commit/e1a77ec5583702429fbe7c42e7ad37dfd5517cce)
- Allow overriding the LG_PAGE configuration by defining the JEMALLOC_OVERRIDE_LG_PAGE macro. (Architecture-related: build configuration)
  ↳ [#2441](https://github.com/jemalloc/jemalloc/pull/2441): [4e6f1e9](https://github.com/jemalloc/jemalloc/commit/4e6f1e920814eafb4ca165a861e9c886022b35e3)
- Added the --enable-pageid configuration option to add identification to the memory map through prctl in Linux 5.17 and above kernels to facilitate identification in /proc/<pid>/maps. (Architecture-related: build and installation methods)
  ↳ No PR: [4fc5c4f](https://github.com/jemalloc/jemalloc/commit/4fc5c4fbac156c9f44452d3f30216451711dfa18)
- HPA allows frequently reused allocations to bypass the slab_max_alloc limit, and adds a new batch allocation function. (Architecture-related: public API)
  ↳ [#2593](https://github.com/jemalloc/jemalloc/pull/2593): [a2c5267](https://github.com/jemalloc/jemalloc/commit/a2c52674091c53f6af1ac8b7ef8849bc7797a5ad)
- The HPA large page allocator adds sliding window-based peak demand tracking, huge page initialization capabilities, time-based cleanup delay and intelligent candidate selection, and experimental options to force hugify. (Architecture-related: public API)
  ↳ [#2780](https://github.com/jemalloc/jemalloc/pull/2780): [ad108d5](https://github.com/jemalloc/jemalloc/commit/ad108d50f1c30700389103ff5fe3ef5f538f804c) | [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [a199278](https://github.com/jemalloc/jemalloc/commit/a199278f3711bc0806e15e2f5f16004f3b287177), [47aeff1](https://github.com/jemalloc/jemalloc/commit/47aeff1d08806deb4ea8f91535f5470d7de89915)
- Added process_madvise system call support, and added experimental options to force the use of this call first. (Architecture-related: public API)
  ↳ [#2794](https://github.com/jemalloc/jemalloc/pull/2794): [22440a0](https://github.com/jemalloc/jemalloc/commit/22440a0207cd7d7c624c78723ca1eeb8a4353e79) | [#2841](https://github.com/jemalloc/jemalloc/pull/2841): [852da1b](https://github.com/jemalloc/jemalloc/commit/852da1be150e9811a3f0ab91302c5d6e9ee62e4f)
- Fix an issue where HPA configuration could cause an infinite purge loop, verify HPA settings at the end of configuration parsing, and normalize or abort based on abort_conf option. (Architecture-related: configuration behavior)
  ↳ [#2484](https://github.com/jemalloc/jemalloc/pull/2484): [3aae792](https://github.com/jemalloc/jemalloc/commit/3aae792b1021a3e46490bd52e8b3300c3aa71e82)
- Fixed the problem of VM over-reservation when using large pages (such as 512M) on aarch64, changed the initial growth value from HUGEPAGE to a fixed 2M, and added basic block size alignment processing; at the same time, added an expected value check for huge page size when HPA is enabled. (Architecture-related: platform compatibility)
  ↳ [#2628](https://github.com/jemalloc/jemalloc/pull/2628): [cd05b19](https://github.com/jemalloc/jemalloc/commit/cd05b19f10fce353105dcc7290a8374a5c4f4a67), [3383b98](https://github.com/jemalloc/jemalloc/commit/3383b98f1b9a2e60ec0bda2fcf463ba271926596)
- Changed macOS mmap tag from 101 to 254 to avoid tag conflict with CoreMedia. (Architecture-related: platform compatibility)
  ↳ [#2659](https://github.com/jemalloc/jemalloc/pull/2659): [c893fcd](https://github.com/jemalloc/jemalloc/commit/c893fcd169fffca1b9d3156c6637a197765b82d0)
- Disable the psset test under an excessively large hugepage, and add logic to return false when the hugepage size exceeds the limit in the HPA support check. (Architecture-related: platform compatibility)
  ↳ [#2770](https://github.com/jemalloc/jemalloc/pull/2770): [587676f](https://github.com/jemalloc/jemalloc/commit/587676fee8a77046e67d3ae8eb26e5456b6da481)
- Reconstructed the HPA cleanup logic, added a vectorized cleanup function for batch processing of multiple large pages, and extracted independent tool functions to support cross-page calls. (Architecture-related: public API)
  ↳ [#2827](https://github.com/jemalloc/jemalloc/pull/2827): [cfa90df](https://github.com/jemalloc/jemalloc/commit/cfa90dfd80c4b3ca2b2678fb55cfc718bd9f42c6)
- Removed the pidfd_open system call, used the PIDFD_SELF constant instead, and added errno save/restore and process madvise gating checks. (Architecture-related: platform compatibility)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [5d5f76e](https://github.com/jemalloc/jemalloc/commit/5d5f76ee015696e0e086650e85722ceca9d191c1)
- Reconstruct the Transparent Huge Page (THP) state initialization logic, extract the function that determines whether to skip setting the THP state, and output init_system_thp_mode in malloc statistics. (Architecture-related: public API)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [2cfa419](https://github.com/jemalloc/jemalloc/commit/2cfa41913e71b0ff24788812f61d5485f04b647d)
- Introduced the option experimental_hpa_max_purge_nhp, which limits the maximum number of hugepages cleaned in each cleaning operation and provides backward-compatible behavior control. (Architecture-related: public API)
  ↳ [#2686](https://github.com/jemalloc/jemalloc/pull/2686): [aaa2900](https://github.com/jemalloc/jemalloc/commit/aaa29003ab90b574c29dc4c0c331085c07f1c1fd)
- Support HPA vectorized cleanup, use process_madvise to reduce system calls, and support vectorized cleanup across multiple large pages, introducing a batch processing mechanism to limit the number of ranges for each system call. (Architecture-related: public API)
  ↳ [#2820](https://github.com/jemalloc/jemalloc/pull/2820): [f19f49e](https://github.com/jemalloc/jemalloc/commit/f19f49ef3ed34e1a74851f112677a9045a0b15f8) | [#2827](https://github.com/jemalloc/jemalloc/pull/2827): [1956a54](https://github.com/jemalloc/jemalloc/commit/1956a54a434ec365fad22d7497d86495b0c31883)
- When HUGEPAGE is too large, HPA function is no longer supported. (Architecture-related: core module)
  ↳ [#2723](https://github.com/jemalloc/jemalloc/pull/2723): [1c90008](https://github.com/jemalloc/jemalloc/commit/1c900088c33402cc8bb0ea78dc1338ab6c087e0c)

### Arena & Metadata Layer
- Move bin-related functions in arena.c to bin.c, add bin_ prefix uniformly, and change functions that rely on arena_is_auto check to accept is_auto parameters. (Architecture event: core internal module reorganization)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [1cc563f](https://github.com/jemalloc/jemalloc/commit/1cc563f531ae26ffa17f7afb3568cf773d80550a)
- Fixed the problem of incorrectly using the global oversize_threshold when arena selection is oversized, instead using each arena's own threshold. (Architecture-related: public API)
  ↳ [#2460](https://github.com/jemalloc/jemalloc/pull/2460): [86eb49b](https://github.com/jemalloc/jemalloc/commit/86eb49b47847e48390c672371987ff4e476e53a3)
- Mark arena's bins field as deprecated, internal code access through the all_bins field instead, and suppress warnings for known legal locations. (Architecture-related: public API)
  ↳ [#2506](https://github.com/jemalloc/jemalloc/pull/2506): [424dd61](https://github.com/jemalloc/jemalloc/commit/424dd61d57500712fad7371bfd921cb9e3caee22)
- Change the fill parameter of the arena_cache_bin_fill_small function from a single fixed value to accept a minimum and maximum value range to support a more flexible filling strategy. (Architecture-related: public API)
  ↳ [#2685](https://github.com/jemalloc/jemalloc/pull/2685): [14d5dc1](https://github.com/jemalloc/jemalloc/commit/14d5dc136a40ddf2464f2178f950b562f38f0d25)

### Cross-cutting / Other Architecture-related Changes
- Updated the default value of opt_experimental_tcache_gc to enabled, and changed the default value of opt_calloc_madvise_threshold from 0 to 8 MB. (Architecture-related: configuration default value change)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [a952a3b](https://github.com/jemalloc/jemalloc/commit/a952a3b8b08a63609172c8c84cf6eb09de9fc7be)
- Added --enable-force-getenv configuration option, allowing getenv() to be used to read MALLOC_CONF in setuid scenarios, disabled by default. (Architecture-related: build configuration)
  ↳ [#2352](https://github.com/jemalloc/jemalloc/pull/2352): [481bbfc](https://github.com/jemalloc/jemalloc/commit/481bbfc9906e7744716677edd49d0d6c22556a1a)
- Added infrastructure for the tcache batching function, including introducing bin types with batch processing capabilities, initializing batcher, handling fork locks, and adding batch allocation functions to improve multi-threading performance. (Architecture-related: public API)
  ↳ [#2608](https://github.com/jemalloc/jemalloc/pull/2608): [c085530](https://github.com/jemalloc/jemalloc/commit/c085530c711fb233203963cd93dfa9339b0b9980), [fc61573](https://github.com/jemalloc/jemalloc/commit/fc615739cbd15dcb4a60c611206d9b8817aab565), [f9c0b5f](https://github.com/jemalloc/jemalloc/commit/f9c0b5f7f8a917661db39289e38ec94d9d198f11) | [#2695](https://github.com/jemalloc/jemalloc/pull/2695): [8c54637](https://github.com/jemalloc/jemalloc/commit/8c54637f8c7a98bbaec6ee38229a904bbf22170c) | [#2710](https://github.com/jemalloc/jemalloc/pull/2710): [60f472f](https://github.com/jemalloc/jemalloc/commit/60f472f367121d7d4933d0237ff38276f565fc88)
- Introduced a new tcache GC design, added a new runtime option opt_experimental_tcache_gc to control the new GC strategy, and introduced locality awareness in GC flush to prioritize flushing remote or idle items. (Architecture-related: runtime options)
  ↳ [#2685](https://github.com/jemalloc/jemalloc/pull/2685): [f68effe](https://github.com/jemalloc/jemalloc/commit/f68effe4ac0d1ee5cf26fc9c7fc50c88d16bf6ba), [e2c9f3a](https://github.com/jemalloc/jemalloc/commit/e2c9f3a9ce684090898b58a5fdb244cff48ef9bb)
- Enhanced the platform abstraction layer, added reentrant safe malloc_open and malloc_close helper functions and replaced system calls, and added a safe traceback unwinder based on frame pointers to support mixed compilation environments. (Architecture-related: platform compatibility)
  ↳ [#2706](https://github.com/jemalloc/jemalloc/pull/2706): [8c2e15d](https://github.com/jemalloc/jemalloc/commit/8c2e15d1a5749e50a1f61e216bb5fefc0d71d9b0) | [#2712](https://github.com/jemalloc/jemalloc/pull/2712): [edc1576](https://github.com/jemalloc/jemalloc/commit/edc1576f03d15a22b968828b68a074d9be6e5cc0)
- When C++ support is enabled, linking shared libraries uses g++ instead of gcc to fix linking errors on some systems. (Architecture-related: build requirements)
  ↳ [#2348](https://github.com/jemalloc/jemalloc/pull/2348): [4422f88](https://github.com/jemalloc/jemalloc/commit/4422f88d17404944a312825a1aec96cd9dc6c165)
- Added private library dependency declaration in pkg-config configuration file, and exposed jemalloc_prefix variable to support build configuration during static linking. (Architecture-related: pkg-config configuration)
  ↳ [#2525](https://github.com/jemalloc/jemalloc/pull/2525): [ed7e6fe](https://github.com/jemalloc/jemalloc/commit/ed7e6fe71a193ce24d1409d19d2c792f19af6a21) | [#2526](https://github.com/jemalloc/jemalloc/pull/2526): [ce8ce99](https://github.com/jemalloc/jemalloc/commit/ce8ce99a4a969e8dd8644d7382126fbb423d9859)
- Added --disable-user-config build option, allowing to disable reading configuration from /etc/malloc.conf or MALLOC_CONF during compilation. (Architecture-related: build and installation methods)
  ↳ [#2690](https://github.com/jemalloc/jemalloc/pull/2690): [c17bf8b](https://github.com/jemalloc/jemalloc/commit/c17bf8b368dd400614a42942c2c31a50bce5c680)
- Change the default page size to 64KiB on Aarch64 Linux, and display the page size setting in the configuration results. (Architecture-related: Platform compatibility)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [9442300](https://github.com/jemalloc/jemalloc/commit/9442300cc3adebdbf1d518dcba990a1c971e4f2e)
- On Android platform, detect page size through NDK header file to support 16KiB page size. (Architecture-related: platform compatibility)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [c51abba](https://github.com/jemalloc/jemalloc/commit/c51abba131e7665e05da0de60c66fb219976050d)
- Added --with-cxx-stdlib configuration option, allowing to explicitly specify the linked C++ standard library (libstdc++ or libcxx) to avoid incorrect linking of libstdc++ on the libc++ platform. (Architecture-related: build configuration)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [a10ef3e](https://github.com/jemalloc/jemalloc/commit/a10ef3e1f1c7593fb1cb211329e02c542af14694)
- The retain option is enabled by default on macOS. (Architecture-related: platform compatibility)
  ↳ [#2287](https://github.com/jemalloc/jemalloc/pull/2287): [b950934](https://github.com/jemalloc/jemalloc/commit/b950934916b2973fd4131ebfb684e53df305001a)
- Added special configuration handling for *-linux-musl* hosts. (Architecture-related: platform compatibility)
  ↳ [#2338](https://github.com/jemalloc/jemalloc/pull/2338): [aba1645](https://github.com/jemalloc/jemalloc/commit/aba1645f2d65a3b5c46958d7642b46ab3c142cf3)
- Added --disable-dss configuration option. (Architecture-related: build and installation methods)
  ↳ [#2476](https://github.com/jemalloc/jemalloc/pull/2476): [ea5b7be](https://github.com/jemalloc/jemalloc/commit/ea5b7bea3144cd26a63510016d778eab3ca58822)
- Adapt to the C23 standard, remove the custom unreachable() macro, and use the standard library definition instead. (Architecture-related: platform compatibility)
  ↳ [#2748](https://github.com/jemalloc/jemalloc/pull/2748): [d8486b2](https://github.com/jemalloc/jemalloc/commit/d8486b2653dc54f4d836e389960f627ab56cb8b4), [4b88bdd](https://github.com/jemalloc/jemalloc/commit/4b88bddbcac1f994034eb5d7485fd35663c3d325)

### Thread-Local Caching Layer
- Changed direct comparison of thread IDs to calling pthread_equal to improve portability and reliability. (Architecture-related: Platform compatibility)
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [5a634a8](https://github.com/jemalloc/jemalloc/commit/5a634a8d0a1d853fc9905bc7b8908895f147322a)
- Optimize thread-local storage access on Windows: use TlsGetValue2 API instead of TlsGetValue to avoid last error overhead, and use __declspec(thread) to implement TSD to improve performance. (Architecture-related: platform compatibility)
  ↳ [#2583](https://github.com/jemalloc/jemalloc/pull/2583): [9e123a8](https://github.com/jemalloc/jemalloc/commit/9e123a833cc6f56381c46a1656a323f893fa2528) | [#2702](https://github.com/jemalloc/jemalloc/pull/2702): [3a0d9cd](https://github.com/jemalloc/jemalloc/commit/3a0d9cdadb8a0dbfd180367459721d13eab0e116)

## Routine Changes

### New features
- Added handling of opt.cache_oblivious option in configuration parsing.
  ↳ [#2307](https://github.com/jemalloc/jemalloc/pull/2307): [a1c7d9c](https://github.com/jemalloc/jemalloc/commit/a1c7d9c046c2a90b978dc409d366b89303c96ab6)
- Disable triggering of decay during reentrancy, and added delay_trigger flag to ticker to skip decay on reentrancy.
  ↳ [#2409](https://github.com/jemalloc/jemalloc/pull/2409): [434a68e](https://github.com/jemalloc/jemalloc/commit/434a68e221f7dbb6f30bd13d318d0c22e1b47e78)
- Added filtering for internal functions such as je_malloc_default and do_rallocx in the jeprof tool to streamline performance analysis output.
  ↳ [#2452](https://github.com/jemalloc/jemalloc/pull/2452): [c1d3ad4](https://github.com/jemalloc/jemalloc/commit/c1d3ad46746da038cfc66ea5b545d195f511b0f4) | [#2692](https://github.com/jemalloc/jemalloc/pull/2692): [397827a](https://github.com/jemalloc/jemalloc/commit/397827a27d0e5092a15812eb421a2762c773920f)
- When metadata_thp is enabled, allocate the tcache bin stack from the base allocator, placing it on huge pages with other metadata, and supporting limited reuse of freed tcache stacks.
  ↳ [#2537](https://github.com/jemalloc/jemalloc/pull/2537): [72cfdce](https://github.com/jemalloc/jemalloc/commit/72cfdce71806443f4ccdbfe10aa5d50346a3d07e)
- Added separate statistics for edata and rtree memory allocation, and introduced the base_alloc_rtree function for rtree node allocation.
  ↳ [#2551](https://github.com/jemalloc/jemalloc/pull/2551): [36becb1](https://github.com/jemalloc/jemalloc/commit/36becb1302552c24b7bd59d8f00598e10a2411ea)
- Added the batcher module, which is used to cache simple operation commands in batches for subsequent use by other threads.
  ↳ [#2608](https://github.com/jemalloc/jemalloc/pull/2608): [70c94d7](https://github.com/jemalloc/jemalloc/commit/70c94d7474c3c4f4b61303f042727d2dab66ad07)
- Improved error message matching logic when opt.experimental_infallible_new fails, only matching message prefixes.
  ↳ [#2278](https://github.com/jemalloc/jemalloc/pull/2278): [cd5aaf3](https://github.com/jemalloc/jemalloc/commit/cd5aaf308a46ce8ad0232ee9efb697b4ed33a7e4)
- Improved the statistical output of HPA, added a header row for non-full slabs, and added a dirty page range counting function.
  ↳ [#2383](https://github.com/jemalloc/jemalloc/pull/2383): [c7805f1](https://github.com/jemalloc/jemalloc/commit/c7805f1eb5b9eadccb9711044e141ff741c09d4c) | [#2827](https://github.com/jemalloc/jemalloc/pull/2827): [0dfb4a5](https://github.com/jemalloc/jemalloc/commit/0dfb4a5a1a83f0968f8499c101dc98586a582546)
- Renamed internal static function fallback_impl to fallbackNewImpl to improve code clarity.
  ↳ [#2452](https://github.com/jemalloc/jemalloc/pull/2452): [d59e30c](https://github.com/jemalloc/jemalloc/commit/d59e30cbc9fa47425a4ba907ab8f8b580e26f37e)
- Added logs at the entry and exit of free and sdallocx related functions to improve debugging experience.
  ↳ [#2578](https://github.com/jemalloc/jemalloc/pull/2578): [b1792c8](https://github.com/jemalloc/jemalloc/commit/b1792c80d2870c87af79d64bcca844d19345412d)

### bug fixes
- Fixed an error when compiling edata.h in MSVC 2019. Change the initialization of composite literals in the edata_cmp_summary_get function to declare the variable first and then assign the value.
  ↳ [#2275](https://github.com/jemalloc/jemalloc/pull/2275): [70d4102](https://github.com/jemalloc/jemalloc/commit/70d4102f48dce2d5755e9139a15eeec606f97bff)
- Fixed the assertion failure problem in arena_stats_merge() caused by improper reading order of nmalloc and ndalloc, and avoid race conditions by exchanging the reading order.
  ↳ [#2304](https://github.com/jemalloc/jemalloc/pull/2304): [cb578bb](https://github.com/jemalloc/jemalloc/commit/cb578bbe01326bfc4a7b676f6921189d84518f03)
- Added slab bitmap based double free detection for arena in debug builds and added sanity check after tcache flush.
  ↳ [#2315](https://github.com/jemalloc/jemalloc/pull/2315): [42daa1a](https://github.com/jemalloc/jemalloc/commit/42daa1ac4405a06ed79f68dc2c0ca8c5ad477ecd)
- Fix safety_check segfault in double free test, correct pointer argument passed in safety_check_fail call, and adjust arena_salloc function to correctly return allocation size.
  ↳ No PR: [1897f18](https://github.com/jemalloc/jemalloc/commit/1897f185d2c06307fefc4d8f4512eeb13c474999)
- Fixed a race condition problem when updating thread names in heap analysis to avoid temporary emptying, causing the analysis read path to obtain null values.
  ↳ [#2380](https://github.com/jemalloc/jemalloc/pull/2380): [5fd5583](https://github.com/jemalloc/jemalloc/commit/5fd55837bbc400d8cc15152ac2b80b64baa9b68c)
- Simplify the logic of the ph_insert function, and fix a potential off-by-one bug in lazy auxiliary list merging where the last node of the auxiliary list has never been touched before.
  ↳ [#2389](https://github.com/jemalloc/jemalloc/pull/2389): [543e2d6](https://github.com/jemalloc/jemalloc/commit/543e2d61e6047208d647cf3fd3499bead3bcc23e)
- Fix the assignment error in the assertion statement in hpa_from_pai, change the assignment operator to the equality operator, and ensure that the assertion correctly checks pointer equality.
  ↳ [#2415](https://github.com/jemalloc/jemalloc/pull/2415): [521970f](https://github.com/jemalloc/jemalloc/commit/521970fb2e5278b7b92061933cbacdbb9478998a)
- Removed a wrong assertion in arena_extent_alloc_large that could trigger falsely due to delayed work when HPA was enabled.
  ↳ [#2418](https://github.com/jemalloc/jemalloc/pull/2418): [fc68012](https://github.com/jemalloc/jemalloc/commit/fc680128e0aed18d878bdc71c1ceb53e79da3de7)
- Fix the possible null pointer dereference problem in the VERIFY_READ macro, and add a non-null check for oldlenp before dereferencing.
  ↳ [#2431](https://github.com/jemalloc/jemalloc/pull/2431): [dc0a184](https://github.com/jemalloc/jemalloc/commit/dc0a184f8d349546af6a051eb87be47715eacff3)
- Fixed the segmentation fault caused by passing in a null pointer in extent_try_coalesce_impl, added a null pointer assertion and corrected passing a valid pointer at the call site.
  ↳ [#2432](https://github.com/jemalloc/jemalloc/pull/2432): [12311fe](https://github.com/jemalloc/jemalloc/commit/12311fe6c37720225a3e8b5798e7051d153d29c1)
- Fix the thread name reference in prof_recent dump to ensure that the thread name pointer is passed correctly; and add the prof_sys_thread_name feature in the prof_recent unit test to fix testing problems in environments without a default thread name.
  ↳ [#2435](https://github.com/jemalloc/jemalloc/pull/2435): [94ace05](https://github.com/jemalloc/jemalloc/commit/94ace05832209543bde81d0a5f0e2a9660243abd), [d4a2b8b](https://github.com/jemalloc/jemalloc/commit/d4a2b8bab10980d4677d43560f27ac9ef66cde45)
- Fixed the bug that hpa_shard was not destroyed correctly, replaced the incorrectly called hpa_shard_disable with hpa_shard_destroy.
  ↳ [#2448](https://github.com/jemalloc/jemalloc/pull/2448): [9c32689](https://github.com/jemalloc/jemalloc/commit/9c32689e576906332d2ceaabafc2a927d152beba)
- Fixed the uninitialized data reading problem in prof_free caused by the security check path of arena_prof_info_get not initializing prof_info->alloc_tctx.
  ↳ [#2464](https://github.com/jemalloc/jemalloc/pull/2464): [210f0d0](https://github.com/jemalloc/jemalloc/commit/210f0d0b2bb3ed51a83a675c34f09fc36ac686e1)
- Fixed memory usage statistics for sampled small allocations, now correctly counting allocations for their effective bin size instead of incorrectly attributed to large object classes; and added test cases to verify that sampled small memory allocations maintain expected page alignment and metadata invariants.
  ↳ [#2486](https://github.com/jemalloc/jemalloc/pull/2486): [07a2eab](https://github.com/jemalloc/jemalloc/commit/07a2eab3ed5dd76657ee689326acd9ecaf1e2830) | [#2459](https://github.com/jemalloc/jemalloc/pull/2459): [ebd7e99](https://github.com/jemalloc/jemalloc/commit/ebd7e99f5c1bd486d9eee5f10a48a92585efc1e3)
- In arena_reset operations, ensure sample allocations are demoted before being freed to maintain consistent profiling counts.
  ↳ [#2496](https://github.com/jemalloc/jemalloc/pull/2496): [62648c8](https://github.com/jemalloc/jemalloc/commit/62648c88e5e50b8ed11181a8c42dbc1134d6d854)
- When there is a configuration parsing error, the error message will now include the configuration string fragment that caused the problem.
  ↳ [#2503](https://github.com/jemalloc/jemalloc/pull/2503): [6816b23](https://github.com/jemalloc/jemalloc/commit/6816b238625d67e0bf3b6768f00709051b23f2a6)
- Fixed an error in the register used when reading the CPU ID via the rdtscp instruction, correcting the register from edx to ecx.
  ↳ [#2529](https://github.com/jemalloc/jemalloc/pull/2529): [b71da25](https://github.com/jemalloc/jemalloc/commit/b71da25b8a12c2c3f0c10b0811d15a61980186e8)
- Fixed the bug that promoted allocation may not be correctly recognized as promoted when released, and adjusted the conditional judgment logic in arena_dalloc_large.
  ↳ [#2530](https://github.com/jemalloc/jemalloc/pull/2530): [867eedf](https://github.com/jemalloc/jemalloc/commit/867eedfc589039257deafe7492afa7aa9ab6169f)
- Fix the bug that nfill may be 0 when ncached_max is 1, make sure it is set to 1 when nfill is 0, and add corresponding assertions.
  ↳ [#2555](https://github.com/jemalloc/jemalloc/pull/2555): [d88fa71](https://github.com/jemalloc/jemalloc/commit/d88fa71bbd8f22814ead264eff07ba70f05f3291)
- Fix the boundary case where the root node may not be the best element in the heap deletion operation, ensuring that the root node is always the best element in the heap after deletion.
  ↳ [#2565](https://github.com/jemalloc/jemalloc/pull/2565): [10d7131](https://github.com/jemalloc/jemalloc/commit/10d713151d7245ae89657a7002a5988522b7bd7a)
- Fixed an issue where allocation statistics were printed incorrectly due to type errors on 32-bit systems.
  ↳ [#2600](https://github.com/jemalloc/jemalloc/pull/2600): [630434b](https://github.com/jemalloc/jemalloc/commit/630434bb0ac619f7beec927569782d924c459385)
- Fixed the infinite cleanup loop in HPA caused by hpa_hugify_blocked_by_ndirty still returning true when there is no dirty memory, and added regression testing; while simplifying the delayed work processing logic.
  ↳ [#2632](https://github.com/jemalloc/jemalloc/pull/2632): [47d69b4](https://github.com/jemalloc/jemalloc/commit/47d69b4eabae199fa8b5d948f0043effccfbc31e) | [#2686](https://github.com/jemalloc/jemalloc/pull/2686): [0a9f51d](https://github.com/jemalloc/jemalloc/commit/0a9f51d0d8d2a8135cc853be7ed771230854ede6)
- Fixed the sanity check of ncached and nstashed during tcache flush. When there are many stash items, ncached may be lower than the remaining value after flush stashed. In this case, flush can return directly.
  ↳ [#2637](https://github.com/jemalloc/jemalloc/pull/2637): [fa451de](https://github.com/jemalloc/jemalloc/commit/fa451de17fff73cc03c31ec8cd817d62927d1ff9)
- Fixed the problem that the locked flag in malloc_mutex_trylock was not set correctly, and added the lock status check function malloc_mutex_is_locked() and assertion verification.
  ↳ [#2718](https://github.com/jemalloc/jemalloc/pull/2718): [1960536](https://github.com/jemalloc/jemalloc/commit/1960536b61ba2c1d287cf7866fae02aea3f4e3b0), [661fb1e](https://github.com/jemalloc/jemalloc/commit/661fb1e6722e9b29e76520182086edcb835077e3)
- Fixed the problem that the locked status was not updated correctly when pthread_cond_wait internally released and reacquired the mutex lock, and added the background_thread_cond_wait function to explicitly maintain this status.
  ↳ [#2718](https://github.com/jemalloc/jemalloc/pull/2718): [3eb7a4b](https://github.com/jemalloc/jemalloc/commit/3eb7a4b53dfeae537fd78cece51342a1f12d86dc)
- Skip the mutex owner check during background thread startup because some mutexes have not yet been initialized and the global initialization lock has overridden all locking operations.
  ↳ [#2719](https://github.com/jemalloc/jemalloc/pull/2719): [44db479](https://github.com/jemalloc/jemalloc/commit/44db479fad82751a3c6a3157e59b9d295f9ec90f)
- Fixed size calculation issue with error message in sized-dealloc safety check.
  ↳ [#2738](https://github.com/jemalloc/jemalloc/pull/2738): [2a693b8](https://github.com/jemalloc/jemalloc/commit/2a693b83d2d1631b6a856d178125e1c47c12add9)
- Removed configuration validation for the HPA ratio (sum of hpa_dirty_mult and hpa_hugification_threshold), and removed related misconfiguration flagging logic.
  ↳ [#2762](https://github.com/jemalloc/jemalloc/pull/2762): [3820e38](https://github.com/jemalloc/jemalloc/commit/3820e38dc1021cebba4628e277cde060e840aaef)
- Fixed the out-of-bounds read problem in the bitmap_ffu function caused by not checking the array boundary, and adjusted the loop logic to avoid loading data at invalid indexes.
  ↳ [#2789](https://github.com/jemalloc/jemalloc/pull/2789): [ef8e512](https://github.com/jemalloc/jemalloc/commit/ef8e512e2916a7c2dfca289e9113324b87324723)
- Fixed the issue where the deferred_allowed flag was not set correctly when arena 0 was initialized, and added a test case to verify the fix.
  ↳ [#2795](https://github.com/jemalloc/jemalloc/pull/2795): [499f306](https://github.com/jemalloc/jemalloc/commit/499f3068593ec61dae961e2c8ea3e0cf1482d616)
- Fixed an issue with profiling sample metadata lookup in xallocx, and added coverage of sdallocx paths in tests.
  ↳ [#2806](https://github.com/jemalloc/jemalloc/pull/2806): [ac279d7](https://github.com/jemalloc/jemalloc/commit/ac279d7e717e6b5f836657fbc525d0975f80a7d0)
- Fixed the frame pointer-based backtrace to handle stack range changes and fallback to the Linux backtrace function when a change is detected.
  ↳ [#2811](https://github.com/jemalloc/jemalloc/pull/2811): [773b580](https://github.com/jemalloc/jemalloc/commit/773b5809f9ab3f7c525badbe7587f8ab8ee20d41)
- Fixed the assertion error caused by repeated calls of huge_arena_auto_thp_switch when deleting and rebuilding b0 in the unit test, and ensured that automatic switching can take effect correctly after turning on huge arena before initialization.
  ↳ [#2818](https://github.com/jemalloc/jemalloc/pull/2818): [3688dfb](https://github.com/jemalloc/jemalloc/commit/3688dfb5c3b7d94a12e18b753c0fc9c405b77b1f)
- Added check for input size exceeding maximum class size in double-release validation.
  ↳ [#2854](https://github.com/jemalloc/jemalloc/pull/2854): [fd60645](https://github.com/jemalloc/jemalloc/commit/fd60645260b74645cd606bb6a48464890ab39dee)
- Adjusted the size of the CACHE_BIN_NFLUSH_BATCH_MAX macro to prevent assertion failures caused by the array size exceeding the allowed maximum.
  ↳ [#2846](https://github.com/jemalloc/jemalloc/pull/2846): [9169e92](https://github.com/jemalloc/jemalloc/commit/9169e9272a9fb123702e04c77ff5326f29818f70)
- Fixed the problem of incorrectly executing dehugify when purging, and added and updated related test cases.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [a156e99](https://github.com/jemalloc/jemalloc/commit/a156e997d7037aba2b2dc09993a62798966c991e)
- Save and restore errno when calling process_madvise to avoid accidentally modifying the errno value due to system call failure.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [5e98585](https://github.com/jemalloc/jemalloc/commit/5e98585b37556cdb762e36f02b657742b8c47fe3)
- Rolled back the "do not cancel huge pages when clearing" changes, restored the dehugify function and its calls, and added related tests and USDT tracking.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [2688047](https://github.com/jemalloc/jemalloc/commit/2688047b56e6ef21d960e40281cb13774c8c17ab)
- Fixed an issue where locks were released prematurely before allocation after inserting a new page from central, ensuring mutex locks are maintained during allocation.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [87555df](https://github.com/jemalloc/jemalloc/commit/87555dfbb22efb0c4bcfc59be0b7ccad19725edf)
- Fixed the page initialization parameters when extracting from central, changed hugify_eager to start_as_huge, and added related test cases.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [3678a57](https://github.com/jemalloc/jemalloc/commit/3678a57c101b84400d6db85c96ad8ce18d5fcdf9)
- Fixed an issue where the derivation counter was not skipped correctly when outputting mutex lock statistics in malloc statistics in JSON format, resulting in an incorrect array index.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [12b33ed](https://github.com/jemalloc/jemalloc/commit/12b33ed8f1a776ea36a5bafa14c65461b9efa64d)
- Fixed an issue where the os_page_id call caused assertion failure when mmap failed and returned a NULL address, which was avoided by adding a non-null address check.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [79cc7dc](https://github.com/jemalloc/jemalloc/commit/79cc7dcc827bb506f5be0345df2a7ce356b84165)
- Fixed an index underflow and assertion failure issue that could result from psset_pick_purge when rejecting candidate entries with unqualified times, and added corresponding unit tests.
  ↳ [#2871](https://github.com/jemalloc/jemalloc/pull/2871): [d758349](https://github.com/jemalloc/jemalloc/commit/d758349ca438ee35769409b06c642ca2d8e408ac)
- Fixed the out-of-bounds check error in arenas_bin_i_index and arenas_extent_i_index, changing the greater-than sign to the greater-than-equal sign to prevent out-of-bounds reads from accessing indexes beyond the valid range; and added a unit test for boundary index returns ENOENT.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [513778b](https://github.com/jemalloc/jemalloc/commit/513778bcb18f7e98073775d2b358674b14f7433f)
- Fixed the problem of repeated nactive_huge key and missing ndirty_huge key in full_slabs and empty_slabs JSON segments in HPA shard statistics output, and added unit test to verify that both segments contain ndirty_huge.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [87f9938](https://github.com/jemalloc/jemalloc/commit/87f9938de51be77946b02f0ed54cbd32a5ff055b)
- Fixed off-by-one bug in stats_arenas_i_bins_j and stats_arenas_i_extents_j bounds checks to prevent array out-of-bounds access, and added unit test validating bounds index returns ENOENT.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [eab2b29](https://github.com/jemalloc/jemalloc/commit/eab2b29736a3f499f7be1236950ed9aab57c4267)
- Fixed the fallback value error when sysconf fails in the os_page_detect function, and changes the wrong LG_PAGE to the correct PAGE to avoid the page size being set to a very small value.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [dd30c91](https://github.com/jemalloc/jemalloc/commit/dd30c91eaaf02e5f347e37a49f99eae670b94c88)
- Fixed the problem in prof_stack_range that the error check failed due to the wrong return value type of malloc_read_fd (using size_t instead of ssize_t), and adjusted the error handling logic to correctly distinguish between read failure and read end.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [3f6e63e](https://github.com/jemalloc/jemalloc/commit/3f6e63e86a193e8a4d685480165812cac6d2350f)
- Fixed the problem of adjacent edata obtained in extent_try_coalesce_impl not being released after size check failure, and added corresponding unit tests.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [675ab07](https://github.com/jemalloc/jemalloc/commit/675ab079e7e6f08a74727ec53569ec2db578d515)
- Fixed an issue where using the wrong variable in an array index loop resulted in array entries not being initialized correctly.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [234404d](https://github.com/jemalloc/jemalloc/commit/234404d324458d4404ef382742741cb4ffbcf921)
- Fixed the wrong order of parameters in the edata_init call in the extent_alloc_dss function, replacing the redundant size parameter with the correct slab parameter.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [2fceece](https://github.com/jemalloc/jemalloc/commit/2fceece256c0a01a28743652ce3e5cc67723e453)
- Fixed a memory leak caused by not restoring old curr_reg when san_bump_grow_locked failed.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [5904a42](https://github.com/jemalloc/jemalloc/commit/5904a421878b31d6a5ec674027b35db63e64537d)
- Fixed the issue of missing cleanup messages when collecting a single profile.
  ↳ [#2579](https://github.com/jemalloc/jemalloc/pull/2579): [dfb3260](https://github.com/jemalloc/jemalloc/commit/dfb3260b97a13a90487ec74e495ca4fc684f6a44)
- Fixed static analysis warnings, added missing enum branches and adjusted type conversions.
  ↳ [#2581](https://github.com/jemalloc/jemalloc/pull/2581): [eda05b3](https://github.com/jemalloc/jemalloc/commit/eda05b39941c0ff6d5236c845e6bca70324c9a32)
- Embed prompt information into the abort function name when the security check fails, and optimize the error prompt for size mismatch.
  ↳ [#2587](https://github.com/jemalloc/jemalloc/pull/2587): [0516025](https://github.com/jemalloc/jemalloc/commit/05160258df8a4e34f323b2c6eb1f2c0f59591d05)
- Fixed the assertion condition when arena is created in ehooks to avoid false triggering when the hugepage size is not 2M.
  ↳ [#2769](https://github.com/jemalloc/jemalloc/pull/2769): [6786934](https://github.com/jemalloc/jemalloc/commit/6786934280392e71a1e14d48b331d4eca58550a7)
- Fixed the problem of missing RDTSCP macro definition and added JEMALLOC_ prefix to the macro.
  ↳ [#2368](https://github.com/jemalloc/jemalloc/pull/2368): [31e01a9](https://github.com/jemalloc/jemalloc/commit/31e01a98f159926493158cde6453cde55f21c42b)
- Fixed or suppressed static analysis warnings.
  ↳ [#2446](https://github.com/jemalloc/jemalloc/pull/2446): [bb0333e](https://github.com/jemalloc/jemalloc/commit/bb0333e745a71aea0230a09be49a752115d45bb7)
- Make internal header files self-contained and explicitly add dependent include directives.
  ↳ [#2463](https://github.com/jemalloc/jemalloc/pull/2463): [41e0b85](https://github.com/jemalloc/jemalloc/commit/41e0b857bef0b787a581c7a8334b46981d5e06ed)
- Enabled more compilation warnings for CI and fixed exposed issues.
  ↳ [#2517](https://github.com/jemalloc/jemalloc/pull/2517): [da66aa3](https://github.com/jemalloc/jemalloc/commit/da66aa391f853ccf2300845b3873cc8f1cf48f2d)

### Refactoring optimization
- Reduce the frequency of garbage collection, require a certain time interval between two GCs, and adjust the filling counting logic of small bins accordingly.
  ↳ [#2685](https://github.com/jemalloc/jemalloc/pull/2685): [0c88be9](https://github.com/jemalloc/jemalloc/commit/0c88be9e0a09fc868ac05ace96466bdc6f502ab8)
- During thread and arena migration, old arena is no longer forced to be cleaned up when background threads are enabled.
  ↳ [#2840](https://github.com/jemalloc/jemalloc/pull/2840): [a3910b9](https://github.com/jemalloc/jemalloc/commit/a3910b9802d066a72707d9d77bc981d05b74d761)
- Roll back the peak demand tracking function and remove related initialization code and functions.
  ↳ No PR: [27d7960](https://github.com/jemalloc/jemalloc/commit/27d7960cf9b48a9a9395661f212d05a471dceed4)
- Roll back a PR and restore the jemalloc changes of the Meta branch, including adjustments to arena initialization, bin information configuration and tcache default settings.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [2114349](https://github.com/jemalloc/jemalloc/commit/2114349a4e9933ebff87df01572a94a12eca5d86)
- Move pages_postfork_child function definition inside pages_purge_process_madvise_impl to support lazy initialization and reset pidfd on fork.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [4246475](https://github.com/jemalloc/jemalloc/commit/4246475b44e660010256206857d941e6f45ca113)
- Changed malloc_write_fd and malloc_read_fd from static inline functions to non-inline global functions, and added a retry loop to handle partial writes and reads.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [38b1242](https://github.com/jemalloc/jemalloc/commit/38b12427b7a832fd97739d7cfcca4081a964df2e)
- Clean up undefined root->prev pointer maintenance in ph_remove.
  ↳ [#2391](https://github.com/jemalloc/jemalloc/pull/2391): [be6da4f](https://github.com/jemalloc/jemalloc/commit/be6da4f663a062353dd9a25baaae0ebcd68b7477)
- Remove unused mutex locks and related initialization code in hpa_central.
  ↳ [#2397](https://github.com/jemalloc/jemalloc/pull/2397): [f743690](https://github.com/jemalloc/jemalloc/commit/f743690739299cb1e72852744bdd79443b264be0)
- Change missing functions in the code base that can be declared static to static link attributes.
  ↳ [#2427](https://github.com/jemalloc/jemalloc/pull/2427): [70344a2](https://github.com/jemalloc/jemalloc/commit/70344a2d38eb71a162ea19d1a4fee8f0d168588b)
- Mark qualified global variables and function parameters as static or const.
  ↳ [#2475](https://github.com/jemalloc/jemalloc/pull/2475): [589c63b](https://github.com/jemalloc/jemalloc/commit/589c63b4244e60dcfe74861a2b110b545182216f)
- Remove unreachable return statements in ffs_u32 and fls_u32 functions.
  ↳ [#2474](https://github.com/jemalloc/jemalloc/pull/2474): [e249d1a](https://github.com/jemalloc/jemalloc/commit/e249d1a2a1eef5bd0b329f0575f9d952a5e73522)
- Define the PROF_TCTX_SENTINEL macro and prof_tctx_is_valid inline function to replace the magic number.
  ↳ [#2485](https://github.com/jemalloc/jemalloc/pull/2485): [7e54dd1](https://github.com/jemalloc/jemalloc/commit/7e54dd1ddb0953093fc640cca9a45897b33cf84d)
- Define SBRK_INVALID macro to replace magic numbers.
  ↳ [#2485](https://github.com/jemalloc/jemalloc/pull/2485): [1431153](https://github.com/jemalloc/jemalloc/commit/14311536959457d10e9307a580afeb0af1a8838b)
- Improved IO tool functions to ensure complete processing of short writes and interrupt signals, and added lseek package.
  ↳ [#2516](https://github.com/jemalloc/jemalloc/pull/2516): [d2c9ed3](https://github.com/jemalloc/jemalloc/commit/d2c9ed3d1e7c1a318e6fd018eb0e0f3ba5ee3365)
- Simplify the conditional judgment logic when incrementing lg_fill_div.
  ↳ [#2678](https://github.com/jemalloc/jemalloc/pull/2678): [a25b9b8](https://github.com/jemalloc/jemalloc/commit/a25b9b8ba91881964be3083db349991bbbbf1661)
- Simplify the internal logic of the ph_remove function, remove redundant variables and repeated conditional branches.
  ↳ [#2393](https://github.com/jemalloc/jemalloc/pull/2393): [5266152](https://github.com/jemalloc/jemalloc/commit/5266152d7922fc76fdaaa39ded9381a4fa7b4b9d)
- Change the arenas_lookup_ctl function to a retryable lookup method and add a null pointer check.
  ↳ [#2424](https://github.com/jemalloc/jemalloc/pull/2424): [019cccc](https://github.com/jemalloc/jemalloc/commit/019cccc293f96c9f7886373d816aab061f65f7de)
- Add check that alloc_ctx.edata is NULL in arenas_lookup_ctl.
  ↳ [#2424](https://github.com/jemalloc/jemalloc/pull/2424): [5bac384](https://github.com/jemalloc/jemalloc/commit/5bac384970a8224daee0b07475950a5291fc37d3)
- Extract the psset heap allocation calculation logic of hpdata into a public function.
  ↳ [#2455](https://github.com/jemalloc/jemalloc/pull/2455): [6d4aa33](https://github.com/jemalloc/jemalloc/commit/6d4aa33753d1d6fa60925b40e0fd40f1e6a42ef4)
- Clean up cache_bin related function interfaces and remove redundant cache_bin_info_t* parameters.
  ↳ [#2562](https://github.com/jemalloc/jemalloc/pull/2562): [e4817c8](https://github.com/jemalloc/jemalloc/commit/e4817c8d89a2a413e835c4adeab5c5c4412f9235)
- Introduce early returns in phn_merge_siblings to reduce nesting, and optimize ph_merge_aux calls.
  ↳ [#2563](https://github.com/jemalloc/jemalloc/pull/2563): [92aa52c](https://github.com/jemalloc/jemalloc/commit/92aa52c0625d35ca1c30e7fc913d7c92c9518f9e)
- Split the processing logic of small objects and large objects in tcache, and add the tcache_try_gc_bin function.
  ↳ [#2608](https://github.com/jemalloc/jemalloc/pull/2608): [6e56848](https://github.com/jemalloc/jemalloc/commit/6e568488500b12441094e084f89b1a1da784f39b)
- Incorporate the HPA's dirty page count into the page allocator's dirty page count.
  ↳ [#2622](https://github.com/jemalloc/jemalloc/pull/2622): [268e8ee](https://github.com/jemalloc/jemalloc/commit/268e8ee880bcb67163eda4c4f43c06697b28a436)
- Simplify the tcache_gc_small function logic and remove unnecessary else branches.
  ↳ [#2643](https://github.com/jemalloc/jemalloc/pull/2643): [5afff2e](https://github.com/jemalloc/jemalloc/commit/5afff2e44e8d31ef1e9eb01d6b1327fe111835ed)
- Set dependency flags that do not involve ownership in all rtree read operations to false.
  ↳ [#2664](https://github.com/jemalloc/jemalloc/pull/2664): [8477ec9](https://github.com/jemalloc/jemalloc/commit/8477ec9562632b0808874416cb2d11ad6fbf99ea)
- Extract the output logic of long string values into independent functions to avoid truncation of statistical values.
  ↳ [#2676](https://github.com/jemalloc/jemalloc/pull/2676): [b66f689](https://github.com/jemalloc/jemalloc/commit/b66f689764e05084f5b995bf2f8d277b70e084fd)
- Split the stats_arena_hpa_shard_print function into multiple sub-functions to improve code readability and maintainability.
  ↳ [#2747](https://github.com/jemalloc/jemalloc/pull/2747): [b82333f](https://github.com/jemalloc/jemalloc/commit/b82333fdec6e5833f88780fcf1fc50b799268e1b)
- Added sz_s2u_compute_using_delta function, used to calculate usize based on delta method.
  ↳ [#2646](https://github.com/jemalloc/jemalloc/pull/2646): [6035d4a](https://github.com/jemalloc/jemalloc/commit/6035d4a8d369d158ca299c10773e05796e1d18ad)
- Change the global age counter in HPA central to use the local age counter of HPA shard.
  ↳ [#2796](https://github.com/jemalloc/jemalloc/pull/2796): [421b17a](https://github.com/jemalloc/jemalloc/commit/421b17a622a5037b82aa658dc0cc8264ddd6e711)
- Added void parameters to parameterless function declarations, and changed several internal functions to static to limit scope.
  ↳ [#2835](https://github.com/jemalloc/jemalloc/pull/2835): [37bf846](https://github.com/jemalloc/jemalloc/commit/37bf846cc38345947ff644bf47d7d51126353c09)
- Encapsulate HPA sharding-independent batch processing operations into hpa_utils, and no longer pass hpa_shard parameters directly.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [3557742](https://github.com/jemalloc/jemalloc/commit/355774270dc41a66e38565b4c5573fd53a8c090f)
- Move the flush pointer array operation out of tcache.c, and add related auxiliary functions and statistics reset logic.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [6d46111](https://github.com/jemalloc/jemalloc/commit/6d4611197e62285ae69fd0237e6b3a29494213c0)
- Migrate bin inline functions from arena_inlines_b.h to the newly created bin_inlines.h, and update related calls.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [0ac9380](https://github.com/jemalloc/jemalloc/commit/0ac9380cf1b2fe1b255a96c5d57d6eab33a78330)
- Removed dead code without callers: extent_commit_wrapper, large_salloc and tcache_gc_dalloc related event waiting functions.
  ↳ [#2877](https://github.com/jemalloc/jemalloc/pull/2877): [19bbefe](https://github.com/jemalloc/jemalloc/commit/19bbefe136cf8684e126cdb80f7ef2aba88e55dc)

### Test related
- Fixed bracket position error in string comparison logic in C++ integration tests.
  ↳ [#2325](https://github.com/jemalloc/jemalloc/pull/2325): [c9ac1f4](https://github.com/jemalloc/jemalloc/commit/c9ac1f4701d621c3f39b94970fa96ce23897a295)
- Enable the -fno-builtin option in test compilation to prevent the compiler from optimizing out unused malloc calls.
  ↳ [#2340](https://github.com/jemalloc/jemalloc/pull/2340): [3de0c24](https://github.com/jemalloc/jemalloc/commit/3de0c24859f4413bf03448249078169bb50bda0f)
- Added a micro-benchmark test for operator delete, and modified bench.h to support C++.
  ↳ [#2332](https://github.com/jemalloc/jemalloc/pull/2332): [06374d2](https://github.com/jemalloc/jemalloc/commit/06374d2a6ad525be86e4381b4bb5010fedff3268)
- Explicitly display ratios as time consumption ratios in benchmarks and adjust output format.
  ↳ [#2332](https://github.com/jemalloc/jemalloc/pull/2332): [14ad820](https://github.com/jemalloc/jemalloc/commit/14ad8205bf0e23cdc1698f65c4d307753726a6a3)
- Fix divide-by-zero error caused by compiler optimization in stress/cpp/microbench.
  ↳ [#2359](https://github.com/jemalloc/jemalloc/pull/2359): [a74acb5](https://github.com/jemalloc/jemalloc/commit/a74acb57e87e2c3ad4386f757f4d792d9aa6e19a)
- Introduce no_opt_ptr helper function in benchmark tests to prevent pointers from being optimized away.
  ↳ [#2364](https://github.com/jemalloc/jemalloc/pull/2364): [09e4b38](https://github.com/jemalloc/jemalloc/commit/09e4b38fb1f9a9b505e35ac13b8f99282990bc2c)
- Reduce the maximum number of arenas and background threads in the test to avoid exhaustion of 32-bit system resources.
  ↳ [#2379](https://github.com/jemalloc/jemalloc/pull/2379): [97b313c](https://github.com/jemalloc/jemalloc/commit/97b313c7d480bc087b0c805b4bb42b71dd9c9e93)
- Skip assumptions about arena ID in tests when percpu_arena is enabled.
  ↳ [#2398](https://github.com/jemalloc/jemalloc/pull/2398): [71bc1a3](https://github.com/jemalloc/jemalloc/commit/71bc1a3d91ae7e513488401627eca2a31e9f6e60)
- Explicitly specify arena allocation in the test to avoid changes in the associated arena when percpu arena is enabled.
  ↳ [#2400](https://github.com/jemalloc/jemalloc/pull/2400): [8e7353a](https://github.com/jemalloc/jemalloc/commit/8e7353a19b5fd9dd1041307b884bc969065b63af)
- Explicitly allocate arena in the test case to avoid arena changes when percpu arena is enabled.
  ↳ [#2400](https://github.com/jemalloc/jemalloc/pull/2400): [8b64be3](https://github.com/jemalloc/jemalloc/commit/8b64be34414e92fcbcdbaf5b81db6d26289667b5)
- When stderr is a terminal and colors are supported, test error messages are displayed in red to enhance readability.
  ↳ [#2479](https://github.com/jemalloc/jemalloc/pull/2479): [65d3b59](https://github.com/jemalloc/jemalloc/commit/65d3b5989b0afa44f0703bc1ca81f2ba74ed90a5)
- Fix compiler warnings in unit tests, including initializing structure fields and removing unused variables.
  ↳ [#2469](https://github.com/jemalloc/jemalloc/pull/2469): [e133870](https://github.com/jemalloc/jemalloc/commit/e1338703efb77f7d276ee65121fa63bb66ede239)
- When the test fails, print the colored assertion information before terminating, so as to locate the problem faster.
  ↳ [#2480](https://github.com/jemalloc/jemalloc/pull/2480): [314c073](https://github.com/jemalloc/jemalloc/commit/314c073a38adfbfc97ed2913e287e8e642fc46ca)
- When a test fails, a colored highlight prompt is output in the terminal, making it easy to quickly locate failed test cases from a large amount of output.
  ↳ [#2509](https://github.com/jemalloc/jemalloc/pull/2509): [254c484](https://github.com/jemalloc/jemalloc/commit/254c4847e8ac263d24720aa93c2c7d410f55a239)
- Fixed the false positive of out-of-bounds array subscript in GCC 12.3.0, and introduced temporary variables to avoid repeated function calls.
  ↳ [#2524](https://github.com/jemalloc/jemalloc/pull/2524): [7d9ecea](https://github.com/jemalloc/jemalloc/commit/7d9eceaf3858515cd8774c3fad8e90fe53454e3c)
- Modify test code to verify respect for hpa_min_purge_interval_ms option.
  ↳ [#2658](https://github.com/jemalloc/jemalloc/pull/2658): [91a6d23](https://github.com/jemalloc/jemalloc/commit/91a6d230dba40ef2ef6e381b4c4fab5f5b0f6111)
- Increase the tcache_ncached_max configuration value to 1024 in the fill_flush test case to avoid stack overflow.
  ↳ [#2677](https://github.com/jemalloc/jemalloc/pull/2677): [8fefabd](https://github.com/jemalloc/jemalloc/commit/8fefabd3a49d1f090fe677722f1e2a66f162237a)
- Fixed the nstime_update_mock function in the arena_decay unit test to avoid incorrect time coverage in monotonic time mode.
  ↳ [#2685](https://github.com/jemalloc/jemalloc/pull/2685): [baa5a90](https://github.com/jemalloc/jemalloc/commit/baa5a90cc6f77e86c2aa58257f3d6c67a1b863dc)
- Fixed the problem of test_retained unit test causing assertion failure due to too many threads on multi-CPU machines, and limited the upper limit of the number of threads to 16.
  ↳ [#2767](https://github.com/jemalloc/jemalloc/pull/2767): [46690c9](https://github.com/jemalloc/jemalloc/commit/46690c9ec036cede074476caa05ecd6fe954bd23)
- Fix undefined behavior of left shift overflow caused by uint8_t integer promotion in test/unit/hash.c.
  ↳ [#2781](https://github.com/jemalloc/jemalloc/pull/2781): [52fa957](https://github.com/jemalloc/jemalloc/commit/52fa9577ba8fa94f41c8c92f845a74c3fb04db80)
- Fix prof_threshold test to skip test when configuration statistics is not enabled.
  ↳ [#2792](https://github.com/jemalloc/jemalloc/pull/2792): [1abeae9](https://github.com/jemalloc/jemalloc/commit/1abeae9ebd7b3c9f3ebb5e49db393149c37f18f9)
- Fixed implicit type conversion issue in prof_threshold test.
  ↳ [#2793](https://github.com/jemalloc/jemalloc/pull/2793): [3bc89cf](https://github.com/jemalloc/jemalloc/commit/3bc89cfecab89cdc2cd6ed8566e15b7fa4fdac88)
- Format and adjust code style for tcache_max tests.
  ↳ [#2837](https://github.com/jemalloc/jemalloc/pull/2837): [5541853](https://github.com/jemalloc/jemalloc/commit/554185356bf990155df8d72060c4efe993642baf)
- Removed unused options from batch madvise tests.
  ↳ No PR: [1972241](https://github.com/jemalloc/jemalloc/commit/1972241cd204c60fb5b66f23c48a117879636161)
- Clean up unused code in test files and fix build issues.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [e4fa331](https://github.com/jemalloc/jemalloc/commit/e4fa33148a4e93275dac0f306d8759c89597d55f), [de886e0](https://github.com/jemalloc/jemalloc/commit/de886e05d27ef3806dca802f3b9d9a0af7765046)
- Fixed the segfault caused by the stack size exceeding the limit in the large page test and changed to dynamically allocating memory.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [c5547f9](https://github.com/jemalloc/jemalloc/commit/c5547f9e64da41ccefa43d349b6bb79d09d5d63b)
- Inline boolean variables that are always false in test files as constant parameters.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [f714cd9](https://github.com/jemalloc/jemalloc/commit/f714cd9249eb1df010b035623ebca89b7614b1cc)
- Added page allocator benchmark testing tool, including data preprocessing and micro-benchmark testing, and expanded output information.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [56cdce8](https://github.com/jemalloc/jemalloc/commit/56cdce8592bf4ffd7962bed99b31027f22e1895d), [261591f](https://github.com/jemalloc/jemalloc/commit/261591f12360fbce99440584a611e9c338ff7378), [707aab0](https://github.com/jemalloc/jemalloc/commit/707aab0c955e97abed6bd0780eb47cd38e7b1843), [7c40be2](https://github.com/jemalloc/jemalloc/commit/7c40be249cc204b2698d7f97ec5ac1de5551a3cc)
- The testing framework now supports running specified subtests through the JEMALLOC_TEST_NAME environment variable.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [0fa27fd](https://github.com/jemalloc/jemalloc/commit/0fa27fd28fd75fc3305d61c742ed028c5b874231)
- Added unit test coverage for bin interface.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [a75655b](https://github.com/jemalloc/jemalloc/commit/a75655badf31a2c6187bf069f8103c626542941f)
- Add unit tests for configuration parsing and its helper functions.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [86b7219](https://github.com/jemalloc/jemalloc/commit/86b721921386a7192e010ec28c7b2308373d07b0)

### Performance optimization
- Inline the implementation of free and sdallocx into the C++ operator delete, optimizing performance by moving the relevant functions to the inline header file and calling the inline version directly.
  ↳ [#2332](https://github.com/jemalloc/jemalloc/pull/2332): [e8f9f13](https://github.com/jemalloc/jemalloc/commit/e8f9f13811c16acb1ab8771fd2ffe4437e1b8620)
- Enable fast thread-local storage for threads that only perform release operations, and when enough release activity is detected, fully initialize the TSD to avoid slow path overhead.
  ↳ [#2349](https://github.com/jemalloc/jemalloc/pull/2349): [143e9c4](https://github.com/jemalloc/jemalloc/commit/143e9c4a2f4eb8916e9802323485fd91260fd17c)
- Optimized two comparison functions, edata_cmp_summary_comp and edata_esnead_comp, using branchless implementation, and using 128-bit integer encoding to reduce comparison instructions when supporting __uint128_t, improving the performance of the former by 30%, and the overall allocator acceleration by about 1%.
  ↳ [#2423](https://github.com/jemalloc/jemalloc/pull/2423): [6841110](https://github.com/jemalloc/jemalloc/commit/6841110bd6ed17b32a5fed90c53c64555366a792) | [#2714](https://github.com/jemalloc/jemalloc/pull/2714): [0181aaa](https://github.com/jemalloc/jemalloc/commit/0181aaa495bc6ef3dcd570ea5d37cb7b72375614)
- Use local variables to set the alignment of specific memory allocations to avoid unnecessary alignment and memory fragmentation caused by permanently modifying mmap_flags.
  ↳ [#2456](https://github.com/jemalloc/jemalloc/pull/2456): [5832ef6](https://github.com/jemalloc/jemalloc/commit/5832ef658975d5f2da2bdfddf55712d9fa343e30)
- When background threads are enabled, the cleaning strategy of the dedicated oversized arena is changed from eager cleaning to normal cleaning to alleviate the performance bottleneck in frequent oversized allocation scenarios.
  ↳ [#2466](https://github.com/jemalloc/jemalloc/pull/2466): [d131331](https://github.com/jemalloc/jemalloc/commit/d1313313101f9df127bba08bf8fd90a849bf3b87)
- Use char* pointer arithmetic instead of uintptr_t integer conversion in phn_link_get, retaining pointer source information and improving compiler optimization effects.
  ↳ [#2481](https://github.com/jemalloc/jemalloc/pull/2481): [36ca0c1](https://github.com/jemalloc/jemalloc/commit/36ca0c1b7de5fc92e6be48f73f28a6dce0e8890e)
- Replace all integer-to-pointer conversions that suppress optimizations with equivalent operations that preserve pointer source information, and enable clang-tidy checks to prevent such problems in the future.
  ↳ [#2485](https://github.com/jemalloc/jemalloc/pull/2485): [3e82f35](https://github.com/jemalloc/jemalloc/commit/3e82f357bb218194df5ba1acee39cd6a7d6fe6f6)
- Use the assume built-in function provided by the compiler to replace the original unreachable implementation to express assumptions more reliably and avoid potential performance issues.
  ↳ [#2510](https://github.com/jemalloc/jemalloc/pull/2510): [4f50f78](https://github.com/jemalloc/jemalloc/commit/4f50f782fa8e48248684e9f479b895fe19609635)
- Optimized the alignment and locality of bins and their mutex locks in arena, and adjusted the memory allocation layout to improve performance.
  ↳ [#2560](https://github.com/jemalloc/jemalloc/pull/2560): [3025b02](https://github.com/jemalloc/jemalloc/commit/3025b021b9206478d2edcf017f1df7657d35e615)
- Optimize the lock competition when tcache is refreshed to the arena bin: partition by bin before locking, to avoid full array scanning when the lock is held, and to know the number to be refreshed in advance.
  ↳ [#2608](https://github.com/jemalloc/jemalloc/pull/2608): [44d91cf](https://github.com/jemalloc/jemalloc/commit/44d91cf2434796188486960a07771709c15b0c2b)
- Optimize the fast path. When the allocation size is known at compile time, the calculation method is used instead of the lookup table, so that the size class index and available size can be statically calculated after LTO is inline, improving performance.
  ↳ [#2708](https://github.com/jemalloc/jemalloc/pull/2708): [323ed2e](https://github.com/jemalloc/jemalloc/commit/323ed2e3a8c88c7db89b4119b10192af4303d29c)
- Added a size limit to the merge operation of large extents in dirty ecache to avoid merging into an extent that is too large and difficult to be reused by subsequent requests, and improve memory reuse efficiency.
  ↳ [#2842](https://github.com/jemalloc/jemalloc/pull/2842): [3c14707](https://github.com/jemalloc/jemalloc/commit/3c14707b016b156c5f86dfd21304b01161c40750)
- Change the atomic operation for accessing the process's madvise pid file descriptor from sequential consistency to relaxed atomic operation to improve performance.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [9528a2e](https://github.com/jemalloc/jemalloc/commit/9528a2e2dd37154475b8a36186e62f32de17cf58)
- Fixed an issue where pac_mapped statistics were incorrectly inflated when allocation failed, and statistics were only updated when allocation was successful.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [3a8bee8](https://github.com/jemalloc/jemalloc/commit/3a8bee81f18bd241ba571a6a77c940c8f8cfcfb1)
- Removed dead storage assignments and unused variables in preparation for enabling CI static analysis.
  ↳ [#2437](https://github.com/jemalloc/jemalloc/pull/2437): [3e2ba7a](https://github.com/jemalloc/jemalloc/commit/3e2ba7a6510be583edb316372f8cfff35f2f25d5)
- Unify parameter names for function declarations and definitions in multiple header files, and enable static analysis checks to prevent future problems.
  ↳ [#2478](https://github.com/jemalloc/jemalloc/pull/2478): [1d9e9c2](https://github.com/jemalloc/jemalloc/commit/1d9e9c2ed6f0cb3bf168c0d602ae0a289ee27093)
- Change the loop variable type in the background thread enablement function from unsigned to size_t to avoid unnecessary vectorization by the compiler and fix memset recognition issues.
  ↳ [#2611](https://github.com/jemalloc/jemalloc/pull/2611): [ed9b00a](https://github.com/jemalloc/jemalloc/commit/ed9b00a96b25ea24e90875d7a79cdbf3411dd53b)
- Refactor cache_bin.h to concentrate the race logic of cross-thread statistical reading into a single function. The remaining functions remove race parameters and use the cache_bin_sz_t type uniformly.
  ↳ [#2317](https://github.com/jemalloc/jemalloc/pull/2317): [ce29b4c](https://github.com/jemalloc/jemalloc/commit/ce29b4c3d9256956a8d60302b5d1fa72c3479686)
- Use a for loop to handle refresh requests that exceed CACHE_BIN_NFLUSH_BATCH_MAX, and add a new tcache_get_default_ncached_max function.
  ↳ [#2677](https://github.com/jemalloc/jemalloc/pull/2677): [47c9bcd](https://github.com/jemalloc/jemalloc/commit/47c9bcd402110be3f64517ad9366d1cfaa751d48)
- Introduce a filling control mechanism to optimize tcache's processing in burst allocation scenarios.
  ↳ [#2685](https://github.com/jemalloc/jemalloc/pull/2685): [7c99686](https://github.com/jemalloc/jemalloc/commit/7c996861656f67dc74ab66f1bc6e758ed96c69b3)

### Security related
- Fixed the stack out-of-bounds writing vulnerability caused by incorrect use of the address operator in background_thread.c, and the out-of-bounds writing vulnerability in malloc_vsnprintf when size is 0, and added relevant unit tests.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [5f353dc](https://github.com/jemalloc/jemalloc/commit/5f353dc28383d070ffa540d1679153f8101e2aa7) | [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [c2d5704](https://github.com/jemalloc/jemalloc/commit/c2d57040f0d281449febb9bb80287e63bfb271fe)

### Documentation
- Updated the documentation to explain that muzzy decay is disabled by default since 5.2.0, a new mallctl interface has been added since 5.3.0, and the description of the default value of opt.max_background_threads has been corrected.
  ↳ [#2730](https://github.com/jemalloc/jemalloc/pull/2730): [8c2b8bc](https://github.com/jemalloc/jemalloc/commit/8c2b8bcf24ec67523d310f46c38730b1d3348b39) | [#2869](https://github.com/jemalloc/jemalloc/pull/2869): [6515df8](https://github.com/jemalloc/jemalloc/commit/6515df8cec7fe50f6b45069f82bdf685171f9ee7) | [#2882](https://github.com/jemalloc/jemalloc/pull/2882): [b8646f4](https://github.com/jemalloc/jemalloc/commit/b8646f4db33338411b590b67f1f04e8a1eedc061)
- Updated ChangeLog to record version 5.3.1 release information.
  ↳ No PR: [81034ce](https://github.com/jemalloc/jemalloc/commit/81034ce1f1373e37dc865038e1bc8eeecf559ce8)

### Build/CI
- Enabled the -Wstrict-prototypes compilation option and fixed related warnings, then removed the option from the default compilation flags and enabled it only in CI static analysis to avoid breaking autoconf's feature detection.
  ↳ [#2473](https://github.com/jemalloc/jemalloc/pull/2473): [602edd7](https://github.com/jemalloc/jemalloc/commit/602edd75664e2a2ef3063d9b3bd42d1f81a1be2b) | [#2477](https://github.com/jemalloc/jemalloc/pull/2477): [5711dc3](https://github.com/jemalloc/jemalloc/commit/5711dc31d87c5aa5b4dd17a0bda850516a45ae53)
- Fixed a compilation issue caused by searching the math library libm under MSVC 2022, skipping the libm search when MSVC is detected.
  ↳ [#2720](https://github.com/jemalloc/jemalloc/pull/2720): [734f29c](https://github.com/jemalloc/jemalloc/commit/734f29ce56a2769857b084a37af09f5846c56a32)
- Added --enable-tsan and --enable-ubsan options to autoconf configuration for enabling threads and undefined behavior sanitizer.
  ↳ [#2779](https://github.com/jemalloc/jemalloc/pull/2779): [34c823f](https://github.com/jemalloc/jemalloc/commit/34c823f1479047990a73d0e9acf396c2e04fb6b1)
- Added additional detection of strerror_r in configure.ac to avoid misjudgments caused by reasons other than the function itself.
  ↳ [#2797](https://github.com/jemalloc/jemalloc/pull/2797): [a4defdb](https://github.com/jemalloc/jemalloc/commit/a4defdb85434c2027c45c956f4d6d333997a1b50)
- Updated AppVeyor configuration, removed --enable-limit-usize-gap compilation option, and added -fcommon compilation flag to some build configurations.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [95fc091](https://github.com/jemalloc/jemalloc/commit/95fc091b0f4f8d4e7a2209baf2e8411a21b234a4)
- Fixed process_madvise compilation check, added unistd.h header file to ensure syscall function declaration is visible, and removed unused sys/mman.h.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [ced8b3c](https://github.com/jemalloc/jemalloc/commit/ced8b3cffb650af8b7bef7f6995b9032b55aeb0b)
- Fixed portability of grep patterns in configure.ac, replacing the GNU extended backslash plus sign with the more general asterisk pattern, and improving the organization of configuration logic.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [6743518](https://github.com/jemalloc/jemalloc/commit/67435187d103a9bef7995be3d625712329578e64), [365747b](https://github.com/jemalloc/jemalloc/commit/365747bc8d1cf202342d905555d7cd360f9ba118) | [#2750](https://github.com/jemalloc/jemalloc/pull/2750): [a361e88](https://github.com/jemalloc/jemalloc/commit/a361e886e2ec23513e374abc1e4e0429cc93ec5c) | [#2396](https://github.com/jemalloc/jemalloc/pull/2396): [d503d72](https://github.com/jemalloc/jemalloc/commit/d503d72129eddb2175d5d5119c9b70d507112947)
- Temporarily removed Windows build configurations in Travis CI due to infrastructure failure.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [755735a](https://github.com/jemalloc/jemalloc/commit/755735a6bf8f7b7f4e31ebc684f0fce7ac22dd78)
- Added percpu_arena test task in macOS CI.
  ↳ [#2291](https://github.com/jemalloc/jemalloc/pull/2291): [adc70c0](https://github.com/jemalloc/jemalloc/commit/adc70c051135ac8909ca37492d7b104150077033)
- Added a new GitHub Action workflow to automatically run static analysis on each PR.
  ↳ [#2447](https://github.com/jemalloc/jemalloc/pull/2447): [0538519](https://github.com/jemalloc/jemalloc/commit/05385191d4ba42eb219141503a42c648722a8d4f)
- Fixed LLVM download version in CI workflow to be llvmorg-16.0.4.
  ↳ [#2465](https://github.com/jemalloc/jemalloc/pull/2465): [46e464a](https://github.com/jemalloc/jemalloc/commit/46e464a26bcf83c414db489c23236663ee570260)
- Upgraded Travis CI's Ubuntu distribution from Focal to Jammy.
  ↳ [#2508](https://github.com/jemalloc/jemalloc/pull/2508): [162ff83](https://github.com/jemalloc/jemalloc/commit/162ff8365da9bc30f3dcddf0e02c7b7c40197bfc)
- Fallback of install -v option in favor of explicit echo command to resolve incompatibility issue on NetBSD.
  ↳ No PR: [df7ad8a](https://github.com/jemalloc/jemalloc/commit/df7ad8a9b6121c5c4b15bad5606b51bf734416a6)
- Disabled end-of-support FreeBSD 12 builds in Travis CI.
  ↳ [#2589](https://github.com/jemalloc/jemalloc/pull/2589): [3a6296e](https://github.com/jemalloc/jemalloc/commit/3a6296e1ef2249b5bb0cffb0be47376ea0491aad)
- Enabled --enable-limit-usize-gap option in CI configuration.
  ↳ [#2646](https://github.com/jemalloc/jemalloc/pull/2646): [70f019c](https://github.com/jemalloc/jemalloc/commit/70f019cd3abc5dfc67df1b8a2c460bc5e8221ae2)
- Removed tests for ppc64le architecture from Travis CI configuration.
  ↳ [#2697](https://github.com/jemalloc/jemalloc/pull/2697): [5b72ac0](https://github.com/jemalloc/jemalloc/commit/5b72ac098abce464add567869d082f2097bd59a2)
- Added Travis CI tests for ARM64 architecture.
  ↳ [#2699](https://github.com/jemalloc/jemalloc/pull/2699): [db4f0e7](https://github.com/jemalloc/jemalloc/commit/db4f0e71820017039f09e5acc04b554826e304fd)
- Enabled huge page testing on arm64 architecture in Travis CI.
  ↳ [#2770](https://github.com/jemalloc/jemalloc/pull/2770): [a17385a](https://github.com/jemalloc/jemalloc/commit/a17385a882c252a292299ab047d13fc3b2d6fb16)
- Added build configuration to enable frame pointer profiling in Travis CI tests.
  ↳ [#2811](https://github.com/jemalloc/jemalloc/pull/2811): [81f35e0](https://github.com/jemalloc/jemalloc/commit/81f35e0b55c52cb0c3e1171afd477e1cb66fafaf)
- Removed macOS build configurations that are no longer supported in Travis CI.
  ↳ [#2831](https://github.com/jemalloc/jemalloc/pull/2831): [f81fb92](https://github.com/jemalloc/jemalloc/commit/f81fb92a8984b767dae10dc54ef48d1d50e6e1de)
- Added a new script to generate GitHub Actions workflow, replacing the original Travis CI and Cirrus CI.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [441e840](https://github.com/jemalloc/jemalloc/commit/441e840df77b88c2fb32d07f56483097261c2f5c)
- Updated Windows build instructions and removed duplicate content.
  ↳ [#2292](https://github.com/jemalloc/jemalloc/pull/2292): [3713932](https://github.com/jemalloc/jemalloc/commit/3713932836db1190ebadd4a0643db2d354b84fa3)
- Added instructions for building jemalloc via vcpkg in the installation documentation.
  ↳ No PR: [c0c9783](https://github.com/jemalloc/jemalloc/commit/c0c9783ec9289e6d1de749ff20081af65bdd78b8)
- Switch URLs in documentation and package configuration files from HTTP to HTTPS.
  ↳ [#2385](https://github.com/jemalloc/jemalloc/pull/2385): [4edea8e](https://github.com/jemalloc/jemalloc/commit/4edea8eb8e879bf4d89a3ed418bf90bb8e09d93b)

### Maintenance
- Add a TODO comment in sec.c to indicate whether future benchmark testing is worth blocking on all shards to improve the hit rate.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [db7d997](https://github.com/jemalloc/jemalloc/commit/db7d99703d41e58ba2932e98a6e12dd377028231)
- Added macros to suppress compilation warnings and static analysis warnings.
  ↳ [#2487](https://github.com/jemalloc/jemalloc/pull/2487): [c49c17f](https://github.com/jemalloc/jemalloc/commit/c49c17f128cc757c6bd4d026af181f01e28f3b41) | [#2608](https://github.com/jemalloc/jemalloc/pull/2608): [86f4851](https://github.com/jemalloc/jemalloc/commit/86f4851f5d1242f4a17f78afeb4b974be5b2b1aa)
- Added variable initialization to eliminate uninitialized variable warnings.
  ↳ [#2698](https://github.com/jemalloc/jemalloc/pull/2698): [bd0a5b0](https://github.com/jemalloc/jemalloc/commit/bd0a5b0f3b6ce17a5f888e8e08ee5de774b29579) | [#2718](https://github.com/jemalloc/jemalloc/pull/2718): [de5606d](https://github.com/jemalloc/jemalloc/commit/de5606d0d819cbea5c9ef17c989821c1bd7a6697) | [#2828](https://github.com/jemalloc/jemalloc/pull/2828): [c20a63a](https://github.com/jemalloc/jemalloc/commit/c20a63a765dcd22f6b91676ab03507dd9d7b3e2d)
- Improve statistical output: adjust column width to support high values, and add display opt.limit_usize_gap configuration item.
  ↳ [#2644](https://github.com/jemalloc/jemalloc/pull/2644): [c1a3ca3](https://github.com/jemalloc/jemalloc/commit/c1a3ca3755f2adae078b14925e874a6ff743aba1) | [#2828](https://github.com/jemalloc/jemalloc/pull/2828): [c23a6bf](https://github.com/jemalloc/jemalloc/commit/c23a6bfdf6eed78dbe9c2b39a3798d091843a957)
- Improved internal assertions and consistency checks.
  ↳ [#2560](https://github.com/jemalloc/jemalloc/pull/2560): [e2cd271](https://github.com/jemalloc/jemalloc/commit/e2cd27132acfe04604352dbaa9d95b124f9ea50e) | [#2719](https://github.com/jemalloc/jemalloc/pull/2719): [6cc4217](https://github.com/jemalloc/jemalloc/commit/6cc42173cbb2dad6ef5c7e49e6666987ce4cf92c) | [#2870](https://github.com/jemalloc/jemalloc/pull/2870): [1d018d8](https://github.com/jemalloc/jemalloc/commit/1d018d8fdabec88134b32122aa054cb8b37fe29c)
- Code cleanup: remove unused macros and merge memset calls.
  ↳ [#2485](https://github.com/jemalloc/jemalloc/pull/2485): [4827bb1](https://github.com/jemalloc/jemalloc/commit/4827bb17bdd5a25921c5b091ffadf3039d297b17) | [#2494](https://github.com/jemalloc/jemalloc/pull/2494): [9ba1e1c](https://github.com/jemalloc/jemalloc/commit/9ba1e1cb37b84daf00d37936f4223823c2aaac44)
- Fix compilation warning on macOS due to missing curly braces for zero-initializer.
  ↳ [#2557](https://github.com/jemalloc/jemalloc/pull/2557): [04d1a87](https://github.com/jemalloc/jemalloc/commit/04d1a87b78230931aa28cca72bef4424223a8d39)
- Updated security check error message: adding --enable-debug is no longer recommended when building with debug enabled.
  ↳ [#2531](https://github.com/jemalloc/jemalloc/pull/2531): [7d563a8](https://github.com/jemalloc/jemalloc/commit/7d563a8f8117966d9466d92ed2c782eeae7a19eb)
- Add size check for stack array declaration, limit to no more than 2048 bytes.
  ↳ [#2677](https://github.com/jemalloc/jemalloc/pull/2677): [48f66cf](https://github.com/jemalloc/jemalloc/commit/48f66cf4a22af3b380d4c049f79fb7e820eba3d3)
- Upgrade actions/checkout and actions/upload-artifact in CI workflow to v4 version.
  ↳ [#2615](https://github.com/jemalloc/jemalloc/pull/2615): [1978e5c](https://github.com/jemalloc/jemalloc/commit/1978e5cdac731dca43b62e4b03612c0758f7cece)

### Others
- Print all malloc_conf settings in statistics output, covering global variables, symlinks and environment variables.
  ↳ [#2601](https://github.com/jemalloc/jemalloc/pull/2601): [373884a](https://github.com/jemalloc/jemalloc/commit/373884ab482ad1de4b839e40bd38fd154f324707)
- Clean up trailing spaces in code and add GitHub Action to prevent subsequent reintroduction.
  ↳ [#2430](https://github.com/jemalloc/jemalloc/pull/2430): [f2e00d2](https://github.com/jemalloc/jemalloc/commit/f2e00d2fd3e56e6599f889ee09d5c41ed4012015)
- Remove duplicate words from documents.
  ↳ [#2303](https://github.com/jemalloc/jemalloc/pull/2303): [41a859e](https://github.com/jemalloc/jemalloc/commit/41a859ef7325569c6c25f92d294d45123bb81355)
- Expanded negative example of "sum first then debias" in PROFILING_INTERNALS.md.
  ↳ [#2339](https://github.com/jemalloc/jemalloc/pull/2339): [b04e766](https://github.com/jemalloc/jemalloc/commit/b04e7666f2f29de096a170c49cb49cd8f308b7e1)
- Fix the indentation problem in cache_bin.h, and change pointer arithmetic to use the += operator.
  ↳ [#2416](https://github.com/jemalloc/jemalloc/pull/2416): [f2b2890](https://github.com/jemalloc/jemalloc/commit/f2b28906e63bef7518c58236e3e9dde8e4fceb89)
- Fix link identifier for arenas.i.bins.j.mutex in manual.
  ↳ [#2528](https://github.com/jemalloc/jemalloc/pull/2528): [87c56c8](https://github.com/jemalloc/jemalloc/commit/87c56c8df86107fdf32e92db68211e8b10d94ded)
- Corrected the format of the malloc_conf option to enable logging in the documentation, changing the equal sign to a colon.
  ↳ [#2548](https://github.com/jemalloc/jemalloc/pull/2548): [005f20a](https://github.com/jemalloc/jemalloc/commit/005f20aa7fdef1be6f9fe46e4f2e7b88177a9f21)
- Add rules to ignore clangd related directories (/build/ and /.cache/) in .gitignore.
  ↳ [#2598](https://github.com/jemalloc/jemalloc/pull/2598): [f96010b](https://github.com/jemalloc/jemalloc/commit/f96010b7fa8ce5f83802144bdebf2bb7a6679649)
- Updated the configuration cache file examples in INSTALL.md, replacing MADV_FREE related examples with MADV_DONTDUMP.
  ↳ [#2731](https://github.com/jemalloc/jemalloc/pull/2731): [02251c0](https://github.com/jemalloc/jemalloc/commit/02251c0070969e526cae3dde6d7b2610a4ed87ef)
- Add clang-format off/on comments before and after macro definitions containing multi-line commands to avoid clang-format incorrectly formatting these macros.
  ↳ [#2857](https://github.com/jemalloc/jemalloc/pull/2857): [edaab8b](https://github.com/jemalloc/jemalloc/commit/edaab8b3ad752a845019985062689551cd6315c1)
- Reformat the entire codebase using clang-format 18.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [6200e89](https://github.com/jemalloc/jemalloc/commit/6200e8987feb5eae198b95b14cd89d09695f7b3c)
- Fixed multiple spelling errors in source code comments.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [395e63b](https://github.com/jemalloc/jemalloc/commit/395e63bf7e79b9faf7187add17ee6b0571857a60)
- Clean up and correct outdated content and spelling errors in code comments.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [48b4ad6](https://github.com/jemalloc/jemalloc/commit/48b4ad60a7ee897c813fb987183bb13d3596814c), [5e49c28](https://github.com/jemalloc/jemalloc/commit/5e49c28ef042d7c1f446ec6615d6d84bafabb3fd)
- Fix typos in comments and adjust function declaration format.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [2a66c0b](https://github.com/jemalloc/jemalloc/commit/2a66c0be5a3727817ccf95c6150d10c19aae00f4)
- Fix operator error in alloc_count check in prof_log_rep_check.
  ↳ [#2866](https://github.com/jemalloc/jemalloc/pull/2866): [a87c518](https://github.com/jemalloc/jemalloc/commit/a87c518babfe81395a63b6b023245d8359ca1b96)
- Change the indentation of a space in Makefile.in to a tab character.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [daf4417](https://github.com/jemalloc/jemalloc/commit/daf44173c54f2e388210bc7f03b4e9bfd938597c)
- Run clang-format on both source files to unify the code format.
  ↳ [#2864](https://github.com/jemalloc/jemalloc/pull/2864): [ace437d](https://github.com/jemalloc/jemalloc/commit/ace437d26ae9c2b27d08492135da52d211c53e01)
- Run clang-format on test files to unify code format.
  ↳ [#2873](https://github.com/jemalloc/jemalloc/pull/2873): [3ac9f96](https://github.com/jemalloc/jemalloc/commit/3ac9f96158f3b095496e260259a3c32857eafd28), [a47fa33](https://github.com/jemalloc/jemalloc/commit/a47fa33b5a7d91ab0218436a75b652a2b65588c9)
