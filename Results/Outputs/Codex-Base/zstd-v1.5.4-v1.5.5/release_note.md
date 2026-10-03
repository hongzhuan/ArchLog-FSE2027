# Release Note

## Important Changes

### API Abstraction Layer (Layer 1)

- Add ZSTD_setCParams(), ZSTD_setCLevel(), and ZSTD_setFParams() parameter setting helper functions. [commit](https://github.com/facebook/zstd/commit/07a2a33135a5f5fd99c7f69e7dc0147c6894d252)
- Clarify the capacity requirements for the compression target buffer. [commit](https://github.com/facebook/zstd/commit/c40c7378c679dab6ab168f5153858226d101db04)
- Mark bufferless and block-level compression/decompression interfaces as deprecated. [commit](https://github.com/facebook/zstd/commit/fbd97f305a521272601fe6394460287294c2406c)
- Explain the compatibility of LDM with dictionaries. [commit](https://github.com/facebook/zstd/commit/f4563d87b954768e5524e1b53bb5e5d607cef35d)
- Add fuzzing interface and examples for sequence production plugins. [commit](https://github.com/facebook/zstd/commit/a810e1eeb7ebc12d5a2c96f6dc3660cfc51c145d)

### Application and Integration Layer (Layer 3)

- Fix data types in LZMA compression and decompression. [commit](https://github.com/facebook/zstd/commit/886de7bc0404f856e6d05b6550d13424d8ad4fe9)
- Add utility function variants that accept an optional file descriptor. [commit](https://github.com/facebook/zstd/commit/a5a2418df4e41a826e87ef8ea2205fc2041ac0d2)
- Use an existing file descriptor to set output file status information. [commit](https://github.com/facebook/zstd/commit/f746c37d00ae7c4e921b9089e8bf1f87d34adcfb)
- Fix the assert definition in the Linux kernel contrib. [commit](https://github.com/facebook/zstd/commit/6313a58e45bb13c19664037a115862703b16b6f5)
- Use memory mapping to load large dictionaries in patch-from mode, with support for controlling whether mmap is enabled. [commit](https://github.com/facebook/zstd/commit/610c8b9e338466451b1e96ab5bcb9d88b6d3a1c1) [commit](https://github.com/facebook/zstd/commit/cc4e9417457bd33c657a613095830f3a2700804d) [commit](https://github.com/facebook/zstd/commit/4373c5ab88b733b482f2e51a209cea8966870901) [commit](https://github.com/facebook/zstd/commit/8a189b1b29c5e3a9946e6dcc0017b4e7c4738282) [commit](https://github.com/facebook/zstd/commit/2d8afd9ce14689b8db44ec0c07e55d5c4198fb69) [commit](https://github.com/facebook/zstd/commit/96e55c14f208d708922a7ef8e9e2dd03fc847274) [commit](https://github.com/facebook/zstd/commit/70850eb72b4288874506589546cb30d0c80d6b58)
- Simplify the synthetic data benchmark implementation. [commit](https://github.com/facebook/zstd/commit/db79219f70aa9b2bee9358ff95f1ba304a82e4bf)
- Simplify the file benchmark implementation. [commit](https://github.com/facebook/zstd/commit/1e38e07b3d6e608361c36bcc4245471b6b03c570)
- Avoid calling setvbuf() on null file pointers. [commit](https://github.com/facebook/zstd/commit/c4c3e11958aed4dc99ec22e3d31c405217575a8c)
- Improve data ingestion speed for the seekable format in small frame scenarios. [commit](https://github.com/facebook/zstd/commit/1df9f36c6c6cea08778d45a4adaf60e2433439a3)
- Add documentation for the seekable format. [commit](https://github.com/facebook/zstd/commit/dd8cb5a0f1a7581c407a7307fc526deb47e1f266)
- Make pzstd automatically select the highest available C++ standard. [commit](https://github.com/facebook/zstd/commit/1b8bddc41ea721d1ff8056280bbf62d3bb0da344)
- Only explicitly set -std=c++11 when the compiler's default standard is lower than C++11. [commit](https://github.com/facebook/zstd/commit/cbe0f0e435e713091fa4741635dab97476e62983)
- Add memory mapping support in Windows file I/O. [commit](https://github.com/facebook/zstd/commit/b2ad17a658f9ac07ad624d8f17ee442ec8f9bc44)
- Avoid repeated frame reads when seeking forward in seekable decompression. [commit](https://github.com/facebook/zstd/commit/618bf84e0d16070ac67a80b404041adb264c4952)
- Add tests for multiple calls to the seekable decompression interface. [commit](https://github.com/facebook/zstd/commit/649a9c85c38195ff67065c02e207da9f8a342785)

### Cross-cutting / Other Architecture-related Changes

- Set default permissions for GitHub Actions workflows to read-only. [commit](https://github.com/facebook/zstd/commit/727d03161f689399b7f6dbd65cd624185bf4de8c)

### Core Compression Engine (Layer 0)

- Fix rare data corruption that could be caused by the block splitter. [commit](https://github.com/facebook/zstd/commit/395a2c54621d36b4eaf17b4111353243f91a1d90)
- Initialize the compression level of static CDict. [commit](https://github.com/facebook/zstd/commit/988ce61a0c019d7fc58575954636b9ff8d147845)
- Halve the memory usage of the RowHash tag table. [commit](https://github.com/facebook/zstd/commit/33e39094e7d6680544290a41ff8f8aa34517bc1f)
- Fix the issue where RowHash mistakenly treated position 0 as a match position. [commit](https://github.com/facebook/zstd/commit/a91e91d61412e0a83e370028d62e7a58dfa85bd0)
- Optimize RowHash table reset using once-initialized workspace memory. [commit](https://github.com/facebook/zstd/commit/9420bce8a491e21821c4b372f837bf4bd47e5870)
- Add salt to the RowHash hash and supplement bit rotation helper functions. [commit](https://github.com/facebook/zstd/commit/91f4c23e634a1d260f290f00b6d870a56cd59ab6)
- Optimize patch-from dictionary loading speed. [commit](https://github.com/facebook/zstd/commit/53bad103ce61fd2c170bf49bf335201a8a51f72f)
- Allow the lazy matcher to quickly skip incompressible data to improve compression speed for such input. [commit](https://github.com/facebook/zstd/commit/a3c3a38b9b956d2689a019b1b29482e86fd98836)
- Fix window update logic during dictionary loading. [commit](https://github.com/facebook/zstd/commit/3e0550ee5279735693b01464ede7cb1ec22fe6b7)
- Inline the BIT_reloadDStream() implementation. [commit](https://github.com/facebook/zstd/commit/e6dccbf48246f4e2844251972fcc0946a5de5154)
- Remove branch hints in the decoding sequence path that were only for Clang. [commit](https://github.com/facebook/zstd/commit/b558190ac76fe6b0f2c42ae5fb9d2f90652d21b0)
- Check the validity of the decompression target buffer and add fuzzing coverage. [commit](https://github.com/facebook/zstd/commit/fcaf06ddb489f683afb1af3639727991fd9accae)
- Fix a potential out-of-bounds read when decompressing skippable frames. [commit](https://github.com/facebook/zstd/commit/e4120c55130656c213c09007c02ece544d66ffc1)

## Routine Changelog

### Bug Fixes

- Fix the issue where fullbench skipped the second file when testing two input files consecutively. [commit](https://github.com/facebook/zstd/commit/4b9e3d11a67e6cea2fb137e5a564925306f9231f)
- Fix the internal benchmark in the zlib wrapper. [commit](https://github.com/facebook/zstd/commit/9efc14804eaa6aa56514a17cabd07c0d73235892)
- Fix sparse file handling when decompressing output to block devices, and avoid repeated checks of the target file type. [commit](https://github.com/facebook/zstd/commit/5bf1359e3be0e64149bbb989f2addfc42adf30d3) [commit](https://github.com/facebook/zstd/commit/14d0cd5d690ef0956a2e3085e81c78578f55b81e) [commit](https://github.com/facebook/zstd/commit/2e29728797c49db1f4e7bfbd52ef9d7ae45d5851)

### Refactoring

- Simplify line splitting logic in CLI test tools. [commit](https://github.com/facebook/zstd/commit/3b001a38fea0a78e6d6a9ce73f9c0ab9459d6341)

### Tests

- Add CI workflow checks for external compressor dependencies. [commit](https://github.com/facebook/zstd/commit/6a86db11a4cafabbbbb56c2ae39881774b52d43f)
- Fix tests related to CLI window size adjustment. [commit](https://github.com/facebook/zstd/commit/7da1c6ddbfe61ad2f9bc9c3a2205567a76be24f5)
- Fix CLI test compatibility under Python 3.6. [commit](https://github.com/facebook/zstd/commit/50e8f55e7d5928af9c3411afdb4fbedb4d8f770d)
- Add CLI file operation tests in directories without write permissions. [commit](https://github.com/facebook/zstd/commit/957a0ae52d0f49eccd260a22ceb5f5dfed064e9f)
- Fix type mismatch between Python bytes and integers in CLI tests. [commit](https://github.com/facebook/zstd/commit/29b8a3d8f2bdd26d6952d5bdb62708aab591e1ae)
- Increase CLI test timeout. [commit](https://github.com/facebook/zstd/commit/b7080f4c67bdb9d190bda529f7309e34fb990b23)

### Security

- Upgrade GitHub CodeQL Action. [commit](https://github.com/facebook/zstd/commit/6894746eb1cf218c045627bac8b21e448754ac1b)
- Fix permissions for the release artifact upload task. [commit](https://github.com/facebook/zstd/commit/d54ad3c234cb154a581d6e91a6010e900311b55e)
- Upgrade GitHub CodeQL Action. [commit](https://github.com/facebook/zstd/commit/1be95291a89160be121c987c2e385331a65a4a0e)
- Pin more GitHub Actions dependencies to specific versions. [commit](https://github.com/facebook/zstd/commit/1ec556238e08d377093d4445aebb5be42637abea)
- Pin dependencies in the Dockerfile to specific commit hashes. [commit](https://github.com/facebook/zstd/commit/cd9486031dcb1cab5143d2c0c6edc34127d97a69)
- Upgrade GitHub CodeQL Action. [commit](https://github.com/facebook/zstd/commit/e2965edd107acd0123294e23848cdc00af906468)
- Upgrade GitHub Actions checkout action. [commit](https://github.com/facebook/zstd/commit/4cf9c7e09810f6f0f41fba2d2b4c1d7998d990c5)
- Upgrade GitHub CodeQL Action. [commit](https://github.com/facebook/zstd/commit/191d22994ffa470c17584d6c6d9a57c476c065b8)

### Documentation

- Clarify Huffman block and stream size descriptions in the zstd format specification. [commit](https://github.com/facebook/zstd/commit/832f559b0b9d22f3afc6b6e11a55044b9a238db5)
- Add format descriptions for Huffman compressed blocks and stream sizes. [commit](https://github.com/facebook/zstd/commit/64e8511b267e48b8c796ae70d41f3e7fe16a28d5)
- Add manual description for --rsyncable. [commit](https://github.com/facebook/zstd/commit/35c0c2075ea831ee10fa08b09c93484f1b098000)
- Add instructions for building Universal2 universal binaries on macOS via CMake. [commit](https://github.com/facebook/zstd/commit/408bd1e9fe8c7dc52b45b3879b0c03d034f51bec) [commit](https://github.com/facebook/zstd/commit/82cf6037ac28042f82bc0bc44188f51177126b43)

### Build / CI

- Add and organize MinGW-based Windows x64 build and artifact generation workflows. [commit](https://github.com/facebook/zstd/commit/f37b291bf56a7b2ba38deb82332aa9f6555d9c3f) [commit](https://github.com/facebook/zstd/commit/43bc470fe0ea6cb188118e27f92b9071d30371a9) [commit](https://github.com/facebook/zstd/commit/5be3f19e1d5745e50dc42c57aeda35e977de39de) [commit](https://github.com/facebook/zstd/commit/f8ae21680f06112c509cdf474e97b6e96634a776)
- Fix multiple MSVC warnings. [commit](https://github.com/facebook/zstd/commit/a7de1d9f4954a1a7f8b15ecc1eff6a249dd9b4f6)
- Complete dependencies required for zstd-dll build. [commit](https://github.com/facebook/zstd/commit/c78f434aa4f5f1097c8edb975f4c1635817a5a71)
- Add 32-bit make test in long-running CI. [commit](https://github.com/facebook/zstd/commit/d3d0b92e5e64e1f1b32aa58679d9c74f3ded0abe)
- Lower the minimum required CMake version. [commit](https://github.com/facebook/zstd/commit/8420502ef9d5980d2297c88f80d19ae18f84f6df)
- Fix Meson playtests dependency declaration. [commit](https://github.com/facebook/zstd/commit/183a18a45c1d69f8c42b9fcd25e6d28f9b3d75bb)
- Ensure zstd executable is built when tests are enabled. [commit](https://github.com/facebook/zstd/commit/97ab0e2ab60fdda78f610032408df104de20b9f1)
- Disable linker flag probing that is not applicable under MSVC/ClangCL. [commit](https://github.com/facebook/zstd/commit/979b047114622265b6015a9587434e8229429411)
- Add Clang-CL Windows tests in CI. [commit](https://github.com/facebook/zstd/commit/0f77956bccc3b95e0e7b51ef0d16ed1db695779b)
- Adjust naming and directory structure of Windows release artifacts. [commit](https://github.com/facebook/zstd/commit/fcaa4228974870bd873130681c29ed140d5c1c39)

### Maintenance

- Fix typos in code and CLI test output. [commit](https://github.com/facebook/zstd/commit/547794ef400832bcb7ebfee2784eb28f5ec6344c)
- Update README content. [commit](https://github.com/facebook/zstd/commit/c36d54f5ed74da651a4bcbbb3bc7128551339f76)
- Remove Appveyor status badge. [commit](https://github.com/facebook/zstd/commit/8eef3370a3c7c98cdac4e7311a7f078f6d564bad)

