# Release Note

## Important Changes

### Core Library Layer

- Add STORE_OFFSET() and STORE_REPCODE() macros to centrally convert real offsets and repeat code numbers in compressed sequences, avoiding each parser duplicating encoding rule handling. [commit](https://github.com/facebook/zstd/commit/1aed962216373a6683ff6f26e4ae0ff8fa62f4e4)
- Create STORED_* macros to uniformly encapsulate offset and repeat code storage rules for compressed sequences, reducing direct dependence of compressor paths on internal numeric encoding. [commit](https://github.com/facebook/zstd/commit/2068889146a8c41947bd57b41c639b9f5ab1b73c)

### Cross-cutting / Other Architecture-related Changes

- Add explicit assembly-disabling compile options for CMake library targets, enabling builds that do not support or need to exclude assembly to use pure C implementations. [commit](https://github.com/facebook/zstd/commit/df5ad5a0f1e087e1202806c8b4baf72d7841edf4)

## Routine Changelog

### Bug Fixes

- Fix MinGW/Clang CMake build library file names, ensuring the zstd-static target generates the expected static library output name. [commit](https://github.com/facebook/zstd/commit/14a0eaf73ba84ab8eabf9ab44b278a13cc0f0b6a)
- Adjust Meson build source files and parameter configuration for MSVC, fixing static library target build support under that compiler. [commit](https://github.com/facebook/zstd/commit/29e44bc5547f88ab5c1942d2514c2d524100b71c)
- Complete the source file list needed for CMake/MSVC builds, ensuring MSVC assembly and C source files are correctly included in the build per target compiler. [commit](https://github.com/facebook/zstd/commit/148ff1577452e1ceb722ff4394007656112d8a41)
- Fix spelling errors in the multithreaded streaming compression example, avoiding incorrect words in example output messages. [commit](https://github.com/facebook/zstd/commit/7ee35bad6b9e20c8f01e96c5e106cab7bd4d45ec)
- Fix assertions in the optimal parser regression test, and adjust affected function declaration formats to restore corresponding builds and test cases. [commit](https://github.com/facebook/zstd/commit/435f5a2e6d7aa8f0ad581c2da688f8a7f1e3e8cd)
- Adjust types of two integer conversions in zstd_lazy.c, so sequence length and offset calculations no longer trigger narrowing conversion warnings. [commit](https://github.com/facebook/zstd/commit/321583ccf508e300d68f6ea3e6fcf9adb13d2a47)
- Fix integer types for offset code conversions in zstd_lazy, eliminating type conversion warnings on the compression path. [commit](https://github.com/facebook/zstd/commit/a34ccad9a6adbaf6bd976434b5ae18a2d60f224a)
- Synchronize the fallback function prototype of POOL_sizeof(), making its const qualification consistent with the official declaration. [commit](https://github.com/facebook/zstd/commit/6211bfee5ec24dc825c11751c33aa31d618b5f10)
- Adjust workspace internal buffer reservation and stage advancement logic, and add region overlap checks, fixing compression performance degradation in issue #2966 scenarios. [commit](https://github.com/facebook/zstd/commit/8c53e526db3bcf5a95f67bd347e1f89c79f4fe94)
- Remove leftover debug prints and temporary options in libzstd.mk and playTests.sh, avoiding irrelevant diagnostic output in normal builds and tests. [commit](https://github.com/facebook/zstd/commit/ff5d1daf33abe71f95f2c90de877ac98cf01af83)
- Fix the literal cost calculation for maximum block length in the optimal parser, avoiding incorrect costs or out-of-bounds handling for unrepresentable lengths from OSS-Fuzz inputs. [commit](https://github.com/facebook/zstd/commit/4d8a2132d0e453232a46dd448e5137035ba25bee)
- Add license headers to the x86-64 Huffman decoding assembly file, and include that file in license integrity tests. [commit](https://github.com/facebook/zstd/commit/c7b03c217c2542152a08e4ca343f8a27d3680901)
- Fix the condition for writing progress information to standard error during decompression, avoiding non-progress output being incorrectly redirected to stderr. [commit](https://github.com/facebook/zstd/commit/308a11b8e88f5201ddeb839269268b3824567d89)

### Refactoring

- Abstract access to the offBase union type in zstd_lazy.c and zstd_opt.c into a unified read method, avoiding code depending on specific union member layout. [commit](https://github.com/facebook/zstd/commit/b7630a474b5e330e07dc743e2a2d7cb26f457a7a)
- Separate the update of the repeat offset code array from returning the new array, uniformly advancing the repcode state of compressor and decompressor via in-place updates. [commit](https://github.com/facebook/zstd/commit/6fa640ef70d01489e2a4a6228f4e439b712f7d68)
- Migrate sequence offset code reads in the zstd_opt optimal parser to common macros, uniformly handling both repcode and real offset encodings. [commit](https://github.com/facebook/zstd/commit/e909fa627fc9005119457bc25e59cd1a03ae76ba)
- Change offset code handling in the zstd_lazy lazy parser to use common macros, eliminating hardcoded assumptions about the numeric representation of sequence storage. [commit](https://github.com/facebook/zstd/commit/92a08eec72c9bd2b28620aab3b47af5a2ae7f0c5)
- Centralize the definition and usage of ZSTD_REP_MOVE, unifying the declaration and maintenance of repeat offset code state transition constants. [commit](https://github.com/facebook/zstd/commit/de9f52e9456f97a3bdf6c2b4ecad424226d65247)
- Rewrite the workspace size calculation expression for readability, keeping the original allocation boundary results unchanged. [commit](https://github.com/facebook/zstd/commit/41ad7332dd59ed9081cee345bd95e080cb96b199)
- Remove unused header files in the dibio example, reducing unnecessary dependencies and avoiding unnecessary compilation coupling. [commit](https://github.com/facebook/zstd/commit/fc946d131b3a028c23d2ae84ade6b6114aa6fec2)
- Refactor the buffer pool interface for multithreaded compression and add memory management notes, clarifying that pool size is configured by maximum buffer count and each worker's buffer requirements. [commit](https://github.com/facebook/zstd/commit/9b6dfedf0c49d6554609419214f58beb6a60480b)

### Tests

- Change ZSTD_storeSeq() parameters from the base value with MINMATCH subtracted to the actual match length, and perform base value conversion uniformly at sequence storage. [commit](https://github.com/facebook/zstd/commit/b77fcac61fadf665f7522dd0c2e44b373eb7d57d)
- Rename seqDef.matchLength to mlBase, clarifying that the sequence structure stores the base value of matchLength−MINMATCH, and restore the actual length when reading. [commit](https://github.com/facebook/zstd/commit/e145b58cfdf94a300295be022d4b41d6ca70d8f1)
- Rename the offset field in compressed sequences to offBase, clarifying its internal representation that encodes both repeat distance codes and real offsets. [commit](https://github.com/facebook/zstd/commit/aeff1283311b6be38c5efc24c019e0f72ce60046)
- Fix command parameters and expected file handling in the tar test in playTests.sh, restoring correct operation of archive decompression cases in different environments. [commit](https://github.com/facebook/zstd/commit/666372c7bf345ef8a238ca1ffbe985ba4a9aedf6)
- Make decodecorpus use common macros to parse sequence offset codes, removing direct dependence on numeric encoding in the offcode union representation. [commit](https://github.com/facebook/zstd/commit/681c81f06c313eed276283c141d0c14e9404b4fa)
- Further migrate compressor paths' dependence on offcode union numeric encoding, uniformly parsing sequences via offset base macros and maintaining repeat code state. [commit](https://github.com/facebook/zstd/commit/8da414231d105e64d424f6661a21e3add8c40fd1)
- Fix the freshCCtx compression scenario benchmark settings in fullbench, ensuring each round times according to the actual lifecycle of a newly created context. [commit](https://github.com/facebook/zstd/commit/213dc6110fda144326cc783c02f98a7886cfe4b3)
- Add the compress_freshCCtx scenario to fullbench, separately measuring compression performance when creating and releasing a brand new ZSTD_CCtx each time. [commit](https://github.com/facebook/zstd/commit/a0b9520e38c459408330bfdfb62f666f331d3bed)
- Add a readelf check in Unix playTests.sh, failing the test if the generated zstd executable has an executable GNU_STACK segment. [commit](https://github.com/facebook/zstd/commit/35208f702f0a5e4ebe70d651efd75770f176b2d0)

### Performance

- Restore the ability to select library optimization compile flags via the command line, allowing libzstd.mk to configure optimization levels according to caller-passed options. [commit](https://github.com/facebook/zstd/commit/75525fcb9f4c7ed1bb39d10aa43ce529c950d208)

### Documentation

- Add ZSTDLIB_STATIC_API markers to ZSTD_findDecompressedSize(), ZSTD_decompressBound(), ZSTD_frameHeaderSize(), and other static-link-only APIs in the manual, aligning documentation signatures with header file visibility. [commit](https://github.com/facebook/zstd/commit/41153071a002296c65c20958e9fb921a8f82edf0)
- Synchronize updates to the zstd manual and zstd/zstdgrep man pages, documenting command-line option descriptions added and adjusted in 1.5.2. [commit](https://github.com/facebook/zstd/commit/e1323744b6998ac237c25904331c6d820bf02aa4)

### Build / CI

- Explicitly disable assembly implementations when Meson uses non-GCC/Clang compilers, avoiding passing incompatible assembly source files to other compilers. [commit](https://github.com/facebook/zstd/commit/c4f5116e95d7aee1fb36f64ce074fc1187630398)
- Automatically detect and enable the noexecstack option for compilation and linking on supported platforms, preventing assembly code from giving the final program an executable stack. [commit](https://github.com/facebook/zstd/commit/4620ce6a9abe7f2aad9ae0ecd4768cd38491edb8)
- Make assembly build rules pass assembly parameters via ASFLAGS instead of CFLAGS, fixing the assembly option channel for libzstd and Linux kernel tests. [commit](https://github.com/facebook/zstd/commit/8ea3d57de4bcff2170296e0d1a5019f030630f3b)

### Maintenance

- Change memcpy calls in public header files to ZSTD_memcpy(), enabling Linux kernel integration to call copy functions through its memory operation redirection adaptation layer. [commit](https://github.com/facebook/zstd/commit/ad7c9fc11e689e105e9c43c016c9160a121ba3b1)
- Mark GNU-stack as non-executable in the x86-64 Huffman decoding assembly object, preventing the linked library from requiring an executable stack. [commit](https://github.com/facebook/zstd/commit/9a9d1ec6f4536ffeb745f360ef010cefd125bfd0)
- Change POOL_sizeof() to accept only const thread pool references, clarifying that this function only queries memory size and does not modify pool state. [commit](https://github.com/facebook/zstd/commit/b1978d60ee6de821501d7e0ce88185f6575028b0)
- Extend the GNU-stack non-executable segment marker from Linux ELF to all ELF targets, avoiding linked artifacts on other ELF systems still having executable stacks. [commit](https://github.com/facebook/zstd/commit/b12edddb3784c59c459a40f6108027b0bcedaf2f)
- Restrict GNU-stack segment directives to ELF and when using the GNU assembler, avoiding non-GNU assemblers rejecting the pseudo-instruction. [commit](https://github.com/facebook/zstd/commit/ef1f9e80ffc62c5de06375bc62012373a5d0b77f)
- Rework the Clang module map, moving header files to the standard module directory and declaring dictbuilder/errors submodules, while listing configuration macros that affect module builds. [commit](https://github.com/facebook/zstd/commit/8dd943e42c13ca33d07ead274e07defd1e2114c5)
- Update the module map path in the Swift Package definition to match the new location after the module map file move. [commit](https://github.com/facebook/zstd/commit/17782224460107dcbc29141db9a9b1209746fd27)
- Inline the xxHash implementation in benchzstd to avoid an extra dependency on a separate xxHash library for the benchmark program. [commit](https://github.com/facebook/zstd/commit/4bd96a61f103ac7ed8b52d39e99424f2f9b52643)
- Bump the Zstandard version number in public headers to 1.5.2 so compile-time version detection reflects this release. [commit](https://github.com/facebook/zstd/commit/46ad9377e8eac2c77ee677a9af94104d996561d9)
- Add hidden visibility to x86-64 Huffman assembly intrinsics to avoid exporting implementation details as dynamic library symbols. [commit](https://github.com/facebook/zstd/commit/568c69a4eb0e30fb03a75176804b47ed51dd3ab1)
- Skip target file timestamp updates when decompressing to standard output to avoid file metadata operations on stdout. [commit](https://github.com/facebook/zstd/commit/57a86d9ec636c75f17a3005962ff178545e404f5)
- Update CI and testing instructions in CONTRIBUTING.md to match the current continuous integration workflow and available test steps. [commit](https://github.com/facebook/zstd/commit/8250faa01bf0a3b46b3204bdefee7ae04ab12f80)

