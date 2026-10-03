# Release Note

## Important Changes

### API Abstraction Layer (Layer 1)
- Deprecated bufferless and block-level APIs, and added corresponding deprecated wrapper functions. (Architecture-related: public API deprecation)
  ↳ [#3534](https://github.com/facebook/zstd/pull/3534): [fbd97f3](https://github.com/facebook/zstd/commit/fbd97f305a521272601fe6394460287294c2406c)
- Added ZSTD_setFParams() and ZSTD_setParams() auxiliary functions, unified the parameter setting interface, and supplemented unit testing and documentation. (Architecture-related: public API)
  ↳ [#3530](https://github.com/facebook/zstd/pull/3530): [07a2a33](https://github.com/facebook/zstd/commit/07a2a33135a5f5fd99c7f69e7dc0147c6894d252)
- Fixed the dictionary loading initialization order issue to ensure that adjustments in special circumstances will not be overwritten by subsequent initialization. (Architecture-related: public API)
  ↳ [#3589](https://github.com/facebook/zstd/pull/3589): [2e29728](https://github.com/facebook/zstd/commit/2e29728797c49db1f4e7bfbd52ef9d7ae45d5851)
- Clarify the requirements of dstCapacity in the single compression function to ensure that compression can succeed when sufficient space is provided. (Architecture-related: public API)
  ↳ [#3531](https://github.com/facebook/zstd/pull/3531): [c40c737](https://github.com/facebook/zstd/commit/c40c7378c679dab6ab168f5153858226d101db04)
- Added documentation for ZSTD_CCtx_loadDictionary and ZSTD_CCtx_refPrefix to explain the compatibility differences between LDM (long distance mode) and dictionaries. (Architecture-related: public API)
  ↳ [#3553](https://github.com/facebook/zstd/pull/3553): [f4563d8](https://github.com/facebook/zstd/commit/f4563d87b954768e5524e1b53bb5e5d607cef35d)
- Added documentation for the seekable format, supplemented the role of the Maximum Frame Size parameter and selection suggestions. (Architecture-related: public API)
  ↳ [#3547](https://github.com/facebook/zstd/pull/3547): [dd8cb5a](https://github.com/facebook/zstd/commit/dd8cb5a0f1a7581c407a7307fc526deb47e1f266)
- The version number has been updated to v1.5.5, and the manual page has been updated simultaneously. (Architecture-related: version and compatibility)
  ↳ [#3577](https://github.com/facebook/zstd/pull/3577): [9f58241](https://github.com/facebook/zstd/commit/9f58241dcc9f0f7882347ec5dc5560e41727b8c4)

### Application and Integration Layer (Layer 3)
- Added memory mapping dictionary support, provided --mmap-dict and --no-mmap-dict command line options, optimized dictionary loading process, avoided unnecessary system calls and memory copies, and supported Windows platform. (Architectural event: HighResTimer module removed)
  ↳ [#3486](https://github.com/facebook/zstd/pull/3486): [610c8b9](https://github.com/facebook/zstd/commit/610c8b9e338466451b1e96ab5bcb9d88b6d3a1c1), [4373c5a](https://github.com/facebook/zstd/commit/4373c5ab88b733b482f2e51a209cea8966870901), [2d8afd9](https://github.com/facebook/zstd/commit/2d8afd9ce14689b8db44ec0c07e55d5c4198fb69), [96e55c1](https://github.com/facebook/zstd/commit/96e55c14f208d708922a7ef8e9e2dd03fc847274) | [#3557](https://github.com/facebook/zstd/pull/3557): [b2ad17a](https://github.com/facebook/zstd/commit/b2ad17a658f9ac07ad624d8f17ee442ec8f9bc44)
- Fixed the problem of automatically enabling sparse writing when decompressing to non-ordinary files such as block devices. Now sparse writing is only automatically enabled on regular files. At the same time, the file opening logic and dictionary file checking are optimized. (Architecture-related: platform compatibility)
  ↳ [#3584](https://github.com/facebook/zstd/pull/3584): [5bf1359](https://github.com/facebook/zstd/commit/5bf1359e3be0e64149bbb989f2addfc42adf30d3), [14d0cd5](https://github.com/facebook/zstd/commit/14d0cd5d690ef0956a2e3085e81c78578f55b81e)
- Fixed the problem of using zlib proprietary types Bytef and uInt in LZMA decompression, using BYTE and direct assignment instead, and updating the progress display macro. (Architecture-related: public API)
  ↳ [#3497](https://github.com/facebook/zstd/pull/3497): [886de7b](https://github.com/facebook/zstd/commit/886de7bc0404f856e6d05b6550d13424d8ad4fe9)
- Simplify the benchmark API, change the return type of BMK_syntheticTest, BMK_benchFilesAdvanced and BMK_benchFiles from BMK_benchOutcome_t to int, directly return the integer error code. (Architecture event: HighResTimer module change)
  ↳ [#3526](https://github.com/facebook/zstd/pull/3526): [db79219](https://github.com/facebook/zstd/commit/db79219f70aa9b2bee9358ff95f1ba304a82e4bf), [1e38e07](https://github.com/facebook/zstd/commit/1e38e07b3d6e608361c36bcc4245471b6b03c570)
- Changed multiple functions in the zlib wrapper internal benchmark to static links to limit their scope. (Architecture-related: public API)
  ↳ [#3526](https://github.com/facebook/zstd/pull/3526): [9efc148](https://github.com/facebook/zstd/commit/9efc14804eaa6aa56514a17cabd07c0d73235892)
- Introduced variants accepting optional file descriptors for common file utility functions to take advantage of the performance advantages of f-variants such as fchmod. (Architecture-related: public API)
  ↳ [#3479](https://github.com/facebook/zstd/pull/3479): [a5a2418](https://github.com/facebook/zstd/commit/a5a2418df4e41a826e87ef8ea2205fc2041ac0d2)
- In the build configuration of contrib/pzstd, added logic to automatically detect and select the latest C++ standard (minimum C++11) supported by the compiler. (Architecture-related: Build requirement: C++11 minimum standard)
  ↳ [#3574](https://github.com/facebook/zstd/pull/3574): [1b8bddc](https://github.com/facebook/zstd/commit/1b8bddc41ea721d1ff8056280bbf62d3bb0da344)
- Modify the build configuration of pzstd, only explicitly set -std=c++11 when the default C++ standard is lower than C++11, otherwise the compiler default standard is used. (Architecture-related: Build requirements: C++11 conditional setting)
  ↳ [#3574](https://github.com/facebook/zstd/pull/3574): [cbe0f0e](https://github.com/facebook/zstd/commit/cbe0f0e435e713091fa4741635dab97476e62983)

### Cross-cutting / Other Architecture-related Changes
- Added init once memory type to ensure that the memory in the workspace is initialized at least once and is used for the implementation of row hash label space. (Architecture-related: public API)
  ↳ [#3529](https://github.com/facebook/zstd/pull/3529): [9420bce](https://github.com/facebook/zstd/commit/9420bce8a491e21821c4b372f837bf4bd47e5870)
- Fixed the problem of missing dependencies when building zstd-dll: moved the custom allocation function to the header file to avoid dependence on common.o; also added test targets and GitHub workflow. (Architecture-related: build and installation methods)
  ↳ [#3496](https://github.com/facebook/zstd/pull/3496): [c78f434](https://github.com/facebook/zstd/commit/c78f434aa4f5f1097c8edb975f4c1635817a5a71)
- Initialize the compression level field in the static CDict; fix the problem of user-defined MOREFLAGS and FUZZER_FLAGS being overwritten in the Makefile; add MSAN fuzz non-optimized CI workflow. (Architecture-related: build and installation methods)
  ↳ [#3527](https://github.com/facebook/zstd/pull/3527): [988ce61](https://github.com/facebook/zstd/commit/988ce61a0c019d7fc58575954636b9ff8d147845)
- Modify the assert macro definition: change WARN_ON((x)) to WARN_ON(!(x)) so that it can trigger the assertion correctly. (Architecture-related: platform compatibility)
  ↳ [#3532](https://github.com/facebook/zstd/pull/3532): [6313a58](https://github.com/facebook/zstd/commit/6313a58e45bb13c19664037a115862703b16b6f5)
- Provide an interface for the fuzz test sequence producer plug-in, and add setup and cleanup calls in multiple fuzz test cases. (Architecture-related: public API)
  ↳ [#3551](https://github.com/facebook/zstd/pull/3551): [a810e1e](https://github.com/facebook/zstd/commit/a810e1eeb7ebc12d5a2c96f6dc3660cfc51c145d)
- Optimize the compression parameter adaptation of the seekable format in small frame size scenarios, significantly improving the compression speed; at the same time, update the seekable_compression sample program to support setting the compression level. (Architecture event: seekable format module change)
  ↳ [#3544](https://github.com/facebook/zstd/pull/3544): [1df9f36](https://github.com/facebook/zstd/commit/1df9f36c6c6cea08778d45a4adaf60e2433439a3)
- Introduce salt value for row hashing, modify the hash function to support salt value parameter, and avoid performance regression when continuous compression uses the same label space. (Architecture-related: public API)
  ↳ [#3533](https://github.com/facebook/zstd/pull/3533): [91f4c23](https://github.com/facebook/zstd/commit/91f4c23e634a1d260f290f00b6d870a56cd59ab6)
- Add instructions for building Universal2 (supporting Apple Silicon and Intel) on macOS through CMake in README. (Architecture-related: build and installation methods)
  ↳ [#3568](https://github.com/facebook/zstd/pull/3568): [408bd1e](https://github.com/facebook/zstd/commit/408bd1e9fe8c7dc52b45b3879b0c03d034f51bec), [82cf603](https://github.com/facebook/zstd/commit/82cf6037ac28042f82bc0bc44188f51177126b43)
- Added GitHub Actions workflow for generating release artifacts in Windows 64-bit environment. (Architecture-related: Build and Release: Windows 64-bit artifacts)
  ↳ [#3491](https://github.com/facebook/zstd/pull/3491): [f37b291](https://github.com/facebook/zstd/commit/f37b291bf56a7b2ba38deb82332aa9f6555d9c3f)
- Lowered the CMake minimum version requirement to 3.16, and disabled the -z noexecstack linker flag check for older versions of CMake. (Architecture-related: Build requirement: CMake minimum version 3.16)
  ↳ [#3510](https://github.com/facebook/zstd/pull/3510): [8420502](https://github.com/facebook/zstd/commit/8420502ef9d5980d2297c88f80d19ae18f84f6df)
- Fixed third-party action dependencies in the GitHub Actions workflow from version tags to specific commit hashes to improve supply chain security. (Architecture-related: Build security: Fixed third-party action dependencies)
  ↳ [#3542](https://github.com/facebook/zstd/pull/3542): [1ec5562](https://github.com/facebook/zstd/commit/1ec556238e08d377093d4445aebb5be42637abea)
- Fixed dependency hash of base image in Dockerfile. (Architecture-related: Build repeatability: Fixed base image dependency)
  ↳ [#3542](https://github.com/facebook/zstd/pull/3542): [cd94860](https://github.com/facebook/zstd/commit/cd9486031dcb1cab5143d2c0c6edc34127d97a69)
- Disable linker flag detection under MSVC and ClangCL compilers to fix compilation issues when using clang-cl on Windows. (Architecture-related: Platform Compatibility: MSVC/ClangCL linker flags)
  ↳ [#3569](https://github.com/facebook/zstd/pull/3569): [979b047](https://github.com/facebook/zstd/commit/979b047114622265b6015a9587434e8229429411)
- Adjust the naming and directory structure of Windows release artifacts to be consistent with the v1.5.0 version specification, and update the CI workflow to automatically execute when an event is released. (Architecture-related: Release artifact structure)
  ↳ [#3591](https://github.com/facebook/zstd/pull/3591): [fcaa422](https://github.com/facebook/zstd/commit/fcaa4228974870bd873130681c29ed140d5c1c39)

### Core Compression Engine (Layer 0)
- Fixed an overread issue that could occur when decompressing certain invalid magic-less frames or requesting invalid skippable frame attributes. (Architecture-related: decompression behavior)
  ↳ [#3592](https://github.com/facebook/zstd/pull/3592): [e4120c5](https://github.com/facebook/zstd/commit/e4120c55130656c213c09007c02ece544d66ffc1)

## Routine Changes

### New features
- No significant changes.

### bug fixes
- Fixed a rare corruption bug in the block splitter, which misjudged a literal sequence of length 65536 as a length of 0, thereby corrupting the duplicate offset history.
  ↳ [#3517](https://github.com/facebook/zstd/pull/3517): [395a2c5](https://github.com/facebook/zstd/commit/395a2c54621d36b4eaf17b4111353243f91a1d90)
- Fixed a segfault caused by calling setvbuf() when the file pointer is null. The setvbuf() call has now been moved to the branch after the file is successfully opened.
  ↳ [#3541](https://github.com/facebook/zstd/pull/3541): [c4c3e11](https://github.com/facebook/zstd/commit/c4c3e11958aed4dc99ec22e3d31c405217575a8c)
- Fixed an issue where position 0 was mistakenly used for matching calculations due to the tagTable size being halved. Position 0 was skipped in the row hash matching loop to avoid premature termination of matching.
  ↳ [#3548](https://github.com/facebook/zstd/pull/3548): [a91e91d](https://github.com/facebook/zstd/commit/a91e91d61412e0a83e370028d62e7a58dfa85bd0)
- Fixed an issue where the window size did not take into account the complete dictionary contents when loading a dictionary, and adjusted the dictionary truncation threshold to support larger index tables.
  ↳ [#3556](https://github.com/facebook/zstd/pull/3556): [3e0550e](https://github.com/facebook/zstd/commit/3e0550ee5279735693b01464ede7cb1ec22fe6b7)
- Added checks for destination buffer validity when decompressing, and added fuzz testing to randomize the destination pointer when zero-sized buffers are used.
  ↳ [#3555](https://github.com/facebook/zstd/pull/3555): [fcaf06d](https://github.com/facebook/zstd/commit/fcaf06ddb489f683afb1af3639727991fd9accae)

### Refactoring optimization
- Restructure the dictionary file status acquisition logic into an independent function to reduce repeated system calls.
  ↳ [#3486](https://github.com/facebook/zstd/pull/3486): [8a189b1](https://github.com/facebook/zstd/commit/8a189b1b29c5e3a9946e6dcc0017b4e7c4738282)
- Add assertion when freeing dictionary to verify dictionary buffer type is valid.
  ↳ [#3486](https://github.com/facebook/zstd/pull/3486): [70850eb](https://github.com/facebook/zstd/commit/70850eb72b4288874506589546cb30d0c80d6b58)

### Test related
- Added unit tests for multiple decompression and forward seeking for seekable format.
  ↳ [#3581](https://github.com/facebook/zstd/pull/3581): [649a9c8](https://github.com/facebook/zstd/commit/649a9c85c38195ff67065c02e207da9f8a342785)
- Fixed fullbench benchNb not resetting when testing multiple files.
  ↳ [#3516](https://github.com/facebook/zstd/pull/3516): [4b9e3d1](https://github.com/facebook/zstd/commit/4b9e3d11a67e6cea2fb137e5a564925306f9231f)

### Performance optimization
- Optimized the performance of forward jump when decompressing seekable format to avoid repeatedly reading frame data when jumping multiple small intervals within the same frame.
  ↳ [#3581](https://github.com/facebook/zstd/pull/3581): [618bf84](https://github.com/facebook/zstd/commit/618bf84e0d16070ac67a80b404041adb264c4952)
- In the lazy match finder, when no match is found for 2KB in a row, stop inserting each position into the hash table and only insert the position actually searched, thus improving the processing speed of incompressible data.
  ↳ [#3552](https://github.com/facebook/zstd/pull/3552): [a3c3a38](https://github.com/facebook/zstd/commit/a3c3a38b9b956d2689a019b1b29482e86fd98836)
- Halved the tag space size of RowHash, compressed each entry from 6 bytes to 5 bytes, saving 16% of the hash table space, with a slight loss of compression rate (up to 0.2%), and the speed increased or decreased.
  ↳ [#3543](https://github.com/facebook/zstd/pull/3543): [33e3909](https://github.com/facebook/zstd/commit/33e39094e7d6680544290a41ff8f8aa34517bc1f)
- Optimized patch-from compression speed, only loaded dictionary suffixes into normal match finders, and fixed bit offset boundary and tagTable size calculation errors.
  ↳ [#3545](https://github.com/facebook/zstd/pull/3545): [53bad10](https://github.com/facebook/zstd/commit/53bad103ce61fd2c170bf49bf335201a8a51f72f)
- Mark the BIT_reloadDStream function as forced inline to improve the decompression speed under PGO optimized compilation.
  ↳ [#3576](https://github.com/facebook/zstd/pull/3576): [e6dccbf](https://github.com/facebook/zstd/commit/e6dccbf48246f4e2844251972fcc0946a5de5154)
- Removed Clang-only branch prediction hints in ZSTD_decodeSequence to improve decompression performance when PGO is enabled.
  ↳ [#3576](https://github.com/facebook/zstd/pull/3576): [b558190](https://github.com/facebook/zstd/commit/b558190ac76fe6b0f2c42ae5fb9d2f90652d21b0)

### Security related
- No significant changes.

### Documentation
- Updated Zstandard format specification document to clarify details of Huffman block and tree descriptions and stream sizes.
  ↳ [#3514](https://github.com/facebook/zstd/pull/3514): [832f559](https://github.com/facebook/zstd/commit/832f559b0b9d22f3afc6b6e11a55044b9a238db5) | [#3538](https://github.com/facebook/zstd/pull/3538): [64e8511](https://github.com/facebook/zstd/commit/64e8511b267e48b8c796ae70d41f3e7fe16a28d5)
- Updated documentation for the --rsyncable option to re-state its impact on compression speed and compression ratio.
  ↳ [#3570](https://github.com/facebook/zstd/pull/3570): [35c0c20](https://github.com/facebook/zstd/commit/35c0c2075ea831ee10fa08b09c93484f1b098000)
- Fixed incorrect build command in README.md, corrected 'ninja build' to 'ninja'.
  ↳ [#3568](https://github.com/facebook/zstd/pull/3568): [c36d54f](https://github.com/facebook/zstd/commit/c36d54f5ed74da651a4bcbbb3bc7128551339f76)

### Build/CI
- Fix the permission configuration of the publishing artifact workflow, and change the content permission from read-only to write to support uploading publishing artifacts.
  ↳ [#3511](https://github.com/facebook/zstd/pull/3511): [d54ad3c](https://github.com/facebook/zstd/commit/d54ad3c234cb154a581d6e91a6010e900311b55e)
- Adjust the build system to ensure that zstd binaries are built during testing, and correct test dependencies.
  ↳ [#3490](https://github.com/facebook/zstd/pull/3490): [97ab0e2](https://github.com/facebook/zstd/commit/97ab0e2ab60fdda78f610032408df104de20b9f1), [183a18a](https://github.com/facebook/zstd/commit/183a18a45c1d69f8c42b9fcd25e6d28f9b3d75bb)
- Optimize the Windows component generation workflow, adjust the shell environment and compiler packages, and simplify the process.
  ↳ [#3491](https://github.com/facebook/zstd/pull/3491): [43bc470](https://github.com/facebook/zstd/commit/43bc470fe0ea6cb188118e27f92b9071d30371a9), [5be3f19](https://github.com/facebook/zstd/commit/5be3f19e1d5745e50dc42c57aeda35e977de39de), [f8ae216](https://github.com/facebook/zstd/commit/f8ae21680f06112c509cdf474e97b6e96634a776)
- Upgrade GitHub CodeQL Action to the latest version.
  ↳ [#3503](https://github.com/facebook/zstd/pull/3503): [6894746](https://github.com/facebook/zstd/commit/6894746eb1cf218c045627bac8b21e448754ac1b) | [#3518](https://github.com/facebook/zstd/pull/3518): [1be9529](https://github.com/facebook/zstd/commit/1be95291a89160be121c987c2e385331a65a4a0e) | [#3549](https://github.com/facebook/zstd/pull/3549): [e2965ed](https://github.com/facebook/zstd/commit/e2965edd107acd0123294e23848cdc00af906468) | [#3573](https://github.com/facebook/zstd/pull/3573): [191d229](https://github.com/facebook/zstd/commit/191d22994ffa470c17584d6c6d9a57c476c065b8)
- Set the default permissions of the GitHub Actions workflow to read-only and fix the action version of the published binary.
  ↳ [#3488](https://github.com/facebook/zstd/pull/3488): [727d031](https://github.com/facebook/zstd/commit/727d03161f689399b7f6dbd65cd624185bf4de8c)
- Added CI workflow to test compilation under different external compressor configurations.
  ↳ [#3505](https://github.com/facebook/zstd/pull/3505): [6a86db1](https://github.com/facebook/zstd/commit/6a86db11a4cafabbbbb56c2ae39881774b52d43f)
- Added 32-bit test task in CI.
  ↳ [#3509](https://github.com/facebook/zstd/pull/3509): [d3d0b92](https://github.com/facebook/zstd/commit/d3d0b92e5e64e1f1b32aa58679d9c74f3ded0abe)
- Upgrade actions/checkout in CI workflow to v3.5.0.
  ↳ [#3572](https://github.com/facebook/zstd/pull/3572): [4cf9c7e](https://github.com/facebook/zstd/commit/4cf9c7e09810f6f0f41fba2d2b4c1d7998d990c5)
- Added Windows test task using ClangCL tool in CI.
  ↳ [#3579](https://github.com/facebook/zstd/pull/3579): [0f77956](https://github.com/facebook/zstd/commit/0f77956bccc3b95e0e7b51ef0d16ed1db695779b)

### Maintenance
- Use file descriptor-based chmod and chown to set the output file status, and adjust the order of calls to ensure that these operations are completed before closing the file.
  ↳ [#3479](https://github.com/facebook/zstd/pull/3479): [f746c37](https://github.com/facebook/zstd/commit/f746c37d00ae7c4e921b9089e8bf1f87d34adcfb)
- Fix MSVC compilation warning, adjust the type conversion and array type of bit counting function in bits.h.
  ↳ [#3495](https://github.com/facebook/zstd/pull/3495): [a7de1d9](https://github.com/facebook/zstd/commit/a7de1d9f4954a1a7f8b15ecc1eff6a249dd9b4f6)

### Others
- Renamed function FIO_createDictBuffer to FIO_createDictBufferMMap, and updated related comments.
  ↳ [#3486](https://github.com/facebook/zstd/pull/3486): [cc4e941](https://github.com/facebook/zstd/commit/cc4e9417457bd33c657a613095830f3a2700804d)
- Fixed typos in several source files.
  ↳ [#3513](https://github.com/facebook/zstd/pull/3513): [547794e](https://github.com/facebook/zstd/commit/547794ef400832bcb7ebfee2784eb28f5ec6344c)
- Updated changelog to prepare for v1.5.5.
  ↳ [#3577](https://github.com/facebook/zstd/pull/3577): [9b4833d](https://github.com/facebook/zstd/commit/9b4833df2de3ab1779474c08725e398ea96127a1)
- Removed the no longer used Appveyor CI badge from the README.
  ↳ [#3593](https://github.com/facebook/zstd/pull/3593): [8eef337](https://github.com/facebook/zstd/commit/8eef3370a3c7c98cdac4e7311a7f078f6d564bad)
