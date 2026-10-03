# Release Note

## Important Changes

### Cross-cutting / Other Architecture-related Changes
- Import VFIO header files from Linux v6.16 for use by DPDK modules. (Architecture event: Added VFIO UAPI module)
  ↳ No PR: [6201cbc](https://github.com/DPDK/dpdk/commit/6201cbc1f2d06880c0a543082b4c0d6b98bf1232)
- Remove the internal header files of multiple driver modules from the public API header file list, and only keep them in the driver SDK header file list to reduce the public API exposure scope. (Architecture event: Driver module internal header files are removed from the public API)
  ↳ No PR: [f8e03a6](https://github.com/DPDK/dpdk/commit/f8e03a6eb91c3c91196fcf1f3da5d6c8ad31ce54)
- The argparse library adds a custom help printing function, exposing the rte_argparse_print_help function and print_help callback. (Architecture-related: public API)
  ↳ No PR: [b9f5d20](https://github.com/DPDK/dpdk/commit/b9f5d20a6b7928b7a81ffb10c410b160ac9696ce), [47f5361](https://github.com/DPDK/dpdk/commit/47f5361af0292377dd4926dd37aa68c0f2b589fb)
- Added complete support for Wangxun Amber-Lite series network cards (10G/25G/40G), including device identification, mailbox interface, optical module identification, link configuration, PHY configuration, Rx/Tx support, hardware reset, FEC support and GPIO configuration. (Architecture-related: New network card driver series)
  ↳ No PR: [abf042d](https://github.com/DPDK/dpdk/commit/abf042d32b3947209a2cc9382d5689023885baa7), [6a139ad](https://github.com/DPDK/dpdk/commit/6a139ade82e7c320332df12ba830fc29da091781), [ab191e6](https://github.com/DPDK/dpdk/commit/ab191e6d9189b179251486aa2a7c6fc2b7cdd152), [06ff2da](https://github.com/DPDK/dpdk/commit/06ff2da39f572de58a51d0c41c3f4e03f0467e97), [fb6eb17](https://github.com/DPDK/dpdk/commit/fb6eb170dfa29667c036cce64b108389c8179999), [ead3616](https://github.com/DPDK/dpdk/commit/ead3616f630d2f50f0af3f404f0a2bb8f26a9ac3), [60b10df](https://github.com/DPDK/dpdk/commit/60b10df94a335742a632184cecbb8900b224af28), [e3a0d03](https://github.com/DPDK/dpdk/commit/e3a0d03ae17d5d2e86d74034889428875751f94a), [65bbae5](https://github.com/DPDK/dpdk/commit/65bbae51058f4a68aa238a18902604973697aa91), [a2d9260](https://github.com/DPDK/dpdk/commit/a2d92608d3b0710947e2eef50e9464f4026f4985), [83de5c1](https://github.com/DPDK/dpdk/commit/83de5c12f0033e5c8ef73c3f34f4783daffea2a0), [594e4cc](https://github.com/DPDK/dpdk/commit/594e4ccd81bf970be345482af3475a42764989c1)
- The Synchronous Streaming API document adds a number of usage restrictions, including tunnel offloading is not supported, rule configuration order requirements, matching field size restrictions, etc. (Architecture-related: public API usage restrictions)
  ↳ No PR: [0e42784](https://github.com/DPDK/dpdk/commit/0e42784c0a5711f7026e3ecae5a23481f36b2c86)
- Fixed the problem of passing a null pointer when passing an empty section name in the rte_cfgfile_num_sections function. Now when the sectionname is NULL, the number of all sections is directly returned. (Architecture-related: public API)
  ↳ No PR: [02bce2f](https://github.com/DPDK/dpdk/commit/02bce2f1e938b409bb6f85391510a2a33ecc1443)
- Fix the integer overflow problem when the highest bit is shifted left in the IPv4 address macro RTE_IPV4, and avoid undefined behavior through explicit type conversion. (Architecture-related: public API)
  ↳ No PR: [f1a544c](https://github.com/DPDK/dpdk/commit/f1a544c939f605dda0046b79fefdbb023a09dd37)
- Fixed an issue where AVX2 support was broken due to Meson builds, removed obsolete compile-time checks, and restored necessary header inclusion. (Architecture-related: Build and Platform Compatibility)
  ↳ No PR: [c367b9a](https://github.com/DPDK/dpdk/commit/c367b9a07c55025eabe1dd6903f4b0f5c4c5d362)
- Fix include guard in multiple header files and use RTE prefix namespace uniformly. (Architecture-related: public API)
  ↳ No PR: [77e85f1](https://github.com/DPDK/dpdk/commit/77e85f1ee5ca2bb1d6c913ac603b8fd387239021)
- Removed support for Linux kernel versions earlier than 3.17, and cleaned up related conditional compilation code. (Architecture-related: platform compatibility)
  ↳ No PR: [44dfa8a](https://github.com/DPDK/dpdk/commit/44dfa8a171095dd36516ac6b0fbbbec755cfb3b4), [0054e84](https://github.com/DPDK/dpdk/commit/0054e84040ba52a60c3bba18f782f787c4114b4b), [e110d5f](https://github.com/DPDK/dpdk/commit/e110d5fbe3335d831bfcdf5797bea5a78dad0e35)
- Replaced the DMA adapter operation structure rte_event_dma_adapter_op with rte_dma_op, and updated all functions, tests and driver codes that use this structure. (Architecture-related: public API)
  ↳ No PR: [77c552f](https://github.com/DPDK/dpdk/commit/77c552f9844eb55be2d627cddb8e3067e930adce)
- Removed v25 ABI compatibility, deleted old CRC API compatible symbols and default processing functions, and updated the public API to adapt to the new ABI version. (Architecture-related: ABI compatibility)
  ↳ No PR: [e3183a6](https://github.com/DPDK/dpdk/commit/e3183a6edafdc41bfd71de1517f9e9ec85eb1276)
- Removed the deprecated queue statistics field from the rte_eth_stats structure, added the eth_queue_stats parameter to the driver to continue to provide queue statistics, and deprecated the queue statistics mapping API. (Architecture-related: public API)
  ↳ No PR: [58ae742](https://github.com/DPDK/dpdk/commit/58ae74244c903171a4b55aadc87f495b15b0293e), [2863cbd](https://github.com/DPDK/dpdk/commit/2863cbd9ee6dabee2b183382d298f4054ba3e8a2)
- Fixed the compilation problem of bbdev test on Windows, removed variable-length arrays, used alloca or constant arrays instead, and added rte_os_shim header file to support getline function. (Architecture-related: platform compatibility)
  ↳ No PR: [7c7189c](https://github.com/DPDK/dpdk/commit/7c7189c4b82440f2de5b9f2328a9c6fed91d92de)
- Updated the mlx5 driver documentation to clarify the support scope of software steering and hardware steering. (Architecture-related: platform compatibility)
  ↳ No PR: [c289235](https://github.com/DPDK/dpdk/commit/c289235808a1661d7255acf888247d56f2f7d143)
- Added the constant time memory comparison function rte_memeq_timingsafe, and replaced memcmp in the authentication verification operation of the ipsec-mb driver to enhance protection against timing side channel attacks. (Architecture-related: public API)
  ↳ No PR: [05bd97b](https://github.com/DPDK/dpdk/commit/05bd97b943767b41a0978fe90c5a6fc279275fa1), [f15575a](https://github.com/DPDK/dpdk/commit/f15575af65c3ede008ecf89665a265fd2793b6ec)
- Added support for RISC-V V extension, which can be enabled through the -Dcpu_instruction_set=rv64gcv option, and the machine parameter configuration can be adjusted accordingly. (Architecture-related: platform compatibility)
  ↳ No PR: [7076aee](https://github.com/DPDK/dpdk/commit/7076aee1385a8347090a79ed4a35d498cea96950)
- Start the 25.11.0-rc0 release cycle, upgrade the ABI version to 26.0, remove the ABI exception list, disable ABI compatibility checking in CI, and create an empty release notes document. (Architecture-related: version and compatibility)
  ↳ No PR: [3e83e07](https://github.com/DPDK/dpdk/commit/3e83e07d7cdce5e7c3d7a080035be6e64db4c995)
- Added support for Microsoft Azure Cobalt-100 SoC in ARM build configuration. (Architecture-related: Platform compatibility)
  ↳ No PR: [defbb8c](https://github.com/DPDK/dpdk/commit/defbb8c709de937064f554ef704768300ede7d79)
- Enable crypto extension for ARM Cortex-A78AE configuration, fix the infinite loop problem of cryptographic performance test caused by the lack of this extension. (Architecture-related: platform compatibility)
  ↳ No PR: [6e6cc1d](https://github.com/DPDK/dpdk/commit/6e6cc1dc3548fc862cea377c98d7feef1a335468)
- Fix Windows build issues: remove variable-length arrays, replace strsep with strtok_r, remove thousands separators in printf, incorporate this test into Windows builds, and add the --query-rate command line option. (Architecture-related: platform compatibility)
  ↳ No PR: [211f166](https://github.com/DPDK/dpdk/commit/211f1660212809640003eb83664d4fbaa01e1a2a)
- Removed the deprecated enable_kmods build option, kernel modules are now built by default. (Architecture-related: build and installation methods)
  ↳ No PR: [ffba07b](https://github.com/DPDK/dpdk/commit/ffba07ba40cdaa6f8c2c98b79d058fa2eb1d1d2f)
- Add rv64gcv cross-compile target for RISC-V, and update cross-build guide to support vector extensions. (Architecture-related: Platform compatibility)
  ↳ No PR: [2e22572](https://github.com/DPDK/dpdk/commit/2e22572b9a6ce8bcdc0347313a35bb3066b0faff)
- Add link compatibility checks for libraries returned by meson find_library in the build system to avoid build failures due to architecture mismatch and other issues. (Architecture-related: build and installation methods)
  ↳ No PR: [0681e15](https://github.com/DPDK/dpdk/commit/0681e15f42df52739eda3a38a5f5e40d8ccc2784)
- Reconstruct the header file installation logic, centralize scattered install_headers calls into meson.build for unified processing, fix the problem that some driver and architecture header files are not checked, and update the checkpatches script to prohibit direct calls to install_headers. (Architecture-related: build and installation methods)
  ↳ No PR: [3fabb9c](https://github.com/DPDK/dpdk/commit/3fabb9c36291d57cb68fb2f1163985bf0e31bd5b)
- Added the RTE_EXEC_ENV_NAME macro definition in the Meson build system, which is used to identify the current execution environment name and update related documents. (Architecture-related: build and installation methods)
  ↳ No PR: [d81eec2](https://github.com/DPDK/dpdk/commit/d81eec2500afac10157b07ba85f68a036d58f90e)
- Enable NUMA support for Neoverse N2 configuration. (Architecture-related: Platform compatibility)
  ↳ No PR: [6edcec2](https://github.com/DPDK/dpdk/commit/6edcec237e31fcdb848cca6c151ee7a5bf057c28)
- Added support for HiSilicon HIP12 platform in ARM build configuration. (Architecture-related: platform compatibility)
  ↳ No PR: [a054de2](https://github.com/DPDK/dpdk/commit/a054de204b0b937dd976d0390fbb03353745e7cb)
- Updated the build configuration of Microsoft Azure Cobalt 100 SoC to adopt CPU-specific mcpu values supported by GCC 14+ and add crypto feature support. (Architecture-related: Platform compatibility)
  ↳ No PR: [2f3b51d](https://github.com/DPDK/dpdk/commit/2f3b51da38b20e09e890cdddb9a0caf05c7fb716)

### Poll-Mode Drivers (PMDs)
- Added Nebulamatrix network card driver, including basic PMD code, hardware layer, channel layer, resource layer, dispatch layer, device layer and device initialization and de-initialization support. (Architecture-related: Added Nebulamatrix network card driver)
  ↳ No PR: [00f5317](https://github.com/DPDK/dpdk/commit/00f53174e455ae4a29a1fd385ac85dbe6836595b), [5309aab](https://github.com/DPDK/dpdk/commit/5309aab4d8dc5cb362dd4725fc59e16a4d2b116a), [a1c5ffa](https://github.com/DPDK/dpdk/commit/a1c5ffa13b2c05bc0d27134890db12e2fa2c0759), [c2d6a1b](https://github.com/DPDK/dpdk/commit/c2d6a1b7a491791395de40d159268fb73375806d), [5af3800](https://github.com/DPDK/dpdk/commit/5af3800384b09e8d0ad8d7faee30b5a41f4ed49d), [603cac5](https://github.com/DPDK/dpdk/commit/603cac5c8d7260860fc52684d5b78edf0c782441), [bf64905](https://github.com/DPDK/dpdk/commit/bf649059c5ea5f515bd63192ac7c588555a1e9f2)
- Remove the PTP hardware identification code in the RX callback and use timesync API to support IEEE 1588. (Architecture-related: public API)
  ↳ No PR: [6cc1246](https://github.com/DPDK/dpdk/commit/6cc1246b3b1a751a1361d742f051e34cf96daec6)
- Reconstruct the DPAA bus driver, add FMan node support, provide SoC version identification internal API, migrate the push queue configuration from PMD to the bus driver, and add a new bus level interface. (Architecture-related: DPAA bus driver reconstruction)
  ↳ No PR: [0095306](https://github.com/DPDK/dpdk/commit/0095306cdbda8e576252cbdc260c290cd96b3bac), [164e9e1](https://github.com/DPDK/dpdk/commit/164e9e13e50f2e931bcca9804f0e442239245091), [fdacaec](https://github.com/DPDK/dpdk/commit/fdacaece350bed8fd87c6a05ebf9c6e201604b84)
- Add detection of AVX512DQ CPU flag in x86 vector capability check to meet Rx path selection requirements of idpf and cpfl drivers. (Architecture-related: Platform compatibility)
  ↳ No PR: [f26580f](https://github.com/DPDK/dpdk/commit/f26580f5343d793d3b1402b0f76987047e5f3065)
- Clean up the fslmc bus driver, remove cryptodev and dmadev pointers, move the device de-initialization logic from the removal function to the shutdown function, and instead obtain the device object through the function. (Architecture-related: fslmc bus driver interface cleanup)
  ↳ No PR: [29a4d53](https://github.com/DPDK/dpdk/commit/29a4d5307f1ce28f6c591c7eba2afc786e2fd089), [868a3ab](https://github.com/DPDK/dpdk/commit/868a3abd0ee5f10af6d0b9ee6b547b4c1405d723)
- The ICE driver main process unifies the Rx path, and all processes use the same receiving path. (Architecture-related: ICE driver Rx path unifies)
  ↳ No PR: [197e70f](https://github.com/DPDK/dpdk/commit/197e70fb89615f170b543f2d3d8d9e1fa6a17301)
- Adjusted CPTR alignment from 128 bytes to 256 bytes on CN20K platform, and dynamically allocated security context and IPsec SA structures. (Architecture-related: Platform compatibility)
  ↳ No PR: [b2d456e](https://github.com/DPDK/dpdk/commit/b2d456efd0763d06bd41b9e4368a7bbab2d11be2)
- Add CPT completion queue (CQ) support to the CN20K platform, enable/disable CQ when the device starts/stops, and adapt queue pair related logic. (Architecture-related: Added CQ support)
  ↳ No PR: [4e8a41a](https://github.com/DPDK/dpdk/commit/4e8a41acaffb0e96bfdd65e4b0c31d2cee6460dc)
- Add UIO/VFIO support for NBL devices, and add PCI device mapping and unmapping operations in the initialization and removal process. (Architecture-related: platform compatibility)
  ↳ No PR: [f19dae0](https://github.com/DPDK/dpdk/commit/f19dae073a165692f5068114dfc4ae9031db731d)
- Add coexistence mode support for NBL devices to implement user device DMA mapping, VFIO container management and channel initialization. (Architecture-related: coexistence mode support)
  ↳ No PR: [dc955cd](https://github.com/DPDK/dpdk/commit/dc955cd24c8f2ee45ad879592302f293c1cbad78)
- Add basic ethdev configuration support for NBL network devices to implement device status management and configuration process. (Architecture-related: Added ethdev support)
  ↳ No PR: [93b38df](https://github.com/DPDK/dpdk/commit/93b38df5a2ecc1b81b17ca004470dc0a8755a6bb)
- Remove the repr_matching_en device parameter in the mlx5 driver, and clean up related code logic. (Architecture-related: public API changes)
  ↳ No PR: [c41f621](https://github.com/DPDK/dpdk/commit/c41f621786ff2892ac3504368c966230a41acda3)
- Added vCPF PMD support, including registration, configuring queues, obtaining absolute queue ID and VSI information, and updating PCI ID table. (Architecture event: ACPI_CPUFreq_Power module removed)
  ↳ No PR: [63393cd](https://github.com/DPDK/dpdk/commit/63393cd7ac6d238525c02c1445547c8d66726d1c), [fa3225f](https://github.com/DPDK/dpdk/commit/fa3225fd0dd4effc19a3d3cbde59b2b97ec04820), [f1ab44f](https://github.com/DPDK/dpdk/commit/f1ab44fb0ebff2d6e3fc57898c5b7d071898c7bb)
- Introduced ENETC4 PMD driver to support PF and VF hardware initialization and basic network operations of multiple NXP SoCs. (Architecture event: BBDev_Main module removed)
  ↳ No PR: [a7fc52f](https://github.com/DPDK/dpdk/commit/a7fc52fcadb103ecd652ce69f5cd599c2bf9eea0)
- Add hot upgrade support to the bnxt driver, including global ID dynamic allocation, TCAM priority update, multi-instance coexistence, dynamic UPAR support, meter statistics and global index table processing functions. (Architecture event: BNXT driver core module extension)
  ↳ No PR: [3ed6fb5](https://github.com/DPDK/dpdk/commit/3ed6fb5edc8ef8faa67812f20ae6d9cb9a5d8dc1), [e3bbf02](https://github.com/DPDK/dpdk/commit/e3bbf020d03d5636dec533d154056e393c17c2b2), [8bce770](https://github.com/DPDK/dpdk/commit/8bce77045abc910d271bca7ee2519c782564e198), [19ddba0](https://github.com/DPDK/dpdk/commit/19ddba000baaf34944d7f77379e02249a40ee7d5), [83133e2](https://github.com/DPDK/dpdk/commit/83133e29bc2825ec457646d0ffcd8255c1874ca5), [eeefaec](https://github.com/DPDK/dpdk/commit/eeefaecba00027fc6522a6f7e966a5ebc445da3f), [93d62d0](https://github.com/DPDK/dpdk/commit/93d62d01ed0cbc5f247e7b0215b68a638b895b39), [c56bb3f](https://github.com/DPDK/dpdk/commit/c56bb3fc3c3ef5b51d8ee6fea8ea82e91233b161), [1d63159](https://github.com/DPDK/dpdk/commit/1d63159261ed2bf75647c706745ad422009fb8ca), [b3c8586](https://github.com/DPDK/dpdk/commit/b3c85863f219ff206a35a50f49bbe0e2a0c1cec3)
- Added DMA enqueue/dequeue operation API based on struct rte_dma_op, which needs to be enabled through the RTE_DMA_CFG_FLAG_ENQ_DEQ flag during configuration, and the operation must be implemented in the cnxk driver. (Architecture-related: public API)
  ↳ No PR: [9674119](https://github.com/DPDK/dpdk/commit/9674119fbf27171311c9295a8482a57fc58deaa3), [f0d9791](https://github.com/DPDK/dpdk/commit/f0d9791451217fb2048c331986bb393e48552e81)
- Implement the rx/tx queue information acquisition callback for the virtio network card, so that the application can obtain the queue size set by the vhost backend to correctly configure the memory pool. (Architecture-related: public API)
  ↳ No PR: [5faa599](https://github.com/DPDK/dpdk/commit/5faa599b2a6c987a2b01e34e411092462f9bd010)
- Obtain and store the DPNI API version during the DPNI device initialization phase, so that the available API can be selected based on the version later. (Architecture-related: public API)
  ↳ No PR: [091616d](https://github.com/DPDK/dpdk/commit/091616db91a59e332867edbbe447f3765e5a7d1c)
- Support VLAN TPID setting, add corresponding API and message processing callback, and fix logical errors in VLAN offload setting. (Architecture-related: public API)
  ↳ No PR: [a13c549](https://github.com/DPDK/dpdk/commit/a13c5490193002dcfb60935da29f880cdef95620)
- Support I510/511 PF device, add device ID recognition and adjust the initialization process. (Architecture-related: public API)
  ↳ No PR: [752ebb3](https://github.com/DPDK/dpdk/commit/752ebb371ded7eec4ccdfc192d1c9475039df9a9)
- Add a callback notification mechanism to the graph in scheduling mode, and trigger a callback when a data packet is enqueued into the work queue, so that the application can sleep/wake up. (Architecture-related: public API)
  ↳ No PR: [16f4c52](https://github.com/DPDK/dpdk/commit/16f4c522003dcfecf23c8d38e009b95a3bbefd03)
- Add configurable XDP program attachment mode to AF_XDP PMD, add vdev parameter mode, support drv, skb and hw modes. (Architecture-related: PMD configuration interface)
  ↳ No PR: [41756f2](https://github.com/DPDK/dpdk/commit/41756f243f46c769886accae308478303d3252d1)
- Added support for 800G link speed in the ethdev library, tests, drivers and command line tools. (Architecture-related: public API)
  ↳ No PR: [b671608](https://github.com/DPDK/dpdk/commit/b671608495d95b2b51487bdb8f5f4b32ca5c7d99)
- Added a new general function in the Intel network card driver for selecting SSE, AVX2 or AVX-512 code paths based on user configuration and CPU characteristics, and added checking of the AVX512DQ flag. (Architecture-related: platform compatibility)
  ↳ No PR: [15a25e3](https://github.com/DPDK/dpdk/commit/15a25e3858b9daf4722411198302caf2e1092413)
- Introducing the Rx path selection infrastructure for the Intel network card driver, adding a new structure and path selection function describing Rx path characteristics. (Architecture-related: Rx path selection API)
  ↳ No PR: [9d99641](https://github.com/DPDK/dpdk/commit/9d99641d80a08da4629c0af60cd66b3a83650760)
- Added support for SM2 elliptic curve asymmetric encryption: Add elliptic curve point fields and capability enumerations to the cryptodev public header file, and implement encryption and decryption operations in QAT PMD. (Architecture-related: SM2 encryption API)
  ↳ No PR: [a2ae984](https://github.com/DPDK/dpdk/commit/a2ae9848360ac834e8ad8209e260ce3a3763e8bb), [80b3362](https://github.com/DPDK/dpdk/commit/80b336214c65e504f6afdb9051930dec1cff548b)
- Add driver event callback API for mlx5 PMD, supporting external registration callbacks to listen to Rx/Tx queue creation and destruction events. (Architecture-related: public API)
  ↳ No PR: [ed26f93](https://github.com/DPDK/dpdk/commit/ed26f937e5902a6c7c929137e6519560a2c7fb9c)
- Added rte_pmd_mlx5_driver_disable_steering() and rte_pmd_mlx5_driver_enable_steering() private APIs for mlx5 PMD, allowing applications to enable or disable flow rule processing. (Architecture-related: public API)
  ↳ No PR: [6fafb11](https://github.com/DPDK/dpdk/commit/6fafb11d410f7197850c19bde6ad53c2de4e8ab9)
- Add NUMA awareness configuration to netvsc, and add the device parameter numa_aware to control whether it is enabled, which is not enabled by default. (Architecture-related: configuration interface)
  ↳ No PR: [311d3e9](https://github.com/DPDK/dpdk/commit/311d3e9ad0b1ba7ce35aded08853af50440b1122)
- Add rte_flow API support to the zxdh network card driver to implement ETH, VLAN, IPv4/IPv6, TCP/UDP, VXLAN and other matching as well as drop/count/mark/queue/rss and VXLAN encapsulation/decapsulation actions. (Architecture-related: public API)
  ↳ No PR: [d0af48c](https://github.com/DPDK/dpdk/commit/d0af48c1b9525894a8f12895ee62f0bcaf70bc7c)
- Added the link_state_on_close device parameter to the ice driver, which supports configuring the link state to down, up or restore to the initial state when the device is closed, and changes the default behavior from restoring the initial state to setting the link to down. (Architecture-related: configuration interface)
  ↳ No PR: [4159ea6](https://github.com/DPDK/dpdk/commit/4159ea62922ce41566c7bab44655ad78bee85458)
- Added TCP Segmentation Offload (TSO) support to xsc PMD, the send queue creation function has been adjusted accordingly to pass the offload flag and socket ID. (Architecture-related: public API)
  ↳ No PR: [7bd566e](https://github.com/DPDK/dpdk/commit/7bd566e1e920ee0f94bd81810362cb5ac7ccc4ec)
- Supports querying and reading EEPROM data of SFP/QSFP modules. (Architecture-related: public API)
  ↳ No PR: [53b2c2c](https://github.com/DPDK/dpdk/commit/53b2c2cbe0252cf6f42c79e398698c8fb5c7a562)
- Added link status acquisition and setting functions to the XSC network card driver, and added interrupt processing to support link status change notification. (Architecture-related: public API)
  ↳ No PR: [b2cbd3a](https://github.com/DPDK/dpdk/commit/b2cbd3ac0338afeffe31179173c4db26096a3728)
- Added VFIO MSI-X interrupt support for xsc network devices, and implemented the processing of link status change events. (Architecture-related: public API)
  ↳ No PR: [433506e](https://github.com/DPDK/dpdk/commit/433506e676031ac84f1dc9057652510c309a972a)
- Added FEC mode acquisition and setting functions to xsc PMD, and added support for interrupt event acquisition and interrupt processing installation/uninstallation. (Architecture-related: public API)
  ↳ No PR: [4a58617](https://github.com/DPDK/dpdk/commit/4a586179cc19324483a3f12b7ca19a294a223521)
- PCT manager now supports independent management of resources for each port, allowing different ports to run in independent DPDK processes. (Architecture-related: module responsibility)
  ↳ No PR: [eb8f97f](https://github.com/DPDK/dpdk/commit/eb8f97f6bf9300bdda4baf503d7732906ccd5e85)
- Added 40G port speed option support for ice driver. (Architecture-related: public API)
  ↳ No PR: [2203508](https://github.com/DPDK/dpdk/commit/2203508145df5391b6d414efc2bfc667d4b0b87e)
- Added hinic3 network card driver, supporting SP series network cards, including basic header files, hardware interface, command queue, event module, AEQ, management module, hardware operation, NIC configuration, work queue, mailbox, device initialization, ethdev operation, sending and receiving packets and other complete functions. (Architecture-related: New driver: hinic3)
  ↳ No PR: [5e67331](https://github.com/DPDK/dpdk/commit/5e673313d8729372afafa67e50b1ac2fef4c671e), [3a04760](https://github.com/DPDK/dpdk/commit/3a047601c4b0d52e7a08d71d01878cc10601aa14), [256d798](https://github.com/DPDK/dpdk/commit/256d798d081c6dd246f65af1e1034fdcca4f4e4a), [925eb5e](https://github.com/DPDK/dpdk/commit/925eb5ebccc7ee6e5e663fce119f823fb4a9af1d), [ba7f9bd](https://github.com/DPDK/dpdk/commit/ba7f9bd628e2d3268c656323355f30951602b00d), [14e369e](https://github.com/DPDK/dpdk/commit/14e369e154b3e3ec136a906b65af5e996e01adc6), [855caf8](https://github.com/DPDK/dpdk/commit/855caf8f9eb0f6d3a90ca53abdde1b46f164f9ec), [de49021](https://github.com/DPDK/dpdk/commit/de490215f74a02844930bdbe54bac9c5445e8599), [eea8db8](https://github.com/DPDK/dpdk/commit/eea8db85acfb54880467e64c671592f60af747ed), [bdc43c2](https://github.com/DPDK/dpdk/commit/bdc43c2b3ab597f1a76dedaa6ec3a77c7460fd31), [b2009dd](https://github.com/DPDK/dpdk/commit/b2009dd36f0ac62700bf9cacc267c3d39905350e), [7608f03](https://github.com/DPDK/dpdk/commit/7608f0367d5afed7ef5580c8447069206797ffb3), [4683684](https://github.com/DPDK/dpdk/commit/468368457681f63ddf3a3b60787157e257b7304c), [6894d84](https://github.com/DPDK/dpdk/commit/6894d844597a049b7b95ddab331faf5cf40df23a), [3774b96](https://github.com/DPDK/dpdk/commit/3774b9630d5b5aef319c6d01f0447fce47d56eed)
- Updated the event device queue weight mapping for the CN20K platform, mapping DPDK's 0-255 weight range to the hardware-supported 1-255. (Architecture-related: platform compatibility)
  ↳ No PR: [0237c06](https://github.com/DPDK/dpdk/commit/0237c06b95695f1f7f862917ee13267fd5bc5c8f)
- Added RSS hash update, configuration acquisition, RETA update and query, and multicast address list setting functions to the hinic3 network card driver. (Architecture-related: public API)
  ↳ No PR: [5ba81b4](https://github.com/DPDK/dpdk/commit/5ba81b43edb187f840612a4d4ceb439b42010cfe)
- Added flow control and filter support to hinic3 driver, including rte_flow, ethertype, IPv4, IPv6 and VXLAN tunnel filtering, and supports users to add or delete filters. (Architecture-related: public API)
  ↳ No PR: [efa3b9b](https://github.com/DPDK/dpdk/commit/efa3b9b36fc71a9b88d601b8503a98f6fc105ebe)
- Support configuring the CPT context length through the devarg parameter ctx_ilen, and use this value when creating IPsec and TLS sessions. (Architecture-related: public API)
  ↳ No PR: [a644620](https://github.com/DPDK/dpdk/commit/a644620ac458c68de46d1c95d6c01b511ec36d09)
- Added API rte_pmd_cnxk_ae_fpm_table_get, used to obtain the AE FPM table address. (Architecture-related: public API)
  ↳ No PR: [a1b4cc3](https://github.com/DPDK/dpdk/commit/a1b4cc32591db917f7f7fefb73baee55c231aad1)
- Added a new API to obtain the AE EC group table address, and added a compile-time enumeration value consistency check. (Architecture-related: public API)
  ↳ No PR: [53ff25b](https://github.com/DPDK/dpdk/commit/53ff25b1086b1fb1482543d8228507b79055fd9d)
- Aligned with the latest firmware for PDCP API, added metadata support and added null pointer check in multiple cryptographic operation functions. (Architecture-related: public API)
  ↳ No PR: [615e08f](https://github.com/DPDK/dpdk/commit/615e08f2f991c1ed33dd2bf745f5025a34ad646b)
- Added support for custom metadata in cn20k PMD, and modified related encryption preprocessing functions to pass metadata parameters. (Architecture-related: public API)
  ↳ No PR: [584531c](https://github.com/DPDK/dpdk/commit/584531cd03100125416529a27e30653c93af06b0)
- Added DCB enhancements to the ice network card driver, including tool functions, configuring flow control parameters by traffic category and asymmetric PFC support. (Architecture-related: public API)
  ↳ No PR: [a7153a9](https://github.com/DPDK/dpdk/commit/a7153a9070820b382532427314e43764978541e8), [c44109e](https://github.com/DPDK/dpdk/commit/c44109e125271c699051b04f66ca116a900c3e1a), [a0e3f9b](https://github.com/DPDK/dpdk/commit/a0e3f9bb6d8b40b6a037c8670c91a5ddb4f4f4ea), [edb3277](https://github.com/DPDK/dpdk/commit/edb3277794b82b3d6066c22a0e2f14004126806e)
- Added packet vector support to the CN20K encryption adapter, and restructured the enqueuing and dequeuing logic to use the new vector processing method. (Architecture-related: public API)
  ↳ No PR: [78c0791](https://github.com/DPDK/dpdk/commit/78c079160866c8bac6885e678ddcf229240ba9bf)
- Added PQC ML-KEM and ML-DSA algorithm support to cryptodev library and OpenSSL driver. (Architecture-related: public API)
  ↳ No PR: [bd3745e](https://github.com/DPDK/dpdk/commit/bd3745e2906520248c9480a827dbac0407134b8e), [5f761d7](https://github.com/DPDK/dpdk/commit/5f761d7b605ecce355a9e638abea5a05195104c8), [76a5877](https://github.com/DPDK/dpdk/commit/76a5877072c06f39be41e5abf13fec282fc78411)
- The compressdev library adds a new PDCP checksum definition and supports dictionary parameters in deflate/inflate operations; zlib PMD implements corresponding support. (Architecture-related: public API)
  ↳ No PR: [72c6fcc](https://github.com/DPDK/dpdk/commit/72c6fcc184293cd1922e935b074a3cb4571bc879), [0dc314d](https://github.com/DPDK/dpdk/commit/0dc314debb22761ba0ef1d6c7bce8e3480bf12ee), [5688155](https://github.com/DPDK/dpdk/commit/568815516e88a88ae2a7ef2f90d650fe364aa131)
- The ice network card driver adds priority flow control (PFC) support and statistical functions, and related counters have been exposed through xstats. (Architecture-related: public API)
  ↳ No PR: [e10ba3e](https://github.com/DPDK/dpdk/commit/e10ba3e59d748fbeff7e8f3bd54930b2e9efd6f5), [0dc6971](https://github.com/DPDK/dpdk/commit/0dc6971eef9674368dae098d4c4fcc7aebd6d862)
- The IAVF driver adds a VF-initiated reset function, a new experimental API rte_pmd_iavf_reinit and the corresponding testpmd command. (Architecture-related: public API)
  ↳ No PR: [28a1a72](https://github.com/DPDK/dpdk/commit/28a1a72eac267ffdd43f048ab0403f98dcf24f8e)
- Added HiSilicon SoC accelerator DMA driver, including device detection, removal, control path operation and data path operation. (Architecture-related: new driver module)
  ↳ No PR: [5a9c32a](https://github.com/DPDK/dpdk/commit/5a9c32a89cc1dfe0ad9aff2e07d5637c66937196), [2557ad8](https://github.com/DPDK/dpdk/commit/2557ad8f8ab8f6bef41ff8ce7daaa82c08990204), [b58c443](https://github.com/DPDK/dpdk/commit/b58c4435eafd534914464a175d46a241052f6098), [8fe92b3](https://github.com/DPDK/dpdk/commit/8fe92b3ab24f2e408b31c4575ff9acc10b4b7f22), [8aa458f](https://github.com/DPDK/dpdk/commit/8aa458f1c44b9f6e73f75047aca77191dc79746f)
- The ENA network card driver adds Rx hardware timestamp support with nanosecond precision, which can be enabled by configuring the Rx offload flag. (Architecture-related: Added hardware timestamp support)
  ↳ No PR: [5bf30b4](https://github.com/DPDK/dpdk/commit/5bf30b41705a95578d515c50b04bafce75437b1d)
- MC firmware API compatibility upgraded to 10.39.0, adding dpbp notification setting and acquisition, dprtc clock offset reading and other APIs, and adjusting the dpdmux device creation reset flag and dpkg key configuration function parameter type. (Architecture-related: API compatibility upgrade)
  ↳ No PR: [2a3fdde](https://github.com/DPDK/dpdk/commit/2a3fdde14c2e432f3fef8368dc7d2edc96456d65)
- Added support for DPMAC counters in xstats, including adding functions to obtain MAC statistics and corresponding statistics setting logic. (Architecture-related: Added xstats statistics interface)
  ↳ No PR: [d1cdef2](https://github.com/DPDK/dpdk/commit/d1cdef2ab592f2806b731a48109735761a9b23e7)
- Add devargs parameter to DPAA2 network card to support discarding packets with parsing errors in hardware. (Architecture-related: devargs parameter)
  ↳ No PR: [e5b61d8](https://github.com/DPDK/dpdk/commit/e5b61d8e2f421683c6e86484fb83f4208d8461af), [407ce3e](https://github.com/DPDK/dpdk/commit/407ce3e5384bc643607c38fd2369e9b3a7483369)
- Added Rx/Tx queue configuration, start, stop and release APIs for ENETC4 devices, and implemented auxiliary functions such as statistics, RSS and mixed mode. (Architecture-related: public API)
  ↳ No PR: [6c9c5aa](https://github.com/DPDK/dpdk/commit/6c9c5aadc0e04fe7462d21302ab040816f13a8bf)
- Added L3 (IPv4, IPv6) and L4 (TCP, UDP) TX checksum offloading and RX checksum verification support to the enetc4 network card driver. (Architecture-related: public API)
  ↳ No PR: [8ac2b32](https://github.com/DPDK/dpdk/commit/8ac2b32c6799be22aaf80b2283a985d3eb735eca)
- Added basic statistical functions to ENETC4 PMD, supporting sending and receiving packets and byte counts as well as error statistics. (Architecture-related: public API)
  ↳ No PR: [394a615](https://github.com/DPDK/dpdk/commit/394a615719635b62d922d81dd1bc884669a4e5a7)
- Added packet type parsing support to ENETC4 PMD, and added multiple functions such as link update, promiscuous mode, queue start and stop, statistics acquisition and control BDR management. (Architecture-related: public API)
  ↳ No PR: [e4ff8ce](https://github.com/DPDK/dpdk/commit/e4ff8ce83746aee433dcbdef0ad6c4a506ffc313)
- Added a message passing mechanism between virtual function (VF) and physical function (PF) for the enetc network card driver, and supports VF to configure the main MAC address. (Architecture-related: public API)
  ↳ No PR: [b75b047](https://github.com/DPDK/dpdk/commit/b75b047928cb2be7dc9a134c7861e4aaae8b3142)
- Added multicast and promiscuous mode support to ENETC4 PMD, including corresponding callbacks and message processing for PF and VF. (Architecture-related: public API)
  ↳ No PR: [e6ca226](https://github.com/DPDK/dpdk/commit/e6ca226e8d5b5962a702709c8579b9594f59099e)
- Added link status acquisition, link speed acquisition and link update operations to the ENETC4 VF driver, and added VLAN promiscuous mode support. (Architecture-related: public API)
  ↳ No PR: [5cdfce5](https://github.com/DPDK/dpdk/commit/5cdfce527b07088710925c7edbd761b1e455fa9e)
- Added link status notification support for ENETC4 PMD, including link online and offline and speed change events. (Architecture-related: public API)
  ↳ No PR: [694b0a8](https://github.com/DPDK/dpdk/commit/694b0a814abcf2a0225c3d4f542cc01747864ab6)
- Added a new service management API to NTNIC PMD, supporting functions such as service addition, deletion, information query and lcore mapping. (Architecture-related: public API: NTNIC service management)
  ↳ No PR: [fb8d25c](https://github.com/DPDK/dpdk/commit/fb8d25ccbec4f0b92230fb51705c7965548e3ae4), [534e658](https://github.com/DPDK/dpdk/commit/534e6581e5ed8988f1efbd5e8fe00d202d2d46bc), [b281252](https://github.com/DPDK/dpdk/commit/b281252a55c1bbf64b966017ddb47544e3d4085e), [31f6679](https://github.com/DPDK/dpdk/commit/31f66794855c2464b8454f09aad6a3cb6cee04f7)
- Unified the Napatech hardware flow API function prefix from flow_ to nthw_flow_, and added the nthw_flow_pull_profile_inline function. (Architecture-related: public API)
  ↳ No PR: [5d1b2fb](https://github.com/DPDK/dpdk/commit/5d1b2fbb9c96b6f0802eb0e4c914f12b285cb1a8)
- Unify the key matcher function prefix in the flow_api module from km_ to nthw_km_, and add support for tunnel traffic in interpret_flow_elements. (Architecture-related: public API)
  ↳ No PR: [c847223](https://github.com/DPDK/dpdk/commit/c847223b77834dd8e751a55b2d3110723eb9f968)
- Support pattern matching for inner Ethernet headers, stream dump output displays both outer and inner L2 masks. (Architecture-related: public API)
  ↳ No PR: [7b0e437](https://github.com/DPDK/dpdk/commit/7b0e437071692965769f668ceed4f7287101d6e0)
- Supports matching of single or multi-layer nested internal VLAN headers, flow dump output prints both outer and inner VLAN masks. (Architecture-related: public API)
  ↳ No PR: [cf2fb93](https://github.com/DPDK/dpdk/commit/cf2fb937486a583eb6fa6a09f85943d46eae678e)
- Added flow pull support to the ntnic driver, implemented eth_flow_pull and related auxiliary functions. (Architecture-related: public API)
  ↳ No PR: [6ba15a5](https://github.com/DPDK/dpdk/commit/6ba15a5aa532d9812971464a77afe3f14f9d9db0)
- Added probe/remove function and log module to NBL network card driver, and implemented device information query function. (Architecture-related: NBL driver module)
  ↳ No PR: [88a433b](https://github.com/DPDK/dpdk/commit/88a433b341abdac278b9be969242726bd29501d2), [ff8db37](https://github.com/DPDK/dpdk/commit/ff8db3711b2906ad95ba2756bcc504de03ffa6a8)
- Added link status detection and notification functions to Amber-Lite VF, supporting correct reporting of link rates and notification of VF link status changes through PF mailbox. (Architecture-related: PF-VF mailbox communication)
  ↳ No PR: [16fd2df](https://github.com/DPDK/dpdk/commit/16fd2df8d95f319bcc68308afe479eef823641ae), [b42d6d5](https://github.com/DPDK/dpdk/commit/b42d6d5c1cf5e41f8c468b0556fba70936247b3b)
- The txgbe driver adds pkt-filter-size and pkt-filter-drop-queue device parameters to replace the deprecated FDIR configuration; automatically switches to the FDIR filter when the ntuple filter is full; the VF driver supports requesting PF configuration FDIR rules through the new mailbox API. (Architecture-related: public configuration interface and mailbox API)
  ↳ No PR: [7e18be9](https://github.com/DPDK/dpdk/commit/7e18be9beef25ee60f9c04f757cb4361706ff818), [ccac5e0](https://github.com/DPDK/dpdk/commit/ccac5e093041f255f38a59ea472c6dee493ccc7c), [7eef710](https://github.com/DPDK/dpdk/commit/7eef71080e1638c0a37b98cff44381265b651a36), [a443523](https://github.com/DPDK/dpdk/commit/a443523d6ddf076c422c9ed1460fb3a4c5c9a05b)
- The tap driver replaces the interface control from ioctl to Netlink, adds Netlink-based auxiliary functions, removes ioctl related code, and forces Netlink socket to be available. (Architecture-related: platform compatibility)
  ↳ No PR: [f13a2bb](https://github.com/DPDK/dpdk/commit/f13a2bb7e97b9f27dc65d008b61fb5bfd9dee04a), [b5d7663](https://github.com/DPDK/dpdk/commit/b5d76639551e5f04be0dbaaedc59202fb80bcede)
- Added support for MPLS protocol, realizing MPLS message parsing and packet loss, forwarding or queuing actions. (Architecture-related: MPLS protocol support)
  ↳ No PR: [98845d0](https://github.com/DPDK/dpdk/commit/98845d04f7c6daedefbfb63d01445553d0021b61)
- Added global table scope support for socket direct applications. Table scopes are divided into three types: global, shared application and non-shared. At the same time, the problem of repeatedly delivering firmware for configuration when DPDK is closed has been fixed. (Architecture-related: global table scope)
  ↳ No PR: [23e0dc6](https://github.com/DPDK/dpdk/commit/23e0dc62d19efadfe55dcb1b91cd940850406fda)
- Added support for GRE Key to the bnxt driver, and added a new GRE Key header parsing processing function. (Architecture-related: GRE Key support)
  ↳ No PR: [8b81af2](https://github.com/DPDK/dpdk/commit/8b81af210b63a744fdd6cdf9d424565f0a6101e7)
- Removed the early return for non-P5 chips in the promiscuous mode setting in the bnxt/tf_ulp driver to support the unicast-only function, so that the application port no longer receives broadcast, multicast and unknown MAC addresses. (Architecture-related: external behavior)
  ↳ No PR: [c9a3c92](https://github.com/DPDK/dpdk/commit/c9a3c921d0c391ccbecedb1b53d6b6b99b9c471d)
- Supports the transfer of stream metadata between E-Switch and VM, and the VM application can handle inbound and outbound stream metadata. (Architecture-related: public API)
  ↳ No PR: [a78425b](https://github.com/DPDK/dpdk/commit/a78425ba3793e3c836e98ffe5d8f975c6d412ccc)
- Added callback parameters for CPT LF's IRQ registration and deregistration functions, and added completion queue initialization, enablement, disabling and cleanup routines to support conditional skipping of IRQ operations. (Architecture-related: public API)
  ↳ No PR: [0ee6d16](https://github.com/DPDK/dpdk/commit/0ee6d162fc14c23207007501a8a07369dc676355), [13ce912](https://github.com/DPDK/dpdk/commit/13ce9121c3c0915bae420c7f7703e29338737c21)
- Added CPT CQ-based outbound soft expiration processing mechanism for CNXK network card, and added devargs support to enable this function. (Architecture-related: public API)
  ↳ No PR: [a7d64a7](https://github.com/DPDK/dpdk/commit/a7d64a7740e0d1287ecab047e1218cb3251cc5fd)
- Added support for ConnectX-9 SuperNIC devices in the mlx5 driver, including defining its PCI device ID and registering the device with encryption and network drivers, and updated related documentation. (Architecture-related: new hardware support)
  ↳ No PR: [1b55eeb](https://github.com/DPDK/dpdk/commit/1b55eeb7b76fc2a4abe1fedce2daba7be9ca1b7a), [075d654](https://github.com/DPDK/dpdk/commit/075d6543c4d0f614c79f8d7cc36461c5baa97fe0)
- Support the use of DevX bulk counters in root table rules and allow specifying offsets. (Architecture-related: public API)
  ↳ No PR: [21a82be](https://github.com/DPDK/dpdk/commit/21a82be177587143b02f3c3c1a5cb66216f3af50)
- Under the HW Steering engine, support the use of count and age flow actions in the root table (group 0). (Architecture-related: public API)
  ↳ No PR: [0cacbcd](https://github.com/DPDK/dpdk/commit/0cacbcd9e9595c1392629e151403b348917a2d50)
- Added the function of reading the software steering capability bit in the MLX5 public driver, which is used to detect whether the hardware supports software forwarding and prepare for disabling SWS in the future. (Architecture-related: platform compatibility)
  ↳ No PR: [53fdc23](https://github.com/DPDK/dpdk/commit/53fdc237df139bd439293b6dcfa09b9bf9b791b4)
- Added a new source-prune device parameter to the ice network card driver. Source MAC address pruning is disabled by default to support VRRP broadcast messages. Users can enable the source pruning function through this parameter. (Architecture-related: public API)
  ↳ No PR: [980c840](https://github.com/DPDK/dpdk/commit/980c840a646a2c8ae49a291c17baf20a74f36086)
- Support link mode configuration, including auto-negotiation, duplex mode and speed settings. Users can configure the port's working mode and speed through the link_speeds field in rte_eth_conf. (Architecture-related: public API)
  ↳ No PR: [00af659](https://github.com/DPDK/dpdk/commit/00af6596f17bebdcce3fe923fc93c920ff250f4f), [292fcbb](https://github.com/DPDK/dpdk/commit/292fcbb3d2906ae21954d9123936cec2a3ada042)
- Obtain port type, connector type and FEC statistics from firmware, enhance port information reporting, and report connector type in link status. (Architecture-related: public API)
  ↳ No PR: [8db7439](https://github.com/DPDK/dpdk/commit/8db7439568e906c4da73186b20cd055f595ea123), [94461a8](https://github.com/DPDK/dpdk/commit/94461a823cb7d5609af62e4fe9c600642090fac4)
- Added IOVA mode check in Linux coexistence scenario, forcing the use of IOVA=PA mode when IOMMU is in pass-through mode. (Architecture-related: platform compatibility)
  ↳ No PR: [a12f1ac](https://github.com/DPDK/dpdk/commit/a12f1acc7bc4a68e497baf1da235a77f7fcd6ff8)
- Added a traffic management tree to the SDP interface of the CNXK platform. When multiple Tx queues are requested, an independent tree is created to support independent backpressure of each queue. (Architecture-related: public API)
  ↳ No PR: [ee46024](https://github.com/DPDK/dpdk/commit/ee46024b5e067b45af3827d91496df83348f99a0), [33800b5](https://github.com/DPDK/dpdk/commit/33800b56d65fb5db8aadcb4a38982bb1e9ecb8ec)
- Expanded the LSO offloading function on the CN20K platform, added mailbox configuration alt flags and supported IPv4 fragmentation. (Architecture-related: public API)
  ↳ No PR: [c054608](https://github.com/DPDK/dpdk/commit/c054608c92e37c0b5c6cc90a6c3878a72738c706), [52123cc](https://github.com/DPDK/dpdk/commit/52123cc744c942b282e47320312a4035e31e2f4a)
- Added SQ count per-package update and SQ resize functions to the CNXK platform, and extended the SQ context to support dynamic expansion and contraction. (Architecture-related: public API)
  ↳ No PR: [141e9a8](https://github.com/DPDK/dpdk/commit/141e9a8a42bc5c802a0b3d252e51f784602c4883), [c993d8f](https://github.com/DPDK/dpdk/commit/c993d8fd5a3391197cf5104bf3d0a378e1268ba1)
- Added BlueField-4 DPU device ID support to mlx5 driver. (Architecture-related: Platform compatibility)
  ↳ No PR: [54fe337](https://github.com/DPDK/dpdk/commit/54fe33798a76d764cef628bc3b7c192e8c55ac98)
- Increase the maximum number of Tx schedulers from 1024 to 2048, support CN10K platform. (Architecture-related: platform compatibility)
  ↳ No PR: [9188d72](https://github.com/DPDK/dpdk/commit/9188d72b2143e7382aae12d22300f2542323389f)
- Fix exported header files so that they can be included alone without compilation warnings, such as adding conditional compilation protection for experimental APIs in rte_pmd_iavf.h. (Architecture-related: public API)
  ↳ No PR: [cae7430](https://github.com/DPDK/dpdk/commit/cae7430fcc712623ebbf52b0e8f232788a5e4679)
- Fixed the problem that the memory area mapping bit mask type in the vmxnet3 driver is too small, changed the index bit mask variable from uint8_t to uint16_t, and corrected the queue number check logic so that both RX and TX queues support up to 16 queues. (Architecture-related: public API)
  ↳ No PR: [387b6e0](https://github.com/DPDK/dpdk/commit/387b6e0cca4ebbb1d2f8c03da5b9d4051dfef913)
- Repair the RSS function in the ZXDH driver, expand the hash factor type from 32 bits to 64 bits, and improve the RSS enable/disable logic and configuration initialization process. (Architecture-related: public API)
  ↳ No PR: [a337a7a](https://github.com/DPDK/dpdk/commit/a337a7a118a51b952b004a56e1c2e82322e8f1a9)
- Fixed the reporting of the minimum and maximum MTU and maximum received packet length in mlx5 PMD, instead querying the actual allowed MTU range from the operating system, and the Windows platform uses the fallback value. (Architecture-related: platform compatibility)
  ↳ No PR: [44d6571](https://github.com/DPDK/dpdk/commit/44d657109216a32e8718446f20f91272e10575dd)
- Add the devarg parameter to the DPAA network card to control error packet reception, fix the problem of error queue causing crash in VSP mode, and adjust the timestamp enable logic and RX queue number check. (Architecture-related: devarg parameter)
  ↳ No PR: [5cea57f](https://github.com/DPDK/dpdk/commit/5cea57f804058d245e41bd8320a4075ba78cf889)
- Fixed the VLAN tag processing logic in the Intel network card driver (i40e, iavf, ice): it no longer assumes that the outer tag must exist, but correctly sets the QinQ or single VLAN tag according to the actual tag, thereby solving the double tag stripping problem under different VLAN protocol types. (Architecture-related: VLAN tag processing)
  ↳ No PR: [2116835](https://github.com/DPDK/dpdk/commit/21168355589ea9edfcb2925f4952ecb05470f92f)
- Fixed the problem that the GVE driver did not release all resources when the device was closed: moved the resource release logic from device removal to the device shutdown function, and reconstructed related steps. (Architecture-related: device shutdown process)
  ↳ No PR: [7ba8445](https://github.com/DPDK/dpdk/commit/7ba84453bacf7a8709f2aaf341e1d0b42d49a4c8)
- When using the port ID action in dv_flow_en=2 mode, an error will now be returned and prompted to use the representative port action instead, thereby preventing the action from being silently ignored. (Architecture-related: external behavior)
  ↳ No PR: [c040e9a](https://github.com/DPDK/dpdk/commit/c040e9a85a1fbce46528e9bc15d1ce4bbc911346)
- Fix the lock inconsistency problem in the rte_flow API of the hns3 driver: replace pthread mutex with spin lock, and remove the no longer needed pthread mutex attributes and redundant functions. (Architecture-related: public API)
  ↳ No PR: [d441169](https://github.com/DPDK/dpdk/commit/d441169bd20415691ea86707e7bf852eb6fcda46)
- Fix connection tracking state item validation to ensure only valid RTE_FLOW_CONNTRACK_PKT_STATE_* flag combinations are allowed. (Architecture-related: public API)
  ↳ No PR: [179e70f](https://github.com/DPDK/dpdk/commit/179e70fd7ad2027705b42e7416d436d299eca78c)
- Fixed flow mark creation problem: Use NOP to replace unsupported flow tag action in the FDB TX direction, and prohibit the use of mark in the transfer template, and create flow tags when FW does not support it. (Architecture-related: public API)
  ↳ No PR: [14a7676](https://github.com/DPDK/dpdk/commit/14a7676322892ec53736427b6c2a9ad587715e97)
- Fixed a crash caused by indirect AGE actions created using the synchronous API: use the current queue index allocation counter instead; also add validation for synchronous and asynchronous AGE action creation, and update the document; synchronous query aging flow is rejected in strict queue mode. (Architecture-related: external behavior)
  ↳ No PR: [8bc72d9](https://github.com/DPDK/dpdk/commit/8bc72d9f277593f6d8b27278bad3a5bb92e7347f)
- Fixed mbuf debugging flag support in Intel network card driver: unified use of raw allocation/release functions rte_mbuf_raw_free_bulk and rte_mbuf_raw_alloc_bulk. (Architecture-related: public API)
  ↳ No PR: [773cbaf](https://github.com/DPDK/dpdk/commit/773cbaf2ad38d9fd99133e282b9cd090783d4a44), [4913131](https://github.com/DPDK/dpdk/commit/491313189072260264049411b2dfe0f75220eb73)
- Fixed the problem of GVE driver DQ Rx supporting out-of-order completion: correctly match the returned buffer by introducing buf_id and completion list. (Architecture-related: public API)
  ↳ No PR: [1aed73b](https://github.com/DPDK/dpdk/commit/1aed73b23ac04690e586fc36126cdffaf92e1063)
- Add direction metadata to all exchange rules to prevent rules from accidentally matching Tx traffic; do not add rules that are close to the capacity limit because they are specific enough. (Architecture-related: public API)
  ↳ No PR: [2587226](https://github.com/DPDK/dpdk/commit/258722673e1e9017a84a25a30fb2a43c130e159c)
- Fixed the issue in the mlx5 driver where rte_eth_dev_get_mtu() returns the default MTU instead of the actual setting value: Correctly synchronize the MTU field during device initialization. (Architecture-related: public API)
  ↳ No PR: [ee6aa2c](https://github.com/DPDK/dpdk/commit/ee6aa2cb66512cd57b69ffe07efbd7f09789c9b2)
- Fix LTO build issues: Update the netlink attribute in the tap driver to add functions and related macros, and change the message structure pointer to be passed. (Architecture-related: build and installation methods)
  ↳ No PR: [adb95cc](https://github.com/DPDK/dpdk/commit/adb95cc6644103d055609f5bcae5df91afea02ab)
- Fixed an issue that may cause overflow when shadow RAM size is defined as 16 bits during NVM initialization: change it to 32 bits. (Architecture-related: public API)
  ↳ No PR: [96b1a23](https://github.com/DPDK/dpdk/commit/96b1a23f3ea5614e5795307295234c15e0e99a1e)
- Fix the calculation of used ring addresses in the virtio-user driver to prevent Vhost-vDPA backends (such as VDUSE) from failing in address translation. (Architecture-related: virtio-user driver)
  ↳ No PR: [7aa71d3](https://github.com/DPDK/dpdk/commit/7aa71d336c18bac0c942018819043a5420a5b160)
- Fixed the issue where vmxnet3 v4 RSS fails to write to the BAR register when configuring a single queue on ESX 8.0+: RSS is automatically disabled in a single queue scenario. (Architecture-related: platform compatibility)
  ↳ No PR: [9a21938](https://github.com/DPDK/dpdk/commit/9a219380b148c1837e54eb15cff501cba1ba842a)
- Correctly clean up the frame queue when the DPAA bus is closed: add a timeout mechanism and debug logs to prevent resource leaks and status abnormalities. (Architecture-related: public API)
  ↳ No PR: [0e3c389](https://github.com/DPDK/dpdk/commit/0e3c389b9e4fc1c98097c00ebe26c6a4350d4b0c)
- Added an interrupt control function in QMan global initialization, allowing users to disable invalid enqueue status interrupts through environment variables to avoid system freezes. (Architecture-related: runtime behavior)
  ↳ No PR: [aef9bc2](https://github.com/DPDK/dpdk/commit/aef9bc2f0a26db3cbe84a29204fbb5c6c745014b)
- Fixed the maximum number of VFs per PF on Thor2 to be 128, and fixed the problem of incorrect calculation of the number of hash table entries when the maximum number of VNICs is less than 8. (Architecture-related: public API: Maximum number of VFs)
  ↳ No PR: [7f88128](https://github.com/DPDK/dpdk/commit/7f8812820fa8064afef785017f07879d15bd158e)
- Correct the boundary check used to determine whether the action type is valid in flow action parsing: correct the upper limit from RTE_FLOW_ACTION_TYPE_INDIRECT to RTE_FLOW_ACTION_TYPE_REPRESENTED_PORT. (Architecture-related: public API)
  ↳ No PR: [a71659c](https://github.com/DPDK/dpdk/commit/a71659cca450dee1a45261154a3afce2dc7be598)
- Fixed external SQ control flow leakage problem: Added rte_pmd_mlx5_external_sq_disable() API, allowing applications to notify PMD to release related implicit flows to avoid flow table overflow after multiple device starts and stops. (Architecture-related: public API)
  ↳ No PR: [3bf9f0f](https://github.com/DPDK/dpdk/commit/3bf9f0f9f0beb8dcd4f3b316c3216a87bc9ab49f)
- In the DV flow engine, when the source field type is not VALUE or POINTER, the add and sub types of modify field operations are rejected, and the related documents are updated. (Schema related: External behavior: modify field operation restrictions)
  ↳ No PR: [17082f4](https://github.com/DPDK/dpdk/commit/17082f45e93697dcfbe056da7f90af90362cc6b2)
- Enable CPT completion queue (CQ) in outbound security processing and support reading error packets from CQ. (Architecture-related: public API: CPT completion queue)
  ↳ No PR: [b06f7bf](https://github.com/DPDK/dpdk/commit/b06f7bf120447977ae22cba10fd3ba1ddf7f8504)
- Fix Rx path selection logic: When two candidate paths have the same SIMD width, the path with less offloading function will be given priority; otherwise, the path with larger SIMD width will be given priority. (Architecture-related: Rx path selection logic)
  ↳ No PR: [8724a85](https://github.com/DPDK/dpdk/commit/8724a85b9a89ceb84371c3fda8156a8ec47602e3)
- Fix the bit offset processing of the IPv6 DSCP field in the HWS engine to ensure that the synchronous stream API sets the field correctly. (Architecture-related: public API behavior)
  ↳ No PR: [15501c4](https://github.com/DPDK/dpdk/commit/15501c4298ea029b4252b8194daa574d4e02df20)
- Fixed the problem of cross-GVMI metadata matching in E-Switch settings, and added cross-GVMI support check in metadata flow item processing. (Architecture-related: Core module: E-Switch metadata)
  ↳ No PR: [1c23465](https://github.com/DPDK/dpdk/commit/1c23465a9a34a59576165945a6905dbb4f956431)
- Downgraded MTU setting check from error to warning when SDP interface does not have hash offload enabled, to support scenarios where the host applies a known maximum buffer size. (Architecture-related: MTU setting behavior change)
  ↳ No PR: [d9a6291](https://github.com/DPDK/dpdk/commit/d9a6291f5a6442e6cfb215c7258ede755d4ebbaa)
- Fixed the support for the REG_C_8 to REG_C_11 registers in the root table flow tag index in the mlx5 driver, and changed the assertion of invalid tag index to return an error message. (Architecture-related: public API)
  ↳ No PR: [3087db1](https://github.com/DPDK/dpdk/commit/3087db16ab13cdd6996b1f3ea8c64171c2e8fd8f)
- Fixed the problem of hard-coded matching conditions when creating streams in the mlx5 driver on the Windows platform, using the match_criteria_enable attribute instead, and adding support for the NVGRE message type. (Architecture-related: platform compatibility)
  ↳ No PR: [e0b87fa](https://github.com/DPDK/dpdk/commit/e0b87fa079b9f35750f4d6fb71a00ab0ca19d170)
- Fix flex flow item header length, support new firmware capability bits, and adjust the calculation and configuration of length field offset accordingly. (Architecture-related: platform compatibility)
  ↳ No PR: [a223460](https://github.com/DPDK/dpdk/commit/a2234609bf7e4f5bb1ad8f6f60c5f574f32c3558)
- Add virtual VLAN offload configuration operation for nbl driver to avoid errors returned when software handles VLAN stripping. (Architecture-related: public API)
  ↳ No PR: [cde0d52](https://github.com/DPDK/dpdk/commit/cde0d5297dd22a7a766d9d56134cc3296e5f02a2)
- Fix Rx offload flag to use device configured Rx offload instead of hardcoded value when event port draining. (Architecture-related: external behavior)
  ↳ No PR: [3e48adc](https://github.com/DPDK/dpdk/commit/3e48adc13585eae2c2b03dbb9681577995c7e28a)
- Fixed the PCI BAR mapping error of the ena network card driver on 64K page size systems, and calculated the correct virtual address offset by adding a new helper function. (Architecture-related: platform compatibility)
  ↳ No PR: [c71e3fb](https://github.com/DPDK/dpdk/commit/c71e3fbee65637084e1e42500e9e6300d50f467b)
- Correct the TruFlow HSI structure definition in the bnxt driver, and add the correct packaging end tag to the relevant structure. (Architecture-related: ABI compatibility)
  ↳ No PR: [a06140b](https://github.com/DPDK/dpdk/commit/a06140b6b630f3cd382648a603aaa774ff834cd7)
- Removed the DPAA driver destructor, moved the cleanup logic to the bus layer, and improved error handling of multiple interfaces. (Architecture-related: Module responsibility changes)
  ↳ No PR: [78ea4b4](https://github.com/DPDK/dpdk/commit/78ea4b4fcb52f786aeb1c470c730ea3e54e239d5)
- Uniformly change the return type of the rx_queue_count callback function in each driver from uint32_t to int, avoiding unnecessary symbolic type conversion. (Architecture-related: public API)
  ↳ No PR: [8b1cd99](https://github.com/DPDK/dpdk/commit/8b1cd9911981caf5132a3542227b2cdee2daa4ee)
- Renamed and exposed the Rx queue mark flag setting and clearing functions so that they can be called later when flow control is turned off. (Architecture-related: public API)
  ↳ No PR: [9790a8d](https://github.com/DPDK/dpdk/commit/9790a8d360953ccaa8c37462a117e4c3f0097198)
- Reconstructed the RSS receiving queue creation process of XSC PMD, and introduced independent QPN allocation and release and queue information setting functions. (Architecture-related: public API)
  ↳ No PR: [3991c89](https://github.com/DPDK/dpdk/commit/3991c890fb4c4fc715c1b20fbae8c14ce7f9e411)
- Reconstructed the stop and close paths of xsc PMD to ensure the correct release of queue resources and removed the flag-based initialization tracking. (Architecture-related: public API)
  ↳ No PR: [7b23a07](https://github.com/DPDK/dpdk/commit/7b23a075266052210c320b506e053534637e0a75)
- Reconstructed the ice-driven RSS LUT selection function, using enumerations to specify LUT size and type, and optimized parameter passing and validation. (Architecture-related: public API)
  ↳ No PR: [68ee0a0](https://github.com/DPDK/dpdk/commit/68ee0a06185df63ea18cff5af4173a60ac2a3be1)
- Changed the return value of the doorbell writing function to void, and optimized the debugging log information. (Architecture-related: public API)
  ↳ No PR: [c9ed40d](https://github.com/DPDK/dpdk/commit/c9ed40dc10e2008ee70cdf0196bcc2673fc98948)
- Refactored the definition of rte_pmu_read inline function to exclude actual code and trigger runtime assertions through conditional compilation when the experimental API is not enabled. (Architecture-related: public API)
  ↳ No PR: [0b2255f](https://github.com/DPDK/dpdk/commit/0b2255fbfb13d403e791af9f2f8ae2d16762416e)
- Change the PMU architecture-specific operations from static functions to callback-based ops structures to make the architecture more modular and easy to expand. (Architecture-related: Architecture Reconstruction)
  ↳ No PR: [47eecb1](https://github.com/DPDK/dpdk/commit/47eecb1b73edcf200b5feb405fbd038ba007f27f)
- Removed automatic enabling of user space performance counter access in ARM64 PMU initialization, changed to record warning log, and renamed related functions. (Architecture-related: platform compatibility)
  ↳ No PR: [74925cf](https://github.com/DPDK/dpdk/commit/74925cf10725804d2f783308e21f876a9602bd42)
- Removed the mpc device parameter in the bnxt driver, mpc is enabled by default on the P7 platform, and the mpc=1 parameter is no longer supported. (Architecture-related: driver configuration)
  ↳ No PR: [d9c08be](https://github.com/DPDK/dpdk/commit/d9c08be1d7cff272341f27cb9d5d5e31014dd6e1)
- Declare the device list variables in the netvsc driver as static, and rename the internal functions to follow the naming convention. (Architecture-related: public API)
  ↳ No PR: [7e90122](https://github.com/DPDK/dpdk/commit/7e9012298ff3746b732dd21274d5c35b01dd88b7), [e1e27de](https://github.com/DPDK/dpdk/commit/e1e27de3fa79a9665dda721a6ceae3f96179be5f)
- Change the flow_lock variable in the ntnic driver to a static variable inside the file, and remove the external declaration in the header file. (Architecture-related: public API)
  ↳ No PR: [bda0956](https://github.com/DPDK/dpdk/commit/bda095642723a6d004ae4ae848d675c90cd58fd6)
- Rename the global variable hwlock in the ntnic driver to nthw_lock, and update related functions simultaneously. (Architecture-related: public API)
  ↳ No PR: [0745b6c](https://github.com/DPDK/dpdk/commit/0745b6ca123eee0f14a1ff35bd7b2c0981ce21d0)
- Split the template enumeration in the bnxt driver into a public enumeration file and an application-specific definition file. (Architecture-related: public enumeration file splitting)
  ↳ No PR: [3fe1bbb](https://github.com/DPDK/dpdk/commit/3fe1bbbe780589a163a1dc3a6a7e0a9f0ac37852)
- Remove the unused rawdev pointer field in the fslmc bus driver. (Architecture-related: public API)
  ↳ No PR: [2db9ce1](https://github.com/DPDK/dpdk/commit/2db9ce15baa0e1eb6b0e254c7196c4c63cdc101f)
- Optimized the BMan buffer acquisition and release performance. By reducing byte swapping and using 128-bit read and write instructions, cache invalid access was reduced, and the performance was improved by about 10%. (Architecture-related: public API)
  ↳ No PR: [d4bf8c0](https://github.com/DPDK/dpdk/commit/d4bf8c0af1c8610a3248d7cc38f53498175110d4)
- Optimized QMan enqueue check, simplified ring buffer pointer operations and corrected byte order, improving data access performance. (Architecture-related: public API)
  ↳ No PR: [cd43719](https://github.com/DPDK/dpdk/commit/cd437199d7a8aee13ff4607678aa2122cdbba81b)
- Optimized the XSC network card Rx path, reduced cache conflicts by checking the CQ producer/consumer index, and improved small packet processing performance. (Architecture-related: public API)
  ↳ No PR: [0609f18](https://github.com/DPDK/dpdk/commit/0609f180af8309752c7c0ffa06913fcaf0d87347)
- Supported CN20K platform in CPT LMT line initialization, and added opcode_major field in security engine's authentication and encryption key settings to optimize opcode processing. (Architecture-related: Platform compatibility)
  ↳ No PR: [b4ca6eb](https://github.com/DPDK/dpdk/commit/b4ca6ebe2f67f1df2cb6cea5475c732e5fa430d2)
- Added TX head write-back mode and RX descriptor merge mode to the Amber-Lite network card. They are enabled by default and can be configured through the devargs parameter, which significantly improves performance. (Architecture-related: devargs configuration parameters)
  ↳ No PR: [8ada71d](https://github.com/DPDK/dpdk/commit/8ada71d0bb7f7ecee7eeb6823cff20a53ed29072), [27cf4ad](https://github.com/DPDK/dpdk/commit/27cf4ad00b98a65ff59d4e964ef9f29b8cd3090d)
- In the bnxt driver, truflow is allowed to use vector mode processing to improve throughput when the representor is not enabled, and device parameter parsing logic for representor mode and scalar mode is added. (Architecture-related: devargs configuration parameter)
  ↳ No PR: [a5274dc](https://github.com/DPDK/dpdk/commit/a5274dc1a6936813dbb919d5d2dcdd2683eb5e62)
- Reduce the default Rx extension header size from 16 bytes to 12 bytes, remove the hash_value field and turn off the semi-offload function to save PCIe bandwidth. (Architecture-related: Rx extension header)
  ↳ No PR: [fdb33a7](https://github.com/DPDK/dpdk/commit/fdb33a7c5a2705c73e2e8cedb3bd0cb76c7abc18)
- Fix the baseband/acc driver and add the missing rte_acc_common_cfg.h header file to the export list of the build system. (Architecture-related: public API)
  ↳ No PR: [611d08f](https://github.com/DPDK/dpdk/commit/611d08f11d42dfafbbf954798ea9c917f7d4ef89)
- Fix the build conditions in meson.build to ensure that the driver can be compiled normally in the arm64 environment. (Architecture-related: platform compatibility)
  ↳ No PR: [71c8c44](https://github.com/DPDK/dpdk/commit/71c8c449303db456dd630f59dcdcc88b1152b319)
- Fixed compilation errors caused by undefined NetUIO constants under MinGW 13, adjusted header file inclusion order and extended conditional compilation to be compatible with MinGW64. (Architecture-related: platform compatibility)
  ↳ No PR: [73e0c90](https://github.com/DPDK/dpdk/commit/73e0c90c48ea393b2725263b32515f668f8f4839)
- Replaced the VFIO build switch from RTE_EAL_VFIO to RTE_EXEC_ENV_LINUX, and removed the empty implementation of non-Linux systems in the crypto/bcmfs driver to support Linux only. (Architecture-related: platform compatibility)
  ↳ No PR: [f02cf5f](https://github.com/DPDK/dpdk/commit/f02cf5f5b182ecaddb94c83244668d9673bc230c)
- Remove the condition for skipping driver construction under the MSVC compiler, so that the driver supports MSVC compilation. (Architecture-related: platform compatibility)
  ↳ No PR: [f41d2db](https://github.com/DPDK/dpdk/commit/f41d2db45d8a23c3315929c190d098154732a1ce)
- Support compiling the zxdh driver on 64-bit RISC-V systems, update the list of unsupported architectures in the build configuration and documentation. (Architecture-related: Platform compatibility)
  ↳ No PR: [dd9a30e](https://github.com/DPDK/dpdk/commit/dd9a30e2c3c098d4a7a31adf1b56d789fb2dd00e)
- Add old name backward compatibility mapping for Intel drivers, so that old names such as net/ixgbe can still be used in the command line to enable or disable the driver. (Architecture-related: build and installation methods)
  ↳ No PR: [ea83571](https://github.com/DPDK/dpdk/commit/ea83571ae14d74a2c554de93b4aca272b05c7413)
- Fix the problem of wildcard matching nested drivers in the meson build system, so that patterns such as net/* can recursively match drivers in subdirectories and restore backward compatibility. (Architecture-related: build and installation methods)
  ↳ No PR: [4384917](https://github.com/DPDK/dpdk/commit/438491733c2d8a109574449d3d6de9b25a05c07c)
- The PMU build script is changed to only install architecture-related header files under the corresponding architecture to avoid header file pollution. (Architecture-related: build and installation methods)
  ↳ No PR: [9159a04](https://github.com/DPDK/dpdk/commit/9159a04b8410c552df9cdafa8e95d9603429d779)
- Remove the custom macro RTE_PMU_SUPPORTED and instead rely on RTE_LIB_PMU automatically defined by the build system for conditional compilation. (Architecture-related: public API)
  ↳ No PR: [8682341](https://github.com/DPDK/dpdk/commit/868234159d120efd01c5d3577f0ca59e0aac9ff2)
- Fixed the build failure of DPDK 24.11 when the TF_FLOW_SCALE_QUERY flag is enabled, and adjusted the relevant log print statement format. (Architecture-related: build and installation methods)
  ↳ No PR: [55ed539](https://github.com/DPDK/dpdk/commit/55ed53956465a86e4f8c0a512a70403fc81e6744)
- Add compile-time detection in the build system to support new DevX counter action types. (Architecture-related: build and install methods)
  ↳ No PR: [102a72d](https://github.com/DPDK/dpdk/commit/102a72da206cf9c5abe7fd0a1ccdd607259014a2)
- Simplify the conditional judgment of loop expansion pragma in virtio/vhost, and use the corresponding pragma directly according to the compiler type. (Architecture-related: build and installation methods)
  ↳ No PR: [4a04a34](https://github.com/DPDK/dpdk/commit/4a04a346e7f3aa68b7a272d05c86fec2e7db8e89)

### Environment Abstraction Layer (EAL)
- Clean up the VFIO public header file dependency, remove the inclusion of the Linux VFIO header file, the local uAPI package, the VFIO_PRESENT macro dependency and the old kernel compatibility package, and instead explicitly include it in the source file or use the kernel header file directly. (Architecture event: VFIO public header file dependency cleanup)
  ↳ No PR: [f86af39](https://github.com/DPDK/dpdk/commit/f86af39537e4e1b08f8eb1af5e0a2a638ff0cd00), [2ffda8c](https://github.com/DPDK/dpdk/commit/2ffda8c2e357662354ee6ddcca769258c33642a9), [df77d01](https://github.com/DPDK/dpdk/commit/df77d015d4d6d39c3eeffa5f7ec928f92f39b62a), [27b39a0](https://github.com/DPDK/dpdk/commit/27b39a01929a1db77a9c931511357ba2ca7df54d)
- Add V extension detection support for RISC-V architecture, and include riscv_vector.h in the vector header file according to this feature condition. (Architecture-related: platform compatibility)
  ↳ No PR: [9202ef2](https://github.com/DPDK/dpdk/commit/9202ef259a9d69cceb00703fc7d9f746c32c25e5)
- Added vector extension-based LPM lookupx4 function implementation for RISC-V architecture. (Architecture-related: public API)
  ↳ No PR: [85f7628](https://github.com/DPDK/dpdk/commit/85f7628b304ac7f425136fa746610d296a758121)
- Added cross-platform rte_basename function, used to safely extract file path base name, and add corresponding unit tests. (Architecture-related: public API)
  ↳ No PR: [b8a75ec](https://github.com/DPDK/dpdk/commit/b8a75ece45fe29cf305d093c27228aae91dfb324), [e2d42b2](https://github.com/DPDK/dpdk/commit/e2d42b26e151fda648d12f74b246cb824875ea74), [4b89d77](https://github.com/DPDK/dpdk/commit/4b89d77aa3405b9db70f042073c04a9a9181cad8), [6251646](https://github.com/DPDK/dpdk/commit/62516462cbc7bd8604764cfa554482a17ffd55a2)
- EAL adds corresponding long options to each short option and unifies the option format. (Architecture-related: public API)
  ↳ No PR: [7fa2709](https://github.com/DPDK/dpdk/commit/7fa270981fb1b24225f04414a8775f8938ee97da)
- EAL adds new parameter definitions based on argparse format, and provides parameter list callback functions and usage printing functions. (Architecture-related: public API)
  ↳ No PR: [f330b01](https://github.com/DPDK/dpdk/commit/f330b01df996869b4a87a4102d0f86fb4ff3f6b6)
- EAL incorporates command line parameter combination verification checks into the parsing process, and adds validity checks for some parameters. (Architecture-related: external behavior)
  ↳ No PR: [8d0c3e3](https://github.com/DPDK/dpdk/commit/8d0c3e389124e18ee062d594db70ce5f97f1375e)
- EAL adds the --remap-lcore-ids option, which supports mapping lcore IDs to low ranges; it also supports using core IDs greater than RTE_MAX_LCORE in the core list, and limits automatic remapping grouping. (Architecture-related: public API)
  ↳ No PR: [ba40fb0](https://github.com/DPDK/dpdk/commit/ba40fb01b3b7a4aed699b38b8fd8612cf5e597ec), [867ee6a](https://github.com/DPDK/dpdk/commit/867ee6a45c4af0bfec4ffe3a42ff275b98b830ae), [c0dac52](https://github.com/DPDK/dpdk/commit/c0dac5236e10606dc03ce2fec5121c3d0c6eb20b)
- Fixed undefined behavior caused by arithmetic operations on NULL pointers in the RTE_TAILQ_LOOKUP macro. (Architecture-related: public API)
  ↳ No PR: [5d2d403](https://github.com/DPDK/dpdk/commit/5d2d4033abe5bb17f6e328fad1a615553573abd5)
- Fixed the alignment problem of param array in multi-process messages, aligning it to 8 bytes to avoid runtime errors caused by unaligned access. (Architecture-related: public API)
  ↳ No PR: [4de27d1](https://github.com/DPDK/dpdk/commit/4de27d169e4b46669aa8914fe2a2895094ebce59)
- Fixed the error log problem caused by improper MP channel cleaning sequence when the secondary process exits, and moved the rte_mp_channel_cleanup call to after eal_bus_cleanup. (Architecture-related: EAL cleaning sequence)
  ↳ No PR: [4bc53f8](https://github.com/DPDK/dpdk/commit/4bc53f8f0d64ceba6c4077aa31229f1e38e0d30f)
- Fixed the L2 length calculation problem in GRE tunnel packets, so that the L2_len returned by rte_net_get_ptype() correctly contains the tunnel protocol header. (Architecture-related: public API)
  ↳ No PR: [cb699a0](https://github.com/DPDK/dpdk/commit/cb699a047d1f2c1cead545db2d266ab5f396b550)
- Fixed the problem that non-EAL threads cannot bind lcore in pipeline mode, use rte_lcore_has_role to check lcore validity, and add error handling when the graph ID is invalid. (Architecture-related: public API)
  ↳ No PR: [faa15e6](https://github.com/DPDK/dpdk/commit/faa15e63f554bccda1ab0ca6fe3a09e3c7ff8658)
- Fix the processing of rawdev device ID acquisition failure, change the return type of rte_rawdev_get_dev_id() from uint16_t to int to support negative error values, and add error checking on the caller. (Architecture-related: public API)
  ↳ No PR: [97e2e19](https://github.com/DPDK/dpdk/commit/97e2e198b96078a4732d468bf0a4e8ec45aa5717), [8887f57](https://github.com/DPDK/dpdk/commit/8887f57cd71e47fa487b8d37c421fba897f7c7ee)
- Fixed syntax error in ARM 32-bit memcpy header file when compiling in C++. (Architecture-related: platform compatibility)
  ↳ No PR: [9b7a162](https://github.com/DPDK/dpdk/commit/9b7a1625adcac411cbab37030b2b8de0290d71fd)
- Fix clang 21 compilation error, replace RTE_TRACE_POINT_ARGS(void) with direct (void) to avoid applying __rte_unused attribute to void parameters. (Architecture-related: build compatibility)
  ↳ No PR: [5ff1ab4](https://github.com/DPDK/dpdk/commit/5ff1ab4103fd2eeac8f476b1957e6796efcadf16)
- Disable ring size from being 0 to prevent runtime crashes, and add corresponding test cases. (Architecture-related: public API: ring size verification)
  ↳ No PR: [dfe87f9](https://github.com/DPDK/dpdk/commit/dfe87f92b05e0ad507aa09d9bd773ae285854576)
- Fix the memory ordering problem of MCS locks, add correct synchronization edges in lock, unlock and trylock to establish the happens-before relationship between threads, and remove invalid memory barriers. (Architecture-related: public API: MCS lock memory ordering repair)
  ↳ No PR: [8357af1](https://github.com/DPDK/dpdk/commit/8357af1cb3a359810bd56eab78ed104495c8094f)
- Fix the data competition problem of the ring library under the weak memory model, and ensure a safe partial order relationship by adjusting the memory order. (Architecture-related: concurrency behavior of the ring library)
  ↳ No PR: [a4ad0eb](https://github.com/DPDK/dpdk/commit/a4ad0eba9def1d1d071da8afe5e96eb2a2e0d71f)
- Fixed the memory ordering problem in HTS ring mode, and established the happens-before relationship between threads of the same role by adjusting the release/acquire semantics of CAS and head load. (Architecture-related: ring library HTS mode concurrency behavior)
  ↳ No PR: [66d5f96](https://github.com/DPDK/dpdk/commit/66d5f962780694f6aebf000907fc3ce7a72584f9)
- Fix the memory ordering problem in RTS mode, and establish a safe partial ordering relationship between threads by using release and acquire semantics for CAS and preorder head load respectively. (Architecture-related: ring library RTS mode concurrency behavior)
  ↳ No PR: [36b69b5](https://github.com/DPDK/dpdk/commit/36b69b5f958e10eb5beb4292ade57199a722a045)
- Fixed the problem that the saved parameters were not released and the run_once flag was not reset when rte_eal_init initialization failed. (Architecture-related: public API)
  ↳ No PR: [4037269](https://github.com/DPDK/dpdk/commit/40372699f4274407f02ed97548818efd09a439a8)
- Fix the problem of custom VFIO container processing under multi-process, adjust the container fd acquisition logic, and avoid the auxiliary process incorrectly requesting the main process to open the container. (Architecture-related: VFIO container processing)
  ↳ No PR: [8a8c02d](https://github.com/DPDK/dpdk/commit/8a8c02d2bb224ebbe60e8e1ce6edcfb481b46151)
- Removed deprecated _u64 telemetry functions, which have been replaced by _uint versions since 2023. (Architecture-related: public API)
  ↳ No PR: [1d627ea](https://github.com/DPDK/dpdk/commit/1d627ea13aeec2bcccf27246e6be2508370d171e)
- Reconstruct the EAL parameter parsing logic, first collect all command line parameters into the structure, and then process them uniformly in a fixed order. (Architecture-related: public API)
  ↳ No PR: [cc0dea4](https://github.com/DPDK/dpdk/commit/cc0dea40b330aff826b457cf88eb90d7d927c080)
- Change the return type of the rte_bitmap_free function from int to void, remove parameter checks and return values, and simplify the API. (Architecture-related: public API)
  ↳ No PR: [874581d](https://github.com/DPDK/dpdk/commit/874581d2e04209ae3353bcfb35a28fb67476db39)
- Move the socket handler function type definition in the public header file to the internal header file and rename it to a prefixed name to avoid namespace pollution and compilation warnings. (Architecture-related: public API)
  ↳ No PR: [572451f](https://github.com/DPDK/dpdk/commit/572451f7728711b1c377cb46d885f918be4c7763)
- Change coremask parsing from array-based to cpuset-based, and adjust the internal function declaration position. (Architecture-related: public API changes)
  ↳ No PR: [99c05ce](https://github.com/DPDK/dpdk/commit/99c05ce5ef81b260bda68bcb99a2ff3dc0d644a1)
- Remove unused header file references in rte_spinlock.h, and add inclusions in the actual dependent source files. (Architecture-related: Public header file dependency adjustment)
  ↳ No PR: [e5b73e2](https://github.com/DPDK/dpdk/commit/e5b73e262f859de41ac56bacf5c7d0332611dc6f)
- Fixed the problem of missing DMA mask verification when explicitly specifying IOVA mode during EAL initialization, ensuring that DMA mask detection is always triggered during cross-platform initialization. (Architecture-related: platform compatibility)
  ↳ No PR: [e37ff4e](https://github.com/DPDK/dpdk/commit/e37ff4ef296f33e4c3a0e9306241c4f8fcae5061)
- Improve the documentation comments of functions such as rte_align32pow2 to clarify the meaning of the return value when the input is a power of 2. (Architecture-related: public API)
  ↳ No PR: [f9f773f](https://github.com/DPDK/dpdk/commit/f9f773fe2d6f49f1223283dc3e75198f2e6c0664)
- Remove support for GCC 8 and below and Clang 7 and below, and clean up related compilation checks and compatibility code. (Architecture-related: compiler version requirements)
  ↳ No PR: [dd7fdff](https://github.com/DPDK/dpdk/commit/dd7fdfff9bc1f369ec4838b06780df594e0e532c)
- Remove the VFIO compatible wrapper for the old Linux kernel and use the kernel's native macro definitions directly. (Architecture-related: platform compatibility)
  ↳ No PR: [b38d3df](https://github.com/DPDK/dpdk/commit/b38d3df0c4b3bcd40ef293cd23f1627cc307611f)

### Device Abstraction Libraries
- Adjusted the DMA adapter header file dependency and replaced the driver internal header files with public header files. (Architecture-related: public API)
  ↳ No PR: [faa398f](https://github.com/DPDK/dpdk/commit/faa398f28d7259e42954c04e048ad03398c938e5)
- Moved the member library internal hash macro from the public header file to the internal header file, hiding the internal implementation. (Architecture-related: public API)
  ↳ No PR: [441861b](https://github.com/DPDK/dpdk/commit/441861b4a30e6b6b6aca07367dd487657b1f50e8)
- Migrated the port event thread, adapter flm update thread and adapter monitoring thread into DPDK services, and restructured related functions to adapt to the new service model. (Architecture-related: thread model migration)
  ↳ No PR: [2125085](https://github.com/DPDK/dpdk/commit/2125085ac7eae682cea917d26a48ca332b4d3ec5), [d2a9a97](https://github.com/DPDK/dpdk/commit/d2a9a970d251e30b1c7a77126d04db6b674e5870)
- In the vmbus bus, save the UIO file descriptor for the secondary process, allowing it to access the vmbus device and use the fd to send signals to the Hyper-V host. (Architecture-related: multi-process support)
  ↳ No PR: [368e8f5](https://github.com/DPDK/dpdk/commit/368e8f5aec2c05196a300964540ab3a4ccf7d2a1)
- Add the struct rte_vmbus_device *dev parameter to all related functions of the vmbus bus and netvsc network driver, so that the secondary process can access the vmbus device through the device private area. (Architecture-related: public API)
  ↳ No PR: [303f928](https://github.com/DPDK/dpdk/commit/303f92849714c00f7d2a9f8f1400eb43d0344df5)
- Added conflicting configuration checking in the ethdev library, disabling Tx offload configurations that enable fast mbuf release and multi-segment transfer at the same time. (Architecture-related: external behavior)
  ↳ No PR: [fdb8403](https://github.com/DPDK/dpdk/commit/fdb840367cf0d6abeb17b05623679b8d1ea4c902), [60d4611](https://github.com/DPDK/dpdk/commit/60d461162b8a9f92382e5b1ce42b142542c012eb)
- Added a new mbuf operation history function, which tracks operations in the mbuf life cycle through dynamic fields, and provides marking and query APIs; this function is disabled by default and is automatically initialized when the mbuf pool is created. At the same time, the dump mbuf history command is added to testpmd, which supports outputting the operation history of all mbufs, a single mbuf or a specified mbuf pool to the console or file. (Architecture-related: public API)
  ↳ No PR: [d265a24](https://github.com/DPDK/dpdk/commit/d265a24a32a47781299618e12669c7792527967f), [1303b50](https://github.com/DPDK/dpdk/commit/1303b50a9c21def008634cfb4a91886b98e7a999)
- Added link connector type parameters for Ethernet devices, and a new API to convert connector enumerations into readable strings. (Architecture-related: public API)
  ↳ No PR: [a57f22c](https://github.com/DPDK/dpdk/commit/a57f22c5e216b5b1d267239d5aecbd62d9683193)
- Added mbuf history mark in Rx/Tx burst function for debugging, and has no performance impact when disabled by default. (Architecture-related: public API)
  ↳ No PR: [d9111b1](https://github.com/DPDK/dpdk/commit/d9111b1e34a10ae16f224611f8566f89bb422b75)
- Added cross-process and cross-operating system DMA transfer support, including capability flags, domain type checking and cross-domain control plane API (create, destroy and leave access groups). (Architecture-related: public API: cross-domain DMA transfer)
  ↳ No PR: [c39e0a9](https://github.com/DPDK/dpdk/commit/c39e0a9b1b99f574e0aa4bb1119241083a2ca60d), [9f0e1c5](https://github.com/DPDK/dpdk/commit/9f0e1c5cad46074bf85bfb9084bc8f7e47e8aff9)
- Added support for NT400D11 network card, including register description, reset initialization (stage 0/1/3/4), initialization stub function, and unified acquisition operation function naming. (Architecture-related: platform compatibility)
  ↳ No PR: [4a662c7](https://github.com/DPDK/dpdk/commit/4a662c758395e0c921e82b632b2b0c5668ec774c), [9bf5138](https://github.com/DPDK/dpdk/commit/9bf5138af3da99e26cab12e29347e0986e7b8c4b), [4e4297a](https://github.com/DPDK/dpdk/commit/4e4297ad029c03fc7be4f74e7b0461c1f3fddafe), [e842731](https://github.com/DPDK/dpdk/commit/e8427317f7a6bf36f4705be2ed70b16481aec288), [46e92f0](https://github.com/DPDK/dpdk/commit/46e92f01abf130c1407dbc78c13b370761671463), [dd4efe1](https://github.com/DPDK/dpdk/commit/dd4efe1f47fef82877949d93a42f3d7ed4bc3cde), [0e10002](https://github.com/DPDK/dpdk/commit/0e10002dc991907b22906e1edaba3d607adf64d1), [02c6f45](https://github.com/DPDK/dpdk/commit/02c6f45d4c331940ec230eca9f3b51204623a2d6), [bd71ba0](https://github.com/DPDK/dpdk/commit/bd71ba0390cee5efd2e2057a864348d7d896aa11), [9acb809](https://github.com/DPDK/dpdk/commit/9acb809ff663c3fe23d51b3ddfe76925c12b5a7d), [5e40c76](https://github.com/DPDK/dpdk/commit/5e40c76c975829c25376e1a7d8b9809db146b4f0), [29a287f](https://github.com/DPDK/dpdk/commit/29a287f3cb1caff8667df5d52919c10949cd4c64)
- Added domain_id parameter to dmadev's join access group API, adjusted the parameter order to be consistent with create API, and updated related documents. (Architecture-related: public API)
  ↳ No PR: [1f1eb71](https://github.com/DPDK/dpdk/commit/1f1eb710e35e46b4bb26c93a72f572e0b4cb38be)
- Improved representor parameter parsing, supporting bracket syntax (such as (pfX)vfY) to explicitly specify only detecting VF representative ports, and suppressing the automatic addition of PF representor ports in multi-port E-Switch scenarios. (Architecture-related: public API)
  ↳ No PR: [9adc7b2](https://github.com/DPDK/dpdk/commit/9adc7b2b84d3e59ffd62a7d359618700a9dbf941), [f87fa31](https://github.com/DPDK/dpdk/commit/f87fa31a9304210799698a811e3333015262b5fe)
- Added allocation annotations to BPF load functions to support the compiler in detecting misuse of memory allocation and deallocation. (Architecture-related: public API)
  ↳ No PR: [0247b16](https://github.com/DPDK/dpdk/commit/0247b166a16e8c662feb60f23e2e05512bf4012d)
- Fixed the compatibility of gpudev driver header files under Windows. (Architecture-related: platform compatibility)
  ↳ No PR: [bda83ec](https://github.com/DPDK/dpdk/commit/bda83ec0bb0c1bfba33843059a244181b46b9907)
- Fix the compression device ID verification logic to ensure that other devices can still be accessed normally after the device is released. (Architecture-related: public API)
  ↳ No PR: [cc80daa](https://github.com/DPDK/dpdk/commit/cc80daa544c15e361a2e2433387581ed1bffcd90)
- Removed callback null pointer check from Ethernet device fast path API, use virtual callback function instead to avoid performance overhead. (Architecture-related: public API)
  ↳ No PR: [066f3d9](https://github.com/DPDK/dpdk/commit/066f3d9cc21ccaf15be29dddc63891c43aac06f4)
- Separate the driver internal header file of the power module from the public header file, and move the rte_power_core_capabilities structure definition to the public header file rte_power_cpufreq.h. (Architecture-related: public API)
  ↳ No PR: [76393b9](https://github.com/DPDK/dpdk/commit/76393b98bf67f94dc6aa23cf5016c32571899261)
- Adjust the inclusion relationship of mbuf log-related header files so that mbuf_log.h explicitly depends on rte_log.h. (Architecture-related: header file dependency)
  ↳ No PR: [7e7401a](https://github.com/DPDK/dpdk/commit/7e7401ab314fc7ca01d640a82c556442e66ad62a)
- Optimized the performance and readability of the rte_pktmbuf_prefree_seg function, and improved the RTE_MBUF_DIRECT macro so that common code paths can be accommodated in one instruction cache line on x86-64. (Architecture-related: public API)
  ↳ No PR: [d5f044e](https://github.com/DPDK/dpdk/commit/d5f044e4af5909cbb0d15031a7d0d58359f83384)
- Replace variable-length arrays in BPF filter functions with alloca allocation, eliminating dependence on C standard extensions and improving Windows compatibility. (Architecture-related: Platform compatibility)
  ↳ No PR: [32d7d57](https://github.com/DPDK/dpdk/commit/32d7d573fb05987a8ac8e2c9456e4e1cb4df0034)

### Protocol and Service Libraries
- Integrate RCU QSBR support in rte_fib6 to achieve safe tbl8 group recycling. (Architecture-related: RCU QSBR integration)
  ↳ No PR: [200ccb9](https://github.com/DPDK/dpdk/commit/200ccb9ebd8e57bd598aeec7f1ca29850fafdb01)
- Added load_echo command to testpmd's load command to provide explicit echo control and remove global echo settings. (Architecture-related: testpmd command line interface)
  ↳ No PR: [15e048c](https://github.com/DPDK/dpdk/commit/15e048c5cc2359307e22b5041426d1974c2eed1f)
- The cmdline-file and cmdline-file-noecho parameters of testpmd can now be specified multiple times, supporting up to 16 command files. (Architecture-related: testpmd command line interface)
  ↳ No PR: [3f8325d](https://github.com/DPDK/dpdk/commit/3f8325d0c0c007892f4bd03a5ec2952f4a3dc86d)
- Added link_type parameter to rte_pcapng_add_interface function, allowing users to specify the protocol link type, and updated all call points to be compatible with this change. (Architecture-related: public API)
  ↳ No PR: [f1642ff](https://github.com/DPDK/dpdk/commit/f1642ffb2505239ffb17d82b7da4e47c3115c0ea)
- The argparse library adds support for parsing core list type parameters. (Architecture-related: public API)
  ↳ No PR: [d78103f](https://github.com/DPDK/dpdk/commit/d78103fb94887c7e44a4992fe3f9f8045254c1a3)
- The argparse library adds the ignore_non_flag_args option. When enabled, it can move non-flag parameters to the end, simulate getopt behavior, and disable positional parameters. (Architecture-related: public API)
  ↳ No PR: [de3bc25](https://github.com/DPDK/dpdk/commit/de3bc2588c3e29343fb7dabeeecc59a72cb081e8)
- The argparse library supports short options followed directly by parameters (such as -xarg), without equal sign separation. (Architecture-related: external behavior)
  ↳ No PR: [66e29a0](https://github.com/DPDK/dpdk/commit/66e29a02b494dee6a3d473dfb44f2ed4738b731c)
- Add a mechanism to monitor the primary process for the secondary process of testpmd. When the primary exits, the secondary will automatically exit to avoid crashes caused by accessing failed devices. (Architecture-related: secondary process monitoring)
  ↳ No PR: [7628f5b](https://github.com/DPDK/dpdk/commit/7628f5bbb7e882e57c956d98731cac12a436c9a7)
- Fix the include guard of VDUSE imported header files to avoid conflicts with system header files, adjust the header file inclusion order, and update related documents. (Architecture-related: public API)
  ↳ No PR: [9dce205](https://github.com/DPDK/dpdk/commit/9dce2056b2fd850e10619c48aa5af9554998bc8c)
- Fixed an issue where the external buffer and linear buffer features were not enabled when the VDUSE device was created, causing TSO support exception. (Architecture-related: public API)
  ↳ No PR: [8ae4f1d](https://github.com/DPDK/dpdk/commit/8ae4f1d511226fd65a979e9f8a1e51835281a59b)
- Fix IPv6 link-local address generation to comply with RFC 4291 specification, inverting u bit of EUI-64 interface identifier. (Architecture-related: public API)
  ↳ No PR: [9727c1b](https://github.com/DPDK/dpdk/commit/9727c1bae406fc080fdfcf3dae5c7a699e896b53)
- Replace the deprecated coremask parameter with the corelist parameter in the proc-info application. (Architecture-related: command line interface)
  ↳ No PR: [ae84c34](https://github.com/DPDK/dpdk/commit/ae84c343d8e6a178ee8689b8acd4eef26a5ca9e1)
- Fixed BPF build error when cross-compiling, by using the Meson sysroot attribute to correctly reference the header file in the target sysroot. (Architecture-related: build and installation mode)
  ↳ No PR: [475af32](https://github.com/DPDK/dpdk/commit/475af3278fbed7c13033eeed605a121c24be077d)

### Core Data Structures
- Add trace points for each operation type of bbdev, and add experimental API rte_bbdev_ops_trace to record input parameters of different operation types. (Architecture-related: public API)
  ↳ No PR: [62fc205](https://github.com/DPDK/dpdk/commit/62fc2059e02b635e814d75c821d737f09b750972)
- Improved mbuf's raw free and raw alloc bulk functions from experimental to stable, and updated the packet mbuf alloc bulk function to use the stable raw alloc bulk function. (Architecture-related: mbuf raw function stabilization)
  ↳ No PR: [cd8c8ba](https://github.com/DPDK/dpdk/commit/cd8c8bac82dd4d03d055b0816f21b4cde63ebc00)
- Add an optimized reset function for reinitialized mbuf batches, which uses mempool information to implement write-only operations and avoids reading the mbuf's own fields, thus improving performance. (Architecture-related: mbuf batch reset function)
  ↳ No PR: [508d60b](https://github.com/DPDK/dpdk/commit/508d60b518bd6870f906285c689c9508c57e9dd4)
- Refactor the sanity check of mbuf from inline function to non-inline, and add optional mempool parameter support. (Architecture-related: public API)
  ↳ No PR: [ba13530](https://github.com/DPDK/dpdk/commit/ba13530aa71fca9f350bcc6e2f640c16046a0673)
- Replace zero-length arrays with flex array members to eliminate dependence on GCC extensions. (Architecture-related: compiler compatibility)
  ↳ No PR: [e816819](https://github.com/DPDK/dpdk/commit/e816819ba8dee9f421c4a45b0ef71cebcdf24f12)
- Fixed compilation failure caused by missing errno definition in dmadev debug build. (Architecture-related: public API)
  ↳ No PR: [1624f34](https://github.com/DPDK/dpdk/commit/1624f34dde105a47e1d22f419a90fd65997c908f)

## Routine Changes

### New features
- Added QinQ insertion offload support for the IAVF driver's scalar Tx path and AVX-512 path, and dynamically reports the offload capability based on the VF capability.
  ↳ No PR: [fdc3796](https://github.com/DPDK/dpdk/commit/fdc37964c2bfbf769c469636ca5f19efa7ab4cd0), [3aa4efa](https://github.com/DPDK/dpdk/commit/3aa4efa36438fffd340e3cc7e03aa9af819158b4)
- Add the trace point of the operation parameter in the acc_error_log function to record the operation details when the operation is rejected by PMD.
  ↳ No PR: [76c87b1](https://github.com/DPDK/dpdk/commit/76c87b1c74f33f923aef6e8473a0509e41cced20)
- Add RISC-V vector extension support to the FIB search function, and add judgment on the RISC-V Vector Extension instruction set and distribution of the corresponding search function in the vector function selection logic.
  ↳ No PR: [f2ccf5f](https://github.com/DPDK/dpdk/commit/f2ccf5fc334b0ef4d62f15606657c05c5673206e)
- Added --enable-rss option to testpmd, which allows forcing RSS in single-queue mode and is mutually exclusive with --disable-rss.
  ↳ No PR: [272eb47](https://github.com/DPDK/dpdk/commit/272eb4785842b596f878917832a35e5a859f6584)
- Added the minimum and maximum MTU values supported by the display port in the show port info command.
  ↳ No PR: [e36eeb5](https://github.com/DPDK/dpdk/commit/e36eeb5eee33ef7e771ca9cc1501dd9516a21def)
- Support unmonitored Hyper-V channels, use UINT8_MAX flag and skip delay setting when reading monitor ID fails, and add support for sending events through interrupt page and UIO interface for vmbus channels that do not support monitor.
  ↳ No PR: [8e4a1b8](https://github.com/DPDK/dpdk/commit/8e4a1b88e102ad10f1989e82d525e77802e60f54), [fb4bff9](https://github.com/DPDK/dpdk/commit/fb4bff96be7da236222a299ffc0b47107d05900b)
- Added the ice_get_max_simd_bitwidth function in the ice driver, which is used to obtain the maximum SIMD bitwidth and uniformly uses the general vector capability function.
  ↳ No PR: [ef7f996](https://github.com/DPDK/dpdk/commit/ef7f996c3d3cca63c7e78e5f073428526e6cc2c0)
- The iavf driver adds a new function to obtain the maximum SIMD bit width, using the general vector capability function.
  ↳ No PR: [8d178bf](https://github.com/DPDK/dpdk/commit/8d178bf5328b2e6977b485ac231e167f77aea664)
- Support GVE DQ Tx out-of-order completion, and introduce a new packet ring and idle completion label stack to solve the performance degradation and memory leak problems caused by out-of-order completion.
  ↳ No PR: [5fd289f](https://github.com/DPDK/dpdk/commit/5fd289ff3a008370befef95029b9b65b66661217)
- Cache all PCI driver parameters so that the same parameters can be reused when the device is hot-plugged again after hot removal, and the related memory allocation and release logic has been cleaned up.
  ↳ No PR: [9a9d038](https://github.com/DPDK/dpdk/commit/9a9d038c782eb2773d774a659607081d5249630b)
- Added new flow guide table entry write, delete and get operation functions through DTB channel.
  ↳ No PR: [43a9a4d](https://github.com/DPDK/dpdk/commit/43a9a4ddada8156b3b560d81d04cfe414ccd616d)
- Added firmware version query, promiscuous mode setting and module information acquisition functions for xsc network card driver.
  ↳ No PR: [cf1bc37](https://github.com/DPDK/dpdk/commit/cf1bc37f183eeb0a0310bb0ff0d3f804ad1d5fcb)
- XSC network card port adds support for enabling and disabling promiscuous mode.
  ↳ No PR: [c74dc3c](https://github.com/DPDK/dpdk/commit/c74dc3cf359034e74a09eb7482b28121b5cd9500)
- Added device ID for Intel E835 series Ethernet controller and mapped it to E830 series MAC type.
  ↳ No PR: [b41758f](https://github.com/DPDK/dpdk/commit/b41758f2f7466a54ad25bd53dc88d9424fbd2c7a)
- Improved the AESNI-MB encryption driver CPU code path, added support for Output in Place (OOP), and fixed many minor issues.
  ↳ No PR: [4b0e460](https://github.com/DPDK/dpdk/commit/4b0e460fd578480ee76c8d2219296da81eb26bb3)
- Added a warning for missing offload flags related to multi-part packages when testpmd is started.
  ↳ No PR: [0da8107](https://github.com/DPDK/dpdk/commit/0da8107342a78278209fb4d0ff886de29af75e7d)
- Updated link speed capabilities to support 200G and 400G, and renamed internal functions.
  ↳ No PR: [9cb4262](https://github.com/DPDK/dpdk/commit/9cb4262fe8f0b713ee51a1421d4c322bb84d15b4)
- To support compressed PCI BAR devices, a new register address initialization function has been added and the command queue configuration and device de-initialization logic have been adjusted.
  ↳ No PR: [f3d775d](https://github.com/DPDK/dpdk/commit/f3d775dc9d4db5ee6e20c3f4a137152aed91d0b4)
- Updated the public Rx routing infrastructure to support the single queue feature and replaced the original complex logic with this public function in the idpf driver.
  ↳ No PR: [12b1c29](https://github.com/DPDK/dpdk/commit/12b1c29017615baf6353782623a2e857a898458e)
- Support multiple PF processes to share flow tables, and reconstruct the device management data structure to distinguish different PFs.
  ↳ No PR: [355e467](https://github.com/DPDK/dpdk/commit/355e467cef9a835383b41957523028497a0454a0)
- Added scattered receive support to the idpf driver split Rx queue, enabling the function to handle jumbo packets and multi-mbuf receive scenarios.
  ↳ No PR: [f02f6af](https://github.com/DPDK/dpdk/commit/f02f6afea14fdd32c386322a22cdf289e147c608)
- Supports reading and setting MAC address from hardware, replacing the original fixed default MAC address.
  ↳ No PR: [4c19f96](https://github.com/DPDK/dpdk/commit/4c19f969526cd630cf3ed752e12d79055bdb4db9)
- Added package type parsing to the enetfec driver, temporarily supporting identification of IPv4 and IPv6 packets.
  ↳ No PR: [f8d6402](https://github.com/DPDK/dpdk/commit/f8d6402c8413c5ac9edcb68c201b46db932b05b4)
- The dump command of testpmd has been changed from underscore separation to space separation, the parsing function has been merged, and a new mbuf history related dump command has been added.
  ↳ No PR: [cae0444](https://github.com/DPDK/dpdk/commit/cae0444c2ecd09487d8bc3042c59b23d237d547c)
- The ice network card driver adds Data Center Bridging (DCB) support, including DCB configuration checking, initialization and de-initialization, and priority flow control settings.
  ↳ No PR: [02b71e5](https://github.com/DPDK/dpdk/commit/02b71e5702941458141f0d5cfb9775db9a521f53)
- The IDPF driver supports device discovery through PCI class ID, and adds a new auxiliary function to determine PF/VF.
  ↳ No PR: [9edaec5](https://github.com/DPDK/dpdk/commit/9edaec519724f8fb60c9f452b7abce877e3f0772)
- CPFL driver adds MMG hardware device ID, renames macros, and dynamically configures the number of queues based on PCI function numbers.
  ↳ No PR: [06c585c](https://github.com/DPDK/dpdk/commit/06c585cb0dee8ad7afceede9d02a5b6953d79e7f)
- The ENA driver adds extended completion descriptor support for the TX path, allows the selection of descriptor types, unifies the use of extended descriptors for the RX path, and adds timestamp processing.
  ↳ No PR: [81463c6](https://github.com/DPDK/dpdk/commit/81463c667fb57e4913eb2fe647516479c406b020)
- The ENA network card driver adds interrupt loss detection support, and adds a lost interrupt indication parameter in the interrupt update register.
  ↳ No PR: [02efdb8](https://github.com/DPDK/dpdk/commit/02efdb898ab625ef999ea41519b3d541beeee401)
- The DPAA2 network driver now queries the actual MAC speed capability through the new MC command during detection, and sets the device's speed capability field accordingly.
  ↳ No PR: [c78fa95](https://github.com/DPDK/dpdk/commit/c78fa95fa9b00acc37ed2f6ecbb642c77defe805)
- Added policer statistics support for each TC, and support for dpmac statistics when MC version is higher than 10.39.0.
  ↳ No PR: [5041175](https://github.com/DPDK/dpdk/commit/5041175c47bfef2ad6e6dc7c4bbd0250ac84de21)
- Added TX laser enable/disable support for Amber-Lite network cards, and adjusted GPIO and LED control logic based on hardware type.
  ↳ No PR: [e30e5fb](https://github.com/DPDK/dpdk/commit/e30e5fba32c48baba594b67189fd862facd79c26)
- Added TX queue rate limiting function to Amber-Lite network card, and adjusted related configuration logic.
  ↳ No PR: [a309ab4](https://github.com/DPDK/dpdk/commit/a309ab43acf321eca9b562959eef35017de1fbe4)
- Added thermal sensor support for Amber-Lite network card, including initialization and data reading configuration.
  ↳ No PR: [aebe9aa](https://github.com/DPDK/dpdk/commit/aebe9aa7ab675e2bc24c434c0d0d17cac6a9eac2)
- Enabled RSS function for Amber-Lite network card, supporting Amber-Lite series MAC types by extending RSS update function.
  ↳ No PR: [9772050](https://github.com/DPDK/dpdk/commit/9772050f92d6e13cb5cb4c7ec4760afade8aceee)
- Added support for up to 4 MAC address filtering and up to 4 VLAN filtering to the ENETC4 driver, and added a new MTU setting function.
  ↳ No PR: [1e4e718](https://github.com/DPDK/dpdk/commit/1e4e718b76d30f7346f01a6f6d55e48c7a578d2b)
- Added queue information query and link update support to the ENETC4 driver, added receive/send queue information acquisition functions and supported message type query functions.
  ↳ No PR: [6fb9f3d](https://github.com/DPDK/dpdk/commit/6fb9f3d8da19958740e9165f3faedeb2e0747eb8)
- Added a delayed queue start/stop function to the ENETC4 driver to support skipping the transceiver queue marked as delayed start when the device starts.
  ↳ No PR: [99a6724](https://github.com/DPDK/dpdk/commit/99a67243ef547169d6a7f9146ba429912904e17f)
- Added a global configuration section for the dma-perf application to support specifying the EAL parameters of all test cases through the eal_args entry in the configuration file.
  ↳ No PR: [9da8422](https://github.com/DPDK/dpdk/commit/9da8422c91b2f022015d5441cc5b2c2d8a72df69)
- Added --list-dma option to dpdk-test-dma-perf tool, and refactored parameter parsing and CSV output modules.
  ↳ No PR: [5e49bc4](https://github.com/DPDK/dpdk/commit/5e49bc4f8d2f8b67fa9c6b39f28a7a931f7faabb), [a4a4e46](https://github.com/DPDK/dpdk/commit/a4a4e462e497307981bda7f2a55fda3eed0bfe36), [b3e36e9](https://github.com/DPDK/dpdk/commit/b3e36e913bca6f2e20bb759f7f29810abf7b3360)
- Migrate the cache_flush and test_seconds parameters of the DMA performance test application from the test case level to the global configuration.
  ↳ No PR: [761fd3f](https://github.com/DPDK/dpdk/commit/761fd3f825db6b41ced01c35d87e4d15db1e4bbe)
- Added the exception_path device parameter to the NTNIC network card driver to support forwarding unmatched packets through queue 0.
  ↳ No PR: [c5ac66c](https://github.com/DPDK/dpdk/commit/c5ac66c168b55818f7a81eb94e86adea7608f6a5)
- Added eth_flow_query function to ntnic driver, supports flow query with counting action, and adjusted the flow operation registration interface.
  ↳ No PR: [75216f7](https://github.com/DPDK/dpdk/commit/75216f73259fb54e0dfe9f0c1fe04ba1f859adf9)
- Extended stream dump function to support output of MBR initialization configuration and rule information.
  ↳ No PR: [0e5d1a6](https://github.com/DPDK/dpdk/commit/0e5d1a6e9d96309baa84f30ff3e99306c08efe68)
- Support the configuration and release of NBL device Rx and Tx queues, implement functions such as stopping the sending ring, releasing the receiving ring and allocating the receiving buffer, and correct the relevant function names.
  ↳ No PR: [5d910b2](https://github.com/DPDK/dpdk/commit/5d910b2789da9f58aefb67c858d621ad9f62b8fc)
- Added device start and stop functionality for NBL network devices.
  ↳ No PR: [edeb40d](https://github.com/DPDK/dpdk/commit/edeb40df98cb8abb9b7db3dc7c2b0c2f630b290d)
- Implemented sending and receiving burst functions for NBL devices, and added packet processing, statistics and link status query functions.
  ↳ No PR: [e5fc1f7](https://github.com/DPDK/dpdk/commit/e5fc1f78c78c93ec6463261883d0c82414410958)
- Added statistics and extended statistics (xstats) functions for NBL network devices, supporting getting, resetting statistics and getting xstats counts, names and values.
  ↳ No PR: [661c0cc](https://github.com/DPDK/dpdk/commit/661c0ccf25126f8ef551be6a46b55ba9a9afb053)
- Added MTU update support for NBL network device driver and implemented MTU setting function.
  ↳ No PR: [75cdda3](https://github.com/DPDK/dpdk/commit/75cdda36a4c50896f3d6de34ad2b890442b217fc)
- Added promiscuous mode support to the NBL network device driver, and implemented promiscuous mode setting and related channel request functions.
  ↳ No PR: [80bd3ca](https://github.com/DPDK/dpdk/commit/80bd3cad22c8d2d6e17361f74cb07bff7f773406)
- Added recognition support for Centec SK21101 PHY in the ngbe driver.
  ↳ No PR: [7c2ef5b](https://github.com/DPDK/dpdk/commit/7c2ef5be5437c30c0260690e98567872510f0785)
- Add three Amber-Lite 25G virtual function device IDs to the txgbe driver to support identification of corresponding devices and driver matching.
  ↳ No PR: [a25a9f5](https://github.com/DPDK/dpdk/commit/a25a9f5a097e790876877065e35441edef14e398)
- Added flush operation for Amber-Lite network card to ensure that the configuration takes effect immediately.
  ↳ No PR: [b95ddb2](https://github.com/DPDK/dpdk/commit/b95ddb2e311c341054a28bdc4b944b9471fd825a)
- Added RSS register mapping support for Amber-Lite 25G VF, and extended the mapping function to correctly access RSS related registers.
  ↳ No PR: [de8816e](https://github.com/DPDK/dpdk/commit/de8816edc3184151e25a4c75b3ffb829c8cac01d)
- Added BME reset configuration for Amber-Lite 25G VF, reconfiguring the PCIE bus master enable register when the VF is reset.
  ↳ No PR: [9f684f0](https://github.com/DPDK/dpdk/commit/9f684f0b245894856244c91a8612a14d3d186c01)
- Add new action bits and adjust field mapping to the Broadcom TruFlow ULP template database, and add application data definitions for Wh+ products to adapt to Wh+, P5, and P7 product series.
  ↳ No PR: [95f2d84](https://github.com/DPDK/dpdk/commit/95f2d8425728f5cc76a00bf08bdcbf1845bfec00), [3c8fd65](https://github.com/DPDK/dpdk/commit/3c8fd65a88ac7cf9fb46a3faefe2b16d83201970)
- Enhance the pdump tool to support multi-process scenarios, add pdump initialization and cleanup logic in dumpcap and pdump applications, and forward callback enablement notifications to secondary processes.
  ↳ No PR: [05326ef](https://github.com/DPDK/dpdk/commit/05326efc0b21d8c43ee150ecc10c006e0372f39b), [c3ceb87](https://github.com/DPDK/dpdk/commit/c3ceb8742295fc15ef68c8743186c650d3be3d62), [b63e7db](https://github.com/DPDK/dpdk/commit/b63e7dbfb076d6a8247dcab014421d7b59e20255)
- Removed the socket direct function's dependence on multi-root configuration, always enabled global table scope for Thor2, and removed the global table scope feature bit; also added support for the unicast only feature.
  ↳ No PR: [cf2b225](https://github.com/DPDK/dpdk/commit/cf2b225241799681d09901354b4eb78a6547a0f9)
- Add non-VFR mode support in the initialization function, enable testpmd inter-port forwarding mode through compile-time flag control.
  ↳ No PR: [4966539](https://github.com/DPDK/dpdk/commit/49665399b1359131e4363ab66dff02703beae59b)
- In no-hugepage mode, replace the memory physical address acquisition function from rte_mem_virt2phy to rte_mem_virt2iova to support running by unprivileged users.
  ↳ No PR: [d9ec96d](https://github.com/DPDK/dpdk/commit/d9ec96d7baf34ac442916ae926ab9bdf0c19c719)
- Added support for using parent PF vnic for PF action handlers.
  ↳ No PR: [5fab919](https://github.com/DPDK/dpdk/commit/5fab9199867906cad1ee7a88d1fb653e8382caa3)
- Added the feature bit of Rx miss sent to the parent PF for the bnxt/tf_ulp driver, and added the corresponding processing logic.
  ↳ No PR: [ef86bb9](https://github.com/DPDK/dpdk/commit/ef86bb9c55abf8a0592249521152d334aac46506), [505ede7](https://github.com/DPDK/dpdk/commit/505ede70a53ac4d2201c8c950b8f534b84ceab47)
- Added promiscuous mode support for TruFlow applications in the bnxt driver, enabling or disabling the reception of packets with unknown destination MAC addresses.
  ↳ No PR: [813a5fa](https://github.com/DPDK/dpdk/commit/813a5fad408611c53dac2825352e376e6f5b268c)
- Add network namespace change detection and processing functions to the tap driver. When the interface is moved to another namespace, the netlink and LSC interrupt sockets are automatically rebuilt and control is maintained.
  ↳ No PR: [aae3a38](https://github.com/DPDK/dpdk/commit/aae3a38e9e03e606065e4891840a6ac2d6dfbf8f)
- Add link carrier configuration to the net/tap interface so that it can be used in Linux bindings; force the carrier to be enabled via ioctl after configuring at least one RX queue and when switching network namespaces.
  ↳ No PR: [ba292a7](https://github.com/DPDK/dpdk/commit/ba292a7c871dc310351dea08bd5a79c756f08403)
- Added support for the E610 network card in the ixgbe driver, allowing it to correctly set all supported link speeds.
  ↳ No PR: [8e5eac7](https://github.com/DPDK/dpdk/commit/8e5eac7fa26f312d7d8306ca310530dbeb9e86f2)
- Added register definitions, control structures and queue description structures related to CQ (completion queue) configuration for the CPT hardware unit to support the initialization, enabling and disabling of CPT CQ.
  ↳ No PR: [9ba64cf](https://github.com/DPDK/dpdk/commit/9ba64cfd4316c1321d1774813adf647680fab2e9)
- Updated mlx5 stream device parameter processing, automatically selecting default values based on whether the hardware supports software or hardware flow control, and forcibly disabling the repeat mode and giving a log prompt when incompatible.
  ↳ No PR: [d1ac7b6](https://github.com/DPDK/dpdk/commit/d1ac7b6c64d987006891fcf35a13c05cf2b05d62)
- Simulates support for sending and receiving VLAN offloading in the software, and implements the insertion and stripping of VLAN tags.
  ↳ No PR: [9d7757d](https://github.com/DPDK/dpdk/commit/9d7757dce874aaee85ea32e6e0cd5b00c94d6b3b)
- Added support for hardware discarded RX packet counting (imissed) for the NBL network device driver, including statistical startup, update, reset and resource management.
  ↳ No PR: [c9726a7](https://github.com/DPDK/dpdk/commit/c9726a719ca18fca1797a0a60ea16e4f0973d615)
- Added DCB forwarding command in testpmd application to support specifying traffic categories and configuring the number of cores used by each traffic category.
  ↳ No PR: [c58bdc7](https://github.com/DPDK/dpdk/commit/c58bdc7a589cc0ca52c8e8e95becd322ad8a4080), [945e9be](https://github.com/DPDK/dpdk/commit/945e9be0a80335b56e637a04b2acb11bcd0816a1)
- Enable parallel detection when auto-negotiation is enabled to attempt to discover link technologies and FEC settings that can lead to link establishment.
  ↳ No PR: [b11c47a](https://github.com/DPDK/dpdk/commit/b11c47a671e8fbff93c9f84f168c9aed21460750)
- Multiple Intel network card drivers (i40e, idpf, cpfl) use common functions to determine the maximum SIMD bit width, simplifying the vector path selection logic.
  ↳ No PR: [89f84c9](https://github.com/DPDK/dpdk/commit/89f84c960abe0156190d76bc801c59568b626ff9), [ae10df0](https://github.com/DPDK/dpdk/commit/ae10df04580e14b0a01da2aea8768362d0c931e6), [94cfe51](https://github.com/DPDK/dpdk/commit/94cfe51d7eec15d6e88c179fb8984bc7bb983e5e)
- Removed the unsupported SCTP receiving offload function in the ice network card driver.
  ↳ No PR: [58e315f](https://github.com/DPDK/dpdk/commit/58e315f5b724392f34a2eadbbb93c4a9076b1ac3)
- Added a datapath-specific log macro for the GVE driver, and migrated datapath-related log calls to this macro, achieving independent control of datapath logs and non-datapath logs.
  ↳ No PR: [74bfd4b](https://github.com/DPDK/dpdk/commit/74bfd4b804d274dd3b6402015e8370b42a292a85)
- Moved the eCPRI parser release function from the main source file to the flex parser-specific file and changed it to non-static for use in subsequent process cleanup steps.
  ↳ No PR: [05ae3e8](https://github.com/DPDK/dpdk/commit/05ae3e885a3bba75ea60a3d9bbd3b67cea879ef9)
- In testpmd, the jump to matcher action uses table ID instead of table pointer, and a corresponding parsing function is added.
  ↳ No PR: [a649d1c](https://github.com/DPDK/dpdk/commit/a649d1cda91355de27d43b935050d0ed60a71b63)
- Supports flow table query rate testing, adds the --query-rate command line option, and implements query process and statistical output.
  ↳ No PR: [cbaa982](https://github.com/DPDK/dpdk/commit/cbaa982521aa5dcc361d086c52affc81bad391f5)
- Added support for signature and verification operations of ECDSA SECP192R1, SECP224R1, SECP384R1 and SECP521R1 curves to the encryption performance testing tool.
  ↳ No PR: [83da718](https://github.com/DPDK/dpdk/commit/83da718261618e7a6d1663fdbe0143bafb79d3f5), [cb666bd](https://github.com/DPDK/dpdk/commit/cb666bd7f753f6ae75a4835d1346b0c8380c1912)
- Added partial encryption and decryption test cases for SM2 elliptic curve point calculation, and added ML-KEM's key generation, encapsulation and decapsulation test functions.
  ↳ No PR: [0a846b8](https://github.com/DPDK/dpdk/commit/0a846b84067e7b521688e28224f141f5110fa759)
- Added ECDH, ECPM, ECDSA elliptic curve tests and ML-DSA signature tests for QAT encryption devices.
  ↳ No PR: [bfa5c57](https://github.com/DPDK/dpdk/commit/bfa5c574602b3d177de7cbbaa4bdcaeb9c87a9b7)
- Added CPU encryption mode code path in block cipher test to improve CPU mode coverage.
  ↳ No PR: [bfaca6b](https://github.com/DPDK/dpdk/commit/bfaca6b17fd8e0bb69eb1aa4bf3608a9be777ce1)
- dmadev test supports SVA copy function, and adds related test cases and test entrances.
  ↳ No PR: [8ebe226](https://github.com/DPDK/dpdk/commit/8ebe22669c1f4edf095d4265651f109cd9e491b3)
- Add ELF loading functionality for BPF testing, including creating ELF files, writing loading and running tests, and skipping tests if libelf is not available.
  ↳ No PR: [cf1e03f](https://github.com/DPDK/dpdk/commit/cf1e03f881af08234892ab2649fb2953ffff52f5)
- Added BPF Rx/Tx filtering test, using null device, skipping the test if libelf is not available.
  ↳ No PR: [8103884](https://github.com/DPDK/dpdk/commit/81038845c90b56b991bb26c669a4d56940a56d66)
- Added port affinity matching and jumping to specified groups in the flow_filtering example, and added multiple code snippets that use jump flows.
  ↳ No PR: [e044839](https://github.com/DPDK/dpdk/commit/e044839bc864304b3422c123902bd1e8627235c3), [260325a](https://github.com/DPDK/dpdk/commit/260325a6c2cae7b687fb9de17652bf684f0caafe)
- Add instructions for multi-host LAG detection in the mlx5 driver documentation to guide users on how to query non-contiguous PF indexes.
  ↳ No PR: [1adf5b8](https://github.com/DPDK/dpdk/commit/1adf5b841c520959be1d1e5af4a08cc929f4f314)
- Updated mlx5 vDPA driver documentation, adjusted supported device list and reformatted header layout.
  ↳ No PR: [87f7895](https://github.com/DPDK/dpdk/commit/87f7895e470c13e13efd6762d701139d0987294a)
- Improve the description of the protocol-independent filtering function in the ICE driver documentation.
  ↳ No PR: [b060d31](https://github.com/DPDK/dpdk/commit/b060d31577519a7b9c3fe3a151f375fad96f218b)
- The IONIC driver documentation adds support information for Pollara 400 400G accelerator NIC.
  ↳ No PR: [899e7bb](https://github.com/DPDK/dpdk/commit/899e7bb0ab84a31a36437e8ad6e40493eea4b0ef)
- Update the firmware and kernel driver versions recommended in the i40e and ice network card driver documentation.
  ↳ No PR: [fe433b5](https://github.com/DPDK/dpdk/commit/fe433b5c99cfedbf976d167500797bb8cac799c2)
- Added Tx offload functionality with fast mbuf release for null network devices.
  ↳ No PR: [675ddc2](https://github.com/DPDK/dpdk/commit/675ddc233d68d90b3858cdb6267dd407c4e85984)
- The ethdev telemetry command adds the hide_zero parameter to support hiding zero values.
  ↳ No PR: [ba4d57b](https://github.com/DPDK/dpdk/commit/ba4d57bd849d68da0487b5d6da37dd116a552c7b)
- Added the function of exporting RSS algorithm information in telemetry.
  ↳ No PR: [8c77a97](https://github.com/DPDK/dpdk/commit/8c77a97ff4503c8eaead138b3260f46d126653e0)
- Added multi-queue support (4RX/2TX) and RSS functionality for 8126 and 8127 chips.
  ↳ No PR: [25e19d5](https://github.com/DPDK/dpdk/commit/25e19d532b4b5862d6b198a22086f20c6bf3a435)
- common/cnxk adds a new function to check whether the board supports 16B alignment.
  ↳ No PR: [ba7254a](https://github.com/DPDK/dpdk/commit/ba7254a8d1a608e6e14f5a733bf4983eb38c115a)
- Added backpressure configuration capability for eight traffic classes per pool for CN20K SoC.
  ↳ No PR: [bf9a339](https://github.com/DPDK/dpdk/commit/bf9a33976460e6de1cb1479d4f0b9bbee6ee1466)
- Add DPNI hotplug support for fslmc bus.
  ↳ No PR: [b5721f2](https://github.com/DPDK/dpdk/commit/b5721f271cbf20d38e8ebc10b9444d0d2512b67a)
- Improve the output information when testpmd processes command files, display the file name and end prompt.
  ↳ No PR: [e86ce47](https://github.com/DPDK/dpdk/commit/e86ce47f671665da89bfcf6e61677f3ce8f73949)
- Added missing macro definitions related to health status in the ice network card driver.
  ↳ No PR: [51f2066](https://github.com/DPDK/dpdk/commit/51f20660948558b9bd8cddf5b8f479b56d1c61ba)
- Added printing function of ECPRI header and message content to DPAA2 network driver.
  ↳ No PR: [bbf5575](https://github.com/DPDK/dpdk/commit/bbf5575dcc2f1142988ad282a6a7546ead1ed70e)

### bug fixes
- Fixed undefined behavior caused by arithmetic operations on null pointers and integer left shifts in port list parsing, using the RTE_BIT32 macro instead of direct shifts.
  ↳ No PR: [48e0347](https://github.com/DPDK/dpdk/commit/48e03475262798e6758b9c767e87e2f88375072c), [f3a07a3](https://github.com/DPDK/dpdk/commit/f3a07a33d7b3a0b153f7f5b60c13bebede9a9104)
- Fixed the left shift overflow problem in rte_rib6_insert caused by implicit promotion of ip_xor to int, and explicit conversion to uint32_t to avoid undefined behavior.
  ↳ No PR: [2f28e59](https://github.com/DPDK/dpdk/commit/2f28e596b956f0da5bcc0244fcf49d46544172de)
- Fixed the issue of incorrect path release in the net/bnxt driver due to LTO compilation, and instead jumped to the cleanup logic.
  ↳ No PR: [49b1673](https://github.com/DPDK/dpdk/commit/49b1673ec6693a673b4dc07984023f481cce4d96)
- Fix UBSan bug caused by misaligned memory access in predictable RSS.
  ↳ No PR: [b70d04d](https://github.com/DPDK/dpdk/commit/b70d04d8ac6d47b221500d418df1de2b2c65b50a)
- Fixed the 128-bit unaligned access problem in the stack implementation by adding alignment constraints to the structure.
  ↳ No PR: [a4f1591](https://github.com/DPDK/dpdk/commit/a4f1591e931fd7393257c15f7df4bf9672e30fe7)
- Fix the Tx vector path selection logic in the iavf driver to ensure that this path is selected first when AVX-512 is available and avoid error fallback to the scalar path.
  ↳ No PR: [ecdccc7](https://github.com/DPDK/dpdk/commit/ecdccc79cf3296bb3cb6d53d87ad85d13828677b)
- Fixed undefined behavior in the graph statistics module caused by calling memset with a NULL pointer, UBSan errors caused by non-aligned memory access, and memory leaks.
  ↳ No PR: [7c6410e](https://github.com/DPDK/dpdk/commit/7c6410ed8b1d800562dcf11ebd1784f6022c617d), [826af93](https://github.com/DPDK/dpdk/commit/826af93a68f358f8eb4f363e42d114b93fde0d69)
- Fix the size and initialization of extract buffer in dpaa2 driver, use rte_zmalloc to ensure zeroing, and adjust the maximum size to the correct structure size.
  ↳ No PR: [53bb620](https://github.com/DPDK/dpdk/commit/53bb620fa66ec89ee888573009771e0e9f279930)
- Fixed the traffic shaping rate configuration in the dpaa2 network card driver to correctly convert the byte rate given by the user into the bit rate required by the hardware.
  ↳ No PR: [953b557](https://github.com/DPDK/dpdk/commit/953b5576093dcd148b674bd2d53e5482970c1270)
- Enable software tail dropping for ordered queues in the DPAA2 driver, and enable congestion notification on traffic management queues by default.
  ↳ No PR: [0d2ffac](https://github.com/DPDK/dpdk/commit/0d2ffac0f6bb6d0a979a17d285f303c7076b4497)
- Fixed crash caused by null pointer dereference when listing timer adapters via telemetry.
  ↳ No PR: [94b2ff7](https://github.com/DPDK/dpdk/commit/94b2ff7ee1976f80dd4822dab090bbbf693d12ca)
- Fixed multiple issues in the GVE DQO send path: writing multiple descriptors to send the entire packet when a single mbuf exceeds the maximum buffer size; dropping packets and incrementing the count when there are insufficient descriptors; avoiding hardware rejection caused by writing zero-length descriptors.
  ↳ No PR: [ee06313](https://github.com/DPDK/dpdk/commit/ee06313a50a8ebf18254a923152bf6729771cbc2), [92d330a](https://github.com/DPDK/dpdk/commit/92d330a3eabb1ca2f74d494ebea0104bc7fd081f), [671d15d](https://github.com/DPDK/dpdk/commit/671d15dad5f41cda4887ca3bb73afafc1b9768e3)
- Fixed the validity check before sending Tx data packets in the GVE driver to avoid hardware disabling transmission due to mbuf errors.
  ↳ No PR: [f33ce44](https://github.com/DPDK/dpdk/commit/f33ce4445ee6bc8f6d2ea4d894511f5446e9e3a2)
- Enforce a limit on the number of descriptors in the GVE driver DQO Tx path, setting the maximum number of data descriptors per MTU segment to GVE_TX_MAX_DATA_DESCS.
  ↳ No PR: [f4a70b4](https://github.com/DPDK/dpdk/commit/f4a70b449bfac5343bf498f4132d5b8da4b0a885)
- Fix the problem of limiting the number of TSO segment descriptors in the GVE driver DQO queue, and add a verification function to ensure that each MTU size segment uses at most 10 data descriptors.
  ↳ No PR: [be8f0eb](https://github.com/DPDK/dpdk/commit/be8f0eb81f987cbd64c2d37fe6f8b2e888328f23)
- Fixed the problem of GVE driver DQO sending descriptor not being cleared, causing hardware misunderstanding. The descriptor should be cleared and initialized before writing.
  ↳ No PR: [4ef9cf4](https://github.com/DPDK/dpdk/commit/4ef9cf43d0ee57e082cb9e89f47756f3414171a4)
- Fix the string length limit of the set core list command in testpmd, replacing fixed-length strings with variable-length strings to support more cores.
  ↳ No PR: [d0f4f07](https://github.com/DPDK/dpdk/commit/d0f4f0779898e41a940e9a6f83f782750ffbfbb7)
- Fixed the GTP tunnel type UDP tunnel mark support in the i40e driver, and fixed the L3 header offset calculation error when GTP packets are sent for checksum offloading.
  ↳ No PR: [cdebcc4](https://github.com/DPDK/dpdk/commit/cdebcc490f6a476755ab3c6726f86105ed90f0b3)
- Fix the error handling when MAC configuration fails in the ZXDH driver, optimize resource release when the device is shut down and error code judgment in MAC address operations.
  ↳ No PR: [b64747e](https://github.com/DPDK/dpdk/commit/b64747ef2951287be66502b900853957cd4bca99)
- Fixed issues with VLAN filtering and port VLAN attribute settings in the ZXDH driver, and added VF VLAN table initialization support.
  ↳ No PR: [9ceb295](https://github.com/DPDK/dpdk/commit/9ceb2950d6f169eb5a11031f7a9f37090673bab0)
- Fixed the problem that the short PCI device name in testpmd could not be correctly recognized. When attach_port, normalize it to the long format before searching for the device.
  ↳ No PR: [12c2405](https://github.com/DPDK/dpdk/commit/12c2405989f6fb002a1c45e892b82897d124d10a)
- Fixed the problem in the octeon_ep driver that the return value is not processed correctly when the interrupt enable fails, and returns gracefully when the file handle is unavailable.
  ↳ No PR: [0fcfecc](https://github.com/DPDK/dpdk/commit/0fcfecc1f1eb3d8b1e8632134462caf3b3885281)
- Fix mbuf data offset update in octeon_ep driver, use rearm data instead of directly modifying data_off, and remove redundant refill count update.
  ↳ No PR: [74348d7](https://github.com/DPDK/dpdk/commit/74348d7ad2503960611e979677acad4b4641e7dd)
- Fix the TX and RX doorbell processing logic when the octeon_ep driver device starts, ensuring that pending packets in the RX queue are emptied and refilled before starting.
  ↳ No PR: [c892964](https://github.com/DPDK/dpdk/commit/c892964faa605c7884b454b435c4fb663dff0c9e)
- Adapt the LS1043A errata for the DPAA memory pool, adjusting each element through the populate callback to ensure that the starting DMA address is 16B aligned and 256B aligned when crossing 4KB boundaries.
  ↳ No PR: [2885165](https://github.com/DPDK/dpdk/commit/2885165676bdd5b3017bccd65e74310d0e91ff8e)
- Fix the SCTP port filtering function on the E610 device in the ixgbe driver, and add the device to the list of devices that support SCTP ports.
  ↳ No PR: [98c359e](https://github.com/DPDK/dpdk/commit/98c359e33004afa3027e83c60c8d1bb6e240fe6b)
- Fixed the problem in ipsec_mb PMD that when the secondary process releases queue pairs, it may mistakenly release queue pairs that do not belong to itself. By adding process ID checks, it ensures that only queue pairs owned by itself are released.
  ↳ No PR: [0e03ab6](https://github.com/DPDK/dpdk/commit/0e03ab647d07cd985a7cac36cefff5195cc3a07d)
- Fixed a memory leak caused by internal cache memory not being released in debug mode when ipool is destroyed.
  ↳ No PR: [83d3188](https://github.com/DPDK/dpdk/commit/83d3188f47fe98a17c17129d85b47797d8bf63a7)
- Fixed an issue where heap memory allocation in the fallback path did not enforce 8-byte alignment, use posix_memalign instead to ensure alignment requirements are met.
  ↳ No PR: [358dc17](https://github.com/DPDK/dpdk/commit/358dc17edcdf00fa5ec423b09e185846df979078)
- Fixed the asynchronous event processing logic. When an asynchronous event is unexpectedly received, confirm and continue waiting until the expected event is received.
  ↳ No PR: [21b631c](https://github.com/DPDK/dpdk/commit/21b631cd0d3670e375151185d74cd5a03888e2bd)
- Fixed the issue where the default flow rule creation failed when the proxy port was not started in HWS mode, causing the port representative to fail to start. Instead, the failure was ignored and the debug log was recorded, and an early return check was added when flow control was disabled.
  ↳ No PR: [6f4909d](https://github.com/DPDK/dpdk/commit/6f4909dfa017aacfca6a3fc89d014d474b1fbc6a)
- Fixed the problem that the representative port cannot traverse its shared Rx queue after the transport agent port is closed, and the shared and non-shared Rx queues are stored in different lists.
  ↳ No PR: [a0a7903](https://github.com/DPDK/dpdk/commit/a0a7903376f2252b06ae272b2c3b69e9b939de04)
- Fixed the ESP header matching issue in strict mode, added implicit matching for IP.proto value 50, and implicit matching for UDP.dport value 4500 when ESP over UDP.
  ↳ No PR: [f2f75ff](https://github.com/DPDK/dpdk/commit/f2f75ffe14a521ee3000be2b5286ff3047f3958c)
- Fixed the problem of incorrectly writing the interrupt mask bit when starting the Rx queue in DQ queue format, and changed to correctly setting the interrupt-free mode.
  ↳ No PR: [8a6418e](https://github.com/DPDK/dpdk/commit/8a6418e11a4d9e3554d592b1b3e3957fea8e7cee)
- Fixed an ASan error in the MLX5 driver when the RSS stream was created due to composite literals that caused the stack memory to be accessed after it was released. The jump action configuration was changed to perform persistent stack allocation at the beginning of the function.
  ↳ No PR: [b7dedd0](https://github.com/DPDK/dpdk/commit/b7dedd019a034331fbc67b1d10d59bf3531b5048)
- Fixed the setting of the VLAN offload flag in the ice network card vector Rx path, replacing the generic VLAN offload flag with the respectively supported VLAN stripping and filtering flags to solve the problem of not supporting QinQ.
  ↳ No PR: [cf454a5](https://github.com/DPDK/dpdk/commit/cf454a5794bf4e3c18cd8a4e449c3d8ded5b30e6)
- Fixed the double free problem in non-template stream destruction to avoid use-after-free caused by repeated release of matchers when creating rules fail due to insufficient memory, and clear freed pointers in the destruction function to prevent potential double-free.
  ↳ No PR: [7867b5d](https://github.com/DPDK/dpdk/commit/7867b5d7a545f32aa6e6c5b4b406434581a0166b)
- Fixed an issue in the ice driver where VLAN tags were not reported correctly on reception due to incorrect modification of the l2tsel field.
  ↳ No PR: [fba64e0](https://github.com/DPDK/dpdk/commit/fba64e026d03f4926e1ddc15a2128b8447b73d69)
- Fixed a race condition when refreshing non-template age rules to prevent the age sampling callback from accessing released resources during age or counter release, causing assertion failure.
  ↳ No PR: [7fb2007](https://github.com/DPDK/dpdk/commit/7fb2007bb1fc0b949661e316cfa60bbdf60e54ac)
- Fixed the definition of ifname parameter in mlx5_get_ifname function, changed it from pointer to character buffer, and updated related calls.
  ↳ No PR: [9e58a50](https://github.com/DPDK/dpdk/commit/9e58a50c059f3760c51ddee16073496c6e1d510a)
- Fixed the problem of conntrack action query failure in testpmd, added processing of RTE_FLOW_ACTION_TYPE_CONNTRACK in the switch branch of action type filtering, and added instructions for querying conntrack status commands in the user guide.
  ↳ No PR: [d23bcfb](https://github.com/DPDK/dpdk/commit/d23bcfb1821cf134deb6e7ae171fcf0238a8bc98), [307b5b4](https://github.com/DPDK/dpdk/commit/307b5b42b6258b8a8deecdf13cc334b3ceffe4a7)
- Fixed the fallback behavior of the sfc driver when the firmware does not support the new netport API, falling back to using the EF10 generic PHY and MAC methods on Medford4 devices to maintain the old behavior.
  ↳ No PR: [2c2fd34](https://github.com/DPDK/dpdk/commit/2c2fd3488a783f0af20857667b8f75b3022d03b6)
- Fixed the problem that TIR action is not allowed in the FDB domain in the HW Steering engine, thus supporting the use of RSS actions in transfer flow rules.
  ↳ No PR: [1fca53b](https://github.com/DPDK/dpdk/commit/1fca53b789db81921389efb47cde3afbc1205e8e)
- Fixed an issue in Direct Verbs counter offset detection incorrectly passing exit flags into the type field, avoiding false positive results being returned on older versions of rdma-core.
  ↳ No PR: [d953431](https://github.com/DPDK/dpdk/commit/d953431da8e1ece042e33ba71650a3ba6b1e27c1)
- Fixed the issue of VLAN resources not being released when hns3 driver initialization failed, and encapsulated the hns3_uninit_hardware() function to release hardware resources uniformly.
  ↳ No PR: [4816b10](https://github.com/DPDK/dpdk/commit/4816b1005bd650b4a1e10af913c497bec860bec5)
- Fixed the problem of mbuf being incorrectly overwritten in the vector path. When the mbuf cannot be applied for, point the mbuf to fake_mbuf to prevent subsequent modifications.
  ↳ No PR: [06b296a](https://github.com/DPDK/dpdk/commit/06b296a2264fcd1fe2d167f2d90a58607f5e81f5)
- Fixed a memory leak problem caused by the GVE driver failing to allocate some mbufs and not releasing the successfully allocated buffer when creating an RX ring.
  ↳ No PR: [fa48f96](https://github.com/DPDK/dpdk/commit/fa48f964253ba018b4a3054246a6e26b31b5c8b0)
- Fixed the input setting and result collection logic of the ECDH implementation in the QAT driver, corrected the data source reference and added branch processing of the key exchange type.
  ↳ No PR: [0f5b7d6](https://github.com/DPDK/dpdk/commit/0f5b7d65c85205a792fe146316eb01279eabc8a2)
- Fixed the parameter reading problem of ECDH key exchange in the QAT driver, and instead obtained the EC parameters from xform to avoid the situation that they may not be set in asym_op.
  ↳ No PR: [25ef596](https://github.com/DPDK/dpdk/commit/25ef596203a94c79b1c9fa8504839c3f41da1a57)
- Added validation of the number of DSCP and VLAN table entries for testpmd's meter creation, limiting the maximum number of entries.
  ↳ No PR: [00092e9](https://github.com/DPDK/dpdk/commit/00092e969aad2fb2a2017b7eec86f033d4527950)
- Fixed a race condition in mlx5 driver device detection, introduced an asynchronous monitor ready flag, ensured that port information updates are only handled by the monitor thread after it is ready, and removed the old direct update function.
  ↳ No PR: [cb4c87f](https://github.com/DPDK/dpdk/commit/cb4c87f0fc8e7c3928cfd80d85c51cb1698cbe93)
- Fixed an issue in the mlx5 driver where multicast MAC address traffic was incorrectly disabled, default rules for multicast MAC addresses are now correctly created when traffic is enabled.
  ↳ No PR: [8c06434](https://github.com/DPDK/dpdk/commit/8c06434cd9e44ef8a4db2eb7e3300c7791c4e7b4)
- Fixed an issue where the xsc driver used uninitialized MAC address variables when initializing the representative port.
  ↳ No PR: [a881be7](https://github.com/DPDK/dpdk/commit/a881be76fe0f3d9f21b72e7fbc76598b9ab7f727)
- Fixed an issue in testpmd where the IPv6 extension header was not processed correctly when obtaining the L4 protocol from the L3 header.
  ↳ No PR: [4961596](https://github.com/DPDK/dpdk/commit/496159613ffc7b6ba592432a1ba4d1a38f6935de)
- Fixed the payload corruption problem caused by incorrect operation of tail packet update TCP flag when GRO merges packets.
  ↳ No PR: [33358cc](https://github.com/DPDK/dpdk/commit/33358ccc291fbc39d93b3c3975bebec1c38ab56d)
- Fixed the problem of repeated or incorrect settings of the vector Rx queue in the i40e driver, and removed the redundant setting logic before path selection.
  ↳ No PR: [7599b94](https://github.com/DPDK/dpdk/commit/7599b9494715f78b2b71442381effc56380a4d9b)
- Fixed the calling order error in the ice_add_adv_recipe function, moving ice_get_sw_fv_list after ice_add_special_words to ensure that special words can be parsed correctly.
  ↳ No PR: [e563992](https://github.com/DPDK/dpdk/commit/e563992fba809bcae90b4734f555e354024ec564)
- Fixed the issue where the ice driver's MAC VLAN filtering rules match the inner VLAN in dual VLAN mode, and introduced a recipe ID override mechanism to correctly match the outer VLAN.
  ↳ No PR: [d5f5b3d](https://github.com/DPDK/dpdk/commit/d5f5b3d77ebfb1dd5bbd5166ab79d42a4c1ccc71)
- Fixed the issue in the ice driver that the core reset was not triggered when the ice_cfg_tx_topo function configuration failed. Ensure that the core reset is performed regardless of success or failure to release the global configuration lock to avoid subsequent DDP loading failures.
  ↳ No PR: [b47c122](https://github.com/DPDK/dpdk/commit/b47c1229d61719e3b3c298406a99efb077295c62)
- Fixed the problem in the ice driver that discarded packets in the receiving direction were not included in statistics, and adjusted the byte count source.
  ↳ No PR: [af05f9e](https://github.com/DPDK/dpdk/commit/af05f9e37153c53335938bcde2978a359c5f4efa)
- Fixed the sfc_efx driver auto-negotiation detection logic, no longer relying on the dynamic AN status of the link partner.
  ↳ No PR: [7085716](https://github.com/DPDK/dpdk/commit/70857163b72a4d9fb23b0e5685743e56a96b0277)
- Automatic negotiation flow control of the sfc_efx driver is enabled by default to speed up link establishment.
  ↳ No PR: [6a66e30](https://github.com/DPDK/dpdk/commit/6a66e3001484fcf66dcec435b858954114716fb6)
- Fixed an issue where netport MCDI automatic FEC selection was ignored in the sfc_efx driver.
  ↳ No PR: [7066cd6](https://github.com/DPDK/dpdk/commit/7066cd699ba46336e6346af437f7d2729f7a4a99)
- The last FEC configuration is retained by default when the sfc_efx driver port is initialized to avoid link interruption.
  ↳ No PR: [0185388](https://github.com/DPDK/dpdk/commit/0185388484f6170b33efc3a4cee92a92ea0e7800)
- Fix the use-after-free problem that may occur when xsc driver Rx queue is cleaned.
  ↳ No PR: [cbfd2eb](https://github.com/DPDK/dpdk/commit/cbfd2eb334ae6cec3c95be46c02917f821fb251f)
- Fixed the problem of ESP matching in strict mode, adding implicit matching for IP.proto value 50 and UDP.dport value 4500 when ESP over UDP.
  ↳ No PR: [4237d1e](https://github.com/DPDK/dpdk/commit/4237d1efa6e3f7f18ba809aa2073640fb034ae8d)
- Fix ESP item validation, allowing hardware steering engine to match ESP serial number.
  ↳ No PR: [96d73a9](https://github.com/DPDK/dpdk/commit/96d73a947331cc146e09b06a6913cdf604ae52a7)
- Fixed the problem of ESP header matching after UDP packets in group 0, ensuring that when the UDP header exists, the matching IP protocol is no longer forced to be ESP.
  ↳ No PR: [ed8eb60](https://github.com/DPDK/dpdk/commit/ed8eb60c9b2c243b4098f59dc6d9a87ee0bbd4c8)
- Fixed the problem that the af_packet driver crashed due to using strdup to allocate interface names in the secondary process. Instead, use rte_malloc to allocate memory and adjust the release method accordingly.
  ↳ No PR: [d57124f](https://github.com/DPDK/dpdk/commit/d57124f60ef60b24cd39e895cf6d211b93b897ae)
- Fixed the problem of repeatedly releasing mbuf when releasing Rx queue in net/ark driver, and renamed related functions to maintain naming consistency.
  ↳ No PR: [f8c8505](https://github.com/DPDK/dpdk/commit/f8c85054cc9cb160ca12e1bf96b569e654f96c74)
- Fixed an issue where the IPv4/6 protocol field was not copied correctly in flow encapsulation hash calculation, ensuring that the hash calculation includes the correct next protocol field.
  ↳ No PR: [7658334](https://github.com/DPDK/dpdk/commit/76583343fb62bf416500ee0df87c934cea18a979)
- Added workaround for polling virtqueue ready status for VDUSE device startup to resolve timing issues.
  ↳ No PR: [84350b1](https://github.com/DPDK/dpdk/commit/84350b1f470558836b61ff1347f660e06c81cbf5)
- Fix vduse_vq_info structure not being initialized in VDUSE virtual ring setup, ensuring all fields start with known values.
  ↳ No PR: [db91578](https://github.com/DPDK/dpdk/commit/db91578981c6869d4ee476347141c0fccd1d6146)
- Use synchronous callback logout during the interrupted uninstallation process to ensure that no callback is running after the interrupted uninstallation, improve the stability of the device during disassembly and avoid usage problems after release.
  ↳ No PR: [056bbaa](https://github.com/DPDK/dpdk/commit/056bbaa7d7d752b49468246f06593dea41e8ee75)
- Fixed the memory leak problem of indirect flow action, releasing the unreleased handle when destroying the asynchronous action list handle.
  ↳ No PR: [a7aeb6a](https://github.com/DPDK/dpdk/commit/a7aeb6ac678c6a0bd45584091529ac6fa6ac58b1)
- Fixed the problem of the secondary process crashing due to forwarding not stopping when the primary exits, and adding a multi-process communication mechanism to notify the secondary to stop forwarding before the primary exits.
  ↳ No PR: [f96273c](https://github.com/DPDK/dpdk/commit/f96273c8e9d39e472bb07acc05e493b1e712e51b)
- Fix WRR token data type, change wrr_tokens array from uint8_t to uint16_t to avoid token truncation.
  ↳ No PR: [8dc7bf9](https://github.com/DPDK/dpdk/commit/8dc7bf943fb6fad7b30b3a494f2216c2c4cf64d7)
- Fixed security vulnerabilities (buffer overflow and type error) in parsing tail drop and XQE drop parameters in the cnxk driver.
  ↳ No PR: [143115b](https://github.com/DPDK/dpdk/commit/143115be04ef4ae3094e0e4e68102d87ff18b753), [de91111](https://github.com/DPDK/dpdk/commit/de91111308b5e1cca03ace9b2cbc6165264b2e42)
- Fix the build problem of GFNI on x86: add the missing rte_cpuflags.h header file inclusion in rte_thash.c to solve the compilation error caused by implicit function declaration.
  ↳ No PR: [9a3c7ae](https://github.com/DPDK/dpdk/commit/9a3c7ae9c7c645d35f1253d39a5c48bf5a040b68)
- Refactor the RSA verification operation to avoid copying the decrypted message to the signature buffer and preventing overwriting of the input buffer.
  ↳ No PR: [dfd038b](https://github.com/DPDK/dpdk/commit/dfd038b97ec3d173ded0f985df39301b7c7662f2)
- Fixed the issue of short tunnel frames losing VLAN tags when VLAN insertion is enabled, padding the tunnel frame length to 65 bytes.
  ↳ No PR: [2262fc2](https://github.com/DPDK/dpdk/commit/2262fc29485bd863db55e820a194bf1e4be8a87c)
- Fixed the problem of ACL configuration failure when initializing 8-port devices. When the number of PFs exceeds 4, the TCAM depth is halved to avoid insufficient memory.
  ↳ No PR: [17a8fc2](https://github.com/DPDK/dpdk/commit/17a8fc206178c6b354a8fde04c23cf29db044961)
- Fixed a crash issue when running debug_autotest on mlx5 devices due to the fork child process calling rte_exit() causing shared memory to be released early.
  ↳ No PR: [2b403dd](https://github.com/DPDK/dpdk/commit/2b403dd8fb37d0ba13723e44ffc7ee2c2795f838)
- Fixed the memory leak problem of unreleased stream index pool, and added a function to release all stream index pools.
  ↳ No PR: [eefec46](https://github.com/DPDK/dpdk/commit/eefec46eeb89672815afd6c2497d21b928d77c54)
- Fixed the problem of resource leakage caused by not closing the file descriptor when the UIO device file read error occurred in the enetfec driver.
  ↳ No PR: [2e50321](https://github.com/DPDK/dpdk/commit/2e503215692e8ab50e473e963ec58d5ab714a375)
- Fixed receive queue descriptor ring size configuration in enetfec driver, forcing a fixed size to ensure correct buffer allocation.
  ↳ No PR: [f034c09](https://github.com/DPDK/dpdk/commit/f034c096b86ed79345cc1f83c6191713b2814fb0)
- Fixed the problem of incorrectly releasing the RX queue pointer when releasing the TX queue in the enet_free_queue function.
  ↳ No PR: [f0aa802](https://github.com/DPDK/dpdk/commit/f0aa80200d87e38a613af1181a2b1048bd512c76)
- Fixed the conditional judgment of TX checksum unloading in the enetfec driver, and corrected the data cache operation instructions.
  ↳ No PR: [b35089c](https://github.com/DPDK/dpdk/commit/b35089c52802378ed267717f069aa57cb8dce5d2)
- Fixed the multi-TX queue configuration problem in the enetfec driver. Now only single queue mode is supported and multi-queue configuration is rejected.
  ↳ No PR: [b1c1628](https://github.com/DPDK/dpdk/commit/b1c162858c1efc31c8b4ac26b5943b7b8dd65bf8)
- Fixed the memory leak problem caused by Rx buffer cleaning in the enetfec driver without checking whether the mbuf is NULL before releasing it.
  ↳ No PR: [979d007](https://github.com/DPDK/dpdk/commit/979d00728b01a77f8f67f46c7cb06e2628542d29)
- Reject unsupported Tx deferred start and multi-queue configurations in enetfec PMD, and fix the problem of incorrectly releasing rx_queues when queue is released.
  ↳ No PR: [dd6b357](https://github.com/DPDK/dpdk/commit/dd6b3572a310d0f3e045d8e9d1eb5f6181729d08)
- Change the cache operation of forwarded packets from flush only to flush and invalidate to ensure data consistency.
  ↳ No PR: [4966137](https://github.com/DPDK/dpdk/commit/496613734f02534b77631df859073f8824e4df41)
- Fix memory leak and tbl8 entry allocation check logic in trie module in IPv6 FIB, allowing use of all pre-allocated tbl8 entries.
  ↳ No PR: [f4905fd](https://github.com/DPDK/dpdk/commit/f4905fdcf6b43ee1499e431ca433fd7570c71224), [f0db0f6](https://github.com/DPDK/dpdk/commit/f0db0f659a1f4192a4aca7ce2a298f272aa3af8f)
- Fixed the wrong function and uninstallation definition of Rx path in iavf driver, and added flexible descriptor path support.
  ↳ No PR: [9c74047](https://github.com/DPDK/dpdk/commit/9c74047ef4b75ef4f933f39cf264d10cb8c1f850), [6e94481](https://github.com/DPDK/dpdk/commit/6e94481c6729590ff504fced0a6c770aeed60623)
- Fixed TSO segmentation processing in the net/rnp driver, performing multi-descriptor fragmentation on TSO packets exceeding 64KB to avoid segmentation exceptions; also repaired the VLAN header boundary check and protocol header type verification of tunnel TSO.
  ↳ No PR: [ebcbbfd](https://github.com/DPDK/dpdk/commit/ebcbbfd71817ccf0ae52cee0ba1e199959996132), [ca76668](https://github.com/DPDK/dpdk/commit/ca76668fd5efc03e127d2da4e9645b1a34b75bc7)
- Fix the parameter validity check of the firmware capability acquisition and speed capability acquisition functions in the net/rnp driver to avoid logic exceptions caused by illegal firmware information; fix the crash problem caused by memory overflow when using the --no-lsc-interrupt option for link updates.
  ↳ No PR: [343a065](https://github.com/DPDK/dpdk/commit/343a06525677415d7b8c7af4a0e2f7c2cecd14ac), [ba3641d](https://github.com/DPDK/dpdk/commit/ba3641decf649330e29c357a9b251dda3dbad0ee)
- Remove the hard-coded memory channel parameter -n4 in the pdump tool, optimize parameter handling to avoid duplicate proc-type flags, and add a check on the main process survival status when exiting; fix the integer type of intermediate bursts, use unsigned integers to avoid wraparound warnings.
  ↳ No PR: [4a8d8db](https://github.com/DPDK/dpdk/commit/4a8d8db495f66b22ce0c12055b1c9f704f542152), [3cf21a8](https://github.com/DPDK/dpdk/commit/3cf21a8b7a803fb590632d3fe85cabbe50b2ecc2), [22fc97b](https://github.com/DPDK/dpdk/commit/22fc97ba1d67f18d10e29ace2f19f8c0d52534e3)
- Fixed multiple stability issues in the DMA performance testing tool: fixed the use-after-free problem caused by still using its pointer after cfgfile is closed; added configuration error information, output specific error information and exit when a required entry is missing in the configuration file; fixed the problem that there may still be DMA in transit when the worker thread exits, and added a wait for DMA completion phase before exiting; fixed two problems that may occur when stopping the device.
  ↳ No PR: [e605615](https://github.com/DPDK/dpdk/commit/e605615db7d4b104f41fc8f409eb569e962710d8), [e588b02](https://github.com/DPDK/dpdk/commit/e588b0265b2bff0a00e9908d395282b13c109233), [d1b3b66](https://github.com/DPDK/dpdk/commit/d1b3b669674a17c58eabf3d631b21aaad7232403), [cca4c3b](https://github.com/DPDK/dpdk/commit/cca4c3bc3feb16226480ea9b3c1dc5e7f0116fee)
- Fixed a resource leak issue in which the VFIO device file descriptor was not released when the PCI bus secondary process failed to obtain region information.
  ↳ No PR: [6ca08d3](https://github.com/DPDK/dpdk/commit/6ca08d36ba7310edfe96207b299f79221b7e2d37)
- Fixed the device name display issue in CDX bus detection error messages, replacing unused variables with the correct device names.
  ↳ No PR: [ebd507b](https://github.com/DPDK/dpdk/commit/ebd507b220b58ff8e2e87d1c2fce51cb1d4420d1)
- Fixed the problem of incorrect release device address when detecting the CDX bus secondary process. The correct device name is now used.
  ↳ No PR: [ad13df8](https://github.com/DPDK/dpdk/commit/ad13df8e9379c5f17e6548eca1ae829f71795fde)
- Fix cleaning order of PCD and FMan handles in dpaa_fm_init function to prevent resource leaks.
  ↳ No PR: [e7665de](https://github.com/DPDK/dpdk/commit/e7665de896836e99866ef8016bbaa12223e1cfb7)
- Fixed a memory leak in the inflate checksum function in the zlib compression driver, releasing the dictionary memory before the end of the function.
  ↳ No PR: [e1627f2](https://github.com/DPDK/dpdk/commit/e1627f25daafaa50c7f05a24592b17fa2b6bb8ea)
- Fixed the checksum error count of the receive path in the txgbe driver, so that the rx_l3_l4_xsum_error statistics can be accumulated correctly.
  ↳ No PR: [b9ad8a6](https://github.com/DPDK/dpdk/commit/b9ad8a6e728aff2c6628f07d41d54f6ca89b936b)
- Fixed the problem that the rx_l3_l4_xsum_error statistics in the ngbe network card driver is always 0, and correctly counts the checksum error count in the receive path.
  ↳ No PR: [6280a30](https://github.com/DPDK/dpdk/commit/6280a306079840301b2cd4eee472142964c2e9f6)
- In receive queue settings, changed memory allocation for ring descriptors from maximum ring size to actual ring size, and fixed virtual function detection logic.
  ↳ No PR: [843c59d](https://github.com/DPDK/dpdk/commit/843c59d1c2cef10a75037ebc73460f2ed28f9839)
- Changed the memory allocation of the ring descriptor from the maximum ring size to the actual queue size to reduce memory usage; also corrected the return type of the receive queue count function.
  ↳ No PR: [22d4fff](https://github.com/DPDK/dpdk/commit/22d4fffbbc99ef2a229869e717a12b2e33c68a9c)
- Fixed the issue with the receive buffer size configuration register in the txgbe VF driver, changing the rounding up to rounding down to avoid segfault caused by receiving over-long packets in LRO mode.
  ↳ No PR: [ee2bc2d](https://github.com/DPDK/dpdk/commit/ee2bc2d16c6d1c59d8f5eae16a874866e3a60de7)
- Fixed the VF device receive buffer size configuration, changing from rounding up to rounding down, to avoid segfault caused by hardware receiving overlong packets in distributed mode.
  ↳ No PR: [f95d28f](https://github.com/DPDK/dpdk/commit/f95d28fe1919cf4b245d6e9fb2f6ac34a9ac0e14)
- Fixed the issue where the maximum number of FDIR filters does not match the actual limit of the hardware, so that the hash table size is dynamically calculated based on the memory space allocated by the hardware to avoid creating rules that exceed what the hardware allows.
  ↳ No PR: [5b1429f](https://github.com/DPDK/dpdk/commit/5b1429fe2674e331d21a8c343d4129e6b7fbcce5)
- Fixed the issue that the FDIR mode was not reset after clearing all FDIR flow rules to avoid failure to create new rules; and also differentiated the FDIR programming paths of PF and VF.
  ↳ No PR: [26048c2](https://github.com/DPDK/dpdk/commit/26048c25942f2579a821a99b78db48fdb2c90c77)
- Fixed the limitation of FDIR drop action on L4 matching packets in the txgbe driver, and removed redundant hardware type and port checks.
  ↳ No PR: [3c858be](https://github.com/DPDK/dpdk/commit/3c858be4997d779a05dd32630ad57c740a2729bc)
- Fixed an issue in the txgbe driver that caused the SCTP tunnel packet FDIR filter to not work properly due to repeated and incorrect mask checks when creating it.
  ↳ No PR: [c9a3410](https://github.com/DPDK/dpdk/commit/c9a341034a29bc5245dd9fc21678be0b30313394)
- Fixed the tunnel packet FDIR filtering support for RAW pattern matching in the txgbe driver, and corrected the relevant checking logic.
  ↳ No PR: [02c9cc1](https://github.com/DPDK/dpdk/commit/02c9cc101281ebf75148de8324455cdc8cbc3baa)
- Fix the FDIR input mask setting in the net/txgbe driver to comply with the hardware requirements (IPv4 mask little endian, IPv6 mask bit inversion), and apply the mask correctly instead of manually clearing it.
  ↳ No PR: [a2d4de2](https://github.com/DPDK/dpdk/commit/a2d4de27109033d5061da44aed919bf46cfd7ca9)
- Fixed the issue where the VF-PF message box only clears the first 4 bytes when adding ntuple flow filter to txgbe network card VF.
  ↳ No PR: [3872d42](https://github.com/DPDK/dpdk/commit/3872d42feb88be81e55af6b48a18bd3afe6815b5)
- Fixed an error in the memory allocation size described by node expansion statistics, replacing the incorrect sizeof macro with the correct macro value.
  ↳ No PR: [cdeb353](https://github.com/DPDK/dpdk/commit/cdeb35313438f6a99c6c9233c89746b9bd86f9f6)
- Fixed the compilation error of iavf driver under clang 21, and initialized the uninitialized variable notify_byte to 0.
  ↳ No PR: [ffa370c](https://github.com/DPDK/dpdk/commit/ffa370cf683a1dd37914a54b243ec38a237b3930)
- Fixed clang compilation warning caused by extra commas in mlx4 driver.
  ↳ No PR: [fdffa18](https://github.com/DPDK/dpdk/commit/fdffa18268a70857865141cd89066eb6e025c0d2)
- Fix clang compilation warnings caused by unnecessary comma expressions.
  ↳ No PR: [3b769d8](https://github.com/DPDK/dpdk/commit/3b769d8389080ef0fd1b34765b9844db8f40729a)
- Fixed the null pointer dereference problem caused by the data being cleared after the upstream library releases the port when the representative port in the bnxt driver accesses the parent device. This can be avoided by adding an existence check for the parent device.
  ↳ No PR: [438b92e](https://github.com/DPDK/dpdk/commit/438b92e8ef2e3e6514ca2386cd57d145e21b3a57)
- Fixed lookup table pool size calculation to include static buckets and starting offsets into the pool capacity to avoid crashes when a large number of streams are unloaded.
  ↳ No PR: [a68a9bc](https://github.com/DPDK/dpdk/commit/a68a9bcec60c5d9a0a70d00ae38fc04659503523)
- Fixed pool size calculation error in Thor2 TF table scope sizing, make sure flow counts and max_pools are powers of 2 to avoid rounding errors.
  ↳ No PR: [a076e73](https://github.com/DPDK/dpdk/commit/a076e73a52353f39fca2a91d7c86d877ad23fea5)
- Fixed the problem that the representative stream was not deleted during VFR cleaning, and fixed the problem of statistics counter thread lock.
  ↳ No PR: [5b6998a](https://github.com/DPDK/dpdk/commit/5b6998aaad6ec024d5cdbc7bfe967238db2d9e36)
- Add null pointer check when destroying meter to avoid crash when Thor does not support meter stats; fix format of bit allocator error message.
  ↳ No PR: [4e38a2c](https://github.com/DPDK/dpdk/commit/4e38a2cd3ea24a20a53f36d983fb3109234535f8)
- Fixed packet count error for OVS traffic, instead always accumulating full counts instead of read-clearing, to avoid count loss due to rapid reset of statistics counters.
  ↳ No PR: [3f5559b](https://github.com/DPDK/dpdk/commit/3f5559bd117434a7d54f5b93f886243e3619f3ea)
- Fixed the default RSS configuration failure problem in the bnxt network card driver due to the mutual exclusion of IPV6 and IPV6_FLOW_LABEL hash types. Only set IPV6_FLOW_LABEL when configuring the hardware, and ensure that both types are reported at the same time when obtaining the configuration.
  ↳ No PR: [ab31723](https://github.com/DPDK/dpdk/commit/ab31723cd48dd46004447bdbe52a6d27adfb01bd)
- Fixed an issue with the table scope closing sequence when Thor2 hot upgrade exits abnormally. The function identifier is removed first and then the memory is released to avoid the firmware deleting scopes repeatedly.
  ↳ No PR: [cfb2217](https://github.com/DPDK/dpdk/commit/cfb22172f72a0cc26d4e05183fab1354139a8609)
- Fixed the MPC completion out-of-order problem, associated requests and completions through the opaque field, and supported out-of-order completion in batch processing.
  ↳ No PR: [19d8c7c](https://github.com/DPDK/dpdk/commit/19d8c7c9aab8f6899a41ad058319af8b97336389)
- Fixed the UDP tunnel port count issue in the bnxt network card driver to avoid incorrectly increasing the count when adding the same port repeatedly.
  ↳ No PR: [7f66db0](https://github.com/DPDK/dpdk/commit/7f66db0347b8b938c354a8dbccfc663165929d49)
- Fixed a crash issue during VFR processing in the bnxt driver, enhanced representor port parameter validation and prevented duplicate port attachment.
  ↳ No PR: [0beb39a](https://github.com/DPDK/dpdk/commit/0beb39a3fb011526805a7d56deab9ab7afa8e6b8)
- Fixed the problem of configuration failure in the bnxt driver when the RSS hash type is none, allowing the RSS configuration to be correctly applied when the hash type is none.
  ↳ No PR: [263ad48](https://github.com/DPDK/dpdk/commit/263ad48aa1e9d1596e6286de05efedc11aeeb955)
- Fixed the issue where the queue status was incorrectly overwritten when the port is restarted, ensuring that the stopped queue remains stopped after the driver is reset to avoid packet loss.
  ↳ No PR: [0c0bf6d](https://github.com/DPDK/dpdk/commit/0c0bf6d2bc927338dd3bea36216d6a016dfa5b68)
- Fixed a crash when memory allocation failed due to unchecked backing store allocation results.
  ↳ No PR: [bc950d4](https://github.com/DPDK/dpdk/commit/bc950d419b71f3144c0bd3208db53de21b350334)
- Removed debug logs that may flush the screen when creating a large number of streams.
  ↳ No PR: [f367d28](https://github.com/DPDK/dpdk/commit/f367d284d86db30de07f7f3b51904ad085a2f596)
- Fix invalid max VF check for fid on table range release in PF initialization when SR-IOV is disabled.
  ↳ No PR: [31f0d1c](https://github.com/DPDK/dpdk/commit/31f0d1cf98d6afda47bd689276207326c24b51c0)
- Fixed the Tx default rule conflict problem in multi-process scenarios, and changed the default rule from matching all globally to matching by sending queue (SQ) to avoid EEXIST errors caused by repeated creation.
  ↳ No PR: [2f1bb79](https://github.com/DPDK/dpdk/commit/2f1bb792ad51aeb2da00198a63422fc478131bd5)
- Fixed the problem of incorrect default action setting for port ID, obtain the action of the port default rule through the new kernel mbox interface, and use this action when creating flow rules.
  ↳ No PR: [d762a8f](https://github.com/DPDK/dpdk/commit/d762a8fbbd50fa24ef8f724c56679c4aae3b7d17)
- Save the MTU value when Rx queue is allocated, and use the saved value instead of the current device MTU when the shared queue is matched, fixing the problem of shared queue joining check failure due to subsequent MTU modifications.
  ↳ No PR: [4414eb8](https://github.com/DPDK/dpdk/commit/4414eb800708475bf1b38794434e590c7204d9d3)
- Fixed the problem in the mlx5 driver that NULL was not returned correctly when accessing external queues to avoid null pointer dereference due to invalid queue indexes.
  ↳ No PR: [d524b58](https://github.com/DPDK/dpdk/commit/d524b58819b46ea47d02338204d24c2f2ba29ee2)
- Fixed a bug in hash adjustment when creating indirect RSS actions in mlx5 PMD. This bug caused the adjustment of certain hash type combinations to be skipped, causing flow rule creation to fail in HW Steering mode.
  ↳ No PR: [6b01088](https://github.com/DPDK/dpdk/commit/6b010880a505c5609355180a7f99df940a163385)
- Fixed the issue in testpmd where PCI device devargs were discarded when ports were attached, and restored the processing of PCI port devargs provided by the application.
  ↳ No PR: [acbff64](https://github.com/DPDK/dpdk/commit/acbff64ea5b1f9551651aed647a8931e15fa102a)
- Fixed the issue of using memory after freeing when updating edges in the activity graph, using malloc+memcpy instead and adding a new function to replace all references to old node memory.
  ↳ No PR: [eaa1176](https://github.com/DPDK/dpdk/commit/eaa11767069f476e13000fc3fec618a40c46ab7e)
- Fixed net/nbl driver to replace random MAC address with hardware MAC address obtained from network device.
  ↳ No PR: [7004ff3](https://github.com/DPDK/dpdk/commit/7004ff37c9f5d6ea6eb7f9f3c0e7a472421ee4cb)
- Fixed the use-after-free issue when clearing the cache list in the net/netvsc driver, and used safe traversal macros instead.
  ↳ No PR: [abf0d7a](https://github.com/DPDK/dpdk/commit/abf0d7a889caf87a340e759ba9c571c6c5843f79)
- Fixed the problem of using objects after release during metering cleanup in the net/nfp driver. Use safe traversal macros instead to avoid accessing released memory.
  ↳ No PR: [080b02c](https://github.com/DPDK/dpdk/commit/080b02cd66cb2b0a08c4903b7f51a10f0ba8c37f)
- In the dumpcap application, when the main process exits, it directly exits without trying to clean up resources to fix the exit behavior.
  ↳ No PR: [cefd5ed](https://github.com/DPDK/dpdk/commit/cefd5edce236e69496693ea0ecbf3e61434ff348)
- Fix the race condition between the pdump callback function and other CPUs in the data path, and ensure callback safety by introducing reference counting and wait mechanisms.
  ↳ No PR: [34536d0](https://github.com/DPDK/dpdk/commit/34536d08b0c9c533a57181f7ff856488dbbfbb3f), [0dea03e](https://github.com/DPDK/dpdk/commit/0dea03ef2e8cd374f7941c87603c25943a16b4c5)
- Fixed an issue where the job may be released using an invalid queue index when allocating meter hardware resources fails.
  ↳ No PR: [112facb](https://github.com/DPDK/dpdk/commit/112facb17b0c0efd90e15501d0830a0f6af7b7c9)
- Fixed the index leak problem caused by not recycling ipool resources when destroying meter_mark indirect action.
  ↳ No PR: [e56ebf2](https://github.com/DPDK/dpdk/commit/e56ebf25074280479141eac8050e1f40a69bdbf9)
- Fixed the problem of missing error reporting when mlx5 PMD handles masked indirect actions in HWS mode. Instead, return specific errors through rte_flow_error, increase the log level, and add port and action handle information.
  ↳ No PR: [1d96131](https://github.com/DPDK/dpdk/commit/1d961316d9f541c6679dcd519a40a667f9885f30)
- Fixed the issue where the MAC address change of the bound device in 802.3ad mode is not synchronized to the hardware MAC of the physical member network card.
  ↳ No PR: [8a2f216](https://github.com/DPDK/dpdk/commit/8a2f21630658a7f3ff5c7564b9a2bcb0b681fb55)
- The ICE network card driver forces the use of the Tx packet scheduling function under the scalar path, and updates the offload flag of the vector path to include this function.
  ↳ No PR: [a7e0d05](https://github.com/DPDK/dpdk/commit/a7e0d05802ce21ad28d686efed404b64ef4ea9fd)
- Fixed the problem of PTP clock being destroyed when Tx packet rate control is enabled, moving the enabling and disabling of time synchronization to the port start and port stop functions respectively.
  ↳ No PR: [8d1dae9](https://github.com/DPDK/dpdk/commit/8d1dae92e9ca8d2a7e258cefbfb6eb3c55d435f0), [e65f6eb](https://github.com/DPDK/dpdk/commit/e65f6eb77239ad1a4079b6af10be54a779b939cf)
- Fixed the problem that the TX port in DCB forwarding configuration may be invalid, use fwd_topology_tx_port_get() instead to obtain the correct port, and support the --port-topology parameter.
  ↳ No PR: [47012b7](https://github.com/DPDK/dpdk/commit/47012b7cbf78531e99b6ab3faa3a69e941ddbaa0)
- Fixed the DCB receive queue configuration error in testpmd, and changed the value of nb_rx_queue from sending queue information to receiving queue information.
  ↳ No PR: [32387ca](https://github.com/DPDK/dpdk/commit/32387caaa00660ebe35be25f2371edb0069cc80a)
- Fixed repeated writing to the L2TAG1 field when VLAN offloading on the AVX-512 path, avoiding redundant storage by merging conditions.
  ↳ No PR: [431bc9c](https://github.com/DPDK/dpdk/commit/431bc9c42e73640fbadce18ef68c5f604164899d)
- Fix the conditions for VLAN insertion under AVX-512 paths to ensure that VLAN offloading is only performed when IAVF_TX_VLAN_QINQ_OFFLOAD is defined and is an offload path.
  ↳ No PR: [23ef9b4](https://github.com/DPDK/dpdk/commit/23ef9b485deccaf1c87591b42795e93b750ff2ea), [1aaa183](https://github.com/DPDK/dpdk/commit/1aaa183a9fa499bd28ee7738c0893b3033f620e0)
- Fixed the positioning error of single VLAN insertion and uninstallation in the iavf driver, ensuring that the outer VLAN tag is inserted when single VLAN is used, and the inner and outer layers are correctly distinguished during QinQ.
  ↳ No PR: [974c2b6](https://github.com/DPDK/dpdk/commit/974c2b6d7457243487f1f37d55b0278fa3b36451)
- Fixed the conflict between TxPP and IEEE 1588 forwarding, by introducing the txpp_ena flag to avoid multiple calls to the time synchronization function.
  ↳ No PR: [9315703](https://github.com/DPDK/dpdk/commit/9315703a619a3bf3d7f40730a8e90d9ef010601b)
- Fix HWS flow sampling action verification to ensure that the sampling action includes the termination action.
  ↳ No PR: [ae57af8](https://github.com/DPDK/dpdk/commit/ae57af82d5811b56cf734ac3893849fe467382b0)
- Fixed the link mode reporting logic in the cnxk network card driver to correctly report fixed or automatic negotiation based on the actual negotiation results of the hardware.
  ↳ No PR: [b8caeff](https://github.com/DPDK/dpdk/commit/b8caeff9ec407bc486cfc1fd9a7cd2f42116f602)
- Fixed a potential buffer overflow issue caused by buffer size mismatch when requesting PF link status in ixgbe VF driver.
  ↳ No PR: [82ff0aa](https://github.com/DPDK/dpdk/commit/82ff0aa59735fefa6e9e9daf77ea87da5b68fabd)
- Fixed the problem of mlx5 PMD causing the CPU to wake up incorrectly due to invalid CQE in power monitoring mode, and introduced a dedicated callback function to skip invalid CQE to improve energy efficiency.
  ↳ No PR: [750f635](https://github.com/DPDK/dpdk/commit/750f635fc6a7ee287e076c5500ca97d77187676a)
- Fixed the problem that the mlx5 driver did not release the representor interrupt handler when the device was closed, and added the stream pool destruction logic.
  ↳ No PR: [dbaed15](https://github.com/DPDK/dpdk/commit/dbaed15366cb9aa66d7e0a580462a042ecfb602f)
- Fix the problem of newly allocated but unused mempool entries not being released when registering a shared memory pool, and avoid deadlock caused by releasing MR while holding a lock.
  ↳ No PR: [aef9434](https://github.com/DPDK/dpdk/commit/aef94343d3d0b7e11071747f0d2fd66546d7b724)
- Fixed the concurrency problem caused by static variables in buddy memory allocation, and adjusted the release logic to avoid double release.
  ↳ No PR: [8d1fe10](https://github.com/DPDK/dpdk/commit/8d1fe10768d2749d00ceb7124866c61d31164380)
- Fixed an error in setting the hash_state_sz field of the request descriptor during AES-CCM operation in the QAT driver, changing it from the digest length to the AAD length.
  ↳ No PR: [3ffcfc4](https://github.com/DPDK/dpdk/commit/3ffcfc48040a076643ec58c5f53b77069305afda), [2c5b18a](https://github.com/DPDK/dpdk/commit/2c5b18a3ba6676d3d7e6fd2985d12b023350be19)
- Fixed QinQ Tx offload not working correctly in vector offload paths, moved it to non-vector paths, and removed the check for QinQ flags.
  ↳ No PR: [61ccab8](https://github.com/DPDK/dpdk/commit/61ccab85e3972d6e3ee61b3e6a6a6872a33e5ac3)
- Fixed a race condition when pdump is disabled: complete the removal of local callbacks before forwarding requests to the secondary process.
  ↳ No PR: [928f43e](https://github.com/DPDK/dpdk/commit/928f43e3f9c12bd1e8eacbbc3c63f07896b64d92)
- Fixed a crash caused by the null pointer of the tx_pkt_prepare function in multiple Intel network card drivers (ice, ixgbe, fm10k). Assign the value to the dummy function in the vector or simple TX path to avoid null pointer calls.
  ↳ No PR: [743bbd3](https://github.com/DPDK/dpdk/commit/743bbd3bd22561ace152403fb505b48e4620ac53), [19d7188](https://github.com/DPDK/dpdk/commit/19d7188f6fc3c147ac9c8a870ca16a22f61d4096), [bd96307](https://github.com/DPDK/dpdk/commit/bd96307d152da4baa1b14a6fcfa7700703179cfc)
- Fix the release sequence of send to kernel action resources in the MLX5 driver, ensuring that related actions and flow tables are released before destroying the domain.
  ↳ No PR: [472b099](https://github.com/DPDK/dpdk/commit/472b0994319198090e44a7c2de1e43f0a0e0a270)
- Drain and close the associated completion queue before stopping the send queue.
  ↳ No PR: [b5b5d16](https://github.com/DPDK/dpdk/commit/b5b5d166d6eed7bd6af1a2065d0e378a7769689f)
- Fixed the null pointer problem when roc_nix is null in inline device write operation.
  ↳ No PR: [5a75391](https://github.com/DPDK/dpdk/commit/5a753913e06ab335d147ddb631d7bd3e15534d62)
- Update the processing logic of the DF flag during IPv4 fragmentation so that it inherits the DF flag of the original packet header instead of forcibly clearing it.
  ↳ No PR: [6565191](https://github.com/DPDK/dpdk/commit/6565191cfc370a54e824b6d1018b2c222ce67e1e)
- Fixed the issue where aura limit is reset to the actual number of buffers instead of the fixed maximum value when cleaning up the SQB pool, to avoid residual threshold buffers causing errors in subsequent pool creation.
  ↳ No PR: [f3c15bb](https://github.com/DPDK/dpdk/commit/f3c15bb6062475a62451c62ca2c5c9a5e12706c8)
- Fixed the null pointer dereference problem in the roc_nix_sq_ena_dis function, added checking for null pointer parameters and returned an error code.
  ↳ No PR: [9d845a3](https://github.com/DPDK/dpdk/commit/9d845a3d13bf70cf356c511f0d1bccfb69dc4f81)
- Fix empty SQ access problem, add non-null check before accessing SQ, and simplify pktio lock handling when threshold configuration.
  ↳ No PR: [52ff61c](https://github.com/DPDK/dpdk/commit/52ff61c2ca114691d74546f5ce16e8a7ebd164ae)
- Fixed error handling in inline inbound queue settings using wrong pointer variable.
  ↳ No PR: [5a06d69](https://github.com/DPDK/dpdk/commit/5a06d69a91f0cb06f98265b488ce482042ab7593)
- Fix the CPT result address configuration logic to avoid generating garbage values when there is no inline device, and ensure that configuration is only triggered when there is an inline device.
  ↳ No PR: [b581982](https://github.com/DPDK/dpdk/commit/b581982e3970c1c7c8a4f91a8c5bb040c9a733f6)
- Fix null value check for roc_nix pointer when NIX Rx inject is enabled to avoid null pointer dereference.
  ↳ No PR: [9396a93](https://github.com/DPDK/dpdk/commit/9396a93a0d848edf0f32a4950418a8083e04924c)
- Fixed illegal access error caused by null pointer in Rx inject configuration.
  ↳ No PR: [7d2c9da](https://github.com/DPDK/dpdk/commit/7d2c9dae103299edffbb436793ef499a6fdd9beb)
- Fixed the handling of invalid default colors when default meter pre-coloring, and added index validation to avoid out of bounds.
  ↳ No PR: [b595d05](https://github.com/DPDK/dpdk/commit/b595d05bf739b5330cbfca00bdb984edea579a57)
- Fix the checking logic for PF Rx timestamp support in the iavf driver to ensure that the capability is only reported when PF actually supports Rx timestamps.
  ↳ No PR: [d21c2fe](https://github.com/DPDK/dpdk/commit/d21c2fe6e5a1ef1e7cc9490f54f359db1cfd5283)
- Fixed an issue where the iavf driver did not check the validity bit when receiving timestamps, to avoid reporting incorrect timestamp values when the hardware did not capture the timestamp.
  ↳ No PR: [dba51a2](https://github.com/DPDK/dpdk/commit/dba51a2fbdde67a2237a8d2c9fb73baf29e04dd0)
- Fixed the missing TCP TSO offload flag in the queue configuration conversion function in the idpf driver, ensuring that the scalar sending path that supports this function is correctly selected when requesting TSO offload.
  ↳ No PR: [f36df6a](https://github.com/DPDK/dpdk/commit/f36df6a25569102afa911b74d8613a5e7267f038)
- Fixed the problem of inaccurate data due to low-bit carry when reading network card statistics.
  ↳ No PR: [9ac3d9c](https://github.com/DPDK/dpdk/commit/9ac3d9cc61bc70fdc6dff14969a7111a673be932)
- Fix error handling when mlx5 device starts, replace single error cleanup label with cascade label, ensure that only steps that have been successfully initialized are cleaned up, and avoid state corruption leading to subsequent startup failure or abnormal behavior.
  ↳ No PR: [860f6c6](https://github.com/DPDK/dpdk/commit/860f6c63dbc1cc6ae6bbaca886c04b88d43a2236)
- Fixed the problem that the mlx5_link_update function in the mlx5 driver did not initialize variables. Initialize dev_link to zero in the function and set link_autoneg to the original value of the link.
  ↳ No PR: [7429374](https://github.com/DPDK/dpdk/commit/7429374afba9827a43cf2efabce14e27ccc4bdef), [a333afa](https://github.com/DPDK/dpdk/commit/a333afabed3b659ea28a92470565bbd5a98b5b53)
- Fixed a crash caused by repeated calls to close in the dpaa2 network card driver during device removal.
  ↳ No PR: [3b82253](https://github.com/DPDK/dpdk/commit/3b8225353ea3b9eb03df5dee94a037582d0d6748)
- Fixed the issue where the global active VDQ status was not cleared when releasing the Rx queue in the dpaa2 driver, causing Rx to hang after detach/attach.
  ↳ No PR: [360a8d6](https://github.com/DPDK/dpdk/commit/360a8d674c36e628523bdd83bedd27ce34b3091b)
- Fix the problem that the Rx error queue in the dpaa2 driver is not released, ensure that the pointer is empty after releasing the queue, and release the mbuf in the error queue back to the original memory pool.
  ↳ No PR: [46d02ee](https://github.com/DPDK/dpdk/commit/46d02eeaaeb8bf93b69a72bd917b119f320c0cf1), [4f0abf4](https://github.com/DPDK/dpdk/commit/4f0abf4b7e3e6e213f419c2facc2fbfbf8afb351)
- Fixed the incorrect capability check in the hash calculation of flow rules in the mlx5 driver and changed it to the correct distribution mode judgment.
  ↳ No PR: [970309c](https://github.com/DPDK/dpdk/commit/970309c7aa889ee06178c6476fe153e17096fc25)
- Fixed the null pointer dereference problem when acts->mhdr may be NULL during modify header processing in the mlx5 driver, and added a defensive NULL check in mlx5_tbl_ensure_shared_modify_header.
  ↳ No PR: [df19cf4](https://github.com/DPDK/dpdk/commit/df19cf4aa720935a31edcb2954a88cfd038880e6)
- Fixed a crash caused by null pointers when destroying hardware flow rules in the mlx5 driver, added defensive null pointer checks and renamed fields to improve code readability.
  ↳ No PR: [ad7db90](https://github.com/DPDK/dpdk/commit/ad7db900a05397773b812e76655918086b07ab36)
- Fixed the problem of inner UDP checksum unloading failure in testpmd, unified inner and outer processing logic, and solved the problem of inner L4 protocol not being recognized under multiple encapsulation formats.
  ↳ No PR: [bbee934](https://github.com/DPDK/dpdk/commit/bbee934955cc7d5b6f8a17b2da26cd19858424a5)
- Fix the crash caused by hns3, ngbe and other drivers when tx_pkt_prepare is set to NULL after removing the ethdev fast path callback check, replace it with the dummy function, and remove unnecessary NULL assignments in the softnic driver.
  ↳ No PR: [9cd1dcc](https://github.com/DPDK/dpdk/commit/9cd1dcc49eb3ff17025881ec3bcb51011e9c3901)
- Roll back the flow engine configuration update, and fix the regression problem of untrusted VF/SF caused by the HWS engine causing the number of memzone segments to exceed the limit.
  ↳ No PR: [cc12189](https://github.com/DPDK/dpdk/commit/cc121898f110871e9bddeb036e3d850694c3819d)
- Fixed a compilation error caused by the missing const qualifier of the pointer type in the fslmc bus device name resolution function.
  ↳ No PR: [f4ef899](https://github.com/DPDK/dpdk/commit/f4ef899bb3aeca2fa195f9605ddaf7567f8b0afb)
- Fixed the concurrency problem of Rx/Tx statistics in the net/nbl driver, introduced a reference value mechanism, so that the actual counter is only updated by the Rx/Tx burst thread, and the reference value is updated synchronously when resetting statistics.
  ↳ No PR: [fb50c47](https://github.com/DPDK/dpdk/commit/fb50c473996ef274aae12722a388a397350f4589)
- Repair the mailbox interface call in the txgbe driver, introduce function pointers for different devices to unify the mailbox command calling method, and adjust the synchronization mask of EEPROM operations.
  ↳ No PR: [82d9cc9](https://github.com/DPDK/dpdk/commit/82d9cc90be63ebaed13a5175c45d5501684a9fc8)
- Rolled back the check for PF Rx timestamp support, and fixed the problem that PF that supports Rx timestamp could not enable this function normally.
  ↳ No PR: [07f93e7](https://github.com/DPDK/dpdk/commit/07f93e7f4936158da712d3540512bf0034207bda)
- Fixed build failure when GCC and RTE_MBUF_HISTORY_DEBUG are enabled, removed extra newlines in log messages.
  ↳ No PR: [39b54f2](https://github.com/DPDK/dpdk/commit/39b54f2dcf44ad1f91eabc7080cd5dea763607fd)
- Extend the MAC address tag bitmap so that it records the addresses of PF, VF and SF, and move the bitmap operations to upper-level OS functions.
  ↳ No PR: [9dd445b](https://github.com/DPDK/dpdk/commit/9dd445bddd89ee2ababf3a7c0659b8d1224ec74a)
- Removed duplicate Tx queue assignment in txgbe driver.
  ↳ No PR: [1623a62](https://github.com/DPDK/dpdk/commit/1623a62ba811dbfd3e261ccdbac6d6c95a3ecfcb)
- Improve the error report when mlx5 flow table resize is completed, distinguishing two failure reasons: resize is not started and some rules are not updated.
  ↳ No PR: [d5a8211](https://github.com/DPDK/dpdk/commit/d5a82110efc70dbcff27a5f347ba0d82bab7e36e)
- Fixed the mask value of flow random item in testpmd from 16 bits to the correct 32 bit full mask.
  ↳ No PR: [e3054b2](https://github.com/DPDK/dpdk/commit/e3054b2f402f52c744344a4ec2a17ff1eb47f8e0)
- Fixed incorrect validation logic after flow_hw_create_flow call in non-template RSS extension, check function return value instead.
  ↳ No PR: [ee60f50](https://github.com/DPDK/dpdk/commit/ee60f50fbbf57e8173282c5cdd7d66cd9090103e)
- Fixed the problem of asymmetric operation failure in the crypto-perf application, corrected the RSA operation type checking logic and removed unnecessary signature data copying.
  ↳ No PR: [ac96bc3](https://github.com/DPDK/dpdk/commit/ac96bc367b6e66a3ac94ba08f84282c92034ae17)
- Fixed the problem that the ice_flow_set_hw_prof function in the ice driver did not release the temporarily allocated memory.
  ↳ No PR: [bce22ae](https://github.com/DPDK/dpdk/commit/bce22ae3a0e61134b5fd19498bd849d1693dadb4)
- Fixed a memory leak in the ice driver caused by not cleaning up old linked list entries when applying or removing GENEVE/VXLAN advanced filters.
  ↳ No PR: [baf3de2](https://github.com/DPDK/dpdk/commit/baf3de23be970346378d5159a81782bfb6eb927b)
- Fixed redundant return statements in the cn20k_ipsec_session_update function to resolve compilation errors in debug mode.
  ↳ No PR: [00da176](https://github.com/DPDK/dpdk/commit/00da1763c63d8aa8cce8e1285cd48dda6165783c)
- Fixed the failure of mbuf sanity check in TLS post-processing, and introduced the pktmbuf_trim_chain function to uniformly trim the mbuf chain.
  ↳ No PR: [08b83e8](https://github.com/DPDK/dpdk/commit/08b83e84e137c5fd1736bfab624e4a7f588ff420)
- Fixed the problem of telemetry command registration failure in the l3fwd-power example, replacing hyphens in the command name with underscores.
  ↳ No PR: [44a4784](https://github.com/DPDK/dpdk/commit/44a4784a9710892a9bdaadbe08732000b90c95f3)
- Fixed the race condition in the stream aging process, merged the counter key fields into atomic access and added atomic read and write functions.
  ↳ No PR: [820ca73](https://github.com/DPDK/dpdk/commit/820ca7361bb7fa40e96e53515d8392ea40a35265)
- Fixed the issue of initialization crash of e1000 network card driver under GCC 13 optimization, and added compiler barrier after register reading.
  ↳ No PR: [4d0b1e2](https://github.com/DPDK/dpdk/commit/4d0b1e252a58f9cee89aa08d6e9742fa4a797e91)
- Fixed an issue in AMD power monitoring where timeout was not enabled, lcore can now automatically wake up after a specified time.
  ↳ No PR: [1213a88](https://github.com/DPDK/dpdk/commit/1213a8895be3bf883f10b3ba60ee84099b5ff75a)
- Roll back changes that caused incorrect counting of non-native MAC packets when promiscuous mode is turned off, restoring correct Rx statistics.
  ↳ No PR: [88132df](https://github.com/DPDK/dpdk/commit/88132dfbe789a8705626efdb8f603206d716cf93)
- Fixed an issue where timeouts or invalid values were not handled correctly when obtaining the physical DMA address width, the return value will now be verified and initialization will be aborted in case of an error.
  ↳ No PR: [d61d90e](https://github.com/DPDK/dpdk/commit/d61d90e52a248d15adf90a1be9e5a2c6b19ec55a)
- Fixed the symmetric Toeplitz hash hash calculation problem for SCTP in the i40e driver, and removed the SCTP Verification Tag to ensure that packets of the same session are assigned to the same queue.
  ↳ No PR: [09937a3](https://github.com/DPDK/dpdk/commit/09937a3646f83ffe9d0d27896066c3f3f6e4ee0c)
- Fixed L3/L4 checksum result reading error, corrected the check status field from word8 to word1.
  ↳ No PR: [8703542](https://github.com/DPDK/dpdk/commit/870354264644bc8a2f014571e9a34757258d2ec8)
- Allow receiving packets with hardware parser length errors, preventing these packets from being dropped.
  ↳ No PR: [e285f6e](https://github.com/DPDK/dpdk/commit/e285f6ead6f20e3d05bf1c8fd4ed119d6fda0335)
- Fix the flow rule size adjustment logic in the dpaa2 network card driver, ensure that the rule size is calculated correctly when appending a new extract, and add error handling.
  ↳ No PR: [3904f56](https://github.com/DPDK/dpdk/commit/3904f568b8e9987c82a4123776a62e4ca9857f1d)
- Added MAC reconfiguration function to reset the MAC when the port is down/up to clear error codes and avoid receiving the first packet loss.
  ↳ No PR: [6ef2180](https://github.com/DPDK/dpdk/commit/6ef2180a7e050104d0acbbf3c69845c221e77a47)
- Fix dictionary parameter handling, avoid assigning signed values to unsigned parameters, and make dictionary optional.
  ↳ No PR: [a2a93c2](https://github.com/DPDK/dpdk/commit/a2a93c20de4d90fb7d7d684f5bad280cc6ee379d)
- Fixed the relative offset matching problem of L3 packets in FDIR rules. Now only L4 packets are supported to use relative offsets.
  ↳ No PR: [f1cd458](https://github.com/DPDK/dpdk/commit/f1cd458035da9066379c457d27488eeb7741af46)
- Fallback to fast mbuf release Tx offload function in net/null driver.
  ↳ No PR: [6c94fef](https://github.com/DPDK/dpdk/commit/6c94fefffbfa1ef9f2a79b212f31e18552b061a3)
- Fixed the problem that QinQ insertion did not take effect when sending a single packet in the iavf driver.
  ↳ No PR: [873a531](https://github.com/DPDK/dpdk/commit/873a5315d0077dc67b35e3e42043f99d41b6b6c6)
- Fixed the issue where the L2TAG2 field is repeatedly written when mbuf sets VLAN and QinQ to insert the offload flag at the same time, causing the tag to be damaged.
  ↳ No PR: [744ff57](https://github.com/DPDK/dpdk/commit/744ff575c7cc17d65a83c537ac71e33c09609008)
- Fixed the format specifier of the bandwidth profile ID and changed its output to hexadecimal format.
  ↳ No PR: [8da4eaf](https://github.com/DPDK/dpdk/commit/8da4eaf43701b8b249435bd452867f1f2c97ca2e)
- Fix GCC 16 compilation warning using unused local variables for missing register write operations.
  ↳ No PR: [dec4636](https://github.com/DPDK/dpdk/commit/dec46366290076afa65bc6b505b274e10e90f494)
- Fixed the problem of memcpy using fixed length in flex link item parsing, instead calculating the correct size based on the actual flow item type, and adding verification for unsupported types.
  ↳ No PR: [39454e2](https://github.com/DPDK/dpdk/commit/39454e245b125ae555bc5a3a058cc3c1e1280f82)
- Fixed flow rule array length allocation error to ensure that the correct number of rules is reserved for each core.
  ↳ No PR: [a0b1480](https://github.com/DPDK/dpdk/commit/a0b148048b3d9960788093b3b94c70af8f04136b)
- Fixed the problem of passing a null pointer when rte_eal_init is called in the test function test_eal_init_once, and instead passes a valid parameter array.
  ↳ No PR: [978ead0](https://github.com/DPDK/dpdk/commit/978ead0144c1a6ed8fcb7cc6246a01db55dd88d4)
- Fixed the test problem when the mempool/stack driver is disabled in the minimal build, separate the stack driver related code and use conditional compilation to protect it.
  ↳ No PR: [26b9200](https://github.com/DPDK/dpdk/commit/26b9200d0f62ddec0069ae83734439dacd910373)
- Fix the problem of AEAD decrypting test vectors, extend out-of-place restrictions to delayed tests, and force the test vector file path to be provided.
  ↳ No PR: [c4aa053](https://github.com/DPDK/dpdk/commit/c4aa053022ba6f91671a1dd0038d63e1fc4772a4)
- Fixed the runtest function in the DMA test to treat non-zero test return values as errors to correctly handle test cases that may return positive numbers.
  ↳ No PR: [fabb8c0](https://github.com/DPDK/dpdk/commit/fabb8c0b7e5bef6dfd54a8faabdee59e05d4be7e)
- The ring size in the DMA test automatically adapts to the minimum and maximum values supported by the device.
  ↳ No PR: [c4b0762](https://github.com/DPDK/dpdk/commit/c4b0762fce81ba6edfec0d935cf23342f78018e3)
- Fix non-standard array initialization of test vector files to support MSVC compilation.
  ↳ No PR: [24288ec](https://github.com/DPDK/dpdk/commit/24288ec2eccadb5916f335d4f485d00d6b63bff7)
- Fixed the problem that the rte_crypto_sym_vec structure in the CPU encryption test path is not initialized.
  ↳ No PR: [78ed944](https://github.com/DPDK/dpdk/commit/78ed9449a63ecc00b059ddc24dd04df8a119f5de)
- Fix the parameters of the EAL initialization call in the unit test, replacing invalid NULL argv[0] with a valid string.
  ↳ No PR: [b74d638](https://github.com/DPDK/dpdk/commit/b74d638ab9a769ed9628d2759029d2d20a081637)
- Fix clang 21 build error, initializing uninitialized variables in test function.
  ↳ No PR: [bec307d](https://github.com/DPDK/dpdk/commit/bec307d512373403a28d447d0d54b191471bc624)
- Add --iova-mode=va parameter for debug testing when using --no-huge under PPC64 architecture.
  ↳ No PR: [c94a9de](https://github.com/DPDK/dpdk/commit/c94a9de51c2100659b25105ef433b88f3e6dc5af)
- Fixed compilation warning in sfc_efx driver (unused variables and type comparison).
  ↳ No PR: [10c044c](https://github.com/DPDK/dpdk/commit/10c044ccf7238ebb1f8b4ab906b348bb07bf3d94), [56b82b9](https://github.com/DPDK/dpdk/commit/56b82b965fe8961caf85e67023a9f18a6fbf0134)
- Fix dpaa2 driver error frame dump, support mbuf format dump load and parsing results.
  ↳ No PR: [f9465bd](https://github.com/DPDK/dpdk/commit/f9465bdcef9db163190f05c9ba80b8b9a205c81b)
- Added a warning that no service core is available when initializing the ntnic driver.
  ↳ No PR: [65dc644](https://github.com/DPDK/dpdk/commit/65dc6444b37fe216db95ad709558f7286606a62d)
- Remove the streaming action mark that is not supported in the txgbe driver.
  ↳ No PR: [7224536](https://github.com/DPDK/dpdk/commit/7224536b051457ce2a9cfd6e433da9d4a7bc97ac)
- Fixed warnings reported by multiple static analysis tools in the r8169 driver.
  ↳ No PR: [822bd84](https://github.com/DPDK/dpdk/commit/822bd84cea15af47b63d1461ee0ed97ade318608)
- Enhanced bnxt driver backing store debugging function, added CLI command to traverse all ports and table ranges.
  ↳ No PR: [2a04a71](https://github.com/DPDK/dpdk/commit/2a04a71841d943b37f276ee5092d360ac7b9d09a)
- Migrate DPAA bus subsystem logs from pr_xxx macros to DPAA_BUS_XXX macros.
  ↳ No PR: [14ac380](https://github.com/DPDK/dpdk/commit/14ac380ae5c8942dcb1c008d87bb665a14abc953)
- Removed TruFlow debugging/non-production printing and cleaned up related debugging code.
  ↳ No PR: [660bde6](https://github.com/DPDK/dpdk/commit/660bde60e43c309ba4b58371e2ac3690593bda0b)
- Removed unused constant MLX5_VDPA_DEFAULT_TIMER_DELAY_US in vdpa/mlx5 driver.
  ↳ No PR: [3d8472f](https://github.com/DPDK/dpdk/commit/3d8472f3c84cee0b5ac302b7d79e3407a30112c6)
- Removed two unused constants in crypto/mlx5 driver.
  ↳ No PR: [37fee55](https://github.com/DPDK/dpdk/commit/37fee5571702ebcf0e5ee9e38e01cb5eceaabe1e)
- Removed multiple unused constant definitions in regex/mlx5 driver.
  ↳ No PR: [9f6da93](https://github.com/DPDK/dpdk/commit/9f6da93ec89a60df71f8e4d4748dff108a395595)
- Removed multiple unused macro definition constants in the mlx5 common driver.
  ↳ No PR: [5f961fe](https://github.com/DPDK/dpdk/commit/5f961fec22ff6903f2a11ffdc5ffef9c8c50cb5b)
- Removed three no longer used macro definitions in the mlx5 driver.
  ↳ No PR: [f2638f1](https://github.com/DPDK/dpdk/commit/f2638f1f388c9300850d217f9a820c1c40f78a77)
- Fixed GCC 16 compilation warning caused by unused parameters in fm10k driver.
  ↳ No PR: [967d5fb](https://github.com/DPDK/dpdk/commit/967d5fbb7b23700ccffccb9979d4f6acdac412c8)
- Fixed clang 21 compilation error caused by log format specifier mismatch in eventdev library.
  ↳ No PR: [9726ac9](https://github.com/DPDK/dpdk/commit/9726ac9d903ce8bc76e4c8abde1de64b2827b609)
- Fixed compilation warnings caused by missing const qualifiers in multiple drivers.
  ↳ No PR: [c70b359](https://github.com/DPDK/dpdk/commit/c70b359f3734dfc6bb35ec6a6c73f2540d1e66c0), [c3a9408](https://github.com/DPDK/dpdk/commit/c3a94087ef4986d9c6b590c9fbfb2e0f7c18fbd5), [5071329](https://github.com/DPDK/dpdk/commit/507132927cfd2e51ca509419285434b08ca2ea7c), [405bbb5](https://github.com/DPDK/dpdk/commit/405bbb5cdc60ea9110b3dbd9a20e55262a0d85a2), [367d26d](https://github.com/DPDK/dpdk/commit/367d26dd8ace9e5f74d7434a82332e9813efd4bc)
- Fixed compilation warning due to pointer type mismatch in collectd format.
  ↳ No PR: [11a64ff](https://github.com/DPDK/dpdk/commit/11a64ff198cf3d380c00f08d3895cd06dcd90d44)
- Print an invalid MAC address to aid debugging when the firmware provides it.
  ↳ No PR: [6a52407](https://github.com/DPDK/dpdk/commit/6a52407cfff51ccece8810fd965625e78a4f5125)

### Refactoring optimization
- Uniformly use the DPAA2_VADDR_TO_IOVA macro for address translation in the DPAA2 memory pool driver, and reconstruct the mbuf release and allocation process to support both VA and PA modes.
  ↳ No PR: [f007da2](https://github.com/DPDK/dpdk/commit/f007da2ec4ffe6b34ee7cf4502fe7e8267a7a417)
- Extracted the general function eal_cpuset_to_str for converting cpuset to string, and reconstructed the original available_cores implementation based on this function.
  ↳ No PR: [982e5ab](https://github.com/DPDK/dpdk/commit/982e5ab1c98e9838c5c976add94b007c76c7f3bb)
- Removed the redundant offload check in the Rx queue vector path and simplified the related function interface.
  ↳ No PR: [82a5e5c](https://github.com/DPDK/dpdk/commit/82a5e5cfefd5a262b45c05987061828dab02e34e)
- Split the general CQ null check function into Rx-specific functions, and add a new auxiliary function to obtain the Tx CQ descriptor.
  ↳ No PR: [e5b0f7c](https://github.com/DPDK/dpdk/commit/e5b0f7cd989fc793f3d29bc1de79cf67f2e4d590)
- Unified the functions and variables of multiple submodules in the Napatech hardware module with the nthw_ prefix, involving FLM, statistics, logs, DBS, hash/flow, register ops, table ID and global variables, etc.
  ↳ No PR: [a451123](https://github.com/DPDK/dpdk/commit/a4511238bb8762d8f358debc036366f0035f15d0), [675e746](https://github.com/DPDK/dpdk/commit/675e74653895f8bb9bc2f222ce0075728035b4b0), [d3d06ae](https://github.com/DPDK/dpdk/commit/d3d06ae396fcafc7dcf3526a519dc48e58f31ba2), [033e722](https://github.com/DPDK/dpdk/commit/033e722c3e471acb4e07c2819aaab5bdfabcd205), [3d68ce7](https://github.com/DPDK/dpdk/commit/3d68ce7020d676aca8f56a1e6d8a04dd937785a7), [6977ddf](https://github.com/DPDK/dpdk/commit/6977ddfe101b38f11f890339ee25cc7fce06a80f), [cf8a697](https://github.com/DPDK/dpdk/commit/cf8a697edc8fb7d991d065d1dbb498f4b629a1d2), [081aaef](https://github.com/DPDK/dpdk/commit/081aaefe57ae337993441cc815f2787cc7a50dcb), [63aef35](https://github.com/DPDK/dpdk/commit/63aef3569d45321ef89e58436adaadf38765bc2e), [f42868c](https://github.com/DPDK/dpdk/commit/f42868c962c8db96b32181875efb9e95ea498eb4), [398675d](https://github.com/DPDK/dpdk/commit/398675d675e4cdf958d06811303c0f013c6de73e), [a80c3d9](https://github.com/DPDK/dpdk/commit/a80c3d98e2c24c6e7efd21f4b623c7d387d49a7e), [1794973](https://github.com/DPDK/dpdk/commit/17949734e9000d2929012615e58684e213c0ca81), [ce6fcd2](https://github.com/DPDK/dpdk/commit/ce6fcd2a227c539fa37dae4b1c23eb20d3684a4a)
- Removed cache line alignment of counter-related structures in the mlx5 driver to reduce memory usage.
  ↳ No PR: [3eec7a7](https://github.com/DPDK/dpdk/commit/3eec7a797f41f1586c7b1de91935ea4a933a6c18)
- Reconstructed the mlx5 driver root flow table group check logic, added a dedicated function to determine whether the group index is a root group, and replaced the direct check in action template translation.
  ↳ No PR: [65ccacc](https://github.com/DPDK/dpdk/commit/65ccacc0d62de6f3e3efbc9b5ba1e314b4d7b5bd)
- Renamed variables in the Rx path selection function in the Intel network card driver to improve readability, and added a support check for single-queue Rx.
  ↳ No PR: [31f1e4e](https://github.com/DPDK/dpdk/commit/31f1e4ea4d60061da3c7a0c18bdea152b6e78f46)
- Unified Rx path selection logic, introduced common infrastructure and applied to i40e, ice, iavf and cpfl drivers.
  ↳ No PR: [3f59c3d](https://github.com/DPDK/dpdk/commit/3f59c3d97a892ed40ebad69d1163cc10f5375046), [258f346](https://github.com/DPDK/dpdk/commit/258f346f5d5e0426c82bb6e1913f1294c2d3b4cc), [872b571](https://github.com/DPDK/dpdk/commit/872b57178709e7a0877945d519e8cc6384e5bfec), [91e3205](https://github.com/DPDK/dpdk/commit/91e3205d72d8a0381cee9135c71ba9bb396711e7), [3f24891](https://github.com/DPDK/dpdk/commit/3f24891594c199439c74dd17c691635c2992009d), [a8225f2](https://github.com/DPDK/dpdk/commit/a8225f2b308dcea8a713d4fb30887701a12f7c87)
- Removed redundant queue structure members in iavf driver.
  ↳ No PR: [6a36701](https://github.com/DPDK/dpdk/commit/6a367015a476316e82043235de14ad11bb5e1e7b), [b990b58](https://github.com/DPDK/dpdk/commit/b990b587cd1f1d7c274a601013be5f87eff38c47)
- Enhanced sanity check of IO queue in ENA driver.
  ↳ No PR: [bfe9685](https://github.com/DPDK/dpdk/commit/bfe9685c25e1f69a195852bd8bf808ef1fdae9dc), [b417bd3](https://github.com/DPDK/dpdk/commit/b417bd3d2b1e39ca13d7df221c849dfaa9113059)
- Improved the error handling logic in ena_close, added error code logs and optimized the coding style.
  ↳ No PR: [0d57c52](https://github.com/DPDK/dpdk/commit/0d57c52937c0854f1c7698b8eb6a2b1d0410126f)
- Split a single PHC error statistics into three detailed statistics, and added an error log.
  ↳ No PR: [a14be4d](https://github.com/DPDK/dpdk/commit/a14be4dd8693789cd6e8a875c47a498efed39325)
- Removed redundant queue mode check in ena_com_init_io_sq function.
  ↳ No PR: [f9a0e33](https://github.com/DPDK/dpdk/commit/f9a0e33b960615e8be99893037a413ebda75ac6d)
- Refactored the DMA performance test application, removed redundant fields and split the configuration loading function to improve code readability.
  ↳ No PR: [86f7299](https://github.com/DPDK/dpdk/commit/86f729996ed5e3a0087e9bb51f2fa66d800605a2), [d2545e6](https://github.com/DPDK/dpdk/commit/d2545e6c46905deea4748d8f3f8c411122067c65)
- Cleaned up VFIO internal macro definitions, used RTE_DIM() instead and removed redundant boundary checks.
  ↳ No PR: [48c503f](https://github.com/DPDK/dpdk/commit/48c503fb7f93b78043929b904bb78521ba64a509)
- Unified the enabling logic of promiscuous mode and full multicast mode, making it consistent with the processing method of disabling functions.
  ↳ No PR: [3b101b9](https://github.com/DPDK/dpdk/commit/3b101b9f4bd4f8d981360c56c6a45f75bcdf56b2)
- Renamed Rx/Tx function type variable from burst_type to func_type.
  ↳ No PR: [224357a](https://github.com/DPDK/dpdk/commit/224357ae24a6e7691374768a6b03daa39a53fab1)
- Reconstruct the command line option conflict checking logic, focus it on the parameter sorting stage and remove redundant global variables.
  ↳ No PR: [471ae35](https://github.com/DPDK/dpdk/commit/471ae35d2d775e10a6621d66a884dcf10bbef795)
- Use the new cpuset to string helper function to replace the original thread affinity to string function.
  ↳ No PR: [5144ddd](https://github.com/DPDK/dpdk/commit/5144dddd294fd49d1117ca2073b55c6b5ace3cee)
- Refactor benchmark.c to extract data validation and resource management sub-functions.
  ↳ No PR: [36ac5a2](https://github.com/DPDK/dpdk/commit/36ac5a2932e795efef161fbc97f9906443d5a4aa), [71870b4](https://github.com/DPDK/dpdk/commit/71870b40924fcdcf1d1027729e1bdefc9a8a2975)
- Simplify the checking logic of the configuration method in the r8169 network card driver, replacing switch-case with conditional judgment.
  ↳ No PR: [4e6ed72](https://github.com/DPDK/dpdk/commit/4e6ed7284f50f18a025c6c5b70002148a412971a)
- Update the logical ID allocation of the bnxt driver TCAM manager, remove the pre-allocation of index 0 on initialization, and rename variables.
  ↳ No PR: [beda74b](https://github.com/DPDK/dpdk/commit/beda74b65c4b1943de2b6d98929ecdda02445a2a)
- Removed unused functions and pointers from dpaa2 driver.
  ↳ No PR: [603caa2](https://github.com/DPDK/dpdk/commit/603caa201d7fea95d9272aec5667cb4a23d0886d)
- Fix the size check logic of table scope query and memory allocation in bnxt driver, and use idempotence judgment function instead.
  ↳ No PR: [3fcdeaf](https://github.com/DPDK/dpdk/commit/3fcdeaf75f22c41ed1f6d894147d6bbb2755ca50)
- Removed conditional compilation code for older versions of DPDK in the bnxt driver.
  ↳ No PR: [0a34107](https://github.com/DPDK/dpdk/commit/0a3410709d0d35c4914e468f2606c69b615d48e7)
- Removed unused VFIO header file inclusions from multiple driver files.
  ↳ No PR: [afc2c84](https://github.com/DPDK/dpdk/commit/afc2c84e4498e8ddbed4662c2255b31e65f430a2)
- Remove unnecessary null pointer checks and simplify memory release logic.
  ↳ No PR: [985a967](https://github.com/DPDK/dpdk/commit/985a967b0bdf3eba52d02ea807d5c6bc15db374f)
- Changed the global symbol prefix of ark PMD from eth_ark_ to ark_.
  ↳ No PR: [2392785](https://github.com/DPDK/dpdk/commit/23927855a4ffc89cafe20a3653d396e021956899)
- Refactor the format of Rx path information array in i40e driver.
  ↳ No PR: [a9d0bab](https://github.com/DPDK/dpdk/commit/a9d0baba7caf3bb09d253e08ee0b809aace46680)
- Refactor the initialization format of the Rx path information array in the ice driver and remove unused macros.
  ↳ No PR: [759622e](https://github.com/DPDK/dpdk/commit/759622e02f4d25a32fae77aded953a71e61b7ef4)
- Declare global variables in enic and dpaa2 drivers as static.
  ↳ No PR: [1755f9d](https://github.com/DPDK/dpdk/commit/1755f9d457f49b5f265766738a575afc5980a971), [3daa94b](https://github.com/DPDK/dpdk/commit/3daa94bcd1b55b35523d2bf970b73f677c6dbe82)
- Remove unused functions in ntnic PMD, and unify the naming of log auxiliary functions.
  ↳ No PR: [e3eac26](https://github.com/DPDK/dpdk/commit/e3eac26b230f5118c30261e9e50ad397f9540a38)
- Inline the auxiliary data structure of flow rules into the same memory pool allocation to reduce memory allocation overhead.
  ↳ No PR: [aff44ad](https://github.com/DPDK/dpdk/commit/aff44ada9abc5831601e7dad5d48d9c6b5493f2d)

### Test related
- Added buffer size check in DMA performance test, and gives a friendly error prompt when the buffer size exceeds the upper limit of uint16 type.
  ↳ No PR: [12b050d](https://github.com/DPDK/dpdk/commit/12b050defa729b0edf416e25ddf16203bcb176e2)
- Added test support for enqueue/dequeue operations for DMA devices.
  ↳ No PR: [af5af1b](https://github.com/DPDK/dpdk/commit/af5af1bd744fe07275110bc4d1486455ad643719)
- Added documentation for Rx/Tx offload test suite, including description of mbuf fast free test case.
  ↳ No PR: [9d7d2ab](https://github.com/DPDK/dpdk/commit/9d7d2abc2e997786485533f5648df6703ec98f48)
- Added documentation for the virtio forwarding test suite to DTS, covering virtio-user/vhost-user server/client forwarding scenarios and testpmd message verification.
  ↳ No PR: [4623d9f](https://github.com/DPDK/dpdk/commit/4623d9ffae1c0b59e8745cbfdfcf6610b98ac37b)
- Removed unnecessary comma operators in test code to eliminate clang's -Wcomma compilation warning.
  ↳ No PR: [b3c63c2](https://github.com/DPDK/dpdk/commit/b3c63c2a8889caa03682220ae1bac44a3ad3f967)

### Performance optimization
- Optimize the acquire and release operations of the DPAA memory pool, adopt the new BMan API and support burst release, improving release performance by about 90%.
  ↳ No PR: [637bde7](https://github.com/DPDK/dpdk/commit/637bde750065b978b120a1d4aba4d1c563db9c42)
- Fixed performance regression caused by non-cache aligned source buffers in QAT crypto PMD, adding alignment processing in the data path.
  ↳ No PR: [2531743](https://github.com/DPDK/dpdk/commit/253174309ff7abf9eaba58d1bccf90cca7e6d215)
- Rename and optimize the mbuf seed function for the Ark NIC Rx queue, adopt a 4K aligned buffer allocation strategy to reduce PCIe requests, and try to allocate smaller blocks when memory is exhausted.
  ↳ No PR: [af94cac](https://github.com/DPDK/dpdk/commit/af94cac0164f0fa6b1236f5b8685a7a037032c6e)
- Optimize the setting method of the ENA network card Tx descriptor field, replacing the operation of erasing first and then setting by direct assignment to improve performance.
  ↳ No PR: [fa2f757](https://github.com/DPDK/dpdk/commit/fa2f7570fb149578ce0331c9a7ddaf6b5a416f8b)
- Remove the redundant clearing operation of the Tx descriptor in the ENA network card LLQ scenario and use the existing bounce buffer clearing mechanism.
  ↳ No PR: [cb856ed](https://github.com/DPDK/dpdk/commit/cb856ed2493864b0862606c8ad04487869dc5e09)
- Optimize the ENETC4 data path, separate cache coherence operations into independent RX/TX functions, reduce memory access, and add checksum offloading and fragmented packet type parsing support.
  ↳ No PR: [72f491f](https://github.com/DPDK/dpdk/commit/72f491f1e53cdf86a6cf2bb36bec0119f87a844b)
- Fixed performance issues with the Thor2 TruFlow memory manager: moved full blocks to the end of the list, making sure searches stop correctly when encountering the first full block.
  ↳ No PR: [d4b1493](https://github.com/DPDK/dpdk/commit/d4b14939a7add8508e8a2b02d8ed09b34566a9eb)
- For the E830 network card, when the number of queues is less than 64, the global RSS LUT is used to improve performance.
  ↳ No PR: [193a11f](https://github.com/DPDK/dpdk/commit/193a11ffd3e69369f0589f501875f7b0acdc55e1)
- When filtering data packets, change the mbuf release per packet to batch release to improve performance.
  ↳ No PR: [ecd42d8](https://github.com/DPDK/dpdk/commit/ecd42d8e5f9cdda9c43d2205a08f01c19f90a071)
- Skip creation and cleanup of Rx control flow tables in flow isolation mode to save resource allocation and speed up device startup.
  ↳ No PR: [3276821](https://github.com/DPDK/dpdk/commit/327682174e1a282c1351c83aacd2b9e8f8d352f2)
- Change the dynamic allocation profile in the ice driver FDIR filter to an embedded structure, eliminating indirect references and fixing potential memory leaks.
  ↳ No PR: [f1dd6c3](https://github.com/DPDK/dpdk/commit/f1dd6c3fdf974810e9a0d57920a4aa66fa16342e)
- Fixed the memory leak problem in the ice network card driver and virtio encryption device driver to improve performance stability.
  ↳ No PR: [3938eee](https://github.com/DPDK/dpdk/commit/3938eeec989181216ea3f9cc8eee931a2915ca5d), [8b0d855](https://github.com/DPDK/dpdk/commit/8b0d855fd98c6c88665489fdba12f8e603deae21)
- Fixed the problem that the ena driver may copy from an invalid memory area, and the kg_cfg structure in the dpaa2 driver is not initialized.
  ↳ No PR: [b70db09](https://github.com/DPDK/dpdk/commit/b70db0912a6a181ecf513a4eef61153d1063c0ae), [058043d](https://github.com/DPDK/dpdk/commit/058043d0590f52dd45555a362d31646c7c3ff943)
- Optimize the error handling of the statistics counter manager in the bnxt driver, perform cleanup when initialization fails and fix the thread cancellation condition judgment.
  ↳ No PR: [60aad99](https://github.com/DPDK/dpdk/commit/60aad9985ce0a63371cb8303cd9f8ad215d4a28c)
- Enhance the measurement functions of DMA performance test application and encryption performance test application, add enqueue/dequeue performance measurement, and increase the number of decimal places in test results.
  ↳ No PR: [e1bfc8d](https://github.com/DPDK/dpdk/commit/e1bfc8d5b89b0daade724b732eb0d42e19946365), [322f0b7](https://github.com/DPDK/dpdk/commit/322f0b7ac8fc262dfaf55fe2d7b3ccd37912e5dc)
- Fixed the issue in the encryption performance test where the test vector plaintext exceeded the buffer causing digest verification to fail, added length check and improved log output.
  ↳ No PR: [b298803](https://github.com/DPDK/dpdk/commit/b2988038656b03d1c019114fbe7609018cc16e87)
- Improved stability and robustness of hash read and write function tests, reduced test entries to avoid timeouts on restricted platforms, and added memory allocation failure checks.
  ↳ No PR: [8c4861d](https://github.com/DPDK/dpdk/commit/8c4861d00aabcf54ef9d6f1df2a4cfb37c06f6c2), [77e23b2](https://github.com/DPDK/dpdk/commit/77e23b2d7ee45d153f588611a3fa479e4cf0c9b6)
- Updated documentation related to performance testing, adding instructions for the TRex traffic generator and documentation for the single-core performance test suite.
  ↳ No PR: [581f250](https://github.com/DPDK/dpdk/commit/581f250f908441156fc135f8cf4bffb865192e19), [d77d7f0](https://github.com/DPDK/dpdk/commit/d77d7f04f24c24a1199af2a7a5a8585fd8bb5bdb)
- Added command line options to the l3fwd and l3fwd-power examples to force a specified port link speed and reject unsupported duplex modes.
  ↳ No PR: [2001c8e](https://github.com/DPDK/dpdk/commit/2001c8eaf4efb94173410644cf29cbaa62a0ac83), [a61cd1c](https://github.com/DPDK/dpdk/commit/a61cd1c50adc43254d2027f1c828a4c188216e33)
- Added --rx-burst and --tx-burst command line options to the l3fwd example, allowing to configure the number of received and sent burst packets respectively.
  ↳ No PR: [79375d1](https://github.com/DPDK/dpdk/commit/79375d1015b308234e8b6955671a296394249f9b)
- Optimize the output of mempool cache dump, hide zero value entries and update prompt information to reduce output noise.
  ↳ No PR: [8010858](https://github.com/DPDK/dpdk/commit/8010858724e2aca25f4b3a6bf383e3eacb2f4b10)
- Fix clang 21 compilation warning, initializing event variables in DMA adapter settings.
  ↳ No PR: [1bdf2b3](https://github.com/DPDK/dpdk/commit/1bdf2b3c27880f1d90df46a89d5643f20587a973)
- In bnxt driver, skip IOVA range check when mbuf uses external memory to avoid unnecessary verification.
  ↳ No PR: [d01de33](https://github.com/DPDK/dpdk/commit/d01de33f98e20acba9d6a2ba7897268d81ef824e)
- Removed several macro definitions that are no longer used, and cleaned up the code to reduce compilation overhead.
  ↳ No PR: [9d37885](https://github.com/DPDK/dpdk/commit/9d3788534cba7cc3424e2a83db6b186211d4e94f)
- Obtain port speed capabilities from firmware, replacing the original hard-coded method.
  ↳ No PR: [8cdd699](https://github.com/DPDK/dpdk/commit/8cdd699d669c1803553852afdc427ea30178acdd)
- Optimize the QP and CQ memory allocation of the XSC network driver and use local NUMA nodes instead to improve performance.
  ↳ No PR: [4349749](https://github.com/DPDK/dpdk/commit/4349749ddf74d8a08a8810a9f9d74b8c7a7db55c)
- Increase the number of inflight buffers of the crypto adapter and fix the problem of performance dropping to zero in high traffic scenarios.
  ↳ No PR: [3e19094](https://github.com/DPDK/dpdk/commit/3e19094cb697998972e7f89bdd3ab08ea457ae1f)
- Add unlikely compiler hint for conditional judgment in ena_com_sq_have_enough_space function to optimize branch prediction performance.
  ↳ No PR: [032b6f7](https://github.com/DPDK/dpdk/commit/032b6f71ebe767d0d6a511659ea15c19f8729d28)
- Added a new prefetch function in the receiving and sending completion processing to uniformly prefetch the next parsing result to improve performance.
  ↳ No PR: [8768966](https://github.com/DPDK/dpdk/commit/876896628dc391f1d7f5a6581bc8bc45d993fb68)

### Security related
- Fixed array out-of-bounds caused by short file names in EAL plug-in directory traversal, and used a safer suffix matching function instead.
  ↳ No PR: [c32e203](https://github.com/DPDK/dpdk/commit/c32e203ee23473ccf3c8526d12e1c59f17c50eab)
- Fixed memory out of bounds when creating index-based streaming rules in mlx5 driver, by skipping items array preparation and correcting ipool allocation/release fields.
  ↳ No PR: [4a35eb5](https://github.com/DPDK/dpdk/commit/4a35eb531b7542c4f86b98bb04b46f17081b537d)
- Fixed out-of-bounds access in enetfec UIO mapping and added mapping size validity check.
  ↳ No PR: [22b0837](https://github.com/DPDK/dpdk/commit/22b0837bd93a777b8ca7fcf234985175e456a4f5)
- Fixed a double read vulnerability in vhost dequeue offloading to prevent data races by copying virtio headers to temporary variables.
  ↳ No PR: [285e6b8](https://github.com/DPDK/dpdk/commit/285e6b8b187485cc69a175261e40d8d2727e20a3)
- Fixed potential format overflow in ntnic driver by replacing sprintf with snprintf and adjusting buffer size.
  ↳ No PR: [f5f6e54](https://github.com/DPDK/dpdk/commit/f5f6e545d91875845287f3c2a0b34b22d309028d)
- Add bounds checking for flex filter mask for e1000 driver, fix array out-of-bounds warning reported by GCC-16 and prevent potential out-of-bounds.
  ↳ No PR: [ce19d0a](https://github.com/DPDK/dpdk/commit/ce19d0ad17886f9f3af5bc16b39e15b00e9a94a2)
- Fixed warnings caused by flexible array member copying during LTO compilation, inline the copy logic and use structure assignment instead.
  ↳ No PR: [3fc246e](https://github.com/DPDK/dpdk/commit/3fc246e883c412f3c285bcabdb402b7d66e78526)
- Fixed a crash caused by the tap network card not deregistering the interrupt callback after a failed startup.
  ↳ No PR: [c44ed08](https://github.com/DPDK/dpdk/commit/c44ed082917316257dbeb2454414932d39f9c321)
- Add verification of RSA module length configuration in encryption performance tests, and limit ECDSA operations to only support signing and verification.
  ↳ No PR: [070a340](https://github.com/DPDK/dpdk/commit/070a3406b6392043752d97f8ea5d09f351960e3d)
- Fixed the mbuf chain processing error in the test case to ensure that the header mbuf fields are updated correctly after releasing the intermediate nodes.
  ↳ No PR: [1ff54c0](https://github.com/DPDK/dpdk/commit/1ff54c055d95736aae05a40b361427215c318cc1)
- Fixed format-overflow warning due to insufficient buffer size in example server_node_efd, adjusted address display and queue name buffer size.
  ↳ No PR: [c97d223](https://github.com/DPDK/dpdk/commit/c97d223fc64fc10cf8f6c6f0e7d506926e83462b)
- Fixed format overflow during iface parameter processing in the vdpa example to avoid snprintf output being truncated.
  ↳ No PR: [6605265](https://github.com/DPDK/dpdk/commit/66052657fcb810c47cbbe52762c9ad0ad7828821)
- Add parameter range check for mbuf pool name formatting in IP fragmentation reassembly example to prevent buffer overflow.
  ↳ No PR: [eb2c85d](https://github.com/DPDK/dpdk/commit/eb2c85dc7b146505a1ec877103b82fa37d197fc3)
- Fixed compilation warnings caused by missing const qualifiers in the QAT driver, and changed multiple function return types and local variables from char * to const char *.
  ↳ No PR: [6fc6bfb](https://github.com/DPDK/dpdk/commit/6fc6bfb0913cdcb436346ca9c66352902cf36129)

### Documentation
- Added Python script for parsing mbuf history dumps, presenting them in human-readable format, and updated comments on related header files.
  ↳ No PR: [fd6bb58](https://github.com/DPDK/dpdk/commit/fd6bb586ca832c0cd6a84bcf7123a6063b3ae133)
- Improved comments in the mbuf core header file to more accurately describe the rearm_data field, second cache line and synchronization requirements when adding new Rx/Tx offload flags.
  ↳ No PR: [6d53169](https://github.com/DPDK/dpdk/commit/6d5316974440c62c8c8f602dc00dd2ad9cdaeab3)
- Added list of platforms tested with NVIDIA network cards in the 25.11 release notes.
  ↳ No PR: [0f51c2a](https://github.com/DPDK/dpdk/commit/0f51c2ad9f73e5084d3f850d64358667964c32b0)
- Updated the requirements description of the stream counting action in the mlx5 document, and added the minimum DOCA version requirements.
  ↳ No PR: [cd6519d](https://github.com/DPDK/dpdk/commit/cd6519d3d6100c32c9b83456dcb300c6526eb434)
- Added tested Intel platform and Intel network card combinations to v25.11 release notes.
  ↳ No PR: [1142310](https://github.com/DPDK/dpdk/commit/114231086215177eb532fecacb8e71ac294b2ae3)
- Migrate the documentation of testpmd, packet processing, and artifact modules to the new API directory, and add API documentation references for the artifact module.
  ↳ No PR: [eba657a](https://github.com/DPDK/dpdk/commit/eba657ae3c3c4e2f210229f6e7f2e6af4215ceee), [95960cf](https://github.com/DPDK/dpdk/commit/95960cf86b423a9fef2567214e1e24687e4f0678), [a1c7f24](https://github.com/DPDK/dpdk/commit/a1c7f2493fadc1dbc8bdd83a8a1f0c6b250da27e), [c950cb6](https://github.com/DPDK/dpdk/commit/c950cb68917d160c83f20ab7c6b55d2fcf879742)
- Reconstructed the README file of DTS, retaining only high-level concept descriptions and quick start guides.
  ↳ No PR: [dc0c607](https://github.com/DPDK/dpdk/commit/dc0c6073e91a0b16ba997cd57141fee44aa0e8a5)
- Updated the coding guidelines in the DTS guide, added new test case decorators and setup/teardown hooks instructions, and corrected the run command.
  ↳ No PR: [b9dcff5](https://github.com/DPDK/dpdk/commit/b9dcff5aa27dcc2eb81977e8d759f7b283f64d77)
- Removed optional dependency on DTS documentation to simplify maintenance process.
  ↳ No PR: [2c41c93](https://github.com/DPDK/dpdk/commit/2c41c9336a8cdeface84e3f04ef043deab30f731)
- Updated the limitation description in the mlx5 network card driver documentation to indicate that IPv6 5-tuple matching is supported on newer hardware.
  ↳ No PR: [5cb1f22](https://github.com/DPDK/dpdk/commit/5cb1f22f380dd5e969723b4d1e6a6862f8cc0e55)
- The support for code block level and transport block level processing of each device is clarified in the baseband device guide.
  ↳ No PR: [1aee594](https://github.com/DPDK/dpdk/commit/1aee59444269c66cdc5dcf64b93584a1f7da57bf)
- Clarified the usage range and mapping of the window index for each circular shift in the FFT processing pipeline in the baseband processing guide.
  ↳ No PR: [113b065](https://github.com/DPDK/dpdk/commit/113b065d6c2a1e0c32d9749296dc83f9c7d517fe)
- Added a new test case docstring example to the "How to write a test suite" section of the DTS guide.
  ↳ No PR: [91a226f](https://github.com/DPDK/dpdk/commit/91a226f80c8bc2253bd01dacfc3890a48cb0b898)
- Updated AMD EPYC platform documentation, corrected typos, added Zen5 EPYC 9005 tuning guide, added uncore power management details, and updated Solarflare network card usage instructions.
  ↳ No PR: [020d6f8](https://github.com/DPDK/dpdk/commit/020d6f851bb1405a04b4758491b5d05bf27c4dea)
- Added description of compile options RTE_LIBRTE_MBUF_DEBUG and RTE_ENABLE_ASSERT in mbuf library guide.
  ↳ No PR: [ceb2f5f](https://github.com/DPDK/dpdk/commit/ceb2f5f84e48139948a825b85741c1735429f8a4)
- Updated telemetry library documentation to clarify that command names can only contain alphanumerics, underscores, and forward slashes.
  ↳ No PR: [994644d](https://github.com/DPDK/dpdk/commit/994644dcbdca1490bd831e4fd1d7d5b0b79d1874)
- Added description of supported value types in the documentation of the argparse library, including automatic parsing of multiple integer types.
  ↳ No PR: [164b88a](https://github.com/DPDK/dpdk/commit/164b88a6a2b10c08ecccd223acb7c0536c4dc466)
- Fixed backtick mismatch in Doxygen comments to be compatible with Doxygen 1.15's strict checking.
  ↳ No PR: [2f8d3fd](https://github.com/DPDK/dpdk/commit/2f8d3fda56754b13a09098fac1140d781366672f)
- Updated Python version references in the FreeBSD build guide, changing py38-pyelftools to py311-pyelftools.
  ↳ No PR: [75204e8](https://github.com/DPDK/dpdk/commit/75204e8dcf420118d17b92f955c4eb4678d27df9)
- Updated external links and comments in the Windows Build Guide and clarified how to open the Visual Studio Developer Command Prompt.
  ↳ No PR: [7b2b79d](https://github.com/DPDK/dpdk/commit/7b2b79dae2742bc28752f0b87543ccb6d30cacf8)
- Updated the documentation on API module usage in the DTS Guide to correctly reflect the current status and usage of the DTS API.
  ↳ No PR: [8e1bdc6](https://github.com/DPDK/dpdk/commit/8e1bdc67ee427dad220a23d47f62dea4fe31d3cf)

### Build/CI
- Added Undefined Behavior Sanitizer test task in CI, and adjusted related build configuration and test skip logic.
  ↳ No PR: [918b667](https://github.com/DPDK/dpdk/commit/918b6674b841cd80ed063ae2541878b77f03ee82)
- Made the Linux uAPI header file checking options mutually exclusive with the import and upgrade options. An error will be reported when used at the same time, and the version acquisition logic has been adjusted.
  ↳ No PR: [b656146](https://github.com/DPDK/dpdk/commit/b6561460b9381d227ddf3ee7ee6938196d8e493b)
- Add silent mode (-q option) to Linux uAPI scripts so that they only output error messages when running normally.
  ↳ No PR: [c164c58](https://github.com/DPDK/dpdk/commit/c164c58b8da2cb7f20bdefcaca61ad961f76e977)
- Fix MSVC build issue: add explicit type conversion for assertions in mlx5_rx_burst and mlx5_rx_burst_out_of_order functions for MSVC compatibility.
  ↳ No PR: [0ee5b2f](https://github.com/DPDK/dpdk/commit/0ee5b2f89300e8917a50fe0b943296917b383faf)
- Fix the order of conditional judgment in the checkpatches.sh script to ensure that the -n and -r flags take precedence over stdin checks to avoid incorrectly reading patches from standard input in non-terminal environments.
  ↳ No PR: [0a630d2](https://github.com/DPDK/dpdk/commit/0a630d23dfea0f437278ff8221427ba901933baf)
- Enable comma operator related warnings in global compilation options and disable them for the driver.
  ↳ No PR: [3ee3c1a](https://github.com/DPDK/dpdk/commit/3ee3c1a6e5e33f4ff04cfa19fbcec6c39c6b9058)
- Add Meson install tag to the document build target to support separate building and installation of documents.
  ↳ No PR: [83e611c](https://github.com/DPDK/dpdk/commit/83e611c5fa86c9a48b290301c33ff651a528fa27)
- In CI workflows, save the ccache cache when a build or test fails to speed up subsequent retries.
  ↳ No PR: [a628f34](https://github.com/DPDK/dpdk/commit/a628f349303f9da34a9e7fd49acd60e6a5391640)
- Remove unnecessary termios.h header file to enable cmdline tests to be built on Windows.
  ↳ No PR: [6d3da11](https://github.com/DPDK/dpdk/commit/6d3da1115e14765645c902116e77dd4db9288279)
- Enable lock annotation checking in hns3 driver.
  ↳ No PR: [2de3085](https://github.com/DPDK/dpdk/commit/2de30859f2f38db8dffe82d64cf0cc0c0ad24974)
- Refactored the Linux uAPI header file update script, encapsulated the update and check logic into functions, and cleaned up redundant explicit error returns.
  ↳ No PR: [7b2a183](https://github.com/DPDK/dpdk/commit/7b2a183cc160e67f63d1ff700aa9cb9856f58eb3), [6e29e2a](https://github.com/DPDK/dpdk/commit/6e29e2a991e1e507289e73a699e27229ca6537a0)
- Introduced the staging directory mechanism for the header file checking tool, copied the library and driver header files to different directories, and added corresponding checking targets.
  ↳ No PR: [9f4fd81](https://github.com/DPDK/dpdk/commit/9f4fd81debf1999409573dfce96655c177bdc74e)
- Added a new script for manipulating mailmap files.
  ↳ No PR: [1d86bff](https://github.com/DPDK/dpdk/commit/1d86bff77664dcdc166068c0e15cb8b41e104c5a)
- Optimized the test build script to only enable debug information when ABI checks are required and use shared links for 32-bit builds to reduce disk footprint.
  ↳ No PR: [1da8dc8](https://github.com/DPDK/dpdk/commit/1da8dc8b1cfad035198ead44458d2c485ad0fef5)
- Refactored the GitHub Actions workflow to extract build dependencies into multi-line variables and use them uniformly in the Fedora pipeline.
  ↳ No PR: [3311adc](https://github.com/DPDK/dpdk/commit/3311adc46daa55864309cbb6d637124fccf19155)
- Added dependency libraries required by AMD uncore power driver for Fedora build environment in GitHub Actions workflow.
  ↳ No PR: [1dfed76](https://github.com/DPDK/dpdk/commit/1dfed76a168ed684f7b4a66c5eedb14e5a0de639)
- Ignored warning about missing Link/Closes for Reported-by tags in checkpatches.sh script.
  ↳ No PR: [0db25f4](https://github.com/DPDK/dpdk/commit/0db25f4eb2812a10d70c242f25761a5a36e97ff7)
- Enabled format truncation warning in the example build, removing the compile option that previously disabled the warning.
  ↳ No PR: [03a8f97](https://github.com/DPDK/dpdk/commit/03a8f971d5666ed407f8f2046c708bfc3fa044b9)
- Fixed MinGW 13 compilation error, added empty status string check and fixed loop variable type in rte_bbdev_queue_ops_dump function.
  ↳ No PR: [7cacb5b](https://github.com/DPDK/dpdk/commit/7cacb5b3f6cc89785f9383ac9544e61dc971897d)
- Increased fast test timeout for RISC-V architecture from 10 seconds to 60 seconds.
  ↳ No PR: [9e36adf](https://github.com/DPDK/dpdk/commit/9e36adf88c49b437c4c5ffa46158e53d96bef82c)
- Fixed the test build configuration to skip the test instead of failing directly when the corresponding driver is missing.
  ↳ No PR: [c93de0a](https://github.com/DPDK/dpdk/commit/c93de0a363c813f31871b8119d0c12271a29a212), [b603ebc](https://github.com/DPDK/dpdk/commit/b603ebc80474c1fc6f8f68b60d23b29116524ba9)

### Maintenance
- Fixed extra blank lines at the end of multiple driver source files, ensuring the files end with a single newline character.
  ↳ No PR: [cc47017](https://github.com/DPDK/dpdk/commit/cc470177d1030114aef91227d72915f82389fc97)
- Upgraded CI test image from Fedora 39 to Fedora 43.
  ↳ No PR: [91bac75](https://github.com/DPDK/dpdk/commit/91bac7546b34fbcbc96ec7b3afa4bb2daa8accb9)
- Removed unused control queue index macro definition.
  ↳ No PR: [89c5eeb](https://github.com/DPDK/dpdk/commit/89c5eeb22624f8bba21c9c2f10f08a95f6394123)
- Replace zero-length arrays in the hash library and driver header files with C99-compliant flex array members.
  ↳ No PR: [9a24b32](https://github.com/DPDK/dpdk/commit/9a24b32d2231279cb9ef678ba33f8bc764ae41a6), [19eb997](https://github.com/DPDK/dpdk/commit/19eb9974143ff0412b2253d2de20368c20a6669b)
- Improved the processing logic of fragmented packages to handle cases where the complete package is not yet available.
  ↳ No PR: [2f98d2f](https://github.com/DPDK/dpdk/commit/2f98d2f86125928cf933582176d6335c57648a89)
- Removed the flag that automatically generates meaningless queue expansion statistics in the ice and ipn3ke drivers, and cleaned up the related code.
  ↳ No PR: [adfb79e](https://github.com/DPDK/dpdk/commit/adfb79e4447c6209fc6e77144aa70357beb2d584), [3d1537e](https://github.com/DPDK/dpdk/commit/3d1537e9de8887063f1775210a720e03a345126a)
- Reformatted the iavf driver Rx path information array to improve readability, and removed unused macros.
  ↳ No PR: [5e8a5d4](https://github.com/DPDK/dpdk/commit/5e8a5d4e0d82e9a86d5f3497d51913d3f4f6fa34)
- Improved the ena driver management command failure log, adding the command ID in the error message.
  ↳ No PR: [4a2e8b5](https://github.com/DPDK/dpdk/commit/4a2e8b59c6202870041ecb519814f0bc9768d772)
- Upgrade the ENA network card driver version from 2.13.0 to 2.14.0.
  ↳ No PR: [255cb9a](https://github.com/DPDK/dpdk/commit/255cb9a98a23a65d23881187a72547d072068345)
- Fixed the unnecessary comma operator in the example code and eliminated the -Wcomma warning of the clang compiler.
  ↳ No PR: [90f49b1](https://github.com/DPDK/dpdk/commit/90f49b1d35b73145619345eea3902dc39497a69b)
- Skip statistics collection to avoid invalid operations when Rx queue is not started and statistics context ID is not assigned.
  ↳ No PR: [3c9e181](https://github.com/DPDK/dpdk/commit/3c9e18185a0f89b1f38d8a2ea647ac0379eb46ae)
- For the cn20k chip, the aura field width is adjusted from 20 bits to 17 bits, and the related shift calculations are updated.
  ↳ No PR: [a8b2e7b](https://github.com/DPDK/dpdk/commit/a8b2e7b664b73f8302c94a3665c624d8b879e1a6)
- Deleted the unused ecore_mng_tlv.c file in the qede driver base directory.
  ↳ No PR: [a273a0e](https://github.com/DPDK/dpdk/commit/a273a0e6dc8c343f12d386bb123201d6e39a39f0)

### Others
- Replaced unnecessary comma operators in multiple drivers and libraries, eliminating compilation warnings.
  ↳ No PR: [90ae5d5](https://github.com/DPDK/dpdk/commit/90ae5d599e53dfb51e2dd2549bc76b1f9cde049e), [e8bf5f9](https://github.com/DPDK/dpdk/commit/e8bf5f948553c8574798c7576fa18df2c685ac50), [fc94d78](https://github.com/DPDK/dpdk/commit/fc94d784d784307d7f4326640b47861336efbe16), [ee42e00](https://github.com/DPDK/dpdk/commit/ee42e00f6b99515f2bea1e02d59e777bc33f5b08), [e966377](https://github.com/DPDK/dpdk/commit/e966377a266d13b12d37765f0e72d895d348ecc0)
- Cleaned up the Linux uAPI script, removing unnecessary curly braces and unused local variables.
  ↳ No PR: [05eadcc](https://github.com/DPDK/dpdk/commit/05eadcc34a174ff1a0877c4f08bcb59f5de77d5f), [724a1f2](https://github.com/DPDK/dpdk/commit/724a1f2321f59e4286b1a40a1242eec0fccdc30d)
- Updated the copyright year and version date in the ICE basic driver README.
  ↳ No PR: [0956bd9](https://github.com/DPDK/dpdk/commit/0956bd9317c4ee848d5ab27319f46596cc05377e), [9f809d1](https://github.com/DPDK/dpdk/commit/9f809d1a8c3359b5d972cf596c3934292eff6b93)
- Reworded term definitions in the DTS Guide and updated the copyright year.
  ↳ No PR: [348a308](https://github.com/DPDK/dpdk/commit/348a308345649c136fb001ed9613500d5c06ddee)
- Added description of IP fragmentation matching restrictions in the mlx5 driver documentation.
  ↳ No PR: [b8ac526](https://github.com/DPDK/dpdk/commit/b8ac526197d40ba3bb0ec534ba347c5bbed4a446)
- Merged the documentation for remote sessions and SSH sessions, and removed the separate SSH session documentation page.
  ↳ No PR: [aedafea](https://github.com/DPDK/dpdk/commit/aedafea4fb19b1a3b58193487a0b72a51a541846)
- Fixed NVIDIA forked driver presentation link.
  ↳ No PR: [f219e55](https://github.com/DPDK/dpdk/commit/f219e55e51d6bb9f8fcfc5899cfe5752e0bfca93)
- Fixed the problem of incorrect command display in the cpfl guide, and adjusted the colon and indentation.
  ↳ No PR: [484451b](https://github.com/DPDK/dpdk/commit/484451b27293f2745baf6793e5c4a3c3224f50f5)
- Fixed the description of the VLAN filter function parameter rx_queue_id in ethdev and corrected it to the correct VLAN stripping description.
  ↳ No PR: [f7eaa90](https://github.com/DPDK/dpdk/commit/f7eaa9063561a130badc978f2dfe49536904c907)
- Reordered the enumeration values of the Rx function type in the IAVF driver so that they are arranged from small to large in SIMD width.
  ↳ No PR: [59a9844](https://github.com/DPDK/dpdk/commit/59a9844f9601284ccdc744f58216bddc3bb0a390)
- Adjusted the log format of the ENA base library to align it with the driver log format.
  ↳ No PR: [5a1f626](https://github.com/DPDK/dpdk/commit/5a1f6261bc498f51f38114a63d955e87ab869726)
- Adjusted the order of variable declarations of multiple functions in ena_com.c to follow the Reverse Christmas Tree specification and removed unnecessary spaces.
  ↳ No PR: [b848d86](https://github.com/DPDK/dpdk/commit/b848d869cd9126be585a83476716df6e8325803b)
- Removed unused frame attribute array in dpaa2_sparser.c.
  ↳ No PR: [1422903](https://github.com/DPDK/dpdk/commit/14229039a2760ee6f43b89c29516469f223541e7)
- Fixed the spelling error of enumeration constant in idpf driver, renamed IDPF_RX_SINGLQ_AVX512 to IDPF_RX_SINGLEQ_AVX512.
  ↳ No PR: [309bbd3](https://github.com/DPDK/dpdk/commit/309bbd342201f5650f4a071e070bdc4c340cacb7)
- Reconstructed the ntnic guide document and improved the format and layout.
  ↳ No PR: [f3f02d1](https://github.com/DPDK/dpdk/commit/f3f02d163895fe99d6bbf43b8d0080b50fe2d123)
- Fixed an issue in the FreeBSD build guide where pyelftools package comments were not displayed correctly due to missing colons.
  ↳ No PR: [da1cd5c](https://github.com/DPDK/dpdk/commit/da1cd5cf6a8578aa879a9d5517132d13973cc38a)
- Moved SPDX license identification in multiple source files from second line to first line to comply with contributor guidelines.
  ↳ No PR: [2d21277](https://github.com/DPDK/dpdk/commit/2d21277d9ae36d527f065f6b4d3c84beee709f46)
- Fixed the Doxygen comment syntax error, correcting the incorrect /*< to a normal comment.
  ↳ No PR: [c7fc741](https://github.com/DPDK/dpdk/commit/c7fc741dbb456e558b7d38b4c587493220041162)
- Updated DPDK 25.11 release notes to correct grammar, spelling and formatting issues.
  ↳ No PR: [174db9f](https://github.com/DPDK/dpdk/commit/174db9f7d4305830bca321f21ba56664c0da5db5)
