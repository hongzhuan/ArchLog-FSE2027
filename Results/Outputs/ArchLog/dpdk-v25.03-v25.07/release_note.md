# Release Note

## Important Changes

### Vendor-Specific PMD Plugins
- Added zsda encryption device driver framework, supporting device configuration, start, stop, shutdown, information acquisition, queue pair management and statistical functions. (Architecture-related: new driver framework)
  ↳ No PR: [1ae3a7d](https://github.com/DPDK/dpdk/commit/1ae3a7d97b674e1db6c875d39ee2b39e1c1b6031)
- Added comprehensive security feature support for CN20K encryption devices, including secure session management, IPsec and TLS data path operations, TLS infrastructure and raw API support. (Architecture event: platform_bus_driver module change)
  ↳ No PR: [8fc370e](https://github.com/DPDK/dpdk/commit/8fc370ee0208dbc0683fc2b7d0f2f4829f205b6e), [b12ed0d](https://github.com/DPDK/dpdk/commit/b12ed0d3115aab90d4d37d68938adeecd5e9b5c7), [55b86a5](https://github.com/DPDK/dpdk/commit/55b86a5c3dad58fa782fc7efa1b7dad108f3c36d), [45efc4d](https://github.com/DPDK/dpdk/commit/45efc4d236a49eae096feb916e6f30d29a19fe54), [852521e](https://github.com/DPDK/dpdk/commit/852521e73ec527d50eb2f6263c5f445559d864a8), [952de44](https://github.com/DPDK/dpdk/commit/952de442e98b506bfd5f9287caa507c48d22a85b), [0c875bf](https://github.com/DPDK/dpdk/commit/0c875bf4a40572094dab0e8add0d22138b554ef5), [54f1da3](https://github.com/DPDK/dpdk/commit/54f1da35f03b598ae0840cfa4ce1ed6e9f2e3db2), [064c767](https://github.com/DPDK/dpdk/commit/064c7673c54ea9e479c465fd520e846dfff8a834), [c05eb27](https://github.com/DPDK/dpdk/commit/c05eb27d55d86acd7f20930a0d7aab5669cfc85b), [6b7da48](https://github.com/DPDK/dpdk/commit/6b7da487eecf931d57bbea2f76e054c6274958ce), [0668088](https://github.com/DPDK/dpdk/commit/0668088984f577651892a93200f50d4ecc58af22), [9146f4e](https://github.com/DPDK/dpdk/commit/9146f4e8d793f01b2939654266cc7c85b33418c1), [f0f9cbc](https://github.com/DPDK/dpdk/commit/f0f9cbcfdf8c56db64e68fa16671d604635caec9), [d2eb17d](https://github.com/DPDK/dpdk/commit/d2eb17dc510ad128f7964219bccfd11bd5bbea7a), [904eaf0](https://github.com/DPDK/dpdk/commit/904eaf0da79f7d2e3c78d62706f57f9b97edbcf6), [11cf216](https://github.com/DPDK/dpdk/commit/11cf216844c56a027314ff292069b2c51e9f1a93)
- Added force_tail_drop device parameter for NIX devices. When enabled, it forces tail drop and doubles CQ descriptors. (Architecture-related: Configuration interface)
  ↳ No PR: [75473b5](https://github.com/DPDK/dpdk/commit/75473b5b62c3cb7ddfe4d3258bf00021597bca02)
- The hns3 VF driver adds support for multiple TC capabilities. VF can obtain the maximum number of TCs from the mailbox and supports configuring multiple TCs through the DCB interface. The configuration must be consistent with PF and does not support PFC. (Architecture-related: public API)
  ↳ No PR: [4bbf4f6](https://github.com/DPDK/dpdk/commit/4bbf4f689cd029dac9fdf0e5e6dc63dc15be4629), [95dc6d3](https://github.com/DPDK/dpdk/commit/95dc6d361143508077e3f3635c170d69126f8faa), [fd89a25](https://github.com/DPDK/dpdk/commit/fd89a25eb8112e0a6ff821a8f19e92b9d95082bc)
- Fixed the problem of mlx5 PMD incorrectly triggering VLAN workaround due to unknown hypervisor type on non-x86 architecture. (Architecture-related: Platform compatibility)
  ↳ No PR: [8518a4e](https://github.com/DPDK/dpdk/commit/8518a4e55980b23dfc7d855aefbef0df02e450e0)
- Fixed the problem of AEAD raw API overwriting target header bytes in out-of-place mode in QAT driver. (Architecture-related: public API)
  ↳ No PR: [06597aa](https://github.com/DPDK/dpdk/commit/06597aaac85638eaa92b66f341185cd0ba39aca6)
- Fixed the problem of chaining, encryption and authentication operations in QAT RAW API overwriting data headers in OOP mode. (Architecture-related: public API)
  ↳ No PR: [317d05f](https://github.com/DPDK/dpdk/commit/317d05f3721c9a740614adf77aa89d00d5302cf7)
- Fixed the problem of CRC data release and KEEP_CRC unloading when receiving multi-segment mbuf in the hns3 driver, ensuring that the last segment of data containing only CRC is not released incorrectly, and recalculating the CRC of specific short packets when KEEP_CRC is enabled, while disabling the use of KEEP_CRC under the NEON or SVE algorithm. (Architecture-related: platform compatibility)
  ↳ No PR: [7a99b6c](https://github.com/DPDK/dpdk/commit/7a99b6ca9d079e9364ba61d3fe802a4761739c8f), [99c065d](https://github.com/DPDK/dpdk/commit/99c065da47c432e9529f761b457cde1fd8c89f20)
- Fixed compilation failure and added necessary inclusions in the header file. (Architecture-related: public API)
  ↳ No PR: [09988bf](https://github.com/DPDK/dpdk/commit/09988bf334a18751f9b5ead9272f2b1ff2ff6866)
- Added a 64-byte alignment check for the hardware GRO function to ensure that the DMA address meets the alignment requirements on the HIP08 platform, otherwise the GRO function is disabled. (Architecture-related: platform compatibility)
  ↳ No PR: [ae68b5d](https://github.com/DPDK/dpdk/commit/ae68b5d91c632a1dde839123f27b0317cf094170)
- Fixed the configuration method of queue and TC mapping in the hns3 network card VF scenario, changing it to through firmware commands instead of directly writing registers. (Architecture-related: driver behavior change)
  ↳ No PR: [a542f48](https://github.com/DPDK/dpdk/commit/a542f48bc0ec83c296ae01ad691479c17caf99b5)
- Fixed the issue of credits release when the port is unlinked in the event/dlb2 driver, the number of single-link ports and the default credits value. (Architecture-related: public API)
  ↳ No PR: [a8b1b99](https://github.com/DPDK/dpdk/commit/a8b1b99ab23baacc57fa8612a96392e38dc9e2ca), [a1a4dd7](https://github.com/DPDK/dpdk/commit/a1a4dd731edb609d54c0ac5fc9f4652527138dc1), [07a08b1](https://github.com/DPDK/dpdk/commit/07a08b13b3bc65abe295557d1dc2609e7f4afc45)
- Reconstruct the DCB module and gather scattered DCB related fields into the hns3_dcb_info structure. (Architecture-related: core module reconstruction)
  ↳ No PR: [c90c52d](https://github.com/DPDK/dpdk/commit/c90c52d7a9028cca0686b799a7614c988d8b9b42)
- UADK compressed PMD switches from synchronous mode to asynchronous mode to improve performance. (Architecture-related: external behavior)
  ↳ No PR: [3cb49ba](https://github.com/DPDK/dpdk/commit/3cb49baa7f153ab2ce4987994ab811d1e8abcb69)
- Change the UADK encryption driver from synchronous mode to asynchronous mode to improve performance, the first operation of the chain operation remains synchronous, and adjust the summary processing of VERIFY operation. (Architecture-related: external behavior)
  ↳ No PR: [aba5b23](https://github.com/DPDK/dpdk/commit/aba5b230ca04a1956d0e45b506bb0bd69f6e45e9)
- Add lock protection for the creation, destruction, update and hardware SA read and write operations of the cnxk driver security session to prevent data corruption caused by concurrent access. (Architecture-related: public API)
  ↳ No PR: [9bebc33](https://github.com/DPDK/dpdk/commit/9bebc33703df999a405ed7103dc45230d0f1fbda)
- Mark the repr_matching_en device parameter of mlx5 PMD as deprecated in the documentation and planned to be removed in DPDK 25.11 version. (Architecture-related: public API)
  ↳ No PR: [0975fd3](https://github.com/DPDK/dpdk/commit/0975fd35047ea109a7229fc2b27a9f204d762154)
- In multiple network card driver files, change the pick_rx_func and pick_tx_func functions to conditional compilation and avoid using the __rte_used macro to improve MSVC compatibility. (Architecture-related: platform compatibility)
  ↳ No PR: [085fe09](https://github.com/DPDK/dpdk/commit/085fe092ad9fce426488d65a63505ab9c3b9deae)
- Introduced the compilation flag IXGBE_VPMD_SUPPORTED to control vector PMD support, removed platform-related stub functions, and instead used macro aliases to map vector functions to scalar implementations or NULL, simplifying compilation and code maintenance. (Architecture-related: build configuration)
  ↳ No PR: [e915d5b](https://github.com/DPDK/dpdk/commit/e915d5b94e509dee9b2e902f8498cdb22d7c666e)
- Change the prefetch control in the ixgbe driver from unconditionally enabled to using the RTE_PMD_PACKET_PREFETCH configuration option, allowing the prefetch function to be turned off at build time. (Architecture-related: Build configuration)
  ↳ No PR: [1c6bd15](https://github.com/DPDK/dpdk/commit/1c6bd15249ae1e358922c1da26355b1a0b5d1e4e)
- Add RTE_PMD_DLB2_ prefix to the token pop mode enumeration of the dlb2 driver to avoid namespace conflicts. (Architecture-related: public API)
  ↳ No PR: [e31d467](https://github.com/DPDK/dpdk/commit/e31d4679575571890974730c989aa286cb516398)

### Abstraction Layers (HAL & Bus)
- Introducing event vector adapters, providing APIs for creating and managing event vector adapters, supporting aggregation of objects into event vectors and offloading CPU overhead. (Architecture-related: New event vector adapter API)
  ↳ No PR: [e12c375](https://github.com/DPDK/dpdk/commit/e12c3754da7aecc2752e99a94bbd131c77fd4950)
- Refactor the ixgbe driver, centralize the public Rx/Tx queue setting functions into ixgbe_rxtx_vec_common.c, migrate the Rx queue data structure to the common ci_rx_queue, and extract the duplicate Rx mbuf recycling implementation to the public header file. (Architecture event: IXGBE driver core module change)
  ↳ No PR: [170a8b6](https://github.com/DPDK/dpdk/commit/170a8b6e7cc4d68b390d85628da30f5b45bf71e5), [56227d7](https://github.com/DPDK/dpdk/commit/56227d70aa3d4de89bf962c7e749a86619d294b2), [3c8c06f](https://github.com/DPDK/dpdk/commit/3c8c06fd883f416e8ddd104beca02f193b985205)
- The i40e driver switches to a universal Rx queue structure, unifies the descriptor format and macro definitions, and creates a universal Rx queue rearm header file to support ARM Neon and PowerPC AltiVec instruction sets, replacing vectorization implementation. (Architecture-related: platform compatibility)
  ↳ No PR: [0067ea7](https://github.com/DPDK/dpdk/commit/0067ea7c395095cf5d3884f9febf0a0bee310037), [b26f26b](https://github.com/DPDK/dpdk/commit/b26f26b81f58d08a6a7328cfd2888b15d73559a1)
- The ice driver migrates to the universal Rx queue structure, adds a universal definition of flex descriptor, generalizes the vectorized Rx ring refill implementation to a public file, and unifies the definitions of constants such as burst size and rearm threshold. (Architecture-related: public API)
  ↳ No PR: [e70342b](https://github.com/DPDK/dpdk/commit/e70342ba90a83be8a13713612a18273dbf03db1a), [c70e865](https://github.com/DPDK/dpdk/commit/c70e8654a81315e33d84f5d972174c9547b941c4)
- Migrate the send queue structure in idpf and cpfl drivers from idpf_tx_queue to general ci_tx_queue, and synchronously update related function type references and field names. (Architecture-related: public API)
  ↳ No PR: [695b3c3](https://github.com/DPDK/dpdk/commit/695b3c3cb63594293bc8f982bc3f66b1511c649c)
- Change the virtq_desc structure to use __rte_packed_begin and __rte_packed_end macros to avoid filling the structure memory. (Architecture-related: ABI compatibility)
  ↳ No PR: [e8e4b9c](https://github.com/DPDK/dpdk/commit/e8e4b9c71b741f09e815af3a4bda2dab7cfe5636)
- The iavf driver switches to using the universal Rx queue structure, replaces iavf-specific descriptors with a universal format, and forces the use of only 32-byte descriptors. (Architecture-related: public API)
  ↳ No PR: [399b294](https://github.com/DPDK/dpdk/commit/399b2946a9b2a823d745f268c8ff33f03f308caa)
- Support enabling opacity mode in common/cnxk, adding flag to override the default natural alignment mode. (Architecture-related: public API)
  ↳ No PR: [77b72fa](https://github.com/DPDK/dpdk/commit/77b72faa388f426613d15f46d9ec9ecc332142b9)
- Add Rx/Tx burst mode information acquisition function to ixgbe driver, and add corresponding API and internal data structure. (Architecture event: IXGBE driver adds Rx/Tx burst mode API)
  ↳ No PR: [1e77640](https://github.com/DPDK/dpdk/commit/1e77640e559524a5a0bbad0665dfc98683769a9e)
- Add Rx/Tx burst mode information acquisition function to the IAVF driver, and reconstruct the burst function array to support returning the corresponding mode information according to the selected burst function name. (Architecture event: IAVF driver adds Rx/Tx burst mode API)
  ↳ No PR: [0d5a856](https://github.com/DPDK/dpdk/commit/0d5a856f5be9c6dc984d6bce6e72e41fbdb0aa7a)
- Migrate the cnxk_gpio driver from the deprecated sysfs GPIO interface to the character device-based GPIO v2 interface, and remove the interrupt mechanism that directly bypasses the kernel. (Architecture-related: GPIO v2 interface migration)
  ↳ No PR: [9a5ce79](https://github.com/DPDK/dpdk/commit/9a5ce79325da04a8ff3ca247d27e5530ca597036)
- Add CC bit settings for ixgbe VF driver to ensure that all VF Tx paths (including simple, offloaded and vectorized paths) have context descriptors set to be compatible with the hardware malicious driver detection (MDD) function. (Architecture-related: Hardware Compatibility: MDD)
  ↳ No PR: [85b7d47](https://github.com/DPDK/dpdk/commit/85b7d47d564ffbe206a7d17bf5a0ed9dff17b555)
- Add basic PCIe ethdev detection and removal functions to net/rnp driver. (Architecture-related: PCIe ethdev detection/removal)
  ↳ No PR: [0dc7115](https://github.com/DPDK/dpdk/commit/0dc7115d27f29faf8d136116a1af8c4d4361ee07)
- Added basic mailbox operations for rnp PMD driver, supporting communication between PF, firmware and VF driver. (Architecture-related: mailbox communication)
  ↳ No PR: [18d555f](https://github.com/DPDK/dpdk/commit/18d555f74fcf54c651e0a1635b06d8114b794fbb)
- Add device initialization and de-initialization functions to the RNP network card, including basic operations such as firmware communication, hardware reset, MAC initialization, transceiver queue control, interrupt processing and resource release. (Architecture-related: driver core module)
  ↳ No PR: [52dfb84](https://github.com/DPDK/dpdk/commit/52dfb84e14be1d1e3663c4ff6b628f247e8e207a)
- Added the function of obtaining device hardware capabilities, including obtaining channel status, link synchronization initialization and PF link event enablement. (Architecture-related: driver core module)
  ↳ No PR: [52aae4e](https://github.com/DPDK/dpdk/commit/52aae4ed4ffb3e553ec706d202b20af4ddbbeb95)
- Add MAC promiscuous mode support to the RNP network driver, including unicast, multicast and broadcast promiscuous modes. (Architecture-related: driver core module)
  ↳ No PR: [e657b76](https://github.com/DPDK/dpdk/commit/e657b7620ae04d98e0c603a5a9ec203b017ffe8d)
- Support the setting and release of TX/RX queue, and add hardware BD queue reset and software queue reset functions. (Architecture-related: driver core module)
  ↳ No PR: [191c637](https://github.com/DPDK/dpdk/commit/191c63742b34d5d2ca331f02027511d4ed1a9ffc)
- Add the start and stop functions of receiving and sending queues to the rnp network card driver. (Architecture-related: driver core module)
  ↳ No PR: [7e805a0](https://github.com/DPDK/dpdk/commit/7e805a027f5d226024b19974ca0fd06956e91254)
- Add basic support for device start and stop to the rnp network device driver, and add functions for setting general operations and clock validity checks. (Architecture-related: driver core module)
  ↳ No PR: [ff9b9a5](https://github.com/DPDK/dpdk/commit/ff9b9a5c00f17567665329bb5f1199d5f17f09a3)
- Add RSS support to rnp network card driver, including RETA update/query, hash configuration acquisition/update, and add RSS configuration check in device configuration. (Architecture-related: driver core module)
  ↳ No PR: [31af554](https://github.com/DPDK/dpdk/commit/31af55425feec1a23ee23d11f054bfbab76891b8)
- Add link update support to the rnp network card driver to implement two link acquisition modes: polling and interrupt. (Architecture-related: driver core module)
  ↳ No PR: [2292ece](https://github.com/DPDK/dpdk/commit/2292ecee5307c418376ba5b3ff12801a2367eb59)
- Add support for setting link uplink and downlink for rnp network card driver. (Architecture-related: public API)
  ↳ No PR: [a3c800e](https://github.com/DPDK/dpdk/commit/a3c800e6303749433e07b98cc3e922b15f621b47)
- Add simple receive burst function to rnp network card driver, support checksum parsing, VLAN stripping and receive ring filling. (Architecture-related: public API)
  ↳ No PR: [0780455](https://github.com/DPDK/dpdk/commit/07804556fbb143803cfad38059d7547ee85259e8)
- Add a simple data packet sending function to the rnp network card driver, and implement support for VLAN insertion and uninstallation, receiving ring filling and sending ring cleaning. (Architecture-related: public API)
  ↳ No PR: [5973c1e](https://github.com/DPDK/dpdk/commit/5973c1ee9598dbcbfebed7d4004639f8981a96a0)
- Support MTU settings, and use the maximum MTU limit of each port for reception in multi-port mode. (Architecture-related: public API)
  ↳ No PR: [0ca46a6](https://github.com/DPDK/dpdk/commit/0ca46a6f5768aab581910b544bc20f7bec7fcbd7)
- Add support for receiving scattered multi-segment data packets to the RNP network card driver, add receiving, sending and cleaning functions, and update statistical counting and parsing logic. (Architecture-related: public API)
  ↳ No PR: [aba4a6b](https://github.com/DPDK/dpdk/commit/aba4a6ba6263ea9c0b010f8e31f9adf2f29592cc)
- Add multi-segment mbuf sending support for rnp network card driver. (Architecture-related: public API)
  ↳ No PR: [656edf8](https://github.com/DPDK/dpdk/commit/656edf8caa6b486332c599b4698d50dc085f9d18)
- Add basic statistical functions to the rnp network card driver, supporting statistics on hardware packet loss, sent and received bytes and number of packets. (Architecture-related: public API)
  ↳ No PR: [497ba2f](https://github.com/DPDK/dpdk/commit/497ba2faf1f78770dec71ccd7e53c23c7381ad8e)
- Add hardware extended statistics (xstats) support to the rnp network card driver, including MAC, Ethernet, receive and send statistics, and add MTU setting function. (Architecture-related: public API)
  ↳ No PR: [6c8e7a0](https://github.com/DPDK/dpdk/commit/6c8e7a078338836863fd7b3d3dd0668f96f33aed)
- Added a queue information acquisition function for the rnp network card driver, allowing users to view the configuration details of the sending and receiving queues during debugging. (Architecture-related: public API)
  ↳ No PR: [f174764](https://github.com/DPDK/dpdk/commit/f17476465226bead6b312384d85c55b31f0c9313)
- Added Rx/Tx burst mode information acquisition function for net/rnp driver. (Architecture-related: public API)
  ↳ No PR: [9e22b4f](https://github.com/DPDK/dpdk/commit/9e22b4fe67dfce4983d1bd42461b478ed5cb5a4c)
- Updated the CN20K model number, added cnf205 support, and added an API for identifying the corresponding model. (Architecture-related: public API)
  ↳ No PR: [a562871](https://github.com/DPDK/dpdk/commit/a56287160cd26e913e36033cb932434106ca53ec)
- The process private data area is introduced in the netvsc driver, and the get_vmbus_device function is added to support setting hyperv events from the secondary process. (Architecture-related: secondary process support)
  ↳ No PR: [2c1d5c2](https://github.com/DPDK/dpdk/commit/2c1d5c20b7afe0753eeeffa0cf3aeb50e2fd9089), [11c0663](https://github.com/DPDK/dpdk/commit/11c0663c94454a103ea74d50c9436af4ef5aadd8)
- Added support for the Medford4 NIC family, including NIC family discovery, minimal probing, X4522 and X4542 model support, and PCI ID addition. (Architecture-related: New hardware support: Medford4)
  ↳ No PR: [277ef02](https://github.com/DPDK/dpdk/commit/277ef02e94ac61c1a84febee28f1f169a327dec8), [0ca0330](https://github.com/DPDK/dpdk/commit/0ca03304f1774dce16f7769fc5c68dcf03af3e41), [012633a](https://github.com/DPDK/dpdk/commit/012633a2d720209cca88d900871ef47a5a05f66b)
- Updated the MCDI header file, adding new port direction, PCIe interface, event code, MAC statistics, resource limits and queue processing definitions for the X4 network port. (Architecture-related: public API: MCDI header file)
  ↳ No PR: [55dda80](https://github.com/DPDK/dpdk/commit/55dda80226d5b29147395ebbe166f93d6385476b)
- Enhanced the netport detection path of Medford4 network card, added netport attach/detach stub function, network port handle acquisition, hardware capability to software capability mapping, link status decoding and loopback mode support. (Architecture-related: public API: netport detection)
  ↳ No PR: [dcbdefe](https://github.com/DPDK/dpdk/commit/dcbdefee5d1efb2b38c300756d72c67e70c36211), [72c24d6](https://github.com/DPDK/dpdk/commit/72c24d6e2e458e07b24c316da48b67e6cd2e2053), [a90549f](https://github.com/DPDK/dpdk/commit/a90549f527eb3d7001703cb1f5bce5096b12c0a5), [06f569d](https://github.com/DPDK/dpdk/commit/06f569de6c06c8283dfcf4bfee4bd6d8391d2539), [2be7d23](https://github.com/DPDK/dpdk/commit/2be7d23f3fe61322f0a0d7be8739de6cae01cb8e), [643b484](https://github.com/DPDK/dpdk/commit/643b484b076aeaeac25d42ae2326dda88e80093d), [18a7c1f](https://github.com/DPDK/dpdk/commit/18a7c1fb5b91340e61f1104c07043756cdaea291)
- Implemented PHY link status acquisition and control for Medford4, reconstructed the link mode decoding auxiliary function, supported 200G link mode and FEC type, and added loopback, rate, and flow control configuration. (Architecture-related: public API: PHY link control)
  ↳ No PR: [407cbf6](https://github.com/DPDK/dpdk/commit/407cbf620c0299e12a3a073f0b4e39fa19bf9fbc), [2a5cf77](https://github.com/DPDK/dpdk/commit/2a5cf77e6de8fe06a8a1a8c942fdeeac940dfcd5), [8e79cd3](https://github.com/DPDK/dpdk/commit/8e79cd30230df0b17fec23a81122341f2ec600c7)
- Added link event processing to support new network cards, including handling new link change events and ignoring old events, and setting a flag to instruct the client driver to query the link status by itself. (Architecture-related: driver behavior)
  ↳ No PR: [f906292](https://github.com/DPDK/dpdk/commit/f9062928a4ad225d5d7fae05f87599f47adacd3f), [ce09d30](https://github.com/DPDK/dpdk/commit/ce09d307e94fa1ccac637c966ae023c7b21dc52f)
- Added support for physical port lane count control, allowing client drivers to set and query possible values of lane count. (Architecture-related: public API)
  ↳ No PR: [b50ff44](https://github.com/DPDK/dpdk/commit/b50ff442479c4ae87699e02d1a6e10daf0ae59ac), [bca6c5f](https://github.com/DPDK/dpdk/commit/bca6c5f18f806c4084e28d44f0713aa71e817472)
- In the virtio encryption device driver, increase the maximum signature size and maximum control data size to 1024 bytes and 4096 bytes respectively to support RSA 8K modular operation. (Architecture-related: public API constant changes)
  ↳ No PR: [eb9714e](https://github.com/DPDK/dpdk/commit/eb9714eaa6127d3d06cc073bb0b76639966a19b8)
- During the initialization of the auxiliary process, by forcing the address to map PCI resources and using the EAL base address as the mmap prompt, avoid mapping device resources to the memory allocation area and reduce mapping conflicts. (Architecture-related: PCI resource mapping strategy)
  ↳ No PR: [22e413e](https://github.com/DPDK/dpdk/commit/22e413e578acf4913f057e146f47704c2f941b7f), [2562435](https://github.com/DPDK/dpdk/commit/25624350f12c9b2a5b52c44c62bbb4420a65fab6)
- Added support for result address offset in CPT result address configuration, allowing the offset to be set relative to the WQE address. (Architecture-related: public API)
  ↳ No PR: [b6b4928](https://github.com/DPDK/dpdk/commit/b6b49284fb21478935ca411f91f7792dfbf22519)
- Enabled the IV provided by the application as the default option for CN9k, and removed the conditional restrictions in debug mode. (Architecture-related: driver behavior)
  ↳ No PR: [b8b35df](https://github.com/DPDK/dpdk/commit/b8b35df9924dc6807afe3bacba81d12977c1debb)
- Added ice_add_mac_with_fltr_flag function to support specifying custom flags when adding MAC filtering rules. (Architecture-related: public API)
  ↳ No PR: [ac6d702](https://github.com/DPDK/dpdk/commit/ac6d702b30e3ab10262d8df18f2628700ef7f4e3)
- Added support for 12-bit sequence number size in PDCP user plane processing. (Architecture-related: public API)
  ↳ No PR: [e6410dd](https://github.com/DPDK/dpdk/commit/e6410dd109554202c62869f6aaba8ac9a7b0039c)
- Added an operation index acquisition interface for the DPAA2 memory pool, and verified the uniqueness of the operation index when creating the pool. (Architecture-related: public API)
  ↳ No PR: [de6a6e8](https://github.com/DPDK/dpdk/commit/de6a6e897fe6e1bdaedf6eda0e0cd04372dbdceb)
- Added disable_xqe_drop device parameter, used to disable XQE drop in RQ context. (Architecture-related: configuration interface)
  ↳ No PR: [17a1c9d](https://github.com/DPDK/dpdk/commit/17a1c9dff5c17ab3ac99e360fe5020e238b1d0a3), [0344fb5](https://github.com/DPDK/dpdk/commit/0344fb5a59c22739d1c05c3487281c7aa54ea1ac)
- Added a default software vector adapter for event devices, falling back to the service core-based software implementation when the hardware does not support it. (Architecture-related: public API)
  ↳ No PR: [de09387](https://github.com/DPDK/dpdk/commit/de09387f13130fbb708a40f6a64154a91089d7ef)
- Added PCI detection and removal support for CN20K encryption devices. (Architecture-related: Platform compatibility)
  ↳ No PR: [332580b](https://github.com/DPDK/dpdk/commit/332580b77493f11a530d8fc471f8ee04fa9670bb)
- Added check for the maximum number of gather entries in CNXK CPT PMD. (Architecture-related: public API)
  ↳ No PR: [127dfd0](https://github.com/DPDK/dpdk/commit/127dfd079ad5cb3de186d4f8bcb140a77e7d1dd6)
- Added metadata field in CNXK CPT driver for passing custom metadata to firmware. (Architecture-related: public API)
  ↳ No PR: [cbce932](https://github.com/DPDK/dpdk/commit/cbce9328403f7024885c17d76d7541f28aa4f90e)
- Added driver support for RTL8168EP/FP/G/H/M network cards, and restructured the DASH code. (Architecture-related: new driver support)
  ↳ No PR: [d9ee71b](https://github.com/DPDK/dpdk/commit/d9ee71b5f1bc579fd9836e79bc8419eac4937c9e)
- Added support for Tx queue contiguous memory pre-allocation for the mlx5 driver, and controls memory alignment through the device parameter txq_mem_algn. (Architecture-related: public API)
  ↳ No PR: [5bbee57](https://github.com/DPDK/dpdk/commit/5bbee57ed5bc21aae6625a4599e3c381cceb92ff), [bbfab2e](https://github.com/DPDK/dpdk/commit/bbfab2eb2528023d9788626d8115fbd42bcb7262), [d941773](https://github.com/DPDK/dpdk/commit/d941773392891a5e57dba48348413372047b1750), [d81e441](https://github.com/DPDK/dpdk/commit/d81e441d7db35e623ce8cd365c64ee6a313f5c1b)
- Added event vector adapter support for the CN20K event device, and added the creation, destruction and enqueuing functions of the vector adapter. (Architecture-related: public API)
  ↳ No PR: [6cf1348](https://github.com/DPDK/dpdk/commit/6cf1348bbfc80abdc4245b37cf5302ca7723bd35)
- Support event/dlb2 driver to perform data path operations in secondary process. (Architecture-related: secondary process support)
  ↳ No PR: [ab10f17](https://github.com/DPDK/dpdk/commit/ab10f1784fea9793d2eb4cada1012ea5118215d0)
- Added crypto adapter support to the CN20K platform, realizing the adaptation function between event devices and encryption devices. (Architecture-related: crypto adapter)
  ↳ No PR: [0e41653](https://github.com/DPDK/dpdk/commit/0e41653d6add0b5932aba39cd00dcdb5949fe702)
- Supports management of the history list resources of DLB2 event device ports through command line parameters, and adds a new runtime API to set port parameters. (Architecture-related: public API)
  ↳ No PR: [c6aa538](https://github.com/DPDK/dpdk/commit/c6aa538b1cdf137490d5e69be53a770ab1b692cf), [97bcb3b](https://github.com/DPDK/dpdk/commit/97bcb3befdee0ceabd2cfa0f5dc4218438fdd34c)
- Added PF mode support for MANA network card. (Architecture-related: driver compatibility)
  ↳ No PR: [484de92](https://github.com/DPDK/dpdk/commit/484de923a5f2aec73f8d8ee0f7ab86bfde603eec), [be4ed96](https://github.com/DPDK/dpdk/commit/be4ed96378811e572860cac558bff54b5c361992)
- Added cross-NUMA node memory allocation support for the mlx5 driver, automatically falling back to other nodes when the local NUMA node has no available memory. (Architecture-related: NUMA support)
  ↳ No PR: [ce2cf34](https://github.com/DPDK/dpdk/commit/ce2cf3403f2ac2c6e5eac05a43db9207e35e8b9d)
- Added correct implementation of queue start/stop function for net/ntnic driver, and supported queue delayed start. (Architecture-related: public API)
  ↳ No PR: [c9612af](https://github.com/DPDK/dpdk/commit/c9612af946a7432e0364717c6c4559ff33c0d3c1), [0722793](https://github.com/DPDK/dpdk/commit/07227933a4b5038fa956ca5c6c41fa2fffcee5e8)
- The ENA network card driver adds support for fragmentation bypass mode, which can be controlled through devarg enable_frag_bypass and is disabled by default. (Architecture-related: devarg configuration)
  ↳ No PR: [bb80ed3](https://github.com/DPDK/dpdk/commit/bb80ed3dd16f773dba2318b58dd8602f90efa170)
- Converted lock and memory allocation functions into macros, and removed ixgbe_osdep.c file to fix thread safety analysis errors reported by lock checker on FreeBSD. (Architectural event: IXGBE_Driver_Core module change)
  ↳ No PR: [b4ce09b](https://github.com/DPDK/dpdk/commit/b4ce09b852e27dc37c18ebff52ea994cd5253352)
- Supports multi-host LAG detection, expands the LAG port array and allows holes in the middle to avoid out-of-bounds array access caused by discontinuous port identifiers. (Architecture-related: public API)
  ↳ No PR: [8144d7e](https://github.com/DPDK/dpdk/commit/8144d7e327b8744b47d4cafe4f6f45796acaabf4)
- Trigger defragmentation and retry when MCAM allocation fails, adjust allocation parameters according to KEX configuration type, and support MCAM reading of CN20K. (Architecture-related: platform compatibility)
  ↳ No PR: [cb360b2](https://github.com/DPDK/dpdk/commit/cb360b201bb7e1f2760eff325609684f40670c10)
- Optimized message processing to be compatible with older firmware versions, and fixed related issues. (Architecture-related: platform compatibility)
  ↳ No PR: [7870e9f](https://github.com/DPDK/dpdk/commit/7870e9f8c43aad1b955a05230210555c630a1417)
- Adjusted the setting of aura offset in NPA_LF_POOL_OP_INT register according to the platform to adapt to the change of aura field width on cn20k. (Architecture-related: platform compatibility)
  ↳ No PR: [270cd2d](https://github.com/DPDK/dpdk/commit/270cd2d12d55eb1dc7677344160dac44aca3030c)
- Standardized the endianness of Rx descriptors, ensuring that all read and write operations correctly use little-endian. (Architecture-related: platform compatibility)
  ↳ No PR: [22252c5](https://github.com/DPDK/dpdk/commit/22252c56bfa2085072d25e0f741111eb0dfa81de)
- Fixed the byte order problem of NFD3 send descriptor, and uniformly converted related fields to little-endian format. (Architecture-related: platform compatibility)
  ↳ No PR: [1095bb0](https://github.com/DPDK/dpdk/commit/1095bb0f86fafee3c7dca7b2dd23075ae869f689)
- Corrected the MAC PDU calculation for the Medford4 network card, added a new general helper function and used this function in the net/sfc driver to avoid using legacy bug fix macros. (Architecture-related: public API)
  ↳ No PR: [add6e01](https://github.com/DPDK/dpdk/commit/add6e01741f58ed71b2dcf3fa99722fef385d9f1), [57a7655](https://github.com/DPDK/dpdk/commit/57a7655b74db3c6bca3a10dcb3a25611ebc10eb1)
- Standardized the byte order of NFDk send descriptors to little endian, and modified related field types. (Architecture-related: platform compatibility)
  ↳ No PR: [ae1baec](https://github.com/DPDK/dpdk/commit/ae1baeca61cf11beea62364bcc0a80ff261abe7c)
- Fixed vmbus ring buffer data area address calculation, using system page size instead of fixed 4k. (Architecture-related: platform compatibility)
  ↳ No PR: [c54fa45](https://github.com/DPDK/dpdk/commit/c54fa45817932057dd8f275fa1b8e4dcaede7813)
- Fixed the Hyper-V page size issue in the vmbus driver, using Hyper-V's 4k page size instead of the system page size. (Architecture-related: platform compatibility)
  ↳ No PR: [30f24d3](https://github.com/DPDK/dpdk/commit/30f24d33f33bbb29b1fba32b01e8c8d77400a5d5)
- Modified the MCDI structure access macro, added uintptr_t conversion to support buffers with const qualifiers, and avoided compilation warnings. (Architecture-related: public API)
  ↳ No PR: [4dfe271](https://github.com/DPDK/dpdk/commit/4dfe2718cea51913a602a323a9ec0844bc96176f)
- Fixed the deadlock problem that may be caused by queues and mutex locks in high-traffic learning scenarios, and changed the reading and writing of the learn_ignored flag to atomic operations to avoid thread competition. (Architecture-related: public API)
  ↳ No PR: [ce6d246](https://github.com/DPDK/dpdk/commit/ce6d246a490c3a805b172b33c498b070b06e2f88)
- Fixed a race condition in the PCI UIO device existence check under FreeBSD, using open(2) instead of access(2) to avoid the problem of device files being removed after checking. (Architecture-related: platform compatibility)
  ↳ No PR: [6d4e6db](https://github.com/DPDK/dpdk/commit/6d4e6dbccc3bd965bfd5e5836d7cb21c1b1f9c6c)
- Fixed out-of-bounds access and uninitialized variable issues in SM2 signature verification preprocessing in the cnxk encryption driver, added upper limit checks for private key length and public key coordinate length, and fixed uninitialized local variables in the cnxk_ae_fill_ec_params function. (Architecture-related: public API)
  ↳ No PR: [cfefc94](https://github.com/DPDK/dpdk/commit/cfefc94a8c155aceb2da519b6b34a01b5caa65e3), [1f72074](https://github.com/DPDK/dpdk/commit/1f720746bed33069c72b7ed08546aea5e9a9aed4)
- Fixed a race condition in the PDCP key command, added a CALM directive in the 12-bit SN scenario, and fell back to using legacy descriptors in the 18-bit SN scenario. (Architecture-related: public API)
  ↳ No PR: [684faac](https://github.com/DPDK/dpdk/commit/684faacc0fde7110c31c640669381dbf19f447f8)
- Fixed the setting order of the last segment length during the scatter list filling process, and added a check that the number of segments exceeds the maximum supported number. (Architecture-related: public API)
  ↳ No PR: [3644dc3](https://github.com/DPDK/dpdk/commit/3644dc3205e6be1a33eb6303c29731acac5b9aaa)
- Moved CN10K's encryption instruction debug dump function to public code for use by CN20K, and fixed field errors in queue pair statistics. (Architecture-related: public API)
  ↳ No PR: [28c1915](https://github.com/DPDK/dpdk/commit/28c191505ab7069ed2d0f3fca5c5f2eb2dfafdab)
- Fixed MSVC compilation error, replacing inline assembly with compiler built-in functions __cpuid and _InterlockedCompareExchange128. (Architecture-related: platform compatibility)
  ↳ No PR: [0d838a1](https://github.com/DPDK/dpdk/commit/0d838a12b320c6f720385f036b9ff2210739048d)
- Fixed the E610 adapter link status mismatch problem, added a mailbox operation to allow the VF driver to request PF to provide actual link data, and updated the mailbox API to v1.6. (Architecture-related: mailbox API)
  ↳ No PR: [adbd710](https://github.com/DPDK/dpdk/commit/adbd71030575771813a9a89a72845d259db764c4)
- Extend the mailbox timeout from 1200 milliseconds to 2500 milliseconds to avoid control network API request failures due to too short timeouts and improve reliability. (Architecture-related: platform compatibility)
  ↳ No PR: [e90979e](https://github.com/DPDK/dpdk/commit/e90979eebbea093f6bab2d7c222fc5f5c9a85eff)
- Fixed the issue where the device may be falsely reported as unresponsive when the control path polling interval is too low, and the lower limit of the effective interval range is adjusted from 1 millisecond to 500 milliseconds. (Architecture-related: public API)
  ↳ No PR: [7905edc](https://github.com/DPDK/dpdk/commit/7905edcda144899abebf1504036fde6b3439e398)
- Fixed the demapping of DMA when the queue is released, and solved the multiple mapping problem when IOMMU is not optimized. (Architecture-related: public API)
  ↳ No PR: [842c1ce](https://github.com/DPDK/dpdk/commit/842c1cee225ca8c79a8a321e2194f83d54a4495a)
- Fixed MSVC compilation error, replacing sizeof(rte_v128u32_t) with macro MLX5_SIZE_MOV16 to eliminate undeclared identifier issue. (Architecture-related: build compatibility)
  ↳ No PR: [0ed20cb](https://github.com/DPDK/dpdk/commit/0ed20cb5eb557cd146256c5d198339bbd58a9699)
- Fixed the out-of-order problem caused by out-of-order arrival of CQE in the shared Rx queue, introduced a sliding window mechanism to track WQE processing progress, and added a new Rx burst function that supports out-of-order. (Architecture-related: public API)
  ↳ No PR: [5f92236](https://github.com/DPDK/dpdk/commit/5f9223611f3570c974b9c8e6c0b62db605fb3076)
- Fixed DER encoding of RSA public keys to comply with RFC 8017 standard. (Architecture-related: public API behavior)
  ↳ No PR: [dd89922](https://github.com/DPDK/dpdk/commit/dd89922616f3e8d6b14b813d1452dea84b869cd7)
- Fixed the problem of missing maximum queue size query in mlx5 PMD Verbs mode, unified acquisition and restriction of queue creation. (Architecture-related: public API)
  ↳ No PR: [9de8acd](https://github.com/DPDK/dpdk/commit/9de8acd30d5adfc5b9703d15a3e1babc7d4ddacc)
- Fix the RSA session parameter setting in the OpenSSL encryption driver to ensure that the private key index is included to comply with RFC 8017. (Architecture-related: RFC 8017 compliance)
  ↳ No PR: [9020477](https://github.com/DPDK/dpdk/commit/9020477270c5dc93e1a347b90d5248b10e8cc4e3)
- Update the CPT parsing header hardware structure to adapt to CN20K, adjust the fields and offset calculations in the debug output. (Architecture-related: hardware adaptation)
  ↳ No PR: [63c19ce](https://github.com/DPDK/dpdk/commit/63c19ce0f6b9a18a8801630e540e9010043f86b7)
- The ixgbe driver switches to the public Rx reordering code, and uniformly uses the descriptor size, burst size and reordering threshold definitions in the public header file; at the same time, the unused read head register address field in the Rx queue structure is removed, and the variable names are unified to be consistent with other drivers. (Architectural event: IXGBE driver core module change)
  ↳ No PR: [e3eda1c](https://github.com/DPDK/dpdk/commit/e3eda1cf9928871b55926fdcfad44b57378a924b), [a2c4c5f](https://github.com/DPDK/dpdk/commit/a2c4c5f738fa5f59e09737a27f801186d9e075f3), [5f95eec](https://github.com/DPDK/dpdk/commit/5f95eecce8c16eb0f714c06dd8d294ceba8196e1)
- Removed redundant and unused fields in the public Tx queue structure, and cleaned up related function implementations to reduce memory usage. (Architecture-related: public API)
  ↳ No PR: [add4903](https://github.com/DPDK/dpdk/commit/add4903c93d050e45b164005559a717ccf8153a4)
- Replace #pragma pack with __rte_packed_begin and __rte_packed_end macros to unify the compact memory layout of structures/unions. (Architecture-related: public API)
  ↳ No PR: [724832b](https://github.com/DPDK/dpdk/commit/724832b177f02ba49afca71f031269f1fd1b647c)
- Extract the secure session instruction word generation function shared by CN10K and CN20K into the public header file, and update the TLS session creation logic to call the public function. (Architecture-related: Cross-module shared function extraction)
  ↳ No PR: [f0244c9](https://github.com/DPDK/dpdk/commit/f0244c95c84a4b491a76a822d842cb1d2435a2cc)
- Change the IPsec statistics structure from direct embedding to dynamic allocation to prepare for subsequent migration to the universal Rx queue structure. (Architecture-related: Rx queue structure preparation)
  ↳ No PR: [40db6a6](https://github.com/DPDK/dpdk/commit/40db6a6202f2915dd778d5e81855ce5e1fd41424)
- Decouple the function that releases Rx mbufs in the ixgbe driver, separate the vectorized and non-vectorized versions, and add public functions to selectively call based on the queue type. (Architecture-related: Rx mbuf release reconstruction)
  ↳ No PR: [171e89a](https://github.com/DPDK/dpdk/commit/171e89a5c9ef859f78ded889ee27d76d28c55f8d)
- Extract the duplicate Tx mbuf recycling logic in ixgbe and i40e drivers to a common header file, and update the i40e driver to use this common implementation. (Architecture-related: driver common logic extraction)
  ↳ No PR: [f5fd081](https://github.com/DPDK/dpdk/commit/f5fd081c86ae415515ab55cbacf10c9c50536ca1)
- Enable AVX2 vector instruction set for CPUs that do not support AVX512 to improve per-core performance of single-queue Rx/Tx. (Architecture-related: Platform compatibility)
  ↳ No PR: [6140a0c](https://github.com/DPDK/dpdk/commit/6140a0c11399997fbf90f531d2e9b03111c4b862)
- Add support for AVX2 and AVX512 instruction sets for the Rx rearm operation of Intel network cards, so that the 32-byte descriptor format can also use wider x86 vectors. (Architecture-related: Platform compatibility)
  ↳ No PR: [798f625](https://github.com/DPDK/dpdk/commit/798f6255a44f0e2dfce2b5150814f8438bec0869)
- Configure independent drop and backpressure thresholds for cnxk-driven CQ, and optimize the drop threshold of security packages. (Architecture-related: public API)
  ↳ No PR: [9fc6620](https://github.com/DPDK/dpdk/commit/9fc6620d1513709954719ebe995e3fd40b788bfb)
- Update the document to add descriptions of the kernel options CONFIG_NET_TC_SKB_EXT and CONFIG_MLX5_CLS_ACT required by the MLX5 driver. (Architecture-related: MLX5 driver kernel options)
  ↳ No PR: [3101799](https://github.com/DPDK/dpdk/commit/3101799fce0016061ff7aa9c3c2ad7155aff1073)
- Update the documentation for compiling mlx5 on Windows to clearly distinguish the link parameters of MSVC and Clang compilers. (Architecture-related: build and installation methods)
  ↳ No PR: [f65583b](https://github.com/DPDK/dpdk/commit/f65583bdd8d252046240b9790f8cbe3433334f67)
- Simplify the way to build the base code in the Intel network card driver. It no longer uses precompiled static libraries, but directly includes the source file list. (Architecture-related: build and installation methods)
  ↳ No PR: [0c4fb26](https://github.com/DPDK/dpdk/commit/0c4fb260a3dd4e977e88cbf5c8e39289bcc94520), [65de215](https://github.com/DPDK/dpdk/commit/65de215007a21de11f9749f44e6b90fab7afd9af), [6039f3c](https://github.com/DPDK/dpdk/commit/6039f3c78214c9ab8737806eae5573f02a482312), [cc10890](https://github.com/DPDK/dpdk/commit/cc1089089d13439698e6ce84f0e622a980a7a0f8)
- The mldev library now supports building with the MSVC compiler. (Architecture-related: Platform compatibility)
  ↳ No PR: [c35666d](https://github.com/DPDK/dpdk/commit/c35666dab9134cdaa1620b392280f5fdf7947d70)
- Add RTE_PMD_EXPORT_SYMBOL macro to support MSVC compiler, and refactor related macro definitions and variable declarations to ensure that driver information can be correctly embedded in the binary in MSVC builds. (Architecture-related: platform compatibility)
  ↳ No PR: [87cf44f](https://github.com/DPDK/dpdk/commit/87cf44faf0e8f5a0b12db1bbaf3e995da39d0e6c)
- Add __builtin_add_overflow macro definition for MSVC compiler in ice base driver. (Architecture-related: platform compatibility)
  ↳ No PR: [cfe9fd0](https://github.com/DPDK/dpdk/commit/cfe9fd0ae836b9ee59db4115dc716dd545c5d3f5)
- Remove the __COUNTER__ parameter in the RTE_PMD_EXPORT_NAME macro and instead directly use the driver name to generate unique symbols to support the MSVC compiler. (Architecture-related: public API)
  ↳ No PR: [facca4d](https://github.com/DPDK/dpdk/commit/facca4dd86adc655eca2930bbed3bd0c8f695350)
- Rename the macro RTE_LIBRTE_I40E_16BYTE_RX_DESC of the 16-byte Rx descriptor in the i40e driver to RTE_NET_INTEL_USE_16BYTE_DESC, and update the related function parameter types. (Architecture-related: public API)
  ↳ No PR: [4c4b9ce](https://github.com/DPDK/dpdk/commit/4c4b9ce017fec5932c462ec67afe93dadbc8258d)
- Fixed the problem of mlx5 dependency detection failure on Windows, it is no longer mandatory that the mlx5devx library must exist. (Architecture-related: platform compatibility)
  ↳ No PR: [2dd1f66](https://github.com/DPDK/dpdk/commit/2dd1f6656ec9690fbcbd782f03fba5c38b32d9f3)

### Core DPDK Framework
- Reconstruct the symbol versioning macros, introduce new macros such as RTE_VERSION_SYMBOL, RTE_DEFAULT_SYMBOL, etc., unify the symbol versioning processing of GCC and MSVC, and add export macros for a large number of functions to clearly mark exported symbols. (Architecture-related: public API)
  ↳ No PR: [e30e194](https://github.com/DPDK/dpdk/commit/e30e194c4d06cf9b0e93f9f0f2a289bef96abc1a), [c7020bb](https://github.com/DPDK/dpdk/commit/c7020bb20fc7d85e6ceee5a72719a61f4ffcb950)
- Move driver export macros from public header files to driver-specific header files to hide internal implementation details. (Architecture-related: public API)
  ↳ No PR: [e691fe3](https://github.com/DPDK/dpdk/commit/e691fe3857cb58d98036a876a680ecf858beae0f)
- Renamed EAL options --socket-mem and --socket-limit to --numa-mem and --numa-limit, the old names remain backward compatible. (Architecture-related: public API)
  ↳ No PR: [1b50f5c](https://github.com/DPDK/dpdk/commit/1b50f5c96ad68caf36d4af97fcaec991cdd74bc8)
- Add compile-time constant checking support for MSVC compiler, define macro __rte_constant instead of __builtin_constant_p. (Architecture-related: platform compatibility)
  ↳ No PR: [9db5d0c](https://github.com/DPDK/dpdk/commit/9db5d0c2f6ed100083902ed2ab0b82c56ea3c62f)
- The argparse library changes to recording parsed parameters in an internal array, no longer modifies the parameter structure passed in by the user, and supports reuse of the parameter structure. (Architecture-related: external behavior)
  ↳ No PR: [4597715](https://github.com/DPDK/dpdk/commit/4597715e7e0872daf2674c2def2193c4eea03bd8)
- Added rte_node_free API, used to release nodes and their memory that do not belong to any graph. (Architecture events: Added rte_node_free API)
  ↳ No PR: [16b7191](https://github.com/DPDK/dpdk/commit/16b719196c94dac54dd28be1e52f3fdb8f76e3f0)
- Expose the next nodes enumeration definition of package classification nodes, and add IPv4 and IPv6 FIB lookup as next hop options. (Architecture event: NFP_Common module change)
  ↳ No PR: [b46e83c](https://github.com/DPDK/dpdk/commit/b46e83c3ed41bc8c87bcc029e056af653a54445d), [13bda1d](https://github.com/DPDK/dpdk/commit/13bda1d04c0c46e3ab971b5d6d051bcc3fc238e9), [5ae1fab](https://github.com/DPDK/dpdk/commit/5ae1fabf36441d5e7eaa7240b90927408db20ef5)
- Added IPv6 search FIB node, and provided IPv6 FIB routing to add public functions. (Architecture event: NFP_Common module change)
  ↳ No PR: [dd174a8](https://github.com/DPDK/dpdk/commit/dd174a89956c17c7a9f235c9fcc07fe0dfeaace0), [e90cda8](https://github.com/DPDK/dpdk/commit/e90cda8ca6783c45fc7e46025afb38698535ced1)
- Added feature arc registration mechanism and related API to the graph library, including node processing function coverage, feature arc initialization, creation, destruction and adding node functions. (Architecture event: NFP_Common module change)
  ↳ No PR: [4e3e889](https://github.com/DPDK/dpdk/commit/4e3e8897c0e9da9c40326573b98a1ec264216c8d), [2bd7189](https://github.com/DPDK/dpdk/commit/2bd71894e8e1deac3e63a32d93e1de9f97dced4b), [23e8ddc](https://github.com/DPDK/dpdk/commit/23e8ddcbc7e107d2c87cec5f259aa4a7bc240aee), [e3942de](https://github.com/DPDK/dpdk/commit/e3942de6c981e14a762185976a84cb02882699ed)
- Added a new PMU event reading library, which supports direct programming and reading of PMU counters at runtime without going through the kernel, suitable for CPU core isolation scenarios; also added runtime event reading support for ARM64 and Intel x86_64 platforms. (Architecture-related: New PMU library)
  ↳ No PR: [960c431](https://github.com/DPDK/dpdk/commit/960c43184c4d82c4ab3b5c9d465d48526c7bc39b), [a8926a6](https://github.com/DPDK/dpdk/commit/a8926a65ad1d329dbf54e8c34eb14cf87021f81d), [1e648ee](https://github.com/DPDK/dpdk/commit/1e648eee69c427a6b04a424b3d2f8ce27d9b15d0)
- Extended rte_str_to_size function to support larger storage units (E, P, T), and added rte_size_to_str function to format uint64_t values into human-readable size strings. (Architecture-related: public API)
  ↳ No PR: [6655090](https://github.com/DPDK/dpdk/commit/66550907585be88e057d5c5fe2b97e56a0e297c0), [62faf2d](https://github.com/DPDK/dpdk/commit/62faf2d485be2e59cbe42d699c9083d047de9a5f)
- Added standard PCI register offset definitions in rte_pci.h, including subsystem ID, revision ID, device status, etc., and updated corresponding read calls in multiple drivers. (Architecture-related: public API)
  ↳ No PR: [5660270](https://github.com/DPDK/dpdk/commit/5660270be181acf7832ac53c6fa3ddcef314c60d)
- Import VDUSE header files from v6.14 kernel for Vhost library. (Architecture-related: public API)
  ↳ No PR: [ddd8f09](https://github.com/DPDK/dpdk/commit/ddd8f09090b4a0d3953a2c833b4a41ea84bfe566)
- Add getline and getdelim function implementations for Windows platform to support POSIX compatibility. (Architecture-related: Platform compatibility)
  ↳ No PR: [ce30185](https://github.com/DPDK/dpdk/commit/ce30185678119f73cdfddb3cd9493c540c90bd4f)
- Add complete device operations, statistics, queue pair configuration, session configuration, enqueuing/dequeuing data paths and capabilities support for zsda encryption devices. (Architecture-related: public API)
  ↳ No PR: [ae428b2](https://github.com/DPDK/dpdk/commit/ae428b2dddd21d45ecf2f58c466fb8e5a645cf3c), [815dd13](https://github.com/DPDK/dpdk/commit/815dd1347eb538ce962e23fd135f35002f82a914), [81107c0](https://github.com/DPDK/dpdk/commit/81107c07d99a5fcd1233416d83ae0048984782fe), [6df9a1c](https://github.com/DPDK/dpdk/commit/6df9a1c3015bd0f936828f0469dad7ff901c23f1), [6677c38](https://github.com/DPDK/dpdk/commit/6677c38fcc32fb449fabad4d08b47b94a83153ea), [ea54160](https://github.com/DPDK/dpdk/commit/ea54160b7635a6ff08e526be45672a8453493542), [9f21778](https://github.com/DPDK/dpdk/commit/9f217781b75194d12ce754e20b0ede96e9eb733a), [c9d6249](https://github.com/DPDK/dpdk/commit/c9d6249eae88740aca3b2630941e3b7186efa6de)
- Merge -l option with --lcores, and export rte_vect_set_max_simd_bitwidth symbol. (Architecture-related: public API)
  ↳ No PR: [1ea3833](https://github.com/DPDK/dpdk/commit/1ea3833e9c4e06cf6693bf6aba3bec545f620e83)
- Add RSS support based on RoCEv2 header for cnxk device, add stream key type and expand RSS offloading capability. (Architecture-related: RSS extension)
  ↳ No PR: [5b832e5](https://github.com/DPDK/dpdk/commit/5b832e5b10a64c05dc9347c71c1ce93f80332db1)
- Move the constant definitions in the FIB library to the header file, and export the rte_fib6_create and rte_fib6_find_existing functions. (Architecture-related: public API)
  ↳ No PR: [66418ef](https://github.com/DPDK/dpdk/commit/66418ef9deb76cb59852e6431da9697403125070)
- Added IPv4 to find FIB nodes, and provided rte_node_ip4_fib_route_add route to add public functions. (Architecture-related: public API)
  ↳ No PR: [6dd7e48](https://github.com/DPDK/dpdk/commit/6dd7e487548657e6bf6657ca9326f43d36f3e7f8), [edbba07](https://github.com/DPDK/dpdk/commit/edbba07ff344971d86c9c0028022aa51dd1c9faa)
- Added IPv4 and IPv6 search mode commands to support switching between LPM and FIB modes, and update routing table logic. (Architecture-related: public API)
  ↳ No PR: [197b9fc](https://github.com/DPDK/dpdk/commit/197b9fcf92d98582da89f29f70a6911370f2e5a4), [abc2e28](https://github.com/DPDK/dpdk/commit/abc2e2848debcd5abfaf111504d51ee0ef65a995)
- Added RSS function based on RoCE v2 header, including corresponding RSS type macros and test command options. (Architecture-related: public API)
  ↳ No PR: [f7527ba](https://github.com/DPDK/dpdk/commit/f7527ba9b93411bcd13273cf49a44ea8460e6608)
- Added feature arc support for the graph library, including IPv4 output direction feature arc and sample programs. (Architecture-related: public API)
  ↳ No PR: [977b265](https://github.com/DPDK/dpdk/commit/977b265712cd1e04554e76ea29aab29bc85bda4c), [e52b97c](https://github.com/DPDK/dpdk/commit/e52b97c10fbdb3d46196c6c965341f899aecb982), [08cea83](https://github.com/DPDK/dpdk/commit/08cea83f058708e005414703fff16006162b6bfb)
- Improved the delay statistics library, added sample number indicators and optimized log and API export. (Architecture-related: API export)
  ↳ No PR: [934731c](https://github.com/DPDK/dpdk/commit/934731cc7c8077cced4b3871ca86c3a4332ba692), [d195a37](https://github.com/DPDK/dpdk/commit/d195a37479faf697aba5a5b650dd9ac4cd687f8c), [b34508b](https://github.com/DPDK/dpdk/commit/b34508b9cbcdf0dc7e1fccb0e107bfcbb4d1aa26)
- Added the function of switching VF sending queue to ixgbe driver to avoid hardware defects. (Architecture-related: public API)
  ↳ No PR: [ffa64e2](https://github.com/DPDK/dpdk/commit/ffa64e2fc083d6b468128310da2c2b95f8891158)
- Added string and boolean parameter type parsing support for the argparse library. (Architecture-related: public API)
  ↳ No PR: [410cc61](https://github.com/DPDK/dpdk/commit/410cc61594ef2a03c030eaec57b840fcd9df8002)
- Added 5-tuple stream filtering support for the txgbe network card VF driver. (Architecture-related: public API)
  ↳ No PR: [065d647](https://github.com/DPDK/dpdk/commit/065d64788cdca2983174771ee58f972e9c05827f)
- Added IPv4/IPv6 SCTP protocol RSS offload support for the txgbe network card driver. (Architecture-related: public API)
  ↳ No PR: [f92f525](https://github.com/DPDK/dpdk/commit/f92f5258237e66cff16f9b4ea97e39434032ffed)
- Added IPv4/IPv6 SCTP protocol RSS offload support for ngbe network card driver. (Architecture-related: public API)
  ↳ No PR: [0542ae6](https://github.com/DPDK/dpdk/commit/0542ae698abb14f8cfa45077aa9bb1e60cf33720)
- Added global mbuf dynamic field support to the node library, and provided an API for registering and obtaining dynamic fields. (Architecture-related: public API)
  ↳ No PR: [746e873](https://github.com/DPDK/dpdk/commit/746e8736da70f49aa91a777446c62193c127aa2a)
- Synchronized the ethtool link mode to Linux 6.15, adding 200G, 400G, 800G and other rate modes. (Architecture-related: platform compatibility)
  ↳ No PR: [5159400](https://github.com/DPDK/dpdk/commit/5159400fd918dcecbe6fa0dc3b145990f62027f6)
- Fixed the error log and delay issues caused by the non-existence of the VFIO directory in container non-privileged mode. (Architecture-related: platform compatibility)
  ↳ No PR: [2c472f5](https://github.com/DPDK/dpdk/commit/2c472f55f2735cc696c9e72de36b8c5b9b95e2d6)
- Added extern "C" protection to the cryptodev header file to ensure that exported global variables can be used normally in C++ code. (Architecture-related: public API)
  ↳ No PR: [4934953](https://github.com/DPDK/dpdk/commit/4934953c8850711b5e99dc3cd1a521cb5dd27518)
- Fixed the checking logic of IPv4 compatible addresses and mapped addresses, corrected the prefix comparison length from 32 bits to 96 bits, and added corresponding unit tests. (Architecture-related: public API)
  ↳ No PR: [bd221be](https://github.com/DPDK/dpdk/commit/bd221bea7080a0c7d18daef4d47924bb59e71664)
- Fixed the possible null pointer dereference problem in the rte_pcapng_close function, and added the symbol export of the function. (Architecture-related: public API)
  ↳ No PR: [b24a634](https://github.com/DPDK/dpdk/commit/b24a6349ae1d56b947186c9545349fca1ca87614)
- Removed variable-length arrays in the RCU library that are not compatible with MSVC and use alloca as a temporary solution. (Architecture-related: platform compatibility)
  ↳ No PR: [117e86c](https://github.com/DPDK/dpdk/commit/117e86c4b96ed761e9a7ab766261208fe81bf5ca)
- Fixed the problem of mmap failure leading to an infinite loop when the process address space is insufficient. Stop retrying when the request size cannot be reduced. (Architecture-related: Core module: Memory allocation behavior)
  ↳ No PR: [6643d1c](https://github.com/DPDK/dpdk/commit/6643d1cad3b8a90a0e5ec4a4afa0d9f61dc5b34e)
- Fixed issue with netvsc driver using system page size instead of Hyper-V page size, ensuring RNDIS implementation and PFN calculation communicate correctly with Hyper-V VSP. (Architecture-related: Platform compatibility)
  ↳ No PR: [2e81551](https://github.com/DPDK/dpdk/commit/2e81551053fcfc7d57b8907a2a8720805298d723)
- Fixed an overflow issue in the per-core trace buffer, now aligning offsets before checking if there is enough space to write. (Architecture-related: public API)
  ↳ No PR: [3c440cd](https://github.com/DPDK/dpdk/commit/3c440cdfe87a2925af1be023e66bdf0bffc423a4)
- Removed the unsupported METER flow action in MLX5 HWS mode, the application should use the METER_MARK action instead; also fixed the HWS large flow mode error notification to ensure that the E2BIG error value is correctly passed in the flow error notification. (Architecture-related: behavior change)
  ↳ No PR: [645f240](https://github.com/DPDK/dpdk/commit/645f240d1cd57d0be1b773c739a5845a7663eeed), [3bd9536](https://github.com/DPDK/dpdk/commit/3bd95360ac6d2dd761c1af07882d21d34d326ce0)
- Fixed the issue where the driver may skip the disabling operation due to early reset of variables when disabling promiscuous mode and full multicast; also added symbol exports for rte_eth_allmulticast_disable and rte_eth_allmulticast_get. (Architecture-related: public API)
  ↳ No PR: [00add16](https://github.com/DPDK/dpdk/commit/00add16978762a8bcd98cd9465503194dc4c1e9a)
- In the cnxk crypto driver, added a check for the maximum gather entries for outbound and inbound SA processing and TLS read operations, returning an error when the number of segments exceeds the limit. (Architecture-related: public API)
  ↳ No PR: [13868cc](https://github.com/DPDK/dpdk/commit/13868cc0de7ce464ab0de113bdcc5e62e595c077)
- To support the Y2038 issue, the time_t type alias definition based on the _TIME_BITS macro has been added to the trace metadata, and the problem of compilation failure on 32-bit systems has been fixed. (Architecture-related: platform compatibility)
  ↳ No PR: [10f457a](https://github.com/DPDK/dpdk/commit/10f457ac0fc2e660036467f39ac3ec149c577c07)
- Fixed the CQ tail drop function to enable it correctly when inline IPsec is disabled, and added control options for forcing tail drop and disabling XQE drop. (Architecture-related: public API)
  ↳ No PR: [dc8f10b](https://github.com/DPDK/dpdk/commit/dc8f10bb36bbd9dd961e4baba693181add66c962)
- Fixed the problem that the rte_flow_configure function did not fill in the wrong structure on the wrong path and caused a crash. (Architecture-related: public API)
  ↳ No PR: [af7ac22](https://github.com/DPDK/dpdk/commit/af7ac22d8da82398065d5f3c799c17a7cec3a6af)
- Fixed the protocol type conversion error in GTP packet parsing, ensuring that the GTP protocol type is correctly converted to the Ethernet protocol type to support subsequent parsing; at the same time, the tunnel length field was added to the UDP tunnel parsing, and the judgment logic of the GTP message protocol type was fixed, and the rte_net_skip_ip6_ext symbol was exported. (Architecture-related: public API)
  ↳ No PR: [b1f3a7a](https://github.com/DPDK/dpdk/commit/b1f3a7a8c375fbb66be48aed078222686d16fdb5), [a585404](https://github.com/DPDK/dpdk/commit/a5854045c38865c44459446565dc749aa29dffba)
- The argparse library has added support for the -- parameter to terminate parsing, and instead returns the number of actual parsed parameters to be compatible with EAL parameter behavior. (Architecture-related: public API)
  ↳ No PR: [8ddf631](https://github.com/DPDK/dpdk/commit/8ddf63106fa573d3d1315a6d10d2b1bfbbfb9832)
- Fixed the problem of unhandled negative values returned by sysconf(_SC_PAGESIZE), updated rte_mem_page_size() to add error checking, and replaced all library functions that directly call sysconf(_SC_PAGESIZE) with calls to rte_mem_page_size(). (Architecture-related: public API)
  ↳ No PR: [1c0bad3](https://github.com/DPDK/dpdk/commit/1c0bad37a7b2aa8770bbe6045d1da5ecc2344237)
- Fixed a C++ compilation error caused by the lack of closing braces in extern "C" in rte_atomic.h and rte_byteorder.h when using RTE_FORCE_INTRINSICS on the x86 platform. (Architecture-related: public API)
  ↳ No PR: [2c6f1f0](https://github.com/DPDK/dpdk/commit/2c6f1f0a847898732c18c8b37821850f1b48aa9d)
- Change the eventdev related flag macro from a 64-bit constant to a 32-bit bit operation macro to make it consistent with the corresponding structure field type. (Architecture-related: public API)
  ↳ No PR: [3734cf2](https://github.com/DPDK/dpdk/commit/3734cf22abf8c467d093dcdc83a025ce1aa186db)
- Fixed C++ compatibility issues, avoiding compilation errors caused by zero-size unions through conditional compilation. (Architecture-related: platform compatibility)
  ↳ No PR: [bd54677](https://github.com/DPDK/dpdk/commit/bd546772e1449ccc0789db338cc398815fa2636d)
- Fixed the return value of rte_lcore_has_role() for invalid lcore ID, now returns false. (Architecture-related: public API)
  ↳ No PR: [65e03bc](https://github.com/DPDK/dpdk/commit/65e03bc2f35109cb33ad4a6e244d5ea90e78fcde)
- Remove unimplemented function declarations and clean up exported symbols. (Architecture-related: public API)
  ↳ No PR: [8947464](https://github.com/DPDK/dpdk/commit/8947464e93a1f1a8b532f3a90f84bf33cf7fdc14), [ee96e01](https://github.com/DPDK/dpdk/commit/ee96e014c49be33df8687c761a24a3a007463627)
- Simplify the x86 platform CRC processor build logic: replace the conditional compilation macros of the SSE42 path with architectural macros, and simplify the build-time check of the AVX512 path. (Architecture-related: Platform compatibility)
  ↳ No PR: [98d04bc](https://github.com/DPDK/dpdk/commit/98d04bcc1d90cf336531f8cb417e0e3142726b48)
- Remove the global node ID counter, dynamically allocate free IDs instead, and ensure that the node list is sorted by increasing ID. (Architecture-related: public API)
  ↳ No PR: [537171f](https://github.com/DPDK/dpdk/commit/537171f631c23ab2554e485fb8ea372776e9aa09)
- Change the argparse parameter attribute from a bitmask macro to an enumeration, indicating whether the parameter has a value, the value type and additional flags, and update the relevant verification logic and test cases. (Architecture-related: public API)
  ↳ No PR: [04acc21](https://github.com/DPDK/dpdk/commit/04acc21beeeb78477b15a3f497d3628fd70a6a9f)
- Mark the parameter structure of argparse as const to ensure that the library will no longer modify the parameters passed in by the user. (Architecture-related: public API)
  ↳ No PR: [98ae295](https://github.com/DPDK/dpdk/commit/98ae2959d47068f335d56ef60f56725e5fd978e9)
- Use shared mbuf dynamic fields in ip4/ip6 lookup and rewrite nodes instead, and remove the old private field access functions. (Architecture-related: public API)
  ↳ No PR: [89c425b](https://github.com/DPDK/dpdk/commit/89c425bbff6157649497348a6df98bd4adae59ee)
- Deprecated coremask-based EAL parameters: Add a deprecation warning in the function that parses coremask, and export related internal symbols; also update the documentation, use core list (-l) instead of core mask (-c) in the application and example guide, and use service core list (-S) instead of service core mask (-s). (Architecture-related: public API (deprecated)
  ↳ No PR: [ce5a6fa](https://github.com/DPDK/dpdk/commit/ce5a6fa0cef0471eac9ca2b17358a2daaf5cf7e3), [bc085f5](https://github.com/DPDK/dpdk/commit/bc085f55a919e2f3d7fb60c43818b9b60e1b9010)
- Optimize the graph search logic in mcore dispatch: avoid repeated slow traversal by caching the first search results, and export related function symbols to improve performance. (Architecture-related: public API)
  ↳ No PR: [fbecf79](https://github.com/DPDK/dpdk/commit/fbecf790b603cccac6eeda4536cba3e043ade209)
- Fixed the potential problem of not checking the rte_socket_id_by_idx return value in the malloc_get_numa_socket function, and added invalid socket ID verification. (Architecture-related: core module: memory allocation verification)
  ↳ No PR: [2aabc7a](https://github.com/DPDK/dpdk/commit/2aabc7a0c879a876b20364aa989505ee61551165)
- Added the safe memory clearing function rte_memzero_explicit and the safe release function rte_free_sensitive, and replaced the key clearing operation in the QAT encryption driver to prevent compiler optimization from causing sensitive data to remain; at the same time, Coccinelle script-assisted migration is provided. (Architecture-related: public API)
  ↳ No PR: [4752753](https://github.com/DPDK/dpdk/commit/47527539d35664be765c996598034ce9b4e1962b), [bd91f4f](https://github.com/DPDK/dpdk/commit/bd91f4f0a044e5e0aa1c297f9b15f565dc0e69ce), [6178ca7](https://github.com/DPDK/dpdk/commit/6178ca7b8d6c9b4824cd6e3b3da321e0c5472b5b), [c22fffd](https://github.com/DPDK/dpdk/commit/c22fffd552c66a5669ba4f19ac1bc044bf32952f)
- Updated the documentation of socket ID-related APIs in EAL, correcting "physical socket" to "NUMA node" to match the actual semantics; at the same time, the socket ID fields in the internal lcore and configuration structures have been renamed to NUMA ID, and the user API is not affected. (Architecture-related: public API)
  ↳ No PR: [45b04d8](https://github.com/DPDK/dpdk/commit/45b04d8694dd0d911e8905ba2f85081593847dfa), [0160e6e](https://github.com/DPDK/dpdk/commit/0160e6eb9703a4546da38fcc0c926e6c3db5935b), [2eeb019](https://github.com/DPDK/dpdk/commit/2eeb0195be9923cef2f568830b24de0b8f3507cd)
- Announced in deprecation.rst that SSE vector paths for i40e, iavf and ice drivers will be removed in DPDK 25.11. (Architecture-related: SSE vector paths deprecated)
  ↳ No PR: [2163ffe](https://github.com/DPDK/dpdk/commit/2163ffe7e78f58a38bc775ff3c701a5a678dfc03)
- Updated Linux guide, removed old pkg-config instructions and updated Fedora development tools installation commands. (Architecture-related: platform compatibility)
  ↳ No PR: [e57c04f](https://github.com/DPDK/dpdk/commit/e57c04f2405a69b5f257582c0b9b198764b4d428), [03bd758](https://github.com/DPDK/dpdk/commit/03bd75890c10a331c9dcae4ec050d4a1944a775a)
- Add build instructions for new Arm SoCs and explain build configuration changes. (Architecture-related: Platform compatibility)
  ↳ No PR: [4e73756](https://github.com/DPDK/dpdk/commit/4e7375612995f9183dd6df545de9ceaedb27522a)
- Use the imported VDUSE uAPI header file, remove the build dependency on the system VDUSE header file, and simplify function declaration. (Architecture event: NFP_Common module adds VDUSE uAPI header file)
  ↳ No PR: [67b79f6](https://github.com/DPDK/dpdk/commit/67b79f6314ae11a0b3795ee89cf5feddb850fc8b)
- The build system has a new symbol mapping generation function, which automatically generates the mapping files required by the linker by marking RTE_EXPORT_*SYMBOL. (Architecture-related: build and installation methods)
  ↳ No PR: [1a0c104](https://github.com/DPDK/dpdk/commit/1a0c104a7fa939a84d4e91fbccc6fcd073dfde88)
- Enable FIB application on Windows, remove unnecessary header files and add rte_os_shim.h to be compatible with strtok_r function. (Architecture-related: platform compatibility)
  ↳ No PR: [89055db](https://github.com/DPDK/dpdk/commit/89055db85c5d4169087bfbe0ed0bc3e501c48caf)
- Enable the compilation of the mbuf library under the MSVC compiler, and adjust the net library compilation options to enhance compatibility. (Architecture-related: platform compatibility)
  ↳ No PR: [b6ae9ae](https://github.com/DPDK/dpdk/commit/b6ae9ae120ed3a3664289003bcd0af436faf0f84)
- Removed the build disabling condition for the LPM library in the MSVC compiler, so that it now supports compilation using the Visual Studio toolset. (Architecture-related: Platform compatibility)
  ↳ No PR: [2970bb0](https://github.com/DPDK/dpdk/commit/2970bb0235dbfc79b7d2dabdea791cf988304784)
- Enable build support for the fib library in the MSVC compilation environment. (Architecture-related: platform compatibility)
  ↳ No PR: [8d3f096](https://github.com/DPDK/dpdk/commit/8d3f096d835d0687be7248df706ce5481101af00)
- Enable gve driver to support building on FreeBSD host operating system, remove Linux environment conditions and add FreeBSD kernel module dependency. (Architecture-related: platform compatibility)
  ↳ No PR: [cb44edb](https://github.com/DPDK/dpdk/commit/cb44edb2f45005eb150997f2f98e7e6faa8dc768)
- Replaced GCC built-in atomic operations in the LPM library with the standard C11 atomic API. (Architecture-related: Platform compatibility)
  ↳ No PR: [99139e9](https://github.com/DPDK/dpdk/commit/99139e9e1c5d4f4bc3c18a47886c84e9f0ee1119)
- Replace __builtin_ffsl in the mlx5 driver with rte_ffs32 provided by EAL to support MSVC compilation. (Architecture-related: platform compatibility)
  ↳ No PR: [79419f5](https://github.com/DPDK/dpdk/commit/79419f502c2f2fd8812580f72b1ac3c2fdb51476)

### User-Space Applications
- Added flow template matching support for IPv6 fragmentation extension headers to the mlx5 driver, supporting matching next_header field. (Architecture-related: flow template matching)
  ↳ No PR: [6aceb4e](https://github.com/DPDK/dpdk/commit/6aceb4e7f86537e0af5b6334834fb81fabc6e0b7)
- Added enqueue paths for CN20K encrypted devices, including lmtst double commit routine and IPsec/TLS secure session command filling. (Architecture-related: public API)
  ↳ No PR: [004cf70](https://github.com/DPDK/dpdk/commit/004cf704afa28dd75cd11b51b78a483de4e75ed8), [e3ad89b](https://github.com/DPDK/dpdk/commit/e3ad89b161d32c1d37d9e57f783e0bd277b06eb7)
- Added SAMPLE action support to mlx5 non-template stream API. (Architecture-related: public API)
  ↳ No PR: [d986f04](https://github.com/DPDK/dpdk/commit/d986f04d65291f6d069183c3485d262dfd5b0b93), [68dbd95](https://github.com/DPDK/dpdk/commit/68dbd957ddb0dc7b5c2945a6f984185f99a6f2f6)
- Added an independent mirror creation function, splitting the HWS mirror function into two steps: mirror action creation and indirect list handle creation. (Architecture-related: public API)
  ↳ No PR: [ac3f43b](https://github.com/DPDK/dpdk/commit/ac3f43b54066620e252850fc4d2b9345e3382465)
- Fixed an error caused by non-static constant initialization when compiling MSVC, replacing static arrays within functions with macro calls. (Architecture-related: platform compatibility)
  ↳ No PR: [c439a84](https://github.com/DPDK/dpdk/commit/c439a84f1a78652b0ed7a471e393ca942628242b)
- Removed static link checks for older versions of pkg-config from the example Makefile. (Architecture-related: pkg-config configuration)
  ↳ No PR: [ecd0dc1](https://github.com/DPDK/dpdk/commit/ecd0dc1d1864e15d103dcdb095fe74adebc1fcfe)

### Cross-cutting / Other Architecture-related Changes
- Adjusted the head space of the buffer layout in the dpaa2 driver to provide enough head space for IPSec and TX dynamic confirmation functions. (Architecture-related: cross-module behavior)
  ↳ No PR: [a8faa0f](https://github.com/DPDK/dpdk/commit/a8faa0fdd117570168c6da2ce5ec6a8e9748701d)
- Rolled back the automatic port attach/detach function, restored the manual port management method, and fixed the compatibility issue with auxiliary processes such as pdump. (Architecture-related: External behavior: Port management method)
  ↳ No PR: [40ef05a](https://github.com/DPDK/dpdk/commit/40ef05a0f6072e40899c8676a2b079df5874d8d3)
- Updated Linux kernel version requirements to 5.4, and removed the guarantee for specific distributions. (Architecture-related: platform compatibility)
  ↳ No PR: [3795e96](https://github.com/DPDK/dpdk/commit/3795e96fc862e2b65aa8951f6661420510c87328)
- Updated the recommended compiler version in the Linux guide to recommend GCC 8.0+ and Clang 7+. (Architecture-related: Compiler version requirements)
  ↳ No PR: [3798ee9](https://github.com/DPDK/dpdk/commit/3798ee96658697f4e7a53099a470495656ed9e44)
- Announced in deprecation.rst that due to unaligned access detected by UBSan, it is planned to update the alignment of some structures in version 25.11, involving rte_stack_lf_head and rte_mp_msg, etc., which are ABI violations. (Architecture-related: ABI compatibility)
  ↳ No PR: [71405d0](https://github.com/DPDK/dpdk/commit/71405d01c198e70ec0aa679e3313f765db7c4dc9)
- Added a list of Intel platforms tested with NVIDIA network cards in the 25.07 release notes. (Architecture-related: Platform compatibility)
  ↳ No PR: [2d58cc6](https://github.com/DPDK/dpdk/commit/2d58cc6287b1993a6fad3db7045c45dcc4155341)
- Version mapping was changed to dynamic generation, scripts and checks related to static version mapping were removed, and build configuration and documentation were updated. (Architecture-related: version and compatibility)
  ↳ No PR: [57c194d](https://github.com/DPDK/dpdk/commit/57c194d142d927f2f5dd757e36777910b5d77d41)
- Start a new release cycle, update the version number to 25.07-rc0, and add an empty release note document. (Architecture-related: version and compatibility)
  ↳ No PR: [370effa](https://github.com/DPDK/dpdk/commit/370effa531728426d7d2ae3ed1bbcb179a2e742c)
- Allow building the app directory under the MSVC compiler, and removed the -Wno-deprecated-declarations compilation flag that is no longer needed. (Architecture-related: platform compatibility)
  ↳ No PR: [ca1690e](https://github.com/DPDK/dpdk/commit/ca1690ebd224f148268285b15b97441ccdbdd07e)
- Added license exception for Linux kernel uAPI header files, and updated SPDX tag checking script to support dual license files. (Architecture-related: public API license)
  ↳ No PR: [d0cdc01](https://github.com/DPDK/dpdk/commit/d0cdc016fb745e5b432d7771fd6484b2e255c1c4)
- Removed Windows build restrictions so that the regexdev library and its test applications can be compiled under MSVC. (Architecture-related: platform compatibility)
  ↳ No PR: [85dfd6b](https://github.com/DPDK/dpdk/commit/85dfd6be3db6f3458066af937bb1970d3de72e4d)
- Added a new script to automatically obtain the minimum Meson version defined in meson.build and use this version during the CI and build process, while updating the minimum Meson version requirement from 0.57 to 0.57.2. (Architecture-related: build requirements)
  ↳ No PR: [9622222](https://github.com/DPDK/dpdk/commit/9622222ea710c4f57f04ea0dc6e640152f87bfc4)
- Updated the Arm Neoverse N3 build configuration to use mcpu to adapt to the latest GCC, and added the platform to the support list. (Architecture-related: Platform compatibility)
  ↳ No PR: [19b0b47](https://github.com/DPDK/dpdk/commit/19b0b47032858f1aebbd9f4e368a2d8d75f0043a)
- Added build configuration support for Arm Neoverse V3. (Architecture-related: Platform compatibility)
  ↳ No PR: [a633a12](https://github.com/DPDK/dpdk/commit/a633a128fd09ff1fc72312f4e4d1a9e0f73aa359)
- In the MSVC compiler environment, the build tool uses lib.exe instead of ar to handle archiving operations. (Architecture-related: build and installation methods)
  ↳ No PR: [b1b329e](https://github.com/DPDK/dpdk/commit/b1b329e6027045de6eced45d41727c5be7308afe)
- Optimized the build configuration. When the target already supports AVX2 or AVX-512 instruction set, the corresponding compiler flags are no longer added repeatedly, and the processing logic of AVX512 compilation flags is simplified. (Architecture-related: build and installation methods)
  ↳ No PR: [e361ae3](https://github.com/DPDK/dpdk/commit/e361ae3f59d3350c83ec3184198218b199d2673d)
- A check for the Python elftools module has been added to the build configuration. If it is missing, an error will be reported directly to terminate the configuration to avoid errors in subsequent builds. (Architecture-related: build dependencies)
  ↳ No PR: [60e3a27](https://github.com/DPDK/dpdk/commit/60e3a270a9edb1d60393d384bd85104898eb43ac)
- Fixed an issue where old compilers (such as GCC 8.5) could not correctly override -march=native, by detecting and explicitly adding the AVX512 compilation flag to avoid build warnings. (Architecture-related: Platform compatibility)
  ↳ No PR: [70c2297](https://github.com/DPDK/dpdk/commit/70c2297528e7c7789af452f78de1932e9a20c8a2)
- Added general support for basic code building of multiple drivers, and migrated related drivers. (Architecture-related: build and installation methods)
  ↳ No PR: [8fa3af6](https://github.com/DPDK/dpdk/commit/8fa3af6c05f821a7242711dc3e7c58f17ee36470), [a87dbe9](https://github.com/DPDK/dpdk/commit/a87dbe9ef21d5d07848c494401fed6bbcb8dd323), [f981fb3](https://github.com/DPDK/dpdk/commit/f981fb3afae013661973967c8682786ee0bf5db4), [c5ad6d1](https://github.com/DPDK/dpdk/commit/c5ad6d18269bff9697fd2048e6a144f0f289b96f), [6090d93](https://github.com/DPDK/dpdk/commit/6090d937d4e385344464b101fe9caf0d8ef1313a), [e550c76](https://github.com/DPDK/dpdk/commit/e550c763383e68a80d8b040029c47ac6c716c1d6), [bf4544f](https://github.com/DPDK/dpdk/commit/bf4544fdd7895cfb6528ecf94b6642530e51e009), [75f179e](https://github.com/DPDK/dpdk/commit/75f179ebe347b6098cf3af26d3d3b7168fe3fe24)
- Updated the recommended DPDK and MEV-ts version matching list in the cpfl and idpf driver documentation. (Architecture-related: platform compatibility)
  ↳ No PR: [db039e0](https://github.com/DPDK/dpdk/commit/db039e0e48fd0e4a850ba6b30560617980a0a2a3)

## Routine Changes

### New features
- Added multiple functions to the zxdh network processor driver: register read and write interface, software and firmware compatibility check, agent channel, DTB queue configuration, eram table read, write and delete, flow table resource acquisition, hash resource configuration and table operation, ACL table entry operation, and added related initialization functions.
  ↳ No PR: [dd09028](https://github.com/DPDK/dpdk/commit/dd0902871899517dc7b036425162892e00713bd8), [fb7515f](https://github.com/DPDK/dpdk/commit/fb7515fb19c0b93f86d3385c15aed36b57816a39), [3ed530a](https://github.com/DPDK/dpdk/commit/3ed530ae67fffa736982ef28ae62529c541e0a10), [43949b2](https://github.com/DPDK/dpdk/commit/43949b2f0bda3f275bf67d591c82b9184a57ebf1), [5c3bd01](https://github.com/DPDK/dpdk/commit/5c3bd01393b40e94fdecfe7c1ba69dcc3650de8c), [5228939](https://github.com/DPDK/dpdk/commit/52289399dfeddcd83a4d8bbd5eb875e2209e5e77), [9d52dd6](https://github.com/DPDK/dpdk/commit/9d52dd606c5cbd60b3358a9a4529efb1c5e20fce), [8a02065](https://github.com/DPDK/dpdk/commit/8a02065f3c5e2c912b7ffba89b759e541ea48f51), [f5bf429](https://github.com/DPDK/dpdk/commit/f5bf4297ad11b56b5c1034b6bf5f7caab0a3e3eb), [9971b84](https://github.com/DPDK/dpdk/commit/9971b844c62d6d8084ad8932ce2088628895eb46), [f3f8ef2](https://github.com/DPDK/dpdk/commit/f3f8ef21f92b1504e4cbd243b1b90a2ce63d0a88), [05d0502](https://github.com/DPDK/dpdk/commit/05d05024bc79978272e098f7e5fc72dda808c00e)
- Add basic PMD library and document building infrastructure for rnp network card driver, and update maintainer files.
  ↳ No PR: [18a9d90](https://github.com/DPDK/dpdk/commit/18a9d90cc2d95749f1aa010942dcec7629d33e4c)
- Add log macros and log type registration for rnp driver, support debugging and tracking log output.
  ↳ No PR: [0db0434](https://github.com/DPDK/dpdk/commit/0db043444e9d3bbd6cbc33fc824e2b160b5cbedb)
- Added unicast MAC address filtering function to RNP network card driver, supporting MAC address setting and clearing in single-port and multi-port modes.
  ↳ No PR: [e936f0d](https://github.com/DPDK/dpdk/commit/e936f0d300cc8af3152775d192659219ddbb2229)
- Added supported hardware packet type parsing function to rnp network card driver, and registered MAC address filtering operation.
  ↳ No PR: [8b46ce1](https://github.com/DPDK/dpdk/commit/8b46ce194f75283947bcd58a64f90d19ae3ba741)
- Added checksum offload support for L3/L4 in the receiving direction and L3/L4 in the tunnel inner layer for the rnp network card driver.
  ↳ No PR: [7a1fc07](https://github.com/DPDK/dpdk/commit/7a1fc07c7a057703ad55c0d87211ce46be715dea)
- Added Tx TSO offload support to the rnp network card driver, including support for VXLAN and GRE tunnel TSO.
  ↳ No PR: [4530e70](https://github.com/DPDK/dpdk/commit/4530e70f1e323bc2c7bf258fa161d05c5d904c7d)
- Added VLAN offload support to the rnp network card driver, including receive VLAN stripping and filtering, sending VLAN and QinQ insertion functions.
  ↳ No PR: [e461237](https://github.com/DPDK/dpdk/commit/e461237b9c92a833010b5b59007b5917d4b79bde)
- Add VLAN filter support to rnp network card driver, including VLAN ID update function.
  ↳ No PR: [81b8ac8](https://github.com/DPDK/dpdk/commit/81b8ac8224040b19c3d8598b70e696a1d2d2d4a2)
- Added multicast MAC filtering support to the RNP network driver, including single-port and multi-port MAC filtering functions.
  ↳ No PR: [5491ab2](https://github.com/DPDK/dpdk/commit/5491ab2801fc6112b3da7b32bc5c31e2de2f5e56)
- Added RSS hash support for ESP and RoCEv2 protocols to cnxk network device driver.
  ↳ No PR: [21d7811](https://github.com/DPDK/dpdk/commit/21d781117aaca78d25ab83ccc31810193fc1ded2)
- Added RSS algorithm configuration query function to the NFP network card driver, and restructured related functions to support the acquisition and setting of RSS hash types.
  ↳ No PR: [33ef193](https://github.com/DPDK/dpdk/commit/33ef193bc4d58ed12d844975d4fa1a5ad5caf2cd), [35cf220](https://github.com/DPDK/dpdk/commit/35cf2202cd4ae789c602ea75bd189b0e097359c8)
- Added RSS algorithm capability query function in the NFP network card driver, and called this query during the device information acquisition and initialization process, while adding log output of related capabilities.
  ↳ No PR: [85a0956](https://github.com/DPDK/dpdk/commit/85a095651a3c01ed42d81d94acfcc1de08455638)
- Added E31X series device support to the ZXDH network card driver, added the device IDs of E312S, E316, E310_RDMA and E312_RDMA, and extracted the PF judgment logic into an independent function.
  ↳ No PR: [a07ebbb](https://github.com/DPDK/dpdk/commit/a07ebbb726cfe69a2da8461abf432ac54aceb48d)
- Support gVNIC PCI revision 1 and higher, use full address settings to manage queues, and introduce a new device/driver reset mechanism.
  ↳ No PR: [76cb07a](https://github.com/DPDK/dpdk/commit/76cb07a6495421bedd30e247b7bc1632d724d2c9)
- Added Rx/Tx burst mode information acquisition function for e1000 network card driver, which can return the corresponding mode according to the selected burst function name.
  ↳ No PR: [b1da17e](https://github.com/DPDK/dpdk/commit/b1da17ebb56935bee6f0e618fc3d6aa41c5af78a)
- Added multiple port mode support for Medford4 network card, including 8-port mode, X4 port mode and extended port mode list.
  ↳ No PR: [e477f2b](https://github.com/DPDK/dpdk/commit/e477f2bf5c5f39b543704359dfe2b58c4aa9c225), [614555f](https://github.com/DPDK/dpdk/commit/614555f82bb5c9f6dc5a6f395ef7d9afda953014), [c610acf](https://github.com/DPDK/dpdk/commit/c610acfcb7390f3d6f5d312c67d03905bff060a4)
- Added the Rx/Tx burst mode information acquisition function to the virtio network card driver, and the new function returns the corresponding mode name based on the currently selected burst function.
  ↳ No PR: [9207857](https://github.com/DPDK/dpdk/commit/920785790d2fc92fc442629e5316a51035d79f80)
- Enabled ethertype filtering support for E610 network cards.
  ↳ No PR: [09766f4](https://github.com/DPDK/dpdk/commit/09766f41b320e68a27ef392af2f34ed5817bf5af)
- Added MAC operation, reconfiguration and PDU control functions for Medford4 network card.
  ↳ No PR: [8dac31d](https://github.com/DPDK/dpdk/commit/8dac31d073af8c762c0b5f539397102eb0c22e89), [aa4d79e](https://github.com/DPDK/dpdk/commit/aa4d79eccc65d0f4210a7ccde96b9d1b4c329129), [6c4c77a](https://github.com/DPDK/dpdk/commit/6c4c77a461c46a74bae5ca97aa71d01993d3a3a6)
- Added MAC statistics functions for Medford4 network cards, including clear, upload, update and periodic DMA updates.
  ↳ No PR: [f2f7745](https://github.com/DPDK/dpdk/commit/f2f77453cb9f16fed39c8232794ff5df4cb68692), [63536d6](https://github.com/DPDK/dpdk/commit/63536d6e9b05ea53e26f84a36ee0323235025622), [aea02dc](https://github.com/DPDK/dpdk/commit/aea02dc04104cb6bdd69b7cdb955c94afbbe103c)
- Added 200G link speed support to the sfc driver, including physical capability mapping, FEC capability query and link information reporting.
  ↳ No PR: [b526903](https://github.com/DPDK/dpdk/commit/b526903f308ed5a8bac5ec0878e74cfb1669122d)
- Added optional parameters prio-tc and keep-qnum to the DCB configuration command of testpmd, and supports disabling the DCB function.
  ↳ No PR: [601576a](https://github.com/DPDK/dpdk/commit/601576ae6699b31460f35816be54a63c34f54377), [2169699](https://github.com/DPDK/dpdk/commit/2169699b15fc4cf317108f86d5039a7e8055d024), [0ecbf93](https://github.com/DPDK/dpdk/commit/0ecbf93f50018e552ea3aa401129ef6075c1b36b)
- Enabled FEC auto-disable feature for E825C devices to support PHY FEC error log configuration.
  ↳ No PR: [10c54ac](https://github.com/DPDK/dpdk/commit/10c54ac3cdfc7b6162bf779aae929b3739860bfb)
- Moved mbuf timestamp dynamic fields and flags into the ice_rx_queue structure so that timestamp offloading functionality works properly in worker processes.
  ↳ No PR: [5fd1fa1](https://github.com/DPDK/dpdk/commit/5fd1fa141c290d84b32465eaa8ecd5ade7502e96)
- Added dequeue path support for CN20K encryption devices, covering dequeue post-processing, TLS MAC pruning and event metadata settings.
  ↳ No PR: [fcfc361](https://github.com/DPDK/dpdk/commit/fcfc361be16ede63c3c51590d4cfaf7755c9b2fb)
- Added support for asymmetric sessionless operation in CNXK CPT PMD.
  ↳ No PR: [e327a3b](https://github.com/DPDK/dpdk/commit/e327a3ba5a0e73f14f3cc12907e67e4d71987c5a)
- Added support for RTL8127 10GbE controller and refactored MAC MCU patch version checking.
  ↳ No PR: [1ab481a](https://github.com/DPDK/dpdk/commit/1ab481a98b59c1847fb97e003eed09da314cb1cf)
- Removed CMAC function for RTL8125AP network card and added IPC2 support.
  ↳ No PR: [98b566e](https://github.com/DPDK/dpdk/commit/98b566ee4bfca832631c8d342f4f602f3921a244)
- Added support for RTL8125CP network card chip.
  ↳ No PR: [53aba41](https://github.com/DPDK/dpdk/commit/53aba4103b059f0d0980018eaccb712c2c0bfdc3)
- Added serdes interface support for RTL8127ATF network card.
  ↳ No PR: [8d9c29c](https://github.com/DPDK/dpdk/commit/8d9c29c2de93683e082cd40a03ce6f20ebd9e389)
- Added IP-in-IP tunnel support for mlx5 driver.
  ↳ No PR: [f66c7c3](https://github.com/DPDK/dpdk/commit/f66c7c3ab983b56573b4f7ae82ac735079b5fa64), [4b70445](https://github.com/DPDK/dpdk/commit/4b7044562f591a674ac08624150ff5ced597b80f)
- Added a clock reading function to the ice driver, which can obtain the current system time (nanoseconds) for message scheduling based on sending time.
  ↳ No PR: [327fe14](https://github.com/DPDK/dpdk/commit/327fe144ca396f494b3ff9ee3b551e5e7d7b4d34)
- Added timestamp-based sending (Tx packet pacing) support for E830 network card.
  ↳ No PR: [0b6ff09](https://github.com/DPDK/dpdk/commit/0b6ff09a1f1978d91d131d2cedaf97c86033e61e)
- Support for cross-NUMA memory allocation in testpmd: allocate memory using arbitrary sockets when GRO is disabled or the --no-numa flag is set.
  ↳ No PR: [835fd48](https://github.com/DPDK/dpdk/commit/835fd4893a31229c311f17d1569794016247c6e7)
- The AF_XDP driver has added support for Rx/Tx queue configuration. When the device supports it, the rx/tx queue count will be used in preference to the combined queue configuration.
  ↳ No PR: [5933943](https://github.com/DPDK/dpdk/commit/5933943107d4dc5b5e99f77219f25486e675f0f5)
- Added stub implementation of PHY methods for Medford4 network card.
  ↳ No PR: [d65a712](https://github.com/DPDK/dpdk/commit/d65a7129c4132cb4bbb639547aa9ceb90fce4776)
- Added process callback functions for ip4_lookup_fib and ip6_lookup_fib nodes.
  ↳ No PR: [c33fc86](https://github.com/DPDK/dpdk/commit/c33fc864b1e5e54d5193a003716b7d1c97fc8ef4), [9ff4112](https://github.com/DPDK/dpdk/commit/9ff4112cc9af688b7e9019f1ef6389badf4a41e2)
- Added support for GRE protocol in encapsulated hash calculation for entropy calculation.
  ↳ No PR: [b310657](https://github.com/DPDK/dpdk/commit/b310657a48e5ed00c77b9d706962e62b53c533fb)
- Registered the fanout mode parameter of af_packet and printed configuration information during initialization.
  ↳ No PR: [3a096e5](https://github.com/DPDK/dpdk/commit/3a096e584df04e2e41c2ce382286162138b485af)
- Added support for NULL authentication and NULL encryption algorithm capabilities to the DPAA2_SEC encryption device.
  ↳ No PR: [ec2d921](https://github.com/DPDK/dpdk/commit/ec2d9213c3cf53de6c6f2157085de1ff4d7a8c60)
- Added support for simple IPsec FD in the DPAA2 SEC driver, and restructured related conversion functions.
  ↳ No PR: [b4fdb8d](https://github.com/DPDK/dpdk/commit/b4fdb8d46d0a488686cd29fba3d1100e6373c2a2)
- Added global CPT LF statistics functionality for lookaside IPsec.
  ↳ No PR: [52bd391](https://github.com/DPDK/dpdk/commit/52bd39138a3f67e0745b69504922171166f847f3)
- Added the function to obtain device information for CN20K encryption devices.
  ↳ No PR: [19a7e22](https://github.com/DPDK/dpdk/commit/19a7e22d1e556b5d35c4523c2c34e237b49e351d)
- Added DASH support for RTL8127AP network card chip.
  ↳ No PR: [44a0f5b](https://github.com/DPDK/dpdk/commit/44a0f5b4c7b210cb466239a7e3eea937df8f0768)
- Added support for sessionless asynchronous operations for CN20K.
  ↳ No PR: [9a56c0e](https://github.com/DPDK/dpdk/commit/9a56c0e3dda8fc889628ac6f5cb7f9d0367ef78a)

### bug fixes
- Removed support for ZUC-256 algorithm in QAT driver.
  ↳ No PR: [40d3c24](https://github.com/DPDK/dpdk/commit/40d3c24617673ccbb841c439d1f12aefdd9ef9c4)
- Fixed the memset size calculation issue of SHA3 hash in QAT driver to ensure correct zeroing.
  ↳ No PR: [9976348](https://github.com/DPDK/dpdk/commit/99763482361f08c77c9752985d7a7fd9adecd719)
- In the bus cleanup function, remove the device object from the device list when removing it to maintain programming standardization.
  ↳ No PR: [398bb77](https://github.com/DPDK/dpdk/commit/398bb775edc5434ad94578a5e6c49fa1328acc0f)
- Fixed the memory usage problem after release due to improper timing of calculating tx_bytes in the zero-copy sending path.
  ↳ No PR: [a23bf7f](https://github.com/DPDK/dpdk/commit/a23bf7fde78b10afbbafda252f15495b26e010a9)
- Reconstructed the AF_XDP zero-copy send path, extracted the common logic of descriptor retention and filling into inline functions, and fixed the send byte count position.
  ↳ No PR: [dd15874](https://github.com/DPDK/dpdk/commit/dd158749e87e52ef1f4baccc7fe4124d612e7b0d)
- Improved ASLR checking, adding detection of whether the current process has address randomization disabled through the setarch command to supplement sysfs file checking.
  ↳ No PR: [dcf9f93](https://github.com/DPDK/dpdk/commit/dcf9f9363aa9b4163d241caf8b26a84ca0c0006b)
- Fixed the order of cleanup operations when startup fails to avoid assertions caused by incorrect order.
  ↳ No PR: [66dced1](https://github.com/DPDK/dpdk/commit/66dced1537734f9ca0616a90f748140168e93868)
- Adjusted the IPv6 fragmentation extension header flag bits for CN20K devices to fit into the lower 4 bits of available space.
  ↳ No PR: [f42334b](https://github.com/DPDK/dpdk/commit/f42334b44415f2a9d56c9ccf79ff6e7e15acace3)
- Fixed buffer refill logic error for SDP output queue in octeon_ep driver.
  ↳ No PR: [fc3106f](https://github.com/DPDK/dpdk/commit/fc3106f82afb3adc885e4fe3d4a83214e900062f)
- Fixed a crash in the ipsec-secgw example caused by out-of-bounds access to the val_eth array when LPM lookup failed due to unconfigured IPv6 rules.
  ↳ No PR: [d03869e](https://github.com/DPDK/dpdk/commit/d03869e8e9c7c46bf7637d221ca6921516764109)
- Fixed the E610 device VF register selection error, and added the missing E610 VF branch in the RSS hash configuration related functions.
  ↳ No PR: [8364a0f](https://github.com/DPDK/dpdk/commit/8364a0f276ebc6ecb6dad1874ce0097966a74f09)
- Fixed the definition of IXGBE_LE32_TO_CPUS macro, removed unnecessary uintptr_t cast, and eliminated related compilation warnings.
  ↳ No PR: [3e7ea9a](https://github.com/DPDK/dpdk/commit/3e7ea9ad5162876583e72de6061752810bdde0fe)
- Fixed compilation warnings for unused parameters and unused variables by improving the macro definition and adding two lines of code.
  ↳ No PR: [ca361b5](https://github.com/DPDK/dpdk/commit/ca361b5ab1ba8ec9191b8376a8be0e3935823596)
- Reduced compilation warnings by removing unused variables and fixing a bad pointer reference in a memory allocation.
  ↳ No PR: [562814c](https://github.com/DPDK/dpdk/commit/562814cfedec6fbc9e899b7e5c15981eb725e022)
- Fixed the RSS hash key length acquisition and setting logic to avoid problems caused by incorrect reading and writing of the MAC address register.
  ↳ No PR: [346a007](https://github.com/DPDK/dpdk/commit/346a007e161e68950acbf59984fefc2bb6fe3982)
- Fixed an issue in port_rss_hash_key_update() where the user-entered RSS hash type was overwritten by rte_eth_dev_rss_hash_conf_get(), ensuring that RSS hash key updates take effect as expected.
  ↳ No PR: [24e94a4](https://github.com/DPDK/dpdk/commit/24e94a4c86c52f45a7a7c139e4e8484f3afe6d8f)
- Fixed the crash problem caused by the null pointer when the NFP network card driver obtains the RSS hash configuration.
  ↳ No PR: [53df262](https://github.com/DPDK/dpdk/commit/53df26286e4570ea328c5972fb244d8bc0008315)
- Fixed the problem that excess data may be copied when copying and sending in the null driver. Instead, only the data of the current mbuf segment is copied.
  ↳ No PR: [0ffd3bc](https://github.com/DPDK/dpdk/commit/0ffd3bc09be5f77b26c16e501e4b4465b1bcb8da)
- Fixed a crash or system lockup problem caused by unmasked control virtqueue ring index, and corrected the assignment of used ring element length.
  ↳ No PR: [38e6400](https://github.com/DPDK/dpdk/commit/38e640038798da92d1b7daf953f06fcd116cb952)
- Fixed the problem that the CN20K hardware cannot automatically correct the IP header of the reassembled packet. The software updates the IPv4 length, MF bit and checksum of the reassembled packet, as well as the IPv6 length and fragmentation extension header removal. It also corrects the data length of the last segment of the multi-segment decrypted packet.
  ↳ No PR: [d84b8bf](https://github.com/DPDK/dpdk/commit/d84b8bf31dfbf235d675eb6789d5ce776fb03cb1)
- Fixed the problem of statistics counter overflow in the ice network card driver causing data anomalies, and expanded the counter limit to a full 64 bits.
  ↳ No PR: [410738a](https://github.com/DPDK/dpdk/commit/410738ae1dc897e93c9c19b28a2517e0fb06e271)
- Fixed the cipher data length calculation error during chain encryption in vhost/crypto, and directly use the correct length value passed.
  ↳ No PR: [7ccd67c](https://github.com/DPDK/dpdk/commit/7ccd67c4185e1f4f0b975ff954e8685252bc3a18)
- Fixed the calculation of ciphertext data source length in symmetric algorithm chain processing, taking into account both ciphertext and authentication data lengths.
  ↳ No PR: [fcb4d1f](https://github.com/DPDK/dpdk/commit/fcb4d1f48e4aecb6be4ef7a4f6f25df24fee0ea2)
- Fixed the integer overflow problem during interrupt demapping in the hns3 driver, extending the interrupt vector variable type from uint8_t to uint16_t.
  ↳ No PR: [e401c04](https://github.com/DPDK/dpdk/commit/e401c04481c7a6a4199504d6f4696c48620ff093)
- Fixed the memory leak of indirect actions in hns3 driver, and changed the storage method of indirect actions from dynamically allocated pointers to uint64_t values.
  ↳ No PR: [18596f7](https://github.com/DPDK/dpdk/commit/18596f7be8f93e159e98704af12b1cc8af289dd6)
- Fixed the issue of missing interrupt rollback after the Tx queue failed to start when the port is started.
  ↳ No PR: [9e91104](https://github.com/DPDK/dpdk/commit/9e911049ac5188be7e080aa8699c0d8e97b32110)
- Fixed a division-by-zero error in the hns3 driver caused by the total queue number returned by the hardware being zero, and added validity verification of the total queue number.
  ↳ No PR: [a88f60f](https://github.com/DPDK/dpdk/commit/a88f60f32de6f94a5acbf2101cb5e527fac0b2d2)
- Fixed the problem that resources such as Rx interrupt mapping were not released when executing dev_stop when the device was reset, and a reset status check was added to prevent misoperation.
  ↳ No PR: [361eab8](https://github.com/DPDK/dpdk/commit/361eab82df67c09cb84a9e2e66c0d93a84be610d)
- Fixed the problem of receiving large packets in the ice driver: changed the selection timing of the Rx function from before the queue is started to after the queue is started, ensuring that the Rx function is correctly selected based on the relationship between the actual buffer size and MTU.
  ↳ No PR: [5c4cd2d](https://github.com/DPDK/dpdk/commit/5c4cd2dcd55b5f247693d92d4b4b61a17d18c63c)
- Removed unused enum constant VIRTCHNL2_CAP_OEM to fix compiler truncation warning caused by initializing a 32-bit enum member with a 64-bit value.
  ↳ No PR: [fc36674](https://github.com/DPDK/dpdk/commit/fc3667401fd5eaf94dd3d83ee96df105641f0904)
- Fixed the missing hardware status check in the event/cnxk timer arm routine to ensure that threads can correctly wait for the hardware status when being scheduled out with a bucket lock.
  ↳ No PR: [f77eb8f](https://github.com/DPDK/dpdk/commit/f77eb8f3c655a2573aed77bea122d98efc12edef)
- Fixed the problem of index calculation error when releasing flow rules to avoid out-of-bounds memory access caused by using fixed limits.
  ↳ No PR: [80209fe](https://github.com/DPDK/dpdk/commit/80209fe2a03b900e3b5e97ea98f487aec01adecc)
- Fixed the overflow problem when sending nfp driver control messages, and adjusted the number of write operations to match 32-bit data transmission.
  ↳ No PR: [3bceb13](https://github.com/DPDK/dpdk/commit/3bceb13047ea31868fb82beeb19befff636d9f20)
- Fixed an issue in the igb driver where the Tx queue offload capability incorrectly returned the port offload capability, instead returning zero to indicate no queue specific capability.
  ↳ No PR: [c2a1b38](https://github.com/DPDK/dpdk/commit/c2a1b38d779d8aed009e7f285ae95988bf9661da)
- Fixed the problem of EEPROM dump failure in the e1000 driver, corrected the boundary condition judgment, and allowed the legal situation where first + offset is equal to word_size.
  ↳ No PR: [b3855b9](https://github.com/DPDK/dpdk/commit/b3855b93dcc890f40dce3b688f5a331dcd8d14e8)
- Fixed use-after-free issue during dpio device cleanup in fslmc bus, use safe traversal macro instead to avoid accessing freed memory.
  ↳ No PR: [1cad17c](https://github.com/DPDK/dpdk/commit/1cad17c43079268d9e15db62b3a1edd42df8d81e)
- Fixed the port mask default value of the fdir filter in the ixgbe driver, changing it from 0xFF to 0 to support processing of raw IP packets.
  ↳ No PR: [c81daae](https://github.com/DPDK/dpdk/commit/c81daae2383ac655fe503e7da4767959ccc38ab7)
- Fixed the resource leak problem caused by directly returning a null pointer in the xsc_rss_qp_create function, and instead jumped to the error handling path.
  ↳ No PR: [e16e802](https://github.com/DPDK/dpdk/commit/e16e80250b8260bcc0106d40acdcef21999a161f)
- Optimized the release path and fixed the resource leakage problem during device shutdown and uninstallation.
  ↳ No PR: [6a7067f](https://github.com/DPDK/dpdk/commit/6a7067f7fbd15edcdd1ba96ebd24554b088e98a1)
- Changed per-queue and rx_nombuf stat counters to cumulative mode to correctly aggregate data from VF.
  ↳ No PR: [0bb9b5a](https://github.com/DPDK/dpdk/commit/0bb9b5aef16d3ba83066e03a87faf96da292c042)
- Added default port information padding on netport attach path, including legacy Siena fields.
  ↳ No PR: [2d3f6cc](https://github.com/DPDK/dpdk/commit/2d3f6cc45a49d3827c60397d15d6306e0502a553)
- Relaxed the limit on the number of traffic classes in the DCB command, now supporting 2 to 8 TCs.
  ↳ No PR: [5f2695e](https://github.com/DPDK/dpdk/commit/5f2695ee948ddaf36050f2d6b58a3437248c1663)
- Fixed the calculation of the required number of WQEs in inline data scenarios to make it more accurate; when the requested queue capacity cannot be met due to inline adjustments, an error is no longer returned, but a warning is issued and the queue is created with the maximum available size.
  ↳ No PR: [0c2f783](https://github.com/DPDK/dpdk/commit/0c2f7837c6733ee54ca8d335edaaf198c0a50f77)
- Fixed an issue where flow/table creation failed due to unnecessary insertion of NOP when using modify field action on group 0 flow rules.
  ↳ No PR: [f1ebb26](https://github.com/DPDK/dpdk/commit/f1ebb26d0d9388b6df65d493b06ce3b55adfb893)
- Added missing check for GTP PSC QFI stream field width to support modify field stream action.
  ↳ No PR: [34471d1](https://github.com/DPDK/dpdk/commit/34471d1645fae0e936c44f2f6d7fea6d22e4173e)
- Fixed the issue where the error code was not propagated correctly when the counter pool was initialized, ensuring that the correct error code is returned when allocation fails.
  ↳ No PR: [8774ac3](https://github.com/DPDK/dpdk/commit/8774ac32dfcf42a192f5b7785e956a8b1b754954)
- Fixed an issue where the mlx5 counter service did not clean up the background service thread when initialization failed, moving the creation of the service thread to the end of the pool initialization to ensure that resources are released correctly.
  ↳ No PR: [4d78ac5](https://github.com/DPDK/dpdk/commit/4d78ac5f3ef7c1ae3ae194423428c0f96e9994bc)
- Fixed a segfault caused by passing the wrong object handle when configuring VLAN stripping on the Rx hairpin queue.
  ↳ No PR: [468334f](https://github.com/DPDK/dpdk/commit/468334f07a9298fb4ff05e6cdcbbde64b0da4aa2)
- Fixed the validation logic of the GENEVE option in the non-template API, which is only validated when the rule is templated, and the parser is delayed until the rule is created.
  ↳ No PR: [3d7dae0](https://github.com/DPDK/dpdk/commit/3d7dae0878a36c4956084c1b5d01e225c170c1c3)
- Fixed a possible null pointer dereference problem in GRE flow item verification, and added a null value check for the gre_item pointer.
  ↳ No PR: [41e1fac](https://github.com/DPDK/dpdk/commit/41e1fac36acf0af9817f158a5ab4f4719cd6af4a)
- Fixed the issue of sending queue synchronization being skipped when destroying FW WQE rules to avoid permanent blocking of queue operations.
  ↳ No PR: [0394577](https://github.com/DPDK/dpdk/commit/0394577bdc91a25338fd9a61eb2ddfedf09f2800)
- Fixed the flex tunnel flow mode verification problem to ensure that the message items after the flex item in the template are correctly identified as inner headers.
  ↳ No PR: [7cafa01](https://github.com/DPDK/dpdk/commit/7cafa01ff9fad60d93ba4c536a28c288c36cbcee)
- Fixed the dereference problem in rte_bbdev_queue_configure that may be caused by conf being a null pointer, and add a null pointer check before calling the tracking function.
  ↳ No PR: [e1dc524](https://github.com/DPDK/dpdk/commit/e1dc5240fef85730c2f25a6cbccf29358e3afe25)
- Fixed the problem that the statistics sum in the net/ntnic driver does not include all queues. Now the sending and receiving data of all queues are included in the total, but the detailed statistics of each queue still only retain the first RTE_ETHDEV_QUEUE_STAT_CNTRS.
  ↳ No PR: [49230c4](https://github.com/DPDK/dpdk/commit/49230c4d74c24f0231be3b75041368636845e17d)
- Explicitly use 64-bit unsigned integers in shift operations to avoid precision issues caused by implicit type conversions.
  ↳ No PR: [64ba38c](https://github.com/DPDK/dpdk/commit/64ba38caaa1eec50a59c466e2eac1fc3a13f77f6)
- Fixed the problem that memory allocation failure in the net/ntnic driver was not handled correctly, and added a check on the return value of calloc to ensure that an error is returned or resources are released when allocation fails.
  ↳ No PR: [878eddf](https://github.com/DPDK/dpdk/commit/878eddf7ce39fc37157388126bd4e54487dc4b59)
- Fixed host-side FEC enable logic, removed redundant initialization and corrected loop boundary conditions.
  ↳ No PR: [e0251df](https://github.com/DPDK/dpdk/commit/e0251dfa15e56e81fb03b621ce4e115435ba96dd)
- Added return value check for IIC scan call, records error log and returns error code when it fails.
  ↳ No PR: [6580685](https://github.com/DPDK/dpdk/commit/6580685b136549d652c241dee57a40950be63a64)
- Fixed a possible divide-by-zero error in the statistics initialization function and added a zero-value check for RPP parameters.
  ↳ No PR: [8bbae3e](https://github.com/DPDK/dpdk/commit/8bbae3e37cf309e8ffc5292bf9d41c44a217f7f1)
- Fixed the problem of missing completion step in ring queue operation, and redesigned the queue read operation.
  ↳ No PR: [13b59c0](https://github.com/DPDK/dpdk/commit/13b59c07d6827e3cd7f746997b97fcffb5992435)
- Fixed the problem of incorrect VSI node position when using only 3 scheduler levels in the ice driver, and added processing logic to move VSI nodes down to the correct level.
  ↳ No PR: [c8f20c6](https://github.com/DPDK/dpdk/commit/c8f20c67da13294934dc71e6c18427685ca6eb38)
- Fixed SEC errors caused by invalid key commands in PDCP AES only 12-bit SN scenarios, and adjusted the control plane encryption operation and user plane encapsulation descriptor generation logic.
  ↳ No PR: [f0ccfc4](https://github.com/DPDK/dpdk/commit/f0ccfc4ddc7a01f4544b8a2913cc3d3f7c8b8832)
- Fixed an issue with uninitialized variables in the dpaa2_sec driver, where the authentication algorithm type was explicitly set during PDCP session setup.
  ↳ No PR: [db4bef4](https://github.com/DPDK/dpdk/commit/db4bef492253c23c0ff3e4c4a8124eb5af09f971)
- Fixed a segfault caused by using the wrong length when parsing the E-tag pattern, using the correct pattern item length instead.
  ↳ No PR: [a610e32](https://github.com/DPDK/dpdk/commit/a610e32b96768b84436ba523bc97af88df4d6963)
- In the virtio encryption driver, parameter checks for encryption and chained requests are added to the request side, and the calculation method of source data length is corrected.
  ↳ No PR: [9771f03](https://github.com/DPDK/dpdk/commit/9771f037ec8c6592126be49ca50953d1a14a0335)
- Configured CPT result address offset for CN20K platform, and corrected the acquisition logic of CPT queue ID.
  ↳ No PR: [3c31a74](https://github.com/DPDK/dpdk/commit/3c31a7485172068a91318168a9b32ee036f06d85)
- On non-cn10k platforms, when inline RQ is enabled, an error is returned if spb_ena is set to fix the configuration issue of inbound CPT LF ID.
  ↳ No PR: [65f4171](https://github.com/DPDK/dpdk/commit/65f4171916a960eb453d773270213dae95defeff)
- Updated buffer size in lookup-mem by default to maintain data order.
  ↳ No PR: [e77851a](https://github.com/DPDK/dpdk/commit/e77851a8c28312d2b753cb1b8d1ed954e148107c)
- Added support check for CPT05 microcode version in the Rx inject configuration function, and returns an error if it is not supported.
  ↳ No PR: [2e31c95](https://github.com/DPDK/dpdk/commit/2e31c95a84195346c9d918d0189e97c88f6cf81b)
- Fixed type conversion warning in ice_sched_move_vsi_to_agg function, changed loop variable type from u16 to u8 to avoid data loss, and added memory barrier instructions.
  ↳ No PR: [1651701](https://github.com/DPDK/dpdk/commit/16517011abfb4974af4eba63ad5a5e2aa65ef3ee)
- Fixed the spelling error of fiber media type check in ice_set_media_type, changed the incorrect C2C type to the correct C2M, to avoid some AOC devices being incorrectly recognized as AUI media types.
  ↳ No PR: [a9ed25d](https://github.com/DPDK/dpdk/commit/a9ed25d9bcaf0808341811bd95b31151ca66b5bf)
- Fixed a possible integer overflow problem when calculating powers of 2 in the ice_is_pow2 function.
  ↳ No PR: [152ebce](https://github.com/DPDK/dpdk/commit/152ebcea022feb1498fed591f92ebcf394a16ea7)
- Increased ice driver reset timeout from 5 seconds to 20 seconds to support longer reset times required by E830 hardware due to security key functionality.
  ↳ No PR: [702b69a](https://github.com/DPDK/dpdk/commit/702b69a837e6534d23a073c7082ad31eea7e94d0)
- Fixed the driver ID setting location of virtio and virtio_user encryption PMD to ensure that the driver ID is correctly assigned during device initialization.
  ↳ No PR: [9843181](https://github.com/DPDK/dpdk/commit/9843181aa5e764fd6876f50e8a795353e9261cb1)
- Optimized the MTU configuration, skipping the setting when the kernel MTU is already the same as the requested value, avoiding the need for NET_ADMIN permissions; also updated the list of supported packet types to include the out-of-order receive function.
  ↳ No PR: [f1f9113](https://github.com/DPDK/dpdk/commit/f1f9113a08b202d302ba9448d351c04da48ff46d)
- Fixed the problem caused by invalid entries remaining in the MAC address table when reconfiguring the device, by initializing the MAC address index mapping and maintaining the address copy to ensure that the index status is correct when adding, deleting and refreshing.
  ↳ No PR: [25e3529](https://github.com/DPDK/dpdk/commit/25e35296b5f5a32ce157d1594518f4d71dd65f34)
- Fixed the problem of incorrect descriptor count update during Rx queue reconfiguration in the cnxk network card driver, ensuring that the initial input descriptor count is used.
  ↳ No PR: [ad23295](https://github.com/DPDK/dpdk/commit/ad23295cb8217390b9f966ad5ee10a4e21f9c20b)
- Fixed a segfault caused by improper cleanup when using multiple devices, and changed the device release to call rte_cryptodev_pmd_release_device.
  ↳ No PR: [6adb7f4](https://github.com/DPDK/dpdk/commit/6adb7f4ae156341958463db80951d8f528932e9f)
- Fixed an issue with flow rule identification issues created by the template API, ensuring that its nt_rule flag is correctly set to false.
  ↳ No PR: [82e0453](https://github.com/DPDK/dpdk/commit/82e0453609e59d66b0fce9c59ce0380d7bc39e17)
- Fixed used length of vhost control virtqueue so that it correctly represents the number of bytes written rather than the number of descriptors.
  ↳ No PR: [69244db](https://github.com/DPDK/dpdk/commit/69244dbc485d72ecf25d561ed085ecece69f6f33)
- Changed the memory access permission of the virtqueue driver area from read-write to read-only to be compatible with all backend configurations.
  ↳ No PR: [3bd0c97](https://github.com/DPDK/dpdk/commit/3bd0c97b56c8e3c198d604871f35c125afdc4dc4)
- Fixed the Tx release threshold check logic in the virtio driver so that the buffer release is correctly triggered when the number of free descriptors is lower than the threshold.
  ↳ No PR: [3e3c7f3](https://github.com/DPDK/dpdk/commit/3e3c7f3fa5ac3f2748a4463d87e73eb28024b401)
- Reconfigured K1 exit timeout, optimized clock synchronization workaround, and reduced power consumption.
  ↳ No PR: [ba54bdc](https://github.com/DPDK/dpdk/commit/ba54bdc79d94f5b292dd4877dbe494de5ab03e67)
- Disabled PHY-based PTP capability support.
  ↳ No PR: [ca2611b](https://github.com/DPDK/dpdk/commit/ca2611b10e5a357aa20221d68f369a37c5e0f765)
- Fixed the setting of the salt value in the AES-CTR algorithm to ensure correct copying and conversion of endianness, and added test cases and test vectors for the AES-CTR encryption mode.
  ↳ No PR: [a1efd31](https://github.com/DPDK/dpdk/commit/a1efd31b0f426c3420d3931c7bb5bd11f03b44de), [305102b](https://github.com/DPDK/dpdk/commit/305102b51f8f333a183f3b70014b22bea58a3e65)
- Fixed the issue where the queue size was not reconfigured when the CPT command queue was enabled, ensuring that NQ_PTR and DQ_PTR are correctly reset each time it is enabled.
  ↳ No PR: [8c60a3f](https://github.com/DPDK/dpdk/commit/8c60a3ff2367e4c1189fac431ccb046107b91357)
- Fixed the compatibility issue between vector algorithm and offload/filter function in hns3 driver, allowing vector algorithm to be used when Tx offload is not enabled, and allowing Rx vector algorithm to be used when VLAN filtering is enabled.
  ↳ No PR: [e05cb70](https://github.com/DPDK/dpdk/commit/e05cb702ca70aecdf01041274cd6ffc9233a726d), [4d345eb](https://github.com/DPDK/dpdk/commit/4d345eb5ef9827aec1547d7dfc9afcf363359b46), [1c27385](https://github.com/DPDK/dpdk/commit/1c27385dcef1384a1a10edd86bb843b06547b161), [7c8cbd3](https://github.com/DPDK/dpdk/commit/7c8cbd3c8ae0cec66fbd5acb89a62ee9742c70b4)
- Fixed the problem that the MAC control frame forwarding configuration of txgbe and ngbe network cards becomes invalid after the port is stopped/started, ensuring that the flow control function can still work normally after the port is restarted.
  ↳ No PR: [b711273](https://github.com/DPDK/dpdk/commit/b71127393a37cda0de6ca088f9945ee1a148e712), [31ae872](https://github.com/DPDK/dpdk/commit/31ae872822cdc89cd00926c3e162781ef927ca24)
- Fixed read errors in rx_undersize_errors and tx_broadcast_packets in txgbe and ngbe device statistics, corrected register addresses and used rd64() instead to get full counts.
  ↳ No PR: [d1406cf](https://github.com/DPDK/dpdk/commit/d1406cf06220c78245bbb9db258f488e97f903e0), [a65009b](https://github.com/DPDK/dpdk/commit/a65009b7621a60faeb1bbefe65160eb5646925dc)
- Fixed calculation problem in latencystats library when TSC frequency is non-integer nanoseconds, use floating point numbers instead and precompute the number of cycles per nanosecond.
  ↳ No PR: [a3645b7](https://github.com/DPDK/dpdk/commit/a3645b758eade231d51d3d39c3febeaa7d1ec7f7), [fed4eef](https://github.com/DPDK/dpdk/commit/fed4eef6b6745ce5b82e6d49552d2473ce1a959b), [b670586](https://github.com/DPDK/dpdk/commit/b670586335766a262787ba3beb86fd557dfa2f99)
- Excluded MACsec statistics for E610 devices to avoid displaying meaningless xstats.
  ↳ No PR: [e24ffb2](https://github.com/DPDK/dpdk/commit/e24ffb2b28b43e3583d357a568c2f7548e0be88a)
- Updated the PHY configuration and MCU patch of RTL8125B, 8125D and 8126A, and introduced MCU patch version checking logic.
  ↳ No PR: [15cc001](https://github.com/DPDK/dpdk/commit/15cc001dc4fcac9eeb11ef3143223e1315e2198f)
- Fixed out-of-place chain/encryption/authentication header issues for gen3 and gen4 in QAT driver.
  ↳ No PR: [068acf1](https://github.com/DPDK/dpdk/commit/068acf11cec0597735c9d82c8f4972251c736717)
- Fixed the ntuple filter parsing error so that certain patterns (such as ipv4/udp/raw) can be correctly parsed as FDIR rules instead of ntuple filters.
  ↳ No PR: [bed0e6a](https://github.com/DPDK/dpdk/commit/bed0e6aba0aef7a1e67d3ee620873817f00a511d)
- Fixed matching of raw pattern in FDIR rules, converting strings to hexadecimal bytes and supporting relative offsets.
  ↳ No PR: [aa49747](https://github.com/DPDK/dpdk/commit/aa4974765499225e13225190a0dc6adaab785c80)
- Fixed the packet type matching of the txgbe network card FDIR filter, and added a packet type mask to support more flexible type matching under the default pattern.
  ↳ No PR: [8d10841](https://github.com/DPDK/dpdk/commit/8d10841e5acd381c7831e421103872d12e806780)
- Fixed the FDIR perfect mode support for IPv6 in the txgbe driver, removed the previous restriction that prohibited IPv6 and added the corresponding hardware configuration.
  ↳ No PR: [db48788](https://github.com/DPDK/dpdk/commit/db4878838ad0e978352cad411f4a72d0cead81fe)
- Fixed the logic of creating FDIR filters for tunnel packets in the txgbe driver, now supporting inner layer matching for VXLAN, GRE, NVGRE and GENEVE protocols.
  ↳ No PR: [a185146](https://github.com/DPDK/dpdk/commit/a1851465f8252ee75a26d05b9b2d3dca7023e8f2)
- Removed the duplicate reservation of FDIR header space and fixed the problem of RX packet buffer size being 256KB less than the theoretical value.
  ↳ No PR: [3f5886d](https://github.com/DPDK/dpdk/commit/3f5886d6435eb7e9add005d8e7dc880841a51465)
- Fixed hardware limitation of VLAN stripping configuration on VF, allowing VLAN stripping offloading to be configured only on device startup.
  ↳ No PR: [b8c3d76](https://github.com/DPDK/dpdk/commit/b8c3d76e790cb06b54469b71a1af822de50c790d)
- Fixed the problem of RSS hash configuration in ice DCF driver, including the logic of obtaining the currently configured hash type and extracting the set RSS key, making its behavior consistent with PF and other drivers.
  ↳ No PR: [5c5641e](https://github.com/DPDK/dpdk/commit/5c5641ec00d3db04a5c123e86a09a3b4c8c748b9), [a84f23c](https://github.com/DPDK/dpdk/commit/a84f23cfb52c0505f87b07e919e1c01ff3e38eb2)
- Added check for invalid socket ID during memory allocation initialization to avoid potential problems.
  ↳ No PR: [2f85628](https://github.com/DPDK/dpdk/commit/2f856284639cb73c4ce20ef1b471dae934807f6d)
- Fixed an issue where the VLAN stripping flag was not synchronized after setting VLAN filtering in the iavf driver, explicitly disabling stripping to remain consistent with the DPDK side.
  ↳ No PR: [3bfad06](https://github.com/DPDK/dpdk/commit/3bfad066f9b4764981c9ad90a750fa6f1afcf15a)
- Solved the problem of sysconf query page size failure, added the mem_page_size() function in the PMU library, and modified the cleanup_events function to use this function to avoid unprocessed negative return values.
  ↳ No PR: [fb2b4a0](https://github.com/DPDK/dpdk/commit/fb2b4a061736a6c01dea67bb5079925990665ac4)
- Fixed null pointer crash caused by uninitialized pointer when HWS counter pool is destroyed.
  ↳ No PR: [0aa0d0e](https://github.com/DPDK/dpdk/commit/0aa0d0e85011116d545318b79e28cb177f5da825)
- Fixed the problem that expired memory may be accessed when accessing auxiliary stream data in the mlx5 driver, and separated the auxiliary data acquisition paths of template streams and non-template streams.
  ↳ No PR: [92a5b06](https://github.com/DPDK/dpdk/commit/92a5b06c150ec5c28d7fb734d1ea1e7d5b4cb26f)
- Fixed an out-of-bounds access problem in the cnxk_gpio driver caused by ioctl returning invalid flags when the underlying GPIO device was removed. This was avoided by adding a bounds check and returning an error code.
  ↳ No PR: [a825de7](https://github.com/DPDK/dpdk/commit/a825de749bdfc988abd8f9702418112df32f9a2f)
- Fixed a segfault caused when querying AGE actions for flow rules tracked using indirect joins, by adding a check to prevent AGE queries for indirect CT actions.
  ↳ No PR: [3bb6e3b](https://github.com/DPDK/dpdk/commit/3bb6e3bf05284f0668e2ac14ce4b90a2909dff99)
- Fixed the descriptor flag error in the virtio encryption device, and updated the virtqueue metadata management.
  ↳ No PR: [2249362](https://github.com/DPDK/dpdk/commit/22493624c15701dad455b892f3ab52c8920cf792)
- Fixed an issue in the mlx5 driver where the mirror action in the unified FDB domain resulted in abnormal STC resource allocation due to incorrect group ID settings.
  ↳ No PR: [3e6bc6f](https://github.com/DPDK/dpdk/commit/3e6bc6fa3ee087f2e14fd6a8a86168db074e9697)
- Fixed the problem of incorrect calculation of the Tx queue WQE size in the mlx5 driver, ensuring that the calculated WQE size is not less than 64 bytes to avoid incorrect calculation of the total WQE number when the number of descriptors is 512.
  ↳ No PR: [5c0c1a1](https://github.com/DPDK/dpdk/commit/5c0c1a13c34aa57c6e18f9ba852a9b5807c58b72)
- Fixed an issue with inconsistent placement of Rx queue VLAN tags in the ice driver, using the queue's register index instead of the queue ID when updating the l2tsel field.
  ↳ No PR: [4cd8c72](https://github.com/DPDK/dpdk/commit/4cd8c72f661c005900ddc39cf0cecfca16184f2a)
- Fixed the processing of interrupt registration or activation failure during device initialization in control path interruption mode, and added error checking and cleaning logic.
  ↳ No PR: [99bfe66](https://github.com/DPDK/dpdk/commit/99bfe66911cabf8f2ae1c17e05970e969bbfe794)
- Fixed a segfault caused by missing validation when using masked indirect age actions in action templates, and removed redundant debug assertions.
  ↳ No PR: [6ed1ce0](https://github.com/DPDK/dpdk/commit/6ed1ce029d6bd89a47968cd92d99cdf7ece8ac96)
- Fixed the adjustment logic of the maximum inline data size when using Verbs to create a queue, ensuring that it complies with the acceptance range of the rdma_core library.
  ↳ No PR: [8cc91d3](https://github.com/DPDK/dpdk/commit/8cc91d33e4447477f5d486475ff8efcefcc3c7d9)
- Fixed an issue where the wrong virtchnl operation was called when VLAN stripping was disabled on an ADQ v2 capable network card.
  ↳ No PR: [5503bbc](https://github.com/DPDK/dpdk/commit/5503bbc975b3ab46240e0ce5da1a6003c8f5dbb5)
- Fixed the resource leak problem caused by the reference count not being decremented correctly when the Tx queue is started in the mlx5 driver.
  ↳ No PR: [d48a5af](https://github.com/DPDK/dpdk/commit/d48a5afc203db0fafe5fb811321788a459d3f6e9)
- In bonding PMD, when the device is configured with flow isolation mode, the RSS RETA update operation is skipped to avoid errors caused by calling unsupported APIs.
  ↳ No PR: [a000085](https://github.com/DPDK/dpdk/commit/a0000859ffbaaaf90bbb9c0f2f5bb7a3d4f5bc9f)
- Fixed the missing flag for RSS support for pure IPv4 traffic in the i40e driver, and added the corresponding pctype mapping.
  ↳ No PR: [5d47e73](https://github.com/DPDK/dpdk/commit/5d47e73e5f4f2eb69bd73f642cfd72b49436bf96)
- Fixed a crash caused by not verifying the existence of the driver when cleaning the auxiliary bus device.
  ↳ No PR: [f03c01f](https://github.com/DPDK/dpdk/commit/f03c01f601b1b8d90f62c8a5acead72c04797d7a)
- Rolled back a fix for the Tx release threshold check that caused a performance regression.
  ↳ No PR: [5a117f0](https://github.com/DPDK/dpdk/commit/5a117f05fc5ad200ec61837fa21d946c6a209822)
- Fixed a mismatch in Tx queue length calculation in different modes, by adding a boolean parameter to the txq_calc_wqebb_cnt function to distinguish Devx mode, and using a more accurate way of getting the WQ size instead.
  ↳ No PR: [9b298e7](https://github.com/DPDK/dpdk/commit/9b298e79703a1343d388d059f4029813f11ac6ad)
- Fixed a parameter mismatch in the cryptodevs_init function call in the ipsec-secgw example, which caused an incorrect initialization of the queue pair.
  ↳ No PR: [7e6d610](https://github.com/DPDK/dpdk/commit/7e6d6106a4ef052d6a2a6bd6e83c5b16a36c65c9)
- Fixed the inclusion order of vector codes in the IAVF driver to avoid compilation errors caused by incorrectly enabling 16-byte descriptors.
  ↳ No PR: [f1853a0](https://github.com/DPDK/dpdk/commit/f1853a0cc95eaae5842b88be0cbcd5becc2e94b7)
- Rolled back the change in clearing the port when exiting in the multi-process example to avoid the error that caused the secondary process to crash when the main process closed the port.
  ↳ No PR: [dc88bee](https://github.com/DPDK/dpdk/commit/dc88beed495c04b745d17bc8c1718fa76b914593)
- Fixed multiple MSVC compilation warnings and errors to improve cross-platform compatibility.
  ↳ No PR: [ff1f31b](https://github.com/DPDK/dpdk/commit/ff1f31bdbd07b278d525f0687dfe66b863873726), [cd70174](https://github.com/DPDK/dpdk/commit/cd70174276bf2ed28b0b95719cbca6fbfa319034), [99c61c7](https://github.com/DPDK/dpdk/commit/99c61c7acc22f9a9b04d95aeee0b808c43bfccf8), [afe0f93](https://github.com/DPDK/dpdk/commit/afe0f9308edf73bb9b0bf7175211d0b925b66d13), [0d7b792](https://github.com/DPDK/dpdk/commit/0d7b792013a4b5efd74fb06186d319ddaf443307), [321f0a6](https://github.com/DPDK/dpdk/commit/321f0a60005e7d3192300988b6a31e2a50945c4b)
- Fix MSVC compilation warning: change the printf format specifier from %d to %u, and correct the calculation logic of l2_len and eth_hdr in tunnel processing.
  ↳ No PR: [5ab6676](https://github.com/DPDK/dpdk/commit/5ab6676a10e771e4eb0d51dcd345cc34557ff406)
- Fix the assignment position of mark_flag in the shared Rx queue to ensure that the flow mark action is set correctly.
  ↳ No PR: [28eeca6](https://github.com/DPDK/dpdk/commit/28eeca69eb1d9bebb0105e47c82885b0a8403654)
- Removed the priority check in the ice_fdir_parse function in non-pipeline mode, and fixed the problem of failure to create valid flow rules.
  ↳ No PR: [1f33249](https://github.com/DPDK/dpdk/commit/1f332499adc57c86c46fdb26c923f8f56d4cb765)
- Fix bug of uninitialized variables in vhost/crypto.
  ↳ No PR: [e859f9f](https://github.com/DPDK/dpdk/commit/e859f9fc40b505f0ef4abbc5f9aca54673663845)
- Fixed a crash caused by calling rte_power_uncore_exit when the driver is not initialized.
  ↳ No PR: [74c4b08](https://github.com/DPDK/dpdk/commit/74c4b081825123350578f18dc838ec0bf69ba03b)
- Fixed the inconsistency in MAC address processing between PF and VF/SF in the mlx5 driver to ensure that IFF_ALLMULTI works properly.
  ↳ No PR: [2d0665a](https://github.com/DPDK/dpdk/commit/2d0665a7f7719e8cd615b64ac9f2c8c22d47450a)
- Fixed the mask initialization of flow random item token in testpmd to avoid out-of-bounds memory access.
  ↳ No PR: [9a18070](https://github.com/DPDK/dpdk/commit/9a18070e3fe43cd45fc5f000452853a0a45d25c2)
- Fixed the problem of false reporting of errors due to errno comparison errors when the tap network card qdisc fails to be created.
  ↳ No PR: [02a6864](https://github.com/DPDK/dpdk/commit/02a68649e6fb55d8975c726e3073ee9d12c20bac)
- Fixed the problem of offset being overwritten when parsing the GENEVE package, and correctly set the inner L2 length.
  ↳ No PR: [0a70cf3](https://github.com/DPDK/dpdk/commit/0a70cf3308f99bd3c32925e5fb0ec465ad4390e8)
- Fixed the problem in testpmd that caused subsequent packet type parsing errors due to residual header length information.
  ↳ No PR: [2e0f1e6](https://github.com/DPDK/dpdk/commit/2e0f1e6ec53d5360e8bb7b9dcbfe63839d8a6d9d)
- Fixed the incorrect assignment of the number of decrypted packets field in the queue pair statistics in the cnxk encryption device driver.
  ↳ No PR: [a82f46b](https://github.com/DPDK/dpdk/commit/a82f46b03b0f91cbd6d9f2fb1efd4947b8f69231)
- Fixed issues with SCTP packet flow direction filter mask checking and LRO flag setting in the txgbe driver.
  ↳ No PR: [0db38d5](https://github.com/DPDK/dpdk/commit/0db38d54b57a963bab33dca65c1795eefdca2dd5), [5bc6a8b](https://github.com/DPDK/dpdk/commit/5bc6a8b17afbf299773a70315ad95262d8f6d0ac)
- Fixed compilation warning in i40e driver.
  ↳ No PR: [3c21258](https://github.com/DPDK/dpdk/commit/3c2125852742d46accc3f35f4fa683768ba25e09), [e0a9cb8](https://github.com/DPDK/dpdk/commit/e0a9cb8b940b539b68acc7d8221f9aeec0f20a82)
- Restrict VLAN strip configuration of ngbe VF devices to only occur when the device is stopped.
  ↳ No PR: [26bf499](https://github.com/DPDK/dpdk/commit/26bf49930cebd6b65fcd3065d0bb8b02419d1abf)
- Fixed bug in auxiliary device name extraction, ensuring that the sysfs directory is closed only after copying the file name.
  ↳ No PR: [a60378a](https://github.com/DPDK/dpdk/commit/a60378a398fd95e6de69401e8ed06fcc3f4a3929)
- Fixed an error in calculating the inner information of tunnel packets in testpmd.
  ↳ No PR: [a738c43](https://github.com/DPDK/dpdk/commit/a738c43ffaee9ba5d8eccb0e881e7c816d3c6415)
- Fix the field offset and bit width of the Tx time queue context structure in the ice driver to align it with the hardware specifications.
  ↳ No PR: [6c1844d](https://github.com/DPDK/dpdk/commit/6c1844d52c1dc2c7ab8889ab27888bc6291552a4)
- Fixed a crash caused by incorrect handling of lookaside mode IPsec packets in ipsec-secgw in event vector mode.
  ↳ No PR: [811383e](https://github.com/DPDK/dpdk/commit/811383ef109d8dae04c0681b84de09c51f153543)
- In flow rule translation, register metadata is used first when matching E-Switch manager ports.
  ↳ No PR: [d0cf107](https://github.com/DPDK/dpdk/commit/d0cf1072380ad7194f373fa80f742bfe9311db47)
- Fix the null pointer check before the CPT instruction is executed, and add null pointer check and structure initialization.
  ↳ No PR: [bba99bb](https://github.com/DPDK/dpdk/commit/bba99bb88c4f2bf3391ade016d808b27a8a17a19)
- Fixed an issue where multi-process examples did not stop and close ports when exiting.
  ↳ No PR: [4382d58](https://github.com/DPDK/dpdk/commit/4382d58097b41d1e1229ce5fc2943994bf44bd83)
- Fix GCC 15 build warning on aarch64, centrally initialize completion structure count field.
  ↳ No PR: [6cde8a3](https://github.com/DPDK/dpdk/commit/6cde8a3dda49ad2721ac15faedf1965cdb4980b0)
- Fixed xstats name spelling error in igb and igc drivers.
  ↳ No PR: [9303834](https://github.com/DPDK/dpdk/commit/9303834c26ec7b3fb91f84d2c953ce4dae3073fb)
- Fix warning on implicit conversion of 32-bit left shift to 64-bit when compiling with MSVC.
  ↳ No PR: [f51731e](https://github.com/DPDK/dpdk/commit/f51731e3ad4b46c5764cc30bfbb107248655b7c8)
- Added null value checks for pointer parameters in multiple functions to prevent null pointer calls.
  ↳ No PR: [520cb8d](https://github.com/DPDK/dpdk/commit/520cb8dda73607ab19e9a1bc04c625e5d45748d8)
- Add clear error log when no lcore is available to facilitate troubleshooting.
  ↳ No PR: [2ea1d30](https://github.com/DPDK/dpdk/commit/2ea1d30dc938866a983156473579d10bddb4951e)
- Updated the error log information when DDP package loading fails to make it more clear.
  ↳ No PR: [f8d5ce2](https://github.com/DPDK/dpdk/commit/f8d5ce2cdc16ac43e0b767402c4b83b36c01da10)
- Fixed MSVC compilation warning: using EAL macro for pointer arithmetic in write_edge function.
  ↳ No PR: [77be488](https://github.com/DPDK/dpdk/commit/77be4888d03381325885ac91c8bf384ffd178d93)

### Refactoring optimization
- Reconstruct the DTB driver queue operation interface, reimplement the queue request and release functions, and add a new queue initialization function.
  ↳ No PR: [3758b92](https://github.com/DPDK/dpdk/commit/3758b92d8ade18a19d225bbd4bdb0bb7f07415e9)
- Replace GCC's built-in atomic operations in the cnxk driver with DPDK's rte_atomic_xxx API.
  ↳ No PR: [3bb6014](https://github.com/DPDK/dpdk/commit/3bb6014459885468dcce3d259c290549bb9e3bf5)
- In dpaa2_sec and dpaa_sec encryption drivers, use rte_cryptodev_pmd_create and rte_cryptodev_pmd_destroy API to replace the original device allocation and release logic, simplifying the driver initialization and disassembly process.
  ↳ No PR: [3ea1ddb](https://github.com/DPDK/dpdk/commit/3ea1ddb3056da4d55a932daa10e7d906c422b88c)
- Updated the calculation method of segment offset.
  ↳ No PR: [ce53d0f](https://github.com/DPDK/dpdk/commit/ce53d0fdacb33a4c5cc0b811288b27dd59a998ff)
- Changed the internal storage of latency statistics from floating point numbers to integer cycle counts, converted to nanoseconds when reading; adopted an exponentially weighted moving average (EWMA) fixed-point scaling algorithm, and initialized the average latency at the first sample per RFC 6298.
  ↳ No PR: [5f415c2](https://github.com/DPDK/dpdk/commit/5f415c2c12df742d92bdf6221b80c287af54b3d7)
- Removed all 16-byte descriptor related code in the iavf driver, because there is no physical function to support VF using this descriptor.
  ↳ No PR: [34b3f63](https://github.com/DPDK/dpdk/commit/34b3f630991ee9b86b9ef379b307fc71508e8218)
- Replace structure copy from memcpy to direct assignment to enhance type safety.
  ↳ No PR: [a7dc45b](https://github.com/DPDK/dpdk/commit/a7dc45b6f70589dceb2ec14e99ab642886c579a0)
- Reconstruct the find_next_n function to flatten the nested loop into a state machine implementation to improve readability and efficiency.
  ↳ No PR: [4055c5c](https://github.com/DPDK/dpdk/commit/4055c5c30dd9dcba1c5a39dbe96ac95bd364aea6)
- Removed unnecessary dereferences of function pointers in multiple drivers and libraries, simplifying the code.
  ↳ No PR: [9d57325](https://github.com/DPDK/dpdk/commit/9d57325f21906f3d0842e967dd81a4ebf47b17f9), [ff22d63](https://github.com/DPDK/dpdk/commit/ff22d6355a1568f3f1b05153fb854ddc42ebf976), [5ab2052](https://github.com/DPDK/dpdk/commit/5ab2052b3112aa261a40f1ba5d794a5bded993b8), [65edd6f](https://github.com/DPDK/dpdk/commit/65edd6f9bd054d7f7059041bfc40f729c904cb8d)
- Unified the conditional compilation macros supported by AVX-512 and removed custom build processing.
  ↳ No PR: [6c15859](https://github.com/DPDK/dpdk/commit/6c15859e773612d81fc2fb4034e1a9ad3ac0b5e0)
- Replace the explicit MAC type comparison for VF judgment in the ixgbe driver with the existing ixgbe_is_vf function call to simplify the code.
  ↳ No PR: [78d6854](https://github.com/DPDK/dpdk/commit/78d6854e0e3941e9b37e7f5c104c2ea7576d0f45)
- Unify the naming of the Tx queue structure fields of idpf and cpfl drivers, and migrate the idpf driver Tx path to a common structure to prepare for subsequent merging.
  ↳ No PR: [f84b2ff](https://github.com/DPDK/dpdk/commit/f84b2ffb0466dff28ab98f2a07c9a88840dad719), [e4b60e2](https://github.com/DPDK/dpdk/commit/e4b60e2eae2c33ed91b5a51457826a8ebadfbde5), [eadb73b](https://github.com/DPDK/dpdk/commit/eadb73be72c4e64e9c4153ce3be75c8a070a040b)
- Renamed the variable if_index representing the PHY index to n_intf_no to avoid confusion.
  ↳ No PR: [0be5787](https://github.com/DPDK/dpdk/commit/0be57877975cc81420a6bbc12bece60077797c47)
- Simplified the conditional judgment of multiple functions in the ntnic driver, removing redundant checks, useless expressions and unused functions.
  ↳ No PR: [40b5c30](https://github.com/DPDK/dpdk/commit/40b5c301f7b2b4ad8fd6e3b1b6d824655c1ccc5f), [853d955](https://github.com/DPDK/dpdk/commit/853d9556884c575d4778a66a37497624fba21708), [d5d5aeb](https://github.com/DPDK/dpdk/commit/d5d5aeb3c94ec9456127f05efb11baad2f181c79), [be36fe8](https://github.com/DPDK/dpdk/commit/be36fe8cf3c1a57ba28e27b3b2013c020fdb500f)
- Reconstructed the array access method, replacing pointer operations with explicit array subscript operations, making the code intent clearer.
  ↳ No PR: [e9def8f](https://github.com/DPDK/dpdk/commit/e9def8fc2b5e27d65e95a06bf9d2dac66cd1a899)
- Clean up zsda compression driver code style, rename multiple internal functions to remove comp_ prefix.
  ↳ No PR: [cf4edbf](https://github.com/DPDK/dpdk/commit/cf4edbf231e8a5fe6b24bf3bed4624307aa9037c)
- In the cnxk encryption driver, rename the IV setting function of AES-GCM to the general 8-byte IV setting function, and extend its calling logic to support the AES-CTR algorithm.
  ↳ No PR: [314c03e](https://github.com/DPDK/dpdk/commit/314c03e20e4c998f7b40875696f29265fa2619b1)
- Replace memcpy with struct assignment to preserve type information and enhance compiler type checking.
  ↳ No PR: [c814ad3](https://github.com/DPDK/dpdk/commit/c814ad3f5df71cef264328fccfdc4d8fbcf91e20)
- Simplify the checking logic of packet type support in the ixgbe driver and remove one-by-one comparison of multiple receiving function pointers.
  ↳ No PR: [0d99ea4](https://github.com/DPDK/dpdk/commit/0d99ea4e78f37208f4805fdb044207c4e9bad7ba)
- Renamed the vector Tx mbufs free function in the ixgbe driver to ixgbe_tx_free_bufs_vec to avoid naming conflicts with the scalar implementation.
  ↳ No PR: [9a9d0a3](https://github.com/DPDK/dpdk/commit/9a9d0a31a10cbec9280cfc170fec2defac5db8ad)
- Moved ixgbe's vector sending function to a common vector file, and adjusted related data structure references.
  ↳ No PR: [fb23883](https://github.com/DPDK/dpdk/commit/fb238838df48c8b391419d9ecb93f1f8ec6070bf)
- Added a new descriptor done function to the ixgbe driver to uniformly check the DD bit status and replace the original method of directly reading the status register.
  ↳ No PR: [df15240](https://github.com/DPDK/dpdk/commit/df15240e733fb11937d779a8e0b1c317c6e7e220)
- The iavf driver uses the public vectorized Rx rearm implementation and uses public macro definitions uniformly.
  ↳ No PR: [11276ec](https://github.com/DPDK/dpdk/commit/11276ec5e042de6adae668efacfca6854a40ddd3)
- Split the doorbell writing logic into independent Rx and Tx processing functions, removing unnecessary LLQ checks in the Rx path.
  ↳ No PR: [8eec2b8](https://github.com/DPDK/dpdk/commit/8eec2b8a46bfcefe4abd72e2ab5b394e08d0fed6)
- In the receive queue setup completion function, the variable length array was removed in favor of a fixed size burst array, and the idle count calculation was adjusted to limit the burst size.
  ↳ No PR: [53f4bbe](https://github.com/DPDK/dpdk/commit/53f4bbeddc6683868f82976df86069d9ea686c96)
- Removed forced inlining and loop unrolling instructions in the TAP device BPF program to adapt to modern BPF validators.
  ↳ No PR: [d13c61b](https://github.com/DPDK/dpdk/commit/d13c61b00bee7f650a948879cc2f766f145b57e4), [fd979f7](https://github.com/DPDK/dpdk/commit/fd979f764cc5640430a05ef13ab618e8b9011a91)
- Remove redundant memset calls in dpdk_stats_collect.
  ↳ No PR: [8b36586](https://github.com/DPDK/dpdk/commit/8b3658670eca7e743fb4a8334c23e494de610e9d)
- Removed unused clock frequency and clock source assignments in PTP code.
  ↳ No PR: [4644c7a](https://github.com/DPDK/dpdk/commit/4644c7a6d306c71c957728e8a92efb621193d3fd)
- To eliminate MSVC compilation warnings, add explicit type conversions for mixed enumeration types.
  ↳ No PR: [e42334e](https://github.com/DPDK/dpdk/commit/e42334ef68b2eb87922661cf5c5fe00d3eb7ba96)
- Renamed rx_using_sse variable in i40e driver to vector_rx.
  ↳ No PR: [0545a2f](https://github.com/DPDK/dpdk/commit/0545a2f6f2af5ae22a7ee42cd0f33f4235947072)
- Renamed rx_ring_dma variable in ice driver to rx_ring_phys_addr.
  ↳ No PR: [9a40f9e](https://github.com/DPDK/dpdk/commit/9a40f9e23e9fcf301be082de4b1fa9ab5d1ddad7)
- Rename the macro definition of the 16-byte Rx descriptor to RTE_NET_INTEL_USE_16BYTE_DESC, and update the related type names simultaneously.
  ↳ No PR: [d1a350c](https://github.com/DPDK/dpdk/commit/d1a350c089e04e57a196378490617cc3032c514d)
- Clean up the internal macro definitions and type names of the ixgbe driver and unify them with the IXGBE_VPMD_ prefix.
  ↳ No PR: [854716b](https://github.com/DPDK/dpdk/commit/854716b61045a2f9934545a18d9bd0e6bbbb50c4)
- Clean up vector PMD macro definitions in i40e, ICE, IAVF drivers, unify prefixes, and add per-cycle descriptor constants for different vector implementations.
  ↳ No PR: [b0d72ca](https://github.com/DPDK/dpdk/commit/b0d72caf41950a95c69c916f34f8d1a1ae470527), [51ceb8f](https://github.com/DPDK/dpdk/commit/51ceb8f600bbb2c7b42d7d26e5b6c2657b008c08), [268383b](https://github.com/DPDK/dpdk/commit/268383b7b0594e7a61c85ec4c613680c8a338943)

### Test related
- Fixed multiple test compatibility issues in the MSVC compilation environment, including stack overflow, compilation warnings and format errors.
  ↳ No PR: [d6a29fe](https://github.com/DPDK/dpdk/commit/d6a29fedf36cd4faf07621d9fa3e82dc4e7ba74b), [af94f48](https://github.com/DPDK/dpdk/commit/af94f48030509306a78a40038f729c6ba0c3ed1c), [86cd422](https://github.com/DPDK/dpdk/commit/86cd422a1d889b44a68b9bc8e7bcb528dc1a9e0f), [76dddce](https://github.com/DPDK/dpdk/commit/76dddce02ae77f0aafe880f071d1cdb852b38a4a)
- Expanded the memory pool performance test, adding cache scenarios and random batch size tests.
  ↳ No PR: [74a5d17](https://github.com/DPDK/dpdk/commit/74a5d1784e607922e3a7cd8c7b1289da1e69d6c3), [685735c](https://github.com/DPDK/dpdk/commit/685735ce6877641394ad64899354b5ae8b4e40b8)
- Added test cases and test vectors for modex group 24 and larger mode RSA for encryption testing.
  ↳ No PR: [fa2857c](https://github.com/DPDK/dpdk/commit/fa2857cdf857f7e8dcc1803191ebf41051424ad8), [e131b8e](https://github.com/DPDK/dpdk/commit/e131b8e643fdf0f1813fdda5a7f13eeff830efdb)
- Refactored malloc and fbarray tests to improve readability and add new test scenarios.
  ↳ No PR: [7fa0e21](https://github.com/DPDK/dpdk/commit/7fa0e212a464d5df12626764ceff6d14a1346d64), [371dd82](https://github.com/DPDK/dpdk/commit/371dd829af3637b06835d07a92241bd30576fc56)
- Fixed AAD offset calculation error in AES-GCM encryption test.
  ↳ No PR: [7c52aea](https://github.com/DPDK/dpdk/commit/7c52aea4e68e0cacc7e41ff08fcddbd513ad7e0a)
- Fixed race condition in per-lcore tests, using atomic variables to synchronize worker threads.
  ↳ No PR: [7c37826](https://github.com/DPDK/dpdk/commit/7c37826c2b87966f3b11b2c74dc720fcc1e0e6f5)
- Fixed a null pointer dereference issue caused by memory allocation failure in eventdev atomic test.
  ↳ No PR: [a6b1b95](https://github.com/DPDK/dpdk/commit/a6b1b95ce4082da3c40f02fdea16f4864355ab8b)
- Fixed an issue where the graph automatic test failed when running for the second time because the node name already existed.
  ↳ No PR: [98cf04b](https://github.com/DPDK/dpdk/commit/98cf04bb903859a3ae778b03e6b17cc0a975104e)
- Fixed return value handling for negative test scenarios in RSA tests.
  ↳ No PR: [cae5a65](https://github.com/DPDK/dpdk/commit/cae5a65a76ee69c32afe518a5e477a4fffa8ae63)
- Intel uncore power management test initialization failure is marked as skipped instead of failed.
  ↳ No PR: [0f25bcf](https://github.com/DPDK/dpdk/commit/0f25bcff93a36913214f41e27744e8c36b0904fd)
- Added dequeue timeout in encryption tests to support longer implementations.
  ↳ No PR: [8e52102](https://github.com/DPDK/dpdk/commit/8e5210215bda80d19c840756b26e841e30407c55)
- Improved the robustness of the test_multi_alloc_statistics test case, using the new malloc heap and adding cleanup logic.
  ↳ No PR: [7777215](https://github.com/DPDK/dpdk/commit/7777215715d475b5e884179de39ff4bc6b8cbf72)
- Added single operation check in cryptographic performance testing tool to avoid infinite loops.
  ↳ No PR: [d2fd236](https://github.com/DPDK/dpdk/commit/d2fd236416b4c5bb20499e1d6dee204538537160)
- Added port_control test suite and corresponding API documentation.
  ↳ No PR: [054083f](https://github.com/DPDK/dpdk/commit/054083f73baf945a745722b24eccbf2b9d1caff2)
- Disabled PMU tests reporting platform failures pending a fix.
  ↳ No PR: [98bfa43](https://github.com/DPDK/dpdk/commit/98bfa438ca7f80baf155636364377be72b4c75dc)
- Disabled event_vector_adapter automatic test as it failed to trigger or failed randomly in CI.
  ↳ No PR: [0eb86b4](https://github.com/DPDK/dpdk/commit/0eb86b4533d40bcd703972421b9a201c02f37f8a), [936ebef](https://github.com/DPDK/dpdk/commit/936ebef5ab4ae0f5b3dc564c8c202d3cd1886ce3)
- Fixed the timeout problem in the event vector adapter test, changed the waiting method to the service core cycle and added event type checking.
  ↳ No PR: [2eca0f4](https://github.com/DPDK/dpdk/commit/2eca0f4cd5daf6cd54b8705f6f76f3003c923912)
- Added test vector support for ECDH group 19, 20 and 21 in encryption tests.
  ↳ No PR: [d135d7c](https://github.com/DPDK/dpdk/commit/d135d7c87903c8e193140e3aaa1af5b1708ebed9)
- Removed unsupported test cases from JSON configuration files for encryption performance tests.
  ↳ No PR: [845a1d2](https://github.com/DPDK/dpdk/commit/845a1d2a5bf2593d591f6d2432ad02b886586035)
- Added support for RSA decryption operations in the encryption performance test application.
  ↳ No PR: [7011e85](https://github.com/DPDK/dpdk/commit/7011e8571fd8a8ccbc29a41a065b0fed92178637)
- Added test cases for repeated argument handling for argparse.
  ↳ No PR: [a4bb25b](https://github.com/DPDK/dpdk/commit/a4bb25ba661db619d70c3d20088c8f6a6ad1694f)
- Fixed the authentication and encryption IV length issue in test cases, adjusting the maximum IV length to 32 bytes.
  ↳ No PR: [c479e33](https://github.com/DPDK/dpdk/commit/c479e33bcf0173f08fd48269fb223e605b6caa41)
- After releasing the encryption operation, set the relevant pointers to null to avoid dangling pointers.
  ↳ No PR: [74164b5](https://github.com/DPDK/dpdk/commit/74164b5881526bffc142eb53b89d8900366222d3)
- Fixed RSA test vectors to comply with RFC 8017 requirements and uniformly use exponential key types.
  ↳ No PR: [653ef76](https://github.com/DPDK/dpdk/commit/653ef76297342061b51c208412cedd46d9c71907)
- Fixed the problem in RSA decryption verification that the verification always succeeds due to reusing the plaintext buffer, use independent buffers instead and add status checks.
  ↳ No PR: [9af3fa5](https://github.com/DPDK/dpdk/commit/9af3fa536ec23d254d15fea4ec0e58442e56409e)
- Fixed the issue where release was incorrectly sent to the entire dequeued batch when cleaning the event device application. Release is now only sent to events that failed to be dequeued.
  ↳ No PR: [c2ef482](https://github.com/DPDK/dpdk/commit/c2ef482eaa0928ee47abe71cd740456a68d88e77)

### Performance optimization
- Refactor the find_prev_n function, flatten nested loops into state machine logic, remove lookbehind and bit ignore functions, simplify the code and improve performance.
  ↳ No PR: [cad93b8](https://github.com/DPDK/dpdk/commit/cad93b832ba312200f46d663ee3fbfcc8ff52b3a)
- Optimize comparison operations and compiler hints in the mempool, replace partial verification with assertions, add likely/unlikely and __rte_assume to optimize hot paths, and refactor cache write functions to improve performance.
  ↳ No PR: [5102580](https://github.com/DPDK/dpdk/commit/5102580c6bef3dc65f06160720325d1de685c03e)
- Optimize the mlx5 network card Tx queue creation process, pass DevX object information to the creation function, and adjust the iteration order to improve memory allocation and performance.
  ↳ No PR: [6f356d3](https://github.com/DPDK/dpdk/commit/6f356d3840e647676cdf583105ca217eeb0577e0)
- Optimize the cache judgment logic when releasing sent mbufs in the Intel network card driver to avoid unnecessary rollback operations.
  ↳ No PR: [689c167](https://github.com/DPDK/dpdk/commit/689c16750ec7f68466e461b262708d43cb0fc69f)
- Remove the use of variable-length arrays in the ntnic driver and replace them with fixed-length arrays or dynamic allocation to improve code robustness.
  ↳ No PR: [2291d44](https://github.com/DPDK/dpdk/commit/2291d44b1b3ab14f48926656fc521db5ed573be0)
- Added null pointer checking of heap memory allocation results in the ntb example, preventing potential crashes and eliminating compiler warnings.
  ↳ No PR: [0c1a5ff](https://github.com/DPDK/dpdk/commit/0c1a5ff96bfca1ac513b64f081a20f4992c6fcc0)
- Fixed the issue in the DLB2 driver where the wrong cache line was dequeued and read when the CQ depth was less than or equal to 16, and the actual CQ depth calculation mask was used instead.
  ↳ No PR: [0b92203](https://github.com/DPDK/dpdk/commit/0b92203cdae06dee0626e46e62b9c34450e776d8)
- Fix QID depth xstat counter in DLB2 driver vector dequeue path.
  ↳ No PR: [9891a50](https://github.com/DPDK/dpdk/commit/9891a50af0693ffef8471fdb1fb09ff8799c39f6)
- Fixed the sampling race problem of the delay statistics library when receiving from multiple queues, added a spin lock to protect the sampling operation and correctly handled TSC wraparound.
  ↳ No PR: [4e12258](https://github.com/DPDK/dpdk/commit/4e12258d782e2511bf0d781faff23fada54ee7d8)
- Removed decryption test cases in AESNI-MB performance test configuration.
  ↳ No PR: [7218c0e](https://github.com/DPDK/dpdk/commit/7218c0ea5cb38ba2970f73ff6cae3dcccc6f0b7a)
- Added event vector adapter performance test for eventdev application.
  ↳ No PR: [063fef6](https://github.com/DPDK/dpdk/commit/063fef651e148b35b67b7de4fd8af955079673b9)
- Optimize the send and receive paths of the null network card driver, remove unnecessary parameter checks and atomic operations, and increase byte count statistics.
  ↳ No PR: [9946ba5](https://github.com/DPDK/dpdk/commit/9946ba548bf8e835edce369f0017e51d32a5540a), [47205af](https://github.com/DPDK/dpdk/commit/47205afc86b03d3ec47c64e6ab84207727878ecc)
- Optimize flow counter ID generation, improve cache access performance through batch enqueuing and pre-allocated arrays, and speed up the pool creation function.
  ↳ No PR: [f121921](https://github.com/DPDK/dpdk/commit/f121921a5e4aeb4946e63aeff58cee7ce7edb187)
- In the send callback of delay statistics, when there is no timestamp in the data packet burst, the locking and reading timestamp operations are skipped to improve performance.
  ↳ No PR: [8a59ec1](https://github.com/DPDK/dpdk/commit/8a59ec1fe088cc2998b4376808dc7728d4e31946)

### Security related
- Fixed the use-after-free vulnerability in the qede driver when cleaning up flowdir resources, and switched to safe traversal to avoid accessing released nodes.
  ↳ No PR: [ab8caba](https://github.com/DPDK/dpdk/commit/ab8caba639ee6378055b2d8518e2a97b2212c737)
- Fixed a possible buffer overflow problem in rte_pci_write_config() in the FreeBSD PCI bus driver to avoid out-of-bounds reads by limiting the copy length.
  ↳ No PR: [a221d2c](https://github.com/DPDK/dpdk/commit/a221d2ce1c3e6298d1c3b0d50638076b3f3d2dea)
- Add checking for invalid IOVA addresses in the virtio encryption driver to avoid using overflow constants.
  ↳ No PR: [18c747b](https://github.com/DPDK/dpdk/commit/18c747b1abbfa19ee6189a6ffcfea83f659e0bea)
- Add memory barriers to ice driver scheduling and configuration functions to fix speculative execution data leakage issues.
  ↳ No PR: [6323f12](https://github.com/DPDK/dpdk/commit/6323f12e497741337e35e8787c6fece0b5c966e4)
- Fixed the use-after-free problem caused by the alarm callback in EAL releasing memory without unregistering it. On both Linux and FreeBSD, the callback is unregistered first and then the interrupt handle is released.
  ↳ No PR: [d84bf0d](https://github.com/DPDK/dpdk/commit/d84bf0d9aeb474d89a412b6af8e947b16bfcb895), [cf1937a](https://github.com/DPDK/dpdk/commit/cf1937a96dcf63f6e00e3181654a845edb1fd682)
- Fixed the LDB port COS ID parameter validation logic in the DLB2 driver.
  ↳ No PR: [49b5fe1](https://github.com/DPDK/dpdk/commit/49b5fe1a6d59edb32c2bd50459ed499a794b9c91)
- Removed unnecessary memory clearing operations in multiple hardware module deletion functions to avoid false alarms from security tools.
  ↳ No PR: [7713854](https://github.com/DPDK/dpdk/commit/77138547073c6256c25cf0b4ed41adea5282eeb6), [ff0521f](https://github.com/DPDK/dpdk/commit/ff0521f4a1353242f89ca888f9de112bdf7ad8d7), [a12879c](https://github.com/DPDK/dpdk/commit/a12879c3d54a6ad973927e7cecadd77d587e3888)
- Add truncation detection in xstats name copy operation, and log warnings when strings are truncated.
  ↳ No PR: [9ef07ab](https://github.com/DPDK/dpdk/commit/9ef07abcd123607df60e972c9a34a9d31cddce23)

### Documentation
- The document announces support for AMD Solarflare X45xx series devices, including X4522 and X4542 network cards.
  ↳ No PR: [c9eef18](https://github.com/DPDK/dpdk/commit/c9eef18188bcec4e9e5f83ae00618b81d6979bac)
- Updated the version date information in the ixgbe base driver README.
  ↳ No PR: [bb66ce9](https://github.com/DPDK/dpdk/commit/bb66ce926c4a48d11d8186757ed47e2f719bb559)
- Added virtual function support instructions to the DTS documentation, including SR-IOV mode enablement and virtual function configuration steps.
  ↳ No PR: [a09b561](https://github.com/DPDK/dpdk/commit/a09b5610f615e38c009066c3556be10d9c81b6c7)
- Added a list of tested Intel platform and Intel network card combinations in the v25.07 release notes.
  ↳ No PR: [fb364dd](https://github.com/DPDK/dpdk/commit/fb364dd7968f0c4f446aa3e725f756fddf50c344)
- Reorganized and reconstructed the Intel VF driver documentation, added a new chapter on using VF with the hypermanager, and added large VF configuration instructions.
  ↳ No PR: [dc8ff12](https://github.com/DPDK/dpdk/commit/dc8ff12fe8b93a9f5434c9f78ad429c923fe5493), [77a3f28](https://github.com/DPDK/dpdk/commit/77a3f28d3ba8e03565cf627e54ac816027aa7253), [627edce](https://github.com/DPDK/dpdk/commit/627edcef93ddef43f1f0012433897d1038b2f0b1)
- Updated Mellanox driver documentation, simplified the device list, restructured the document structure and added testpmd command examples.
  ↳ No PR: [bdb6a7a](https://github.com/DPDK/dpdk/commit/bdb6a7aebe7a041171128a76582f82f6fc701031), [ca7afc1](https://github.com/DPDK/dpdk/commit/ca7afc1e0414842c709584882e81b483340ed551), [f6e3473](https://github.com/DPDK/dpdk/commit/f6e3473724e7ce31103fa0ecad62b282ec8e7090)
- Updated DTS documentation, added port statistics test suite instructions, improved port processing instructions and supplemented test suite configuration instructions.
  ↳ No PR: [d23083d](https://github.com/DPDK/dpdk/commit/d23083df08114975987753a887f1d1deed387ce2), [4cef16f](https://github.com/DPDK/dpdk/commit/4cef16f1f0a41ecac06a2868e90d73ffe7b14ac0), [318797b](https://github.com/DPDK/dpdk/commit/318797bfcd21d920c3ff602473c6fe2005b54b59)
- Updated cnxk crypto driver documentation to add support for CN20K SoC.
  ↳ No PR: [477bc11](https://github.com/DPDK/dpdk/commit/477bc11c2bca733361b939638c4d88d02c28ba19)
- Add entry in release notes for EAL -l parameter support for full core-to-cpu mapping.
  ↳ No PR: [ff06bdc](https://github.com/DPDK/dpdk/commit/ff06bdcbdcb051657a9670e3de6a10fcea425620)
- Rewritten and expanded the glossary, adding multiple term definitions and reference links, and adding large page entries.
  ↳ No PR: [cf2a7f0](https://github.com/DPDK/dpdk/commit/cf2a7f07f53b539862343c5e4f15facd925cc333)
- Added test suite documentation for packet capture framework.
  ↳ No PR: [f104a14](https://github.com/DPDK/dpdk/commit/f104a14b94a210a985b56e793e3700f7897895ea)
- Reduce the index depth of multiple guide documents from level two or three to level one to improve browsing experience.
  ↳ No PR: [dbeb8ae](https://github.com/DPDK/dpdk/commit/dbeb8ae8d09387bd525353f4a5aa6ec152cddffa)
- Added code snippet to the example to reroute packets directly to the kernel, and support port promiscuity/stream isolation mode and stream configuration.
  ↳ No PR: [19154c5](https://github.com/DPDK/dpdk/commit/19154c548d15cfa4928fcfb208b381d377039519)
- Added usage example of --lcores EAL option in documentation.
  ↳ No PR: [de7d4a7](https://github.com/DPDK/dpdk/commit/de7d4a7a657b22a366caa2e14723cd03d40bdb7c)
- Add parameter usage instructions to the crypto-perf tool documentation to avoid segfaults caused by scatter gather buffer list initialization issues.
  ↳ No PR: [7d24d0d](https://github.com/DPDK/dpdk/commit/7d24d0db8869287d219562a636ceba3d39bb5dd5)
- Added feature matrix tables for DMA adapters and event vector adapters in the documentation.
  ↳ No PR: [0f13711](https://github.com/DPDK/dpdk/commit/0f13711244c242801b5a89ed2b5014a3b5973bc8)
- Added documentation for the service core list flag -S, covering EAL parameter documentation and usage instructions.
  ↳ No PR: [748ad14](https://github.com/DPDK/dpdk/commit/748ad1466e50d33908c1bee5ea52f02752c7263d), [39f537e](https://github.com/DPDK/dpdk/commit/39f537efd8bc8f86c8a4e667328ab3b4c6cf4b2d)
- Added documentation for RTE Flow API test suite in DTS documentation.
  ↳ No PR: [2f8d320](https://github.com/DPDK/dpdk/commit/2f8d3203fe94593362e3be61f8bdf488f6ee484e)
- Added note to the Linux guide that CPU 0 cannot be completely isolated and it is recommended to avoid running DPDK polling applications on this core.
  ↳ No PR: [716893e](https://github.com/DPDK/dpdk/commit/716893ec1abe2795e82f342e3254e1ba54f7e2b6)
- Removed the no longer required -n 4 memory channel option from documentation examples, and updated related descriptions.
  ↳ No PR: [497ffbd](https://github.com/DPDK/dpdk/commit/497ffbd563357152e8879f0174b4dd4a7d90667d)
- Removed reference to the deprecated --use-device option from the Linux and FreeBSD Getting Started documentation.
  ↳ No PR: [674908c](https://github.com/DPDK/dpdk/commit/674908ce49f875cd3411bedd0d2c45cd73dd7e2f)
- In the sample application documentation, the detailed enumeration of some EAL parameters has been replaced with a generic description and the complete list has been quoted instead.
  ↳ No PR: [e295204](https://github.com/DPDK/dpdk/commit/e295204db382c78db3494240118e43578eaa8159)
- Update i40e and ice network card driver documentation, add the recommended kernel driver and firmware version corresponding to DPDK 25.07, and expand the list of controllers supported by ice network card.
  ↳ No PR: [b277483](https://github.com/DPDK/dpdk/commit/b27748311e9f6e4a5d68d94bb6e3b28207226e40)

### Build/CI
- The build system now forces checking of assertion expressions at compile time, even if assertion functionality is disabled, to catch compilation warnings early.
  ↳ No PR: [1e3f063](https://github.com/DPDK/dpdk/commit/1e3f0632979104370e54206911209f0792f6bd44)
- Added universal AVX2 and AVX512 source file processing support for driver building, simplifying driver building logic.
  ↳ No PR: [d6cb19c](https://github.com/DPDK/dpdk/commit/d6cb19c18a24f18fe6da8e175786bd1940d4219b), [c29e728](https://github.com/DPDK/dpdk/commit/c29e728c645358e90c23fd483a043386d4617cd1), [469a556](https://github.com/DPDK/dpdk/commit/469a556f1c9ebf8c753e493922357806777c2f9d)
- Added common AVX2 and AVX512 build processing logic to the top-level library build file to support separate compilation for specific source files, simplifying library construction.
  ↳ No PR: [ad20bed](https://github.com/DPDK/dpdk/commit/ad20bedc9a0c8392b702c142021e03e999f7f931)
- Removed custom AVX2 and AVX-512 compilation logic in the build of the ACL library and instead uses the common AVX build processing method.
  ↳ No PR: [defa5d5](https://github.com/DPDK/dpdk/commit/defa5d5e38e3e41999463dfc8f2a7dd6dd457c7e)
- Unify the AVX512 build logic of the member library to use a common build processing method.
  ↳ No PR: [edd3f4b](https://github.com/DPDK/dpdk/commit/edd3f4b1265e6da707c46ca9b6c39d332647baea)
- Skip checking for atomic operations on the drivers/common/cnxk directory in the check script to allow use of GCC built-in atomic functions.
  ↳ No PR: [0f1faed](https://github.com/DPDK/dpdk/commit/0f1faed2c4dcaab44cc5029e5659387965828588)
- Fixed build failure in dlopen link mode on Linux due to missing internal EAL include directories.
  ↳ No PR: [8ee74a6](https://github.com/DPDK/dpdk/commit/8ee74a69abcf48563f05adeafecd298bb03477a8)
- Fixed the mlx5 driver compilation and link error on Windows, incorporated mlx5_flow_geneve.c into all platform compilations, and sorted out the order of meson.build files.
  ↳ No PR: [4031a5f](https://github.com/DPDK/dpdk/commit/4031a5f261754ad5d4125e84888316d0678f43e7)
- Fixed the problem that the pmdinfogen temporary directory on Windows could not be cleaned due to sharing conflicts, and adjusted the parameter passing method of the pmdinfo command.
  ↳ No PR: [243abeb](https://github.com/DPDK/dpdk/commit/243abeb40b4fd65d6fd3cdbc71a9c9410c8a7508)
- Fixed a build error caused by variable scope issues when developer mode was disabled, and moved the import of the fs module before conditional judgment.
  ↳ No PR: [2bf836d](https://github.com/DPDK/dpdk/commit/2bf836de46d36a81f9321f947fbfce52b3180782)
- Unified the compilation conditions of AVX code, removed specific macro definitions, and replaced them with general architecture or AVX supported macros.
  ↳ No PR: [6a64f40](https://github.com/DPDK/dpdk/commit/6a64f40356eca976499db1d152b96391a3ec1e92), [ac93dc0](https://github.com/DPDK/dpdk/commit/ac93dc018a3a089a60b12d95efcd0cee58c8bc7d), [7ae40e5](https://github.com/DPDK/dpdk/commit/7ae40e5bcab5fffd116c97a3fa57ff8e75f90c79)
- Change the installation path of API documentation and guide documents to independent subdirectories to avoid overwriting.
  ↳ No PR: [79f8422](https://github.com/DPDK/dpdk/commit/79f8422c84b20357b7d1ec43a474481554726114)
- Disable use of compiler pragma in patch check scripts, and allow use of rte_common.h.
  ↳ No PR: [ad9b50d](https://github.com/DPDK/dpdk/commit/ad9b50dc15b17b806e6ed981be4e961eb510158e)
- Removed static version mapping files, and updated SPDX tag checking script to no longer ignore .map files.
  ↳ No PR: [7c3bd0d](https://github.com/DPDK/dpdk/commit/7c3bd0d3d076b4b351ec773163a326d978434d91)
- Fixed the make clean goal of examples/flow_filtering so that it can delete .o files in the build directory.
  ↳ No PR: [ab79c1b](https://github.com/DPDK/dpdk/commit/ab79c1ba245646055cac3a3c6ec3544b217c6751)
- Enable warnings as errors in MSVC builds in GitHub Actions.
  ↳ No PR: [10f4134](https://github.com/DPDK/dpdk/commit/10f413485518e1c4321591af8526f97258d291cb)
- Added note in build configuration for Windows-specific Meson version requirements.
  ↳ No PR: [6890ee7](https://github.com/DPDK/dpdk/commit/6890ee7ba76e92745d6c61b3b6b9d757ebaaa89d)

### Maintenance
- Updated PHY configuration and MAC MCU settings of RTL8127.
  ↳ No PR: [d458c9f](https://github.com/DPDK/dpdk/commit/d458c9f52e97795bc485458dbfff0823fafcc486)
- Fixed indentation problem in ixgbe_set_tx_function function.
  ↳ No PR: [5a7d607](https://github.com/DPDK/dpdk/commit/5a7d607748c2d4c59c8a7b4747ade69096846497)
- Add missing newlines at the end of the meson.build file to comply with text file specifications.
  ↳ No PR: [4a1f110](https://github.com/DPDK/dpdk/commit/4a1f110b2e7aef516859a2d8797e2ee184573f00)
- Add debug log and cache validity check for mlx5 driven ipool module.
  ↳ No PR: [0b03383](https://github.com/DPDK/dpdk/commit/0b03383f65a394477775cc8d3e68ea15beb3d587), [3a2bda3](https://github.com/DPDK/dpdk/commit/3a2bda3635d41c3842064b353ca5b242958cec5e)
- Enhanced null pointer checking and assertion, and adjusted the order of variable declaration.
  ↳ No PR: [66b065e](https://github.com/DPDK/dpdk/commit/66b065efa5baded3273e3dab8cd0fffd36e31f7b)
- Fixed compilation warnings and comment typos in the fm10k base code.
  ↳ No PR: [48fc518](https://github.com/DPDK/dpdk/commit/48fc5188aa753824a4bd469f9c482e845404c963)
- Count the number of packets and bytes sent and received in all queues in the null network driver, and remove the inherited igb prefix.
  ↳ No PR: [31326ce](https://github.com/DPDK/dpdk/commit/31326ce7f15143cda3d3ca27148c85e8ad8d0ece)
- Add error logging for HSH RCP preset failure in the hw_db_inline_hsh_deref function.
  ↳ No PR: [4289155](https://github.com/DPDK/dpdk/commit/428915542e1b8df862db757c2da6e8497c043729)
- Fixed the error reason variable recorded in the log when madvise() fails in eal_mem_set_dump().
  ↳ No PR: [58d5d5e](https://github.com/DPDK/dpdk/commit/58d5d5e8269055b6bb11b18fb5897fee3fa73363)
- Add license checking step in CI workflow.
  ↳ No PR: [224ea1c](https://github.com/DPDK/dpdk/commit/224ea1c30dc64274fa2abdb48823f80649bdac52)
- Removed unused variables and related memset calls to eliminate PVS Studio warnings.
  ↳ No PR: [bbf9ce4](https://github.com/DPDK/dpdk/commit/bbf9ce4a67792072a56a0f327b189e0dae8d8a6b)
- Update the steward rule message processing of the CN20K platform to use the dedicated cn20k message type.
  ↳ No PR: [3f74e33](https://github.com/DPDK/dpdk/commit/3f74e337caf2f60bfecea03a7436ed829cd9e5c0)
- Unify and correct log format specifiers to match the actual data type of the variable.
  ↳ No PR: [a3151e2](https://github.com/DPDK/dpdk/commit/a3151e201ec434350054e44e98fdd8c22545093f)
- Add debug printout for management interface in ixgbe base driver.
  ↳ No PR: [12648d0](https://github.com/DPDK/dpdk/commit/12648d0a5afc0862cda79bb7ace672da5713332e)
- Remove unnecessary platform check macros in ixgbe driver and adjust related data structure fields.
  ↳ No PR: [0a76750](https://github.com/DPDK/dpdk/commit/0a76750c72f5e9bf367cfec9c609de38d6720133)
- Reuse the precomputed desc_per_entry value in the ENA driver to avoid repeated calculations on the fast path.
  ↳ No PR: [ab8ca42](https://github.com/DPDK/dpdk/commit/ab8ca426ebdb6acfde21b0386bf7c8d5d9c6bde1)
- Upgrade the ENA network card driver version from 2.12.0 to 2.13.0.
  ↳ No PR: [ca91e72](https://github.com/DPDK/dpdk/commit/ca91e725393ba3905e5ec36a98fc94bf4280afd5)

### Others
- Improved the commit log prefix checking script so that it displays the expected correct prefix when prompted with a prefix error.
  ↳ No PR: [2f4cd1b](https://github.com/DPDK/dpdk/commit/2f4cd1b4dbaec6633da510da67c2213cfd2bd359)
- Removed unused local variables in test functions to eliminate compiler warnings.
  ↳ No PR: [cbdc9e3](https://github.com/DPDK/dpdk/commit/cbdc9e39ced647e2d3bcbc8fe3a9bafff0b45152)
- Added API documentation for ShellPool class.
  ↳ No PR: [3a56213](https://github.com/DPDK/dpdk/commit/3a562133fcf5f9f3fcf8719a9d6b9bb9545fa001)
- Removed outdated advice on local variable declarations from the coding style documentation.
  ↳ No PR: [80b2e5f](https://github.com/DPDK/dpdk/commit/80b2e5fcf7627d97f71c460922aebbe04e3b7aac)
- Unify the function parameter types in the test file from unsigned to unsigned int.
  ↳ No PR: [7af04d2](https://github.com/DPDK/dpdk/commit/7af04d243b878bfacff217a42eb798faac58eb06)
- Optimized the output format of the memory pool performance test, adjusted the parameter order and display width.
  ↳ No PR: [9374e58](https://github.com/DPDK/dpdk/commit/9374e580dc091d3c282c676fd909a32d2bb1de02)
- Removed the Known Issues section from the Release Notes document and moved the related content to bugzilla.
  ↳ No PR: [bc9f633](https://github.com/DPDK/dpdk/commit/bc9f63350b1b860179e82f17b55188aa6215c15d)
- Added recommendations on the frequency and quantity of patch submissions to the contribution guide.
  ↳ No PR: [7a527ec](https://github.com/DPDK/dpdk/commit/7a527ecd2eda2eedaaea8ed6d09ebb87294c9ab9)
- Fixed typos in variable names, renamed alloced_size and num_queues_alloced to their full forms.
  ↳ No PR: [a023765](https://github.com/DPDK/dpdk/commit/a0237654363440f19b99cd73ed67f22184560170)
- Removed unnecessary void type conversions in multiple memset calls in the net/ntnic driver.
  ↳ No PR: [53f6313](https://github.com/DPDK/dpdk/commit/53f63132f2eabdcf6f58d64b0deb7ab7258af51f)
- Fixed typo in E825-C device ID 0x579F description, correcting 1GbE to 10GbE.
  ↳ No PR: [e54cf1f](https://github.com/DPDK/dpdk/commit/e54cf1fec8517f9ec1ec6bdca6fd9e6b0dd2c307)
- Updated the snapshot date in the ice base code README to 2025-05-23.
  ↳ No PR: [4e2007b](https://github.com/DPDK/dpdk/commit/4e2007be532646ff432394478163170728575c88)
- Updated the copyright year and snapshot generation date in the e1000 base driver code README.
  ↳ No PR: [31e3b65](https://github.com/DPDK/dpdk/commit/31e3b6595e8dff2148bac165dfe2c4198a79bd07)
- Fixed message parameter in EdDSA 25519PH test vector description, corrected from 1 to 3.
  ↳ No PR: [9f45766](https://github.com/DPDK/dpdk/commit/9f45766699f0dc066ee4dc5908a9c9e8bdc46e8c)
- Adjusted local variable declaration order in ena driver to follow reverse Christmas tree style.
  ↳ No PR: [e229d1c](https://github.com/DPDK/dpdk/commit/e229d1c4d16dec5ec024bf92a5878df1d6c0772f)
- Removed references to NVIDIA's acquisition of Mellanox in multiple documents.
  ↳ No PR: [20a053a](https://github.com/DPDK/dpdk/commit/20a053a223db35244b6daee98d71fdab631646b6)
- Updated the 25.07 release notes document to remove comments and single-line list items.
  ↳ No PR: [f6965da](https://github.com/DPDK/dpdk/commit/f6965da493135a5af3a6369da2a1190196d846cc)
