# Release Note

## Important Changes

### RADOS Block Device (RBD)
- Added an overloaded function that only accepts request types for librbd's ExclusiveLock::accept_request(), and set the return value output parameters of the original method as required. (Architecture event: new IODispatchLayers module)
  ↳ [#66627](https://github.com/ceph/ceph/pull/66627): [0b89d97](https://github.com/ceph/ceph/commit/0b89d978463f7fd74185659a4376bf2c9634e908)
- librbd adds RBD_LOCK_MODE_EXCLUSIVE_TRANSIENT lock mode, which allows other peer nodes to block and wait instead of reporting an error immediately when manually acquiring an exclusive lock. (Architecture event: RBD_Core module change)
  ↳ [#67278](https://github.com/ceph/ceph/pull/67278): [b67e960](https://github.com/ceph/ceph/commit/b67e960141d141285a818a23b2d585435fb00dea), [81eaf2e](https://github.com/ceph/ceph/commit/81eaf2e6bf3f55b8e21aac3e7a6ad42e935c0e91)
- Added a new clone settings chapter to the RBD configuration reference document and improved the description of related options. (Architecture-related: configuration and document constraints)
  ↳ [#66174](https://github.com/ceph/ceph/pull/66174): [f30ce67](https://github.com/ceph/ceph/commit/f30ce67c71b5c61988ed816d609970c83a2fefa0)

### RADOS Gateway (RGW)
- Added max-entries and marker query parameters to the bucket list interface of the RGW management API to support paging and prevent request timeouts due to too many buckets. (Architecture-related: public API)
  ↳ [#65486](https://github.com/ceph/ceph/pull/65486): [e5c1505](https://github.com/ceph/ceph/commit/e5c15059983829919b2bf8e00a67081da812a2ec), [77592b1](https://github.com/ceph/ceph/commit/77592b1886b00b83fce62ca7481ac9710e367dfc)
- RGW added a new configuration item rgw_enable_jwks_url_verification, which allows users to control whether to enable the verification logic of JWKS URL. (Architecture-related: configuration item)
  ↳ [#64936](https://github.com/ceph/ceph/pull/64936): [c0e18cc](https://github.com/ceph/ceph/commit/c0e18ccca77484ce7b879044c05f9daea62769f5)
- Added ssl_reload configuration option to RGW Beast front-end, which supports automatic hot reloading of SSL context at specified intervals without restarting the service. (Architecture-related: configuration items)
  ↳ [#66289](https://github.com/ceph/ceph/pull/66289): [52727bd](https://github.com/ceph/ceph/commit/52727bd5694b5d69f007bd2168b86b9219298bd0)
- Fixed the problem that objects created through multi-part upload could not correctly obtain tags. It now supports parsing and saving tags during initialization. (Architecture-related: public API)
  ↳ [#66335](https://github.com/ceph/ceph/pull/66335): [2754a3a](https://github.com/ceph/ceph/commit/2754a3a7caeed39e7584672910dc99537a056b51)
- Fixed the issue of bucket ACL not being fully migrated when users migrate to accounts. By introducing a new owner name parameter in the bucket ownership change operation, ensure that the authorization information in the access control list is correctly updated. (Architecture-related: public API)
  ↳ [#65665](https://github.com/ceph/ceph/pull/65665): [634d7ed](https://github.com/ceph/ceph/commit/634d7edbcb2dfb609a6bdd2c67eb4ff5c2482dc6)
- The RGW STS token verification logic has been enhanced, it will now check all available JWKS keys to verify the signature, and a new configuration item is added to control whether to enable certificate fingerprint verification of the JWKS URL. (Architecture event: RGW_Auth module change)
  ↳ [#64936](https://github.com/ceph/ceph/pull/64936): [6ca2922](https://github.com/ceph/ceph/commit/6ca29223b35e83c7649c0fd6fbf604ce548aef73)

### RADOS (Core Object Store)
- Fixed the usage problem of bluestore_volume_selection_reserved_factor, and added an interface to obtain additional available space and levels in RocksDBBlueFSVolumeSelector. (Architecture-related: public API)
  ↳ [#66838](https://github.com/ceph/ceph/pull/66838): [91d5739](https://github.com/ceph/ceph/commit/91d57394d8c315cfed68f15b0dfdd8dbd269c4c1)
- Added a timestamp field to the Monitor information structure to record the time of joining the mapping, updated the serialization version and related printing, dumping and testing logic. (Architecture-related: serialization compatibility)
  ↳ [#67324](https://github.com/ceph/ceph/pull/67324): [48ecc59](https://github.com/ceph/ceph/commit/48ecc59c5309e793e5547804778d1affa87d8b4b)
- Fixed the problem of incorrect calculation of the reservation factor in the BlueFS volume selector, and added a new interface to obtain available additional space. (Architecture-related: public API)
  ↳ [#66838](https://github.com/ceph/ceph/pull/66838): [1bc9e3a](https://github.com/ceph/ceph/commit/1bc9e3a8aca994cc1cc12918bdb8ea6315a0b61f)
- Fixed the configuration failure problem caused by failure to delete extended attributes when removing RGW life cycle configuration. (Architecture-related: RGW life cycle configuration persistence)
  ↳ [#64741](https://github.com/ceph/ceph/pull/64741): [36bc8e4](https://github.com/ceph/ceph/commit/36bc8e4242a352830dce516f4b40e3dfa0de72f5)

### Client Libraries and Interfaces
- Added --run-benchmark option to ceph-osd to support benchmark testing after OSD is created and before joining the cluster. (Architecture-related: command line interface)
  ↳ [#65523](https://github.com/ceph/ceph/pull/65523): [ca4b31b](https://github.com/ceph/ceph/commit/ca4b31b007ebcc731e5309c2d19204ccbfafd26c)
- Added --service_unique_id command line parameter, allowing to associate custom unique identifiers when enabling performance counters for Ceph services. (Architecture-related: command line parameters)
  ↳ [#65588](https://github.com/ceph/ceph/pull/65588): [9bccd05](https://github.com/ceph/ceph/commit/9bccd053715219893ce0aae571c0be99d4012f52), [88f8fd2](https://github.com/ceph/ceph/commit/88f8fd2481301ad86a31c108f893433c992ae930)
- Added is_frag_valid method in the frag_t structure, which is used to detect damaged fragmented data caused by byte order errors. (Architecture-related: public API)
  ↳ [#66541](https://github.com/ceph/ceph/pull/66541): [204bcc8](https://github.com/ceph/ceph/commit/204bcc8bfcab819f27fc74b2edc0c6272ca5674c)
- Fixed the problem that the msgr2 protocol may return the wrong allowed mode when authentication fails, ensuring data accuracy by splitting the AuthServer interface into functions that independently obtain the authentication method and connection mode. (Architecture event: AuthRegistry module change)
  ↳ [#65335](https://github.com/ceph/ceph/pull/65335): [d9703a9](https://github.com/ceph/ceph/commit/d9703a999eee5896762b78a4027d5beaa795c4c9)
- Fixed an issue where ceph_statxat() could not handle file descriptors correctly when an empty pathname was passed in and the AT_EMPTY_PATH flag was set. (Architecture-related: public API)
  ↳ [#61166](https://github.com/ceph/ceph/pull/61166): [8cfe15a](https://github.com/ceph/ceph/commit/8cfe15a59cce2e7c295d7c8108a39f75ab843a44)
- Fixed the memory leak problem caused by use after release when the client uses the non-blocking asynchronous read API. (Architecture-related: public API)
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [bd98ba4](https://github.com/ceph/ceph/commit/bd98ba47eb59e4d3bffafdd7f509890a2bd850d8)
- Fixed an issue where rbd-mirror may incorrectly delete the local mirror when resynchronizing in snapshot mirroring mode. (Architecture-related: rbd-mirror snapshot mirror consistency)
  ↳ [#64739](https://github.com/ceph/ceph/pull/64739): [e1fd62e](https://github.com/ceph/ceph/commit/e1fd62e8b7851741721d72ac9b363a4e2ab1b90f)
- Fixed the byte order conversion problem of the frag_t type during network transmission and storage to ensure that it can be processed correctly on big-end machines. (Architecture-related: platform compatibility)
  ↳ [#66541](https://github.com/ceph/ceph/pull/66541): [04b8dc5](https://github.com/ceph/ceph/commit/04b8dc58fb16887f2053a6b2554293977a32547e)
- Change the parameter type of the strict_strtob function from const char* to std::string_view, and use boost instead for case-insensitive string comparison to optimize the implementation. (Architecture event: strict_strtob public API parameter type change)
  ↳ [#63019](https://github.com/ceph/ceph/pull/63019): [cfd31b6](https://github.com/ceph/ceph/commit/cfd31b6b4f9665c9a03421be600c7196021bd348)
- Move the inline methods in the frag.h header file to the frag.cc implementation to optimize the compilation structure. (Architecture-related: public header file compilation optimization)
  ↳ [#66541](https://github.com/ceph/ceph/pull/66541): [84dfe73](https://github.com/ceph/ceph/commit/84dfe7301019c95d91d4249481c90bb9334f687f)
- Fixed a security vulnerability where unprivileged users could still independently set SUID/SGID permission bits. Setting these privileged bits by unprivileged users is now prohibited under any circumstances. (Architecture-related: Security Behavior)
  ↳ [#66039](https://github.com/ceph/ceph/pull/66039): [44c3410](https://github.com/ceph/ceph/commit/44c3410cf519aa4a3ea5423d909e0b9a4d98efc8)
- Amended the documentation of ceph_statxat() API in libcephfs.h to clarify that its flags parameter only supports AT_STATX_DONT_SYNC and AT_SYMLINK_NOFOLLOW. (Architecture-related: public API)
  ↳ [#61166](https://github.com/ceph/ceph/pull/61166): [47166cf](https://github.com/ceph/ceph/commit/47166cf7ba57260d4a86d4801acaf984e33bd68b)

### CephFS (Ceph File System)
- Added the new configuration item mds_allow_batched_ops to support disabling batch operations, aiming to solve the problem that batch search or attribute acquisition cannot effectively prompt MDS to quickly switch states. (Architecture-related: Configuration items)
  ↳ [#64539](https://github.com/ceph/ceph/pull/64539): [f51d2a6](https://github.com/ceph/ceph/commit/f51d2a6352aff78d30862d5c4b51bdfce948ff3c), [dd1b518](https://github.com/ceph/ceph/commit/dd1b5184805de01caf5cd12adbd6bc3d312ff706)
- Corrected the use and sending logic of issue_seq in the capability message between the client and MDS to ensure that the correct sequence number type and field is used. (Architecture-related: client and MDS communication protocol)
  ↳ [#61300](https://github.com/ceph/ceph/pull/61300): [8826727](https://github.com/ceph/ceph/commit/88267276ad077f85902213c28aeb9c37bbbb17f9), [4d096fb](https://github.com/ceph/ceph/commit/4d096fb00de7e54a67594f96789985e6f6cf55a7), [bfb3ce3](https://github.com/ceph/ceph/commit/bfb3ce314d20240fa41d0ee1dd05c90ed44bd4ea), [8793497](https://github.com/ceph/ceph/commit/879349719cacc4414fcdb42696777ab80d0dbd42), [e13cdb4](https://github.com/ceph/ceph/commit/e13cdb4c7aa2852e4a4ae86b833008896e2914b6)
- Modifying the CephFS max_mds configuration when the cluster is unhealthy now requires explicitly passing the confirmation flag to prevent misoperations from causing system instability. (Architecture-related: CLI operation confirmation mechanism)
  ↳ [#60398](https://github.com/ceph/ceph/pull/60398): [fe45c05](https://github.com/ceph/ceph/commit/fe45c051dc7ff829d874ff0f0c1832122cff5e40)
- Fixed the metadata corruption problem in the libcephfs asynchronous write path caused by the callback not holding the client lock. (Architecture-related: data consistency)
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [ce59fc0](https://github.com/ceph/ceph/commit/ce59fc007b04392764fefbbbb8331d882a92af0d)
- Fixed the release issue after use of C_Flush_Journal in MDLog, and made the submit_entry method return the sequence number of the submitted event. (Architecture-related: public API)
  ↳ [#65141](https://github.com/ceph/ceph/pull/65141): [4dda1f1](https://github.com/ceph/ceph/commit/4dda1f1a759663b2cd7e26eebdd7d4dcd5b278c1)
- Fixed multiple issues in client statfs calls: ensuring correct use of incoming paths, finding quota root nodes based on inodes and supporting upward traversal, and returning errors directly in the unconnected state. (Architecture-related: public API)
  ↳ [#65133](https://github.com/ceph/ceph/pull/65133): [097bcc0](https://github.com/ceph/ceph/commit/097bcc0c1c9c7e5df3a3c1acc22f5958c5ad7768), [84af287](https://github.com/ceph/ceph/commit/84af2873bab0d658b8b56b0e78c9a4b64df4a603), [8546554](https://github.com/ceph/ceph/commit/8546554ce72d11325999b31fbe7c19d1b145efca)
- Fixed the issue where the export_ephemeral_random_pin field was incorrectly output in integer format when exporting inode information. (Architecture-related: public API)
  ↳ [#65162](https://github.com/ceph/ceph/pull/65162): [50a1c12](https://github.com/ceph/ceph/commit/50a1c129af018b0443bf530fb1383f52932efe35)
- Rename the completion processing method of MDSContext from complete to finish to unify the code style and enhance the security of the dump orphan directory command. (Architecture event: MDSContext public method renamed)
  ↳ [#62517](https://github.com/ceph/ceph/pull/62517): [a589e14](https://github.com/ceph/ceph/commit/a589e142a1116754e29ca1d732e30670701fbdfe)

### Cluster Management (Monitors and Managers)
- Optimized the holding time of the DaemonStateIndex lock to avoid thread blocking caused by calling Python callbacks during the lock holding period. (Architecture event: MgrAuthAndDaemon module change)
  ↳ [#65462](https://github.com/ceph/ceph/pull/65462): [6aac9a5](https://github.com/ceph/ceph/commit/6aac9a583fed5bbd9e120c14c51ce7db9f620ae4)
- Fixed the problem of missing heartbeats between nodes due to the election feature not being ready when the Monitor is started or restarted. (Architecture-related: cluster communication protocol)
  ↳ [#62924](https://github.com/ceph/ceph/pull/62924): [33bb15b](https://github.com/ceph/ceph/commit/33bb15bbb36d0eabd7aac35ff8d618e52e24e801)
- Change the default constructor of MonMap related classes to use = default declaration. (Architecture-related: public API)
  ↳ [#67324](https://github.com/ceph/ceph/pull/67324): [fe645ca](https://github.com/ceph/ceph/commit/fe645caefa50010080eef490b2c096c3f4fae2ec)
- Fixed the cluster label matching logic of Prometheus query in the Grafana dashboard to ensure compatibility with historical indicators that lack cluster labels after the upgrade, so that old version data can still be displayed normally after the upgrade. (Architecture-related: platform compatibility)
  ↳ [#66985](https://github.com/ceph/ceph/pull/66985): [01434ad](https://github.com/ceph/ceph/commit/01434ad713787be4d4b706a496907bfaa4701a4b)
- Fixed the decompression failure in the container due to CMake quote escaping issues in the Dashboard front-end build script, and added NPM_CACHEDIR environment variable support to optimize build performance. (Architecture-related: build and installation methods)
  ↳ [#65186](https://github.com/ceph/ceph/pull/65186): [78fe267](https://github.com/ceph/ceph/commit/78fe267fdc9787bd124cffff65660b3c100cd738), [c8841d6](https://github.com/ceph/ceph/commit/c8841d64c03cf46dcc8e6123ffe364006754bb0b), [f7e2a85](https://github.com/ceph/ceph/commit/f7e2a85031d7e7569213a558a05189a29f04fca6)

### Cross-cutting / Other Architecture-related Changes
- Updated the release process documentation to explain that the new Jenkins task is now used to automatically build pre-release container images, replacing the original manual build steps that were complex and dependent on arm64 hosts. (Architecture-related: build and installation methods)
  ↳ [#62612](https://github.com/ceph/ceph/pull/62612): [d81ebc5](https://github.com/ceph/ceph/commit/d81ebc5f039824c09b35bc2582706023d3b1ec50)
- Fixed deprecation warning about std::shared_ptr atomic operations in GCC 14, and improved cross-compiler compatibility by using the __cpp_lib_atomic_shared_ptr feature test macro. (Architecture-related: Platform compatibility)
  ↳ [#66185](https://github.com/ceph/ceph/pull/66185): [e68c5db](https://github.com/ceph/ceph/commit/e68c5db5df138a453e779c2f243cbe53bb65aa49), [8d56b19](https://github.com/ceph/ceph/commit/8d56b19f7899aa7192345d336edbc7ca933948a4)
- Removed the hard-coded _FORTIFY_SOURCE definition in CMake and instead relied on environment variable settings to solve the compilation failure problem caused by default value conflicts in Ubuntu 24 and other environments. (Architecture-related: build and installation methods)
  ↳ [#65659](https://github.com/ceph/ceph/pull/65659): [c27259a](https://github.com/ceph/ceph/commit/c27259ac1a8d4451b13949b01cf5dec85bc3bd78)
- Fixed external action references in GitHub Actions workflows from version tags to specific SHA-1 commit hashes to improve build security. (Architecture-related: build and install methods)
  ↳ [#65758](https://github.com/ceph/ceph/pull/65758): [dacc5fa](https://github.com/ceph/ceph/commit/dacc5fac1dca33f67acbf4d885b9fa3a99f00175)
- Limit the pip version to lower than 25.3 in the Readthedocs build configuration to solve the problem of document build failure caused by pybind's lack of PEP 517 support. (Architecture-related: build and installation methods)
  ↳ [#66117](https://github.com/ceph/ceph/pull/66117): [72f675b](https://github.com/ceph/ceph/commit/72f675b8b5f472e35fed8112a40b0d511b6c36aa)

## Routine Changes

### New features
- Added OSD management command clear_shards_repaired, which is used to manually reset the shard repair count to clear false positive OSD_TOO_MANY_REPAIRS alarms.
  ↳ [#60567](https://github.com/ceph/ceph/pull/60567): [d27afb4](https://github.com/ceph/ceph/commit/d27afb44e6c6c9fb71e83f18531f5ac4b3825294)
- HealthMonitor adds a new topology-aware network partition detection function, which can monitor communication interruptions between nodes based on CRUSH topology-level aggregation reports and provide corresponding health warnings.
  ↳ [#63024](https://github.com/ceph/ceph/pull/63024): [a7477be](https://github.com/ceph/ceph/commit/a7477bef6484134887c19371ca3968090794fcc5)
- Added asok command dump stray to MDS to support exporting orphan directory contents.
  ↳ [#62517](https://github.com/ceph/ceph/pull/62517): [3bafd65](https://github.com/ceph/ceph/commit/3bafd65c2589b46008085a916b9f8fe72c7baef8), [3fc942c](https://github.com/ceph/ceph/commit/3fc942c985d7fe51d333924f95797aea65af6bfc)
- Added pending and failed count indicators for RGW's Kafka and AMQP publish push processes, and updated failure statistics when message processing expires.
  ↳ [#65903](https://github.com/ceph/ceph/pull/65903): [765671a](https://github.com/ceph/ceph/commit/765671a91861f043f8794bf98f3932a41d54ead5)
- Added system information field to MDS status command output, including CPU architecture and endianness details.
  ↳ [#66541](https://github.com/ceph/ceph/pull/66541): [0226153](https://github.com/ceph/ceph/commit/02261536cc359165a38eeeb69b3ec2ef49adcb3e)
- Add dump method to dirfrag_t to support objectized output, and update MDSCacheObjectInfo::dump to use this new method instead of streaming output.
  ↳ [#66541](https://github.com/ceph/ceph/pull/66541): [c49ea95](https://github.com/ceph/ceph/commit/c49ea953288413d21b4b32419cf6d521551becc5)

### bug fixes
- radosgw-admin now supports specifying the SSL CA certificate path via the environment variable CURL_CA_BUNDLE, which is used to verify server certificates in HTTPS management operations.
  ↳ [#64357](https://github.com/ceph/ceph/pull/64357): [1c738a6](https://github.com/ceph/ceph/commit/1c738a6d0f64db2240d44fbf00cfc4ae90279694)
- Fixed an issue with the asynchronous messaging protocol encoding messages prematurely when the connection feature was not ready, ensuring messages are only encoded after the feature is set.
  ↳ [#65624](https://github.com/ceph/ceph/pull/65624): [542de25](https://github.com/ceph/ceph/commit/542de25001d89a23d370fe99c2958b8bc38af436)
- Fixed multiple session management and race condition issues in MDS when exporting/importing subtree tasks are interrupted, including cleaning up importing sessions, export confirmation processing, and client error eviction.
  ↳ [#62055](https://github.com/ceph/ceph/pull/62055): [bcbed30](https://github.com/ceph/ceph/commit/bcbed3092b72f6e4d6f6b207b4c78c30ceb48ee4), [44b9847](https://github.com/ceph/ceph/commit/44b98477444c4fc6bb64aa4681a24864fa12c761), [ed3bec3](https://github.com/ceph/ceph/commit/ed3bec39ed088f97f0cebf16b55feb0a96350476)
- Fixed the thread safety issue when CephContext notifies observers after fork to ensure that the lock is acquired correctly.
  ↳ [#62051](https://github.com/ceph/ceph/pull/62051): [80e7789](https://github.com/ceph/ceph/commit/80e7789ba6be3602f5ba518f3d14d53ea633fe88)
- Fixed an issue where the ISAL compression function could not take effect due to build macro removal, and a warning would be output when enabled on an unsupported architecture.
  ↳ [#64815](https://github.com/ceph/ceph/pull/64815): [d098334](https://github.com/ceph/ceph/commit/d098334b7c9027c263a40a2bf02b4d299b06497e)
- Fixed an issue where the mgr module incorrectly removed an offline or removed OSD from the daemon state when handling it, clearing its health indicators directly instead.
  ↳ [#67527](https://github.com/ceph/ceph/pull/67527): [3e148dd](https://github.com/ceph/ceph/commit/3e148ddabcaad1a76c0819a00af5fbf323ee159f)
- Fixed an assertion failure that could be triggered when the client reads a zero-byte file in non-blocking mode.
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [d04f782](https://github.com/ceph/ceph/commit/d04f78219a313a88a92bb6c2982caafc55518d9e)
- Fixed a crash in the CephFS client due to improper management of capability references when object caching is disabled.
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [c09c4e1](https://github.com/ceph/ceph/commit/c09c4e1117c73f890022933d852782634c3f3b44)
- Fixed the deadlock problem caused by the lock waiting for beacon confirmation during MDS shutdown.
  ↳ [#64886](https://github.com/ceph/ceph/pull/64886): [aee88b7](https://github.com/ceph/ceph/commit/aee88b701914cfdfa15558ad6d74850da734bc30)
- Adjusted the triggering threshold of versioned bucket shard rebalancing so that it triggers earlier to adapt to the higher number of keys.
  ↳ [#63567](https://github.com/ceph/ceph/pull/63567): [72092a6](https://github.com/ceph/ceph/commit/72092a63aa378af4b700ed8d24fdb32e232c2cb8)
- Fixed an issue where RGW incorrectly displayed empty storage classes as STANDARD when listing multipart uploads.
  ↳ [#64313](https://github.com/ceph/ceph/pull/64313): [daa0baf](https://github.com/ceph/ceph/commit/daa0baf2c4f2da2e705a6789a91c976e4a1ba54a)
- Fixed the RGW Keystone authentication logic so that it no longer forces dependence on the administrator token when validating user tokens.
  ↳ [#64202](https://github.com/ceph/ceph/pull/64202): [f9d2094](https://github.com/ceph/ceph/commit/f9d209427d7d6f8c8928699190ad1adb1a279e31)
- Fixed a crash in cephfs-journal-tool when processing invalid dump files, and now verifies file header information before restoring.
  ↳ [#62115](https://github.com/ceph/ceph/pull/62115): [acfdb5a](https://github.com/ceph/ceph/commit/acfdb5aa935f9d083afceb4d27265074b824577f), [f6d296a](https://github.com/ceph/ceph/commit/f6d296a6c3888b4296fa24d4554e86b3a40370e4)
- Fixed the issue where the client incorrectly assigned the capability serial number field to itself instead of correctly updating it to the peer serial number when processing capability export messages.
  ↳ [#61300](https://github.com/ceph/ceph/pull/61300): [6edaebb](https://github.com/ceph/ceph/commit/6edaebb4ce9f47d27e4a1eded6ad2e7e8439d7a4)
- Fixed an illegal memory access problem caused by not checking whether the dn array is empty when MDS handles getattr requests.
  ↳ [#61451](https://github.com/ceph/ceph/pull/61451): [5be3d2f](https://github.com/ceph/ceph/commit/5be3d2fe4040d46b37982b9d598c1602765b65ae)
- Fixed the shutdown hang issue caused by a race condition when the asynchronous message module closes the connection.
  ↳ [#65785](https://github.com/ceph/ceph/pull/65785): [ec57e01](https://github.com/ceph/ceph/commit/ec57e01b8d75f691de290dbdddb8aaf41dc6eabc) | [#64924](https://github.com/ceph/ceph/pull/64924): [8af12ef](https://github.com/ceph/ceph/commit/8af12ef9d1876e19b753e0a162f69fb04e56b1df)
- Fixed an issue where RGW's Swift API could not delete container metadata due to incorrect merging of properties when rebuilding a bucket or updating metadata.
  ↳ [#64387](https://github.com/ceph/ceph/pull/64387): [c5887a7](https://github.com/ceph/ceph/commit/c5887a763b41aad5d89955e88337288f1019cccc)
- Adjusted RGW sharding expansion logic to ensure that pending versioned buckets can also trigger re-sharding.
  ↳ [#63567](https://github.com/ceph/ceph/pull/63567): [b8a12ca](https://github.com/ceph/ceph/commit/b8a12ca1ebcddcee46b87a6dfea4e18e57b0cd43)
- Fixed the calculation logic of the bluestore histogram default base size to use the allocator's actual block size instead.
  ↳ [#67398](https://github.com/ceph/ceph/pull/67398): [53dd77f](https://github.com/ceph/ceph/commit/53dd77f07ebabf633f27395da331efa8605b2345)
- Fixed an issue in MDS where silent operations were incorrectly scheduled for imported inodes of non-head nodes.
  ↳ [#61857](https://github.com/ceph/ceph/pull/61857): [f786bd3](https://github.com/ceph/ceph/commit/f786bd335bd40dd1904b024bf3f9d5a74e01173d)
- Fixed an issue where BlueFS truncation operations could trigger assertion failures when allocation unit alignment exceptions occurred.
  ↳ [#63753](https://github.com/ceph/ceph/pull/63753): [9832d76](https://github.com/ceph/ceph/commit/9832d7666439903edd11a20b1c6ae20de66dd9e4)
- Fixed C_Flush_Journal use-free issue in MDS caused by dereferencing after object destruction.
  ↳ [#65141](https://github.com/ceph/ceph/pull/65141): [cdea0ee](https://github.com/ceph/ceph/commit/cdea0ee3d091a6932206be687f362583ec2cd2f2)
- Fixed an issue where the client ll_walk interface incorrectly treated input file paths as relative to non-existent inode 0 and now correctly handles absolute paths instead.
  ↳ [#62499](https://github.com/ceph/ceph/pull/62499): [a717ce0](https://github.com/ceph/ceph/commit/a717ce0d2caf2744dbaa5359314494dbdf9fb162)
- Fixed an issue where settings were lost due to not explicitly calling the initialization function when configuring mon_memory_target.
  ↳ [#63804](https://github.com/ceph/ceph/pull/63804): [9e38418](https://github.com/ceph/ceph/commit/9e38418218a0b26905050c9e0046344848ed796b)
- Fixed an issue in the MDS dump stray directory command that could incorrectly close object segments due to incorrect status checking.
  ↳ [#62517](https://github.com/ceph/ceph/pull/62517): [498ddd1](https://github.com/ceph/ceph/commit/498ddd12c5db02a6388d845e852aace8158bca93)
- Fixed assertion failures and exceptions caused by null pointers in MDCache, ensuring the stability of request cleaning and distribution logic.
  ↳ [#66472](https://github.com/ceph/ceph/pull/66472): [02cc17d](https://github.com/ceph/ceph/commit/02cc17d76c9099603e3331b216807c032a3ad821), [388544b](https://github.com/ceph/ceph/commit/388544ba72d0dc7484ae6877a2a989d84a883fd5)
- Fixed the logic error when the client performs directory operations and lookups on non-directory inodes, avoiding reference leaks and error code issues.
  ↳ [#65289](https://github.com/ceph/ceph/pull/65289): [11a08c5](https://github.com/ceph/ceph/commit/11a08c5871d0ba46ed289a9642c77e81c6c56c87), [6dc55fc](https://github.com/ceph/ceph/commit/6dc55fcda3b9280a8ae3cdcc681a9d1fa0f7148d)
- Fixed a logic error in MDS's handling of snapshot domain checks and boolean attribute parsing, ensuring correct rejection of directory operations and robustness of configuration parsing.
  ↳ [#63019](https://github.com/ceph/ceph/pull/63019): [571e86f](https://github.com/ceph/ceph/commit/571e86f49b0667a117bd251872ddb5d01a516195), [d8419fe](https://github.com/ceph/ceph/commit/d8419fe9a0ffb30d2f66ef4ff4ca9ba5e3bda766)
- Fixed BlueStore's data boundary and dirty range marking issues in re-sharding and deletion operations, ensuring data consistency and performance.
  ↳ [#66518](https://github.com/ceph/ceph/pull/66518): [cd15c46](https://github.com/ceph/ceph/commit/cd15c46cd765a8f8f07c9668d169f5248722182a), [d901772](https://github.com/ceph/ceph/commit/d901772ec0600a55bf8058d2fd78f78ef896ba67)
- Fixed the issue where the configuration parameters could not take effect due to the temporary Messenger stack singleton not being released in the foreground mode of the daemon process.
  ↳ [#66897](https://github.com/ceph/ceph/pull/66897): [d659149](https://github.com/ceph/ceph/commit/d6591499ec89de4de0639f1559e48a211f3838c4)
- Fixed the problem of no output and error prompts for monitoring historical operation commands, and added dynamic tracking support for configuration items.
  ↳ [#64842](https://github.com/ceph/ceph/pull/64842): [6c88d29](https://github.com/ceph/ceph/commit/6c88d29bf05393a8bae225fc5a7ac5efe1e06af6)
- Fixed the issue of lock blocking caused by MDS not refreshing the log after early reply, ensuring the correctness of concurrency control.
  ↳ [#64539](https://github.com/ceph/ceph/pull/64539): [c057caa](https://github.com/ceph/ceph/commit/c057caa9453a83fde59c999e9b3788a51310eac9)
- MDS adds authentication credentials and import count fields to session dump output to more accurately identify session source and status.
  ↳ [#65267](https://github.com/ceph/ceph/pull/65267): [2df453c](https://github.com/ceph/ceph/commit/2df453cb686b9c68a5e603aeb6a5375b002a2a9d) | [#62055](https://github.com/ceph/ceph/pull/62055): [8a9a457](https://github.com/ceph/ceph/commit/8a9a45789b41a368f2bfc817625388ddf537256d)
- Fixed the crash problem caused by unhandled exceptions during indicator parsing, and enhanced the fault tolerance of DaemonMetricCollector when parsing ASOK indicators.
  ↳ [#65228](https://github.com/ceph/ceph/pull/65228): [9608883](https://github.com/ceph/ceph/commit/96088837e53e55476d13b2c08a5e1bc51d29eddb)
- Fixed a potential race condition in the DiscardThread lifecycle in the blk/kernel module, eliminating the race between thread startup and removal by removing the thread ID dependency and using raw pointer management instead.
  ↳ [#65214](https://github.com/ceph/ceph/pull/65214): [b201cbf](https://github.com/ceph/ceph/commit/b201cbf5c5d58c70a879a6ff25a22aa1a5633871)
- Fixed an issue where the RGW S3 interface incorrectly returned the aws-chunked Content-Encoding value in the Get/HeadObject response. This field will now be filtered out before returning to comply with the S3 specification.
  ↳ [#65219](https://github.com/ceph/ceph/pull/65219): [e1dfc14](https://github.com/ceph/ceph/commit/e1dfc14e7052c1e12c3364874f37ab361e1f7c1c)
- Fixed an issue where when librbd handles group snapshot removal and rollback operations, failure to create IoCtx may result in the image not being closed and memory leaks.
  ↳ [#64621](https://github.com/ceph/ceph/pull/64621): [2273510](https://github.com/ceph/ceph/commit/2273510230304b42908b58bdd20460e623b62472)
- Fixed an issue with radosgw-admin causing the bucket list and bucket stats command output format to be broken due to max_entries not being initialized when the --max-entries parameter was not specified. This parameter is now ensured to be passed correctly to maintain backward compatibility.
  ↳ [#65486](https://github.com/ceph/ceph/pull/65486): [39e7715](https://github.com/ceph/ceph/commit/39e7715f5419aad5eeab266701aac0195fd0e16a)
- Fixed the concurrency problem caused by unlocked access to epoch mapping in the OSDSuperblock class, ensuring thread safety by encapsulating the mapping data into a GuardedMap structure with mutex protection and updating the relevant calling interface.
  ↳ [#64732](https://github.com/ceph/ceph/pull/64732): [1fdf9cd](https://github.com/ceph/ceph/commit/1fdf9cd6e4a5dc666e3ba5921fc6577db14afecc)
- Fixed the problem that MonClient may continue to execute tick() during the shutdown process. Now when a stop state is detected, the scheduled task will be skipped and returned directly.
  ↳ [#66915](https://github.com/ceph/ceph/pull/66915): [f8a8a56](https://github.com/ceph/ceph/commit/f8a8a5663842bbcbf343219733c4c8b2da29225b)
- Fixed an issue caused by MDS incorrectly performing a charmap handler check when handling rename requests without a session, which is now only performed when a session exists.
  ↳ [#64954](https://github.com/ceph/ceph/pull/64954): [601624d](https://github.com/ceph/ceph/commit/601624d80162c0f75337cf48022c03a6b71eeb71)
- Fixed the issue where OSD ignores the beacon reporting interval configuration when clearing cleared snapshots, and avoids frequent generation of OSDMap epochs by unifying the beacon sending logic.
  ↳ [#65584](https://github.com/ceph/ceph/pull/65584): [a1446e8](https://github.com/ceph/ceph/commit/a1446e800aca31641fc86e88fc6e4acac124ee64)
- Fixed two bugs in the OSD cleanup module: undefined behavior when handling inconsistent objects, and ensuring that operator-initiated repair operations are no longer limited by the upper limit on the number of auto-repair errors.
  ↳ [#66247](https://github.com/ceph/ceph/pull/66247): [69cf85a](https://github.com/ceph/ceph/commit/69cf85a28418fb75a24ed82bdde61e09f3bef58b) | [#64915](https://github.com/ceph/ceph/pull/64915): [78ba60e](https://github.com/ceph/ceph/commit/78ba60e68d82fdd3e743fdeafbadf17805704b5e)
- Fixed CephFS client initialization sequence to ensure mon authentication is completed before starting objecter.
  ↳ [#66471](https://github.com/ceph/ceph/pull/66471): [b617c9b](https://github.com/ceph/ceph/commit/b617c9b3259e461ace5cd7e6c50aa3cebfd1f104)
- Fixed the problem of truncation of returned results when MDS processes snapdiff requests due to the inability of entries with the same name to fully fit into a single fragment, ensuring that incomplete entries with the same name are correctly rolled back and discarded when there is insufficient space.
  ↳ [#65363](https://github.com/ceph/ceph/pull/65363): [887dbc2](https://github.com/ceph/ceph/commit/887dbc2933c4ffa4b10fd0ea1a96514919930e8f), [f512eda](https://github.com/ceph/ceph/commit/f512edacf124e851ccb8ffcc754f8aa55b539d95), [baeae88](https://github.com/ceph/ceph/commit/baeae8885ca026ee3ab0447a283a98002045bd05)
- Fixed an issue where BlueStore was not forcing splitting when processing spanned blobs at shard boundaries, ensuring re-sharding logic is triggered correctly to avoid data layout errors.
  ↳ [#66518](https://github.com/ceph/ceph/pull/66518): [90a4bdb](https://github.com/ceph/ceph/commit/90a4bdb313756fa839822f3196b9975c498a0b99)
- Fixed an issue where olh_ related attributes were not discarded correctly when copying objects from a versioning-suspended bucket to a versioning-disabled bucket.
  ↳ [#65556](https://github.com/ceph/ceph/pull/65556): [d6c5980](https://github.com/ceph/ceph/commit/d6c598052d82e4def14d097de65ccd408e6def93)
- Fixed the issue where cephfs-journal-tool incorrectly resets the pruning position when resetting the log, ensuring that old useless log objects can be cleaned up during the regular pruning cycle to reclaim metadata pool space.
  ↳ [#65602](https://github.com/ceph/ceph/pull/65602): [829fa28](https://github.com/ceph/ceph/commit/829fa28a72e6f03b8ee4663281aa7475da4ef159)
- Fixed the problem in the RGW life cycle policy that the deletion mark was removed prematurely due to being unconditionally judged to be expired. It is now correctly judged based on the modification time.
  ↳ [#65966](https://github.com/ceph/ceph/pull/65966): [b36242c](https://github.com/ceph/ceph/commit/b36242ce1c46fab5a94609a02870faa0435530cc)
- Fixed the problem caused by misuse of the head object removal interface when using the --bypass-gc parameter to delete a bucket containing copied objects. Now the relevant internal methods are renamed and use the correct reference counting interface to clean up the tail objects.
  ↳ [#66003](https://github.com/ceph/ceph/pull/66003): [83e895a](https://github.com/ceph/ceph/commit/83e895a02fff83fbb476ec97048e763b08a8bc48)
- Fixed an issue caused by rbd-mirror using only the pool ID for the remote metadata cache key when mirroring multiple clusters. The cluster fsid is now included in the cache key to ensure uniqueness.
  ↳ [#66296](https://github.com/ceph/ceph/pull/66296): [6d45af8](https://github.com/ceph/ceph/commit/6d45af82879b038b10ecbe36f688467ddc52b10d)
- Fixed an issue in scrub preemption logic that incorrectly halved the minimum chunk size. Now only applies reduction to the largest chunks to ensure a sufficient number of objects are fetched per operation.
  ↳ [#66236](https://github.com/ceph/ceph/pull/66236): [74c62e1](https://github.com/ceph/ceph/commit/74c62e12008943dcbd4aa8588e5b2d3052c18d79)
- Fixed the problem of inaccurate statistics of statfs in mixed quota scenarios. It now supports searching the quota root directory for the number of files and bytes separately to correctly inherit the missing quota value of the parent directory.
  ↳ [#66473](https://github.com/ceph/ceph/pull/66473): [8c05924](https://github.com/ceph/ceph/commit/8c05924f5430038e1c9b9cfe28252b4155fb5a5a), [ac059b1](https://github.com/ceph/ceph/commit/ac059b127094f6120d1c68995bfe01375dfcfa44) | [#65133](https://github.com/ceph/ceph/pull/65133): [398073d](https://github.com/ceph/ceph/commit/398073d8a784d8ca2d40f524ed97163c08e86f74)
- Fixed the issue where mirror synchronization failed due to the existence of unfinished downgraded snapshots after the rbd-mirror daemon was restarted.
  ↳ [#66165](https://github.com/ceph/ceph/pull/66165): [e768f9f](https://github.com/ceph/ceph/commit/e768f9f441d8522660b53964496b0e8b6fe5ca55)
- Fixed the issue where the radosgw-admin object unlink command could not correctly remove objects due to incorrect calculation of the number of shards when processing unsharded bucket indexes.
  ↳ [#66152](https://github.com/ceph/ceph/pull/66152): [938a759](https://github.com/ceph/ceph/commit/938a759fdf0c37e29ff9a5241f169be3a95841f0)
- Fixed an issue where HealthMonitor falsely reported a MON_DOWN warning when the newly added Monitor had not yet joined the quorum, and avoided such a situation by introducing a reasonable grace period.
  ↳ [#67324](https://github.com/ceph/ceph/pull/67324): [0001004](https://github.com/ceph/ceph/commit/0001004e3abc01881e0300c458e61c66ac2af2f7)
- Fix backward compatibility issues when MonMap dumps, ensuring that the addr field only outputs traditional string format.
  ↳ [#68323](https://github.com/ceph/ceph/pull/68323): [1f2600e](https://github.com/ceph/ceph/commit/1f2600e261dd9c015e84c3ddea5fa4fefcd01389)
- Fixed the issue where librbd incorrectly returns the request blocked code when the exclusive lock is not in the locked state, thus avoiding the failure of maintenance operations due to false positives of duplicate lock owners.
  ↳ [#66627](https://github.com/ceph/ceph/pull/66627): [bf83e6b](https://github.com/ceph/ceph/commit/bf83e6b049950d6288e7f470233e6de1c1c909b6)
- Fixed the defect of missing empty data buffer in OSD response when the sparse read result is empty, ensuring that the client can receive the complete reply format as expected.
  ↳ [#67356](https://github.com/ceph/ceph/pull/67356): [2dc0f00](https://github.com/ceph/ceph/commit/2dc0f00a9202335cf44bd83c7a704c422b8f4383)
- Fixed the reserved_size memory leak problem in the RGW notification module caused by not deducting the entry overhead, and ensure that the occupied space is released correctly when the reserved resources are submitted, aborted or expired to clean up.
  ↳ [#67575](https://github.com/ceph/ceph/pull/67575): [b97fe16](https://github.com/ceph/ceph/commit/b97fe168f62274de043b4c15a01d5530760ef159)
- Fixed the queue space leakage problem in the RGW notification module caused by reservation size calculation deviation, and introduced a one-time self-healing mechanism to recalibrate the reservation value when submitting or aborting to avoid false positives of ENOSPC errors.
  ↳ [#67575](https://github.com/ceph/ceph/pull/67575): [8f86e09](https://github.com/ceph/ceph/commit/8f86e0926f4aaf49786f8b35e9b4e478a24a9b73)
- Fixed the debug output operator of WriteLogOperationSet in the librbd cache module, and removed the printing of uninitialized pointer cells to avoid outputting garbage data.
  ↳ [#67704](https://github.com/ceph/ceph/pull/67704): [d2b0311](https://github.com/ceph/ceph/commit/d2b03116f137dfdd49e8805ee046483689138407)
- Fixed the issue in the librbd mirroring module where UnlinkPeerRequest incorrectly returns EINVAL instead of ENOENT when encountering a discarded snapshot in a concurrent scenario, to avoid causing ImageReplayer to stop unexpectedly.
  ↳ [#67582](https://github.com/ceph/ceph/pull/67582): [3101554](https://github.com/ceph/ceph/commit/31015544fb0cf29781e5bede126564ff655334f7)
- Fixed a race condition in librbd caused by premature completion of ImageUpdateWatchers::shut_down() during image shutdown, avoiding potential use-after-free and segfaults.
  ↳ [#67580](https://github.com/ceph/ceph/pull/67580): [151ff1e](https://github.com/ceph/ceph/commit/151ff1e3e1a9c7d28080ba769fec2302e15f0c14)
- Fixed an issue where the monmaptool tool did not correctly apply the set properties when adding addresses.
  ↳ [#62061](https://github.com/ceph/ceph/pull/62061): [a7a1713](https://github.com/ceph/ceph/commit/a7a171368a3656d118a9c634cb5bb04e3c2601db)
- Fix the problem that may be caused by explicitly releasing the request reference when MgrOpRequest is destroyed.
  ↳ [#65006](https://github.com/ceph/ceph/pull/65006): [9e2281b](https://github.com/ceph/ceph/commit/9e2281b73d7222e9b38b22ff3d7c9f3d67a8afae)
- Fixed an issue where the CephFS client incorrectly checks the file size when the inode lacks Fc capability, causing read requests to return empty data.
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [3c52305](https://github.com/ceph/ceph/commit/3c52305b02fa75b6902a5a1f1e8de30b2363dda1)
- Fixed a divide-by-zero crash caused by RGW calculating the maximum number of objects per shard to zero when processing versioned buckets in debugging scenarios.
  ↳ [#63567](https://github.com/ceph/ceph/pull/63567): [eb28b98](https://github.com/ceph/ceph/commit/eb28b986907475bbc7a76908a6e155c116d06762)
- Fix client crash caused by repeatedly decrementing request reference count in asynchronous fsync execution context.
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [238d1f9](https://github.com/ceph/ceph/commit/238d1f9cec569b3d35627adf11e962a83d42c8e1)
- Fixed an issue where OSDMonitor did not notify the forwarding monitor of discard status when ignoring OSD alive messages.
  ↳ [#64509](https://github.com/ceph/ceph/pull/64509): [5e0984c](https://github.com/ceph/ceph/commit/5e0984c6c5377aa068ac269e5a6201b8ad2f5570)
- Fixed the ceph-objectstore-tool tool to recognize the get-attr operation as a read-only operation.
  ↳ [#66538](https://github.com/ceph/ceph/pull/66538): [e5272b6](https://github.com/ceph/ceph/commit/e5272b6db68c4aa45f537914ef5f98e075090b2d)
- MDS adds event markers when creating batch request headers to facilitate debugging slow request or deadlock issues.
  ↳ [#65279](https://github.com/ceph/ceph/pull/65279): [8ed9f3b](https://github.com/ceph/ceph/commit/8ed9f3b3c76f021fbdc958f0f7f78ae987af8098)
- Fixed the issue where next_snap information is missing from the log when MDS detects directory entry damage.
  ↳ [#61977](https://github.com/ceph/ceph/pull/61977): [a14ba29](https://github.com/ceph/ceph/commit/a14ba290ef637d896a140358dc51946d86abb6ab)
- Fix signed comparison warning in client code.
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [b141469](https://github.com/ceph/ceph/commit/b14146994504c000f70be921f6843eba06982e3d)
- Fixed a format error caused by missing spaces in the output information when executing the ceph mgr module force disable command.
  ↳ [#64686](https://github.com/ceph/ceph/pull/64686): [6ffe765](https://github.com/ceph/ceph/commit/6ffe765a9a470b7c01034fd049e50e5df113ae1f)
- Fix the log description when ImageWatcher handles lock request notification in librbd.
  ↳ [#67278](https://github.com/ceph/ceph/pull/67278): [1c4f472](https://github.com/ceph/ceph/commit/1c4f472aaf44b9a2e06b4b6f0bfb0678d982b52b)
- Improved the usage prompt information of ceph-fuse and added the --client_fs option description.
  ↳ [#61274](https://github.com/ceph/ceph/pull/61274): [add5ec7](https://github.com/ceph/ceph/commit/add5ec7cb9d318e10b517c04e4a73f939b84edc8)

### Refactoring optimization
- Move the client lock acquisition logic out of the statfs auxiliary method, and directly lock it in the ll_statfs method to simplify the calling process.
  ↳ [#65133](https://github.com/ceph/ceph/pull/65133): [a4f4bb7](https://github.com/ceph/ceph/commit/a4f4bb7d854ed8b9111d562d683fe6cdbfcef8ae)
- Removed superseded dead code methods in MDS module.
  ↳ [#61300](https://github.com/ceph/ceph/pull/61300): [590b713](https://github.com/ceph/ceph/commit/590b71326eb0020c49cfbb1affbcf4e81cb40757)
- Correct test instance generation logic to ensure valid dirfrag fragment is created for MDSCacheObjectInfo.
  ↳ [#66541](https://github.com/ceph/ceph/pull/66541): [abd1e2e](https://github.com/ceph/ceph/commit/abd1e2ed152530691cca6c7c4e1aa86648a7e0e7)
- Rename volume level name in RocksDBBlueFSVolumeSelector debug output and increase display level.
  ↳ [#66838](https://github.com/ceph/ceph/pull/66838): [f1259eb](https://github.com/ceph/ceph/commit/f1259ebbfefb453b4d8e2e4dca49bb41be767d32)
- Clean up IoCtx usage in librbd Group.cc, correct internal type to librados::IoCtx.
  ↳ [#64621](https://github.com/ceph/ceph/pull/64621): [13be62d](https://github.com/ceph/ceph/commit/13be62d2b1ef469939bbf6a7f3664ee7e4ffcbdb)
- Simplify the printing logic of frag_t and use modern formatting tools instead of bit operation loops.
  ↳ [#66541](https://github.com/ceph/ceph/pull/66541): [d81b4c4](https://github.com/ceph/ceph/commit/d81b4c457483e0dc19723aab37719b4958c42e17)

### Test related
- Added support verification for ceph_chownat() using empty pathnames with the AT_EMPTY_PATH flag in tests.
  ↳ [#61166](https://github.com/ceph/ceph/pull/61166): [098403c](https://github.com/ceph/ceph/commit/098403c50dffc98d6b52ff6e8a7f2576944b449d)
- Added ll_walk use case in client test to verify behavior under current working directory and root path.
  ↳ [#62499](https://github.com/ceph/ceph/pull/62499): [0368f38](https://github.com/ceph/ceph/commit/0368f3842aa4040f5f9a8994b1b735ead5fc15f1)
- Added a new use case in the libcephfs test to verify whether hangs will occur after uninstalling using high-level and low-level APIs for search operations.
  ↳ [#65289](https://github.com/ceph/ceph/pull/65289): [6c2d594](https://github.com/ceph/ceph/commit/6c2d594b3547297eff509793f487c863e0d82823)
- Added unit test for volume selector for Bluestore component.
  ↳ [#66838](https://github.com/ceph/ceph/pull/66838): [01f9a87](https://github.com/ceph/ceph/commit/01f9a8735ab1acb6d852070ee59f378b5d4a98a1)
- Added io_callback auxiliary function in libcephfs test to support multi-client file reading and writing extended writing test scenarios.
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [be1fc54](https://github.com/ceph/ceph/commit/be1fc54b93cd76676e95f591f6e3f5ef1e642d5b)
- Removed unit tests related to deprecated cache tiering functionality.
  ↳ [#64589](https://github.com/ceph/ceph/pull/64589): [f29d750](https://github.com/ceph/ceph/commit/f29d75045d5e238a3c7739a3bba23c1463663d6b)
- Fixed a race condition in the rbd-mirror test case ResyncRequestedRemoteNotPrimary, by adjusting the number of notification waits to ensure that the mirror replayer correctly enters the completion state.
  ↳ [#64739](https://github.com/ceph/ceph/pull/64739): [6ee6ab7](https://github.com/ceph/ceph/commit/6ee6ab764ebcdc1c695c41c8c2d04d7b5574049b)
- Add test cases for cephfs SingletonClient to verify whether the monmap and configuration subscription status are correct.
  ↳ [#66471](https://github.com/ceph/ceph/pull/66471): [dd37ff4](https://github.com/ceph/ceph/commit/dd37ff462102cb0b573e8828d7295916756cfac2)
- Add SnapdiffDeletionRecreation use case to the LibCephFS test suite to reproduce failure scenarios related to snapshot differences, and adjust the data size parameters of this test.
  ↳ [#65363](https://github.com/ceph/ceph/pull/65363): [67986ff](https://github.com/ceph/ceph/commit/67986ffe9919b0483ae914697e8ae8906832843c)
- Fixed the failure of libcephsqlite test due to json_tree syntax compatibility issue in some SQLite versions, and changed related queries to use json_extract implementation.
  ↳ [#67322](https://github.com/ceph/ceph/pull/67322): [be173db](https://github.com/ceph/ceph/commit/be173dbe0f1e9e7d77e0b8bc893a40f4d1203d72)

### Performance optimization
- Optimize the performance of RGW batch deletion of objects and improve efficiency by skipping redundant OLH updates.
  ↳ [#65500](https://github.com/ceph/ceph/pull/65500): [064d45f](https://github.com/ceph/ceph/commit/064d45f229c1915dfd413f74394821ea8fe53c9d)
- Fixed the problem of BlueFS incorrectly reporting the bytes_written_slow performance counter as 0 in asynchronous I/O scenarios to ensure accurate performance indicator statistics.
  ↳ [#66354](https://github.com/ceph/ceph/pull/66354): [255db43](https://github.com/ceph/ceph/commit/255db43988828131cc616552a772ac542d430671)
- Add path depth information to the MDS path traversal debug log to assist in troubleshooting issues such as lock acquisition.
  ↳ [#65279](https://github.com/ceph/ceph/pull/65279): [761eb16](https://github.com/ceph/ceph/commit/761eb16125a795a445f115c24741364c741f29f2)

### Security related
- No significant changes.

### Documentation
- Fixed formatting and spelling errors in the ceph-conf.rst document, unified chapter title case, corrected hyperlinks, and adjusted sample code blocks to INI format and use a privileged command prompt.
  ↳ [#64287](https://github.com/ceph/ceph/pull/64287): [6b2d454](https://github.com/ceph/ceph/commit/6b2d454f08a5ab467d7888a4ff5d68fa6ec03df6) | [#64785](https://github.com/ceph/ceph/pull/64785): [9cb16d1](https://github.com/ceph/ceph/commit/9cb16d1e27bafc00cd6a2f54ae447838f71d2d5d) | [#64852](https://github.com/ceph/ceph/pull/64852): [5295153](https://github.com/ceph/ceph/commit/5295153f56e9eea694dee6858d80b4b0f12dc0d5) | [#64871](https://github.com/ceph/ceph/pull/64871): [09b3a54](https://github.com/ceph/ceph/commit/09b3a54bdac4e29ceeb9715c440ed29af1bec354) | [#64878](https://github.com/ceph/ceph/pull/64878): [87506fe](https://github.com/ceph/ceph/commit/87506fe718529314ccbbd362065ef10c7cf337e1)
- Improved the presentation format of operating system recommendations in the CephFS and RBD Windows client documentation, changing it to a note alert box to enhance visibility.
  ↳ [#64492](https://github.com/ceph/ceph/pull/64492): [1774e12](https://github.com/ceph/ceph/commit/1774e1228f229639049a3d313a9034a9ddb0e70e) | [#64481](https://github.com/ceph/ceph/pull/64481): [0fa1403](https://github.com/ceph/ceph/commit/0fa14036c57a6194f67d26a34ea0c51f0035ddca)
- A new basic_stretch_cluster collection entry has been added to the Telemetry document to record information related to the Stretch cluster deployment mode.
  ↳ [#66389](https://github.com/ceph/ceph/pull/66389): [b62a229](https://github.com/ceph/ceph/commit/b62a22912459e76a466526d3c3266d1a3122b21f)
- Updated the description of the configuration item mon_warn_pg_not_scrubbed_ratio to clarify that it needs to be set in the Manager or global scope, and added specific configuration command instructions.
  ↳ [#62551](https://github.com/ceph/ceph/pull/62551): [6a2288d](https://github.com/ceph/ceph/commit/6a2288da7e4aaa915b7ca1d0adf189c47c0f9b4e)
- Added instructions to obtain the absolute path of a subvolume snapshot using the ceph fs subvolume snapshot getpath command in the CephFS documentation.
  ↳ [#62918](https://github.com/ceph/ceph/pull/62918): [e0fc650](https://github.com/ceph/ceph/commit/e0fc650527f5294b92a57d9fa4b303fa1255ea0d)
- Updated the RadosGW documentation, added the description of the x-amz-delete-if-unmodified-since request header in the S3 object deletion operation, and corrected the description and format of the NFS-related documentation.
  ↳ [#64315](https://github.com/ceph/ceph/pull/64315): [5d090e4](https://github.com/ceph/ceph/commit/5d090e4c08318a48c1627c52d4d5f925f5fc4a0d)
- Added note in CephFS documentation: The subvolume pool namespace format has been updated after Tentacle version to avoid naming conflicts for subvolumes with the same name in different subvolume groups.
  ↳ [#64205](https://github.com/ceph/ceph/pull/64205): [0b287c6](https://github.com/ceph/ceph/commit/0b287c615cc4e834529afb48905dec46631d31e4)
- Updated the CephFS documentation to explain that the output of the subvolume information command adds a source field in the cloning scenario to display the source snapshot and related location information.
  ↳ [#64652](https://github.com/ceph/ceph/pull/64652): [c40eb13](https://github.com/ceph/ceph/commit/c40eb13f96f4af9ea9676af429f963bde9cb7516)
- Updated the mgr telemetry module documentation, optimized the description of enabling telemetry, time-consuming and privacy protection for generating sample reports, and clarified that smartmontools 7.0 or higher is required to generate device reports.
  ↳ [#63809](https://github.com/ceph/ceph/pull/63809): [604a35e](https://github.com/ceph/ceph/commit/604a35eab415c0a9f46dc8de10c2d818f624e678)
- Updated the RADOSGW documentation to clarify the description of rgw-multitenancy behavior, indicating that buckets and users with the same name can be used under different tenants.
  ↳ [#63812](https://github.com/ceph/ceph/pull/63812): [3886e1a](https://github.com/ceph/ceph/commit/3886e1afe05b26a9bd2cc2e54cae778fc516a749)
- Updated RADOS operational documentation to include instructions on deprecating deployment of new cache layers and recommending migration from older deployments.
  ↳ [#64496](https://github.com/ceph/ceph/pull/64496): [17cf0e5](https://github.com/ceph/ceph/commit/17cf0e5e7cc4367e7d492bc365ce57df9ed1fa51)
- Updated the Rados configuration document, supplemented the purpose of the ceph config show-with-defaults command, and clarified that ceph-conf --show-config is a legacy command.
  ↳ [#65206](https://github.com/ceph/ceph/pull/65206): [fba129e](https://github.com/ceph/ceph/commit/fba129ef5fdaedc2b1ed95a676f099ea0ae9a7a6)
- Added a definition document for ceph-mgr module configuration options, detailing supported attributes, types and usage examples to guide developers to correctly configure module options.
  ↳ [#64396](https://github.com/ceph/ceph/pull/64396): [7f72851](https://github.com/ceph/ceph/commit/7f72851196551ac128263100391b8b4671ed60ff)
- Updated the developer documentation, supplemented the guidance on using the :confval: directive to record configuration options, and clarified the naming convention and cross-reference method of general options and mgr module options.
  ↳ [#64166](https://github.com/ceph/ceph/pull/64166): [bdfcf7c](https://github.com/ceph/ceph/commit/bdfcf7cfc52a70a7a077fc823a3f91e60c71e31c)
- Update the crash module documentation to remove outdated manual enable instructions and clarify that the module is permanently enabled and cannot be disabled.
  ↳ [#64284](https://github.com/ceph/ceph/pull/64284): [bf4a607](https://github.com/ceph/ceph/commit/bf4a6071f898f76860dfde81708217d48392dec1)
- Added caps recovery command instructions to the Rados operation documentation to guide users on how to repair client.admin permissions after they are accidentally deleted.
  ↳ [#64321](https://github.com/ceph/ceph/pull/64321): [2cf30ed](https://github.com/ceph/ceph/commit/2cf30ed99843f6a9fdb540206a2a2625279b754b)
- Added descriptions of rgw_enable_lc_threads and rgw_enable_gc_threads configuration items in the RadosGW configuration reference document, clarifying that at least one life cycle and garbage collection maintenance thread must be enabled in each region.
  ↳ [#64338](https://github.com/ceph/ceph/pull/64338): [8a349c2](https://github.com/ceph/ceph/commit/8a349c234896494b425c2830792a2cf9ce984c46)
- Removed the deprecated clonedata command and its description from the rados man page.
  ↳ [#64393](https://github.com/ceph/ceph/pull/64393): [97a0268](https://github.com/ceph/ceph/commit/97a02680ff32400f4510a10d4ee38b5e323489d2)
- Updated mgr module documentation to indicate that modules need to explicitly declare the NOTIFY_TYPES list to receive notifications of specific types.
  ↳ [#64530](https://github.com/ceph/ceph/pull/64530): [29f00a1](https://github.com/ceph/ceph/commit/29f00a18368989ee945016b6212b109f3b6ab970)
- Updated the CephFS FUSE mounting documentation, improved the description of passing the Monitor address, mounting specific directories and multiple file system scenarios, and improved the tips to ensure that no process occupies the file system before unmounting.
  ↳ [#64472](https://github.com/ceph/ceph/pull/64472): [1038d80](https://github.com/ceph/ceph/commit/1038d80a83b7d42c90d7fc225f1657f513be38b7)
- Updated the CephFS disaster recovery documentation to clarify the behavior when the data pool is damaged, how to identify files, and added notes and known limitations on the use of metadata repair tools.
  ↳ [#64608](https://github.com/ceph/ceph/pull/64608): [06fde93](https://github.com/ceph/ceph/commit/06fde9378a881e2d118d7fe1292aeb78da334d91) | [#64644](https://github.com/ceph/ceph/pull/64644): [f235c29](https://github.com/ceph/ceph/commit/f235c29f8f0e77156a4b432104f9c51a3fd66171) | [#65057](https://github.com/ceph/ceph/pull/65057): [f07ad87](https://github.com/ceph/ceph/commit/f07ad872547f323cfb93fd8dc602ec7e0fd10fbd)
- Fixed the wording of the description of the bucket lifecycle handling mechanism in the RadosGW configuration reference document.
  ↳ [#64647](https://github.com/ceph/ceph/pull/64647): [965a161](https://github.com/ceph/ceph/commit/965a1610f3738eb0e1ee9167b0b7f03467e9b082)
- Optimized the CephFS ceph-dokan document, improved the Windows mount command description, parameter explanation and uninstall operation instructions.
  ↳ [#64735](https://github.com/ceph/ceph/pull/64735): [206c67f](https://github.com/ceph/ceph/commit/206c67f67061c20f027eb822d30c47fba364f2a0) | [#64759](https://github.com/ceph/ceph/pull/64759): [4e76827](https://github.com/ceph/ceph/commit/4e7682761998f201390ca96dd8b2d249401c32a7)
- Updated the mount.ceph man page to clarify the mechanism and default status of dirstat and nodirstat options.
  ↳ [#65183](https://github.com/ceph/ceph/pull/65183): [ae881ba](https://github.com/ceph/ceph/commit/ae881bae11227029bddda996fc62b3519b243596)
- Added version compatibility note to Rados erasure coding documentation, warning against adding specific sections to older versions of the documentation.
  ↳ [#64867](https://github.com/ceph/ceph/pull/64867): [a51662d](https://github.com/ceph/ceph/commit/a51662dff9b736b0896925d8036f70cb04341e54)
- Comprehensively updated and optimized the CephFS troubleshooting documentation, improving the descriptions of multiple chapters, problem locating steps and command instructions.
  ↳ [#64903](https://github.com/ceph/ceph/pull/64903): [3955a19](https://github.com/ceph/ceph/commit/3955a19281124d705a61d37bf35c987f3bf1fa8d) | [#64900](https://github.com/ceph/ceph/pull/64900): [1e66c84](https://github.com/ceph/ceph/commit/1e66c84cc79eb184f51b90784d71e3311a9cdae7) | [#65087](https://github.com/ceph/ceph/pull/65087): [88d99ba](https://github.com/ceph/ceph/commit/88d99ba1691241343bf0c49d263457ed82a14302) | [#65036](https://github.com/ceph/ceph/pull/65036): [77ff5a3](https://github.com/ceph/ceph/commit/77ff5a37248ad3326e40d9fd04b71464eb6d973d) | [#65040](https://github.com/ceph/ceph/pull/65040): [54236c4](https://github.com/ceph/ceph/commit/54236c45742c104a1ab7b639c73e3fa10ea5a468) | [#65090](https://github.com/ceph/ceph/pull/65090): [e5f197f](https://github.com/ceph/ceph/commit/e5f197fc06b69412e94ee0d956aaffad9ee1a757) | [#65125](https://github.com/ceph/ceph/pull/65125): [6e34c7d](https://github.com/ceph/ceph/commit/6e34c7d50494939af9949cba124bc72395f753e3) | [#65043](https://github.com/ceph/ceph/pull/65043): [349fabe](https://github.com/ceph/ceph/commit/349fabe0b008326ccc973dfba2af58e836e66ffe) | [#65093](https://github.com/ceph/ceph/pull/65093): [d6e1b39](https://github.com/ceph/ceph/commit/d6e1b3927525c1fac6fc761427218429add8f12f) | [#65077](https://github.com/ceph/ceph/pull/65077): [4f2c86d](https://github.com/ceph/ceph/commit/4f2c86db59be9dd2b879983e453db057ab728b6c) | [#65096](https://github.com/ceph/ceph/pull/65096): [21ba1a3](https://github.com/ceph/ceph/commit/21ba1a34d2630aa2aff8e273587c123d11bfb035)
- Fixed parsing issue due to PromQL syntax error in Grafana host overview dashboard.
  ↳ [#64884](https://github.com/ceph/ceph/pull/64884): [8f4f055](https://github.com/ceph/ceph/commit/8f4f055e30a02c29c9867714f7694cd6ccdfd7de)
- Updated the CephFS troubleshooting document, corrected many error descriptions, and added the debugging and mounting chapters.
  ↳ [#65046](https://github.com/ceph/ceph/pull/65046): [e6e9686](https://github.com/ceph/ceph/commit/e6e9686fa118844d22fa466f7c043c44d7170b19) | [#65025](https://github.com/ceph/ceph/pull/65025): [56ffdf8](https://github.com/ceph/ceph/commit/56ffdf8b6a346035df2d6b427ab56339dcca03ff) | [#65122](https://github.com/ceph/ceph/pull/65122): [d49d7bc](https://github.com/ceph/ceph/commit/d49d7bc20406950c0b4bfb3f10f66dada04af0b6) | [#65379](https://github.com/ceph/ceph/pull/65379): [4170504](https://github.com/ceph/ceph/commit/41705043d7b85f86711b040bb74d7cd9baa1564c)
- Updated Crimson development documentation, clarified CPU allocation instructions and restructured the object storage backend chapter.
  ↳ [#65311](https://github.com/ceph/ceph/pull/65311): [05a9dbf](https://github.com/ceph/ceph/commit/05a9dbfa6fbf10fd49412647298af0af497da6a1)
- Updated CephFS quota documentation to clarify client permission requirements and fix broken links.
  ↳ [#65082](https://github.com/ceph/ceph/pull/65082): [9214c09](https://github.com/ceph/ceph/commit/9214c0921d741c4e98646f85fef0b40874949cc0)
- Fixed the format problem of rados configuration document, and added NVMe-oF related configuration items.
  ↳ [#65137](https://github.com/ceph/ceph/pull/65137): [a17d51e](https://github.com/ceph/ceph/commit/a17d51e0fb8d04de4f54c63a8ea85e852e4b0273)
- Updated the development document blkin.rst, adding instructions for installing the development packages required for LTTng tracking when deploying based on packages.
  ↳ [#65211](https://github.com/ceph/ceph/pull/65211): [b83b38c](https://github.com/ceph/ceph/commit/b83b38cb286ebbab1f1178a2bbecb2d35b24d04d)
- Fixed the calculation expression and metric display of the number of OSDs in the Ceph cluster advanced Grafana panel.
  ↳ [#65671](https://github.com/ceph/ceph/pull/65671): [2943914](https://github.com/ceph/ceph/commit/2943914a0dc4abae52e18fb4776046d15ba98651)
- Removed cloud-restore related documentation from RADOSGW documentation.
  ↳ [#65639](https://github.com/ceph/ceph/pull/65639): [a547648](https://github.com/ceph/ceph/commit/a547648245c7de6a237c61ff8c50922add159a04)
- Fixed the filtering logic of charts in the RGW Sync Overview Grafana dashboard.
  ↳ [#66990](https://github.com/ceph/ceph/pull/66990): [6a410da](https://github.com/ceph/ceph/commit/6a410dab6e99eec8ee8061d9313f07d9482761f9)
- Removed documentation for Dashboard OAuth2 SSO and corrected single sign-on instructions to only cover SAML 2.0.
  ↳ [#66797](https://github.com/ceph/ceph/pull/66797): [a4c1945](https://github.com/ceph/ceph/commit/a4c1945802d9189455f94c546ce9c1347b7c8547)
- Updated cephadm RGW service documentation, removing instructions that only apply to Tentacle versions to match Squid versions.
  ↳ [#66970](https://github.com/ceph/ceph/pull/66970): [a295b6a](https://github.com/ceph/ceph/commit/a295b6aefe717fdc87903d4eeb876ec90607ad1e)

### Build/CI
- Upgraded Dashboard's cheroot dependency version.
  ↳ [#65636](https://github.com/ceph/ceph/pull/65636): [cd6930e](https://github.com/ceph/ceph/commit/cd6930e94dbcbcfba272f55a9a2b0c0ee444e902)
- Removed lxml version locking in Dashboard dependency configuration to fix test failures.
  ↳ [#64613](https://github.com/ceph/ceph/pull/64613): [aa9638d](https://github.com/ceph/ceph/commit/aa9638db65ac6fc9fcccedeeb05726baadeac57e)
- The typed-ast dependency that has been discontinued has been removed from the document build configuration and the Python standard library module is used instead.
  ↳ [#64399](https://github.com/ceph/ceph/pull/64399): [4f784c8](https://github.com/ceph/ceph/commit/4f784c84652e5e5497d24b28ff4a1e67d7885556)
- Unlocked the version lock of grpcio and grpcio-tools dependencies in Dashboard.
  ↳ [#64613](https://github.com/ceph/ceph/pull/64613): [034982b](https://github.com/ceph/ceph/commit/034982b6b2be6d415ffc1c7b127d064d60d0ea33)
- Added missing runtime flags for related options in mon.yaml.in configuration file.
  ↳ [#67324](https://github.com/ceph/ceph/pull/67324): [841e728](https://github.com/ceph/ceph/commit/841e7282ade94274b9e03fd34c03ee80ef4d1daf)
- Switched the dependency of RGW bucket notification test from nose-py3 to pynose.
  ↳ [#67450](https://github.com/ceph/ceph/pull/67450): [c8eb7d9](https://github.com/ceph/ceph/commit/c8eb7d921cf5700a3e85bd1d335bdd885a8c92d2)
- Disabled automatic registration of unittest_deferred in Bluestore test build configuration.
  ↳ [#66357](https://github.com/ceph/ceph/pull/66357): [c504c85](https://github.com/ceph/ceph/commit/c504c85c0d704c423d3ee28f559b941e0af6f5ee)
- Removed dependency on libcephfs for client tests in test build configuration.
  ↳ [#63720](https://github.com/ceph/ceph/pull/63720): [808f538](https://github.com/ceph/ceph/commit/808f53885e21c3a81415248647cdb215580c3557)
- Fixed the build failure issue of some libcephfs test programs on Ubuntu 22.04 due to linker errors.
  ↳ [#63720](https://github.com/ceph/ceph/pull/63720): [b1068d1](https://github.com/ceph/ceph/commit/b1068d1f751023f39b6453604f6efec9d8851c2f)
- Adjusted the build configuration of the file system test and optimized the link dependencies of the executable file.
  ↳ [#63720](https://github.com/ceph/ceph/pull/63720): [08e9789](https://github.com/ceph/ceph/commit/08e97895769c7722f61167fd459f0bf6547ed890)
- Adjusted the build configuration of the unittest_fault_injector test to address initialization issues with death tests.
  ↳ [#63981](https://github.com/ceph/ceph/pull/63981): [2b881df](https://github.com/ceph/ceph/commit/2b881dfcf07ad23631f60c9d3ad702517464135f)
- Fixed cheroot version in the required dependency list of pybind/mgr to resolve compatibility issues.
  ↳ [#65636](https://github.com/ceph/ceph/pull/65636): [1484aa4](https://github.com/ceph/ceph/commit/1484aa4fe56d9fd545c0c96bd7fddf66c807fe74)
- Removed the no longer maintained and incompatible sphinxcontrib-seqdiag package from the documentation build configuration.
  ↳ [#67501](https://github.com/ceph/ceph/pull/67501): [fa0e7b5](https://github.com/ceph/ceph/commit/fa0e7b5bd4aaa109bcad33698e06e604907314b7)
- Upgraded Grafana version and fixed multiple monitoring dashboard configurations to be compatible with the new version.
  ↳ [#66964](https://github.com/ceph/ceph/pull/66964): [6ffb53d](https://github.com/ceph/ceph/commit/6ffb53df5de37de5ee6cf6a1b8991e10dcc2a075)
- Updated the project version number and added the corresponding Debian release change record.
  ↳ [#69139](https://github.com/ceph/ceph/pull/69139): [7cc0193](https://github.com/ceph/ceph/commit/7cc0193a616a3333d22b7762037fa5b73a4d06a6)

### Maintenance
- No significant changes.

### Others
- Fixed the error message when acquiring exclusive lock fails in librbd.
  ↳ [#67278](https://github.com/ceph/ceph/pull/67278): [8e4b033](https://github.com/ceph/ceph/commit/8e4b033b15760740649f0956ffb4a54aa377ccff)
- Updated CephFS mirror documentation and added instructions for using the ceph fs snapshot mirror ls command.
  ↳ [#60177](https://github.com/ceph/ceph/pull/60177): [9337255](https://github.com/ceph/ceph/commit/9337255bacf6c8251c2e8d06db3b82710dcf2bdc)
- Updated CephFS management documentation to indicate that modifying the max_mds setting when the cluster is unhealthy must add a confirmation flag.
  ↳ [#60398](https://github.com/ceph/ceph/pull/60398): [90632e5](https://github.com/ceph/ceph/commit/90632e50b976b0d371b85819f9e9341fc63be83e)
- Fixed the problem of test failure in client non-blocking test due to buffer list not being cleared.
  ↳ [#64090](https://github.com/ceph/ceph/pull/64090): [9ca11c6](https://github.com/ceph/ceph/commit/9ca11c61097e5bac2ca8448c5d1e4fab8c3f75fa)
- Fixed typo in mgr_osd_messages configuration item name.
  ↳ [#63344](https://github.com/ceph/ceph/pull/63344): [c5dbd53](https://github.com/ceph/ceph/commit/c5dbd538d8243569a9e974674066e42b4ff8c25a)
- Fixed a typo in the description of the BlueStore slow operation warning threshold in the global.yaml.in configuration file.
  ↳ [#64217](https://github.com/ceph/ceph/pull/64217): [8bd12a1](https://github.com/ceph/ceph/commit/8bd12a11c974ec2ba493e4c375591122cf41b0d9)
- Optimize the RGW cache document, improve expression, correct punctuation and formatting errors, and adjust the display of chapter levels and command line examples.
  ↳ [#64475](https://github.com/ceph/ceph/pull/64475): [b231956](https://github.com/ceph/ceph/commit/b2319567a4e56e6ce28a0ba8d17cb488146c2021)
- Update the description of the mgr_data option in the mgr.yaml.in configuration file to make it more generic.
  ↳ [#63764](https://github.com/ceph/ceph/pull/63764): [57b8f73](https://github.com/ceph/ceph/commit/57b8f73668018c04bf1b07c9fc99abac5c695df7)
- Updated the installation documentation to correct the SSH key path description from hardcoded /home/<user> to the generic ~<user>.
  ↳ [#64605](https://github.com/ceph/ceph/pull/64605): [ed92bef](https://github.com/ceph/ceph/commit/ed92bef1d3dfea92fa3d60269a02620bef0753c4)
- Update mgr telemetry module documentation, correct some expressions and unify terminology.
  ↳ [#64343](https://github.com/ceph/ceph/pull/64343): [15f9d3b](https://github.com/ceph/ceph/commit/15f9d3b9304ad6ef342dd5c9488caef6344e1113)
- Fixed typos in the document, changing "communicate" to "communicate".
  ↳ [#64147](https://github.com/ceph/ceph/pull/64147): [909b22e](https://github.com/ceph/ceph/commit/909b22e521b4adfba042b62a7329e0db9e0dcf7a)
- Fixed typos in the documentation about the balancer operation example command, and added the missing mgr parameter.
  ↳ [#65550](https://github.com/ceph/ceph/pull/65550): [7ebcb1a](https://github.com/ceph/ceph/commit/7ebcb1a4b27913a652906f7d6e547f0364225e67)
- Fixed the problem that inline literals were not terminated correctly due to missing spaces in the ceph-conf.rst document, and eliminated Sphinx build warnings.
  ↳ [#64170](https://github.com/ceph/ceph/pull/64170): [9855af3](https://github.com/ceph/ceph/commit/9855af384846ce8827e3291e00e6f381cc87e919)
- Corrected wording and grammatical errors in the "Life Cycle Settings" chapter in the RadosGW configuration reference document, and optimized related expressions.
  ↳ [#64547](https://github.com/ceph/ceph/pull/64547): [2e41400](https://github.com/ceph/ceph/commit/2e414002a6a998ee01b80468a8a3a2e093b39a9d)
- Fix link format to mClock configuration reference in documentation.
  ↳ [#64752](https://github.com/ceph/ceph/pull/64752): [012e4e1](https://github.com/ceph/ceph/commit/012e4e1ebd3808c96c8de2493121a6b38f3d9585)
- Adjust the position of the Slow requests (MDS) chapter in the CephFS troubleshooting document to comply with the recommended troubleshooting order.
  ↳ [#65202](https://github.com/ceph/ceph/pull/65202): [a2b6e55](https://github.com/ceph/ceph/commit/a2b6e5573c67029a7a47b72ef96f61425f38928a)
- Update the health check instructions in the RADOS operation documentation, improve the description and unify the presentation format of command examples.
  ↳ [#65238](https://github.com/ceph/ceph/pull/65238): [d7b1a35](https://github.com/ceph/ceph/commit/d7b1a35cbaa78efb636773a1249dc36f53a92c23)
- Fixed compilation issues caused by spelling errors in the RGW Asio front-end, and corrected the calling name of the atomic loading function.
  ↳ [#66289](https://github.com/ceph/ceph/pull/66289): [aeff969](https://github.com/ceph/ceph/commit/aeff969fcb9d019e765ed7e582e5396b20c66f82)
- Fixed typo in radosgw frontend documentation.
  ↳ [#66289](https://github.com/ceph/ceph/pull/66289): [aed9d86](https://github.com/ceph/ceph/commit/aed9d86e650df34889c90c3359650d42f250415f)
