# Release Note

## Important Changes

### Core Compression Engine
- Added a new pre-splitter to analyze the data before compression and split blocks at more appropriate boundaries to improve the compression ratio. (Architecture event: Zstandard compression library module change)
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [a5bce4a](https://github.com/facebook/zstd/commit/a5bce4ae84daa5885e61753fa98903964c3348bd)
- Moved sequence-related type definitions from public header files to compressed internal header files, and renamed some types, which is a destructive change. (Architecture event: Sequence type definitions were moved to internal header files)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [b4a40a8](https://github.com/facebook/zstd/commit/b4a40a845fffc07a0e95a8a59fdbb1b87934d256)
- Added new public API ZSTD_compressSequencesAndLiterals(), which supports receiving external literal buffers for compression and supports multi-block frames. At the same time, srcSize, litCapacity parameters and dedicated error codes are added. (Architecture-related: public API)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [125f052](https://github.com/facebook/zstd/commit/125f05282b0566790551e6756bdbc0290addfcb2), [14a21e4](https://github.com/facebook/zstd/commit/14a21e43b31042b8cd67d4a757920735a8d33d94), [31b5ef2](https://github.com/facebook/zstd/commit/31b5ef25393c3abf4bb9e290cf32b06d97c78b93), [0a54f6f](https://github.com/facebook/zstd/commit/0a54f6f288bab194e1c4edcd03cedc8d084c2d6f), [b339eff](https://github.com/facebook/zstd/commit/b339efff2bc9d11ce091bca62328c1884a38b5f3), [b7a9e69](https://github.com/facebook/zstd/commit/b7a9e69d8dc8b61be9d341a4e7a56350fb1e545e), [f0d0d95](https://github.com/facebook/zstd/commit/f0d0d952348b4bdc2e3111d73d6703f1b6151f0d), [f281497](https://github.com/facebook/zstd/commit/f281497aef87a0e6459eef28f695c437a3dec42d), [e9f8a11](https://github.com/facebook/zstd/commit/e9f8a119b4fcd44038dbb0d072aa44968d81bd9b), [0165eeb](https://github.com/facebook/zstd/commit/0165eeb441de43ffe11b95b9073c0a694b66e6a4), [ab0f179](https://github.com/facebook/zstd/commit/ab0f1798e8ec85dc03d39412513c84a5ef5539ff)
- Promote ZSTD_getErrorCode() to a stable API, and update the version number and related documentation comments. (Architecture-related: public API)
  ↳ [#4184](https://github.com/facebook/zstd/pull/4184): [d9553fd](https://github.com/facebook/zstd/commit/d9553fd2180535a11dcb4e2f5a3197202befc2c0)
- Exposed the get1BlockSummary function as ZSTD_get1BlockSummary, and added a performance test for it in the benchmark framework. (Architecture-related: public API)
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [8eb2587](https://github.com/facebook/zstd/commit/8eb2587432d70359f26ff98fd12db7e8c9be7515)
- Generalize the parameter and return value types of bit container operation functions from size_t to BitContainerType, so that the register type and size can be controlled independently of size_t. (Architecture-related: public API)
  ↳ [#4253](https://github.com/facebook/zstd/pull/4253): [82346b9](https://github.com/facebook/zstd/commit/82346b92bb5f02dea90907135f74cd77f0c9cb33)
- Fixed the compilation warning of the zstd.h header file in the C++ environment, and added conditional compilation protection to be compatible with the -Wzero-as-null-pointer-constant option. (Architecture-related: public API)
  ↳ [#4034](https://github.com/facebook/zstd/pull/4034): [d7cb470](https://github.com/facebook/zstd/commit/d7cb47036cb78b3681aee4725107381a1b69abfc), [97291fc](https://github.com/facebook/zstd/commit/97291fc5020a8994019ab76cf0cda83a9824374c)
- During the FSE decompression process, an error is thrown when the initial state of the Huffman weight is truncated. (Architecture-related: external behavior)
  ↳ [#4079](https://github.com/facebook/zstd/pull/4079): [0938308](https://github.com/facebook/zstd/commit/0938308ff69b3a7679898d75403832bafe43ba89)
- Fixed a memory leak caused by parameter checking when ZSTD_generateSequences returns early, moving the target buffer allocation after parameter checking. (Architecture-related: public API)
  ↳ [#4115](https://github.com/facebook/zstd/pull/4115): [a40bad8](https://github.com/facebook/zstd/commit/a40bad8ec06aeb992e8d8e58648a4024261b2a54)
- Limit inline assembly statements to only take effect under the GCC compiler to improve platform compatibility. (Architecture-related: platform compatibility)
  ↳ [#4165](https://github.com/facebook/zstd/pull/4165): [d45aee4](https://github.com/facebook/zstd/commit/d45aee43f4b1ac8ee0fbb182310b9b7622f85d1c)
- Fixed the problem of workspace alignment on non-64-bit systems, and adjusted related alignment checks and retention functions. (Architecture-related: platform compatibility)
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [4ce91cb](https://github.com/facebook/zstd/commit/4ce91cbf2bfecefcd99973a5e68711c388684d41), [4685eaf](https://github.com/facebook/zstd/commit/4685eafa81d4c31048577aeb461883043ca96c2f)
- Added sequence validation error return for ZSTD_compressSequencesAndLiterals, and updated related documentation. (Architecture-related: public API)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [76445bb](https://github.com/facebook/zstd/commit/76445bb379fe74b0a8cddcce2658c111a2e8d7b0), [d2d0fda](https://github.com/facebook/zstd/commit/d2d0fdac4288fed2d63b4d3e0e41f4b4768f8b60), [b7b4e86](https://github.com/facebook/zstd/commit/b7b4e8634786024499dd42d479a2be3a2edae92c)
- Improved ZSTD_getFrameHeader handling of skippable frames, now correctly reports header size and magic variants (via dictID field). (Architecture-related: public API)
  ↳ [#4228](https://github.com/facebook/zstd/pull/4228): [a2ff6ea](https://github.com/facebook/zstd/commit/a2ff6ea7846c598812be580026dfc63fd7229db3) | [#4227](https://github.com/facebook/zstd/pull/4227): [f8a2b35](https://github.com/facebook/zstd/commit/f8a2b352d62b1a2e41ff1715e1afe8771fe43abc)
- Removed differences in row matcher selection based on SSE2/Neon availability, and unified the use of the same window log threshold to enhance reproducibility. (Architecture-related: platform compatibility)
  ↳ [#4230](https://github.com/facebook/zstd/pull/4230): [d88651e](https://github.com/facebook/zstd/commit/d88651e6041995243c8cd6884bbc44c279ab80d2)
- Fixed the problem of error checking macro when building MSVC 64-bit, and adjusted the return type of two bit operation functions to BitContainerType. (Architecture-related: platform compatibility)
  ↳ [#4234](https://github.com/facebook/zstd/pull/4234): [42d704a](https://github.com/facebook/zstd/commit/42d704ad5e286fe8ad8b8aca0af4c78543abd3f1)
- Added CI test for x86 32-bit + AVX2 combination, and fixed type conversion in BIT_closeCStream function. (Architecture-related: public API)
  ↳ [#4250](https://github.com/facebook/zstd/pull/4250): [9efb097](https://github.com/facebook/zstd/commit/9efb09749b85acfbc2299fb6dec6146b942c6b2e), [35edbc2](https://github.com/facebook/zstd/commit/35edbc20dc31fcc64f7dfe0c256d5005879b1b59), [0501095](https://github.com/facebook/zstd/commit/050109589800be49d3840927b9e821d24622e1ea), [d2d7461](https://github.com/facebook/zstd/commit/d2d74616c0bfaf9d76186398a23fffafbb591c52), [f0b5f65](https://github.com/facebook/zstd/commit/f0b5f65bca6587f6d9b642e3a95d58ae36b7cdea)
- Fixed the compatibility issue of BMI2 built-in function on 32-bit platform, including selecting the correct built-in function according to size_t size, parameter type adjustment, conditional compilation format correction and enabling DYNAMIC_BMI2 support by default. (Architecture-related: platform compatibility)
  ↳ [#4248](https://github.com/facebook/zstd/pull/4248): [ee17f4c](https://github.com/facebook/zstd/commit/ee17f4c6d295e82733673f824e7dba81a33e245b), [936927a](https://github.com/facebook/zstd/commit/936927a427704ca21dfd07c666c4123737c8fb03), [26e5fb3](https://github.com/facebook/zstd/commit/26e5fb36149b9d155a3640ca0800199fc13711e8), [462484d](https://github.com/facebook/zstd/commit/462484d5dcbab964474bf4704df4d188e5c31818) | [#4252](https://github.com/facebook/zstd/pull/4252): [4bbf4a2](https://github.com/facebook/zstd/commit/4bbf4a285d92e4cb5b37e0fd1d4af96c12c2c249) | [#4265](https://github.com/facebook/zstd/pull/4265): [0cda010](https://github.com/facebook/zstd/commit/0cda0100ea4b9d87eeaaf68e7d192fbbff4f2ab2)
- The ZSTD_splitBlock_4k and ZSTD_splitBlock_byChunks functions are changed to use the external workspace passed in and no longer rely on internal static allocation; at the same time, the memory alignment allocation function is restructured and ZSTD_cwksp_initialAllocStart is rewritten to improve readability. (Architecture-related: public API)
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [73a6653](https://github.com/facebook/zstd/commit/73a665365350668757ec542277472ca73267603a), [cae8d13](https://github.com/facebook/zstd/commit/cae8d13294904c0b6095a5533d0cda72d7e6a7ff), [06b7cfa](https://github.com/facebook/zstd/commit/06b7cfabf8f5f3ba48694758cf85aaf7671504d2)
- Simplify the signature of ZSTD_splitBlock and its internal auxiliary functions, remove the blockSizeMax parameter, and adjust the internal logic to support more split strategies. (Architecture-related: public API)
  ↳ [#4176](https://github.com/facebook/zstd/pull/4176): [ca6e55c](https://github.com/facebook/zstd/commit/ca6e55cbf5bf3739520dd6ee07ae2785629f1b1e)
- Rename the block splitter control parameter enumeration constant ZSTD_c_blockSplitter_level to ZSTD_c_blockSplitterLevel, and update related code and tests simultaneously. (Architecture-related: public API)
  ↳ [#4180](https://github.com/facebook/zstd/pull/4180): [4f93206](https://github.com/facebook/zstd/commit/4f93206d62f306040a8e35033312e16986d0aeab)
- Make ZSTD_copySequencesToSeqStore related functions internally private, add sequence verification functions, and correct parameter types and enumeration naming; also add ZSTD_storeSeqOnly functions to support separation of registered sequences and copy literals. (Architecture-related: public API)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [76dd3a9](https://github.com/facebook/zstd/commit/76dd3a98c48445f5f586d2deca5a3aedfefbd49d), [a00f45a](https://github.com/facebook/zstd/commit/a00f45a03751a90f620425f30690d86d872dfef1)
- Simplify the block size calculation logic in delimiter-less mode, and adjust the API parameter names of ZSTD_compressSequences and ZSTD_compressSequencesAndLiterals. (Architecture-related: public API)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [13b9296](https://github.com/facebook/zstd/commit/13b9296d79094185565f42b55a19fa88b43aa19d)
- Rename the enumeration ZSTD_paramSwitch_e to ZSTD_ParamSwitch_e, unify related parameter names (such as ZSTD_c_searchForExternalRepcodes to ZSTD_c_repcodeResolution), simplify the parsing logic of the row matching finder, and remove the platform-related SIMD conditional branch. (Architecture-related: public API rename)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [56cfb78](https://github.com/facebook/zstd/commit/56cfb7816a5a627b39c03405e967cf67691974c4)
- Adjust the return value semantics of the sequence copy function so that it returns the actual number of bytes consumed from the input, and refactor the related internal functions to support the new return value convention. (Architecture-related: public API behavior changes)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [047db4f](https://github.com/facebook/zstd/commit/047db4f1f8e9d340e24b752323af17df1f0bb782)
- Optimized the performance of the sequence converter, introduced AVX2 to accelerate sequence format conversion, and removed the sequence verification function to simplify the logic. (Architecture-related: External behavior: Sequence verification removed)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [12c47d3](https://github.com/facebook/zstd/commit/12c47d32624df633b9dd3402273529cff7705228)
- Optimize ZSTD_get1BlockSummary function performance: enable AVX2 vectorization path, and improve alignment macro compatibility. (Architecture-related: platform compatibility)
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [b6a4d5a](https://github.com/facebook/zstd/commit/b6a4d5a8ba29bc873c95098103f57f987cfacd23), [ed0a8b8](https://github.com/facebook/zstd/commit/ed0a8b8be173fdd8fc0a05b60c1571d13c14b0a3)
- The document clearly states that ZSTD_decompress() supports decompression of multiple consecutive compressed frames at one time, and the result will be splicing of all decompressed data. (Architecture-related: public API)
  ↳ [#4298](https://github.com/facebook/zstd/pull/4298): [2acf904](https://github.com/facebook/zstd/commit/2acf90431ab2ffdc7d85d1017cf344bac897e704)
- Documentation supplement: New prototype ZSTD_compressSequencesAndLiterals() is incompatible with frame checksum. (Architecture-related: public API)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [e0f3aae](https://github.com/facebook/zstd/commit/e0f3aaee467bbcb7e1653756eb426a9b7adde5d8)
- Update the API documentation of ZSTD_compressSequencesAndLiterals: rename the parameter litCapacity to litBufCapacity and improve the description; also clarify its restrictions, and adjust the description of the ZSTD_c_searchForExternalRepcodes parameter. (Architecture-related: public API)
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [e3181cf](https://github.com/facebook/zstd/commit/e3181cfd325db59dbdeadcaf91b8187f49c5546c) | [#4217](https://github.com/facebook/zstd/pull/4217): [f176514](https://github.com/facebook/zstd/commit/f17651446730b580f0a45c4a7917236da140db76)
- Update the API documentation, recommend users to check the return value of ZSTD_decompressStream(), and correct the condition error in the ZSTD_compressBound documentation. (Architecture-related: public API)
  ↳ [#4031](https://github.com/facebook/zstd/pull/4031): [a86f5f3](https://github.com/facebook/zstd/commit/a86f5f3f33f40945c0d1341827fabc6a22338499) | [#4202](https://github.com/facebook/zstd/pull/4202): [10beb7c](https://github.com/facebook/zstd/commit/10beb7cb53ba328722d82c271d7b450b97869c92)
- Added AVX2 compilation macros and unified conditional compilation methods. (Architecture-related: platform compatibility)
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [6f8e6f3](https://github.com/facebook/zstd/commit/6f8e6f3c97c8e95527a29c4667edca6b793f798f), [2f3ee8b](https://github.com/facebook/zstd/commit/2f3ee8b5309958a2bc1fc7477e703fd8195a31ea)
- Fixed the size check of the static assertion in the BIT_getLowerBits function to ensure correct verification that the bitContainer type is U32. (Architecture-related: public API type check)
  ↳ [#4248](https://github.com/facebook/zstd/pull/4248): [fcd684b](https://github.com/facebook/zstd/commit/fcd684b9b45917dbb90e8122faf782e4028fdb42)
- Replaced memset calls in zstd_preSplit.c with ZSTD_memset to improve portability on Linux kernel. (Architecture-related: platform compatibility)
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [e2d7d08](https://github.com/facebook/zstd/commit/e2d7d08888f915667c94e6dbbadaee38a5d50fa5), [fa147cb](https://github.com/facebook/zstd/commit/fa147cbb4d3fbd8c31b1f35c7984ae62f4c6ea03)
- Added explicit type conversion in zstd_preSplit.c to fix C++ compatibility issues. (Architecture-related: C++ compatibility)
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [6021b66](https://github.com/facebook/zstd/commit/6021b6663a4705f446f7cf856d944819caa575c3)

### Linux Kernel Integration Module
- Exposed external sequence producer API for Linux kernel modules, and added helper functions for calculating compression context workspace size. (Architectural event: Linux kernel module)
  ↳ [#4064](https://github.com/facebook/zstd/pull/4064): [3242ac5](https://github.com/facebook/zstd/commit/3242ac598e6f17d8008f6110337a3b4c1205842b) | [#4063](https://github.com/facebook/zstd/pull/4063): [be6a182](https://github.com/facebook/zstd/commit/be6a18200621dd21ce073b77fce7f57636a6f4f4)
- Exposed the ZSTD_compressSequencesAndLiterals() and ZSTD_CCtx_setParameter() functions in the kernel, and updated the build process and header file references. (Architecture-related: public API)
  ↳ [#4260](https://github.com/facebook/zstd/pull/4260): [92be4be](https://github.com/facebook/zstd/commit/92be4be8102eecedaa0d2a7c65b2d1088e01622a)

### Parallel Compression Module
- Added the block splitting level control parameter ZSTD_c_blockSplitterLevel, and introduced multiple block splitting strategies such as split_lvl3, faster variants and boundary fingerprint-based variants. At the same time, all complete 128KB blocks will now be split, making streaming behavior more consistent. (Architecture-related: public API)
  ↳ [#4176](https://github.com/facebook/zstd/pull/4176): [566763f](https://github.com/facebook/zstd/commit/566763fdc9b54220e8e419446331dc15fb1c183b), [da2c0df](https://github.com/facebook/zstd/commit/da2c0dffd8c3e6306fcf2e8e5bd5f8ef97d7a999), [94d7b07](https://github.com/facebook/zstd/commit/94d7b0742500ecb02546c562c68f6e095068ce35), [326c45b](https://github.com/facebook/zstd/commit/326c45bb8ed8f9f9e7dce1721db5d5e1ec1cb818) | [#4136](https://github.com/facebook/zstd/pull/4136): [7d3e5e3](https://github.com/facebook/zstd/commit/7d3e5e3ba1007635fc991a3b208353463cb2712d), [0d4b520](https://github.com/facebook/zstd/commit/0d4b52065791a8e96faf8eb7665cb701b29d186e), [1c62e71](https://github.com/facebook/zstd/commit/1c62e714ab9f53aefd6478e033ce448597b68fab), [1ec5f9f](https://github.com/facebook/zstd/commit/1ec5f9f1f6b187095d996248471a6c6f128e9001), [16450d0](https://github.com/facebook/zstd/commit/16450d0732ff84e3ad367f616d84cee1567cfb8e) | [#4178](https://github.com/facebook/zstd/pull/4178): [e557abc](https://github.com/facebook/zstd/commit/e557abc8a0380b095b14623ca7c4105a38fdb981) | [#4180](https://github.com/facebook/zstd/pull/4180): [226ae73](https://github.com/facebook/zstd/commit/226ae73311d1ffd0c3488d8bc6a59576d910d6d4), [bbaba45](https://github.com/facebook/zstd/commit/bbaba45589f233b91a310806d97ee7b4d9ee8320), [01474bf](https://github.com/facebook/zstd/commit/01474bf73b357fe0c7bcf51f5cd41928462e2488)

### Cross-cutting / Other Architecture-related Changes
- Enhanced support for the IAR compiler, adding IAR compiler specific branches in the endianness detection and byte swap functions. (Architecture-related: platform compatibility)
  ↳ [#4046](https://github.com/facebook/zstd/pull/4046): [2955d92](https://github.com/facebook/zstd/commit/2955d92ac02eb60b6d0d00e7c6cd3f013ac020e6)
- Enable weak symbol support on RISC-V architecture. (Architecture-related: Platform compatibility)
  ↳ [#4114](https://github.com/facebook/zstd/pull/4114): [6dbd49b](https://github.com/facebook/zstd/commit/6dbd49bcd04c42b0b4893d824b856563ae901b33)
- Enable x86_64 assembly support on Windows platforms. (Architecture-related: Platform compatibility)
  ↳ [#4246](https://github.com/facebook/zstd/pull/4246): [46e17b8](https://github.com/facebook/zstd/commit/46e17b805b1bb2982583208da3b9184e377c2dd5)
- Automatic BMI2 detection is no longer limited to x64 mode. In 32-bit mode, the instruction set can also be automatically detected and enabled at compile time, and the library documentation is updated at the same time. (Architecture-related: platform compatibility)
  ↳ [#4251](https://github.com/facebook/zstd/pull/4251): [a556559](https://github.com/facebook/zstd/commit/a556559841db607ede4e4e0a85773e5b214e66f1)
- Implement the ZSTD_ALIGNED macro for the MSVC compiler, use __declspec(align) to provide alignment support, and replace local alignment definitions. (Architecture-related: platform compatibility)
  ↳ [#4258](https://github.com/facebook/zstd/pull/4258): [a0872a8](https://github.com/facebook/zstd/commit/a0872a837294ae9b18967e9e80342587f3089fb0) | [#4232](https://github.com/facebook/zstd/pull/4232): [8bff69a](https://github.com/facebook/zstd/commit/8bff69af869fca1cc44172c2ae5d5f995322509b)
- Added the --max command to set all compression parameters to the maximum value to pursue the ultimate compression ratio, and updated the manual instructions. (Architecture-related: public API)
  ↳ [#4290](https://github.com/facebook/zstd/pull/4290): [630b47a](https://github.com/facebook/zstd/commit/630b47a158cc22002045494c7e0dc0f0672c2fca), [8ae1330](https://github.com/facebook/zstd/commit/8ae1330708b42c7f5751e94e02970e7ccb5d9731), [39d1d82](https://github.com/facebook/zstd/commit/39d1d82fa80bfbec6d894ccf8bf18137cedad5d6)
- Fixed build issues when using clang 16 and above on Windows x86, and adjusted the conditional judgment of CPUID detection. (Architecture-related: platform compatibility)
  ↳ [#3998](https://github.com/facebook/zstd/pull/3998): [72c16b1](https://github.com/facebook/zstd/commit/72c16b187d27016b7634f5c6b7290e7c66ba44b3)
- Fixed the problem caused by the unavailability of register %rbx when using clang in 32-bit mode, and added a 64-bit mode check to disable the relevant code paths in 32-bit mode. (Architecture-related: platform compatibility)
  ↳ [#4118](https://github.com/facebook/zstd/pull/4118): [5e0a83e](https://github.com/facebook/zstd/commit/5e0a83ec255a0f4bb6a3cf8c4abcae46bfc2c3c5)
- Disable the --max option in 32-bit mode, prompt incompatibility and exit when using. (Architecture-related: platform compatibility)
  ↳ [#4290](https://github.com/facebook/zstd/pull/4290): [468e145](https://github.com/facebook/zstd/commit/468e1453a55d119c914843bff73af809cbe4ba79)
- Rename the public API enumeration ZSTD_sequenceFormat_e to ZSTD_SequenceFormat_e, and add backward compatibility macro definitions. (Architecture-related: public API)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [c97522f](https://github.com/facebook/zstd/commit/c97522f7fb797cde035ab26f0ba97addb718c174)
- Rename the advanced parameter ZSTD_c_searchForExternalRepcodes to ZSTD_c_repcodeResolution, and the old name remains backward compatible through macro definition; at the same time, change the repcodeResolution parameter type from ZSTD_ParamSwitch_e to int. (Architecture-related: public API renaming and compatibility)
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [5164d44](https://github.com/facebook/zstd/commit/5164d44dabbbf2f3f1cd89bbf1244b7b73d69ef3), [ca8bd83](https://github.com/facebook/zstd/commit/ca8bd83373310ade16a6d230c01b671d7725eaf1)
- Unify type naming conventions, change the first letters of multiple internal and public type names to uppercase, involving ZSTD_matchState_t, seqStore_t, ZSTD_sequencePosition, ZSTD_paramSwitch_e, etc., and adjust function names and field names accordingly. (Architecture-related: public API naming convention)
  ↳ [#4228](https://github.com/facebook/zstd/pull/4228): [04a2a02](https://github.com/facebook/zstd/commit/04a2a0219ca424595949d725fda5da5cf764b419) | [#4217](https://github.com/facebook/zstd/pull/4217): [894ea31](https://github.com/facebook/zstd/commit/894ea312819e36084e0ce26922037ba8571cd65d), [30671d7](https://github.com/facebook/zstd/commit/30671d77afeedbc70957ac8ce8e864d5219d97bb), [fa46894](https://github.com/facebook/zstd/commit/fa468944f2a999a10f6a823fe7252da3e0fdc129), [5df80ac](https://github.com/facebook/zstd/commit/5df80acedb6b352e949ef24446cb489b15524ce0), [41c667c](https://github.com/facebook/zstd/commit/41c667c0fdfa653f52809975bce8306b21099810), [25bef24](https://github.com/facebook/zstd/commit/25bef24c5cf47fe9841edb4b2b6708e206833d31), [08edecb](https://github.com/facebook/zstd/commit/08edecb78c0b95db74aa9747cc06206d74027b0f), [9671813](https://github.com/facebook/zstd/commit/9671813375cec4576f874eab00ebe669e3cfbe36), [a224572](https://github.com/facebook/zstd/commit/a2245721ca3e91261d7c948f7a71d195caf1f871), [8d4506b](https://github.com/facebook/zstd/commit/8d4506bc9463607725e43131b71b2f09b7e1109d), [477a010](https://github.com/facebook/zstd/commit/477a01067f46f9a6909784b3777d6182f1991f0a), [0442e43](https://github.com/facebook/zstd/commit/0442e43acadd65b35b41f1fadae301a629d7e37e) | [#4136](https://github.com/facebook/zstd/pull/4136): [7bad787](https://github.com/facebook/zstd/commit/7bad787d8bcae57cf0bdcbca00b3f106ae557b75)
- Replace C11's alignas with the _Alignas keyword to eliminate dependence on header files. (Architecture-related: platform compatibility)
  ↳ [#4286](https://github.com/facebook/zstd/pull/4286): [bcf404c](https://github.com/facebook/zstd/commit/bcf404c0ab73cb6cc822a1412b78ba7965f9d74d)
- Unified MSVC x64 detection macro to _M_X64, replacing _M_AMD64. (Architecture-related: platform compatibility)
  ↳ [#4257](https://github.com/facebook/zstd/pull/4257): [6c1d1cc](https://github.com/facebook/zstd/commit/6c1d1cc600f0cc5dab40e16200f4d23eeaeb0c9f)
- Adjust the ZSTD_ASM_SUPPORTED macro definition to separate the processing conditions of the memory sanitizer and the data flow sanitizer. (Architecture-related: platform compatibility)
  ↳ [#4246](https://github.com/facebook/zstd/pull/4246): [d60c4d7](https://github.com/facebook/zstd/commit/d60c4d75e9d29d76cc202f7a8341ab0bda1d6402)
- Update the README document, update the benchmark test data to Zstd 1.5.6, and add instructions for installing zstd through Conan. (Architecture-related: installation configuration)
  ↳ [#3997](https://github.com/facebook/zstd/pull/3997): [e0ee0fc](https://github.com/facebook/zstd/commit/e0ee0fccf8c591465be4c3f4872ef550e7939f73) | [#4101](https://github.com/facebook/zstd/pull/4101): [0986e1e](https://github.com/facebook/zstd/commit/0986e1e630c0a4286ea07516bde3e6571c22274d)
- Fix Android NDK r27 build failure, avoid defining _GNU_SOURCE macro on Android because NDK does not provide qsort_r() function. (Architecture-related: platform compatibility)
  ↳ [#4107](https://github.com/facebook/zstd/pull/4107): [c3c28c4](https://github.com/facebook/zstd/commit/c3c28c4d5a28bca93c97c4ce447f3c8ece42791d)
- Fix QNX platform compilation issues, adjust header file inclusion and extern "C" declaration position. (Architecture-related: platform compatibility)
  ↳ [#4188](https://github.com/facebook/zstd/pull/4188): [b3035b3](https://github.com/facebook/zstd/commit/b3035b36c631614e32707cce0ab04c72c79c49a7)
- Adjust the header file inclusion location and extern "C" block structure in debug.h and huf.h to fix C++ compilation compatibility issues. (Architecture-related: public API)
  ↳ [#4218](https://github.com/facebook/zstd/pull/4218): [63acf9a](https://github.com/facebook/zstd/commit/63acf9a9955302c9595d6eccf3e8813256dfe069)
- Re-added extern "C" block in xxhash.h to support C++ compilation. (Architecture-related: public API)
  ↳ [#4218](https://github.com/facebook/zstd/pull/4218): [8f49db5](https://github.com/facebook/zstd/commit/8f49db5a022f5f77ad2c9a468b5929855bb6f36b)
- Fixed the problem that the resource compiler include directory path in the CMake build script is not quoted, ensuring that the path can be quoted correctly even if it contains spaces. (Architecture-related: build and installation methods)
  ↳ [#4269](https://github.com/facebook/zstd/pull/4269): [be1bf24](https://github.com/facebook/zstd/commit/be1bf2469e44952efb318f80b781e82e8e9e5183), [6cd4204](https://github.com/facebook/zstd/commit/6cd4204ee30c9d3a1ae00ca4082bf4b5c7e3dd7d)
- Windows build no longer adds the -pthread static link flag, and adds MinGW cross-compilation CI test. (Architecture-related: build and installation methods)
  ↳ [#3931](https://github.com/facebook/zstd/pull/3931): [5be2a87](https://github.com/facebook/zstd/commit/5be2a8721d527ae349539b459b35fb628467e00d)
- Provide a variant pkg-config file for the multi-threaded static library so that it can correctly contain the -pthread link and compile flag. (Architecture-related: pkg-config configuration)
  ↳ [#4020](https://github.com/facebook/zstd/pull/4020): [f1f1ae3](https://github.com/facebook/zstd/commit/f1f1ae369a4cefd3474b3528e8d1847b18750605)
- Fix the problem of wrong order of $filter parameters, and improve the recognition of MSYS/Cygwin environment. (Architecture-related: platform compatibility)
  ↳ [#4067](https://github.com/facebook/zstd/pull/4067): [f19c982](https://github.com/facebook/zstd/commit/f19c98228f773413850736b3aab574a63f03f2bc)
- Adjust libzstd dependency management in Meson builds, separate internal dependencies from public dependencies, avoid name conflicts caused by exporting private header files, and fix the construction of contrib and tests. (Architecture-related: build and installation methods)
  ↳ [#4153](https://github.com/facebook/zstd/pull/4153): [d2d49a1](https://github.com/facebook/zstd/commit/d2d49a11618bd3958b0501942b3525d9431008c1), [ccc02a9](https://github.com/facebook/zstd/commit/ccc02a9a7786c7556d31cfd3d7b08ba8d6895eea)
- Improved build system: Added Meson build target to facilitate local testing, and fixed the problem of incorrect use of environment variables in macOS build. (Architecture-related: platform compatibility)
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [cdddcaa](https://github.com/facebook/zstd/commit/cdddcaaec9111c4ab086a55e4d0337131ca13fd0) | [#4191](https://github.com/facebook/zstd/pull/4191): [d0fe334](https://github.com/facebook/zstd/commit/d0fe334c8552edb764b853854037697c6710fa64)
- Fixed portability issues with -z noexecstack flag in CMake builds. (Architecture-related: platform compatibility)
  ↳ [#4222](https://github.com/facebook/zstd/pull/4222): [f0937b8](https://github.com/facebook/zstd/commit/f0937b83d9a32cb2b59f99bbc4db717ae6e83c9b)
- Added compile-time macro support for old libc that does not support fseeko/ftello. (Architecture-related: platform compatibility)
  ↳ [#4229](https://github.com/facebook/zstd/pull/4229): [54c3d99](https://github.com/facebook/zstd/commit/54c3d998a04a4002697a3a44293074cb01df54a5)
- Increased the minimum version requirement of CMake from 3.10 to 3.14, and added Apple Framework build support. (Architecture-related: build and installation methods)
  ↳ [#4259](https://github.com/facebook/zstd/pull/4259): [897cec3](https://github.com/facebook/zstd/commit/897cec38760d1bb41e690225ba07b91c568e7cc8), [becef67](https://github.com/facebook/zstd/commit/becef672bb7c22af0fd723a4f8e4d279cf2a780a), [45c0e72](https://github.com/facebook/zstd/commit/45c0e72c0a481be824cc12fe6032ac685205d187)
- Added noexecstack compilation and linking flags to GCC/Clang, and added alignment attribute macro detection to the ClangCL compiler. (Architecture-related: platform compatibility)
  ↳ [#4284](https://github.com/facebook/zstd/pull/4284): [7b856e3](https://github.com/facebook/zstd/commit/7b856e3028518109eb34019e215802cda7cbafc1) | [#4286](https://github.com/facebook/zstd/pull/4286): [54e9d46](https://github.com/facebook/zstd/commit/54e9d46db44c4832d031100800f54a397358f896)
- Removed x32 ABI test task, and updated ARM64 test configuration, including QEMU system package and CFLAGS parameters. (Architecture-related: platform compatibility)
  ↳ [#4293](https://github.com/facebook/zstd/pull/4293): [75bcae1](https://github.com/facebook/zstd/commit/75bcae1272cbd6e417a9eb2c0e35e9f02828fba4), [2b7c661](https://github.com/facebook/zstd/commit/2b7c661ad2c022a56f6d0c58cbafa6f3d637ad4f), [fc1baf3](https://github.com/facebook/zstd/commit/fc1baf34637e7f230996cdc8ca259bf71809978a), [0b8119f](https://github.com/facebook/zstd/commit/0b8119f0ad0b027faffb7955b835718e049399e6)
- Strengthened GitHub Actions security of the Android NDK build workflow: restricted global permissions to read-only, and fixed dependent Action version hashes. (Architecture-related: build and installation methods)
  ↳ [#4299](https://github.com/facebook/zstd/pull/4299): [5c465fc](https://github.com/facebook/zstd/commit/5c465fcabeea65e642aaf70d1059958acd6acd69)
- Enabled Intel LLVM C Compiler (icx) checks in CI. (Architecture-related: Platform compatibility)
  ↳ [#4274](https://github.com/facebook/zstd/pull/4274): [8df6155](https://github.com/facebook/zstd/commit/8df6155495548d5db02b494fd8be23fad8c6cdfc)
- Added compilation tests for Visual Studio 2022, ClangCL toolset and AVX2 instruction set in CI. (Architecture-related: Platform compatibility)
  ↳ [#4286](https://github.com/facebook/zstd/pull/4286): [6e1d02f](https://github.com/facebook/zstd/commit/6e1d02f1f04f9c255108f84cc788b709e7871c2e)
- Migrated the ubuntu-20.04 running environment in CI testing to a newer Ubuntu version. (Architecture-related: platform compatibility)
  ↳ [#4293](https://github.com/facebook/zstd/pull/4293): [815ca8c](https://github.com/facebook/zstd/commit/815ca8c6784f59de825058b2b84bdb59b854feee)
- Adjusted the position and scope of extern "C" blocks in multiple header files to improve C++ compatibility, and removed extern "C" blocks from bitstream.h and fse.h to simplify header file structure. (Architecture-related: C++ compatibility)
  ↳ [#4218](https://github.com/facebook/zstd/pull/4218): [fc726da](https://github.com/facebook/zstd/commit/fc726da7747b159520de2edb0febab30342d2744), [fa5bfb6](https://github.com/facebook/zstd/commit/fa5bfb603065e0f426c3ede2b5e239a13b69ea22), [58a7f4b](https://github.com/facebook/zstd/commit/58a7f4b869e02e02ab7e119f20fca9ea631dd83d), [f25b9f1](https://github.com/facebook/zstd/commit/f25b9f11ba1df6e2a5bfe7e73e43c24c7c0906db), [07ffcc6](https://github.com/facebook/zstd/commit/07ffcc6b65a0eb95afc63a73e595384aef9f3552), [d51e607](https://github.com/facebook/zstd/commit/d51e6072a847f91610637e44feef972fd41167ea), [5222dd8](https://github.com/facebook/zstd/commit/5222dd87cff5533a83938d0e54b724f675266bf6), [a7bb6d6](https://github.com/facebook/zstd/commit/a7bb6d6c490a5b60b58666e73890c19921907e18), [d0d5ce4](https://github.com/facebook/zstd/commit/d0d5ce4c00469d4f11970e649e55217a659b4690), [c727d5c](https://github.com/facebook/zstd/commit/c727d5cd675dc04e07c0113d168ce93dc5624e54)
- Update the build system configuration, including Meson build fixes, updating the minimum version of CMake to 3.10 and adding the UNAME_TARGET_SYSTEM build flag. (Architecture-related: build and installation methods)
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [6939235](https://github.com/facebook/zstd/commit/6939235f010255bbe513dc5b18b1796cbee39d52) | [#4210](https://github.com/facebook/zstd/pull/4210): [e190e79](https://github.com/facebook/zstd/commit/e190e7944e42309a60b31c9d025c877219e7f878) | [#4220](https://github.com/facebook/zstd/pull/4220): [d06e877](https://github.com/facebook/zstd/commit/d06e8778bc4b150507abe0a8b7eaed08f2d16a17)

### Seekable Format Module
- Add null pointer check before creating seek table to avoid segfault. (Architecture-related: public API)
  ↳ [#4201](https://github.com/facebook/zstd/pull/4201): [b683c0d](https://github.com/facebook/zstd/commit/b683c0dbe278f71e371376847deebd44fdcf392f)

### Dictionary Builder Module
- The COVER algorithm dictionary training function is changed to be fully reentrant, using platform-related qsort_r/qsort_s instead of global variables to pass context, and providing a C90-compatible stable sort fallback implementation for BSD systems. (Architecture-related: platform compatibility)
  ↳ [#4086](https://github.com/facebook/zstd/pull/4086): [345bcb5](https://github.com/facebook/zstd/commit/345bcb5ff7001fbe2dfd59974808170c9e0f4d5d)

## Routine Changes

### New features
- Initial implementation of sequence conversion function, support for processing sequences longer than 65535, and added AVX2 acceleration path to improve performance.
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [8867204](https://github.com/facebook/zstd/commit/886720442f712b6e94c13075edaec1f224c1ae1a), [8d62164](https://github.com/facebook/zstd/commit/8d621645891a8ec8a114fe09e94f967f2049352b), [aa2cdf9](https://github.com/facebook/zstd/commit/aa2cdf964f93d96113c09028ad7354ca2debc849), [db3d488](https://github.com/facebook/zstd/commit/db3d48823a75a12a5ad9221e5a39191ff0044d3a), [debe3d2](https://github.com/facebook/zstd/commit/debe3d20d9ea0aaa45fbb692302347d0ece9f2c0) | [#4217](https://github.com/facebook/zstd/pull/4217): [95ad9e4](https://github.com/facebook/zstd/commit/95ad9e47ffa930d2facb5d2dd2de511bf8171e5d), [1ac79ba](https://github.com/facebook/zstd/commit/1ac79ba1b63f9e060d767380bca369051f6969be), [d48e330](https://github.com/facebook/zstd/commit/d48e330ae10a4042b85122213b0add998d6598f6) | [#4214](https://github.com/facebook/zstd/pull/4214): [50ca998](https://github.com/facebook/zstd/commit/50ca9984adcff0c298b4cf19a12cbee3372a6a0a)
- The CLI enables multi-threading by default, adjusts the calculation logic of the default number of threads, and optimizes the display information of benchmark tests.
  ↳ [#4211](https://github.com/facebook/zstd/pull/4211): [17beeb5](https://github.com/facebook/zstd/commit/17beeb5d1a978cb7775d37ee5f2b184368262ef5)
- In benchmark mode, the number of threads used will be displayed when using the -v option, and the display information of the benchmark test will be optimized.
  ↳ [#4235](https://github.com/facebook/zstd/pull/4235): [5650004](https://github.com/facebook/zstd/commit/56500044c4c517dc405c04e6933130684743cb89)
- When using the --long or --patch-from option, --ultra is automatically enabled without the user having to specify it explicitly.
  ↳ [#4289](https://github.com/facebook/zstd/pull/4289): [aebffd6](https://github.com/facebook/zstd/commit/aebffd66ec43a721b9d07e67e18f353bf2082430)
- Rolled back unnecessary free calls in gz_init().
  ↳ [#4025](https://github.com/facebook/zstd/pull/4025): [75d0f66](https://github.com/facebook/zstd/commit/75d0f66c879451e20f62f07162a38af2b314262a)
- Rename the variable name new to newfp to avoid conflict with C++ keywords.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [586ca96](https://github.com/facebook/zstd/commit/586ca96fec794cde09f4aa01fe792a9779b62368)

### bug fixes
- Fixed the ISO C incompatibility issue, replacing the empty initialization list of the structure with member-by-member assignment.
  ↳ [#4025](https://github.com/facebook/zstd/pull/4025): [4f41631](https://github.com/facebook/zstd/commit/4f41631aa4fffffac511d484ad10d603650e0156), [01cea2e](https://github.com/facebook/zstd/commit/01cea2e1e2cf1cafa4b61e1bc8eb85618cf18c76)
- Decompression error messages now always show the full original filename, no longer truncated.
  ↳ [#4011](https://github.com/facebook/zstd/pull/4011): [a2f145f](https://github.com/facebook/zstd/commit/a2f145f059150744132639cf30a918ceadac9b77)
- Fixed zlibWrapper build error, changed type conversion in gz_write function from z_uInt to uInt.
  ↳ [#4021](https://github.com/facebook/zstd/pull/4021): [71def59](https://github.com/facebook/zstd/commit/71def598906637866f1b165bc9113defdd36983c)
- Fixed multiple memory leaks and initialized variables to avoid undefined behavior.
  ↳ [#4025](https://github.com/facebook/zstd/pull/4025): [1d5e970](https://github.com/facebook/zstd/commit/1d5e9705db5933f5d89dc53d9312d6db5d3c423c)
- Fixed the null pointer dereference problem in legacy/zstd_v06 caused by the lack of check for ZSTDv06_createDCtx allocation failure, and added memory release and null pointer return processing on failure.
  ↳ [#4050](https://github.com/facebook/zstd/pull/4050): [1872688](https://github.com/facebook/zstd/commit/1872688e0adb630e8710cb3d17846ca49f596e46)
- Fixed an issue where pzstd could cause the thread to hang due to the work queue not ending correctly when decompressing a corrupted file.
  ↳ [#4080](https://github.com/facebook/zstd/pull/4080): [80af41e](https://github.com/facebook/zstd/commit/80af41e08a630946a75a5cda9e4cdf192247f20a)
- Fixed the formatString_u function so that it can correctly display numbers greater than 100, so that the benchmark can handle more than 100 files without the -S option.
  ↳ [#4113](https://github.com/facebook/zstd/pull/4113): [89451ca](https://github.com/facebook/zstd/commit/89451cafbd92a350b4a924d0020efbc775054378)
- In 32-bit mode, limit the range of index operations and use unsigned types to reduce the risk of negative numbers when operations cross 2GB boundaries.
  ↳ [#4129](https://github.com/facebook/zstd/pull/4129): [09cb37c](https://github.com/facebook/zstd/commit/09cb37cbb1be014756fbc00d3c5db8eaec20f32d)
- Fixed multiple issues with the block splitting strategy under incompressible data, including overlapping writing, lastBlock judgment, excessive splitting, etc.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [83a3402](https://github.com/facebook/zstd/commit/83a3402a928ef07700b1431c86534bec902ad11d), [5ae34e4](https://github.com/facebook/zstd/commit/5ae34e4c96265f1face970f3458836b3edf2e76d), [ea85dc7](https://github.com/facebook/zstd/commit/ea85dc7af6f97cbfc7fd1e6ff1515660e58501a3), [c80645a](https://github.com/facebook/zstd/commit/c80645a055d19f7e77cff3c268d818f811b9e1bb), [90095f0](https://github.com/facebook/zstd/commit/90095f056d4ccb8e0ed0942b2e30a664f0489932) | [#4180](https://github.com/facebook/zstd/pull/4180): [37706a6](https://github.com/facebook/zstd/commit/37706a677c09a1051f8b02361928c475bd094e67)
- Fixed the issue of files not being closed in the BMK_loadFiles function.
  ↳ [#4158](https://github.com/facebook/zstd/pull/4158): [8edd147](https://github.com/facebook/zstd/commit/8edd1476862222c4f0e88511241b83ab0e1948c4)
- Fixed the problem of incorrect parameter order in dfast compression strategy.
  ↳ [#4165](https://github.com/facebook/zstd/pull/4165): [83de003](https://github.com/facebook/zstd/commit/83de00316c29a7f5245a67733f6208c699b686c2)
- Fixed format issue when logging is enabled in 32-bit mode, corrected type names and format specifiers in debug logs.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [31d48e9](https://github.com/facebook/zstd/commit/31d48e9ffadde779e5fd9b290dee44f616b050fa)
- Fixed the problem of the benchmark module repeatedly displaying the loading summary in --quiet mode. Now the source file is only loaded once, and all compression levels are tested uniformly.
  ↳ [#4174](https://github.com/facebook/zstd/pull/4174): [0079d51](https://github.com/facebook/zstd/commit/0079d515b1673a7deba3dfa46204a1af61d81dce)
- Fixed space size constant used in static state allocation check.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [0be334d](https://github.com/facebook/zstd/commit/0be334d208b9fadd805a401ebcfdf6f253adae2a)
- Fixed type conversion warning in DEBUGLOG, changed format specifier from %lli to %i and explicitly converted parameter types.
  ↳ [#4180](https://github.com/facebook/zstd/pull/4180): [fcbf6b0](https://github.com/facebook/zstd/commit/fcbf6b014afebf4be07c5ba853f45513f1bd7f59)
- Fixed the problem of printing display error when the file size exceeds 4GB.
  ↳ [#4199](https://github.com/facebook/zstd/pull/4199): [194062a](https://github.com/facebook/zstd/commit/194062a4e73fef16e29e9175426fe1a3b9b23a73)
- Fixed forceNonContiguous field type changing from U32 to int to match actual usage.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [03d95f9](https://github.com/facebook/zstd/commit/03d95f9d135a9009b15567acf6f85b6e23534224)
- Fixed correctness of pointer difference calculation and parameter types in dictionary loading and compression end phases.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [5359d16](https://github.com/facebook/zstd/commit/5359d16d8d646b2010b9d5ac07fbf747d432fdfe)
- Restored the ZSTD_entropyCompressSeqStore call and changed the relevant parameters from srcSize to blockSize.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [47cbfc8](https://github.com/facebook/zstd/commit/47cbfc87a9c7ecb5a9058ad8e55ba19dcaf6a861)
- Fixed a bug where the optimal parser might generate too short matches when long distance matching is enabled, and changed the match length check from the hardcoded MINMATCH to the dynamic minMatch parameter.
  ↳ [#4223](https://github.com/facebook/zstd/pull/4223): [1548bfc](https://github.com/facebook/zstd/commit/1548bfc3497f45399daab58bcec4ab06a0878af1)
- Fixed the array index out-of-bounds access problem and added bounds check before access.
  ↳ [#4238](https://github.com/facebook/zstd/pull/4238): [e490be8](https://github.com/facebook/zstd/commit/e490be895cda9d1d6f707eaa86f8a72995960053)
- Fixed an array out-of-bounds access problem that may occur when the block delimiter is not found, and added corresponding error returns.
  ↳ [#4238](https://github.com/facebook/zstd/pull/4238): [afff3d2](https://github.com/facebook/zstd/commit/afff3d2cce1ad2e81b16459de5b572131949c44f)
- Fixed issue where cdict pointer was not properly reset to NULL in multi-threaded compression context.
  ↳ [#4276](https://github.com/facebook/zstd/pull/4276): [f11bd19](https://github.com/facebook/zstd/commit/f11bd19c7f7899840585a260688e969eb705a008)
- Rolled back the modification of passing the dictionary loading method as a parameter, restored the original dictionary loading behavior and updated the related type names synchronously.
  ↳ [#4276](https://github.com/facebook/zstd/pull/4276): [23e5f80](https://github.com/facebook/zstd/commit/23e5f80390db9a3a65485933d255e163d2dab519)
- Fixed boundary conditions in long distance matching mode parameter adjustment to ensure hash log values do not exceed the maximum allowed value.
  ↳ [#4288](https://github.com/facebook/zstd/pull/4288): [d5e4698](https://github.com/facebook/zstd/commit/d5e4698267b970545c349b3ed30a9168bcd165c3)
- Fix missing source file include in single library build.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [dd38c67](https://github.com/facebook/zstd/commit/dd38c677ebd680f29afdf4eab5c08d7a01eb8f39)
- Adjust the sample size and expected compression size of RLE detection test, and optimize the condition judgment logic.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [f83ed08](https://github.com/facebook/zstd/commit/f83ed087f6310a8cf51267ea431ec4a7b7ffd94f)
- Fixed the problem in minigzip.c that only the first element of the array was initialized to zero, instead the entire array was initialized to zero.
  ↳ [#4025](https://github.com/facebook/zstd/pull/4025): [b4ecf72](https://github.com/facebook/zstd/commit/b4ecf724b15f0ab21a996339112680d3f4ba33eb)
- Removed improper release of pointers in doc/educational_decoder/harness.c to fix potential memory errors.
  ↳ [#4025](https://github.com/facebook/zstd/pull/4025): [849b2ad](https://github.com/facebook/zstd/commit/849b2ad907070c6a46cc4679f4f831eaebacc715)
- Fixed the format problem of missing newline character at the end of the warning message in programs/dibio.c.
  ↳ [#4054](https://github.com/facebook/zstd/pull/4054): [4c6a519](https://github.com/facebook/zstd/commit/4c6a519fdd8caef500244b838beab7f7a160f70f)
- Fixed a warning caused by not using the return value of std::remove_if when compiling pzstd.
  ↳ [#4134](https://github.com/facebook/zstd/pull/4134): [a8b544d](https://github.com/facebook/zstd/commit/a8b544d460f3db9a79d630d95f1fa3564c29be12)
- Fix compilation issues in C90 strict mode, move variable declarations out of for loops and remove empty initializers.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [9e52789](https://github.com/facebook/zstd/commit/9e52789962bc5d47ee62bc3e499c52435c693e89)
- Fix incorrect pointer operation and return type declaration in result_get_error_string function.
  ↳ [#4157](https://github.com/facebook/zstd/pull/4157): [de6cc98](https://github.com/facebook/zstd/commit/de6cc98e07e1770b9f4571ea25dd6bf61612c08f)
- Fix kernel build error, add missing header file reference.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [8b3887f](https://github.com/facebook/zstd/commit/8b3887f579f7e98d09ec3823736b467ceaebbcd1)
- Fix incorrectly referenced variables in assert statements to ensure assertions check for correct parameters.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [20c3d17](https://github.com/facebook/zstd/commit/20c3d176cd8871d01fe8135bdc7693a208d739bc)
- Fix type conversion warning on Visual compiler.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [433f459](https://github.com/facebook/zstd/commit/433f4598ad96a4e661cfd877b50c9000ea174897)
- Fix type conversion warning, change streaming field type from unsigned to int.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [0a5c080](https://github.com/facebook/zstd/commit/0a5c0807afabfb46b95aff87b923bd421f315c0c)
- Fix type conversion warning, change explicit char type conversion to BYTE type to avoid sign extension issues.
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [4aaf9ce](https://github.com/facebook/zstd/commit/4aaf9cefe9bdda1fafb5f6a5ba13294d2b478bd7)
- Fixed alignment warnings caused by function parameter type mismatch, and added const void* cast.
  ↳ [#4287](https://github.com/facebook/zstd/pull/4287): [32dff04](https://github.com/facebook/zstd/commit/32dff04d320c2dc667380076dff5d575fcf73207)
- Fix alignment warning in _mm_storeu_si128 call, add void* intermediate conversion.
  ↳ [#4287](https://github.com/facebook/zstd/pull/4287): [c39424e](https://github.com/facebook/zstd/commit/c39424ea87288aec400305c3bc3cf1ec6ef7d803)
- Fixed alignment warning in Visual Studio compilation and added explicit type conversion.
  ↳ [#4287](https://github.com/facebook/zstd/pull/4287): [e117d79](https://github.com/facebook/zstd/commit/e117d79e22ae98be24d1867b0f2b8730e952c835)
- Fix redundant return statements in zstd_preSplit.c to pass strict C90 compliance testing.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [18b1e67](https://github.com/facebook/zstd/commit/18b1e67223823e48a96ed9f2ae489e8989802e42)
- Fix strict C90 compatibility issue, remove semicolon at the end of macro call.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [57239c4](https://github.com/facebook/zstd/commit/57239c4d3b5a21529ade206241f3f0a4815f2295)
- Fixed visual conversion warning caused by integer type mismatch in displacement operations.
  ↳ [#4176](https://github.com/facebook/zstd/pull/4176): [2366a87](https://github.com/facebook/zstd/commit/2366a87ddc7ed9ad54944404c57e506ea8bd79bc)
- Fix minor flaws in single_file_lib, delete sample header file zstd_errors.h.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [2503b64](https://github.com/facebook/zstd/commit/2503b64345b22d3f1729c2c380bc98500c8024aa)

### Refactoring optimization
- Rewrite the fingerprint storage structure, remove the 64-bit alignment member requirement, and make the structure support standard alignment; and rename FingerPrint to Fingerprint.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [b68ddce](https://github.com/facebook/zstd/commit/b68ddce818c274b9651ba47d45e46f7ffb4592ae), [4662f6e](https://github.com/facebook/zstd/commit/4662f6e646395b3f1902bc280991b82aefc1ba5d)
- Rename the enumeration ZSTD_cParamMode_e to ZSTD_CParamMode_e, and update the parameter types and comments of related functions simultaneously.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [4ef9d7d](https://github.com/facebook/zstd/commit/4ef9d7d585e8892dacd3f954848b91cd5e773ff7)
- Change the preprocessor condition from DYNAMIC_BMI2 != 0 to DYNAMIC_BMI2, migrate the STATIC_BMI2 macro definition to portability_macros.h, and uniformly use the STATIC_BMI2 macro check instead of ==1 comparison.
  ↳ [#4263](https://github.com/facebook/zstd/pull/4263): [1204626](https://github.com/facebook/zstd/commit/12046261382422494d7423cd39df553f236270ee) | [#4264](https://github.com/facebook/zstd/pull/4264): [1b15e88](https://github.com/facebook/zstd/commit/1b15e888fc1a2f5f84583b0df014c6032eb3a162) | [#4265](https://github.com/facebook/zstd/pull/4265): [f7e8fc3](https://github.com/facebook/zstd/commit/f7e8fc339b1ce64bbbfe3dc149b8cc0a13644844)
- Adjust the conditional judgment order of the STATIC_BMI2 macro definition: check the __BMI2__ macro first, and then use MSVC and __AVX2__ as alternatives.
  ↳ [#4264](https://github.com/facebook/zstd/pull/4264): [0a18362](https://github.com/facebook/zstd/commit/0a183620a3c21bce4ca3b10a12aba7d7f84c12b2)
- Update the internal type naming convention and rename buffer_t, range_t, serialState_t, syncPoint_t and other types to Buffer, Range, SerialState, SyncPoint starting with an uppercase letter.
  ↳ [#4276](https://github.com/facebook/zstd/pull/4276): [e637fc6](https://github.com/facebook/zstd/commit/e637fc64c5f918e316146fb1d78c1cb587b1134c)
- Fix pzstd compilation warning, use erase-remove idiom to delete elements instead.
  ↳ [#4134](https://github.com/facebook/zstd/pull/4134): [9215de5](https://github.com/facebook/zstd/commit/9215de52c7029bdad06d5fa59a4777edf0c92df9)
- Optimize the variable scope of frame header writing and compression block generation in ZSTD_compressSequences, and remove unused variables.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [bcb1509](https://github.com/facebook/zstd/commit/bcb15091aa7edc7d945a002d2d947577d999d7ea)
- Remove unused ZSTD_decompressSequences_t type definition.
  ↳ [#4266](https://github.com/facebook/zstd/pull/4266): [59afb28](https://github.com/facebook/zstd/commit/59afb28c977ab743b4430e8c284c41d209ac49eb)
- Roll back the FSE_readNCount_body function attribute, remove the special conditional compilation for the IAR compiler, and use FORCE_INLINE_TEMPLATE uniformly.
  ↳ [#4046](https://github.com/facebook/zstd/pull/4046): [5fadd8e](https://github.com/facebook/zstd/commit/5fadd8e6b1229e3116ba53a8cd34b678df403d97)
- Extract the index overlap check into an independent function ZSTD_index_overlap_check, and unify the calling method in each compression block function.
  ↳ [#4039](https://github.com/facebook/zstd/pull/4039): [5e9a6c2](https://github.com/facebook/zstd/commit/5e9a6c2fe4e4bfabeef750642871e3edcf6c6d79)
- Optimize the type conversion of pointer operations in ZSTD_window_update, adjust the log format and code style of ZSTD_cwksp_reserve_internal_buffer_space and ZSTD_cwksp_clear_tables.
  ↳ [#4109](https://github.com/facebook/zstd/pull/4109): [cb784ed](https://github.com/facebook/zstd/commit/cb784edf5de07940c0f48bae6cf8c4b2f4993705)
- Restore the complete equation expression without pre-simplification, allowing the compiler to optimize at compile time and improve code clarity.
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [87f0a4f](https://github.com/facebook/zstd/commit/87f0a4fbe0a1ffcaab4618f2aa76545e225acf07)
- Add an assertion at the entrance of the ZSTD_decompressStream function to ensure that the status pointer passed in is not empty.
  ↳ [#4249](https://github.com/facebook/zstd/pull/4249): [e8de808](https://github.com/facebook/zstd/commit/e8de8085f4a75fe46021b82851b72b07bb824c2b)
- When only hashLog is set, hashRateLog is deduced from hashLog, and the default value calculation logic of minMatchLength and bucketSizeLog is adjusted.
  ↳ [#4288](https://github.com/facebook/zstd/pull/4288): [67fad95](https://github.com/facebook/zstd/commit/67fad95f7971b97085fb838e3aa47cd37e9d7908)
- Adjust the calculation method of hash rate parameters at low compression levels to slightly increase the compression ratio while maintaining speed.
  ↳ [#4288](https://github.com/facebook/zstd/pull/4288): [72406b7](https://github.com/facebook/zstd/commit/72406b71c30efbfe865611a79f50117254820c40)
- Adjust long-distance matching mode parameters and optimize compression ratio.
  ↳ [#4288](https://github.com/facebook/zstd/pull/4288): [09d7e34](https://github.com/facebook/zstd/commit/09d7e34ed8c138e913d8c11724f2d5fb5a1436bd)

### Test related
- Fixed buffer size calculation and offset calculation errors in sequence preparation phase in fullbench benchmark.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [ad023b3](https://github.com/facebook/zstd/commit/ad023b392fc5081f53ebc30f68d6e8dfda256104), [52a9bc6](https://github.com/facebook/zstd/commit/52a9bc6fca23bf0f9d51be0fe97a525db85aa12b)
- Added new tests for ZSTD_compressSequencesAndLiterals, covering frame header verification, incompressible data error codes, invalid call fixes, and adjusted auxiliary functions.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [a80f55f](https://github.com/facebook/zstd/commit/a80f55f47d7d4076c19a000459b88e28e8c95eee), [f8725e8](https://github.com/facebook/zstd/commit/f8725e80cc6089ec21903e292a58a21d322e302b), [7b294ca](https://github.com/facebook/zstd/commit/7b294caf461a15d74e64389bde16d5c33fc3d0c8), [72ce56b](https://github.com/facebook/zstd/commit/72ce56b527d1710dd2fa193ca0c22933da382f44), [0b013b2](https://github.com/facebook/zstd/commit/0b013b26884bb25149eedc6d78a5d8f5dc38739a)
- Added verification function support in the fullbench benchmark framework to verify compression results; added sequence conversion and block summary test scenarios, and reconstructed the decoupling of the preparation function and the benchmark test function.
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [d1f0e5f](https://github.com/facebook/zstd/commit/d1f0e5fb9738073150e7e5c25b03444b5a6a5389), [bfc58f5](https://github.com/facebook/zstd/commit/bfc58f5ba24a3c27edfbc61288e09d2837235456) | [#4217](https://github.com/facebook/zstd/pull/4217): [09964c6](https://github.com/facebook/zstd/commit/09964c62762186da7ab54b0081071c2bcb7626f4), [4c097b4](https://github.com/facebook/zstd/commit/4c097b49396c8768c11e65688def8f3da7eac729), [c540976](https://github.com/facebook/zstd/commit/c540976a4bff384690da03d8c634fbc8449ff4c7), [8b7e1b7](https://github.com/facebook/zstd/commit/8b7e1b795d50b69f44b5306511116251f60d1dda), [c050ae4](https://github.com/facebook/zstd/commit/c050ae4fb89bc17fd9591558e44d01e627039576), [8ab0409](https://github.com/facebook/zstd/commit/8ab04097ed9736923405e4928f928e49654e2c9a), [ac05ea8](https://github.com/facebook/zstd/commit/ac05ea89a5e87cf9e9756790f08b9d21b349fd9e)
- Fixed compilation warnings in test files, including format specifier mismatch and implicit type conversion, for compatibility with older versions of MinGW and Visual Studio.
  ↳ [#4287](https://github.com/facebook/zstd/pull/4287): [f9c1850](https://github.com/facebook/zstd/commit/f9c1850aa2df6024e930b257067401108fa268ef), [590c224](https://github.com/facebook/zstd/commit/590c22454e24c0247f60a5fd939a1c4f1d49e896), [e87d159](https://github.com/facebook/zstd/commit/e87d15938c888011cdcc7aa6d45a85ea055a5da8), [2949252](https://github.com/facebook/zstd/commit/294925292304b3c5b5e975f9036a684881dba469) | [#3991](https://github.com/facebook/zstd/pull/3991): [81a5e5d](https://github.com/facebook/zstd/commit/81a5e5d4384342c0312198f4db35b8cdabc30d96) | [#4217](https://github.com/facebook/zstd/pull/4217): [61ac831](https://github.com/facebook/zstd/commit/61ac8311e0983d21b95d5ef8ac98477b348a806e)
- Split the zlib wrapper test steps into independent steps to facilitate locating the cause of CI failure.
  ↳ [#4243](https://github.com/facebook/zstd/pull/4243): [43626f1](https://github.com/facebook/zstd/commit/43626f1ce0ae4f7f3a9f6d5b7b04f54566d49b52)
- Disabled BTI testing to adapt to Ubuntu 24.04 environment.
  ↳ [#4293](https://github.com/facebook/zstd/pull/4293): [2a58b04](https://github.com/facebook/zstd/commit/2a58b047529ca385867fea53b4077526bb10486e)
- Updated the test name, and added dictionary compression and decompression test files.
  ↳ [#4298](https://github.com/facebook/zstd/pull/4298): [ff7a151](https://github.com/facebook/zstd/commit/ff7a151f2e6c009b657d9f798c2d9962b0e3feb5)
- Added advanced options to the decodecorpus testing tool, supporting forced specification of block types, literal types, etc.
  ↳ [#4102](https://github.com/facebook/zstd/pull/4102): [1f5df58](https://github.com/facebook/zstd/commit/1f5df587fa3edbbf2faf24ef2f0941652663305f)
- Fixed expected compression size value in dictionary compression test case.
  ↳ [#4170](https://github.com/facebook/zstd/pull/4170): [730d2dc](https://github.com/facebook/zstd/commit/730d2dce41800d2850726cdb0eefbf5fcb10b3de)
- Fixed an issue with insufficient compressed output buffer margin in test cases.
  ↳ [#4171](https://github.com/facebook/zstd/pull/4171): [61d08b0](https://github.com/facebook/zstd/commit/61d08b0e42e7397af479ca9d1b66fe7235508f34)
- Fixed decompression buffer size parameter error in zstreamtest.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [80a912d](https://github.com/facebook/zstd/commit/80a912dec1e5ec1fad6e6a698cfe04685c0d865e)
- Fixed incorrect assertion values in fullbench.c test file.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [f617e86](https://github.com/facebook/zstd/commit/f617e86b71f71267b5ffc31aafb46c7ba83ee9e7)
- Fixed the zlib test to adapt to the error code changes in the new version of the library.
  ↳ [#4243](https://github.com/facebook/zstd/pull/4243): [0b96e6d](https://github.com/facebook/zstd/commit/0b96e6d42a9b22eb472a050fcd2cc4be3ffb8e2b)

### Performance optimization
- In the fast compression strategy, conditional move instructions are used to replace branches, and the strategy is automatically selected based on the window size, improving performance by about 10%.
  ↳ [#4165](https://github.com/facebook/zstd/pull/4165): [e8fce38](https://github.com/facebook/zstd/commit/e8fce38954efd6bc58a5b0ec72dd26f41c8365e6), [2cc600b](https://github.com/facebook/zstd/commit/2cc600bab21657ccf966ceadfeb316e2eacff25c), [186b132](https://github.com/facebook/zstd/commit/186b1324951f2505469a3415aaf8ddc3398b9fca), [1e7fa24](https://github.com/facebook/zstd/commit/1e7fa242f4aa71c3aec5e1e39ec69ad54e117051), [197c258](https://github.com/facebook/zstd/commit/197c258a79a94b60ec45020defc5fb6a2f570e80), [741b860](https://github.com/facebook/zstd/commit/741b860fc1e8171519a72bf3d30cdd20995b00ce), [fa1fcb0](https://github.com/facebook/zstd/commit/fa1fcb08ab447de8cdb4492d663779cad6841379), [8e5823b](https://github.com/facebook/zstd/commit/8e5823b65c6d0d1eb1c07be8428f427df5892d3a)
- Optimize dictionary compression speed: Improved match detection logic under fast strategy.
  ↳ [#4170](https://github.com/facebook/zstd/pull/4170): [e63896e](https://github.com/facebook/zstd/commit/e63896eb5844cb246aad7959ab208aa0a8f152bd)
- Optimize the matching logic of level 3 dictionary compression: simplify conditional judgment and introduce a new index overlap check function, slightly improving the compression ratio.
  ↳ [#4170](https://github.com/facebook/zstd/pull/4170): [c2abfc5](https://github.com/facebook/zstd/commit/c2abfc5ba40b2c7863080c937b728fb902b9cb5b)
- Optimize the selection logic of long match candidates in compression levels 3 and 4: only use it if the candidate match is indeed longer, slightly improving the compression ratio.
  ↳ [#4171](https://github.com/facebook/zstd/pull/4171): [6326775](https://github.com/facebook/zstd/commit/632677516616434c312d2fff2d84dcf0c9b78012)
- Optimize the selection logic of long matching candidates in the dfast strategy: only use it when the candidate matching is really longer to improve the compression rate.
  ↳ [#4171](https://github.com/facebook/zstd/pull/4171): [47d4f56](https://github.com/facebook/zstd/commit/47d4f5662df83c1a84476ab6c6f7fcb1d415f4f1)
- Introducing a faster block splitting variant: speeded up by sampling every 5 positions, applied to lazy2 and btlazy2 compression strategies.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [a167571](https://github.com/facebook/zstd/commit/a167571db535377070c43098932a7747d859177c)
- Optimize the sequence processing flow: unnecessary tracking and branches are removed, and the compression speed is increased by about 4%.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [1c8f5b0](https://github.com/facebook/zstd/commit/1c8f5b0f11c9fbcd47135a658dca9b927a0b27b7), [a288751](https://github.com/facebook/zstd/commit/a288751de78e3dd69dfacfe74d3f35c534b57096), [1f6d681](https://github.com/facebook/zstd/commit/1f6d6815c3fc4b6d1f406e01849c49b15518ba54)
- Optimize the compression speed and memory usage of --patch-from mode: avoid repeated memory references and adjust parameters to improve compression ratio and speed.
  ↳ [#4276](https://github.com/facebook/zstd/pull/4276): [ffa66a6](https://github.com/facebook/zstd/commit/ffa66a6971010057a5918ddc54531bec7bf18842), [34ba144](https://github.com/facebook/zstd/commit/34ba14437aeeb5e678ae7f1dbdfa6333beb2723b), [220abe6](https://github.com/facebook/zstd/commit/220abe6da857142305ab7337b346c826856bcfd1), [7406d2b](https://github.com/facebook/zstd/commit/7406d2b6eb91851db6a1cef10121de2a4c5a794a) | [#4288](https://github.com/facebook/zstd/pull/4288): [4609a40](https://github.com/facebook/zstd/commit/4609a40b89b94cc61cc6a6a833725d6f89bf9de6)
- Optimize the fluency of multi-threaded compression: separate sequence generation from sequence application to avoid blocking the first job when loading the dictionary.
  ↳ [#4276](https://github.com/facebook/zstd/pull/4276): [c7cd7dc](https://github.com/facebook/zstd/commit/c7cd7dc04bede050475da32fa019c2d0712ed6cf)
- Dynamically adjust the bucket size parameters of long-distance matching mode: automatically increase the bucket size at high compression levels to improve compression ratio.
  ↳ [#4288](https://github.com/facebook/zstd/pull/4288): [f26cc54](https://github.com/facebook/zstd/commit/f26cc54f37c614d3351b6873f0ee6e3fff00f6f6)

### Security related
- No significant changes.

### Documentation
- Updated the format specification document, reconstructed the FSE decoding table construction instructions, added ascending order examples, corrected terminology, and clarified that the decoder can reject non-zero probability frames that exceed the maximum offset code.
  ↳ [#4013](https://github.com/facebook/zstd/pull/4013): [c54f478](https://github.com/facebook/zstd/commit/c54f4783d0cd51d8aad1c0a4fd9fe564d461aae4) | [#4159](https://github.com/facebook/zstd/pull/4159): [a8b86d0](https://github.com/facebook/zstd/commit/a8b86d024a2e5ca7029ab19f7638cd6ca42bde1a) | [#4164](https://github.com/facebook/zstd/pull/4164): [3e7c66a](https://github.com/facebook/zstd/commit/3e7c66acd1b6dab2473a996adac027dacf648d0a)
- Updated the zstd.1 manual, corrected the description of the compression level limit used with --single-thread and --patch-from, and updated the description of the default value of the long-distance matching mode parameter.
  ↳ [#4094](https://github.com/facebook/zstd/pull/4094): [b320d09](https://github.com/facebook/zstd/commit/b320d096a44b592d5f5bcda37e323b799c0cef57) | [#4288](https://github.com/facebook/zstd/pull/4288): [339bca6](https://github.com/facebook/zstd/commit/339bca66066e4a099bc91d04265c9bfbf15001bb)
- Updated the command line help text, added a description of the -D option, and updated the LDM documentation tips and parameter suggestions in --patch-from mode.
  ↳ [#4146](https://github.com/facebook/zstd/pull/4146): [039f404](https://github.com/facebook/zstd/commit/039f404faa9230e389b360c80d6c842fae3f75a0) | [#4288](https://github.com/facebook/zstd/pull/4288): [bf218c1](https://github.com/facebook/zstd/commit/bf218c142aade4aa842205e93bc8260dcbfb372d)
- Add a description to the automatically generated HTML manual to inform users that the file was automatically generated by parsing zstd.h.
  ↳ [#4184](https://github.com/facebook/zstd/pull/4184): [2e02cd3](https://github.com/facebook/zstd/commit/2e02cd330dee3fcf9a8609b90ed7b965e0a6f9a1)
- Update the CHANGELOG file to add the change record of v1.5.7 version.
  ↳ [#4297](https://github.com/facebook/zstd/pull/4297): [c26bde1](https://github.com/facebook/zstd/commit/c26bde119ba984ae1f2efe76d610eb50d152b1ec)

### Build/CI
- Upgraded msys2/setup-msys2 actions used in CI from v2.23.0 to v2.26.0 to fix Node.js deprecation warning.
  ↳ [#4106](https://github.com/facebook/zstd/pull/4106): [46a3135](https://github.com/facebook/zstd/commit/46a3135524b1ea9cd46ea5cd61529f1231606465) | [#4111](https://github.com/facebook/zstd/pull/4111): [688a815](https://github.com/facebook/zstd/commit/688a815c8643c8ea2475ac90bdd261bbcc43631b) | [#3996](https://github.com/facebook/zstd/pull/3996): [ebf24b7](https://github.com/facebook/zstd/commit/ebf24b7b77ed3b4430e7dd3ef45104d05d3585a6) | [#4040](https://github.com/facebook/zstd/pull/4040): [4356192](https://github.com/facebook/zstd/commit/4356192cb2a16975720a04ac5681a495e7ef1acc) | [#4196](https://github.com/facebook/zstd/pull/4196): [a9d279c](https://github.com/facebook/zstd/commit/a9d279c97c76f3d5018f96fd4f65b28cb501e3ad) | [#4208](https://github.com/facebook/zstd/pull/4208): [c254ea0](https://github.com/facebook/zstd/commit/c254ea097b017cac8f9b33856370afb729048035)
- Fixed failure due to missing liblzma dependency in Meson and CMake Linux build tests, explicitly installing the liblzma-dev package in CI.
  ↳ [#4243](https://github.com/facebook/zstd/pull/4243): [0e819c9](https://github.com/facebook/zstd/commit/0e819c9f933a6b1193cfa26453ba967eb198af13), [80ff61d](https://github.com/facebook/zstd/commit/80ff61de1de352fb14d4bee6de7f7dd1e254da38), [196e76e](https://github.com/facebook/zstd/commit/196e76efe16623c4a1aa5d636298b59f392671b5)
- Use the system's own md5sum instead of gmd5sum on FreeBSD.
  ↳ [#3994](https://github.com/facebook/zstd/pull/3994): [103a85e](https://github.com/facebook/zstd/commit/103a85e6f64f305684db354a0eb9a10d5c586d5c)
- Fixed the issue of resource compiler missing include directory in CMake build, and set the correct include path for rc.
  ↳ [#4019](https://github.com/facebook/zstd/pull/4019): [fd5f810](https://github.com/facebook/zstd/commit/fd5f8106a58601a963ee816e6a57aa7c61fafc53)
- Fixed macOS build issues and renamed CI task to make-test-macos.
  ↳ [#4076](https://github.com/facebook/zstd/pull/4076): [80170f6](https://github.com/facebook/zstd/commit/80170f6aad9f48574b108584e7504b0f9254958f)
- Fixed the gen_html build error under Windows and added extension variable support for the gen_html command in the Makefile.
  ↳ [#4087](https://github.com/facebook/zstd/pull/4087): [1f72f52](https://github.com/facebook/zstd/commit/1f72f52bc1efd943f390a3dec3b569cf49f7a83a)
- Fixed the spelling error of LIB_BINDIR definition in lib/libzstd.mk, and solved the problem that the libzstd library cannot be found during linking.
  ↳ [#4096](https://github.com/facebook/zstd/pull/4096): [5d63f18](https://github.com/facebook/zstd/commit/5d63f186cce4bb21fde156492fe945f2ae69104c)
- Upgraded ossf/scorecard-action from 2.3.1 to 2.4.0.
  ↳ [#4104](https://github.com/facebook/zstd/pull/4104): [efbb5ef](https://github.com/facebook/zstd/commit/efbb5ef01596880cfd87d09a35c7599504ee3bce)
- Fixed the issue where multi-threading and other feature detection failed due to -Werror=missing-profile when building PGO.
  ↳ [#4119](https://github.com/facebook/zstd/pull/4119): [bf4a43f](https://github.com/facebook/zstd/commit/bf4a43fcd45aea991d273160262a31925ea31ba3)
- Improved GitHub Actions CI workflow: fixed dependency issues for nightly testing and enabled regression testing.
  ↳ [#4160](https://github.com/facebook/zstd/pull/4160): [b84653f](https://github.com/facebook/zstd/commit/b84653fc839367281481bc3fee9f9d7e8496701f) | [#4171](https://github.com/facebook/zstd/pull/4171): [ff8e98b](https://github.com/facebook/zstd/commit/ff8e98bebee144321d7c39234deff43f9211dfbc)
- Updated the FreeBSD man page installation directory.
  ↳ [#4231](https://github.com/facebook/zstd/pull/4231): [0fd5210](https://github.com/facebook/zstd/commit/0fd521048d9304e2e06020bebcfb0b481261b2fc)
- Updated the lib64gcc version of cross-compilation dependency in CI.
  ↳ [#4243](https://github.com/facebook/zstd/pull/4243): [d4ae5c3](https://github.com/facebook/zstd/commit/d4ae5c3752c0f4a918cadcfb9489c91e59bb1f47)
- Upgraded CodeQL Action to the latest version.
  ↳ [#3988](https://github.com/facebook/zstd/pull/3988): [101e601](https://github.com/facebook/zstd/commit/101e601c793e9d4dbdffaf05331774bca2aa12be) | [#4022](https://github.com/facebook/zstd/pull/4022): [7968c66](https://github.com/facebook/zstd/commit/7968c661af8ec976782ddcfde3ea609d9353a0cf) | [#4029](https://github.com/facebook/zstd/pull/4029): [68a6d9b](https://github.com/facebook/zstd/commit/68a6d9b9f6ce605010ea1164590e4e015567dee7) | [#4128](https://github.com/facebook/zstd/pull/4128): [ec0c414](https://github.com/facebook/zstd/commit/ec0c41414d5d41e6e49b5bd7402a7252ad91e7e7) | [#4194](https://github.com/facebook/zstd/pull/4194): [2d1bbc3](https://github.com/facebook/zstd/commit/2d1bbc37ebf4cbf48a2f107a3816f3e137fb5d49)
- Optimized the 32-bit CI test process, including adjusting the compilation optimization level, enabling parallel testing and replacing test names.
  ↳ [#4167](https://github.com/facebook/zstd/pull/4167): [1024aa9](https://github.com/facebook/zstd/commit/1024aa9252ff02ebc03511a2c0311957511d0be9), [6f2e29a](https://github.com/facebook/zstd/commit/6f2e29a234c9f9ca63f1dd2748933a03f03ac731), [e674035](https://github.com/facebook/zstd/commit/e6740355e35fa5695cb606e7bbda41b595175b3a) | [#4136](https://github.com/facebook/zstd/pull/4136): [7f015c2](https://github.com/facebook/zstd/commit/7f015c2fd799d3c273c5986a63059ef9536b701e)
- Cleaned up build targets, replaced shortest with check, and added test success messages.
  ↳ [#4247](https://github.com/facebook/zstd/pull/4247): [7827514](https://github.com/facebook/zstd/commit/78275149ead3bfc068d58a67480653740da5a86b), [4f3311f](https://github.com/facebook/zstd/commit/4f3311f245fedb99d65baca98cd33f6ec41a6589)
- Upgraded cygwin-install-action to v5.
  ↳ [#4254](https://github.com/facebook/zstd/pull/4254): [056492e](https://github.com/facebook/zstd/commit/056492e31b80fa746c187a5078e96163437c8739), [e39ed41](https://github.com/facebook/zstd/commit/e39ed414350313e8170d96c8fc82b3d0c2e67a6a)
- Change the running environment of sanitizer CI jobs from ubuntu-20.04 back to ubuntu-latest.
  ↳ [#4213](https://github.com/facebook/zstd/pull/4213): [7236e05](https://github.com/facebook/zstd/commit/7236e05b0a4f5e9c9435661fe7b2bfedeba29ec4)
- Added Cygwin installation test step to CI workflow.
  ↳ [#4073](https://github.com/facebook/zstd/pull/4073): [d7a84a6](https://github.com/facebook/zstd/commit/d7a84a683fe345342139660b9d3a36328ed5f4b3)
- Upgraded actions/setup-java from v3 to v4.
  ↳ [#4122](https://github.com/facebook/zstd/pull/4122): [aed3c75](https://github.com/facebook/zstd/commit/aed3c7540a904b2dbb12fd88038bd09d743ca05d)
- Removed CircleCI-based nightly test configuration and related Docker images and workflow files.
  ↳ [#4156](https://github.com/facebook/zstd/pull/4156): [3d5d3f5](https://github.com/facebook/zstd/commit/3d5d3f5630acdb14ddd94721b2011dca8eaf496a)
- Modified the CMake version checking logic, changed VERSION_LESS to VERSION_GREATER_EQUAL and removed the annotation dependency on CMake 3.7.
  ↳ [#4210](https://github.com/facebook/zstd/pull/4210): [1198a58](https://github.com/facebook/zstd/commit/1198a582d3c931c7faba149cbf1b48910da3f256)
- Fixed clang-pgo tests in CI, switched compiler from clang-14 to generic clang, and adjusted gcc-pgo test configuration.
  ↳ [#4243](https://github.com/facebook/zstd/pull/4243): [908a958](https://github.com/facebook/zstd/commit/908a95889b2bbcdb30e945ac12e0b6b2e025fa4d)
- Split the test steps in CI into multiple independent named steps to provide a clearer view of the execution of each test.
  ↳ [#4243](https://github.com/facebook/zstd/pull/4243): [642157c](https://github.com/facebook/zstd/commit/642157cc450c5e2b1c5703ba0a164514ce29061a)
- Upgraded CodeQL Action dependency version.
  ↳ [#4255](https://github.com/facebook/zstd/pull/4255): [5b9c5d4](https://github.com/facebook/zstd/commit/5b9c5d4929cea7b3a134f44887bfffeefd448500) | [#4291](https://github.com/facebook/zstd/pull/4291): [7a2fce5](https://github.com/facebook/zstd/commit/7a2fce5a1fabcd28cc8c8ea5ef039dab32b24f0b)
- Removed duplicate INCLUDES DESTINATION lines in CMakeLists.txt.
  ↳ [#4271](https://github.com/facebook/zstd/pull/4271): [de7c8b9](https://github.com/facebook/zstd/commit/de7c8b984236654a567b7b743913849fa6806e8e)
- Enabled warnings as errors in Visual Studio build tests.
  ↳ [#4287](https://github.com/facebook/zstd/pull/4287): [5883ee6](https://github.com/facebook/zstd/commit/5883ee6cc2303259f6a5ca824d9b9786c223df54)
- Optimized build commands for ARM64 tests to speed up test execution.
  ↳ [#4293](https://github.com/facebook/zstd/pull/4293): [85c39b7](https://github.com/facebook/zstd/commit/85c39b78cfabf64fe0d8859f3c4ac5f240d52fc8)
- Pin dependency actions in GitHub Actions workflows to specific hash versions.
  ↳ [#4299](https://github.com/facebook/zstd/pull/4299): [b14d76d](https://github.com/facebook/zstd/commit/b14d76d88810f2984e0cd9ebd307269843a5d7d9)
- Removed debug output statements in Makefile.
  ↳ [#4220](https://github.com/facebook/zstd/pull/4220): [5a7f5c7](https://github.com/facebook/zstd/commit/5a7f5c745cfb7135f27002efc79fee1804d21d44)
- Cleaned up debug output in CMake build scripts, and updated messages for compilation definitions under the Android old API.
  ↳ [#4229](https://github.com/facebook/zstd/pull/4229): [757e29e](https://github.com/facebook/zstd/commit/757e29e170565ac48ff7d893a4cc421e0450dd72)

### Maintenance
- Fixed comment style in code that does not comply with C90 standards.
  ↳ [#4136](https://github.com/facebook/zstd/pull/4136): [6dc5212](https://github.com/facebook/zstd/commit/6dc52122e6e8b28b8477a202726dfff7d0ce0b9c)
- Removed incorrect header file inclusion automatically added by the editor.
  ↳ [#4232](https://github.com/facebook/zstd/pull/4232): [cd53924](https://github.com/facebook/zstd/commit/cd53924eff684146b67e890d7b48158c37eca32c)
- Updated the description of benchmark mode in the man page and README, and displays level 0 when decompressing benchmark.
  ↳ [#4174](https://github.com/facebook/zstd/pull/4174): [f34bc9c](https://github.com/facebook/zstd/commit/f34bc9cee63759a85011db66e5cb9187c88ea843)
- Fixed the initialization method of character array in minigzip.c to avoid undefined behavior.
  ↳ [#4025](https://github.com/facebook/zstd/pull/4025): [0b24fc0](https://github.com/facebook/zstd/commit/0b24fc0a113c92c5ba5ec78f7169a2ddfe0d700f)
- Fixed the syntax error of conditional compilation in programs/util.h, changing #if not to #if !.
  ↳ [#4218](https://github.com/facebook/zstd/pull/4218): [ded4c1e](https://github.com/facebook/zstd/commit/ded4c1ec18bf39db0ce6b4263ddf6daac6712e94)
- Added rules to ignore generated framework and xcframework artifacts in .gitignore.
  ↳ [#4259](https://github.com/facebook/zstd/pull/4259): [03d5ad6](https://github.com/facebook/zstd/commit/03d5ad6fed5882a300289e5fa8a238f2fec29300)
- Improved alignment of ratio display in benchmark results, especially display accuracy when ratio is greater than 100.
  ↳ [#4278](https://github.com/facebook/zstd/pull/4278): [60f84f7](https://github.com/facebook/zstd/commit/60f84f73fed4cb94c166e1dadf3f96ec71a7792c)
- Changed the block header writing of empty frames from 4 bytes to 3 bytes, and adjusted the target capacity check accordingly.
  ↳ [#4217](https://github.com/facebook/zstd/pull/4217): [522adc3](https://github.com/facebook/zstd/commit/522adc34eb83c9145dfe1be36412eefa642413e1)

### Others
- Updated the compression format documentation, removed outdated descriptions, updated the version number to 0.4.3, and clarified the Huffman prefix code description.
  ↳ [#4012](https://github.com/facebook/zstd/pull/4012): [8cff66f](https://github.com/facebook/zstd/commit/8cff66f2f53fa41b8f5be65996600d88fbbe1a98) | [#4164](https://github.com/facebook/zstd/pull/4164): [3b343dc](https://github.com/facebook/zstd/commit/3b343dcfb140ccb278a781faa8116d273f36e4a1)
- Fixed multiple spelling errors in code comments, API documentation and macro definitions.
  ↳ [#4068](https://github.com/facebook/zstd/pull/4068): [2d736d9](https://github.com/facebook/zstd/commit/2d736d9c50057e6d1f33c175e126590816c54251), [44e83e9](https://github.com/facebook/zstd/commit/44e83e9180ee326353f98e680a7769d4b76f4c25) | [#4143](https://github.com/facebook/zstd/pull/4143): [7a48dc2](https://github.com/facebook/zstd/commit/7a48dc230c42ba4d779fab4e68da14f44c92a7b3) | [#4205](https://github.com/facebook/zstd/pull/4205): [fcf88ae](https://github.com/facebook/zstd/commit/fcf88ae39b560f8605f8e7c56e243cb1a3a98e5c) | [#4237](https://github.com/facebook/zstd/pull/4237): [f5dbdac](https://github.com/facebook/zstd/commit/f5dbdac81879e34a4dfffb77dd7769c536a9b702)
- Update the ZSTD_splitBlock() function comment and adjust the level parameter range to 0 to 4.
  ↳ [#4178](https://github.com/facebook/zstd/pull/4178): [5b4ce64](https://github.com/facebook/zstd/commit/5b4ce643f03a2cc2c6f4e10dca3332c058f165d5)
- Fixed a C90 comment style, changing C++ style comments to C style.
  ↳ [#4113](https://github.com/facebook/zstd/pull/4113): [14b8d39](https://github.com/facebook/zstd/commit/14b8d398fd0f9155203031239748537e7df2ad75)
- Update test related files, including .gitignore and remove debug output.
  ↳ [#4171](https://github.com/facebook/zstd/pull/4171): [41d870f](https://github.com/facebook/zstd/commit/41d870fbbf594c1ee1c0ac4113d1278ebf8301da) | [#4180](https://github.com/facebook/zstd/pull/4180): [f593ccd](https://github.com/facebook/zstd/commit/f593ccda04f89be6fc4f966b9b816d542941771f)
- Adjust and clean up the code format, including removing unnecessary declarations, adjusting the location of header files, unifying the indentation format and removing unused variables.
  ↳ [#4218](https://github.com/facebook/zstd/pull/4218): [10b9d81](https://github.com/facebook/zstd/commit/10b9d81909f8631e3ac64bd45e3bdd04982e39d6), [c7af042](https://github.com/facebook/zstd/commit/c7af0428c6cceac32a192392d954dc8e6e1ba79a) | [#4229](https://github.com/facebook/zstd/pull/4229): [6b046f5](https://github.com/facebook/zstd/commit/6b046f58410fe66ea300c31ffc92dbfb4c956bb1), [dfb236b](https://github.com/facebook/zstd/commit/dfb236b2aa58d3460945f5112e8d5388d7c4a666) | [#4250](https://github.com/facebook/zstd/pull/4250): [27d7940](https://github.com/facebook/zstd/commit/27d794063162096e3a4be7d2d3f80ce117a5592d) | [#4232](https://github.com/facebook/zstd/pull/4232): [57a4554](https://github.com/facebook/zstd/commit/57a45541927180724712b651ed1fb3e125105f30)
- Updated STATIC_BMI2 macro comments to describe compile-time BMI2 support detection more concisely.
  ↳ [#4264](https://github.com/facebook/zstd/pull/4264): [d486ccc](https://github.com/facebook/zstd/commit/d486ccc9e90a9d2e0095f9a81cbf29f72bac4f37)
- Updated comments in ZSTDMT_createCompressionJob to describe prefix settings more accurately.
  ↳ [#4276](https://github.com/facebook/zstd/pull/4276): [85a44b2](https://github.com/facebook/zstd/commit/85a44b233accb544d89c85b804182e3f34e8d4b1)
- Enhance the warning in the man page that the --max option consumes excessive resources on 32-bit systems.
  ↳ [#4290](https://github.com/facebook/zstd/pull/4290): [f86024c](https://github.com/facebook/zstd/commit/f86024ccd2b2fc4608be336594e073096405ac13)
- Updated comments about hashRateLog mapping in zstd_ldm.c.
  ↳ [#4288](https://github.com/facebook/zstd/pull/4288): [d2c562b](https://github.com/facebook/zstd/commit/d2c562b803a4c49dbd5afb1717db095aae1557b1)
