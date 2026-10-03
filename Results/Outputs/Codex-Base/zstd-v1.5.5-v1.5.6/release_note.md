# Release Note

## Important Changes

### Core Compression Engine


- Improve the price update and path selection logic of the optimal parser to enhance high compression ratio performance for specific file inputs. [commit](https://github.com/facebook/zstd/commit/de10f56be2765e8375939b97bb27ad3e378f217f) [commit](https://github.com/facebook/zstd/commit/4683667785c6248a20eba83dd192dc9baea70d84) [commit](https://github.com/facebook/zstd/commit/0166b2ba8083481df3ae68e3431a43f541d3c9bd) [commit](https://github.com/facebook/zstd/commit/d31018e223691256aac9c426fcfbeec735a2d6ab) [commit](https://github.com/facebook/zstd/commit/8168a451e58261baf9a53b0c1bcfdaff2ba0480d) [commit](https://github.com/facebook/zstd/commit/e5af24c5fa82186d61ee1ed4dfe161d65a1c1a7d)

- Improve the price update and path selection logic of the optimal parser to enhance high compression ratio performance for specific file inputs, and update regression results and related tests. [commit](https://github.com/facebook/zstd/commit/9ae3bf5ee2ea676594b84afc6a3a4edcc22a19bf) [commit](https://github.com/facebook/zstd/commit/5474edbe6016175453d09eca139566baefe0b97b) [commit](https://github.com/facebook/zstd/commit/0ae21d8c3170741e4005c877d3c300a6034601ec) [commit](https://github.com/facebook/zstd/commit/fe2e2ad36d434d0989ca669d3a4f4d60f1cb907b) [commit](https://github.com/facebook/zstd/commit/641749fc0935b6905b2fcfaa362cedfc631f5960) [commit](https://github.com/facebook/zstd/commit/6c35fb2e8cb826b70226856cd7442861037cca8a) [commit](https://github.com/facebook/zstd/commit/887f5b62aea77ec26a1a693ff9d8e2b1eba3a2cd) [commit](https://github.com/facebook/zstd/commit/b88c593d8ff79b96390308380604f232802e0f04)

- Add targetCBlockSize target block size control and benchmark options, and improve sub-block splitting strategy; fix issues with incompressible sections, long sequences, and partial-block paths, and improve regression tests and API documentation. [commit](https://github.com/facebook/zstd/commit/68a232c5917ff387031c76acea80f77e8115419f) [commit](https://github.com/facebook/zstd/commit/cc4530924b42c5d138f871c33726d374e2778ad3) [commit](https://github.com/facebook/zstd/commit/6b11fc436c3001cb9beb07627e7b434aab97b4b1) [commit](https://github.com/facebook/zstd/commit/3b401000580a3e605694055834dcd254fa36202e) [commit](https://github.com/facebook/zstd/commit/0591e7eea118eccb6b8ceef00296bedaad3d7e9e) [commit](https://github.com/facebook/zstd/commit/6719794379ada9cc33cae486a6fea4930eda481c) [commit](https://github.com/facebook/zstd/commit/4b5152641239c571ae6cd67ae74cc87776e21362) [commit](https://github.com/facebook/zstd/commit/f77f634d41149c3e5754ebfe4d5cf3a5f138c843) [commit](https://github.com/facebook/zstd/commit/f8372191f595f112ba13445205cf46997da67350) [commit](https://github.com/facebook/zstd/commit/038a8a906b8bbf60491b2643febaf8f9d5a4139c) [commit](https://github.com/facebook/zstd/commit/1fafd0c4ae56a524a92369c065d616a447a21a0f) [commit](https://github.com/facebook/zstd/commit/e0412c20625c7358d506c969a9c9861b70eb10ee) [commit](https://github.com/facebook/zstd/commit/aa8592c532e1a2b30b08763140b9bd66bdce4f83) [commit](https://github.com/facebook/zstd/commit/ef82b214ad1023f6123c3d9c9a7dbce24130d9bd) [commit](https://github.com/facebook/zstd/commit/86db60752d1f813642054d12d704663c7757d434) [commit](https://github.com/facebook/zstd/commit/d23b95d21d5cb9c5378b3537271dbbff7cdb49b7) [commit](https://github.com/facebook/zstd/commit/8d31e8ec42a736bf7cc70f9f21e9c1afc920c148) [commit](https://github.com/facebook/zstd/commit/3613448fb8623361dc6bd9b32c8d4b3d2da85823) [commit](https://github.com/facebook/zstd/commit/f5728da365e14a715a131434847f732ee84d8719) [commit](https://github.com/facebook/zstd/commit/6f1215b874dbf74b50dcb64915e91e11ba198008)

- When decompressing multi-frame data, verify that the content size declared in the frame header matches the actual decompressed size, and report corruption on mismatch; cover this interface in the simple_decompress fuzz test. [commit](https://github.com/facebook/zstd/commit/f65b9e27ce0b6e4ed096126659021359d004d1ab)

### Advanced Features


- Fix the sequence producer callback type and include offload API parameters in the CCtx parameter object; subsequently make this API usable for static CCtx. [commit](https://github.com/facebook/zstd/commit/809c7eb6bff1934745b425437d2116d9c0dbe0df) [commit](https://github.com/facebook/zstd/commit/d151a4880bdcb15d10ed11136b8b7d8d3d66af2c) [commit](https://github.com/facebook/zstd/commit/c6cabf94417d84ebb5da62e05d8b8a9623763585)

### Tools & Applications


- CLI provides more specific error output for invalid parameters and displays relevant parameter information in error scenarios. [commit](https://github.com/facebook/zstd/commit/8052cd0131a4f483ef14be3e564530c07ea382f5)

- In patch mode, lower the default output level for automatically enabling long mode and optimal parser tuning instructions. [commit](https://github.com/facebook/zstd/commit/1f87c88ecf3814ef59fa514dd7fe3522d2d400b1)

- Use explicit character arrays to construct short option error text, removing the CLI error path's dependency on sprintf. [commit](https://github.com/facebook/zstd/commit/4d2bf7f0f2feb2c6928204db218ff9384ac605ac)

- Update the option priority description for CLI -c/--stdout and -o; --stdout no longer automatically cancels --rm, and the manual synchronizes the behavior description. [commit](https://github.com/facebook/zstd/commit/c610a01d7dbe0e6586f94bfb5f8b540a2f28b1c5) [commit](https://github.com/facebook/zstd/commit/fbd9e628ae124d4bbf4db0b8afd54b6b6e653b29) [commit](https://github.com/facebook/zstd/commit/1362699e875994689390bbee3cba87d2c11a11fb)

- Expand the list of compressed file extensions for CLI --exclude-compressed to cover more common media, archive, and application package formats. [commit](https://github.com/facebook/zstd/commit/5a66afa0514d0853b0f2a6b5ff3df1ae706f4862)

- In verbose mode, display full file names; only non-verbose output continues to truncate long file names. [commit](https://github.com/facebook/zstd/commit/83ec3d0164887904a7ae7f3382051ed20d5792b2)

### Compatibility & Legacy


- Fix the conditional check for x86/x64-specific _mm_prefetch in MSVC ARM64EC builds. [commit](https://github.com/facebook/zstd/commit/1b994cbc57869cc73e6434acb639aab648fcc678)

- Change the 64 bit suffix of the ZSTD_MAX_INPUT_SIZE constant from LLU to ULL for compatibility with older Visual Studio compilers. [commit](https://github.com/facebook/zstd/commit/94a2f2791f313d27b6a2c0293971954cdd66035b)

- Fix attribute/bounds check declarations in the FORCE_INLINE bitstream function helper implementation to avoid inappropriate inline attribute issues. [commit](https://github.com/facebook/zstd/commit/74c901bbedd4584190f0cd93d573cf7e014b76d1)

- Fix the potential duplicate definition of the MEM_STATIC macro in Linux kernel integration. [commit](https://github.com/facebook/zstd/commit/d9645327b3b6d18b04ac1dd0bc4346a2af87bb9b)

- Enable .private_extern visibility declarations for assembly functions on Apple platforms. [commit](https://github.com/facebook/zstd/commit/b1a30e2b4a69e6fcca9c2a6f9d4e43e8e3b243c8)

- Add the _QNX_SOURCE marker for QNX to POSIX platform recognition conditions. [commit](https://github.com/facebook/zstd/commit/839c7939e825d9a6a24eea4122b5cfd4ab8b5243)

- Unify Windows platform conditions to use the standard _WIN32 macro, removing dependency on the WIN32 alias. [commit](https://github.com/facebook/zstd/commit/585aaa0ed324a858226908fc1f00d78ed92b0f4b)

- In Linux kernel adaptation, remove the duplicate definition of intptr_t and use the type definition already present in common dependencies. [commit](https://github.com/facebook/zstd/commit/a419265d30f4fa05caa8df0b12fac1ce2558ec6a)

- The Linux kernel decompression module now uses ZSTD_DCtx_reset(..., ZSTD_reset_session_only) to reset stream state. [commit](https://github.com/facebook/zstd/commit/c2d470581eaee3dc9f747dbab16d1fc0816f94aa)

- Linux kernel builds no longer define g_debuglevel, which is only used at higher DEBUGLEVEL, avoiding pedantic warnings for empty translation units. [commit](https://github.com/facebook/zstd/commit/e122fcbf58e142e837a2bba382ef7ca4f5eaa13b)

- Change the 64-bit integer constant suffix in test code to ULL for better compatibility with older compilers. [commit](https://github.com/facebook/zstd/commit/2abe8d63e06f0e7c9adacd50855a05023e51f1e0)

- Fix xxHash build on AIX 5.1 by using the inttypes.h provided by that platform. [commit](https://github.com/facebook/zstd/commit/66269e74a00e531a5f27fcb4fd65eb061d02dc5c)

- BSD platforms are no longer hardcoded to a specific POSIX version; instead, other platform capability checks handle it. [commit](https://github.com/facebook/zstd/commit/f99a450ca4d5fdb25d0d9bc5ae4c5d4787fbcb87)

- Fix the issue where CPUID inline assembly under Windows Clang clobbers the RBX reserved register. [commit](https://github.com/facebook/zstd/commit/94c102038b81ed89e3b013cb1977496612609f85)

- Mark BTI and PAC support for AArch64 assembly and enable corresponding protection parameters in QEMU RISC-V/AArch64 CI configurations. [commit](https://github.com/facebook/zstd/commit/ff0afbad58611d22b8b4477e9383b9b9ffdbaee6)

- FreeBSD file timestamp handling now uses utimensat(). [commit](https://github.com/facebook/zstd/commit/d6ee2d5d2454f5023c78d59e7464c9c902d6597b)

## Routine Changelog

### New Features


- Add decompression parameter ZSTD_d_maxBlockSize to limit the maximum block size accepted by the decoder, and include it in parameter bounds, get/set interfaces, and decompression buffer calculations. [commit](https://github.com/facebook/zstd/commit/61efb2a047b308b6f0c265e1eae9ca8a062268e4)

- Add a lorem ipsum data generator for generating synthetic text input in benchmarks. [commit](https://github.com/facebook/zstd/commit/d0b7da30e26406c7ece2bf538a70410e80b9de9f)

- Expand the vocabulary and runtime weight distribution of the lorem ipsum synthetic text generator, and make datagen generate lorem text by default; benchmark tools support selecting synthetic sample sizes. [commit](https://github.com/facebook/zstd/commit/1e046ce7fa6ebabb48a182009df6e4fe90fa2740) [commit](https://github.com/facebook/zstd/commit/40874d4aea44bc9e1efd2ce14b98ea19d1d2e42d) [commit](https://github.com/facebook/zstd/commit/5a1bb4a4e0aaba722e57cdca46486bc3c6d7e457) [commit](https://github.com/facebook/zstd/commit/3dbd861b7dc05bc4291f9de222e397e50fb4c32b) [commit](https://github.com/facebook/zstd/commit/7003c9905e0c80aafe00ef485e586f859707c04c) [commit](https://github.com/facebook/zstd/commit/83598aa106ba0edaa8b449b2fe5d63773eeebc4e) [commit](https://github.com/facebook/zstd/commit/7a225c0c465149f1a72811dab669985b6ea5e5f4) [commit](https://github.com/facebook/zstd/commit/1e240af30a1d11ae45745c6c3e96307bad3771fd)

- Support one-shot size query fallback for magicless format, and fix and fuzz test the magicless decoding path. [commit](https://github.com/facebook/zstd/commit/7d970bd83c2323c5e78b4f15ae850373c70f055d) [commit](https://github.com/facebook/zstd/commit/741b87bbe1c7c7e7292742f3b1ed9c4055c4743c)

- Fix and strengthen the ZSTD_generateSequences sequence generation API, adding multithreaded path and fuzz test coverage. [commit](https://github.com/facebook/zstd/commit/731f4b70fcd22fc9badd4e51dc6d939ee6da6c54)

### Bug Fixes


- Avoid pointer rollback when the input pointer is null in stable input stream processing, fixing the UBSAN-reported null pointer zero offset issue. [commit](https://github.com/facebook/zstd/commit/d01a2c69296cff9bd052b797b2be1055a96cd644)

- Fix the educational decoder's handling of the offset state of the last sequence. [commit](https://github.com/facebook/zstd/commit/5108c9ac975b5e4ff62418584cc6c8934d747b38)

- Fix the decoder incorrectly reading the FSE table when the sequence count is zero and that value is encoded with two bytes. [commit](https://github.com/facebook/zstd/commit/3732a08f5b82ed87a744e65daa2f11f77dabe954)

- The decoder now rejects extra bytes in the Sequences section that are not consumed by decoding, and adds corresponding error sample tests. [commit](https://github.com/facebook/zstd/commit/b46236278a0adea097ce7792824f93a678a74069) [commit](https://github.com/facebook/zstd/commit/b39c76765b761c9c3c3c23db3ed55f3f825f7e4d) [commit](https://github.com/facebook/zstd/commit/0ae98ba2155154dfdea253fef5876ec23fa26a86) [commit](https://github.com/facebook/zstd/commit/37ff4f91eba72a936771b177c83d27151d33e2f1)

- Fix out-of-bounds handling in bitstream reads so that overflow generates zero-value bits; affects both new and legacy decoding implementations. [commit](https://github.com/facebook/zstd/commit/ba508070299b4ab7ae1e22b659557489122cdcd7)

- Fix thread handle initialization and null parameter checks in the Win32 pthread wrapper, and add assertions for mutex/condition variable initialization and destruction. [commit](https://github.com/facebook/zstd/commit/e4aeaebc201ba49fec50b087aeb15343c63712e5)

- The external sequence interface no longer returns misleading parameter errors when LDM is enabled but the sequence count is zero; related preconditions are changed to assertions. [commit](https://github.com/facebook/zstd/commit/c6a888c073a0a6693026e67e8db3813ba6b78850)

- Initialize the stat structure in fileio to fix build failures when LTO is enabled. [commit](https://github.com/facebook/zstd/commit/de6b46dfc80d950a32176c7eca79bb229d47f501)

- When the async read pool fails to allocate a coalesce buffer, an explicit memory allocation error is now thrown. [commit](https://github.com/facebook/zstd/commit/4d267f3d4f9f85eecf98d1a2353408b8e840f1a3)

- The decompression dictionary is no longer incorrectly rejected because the maxSymbolValue of literals is less than 255; zero-weight validation is now limited to the full symbol range. [commit](https://github.com/facebook/zstd/commit/bd02c9be6e3708c6dd53f4df1f4dc13d29441e89)

- Fixed the export declaration of the dictionary training function to use ZDICTLIB_STATIC_API, consistent with header prototypes/build visibility configuration. [commit](https://github.com/facebook/zstd/commit/ecb86d82868d60517453151127b229c96ff89fec)

- Huffman fast decoding now returns directly when the target length is zero, avoiding pointer arithmetic on a null target pointer. [commit](https://github.com/facebook/zstd/commit/dd4de1dd7a78ccff933025cf1de08a75d310802b)

- ZSTD_createCDict_advanced2() no longer dereferences a null pointer when advanced dictionary creation fails and returns NULL. [commit](https://github.com/facebook/zstd/commit/9a3b17c4d61f00e22997d946f422533564812fe3)

- Fixed an issue in the optimal parser triggered by specific inputs. [commit](https://github.com/facebook/zstd/commit/22574d848df09616d07fe26b363700525cb9cce9)

- Fixed a fuzz issue caused by the optimal parser. [commit](https://github.com/facebook/zstd/commit/b0e8580dc7f71881361f3a6fe46841af9d70bedf)

- The decoder now rejects corrupted zstd data where the reserved bits of the sequence section are non-zero. [commit](https://github.com/facebook/zstd/commit/468bb173782115e7bd2704f3a9e82341912eebd4)

- Clarified that offset 0 is an invalid value; the decoder now converts this case into a subsequently detectable corrupted state, and added golden error samples and regression tests. [commit](https://github.com/facebook/zstd/commit/f06b18b3ff009ef7dc90294fca674658ddf139bf) [commit](https://github.com/facebook/zstd/commit/a9fb8d4c41bf3cc829adf20aea3768863d03cd0d) [commit](https://github.com/facebook/zstd/commit/d2f56ba44208f56b5370a9ef6ce0d2c32f283131) [commit](https://github.com/facebook/zstd/commit/eb5f7a7fa278ab76c3390555f36162c638f63b53)

- Fixed loop handling when AsyncIO reads the seed queue. [commit](https://github.com/facebook/zstd/commit/edab9eed66f02c7c3c8be849f22f20ffbd04976b)

- Fixed --output-dir-mirror incorrectly excluding hidden files and directories, and added directory mirror regression tests. [commit](https://github.com/facebook/zstd/commit/2215101cad9d809e345e2e939fa1e125563d25cf) [commit](https://github.com/facebook/zstd/commit/86b8e39a84d15ebcae3fa4b36240db27f2ae74ac)

### Refactoring


- The compression library build can now exclude block compressor implementations based on policy; the policy avoids uncompiled implementations and errors on unsupported parameter combinations, with corresponding adjustments to declarations, function tables, and tests. [commit](https://github.com/facebook/zstd/commit/cbf3e263160e0bfc9499f55f34c3759a14c0c1cc) [commit](https://github.com/facebook/zstd/commit/81b86a2024c80c1fc69bb6a76407628e063917ed) [commit](https://github.com/facebook/zstd/commit/50cdf84f58e1d8f989877db453fdfe9d63c1925e) [commit](https://github.com/facebook/zstd/commit/5a75956001efbde704eedad755daae2816273a74) [commit](https://github.com/facebook/zstd/commit/16bbd7437cf67a748ac22349a3ff974a518a3d66) [commit](https://github.com/facebook/zstd/commit/6761e1c949b99050f79a90a333c3432ba7cf3f22) [commit](https://github.com/facebook/zstd/commit/b12e8cb3e73c2eb0d176eb9b4dd0ff943b766242) [commit](https://github.com/facebook/zstd/commit/39b7946b95dc4359d7a9546ede906489682dd0d9) [commit](https://github.com/facebook/zstd/commit/f242f5be8f0d57fb9b49f22f35032953072471cc) [commit](https://github.com/facebook/zstd/commit/b7add1dd67f24124f2ebc722effb322fb77ee92b) [commit](https://github.com/facebook/zstd/commit/d09f195ceb774bc0b3b7c764ddb907bc3de8c69e) [commit](https://github.com/facebook/zstd/commit/eb9227935ead3eff349dcdde296543ff097deae0)

- Reorganized lazy and optimal parser function definitions according to compressor exclusion macros, aligning each implementation with conditional compilation boundaries. [commit](https://github.com/facebook/zstd/commit/59c7b2a49247de8d2335e3a492135e9396ce8e84) [commit](https://github.com/facebook/zstd/commit/1b65803fe7f506f5551d3946dc74f9fef8b87f71)

- Refactored the split-literal decoding sequence flow: unified the sequence decoding loop and adapted the long-offset path. [commit](https://github.com/facebook/zstd/commit/02134fad123a26e17bcb48edc2868b5968ed76d5) [commit](https://github.com/facebook/zstd/commit/84e898a76c50aa31bd05b37a370c674250706254) [commit](https://github.com/facebook/zstd/commit/33fca19dd4b8cc9d68feb3daa129297b31680e47) [commit](https://github.com/facebook/zstd/commit/c60dcedcc91da9bb7550f237f79ee001ca6d1a75)

- Adjusted the position of workspace helper functions in the header file for better implementation organization. [commit](https://github.com/facebook/zstd/commit/5f5bdc1e5d23544391df1c47cec3a69b96a09f5b)

- Refactored Huffman dictionary duplicate table handling and added a header information interface to read tableLog and maxSymbolValue from CTable. [commit](https://github.com/facebook/zstd/commit/396ef5b434e5e7f15773a7495f374a99a6377778)

- Removed the single-element trailing array allocation pattern for multithreaded compression contexts and buffer pools, replacing it with separate array allocations and corresponding frees. [commit](https://github.com/facebook/zstd/commit/e8ff7d18ebdb7af55ad73f92c5192e74bdc85ca2) [commit](https://github.com/facebook/zstd/commit/c87ad5bdb59c95c16871ff99d83ec3b09bd742c8) [commit](https://github.com/facebook/zstd/commit/ea4027c003d31bb75d24a2284d06ed4c06300f59) [commit](https://github.com/facebook/zstd/commit/6bb1688c1a13a9368d7c1b6f992e0a0fa7c1cbba)

- Adjusted FSE decoding table definitions and related integer conversions to avoid relying on existing flexible array/type layout methods. [commit](https://github.com/facebook/zstd/commit/d988e00a7fe551785bc8c3de8cd5e4266280ce6d) [commit](https://github.com/facebook/zstd/commit/24dabde507c8d141e282e568be21e648987a7d77)

- Changed multiple internal macros to the do { ... } while (0) form to reduce expansion risks in conditional statements. [commit](https://github.com/facebook/zstd/commit/8193250615f56ace446a3bf963d195f9f33fa9a9)

- zlibWrapper examples and implementation now use C89/ANSI C function definition style. [commit](https://github.com/facebook/zstd/commit/2ce0290e4d745846f03956be238596929de88768)

- Reduced the scope of local variables in multiple functions. [commit](https://github.com/facebook/zstd/commit/b921f1aad67cfc347ea7f8ef1c0afb6688bad4b6)

- Reduced indirect dependencies of the dictBuilder cover header and explicitly included dependent headers at actual usage sites. [commit](https://github.com/facebook/zstd/commit/c8ab027227536a543efd1b7bea04aabf9e97accf)

### Tests


- Fixed the OSS-Fuzz simple_round_trip test's calculation of decompression margin in overlapping decompression scenarios to consider maxBlockSize. [commit](https://github.com/facebook/zstd/commit/e72e13ac6c1dc373a0826df0de6f9bf13ee02ee4)

- Added a golden decompression sample for 128 KB compressed blocks and referenced it in the errata documentation. [commit](https://github.com/facebook/zstd/commit/0d6954b4cc309b430dd010dbeb20b112e7092644)

- Added explicit initialization for the sequence variable in split-literal decoding to eliminate false positives from static analyzers. [commit](https://github.com/facebook/zstd/commit/c123e69ad087cea5b779ce2a26b0845810783d12)

- Fixed the execution prefix variable name used by playTests.sh so that test wrapper reads and writes are consistent. [commit](https://github.com/facebook/zstd/commit/e99d554903643e8dda22d664bbba62e8a9d5b0b0)

- fullbench adds a ZSTD_decompressDCtx benchmark option. [commit](https://github.com/facebook/zstd/commit/a07d7c4e29f9329a1c98fbecc2e54ed6b663caef)

- Stopped suppressing pointer-overflow errors in UBSAN test commands and added required standard type declarations. [commit](https://github.com/facebook/zstd/commit/43118da8a7fb51e660bfa7e958639c5cc8285580)

- Fuzz builds can now explicitly control debuglevel via the Makefile. [commit](https://github.com/facebook/zstd/commit/695d154cac251c4ae2e2a438af21f0455a4c4149)

- Test builds enable ZSTD_LEGACY_SUPPORT=5 and use separate context type names for legacy v0.2/v0.3 decoders. [commit](https://github.com/facebook/zstd/commit/e0872806df5c255d23c9c9ec95fb7db50127a9e6) [commit](https://github.com/facebook/zstd/commit/92fbd42894e4dd9d58d3184923b17dda94ca6b44)

- Added multithreaded compression tests covering default, single-worker, dual-worker, and multi-worker configurations. [commit](https://github.com/facebook/zstd/commit/74e856a195005c2358b5fb4d6c90c540c5b29812)

- Fixed the expected decompressed size type in the simple_decompress fuzzer and enabled the corresponding static API declaration. [commit](https://github.com/facebook/zstd/commit/6a0052a409e2604bd40354b76b86272b712edd7d)

- Fuzzer builds now enable -Werror by default and only disable error handling for specific compatibility warnings. [commit](https://github.com/facebook/zstd/commit/3487a60950ea01e89883a3e807a18a6e155768b7)

- Fixed void pointer arithmetic warnings in the cross-format fuzzer by using byte pointers for buffer offsets. [commit](https://github.com/facebook/zstd/commit/dc1f7b560b23f5bd50a0fcddd677007c9c76ec0b)

### Performance


- The streaming decompression path reduces buffer overhead by about 128 KB and adjusts the minimum decoding buffer size calculation accordingly. [commit](https://github.com/facebook/zstd/commit/0abf2baef925fed4dac13d551c35d817e3206fdd)

- Fixed the boundary check for superblock sequence count encoding so that 128 sequences use the two-byte format, and updated the format specification and corpus test generator accordingly. [commit](https://github.com/facebook/zstd/commit/1f83b7cfc459c2dbef00dc6276f790370e17aef6)

- The frame end empty block write is changed from 4 bytes to 3 bytes, outputting according to the actual block header length, saving 1 bytes. [commit](https://github.com/facebook/zstd/commit/55ff3e4e17ea42a7c3726e51945c483a18d8c4c8)

- Adjusted the fast Huffman decoding implementation and added the HUF_DISABLE_FAST_DECODE build macro to disable the fast path on platforms where it is not suitable. [commit](https://github.com/facebook/zstd/commit/c7269add7eaf028ed828d9af41e732cf01993aad)

- Optimized the C and x86-64 assembly fast Huffman decoding paths for small data. [commit](https://github.com/facebook/zstd/commit/5ab78c0418dd2b77e76e8350a563b9771a424b27)

- By default, prevent the compiler from auto-vectorizing the XXH64 loop in AVX-512 builds; this behavior can be explicitly enabled via a macro. [commit](https://github.com/facebook/zstd/commit/007cda88ca1c7819eec966ce030934756d33c8c1)

### Security


- In MemorySanitizer builds, unpoison the workspace buffer before calling custom free functions. [commit](https://github.com/facebook/zstd/commit/9987d2f5942a7701b388eec4307be71a121e5652)

- Added SECURITY.md explaining how to report vulnerabilities and publishing channels for subscribing to security vulnerability notifications. [commit](https://github.com/facebook/zstd/commit/b6805c54d67f902d32afecc5ca153cd81a77764f) [commit](https://github.com/facebook/zstd/commit/e13d099bf881d69d6cf8bcd5cd4f677e1ce86bea)

- Commit and nightly workflows set read-all permissions, clarifying their read-only access scope to eliminate Scorecard permission warnings. [commit](https://github.com/facebook/zstd/commit/273d1279cab66ac9bccc862da17e35ee547d7610)

### Documentation


- Documented in the decompressor errata the issue where "compressed block size exactly 128 KB" was incorrectly rejected and its impact scope. [commit](https://github.com/facebook/zstd/commit/a29b6ed2510795bb7bca93bb6fadb09cf4c0345d)

- The streaming compression example now uses single-threaded mode by default; when multithreading is requested but the linked library does not support it, a message is shown and it falls back to single-threaded. [commit](https://github.com/facebook/zstd/commit/6ec18aed31a955ce7ce04403538f7539cd57eb56)

- Fixed two English spelling/wording errors in CONTRIBUTING.md. [commit](https://github.com/facebook/zstd/commit/a1b9a5ad0e1a10bea2315132bef21de3ed9cebc7)

- Clarified the dual license statement in README as either BSD or GPLv2. [commit](https://github.com/facebook/zstd/commit/969e54f26ee5e03677d47b6449be02fe48e6d349)

- Added usage descriptions for the ZSTD_estimate*Size() family of interfaces, clarifying static context usage scenarios and the applicable boundaries for one-shot and streaming estimates. [commit](https://github.com/facebook/zstd/commit/3fc14e411b18869e333732ceedad4f1052d73b86)

- Fixed spelling errors in documentation, comments, and build configuration detected by codespell. [commit](https://github.com/facebook/zstd/commit/fe34776c207f3f879f386ed4158a38d927ff6d10)

- Fixed a punctuation format issue in lib/README.md. [commit](https://github.com/facebook/zstd/commit/48b5a7bd8bedcfcaf22631d45c61c2f544315053)

- Added a CMake FetchContent integration example and explained the include directory settings required for Windows/macOS projects. [commit](https://github.com/facebook/zstd/commit/e590c8a0e3b2ecdde5f63d385fa7f9bd759721d3) [commit](https://github.com/facebook/zstd/commit/3c3845b9d88dacbd41cc544abcd3a5f58a120749)

- Clarified the definition of log2sup(N) in the format specification and the maximum number of bits consumed when reading Huffman symbol weights. [commit](https://github.com/facebook/zstd/commit/b38d87b476b804d7948928d298c784deb875a93c) [commit](https://github.com/facebook/zstd/commit/324cce4996d24af7b2cd86cf5eb1b9bd80de0a47)

- Added instructions in README for integrating zstd via the Bazel Central Registry. [commit](https://github.com/facebook/zstd/commit/98d8ad27a2b2a2fc75e0594bae992824c470f61c)

- Clarified that decoding more than 255 Huffman weights indicates corrupted data. [commit](https://github.com/facebook/zstd/commit/e61e3ff15208432cecf09ede09e8ebcf1d126bdd)

- Clarified that the Huffman weight table must have at least two non-zero weights and must include weight 1; otherwise the data is invalid. [commit](https://github.com/facebook/zstd/commit/dc84e35138338e95016fe23feb7dae43a842ca4f) [commit](https://github.com/facebook/zstd/commit/05059e5a48333e594e0204894cbbdffe51305487)

- Clarified that in the FSE table, assigning a non-zero probability to an invalid symbol is considered corrupted data, even if the symbol is never used. [commit](https://github.com/facebook/zstd/commit/c5bf96fb74378aaefec44f30f67f88f3f70f8e4e)

- Fixed the FSE state table in the zstd format documentation. [commit](https://github.com/facebook/zstd/commit/52e41b9ac8010da90bbe97421cca533afd6914c0)

- Added a description for the CLI -V version display option, noting immediate exit and the output form when combined with -q. [commit](https://github.com/facebook/zstd/commit/4fb0a77314cabc65eb90895fae35a7f38ace560d)

- Updated the implementation description of ZSTD_RowFindBestMatch, adding row/tag layout and hash usage. [commit](https://github.com/facebook/zstd/commit/b20703f273197589c8c70dd406b81ad601fa9b4a)

- Updated man page format and compression level descriptions, removing duplicate paragraphs. [commit](https://github.com/facebook/zstd/commit/5473b72a05ad03555fed8774f7e5af5e99e27e47) [commit](https://github.com/facebook/zstd/commit/ff6713fd72b083ce8a7d1f2a89cd3749ce9f07a8)

- Added steps for creating, building, and registering new fuzz harnesses. [commit](https://github.com/facebook/zstd/commit/f62b2663b96d440d3b9dd50b40dc911f9e0083d3)

- Clarified that after a compression or decompression operation returns an error, the associated CCtx/DCtx may be in an undefined state and must be reset before continuing streaming operations; updated the API manual accordingly. [commit](https://github.com/facebook/zstd/commit/5d82c2b57c0f5f239ba712a7e6ec46c84a6ba02d) [commit](https://github.com/facebook/zstd/commit/902c7ec1fe833f7f8d542fe94acba9e3a0a013a1) [commit](https://github.com/facebook/zstd/commit/3d18d9a9ce5fd5a03c6389b17ee464cf2cf60e94)

### Build / CI


- Upgraded OSSF Scorecard GitHub Action to 2.1.3. [commit](https://github.com/facebook/zstd/commit/da41d1d401fade89b868ec5306b2805460bcd909)

- Upgraded CodeQL GitHub Action to 2.2.9. [commit](https://github.com/facebook/zstd/commit/68a4a034531df5bf2b895a2ca76c1bf629ee3415)

- The Windows artifacts workflow adds Win32 builds and uses strategy.matrix to organize platform tasks. [commit](https://github.com/facebook/zstd/commit/520843d8ffeaed2f57035b7ec3c24d2dbe2e342f) [commit](https://github.com/facebook/zstd/commit/a4fff8e0e81cb2e5ab44816b62b490cea3d4de0d)

- Upgrade the Cygwin installation workflow action to v4. [commit](https://github.com/facebook/zstd/commit/d9582a0cb8070c78e8a53fba56b94a41936914aa)

- Upgraded CodeQL GitHub Action to 2.2.11. [commit](https://github.com/facebook/zstd/commit/dc88f7b8a0c154a555c3af997e18ec174cf2d3e6)

- Upgrade actions/checkout to 3.5.2 in multiple GitHub Actions workflows. [commit](https://github.com/facebook/zstd/commit/803e65f935d0e0faefb268341aa67124336bdb58)

- Add clangbuild-darwin-fat Makefile target for macOS, building arm64 and x86_64 separately and merging universal binaries with lipo. [commit](https://github.com/facebook/zstd/commit/0a794163f4feccf2c408c206f37da5f5b0eab4de)

- Fix unused variable warnings under MemorySanitizer configuration. [commit](https://github.com/facebook/zstd/commit/4c25ea329b851e1d2e45c2a91e0d5d79a3ad3be0)

- Upgraded CodeQL GitHub Action to 2.3.0. [commit](https://github.com/facebook/zstd/commit/be489f78df642cf8fd40fcfa59ec700cb494a1b5)

- Upgraded CodeQL GitHub Action to 2.3.2. [commit](https://github.com/facebook/zstd/commit/2a5076d26481fddb22f1e589c1d1666b0a7456d6)

- Add build options to Makefile to exclude compressors at dfast and above or greedy and above, with corresponding tests, CI validation, and usage instructions. [commit](https://github.com/facebook/zstd/commit/bae174960b4abd8cefadf23f323b2c82829538e6) [commit](https://github.com/facebook/zstd/commit/698af84fcf8bdcfa3db4936a88e84c354331a84a) [commit](https://github.com/facebook/zstd/commit/cc1ffe0bd6561128f39cc6c673aa75c91a925b68) [commit](https://github.com/facebook/zstd/commit/5490c75ddaae98010985618832ab55ed7b98dbed)

- Add CMake options for compression, decompression, dictionary building, and deprecated module switches, and provide related API visibility configuration options. [commit](https://github.com/facebook/zstd/commit/5059618295bc67f4f70eb6f12e6cf57b8d3de141)

- Upgrade actions/checkout in GitHub Actions workflows to 3.5.3. [commit](https://github.com/facebook/zstd/commit/6579f6c452cfb4bc87f2b25c98adc1a2dda7b87b)

- Update FreeBSD CI images to 13.2 and 12.4. [commit](https://github.com/facebook/zstd/commit/f307493711b74ddfdbf9da711f75c4e07bcc93a3)

- Upgrade OSSF Scorecard GitHub Action to 2.2.0. [commit](https://github.com/facebook/zstd/commit/2c97f5dbedb0b581c733eb658665a9cc886eccef)

- Upgrade CodeQL GitHub Action to 2.20.1. [commit](https://github.com/facebook/zstd/commit/1a6278c82d3b35cd8abd82db7bc5dc0907b838dd)

- Upgrade CodeQL GitHub Action to 2.20.3. [commit](https://github.com/facebook/zstd/commit/065ea9274fbbf794616df86a6376cd1c7f0dd5ca)

- Fix Intel Xcode/CMake build configuration when using assembly implementation. [commit](https://github.com/facebook/zstd/commit/7e09f07b325b6e2a95e11776f23ff97716b7b924)

- Upgrade CodeQL GitHub Action to 2.21.4. [commit](https://github.com/facebook/zstd/commit/db0ae65436c6aa977b60b8a7fd7d4522a3cd14ae)

- Add support for cleaning, building, and testing in MSYS2 and Cygwin environments to the Makefile. [commit](https://github.com/facebook/zstd/commit/78dbba76b81ea1d8713900b57bc5d5f5f43bf74b)

- Fix issue where CMake linking zstd program with shared library on Windows omitted pool and threading source files. [commit](https://github.com/facebook/zstd/commit/253873220f26c0fd43aef740751355f91f40b750)

- Upgrade actions/upload-artifact in GitHub Actions to 3.1.3. [commit](https://github.com/facebook/zstd/commit/d8b25cbf689092b175b3874b964e958218ff501a)

- Upgrade actions/checkout in GitHub Actions workflows to 4.0.0. [commit](https://github.com/facebook/zstd/commit/e0e309f27cf73f407f77cfce485203636678a46a)

- Pin x32 CI job to Ubuntu 20.04 to work around x32 test issues on ubuntu-latest environment. [commit](https://github.com/facebook/zstd/commit/2c17e0564689060d14dfc522497787364bc8f0e4)

- Fix pzstd Makefile concatenation of DESTDIR and BINDIR, allowing independent specification of BINDIR during installation. [commit](https://github.com/facebook/zstd/commit/d55ebb5718a1c7eaff65a720932aa628ccf4f66e)

- Upgrade actions/checkout in GitHub Actions workflows to 4.1.0. [commit](https://github.com/facebook/zstd/commit/d5cbae7c50835b84114efd3c80ff8bbe99080fe8)

- Upgrade actions/checkout in GitHub Actions workflows to 4.1.1. [commit](https://github.com/facebook/zstd/commit/af971cec6572e156e26bc403cb42396e7d908ba1)

- Export unified zstd::libzstd target in CMake, allowing consumers to choose built static or dynamic library at find_package stage. [commit](https://github.com/facebook/zstd/commit/c53d650d9a047ab12b2c7e5808878aff37d3cfc5) [commit](https://github.com/facebook/zstd/commit/475da4fb2e2aef102edecba04278b38fce44fb81) [commit](https://github.com/facebook/zstd/commit/dcd713ce06fd9729e2e1eefa079be866f5e2f519)

- Raise minimum CMake version requirement to 3.5 and remove compatibility code for CMake versions below 3.0. [commit](https://github.com/facebook/zstd/commit/4502ca5f422a4e3f0b8980d5a365fcc3f62e97e0) [commit](https://github.com/facebook/zstd/commit/f013b1b504cc2065e8860cf90461cef9364d96b0)

- Remove 12.4 image from FreeBSD CI. [commit](https://github.com/facebook/zstd/commit/20f8df64404b125fb76b851ccea944f47b820fd8)

- Upgrade actions/upload-artifact in GitHub Actions to 4.0.0 and update Windows artifacts workflow configuration. [commit](https://github.com/facebook/zstd/commit/e515327764889938692dac3257a300df56a15e8f) [commit](https://github.com/facebook/zstd/commit/377ecefce93d3a8705cb54c553681ff234bd9f34)

- Add FreeBSD 14 build task to Cirrus CI. [commit](https://github.com/facebook/zstd/commit/a52d897d6044029a904ab0d6893f6e73eec87d18)

- Meson MSVC CI now uses built-in --vsenv environment handling and meson compile command. [commit](https://github.com/facebook/zstd/commit/923cf3dc9289d00b668cd0a330d5c28f22d4837f)

- Upgrade actions/upload-artifact in GitHub Actions to 4.1.0. [commit](https://github.com/facebook/zstd/commit/e2fe26627907274f04b9ad7dabf41a3243547a1d)

- Upgrade CodeQL GitHub Action to 3.23.0. [commit](https://github.com/facebook/zstd/commit/3a2e302b2ca25eadca7d1952119837be70b2b8b2)

- playTests.sh directly uses portable grep regular expressions, reducing dependency on grep -E; and is compatible with older grep. [commit](https://github.com/facebook/zstd/commit/e6f4b464938008c4f800a26027248a00db5c81c8) [commit](https://github.com/facebook/zstd/commit/81f444f4f92b561278552c00d1d764caea1cff05)

- Fix CMake build test workflow, remove duplicate step copying build directory and explicitly output build logs. [commit](https://github.com/facebook/zstd/commit/2fc7248412db6c92086369fc3243f93f397cff4c)

- Upgrade actions/upload-artifact in GitHub Actions to 4.2.0. [commit](https://github.com/facebook/zstd/commit/ee2efb634eab104a2ec18ab6b2ce277bc159cbd0)

- Upgrade actions/upload-artifact in GitHub Actions to 4.3.0. [commit](https://github.com/facebook/zstd/commit/163e9b66377126e1b498c40628660d59aababf9f)

- Upgrade microsoft/setup-msbuild to 1.3.2. [commit](https://github.com/facebook/zstd/commit/c485b57bc73abfda9085650b4caaf013248e42dc)

- Add sparc64 compilation CI check. [commit](https://github.com/facebook/zstd/commit/e1ef81a3ae94dad4aa846615fc6e2293b28f50e8)

- Integrate lorem generator into paramgrill, Visual Studio, CMake, and Meson builds; also fix related build recipes. [commit](https://github.com/facebook/zstd/commit/a261375996c2301267ef6b00643e6efe92043d8a) [commit](https://github.com/facebook/zstd/commit/3ce4c6e046ed29ba4c0cb05fb48581edc52c1d3c) [commit](https://github.com/facebook/zstd/commit/befcec17886479a22028b1d0b632fa15e31d5abc) [commit](https://github.com/facebook/zstd/commit/fd03971252d043bb9d3e065dc2361db6d40c87b6)

- Intel CET compatibility CI updates Intel SDE dependency to 9.33.0 and re-enables the test. [commit](https://github.com/facebook/zstd/commit/04a6c8cbe240495f2dcf7ab108bec327ef245813)

- Upgrade microsoft/setup-msbuild to 2.0.0 and fix version comments in workflow. [commit](https://github.com/facebook/zstd/commit/9fed5ef108d63ff25964574c2ec980e578b1adbc) [commit](https://github.com/facebook/zstd/commit/0d9fb5dc3394161097dc54642bd793e6de3f7593)

- Upgrade setup-msys2 GitHub Action to v2.22.0. [commit](https://github.com/facebook/zstd/commit/0a68be83e7cb84c8212f666b4b4aa6e0dc8477cc)

- Add Meson, CMake, Visual Studio, and paramgrill build support for lorem/datagen and benchmark tools, and fix C89/clang build compatibility. [commit](https://github.com/facebook/zstd/commit/c2d357033838c01c827fc10f0b2b850df339776a) [commit](https://github.com/facebook/zstd/commit/588dfbcc97657f1d70e711f3e22d8f992e14ae28) [commit](https://github.com/facebook/zstd/commit/b34517a4402603e8210c24ceb7b976a360ef978b) [commit](https://github.com/facebook/zstd/commit/e62e15df190ebb41b0b9f1453b2a4e9bd6e05f51) [commit](https://github.com/facebook/zstd/commit/9e711c9360d8ebf17132e750b3fe24f79fc63a6d) [commit](https://github.com/facebook/zstd/commit/7170f51dd277d4aa4a675ffdd5593af362abe83c)

- Upgrade actions/upload-artifact in GitHub Actions to 4.3.1. [commit](https://github.com/facebook/zstd/commit/927d0799442c42ece088dcf339ca25968274f5a0)

- Fix actions/checkout version tags in multiple GitHub Actions workflows. [commit](https://github.com/facebook/zstd/commit/bb4f85db42925a1dd129e733d3413316ebd5c9bb)

- Upgrade CodeQL GitHub Action to 3.24.5. [commit](https://github.com/facebook/zstd/commit/a412bedb3f63a5bbb88601c0ab085a8eb0c39e48)

- Upgrade OSSF Scorecard GitHub Action to 2.3.1. [commit](https://github.com/facebook/zstd/commit/9446b1910cab25dd2eb93d76ca5e6168a6e70a51)

- Add include guard to Makefile, unify default targets/variable naming for library and programs, and simplify dependency file generation. [commit](https://github.com/facebook/zstd/commit/b69d06a8102f0e04cde0bda2e34984099a0dfba4) [commit](https://github.com/facebook/zstd/commit/4edfaa93b7631e5fcb2911869ab77c833d73d142) [commit](https://github.com/facebook/zstd/commit/feaa8ac50d4e0299f652a436e72cc64f9b504c38) [commit](https://github.com/facebook/zstd/commit/f4dbfce79cb2b82fb496fcd2518ecd3315051b7d) [commit](https://github.com/facebook/zstd/commit/607933a2ff41f985ec9f05f2a0fc3b5b74f52b48)

- Upgrade CodeQL GitHub Action to 3.24.6. [commit](https://github.com/facebook/zstd/commit/70df177615ea99eeea5a7704a823b32bb302e6a6)

- Fix CMake thread library detection on HP-UX 11.11 PA-RISC and extract dedicated configuration logic into a function. [commit](https://github.com/facebook/zstd/commit/e49d1ab6aabcd662b76a46ef48391a5462357167) [commit](https://github.com/facebook/zstd/commit/f6039f3d5fa607555fc193042671a05bf5029bad)

- Pin TSan and MSan CI jobs to Ubuntu 20.04. [commit](https://github.com/facebook/zstd/commit/ee6acaf26bbf842837513087c91776b83d4d9560)

- Add QEMU-based RISC-V cross-compilation and test tasks in GitHub Actions. [commit](https://github.com/facebook/zstd/commit/ad590275b482d4c561bdc58418ef6b6a1db80c25)

- Migrate commit and nightly workflows from CircleCI to GitHub Actions. [commit](https://github.com/facebook/zstd/commit/3a64c69eba2592ec1cbcbed294a84019ab47dd19)

- Add CMake build and CTest test tasks to Windows CI. [commit](https://github.com/facebook/zstd/commit/c1e995321e9d66a648818f7995999c4fe6d77878)

- CMake always generates unified libzstd target; selects implementation based on static/shared build configuration, and exposes include directories for FetchContent/ExternalProject. [commit](https://github.com/facebook/zstd/commit/a0a9bc6c95436c85002ffca972ae545f862e1638) [commit](https://github.com/facebook/zstd/commit/79cd0ff7120ed05ac9e52ba4c7a484752be4d758) [commit](https://github.com/facebook/zstd/commit/a595e5812a5c7e4ac47839383f931fb8000623f0)

- Upgrade actions/cache in GitHub Actions to v4. [commit](https://github.com/facebook/zstd/commit/88301b58c1b2f84e55f27fd7259db4f8afdafc22)

- Upgrade CodeQL GitHub Action to 3.24.7. [commit](https://github.com/facebook/zstd/commit/9dca0602f45e925c919ac130c9c9f37d88d4ab98)

- pzstd Makefile now uniformly requires C++14 to meet Google Test build requirements. [commit](https://github.com/facebook/zstd/commit/cd4dba74dea8a92f9e33d72fcb5b60224bc4e6c3)

- CMake emits clear warning when BUILD_SHARED_LIBS conflicts with ZSTD_BUILD_SHARED/ZSTD_BUILD_STATIC configuration. [commit](https://github.com/facebook/zstd/commit/42b02f5185393e5f71abaa4c532684de3569be85)

- CMake selects x86-64 Huffman assembly implementation based on target architecture, and disables the assembly source on MSVC or non-x86-64 platforms. [commit](https://github.com/facebook/zstd/commit/4f77b81c8a15976d79070ec995adbbe8ba5a6966)

### Maintenance


- mmap-dict CLI help now displays --[no-]mmap-dict and fixes line breaks. [commit](https://github.com/facebook/zstd/commit/c28031df8f1809621407b5bc9c4b3e052872409f)

- Remove Travis CI and AppVeyor configuration scripts. [commit](https://github.com/facebook/zstd/commit/05434fe9a5d0d55650596e43171efcf1208c5c84)

- Fix spelling of ZSTD_BUILD_DECOMPRESSION option description in CMake. [commit](https://github.com/facebook/zstd/commit/a02d81f944c24aca2ccca2f16a6a96474f97e18b)

- Tighten fuzzing/debug conditional compilation scope for internal helper functions like ZSTD_assertValidSequence. [commit](https://github.com/facebook/zstd/commit/cdceb0fce59785c841bf697e00067163106064e1)

- Update bundled xxHash to v0.8.2 and adjust its copyright and license header information accordingly. [commit](https://github.com/facebook/zstd/commit/592b1acb1804f18e42412607a81c636dc1d4e850) [commit](https://github.com/facebook/zstd/commit/3fd5f9f52dff5e4e8a9afcf9afb1abc946844535) [commit](https://github.com/facebook/zstd/commit/59dcc475798b3e522be8cd3ba41a170b34c10d63)

- Fix spelling errors in Makefile comments. [commit](https://github.com/facebook/zstd/commit/8ba5bc4729a04919e4416d8e84cfab28e1d7801c)

- Lower debug level of several debug logs in sub-block compression process so they only output at higher verbosity. [commit](https://github.com/facebook/zstd/commit/aed172a8fe84caccc86e5f27999a309d1df47c00)

- Remove duplicate and inaccurate function comments in zstd_decompress.c, unifying to header file API documentation. [commit](https://github.com/facebook/zstd/commit/559762da12f54712d44f619098aa4a7e7bc5727b)

- Add source file line numbers to debug trace output. [commit](https://github.com/facebook/zstd/commit/9cc3304614f9ea28a870f9e94e1e449c6d7de1fc)

- Fix spelling errors in API header files and HTML manual. [commit](https://github.com/facebook/zstd/commit/c5da438dc0ca81ce697a73a02b060e3ba7550bab)

