# Release Note

## Important Changes

### Core Library Layer

- Core library changes: `change ZSTD_storeSeq() interface to accept matchLength`. [commit](https://github.com/facebook/zstd/commit/b77fcac61fadf665f7522dd0c2e44b373eb7d57d)
- Core library changes: `x86-64: Hide internal assembly functions`. [commit](https://github.com/facebook/zstd/commit/568c69a4eb0e30fb03a75176804b47ed51dd3ab1)

### Application & Tool Layer

- Tools and platform integration: `Improve Module Map File`. [commit](https://github.com/facebook/zstd/commit/8dd943e42c13ca33d07ead274e07defd1e2114c5)
- Tools and platform integration: `Update the Swift Package Definition to Reflect Move`. [commit](https://github.com/facebook/zstd/commit/17782224460107dcbc29141db9a9b1209746fd27)

### Cross-cutting / Other Architecture-related Changes

- Cross-module security hardening: `Mark Huffman Decoder Assembly `noexecstack` on All Architectures`. [commit](https://github.com/facebook/zstd/commit/9a9d1ec6f4536ffeb745f360ef010cefd125bfd0)
- Cross-module security hardening: `Makefiles: Add `noexecstack` Options to Compilation and Linking`. [commit](https://github.com/facebook/zstd/commit/4620ce6a9abe7f2aad9ae0ecd4768cd38491edb8)
- Cross-module security hardening: `Write `GNU-stack` Section on All ELF Architectures`. [commit](https://github.com/facebook/zstd/commit/b12edddb3784c59c459a40f6108027b0bcedaf2f)
- Cross-module security hardening: `Restrict `GNU-stack` Note to GNU Assemblers`. [commit](https://github.com/facebook/zstd/commit/ef1f9e80ffc62c5de06375bc62012373a5d0b77f)

## Routine Changelog

### Bug Fixes

- Fix: `Fix zstd-static output name with MINGW/Clang`. [commit](https://github.com/facebook/zstd/commit/14a0eaf73ba84ab8eabf9ab44b278a13cc0f0b6a)
- Fix: `Fix tar test cases`. [commit](https://github.com/facebook/zstd/commit/666372c7bf345ef8a238ca1ffbe985ba4a9aedf6)
- Fix: `Fixup MSVC source file inclusion for cmake builds`. [commit](https://github.com/facebook/zstd/commit/148ff1577452e1ceb722ff4394007656112d8a41)
- Fix: `Fix mini typo`. [commit](https://github.com/facebook/zstd/commit/7ee35bad6b9e20c8f01e96c5e106cab7bd4d45ec)
- Fix: `fixed regression test assert`. [commit](https://github.com/facebook/zstd/commit/435f5a2e6d7aa8f0ad581c2da688f8a7f1e3e8cd)
- Fix: `fixed minor typecast warnings`. [commit](https://github.com/facebook/zstd/commit/321583ccf508e300d68f6ea3e6fcf9adb13d2a47)
- Fix: `fixed minor conversion warnings`. [commit](https://github.com/facebook/zstd/commit/a34ccad9a6adbaf6bd976434b5ae18a2d60f224a)
- Fix: `fixed backup prototype for POOL_sizeof()`. [commit](https://github.com/facebook/zstd/commit/6211bfee5ec24dc825c11751c33aa31d618b5f10)
- Fix: `Fix stderr progress logging for decompression`. [commit](https://github.com/facebook/zstd/commit/308a11b8e88f5201ddeb839269268b3824567d89)
- Fix: `Avoid updating timestamps when the destination is stdout`. [commit](https://github.com/facebook/zstd/commit/57a86d9ec636c75f17a3005962ff178545e404f5)

### Refactoring

- Refactor or adjust: `changed seqDef.matchLength into seqDef.mlBase`. [commit](https://github.com/facebook/zstd/commit/e145b58cfdf94a300295be022d4b41d6ca70d8f1)
- Refactor or adjust: `change seqDef.offset into seqDef.offBase`. [commit](https://github.com/facebook/zstd/commit/aeff1283311b6be38c5efc24c019e0f72ce60046)
- Refactor or adjust: `created STORED_*() macros`. [commit](https://github.com/facebook/zstd/commit/2068889146a8c41947bd57b41c639b9f5ab1b73c)
- Refactor or adjust: `abstracted usage of offBase sumtype within zstd_lazy.c`. [commit](https://github.com/facebook/zstd/commit/b7630a474b5e330e07dc743e2a2d7cb26f457a7a)
- Refactor or adjust: `separate newRep() from updateRep()`. [commit](https://github.com/facebook/zstd/commit/6fa640ef70d01489e2a4a6228f4e439b712f7d68)
- Refactor or adjust: `abstracted storeSeq() sumtype numeric representation from decodecorpus.c`. [commit](https://github.com/facebook/zstd/commit/681c81f06c313eed276283c141d0c14e9404b4fa)
- Refactor or adjust: `abstracted storeSeq() sumtype numeric representation from zstd_opt.c`. [commit](https://github.com/facebook/zstd/commit/e909fa627fc9005119457bc25e59cd1a03ae76ba)
- Refactor or adjust: `abstracted storeSeq() sumtype numeric representation from zstd_lazy.c`. [commit](https://github.com/facebook/zstd/commit/92a08eec72c9bd2b28620aab3b47af5a2ae7f0c5)
- Refactor or adjust: `regroup all mentions of ZSTD_REP_MOVE within zstd_compress_internal.h`. [commit](https://github.com/facebook/zstd/commit/de9f52e9456f97a3bdf6c2b4ecad424226d65247)
- Refactor or adjust: `found a few more places which were dependent on seqStore offcode sumtype numeric representation`. [commit](https://github.com/facebook/zstd/commit/8da414231d105e64d424f6661a21e3add8c40fd1)
- Refactor or adjust: `POOL_sizeof() only needs a const read-only reference`. [commit](https://github.com/facebook/zstd/commit/b1978d60ee6de821501d7e0ce88185f6575028b0)
- Refactor or adjust: `Updated expression for better readability`. [commit](https://github.com/facebook/zstd/commit/41ad7332dd59ed9081cee345bd95e080cb96b199)
- Refactor or adjust: `Avoid xxHash Dependency by Inlining`. [commit](https://github.com/facebook/zstd/commit/4bd96a61f103ac7ed8b52d39e99424f2f9b52643)

### Tests

- Test updates: `fixed fullbench freshCCtx scenario`. [commit](https://github.com/facebook/zstd/commit/213dc6110fda144326cc783c02f98a7886cfe4b3)
- Test updates: `Add Test Validating Stack is not Executable in playTests.sh`. [commit](https://github.com/facebook/zstd/commit/35208f702f0a5e4ebe70d651efd75770f176b2d0)

### Performance

- Performance optimization: `fix performance issue in scenario #2966 (part 1)`. [commit](https://github.com/facebook/zstd/commit/8c53e526db3bcf5a95f67bd347e1f89c79f4fe94)
- Test updates: `fullbench: added compress_freshCCtx scenario`. [commit](https://github.com/facebook/zstd/commit/a0b9520e38c459408330bfdfb62f666f331d3bed)

### Documentation

- Documentation updates: `updated manual`. [commit](https://github.com/facebook/zstd/commit/41153071a002296c65c20958e9fb921a8f82edf0)
- Documentation updates: `Update Docs`. [commit](https://github.com/facebook/zstd/commit/e1323744b6998ac237c25904331c6d820bf02aa4)
- Documentation updates: `Documentation and minor refactor to clarify MT memory management.`. [commit](https://github.com/facebook/zstd/commit/9b6dfedf0c49d6554609419214f58beb6a60480b)
- Documentation updates: `Update CI documentation`. [commit](https://github.com/facebook/zstd/commit/8250faa01bf0a3b46b3204bdefee7ae04ab12f80)

### Build / CI

- Build / CI updates: `meson: fix MSVC support`. [commit](https://github.com/facebook/zstd/commit/29e44bc5547f88ab5c1942d2514c2d524100b71c)
- Build / CI updates: `library optimization flag can be selected on command line again`. [commit](https://github.com/facebook/zstd/commit/75525fcb9f4c7ed1bb39d10aa43ce529c950d208)
- Build / CI updates: `[meson] Explicitly disable assembly for non clang/gcc copmilers`. [commit](https://github.com/facebook/zstd/commit/c4f5116e95d7aee1fb36f64ce074fc1187630398)
- Build / CI updates: `Add a compile option to explicitely disable assembly`. [commit](https://github.com/facebook/zstd/commit/df5ad5a0f1e087e1202806c8b4baf72d7841edf4)
- Build / CI updates: `[build][asm] Pass ASFLAGS to the assembler instead of CFLAGS`. [commit](https://github.com/facebook/zstd/commit/8ea3d57de4bcff2170296e0d1a5019f030630f3b)

### Maintenance

- Maintenance Updates: `Clean Up Debugging Statements`. [commit](https://github.com/facebook/zstd/commit/ff5d1daf33abe71f95f2c90de877ac98cf01af83)
- Maintenance Updates: `Remove Unused Include`. [commit](https://github.com/facebook/zstd/commit/fc946d131b3a028c23d2ae84ade6b6114aa6fec2)
- Maintenance Updates: `[license] Fix license header of huf_decompress_amd64.S`. [commit](https://github.com/facebook/zstd/commit/c7b03c217c2542152a08e4ca343f8a27d3680901)
- Maintenance Updates: `Bump Version Number to 1.5.2`. [commit](https://github.com/facebook/zstd/commit/46ad9377e8eac2c77ee677a9af94104d996561d9)

### Others

- Updates: `introduce macros STORE_OFFSET() and STORE_REPCODE()`. [commit](https://github.com/facebook/zstd/commit/1aed962216373a6683ff6f26e4ae0ff8fa62f4e4)
- Updates: `use ZSTD_memcpy(), for proper redirection within Linux Kernel`. [commit](https://github.com/facebook/zstd/commit/ad7c9fc11e689e105e9c43c016c9160a121ba3b1)
- Updates: `[opt] Fix oss-fuzz bug in optimal parser`. [commit](https://github.com/facebook/zstd/commit/4d8a2132d0e453232a46dd448e5137035ba25bee)
