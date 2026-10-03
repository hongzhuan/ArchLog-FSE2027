# Release Note

## Important Changes

### Core Library Layer
- Fix the POOL_sizeof function prototype and add const qualifier to its parameters. (Architecture-related: public API)
  ↳ [#2995](https://github.com/facebook/zstd/pull/2995): [6211bfe](https://github.com/facebook/zstd/commit/6211bfee5ec24dc825c11751c33aa31d618b5f10), [b1978d6](https://github.com/facebook/zstd/commit/b1978d60ee6de821501d7e0ce88185f6575028b0)
- Hide x86-64 internal assembly functions so that they are no longer exposed in the dynamic symbol table. (Architecture-related: public API)
  ↳ [#2993](https://github.com/facebook/zstd/pull/2993): [568c69a](https://github.com/facebook/zstd/commit/568c69a4eb0e30fb03a75176804b47ed51dd3ab1)
- Reconstruct multi-thread memory management, move the calculation of the maximum number of buffers in the buffer pool and sequence pool to the caller, introduce macros to clarify the upper limit, and update related documents. (Architecture-related: multi-thread memory management interface)
  ↳ [#3000](https://github.com/facebook/zstd/pull/3000): [9b6dfed](https://github.com/facebook/zstd/commit/9b6dfedf0c49d6554609419214f58beb6a60480b)
- In Linux kernel scenarios, replace memcpy calls with ZSTD_memcpy to ensure correct function redirection. (Architecture-related: platform compatibility)
  ↳ [#2962](https://github.com/facebook/zstd/pull/2962): [ad7c9fc](https://github.com/facebook/zstd/commit/ad7c9fc11e689e105e9c43c016c9160a121ba3b1)
- The version number has been upgraded to 1.5.2, and the version macro definition in the header file has been updated. (Architecture-related: version and compatibility)
  ↳ [#2987](https://github.com/facebook/zstd/pull/2987): [46ad937](https://github.com/facebook/zstd/commit/46ad9377e8eac2c77ee677a9af94104d996561d9)

### Application & Tool Layer
- Fixed an issue where the progress bar was incorrectly printed when using the -q option to decompress and specify an output file. (Architecture-related: CLI behavior)
  ↳ [#2982](https://github.com/facebook/zstd/pull/2982): [308a11b](https://github.com/facebook/zstd/commit/308a11b8e88f5201ddeb839269268b3824567d89)
- By inlining the xxHash header file, the dependence on the xxHash dynamic library symbol is removed, allowing the zstd binary to be dynamically linked to the library. (Architecture-related: build and installation methods)
  ↳ [#2977](https://github.com/facebook/zstd/pull/2977): [4bd96a6](https://github.com/facebook/zstd/commit/4bd96a61f103ac7ed8b52d39e99424f2f9b52643)

### Cross-cutting / Other Architecture-related Changes
- Allows you to select the optimization level of the library through command line parameters (such as CFLAGS=-O0) to speed up testing. (Architecture-related: build and installation methods)
  ↳ [#2995](https://github.com/facebook/zstd/pull/2995): [75525fc](https://github.com/facebook/zstd/commit/75525fcb9f4c7ed1bb39d10aa43ce529c950d208)
- Added noexecstack linker and assembler flags to the Makefile build system to ensure that generated binaries are marked as non-executable stack. (Architecture-related: platform compatibility)
  ↳ [#2964](https://github.com/facebook/zstd/pull/2964): [4620ce6](https://github.com/facebook/zstd/commit/4620ce6a9abe7f2aad9ae0ecd4768cd38491edb8)
- Fixed the problem of MSVC compilation failure in Meson build: conditionalize assembly source files, enable it only for GCC and Clang compilers, and explicitly disable assembly support for non-GCC/Clang compilers. (Architecture-related: build and installation mode)
  ↳ [#2951](https://github.com/facebook/zstd/pull/2951): [29e44bc](https://github.com/facebook/zstd/commit/29e44bc5547f88ab5c1942d2514c2d524100b71c) | [#2972](https://github.com/facebook/zstd/pull/2972): [c4f5116](https://github.com/facebook/zstd/commit/c4f5116e95d7aee1fb36f64ce074fc1187630398)
- Fixed the problem of MSVC compilation failure in CMake build: correctly exclude assembly source files, and add compilation options for MSVC to explicitly disable assembly. (Architecture-related: build and installation mode)
  ↳ [#2957](https://github.com/facebook/zstd/pull/2957): [148ff15](https://github.com/facebook/zstd/commit/148ff1577452e1ceb722ff4394007656112d8a41), [df5ad5a](https://github.com/facebook/zstd/commit/df5ad5a0f1e087e1202806c8b4baf72d7841edf4)
- Fixed the issue where the zstd static library output name is incorrect when using the Clang compiler in the MINGW environment. (Architecture-related: build and installation methods)
  ↳ [#2947](https://github.com/facebook/zstd/pull/2947): [14a0eaf](https://github.com/facebook/zstd/commit/14a0eaf73ba84ab8eabf9ab44b278a13cc0f0b6a)
- Fix the build system: Change the compilation of assembly files from using CFLAGS to using ASFLAGS, and add the -Wa, --noexecstack flag. (Architecture-related: build and installation methods)
  ↳ [#3009](https://github.com/facebook/zstd/pull/3009): [8ea3d57](https://github.com/facebook/zstd/commit/8ea3d57de4bcff2170296e0d1a5019f030630f3b)

## Routine Changes

### New features
- No significant changes.

### bug fixes
- Fix regression test assertions to ensure offset codes for candidate matches are calculated using the STORE_OFFSET macro only under valid conditions.
  ↳ [#2962](https://github.com/facebook/zstd/pull/2962): [435f5a2](https://github.com/facebook/zstd/commit/435f5a2e6d7aa8f0ad581c2da688f8a7f1e3e8cd)
- Fixed the out-of-bounds access problem in the optimal parser caused by the literal length exceeding the format representation range.
  ↳ [#2980](https://github.com/facebook/zstd/pull/2980): [4d8a213](https://github.com/facebook/zstd/commit/4d8a2132d0e453232a46dd448e5137035ba25bee)
- Fixed the problem of incorrectly updating timestamp when the output target is standard output.
  ↳ [#2998](https://github.com/facebook/zstd/pull/2998): [57a86d9](https://github.com/facebook/zstd/commit/57a86d9ec636c75f17a3005962ff178545e404f5)
- Fixed the issue of repeated creation and release of global compression context variables in the freshCCtx scenario in the fullbench test.
  ↳ [#2995](https://github.com/facebook/zstd/pull/2995): [213dc61](https://github.com/facebook/zstd/commit/213dc6110fda144326cc783c02f98a7886cfe4b3)

### Refactoring optimization
- Introduced STORE_OFFSET() and STORE_REPCODE() macros to abstractly represent the offset and repeat code values passed to ZSTD_storeSeq(), and update multiple call points, while the behavior remains unchanged.
  ↳ [#2962](https://github.com/facebook/zstd/pull/2962): [1aed962](https://github.com/facebook/zstd/commit/1aed962216373a6683ff6f26e4ae0ff8fa62f4e4), [2068889](https://github.com/facebook/zstd/commit/2068889146a8c41947bd57b41c639b9f5ab1b73c), [b7630a4](https://github.com/facebook/zstd/commit/b7630a474b5e330e07dc743e2a2d7cb26f457a7a), [e909fa6](https://github.com/facebook/zstd/commit/e909fa627fc9005119457bc25e59cd1a03ae76ba), [92a08ee](https://github.com/facebook/zstd/commit/92a08eec72c9bd2b28620aab3b47af5a2ae7f0c5), [a34ccad](https://github.com/facebook/zstd/commit/a34ccad9a6adbaf6bd976434b5ae18a2d60f224a), [321583c](https://github.com/facebook/zstd/commit/321583ccf508e300d68f6ea3e6fcf9adb13d2a47) | [#2954](https://github.com/facebook/zstd/pull/2954): [b77fcac](https://github.com/facebook/zstd/commit/b77fcac61fadf665f7522dd0c2e44b373eb7d57d)
- Split the repeated offset update function into updateRep() that updates in place and newRep() that returns a new structure to clarify the two behaviors.
  ↳ [#2962](https://github.com/facebook/zstd/pull/2962): [6fa640e](https://github.com/facebook/zstd/commit/6fa640ef70d01489e2a4a6228f4e439b712f7d68)
- Optimize the expression in the initialization phase of the compression state.
  ↳ [#2969](https://github.com/facebook/zstd/pull/2969): [41ad733](https://github.com/facebook/zstd/commit/41ad7332dd59ed9081cee345bd95e080cb96b199)
- Remove unused header file references and clean up code dependencies.
  ↳ [#2977](https://github.com/facebook/zstd/pull/2977): [fc946d1](https://github.com/facebook/zstd/commit/fc946d131b3a028c23d2ae84ade6b6114aa6fec2)

### Test related
- In decodecorpus.c, abstract the numerical judgment of sumtype in ZSTD_storeSeq into the macro STORED_IS_REPCODE
  ↳ [#2962](https://github.com/facebook/zstd/pull/2962): [681c81f](https://github.com/facebook/zstd/commit/681c81f06c313eed276283c141d0c14e9404b4fa)
- Added compress_freshCCtx test scenario in fullbench
  ↳ [#2995](https://github.com/facebook/zstd/pull/2995): [a0b9520](https://github.com/facebook/zstd/commit/a0b9520e38c459408330bfdfb62f666f331d3bed)

### Performance optimization
- Fixed the performance regression caused by the failure of workspace initialization optimization when reusing the compression state, restoring the compression performance of small data flow scenarios to the v1.4.9 level.
  ↳ [#2969](https://github.com/facebook/zstd/pull/2969): [8c53e52](https://github.com/facebook/zstd/commit/8c53e526db3bcf5a95f67bd347e1f89c79f4fe94)

### Security related
- No significant changes.

### Documentation
- Updated CHANGELOG, supplemented the release notes of v1.5.2 version.
  ↳ [#2987](https://github.com/facebook/zstd/pull/2987): [144879a](https://github.com/facebook/zstd/commit/144879a7cd1b7ac40cf46178f3951a0a97df3c63)
- Updated continuous integration documentation in the contribution guide, moved the CI process to GitHub Actions, and removed outdated third-party CI setup instructions.
  ↳ [#2999](https://github.com/facebook/zstd/pull/2999): [8250faa](https://github.com/facebook/zstd/commit/8250faa01bf0a3b46b3204bdefee7ae04ab12f80)

### Build/CI
- Clean up debug output statements in build scripts.
  ↳ [#2964](https://github.com/facebook/zstd/pull/2964): [ff5d1da](https://github.com/facebook/zstd/commit/ff5d1daf33abe71f95f2c90de877ac98cf01af83)

### Maintenance
- No significant changes.

### Others
- Fixed typo in compressFile_orDie function comment.
  ↳ [#2960](https://github.com/facebook/zstd/pull/2960): [7ee35ba](https://github.com/facebook/zstd/commit/7ee35bad6b9e20c8f01e96c5e106cab7bd4d45ec)
