# Release Note

## Important Changes

### Core Compression Engine
- Deprecated ZSTD_generateSequences function and marked as unsafe (architectural event: Linux_Kernel_Module removed)
  ↳ [#3981](https://github.com/facebook/zstd/pull/3981): [731f4b7](https://github.com/facebook/zstd/commit/731f4b70fcd22fc9badd4e51dc6d939ee6da6c54)
- Added ZSTD_d_maxBlockSize parameter to allow limiting the maximum block size during streaming decompression, thereby reducing memory usage. (Architecture event: Zstd_Core_Module module change)
  ↳ [#3616](https://github.com/facebook/zstd/pull/3616): [0abf2ba](https://github.com/facebook/zstd/commit/0abf2baef925fed4dac13d551c35d817e3206fdd) | [#3617](https://github.com/facebook/zstd/pull/3617): [61efb2a](https://github.com/facebook/zstd/commit/61efb2a047b308b6f0c265e1eae9ca8a062268e4)
- Added targetCBlockSize parameter support, improved the splitting strategy to make sub-block sizes more even, and upgraded this parameter from experimental API to stable API. (Architecture event: Zstd_Core_Module module change)
  ↳ [#3915](https://github.com/facebook/zstd/pull/3915): [68a232c](https://github.com/facebook/zstd/commit/68a232c5917ff387031c76acea80f77e8115419f) | [#3917](https://github.com/facebook/zstd/pull/3917): [038a8a9](https://github.com/facebook/zstd/commit/038a8a906b8bbf60491b2643febaf8f9d5a4139c) | [#3964](https://github.com/facebook/zstd/pull/3964): [3613448](https://github.com/facebook/zstd/commit/3613448fb8623361dc6bd9b32c8d4b3d2da85823) | [#3977](https://github.com/facebook/zstd/pull/3977): [f5728da](https://github.com/facebook/zstd/commit/f5728da365e14a715a131434847f732ee84d8719), [6f1215b](https://github.com/facebook/zstd/commit/6f1215b874dbf74b50dcb64915e91e11ba198008)
- The long decoder adapts to the new decodeSequences interface, removes the old implementation and optimizes the loop logic to detect corruption earlier. (Architecture-related: core decompression module)
  ↳ [#3677](https://github.com/facebook/zstd/pull/3677): [c60dced](https://github.com/facebook/zstd/commit/c60dcedcc91da9bb7550f237f79ee001ca6d1a75)
- Fixed typos and added a new workspace size query function. (Architecture-related: public API)
  ↳ [#3771](https://github.com/facebook/zstd/pull/3771): [fe34776](https://github.com/facebook/zstd/commit/fe34776c207f3f879f386ed4158a38d927ff6d10)
- Implemented single decompression fallback for magicless format, added private functions to support magicless frames. (Architecture-related: public API)
  ↳ [#3971](https://github.com/facebook/zstd/pull/3971): [7d970bd](https://github.com/facebook/zstd/commit/7d970bd83c2323c5e78b4f15ae850373c70f055d)
- Removed the flexible array mode of Buffer Pool and CCtx Pool in ZSTDMT and changed it to external allocation, which solved the compatibility issue with the new version of ubsan. (Architecture-related: platform compatibility)
  ↳ [#3786](https://github.com/facebook/zstd/pull/3786): [e8ff7d1](https://github.com/facebook/zstd/commit/e8ff7d18ebdb7af55ad73f92c5192e74bdc85ca2), [6bb1688](https://github.com/facebook/zstd/commit/6bb1688c1a13a9368d7c1b6f992e0a0fa7c1cbba), [c87ad5b](https://github.com/facebook/zstd/commit/c87ad5bdb59c95c16871ff99d83ec3b09bd742c8)
- Add a check on the reserved field in the sequence header decoding of zstd decompression to ensure that it must be zero to prevent corrupted data from causing undefined behavior. (Architecture-related: parsing behavior)
  ↳ [#3840](https://github.com/facebook/zstd/pull/3840): [468bb17](https://github.com/facebook/zstd/commit/468bb173782115e7bd2704f3a9e82341912eebd4)
- Fixed the crash problem in the decompression module when the old version of the frame header is invalid, and fixed multiple bugs in magicless format decoding that incorrectly rejected legal frames, and added cross-format fuzz testing to verify decoding consistency. (Architecture-related: decoding behavior)
  ↳ [#3959](https://github.com/facebook/zstd/pull/3959): [f65b9e2](https://github.com/facebook/zstd/commit/f65b9e27ce0b6e4ed096126659021359d004d1ab) | [#3976](https://github.com/facebook/zstd/pull/3976): [741b87b](https://github.com/facebook/zstd/commit/741b87bbe1c7c7e7292742f3b1ed9c4055c4743c)
- Dictionaries with a literal maximum symbol value less than 255 are no longer rejected, because the Huffman encoder already has verification logic for missing symbol tables. (Architecture-related: dictionary behavior)
  ↳ [#3731](https://github.com/facebook/zstd/pull/3731): [bd02c9b](https://github.com/facebook/zstd/commit/bd02c9be6e3708c6dd53f4df1f4dc13d29441e89)
- Fixed the verification error caused by the missing CTable header information in the dictionary of Huffman duplicate tables, and unified processing by writing the header containing tableLog and maxSymbolValue for each CTable. (Architecture-related: public API)
  ↳ [#3737](https://github.com/facebook/zstd/pull/3737): [396ef5b](https://github.com/facebook/zstd/commit/396ef5b434e5e7f15773a7495f374a99a6377778)
- Optimized the macro protection conditions of ZSTD_assertValidSequence related functions and fixed Chromium build issues. (Architecture-related: build compatibility)
  ↳ [#3770](https://github.com/facebook/zstd/pull/3770): [cdceb0f](https://github.com/facebook/zstd/commit/cdceb0fce59785c841bf697e00067163106064e1)
- Support compile-time exclusion of individual compression policies, set excluded policy entries in the block compressor table to NULL, and adjust the policy selection logic in CParams to avoid using excluded block compressors, while adding NULL checks and assertions to ensure safety. (Architecture-related: Compile-time policy exclusion)
  ↳ [#3623](https://github.com/facebook/zstd/pull/3623): [81b86a2](https://github.com/facebook/zstd/commit/81b86a2024c80c1fc69bb6a76407628e063917ed), [5a75956](https://github.com/facebook/zstd/commit/5a75956001efbde704eedad755daae2816273a74), [16bbd74](https://github.com/facebook/zstd/commit/16bbd7437cf67a748ac22349a3ff974a518a3d66), [cbf3e26](https://github.com/facebook/zstd/commit/cbf3e263160e0bfc9499f55f34c3759a14c0c1cc), [b7add1d](https://github.com/facebook/zstd/commit/b7add1dd67f24124f2ebc722effb322fb77ee92b), [59c7b2a](https://github.com/facebook/zstd/commit/59c7b2a49247de8d2335e3a492135e9396ce8e84), [1b65803](https://github.com/facebook/zstd/commit/1b65803fe7f506f5551d3946dc74f9fef8b87f71)
- Refactored the ZSTD_sequenceProducer_F type from a function type to a function pointer type, and updated all related uses. (Architecture-related: public API type changes)
  ↳ [#3839](https://github.com/facebook/zstd/pull/3839): [809c7eb](https://github.com/facebook/zstd/commit/809c7eb6bff1934745b425437d2116d9c0dbe0df)
- Migrate the parameters of the external sequence generator (ESP) from the compression context to the ZSTD_CCtx_params structure, and add the auxiliary function ZSTD_hasExtSeqProd. (architecture-related: public API parameter migration)
  ↳ [#3839](https://github.com/facebook/zstd/pull/3839): [d151a48](https://github.com/facebook/zstd/commit/d151a4880bdcb15d10ed11136b8b7d8d3d66af2c)
- Replaced memcpy with ZSTD_memcpy to support redirection in Linux kernel mode. (Architecture-related: Platform compatibility: Linux kernel mode)
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [fe2e2ad](https://github.com/facebook/zstd/commit/fe2e2ad36d434d0989ca669d3a4f4d60f1cb907b)
- Optimize Huffman decoder performance, eliminate compiler checks through manual loop unrolling and masking operations, and add a new HUF_DISABLE_FAST_DECODE macro to support disabling fast decoding at compile time. (Architecture-related: build and installation methods)
  ↳ [#3826](https://github.com/facebook/zstd/pull/3826): [c7269ad](https://github.com/facebook/zstd/commit/c7269add7eaf028ed828d9af41e732cf01993aad) | [#3827](https://github.com/facebook/zstd/pull/3827): [5ab78c0](https://github.com/facebook/zstd/commit/5ab78c0418dd2b77e76e8350a563b9771a424b27)
- Modify the decoding sequence process, add new parameters to detect overflow events, eliminate the need for checksums, and enhance security. (Architecture-related: core decompression behavior)
  ↳ [#3677](https://github.com/facebook/zstd/pull/3677): [02134fa](https://github.com/facebook/zstd/commit/02134fad123a26e17bcb48edc2868b5968ed76d5)
- Stop global suppression of UBSAN pointer overflow, change to local suppression, and introduce auxiliary functions to safely handle pointer operations, fix fuzzer problems. (Architecture-related: public API macro definition)
  ↳ [#3776](https://github.com/facebook/zstd/pull/3776): [43118da](https://github.com/facebook/zstd/commit/43118da8a7fb51e660bfa7e958639c5cc8285580), [3daed70](https://github.com/facebook/zstd/commit/3daed7017af2f015dc34e88ff4ac1cac8cd7e511) | [#3947](https://github.com/facebook/zstd/pull/3947): [b20703f](https://github.com/facebook/zstd/commit/b20703f273197589c8c70dd406b81ad601fa9b4a) | [#3658](https://github.com/facebook/zstd/pull/3658): [d01a2c6](https://github.com/facebook/zstd/commit/d01a2c69296cff9bd052b797b2be1055a96cd644) | [#3738](https://github.com/facebook/zstd/pull/3738): [c27fa39](https://github.com/facebook/zstd/commit/c27fa399042f466080e79bb4fd8a4871bc0bcf28)
- Convert invalid cases with offset 0 to extremely positive numbers so that they are detected as data corruption in distance checks and no longer rely on checksums. (Architecture-related: core decompression behavior)
  ↳ [#3937](https://github.com/facebook/zstd/pull/3937): [a9fb8d4](https://github.com/facebook/zstd/commit/a9fb8d4c41bf3cc829adf20aea3768863d03cd0d)
- The format specification clearly defines the case where the offset calculation result is 0 as data corruption, and adds that the decompressor should treat it as offset 1 in this case. At the same time, add a note in the API document of ZSTD_decompressStream: After the operation returns an error, the DCtx state is undefined. Calling this function at this time is undefined behavior, and the state must be reset first. (Architecture-related: public API and format specification)
  ↳ [#3824](https://github.com/facebook/zstd/pull/3824): [f06b18b](https://github.com/facebook/zstd/commit/f06b18b3ff009ef7dc90294fca674658ddf139bf) | [#3977](https://github.com/facebook/zstd/pull/3977): [5d82c2b](https://github.com/facebook/zstd/commit/5d82c2b57c0f5f239ba712a7e6ec46c84a6ba02d)
- Added documentation for the behavior of CCtx and DCtx in an undefined state after an error, and clarified the contract of the public API. (Architecture-related: public API)
  ↳ [#3977](https://github.com/facebook/zstd/pull/3977): [902c7ec](https://github.com/facebook/zstd/commit/902c7ec1fe833f7f8d542fe94acba9e3a0a013a1)
- Added an entry in the decoder errata document stating that compressed block sizes of exactly 128KB were incorrectly rejected by older decoders, and implementers are reminded to avoid generating such blocks. (Architecture-related: format compatibility)
  ↳ [#3620](https://github.com/facebook/zstd/pull/3620): [a29b6ed](https://github.com/facebook/zstd/commit/a29b6ed2510795bb7bca93bb6fadb09cf4c0345d)
- Update the documentation comments of the ZSTD_estimate*Size() series of functions to clarify the applicable scope of memory estimation (single compression vs streaming compression), and change the parameter name of ZSTD_estimateCCtxSize to maxCompressionLevel to make its meaning clearer. (Architecture-related: public API)
  ↳ [#3755](https://github.com/facebook/zstd/pull/3755): [3fc14e4](https://github.com/facebook/zstd/commit/3fc14e411b18869e333732ceedad4f1052d73b86)
- Added multiple data corruption determination conditions in the format specification document: decoding too many Huffman weights (more than 255) is considered corrupt; no symbol weight of 1 is considered corrupt; at least two non-zero weight literals are required; the non-zero probability of invalid values in the FSE probability table causes data corruption. (Architecture-related: format specification)
  ↳ [#3813](https://github.com/facebook/zstd/pull/3813): [e61e3ff](https://github.com/facebook/zstd/commit/e61e3ff15208432cecf09ede09e8ebcf1d126bdd) | [#3814](https://github.com/facebook/zstd/pull/3814): [dc84e35](https://github.com/facebook/zstd/commit/dc84e35138338e95016fe23feb7dae43a842ca4f), [05059e5](https://github.com/facebook/zstd/commit/05059e5a48333e594e0204894cbbdffe51305487) | [#3817](https://github.com/facebook/zstd/pull/3817): [c5bf96f](https://github.com/facebook/zstd/commit/c5bf96fb74378aaefec44f30f67f88f3f70f8e4e)
- Added compile-time macro protection, allowing to exclude specific compression strategies during build; also added new build options ZSTD_LIB_EXCLUDE_COMPRESSORS_DFAST_AND_UP and ZSTD_LIB_EXCLUDE_COMPRESSORS_GREEDY_AND_UP to reduce library size. (Architecture-related: build options)
  ↳ [#3623](https://github.com/facebook/zstd/pull/3623): [50cdf84](https://github.com/facebook/zstd/commit/50cdf84f58e1d8f989877db453fdfe9d63c1925e), [6761e1c](https://github.com/facebook/zstd/commit/6761e1c949b99050f79a90a333c3432ba7cf3f22), [b12e8cb](https://github.com/facebook/zstd/commit/b12e8cb3e73c2eb0d176eb9b4dd0ff943b766242), [39b7946](https://github.com/facebook/zstd/commit/39b7946b95dc4359d7a9546ede906489682dd0d9), [bae1749](https://github.com/facebook/zstd/commit/bae174960b4abd8cefadf23f323b2c82829538e6), [d09f195](https://github.com/facebook/zstd/commit/d09f195ceb774bc0b3b7c764ddb907bc3de8c69e), [eb92279](https://github.com/facebook/zstd/commit/eb9227935ead3eff349dcdde296543ff097deae0), [5490c75](https://github.com/facebook/zstd/commit/5490c75ddaae98010985618832ab55ed7b98dbed), [cc1ffe0](https://github.com/facebook/zstd/commit/cc1ffe0bd6561128f39cc6c673aa75c91a925b68)
- Update the version number to v1.5.6. (Architecture-related: version and compatibility)
  ↳ [#3969](https://github.com/facebook/zstd/pull/3969): [686e7e4](https://github.com/facebook/zstd/commit/686e7e4b4b3821df4de0e7dd4722049ee2c5fb88)
- Fixed compilation error on Windows ARM64EC platform. (Architecture event: Linux_Kernel_Module removed)
  ↳ [#3636](https://github.com/facebook/zstd/pull/3636): [1b994cb](https://github.com/facebook/zstd/commit/1b994cbc57869cc73e6434acb639aab648fcc678)
- Fixed the problem of __cpuid built-in function when compiling Clang on Windows. (Architecture-related: platform compatibility)
  ↳ [#3957](https://github.com/facebook/zstd/pull/3957): [94c1020](https://github.com/facebook/zstd/commit/94c102038b81ed89e3b013cb1977496612609f85)

### Advanced Features
- Added ZSTD_CCtxParams_registerSequenceProducer public API to enable external sequence generators to be used with static CCtx. (Architecture event: Zstd_Core_Module module change)
  ↳ [#3854](https://github.com/facebook/zstd/pull/3854): [c6cabf9](https://github.com/facebook/zstd/commit/c6cabf94417d84ebb5da62e05d8b8a9623763585)
- Add support for QNX system in platform.h. (Architecture-related: platform compatibility)
  ↳ [#3745](https://github.com/facebook/zstd/pull/3745): [839c793](https://github.com/facebook/zstd/commit/839c7939e825d9a6a24eea4122b5cfd4ab8b5243)
- Enable utimensat support on FreeBSD, using more precise timestamp settings. (Architecture-related: platform compatibility)
  ↳ [#3960](https://github.com/facebook/zstd/pull/3960): [d6ee2d5](https://github.com/facebook/zstd/commit/d6ee2d5d2454f5023c78d59e7464c9c902d6597b)
- Fixed the null pointer dereference problem caused by unchecked memory allocation failure in ZSTD_createCDict_advanced2(). (Architecture-related: public API)
  ↳ [#3847](https://github.com/facebook/zstd/pull/3847): [9a3b17c](https://github.com/facebook/zstd/commit/9a3b17c4d61f00e22997d946f422533564812fe3)
- Changed the visibility macro of the four dictionary training functions from ZDICTLIB_API to ZDICTLIB_STATIC_API, and fixed the compiler warning caused by function prototype mismatch. (Architecture-related: public API visibility change)
  ↳ [#3733](https://github.com/facebook/zstd/pull/3733): [ecb86d8](https://github.com/facebook/zstd/commit/ecb86d82868d60517453151127b229c96ff89fec)

### Tools & Applications
- Fixed an issue where the --rm option was incorrectly disabled when mixed with -c, -o or --stdout; --rm is now only disabled when final output is to stdout. (Architecture-related: CLI behavior)
  ↳ [#3942](https://github.com/facebook/zstd/pull/3942): [c610a01](https://github.com/facebook/zstd/commit/c610a01d7dbe0e6586f94bfb5f8b540a2f28b1c5), [fbd9e62](https://github.com/facebook/zstd/commit/fbd9e628ae124d4bbf4db0b8afd54b6b6e653b29)
- Fixed the problem of failure when compiling with GCC 4.5.4 on AIX 5.1 because stdint.h could not be found, and included inttypes.h in the AIX environment instead (architecture-related: platform compatibility)
  ↳ [#3860](https://github.com/facebook/zstd/pull/3860): [66269e7](https://github.com/facebook/zstd/commit/66269e74a00e531a5f27fcb4fd65eb061d02dc5c)
- Fixed the compilation compatibility problem caused by the LLU suffix in the old version of Visual Studio, replacing the constant suffix with ULL. (Architecture-related: platform compatibility)
  ↳ [#3929](https://github.com/facebook/zstd/pull/3929): [2abe8d6](https://github.com/facebook/zstd/commit/2abe8d63e06f0e7c9adacd50855a05023e51f1e0) | [#3664](https://github.com/facebook/zstd/pull/3664): [94a2f27](https://github.com/facebook/zstd/commit/94a2f2791f313d27b6a2c0293971954cdd66035b)
- Fixed incorrect decoder behavior when the sequence number is 0, ensuring correct end of sequence segments and detection of excess bytes. (Architecture-related: decoder behavior)
  ↳ [#3669](https://github.com/facebook/zstd/pull/3669): [3732a08](https://github.com/facebook/zstd/commit/3732a08f5b82ed87a744e65daa2f11f77dabe954) | [#3674](https://github.com/facebook/zstd/pull/3674): [b462362](https://github.com/facebook/zstd/commit/b46236278a0adea097ce7792824f93a678a74069)
- Fixed the problem of repeated definition of MEM_STATIC macro in Linux kernel mode. (Architecture-related: platform compatibility)
  ↳ [#3676](https://github.com/facebook/zstd/pull/3676): [d964532](https://github.com/facebook/zstd/commit/d9645327b3b6d18b04ac1dd0bc4346a2af87bb9b)
- Fixed null pointer check bug in Win32 pthread wrapper, and added parameter non-null assertion. (Architecture-related: public API)
  ↳ [#3984](https://github.com/facebook/zstd/pull/3984): [e4aeaeb](https://github.com/facebook/zstd/commit/e4aeaebc201ba49fec50b087aeb15343c63712e5)
- The pzstd build configuration removes conditional judgment and directly uses the C++14 standard to solve portability issues. (Architecture-related: build requirements)
  ↳ [#3682](https://github.com/facebook/zstd/pull/3682): [cd4dba7](https://github.com/facebook/zstd/commit/cd4dba74dea8a92f9e33d72fcb5b60224bc4e6c3)
- Fixed the problem of missing source files when building Windows MSVC shared libraries, causing the build to fail. (Architecture-related: build and installation methods)
  ↳ [#3739](https://github.com/facebook/zstd/pull/3739): [2538732](https://github.com/facebook/zstd/commit/253873220f26c0fd43aef740751355f91f40b750)
- Improved CMake build tests to be compatible with earlier versions of CMake (<3.13), and fixed compilation issues when using CMake to build pzstd on macOS. (Architecture-related: Platform compatibility)
  ↳ [#3883](https://github.com/facebook/zstd/pull/3883): [2fc7248](https://github.com/facebook/zstd/commit/2fc7248412db6c92086369fc3243f93f397cff4c)
- Stop hardcoding the POSIX version on BSD systems and instead rely on the system's own unistd.h. (Architecture-related: platform compatibility)
  ↳ [#3952](https://github.com/facebook/zstd/pull/3952): [f99a450](https://github.com/facebook/zstd/commit/f99a450ca4d5fdb25d0d9bc5ae4c5d4787fbcb87)
- Fixed build failure due to uninitialized statbuf variable when LTO is enabled. (Architecture-related: build requirements)
  ↳ [#3695](https://github.com/facebook/zstd/pull/3695): [de6b46d](https://github.com/facebook/zstd/commit/de6b46dfc80d950a32176c7eca79bb229d47f501)
- Removed the custom type definition of intptr_t because this type is already provided in <linux/types.h> of the Linux kernel. (Architecture-related: platform compatibility)
  ↳ [#3822](https://github.com/facebook/zstd/pull/3822): [a419265](https://github.com/facebook/zstd/commit/a419265d30f4fa05caa8df0b12fac1ce2558ec6a)

### Cross-cutting / Other Architecture-related Changes
- Upgrade the xxHash library to v0.8.2, including performance optimization and SVE vectorization support, and disabling automatic vectorization of XXH64 by default to avoid performance degradation. (Architecture-related: public API)
  ↳ [#3820](https://github.com/facebook/zstd/pull/3820): [592b1ac](https://github.com/facebook/zstd/commit/592b1acb1804f18e42412607a81c636dc1d4e850) | [#3933](https://github.com/facebook/zstd/pull/3933): [007cda8](https://github.com/facebook/zstd/commit/007cda88ca1c7819eec966ce030934756d33c8c1)
- Raise the minimum version requirement of CMake from 2.8.12 to 3.5, and remove the compatibility code for versions below CMake 3.0. (Architecture-related: CMake version requirement)
  ↳ [#3807](https://github.com/facebook/zstd/pull/3807): [4502ca5](https://github.com/facebook/zstd/commit/4502ca5f422a4e3f0b8980d5a365fcc3f62e97e0), [f013b1b](https://github.com/facebook/zstd/commit/f013b1b504cc2065e8860cf90461cef9364d96b0)
- Windows build workflow adds win32 architecture support, and changes to a strategy matrix to build win32 and win64 architecture products at the same time. (Architecture-related: platform compatibility)
  ↳ [#3600](https://github.com/facebook/zstd/pull/3600): [520843d](https://github.com/facebook/zstd/commit/520843d8ffeaed2f57035b7ec3c24d2dbe2e342f), [a4fff8e](https://github.com/facebook/zstd/commit/a4fff8e0e81cb2e5ab44816b62b490cea3d4de0d)
- Added Makefile target on macOS, used to build universal binaries that support both Intel and ARM architectures. (Architecture-related: Platform compatibility)
  ↳ [#3614](https://github.com/facebook/zstd/pull/3614): [0a79416](https://github.com/facebook/zstd/commit/0a794163f4feccf2c408c206f37da5f5b0eab4de)
- Added compile module options and symbol visibility control options in CMake build to align Makefile functions. (Architecture-related: symbol visibility control)
  ↳ [#3657](https://github.com/facebook/zstd/pull/3657): [5059618](https://github.com/facebook/zstd/commit/5059618295bc67f4f70eb6f12e6cf57b8d3de141)
- Fixed the problem of assembly file compilation failure in Intel Xcode build, forcing the source file language to C only when the assembly is different from the C compiler. (Architecture-related: platform compatibility)
  ↳ [#3665](https://github.com/facebook/zstd/pull/3665): [7e09f07](https://github.com/facebook/zstd/commit/7e09f07b325b6e2a95e11776f23ff97716b7b924)
- Use the .private_extern directive to hide assembly function symbols on Apple platforms, instead of .hidden. (Architecture-related: platform compatibility)
  ↳ [#3688](https://github.com/facebook/zstd/pull/3688): [b1a30e2](https://github.com/facebook/zstd/commit/b1a30e2b4a69e6fcca9c2a6f9d4e43e8e3b243c8)
- Add a public header file include directory to the library target through the CMake BUILD_INTERFACE generator expression, so that other projects can correctly reference the zstd header file through FetchContent or ExternalProject_Add. (Architecture-related: build and installation methods)
  ↳ [#3968](https://github.com/facebook/zstd/pull/3968): [79cd0ff](https://github.com/facebook/zstd/commit/79cd0ff7120ed05ac9e52ba4c7a484752be4d758)
- Added complete installation and testing support for MSYS2 and Cygwin environments. (Architecture-related: platform compatibility)
  ↳ [#3720](https://github.com/facebook/zstd/pull/3720): [78dbba7](https://github.com/facebook/zstd/commit/78dbba76b81ea1d8713900b57bc5d5f5f43bf74b)
- Improved CMake configuration to export a unified zstd::libzstd target when only static or dynamic linking is specified. (Architecture-related: build and installation methods)
  ↳ [#3811](https://github.com/facebook/zstd/pull/3811): [c53d650](https://github.com/facebook/zstd/commit/c53d650d9a047ab12b2c7e5808878aff37d3cfc5)
- Change zstd::libzstd from an alias target to an imported interface target to dynamically select static or dynamic linking when using find_package. (Architecture-related: build and installation methods)
  ↳ [#3811](https://github.com/facebook/zstd/pull/3811): [475da4f](https://github.com/facebook/zstd/commit/475da4fb2e2aef102edecba04278b38fce44fb81)
- Fixed an issue where compilation was interrupted due to thread library lookup failure when building with CMake 3.8.2 and GCC 4.7.1 on HP-UX 11.11 PA-RISC systems. (Architecture-related: Platform compatibility)
  ↳ [#3862](https://github.com/facebook/zstd/pull/3862): [e49d1ab](https://github.com/facebook/zstd/commit/e49d1ab6aabcd662b76a46ef48391a5462357167) | [#3946](https://github.com/facebook/zstd/pull/3946): [f6039f3](https://github.com/facebook/zstd/commit/f6039f3d5fa607555fc193042671a05bf5029bad)
- Added compilation testing for SPARC64 architecture in CI workflow. (Architecture-related: Platform compatibility)
  ↳ [#3886](https://github.com/facebook/zstd/pull/3886): [e1ef81a](https://github.com/facebook/zstd/commit/e1ef81a3ae94dad4aa846615fc6e2293b28f50e8)
- Define and export the zstd::libzstd target uniformly in the CMake project to avoid repeated definitions. (Architecture-related: build and installation methods)
  ↳ [#3811](https://github.com/facebook/zstd/pull/3811): [dcd713c](https://github.com/facebook/zstd/commit/dcd713ce06fd9729e2e1eefa079be866f5e2f519)
- Added RISC-V simulation tests in GitHub CI. (Architecture-related: Platform compatibility)
  ↳ [#3934](https://github.com/facebook/zstd/pull/3934): [ad59027](https://github.com/facebook/zstd/commit/ad590275b482d4c561bdc58418ef6b6a1db80c25)
- Fix CMake build, when both shared and static libraries are enabled, the libzstd target is always created and its type is determined based on BUILD_SHARED_LIBS. (Architecture-related: build and installation methods)
  ↳ [#3965](https://github.com/facebook/zstd/pull/3965): [a0a9bc6](https://github.com/facebook/zstd/commit/a0a9bc6c95436c85002ffca972ae545f862e1638)
- Fix CMake build: Unify the management of public header files, expose only the include path of the library directory, and set the include directory to INTERFACE. (Architecture-related: public API)
  ↳ [#3968](https://github.com/facebook/zstd/pull/3968): [a595e58](https://github.com/facebook/zstd/commit/a595e5812a5c7e4ac47839383f931fb8000623f0)
- In CMake builds, when the settings of ZSTD_BUILD_SHARED and ZSTD_BUILD_STATIC conflict with BUILD_SHARED_LIBS, a warning will now be issued and the former will take precedence. (Architecture-related: build and installation methods)
  ↳ [#3975](https://github.com/facebook/zstd/pull/3975): [42b02f5](https://github.com/facebook/zstd/commit/42b02f5185393e5f71abaa4c532684de3569be85)
- Remove the third-party MSVC environment initialization action, use Meson's built-in --vsenv option instead, and replace the build command from ninja to meson compile. (Architecture-related: build and installation methods)
  ↳ [#3858](https://github.com/facebook/zstd/pull/3858): [923cf3d](https://github.com/facebook/zstd/commit/923cf3dc9289d00b668cd0a330d5c28f22d4837f)
- Update the dependency of Intel CET compatibility test and re-enable the test. (Architecture-related: platform compatibility)
  ↳ [#3893](https://github.com/facebook/zstd/pull/3893): [04a6c8c](https://github.com/facebook/zstd/commit/04a6c8cbe240495f2dcf7ab108bec327ef245813)
- Convert CircleCI workflow to GitHub Actions workflow. (Architecture-related: build and installation methods)
  ↳ [#3901](https://github.com/facebook/zstd/pull/3901): [3a64c69](https://github.com/facebook/zstd/commit/3a64c69eba2592ec1cbcbed294a84019ab47dd19)
- Unify Windows platform detection macros to only check compiler-defined _WIN32 to unify Windows detection methods. (Architecture-related: platform compatibility)
  ↳ [#3772](https://github.com/facebook/zstd/pull/3772): [585aaa0](https://github.com/facebook/zstd/commit/585aaa0ed324a858226908fc1f00d78ed92b0f4b)

### Compatibility & Legacy
- Modify the bitstream implementation to always return 0 after overflow, and introduce internal overloaded functions to enhance cross-platform behavioral consistency and improve security. (Architecture-related: public API behavior)
  ↳ [#3676](https://github.com/facebook/zstd/pull/3676): [ba50807](https://github.com/facebook/zstd/commit/ba508070299b4ab7ae1e22b659557489122cdcd7), [74c901b](https://github.com/facebook/zstd/commit/74c901bbedd4584190f0cd93d573cf7e014b76d1)

## Routine Changes

### New features
- Added a new lorem ipsum generator, the datagen tool generates lorem ipsum paragraphs by default, and optimizes the vocabulary distribution to be closer to the real text.
  ↳ [#3890](https://github.com/facebook/zstd/pull/3890): [d0b7da3](https://github.com/facebook/zstd/commit/d0b7da30e26406c7ece2bf538a70410e80b9de9f) | [#3913](https://github.com/facebook/zstd/pull/3913): [83598aa](https://github.com/facebook/zstd/commit/83598aa106ba0edaa8b449b2fe5d63773eeebc4e), [1e046ce](https://github.com/facebook/zstd/commit/1e046ce7fa6ebabb48a182009df6e4fe90fa2740), [40874d4](https://github.com/facebook/zstd/commit/40874d4aea44bc9e1efd2ce14b98ea19d1d2e42d), [3dbd861](https://github.com/facebook/zstd/commit/3dbd861b7dc05bc4291f9de222e397e50fb4c32b), [7003c99](https://github.com/facebook/zstd/commit/7003c9905e0c80aafe00ef485e586f859707c04c), [1e240af](https://github.com/facebook/zstd/commit/1e240af30a1d11ae45745c6c3e96307bad3771fd), [5a1bb4a](https://github.com/facebook/zstd/commit/5a1bb4a4e0aaba722e57cdca46486bc3c6d7e457)
- Internal benchmark supports generating lorem ipsum samples, and allows sample size to be selected via the -B# parameter.
  ↳ [#3913](https://github.com/facebook/zstd/pull/3913): [7a225c0](https://github.com/facebook/zstd/commit/7a225c0c465149f1a72811dab669985b6ea5e5f4)
- Added more common compressed file extensions to --exclude-compressed option.
  ↳ [#3951](https://github.com/facebook/zstd/pull/3951): [5a66afa](https://github.com/facebook/zstd/commit/5a66afa0514d0853b0f2a6b5ff3df1ae706f4862)

### bug fixes
- Added formatString_u function, replaced snprintf call, fixed -Wconversion and -Wdocumentation warnings in Clang build, and compatible with C89 standard.
  ↳ [#3913](https://github.com/facebook/zstd/pull/3913): [e62e15d](https://github.com/facebook/zstd/commit/e62e15df190ebb41b0b9f1453b2a4e9bd6e05f51), [588dfbc](https://github.com/facebook/zstd/commit/588dfbcc97657f1d70e711f3e22d8f992e14ae28)
- Fixed the problem of adding null pointers during null output and avoiding null pointer operations by returning early.
  ↳ [#3827](https://github.com/facebook/zstd/pull/3827): [dd4de1d](https://github.com/facebook/zstd/commit/dd4de1dd7a78ccff933025cf1de08a75d310802b)
- Improve CLI parameter parsing error prompts, display the specific parameters that caused the error, and rename related functions to comply with naming conventions.
  ↳ [#3850](https://github.com/facebook/zstd/pull/3850): [8052cd0](https://github.com/facebook/zstd/commit/8052cd0131a4f483ef14be3e564530c07ea382f5)
- Optimize the type safety of thread pool memory copy, and fix the type conversion problem of job count calculation in asynchronous IO reading.
  ↳ [#3865](https://github.com/facebook/zstd/pull/3865): [e6f4b46](https://github.com/facebook/zstd/commit/e6f4b464938008c4f800a26027248a00db5c81c8)
- Fixed a wrong assertion in the compression optimization code.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [e5af24c](https://github.com/facebook/zstd/commit/e5af24c5fa82186d61ee1ed4dfe161d65a1c1a7d)
- Fix assertion errors and uniformly manage the size of the optimal parser table by introducing the ZSTD_OPT_SIZE macro.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [5474edb](https://github.com/facebook/zstd/commit/5474edbe6016175453d09eca139566baefe0b97b)
- Fix memory sanitizer (msan) warning, initialize uninitialized fields in optimal parser and adjust conditional judgment.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [6c35fb2](https://github.com/facebook/zstd/commit/6c35fb2e8cb826b70226856cd7442861037cca8a)
- Fixed the issue of assertion failure caused by insufficient backward search space, and added an extra space to avoid triggering assertions.
  ↳ [#3900](https://github.com/facebook/zstd/pull/3900): [22574d8](https://github.com/facebook/zstd/commit/22574d848df09616d07fe26b363700525cb9cce9)
- Fixed an out-of-bounds read issue found in fuzz testing.
  ↳ [#3902](https://github.com/facebook/zstd/pull/3902): [b0e8580](https://github.com/facebook/zstd/commit/b0e8580dc7f71881361f3a6fe46841af9d70bedf)
- Fixed the boundary condition problem of sub-block division when processing incompressible data blocks, and optimized the performance of the target block size parameter.
  ↳ [#3915](https://github.com/facebook/zstd/pull/3915): [6b11fc4](https://github.com/facebook/zstd/commit/6b11fc436c3001cb9beb07627e7b434aab97b4b1)
- Fixed a pointer arithmetic problem that may occur when processing long sequences exceeding 64KB.
  ↳ [#3915](https://github.com/facebook/zstd/pull/3915): [3b40100](https://github.com/facebook/zstd/commit/3b401000580a3e605694055834dcd254fa36202e)
- Fixed the problem that some sub-blocks were not compressed in the target compression block size mode, and optimized the related processing logic.
  ↳ [#3915](https://github.com/facebook/zstd/pull/3915): [4b51526](https://github.com/facebook/zstd/commit/4b5152641239c571ae6cd67ae74cc87776e21362) | [#3917](https://github.com/facebook/zstd/pull/3917): [aa8592c](https://github.com/facebook/zstd/commit/aa8592c532e1a2b30b08763140b9bd66bdce4f83)
- Fixed the problem of insufficient filling of the seed queue when AsyncIO reads, ensuring that the loop continues to enqueue until the number of available tasks reaches zero.
  ↳ [#3940](https://github.com/facebook/zstd/pull/3940): [edab9ee](https://github.com/facebook/zstd/commit/edab9eed66f02c7c3c8be849f22f20ffbd04976b)
- Fix a rare edge case in the education decoder: FSE uses less than 1 bit to represent the dominant symbol.
  ↳ [#3659](https://github.com/facebook/zstd/pull/3659): [5108c9a](https://github.com/facebook/zstd/commit/5108c9ac975b5e4ff62418584cc6c8934d747b38)
- Fix header file inclusion order to ensure platform.h is included before system header files.
  ↳ [#3913](https://github.com/facebook/zstd/pull/3913): [7170f51](https://github.com/facebook/zstd/commit/7170f51dd277d4aa4a675ffdd5593af362abe83c)
- Fixed compilation warnings caused by being too cautious in pointer type conversion in the DEBUGLOG macro.
  ↳ [#3915](https://github.com/facebook/zstd/pull/3915): [0591e7e](https://github.com/facebook/zstd/commit/0591e7eea118eccb6b8ceef00296bedaad3d7e9e)
- Fixed bug with incorrect debug log level.
  ↳ [#3936](https://github.com/facebook/zstd/pull/3936): [aed172a](https://github.com/facebook/zstd/commit/aed172a8fe84caccc86e5f27999a309d1df47c00)
- Add handling of malloc failure in AIO_ReadPool_create, and throw an exception when memory allocation fails.
  ↳ [#3704](https://github.com/facebook/zstd/pull/3704): [4d267f3](https://github.com/facebook/zstd/commit/4d267f3d4f9f85eecf98d1a2353408b8e840f1a3)
- File names are no longer truncated in verbose mode, and the problem of incomplete file name display is fixed.
  ↳ [#3956](https://github.com/facebook/zstd/pull/3956): [83ec3d0](https://github.com/facebook/zstd/commit/83ec3d0164887904a7ae7f3382051ed20d5792b2)
- Suppress error message produced by ZSTD_referenceExternalSequences when nbSeq is zero in LDM mode, and remove unused error checking.
  ↳ [#3686](https://github.com/facebook/zstd/pull/3686): [c6a888c](https://github.com/facebook/zstd/commit/c6a888c073a0a6693026e67e8db3813ba6b78850)
- Fixed static analyzer false positives, adjusted code structure to make it more explicit to the analyzer.
  ↳ [#3917](https://github.com/facebook/zstd/pull/3917): [1fafd0c](https://github.com/facebook/zstd/commit/1fafd0c4ae56a524a92369c065d616a447a21a0f)

### Refactoring optimization
- Remove old variants in splitLitBuffer decoding path, simplify decoding loop and update related function signatures.
  ↳ [#3677](https://github.com/facebook/zstd/pull/3677): [84e898a](https://github.com/facebook/zstd/commit/84e898a76c50aa31bd05b37a370c674250706254), [33fca19](https://github.com/facebook/zstd/commit/33fca19dd4b8cc9d68feb3daa129297b31680e47)
- Refactor the access method of flexible array members in the FSE decompression workspace to obtain the dtable through pointer offset calculation, and add several type conversions and assertions to alleviate UBSan warnings.
  ↳ [#3789](https://github.com/facebook/zstd/pull/3789): [d988e00](https://github.com/facebook/zstd/commit/d988e00a7fe551785bc8c3de8cd5e4266280ce6d)
- Refactor the optimal parser, changing the internal storage from sequence to stretch to support chaining predecessor solutions, and adjusting memory allocation and conditional compilation accordingly.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [4683667](https://github.com/facebook/zstd/commit/4683667785c6248a20eba83dd192dc9baea70d84)
- Reorder lazy compression strategy declarations and streamline conditional compilation macros.
  ↳ [#3623](https://github.com/facebook/zstd/pull/3623): [f242f5b](https://github.com/facebook/zstd/commit/f242f5be8f0d57fb9b49f22f35032953072471cc)
- The unified macro is defined in the form of do { } while (0) and appended with the trailing semicolon.
  ↳ [#3831](https://github.com/facebook/zstd/pull/3831): [8193250](https://github.com/facebook/zstd/commit/8193250615f56ace446a3bf963d195f9f33fa9a9)
- Remove redundant assignments and unused code in the optimal parser to simplify structure copy logic.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [8168a45](https://github.com/facebook/zstd/commit/8168a451e58261baf9a53b0c1bcfdaff2ba0480d)
- Moved two helper functions up in the source file.
  ↳ [#3725](https://github.com/facebook/zstd/pull/3725): [5f5bdc1](https://github.com/facebook/zstd/commit/5f5bdc1e5d23544391df1c47cec3a69b96a09f5b)
- Move variable declarations in multiple functions to smaller scopes to improve code readability and prevent misuse.
  ↳ [#3903](https://github.com/facebook/zstd/pull/3903): [b921f1a](https://github.com/facebook/zstd/commit/b921f1aad67cfc347ea7f8ef1c0afb6688bad4b6)
- Refactor the loop condition and add assertions to ensure that the number of sub-blocks is greater than zero to make the code intent clearer.
  ↳ [#3917](https://github.com/facebook/zstd/pull/3917): [d23b95d](https://github.com/facebook/zstd/commit/d23b95d21d5cb9c5378b3537271dbbff7cdb49b7)
- Reduce the header file inclusion in cover.h, and adjust the coding style and bounds checking of related functions in cover.c.
  ↳ [#3962](https://github.com/facebook/zstd/pull/3962): [c8ab027](https://github.com/facebook/zstd/commit/c8ab027227536a543efd1b7bea04aabf9e97accf)

### Test related
- Add .gitignore rules in the test directory to ensure that .zst files are not ignored by Git. These files are used to decompress error tests and decompress golden files for tests.
  ↳ [#3954](https://github.com/facebook/zstd/pull/3954): [b39c767](https://github.com/facebook/zstd/commit/b39c76765b761c9c3c3c23db3ed55f3f825f7e4d), [0ae98ba](https://github.com/facebook/zstd/commit/0ae98ba2155154dfdea253fef5876ec23fa26a86)
- Fixed the dstSize_tooSmall problem in fuzzer caused by incorrect decompression margin calculation.
  ↳ [#3612](https://github.com/facebook/zstd/pull/3612): [e72e13a](https://github.com/facebook/zstd/commit/e72e13ac6c1dc373a0826df0de6f9bf13ee02ee4)
- Add benchmark option for ZSTD_decompressDCtx() in fullbench.
  ↳ [#3726](https://github.com/facebook/zstd/pull/3726): [a07d7c4](https://github.com/facebook/zstd/commit/a07d7c4e29f9329a1c98fbecc2e54ed6b663caef)
- Disable Intel CET compatibility testing which is not available due to external dependencies.
  ↳ [#3884](https://github.com/facebook/zstd/pull/3884): [c7611d6](https://github.com/facebook/zstd/commit/c7611d6964d7012c24850c3a2cd3092f50f9d6ba)
- Partially fixed regression testing.
  ↳ [#3915](https://github.com/facebook/zstd/pull/3915): [6719794](https://github.com/facebook/zstd/commit/6719794379ada9cc33cae486a6fea4930eda481c)
- Enable -Werror when building fuzzer and fix declaration-after-statement warning.
  ↳ [#3979](https://github.com/facebook/zstd/pull/3979): [3487a60](https://github.com/facebook/zstd/commit/3487a60950ea01e89883a3e807a18a6e155768b7)
- Fix variable type error in simple_decompress.c and add macro definitions required for experimental API.
  ↳ [#3978](https://github.com/facebook/zstd/pull/3978): [6a0052a](https://github.com/facebook/zstd/commit/6a0052a409e2604bd40354b76b86272b712edd7d)
- Fix pointer arithmetic warning in fuzzers, change variable type from void* to uint8_t*.
  ↳ [#3983](https://github.com/facebook/zstd/pull/3983): [dc1f7b5](https://github.com/facebook/zstd/commit/dc1f7b560b23f5bd50a0fcddd677007c9c76ec0b)

### Performance optimization
- Optimize the compression ratio of integer arrays in high compression mode: adjust the price calculation logic in the optimal parser to improve compression performance in specific scenarios while avoiding negative impacts on other data.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [de10f56](https://github.com/facebook/zstd/commit/de10f56be2765e8375939b97bb27ad3e378f217f), [d31018e](https://github.com/facebook/zstd/commit/d31018e223691256aac9c426fcfbeec735a2d6ab)
- In the btultra2 block compressor, optimize the literal update logic at position pos+1 to achieve better compression results when litlen==1.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [0166b2b](https://github.com/facebook/zstd/commit/0166b2ba8083481df3ae68e3431a43f541d3c9bd)
- Optimize the superblock processing performance of the compression engine: improve the sequence encoding format, optimize the target compression block size parameter, exit incompressible data early, and improve the sub-block boundary judgment logic.
  ↳ [#3668](https://github.com/facebook/zstd/pull/3668): [1f83b7c](https://github.com/facebook/zstd/commit/1f83b7cfc459c2dbef00dc6276f790370e17aef6) | [#3915](https://github.com/facebook/zstd/pull/3915): [cc45309](https://github.com/facebook/zstd/commit/cc4530924b42c5d138f871c33726d374e2778ad3), [f837219](https://github.com/facebook/zstd/commit/f8372191f595f112ba13445205cf46997da67350) | [#3917](https://github.com/facebook/zstd/pull/3917): [86db607](https://github.com/facebook/zstd/commit/86db60752d1f813642054d12d704663c7757d434), [8d31e8e](https://github.com/facebook/zstd/commit/8d31e8ec42a736bf7cc70f9f21e9c1afc920c148)

### Security related
- Removed unsafe sprintf calls in zstdcli.c, switched to safe initialization, and adjusted the error prompt format.
  ↳ [#3916](https://github.com/facebook/zstd/pull/3916): [4d2bf7f](https://github.com/facebook/zstd/commit/4d2bf7f0f2feb2c6928204db218ff9384ac605ac)
- Added and improved security vulnerability reporting and notification guidelines.
  ↳ [#3909](https://github.com/facebook/zstd/pull/3909): [b6805c5](https://github.com/facebook/zstd/commit/b6805c54d67f902d32afecc5ca153cd81a77764f), [e13d099](https://github.com/facebook/zstd/commit/e13d099bf881d69d6cf8bcd5cd4f677e1ce86bea)

### Documentation
- Update the streaming_compression example to check if the library supports multi-threaded compression when requesting it. If not, display a warning and fall back to single-threaded mode.
  ↳ [#3631](https://github.com/facebook/zstd/pull/3631): [6ec18ae](https://github.com/facebook/zstd/commit/6ec18aed31a955ce7ce04403538f7539cd57eb56)
- Maintain documentation comments in zstd_decompress.c, remove duplicate instructions, update API documentation and adjust header file inclusion order.
  ↳ [#3967](https://github.com/facebook/zstd/pull/3967): [559762d](https://github.com/facebook/zstd/commit/559762da12f54712d44f619098aa4a7e7bc5727b) | [#3915](https://github.com/facebook/zstd/pull/3915): [f77f634](https://github.com/facebook/zstd/commit/f77f634d41149c3e5754ebfe4d5cf3a5f138c843)
- Add instructions for using the Bazel module in README.md.
  ↳ [#3812](https://github.com/facebook/zstd/pull/3812): [98d8ad2](https://github.com/facebook/zstd/commit/98d8ad27a2b2a2fc75e0594bae992824c470f61c)
- Made multiple updates to the man page, clarifying descriptions of conflicts between -o and -c options, improving descriptions of compression levels, environment variables, advanced options and benchmarks.
  ↳ [#3942](https://github.com/facebook/zstd/pull/3942): [1362699](https://github.com/facebook/zstd/commit/1362699e875994689390bbee3cba87d2c11a11fb) | [#3958](https://github.com/facebook/zstd/pull/3958): [5473b72](https://github.com/facebook/zstd/commit/5473b72a05ad03555fed8774f7e5af5e99e27e47)
- Updated CHANGELOG file to record changelog entries for v1.5.6 version and fix formatting issues.
  ↳ [#3969](https://github.com/facebook/zstd/pull/3969): [351498b](https://github.com/facebook/zstd/commit/351498b9320e9c03cbe4ed722e8967a5673f46a0)
- Added guidelines for adding new fuzz testing tools to the fuzz testing README document.
  ↳ [#3982](https://github.com/facebook/zstd/pull/3982): [f62b266](https://github.com/facebook/zstd/commit/f62b2663b96d440d3b9dd50b40dc911f9e0083d3)

### Build/CI
- Upgraded GitHub CodeQL Action from 2.2.11 to 3.24.6, and simultaneously upgraded upload-artifact and other related actions.
  ↳ [#3629](https://github.com/facebook/zstd/pull/3629): [be489f7](https://github.com/facebook/zstd/commit/be489f78df642cf8fd40fcfa59ec700cb494a1b5) | [#3587](https://github.com/facebook/zstd/pull/3587): [68a4a03](https://github.com/facebook/zstd/commit/68a4a034531df5bf2b895a2ca76c1bf629ee3415) | [#3606](https://github.com/facebook/zstd/pull/3606): [dc88f7b](https://github.com/facebook/zstd/commit/dc88f7b8a0c154a555c3af997e18ec174cf2d3e6) | [#3634](https://github.com/facebook/zstd/pull/3634): [2a5076d](https://github.com/facebook/zstd/commit/2a5076d26481fddb22f1e589c1d1666b0a7456d6) | [#3697](https://github.com/facebook/zstd/pull/3697): [065ea92](https://github.com/facebook/zstd/commit/065ea9274fbbf794616df86a6376cd1c7f0dd5ca) | [#3730](https://github.com/facebook/zstd/pull/3730): [db0ae65](https://github.com/facebook/zstd/commit/db0ae65436c6aa977b60b8a7fd7d4522a3cd14ae) | [#3863](https://github.com/facebook/zstd/pull/3863): [3a2e302](https://github.com/facebook/zstd/commit/3a2e302b2ca25eadca7d1952119837be70b2b8b2) | [#3880](https://github.com/facebook/zstd/pull/3880): [ee2efb6](https://github.com/facebook/zstd/commit/ee2efb634eab104a2ec18ab6b2ce277bc159cbd0) | [#3887](https://github.com/facebook/zstd/pull/3887): [163e9b6](https://github.com/facebook/zstd/commit/163e9b66377126e1b498c40628660d59aababf9f) | [#3905](https://github.com/facebook/zstd/pull/3905): [927d079](https://github.com/facebook/zstd/commit/927d0799442c42ece088dcf339ca25968274f5a0) | [#3918](https://github.com/facebook/zstd/pull/3918): [a412bed](https://github.com/facebook/zstd/commit/a412bedb3f63a5bbb88601c0ab085a8eb0c39e48) | [#3927](https://github.com/facebook/zstd/pull/3927): [70df177](https://github.com/facebook/zstd/commit/70df177615ea99eeea5a7704a823b32bb302e6a6)
- Modify the default target name in programs/Makefile to avoid conflicts with targets in the lib/ directory.
  ↳ [#3753](https://github.com/facebook/zstd/pull/3753): [4edfaa9](https://github.com/facebook/zstd/commit/4edfaa93b7631e5fcb2911869ab77c833d73d142)
- Simplified dependency generation rules, and fixed the exclusion logic and testing of libzstd-nomt.
  ↳ [#3753](https://github.com/facebook/zstd/pull/3753): [607933a](https://github.com/facebook/zstd/commit/607933a2ff41f985ec9f05f2a0fc3b5b74f52b48)
- Fixed the installation path logic of DESTDIR and BINDIR in pzstd Makefile so that they can be set separately.
  ↳ [#3752](https://github.com/facebook/zstd/pull/3752): [d55ebb5](https://github.com/facebook/zstd/commit/d55ebb5718a1c7eaff65a720932aa628ccf4f66e)
- Switched the CI running environment of x32 test from ubuntu-latest to ubuntu-20.04 to solve the compatibility issue, and fixed the sanitizer task to ubuntu-20.04.
  ↳ [#3777](https://github.com/facebook/zstd/pull/3777): [2c17e05](https://github.com/facebook/zstd/commit/2c17e0564689060d14dfc522497787364bc8f0e4) | [#3945](https://github.com/facebook/zstd/pull/3945): [ee6acaf](https://github.com/facebook/zstd/commit/ee6acaf26bbf842837513087c91776b83d4d9560)
- Fixed datagen missing lorem related source files in Meson and CMake builds.
  ↳ [#3913](https://github.com/facebook/zstd/pull/3913): [c2d3570](https://github.com/facebook/zstd/commit/c2d357033838c01c827fc10f0b2b850df339776a), [b34517a](https://github.com/facebook/zstd/commit/b34517a4402603e8210c24ceb7b976a360ef978b) | [#3890](https://github.com/facebook/zstd/pull/3890): [befcec1](https://github.com/facebook/zstd/commit/befcec17886479a22028b1d0b632fa15e31d5abc), [fd03971](https://github.com/facebook/zstd/commit/fd03971252d043bb9d3e065dc2361db6d40c87b6)
- Enabled ZSTD_LEGACY_SUPPORT=5 in test builds, and fixed compilation errors caused by static alias rules in legacy code.
  ↳ [#3943](https://github.com/facebook/zstd/pull/3943): [e087280](https://github.com/facebook/zstd/commit/e0872806df5c255d23c9c9ec95fb7db50127a9e6) | [#3955](https://github.com/facebook/zstd/pull/3955): [92fbd42](https://github.com/facebook/zstd/commit/92fbd42894e4dd9d58d3184923b17dda94ca6b44)
- Upgraded actions/checkout from v3.5.0 to v4.1.1.
  ↳ [#3619](https://github.com/facebook/zstd/pull/3619): [803e65f](https://github.com/facebook/zstd/commit/803e65f935d0e0faefb268341aa67124336bdb58) | [#3671](https://github.com/facebook/zstd/pull/3671): [6579f6c](https://github.com/facebook/zstd/commit/6579f6c452cfb4bc87f2b25c98adc1a2dda7b87b) | [#3749](https://github.com/facebook/zstd/pull/3749): [e0e309f](https://github.com/facebook/zstd/commit/e0e309f27cf73f407f77cfce485203636678a46a) | [#3774](https://github.com/facebook/zstd/pull/3774): [d5cbae7](https://github.com/facebook/zstd/commit/d5cbae7c50835b84114efd3c80ff8bbe99080fe8) | [#3800](https://github.com/facebook/zstd/pull/3800): [af971ce](https://github.com/facebook/zstd/commit/af971cec6572e156e26bc403cb42396e7d908ba1)
- Upgraded actions/upload-artifact from v3.1.2 to v4.1.0.
  ↳ [#3750](https://github.com/facebook/zstd/pull/3750): [d8b25cb](https://github.com/facebook/zstd/commit/d8b25cbf689092b175b3874b964e958218ff501a) | [#3849](https://github.com/facebook/zstd/pull/3849): [e515327](https://github.com/facebook/zstd/commit/e515327764889938692dac3257a300df56a15e8f) | [#3864](https://github.com/facebook/zstd/pull/3864): [e2fe266](https://github.com/facebook/zstd/commit/e2fe26627907274f04b9ad7dabf41a3243547a1d)
- Upgraded ossf/scorecard-action from v2.1.2 to v2.3.1.
  ↳ [#3588](https://github.com/facebook/zstd/pull/3588): [da41d1d](https://github.com/facebook/zstd/commit/da41d1d401fade89b868ec5306b2805460bcd909) | [#3804](https://github.com/facebook/zstd/pull/3804): [9446b19](https://github.com/facebook/zstd/commit/9446b1910cab25dd2eb93d76ca5e6168a6e70a51)
- Upgraded microsoft/setup-msbuild to v2.0.0.
  ↳ [#3888](https://github.com/facebook/zstd/pull/3888): [c485b57](https://github.com/facebook/zstd/commit/c485b57bc73abfda9085650b4caaf013248e42dc) | [#3897](https://github.com/facebook/zstd/pull/3897): [0d9fb5d](https://github.com/facebook/zstd/commit/0d9fb5dc3394161097dc54642bd793e6de3f7593), [9fed5ef](https://github.com/facebook/zstd/commit/9fed5ef108d63ff25964574c2ec980e578b1adbc)
- Upgraded cygwin/cygwin-install-action from v3 to v4.
  ↳ [#3607](https://github.com/facebook/zstd/pull/3607): [d9582a0](https://github.com/facebook/zstd/commit/d9582a0cb8070c78e8a53fba56b94a41936914aa)
- Update msys2/setup-msys2 to v2.22.0 to resolve deprecation warning for Node.js 16.
  ↳ [#3914](https://github.com/facebook/zstd/pull/3914): [0a68be8](https://github.com/facebook/zstd/commit/0a68be83e7cb84c8212f666b4b4aa6e0dc8477cc)
- Added CI tests for build configurations that exclude matching finders.
  ↳ [#3623](https://github.com/facebook/zstd/pull/3623): [698af84](https://github.com/facebook/zstd/commit/698af84fcf8bdcfa3db4936a88e84c354331a84a)
- Fixed the paramgrill Makefile recipe and added missing dependency files.
  ↳ [#3890](https://github.com/facebook/zstd/pull/3890): [a261375](https://github.com/facebook/zstd/commit/a261375996c2301267ef6b00643e6efe92043d8a)
- Upgraded the versions of actions/checkout, actions/cache, CodeQL Action and scorecard-action in the GitHub Actions workflow.
  ↳ [#3926](https://github.com/facebook/zstd/pull/3926): [bb4f85d](https://github.com/facebook/zstd/commit/bb4f85db42925a1dd129e733d3413316ebd5c9bb) | [#3972](https://github.com/facebook/zstd/pull/3972): [88301b5](https://github.com/facebook/zstd/commit/88301b58c1b2f84e55f27fd7259db4f8afdafc22) | [#3973](https://github.com/facebook/zstd/pull/3973): [9dca060](https://github.com/facebook/zstd/commit/9dca0602f45e925c919ac130c9c9f37d88d4ab98) | [#3689](https://github.com/facebook/zstd/pull/3689): [1a6278c](https://github.com/facebook/zstd/commit/1a6278c82d3b35cd8abd82db7bc5dc0907b838dd) | [#3690](https://github.com/facebook/zstd/pull/3690): [2c97f5d](https://github.com/facebook/zstd/commit/2c97f5dbedb0b581c733eb658665a9cc886eccef)
- Added read-only permissions to GitHub Actions workflows to eliminate Scorecard security warnings.
  ↳ [#3985](https://github.com/facebook/zstd/pull/3985): [273d127](https://github.com/facebook/zstd/commit/273d1279cab66ac9bccc862da17e35ee547d7610)
- Enabled CMake building and running tests in Windows CI, and fixed CMake test commands.
  ↳ [#3957](https://github.com/facebook/zstd/pull/3957): [c1e9953](https://github.com/facebook/zstd/commit/c1e995321e9d66a648818f7995999c4fe6d77878)
- Added BTI and PAC support for ARM64 assembly files, and configured QEMU tests.
  ↳ [#3961](https://github.com/facebook/zstd/pull/3961): [ff0afba](https://github.com/facebook/zstd/commit/ff0afbad58611d22b8b4477e9383b9b9ffdbaee6)
- Added header file protection macros to lib/libzstd.mk to prevent repeated inclusion.
  ↳ [#3753](https://github.com/facebook/zstd/pull/3753): [b69d06a](https://github.com/facebook/zstd/commit/b69d06a8102f0e04cde0bda2e34984099a0dfba4)
- Renamed STATLIB variable in Makefile to STATICLIB and added default build target.
  ↳ [#3753](https://github.com/facebook/zstd/pull/3753): [feaa8ac](https://github.com/facebook/zstd/commit/feaa8ac50d4e0299f652a436e72cc64f9b504c38)
- Defined LIB_SRCDIR and LIB_BINDIR variables in Makefile, and updated related path references.
  ↳ [#3753](https://github.com/facebook/zstd/pull/3753): [f4dbfce](https://github.com/facebook/zstd/commit/f4dbfce79cb2b82fb496fcd2518ecd3315051b7d)
- Allows controlling the debugging level of fuzz testing via the DEBUGLEVEL variable in the Makefile.
  ↳ [#3902](https://github.com/facebook/zstd/pull/3902): [695d154](https://github.com/facebook/zstd/commit/695d154cac251c4ae2e2a438af21f0455a4c4149)
- Updated CMake build documentation, adding instructions for FetchContent integration, and instructions for using target_include_directories on Windows and macOS platforms.
  ↳ [#3795](https://github.com/facebook/zstd/pull/3795): [e590c8a](https://github.com/facebook/zstd/commit/e590c8a0e3b2ecdde5f63d385fa7f9bd759721d3), [3c3845b](https://github.com/facebook/zstd/commit/3c3845b9d88dacbd41cc544abcd3a5f58a120749)
- In Linux kernel builds, the g_debuglevel variable is no longer defined when DEBUGLEVEL is less than 2 to avoid compilation errors caused by empty translation units.
  ↳ [#3822](https://github.com/facebook/zstd/pull/3822): [e122fcb](https://github.com/facebook/zstd/commit/e122fcbf58e142e837a2bba382ef7ca4f5eaa13b)

### Maintenance
- Added [no-] prefix to mmap-dict help output, and completed missing newlines.
  ↳ [#3601](https://github.com/facebook/zstd/pull/3601): [c28031d](https://github.com/facebook/zstd/commit/c28031df8f1809621407b5bc9c4b3e052872409f)
- Standardize create_dictionary function declaration, add void parameter.
  ↳ [#3620](https://github.com/facebook/zstd/pull/3620): [0d6954b](https://github.com/facebook/zstd/commit/0d6954b4cc309b430dd010dbeb20b112e7092644)
- Fixed the copyright linter problem and updated the copyright statement format in the xxhash library source file.
  ↳ [#3820](https://github.com/facebook/zstd/pull/3820): [3fd5f9f](https://github.com/facebook/zstd/commit/3fd5f9f52dff5e4e8a9afcf9afb1abc946844535)
- Updated comments in zstd optimal parser code to improve readability.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [b88c593](https://github.com/facebook/zstd/commit/b88c593d8ff79b96390308380604f232802e0f04)
- Removed no longer used Travis CI and AppVeyor continuous integration scripts.
  ↳ [#3621](https://github.com/facebook/zstd/pull/3621): [05434fe](https://github.com/facebook/zstd/commit/05434fe9a5d0d55650596e43171efcf1208c5c84)
- Fix unused variable warning and poisoned memory issues in MSAN configuration.
  ↳ [#3624](https://github.com/facebook/zstd/pull/3624): [4c25ea3](https://github.com/facebook/zstd/commit/4c25ea329b851e1d2e45c2a91e0d5d79a3ad3be0) | [#3725](https://github.com/facebook/zstd/pull/3725): [9987d2f](https://github.com/facebook/zstd/commit/9987d2f5942a7701b388eec4307be71a121e5652)
- Replaced deprecated ZSTD_resetDStream() with ZSTD_DCtx_reset() in the Linux kernel module.
  ↳ [#3822](https://github.com/facebook/zstd/pull/3822): [c2d4705](https://github.com/facebook/zstd/commit/c2d470581eaee3dc9f747dbab16d1fc0816f94aa)
- Convert function definitions in zlibWrapper from K&R style to C89/ANSI C style to be compatible with Clang 16.
  ↳ [#3846](https://github.com/facebook/zstd/pull/3846): [2ce0290](https://github.com/facebook/zstd/commit/2ce0290e4d745846f03956be238596929de88768)
- Remove debug trace control code.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [0ae21d8](https://github.com/facebook/zstd/commit/0ae21d8c3170741e4005c877d3c300a6034601ec)
- Add debug logs in the ZSTD_rawLiteralsCost function to assist in diagnosing dictionary stream round-trip fuzzing issues.
  ↳ [#3895](https://github.com/facebook/zstd/pull/3895): [641749f](https://github.com/facebook/zstd/commit/641749fc0935b6905b2fcfaa362cedfc631f5960)
- Reduce the level of some logs in patch mode.
  ↳ [#3899](https://github.com/facebook/zstd/pull/3899): [1f87c88](https://github.com/facebook/zstd/commit/1f87c88ecf3814ef59fa514dd7fe3522d2d400b1)
- Debug logs will now include line numbers in the output, making it easier to locate problems.
  ↳ [#3966](https://github.com/facebook/zstd/pull/3966): [9cc3304](https://github.com/facebook/zstd/commit/9cc3304614f9ea28a870f9e94e1e449c6d7de1fc)
- Optimized capacity check in end-of-frame check, reducing target capacity from 4 bytes to 3 bytes.
  ↳ [#3700](https://github.com/facebook/zstd/pull/3700): [55ff3e4](https://github.com/facebook/zstd/commit/55ff3e4e17ea42a7c3726e51945c483a18d8c4c8)

### Others
- Explicitly convert parameter types in FSE encoded functions to avoid static analyzer false positives.
  ↳ [#3789](https://github.com/facebook/zstd/pull/3789): [24dabde](https://github.com/facebook/zstd/commit/24dabde507c8d141e282e568be21e648987a7d77)
- Removed logic in the --output-dir-mirror option that incorrectly excluded hidden files and folders.
  ↳ [#3963](https://github.com/facebook/zstd/pull/3963): [86b8e39](https://github.com/facebook/zstd/commit/86b8e39a84d15ebcae3fa4b36240db27f2ae74ac)
- Added definition of log2sup function in documentation.
  ↳ [#3806](https://github.com/facebook/zstd/pull/3806): [324cce4](https://github.com/facebook/zstd/commit/324cce4996d24af7b2cd86cf5eb1b9bd80de0a47)
- Removed an extra semicolon in the source file.
  ↳ [#3917](https://github.com/facebook/zstd/pull/3917): [e0412c2](https://github.com/facebook/zstd/commit/e0412c20625c7358d506c969a9c9861b70eb10ee)
- Fixed false positives from static analysis tools regarding sequence initialization.
  ↳ [#3677](https://github.com/facebook/zstd/pull/3677): [c123e69](https://github.com/facebook/zstd/commit/c123e69ad087cea5b779ce2a26b0845810783d12)
- Fixed a typo in CONTRIBUTING.md.
  ↳ [#3701](https://github.com/facebook/zstd/pull/3701): [a1b9a5a](https://github.com/facebook/zstd/commit/a1b9a5ad0e1a10bea2315132bef21de3ed9cebc7)
- Corrected the description of dual license in README.
  ↳ [#3718](https://github.com/facebook/zstd/pull/3718): [969e54f](https://github.com/facebook/zstd/commit/969e54f26ee5e03677d47b6449be02fe48e6d349)
- Fixed typo in CMake option description.
  ↳ [#3728](https://github.com/facebook/zstd/pull/3728): [a02d81f](https://github.com/facebook/zstd/commit/a02d81f944c24aca2ccca2f16a6a96474f97e18b)
- Fixed formatting errors in lib/README.md.
  ↳ [#3763](https://github.com/facebook/zstd/pull/3763): [48b5a7b](https://github.com/facebook/zstd/commit/48b5a7bd8bedcfcaf22631d45c61c2f544315053)
- Removed an unused macro constant.
  ↳ [#3786](https://github.com/facebook/zstd/pull/3786): [ea4027c](https://github.com/facebook/zstd/commit/ea4027c003d31bb75d24a2284d06ed4c06300f59)
- Fixed documentation description of FSE probability bit consumption.
  ↳ [#3806](https://github.com/facebook/zstd/pull/3806): [b38d87b](https://github.com/facebook/zstd/commit/b38d87b476b804d7948928d298c784deb875a93c)
- Fixed the status table format error in the document.
  ↳ [#3816](https://github.com/facebook/zstd/pull/3816): [52e41b9](https://github.com/facebook/zstd/commit/52e41b9ac8010da90bbe97421cca533afd6914c0)
- Updated license text in xxhash.c and xxhash.h.
  ↳ [#3820](https://github.com/facebook/zstd/pull/3820): [59dcc47](https://github.com/facebook/zstd/commit/59dcc475798b3e522be8cd3ba41a170b34c10d63)
- Updated actions/upload-artifact version notes in Windows build workflow.
  ↳ [#3849](https://github.com/facebook/zstd/pull/3849): [377ecef](https://github.com/facebook/zstd/commit/377ecefce93d3a8705cb54c553681ff234bd9f34)
- Adjust comment indentation to keep code style consistent.
  ↳ [#3917](https://github.com/facebook/zstd/pull/3917): [ef82b21](https://github.com/facebook/zstd/commit/ef82b214ad1023f6123c3d9c9a7dbce24130d9bd)
- Updated documentation for -V option.
  ↳ [#3928](https://github.com/facebook/zstd/pull/3928): [4fb0a77](https://github.com/facebook/zstd/commit/4fb0a77314cabc65eb90895fae35a7f38ace560d)
- Migrate documents related to zero offset processing.
  ↳ [#3937](https://github.com/facebook/zstd/pull/3937): [d2f56ba](https://github.com/facebook/zstd/commit/d2f56ba44208f56b5370a9ef6ce0d2c32f283131)
- Update example frames in documentation for offset==0 decoder testing.
  ↳ [#3937](https://github.com/facebook/zstd/pull/3937): [eb5f7a7](https://github.com/facebook/zstd/commit/eb5f7a7fa278ab76c3390555f36162c638f63b53)
- Adjust .gitignore file to preserve .zst files for testing.
  ↳ [#3954](https://github.com/facebook/zstd/pull/3954): [37ff4f9](https://github.com/facebook/zstd/commit/37ff4f91eba72a936771b177c83d27151d33e2f1)
- Fix duplicate paragraphs in document.
  ↳ [#3958](https://github.com/facebook/zstd/pull/3958): [ff6713f](https://github.com/facebook/zstd/commit/ff6713fd72b083ce8a7d1f2a89cd3749ce9f07a8)
- Fixed typos in Makefile.
  ↳ [#3949](https://github.com/facebook/zstd/pull/3949): [8ba5bc4](https://github.com/facebook/zstd/commit/8ba5bc4729a04919e4416d8e84cfab28e1d7801c)
- Fixed typos in comments in zstd.h.
  ↳ [#3977](https://github.com/facebook/zstd/pull/3977): [c5da438](https://github.com/facebook/zstd/commit/c5da438dc0ca81ce697a73a02b060e3ba7550bab)
