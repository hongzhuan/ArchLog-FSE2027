# Release Note

## Important Changes

### Cross-cutting / Other Architecture-related Changes

- EAL adds a static per-lcore memory variable facility and uses it for PRNG, power, and service state management. [commit](https://github.com/DPDK/dpdk/commit/5bce9bed67ad59aa5aede02256a8490d758b0c29) [commit](https://github.com/DPDK/dpdk/commit/b0faa8330bfdc919c6591850e883b57304bd0fbe) [commit](https://github.com/DPDK/dpdk/commit/2cd441bd17fc43768755162bfb218395c795b82d) [commit](https://github.com/DPDK/dpdk/commit/776d4753893335d43011f97b08d422b84a54b16c) [commit](https://github.com/DPDK/dpdk/commit/29c39cd3d54d8330ee578dd3ea27cfda1c562079) [commit](https://github.com/DPDK/dpdk/commit/13064331957930f6b6c49ad02a638d7d5516c88f) [commit](https://github.com/DPDK/dpdk/commit/b24bbaedbba2df6ad2c25bc0bbde52fb55876fdb) [commit](https://github.com/DPDK/dpdk/commit/18b5049ab4fecda6ad303606cc265d923b56da14) [commit](https://github.com/DPDK/dpdk/commit/9ebdbe62c2aaae8f71851483139b3b4dcfaf991b)

- EAL adds a static per-lcore memory variable facility and uses it for PRNG, power, and service state management. [commit](https://github.com/DPDK/dpdk/commit/5bce9bed67ad59aa5aede02256a8490d758b0c29)

### Packet Processing Nodes

- CN20K Ethernet adds basic control path, Rx/Tx function selection, scalar/vector data paths, and multi-segment Tx. [commit](https://github.com/DPDK/dpdk/commit/1bf0fd7e4f5357238e68ab2f53892aad3ba53748) [commit](https://github.com/DPDK/dpdk/commit/8bf50857ce08f9d330c25820461a2962dc2685d7) [commit](https://github.com/DPDK/dpdk/commit/ec380d45edaa00b5dc3c38d2a3432c6553ee3e30) [commit](https://github.com/DPDK/dpdk/commit/493c4fa524a266d2ee492a86857f2d643ef7acca) [commit](https://github.com/DPDK/dpdk/commit/9a8b99cf8822aa4f911da7f3ff512c6259b836ce) [commit](https://github.com/DPDK/dpdk/commit/006c1daa89b9be6fea53ea49fc34fd382ebe844d) [commit](https://github.com/DPDK/dpdk/commit/e634a59477f6c0d0ca380e32d003baed8cd2f795) [commit](https://github.com/DPDK/dpdk/commit/e829e60c6917de836b4b417961b628b438a9a4b3) [commit](https://github.com/DPDK/dpdk/commit/98613d32e3dac58d685f4f236cf8cc9733abaaf3)

- Add Realtek RTL8169 Ethernet driver, supporting hardware and PHY initialization, Rx/Tx, link and interrupt management, statistics, MTU, promiscuous mode, and port start/stop. [commit](https://github.com/DPDK/dpdk/commit/9b170cfc6303a9a9a7279149ac6800a72239ad4e) [commit](https://github.com/DPDK/dpdk/commit/88f5b657aa39dad2451fc48c3b2fd0ece82580d8) [commit](https://github.com/DPDK/dpdk/commit/1bbe869ee8571aa282a1069c0f2921e13fe58e11) [commit](https://github.com/DPDK/dpdk/commit/619f6ebce1152836c44a3e9b783d51f8c431c4a3) [commit](https://github.com/DPDK/dpdk/commit/c4adac969428db7024a1a160ef630cae250e0523) [commit](https://github.com/DPDK/dpdk/commit/8e85226086b45cc60667ad4347a75025fb59e151) [commit](https://github.com/DPDK/dpdk/commit/38589978be7d4c3e2ebc6b491c4a145dcfddc07c) [commit](https://github.com/DPDK/dpdk/commit/7d5027916b24efaf6ad974307723054c2f321aff) [commit](https://github.com/DPDK/dpdk/commit/f7327670814e69fd5b11871828065940268f664c) [commit](https://github.com/DPDK/dpdk/commit/2f198f0a20bcf10ee3188588e80b7d5e6965d2fc) [commit](https://github.com/DPDK/dpdk/commit/63d37ff9a453370a82a28ca8194f38b09aeb8191) [commit](https://github.com/DPDK/dpdk/commit/fa0b0ad6246709184d73fbc944039391c1db22be) [commit](https://github.com/DPDK/dpdk/commit/d2b39de23c1d895627d15acd0c042bb3968c10dd) [commit](https://github.com/DPDK/dpdk/commit/9514e4b6d37db561dd33448c585a9fa42a0e0283) [commit](https://github.com/DPDK/dpdk/commit/b2e17252e6161a1a2c29978bfffbc6f3b3337e8e) [commit](https://github.com/DPDK/dpdk/commit/b574fb4cc855f4e86659d37ded01e7a218c38865)

- Add Realtek RTL8169 Ethernet driver, supporting hardware and PHY initialization, Rx/Tx, link and interrupt management, statistics, MTU, promiscuous mode, and port start/stop. [commit](https://github.com/DPDK/dpdk/commit/9b170cfc6303a9a9a7279149ac6800a72239ad4e) [commit](https://github.com/DPDK/dpdk/commit/7d5027916b24efaf6ad974307723054c2f321aff) [commit](https://github.com/DPDK/dpdk/commit/f7327670814e69fd5b11871828065940268f664c) [commit](https://github.com/DPDK/dpdk/commit/2f198f0a20bcf10ee3188588e80b7d5e6965d2fc) [commit](https://github.com/DPDK/dpdk/commit/63d37ff9a453370a82a28ca8194f38b09aeb8191) [commit](https://github.com/DPDK/dpdk/commit/b574fb4cc855f4e86659d37ded01e7a218c38865)

### Event Dispatch Router

- Eventdev adds pre-scheduling and hint APIs, supported by CNXK driver, test applications, and examples. [commit](https://github.com/DPDK/dpdk/commit/acc65ee307f7a18d2d560ebcee750e5407318def) [commit](https://github.com/DPDK/dpdk/commit/c1bdd86d04d161c07c61ec1be8ef081108d29d2a) [commit](https://github.com/DPDK/dpdk/commit/4ade669c2823c0ebcaf7bfb7589db13cb2e4a6d8) [commit](https://github.com/DPDK/dpdk/commit/53e736a04dca6725b67dbe1d40b86520b0c28f97) [commit](https://github.com/DPDK/dpdk/commit/7a7a04d3ce8eab9b53d23b673dfdc71b50fd523d) [commit](https://github.com/DPDK/dpdk/commit/6cf329f9d8c2eb97c8f39becd514c14b25251ac1)

- CN20K eventdev adds SSO hardware information, device/queue/port configuration, enqueue/dequeue fast path, Rx/Tx adapter, event vector, and timer adapter support. [commit](https://github.com/DPDK/dpdk/commit/82526521ca123dc67361905e0e6e96bf2fa2602c) [commit](https://github.com/DPDK/dpdk/commit/45ce5425bbbe8c8e4c84134db792243ff0036054) [commit](https://github.com/DPDK/dpdk/commit/6976186968902cacf3922d5eb17c7f8b8a0041a8) [commit](https://github.com/DPDK/dpdk/commit/d2e685b20dcbb93bac61976eb2620a8c01c05d4d) [commit](https://github.com/DPDK/dpdk/commit/9736df4f1851d8170723cf2820387a86615d2259) [commit](https://github.com/DPDK/dpdk/commit/b08b193bceab2202aee3928a0fa2df5e5aa3ee92) [commit](https://github.com/DPDK/dpdk/commit/7473a65f2f08006e92c57bf4e411cedc80647b77) [commit](https://github.com/DPDK/dpdk/commit/638fe881ea0f4c78b48004877026b12690bde630) [commit](https://github.com/DPDK/dpdk/commit/33da486cd3676aa39bd83f92385e189f6e2c8ccd) [commit](https://github.com/DPDK/dpdk/commit/1e2d9b3dfc9a475eefa472cbcd3adbd7f43e3f04) [commit](https://github.com/DPDK/dpdk/commit/97b495c912e11167e51a58daa01e4aa88a4770dc) [commit](https://github.com/DPDK/dpdk/commit/a0fae00a033b58302ae50dfd0bf1197f1a46bbeb) [commit](https://github.com/DPDK/dpdk/commit/6305afee038f47b64236069eeb4355d28ef8fec9) [commit](https://github.com/DPDK/dpdk/commit/7c011b0223cc54e0a478dda24c544ccc55967f16) [commit](https://github.com/DPDK/dpdk/commit/d8f53c18203eb2b889eaf154af9552145353e0d1) [commit](https://github.com/DPDK/dpdk/commit/2dab30000ba66464a3c9f35c041ad0994cd3ec2c) [commit](https://github.com/DPDK/dpdk/commit/54101f84f718f583fad6dcbc81858dd5f1f4d3c1) [commit](https://github.com/DPDK/dpdk/commit/62afdd8d493d8f563c053a4afccb3c5acd1acf54) [commit](https://github.com/DPDK/dpdk/commit/b775abdd412bab2bfa698f7598979155bbbb24b0) [commit](https://github.com/DPDK/dpdk/commit/f3c7b60769f997be0c49788d7bfc515c59910f83) [commit](https://github.com/DPDK/dpdk/commit/822d4ef519f66b4f1184a1e708ed758e44b99b3a)

- CN20K eventdev adds SSO hardware information, device/queue/port configuration, enqueue/dequeue fast path, Rx/Tx adapter, event vector, and timer adapter support. [commit](https://github.com/DPDK/dpdk/commit/45ce5425bbbe8c8e4c84134db792243ff0036054) [commit](https://github.com/DPDK/dpdk/commit/6976186968902cacf3922d5eb17c7f8b8a0041a8) [commit](https://github.com/DPDK/dpdk/commit/d2e685b20dcbb93bac61976eb2620a8c01c05d4d) [commit](https://github.com/DPDK/dpdk/commit/9736df4f1851d8170723cf2820387a86615d2259) [commit](https://github.com/DPDK/dpdk/commit/b08b193bceab2202aee3928a0fa2df5e5aa3ee92) [commit](https://github.com/DPDK/dpdk/commit/7473a65f2f08006e92c57bf4e411cedc80647b77) [commit](https://github.com/DPDK/dpdk/commit/7c011b0223cc54e0a478dda24c544ccc55967f16) [commit](https://github.com/DPDK/dpdk/commit/2dab30000ba66464a3c9f35c041ad0994cd3ec2c) [commit](https://github.com/DPDK/dpdk/commit/b775abdd412bab2bfa698f7598979155bbbb24b0) [commit](https://github.com/DPDK/dpdk/commit/822d4ef519f66b4f1184a1e708ed758e44b99b3a)

## Routine Changelog

### New Features

- EAL service API adds the ability to count function calls per service. [commit](https://github.com/DPDK/dpdk/commit/a37e053b2364fc1104988285163261a8c7609dda)

- eventdev test application adds DMA adapter latency measurement. [commit](https://github.com/DPDK/dpdk/commit/bca734c27e345af500d0d951421584e2567cd107)

- DPAA2 Ethernet supports frame-context stashing. [commit](https://github.com/DPDK/dpdk/commit/c794f2cab6cc04260545784c24e3788204c44e96)

- Enhance DPAA2 IPsec receive direction flow-context handling. [commit](https://github.com/DPDK/dpdk/commit/8c8bbb14560ffda3a22de37dcd6a8301dd2508da)

- Enhance DPAA2 PDCP flow-context handling. [commit](https://github.com/DPDK/dpdk/commit/ac965c980c6164b12540ecf7205f1643ee5757d6)

- CNXK crypto supports multi-segment receive-inject packets. [commit](https://github.com/DPDK/dpdk/commit/62b577026d8b6a7059383bc4609d05ca7203f3a5)

- CNXK crypto PMD adds opaque queue handle, context flush, CPTR read/write, and queue statistics interfaces. [commit](https://github.com/DPDK/dpdk/commit/21653af489e7c695c7ddccb317f9957f93409597) [commit](https://github.com/DPDK/dpdk/commit/e5abbeeeefa5760f8516e260f739b1b3dd45bb17) [commit](https://github.com/DPDK/dpdk/commit/3ca607402c4d6b03c0deebc11d087334f31a2736) [commit](https://github.com/DPDK/dpdk/commit/0b7f67de81ecfab8a4d53c4e131b79e02a923abb) [commit](https://github.com/DPDK/dpdk/commit/bf52722b937738f50ada730bead83fb4fc43a1e2)

- EAL adds bit operation APIs, supporting atomic operations and volatile pointers. [commit](https://github.com/DPDK/dpdk/commit/471de107ae234aceea8ee43e153b4d7ec3f3c755) [commit](https://github.com/DPDK/dpdk/commit/35326b61aecb8e9653e889c217b775fcbe95e39d) [commit](https://github.com/DPDK/dpdk/commit/0883d736a7e59fc1847e9c8185dc43eb43d32630)

- Increase the maximum number of file descriptors supported by the IPC API. [commit](https://github.com/DPDK/dpdk/commit/5ff00bbc04d8338108241b083b7a6238208cfbc6)

- Eventdev adds independent enqueue capability, with implementations provided by DLB2 and DSW drivers. [commit](https://github.com/DPDK/dpdk/commit/79ca24a41c16445594303a62151ee68156a5a320) [commit](https://github.com/DPDK/dpdk/commit/6e2e98d6775b9d39ef4d5ef75d86416085154c88) [commit](https://github.com/DPDK/dpdk/commit/0dab9afe0c2d4d47f79241050e35158d53f62b01)

- Cryptodev adds queue-pair priority configuration, and crypto-perf can be used to verify this configuration. [commit](https://github.com/DPDK/dpdk/commit/6ef8e70ecfbd0963a35a301bc9d6d0745891f6e3) [commit](https://github.com/DPDK/dpdk/commit/e004aaa83a4afcc9e27b19ad2340a84fdc90f267)

- Cryptodev adds queue-pair reset API, implemented by the CNXK driver. [commit](https://github.com/DPDK/dpdk/commit/0a054e8dd5b0960eec4226821137aceb77a2bf22) [commit](https://github.com/DPDK/dpdk/commit/3be1df02fb09db123b9372e1fec6b4d741ae53d9)

- l2fwd MACsec example enables extended packet number. [commit](https://github.com/DPDK/dpdk/commit/0d187ba834b1a7f67fa73265743dfff9d8f706fe)

- Intel IPsec Multi-Buffer PMD adds SM3, HMAC-SM3, and SM4 support. [commit](https://github.com/DPDK/dpdk/commit/9a1d479742aa5e27313117915f8a465867a2d6e6) [commit](https://github.com/DPDK/dpdk/commit/add05a010671f59503198d7e5fe9fc74348aba65) [commit](https://github.com/DPDK/dpdk/commit/0c2f1b05ffc7493dada89df10ef0ad704004a870)

- Cryptodev adds EdDSA asymmetric algorithm, supported by OpenSSL, CNXK PMD, and crypto-perf. [commit](https://github.com/DPDK/dpdk/commit/8bd4315ceba8d9de9dedafdaa963ffecc09cc971) [commit](https://github.com/DPDK/dpdk/commit/5a74d7fd37debc1b4fa1fa44b82fa9cf3b87a291) [commit](https://github.com/DPDK/dpdk/commit/a8ebe94f8cc11cda874cd0353a47e78279699d10) [commit](https://github.com/DPDK/dpdk/commit/981a1ed32a7920bf0f5e2864ab1f78c296bdfaec)

- FIPS validation example supports EdDSA. [commit](https://github.com/DPDK/dpdk/commit/12ede9ac497fed989a1f4d0357e839cbe7d1e45b)

- IPsec adds stateless packet processing capability, allowing applications to manage SA state themselves. [commit](https://github.com/DPDK/dpdk/commit/aae98b8c6690ccc49d7a1536a1b1ee1264de49a7)

- Cryptodev exposes asymmetric operation capability information for driver feature discovery. [commit](https://github.com/DPDK/dpdk/commit/53c65a3ce2c6b56cf3fa71621a74b97c41432fc0)

- OpenSSL crypto PMD declares support for SM2 capability. [commit](https://github.com/DPDK/dpdk/commit/8fdfedb125beac73e4ebe14f5ffe369d0465ba19)

- Add Arm Neoverse N3 CPU configuration. [commit](https://github.com/DPDK/dpdk/commit/cdbcdc5573933d709a95668982c7e31eb9249105)

- EAL memory dump adds total memory size; procinfo can output memory heap details. [commit](https://github.com/DPDK/dpdk/commit/17bb60044bae68c0f062755527ad8febe9f448d1) [commit](https://github.com/DPDK/dpdk/commit/c33717c6f886b840e2121a14048f59d1c0929621)

- Cryptodev API and corresponding PMDs add SM4-XTS algorithm support. [commit](https://github.com/DPDK/dpdk/commit/4acc862b18a2f1691d1561f7b75542f6a056d41f)

- Graph nodes support exposing their context via pointers. [commit](https://github.com/DPDK/dpdk/commit/28f0225a9c30c6ba168c83abf23fbee9c54f562e)

- Extend Octeon EP mailbox functionality. [commit](https://github.com/DPDK/dpdk/commit/826da0f56d42e256e647b7d32b5cb567f5263d52)

- Add CN20KA model identification and CNXK PF/VF mailbox configuration support. [commit](https://github.com/DPDK/dpdk/commit/814bedeeed7ccd44191fcc7222254ece5fcc42c6) [commit](https://github.com/DPDK/dpdk/commit/966f57a6232ea2efd83cb3d12053390384f645b9) [commit](https://github.com/DPDK/dpdk/commit/61deac72abbff3924dd06937887ad399a3a42863) [commit](https://github.com/DPDK/dpdk/commit/7816df7911736f7f880db04fa62cdbd20405a63c) [commit](https://github.com/DPDK/dpdk/commit/9bd368ca311a1ede6c17bb9e39d0e30f6a9abb2d)

- CNXK Ethernet exposes IPsec SA information via telemetry. [commit](https://github.com/DPDK/dpdk/commit/d74ed1628f7e3772593be6c48f364816ae85e448)

- Allow clearing statistics on CNXK RPM, no longer restricted by the original condition. [commit](https://github.com/DPDK/dpdk/commit/1eb1bb394b013b844671bbad0a1f1048d633e8be)

- CNXK PMD adds IPsec SA management, CPT instruction submission, queue statistics, custom inbound SA, and model query APIs. [commit](https://github.com/DPDK/dpdk/commit/a72e15611303cceadc8233b6713e5978089e1587) [commit](https://github.com/DPDK/dpdk/commit/de8c60d113f0f688623f5a93b991f8b0e5dbf5f0) [commit](https://github.com/DPDK/dpdk/commit/d8c8ad3a1feef3905c8c3eb27db9d454a6e16856) [commit](https://github.com/DPDK/dpdk/commit/03b152389fb15f96e25d9acd87b84c9c22cf8b2b) [commit](https://github.com/DPDK/dpdk/commit/92fa0ac7eda65aa0b3c1fd9f8611fe9b297a6e01)

- Add CN20K PCI ID, and initialize NPA/mempool support, adapting to aura field width and mailbox changes. [commit](https://github.com/DPDK/dpdk/commit/5ed98ad510aeba72dbd3db275cbac555c3fb661b) [commit](https://github.com/DPDK/dpdk/commit/620fc02bf7ebfb9c8ca8d4a391df9e243397270c) [commit](https://github.com/DPDK/dpdk/commit/143a419edf35f3dc093b4f8f7a29163f9c075316) [commit](https://github.com/DPDK/dpdk/commit/8d1ddeb6c3382e834fbc0a459788a9f58e1ae7fd)

- CN20K adds NIX register definitions, queue configuration, bandwidth profiles, debug, and RSS support. [commit](https://github.com/DPDK/dpdk/commit/9a01217e287197cfc2ac778edcec18d84056d244) [commit](https://github.com/DPDK/dpdk/commit/4785c406c26df4f8c29a84ea89712aa95acde44d) [commit](https://github.com/DPDK/dpdk/commit/43e42816d36c7348d80104a05a30666eab733da0) [commit](https://github.com/DPDK/dpdk/commit/db5744d3cd23c485c506bc2a35e91132b1eb9ed0) [commit](https://github.com/DPDK/dpdk/commit/86667e895f5bb78f836cf93fa574c32faf4d36eb)

- bbdev adds LDPC decoder `k0` parameters, implemented by ACC and FPGA 5G FEC drivers. [commit](https://github.com/DPDK/dpdk/commit/591d38cc83f3ebe69ba44ce136170299d4825fdf) [commit](https://github.com/DPDK/dpdk/commit/cb9dc567af0392850a622e6ba80020bcc65de1e5)

- bbdev exposes statistics for the number of available enqueue descriptors. [commit](https://github.com/DPDK/dpdk/commit/f8d8fa0eea4b0d4c91da9ff3da03162135c3f706)

- bbdev and ACC add queue debug dump interfaces. [commit](https://github.com/DPDK/dpdk/commit/353e3639d458f5cdaf3d938aade25579fa490b1b) [commit](https://github.com/DPDK/dpdk/commit/3423756cf2e33cb222c2f82361c11f5d83a48ba3)

- ACC supports configuring the maximum number of queues per device. [commit](https://github.com/DPDK/dpdk/commit/21352447018b9f055161cd7546197fce82b370e0)

- VRB1 no longer advertises interrupt capabilities it does not support. [commit](https://github.com/DPDK/dpdk/commit/afa685dffeaf0e2cb96dff51963b5af415a6902e)

- EAL adds bitset type and atomic operations, used to represent service flags. [commit](https://github.com/DPDK/dpdk/commit/99a1197647d803e43a676622396ffddf6bf93b62) [commit](https://github.com/DPDK/dpdk/commit/c889c037f67342d972ef7a24580d3c24b6f33e26) [commit](https://github.com/DPDK/dpdk/commit/34ec23845d9e3fe066d8d38fba9ebb0b9e7cdb5e)

- DSW eventdev supports more event ports. [commit](https://github.com/DPDK/dpdk/commit/fb011cdae56cc698ae76b17635c5b1968f5754b4)

- NFP vDPA adds live migration, covering interrupts, VF configuration, ring index recovery, and relay threads. [commit](https://github.com/DPDK/dpdk/commit/94fde3a7f574103ad4ba274bf015bca3879e0408) [commit](https://github.com/DPDK/dpdk/commit/10421b0d90751552709498ca15fa25dfa3135495) [commit](https://github.com/DPDK/dpdk/commit/e6ac31e08c7b389994d7968dfe86186647c6f77a) [commit](https://github.com/DPDK/dpdk/commit/9725f3260004cffafe8437deb6a6bcdb18794c23) [commit](https://github.com/DPDK/dpdk/commit/02fe8366156a0bc7f3049f92120c185d11bbc217) [commit](https://github.com/DPDK/dpdk/commit/adec2a5ce47fa3fccd82c9796c71eeeb65e99700)

- VDUSE adds connection recovery capability and restricts the max-queue-pair API to be used only by corresponding devices. [commit](https://github.com/DPDK/dpdk/commit/da79cc7fda76a1e1ff9194fc54f1d948d22f4809) [commit](https://github.com/DPDK/dpdk/commit/e1808999d36bb2e136a649f4651f36030aa468f1)

- FIB rule reclamation uses RCU deferred release. [commit](https://github.com/DPDK/dpdk/commit/96c3d06a354753cdef9177e0c204c2e9361f31d5)

- Improves PCI hotplug for bound VFIO devices and promotes the vhost maximum queue setting API to a stable interface. [commit](https://github.com/DPDK/dpdk/commit/5f7b98189de733080656989d63b0e7ffd249830a) [commit](https://github.com/DPDK/dpdk/commit/d8381a8f54cdc789c4260efefb5a17b9612f417e)

- Telemetry command registration supports attaching private parameters. [commit](https://github.com/DPDK/dpdk/commit/ceb5914cd1e153b01bedd9f14a8119355114a21f)

- ICE adds tag definitions, optional signature segment flags, and E830 FEC auto-detection. [commit](https://github.com/DPDK/dpdk/commit/638604cc386b76bc50f926c2a527bfc31a35e5c6) [commit](https://github.com/DPDK/dpdk/commit/8da382fb2d77930e4c4e01f610970ef77bca85b4) [commit](https://github.com/DPDK/dpdk/commit/15490b87d9a7c3cabf41b15010f356c2e6de9485)

- Adds more PCI IDs for Intel E610 VFs. [commit](https://github.com/DPDK/dpdk/commit/5662e97457eb1133ec17f6b6060b97cc9b66da41)

- i40e adds 25G device, Rx error registers, VLAN input-set, LED query, DDP package, and X722 input-set definitions, and provides named/raw Rx descriptor views. [commit](https://github.com/DPDK/dpdk/commit/ef8d118ad5fc38db0fa035bc1eb256843ac7abeb) [commit](https://github.com/DPDK/dpdk/commit/08f6fedee453df7390ed5623d2fe5ec5ab362f53) [commit](https://github.com/DPDK/dpdk/commit/485464cf37247961fe0adbca2172a09ae0a5106b) [commit](https://github.com/DPDK/dpdk/commit/dcf9ce7d0ef28f0f58adb1a8df7617dda8a41bf8) [commit](https://github.com/DPDK/dpdk/commit/4e7dd1680896201dedcbfec4f23959198ef48163) [commit](https://github.com/DPDK/dpdk/commit/e861ed0b47fec56ecb9a5f8125e48c1048b9fdff) [commit](https://github.com/DPDK/dpdk/commit/35dac9668df5b2d1ba63bf1ccfd045eb53c614f7)

- i40e supports outputting PHY debug register information and avoids duplicate dumps. [commit](https://github.com/DPDK/dpdk/commit/10bcd34584405e96079b5291c903210cf0117465) [commit](https://github.com/DPDK/dpdk/commit/efc6a6b1facfa160e5e72f55893a301a6b27c628)

- i40e adds FLU register definitions, trace buffer read dependencies, and shadow RAM pointer definitions. [commit](https://github.com/DPDK/dpdk/commit/c13b636cd78f5994e833b5650979e6dcca0b3e92) [commit](https://github.com/DPDK/dpdk/commit/1f4adfeb5ff94a88efb00b742eff8e63671313b6) [commit](https://github.com/DPDK/dpdk/commit/c7cb270a6e66f2a2e619d8641122de8b7c66693e)

- i40e NVM get operations support custom timeouts. [commit](https://github.com/DPDK/dpdk/commit/d980a401b137a53170ce60dc94059720d9999c43)

- iavf extends PTP, SyncE, GNSS, RefSync, QGRP, and RSS hash configuration capabilities. [commit](https://github.com/DPDK/dpdk/commit/286e99f3a802381c14f19d35420c4eea03ffb4af) [commit](https://github.com/DPDK/dpdk/commit/886cc4b8696db2daf00189546486bd0b13674145) [commit](https://github.com/DPDK/dpdk/commit/7025057186d3ea52809b724305326882d0ea86de) [commit](https://github.com/DPDK/dpdk/commit/a26c6596be6c58da8fbd73d8615e3edc02e5c04b) [commit](https://github.com/DPDK/dpdk/commit/0016b690b5c836a4e6f963944ff5dc194ec3da72) [commit](https://github.com/DPDK/dpdk/commit/2381def42646b861a5da9d27b9a4917607cc51bc)

- ICE supports specifying a custom search path for DDP packages. [commit](https://github.com/DPDK/dpdk/commit/9207f93640a709cad1412430c5f0edfee3ad5a87)

- Graph API and IPv4 nodes add xstats queries. [commit](https://github.com/DPDK/dpdk/commit/070db97e017b7ed9a5320b2f624f05562a632bd3) [commit](https://github.com/DPDK/dpdk/commit/be4c0cb4901fc0703786e0d3da4e0123306e4539)

- GVE DQO RDA supports TSO, and the MANA NIC driver supports arm64. [commit](https://github.com/DPDK/dpdk/commit/403c671a46b64b6a22a0959e40b46eb6e4f05a42) [commit](https://github.com/DPDK/dpdk/commit/7649794dcfe9fff3e33f98a93dff65bd11ec3c42)

- NFP driver removes port queue number limits, adds representor queues, and supports Ethernet type flow items. [commit](https://github.com/DPDK/dpdk/commit/64e472d84a95ccd33dc3568cd84bd7aa8c0abbfc) [commit](https://github.com/DPDK/dpdk/commit/602792e55cbac4b9704104be3e9b5b4fdcfe7098) [commit](https://github.com/DPDK/dpdk/commit/761e06e2278630d47e234aae4cb8da00b7bc088a) [commit](https://github.com/DPDK/dpdk/commit/7217d258257bd85b88822f4e5f1427e7e20af799)

- GVE DQ format supports packet type parsing; af_packet supports timestamp offload. [commit](https://github.com/DPDK/dpdk/commit/83e0cc58addea0976ec978efcf56851779744e1b) [commit](https://github.com/DPDK/dpdk/commit/be10211cbec25c7edf0717ba9791fc929c5f5610)

- ENIC supports managing SR-IOV VFs via the admin channel, and adds rate capabilities and multicast MAC configuration for new models. [commit](https://github.com/DPDK/dpdk/commit/00ce43111dc5b364722c882cdd37d3664d87b6cc) [commit](https://github.com/DPDK/dpdk/commit/543617f44eec3e348ea8cd04924ef80389610d46) [commit](https://github.com/DPDK/dpdk/commit/c103585df76017fedd5b0ea2f4769fb9ee42f31f)

- Ethdev flow API supports inserting rules by index and pattern, jumping to specified tables, and provides corresponding tracepoints. [commit](https://github.com/DPDK/dpdk/commit/29e7c6263926351be4d402559a49ff346e1bcc42) [commit](https://github.com/DPDK/dpdk/commit/933f18db7951206822c1343c6f5aa5e826700412) [commit](https://github.com/DPDK/dpdk/commit/2c52a2b3eca9b619b7ab16e4e936e52f8aa3b3d3) [commit](https://github.com/DPDK/dpdk/commit/be5ded2f96072e887d5155516f8bbe69d1fb07ad)

- Ethdev/HNS3 adds register name queries, filtering by module, and telemetry display capabilities. [commit](https://github.com/DPDK/dpdk/commit/083db2ed9e9ea321f37fb49a9ea118446c04a782) [commit](https://github.com/DPDK/dpdk/commit/d916d27e3dca9d2e19e411fff9208929a7c7cbdf) [commit](https://github.com/DPDK/dpdk/commit/dd4b8bba785faf9d1bb9c4460e75068e2822bdb3) [commit](https://github.com/DPDK/dpdk/commit/99d3bd8b85d357c8d4e7ee23765a073f4970ff74)

- Ethdev adds link speed lanes configuration, and the BNXT driver implements this capability. [commit](https://github.com/DPDK/dpdk/commit/60bac72264d8dcec55d58919e4710a70968ae4a8) [commit](https://github.com/DPDK/dpdk/commit/dc6810a2ab7b4a7c5fc45cb3e82362178a190821)

- NFP supports setting device packet types. [commit](https://github.com/DPDK/dpdk/commit/a498019d793b3d5ae354a1a947b6bec3bd16fb5f)

- DPAA bus exposes port buffer manager statistics. [commit](https://github.com/DPDK/dpdk/commit/d2536b006d788039112f9646e4fb2a91ecb6ae45)

- DPAA NIC supports Tx confirmation queue configuration and separation, and adds transmit/receive timestamps and IEEE 1588 PTP support. [commit](https://github.com/DPDK/dpdk/commit/58e0420f72f89cb022657253cd1b75d9bc47e5a7) [commit](https://github.com/DPDK/dpdk/commit/d11482d91b23e2ff2be36a6a0b6b026c5d0bf04e) [commit](https://github.com/DPDK/dpdk/commit/615352f522707e432c1a77f6e8f81a807d43866e) [commit](https://github.com/DPDK/dpdk/commit/73585446921304f543360af104473a955ae46df9)

- Enhances DPAA packet parsing and frame display, mempool debugging, and adds OH/ONIC port modes. [commit](https://github.com/DPDK/dpdk/commit/a350a9543d4e7a842e0ad82ef4ad81c7314f7c2e) [commit](https://github.com/DPDK/dpdk/commit/480ec5b43e51a426bf86759214b4a3b4a70ddb12) [commit](https://github.com/DPDK/dpdk/commit/b0827a40f1b9c9562fb14dca69b5e033e8547deb) [commit](https://github.com/DPDK/dpdk/commit/a0edbb8a8e521e0720d31fd910bd9dce41874d9c) [commit](https://github.com/DPDK/dpdk/commit/7e5f49ae767da93486d28142ef53a8fd745f240b)

- NFP driver identifies PF ports, reserves expansion ROM BARs, and adjusts firmware version and specific BSP compatibility handling. [commit](https://github.com/DPDK/dpdk/commit/c2b4f0d5b1c8705ec0a0bcaab37f305ce0b2137e) [commit](https://github.com/DPDK/dpdk/commit/000feb4c417c9776236342e524d98e61e43e2f12) [commit](https://github.com/DPDK/dpdk/commit/d5c18ff54d964ee2e576469f2a9b5cb448fa025d) [commit](https://github.com/DPDK/dpdk/commit/e57a531c9b681d88900cb1ba1d4119559c0e5bb9)

- NFP supports different BAR sizes and flow steering rule limits, and can query NSP capabilities and load firmware from flash. [commit](https://github.com/DPDK/dpdk/commit/19bd7cce5705e14f59aeb7bc28dddd9c8cab913f) [commit](https://github.com/DPDK/dpdk/commit/66df893f2fefc50fb6a53a0cfcaa8aed4461442b) [commit](https://github.com/DPDK/dpdk/commit/9e76c352120f8860a75234699afa371ec6aa2e9a) [commit](https://github.com/DPDK/dpdk/commit/08ea495d624b5ef9899e43a62bfe87ecd1c5b1e4)

- Ethdev adds explicit configuration recovery control and driver callbacks; configuration is only restored when requested, and MLX5 disables this flow by default. [commit](https://github.com/DPDK/dpdk/commit/a98bd0fe444c3cdbce7d40cd5545abb38aca9469) [commit](https://github.com/DPDK/dpdk/commit/5e46b176d37787c5536d48b23fff8baf5d674c88) [commit](https://github.com/DPDK/dpdk/commit/e14ebecf109ef8ffca62e173ad8147e928f54e9e) [commit](https://github.com/DPDK/dpdk/commit/6a3446cf577b70edbb072be19c7466b006ee2aa2)

- NTNIC driver updates FPGA version information. [commit](https://github.com/DPDK/dpdk/commit/a1c2c9db7cfeaeb6925141428b4d356c4bdb9f6f)

- NTNIC documentation adds link status capability description. [commit](https://github.com/DPDK/dpdk/commit/4ea73e921f9ceea16a8165c9d477fd1442373a92)

- NTNIC adds hardware flow engine and ethdev flow API infrastructure, including classification, matching, hashing, queue selection, fragmentation, packet editing, and related FPGA modules, and provides basic queue operations. [commit](https://github.com/DPDK/dpdk/commit/36cf85c8997500c90cd1875bbe43190124660a12) [commit](https://github.com/DPDK/dpdk/commit/0e5e289e4b15ae8032ddb819dce934ae3736a28d) [commit](https://github.com/DPDK/dpdk/commit/0ea00f33754b342d95623c9af81d827a06c31f58) [commit](https://github.com/DPDK/dpdk/commit/8df4a5f8b10fbc2124a346fd5f2d027ba5718117) [commit](https://github.com/DPDK/dpdk/commit/e3723ca6f492f3b1df4799ae9248860ddf214be3) [commit](https://github.com/DPDK/dpdk/commit/636b2cfe0259549bb8df98c30651c90355b679b7) [commit](https://github.com/DPDK/dpdk/commit/3005c75d6b55c73eeb2c25406b7901bac5b54d6d) [commit](https://github.com/DPDK/dpdk/commit/cec43fab911c9ff28cb2d00a72c306572f1d09e9) [commit](https://github.com/DPDK/dpdk/commit/7d90a4405e889f7edce73be8b541fc14e0192b61) [commit](https://github.com/DPDK/dpdk/commit/a5a5d5bb316a1b65c92bdc436462b9e24d051108) [commit](https://github.com/DPDK/dpdk/commit/b95f1cd053cee23862a0dfc613e95e86dfd5f3aa) [commit](https://github.com/DPDK/dpdk/commit/8c545325ec2b7a6e787d6ca156cc0b2501c96cac) [commit](https://github.com/DPDK/dpdk/commit/7d65ee1accfb3ee909f4147971738d824243d161) [commit](https://github.com/DPDK/dpdk/commit/a653fa9c505d214ef5dd0c639b793cd281d6d4a6) [commit](https://github.com/DPDK/dpdk/commit/f543ca6b9ab2b09750b2e2d44737b0af1ff4df2e) [commit](https://github.com/DPDK/dpdk/commit/d42029a54dc9ace2bb1ed1769f9877949730ae67) [commit](https://github.com/DPDK/dpdk/commit/55f767cb7f66a255159dd5ffb22103fc7ab38072) [commit](https://github.com/DPDK/dpdk/commit/689a97b08f1075dc78a3d9ec2cf5802a72f71db2) [commit](https://github.com/DPDK/dpdk/commit/0338fef450a4be0f2ccb7cc491e16d6a80caa504) [commit](https://github.com/DPDK/dpdk/commit/7f058028ff772ef7a413a6fa41e87f41276df110) [commit](https://github.com/DPDK/dpdk/commit/1d3f62a0c4f1f4e2e9ac26aaf840d3e050bc4d86) [commit](https://github.com/DPDK/dpdk/commit/7917b0d38e92e8b9ec5a870415b791420e10f11a) [commit](https://github.com/DPDK/dpdk/commit/6e8b7f11205f4956756c3c53868b55059e8f6609) [commit](https://github.com/DPDK/dpdk/commit/fbe2726faa592b7ffee79b04083d9c2cc69c77f7) [commit](https://github.com/DPDK/dpdk/commit/059dfc39e94dd5482f3b07faee60ead36401a43b) [commit](https://github.com/DPDK/dpdk/commit/afad5ac406e3896ee8565f7e21da896d2320c427) [commit](https://github.com/DPDK/dpdk/commit/0e474ae51f2a6531b7410b24e80cf12d72a16582) [commit](https://github.com/DPDK/dpdk/commit/7fadd2ba32137dae8cfe1e4634c1b67a6d29e35a) [commit](https://github.com/DPDK/dpdk/commit/87ad21510b751f799286b3c2cb8a62157332f536) [commit](https://github.com/DPDK/dpdk/commit/4d4e9018bea75f85f88c9cff51e80f1b2dbe0c90) [commit](https://github.com/DPDK/dpdk/commit/9bd7e52d03b1963bda7380f8bceea616bc353d39) [commit](https://github.com/DPDK/dpdk/commit/fe91ade9f5dbda414350a18f6cd8b0b1d9942649)

- NTNIC enhances Ethernet configuration and queue management, supporting virtio split/packed virtqueues, descriptor transmit/receive, availability monitoring, and packet management. [commit](https://github.com/DPDK/dpdk/commit/b0cd36e9608c89381bda58ba746d39f90202571a) [commit](https://github.com/DPDK/dpdk/commit/5284180a54988cbf612c66ae864286bb9ce93ea0) [commit](https://github.com/DPDK/dpdk/commit/6b0047fadf4116f0e714998d0b82aec910ef6ead) [commit](https://github.com/DPDK/dpdk/commit/da25ae3c88fd38f583d38f9008e5efc4ea6046e9) [commit](https://github.com/DPDK/dpdk/commit/576e77213f0d333284d740acdbbe8de510ab7f1c) [commit](https://github.com/DPDK/dpdk/commit/e13da07fd9fda5a248abf503d3272a4efcbf44e8) [commit](https://github.com/DPDK/dpdk/commit/01e34ed9c756c0db67af45639dd1bba1040e8dd2) [commit](https://github.com/DPDK/dpdk/commit/67aee0a69665496f9369f00619d0259c8f89b2fe) [commit](https://github.com/DPDK/dpdk/commit/f7b881659406fcece705eef3fbc042a8e62d3400) [commit](https://github.com/DPDK/dpdk/commit/20ab0df3dc7c0518d579b6660e531492dad17060) [commit](https://github.com/DPDK/dpdk/commit/af30088786c2eb65754b258ab8a66d2f212e5dba) [commit](https://github.com/DPDK/dpdk/commit/f0fe222ea9cfe3c8a6972318d02a81a637aefd47) [commit](https://github.com/DPDK/dpdk/commit/9c2e6e75f695f1c2ab1d2df99f1b4f427357609c)

- Ethdev adds a frequency adjustment API, which ICE uses for PTP clock adjustment. [commit](https://github.com/DPDK/dpdk/commit/be86a6823f5ae08efbdc11297425fa844508a15d) [commit](https://github.com/DPDK/dpdk/commit/c37d50533798987027b89033ac31dac449ccca15)

- Enhances the NFP flower service framework. [commit](https://github.com/DPDK/dpdk/commit/ebb45428f493df4aed55ac3b31bf6c98de71162e)

- Ethdev adds traffic manager node queries, and the ICE driver implements this query. [commit](https://github.com/DPDK/dpdk/commit/25a2a0dc3de31ca0a6fbc9371cf3dd85dfd74b07) [commit](https://github.com/DPDK/dpdk/commit/bd6bbe6db3585d0cb40cebb945a6444f95b4cb88)

- testpmd adds device EEPROM configuration and LED on/off control commands. [commit](https://github.com/DPDK/dpdk/commit/5478054254ca86b6816514b9acd093c51a6d7ffb) [commit](https://github.com/DPDK/dpdk/commit/045e35aa3fd6a9f82a6b30be81403a77fe4ee551)

- MLX5 enhances flex parser support, adds tunnel flex item queries, and fixes protocol validation, header length, and field conversion. [commit](https://github.com/DPDK/dpdk/commit/821a6a5cc4951337a7eac64b6cce6a25c01be442) [commit](https://github.com/DPDK/dpdk/commit/6dfb83f13f7a6d259e4ecd3d53d40b9ed87e2fe1) [commit](https://github.com/DPDK/dpdk/commit/850233aca685ed1142ae2003ec6d4eefe82df4bd) [commit](https://github.com/DPDK/dpdk/commit/624ca89b57550f13c49224d931d391680dc62d69) [commit](https://github.com/DPDK/dpdk/commit/e46b26663de964b54ed9fc2e7eade07261d8e396) [commit](https://github.com/DPDK/dpdk/commit/16d8f37b4ebb59a2b2d48dbd9c0f3b8302d4ab1f) [commit](https://github.com/DPDK/dpdk/commit/3847a3b192315491118eab9830e695eb2c9946e2) [commit](https://github.com/DPDK/dpdk/commit/97e19f0762e5235d6914845a59823d4ea36925bb) [commit](https://github.com/DPDK/dpdk/commit/b04b06f4cb3f3bdd24228f3ca2ec5b3a7b64308d)

- af_packet driver supports updating link status. [commit](https://github.com/DPDK/dpdk/commit/dcb035b0ed26c9b38d569f16310dd9326680926c)

- DTS adds batch packet transmit/receive, reproducible random packets, testpmd port/queue/MTU operations, Scapy Python shell, and testpmd output parsing. [commit](https://github.com/DPDK/dpdk/commit/0bf6796a8ca351fb79a62841c0afcd35576fcb9a) [commit](https://github.com/DPDK/dpdk/commit/cfe40bac95fb9c839f1c151f6c101e53e0cbfb63) [commit](https://github.com/DPDK/dpdk/commit/f51557fb27115ffa4487c5807ebca77023c3f484) [commit](https://github.com/DPDK/dpdk/commit/2ecfd1267a070ccf13c3f43841e14e62289acc1e) [commit](https://github.com/DPDK/dpdk/commit/07816ead4d1f660663aa9077b931ffb35f053a82) [commit](https://github.com/DPDK/dpdk/commit/85d15c7c93c8f0afaba08584834047d7df0f2c79) [commit](https://github.com/DPDK/dpdk/commit/9910db35962bb22af0b02aa28025720ebf31278a) [commit](https://github.com/DPDK/dpdk/commit/1a1825962777c33c5fe6b3a547e1e61168906541) [commit](https://github.com/DPDK/dpdk/commit/2e69387a656396a7382fe27d8d9f61f1b5890573) [commit](https://github.com/DPDK/dpdk/commit/99740300890620065d06277811c81b33cd302d39) [commit](https://github.com/DPDK/dpdk/commit/a91d5f4748c6feeff571439c5f5c26c4c92edc9a)

- DTS improves testpmd port exception handling and mounts hugepage with administrator privileges. [commit](https://github.com/DPDK/dpdk/commit/618d9140e5efd9c59a8143b95ac6007961d4db7d) [commit](https://github.com/DPDK/dpdk/commit/224c1f0ebb91f94bc462f4d3757fe2051d515ac1)

- DTS adds test case marking/skipping mechanism, simplifies topology and generic, NIC, Rx offload, port and VLAN capability queries. [commit](https://github.com/DPDK/dpdk/commit/b6eb5004460e1e96269a29a54ae70c24611ad4b0) [commit](https://github.com/DPDK/dpdk/commit/566201aebdda2aa2b290d551b8f01cb329daf428) [commit](https://github.com/DPDK/dpdk/commit/0b5ee16d1bee1a398aabd31de6597e391969b53e) [commit](https://github.com/DPDK/dpdk/commit/eebfb5bb7b1427e0ba2c48190230cb8701517766) [commit](https://github.com/DPDK/dpdk/commit/c89d003806033a5f49befaef758f9cfe43d46d94) [commit](https://github.com/DPDK/dpdk/commit/c0119400ca86fce3cfeca68000e8525ef1d69912) [commit](https://github.com/DPDK/dpdk/commit/039256daa8bfa9d258b57b5fd56c12df9891721f) [commit](https://github.com/DPDK/dpdk/commit/a79884f9baa06eb9220344659ef3d12132428f9d) [commit](https://github.com/DPDK/dpdk/commit/d64f6ba5f38a847b540fe1e3a592b82ec56fa32c) [commit](https://github.com/DPDK/dpdk/commit/1a7520a1b744b9fff07a5b18c0d0ca0121535844)

- devbind supports device binding in VFIO non-IOMMU mode. [commit](https://github.com/DPDK/dpdk/commit/6ca0f1c8450d6e28926cad33c6500ad487f4cfdb)

- dmadev supports strict-priority configuration. [commit](https://github.com/DPDK/dpdk/commit/2dff0bcd3b54bc3279de42123aa618620224ad44)

- mldev adds queue-pair count configuration, data type conversion interface, and scale and zero point in I/O information. [commit](https://github.com/DPDK/dpdk/commit/804786f1012a35ee665e9d0fdf3bee1847a374fc) [commit](https://github.com/DPDK/dpdk/commit/65282e9f8e118a4ca977d1aee2d7f51f44e9bc1b) [commit](https://github.com/DPDK/dpdk/commit/fe8eba692c59a92c9308f1fe429b101b9f2377bf)

- Network library adds more ICMP type and code definitions. [commit](https://github.com/DPDK/dpdk/commit/87bde5ae68732ba62b658411fffd6abce8c80553)

- Adds driver development guide, explaining design and submission specifications for new drivers. [commit](https://github.com/DPDK/dpdk/commit/ad6833e5accbf67b4e1e8c9ca4911ba1163d3cb5)

- Network library and flow API add IPv6 traffic class and flow label fields. [commit](https://github.com/DPDK/dpdk/commit/cba27998dc8124f0d816f6342dff7451b51fe5e0)

- Rawdev API can get device structure by device ID. [commit](https://github.com/DPDK/dpdk/commit/3ee7a3e0e0e0f5a81a4b102a834697bc488fb32f)

- HNS3 flow supports generic tunnel match, VLAN match mode parameter, and outer VLAN matching. [commit](https://github.com/DPDK/dpdk/commit/90294fa5bc3ab8d0592bbde190dcc8b614850aad) [commit](https://github.com/DPDK/dpdk/commit/bf16032eb1e62338e02b1278e10033366448c5bc) [commit](https://github.com/DPDK/dpdk/commit/a47328471c9a297dbe6caddf9db867cddc902f6d)

- ICE supports selecting DDP package; ixgbe provides per-queue statistics for fewer queues. [commit](https://github.com/DPDK/dpdk/commit/9dd6dd1db8344cd2e389687d97e5272a98498773) [commit](https://github.com/DPDK/dpdk/commit/2de23282c17878ffdab7fac276c2c18b608d114d)

- CNXK DMA supports queue priority; CNXK representor events use shared mailbox and are handled uniformly. [commit](https://github.com/DPDK/dpdk/commit/fca0bae93126541c90173d84dae1ead2fe9eeacc) [commit](https://github.com/DPDK/dpdk/commit/e66a6e5401ed8dc1e03e42af516deb8b8b2dfac8) [commit](https://github.com/DPDK/dpdk/commit/03b8c847479e22cf5e955bf1dff4759c4e563b44)

- CNXK flow adds flow-mark action and single rule dump, and supports updating representor RSS rules via PF and handling RSS action. [commit](https://github.com/DPDK/dpdk/commit/c2f3e9e76f39fc925e4f3ce7b2d0551a38a17f74) [commit](https://github.com/DPDK/dpdk/commit/abdd7a9d6be5fa1ad44cf3eecd71e812b8bffbcb) [commit](https://github.com/DPDK/dpdk/commit/29a8df5cb664feb6f182c07868c49c0f5c9a4c46) [commit](https://github.com/DPDK/dpdk/commit/0981a22ec3359793e7515decb07adc5a13d772c0)

- ACC VRB2 PRQ device extends FFT support. [commit](https://github.com/DPDK/dpdk/commit/7a875f5697aaab632e45d191888ceda35f78adb0)

- Configure higher maximum lcore count for AMD EPYC Zen5. [commit](https://github.com/DPDK/dpdk/commit/892bf8cf7ea1591e71f398657c2d4a29cd316d06)

- Import Linux VDUSE uAPI header files and switch vhost to use this interface definition. [commit](https://github.com/DPDK/dpdk/commit/cf97dfd12eaf3617cf7243226efa4940729c9a9a) [commit](https://github.com/DPDK/dpdk/commit/b212c2fc2cd66f21272f48da3bb2e68513c5d92a) [commit](https://github.com/DPDK/dpdk/commit/9fec3f0569087de06666129c7f2badaf5be2776e)

- Promote EAL power intrinsics, application lcore usage, and memzone segments configuration APIs to stable interfaces. [commit](https://github.com/DPDK/dpdk/commit/86a308fffa7752e460dcc9d8dba632f21ec3a8f3) [commit](https://github.com/DPDK/dpdk/commit/9625d8dbd9248490026088a7f861c3fc03e4b139) [commit](https://github.com/DPDK/dpdk/commit/40e6cf97d3a785645f075bc40a051502f935881d)

- MLX5 refactors control flow rule management, adds unicast DMAC/VLAN rule tracking, legacy/dynamic rule registration, and filtering processing optimization. [commit](https://github.com/DPDK/dpdk/commit/a977e2b5b2768e74019ccab52943b7c0d3c30470) [commit](https://github.com/DPDK/dpdk/commit/9660a4e62afd7aef519b306da8eaeb1197da635e) [commit](https://github.com/DPDK/dpdk/commit/da7f82b0af62649612979f6f944ca0fdd8148c4e) [commit](https://github.com/DPDK/dpdk/commit/04ea84684aa296659dac15892abadfa4ef083faa) [commit](https://github.com/DPDK/dpdk/commit/d6708a9d29e48595202a816df1aedd082003550c) [commit](https://github.com/DPDK/dpdk/commit/80a5af9f2adb23f1f13c34014f84abbf45abcadc) [commit](https://github.com/DPDK/dpdk/commit/cf99567fe566fb679a2d2485ab7c113a42df04f7) [commit](https://github.com/DPDK/dpdk/commit/86d09686c6c623adf6edd40d1217b48a8e56a425) [commit](https://github.com/DPDK/dpdk/commit/d9f284954a7387789fa6658c284a00de647a692d) [commit](https://github.com/DPDK/dpdk/commit/465328609aeca77f455175b12440233dbcc5a826)

- MLX5 supports configurations without host PF. [commit](https://github.com/DPDK/dpdk/commit/6d1f4393349fc98397b409af89642c4a2aa3ee19)

- MLX5 HWS adds STE array matcher, and supports inserting flow rules by index and jumping to specified flow table. [commit](https://github.com/DPDK/dpdk/commit/486f9aac0cbe2598a76c853890c1d557747f71cf) [commit](https://github.com/DPDK/dpdk/commit/efb62499c623db13b7396231d0da8d1906d23d9b) [commit](https://github.com/DPDK/dpdk/commit/e87a9b609fb1eea5ebc67eca3eb379beba967e7f) [commit](https://github.com/DPDK/dpdk/commit/36c379c82e82bb7a60d17a2bb654988df0ea82ae) [commit](https://github.com/DPDK/dpdk/commit/af154d7a00441b54ea1439cbcd4b2d0e9fc0626a)

- Improve EAL log initialization and option parsing, support syslog/systemd journal, timestamps, colors, and print hooks, and avoid duplicate reporting of initialization failures. [commit](https://github.com/DPDK/dpdk/commit/9eeefca0c0d375dd4c76d3630d5a3913a8f94d96) [commit](https://github.com/DPDK/dpdk/commit/9a4276f92d3d9703c3509c67629a0fa3632d53a6) [commit](https://github.com/DPDK/dpdk/commit/72bf6da85a657dc4dd0662f1cd854dcc0da6da07) [commit](https://github.com/DPDK/dpdk/commit/c4e03aca4a241fb7bbd7754801604171412c5a0f) [commit](https://github.com/DPDK/dpdk/commit/985130369be32dd68ca104c1ccc86716f6e2bb7b) [commit](https://github.com/DPDK/dpdk/commit/2773d39ffee46f66fd628cebdd401d89fce09f1f) [commit](https://github.com/DPDK/dpdk/commit/630cdfcd69c90dcdf54fcf6be05f73fd1ac1e0a9) [commit](https://github.com/DPDK/dpdk/commit/62ae1149f2bdaed3482abb08f2e255f1ac4746e7) [commit](https://github.com/DPDK/dpdk/commit/9da0dc6c0331a65e841d27dde7cae4441294a313) [commit](https://github.com/DPDK/dpdk/commit/259f6f78094d0fa33ce2ffe298b8df526c535f3b)

- Limit lcore variable maximum capacity to 128 KiB. [commit](https://github.com/DPDK/dpdk/commit/f2fd6c2e080c0c595bcc72d8c05d9e1014d398e2)

- Add transport-mode ESP packet type, and MLX5 supports this type. [commit](https://github.com/DPDK/dpdk/commit/2ee0e591d24be762a8046307eaeb1dcc87504a11) [commit](https://github.com/DPDK/dpdk/commit/a371119084b81f77400fa3aed061d570cfc0eefe)

- DPAA2 DMA supports configuring route by PCIe port parameter, improves QBMAN DQ storage, and adapts short frame descriptor, maximum descriptor count, and copy return value. [commit](https://github.com/DPDK/dpdk/commit/3d990faa3f51f4f2ef8198f2971837cfae9ccaa9) [commit](https://github.com/DPDK/dpdk/commit/12d98eceb8ac89d6284a2a56f9b83cca40b73e80) [commit](https://github.com/DPDK/dpdk/commit/388e888dc082520f3dbe6318ae32fbf99695cf4c) [commit](https://github.com/DPDK/dpdk/commit/b52af62f825c3c41bbafae603c9ccfcda77ffbd1) [commit](https://github.com/DPDK/dpdk/commit/dcb9be853be46e1bdb78911f26e62ebf793844f9)

- DPAA DMA supports burst-capacity query, silent mode, scatter-gather, and configurable error checking. [commit](https://github.com/DPDK/dpdk/commit/1686d80952feaef77c66c5d8ba85d1b70721fc62) [commit](https://github.com/DPDK/dpdk/commit/7a7bb89e34b33b10eb149bf5934ff9900d19062e) [commit](https://github.com/DPDK/dpdk/commit/a77261f61245cf1e1880bd1c40511de523618c9f) [commit](https://github.com/DPDK/dpdk/commit/a63c6426fdfd9233ba9c7d4503e52bff3732fe69)

- DPAA2 Ethernet supports PTP one-step timestamp. [commit](https://github.com/DPDK/dpdk/commit/2013e3080894eab440c8fbe5a39fe00ca81066d1)

- FSLMC bus hides DPCON close internal symbols and supports device close operation. [commit](https://github.com/DPDK/dpdk/commit/1eb72b977b2cf2d82bcf116c241f03f286b5663f) [commit](https://github.com/DPDK/dpdk/commit/274fd921ff7f2829c4ddb8f488a5a3e17499aad2)

- DPAA2 Ethernet supports CVLAN DPDMUX. [commit](https://github.com/DPDK/dpdk/commit/cfe96771186470ad71d6b0ac9bbadfb1057cd572)

- DPAA2 Ethernet supports getting and updating DPNI link state. [commit](https://github.com/DPDK/dpdk/commit/25dd1fd045ed230f7d6388be4044ebf16912da3a) [commit](https://github.com/DPDK/dpdk/commit/263377be771f09a20197c30ce83ea44922a4e8fe)

- DPAA2 provides APIs to query port driver and endpoint name. [commit](https://github.com/DPDK/dpdk/commit/72cd5a480180457369d1cd369da664c4ebc7cad7) [commit](https://github.com/DPDK/dpdk/commit/a0f8ddc41218687134b33f6a462ff0b7eb04df65)

- Enhance FSLMC VFIO multi-process support, dynamically configure IOVA mode, directly get/release VFIO group FD, and provide DMA mapping API. [commit](https://github.com/DPDK/dpdk/commit/0e603d80cea6d546e3c0d283a5d751eab8eaa662) [commit](https://github.com/DPDK/dpdk/commit/57cb02edf1224b0464dd1744a7f540c8f7f21a08) [commit](https://github.com/DPDK/dpdk/commit/3b5f8dfab7e85c180cc64e130c33cee4b5d43c28) [commit](https://github.com/DPDK/dpdk/commit/a3c123e22dc685db778de34edb234642cd6e17ac) [commit](https://github.com/DPDK/dpdk/commit/8831b45622a9bb4a76269854518a556b17ac825f) [commit](https://github.com/DPDK/dpdk/commit/12dc2539f7b12b2ec4570197c1e8a16a973d71f6)

- DPAA2 flow supports VXLAN, tunnel inner protocol, eCPRI, GTP, IPsec AH/ESP matching, enhances raw-flow/soft-parser validation, and supports multi-rule extraction. [commit](https://github.com/DPDK/dpdk/commit/068be45fb5363dc9f79821a133f13d8bd781d26d) [commit](https://github.com/DPDK/dpdk/commit/93e41cb315db171aad78bba09b2983472b7fe8f5) [commit](https://github.com/DPDK/dpdk/commit/e21bff64e25667bddb8889e2d34fc7226e21e057) [commit](https://github.com/DPDK/dpdk/commit/200a33e4c2b0f401a9bfb3cc4a8f3fe8ad8923ad) [commit](https://github.com/DPDK/dpdk/commit/39c8044ffb7bb6956573fc63312e3f93170ce57b) [commit](https://github.com/DPDK/dpdk/commit/9ec293434e90e95cdbbc4b9fff5370e250e1af20) [commit](https://github.com/DPDK/dpdk/commit/a8a6b82e80ef3f96ca3370a98c67ae09df940886) [commit](https://github.com/DPDK/dpdk/commit/146c745e308825bdd4280f17506a3ff92eb9c0a2) [commit](https://github.com/DPDK/dpdk/commit/994007801e643cf5098b0b422752607d9e074cdd) [commit](https://github.com/DPDK/dpdk/commit/1cf6d181b58f83bd54c444499ec95380eb4b1c38) [commit](https://github.com/DPDK/dpdk/commit/4cc5cf4a291d79efe6fd0ffcc9dbdd25549c654a) [commit](https://github.com/DPDK/dpdk/commit/25e5845b5272764d8c2cbf64a9fc5989b34a932c)

- DPAA2 Ethernet supports software taildrop, mbuf drop-priority marking, and VLAN traffic splitting. [commit](https://github.com/DPDK/dpdk/commit/c3ffe74d85beb05784607a256ce47d95b91fb1de) [commit](https://github.com/DPDK/dpdk/commit/7994a12c4eb9a6bfe05c9c7c8de1d8d0bb427293) [commit](https://github.com/DPDK/dpdk/commit/4160359077073d148557297ac8c6c7b94ea148f9)

- Power module adds AMD EPYC uncore support and CPU-wide PM QoS API; l3fwd-power can configure PM QoS. [commit](https://github.com/DPDK/dpdk/commit/da4d64d0e80343d54ec22b583c6cc606826e73ba) [commit](https://github.com/DPDK/dpdk/commit/dd6fd75bf662e89edf2cda8f34c37e762e79c274) [commit](https://github.com/DPDK/dpdk/commit/4d23d39fd06ed89b2d2566273b95bbecbd48ed83)

- Hash library adds dynamic polynomial calculation and RSS hash key generation interfaces. [commit](https://github.com/DPDK/dpdk/commit/f9773e6676950b986c2375d9ac0bcbce8ea1b469) [commit](https://github.com/DPDK/dpdk/commit/6addb78158c232bfbb13561c8cbb7be33fb0d4a1)

- NFP Ethernet extends multi-PF management, initializes PF representor, and supports receive/transmit and control operations for multiple PFs. [commit](https://github.com/DPDK/dpdk/commit/619ea0b6a5489de8ae9b5c45634dca78ca79cb56) [commit](https://github.com/DPDK/dpdk/commit/cb6448f173688d8691494925ae2fa9d35546e3ff) [commit](https://github.com/DPDK/dpdk/commit/99da56de8c8402c38ca9985c7dd881ae33fd4a19) [commit](https://github.com/DPDK/dpdk/commit/62b609721dc52ac6b520d77fadd56de50fc6f88d) [commit](https://github.com/DPDK/dpdk/commit/636e133ec8913d8a5e964289501060b97e7d4053)

- ENA driver upgraded to 2.11.0, and reports malformed Rx descriptor errors. [commit](https://github.com/DPDK/dpdk/commit/3a2509ab1c524a7d0f106eb24f5f839db9e5bf82) [commit](https://github.com/DPDK/dpdk/commit/7a166990faa46a470f16e7c96404c9288f2e1a86)

- NTNIC flow offload adds configuration, profile, and create/destroy management, and supports queue, mark, jump, drop, TCP, VLAN actions and Ethernet/IPv4/ICMP/UDP flow items. [commit](https://github.com/DPDK/dpdk/commit/b01eb812018690b6ec94303a4cdb78bd3d7439a9) [commit](https://github.com/DPDK/dpdk/commit/ed01e43664aaa98b5660972e9b18645080afcc4e) [commit](https://github.com/DPDK/dpdk/commit/e526adf1fdef0cf12afe5c03c59f7591bd197591) [commit](https://github.com/DPDK/dpdk/commit/52fae3f41b7a4cdd23d61c65e4712982970e1240) [commit](https://github.com/DPDK/dpdk/commit/11ea97805ba167864f318bd32dcd309bf33a4d49) [commit](https://github.com/DPDK/dpdk/commit/2005c5493344798df735cfbd1f3b7ac6b97a3b1c) [commit](https://github.com/DPDK/dpdk/commit/8385ba0e4008d6a02af5fae8576e119301208b1a) [commit](https://github.com/DPDK/dpdk/commit/e02fdb65c2a8a90f4457a04a37a9e7bca4410434) [commit](https://github.com/DPDK/dpdk/commit/6fec9a9a12e192efdd750509b0f411b63daed75e) [commit](https://github.com/DPDK/dpdk/commit/b8890554b8075bce07d290bef76ebdd76ea55d7b) [commit](https://github.com/DPDK/dpdk/commit/749527702bd0ac78f4ff8cea56952bbf2c407f4d) [commit](https://github.com/DPDK/dpdk/commit/8006d07856e01873c9bcf5409c2b9993c7569ae8) [commit](https://github.com/DPDK/dpdk/commit/ba8c9f967b682950de9496dcefef8b25641fa4e5) [commit](https://github.com/DPDK/dpdk/commit/29584e9dc47b60df55e6e05942d1507ba5db6e9b) [commit](https://github.com/DPDK/dpdk/commit/4e2798a722f6b50c103a80d4c16b88ff7ffdfdf1) [commit](https://github.com/DPDK/dpdk/commit/43999d0d4ddcc5cd252cbff2afc00298ad5b1b18) [commit](https://github.com/DPDK/dpdk/commit/47003b93c375a41889d68e4bf3fc9a2c92c5eb56) [commit](https://github.com/DPDK/dpdk/commit/57fa1d4ddb504f2f98ad318c20fb269c49105738) [commit](https://github.com/DPDK/dpdk/commit/e872a0c9507a660789b2a7b1fc0f33d633db3b72) [commit](https://github.com/DPDK/dpdk/commit/a8fbe91974c95497eeec8b18d52f7ee25c4c1bec) [commit](https://github.com/DPDK/dpdk/commit/56232827a0d7b0923361353764dc93d28a7bf0e8)

- NTNIC flow supports SCTP, IPv6/ICMPv6, field modify, GTP, and raw encap/decap. [commit](https://github.com/DPDK/dpdk/commit/af7ae7aa3ca699393fb146d683873b90c69e95e6) [commit](https://github.com/DPDK/dpdk/commit/b199509a19a05938d38be417639f3c13ad93c87a) [commit](https://github.com/DPDK/dpdk/commit/339ca124e659516f35f92d376b24d60af3e3a1e2) [commit](https://github.com/DPDK/dpdk/commit/c6821abf58e8e53ca800cbe2cbb30c34536dd682)

- NTNIC adds CAT, SLC, PDB, QSL, KM, hash, TPE, FLM, RCP, and GMF flow hardware modules and queue/match database management. [commit](https://github.com/DPDK/dpdk/commit/833962ebb8935089336a0ede3efb1cd8fbb06eb3) [commit](https://github.com/DPDK/dpdk/commit/c4d1272b279d8c770b6d662db9c5e3d31c7bcf29) [commit](https://github.com/DPDK/dpdk/commit/ef6e148b813ca9caf4939b02d609aa9f3728dd6d) [commit](https://github.com/DPDK/dpdk/commit/98e40f83f49d1b37c33d59a196e20bd66c83cd81) [commit](https://github.com/DPDK/dpdk/commit/9bd46cf2599ed080b3a64a6b9295b12f61eb553d) [commit](https://github.com/DPDK/dpdk/commit/7fa0bf29e667c12dc32a8cfd6330a639adcf1358) [commit](https://github.com/DPDK/dpdk/commit/0b98e4c1509c446fac29b53726198e66babded87) [commit](https://github.com/DPDK/dpdk/commit/deda5e0f1c2f1718096319637a3042be7471eb7f) [commit](https://github.com/DPDK/dpdk/commit/866d8d06ad5dc4bcd49a08fc5c61ce4289505c79) [commit](https://github.com/DPDK/dpdk/commit/96c8249be53e94d21e5078cb2f21c3f31bbcd71e) [commit](https://github.com/DPDK/dpdk/commit/032d2b7603c864ed27935ba2916b052b42c8dadc) [commit](https://github.com/DPDK/dpdk/commit/30b2f87ac650e33b9ca34d2f568696016d3cf393)

- NTNIC supports RSS, statistics polling, FLM statistics interface, xstats, and flow statistics. [commit](https://github.com/DPDK/dpdk/commit/8eed292b277518a6d969e62b05557331dbec94da) [commit](https://github.com/DPDK/dpdk/commit/effa04693274e59d82b24907c5ee4d1f8eef3cd7) [commit](https://github.com/DPDK/dpdk/commit/a1ba8c473f5c4b9b3bfb487cc3e18c37c19c8777) [commit](https://github.com/DPDK/dpdk/commit/971245aa17ca9430b8462f38ad451a27ff909b6c) [commit](https://github.com/DPDK/dpdk/commit/cf6007eac4989cdfc442547f0dd700cc3c76041b) [commit](https://github.com/DPDK/dpdk/commit/e7e49ce6c760888e62e27084a45446a70305cbfa)

- NTNIC flow adds high-level aging, aging events, rule configuration, and termination handling threads. [commit](https://github.com/DPDK/dpdk/commit/41e430dec4b8369714b196d21b3682264beb2b8a) [commit](https://github.com/DPDK/dpdk/commit/57a7d2bcff72fdb57192d7cf765f89c059d74840) [commit](https://github.com/DPDK/dpdk/commit/e7e01fd15ddee1eb92d68a3aabe800850a8c757a) [commit](https://github.com/DPDK/dpdk/commit/c0d44442b8315eabda40c1461a85856576b9a728) [commit](https://github.com/DPDK/dpdk/commit/4f0f5ab0e4eb5ce654ca315a8faf646bb14c8ef7)

- NTNIC flow supports meter configuration. [commit](https://github.com/DPDK/dpdk/commit/4033e0539435c49c10cd17a4837af91fb7e62c57) [commit](https://github.com/DPDK/dpdk/commit/c35c06fb4ac1aee609fbca05116655628a844172)

- NTNIC supports updating actions of created flows, including inline profile actions. [commit](https://github.com/DPDK/dpdk/commit/54204ead942133b853c1a882345a61914ec619ca) [commit](https://github.com/DPDK/dpdk/commit/713bf087cedaf5b77da6eaada9335297675345d0) [commit](https://github.com/DPDK/dpdk/commit/dc52e60cfae9a93cc748cf350435d31ad1191c47)

- NTNIC flow adds asynchronous create/destroy operations and asynchronous flow templates. [commit](https://github.com/DPDK/dpdk/commit/87b3bb06d918af82092b4aadecb9d19ac354606d) [commit](https://github.com/DPDK/dpdk/commit/8195eb04332ffb2285babe459e997c4087f77100) [commit](https://github.com/DPDK/dpdk/commit/1042162db4393a19a2eb69722f4e8a7477bf80fd) [commit](https://github.com/DPDK/dpdk/commit/96d92ae46407bd381ac4d97d922e588763227897)

- NTNIC Ethernet supports MTU configuration. [commit](https://github.com/DPDK/dpdk/commit/6019656d6f6848c83591f24867538311545776eb)

- testpmd hairpin configuration adds a map parameter. [commit](https://github.com/DPDK/dpdk/commit/5334c3feb137ca4eeb4c0f150aae602016b6a5ea)

- Added ZXDH NIC driver, supporting PCI initialization, message channel, hardware lock, interrupts, device information query, configuration, and shutdown operations. [commit](https://github.com/DPDK/dpdk/commit/29e89288ff14f153c981bd6658ef80939bc16a05) [commit](https://github.com/DPDK/dpdk/commit/102ac20e036c53e86ad0b4a3cf1fe5b0ba2f1b3e) [commit](https://github.com/DPDK/dpdk/commit/9d80d5925f35587053373380d74b2a2f4a54c669) [commit](https://github.com/DPDK/dpdk/commit/d2fc5332aa78c4865fd1a4be62531dbdfe613453) [commit](https://github.com/DPDK/dpdk/commit/6310e3976bbaa19e03c2918392294bb94af051cd) [commit](https://github.com/DPDK/dpdk/commit/3630ac8bd81f09c4cd1d12fe1c5bf84c67141c48) [commit](https://github.com/DPDK/dpdk/commit/fea1ddb0c1bfecd131c43f71b1dddec32845209c) [commit](https://github.com/DPDK/dpdk/commit/70d49e4b97702155b4b4f52623f7a154efddf2c8) [commit](https://github.com/DPDK/dpdk/commit/27ed58d320be21f3a0a725194a0701b5b5d1c176)

- TXGBE and NGBE expose Tx descriptor error statistics. [commit](https://github.com/DPDK/dpdk/commit/e028ec1b84c64891932d1b79c46d1ed41be1f77d) [commit](https://github.com/DPDK/dpdk/commit/3eba2f2888a31dc275d37203c9d03e23604822ea)

- NFP adds EEPROM and LED operations; VMXNET3 v6 supports larger MTU; HNS3 supports flow priority, and the bonding API becomes a stable interface. [commit](https://github.com/DPDK/dpdk/commit/7f693813cf40f52a428507e01c7dd30648d59ca1) [commit](https://github.com/DPDK/dpdk/commit/8bd6f5403743ccea850514e29d38fb239312f61d) [commit](https://github.com/DPDK/dpdk/commit/a4b83a747d7d21c6d61b9ae69d39db5e1c700dcd) [commit](https://github.com/DPDK/dpdk/commit/ac72aae60f71b8716f65d1e2daf531a5ca38c998) [commit](https://github.com/DPDK/dpdk/commit/19da63ccfc7e83f06e1bb14d830d4e0de99b13cf)

- Network drivers support configuring only one queue per port. [commit](https://github.com/DPDK/dpdk/commit/084d0cdb572f87ec6a52d32f2f7890fd337ddfba)

- Allow enabling the IOVA field in mbuf. [commit](https://github.com/DPDK/dpdk/commit/592fdee47dbb9b8c1141a5d679eeab4f2861731f)

- Added CNXK RVU LF rawdev driver, supporting PF function query, interrupt callbacks, message handling, mailbox, BAR query, and self-tests. [commit](https://github.com/DPDK/dpdk/commit/318ee1b0468299e92411ea8616073c477743b34e) [commit](https://github.com/DPDK/dpdk/commit/59c15941bf34887cf75e6286524efa2a5691bfdc) [commit](https://github.com/DPDK/dpdk/commit/f4c67d7218b74b2dab86a6a5d3af12d47e6f55e0) [commit](https://github.com/DPDK/dpdk/commit/7396eaceaac52e6d66808daaf5ba414a47d2cfe6) [commit](https://github.com/DPDK/dpdk/commit/0924cc0b2489f72fcedd92fa4804821c730f7559) [commit](https://github.com/DPDK/dpdk/commit/384903ed3e6427e1a1a05d3df313a272011e2bf6) [commit](https://github.com/DPDK/dpdk/commit/fcac76a874e6419f125e5cf6bbd38bc4097351bd) [commit](https://github.com/DPDK/dpdk/commit/79c469df190056eb44ff5c91c6b02d49a1b98884) [commit](https://github.com/DPDK/dpdk/commit/aeb86158bf15140d49f9904ae40aa0ea9f13ec62)

- bbdev application supports capturing queue dumps and disabling interrupts. [commit](https://github.com/DPDK/dpdk/commit/067fae411cfe5c966f5122afad4b766fa3159cc1) [commit](https://github.com/DPDK/dpdk/commit/92351557d57637431807f46f5433886a10efcc91)

- DPAA/DPAA2 security crypto supports IPsec extended sequence numbers, DiffServ/ECN, UDP-encapsulated ESP, and IPv6 UDP encapsulation. [commit](https://github.com/DPDK/dpdk/commit/123098cdd4039858f5ed6941e38c2513ae3940fb) [commit](https://github.com/DPDK/dpdk/commit/c253236a38843dc4ee2126a397398e8c3a12e9ca) [commit](https://github.com/DPDK/dpdk/commit/32d8bc55476dcfabf3b3650f75fc19c9b09050ba) [commit](https://github.com/DPDK/dpdk/commit/3a3885276124a26cce507a6bf0a8f2f54de25ad0)

- ICE supports downloading scheduler topology, improves Tx scheduler hierarchy configuration, and allows applying TM topology after stopping the port, with layer count limits. [commit](https://github.com/DPDK/dpdk/commit/2a77f6496fe38dc2f66110d8c0bdf189ef6f0c1c) [commit](https://github.com/DPDK/dpdk/commit/715d449a965b104ce95af83211766309e92f33d7) [commit](https://github.com/DPDK/dpdk/commit/6412a8f741e81145479d0ea264e28db55d5a5eac) [commit](https://github.com/DPDK/dpdk/commit/4ace7701eb443d5dea965ea70fc192c900cbdff9)

- ICE enables 200G link rate; IXGBE and ICE add Rx/Tx descriptor limits. [commit](https://github.com/DPDK/dpdk/commit/36ffcdc254be9a6dbdc6cbcbfdb02d5603463e5d) [commit](https://github.com/DPDK/dpdk/commit/9fd2193e56a55c6509477f8d5751c18a388f3977) [commit](https://github.com/DPDK/dpdk/commit/a378cbf017403b4526125e8d9d1b102059874bd1)

- BNXT TruFlow enhances flow scale/query and dynamic TCAM, supporting Thor2, VXLAN-GPE, custom L2 tunnels, VF-to-VF offload, Wh+ mirroring, overlapping rules, action query/clear, and tunnel flow statistics. [commit](https://github.com/DPDK/dpdk/commit/8a2e845d735aa7379de77d51026b6b580ba05078) [commit](https://github.com/DPDK/dpdk/commit/19f3ac618ab2d309e24a3034fcfdacaa6f31c718) [commit](https://github.com/DPDK/dpdk/commit/580fcb3d718069a8058f4395dd64d19fed0c1f65) [commit](https://github.com/DPDK/dpdk/commit/80317ff6adfde7f618a100098e068ad5512e8e22) [commit](https://github.com/DPDK/dpdk/commit/74cab005e74976adbc800ab514291bb4c02d11f2) [commit](https://github.com/DPDK/dpdk/commit/5c275d61e19b08740c50f99258e6e4088bf1b663) [commit](https://github.com/DPDK/dpdk/commit/032d49ef310179bc0bd165dde4c018884bc5a3e2) [commit](https://github.com/DPDK/dpdk/commit/987f2ec9a0cfcb835cb62fe4c4abde6a584735a8) [commit](https://github.com/DPDK/dpdk/commit/dd0191d5e70d0e65a7f041a88af480fc673160e1) [commit](https://github.com/DPDK/dpdk/commit/af50070ef4f994196b09c96b52826e80395bbaea) [commit](https://github.com/DPDK/dpdk/commit/4a925aa7bf1b622b96da193eab5ebac9943490be) [commit](https://github.com/DPDK/dpdk/commit/32bdbf441469b4ade6f34037afae02b159d56b8c) [commit](https://github.com/DPDK/dpdk/commit/8499b456145375f3f93c04b1bf6a783ab29542c3) [commit](https://github.com/DPDK/dpdk/commit/be4732e8bc48dff2050500825a0d1d601ec68d4b) [commit](https://github.com/DPDK/dpdk/commit/49cdf04367be38dec1433ea21ef98d6acd151047)

- BNXT TruFlow extends recipe/table capabilities, supporting jump, priority, dynamic tunnel ports, metering, flow scale/RSS queries, generic template items, and Thor2 statistics caching. [commit](https://github.com/DPDK/dpdk/commit/61a7ca1f6f874286e6787b52c867f1bb25f4cd42) [commit](https://github.com/DPDK/dpdk/commit/f6e1201540603ced7cbaf8c883b03d859df62923) [commit](https://github.com/DPDK/dpdk/commit/83f916bddb17f2bed168a1093ff898a08cd3008b) [commit](https://github.com/DPDK/dpdk/commit/22b65613909ee32b69d1cceea6485180a6353999) [commit](https://github.com/DPDK/dpdk/commit/94dbd6cf36688f36872b6878879442889baac997) [commit](https://github.com/DPDK/dpdk/commit/80d760e129ae8bf928b3aa77800cd1bc5609d4b0) [commit](https://github.com/DPDK/dpdk/commit/288becfb77dfb2d37c80960e3f40f5477f237f6c) [commit](https://github.com/DPDK/dpdk/commit/35e03bafdce10b98fc68383ed323cece507f8bb7) [commit](https://github.com/DPDK/dpdk/commit/2aa70990392930426d92192c59d237dd16de31e5) [commit](https://github.com/DPDK/dpdk/commit/30d7102d9e71f57b32d4c65689726f0786a5890b) [commit](https://github.com/DPDK/dpdk/commit/ffbc3529089ac96517d4065a9b76c730c5586daa) [commit](https://github.com/DPDK/dpdk/commit/b413ab0ae7932d2ab27d783870e3d9a698193f08) [commit](https://github.com/DPDK/dpdk/commit/d4b36fc5f0dc59b256441c82e5a9395054026496) [commit](https://github.com/DPDK/dpdk/commit/0513f0af034df5dc543bb6eb6b17661839491a89)

- BNXT validates TSO/segments and invalid mbufs, frees and counts error Tx mbufs, responds to RSS configuration changes, and supports buffer-split Rx offload. [commit](https://github.com/DPDK/dpdk/commit/9151adf2b9eb901faf8f090ad4e612f5f20e36f5) [commit](https://github.com/DPDK/dpdk/commit/a4fd911f47d71757f10d6a3abacf49388cfdd656) [commit](https://github.com/DPDK/dpdk/commit/6f896ab33991de71af234a9653d1b862f763a94a) [commit](https://github.com/DPDK/dpdk/commit/6cc5dfa69a0335849fc0903d3ada943acb33c7ce) [commit](https://github.com/DPDK/dpdk/commit/643e7ee39879083ec8a9b86c2b60ca9f50182ed7) [commit](https://github.com/DPDK/dpdk/commit/b5dafa316ebc9df7da08ae8e98a3776b80ee67c4)

- Disable BNXT VLAN filter when TruFlow is enabled. [commit](https://github.com/DPDK/dpdk/commit/2c033311ec730dfbe519e059c0c53373e5133e8a)

- Update BNXT HWRM API and support selecting Rx profiles. [commit](https://github.com/DPDK/dpdk/commit/57e571c19fe7d9dc02eec6c1ee6379fd393f21fb) [commit](https://github.com/DPDK/dpdk/commit/7a535f301db655582fe44c26b908a40c9dc4983f)

- dma-perf supports per-device configuration; l3fwd can configure Rx burst size and mbuf cache size. [commit](https://github.com/DPDK/dpdk/commit/533d7e7f66f39de658ba167aad40837d916c52b4) [commit](https://github.com/DPDK/dpdk/commit/d5c4897ecfb2540dc4990d9b367ddbe5013d0e66) [commit](https://github.com/DPDK/dpdk/commit/d9f26e52a55c8a500439d5f0539dfbf5a6b41c3c)

- devbind recognizes all values of VFIO non-IOMMU sysfs. [commit](https://github.com/DPDK/dpdk/commit/c77887ad87931526768ae501596fcba15c21db82)

- FreeBSD kernel includes mapped buffers in core dumps. [commit](https://github.com/DPDK/dpdk/commit/cbe57f351b4e6541eb7b50a5c0d6f7e77b45c9db)

- Added GDTC rawdev driver, supporting queue configuration, basic device operations, and enqueue/dequeue. [commit](https://github.com/DPDK/dpdk/commit/30495f54583d93d50df02ec5e15cbaad6f6dcc6a) [commit](https://github.com/DPDK/dpdk/commit/d373c66ef139ad4fa1847c4ea11f37a50b497fb7) [commit](https://github.com/DPDK/dpdk/commit/648001aa00a15e48bb7f6a3acdf6fc9b48895dbb) [commit](https://github.com/DPDK/dpdk/commit/a73d74c2e30e7111b71b863aadf0c351a0f7ec8c) [commit](https://github.com/DPDK/dpdk/commit/81c6bacb0cdc43bc90d72e66968777653fbc4e31)

- MLX5 supports using vport action in Rx flows; testpmd displays L4 ports and reuses RSS configuration when configuring DCB. [commit](https://github.com/DPDK/dpdk/commit/7911783578f5bc6458c2af0670efeb617980ad9c) [commit](https://github.com/DPDK/dpdk/commit/e2bce04b48ab7e9fb184322a4ffa5a58705cae45) [commit](https://github.com/DPDK/dpdk/commit/34847a73034566ed1dab8bbc6882a12492b7f7fd)

- cpu_layout and devbind can display NUMA node information for devices/CPUs. [commit](https://github.com/DPDK/dpdk/commit/2b091dea3d37d076b6f11e6e676924be77122770) [commit](https://github.com/DPDK/dpdk/commit/a7d69cef8f20a9aeab4657c20ca3e424823163cd)

### Bug Fixes

- EAL validates alarm expiration parameters and fixes alarm cancellation handling. [commit](https://github.com/DPDK/dpdk/commit/7f34ecb6fef6cd6668d5449aabb26f1d3bce0452) [commit](https://github.com/DPDK/dpdk/commit/a4835c22ccfb5c5ba0aa5b32ebbafc0df12bf75a)

- Fixed write-combining store implementation on x86 32-bit platforms. [commit](https://github.com/DPDK/dpdk/commit/41b09d64e35b877e8f29c4e5a8cf944e303695dd)

- Fixed a crash in the eventdev generic pipeline example when processing queues. [commit](https://github.com/DPDK/dpdk/commit/f6f2307931c90d924405ea44b0b4be9d3d01bd17)

- Fixed a memory leak in the DPAA2 security crypto driver. [commit](https://github.com/DPDK/dpdk/commit/9c0abd27c3fe7a8b842d6fc254ac1241f4ba8b65)

- Fixed PDCP SNOW/ZUC watchdog descriptor handling. [commit](https://github.com/DPDK/dpdk/commit/2369bc1343fa5aac2890b2a3e12d65a2f1a2fd31)

- Adjusted alignment for CNXK crypto SM cipher pass-through data. [commit](https://github.com/DPDK/dpdk/commit/f593ed5b0ae9da85936bb4871130c56b92a35b26)

- CNXK crypto hardware flush path no longer triggers abort when it cannot complete. [commit](https://github.com/DPDK/dpdk/commit/e78159500d56015064c11f04c43ed2e25c02b5c1)

- Fixed callback lookup during device unregistration. [commit](https://github.com/DPDK/dpdk/commit/66fd2cc2e47c69ee57f0fe32558e55b085c2e32d)

- Fixed session size calculation in crypto scheduler. [commit](https://github.com/DPDK/dpdk/commit/b00bf84f0d3eb4c6a2944c918f697dc17cb3fce5)

- Fixed mbuf ownership and cryptodev dequeue count handling in the IPsec security gateway example. [commit](https://github.com/DPDK/dpdk/commit/991b0859151a461fffd114fed36905e9106e6361) [commit](https://github.com/DPDK/dpdk/commit/88948ff31f57618a74c8985c59e332676995b438)

- Fixed erroneous free in BPF conversion failure cleanup, and use-after-free in EAL memzone trace path. [commit](https://github.com/DPDK/dpdk/commit/a3923d6bd5c0b9838d8f4678233093ffad036193) [commit](https://github.com/DPDK/dpdk/commit/a306620e357af9d1e2b99a93fabc40b382c3fa88)

- Fixed use-after-free or allocator mismatch issues during initialization of LA12xx, QAT, IDPF, BCMFS, IDXD, and CNXK event drivers. [commit](https://github.com/DPDK/dpdk/commit/6ffb34498913f84713e98d6a2a21d2a86028a604) [commit](https://github.com/DPDK/dpdk/commit/1af60a8ce25a4a1a2ae1da6c00f432ce89a4c2eb) [commit](https://github.com/DPDK/dpdk/commit/4baf54ed9dc87b89ea2150578c51120bc0157bb0) [commit](https://github.com/DPDK/dpdk/commit/b1703af8e77d9e872e2ead92ab2dbcf290686f78) [commit](https://github.com/DPDK/dpdk/commit/91b026fb46d987e68c1152b0bb5f0bc8f1f274db) [commit](https://github.com/DPDK/dpdk/commit/db92f4e2ce491bb96605621cdd6f6251ea3bde85)

- Fixed resource lifetime errors in CNXK mempool, CPFL JSON parser, e1000 filter, NFP flow teardown, IFPGA interrupt, vhost example, and NFB paths. [commit](https://github.com/DPDK/dpdk/commit/c024de17933128f37b1dfe38a0fae9975be1b104) [commit](https://github.com/DPDK/dpdk/commit/1c20cf5be5c8b3e09673a44da2ce532ec0f35236) [commit](https://github.com/DPDK/dpdk/commit/58196dc411576925a1d66b0da1d11b06072a7ac2) [commit](https://github.com/DPDK/dpdk/commit/fae5c633522efd30b6cb2c7a1bdfeb7e19e2f369) [commit](https://github.com/DPDK/dpdk/commit/11986223b54d981300e9de2d365c494eb274645c) [commit](https://github.com/DPDK/dpdk/commit/d891a597895bb65db42404440660f82092780750) [commit](https://github.com/DPDK/dpdk/commit/ae67f7d0256687fdfb24d27ee94b20d88c65108e) [commit](https://github.com/DPDK/dpdk/commit/76da9834ebb6e43e005bd5895ff4568d0e7be78f)

- Added runtime bounds checking for AVX-512 FIB lookup. [commit](https://github.com/DPDK/dpdk/commit/45ddc5660f9830f3b7b39ddaf57af02e80d589a4)

- Fixed pcapng handling of chained mbufs, and dumpcap handling of jumbo frames. [commit](https://github.com/DPDK/dpdk/commit/6db358536fee7891b5cb670df94ec87543ddd0fb) [commit](https://github.com/DPDK/dpdk/commit/5c0f970c0d0e2a963a7a970a71cad4f4244414a5)

- Fixed CNXK ML handling of TVM model inputs/outputs, and improved CN10K error handling. [commit](https://github.com/DPDK/dpdk/commit/c4636d36bc2cc3a370200245da69006d6f5d9852) [commit](https://github.com/DPDK/dpdk/commit/63b82e242251f8684d46390b9e8bb9dcc5d34147)

- Fixed receive timestamp and offload handling in CNXK Ethernet and eventdev paths. [commit](https://github.com/DPDK/dpdk/commit/0efd93a2740d1ab13fc55656ce9e55f79e09c4f3) [commit](https://github.com/DPDK/dpdk/commit/f12dab814f0898c661d32f6cdaaae6a11bbacb6e) [commit](https://github.com/DPDK/dpdk/commit/697883bcb0a84f06b52064ecbf60c619edbf9083)

- Fixed mbuf rearm metadata for CNXK receive-inject packets. [commit](https://github.com/DPDK/dpdk/commit/0cce86f9966909bd68ade7cfa42ffafb90470ae2)

- Fixed issue with changing MAC address when VF is enabled on CNXK devices. [commit](https://github.com/DPDK/dpdk/commit/2d4505dc6d4b541710f1c178ee0b309fab4d2ee8)

- Fixed CNXK inline context write and outbound SA hardware word size handling. [commit](https://github.com/DPDK/dpdk/commit/6c3de40af8362d2d7eede3b4fd12075fce964f4d) [commit](https://github.com/DPDK/dpdk/commit/9587a324f28e84937c9efef534da542c30ff122b)

- Fixed out-of-place packet handling in CNXK Ethernet and event modes. [commit](https://github.com/DPDK/dpdk/commit/d524a5526efa6b4cc01d13d8d50785c08d9b6891) [commit](https://github.com/DPDK/dpdk/commit/01a990fe40e827c5f3497f785ce7fd68bff8ef5c)

- Handle device removal during Octeon EP probe, and fix CNXK interrupt reconfiguration. [commit](https://github.com/DPDK/dpdk/commit/304ba46be396d2ec5ddf1d6b02793015785cd823) [commit](https://github.com/DPDK/dpdk/commit/758b58f06a43564f435e3ecc1a8af994564a6b6b)

- Initialize queue count for baseband devices. [commit](https://github.com/DPDK/dpdk/commit/0f4e9909bc517d845e47da803f8b534691bbe5a3)

- Fixed ACC access to freed memory and soft-output bypass rate-matching handling. [commit](https://github.com/DPDK/dpdk/commit/a090b8ffe73ed21d54e17e5d5711d2e817d7229e) [commit](https://github.com/DPDK/dpdk/commit/2fd167b61bc6c6f40a6c04085caa56be40451e2a)

- Reset ring data-valid flag when ACC queue is reused. [commit](https://github.com/DPDK/dpdk/commit/63dcaf20304d24305bf0113f370bea2721307c1f)

- Fix vhost log-base mapping offset and vDPA relay used-ring flags propagation. [commit](https://github.com/DPDK/dpdk/commit/bdd96d8ac76ca412165b2d1bbd3701e978246d8e) [commit](https://github.com/DPDK/dpdk/commit/b3f923fe1710e448c073f03aad2c087ffb6c7a5c)

- Fix NFP vDPA hardware initialization and reconfiguration. [commit](https://github.com/DPDK/dpdk/commit/fc470d5e88f848957b8f6d2089210254525e9e13) [commit](https://github.com/DPDK/dpdk/commit/d149827203a61da4c8c9e4a13e07bb0260438124)

- Reset used-index counter on virtio-user restart. [commit](https://github.com/DPDK/dpdk/commit/ff11fc60c5d8d9ae5a0f0114db4c3bc834090548)

- Fix AVX-512 FIB lookup and IPv4 address byte order handling. [commit](https://github.com/DPDK/dpdk/commit/66ed1786ad067198814e9b2ab54f0cad68a58f1e) [commit](https://github.com/DPDK/dpdk/commit/e194f3cd5685d5b16c8561a715395a5f579c1bf3)

- Fix VFIO hotplug handling in multiprocess EAL. [commit](https://github.com/DPDK/dpdk/commit/6e18a2d452b2712930338f482960235687007fd0)

- Fix ethdev telemetry race, and port status and flow parsing issues in e1000, CPFL, and iavf. [commit](https://github.com/DPDK/dpdk/commit/6f96937dada54d5cfc8def0955b0807759b45ac4) [commit](https://github.com/DPDK/dpdk/commit/84506cfe07326fd6ddb158f3fa57bd678751561a) [commit](https://github.com/DPDK/dpdk/commit/86126195768418da56031305cdf3636ceb6650c8) [commit](https://github.com/DPDK/dpdk/commit/57ed9ca61f44ffc3801f55c749347bd717834008) [commit](https://github.com/DPDK/dpdk/commit/8125fea74b860a71605dfe94dc03ef73c912813e)

- Update ICE PTP initialization, and fix 200G link, TLV traversal, and Tx scheduler command handling. [commit](https://github.com/DPDK/dpdk/commit/3bb9d730d300b33c490289be4bcc5ed388c5d109) [commit](https://github.com/DPDK/dpdk/commit/b144d0c51782bf2e12e92fc485eba56fd07215a7) [commit](https://github.com/DPDK/dpdk/commit/e3992ab377d2879d6c5bfb220865638404b85dba) [commit](https://github.com/DPDK/dpdk/commit/dcb760bf0f951b404bce33a1dd14906154b58c75) [commit](https://github.com/DPDK/dpdk/commit/58ed532abc5681c39457282fddd5c4de31a8bc03)

- Add hardware and mailbox support for Intel E610, and fix media detection, auto-negotiation, 5G rate, temperature operations, mailbox acknowledgment, and EEPROM writes. [commit](https://github.com/DPDK/dpdk/commit/0d56299c3b6f13367a381838b358332a4481b275) [commit](https://github.com/DPDK/dpdk/commit/93a3916617cc478bc19db3a4e84c54fb2c19775f) [commit](https://github.com/DPDK/dpdk/commit/1be9d85b13f513f09d1949524255e8fbfa41020a) [commit](https://github.com/DPDK/dpdk/commit/659e36767e77b31088dc1f543ecba94562ecf08f) [commit](https://github.com/DPDK/dpdk/commit/eb3684b191928ebb5d263e3f8ab1e309bfec099e) [commit](https://github.com/DPDK/dpdk/commit/6c4abcb0f0b1d587c62dc4d0462665e4e6469b09) [commit](https://github.com/DPDK/dpdk/commit/b616e645ed1d1b2fd24b0012826c1aa4a6073da4) [commit](https://github.com/DPDK/dpdk/commit/2a18945801bf6b523af0596454257581f3c7a992) [commit](https://github.com/DPDK/dpdk/commit/d4a87e512efa6b2e031435e687a7bf2cdd489bba) [commit](https://github.com/DPDK/dpdk/commit/1f119e4e3c36f954a353028d2ce6879b8adc8289) [commit](https://github.com/DPDK/dpdk/commit/c83c62fbf75a4ada591a5c7146d10fe1831f74a6)

- Fix i40e initialization flags, device identification, X722 MAC/PHY handling, and DDP loading with reserved track ID. [commit](https://github.com/DPDK/dpdk/commit/deb7c447d088903d06a76e2c719a8207c94a576e) [commit](https://github.com/DPDK/dpdk/commit/597e19e7eae17beb820795c3a8a97c547870ba26) [commit](https://github.com/DPDK/dpdk/commit/b0bad8e99815d9a95614ff05cbcbd5057082b43c) [commit](https://github.com/DPDK/dpdk/commit/bf0183e9ab98c946e0c7e178149e4b685465b9b1) [commit](https://github.com/DPDK/dpdk/commit/f646061cd9328f1265d8b9996c9b734ab2ce3707)

- Fix i40e register layout, return value checks, loop boundaries, and semaphore timeout width handling. [commit](https://github.com/DPDK/dpdk/commit/221a3d87a690e6212f2e122fff95aa271fd22cc8) [commit](https://github.com/DPDK/dpdk/commit/7fb34b9141aab299c2b84656ec5b12bf41f1c21d) [commit](https://github.com/DPDK/dpdk/commit/3e61fe48412f46daa66f7ccc8f03b1e7620d0b64) [commit](https://github.com/DPDK/dpdk/commit/c61390d94d46b05b7cd97d34561cb0b360d4e89c)

- Fix iavf VF reset timing, ICE PHC initialization, and correct AVX-512 pointer copying in multiple drivers on 32-bit platforms. [commit](https://github.com/DPDK/dpdk/commit/b34fe66ea893c74f09322dc1109e80e81faa7d4f) [commit](https://github.com/DPDK/dpdk/commit/faa310a75f66953dda22887345dc196f8aef28de) [commit](https://github.com/DPDK/dpdk/commit/2d040df2437a025ef6d2ecf72de96d5c9fe97439) [commit](https://github.com/DPDK/dpdk/commit/da97aeafca4cdd40892ffb7e628bb15dcf9c0f25) [commit](https://github.com/DPDK/dpdk/commit/77608b24bdd840d323ebd9cb6ffffaf5c760983e) [commit](https://github.com/DPDK/dpdk/commit/d16364e3bdbfd9e07a487bf776a829c565337e3c)

- Fix FIB rule reclamation error codes, GVE queue lifecycle and chained mbuf Tx, and TAP null pointer memcpy. [commit](https://github.com/DPDK/dpdk/commit/cc8764c6c9af150131f714bbe8d39de861d5e377) [commit](https://github.com/DPDK/dpdk/commit/7174c8891dcfb2a148e03c5fe2f200742b2dadbe) [commit](https://github.com/DPDK/dpdk/commit/21b1d725e5a6cd38fe28d83c1f6cf00d80643b31) [commit](https://github.com/DPDK/dpdk/commit/3975d85fb8606308ccdb6439b35f70e8733a78e8)

- Fix ethdev descriptor count overflow, DPAA PFDR leak, and VSP/FMan state handling in DPAA bus. [commit](https://github.com/DPDK/dpdk/commit/30efe60d3a37896567b660229ef6a04c5526f6db) [commit](https://github.com/DPDK/dpdk/commit/b292acc3c4a8fd5104cfdfa5c6d3d0df95b6543b) [commit](https://github.com/DPDK/dpdk/commit/25434831ca958583fb79e1e8b06e83274c68fc93) [commit](https://github.com/DPDK/dpdk/commit/a87a1d0f4e7667fa3d6b818f30aa5c062e567597)

- Improve DPAA port cleanup, A010022 errata handling, and mbuf reallocation. [commit](https://github.com/DPDK/dpdk/commit/e498f3b51f3882c43eccb3d5b59b1d045b51c39a) [commit](https://github.com/DPDK/dpdk/commit/a978a7f6b7cdc48b4e9486fa983ac320f005b945) [commit](https://github.com/DPDK/dpdk/commit/7594cafa92189fd5bad87a5caa6b7a92bbab0979)

- Fix GVE DQ Rx memory leak and continuously attempt buffer refill during receive queue refill. [commit](https://github.com/DPDK/dpdk/commit/265daac8a53aaaad89f562c201bc6c269d7817fc) [commit](https://github.com/DPDK/dpdk/commit/31d2149719b716dfc8a30f2fc4fe4bd2e02f7a50)

- Fix potential memory corruption in GVE Rx refill and memif zero-copy Rx buffer overflow. [commit](https://github.com/DPDK/dpdk/commit/52c9b4069b216495d6e709bb500b6a52b8b2ca82) [commit](https://github.com/DPDK/dpdk/commit/b92b18b76858ed58ebe9c5dea9dedf9a99e7e0e2)

- Add I/O memory barrier before reading GVE descriptors. [commit](https://github.com/DPDK/dpdk/commit/f8fee84eb48cdf13a7a29f5851a2e2a41045813a)

- Fix redundant release call in NTNIC port release path. [commit](https://github.com/DPDK/dpdk/commit/7fa6075dee49bab1441d64f75cecf9647f66100b)

- Adjust TAP multiprocess file descriptor limit check and increase maximum allowed queue count. [commit](https://github.com/DPDK/dpdk/commit/288649a11a8a332727f2a988c676ff7dfd1bc4c5) [commit](https://github.com/DPDK/dpdk/commit/039aded84451df5a2b90035474ed309569c236e2) [commit](https://github.com/DPDK/dpdk/commit/6a2e47a3e26acb5ec206918c7f6454ee4aefa138)

- Ethdev Tx done cleanup validates queue ID; HNS3 validates reset type based on firmware return value. [commit](https://github.com/DPDK/dpdk/commit/707f50cef003a89f8fc5170c2ca5aea808cf4297) [commit](https://github.com/DPDK/dpdk/commit/3db846003734d38d59950ebe024ad6d61afe08f0)

- Use bounded `strlcpy` for NFP string copying. [commit](https://github.com/DPDK/dpdk/commit/cda9123ec16e08f2aa6476343733252512a3bf5e)

- Fix NFP link-change return value, port up/down checks, pause frame and FEC configuration result handling. [commit](https://github.com/DPDK/dpdk/commit/0ca4f216b89162ce8142d665a98924bdf4a23a6e) [commit](https://github.com/DPDK/dpdk/commit/1580387e07cf0facf695db2b8bc23f1238810c59) [commit](https://github.com/DPDK/dpdk/commit/4bb6de512fbc361e16d5a7a38b704735c831540d) [commit](https://github.com/DPDK/dpdk/commit/47fc5e4ee99bd8efa587ac6c6e7966318de4da1c)

- Fix memory leak during NFP VF initialization. [commit](https://github.com/DPDK/dpdk/commit/9fa4d03f746d84d8ecbb3ffb2b19f110cf79baae)

- Update ICE E822 scheduler and VLAN reset handling, expand scheduler node limit, and improve VSI topology initialization and upload. [commit](https://github.com/DPDK/dpdk/commit/f71ee587f371beecee55348d2a1314f9e8d3ce1c) [commit](https://github.com/DPDK/dpdk/commit/9378aa47f45fa5cd5be219c8eb770f096e8a4c27) [commit](https://github.com/DPDK/dpdk/commit/8e191a67df2d217c2cbd96325b38bf2f5f028f03) [commit](https://github.com/DPDK/dpdk/commit/aff06930682ca3f243d91bba3104c4af8169c38a) [commit](https://github.com/DPDK/dpdk/commit/d0c63c7f0fcaedae4537910590020fe59210dbb1) [commit](https://github.com/DPDK/dpdk/commit/4376d9fd19f332dbabf11548fe59cda296d53a75) [commit](https://github.com/DPDK/dpdk/commit/5ac957beedfbb12749aa4cbdd76f386bd0687f94) [commit](https://github.com/DPDK/dpdk/commit/55250a2d5b5041fb28e4d87ba20f43364c04cc72) [commit](https://github.com/DPDK/dpdk/commit/d4ee6403b58dab6935661f8b99736707fe7d108c)

- Preserve original MAC address in iavf when using i40e PF Linux driver. [commit](https://github.com/DPDK/dpdk/commit/3d42086def307be853d1e2e5b9d1e76725c3661f)

- Fix MLX5 Rx queue control list management, hardware flow queue full detection, matcher release order, mask translation, and ipool error code handling. [commit](https://github.com/DPDK/dpdk/commit/f957ac99643535fd218753f4f956fc9c5aadd23c) [commit](https://github.com/DPDK/dpdk/commit/b56ba2139f4dc04b97f69f0d0ece1f28725a100b) [commit](https://github.com/DPDK/dpdk/commit/045da18ec955f4ab5afe7697454965d40d9289a1) [commit](https://github.com/DPDK/dpdk/commit/02508320543df75a4dfabad83adfcd3353600c61) [commit](https://github.com/DPDK/dpdk/commit/e4a40879922e4685bbbbf3503d6b388e2ee11044)

- Fix hash thash LFSR initialization. [commit](https://github.com/DPDK/dpdk/commit/ebf7f1188ea83d6154746e90d535392113ecb1e8)

- Fix NFP flower PF link rate notification, IPv6 transport flag, AER state cleanup, and Rx buffer size configuration. [commit](https://github.com/DPDK/dpdk/commit/2254813795099aa6c05caed5e8c0dcc7a8f03b4e) [commit](https://github.com/DPDK/dpdk/commit/4f64ebdd41ce8bb60dba95589a5cc684fb9cb89c) [commit](https://github.com/DPDK/dpdk/commit/c4ced2d58a542980fdbbbf3095ad6571e3e6ba14) [commit](https://github.com/DPDK/dpdk/commit/b5fae3a560c39b1a9a09c40dbeec2086f12ac53a)

- Fix dmadev null pointer access, mbuf allocator strict-aliasing, GVE Rawhide build, VLAN header alignment, and power lcore mapping. [commit](https://github.com/DPDK/dpdk/commit/e5389d427ec43ab805d0a1caed89b63656fd7fde) [commit](https://github.com/DPDK/dpdk/commit/6011b12f52b60565d4dfcc3b382551ec1f53b3d4) [commit](https://github.com/DPDK/dpdk/commit/f0d9e787747dda0715654da9f0501f54fe105868) [commit](https://github.com/DPDK/dpdk/commit/e214d58eb87b8af488272f084220617ecabb510a) [commit](https://github.com/DPDK/dpdk/commit/5c9b07eeba55d527025f1f4945e2dbb366f21215)

- Fix NFP VXLAN inner-layer RSS, netvsc Tx queue usage, af_packet socket protocol selection, NFP return value checks, and ethdev C++ linking; restrict HNS3 tunnel flow to a single header. [commit](https://github.com/DPDK/dpdk/commit/5b81c1e2669081c0de8a7bd4b55f2123a7e48c33) [commit](https://github.com/DPDK/dpdk/commit/e90020535c03cf9e60448ba623cac3301f111dae) [commit](https://github.com/DPDK/dpdk/commit/5b81eac5fd6f8035a2d8fdd3863eb789f77de164) [commit](https://github.com/DPDK/dpdk/commit/8c1d15f1c44f2deeb62fadf32c8b4ea7390964d3) [commit](https://github.com/DPDK/dpdk/commit/20387ebce20ac5bc2e4e26bd008129a6c2cad9cc) [commit](https://github.com/DPDK/dpdk/commit/8887c207b9373a1875031c5346706f698322d66d)

- Fix ICE flow-director queue duplicate stop, scheduler queue overrun, FreeBSD ixgbe link status delay, Octeon EP initialization failure, and Mvneta out-of-bounds write. [commit](https://github.com/DPDK/dpdk/commit/7b230d43e8061bdaba02a41f601bb8e0b5dbff03) [commit](https://github.com/DPDK/dpdk/commit/5117ebfcc0d52bdf13eb5e04997293287fe69f1f) [commit](https://github.com/DPDK/dpdk/commit/f775386d92d68e534600fcff3fc4bcaa30d3e68c) [commit](https://github.com/DPDK/dpdk/commit/283c97cffd7f58ce13ce59feface5ee94aa2acc8) [commit](https://github.com/DPDK/dpdk/commit/c705c67d304b9450824a169b652520c2358c6aee)

- Fix CNXK flow aging resource double-free and eSwitch multi-segment packet handling. [commit](https://github.com/DPDK/dpdk/commit/d1066ea60bcb5cbd3cdcc06d21afc232d8c08407) [commit](https://github.com/DPDK/dpdk/commit/cfd5db0dcdb9005a3b82c628f0ebd8677ff85ec6)

- Fix VDUSE creation error handling, TOCTOU risk, and reconnect startup flow; adjust reconnection log validation and recovery timing after device creation. [commit](https://github.com/DPDK/dpdk/commit/47458d13d44af88f0bb3af0a327a7b06784f8480) [commit](https://github.com/DPDK/dpdk/commit/29ab97dd8316b6ecbb1753202b87ace1c854d445) [commit](https://github.com/DPDK/dpdk/commit/952e49451600bea61214249815f241167c7c456d) [commit](https://github.com/DPDK/dpdk/commit/69d2e2567b04833dbb1e92f572d6d97943faee9c) [commit](https://github.com/DPDK/dpdk/commit/a2a05e55396435db4fd06f91a829175fba885fa3)

- VRB decoder saturates input to 6 bits. [commit](https://github.com/DPDK/dpdk/commit/e71eb4f7bf3e2550015914661406ff4324c0c5f8)

- Fix event device stop test handling and CNXK getwork write data issue during reconfiguration. [commit](https://github.com/DPDK/dpdk/commit/b74f298f9bfaba19527153098546fa1011c100a1) [commit](https://github.com/DPDK/dpdk/commit/6dad0bb5c8621644beca86ff5f4910a943ba604d)

- Fix OpenSSL crypto PMD 3DES-CTR handling on big-endian platforms. [commit](https://github.com/DPDK/dpdk/commit/97afd07ca79c7270480a65febd7f616a4c0b07ca)

- Fix MLX5 trace script under multiple burst completions, PCI BAR real-time counter reading, and Tx timestamp source, and display incomplete trace records. [commit](https://github.com/DPDK/dpdk/commit/d67215274063cb853b6c64e218a8b6a8025adc19) [commit](https://github.com/DPDK/dpdk/commit/27918f0d53f482fa97f2a8dcd5792c23094abcec) [commit](https://github.com/DPDK/dpdk/commit/02932480ae82d7ed3c207f02cc40b508cdda6ded) [commit](https://github.com/DPDK/dpdk/commit/171360df9f89a17f8b4177f01f11fa4473c74099)

- dumpcap checks return value of interface addition failure. [commit](https://github.com/DPDK/dpdk/commit/c79900e31e3e5a16c7f5410d0800315a0491ccad)

- Fix MLX5 metering resource leak, GRE/root flow conversion, HWS error recovery and counter notification, and flow/meter/NAT64 validation and descriptor capability reporting. [commit](https://github.com/DPDK/dpdk/commit/4dd46d38820e0bf5e74f99b84f4b098d1b7220dd) [commit](https://github.com/DPDK/dpdk/commit/25ab2cbba31d937e685f0cf9ecce0c680cc4083e) [commit](https://github.com/DPDK/dpdk/commit/84c3090e517641027a7b64fe5bb6eccbcfa05a6d) [commit](https://github.com/DPDK/dpdk/commit/d46f3b525aafbb4c6c88d9c61b445eb0d93d2149) [commit](https://github.com/DPDK/dpdk/commit/7c66fa49ddcce1981c2fa3a0c024ec82b036639c) [commit](https://github.com/DPDK/dpdk/commit/ee76b173b2e93ab4a0c9b4153191965259dae972) [commit](https://github.com/DPDK/dpdk/commit/0c37d8f7ba2cac289896de024d9c58a65ba3ece9) [commit](https://github.com/DPDK/dpdk/commit/61a810617ec864aa30b36d7aaffc0bda4cc28f54) [commit](https://github.com/DPDK/dpdk/commit/d3e46998443e47e48bea30e116c6330bfdf5302c) [commit](https://github.com/DPDK/dpdk/commit/4c3d7961d9002bb715a8ee76bcf464d633316d4c) [commit](https://github.com/DPDK/dpdk/commit/db830c40bc8296fc013d9328255192fb589d858a) [commit](https://github.com/DPDK/dpdk/commit/e53e4c39d2514667a7065cb0dd2d8fe3dcd843e3)

- Fix graph node clone memory leak, IPv6 address utility out-of-bounds, and simple IPv4 checksum calculation. [commit](https://github.com/DPDK/dpdk/commit/5e65cd4a722ec7f277a70447db318953252bf6f9) [commit](https://github.com/DPDK/dpdk/commit/b805c834c776c67fb52d2b84c74258c5323a7872) [commit](https://github.com/DPDK/dpdk/commit/1d9c6bbeb6cd8d0e3b7d54c7732199524020ea23) [commit](https://github.com/DPDK/dpdk/commit/c14fba68edfa4aeba7c0dfb5dbc3b4f23affbb81)

- Align Windows getopt behavior with FreeBSD. [commit](https://github.com/DPDK/dpdk/commit/a06fb0fae6ab6a79fa3e8288dbb0c5166be843c2)

- Add hardware workarounds for DPAA DMA ERR050757 and QDMA stall ERR050265. [commit](https://github.com/DPDK/dpdk/commit/bdcb782a460108c894798ae6a1e04dd1df94c29e) [commit](https://github.com/DPDK/dpdk/commit/8c53b9b7954d6beb16d2497a28005a7d9c5bb1c8)

- Fix DPAA2 traffic manager memory corruption, validate IOVA before sending MC commands, and improve DPDMUX drop priority error handling. [commit](https://github.com/DPDK/dpdk/commit/d77cb0c44cf6b68dc71684bd302fd3138b36e5f1) [commit](https://github.com/DPDK/dpdk/commit/25d0ae6242453c3e482d752495d5a30f3ada11dd) [commit](https://github.com/DPDK/dpdk/commit/00e928e9704c3794062b46c1c30352281e4f9cb8)

- Fix l3fwd-power parameter parsing overflow and out-of-bounds reads in l3fwd normal/ACL modes. [commit](https://github.com/DPDK/dpdk/commit/0bc4795d5994459a3d261afd7f843eb0cabdecf5) [commit](https://github.com/DPDK/dpdk/commit/ebab0e8b2257aa049dd35dedc7efd230b0f45b88) [commit](https://github.com/DPDK/dpdk/commit/795b63416b96aac4358a0b01f59d83797b94e522)

- Fix FSLMC bus scan return value in non-essential scenarios. [commit](https://github.com/DPDK/dpdk/commit/b472c50aeee1ca4f3a86be0580d31474653dfd8f)

- ethdev and multiple examples/drivers check device information query results to avoid ignoring query failures; also require callers to handle ethdev query function return values. [commit](https://github.com/DPDK/dpdk/commit/a4fa02e06046d36c6a7340201571397d2f59a682) [commit](https://github.com/DPDK/dpdk/commit/fe02b98cd3925d455731f0201030c587a387eef0) [commit](https://github.com/DPDK/dpdk/commit/7d04227433ede0e3fdab1319cadafa46cc28266d) [commit](https://github.com/DPDK/dpdk/commit/a937954e3d1ccfcc88aad472b0e6ee67f3eb560c) [commit](https://github.com/DPDK/dpdk/commit/07e4dc04d99a99699d71a0a39dd2a7034049e663) [commit](https://github.com/DPDK/dpdk/commit/d0974e07f42e12626ee78cba0d285090de40d149) [commit](https://github.com/DPDK/dpdk/commit/6c5e32c71220a69ee079284814a26d8ad29dabe4) [commit](https://github.com/DPDK/dpdk/commit/69559d0df94779b2d76f991831390400e33237fe) [commit](https://github.com/DPDK/dpdk/commit/1ff8b9a6ef248dddebd07a8df7b47f4de9ffab62)

- Fix Tx VLAN offload for netvsc on 802.1Q packets, as well as HNS3 integer overflow and register pointer offset. [commit](https://github.com/DPDK/dpdk/commit/06c968f9ba8afeaf03b60871a453652a5828ff3f) [commit](https://github.com/DPDK/dpdk/commit/b1fefe40550836b58c4ec50dce14a6e6dbda8499) [commit](https://github.com/DPDK/dpdk/commit/013fdd2d7b319e6a35d966f375e33ee330d9ccb5)

- Fix crash after VMXNET3 configuration failure and out-of-bounds access in statistics. [commit](https://github.com/DPDK/dpdk/commit/439847c154ccf05e1a8bbb955c552921514d31e2) [commit](https://github.com/DPDK/dpdk/commit/d3a229dd493abcb29d5717c5ce37e0a0bc1777c4)

- Fix TXGBE/NGBE mailbox communication, interrupts, firmware load notification, and Rx/Tx configuration, and add Tx descriptor error interrupt and packet length validation. [commit](https://github.com/DPDK/dpdk/commit/e389504ed46d84c6a5a6a32b09d6750a182f8725) [commit](https://github.com/DPDK/dpdk/commit/5a4ce69701fc01f23a2769c8afff055d87eff864) [commit](https://github.com/DPDK/dpdk/commit/0a8f064bbc2cf4978857eae84e86c6b2c9e65feb) [commit](https://github.com/DPDK/dpdk/commit/0eabdfcd4af44fd8b32ccdeb3d01c256572a52d0) [commit](https://github.com/DPDK/dpdk/commit/7029832c24f051032798c1cfaeb137ab886db094) [commit](https://github.com/DPDK/dpdk/commit/8d75bf037aa29c865ce7ce1c891519ec5118f9df) [commit](https://github.com/DPDK/dpdk/commit/cb7be5b510ef0995fa171832f0e0994f667e2161) [commit](https://github.com/DPDK/dpdk/commit/b8d52e1084a17c7ef83624f3bbd11a090e7b2267) [commit](https://github.com/DPDK/dpdk/commit/68f04c0aa79316de333441e7efdadd2876412ffa)

- Remove unsupported outer UDP checksum capability from TXGBE, and restrict NGBE VLAN strip configuration. [commit](https://github.com/DPDK/dpdk/commit/25fe1c780d39ea3637ba8407f6e9a9800135becd) [commit](https://github.com/DPDK/dpdk/commit/baca8ec066dc6fdc42374e8eafd67eecfd6c9267)

- Fix NFP port index, HNS3 counter duplicate creation error code, and flow director entry usage. [commit](https://github.com/DPDK/dpdk/commit/fbbfcc19e3acb5cbd0026d71399f084f4d55aeeb) [commit](https://github.com/DPDK/dpdk/commit/d3a229dd493abcb29d5717c5ce37e0a0bc1777c4) [commit](https://github.com/DPDK/dpdk/commit/585f1f68f18c7acbc4f920053cbf4ba888e0c271) [commit](https://github.com/DPDK/dpdk/commit/b8e60c33168a2999604c17322dd0198a6746428f)

- Fix integer overflow risk in OcteonTX event driver. [commit](https://github.com/DPDK/dpdk/commit/3e86eee028c69b98144e2c62ec48091467e790be)

- Fix ACC ring memory allocation. [commit](https://github.com/DPDK/dpdk/commit/0c5709824b531e83b36ed91852cea98b1cb292e1)

- Fix OpenSSL string overflow risk, as well as QAT modexp/inv length and ECDSA session handling. [commit](https://github.com/DPDK/dpdk/commit/c5819b0d96d1a24c25aa4324913fd2566eb19ae9) [commit](https://github.com/DPDK/dpdk/commit/5b2fe7ef3c1b731f086d9454262a530a082b0441) [commit](https://github.com/DPDK/dpdk/commit/20e633b0ca15539b682539a665e8d3dc0dc2c899)

- Fix Rx buffer in IGC timestamp scenarios, ICE empty DDP path and invalid PHY timestamp, E610 queue interrupt, and CPFL forwarding to physical port. [commit](https://github.com/DPDK/dpdk/commit/4e08d335554ec6d975ded8a7badf81e0edb39234) [commit](https://github.com/DPDK/dpdk/commit/14d66da59b4a29f23f34315bf51616f5e90b16ad) [commit](https://github.com/DPDK/dpdk/commit/b55051d1c59d8670fd59423b5af529936cf5554d) [commit](https://github.com/DPDK/dpdk/commit/42e7a159f0d959f2c9e41b0b76ad281124125327) [commit](https://github.com/DPDK/dpdk/commit/b0e6aff62efa4bcc23f64b80b91709bef73e6d79)

- Fix CN9K event template macro. [commit](https://github.com/DPDK/dpdk/commit/49a841e1983acfaefdfe19957166d985ad921867)

- Fix BNXT TCAM multi-slice deletion, TCAM data corruption, Thor key size validation, and slice count after HA entry movement. [commit](https://github.com/DPDK/dpdk/commit/78dcdb821cb81f4abddfd4abc0192e238d4bfcec) [commit](https://github.com/DPDK/dpdk/commit/0bee506e9ec6bca60111b63e631c84080b14aec2) [commit](https://github.com/DPDK/dpdk/commit/912abed4250c792214886880fa0b93b7712fba21) [commit](https://github.com/DPDK/dpdk/commit/1190f2f8d5abf82c843ad071ad4c7d0aea202cce)

- Fix BNXT parent/child DB count, SFP EEPROM read, TCP/UDP checksum flags, Tx buffer descriptor action offset, and LRO capability reporting. [commit](https://github.com/DPDK/dpdk/commit/8782e4de3ef2e55bd4aed98dc18e26d2bfc83868) [commit](https://github.com/DPDK/dpdk/commit/7b8400464f14637ed2669dbf732c256bf2447de6) [commit](https://github.com/DPDK/dpdk/commit/4c0451197e5a88531c30398b58b7e5601be90080) [commit](https://github.com/DPDK/dpdk/commit/b019ddf9b1de65491b4c07c25bbab3dc70c15f79) [commit](https://github.com/DPDK/dpdk/commit/019c181687371f24196f437b648dc80f67519b72)

- Fix bnx2x condition checks and potential infinite loop at startup. [commit](https://github.com/DPDK/dpdk/commit/fb6b0e9a36326a4f13f496b00f7f92aaffe1d5f4) [commit](https://github.com/DPDK/dpdk/commit/a47272b052dd1c8c571a1c0b89b56aaa3ebf4351) [commit](https://github.com/DPDK/dpdk/commit/87e210eb086f49f32733c579003b9565e46535d7)

- Fix l2fwd-event spinlock handling and eventdev array out-of-bounds risk. [commit](https://github.com/DPDK/dpdk/commit/1f41deac447d7938198a2acdd1b7862161feef91) [commit](https://github.com/DPDK/dpdk/commit/952b24bd0475450e548d4aafae7d8cf48258402b)

- Fix MLX5 128-byte CQE error handling, vector Rx queue numbering, STC allocation, flow parameter lifetime, counter query, Rx queue management, alignment, RSS flow creation, and miniCQE calculation. [commit](https://github.com/DPDK/dpdk/commit/3cddeba0ca38b00c7dc646277484d08a4cb2d862) [commit](https://github.com/DPDK/dpdk/commit/3638f431b9ff39003e31c3a761d407e04b25576a) [commit](https://github.com/DPDK/dpdk/commit/691326d15da263d068de71c468c74c225c4f75c3) [commit](https://github.com/DPDK/dpdk/commit/d1357665a85b30066c8b69996ddf601332a198f8) [commit](https://github.com/DPDK/dpdk/commit/c0e29968294c92ca15fdb34ce63fbba01c4562a6) [commit](https://github.com/DPDK/dpdk/commit/3c9a82fa6edc06c1d4dc6c0ac53609002c4d9462) [commit](https://github.com/DPDK/dpdk/commit/90967539d0d1afcfd5237ed85efdc430359a0e6b) [commit](https://github.com/DPDK/dpdk/commit/9a66bb734e1311bcc2bf3b286f7ab6d28975c5c7) [commit](https://github.com/DPDK/dpdk/commit/1ea333d2de220d5bad600ed50b43f91f7703c123) [commit](https://github.com/DPDK/dpdk/commit/a7ae9ba1f8c888a7ed546a88a954426477cd24a4)

- app/graph switches to reentrant string parsing; FIPS example fixes RSA pre-hash handling and EdDSA signature length. [commit](https://github.com/DPDK/dpdk/commit/9236e5b31d909b45fa52c5e19adf02108a2052d1) [commit](https://github.com/DPDK/dpdk/commit/733c7861492d67eb5fba8ee50fb08d7db82a176d) [commit](https://github.com/DPDK/dpdk/commit/2cf2f84442e80ff382b05dfd0db62bd969422da4)

- Fix BNXT TruFlow VXLAN counter accumulation, VFR cleanup, and statistics lockup. [commit](https://github.com/DPDK/dpdk/commit/a089734a026a316994674e3f405ee4d56a114efc) [commit](https://github.com/DPDK/dpdk/commit/67ad40007cd6bb6ce9f0b3eefe2af611848d10dc)

- Add iavf Tx segment length and ICE null pointer checks, and validate i40e outer VLAN register read results. [commit](https://github.com/DPDK/dpdk/commit/4523e0753b243066357f98fd9739fde72605d0fb) [commit](https://github.com/DPDK/dpdk/commit/c11c52dd5d2a19c97616ac32a1d4911c48f157d4) [commit](https://github.com/DPDK/dpdk/commit/19a02bc972759a0fc1f40753ccfe0d8152d68d1e)

- Fix resource leak on procinfo exit and bucket selection error in member displacement. [commit](https://github.com/DPDK/dpdk/commit/8a171e52ed8b26f768ced79a22286914ebd30180) [commit](https://github.com/DPDK/dpdk/commit/33f5b0dcb11580be8091f3b589845e512008e2f0)

- Fix testpmd flow update and aged flow destroy command handling. [commit](https://github.com/DPDK/dpdk/commit/5b7d82e817afad123c8ff5f9f0e53ef36fadac3d) [commit](https://github.com/DPDK/dpdk/commit/098f949f8a70f7618f5390f9c1e9edfb9e5469c4)

- Fix BNXT mbuf offload flags, MLX5 shared Rx queue release, vhost async Rx deadlock, TXGBE interrupt, and NTNIC DSCP flow action; restore VDUSE uAPI consistent with kernel, and correct Toeplitz key handling. [commit](https://github.com/DPDK/dpdk/commit/3e9a43bad2ce1413be2456c7e53945444aac99f9) [commit](https://github.com/DPDK/dpdk/commit/f8f294c66b5ff6ee89590cce56a3d733513ff9a0) [commit](https://github.com/DPDK/dpdk/commit/22aa9a9c7099e1f4b297899c33b4fea1131d3ac7) [commit](https://github.com/DPDK/dpdk/commit/4025e36fa5b7e44df07d53f8e7ddfeab5f1512a2) [commit](https://github.com/DPDK/dpdk/commit/916aa13f4a198aebf5383f9680cb5cd527518f2c) [commit](https://github.com/DPDK/dpdk/commit/9141a191d40b9cc7c669588cc6dad4c8bafba373) [commit](https://github.com/DPDK/dpdk/commit/ef6ed529b220b74b5ca52bc7619f21522cd6a874)

- Fix E610 PTP/RSS/loopback handling, and initialize PTP clocks on multiple Intel NICs with system time; pcapng avoids unaligned data access. [commit](https://github.com/DPDK/dpdk/commit/d797d98e6313127e5735e069c3e7057b49205bb7) [commit](https://github.com/DPDK/dpdk/commit/a80016c8b8d1995db5853b980cc8a7af6b5ce863) [commit](https://github.com/DPDK/dpdk/commit/62fd579fcd15f13f2bed84a003d284d04ddbd9cf) [commit](https://github.com/DPDK/dpdk/commit/d2394b2790f36becf3fef5ff979a988855f1024f) [commit](https://github.com/DPDK/dpdk/commit/77e90b1da5d31a6731b33bf1661f32353df35a48) [commit](https://github.com/DPDK/dpdk/commit/41927fde0889abb24aecc3538aed06f3ae1ae09e) [commit](https://github.com/DPDK/dpdk/commit/0cbf27521b0d6e7cb79f41a5e699d82562b09c03)

- Fix redundant flow policy action check in testpmd and potential out-of-bounds access in flow commands. [commit](https://github.com/DPDK/dpdk/commit/4c2e7468426ae6be3f2a8f2d15e7d1222083eb9d) [commit](https://github.com/DPDK/dpdk/commit/f86085caab0c6c5dc630b9d6ad20d1c728e7703e)

- Restore devbind active marker, and fix NUMA node information display. [commit](https://github.com/DPDK/dpdk/commit/828fe9de4c186ca3715a068ea59f689dde853e7f) [commit](https://github.com/DPDK/dpdk/commit/b456bf50063deeecbf3eaedfbd0949a0e7cbe19f)

- Add missing VF PCI ID for ixgbe. [commit](https://github.com/DPDK/dpdk/commit/f678f3dea8fd2a5e7fe2d78b5889c141ac263f7a)

### Refactoring

- Remove zero-length arrays in event-related structures to improve C compiler compatibility. [commit](https://github.com/DPDK/dpdk/commit/29911b323e7a4200b95e2049df08779c0673fbfc)

- Adjust may_alias type conversion style in cxgbe driver. [commit](https://github.com/DPDK/dpdk/commit/3e49a10f2ede1d047bbdec9ee56e2227459278f7)

- Update RSA asymmetric transform configuration to explicitly represent ASN.1 encoding and padding parameters. [commit](https://github.com/DPDK/dpdk/commit/0e3b2fc18c6b9bae9c6d51779bcd2b057ba0e300) [commit](https://github.com/DPDK/dpdk/commit/8a97564b1c1e035daaa0cdda553edd46178889e2)

- Refactor kvargs handling into reusable API, and migrate SFC, TAP, and NFP calls. [commit](https://github.com/DPDK/dpdk/commit/de89988365a7ca4087dd451c675320c993910332) [commit](https://github.com/DPDK/dpdk/commit/f33e8c0e4a80c1456987f96c1ce448d65e7d6dfb) [commit](https://github.com/DPDK/dpdk/commit/4ed306131f85ef180589169b868f292d9149b0c7) [commit](https://github.com/DPDK/dpdk/commit/3977d07df186e6f4c79802db19451f51703a3d60)

- Reduce storage width of i40e time variables. [commit](https://github.com/DPDK/dpdk/commit/cb593a832630a81403a9fc3e3de0bd06742e4bbb)

- Adjust ENA LLQ policy user configuration structure. [commit](https://github.com/DPDK/dpdk/commit/d7918d19d25ecfbac7326a28e8ff30c60662e4d7)

- Ethdev traffic-management node, profile, and shaper APIs now accept read-only parameters. [commit](https://github.com/DPDK/dpdk/commit/5d49af626c829c465d36dd482ae17abc347f1929) [commit](https://github.com/DPDK/dpdk/commit/5d96356688da2f79a62a48025a017c77e90d6232) [commit](https://github.com/DPDK/dpdk/commit/3953323852dfe399c0e6bdf2d35f88005b8a2135)

- DPAA bus replaces a system call with file I/O. [commit](https://github.com/DPDK/dpdk/commit/126cc1b2b44a3d2967943e1ef995b9e20f9e5021)

- Refactor dmadev parameter validation, and split hash creation parameter checks. [commit](https://github.com/DPDK/dpdk/commit/2980a27ecfaf2ea3a990cfa38cc310221a1c9b97) [commit](https://github.com/DPDK/dpdk/commit/bf26e6f4019b7ab29e2ff8263effd3695d415ef4)

- Argparse adjusts flag definitions and fixes parameter flag storage space and hyphen handling in documentation. [commit](https://github.com/DPDK/dpdk/commit/bd0d68bdc36d4422176e72d49eccfe88f167e3d9) [commit](https://github.com/DPDK/dpdk/commit/f48e4eed4aebba5b61565fbf8515fd723b53cd0c) [commit](https://github.com/DPDK/dpdk/commit/51a639ca804234462df0a8c72523fa71181cea24)

- Add IPv6 address type and common address judgment utilities, and migrate IPv4/IPv6 addresses, packet headers, LPM/FIB/RIB, cmdline, graph, pipeline, IPsec, security, hash, GRO, and ethdev flow to unified structures. [commit](https://github.com/DPDK/dpdk/commit/4149b1fb5e0bd3f5339a62c0058125e6305b9122) [commit](https://github.com/DPDK/dpdk/commit/1a2b549bb482b580424ed40b3b33d0673fcd89b0) [commit](https://github.com/DPDK/dpdk/commit/ca786def84caa9c4f1f36f516477e9a5f58389b5) [commit](https://github.com/DPDK/dpdk/commit/89b5642d0d45c22c0ceab57efe3fab3b49ff4324) [commit](https://github.com/DPDK/dpdk/commit/e1a06e391ba74f9c4d46a6ecef6d8ee084f4229e) [commit](https://github.com/DPDK/dpdk/commit/6cb10a9bdb6d2d0253e4d022f230371d703d8ac2) [commit](https://github.com/DPDK/dpdk/commit/59b993151ff57e9e8b0fdb1d4b57913243b605fa) [commit](https://github.com/DPDK/dpdk/commit/52e04a6323319ff1a7b4e1d7ed1df2b45d11a0a4) [commit](https://github.com/DPDK/dpdk/commit/2cfebc3f1046e4166e13b4f906e3ddc1c26c7eeb) [commit](https://github.com/DPDK/dpdk/commit/5ac1abdd37aa43692603cd8670111c354014766f) [commit](https://github.com/DPDK/dpdk/commit/9ac91e2f7339e66658ef55b756a06b328e336fde) [commit](https://github.com/DPDK/dpdk/commit/2ede1422fa57225b0864702083a8c7bea2c5117e) [commit](https://github.com/DPDK/dpdk/commit/431e6b9a618329cc684f6b3db91195757cbae07e) [commit](https://github.com/DPDK/dpdk/commit/41d71aeb56694f06d60f0de20e5ac2d718ea5328) [commit](https://github.com/DPDK/dpdk/commit/cc13675026303f1da82551deee89027cda3d7aef) [commit](https://github.com/DPDK/dpdk/commit/3d6d85f58c1cb88e3906dd3318f232a58be2e10e) [commit](https://github.com/DPDK/dpdk/commit/189fdd3762758486aec347ebdeb9f5bfe74b5600)

- Remove single-event enqueue/dequeue interfaces from eventdev and drivers, and unify to batch event processing APIs. [commit](https://github.com/DPDK/dpdk/commit/dd1d4398795aeaaa32b66889b64650e940d7204f) [commit](https://github.com/DPDK/dpdk/commit/e20e2148cf9268fa16ad6d0baff943a3eaae5bf0) [commit](https://github.com/DPDK/dpdk/commit/3cdcc0c17c6f62c4355b3adcc3191db8e7546d52) [commit](https://github.com/DPDK/dpdk/commit/88ca872150d0b61b4e6ffcb96f5cecc9e781adb5) [commit](https://github.com/DPDK/dpdk/commit/e1b07dd581cb487e1138e60c21159c499173352e) [commit](https://github.com/DPDK/dpdk/commit/813ab18d5753d6bf78ec614aecc0b6bd583aab1f) [commit](https://github.com/DPDK/dpdk/commit/8b565b3445b67567a459d48e64ba5700320fc852) [commit](https://github.com/DPDK/dpdk/commit/a83fc0f4e118019b2e4fc8f033d59aedce17d7cb) [commit](https://github.com/DPDK/dpdk/commit/5079ede71edeed44c6c25e9ceffcd342940b309f) [commit](https://github.com/DPDK/dpdk/commit/34e3ad3a1e423a874d0d2388efa04d5d6ebee340)

- Remove unaligned/packed markers from ip_frag, efd, pipeline, and IFPGA structures, and add IPv4 checksum function for simple scenarios; narrow packed-member warning suppression scope. [commit](https://github.com/DPDK/dpdk/commit/5763d240624df6e3fd4e93a9f32b3408c7774951) [commit](https://github.com/DPDK/dpdk/commit/1887f919549de2821b0eeabe808a5f2b76370c34) [commit](https://github.com/DPDK/dpdk/commit/eca9f4f830bfd36c615427dd71d782146d34892b) [commit](https://github.com/DPDK/dpdk/commit/f9e1d67f237a00cf94feb4413e3d978fdd632052) [commit](https://github.com/DPDK/dpdk/commit/63c9142b3d634c2abf5a9ef0594ffb652517791c) [commit](https://github.com/DPDK/dpdk/commit/8f999036e16d03d1cc704cf97f5de5b2751d8d49)

- DPAAx and drivers unify to use common prefetch, branch-prediction, and bitops macros/APIs. [commit](https://github.com/DPDK/dpdk/commit/2204658fa80698f17698626293d2cee2b706f2e0) [commit](https://github.com/DPDK/dpdk/commit/6d736695a7467eddd6feeef0be78e1a3b511610c) [commit](https://github.com/DPDK/dpdk/commit/191128d7f6a02b816deaa86d761fbde4483724e9) [commit](https://github.com/DPDK/dpdk/commit/2a682d65f8dbe1e8be9cc2425095827e18c700e3)

- Adjust alignment of IPv6 header type. [commit](https://github.com/DPDK/dpdk/commit/365b7f341ca633743d44c365eccff7ae729d37c2)

- Refactor DPAA/DPAA2 DMA driver structures and share QDMA header file. [commit](https://github.com/DPDK/dpdk/commit/07d679bceee383aa07f508cee4f61ba790030158) [commit](https://github.com/DPDK/dpdk/commit/7cfcce8e5ed809bd1a1c81ab2b84ab6146a4bbd2) [commit](https://github.com/DPDK/dpdk/commit/f1d30e2786b6c0f2cfd4a6bd2ccc5de5d51ae02c)

- Refactor power core/uncore management logic and CPU frequency file structure. [commit](https://github.com/DPDK/dpdk/commit/6f987b594fa6751b49769755fe1d1bf9f9d15ac4) [commit](https://github.com/DPDK/dpdk/commit/ebe99d351a3f79acf305b882052f286c65cd9b25) [commit](https://github.com/DPDK/dpdk/commit/f30a1bbd63f494f5ba623582d7e9166c817794a4)

- Remove HNS3 ROH device support. [commit](https://github.com/DPDK/dpdk/commit/feb4548ffd80bf249239d99bf9053ecf78f815d1)

- EAL adds unreachable and precondition compiler hints. [commit](https://github.com/DPDK/dpdk/commit/bf7ded9a07f6c7f9dbf9c6be417302d783e805d6)

- Refactor DTS build/node information classes and organize test suite specification imports. [commit](https://github.com/DPDK/dpdk/commit/c72ff85d259287c7ec9880b94891310050fe54e6) [commit](https://github.com/DPDK/dpdk/commit/5ea59af40b6d53676f2b369d06047f2ad2685e90)

### Tests

- DTS extends test capabilities for VLAN, L2 forwarding, blocklist, dynamic queue, and checksum offload, and improves test run configuration, remote file transfer, external DPDK build, packet matching, address adjustment, MAC/multicast, and queue management. [commit](https://github.com/DPDK/dpdk/commit/e41fe1f8df707c7de026eae6b529126469bb955f) [commit](https://github.com/DPDK/dpdk/commit/11b2279afbb5e628e9cff26b4b3fff4127711949) [commit](https://github.com/DPDK/dpdk/commit/441c5fbf939b55f635d42ad9b7dcc3741e1c2a7c) [commit](https://github.com/DPDK/dpdk/commit/80158fd411bb06d1a1c22f56fd387ecc49eaf15d) [commit](https://github.com/DPDK/dpdk/commit/f995766758403e13a7b97e6e3e863ac900716844) [commit](https://github.com/DPDK/dpdk/commit/187a944772c9665a7a10e439560d6a505c4e46a2) [commit](https://github.com/DPDK/dpdk/commit/d7181426eda8b123a0bed505ed8388b7ac3726ab) [commit](https://github.com/DPDK/dpdk/commit/c64af3c7a80ee76a771017b56487be1062c7ae1f) [commit](https://github.com/DPDK/dpdk/commit/9f8a257235ac6d7ed5b621428551c88b4408ac26) [commit](https://github.com/DPDK/dpdk/commit/a97f8cc4efef6dd88352c823d98f89a8a8183e58) [commit](https://github.com/DPDK/dpdk/commit/8d46662d93e45ab301a5e4dbb1187d26760aed6a) [commit](https://github.com/DPDK/dpdk/commit/f5418c97fc19a20234ec0cb72ef0ffb5e93fdf2e) [commit](https://github.com/DPDK/dpdk/commit/0264e4087f9504a2847258c99c4dec0e9c42922e) [commit](https://github.com/DPDK/dpdk/commit/e3b16f45cb17fe7dc4251e493fa5e9ef235bfd0d) [commit](https://github.com/DPDK/dpdk/commit/474ce443f7fb8f316faa362ecaf3e6841b3ad6b1) [commit](https://github.com/DPDK/dpdk/commit/c986c3393e95f096ec76fa7a54b0a258ea4c0d5b) [commit](https://github.com/DPDK/dpdk/commit/bee7cf823cd80f83b026a02508ba05fdac1b4113)

### Performance

- Improve TSC frequency estimation and support using the CPU frequency reported by the operating system. [commit](https://github.com/DPDK/dpdk/commit/7268f21aa044309a74592a78955d7051bc7063c1) [commit](https://github.com/DPDK/dpdk/commit/dbdf3d5581caa1de40b5952e41d54b64e39536d1)

- Remove unnecessary prefetch in DPAA2 crypto event mode. [commit](https://github.com/DPDK/dpdk/commit/fa95cbb55c91dbbadb5f8ba1581ddfd603c446ff)

- Align CNXK crypto pointers to 128 bytes and adjust structure layout to eliminate padding space. [commit](https://github.com/DPDK/dpdk/commit/d53727d0a4244cdff51b6892483a5616f3bb730e) [commit](https://github.com/DPDK/dpdk/commit/1c3f7561503734cb62616324d524ddb6e22e6044)

- Remove unnecessary delay in CNXK IPsec statistics collection. [commit](https://github.com/DPDK/dpdk/commit/f852c95807f37f390e21874fbfc681442ad865f6)

- Arm EAL adds WFET power management support and extends the usable range of WFE instructions; the power module can detect supported drivers and enable CPPC. [commit](https://github.com/DPDK/dpdk/commit/990b065f3a3b209282527203663dfb7991723917) [commit](https://github.com/DPDK/dpdk/commit/2f1a90f0455b4920df3a767ab5d9be37dcbf0d12) [commit](https://github.com/DPDK/dpdk/commit/35220c7cb3aff022b3a41919139496326ef6eecc) [commit](https://github.com/DPDK/dpdk/commit/bc5ca53efb4b97a943085d625408410b59080bb6)

- Improve ACC software ring alignment and adjust the LDPC decoder algorithm. [commit](https://github.com/DPDK/dpdk/commit/6aea11c12484489f95549a3b952e98c0a32c5c55) [commit](https://github.com/DPDK/dpdk/commit/b9cb8e68b9bbc4bbb2347b09556207da0a37b398)

- Optimize statistics counter updates for virtio and vhost-user. [commit](https://github.com/DPDK/dpdk/commit/e9dac45c0d3071bf3c6308a0cfbae93421ac4829) [commit](https://github.com/DPDK/dpdk/commit/10be3321d1a8ae4747950344dfa16b00db67f1a6)

- Cache CPU feature flags queried on x86. [commit](https://github.com/DPDK/dpdk/commit/4225db8dc0fa83c9ba1247ac5aec54ab7f3f8d94)

- SFC tunnel offload uses indirect counter. [commit](https://github.com/DPDK/dpdk/commit/5f701365ca2d867467026d72581f47d3f1ca60e0)

- Optimize ethdev fast-path tracepoint activation and netvsc statistics counter updates. [commit](https://github.com/DPDK/dpdk/commit/e075ca1d2a22552a4ee6e2f2fa8d847b9e305c8e) [commit](https://github.com/DPDK/dpdk/commit/84c292fab3447295bf8553e25c31bc50f459c786)

- Optimize the data path and offload configuration of the testpmd SSE MAC swap example. [commit](https://github.com/DPDK/dpdk/commit/8001e1c8f7fecdeb2bb9193a3b7acdb870546c0d) [commit](https://github.com/DPDK/dpdk/commit/222effc6ec29cafc7f23d4f6141b8ba2bd384531) [commit](https://github.com/DPDK/dpdk/commit/1b307e535643c94be10f2dadca8de354bb2def6d)

- IDXD DMA driver sets GRPCFG traffic class to improve transfer performance. [commit](https://github.com/DPDK/dpdk/commit/aa8ed903d29ec90ced2e9dbcf1132d098de3b6f7)

- Improve ICE traffic manager scheduler graph output. [commit](https://github.com/DPDK/dpdk/commit/824e68d4c060cc8c491e6134e764c285fa62126f)

- Optimize the EAL thread creation process. [commit](https://github.com/DPDK/dpdk/commit/64f27886b8bf127cd365a8a3ed5c05852a5ae81d)

- Increase the number of DV sub-flows supported by MLX5 to 64. [commit](https://github.com/DPDK/dpdk/commit/62919d327e58208b21c7972adcf3cdc9c6d7468c)

- Improve DPAA2 Tx scatter-gather mempool usage. [commit](https://github.com/DPDK/dpdk/commit/748b998046355329c5cb4abc99293c5d925de146)

- Improve the FSLMC BMAN buffer acquisition process. [commit](https://github.com/DPDK/dpdk/commit/a116979a03c6873ad3c72422175ac0325f51c846)

- Optimize BNXT TruFlow inline branch prediction and CRC32 hash. [commit](https://github.com/DPDK/dpdk/commit/0c036a1485b9d9163a8fa8059ed5272d060c05e0) [commit](https://github.com/DPDK/dpdk/commit/b14da6540294be2ecae13b69dbe0b00f93bcc597)

- Optimize Thor2 TruFlow stats cache performance. [commit](https://github.com/DPDK/dpdk/commit/ca827d42ad72f90d045716e688b539e53e31a7cc)

### Documentation

- Remove deprecated documentation hints for cryptodev event callback. [commit](https://github.com/DPDK/dpdk/commit/76b354be229926ccdf28951c3dbab4f4bb9570ea)

- Update DTS documentation and build dependencies, and add API and capability documentation generation. [commit](https://github.com/DPDK/dpdk/commit/1e4f18558427c0aa876851d72609b302c2f6b224) [commit](https://github.com/DPDK/dpdk/commit/168d6d94d7309677c539d865693e2e8b422cbbff) [commit](https://github.com/DPDK/dpdk/commit/1e472b5746aeb6189fa254ab82ce4cd27999f868) [commit](https://github.com/DPDK/dpdk/commit/7f9326423a045f7346a459280dc98fed4afd6811) [commit](https://github.com/DPDK/dpdk/commit/64fdb622e3f15da32dee0feffb18e552ff14c044)

- Fix Sphinx documentation build when RTD theme is not installed. [commit](https://github.com/DPDK/dpdk/commit/c523e8643b60f39eda3864af022a84203d962a94)

- Update supported firmware version notes for CPFL. [commit](https://github.com/DPDK/dpdk/commit/d006f936d5dac3b8a17bf1a3f24766f1783cf561)

- Clarify MLX5 PCI VF MTU behavior, fix lcore variables documentation, and update Windows build instructions. [commit](https://github.com/DPDK/dpdk/commit/82caf3da8a7048a9268fc58ec5647ae969fab688) [commit](https://github.com/DPDK/dpdk/commit/37dda90ee15b7098bc48356868a87d34f727eecc) [commit](https://github.com/DPDK/dpdk/commit/5d5dcd8492f8b2863a2de0f5bad223df27749c09)

- Add flow_filtering example scenario snippets. [commit](https://github.com/DPDK/dpdk/commit/16158f34900075f2f30b879bf3708e54e07455f4)

- Update DTS external DPDK options, API documentation generation, and Pydantic configuration notes, and allow Sphinx documentation build warnings. [commit](https://github.com/DPDK/dpdk/commit/0ae32140331f61e6c7e6fe59b4c27e6a2059f395) [commit](https://github.com/DPDK/dpdk/commit/dfef829263561809e20d0000dd4cf628a20ba9b2) [commit](https://github.com/DPDK/dpdk/commit/6597fa4a30add6e0790f0e25833c3e073d76a877) [commit](https://github.com/DPDK/dpdk/commit/3fbb93cff3be23a45fc1ec524f83d001a30df273) [commit](https://github.com/DPDK/dpdk/commit/949d1488e50f0516df065232640617b5a921ed95) [commit](https://github.com/DPDK/dpdk/commit/f4ccce58c1a33cb41e1e820da504698437987efc)

- Update MLX5 compare item limitations and i40e/ICE recommended version notes. [commit](https://github.com/DPDK/dpdk/commit/c07dbef7e0208d4f5e36aa241ce360fc470f203b) [commit](https://github.com/DPDK/dpdk/commit/0fdf973cdb1dcef6513fb36f3105c8123844d937) [commit](https://github.com/DPDK/dpdk/commit/ae52bdf2ce7a6a32202ddfdb1369f415a067fd3b)

- Clarify per-queue statistics definitions and MLX5 send scheduling counters, and update multi-process, security protocol, and example application guides. [commit](https://github.com/DPDK/dpdk/commit/71eae7fe3eac90b70200460c714d1c13ee43dc25) [commit](https://github.com/DPDK/dpdk/commit/4843aacb0d1201fef37e8a579fcd8baec4acdf98) [commit](https://github.com/DPDK/dpdk/commit/c0f5a9dd74f41688660e4ef84487a175ee44a54a) [commit](https://github.com/DPDK/dpdk/commit/8750576fb2a9a067ffbcce4bab6481f3bfa47097) [commit](https://github.com/DPDK/dpdk/commit/8711af290f353f727989684de2e75c7c41d2779a) [commit](https://github.com/DPDK/dpdk/commit/d5f81030df75c587885245ff1b14f123448a97c7)

- Adjust the HTML output directory for DTS API documentation generation. [commit](https://github.com/DPDK/dpdk/commit/497cf54829c28859482998957d75477ae2b1bc1c)

### Build / CI

- Add an option to disable tracepoints at compile time. [commit](https://github.com/DPDK/dpdk/commit/e7bc451c996b5882c5d8267725f3d88118009c75)

- Unify AVX-512 build capability checks across common, drivers, and lib/net. [commit](https://github.com/DPDK/dpdk/commit/979f59decf69023bdba93d16900c45c57fbdd9c0) [commit](https://github.com/DPDK/dpdk/commit/ef7a4025cd714189dc333bb19ea60c2abdeffb7d) [commit](https://github.com/DPDK/dpdk/commit/82621e2fec8143c50f8847f385d6ee646f556b24)

- Fix issues when using buildtools command-line tools as a Meson subproject. [commit](https://github.com/DPDK/dpdk/commit/672c32999e18d7194de90d12d3166c1a967dcb44)

- MANA driver detects rdma-core via pkg-config. [commit](https://github.com/DPDK/dpdk/commit/8d7596cad7abb413c25f6782fe62fd0d388b8b94)

- Fix bitops build failure on GCC configurations without experimental APIs enabled. [commit](https://github.com/DPDK/dpdk/commit/8b65ddc0522ef6d8134edbcfd05bcd7d4f748d19)

- Fix bitset build under MSVC and extend development checks to restrict incompatible builtin bit-count usage. [commit](https://github.com/DPDK/dpdk/commit/5f3cd043a8e115353902b8b5d76ec0bb1928a2f5) [commit](https://github.com/DPDK/dpdk/commit/65c6733a679eb4cc3b6dc00af75bc65280422775)

- Adjust Meson/C compiler version detection and add x86 32-bit cross-compilation configurations for Debian, Fedora, and Arch Linux. [commit](https://github.com/DPDK/dpdk/commit/6f3dbd306de03410cffb40a0f0b47a2cdcfcf362) [commit](https://github.com/DPDK/dpdk/commit/2909f9afbfd1b54ace204d40d57b68e6058aca28) [commit](https://github.com/DPDK/dpdk/commit/3019b11fc1fc7c2ed8a405a551391e51fd94a087) [commit](https://github.com/DPDK/dpdk/commit/198054305b95b9568017571baf49327d23834e9a) [commit](https://github.com/DPDK/dpdk/commit/b0d0c84b3c0ffcdd0c3ef307c4966f06bd296db7) [commit](https://github.com/DPDK/dpdk/commit/08cf11121e06ea1b1fc14127ae8fe08888e77324) [commit](https://github.com/DPDK/dpdk/commit/c3096d218f66708cdad2bc43699e08677b83e8dc) [commit](https://github.com/DPDK/dpdk/commit/b6105ba40a467f5c3463505cf210986273d1031f) [commit](https://github.com/DPDK/dpdk/commit/b7d0c73851aef89fb64867243015b80a138fa758)

- Configure DTS Poetry package mode and fix Docker runner target. [commit](https://github.com/DPDK/dpdk/commit/72a44b260f0f4f824aa473b30b8d97d84512c081) [commit](https://github.com/DPDK/dpdk/commit/4701af16df123dc23986d5d443fe3d2858efd2a6)

- Enable zero-length array and cast-qualifier compilation warnings in the build. [commit](https://github.com/DPDK/dpdk/commit/1435e94f9ea79ae1d3748af90895ed53ef220d6c) [commit](https://github.com/DPDK/dpdk/commit/74efd38b416fcf9eae2a5b429b81b550a73a47b6)

- Fix MVPP2 IPv6 structure migration build issues and strengthen stable API and driver-specific header checks; fix bitset GCC and IFPGA C linkage build compatibility. [commit](https://github.com/DPDK/dpdk/commit/61938a2d178554a0605f8d7ec2e5b7eeaea20e43) [commit](https://github.com/DPDK/dpdk/commit/a3e126fd58d11aee85220480f4bf692612fbadc2) [commit](https://github.com/DPDK/dpdk/commit/e8752e311a3d32d08c3fb04cc9a0262fbaa05b31) [commit](https://github.com/DPDK/dpdk/commit/90cb8ff8196f9b9c1c2bcee1c94ea583789bb63f) [commit](https://github.com/DPDK/dpdk/commit/706fb9b3c6190990126fb5262accbe87a77e5790)

- Fix warning for Arm native build under Meson 0.55 and above. [commit](https://github.com/DPDK/dpdk/commit/c3495563c5e13be8baf150196645bb944230c489)

- Skip driver symlinks without corresponding subdirectories during build. [commit](https://github.com/DPDK/dpdk/commit/dae002ff55a416206e710b05a06f050d5bc4dc6d)

- Fix build issues for MLX5 and DPAA2 drivers under GCC 15. [commit](https://github.com/DPDK/dpdk/commit/09158ba4cb0cefbadf45be08fa0cd587714d8813) [commit](https://github.com/DPDK/dpdk/commit/11f84bf4eab350517ddd59498ae488562e3ccc23)

- Raise the minimum dependency version for the IPsec Multi-Buffer crypto PMD. [commit](https://github.com/DPDK/dpdk/commit/8484d74bd656bc0e951a3ed4e0816ee0fea5e593)

- Fix build issues for power and libvirt, and install libvirt in CI. [commit](https://github.com/DPDK/dpdk/commit/b462f2737eb08b07b84da4204fbd1c9b9ba00b2d) [commit](https://github.com/DPDK/dpdk/commit/d3a214acdfc2016d748760cf54727fc013c54d21)

- Fix build issues for common/CNXK and net/CNXK on Ubuntu 24.04. [commit](https://github.com/DPDK/dpdk/commit/20c29a0e4602b9c7be5ea299457f909846c3785d) [commit](https://github.com/DPDK/dpdk/commit/b9799fb5e7a38c824c91b88d3c89250d23c783e6)

- Fix lock conditions during DPAA error handling and enable Clang thread-safety checks for FQ locks. [commit](https://github.com/DPDK/dpdk/commit/c7c3a329750b81bdaeb3f7ceffac0ec3a65f61f8) [commit](https://github.com/DPDK/dpdk/commit/68508c18a91064ced34c664697ce0c6e25b5f787)

- Fix RCU shift type conversion and enable MSVC support for argparse and mempool. [commit](https://github.com/DPDK/dpdk/commit/ffe827f38e6e0be8a307d7ef9c0e1347874f0af7) [commit](https://github.com/DPDK/dpdk/commit/85a9a589da099f8da3230b38a0eb5e92e458b90c) [commit](https://github.com/DPDK/dpdk/commit/2cd0c96f5b73e81317e97ac719862c9e9149e4ed)

- Enable fallthrough compilation warning for caamflib. [commit](https://github.com/DPDK/dpdk/commit/277552e175b3529863adec9bbd8bb6288164506e)

- Add a tool in buildtools to convert text files to header files. [commit](https://github.com/DPDK/dpdk/commit/50614ebc112e53d54193f8b14ff7d1b37b5be15b)

- Organize DTS build targets and runtime dependencies, adopt Pydantic configuration, and remove warlock and external Python documentation dependencies. [commit](https://github.com/DPDK/dpdk/commit/ecaff610f53d7f4771150a99ffb54e27159f6029) [commit](https://github.com/DPDK/dpdk/commit/a0d77f208c4fc58b6af558efb703c3cc3d062abf) [commit](https://github.com/DPDK/dpdk/commit/9f4e8bdc8c500321935580d638f8bf3fecf9a7cc) [commit](https://github.com/DPDK/dpdk/commit/b935bdc3da26ab86ec775dfad3aa63a1a61f5667) [commit](https://github.com/DPDK/dpdk/commit/f94100da8ead989c6ff070da1c9a8754d69207e9)

- Remove Ubuntu GHA ASan workaround and run more checks in private repository CI. [commit](https://github.com/DPDK/dpdk/commit/5744e912341ee26a0dd5b9ec28b16b8a4e45d1bc) [commit](https://github.com/DPDK/dpdk/commit/2233925d78b2c36fa2db610fd41ca7848b89e0c3)

### Maintenance

- Add queue head/tail pointers to HNS3 debug information. [commit](https://github.com/DPDK/dpdk/commit/364a31b7628536ad7c5fb68603e11c5b166df248)

- Add failure reason and syndrome information to MLX5 hardware flow error logs. [commit](https://github.com/DPDK/dpdk/commit/0573a3928d6239822628a81efa5d0f90ee30f4e0) [commit](https://github.com/DPDK/dpdk/commit/d9acab175085754eec705463bafa7b39b1a88e22)

- Improve argparse error logs to facilitate locating parameter parsing failures. [commit](https://github.com/DPDK/dpdk/commit/9b8df29bf15575f2f0570e6f1e68294a399f6917)

- Improve DPAA2 MTU diagnostic logs and allow dumping DPDMUX counters. [commit](https://github.com/DPDK/dpdk/commit/de08b47438a75afb6f4246d7fed10a2460797b82) [commit](https://github.com/DPDK/dpdk/commit/17eda10df93e1db1344819c19832533d777e48d1)

- NTNIC flow supports dumping and clearing rules. [commit](https://github.com/DPDK/dpdk/commit/6f0fe142caedfd0c9dbfb4e1288cfe6b1462c739) [commit](https://github.com/DPDK/dpdk/commit/f7cb8420e2b004613497048b40baac42f59d6e52)

- NTNIC adds register definitions for FPGA flow, MAC, RPP, SLC, Tx, and statistics modules. [commit](https://github.com/DPDK/dpdk/commit/bbd8b3901bcee48827933169e2c20649953c6724) [commit](https://github.com/DPDK/dpdk/commit/923493778d2c9971d68446db178b05db11915f6a) [commit](https://github.com/DPDK/dpdk/commit/60bc04468b94a32ddf7cac6d4bd8aacc07be3886) [commit](https://github.com/DPDK/dpdk/commit/58c2db9abaa9de58bd8e423cf31e182aabf33263) [commit](https://github.com/DPDK/dpdk/commit/fc777f34f135c36a6fa32e7e0e04980ec86fb207) [commit](https://github.com/DPDK/dpdk/commit/3255bfbefb6a5f0fd6314d957e326cc99ab28baa) [commit](https://github.com/DPDK/dpdk/commit/f08a1161e52070fbd25529f7ddf615bb408e2a6e) [commit](https://github.com/DPDK/dpdk/commit/0beca5d26a883ba2f690956222aee23a266de9ef) [commit](https://github.com/DPDK/dpdk/commit/ea5653cfb89e97e299a55442de795c972e63a1dd) [commit](https://github.com/DPDK/dpdk/commit/3a747e96c4fed9be947a14f89b85358e62f75cbd) [commit](https://github.com/DPDK/dpdk/commit/0214ba672b2559102f141587b33cd43fe1d6a1c3) [commit](https://github.com/DPDK/dpdk/commit/21a66096bb44a4468353782c36fc85913520dc6c) [commit](https://github.com/DPDK/dpdk/commit/3d600f7d565fc530a411759a080c4039f78fde42) [commit](https://github.com/DPDK/dpdk/commit/672e81740f7c529572f4a3509e7a7df0277e90a7) [commit](https://github.com/DPDK/dpdk/commit/a9cba85abe7a8159a1c08af32cf3aa083b112ed2) [commit](https://github.com/DPDK/dpdk/commit/a7e77283c2ab6157fd1cbdb86a0e5dcb9e1de550)

- Graph output improves node layout and adds node dump information. [commit](https://github.com/DPDK/dpdk/commit/ba0a0e44f361cbc4667088a0c0e2d0b63f8dee20) [commit](https://github.com/DPDK/dpdk/commit/0787cdbce54381a3517c24ccec8bbb58215e17b3)

### Others

- Improve readability of graphviz graph export. [commit](https://github.com/DPDK/dpdk/commit/5b8d861cfe89ebcbb08760c7817be0b79b9ff6f9)

- testpmd displays traffic-management parameters; NFP unifies link rate and representor status updates. [commit](https://github.com/DPDK/dpdk/commit/52e5e7c2d393a244e77997b2b3d2edd6365257b7) [commit](https://github.com/DPDK/dpdk/commit/48de6254632fa248e24b502e56f5336eaca6d30f) [commit](https://github.com/DPDK/dpdk/commit/2e3ad18750f8f786f3d4e9a5b0f262e01a6386b4) [commit](https://github.com/DPDK/dpdk/commit/1b3b12c4a89c12fdf33196af1cf80f3f71d7bf8a) [commit](https://github.com/DPDK/dpdk/commit/298f29730a2258df9dd8d2b543e731c4f026cc01) [commit](https://github.com/DPDK/dpdk/commit/441839f1dbe12410de553095d599a060b8a37b25) [commit](https://github.com/DPDK/dpdk/commit/c33504de83eedf218ba4ed3ca75a1ca377346ec2) [commit](https://github.com/DPDK/dpdk/commit/d95cf21d2ed6630d21b5b1ca4abc40155720cd3f)

- testpmd supports displaying command output read from a command file. [commit](https://github.com/DPDK/dpdk/commit/76669d2e7ca9dcf50939882e74b6d06c8ce16e04)
