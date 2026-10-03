# Release Note

## Important Changes

### Driver Layer (PMDs)
- The allocation timing of pop_vlan, send_to_kernel, NAT64 and default miss actions in the HWS driver is changed from port initialization or flow configuration to on-demand delayed allocation when first used, and is changed to allocation by domain to reduce firmware resource usage. (Architecture-related: HWS action allocation strategy)
  ↳ No PR: [f7ba302](https://github.com/DPDK/dpdk/commit/f7ba30204cb90408e5a721b4f552734e1bd155d0), [531ae0a](https://github.com/DPDK/dpdk/commit/531ae0a847cd4b8335e5aea37d96a5c997fe2c3c), [de59f25](https://github.com/DPDK/dpdk/commit/de59f25b6f90e13e14330d4d18dc59f4d5ecdfe2), [b4e6123](https://github.com/DPDK/dpdk/commit/b4e61239f8291d3005438c38111e69a9bca8dce4)
- Unify the Rx path selection infrastructure driven by Intel network card and make it consistent with the Tx side, including simplifying the feature structure, optimizing the selection logic and adjusting the function initialization timing. (Architecture-related: Rx path selection infrastructure)
  ↳ No PR: [7644bb1](https://github.com/DPDK/dpdk/commit/7644bb1d2f0a2e77b36ded43f275c6e5cac44a5f), [2e97d51](https://github.com/DPDK/dpdk/commit/2e97d51b5572a58de348cf3524012aa7391c70bf)
- Introduce a unified Tx descriptor structure for i40e, iavf, ice and idpf drivers, and unify ring pointers and field definitions. (Architecture-related: Tx descriptor structure unification)
  ↳ No PR: [ab4c1b2](https://github.com/DPDK/dpdk/commit/ab4c1b28662ece4d0378df7e1645d6a3009aba3c), [c638927](https://github.com/DPDK/dpdk/commit/c6389278fcf2f7e21e999c11517532fb31ebaf5d), [ece72e7](https://github.com/DPDK/dpdk/commit/ece72e755ec5dd2d2761a128759609cf70ba24ff)
- Complete the merging of Intel network card driver scalar sending paths, create a common checksum function and extract the common Tx auxiliary function. (Architecture-related: scalar sending path merging)
  ↳ No PR: [d9550ce](https://github.com/DPDK/dpdk/commit/d9550ce576a7def03efb4e70fb865c2bab355b85), [e72c501](https://github.com/DPDK/dpdk/commit/e72c501cfa7896b4ac75bf47e7b572f72452ddfd), [285d92b](https://github.com/DPDK/dpdk/commit/285d92bdacc89b0125d67039343316f979d74e61)
- Introduce an independent descriptor status tracking mechanism based on RS threshold bucket for Intel network card driver, and force tx_rs_thresh to be a power of 2. (Architecture-related: descriptor status tracking mechanism)
  ↳ No PR: [8f4396b](https://github.com/DPDK/dpdk/commit/8f4396b9f63c4bf7b48b314f29b0d051cc5417cf)
- Decouple hash (RSS) de-initialization and parser de-initialization, and remove RSS configuration separately during the device shutdown process. (Architecture-related: RSS de-initialization decoupling)
  ↳ No PR: [388acb4](https://github.com/DPDK/dpdk/commit/388acb4f62011348c5d3a460e061cc0e1427cdbc)
- The TAP network card driver changes the receive and send queues from static embedded structures to dynamic allocation when the queue is set up, and is released when the queue is released and the device is closed. (Architecture-related: TAP driver queue dynamic allocation)
  ↳ No PR: [23e2387](https://github.com/DPDK/dpdk/commit/23e2387b49a13e0acb7b83cf536a6e034cc61185)
- In order to support the new SPx series network cards, the command queue is reconstructed and split into two sets of old and new implementations. (Architecture-related: Command queue reconstruction)
  ↳ No PR: [aa31be3](https://github.com/DPDK/dpdk/commit/aa31be38544ebe55737052a0091fca727f39e5bd), [9204b6b](https://github.com/DPDK/dpdk/commit/9204b6b7bb1a0e74cd93979198823e0f1ec48960)
- Unify the Tx path selection logic of Intel network card driver (iavf, idpf, cpfl), introduce public infrastructure and simplify path selection. (Architecture-related: public data path)
  ↳ No PR: [ebcfb03](https://github.com/DPDK/dpdk/commit/ebcfb039afa896d6fd3a6ff6daae140e622ac43b), [7cab7e6](https://github.com/DPDK/dpdk/commit/7cab7e67363a634b7701034cbeb6e97acb542112), [6970745](https://github.com/DPDK/dpdk/commit/6970745698b962fbd8463313c77c312c4cf40c9f), [01cf94d](https://github.com/DPDK/dpdk/commit/01cf94df9dce75bfd55ed1f110ab0c4893a28e2e), [995317a](https://github.com/DPDK/dpdk/commit/995317adacee743db0a603801d74c19ce9475bfe), [a1b6569](https://github.com/DPDK/dpdk/commit/a1b6569433487701dcaa4deff540272b5824f330), [55d1638](https://github.com/DPDK/dpdk/commit/55d16387ec85153a34e999ced31c601b9e70a6db), [102d4e9](https://github.com/DPDK/dpdk/commit/102d4e9c69869496be41d24792bc95304b2e79db), [df21892](https://github.com/DPDK/dpdk/commit/df218928e11a90ba1716bc9eb24893770a860362), [2e4b5ef](https://github.com/DPDK/dpdk/commit/2e4b5ef050039cf6136deb6b66efc8d98a0c7621)
- Support CUDA 13.0, adapting the function pointer declaration of the new API through conditional compilation. (Architecture-related: platform compatibility)
  ↳ No PR: [cd60dcd](https://github.com/DPDK/dpdk/commit/cd60dcd503b91956f966a1f6d595b35d256ac00f)
- Define the pause mode capability mask in the public header file for client drivers to use for flow control settings. (Architecture-related: public API)
  ↳ No PR: [69123fb](https://github.com/DPDK/dpdk/commit/69123fbca74cc5bd7bb7105313305d14c493c99e)
- Added private API for RSS TIR registration and release in mlx5 PMD. (Architecture-related: public API)
  ↳ No PR: [9ec0c6b](https://github.com/DPDK/dpdk/commit/9ec0c6bda04a776f5bb0bea7791d68310cdb8590)
- Added the function of registering VF pre-reset and post-reset callbacks for the IAVF driver. (Architecture-related: public API)
  ↳ No PR: [a42b8d6](https://github.com/DPDK/dpdk/commit/a42b8d60b6d90289a42da6da97b3f6223a889690)
- Support configurable queue depth (512 to 32768), set by rx_nb_desc and tx_nb_desc, and reconstruct the queue configuration and initialization process to adapt to dynamic depth. (Architecture-related: Queue depth configuration)
  ↳ No PR: [05da61f](https://github.com/DPDK/dpdk/commit/05da61f9b3984f8e16d3735e71e8b78385d3ea9c)
- Add link speed configuration and auto-negotiation status query functions to the zxdh network card driver. (Architecture-related: link speed configuration)
  ↳ No PR: [3db787f](https://github.com/DPDK/dpdk/commit/3db787f6f5d60391a69e9432887b6526b17b6872)
- Supports DPDK multi-process architecture, the main process has complete control, and the slave process only supports limited operations such as statistical query and device information query. (Architecture-related: multi-process architecture)
  ↳ No PR: [360b1d0](https://github.com/DPDK/dpdk/commit/360b1d0a89cdc1d2af8363bb15e96bfc13eee1a1)
- Fix the resource release problem in the net/nfb driver, ensure that the resources allocated during initialization are correctly released in eth_dev_uninit, and add MTU setting support. (Architecture-related: MTU setting support)
  ↳ No PR: [9395b64](https://github.com/DPDK/dpdk/commit/9395b64a47be63fc74a02d6ad9aeb5979c385d43)
- Add IPsec offload hook for iavf driver in general Tx function, and ensure no performance impact on drivers that do not support IPsec through compile-time constant optimization. (Architecture-related: IPsec offload hook)
  ↳ No PR: [fd1e645](https://github.com/DPDK/dpdk/commit/fd1e6458b3d21ff5b71d2826ff7428a55866518a)
- Make VLAN tag insertion logic configurable, add a new enumeration type to choose to put VLAN tags into data descriptors or context descriptors. (Architecture-related: VLAN tag configuration)
  ↳ No PR: [6ea6d67](https://github.com/DPDK/dpdk/commit/6ea6d67bebfe86feefa5ffe1fabcf8dfe77f87df)
- Add support for RTL8168KD chip, enabling network speed up to 1Gbps. (Architecture-related: platform compatibility)
  ↳ No PR: [521ecb8](https://github.com/DPDK/dpdk/commit/521ecb813a9dd850f73854b12cf231271cf3c011)
- Adjust the jumbo frame size limit for non-Gigabit network cards, set the maximum size to 16K-1 for RTL8125A, and add support for RTL9151A and RTL8125K models. (Architecture-related: platform compatibility)
  ↳ No PR: [12f2bde](https://github.com/DPDK/dpdk/commit/12f2bde32ba73626d4a4bd0f76794b1eb588d34a)
- Added support for RTL9151A network card chip, enabling it to support 2.5Gbps network speed. (Architecture-related: platform compatibility)
  ↳ No PR: [7acd732](https://github.com/DPDK/dpdk/commit/7acd73204fa99f1bbfe62ef84ca6c459e7f6d365)
- Support RTL8125K network device, maximum rate 2.5Gbps. (Architecture-related: platform compatibility)
  ↳ No PR: [e0373ea](https://github.com/DPDK/dpdk/commit/e0373eac0dcb290b50911609b2fcaf16f5a02405)
- Add indirect queue mapping support to the NFB driver, add a queue mapping array and adjust queue settings and initialization functions, while adding firmware version and FEC acquisition functions. (Architecture-related: public API)
  ↳ No PR: [456d405](https://github.com/DPDK/dpdk/commit/456d405b83cc57648dd70272dcacf04637bb99d6)
- Change the NFB network card driver to create an ethdev for each Ethernet port based on firmware port information, and add FEC acquisition and setting support. (Architecture-related: public API)
  ↳ No PR: [9b50175](https://github.com/DPDK/dpdk/commit/9b50175259b83494b3a001ff3a821b82d726574e)
- Added a new port parameter to the NFB network device driver, which supports specifying ports multiple times. If not specified, all ports will be used by default. (Architecture-related: driver configuration interface)
  ↳ No PR: [afd9ad9](https://github.com/DPDK/dpdk/commit/afd9ad923ad253aa505ddcabdc99d5fca7cfcd40)
- Add PDB support for IPsec paths, covering inline inbound and outbound directions. (Architecture-related: IPsec PDB support)
  ↳ No PR: [16e9536](https://github.com/DPDK/dpdk/commit/16e9536e81f61a3d5bb786981d66d3842102c80a), [4644841](https://github.com/DPDK/dpdk/commit/46448417ac5cf4e82258c69cdbc2806268fca182)
- Add Out-Of-Place secure reassembly support to the CN20k platform, including reassembly path adaptation and Rx fast path processing. (Architecture-related: CN20k OOP secure reassembly)
  ↳ No PR: [0bbf010](https://github.com/DPDK/dpdk/commit/0bbf0102d20c514eb1f13101bbfccfa73d738c8a), [9f13f3d](https://github.com/DPDK/dpdk/commit/9f13f3d0691a192cca2eaafbf861b1949174d1d1)
- Add L2TPv2 tunnel support to the ice network card driver, including data structure definition, protocol identifier, flow pattern matching and packet generation. (Architecture-related: L2TPv2 tunnel support)
  ↳ No PR: [d1f8553](https://github.com/DPDK/dpdk/commit/d1f8553d5d7ea36f9bf81f156de25bf230fea240), [5a6292d](https://github.com/DPDK/dpdk/commit/5a6292de5fd8016f7cb12e6905385dea161811f7), [04aa030](https://github.com/DPDK/dpdk/commit/04aa030bcb96d2df0fed18bce115016c0f524b8b), [a4bd231](https://github.com/DPDK/dpdk/commit/a4bd231eaaae3caaed1146de923dccc888d115c3), [733640d](https://github.com/DPDK/dpdk/commit/733640dae75e4edb1aaefc4150cbb9cac4303cdb), [512e4d4](https://github.com/DPDK/dpdk/commit/512e4d428ca648f94cbeda78ffea54e4da639340)
- The idpf driver adds PTP time synchronization support, including basic operation codes, PTP message processing, clock operations and sending timestamps. (Architecture-related: public API)
  ↳ No PR: [3e17556](https://github.com/DPDK/dpdk/commit/3e175561a4fc21d4b94ed76cbb2e5caf1543658c), [cdf4b9d](https://github.com/DPDK/dpdk/commit/cdf4b9ded461af79e9cd3f8ffeab97548cd0077e), [1c6e273](https://github.com/DPDK/dpdk/commit/1c6e2737fd3e43b57f0502f11ca70066b6703157)
- The IDPF driver adds AVX2 vectorized split queue receive and send paths to provide support for CPUs that do not support AVX512. (Architecture-related: platform compatibility)
  ↳ No PR: [1f065f9](https://github.com/DPDK/dpdk/commit/1f065f9d75ff7319be31618c45670406306268af), [57560a9](https://github.com/DPDK/dpdk/commit/57560a92167a96952e32387a76a02e947cdd3cc0)
- Unify the naming of queue statistics fields of TAP PMD, and add MAC address filtering function. (Architecture-related: public API)
  ↳ No PR: [0d3ba14](https://github.com/DPDK/dpdk/commit/0d3ba143e440ac532d32d11b5b2499ac486c3ef8)
- Added a function to convert the HWS table type to the corresponding action flag, supporting root tables and non-root tables. (Architecture-related: public API)
  ↳ No PR: [b21abc5](https://github.com/DPDK/dpdk/commit/b21abc51b80c66a4d9519111860270c61d705d37)
- Add IPsec receive injection support to the CN20K platform, including injection configuration and receive injection processing function. (Architecture-related: public API)
  ↳ No PR: [1b8326b](https://github.com/DPDK/dpdk/commit/1b8326be5abb38a2757b96615d96d3aeaa0d38a9)
- Added Packet Buffering (PB) and Work Queue Element (WQE) cache configuration options for Receive Queue (RQ). (Architecture-related: public API)
  ↳ No PR: [4309761](https://github.com/DPDK/dpdk/commit/4309761d85b66f010264ad442c632378c57c3c5f), [4d3de9c](https://github.com/DPDK/dpdk/commit/4d3de9c4cf2c2b388acd0a61026e62e361d67f54)
- Update flow rules to support out-of-place IPsec session configuration. (Architecture-related: public API)
  ↳ No PR: [c61cba3](https://github.com/DPDK/dpdk/commit/c61cba3eab9728b35b09d6feb6d7dba4f4dc6bbb)
- Add flow steering functionality to the GVE driver, including device options, extended management commands, flow rule configuration and rte_flow API support. (Architecture-related: public API)
  ↳ No PR: [9c149ff](https://github.com/DPDK/dpdk/commit/9c149ff88b2f76be134171e4cc14ca3c6fb27965), [88fff20](https://github.com/DPDK/dpdk/commit/88fff203be36234261e968eb6fb7844c03d0ca54), [4cbb6fd](https://github.com/DPDK/dpdk/commit/4cbb6fd9f84baccfda2a11cb8cc660ae9331c16b), [82ef40f](https://github.com/DPDK/dpdk/commit/82ef40fb2e7eaf452b1b8c9d7bdbad670ee6bc3a)
- Add support for Huawei SPx series new network cards to the hinic3 driver, including device ID, compact CQE mode and transceiver path processing. (Architecture-related: platform compatibility)
  ↳ No PR: [8843a7a](https://github.com/DPDK/dpdk/commit/8843a7a6bca542a06050468966d0cca7f73c82ea), [c1537bf](https://github.com/DPDK/dpdk/commit/c1537bf6c03309b6b8bb7060aa8b2d452b0ee414), [b20dc78](https://github.com/DPDK/dpdk/commit/b20dc78b286ab1fd8a25c0ef08659c2fb0b2ec91), [fe7ced2](https://github.com/DPDK/dpdk/commit/fe7ced2b83bc2fa0e5f9b05803eeda7ea3cd953d)
- Add HTN FDIR support to the new SPx series network cards, and reconstruct TCAM filter management, RSS, MTU, LRO and other functions. (Architecture-related: platform compatibility)
  ↳ No PR: [b2d4933](https://github.com/DPDK/dpdk/commit/b2d4933b80ec1566380d441454d2941732d71b82)
- Add software MAC address filtering function for Linux TAP devices, supporting unicast and multicast address filtering. (Architecture-related: public API)
  ↳ No PR: [213e70b](https://github.com/DPDK/dpdk/commit/213e70b3220d68c8f8cdfce9dfee705cab7156fb)
- Added devargs option drv_no_data_stashing for DPAA2 network driver, which replaces environment variables to disable data stashing. (Architecture-related: public API)
  ↳ No PR: [85fdd18](https://github.com/DPDK/dpdk/commit/85fdd181e41285bb28a082674819fefc4384c293)
- Enable LLDP filtering control function for new hardware such as E830, and add fallback logic to improve driver robustness. (Architecture-related: platform compatibility)
  ↳ No PR: [9e90c61](https://github.com/DPDK/dpdk/commit/9e90c619d41f012b32f604192141b248dbd4933f)
- Fixed the issue where the iavf driver incorrectly reports the maximum number of queues when the PF kernel driver does not support large VF, and instead reports the correct number of queues based on actual support capabilities. (Architecture-related: public API)
  ↳ No PR: [23bd0b1](https://github.com/DPDK/dpdk/commit/23bd0b1785d6b6e8c935f30fc214381794f1b299)
- Fixed the compilation warning caused by the conflict between the enumeration member name unused and the mbuf parameter, and renamed it to MLX5_UNUSED_DOMAIN_TYPE. (Architecture-related: public API)
  ↳ No PR: [2a9bcc3](https://github.com/DPDK/dpdk/commit/2a9bcc306094e721b58af4887a5a1c887afcd4f4)
- Fixed the problem of returning decrypted data when there is no padding mode in the RSA verify operation. (Architecture-related: external behavior)
  ↳ No PR: [adaf208](https://github.com/DPDK/dpdk/commit/adaf208c017724a814a08472a22908ca0a2f11b8)
- Add overflow check in the statistical name acquisition function of the ethdev library, and log an error when the name length exceeds the buffer size. (Architecture-related: public API)
  ↳ No PR: [d6600ab](https://github.com/DPDK/dpdk/commit/d6600abaceac488e69639109feb5fbafef4f81c2)
- Fixed the problem that the shared RX queue allows MTU mismatch at runtime to avoid failure of hot adding representor or runtime MTU change; at the same time, remove the redundant priv->mtu field and uniformly use dev->data->mtu to track MTU. (Architecture-related: public API)
  ↳ No PR: [aab5fcb](https://github.com/DPDK/dpdk/commit/aab5fcbd6a79954e311c91ba65f7198e7a73ca24)
- Move the internal data structure of the NFB network card driver from dev_private to process_private to support the correct initialization and uninstallation of Ethernet devices by slave processes in multi-process scenarios. (Architecture-related: multi-process support)
  ↳ No PR: [e08f7ca](https://github.com/DPDK/dpdk/commit/e08f7ca34b300e0aa0c02df6cb56d9aea60b750c)
- Fix the naming conflict between global variables and internal symbols in the mlx5 driver, add the mlx5_ prefix and change it to static to avoid link symbol conflicts. (Architecture-related: public API)
  ↳ No PR: [22438a1](https://github.com/DPDK/dpdk/commit/22438a177efd706a25792ed5ecf0cf9cd5274943), [4deb765](https://github.com/DPDK/dpdk/commit/4deb765dd2a819051c7195f2389be6e95503c0cf)
- Fixed the problem that mlx5 PMD cannot read the flow mark metadata after reconfiguring the Rx queue. Now the flow mark flag will be restored correctly when the port is started. (Architecture-related: flow mark metadata)
  ↳ No PR: [e644064](https://github.com/DPDK/dpdk/commit/e6440647436ba5011de84db8dd1bbb46e96425fe)
- Extracted TX descriptor calculation logic from multiple Intel network card drivers into public functions, and fixed the descriptor calculation error of the idpf driver in TSO scenarios. (Architecture-related: public API)
  ↳ No PR: [2904020](https://github.com/DPDK/dpdk/commit/2904020f8313b0bd6adcdd1cd522b05ec30691d0)
- Added the missing E610 MAC type check to the ixgbe driver, so that the E610 device can correctly support functions such as bypass, queue statistics mapping, VLAN extension, device startup, information acquisition, E-Tag, flow steering, L2 tunnel, VF jumbo frame and receive queue settings, and added a legality check for the receive queue ring size. (Architecture-related: public API)
  ↳ No PR: [ffac9bc](https://github.com/DPDK/dpdk/commit/ffac9bc95aa8311c1e9f2bd590a015532d31c3ad)
- Fixed the memory leak of safe streams in the ixgbe driver, added the ability to destroy safe streams, and fixed the problem of pointers still being returned when creation fails. (Architecture-related: public API)
  ↳ No PR: [590ad6c](https://github.com/DPDK/dpdk/commit/590ad6c13b37fccedc5782239feed914ee91403f)
- Fixed the pointer passing error of the ixgbe driver in the IPsec adding SA process, changed the originally incorrectly passed rte_flow_action_security container to directly pass in the security session pointer, and made the function parameter type explicit to enhance compile-time type checking. (Architecture-related: public API)
  ↳ No PR: [f82b3ed](https://github.com/DPDK/dpdk/commit/f82b3ed6abeb7a450e5bff0be76a38ee7f92f101)
- For the CN20K platform, skip writing SA operations for inline IPsec, disable this option, and follow the hardware recommended sequence for writing SA contexts. (Architecture-related: Platform compatibility)
  ↳ No PR: [e496baa](https://github.com/DPDK/dpdk/commit/e496baa476feda9ab9fa066ae90ea5fa550e0e25)
- The ability to obtain the actual link speed by reading the MDIO register has corrected the method of obtaining the link speed in the nfb network card driver. (Architecture-related: driver behavior)
  ↳ No PR: [6fdf391](https://github.com/DPDK/dpdk/commit/6fdf3914351a92704d9c74512cb76fc9a724d38b)
- Fixed the limitations of shared Rx queues: added judgment on shared Rx queues in vectorized Rx and MPRQ support checks to avoid memory leaks caused by incorrect initialization of resources, and updated related documentation. (Architecture-related: public API)
  ↳ No PR: [568857f](https://github.com/DPDK/dpdk/commit/568857f18c2ab7cb73e6fd0bf1e612a5f352af26)
- Fixed the interface name length issue in the tap driver, using the correct IFNAMSIZ instead of RTE_ETH_NAME_MAX_LEN. (architecture-related: public API)
  ↳ No PR: [0e5bbe2](https://github.com/DPDK/dpdk/commit/0e5bbe2a4b25aab4c83cf4234212a8064de18f52)
- Fixed the calculation logic of the number of hash segments in TAP PMD, changed iovecs to flexible array members, and replaced the runtime check with compile-time static_assert. (architecture-related: public API)
  ↳ No PR: [c67f595](https://github.com/DPDK/dpdk/commit/c67f59508ddbef1c0cc5832d0495da8fe11b7b7c)
- Fixed the race condition of VF add/remove events in the netvsc driver, and introduced lock protection and event attachment mechanism. (Architecture-related: VF add/remove mechanism)
  ↳ No PR: [8bf322c](https://github.com/DPDK/dpdk/commit/8bf322cdc49774c225c6d35f091a86284888e097)
- Fixed the problem that the netvsc driver did not release the port reference from the process during VF hot removal in a multi-process scenario, and added a multi-process communication mechanism to coordinate VF removal. (Architecture-related: multi-process communication mechanism)
  ↳ No PR: [f741298](https://github.com/DPDK/dpdk/commit/f741298f702772570ff20df000050483488092d0)
- Fixed the problem that the fast-path ops of the secondary process in the mlx4 driver are not synchronized, and updated the burst function pointer and queue data pointer of rte_eth_fp_ops in the START_RXTX and STOP_RXTX processing. (Architecture-related: public API)
  ↳ No PR: [b801feb](https://github.com/DPDK/dpdk/commit/b801feb51cd712ae4517a99d40ee4701b6612993)
- Added explicit checks for igb_uio and uio_pci_generic drivers in NBL PMD's probe function, rejecting bindings and updated documentation to account for these limitations. (Architecture-related: Platform compatibility)
  ↳ No PR: [4ca3851](https://github.com/DPDK/dpdk/commit/4ca3851a472cb1b47d2fcbe6ac76a7decbe90fe8)
- Fixed Thor2's VLAN stripped flag reporting issue in the bnxt driver, setting the VLAN_STRIPPED flag based on the actual stripping status in the scalar path. (Architecture-related: public API)
  ↳ No PR: [c87efa4](https://github.com/DPDK/dpdk/commit/c87efa43b971ddb09abba95dfef2f06f6fa3c9b0)
- Pass the receive timestamp to mbuf through dynamic field in bnxt driver, and add ptp_cfg null pointer check to avoid segfault. (Architecture-related: public API)
  ↳ No PR: [9b5c01c](https://github.com/DPDK/dpdk/commit/9b5c01c2dc977fd57e93461c366d7cbd35428ff1)
- Fixed the bonding device detection logic in the mlx5 driver, using sysfs parsing and dedicated functions instead of device name checking. (Architecture-related: bonding detection method)
  ↳ No PR: [2aa207b](https://github.com/DPDK/dpdk/commit/2aa207b1144abe99e7c57e5c1690ffa676a2d731), [f6e478d](https://github.com/DPDK/dpdk/commit/f6e478d5557a8d8c1407b35620fd7a32b8211a91)
- Fixed the problem of port name conflict in mlx5 driver under BlueField Socket Direct configuration, supporting shared E-Switch scenarios through more general uplink and host PF counting logic and improved port name generation and representor matching. (Architecture-related: port name generation and representor matching)
  ↳ No PR: [2f7cdd8](https://github.com/DPDK/dpdk/commit/2f7cdd821b1b4954f18faad0e8b6d9ab41ca3f23)
- Fixed the regression problem of mlx5 PMD default flow engine on Windows, introduced platform-specific device parameter initialization, and set dv_flow_en and allow_duplicate_pattern to 1 by default on Windows (architecture-related: platform compatibility)
  ↳ No PR: [b8744d9](https://github.com/DPDK/dpdk/commit/b8744d9e39444fcf04e3864cb4b4f93e584f9742)
- Fixed the problem of vsocket resources not being released when vhost driver registration failed, and restored the release operation on the wrong path. (Architecture-related: public API)
  ↳ No PR: [26bb3eb](https://github.com/DPDK/dpdk/commit/26bb3ebd833e24aa2a11211bc8fedfcda69aa253)
- Fixed the issue where the masked VXLAN/NVGRE encapsulation action in the asynchronous stream API caused the data packet to be encapsulated into an empty header. By separating the tunnel header translation logic from mlx5_tbl_translate_reformat and processing it uniformly, it ensures that the encapsulated data is delivered correctly. (Architecture-related: public API)
  ↳ No PR: [d0a0040](https://github.com/DPDK/dpdk/commit/d0a0040f044556cdf8692aff735797fd83036949)
- Fixed the problem that the VLAN stripping flags (RTE_MBUF_F_RX_VLAN and RTE_MBUF_F_RX_VLAN_STRIPPED) of the mlx5 driver may be incorrectly set in the CQE compression scenario, and corrected the position of the packet header information bytes in mini CQE and the checking method of the CVLAN bit. (Architecture-related: public API)
  ↳ No PR: [5654f38](https://github.com/DPDK/dpdk/commit/5654f38eba85dc180384d5b2caf621b224da51eb)
- Fixed the GEN4 elliptic curve capability detection and verification in the QAT driver: reject unsupported RSA padding and EC curves and return -ENOTSUP during session configuration, supplement the missing ECDH, ECDSA, ECPM capability table entries, and make the asymmetric test return TEST_SKIPPED when session creation returns -ENOTSUP. (Architecture-related: external behavior)
  ↳ No PR: [b7d12c4](https://github.com/DPDK/dpdk/commit/b7d12c41eec5f682c72ff76d590e20f6f5bc415e)
- Fixed the error in setting the length of modular exponentiation and modular inversion operation results in QAT hardware, and fixed the problem that the leading zero bytes of the result were not skipped during comparison. (Architecture-related: external behavior)
  ↳ No PR: [117c766](https://github.com/DPDK/dpdk/commit/117c7662c64aa913002abcaf119153ea8b03a67d)
- Fixed a crash on BCM57608 caused by wrong structure field offset, adjusted the position of the multi-doorbell page size field to match the firmware response layout. (Architecture-related: public API)
  ↳ No PR: [82864dd](https://github.com/DPDK/dpdk/commit/82864dd050b8bba9a7ce75a47e88cf89985d299d)
- Supports querying statistical information when the port is stopped and returning previously saved statistical values. (Architecture-related: external behavior)
  ↳ No PR: [898248f](https://github.com/DPDK/dpdk/commit/898248fc42871748ae068e94b7a4d6aed28dec5f)
- Introduce a universal Tx path selection infrastructure for Intel network card drivers, uniformly select the Tx path by the main process, and remove the private implementation in each driver. (Architecture-related: Tx path selection)
  ↳ No PR: [cf96ec2](https://github.com/DPDK/dpdk/commit/cf96ec231d02197081f3e9ccbc68da5fa0db982f), [8d57c17](https://github.com/DPDK/dpdk/commit/8d57c17888064fbde677eabd0d4dd578bf949747), [910dce5](https://github.com/DPDK/dpdk/commit/910dce5ab07dbdc1cf528562fb9b869fc7fb8542)
- Reconstruct the MAC initialization logic of the NFB network card driver, add MDIO management, improve error handling, and realize interface port separation management. (Architecture-related: NFB driver MAC reconstruction)
  ↳ No PR: [286a8af](https://github.com/DPDK/dpdk/commit/286a8afc1dd489f66e2b5b41d429f0c2b27ddbe1)
- Replace the __be64 type with DPDK's rte_be64_t to reduce dependence on header files when building cross-platforms. (Architecture-related: platform compatibility)
  ↳ No PR: [527844a](https://github.com/DPDK/dpdk/commit/527844aec0111547147b4a955ddf75b568216191)
- Merge the scalar Tx path buffer release function of ice and i40e drivers into the common header file. (Architecture-related: public header file)
  ↳ No PR: [a1aaf18](https://github.com/DPDK/dpdk/commit/a1aaf1808114dad5e0ff0b15c5c637ed71497c62)
- Allow the driver path loaded by the main process to be passed to the child process to fix test failures in shared builds. (Architecture-related: build and installation methods)
  ↳ No PR: [e8dca79](https://github.com/DPDK/dpdk/commit/e8dca796729006e96eff6200256e787bd387f087)
- Added mbuf quick release memory pool pointer to the general send queue structure, optimized the mbuf release process of ice and i40e drivers, and improved performance. (Architecture-related: public API)
  ↳ No PR: [3690144](https://github.com/DPDK/dpdk/commit/369014467b121fe4a8015281dcf35529de78a9af)
- Improve mailbox exception handling, introduce a state machine to replace the simple confirmation mark, add message ID and type verification, and handle timeout scenarios and pre-send status checks. (Architecture-related: mailbox exception handling)
  ↳ No PR: [903bec3](https://github.com/DPDK/dpdk/commit/903bec3c46e89c76403ecbb5c6a23266a601d873)
- Renamed MLX5 debug build flag from RTE_LIBRTE_MLX5_DEBUG to RTE_PMD_MLX5_DEBUG. (Architecture-related: public API)
  ↳ No PR: [88e5d17](https://github.com/DPDK/dpdk/commit/88e5d17b46c01ba3233423ea901f541e1d74634e)
- Renamed MLX4 debug build flag from RTE_LIBRTE_MLX4_DEBUG to RTE_PMD_MLX4_DEBUG. (Architecture-related: public API)
  ↳ No PR: [ce319a5](https://github.com/DPDK/dpdk/commit/ce319a5add44cd29611af851b9d6572b21b5d8b5)
- Remove all conditional compilation macros that depend on the security library in the ixgbe driver, because the library has become an explicit dependency. (Architecture-related: build dependency changes)
  ↳ No PR: [c84f3ae](https://github.com/DPDK/dpdk/commit/c84f3aebcd8e1de28b747078f3f81b9428b27c73)
- Disable MSVC warnings about zero extensions in ice base code builds. (Architecture-related: platform compatibility)
  ↳ No PR: [80b3e9c](https://github.com/DPDK/dpdk/commit/80b3e9cad7599ce01f94cd6f8f966401a77e29c1)
- Update the hardware configuration of the RTL8127 network card driver, including enabling flow control, updating PHY configuration, MAC MCU patch and PHY MCU patch. (Architecture-related: driver configuration)
  ↳ No PR: [e04c235](https://github.com/DPDK/dpdk/commit/e04c2359ee6e2e2f30f285c9e0d4f054eb9e2edd)
- Update the PHY configuration and MAC MCU patch of the RTL8126 network card driver, and remove the obsolete configuration method. (Architecture-related: driver configuration)
  ↳ No PR: [cc0a40c](https://github.com/DPDK/dpdk/commit/cc0a40c6abd15eb90199e1cf147f973afebb64c7)
- Updated the hardware configuration of multiple models of RTL8125 series network cards, including MAC MCU patches, PHY configuration, interrupt processing and ASPM clock request locking. (Architecture-related: driver configuration)
  ↳ No PR: [974c62b](https://github.com/DPDK/dpdk/commit/974c62b3486e38ec047669b5f57f4f6d2b9f2729)
- Update the mask and shift logic of the aura batch free operation in the RX fast path for the cn20k platform to match the hardware register changes. (Architecture-related: platform compatibility)
  ↳ No PR: [5a40b4f](https://github.com/DPDK/dpdk/commit/5a40b4f70c34a8dca9613dbb1254d15b09e32f5c)

### Core Library Layer
- Added interrupt event flag and internal API, used to obtain the current event type in the interrupt callback. (Architecture-related: public API)
  ↳ No PR: [0b0c6f8](https://github.com/DPDK/dpdk/commit/0b0c6f85bea1e9a595174ac39c1e7cb1c13c9e7b)
- Added an internal API to EAL to query the loaded driver path, and adjusted the plug-in loading logic. (Architecture-related: EAL internal API)
  ↳ No PR: [d767378](https://github.com/DPDK/dpdk/commit/d767378e75ac06b96c951b5aa1ba9fbc95d80fd8)
- Add RTE_MIN3 and RTE_MAX3 macros, and rename local variables in existing macros to avoid shadow declaration warnings. (Architecture-related: public API)
  ↳ No PR: [3d3cb5c](https://github.com/DPDK/dpdk/commit/3d3cb5cf4d2cbf86f36d5e65a3ae62a205c9edda), [c8cbe8e](https://github.com/DPDK/dpdk/commit/c8cbe8e96d533c81746b3fbc41d8133655f436e5)
- Allow variables as first argument to RTE_SHIFT_VAL32 and RTE_SHIFT_VAL64 macros, and change internal implementation from UINT32_C/UINT64_C to cast. (Architecture-related: public API)
  ↳ No PR: [0340918](https://github.com/DPDK/dpdk/commit/0340918b0ce86d2b7824e933c555b8819ae0581c)
- Add 256-NxA4/5/6 algorithm support to cryptodev, including confidentiality, integrity and AEAD modes for Snow 5G, AES 256 and ZUC 256. (Architecture-related: public API: New encryption algorithm)
  ↳ No PR: [6e928dc](https://github.com/DPDK/dpdk/commit/6e928dcd68ab2bca9fefea9031f5edc388e89258)
- Fixed the out-of-bounds access problem caused by insufficient virtqueue array size in VDUSE, and correctly included the control queue by defining the VHOST_MAX_VRING macro. (Architecture-related: public API)
  ↳ No PR: [7cc4f26](https://github.com/DPDK/dpdk/commit/7cc4f260bf1c01ff717b6490f6c0ca205cb08953)
- Fixed two related bugs in FreeBSD EAL memory initialization: hole placement error and memseg search may incorrectly occupy reserved holes. (Architecture-related: platform compatibility)
  ↳ No PR: [c21f2e2](https://github.com/DPDK/dpdk/commit/c21f2e2caad15a0a421a7016ffea19aeadefc6d8), [2db5130](https://github.com/DPDK/dpdk/commit/2db5130217364c08b5d2669e4150ec70b695db87)
- Fixed the rte_net_get_ptype function's parsing of stacked VLAN frames, supporting up to 8 layers of VLAN headers and correctly setting the ptype bitmask. (Architecture-related: public API)
  ↳ No PR: [1f25067](https://github.com/DPDK/dpdk/commit/1f250674085aeb4ffd15ac2519a68efc04faf7ac)
- Add name length check for LPM library, reject overly long names and return ENAMETOOLONG; fix internal buffer size, add truncation warning for RCU delay queue names. (Architecture-related: public API)
  ↳ No PR: [2d6c783](https://github.com/DPDK/dpdk/commit/2d6c7836bd6726bc607638c8137a5cf14d6bb298)
- Add name length check for rte_hash_create and rte_fbk_hash_create, return ENAMETOOLONG; add truncation warning for internal ring names. (Architecture-related: public API)
  ↳ No PR: [bac12fa](https://github.com/DPDK/dpdk/commit/bac12fa076a528287fedd3ce4de372b7b8254784)
- Add name length verification in rte_efd_create, reject overly long names and return an error; also improve the logging when ring name is truncated and the error message when ring creation fails. (Architecture-related: public API)
  ↳ No PR: [2e6c513](https://github.com/DPDK/dpdk/commit/2e6c5139c87ca2931be9e4faa8a0b8a1ceaeec41)
- Limit the length of the runtime directory and Unix domain socket paths to avoid binding failures or command line parsing errors caused by too long paths. (Architecture-related: platform compatibility)
  ↳ No PR: [6375935](https://github.com/DPDK/dpdk/commit/637593544a1d175939089385f1041efbfeb32e26)
- Add parameter verification and error code settings in tailq search, create and register functions, reject overly long names and improve error handling. (Architecture-related: public API)
  ↳ No PR: [93d1972](https://github.com/DPDK/dpdk/commit/93d19726f1d475898ed458561b482086fd16c72d)
- Fixed the problem of loss of precision due to integer division first in TSC frequency query. Change to multiplication first and then division to get a more accurate frequency value. (Architecture-related: core behavior)
  ↳ No PR: [a17499c](https://github.com/DPDK/dpdk/commit/a17499cf33a1606731d75d15a18bfd42c497b40e)
- Fix the annotation of the per-lcore variable allocation function, remove the incorrect __rte_alloc_size attribute, and avoid false positives in the FORTIFY_SOURCE runtime check. (Architecture-related: public API)
  ↳ No PR: [de5991d](https://github.com/DPDK/dpdk/commit/de5991dcd751f7bbe9596b750538803a7e187548)
- Fix the problem that the fbarray name may be truncated in the secondary process, add snprintf return value check and return an error when the name is too long. (Architecture-related: EAL fbarray)
  ↳ No PR: [9f3d511](https://github.com/DPDK/dpdk/commit/9f3d51136011e1ed63180332730768efaa35c0a3)
- Fixed the fbarray name conflict problem caused by non-unique PID in containers that share hugetlbfs mounts, use TSC values to generate unique names, and reduce the name buffer size. (Architecture-related: core module behavior)
  ↳ No PR: [9b1eae9](https://github.com/DPDK/dpdk/commit/9b1eae94b3e40b5829b36a30f1d07b79899224ce)
- Add length check for string parameters in pcapng copy function to prevent over-long strings from causing silent truncation or buffer problems. (Architecture-related: public API)
  ↳ No PR: [12e649a](https://github.com/DPDK/dpdk/commit/12e649addd0b9f63a79fcfd6b8ccffcffd7d41eb)
- Move HPET timer related functions from eal_timer.c to the newly added eal_timer_hpet.c source file, ensure that these symbols are only exported when HPET is enabled, and fix the problem that symbol export is not controlled by the build configuration. (Architecture-related: Build configuration control)
  ↳ No PR: [2bee1a8](https://github.com/DPDK/dpdk/commit/2bee1a8c9f2bff5b56d327840f79bd1acbfcff7c)
- Fix the memory corruption caused by inconsistent dev_id allocation in cryptodev in the secondary process, so that the secondary process can find the device in the existing memzone through the device name. (Architecture-related: multi-process behavior)
  ↳ No PR: [55ec467](https://github.com/DPDK/dpdk/commit/55ec467f2e9f437acbec42a6a1ccc4bcfee7ad45)
- Fixed the offset overflow problem caused by 32-bit multiplication in the hash library, and converted the relevant multiplication operands to size_t type to ensure correct calculation on 64-bit systems. (Architecture-related: public API)
  ↳ No PR: [476a053](https://github.com/DPDK/dpdk/commit/476a0536b004984e47bd49e36e99949a8b95c701)
- Fix the unaligned access problem in the rte_hash_crc function caused by the misalignment of the input pointer. Align the input pointer before calculation. (Architecture-related: public API)
  ↳ No PR: [112c07c](https://github.com/DPDK/dpdk/commit/112c07c62a885c826d316d84d6e540fdc7860c41)
- Add processing of epoll errors and disconnection events (EPOLLERR, EPOLLHUP, EPOLLRDHUP) in Linux EAL interrupt processing, and add auxiliary functions for event conversion and interrupt source removal and release. (Architecture-related: EAL interrupt processing)
  ↳ No PR: [1c0a741](https://github.com/DPDK/dpdk/commit/1c0a74161a2c96a24e986e454bb58f4e11b0d6e6)
- Fixed the memory leak problem of hash tables under RCU delayed release configuration, including leaks when entries are deleted and keys are overwritten. (Architecture-related: Hash table RCU release behavior)
  ↳ No PR: [cbc677c](https://github.com/DPDK/dpdk/commit/cbc677ce0df333b92f7838af47699fa68796a86e), [50d9439](https://github.com/DPDK/dpdk/commit/50d943929acf3948df13ce0e5cdb126587ff9654)
- Fixed compilation failure caused by using non-standard __COUNTER__ in pedantic compilation mode, and changed the cache protection macro to use __LINE__ to generate unique names. (Architecture-related: platform compatibility)
  ↳ No PR: [ebceabd](https://github.com/DPDK/dpdk/commit/ebceabddf19b7bccebd9c477a22cf345a50cee7a)
- Replaced the fixed size stack buffer in the pcapng block build with dynamic allocation to avoid buffer overflow caused by too long strings, and added input length checking and allocation failure handling. (Architecture-related: public API)
  ↳ No PR: [edd9b97](https://github.com/DPDK/dpdk/commit/edd9b971f7781390e050d4d2f54656ec8e98bbc1)
- Removed outdated mempool creation advice and fixed copy-paste error in rte_mempool_calc_obj_size() function description. (Architecture-related: public API)
  ↳ No PR: [3d520f5](https://github.com/DPDK/dpdk/commit/3d520f5942346d07a86fe9b106a82158855674c8)
- Updated the Control+L shortcut behavior to clear the screen and then redisplay the prompt to match standard bash and readline behavior. (Architecture-related: external behavior)
  ↳ No PR: [3022c84](https://github.com/DPDK/dpdk/commit/3022c8464b13c88bab4f2935353842fe8f5fdd3e)
- Use the standard C library function getmntent() instead of manually parsing /proc/mounts, and optimize the mount point verification method when hugepage_dir is explicitly specified. (Architecture-related: EAL core module)
  ↳ No PR: [7b306f9](https://github.com/DPDK/dpdk/commit/7b306f9ab3c72f634eca12f53fd059f1bd823699)
- Fixed MSVC build bug, replacing 1UL with RTE_BIT64 to force 64-bit value. (Architecture-related: Platform compatibility)
  ↳ No PR: [d1ab1a2](https://github.com/DPDK/dpdk/commit/d1ab1a2facf9b823bc400e573aa39381ca7b915f)
- Added return value documentation for the rte_pcapng_add_interface() and rte_pcapng_write_stats() functions in the pcapng library. (Architecture-related: public API documentation)
  ↳ No PR: [bb7af6b](https://github.com/DPDK/dpdk/commit/bb7af6b4a8295f29fdafa670f6b511090e4e877b)

### Bus Layer (HAL)
- Added diagnostic and performance counter support for CN20K's NPA pool operation. (Architecture-related: public API)
  ↳ No PR: [28d65f1](https://github.com/DPDK/dpdk/commit/28d65f12ac774b4739363456ca8b8553f04d4207)
- Set the CPT cache line size according to platform conditions: CN10K/CN9K uses 128 bytes, others use 256 bytes. (Architecture-related: platform compatibility)
  ↳ No PR: [787f3f6](https://github.com/DPDK/dpdk/commit/787f3f629547d5766034bdbdcfbd68505aa1b119)
- Adjust the alignment requirement of the TLS context pointer from 128 bytes to 256 bytes, and update the related memory allocation and cleanup logic. (Architecture-related: ABI compatibility)
  ↳ No PR: [74edca7](https://github.com/DPDK/dpdk/commit/74edca70216ce7f5bfce611580581bff5477f183)
- Added out-of-place flow rule configuration support for security actions. (Architecture-related: security action OOP flow rules)
  ↳ No PR: [e216185](https://github.com/DPDK/dpdk/commit/e2161850fd2f8764c379b9f7c604d99157de07e8)
- HALO support was introduced in the NPA of cn20k, allowing 1:1 aura-pool mapping, and adding the devargs parameter halo_ena to enable or disable this feature. (Architecture-related: HALO support and devargs parameter)
  ↳ No PR: [a7cc84c](https://github.com/DPDK/dpdk/commit/a7cc84c6e9e57dc3637d0ddd97328eba84d60db5), [45abbfc](https://github.com/DPDK/dpdk/commit/45abbfc836b120fe55af96829a35ffa1309fea67)
- The axgbe driver adds external PHY read and write functions, supports the IEEE Clause 22 standard, and adds support for Marvell M88E1512 PHY. (Architecture-related: public API)
  ↳ No PR: [99ab4c4](https://github.com/DPDK/dpdk/commit/99ab4c45df8ace90bf8457312bbef289e4ad8e97), [7ba7d89](https://github.com/DPDK/dpdk/commit/7ba7d89890ab6b68a58aa24f3c985e594da27a7e)
- Added CPT CQ (completion queue) configuration support for inline inbound IPsec. (Architecture-related: public API)
  ↳ No PR: [3fdf3e5](https://github.com/DPDK/dpdk/commit/3fdf3e53f3c43d3eb69e0b947db163a15fe4520b), [a2ae23b](https://github.com/DPDK/dpdk/commit/a2ae23bf4e65f88780dab6f6d1501fecfb7784d5)
- Added API forward compatibility support for uacce bus driver and hisi_acc DMA driver. (Architecture-related: API compatibility)
  ↳ No PR: [89597cf](https://github.com/DPDK/dpdk/commit/89597cf132258551981d61b55eb21810f3cd7056), [591d2e1](https://github.com/DPDK/dpdk/commit/591d2e1263c0faa31c3f848b75bfff6c06e75c50)
- Added ZUC 256 v2 pure encryption support to the CN20K encryption device driver, and restructured PDCP related functions. (Architecture-related: public API)
  ↳ No PR: [72eb756](https://github.com/DPDK/dpdk/commit/72eb75662a57b0e55ee6eca2128920eeb58e351a)
- Added support for Snow 5G and ZUC 256 algorithms in the cnxk encryption driver. (Architecture-related: public API)
  ↳ No PR: [8a95274](https://github.com/DPDK/dpdk/commit/8a952741b9f0a512efcd258fb290323fbd4aca45)
- Fix CPT CQ loop wrapping processing, correct CQ size assignment and optimize pointer calculation and head pointer management in CQ callback. (Architecture-related: public API)
  ↳ No PR: [63b16e2](https://github.com/DPDK/dpdk/commit/63b16e2671061e4f7d09988ae3f8cd67a6dec0d9)
- Updated the CPT RXC time configuration of the CN20k platform, changed the reassembly configuration to fixed granularity and variable activity limit time, and added the rxc_step device parameter for NIX devices. (Architecture-related: platform compatibility)
  ↳ No PR: [910626d](https://github.com/DPDK/dpdk/commit/910626df29dd5f34d4e3235b46e7c0fdaf7f66c0), [1886c80](https://github.com/DPDK/dpdk/commit/1886c80595a033de6bcfa110d48fd9337172cd04)
- Fixed the bit width error of the DPC setting field in the NPA structure. (Architecture-related: public API)
  ↳ No PR: [f85f3af](https://github.com/DPDK/dpdk/commit/f85f3af3f7006d7439287df5ae3f2d3a40c30336)
- Fixed undefined shifting behavior caused by zero value in __rte_red_calc_qempty_factor function. (Architecture-related: public API)
  ↳ No PR: [f904b81](https://github.com/DPDK/dpdk/commit/f904b818928931924f1f4a117d10d98617b92209)
- Update the CPT RXC structure to adapt to CN20k and CN10k platforms, and correct the structure type in related parsing functions. (Architecture-related: platform compatibility)
  ↳ No PR: [8d7f089](https://github.com/DPDK/dpdk/commit/8d7f08932ec1645ae4ce76cee286412782fb08ca)
- Fix DES/3DES and AES key length verification, verify the key before copying it to the SA structure, and prevent out-of-bounds writing to adjacent IV/salt fields. (Architecture-related: public API)
  ↳ No PR: [fda5740](https://github.com/DPDK/dpdk/commit/fda5740324f5d3c77d9d6e35e1b6fcd9a72b9bd2)
- Modified the description of mbuf quick release, explicitly supports segmented messages, and updated the Rx/Tx offload function description. (Architecture-related: public API behavior)
  ↳ No PR: [71e469a](https://github.com/DPDK/dpdk/commit/71e469ada86210e9831c84607999278a01872a0b)
- Remove the global dependency on cryptodev in the reorganization configuration and change it to only the cn10k platform, and add the RXC queue configuration for the cn20k platform. (Architecture-related: platform compatibility)
  ↳ No PR: [c5bcdea](https://github.com/DPDK/dpdk/commit/c5bcdea70a9539de16317cf3416cde4919cbae69)
- Added cnf20ka platform check for normal message reassembly function, disable this function on this platform. (Architecture-related: platform compatibility)
  ↳ No PR: [004656b](https://github.com/DPDK/dpdk/commit/004656b5738a5e922b8f7ba7527349fb99c0c9c9)

### Cross-cutting / Other Architecture-related Changes
- Add custom memory allocator support to the ACL library, and add a new public API. (Architecture-related: public API)
  ↳ No PR: [19e585c](https://github.com/DPDK/dpdk/commit/19e585ca26e0327ac2e9e46fa1ee21c8d8b3c7e2)
- Added support for BPF atomic xchg instruction and added related test cases. (Architecture-related: BPF instruction extension)
  ↳ No PR: [81871f5](https://github.com/DPDK/dpdk/commit/81871f5668f3a7d43013801a74106945006db623)
- Fixed the problem of returning an error when adding a dictionary container to an array container, and added corresponding test cases. (Architecture-related: public API)
  ↳ No PR: [dd5789e](https://github.com/DPDK/dpdk/commit/dd5789e3cedbcd44fb832e9b8f969850182e1e25)
- Fixed the bug that the mbuf copy function incorrectly returned NULL when copying to the end of the packet, and the external flag was not retained when allocating from the fixed external buffer memory pool. (Architecture-related: public API)
  ↳ No PR: [8a75c9a](https://github.com/DPDK/dpdk/commit/8a75c9af639b68a594d1f0e58b650c54974cf3db)
- Fixed the stack alignment problem when calling external functions in x86 JIT compilation, added stack pointer alignment operation in prolog, and added related test cases. (Architecture-related: Core module: BPF JIT)
  ↳ No PR: [6d0e6b5](https://github.com/DPDK/dpdk/commit/6d0e6b5e3a76b20263ef35c7f60266f600f0c8bb)
- Add name and value length checks in the configuration file, reject entries that are too long, and increase the read buffer to avoid silent truncation. (Architecture-related: public API)
  ↳ No PR: [5d322b0](https://github.com/DPDK/dpdk/commit/5d322b0ccaebb94628a2a34796376f2a338c545b)
- Fixed the use-after-free competition problem caused by not safely destroying fdset when cleaning up the vhost library. Added fdset_destroy function to ensure that the event distribution thread exits correctly and releases resources. (Architecture-related: public API)
  ↳ No PR: [73ea443](https://github.com/DPDK/dpdk/commit/73ea44370d35f7683cb5e59a721f191aec724eb6)
- Fixed the 32-bit integer wrapping problem that may be caused by the addition of offset and length when mbuf reads data, and uses 64-bit calculations instead; at the same time, the relevant test cases are updated to correctly verify the failure behavior of over-long reads. (Architecture-related: public API)
  ↳ No PR: [45f1da4](https://github.com/DPDK/dpdk/commit/45f1da4401f0934ae1d5e194d8bf689c8d7a6300)
- Added a description in the deprecation notice: VFIO API will soon become an internal interface or be removed. (Architecture-related: public API)
  ↳ No PR: [e0e492f](https://github.com/DPDK/dpdk/commit/e0e492f2d86a2503b1d2d89e79be1154f0794c85)
- Added vDPA driver API deprecation notice in the release notes: This API will no longer provide the get_vfio_group_fd interface, and it is recommended to use the new unified VFIO container device allocation API. (Architecture-related: public API)
  ↳ No PR: [e69d978](https://github.com/DPDK/dpdk/commit/e69d9786332b02ce3abe8c44807f9fa5e44a0548)
- Added a list of tested Intel platform and Intel network card combinations, a list of Intel platforms equipped with NVIDIA network cards, and IBM Power 11 platform test results in the 26.03 release notes. (Architecture-related: Platform compatibility)
  ↳ No PR: [4765974](https://github.com/DPDK/dpdk/commit/476597450c973cab17b236d1272bd846247ad291), [2d916e6](https://github.com/DPDK/dpdk/commit/2d916e67243be59b165abe09ca295ffac84c2a0d), [2fef794](https://github.com/DPDK/dpdk/commit/2fef794c8cd1f3b552e9b2448782cb6bd6d60a8b)
- Start a new release cycle, upgrade the version to 26.03-rc0, increase the ABI minor version number, and initialize the release notes. (Architecture-related: version and compatibility)
  ↳ No PR: [0ace445](https://github.com/DPDK/dpdk/commit/0ace445fc09bafa43d63155e3a44815efa262c0d)
- Change the global -Wno-comma compilation option to enable on-demand, and only add it separately in drivers that require this option to solve the problem that compilers such as MSVC do not support this flag. (Architecture-related: platform compatibility)
  ↳ No PR: [4448855](https://github.com/DPDK/dpdk/commit/444885550c9ee5e9093fdbe2a0f59a1dace74d19)
- Remove crypto extension in Cortex-A78AE configuration to avoid build failure on compilation toolchains lacking AES support. (Architecture-related: Platform compatibility)
  ↳ No PR: [b32a973](https://github.com/DPDK/dpdk/commit/b32a97330a04a2342f792c8e24d2008782700ae1)
- Announcing the deprecation of support for OpenSSL 1.1.1, future versions will require a minimum OpenSSL 3.0 version. (Architecture-related: build dependencies)
  ↳ No PR: [8ea4f9c](https://github.com/DPDK/dpdk/commit/8ea4f9cf7c8e09a6f3f4fe0bc2e5f3106ff85ae4)

### Application Layer
- testpmd txonly multi-flow mode now supports configurable number of flows, adding the --txonly-flows parameter and set txonly-flows command. (Architecture-related: public API)
  ↳ No PR: [8d16bc5](https://github.com/DPDK/dpdk/commit/8d16bc5c2c6733ef1fa48e5021e4d2aed6da3955)
- testpmd's --rxq-share parameter now supports dynamic allocation of Rx queue sharing groups. (Architecture-related: configuration behavior)
  ↳ No PR: [bc63569](https://github.com/DPDK/dpdk/commit/bc63569c1071543b37b2e71b5c2b5ed8bc96c8e1), [1a9c36e](https://github.com/DPDK/dpdk/commit/1a9c36eb28a6e2d4ac485ac23b489febd9d0689a)
- The upper limit of the number of worker threads is changed from a fixed value of 128 to RTE_MAX_LCORE, which fixes the buffer overflow problem on high-core platforms. (Architecture-related: Platform compatibility)
  ↳ No PR: [be237f6](https://github.com/DPDK/dpdk/commit/be237f643831d9f79a3c104d19b4bd617bc7e99d)
- Optimize the memory pool object acquisition function: remove the compile-time constant check, and adjust the cache update order to improve performance. (Architecture-related: public API)
  ↳ No PR: [80386cc](https://github.com/DPDK/dpdk/commit/80386ccf6582aa13a1994ebfaacc3aec1bb62171)
- Optimize the __rte_pktmbuf_free_direct function to reduce one memory storage operation and improve performance. (Architecture-related: public API)
  ↳ No PR: [c53d28c](https://github.com/DPDK/dpdk/commit/c53d28ce371e8c066bf2b27445d3c211c91b06f0)
- Add bounds checks and loop counters to descriptor chain traversal of the vhost control queue to prevent malicious clients from causing memory corruption or infinite loops. (Architecture-related: vhost core module)
  ↳ No PR: [6ec1778](https://github.com/DPDK/dpdk/commit/6ec17781346e0fe4b566b6bf8f79be71f87c10e4)
- Disable empty BPF programs, and fix the problem of buffer out-of-bounds reading caused by the acceptance of no-instruction programs and the lack of EXIT instructions. (Architecture-related: BPF core module)
  ↳ No PR: [cee21cc](https://github.com/DPDK/dpdk/commit/cee21cc5be82faef74bb1b8f84407cc92de5dee7)

## Routine Changes

### New features
- Add support for AES-XTS encryption algorithm in OpenSSL encryption PMD.
  ↳ No PR: [c4ac898](https://github.com/DPDK/dpdk/commit/c4ac89884b7481a7e1a2ef41e9d9bc96fec935da)
- Add support for V4000 Krackan2e device to axgbe network card driver.
  ↳ No PR: [92ad538](https://github.com/DPDK/dpdk/commit/92ad538c329e8da03dea6191b46eab5b425b65d0)
- Added IPv4 and IPv6 fragmented RSS types to IAVF PMD, supporting symmetric Toeplitz hashing.
  ↳ No PR: [06680fa](https://github.com/DPDK/dpdk/commit/06680fad4a788e55a1d1cd8c12c6b00453b2f423)
- Add SHAKE-128 and SHAKE-256 algorithm support to OpenSSL PMD.
  ↳ No PR: [665479f](https://github.com/DPDK/dpdk/commit/665479fa2f8d3d211e3e2fdd6c1c57b33c6fefee), [ec2691f](https://github.com/DPDK/dpdk/commit/ec2691f52957414004ec671782a9779365d495bd)
- Migrate the iavf driver Tx path to the universal scalar Tx function, delete duplicate private implementations, and add callback functions such as IPsec descriptor acquisition and context descriptor generation.
  ↳ No PR: [182b243](https://github.com/DPDK/dpdk/commit/182b243f4188b23f4be8f539ba087bbd8e8986f8)
- Added support for simple Tx functions to the idpf driver, and adjusted the Tx path selection logic in single queue mode.
  ↳ No PR: [376faf4](https://github.com/DPDK/dpdk/commit/376faf4aaa1638209b26ac820d8cd68f26dda529)
- Enable simple send function for cpfl driver, and refactor send path selection logic to support single queue mode.
  ↳ No PR: [e165a4b](https://github.com/DPDK/dpdk/commit/e165a4bd0a8ae84c16e17b165ed6a1adaae60dfe)
- Add a device reset callback function to the GVE network card driver, and clear the transceiver queue array in the device pointer when releasing the queue.
  ↳ No PR: [1bf64ed](https://github.com/DPDK/dpdk/commit/1bf64edce3c4010b539f27094173128c5a553c2e)
- Added vdev-based alternative detection method for NFB network device driver, supporting virtual or emulated devices with non-PCI representation.
  ↳ No PR: [f1029ad](https://github.com/DPDK/dpdk/commit/f1029adabbe3a5442dfb6aa6ae2742c857603c9e)
- Added support for a variety of compatible network cards to the nfb network card driver, including NFB-200G2QL secondary card, FB2CGHH card, COMBO-400G1 card and universal CESNET-NDK card.
  ↳ No PR: [26db82f](https://github.com/DPDK/dpdk/commit/26db82f614b2410969357ce1666ccdf488cbf608)
- Add firmware version reporting function for nfb network card driver.
  ↳ No PR: [a806aa7](https://github.com/DPDK/dpdk/commit/a806aa716c0fd9e49369ab52cb6dd80786f77a0c)
- Optimize the MAC address allocation logic of the nfb network card driver, giving priority to the MAC address assigned by the network card.
  ↳ No PR: [5fc0737](https://github.com/DPDK/dpdk/commit/5fc07378598d877ea7cf5dbf21999dade659e938)
- Add the function of configuring the up and down status of the real link through the MDIO register for the nfb network card driver.
  ↳ No PR: [746a00c](https://github.com/DPDK/dpdk/commit/746a00cf08b050dd53defc03c200c8c9db574508)
- Add basic support for configuring RS-FEC link mode via MDIO to the nfb network card driver.
  ↳ No PR: [420ba6a](https://github.com/DPDK/dpdk/commit/420ba6a5138ee93ebe649919ab7dbfab7047457f)
- Added support for receiving MTU settings for nfb network card driver, and reporting the maximum MTU value in device information.
  ↳ No PR: [bf27de6](https://github.com/DPDK/dpdk/commit/bf27de61385c989a5f99e55cb38c96df1659674c)
- Optimized the way to obtain statistical information of the nfb network card driver, instead reading the total counter provided by the firmware MAC component.
  ↳ No PR: [9061ac2](https://github.com/DPDK/dpdk/commit/9061ac2713bb97efb50c9911d996ebba407392f3)
- Added Out-Of-Place handling support in event Rx fastpath for CN20k platform.
  ↳ No PR: [a98b770](https://github.com/DPDK/dpdk/commit/a98b7704a6fcef003196ee68d648370869b41309)
- The bnxt driver has added PTP time synchronization support, processing PTP frames in the receiving path, and parsing the timestamp when the transmission is completed.
  ↳ No PR: [29a075c](https://github.com/DPDK/dpdk/commit/29a075c290e1e2be9d8e2e29e0c5b6dfc3ffb528), [5722ed1](https://github.com/DPDK/dpdk/commit/5722ed1aafd2fc5ad44e432a4f6c7bd337c673d8), [a075b33](https://github.com/DPDK/dpdk/commit/a075b33deafb1a1e83d3fb04b0c65775d77d416b)
- The ice network card driver adds support for RSS hashing of L2TPv2 packets.
  ↳ No PR: [02d9f41](https://github.com/DPDK/dpdk/commit/02d9f41bada6b5f6af2e58430cde2e11f1c3712a)
- testpmd adds the show config dcbfwdtc command, which is used to display the DCB forwarding TC list.
  ↳ No PR: [bf8603f](https://github.com/DPDK/dpdk/commit/bf8603f4b18510c1b217857f36fc398e7e49695b)
- mlx5 PMD introduces a mechanism to delay allocation of HWS drop actions to minimize firmware resource usage.
  ↳ No PR: [8831772](https://github.com/DPDK/dpdk/commit/88317720774caefcf8749e097afa0bbe3ea2c1fc)
- Supports the IP fragmentation reassembly function of ordinary packets (non-security offloading), which is implemented by configuring UCAST_CPT rules.
  ↳ No PR: [0702edf](https://github.com/DPDK/dpdk/commit/0702edf0954e57718c0ba7c2f90467709870cf1b)
- Added scatter reception support for jumbo frames to the af_packet driver.
  ↳ No PR: [f4724f3](https://github.com/DPDK/dpdk/commit/f4724f3e9ad5a82ba13eda23a3ad6f96afdcaba3)
- Added the ability to disable Rx tail drop via the devargs parameter drv_no_taildrop for the DPAA2 network card driver.
  ↳ No PR: [954c544](https://github.com/DPDK/dpdk/commit/954c544c67831fe024cb39cfae63d6babe701230)
- Added dependency checks for QinQ TX offloading and VLAN extension mode for i40e driver.
  ↳ No PR: [7e8b3ac](https://github.com/DPDK/dpdk/commit/7e8b3acc4ed01ee7355570600c05d7de3c64166f)
- Updated the setting logic of CN20K inline IPsec profile ID.
  ↳ No PR: [f8b8ed4](https://github.com/DPDK/dpdk/commit/f8b8ed4051274eecd798337135580788917a284d)
- Added CPT code check for soft expiration processing, supporting soft expiration scenario again.
  ↳ No PR: [a3ccdf1](https://github.com/DPDK/dpdk/commit/a3ccdf183632f4732633524e9570d7b73c8dab20)
- Extended pcapng test coverage, added annotation processing tests, random packet size and timestamp wraparound verification.
  ↳ No PR: [de74d16](https://github.com/DPDK/dpdk/commit/de74d16a30ed733943166c7b9d34957ab20e3988)
- Skip Rx adapter test when there is no ethdev and device cannot be created via net_null driver.
  ↳ No PR: [184fbd2](https://github.com/DPDK/dpdk/commit/184fbd22ec590e25c1b216e229c087800c3a78b1)
- Removed the hard dependence on the net_null driver in the eventdev eth Tx adapter test and instead skips the test when the driver is not configured.
  ↳ No PR: [56f1ef1](https://github.com/DPDK/dpdk/commit/56f1ef130fa908972d2f59c5afdb4b6ede35a06b)
- Add an independent unit test suite for TAP PMD, covering device configuration, link status, statistics, MTU, MAC address and other functions.
  ↳ No PR: [210e5bf](https://github.com/DPDK/dpdk/commit/210e5bffa37fc632aaf88871402a83a96e7be627)
- Added multiple new code snippets to the flow_filtering example, covering integrity check flag matching, packet type matching, ECN modification, random matching, VXLAN-GPE/GBP field matching, NVGRE matching and NAT64 action usage.
  ↳ No PR: [3ebb878](https://github.com/DPDK/dpdk/commit/3ebb8789136a5509360c33d4b74095eb6f3783d5)
- Supports dynamic adjustment of the number of RX/TX queues through the port stop/configuration/start process at runtime, and fixes concurrency security issues when VF queues are released.
  ↳ No PR: [7306b83](https://github.com/DPDK/dpdk/commit/7306b83a809415b4e64bd655d597ba0a73cb0cf5)
- Supports jumbo frames, dynamically calculating the maximum received packet length and MTU based on the actual TPACKET ring frame size.
  ↳ No PR: [220a5c7](https://github.com/DPDK/dpdk/commit/220a5c7b75c9ef669c2e2bd9da78d3f6c50a546f)

### bug fixes
- Fixed an issue where the default replication rule was created in the wrong group when sharing flow metadata, and ensured that the REG_C_1 register was always used when sharing flow metadata between E-Switch and VM.
  ↳ No PR: [5b11132](https://github.com/DPDK/dpdk/commit/5b11132a8942abf26ddb80cb7ccce6ffc7fefd3f), [a1cca69](https://github.com/DPDK/dpdk/commit/a1cca690a1e3a46a1ebdede15e09fd282e2ea187)
- Fixed the launch time function problem in the e1000/igc network card driver, including correctly allocating context descriptor and correctly handling the situation when txtime expires or exceeds the Qbv cycle.
  ↳ No PR: [fc9ff0b](https://github.com/DPDK/dpdk/commit/fc9ff0bcabe73a70d5ae8a235601734d89abdd69), [2e79349](https://github.com/DPDK/dpdk/commit/2e79349dcd07440a7aecd61f00792d82e1bfebbc)
- Fixed the IPv6 SRH flex node header length calculation and concurrent initialization issues in the mlx5 driver.
  ↳ No PR: [f9399ef](https://github.com/DPDK/dpdk/commit/f9399efbf39fe16d5a8beda666b72e7312103f99), [1bef695](https://github.com/DPDK/dpdk/commit/1bef69570faf98ea82474dfb02f3d67d5a2d80e1)
- Fixed multiple issues related to flow control, FEC and auto-negotiation in the sfc driver, including flow control mode settings, FEC flag indication, RX_TRUNC_ERR event classification, fixed speed reset and auto-negotiation status reporting.
  ↳ No PR: [133e9ad](https://github.com/DPDK/dpdk/commit/133e9ad7ec1c5636567f96d1a57855768b969e28), [054d17a](https://github.com/DPDK/dpdk/commit/054d17aceb2e14be3bd2dbc53cd18430b0eb2269), [b54143b](https://github.com/DPDK/dpdk/commit/b54143bfd6d57a6fd7062e9f7f44abdbae0248f3), [77bb34e](https://github.com/DPDK/dpdk/commit/77bb34e047e3c6ddbe2c8c1d78d349f46a484325), [a0d1eb6](https://github.com/DPDK/dpdk/commit/a0d1eb6a4e1b8be4cd6209c1186d28ec373611de), [95330ee](https://github.com/DPDK/dpdk/commit/95330ee234cd2d4e60dec4ca7c02bb09e766ce86)
- Fixed the return type and error log logic of tap_mp_req_on_rxtx function in TAP driver.
  ↳ No PR: [d26d69a](https://github.com/DPDK/dpdk/commit/d26d69a054012f77b535da77ee78c108646ee01c)
- Fixed the problem of AF_XDP driver incorrectly triggering zero-copy optimization when transmitting external mbuf, and added a check on whether the mbuf is a direct buffer.
  ↳ No PR: [10ed220](https://github.com/DPDK/dpdk/commit/10ed220497b31182385ca3ac62cd07c20842a4db)
- Fixed MPESW PF detection logic to support any number of ports.
  ↳ No PR: [a3ad6ba](https://github.com/DPDK/dpdk/commit/a3ad6bace70cc229698f4e9b14cb713937d02fa3)
- Fixed flow devargs handling, dynamically set steering defaults based on hardware capabilities, and force disable and output clear logs when incompatible.
  ↳ No PR: [170ebe9](https://github.com/DPDK/dpdk/commit/170ebe941be3a4c2a2bddeff039d62088d2c6463)
- Fixed the problem of mlx5 PMD allocating too many memzones under the default synchronous streaming API configuration, and removed two unused ring objects to avoid memzone exhaustion when a large number of SF probes are performed.
  ↳ No PR: [0da95cc](https://github.com/DPDK/dpdk/commit/0da95cc8c246d41d916c53bd397f942c63214634)
- Fixed an issue with setting redundant control rules in promiscuous mode so that DMAC and multicast/broadcast control flow rules are only created in non-promiscuous mode.
  ↳ No PR: [43a8ff6](https://github.com/DPDK/dpdk/commit/43a8ff69a8c5e5b7dd01cc9a0f2aa3296cebb3a0)
- Fixed errors in batch offset calculation and queried counter number tracking in HW flow counter query, ensuring that counters exceeding 64k can obtain correct values and all counters are queried.
  ↳ No PR: [c2020c1](https://github.com/DPDK/dpdk/commit/c2020c16e972aafbcd8aaa1dc11afca2fd640c61)
- Fixed the bnxt driver's statistics collection failure to aggregate statistics for rings exceeding RTE_ETHDEV_QUEUE_STAT_CNTRS when the number of queues is high.
  ↳ No PR: [e0f92e3](https://github.com/DPDK/dpdk/commit/e0f92e31f72790b63897942e06189a02a12d50b5)
- Fixed the interrupt nesting problem caused by hardware statistics query in the net/nbl driver, and changed the statistics update to a dedicated thread.
  ↳ No PR: [3808404](https://github.com/DPDK/dpdk/commit/3808404c49aa68de55c3602bac20bd496aaaaeba)
- Fixed the Tx scheduler level priority configuration in the ice driver, allowing strict priority to be set at the non-root level again.
  ↳ No PR: [45f435d](https://github.com/DPDK/dpdk/commit/45f435ddf758edb74cee2b36bb8d2c9054e824f6)
- Fixed the problem that the key length was not updated correctly when obtaining RSS hash configuration in ixgbe and e1000 drivers.
  ↳ No PR: [23e5d5e](https://github.com/DPDK/dpdk/commit/23e5d5ed70c89715d1a29ee780ade74c8aab1998)
- Fixed length attribute on flex parser creation, set workaround bit for all length modes, and updated eCPRI and IPv6 SRH internal parsers.
  ↳ No PR: [1d67f4e](https://github.com/DPDK/dpdk/commit/1d67f4e2cd0b85f3972bf3252494b035667b5c15)
- Fixed the stack alignment problem when compiling ASan, and added 64-byte alignment macros for local variables in multiple functions.
  ↳ No PR: [4c3d838](https://github.com/DPDK/dpdk/commit/4c3d83867c1fe17d8bbc803064f62a96fbb25d98)
- Fixed the null pointer dereference problem that may occur when the represented_port mode item in the template API lacks spec.
  ↳ No PR: [131cf20](https://github.com/DPDK/dpdk/commit/131cf206f19a789cd0686c8c2052b60c22581b9a)
- Fixed the issue where the reserved TBL8 count was not incremented correctly when prefixes were added in FIB and FIB6 to avoid integer overflow.
  ↳ No PR: [3ad9ad9](https://github.com/DPDK/dpdk/commit/3ad9ad9e362b1c114dc6103ee5a1394048fd78c0)
- Mark the portal pointer of the idxd device as volatile and perform type conversion when unmapping to maintain consistency.
  ↳ No PR: [ab797d5](https://github.com/DPDK/dpdk/commit/ab797d5bcf268e4ac7f2a856568bfcefd3cdb027)
- Fixed the memory leak caused by memzone not being released when the queue is released in the net/nbl driver.
  ↳ No PR: [b6fd866](https://github.com/DPDK/dpdk/commit/b6fd866d91ed14a1d9f6c96fcacbf49b510072ab)
- Fixed the mbuf header space usage problem when sending data packets in the net/nbl driver to avoid data corruption caused by modification of the shared mbuf.
  ↳ No PR: [8e138e8](https://github.com/DPDK/dpdk/commit/8e138e870f9b52069afd3a328521d06c435fa275)
- Fixed the mbuf double release problem that may occur during queue cleaning, adjusted the port stop process and optimized the TX/RX ring release logic.
  ↳ No PR: [43ed974](https://github.com/DPDK/dpdk/commit/43ed974c6976af0df3383ca0d793021204a1a1f3)
- Fixed the problem of only evaluating one execution branch when a BPF program starts with a conditional jump, and added related test cases.
  ↳ No PR: [5b3ef93](https://github.com/DPDK/dpdk/commit/5b3ef932bee6da8b40ed54f41ef7185240833dde)
- Fixed pcapng comment buffer overflow issue, use dynamic allocation instead to support arbitrary length comments, and still log packets when allocation fails.
  ↳ No PR: [5dbc403](https://github.com/DPDK/dpdk/commit/5dbc403830c1f3d7a367d436c2420331083615f8)
- Add length check when copying delay statistics name, and record warning log if the name is too long.
  ↳ No PR: [20fae57](https://github.com/DPDK/dpdk/commit/20fae57ec6b109894fc589bc9b98526345c92c1f)
- Added length check in Unix domain socket path replication to prevent security issues caused by path overflow.
  ↳ No PR: [2c31e12](https://github.com/DPDK/dpdk/commit/2c31e126c3104a0dc3c2b02e34539dead7991415)
- Fixed the buffer size of address strings in memory telemetry information to prevent address overflow.
  ↳ No PR: [f272d54](https://github.com/DPDK/dpdk/commit/f272d54984d9c9928b74182ea04f244205e8a4a0)
- Added overflow check when constructing large page file path to prevent buffer overflow caused by too long path.
  ↳ No PR: [0a6695f](https://github.com/DPDK/dpdk/commit/0a6695f256814bc52c7692fa634050fbd354a49a)
- Use dynamically allocated buffers instead of fixed-size arrays to avoid the problem of possible truncation when the driver library path is spliced.
  ↳ No PR: [11fb9a0](https://github.com/DPDK/dpdk/commit/11fb9a028cc3e31942788320e75617d88067fa46)
- Fixed the Tx statistics accumulation error in the net/null driver. Change the assignment of opackets and obytes to accumulation to ensure that the statistics of all Tx queues are correctly aggregated.
  ↳ No PR: [db55352](https://github.com/DPDK/dpdk/commit/db55352a153328fb8dfc4d74c0578a7f1e1bd987)
- Use hardware constant values instead of dynamically variable queue numbers, fix the way to get the maximum Rx/Tx queue number in the nfb driver, and adjust the status setting when the device is stopped.
  ↳ No PR: [1951820](https://github.com/DPDK/dpdk/commit/195182056289519f48b76d25dcc414abad7de0c1)
- Fixed the null pointer dereference problem of the queue statistics function in the net/nfb driver, and fixed the error of misuse of pointer array as structure array.
  ↳ No PR: [5052a81](https://github.com/DPDK/dpdk/commit/5052a816aead1ba09cc11b7d9cf080cdae1de869)
- Fixed the problem of net/nfb driver stopping unstarted queues when startup fails, instead only stopping the started queues.
  ↳ No PR: [0464ec1](https://github.com/DPDK/dpdk/commit/0464ec16a1a118b3092159a2fe5964e46b4c4ae7)
- Fixed the asynchronous stream operation queue job leak problem in testpmd. The life cycle of queue_job is managed through a linked list to ensure that all unprocessed jobs are released before exiting.
  ↳ No PR: [df503d7](https://github.com/DPDK/dpdk/commit/df503d757b3601be7cd85c646c5300c07cbe4595)
- Fixed a null pointer dereference issue in IPsec flow parsing in the ixgbe driver to avoid crashes and undefined behavior.
  ↳ No PR: [eb3de5f](https://github.com/DPDK/dpdk/commit/eb3de5f328afbff3a1abd2184052355b4fe4a981), [b2eb30b](https://github.com/DPDK/dpdk/commit/b2eb30b5c286bb454fc0fe6a041263f33e9717ce)
- Fixed the null pointer dereference problem in the nbl_dev_configure function and moved the debug log after the null pointer check.
  ↳ No PR: [fd573c1](https://github.com/DPDK/dpdk/commit/fd573c1c5fa125324dd696094f9d82012b307e79)
- Fixed a compilation error caused by uninitialized variables in the iavf driver under the minsize build option.
  ↳ No PR: [7c8bfad](https://github.com/DPDK/dpdk/commit/7c8bfad0ca350345a930d90365bb32f4de74a212)
- Fixed the problem of uninitialized variables caused by not checking the return value in the bnxt driver's ulp_blob_append function.
  ↳ No PR: [374125f](https://github.com/DPDK/dpdk/commit/374125fc8508efd83cfb6896639cc04e3e5d951c)
- Fixed a compilation error caused by uninitialized variables in the intel_pstate driver under the minsize build option.
  ↳ No PR: [64231ea](https://github.com/DPDK/dpdk/commit/64231eacd38b48aa791d628385c9f41d6cdedffd)
- Fixed the memory leak caused by not releasing sw_ring when TX queue setup failed in cpfl and idpf drivers.
  ↳ No PR: [6528c61](https://github.com/DPDK/dpdk/commit/6528c61f17f7f7732340768049e1931e84c942af)
- Fixed uninitialized variable warning for GFNI code in hash library, explicitly zero-initialize relevant variables to eliminate false positives.
  ↳ No PR: [32cdf06](https://github.com/DPDK/dpdk/commit/32cdf0611b570b49fcee799d080656e3bfbed8e5)
- Fixed the FDIR filter initialization and configuration timing issue in the i40e driver. The initialization and configuration logic was removed from the parsing function and executed during flow create to avoid incorrectly modifying the FDIR status during flow validate.
  ↳ No PR: [59acde9](https://github.com/DPDK/dpdk/commit/59acde9b24725d0bc3ad745773749c3b798c7896)
- Fixed the IPv6 GTPU stream parsing error in the i40e driver, and added the processing of IPv6 stream mode items.
  ↳ No PR: [089e093](https://github.com/DPDK/dpdk/commit/089e093ee9e6d3bea5721dc17c79091aa59114b2)
- Fixed the memory leak problem of the egress IPsec stream in the iavf driver. By correctly marking the stream and adding it to the queue, it ensures that the memory can be released normally when destroyed.
  ↳ No PR: [e783da1](https://github.com/DPDK/dpdk/commit/e783da175250095e65d39bc8a97631f1725f3256)
- Fixed a memory leak caused by the iavf driver not cleaning up the IPsec engine when uninstalling.
  ↳ No PR: [c7f7b3a](https://github.com/DPDK/dpdk/commit/c7f7b3ab32fd8da9023599c363b448d54f6c9a09)
- Fixed an error in calculating the number of bytes in the input set when subscribing to IPv4 streams in the iavf driver, and corrected the number of bytes in the IPv4 source address and destination address from 2 bytes to 4 bytes.
  ↳ No PR: [9b1780d](https://github.com/DPDK/dpdk/commit/9b1780d392b21e6c8e5d89a4c01503105e4372bd)
- Fixed memory leak in DCF QoS bandwidth configuration, replaced temporary buffer allocation from rte_zmalloc to calloc, and added free operation in failure path.
  ↳ No PR: [efd5d15](https://github.com/DPDK/dpdk/commit/efd5d15a886b51f8abd2315d5666cdd78814212a)
- Fixed the RAW mode memory leak in ice FDIR parsing, releasing the pkt_buf buffer under the verification path, and uniformly using rte_zmalloc to allocate memory.
  ↳ No PR: [3a3a249](https://github.com/DPDK/dpdk/commit/3a3a249bc595627a81dd1e9cc0a93993736a6871)
- Fixed the null pointer crash caused by the lack of PHY MCU configuration function pointer during RTL8168FP initialization, and added a new hw_phy_mcu_config_8168fp function with no operation.
  ↳ No PR: [5887ff7](https://github.com/DPDK/dpdk/commit/5887ff7505a4d599b2e971f42962156f2123a158)
- Fix the speed classification of the RTL8168KB chip and remove it from the 2.5G device list (the chip actually supports a maximum of 1Gbps).
  ↳ No PR: [503c136](https://github.com/DPDK/dpdk/commit/503c13691b4969ea649c964c477ae6b4df629d58)
- Fix the issue of incorrect link status reporting after binding PMD, make sure to use the old mapping.
  ↳ No PR: [356b354](https://github.com/DPDK/dpdk/commit/356b3541b73febc5f37b3b9a075776c2e30dd624)
- Fixed the bit mask logic error when setting 1G and 10G capabilities in the RTL8127 network card driver.
  ↳ No PR: [972a46c](https://github.com/DPDK/dpdk/commit/972a46ca1ccf06adb7de2e5f286176310c4c71bb)
- Fix the issue in the iavf driver where the Tx queue flag is incorrectly set after path selection, ensure that the use_ctx and use_vec_entry flags are always correctly configured, and simplify the flag setting logic.
  ↳ No PR: [258da17](https://github.com/DPDK/dpdk/commit/258da170bb760560ba37a8babe8b5437c345b377)
- Fixed the problem of packet loss caused by too long comments when copying pcapng: when there is insufficient tail space, additional mbuf segments are automatically allocated and linked to accommodate comments of any length.
  ↳ No PR: [2aae0e6](https://github.com/DPDK/dpdk/commit/2aae0e66b4ef84a0a7c310552714dcc92e27d260)
- Fixed the problem that the Tx queue in the mlx5 driver may crash due to null pointer dereference when starting, and move the assignment of txq_data after the NULL check.
  ↳ No PR: [c3a666f](https://github.com/DPDK/dpdk/commit/c3a666ff87cb5c6f121118191d6bff9e0d3777c3)
- Fixed a counter leak issue caused by incorrect paths not destroying allocated DevX queue counter objects when per-queue hairpin counters are enabled.
  ↳ No PR: [c9a11e9](https://github.com/DPDK/dpdk/commit/c9a11e93f142b877c027b94cd6167d3cb083842e)
- Fixed the use-after-free problem in the mlx5 driver caused by the shared context pointer not being cleared after initialization failure of ASO management.
  ↳ No PR: [07d527b](https://github.com/DPDK/dpdk/commit/07d527b2e268599a80b7464866856bbf45fd07bc)
- Fixed the truncation problem when reading the queue counter in the mlx5 driver to ensure that the 64-bit counter value is read correctly.
  ↳ No PR: [614cae8](https://github.com/DPDK/dpdk/commit/614cae8a82c2e03091eaaf2cce4e3c93bf99c86c)
- Fixed the loop condition check error in the CN9k platform engine capability acquisition logic.
  ↳ No PR: [aa65682](https://github.com/DPDK/dpdk/commit/aa656824205dac6b55dfde7551cb8f50a5d98569)
- Fixed an issue where the fast path security flag was incorrectly enabled under custom inbound SA configuration.
  ↳ No PR: [b38522a](https://github.com/DPDK/dpdk/commit/b38522ad7338e7a9654774dbf5adc19858b22526)
- Fixed an issue where the auxiliary process in the i40e driver could not correctly select the Rx path when the device was not started.
  ↳ No PR: [6662ed2](https://github.com/DPDK/dpdk/commit/6662ed2481885b9e27052d02f67f4bd3caedd9d0)
- Fixed the problem in the iavf driver that the secondary process cannot correctly select the Rx path when the device is not started.
  ↳ No PR: [7d0126b](https://github.com/DPDK/dpdk/commit/7d0126bc830280a0e73c7c9429177e5d0d9090bf)
- Fixed the issue in the ice driver where the secondary process cannot correctly select the Rx path when the device is not started.
  ↳ No PR: [04a766b](https://github.com/DPDK/dpdk/commit/04a766bf7cbc3d614ad39f19e83269b049d121e2)
- Allow the auxiliary process to choose the sending path by itself when the device has not been started, and fix the problem that the auxiliary process cannot correctly select the sending function when the main process has not started the device, involving multiple Intel network card drivers.
  ↳ No PR: [af7ae88](https://github.com/DPDK/dpdk/commit/af7ae88302578da576ad898be044c8f14c433dfa)
- Fix the use-after-free problem of vhost fdset when closing, change the fdset allocation from rte_zmalloc to libc's calloc.
  ↳ No PR: [21d9fb6](https://github.com/DPDK/dpdk/commit/21d9fb6badad050cfee7c5d879d5e2190ad01648)
- Fixed the issue of using the wrong structure size when obtaining IPsec status in the iavf driver.
  ↳ No PR: [4743815](https://github.com/DPDK/dpdk/commit/47438158efc2bd0fcd81de6c3ea1d335640f630e)
- Fixed the problem that TAP PMD may miss some queues when counting queue statistics, and changed the statistics clearing method to use memset.
  ↳ No PR: [abacc3b](https://github.com/DPDK/dpdk/commit/abacc3b2dac34bd0cafe23c95902730b0ace8bff)
- Extend the interface index of fixed MAC address from single byte to two bytes to avoid duplicate MACs when hot-plugging more than 256 devices.
  ↳ No PR: [804462a](https://github.com/DPDK/dpdk/commit/804462ac4390ece28e9f49dc2d19fbde6699d7ab)
- Fix resource leak when net/tap device creation fails: ensure process_private memory is released, and allocated ethdev ports are properly released when memory allocation fails.
  ↳ No PR: [8c7751d](https://github.com/DPDK/dpdk/commit/8c7751daa8a879f46b67969e1b995a99ed010869)
- Fixed the resource leak problem during secondary process detection, and correctly released eth_dev and process_private in the wrong path.
  ↳ No PR: [65d0b2f](https://github.com/DPDK/dpdk/commit/65d0b2fbb3f451baf6819ec0cc724897a99965eb)
- Fixed the memory leak problem caused by the IPC reply buffer not being released when the number of queues in the tap driver does not match.
  ↳ No PR: [86a3ffe](https://github.com/DPDK/dpdk/commit/86a3ffe64f4e2cdde9ebe9c05b737a185c77034a)
- Fixed the use-after-free problem in the net/tap driver when remote stream creation failed, and correctly deleted the local TC rule and removed it from the linked list before releasing the stream.
  ↳ No PR: [df92002](https://github.com/DPDK/dpdk/commit/df92002ddbc856858ebca2c8fa42d975573049ee)
- Fix the memory leak problem when creating implicit rules in the tap driver, and ensure remote_flow is released when the kernel returns EEXIST.
  ↳ No PR: [d08dd4f](https://github.com/DPDK/dpdk/commit/d08dd4fd79ec0640c7efa9987e36d49af2997710)
- Replace variable length arrays in the tap driver send path with fixed size arrays, add receive path MAC filtering checks, and enable VLA warnings.
  ↳ No PR: [02df7e9](https://github.com/DPDK/dpdk/commit/02df7e9bf30eb09b395c4c26b9408781f33d1623), [812a335](https://github.com/DPDK/dpdk/commit/812a335db4430b078f7cc9c8f57e704a5fa2c980)
- Fixed the configuration problem of the slow Rx queue in the bonding driver, limiting the idle threshold to a quarter of the ring size to avoid driver failure in small rings due to the default threshold being too large.
  ↳ No PR: [db0d974](https://github.com/DPDK/dpdk/commit/db0d974a19cda17fa88896412fc0bcecb6d8a6a3)
- Remove unnecessary huge page memory allocation in the i40e driver, change temporary variables to static arrays on the stack or ordinary calloc/free, and fix the issue where outer VLAN stripping is accidentally disabled after enabling VLAN strip.
  ↳ No PR: [8ea9e78](https://github.com/DPDK/dpdk/commit/8ea9e7801a09b3780be916c7d67cb4253f38d4a2)
- Add forwarding status check for testpmd's DCB forwarding TC configuration command to prevent the configuration from being modified during the forwarding process.
  ↳ No PR: [2d09d6a](https://github.com/DPDK/dpdk/commit/2d09d6a598112ca65fa1b297d39893e0c33e04e2)
- Defer qdisc initialization until rte_flow rules are created to avoid printing error logs when not needed.
  ↳ No PR: [d8e87f2](https://github.com/DPDK/dpdk/commit/d8e87f26d04bdce0f4daebb639a7d8c80dec1438)
- Fixed errors in conditional compilation instructions in process.h and simplified #ifdef structure.
  ↳ No PR: [e859751](https://github.com/DPDK/dpdk/commit/e859751ca016d33fd31956a69621402528fa1f77)
- Fix wrap check issue in simple Tx scalar path to ensure tx_tail is correctly reset to 0 instead of ring_size when the transmit burst ends exactly at the last descriptor of the ring.
  ↳ No PR: [600a43a](https://github.com/DPDK/dpdk/commit/600a43aeddebc1d7b3e4a4cb2285f691eef5e8d7)
- Fixed a resource leak in the net/mana driver caused by Protection Domains not being released when the device is closed.
  ↳ No PR: [5906f9b](https://github.com/DPDK/dpdk/commit/5906f9b6abf4318c9464db4438e85e0507f6a0cb)
- Fixed the memory leak problem of device parameters during VF hot plug, releasing devargs in both cleanup paths of hot plug retry and device shutdown.
  ↳ No PR: [fe2b03b](https://github.com/DPDK/dpdk/commit/fe2b03b6c950f29010f1abd694242747a4dc59e7)
- Fixed the problem that the auxiliary process cannot correctly set the fast path operation structure in the hot-plug scenario, ensuring that it can access the device's transceiver queue array and update the burst function pointer.
  ↳ No PR: [a5d0e9f](https://github.com/DPDK/dpdk/commit/a5d0e9f61c30127af637bf68838f8ac1dd5aecdf)
- Fixed the issue where the secondary process cannot correctly update the fast-path queue data pointer and burst function pointer during hot plugging to avoid segmentation faults caused by using stale pointers.
  ↳ No PR: [36a34a5](https://github.com/DPDK/dpdk/commit/36a34a5cb7569f6fa672fe7fed33a9be06c43ec8)
- Fixed the problem of commas being misused as semicolons in the bnxt ULP driver, and eliminated the warning triggered by the -Wcomma flag when compiling with clang.
  ↳ No PR: [e99612b](https://github.com/DPDK/dpdk/commit/e99612b26f6be4324ba0af372964d883789d9345)
- Fixed issue where queue statistics count continued to grow in port stop/start loop, use queue count from device data instead.
  ↳ No PR: [448bd23](https://github.com/DPDK/dpdk/commit/448bd23d0ef3601632a5b54b46e38ce9794c4101)
- Fix the timestamp calculation error caused by calling the copy function before the file is opened in the pcapng module, and handle the case where the TSC difference is negative.
  ↳ No PR: [77f831b](https://github.com/DPDK/dpdk/commit/77f831b6f12b78a9ae6391a21f6114fc1941a071), [bb09367](https://github.com/DPDK/dpdk/commit/bb09367b15ce28ffb75b7e16f1c1fcd4dfdcfde1)
- Fixed the MAC speed setting error in SGMII 100M mode, changed it from 1G to 100M, and added the corresponding PHY implementation.
  ↳ No PR: [11b9189](https://github.com/DPDK/dpdk/commit/11b918959cd924fc6ad09d8cae1a86411490218a)
- Fixed the problem of residual descriptor flags in the memif driver Tx path, and ensured that the descriptor status was clean during each transmission through direct assignment instead of bitwise OR operation.
  ↳ No PR: [f7a5220](https://github.com/DPDK/dpdk/commit/f7a52200d4c2d12c0a35e643cb1d6fd45b21ccb7)
- Fixed the resource leak problem caused by sub-channel not being closed when the device is removed in the net/netvsc driver.
  ↳ No PR: [cfd239b](https://github.com/DPDK/dpdk/commit/cfd239bd7c5250f790b7fa4c0e7d8cd0a65ca808)
- Fixed the problem of repeated release of the main receive queue by the netvsc driver when canceling initialization, and removed redundant release calls.
  ↳ No PR: [d2e85dc](https://github.com/DPDK/dpdk/commit/d2e85dc8144995b595021d08a14de6ee5e0ad72d)
- Fix the resource leak of net/netvsc driver when initialization fails, and ensure that the main channel and primary structure are released correctly.
  ↳ No PR: [7971a12](https://github.com/DPDK/dpdk/commit/7971a129ef27e35b7ea9a4e977193476c063640e)
- Fixed the resource leak problem caused by not logging out of the device event callback when the Rx filter fails in the net/netvsc driver.
  ↳ No PR: [134ae1d](https://github.com/DPDK/dpdk/commit/134ae1dc0e36d19d04f2288ffab71d1290b0579d)
- Fixed the resource leak problem when MTU changes: correctly close the VMBus channel, release rxbuf_info and re-initialize the chimney bitmap; at the same time, add a hot-plug callback in hn_dev_start/stop to log out and clear the pending TX completion.
  ↳ No PR: [980b54a](https://github.com/DPDK/dpdk/commit/980b54aaa21e92382e11f55d316e5ba38de990c6)
- Fixed the busy loop problem caused by undetected disconnect/error events in DevX interrupt handling in the mlx5 driver, by checking the interrupt event flag and unregistering the callback.
  ↳ No PR: [bf0bbe0](https://github.com/DPDK/dpdk/commit/bf0bbe03b6db90478216961fd5cfff984a8c5391)
- Fixed the issue where the eventdev/eth_rx adapter crashed when passing an out-of-range port ID through the telemetry interface, and changed the eth_dev_id type from int to uint16_t.
  ↳ No PR: [ca972f6](https://github.com/DPDK/dpdk/commit/ca972f6c6430775b57f2e7e24d6a568552a9ea81)
- Fixed an issue in the iavf driver where setting the default MAC address when the VF was not started resulted in failure to delete the primary MAC, by introducing the mac_primary_set flag to ensure that deletion of the old address is only attempted when the primary MAC has been set.
  ↳ No PR: [d1e2005](https://github.com/DPDK/dpdk/commit/d1e200594b98b6126e77bd910c0c452543b97f8b)
- Fixed a crash on CN10K caused by a null event_dev pointer, and added a null pointer check in polling mode.
  ↳ No PR: [f181c1e](https://github.com/DPDK/dpdk/commit/f181c1e2897eaf9defdabfcf9d641cf1b77436bf)
- Fixed the problem of label insertion order being wrong when uninstalling QinQ under AVX512 path, making it consistent with single package functions and scalar paths.
  ↳ No PR: [079095d](https://github.com/DPDK/dpdk/commit/079095da2a7e2d62f46893f34f6e094e381ebd75)
- Fixed the dangling pointer problem of SHA and SHAKE tests in the FIPS verification example, and empty the vector pointer after release to avoid repeated release.
  ↳ No PR: [ba665ac](https://github.com/DPDK/dpdk/commit/ba665acecbfe510f5f961f5539ddea6d162ed4cc)
- Add a check for invalid topology in ice_sched_add_node, return an error in advance and record a warning when the parent node does not prepare child nodes, to avoid crashes caused by abnormal topology information after NVM update.
  ↳ No PR: [12e1ee7](https://github.com/DPDK/dpdk/commit/12e1ee7b2d89237ac4fc7f1079f9fa42afac1f7f)
- Fix the E830 device clock adjustment timer programming sequence, and add a write command register to make the adjustment take effect.
  ↳ No PR: [f9767f7](https://github.com/DPDK/dpdk/commit/f9767f70cb73429739954491d532951de1ba0165)
- Fixed data size calculation for MTU settings in the af_packet driver to be consistent with the queue initialization path, thereby accepting all valid MTU values.
  ↳ No PR: [b1cd278](https://github.com/DPDK/dpdk/commit/b1cd278e97315fc4c19d4157a54d05e974a8d121)
- Fixed the error of unused variables when removing MAC/VLAN filter in i40e driver, and optimized the error handling logic.
  ↳ No PR: [0acd1bb](https://github.com/DPDK/dpdk/commit/0acd1bb678d8df61d4c55a5a236dae8de1538b7c)
- Fixed the problem that batch_info in ulp_stats_cache_main_loop in bnxt driver is read without initialization, and avoids potential errors through zero initialization.
  ↳ No PR: [aff31f4](https://github.com/DPDK/dpdk/commit/aff31f4ea10a1653731439ba20a79bb9d6c3844d)
- Fixed the resource leak problem caused by not closing the file descriptor when parsing the mbuf history command in testpmd.
  ↳ No PR: [f3b9adc](https://github.com/DPDK/dpdk/commit/f3b9adc8c02df3ba1318a276fa1646c30c6e4fcb)
- Fixed the leakage problem of the meter ASO action in the mlx5 driver when it is released back to the pool. By saving and restoring the action pointer, it ensures that the cached action is still valid after the pool is recycled, and is destroyed correctly when closing.
  ↳ No PR: [b74b425](https://github.com/DPDK/dpdk/commit/b74b4258cb03a796cb3dbb93df2da86ca58b10ce)
- Fixed the abnormality in DCB forwarding in testpmd caused by the inconsistent number of TCs between ports, by taking the minimum value of Rx and Tx TCs as the effective TC count, and adding a check on the validity of the Tx queue.
  ↳ No PR: [388bb5d](https://github.com/DPDK/dpdk/commit/388bb5d87a4e88182fc625f6d23e68fe790f2f25)
- Fixed the problem that tx_skew was not set correctly in wait on time mode, moved skew initialization to the shared device context allocation stage, so that it takes effect for both sending scheduling modes.
  ↳ No PR: [cf69152](https://github.com/DPDK/dpdk/commit/cf69152295fa8d777ea0869f3ac33b8e4f11680d)
- Fix MAC address deletion failure in mlx5 driver on Linux, and always enable debug logs to aid diagnosis.
  ↳ No PR: [c62ff2e](https://github.com/DPDK/dpdk/commit/c62ff2e6d48b83fb423bea21da98aceb4a00ef41)
- Fixed the error in the flow type setting of the inner tunnel item in the ice driver, limiting the inner protocol tracking conditions to only apply to L2TPv2 tunnels, to avoid affecting FDIR rules of tunnel types such as VXLAN and GTPU.
  ↳ No PR: [0a2fa57](https://github.com/DPDK/dpdk/commit/0a2fa57e63b671b9d96ee5bf60ef7ef421fbb252)
- Fix the missing check for flex parser capabilities when creating flex items, avoid reporting irrelevant error messages under old firmware, and update the limitation description in the documentation simultaneously.
  ↳ No PR: [120a175](https://github.com/DPDK/dpdk/commit/120a1757c1bff5cef7280f755faf1cfb8622d86c)
- Fixed the memory leak problem caused by not releasing the old job_list when executing the flow configure command multiple times in testpmd.
  ↳ No PR: [7fadc80](https://github.com/DPDK/dpdk/commit/7fadc803958843ced984faaa4ca2a75b5d3c1d4f)
- Removed the error check that the spec and mask lengths must be equal when validating raw flow items in the i40e driver, and fixed the problem of flow being rejected when using the default mask.
  ↳ No PR: [d181b00](https://github.com/DPDK/dpdk/commit/d181b00172f0b7fc9a559df153518a4e20eb14a6)
- Fix net/memif multi-segment Rx data corruption problem: move dst_off initialization to be executed only once per package to avoid overwriting data during chain descriptor processing; at the same time, add boundary checks in both Rx paths to prevent out-of-bounds reads when n_slots is 0. Update statistical counts to record new errors.
  ↳ No PR: [40e0e7c](https://github.com/DPDK/dpdk/commit/40e0e7c0a2236adde8c398515619347d9948b8d3)
- Fixed issue where share group and queue IDs were not reported when getting Rx queue information via rte_eth_rx_queue_info_get().
  ↳ No PR: [349b40a](https://github.com/DPDK/dpdk/commit/349b40a677e2efc69bec10ed36e86459ac4d44cc)
- Fixed the logic of CQE suppression processing when error completion in the net/mana driver. Reading is now only skipped when the CQE type is normal completion, avoiding consumer index misalignment and subsequent misreading and memory problems caused by skipping error CQE.
  ↳ No PR: [823dbf2](https://github.com/DPDK/dpdk/commit/823dbf286053c1cc4231a5828ffc300a70f4f510)
- Fixed the kernel warning caused by the data path not switching back to synthetic when the netvsc device is stopped. Switch the data path before stopping the VF, switch back after starting the VF, and change the read lock to a write lock.
  ↳ No PR: [da1fcd9](https://github.com/DPDK/dpdk/commit/da1fcd9b36d8d6e0dd87518ad675ccc61addf43f)
- Fixed the hardware register selection logic of NAT64 stream action, when REG_C_6 is unavailable, the last three available tag registers are used instead.
  ↳ No PR: [145a945](https://github.com/DPDK/dpdk/commit/145a94542445005549c64293c79c351aa40a4aa4)
- Fix EC session crash due to missing key in QAT driver: fix session_set_ec() check for key field, zero-initialize xform structure in test case, and add unsupported curve ID error log in pick_curve().
  ↳ No PR: [90e0f1b](https://github.com/DPDK/dpdk/commit/90e0f1bf091650844809f6df55f7a78fd884763f)
- Fixed the support issue of axgbe driver under 100 Mbps link: corrected the width of MAC transmit configuration register speed selection field to 3 bits to match the hardware specification, added 100 Mbps MAC speed selection support, and corrected the macro definition of auto-negotiation capability to ensure that link modes such as 10baseT and 100baseT are correctly advertised.
  ↳ No PR: [04c921f](https://github.com/DPDK/dpdk/commit/04c921fa73919a9b9cac5cbad5dd8d1f841c4508), [8d3e276](https://github.com/DPDK/dpdk/commit/8d3e276a37e7b0db936b5885a71e234d5e719284), [444befa](https://github.com/DPDK/dpdk/commit/444befa09f47d584919d8642b3f8c0d3a925a121)
- Fixed the RSS LUT access issue in the ice driver. When VSI allocates a global LUT, the global LUT parameters are correctly used instead of the PF LUT parameters.
  ↳ No PR: [6ca9244](https://github.com/DPDK/dpdk/commit/6ca92441c4c648fbb02d34febcc1fd8f08fc649a)
- Fixed the issue of queue memory leak caused by early emptying of rx_vq[0] in the loop when the dpaa2 driver closes the port. Instead, the base pointer is saved and then released before the loop.
  ↳ No PR: [acc7882](https://github.com/DPDK/dpdk/commit/acc78825a671d21e687a717c774f52dceea4dec3)
- Fixed the memory leak problem of the Rx error queue in the dpaa2 network card driver, and added missing free and null pointer assignments on the port closing and allocation failure paths.
  ↳ No PR: [f9b31cf](https://github.com/DPDK/dpdk/commit/f9b31cf4a64e60d88dcf157da6000247a5279b49)
- Fixed false positives for Rx descriptor number warnings in the net/dpaa2 driver: only issue a warning when DPNI enables high-performance buffering mode (PFDR in PEB) and the total number of descriptors exceeds 11264, to avoid misleading noise in normal buffering mode.
  ↳ No PR: [69226df](https://github.com/DPDK/dpdk/commit/69226df1cf0e05a2dd0949f2f6f8698ee915bdda)
- Fixed an issue where allocated resources were not released when the soft parser failed to load or enable, and ensure that error paths are properly cleaned up.
  ↳ No PR: [ec7e017](https://github.com/DPDK/dpdk/commit/ec7e017938f3f8dfaa5494bb26810e5803730e45)
- Fixed the problem that the link status of the dpaa2 network card cannot be updated correctly after the port is stopped/started: move the link start operation to LSC after interrupt registration to ensure that the link up event is not missed.
  ↳ No PR: [d1e3247](https://github.com/DPDK/dpdk/commit/d1e32473d1145870fc26e8a9241d3a41014c457e)
- Fixed an issue where device parameters were not propagated correctly during fslmc bus hot swapping, refreshing devargs of existing devices during rescan.
  ↳ No PR: [10f30d4](https://github.com/DPDK/dpdk/commit/10f30d4d32f1252d7485db1714c3c96630b77217)
- Fixed the problem in the dpaa2 driver that non-VLAN packets were incorrectly inserted into the VLAN header. VLAN insertion is now only performed based on the flag bit of each packet.
  ↳ No PR: [a61868f](https://github.com/DPDK/dpdk/commit/a61868f19e0fc74842579c1b1efb450f022e4c78)
- Fixed three defects in the dump_err_pkts() function: null pointer dereference, multi-segment message memory leak and segment serial number not reset.
  ↳ No PR: [e7cd393](https://github.com/DPDK/dpdk/commit/e7cd393f30a232165f75bb003b9e2e8d92208132)
- Fixed L4 packet type setting error in dpaa2 driver slow parsing path, moved NONFRAG flag to last as default value, and fixed handling of IP and L4 checksum flags.
  ↳ No PR: [c94e6dd](https://github.com/DPDK/dpdk/commit/c94e6dd8fa5c932bca12b53a1e17c0930b8301c5)
- Fixed the L3/L4 checksum flag reporting issue in the dpaa2 driver: use independent if statements to report L3 and L4 checksum errors simultaneously, and correctly mark the GOOD status when the check passes.
  ↳ No PR: [6435a1d](https://github.com/DPDK/dpdk/commit/6435a1d00a149dc32020a3fcf8268401c733c0f0)
- Fixed buffer access out-of-bounds and memory leak issues in the taildrop path of the dpaa2 driver software, using the same release mode as the ordered send path instead.
  ↳ No PR: [3cb5e69](https://github.com/DPDK/dpdk/commit/3cb5e6929f97f171bc1d0211bbee2ea0104c6eec)
- Fixed the dpaa2 network card burst mode information acquisition function so that it correctly reports the actual burst function pointer used instead of only listing the configured offload flag, and corrected the problem of only displaying the first offload.
  ↳ No PR: [a86fd77](https://github.com/DPDK/dpdk/commit/a86fd775331c166d3fd2b3c19bf634e42d319eb1)
- Added an upper limit to the SG table traversal in the Rx path of the dpaa2 network card driver to prevent out-of-bound access caused by not setting the FINAL bit.
  ↳ No PR: [e8c04ef](https://github.com/DPDK/dpdk/commit/e8c04ef2182ec61fbcb639f1089e2ab63144d3ab)
- Move the allocation of MAC statistics DMA buffer from each xstats call to the device initialization phase and release it on shutdown to avoid resource waste and thread safety issues.
  ↳ No PR: [d910d1b](https://github.com/DPDK/dpdk/commit/d910d1bbc23efab3e420bd68b312ef48e017889e)
- Fixed the issue where the hardware was repeatedly re-initialized after downloading the backup scheduler topology, and removed redundant initialization steps in the calling code.
  ↳ No PR: [6d317b4](https://github.com/DPDK/dpdk/commit/6d317b464e7ba5e9d674bf0dfe9ee38207495c50)
- Fixed the crash issue caused by the tap network card driver accessing the uninitialized receive queue when some configured ports are closed.
  ↳ No PR: [eb73716](https://github.com/DPDK/dpdk/commit/eb73716c39ad8c4af057a63f0740a0b329e6f706)
- Modify the SGMII auto-negotiation status bit definition in the AXGBE driver to align the link status and duplex mode bits with the hardware specification.
  ↳ No PR: [973854f](https://github.com/DPDK/dpdk/commit/973854fe4b7ec8bc03539dc6c27ca0168f4296ae)
- Fix the FEC capability check logic to ensure that it can correctly verify whether the FEC mode is supported by the current link speed even when the port is not started.
  ↳ No PR: [2b57b2b](https://github.com/DPDK/dpdk/commit/2b57b2b654054fe918a74b888865f40214e66689)
- Fix insufficient mempool name buffer size in ethtool example, use RTE_MEMPOOL_NAMESIZE macro instead and correct snprintf length parameter.
  ↳ No PR: [b3a5c32](https://github.com/DPDK/dpdk/commit/b3a5c3281d8accc2d8dc4c0e878302a7b791792c)
- Fixed the variable shadowing problem of the ixgbe_fdir_info_get function in the ixgbe driver.
  ↳ No PR: [9ae0429](https://github.com/DPDK/dpdk/commit/9ae0429758394c7590fd1f4cade3adf9ef833f75)
- Fixed variable shadowing issues in multiple functions in testpmd and removed unused variables.
  ↳ No PR: [e3ac7da](https://github.com/DPDK/dpdk/commit/e3ac7daed962aecbd5fe66de9c1be09f3c47dd2b)
- Fixed the variable shadowing problem in the graph application and renamed local connection variables to c.
  ↳ No PR: [7cf4b28](https://github.com/DPDK/dpdk/commit/7cf4b28a211dd832847130036cfc83a670990f9a)
- Fixed the parameter name conflict problem in the pdump application, changing the parameter name from optarg to arg.
  ↳ No PR: [da33fbc](https://github.com/DPDK/dpdk/commit/da33fbc6f344883b2970556ea34a256d410c92a3)
- Fixed the variable shadowing problem in test-compress-perf and changed the parameter names of the three functions from test_data to td.
  ↳ No PR: [793622c](https://github.com/DPDK/dpdk/commit/793622c6b68fa513ede82aecd293be0bf24ada27)
- Fixed the variable shadow problem in the encryption performance test and renamed the local variable iv_offset to iv_ofs.
  ↳ No PR: [ee12c9e](https://github.com/DPDK/dpdk/commit/ee12c9ee9c8bc96d97deb48d37f7f96fb233fa0b)
- Fixed variable shadowing problem in eventdev test, rename or remove related variables to support -Wshadow compilation option.
  ↳ No PR: [847548f](https://github.com/DPDK/dpdk/commit/847548f6d439bd281ce3d1c2c0ea8ad24630c52c)
- Remove unnecessary repeated definitions of variables in test-flow-perf.
  ↳ No PR: [a6cee45](https://github.com/DPDK/dpdk/commit/a6cee4542a369c1ecb96c683da86f09cc0f152dc)
- Fixed the error message about the port number limit in the ethtool example, and exchanged the printing order of the expected port number and the maximum port number.
  ↳ No PR: [a3df13c](https://github.com/DPDK/dpdk/commit/a3df13c880641c6eafade0f21580e35379a065e6)
- Optimize the NP online unloading process and move the soft resource release operation out of the online unloading function to avoid repeated releases.
  ↳ No PR: [962a591](https://github.com/DPDK/dpdk/commit/962a591468aa1424f21b4b27f3e901311d4e03fc)
- Add function name and line number information to interrupt unallocated error log.
  ↳ No PR: [c92dd4c](https://github.com/DPDK/dpdk/commit/c92dd4c7a14988cc7067d200a29d26e9c5e101de)
- Fixed compilation warnings in the cnxk driver caused by identical conditional branches, merged duplicate branches and corrected a loop condition.
  ↳ No PR: [bd2f563](https://github.com/DPDK/dpdk/commit/bd2f563dbd3516bd71d749011686ce097847ad1f)
- Change the queue comparison variable type in the i40e driver to unsigned to eliminate compilation warnings.
  ↳ No PR: [1e88e9f](https://github.com/DPDK/dpdk/commit/1e88e9fd790d601b7152c98f174b790087840ddb)
- Add socket path truncation check in virtual machine power management example.
  ↳ No PR: [90d45ee](https://github.com/DPDK/dpdk/commit/90d45ee6021a163955a73c510375e9a2f2d0b1f6)
- Fixed CodeQL warnings due to integer type width mismatch in ice driver, added explicit type conversions in multiple bitmap operations, ACL, DCB and scheduler functions.
  ↳ No PR: [29e53e3](https://github.com/DPDK/dpdk/commit/29e53e34ca2fbdf6f0df246582dda7aad40bb360)
- Fixed compilation warning of ipsec-secgw example under glibc 2.43, declare related pointer variable as const.
  ↳ No PR: [ce43790](https://github.com/DPDK/dpdk/commit/ce43790ffa2f215927e55b2bbe4c437559c9136c)
- Fixed compilation warnings caused by misuse of the comma operator in the idpf driver, replacing commas with semicolons.
  ↳ No PR: [b3b8301](https://github.com/DPDK/dpdk/commit/b3b8301dee7f1fd3e6bc8c2d79fd6f6cc04a7d58)
- Fixed the problem that temporary file names may be truncated during testing, and use unified functions to create temporary files instead.
  ↳ No PR: [3569561](https://github.com/DPDK/dpdk/commit/356956154480d2906f11ed959b3c62cc0c8649ad)
- Fixed the issue where mbuf segment number was not updated correctly in SGL test.
  ↳ No PR: [42be421](https://github.com/DPDK/dpdk/commit/42be4215de63144a80dce80fa5bc61843043abac)
- Fixed data length assignment error in RSA signature test.
  ↳ No PR: [318d45a](https://github.com/DPDK/dpdk/commit/318d45aeb52d041309db3f387bfde44e29da2e6f)
- Add debug log flag and improve error message output in EAL test cases.
  ↳ No PR: [2ce8fe8](https://github.com/DPDK/dpdk/commit/2ce8fe8fda0a344f8ef89adb5c92fa674f087494)
- Fixed the build problem of pcapng test on Windows and the problem of taking too long.
  ↳ No PR: [93efb28](https://github.com/DPDK/dpdk/commit/93efb28e67f8a39ddf171c43a9b2d079e1f8c30e), [5f384e0](https://github.com/DPDK/dpdk/commit/5f384e04d814917ce18646de7c4270e786a9f673)
- Dynamically scale the number of atomic test iterations and replace busy wait loops to reduce power consumption.
  ↳ No PR: [c9eb695](https://github.com/DPDK/dpdk/commit/c9eb695f162a0dce737337c500dd350012a44732)
- Fixed the device name overwriting problem in the dpaa2_sec encryption device driver, directly reusing the bus device name.
  ↳ No PR: [d229414](https://github.com/DPDK/dpdk/commit/d229414e99dc5bbd29240db86de563ffedd7c91b)
- Fixed compilation errors caused by uninitialized variables under the minsize build type.
  ↳ No PR: [0ab2c57](https://github.com/DPDK/dpdk/commit/0ab2c579ad5aa3501b49ceb4ebb1cc16625e3636), [0cc620f](https://github.com/DPDK/dpdk/commit/0cc620fbeff2889089f922c5218bc869600dfed2)
- Fix the error log of vlan_extend_set and vlan_tpid_set functions in testpmd, replace the static function name with dynamic __func__.
  ↳ No PR: [9323e3b](https://github.com/DPDK/dpdk/commit/9323e3b5d8ff7c0378676bdfb91af926fb0cec63)
- Fixed multiple resource leak issues in the mlx5 driver (meter job, stream pool, counter).
  ↳ No PR: [f5a92b7](https://github.com/DPDK/dpdk/commit/f5a92b70f545e830bf6baae9d15f88bb500481c4), [093b145](https://github.com/DPDK/dpdk/commit/093b145b3af3eb3f2b7a8392b7d720b24e119dd3), [7e14fd5](https://github.com/DPDK/dpdk/commit/7e14fd5b20006c51afe47c323cf8f29958121155)
- Fixed MAC address ownership tracking issue in mlx5 driver under Windows.
  ↳ No PR: [b93dbd8](https://github.com/DPDK/dpdk/commit/b93dbd8556600bf1ad921dc398575de9f0202339)
- Negotiate PTP capabilities with PF in advance when iavf driver is initialized to avoid incorrect activation.
  ↳ No PR: [d9cfba0](https://github.com/DPDK/dpdk/commit/d9cfba0abb5734a3aea524902dc406b6f1bef3be)
- Improved the check of Rx descriptor ring size in Intel network card driver, requiring the ring size to be greater than 2 times rx_free_thresh.
  ↳ No PR: [93de214](https://github.com/DPDK/dpdk/commit/93de214d5eb6e11dfef196d79873ad055fffc195)
- Fixed type conversion and bit order errors in UDC checksum calculation.
  ↳ No PR: [c92eb50](https://github.com/DPDK/dpdk/commit/c92eb504081aa06c16983e0d0935bcadd1f113ca)
- Fixed rte_bpf_dump support and printing issues for conditional jumps, call instructions, store/load instruction mode checks, atomic instructions and non-zero variants of unused fields.
  ↳ No PR: [c22ce68](https://github.com/DPDK/dpdk/commit/c22ce687a1556dc1a8cbbf1ef28e6c41b61425db)
- Fixed array out-of-bounds warning caused by using rte_memcpy in the FIPS verification example, use standard memcpy instead.
  ↳ No PR: [dac0edb](https://github.com/DPDK/dpdk/commit/dac0edb433859c026b35615495b48dc6d394b7b8)
- Added null pointer checking for IAVF and ICE driven RAW stream entries to avoid null pointer dereferences.
  ↳ No PR: [f1425be](https://github.com/DPDK/dpdk/commit/f1425bea1b21dfb74ffcdf6ed01e9e11d96d22bd)
- Fix mmap error check in VDUSE IOTLB miss handler, replace NULL check with MAP_FAILED check.
  ↳ No PR: [970e569](https://github.com/DPDK/dpdk/commit/970e569b85a499f5bf72192c8e4d51451acc4727)
- Fix invalid memory access issue caused by not checking that the root node is empty when submitting a new Tx scheduler hierarchy.
  ↳ No PR: [17f994b](https://github.com/DPDK/dpdk/commit/17f994ba82dd8031958729ea1be4e6b641baa7e9)
- Fixed the priority mode printing error when Tx scheduling tree dump in ice driver.
  ↳ No PR: [e648984](https://github.com/DPDK/dpdk/commit/e648984c2811203697492d0af4d9904f4e574166)
- Fixed variable shadowing warning caused by repeated declaration of variable i in mrvl_rx_pkt_burst function.
  ↳ No PR: [fc97ac5](https://github.com/DPDK/dpdk/commit/fc97ac545fcb5983dd9f6b5c9cc4a957968e8c8f)
- Add PCIe BAR channel check and return dedicated error code when DTB times out.
  ↳ No PR: [c76668b](https://github.com/DPDK/dpdk/commit/c76668b42b3bf421e829709886d956a1209730ef)
- Check the return value of ioctl call and log error in case of failure.
  ↳ No PR: [2e1c778](https://github.com/DPDK/dpdk/commit/2e1c77833358db589fb014328ee0c5db1ae6c1ed)
- Fixed the issue of using variable-length arrays for interrupt configuration in the CNXK driver, using predefined constants instead to avoid LTO compilation warnings.
  ↳ No PR: [1fb9f4a](https://github.com/DPDK/dpdk/commit/1fb9f4ab14b34fe6b1613c1b37f84602654b77ce)
- Removed useless AVX512 Tx setting functions and their calls, fixed Coverity defects.
  ↳ No PR: [b7d3525](https://github.com/DPDK/dpdk/commit/b7d3525e610da890a8d12f095e824104c49c49ea)
- Change the local configuration structure assignment to a designated initializer in the get_eth_conf function to ensure zero initialization.
  ↳ No PR: [5a93623](https://github.com/DPDK/dpdk/commit/5a9362386ef80d36c9972ba1717c4a82c9ea2cc6)
- Explicitly pass the ol_flags parameter of the Tx context-related function in the iavf driver to avoid repeated reading of mbuf.
  ↳ No PR: [086a7a9](https://github.com/DPDK/dpdk/commit/086a7a9a7200c97dd3709172230286ed32c5dfc6)
- Fix race condition in statistics display in l2fwd-jobstats example.
  ↳ No PR: [169180b](https://github.com/DPDK/dpdk/commit/169180b961239c09087543330945a5aa8850ae57)
- Fixed an issue where firmware error logs were not recorded when modifying SQ and RQ.
  ↳ No PR: [1855b0c](https://github.com/DPDK/dpdk/commit/1855b0c11b27797431b1602156b8896341874bfd)

### Refactoring optimization
- Change timestamp calculation to Unix epoch-based nanosecond values to ensure monotonically increasing values.
  ↳ No PR: [cf98635](https://github.com/DPDK/dpdk/commit/cf9863555e2ea06daa892fb611801ff78ad68826)
- Updated the inline RQ mask configuration to adapt to mbox changes, and added support for the default RQ first skip byte configuration.
  ↳ No PR: [3cb2961](https://github.com/DPDK/dpdk/commit/3cb2961acaa9ed13de76159aaf8ac375957d866b)
- Explicitly mark ARM opcode constants as type uint32.
  ↳ No PR: [256dae5](https://github.com/DPDK/dpdk/commit/256dae55be967dee16cbeb94b99e46ccafc083ae)
- Removed the Tx queue used descriptor count and related fields that are no longer used in the Intel network card driver.
  ↳ No PR: [2f987ed](https://github.com/DPDK/dpdk/commit/2f987edd2b81ab6602e94f27f79a3dc1ba9cd1c6)
- Removed unused code left by the pipeline mode in the iavf driver.
  ↳ No PR: [28bef18](https://github.com/DPDK/dpdk/commit/28bef1868a7f036077cabc039f89f1fba2fe5249)
- Change the link status update of the ice driver to be obtained through adminq messages to simplify interrupt processing.
  ↳ No PR: [e01265e](https://github.com/DPDK/dpdk/commit/e01265e4a9bf259e5ec26010a38d66eec0415559)
- Removed unused Tx doorbelling intrinsic function in mlx5 driver.
  ↳ No PR: [55b022e](https://github.com/DPDK/dpdk/commit/55b022e849d388d65882d29b40d11fe50760e17d)
- Replaced hardcoded delays in dpaa2 driver link down functions with unified check interval macros.
  ↳ No PR: [f47d08c](https://github.com/DPDK/dpdk/commit/f47d08c06378c42cde80ab16078239fcaf4495a7)
- Remove the SSE vector data path of i40e, iavf and ice network card drivers, and use AVX2 or scalar fallback path uniformly.
  ↳ No PR: [8a1ac55](https://github.com/DPDK/dpdk/commit/8a1ac556c16ffde1ccbb72877b2ae108058987bf), [3382757](https://github.com/DPDK/dpdk/commit/338275758d65a485584b04c1913af0a1ad1806cb), [d23d825](https://github.com/DPDK/dpdk/commit/d23d82594ddc9fe1b0fc82bd84ed5f171a527435)
- Add unified prefixes to global variables and functions of virtio network PMD to avoid link conflicts.
  ↳ No PR: [7d3b2a9](https://github.com/DPDK/dpdk/commit/7d3b2a980fa5b544c69a7d84dfc6515eaceef03d)
- Remove variable length arrays in AES-XBC code, use fixed size arrays instead and add assertions.
  ↳ No PR: [3d31eb1](https://github.com/DPDK/dpdk/commit/3d31eb18f05c83d3023d79445b95352e5f23a86a)
- Reconstruct the context descriptor processing logic of ice, i40e and idpf drivers, unify it into a single function and optimize the sending path.
  ↳ No PR: [2021af6](https://github.com/DPDK/dpdk/commit/2021af6981b2e9b05ac8406381aebdf3c2939d04), [44d99d4](https://github.com/DPDK/dpdk/commit/44d99d409880f0cca78de87c1df6ed12ec4b4b7c), [025b898](https://github.com/DPDK/dpdk/commit/025b898d1add89488b5d213ec5de7d97da20243e)
- The ixgbe driver instead uses a separate array to track transmit descriptor completion status to match the universal scalar Tx code.
  ↳ No PR: [2826cf9](https://github.com/DPDK/dpdk/commit/2826cf91f6980a06f71006f3945c3c88ecd449a0)
- Removed redundant code that manually sets the callback function to NULL when the device is released in multiple network drivers.
  ↳ No PR: [a8f0927](https://github.com/DPDK/dpdk/commit/a8f0927f2e7f2fb0981367fbe971cdd6a1a743ff)
- Remove the MAC type checking macro in the ixgbe driver and use explicit conditional judgment instead.
  ↳ No PR: [5b0f8d6](https://github.com/DPDK/dpdk/commit/5b0f8d60f79432f27f6fe3d29ce280420eabc868)
- Separate the security filter and ntuple filter in the ixgbe driver and analyze them independently.
  ↳ No PR: [2ad7ff7](https://github.com/DPDK/dpdk/commit/2ad7ff7d960e72b5728c8ef0952ffb110cb7239e)
- Eliminate the global variable dependency of the rte_flow verification and creation process in the i40e driver and introduce the context structure.
  ↳ No PR: [de229bd](https://github.com/DPDK/dpdk/commit/de229bd5bc5c5e13f74ebdd9f38cf95e92d4dc09)
- Changed the i40e driver's default RSS key to a global constant to facilitate maintenance and reuse.
  ↳ No PR: [52fbae1](https://github.com/DPDK/dpdk/commit/52fbae1fbe35c9e6d49ae712de25ea1f0767522b)
- Remove the global variables parsed by i40e driver flow mode and use dynamic memory allocation instead.
  ↳ No PR: [aaf9a5f](https://github.com/DPDK/dpdk/commit/aaf9a5f5b818eb19185f4138885a79f78bd71627)
- Unify the assignment timing of the link auto-negotiation flag in em, igb and igc drivers so that it is always set according to the configuration.
  ↳ No PR: [dc7bfca](https://github.com/DPDK/dpdk/commit/dc7bfca7510543a0d5b63a71615796a4e7c5871a)
- Removed unused olx parameter in mlx5 driver Tx release routine, and simplified multi-packet buffer release check.
  ↳ No PR: [5dcd88e](https://github.com/DPDK/dpdk/commit/5dcd88e3df252e2e160bca0cb01e71096ffb6fd6)
- Optimize the Intel network card driver scalar Tx path: introduce the write_txd function to allow the compiler to merge storage operations, introduce a smaller sw_ring_vec structure and rename the vector_tx flag.
  ↳ No PR: [5339b41](https://github.com/DPDK/dpdk/commit/5339b41e9b545495eb88c42ced7f7540b9e94c57), [e8cccb4](https://github.com/DPDK/dpdk/commit/e8cccb42a99710c074c5944a12fc75d6f1d42f17)

### Test related
- Remove the deprecated coremask option from testing and use -l to specify the core list instead.
  ↳ No PR: [0961073](https://github.com/DPDK/dpdk/commit/0961073c656d85ed455e9531595c93ee5c4d9b19)
- Adjust the waiting delay and number of timers for the secondary process timer test to avoid timeouts in the CI environment.
  ↳ No PR: [fdce001](https://github.com/DPDK/dpdk/commit/fdce001f3f2e0947ed274d011541ea665633ffbc), [36535b6](https://github.com/DPDK/dpdk/commit/36535b6e98f99e6a7ce7e16d86573a0ecaed7e1a)
- In the power capability test, when the subsystem cannot be initialized, the test is skipped instead of failing directly.
  ↳ No PR: [dc8d455](https://github.com/DPDK/dpdk/commit/dc8d45587b723fe73196ede81948928d7c710a50)
- Register eventdev, cryptodev and ethdev test cases that require device presence as driver tests.
  ↳ No PR: [e2b6719](https://github.com/DPDK/dpdk/commit/e2b671954578cf43233e2651ebba108c3283edd6)
- Moved red_autotest test cases to the new attic test suite.
  ↳ No PR: [636b165](https://github.com/DPDK/dpdk/commit/636b16520de5c12c22ae2171c764877969373bf6)
- Refactor PMD-specific asymmetric test suites into a generic test suite based on capability checks.
  ↳ No PR: [064ef1b](https://github.com/DPDK/dpdk/commit/064ef1b098d1827d62a053d5424db9a1b10b5029)
- Add line numbers and additional log output to the EAL file prefix unit test to facilitate debugging.
  ↳ No PR: [9ffb046](https://github.com/DPDK/dpdk/commit/9ffb046b58c4a900be3375859a1a4f6349b1c1f0), [491d298](https://github.com/DPDK/dpdk/commit/491d2986bf79d958bd0914645ffc2d803868832c)
- Improve BPF testing, add NULL PMD dependency check, fix error handling and payload size.
  ↳ No PR: [167275b](https://github.com/DPDK/dpdk/commit/167275b6e89673a07ae4158996f7c4f19316bf98), [4e10db0](https://github.com/DPDK/dpdk/commit/4e10db0bcb4e1c2aa9d4f4264cc7fa0c3b6749bd), [e8f7ffd](https://github.com/DPDK/dpdk/commit/e8f7ffd2cc10da83ffa456da9f63da19c1137893)
- Disable PCI probing in EAL flag tests and vdev tests to avoid false positive CI failures.
  ↳ No PR: [f67f76e](https://github.com/DPDK/dpdk/commit/f67f76e6bbfd122270e8ac1aa384fefa9782e779), [af06ac4](https://github.com/DPDK/dpdk/commit/af06ac4c9ad74517f9f3ebf45d3e957845337ea3)
- Optimize memcpy test, reduce the number of aligned offset pairs, and avoid timeout in slow simulation environment.
  ↳ No PR: [bc15681](https://github.com/DPDK/dpdk/commit/bc15681021d5588072f0635ccb9937d127c64b3d)
- Change the output of pcapng function test to stdout, change the timestamp to UTC format, and optimize error handling.
  ↳ No PR: [0f49bc4](https://github.com/DPDK/dpdk/commit/0f49bc4923a569edaa3fbf0d6c0a3f93a8262aba)
- Change the number of cycles of the MCS lock test to dynamic scaling based on the number of cores.
  ↳ No PR: [f0437ad](https://github.com/DPDK/dpdk/commit/f0437ade1595c54ed5d4bfa52a1a89a490170d99)
- Dynamically adjust the number of test iterations based on the number of cores to fix synchronization issues on multi-core systems.
  ↳ No PR: [837afbf](https://github.com/DPDK/dpdk/commit/837afbfc49c08620b9be08d7cedbada5da14027d)
- Replaced volatile variables with C11 atomic operations in the test timer shared memory structure.
  ↳ No PR: [5e52e43](https://github.com/DPDK/dpdk/commit/5e52e43cdf823a9c59199eed40413e2bd5e9c09a)
- When the TAP virtual device cannot be created, mark the test result as skipped instead of failed.
  ↳ No PR: [567ec7e](https://github.com/DPDK/dpdk/commit/567ec7e6e80f28b1b60e1b9d57148e1d0a64e092)
- Fixed an issue where the timer test hangs when the auxiliary process fails to run.
  ↳ No PR: [5f6945b](https://github.com/DPDK/dpdk/commit/5f6945bcfb0de8292da9dd8cd56556e2306d02cb)
- Fixed the issue where the source and destination buffer pointers were incorrectly reversed in the do_cpu_mem_copy function.
  ↳ No PR: [e76312d](https://github.com/DPDK/dpdk/commit/e76312d0792e3bb8958cd4c16ed014d2890ae55d)
- Replaced quick test boolean parameters with clearer enumeration values, added parameter validation.
  ↳ No PR: [f092084](https://github.com/DPDK/dpdk/commit/f09208479261af910c2d321bd684309099e499b3)
- Fixed the variable shadowing problem and renamed related variables to avoid naming conflicts.
  ↳ No PR: [b18e337](https://github.com/DPDK/dpdk/commit/b18e337f22eb989d377a6264dadb434714efc883)
- Fixed the variable shadowing problem in the main function and deleted redundant ret variable definitions.
  ↳ No PR: [b7358fc](https://github.com/DPDK/dpdk/commit/b7358fc35348420542e521153101974fd9fbca6f)
- Simplify the implementation of getting the current file prefix, use rte_eal_get_runtime_dir() instead of reading the /proc directory.
  ↳ No PR: [8dc80af](https://github.com/DPDK/dpdk/commit/8dc80afda7a52a1bd28088fe34102e7c1ba17282)

### Performance optimization
- Divide HWS schema template creation into internal and external templates, internal templates skip validation to speed up PMD initialization.
  ↳ No PR: [2269696](https://github.com/DPDK/dpdk/commit/2269696b023254d3d4c99e3d5d03466a8f47cce3)
- Lock operations are merged during the queue allocation process, reducing hardware lock overhead and improving queue setting performance.
  ↳ No PR: [319bab4](https://github.com/DPDK/dpdk/commit/319bab49327b9c547b49730798cc4432977f6191)
- Added GENEVE tunnel TSO and receiver outer UDP checksum offload support to the zxdh network card driver, improving the performance of tunnel encapsulated traffic.
  ↳ No PR: [af40a93](https://github.com/DPDK/dpdk/commit/af40a93fa21f94a3a41b9953918a0937ad7e4599), [2aa7e28](https://github.com/DPDK/dpdk/commit/2aa7e28b41bd7bf18a62a81a31c41ffdfe8a30bb)
- Added a shortcut processing path for packets that do not use TSO and have only one data descriptor, improving performance.
  ↳ No PR: [2d17ea2](https://github.com/DPDK/dpdk/commit/2d17ea27de46d56edbbc7d47abc024f85d99853c)
- Optimized Rx performance for RTL8127, adjusted the number of Rx descriptor batch acquisitions to 12.
  ↳ No PR: [8865f1f](https://github.com/DPDK/dpdk/commit/8865f1f4c390dcbcb9c164ce2f986b93ce563873)
- Optimized pcapng timestamp conversion performance, using precomputed TSC frequency reciprocal instead of division operation.
  ↳ No PR: [4fc6561](https://github.com/DPDK/dpdk/commit/4fc65615b274701070c67f8c424d93aef8bf7483)
- Replace unnecessary huge page memory allocations with ordinary heap or stack allocations in the ice driver, reducing memory overhead.
  ↳ No PR: [5419cfa](https://github.com/DPDK/dpdk/commit/5419cfa9d9f66aea3813cb51e3f2f4b6f48b1bcd)
- Delayed allocation of HWS tag action in the mlx5 driver, and creation by domain only when the FLAG/MARK action is used for the first time, reducing firmware resource usage.
  ↳ No PR: [c51430d](https://github.com/DPDK/dpdk/commit/c51430d840252aea1e9c9315fe1d70f0635bb800)
- Implemented delayed allocation of HWS push_vlan action in the mlx5 driver, which is only created by domain when used for the first time, reducing firmware resource usage.
  ↳ No PR: [7e1ef27](https://github.com/DPDK/dpdk/commit/7e1ef27a8a44ef2c6fd95e08125463306bc0ec6f)
- For the CN20k platform, reduce the AES_GCM encrypted SA context push size to 128 bytes, improving CPT performance.
  ↳ No PR: [a3440b7](https://github.com/DPDK/dpdk/commit/a3440b790bc3abe886c6db1c014c3c21b0f8d222)
- Added multi-doorbell support to the bnxt driver, which improves P5/P7 chip performance by detecting hardware capabilities and assigning different doorbell page indexes to disperse doorbell access.
  ↳ No PR: [7a1f9c7](https://github.com/DPDK/dpdk/commit/7a1f9c782b50a1045a560782717fab20bc370877)
- Changed the memory allocation of temporary variables in the iavf driver from huge pages to normal dynamic or stack allocation.
  ↳ No PR: [292d3b7](https://github.com/DPDK/dpdk/commit/292d3b781ac4224abe770b6ae2bb4c16cb5c5907)
- Replace dynamic memory allocation in ice driver managed queue message handling with on-stack buffers.
  ↳ No PR: [ae059c6](https://github.com/DPDK/dpdk/commit/ae059c611e92e9b2c54364050c561cceb3e9bd05)
- Relaxed the check for zero latency in latency testing to be compatible with simulated hardware environments.
  ↳ No PR: [05d74da](https://github.com/DPDK/dpdk/commit/05d74daef2d301660c7ba545de45147973c88d79)
- Added rte_pause() in synchronized spin loops for atomic operations and thread tests, improving CPU resource sharing.
  ↳ No PR: [0df23c6](https://github.com/DPDK/dpdk/commit/0df23c6d0714d5aa676c06b8c6037a0810222607)
- Optimized the sending processing of the Intel network card driver scalar data path, including adjusting the end packet flag setting and removing unnecessary completion flag clearing.
  ↳ No PR: [faf8d5c](https://github.com/DPDK/dpdk/commit/faf8d5c90679027e43200f15188456f4029740c9), [b0086ad](https://github.com/DPDK/dpdk/commit/b0086ade30be7a9f4b7ef8c595d2f5b76bc8b70f), [c42fe8a](https://github.com/DPDK/dpdk/commit/c42fe8af73fed0780f9ea33be7e121532282ee08), [9bacf6a](https://github.com/DPDK/dpdk/commit/9bacf6a81b9287ff9cbc9b3d0645a76afff5cc3e)
- Changed the TAP/TUN virtual device's link speed capability from runtime dynamic calculation to compile-time constant.
  ↳ No PR: [52ceffe](https://github.com/DPDK/dpdk/commit/52ceffe214bbdde3312d53a90fb585bd05a98a5f)

### Security related
- Fixed the array out-of-bounds access problem caused by improper declaration of temporary variables in the inl_outb_soft_exp_poll function in the cnxk driver.
  ↳ No PR: [4a6154a](https://github.com/DPDK/dpdk/commit/4a6154a7bd275f2cbe9a3aee272b393fd00aeaed)
- Fixed the sign bit overflow problem caused by the left shift operation in ARM JIT, and used safe macros to avoid undefined behavior.
  ↳ No PR: [8203cb4](https://github.com/DPDK/dpdk/commit/8203cb408d51a49828d9870a96557c245825d49a)
- Fixed signed integer overflow issue in addition and subtraction operations in BPF validator.
  ↳ No PR: [8239b20](https://github.com/DPDK/dpdk/commit/8239b206da5c428b00ed7d5e22ad6284eff1c546)
- Fixed integer overflow caused by u16 type multiplication in net/nbl driver, which has been explicitly converted to 64-bit type when calculating buffer size.
  ↳ No PR: [9559873](https://github.com/DPDK/dpdk/commit/9559873f4a74be5ad840a4210436c0b7fdad9aed)
- Fixed buffer overflow in SA table settings to prevent heap corruption by correcting SA size initialization value.
  ↳ No PR: [99a23d7](https://github.com/DPDK/dpdk/commit/99a23d765ec43389267c9c1958e60bd41f54585b)
- Fix potential buffer overflow in hugepage path construction, use dynamic allocation of path strings instead and add error handling.
  ↳ No PR: [46e7703](https://github.com/DPDK/dpdk/commit/46e7703d10b58bdaf9560c3231edac8431bf35de)
- Fix out-of-bounds read caused by L4 header truncation in tap driver, add bounds check to skip checksum verification.
  ↳ No PR: [c91c4e1](https://github.com/DPDK/dpdk/commit/c91c4e15392de76fe1383caea457425474d5e956)
- Replaced variable-length arrays in flow item validation functions with fixed-size buffers in the tap driver, and added a check for upper size limits.
  ↳ No PR: [d915804](https://github.com/DPDK/dpdk/commit/d91580464394d8474181ac83079ec28b64cc19da)
- Add null pointer and length matching verification for RAW stream items in i40e driver to prevent segmentation faults and out-of-bounds access.
  ↳ No PR: [c138a6c](https://github.com/DPDK/dpdk/commit/c138a6c3bd0aa369305fe6cf46ef376e4af69f54)
- Fix mbuf buffer overflow caused by unchecked packet size in AF_PACKET receive path, add boundary check and discard overlong packets.
  ↳ No PR: [3ed9a05](https://github.com/DPDK/dpdk/commit/3ed9a05bff5d0e06efb0bd5617a398337fe5eac7)
- Fixed a heap buffer overflow in the sample group match in the net/mlx5 driver, and added a size check before comparing cache actions to avoid out-of-bounds reads.
  ↳ No PR: [bc2738c](https://github.com/DPDK/dpdk/commit/bc2738c4fe2d9d96b0a6700dc7ce7da6ef4f8e85)
- Fixed the SM2 public key buffer overflow vulnerability and added verification of the public key coordinate length when setting session parameters to prevent stack buffer overflow caused by overly long coordinates.
  ↳ No PR: [becf14f](https://github.com/DPDK/dpdk/commit/becf14f6f6d4d1ae834b797a0f9f83e0bea605c3)
- Add buffer overflow check in vhost, log warning when name is truncated.
  ↳ No PR: [18efd5b](https://github.com/DPDK/dpdk/commit/18efd5b2a2155a328c34e9ad642e857bae0d6da2)
- Fixed buffer overflow issues in multiple tests, including memory area names, file prefixes, directory paths, input lines and vdev parameters.
  ↳ No PR: [d22ed11](https://github.com/DPDK/dpdk/commit/d22ed116b0193bd71285ab93d014f549b3c87265), [f17b6ea](https://github.com/DPDK/dpdk/commit/f17b6eacf00ae8e61ce5cac7c8409372888c68f6), [5c82610](https://github.com/DPDK/dpdk/commit/5c82610e24275a9b546ec712a76698537224e9e8), [3a73391](https://github.com/DPDK/dpdk/commit/3a73391f2b5327ff7131f9c3198a4574cd7e3de4), [35cd4ce](https://github.com/DPDK/dpdk/commit/35cd4ce4bdca34b66d06ac23e88b589ea0b390b9)
- Added ESP-specific flow rule support for out-of-place inline inbound scenarios for IPsec security testing, falling back to default rules when hardware does not support it.
  ↳ No PR: [b48b18e](https://github.com/DPDK/dpdk/commit/b48b18e9a289421614ff8e786833af810ad795d6)
- Skip inline protocol testing to avoid subsequent failures when the underlying hardware does not support safe offloading.
  ↳ No PR: [a4911f7](https://github.com/DPDK/dpdk/commit/a4911f7b1085c033cb2f063908fec70e0dd91efb)
- Added support for SM4-CBC and SM3-HMAC national encryption algorithms in the IPsec security gateway example.
  ↳ No PR: [9631ec0](https://github.com/DPDK/dpdk/commit/9631ec0f922d376b181bd5aa7d9efe941ad00147)

### Documentation
- The ixgbe network card driver document adds support information for Intel Ethernet Controller E610 and adapters based on this controller.
  ↳ No PR: [2fd49e7](https://github.com/DPDK/dpdk/commit/2fd49e727e57400d9ac7b3b2b24d2840af329611)
- Added documentation for device parameters (devargs) and device hot-plug functionality in the Programmer's Guide.
  ↳ No PR: [610d3bb](https://github.com/DPDK/dpdk/commit/610d3bb95ce7a2599467e545ccf123c49f69a869), [d8e8d0c](https://github.com/DPDK/dpdk/commit/d8e8d0c9a8dead6495808007e48f023a02d3b79a)
- Added documentation for QinQ and encryption device throughput to DTS test suite.
  ↳ No PR: [018fe03](https://github.com/DPDK/dpdk/commit/018fe03128e0dccf8466c5c8384ab1f5823a1d34), [a830091](https://github.com/DPDK/dpdk/commit/a8300915fb48e73657df9bc829244f264fd03bc0)
- Updated i40e network card documentation, added QinQ strip chapter and added VLAN filter command instructions.
  ↳ No PR: [d52c6b4](https://github.com/DPDK/dpdk/commit/d52c6b4857101015b258c35426f4d8814e3f9af2)
- Added driver information and device configuration instructions to the QAT guide.
  ↳ No PR: [4b08542](https://github.com/DPDK/dpdk/commit/4b08542a67be859f9554204decf4d0f63eb4c846)
- Removed support for out-of-maintenance AMD Solarflare SFN7xxx series network cards from documentation.
  ↳ No PR: [a2d1148](https://github.com/DPDK/dpdk/commit/a2d1148dcf0339034c4a0fe317ed1a7519117bb8)
- Split pcap and ring driver documentation into two separate files, and updated the index.
  ↳ No PR: [4fd8a79](https://github.com/DPDK/dpdk/commit/4fd8a79bdad493991bf9ef3b95028d87bee58716)
- Added description of --query-rate option in flow-perf usage guide.
  ↳ No PR: [17a6a71](https://github.com/DPDK/dpdk/commit/17a6a71aa8864a7602acb69d64893363f6da30f8)
- Fixed syntax and terminology in Universal Streams API documentation.
  ↳ No PR: [c736147](https://github.com/DPDK/dpdk/commit/c736147d9ad61ad24294d332d5eafefebe94d705)
- The mlx5 driver documentation states that PMD will close duplicate cmd_fd when the device is shut down.
  ↳ No PR: [b302b35](https://github.com/DPDK/dpdk/commit/b302b35ad71707b0d0d9a9386c8aa3a798606159)
- Cleaned and updated the NFB network card driver documentation, and added the supported network card list and firmware download link.
  ↳ No PR: [08ec57a](https://github.com/DPDK/dpdk/commit/08ec57afe8eae5902d5146eed166124a23d985f7)
- The IDPF driver documentation states that multiple send queues sharing completion queues are not supported in split queue mode.
  ↳ No PR: [5c21fb5](https://github.com/DPDK/dpdk/commit/5c21fb5057ea6f0f7b3eca5bda75ccbb88726d2e)
- Updated AMD EPYC Tuning Guide, updated URL and added instructions for disabling ASPM in low-latency mode (pcie_aspm=off).
  ↳ No PR: [bc15a33](https://github.com/DPDK/dpdk/commit/bc15a33eeebcaa339f797966f478ad4d27169c80)
- Revised NBL network card driver guide, corrected document format and added vfio-pci driver setup instructions.
  ↳ No PR: [26bef5e](https://github.com/DPDK/dpdk/commit/26bef5ec49f04da43195e75bc9f9a46eae77a40e)
- Update the version support range of Intel Multi-buffer library in the cryptodev guide, DPDK 24.11+ version is adjusted from 1.4-1.5 to 1.4+.
  ↳ No PR: [15f1c9e](https://github.com/DPDK/dpdk/commit/15f1c9ea83c22d0445b7ade46acdf9b9e7b17cff)
- Added IBM Power 10 test platform information to the 25.11 release notes.
  ↳ No PR: [148137b](https://github.com/DPDK/dpdk/commit/148137b801d7233340e23317f2f802d16763d7f7)
- Merge the version tables of E810 and E830, rename the firmware column to E810 FW and add the E830 FW column.
  ↳ No PR: [1c6cf12](https://github.com/DPDK/dpdk/commit/1c6cf125be309a5c518595c72f781a6f089dbeb1)
- Remove non-LTS versions that have expired support from the ice driver document version compatibility table, and prioritize them by the latest version.
  ↳ No PR: [ee4eae6](https://github.com/DPDK/dpdk/commit/ee4eae6f26086fbdeb851da5506344d845039917)
- Removed 21.11 and all non-LTS versions from the version table for X710 and X722 network cards.
  ↳ No PR: [9a24cad](https://github.com/DPDK/dpdk/commit/9a24cad46edc2f06b0dbac566941c418ae5439fc)
- Merge the version table in the i40e driver document, retaining one column of firmware version information for X710 and X722 respectively.
  ↳ No PR: [47bc1f5](https://github.com/DPDK/dpdk/commit/47bc1f5a60849f59b7a38d9e79c94667c8f7d765)
- A verified kernel driver and firmware version matching table has been added to the ixgbe driver documentation.
  ↳ No PR: [a1ae16b](https://github.com/DPDK/dpdk/commit/a1ae16b4f8d00047e805c17b3742ff2dea94da74)
- Updated the version matching table in the ice network card document, adding version 26.03 verified driver, firmware and DDP package version information.
  ↳ No PR: [acdd48f](https://github.com/DPDK/dpdk/commit/acdd48f6e6e3b5fc14a0038ef4cc735f76884628)
- Update the version matching table in the i40e network card document to add the verified driver and firmware version information of version 26.03.
  ↳ No PR: [43f8f14](https://github.com/DPDK/dpdk/commit/43f8f1472815fadee390ac9f785713a550159261)

### Build/CI
- Enable variable shadow warning (-Wshadow) in global builds.
  ↳ No PR: [6073bd9](https://github.com/DPDK/dpdk/commit/6073bd97b417cb00307bbe7fa404bebfbdbe6491)
- Enable compiler checking for format overflows.
  ↳ No PR: [de2604d](https://github.com/DPDK/dpdk/commit/de2604d55cb7098a941db696248c4d4d00abff43)
- Removed compile flag to suppress VLA warnings in common/cnxk build configuration, using VLA now triggers warnings.
  ↳ No PR: [5bde94b](https://github.com/DPDK/dpdk/commit/5bde94b2e31b5c7ef5f6a81d616a48a5b39c2d2e)
- Add the --file-prefix parameter to all fast-tests on Linux, using the test name as the unique prefix to avoid EAL initialization failures due to file prefix conflicts when running in parallel.
  ↳ No PR: [5ef1668](https://github.com/DPDK/dpdk/commit/5ef1668383942b1c472a514404d95250baba24af)
- Disabled variable shadow warnings for driver, application and sample builds.
  ↳ No PR: [dcd5b77](https://github.com/DPDK/dpdk/commit/dcd5b773e82e5d5fe78b3b5047fce15370fa84b6), [33fe21a](https://github.com/DPDK/dpdk/commit/33fe21a8afeac76e61297afe3eadb8740061c46f), [d819dec](https://github.com/DPDK/dpdk/commit/d819decd1a34bec39db100678d5e53b11a53f220)
- Added build dependencies and warnings for tests that rely on the net_null driver.
  ↳ No PR: [86641ef](https://github.com/DPDK/dpdk/commit/86641ef2845b59a0ecd8cf367ee326f76e74fddc), [7b0bbf9](https://github.com/DPDK/dpdk/commit/7b0bbf92c8c94cdd1c8604a242af5455293ab923), [98a3c0d](https://github.com/DPDK/dpdk/commit/98a3c0d18aa9b3b63f9e8a81d00808e80af2ee16)
- Adjusted the test build script to specify different build modes for different build types.
  ↳ No PR: [177acaf](https://github.com/DPDK/dpdk/commit/177acaf5cf75c4b0bacf66f655a636d0fbc88f2a)
- Enable format overflow warnings when testing builds.
  ↳ No PR: [85c1122](https://github.com/DPDK/dpdk/commit/85c11223d12caf8ceda8ed5ab4a48dc14ce4652c)
- Added minsize build type checking in Fedora GCC builds in GitHub Actions.
  ↳ No PR: [ed9c14b](https://github.com/DPDK/dpdk/commit/ed9c14b4548ec1b153f1ae6c099be6795f6e7b07)
- Added disabling detection of the perror function in the patch check script.
  ↳ No PR: [307d8e4](https://github.com/DPDK/dpdk/commit/307d8e49e621ee037e5c0547c53033fc4271b94a)
- Added DTS test case document string checking script and integrated it into the format checking process.
  ↳ No PR: [edc493e](https://github.com/DPDK/dpdk/commit/edc493e4f24ef477502b8d293f36ea070df31508)
- Fixed a crash in the symbol change checking script when processing documentation-only patches.
  ↳ No PR: [7f75813](https://github.com/DPDK/dpdk/commit/7f75813e3c24a4e707b5a25bf977baa5f7af55e3)
- Fixed spurious -Wstringop-overflow warning due to inlining when compiling with LTO.
  ↳ No PR: [66c348c](https://github.com/DPDK/dpdk/commit/66c348c208b79a87c32a7e744159076c8d0b67f0), [00d4138](https://github.com/DPDK/dpdk/commit/00d41387a5863affd3a018ddb784f3b2195d7fa1)
- In DTS document builds, treat Sphinx warnings as errors when the werror option is enabled.
  ↳ No PR: [68fdc7c](https://github.com/DPDK/dpdk/commit/68fdc7c84912bc8981b907a757582a2352b6cae2)
- Fixed file prefix conflict when trace tests are executed in parallel.
  ↳ No PR: [07b697b](https://github.com/DPDK/dpdk/commit/07b697b29741c080a6f125a96a5ef5f68249a34d)
- Fixed BPF ELF load test to limit BPF target CPU version to v2.
  ↳ No PR: [78a657c](https://github.com/DPDK/dpdk/commit/78a657c0a5d4fea6196dd0040e1b9e545bcb769a)
- Register four test cases: external_mem, ipsec_sad, power_caps and timer_secondary as quick tests.
  ↳ No PR: [d32cdaa](https://github.com/DPDK/dpdk/commit/d32cdaacbbb6bacabfa2703c0f2c6fff3b567289)

### Maintenance
- Standardize SPDX license tag format in all source files, remove extra brackets and spaces, unify comment style, and update check scripts.
  ↳ No PR: [b99a3b8](https://github.com/DPDK/dpdk/commit/b99a3b8aa9895047754b3f924af1096628d2186e)
- Clean up extra blank lines and extra asterisks at the end of comment blocks in multiple library header files.
  ↳ No PR: [b11692d](https://github.com/DPDK/dpdk/commit/b11692dbeecd48a58f83c2e68c1c5c626288fe40)
- Added parentheses to ternary expressions assigned to TUN/TAP flags to clarify operator precedence, no functional changes.
  ↳ No PR: [3769fda](https://github.com/DPDK/dpdk/commit/3769fda557ef5d0c1bbfde20a65686aa101a1bb0)
- Fixed variable shadowing issues in multiple libraries and drivers, eliminating compilation warnings by renaming variables or removing duplicate declarations.
  ↳ No PR: [68c2dde](https://github.com/DPDK/dpdk/commit/68c2dde1d441cda8e5656e46b018f7a39e47a669), [a92bd5b](https://github.com/DPDK/dpdk/commit/a92bd5bf2a53c3bf0945be693fb6d80a7863f9a6), [c45fb0f](https://github.com/DPDK/dpdk/commit/c45fb0fb48edb3eb88702c7aa00019d0756e7d52), [a2472f3](https://github.com/DPDK/dpdk/commit/a2472f3a81d04c1cd5e08a0eb5dff87fba736935), [5b83f52](https://github.com/DPDK/dpdk/commit/5b83f52407d681f176262b5db9f3ca09226d2a37), [99c3958](https://github.com/DPDK/dpdk/commit/99c39584343e13aa7f52119bd4e22cc24bb52bdb), [1893a63](https://github.com/DPDK/dpdk/commit/1893a6331a46603803a23d07a5a6a9fa564cbc3d), [f6323a2](https://github.com/DPDK/dpdk/commit/f6323a2561b673665550fe3696702ee815ae0f11), [deca182](https://github.com/DPDK/dpdk/commit/deca182c8c129fd365853d407bf19767ceeeb2a7), [d061b3a](https://github.com/DPDK/dpdk/commit/d061b3a53355b5976de45092fc853f0f46d8199e), [bff1ed5](https://github.com/DPDK/dpdk/commit/bff1ed567bd0de967b01615f99f3af781f91f651), [5c01159](https://github.com/DPDK/dpdk/commit/5c01159bf31e295c7d59f2e61d0b3afd7a9f6c14), [7630aa3](https://github.com/DPDK/dpdk/commit/7630aa3f5a7da4975d22f4f0e6c80bf895a09489)
- Replace perror calls with logging in the DPAA bus, telemetry and common/dpaax drivers.
  ↳ No PR: [ee3af0e](https://github.com/DPDK/dpdk/commit/ee3af0e2c0aadec8c9bf7f10406bbc3707f88163), [c3a6788](https://github.com/DPDK/dpdk/commit/c3a67888b329b68043b9766c189b1d19350a1af3), [4422044](https://github.com/DPDK/dpdk/commit/442204438dfc63fd8595b1e483b037a2b5359051)
- Remove unnecessary __rte_unused attribute flag in nfb and af_packet drivers.
  ↳ No PR: [635f633](https://github.com/DPDK/dpdk/commit/635f63381868f1d02c1d3d7ba28d7b937f8b6572), [8d3e1cb](https://github.com/DPDK/dpdk/commit/8d3e1cb62d742905a52156b07f3d75548c2077fc)
- Delete old source files in the bnxt driver that were never compiled and used.
  ↳ No PR: [f8732c1](https://github.com/DPDK/dpdk/commit/f8732c176e7c60158bca38e2f28a92871042c4a8)
- Set the physical address for the digest buffer in the PDCP preprocessor function.
  ↳ No PR: [9b1a845](https://github.com/DPDK/dpdk/commit/9b1a845e51e752158489cd6040024f3121644906)
- Fixed the variable shadowing problem caused by nested RTE_MIN macros in the ice driver.
  ↳ No PR: [085df9f](https://github.com/DPDK/dpdk/commit/085df9fdcbceb2453deee4b55750c51cf30ba8a8)
- Fixed the variable shadowing problem in the cpfl driver and removed unnecessary variable definitions.
  ↳ No PR: [b26d1df](https://github.com/DPDK/dpdk/commit/b26d1df93beba75aa22d8f7cbc0e5d4756494db6)
- Removed unused rte_memcpy.h header file from several example files.
  ↳ No PR: [0b308d5](https://github.com/DPDK/dpdk/commit/0b308d5ee5952f0eb52b0fa77a5bf1af7cb52904)
- During EAL initialization, log INFO level log warning when worker thread name is truncated due to length limit.
  ↳ No PR: [b7b305e](https://github.com/DPDK/dpdk/commit/b7b305ed97d97a0f813c734643f2510f01cb26b3)
- Adjust some error log levels to debug level to reduce log output in non-critical scenarios.
  ↳ No PR: [506be24](https://github.com/DPDK/dpdk/commit/506be24581e6af360167f9a97b039f5584bf3032)
- Remove support for test chip CFG_METHOD_69, clean up related code and adjust default configuration.
  ↳ No PR: [5baaf5a](https://github.com/DPDK/dpdk/commit/5baaf5a1953ced9af4b6b8af601e979a9d111eac)
- Prevent repeated calls to the Rx path selection function after the device is started to avoid unnecessary performance overhead.
  ↳ No PR: [594db65](https://github.com/DPDK/dpdk/commit/594db65528ba588ed54e86a272553d2ced1078ff), [565f704](https://github.com/DPDK/dpdk/commit/565f70444e625fe61c57d54cd493dff911b88b76)
- Unify the flexbytes array length definition in the FDIR structure into an i40e-specific macro.
  ↳ No PR: [401d7be](https://github.com/DPDK/dpdk/commit/401d7be41f08ea841057e768728dad1d75f92eb0)
- Add initialization for local variables in the cnxk driver send function to avoid using uninitialized variables.
  ↳ No PR: [f37549f](https://github.com/DPDK/dpdk/commit/f37549f680ceb8d37ae713598bb60814e5d0d57d)
- Add bounds check on control word size in bnxt driver, fix warning about possible use of uninitialized variables when compiling with GCC 16.
  ↳ No PR: [bad04ef](https://github.com/DPDK/dpdk/commit/bad04ef83fc3b367c0e297ea46394f7c6b138162)
- Fixed clang compilation warning caused by misuse of comma operator in Intel PMD.
  ↳ No PR: [3dd316f](https://github.com/DPDK/dpdk/commit/3dd316f03ec631cb3d1cc79347a69222840e7151)
- Replace rte_memcpy with struct assignment in example code to improve type safety.
  ↳ No PR: [84308d6](https://github.com/DPDK/dpdk/commit/84308d6ad4d00521ce862cc014d11e84b048efea)

### Others
- Fixed a compilation error caused by uninitialized variables in minsize builds.
  ↳ No PR: [614fcf1](https://github.com/DPDK/dpdk/commit/614fcf1b4e371206a617ff7cc6eebe1173e15b5b)
- Added switch domain and Rx domain matching checks for shared queues in testpmd's Rx queue settings.
  ↳ No PR: [8ebba91](https://github.com/DPDK/dpdk/commit/8ebba91086f47c90e398d7775921e05659c0d62f)
- Fixed a memory leak during port attach in testpmd.
  ↳ No PR: [d1b5082](https://github.com/DPDK/dpdk/commit/d1b5082f134c50a07679f9068be472f62cf3b608)
- Fixed a segmentation fault in the bnxt driver caused by improper HWRM capability query order.
  ↳ No PR: [0e2b6de](https://github.com/DPDK/dpdk/commit/0e2b6deb6b2590945fabee6f4cfa500977f66769)
- Fixed a message processing error caused when outer UDP checksum offloading is enabled on hardware that supports simple BD.
  ↳ No PR: [dce76ac](https://github.com/DPDK/dpdk/commit/dce76acf61859242946e619cf6113de5e134b117)
- Fixed an issue where outer VLAN stripping was unexpectedly disabled after enabling or disabling inner VLAN stripping.
  ↳ No PR: [5b00b18](https://github.com/DPDK/dpdk/commit/5b00b18884e825215c506407d906a13e796d9adc)
- Change the clock reading function of the igc network card to read the hardware timestamp register.
  ↳ No PR: [f2930ba](https://github.com/DPDK/dpdk/commit/f2930bafb22d6a31c2e78cf096c72179c1d4c1b6)
- Fixed an issue where IP tunnel detection in HWS was not RFC compliant, tunnel type is now correctly identified based on the protocol field of the outer IP header.
  ↳ No PR: [cae606b](https://github.com/DPDK/dpdk/commit/cae606b65a46ec0e62bdc4e6aabb50cf58fdeb0d)
- Fixed an issue where port status was not correctly set to down when link detection failed.
  ↳ No PR: [85182f9](https://github.com/DPDK/dpdk/commit/85182f9006c3f26ba6c61148110565ae3e655573)
- Fixed source buffer alignment logic in QAT driver.
  ↳ No PR: [89895cd](https://github.com/DPDK/dpdk/commit/89895cdab75f160ec8323d0f6946ebe0a4e7851d)
- Fixed grammar, spelling and formatting issues in DPDK 26.03 release notes.
  ↳ No PR: [d3b78b6](https://github.com/DPDK/dpdk/commit/d3b78b62e7ec3832e365760bf58195f77e3d4afc)
- Updated the recommended firmware version of E830 in the ice network card documentation to 1.11.
  ↳ No PR: [4a0fef4](https://github.com/DPDK/dpdk/commit/4a0fef49ecb8a795e0f4afffc5f86e4da4684fb8)
- Added missing RST documentation files for RSS test suite.
  ↳ No PR: [92bc9f0](https://github.com/DPDK/dpdk/commit/92bc9f05375c8c1c0b91fdefacb583b854cbb802)
- Fixed grammar, spelling errors and expressions in the Linux Getting Started Guide document.
  ↳ No PR: [f45c706](https://github.com/DPDK/dpdk/commit/f45c7060ab03a31462817f1e2dd22e9aab0fb912)
- Fixed grammar, spelling, style and code example errors in the eventdev programming guide, and updated outdated library paths.
  ↳ No PR: [9aa8e1a](https://github.com/DPDK/dpdk/commit/9aa8e1abefbffc0e0e0c0f9d0a89e44484082fd0)
- Added extra logging for recursive calls to aid debugging.
  ↳ No PR: [93450f1](https://github.com/DPDK/dpdk/commit/93450f129688a7a625ebfea91d996537fdb61679)
- Fixed grammatical, punctuation and spelling errors in the ethdev guide documentation.
  ↳ No PR: [6084025](https://github.com/DPDK/dpdk/commit/60840259cd5f90195f4d709a2e736e3a6ad1eb1a)
- Fixed grammatical, spelling, punctuation and formatting errors in QoS Framework documentation.
  ↳ No PR: [d32993e](https://github.com/DPDK/dpdk/commit/d32993e3cd5c93045991d9fd190c18463a238d2c)
- Fixed spelling and grammatical errors in the switch representation guide.
  ↳ No PR: [e88e350](https://github.com/DPDK/dpdk/commit/e88e350f6939d356cb591065481d169489670d6a)
- Fixed spelling, grammatical and punctuation errors in the Traffic Management Guide and Traffic Measurement and Policy documentation.
  ↳ No PR: [7ecdbb4](https://github.com/DPDK/dpdk/commit/7ecdbb4419118f5a6770a02c0ebc88f7fa88188b), [2e5957d](https://github.com/DPDK/dpdk/commit/2e5957db4029ec432b8f643631b6edee1c8ae188)
- Fixed typo in comments in pcapng module.
  ↳ No PR: [00fd2cb](https://github.com/DPDK/dpdk/commit/00fd2cb5efc78a8484426e05ed94d05e965669e7)
- Fixed the spelling error of macro name IDPD_TXQ_SCAN_CQ_THRESH, corrected to IDPF_TXQ_SCAN_CQ_THRESH.
  ↳ No PR: [aecba37](https://github.com/DPDK/dpdk/commit/aecba37874e9292ef63d8f3b46f08b3f53e68463)
- Removed reference to the deprecated testpmd --pkt-filter-mode parameter in the documentation.
  ↳ No PR: [29380c9](https://github.com/DPDK/dpdk/commit/29380c93e6d928b5991f1dc4bde181cea452a8a2)
- Fixed format specifier for port ID in several examples, correcting PRIu8 to PRIu16 to match uint16_t type.
  ↳ No PR: [626d4e3](https://github.com/DPDK/dpdk/commit/626d4e39327333cd5508885162e45ca7fb94ef7f), [3a5b636](https://github.com/DPDK/dpdk/commit/3a5b6366ac28c9d5bf9e9e149e67f70534a8efc0), [66309fc](https://github.com/DPDK/dpdk/commit/66309fc782da72b6a1db3c9674f29e19c5769393)
