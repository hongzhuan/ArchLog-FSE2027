# Release Note

## Important Changes

### Application and Integration Layer (Layer 3)

- The file tool adds a status-setting interface that can accept an optional file descriptor, allowing metadata such as permissions and owner to be set directly through the already-open output file handle. [commit](https://github.com/facebook/zstd/commit/a5a2418df4e41a826e87ef8ea2205fc2041ac0d2)
- Add a CLI parameter to manually control whether the dictionary uses memory mapping, allowing callers to override the automatic behavior based on dictionary size. [commit](https://github.com/facebook/zstd/commit/2d8afd9ce14689b8db44ec0c07e55d5c4198fb69)

### Cross-cutting / Other Architecture-related Changes

- Long-running CI adds 32-bit build and test tasks, covering compilation and runtime paths in 32-bit environments. [commit](https://github.com/facebook/zstd/commit/d3d0b92e5e64e1f1b32aa58679d9c74f3ded0abe)
- README adds commands for building macOS Universal2 binaries via CMake, explaining how to include both Intel and Apple Silicon architectures. [commit](https://github.com/facebook/zstd/commit/82cf6037ac28042f82bc0bc44188f51177126b43)
- README supplements macOS Universal2 CMake build commands and adjusts the architecture list to supported Intel and Apple Silicon targets. [commit](https://github.com/facebook/zstd/commit/408bd1e9fe8c7dc52b45b3879b0c03d034f51bec)

### Core Compression Engine (Layer 0)

- Add `ZSTD_setCParams()`, `ZSTD_setFParams()`, and `ZSTD_setParams()` helper interfaces for setting compression, frame, and combined parameters respectively, and add fuzz tests. [commit](https://github.com/facebook/zstd/commit/07a2a33135a5f5fd99c7f69e7dc0147c6894d252)
- Add a one-time initialization memory allocation path in the workspace, and adjust compression context and workspace allocation logic to reuse this area. [commit](https://github.com/facebook/zstd/commit/9420bce8a491e21821c4b372f837bf4bd47e5870)
- Add a 64-bit circular right shift helper function for the RowHash implementation, used to mix the bit distribution of hash values into match tags. [commit](https://github.com/facebook/zstd/commit/91f4c23e634a1d260f290f00b6d870a56cd59ab6)

## Routine Changelog

### Bug Fixes

- Fix MSVC warnings in Visual Studio builds, and adjust bit operations, Huffman decoding code, and CI configuration so that warning checks pass. [commit](https://github.com/facebook/zstd/commit/a7de1d9f4954a1a7f8b15ecc1eff6a249dd9b4f6)
- Fix missing public dependency declarations in Windows DLL builds, and organize public symbol dependencies through a centralized allocation header file. [commit](https://github.com/facebook/zstd/commit/c78f434aa4f5f1097c8edb975f4c1635817a5a71)
- Fix permission configuration in the release artifact workflow, ensuring that tasks uploading release assets have the required release write permission. [commit](https://github.com/facebook/zstd/commit/d54ad3c234cb154a581d6e91a6010e900311b55e)
- Fix typos in documentation, code, and tests, and synchronously correct affected CLI expected output. [commit](https://github.com/facebook/zstd/commit/547794ef400832bcb7ebfee2784eb28f5ec6344c)
- Fix occasional data corruption in the high compression level block splitter, adjust long literal sequence handling, and add regression samples and fuzz tests. [commit](https://github.com/facebook/zstd/commit/395a2c54621d36b4eaf17b4111353243f91a1d90)
- Fix parameter and return value handling in internal benchmark calls of the zlib wrapper, ensuring the wrapper example runs tests as expected. [commit](https://github.com/facebook/zstd/commit/9efc14804eaa6aa56514a17cabd07c0d73235892)
- Fix assertion definitions in the Linux kernel adaptation layer so that assertions expand correctly under kernel build configurations. [commit](https://github.com/facebook/zstd/commit/6313a58e45bb13c19664037a115862703b16b6f5)
- Fix the issue where RowHash treats input position 0 as a match candidate, and update compression regression results. [commit](https://github.com/facebook/zstd/commit/a91e91d61412e0a83e370028d62e7a58dfa85bd0)
- Fix the update position of the matcher after window updates, and increase the maximum loadable dictionary size to avoid missing input regions when the window advances. [commit](https://github.com/facebook/zstd/commit/3e0550ee5279735693b01464ede7cb1ec22fe6b7)
- Disable sparse writes when decompressing to non-regular files such as block devices using `-o`, avoiding error paths for targets that do not support sparse file operations. [commit](https://github.com/facebook/zstd/commit/5bf1359e3be0e64149bbb989f2addfc42adf30d3)
- Fix handling of decompression to block devices via `-o` in issue #3583, and correct ChangeLog entries and local dictionary initialization documentation. [commit](https://github.com/facebook/zstd/commit/2e29728797c49db1f4e7bfbd52ef9d7ae45d5851)
- Fix potential over-read in skippable frame decoding, and clarify that the read interface only returns frame content and requires the input to be a valid skippable frame. [commit](https://github.com/facebook/zstd/commit/e4120c55130656c213c09007c02ece544d66ffc1)

### Refactoring

- The Windows artifact workflow switches the execution shell to the MinGW environment to be compatible with commands required by build scripts. [commit](https://github.com/facebook/zstd/commit/43bc470fe0ea6cb188118e27f92b9071d30371a9)
- Streamline the Windows 64-bit artifact generation workflow, reusing existing build steps and removing duplicate manual packaging commands. [commit](https://github.com/facebook/zstd/commit/5be3f19e1d5745e50dc42c57aeda35e977de39de)
- Refactor the dictionary file status retrieval process, centralizing the file type, size, and status information of the dictionary for loading logic. [commit](https://github.com/facebook/zstd/commit/8a189b1b29c5e3a9946e6dcc0017b4e7c4738282)
- Simplify the synthetic data benchmark interface and unify error return methods, so that failure scenarios such as invalid compression levels are reported via status codes. [commit](https://github.com/facebook/zstd/commit/db79219f70aa9b2bee9358ff95f1ba304a82e4bf)
- Remove branch probability hints used only for Clang in Zstandard sequence decoding, unifying the decoding code path across different compilers. [commit](https://github.com/facebook/zstd/commit/b558190ac76fe6b0f2c42ae5fb9d2f90652d21b0)
- The Windows release workflow is changed to trigger on release publish events, and the artifact directory is named after the release tag to adjust the artifact structure. [commit](https://github.com/facebook/zstd/commit/fcaa4228974870bd873130681c29ed140d5c1c39)

### Tests

- When setting output file metadata, use the descriptor of the already-open file to call the status-setting function, avoiding re-looking up the target file by path. [commit](https://github.com/facebook/zstd/commit/f746c37d00ae7c4e921b9089e8bf1f87d34adcfb)
- Fix expected output in basic compression, gzip compatibility, and window adjustment CLI tests, making assertions match current command behavior. [commit](https://github.com/facebook/zstd/commit/7da1c6ddbfe61ad2f9bc9c3a2205567a76be24f5)
- Fix the issue where fullbench did not reset counters when benchmarking multiple files consecutively, so that the second and subsequent files also participate in performance testing. [commit](https://github.com/facebook/zstd/commit/4b9e3d11a67e6cea2fb137e5a564925306f9231f)
- Extend the default timeout of the CLI test runner to reduce premature termination of tests in slow CI environments. [commit](https://github.com/facebook/zstd/commit/b7080f4c67bdb9d190bda529f7309e34fb990b23)
- Adjust byte string and integer comparison methods in CLI tests to be compatible with Python 3.6 type behavior. [commit](https://github.com/facebook/zstd/commit/50e8f55e7d5928af9c3411afdb4fbedb4d8f770d)
- Add a CLI test for compressing files when the directory has no write permission, verifying that the program reports inability to create the output file. [commit](https://github.com/facebook/zstd/commit/957a0ae52d0f49eccd260a22ceb5f5dfed064e9f)
- Halve the storage width of the RowHash match tag table, and synchronously adjust the compressor implementation, fuzz tests, and regression data. [commit](https://github.com/facebook/zstd/commit/33e39094e7d6680544290a41ff8f8aa34517bc1f)
- Mark bufferless and block-level compression interfaces as deprecated, and retain compatibility entry points through public wrapper functions, guiding callers to migrate to the recommended API. [commit](https://github.com/facebook/zstd/commit/fbd97f305a521272601fe6394460287294c2406c)
- Fix type errors in CLI tests when mixing byte strings and integer comparisons in Python 3. [commit](https://github.com/facebook/zstd/commit/29b8a3d8f2bdd26d6952d5bdb62708aab591e1ae)
- Simplify the line-splitting logic of the CLI test runner output, uniformly handle line endings, and reduce redundant conversions. [commit](https://github.com/facebook/zstd/commit/3b001a38fea0a78e6d6a9ce73f9c0ab9459d6341)
- The lazy matcher adds a strategy to skip incompressible data, speeding up scanning of incompressible regions at a small compression ratio cost. [commit](https://github.com/facebook/zstd/commit/a3c3a38b9b956d2689a019b1b29482e86fd98836)
- The fuzz testing framework adds a third-party block-level sequence generator plugin interface, and supports compiling, integrating, and running external plugins through independent targets. [commit](https://github.com/facebook/zstd/commit/a810e1eeb7ebc12d5a2c96f6dc3660cfc51c145d)
- The decompression API rejects null destination pointers or zero-capacity buffers when the sequence count is non-zero, and adds destination address boundary checks and fuzz tests. [commit](https://github.com/facebook/zstd/commit/fcaf06ddb489f683afb1af3639727991fd9accae)

### Performance

- Optimize read and index handling of the seekable format in small frame scenarios, reducing extra read overhead required for parsing frames. [commit](https://github.com/facebook/zstd/commit/1df9f36c6c6cea08778d45a4adaf60e2433439a3)
- When patch-from loads a dictionary, the full dictionary is passed to the long-distance matcher, and window and dictionary state settings are optimized to reduce patch compression overhead. [commit](https://github.com/facebook/zstd/commit/53bad103ce61fd2c170bf49bf335201a8a51f72f)

### Documentation

- Clarify the length ranges and bit encoding rules for Huffman tree descriptions and compressed literal streams in the Zstandard format specification. [commit](https://github.com/facebook/zstd/commit/832f559b0b9d22f3afc6b6e11a55044b9a238db5)
- Supplement the format specification with explanations of compressed Huffman tree descriptions and literal stream sizes, clarifying encoding length boundaries. [commit](https://github.com/facebook/zstd/commit/64e8511b267e48b8c796ae70d41f3e7fe16a28d5)
- Update library, CLI, and manual versions to 1.5.5, and synchronize API manual chapter titles and deprecated interface descriptions. [commit](https://github.com/facebook/zstd/commit/9f58241dcc9f0f7882347ec5dc5560e41727b8c4)

### Build / CI

- Update v1.5.4 release notes and project build and CI configuration, summarizing performance, CLI, API, bug fixes, and platform support changes in this version, and synchronize dependencies and copyright information. [commit](https://github.com/facebook/zstd/commit/610c8b9e338466451b1e96ab5bcb9d88b6d3a1c1)
- Meson test targets explicitly depend on programs required by `playTests.sh`, ensuring that relevant executables are built before integration tests are run. [commit](https://github.com/facebook/zstd/commit/183a18a45c1d69f8c42b9fcd25e6d28f9b3d75bb)
- Always build the zstd command-line program when Meson tests are enabled, avoiding test task failures due to missing executables. [commit](https://github.com/facebook/zstd/commit/97ab0e2ab60fdda78f610032408df104de20b9f1)
- Add a Windows 64-bit release workflow that uses GitHub Actions to build and upload zstd binary artifacts. [commit](https://github.com/facebook/zstd/commit/f37b291bf56a7b2ba38deb82332aa9f6555d9c3f)
- The Windows artifact workflow switches to another C compiler to resolve build issues with the original compiler. [commit](https://github.com/facebook/zstd/commit/f8ae21680f06112c509cdf474e97b6e96634a776)
- The Scorecards workflow upgrades the GitHub CodeQL action from 2.2.1 to 2.2.4. [commit](https://github.com/facebook/zstd/commit/6894746eb1cf218c045627bac8b21e448754ac1b)
- GitHub Actions workflows default to read-only repository permissions, and only explicitly grant the required write permissions to release artifact tasks. [commit](https://github.com/facebook/zstd/commit/727d03161f689399b7f6dbd65cd624185bf4de8c)
- Short-test CI adds an external compressor dependency matrix, verifying builds with no zlib/LZ4/LZMA and with different combinations enabled. [commit](https://github.com/facebook/zstd/commit/6a86db11a4cafabbbbb56c2ae39881774b52d43f)
- CMake compilation flag configuration no longer requires CMake 3.18, and bypasses unavailable linker flag detection interfaces in older versions. [commit](https://github.com/facebook/zstd/commit/8420502ef9d5980d2297c88f80d19ae18f84f6df)
- The Scorecards workflow upgrades the GitHub CodeQL action from 2.2.4 to 2.2.5. [commit](https://github.com/facebook/zstd/commit/1be95291a89160be121c987c2e385331a65a4a0e)
- Static dictionary compression context now initializes the compression level, and a new MSan long test CI check covers this context construction path. [commit](https://github.com/facebook/zstd/commit/988ce61a0c019d7fc58575954636b9ff8d147845)
- Pin more GitHub Actions dependencies to specific commit hashes to reduce the risk of workflows referencing mutable tags. [commit](https://github.com/facebook/zstd/commit/1ec556238e08d377093d4445aebb5be42637abea)
- Pin dependency references in CircleCI and Docker build images to hashes to avoid base image dependencies changing with tags. [commit](https://github.com/facebook/zstd/commit/cd9486031dcb1cab5143d2c0c6edc34127d97a69)
- The Scorecards workflow upgrades the GitHub CodeQL action from 2.2.5 to 2.2.6. [commit](https://github.com/facebook/zstd/commit/e2965edd107acd0123294e23848cdc00af906468)
- CMake skips unreliable linker flag detection under MSVC and ClangCL to avoid using incorrect detection results for build options. [commit](https://github.com/facebook/zstd/commit/979b047114622265b6015a9587434e8229429411)
- GitHub Actions workflows upgrade the checkout action from 3.3.0 to 3.5.0. [commit](https://github.com/facebook/zstd/commit/4cf9c7e09810f6f0f41fba2d2b4c1d7998d990c5)
- The Scorecards workflow upgrades the GitHub CodeQL action from 2.2.6 to 2.2.8. [commit](https://github.com/facebook/zstd/commit/191d22994ffa470c17584d6c6d9a57c476c065b8)
- Short test CI adds a Clang-CL Windows build task to verify Windows code under that compiler frontend. [commit](https://github.com/facebook/zstd/commit/0f77956bccc3b95e0e7b51ef0d16ed1db695779b)

### Maintenance

- Rename the dictionary buffer loading function to `FIO_createDictBufferMMap()` to clearly distinguish the memory-mapped loading path from the normal allocation path. [commit](https://github.com/facebook/zstd/commit/cc4e9417457bd33c657a613095830f3a2700804d)
- patch-from mode can now use memory mapping for large dictionaries, avoiding copying the entire dictionary into a limited normal memory buffer. [commit](https://github.com/facebook/zstd/commit/4373c5ab88b733b482f2e51a209cea8966870901)
- The LZMA wrapper layer now uses buffer pointer and length types consistent with zlib type definitions, fixing type mismatches during compression and decompression. [commit](https://github.com/facebook/zstd/commit/886de7bc0404f856e6d05b6550d13424d8ad4fe9)
- Simplify the advanced file benchmark function and its CLI invocation, changing benchmark failures to a clear non-zero return status. [commit](https://github.com/facebook/zstd/commit/1e38e07b3d6e608361c36bcc4245471b6b03c570)
- Refactor the CLI dictionary object and add an option to disable memory mapping, allowing callers to manage dictionary buffers and choose mmap or normal allocation. [commit](https://github.com/facebook/zstd/commit/96e55c14f208d708922a7ef8e9e2dd03fc847274)
- Add a buffer type assertion after dictionary file loading to ensure subsequent processing receives a valid memory or mapped buffer. [commit](https://github.com/facebook/zstd/commit/70850eb72b4288874506589546cb30d0c80d6b58)
- When the file output target is empty, `setvbuf()` is no longer called, avoiding passing a null file pointer to standard I/O functions. [commit](https://github.com/facebook/zstd/commit/c4c3e11958aed4dc99ec22e3d31c405217575a8c)
- Clarify the `dstCapacity` requirement of the compression API, stating that providing a capacity not less than `ZSTD_compressBound()` guarantees enough space to write the compressed frame. [commit](https://github.com/facebook/zstd/commit/c40c7378c679dab6ab168f5153858226d101db04)
- Add seekable format documentation explaining the independent frame layout and how seeking and decompressing intermediate data in the archive works. [commit](https://github.com/facebook/zstd/commit/dd8cb5a0f1a7581c407a7307fc526deb47e1f266)
- Dictionary and LDM documentation clarify that the dictionary remains effective for subsequent compression or decompression in the same context until context parameters are reset or the dictionary is replaced; the prefix remains valid only for a single operation. [commit](https://github.com/facebook/zstd/commit/f4563d87b954768e5524e1b53bb5e5d607cef35d)
- The zstd manual supplements the impact of `--rsyncable` on compression ratio and speed, and notes that performance costs may be more noticeable under multithreading and high-speed compression. [commit](https://github.com/facebook/zstd/commit/35c0c2075ea831ee10fa08b09c93484f1b098000)
- The pzstd Makefile probes the latest C++ standard supported by the compiler and compiles with at least C++11. [commit](https://github.com/facebook/zstd/commit/1b8bddc41ea721d1ff8056280bbf62d3bb0da344)
- Fix redundant wording in the Ninja build command in the README so the example command matches the actual target. [commit](https://github.com/facebook/zstd/commit/c36d54f5ed74da651a4bcbbb3bc7128551339f76)
- pzstd only explicitly passes `-std=c++11` when the compiler's default standard is lower than C++11, avoiding overriding newer default standards. [commit](https://github.com/facebook/zstd/commit/cbe0f0e435e713091fa4741635dab97476e62983)
- Declare `BIT_reloadDStream()` as a forced inline function to reduce function call overhead in the bitstream decoding hot path. [commit](https://github.com/facebook/zstd/commit/e6dccbf48246f4e2844251972fcc0946a5de5154)
- Windows CLI adds memory-mapped loading support for large dictionaries and unifies dictionary buffer management into a single dictionary object. [commit](https://github.com/facebook/zstd/commit/b2ad17a658f9ac07ad624d8f17ee442ec8f9bc44)
- When seeking forward in seekable decompression, it only reads back if the target frame is earlier than the current frame or the target offset is earlier than the current decompression position, avoiding re-reading consumed frames. [commit](https://github.com/facebook/zstd/commit/618bf84e0d16070ac67a80b404041adb264c4952)
- Add unit tests for multiple consecutive decompression calls in seekable decompression, and use memory buffers to simulate file reading, writing, and seeking. [commit](https://github.com/facebook/zstd/commit/649a9c85c38195ff67065c02e207da9f8a342785)
- Cache the result of checking whether the output target is a regular file to avoid repeatedly calling `UTIL_isRegularFile()` on the same path during file processing. [commit](https://github.com/facebook/zstd/commit/14d0cd5d690ef0956a2e3085e81c78578f55b81e)
- Remove the obsolete Appveyor build status badge and its link from the README. [commit](https://github.com/facebook/zstd/commit/8eef3370a3c7c98cdac4e7311a7f078f6d564bad)

