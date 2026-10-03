# Release Note

## Important Changes

### Cross-cutting / Other Architecture-related Changes
- Added Generic MAC Feeder (GMF) module, which provides the function of feeding data directly from FPGA to MAC module. (Architecture event: Added GMF module)
  ↳ No PR: [30b2f87](https://github.com/DPDK/dpdk/commit/30b2f87ac650e33b9ca34d2f568696016d3cf393)
- Added RPF (receive port FIFO) module, used to control the packet storage FIFO in FPGA. (Architecture event: Added RPF module)
  ↳ No PR: [21a6609](https://github.com/DPDK/dpdk/commit/21a66096bb44a4468353782c36fc85913520dc6c)
- Add STA module support for FPGA mapping and enable statistical functions. (Architecture event: Added STA module)
  ↳ No PR: [672e817](https://github.com/DPDK/dpdk/commit/672e81740f7c529572f4a3509e7a7df0277e90a7)
- Add meter module to ntnic network card driver, support configuring meter profile, meter policy, create/destroy streams and read/update statistical information. (Architecture event: Add meter module)
  ↳ No PR: [c35c06f](https://github.com/DPDK/dpdk/commit/c35c06fb4ac1aee609fbca05116655628a844172)
- Added info flow module, which is used to track FPGA hard-coded parameters and provide an abstraction of whether the parameters are supported. (Architecture-related: New flow module)
  ↳ No PR: [e3723ca](https://github.com/DPDK/dpdk/commit/e3723ca6f492f3b1df4799ae9248860ddf214be3)
- Added uncore power management driver support for AMD EPYC processors, providing uncore frequency acquisition, setting and initialization/exit functions. (Architecture-related: Added AMD EPYC uncore driver)
  ↳ No PR: [da4d64d](https://github.com/DPDK/dpdk/commit/da4d64d0e80343d54ec22b583c6cc606826e73ba)
- Added rte_telemetry_register_cmd_arg function to support callback registration with private parameters. (Architecture-related: public API)
  ↳ No PR: [ceb5914](https://github.com/DPDK/dpdk/commit/ceb5914cd1e153b01bedd9f14a8119355114a21f)
- Reconstruct the core power management, move each driver implementation from lib/power to the drivers/power directory, each driver provides an independent ops structure, and the core library uniformly manages driver initialization and uninstallation through the ops pointer. (Architecture-related: driver architecture reconstruction)
  ↳ No PR: [6f987b5](https://github.com/DPDK/dpdk/commit/6f987b594fa6751b49769755fe1d1bf9f9d15ac4)
- Reconstruct uncore power management, create an independent directory for each driver, and introduce an ops-based driver registration mechanism to support selective activation. (Architecture-related: driver registration mechanism)
  ↳ No PR: [ebe99d3](https://github.com/DPDK/dpdk/commit/ebe99d351a3f79acf305b882052f286c65cd9b25)
- Unified IPv6 addresses are expressed as rte_ipv6_addr structure, and IPv4/IPv6 related symbols are split from the header file rte_ip.h to independent header files rte_ip4.h, rte_ip6.h, and the checksum function is split into rte_cksum.h to maintain backward compatibility. (Architecture-related: public API)
  ↳ No PR: [4149b1f](https://github.com/DPDK/dpdk/commit/4149b1fb5e0bd3f5339a62c0058125e6305b9122), [1a2b549](https://github.com/DPDK/dpdk/commit/1a2b549bb482b580424ed40b3b33d0673fcd89b0), [2cfebc3](https://github.com/DPDK/dpdk/commit/2cfebc3f1046e4166e13b4f906e3ddc1c26c7eeb), [5ac1abd](https://github.com/DPDK/dpdk/commit/5ac1abdd37aa43692603cd8670111c354014766f), [431e6b9](https://github.com/DPDK/dpdk/commit/431e6b9a618329cc684f6b3db91195757cbae07e), [41d71ae](https://github.com/DPDK/dpdk/commit/41d71aeb56694f06d60f0de20e5ac2d718ea5328)
- Reconstruct syslog processing from EAL to the lib/log layer, unify Linux and FreeBSD implementations, and add FreeBSD syslog support; only log to syslog when the --syslog option is specified, otherwise only output to standard error. (Architecture-related: log layer reconstruction)
  ↳ No PR: [9851303](https://github.com/DPDK/dpdk/commit/985130369be32dd68ca104c1ccc86716f6e2bb7b)
- Reconstruct the MC VFIO driver, introduce a group/container-based management model, support multi-process communication, and allow multiple MC groups to be connected to the same VFIO container. (Architecture-related: VFIO management model)
  ↳ No PR: [57cb02e](https://github.com/DPDK/dpdk/commit/57cb02edf1224b0464dd1744a7f540c8f7f21a08)
- Make the fslmc bus IOVA mode configuration dynamic, remove the compile-time CFLAGS configuration, use the runtime API to determine the VA/PA mode, and reconstruct the IOMMU mapping and DMA mapping management of memory and I/O. (Architecture-related: Dynamic IOVA mode)
  ↳ No PR: [a3c123e](https://github.com/DPDK/dpdk/commit/a3c123e22dc685db778de34edb234642cd6e17ac)
- Expand WFE/WFET instruction support on the ARM platform, making it always available under 64-bit and adding power management functions. (Architecture-related: platform compatibility)
  ↳ No PR: [990b065](https://github.com/DPDK/dpdk/commit/990b065f3a3b209282527203663dfb7991723917), [2f1a90f](https://github.com/DPDK/dpdk/commit/2f1a90f0455b4920df3a767ab5d9be37dcbf0d12)
- Added API for obtaining the number of queue pairs for ML devices. (Architecture-related: public API)
  ↳ No PR: [804786f](https://github.com/DPDK/dpdk/commit/804786f1012a35ee665e9d0fdf3bee1847a374fc)
- Increase the maximum number of IPC file descriptors from 8 to 253, and lift the limit on the number of queues in the TAP and XDP drivers. (Architecture-related: public API)
  ↳ No PR: [5ff00bb](https://github.com/DPDK/dpdk/commit/5ff00bbc04d8338108241b083b7a6238208cfbc6)
- Add Rx burst support for CN20K network card, including scalar version and vectorized batch reception. (Architecture event: Added cn20k hardware support)
  ↳ No PR: [493c4fa](https://github.com/DPDK/dpdk/commit/493c4fa524a266d2ee492a86857f2d643ef7acca), [9a8b99c](https://github.com/DPDK/dpdk/commit/9a8b99cf8822aa4f911da7f3ff512c6259b836ce)
- Add vectorized Tx burst support for CN20K network card, including basic vector send, multi-segment send and TSO functions. (Architecture event: Added cn20k hardware support)
  ↳ No PR: [e829e60](https://github.com/DPDK/dpdk/commit/e829e60c6917de836b4b417961b628b438a9a4b3), [98613d3](https://github.com/DPDK/dpdk/commit/98613d32e3dac58d685f4f236cf8cc9733abaaf3)
- Reconstructed unicast DMAC control flow rules, added a dedicated type and recorded DMAC and VLAN ID in the flow information; separated the creation logic from port startup, supported the creation of unicast DMAC and unicast DMAC+VLAN flow rules separately after port startup, and added corresponding creation and destruction interfaces; also added a dynamic management function to support adding, removing and destroying unicast DMAC and DMAC+VLAN control flow rules. (Architecture-related: public API)
  ↳ No PR: [a977e2b](https://github.com/DPDK/dpdk/commit/a977e2b5b2768e74019ccab52943b7c0d3c30470), [da7f82b](https://github.com/DPDK/dpdk/commit/da7f82b0af62649612979f6f944ca0fdd8148c4e), [04ea846](https://github.com/DPDK/dpdk/commit/04ea84684aa296659dac15892abadfa4ef083faa), [d9f2849](https://github.com/DPDK/dpdk/commit/d9f284954a7387789fa6658c284a00de647a692d), [9660a4e](https://github.com/DPDK/dpdk/commit/9660a4e62afd7aef519b306da8eaeb1197da635e), [80a5af9](https://github.com/DPDK/dpdk/commit/80a5af9f2adb23f1f13c34014f84abbf45abcadc), [cf99567](https://github.com/DPDK/dpdk/commit/cf99567fe566fb679a2d2485ab7c113a42df04f7), [86d0968](https://github.com/DPDK/dpdk/commit/86d09686c6c623adf6edd40d1217b48a8e56a425)
- Added RTE bitset type, provided functions and macros for operating large bitsets, and added atomic operation functions and corresponding unit tests. (Architecture-related: public API)
  ↳ No PR: [99a1197](https://github.com/DPDK/dpdk/commit/99a1197647d803e43a676622396ffddf6bf93b62), [c889c03](https://github.com/DPDK/dpdk/commit/c889c037f67342d972ef7a24580d3c24b6f33e26)
- Supports Ethernet type flow item matching, which can match the Ethernet type individually when using flower firmware. (Architecture-related: public API)
  ↳ No PR: [7217d25](https://github.com/DPDK/dpdk/commit/7217d258257bd85b88822f4e5f1427e7e20af799)
- Promoted multiple EAL core APIs from experimental status to stable, including power intrinsics, lcore usage and memzone segment configuration API. (Architecture-related: public API)
  ↳ No PR: [86a308f](https://github.com/DPDK/dpdk/commit/86a308fffa7752e460dcc9d8dba632f21ec3a8f3), [9625d8d](https://github.com/DPDK/dpdk/commit/9625d8dbd9248490026088a7f861c3fc03e4b139), [40e6cf9](https://github.com/DPDK/dpdk/commit/40e6cf97d3a785645f075bc40a051502f935881d)
- Added APIs for loading storage firmware and reading module EEPROM for the NSP module, and supported loading firmware from flash memory and reconstructed firmware loading logic. (Architecture-related: public API)
  ↳ No PR: [9e76c35](https://github.com/DPDK/dpdk/commit/9e76c352120f8860a75234699afa371ec6aa2e9a), [08ea495](https://github.com/DPDK/dpdk/commit/08ea495d624b5ef9899e43a62bfe87ecd1c5b1e4)
- Added new atomic bit operation API, including test, set, clear, assign, flip and test-and-set/clear/assign/flip functions, supports specifying memory order and volatile pointers, and added corresponding unit tests. (Architecture-related: public API)
  ↳ No PR: [35326b6](https://github.com/DPDK/dpdk/commit/35326b61aecb8e9653e889c217b775fcbe95e39d), [0883d73](https://github.com/DPDK/dpdk/commit/0883d736a7e59fc1847e9c8185dc43eb43d32630), [471de10](https://github.com/DPDK/dpdk/commit/471de107ae234aceea8ee43e153b4d7ec3f3c755), [46ce151](https://github.com/DPDK/dpdk/commit/46ce151ce49d2e44155436adad5e39359db2889e), [899cffe](https://github.com/DPDK/dpdk/commit/899cffe059b8e7ef602d4e622abc6c34f28a2bef)
- Added silent mode support to the DPAA DMA driver, which can be enabled during configuration and checked for this mode during dequeue operations. (Architecture-related: public API)
  ↳ No PR: [7a7bb89](https://github.com/DPDK/dpdk/commit/7a7bb89e34b33b10eb149bf5934ff9900d19062e)
- Added device options for the ice driver, allowing users to specify the path of the loaded DDP package file. (Architecture-related: public API)
  ↳ No PR: [9dd6dd1](https://github.com/DPDK/dpdk/commit/9dd6dd1db8344cd2e389687d97e5272a98498773)
- The public API for VFIO DMA mapping and unmapping is declared in bus_fslmc_driver.h. (Architecture-related: public API)
  ↳ No PR: [12dc253](https://github.com/DPDK/dpdk/commit/12dc2539f7b12b2ec4570197c1e8a16a973d71f6)
- Introduced the STE array matcher (only as an isolated matcher under the parent table) and the action of jumping to the matcher. It supports jumping to the STE array matcher and the matcher with size 1 through index. (Architecture-related: public API)
  ↳ No PR: [486f9aa](https://github.com/DPDK/dpdk/commit/486f9aac0cbe2598a76c853890c1d557747f71cf), [efb6249](https://github.com/DPDK/dpdk/commit/efb62499c623db13b7396231d0da8d1906d23d9b)
- Supports configuring DPI DMA queue priority through mailbox requests, and exposes priority capabilities in device information. (Architecture-related: public API)
  ↳ No PR: [fca0bae](https://github.com/DPDK/dpdk/commit/fca0bae93126541c90173d84dae1ead2fe9eeacc)
- Enhanced IPsec extended sequence number (ESN) support, initializes the sequence number and sets the high 32 bits, and declares ESN support in the security capability. (Architecture-related: IPsec ESN)
  ↳ No PR: [123098c](https://github.com/DPDK/dpdk/commit/123098cdd4039858f5ed6941e38c2513ae3940fb)
- Supports UDP encapsulated ESP protocol to implement IPsec NAT-T traversal function. (Architecture-related: IPsec NAT-T)
  ↳ No PR: [32d8bc5](https://github.com/DPDK/dpdk/commit/32d8bc55476dcfabf3b3650f75fc19c9b09050ba)
- In IPSEC ESP protocol offload mode, add UDP encapsulation (NAT-T traversal) support for IPv6 tunnels, and fix resource release issues in related session initialization. (Architecture-related: IPsec NAT-T)
  ↳ No PR: [3a38852](https://github.com/DPDK/dpdk/commit/3a3885276124a26cce507a6bf0a8f2f54de25ad0)
- Added lcore variable static memory allocation mechanism, providing independent variable storage for each lcore, and integrating resource release in the EAL cleanup process. At the same time, each lcore state storage in PRNG, power management, service library and other modules will be migrated to lcore variables to improve cache friendliness and performance. (Architecture-related: public API)
  ↳ No PR: [5bce9be](https://github.com/DPDK/dpdk/commit/5bce9bed67ad59aa5aede02256a8490d758b0c29), [29c39cd](https://github.com/DPDK/dpdk/commit/29c39cd3d54d8330ee578dd3ea27cfda1c562079), [1306433](https://github.com/DPDK/dpdk/commit/13064331957930f6b6c49ad02a638d7d5516c88f), [b24bbae](https://github.com/DPDK/dpdk/commit/b24bbaedbba2df6ad2c25bc0bbde52fb55876fdb), [b0faa83](https://github.com/DPDK/dpdk/commit/b0faa8330bfdc919c6591850e883b57304bd0fbe), [2cd441b](https://github.com/DPDK/dpdk/commit/2cd441bd17fc43768755162bfb218395c795b82d)
- Added __rte_unreachable and __rte_assume macros, which are used to mark unreachable code and provide precondition information to assist compiler optimization. (Architecture-related: public API)
  ↳ No PR: [bf7ded9](https://github.com/DPDK/dpdk/commit/bf7ded9a07f6c7f9dbf9c6be417302d783e805d6)
- Added hw.contigmem.coredump_enable tunable parameter in the contigmem driver of the FreeBSD kernel, which is used to control whether mapped contiguous memory buffers are included in core dumps. (Architecture-related: platform compatibility)
  ↳ No PR: [cbe57f3](https://github.com/DPDK/dpdk/commit/cbe57f351b4e6541eb7b50a5c0d6f7e77b45c9db)
- Add a timestamp option to the log system, support multiple time formats (such as relative startup time, ISO 8601, etc.), and add the --log-timestamp command line parameter; also add a localtime_r replacement function for the Windows platform. (Architecture-related: platform compatibility)
  ↳ No PR: [62ae114](https://github.com/DPDK/dpdk/commit/62ae1149f2bdaed3482abb08f2e255f1ac4746e7)
- Support systemd journal log protocol, which is automatically detected and used when the DPDK application is running as a systemd service to record priority and other log information. (Architecture-related: platform compatibility)
  ↳ No PR: [9da0dc6](https://github.com/DPDK/dpdk/commit/9da0dc6c0331a65e841d27dde7cae4441294a313)
- Improved the rte_eth_bond_member_add, rte_eth_bond_member_remove, rte_eth_bond_members_get, rte_eth_bond_active_members_get and rte_eth_bond_8023ad_member_info interfaces in the bonding driver from experimental to stable API. (Architecture-related: public API stabilization)
  ↳ No PR: [19da63c](https://github.com/DPDK/dpdk/commit/19da63ccfc7e83f06e1bb14d830d4e0de99b13cf)
- Introduced log option parser, added eal_option_is_log auxiliary function, expanded log option processing, supported --log-timestamp and --log-color options. (Architecture-related: public API)
  ↳ No PR: [9a4276f](https://github.com/DPDK/dpdk/commit/9a4276f92d3d9703c3509c67629a0fa3632d53a6)
- Added CPU granular PM QoS API, and provided command line configuration in the l3fwd-power example. (Architecture-related: public API)
  ↳ No PR: [dd6fd75](https://github.com/DPDK/dpdk/commit/dd6fd75bf662e89edf2cda8f34c37e762e79c274), [4d23d39](https://github.com/DPDK/dpdk/commit/4d23d39fd06ed89b2d2566273b95bbecbd48ed83)
- Add queue initialization and release interfaces to GDTC raw device, support queue setting operations, and add support for enqueue operations, including enqueue_bufs interface and related auxiliary functions. (Architecture-related: public API)
  ↳ No PR: [d373c66](https://github.com/DPDK/dpdk/commit/d373c66ef139ad4fa1847c4ea11f37a50b497fb7), [648001a](https://github.com/DPDK/dpdk/commit/648001aa00a15e48bb7f6a3acdf6fc9b48895dbb), [a73d74c](https://github.com/DPDK/dpdk/commit/a73d74c2e30e7111b71b863aadf0c351a0f7ec8c)
- Increase the maximum number of queues in the TAP driver from 16 to 64, remove redundant queue number checks, and add compile-time assertions to ensure that the multi-process file descriptor limit is not exceeded. (Architecture-related: build and installation methods)
  ↳ No PR: [6a2e47a](https://github.com/DPDK/dpdk/commit/6a2e47a3e26acb5ec206918c7f6454ee4aefa138), [9439fee](https://github.com/DPDK/dpdk/commit/9439fee9187069d43536f676b566ab0b68645502), [039aded](https://github.com/DPDK/dpdk/commit/039aded84451df5a2b90035474ed309569c236e2)
- Add metadata splitting function to mlx5 driver to support compatibility in hardware streaming (HWS) mode. When FDB rule specifies mark action, rules will be automatically created in NIC Rx to match and copy metadata. (Architecture-related: external behavior)
  ↳ No PR: [821a6a5](https://github.com/DPDK/dpdk/commit/821a6a5cc4951337a7eac64b6cce6a25c01be442)
- Add an available enqueuing depth counter to bbdev to help applications monitor the available enqueuing depth of the queue. (Architecture-related: public API)
  ↳ No PR: [f8d8fa0](https://github.com/DPDK/dpdk/commit/f8d8fa0eea4b0d4c91da9ff3da03162135c3f706)
- Replace the flag enumeration in the argparse library with macro definitions to solve the problem of enumeration value type mismatch, correct the flags type from uint32_t to uint64_t, introduce bit mask macros and update test cases. (Architecture-related: public API)
  ↳ No PR: [bd0d68b](https://github.com/DPDK/dpdk/commit/bd0d68bdc36d4422176e72d49eccfe88f167e3d9), [f48e4ee](https://github.com/DPDK/dpdk/commit/f48e4eed4aebba5b61565fbf8515fd723b53cd0c)
- Fixed the issue where 200G link speed was not advertised correctly during PHY configuration initialization, extended the link speed mask to include 200G rate bits. (Architecture-related: public API)
  ↳ No PR: [e3992ab](https://github.com/DPDK/dpdk/commit/e3992ab377d2879d6c5bfb220865638404b85dba)
- Fixed the REX prefix problem of write combined storage instructions in 32-bit mode, and removed unnecessary bytes to ensure compatibility. (Architecture-related: platform compatibility)
  ↳ No PR: [41b09d6](https://github.com/DPDK/dpdk/commit/41b09d64e35b877e8f29c4e5a8cf944e303695dd)
- Fixed the problem of VFIO hot-plugging in multi-process scenarios, enhanced automatic retry support, and removed redundant functions. (Architecture-related: VFIO multi-process synchronization)
  ↳ No PR: [6e18a2d](https://github.com/DPDK/dpdk/commit/6e18a2d452b2712930338f482960235687007fd0), [5f7b981](https://github.com/DPDK/dpdk/commit/5f7b98189de733080656989d63b0e7ffd249830a)
- Fixed multiple issues with flex item in mlx5 driver, including tunnel mode processing, protocol verification, sample field matching, header length translation and maximum parser number limit. (Architecture-related: mlx5 flex item behavior)
  ↳ No PR: [624ca89](https://github.com/DPDK/dpdk/commit/624ca89b57550f13c49224d931d391680dc62d69), [e46b266](https://github.com/DPDK/dpdk/commit/e46b26663de964b54ed9fc2e7eade07261d8e396), [16d8f37](https://github.com/DPDK/dpdk/commit/16d8f37b4ebb59a2b2d48dbd9c0f3b8302d4ab1f), [3847a3b](https://github.com/DPDK/dpdk/commit/3847a3b192315491118eab9830e695eb2c9946e2), [97e19f0](https://github.com/DPDK/dpdk/commit/97e19f0762e5235d6914845a59823d4ea36925bb), [b04b06f](https://github.com/DPDK/dpdk/commit/b04b06f4cb3f3bdd24228f3ca2ec5b3a7b64308d)
- Fix strict alias violation warning due to type pun pointer in rte_mbuf_raw_alloc function, avoid incorrect type conversion by using inline union variables. (Architecture-related: public API)
  ↳ No PR: [6011b12](https://github.com/DPDK/dpdk/commit/6011b12f52b60565d4dfcc3b382551ec1f53b3d4)
- Fixed the thread starvation problem caused by lock competition in rte_eal_alarm_cancel, calling sched_yield() (SwitchToThread() on Windows) after releasing the lock to give up CPU control. (Architecture-related: public API)
  ↳ No PR: [a4835c2](https://github.com/DPDK/dpdk/commit/a4835c22ccfb5c5ba0aa5b32ebbafc0df12bf75a)
- Fixed the problem of incorrect mapping between lcore ID and CPU ID in the power library. Now the CPU ID can be obtained correctly based on the mapping relationship, and only supports lcore mapped to a single physical core. (Architecture-related: public API)
  ↳ No PR: [5c9b07e](https://github.com/DPDK/dpdk/commit/5c9b07eeba55d527025f1f4945e2dbb366f21215), [bc5ca53](https://github.com/DPDK/dpdk/commit/bc5ca53efb4b97a943085d625408410b59080bb6)
- Add const qualification to getopt series function parameters on Windows platform, consistent with FreeBSD version. (Architecture-related: platform compatibility)
  ↳ No PR: [a06fb0f](https://github.com/DPDK/dpdk/commit/a06fb0fae6ab6a79fa3e8288dbb0c5166be843c2)
- Advance log initialization to the beginning of rte_eal_init() to ensure that all log messages (including CPU mismatch, etc.) can be output through the log library. (Architecture-related: initialization process)
  ↳ No PR: [2773d39](https://github.com/DPDK/dpdk/commit/2773d39ffee46f66fd628cebdd401d89fce09f1f)
- Fix heap corruption caused by lcore variables memory release mismatch on Windows, and limit the maximum size of each lcore variable to 128K to avoid memory exhaustion. (Architecture-related: platform compatibility)
  ↳ No PR: [9ebdbe6](https://github.com/DPDK/dpdk/commit/9ebdbe62c2aaae8f71851483139b3b4dcfaf991b), [f2fd6c2](https://github.com/DPDK/dpdk/commit/f2fd6c2e080c0c595bcc72d8c05d9e1014d398e2)
- Fixed the fslmc bus scanning failure issue on non-DPAA2 platforms, and removed the debug log. (Architecture-related: platform compatibility)
  ↳ No PR: [b472c50](https://github.com/DPDK/dpdk/commit/b472c50aeee1ca4f3a86be0580d31474653dfd8f)
- Fix the default RSS stream creation order to ensure that rules are created in the correct priority order in SWS and HWS modes. (Architecture-related: Packet processing priority)
  ↳ No PR: [9a66bb7](https://github.com/DPDK/dpdk/commit/9a66bb734e1311bcc2bf3b286f7ab6d28975c5c7)
- Fixed the issue where the Rx queue reference count was not reduced correctly when stopping the port and refreshing the flow rules, and introduced the device-level refresh flag. (Architecture-related: Resource Management)
  ↳ No PR: [1ea333d](https://github.com/DPDK/dpdk/commit/1ea333d2de220d5bad600ed50b43f91f7703c123)
- Fix MSVC compiler warning in RCU QSBR library due to implicit conversion of 32-bit shifts to 64-bit, and fix bug where bit operations may be wrong when thread ID is greater than 0x1f. (Architecture-related: Platform compatibility)
  ↳ No PR: [ffe827f](https://github.com/DPDK/dpdk/commit/ffe827f38e6e0be8a307d7ef9c0e1347874f0af7)
- Replace IPv6 address representation from uint8_t[16] array to rte_ipv6_addr structure, and update related API simultaneously. (Architecture-related: public API)
  ↳ No PR: [89b5642](https://github.com/DPDK/dpdk/commit/89b5642d0d45c22c0ceab57efe3fab3b49ff4324), [e1a06e3](https://github.com/DPDK/dpdk/commit/e1a06e391ba74f9c4d46a6ecef6d8ee084f4229e), [6cb10a9](https://github.com/DPDK/dpdk/commit/6cb10a9bdb6d2d0253e4d022f230371d703d8ac2), [59b9931](https://github.com/DPDK/dpdk/commit/59b993151ff57e9e8b0fdb1d4b57913243b605fa)
- Merge three independent devargs in the ena driver into a unified llq_policy devarg. (Architecture-related: public API)
  ↳ No PR: [d7918d1](https://github.com/DPDK/dpdk/commit/d7918d19d25ecfbac7326a28e8ff30c60662e4d7)
- Reconstruct the firmware version management logic and migrate the version information from the network card hardware structure to the PF device structure. (Architecture-related: core module responsibilities)
  ↳ No PR: [000feb4](https://github.com/DPDK/dpdk/commit/000feb4c417c9776236342e524d98e61e43e2f12)
- Reconstruct the kvargs processing API, and add the rte_kvargs_process_opt function to support key=value and key-only parameter formats. (Architecture-related: public API)
  ↳ No PR: [de89988](https://github.com/DPDK/dpdk/commit/de89988365a7ca4087dd451c675320c993910332)
- Extract the log level parsing logic from the EAL implementation of each platform to the public option parsing module for unified processing. (Architecture-related: public API)
  ↳ No PR: [9eeefca](https://github.com/DPDK/dpdk/commit/9eeefca0c0d375dd4c76d3630d5a3913a8f94d96)
- Optimize the log output format of rte_exit(), use a unified prefix and change it to a single line to avoid confusion with timestamp and color options. (Architecture-related: public API)
  ↳ No PR: [c4e03ac](https://github.com/DPDK/dpdk/commit/c4e03aca4a241fb7bbd7754801604171412c5a0f)
- Rename the TAP device internal structure struct nlmsg to struct tap_nlmsg to avoid confusion with nlmsghdr in the netlink header file. (Architecture-related: public API)
  ↳ No PR: [b424101](https://github.com/DPDK/dpdk/commit/b4241019d426114fe7adb4da892053a1dbf51261)
- Rename the core power library source files from rte_power.* to rte_power_cpufreq.*, and update all relevant header file references. (Architecture-related: public API)
  ↳ No PR: [f30a1bb](https://github.com/DPDK/dpdk/commit/f30a1bbd63f494f5ba623582d7e9166c817794a4)
- Replace compiler built-in functions with macros provided by DPDK EAL in multiple drivers. (Architecture-related: Unification of EAL macros)
  ↳ No PR: [2204658](https://github.com/DPDK/dpdk/commit/2204658fa80698f17698626293d2cee2b706f2e0), [6d73669](https://github.com/DPDK/dpdk/commit/6d736695a7467eddd6feeef0be78e1a3b511610c), [191128d](https://github.com/DPDK/dpdk/commit/191128d7f6a02b816deaa86d761fbde4483724e9)
- Change the ice_alloc_lan_q_ctx function from static to non-static so that driver code can call it. (Architecture-related: public interface)
  ↳ No PR: [31f2a1d](https://github.com/DPDK/dpdk/commit/31f2a1d9460cd76733bc2ca990f2afabece9947d)
- Improve TSC frequency estimation accuracy, adjust rounding granularity from 10MHz to 100KHz, and allow CPU values to be overridden with frequencies provided by the operating system. (Architecture-related: Core timer behavior)
  ↳ No PR: [7268f21](https://github.com/DPDK/dpdk/commit/7268f21aa044309a74592a78955d7051bc7063c1), [dbdf3d5](https://github.com/DPDK/dpdk/commit/dbdf3d5581caa1de40b5952e41d54b64e39536d1)
- Add compiler property annotations to memory allocation functions, optimize alignment hints and help detect allocation and release mismatches. (Architecture-related: public API)
  ↳ No PR: [80da7ef](https://github.com/DPDK/dpdk/commit/80da7efbb4c4216de93b1039b891a6f31fa06f2d)
- Cache CPU feature query results on x86 platform to avoid repeated hardware queries, improve performance and fix errors in non-AVX virtual machines. (Architecture-related: platform compatibility)
  ↳ No PR: [4225db8](https://github.com/DPDK/dpdk/commit/4225db8dc0fa83c9ba1247ac5aec54ab7f3f8d94)
- Optimize MAC address and VLAN filtering processing, add or remove only necessary control flow rules, and improve related API performance. (Architecture-related: public API)
  ↳ No PR: [4653286](https://github.com/DPDK/dpdk/commit/465328609aeca77f455175b12440233dbcc5a826)
- Store each lcore's power internal state into an lcore variable, reducing cache working set size and avoiding false sharing. (Architecture-related: core module)
  ↳ No PR: [18b5049](https://github.com/DPDK/dpdk/commit/18b5049ab4fecda6ad303606cc265d923b56da14)
- Increase the maximum number of Rx/Tx descriptors of the ice driver to 8160 to support applications that require greater buffering capacity. (Architecture-related: core module)
  ↳ No PR: [a378cbf](https://github.com/DPDK/dpdk/commit/a378cbf017403b4526125e8d9d1b102059874bd1)
- Enable 200G link speed support for E830 devices. (Architecture-related: public API)
  ↳ No PR: [36ffcdc](https://github.com/DPDK/dpdk/commit/36ffcdc254be9a6dbdc6cbcbfdb02d5603463e5d)
- Updated the Windows build guide to update the Meson minimum version requirement to 1.5.2, and added instructions for specifying a 64-bit build in the Visual Studio developer command prompt. (Architecture-related: Build and install methods)
  ↳ No PR: [5d5dcd8](https://github.com/DPDK/dpdk/commit/5d5dcd8492f8b2863a2de0f5bad223df27749c09)
- Added list of tested Intel platforms in v24.11 release notes. (Architecture-related: Platform compatibility)
  ↳ No PR: [cb490d9](https://github.com/DPDK/dpdk/commit/cb490d9bf8638fe01b7873bdde67d18dd372feca)
- Fixed compilation errors caused by type conflicts on Fedora Rawhide platform, changing typedef to macro definition with conditional protection. (Architecture-related: platform compatibility)
  ↳ No PR: [f0d9e78](https://github.com/DPDK/dpdk/commit/f0d9e787747dda0715654da9f0501f54fe105868)
- Enhanced the header file checking build, added stable, experimental and internal API level compilation tests, and extended to driver-specific header files, fixed the vmbus driver header file dependency problem. (Architecture-related: build and installation methods)
  ↳ No PR: [e8752e3](https://github.com/DPDK/dpdk/commit/e8752e311a3d32d08c3fb04cc9a0262fbaa05b31), [90cb8ff](https://github.com/DPDK/dpdk/commit/90cb8ff8196f9b9c1c2bcee1c94ea583789bb63f)
- Added Neoverse N3 SoC support in Arm build configurations, including its part number and compilation options. (Architecture-related: Platform compatibility)
  ↳ No PR: [cdbcdc5](https://github.com/DPDK/dpdk/commit/cdbcdc5573933d709a95668982c7e31eb9249105)
- Started a new release cycle, cleared the release notes, updated the ABI version to 25.0, and removed the temporary ABI compatibility exception. (Architecture-related: ABI version)
  ↳ No PR: [cb9187b](https://github.com/DPDK/dpdk/commit/cb9187bc5c2b4bab0ad80194ac3b60491de14e8c)
- Added compile-time platform configuration in the cnxk driver, and set SOC type macros according to the build environment to distinguish different chips. (Architecture-related: platform compatibility)
  ↳ No PR: [814bede](https://github.com/DPDK/dpdk/commit/814bedeeed7ccd44191fcc7222254ece5fcc42c6)
- Change 32-bit x86 builds to use cross-compilation configuration files to avoid reconfiguration failures caused by missing environment variables. (Architecture-related: build and installation methods)
  ↳ No PR: [b7d0c73](https://github.com/DPDK/dpdk/commit/b7d0c73851aef89fb64867243015b80a138fa758)
- Adjusted the order of use of extern "C" in header files, moved it after all #includes, removed extern "C" in header files that do not declare symbols, and deleted mandatory checks. (Architecture-related: public API)
  ↳ No PR: [719834a](https://github.com/DPDK/dpdk/commit/719834a6849e1daf4a70ff7742bbcc3ae7e25607)
- Increased the minimum version requirement of the Meson build system from 0.53.2 to 0.57, and updated related documents simultaneously. (Architecture-related: Build requirements)
  ↳ No PR: [6f3dbd3](https://github.com/DPDK/dpdk/commit/6f3dbd306de03410cffb40a0f0b47a2cdcfcf362)
- Replace the deprecated get_cross_property in cross-compilation with get_external_property, adapting to Meson 0.58 and above. (Architecture-related: platform compatibility)
  ↳ No PR: [b0d0c84](https://github.com/DPDK/dpdk/commit/b0d0c84b3c0ffcdd0c3ef307c4966f06bd296db7)
- Fixed the build failure of net/mana driver when using custom rdma-core through pkg-config, updated meson.build to ensure that header file symbol detection correctly includes dependent libraries. (Architecture-related: pkg-config configuration)
  ↳ No PR: [8d7596c](https://github.com/DPDK/dpdk/commit/8d7596cad7abb413c25f6782fe62fd0d388b8b94)
- Supports specifying external DPDK source directory, tarball or precompiled build directory through configuration files, command line parameters or environment variables, and allows these resources to be stored on the SUT node or execution host. (Architecture-related: build and installation methods)
  ↳ No PR: [f995766](https://github.com/DPDK/dpdk/commit/f995766758403e13a7b97e6e3e863ac900716844)
- Added unified AVX512 support check in the build system for reuse by all drivers and libraries. (Architecture-related: platform compatibility)
  ↳ No PR: [979f59d](https://github.com/DPDK/dpdk/commit/979f59decf69023bdba93d16900c45c57fbdd9c0)
- Increase the minimum version requirement of Intel IPsec MB library to 1.4, remove the compatibility code for old versions, and add support for SM4 and SM3 algorithms. (Architecture-related: version and compatibility)
  ↳ No PR: [8484d74](https://github.com/DPDK/dpdk/commit/8484d74bd656bc0e951a3ed4e0816ee0fea5e593)
- Fixed the use of the deprecated get_cross_property function when cross compiling and changed it to get_external_property. (Architecture-related: platform compatibility)
  ↳ No PR: [530c0ac](https://github.com/DPDK/dpdk/commit/530c0ac654ff89de3f3e83e6ce6c6693739eb670)
- Set maximum lcore count to 768 for AMD EPYC Zen5 processors in x86 configuration. (Architecture-related: Platform compatibility)
  ↳ No PR: [892bf8c](https://github.com/DPDK/dpdk/commit/892bf8cf7ea1591e71f398657c2d4a29cd316d06)
- Fixed the deprecation warning for meson >= 0.55 when building natively on ARM, instead use files() to directly reference the script. (Architecture-related: build and installation methods)
  ↳ No PR: [c349556](https://github.com/DPDK/dpdk/commit/c3495563c5e13be8baf150196645bb944230c489)
- Allowed enabling the IOVA field in mbuf on the CNXK platform, and added a warning prompt, and updated the build configuration and documentation. (Architecture-related: platform compatibility)
  ↳ No PR: [592fdee](https://github.com/DPDK/dpdk/commit/592fdee47dbb9b8c1141a5d679eeab4f2861731f)
- Introduced the Linux kernel uAPI header file import mechanism, added import scripts, documentation and build configuration support. (Architecture-related: build and installation methods)
  ↳ No PR: [cf97dfd](https://github.com/DPDK/dpdk/commit/cf97dfd12eaf3617cf7243226efa4940729c9a9a)
- Imported the VDUSE kernel uAPI header file (based on Linux kernel v6.10), and removed conditional compilation, so that VDUSE supports always building on Linux systems. (Architecture-related: platform compatibility)
  ↳ No PR: [b212c2f](https://github.com/DPDK/dpdk/commit/b212c2fc2cd66f21272f48da3bb2e68513c5d92a), [9fec3f0](https://github.com/DPDK/dpdk/commit/9fec3f0569087de06666129c7f2badaf5be2776e)
- Added feature bit Meson compilation configuration parameters for the TruFlow function, which is used to enable optional capability features of the application. (Architecture-related: build and installation methods)
  ↳ No PR: [b413ab0](https://github.com/DPDK/dpdk/commit/b413ab0ae7932d2ab27d783870e3d9a698193f08)
- Fixed the compilation problem of the argparse library under the MSVC compiler, and now supports compilation using the Visual Studio toolset. (Architecture-related: platform compatibility)
  ↳ No PR: [85a9a58](https://github.com/DPDK/dpdk/commit/85a9a589da099f8da3230b38a0eb5e92e458b90c)
- Rolled back the VDUSE uAPI header file import, restored the use of system header files, and added conditional compilation to handle compilation errors when VDUSE support is disabled. (Architecture-related: public API)
  ↳ No PR: [4025e36](https://github.com/DPDK/dpdk/commit/4025e36fa5b7e44df07d53f8e7ddfeab5f1512a2)
- Move the API header file rte_pmd_ntnic.h to the driver directory and register it as a public header file in meson.build. (Architecture-related: public API)
  ↳ No PR: [de9f35e](https://github.com/DPDK/dpdk/commit/de9f35ebf2c40cbcdac4ca64888704619b84f8f6)
- Extend the checkpatches.sh script to disable the use of bit counting built-in functions such as __builtin_ffs and __builtin_ffsll to enhance MSVC compiler compatibility. (Architecture-related: platform compatibility)
  ↳ No PR: [65c6733](https://github.com/DPDK/dpdk/commit/65c6733a679eb4cc3b6dc00af75bc65280422775), [8fa925f](https://github.com/DPDK/dpdk/commit/8fa925fa206ef02de104cd4707db482731cf7e76)
- Unified use of standard AVX-512 build check variables in config/x86, replacing duplicate AVX-512 support detection logic in multiple drivers and net libraries. (Architecture-related: platform compatibility)
  ↳ No PR: [ef7a402](https://github.com/DPDK/dpdk/commit/ef7a4025cd714189dc333bb19ea60c2abdeffb7d), [82621e2](https://github.com/DPDK/dpdk/commit/82621e2fec8143c50f8847f385d6ee646f556b24)
- Remove checks for Meson build system versions 0.60 and 0.57, simplify build scripts and relax version requirements. (Architecture-related: build requirements)
  ↳ No PR: [2909f9a](https://github.com/DPDK/dpdk/commit/2909f9afbfd1b54ace204d40d57b68e6058aca28), [3019b11](https://github.com/DPDK/dpdk/commit/3019b11fc1fc7c2ed8a405a551391e51fd94a087)
- Supplement the definitions of standard file descriptor macros STDIN_FILENO, STDOUT_FILENO and STDERR_FILENO for the Windows platform to enhance platform compatibility. (Architecture-related: Platform compatibility)
  ↳ No PR: [e0bf217](https://github.com/DPDK/dpdk/commit/e0bf217330a89c30505f218ce89005cfb662af7c)
- Expand the Octeon EP driver mailbox function, support PF to VF message processing, and update the mailbox version to v3. (Architecture-related: mailbox interface)
  ↳ No PR: [826da0f](https://github.com/DPDK/dpdk/commit/826da0f56d42e256e647b7d32b5cb567f5263d52)
- Added an idx field in the nfp_flower_representor structure, which is used to identify the sequential physical port number of the representative port. (Architecture-related: representative port identification)
  ↳ No PR: [298f297](https://github.com/DPDK/dpdk/commit/298f29730a2258df9dd8d2b543e731c4f026cc01)
- Added two counters for service function call statistics: idle call count and error call count. (Architecture-related: public API)
  ↳ No PR: [a37e053](https://github.com/DPDK/dpdk/commit/a37e053b2364fc1104988285163261a8c7609dda)
- Add tunnel mode query API for flex item. (Architecture-related: public API)
  ↳ No PR: [850233a](https://github.com/DPDK/dpdk/commit/850233aca685ed1142ae2003ec6d4eefe82df4bd)
- Supports custom firmware search path for DDP package, PMD is loaded from system parameter path. (Architecture-related: driver loading configuration)
  ↳ No PR: [9207f93](https://github.com/DPDK/dpdk/commit/9207f93640a709cad1412430c5f0edfee3ad5a87)

### Packet Processing Nodes
- Added TSM (time stamp module), which provides functions such as physical network card timer operation, time synchronization, timestamp format and PTP protocol control. (Architecture event: Added TSM module)
  ↳ No PR: [3d600f7](https://github.com/DPDK/dpdk/commit/3d600f7d565fc530a411759a080c4039f78fde42), [a9cba85](https://github.com/DPDK/dpdk/commit/a9cba85abe7a8159a1c08af32cf3aa083b112ed2)
- Added the Tx Packet Editor (TPE) FPGA module and its software abstraction layer, which provides software abstraction management of multiple FPGA modules and implements the initialization and refresh functions of related RCP configurations. (Architectural event: ntnic FPGA hardware abstraction layer change)
  ↳ No PR: [7f05802](https://github.com/DPDK/dpdk/commit/7f058028ff772ef7a413a6fa41e87f41276df110), [4d4e901](https://github.com/DPDK/dpdk/commit/4d4e9018bea75f85f88c9cff51e80f1b2dbe0c90), [0b98e4c](https://github.com/DPDK/dpdk/commit/0b98e4c1509c446fac29b53726198e66babded87)
- Added SLC LR (Slicer for Local Retransmit) FPGA module, which is used to truncate the packet header before the data packet leaves the RX pipeline to match the TX pipeline to add a new packet header. (Architectural event: Added SLC LR FPGA module)
  ↳ No PR: [7fadd2b](https://github.com/DPDK/dpdk/commit/7fadd2ba32137dae8cfe1e4634c1b67a6d29e35a), [c4d1272](https://github.com/DPDK/dpdk/commit/c4d1272b279d8c770b6d662db9c5e3d31c7bcf29), [0beca5d](https://github.com/DPDK/dpdk/commit/0beca5d26a883ba2f690956222aee23a266de9ef)
- Added Packet Descriptor Builder (PDB) FPGA module, used to create packet metadata (such as virtio-net header). (Architecture event: Added PDB FPGA module)
  ↳ No PR: [87ad215](https://github.com/DPDK/dpdk/commit/87ad21510b751f799286b3c2cb8a62157332f536), [ef6e148](https://github.com/DPDK/dpdk/commit/ef6e148b813ca9caf4939b02d609aa9f3728dd6d)
- Added IP Fragmenter (IFR) flow module to support fragmentation of outbound packets based on programmable MTU. (Architecture-related: New flow module)
  ↳ No PR: [7d90a44](https://github.com/DPDK/dpdk/commit/7d90a4405e889f7edce73be8b541fc14e0192b61), [58c2db9](https://github.com/DPDK/dpdk/commit/58c2db9abaa9de58bd8e423cf31e182aabf33263)
- Uniformly migrated the IPv6 address representation in IPsec related code from uint8_t[16] array to rte_ipv6_addr structure, and updated the initialization, assignment and printing methods. (Architecture-related: public API)
  ↳ No PR: [9ac91e2](https://github.com/DPDK/dpdk/commit/9ac91e2f7339e66658ef55b756a06b328e336fde), [2ede142](https://github.com/DPDK/dpdk/commit/2ede1422fa57225b0864702083a8c7bea2c5117e)
- Changed the IPv6 address field in the stream API from the uint8_t[16] array to the rte_ipv6_addr structure, and updated the access method in the relevant driver and test code. (Architecture-related: public API)
  ↳ No PR: [cc13675](https://github.com/DPDK/dpdk/commit/cc13675026303f1da82551deee89027cda3d7aef)
- Migrate the same algorithm enumerations in the 9k and 10k platforms to the public namespace. (Architecture-related: public API)
  ↳ No PR: [c31a946](https://github.com/DPDK/dpdk/commit/c31a94655944a03716257e01376123cde65f7b35)
- Move the cn10k security PMD function definition to the cn9k/cn10k public code, and remove the reference to struct rte_security_session. (Architecture-related: public API)
  ↳ No PR: [99e540d](https://github.com/DPDK/dpdk/commit/99e540d65c9adbc1515543a635734055046a3c18)
- Clean up all unnecessary conditional compilation tags in the i40e base code, and remove VF support related code, because the VF function has been taken over by the IAVF driver. (Architecture-related: driver responsibility adjustment)
  ↳ No PR: [77b4bce](https://github.com/DPDK/dpdk/commit/77b4bceb6b4a0a59fb8ef96cce4b7518546a92ab)
- Add the definition of the high bits of the Rx error register, and migrate the receive error counter from the PF private structure to the basic driver statistics structure. (Architecture-related: public API)
  ↳ No PR: [08f6fed](https://github.com/DPDK/dpdk/commit/08f6fedee453df7390ed5623d2fe5ec5ab362f53)
- Fixed the rte_fib_rcu_qsbr_add() function returning a negative error code when recycling rules to comply with the API specification. (Architecture-related: public API)
  ↳ No PR: [cc8764c](https://github.com/DPDK/dpdk/commit/cc8764c6c9af150131f714bbe8d39de861d5e377)
- Add independent version, traffic category and flow label fields to the IPv6 header structure, and retain the original vtc_flow field to maintain backward compatibility. (Architecture-related: public API)
  ↳ No PR: [cba2799](https://github.com/DPDK/dpdk/commit/cba27998dc8124f0d816f6342dff7451b51fe5e0)
- Support using indirect counters instead of inline counters in SWITCH rules for tunnel offloading. (Architecture-related: public API)
  ↳ No PR: [5f70136](https://github.com/DPDK/dpdk/commit/5f701365ca2d867467026d72581f47d3f1ca60e0)
- Reconstruct queue statistics update logic in acc PMD, and extend the FFT function of VRB2 PRQ device. (Architecture-related: public API)
  ↳ No PR: [dded7c6](https://github.com/DPDK/dpdk/commit/dded7c68361180a284aaea3e57a9dc01bd41bf2a), [7a875f5](https://github.com/DPDK/dpdk/commit/7a875f5697aaab632e45d191888ceda35f78adb0)
- Added transmission mode ESP packet type constant and corresponding type name query support in the mbuf library. (Architecture-related: public API)
  ↳ No PR: [2ee0e59](https://github.com/DPDK/dpdk/commit/2ee0e591d24be762a8046307eaeb1dcc87504a11)
- Add support for symmetric algorithm SM4-XTS in cryptodev and update tests. (Architecture-related: public API)
  ↳ No PR: [4acc862](https://github.com/DPDK/dpdk/commit/4acc862b18a2f1691d1561f7b75542f6a056d41f)
- Add network byte order IPv4 address lookup support to the FIB library, and add the RTE_FIB_F_NETWORK_ORDER flag. (Architecture-related: public API)
  ↳ No PR: [e194f3c](https://github.com/DPDK/dpdk/commit/e194f3cd5685d5b16c8561a715395a5f579c1bf3)
- Added xstat counter support for graph nodes, and added related APIs for retrieving and incrementing node-specific counters. (Architecture-related: public API)
  ↳ No PR: [070db97](https://github.com/DPDK/dpdk/commit/070db97e017b7ed9a5320b2f624f05562a632bd3)
- Add flow scale query function to bnxt driver, support tracking the usage of WC TCAM, EM, Action and other resources, which can be queried through niccli; this function is disabled by default and needs to be enabled through the build flag TF_FLOW_SCALE_QUERY. (Architecture-related: Build configuration: TF_FLOW_SCALE_QUERY)
  ↳ No PR: [19f3ac6](https://github.com/DPDK/dpdk/commit/19f3ac618ab2d309e24a3034fcfdacaa6f31c718), [ffbc352](https://github.com/DPDK/dpdk/commit/ffbc3529089ac96517d4065a9b76c730c5586daa)
- Add the optional k0 parameter to the LDPC decoder API, allowing the circular buffer starting position to be specified directly, instead of deriving from the redundant version index; the baseband/acc driver already supports this parameter. (Architecture-related: public API)
  ↳ No PR: [591d38c](https://github.com/DPDK/dpdk/commit/591d38cc83f3ebe69ba44ce136170299d4825fdf), [cb9dc56](https://github.com/DPDK/dpdk/commit/cb9dc567af0392850a622e6ba80020bcc65de1e5)
- Add asymmetric/affine quantization support for ML devices, add scale and zero point fields to the I/O information structure, and support user-defined scaling factors and zero points in the data type conversion function. (Architecture-related: public API)
  ↳ No PR: [fe8eba6](https://github.com/DPDK/dpdk/commit/fe8eba692c59a92c9308f1fe429b101b9f2377bf), [65282e9](https://github.com/DPDK/dpdk/commit/65282e9f8e118a4ca977d1aee2d7f51f44e9bc1b)
- Added encrypted device queue pair reset API, allowing the specified queue pair to be reset without stopping the entire device; cnxk platform has implemented support. (Architecture-related: public API)
  ↳ No PR: [0a054e8](https://github.com/DPDK/dpdk/commit/0a054e8dd5b0960eec4226821137aceb77a2bf22), [3be1df0](https://github.com/DPDK/dpdk/commit/3be1df02fb09db123b9372e1fec6b4d741ae53d9)
- Complete the missing VF support definitions and code paths for E610 devices, add ACI capability definitions, VF device and functional capability analysis, and SRIOV capability support. (Architecture-related: VF/SRIOV support)
  ↳ No PR: [93a3916](https://github.com/DPDK/dpdk/commit/93a3916617cc478bc19db3a4e84c54fb2c19775f), [0d56299](https://github.com/DPDK/dpdk/commit/0d56299c3b6f13367a381838b358332a4481b275)
- The ixgbe driver adds support for new variants of the E610 series, adding subdevice ID macro, PCI device ID and VF MAC type detection to correctly identify and initialize the device; at the same time, the thermal sensor operation of the E610 is disabled. (Architecture-related: platform compatibility)
  ↳ No PR: [659e367](https://github.com/DPDK/dpdk/commit/659e36767e77b31088dc1f543ecba94562ecf08f), [2a18945](https://github.com/DPDK/dpdk/commit/2a18945801bf6b523af0596454257581f3c7a992), [5662e97](https://github.com/DPDK/dpdk/commit/5662e97457eb1133ec17f6b6060b97cc9b66da41), [d4a87e5](https://github.com/DPDK/dpdk/commit/d4a87e512efa6b2e031435e687a7bf2cdd489bba)
- Add XXV710 N3000 device ID (0x0D58) to the i40e driver to identify it as a 25G device. (Architecture-related: platform compatibility)
  ↳ No PR: [ef8d118](https://github.com/DPDK/dpdk/commit/ef8d118ad5fc38db0fa035bc1eb256843ac7abeb)
- Added API for reading LED flashing settings. (Architecture-related: public API)
  ↳ No PR: [dcf9ce7](https://github.com/DPDK/dpdk/commit/dcf9ce7d0ef28f0f58adb1a8df7617dda8a41bf8)
- Added a function that supports custom timeout for NVM acquisition operation to solve the problem of adapter being disabled for a long time due to lock during NVM update; at the same time, the definition of the 5th free supply area pointer in Shadow RAM was added to the i40e driver base layer. (Architecture-related: public API)
  ↳ No PR: [d980a40](https://github.com/DPDK/dpdk/commit/d980a401b137a53170ce60dc94059720d9999c43), [c7cb270](https://github.com/DPDK/dpdk/commit/c7cb270a6e66f2a2e619d8641122de8b7c66693e)
- Supports different configurations of BAR sizes, dynamically sets BAR size according to firmware version class, and adds version class validity check. (Architecture-related: configuration behavior)
  ↳ No PR: [19bd7cc](https://github.com/DPDK/dpdk/commit/19bd7cce5705e14f59aeb7bc28dddd9c8cab913f)
- Supports obtaining the limit on the number of flow rules from firmware, dynamically allocating the flow position array, and adjusting the flow rule acquisition logic accordingly. (Architecture-related: public API)
  ↳ No PR: [66df893](https://github.com/DPDK/dpdk/commit/66df893f2fefc50fb6a53a0cfcaa8aed4461442b)
- Add CN20K platform support to common/cnxk driver, including model detection, PF/VF bit encoding, mailbox communication and mailbox register configuration. (Architecture-related: platform compatibility)
  ↳ No PR: [966f57a](https://github.com/DPDK/dpdk/commit/966f57a6232ea2efd83cb3d12053390384f645b9), [61deac7](https://github.com/DPDK/dpdk/commit/61deac72abbff3924dd06937887ad399a3a42863), [7816df7](https://github.com/DPDK/dpdk/commit/7816df7911736f7f880db04fa62cdbd20405a63c), [9bd368c](https://github.com/DPDK/dpdk/commit/9bd368ca311a1ede6c17bb9e39d0e30f6a9abb2d)
- Added multiple PMD APIs for cnxk encryption devices, including CPTR acquisition, refresh, read and write and queue pair statistics functions, and improved type safety. (Architecture-related: public API)
  ↳ No PR: [21653af](https://github.com/DPDK/dpdk/commit/21653af489e7c695c7ddccb317f9957f93409597), [e5abbee](https://github.com/DPDK/dpdk/commit/e5abbeeeefa5760f8516e260f739b1b3dd45bb17), [3ca6074](https://github.com/DPDK/dpdk/commit/3ca607402c4d6b03c0deebc11d087334f31a2736), [0b7f67d](https://github.com/DPDK/dpdk/commit/0b7f67de81ecfab8a4d53c4e131b79e02a923abb), [bf52722](https://github.com/DPDK/dpdk/commit/bf52722b937738f50ada730bead83fb4fc43a1e2)
- Expand the virtchnl interface in the IAVF public driver, and add support for virtual channel commands for PTP, SyncE, GNSS and HQOS management. (Architecture-related: public API)
  ↳ No PR: [286e99f](https://github.com/DPDK/dpdk/commit/286e99f3a802381c14f19d35420c4eea03ffb4af), [886cc4b](https://github.com/DPDK/dpdk/commit/886cc4b8696db2daf00189546486bd0b13674145), [7025057](https://github.com/DPDK/dpdk/commit/7025057186d3ea52809b724305326882d0ea86de), [d00846d](https://github.com/DPDK/dpdk/commit/d00846d9419e62abefb31195255ee320f9f644c8)
- Added RefSync support, QGRPS and FLOW_STEER_TO_QGRP offloading capability definitions, and RSS hash function configuration functions in virtchnl.h, extending the public API and configuration options of the iavf driver. (Architecture-related: public API)
  ↳ No PR: [a26c659](https://github.com/DPDK/dpdk/commit/a26c6596be6c58da8fbd73d8615e3edc02e5c04b), [0016b69](https://github.com/DPDK/dpdk/commit/0016b690b5c836a4e6f963944ff5dc194ec3da72), [2381def](https://github.com/DPDK/dpdk/commit/2381def42646b861a5da9d27b9a4917607cc51bc)
- Add a priority field in the encryption device queue pair configuration and define the priority range from the highest to the lowest; the encryption performance test application adds the --low-prio-qp-mask option to support setting a low-priority queue. (Architecture-related: public API)
  ↳ No PR: [6ef8e70](https://github.com/DPDK/dpdk/commit/6ef8e70ecfbd0963a35a301bc9d6d0745891f6e3), [e004aaa](https://github.com/DPDK/dpdk/commit/e004aaa83a4afcc9e27b19ad2340a84fdc90f267)
- Added index matching mode of flow table rules, asynchronous creation API and jump to flow table index action, expanded the ethdev flow rule function. (Architecture-related: public API)
  ↳ No PR: [29e7c62](https://github.com/DPDK/dpdk/commit/29e7c6263926351be4d402559a49ff346e1bcc42), [933f18d](https://github.com/DPDK/dpdk/commit/933f18db7951206822c1343c6f5aa5e826700412), [2c52a2b](https://github.com/DPDK/dpdk/commit/2c52a2b3eca9b619b7ab16e4e936e52f8aa3b3d3)
- Added link speed channel acquisition, capability query and setting API, and implemented support in Broadcom Thor2 network card driver; testpmd added corresponding display and configuration commands. (Architecture-related: public API)
  ↳ No PR: [60bac72](https://github.com/DPDK/dpdk/commit/60bac72264d8dcec55d58919e4710a70968ae4a8), [dc6810a](https://github.com/DPDK/dpdk/commit/dc6810a2ab7b4a7c5fc45cb3e82362178a190821)
- Added bbdev queue debugging dump function, providing API to output detailed status information of the specified queue, and supporting PMD level operations to print more low-level information; the bbdev-test application has integrated this function. (Architecture-related: public API)
  ↳ No PR: [353e363](https://github.com/DPDK/dpdk/commit/353e3639d458f5cdaf3d938aade25579fa490b1b), [067fae4](https://github.com/DPDK/dpdk/commit/067fae411cfe5c966f5122afad4b766fa3159cc1)
- Support reporting register names and filtering by module, new rte_eth_dev_get_reg_info_ext API, and implemented in hns3 driver; also adjusted the register dump function. (Architecture-related: public API)
  ↳ No PR: [083db2e](https://github.com/DPDK/dpdk/commit/083db2ed9e9ea321f37fb49a9ea118446c04a782), [dd4b8bb](https://github.com/DPDK/dpdk/commit/dd4b8bba785faf9d1bb9c4460e75068e2822bdb3), [99d3bd8](https://github.com/DPDK/dpdk/commit/99d3bd8b85d357c8d4e7ee23765a073f4970ff74), [7fddd3c](https://github.com/DPDK/dpdk/commit/7fddd3cac6a3730fc016480418ce693b4a491cb5)
- Added telemetry command to ethdev to support dumping registers of specified modules; also fixed race conditions caused by concurrent addition/removal of ports. (Architecture-related: telemetry interface)
  ↳ No PR: [d916d27](https://github.com/DPDK/dpdk/commit/d916d27e3dca9d2e19e411fff9208929a7c7cbdf), [6f96937](https://github.com/DPDK/dpdk/commit/6f96937dada54d5cfc8def0955b0807759b45ac4), [8cdddc2](https://github.com/DPDK/dpdk/commit/8cdddc252dd5320bbbb1df948bbdd8d19f8fda22)
- Add anonymous unions in node context, support direct storage of opaque pointers, and adjust structure layout to maintain ABI/API compatibility. (Architecture-related: ABI/API compatibility)
  ↳ No PR: [28f0225](https://github.com/DPDK/dpdk/commit/28f0225a9c30c6ba168c83abf23fbee9c54f562e)
- Added PMD API to CNXK platform, supports submitting CPT instructions to Inline Device, and adds flow control inspection mechanism. (Architecture-related: public API)
  ↳ No PR: [de8c60d](https://github.com/DPDK/dpdk/commit/de8c60d113f0f688623f5a93b991f8b0e5dbf5f0)
- Add custom_inb_sa device parameter for CNXK network card, support application to use custom inbound SA and directly process inline IPsec inbound packets, and add RTE PMD API for configuring inline inbound parameters. (Architecture-related: public API)
  ↳ No PR: [03b1523](https://github.com/DPDK/dpdk/commit/03b152389fb15f96e25d9acd87b84c9c22cf8b2b)
- Added PMD API to obtain hardware model string. (Architecture-related: public API)
  ↳ No PR: [92fa0ac](https://github.com/DPDK/dpdk/commit/92fa0ac7eda65aa0b3c1fd9f8611fe9b297a6e01)
- Add port buffer manager (BMI) statistics functionality to the DPAA bus, including enable, disable, get and reset interfaces, and extend xstats to include BMI statistics. (Architecture-related: public API)
  ↳ No PR: [d2536b0](https://github.com/DPDK/dpdk/commit/d2536b006d788039112f9646e4fb2a91ecb6ae45)
- Support TX confirmation queue to enable PTP, and control IEEE1588 function through devargs parameter. (Architecture-related: device parameters)
  ↳ No PR: [58e0420](https://github.com/DPDK/dpdk/commit/58e0420f72f89cb022657253cd1b75d9bc47e5a7)
- Separate the Tx confirmation queue for the DPAA network driver, support VSP scenarios, and repair the VSP initialization logic to uniformly handle 1G and 10G ports. (Architecture-related: public API)
  ↳ No PR: [d11482d](https://github.com/DPDK/dpdk/commit/d11482d91b23e2ff2be36a6a0b6b026c5d0bf04e), [2543483](https://github.com/DPDK/dpdk/commit/25434831ca958583fb79e1e8b06e83274c68fc93)
- Add offline (OH) port mode support to the DPAA bus driver, allowing the hardware port not to connect to the actual MAC, and realize inter-application IPC communication through the QMan queue. (Architecture-related: public API)
  ↳ No PR: [a0edbb8](https://github.com/DPDK/dpdk/commit/a0edbb8a8e521e0720d31fd910bd9dce41874d9c)
- Added ONIC port mode to the OH port of dpaa-eth to support two applications on the same SoC communicating with each other through dpaa-eth. (Architecture-related: public API)
  ↳ No PR: [7e5f49a](https://github.com/DPDK/dpdk/commit/7e5f49ae767da93486d28142ef53a8fd745f240b)
- Add a dedicated NPA AQ enq mailbox for the CN20K platform, and select and use the new mailbox according to the platform type during NPA initialization, configuration and cleanup operations to handle bit width changes and NDC synchronization differences. (Architecture-related: platform compatibility)
  ↳ No PR: [143a419](https://github.com/DPDK/dpdk/commit/143a419edf35f3dc093b4f8f7a29163f9c075316)
- Add NIX register definitions for the CN20K platform, modify the nix_get_blkaddr function to support new platform address acquisition, and add debug dump support for NIX queue structures. (Architecture-related: platform compatibility)
  ↳ No PR: [9a01217](https://github.com/DPDK/dpdk/commit/9a01217e287197cfc2ac778edcec18d84056d244), [db5744d](https://github.com/DPDK/dpdk/commit/db5744d3cd23c485c506bc2a35e91132b1eb9ed0)
- Introducing a stateless packet preparation API for IPsec processing, supporting outbound processing without updating the IPsec session internal state, and allowing users to provide sequence numbers. (Architecture-related: public API)
  ↳ No PR: [aae98b8](https://github.com/DPDK/dpdk/commit/aae98b8c6690ccc49d7a1536a1b1ee1264de49a7)
- Added EdDSA asymmetric algorithm support, including API definition, OpenSSL PMD and CNXK encryption device driver implementation. (Architecture-related: public API)
  ↳ No PR: [8bd4315](https://github.com/DPDK/dpdk/commit/8bd4315ceba8d9de9dedafdaa963ffecc09cc971), [5a74d7f](https://github.com/DPDK/dpdk/commit/5a74d7fd37debc1b4fa1fa44b82fa9cf3b87a291), [a8ebe94](https://github.com/DPDK/dpdk/commit/a8ebe94f8cc11cda874cd0353a47e78279699d10), [2cf2f84](https://github.com/DPDK/dpdk/commit/2cf2f84442e80ff382b05dfd0db62bd969422da4), [12ede9a](https://github.com/DPDK/dpdk/commit/12ede9ac497fed989a1f4d0357e839cbe7d1e45b), [2fba523](https://github.com/DPDK/dpdk/commit/2fba5232e77ea72993d282c170bb7be0a48b8110), [981a1ed](https://github.com/DPDK/dpdk/commit/981a1ed32a7920bf0f5e2864ab1f78c296bdfaec)
- Introduced kvargs processing API that supports key parameters only, and applied in sfc and TAP drivers. (Architecture-related: public API)
  ↳ No PR: [f33e8c0](https://github.com/DPDK/dpdk/commit/f33e8c0e4a80c1456987f96c1ce448d65e7d6dfb), [4ed3061](https://github.com/DPDK/dpdk/commit/4ed306131f85ef180589169b868f292d9149b0c7), [3977d07](https://github.com/DPDK/dpdk/commit/3977d07df186e6f4c79802db19451f51703a3d60), [93afd6c](https://github.com/DPDK/dpdk/commit/93afd6caefb7f575ed607283dcfe217bbb097294), [a79d5ce](https://github.com/DPDK/dpdk/commit/a79d5ce97b578cdc981445519f6a34c6c06f323b), [ce7e937](https://github.com/DPDK/dpdk/commit/ce7e937f1aae7aecca5de5ffa4c051103020ca5e), [7dd7102](https://github.com/DPDK/dpdk/commit/7dd71026216ec94436c69d91ac812c70f5a7712d), [a04d13a](https://github.com/DPDK/dpdk/commit/a04d13aa619d1cefb9e2ab67faf8cd326a781cc9), [c189450](https://github.com/DPDK/dpdk/commit/c189450b37639bd8b7535e527fc424706db71e0d), [0e95a67](https://github.com/DPDK/dpdk/commit/0e95a6777fe3e99b5cd5747a84e6df4aa85c4ec4)
- Added a new node query API for the ethdev traffic manager, and added corresponding commands in testpmd. (Architecture-related: public API)
  ↳ No PR: [25a2a0d](https://github.com/DPDK/dpdk/commit/25a2a0dc3de31ca0a6fbc9371cf3dd85dfd74b07)
- Added configuration option to disable trace at compile time and runtime detection function rte_trace_feature_is_enabled. (architecture-related: public API)
  ↳ No PR: [e7bc451](https://github.com/DPDK/dpdk/commit/e7bc451c996b5882c5d8267725f3d88118009c75)
- Added an internal API to rawdev PMD to support obtaining the raw device structure pointer through the device ID. (Architecture-related: public API)
  ↳ No PR: [3ee7a3e](https://github.com/DPDK/dpdk/commit/3ee7a3e0e0e0f5a81a4b102a834697bc488fb32f)
- Add asymmetric operation capability checking function for cryptodev, and update SM2 test cases. (Architecture-related: public API)
  ↳ No PR: [53c65a3](https://github.com/DPDK/dpdk/commit/53c65a3ce2c6b56cf3fa71621a74b97c41432fc0)
- Add PTP clock frequency adjustment API for Ethernet devices and ice drivers, and integrate PI servo controller in the ptpclient example. (Architecture-related: PTP clock frequency adjustment API)
  ↳ No PR: [be86a68](https://github.com/DPDK/dpdk/commit/be86a6823f5ae08efbdc11297425fa844508a15d), [c37d505](https://github.com/DPDK/dpdk/commit/c37d50533798987027b89033ac31dac449ccca15), [6d55af6](https://github.com/DPDK/dpdk/commit/6d55af611fd51e1e7676ccad620f64cc06ea3ed7)
- Introduce on-demand recovery configuration mechanism: add get_restore_flags driver callback, modify rte_eth_dev_start behavior, and provide implementation for mlx5 driver. (Architecture-related: driver callback interface)
  ↳ No PR: [5e46b17](https://github.com/DPDK/dpdk/commit/5e46b176d37787c5536d48b23fff8baf5d674c88), [e14ebec](https://github.com/DPDK/dpdk/commit/e14ebecf109ef8ffca62e173ad8147e928f54e9e), [6a3446c](https://github.com/DPDK/dpdk/commit/6a3446cf577b70edbb072be19c7466b006ee2aa2)
- Added burst capacity API to DPAA QDMA driver, optimized initialization process, and added scatter-gather replication support. (Architecture-related: public API)
  ↳ No PR: [1686d80](https://github.com/DPDK/dpdk/commit/1686d80952feaef77c66c5d8ba85d1b70721fc62)
- Add support for scatter-gather copy operation to DPAA DMA driver. (Architecture-related: public API)
  ↳ No PR: [a77261f](https://github.com/DPDK/dpdk/commit/a77261f61245cf1e1880bd1c40511de523618c9f)
- Add user-configurable hardware error checking options to the DPAA DMA driver, and enable corresponding error handling in the dequeue and initialization processes. (Architecture-related: public API)
  ↳ No PR: [a63c642](https://github.com/DPDK/dpdk/commit/a63c6426fdfd9233ba9c7d4503e52bff3732fe69)
- Add more ICMP types and codes based on RFC 792, and rename the macro prefix from RTE_IP_ICMP_ to RTE_ICMP_ to distinguish types from codes. (Architecture-related: public API)
  ↳ No PR: [87bde5a](https://github.com/DPDK/dpdk/commit/87bde5ae68732ba62b658411fffd6abce8c80553)
- Supports outer VLAN flow matching, enabled by runtime configuration fdir_tuple_config, inner tuple can be replaced to enable outer VLAN matching. (Architecture-related: public API)
  ↳ No PR: [a473284](https://github.com/DPDK/dpdk/commit/a47328471c9a297dbe6caddf9db867cddc902f6d)
- Added IPv6 address structure and related tool functions, including multicast scope, link local address, request node address and Ethernet multicast address translation, and IPv6 version number checking function, and added corresponding unit tests. (Architecture-related: public API)
  ↳ No PR: [ca786de](https://github.com/DPDK/dpdk/commit/ca786def84caa9c4f1f36f516477e9a5f58389b5), [3d6d85f](https://github.com/DPDK/dpdk/commit/3d6d85f58c1cb88e3906dd3318f232a58be2e10e), [189fdd3](https://github.com/DPDK/dpdk/commit/189fdd3762758486aec347ebdeb9f5bfe74b5600)
- Add PTP single-step timestamp support and endpoint name acquisition API to the DPAA2 network driver, and optimize the creation of the scatter-gather memory pool. (Architecture-related: public API)
  ↳ No PR: [748b998](https://github.com/DPDK/dpdk/commit/748b998046355329c5cb4abc99293c5d925de146), [2013e30](https://github.com/DPDK/dpdk/commit/2013e3080894eab440c8fbe5a39fe00ca81066d1)
- Added DPDMUX counter dump function to identify the reason for packet discarding; at the same time, the stream creation interface was restructured and the return value was changed from a structure pointer to an integer. (Architecture-related: public API)
  ↳ No PR: [17eda10](https://github.com/DPDK/dpdk/commit/17eda10df93e1db1344819c19832533d777e48d1)
- Added DPDMUX method support based on C-VLAN and MAC address to the dpaa2 driver, and added device shutdown and counter dump functions. (Architecture-related: public API)
  ↳ No PR: [cfe9677](https://github.com/DPDK/dpdk/commit/cfe96771186470ad71d6b0ac9bbadfb1057cd572), [e6bf325](https://github.com/DPDK/dpdk/commit/e6bf3256b95c77ee4d0b2874e1896d01c41c2d7c)
- Added a new API for the DPAA2 network device driver to check whether the port belongs to the DPAA2 platform. (Architecture-related: public API)
  ↳ No PR: [72cd5a4](https://github.com/DPDK/dpdk/commit/72cd5a480180457369d1cd369da664c4ebc7cad7)
- Reconstruct the DPAA2 network card flow engine, introduce the key_profile structure, and add support for VXLAN, ECPRI, GTP, IPsec AH/ESP and other protocol flow matching. (Architecture-related: public API)
  ↳ No PR: [56c1817](https://github.com/DPDK/dpdk/commit/56c1817d532e0203e85cdce97068dd19deee0e51), [39c8044](https://github.com/DPDK/dpdk/commit/39c8044ffb7bb6956573fc63312e3f93170ce57b), [9ec2934](https://github.com/DPDK/dpdk/commit/9ec293434e90e95cdbbc4b9fff5370e250e1af20), [a8a6b82](https://github.com/DPDK/dpdk/commit/a8a6b82e80ef3f96ca3370a98c67ae09df940886), [146c745](https://github.com/DPDK/dpdk/commit/146c745e308825bdd4280f17506a3ff92eb9c0a2), [4cc5cf4](https://github.com/DPDK/dpdk/commit/4cc5cf4a291d79efe6fd0ffcc9dbdd25549c654a)
- Enhanced RAW stream extraction function, supports the combination of RAW extraction and header extraction, and allows starting from any absolute offset. (Architecture-related: public API)
  ↳ No PR: [e21bff6](https://github.com/DPDK/dpdk/commit/e21bff64e25667bddb8889e2d34fc7226e21e057)
- Added rte_flow_async_create_by_index_with_pattern function, and supports jump to flow table index action, realizing the creation, verification, construction and resource management of hardware steering jump to matcher action. (Architecture-related: public API)
  ↳ No PR: [36c379c](https://github.com/DPDK/dpdk/commit/36c379c82e82bb7a60d17a2bb654988df0ea82ae), [af154d7](https://github.com/DPDK/dpdk/commit/af154d7a00441b54ea1439cbcd4b2d0e9fc0626a), [be5ded2](https://github.com/DPDK/dpdk/commit/be5ded2f96072e887d5155516f8bbe69d1fb07ad)
- Added an API to obtain the endpoint name for the DPAA2 network device, and exported the interface in the public header file. (Architecture-related: public API)
  ↳ No PR: [a0f8ddc](https://github.com/DPDK/dpdk/commit/a0f8ddc41218687134b33f6a462ff0b7eb04df65)
- Supports the extraction of multiple flow rules, adds hardware descriptions of IP fragmentation frames, and reconstructs the flow rule creation interface. (Architecture-related: public API)
  ↳ No PR: [25e5845](https://github.com/DPDK/dpdk/commit/25e5845b5272764d8c2cbf64a9fc5989b34a932c)
- Add RSS action support for streams on single-queue port delegates, enabling multi-queue delegate applications to take advantage of RSS functionality. (Architecture-related: public API)
  ↳ No PR: [0981a22](https://github.com/DPDK/dpdk/commit/0981a22ec3359793e7515decb07adc5a13d772c0)
- Add support for DiffServ, ECN and replication DF/DSCP, decrement TTL and other options in IPsec tunnel mode for DPAA_SEC encryption device. (Architecture-related: public API)
  ↳ No PR: [c253236](https://github.com/DPDK/dpdk/commit/c253236a38843dc4ee2126a397398e8c3a12e9ca)
- Added rte_ipv4_cksum_simple function to simplify IPv4 header checksum calculation and replace duplicate implementations in multiple applications. (Architecture-related: public API)
  ↳ No PR: [f9e1d67](https://github.com/DPDK/dpdk/commit/f9e1d67f237a00cf94feb4413e3d978fdd632052)
- Added roc_npa_pf_func_get API, used to obtain NPA PF functions for use by external drivers. (Architecture-related: public API)
  ↳ No PR: [59c1594](https://github.com/DPDK/dpdk/commit/59c15941bf34887cf75e6286524efa2a5691bfdc)
- Add scheduler topology loading to the ice network card driver, enhance the flexibility of the Tx scheduler hierarchy, and add a new devarg parameter that limits the number of visible layers of the TM scheduler. (Architecture-related: scheduler topology and devarg parameters)
  ↳ No PR: [2a77f64](https://github.com/DPDK/dpdk/commit/2a77f6496fe38dc2f66110d8c0bdf189ef6f0c1c), [715d449](https://github.com/DPDK/dpdk/commit/715d449a965b104ce95af83211766309e92f33d7), [4ace770](https://github.com/DPDK/dpdk/commit/4ace7701eb443d5dea965ea70fc192c900cbdff9), [bd6bbe6](https://github.com/DPDK/dpdk/commit/bd6bbe6db3585d0cb40cebb945a6444f95b4cb88), [824e68d](https://github.com/DPDK/dpdk/commit/824e68d4c060cc8c491e6134e764c285fa62126f)
- Add flow rule priority support to the hns3 network card driver, and select the index strategy (hash or priority) through the runtime configuration fdir_index_config. (Architecture-related: flow rule priority configuration)
  ↳ No PR: [ac72aae](https://github.com/DPDK/dpdk/commit/ac72aae60f71b8716f65d1e2daf531a5ca38c998)
- Add register definitions and registrations for TX Copy, Tx INS and Tx RPL modules to the ntnic driver. (Architecture-related: public header file register definitions)
  ↳ No PR: [ea5653c](https://github.com/DPDK/dpdk/commit/ea5653cfb89e97e299a55442de795c972e63a1dd), [3a747e9](https://github.com/DPDK/dpdk/commit/3a747e96c4fed9be947a14f89b85358e62f75cbd), [0214ba6](https://github.com/DPDK/dpdk/commit/0214ba672b2559102f141587b33cd43fe1d6a1c3)
- Add tf-core (TruFlow) support for Thor2 chip to bnxt driver, add session management, table range management, hardware resource allocation and other APIs and HWRM message processing. (Architecture-related: Thor2 chip support)
  ↳ No PR: [80317ff](https://github.com/DPDK/dpdk/commit/80317ff6adfde7f618a100098e068ad5512e8e22), [2c03331](https://github.com/DPDK/dpdk/commit/2c033311ec730dfbe519e059c0c53373e5133e8a)
- Add VXLAN-GPE tunnel support at the ULP layer, and update the template infrastructure. (Architecture-related: VXLAN-GPE tunnel support)
  ↳ No PR: [74cab00](https://github.com/DPDK/dpdk/commit/74cab005e74976adbc800ab514291bb4c02d11f2)
- Add hooks in hwrm and ulp layers to support custom L2 etype tunnels, including allocation, release and acquisition of tunnel ports and UPAR ID processing. (Architecture-related: custom L2 etype tunnel support)
  ↳ No PR: [5c275d6](https://github.com/DPDK/dpdk/commit/5c275d61e19b08740c50f99258e6e4088bf1b663)
- Added VF to VF stream offloading support for Whitney Platform, changing pipelines from using VLAN tags to using custom L2 encapsulation and decapsulation. (Architecture-related: Whitney Platform VF stream offloading)
  ↳ No PR: [032d49e](https://github.com/DPDK/dpdk/commit/032d49ef310179bc0bd165dde4c018884bc5a3e2)
- Add Thor2 ULP layer support to the bnxt network driver, including ULP initialization, MPC memory access, VF support, inter-VF traffic offloading, Geneve header parsing, set TTL action, MPC batch processing and other functions, and update related template files. (Architecture-related: Added Thor2 platform support)
  ↳ No PR: [dd0191d](https://github.com/DPDK/dpdk/commit/dd0191d5e70d0e65a7f041a88af480fc673160e1)
- Add feature bit support for the ingress flow, which is used to set the default destination MAC when the destination MAC address is not specified; also add function operand size support, and update the template file. (Architecture-related: Behavior change: Default destination MAC)
  ↳ No PR: [32bdbf4](https://github.com/DPDK/dpdk/commit/32bdbf441469b4ade6f34037afae02b159d56b8c)
- Update VFR code to support Thor 2: Add endpoint identifier (efid) to session, modify common table to write L2 context ID, and allow releasing rfid and efid simultaneously from AFM. (Architecture-related: Added Thor2 VFR support)
  ↳ No PR: [be4732e](https://github.com/DPDK/dpdk/commit/be4732e8bc48dff2050500825a0d1d601ec68d4b)
- Support for dynamic tunnel UDP ports, allowing configuration of tunnel UDP destination ports based on flow runtime; also fixes context access segfault, sets default VxLAN tunnel port, and improves multi-flow support. (Architecture-related: Behavior change: Dynamic tunnel UDP ports)
  ↳ No PR: [94dbd6c](https://github.com/DPDK/dpdk/commit/94dbd6cf36688f36872b6878879442889baac997)
- Add metering support to Thor2, implement the Thor2 meter template table, make the rte_mtr API device-independent to adapt to hardware changes, and fix the rounding problem in xir calculation. (Architecture-related: public API)
  ↳ No PR: [80d760e](https://github.com/DPDK/dpdk/commit/80d760e129ae8bf928b3aa77800cd1bc5609d4b0)
- Added Rx rate profile selection function to bnxt network card driver, and set polling mode in Rx and AGG ring allocation when firmware supports it. (Architecture-related: public API)
  ↳ No PR: [57e571c](https://github.com/DPDK/dpdk/commit/57e571c19fe7d9dc02eec6c1ee6379fd393f21fb), [7a535f3](https://github.com/DPDK/dpdk/commit/7a535f301db655582fe44c26b908a40c9dc4983f)
- Add management channel support for SR-IOV VF to net/enic driver, through which VF communicates with PF to execute restricted devcmds, and supports soft Rx statistics and backward compatibility mode. (Architecture-related: backward compatibility mode)
  ↳ No PR: [00ce431](https://github.com/DPDK/dpdk/commit/00ce43111dc5b364722c882cdd37d3664d87b6cc)
- Add arm64 support to mana driver and supplement missing header files. (Architecture-related: platform compatibility)
  ↳ No PR: [7649794](https://github.com/DPDK/dpdk/commit/7649794dcfe9fff3e33f98a93dff65bd11ec3c42)
- Update Thor2 universal template, fix WC matching failure, L2 flow ethertype check, L3 protocol configuration error and non-default priority flow table entry allocation problem. (Architecture event: bnxt_ulp_template_db adds Thor2 template)
  ↳ No PR: [334f347](https://github.com/DPDK/dpdk/commit/334f34706e30d448db125007f98fc6926e842aae)
- Register and handle RSS change events, fix the bug of not clearing old flags in PMD QCAPS update. (Architecture-related: public API)
  ↳ No PR: [643e7ee](https://github.com/DPDK/dpdk/commit/643e7ee39879083ec8a9b86c2b60ca9f50182ed7)
- Fixed the use of incorrect control words and configuration functions during vDPA reconfiguration, using extended configuration functions and correct virtio control macros instead. (Architecture-related: public API)
  ↳ No PR: [d149827](https://github.com/DPDK/dpdk/commit/d149827203a61da4c8c9e4a13e07bb0260438124)
- Fixed the Rx/Tx descriptor limit reported in the mlx5 network card driver. The actual maximum number of descriptors is now set according to the hardware capabilities, and the upper limit is checked when setting the queue. (Architecture-related: public API)
  ↳ No PR: [4c3d796](https://github.com/DPDK/dpdk/commit/4c3d7961d9002bb715a8ee76bcf464d633316d4c)
- In the ice network card driver, when time synchronization is enabled, the PHC main timer is initialized to the current system time to avoid timestamp errors. (Architecture-related: time synchronization behavior)
  ↳ No PR: [faa310a](https://github.com/DPDK/dpdk/commit/faa310a75f66953dda22887345dc196f8aef28de)
- Fix PTP initialization for E825C devices, correct hardcoded values for clock source and frequency, and adjust sideband access to support second PHY and CGU devices. (Architecture-related: PTP initialization behavior)
  ↳ No PR: [3bb9d73](https://github.com/DPDK/dpdk/commit/3bb9d730d300b33c490289be4bcc5ed388c5d109)
- Fixed the X710TL device check in the i40e driver and completed the missing 1G network card device ID. (Architecture-related: public API)
  ↳ No PR: [597e19e](https://github.com/DPDK/dpdk/commit/597e19e7eae17beb820795c3a8a97c547870ba26)
- Fix the hardware semaphore timeout variable type and timeout judgment logic in the i40e driver to correctly handle 32-bit value wrapping. (Architecture-related: public API)
  ↳ No PR: [c61390d](https://github.com/DPDK/dpdk/commit/c61390d94d46b05b7cd97d34561cb0b360d4e89c)
- Make sure the CPTR pointer is 128 bytes aligned, otherwise an error will be returned. (Architecture-related: public API)
  ↳ No PR: [d53727d](https://github.com/DPDK/dpdk/commit/d53727d0a4244cdff51b6892483a5616f3bb730e)
- Fixed the problem of pcapng generating corrupted files when processing chained mbufs, and corrected EPB block length calculation. (Architecture-related: pcapng file generation behavior)
  ↳ No PR: [6db3585](https://github.com/DPDK/dpdk/commit/6db358536fee7891b5cb670df94ec87543ddd0fb)
- Fixed the problem in event mode that caused inbound out-of-order processing to fail due to the reorganization flag not being updated, and added a new registration function for receiving uninstall callbacks. (Architecture-related: public API)
  ↳ No PR: [d524a55](https://github.com/DPDK/dpdk/commit/d524a5526efa6b4cc01d13d8d50785c08d9b6891)
- Adjust the aura field width for cn20k chips, and modify the bit offset in related register read and write operations. (Architecture-related: public API)
  ↳ No PR: [620fc02](https://github.com/DPDK/dpdk/commit/620fc02bf7ebfb9c8ca8d4a391df9e243397270c)
- Limit the rte_vhost_driver_set_max_queue_num API to only take effect on the VDUSE backend to avoid affecting Vhost-user live migration. (Architecture-related: public API)
  ↳ No PR: [e180899](https://github.com/DPDK/dpdk/commit/e1808999d36bb2e136a649f4651f36030aa468f1)
- Add a runtime check on whether the CPU supports the AVX512DQ and AVX512BW instruction sets in the AVX512 lookup function to ensure that vector functions are only used when the conditions are met. (Architecture-related: platform compatibility)
  ↳ No PR: [45ddc56](https://github.com/DPDK/dpdk/commit/45ddc5660f9830f3b7b39ddaf57af02e80d589a4)
- Integrate the RCU QSBR mechanism for the DIR24-8 algorithm to prevent the tbl8 group from being released while the reader is still in use, thereby preventing lookup errors. (Architecture-related: public API)
  ↳ No PR: [96c3d06](https://github.com/DPDK/dpdk/commit/96c3d06a354753cdef9177e0c204c2e9361f31d5)
- Fixed the spelling error in the VLAN flow matching mode macro definition in the hns3 driver, and added the parameter in the driver parameter registration string. (Architecture-related: driver parameter configuration)
  ↳ No PR: [bf16032](https://github.com/DPDK/dpdk/commit/bf16032eb1e62338e02b1278e10033366448c5bc)
- Add verification support for malformed Rx descriptor errors to the ENA network card driver, improve reset logic and statistical tracking. (Architecture-related: public API)
  ↳ No PR: [7a16699](https://github.com/DPDK/dpdk/commit/7a166990faa46a470f16e7c96404c9288f2e1a86)
- Before sending commands to MC, convert VA to IOVA and check its validity to prevent invalid IOVA from causing the system to hang. (Architecture-related: core module behavior)
  ↳ No PR: [25d0ae6](https://github.com/DPDK/dpdk/commit/25d0ae6242453c3e482d752495d5a30f3ada11dd)
- Improved DPDMUX error behavior settings to make it compatible with MC v10.36 and higher. (Architecture-related: MC version compatibility)
  ↳ No PR: [00e928e](https://github.com/DPDK/dpdk/commit/00e928e9704c3794062b46c1c30352281e4f9cb8)
- Fix the array index overflow problem caused by type conversion in IPv6 address comparison and masking functions, and avoid potential security risks by modifying variable types and constants. (Architecture-related: public API)
  ↳ No PR: [b805c83](https://github.com/DPDK/dpdk/commit/b805c834c776c67fb52d2b84c74258c5323a7872)
- Fixed the array out-of-bounds reading problem caused by memset in the rte_ipv6_addr_mask function, and instead used a loop to clear the remaining bytes. (Architecture-related: public API)
  ↳ No PR: [1d9c6bb](https://github.com/DPDK/dpdk/commit/1d9c6bbeb6cd8d0e3b7d54c7732199524020ea23)
- Fix the problem that some symbols in the ethdev header file are not included in the extern "C" block, causing C++ link failure, and adjust the tracing call of rte_eth_rx_burst to distinguish between null and non-null reception. (Architecture-related: public API)
  ↳ No PR: [20387eb](https://github.com/DPDK/dpdk/commit/20387ebce20ac5bc2e4e26bd008129a6c2cad9cc)
- Remove support for ROH devices and roll back the addition of related devices. (Architecture-related: public API)
  ↳ No PR: [feb4548](https://github.com/DPDK/dpdk/commit/feb4548ffd80bf249239d99bf9053ecf78f815d1)
- Fix the error handling problem of 128-byte CQE in the mlx5 driver, unify the error CQE structure into mlx5_error_cqe and correct the related size calculation. (Architecture-related: public API)
  ↳ No PR: [3cddeba](https://github.com/DPDK/dpdk/commit/3cddeba0ca38b00c7dc646277484d08a4cb2d862)
- Fixed the bit definition error of VF-PF mailbox interrupt in txgbe driver to ensure that the interrupt can be processed correctly. (Architecture-related: public API)
  ↳ No PR: [5a4ce69](https://github.com/DPDK/dpdk/commit/5a4ce69701fc01f23a2769c8afff055d87eff864)
- Add Tx descriptor error statistics function to the txgbe network card driver to count the number of unsent packets due to descriptor errors. (Architecture-related: public API: Tx descriptor error statistics)
  ↳ No PR: [e028ec1](https://github.com/DPDK/dpdk/commit/e028ec1b84c64891932d1b79c46d1ed41be1f77d)
- Fixed the compilation warning caused by the structure misalignment of the IPv4 checksum simple function, by aligning the rte_ipv4_hdr structure to 2 bytes and adjusting the pointer conversion method. (Architecture-related: public API)
  ↳ No PR: [c14fba6](https://github.com/DPDK/dpdk/commit/c14fba68edfa4aeba7c0dfb5dbc3b4f23affbb81)
- Add a 2-byte alignment attribute to the IPv6 header structure to reflect its actual alignment requirements. (Architecture-related: public API)
  ↳ No PR: [365b7f3](https://github.com/DPDK/dpdk/commit/365b7f341ca633743d44c365eccff7ae729d37c2)
- This submission contains multiple fixes and feature enhancements, covering template compiler modifications, VxLAN-GPE support, single-port card default parif processing, hot upgrade API, custom VxLAN stream support, asynchronous event synchronization, log level adjustment, memory release fix, null pointer check, crash fix and VF representative support, etc. (Architecture-related: public API)
  ↳ No PR: [2921498](https://github.com/DPDK/dpdk/commit/2921498c88ba84f9b0cb69b9a2cfb02ec2e41a0f)
- Fixed the problem of using the default mask when no mask is specified in protocol header parsing, updated the flow database to support 64-bit handles and more resource types, and fixed shared session statistics and template rejection logic. (Architecture-related: 64-bit handle support)
  ↳ No PR: [f6e1201](https://github.com/DPDK/dpdk/commit/f6e1201540603ced7cbaf8c883b03d859df62923)
- Removed experimental flags from several inline functions of the bbdev library. (Architecture-related: public API)
  ↳ No PR: [909a133](https://github.com/DPDK/dpdk/commit/909a13331668883b5f997773123d2a34ad5e079d)
- Change the timeout parameter type of the i40e_aq_request_resource function from 64 bits to 32 bits. (Architecture-related: public API)
  ↳ No PR: [cb593a8](https://github.com/DPDK/dpdk/commit/cb593a832630a81403a9fc3e3de0bd06742e4bbb)
- Rearrange structure fields to eliminate memory holes. (Architecture-related: ABI compatibility)
  ↳ No PR: [1c3f756](https://github.com/DPDK/dpdk/commit/1c3f7561503734cb62616324d524ddb6e22e6044)
- Change the behavior when CTX flush fails from calling abort() to returning an error code. (Architecture-related: error handling behavior)
  ↳ No PR: [e781595](https://github.com/DPDK/dpdk/commit/e78159500d56015064c11f04c43ed2e25c02b5c1)
- Add __rte_warn_unused_result attribute to multiple query functions in ethdev API. (Architecture-related: public API)
  ↳ No PR: [1ff8b9a](https://github.com/DPDK/dpdk/commit/1ff8b9a6ef248dddebd07a8df7b47f4de9ffab62)
- Update the RSA transformation structure, changing the private exponent and quintuple from union to structure. (Architecture-related: public API)
  ↳ No PR: [0e3b2fc](https://github.com/DPDK/dpdk/commit/0e3b2fc18c6b9bae9c6d51779bcd2b057ba0e300)
- Moved RSA padding information from encryption operations into xform structures. (Architecture-related: public API)
  ↳ No PR: [8a97564](https://github.com/DPDK/dpdk/commit/8a97564b1c1e035daaa0cdda553edd46178889e2)
- Mark the node parameter pointer in the rte_tm_node_add function and its driver implementation as const. (architecture-related: public API)
  ↳ No PR: [5d49af6](https://github.com/DPDK/dpdk/commit/5d49af626c829c465d36dd482ae17abc347f1929)
- Declare the parameters of functions related to TM profile addition as const. (architecture-related: public API)
  ↳ No PR: [5d96356](https://github.com/DPDK/dpdk/commit/5d96356688da2f79a62a48025a017c77e90d6232)
- Mark the parameters of the TM shaper configuration file adding function as const. (architecture-related: public API)
  ↳ No PR: [3953323](https://github.com/DPDK/dpdk/commit/3953323852dfe399c0e6bdf2d35f88005b8a2135)
- Reconstruct FMC scheme and CC parsing for DPAA shared MAC scenarios, support RX queue allocation from VSP scheme and CC rules. (Architecture-related: public API)
  ↳ No PR: [9e97abf](https://github.com/DPDK/dpdk/commit/9e97abf23766e2853c7a9de86e158540538892ad)
- Reconstruct the queue memory management of VRB devices to handle queue configuration, DMA ring, tail pointer and software ring allocation and release respectively according to device variants. (Architecture-related: public API)
  ↳ No PR: [fc65d3d](https://github.com/DPDK/dpdk/commit/fc65d3dcabe01770aed9a6e9a57348526f69ca58)
- Removed unused enumeration end markers RTE_CRYPTO_ASYM_XFORM_TYPE_LIST_END and RTE_CRYPTO_RSA_PADDING_TYPE_LIST_END. (architecture-related: public API)
  ↳ No PR: [e17a4a8](https://github.com/DPDK/dpdk/commit/e17a4a880550278ad367109be54116b098c0627a)
- Cleaned up the parameter verification logic in the DMA device API, ensuring that the device pointer is used after verifying the dev_id parameter, and adding a new legitimacy check for parameters such as priority. (Architecture-related: public API)
  ↳ No PR: [2980a27](https://github.com/DPDK/dpdk/commit/2980a27ecfaf2ea3a990cfa38cc310221a1c9b97)
- Optimized the alignment of Ethernet headers and VLAN headers, removed unnecessary alignment and packaging attributes, and added compile-time assertions. (Architecture-related: public API)
  ↳ No PR: [e214d58](https://github.com/DPDK/dpdk/commit/e214d58eb87b8af488272f084220617ecabb510a)
- Refactor the DPAA2 qDMA driver to support multiple hardware queues, single copy and SG copy and silent mode, and introduce new internal functions to manage FLE/SDD/SG entries. (Architecture-related: public API)
  ↳ No PR: [07d679b](https://github.com/DPDK/dpdk/commit/07d679bceee383aa07f508cee4f61ba790030158)
- Reconstruct the DPAA DMA driver, update the hardware descriptor and queue structure, and use the rte_ring API to implement enqueue and dequeue operations. (Architecture-related: public API)
  ↳ No PR: [f1d30e2](https://github.com/DPDK/dpdk/commit/f1d30e2786b6c0f2cfd4a6bd2ccc5de5d51ae02c)
- Removed internal symbol rte_vdpa_relay_vring_used. from vDPA public header file (architecture-related: public API)
  ↳ No PR: [85dbfcb](https://github.com/DPDK/dpdk/commit/85dbfcb1be49e512fde5c7455f9872158421ca66)
- Renamed the IPv4 lookup configuration flag RTE_FIB_F_NETWORK_ORDER to RTE_FIB_F_LOOKUP_NETWORK_ORDER to make it clear that it is only used for lookup operations. (Architecture-related: public API)
  ↳ No PR: [df8b5bf](https://github.com/DPDK/dpdk/commit/df8b5bf744f9aa9a1fbb790dac14a32d9cc9f236)
- Split the tracking point that receives the callback into two versions, empty and non-empty, to avoid quickly filling up the tracking buffer. (Architecture-related: public API)
  ↳ No PR: [e075ca1](https://github.com/DPDK/dpdk/commit/e075ca1d2a22552a4ee6e2f2fa8d847b9e305c8e)
- Support short FD format to improve single transfer performance, and refactor related functions to identify FD types and save index context. (Schema related: public API)
  ↳ No PR: [388e888](https://github.com/DPDK/dpdk/commit/388e888dc082520f3dbe6318ae32fbf99695cf4c)
- Increase the maximum number of Rx/Tx descriptors in the ixgbe driver from 4096 to 8192 to support applications that require greater buffering capacity. (Architecture-related: public API)
  ↳ No PR: [9fd2193](https://github.com/DPDK/dpdk/commit/9fd2193e56a55c6509477f8d5751c18a388f3977)
- Unified the IPv6 address structure, replaced in6_addr with rte_ipv6_addr, and fixed compilation errors caused by structural changes. (Architecture-related: public API)
  ↳ No PR: [52e04a6](https://github.com/DPDK/dpdk/commit/52e04a6323319ff1a7b4e1d7ed1df2b45d11a0a4), [61938a2](https://github.com/DPDK/dpdk/commit/61938a2d178554a0605f8d7ec2e5b7eeaea20e43)
- Updated template files for Thor2 platform, added statistics caching support, and adjusted enumeration definitions, entries and condition lists. (Architecture event: bnxt Thor2 template update)
  ↳ No PR: [2d1f4d4](https://github.com/DPDK/dpdk/commit/2d1f4d49e2234671fb9d3884bc7fbd0a5567cb5e), [f76387a](https://github.com/DPDK/dpdk/commit/f76387ad8faa5df1ed2d6cd9631893c0b5855930), [25b38ed](https://github.com/DPDK/dpdk/commit/25b38ed0e73f9679225e2c3db9450ac6eca59d80)
- Updated the firmware API version of ixgbe driver to 1.7 to maintain compatibility with firmware. (Architecture-related: Firmware API version compatibility)
  ↳ No PR: [d725446](https://github.com/DPDK/dpdk/commit/d72544655ea05190f57e9100e1d533d6c7989a42)
- rte_vhost_driver_set_max_queue_num API has been upgraded from experimental to stable version. (Architecture-related: public API)
  ↳ No PR: [d8381a8](https://github.com/DPDK/dpdk/commit/d8381a8f54cdc789c4260efefb5a17b9612f417e)
- Added multi-segment message processing logic for Rx inject. (Architecture-related: Rx inject behavior)
  ↳ No PR: [62b5770](https://github.com/DPDK/dpdk/commit/62b577026d8b6a7059383bc4609d05ca7203f3a5)

### Event Dispatch Router
- Added Categorizer (CAT) FPGA module, which is used to select the behavior of other modules in the FPGA pipeline based on protocol inspection. (Architectural event: ntnic FPGA hardware abstraction layer change)
  ↳ No PR: [6e8b7f1](https://github.com/DPDK/dpdk/commit/6e8b7f11205f4956756c3c53868b55059e8f6609), [833962e](https://github.com/DPDK/dpdk/commit/833962ebb8935089336a0ede3efb1cd8fbb06eb3)
- Added Key Matcher (KM) FPGA module, supporting CAM-based exact matching and TCAM-based wildcard matching. (Architecture event: ntnic FPGA hardware abstraction layer change)
  ↳ No PR: [fbe2726](https://github.com/DPDK/dpdk/commit/fbe2726faa592b7ffee79b04083d9c2cc69c77f7), [9bd46cf](https://github.com/DPDK/dpdk/commit/9bd46cf2599ed080b3a64a6b9295b12f61eb553d)
- Added the Flow Matcher (FLM) FPGA module, which provides a high-performance stateful SDRAM search and programming engine, supporting precise match search and module present detection, allocation, release, reset, control and status management. (Architectural event: Added FLM FPGA module)
  ↳ No PR: [059dfc3](https://github.com/DPDK/dpdk/commit/059dfc39e94dd5482f3b07faee60ead36401a43b), [866d8d0](https://github.com/DPDK/dpdk/commit/866d8d06ad5dc4bcd49a08fc5c61ce4289505c79)
- Added HSH (Hasher) FPGA module, used to calculate configurable hash values, supporting Toeplitz and NT-hash hash algorithms. (Architectural event: Added HSH FPGA module)
  ↳ No PR: [afad5ac](https://github.com/DPDK/dpdk/commit/afad5ac406e3896ee8565f7e21da896d2320c427)
- Added Queue Selector (QSL) FPGA module, which is used to direct packets to host queues, physical ports, abnormal paths or discards. (Architecture event: Added QSL FPGA module)
  ↳ No PR: [0e474ae](https://github.com/DPDK/dpdk/commit/0e474ae51f2a6531b7410b24e80cf12d72a16582), [98e40f8](https://github.com/DPDK/dpdk/commit/98e40f83f49d1b37c33d59a196e20bd66c83cd81)
- Added Categorizer (CAT) flow module to select the behavior of other modules in the FPGA pipeline based on protocol inspection. (Architecture-related: New flow module)
  ↳ No PR: [636b2cf](https://github.com/DPDK/dpdk/commit/636b2cfe0259549bb8df98c30651c90355b679b7)
- Added Key Match (KM) flow module, supporting CAM-based exact matching and TCAM-based wildcard matching. (Architecture-related: New flow module)
  ↳ No PR: [3005c75](https://github.com/DPDK/dpdk/commit/3005c75d6b55c73eeb2c25406b7901bac5b54d6d)
- Added the Flow Matcher (FLM) flow module, which is a high-performance stateful SDRAM search and programming engine that supports line-speed accurate match search and can handle hundreds of millions of flows. (Architecture-related: New flow module)
  ↳ No PR: [cec43fa](https://github.com/DPDK/dpdk/commit/cec43fab911c9ff28cb2d00a72c306572f1d09e9), [deda5e0](https://github.com/DPDK/dpdk/commit/deda5e0f1c2f1718096319637a3042be7471eb7f)
- Added Hasher (HSH) hash module, which supports two configurable hash algorithms, Toeplitz and NT-hash, for calculating hash values internally in FPGA. (Architecture-related: New stream module)
  ↳ No PR: [a5a5d5b](https://github.com/DPDK/dpdk/commit/a5a5d5bb316a1b65c92bdc436462b9e24d051108), [7fa0bf2](https://github.com/DPDK/dpdk/commit/7fa0bf29e667c12dc32a8cfd6330a639adcf1358)
- Added queue selection (QSL) flow module, which is used to direct data packets to host queues, physical ports, abnormal paths or discard. (Architecture-related: new flow module)
  ↳ No PR: [b95f1cd](https://github.com/DPDK/dpdk/commit/b95f1cd053cee23862a0dfc613e95e86dfd5f3aa)
- Added Slicer for Local Retransmit (SLC LR) flow module, which supports truncating packet headers in the FPGA RX pipeline. (Architecture-related: New flow module)
  ↳ No PR: [8c54532](https://github.com/DPDK/dpdk/commit/8c545325ec2b7a6e787d6ca156cc0b2501c96cac)
- Clean up the obsolete external EM support in the bnxt driver, remove related functions; change TCAM entries from static allocation to dynamic allocation, use abstract entry ID; remove AFM allocation memory related code that is no longer supported; use the built-in TCAM manager of the driver uniformly, remove the selection logic based on rx/tx_tcam_supported. (Architecture-related: TCAM manager reconstruction)
  ↳ No PR: [aa49b38](https://github.com/DPDK/dpdk/commit/aa49b38fa7c350da251b70f455224ae8e3f79d0b), [580fcb3](https://github.com/DPDK/dpdk/commit/580fcb3d718069a8058f4395dd64d19fed0c1f65), [4545fdf](https://github.com/DPDK/dpdk/commit/4545fdf6a25f1d2d7c269eb46c200a5526028a5e), [5873bd3](https://github.com/DPDK/dpdk/commit/5873bd31dc8393b17fb7b45bd1f714c227dad3f5)
- Implement SSO hardware information acquisition mechanism, obtain hardware capabilities through mailbox and replace hard-coded values. (Architecture-related: hardware abstraction layer)
  ↳ No PR: [8252652](https://github.com/DPDK/dpdk/commit/82526521ca123dc67361905e0e6e96bf2fa2602c)
- Add flow API initialization and de-initialization support to the ntnic driver, including flow filters, high-level interface registration and acquisition of flow backend, and resource management functions. (Architecture event: ntnic flow API module change)
  ↳ No PR: [36cf85c](https://github.com/DPDK/dpdk/commit/36cf85c8997500c90cd1875bbe43190124660a12), [0e5e289](https://github.com/DPDK/dpdk/commit/0e5e289e4b15ae8032ddb819dce934ae3736a28d), [0ea00f3](https://github.com/DPDK/dpdk/commit/0ea00f33754b342d95623c9af81d827a06c31f58), [8df4a5f](https://github.com/DPDK/dpdk/commit/8df4a5f8b10fbc2124a346fd5f2d027ba5718117), [1d3f62a](https://github.com/DPDK/dpdk/commit/1d3f62a0c4f1f4e2e9ac26aaf840d3e050bc4d86), [7917b0d](https://github.com/DPDK/dpdk/commit/7917b0d38e92e8b9ec5a870415b791420e10f11a)
- Added complete virtual queue management functions to the ntnic driver, including availability monitoring, used writer data processing, descriptor reader, packed ring support, queue release and packet sending and receiving. (Architecture event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [01e34ed](https://github.com/DPDK/dpdk/commit/01e34ed9c756c0db67af45639dd1bba1040e8dd2), [67aee0a](https://github.com/DPDK/dpdk/commit/67aee0a69665496f9369f00619d0259c8f89b2fe), [f7b8816](https://github.com/DPDK/dpdk/commit/f7b881659406fcece705eef3fbc042a8e62d3400), [af30088](https://github.com/DPDK/dpdk/commit/af30088786c2eb65754b258ab8a66d2f212e5dba), [f0fe222](https://github.com/DPDK/dpdk/commit/f0fe222ea9cfe3c8a6972318d02a81a637aefd47), [9c2e6e7](https://github.com/DPDK/dpdk/commit/9c2e6e75f695f1c2ab1d2df99f1b4f427357609c)
- Added support for IPV4, ICMP, PORT_ID, VOID, UDP, TCP flow items to the ntnic driver. (Architecture event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [4e2798a](https://github.com/DPDK/dpdk/commit/4e2798a722f6b50c103a80d4c16b88ff7ffdfdf1), [43999d0](https://github.com/DPDK/dpdk/commit/43999d0d4ddcc5cd252cbff2afc00298ad5b1b18), [47003b9](https://github.com/DPDK/dpdk/commit/47003b93c375a41889d68e4bf3fc9a2c92c5eb56), [57fa1d4](https://github.com/DPDK/dpdk/commit/57fa1d4ddb504f2f98ad318c20fb269c49105738), [e872a0c](https://github.com/DPDK/dpdk/commit/e872a0c9507a660789b2a7b1fc0f33d633db3b72), [a8fbe91](https://github.com/DPDK/dpdk/commit/a8fbe91974c95497eeec8b18d52f7ee25c4c1bec)
- Add stream aging support to the ntnic driver, including obtaining aging streams and inline profile aging implementation. (Architecture event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [41e430d](https://github.com/DPDK/dpdk/commit/41e430dec4b8369714b196d21b3682264beb2b8a), [57a7d2b](https://github.com/DPDK/dpdk/commit/57a7d2bcff72fdb57192d7cf765f89c059d74840)
- Added support for VLAN flow items to the ntnic driver. (Architecture event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [5623282](https://github.com/DPDK/dpdk/commit/56232827a0d7b0923361353764dc93d28a7bf0e8)
- Added support for SCTP flow items to ntnic driver. (Architecture event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [af7ae7a](https://github.com/DPDK/dpdk/commit/af7ae7aa3ca699393fb146d683873b90c69e95e6)
- Added support for IPv6 and ICMPv6 flow items to the flow API. (Architecture event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [b199509](https://github.com/DPDK/dpdk/commit/b199509a19a05938d38be417639f3c13ad93c87a)
- Added support for MODIFY_FIELD flow action to ntnic driver. (Architecture event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [339ca12](https://github.com/DPDK/dpdk/commit/339ca124e659516f35f92d376b24d60af3e3a1e2)
- Added support for GTP and GTP-PSC flow items and raw encapsulation/decapsulation actions to the net/ntnic driver. (Architectural event: ntnic FPGA hardware abstraction layer module change)
  ↳ No PR: [c6821ab](https://github.com/DPDK/dpdk/commit/c6821abf58e8e53ca800cbe2cbb30c34536dd682)
- Add software live migration support for NFP vDPA devices, including reconstructing the data path update logic, adding relay vring, interrupt settings, vring index recovery, relay threads and VHOST_F_LOG_ALL feature bits. (Architecture-related: live migration support)
  ↳ No PR: [7bd2558](https://github.com/DPDK/dpdk/commit/7bd255833d3d1c7ce558a84117c02d0fd41ad9f4), [94fde3a](https://github.com/DPDK/dpdk/commit/94fde3a7f574103ad4ba274bf015bca3879e0408), [10421b0](https://github.com/DPDK/dpdk/commit/10421b0d90751552709498ca15fa25dfa3135495), [e6ac31e](https://github.com/DPDK/dpdk/commit/e6ac31e08c7b389994d7968dfe86186647c6f77a), [9725f32](https://github.com/DPDK/dpdk/commit/9725f3260004cffafe8437deb6a6bcdb18794c23), [02fe836](https://github.com/DPDK/dpdk/commit/02fe8366156a0bc7f3049f92120c185d11bbc217), [adec2a5](https://github.com/DPDK/dpdk/commit/adec2a5ce47fa3fccd82c9796c71eeeb65e99700)
- Add independent enqueue function for event devices, add capability flags and port configuration options, and implement them in DLB2 PMD and DSW drivers. (Architecture-related: public API)
  ↳ No PR: [79ca24a](https://github.com/DPDK/dpdk/commit/79ca24a41c16445594303a62151ee68156a5a320), [6e2e98d](https://github.com/DPDK/dpdk/commit/6e2e98d6775b9d39ef4d5ef75d86416085154c88), [0dab9af](https://github.com/DPDK/dpdk/commit/0dab9afe0c2d4d47f79241050e35158d53f62b01)
- Added a pre-scheduling mechanism for event devices, including capability flags, configuration types, runtime modification APIs, pre-scheduling prompt APIs, and implemented them in cnxk event devices. (Architecture-related: public API)
  ↳ No PR: [acc65ee](https://github.com/DPDK/dpdk/commit/acc65ee307f7a18d2d560ebcee750e5407318def), [c1bdd86](https://github.com/DPDK/dpdk/commit/c1bdd86d04d161c07c61ec1be8ef081108d29d2a), [4ade669](https://github.com/DPDK/dpdk/commit/4ade669c2823c0ebcaf7bfb7589db13cb2e4a6d8), [53e736a](https://github.com/DPDK/dpdk/commit/53e736a04dca6725b67dbe1d40b86520b0c28f97), [6cf329f](https://github.com/DPDK/dpdk/commit/6cf329f9d8c2eb97c8f39becd514c14b25251ac1), [7a7a04d](https://github.com/DPDK/dpdk/commit/7a7a04d3ce8eab9b53d23b673dfdc71b50fd523d)
- Added a shutdown operation to the fslmc bus, added rte_fslmc_close API and multiple device shutdown functions, supporting the release of DPAA2 device resources when the application is closed. (Architecture-related: public API)
  ↳ No PR: [274fd92](https://github.com/DPDK/dpdk/commit/274fd921ff7f2829c4ddb8f488a5a3e17499aad2)
- Added rte_thash_gen_key function, and introduced dynamic polynomial calculation to generate higher entropy Toeplitz hash keys and improve packet distribution in small traffic scenarios. (Architecture-related: public API)
  ↳ No PR: [6addb78](https://github.com/DPDK/dpdk/commit/6addb78158c232bfbb13561c8cbb7be33fb0d4a1), [f9773e6](https://github.com/DPDK/dpdk/commit/f9773e6676950b986c2375d9ac0bcbce8ea1b469)
- Add event device detection, configuration and port linking, unlinking and release functions to the CN20K platform. (Architecture-related: CN20K platform support)
  ↳ No PR: [45ce542](https://github.com/DPDK/dpdk/commit/45ce5425bbbe8c8e4c84134db792243ff0036054)
- Add event queue (SSO HWGRP) configuration, setting and release functions for the CN20k event device, and support adjusting the queue buffer count and quality of service through device parameters. (Architecture-related: configuration interface)
  ↳ No PR: [d2e685b](https://github.com/DPDK/dpdk/commit/d2e685b20dcbb93bac61976eb2620a8c01c05d4d)
- Adds full SSO event port, enqueue/dequeue fast path, port muting, profile switching, pre-scheduling, start/stop/shutdown, Ethernet Rx/Tx adapter, event aggregator configuration, event vector support and event timer adapter functionality for the CN20K event device. (Architecture-related: CN20K platform support)
  ↳ No PR: [9736df4](https://github.com/DPDK/dpdk/commit/9736df4f1851d8170723cf2820387a86615d2259), [b08b193](https://github.com/DPDK/dpdk/commit/b08b193bceab2202aee3928a0fa2df5e5aa3ee92), [7473a65](https://github.com/DPDK/dpdk/commit/7473a65f2f08006e92c57bf4e411cedc80647b77), [638fe88](https://github.com/DPDK/dpdk/commit/638fe881ea0f4c78b48004877026b12690bde630), [33da486](https://github.com/DPDK/dpdk/commit/33da486cd3676aa39bd83f92385e189f6e2c8ccd), [1e2d9b3](https://github.com/DPDK/dpdk/commit/1e2d9b3dfc9a475eefa472cbcd3adbd7f43e3f04), [97b495c](https://github.com/DPDK/dpdk/commit/97b495c912e11167e51a58daa01e4aa88a4770dc), [7c011b0](https://github.com/DPDK/dpdk/commit/7c011b0223cc54e0a478dda24c544ccc55967f16), [d8f53c1](https://github.com/DPDK/dpdk/commit/d8f53c18203eb2b889eaf154af9552145353e0d1), [2dab300](https://github.com/DPDK/dpdk/commit/2dab30000ba66464a3c9f35c041ad0994cd3ec2c), [54101f8](https://github.com/DPDK/dpdk/commit/54101f84f718f583fad6dcbc81858dd5f1f4d3c1), [62afdd8](https://github.com/DPDK/dpdk/commit/62afdd8d493d8f563c053a4afccb3c5acd1acf54), [b775abd](https://github.com/DPDK/dpdk/commit/b775abdd412bab2bfa698f7598979155bbbb24b0), [822d4ef](https://github.com/DPDK/dpdk/commit/822d4ef519f66b4f1184a1e708ed758e44b99b3a), [6305afe](https://github.com/DPDK/dpdk/commit/6305afee038f47b64236069eeb4355d28ef8fec9)
- Update the event timer basic code to support hardware accelerated timer startup and cancellation functions, and add a new hardware work queue configuration interface. (Architecture-related: hardware accelerated timer interface)
  ↳ No PR: [f3c7b60](https://github.com/DPDK/dpdk/commit/f3c7b60769f997be0c49788d7bfc515c59910f83)
- Added infrastructure support for the flow function to the ntnic driver, including configuration API, flow operation registration, creation and destruction, configuration file management, flow group handle, etc. (Architecture-related: flow API infrastructure)
  ↳ No PR: [b01eb81](https://github.com/DPDK/dpdk/commit/b01eb812018690b6ec94303a4cdb78bd3d7439a9), [ed01e43](https://github.com/DPDK/dpdk/commit/ed01e43664aaa98b5660972e9b18645080afcc4e), [e526adf](https://github.com/DPDK/dpdk/commit/e526adf1fdef0cf12afe5c03c59f7591bd197591), [52fae3f](https://github.com/DPDK/dpdk/commit/52fae3f41b7a4cdd23d61c65e4712982970e1240), [11ea978](https://github.com/DPDK/dpdk/commit/11ea97805ba167864f318bd32dcd309bf33a4d49), [2005c54](https://github.com/DPDK/dpdk/commit/2005c5493344798df735cfbd1f3b7ac6b97a3b1c), [8385ba0](https://github.com/DPDK/dpdk/commit/8385ba0e4008d6a02af5fae8576e119301208b1a), [6fec9a9](https://github.com/DPDK/dpdk/commit/6fec9a9a12e192efdd750509b0f411b63daed75e)
- Added flow create/destroy function to ntnic driver, supporting item any and action port id. (Architecture-related: flow create/destroy)
  ↳ No PR: [e02fdb6](https://github.com/DPDK/dpdk/commit/e02fdb65c2a8a90f4457a04a37a9e7bca4410434)
- Added support for QUEUE, MARK, JUMP, DROP flow actions to the ntnic driver. (Architecture-related: flow action extension)
  ↳ No PR: [b889055](https://github.com/DPDK/dpdk/commit/b8890554b8075bce07d290bef76ebdd76ea55d7b), [7495277](https://github.com/DPDK/dpdk/commit/749527702bd0ac78f4ff8cea56952bbf2c407f4d), [8006d07](https://github.com/DPDK/dpdk/commit/8006d07856e01873c9bcf5409c2b9993c7569ae8), [ba8c9f9](https://github.com/DPDK/dpdk/commit/ba8c9f967b682950de9496dcefef8b25641fa4e5)
- Added support for ETH flow items to the ntnic driver, and expanded the processing of flow actions such as MODIFY_FIELD, RAW_ENCAP, RSS. (Architecture-related: ETH flow items and action extensions)
  ↳ No PR: [29584e9](https://github.com/DPDK/dpdk/commit/29584e9dc47b60df55e6e05942d1507ba5db6e9b)
- Implemented the processing thread of the flow learning queue for the ntnic driver, and added related buffer control, statistical update and queue management functions. (Architecture-related: ntnic driver core module)
  ↳ No PR: [96c8249](https://github.com/DPDK/dpdk/commit/96c8249be53e94d21e5078cb2f21c3f31bbcd71e)
- Added matching and action database properties to the net/ntnic driver, and implemented the match/action dereference function. (Architecture-related: ntnic driver core module)
  ↳ No PR: [032d2b7](https://github.com/DPDK/dpdk/commit/032d2b7603c864ed27935ba2916b052b42c8dadc)
- Added the ability to export flow rules (flow dump) in human-readable format to the ntnic driver. (Architecture-related: public API)
  ↳ No PR: [6f0fe14](https://github.com/DPDK/dpdk/commit/6f0fe142caedfd0c9dbfb4e1288cfe6b1462c739)
- Added flow flush support for net/ntnic driver. (Architecture-related: public API)
  ↳ No PR: [f7cb842](https://github.com/DPDK/dpdk/commit/f7cb8420e2b004613497048b40baac42f59d6e52)
- Enabled the receive side scaling (RSS) function for the ntnic network card driver, including adding RSS configuration structure, hash update and acquisition interface, and RSS action processing in flow rules. (Architecture-related: public API)
  ↳ No PR: [8eed292](https://github.com/DPDK/dpdk/commit/8eed292b277518a6d969e62b05557331dbec94da)
- Add a statistics polling mechanism to the ntnic driver, add a new statistics thread and a series of functions for polling the statistics module and updating data through DMA. (Architecture-related: public API)
  ↳ No PR: [a1ba8c4](https://github.com/DPDK/dpdk/commit/a1ba8c473f5c4b9b3bfb487cc3e18c37c19c8777)
- Added the FLM statistics interface, implemented the flow_get_flm_stats function and registered it in the operation table. (Architecture-related: public API)
  ↳ No PR: [971245a](https://github.com/DPDK/dpdk/commit/971245aa17ca9430b8462f38ad451a27ff909b6c)
- Added extended statistics (xstats) support to the ntnic network card driver, including operations such as acquisition, acquisition by ID, reset, and name acquisition, and initialized related operation interfaces. (Architecture-related: public API)
  ↳ No PR: [cf6007e](https://github.com/DPDK/dpdk/commit/cf6007eac4989cdfc442547f0dd700cc3c76041b)
- Expanded the xstats statistics function for the ntnic driver, and added support for the collection and reporting of FLM learning, cancel learning, load and other counters. (Architecture-related: public API)
  ↳ No PR: [e7e49ce](https://github.com/DPDK/dpdk/commit/e7e49ce6c760888e62e27084a45446a70305cbfa)
- Extended flow info acquisition and flow configure functions for inline profile, and added creation and release operations for age queue module. (Architecture-related: public API)
  ↳ No PR: [e7e01fd](https://github.com/DPDK/dpdk/commit/e7e01fd15ddee1eb92d68a3aabe800850a8c757a)
- Add stream aging event support to the ntnic driver, expand the aging event callback of the port thread, and add read and write interfaces for LRN, INF, and STA registers. (Architecture-related: public API)
  ↳ No PR: [c0d4444](https://github.com/DPDK/dpdk/commit/c0d44442b8315eabda40c1461a85856576b9a728)
- Add flow meter support for inline configuration files, including meter flow management, queue operations, flow programming, initial cleanup, statistics reading and API registration. (Architecture-related: public API)
  ↳ No PR: [4033e05](https://github.com/DPDK/dpdk/commit/4033e0539435c49c10cd17a4837af91fb7e62c57)
- Added flow action update function to ntnic driver, extended rte_flow_ops interface and internal flow_filter_ops, and implemented specific functions in inline profile. (Architecture-related: public API)
  ↳ No PR: [54204ea](https://github.com/DPDK/dpdk/commit/54204ead942133b853c1a882345a61914ec619ca), [713bf08](https://github.com/DPDK/dpdk/commit/713bf087cedaf5b77da6eaada9335297675345d0), [dc52e60](https://github.com/DPDK/dpdk/commit/dc52e60cfae9a93cc748cf350435d31ad1191c47)
- Add asynchronous stream creation/destruction and stream template support to the ntnic driver, extend the public interface and internal implementation, including stream mode templates, action templates, template table operations. (Architecture-related: public API)
  ↳ No PR: [87b3bb0](https://github.com/DPDK/dpdk/commit/87b3bb06d918af82092b4aadecb9d19ac354606d), [8195eb0](https://github.com/DPDK/dpdk/commit/8195eb04332ffb2285babe459e997c4087f77100), [1042162](https://github.com/DPDK/dpdk/commit/1042162db4393a19a2eb69722f4e8a7477bf80fd), [96d92ae](https://github.com/DPDK/dpdk/commit/96d92ae46407bd381ac4d97d922e588763227897)
- Add MTU configuration function to ntnic driver, support setting MTU through rte_eth_dev_set_mtu API. (Architecture-related: public API)
  ↳ No PR: [6019656](https://github.com/DPDK/dpdk/commit/6019656d6f6848c83591f24867538311545776eb)
- Added the opposite macro corresponding to the existing switch macro in the flow API configuration header file to support enabling fragmentation, forwarding IPv4 DF packets and IPv6 fragmentation functions. (Architecture-related: public API)
  ↳ No PR: [190e99b](https://github.com/DPDK/dpdk/commit/190e99be4fd06ab10bc9a05b4740c05c55665529)
- Fixed the problem of incorrectly removing all callbacks that do not specify a device name when logging out of device event callbacks. Now only callbacks that match the callback function and parameters are removed. (Architecture-related: public API)
  ↳ No PR: [66fd2cc](https://github.com/DPDK/dpdk/commit/66fd2cc2e47c69ee57f0fe32558e55b085c2e32d)
- Fixed issues with the PTP timestamp function in the cnxk driver, including the mbuf_addr in the VF being destroyed and the Rx offload flag not being set correctly. (Architecture-related: cnxk PTP timestamp behavior)
  ↳ No PR: [0efd93a](https://github.com/DPDK/dpdk/commit/0efd93a2740d1ab13fc55656ce9e55f79e09c4f3), [f12dab8](https://github.com/DPDK/dpdk/commit/f12dab814f0898c661d32f6cdaaae6a11bbacb6e), [697883b](https://github.com/DPDK/dpdk/commit/697883bcb0a84f06b52064ecbf60c619edbf9083)
- Allow users to configure the number of STC allocated per context to avoid exhaustion of hardware resources due to excessive default allocation. (Architecture-related: public API)
  ↳ No PR: [691326d](https://github.com/DPDK/dpdk/commit/691326d15da263d068de71c468c74c225c4f75c3)
- Add functions to release the aging event queue and status event queue during the ntnic driver deinitialization process to ensure safe thread termination. (Architecture-related: public API)
  ↳ No PR: [4f0f5ab](https://github.com/DPDK/dpdk/commit/4f0f5ab0e4eb5ce654ca315a8faf646bb14c8ef7)
- Fixed the issue of incomplete log message list, added missing error messages and added static assertions to ensure list completeness. (Architecture-related: public API)
  ↳ No PR: [c4e84cd](https://github.com/DPDK/dpdk/commit/c4e84cd7f77ae44598576d88357138a08734a494)
- Replace legacy zero-length arrays in event device drivers and libraries with flexible array members. (Architecture-related: ABI compatibility)
  ↳ No PR: [29911b3](https://github.com/DPDK/dpdk/commit/29911b323e7a4200b95e2049df08779c0673fbfc)
- Remove single event enqueuing and dequeuing interfaces, retaining only batch enqueuing and dequeuing functions. (Architecture-related: public API)
  ↳ No PR: [dd1d439](https://github.com/DPDK/dpdk/commit/dd1d4398795aeaaa32b66889b64650e940d7204f), [88ca872](https://github.com/DPDK/dpdk/commit/88ca872150d0b61b4e6ffcb96f5cecc9e781adb5), [34e3ad3](https://github.com/DPDK/dpdk/commit/34e3ad3a1e423a874d0d2388efa04d5d6ebee340)
- Removed single event enqueuing and dequeuing interfaces in multiple event drivers, leaving only batch operations. (Architecture-related: public API)
  ↳ No PR: [e20e214](https://github.com/DPDK/dpdk/commit/e20e2148cf9268fa16ad6d0baff943a3eaae5bf0), [3cdcc0c](https://github.com/DPDK/dpdk/commit/3cdcc0c17c6f62c4355b3adcc3191db8e7546d52), [e1b07dd](https://github.com/DPDK/dpdk/commit/e1b07dd581cb487e1138e60c21159c499173352e), [813ab18](https://github.com/DPDK/dpdk/commit/813ab18d5753d6bf78ec614aecc0b6bd583aab1f), [8b565b3](https://github.com/DPDK/dpdk/commit/8b565b3445b67567a459d48e64ba5700320fc852), [a83fc0f](https://github.com/DPDK/dpdk/commit/a83fc0f4e118019b2e4fc8f033d59aedce17d7cb), [5079ede](https://github.com/DPDK/dpdk/commit/5079ede71edeed44c6c25e9ceffcd342940b309f)
- Register an independent dynamic log type for DSW event driver. (Architecture-related: dynamic log type)
  ↳ No PR: [5727bd6](https://github.com/DPDK/dpdk/commit/5727bd63bc6840f2db07043b1ffaa4e1619817ea)
- Replace the GCC built-in atomic operations in the event/cnxk driver with the DPDK standard rte_atomic_xxx API. (Architecture-related: Atomic operation API unification)
  ↳ No PR: [01f87d5](https://github.com/DPDK/dpdk/commit/01f87d55c7b0b61c10cc8ea22079f15d77790a91)
- Perform minimum cache line alignment on the dispatch and xstat_off members of the rte_node structure to optimize performance and reserve space for future expansion. (Architecture-related: public API)
  ↳ No PR: [ba0a0e4](https://github.com/DPDK/dpdk/commit/ba0a0e44f361cbc4667088a0c0e2d0b63f8dee20)
- Optimize Thor2 statistics cache performance, change the act get API to directly receive the host memory physical address, avoid virtual address translation, and adjust mutex and main loop delays. (Architecture-related: public API)
  ↳ No PR: [ca827d4](https://github.com/DPDK/dpdk/commit/ca827d42ad72f90d045716e688b539e53e31a7cc)

### Network I/O Filter
- Added Realtek R8169 network card DPDK driver skeleton, including Meson build support, device initialization, configuration and interrupt control and other basic functions. (Architecture event: cnxk_ethernet_driver module adds cn20k variant support)
  ↳ No PR: [9b170cf](https://github.com/DPDK/dpdk/commit/9b170cfc6303a9a9a7279149ac6800a72239ad4e)
- Introduced GDTC rawdev driver skeleton, used to connect two independent hosts, including basic methods such as configure/start/stop. (Architecture event: cnxk_ethernet_driver module adds cn20k variant support)
  ↳ No PR: [30495f5](https://github.com/DPDK/dpdk/commit/30495f54583d93d50df02ec5e15cbaad6f6dcc6a), [81c6bac](https://github.com/DPDK/dpdk/commit/81c6bacb0cdc43bc90d72e66968777653fbc4e31)
- Migrate the QDMA header files from the dpaa2 driver to the public dpaax driver, unify the macro naming and remove the BMT settings of conditional compilation, and replace it with offset-based IOVA calculation. (Architecture-related: public header file migration)
  ↳ No PR: [7cfcce8](https://github.com/DPDK/dpdk/commit/7cfcce8e5ed809bd1a1c81ab2b84ab6146a4bbd2)
- Add basic control path support for CN20K Ethernet devices, including receive/send offload flags, packet type settings, queue management, PTP time synchronization and other functions. (Architecture event: Added CN20K Ethernet driver)
  ↳ No PR: [1bf0fd7](https://github.com/DPDK/dpdk/commit/1bf0fd7e4f5357238e68ab2f53892aad3ba53748)
- Add the receive function and send function selection function based on the offload flag for the CN20K network card. (Architecture event: Added cn20k hardware support)
  ↳ No PR: [8bf5085](https://github.com/DPDK/dpdk/commit/8bf50857ce08f9d330c25820461a2962dc2685d7), [ec380d4](https://github.com/DPDK/dpdk/commit/ec380d45edaa00b5dc3c38d2a3432c6553ee3e30)
- Add scalar Tx burst support for CN20K network card, including basic send and multi-segment send. (Architecture event: Added cn20k hardware support)
  ↳ No PR: [006c1da](https://github.com/DPDK/dpdk/commit/006c1daa89b9be6fea53ea49fc34fd382ebe844d), [e634a59](https://github.com/DPDK/dpdk/commit/e634a59477f6c0d0ca380e32d003baed8cd2f795)
- Added PMD API for Inline IPsec hardware SA refresh and base address acquisition, and changed the input parameters of the existing API from device pointer to port ID. (Architecture-related: public API)
  ↳ No PR: [a72e156](https://github.com/DPDK/dpdk/commit/a72e15611303cceadc8233b6713e5978089e1587)
- Added PMD API to obtain statistics on the number of encryption/decryption bytes and number of packets in the CPT queue. (Architecture-related: public API)
  ↳ No PR: [d8c8ad3](https://github.com/DPDK/dpdk/commit/d8c8ad3a1feef3905c8c3eb27db9d454a6e16856)
- Add interrupt callback registration and deregistration API for RVU LF original device, and add self-test function to verify PMD API. (Architecture-related: public API)
  ↳ No PR: [f4c67d7](https://github.com/DPDK/dpdk/commit/f4c67d7218b74b2dab86a6a5d3af12d47e6f55e0), [aeb8615](https://github.com/DPDK/dpdk/commit/aeb86158bf15140d49f9904ae40aa0ea9f13ec62)
- Added mailbox message handler registration and deregistration API, message ID range setting API and message processing API for RVU LF device to realize complete mailbox message processing function. (Architecture-related: public API)
  ↳ No PR: [7396eac](https://github.com/DPDK/dpdk/commit/7396eaceaac52e6d66808daaf5ba414a47d2cfe6), [0924cc0](https://github.com/DPDK/dpdk/commit/0924cc0b2489f72fcedd92fa4804821c730f7559), [384903e](https://github.com/DPDK/dpdk/commit/384903ed3e6427e1a1a05d3df313a272011e2bf6)
- Added API rte_pmd_rvu_lf_pf_func_get to obtain RVU LF device pffunc and API rte_pmd_rvu_lf_bar_get to obtain BAR address (architecture-related: public API)
  ↳ No PR: [fcac76a](https://github.com/DPDK/dpdk/commit/fcac76a874e6419f125e5cf6bbd38bc4097351bd), [79c469d](https://github.com/DPDK/dpdk/commit/79c469df190056eb44ff5c91c6b02d49a1b98884)
- Added statistical functions to the ntnic driver, including statistical initialization, setting, obtaining and resetting, and added related FPGA definitions. (Architecture-related: public API)
  ↳ No PR: [effa046](https://github.com/DPDK/dpdk/commit/effa04693274e59d82b24907c5ee4d1f8eef3cd7)
- Add the --hairpin-map parameter to testpmd to support explicitly specifying the port and queue mapping relationship between Rx and Tx in hairpin forwarding. (Architecture-related: public API)
  ↳ No PR: [5334c3f](https://github.com/DPDK/dpdk/commit/5334c3feb137ca4eeb4c0f150aae602016b6a5ea)
- Added MTU update support for r8169 network card driver, added MTU setting function and firmware version acquisition function, and added DASH stop processing when the device is shut down. (Architecture-related: public API)
  ↳ No PR: [9514e4b](https://github.com/DPDK/dpdk/commit/9514e4b6d37db561dd33448c585a9fa42a0e0283), [b2e1725](https://github.com/DPDK/dpdk/commit/b2e17252e6161a1a2c29978bfffbc6f3b3337e8e)
- Support BlueField firmware NUM_OF_PF=0 configuration, which allows detecting PF devices when there is no host PF and skips error checking for unassociated ports. (Architecture-related: platform compatibility)
  ↳ No PR: [6d1f439](https://github.com/DPDK/dpdk/commit/6d1f4393349fc98397b409af89642c4a2aa3ee19)
- Fixed the problem of inaccurate detection of sending queue full status during polling in the mlx5/hws driver. Instead, use the actual queue status judgment to avoid failure of rule movement when matcher re-hashes. (Architecture-related: public API)
  ↳ No PR: [b56ba21](https://github.com/DPDK/dpdk/commit/b56ba2139f4dc04b97f69f0d0ece1f28725a100b)
- Fixed the dangling pointer warning caused by moving the stream parameter structure from the stack to the queue private data structure in the mlx5 driver, and added the error code setting. (Architecture-related: public API)
  ↳ No PR: [d135766](https://github.com/DPDK/dpdk/commit/d1357665a85b30066c8b69996ddf601332a198f8)
- Fix miniCQEs number calculation, instead obtain the number of miniCQEs in the compressed CQE array from CQE instead of header packet, to avoid segfault when mbuf is corrupted. (Architecture-related: data path behavior)
  ↳ No PR: [a7ae9ba](https://github.com/DPDK/dpdk/commit/a7ae9ba1f8c888a7ed546a88a954426477cd24a4)
- Fix the reference counting and condition checking of the shared Rx queue control structure when the port is stopped and the device is closed, to ensure that the control structure is released correctly and avoid crashing when the port is restarted. (Architecture-related: public API)
  ↳ No PR: [f8f294c](https://github.com/DPDK/dpdk/commit/f8f294c66b5ff6ee89590cce56a3d733513ff9a0)
- Fixed the memory alignment problem of the SQ flow item structure in the mlx5 driver on 64-bit systems to prevent buffer overflow during DPDK copying; also added a context existence check for meter operations in HWS mode and refused to perform related operations before port configuration. (Architecture-related: public API)
  ↳ No PR: [7c66fa4](https://github.com/DPDK/dpdk/commit/7c66fa49ddcce1981c2fa3a0c024ec82b036639c), [61a8106](https://github.com/DPDK/dpdk/commit/61a810617ec864aa30b36d7aaffc0bda4cc28f54)

### Inter-Connect Pipes
- Added CNXK RVU LF raw device driver to support mailbox communication and interrupt handling between PF/VF. (Architecture-related: Added CNXK RVU LF raw device driver)
  ↳ No PR: [318ee1b](https://github.com/DPDK/dpdk/commit/318ee1b0468299e92411ea8616073c477743b34e)
- Added zxdh network card driver basic framework, including ethdev initialization and PCI detection functions. (Architecture-related: Added zxdh network card driver framework)
  ↳ No PR: [29e8928](https://github.com/DPDK/dpdk/commit/29e89288ff14f153c981bd6658ef80939bc16a05)
- Change the DPAA2 device creation function to directly receive the device object instead of the object ID, and assign its container to each device. (Architecture-related: public API)
  ↳ No PR: [4d4399a](https://github.com/DPDK/dpdk/commit/4d4399ae859fbb0b1a4390fb8efb7d79a791a4ad)
- dmadev adds strict priority configuration support, the device needs to declare the RTE_DMA_CAPA_PRI_POLICY_SP flag. (Architecture-related: public API)
  ↳ No PR: [2dff0bc](https://github.com/DPDK/dpdk/commit/2dff0bcd3b54bc3279de42123aa618620224ad44)
- Support configuring device package type through Rx package uninstall flag, and add a new setting interface for applications to control this flag. (Architecture-related: public API)
  ↳ No PR: [a498019](https://github.com/DPDK/dpdk/commit/a498019d793b3d5ae354a1a947b6bec3bd16fb5f)
- Add IEEE 1588 PTP timestamp support for DPAA platform, including Rx/Tx timestamp reading function of DPAA1 platform and ethdev API for general enable/disable, read/write/adjust timestamp. (Architecture-related: public API)
  ↳ No PR: [615352f](https://github.com/DPDK/dpdk/commit/615352f522707e432c1a77f6e8f81a807d43866e), [7358544](https://github.com/DPDK/dpdk/commit/73585446921304f543360af104473a955ae46df9)
- Upgraded MC firmware compatibility to 10.37, and added/updated multiple MC driver APIs. (Architecture-related: platform compatibility)
  ↳ No PR: [591200e](https://github.com/DPDK/dpdk/commit/591200ef6f32b56adc367ebe3647cc3dbe9362db)
- Add EEPROM reading and writing and module EEPROM information acquisition functions for nfp network card. (Architecture-related: public API)
  ↳ No PR: [7f69381](https://github.com/DPDK/dpdk/commit/7f693813cf40f52a428507e01c7dd30648d59ca1)
- Add PCI initialization implementation for zxdh network device, including PCI capability acquisition, configuration reading and writing, status management, feature negotiation, interrupt setting and queue management. (Architecture-related: new driver module)
  ↳ No PR: [102ac20](https://github.com/DPDK/dpdk/commit/102ac20e036c53e86ad0b4a3cf1fe5b0ba2f1b3e), [425a96e](https://github.com/DPDK/dpdk/commit/425a96e64fb8e1cc5fac9cd2c05abc870c89bd11)
- Add the function of obtaining device information to the zxdh network card driver, including defining the device operation structure and registering the device information obtaining callback. (Architecture-related: public API)
  ↳ No PR: [fea1ddb](https://github.com/DPDK/dpdk/commit/fea1ddb0c1bfecd131c43f71b1dddec32845209c)
- Fixed the null pointer access problem that may occur when the status parameter in the rte_dma_vchan_status function is NULL, added a null pointer check and adjusted the variable assignment order. (Architecture-related: public API)
  ↳ No PR: [e5389d4](https://github.com/DPDK/dpdk/commit/e5389d427ec43ab805d0a1caed89b63656fd7fde)
- Removed the packed attribute of struct rte_afu_device, the structure does not need to be compactly aligned. (Architecture-related: public API)
  ↳ No PR: [8f99903](https://github.com/DPDK/dpdk/commit/8f999036e16d03d1cc704cf97f5de5b2751d8d49)
- Refactor the DPAA2 QDMA driver, introduce routing configuration based on PCIe port parameters, and add multi-queuing and FD operation auxiliary functions. (Architecture-related: public API)
  ↳ No PR: [3d990fa](https://github.com/DPDK/dpdk/commit/3d990faa3f51f4f2ef8198f2971837cfae9ccaa9)
- Rename the structures and enumerations related to HWS control flow rules, and remove the hw prefix to facilitate reuse in Verbs and DV flow engines. (Architecture-related: public API)
  ↳ No PR: [d6708a9](https://github.com/DPDK/dpdk/commit/d6708a9d29e48595202a816df1aedd082003550c)
- Mark dpcon_close API as an internal symbol to limit its external visibility. (Architecture-related: public API)
  ↳ No PR: [1eb72b9](https://github.com/DPDK/dpdk/commit/1eb72b977b2cf2d82bcf116c241f03f286b5663f)
- Added lcore variables programming guide, and fixed description of experimental flags and default buffer size (changed from 1 MB to 128 kB) in the documentation. (Architecture-related: public API)
  ↳ No PR: [776d475](https://github.com/DPDK/dpdk/commit/776d4753893335d43011f97b08d422b84a54b16c), [37dda90](https://github.com/DPDK/dpdk/commit/37dda90ee15b7098bc48356868a87d34f727eecc)
- Fixed compilation compatibility issues with bitset header files under GCC and MSVC, hiding experimental API dependencies through conditional compilation, and replacing __builtin_ffsll with rte_bsf64. (Architecture-related: platform compatibility)
  ↳ No PR: [8b65ddc](https://github.com/DPDK/dpdk/commit/8b65ddc0522ef6d8134edbcfd05bcd7d4f748d19), [a3e126f](https://github.com/DPDK/dpdk/commit/a3e126fd58d11aee85220480f4bf692612fbadc2), [5f3cd04](https://github.com/DPDK/dpdk/commit/5f3cd043a8e115353902b8b5d76ec0bb1928a2f5)

### Memory Buffer Manager
- Add reconnection support for vhost backend and VDUSE device, including reconnection log mechanism and state recovery function, supporting reconnection without front-end cooperation. (Architecture-related: public API)
  ↳ No PR: [15677ca](https://github.com/DPDK/dpdk/commit/15677ca2c751b3be2f02429bb006d859dccae0c0), [da79cc7](https://github.com/DPDK/dpdk/commit/da79cc7fda76a1e1ff9194fc54f1d948d22f4809), [5597769](https://github.com/DPDK/dpdk/commit/559776944efc6a7f7024cf6bc8583662134a4eb6), [a2a05e5](https://github.com/DPDK/dpdk/commit/a2a05e55396435db4fd06f91a829175fba885fa3)
- Added output of total memory size in memory segment and memory area dump API. (Architecture-related: public API)
  ↳ No PR: [17bb600](https://github.com/DPDK/dpdk/commit/17bb60044bae68c0f062755527ad8febe9f448d1)
- Removed the build exclusion of the mempool library under the MSVC compiler and now supports compilation under MSVC. (Architecture-related: platform compatibility)
  ↳ No PR: [2cd0c96](https://github.com/DPDK/dpdk/commit/2cd0c96f5b73e81317e97ac719862c9e9149e4ed)
- Initialized the mempool operation for the CN20K platform, allowing it to reuse the mempool ops of CN10K. (Architecture-related: platform compatibility)
  ↳ No PR: [8d1ddeb](https://github.com/DPDK/dpdk/commit/8d1ddeb6c3382e834fbc0a459788a9f58e1ae7fd)

## Routine Changes

### New features
- Added shift and mask definitions for VLAN source fields for i40e base driver, input set for flow-directed programming.
  ↳ No PR: [485464c](https://github.com/DPDK/dpdk/commit/485464cf37247961fe0adbca2172a09ae0a5106b)
- Add macro definitions related to DDP packet type for i40e driver.
  ↳ No PR: [4e7dd16](https://github.com/DPDK/dpdk/commit/4e7dd1680896201dedcbfec4f23959198ef48163)
- Add RSS and flow director input set mask macro definitions for X722 series network cards.
  ↳ No PR: [e861ed0](https://github.com/DPDK/dpdk/commit/e861ed0b47fec56ecb9a5f8125e48c1048b9fdff)
- Add FLU (MAC source pruning function) related register macro definitions to the i40e network card driver.
  ↳ No PR: [c13b636](https://github.com/DPDK/dpdk/commit/c13b636cd78f5994e833b5650979e6dcca0b3e92)
- Support configuring multiple Rx and Tx queues for NFP flower representor ports, remove hard-coded restrictions and adjust related data sending and receiving and resource release logic.
  ↳ No PR: [64e472d](https://github.com/DPDK/dpdk/commit/64e472d84a95ccd33dc3568cd84bd7aa8c0abbfc), [602792e](https://github.com/DPDK/dpdk/commit/602792e55cbac4b9704104be3e9b5b4fdcfe7098), [761e06e](https://github.com/DPDK/dpdk/commit/761e06e2278630d47e234aae4cb8da00b7bc088a)
- Added SA information telemetry command to cnxk network card driver, which supports querying inbound and outbound SA information through port ID and SA index.
  ↳ No PR: [d74ed16](https://github.com/DPDK/dpdk/commit/d74ed1628f7e3772593be6c48f364816ae85e448)
- Implemented detailed packet parsing based on hardware annotations, supported identification of IPSec ESP, GRE and SCTP packets, and updated the list of supported packet types.
  ↳ No PR: [a350a95](https://github.com/DPDK/dpdk/commit/a350a9543d4e7a842e0ad82ef4ad81c7314f7c2e)
- Add CN20K device PCI ID (including PF and VF) to mempool/cnxk driver.
  ↳ No PR: [5ed98ad](https://github.com/DPDK/dpdk/commit/5ed98ad510aeba72dbd3db275cbac555c3fb661b)
- Add configuration support for NIX receive queue, send queue and completion queue in common/cnxk driver for CN20K chip.
  ↳ No PR: [4785c40](https://github.com/DPDK/dpdk/commit/4785c406c26df4f8c29a84ea89712aa95acde44d)
- Added bandwidth profile support for CN20K platform, for use with sink policer.
  ↳ No PR: [43e4281](https://github.com/DPDK/dpdk/commit/43e42816d36c7348d80104a05a30666eab733da0)
- Add RSS configuration support for CN20K, and fix the format problem in nix_cn9k_rss_reta_set, and rename nix_rss_reta_set to nix_cn10k_rss_reta_set.
  ↳ No PR: [86667e8](https://github.com/DPDK/dpdk/commit/86667e895f5bb78f836cf93fa574c32faf4d36eb)
- Add SM3, HMAC SM3, SM4 (CBC/ECB/CTR) algorithm support to AESNI_MB PMD.
  ↳ No PR: [9a1d479](https://github.com/DPDK/dpdk/commit/9a1d479742aa5e27313117915f8a465867a2d6e6), [add05a0](https://github.com/DPDK/dpdk/commit/add05a010671f59503198d7e5fe9fc74348aba65), [0c2f1b0](https://github.com/DPDK/dpdk/commit/0c2f1b05ffc7493dada89df10ef0ad704004a870)
- Add complete queue operation support to the ntnic driver, including queue configuration, start, stop, release, packet processing, scatter-gather hardware release, DBS virtqueue initialization and split-queue functions.
  ↳ No PR: [fe91ade](https://github.com/DPDK/dpdk/commit/fe91ade9f5dbda414350a18f6cd8b0b1d9942649), [b0cd36e](https://github.com/DPDK/dpdk/commit/b0cd36e9608c89381bda58ba746d39f90202571a), [5284180](https://github.com/DPDK/dpdk/commit/5284180a54988cbf612c66ae864286bb9ce93ea0), [6b0047f](https://github.com/DPDK/dpdk/commit/6b0047fadf4116f0e714998d0b82aec910ef6ead), [da25ae3](https://github.com/DPDK/dpdk/commit/da25ae3c88fd38f583d38f9008e5efc4ea6046e9), [576e772](https://github.com/DPDK/dpdk/commit/576e77213f0d333284d740acdbbe8de510ab7f1c), [e13da07](https://github.com/DPDK/dpdk/commit/e13da07fd9fda5a248abf503d3272a4efcbf44e8)
- Add the ability to set device EEPROM via the command line in testpmd.
  ↳ No PR: [5478054](https://github.com/DPDK/dpdk/commit/5478054254ca86b6816514b9acd093c51a6d7ffb)
- Added set port <port-id> led on/off command in testpmd, which is used to control the LED switch of the Ethernet device port.
  ↳ No PR: [045e35a](https://github.com/DPDK/dpdk/commit/045e35aa3fd6a9f82a6b30be81403a77fe4ee551)
- Add SM2 operation capabilities to the OpenSSL encryption device driver, supporting signature, verification, encryption and decryption.
  ↳ No PR: [8fdfedb](https://github.com/DPDK/dpdk/commit/8fdfedb125beac73e4ebe14f5ffe369d0465ba19)
- Add an alarm mechanism to the NFP network card driver to support running the flower service through timer polling when there is no service core available.
  ↳ No PR: [ebb4542](https://github.com/DPDK/dpdk/commit/ebb45428f493df4aed55ac3b31bf6c98de71162e)
- Extended the support range for the number of scheduler child nodes in the ice driver from 8 bits to 16 bits, and removed the flag check before topology upload to support more levels of topology configuration.
  ↳ No PR: [aff0693](https://github.com/DPDK/dpdk/commit/aff06930682ca3f243d91bba3104c4af8169c38a), [5ac957b](https://github.com/DPDK/dpdk/commit/5ac957beedfbb12749aa4cbdd76f386bd0687f94)
- Added xstat counters for LPM lookup failures for IPv4 lookup nodes and xstat counters for reassembly failures for IPv4 reassembly nodes.
  ↳ No PR: [be4c0cb](https://github.com/DPDK/dpdk/commit/be4c0cb4901fc0703786e0d3da4e0123306e4539)
- Added link status update function to af_packet network PMD, obtain the IFF_RUNNING flag of the socket through ioctl to set the link status.
  ↳ No PR: [dcb035b](https://github.com/DPDK/dpdk/commit/dcb035b0ed26c9b38d569f16310dd9326680926c)
- Supports matching general tunnel packets through PTYPE, simplifying the configuration of tunnel flow rules.
  ↳ No PR: [90294fa](https://github.com/DPDK/dpdk/commit/90294fa5bc3ab8d0592bbde190dcc8b614850aad)
- Added multi-PF firmware support to the NFP driver, added a new PF stop operation, updated the PF start function, and updated the Tx/Rx function to support multiple physical functions, while simplifying the Rx function.
  ↳ No PR: [62b6097](https://github.com/DPDK/dpdk/commit/62b609721dc52ac6b520d77fadd56de50fc6f88d), [636e133](https://github.com/DPDK/dpdk/commit/636e133ec8913d8a5e964289501060b97e7d4053), [cb6448f](https://github.com/DPDK/dpdk/commit/cb6448f173688d8691494925ae2fa9d35546e3ff), [8c1d15f](https://github.com/DPDK/dpdk/commit/8c1d15f1c44f2deeb62fadf32c8b4ea7390964d3), [c2b4f0d](https://github.com/DPDK/dpdk/commit/c2b4f0d5b1c8705ec0a0bcaab37f305ce0b2137e)
- Added support for IPsec ESP transport mode packet type matching in the MLX5 driver.
  ↳ No PR: [a371119](https://github.com/DPDK/dpdk/commit/a371119084b81f77400fa3aed061d570cfc0eefe)
- Added a software tail discard function to the DPAA2 network driver to automatically release the data packets to be sent when the hardware is congested.
  ↳ No PR: [c3ffe74](https://github.com/DPDK/dpdk/commit/c3ffe74d85beb05784607a256ce47d95b91fb1de)
- Supports traffic splitting function based on VLAN ID.
  ↳ No PR: [4160359](https://github.com/DPDK/dpdk/commit/4160359077073d148557297ac8c6c7b94ea148f9)
- Add link status event support in representative port message processing, and optimize the search logic of representative ports in MTU message processing.
  ↳ No PR: [03b8c84](https://github.com/DPDK/dpdk/commit/03b8c847479e22cf5e955bf1dff4759c4e563b44)
- Support updating the RSS rules of representee through the PF port, and verify whether representee belongs to the PF port before updating.
  ↳ No PR: [29a8df5](https://github.com/DPDK/dpdk/commit/29a8df5cb664feb6f182c07868c49c0f5c9a4c46)
- The ixgbe driver supports providing per-queue statistics for less than the maximum number of queues, and no longer requires that the number of statistical queues must be equal to the maximum supported by the driver.
  ↳ No PR: [2de2328](https://github.com/DPDK/dpdk/commit/2de23282c17878ffdab7fac276c2c18b608d114d)
- Add a hook function for log output, support customized printing behavior, and facilitate formatted output on the console or log system.
  ↳ No PR: [630cdfc](https://github.com/DPDK/dpdk/commit/630cdfcd69c90dcdf54fcf6be05f73fd1ac1e0a9)
- Added color support to log output, with timestamps, subsystems and message levels individually colored, off by default, and added necessary file descriptor and terminal detection functions for Windows.
  ↳ No PR: [259f6f7](https://github.com/DPDK/dpdk/commit/259f6f78094d0fa33ce2ffe298b8df526c535f3b)
- Increased the maximum number of supported DV substreams from 32 to 64.
  ↳ No PR: [62919d3](https://github.com/DPDK/dpdk/commit/62919d327e58208b21c7972adcf3cdc9c6d7468c)
- Added configuration support for CN20K event devices, including initializing SSO hardware ports and queue resources.
  ↳ No PR: [6976186](https://github.com/DPDK/dpdk/commit/6976186968902cacf3922d5eb17c7f8b8a0041a8)
- Added LED blinking functionality to NFP network devices for identifying physical ports.
  ↳ No PR: [8bd6f54](https://github.com/DPDK/dpdk/commit/8bd6f5403743ccea850514e29d38fb239312f61d)
- Add message channel support to the zxdh network card driver, including initialization, enabling and obtaining back-end device information through message channels.
  ↳ No PR: [9d80d59](https://github.com/DPDK/dpdk/commit/9d80d5925f35587053373380d74b2a2f4a54c669), [d2fc533](https://github.com/DPDK/dpdk/commit/d2fc5332aa78c4865fd1a4be62531dbdfe613453), [6310e39](https://github.com/DPDK/dpdk/commit/6310e3976bbaa19e03c2918392294bb94af051cd)
- Add interrupt configuration function to zxdh network card driver, support RISC and DTB interrupt setting and interrupt release.
  ↳ No PR: [3630ac8](https://github.com/DPDK/dpdk/commit/3630ac8bd81f09c4cd1d12fe1c5bf84c67141c48)
- Implement device configuration operations for the zxdh network card driver, supporting functions such as queue check, reset, allocation and resource management.
  ↳ No PR: [70d49e4](https://github.com/DPDK/dpdk/commit/70d49e4b97702155b4b4f52623f7a154efddf2c8)
- Add device shutdown operation to zxdh network card driver to realize resource release.
  ↳ No PR: [27ed58d](https://github.com/DPDK/dpdk/commit/27ed58d320be21f3a0a725194a0701b5b5d1c176)
- Improve stream scalability, return appropriate error codes when the exact match table space is insufficient, and add EM usage update logic.
  ↳ No PR: [8a2e845](https://github.com/DPDK/dpdk/commit/8a2e845d735aa7379de77d51026b6b580ba05078)
- Added image support for Wh+ platform, including multi-port processing, ingress and egress image template updates and related parser adjustments.
  ↳ No PR: [987f2ec](https://github.com/DPDK/dpdk/commit/987f2ec9a0cfcb835cb62fe4c4abde6a584735a8)
- Supports overlapping streams, and includes stream sizing improvements, conditional list handling, Thor2 platform overlapping stream functionality, VFREP and non-VFREP template capability merging, compile error fixes and build warning fixes.
  ↳ No PR: [af50070](https://github.com/DPDK/dpdk/commit/af50070ef4f994196b09c96b52826e80395bbaea)
- Add VXLAN tunnel flow statistics support for Thor2 platform, and update related template files.
  ↳ No PR: [49cdf04](https://github.com/DPDK/dpdk/commit/49cdf04367be38dec1433ea21ef98d6acd151047)
- Support jump action, allow the use of group attributes in flow rules for chain matching, and add distributor table management functions.
  ↳ No PR: [83f916b](https://github.com/DPDK/dpdk/commit/83f916bddb17f2bed168a1093ff898a08cd3008b)
- Supports applying flow priority. When a flow specifies a priority, it will be placed in the corresponding location of the TCAM and the relevant template file will be updated.
  ↳ No PR: [22b6561](https://github.com/DPDK/dpdk/commit/22b65613909ee32b69d1cceea6485180a6353999)
- Add RSS flow query support at the ULP layer, add RSS query information filling and retrieval functions, and adjust related log macros.
  ↳ No PR: [35e03ba](https://github.com/DPDK/dpdk/commit/35e03bafdce10b98fc68383ed323cece507f8bb7)
- Added port table write operation, socket direct universal template, promiscuous mode, profile TCAM entry metadata setting and group missing action support.
  ↳ No PR: [105126e](https://github.com/DPDK/dpdk/commit/105126eb7e54ad26debbf3d9997c3dce0667aadd), [d4b36fc](https://github.com/DPDK/dpdk/commit/d4b36fc5f0dc59b256441c82e5a9395054026496)
- Add track type field to mapper table, merge Thor/Thor2 action template, correct GPE stream creation and deletion.
  ↳ No PR: [2aa7099](https://github.com/DPDK/dpdk/commit/2aa70990392930426d92192c59d237dd16de31e5)
- Added jump actions, dynamic tunneling and flow priority support for Thor2, and fixed universal application template issues.
  ↳ No PR: [30d7102](https://github.com/DPDK/dpdk/commit/30d7102d9e71f57b32d4c65689726f0786a5890b)
- Added stream statistics cache for Thor2, supporting background collection and counter read clearing.
  ↳ No PR: [0513f0a](https://github.com/DPDK/dpdk/commit/0513f0af034df5dc543bb6eb6b17661839491a89)
- Added hardware register access routines (MMIO, MAC OCP, CSI) for r8169 network card driver.
  ↳ No PR: [88f5b65](https://github.com/DPDK/dpdk/commit/88f5b657aa39dad2451fc48c3b2fd0ece82580d8)
- Added the core logic of the transceiver data path to the r8169 network card driver, including initialization function and transceiver function prototype, and integrated it in device startup and initialization.
  ↳ No PR: [1bbe869](https://github.com/DPDK/dpdk/commit/1bbe869ee8571aa282a1069c0f2921e13fe58e11)
- Added hardware configuration function to r8169 network card driver, implemented rtl_hw_config function and related auxiliary functions, used to initialize registers at startup.
  ↳ No PR: [619f6eb](https://github.com/DPDK/dpdk/commit/619f6ebce1152836c44a3e9b783d51f8c431c4a3)
- Add PHY configuration support to the r8169 network card driver, including PHY power on and off, EPHY configuration, PHY reset, MCU firmware version check and EEE disabling functions.
  ↳ No PR: [3858997](https://github.com/DPDK/dpdk/commit/38589978be7d4c3e2ebc6b491c4a145dcfddc07c)
- Add hardware initialization support to the r8169 network card driver, including software variable initialization, NIC reset, DASH function detection, MAC address reading and link settings, etc.
  ↳ No PR: [7d50279](https://github.com/DPDK/dpdk/commit/7d5027916b24efaf6ad974307723054c2f321aff)
- Add link status management and interrupt management functions to the r8169 network card driver, including device start/stop, link up and down switching, promiscuous mode, statistics acquisition and reset, etc.
  ↳ No PR: [f732767](https://github.com/DPDK/dpdk/commit/f7327670814e69fd5b11871828065940268f664c)
- Add complete receive (Rx) data path support to the r8169 network card driver, including receive queue settings, initialization, packet reception and hardware configuration and other functions.
  ↳ No PR: [2f198f0](https://github.com/DPDK/dpdk/commit/2f198f0a20bcf10ee3188588e80b7d5e6965d2fc)
- Add a complete TX data path implementation to the r8169 network card driver, including functions such as send queue management, message sending, checksum offloading, TSO segmentation, VLAN tagging, and sending completion cleaning.
  ↳ No PR: [63d37ff](https://github.com/DPDK/dpdk/commit/63d37ff9a453370a82a28ca8194f38b09aeb8191)
- Add statistics function to r8169 network card driver, support obtaining, clearing and initializing statistics counters.
  ↳ No PR: [fa0b0ad](https://github.com/DPDK/dpdk/commit/fa0b0ad6246709184d73fbc944039391c1db22be)
- Add configuration support for promiscuous mode and multicast mode to r8169 network card driver.
  ↳ No PR: [d2b39de](https://github.com/DPDK/dpdk/commit/d2b39de23c1d895627d15acd0c042bb3968c10dd)
- Add driver start and stop functions for rtl8125ap and rtl8125bp network cards, which need to be executed regardless of whether DASH is enabled or not.
  ↳ No PR: [b574fb4](https://github.com/DPDK/dpdk/commit/b574fb4cc855f4e86659d37ded01e7a218c38865)
- Allow using vport action in Rx stream to send directly to uplink without discarding.
  ↳ No PR: [7911783](https://github.com/DPDK/dpdk/commit/7911783578f5bc6458c2af0670efeb617980ad9c)
- Add a sending descriptor error statistics function to the ngbe network card driver, and accumulate the descriptor error count of each sending queue when obtaining and resetting statistical information.
  ↳ No PR: [3eba2f2](https://github.com/DPDK/dpdk/commit/3eba2f2888a31dc275d37203c9d03e23604822ea)
- Allow adding multicast addresses in MAC address add callback, removed address validity check.
  ↳ No PR: [c103585](https://github.com/DPDK/dpdk/commit/c103585df76017fedd5b0ea2f4769fb9ee42f31f)
- Fixed the compilation warning caused by unaligned pointer assignment in the IP fragmentation reorganization function, and replaced it with memcpy.
  ↳ No PR: [5763d24](https://github.com/DPDK/dpdk/commit/5763d240624df6e3fd4e93a9f32b3408c7774951)
- Supports separate configuration parameters for each DMA device, and reconstructs the configuration parsing and initialization process.
  ↳ No PR: [533d7e7](https://github.com/DPDK/dpdk/commit/533d7e7f66f39de658ba167aad40837d916c52b4)
- Introduced reusable code snippets in the flow_filtering example to demonstrate the use of template and non-template APIs to create flow rules, and added command line parameters to support selecting template APIs.
  ↳ No PR: [16158f3](https://github.com/DPDK/dpdk/commit/16158f34900075f2f30b879bf3708e54e07455f4)
- Add receive buffer split offload support to Broadcom NetXtreme network card driver. When the hardware supports it, IPv4/IPv6 packets can be header and data splitted at fixed offsets.
  ↳ No PR: [b5dafa3](https://github.com/DPDK/dpdk/commit/b5dafa316ebc9df7da08ae8e98a3776b80ee67c4)
- Added TSO support in DQO RDA format, added function for populating TSO context descriptor.
  ↳ No PR: [403c671](https://github.com/DPDK/dpdk/commit/403c671a46b64b6a22a0959e40b46eb6e4f05a42)
- Added FLC stashing support to dpaa2 driver, for configuring flow steering actions to align RSS configurations.
  ↳ No PR: [c794f2c](https://github.com/DPDK/dpdk/commit/c794f2cab6cc04260545784c24e3788204c44e96)
- When testpmd reads a command from a file, it will now display the command execution output to the standard output to improve user visibility.
  ↳ No PR: [76669d2](https://github.com/DPDK/dpdk/commit/76669d2e7ca9dcf50939882e74b6d06c8ce16e04)
- Add macro definitions related to time synchronization register range forcing for the E830 network card.
  ↳ No PR: [638604c](https://github.com/DPDK/dpdk/commit/638604cc386b76bc50f926c2a527bfc31a35e5c6)
- Added the function of dumping RxTx queue head and tail pointer information for hns3 driver.
  ↳ No PR: [364a31b](https://github.com/DPDK/dpdk/commit/364a31b7628536ad7c5fb68603e11c5b166df248)
- Enable the extension package numbering (XPN) function in the l2fwd-macsec example, modify the enabling conditions of XPN in the secure channel configuration, and switch the default encryption algorithm to the XPN version.
  ↳ No PR: [0d187ba](https://github.com/DPDK/dpdk/commit/0d187ba834b1a7f67fa73265743dfff9d8f706fe)
- Add single-stream dump support to the cnxk driver, and directly output its detailed information when a stream is specified.
  ↳ No PR: [abdd7a9](https://github.com/DPDK/dpdk/commit/abdd7a9d6be5fa1ad44cf3eecd71e812b8bffbcb)
- Add PHY register access routines to the RTL8169 series network card driver, including OCP address mapping, MDIO reading and writing, and bit operation functions of Ethernet PHY and PCIe PHY, and uniformly manage the hardware operation functions of multiple chip models through the rtl_hw_ops structure.
  ↳ No PR: [c4adac9](https://github.com/DPDK/dpdk/commit/c4adac969428db7024a1a160ef630cae250e0523), [8e85226](https://github.com/DPDK/dpdk/commit/8e85226086b45cc60667ad4347a75025fb59e151)
- Add stop and shutdown callback functions for CN20K event device.
  ↳ No PR: [a0fae00](https://github.com/DPDK/dpdk/commit/a0fae00a033b58302ae50dfd0bf1197f1a46bbeb)

### bug fixes
- Fixed the problem of missing verification of the number of packet fragments in the bnxt driver sending path, preventing the hardware from sending invalid descriptors due to incorrect number of fragments.
  ↳ No PR: [a4fd911](https://github.com/DPDK/dpdk/commit/a4fd911f47d71757f10d6a3abacf49388cfdd656)
- Added invalid mbuf check for bnxt driver sending path to prevent hardware reset caused by invalid mbuf, and adjusted related function return types and logging.
  ↳ No PR: [6f896ab](https://github.com/DPDK/dpdk/commit/6f896ab33991de71af234a9653d1b862f763a94a)
- Fixed the issue where the bnxt driver did not release invalid mbufs when sending, now it will release and update the oerrors statistics counter.
  ↳ No PR: [6cc5dfa](https://github.com/DPDK/dpdk/commit/6cc5dfa69a0335849fc0903d3ada943acb33c7ce)
- Fixed the problem of incorrect high-bit offset setting of action table entries in bnxt driver Tx BD, preventing PDCU from aborting acquisition due to incorrect values and causing the pipeline to stall.
  ↳ No PR: [b019ddf](https://github.com/DPDK/dpdk/commit/b019ddf9b1de65491b4c07c25bbab3dc70c15f79)
- Explicitly set TCP and UDP checksum flags for LSO capable packets, fix checksum calculation for tunneled and non-tunneled packets on some older chip variants.
  ↳ No PR: [4c04511](https://github.com/DPDK/dpdk/commit/4c0451197e5a88531c30398b58b7e5601be90080)
- Fixed the LRO offload capability export condition in the bnxt driver, which only exports the capability to the application when the compressed Rx CQE mode is not enabled.
  ↳ No PR: [019c181](https://github.com/DPDK/dpdk/commit/019c181687371f24196f437b648dc80f67519b72)
- Optimized the error log information of the argparse module to make it clearer and more accurate, and adjusted some parameter verification logic.
  ↳ No PR: [9b8df29](https://github.com/DPDK/dpdk/commit/9b8df29bf15575f2f0570e6f1e68294a399f6917)
- Fixed buffer overflow due to unhandled index wraparound in memif driver zero-copy reception, by allocating double buffer space and copying extra entries on overflow.
  ↳ No PR: [b92b18b](https://github.com/DPDK/dpdk/commit/b92b18b76858ed58ebe9c5dea9dedf9a99e7e0e2)
- Fixed encrypted scheduler session size calculation error, now correctly includes the scheduler's own session context size.
  ↳ No PR: [b00bf84](https://github.com/DPDK/dpdk/commit/b00bf84f0d3eb4c6a2944c918f697dc17cb3fce5)
- Fixed the problem of incorrect offset parameter passing when mapping log base address in vhost.
  ↳ No PR: [bdd96d8](https://github.com/DPDK/dpdk/commit/bdd96d8ac76ca412165b2d1bbd3701e978246d8e)
- Fixed the problem of the e1000 network card driver crashing when updating the link status in the auxiliary process, and added a process type check.
  ↳ No PR: [84506cf](https://github.com/DPDK/dpdk/commit/84506cfe07326fd6ddb158f3fa57bd678751561a)
- Fixed the issue where the used ring flags in the vDPA device were not updated correctly, ensuring that flags such as VRING_USED_F_NO_NOTIFY are synchronized.
  ↳ No PR: [b3f923f](https://github.com/DPDK/dpdk/commit/b3f923fe1710e448c073f03aad2c087ffb6c7a5c)
- Fixed the post-use release issue caused by the mlx5 driver compatible matcher release order, ensuring that group information is saved before releasing group resources.
  ↳ No PR: [045da18](https://github.com/DPDK/dpdk/commit/045da18ec955f4ab5afe7697454965d40d9289a1)
- Fixed the problem of group information not being passed when translating the mlx5 driver's non-template API stream matcher mask to avoid layer recognition exceptions caused by incorrectly passed flags.
  ↳ No PR: [0250832](https://github.com/DPDK/dpdk/commit/02508320543df75a4dfabad83adfcd3353600c61)
- Fixed a memory access problem caused by the hairpin Rx queue control block being repeatedly removed from the linked list when shared and non-shared Rx queues are configured at the same time.
  ↳ No PR: [f957ac9](https://github.com/DPDK/dpdk/commit/f957ac99643535fd218753f4f956fc9c5aadd23c)
- Updated the default mask for NVGRE items for the template API and fixed its validation logic.
  ↳ No PR: [0025fd4](https://github.com/DPDK/dpdk/commit/0025fd47f2a01997bbb41d04139b220b143e6b31)
- Added validity check for flow action type in CPFL PMD to prevent incorrect use of port_representor and represented_port action.
  ↳ No PR: [8612619](https://github.com/DPDK/dpdk/commit/86126195768418da56031305cdf3636ceb6650c8)
- Fixed I/O handling of single MRVL layer in TVM model, set I/O layout to packed, and corrected calculation of quantized and dequantized data buffer addresses.
  ↳ No PR: [c4636d3](https://github.com/DPDK/dpdk/commit/c4636d36bc2cc3a370200245da69006d6f5d9852)
- Fixed the queue start and stop logic in the GVE driver so that the corresponding queue operation function can be correctly called in the DQO format.
  ↳ No PR: [7174c88](https://github.com/DPDK/dpdk/commit/7174c8891dcfb2a148e03c5fe2f200742b2dadbe)
- Fixed the issue where the EOP and checksum offload flags of chained mbufs in the GVE driver DQO sending path were not set correctly to avoid sending stagnation caused by missing flags.
  ↳ No PR: [21b1d72](https://github.com/DPDK/dpdk/commit/21b1d725e5a6cd38fe28d83c1f6cf00d80643b31)
- Fixed virtio-user not resetting used index counter of packed ring on reinitialization.
  ↳ No PR: [ff11fc6](https://github.com/DPDK/dpdk/commit/ff11fc60c5d8d9ae5a0f0114db4c3bc834090548)
- Fixed the reconfiguration failure problem caused by the lack of queue configuration pointer initialization logic during vdpa/nfp hardware initialization, and added the correct initialization steps.
  ↳ No PR: [fc470d5](https://github.com/DPDK/dpdk/commit/fc470d5e88f848957b8f6d2089210254525e9e13)
- Fixed a crash caused by dereferencing a null pointer when VF resources are not allocated due to unstable physical links.
  ↳ No PR: [57ed9ca](https://github.com/DPDK/dpdk/commit/57ed9ca61f44ffc3801f55c749347bd717834008)
- Fixed memory leak caused by invalid data when creating PDCP session.
  ↳ No PR: [9c0abd2](https://github.com/DPDK/dpdk/commit/9c0abd27c3fe7a8b842d6fc254ac1241f4ba8b65)
- Fixed the PDCP SNOW-ZUC watchdog problem and added conditional jump instructions in the relevant processing flow to ensure that the preamble processing is completed.
  ↳ No PR: [2369bc1](https://github.com/DPDK/dpdk/commit/2369bc1343fa5aac2890b2a3e12d65a2f1a2fd31)
- Enhance RFLC processing for IPsec and PDCP, adjust Response FLC pointing, enable data stashing, and fix array size definition.
  ↳ No PR: [8c8bbb1](https://github.com/DPDK/dpdk/commit/8c8bbb14560ffda3a22de37dcd6a8301dd2508da), [ac965c9](https://github.com/DPDK/dpdk/commit/ac965c980c6164b12540ecf7205f1643ee5757d6)
- Add parameter validity check for Windows EAL's rte_eal_alarm_set function, and fix test cases to run correctly on Windows.
  ↳ No PR: [7f34ecb](https://github.com/DPDK/dpdk/commit/7f34ecb6fef6cd6668d5449aabb26f1d3bce0452)
- Fixed the issue where the bnxt driver did not correctly obtain DDM information when reading SFF-8436 SFP EEPROM.
  ↳ No PR: [7b84004](https://github.com/DPDK/dpdk/commit/7b8400464f14637ed2669dbf732c256bf2447de6)
- Fixed the undefined behavior of memcpy in the net/tap driver that may pass in a null pointer, and added a length check before calling.
  ↳ No PR: [3975d85](https://github.com/DPDK/dpdk/commit/3975d85fb8606308ccdb6439b35f70e8733a78e8)
- Fixed parameter format error when registering net/sfc driver log type.
  ↳ No PR: [6cb9465](https://github.com/DPDK/dpdk/commit/6cb94658813b5fcea1e35cbb51cefb5c5b57f33d)
- In the encryption event vector scenario, fix the logic of releasing the actual mbuf pointer, and instead extract and release the correct mbuf from the encryption operation structure.
  ↳ No PR: [991b085](https://github.com/DPDK/dpdk/commit/991b0859151a461fffd114fed36905e9106e6361)
- Enable FEC automatic detection support for the E830 network card, and add adapter model judgment before firmware version checking.
  ↳ No PR: [15490b8](https://github.com/DPDK/dpdk/commit/15490b87d9a7c3cabf41b15010f356c2e6de9485)
- Fixed the issue where the CPFL parser incorrectly parsed the mask value of the next_proto_id field as a string and changed it to unsigned integer parsing.
  ↳ No PR: [8125fea](https://github.com/DPDK/dpdk/commit/8125fea74b860a71605dfe94dc03ef73c912813e)
- Set the PCAP real-time interface to non-blocking mode to comply with the non-blocking polling requirements of DPDK PMD.
  ↳ No PR: [60dd5a7](https://github.com/DPDK/dpdk/commit/60dd5a70035f447104d457aa338557fb58d5cb06)
- Add the missing legacy mailbox clearing function for the ixgbe driver, and register this operation in the mailbox parameter initialization of VF and PF.
  ↳ No PR: [1be9d85](https://github.com/DPDK/dpdk/commit/1be9d85b13f513f09d1949524255e8fbfa41020a)
- Fix the problem that the return value of ixgbe_read_eeprom is not checked in the ixgbe_stop_mac_link_on_d3_82599 function and add return value check.
  ↳ No PR: [eb3684b](https://github.com/DPDK/dpdk/commit/eb3684b191928ebb5d263e3f8ab1e309bfec099e)
- Fixed the issue where the media type of the E610 network card was incorrectly set to unknown when the link was disconnected, and moved the media type update logic to ixgbe_get_media_type_E610.
  ↳ No PR: [6c4abcb](https://github.com/DPDK/dpdk/commit/6c4abcb0f0b1d587c62dc4d0462665e4e6469b09)
- Fixed the issue where the E610 network card cannot enable all supported speeds when changing the advertised speed setting when the link is established. Instead, obtain all speeds supported by the hardware to allow any supported speed to be enabled.
  ↳ No PR: [b616e64](https://github.com/DPDK/dpdk/commit/b616e645ed1d1b2fd24b0012826c1aa4a6073da4)
- Fix the ACK processing of ixgbe mailbox, check whether other threads already hold the lock when acquiring the lock to avoid deadlock, and wait for ACK only when the CTS bit is set when sending a message to prevent timeout.
  ↳ No PR: [1f119e4](https://github.com/DPDK/dpdk/commit/1f119e4e3c36f954a353028d2ce6879b8adc8289)
- Fixed NVM access permission bug in E610 devices, ensuring that write access type is used instead of read-only access type when writing to EEPROM.
  ↳ No PR: [c83c62f](https://github.com/DPDK/dpdk/commit/c83c62fbf75a4ada591a5c7146d10fe1831f74a6)
- Add missing MAC type setting for specific X722 device variants.
  ↳ No PR: [b0bad8e](https://github.com/DPDK/dpdk/commit/b0bad8e99815d9a95614ff05cbcbd5057082b43c)
- Fixed the LED flashing problem of X722 and X557 PHY, removed the check of LED activity status, and always triggered flashing.
  ↳ No PR: [bf0183e](https://github.com/DPDK/dpdk/commit/bf0183e9ab98c946e0c7e178149e4b685465b9b1)
- Fixed the issue where another reserved track ID was not checked when loading the DDP package. Now both reserved track IDs will be filtered at the same time.
  ↳ No PR: [f646061](https://github.com/DPDK/dpdk/commit/f646061cd9328f1265d8b9996c9b734ab2ce3707)
- Fixed the problem of data changes caused by repeated dump registers in the i40e driver, by making the register list read-only to avoid data being modified during repeated dumps.
  ↳ No PR: [efc6a6b](https://github.com/DPDK/dpdk/commit/efc6a6b1facfa160e5e72f55893a301a6b27c628)
- Fix the problem of unchecked return value in i40e driver, check the return value read by debug register when parsing capability, and add type conversion.
  ↳ No PR: [7fb34b9](https://github.com/DPDK/dpdk/commit/7fb34b9141aab299c2b84656ec5b12bf41f1c21d)
- Fixed the PXE startup problem of NFP network card, reserving and locking the BAR 2.0 mapping of the expansion ROM during initialization.
  ↳ No PR: [d5c18ff](https://github.com/DPDK/dpdk/commit/d5c18ff54d964ee2e576469f2a9b5cb448fa025d)
- Fixed a potential error caused by not checking BSP command support in the NFP driver. Make sure to confirm support before sending the command.
  ↳ No PR: [e57a531](https://github.com/DPDK/dpdk/commit/e57a531c9b681d88900cb1ba1d4119559c0e5bb9)
- Fix the blocking problem of pcap driver receiving function and use pcap_next_ex instead of pcap_next.
  ↳ No PR: [f5ead8f](https://github.com/DPDK/dpdk/commit/f5ead8f84f205babb320a1d805fb436ba31a5532)
- Fixed the variable type declaration of the link speed conversion function in the NFP driver, and added a new check function.
  ↳ No PR: [93ebb1e](https://github.com/DPDK/dpdk/commit/93ebb1e57e3ff5ce34168058d73a82ae206255cc)
- Fixed the NFP representative port link speed update problem, and added a function to obtain the correct device index.
  ↳ No PR: [441839f](https://github.com/DPDK/dpdk/commit/441839f1dbe12410de553095d599a060b8a37b25)
- Fix NFP representative port link status update, remove the operation of incorrectly reading status from the control BAR, and use the correct stored link status value instead.
  ↳ No PR: [d95cf21](https://github.com/DPDK/dpdk/commit/d95cf21d2ed6630d21b5b1ca4abc40155720cd3f)
- Fixed the pointer copy problem of AVX-512 Tx release buffer in i40e driver on 32-bit platform.
  ↳ No PR: [2d040df](https://github.com/DPDK/dpdk/commit/2d040df2437a025ef6d2ecf72de96d5c9fe97439)
- Fixed the AVX-512 pointer copy problem on 32-bit systems in the ice driver.
  ↳ No PR: [da97aea](https://github.com/DPDK/dpdk/commit/da97aeafca4cdd40892ffb7e628bb15dcf9c0f25)
- Fixed the problem of AVX-512 pointer copying on 32-bit systems in the iavf driver.
  ↳ No PR: [77608b2](https://github.com/DPDK/dpdk/commit/77608b24bdd840d323ebd9cb6ffffaf5c760983e)
- Fixed the AVX-512 pointer copy issue on 32-bit systems in the idpf driver.
  ↳ No PR: [d16364e](https://github.com/DPDK/dpdk/commit/d16364e3bdbfd9e07a487bf776a829c565337e3c)
- Fixed the polynomial inversion error in hash LFSR initialization and implemented the correct inversion function.
  ↳ No PR: [ebf7f11](https://github.com/DPDK/dpdk/commit/ebf7f1188ea83d6154746e90d535392113ecb1e8)
- Fixed the out-of-bounds access problem at the end of the tbl24 table caused by the gather instruction in AVX512 search, adding an additional 4 bytes of space when allocating memory.
  ↳ No PR: [66ed178](https://github.com/DPDK/dpdk/commit/66ed1786ad067198814e9b2ab54f0cad68a58f1e)
- Fixed the VF reset timing problem in the iavf device shutdown function, delaying execution and reusing the public reset function.
  ↳ No PR: [b34fe66](https://github.com/DPDK/dpdk/commit/b34fe66ea893c74f09322dc1109e80e81faa7d4f)
- Fixed the uninitialized variable compilation warning caused by GCC optimization bug in the otx_ep_dev_mtu_set function, and added the memset initialization devinfo structure.
  ↳ No PR: [6f0f106](https://github.com/DPDK/dpdk/commit/6f0f1065cc0e20b73bf69602d1d069a4be76d126)
- Fixed the problem of cryptodev dequeue counting and limited the number of dequeued packets to MAX_PKT_BURST to prevent stack destruction.
  ↳ No PR: [88948ff](https://github.com/DPDK/dpdk/commit/88948ff31f57618a74c8985c59e332676995b438)
- Fixed a segmentation fault caused by mbuf txq being prewritten in the eventdev pipeline example.
  ↳ No PR: [f6f2307](https://github.com/DPDK/dpdk/commit/f6f2307931c90d924405ea44b0b4be9d3d01bd17)
- Fixed the issue in mlx5 driver where rte_errno was not set when ipool allocation failed.
  ↳ No PR: [e4a4087](https://github.com/DPDK/dpdk/commit/e4a40879922e4685bbbbf3503d6b388e2ee11044)
- Add syndrome and more information log output when mlx5 driver CQE error occurs, and correct the wrong CQE structure type.
  ↳ No PR: [d9acab1](https://github.com/DPDK/dpdk/commit/d9acab175085754eec705463bafa7b39b1a88e22)
- Fixed the calculation error of the register dump counter in the hns3 driver to make it consistent with the number of queue interrupt registers.
  ↳ No PR: [e9b82b4](https://github.com/DPDK/dpdk/commit/e9b82b4d54c019973ffcb5f404ba920494f70513)
- Fixed the uint16_t descriptor count overflow problem in the eth_dev_adjust_nb_desc function, by promoting the intermediate calculation to uint32_t to avoid value wrapping caused by the alignment macro.
  ↳ No PR: [30efe60](https://github.com/DPDK/dpdk/commit/30efe60d3a37896567b660229ef6a04c5526f6db)
- Fixed the problem of iavf port MAC address loss under i40e PF driver, by setting the VIRTCHNL_VF_OFFLOAD_USO flag and removing the operation of deleting all MAC addresses when the device is stopped.
  ↳ No PR: [3d42086](https://github.com/DPDK/dpdk/commit/3d42086def307be853d1e2e5b9d1e76725c3661f)
- Fix the next pointer and rearm data update logic of mbuf in the cnxk driver Rx inject package to avoid incorrectly clearing the next pointer when injecting the package.
  ↳ No PR: [0cce86f](https://github.com/DPDK/dpdk/commit/0cce86f9966909bd68ade7cfa42ffafb90470ae2)
- Fixed the problem that the MAC address cannot be set or added when there is an active VF on the PF. Now it is allowed to modify the MAC address when there is an active VF.
  ↳ No PR: [2d4505d](https://github.com/DPDK/dpdk/commit/2d4505dc6d4b541710f1c178ee0b309fab4d2ee8)
- Add device removal event callback during driver detection, move global register configuration to dev_configure, and add verification of invalid values read from hardware registers.
  ↳ No PR: [304ba46](https://github.com/DPDK/dpdk/commit/304ba46be396d2ec5ddf1d6b02793015785cd823)
- Fixed the bracket position error when calculating fman status statistics in the dpaa bus, correcting (a | b) << 32 to a | (b << 32).
  ↳ No PR: [a87a1d0](https://github.com/DPDK/dpdk/commit/a87a1d0f4e7667fa3d6b818f30aa5c062e567597)
- Fix the segfault when the DPAA driver closes and destructs the device in FMCLESS mode, improves the port cleanup logic, ensures that queue resources are released correctly and avoids accessing released memory.
  ↳ No PR: [e498f3b](https://github.com/DPDK/dpdk/commit/e498f3b51f3882c43eccb3d5b59b1d045b51c39a)
- Optimized errata A010022 processing for the LS1043A platform, and added a new mbuf reallocation function to solve FMAN stalls caused by misaligned data offsets.
  ↳ No PR: [a978a7f](https://github.com/DPDK/dpdk/commit/a978a7f6b7cdc48b4e9486fa983ac320f005b945)
- Fixed the problem of incorrect source location when the reallocate_mbuf function copies data in the dpaa driver.
  ↳ No PR: [7594caf](https://github.com/DPDK/dpdk/commit/7594cafa92189fd5bad87a5caa6b7a92bbab0979)
- Always try to refill the Rx buffer in memory-constrained scenarios to avoid driver lockup due to not receiving packets.
  ↳ No PR: [31d2149](https://github.com/DPDK/dpdk/commit/31d2149719b716dfc8a30f2fc4fe4bd2e02f7a50)
- Fixed the memory leak problem of mbuf allocation in DQ Rx queue, ensuring that a buffer is no longer leaked every time the queue is stopped/started.
  ↳ No PR: [265daac](https://github.com/DPDK/dpdk/commit/265daac8a53aaaad89f562c201bc6c269d7817fc)
- Fix IRQ reconfiguration issue: Before adjusting the IRQ size, unregister the IRQ of the SSO device and NPA to clean up the stale IRQ handles.
  ↳ No PR: [758b58f](https://github.com/DPDK/dpdk/commit/758b58f06a43564f435e3ecc1a8af994564a6b6b)
- Fixed a crash caused by rte_pktmbuf_read() returning NULL when dumpcap processes jumbo frames in legacy pcap mode.
  ↳ No PR: [5c0f970](https://github.com/DPDK/dpdk/commit/5c0f970c0d0e2a963a7a970a71cad4f4244414a5)
- Fix the boundary condition error in the GVE driver RX refill logic, avoid memory corruption caused by invalid tail pointer, and simplify the refill process.
  ↳ No PR: [52c9b40](https://github.com/DPDK/dpdk/commit/52c9b4069b216495d6e709bb500b6a52b8b2ca82)
- Added a read memory barrier to the GVE driver's TX and RX completion processing to ensure that the NIC has completed ownership transfer before reading descriptor data to avoid reading stale data.
  ↳ No PR: [f8fee84](https://github.com/DPDK/dpdk/commit/f8fee84eb48cdf13a7a29f5851a2e2a41045813a)
- Fixed a memory leak problem caused by rte_eal_cleanup() not being called when app/procinfo exits in certain modes.
  ↳ No PR: [8a171e5](https://github.com/DPDK/dpdk/commit/8a171e52ed8b26f768ced79a22286914ebd30180)
- Check the return value of APIs such as rte_eth_dev_info_get in the ethdev_show function, and return directly if an error occurs to avoid using undefined data.
  ↳ No PR: [fe02b98](https://github.com/DPDK/dpdk/commit/fe02b98cd3925d455731f0201030c587a387eef0)
- Fix the problem of using freed memory for tracing after memzone is released: move the tracing call to before the release operation.
  ↳ No PR: [a306620](https://github.com/DPDK/dpdk/commit/a306620e357af9d1e2b99a93fabc40b382c3fa88)
- Fixed the mismatch problem of device structure memory release function in BCMFS encryption driver: change the wrong free() to rte_free().
  ↳ No PR: [b1703af](https://github.com/DPDK/dpdk/commit/b1703af8e77d9e872e2ead92ab2dbcf290686f78)
- Fixed the problem of memory release function mismatch during device detection in dma/idxd driver: replace free with rte_free.
  ↳ No PR: [91b026f](https://github.com/DPDK/dpdk/commit/91b026fb46d987e68c1152b0bb5f0bc8f1f274db)
- Fixed the free function mismatch problem caused by dereferencing a null pointer during error cleanup in the event/cnxk port configuration.
  ↳ No PR: [db92f4e](https://github.com/DPDK/dpdk/commit/db92f4e2ce491bb96605621cdd6f6251ea3bde85)
- Fix the mismatch of memory release functions in the vhost example: replace the incorrectly used free() with rte_free() to avoid memory pool damage.
  ↳ No PR: [ae67f7d](https://github.com/DPDK/dpdk/commit/ae67f7d0256687fdfb24d27ee94b20d88c65108e)
- Fix the release order problem when mempool is created in the cnxk network card driver to avoid use-after-free caused by accessing its configuration after mempool is released.
  ↳ No PR: [c024de1](https://github.com/DPDK/dpdk/commit/c024de17933128f37b1dfe38a0fae9975be1b104)
- Fixed the problem of mismatch of release functions when converting cBPF to eBPF fails: replace free() with rte_free().
  ↳ No PR: [a3923d6](https://github.com/DPDK/dpdk/commit/a3923d6bd5c0b9838d8f4678233093ffad036193)
- Fixed the use-after-free issue when filter clearing in the e1000 driver: move the release operation to after all filter member accesses.
  ↳ No PR: [58196dc](https://github.com/DPDK/dpdk/commit/58196dc411576925a1d66b0da1d11b06072a7ac2)
- Fixed the use-after-free problem caused by the debug log in the net/sfc driver being accessed after the object is released: move the debug log to before the release operation.
  ↳ No PR: [757b0b6](https://github.com/DPDK/dpdk/commit/757b0b6f207c072a550f43836856235aa41553ad)
- Fixed invalid free call in cpfl driver JSON parser due to incorrect release of non-heap allocated memory.
  ↳ No PR: [1c20cf5](https://github.com/DPDK/dpdk/commit/1c20cf5be5c8b3e09673a44da2ce532ec0f35236)
- Fixed the double release problem when streams are destroyed in the net/nfp driver to avoid heap corruption caused by repeated calls to rte_free.
  ↳ No PR: [fae5c63](https://github.com/DPDK/dpdk/commit/fae5c633522efd30b6cb2c7a1bdfeb7e19e2f369)
- Fixed the use after release problem caused by continued access after releasing the node when traversing the sensor linked list in raw/ifpga/base: use safe traversal macro instead.
  ↳ No PR: [1198622](https://github.com/DPDK/dpdk/commit/11986223b54d981300e9de2d365c494eb274645c)
- Fixed a use-after-free issue that could be caused by checking rte_memzone_free return value in QAT device detection.
  ↳ No PR: [1af60a8](https://github.com/DPDK/dpdk/commit/1af60a8ce25a4a1a2ae1da6c00f432ce89a4c2eb)
- Fixed the memory allocation and release mismatch problem of interrupt configuration in ifpga driver: use rte_calloc and rte_free instead of calloc and free.
  ↳ No PR: [d891a59](https://github.com/DPDK/dpdk/commit/d891a597895bb65db42404440660f82092780750)
- Fixed use-after-free issue in baseband/la12xx driver: empty pointer after releasing it to avoid repeated release.
  ↳ No PR: [6ffb344](https://github.com/DPDK/dpdk/commit/6ffb34498913f84713e98d6a2a21d2a86028a604)
- Fixed the use after free problem caused by macro definition errors in mailbox initialization.
  ↳ No PR: [4baf54e](https://github.com/DPDK/dpdk/commit/4baf54ed9dc87b89ea2150578c51120bc0157bb0)
- Fixed the error in the return value check of functions such as link status setting, port power on and off, pause frame setting and FEC mode setting in the NFP driver to ensure that the three-way return value is correctly judged.
  ↳ No PR: [0ca4f21](https://github.com/DPDK/dpdk/commit/0ca4f216b89162ce8142d665a98924bdf4a23a6e), [1580387](https://github.com/DPDK/dpdk/commit/1580387e07cf0facf695db2b8bc23f1238810c59), [4bb6de5](https://github.com/DPDK/dpdk/commit/4bb6de512fbc361e16d5a7a38b704735c831540d), [47fc5e4](https://github.com/DPDK/dpdk/commit/47fc5e4ee99bd8efa587ac6c6e7966318de4da1c)
- Fixed the problem of accessing freed memory in the ACC baseband driver: removed the soft output bypass rate matching function, and automatically reset the data_len of the HARQ output buffer to avoid errors reported by the application without explicit reset.
  ↳ No PR: [a090b8f](https://github.com/DPDK/dpdk/commit/a090b8ffe73ed21d54e17e5d5711d2e817d7229e), [2fd167b](https://github.com/DPDK/dpdk/commit/2fd167b61bc6c6f40a6c04085caa56be40451e2a), [6cdecfc](https://github.com/DPDK/dpdk/commit/6cdecfc1f56bec8d799376a5f8c05a4603c4d6d3)
- Updated the FPGA version, fixed coding style issues, and resolved multiple issues such as null pointer dereferences, resource leaks, array out-of-bounds problems discovered by Coverity.
  ↳ No PR: [a1c2c9d](https://github.com/DPDK/dpdk/commit/a1c2c9db7cfeaeb6925141428b4d356c4bdb9f6f), [3de5fe7](https://github.com/DPDK/dpdk/commit/3de5fe7996a399fcd92888172a733eed315d1d0d)
- Fixed the initialization check of the CPPC driver in the power management library so that it can correctly identify and initialize CPPC mode.
  ↳ No PR: [35220c7](https://github.com/DPDK/dpdk/commit/35220c7cb3aff022b3a41919139496326ef6eecc)
- Fixed the use after free problem when releasing the queue in the net/nfb driver, and moved the rte_free call to after the empty operation.
  ↳ No PR: [76da983](https://github.com/DPDK/dpdk/commit/76da9834ebb6e43e005bd5895ff4568d0e7be78f)
- Limits the number of queues allowed in multi-process messages of the TAP device to not exceed the maximum number of queues supported by the device, and fixes the problem of over-limiting the number of queues that may be caused by an increase in the maximum number of MP file descriptors.
  ↳ No PR: [288649a](https://github.com/DPDK/dpdk/commit/288649a11a8a332727f2a988c676ff7dfd1bc4c5)
- Fixed the memory leak problem in NFP VF initialization, corrected the memory allocation method and error handling path.
  ↳ No PR: [9fa4d03](https://github.com/DPDK/dpdk/commit/9fa4d03f746d84d8ecbb3ffb2b19f110cf79baae)
- Added queue ID verification in debug mode in rte_eth_tx_done_cleanup function.
  ↳ No PR: [707f50c](https://github.com/DPDK/dpdk/commit/707f50cef003a89f8fc5170c2ca5aea808cf4297)
- Fixed the problem in the flower firmware that the PF speed was not notified, causing the VF speed to be unavailable, and added the logic to notify the firmware of the PF speed.
  ↳ No PR: [2254813](https://github.com/DPDK/dpdk/commit/2254813795099aa6c05caed5e8c0dcc7a8f03b4e)
- Fixed an issue where the NFP IPsec driver no longer sets the IPv6 flag in transport mode.
  ↳ No PR: [4f64ebd](https://github.com/DPDK/dpdk/commit/4f64ebdd41ce8bb60dba95589a5cc684fb9cb89c)
- Added workarounds for hardware errata ERR050757 and ERR050265 to the DPAA QDMA driver to prevent QDMA hangs or stalls by setting stride mode and prefetch reads.
  ↳ No PR: [bdcb782](https://github.com/DPDK/dpdk/commit/bdcb782a460108c894798ae6a1e04dd1df94c29e), [8c53b9b](https://github.com/DPDK/dpdk/commit/8c53b9b7954d6beb16d2497a28005a7d9c5bb1c8)
- When sending data packets, force VLAN offloading on 802.1Q data packets, stripping VLAN tags and passing VLAN information through the VSP protocol.
  ↳ No PR: [06c968f](https://github.com/DPDK/dpdk/commit/06c968f9ba8afeaf03b60871a453652a5828ff3f)
- Fixed the problem of tunnel flow rules supporting multiple tunnel headers in the hns3 driver, and now returns an error when passing multiple tunnel headers.
  ↳ No PR: [8887c20](https://github.com/DPDK/dpdk/commit/8887c207b9373a1875031c5346706f698322d66d)
- Under multiple PF firmware, ignore useless PF representative port control messages to avoid error processing.
  ↳ No PR: [99da56d](https://github.com/DPDK/dpdk/commit/99da56de8c8402c38ca9985c7dd881ae33fd4a19)
- Fixed the delay problem of ixgbe network card link status query on FreeBSD, and removed the forced waiting logic so that no-wait requests can be returned immediately.
  ↳ No PR: [f775386](https://github.com/DPDK/dpdk/commit/f775386d92d68e534600fcff3fc4bcaa30d3e68c)
- Fixed the integer overflow problem caused by the register offset variable type in the hns3 driver to avoid data truncation.
  ↳ No PR: [b1fefe4](https://github.com/DPDK/dpdk/commit/b1fefe40550836b58c4ec50dce14a6e6dbda8499)
- Fixed the problem that when the hns3 driver obtains multiple module register values at one time, the register value is incorrect due to the data pointer offset error.
  ↳ No PR: [013fdd2](https://github.com/DPDK/dpdk/commit/013fdd2d7b319e6a35d966f375e33ee330d9ccb5)
- Fixed the error caused by repeated stop of the flow director queue in the ice driver. When stopping the queue, check whether it has stopped to avoid secondary stop failure.
  ↳ No PR: [7b230d4](https://github.com/DPDK/dpdk/commit/7b230d43e8061bdaba02a41f601bb8e0b5dbff03)
- By querying the scheduling tree node limit, additional upper limit constraints are placed on the number of ice-driven queues to avoid exceeding the hardware scheduling capability.
  ↳ No PR: [5117ebf](https://github.com/DPDK/dpdk/commit/5117ebfcc0d52bdf13eb5e04997293287fe69f1f)
- Update getwork write data when the device is reconfigured to avoid using outdated configurations.
  ↳ No PR: [6dad0bb](https://github.com/DPDK/dpdk/commit/6dad0bb5c8621644beca86ff5f4910a943ba604d)
- Fixed the memory leak problem of meter profile table when meter is not enabled, the table is only allocated when meter is enabled.
  ↳ No PR: [4dd46d3](https://github.com/DPDK/dpdk/commit/4dd46d38820e0bf5e74f99b84f4b098d1b7220dd)
- Fixed the method of obtaining the DPNI link status and used the dpni_get_link_cfg API to obtain static configuration data. This solved the problem that the link status was displayed as DOWN due to the flow control configuration after the SFP module was connected.
  ↳ No PR: [263377b](https://github.com/DPDK/dpdk/commit/263377be771f09a20197c30ce83ea44922a4e8fe)
- Release the VFIO group file descriptor when adding the VFIO group fails to avoid resource leaks.
  ↳ No PR: [3b5f8df](https://github.com/DPDK/dpdk/commit/3b5f8dfab7e85c180cc64e130c33cee4b5d43c28)
- Fixed Coverity warning in QBMAN debug function, avoid null pointer dereference by introducing temporary variable to check return value, and add type conversion to prevent integer overflow.
  ↳ No PR: [051f418](https://github.com/DPDK/dpdk/commit/051f4185f98faa964b6a965b2e8e7b2da68969de)
- Fixed the problem of the conflict between miss flow ID macro name and enumeration, and set the default miss flow ID to 0.
  ↳ No PR: [068be45](https://github.com/DPDK/dpdk/commit/068be45fb5363dc9f79821a133f13d8bd781d26d)
- Fixed the memory corruption problem of the traffic management module in the net/dpaa2 driver and changed the queue configuration array size from a fixed value to the actual number of queues.
  ↳ No PR: [d77cb0c](https://github.com/DPDK/dpdk/commit/d77cb0c44cf6b68dc71684bd302fd3138b36e5f1)
- Fixed the issue of double release of aging resources during the NPC dismantling process.
  ↳ No PR: [d1066ea](https://github.com/DPDK/dpdk/commit/d1066ea60bcb5cbd3cdcc06d21afc232d8c08407)
- Fixed the data corruption problem caused by incorrect processing of segment data when eswitch processes multi-segment VxLAN packets.
  ↳ No PR: [cfd5db0](https://github.com/DPDK/dpdk/commit/cfd5db0dcdb9005a3b82c628f0ebd8677ff85ec6)
- Fixed the issue where the reconnection log mapping was not correctly released in the wrong path when creating the VDUSE device.
  ↳ No PR: [47458d1](https://github.com/DPDK/dpdk/commit/47458d13d44af88f0bb3af0a327a7b06784f8480)
- Fixed the TOCTOU vulnerability when creating VDUSE devices, changed the file existence check to directly opening the device file, and adjusted the parameters and error handling path of the reconnection log check function.
  ↳ No PR: [29ab97d](https://github.com/DPDK/dpdk/commit/29ab97dd8316b6ecbb1753202b87ace1c854d445)
- Fixed the file descriptor leak caused by startup failure when reconnecting the VDUSE device, and restructured the reconnection startup logic into an independent function.
  ↳ No PR: [952e494](https://github.com/DPDK/dpdk/commit/952e49451600bea61214249815f241167c7c456d)
- Fixed the missing error handling in VDUSE reconnection log version check, and extracted the relevant check logic into independent functions to simplify the device creation code.
  ↳ No PR: [69d2e25](https://github.com/DPDK/dpdk/commit/69d2e2567b04833dbb1e92f572d6d97943faee9c)
- Fixed the problem that in the template table inserted by index and with pattern matching, packets that miss the rules are mistakenly routed to the lower priority table. Now they are changed to the default miss route.
  ↳ No PR: [e87a9b6](https://github.com/DPDK/dpdk/commit/e87a9b609fb1eea5ebc67eca3eb379beba967e7f)
- Fix endianness handling of 3DES-CTR on big-endian CPUs, remove unconditional byte swapping and use explicit big-endian conversion instead, and remove unused ctr_inc helper function.
  ↳ No PR: [97afd07](https://github.com/DPDK/dpdk/commit/97afd07ca79c7270480a65febd7f616a4c0b07ca)
- Fixed a crash caused by the adapter_stopped state not being properly initialized when the vmxnet3 driver calls the shutdown function after configuration failure.
  ↳ No PR: [439847c](https://github.com/DPDK/dpdk/commit/439847c154ccf05e1a8bbb955c552921514d31e2)
- Fix the verification of raw encap action in mlx5 driver, separate the verification logic of SWS and HWS, and check different parameters respectively.
  ↳ No PR: [db830c4](https://github.com/DPDK/dpdk/commit/db830c40bc8296fc013d9328255192fb589d858a)
- Add a check on the return value of rte_pcapng_add_interface in the dumpcap application, and exit and output an error message when it fails.
  ↳ No PR: [c79900e](https://github.com/DPDK/dpdk/commit/c79900e31e3e5a16c7f5410d0800315a0491ccad)
- Fixed the problem of GRE flow item item mask not being initialized when translating root table.
  ↳ No PR: [25ab2cb](https://github.com/DPDK/dpdk/commit/25ab2cbba31d937e685f0cf9ecce0c680cc4083e)
- Fixed range definer error recovery: when an invalid matcher range definition is detected, correctly set rte_errno to EINVAL to ensure that the calling function can learn the error status.
  ↳ No PR: [84c3090](https://github.com/DPDK/dpdk/commit/84c3090e517641027a7b64fe5bb6eccbcfa05a6d)
- Fixed the problem of using integer return values during counter initialization, and instead used the rte_flow_error structure to provide more detailed error information.
  ↳ No PR: [d46f3b5](https://github.com/DPDK/dpdk/commit/d46f3b525aafbb4c6c88d9c61b445eb0d93d2149)
- Fix non-template flow action validation logic, only perform action template validation in template mode.
  ↳ No PR: [ee76b17](https://github.com/DPDK/dpdk/commit/ee76b173b2e93ab4a0c9b4153191965259dae972)
- Fix SWS meter object state initialization to ensure ASO object availability is tracked correctly.
  ↳ No PR: [0c37d8f](https://github.com/DPDK/dpdk/commit/0c37d8f7ba2cac289896de024d9c58a65ba3ece9)
- Fixed the mapping error from Traffic Class field to Type of Service field in NAT64 IPv6 to IPv4 conversion to ensure that QoS information is correctly retained.
  ↳ No PR: [d3e4699](https://github.com/DPDK/dpdk/commit/d3e46998443e47e48bea30e116c6330bfdf5302c)
- Fixed the problem of incorrect parameters being passed when calling indirect list flow action callbacks. Make sure to pass a single flow action instead of an action list.
  ↳ No PR: [e53e4c3](https://github.com/DPDK/dpdk/commit/e53e4c39d2514667a7065cb0dd2d8fe3dcd843e3)
- Fixed CQE index error when getting shared Rx queue port number in mlx5 vectorized Rx routine.
  ↳ No PR: [3638f43](https://github.com/DPDK/dpdk/commit/3638f431b9ff39003e31c3a761d407e04b25576a)
- Allow automatically stopping and restarting a port to apply TM topology when it is up, instead of returning an error directly.
  ↳ No PR: [6412a8f](https://github.com/DPDK/dpdk/commit/6412a8f741e81145479d0ea264e28db55d5a5eac)
- Fixed an issue where the MLX5 counter query loop might get stuck, removed the inner loop in __mlx5_hws_cnt_svc(), and added debug logs and documentation.
  ↳ No PR: [c0e2996](https://github.com/DPDK/dpdk/commit/c0e29968294c92ca15fdb34ce63fbba01c4562a6)
- Fixed the alignment of the virtual queue structure in the ntnic driver, changing __rte_aligned(8) to __rte_packed.
  ↳ No PR: [f2a3bf9](https://github.com/DPDK/dpdk/commit/f2a3bf9ef7b33ca001fa9204d29eac2f718b01ce)
- Fixed the problem that the length of modular exponentiation and modular inversion operation results in QAT asymmetric encryption PMD is not set.
  ↳ No PR: [5b2fe7e](https://github.com/DPDK/dpdk/commit/5b2fe7ef3c1b731f086d9454262a530a082b0441)
- Fixed the problem of incorrect calculation of received data length when hardware timestamp is enabled in the igc driver: subtract the timestamp header length in non-dispersed mode, adjust the data offset of subsequent mbuf in dispersed mode, to avoid packet length anomalies and inter-segment data loss.
  ↳ No PR: [4e08d33](https://github.com/DPDK/dpdk/commit/4e08d335554ec6d975ded8a7badf81e0edb39234)
- Fixed the issue where the port index in the NFP network driver was not assigned correctly.
  ↳ No PR: [fbbfcc1](https://github.com/DPDK/dpdk/commit/fbbfcc19e3acb5cbd0026d71399f084f4d55aeeb)
- Fixed the problem in the txgbe driver that the SWFW mbox could not write to the register when compiling with a higher version of GCC, which was solved by adding a register refresh operation.
  ↳ No PR: [e389504](https://github.com/DPDK/dpdk/commit/e389504ed46d84c6a5a6a32b09d6750a182f8725)
- Fixed the issue where the txgbe driver incorrectly declared the outer UDP checksum offload capability, and removed the offload flag which is not supported by the hardware.
  ↳ No PR: [25fe1c7](https://github.com/DPDK/dpdk/commit/25fe1c780d39ea3637ba8407f6e9a9800135becd)
- Fixed the issue where the driver loading bit in the txgbe driver is lost after hardware reset. The bit is reset after reset to notify the firmware that the driver has been loaded, and is cleared when the device is turned off.
  ↳ No PR: [0a8f064](https://github.com/DPDK/dpdk/commit/0a8f064bbc2cf4978857eae84e86c6b2c9e65feb)
- Enable the Tx descriptor error interrupt in the txgbe driver to handle non-fatal and fatal errors; also fix the problem of mismatch between packet length and packet type to prevent excessive hardware checking.
  ↳ No PR: [0eabdfc](https://github.com/DPDK/dpdk/commit/0eabdfcd4af44fd8b32ccdeb3d01c256572a52d0)
- Add length check for Tx packets in txgbe driver, set invalid packet length to default value in simple Tx path, and directly discard invalid packets in feature Tx path to avoid TDM fatal errors.
  ↳ No PR: [7029832](https://github.com/DPDK/dpdk/commit/7029832c24f051032798c1cfaeb137ab886db094)
- Add sending packet length check for ngbe network card driver, set the illegal packet length to the default value in the simple sending path, directly discard illegal packets and increase the error count in the complete sending path.
  ↳ No PR: [8d75bf0](https://github.com/DPDK/dpdk/commit/8d75bf037aa29c865ce7ce1c891519ec5118f9df)
- Fix ngbe driver loading bit, reconfigure after hardware LAN reset to notify firmware that driver is loaded, and clear the bit when device is shut down.
  ↳ No PR: [cb7be5b](https://github.com/DPDK/dpdk/commit/cb7be5b510ef0995fa171832f0e0994f667e2161)
- Fixed the problem that data packets may not be received after the link status changes in the ngbe driver, and reconfigured the MAC Rx related registers.
  ↳ No PR: [b8d52e1](https://github.com/DPDK/dpdk/commit/b8d52e1084a17c7ef83624f3bbd11a090e7b2267)
- Fixed the issue in the ngbe driver that caused shared interrupts in legacy or MSI mode to cause interrupts to fail to be re-enabled, by reading the shared interrupt status and ensuring that the interrupt is re-enabled.
  ↳ No PR: [68f04c0](https://github.com/DPDK/dpdk/commit/68f04c0aa79316de333441e7efdadd2876412ffa)
- Fixed the problem that the ngbe network card cannot configure VLAN stripping and offloading after the device is started. The configuration is now only performed when the device is stopped.
  ↳ No PR: [baca8ec](https://github.com/DPDK/dpdk/commit/baca8ec066dc6fdc42374e8eafd67eecfd6c9267)
- Fixed the out-of-bounds problem of the statistics array in the vmxnet3 driver caused by the increase in the number of queues in virtual hardware version 6, by expanding the statistics array and limiting the access range of each queue counter.
  ↳ No PR: [d3a229d](https://github.com/DPDK/dpdk/commit/d3a229dd493abcb29d5717c5ce37e0a0bc1777c4)
- Fixed the problem that the device information in the vmxnet3 driver did not correctly reflect the virtual hardware version 6 supporting a larger MTU. The maximum MTU is now dynamically set according to the hardware version.
  ↳ No PR: [a4b83a7](https://github.com/DPDK/dpdk/commit/a4b83a747d7d21c6d61b9ae69d39db5e1c700dcd)
- Fixed incorrect template macro used in CN9K dual worker slot function.
  ↳ No PR: [49a841e](https://github.com/DPDK/dpdk/commit/49a841e1983acfaefdfe19957166d985ad921867)
- Fixed the issue where the driver incorrectly searches for DDP packages in the root directory when the DDP search path is empty. It will now correctly check whether the path value length is greater than zero.
  ↳ No PR: [14d66da](https://github.com/DPDK/dpdk/commit/14d66da59b4a29f23f34315bf51616f5e90b16ad)
- Add reference counting management for shared Rx queue control structures to avoid use-after-free issues, and migrate the management of queue control structures from device private data to the shared context.
  ↳ No PR: [3c9a82f](https://github.com/DPDK/dpdk/commit/3c9a82fa6edc06c1d4dc6c0ac53609002c4d9462)
- Fixed an issue in ICE PMD where the Ready bit was not checked when reading the PHY timestamp, resulting in an incorrect Tx timestamp. Now the timestamp is only read after the Ready bit is set.
  ↳ No PR: [b55051d](https://github.com/DPDK/dpdk/commit/b55051d1c59d8670fd59423b5af529936cf5554d)
- Fixed the problem that the key was not set correctly during ECDSA session initialization in the QAT driver, and added key memory allocation and error return in session_set_ec.
  ↳ No PR: [20e633b](https://github.com/DPDK/dpdk/commit/20e633b0ca15539b682539a665e8d3dc0dc2c899)
- Fixed the interrupt mode of E610 devices and added support for E610 devices in the queue interrupt map.
  ↳ No PR: [42e7a15](https://github.com/DPDK/dpdk/commit/42e7a159f0d959f2c9e41b0b76ad281124125327)
- Fixed the array out-of-bounds reading problem caused by send_packets_multi() being unable to handle invalid port numbers in ACL mode. Check whether all target ports are valid before calling, otherwise fall back to send_packets_single().
  ↳ No PR: [795b634](https://github.com/DPDK/dpdk/commit/795b63416b96aac4358a0b01f59d83797b94e522)
- Fixed the problem of offset 1 in the calculation of the end address of ring memory allocation in the baseband/acc driver, ensuring it is aligned with 64MB.
  ↳ No PR: [0c57098](https://github.com/DPDK/dpdk/commit/0c5709824b531e83b36ed91852cea98b1cb292e1), [6aea11c](https://github.com/DPDK/dpdk/commit/6aea11c12484489f95549a3b952e98c0a32c5c55)
- Fixed the problem caused by the read-only HWRM request buffer when deleting WC TCAM multi-slices, forcing the use of DMA channels to send setup messages; and added an error log for the tunnel port allocation API.
  ↳ No PR: [78dcdb8](https://github.com/DPDK/dpdk/commit/78dcdb821cb81f4abddfd4abc0192e238d4bfcec)
- Fixed data corruption issue caused by TCAM manager not resetting the maximum entry counter when the session is closed, and clearing the counter to zero on session initialization.
  ↳ No PR: [0bee506](https://github.com/DPDK/dpdk/commit/0bee506e9ec6bca60111b63e631c84080b14aec2)
- Fix Thor TF EM key size check, correct EM insert record size from 80 bytes to 96 bytes to support key inserts larger than 601 bits.
  ↳ No PR: [912abed](https://github.com/DPDK/dpdk/commit/912abed4250c792214886880fa0b93b7712fba21)
- Fixed the problem of incorrect entries being written due to slice number calculation errors when moving HA entries. Make sure the slice number is correct by copying entry_size before moving.
  ↳ No PR: [1190f2f](https://github.com/DPDK/dpdk/commit/1190f2f8d5abf82c843ad071ad4c7d0aea202cce)
- Support action reading and clearing, implement stream query count reset after reading in ULP, and fix bnxt_mpc_xmit() message padding to 16 byte multiples.
  ↳ No PR: [8499b45](https://github.com/DPDK/dpdk/commit/8499b456145375f3f93c04b1bf6a783ab29542c3)
- Update template files to enable recipe ID generation, and fix segfault in wildcard recipe handling.
  ↳ No PR: [ab2e230](https://github.com/DPDK/dpdk/commit/ab2e230e7563cbed2a708e4d1d994e937d9f7cc5)
- Fixed the wildcard recipe segfault in the bnxt driver, added recipe ID generation support, ported the default_non_ha resource code, and adjusted the debug log level.
  ↳ No PR: [61a7ca1](https://github.com/DPDK/dpdk/commit/61a7ca1f6f874286e6787b52c867f1bb25f4cd42)
- Fixed the lock scope problem of the parent-child flow counter in the bnxt driver, added reference count maintenance, and fixed the hash table name conflict.
  ↳ No PR: [8782e4d](https://github.com/DPDK/dpdk/commit/8782e4de3ef2e55bd4aed98dc18e26d2bfc83868)
- Updated Thor and Thor2 template databases, changed VF representor mode to dynamic, and fixed Thor2's L2 TCAM record priority issue.
  ↳ No PR: [f5760d7](https://github.com/DPDK/dpdk/commit/f5760d720f67863da68ad024ea89f23173bc2cf8)
- Fixed the problem that the hardware flow table in the hns3 driver cannot be fully utilized, by enabling the rte_hash extensible bucket table feature.
  ↳ No PR: [b8e60c3](https://github.com/DPDK/dpdk/commit/b8e60c33168a2999604c17322dd0198a6746428f)
- Fixed an issue in CPFL PMD forwarding traffic to physical ports, removing incorrect check for represented_port action.
  ↳ No PR: [b0e6aff](https://github.com/DPDK/dpdk/commit/b0e6aff62efa4bcc23f64b80b91709bef73e6d79)
- Added a check for the data length of a single buffer packet in the IAVF driver's send preparation function to ensure that it is consistent with the packet length.
  ↳ No PR: [4523e07](https://github.com/DPDK/dpdk/commit/4523e0753b243066357f98fd9739fde72605d0fb)
- Fixed the logic error in the bnx2x driver that the single interrupt mode enable condition is always true.
  ↳ No PR: [fb6b0e9](https://github.com/DPDK/dpdk/commit/fb6b0e9a36326a4f13f496b00f7f92aaffe1d5f4)
- Fixed an infinite loop that could occur when starting the bnx2x driver, by correctly initializing the loop condition variables according to the chip type.
  ↳ No PR: [a47272b](https://github.com/DPDK/dpdk/commit/a47272b052dd1c8c571a1c0b89b56aaa3ebf4351)
- Fixed the memory access error caused by structure misalignment in the mlx5 driver, and added alignment and packaging attributes.
  ↳ No PR: [9096753](https://github.com/DPDK/dpdk/commit/90967539d0d1afcfd5237ed85efdc430359a0e6b)
- Fixed the fallthrough problem of the switch statement in the e1000 network card driver basic code to avoid potential logic errors.
  ↳ No PR: [11a5adb](https://github.com/DPDK/dpdk/commit/11a5adba21237d5905bcb3f5f695aa5a5cfecd9f)
- Added null pointer check in Tx scheduler node settings to avoid null pointer dereference issues caused by invalid node IDs.
  ↳ No PR: [19a02bc](https://github.com/DPDK/dpdk/commit/19a02bc972759a0fc1f40753ccfe0d8152d68d1e)
- Fixed an out-of-bounds write issue in the eventdev Rx adapter due to array index underflow when the number of interrupts is zero.
  ↳ No PR: [952b24b](https://github.com/DPDK/dpdk/commit/952b24bd0475450e548d4aafae7d8cf48258402b)
- Fixed the problem that the FQ lock was not released during error handling in the dpaa bus to avoid abnormal locking of resources.
  ↳ No PR: [c7c3a32](https://github.com/DPDK/dpdk/commit/c7c3a329750b81bdaeb3f7ceffac0ec3a65f61f8)
- Fixed a large number of interrupts caused by GPIO tx_fault interrupt not being cleared.
  ↳ No PR: [916aa13](https://github.com/DPDK/dpdk/commit/916aa13f4a198aebf5383f9680cb5cd527518f2c)
- Fixed the displacement bucket selection logic when adding hash table members, and fixed the problem of always using the main bucket due to misuse of the logical AND operator.
  ↳ No PR: [33f5b0d](https://github.com/DPDK/dpdk/commit/33f5b0dcb11580be8091f3b589845e512008e2f0)
- Fixed the issue in the i40e driver that i40e_get_outer_vlan() did not check the return value of the register read, changed its return type to int and returned the VLAN TPID through the output parameter, and updated the call site to add error handling; in addition, the parameter passing method when comparing and copying IPv6 addresses was corrected.
  ↳ No PR: [c11c52d](https://github.com/DPDK/dpdk/commit/c11c52dd5d2a19c97616ac32a1d4911c48f157d4)
- Fixed the deadlock problem in the vhost Rx asynchronous path caused by incorrect use of read locks to release write locks.
  ↳ No PR: [22aa9a9](https://github.com/DPDK/dpdk/commit/22aa9a9c7099e1f4b297899c33b4fea1131d3ac7)
- Fixed the issue where the flow update command in testpmd did not correctly update the age action context. Now the flow aged destroy command can be executed normally.
  ↳ No PR: [5b7d82e](https://github.com/DPDK/dpdk/commit/5b7d82e817afad123c8ff5f9f0e53ef36fadac3d)
- Fixed an issue where the first stream was incorrectly deleted in the cleanup process when asynchronous stream creation failed, and ensured that the released stream ID is not accessed after destroying the stream.
  ↳ No PR: [098f949](https://github.com/DPDK/dpdk/commit/098f949f8a70f7618f5390f9c1e9edfb9e5469c4)
- Fixed the problem that the offload flags of mbuf in the bnxt driver were not reset, and changed it to direct assignment to avoid application exceptions due to residual flag bits.
  ↳ No PR: [3e9a43b](https://github.com/DPDK/dpdk/commit/3e9a43bad2ce1413be2456c7e53945444aac99f9)
- Fixed F1F2 VXLAN parent-child flow counter accumulation issue on Thor2 platform, and added device status check in TF tunnel release API to skip completed resource release.
  ↳ No PR: [a089734](https://github.com/DPDK/dpdk/commit/a089734a026a316994674e3f405ee4d56a114efc)
- Fixed an issue where representative streams were not deleted during VFR cleanup, and fixed statistics counter thread deadlock.
  ↳ No PR: [67ad400](https://github.com/DPDK/dpdk/commit/67ad40007cd6bb6ce9f0b3eefe2af611848d10dc)
- Fix the problem in the pcapng module that may cause unaligned access due to the use of uint8_t buffer, and change the buffer declaration to uint32_t type.
  ↳ No PR: [0cbf275](https://github.com/DPDK/dpdk/commit/0cbf27521b0d6e7cb79f41a5e699d82562b09c03)
- Fixed an issue where the values were not copied correctly to the flow handler when modifying IPv4 and IPv6 DSCP fields.
  ↳ No PR: [9141a19](https://github.com/DPDK/dpdk/commit/9141a191d40b9cc7c669588cc6dad4c8bafba373)
- Fixed the PTP initialization problem of E610 devices in ixgbe driver, and added missing E610 branch processing in the functions of reading system time, receiving/transmitting timestamp and startup time counter.
  ↳ No PR: [d797d98](https://github.com/DPDK/dpdk/commit/d797d98e6313127e5735e069c3e7057b49205bb7)
- Fixed the RSS hash value exception caused by the byte order reversal of Toeplitz keys during FPGA programming, and corrected the byte order processing of masks.
  ↳ No PR: [ef6ed52](https://github.com/DPDK/dpdk/commit/ef6ed529b220b74b5ca52bc7619f21522cd6a874)
- Fixed the issue where the timestamp of the ixgbe driver is initialized to system time instead of zero when PTP is enabled, and fixed the calling issue of the mailbox read operation when MinGW is compiled.
  ↳ No PR: [d2394b2](https://github.com/DPDK/dpdk/commit/d2394b2790f36becf3fef5ff979a988855f1024f)
- Fixed RSS redirection table configuration for E610 devices in ixgbe driver, adding correct table size and register address.
  ↳ No PR: [a80016c](https://github.com/DPDK/dpdk/commit/a80016c8b8d1995db5853b980cc8a7af6b5ce863)
- Fixed the issue in the ixgbe driver that the E610 device does not support loopback mode, and added judgment on E610 in the loopback support check.
  ↳ No PR: [62fd579](https://github.com/DPDK/dpdk/commit/62fd579fcd15f13f2bed84a003d284d04ddbd9cf)
- Roll back the submission and remove the frequency adjustment function (PI servo controller) in the sample program ptpclient because it contains GPL licensed code; after rolling back, the clock synchronization accuracy drops to microsecond level.
  ↳ No PR: [5357e22](https://github.com/DPDK/dpdk/commit/5357e228f3fc9db861a45fa512db6decfb29352b)
- Add the PCI ID of the E610 virtual function to the ixgbe driver, fixing the omission of only adding the physical function ID before.
  ↳ No PR: [f678f3d](https://github.com/DPDK/dpdk/commit/f678f3dea8fd2a5e7fe2d78b5889c141ac263f7a)
- Fixed the false positive error log caused by incorrectly checking the resource release return value when non-template streams are destroyed.
  ↳ No PR: [7493f6f](https://github.com/DPDK/dpdk/commit/7493f6f8a38bc89ce53032e15018474d8a83bab1)
- Fix inline CTX writing, ensure FLUSH operation is completed by reading the CPT_LF_CTX_ERR register, and print a warning if it fails.
  ↳ No PR: [6c3de40](https://github.com/DPDK/dpdk/commit/6c3de40af8362d2d7eede3b4fd12075fce964f4d)
- Fix CPT hardware word size initialization for outbound SA, setting it to two words.
  ↳ No PR: [9587a32](https://github.com/DPDK/dpdk/commit/9587a324f28e84937c9efef534da542c30ff122b)
- Fixed the OOP processing problem in the cn10k event device, added the reception uninstall callback registration and updated the function pointer update logic.
  ↳ No PR: [01a990f](https://github.com/DPDK/dpdk/commit/01a990fe40e827c5f3497f785ce7fd68bff8ef5c)
- Fixed an issue where channel ID type conversion in the net/dpaa driver may damage data, use temporary u32 variables instead and convert them back to u16 correctly.
  ↳ No PR: [5edc61e](https://github.com/DPDK/dpdk/commit/5edc61ee9a2c1e1d9c8b75faac4b61de7111c34e)
- Removed redundant rte_eth_dev_release_port calls in the eth_dev_close function in the ntnic driver to avoid repeatedly releasing the port.
  ↳ No PR: [7fa6075](https://github.com/DPDK/dpdk/commit/7fa6075dee49bab1441d64f75cecf9647f66100b)
- Fixed the problem of Tx tracing using a single clock source, unified the tracing timestamps to the NIC hardware clock, and updated the tracing analysis script.
  ↳ No PR: [0293248](https://github.com/DPDK/dpdk/commit/02932480ae82d7ed3c207f02cc40b508cdda6ded)
- Fixed a bug where only the last VLAN could work properly due to incorrect clearing of the VSI mapping bitmap during VLAN replay after reset.
  ↳ No PR: [8e191a6](https://github.com/DPDK/dpdk/commit/8e191a67df2d217c2cbd96325b38bf2f5f028f03)
- When creating a scheduling node, set its VSI index to ensure that the node is associated with the correct VSI.
  ↳ No PR: [d0c63c7](https://github.com/DPDK/dpdk/commit/d0c63c7f0fcaedae4537910590020fe59210dbb1)
- Allow port initialization without traffic classification scheduling node, and use the root node as the default TC0 node when no TC node is detected.
  ↳ No PR: [55250a2](https://github.com/DPDK/dpdk/commit/55250a2d5b5041fb28e4d87ba20f43364c04cc72)
- Forced LDPC decoder input saturation to 6-bit LLR to improve VRB decoder robustness.
  ↳ No PR: [e71eb4f](https://github.com/DPDK/dpdk/commit/e71eb4f7bf3e2550015914661406ff4324c0c5f8)
- Fix the error handling when the net/octeon_ep driver initialization fails, remove the error direct return statement, and ensure that the cleanup process is executed when the chip ID is invalid.
  ↳ No PR: [283c97c](https://github.com/DPDK/dpdk/commit/283c97cffd7f58ce13ce59feface5ee94aa2acc8)
- Fixed a segfault that could be caused when the number of Tx queues is higher than the Rx queues in the net/netvsc driver, by creating corresponding Rx queues for each Tx queue (only allocating event buffers) and ensuring that RSS does not distribute traffic to these queues.
  ↳ No PR: [e900205](https://github.com/DPDK/dpdk/commit/e90020535c03cf9e60448ba623cac3301f111dae)
- Fixed an issue in the hns3 driver that resulted in inaccurate register name query logs due to incorrect use of logical AND operators.
  ↳ No PR: [f58fd22](https://github.com/DPDK/dpdk/commit/f58fd22240c27ea20cf41dd2aa15810712f518bf)
- Fixed the log format string in the i40e driver, changing the format specifier of the time_left variable from PRIu64 to PRIu32 to match its 32-bit type.
  ↳ No PR: [ba90329](https://github.com/DPDK/dpdk/commit/ba90329a5eb31234c65d5bbef68ff5c88318445b)
- Added pre-hashed input handling for RSA asymmetric encryption in FIPS validation examples.
  ↳ No PR: [733c786](https://github.com/DPDK/dpdk/commit/733c7861492d67eb5fba8ee50fb08d7db82a176d)
- Extracted the empty element parsing test into an independent test case, and fixed the resource leak problem of kvlist not being released when the branch fails.
  ↳ No PR: [8b1656a](https://github.com/DPDK/dpdk/commit/8b1656a9d951823d35ce0e51b31cf61fa191ac94)
- Fixed the error code returned when repeatedly creating counters in the hns3 driver, changing ENOTSUP to EINVAL.
  ↳ No PR: [585f1f6](https://github.com/DPDK/dpdk/commit/585f1f68f18c7acbc4f920053cbf4ba888e0c271)
- Fixed the issue in the l2fwd-event example that the spin lock was not released when obtaining the free event port.
  ↳ No PR: [1f41dea](https://github.com/DPDK/dpdk/commit/1f41deac447d7938198a2acdd1b7862161feef91)
- Reuse the RSS configuration saved by the software when configuring DCB to avoid configuration loss caused by hardware reset when the port is stopped.
  ↳ No PR: [34847a7](https://github.com/DPDK/dpdk/commit/34847a73034566ed1dab8bbc6882a12492b7f7fd)
- Fixed the array out-of-bounds access problem of comp_names_to_index function in testpmd.
  ↳ No PR: [f86085c](https://github.com/DPDK/dpdk/commit/f86085caab0c6c5dc630b9d6ad20d1c728e7703e)
- Add validity check for firmware reset types in hns3 driver, and record error logs for invalid types.
  ↳ No PR: [3db8460](https://github.com/DPDK/dpdk/commit/3db846003734d38d59950ebe024ad6d61afe08f0)
- Improve the flow scale query function of bnxt driver, synchronize resource status and add buffer dirty status to avoid unnecessary firmware synchronization.
  ↳ No PR: [288becf](https://github.com/DPDK/dpdk/commit/288becfb77dfb2d37c80960e3f40f5477f237f6c)
- Removed deprecation notice for cryptodev callback function prototype update as replacement API has been provided.
  ↳ No PR: [76b354b](https://github.com/DPDK/dpdk/commit/76b354be229926ccdf28951c3dbab4f4bb9570ea)
- Fix the loop boundary vulnerability in the i40e driver management send queue cleaning function, add validity check and reconstruct the loop logic.
  ↳ No PR: [3e61fe4](https://github.com/DPDK/dpdk/commit/3e61fe48412f46daa66f7ccc8f03b1e7620d0b64)
- Fixed an array out-of-bounds writing problem that may occur when parsing iface parameters in the mvneta driver.
  ↳ No PR: [c705c67](https://github.com/DPDK/dpdk/commit/c705c67d304b9450824a169b652520c2358c6aee)
- Fix the integer overflow problem of the ssovf_parsekv function in the event/octeontx driver, use strtoul instead and add input verification.
  ↳ No PR: [3e86eee](https://github.com/DPDK/dpdk/commit/3e86eee028c69b98144e2c62ec48091467e790be)
- Add L4 port numbers for all packets in testpmd's verbose output.
  ↳ No PR: [e2bce04](https://github.com/DPDK/dpdk/commit/e2bce04b48ab7e9fb184322a4ffa5a58705cae45)
- Remove extra newlines in Marvell driver and fix build errors triggered by RTE_LOG_LINE check.
  ↳ No PR: [8df7165](https://github.com/DPDK/dpdk/commit/8df71650e9fdc6346f09b7a57e86cded7b553152)
- Fix build warning due to data type mismatch on Ubuntu 24.04.
  ↳ No PR: [20c29a0](https://github.com/DPDK/dpdk/commit/20c29a0e4602b9c7be5ea299457f909846c3785d), [b9799fb](https://github.com/DPDK/dpdk/commit/b9799fb5e7a38c824c91b88d3c89250d23c783e6)
- Add TM node and parameter printing after shaper command in testpmd.
  ↳ No PR: [52e5e7c](https://github.com/DPDK/dpdk/commit/52e5e7c2d393a244e77997b2b3d2edd6365257b7)
- Fixed the log printing format in the ice driver, using %u for unsigned integers and 0x%x for bit masks.
  ↳ No PR: [c11665b](https://github.com/DPDK/dpdk/commit/c11665b25f78bc6c867ce27ff4e359a87db1050e)
- Remove unnecessary flags settings for X722 devices in i40e driver.
  ↳ No PR: [deb7c44](https://github.com/DPDK/dpdk/commit/deb7c447d088903d06a76e2c719a8207c94a576e)
- Add definitions of multiple PHY debug registers for i40e network card driver.
  ↳ No PR: [10bcd34](https://github.com/DPDK/dpdk/commit/10bcd34584405e96079b5291c903210cf0117465)
- Remove the remnants of the flow flex init command in testpmd that is used for debugging and has no actual function.
  ↳ No PR: [d5c5039](https://github.com/DPDK/dpdk/commit/d5c50397a1cc06419970afbea9cd1c37e3c08a5b)
- Removed restriction on clearing RPM statistics on cn10k platform.
  ↳ No PR: [1eb1bb3](https://github.com/DPDK/dpdk/commit/1eb1bb394b013b844671bbad0a1f1048d633e8be)
- Add memory pool debugging support to dpaa driver, add memory pool cookie checking in receive and send paths.
  ↳ No PR: [b0827a4](https://github.com/DPDK/dpdk/commit/b0827a40f1b9c9562fb14dca69b5e033e8547deb)
- Check the return value of rte_eth_link_get in the memif driver and log an error if it fails.
  ↳ No PR: [a4fa02e](https://github.com/DPDK/dpdk/commit/a4fa02e06046d36c6a7340201571397d2f59a682)
- Fixed an issue in the ethtool example where the return value was not processed when the driver did not support register information.
  ↳ No PR: [7d04227](https://github.com/DPDK/dpdk/commit/7d04227433ede0e3fdab1319cadafa46cc28266d)
- Added checks on the return values of device information acquisition and link status acquisition in multiple sample programs.
  ↳ No PR: [07e4dc0](https://github.com/DPDK/dpdk/commit/07e4dc04d99a99699d71a0a39dd2a7034049e663), [d0974e0](https://github.com/DPDK/dpdk/commit/d0974e07f42e12626ee78cba0d285090de40d149), [6c5e32c](https://github.com/DPDK/dpdk/commit/6c5e32c71220a69ee079284814a26d8ad29dabe4)
- Repair and expand the NTNIC driver's log system, unify the log format, and lower the partial initialization log level from INFO to DEBUG.
  ↳ No PR: [3489b87](https://github.com/DPDK/dpdk/commit/3489b87b497ed477257f5ed5b112c27c1407a68d)
- Remove dead code and fix conditional branch duplication issue in bnx2x driver.
  ↳ No PR: [3868c0c](https://github.com/DPDK/dpdk/commit/3868c0ce5ce83eacc9611cc4a83d20120ae3442e), [87e210e](https://github.com/DPDK/dpdk/commit/87e210eb086f49f32733c579003b9565e46535d7)

### Refactoring optimization
- Removed the interrupt capability of VRB1 device and updated related capability flags.
  ↳ No PR: [afa685d](https://github.com/DPDK/dpdk/commit/afa685dffeaf0e2cb96dff51963b5af415a6902e)
- Removed the checking logic based on firmware API version in ixgbe driver.
  ↳ No PR: [8e0c388](https://github.com/DPDK/dpdk/commit/8e0c3889de68029fa9385a2f77c27392a4e20240)
- Change the definition of the four PF power management registers in the i40e network card driver to offset by PF index.
  ↳ No PR: [221a3d8](https://github.com/DPDK/dpdk/commit/221a3d87a690e6212f2e122fff95aa271fd22cc8)
- Read scheduling layer information directly from VSI nodes, and add VSI handle matching checks to support runtime layer changes.
  ↳ No PR: [d4ee640](https://github.com/DPDK/dpdk/commit/d4ee6403b58dab6935661f8b99736707fe7d108c)
- Reconstruct DQ storage management: remove the independent single storage structure of each queue, replace it with multi-core shared storage allocation, and fix the memory leak during multi-storage allocation.
  ↳ No PR: [12d98ec](https://github.com/DPDK/dpdk/commit/12d98eceb8ac89d6284a2a56f9b83cca40b73e80)
- When supporting multi-PF firmware, PF representative ports are no longer created, and the calculation logic for the number of representative ports is adjusted accordingly.
  ↳ No PR: [619ea0b](https://github.com/DPDK/dpdk/commit/619ea0b6a5489de8ae9b5c45634dca78ca79cb56)
- Obtain VFIO group FD directly through the file system for the FSL MC bus to avoid conflicts with PCIe VFIO; at the same time, restructure the VFIO setting logic and add DMA mapping and extended checking functions.
  ↳ No PR: [0e603d8](https://github.com/DPDK/dpdk/commit/0e603d80cea6d546e3c0d283a5d751eab8eaa662), [8831b45](https://github.com/DPDK/dpdk/commit/8831b45622a9bb4a76269854518a556b17ac825f)
- Changed the protocol identification method from based on the previous protocol type to based on the frame attribute flag (FAF), added a new FAF parser, and restructured related extraction and configuration functions.
  ↳ No PR: [200a33e](https://github.com/DPDK/dpdk/commit/200a33e4c2b0f401a9bfb3cc4a8f3fe8ad8923ad)
- When EAL initialization fails, it will no longer be output to stderr and log at the same time, but will be recorded only through logging, and the log level will be raised from ERR to ALERT.
  ↳ No PR: [72bf6da](https://github.com/DPDK/dpdk/commit/72bf6da85a657dc4dd0662f1cd854dcc0da6da07)
- Extracted the auxiliary function used to determine the physical representative port, and reconstructed the related initialization logic.
  ↳ No PR: [2e3a514](https://github.com/DPDK/dpdk/commit/2e3a514376abc530d3f99cb7be5bd10392b619d4)
- Removed VNIC asynchronous event handling function, and adjusted the default VNIC/SVIF acquisition logic.
  ↳ No PR: [ef9e424](https://github.com/DPDK/dpdk/commit/ef9e424aa72477cc5fd35efeb31c923a67383241)
- Renamed CNXK error code to CN10K error code, and added dedicated op_error_get functions for different models.
  ↳ No PR: [63b82e2](https://github.com/DPDK/dpdk/commit/63b82e242251f8684d46390b9e8bb9dcc5d34147)
- Reconstructed the debug log of the dpaa2_sec driver and optimized the log output method.
  ↳ No PR: [673382d](https://github.com/DPDK/dpdk/commit/673382d4906f16d87fa11ec7e50cc9fe58c30baa), [662811c](https://github.com/DPDK/dpdk/commit/662811cba41f86af94e029230725c985a1eedb20)
- Use rte_bitset to replace the homemade single bit set to support a larger number of ports.
  ↳ No PR: [fb011cd](https://github.com/DPDK/dpdk/commit/fb011cdae56cc698ae76b17635c5b1968f5754b4)
- Unified the log packaging macros in the Intel basic driver to directly call RTE_LOG(), and removed the _RAW macro.
  ↳ No PR: [3cd9f24](https://github.com/DPDK/dpdk/commit/3cd9f24df2b608d879a8980047b69e9c6697dfa7)
- The SFC driver and SFC vDPA driver use the default log type provided by the build framework instead of using the hard-coded log prefix string.
  ↳ No PR: [df47324](https://github.com/DPDK/dpdk/commit/df47324b6022119e9ce3774795ddb40446762895)
- For E825C devices, the RD bit setting method of the AQ command to obtain Tx topology has been adjusted to make it consistent with E830.
  ↳ No PR: [58ed532](https://github.com/DPDK/dpdk/commit/58ed532abc5681c39457282fddd5c4de31a8bc03)
- Reconstructed the flow item inspection and calculation functions, and unified the parameter transfer method.
  ↳ No PR: [2a71691](https://github.com/DPDK/dpdk/commit/2a716911fd746b55694fb9daf419a873cdc99e24)
- Added naming structure and raw data access structure for the 16-byte receive descriptor of the i40e network card driver.
  ↳ No PR: [35dac96](https://github.com/DPDK/dpdk/commit/35dac9668df5b2d1ba63bf1ccfd045eb53c614f7)
- Reconstructed the link speed update logic of NFP network card driver and added auxiliary functions.
  ↳ No PR: [48de625](https://github.com/DPDK/dpdk/commit/48de6254632fa248e24b502e56f5336eaca6d30f), [2e3ad18](https://github.com/DPDK/dpdk/commit/2e3ad18750f8f786f3d4e9a5b0f262e01a6386b4), [1b3b12c](https://github.com/DPDK/dpdk/commit/1b3b12c4a89c12fdf33196af1cf80f3f71d7bf8a)
- Standardized the use of port indexes in multiple functions, and uniformly obtained the index through nfp_net_get_idx.
  ↳ No PR: [c33504d](https://github.com/DPDK/dpdk/commit/c33504de83eedf218ba4ed3ca75a1ca377346ec2)
- Moved the BP_LOG macro definition from txgbe_logs.h to txgbe_osdep.h of the base driver.
  ↳ No PR: [cd98310](https://github.com/DPDK/dpdk/commit/cd983102803b12cd01ed7bb4c45933165703f56a)
- Reconstructed the thread registration and deregistration functions, using atomic fetch operation instead of CAS loop, and using RTE_BIT64 macro instead.
  ↳ No PR: [8d03152](https://github.com/DPDK/dpdk/commit/8d03152e0b934903d220167c87fe73ea42cc13bf)
- Dynamically calculate the maximum number of queues based on device variants, replacing the original fixed value configuration.
  ↳ No PR: [2135244](https://github.com/DPDK/dpdk/commit/21352447018b9f055161cd7546197fce82b370e0)
- Code cleanup and reconstruction of baseband/acc driver, including optimizing condition judgment, adjusting queue initialization, etc.
  ↳ No PR: [cbf1bb8](https://github.com/DPDK/dpdk/commit/cbf1bb8b47caa0f80dadd555173a29c08441ec4a), [b460b3b](https://github.com/DPDK/dpdk/commit/b460b3bbbbe708bc8ac2426c42bd96f18d04c41c)
- Reconstruct the configuration recovery logic and extract promiscuous mode and multicast recovery into independent functions.
  ↳ No PR: [a98bd0f](https://github.com/DPDK/dpdk/commit/a98bd0fe444c3cdbce7d40cd5545abb38aca9469)
- Extract the allocation auxiliary functions of PHY, PF and VF representors, and reconstruct the representative allocation logic.
  ↳ No PR: [0006b08](https://github.com/DPDK/dpdk/commit/0006b08758a29c64671883eabc4c2822a70ebe93), [5f22bc0](https://github.com/DPDK/dpdk/commit/5f22bc0a00bf6a5769169cbddbd5c325364258c2), [edcf048](https://github.com/DPDK/dpdk/commit/edcf04893876949db915a4b662ff31adda491fa7)
- Reconstruct the initialization process and simplify multiple function parameters into structure pointers.
  ↳ No PR: [6f708e5](https://github.com/DPDK/dpdk/commit/6f708e5215517879b8f05905c90a674d06206daf)
- Add auxiliary functions to the NFP driver and rename them to make the main process and auxiliary process logic consistent.
  ↳ No PR: [eac7eda](https://github.com/DPDK/dpdk/commit/eac7eda4831ea33749994fa2e49c8a2c39fbed25)
- Split the parameter verification in the hash creation function into independent checks, and optimize the error message.
  ↳ No PR: [bf26e6f](https://github.com/DPDK/dpdk/commit/bf26e6f4019b7ab29e2ff8263effd3695d415ef4)
- Improve BMan buffer acquire operation, ignore reserved bits in response, use mask to extract valid quantity.
  ↳ No PR: [a116979](https://github.com/DPDK/dpdk/commit/a116979a03c6873ad3c72422175ac0325f51c846)
- Rename variables in QBMAN driver to avoid duplicate definitions.
  ↳ No PR: [98cfbbb](https://github.com/DPDK/dpdk/commit/98cfbbbe0f2bacdaffb12faadb984610055efc09)
- In the DPAA2 network card driver, extract the drop priority from the frame descriptor and store it in mbuf.
  ↳ No PR: [7994a12](https://github.com/DPDK/dpdk/commit/7994a12c4eb9a6bfe05c9c7c8de1d8d0bb427293)
- Merge multiple representor event handling functions to handle events such as representee status changes and MTU settings through a unified mbox.
  ↳ No PR: [e66a6e5](https://github.com/DPDK/dpdk/commit/e66a6e5401ed8dc1e03e42af516deb8b8b2dfac8)
- Replaced the MAC address copy method in the TAP driver from rte_memcpy to rte_ether_addr_copy.
  ↳ No PR: [94bdbf1](https://github.com/DPDK/dpdk/commit/94bdbf14af734b667e549c0806105e1b9262c967)
- Change the parameter of the tap stream conversion function from an opaque void pointer to a concrete structure type.
  ↳ No PR: [9abf92e](https://github.com/DPDK/dpdk/commit/9abf92e01cb68b6178730433a2dd16bd5637f55c)
- Migrate pthread mutex in ntnic driver to DPDK spin lock.
  ↳ No PR: [2407c75](https://github.com/DPDK/dpdk/commit/2407c75530e06fde79e9e0167b162a9253f08b2b)
- Change the key recipe table from static allocation to dynamic memory allocation, and refactor related functions.
  ↳ No PR: [4a925aa](https://github.com/DPDK/dpdk/commit/4a925aa7bf1b622b96da193eab5ebac9943490be)
- Replace FQLOCK/FQUNLOCK macros with inline functions with thread-safe annotations.
  ↳ No PR: [68508c1](https://github.com/DPDK/dpdk/commit/68508c18a91064ced34c664697ce0c6e25b5f787)
- Removed redundant conditions in policy action count checks.
  ↳ No PR: [4c2e746](https://github.com/DPDK/dpdk/commit/4c2e7468426ae6be3f2a8f2d15e7d1222083eb9d)
- In several drivers, replaced the logging macro with a version that supports automatic line wrapping, and removed manually added newlines in the log string.
  ↳ No PR: [2b843ca](https://github.com/DPDK/dpdk/commit/2b843cac232eb3f2fa79e4254e21766817e2019f)
- Split multi-line log messages in the driver into single-line log calls.
  ↳ No PR: [1af8b0b](https://github.com/DPDK/dpdk/commit/1af8b0b2747fe6c6267fa7bedb602e569742362e)
- Replace the __attribute__((__may_alias__)) used directly in the cxgbe driver with the existing __rte_may_alias macro.
  ↳ No PR: [3e49a10](https://github.com/DPDK/dpdk/commit/3e49a10f2ede1d047bbdec9ee56e2227459278f7)
- Removed impossible dead code checks in the argparse module.
  ↳ No PR: [66e57df](https://github.com/DPDK/dpdk/commit/66e57df338d1e7a503220e4a3c3f2b92998f3f23)
- Removed unnecessary error log when aggregate mbuf allocation failed in bnxt driver.
  ↳ No PR: [9342a8d](https://github.com/DPDK/dpdk/commit/9342a8d977b7f91588bc61844fe16c94ffd615c3)
- Removed unnecessary type conversion in FPGA 5GNR FEC driver.
  ↳ No PR: [3f9eab1](https://github.com/DPDK/dpdk/commit/3f9eab142058e7e4867e9f675889430a0eee8e87)
- Reduced multiple log_max_* field types in HCA attributes from int to uint8_t.
  ↳ No PR: [ec17aa6](https://github.com/DPDK/dpdk/commit/ec17aa6a129531601f740ff4551a367e863e97e0)
- Removed debug macros that never took effect in the net/dpaa driver.
  ↳ No PR: [2a0c7fb](https://github.com/DPDK/dpdk/commit/2a0c7fb22dcd2081323696ca7dcaa4ce65a00c12)
- Replaced logging macros in multiple drivers with new macros with _LINE suffix, and removed extra newlines.
  ↳ No PR: [e99981a](https://github.com/DPDK/dpdk/commit/e99981af34632ecce3bac82d05db97b08308f9b5)
- Enable type qualifier warnings in the power library and modify related functions to eliminate warnings.
  ↳ No PR: [74efd38](https://github.com/DPDK/dpdk/commit/74efd38b416fcf9eae2a5b429b81b550a73a47b6)
- In the baseband driver, explicitly initialize the queue number to 0 for FFT and MLDTS operation types.
  ↳ No PR: [0f4e990](https://github.com/DPDK/dpdk/commit/0f4e9909bc517d845e47da803f8b534691bbe5a3)
- Remove unnecessary type conversions from the testpmd built-in command list.
  ↳ No PR: [0a3901a](https://github.com/DPDK/dpdk/commit/0a3901aa624a690faa49ca081c468320d4edcb7a)
- Update variable types in PTP initialization function and adjust code format.
  ↳ No PR: [b144d0c](https://github.com/DPDK/dpdk/commit/b144d0c51782bf2e12e92fc485eba56fd07215a7)
- Clean up unused local variables in i40e driver.
  ↳ No PR: [d63c082](https://github.com/DPDK/dpdk/commit/d63c0823472340db19aa1103cbfbcd94fefd00ce)
- Replace strtok in string parsing functions with the reentrant version strtok_r.
  ↳ No PR: [9236e5b](https://github.com/DPDK/dpdk/commit/9236e5b31d909b45fa52c5e19adf02108a2052d1)
- Removed unnecessary IEEE1588 compilation options in bnxt driver.
  ↳ No PR: [07e3beb](https://github.com/DPDK/dpdk/commit/07e3bebf3c93750c52ed9be87edd212fbc22da0a)
- Rearrange the structure order in the asymmetric encryption header file and move the SM2 operation parameter structure to an adjacent position.
  ↳ No PR: [6d66f08](https://github.com/DPDK/dpdk/commit/6d66f08e794257cdb30c566bbc1c360b529e4665)
- Renamed flower service flag field.
  ↳ No PR: [14eb71f](https://github.com/DPDK/dpdk/commit/14eb71f6293687e2abcabef7e2987dc9bcb394ae)
- Modify return values of several ULP tools to use EXIT_SUCCESS/EXIT_FAILURE macros.
  ↳ No PR: [c569279](https://github.com/DPDK/dpdk/commit/c569279aded4bb8fdf83b09e0726fa07028dcef8)
- Removed unnecessary NULL pointer checks before free and related functions in multiple drivers.
  ↳ No PR: [8e469ec](https://github.com/DPDK/dpdk/commit/8e469ecf509b38e0c9a738864236c2d22f262839), [165bed4](https://github.com/DPDK/dpdk/commit/165bed470a6d7bad077f178b696f441772182797), [0e361f5](https://github.com/DPDK/dpdk/commit/0e361f5a0ca96d4e228191ceaf800636e7beeea0)
- Add debug log macro for r8169 driver.
  ↳ No PR: [491aa39](https://github.com/DPDK/dpdk/commit/491aa390728abbf3527d49c4063ebc16d8a47075)

### Test related
- Added a random seed setting function to the DTS testing framework, supporting pseudo-random generation of seeds specified through command line parameters or configuration files to ensure reproducible test results.
  ↳ No PR: [cfe40ba](https://github.com/DPDK/dpdk/commit/cfe40bac95fb9c839f1c151f6c101e53e0cbfb63)
- Remove term master. from test file test_red.c.
  ↳ No PR: [bccabd1](https://github.com/DPDK/dpdk/commit/bccabd15fed89e12de5fdee022ca92ffea6e83d0)
- Clean up duplicate definitions and unused macros in the test_cryptodev test file.
  ↳ No PR: [9632654](https://github.com/DPDK/dpdk/commit/9632654250891db798ee154e9f808cc5584011c7), [e296fe6](https://github.com/DPDK/dpdk/commit/e296fe619ce276b645a4fb1243c9be6dc40de9f3)
- Refactor and fix argparse test cases, add comments and correct parameter names.
  ↳ No PR: [9684dfe](https://github.com/DPDK/dpdk/commit/9684dfeae3284ec93a56090e653fb74886d5a40e)
- Fixed NUMA configuration check error message in DMA performance test.
  ↳ No PR: [ff92d10](https://github.com/DPDK/dpdk/commit/ff92d10af68e87561046ba1c0b41a44d6a1dea5c)
- Register the cksum performance test into the performance test suite.
  ↳ No PR: [99ed5e9](https://github.com/DPDK/dpdk/commit/99ed5e931f59ebaf48cf4ab045f75466a2c388cd)
- Fixed the issue where the event scheduling type was not correctly assigned in the test.
  ↳ No PR: [adadb55](https://github.com/DPDK/dpdk/commit/adadb5585bd50260c3fa5495fcbe8baf64386f7e)
- Enable and improve the alarm test case on FreeBSD to make it more reliable.
  ↳ No PR: [fc7eec2](https://github.com/DPDK/dpdk/commit/fc7eec29dd7f9fcdf440ae23a6bc8580418bd9a9), [31fcb7d](https://github.com/DPDK/dpdk/commit/31fcb7d7dbf04b3ce4ae66602485c9797f6dbcd8)
- Remove resource APIs not used in tests.
  ↳ No PR: [e3052c1](https://github.com/DPDK/dpdk/commit/e3052c189f8a6f5bc260b263f3b3be0306751768)
- Restore cfgfile unit tests and use temporary files instead of embedded resources.
  ↳ No PR: [be22019](https://github.com/DPDK/dpdk/commit/be22019a58c484c0b43ec32de8cd4e58a91aa53f)
- Fixed the selection logic of the target event queue in testing.
  ↳ No PR: [367fa35](https://github.com/DPDK/dpdk/commit/367fa3504851ec6c4aef393a7c53638da45a903e)
- Added error recovery callbacks and new unit tests for cryptodev.
  ↳ No PR: [462ba59](https://github.com/DPDK/dpdk/commit/462ba592e53f74057bbf944c9e3e553317d7c32d)
- Add compile-time assertions in encryption tests to verify test vector length.
  ↳ No PR: [17406ec](https://github.com/DPDK/dpdk/commit/17406ec24b4ef9c1fc954f774230f461cb037979)
- Enable larger packets in TLS tests and add helper functions.
  ↳ No PR: [b22cdcc](https://github.com/DPDK/dpdk/commit/b22cdccdd366c06e45888713ed865061c3181e3a)
- Free allocated memory pool and fix constants in test suite's cleanup function.
  ↳ No PR: [acab7f3](https://github.com/DPDK/dpdk/commit/acab7f3fdfe09bc684ccc7804fdf3c8ff3268878)
- Use mempool to manage DMA operations and add latency measurement functionality.
  ↳ No PR: [bca734c](https://github.com/DPDK/dpdk/commit/bca734c27e345af500d0d951421584e2567cd107)
- Add retry mechanism in IPsec statistical verification test.
  ↳ No PR: [db65855](https://github.com/DPDK/dpdk/commit/db65855a0317ab5ce3a1f682e64dc61d654afdb3)
- Memory pool performance test adds larger burst size and cache optimization.
  ↳ No PR: [7775adc](https://github.com/DPDK/dpdk/commit/7775adc618811cd3713403cae7d6acc5b296d558)
- Reintroducing delays and eliminating unreachable code in the test service core.
  ↳ No PR: [fd1bcb6](https://github.com/DPDK/dpdk/commit/fd1bcb6c58b0752f408beaedfdb83a2e82173129)
- Skip IPsec post-processing for negative test cases and add packet length validity checks in secure IPsec testing.
  ↳ No PR: [4677de0](https://github.com/DPDK/dpdk/commit/4677de0a4c2ba803d0e1adc26774f2c6c8b5b6df)
- Removed redundant rte_eth_dev_info_get calls in bonding tests.
  ↳ No PR: [419daaa](https://github.com/DPDK/dpdk/commit/419daaa2794ca380db2b1267c62c2d5de516b1b3)
- Added configuration support for VLAN test suite, added vlan option.
  ↳ No PR: [e41fe1f](https://github.com/DPDK/dpdk/commit/e41fe1f8df707c7de026eae6b529126469bb955f)
- Fixed the problem of uninitialized structure fields in FIB RCU test.
  ↳ No PR: [19d463a](https://github.com/DPDK/dpdk/commit/19d463aacd5a5345365075db65deb8e9b3003654)
- Added test cases for RSS key generation in hash tests.
  ↳ No PR: [89398ec](https://github.com/DPDK/dpdk/commit/89398ecec0486f91e1d9302ae2fb454f3b2dd012)
- Added interrupt disabling API call in bbdev test application to improve test coverage.
  ↳ No PR: [9235155](https://github.com/DPDK/dpdk/commit/92351557d57637431807f46f5433886a10efcc91)
- Fixed synchronous API test cases, skipping tests involving enqueue/dequeue when using synchronous API.
  ↳ No PR: [251fdc5](https://github.com/DPDK/dpdk/commit/251fdc592da5eddc4d84a95d0c151b0134504a32)
- Enhanced test coverage for RCU rule recycling, adding additional negative tests and explicitly checking return codes.
  ↳ No PR: [259deb7](https://github.com/DPDK/dpdk/commit/259deb73d989d91cb1ddb8c60c24de58aa09609a)
- Add a check on the return value of the temporary file deletion operation in the cfgfile test.
  ↳ No PR: [554e802](https://github.com/DPDK/dpdk/commit/554e802ee3204a24149f76946c8ad81b2582349c)
- Fixed the problem of using the same variables in the inner and outer loops in the bonding unit test, and used batch release of mbufs instead.
  ↳ No PR: [112ce39](https://github.com/DPDK/dpdk/commit/112ce3917674b7e316776305d7e27778d17eb1b7)
- Fixed MAC address comparison error in bonding unit test.
  ↳ No PR: [f7f8563](https://github.com/DPDK/dpdk/commit/f7f85632daf6d6f525d443f90a0ac3c8a3e40b72)
- Fixed an operator precedence issue caused by incorrect placement of brackets in the IPv6 extension header loop.
  ↳ No PR: [0151b80](https://github.com/DPDK/dpdk/commit/0151b80786ebbc62f0ead73bd4708665228a093d)
- Fixed the issue of repeated initialization of event device configuration in testing.
  ↳ No PR: [8c08b10](https://github.com/DPDK/dpdk/commit/8c08b10d047ac64fb98709871b192698663af7d7)
- Fix duplicate condition in TLS zero-length record check.
  ↳ No PR: [c6f484a](https://github.com/DPDK/dpdk/commit/c6f484adf173567a66b72bfebdda41499e723952)
- Fixed the alignment macro test loop coverage, and fixed the problem of missing parentheses in the macro definition causing the loop to end prematurely.
  ↳ No PR: [b3e64fe](https://github.com/DPDK/dpdk/commit/b3e64fe596a3117edf6d3a79a6c5238a9b92dc4f)
- Fixed the expression of lcore enable check in test/eal, and added the check for lcore 6.
  ↳ No PR: [357f915](https://github.com/DPDK/dpdk/commit/357f915ef5e1280d921fb103ea33066e7a888ed2)

### Performance optimization
- Optimize testpmd's SSE MAC swap processing, improve the performance of sending and receiving packets by moving the offload flag update to the beginning of the loop and interleaving SIMD operations.
  ↳ No PR: [222effc](https://github.com/DPDK/dpdk/commit/222effc6ec29cafc7f23d4f6141b8ba2bd384531), [1b307e5](https://github.com/DPDK/dpdk/commit/1b307e535643c94be10f2dadca8de354bb2def6d), [8001e1c](https://github.com/DPDK/dpdk/commit/8001e1c8f7fecdeb2bb9193a3b7acdb870546c0d)
- Optimize virtio statistics counter update performance, reduce branches and sort packet size comparison by typical traffic probability.
  ↳ No PR: [e9dac45](https://github.com/DPDK/dpdk/commit/e9dac45c0d3071bf3c6308a0cfbae93421ac4829)
- Removed the 1 millisecond per-session delay when obtaining IPsec statistics to avoid cumulative delays in large-session scenarios.
  ↳ No PR: [f852c95](https://github.com/DPDK/dpdk/commit/f852c95807f37f390e21874fbfc681442ad865f6)
- Adjust LDPC decoder algorithm parameters and fall back to MS1 version to improve performance under MU1 fading conditions.
  ↳ No PR: [b9cb8e6](https://github.com/DPDK/dpdk/commit/b9cb8e68b9bbc4bbb2347b09556207da0a37b398)
- Change the protocol parameter when creating AF_PACKET socket from ETH_P_ALL to 0 to avoid implicit binding and make it safer and more efficient.
  ↳ No PR: [5b81eac](https://github.com/DPDK/dpdk/commit/5b81eac5fd6f8035a2d8fdd3863eb789f77de164)
- Optimize the scheduler subtree search, change the search direction from downward to upward, avoid traversing irrelevant branches, and improve processing speed.
  ↳ No PR: [4376d9f](https://github.com/DPDK/dpdk/commit/4376d9fd19f332dbabf11548fe59cda296d53a75)
- Optimize thread creation performance by using pthread_attr_setaffinity_np to set CPU affinity before creating threads to avoid synchronization waits.
  ↳ No PR: [64f2788](https://github.com/DPDK/dpdk/commit/64f27886b8bf127cd365a8a3ed5c05852a5ae81d)
- Replaced CRC32 hash calculation with DPDK-optimized CRC32 implementation, and enabled SSE4.2 hardware acceleration.
  ↳ No PR: [b14da65](https://github.com/DPDK/dpdk/commit/b14da6540294be2ecae13b69dbe0b00f93bcc597)
- Fixed the leakage problem of PFDRs in the dpaa bus to avoid resource exhaustion affecting performance.
  ↳ No PR: [b292acc](https://github.com/DPDK/dpdk/commit/b292acc3c4a8fd5104cfdfa5c6d3d0df95b6543b)
- Clear PCIe AER register error status after soft reset to avoid error accumulation affecting performance.
  ↳ No PR: [c4ced2d](https://github.com/DPDK/dpdk/commit/c4ced2d58a542980fdbbbf3095ad6571e3e6ba14)
- Synchronously update the link duplex mode and optimize the error log to improve the accuracy of link configuration.
  ↳ No PR: [25dd1fd](https://github.com/DPDK/dpdk/commit/25dd1fd045ed230f7d6388be4044ebf16912da3a)
- Fixed a memory leak caused by xstats memory allocation failure during node cloning.
  ↳ No PR: [5e65cd4](https://github.com/DPDK/dpdk/commit/5e65cd4a722ec7f277a70447db318953252bf6f9)
- Use multi-word bitmap instead of byte array to represent service flags, support more services and reduce memory usage.
  ↳ No PR: [34ec238](https://github.com/DPDK/dpdk/commit/34ec23845d9e3fe066d8d38fba9ebb0b9e7cdb5e)
- Added speed capability support for new network card models to enic driver.
  ↳ No PR: [543617f](https://github.com/DPDK/dpdk/commit/543617f44eec3e348ea8cd04924ef80389610d46)
- Add malloc heap dump support in the memory dump option to facilitate performance debugging.
  ↳ No PR: [c33717c](https://github.com/DPDK/dpdk/commit/c33717c6f886b840e2121a14048f59d1c0929621)
- Added command line options for configurable Rx burst size and mbuf cache size to the l3fwd example.
  ↳ No PR: [d5c4897](https://github.com/DPDK/dpdk/commit/d5c4897ecfb2540dc4990d9b367ddbe5013d0e66), [d9f26e5](https://github.com/DPDK/dpdk/commit/d9f26e52a55c8a500439d5f0539dfbf5a6b41c3c)
- Roll back the redefinition from memcpy to rte_memcpy in the net/ena driver to avoid performance degradation and out-of-bounds problems.
  ↳ No PR: [966764d](https://github.com/DPDK/dpdk/commit/966764d003554b38e892cf18df9e9af44483036d)
- Set the GRPCFG traffic category to 1 for the idxd DMA device to improve the performance of the current generation accelerator.
  ↳ No PR: [aa8ed90](https://github.com/DPDK/dpdk/commit/aa8ed903d29ec90ced2e9dbcf1132d098de3b6f7)
- Optimize vhost queue statistics counter update performance, by reducing branching and reordering packet size comparisons.
  ↳ No PR: [10be332](https://github.com/DPDK/dpdk/commit/10be3321d1a8ae4747950344dfa16b00db67f1a6)
- Optimize netvsc network statistics counter update performance, by reducing branching and reordering packet size comparisons.
  ↳ No PR: [84c292f](https://github.com/DPDK/dpdk/commit/84c292fab3447295bf8553e25c31bc50f459c786)
- Performance optimization of bnxt/tf_ulp driver, including inlining and branch prediction hints.
  ↳ No PR: [0c036a1](https://github.com/DPDK/dpdk/commit/0c036a1485b9d9163a8fa8059ed5272d060c05e0)

### Security related
- Fixed the problem of possible out-of-bounds reading when parsing the Preserved Fields Area in the ice driver, and added a boundary check on the head value in the ice_clean_sq function to prevent out-of-bounds access.
  ↳ No PR: [dcb760b](https://github.com/DPDK/dpdk/commit/dcb760bf0f951b404bce33a1dd14906154b58c75), [9378aa4](https://github.com/DPDK/dpdk/commit/9378aa47f45fa5cd5be219c8eb770f096e8a4c27)
- Fixed the problem of the send_packets_multi function reading out of bounds of the dst_port array in the l3fwd example, and the integer overflow problem of option parsing in the l3fwd-power example.
  ↳ No PR: [ebab0e8](https://github.com/DPDK/dpdk/commit/ebab0e8b2257aa049dd35dedc7efd230b0f45b88), [0bc4795](https://github.com/DPDK/dpdk/commit/0bc4795d5994459a3d261afd7f843eb0cabdecf5)
- Added __rte_assume prompt for multiple network drivers to avoid array out-of-bounds compilation errors in single-queue configuration.
  ↳ No PR: [084d0cd](https://github.com/DPDK/dpdk/commit/084d0cdb572f87ec6a52d32f2f7890fd337ddfba)
- Added TSO segment size minimum length check for bnxt driver, discarding segments smaller than 4 bytes.
  ↳ No PR: [9151adf](https://github.com/DPDK/dpdk/commit/9151adf2b9eb901faf8f090ad4e612f5f20e36f5)
- Changed interrupt affinity settings from system() calls to direct file I/O, eliminating potential security risks.
  ↳ No PR: [126cc1b](https://github.com/DPDK/dpdk/commit/126cc1b2b44a3d2967943e1ef995b9e20f9e5021)
- For security reasons, the debugging information export of some exposed address registers in the hns3 driver has been removed.
  ↳ No PR: [c8b7bec](https://github.com/DPDK/dpdk/commit/c8b7bec0ef23f53303c9cf03cfea44f1eb208738)
- Fixed a possible string overflow problem when copying the OpenSSL algorithm name, use strlcpy instead of rte_memcpy.
  ↳ No PR: [c5819b0](https://github.com/DPDK/dpdk/commit/c5819b0d96d1a24c25aa4324913fd2566eb19ae9)
- Removed function to read minimum safe revision from NVM.
  ↳ No PR: [e0acd76](https://github.com/DPDK/dpdk/commit/e0acd76ad8396e521aece181040700e6da3f1c18)

### Documentation
- Updated contributor guide: Removed misleading instructions about new patches not requiring CC to maintainers, added new driver development guide, provided best practices for creating DPDK drivers and upstream submission suggestions.
  ↳ No PR: [d5f8103](https://github.com/DPDK/dpdk/commit/d5f81030df75c587885245ff1b14f123448a97c7), [ad6833e](https://github.com/DPDK/dpdk/commit/ad6833e5accbf67b4e1e8c9ca4911ba1163d3cb5)
- Add missing newlines at the end of the README file in common/idpf.
  ↳ No PR: [402cbd4](https://github.com/DPDK/dpdk/commit/402cbd45beb1428bcac3a438eb77a9c5fa5b4237)
- Reorganize the index structure of the Programmer's Guide, create ethdev and eventdev subdirectories, and unify the chapter title format.
  ↳ No PR: [41dd9a6](https://github.com/DPDK/dpdk/commit/41dd9a6bc2d9c6e20e139ad713cc9d172572dd43)
- Added manually optimized Sphinx API documentation source files for the DTS framework, and added API documentation for the capability and topology modules.
  ↳ No PR: [1e472b5](https://github.com/DPDK/dpdk/commit/1e472b5746aeb6189fa254ab82ce4cd27999f868), [64fdb62](https://github.com/DPDK/dpdk/commit/64fdb622e3f15da32dee0feffb18e552ff14c044)
- Fixed the display problem of hyphens in parameter names in argparse documents.
  ↳ No PR: [51a639c](https://github.com/DPDK/dpdk/commit/51a639ca804234462df0a8c72523fa71181cea24)
- Updated PTP client examples to replace the term master/slave with the IEEE 1588g-2022 recommended timeTransmitter/timeReceiver.
  ↳ No PR: [b8d1d60](https://github.com/DPDK/dpdk/commit/b8d1d60fadc414321221843f3277445d8156c202)
- Update the dependency version document of the Arm IPsec-MB library to SECLIB-IPSEC-2024.07.08, and simultaneously modify the relevant instructions in the snow3g and zuc documents.
  ↳ No PR: [79e8689](https://github.com/DPDK/dpdk/commit/79e8689b9d53b3feca235a6e4b661cb98f1432b1)
- Updated DTS documentation, added descriptions of related options for external DPDK build support, and removed the obsolete --git-ref option.
  ↳ No PR: [0ae3214](https://github.com/DPDK/dpdk/commit/0ae32140331f61e6c7e6fe59b4c27e6a2059f395), [187a944](https://github.com/DPDK/dpdk/commit/187a944772c9665a7a10e439560d6a505c4e46a2)
- Updated the README of the ice driver base directory, updated the copyright year and version date, and added support for the E830 network card.
  ↳ No PR: [589347f](https://github.com/DPDK/dpdk/commit/589347feaf9dde1e5f8fc599858e69d413a5132d)
- Updated the supported firmware versions in the CPFL network card documentation, adding support for version 24.11 and FW 1.6.
  ↳ No PR: [d006f93](https://github.com/DPDK/dpdk/commit/d006f936d5dac3b8a17bf1a3f24766f1783cf561)
- Revised the grammar and clarity of multiple example application guide documents, and adjusted the chapter format to unify the template.
  ↳ No PR: [8750576](https://github.com/DPDK/dpdk/commit/8750576fb2a9a067ffbcce4bab6481f3bfa47097)
- Updated mlx5 driver documentation: Added descriptions of the -a and -v optional parameters of the mlx5_trace script, added descriptions of sending scheduling extended statistical counters, and explained that the ingress rule does not support the limit of match with compare result item in switch mode with repr_matching_en devarg enabled.
  ↳ No PR: [171360d](https://github.com/DPDK/dpdk/commit/171360df9f89a17f8b4177f01f11fa4473c74099), [4843aac](https://github.com/DPDK/dpdk/commit/4843aacb0d1201fef37e8a579fcd8baec4acdf98), [c07dbef](https://github.com/DPDK/dpdk/commit/c07dbef7e0208d4f5e36aa241ce360fc470f203b)
- Removed the outdated normal_llq_hdr devarg document, its functionality has been replaced by the new llq_policy devarg.
  ↳ No PR: [0525b49](https://github.com/DPDK/dpdk/commit/0525b496a4ecdc3b53b91fd36893d5d2541b056c)
- Added instructions on how to include huge pages in core dumps in the Linux System Guide, including setup methods and precautions.
  ↳ No PR: [036f72d](https://github.com/DPDK/dpdk/commit/036f72d07249aa36c2d2d61bdaf84a492044d0d9)
- Added autodoc-pydantic Sphinx extension to correctly generate documentation for Pydantic models, updated DTS configuration documentation to reference automatically generated API documentation.
  ↳ No PR: [6597fa4](https://github.com/DPDK/dpdk/commit/6597fa4a30add6e0790f0e25833c3e073d76a877)
- Added a new security protocol-specific guide and added references to related documents.
  ↳ No PR: [8711af2](https://github.com/DPDK/dpdk/commit/8711af290f353f727989684de2e75c7c41d2779a)
- Updated the recommended firmware and DDP version lists for i40e and ice network cards, and added corresponding version information for DPDK 24.11 and 24.07.
  ↳ No PR: [0fdf973](https://github.com/DPDK/dpdk/commit/0fdf973cdb1dcef6513fb36f3105c8123844d937), [ae52bdf](https://github.com/DPDK/dpdk/commit/ae52bdf2ce7a6a32202ddfdb1369f415a067fd3b)

### Build/CI
- Fixed compilation errors caused by header file movement, added header file inclusion in the vm_power_manager example, and cleaned up redundant references in lib/power.
  ↳ No PR: [b462f27](https://github.com/DPDK/dpdk/commit/b462f2737eb08b07b84da4204fbd1c9b9ba00b2d)
- Fixed build failure caused by using file() function in Meson subproject.
  ↳ No PR: [672c329](https://github.com/DPDK/dpdk/commit/672c32999e18d7194de90d12d3166c1a967dcb44)
- Fixed the problem of symbolic link script error when the driver installation subdirectory is empty or . by skipping the execution of the script.
  ↳ No PR: [dae002f](https://github.com/DPDK/dpdk/commit/dae002ff55a416206e710b05a06f050d5bc4dc6d)
- Added helper script for converting text files into initialization strings in C header files.
  ↳ No PR: [50614eb](https://github.com/DPDK/dpdk/commit/50614ebc112e53d54193f8b14ff7d1b37b5be15b)
- Fixed an issue where ban token checks could be bypassed, and cleaned up unused arrays.
  ↳ No PR: [84cf9b7](https://github.com/DPDK/dpdk/commit/84cf9b71fc2d6baf1869ef213daee7ec9f8880bc)
- The build system uses Meson's built-in version file support to obtain DPDK version numbers instead.
  ↳ No PR: [1980543](https://github.com/DPDK/dpdk/commit/198054305b95b9568017571baf49327d23834e9a)
- Moved the -Wno-address-of-packed-member warning disable from the global build configuration to the drivers subfolder and kept the flag for the vhost library and ipsec-secgw examples.
  ↳ No PR: [63c9142](https://github.com/DPDK/dpdk/commit/63c9142b3d634c2abf5a9ef0594ffb652517791c)
- Removed disabling of GCC 7's fallthrough warning and re-enabled it to catch potential bugs.
  ↳ No PR: [277552e](https://github.com/DPDK/dpdk/commit/277552e175b3529863adec9bbd8bb6288164506e)
- Fixed backport search logic and simplified related functions.
  ↳ No PR: [dbee696](https://github.com/DPDK/dpdk/commit/dbee69686b63fab960a98295a7de542d45de9b6d), [e2e4775](https://github.com/DPDK/dpdk/commit/e2e4775cc7a0699a66283ed6ddb0c2a51daae1ef)
- Added API documentation generation functionality to DTS, and fixed generation paths and links.
  ↳ No PR: [7f93264](https://github.com/DPDK/dpdk/commit/7f9326423a045f7346a459280dc98fed4afd6811), [dfef829](https://github.com/DPDK/dpdk/commit/dfef829263561809e20d0000dd4cf628a20ba9b2)
- Updated documentation and configuration files, removed the --no-root option to adapt to future Poetry versions.
  ↳ No PR: [72a44b2](https://github.com/DPDK/dpdk/commit/72a44b260f0f4f824aa473b30b8d97d84512c081)
- Added a job to check patches in the private warehouse CI.
  ↳ No PR: [2233925](https://github.com/DPDK/dpdk/commit/2233925d78b2c36fa2db610fd41ca7848b89e0c3)
- Improved ban token checking tool to support skipping multiple file modes and reporting all file warnings before exiting.
  ↳ No PR: [d500e69](https://github.com/DPDK/dpdk/commit/d500e69f644f0f98ed4ea7114481f2612056234c), [129f38c](https://github.com/DPDK/dpdk/commit/129f38c5b7ab4428ed94d088e3d3ef6a81807b55)
- Fixed false positives in the checkpatches script and added parameter checking, while excluding public EAL header files to avoid false positives.
  ↳ No PR: [5f33036](https://github.com/DPDK/dpdk/commit/5f33036cbc59d943ecc272916a722268e293cac3), [93f8d73](https://github.com/DPDK/dpdk/commit/93f8d73ac18de2df963698d31d8dd819392deade)
- Re-enable zero-length array warnings for gcc 10 and above.
  ↳ No PR: [1435e94](https://github.com/DPDK/dpdk/commit/1435e94f9ea79ae1d3748af90895ed53ef220d6c)
- Output the source code directory and build directory path at the end of the build configuration.
  ↳ No PR: [2169d01](https://github.com/DPDK/dpdk/commit/2169d012477c41e619a1485bf19ea42ea1d2b2f2)
- Removed unnecessary compiler warning disable flags in driver base codes such as i40e, ice, e1000, iavf, fm10k, etc., and streamlined the build configuration.
  ↳ No PR: [67bc46d](https://github.com/DPDK/dpdk/commit/67bc46de788f964af6864fe792f127aacd8c5bb5), [e565dbb](https://github.com/DPDK/dpdk/commit/e565dbbd3e86af41eb455f587fab2aa63124240d), [c881a1d](https://github.com/DPDK/dpdk/commit/c881a1d983337a12d24354ec7d10fd7b1a42a037), [3dbd0c5](https://github.com/DPDK/dpdk/commit/3dbd0c5dc7819919f4a3617d0ea4ac964aedc482), [ac69af6](https://github.com/DPDK/dpdk/commit/ac69af6d1d043c937fc2b283e34cbe6dd8a72b7c), [914bffb](https://github.com/DPDK/dpdk/commit/914bffbd112127c11af7bdada236d551242e6911)
- Install the libvirt development package in the CI workflow to support compilation testing of the vm_power_manager example.
  ↳ No PR: [d3a214a](https://github.com/DPDK/dpdk/commit/d3a214acdfc2016d748760cf54727fc013c54d21)
- Removed setting to treat Sphinx warnings as errors in DTS API documentation builds, allowing builds to ignore warnings from missing optional dependencies.
  ↳ No PR: [f4ccce5](https://github.com/DPDK/dpdk/commit/f4ccce58c1a33cb41e1e820da504698437987efc)
- Removed the nested html directory under the dts subdirectory in the API documentation to make the document path more consistent.
  ↳ No PR: [497cf54](https://github.com/DPDK/dpdk/commit/497cf54829c28859482998957d75477ae2b1bc1c)

### Maintenance
- The build target field in the DTS configuration has been renamed from build_target to dpdk_build to more accurately reflect its purpose; the configuration mode has also been simplified to use only one DPDK build per test run.
  ↳ No PR: [ecaff61](https://github.com/DPDK/dpdk/commit/ecaff610f53d7f4771150a99ffb54e27159f6029), [11b2279](https://github.com/DPDK/dpdk/commit/11b2279afbb5e628e9cff26b4b3fff4127711949)
- Removed extra newlines at the end of log messages in multiple drivers and fixed log format issues.
  ↳ No PR: [f665790](https://github.com/DPDK/dpdk/commit/f665790a5dbad7b645ff46f31d65e977324e7bfc)
- Adjust the base log level of the CNXK driver from NOTICE to INFO so that logs can be displayed properly when running the application.
  ↳ No PR: [adc561f](https://github.com/DPDK/dpdk/commit/adc561fc5352bd1f1c8e736a33bb9b03bbb95b3f)
- Move the C language linkage declaration in the driver header file after the include header file to maintain consistency with other header files in the project.
  ↳ No PR: [706fb9b](https://github.com/DPDK/dpdk/commit/706fb9b3c6190990126fb5262accbe87a77e5790)
- Removed extra newlines at the end of multiple debug logs in the fmlib base driver.
  ↳ No PR: [6be4899](https://github.com/DPDK/dpdk/commit/6be4899c951e85595c66cb13b13a229ec1268e45)
- Uniformly added a period at the end of the log message to standardize the log format.
  ↳ No PR: [b6de435](https://github.com/DPDK/dpdk/commit/b6de43530dfa30cbf6b70857e3835099701063d4)
- Added register definition and initialization support for multiple modules to the ntnic driver's FPGA support file, sorted and cleaned it up.
  ↳ No PR: [bf53e46](https://github.com/DPDK/dpdk/commit/bf53e467b4a347a3b9d37b3e9ee64803246af791), [bbd8b39](https://github.com/DPDK/dpdk/commit/bbd8b3901bcee48827933169e2c20649953c6724), [9234937](https://github.com/DPDK/dpdk/commit/923493778d2c9971d68446db178b05db11915f6a), [a7e7728](https://github.com/DPDK/dpdk/commit/a7e77283c2ab6157fd1cbdb86a0e5dcb9e1de550), [20ab0df](https://github.com/DPDK/dpdk/commit/20ab0df3dc7c0518d579b6660e531492dad17060)
- Fixed GCC 15 compilation error, changing string initialization of MAC address and VXLAN VNI to array initialization.
  ↳ No PR: [09158ba](https://github.com/DPDK/dpdk/commit/09158ba4cb0cefbadf45be08fa0cd587714d8813), [11f84bf](https://github.com/DPDK/dpdk/commit/11f84bf4eab350517ddd59498ae488562e3ccc23), [e0d947a](https://github.com/DPDK/dpdk/commit/e0d947a1e6c2f80aa039a4f7082a8aa16797d8b9)
- Initialize PTP timestamps for i40e and e1000 drivers to system time to align kernel driver behavior.
  ↳ No PR: [77e90b1](https://github.com/DPDK/dpdk/commit/77e90b1da5d31a6731b33bf1661f32353df35a48), [41927fd](https://github.com/DPDK/dpdk/commit/41927fde0889abb24aecc3538aed06f3ae1ae09e)
- Unified the use of DLB2 base driver log macros, and corrected newline characters in log messages.
  ↳ No PR: [6a41e60](https://github.com/DPDK/dpdk/commit/6a41e6070ea6f251987f81f9d610190b9adfb978)
- Replaced the string copy operation with strlcpy in the NFP driver, extracted the PF representative port initialization function, and added the EEPROM/module information operation interface.
  ↳ No PR: [cda9123](https://github.com/DPDK/dpdk/commit/cda9123ec16e08f2aa6476343733252512a3bf5e), [608bc94](https://github.com/DPDK/dpdk/commit/608bc946e25fc8ca94331c64adcd5750b49446b0)
- Added empty SG entry check in dpaa2 QDMA driver and adjusted return value on success to the index of the copied descriptor.
  ↳ No PR: [dcb9be8](https://github.com/DPDK/dpdk/commit/dcb9be853be46e1bdb78911f26e62ebf793844f9)
- Use DPDK's bitops API in dumpcap applications instead of compiler built-in functions.
  ↳ No PR: [2a682d6](https://github.com/DPDK/dpdk/commit/2a682d65f8dbe1e8be9cc2425095827e18c700e3)
- Added independent mark ID and RSS action append functions for the representor port action in the CNXK network card driver.
  ↳ No PR: [c2f3e9e](https://github.com/DPDK/dpdk/commit/c2f3e9e76f39fc925e4f3ce7b2d0551a38a17f74)
- Removed workaround for ASan in CI as the fix is integrated into the Ubuntu GHA image.
  ↳ No PR: [5744e91](https://github.com/DPDK/dpdk/commit/5744e912341ee26a0dd5b9ec28b16b8a4e45d1bc)
- Removed prefetching of mbuf and crypto_op in DPAA2 SEC event handler.
  ↳ No PR: [fa95cbb](https://github.com/DPDK/dpdk/commit/fa95cbb55c91dbbadb5f8ba1581ddfd603c446ff)
- Migrated the configuration system from warlock to Pydantic, removed the old JSON Schema configuration file, and updated related documentation.
  ↳ No PR: [b935bdc](https://github.com/DPDK/dpdk/commit/b935bdc3da26ab86ec775dfad3aa63a1a61f5667)
- Fixed compilation issues caused by implicit type conversion in the ice driver, adjusted function parameter types and removed unused auxiliary functions.
  ↳ No PR: [cc80bd1](https://github.com/DPDK/dpdk/commit/cc80bd159c5d9cf7208d44633e3a35424ed2faee)
- Updated the E830 50G network card brand string, changing E830-XXV to E830-L.
  ↳ No PR: [93eca93](https://github.com/DPDK/dpdk/commit/93eca93598431bf3fbc0e14c846f2c1b6f80a7f8)
- Optimized graphviz export: changed the text color of the sink node to dark orange and removed the ellipse shape, and changed the color of the arrow pointing to the sink node to dark orange.
  ↳ No PR: [5b8d861](https://github.com/DPDK/dpdk/commit/5b8d861cfe89ebcbb08760c7817be0b79b9ff6f9)
- Replaced non-inclusive terms in the i40e driver, added type conversions to eliminate compile warnings, and added macro definitions required to read the alternate trace buffer.
  ↳ No PR: [564c9e4](https://github.com/DPDK/dpdk/commit/564c9e44831b7d3ce06099250562e0385cd478e3), [2c68a61](https://github.com/DPDK/dpdk/commit/2c68a61b8cba07646216ddb3bdf70c83766b1706), [1f4adfe](https://github.com/DPDK/dpdk/commit/1f4adfeb5ff94a88efb00b742eff8e63671313b6)
- Defined the maximum MSIX index macro in the IAVF driver and updated the comment range, and added a macro definition for the flex descriptor status bit.
  ↳ No PR: [1cc2ffd](https://github.com/DPDK/dpdk/commit/1cc2ffd1e9d763166d0752afc7506c274d40f68b), [3a988e3](https://github.com/DPDK/dpdk/commit/3a988e3007720bdfb6fbbd674532ebb93d0279fb)
- Added log messages for flow rule creation failure scenarios to record the failure reasons.
  ↳ No PR: [0573a39](https://github.com/DPDK/dpdk/commit/0573a3928d6239822628a81efa5d0f90ee30f4e0)
- A new queue debugging dump function has been added to the baseband/acc driver, which supports outputting queue internal operation information through the new operation interface.
  ↳ No PR: [3423756](https://github.com/DPDK/dpdk/commit/3423756cf2e33cb222c2f82361c11f5d83a48ba3)
- Enhanced the frame display function of the DPAA driver in debug mode, added the ability to control frame display output through environment variables, and expanded the display content of frame parsing information.
  ↳ No PR: [480ec5b](https://github.com/DPDK/dpdk/commit/480ec5b43e51a426bf86759214b4a3b4a70ddb12)
- Added return value check for rte_eth_dev_info_get call to ensure device information is obtained successfully before using it.
  ↳ No PR: [a937954](https://github.com/DPDK/dpdk/commit/a937954e3d1ccfcc88aad472b0e6ee67f3eb560c), [69559d0](https://github.com/DPDK/dpdk/commit/69559d0df94779b2d76f991831390400e33237fe)
- Removed unused abort macro in ENA driver.
  ↳ No PR: [917b7c7](https://github.com/DPDK/dpdk/commit/917b7c78cee5ea96862fa6351a646bf305a99b6d)
- Changed bbdev structure size calculation from hardcoded constants to using sizeof.
  ↳ No PR: [77120a7](https://github.com/DPDK/dpdk/commit/77120a7b9472c6fd41aee66c29561477d7440bb4)
- Only reset the valid bit of the info ring in the baseband/acc driver to preserve data for dumping.
  ↳ No PR: [63dcaf2](https://github.com/DPDK/dpdk/commit/63dcaf20304d24305bf0113f370bea2721307c1f)
- Added more debugging logs for the NFP driver, and adjusted some log levels to assist in debugging the detection process.
  ↳ No PR: [aa6b4a8](https://github.com/DPDK/dpdk/commit/aa6b4a80a3afd5c9e3b07f6b516f44cae7505e16)
- Recalculated and limited the maximum number of descriptors based on the FD attribute offset bit width, and added runtime assertion checks.
  ↳ No PR: [b52af62](https://github.com/DPDK/dpdk/commit/b52af62f825c3c41bbafae603c9ccfcda77ffbd1)
- Lowered the level of specific error logs in the NFP driver to avoid exposing irrelevant error information to users during normal operation.
  ↳ No PR: [1a92d15](https://github.com/DPDK/dpdk/commit/1a92d15d749626f7334c19434e3e4d93f58cc037), [17d6720](https://github.com/DPDK/dpdk/commit/17d6720e0477de1ee786ac9a03f689cd9e311d98)
- Added information such as parent node ID, initialization, cleanup, statistics, and next node address and name to the node dump function.
  ↳ No PR: [0787cdb](https://github.com/DPDK/dpdk/commit/0787cdbce54381a3517c24ccec8bbb58215e17b3)
- Optimized the log output of MTU configuration in the DPAA2 network card driver, stored the MTU value when setting the MTU, and set the default MTU during initialization.
  ↳ No PR: [de08b47](https://github.com/DPDK/dpdk/commit/de08b47438a75afb6f4246d7fed10a2460797b82)
- Added debug printing function of RX parsing results and frame attribute flags controlled by environment variable DPAA2_PRINT_RX_PARSER_RESULT for DPAA2 network driver.
  ↳ No PR: [93e41cb](https://github.com/DPDK/dpdk/commit/93e41cb315db171aad78bba09b2983472b7fe8f5)
- Added soft parser loading status check in DPAA2 network card driver, and output relevant information during initialization.
  ↳ No PR: [9940078](https://github.com/DPDK/dpdk/commit/994007801e643cf5098b0b422752607d9e074cdd)
- Added software parser streaming mode validation for DPAA2 network cards, grouped supported modes and optimized error logs.
  ↳ No PR: [1cf6d18](https://github.com/DPDK/dpdk/commit/1cf6d181b58f83bd54c444499ec95380eb4b1c38)
- Removed the packed attribute of structures in the efd library and pipeline library to eliminate compilation warnings.
  ↳ No PR: [1887f91](https://github.com/DPDK/dpdk/commit/1887f919549de2821b0eeabe808a5f2b76370c34), [eca9f4f](https://github.com/DPDK/dpdk/commit/eca9f4f830bfd36c615427dd71d782146d34892b)
- Removed the function pointer validity check in the power library application, and adjusted the related header file references.
  ↳ No PR: [b21cf7d](https://github.com/DPDK/dpdk/commit/b21cf7d3b67b67e4c37803d8ff54839c6e6bdfd5)
- Removed unnecessary type conversions and used dynamic logging instead.
  ↳ No PR: [e0d9b3c](https://github.com/DPDK/dpdk/commit/e0d9b3cd6d3eec6f84ca481c8af29e36d07fbb79)
- Removed unused rx_cb array in dumpcap to save memory.
  ↳ No PR: [9bbd44d](https://github.com/DPDK/dpdk/commit/9bbd44d63846cf0771ec0f1c7e1b5a63ec5e9603)

### Others
- Optimize the NFP driver Rx buffer size setting logic to avoid a single queue configuration affecting all queues.
  ↳ No PR: [b5fae3a](https://github.com/DPDK/dpdk/commit/b5fae3a560c39b1a9a09c40dbeec2086f12ac53a)
- Add descriptive comments to Arm CPU feature enumerations.
  ↳ No PR: [c9083da](https://github.com/DPDK/dpdk/commit/c9083daf4426cc386edb3fa4594ce31119ead504)
- Add padding to passthrough data of SM cryptographic algorithm, aligned to 16 bytes.
  ↳ No PR: [f593ed5](https://github.com/DPDK/dpdk/commit/f593ed5b0ae9da85936bb4871130c56b92a35b26)
- Add packet type parsing for GVE DQ format receive path.
  ↳ No PR: [83e0cc5](https://github.com/DPDK/dpdk/commit/83e0cc58addea0976ec978efcf56851779744e1b)
- Updated arc type support for MLX5 driver flex parser, adding input IPv4 and output ESP arcs.
  ↳ No PR: [6dfb83f](https://github.com/DPDK/dpdk/commit/6dfb83f13f7a6d259e4ecd3d53d40b9ed87e2fe1)
- Add timestamp offload support for af_packet driver.
  ↳ No PR: [be10211](https://github.com/DPDK/dpdk/commit/be10211cbec25c7edf0717ba9791fc929c5f5610)
- Modify the .gitignore file and add explicit inclusion rules.
  ↳ No PR: [58ae3be](https://github.com/DPDK/dpdk/commit/58ae3be1445b9f60d7595dc8729dbb4b839a4bcf)
- In hash tests, replace the term segregate with separate in comments.
  ↳ No PR: [f81cdd7](https://github.com/DPDK/dpdk/commit/f81cdd729bdfd362ab834d4b3efe78f5ec06b56a)
- Adjust the brace positions of the three functions in the test code to comply with coding standards.
  ↳ No PR: [e04de8d](https://github.com/DPDK/dpdk/commit/e04de8d5d1cde53dd71a77811971572996185366)
- Adjust the blank format in i40e basic driver code.
  ↳ No PR: [e10fbcd](https://github.com/DPDK/dpdk/commit/e10fbcd8973af3a781044797ce80b531049ff87c)
- Fix misleading debug logs and comments in i40e_read_nvm_aq function, correct wrong write to read.
  ↳ No PR: [719ec1b](https://github.com/DPDK/dpdk/commit/719ec1bfebde956b661d403ef73ecb1e7483d50f)
- Update the version information, copyright year or build date in the README file of i40e, ixgbe and IAVF base drivers.
  ↳ No PR: [5a87641](https://github.com/DPDK/dpdk/commit/5a87641a443f11f1f63d4a9af64d3d0f8ac64f5a), [bf959e4](https://github.com/DPDK/dpdk/commit/bf959e45181947a8ee1a4b23d6a32d65198b9a28), [79c9190](https://github.com/DPDK/dpdk/commit/79c919080436d5dfabb48fe96f58a9095c7fece5)
- Fixed grammar, phrasing and documentation cross-references in the multi-process application guide.
  ↳ No PR: [c0f5a9d](https://github.com/DPDK/dpdk/commit/c0f5a9dd74f41688660e4ef84487a175ee44a54a)
- Replace discriminatory words in driver comments and change segregate to separate.
  ↳ No PR: [f2b1510](https://github.com/DPDK/dpdk/commit/f2b1510f19d7bfd386d130fa38123d6e2152cf80)
- Corrected documentation definition and description of Stats per queue feature.
  ↳ No PR: [71eae7f](https://github.com/DPDK/dpdk/commit/71eae7fe3eac90b70200460c714d1c13ee43dc25)
- Fixed an error in the structure bit field annotation in the NFP flower control message header file.
  ↳ No PR: [1a6c589](https://github.com/DPDK/dpdk/commit/1a6c58929d683bf237836583db1320fc3ddc12d6)
- Update the basic code snapshot date in the ice driver README.
  ↳ No PR: [8ca6d8c](https://github.com/DPDK/dpdk/commit/8ca6d8c48b73c8337bbaaf18f0458777c916c188)
- Unified NFP driver log format, including initial capitalization, periods, abbreviation expansion and spelling correction.
  ↳ No PR: [f6272c7](https://github.com/DPDK/dpdk/commit/f6272c7aa61f65f71fb376cb0cb3890e502f3521), [fb86136](https://github.com/DPDK/dpdk/commit/fb86136d92516499a65aa2299d575ea2da7b40d7), [5232ed0](https://github.com/DPDK/dpdk/commit/5232ed0f653d75e85c7712f370a29941b3175698)
- Fixed the problem of missing event device stop in test cases.
  ↳ No PR: [b74f298](https://github.com/DPDK/dpdk/commit/b74f298f9bfaba19527153098546fa1011c100a1)
- Upgrade ENA driver version to 2.11.0.
  ↳ No PR: [3a2509a](https://github.com/DPDK/dpdk/commit/3a2509ab1c524a7d0f106eb24f5f839db9e5bf82)
- Improve the DTS configuration API documentation to clarify the annotation requirements for Pydantic model fields.
  ↳ No PR: [3fbb93c](https://github.com/DPDK/dpdk/commit/3fbb93cff3be23a45fc1ec524f83d001a30df273)
- Added PCI virtual function MTU limit description in mlx5 driver documentation.
  ↳ No PR: [82caf3d](https://github.com/DPDK/dpdk/commit/82caf3da8a7048a9268fc58ec5647ae969fab688)
- Fixed typo in PM QoS documentation.
  ↳ No PR: [b3477a6](https://github.com/DPDK/dpdk/commit/b3477a6bae7e889955edd8b82f359868dc0abb01)
- Fixed grammar, spelling and formatting issues in DPDK 24.11 release notes.
  ↳ No PR: [84339a7](https://github.com/DPDK/dpdk/commit/84339a739845272045ce2a5e077def38c0a2170a)
