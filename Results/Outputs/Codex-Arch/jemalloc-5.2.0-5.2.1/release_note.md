# Release Note

## Important Changes

### Debugging & Profiling Layer

- bin_stats_t adds nonfull_slabs count and explains it in the manual, used to count the number of slabs that are not yet full. [commit](https://github.com/jemalloc/jemalloc/commit/7fc4f2a32c74701e40e98c8ac05aa7cf12d876c9)
- Added nfills/nflushes to arenas.i.small and arenas.i.large statistics, recording the number of times thread caches fill and reclaim objects to/from arenas. [commit](https://github.com/jemalloc/jemalloc/commit/07c44847c24634d0d11f9ceab7318400ffc1a16e)
- Added the confirm_conf option, which outputs the parsed malloc configuration at initialization, making it easy to confirm the final values of user parameters. [commit](https://github.com/jemalloc/jemalloc/commit/c92ac306013bc95cd5f34de421b1aa5eb1f28971)
- Added abandoned_vm statistics, accumulating the virtual memory space temporarily left behind due to inability to reclaim. [commit](https://github.com/jemalloc/jemalloc/commit/4e36ce34c1e6a6f470a9355b90b0a757c6fdb0b5)

### User API Layer

- Added an extent utilization analysis mallctl, providing a query interface for utilization of allocated, active, and reclaimable extents. [commit](https://github.com/jemalloc/jemalloc/commit/9aab3f2be041b09f42375d3bf173d1a8795a1ee9)
- configure probes for format_arg attribute support and defines a jemalloc-specific macro, enabling emitter annotations on compilers that support the attribute. [commit](https://github.com/jemalloc/jemalloc/commit/7f7935cf7805036d42fb510592ab8b40bcfb0690)
- Added experimental.arenas.i.pactivep mallctl, querying pointer or count information for the current active pages of a specified arena. [commit](https://github.com/jemalloc/jemalloc/commit/e13cf65a5f37bbd9b44badb198ccc138cbacc219)
- confirm_conf output adds indentation for each independent configuration option, making it easier to distinguish global and arena-level configuration items. [commit](https://github.com/jemalloc/jemalloc/commit/85f0cb2d0c0a05e9fc926544c65ca784c03ab239)

### Platform Abstraction Layer

- Windows builds now enable opt.retain by default, allowing released virtual address regions to be retained by jemalloc for subsequent allocations. [commit](https://github.com/jemalloc/jemalloc/commit/badf8d95f11cf8ead0f8b7192663002d1d4dc4b2)

### Cross-cutting / Other Architecture-related Changes

- configure adds the --disable-doc option, allowing skipping manual and API documentation generation during build. [commit](https://github.com/jemalloc/jemalloc/commit/702d76dbd03e4fe7347399e1e322c80102c95544)
- The extent first-fit matching strategy applies the max_active_fit limit, avoiding first-fit selecting active extents significantly larger than requested. [commit](https://github.com/jemalloc/jemalloc/commit/b62d126df894dac00772eb5f3d170a1c1d3d1614)
- Added safety_check.c to the Visual Studio 2015 project and filters, ensuring MSBuild compilation includes safety check implementation. [commit](https://github.com/jemalloc/jemalloc/commit/40a3435b8dc225ad61329aca89d9c8d0dfbc03ab)
- Windows extent management implements retain mode, retaining released address space for reuse in subsequent allocations. [commit](https://github.com/jemalloc/jemalloc/commit/9a86c65abc2cf242efe9354c9ce16901673eeb0c)

## Routine Changelog

### Bug Fixes

- Fixed the invocation of extent external function macros, completing function prototype declarations to eliminate missing-prototype diagnostics when compilation warnings are enabled. [commit](https://github.com/jemalloc/jemalloc/commit/14e4176758379875c4ef486d6c57327ed07edd86)
- jeprof fixes the comment spelling inherited from tcmalloc pprof, keeping profiling tool help text accurate. [commit](https://github.com/jemalloc/jemalloc/commit/498f47e1ec83431426cdff256c23eceade41b4ef)
- Fixed the assertion condition in the free fast path, avoiding legitimate small object frees being misjudged as size class errors. [commit](https://github.com/jemalloc/jemalloc/commit/13e88ae9700416b43bf88c596ea15c85bdb9f9e7)
- Fixed the format type conversion in the GET_ARG_NUMERIC macro, eliminating GCC 9.1 warnings for numeric parameter parsing. [commit](https://github.com/jemalloc/jemalloc/commit/2d6d099fed05b1509e81e54458516528bfbbf38d)
- Statistics queries no longer wait for background thread locks, using non-blocking state reads instead to avoid stats requests being blocked by purge threads. [commit](https://github.com/jemalloc/jemalloc/commit/1a71533511027dbe3f9d989659efeec446915d6b)
- Fixed the byte count used for redzone size configuration and object boundary checks, ensuring consistent guard region lengths for allocation and validation. [commit](https://github.com/jemalloc/jemalloc/commit/7720b6e3851d200449914448c7163f7af92cd63f)
- Fixed the documentation option logic description and internal printing conditions, ensuring safety check configuration behavior matches implementation. [commit](https://github.com/jemalloc/jemalloc/commit/d26636d566167a439ea18da7a234f9040668023b)
- Fixed buffer boundary handling in prof_dump_write when writing profiling dumps, avoiding incorrect updates to file output positions. [commit](https://github.com/jemalloc/jemalloc/commit/e0a0c8d4bf512283e8c85fb4a51761fce5e0c08f)
- posix_memalign handles zero-size requests per standard and correctly sets the output pointer, adding integration test coverage for this boundary condition. [commit](https://github.com/jemalloc/jemalloc/commit/f32f23d6cc3ac9e663983ae62371acd47405c886)
- When extents do not support splitting, reclaim parent extents and virtual memory mappings, avoiding address space leaks on split failure paths. [commit](https://github.com/jemalloc/jemalloc/commit/57dbab5d6bc764a8b971334ec80977d6333688af)
- On Windows, when retain is not enabled, only accept extents that exactly match the requested size, avoiding approximate matching for system-allocated regions that cannot be split. [commit](https://github.com/jemalloc/jemalloc/commit/c9cdc1b27f8aa9c1e81e733e60d470c04be960b3)
- Adjusted temporary variable usage in the GCC atomic operations header, avoiding g++ compiler warnings for unused variables. [commit](https://github.com/jemalloc/jemalloc/commit/9344d25488b626739c9080eb471d1bd15eeb046b)
- Check the remaining capacity of the output buffer before writing profiling dumps, avoiding formatted statistics content exceeding buffer boundaries. [commit](https://github.com/jemalloc/jemalloc/commit/8a94ac25d597e439b05b38c013e4cb2d1169c681)

### Refactoring

- Placed the additional allocation size safety check under configure option control, allowing users to choose between performance and strict checking. [commit](https://github.com/jemalloc/jemalloc/commit/f4d24f05e1f270c43bc4129c0d18d673b8ac85b8)
- Refactored arena_dalloc and arena_sdalloc deallocation functions, unifying handling of object reclamation branches with known and unknown sizes. [commit](https://github.com/jemalloc/jemalloc/commit/a3fa597921987709eb0aa2258f1b35cc433ae5d4)
- Split the profiling log implementation into a separate module, isolating log buffer, formatting, and output logic. [commit](https://github.com/jemalloc/jemalloc/commit/7618b0b8e458d9c0db6e4b05ccbe6c6308952890)
- Refactored the profiling core interface, organizing sampling state and data recording responsibilities into a separate internal module. [commit](https://github.com/jemalloc/jemalloc/commit/0b462407ae84a62b3c097f0e9f18df487a47d9a7)
- Reverted the profiling module split, restoring the previous unified profiling implementation managing sampling state. [commit](https://github.com/jemalloc/jemalloc/commit/1a0503367be5950a8da648996ba7ae2620e39393)
- Revert the split of the profiling log module, restoring the organization of log functions in the original profiling implementation. [commit](https://github.com/jemalloc/jemalloc/commit/5742473cc87558b4655064ebacfd837119673928)

### Tests

- Fix the log configuration and expected output of the prof_log unit test, ensuring that profiling log assertions cover the actual recorded content. [commit](https://github.com/jemalloc/jemalloc/commit/c2a3a7cd3f3cbc177d677101be85a31a39c26bd0)
- 32-bit system reduces the number of concurrent threads created by the retained unit test, lowering the memory peak when the test reserves extents simultaneously. [commit](https://github.com/jemalloc/jemalloc/commit/10fcff6c38c08bc2b1a672ff92701012944d843a)

### Performance

- Reorganize the size class definitions and comments in the size class header file, making class limits and classification mapping clearer. [commit](https://github.com/jemalloc/jemalloc/commit/ae124b86849bb5464940db6731183dede6a70873)
- Rearrange the malloc_conf_init macro and configuration field checks, making MALLOC_CONF option parsing more readable while preserving the parsing order. [commit](https://github.com/jemalloc/jemalloc/commit/259b15dec5bff8b67b331b63703aa8511c759077)
- Extend the extent utilization unit test to cover statistics after allocation, splitting, merging, retention, and deallocation. [commit](https://github.com/jemalloc/jemalloc/commit/4c63b0e76a693b0cfdf209cb4f8fbd1ed74453b0)
- Cache the max_active_fit result in the first-fit extent search, reducing repeated checks of the maximum size constraint for the same request during traversal. [commit](https://github.com/jemalloc/jemalloc/commit/1d148f353a2c71bc12fd066e467649fd17df3c95)

### Documentation

- Update the manual's opt.retain description, noting that Windows enables retain mode by default and its impact on virtual address space reclamation. [commit](https://github.com/jemalloc/jemalloc/commit/9f6a9f4c1f78fd61297e01ae1521af9696d2023b)

### Build / CI

- Split the extent utilization API's setting, reading, and error conditions into separate tests, verifying each type of query result individually. [commit](https://github.com/jemalloc/jemalloc/commit/7ee3897740aabdccb2381b7b6ab68fff0aac3ec4)
- The safety_check module performs size and pointer checks through independent functions, reducing the direct inclusion of safety check logic in the allocation fast path. [commit](https://github.com/jemalloc/jemalloc/commit/b92c9a1a81f3f68da87afe5887d8450fef0700d3)
- Add redzoning protection to safety_checks, filling and validating guard areas at allocation object boundaries to detect out-of-bounds writes. [commit](https://github.com/jemalloc/jemalloc/commit/33e1dad6803ea3e20971b46baa299045f736d22a)
- Travis CI builds and runs safety check tests by default, continuously validating redzone and safety check paths. [commit](https://github.com/jemalloc/jemalloc/commit/21cfe59ff7b10a61dabe26cd3dbfb7a255e1f5e8)
- Adjust the execution order of the AppVeyor Windows build configuration so that compilation, testing, and packaging stages run according to dependencies. [commit](https://github.com/jemalloc/jemalloc/commit/34e75630cc512423b4f227338056a2f5d7e81740)

### Maintenance

- Ensure that extent_alloc and DSS allocation paths return addresses that meet page alignment requirements, avoiding extent base addresses not aligned to page size. [commit](https://github.com/jemalloc/jemalloc/commit/93084cdc8960935d0acc93424dddd3a79a86e2da)
- Remove unnecessary comparisons and branch checks in the C++ delete[] fast path, reducing allocator path overhead for array deletion operations. [commit](https://github.com/jemalloc/jemalloc/commit/d3d7a8ef09b6fa79109e8930aaba7a677f8b24ac)
- Add printf-format compiler annotations to emitter format generation functions, enabling compile-time validation of generated format string arguments. [commit](https://github.com/jemalloc/jemalloc/commit/020b5dc7ac5138a347e5462508b2b5e4ecd6bc52)
- Expose the current safety_checks configuration value via mallctl and stats, making it easy for applications and diagnostic tools to confirm whether safety checks are enabled. [commit](https://github.com/jemalloc/jemalloc/commit/f95a88fcd92e8ead1a6c5c8b2ca8c401c6eba162)
- Force the TSD TLS variable declaration to use the configured TLS_MODEL attribute, ensuring thread state access uses a compatible TLS model. [commit](https://github.com/jemalloc/jemalloc/commit/1aabab5fdca1cd76be3900e9272ef83549006ac0)
- Remove the best-fit extent search implementation, unifying on the first-fit strategy to reduce free extent search and maintenance overhead. [commit](https://github.com/jemalloc/jemalloc/commit/56797512083fe1457163170dfa44ee5ec12abe5f)
- Delete the unused prof_accumbytes field in arena, cleaning up state that has been superseded by other profiling statistics. [commit](https://github.com/jemalloc/jemalloc/commit/a2a693e722d3ec0f0fb7dfcac54e775b1837efda)
- On extent_register failure, return the extent to extent_dalloc instead of permanently leaking the acquired extent memory. [commit](https://github.com/jemalloc/jemalloc/commit/42807fcd9ed68c78f660c6dd85bcf9d82e134244)
- When no tcache is available, correctly call arena_dalloc_promoted for deallocating allocations promoted to large objects and return the object's arena. [commit](https://github.com/jemalloc/jemalloc/commit/bc0998a9052957584b6944b6f43fffe0648f603e)
- Fix the printf format string and argument correspondence in profiling logs, ensuring log content is output according to actual values. [commit](https://github.com/jemalloc/jemalloc/commit/82b8aaaeb68ccb65ca52532f4806a43fbdb26b7a)

