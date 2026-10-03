# Release Note

## Important Changes

### Cross-cutting / Other Architecture-related Changes
- Introduced the Staged-Ordered-Ring (SORING) software abstraction, supports ordered queues and multi-processing stages, and provides enqueue/dequeue and acquire/release data path APIs. (Architecture-related: public API)
  ↳ No PR: [b5458e2](https://github.com/DPDK/dpdk/commit/b5458e2cc48349b314c7354e4ddfd2100bd55c29)
- Moved the support check for deferred start (deferred start) from each driver to the ethdev layer, and removed the redundant check code in the driver. (Architecture-related: Delayed start check moved to the ethdev layer)
  ↳ No PR: [f73dd2a](https://github.com/DPDK/dpdk/commit/f73dd2aa1e16e8994d089593dd3f48cfa9915ea0)
- Removed the weak symbols in the Nitrox driver, and instead managed compression and encryption drivers through a unified driver registration mechanism. (Architecture-related: Unified driver registration mechanism)
  ↳ No PR: [8c1e722](https://github.com/DPDK/dpdk/commit/8c1e722908a15bc5916734f8d97cd69e0fa2abff)
- Reconstructed the virtio encryption device queue operation, extracted the control queue related logic to the common module, and added support for packed virtqueue. (Architecture-related: virtio encryption device queue reconstruction)
  ↳ No PR: [d49a5a7](https://github.com/DPDK/dpdk/commit/d49a5a76d0cdbbcdc24c466a6da8d411ba4ccf94)
- Migrate the CPT context macro definition from the dedicated header file to the common header file, making it common to all modules using CPT CTX. (Architecture-related: public API)
  ↳ No PR: [a19ceac](https://github.com/DPDK/dpdk/commit/a19ceac6b20cb905bd3cabc62ed7698107ffd120)
- Migrate interrupt handling logic from general code to platform-specific implementation to improve code clarity and maintainability. (Architecture-related: platform compatibility)
  ↳ No PR: [375cb16](https://github.com/DPDK/dpdk/commit/375cb16018824e75a1b20e90c7f142e5bc8d5750)
- Introduce __rte_packed_begin and __rte_packed_end macros, and abandon the old __rte_packed macro to achieve cross-compiler structure packaging compatibility. (Architecture-related: public API)
  ↳ No PR: [fac4bc0](https://github.com/DPDK/dpdk/commit/fac4bc0d06c98e15788f47da4e08a8cfb2ba942b), [154303b](https://github.com/DPDK/dpdk/commit/154303b06ab29e040000f0536961601d952e2974), [ae2e4c4](https://github.com/DPDK/dpdk/commit/ae2e4c4885c8a185beaf209d7b7c122700cc966f), [a2bed5d](https://github.com/DPDK/dpdk/commit/a2bed5d09dae16f4137d0e0c95e992cccad7c5db), [37e3339](https://github.com/DPDK/dpdk/commit/37e33391ee75767310b5ac388278082104caefe7), [5dc68f2](https://github.com/DPDK/dpdk/commit/5dc68f2be8adea7aad24dc56dad57ec9a3bfe413), [b5662e6](https://github.com/DPDK/dpdk/commit/b5662e6d288762fe2c538551eb03d68854896e0b)
- Add MSVC compiler support for x86 EAL's write merge stored functions. (Architecture-related: Platform compatibility)
  ↳ No PR: [feb9fd6](https://github.com/DPDK/dpdk/commit/feb9fd6a9f019b20b1c60ed664b4887592f78032)
- Added rte_ffs32 and rte_ffs64 experimental APIs, used to find the first set bit starting from the least significant bit. (Architecture-related: public API)
  ↳ No PR: [21cab84](https://github.com/DPDK/dpdk/commit/21cab84f6f8c946fabf72fdb03ce4b274887b950)
- Add an API to dynamically enable or disable xstat counters for ethdev, and add an interface to query the counter status. (Architecture-related: public API)
  ↳ No PR: [9854659](https://github.com/DPDK/dpdk/commit/985465997b73a09b325cf78a5dd1ed47ed0ed3e8)
- Enhanced assertion checks when releasing mbufs, and added APIs for batch allocation and release of mbufs. (Architecture-related: public API)
  ↳ No PR: [5562417](https://github.com/DPDK/dpdk/commit/55624173bacb2becaa67793b71391884876673c1)
- Support dereferencing pointers directly in trace points, and updated dmadev's trace points to use the new mechanism. (Architecture-related: trace API extension)
  ↳ No PR: [8fc882c](https://github.com/DPDK/dpdk/commit/8fc882c01fe993c8e918cd6b40d5ea6baaa1b6ea), [223eff9](https://github.com/DPDK/dpdk/commit/223eff9aab86ab225b846982f7aa3d3dffd97841)
- Added rte_event_eth_rx_adapter_queues_add API, which supports adding Rx queues in batches and specifying their respective configurations; the Rx adapter of the cnxk event device PMD also adds support for adding queues in batches. (Architecture-related: public API)
  ↳ No PR: [7e278cb](https://github.com/DPDK/dpdk/commit/7e278cb4bcc6717bebe3cb65ef9310c1483fa03b), [17e0587](https://github.com/DPDK/dpdk/commit/17e05874e8a3264ad6d65138c54317b39f0448b4)
- Add IPsec and CPT support to the CN20K platform, including device enumeration, SA initialization, session management, parsing header structures, inline SA synchronization and feature flag updates. (Architecture-related: platform compatibility)
  ↳ No PR: [7301b3e](https://github.com/DPDK/dpdk/commit/7301b3ef52380e763be29bf96310072c0031057c), [7b2b75a](https://github.com/DPDK/dpdk/commit/7b2b75accfa3e8451608269362362653f14196ad), [24d1064](https://github.com/DPDK/dpdk/commit/24d10645bdfb44c1fb9f9e825515dc10de7e0ead), [4ed9434](https://github.com/DPDK/dpdk/commit/4ed9434c8588a0150879e4febb06d8ffd3951260), [0d9e323](https://github.com/DPDK/dpdk/commit/0d9e323bacf0ee8b5b0b8dff69a68e40ace2c5b8), [f81ee71](https://github.com/DPDK/dpdk/commit/f81ee7133b489076098da44007f3a7cb1207755a), [814d45f](https://github.com/DPDK/dpdk/commit/814d45f844edd7b5ddf9c03de1644a0b5d581954), [0d31823](https://github.com/DPDK/dpdk/commit/0d31823d36ef1f4c8efc0644db3bca28da958b14), [3683198](https://github.com/DPDK/dpdk/commit/3683198ecba6c62f4ebbb3155ec473490fbbd6d6), [d18f21d](https://github.com/DPDK/dpdk/commit/d18f21df6e2db344871972a4e9e0330812c34546)
- Added performance test support for the RSA asymmetric encryption algorithm in the crypto-perf application; added support for asymmetric RSA operations (signature, verification, encryption and decryption) in vhost-user and virtio encryption PMD, and restructured session management to support both symmetric and asymmetric operation types; and added relevant test cases for CNXK PMD and Virtio PMD. (Architecture-related: public API)
  ↳ No PR: [44975cb](https://github.com/DPDK/dpdk/commit/44975cb7b5f30301d9ce216372ea1bef6bc9082e), [d1b484b](https://github.com/DPDK/dpdk/commit/d1b484bf1876d4e072e4e9aa391e7c88e18e95d9), [1070213](https://github.com/DPDK/dpdk/commit/10702138f1a1a0efbc00ec5dbb6235ebaa92fb88), [dc4ce7c](https://github.com/DPDK/dpdk/commit/dc4ce7c2538b713e16887eb598da309bc7b4d528), [99cc389](https://github.com/DPDK/dpdk/commit/99cc389af4e16011c821cabb867e6646357f429d), [9682e82](https://github.com/DPDK/dpdk/commit/9682e8246ae29fec9f072674cd7d13aff043ffdd), [7e2e9d5](https://github.com/DPDK/dpdk/commit/7e2e9d5f3227d0c813659ff7b1d159192a222c47), [a8f3d4f](https://github.com/DPDK/dpdk/commit/a8f3d4f5b5474388133275a0527450b60470b354)
- Added atomic 128-bit comparison and exchange support for the MSVC compiler, enabling the stack library to be built in the MSVC environment. (Architecture-related: platform compatibility)
  ↳ No PR: [9c2fde3](https://github.com/DPDK/dpdk/commit/9c2fde3bc2b1b00cfe5385296b6526e9ab07865f)
- Fix the double release problem during log cleaning: add internal file mark, only close log files allocated by DPDK, avoid executing fclose on files passed in by users (architecture-related: log file ownership)
  ↳ No PR: [ba9fb27](https://github.com/DPDK/dpdk/commit/ba9fb2795b9f751836c0949c0c531da7af52a4f2)
- Fixed the memory order problem of atomic loading in batch allocation waiting in the cnxk driver, and changed the memory order from relaxed to acquisition to avoid potential out-of-order loading problems. (Architecture-related: public API)
  ↳ No PR: [73d3868](https://github.com/DPDK/dpdk/commit/73d38682fddd614d95942442c20b3a1de211bb4c)
- Changed variadic macros in driver code from GCC extended syntax to standard C99 form to fix MSVC compilation errors. (Architecture-related: Platform compatibility)
  ↳ No PR: [fd51012](https://github.com/DPDK/dpdk/commit/fd51012de5369679e807be1d6a81d63ef15015ce)
- Fixed an error caused by type conversion when compiling MSVC. Use intrinsic function to access __m128i content instead, ensuring compatibility with GCC, Clang and MSVC under 64-bit architecture. (Architecture-related: platform compatibility)
  ↳ No PR: [3a70b20](https://github.com/DPDK/dpdk/commit/3a70b20a7b79004777a515cef318fd0eb3f2d9e2), [a2c4e7f](https://github.com/DPDK/dpdk/commit/a2c4e7f67d57120e19f698af73495c36c24ad4e2)
- Fix the timing of logging and parameter checking in the rte_vhost_driver_set_max_queue_num function to ensure that it is only executed on the VDUSE backend to avoid misleading Vhost-user devices. (Architecture-related: public API)
  ↳ No PR: [2742921](https://github.com/DPDK/dpdk/commit/274292190d1384b028552adc601dda4b197f2417)
- Fixed Windows compilation errors and removed the AVX conditional judgment in the immintrin.h header file. (Architecture-related: platform compatibility)
  ↳ No PR: [5b85620](https://github.com/DPDK/dpdk/commit/5b856206c74bbcf19e12cafa15382a7e15b0a1b5)
- Fixed the issue where vhost device returns wrong packet count when calling rte_vhost_dequeue_burst when virtqueue is not ready. (Architecture-related: public API)
  ↳ No PR: [8b96508](https://github.com/DPDK/dpdk/commit/8b96508af6021d868052545a76ef2ce5219b7702)
- Fixed the problem that rte_eth_dev_socket_id() and rte_eth_dev_owner_get() functions are not available during the device detection phase, and relaxed the port validity check. (Architecture-related: public API)
  ↳ No PR: [0b8f353](https://github.com/DPDK/dpdk/commit/0b8f35358ceb0178878f72b66a36dc0ab7924377)
- Fixed the problem of rte_mempool_create_empty not setting rte_errno correctly when creating an empty memory pool failed. (Architecture-related: public API)
  ↳ No PR: [a81d8ce](https://github.com/DPDK/dpdk/commit/a81d8ceff4e961995c78df6dbc9353dbbfbd8c32)
- Support the use of arbitrary expressions in trace blob length, avoid side effects through internal intermediate variables, and update ethdev trace points to remove unnecessary intermediate variables. (Architecture-related: public API)
  ↳ No PR: [a92cdcf](https://github.com/DPDK/dpdk/commit/a92cdcf1dd065b8dd3f4c0848f7278fd00103158)
- Added allocation and release annotations to the hash table creation function to assist in detecting memory leaks. (Architecture-related: public API)
  ↳ No PR: [3f3b4c3](https://github.com/DPDK/dpdk/commit/3f3b4c3b4055512a83afe777afef19dde02f481b)
- Added __rte_malloc and __rte_dealloc attribute annotations to the allocation function of bitrate statistics to help detect the problem of improper release of memory after allocation. (Architecture-related: public API)
  ↳ No PR: [fa96a4a](https://github.com/DPDK/dpdk/commit/fa96a4ac7a460b4e24d9cee62831607244b9b244)
- Fixed the undefined behavior when registering tracepoints by adding an inline _register() handler for each tracepoint and adjusting the macro definition, and also removed the relevant workaround code in dmadev tracepoints. (Architecture-related: public API)
  ↳ No PR: [856aef5](https://github.com/DPDK/dpdk/commit/856aef55de953957e4fd837750092a85734ffb18)
- Delayed the initialization of the random number generator from the constructor to the EAL initialization phase, explicitly called eal_rand_init() in rte_eal_init(), and added assertions to ensure initialization order. (Architecture-related: EAL initialization order)
  ↳ No PR: [6b77657](https://github.com/DPDK/dpdk/commit/6b77657ef2e473309a3435cdf63b0f0cbb8328af)
- Updated the default encryption engine group for the CN20K platform (the platform does not support the IE engine), and retained the legacy engine group for CN10K and earlier versions. (Architecture-related: platform compatibility)
  ↳ No PR: [9213b28](https://github.com/DPDK/dpdk/commit/9213b284d6b356804348c0e649f93e12230795c7)
- Fixed an issue where NUMA nodes were not detected when the number of cores for a single socket exceeds RTE_MAX_LCORE, by expanding the core to socket mapping array and traversing all possible lcore IDs to record all NUMA nodes. (Architecture-related: NUMA node detection)
  ↳ No PR: [ef41b96](https://github.com/DPDK/dpdk/commit/ef41b96461703c766e4a39ecf4bf7cb731d9617d)
- Add attribute annotations to the allocation function of the ring library to help detect memory leaks. (Architecture-related: public API)
  ↳ No PR: [70005ea](https://github.com/DPDK/dpdk/commit/70005ea51c0dc800c75f26ed4bcd09f48c76213f)
- Improved the rte_ring_dump function to provide independent head/tail dump logic for each synchronization type to correctly output the head/tail values and additional metadata in different synchronization modes. (Architecture-related: public API)
  ↳ No PR: [700989f](https://github.com/DPDK/dpdk/commit/700989f512bbc2ee9758a8a9cb6973cfdeda6f27)
- Replace the structure packing macros with __rte_packed_begin and __rte_packed_end to solve the compatibility issue between MSVC and GCC. (Architecture-related: platform compatibility)
  ↳ No PR: [e775063](https://github.com/DPDK/dpdk/commit/e77506397fc8005c5129e22e9e2d15d5876790fd), [7f2a987](https://github.com/DPDK/dpdk/commit/7f2a987ca852a45bdb4520edc7ad7e02c4efd269), [fba9875](https://github.com/DPDK/dpdk/commit/fba9875559906e04eaeb74532f4cfd51194259a2)
- Added diagnostic control macros and pointer type conversion macros to the public header file, and added MSVC inline prompt macro support. (Architecture-related: public API)
  ↳ No PR: [a1b873f](https://github.com/DPDK/dpdk/commit/a1b873f1de53d202ccd905d3b5ff3e561a5381ce), [4b4ed9c](https://github.com/DPDK/dpdk/commit/4b4ed9cc7d213d4be620ab12b4a329ee5dfb8d67)
- Updated the session parameter structure of vhost/crypto to be compatible with QEMU v9, replacing VhostUserCryptoSessionParam with VhostUserCryptoSymSessionParam. (Architecture-related: public API)
  ↳ No PR: [b1d0271](https://github.com/DPDK/dpdk/commit/b1d02713d35af10218a8e0333b99ef821e4a669f)
- Removed variable-length arrays in Linux EAL interrupt handling and used alloca() or fixed-size arrays instead to be compatible with MSVC. (Architecture-related: platform compatibility)
  ↳ No PR: [36a4ba4](https://github.com/DPDK/dpdk/commit/36a4ba4c02f28e135f234ffe96610114b6c6e8f7)
- Clarified the semantics of the RTE_ETH_EVENT_NEW event: the port is being probed but is not yet available, and the validity should not be checked, information queried or the port configured at this time. (Architecture-related: public API)
  ↳ No PR: [c6c0dfb](https://github.com/DPDK/dpdk/commit/c6c0dfb271008ef5c7bc544f4efde26f99d50a3e)
- Added unified FDB domain restrictions in the mlx5 driver documentation: template tables with wire_orig or vport_orig flags cannot be created on group 0, and the FDB_TX domain does not support rte_flow_action_mark ID. (Architecture-related: external behavior)
  ↳ No PR: [8d82693](https://github.com/DPDK/dpdk/commit/8d82693eb70e55924e3a5c9b75adcd6f54c6606b)
- Announced that the vmbus API will become an internal API in DPDK 25.11 version, and added a corresponding deprecation notice. (Architecture-related: public API)
  ↳ No PR: [7642e3b](https://github.com/DPDK/dpdk/commit/7642e3b0e04d8d38d363842e34e83aef8269af2a)
- Added a list of tested Intel platform and Intel network card combinations in the 25.03 release notes. (Architecture-related: Platform compatibility)
  ↳ No PR: [03e6bb3](https://github.com/DPDK/dpdk/commit/03e6bb39b1438e296f04541b115ca21580767265), [2ac64b2](https://github.com/DPDK/dpdk/commit/2ac64b2c4331acc9e84e206858bc32e5590baaa1), [d4831cc](https://github.com/DPDK/dpdk/commit/d4831cc5c68218b7f725218a9692cb050a82055e)
- Updated supported bbdev operation range in bbdev guide to explicitly include FEC functions, FFT and MLD-TS. (Architecture-related: public API)
  ↳ No PR: [8a77984](https://github.com/DPDK/dpdk/commit/8a77984785a650db9af28fc5fa5cc0534ed8b91e)
- Fixed a build error caused by including x86intrin.h under MSVC. This header file is only included in non-MSVC environments. (Architecture-related: platform compatibility)
  ↳ No PR: [af1a794](https://github.com/DPDK/dpdk/commit/af1a794cead9198ae674986e37c9ddf9d7a3fc89)
- Fixed AVX512 compilation error caused by __rte_aligned not supporting sizeof expression under MSVC, changed RTE_X86_ZMM_SIZE to a constant value and added static assertion to ensure correctness. (Architecture-related: platform compatibility)
  ↳ No PR: [489aa1e](https://github.com/DPDK/dpdk/commit/489aa1e798ee8017ad5057561c8a594c9847dbd0)
- Started a new 25.03 release cycle, updated the version number and ABI minor version, upgraded libabigail from 2.4 to 2.6 and enabled ABI checking, and added a new libxxhash dependency. (Architecture-related: version and compatibility)
  ↳ No PR: [7df61db](https://github.com/DPDK/dpdk/commit/7df61db6c387703a36306c1aea92225921e2eeb2)
- The Arm build system changed to give priority to -mcpu, and introduced pseudo-CPU names and corresponding march and march_extensions definitions for SoCs that do not correspond to -mcpu. At the same time, the silent downgrade behavior was removed. If the compiler does not support the specified configuration, an error will be reported. (Architecture-related: build and installation methods)
  ↳ No PR: [c02c01d](https://github.com/DPDK/dpdk/commit/c02c01dbf90781beaeeed83b557f37a61282c1ff)
- Allows disabling AVX512 instruction set support through the compiler flag -mno-avx512f. The build system will give priority to checking the user-specified c_args parameter when detecting AVX512 capabilities. (Architecture-related: build and installation methods)
  ↳ No PR: [6f8c03d](https://github.com/DPDK/dpdk/commit/6f8c03d57dae9cbde4e5283409e035490e2d8862)
- Added -fzero-init-padding-bits=all compilation option to the build configuration, forcing GCC 15 to initialize the padding bits of structures/unions to zero to fix potential problems caused by changes in the default behavior of the compiler. (Architecture-related: build and installation methods)
  ↳ No PR: [3c015da](https://github.com/DPDK/dpdk/commit/3c015da37afecbeaa7c9ebf8cf2adcb20ab0e54d)
- Added header file inclusion required for alloca() function to EAL header files for FreeBSD, Linux and Windows platforms. (Architecture-related: public API)
  ↳ No PR: [f0aef8d](https://github.com/DPDK/dpdk/commit/f0aef8dc28160fcad4f04d0fbd49bd021e9bc8a6)
- Globally enable the -Wvla compilation warning, define the no_wvla_cflag variable to temporarily disable the warning for submodules that have not eliminated variable-length arrays, and add a compilation flag to disable VLA warnings for nfb, mvpp2, mvsam drivers. (Architecture-related: build and installation methods)
  ↳ No PR: [1bf8680](https://github.com/DPDK/dpdk/commit/1bf86800f7daf8d5c71a08a0776ff3b754ee6570), [3553897](https://github.com/DPDK/dpdk/commit/3553897d84d8b54a1b1136cbf04dd7f1a40fd85b)
- Remove support for the Intel C++ compiler (icc), switch to the clang-based Intel oneAPI DPC++/C++ compiler (icx), and clean up related code comments and build configurations. (Architecture-related: build and installation methods)
  ↳ No PR: [d35cb54](https://github.com/DPDK/dpdk/commit/d35cb54e68511eba0e36a0ccab9350ea27ba7771)
- Added build target using MSVC compiler on Windows 2022 in GitHub Actions. (Architecture-related: Platform compatibility)
  ↳ No PR: [6d80989](https://github.com/DPDK/dpdk/commit/6d80989ab2dcae3d70c0deeccf104c00b49d029c)
- Add support for Phytium TengYun S5000c processor in ARM build configuration. (Architecture-related: Platform compatibility)
  ↳ No PR: [fab31a0](https://github.com/DPDK/dpdk/commit/fab31a03ba98e7457284df95dd9eef2223a4ccaa)
- Fix ARM configuration for NVIDIA BlueField-3, add missing mcpu and flags definitions to resolve build errors. (Architecture-related: Platform compatibility)
  ↳ No PR: [068d88e](https://github.com/DPDK/dpdk/commit/068d88e7bf8f06cb22de1bae12528d81527c2053)
- Add AVX2 build flags to the MSVC compiler, define the cc_avx2_flags variable in the top-level meson.build, and replace the hardcoded -mavx2 option in builds of multiple drivers and ACL libraries. (Architecture-related: Platform compatibility)
  ↳ No PR: [7548123](https://github.com/DPDK/dpdk/commit/754812303749e37168262e48e839ada645426742)
- Separate the common flags from the AVX512 flags in the x86 build configuration, and bring the common configuration code forward to prepare for the subsequent addition of MSVC specific support. (Architecture-related: platform compatibility)
  ↳ No PR: [c597a01](https://github.com/DPDK/dpdk/commit/c597a01a651f079609ea6a5fdbbbec60e6816809)
- Allow dmadev library to be compiled under MSVC compiler. (Architecture-related: platform compatibility)
  ↳ No PR: [7fa30bc](https://github.com/DPDK/dpdk/commit/7fa30bca91de033016b9b1b34dbda20ce347a298)
- Fixed an issue where extra -march features for SoCs in ARM build configurations were not correctly added to the -mcpu flag. (Architecture-related: Platform compatibility)
  ↳ No PR: [7829776](https://github.com/DPDK/dpdk/commit/7829776d0abf10315791957febbea6f24d2c723e)
- Migrate the thread safety annotations of spinlock and its derived seqlock from the old lock function macros to clang capability annotations. (Architecture-related: public API annotation migration)
  ↳ No PR: [f5c59ca](https://github.com/DPDK/dpdk/commit/f5c59cae51f1ec9e9f71118ddf9d079cd3a13cd9)
- Convert the lock annotations of read-write locks into clang capability annotations. (Architecture-related: public API annotation migration)
  ↳ No PR: [f82cbad](https://github.com/DPDK/dpdk/commit/f82cbad33fc046a9adbac3af6b31918e5f0591f1)
- Remove variable length arrays in testpmd, idpf driver, mlx5 public library and net/mlx5 driver, use standard arrays or alloca() instead, to support MSVC compiler. (Architecture-related: platform compatibility)
  ↳ No PR: [fea9c01](https://github.com/DPDK/dpdk/commit/fea9c011bc25a7428131691c26df9539299c2665), [ea78e65](https://github.com/DPDK/dpdk/commit/ea78e65cec637aa2f434a895bdba2175a53a36dd), [0e7f672](https://github.com/DPDK/dpdk/commit/0e7f672bab8296e0d29b1d0534f038d892224e7e), [c8626e5](https://github.com/DPDK/dpdk/commit/c8626e51ebe04443f436a26f5f5e2ab15bb46d13)
- Replace the GCC diagnostic ignore pragmas scattered in various drivers with unified macros to simplify MSVC compatibility maintenance. (Architecture-related: platform compatibility)
  ↳ No PR: [43fd362](https://github.com/DPDK/dpdk/commit/43fd3624fdfe3a33904a9b64d94306dd3d4f2c13)
- Added __SIZEOF_LONG__ and __SIZEOF_LONG_LONG__ macro definitions for MSVC compiler. (Architecture-related: platform compatibility)
  ↳ No PR: [a8fea3f](https://github.com/DPDK/dpdk/commit/a8fea3ffd6cdca6d414908c2fa5527e8b7f7dd96)
- Remove the packed attribute of IPv6 multicast scope enumeration and adjust the storage size. (Architecture-related: public API)
  ↳ No PR: [3cd0547](https://github.com/DPDK/dpdk/commit/3cd0547a54bd20cf8840721d4fbfe5641b3843ca)

### Input Poll-Mode Drivers (PMD)
- Added xsc network card driver, supporting PCI detection, device initialization, RSS configuration and MAC address management. (Architecture-related: new network card driver)
  ↳ No PR: [3df82f2](https://github.com/DPDK/dpdk/commit/3df82f2592897e3b7e5729fe0bff8f17de0ca35d)
- The igc driver has been removed, and its functions have been merged into the e1000 driver, which is an architecture-level reorganization. (Architecture event: Intel ICE driver module removed)
  ↳ No PR: [56c2a7f](https://github.com/DPDK/dpdk/commit/56c2a7f3467cc173568784193a9105b29991d9f7)
- Unified the Tx path of the Intel network card driver, including defining a common Tx entry structure, merging the Tx queue structure, introducing a common mbuf cleanup function, and unifying field naming and release logic. (Architecture-related: Intel network card driver Tx path unification)
  ↳ No PR: [5cc9919](https://github.com/DPDK/dpdk/commit/5cc9919fd443fbd3fce77a257601890a0ee6a247), [c038157](https://github.com/DPDK/dpdk/commit/c038157a2e4416338bb5c7171ae7d611c454045d), [cef0538](https://github.com/DPDK/dpdk/commit/cef05386b08a19741f0559f7f072eefb8b59f0bb), [bb8a37a](https://github.com/DPDK/dpdk/commit/bb8a37a95bad6734c9818ad6f7dee931c2f48c5b), [e61679e](https://github.com/DPDK/dpdk/commit/e61679e7be157c1cb2cf309533a20375b3478ef8), [4d0f54d](https://github.com/DPDK/dpdk/commit/4d0f54d9ef91184cc0027683af4ce9dd404391e3), [f6f34a5](https://github.com/DPDK/dpdk/commit/f6f34a5c24570276c81e36d21279e34e836b9366), [552979d](https://github.com/DPDK/dpdk/commit/552979dfb1c98a939b0f8b087547386d3c32ac00), [7c5d1d4](https://github.com/DPDK/dpdk/commit/7c5d1d4da3a652065c5b2b74455c608569bda100), [c2843ea](https://github.com/DPDK/dpdk/commit/c2843ea25801911665d8519504dcc98f12974ae9), [d3bb1c9](https://github.com/DPDK/dpdk/commit/d3bb1c9e0a16145eacc75deadc96726b351495ec), [6e40546](https://github.com/DPDK/dpdk/commit/6e4054618f47e3239f174e77d73af0176f8f7e7f)
- Created a public package reassembly function to unify the repeated package reassembly logic in multiple Intel network card drivers into a single implementation. (Architecture-related: public package reassembly function)
  ↳ No PR: [82fbc4a](https://github.com/DPDK/dpdk/commit/82fbc4a4479c4588e9e8c1067b5417a4547c0904)
- Rename the ROH_MAC module to HIMAC to avoid naming misunderstandings. (Architecture-related: module renaming)
  ↳ No PR: [501a40a](https://github.com/DPDK/dpdk/commit/501a40ae8370dcbfe086ef080a60c86a8d428ef6)
- Merged the IGC network card driver into the e1000 driver directory, and disabled the independent build of the IGC driver; at the same time, copied the i225 driver code to the e1000 directory and unified the symbol prefix. (Architecture-related: IGC driver merged into e1000)
  ↳ No PR: [010b69a](https://github.com/DPDK/dpdk/commit/010b69a03a94809a7112f68c463e74ebc66bd0ef), [7346f78](https://github.com/DPDK/dpdk/commit/7346f78b4f329ab1778c11f4bed5b20d8fe083e0)
- Moved the Intel network card driver from drivers/net to the drivers/net/intel subdirectory, merged the common/idpf and common/iavf drivers into the corresponding net/intel driver, and updated the build system and documentation. (Architecture-related: module reorganization and build update)
  ↳ No PR: [c1d1458](https://github.com/DPDK/dpdk/commit/c1d145834f287aa8cf53de914618a7312f2c360e), [04f1b16](https://github.com/DPDK/dpdk/commit/04f1b16c54f385efab527bd618083151f959229c), [f1fdc9d](https://github.com/DPDK/dpdk/commit/f1fdc9ddba5e82b080612d51a66ec6294e356093)
- The iavf driver uses the common Tx queue structure, and adjusts related fields and release logic accordingly. (Architecture-related: public API)
  ↳ No PR: [b92babc](https://github.com/DPDK/dpdk/commit/b92babc246830ede6c33a2dfa1d6291076b1a81d)
- The iavf driver AVX-512 path is changed to use the universal Tx release function, and the function signature is adjusted to support the context descriptor scenario. (Architecture-related: public API)
  ↳ No PR: [0f62bbe](https://github.com/DPDK/dpdk/commit/0f62bbef0b8893d7fa230c11d46603556489fb2b)
- The ixgbe driver is migrated to the general Tx queue structure, and related functions are updated to use the new queue type. (Architecture-related: public API)
  ↳ No PR: [f6e9f40](https://github.com/DPDK/dpdk/commit/f6e9f40fb9690ae5af15c116946d7d84ef1d7ab3)
- Added a function to obtain additional InfiniBand or MLX5 context, which is used to independently manage resources when the port starts and stops. (Architecture-related: public API)
  ↳ No PR: [786cd5b](https://github.com/DPDK/dpdk/commit/786cd5b0fac36386695627a102d58deb7b3552f8)
- Added memory allocation/release attribute annotations to the compressdev operation allocation function, and adjusted the release function declaration location. (Architecture-related: public API)
  ↳ No PR: [0ecabcb](https://github.com/DPDK/dpdk/commit/0ecabcb98d3a58849821c92164f9afc1cf696f3e)
- Created a public mbuf initialization function for the Intel network card driver, replaced the repeated rxq_vec_setup_default implementation in each driver, and added a vector driver capability check function. (Architecture-related: public initialization function)
  ↳ No PR: [61dcf27](https://github.com/DPDK/dpdk/commit/61dcf278a0958542414603afb21a3d3badd49380)
- Extracted the common enabling conditions of the Intel network card Rx vector driver to the public module, and updated the iavf, ice, and ixgbe drivers to use these common checks. (Architecture-related: common enabling conditions)
  ↳ No PR: [9eb6058](https://github.com/DPDK/dpdk/commit/9eb60580d155f5e3a36927dbb1e59ef9623231ce)
- Add basic function support to the zxdh network processor driver, including resource initialization, queue configuration, start and stop, data sending and receiving, and link status management. (Architecture-related: new driver support)
  ↳ No PR: [efb6a77](https://github.com/DPDK/dpdk/commit/efb6a77ff34ac26c6b46523bb6d8f40b0f87b93f), [7677f38](https://github.com/DPDK/dpdk/commit/7677f3871ef311bf190c7a6fa955d55afaf09935), [1193ce4](https://github.com/DPDK/dpdk/commit/1193ce452f49fdd2f7f2cf85ba58c28531f48369), [0eba152](https://github.com/DPDK/dpdk/commit/0eba152f427d9603cef57a610eda63561d38ae95), [4966a36](https://github.com/DPDK/dpdk/commit/4966a360a2e1665b436a7bf23a31b16ca5320312), [418d728](https://github.com/DPDK/dpdk/commit/418d728a4020a34e086fb459e3640eca7141e97a), [b502d9b](https://github.com/DPDK/dpdk/commit/b502d9b247bea227e894ec46f1dbee3bd3997101)
- Add MAC filtering support to the zxdh network card driver, provide MAC address settings, add and remove operations. (Architecture-related: public API extension)
  ↳ No PR: [78cc9a8](https://github.com/DPDK/dpdk/commit/78cc9a808f04c8d6e2ba06ad90a1296d327525d6)
- Add promiscuous mode and full multicast mode support to zxdh network device driver. (Architecture-related: public API extension)
  ↳ No PR: [267959f](https://github.com/DPDK/dpdk/commit/267959fba0716d9d6afde954b7a5f0b27f0e50f5)
- Add VLAN filtering and offloading operation support for zxdh network device driver. (Architecture-related: public API extension)
  ↳ No PR: [11300a7](https://github.com/DPDK/dpdk/commit/11300a7ff5b4a89da90993e42fa7de936e206900)
- The zxdh network card driver supports RSS configuration, and adds hash configuration and RETA update functions. (Architecture-related: public API extension)
  ↳ No PR: [9b2ce54](https://github.com/DPDK/dpdk/commit/9b2ce54ea216a8699d0d460e871d139f6d5a53ac)
- The zxdh network card driver supports the MTU update operation and sets the maximum and minimum MTU values in the device information. (Architecture-related: public API extension)
  ↳ No PR: [1c6d5cd](https://github.com/DPDK/dpdk/commit/1c6d5cd9ceab0b3274ee5c13c08011fc662880e6)
- Add hairpin packet loss counters for mlx5 PMD, including port-level and queue-level counters. (Architecture-related: public API)
  ↳ No PR: [f0c0731](https://github.com/DPDK/dpdk/commit/f0c0731b6d40db253c0ed80b5795f74e74540e3c)
- Added ROC API for checking MACsec hardware capabilities. (Architecture-related: public API)
  ↳ No PR: [1ee0302](https://github.com/DPDK/dpdk/commit/1ee0302b17028dd31ef3bb11e33e9e2319935805)
- Add hash report function to virtio network card, support reporting RSS hash value in packed ring queue in scalar mode. (Architecture-related: public API)
  ↳ No PR: [eca8915](https://github.com/DPDK/dpdk/commit/eca8915160613eb9904f3e1e1573887800a3b6cb), [2575909](https://github.com/DPDK/dpdk/commit/2575909a4c2311ebae7e8a132ccd7fa6c707d01b)
- Add initialization functions to XSC devices, including device operation registration, link management, queue creation and destruction, and RSS key modification interfaces. (Architecture-related: public API)
  ↳ No PR: [fb7d4f7](https://github.com/DPDK/dpdk/commit/fb7d4f7ae39a454eda094763b4d0a23e7acf29ce)
- Added mailbox mechanism to XSC network card driver for interaction between PMD and firmware. (Architecture-related: mailbox mechanism)
  ↳ No PR: [18979ca](https://github.com/DPDK/dpdk/commit/18979caf94854c379631113b78f4601e2fbd2c47)
- Add VFIO driver support to XSC network PMD, covering operations such as device initialization, opening, closing, BAR initialization, MTU setting and MAC address acquisition. (Architecture-related: public API)
  ↳ No PR: [31e84e3](https://github.com/DPDK/dpdk/commit/31e84e37c0b91edf2c696204134381e1854a3b20)
- Added a new Packet Classification Table (PCT) interface to the xsc network card driver, which supports creation, destruction, management of PCT entries and related IPAT/EPAT operations. (Architecture-related: public API)
  ↳ No PR: [9f75cad](https://github.com/DPDK/dpdk/commit/9f75cad1287fe0e87d10c492a772f4594968fbe1)
- Add representor initialization support to xsc PMD, including basic functions such as parameter parsing, queue release, MAC address addition and device activation. (Architecture-related: public API)
  ↳ No PR: [0b0f9c1](https://github.com/DPDK/dpdk/commit/0b0f9c161e07095e010a0226197e4ae935549e00)
- Add RSS configuration support to the xsc network card driver, including functions such as modifying RSS hash keys, obtaining and updating hash configurations. (Architecture-related: RSS configuration)
  ↳ No PR: [5fb899f](https://github.com/DPDK/dpdk/commit/5fb899f4b225f989745363ea6ab58bfe4670ff20)
- Implement startup function for xsc network card device, including initialization, start and stop of receive and send queues. (Architecture-related: device startup)
  ↳ No PR: [0ff4b93](https://github.com/DPDK/dpdk/commit/0ff4b93c318f1c374e7e6fa653bf550749d3f1dd)
- Add device stop and shutdown functions to the xsc network card driver. When stopped, the sending and receiving burst functions are reset and the sending queue resources are released. (Architecture-related: device stop/shutdown)
  ↳ No PR: [aa53f09](https://github.com/DPDK/dpdk/commit/aa53f0993ecf441862a019763cae444ab0642638)
- Add Rx receiving packet function to xsc network card driver, and add a new auxiliary function to check the ownership of the completion queue element. (Architecture-related: Rx receiving)
  ↳ No PR: [74af179](https://github.com/DPDK/dpdk/commit/74af179c1db5260735e90e630a68efe576ec3b5f)
- Implement the send burst function for the xsc network card driver. (Architecture-related: send burst)
  ↳ No PR: [2df8b91](https://github.com/DPDK/dpdk/commit/2df8b91a96da9b9eeef746f6b5526f63e60773b4)
- Add link status and MTU setting operations to the xsc network card driver, and fix the comparison logic in MAC address addition. (Architecture-related: public API)
  ↳ No PR: [4e1139c](https://github.com/DPDK/dpdk/commit/4e1139cc5c62142705701ba5e2bd6532ffd7386d)
- Add NPC flow processing and rte flow support to the CN20K platform, including MCAM entry operations, KEX configuration and public flow logic reconstruction. (Architecture-related: Platform compatibility: CN20K)
  ↳ No PR: [cedbdf7](https://github.com/DPDK/dpdk/commit/cedbdf7a1aa4bc392caa93aa9461a0a06f221564), [9d29cd6](https://github.com/DPDK/dpdk/commit/9d29cd6dc87d6c35c52194a5f7a34f2d84140353)
- Refactor the FPGA initialization function, remove unnecessary checks and logs, add support for the NT400D13 adapter, and use RTE_ASSERT for assertions instead. (Architecture-related: Hardware support: NT400D13)
  ↳ No PR: [217e266](https://github.com/DPDK/dpdk/commit/217e266a88bb4869d9ed4fbe51a3b7759f8f0ae6)
- Add driver support for RTL8168KB network card, including hardware initialization and configuration functions. (Architecture-related: Hardware support: RTL8168KB)
  ↳ No PR: [65b2af0](https://github.com/DPDK/dpdk/commit/65b2af0e4e81a713b8bc664c8f7e2e81b217e5f6)
- Add missing i225 series devices (including i226) to the IGC driver, and sort the device list. (Architecture-related: Hardware support: i225/i226)
  ↳ No PR: [8c1fa22](https://github.com/DPDK/dpdk/commit/8c1fa22a7d6a37c804c3373448d796ca087f33eb)
- Add support for more I219 series network devices to the e1000 driver, add multiple hardware IDs and update the corresponding initialization and configuration logic. (Architecture-related: platform compatibility)
  ↳ No PR: [fb78670](https://github.com/DPDK/dpdk/commit/fb78670e42922646582880635f9274e135b1e354)
- Add a common API function to enable/disable EEE (Energy Efficient Ethernet) in the e1000 base code. (Architecture-related: public API)
  ↳ No PR: [96a08cb](https://github.com/DPDK/dpdk/commit/96a08cb332acb7bfaa9e64b6a80f09eb5f9d3231), [fea90e5](https://github.com/DPDK/dpdk/commit/fea90e57c2cdb00d4f6140c06ad1ac5d86c68fb2)
- Add device profile information fields in the e1000 hardware structure to meet tool requirements. (Architecture-related: public API)
  ↳ No PR: [276d3f1](https://github.com/DPDK/dpdk/commit/276d3f100520bc2073d5e70a5cc1219b84b76b84)
- Add LPI counters to the e1000 basic driver to count EEE LPI events on the Tx and Rx paths. (Architecture-related: public API)
  ↳ No PR: [2e8078e](https://github.com/DPDK/dpdk/commit/2e8078ee69855c2f9fd91cfebe6a603c5380479d)
- Add the definition of the extended firmware semaphore (EXFWSM) register and related bit masks for the e1000 network card driver. (Architecture-related: public API)
  ↳ No PR: [1858060](https://github.com/DPDK/dpdk/commit/18580604c7bfad4a07202b74c4c5054106d94fab)
- Extend the ULP exit timeout on more hardware models, and add macro definitions and structure fields related to ULP WoL. (Architecture-related: platform compatibility)
  ↳ No PR: [7aa4c34](https://github.com/DPDK/dpdk/commit/7aa4c34581a55c4b7fb38f7bf1ccc66253fca590)
- Add WoL (Wake on LAN) related constant definitions for i210 network card. (Architecture-related: public API)
  ↳ No PR: [d7a7519](https://github.com/DPDK/dpdk/commit/d7a75194374ca8d1e40df2f129358bb726dcbc31)
- Add basic drivers to common/zsda to implement the initialization, registration, detection and removal functions of PCI devices. (Architecture-related: New driver module)
  ↳ No PR: [6592da5](https://github.com/DPDK/dpdk/commit/6592da5893d3a0146bd0508e0eccaea2853c3c42)
- Added hardware queue operation functions in the ZSDA public driver to support starting, stopping and clearing the queue. (Architecture-related: public API)
  ↳ No PR: [dc18741](https://github.com/DPDK/dpdk/commit/dc187415dce58bd08e274ac8934b3ea789148031)
- Add message channel functions to the zsda public driver, including queue management, register access and management of message sending and receiving. (Architecture-related: public API)
  ↳ No PR: [6fb10db](https://github.com/DPDK/dpdk/commit/6fb10db3d8b5626a6886e3204e8f46d1ed16f935)
- Added ZSDA compression device driver, including device interface skeleton, queue management, statistics, xform, enqueue and dequeue data paths and capabilities support. (Architecture-related: new driver module)
  ↳ No PR: [e585239](https://github.com/DPDK/dpdk/commit/e5852395e0219670b7be4529abdcc709cdad4d16), [b86de3b](https://github.com/DPDK/dpdk/commit/b86de3b1708458dbeb4a2367b7d1375135e0f5e9), [132fbfe](https://github.com/DPDK/dpdk/commit/132fbfe7f92d3e53804f9af1830eda0a656ca9b8), [5a3c51b](https://github.com/DPDK/dpdk/commit/5a3c51bd1d7a272104184052ba684c21ffd3c91b), [fe9228a](https://github.com/DPDK/dpdk/commit/fe9228a9ae3143f9f80eb50be70885e5f0542328), [3af6d99](https://github.com/DPDK/dpdk/commit/3af6d99705ccf96cb591de7586a792a001d5b959), [6c0e15e](https://github.com/DPDK/dpdk/commit/6c0e15eda46f8c64cc9db82c087f5782c014527b), [82f41e5](https://github.com/DPDK/dpdk/commit/82f41e589be4652ce1c13df82a11f6edae5d2c38)
- Added initialization functions for RPF and GFG modules, including configuration and stop interfaces. (Architecture-related: public API)
  ↳ No PR: [21144f4](https://github.com/DPDK/dpdk/commit/21144f438a31b4a73649b9cf5b1d2d8c159662db)
- Initialize NIM and PHY settings for Agilex FPGA ports, add loopback, reset and low power control functions. (Architecture-related: public API)
  ↳ No PR: [4dda924](https://github.com/DPDK/dpdk/commit/4dda9240b1d4b3ced366de79a78a6032ddcb56db)
- Add PHY line loopback configuration function to Agilex FPGA, and initialize host loopback support. (Architecture-related: public API)
  ↳ No PR: [eaaf350](https://github.com/DPDK/dpdk/commit/eaaf35045e1f9a05be4eae66eee0e6018a5cb98d)
- Implemented PHY host loopback configuration for Agilex FPGA, added line loopback function and optimized NIM I2C read and write and low power control. (Architecture-related: public API)
  ↳ No PR: [b02df67](https://github.com/DPDK/dpdk/commit/b02df6792d547e3e5b6c6bf6276e7095e24f4b41)
- Initialize NIM and 100G ports for Agilex FPGA, add link management, polarity switching, timestamp injection and I/O expander driver. (Architecture-related: public API)
  ↳ No PR: [c3d93ae](https://github.com/DPDK/dpdk/commit/c3d93ae1566b999bc065fc34c2a596ce9bc62b74)
- Added post-port initialization functionality for 100G NIM on Agilex FPGA, including configuring FEC and TX equalization. (Architecture-related: public API)
  ↳ No PR: [a79dd63](https://github.com/DPDK/dpdk/commit/a79dd63e88b7d97709577dfcf640ce8d5356e5fb)
- Added NIM reset and low power control functions, and added NIM existence check. (Architecture-related: public API)
  ↳ No PR: [95b394e](https://github.com/DPDK/dpdk/commit/95b394e51d922423e6f6a6025d666958d886b04a)
- Added link status management functions to the ntnic driver, including NIM module hot-plug processing, port disabling and link status reporting, and added PCA9532 LED controller initialization and LED control functions. (Architecture-related: public API)
  ↳ No PR: [c3d2bfd](https://github.com/DPDK/dpdk/commit/c3d2bfd4763481eeab9b0eabe368debb0c5d4ba6), [139d5e2](https://github.com/DPDK/dpdk/commit/139d5e2e59e126ba723444acbbabec0834f5d0da), [89881a8](https://github.com/DPDK/dpdk/commit/89881a8033f00fba857c52f0bc1ccf8f2064ffbb)
- Add minimal initialization support for NT400D13 network card, including clock synthesizer initialization, AVR detection, adapter ID mapping and operation registration framework. (Architecture-related: public API)
  ↳ No PR: [41aca2c](https://github.com/DPDK/dpdk/commit/41aca2c2083ebd0ddef603bd85972d5fcca86b54)
- Add FPGA reset function to NTNIC driver, define and register reset operation interface, support DDR4 reset and calibration completion processing. (Architecture-related: public API)
  ↳ No PR: [c7ea2ad](https://github.com/DPDK/dpdk/commit/c7ea2ad5c0087b3c34d51470880d26203fbfce99), [82fa5b3](https://github.com/DPDK/dpdk/commit/82fa5b38779310318070006968ac18f89e41b2cd), [1ce0bd6](https://github.com/DPDK/dpdk/commit/1ce0bd67a45df36e67f1abf33fa2e0ab97a22b24)
- Added FPGA module and register definitions for the NT400DXX card, including module initialization code, register header files, and updated module instance lists and mappings. (Architecture-related: public API)
  ↳ No PR: [e39037d](https://github.com/DPDK/dpdk/commit/e39037dc5b9723e5e755e2904db346a3e2eec56f), [a7bd262](https://github.com/DPDK/dpdk/commit/a7bd2629873899df82ee3717339a4813af66bc0a)
- Add a reset waiting function and reset process to the PHY FTILE module, and add DDR4 calibration and PHY FTILE reset waiting functions during the FPGA reset phase. (Architecture-related: public API)
  ↳ No PR: [5dbfa17](https://github.com/DPDK/dpdk/commit/5dbfa179740b53e0a2fe08cd213317b42d97ead6), [9a73c11](https://github.com/DPDK/dpdk/commit/9a73c11360f46c9e3deb570b66fdeaf6dd8efe2b)
- Add clock subsystem initialization support for ntnic network driver. (Architecture-related: public API)
  ↳ No PR: [c93a173](https://github.com/DPDK/dpdk/commit/c93a173df12f3a75fc28ea47c17c384ba00ed7b3)
- Initialize and create PCM support for NT400D13's FPGA and HIF modules. (Architecture-related: public API)
  ↳ No PR: [0948dde](https://github.com/DPDK/dpdk/commit/0948dde6f1bd6b4081b5cdf3927ce0c3ecc42838)
- Add read and write test register functions to HIF clock, and replace some assertions with RTE_ASSERT. (Architecture-related: public API)
  ↳ No PR: [568c631](https://github.com/DPDK/dpdk/commit/568c631ec8daa64cdefc2cea77262321b134619c)
- Add hardware initialization support to the NT400D13 platform, including the creation and initialization of PRM, SPI v3, I2CM, PHY Tile, IGAM and other modules, as well as peripheral reset and PLL configuration. (Architecture-related: core module)
  ↳ No PR: [aacb4fc](https://github.com/DPDK/dpdk/commit/aacb4fc0a686a9e03cd3e3a9abd7b1e2f9204b70), [9fab53d](https://github.com/DPDK/dpdk/commit/9fab53d7ded1d62faa778cfc6f38e5b9c13171d3), [949281e](https://github.com/DPDK/dpdk/commit/949281e310e20de7b20e441d34c4cff7aeef098b), [4cb190e](https://github.com/DPDK/dpdk/commit/4cb190e119ea8cb9146f961b1e72d894fe13eed4), [96970b2](https://github.com/DPDK/dpdk/commit/96970b2d8b6c40e8da6f5ce65e2b1737109cd44d), [ba17aac](https://github.com/DPDK/dpdk/commit/ba17aac63fd7a9d390cb18dd0cd6799a05eff2c5), [e1c59a0](https://github.com/DPDK/dpdk/commit/e1c59a07ac194c1979d6168aaa45405b642c934f), [28c08d3](https://github.com/DPDK/dpdk/commit/28c08d3138224c990576b766ebf9cba039844995), [f31f283](https://github.com/DPDK/dpdk/commit/f31f2834762f9d015b05aaed78c90e302cb0b943)
- Supports dynamic adjustment of ENA driver RSS indirect table size, no longer relying on a fixed 128 items based on device capabilities. (Architecture-related: RSS configuration)
  ↳ No PR: [923c753](https://github.com/DPDK/dpdk/commit/923c753a8f51fbedb906736ec0b82cc425ac3b2a)
- Added inline IPsec receive support for CN20K platform, modified WQE to mbuf conversion, vector processing and post-processing functions to handle safe offload flags and metadata buffers. (Architecture-related: Platform compatibility)
  ↳ No PR: [5856f23](https://github.com/DPDK/dpdk/commit/5856f23129bb084e5d5028a736802288bcbb2416), [edd0d5f](https://github.com/DPDK/dpdk/commit/edd0d5f3c299ab7790d82e3e80aaae51faad857c)
- Added reorganization configuration file support for NIX inline paths, and updated the mailbox interface to support CN20K new fields. (Architecture-related: platform compatibility)
  ↳ No PR: [fc9a711](https://github.com/DPDK/dpdk/commit/fc9a711b5c8ff4c9fb6f00d543f46c1d05ae7949), [9cf6470](https://github.com/DPDK/dpdk/commit/9cf6470da05a71a20b5ff8f0bc268d86f59da09f)
- Add support for multiple inline inbound queues to the CN20k platform, allowing applications to attach inline inbound queues directly instead of through CPT PF. (Architecture-related: public API: inline inbound queue)
  ↳ No PR: [f410059](https://github.com/DPDK/dpdk/commit/f410059baac620df99fe7ca1370156865ce00d45)
- Added ROC API for Inline devices, used to obtain IPsec and reassemble profile ID. (Architecture-related: public API: ROC API)
  ↳ No PR: [64f7d4a](https://github.com/DPDK/dpdk/commit/64f7d4abb06c060e9d1cfcb23e7985e714033f27)
- Added support for the creation and destruction of inline IPsec sessions for the CN20K platform, and registered corresponding security operation callbacks. (Architecture-related: public API: security operation callbacks)
  ↳ No PR: [7eaa499](https://github.com/DPDK/dpdk/commit/7eaa499dd0c2ded0e56f157b874348ec11fbb9aa)
- Add support for SM4 GCM symmetric algorithm in cryptodev and AESNI_MB PMD, requires Intel IPsec MB library v2.0 and above. (Architecture-related: public API)
  ↳ No PR: [1f4d2a2](https://github.com/DPDK/dpdk/commit/1f4d2a286ee0fc8faa55e9b029d3b71a2c68b5ba), [df4acb2](https://github.com/DPDK/dpdk/commit/df4acb2d31dc699f1dcab4a14b5030caf4d9269d)
- Optimize NP DTB channel initialization, change global DTB data to per-device structure, and add RSS, VLAN, promiscuous mode, MAC address configuration and other functional support. (Architecture-related: driver core reconstruction)
  ↳ No PR: [f7132f9](https://github.com/DPDK/dpdk/commit/f7132f9cc664b9701b8ee52a293b2ce285777672)
- Update Rx/Tx implementation, add offload detection, packet statistics and descriptor management functions, and reconstruct related data structures. (Architecture-related: driver core reconstruction)
  ↳ No PR: [5b91a42](https://github.com/DPDK/dpdk/commit/5b91a4201c4ab10d04e3e9d8ad4452412da1c997)
- Provide PF/VF message interrupt callback, new message reception callback registration, VF mixed mode control and VF MAC table addition function for the zxdh network card driver. (Architecture-related: internal interface)
  ↳ No PR: [2e22ff2](https://github.com/DPDK/dpdk/commit/2e22ff2528dba000216a7783b881344f55cdd346)
- Added RSS hash configuration, enablement, and RSS table setting and acquisition functions for VF. (Architecture-related: driver function enhancement)
  ↳ No PR: [01acc23](https://github.com/DPDK/dpdk/commit/01acc23bab131de376a0cbd81b4a3f3e844aea60)
- Optimize basic statistics functions, restructure statistical field naming and add multiple statistics acquisition and reset interfaces. (Architecture-related: public API)
  ↳ No PR: [2584716](https://github.com/DPDK/dpdk/commit/258471636d2eb3b856175f6022c95e54bf29028e)
- Added checksum, TSO, LRO, extended statistics, firmware version acquisition, module EEPROM reading and entry metering functions to the zxdh network card driver. (Architecture-related: public API)
  ↳ No PR: [02c4070](https://github.com/DPDK/dpdk/commit/02c4070d3b09bf836a9d30b7326cc3486464008a), [ca3a702](https://github.com/DPDK/dpdk/commit/ca3a7025f72f211d914e374461be5ab995063666), [0cc33ad](https://github.com/DPDK/dpdk/commit/0cc33adc3d1b0eb9677aec475979669284bfe45c), [f566e15](https://github.com/DPDK/dpdk/commit/f566e15ff2883c1a2005311b65f311559704fbc5)
- Added support for packed ring in the virtio crypto driver, including functions such as initialization, data transmission and reception, and interrupt control; and added vDPA backend support for virtio_user crypto. (Architecture-related: public API)
  ↳ No PR: [6676419](https://github.com/DPDK/dpdk/commit/66764190712db5da21ce595c4cc519fcef5b974a), [a03c2af](https://github.com/DPDK/dpdk/commit/a03c2aff6421993ecfedd98cc7549c4492e069a0)
- Added sfc_get_restore_flags function, returns 0 to indicate that sfc PMD does not need to be configured for recovery, to avoid repeated recovery of MAC addresses by the ethdev layer, promiscuous and full multicast modes. (Architecture-related: external behavior)
  ↳ No PR: [1311ec2](https://github.com/DPDK/dpdk/commit/1311ec23f6bfd3a71a76cd3ceaffdeec2ed623c5)
- Unify NFP network card Rx/Tx queue threshold query, so that the threshold returned by rte_eth_rx_queue_info_get() and rte_eth_tx_queue_info_get() is consistent with the device default configuration. (Architecture-related: public API)
  ↳ No PR: [4f0ece5](https://github.com/DPDK/dpdk/commit/4f0ece5e5a38df8aac666e1f7ea2642b449be848)
- Fixed the problem of hardcoding the dedicated hardware queue size in bonding PMD. Instead, use the minimum hardware queue size of the member port to initialize the dedicated queue to avoid port startup failure due to insufficient number of required descriptors for some NICs. (Architecture-related: public API)
  ↳ No PR: [4da0705](https://github.com/DPDK/dpdk/commit/4da0705bf896327af062212b5a1e6cb1f1366aa5)
- Corrected the value of the IXGBE_SUBDEV_ID_E610_VF_HV macro to avoid conflict with the real device ID, and solved the problem of driver hang in the virtual machine. (Architecture-related: platform compatibility)
  ↳ No PR: [e5e7c3c](https://github.com/DPDK/dpdk/commit/e5e7c3cababa83b7e412e2fc87ce4de55b73b094)
- Added complete start, stop, reset and shutdown operations for ngbe VF devices, and added device operation functions such as VLAN filtering, queue settings, etc. (Architecture-related: device operations)
  ↳ No PR: [95956bc](https://github.com/DPDK/dpdk/commit/95956bc0de17b90cdc8314ca65df29abb1fb3de5)
- Adjust the maximum number of actions of mlx5 driver HWS rules from 16 to 32 to be compatible with SWS. (Architecture-related: public API)
  ↳ No PR: [ab54e17](https://github.com/DPDK/dpdk/commit/ab54e17fe2f5207d7b988d568344570e156551ad)
- Fixed the problem of flow processing in ICE PMD that violated the rte_flow API, removed the dependence on the group attribute, and instead evaluated each engine parser in sequence according to the hardware pipeline order. (Architecture-related: public API)
  ↳ No PR: [fabc9e1](https://github.com/DPDK/dpdk/commit/fabc9e1322e26b41ab74a8e35dcb477c702c3f6d)
- Fixed the read and write logic of the PHY register in the e1000 driver, added a write function for the GPY PHY register, and added a PHY read/write retry mechanism to solve occasional MDI errors. (Architecture-related: public API)
  ↳ No PR: [62addde](https://github.com/DPDK/dpdk/commit/62adddef81d4ddb9789e9f0e5a0899b399bd5d8d), [bdca22d](https://github.com/DPDK/dpdk/commit/bdca22d62ff0555cb4d8498478e2981c16e05290)
- Fixed the crash problem of e1000, igb, igc and ixgbe network card drivers in the secondary process, by prohibiting calling the base driver function pointer or adding process type checking. (Architecture-related: multi-process compatibility)
  ↳ No PR: [b0ef6e7](https://github.com/DPDK/dpdk/commit/b0ef6e7a970bc745537c5b5140d838431f118c5e), [c092ecb](https://github.com/DPDK/dpdk/commit/c092ecb6d1d4cc27eebbcaf43c2ad35c4cfed4e1)
- Fixed the minimum number of receive/transmit ring descriptors of the ixgbe driver, adjusting the default minimum value from 32 to 64. (Architecture-related: public API)
  ↳ No PR: [6808ee1](https://github.com/DPDK/dpdk/commit/6808ee1ceddc76846f80ae3d05aad374a34a1754)
- Fixed the issue where the nfp driver did not pass the PF ID to the BSP when loading firmware, resulting in DMA mapping errors in multi-PF scenarios. (Architecture-related: nfp multi-PF DMA mapping)
  ↳ No PR: [2bcb9c9](https://github.com/DPDK/dpdk/commit/2bcb9c942fc9e81e035f3f34bdb872ba4de2c076)
- Fixed the mbuf release problem in Arm multi-process environment, and extended the x86 fix to Arm architecture. (Architecture-related: Arm platform compatibility)
  ↳ No PR: [289d1b2](https://github.com/DPDK/dpdk/commit/289d1b2e348032543f9b823d2eaf3d0e0073af56)
- Added interrupt registration success check in iavf driver initialization, falls back to polling mode when registration fails, fixed management queue message loss problem on FreeBSD caused by interrupt registration failure. (Architecture-related: FreeBSD platform compatibility)
  ↳ No PR: [12e8844](https://github.com/DPDK/dpdk/commit/12e8844f0bda3c4e4e578e180dfa0136f9285182)
- Fixed the problem of port closing failure due to context inconsistency during GENEVE parser cleanup. Instead, an independent context is created by the physical device to ensure that the parser uses a consistent context for creation and cleanup. (Architecture-related: GENEVE parser context)
  ↳ No PR: [c8a6da8](https://github.com/DPDK/dpdk/commit/c8a6da8678c12bd4c7814a9b15c3cd05402d253f)
- Added missing PCI ID check for E610 virtual function device in ixgbe driver. (Architecture-related: Platform Compatibility)
  ↳ No PR: [6e41ba1](https://github.com/DPDK/dpdk/commit/6e41ba1306e6f57f6812883df0e4687894fa70b7)
- Change the context cache field in the ixgbe Tx queue structure from an array to a pointer, and dynamically allocate memory when the queue is set up. (Architecture-related: public API)
  ↳ No PR: [c5faf26](https://github.com/DPDK/dpdk/commit/c5faf26beb3869b13746a6decd0427b70e01ec50)
- Remove variable-length arrays in the ice driver, replace runtime dynamic arrays by pre-allocating extra space during queue setup, and eliminate compilation warnings. (Architecture-related: public API)
  ↳ No PR: [9c22583](https://github.com/DPDK/dpdk/commit/9c22583423e074db8ae9cd7a1fa1ed0537551756)
- Removed weak symbols in the fm10k driver and instead provided stub functions under non-x86 architectures to improve platform compatibility. (Architecture-related: Platform compatibility)
  ↳ No PR: [14f8c27](https://github.com/DPDK/dpdk/commit/14f8c270824e64dca79cde820934dcc149480b6c)
- Remove weak symbols and deprecate the __rte_weak macro, instead use conditional compilation to provide stub implementation for non-ARM64 architecture. (Architecture-related: platform compatibility)
  ↳ No PR: [2d6abf5](https://github.com/DPDK/dpdk/commit/2d6abf506dfe5cccc0db3e607bc76da30c54236f), [fd233ad](https://github.com/DPDK/dpdk/commit/fd233ad17e5ffa42d50f1625165a7fce3f1cbc5f)
- Remove iNVM support for i225 devices, and change e1000_set_ltr_i225 and e1000_access_phy_wakeup_reg_bm functions to non-static to expand visibility. (Architecture-related: public API)
  ↳ No PR: [92f202f](https://github.com/DPDK/dpdk/commit/92f202f1e3274540ef8da20fc0e77ed2aea86c39), [e4d0b20](https://github.com/DPDK/dpdk/commit/e4d0b20aad04dfe0f9b64aad47053cebbd34ba60), [ca44b87](https://github.com/DPDK/dpdk/commit/ca44b874712937d4d1ed108a03f9f6a2a2e2c60a)
- Upgrade the ena-com module, remove the obsolete ena_com_get_offload_settings function, and rename the interrupt register related functions to unified naming. (Architecture-related: public API)
  ↳ No PR: [b1ca35a](https://github.com/DPDK/dpdk/commit/b1ca35adab93a66f7a0e86b3ae6d6cf09ce37950)
- Concentrate the common logic of buffer release after sending in i40e, iavf and ice drivers into the Intel public driver. (Architecture-related: Intel network card driver common logic concentration)
  ↳ No PR: [b87fc21](https://github.com/DPDK/dpdk/commit/b87fc2117eb2a35a8c65c9dd74b5aace40fbad95)
- Allow the ice driver to be compiled independently when the iavf driver is not built, and avoid unnecessary symbol exports through conditional compilation. (Architecture-related: build and installation methods)
  ↳ No PR: [c799bf0](https://github.com/DPDK/dpdk/commit/c799bf0d9cb1b0b7b0199f518d95baed6c40e9de)
- Fixed the build warning caused by overriding the -march flag of the Intel network card driver under the icx compiler. By adding the -Wno-overriding-option compilation option, it is allowed to build normally when -Werror is enabled. (Architecture-related: build and installation methods)
  ↳ No PR: [2641704](https://github.com/DPDK/dpdk/commit/2641704664267dd3ebe4ad77784ae28440dfaf60)
- Initialize the network processor, unify function naming prefixes and add resource management functions. (Architecture-related: public API)
  ↳ No PR: [a51e807](https://github.com/DPDK/dpdk/commit/a51e80702d1d4db4c16feb033148192ab61fcbc2)

### Output Transmission and Buffer Management Filter
- Introduce unified FDB_UNIFIED subfield into FDB table type, update table initialization and type judgment logic, and add auxiliary functions to improve code readability. (Architecture-related: FDB table introduces unified subfield)
  ↳ No PR: [94c90db](https://github.com/DPDK/dpdk/commit/94c90db63773dddd33e6262c69347562c69a83f8), [1951fb1](https://github.com/DPDK/dpdk/commit/1951fb1331d2987008630e025f6546c1c41f0c88)
- NFP network card driver adds Rx and Tx burst mode query support. (Architecture-related: public API)
  ↳ No PR: [4dcbf32](https://github.com/DPDK/dpdk/commit/4dcbf32ffefd84dbb5924de3b2c6dd517f7809c8)
- The MLX5 network card driver adds the probe_opt_en device parameter, which is used to control probe optimization behavior. (Architecture-related: public API)
  ↳ No PR: [ecdc385](https://github.com/DPDK/dpdk/commit/ecdc385a84b71c4b40c1b3f847d7518239253b99)
- RDMA monitor adds backward compatibility support and falls back to the old way of updating port information when the kernel driver does not support it. (Architecture-related: platform compatibility)
  ↳ No PR: [cf35221](https://github.com/DPDK/dpdk/commit/cf352218fb714ba53eb5ba85e3ec8eb21543b927), [2ab0ece](https://github.com/DPDK/dpdk/commit/2ab0ece5b5edde3f563098809c29105ea12b2b0a)
- Add unified FDB subdomain support in the mlx5 driver, including capability flags and dedicated action flags, allowing users to specify the FDB_UNIFIED domain to process packets from any port. (Architecture-related: FDB_UNIFIED domain support)
  ↳ No PR: [79c6f29](https://github.com/DPDK/dpdk/commit/79c6f29f38d92797c2a5e9a4e68715ba81adf885), [9bc7955](https://github.com/DPDK/dpdk/commit/9bc795541094dcaa222255232d98c645ecb3aab5), [3630292](https://github.com/DPDK/dpdk/commit/363029214a810071846ba27a9812336c8c921632)
- Allow adding DROP target in image clone action. (Architecture-related: Image clone action extension)
  ↳ No PR: [0c54d67](https://github.com/DPDK/dpdk/commit/0c54d671079cb5e1526e43fc5d9cca6c39883fdb)
- Add function attribute annotations to the mempool allocation function to detect when the mempool is not released correctly after allocation. (Architecture-related: public API)
  ↳ No PR: [24f45f0](https://github.com/DPDK/dpdk/commit/24f45f0a0f2bbe02a2445dcd88280c35def436d7)
- Add attribute annotations to the allocation function of the reorder library, and expose the rte_reorder_free interface to help detect problems with incorrect release after allocation. (Architecture-related: public API)
  ↳ No PR: [db372de](https://github.com/DPDK/dpdk/commit/db372de141bab36cbb3d45049659b48670d006eb)
- Fixed a potential crash problem caused by uninitialized variables in the stack pop operation in C11 atomic implementation. (Architecture-related: public API)
  ↳ No PR: [916424f](https://github.com/DPDK/dpdk/commit/916424f2c6029cd8da5c56ed62847a4b09d7e0ac)
- Add allocation and release annotations to the scheduling port configuration function to help detect memory leaks. (Architecture-related: public API)
  ↳ No PR: [e4f6a30](https://github.com/DPDK/dpdk/commit/e4f6a306b4393021972d700bc7f53ff13dc64fe7)

### Header Parsing and Decapsulation Filter
- Reconstruct the RSS implementation, extract the conversion logic from the RTE_ETH_RSS field to the HSH register into a separate file, remove the profile wrapper, and use the unified hsh_set interface to replace the original hasher configuration function. (Architecture-related: public API)
  ↳ No PR: [bbe6f8f](https://github.com/DPDK/dpdk/commit/bbe6f8f96d2ffec34aff0cc8b1983603e7a4a0df)
- Added eventdev telemetry device information query command, and added /eventdev/list and /eventdev/info as standard aliases. (Architecture-related: public API)
  ↳ No PR: [feaea05](https://github.com/DPDK/dpdk/commit/feaea0573429ae2a69a4e375c1f642404bbe6313), [9920eff](https://github.com/DPDK/dpdk/commit/9920eff5eee38e7cd3f88011e65eddcc78f0bd9d)
- Add enhanced lock annotation macros to the EAL library to support Clang shared and exclusive capability annotations. (Architecture-related: public API)
  ↳ No PR: [9cef0ff](https://github.com/DPDK/dpdk/commit/9cef0ff8dfb977cc4a46ba3a38f0df3c5b7f1aee)
- The eventdev port attribute query function adds support for independent enqueuing attributes. (Architecture-related: public API)
  ↳ No PR: [8c565bb](https://github.com/DPDK/dpdk/commit/8c565bbebb8f72decbc4af6a69cb76f07bffc472)
- Add a packet loss counter to the IP fragmenter (IFR) to count the number of packets dropped because the size of the packet exceeds the MTU. (Architecture-related: public API: Packet loss statistics)
  ↳ No PR: [306a245](https://github.com/DPDK/dpdk/commit/306a245d2ce1fdfc19cc2ad0c0c07d46089c9900)
- Add 100G link operation support for NT400D13 (Intel Agilex FPGA), including link initialization, state machine, reset and loopback, etc. (Architecture-related: link operation interface)
  ↳ No PR: [36ad65b](https://github.com/DPDK/dpdk/commit/36ad65b2f58b6b2dbb24845b233b14dafa5d443b), [93a1966](https://github.com/DPDK/dpdk/commit/93a19661c6a1b9ed649e4882ef9eb993b6a349d5)
- Added thread-safe CRC API (with _v26 suffix), and updated QAT driver and test cases to adapt to the new interface. (Architecture-related: thread-safe CRC API)
  ↳ No PR: [52633e3](https://github.com/DPDK/dpdk/commit/52633e3a3fa8cd274acd0b7c41f39c4290f353fd)
- Added type resolution support for VXLAN, VXLAN-GPE, GTP and Geneve tunnel protocols, expanding network packet processing capabilities. (Architecture-related: parsing behavior)
  ↳ No PR: [64ed7f8](https://github.com/DPDK/dpdk/commit/64ed7f854cf445829b525df7b27ed00a9bcc9b16)
- Add a release function declaration to the event ring allocation function, and mark the __rte_malloc and __rte_dealloc attributes to support memory leak detection. (Architecture-related: public API)
  ↳ No PR: [9317108](https://github.com/DPDK/dpdk/commit/9317108275402a2868d8fb165106a69d2ee9d652)
- Fixed the registration failure problem caused by the return value not being updated correctly when registering VDUSE devices. (Architecture-related: public API)
  ↳ No PR: [36309ee](https://github.com/DPDK/dpdk/commit/36309ee895a0955d03d15cc3b49657d20fafbfc0)
- Fixed the display of group jump in flow dump, now output the original group number instead of internal encoding. (Architecture-related: public API)
  ↳ No PR: [61399e5](https://github.com/DPDK/dpdk/commit/61399e5e649436b1e9f566e2f2af447bfcce2b3b)
- Fixed the order issue of file descriptor cleaning in vhost. Now the FD will be removed from the collection first and then the shutdown operation is performed to avoid epoll errors. (Architecture-related: vhost core module)
  ↳ No PR: [5096693](https://github.com/DPDK/dpdk/commit/50966930caf2d1a82655f2c3415c093421d70072)
- Add assertions in the rte_lcore_var_lcore function to ensure that the passed handle pointer is not null to catch initialization or allocation problems in advance. (Architecture-related: public API)
  ↳ No PR: [c35c550](https://github.com/DPDK/dpdk/commit/c35c550a7068d8a68a1faf580d0c029d53321a20)
- Remove the deprecated error conversion function in the ntnic driver and simplify the related error handling logic. (Architecture-related: public API)
  ↳ No PR: [46a660a](https://github.com/DPDK/dpdk/commit/46a660a031c9968ff4250a8806a149189831fa67)
- Add nthw prefix to functions with abstract names in ntnic driver to avoid exposing global symbols. (Architecture-related: public API)
  ↳ No PR: [2364700](https://github.com/DPDK/dpdk/commit/2364700d16e60a0a74725a754c610cc6b40c90bf)

### Action Execution and Hardware Offload Filter
- The IE engine is only enabled on CN9K and CN10K platforms, other platforms no longer include the IE engine group. (Architecture-related: platform compatibility)
  ↳ No PR: [419bcc7](https://github.com/DPDK/dpdk/commit/419bcc73a943ed40a613194531e73d80b5d44a9f)
- Fix the C++ inclusion issue in the cryptodev header file to ensure that related functions are correctly wrapped in extern "C" blocks. (Architecture-related: public API)
  ↳ No PR: [24d4d29](https://github.com/DPDK/dpdk/commit/24d4d29b5f553e0bae42702b246ae97a812e8f45)

### ACL and LPM Match Filter
- Add function attributes to telemetry data allocation functions to help detect cases where they are not released correctly after allocation. (Architecture-related: public API)
  ↳ No PR: [414e642](https://github.com/DPDK/dpdk/commit/414e64245bd56fe3e693447b1d31bb9abc8af9de)
- Update the virtio_crypto_config structure, replacing reserved fields with AKCIPHER algorithm fields to comply with the VirtIO standard. (Architecture-related: public API)
  ↳ No PR: [2c0d9a8](https://github.com/DPDK/dpdk/commit/2c0d9a8b497d6bacf212cabd65b996a9becb56f6)
- Add complete VF device support to the ngbe network card driver, including driver basics, PF-VF communication, hardware configuration, network functions, data path, interrupts, statistics and link management. (Architecture-related: VF device support)
  ↳ No PR: [950820f](https://github.com/DPDK/dpdk/commit/950820f10cb8a8c45998536546b5a00123fe40aa), [ace4497](https://github.com/DPDK/dpdk/commit/ace44974a1b767dee3417a5b737d962127c4a289), [66070ca](https://github.com/DPDK/dpdk/commit/66070ca419c1675c5f64f32908f1eae510dd3637), [7744e90](https://github.com/DPDK/dpdk/commit/7744e90805b525162441f02c3bccfc1f73b1b07c), [7710237](https://github.com/DPDK/dpdk/commit/77102375801d01abdf937434de0fb5c519e2af2b), [2aba42f](https://github.com/DPDK/dpdk/commit/2aba42f6712c9ffd87a1c2cf227c23f0166f2f96), [711a06e](https://github.com/DPDK/dpdk/commit/711a06e896ba6307089bb6aa707c16ab3a110d20), [f47dc03](https://github.com/DPDK/dpdk/commit/f47dc03c706ff314e7e2b5ff28a3678834dfff04), [fda4258](https://github.com/DPDK/dpdk/commit/fda42583f6b13c48b421b4c847ddf340807ea5cf), [62c072c](https://github.com/DPDK/dpdk/commit/62c072c03c146b50aaef58893d02f9fd270193ee), [1d13283](https://github.com/DPDK/dpdk/commit/1d13283a1a6211a2ecba7ee9e59476dade9135d3), [e0c29b2](https://github.com/DPDK/dpdk/commit/e0c29b2f6568a71372b0a0a0ee5bcaa54ec98a1b), [54670a1](https://github.com/DPDK/dpdk/commit/54670a16f7ab0ee3fc77adb4d26802b11f2f3ea1), [551b556](https://github.com/DPDK/dpdk/commit/551b556c56d2003e6763a6abbb365e02abba5236)
- Add IPv4 fragmentation processing support to the ice driver, including fragmentation flags, offset fields, offset mask matching and fragmentation mode support in ACL filters. (Architecture-related: public API extension)
  ↳ No PR: [4454410](https://github.com/DPDK/dpdk/commit/44544107dd4bfd6e3aed96b2f8d8d1c607d429dc), [ec3025b](https://github.com/DPDK/dpdk/commit/ec3025b7ae9f945f3abc9d5add4c012dc375b94b), [a9d6122](https://github.com/DPDK/dpdk/commit/a9d612291c2d5e1a65cba3cd9e6ff2fafe2c164a)
- Add inline IPsec rule support for the CN20K platform, use the UCAST_CPT action instead of UCAST_IPSEC, and restructure the relevant judgment logic to be compatible with both platforms. (Architecture-related: Behavior changes: UCAST_CPT)
  ↳ No PR: [57c9296](https://github.com/DPDK/dpdk/commit/57c9296593d9f2b446fdc2337df580aab6e3c37b)
- Enable full multicast mode for CGX/RPM VF devices, and adjust promiscuous mode configuration logic to only enable promiscuous mode on non-VF devices. (Architecture-related: Behavior changes: Multicast vs. promiscuous mode)
  ↳ No PR: [2b94c80](https://github.com/DPDK/dpdk/commit/2b94c8091b9daf32001284942cd0370f5965a3fd)
- Added support for eCPRI item matching in mlx5 HWS, supporting both template API and backward compatibility API; and supporting MPLSoGRE matching, removing related verification restrictions, using MPLSoUDP by default in non-relaxed mode, and only setting the MPLS destination port for the UDP protocol. (Architecture-related: public API)
  ↳ No PR: [93c7d4c](https://github.com/DPDK/dpdk/commit/93c7d4c226285218b887e96f226836e12447da65), [3c85457](https://github.com/DPDK/dpdk/commit/3c8545717fa8e180591b0ab5476edef00eafdbb1)
- Fix the DPI mailbox structure, adjust the field bit width to ensure that the mailbox fields are correctly aligned. (Architecture-related: public API)
  ↳ No PR: [b03c474](https://github.com/DPDK/dpdk/commit/b03c474188383c3d3d529b1c9ca86767e5fb6167)
- Add memory allocation and release attribute annotations to the creation functions of FIB and FIB6 to help detect memory leaks. (Architecture-related: public API)
  ↳ No PR: [8faad33](https://github.com/DPDK/dpdk/commit/8faad338277ac3880621406637613347fd055ae1)
- Add __rte_malloc and __rte_dealloc attributes to the RIB allocation function, and adjust the declaration positions of rte_rib_free and rte_rib6_free to assist in detecting the problem of incorrect release after allocation. (Architecture-related: public API)
  ↳ No PR: [fa0c2e4](https://github.com/DPDK/dpdk/commit/fa0c2e4c1c2cecd7156c4a1c809f359933148a17)
- Add __rte_malloc and __rte_dealloc attribute annotations to LPM allocation functions to help detect improperly released memory. (Architecture-related: public API)
  ↳ No PR: [a998fce](https://github.com/DPDK/dpdk/commit/a998fce7b7026bdfa86ce8a9ea52ed561300bd2e)
- Add memory allocation and release attribute annotations to the ACL context allocation function to help the compiler detect memory leaks that are not released correctly. (Architecture-related: public API)
  ↳ No PR: [890f4db](https://github.com/DPDK/dpdk/commit/890f4db14ba2fa128aa4e8c8fc3c240fdc04a053)
- Add __rte_malloc and __rte_dealloc attribute annotations to the rte_member_create function, and adjust the rte_member_free declaration position to support the compiler in detecting memory leaks. (Architecture-related: public API)
  ↳ No PR: [aacdb6e](https://github.com/DPDK/dpdk/commit/aacdb6e3db58880b256c1097c1fc251c45422445)
- Fixed compilation issues caused by const conversion under Arm SVE. (Architecture-related: platform compatibility)
  ↳ No PR: [1c97680](https://github.com/DPDK/dpdk/commit/1c97680265f59f8ed453b72460cb755248104668)
- Adjusted the flow engine evaluation order, prioritizing the ACL engine over the switch engine to solve the scalability problem of wildcard flow rules. (Architecture-related: flow engine evaluation order)
  ↳ No PR: [b309503](https://github.com/DPDK/dpdk/commit/b309503d63159680d4ff8ca9e968fcb12ac609a0)
- Add the -mavx512cd option to the public AVX512 flag set, and update the build script of the ACL library to reuse public variables, simplify conditional judgments and compilation parameters. (Architecture-related: platform compatibility)
  ↳ No PR: [bce754b](https://github.com/DPDK/dpdk/commit/bce754b5d9420e3fd65ab305dfb29c9c088e443c)

## Routine Changes

### New features
- dpdk-devbind.py adds --uid and --gid options to support specifying user and group IDs when binding devices to VFIO.
  ↳ No PR: [29522b9](https://github.com/DPDK/dpdk/commit/29522b9d193aae818fcf73167f61d4bb915a4087)
- Added a new interface for the E610 network card to set the port identification LED through the ACI command.
  ↳ No PR: [ed20d19](https://github.com/DPDK/dpdk/commit/ed20d19a56a796eafdc02b8a7c03526fd835406a)
- Add PTP timestamping by PHY function to E610 network card, and enhance clock drift threshold configuration.
  ↳ No PR: [b58cf63](https://github.com/DPDK/dpdk/commit/b58cf63abdb17a6dd97b0e4edd160e9917b9c143), [08e467a](https://github.com/DPDK/dpdk/commit/08e467a7a937c586e2588888e1577c82860e2c60)
- Add OROM recovery update capability support for ixgbe base driver.
  ↳ No PR: [4072c7a](https://github.com/DPDK/dpdk/commit/4072c7a6889dffc70c4112778ee43a32d59ac3e0)
- Add Tx timestamp descriptor and queue context configuration support to ice network card driver.
  ↳ No PR: [bbb674b](https://github.com/DPDK/dpdk/commit/bbb674b09ce10b2e4fc5fab4cc4dca3abc02881f), [bbf08f9](https://github.com/DPDK/dpdk/commit/bbf08f9e42740fee366c3cf1304115bbd467c86e)
- testpmd supports updating port information through event callbacks in multi-process scenarios to implement port mounting and unmounting.
  ↳ No PR: [994635e](https://github.com/DPDK/dpdk/commit/994635edb2c038e64617bcf2790a8cd326c3e8e0)
- AF_PACKET PMD adds configurable fan-out mode support, using PACKET_FANOUT_HASH by default.
  ↳ No PR: [d3bc77a](https://github.com/DPDK/dpdk/commit/d3bc77ab05a430cdd9bc3497edbfa1d7e1bb94ac)
- cnxk dmadev maximum number of virtual channels per queue increased from 4 to 128.
  ↳ No PR: [212bfb5](https://github.com/DPDK/dpdk/commit/212bfb5c4cbd1a2dc3a12f6f52f0b0299a67ff98)
- The af_packet driver adds packet loss statistics functions, including querying socket packet loss counters and mbuf allocation failure counters.
  ↳ No PR: [6b32462](https://github.com/DPDK/dpdk/commit/6b3246245507e5257a17c1684daed27d8a82fc7a)
- Add firmware loading support for network cards without DDR.
  ↳ No PR: [74fd1a7](https://github.com/DPDK/dpdk/commit/74fd1a71cec15ef439569e634a463f5f59925334)
- Add tracking points to the bbdev library, covering device configuration, queue operations, and the enqueuing and dequeuing processes of various encoding and decoding operations.
  ↳ No PR: [61aa25b](https://github.com/DPDK/dpdk/commit/61aa25b96e141eb2ef06e09269a2c2150ab2a638)
- Add trace points to the baseband/acc driver and use the acc_error_log function to replace the original error log.
  ↳ No PR: [ce28780](https://github.com/DPDK/dpdk/commit/ce28780dc54f2d3bb9b88212f3f2c059e35aa936)
- Add TSO support to axgbe PMD, including configuration, device information notification and implementation of sending paths.
  ↳ No PR: [186f8e8](https://github.com/DPDK/dpdk/commit/186f8e8c336158942d9dceae03db89266dddaa97)
- Added Rx and Tx queue initialization functions to the xsc network card driver, and added related data structure definitions and header files.
  ↳ No PR: [4882629](https://github.com/DPDK/dpdk/commit/488262986eeef83b5d75c5ffc3f04b2959235789)
- Added basic statistics functions to the xsc network card driver, enabling operations such as statistics acquisition, device start and stop, and queue release.
  ↳ No PR: [c80ab1a](https://github.com/DPDK/dpdk/commit/c80ab1a551cc5d15c4f9b00a2fc0e84564cadff6)
- Added device information query operation to xsc network card driver, and implemented auxiliary functions such as link control, queue offloading and statistics.
  ↳ No PR: [68c9f1c](https://github.com/DPDK/dpdk/commit/68c9f1c2cfd272cfd357c1223ffac9c723c5742b)
- Added the hide_zero option to the --xstats parameter of the dpdk-proc-info tool to support hiding extended statistics with a value of zero.
  ↳ No PR: [c2b6f3e](https://github.com/DPDK/dpdk/commit/c2b6f3e7212dc32603304a6bb41b0e8f081761a5)
- Added missing i210 and i219 series hardware device IDs for EM and IGB drivers.
  ↳ No PR: [6a0f605](https://github.com/DPDK/dpdk/commit/6a0f605bc582c50d119037bce3112f65db2ef78f)
- Added the function of reading PCIe bus information for i225 network card.
  ↳ No PR: [724c060](https://github.com/DPDK/dpdk/commit/724c060e89681377ebe3ff0d7533f9b5adc00714)
- Added power management control to the e1000 PHY, reducing post-reset latency by reading the PHPM register and polling the reset completion flag.
  ↳ No PR: [652a577](https://github.com/DPDK/dpdk/commit/652a577342e138cab2e16a7f822d8fc4659764bd)
- Added LED flash function support for i225 network card.
  ↳ No PR: [74496eb](https://github.com/DPDK/dpdk/commit/74496ebc30ed1ba5ce87c4a2e5bf306422e567a7)
- Added PHY reset support for i225 network card, using universal reset implementation.
  ↳ No PR: [6fdedd9](https://github.com/DPDK/dpdk/commit/6fdedd9e8834f792fb7fa8f517603b450dcdb95e)
- Added macro definitions related to address selection mask and queue selection for the e1000 network card driver, which are used for address filtering and specifying receive queues matching MAC addresses.
  ↳ No PR: [fe6a886](https://github.com/DPDK/dpdk/commit/fe6a886ff553a20912f8a4fbcfd8e6277cca3c54)
- Changed the pending count from per virtual channel to per hardware DMA channel, allowing the doorbell to ring for the exact number of DMA commands in the queue.
  ↳ No PR: [4746117](https://github.com/DPDK/dpdk/commit/47461173800f029033d7088b7d49860ea27305db)
- Supported DROP operation in multi-destination action, set NOP destination type when specifying DROP.
  ↳ No PR: [54795cb](https://github.com/DPDK/dpdk/commit/54795cbb4a67ab274a667d3ba309378f7f3b8139)
- Added support for ESP protocol in non-template RSS extension to enhance receiver scaling functionality.
  ↳ No PR: [6739c4b](https://github.com/DPDK/dpdk/commit/6739c4be5bb56c065e1ad7dc50068b702033ecb3)
- Add ConnectX-8 device ID support for MLX5 PMD.
  ↳ No PR: [b5544aa](https://github.com/DPDK/dpdk/commit/b5544aa65dc4f5afce70ab70487cfa7b139bd65f)
- Add mailbox message support for inline IPsec configuration to support global inline profile assignment.
  ↳ No PR: [427d104](https://github.com/DPDK/dpdk/commit/427d10437175cff8c8c7c3b1e1d068d794514935)
- Added NPC action2 configuration support for IPsec rules, expanded related data structures and adjusted channel masks.
  ↳ No PR: [6f85e39](https://github.com/DPDK/dpdk/commit/6f85e39f72c377e0110239bf4ec1f016dbf7de2f)
- Added inline device statistics reset function.
  ↳ No PR: [839d753](https://github.com/DPDK/dpdk/commit/839d753a9b3fa3e4fcfaef493ad559d73fda5ad7)
- Optimized MTU setting operation, added port attribute setting function to support various offload flags and statistical updates.
  ↳ No PR: [74afaaf](https://github.com/DPDK/dpdk/commit/74afaaf6de5a0e70db806ac8715014f636b361e6)
- Added unified FDB capability query in the mlx5 driver, supporting three subfields: FDB_RX, FDB_TX and FDB_UNIFIED, and supporting FDB Rx jump, allowing the flow to jump from FDB Tx to FDB Rx; when supporting the JUMP_FDB_RX action, RSS is allowed to be used in FDB Rx rules.
  ↳ No PR: [878d354](https://github.com/DPDK/dpdk/commit/878d354ac5b801aa030039d272476d673f48be22), [ac687bb](https://github.com/DPDK/dpdk/commit/ac687bb002c998ba8abb3068f44c7b801bc11404), [ec566b4](https://github.com/DPDK/dpdk/commit/ec566b4b09252d1bfdf6c803451a12b5a001ee16), [a8b5217](https://github.com/DPDK/dpdk/commit/a8b52174592b6a18eb44498bbed7d0449f409442), [794b9b3](https://github.com/DPDK/dpdk/commit/794b9b37922f0a35cb7e0ee861d2a0eadbc27680)
- Added basic statistical functions to the zxdh network device driver, including RSS hash configuration, VQM statistics, NP statistics and statistical updates of the sending and receiving paths.
  ↳ No PR: [0b794f6](https://github.com/DPDK/dpdk/commit/0b794f66610eac546c74b529a525812b9230dc80)
- Added initial color configuration support for the meter_mark action in the indirect flow action list, allowing the init_color value to be set via the conf parameter.
  ↳ No PR: [ab42ea9](https://github.com/DPDK/dpdk/commit/ab42ea9082bc75ecf78fd10e43141eb8f6f903ff)
- Added opcode and event structure definitions for firmware temperature events for E610 network cards.
  ↳ No PR: [05eb929](https://github.com/DPDK/dpdk/commit/05eb9293dec960d11a7ff56f966baa8b952df555)
- Added two new PCI device IDs to the idxd driver to support future hardware releases.
  ↳ No PR: [fedffb1](https://github.com/DPDK/dpdk/commit/fedffb112f987f096a03549badc68d7bcbd6bc64)
- Removed the deprecated asynchronous event notification from the device, leaving only the supported event handling mechanism.
  ↳ No PR: [5b98a1e](https://github.com/DPDK/dpdk/commit/5b98a1ed1656a12eeff9d48e1a14c6a34bf411fe)
- Added the implementation of obtaining receive queue and send queue information for the zxdh network card driver.
  ↳ No PR: [fa0b975](https://github.com/DPDK/dpdk/commit/fa0b97513894809334a8ecdac84336a68842faca)
- Renamed clock register header file and added missing SPDX license tag.
  ↳ No PR: [5c681f1](https://github.com/DPDK/dpdk/commit/5c681f13c847f977390aabd9c04f6fc485f67ad4)
- Removed variable-length arrays (VLA) in dynamic polynomial calculations in favor of fixed-size standard C arrays, and updated degree bounds checks.
  ↳ No PR: [31ec5ca](https://github.com/DPDK/dpdk/commit/31ec5caa7bb42f9f72528e658be086ecdafb0375)
- Use rte_net_get_ptype() in testpmd instead of manually parsing packets, and support TSO for IPv6 extension headers.
  ↳ No PR: [76730c7](https://github.com/DPDK/dpdk/commit/76730c7b9b5a35d1a74d45a08153a03bdb1b26f8)
- Improved multicast address list configuration, returning -ENOSPC when there is insufficient space and not refreshing the existing list, and extracting the refresh logic into a separate function.
  ↳ No PR: [6a7f442](https://github.com/DPDK/dpdk/commit/6a7f44217595c7a5a26bdbb7fd2047db10c61af8)

### bug fixes
- Fixed the problem that the link status of the representor port is not switched correctly according to the representee status: the link status is set to up when the representee starts, and is set to down when it stops.
  ↳ No PR: [4a3a25b](https://github.com/DPDK/dpdk/commit/4a3a25bb6893bfbbde8a779b19634329bd50656d)
- Fixed the action data memory leak in the mlx5 non-template API, and separated the logic of action data release and DR action destruction.
  ↳ No PR: [d68bcfb](https://github.com/DPDK/dpdk/commit/d68bcfb6da221ee114835db8c2ab9449d277590f)
- Fixed the issue where the ring address was not cleared when the vhost obtained the vring base, causing the device to be incorrectly ready after the virtual machine was restarted.
  ↳ No PR: [1846fe7](https://github.com/DPDK/dpdk/commit/1846fe767f00a9d0dade333e7838f81e6721b694)
- Fixed the issue of repeatedly releasing the queue in the virtio crypto driver, releasing the post-empty queue pointer and removing redundant control queue release calls.
  ↳ No PR: [89241ab](https://github.com/DPDK/dpdk/commit/89241aba832c044a9efb99329cfaa9faff8a6c4e)
- Fix implicit conversion of 32-bit left shift to 64-bit in cryptodev, use RTE_BIT64 macro instead to avoid MSVC warnings.
  ↳ No PR: [fbf5828](https://github.com/DPDK/dpdk/commit/fbf5828f1965dccafddb872a0e5a715370c0aa86)
- Fixed a segmentation fault in the virtio network card Rx path caused by the checksum start position exceeding the message length.
  ↳ No PR: [4dc4e33](https://github.com/DPDK/dpdk/commit/4dc4e33ffa108e945fc8a1e2bbc7819791faa61e)
- Fixed unnecessary context cleanup in the CMAC authentication function to avoid subsequent call failures.
  ↳ No PR: [0241aeb](https://github.com/DPDK/dpdk/commit/0241aebfa3bdc53fb36972fb116298adbdbd3957)
- Fix cryptodev and eventdev IDs in wrong order in ipsec-secgw example.
  ↳ No PR: [c7b38c6](https://github.com/DPDK/dpdk/commit/c7b38c687d920000aef08659465e07106caa22c5)
- Fix the integer overflow problem of the alloc_link_pbl function in the net/bnxt driver, and avoid overflow by converting the multiplication operand to uint64_t type.
  ↳ No PR: [1cde8c8](https://github.com/DPDK/dpdk/commit/1cde8c8f1fb0dd8a6d437d6cd60daa91cf117e86)
- Fixed an integer underflow problem that may be caused by block index calculation in the cfa_mm_open function.
  ↳ No PR: [a966ec6](https://github.com/DPDK/dpdk/commit/a966ec66a2b14bc91cdd9a9968b4d0c5021139cd)
- Fixed the problem of uninitialized variables in two functions in the bnxt driver to avoid errors reported by Coverity scan.
  ↳ No PR: [7ef8b9a](https://github.com/DPDK/dpdk/commit/7ef8b9a8a16bcc3574d4c69a29ee2039e3778045)
- Fixed the dead code problem during feature checking in the bnxt driver, and changed the conditional judgment to else if to avoid logical conflicts.
  ↳ No PR: [c4ec78e](https://github.com/DPDK/dpdk/commit/c4ec78ee3abe2b1794b862419d634bef999baaf4)
- Add support for the E610 device type in the ixgbe stream engine, and fix the problem that it cannot use the FDIR function.
  ↳ No PR: [4d34945](https://github.com/DPDK/dpdk/commit/4d349458a18970730c6b2cda1be362042344b1c7)
- Fixed an issue where the mlx5 driver could access unallocated mbufs when polling CQEs, by limiting the processing batch to no more than the number of replenished mbufs.
  ↳ No PR: [73f7ae1](https://github.com/DPDK/dpdk/commit/73f7ae1d721aa5c388123db11827937205985999)
- Fixed variadic macro definitions in multiple applications to use standard C99 syntax to eliminate MSVC compilation warnings.
  ↳ No PR: [f7c9651](https://github.com/DPDK/dpdk/commit/f7c9651c830e4a54c81b0357fca768787d3d6402)
- Fixed the issue where the net/ena driver does not set the default LLQ policy, and ensures that LLQ is correctly enabled when the user does not specify it through devarg.
  ↳ No PR: [c4f16ab](https://github.com/DPDK/dpdk/commit/c4f16ab009ad53446157c6fcde85435b1ca8c780)
- Removed the invalid reset operation of the Tx preparation function pointer in the iavf driver, and fixed the Tx path selection problem caused by the pointer not being reassigned after being left blank.
  ↳ No PR: [41be96c](https://github.com/DPDK/dpdk/commit/41be96c907607bc709654f71901913f1534264f8)
- Fix VF link speed issue: Correctly update rte_eth_device and notify the firmware when the port link status changes, and add speed notification under multi-PF firmware for the physical representor port.
  ↳ No PR: [c43d2aa](https://github.com/DPDK/dpdk/commit/c43d2aab426bdc6e22142b4c5667d6d1634248de)
- Fixed the initialization of bnxt driver Rx and Tx burst handler. It is no longer set to static mode by default, but the correct handler function is dynamically selected through function call.
  ↳ No PR: [daff117](https://github.com/DPDK/dpdk/commit/daff117275e54a14bc840f1e0dd1f46c5a785066)
- Fixed undefined behavior caused by 32-bit integer left shift in bnx2x driver, use RTE_BIT32 macro to define interrupt and error flags instead.
  ↳ No PR: [c3ffa04](https://github.com/DPDK/dpdk/commit/c3ffa0426a9a8351ae4ba4a15a72b6022376ed00)
- Fixed the problem of pdump statistics not being cleared at the beginning of each capture to avoid counting accumulation when dumpcap is called multiple times.
  ↳ No PR: [b8392fa](https://github.com/DPDK/dpdk/commit/b8392fa204ed46b580d61e7621948f1b187c9f98)
- Fixed the crash problem in the bnxt driver when the representative port is remounted, and modified the cleanup logic to correctly release the ethdev of all sub-representative ports.
  ↳ No PR: [fca6cf6](https://github.com/DPDK/dpdk/commit/fca6cf68bbcf9b84e4388239031fb168a6624375)
- Fixed an issue where fragmented packet types were not correctly matched when L2/L3 masks were specified at the same time.
  ↳ No PR: [5782bb1](https://github.com/DPDK/dpdk/commit/5782bb1a5902a498176cb2fd0903d7a97be1b01a)
- Fix GSO size validity check in vhost to prevent errors from being raised when gso_size is 0.
  ↳ No PR: [7023f3e](https://github.com/DPDK/dpdk/commit/7023f3e532787eec7be674efb7a4aa54f1626b6c)
- Fixed an error caused by the introduction of the lcore variable when obtaining service idle call and error call statistics.
  ↳ No PR: [1ecb19e](https://github.com/DPDK/dpdk/commit/1ecb19eb4f44f984f15068834ef0c530f24ae697)
- Add descriptor chain length check in the vhost asynchronous packed ring dequeue path to prevent the problem of no data packet when the length is smaller than the Virtio-net header.
  ↳ No PR: [e31b57e](https://github.com/DPDK/dpdk/commit/e31b57e732d52f3cd8c707824f79fef8c117df95)
- Fixed Netlink socket leak problem: close the corresponding socket file descriptor when unloading the shared interrupt handler.
  ↳ No PR: [556a5f4](https://github.com/DPDK/dpdk/commit/556a5f4ccd452d9281c3476b120d1306e0093e01)
- Fixed the problem of incorrect mbuf release when the quick release offload is not set in the simple Tx path of the hns3 driver. Use rte_pktmbuf_free_seg() to release the mbuf instead.
  ↳ No PR: [d78c76d](https://github.com/DPDK/dpdk/commit/d78c76dbeffbd2994d77236c403281b34612e024)
- Removed the printing of VF's PVID information in the hns3 driver to avoid misunderstandings caused by inconsistent PVID status obtained by kernels on different platforms.
  ↳ No PR: [3c805c1](https://github.com/DPDK/dpdk/commit/3c805c1ebe02248bb0c2ba944046c2e3354b0c11)
- Fixed the issue where the length field of the unused memory segment list was not reset when releasing it, to avoid subsequent memory being misjudged as DPDK memory and being released incorrectly.
  ↳ No PR: [b974cbb](https://github.com/DPDK/dpdk/commit/b974cbbbef6e1036e7ed7d19fefb7ef8cda0e4a1)
- Fixed the problem of incorrectly closing the encryption device when the secondary process exits. Instead, the device shutdown operation is only performed in the main process.
  ↳ No PR: [c87c8fb](https://github.com/DPDK/dpdk/commit/c87c8fba192a9e24b5b3c37af0625f977874aadf)
- Fixed the problem of using the number of queue pairs in the device data instead of the maximum number of data queues when iterating the data queue.
  ↳ No PR: [e27ff6e](https://github.com/DPDK/dpdk/commit/e27ff6e63a8d6202149d5b458ad3d78711806dfc)
- Fixed the issue where the crypto/virtio driver returned fixed error code -1 when session configuration failed, and changed to return the correct error code.
  ↳ No PR: [d439ea4](https://github.com/DPDK/dpdk/commit/d439ea4ffb0b2f0f41b1ba3c8bc85c4a36e60625)
- Change the QPL allocation method of the RX queue from memzone to malloc to avoid allocation failure due to insufficient continuous IOVA memory; the TX queue still uses memzone.
  ↳ No PR: [a71168a](https://github.com/DPDK/dpdk/commit/a71168a775e658ac7e9cc839f53d25953d45bed9)
- Fix IPv4 matching fragment: correct target IP address mask, supplement missing queue action in action template, and replace misused rte_flow_item_tcp with correct rte_flow_item_ipv4.
  ↳ No PR: [5fa2591](https://github.com/DPDK/dpdk/commit/5fa25916f1ab47c82310264449a6d67dbb15ca4d)
- Fixed the issue where the ixgbe_get_fw_tsam_mode function returned an incorrect integer value when it was not implemented, and returned false instead.
  ↳ No PR: [0699ce4](https://github.com/DPDK/dpdk/commit/0699ce484da324b60572a906cf7d013394f074e2)
- Exclude auto-negotiation of 2.5G and 5G link speeds for E610 devices to avoid compatibility issues with some switches while retaining support for E610 2.5G SKU devices.
  ↳ No PR: [c38b427](https://github.com/DPDK/dpdk/commit/c38b4274255703a48d0177c013ee95afb4bde910)
- Fixed a bug in the ixgbe_aci_send_cmd function where the original command buffer was not copied when retrying the AQ command.
  ↳ No PR: [3723979](https://github.com/DPDK/dpdk/commit/37239792b0d67fedc011db54ffa32b022a391787)
- Fixed an issue in the SRAM manager allocation status indication that incorrectly assigned false to a pointer instead of the Boolean value pointed to by the pointer.
  ↳ No PR: [8531f9b](https://github.com/DPDK/dpdk/commit/8531f9ba0062032454121f4959cd3d495cd4147e)
- Fixed the memory leak caused by the payload mbuf allocation failure in the buffer splitting scenario in the ice driver scalar receiving path, and ensured that the allocated header mbuf was released correctly.
  ↳ No PR: [07cbd0b](https://github.com/DPDK/dpdk/commit/07cbd0b43ce4af9d628c8ad751789934d0a8c4a7)
- Fixed the issue of missing event weight processing in the DLB2 driver SSE code path, making it consistent with the AVX512 path.
  ↳ No PR: [96357d5](https://github.com/DPDK/dpdk/commit/96357d5afefc7f4be8f5735f0d5ea011e68d24f2)
- Fixed a logic error when the NFP driver checks multiple PFs from NSP, changed the function return type to integer and added an output parameter to correctly pass the flag.
  ↳ No PR: [c19d389](https://github.com/DPDK/dpdk/commit/c19d389f5b553b0a9dddbb22882750c17a6fa577)
- Fixed a logical judgment error in NFP driver conntrack caused by assigning the negative return value of nfp_ct_offload_add to a Boolean variable.
  ↳ No PR: [f19ffdb](https://github.com/DPDK/dpdk/commit/f19ffdb1574cb0a9c9566b0b5c4098beb95ced49)
- Fixed the issue where the NFP driver does not set the NFP_NET_CFG_CTRL_MULTI_PF control flag in multi-PF firmware scenarios.
  ↳ No PR: [02c056a](https://github.com/DPDK/dpdk/commit/02c056aaac1ba1bd16658eef19cb78457d556041)
- Repair the NFP driver firmware loading priority logic, adjust the priority order of file system and flash loading, and ensure that the file system can correctly fall back to flash loading after the file system loading fails.
  ↳ No PR: [d7c07c8](https://github.com/DPDK/dpdk/commit/d7c07c8e29bea66622183e4279d881c20fafe375)
- Add a null pointer check before calling the rte_vhost_device_ops callback to avoid null pointer dereference problems caused by unregistered callbacks.
  ↳ No PR: [66be1a0](https://github.com/DPDK/dpdk/commit/66be1a05a480a0484b02c1a0194126763f4dbb99)
- Fixed a memory leak when creating the HWS flow counter action in the mlx5 driver, ensuring that mp_name is released correctly when initialization fails.
  ↳ No PR: [9e34fcc](https://github.com/DPDK/dpdk/commit/9e34fcc81c005a60c919c572ef83c10ebb0201af)
- Fixed bnxt driver automatically disabling TruFlow when compressed CQE mode is enabled to avoid exceptions.
  ↳ No PR: [abb2cb9](https://github.com/DPDK/dpdk/commit/abb2cb9b08ba7e0a83c9e8e64320c900f44c56e7)
- Fixed the crash problem of mlx5 driver when splitting using mark action in switch dev mode: fixed the problem of incorrect use of queue[0] index in hairpin RX queue check, and replaced the unsupported set tag action with modify field action.
  ↳ No PR: [51470cd](https://github.com/DPDK/dpdk/commit/51470cd861f952d79970972d8c3f1929ddc298f3)
- Fixed a memory leak caused by early return without releasing the non-template stream list when the mlx5 driver refreshes non-template streams.
  ↳ No PR: [716929b](https://github.com/DPDK/dpdk/commit/716929be9456b78875d0eb20bc54c13acf99efc0)
- Fixed the performance degradation problem of GRE stream matching in mlx5 driver in SWS mode, and adjusted the translation logic of GRE items to distinguish SWS and HWS processing.
  ↳ No PR: [05db99c](https://github.com/DPDK/dpdk/commit/05db99c117e36c0cd28cda8f558309efd20055da)
- Fixed ppc64le compilation error caused by missing volatile qualifiers and type aliases in the AltiVec receive path of the mlx5 driver.
  ↳ No PR: [9ab5a5f](https://github.com/DPDK/dpdk/commit/9ab5a5f30c4be9f12ddaf50aec3435986bc5a495)
- Fixed the issue where the default L3 type of the CNXK network card was incorrectly set to IPv6 in vector send processing, causing small packet SQ error interruption. Change the default L3 type to none, and correctly set the L3 type in TSO processing.
  ↳ No PR: [32c18e7](https://github.com/DPDK/dpdk/commit/32c18e7364e30a8e43cc7cc6709a7ce606fa285e)
- Fixed a crash caused by passing a value instead of a pointer in the AVX512 receiving function.
  ↳ No PR: [3a02a1c](https://github.com/DPDK/dpdk/commit/3a02a1c565c5aa7fe565aa58947413de005fee6f)
- Fix the receive data path of compressed CQE in bnxt driver scalar mode, and move the compressed CQE processing code out of the normal CQE branch.
  ↳ No PR: [73b05bb](https://github.com/DPDK/dpdk/commit/73b05bbc6dd2d21c59b6ec6f72d8ae88d6bead3d)
- Fixed the issue where af_packet PMD closes the socket when calling rte_eth_dev_stop(), causing the port to fail to restart, and moves the socket closing operation to eth_dev_close().
  ↳ No PR: [872e846](https://github.com/DPDK/dpdk/commit/872e846f6bb31afbdd508903380cf05a3d313a3a)
- Fixed the wrong path for systemd journal socket opening to avoid Coverity warnings caused by calling close(-1) when socket creation fails.
  ↳ No PR: [d0dbcae](https://github.com/DPDK/dpdk/commit/d0dbcae33d86514159b56e8d03c7f59536cbea9d)
- Fixed the printing error in the representor parsing log in the cpfl driver, and replaced the incorrect NULL variables in the log with the correct input parameters.
  ↳ No PR: [7501478](https://github.com/DPDK/dpdk/commit/7501478b95fc79b178fc525246482215a6018651)
- Fixed the array out-of-bounds problem when parsing the devargs layer, and changed the boundary check from greater than to greater than or equal to.
  ↳ No PR: [42f9149](https://github.com/DPDK/dpdk/commit/42f91490ebc97a816ea11ce9c995f455c169a77a)
- Fixed an error in clock ID comparison during message parsing in the PTP client example to avoid the problem of always returning true.
  ↳ No PR: [19630bd](https://github.com/DPDK/dpdk/commit/19630bd0d735badb06143086d4f1c50d726b7bad)
- Fixed the 64-bit type mask truncation problem in the net/hinic driver caused by using 32-bit integer literals for shift operations.
  ↳ No PR: [a357d5b](https://github.com/DPDK/dpdk/commit/a357d5b703253b5920aba808a24877386a22720e)
- Fixed an issue in the dpaa2_sec driver where the 64-bit bit mask caused shift truncation due to the use of int type constants.
  ↳ No PR: [013ddc8](https://github.com/DPDK/dpdk/commit/013ddc85bff5fdb85eb6006315ebdaa0c12eeece)
- Fixed an update error in the dpaa_sec driver caused by truncation of the 64-bit bitmask due to integer type.
  ↳ No PR: [7c18f57](https://github.com/DPDK/dpdk/commit/7c18f573c1f5368f70e6e956c4ba0c6f97b19cb1)
- Fixed the truncation problem in bitmask calculation in event/dpaa driver to ensure correct operation in 64-bit environment.
  ↳ No PR: [a82888e](https://github.com/DPDK/dpdk/commit/a82888ed6edc599f82263a1bd067a7edb7cceeee)
- Fixed an issue in the dpaa driver where the high 32 bits of the 64-bit bit mask were truncated due to the use of int type shifting.
  ↳ No PR: [8f64c18](https://github.com/DPDK/dpdk/commit/8f64c187ad8e4e0b953439b2ce92d8573721eda3)
- Fixed an issue in the dpaa2 driver where the shift result was truncated due to the use of int type for the 64-bit mask.
  ↳ No PR: [e4591c3](https://github.com/DPDK/dpdk/commit/e4591c38b50e23fc6ac6b73803e78d49142ecf57)
- Fixed the nested loop variable error in the LLDP update event handler function in the qede driver to avoid logic defects caused by using the same loop variable.
  ↳ No PR: [c8b3833](https://github.com/DPDK/dpdk/commit/c8b3833965dc84914e94776cadfc8fb48c34459b)
- Fixed the operator precedence error of socket ID check in l3fwd example to ensure that socketid is assigned correctly instead of being assigned a boolean value.
  ↳ No PR: [a7216f0](https://github.com/DPDK/dpdk/commit/a7216f081767c7259dd3fba5eda0ca7b0bcb4595)
- Fixed the order problem of null pointer checks in the roc_bphy_cgx_set_link_mode function, advancing the null value check of mode to the beginning of the function to avoid dereferencing the null pointer.
  ↳ No PR: [1bab028](https://github.com/DPDK/dpdk/commit/1bab0289c6a58c3847ffbde2718b73a9b988deca)
- Fixed the boundary conditions of index verification in the statistical function to prevent array out-of-bounds access.
  ↳ No PR: [a680168](https://github.com/DPDK/dpdk/commit/a68016802dc4db7fb0a93523815ec234bb244a6c)
- Fixed the defect of not checking the return value when creating a thread. If the creation fails, an error will be recorded and returned.
  ↳ No PR: [8465e44](https://github.com/DPDK/dpdk/commit/8465e44694238340f52645473f19a7025b0cdc16)
- Fixed the problem of unchecked memcmp return value and resolved the BAD_COMPARE defect reported by Coverity.
  ↳ No PR: [64ae255](https://github.com/DPDK/dpdk/commit/64ae2553d52205b80963e91487c951d37f372f90)
- Fixed the memory leak caused by the pointer not being updated when realloc succeeds in flow_configure_profile_inline, and corrected a function call name.
  ↳ No PR: [64777cd](https://github.com/DPDK/dpdk/commit/64777cdd285753783b26518469a7172eb373beb4)
- Fixed the out-of-bounds array index problem in the clear_pdrv function, and changed the out-of-bounds check condition from greater than to greater than or equal to.
  ↳ No PR: [f5c983a](https://github.com/DPDK/dpdk/commit/f5c983ac65e3afcce0eb38554e1b3df9f02e047e)
- Fixed the use-after-free problem caused by not clearing eth_base after releasing the port in the net/ntnic driver.
  ↳ No PR: [e10b91b](https://github.com/DPDK/dpdk/commit/e10b91bf9fea4698d0bbdbf74717d7cd1e12acb5)
- Fixed a resource leak caused by p_fpga_mgr not being released when FPGA initialization failed.
  ↳ No PR: [7186a34](https://github.com/DPDK/dpdk/commit/7186a34bd75277f2ab49ea1fa0a2cffa6af3de5f)
- Fixed a potential overflow problem caused by integer left shift when assigning modify_field_use_flag.
  ↳ No PR: [a185f64](https://github.com/DPDK/dpdk/commit/a185f64986798db2b9740ab5826c44ee87446058)
- Fixed an overflow problem that may occur in bit shift operations, and limited the maximum shift value.
  ↳ No PR: [d68a54e](https://github.com/DPDK/dpdk/commit/d68a54e9ab545d945ea197789436b7a41fd2ddf9)
- Fixed the problem that the return value type of the dbs_qsize_log2 function does not match the variable size, and adjusted the return type and internal variables from uint16_t/uint32_t to uint8_t.
  ↳ No PR: [1188c29](https://github.com/DPDK/dpdk/commit/1188c29e49d6bf3eb8a87b7b4a24f63000422b51)
- Fixed an integer overflow that may occur when allocating hardware queues in the ntnic driver, explicitly convert buf_size and num_descr to uint64_t before multiplying them.
  ↳ No PR: [83ce5aa](https://github.com/DPDK/dpdk/commit/83ce5aa6f1a3a56b267126f0dfb4d5977fc80fcf)
- Fixed array bounds check to prevent word_off from out-of-bounds access.
  ↳ No PR: [26befdd](https://github.com/DPDK/dpdk/commit/26befddb2d81053bd88e1dcdb5882c4513ea78ed)
- Fixed memory leak in ntnic driver, freeing kvlist before error is returned.
  ↳ No PR: [c41a6f0](https://github.com/DPDK/dpdk/commit/c41a6f0636783cde5e498767d3d49d6b844a0a5c)
- Fixed unnecessary null pointer check in xstats retrieval, ensuring port load statistics values are always valid.
  ↳ No PR: [5ed5a36](https://github.com/DPDK/dpdk/commit/5ed5a36cd0e2a47da73f684d3e7ce5a3f69ecfd0)
- Fixed age timeout to FPGA internal time unit conversion bug, and updated timeout decoding functions to support longer timeout ranges.
  ↳ No PR: [b482ab7](https://github.com/DPDK/dpdk/commit/b482ab75dfd54b2d562b80e90a8e0166ba8c6350)
- Added range check and modification type check not supported by group 0 for action modify, and modified related functions to handle error return when verification fails.
  ↳ No PR: [f3bdad5](https://github.com/DPDK/dpdk/commit/f3bdad57f275be1b8b76a130cf9c53cce8620716)
- Fixed an issue with unprocessed IPv4 packets in GRO, ensuring that the starting position and remaining number of unprocessed packets are correctly passed when refreshing the VXLAN TCP table.
  ↳ No PR: [5c762a5](https://github.com/DPDK/dpdk/commit/5c762a58c3fa81e232a5cba8087577be1a593c33)
- Fixed the deadlock problem caused by not releasing the semaphore when writing the register in the i225 network card driver failed, ensuring that the semaphore is always released.
  ↳ No PR: [f05363d](https://github.com/DPDK/dpdk/commit/f05363dceac78694638f86a8af1acd173ca9e3e0)
- Fixed the problem of being stuck in an infinite loop due to the inability to obtain the hardware semaphore when releasing software/firmware synchronization resources in the igc driver. Instead, the error is logged and returned directly.
  ↳ No PR: [532e495](https://github.com/DPDK/dpdk/commit/532e495e4a20cf09e1f42d01bcbe782f7e2bb03f)
- Increased i225 PHY post-power-up delay time to 300 microseconds to comply with chip specifications.
  ↳ No PR: [a8a4acb](https://github.com/DPDK/dpdk/commit/a8a4acb46fa6bbe0a669b4eca0f73f112a7646ac)
- Fixed bit offset errors and data type issues in MAC address hash calculation in the igc driver to avoid hash value errors and overflows.
  ↳ No PR: [bccccac](https://github.com/DPDK/dpdk/commit/bccccacfb6f6f2e84a24c6733c7e3d4af05f73b5), [cad5c51](https://github.com/DPDK/dpdk/commit/cad5c51ec3a0e965d6d4bb98166890499597f23a)
- Fixed the semaphore timeout value in the e1000 and igc network card drivers, correcting the waiting time from the maximum 1.5 seconds to 100 milliseconds in line with the datasheet requirements to avoid triggering DPC timeout.
  ↳ No PR: [c8bcaf0](https://github.com/DPDK/dpdk/commit/c8bcaf0f2a02995b447c121e860fd550b9c55114), [7caabb9](https://github.com/DPDK/dpdk/commit/7caabb9834bc9596190c03279eae8980b1c24800)
- Fixed bit offset errors and data type issues in MAC address hash calculation in e1000 and igc network card drivers to ensure that hash values are generated correctly.
  ↳ No PR: [1749e66](https://github.com/DPDK/dpdk/commit/1749e662f68ba6571ed81cd264cffd1107abc307), [458734a](https://github.com/DPDK/dpdk/commit/458734aaac3225d98aeee5f4c45b3d39a7d82949)
- Fixed power state switching and clock gating issues for specific PHY and MAC types in the e1000 driver to avoid packet loss.
  ↳ No PR: [90f456c](https://github.com/DPDK/dpdk/commit/90f456cea0c274b967aac7ccdc1bc9bd159f2e45), [fcead8f](https://github.com/DPDK/dpdk/commit/fcead8f5512761f61f2973ae2e846af91c4cb3b2)
- Fixed hardware synchronization and PCIe configuration issues for ICH8 devices in the e1000 driver, removed invalid calls and optimized the code.
  ↳ No PR: [4600a09](https://github.com/DPDK/dpdk/commit/4600a098fd441787218b43f982ba328d47c1d93e), [d439b41](https://github.com/DPDK/dpdk/commit/d439b416e7b97399cb5202056dc273ad1b5c45e5)
- Fixed the read failure problem in the I225 network card PHY initialization, introduced the PHY ID read retry mechanism (up to 10 times, with an interval of 100 milliseconds), and corrected the call of the PCI-E master/slave disable function during the reset process.
  ↳ No PR: [1aea236](https://github.com/DPDK/dpdk/commit/1aea2367a3362251dbb51c30651a44734f8ba437)
- Improved error handling when matcher disconnects to avoid segfault caused by firmware failure.
  ↳ No PR: [d6de990](https://github.com/DPDK/dpdk/commit/d6de990d3159c88fa9a24072ea9a4eedae77f5f4)
- Fixed the problem that the L4 protocol type of ConnectX-8 network card was not correctly recognized in IP fragmentation, and updated the hardware packet type translation table.
  ↳ No PR: [ed99352](https://github.com/DPDK/dpdk/commit/ed9935258f5c3cbb07b2828b6072dec9be8c3891)
- Added a retry mechanism for copper port initialization to solve the problem of driver initialization failure due to unfinished asynchronous tasks in earlier firmware versions.
  ↳ No PR: [763546c](https://github.com/DPDK/dpdk/commit/763546c33ea9600e76790c470d2921808068eb3d)
- Fixed an issue where the hns3 driver may timeout during reset, adjusting the reset command timeout to 100 milliseconds by dynamically setting the timeout based on the command type.
  ↳ No PR: [9f7c28c](https://github.com/DPDK/dpdk/commit/9f7c28c5e98062576dfbf555cd5ede7e33d6624b)
- Fixed the problem of inconsistent device names when registering PCI devices. Now the device names use the parsed canonical PCI address.
  ↳ No PR: [bd78676](https://github.com/DPDK/dpdk/commit/bd786765996fc2654770049043021ea618fc23f0)
- Fixed the scanning problem of multiple Ethernet devices under PCI devices in the netvsc driver, which will now traverse all network devices instead of just processing the first one.
  ↳ No PR: [7690b9c](https://github.com/DPDK/dpdk/commit/7690b9ca7b0e5f54ffa7e94957e3fc04bcdc92e4)
- Fixed netvsc driver making sure all Ethernet devices are turned off before removing RTE devices during hot removal.
  ↳ No PR: [1ec0995](https://github.com/DPDK/dpdk/commit/1ec0995e173da14f2871ee19326f275f94f412c4)
- In the netvsc driver, an error log is recorded when switching data paths fails to facilitate troubleshooting.
  ↳ No PR: [b71edf4](https://github.com/DPDK/dpdk/commit/b71edf4bf34cbd64a875df1883e9fa431e6d1975)
- Fixed the problem of segfault caused by empty driver operation selection when creating an empty stream list, and added the corresponding empty operation implementation.
  ↳ No PR: [c30b356](https://github.com/DPDK/dpdk/commit/c30b356a4d48542fe99c47aa470afc8cd1ced9f5)
- Fixed asymmetric operation status code, returning error status when known conditions are not met.
  ↳ No PR: [a5c2058](https://github.com/DPDK/dpdk/commit/a5c2058e22edd150ace5b23076fde7f9e722755d)
- Fixed an issue where the width and offset parameters in the Ethernet device register information request were not passed correctly.
  ↳ No PR: [b14a65c](https://github.com/DPDK/dpdk/commit/b14a65cdd0fa4b8dddffcda1e870e4b97ec53979)
- Fixed the problem of error information being overwritten during flow action translation, introduced local error variables, and restructured the error handling logic of SEND_TO_KERNEL, AGE and COUNT actions.
  ↳ No PR: [494da70](https://github.com/DPDK/dpdk/commit/494da70e289c6a603185c890111f95568eb1fd63)
- Fixed out-of-bound reference and segfault issues in testpmd caused by missing port ID verification, including the issue where the DCB configuration command caused a segfault when an invalid port number was entered.
  ↳ No PR: [8f84702](https://github.com/DPDK/dpdk/commit/8f847023dd16cb6e5858756d7ec16c940ac6eee9), [d646e21](https://github.com/DPDK/dpdk/commit/d646e219b34ffc4d531f3703fc317e7cff9a25ae)
- Fixed race condition when device is removed in mana driver, moved multi-process usage count from shared data to local data.
  ↳ No PR: [57aa3ec](https://github.com/DPDK/dpdk/commit/57aa3ec91ecf13ab2f11e4dc0dc74c50a2afa0cc)
- Rolled back the modification of the untrusted loop boundary in VLAN processing to fix the problem of abnormal VLAN processing.
  ↳ No PR: [af5fcdd](https://github.com/DPDK/dpdk/commit/af5fcdd33c02b962f5a3b5b70a2f96c14361111b)
- Fixed the ACL filter cleaning logic so that it is no longer limited to DCF mode, and PF can also be cleaned normally.
  ↳ No PR: [393708a](https://github.com/DPDK/dpdk/commit/393708a9ba52b3454d6ad8ec3a37aabab38310c9)
- Fixed the problem of incorrect timing of calling the mbuf cleanup function in the ice driver. The selection of Rx and Tx functions is advanced before the queue is started to avoid memory leaks and segmentation faults caused by incorrect timing of setting flag bits.
  ↳ No PR: [3c79a3d](https://github.com/DPDK/dpdk/commit/3c79a3d91d9d548b8fa1eba60960b4fee47511d5)
- Added error checking for port enable failure in the xsc network card startup process.
  ↳ No PR: [d531311](https://github.com/DPDK/dpdk/commit/d531311e57bc6c8022198f4258ef45c593552e41)
- Fixed multiple null pointer dereferences, logic errors and initialization issues in the xsc driver, including null pointer operations after memory allocation failure, repeated calculation of data length in mbuf initialization, memcmp comparison logic errors, etc.
  ↳ No PR: [86ca998](https://github.com/DPDK/dpdk/commit/86ca9984d925552bc7519dbc9c091d3b0af2582d), [55b45ed](https://github.com/DPDK/dpdk/commit/55b45edf3097baca14384dfa42e4f4b0ab1b9cc0), [2fedd70](https://github.com/DPDK/dpdk/commit/2fedd7009809010c46ae6e37add66ac6539ef702), [42fb313](https://github.com/DPDK/dpdk/commit/42fb3131b9041b950887168d5ecfb0042caacd32), [b6c9b19](https://github.com/DPDK/dpdk/commit/b6c9b1948efe8ff9bf23000b8ab10bb8999508c9), [3d57851](https://github.com/DPDK/dpdk/commit/3d57851720d44b178a96d1a4b7bbb79a53b1c69c)
- Fixed inbound IPsec SA configuration error in cnxk driver, ensuring L3 header writeback is set correctly on errors in inline IPsec.
  ↳ No PR: [26e8a2a](https://github.com/DPDK/dpdk/commit/26e8a2ac205749441971f81e5de0eff57e94ce90)
- Fixed the judgment logic of WOL and NCSI capabilities in the ngbe driver, changing the inclusive matching of the subsystem ID to an exact match to avoid misjudgment causing the PHY configuration to be skipped and causing link failure.
  ↳ No PR: [7e77960](https://github.com/DPDK/dpdk/commit/7e77960c402cda75534b4bfb32e1056e1b3fa5c8)
- Fixed the problem of inaccurate results caused by concurrent calculation of the number of packets sent and received by multiple queues in nfp driver representative port statistics. Instead, the data of each queue is summarized when obtaining statistics.
  ↳ No PR: [87a5cc7](https://github.com/DPDK/dpdk/commit/87a5cc7c3e829b8a14fe9cb6db7feb0161c10861)
- Fixed error checking in mlx5 driver when queue counter allocation fails, now by checking the firmware syndrome code to determine whether the maximum queue counter limit has been reached.
  ↳ No PR: [7c88219](https://github.com/DPDK/dpdk/commit/7c882196e4d45e7ac130dc98b9a64ea065a49f6f)
- Fixed the problem that the show port dcb_tc command in testpmd only displays the TC quantity mapping, and instead displays the TC mapping of all priorities.
  ↳ No PR: [164d7ac](https://github.com/DPDK/dpdk/commit/164d7ac277bba10b27dd96821536e6b4a71cfebf)
- Fixed SM3 hash algorithm state size setting error in QAT PMD.
  ↳ No PR: [873577f](https://github.com/DPDK/dpdk/commit/873577fac7e4bce6d6ae9bacfae8eebd08acfce7)
- Fixed an issue in the default miss table jump validation that allowed jumps between FDB_UNIFIED and FDB_RX/FDB_TX types.
  ↳ No PR: [c3b2da4](https://github.com/DPDK/dpdk/commit/c3b2da4e1c17d92453e0ffcbafe6565ab4d5d32f)
- Fixed two errors in the nfp PF initialization failure processing logic, and improved the resource cleanup of wrong paths.
  ↳ No PR: [1992e3f](https://github.com/DPDK/dpdk/commit/1992e3ffac00c61e41ba13d8c4808ced48c9e8da)
- Fixed the problem of premature flipping of epoch bits in the bnxt network card driver vector path, improved wraparound recognition and correct calculation of epoch bits.
  ↳ No PR: [12f77a5](https://github.com/DPDK/dpdk/commit/12f77a5f69ee35cf8dae5801c1ed8d4ef2423f97)
- Added IPv4 and UDP checksum offload flags in txonly forwarding mode, fixed lack of corresponding mbuf offload flags when supported by hardware.
  ↳ No PR: [4a3fd8d](https://github.com/DPDK/dpdk/commit/4a3fd8d2a90f2beac4ce5302e1aa4fdbd23c28b0)
- Fixed assertion failure due to mishandling of shared Rx queue when hairpin queue is released.
  ↳ No PR: [6886b5f](https://github.com/DPDK/dpdk/commit/6886b5f39d66770fb7e233fa1c8fc74ed1935116)
- Fixed the issue of incorrect processing of LACP packets in isolation mode, by adjusting the position of the isolation mode check to ensure its correct execution.
  ↳ No PR: [d15d74f](https://github.com/DPDK/dpdk/commit/d15d74fc4b22cf7f09194f7d4de8d8ee03ca63a6)
- Fixed the crash caused by not setting ethdev_port_id when using the represented port item in the non-template API, added a null pointer check and used the switch manager ID by default.
  ↳ No PR: [1de93ca](https://github.com/DPDK/dpdk/commit/1de93ca6aee6acb785c8080f84da26b09835af0f)
- Fixed a crash that may occur when setting VLAN VID in non-template mode, and updated the error handling of related functions.
  ↳ No PR: [5fd4de3](https://github.com/DPDK/dpdk/commit/5fd4de3aef4cec5ca3395139135b1c58d43d5a9c)
- Fixed GTP flag matching, now supports all v_pt_rsv_flags bits, not just extended flags.
  ↳ No PR: [a31da10](https://github.com/DPDK/dpdk/commit/a31da10717be6a79877621e94eeb003f547c5f88)
- Fixed the thread safety check of vhost crypto: changed the function parameters from vhost_crypto_data_req to explicit virtio_net and vhost_virtqueue, and updated the thread safety attribute macro; also added asymmetric encryption session creation and related functions, and added the --asym command line option to the example to support asymmetric operations.
  ↳ No PR: [88c73b5](https://github.com/DPDK/dpdk/commit/88c73b5434e6555e50caf516f599bca6f2c5d018), [6017ce6](https://github.com/DPDK/dpdk/commit/6017ce62898085ee1a66520bb3deff5283a5f9d3)
- Fixed the memory error caused by the worker thread trying to obtain the encryption operation when the virtio ring is not initialized, added a check on the vring initialization status and adjusted the lock acquisition method.
  ↳ No PR: [b03cb9c](https://github.com/DPDK/dpdk/commit/b03cb9c87a61054ce34b1c19c89170c80d75d27d)
- Fixed the issue where verification failed when non-template flows were created on HWS but could still be created successfully. Rule verification was added during the flow creation process, and the method of obtaining the match flag was adjusted. At the same time, a dedicated verification function was added for non-template flow rules based on HWS.
  ↳ No PR: [f8ce702](https://github.com/DPDK/dpdk/commit/f8ce702cd05f555ab8a52e6d827f096d80fbb825), [5b0b674](https://github.com/DPDK/dpdk/commit/5b0b6742d222299f3369eeeaa484639ef0134db3)
- Fixed the problem that the actual group ID was not set correctly when converting flow actions in non-template API to avoid misuse of root table actions.
  ↳ No PR: [39c93b8](https://github.com/DPDK/dpdk/commit/39c93b85866bad6c43a8a6d8bb3f81bfc0d2ff94)
- Fixed the problem of non-template API failing to match GENEVE options on HWS, added a GENEVE option parser, and updated related documentation.
  ↳ No PR: [fdca628](https://github.com/DPDK/dpdk/commit/fdca628a3e22080a27ff5cd166b2e6537f3cf464)
- Fixed the thread safety issue in vhost/crypto caused by repeated lock acquisition by the same thread, changed the lock reference from vc_req->vq to use vq directly, and split the session cache ID to distinguish symmetric and asymmetric sessions.
  ↳ No PR: [7b2ab3b](https://github.com/DPDK/dpdk/commit/7b2ab3b1731e928d0a7ca66fa1d1e7448bf076a1)
- Fixed VRB2 variant having incomplete cleanup when queue setup failed, ensuring queue index is decremented correctly.
  ↳ No PR: [dd81690](https://github.com/DPDK/dpdk/commit/dd81690238585a1985767a8473ac452a048643ea)
- Fixed the problem of incorrect conversion of table types when creating root type actions, and added target conversion for non-root FDB actions.
  ↳ No PR: [16ac8f9](https://github.com/DPDK/dpdk/commit/16ac8f980042da5c88860f1931789f3060caa38c)
- Added return value checking for malloc calls in multiple functions to avoid null pointer dereferences.
  ↳ No PR: [336893b](https://github.com/DPDK/dpdk/commit/336893b71320acb0fdb06682fb82a4c1c28788c8)
- Fixed a crash caused by the interrupt handler function accessing an invalid pointer when the application exits on FreeBSD, and added a null pointer check.
  ↳ No PR: [44a86bc](https://github.com/DPDK/dpdk/commit/44a86bcf2447d7d914d7195448285aa82eaedcba)
- Fixed the IP-in-IP tunnel verification logic in MLX5 PMD, and fixed the problem that the inner IP protocol under VXLAN encapsulation was incorrectly recognized as the same layer, causing flow verification to fail.
  ↳ No PR: [3d80d35](https://github.com/DPDK/dpdk/commit/3d80d35b118ecfb650e51fabafc682ea8a3adb8f)
- Fixed the issue of insufficient memory allocation due to string terminators not being considered in QAT device parameter parsing.
  ↳ No PR: [b5f5617](https://github.com/DPDK/dpdk/commit/b5f561739d81ed248fee9c801db4cd84caffc5b2)
- Fixed the verification logic of mark flow action in FDB mode in mlx5 driver, and now supports both SWS and HWS modes.
  ↳ No PR: [3e83c48](https://github.com/DPDK/dpdk/commit/3e83c4821d57874b2677d7344bcc26f587ce5ba2)
- Enabled local loopback and source pruning flags in ice PF's VSI settings, fixed packet loss issue when using VRRP virtual MAC address.
  ↳ No PR: [6f866eb](https://github.com/DPDK/dpdk/commit/6f866eb93e796aaf226f66c689e4c4e1b2290c90)
- Fixed the NAT64 register selection problem: Check whether REG_C_6 is supported by the firmware during initialization. If there are insufficient registers, NAT64 actions will no longer be created.
  ↳ No PR: [f155351](https://github.com/DPDK/dpdk/commit/f15535128617db8c1e9cad4793e7daf0d698eef9)
- Fixed the problem of incorrect default protocol mask value when GRE matching on the root table. Changed the default protocol mask from 0xffff to 0 so that empty GRE matching no longer forces matching of the protocol field.
  ↳ No PR: [111bde2](https://github.com/DPDK/dpdk/commit/111bde25455114e1d4ad843e7b3a03c5ffd6eca5)
- Fixed the infinite loop problem in the checksum engine when processing VLAN and QinQ packets, and updated the get_ethertype_by_ptype function to correctly parse the VLAN header.
  ↳ No PR: [3e00b30](https://github.com/DPDK/dpdk/commit/3e00b30e9b208092f896672046a3ae39b878955b)
- Fixed the error handling problem reported by Coverity in the bnxt driver, and added return value checks in the ulp_mapper and ulp_rte_parser functions.
  ↳ No PR: [8eb0ce2](https://github.com/DPDK/dpdk/commit/8eb0ce22e04da7461ec89ef49ea495b9afca0bf0)
- Fixed the issue of repeated assignment of action templates in the flow_filtering example.
  ↳ No PR: [7d73fa4](https://github.com/DPDK/dpdk/commit/7d73fa47f4ef9223cf39303bb731f071435228be)
- Removed the duplicate status assignment of the sfc_repr_close function in the sfc driver and fixed the Coverity problem.
  ↳ No PR: [de87641](https://github.com/DPDK/dpdk/commit/de87641d5c004ef505d58d542a66d66f6a1cb2be)
- Fixed the MSVC compilation warning caused by the void function return value in the Intel network card driver.
  ↳ No PR: [c39e89b](https://github.com/DPDK/dpdk/commit/c39e89b467c510923295a73e5b76a6a44c72dd1b), [bc64580](https://github.com/DPDK/dpdk/commit/bc64580a631ee4ad67d7a2a9ae96a63e8d4a02b1)
- Fixed the file descriptor leak caused by fscanf failure in cnxk_gpio driver selftest.
  ↳ No PR: [67f0bea](https://github.com/DPDK/dpdk/commit/67f0beaf0f5bf2cf239219c737ed8d93aaaaa673)
- Fix the qede driver debugging status string array, add missing status descriptions and add static assertions to ensure consistency.
  ↳ No PR: [60c68da](https://github.com/DPDK/dpdk/commit/60c68da0392e31ea4c163e0be8f1236a00cd350c)
- Add null pointer check in ntnic driver to prevent potential null pointer dereference.
  ↳ No PR: [7ae6a53](https://github.com/DPDK/dpdk/commit/7ae6a5381a2d0f2e2ef4868d14e5e2fbc5c7347b), [18decec](https://github.com/DPDK/dpdk/commit/18decec49eb25f71eb8bf78572a1d2441c376818), [1008dfe](https://github.com/DPDK/dpdk/commit/1008dfebe9409f3b938b70fd351625c6a878ee82)
- Fixed an issue in the ntnic driver that may cause an infinite loop due to external modifications, replacing while with if.
  ↳ No PR: [36cd2cb](https://github.com/DPDK/dpdk/commit/36cd2cb0eea49813dd59ee1df2eb592e8ae5b6b4)
- Fixed multiple issues such as bitwise operation type mismatch, Shadow RAM writing return value, LTR calculation and unused variables in the igc driver.
  ↳ No PR: [bf51125](https://github.com/DPDK/dpdk/commit/bf51125b75b18a3a43439edb2c6e1f0b14793d51), [60dca8e](https://github.com/DPDK/dpdk/commit/60dca8e0f6b2d8526dc9dc8b54e59b5d68964e8e), [6a304bc](https://github.com/DPDK/dpdk/commit/6a304bc65269cfd86193663e9b94c73299b54d00), [ce11274](https://github.com/DPDK/dpdk/commit/ce11274c5c7188322cc141cdce8cd0680e76f79f), [c506cc8](https://github.com/DPDK/dpdk/commit/c506cc8305b4ca17bae903a54daaeaf5b7005038)
- Fixed the setting of the device reset status bit when the 82580 network card is reset. Instead, the register value is read first and then written.
  ↳ No PR: [88a1eb7](https://github.com/DPDK/dpdk/commit/88a1eb79ef08d309af58ad4921db7200fa7c5073)
- Add a check on the return value of e1000_write_emi_reg_locked in the e1000 driver.
  ↳ No PR: [b0b6b50](https://github.com/DPDK/dpdk/commit/b0b6b50c20b03170c83985194fd9acef9467ded6)
- Fix the 82575 network card Rx FIFO refresh logic, skip the management control check, and perform refresh unconditionally.
  ↳ No PR: [d107a23](https://github.com/DPDK/dpdk/commit/d107a23f60c6a8b9543c386ecc48abc4f92f50d3)
- Fix VXLAN flow flag processing in testpmd, only set G bit by default when the user does not specify flags.
  ↳ No PR: [7441e59](https://github.com/DPDK/dpdk/commit/7441e59a1f8352f176e9a4b9c480e944a4f145f6)
- Fixed the problem of testpmd not updating the queue number after device attach, and delaying the initialization of new ports.
  ↳ No PR: [2d87f85](https://github.com/DPDK/dpdk/commit/2d87f8569934ddbb7ffa7f9d70b3d72196bdbdf7)
- Fix uninitialized return variable in test/ring.
  ↳ No PR: [afccc9c](https://github.com/DPDK/dpdk/commit/afccc9c87834627844c3e60e8bd8b1b52f950818)
- Fixed the problem of missing error information when constructing the mlx5 driver stream operation, and now returns a specific error description.
  ↳ No PR: [562eba8](https://github.com/DPDK/dpdk/commit/562eba858fa4fcd049a797145fcb1f7b72d5a35e)
- Fixed compilation errors caused by missing header files when bbdev library is compiled in MSVC.
  ↳ No PR: [42cb1fc](https://github.com/DPDK/dpdk/commit/42cb1fc70dcb65c75c0a2a0cfa9b93b860fc9dd7)
- Fixed the initialization error of ntnic driver when RTE_ASSERT is not enabled, and corrected the assertion condition.
  ↳ No PR: [5ecaf2e](https://github.com/DPDK/dpdk/commit/5ecaf2eb07bb1ecf3c58588ef288056a68b70ea5)
- Removed a useless assignment in the octeon_ep driver when mailbox obtains link information.
  ↳ No PR: [4143d5f](https://github.com/DPDK/dpdk/commit/4143d5f09074c15706479ad4e271f3ab16d90579)
- Removed a useless variable assignment in the enetfec driver.
  ↳ No PR: [93fdf2a](https://github.com/DPDK/dpdk/commit/93fdf2ab302f244076c3894ab4a1a5b86d704eae)
- Fixed the DMA adapter log format string in eventdev and corrected the device ID data type.
  ↳ No PR: [b2ff5f6](https://github.com/DPDK/dpdk/commit/b2ff5f66189e75deea067598263929c591250e1b)
- Remove useless assignments in dev_uev_socket_fd_create and dev_uev_parse.
  ↳ No PR: [36128ec](https://github.com/DPDK/dpdk/commit/36128ec5d93591700b72f3fc01bfe6216eaee905)
- Removed redundant checks on the return value of pthread_mutex_init in multiple drivers and libraries to simplify the initialization process.
  ↳ No PR: [d28809c](https://github.com/DPDK/dpdk/commit/d28809c27d2dae063231bee4e8332095476812f3), [7d32c00](https://github.com/DPDK/dpdk/commit/7d32c003ac175d7ac8669dc11684c75cc7eb56b8), [6169517](https://github.com/DPDK/dpdk/commit/6169517c111e5fefb9bb22458191e6c402d2ae9c), [58825f4](https://github.com/DPDK/dpdk/commit/58825f4138629d35a74011db62863c7af8e64669), [0745048](https://github.com/DPDK/dpdk/commit/0745048c415f46cc61259dc3b46c6b87be50ef6d), [4d2aa15](https://github.com/DPDK/dpdk/commit/4d2aa150769b170e439b4ae6200463140cb44ff5)
- Split the DTS configuration file into two independent files: node and test run, and add corresponding command line parameters.
  ↳ No PR: [a06851d](https://github.com/DPDK/dpdk/commit/a06851d856ad5a38beeb49de5390596fbcb9edf2)
- Fix MSVC warning about implicit conversion of 32-bit shifts to 64-bit, use explicit type conversion.
  ↳ No PR: [0644f07](https://github.com/DPDK/dpdk/commit/0644f07f822e71b10f8c968c0f1d62d924e42d3e)
- Remove duplicate conditional branches in the i40e driver and unify the if/else curly brace style.
  ↳ No PR: [8c085f7](https://github.com/DPDK/dpdk/commit/8c085f702ac3074d20e51ee691b0bc967919c43e)
- Remove unused code in flow_create_profile_inline and simplify error handling paths.
  ↳ No PR: [e4050ed](https://github.com/DPDK/dpdk/commit/e4050ed404b23e881deb40c02a5dc64829946175)
- Remove redundant conditional judgments in nthw_setup_rx_virt_queue.
  ↳ No PR: [af77f8b](https://github.com/DPDK/dpdk/commit/af77f8b4790ce728bbbc1cf3ac7302b909c86606)
- Replace multiple variable-length arrays with fixed-size arrays to eliminate ISO C90 compiler warnings.
  ↳ No PR: [4643565](https://github.com/DPDK/dpdk/commit/464356531592bc42a3742d50cd380a30faa876b2), [42dc8da](https://github.com/DPDK/dpdk/commit/42dc8daee943cbf5deca5306245f6a3c38f0e701), [a09e6d9](https://github.com/DPDK/dpdk/commit/a09e6d972080b34cf281269cd24c37f3479a95c5), [fed4f40](https://github.com/DPDK/dpdk/commit/fed4f403d131d8f399db30780aad63cda974506a)
- Fixed the data type conversion problem when NVM reads, and eliminates static analysis warnings through explicit type conversion.
  ↳ No PR: [d6ad4cd](https://github.com/DPDK/dpdk/commit/d6ad4cdad361558bfb2c04112bd6650debbc9c7f)
- Fixed a warning in the e1000 driver that loop variable type width mismatch may lead to infinite loops.
  ↳ No PR: [3d36053](https://github.com/DPDK/dpdk/commit/3d3605399170d5871ba80448de236f7acbbe8f98)
- Fixed uninitialized array variables in the e1000 driver, eliminating static analysis warnings by initializing them to zero.
  ↳ No PR: [4be9a70](https://github.com/DPDK/dpdk/commit/4be9a7008efe063fbd326fea9965f946c8969039)
- Fixed the type problem of SW/FW semaphore mask bit operation in e1000 driver.
  ↳ No PR: [c848457](https://github.com/DPDK/dpdk/commit/c848457b38851f175893488c0be713995cb19bf2)
- Fixed static analysis warnings caused by data type errors when reading NVM data in the e1000 driver.
  ↳ No PR: [b932270](https://github.com/DPDK/dpdk/commit/b932270c66d0179824118afbfd7cfb347ddf07d2)
- Fixed compilation warnings caused by symbol mismatch in the vmxnet3 driver, and renamed variables to comply with coding specifications.
  ↳ No PR: [feed1d0](https://github.com/DPDK/dpdk/commit/feed1d0733a60b4b3c9942af58f0380746aff28c)
- Replace 32-bit shift operations with 64-bit macros in i40e, iavf, and ice drivers to eliminate MSVC compilation warnings.
  ↳ No PR: [35db745](https://github.com/DPDK/dpdk/commit/35db745d37d0b12a16c41d05695ad6a1296a20c1)
- Fixed MSVC compilation warning caused by symbol mismatch in ice_dcf_node_param_check function.
  ↳ No PR: [2cec7d4](https://github.com/DPDK/dpdk/commit/2cec7d4f11d81c31d8ccbe2871cb54c3ba557c0a)
- Support new FDB_TX field type in debug information.
  ↳ No PR: [28736d9](https://github.com/DPDK/dpdk/commit/28736d99f068ba81dfc539d70145b71940d19c44)
- Fix the USELESS_CALL problem reported by Coverity and remove useless release operations.
  ↳ No PR: [65f56bc](https://github.com/DPDK/dpdk/commit/65f56bc68206237f8a8efa07143d97e6f279afcb)
- Fixed the format error when printing the port number in the log, changing the format specifier from %u to %d.
  ↳ No PR: [35f5d79](https://github.com/DPDK/dpdk/commit/35f5d799a70d7fe0063bca428013af8504704066)
- Remove the useless conditional judgment of the port initialization function in the xsc network card driver.
  ↳ No PR: [17fa38f](https://github.com/DPDK/dpdk/commit/17fa38f4e8180e3caa1735d690ad629abd1f0a9f)
- Removed useless conditional judgment in xsc_rx_poll_len function and fixed PVS Studio warning.
  ↳ No PR: [704a854](https://github.com/DPDK/dpdk/commit/704a8546bc12754268e54b015412737c07a6dde6)
- Remove useless assignments in xsc_np.c and xsc_tx.c.
  ↳ No PR: [245fc72](https://github.com/DPDK/dpdk/commit/245fc72fdc3fdaf67240f64e45cd0587a479d487)
- Downgraded inline device not detected error log to debug log.
  ↳ No PR: [6d642d0](https://github.com/DPDK/dpdk/commit/6d642d06820cf94515946248977892f5256cd52a)
- Reconstruct the age event generation logic to only generate age events for physical ports.
  ↳ No PR: [354b5fc](https://github.com/DPDK/dpdk/commit/354b5fc865b0edda48717e5d94d66a67a82b2c46)
- Delay lcore variable allocation, only allocated when power management queue is enabled/disabled.
  ↳ No PR: [108d30a](https://github.com/DPDK/dpdk/commit/108d30ab8d7a63fea4842c6079fe2669af17ae11)
- Removed redundant condition judgment for SW-FW synchronization in txgbe driver.
  ↳ No PR: [0d6b122](https://github.com/DPDK/dpdk/commit/0d6b122c28b4a3ab4cbb79103f305e49a9edfcae)
- Fixed compilation warnings caused by excessively long union partial initialization and array initialization strings under GCC 15.
  ↳ No PR: [e7133f8](https://github.com/DPDK/dpdk/commit/e7133f8fb39f506dc1eef02c2927acda949ca000), [e931818](https://github.com/DPDK/dpdk/commit/e931818831336de2732ca29082e47799359d9c71)
- Fix user callback in vhost_crypto example, use new_connection and destroy_connection instead.
  ↳ No PR: [f7cf44d](https://github.com/DPDK/dpdk/commit/f7cf44d49b1115238a87c5852db4b47290bfdc25)

### Refactoring optimization
- Postpone the allocation of lcore variables related to power monitoring and only allocate them when calling relevant APIs to avoid early allocation.
  ↳ No PR: [77e33f2](https://github.com/DPDK/dpdk/commit/77e33f28c06dde70b90b9d4fa9a57062c3bf11f7)
- Allow duplicate SPIs for outbound IPsec sessions, and change session lookup from SPI to SA index.
  ↳ No PR: [c7c508e](https://github.com/DPDK/dpdk/commit/c7c508ea8ac802d2b29818cd4433f728ded98e65)
- Removed variable length arrays from the GRO library, ixgbe and i40e drivers and used fixed size arrays instead to avoid compilation warnings.
  ↳ No PR: [b1a3b26](https://github.com/DPDK/dpdk/commit/b1a3b2615a2ac3fa56fba42773259823bb071da3), [948a4bb](https://github.com/DPDK/dpdk/commit/948a4bbdeac9f1eef0c62b96bd1b59b1f9a021cc), [32ecd02](https://github.com/DPDK/dpdk/commit/32ecd02ce2bdf84dcc29dfd118e19e947f8f7a66)
- Removed redundant dereferences for function pointer calls in multiple drivers to simplify the code.
  ↳ No PR: [3e5df72](https://github.com/DPDK/dpdk/commit/3e5df723600e0d725bf2a3f037eed04203c1d5b3), [25c03a3](https://github.com/DPDK/dpdk/commit/25c03a3df58bf41ff7e649f89ae42ff84591e6b7), [d9217b6](https://github.com/DPDK/dpdk/commit/d9217b6aed60cec7316bd3e6395483d98afb0e1b), [58a5281](https://github.com/DPDK/dpdk/commit/58a5281253f8ddf52c8c1cb3476151cf4936de76), [d3eeb85](https://github.com/DPDK/dpdk/commit/d3eeb85187f85b472f57fccf9e673eb0fc32dfab), [ebffb2b](https://github.com/DPDK/dpdk/commit/ebffb2b3d3aea1571ca73791dd6a61261e5ce517), [4490d81](https://github.com/DPDK/dpdk/commit/4490d81ce350b3fe783c26e56f2c9e2624bb95ce)
- Renamed VLAN PQF macro and local variable version to improve code consistency.
  ↳ No PR: [1db13a7](https://github.com/DPDK/dpdk/commit/1db13a7aeece7b434c0bb652d1e46cbbf5f365b6), [ef782b7](https://github.com/DPDK/dpdk/commit/ef782b7fe309a60f875268d57cc575e33de02117)
- Removed unused variable declarations and weak symbol functions in multiple drivers and cleaned up dead code.
  ↳ No PR: [298535b](https://github.com/DPDK/dpdk/commit/298535bf00dd799b97e758c91425ec1a6702a4f6), [0b0884a](https://github.com/DPDK/dpdk/commit/0b0884aca3d3c0f8928a1b7dd1345abbb953ba94), [385668e](https://github.com/DPDK/dpdk/commit/385668e9b845c2d90e6b9bd0f33bbcd9d5f5ca7b)
- Remove unnecessary null pointer check before rte_free call.
  ↳ No PR: [eca688c](https://github.com/DPDK/dpdk/commit/eca688cbd15dda808a4605f52fa78b5cf8f81776)
- Removed repeated cleanup code in the octeon_ep driver uninstall function, and unified the device operation pointer clearing logic.
  ↳ No PR: [52b1124](https://github.com/DPDK/dpdk/commit/52b11243aa1f73bcac38d6f15cc05a0c4b5ab119)
- Remove unused NIM_TRIGGER related code in the nt4ga_stat_setup function, and add memory allocation of the ifr_counters structure.
  ↳ No PR: [f7dabff](https://github.com/DPDK/dpdk/commit/f7dabff91738e97d81f6844cb6c00b503de3d9ea)
- Remove PMD level shutdown threads and SIGINT signal processing to simplify the PMD shutdown mechanism.
  ↳ No PR: [b8f202b](https://github.com/DPDK/dpdk/commit/b8f202b85468f3e22de783873a74e21c10c8c233)
- Change the queue release operation in the memif driver from a function pointer call to a direct call to a local function.
  ↳ No PR: [d3bf431](https://github.com/DPDK/dpdk/commit/d3bf431814dfb9364e4d622a3013fb5b40dbc649)
- Removed unnecessary function pointer dereferences in compressdev, dmadev, rawdev, mldev and regexdev drivers.
  ↳ No PR: [4bee341](https://github.com/DPDK/dpdk/commit/4bee341357b1cc105465dfb03aa4bb1bfb535c3b), [04d80ff](https://github.com/DPDK/dpdk/commit/04d80ffae7e2d712ca9d37fdaf12eafa3b2d3aa9), [0e18ccb](https://github.com/DPDK/dpdk/commit/0e18ccbe18fe7904a72df865f434b28ab4f6b154), [e36ce07](https://github.com/DPDK/dpdk/commit/e36ce0700e112e5d0e3e1af7bf6956771f68e222), [09acb86](https://github.com/DPDK/dpdk/commit/09acb863d13256871f901a2940a4d212b600099d)
- Remove weak symbols in auxiliary, virtio, enic and nfp drivers and use conditional compilation to provide stub functions.
  ↳ No PR: [def2f7c](https://github.com/DPDK/dpdk/commit/def2f7c71ad3473ed0eb125c7155381569050bc6), [510f7c2](https://github.com/DPDK/dpdk/commit/510f7c212c5df71c7ebb3fb3ceec421dd81472fe), [db9c9e3](https://github.com/DPDK/dpdk/commit/db9c9e37d1ea2d4d3fb09bda7a9e3cf6ae628f92), [54affcd](https://github.com/DPDK/dpdk/commit/54affcdc00821edc1a7d75ea7a3b6071b4ee56cd)
- Code deduplication and generalization of the internal functions of the ring library to improve modularity and reusability.
  ↳ No PR: [3197a1f](https://github.com/DPDK/dpdk/commit/3197a1ff2a2a6bef224cd51f835f135be3776f23), [e4251ab](https://github.com/DPDK/dpdk/commit/e4251abd4a3a1dbf7d613fa407e4d2843708a843)
- Reconstruct Vhost dequeue path error handling and RARP packet injection processing to improve code maintainability.
  ↳ No PR: [6ee0cf8](https://github.com/DPDK/dpdk/commit/6ee0cf8024f392a07dc0f3a624f3cc2daa48a0df), [6d7e741](https://github.com/DPDK/dpdk/commit/6d7e741be18ab1e6ecce46edb2516318305c3c73)
- Internal refactoring of bnxt driver, including macro renaming and simplified checking logic.
  ↳ No PR: [35180d7](https://github.com/DPDK/dpdk/commit/35180d7b216f987a0e4fb98eb1e6bcf26fe76e69), [e33f713](https://github.com/DPDK/dpdk/commit/e33f713614e4639a4f7f1f008b4a42abe6412693)
- Internally reconstruct the zxdh driver, delete the port table and optimize the queue resource allocation and release process.
  ↳ No PR: [f16b169](https://github.com/DPDK/dpdk/commit/f16b1690acc0b18f966ab49b44e12d745bc83d15), [074b7c3](https://github.com/DPDK/dpdk/commit/074b7c3f602d6fea4a06d0f62d6e5e4b25173c5c)
- Replace unnecessary rte_memcpy with structure assignment in the ptpclient example to improve type safety.
  ↳ No PR: [e336b35](https://github.com/DPDK/dpdk/commit/e336b357a204e932bed5cd98307309dfe554ee4a)
- Refactor the ICH8LAN code and reduce the indentation level to improve the code flow.
  ↳ No PR: [d15cddc](https://github.com/DPDK/dpdk/commit/d15cddcd031fb8a18d25ceae7745d2bb8e6f813b)
- Removed unused packet reassembly functions in i40e, iavf and ice drivers.
  ↳ No PR: [4ffcdb5](https://github.com/DPDK/dpdk/commit/4ffcdb59f59c400ea9d28932a298494dcd498501)
- Replace the standard assert call in the ntnic driver with the RTE_ASSERT macro to unify the assertion mechanism.
  ↳ No PR: [78c2c96](https://github.com/DPDK/dpdk/commit/78c2c965cc72734f4aa51df241b4eccf3f535ca8)

### Test related
- Fixed the error code and null pointer issues when session creation failed in the encryption test.
  ↳ No PR: [bda6b74](https://github.com/DPDK/dpdk/commit/bda6b749398ed0a3fdefadf76a43a2e575257d40)
- Fixed the problem of ring stress test initialization failure when the number of customized lcores is not a power of 2.
  ↳ No PR: [2cf3a8d](https://github.com/DPDK/dpdk/commit/2cf3a8d35d2db1cee1523e6e9ef5553432fbf56f)
- Add functional testing and stress testing for soring API.
  ↳ No PR: [70581c3](https://github.com/DPDK/dpdk/commit/70581c355d6965f7be2dbf1c4fc0d30778c53b98)
- Added a new stress test suite, and registered ring_stress_autotest and soring_stress_autotest test cases.
  ↳ No PR: [06e2856](https://github.com/DPDK/dpdk/commit/06e2856620a70000b2a28f0ea715fc247b85fd8d)
- Fixed incorrect assumption of active backup receiving test in bonding test.
  ↳ No PR: [eb29e62](https://github.com/DPDK/dpdk/commit/eb29e625ce41b50898efc8e2618b7eeb128460ed)
- Fixed the length error of plaintext and ciphertext in AES-ECB test vector.
  ↳ No PR: [4d6b263](https://github.com/DPDK/dpdk/commit/4d6b2633b030f6b469c78fd00f012c8192979332)
- Add device MACsec offload capability check in MACsec inline test, and skip the test if it is not supported.
  ↳ No PR: [15fb12f](https://github.com/DPDK/dpdk/commit/15fb12fee0a7dff1b02fe8868b916927289b8e8f)
- Skip non-C11 atomic tests under MSVC compiler.
  ↳ No PR: [763bdca](https://github.com/DPDK/dpdk/commit/763bdca4cc48768c5b69b6028af8a2fe899379c5)
- Removed variable-length arrays in test code to be compatible with MSVC compiler.
  ↳ No PR: [f9c043b](https://github.com/DPDK/dpdk/commit/f9c043b542394281484769fcc6daf9ccb297efd3)
- Fixed the problem of insufficient number of event queues configured for event devices in unit tests.
  ↳ No PR: [baa3cc1](https://github.com/DPDK/dpdk/commit/baa3cc13c1df10eb36a158c45a921ede2e806f75)
- Removed no longer needed private session memory pool members from the test suite parameters structure.
  ↳ No PR: [dafeb6a](https://github.com/DPDK/dpdk/commit/dafeb6ae229bc572fc809e62e4e8e242b08ca2f7)
- Fixed an issue where output buffer header data was not checked in GCM OOP tests.
  ↳ No PR: [27eb74e](https://github.com/DPDK/dpdk/commit/27eb74ea6e25966d3857539cb15ddd4f20f05ebe)
- Fixed pointer conversion issue in IOVA as physical address mode in DMA test.
  ↳ No PR: [5879d20](https://github.com/DPDK/dpdk/commit/5879d209d847c1025d0852dad7f3bee3e5cff2f6)
- Introduced atomic testing support for eventdev applications.
  ↳ No PR: [9d619f8](https://github.com/DPDK/dpdk/commit/9d619f82321b1b56c24bf9deff96845e19828870)
- Added atomic queue-based tests in the test-eventdev application.
  ↳ No PR: [4b522ef](https://github.com/DPDK/dpdk/commit/4b522ef8bca8e75711be90234468644df27a8ff6)
- Added atomic ATQ test for test-eventdev application.
  ↳ No PR: [2c1d945](https://github.com/DPDK/dpdk/commit/2c1d94555cdb37e1e1d5a2872bb6c407021cbb14)
- In encryption tests, change test result from fail to skip when virtio or virtio-user PMD is not loaded.
  ↳ No PR: [6a07562](https://github.com/DPDK/dpdk/commit/6a0756249de96d0962266feb8ed8f9e8fa3a78ff)

### Performance optimization
- Optimize the mlx5 device detection process: introduce a device information caching mechanism to avoid repeated netlink communications, and change port information updates to RDMA Netlink monitor events to improve performance.
  ↳ No PR: [51fb5c4](https://github.com/DPDK/dpdk/commit/51fb5c40c826ecd5eef7f1ddbea2d44d7dd97fc4), [2a18d00](https://github.com/DPDK/dpdk/commit/2a18d0022c0593b209fc8196c9978a4ffb83f030)
- Add AVX2 vector path support (single queue receive and send paths) to the idpf driver, automatically enable it on CPUs that do not support AVX512, and improve performance.
  ↳ No PR: [24cc335](https://github.com/DPDK/dpdk/commit/24cc335bad50cdb0934cc674c916e7ee025b6556), [afac626](https://github.com/DPDK/dpdk/commit/afac6261461f104cea03198616df39d39932dbd2)
- Optimize the rule creation performance of non-template flow API: replace heap memory allocation by pre-allocating thread workspace to reduce overhead.
  ↳ No PR: [3cd695c](https://github.com/DPDK/dpdk/commit/3cd695c34528571c378c5f6be7ff81d3cca9a84c)
- Optimize the Tx queue structure layout of i40e and ice drivers to improve cache efficiency: uniformly use a streamlined software ring structure that only contains mbuf pointers, and use the default threshold to query queue information to improve performance.
  ↳ No PR: [e3b5f52](https://github.com/DPDK/dpdk/commit/e3b5f52d590ec2cae30f2eddcc310832154847f1), [7e230d5](https://github.com/DPDK/dpdk/commit/7e230d568a751685588b7badcc14ede92cdd9c91), [10da679](https://github.com/DPDK/dpdk/commit/10da6792988bbe0b4aaa2221c7e1be8283e74c17)
- Unify all vector paths of the iavf driver to use a smaller and faster software ring structure, remove the AVX-512 dedicated setting function, and update the sending function interface to improve performance.
  ↳ No PR: [7662502](https://github.com/DPDK/dpdk/commit/7662502d4c0344059903be75e9afa0ffe26865b3)
- Optimize the receiving performance of mana network card driver under 32-bit architecture: change the short doorbell triggering method from triggering immediately after each mbuf is allocated to batch triggering.
  ↳ No PR: [4e6a273](https://github.com/DPDK/dpdk/commit/4e6a273d60c766a3697935319cf5bb00bd330704)
- Configure pool attributes according to table types, and set corresponding optimization strategies for FDB subdomains to improve performance.
  ↳ No PR: [16360ab](https://github.com/DPDK/dpdk/commit/16360abec9defce9a2661d8dc2f9b40f0f74263f)
- Dynamically adjust the Rx burst threshold of the bnxt driver according to the link speed, configure higher burst values for high-speed ports such as 400G, and optimize performance.
  ↳ No PR: [478ead4](https://github.com/DPDK/dpdk/commit/478ead42ce59e48b61f368eaed17a7b9426940fe)
- Added --cmdline-file-noecho option to testpmd, and fixed file descriptor leak of --cmdline-file option.
  ↳ No PR: [184796f](https://github.com/DPDK/dpdk/commit/184796f62847edba4e8107314255898de4cb275d)
- Replace non-standard bit operation macros with RTE_BIT32 macros to unify the coding style.
  ↳ No PR: [4152005](https://github.com/DPDK/dpdk/commit/415200554bb2a5b1412f340813bdb733306de642)
- Remove loops and their associated arrays that are invalid because the dependent variable is always zero, and clean up assertions and memory deallocation.
  ↳ No PR: [6d98cc2](https://github.com/DPDK/dpdk/commit/6d98cc26bd2554e4829549cc504c169b257c0bea)
- Optimize the link update process: Supplement the auto-negotiation status and avoid repeated port configuration when the link status does not change.
  ↳ No PR: [1ac9997](https://github.com/DPDK/dpdk/commit/1ac99972f1ff47db9dee7146232142dbc35847d7)
- Optimize MAC address operation: Add MAC table management function to improve link information acquisition and shared data initialization.
  ↳ No PR: [1c8f68b](https://github.com/DPDK/dpdk/commit/1c8f68b64cfc0c3bbc05ce2c0c00378a1d3b43ca)
- Optimized promiscuous mode operation: Added functions such as port initialization, promiscuous mode setting, broadcast table setting and RSS table acquisition.
  ↳ No PR: [6736fb7](https://github.com/DPDK/dpdk/commit/6736fb7d161fb70696c1410bf6a7a8383fb00e0a)
- Optimize VLAN filtering and offloading operations: Reconstruct related functions and add VF side processing logic.
  ↳ No PR: [b4f996b](https://github.com/DPDK/dpdk/commit/b4f996b7fcf601f983bbd0f61028d1de859fa6d5)
- Replace memory barriers in r8169 driver with atomic loads, using acquire memory ordering to improve performance.
  ↳ No PR: [4709bcf](https://github.com/DPDK/dpdk/commit/4709bcf7a5d96c0fe074eb06120bd67581ea8be0)
- Remove cache line alignment of per-lcore status structure to reduce memory usage.
  ↳ No PR: [e8c626a](https://github.com/DPDK/dpdk/commit/e8c626ac05cae35f772cf4a4321de7011d2f63e1)
- Reconstruct the lookup memory data layout, store the pool buffer size by port, and support reorganization scenarios in the fast path.
  ↳ No PR: [b826d04](https://github.com/DPDK/dpdk/commit/b826d043c01f26e7c0f6807a67928a41704c0fd4)

### Security related
- Fixed the array out-of-bounds problem in the hash classifier and packet descriptor modules, and added index boundary checking.
  ↳ No PR: [7e46508](https://github.com/DPDK/dpdk/commit/7e4650843db76a5f6909c45a9550060721ad41fb)
- Fixed the redundant address operator in macro DO_COMPARE_INDEXS to avoid pointer misuse causing array out-of-bounds.
  ↳ No PR: [222466c](https://github.com/DPDK/dpdk/commit/222466ce80c0f339b97052b0bbcbf5516aa79a22)
- Fixed integer overflow problem in XSC network driver.
  ↳ No PR: [22fe07c](https://github.com/DPDK/dpdk/commit/22fe07ccc23c978ee96d33847815d6717b220609)
- Fixed an issue where invalid signatures returned error status in OpenSSL RSA verification operations.
  ↳ No PR: [6c209dd](https://github.com/DPDK/dpdk/commit/6c209dd8785f34bfdc99b869c14e063d084508c2)
- Fixed a potential infinite loop problem caused by mismatched loop variable types in the igc PHY driver.
  ↳ No PR: [c7da9da](https://github.com/DPDK/dpdk/commit/c7da9dab82190564d68f0d928ba3e381dcc74d9f)
- In cnxk and openssl encryption drivers, replace the bit left shift macro used in the initialization of the EDDSA hash algorithm with a 64-bit macro.
  ↳ No PR: [f846eb3](https://github.com/DPDK/dpdk/commit/f846eb37e241d801b43c52e034fb9e82d5b1f8a1)
- Removed repeated conditional judgments in the IPsec SA parameter filling function, and adjusted the header file inclusion order.
  ↳ No PR: [1585667](https://github.com/DPDK/dpdk/commit/15856672e7f194fadad4ea5dbcc224c4129220bf)
- Remove function pointer dereference, simplify null pointer checking and function calling.
  ↳ No PR: [5515d4d](https://github.com/DPDK/dpdk/commit/5515d4d913f5944eed29029667e37d9f13e8f70d)
- Removed unnecessary 1ms delay in security statistics reading interface.
  ↳ No PR: [54c590e](https://github.com/DPDK/dpdk/commit/54c590e585db7058d551c12dd21aafe71c6b10f3)
- Replaced strncpy with strlcpy in the vhost library, ensuring proper string termination and avoiding compiler warnings.
  ↳ No PR: [c171a2d](https://github.com/DPDK/dpdk/commit/c171a2d5ff17657916256b137a000d63176b9118)

### Documentation
- Updated ionic driver guide, fixed broken link, and added link to DSC3-400 product introduction.
  ↳ No PR: [328f800](https://github.com/DPDK/dpdk/commit/328f800ccc1acdeb04288ddd21ed551bd7f78cc1)
- Fixed grammar, spelling and formatting issues in DPDK 25.03 release notes, and cleaned up template comments.
  ↳ No PR: [71a4b33](https://github.com/DPDK/dpdk/commit/71a4b3332f42607c214e6eb9087b6095d6a1dee7)
- Added missing API documentation for DTS test suite.
  ↳ No PR: [c9f4d4b](https://github.com/DPDK/dpdk/commit/c9f4d4b4f27149f2574ba9fb8d66b009b1dcec52)
- Added documentation for the --noiommu-mode option in the devbind tool guide.
  ↳ No PR: [a85d7ca](https://github.com/DPDK/dpdk/commit/a85d7ca7d075d314c780e845fd9788ae2d532289)
- Removed documentation references to old code inspection tools and formatting tools that are no longer used in DTS.
  ↳ No PR: [43f07ae](https://github.com/DPDK/dpdk/commit/43f07ae4bbeda0fee30515a74b3725ac51e23f4a)
- Corrected documentation for queue start/stop function flags, added description of delayed start configuration options.
  ↳ No PR: [4f6641c](https://github.com/DPDK/dpdk/commit/4f6641cbdd571433d38fd82781916e0f1e64908b)
- Updated the devargs documentation in the vhost user guide, added client parameter descriptions, and improved iface and queues parameter descriptions.
  ↳ No PR: [17fe95e](https://github.com/DPDK/dpdk/commit/17fe95e0146f1a7b57492d875ffba849c4c8605c)
- Updated the MLX5 network card driver documentation to detail the support limitations of RSS hash results.
  ↳ No PR: [86bfe90](https://github.com/DPDK/dpdk/commit/86bfe90232fbd57a3cffdeb71a5fa2c42934c115)
- Updated the ZXDH network driver documentation, corrected the link format, and added function support instructions.
  ↳ No PR: [3a2be32](https://github.com/DPDK/dpdk/commit/3a2be32b7cc9e5b1d426f3abef1061297adf91f1)
- Updated the ODM DMA device guide, replaced the kernel PF driver module with the ODM PF driver application, and updated the performance tuning parameter configuration method.
  ↳ No PR: [c1d3a5e](https://github.com/DPDK/dpdk/commit/c1d3a5ec473850c9f6f27aeae6821f97342fcce3)
- Added work queue naming constraints in the idxd DMA device documentation, stating that the name must start with dpdk_ or apply the file-prefix parameter when DPDK automatically discovers the queue.
  ↳ No PR: [5d7abee](https://github.com/DPDK/dpdk/commit/5d7abeeea66143d011e107278f8f3fa28b1dcf75)
- Updated the version information of the e1000 base code, and updated the relevant descriptions in the release notes and README.
  ↳ No PR: [f43b1e8](https://github.com/DPDK/dpdk/commit/f43b1e80203dd2c6acc9eca2d44b3dc96536c295)
- Refactored the runtime internals, introduced the TestRun class to isolate test runs, converted the runtime state into a finite state machine, and updated the relevant API documentation.
  ↳ No PR: [3c76bb6](https://github.com/DPDK/dpdk/commit/3c76bb630c7d21d6cfa037b9730cedadf19ef549)
- Removed the distinction between SUT and TG nodes, split the DPDK configuration into build and runtime parts, and updated related documentation.
  ↳ No PR: [d77a4a2](https://github.com/DPDK/dpdk/commit/d77a4a27bd240bd3cded76d15b410b2af74d256f)
- Added instructions on setting the corresponding flags when matching VXLAN-GPE and VXLAN-GBP in the mlx5 network card driver guide.
  ↳ No PR: [e808f7c](https://github.com/DPDK/dpdk/commit/e808f7c8455736a69f9740267a45fae0491c2fb3)
- Added the ability to configure individual test suites for DTS, and added the --tests-config-file command line parameter to support overriding variable values for specific test suites through YAML files.
  ↳ No PR: [184d21f](https://github.com/DPDK/dpdk/commit/184d21f08db4b236bdeb9f3f71f921017cdf7188)
- Fixed the description of the final LTS release year in the documentation, updating "2 years" to "3 years" to match the actual maintenance period.
  ↳ No PR: [7d6c28c](https://github.com/DPDK/dpdk/commit/7d6c28c9199351805e693e9b8f58f60e6f51c2ab)
- Updated the NVIDIA BlueField platform documentation, added a comparison table between BlueField-2 and BlueField-3, added a description of DPDK 25.03 compilation options, and fixed a broken documentation link.
  ↳ No PR: [05fefe4](https://github.com/DPDK/dpdk/commit/05fefe4faddd56f1489d1ab663dfc025cd8c9eba)
- Added a list of test platforms equipped with NVIDIA network cards in the 25.03 release notes.
  ↳ No PR: [bc59bdc](https://github.com/DPDK/dpdk/commit/bc59bdce1208e267b41c89053aa20f41c052c1de)
- Updated the recommended kernel driver version and firmware version for i40e and ice network cards.
  ↳ No PR: [464ce3c](https://github.com/DPDK/dpdk/commit/464ce3c581c8791970222c69736589ab47d35ede)
- Changed DTS to run only one test run per execution, and updated configuration file names, command line arguments and documentation references accordingly.
  ↳ No PR: [d6d41e3](https://github.com/DPDK/dpdk/commit/d6d41e3a49ac3f96e104dc98568e33b901fd7e4d)

### Build/CI
- Fix compilation warning in vhost/crypto due to comparison of signed and unsigned integers.
  ↳ No PR: [c2fcece](https://github.com/DPDK/dpdk/commit/c2fcecebd02314d1f35284a3b07eb3d105d22c7c)
- Optimize the license check script, reformat the exception file list, and increase the display of files that do not comply with the BSD-3 license.
  ↳ No PR: [8729a59](https://github.com/DPDK/dpdk/commit/8729a593eb61bf9348cfa1a33ea674d6a50c6454)
- Changed Python strings to raw string representation to avoid invalid escape sequences causing warnings or errors in Python 3.12 and future versions.
  ↳ No PR: [d3e90e5](https://github.com/DPDK/dpdk/commit/d3e90e5e37872f1040f37a08b056102c1a302bb3)
- Fix warnings due to uninitialized variables when compiling with GCC 15, zero-initialize the fc_params structure in fill_pdcp_chain_params.
  ↳ No PR: [224e37a](https://github.com/DPDK/dpdk/commit/224e37a6a442b6a1f6d179b1756383f1a80cf3ed)
- Fixed the bug in the dts-check-format script that did not capture the linter return value to ensure that errors that cannot be automatically repaired can be correctly detected.
  ↳ No PR: [a1018d1](https://github.com/DPDK/dpdk/commit/a1018d158a089bf8e4d416fa68df380ddac65315)
- Add crypto as an additional march feature for CN9K SoC.
  ↳ No PR: [b4d2b0b](https://github.com/DPDK/dpdk/commit/b4d2b0ba7046fa779d342f6969dac09657af0dbf)
- Fixed Arm native build failure and added global definition for extra_features.
  ↳ No PR: [7246d0a](https://github.com/DPDK/dpdk/commit/7246d0a80cb79a04e1334393ef507aa4ef7accd9)
- Alphabetically sorted ARM platform SoC configurations and names.
  ↳ No PR: [046cca9](https://github.com/DPDK/dpdk/commit/046cca99c3fd03bfb95d3e27a56aab40c2c8f45a)
- Removed the compilation workaround for unused parameter warnings in the e1000 base code, and instead used macros to explicitly mark and clean up the formatting.
  ↳ No PR: [4bfa109](https://github.com/DPDK/dpdk/commit/4bfa1096249cb52f5d62cabb6a538ee37696fd08)
- Fixed the path matching problem of checkpatches.sh script in devtools.
  ↳ No PR: [91c717c](https://github.com/DPDK/dpdk/commit/91c717ca1e98adc211a7fa5d00515758c9438132)
- Replaced code formatting and lint tools in dts-check-format tool with Ruff.
  ↳ No PR: [2f6c0c4](https://github.com/DPDK/dpdk/commit/2f6c0c4e979399d62bc8089413b907f9f32aa910)
- Added compile flag for MSVC compiler to ignore unused variable warnings for multiple drivers.
  ↳ No PR: [84fbc5b](https://github.com/DPDK/dpdk/commit/84fbc5bb3b985ca1f559efb14269996f6402ca78), [7587660](https://github.com/DPDK/dpdk/commit/7587660f199266ce45aabb8c2259dd09452cb01d)
- Merge scattered .gitignore files to the top level and update exclusion rules in the check script.
  ↳ No PR: [d85aaff](https://github.com/DPDK/dpdk/commit/d85aaff163a0bea5f365f9e38db757aa0e715f36)
- Install the babeltrace tool in CI to verify whether the generated trace file can be parsed.
  ↳ No PR: [75d1e88](https://github.com/DPDK/dpdk/commit/75d1e888f49a7fb07c2260032c6fcbb9108a6b10)
- Removed the compile option that disables unused variable warnings in the base code build of the idpf driver, and re-enables these warnings.
  ↳ No PR: [4c0db9c](https://github.com/DPDK/dpdk/commit/4c0db9c8d767879e4559c9f53737bd786eb3877d)
- Fix the cache directory configuration of ccache on Ubuntu 22.04 so that it works properly in CI.
  ↳ No PR: [ef2535d](https://github.com/DPDK/dpdk/commit/ef2535d022b9ee53467f7ae80018ab62edd8b0b1)
- In the build configuration of the member library, use the public AVX512 compilation flag variable to simplify and unify the flag settings of different compilers.
  ↳ No PR: [7da47be](https://github.com/DPDK/dpdk/commit/7da47bee27788e2564b7cac63aa1964494523f47)
- Switch the DPDK warehouse address referenced in CI from dpdk.org to the GitHub mirror to solve the problem of random access failures.
  ↳ No PR: [860019b](https://github.com/DPDK/dpdk/commit/860019bd4c804cba4265dfe007fa5b9b282f5fcc)
- Removed the -fno-asynchronous-unwind-tables compiler flag that is no longer required when compiling the Intel network card driver with MinGW.
  ↳ No PR: [03cb7b3](https://github.com/DPDK/dpdk/commit/03cb7b3fda380e523927ee7f5accaba249cbe50c)

### Maintenance
- Fixed format differences between the e1000 driver and internal shared code, involving comments, indentation, whitespace, brackets, definitions and redundant fall-through comments.
  ↳ No PR: [64bb32f](https://github.com/DPDK/dpdk/commit/64bb32fa87d5250555ee62733ba17c310566b182)
- Remove non-inclusive language in e1000 shared code, replacing terms such as master/slave with primary/secondary.
  ↳ No PR: [f792bee](https://github.com/DPDK/dpdk/commit/f792bee8c64d12f85c4acf01ad9aafa1daacfb5a)
- Add error log and hexadecimal dump functions to zsda driver to enhance internal debugging capabilities.
  ↳ No PR: [790e2bb](https://github.com/DPDK/dpdk/commit/790e2bb72a79abe99289ce7b6f01e70b89c2eee1)
- Improved e1000 PHY debug printing, using decimal numbers and outputting actual values.
  ↳ No PR: [cb9b3dd](https://github.com/DPDK/dpdk/commit/cb9b3dda6da76fe19a32ca6aaf44f40efdaa28f1)
- Improved NVM checksum processing: when NVM is read-only and the checksum is invalid, the checksum is no longer updated and only debugging information is recorded.
  ↳ No PR: [5241c17](https://github.com/DPDK/dpdk/commit/5241c17f0d7fbc39047d431b0646e897826f8d7b)
- Add return value checking for bonding device promiscuous mode operations, and log errors in case of failure.
  ↳ No PR: [2b91fa5](https://github.com/DPDK/dpdk/commit/2b91fa5f70dd3f86ac7e03f7f6e1556117e38e2c)

### Others
- Fixed IV length configuration for AES-CTR 192/256 algorithm in IPsec example.
  ↳ No PR: [7e2a7c3](https://github.com/DPDK/dpdk/commit/7e2a7c336737084d8d8ef89260e511ff5670edbf)
- Updated the snapshot generation date in the ixgbe base driver README.
  ↳ No PR: [737a7c8](https://github.com/DPDK/dpdk/commit/737a7c83e0dd1ad6fd306d6ebe09d4d1c5f340e9)
- Reduce the level of logs related to global register updates in the i40e driver from WARNING to INFO.
  ↳ No PR: [7048ef4](https://github.com/DPDK/dpdk/commit/7048ef4409a0ac6f6ac1f01bd93c7a6af9b18b1b)
- Added documentation support for runtime context modules for DTS.
  ↳ No PR: [2efbcd1](https://github.com/DPDK/dpdk/commit/2efbcd1146157f3e754dc9753f5a8f02520aa20c)
- Upgrade the ENA network card driver version to 2.12.0.
  ↳ No PR: [379a64b](https://github.com/DPDK/dpdk/commit/379a64b407412e3be47f9849ffd3a13fd34cb8d7)
- Added comments in xsc_vfio_mbox.c to suppress PVS Studio's V1048 warning.
  ↳ No PR: [9965a37](https://github.com/DPDK/dpdk/commit/9965a375276df9a0f21748141d6cb76cfe541351)
