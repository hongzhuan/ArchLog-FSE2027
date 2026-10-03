# Release Note

## Important Changes

### Distribution & Logic Layer
- Integrate the dmclock submodule into the ceph.git repository as the new QoS scheduling core module. (Architecture event: QoS scheduling module change)
  ↳ [#62364](https://github.com/ceph/ceph/pull/62364): [2cf2d74](https://github.com/ceph/ceph/commit/2cf2d745aaadd482ab7e918b1a818993c5739b84), [16b8eb3](https://github.com/ceph/ceph/commit/16b8eb315090d9714730669a74eeb726f1a0a04f)
- Added a new independent sleep control configuration item for the recovery process of downgraded PG, and modified the recovery logic to limit data movement. (Architecture-related: configuration items)
  ↳ [#62399](https://github.com/ceph/ceph/pull/62399): [ccf513f](https://github.com/ceph/ceph/commit/ccf513fa0cf56845fad1a8f7059b85345dae7ed4)
- Fixed the problem of not correctly marking new objects when deleting missing entries, and restored the new object marking behavior for missing records. (Architecture-related: public API)
  ↳ [#63152](https://github.com/ceph/ceph/pull/63152): [9dc4f74](https://github.com/ceph/ceph/commit/9dc4f74f09b4008476b0aa36bc1fb909357c1eba)
- Fixed the issue where the ceph node ls command still displays an error after the OSD is destroyed. (Architecture-related: public API)
  ↳ [#62326](https://github.com/ceph/ceph/pull/62326): [aa34436](https://github.com/ceph/ceph/commit/aa3443679f251a6eff876e75aa4a09890785a8df)
- Fixed the problem of AuthBadMethodFrame returning error allowed_modes in msgr2 protocol. (Architecture-related: public API)
  ↳ [#65334](https://github.com/ceph/ceph/pull/65334): [fb08c3c](https://github.com/ceph/ceph/commit/fb08c3c120991b32e123dbddbd925aef77a08c08)
- CephFS rename operations now require the refuse_client_session flag to be set first. (Architecture-related: parsing behavior)
  ↳ [#61410](https://github.com/ceph/ceph/pull/61410): [3a8046c](https://github.com/ceph/ceph/commit/3a8046c3be8969aee04c612094194173b7dbe1ce)
- Change the return type of ScrubQueue::scrub_sleep_time from double to std::chrono::milliseconds. (Architecture-related: public API)
  ↳ [#63558](https://github.com/ceph/ceph/pull/63558): [015e384](https://github.com/ceph/ceph/commit/015e3845f1918740cbac8d05d7a07763821aa942)
- Deprecated cls_cxx_gather and cls_cxx_get_gathered_data functions. (Architecture-related: public API)
  ↳ [#60195](https://github.com/ceph/ceph/pull/60195): [f54d8fd](https://github.com/ceph/ceph/commit/f54d8fd96895e5cfed5d15e2b5917b32656fcbf9), [67784b1](https://github.com/ceph/ceph/commit/67784b17578a0f1c12e09c0657f260f52720dd4e)
- Clarified the scope of the OSD cleanup interval option, and added the deep cleanup interval coefficient of variation option. (Architecture-related: configuration options)
  ↳ [#63490](https://github.com/ceph/ceph/pull/63490): [ff57d7e](https://github.com/ceph/ceph/commit/ff57d7eb67076b005408d3cf45106eb1aa818932)
- Added setting guidance for the mon_warn_pg_not_deep_scrubbed_ratio configuration item, indicating that this value should be set on the Manager through the ceph config set mgr command. (Architecture-related: installation configuration)
  ↳ [#62503](https://github.com/ceph/ceph/pull/62503): [ddadd44](https://github.com/ceph/ceph/commit/ddadd44ae2302972d6a62a1755c62ff24d330f4a)

### Interface Layer
- Before renaming CephFS, you must ensure that the file system is offline and the refuse_client_session flag is set, otherwise the operation will be rejected. (Architecture-related: public API)
  ↳ [#61410](https://github.com/ceph/ceph/pull/61410): [c3f6320](https://github.com/ceph/ceph/commit/c3f632044c9e68aad6f7e1cd4284a8862afdf572)
- Fixed historical operation command output and error handling, added missing commands, corrected mon_enable_op_tracker check logic, and tracked changes to this configuration item to correctly enable tracking. (Architecture-related: configuration item behavior)
  ↳ [#64843](https://github.com/ceph/ceph/pull/64843): [a54bdde](https://github.com/ceph/ceph/commit/a54bdde7138c3b4cece91fa004570a6d3bec4dd7)
- Support configuring multiple Kafka brokers in bucket notification, add optional parameter kafka-brokers, and update related documents and tests. (Architecture-related: public API)
  ↳ [#61825](https://github.com/ceph/ceph/pull/61825): [2f79424](https://github.com/ceph/ceph/commit/2f79424f3292d144b4c2512531cec6e8d5d373f6)
- Added ceph mgr module force disable command to allow forcible disabling of the always-on MGR module, and updated related data structures to support this function. (Architecture-related: public API)
  ↳ [#60563](https://github.com/ceph/ceph/pull/60563): [ba3bb8d](https://github.com/ceph/ceph/commit/ba3bb8d290738a7ebee1c0808d0fcc6211d01da7)
- Added support for partNumber parameter to S3 GetObject operation, allowing to read specified fragments of multi-part upload objects. (Architecture-related: public API)
  ↳ [#62544](https://github.com/ceph/ceph/pull/62544): [fbddb23](https://github.com/ceph/ceph/commit/fbddb234985f5743f2d5146e542773a167162159), [2b1290c](https://github.com/ceph/ceph/commit/2b1290c38eaa41a0c4d2f9d80b14b3b4f708884e), [d0d8253](https://github.com/ceph/ceph/commit/d0d8253858b6a6beeb96108e22e3f427e8f3296e), [792ec70](https://github.com/ceph/ceph/commit/792ec70a4fb5632cdedb5595158bf0c99a3712c6)
- Added ceph mon disable_stretch_mode command to allow users to gracefully exit stretch mode and restore to a normal cluster. (Architecture-related: public API)
  ↳ [#60630](https://github.com/ceph/ceph/pull/60630): [6f571d3](https://github.com/ceph/ceph/commit/6f571d38ae1b131d8d18668e8dee243115d1f40c) | [#61654](https://github.com/ceph/ceph/pull/61654): [e6ae37f](https://github.com/ceph/ceph/commit/e6ae37f56894462b86fe4eb26e9f1b1278bf0e9c)
- Added RSA algorithm support using modulus and exponent for JWT signature verification of STS. (Architecture-related: public API)
  ↳ [#63053](https://github.com/ceph/ceph/pull/63053): [6a5d465](https://github.com/ceph/ceph/commit/6a5d465ed008b5fd1d5d3f18bc1acd989fb90c17), [6584940](https://github.com/ceph/ceph/commit/658494088357f01af1c43fd0a8247c8c970272de)
- Allow object locking to be enabled on existing buckets through PutObjectLockConfiguration, provided that the bucket has version control enabled. (Architecture-related: public API)
  ↳ [#62063](https://github.com/ceph/ceph/pull/62063): [f7b390c](https://github.com/ceph/ceph/commit/f7b390c324f89633c4342cc0494fe87bf8f77a6f)
- Added a new status management command to the ceph-mgr daemon to replace the removed command of the same name provided by the static link client. (Architecture-related: public API)
  ↳ [#62505](https://github.com/ceph/ceph/pull/62505): [abb1ab7](https://github.com/ceph/ceph/commit/abb1ab73a6eb69721b981fa1671d79a45b290d8f)
- Added force deletion options (force and --yes-i-really-mean-it) to radosgw-admin object rm, allowing bucket index entries to be deleted even when the object header does not exist or is damaged. (Schema related: public API)
  ↳ [#64311](https://github.com/ceph/ceph/pull/64311): [9665ade](https://github.com/ceph/ceph/commit/9665ade024d828b676316395a6bd0322922527ab), [1d8c554](https://github.com/ceph/ceph/commit/1d8c5544156ea1baa66f8cfc7343ce1d5a1293ea), [fb4a398](https://github.com/ceph/ceph/commit/fb4a3989b6a56ab4c171e1edfbe4a797ed765e18)
- Improved the JWKS verification logic of STS, and added a configurable JWKS endpoint verification switch. (Architecture-related: public API)
  ↳ [#64937](https://github.com/ceph/ceph/pull/64937): [e1f22a0](https://github.com/ceph/ceph/commit/e1f22a046f0eac4b5807b20e04739dfde49c9784), [d58822d](https://github.com/ceph/ceph/commit/d58822d9b6ae475aa3443337e28176a7533e1b4f) | [#63053](https://github.com/ceph/ceph/pull/63053): [9757eb0](https://github.com/ceph/ceph/commit/9757eb00f001279f7113ace9b1584bf35d9c0ff5)
- Trigger re-sharding in advance for versioned buckets, and speed up sharding judgment by lowering the maximum number of objects per shard threshold. (Architecture-related: public API)
  ↳ [#63598](https://github.com/ceph/ceph/pull/63598): [9bea73a](https://github.com/ceph/ceph/commit/9bea73a633c3f2aa00ec15c1aa8bd8140a27af8c)
- Added mds_allow_batched_ops configuration item for MDS, allowing batch operations to be disabled. (Architecture-related: configuration item)
  ↳ [#64540](https://github.com/ceph/ceph/pull/64540): [1e2aefd](https://github.com/ceph/ceph/commit/1e2aefdfc8cef76a5c4338da84c9a3d8829f5392), [03830d8](https://github.com/ceph/ceph/commit/03830d8d1ade96b06fa8bcb833d435a7e72745fe)
- Disable unprivileged users from setting suid/sgid permission bits. (Architecture-related: public API)
  ↳ [#66040](https://github.com/ceph/ceph/pull/66040): [6e9983e](https://github.com/ceph/ceph/commit/6e9983e56a6dfdb06758c72e9d74e5596f01095d)
- Added an admin socket command to MDS for exporting subtree export status. (Architecture-related: public API)
  ↳ [#61512](https://github.com/ceph/ceph/pull/61512): [1446818](https://github.com/ceph/ceph/commit/144681835af1dbfbb4f5c3792f071e0e1bff2f62)
- Added ceph auth rotate command to support rotating the permanent key of the entity. (Architecture-related: public API)
  ↳ [#58236](https://github.com/ceph/ceph/pull/58236): [c642834](https://github.com/ceph/ceph/commit/c642834e0194867f89e61d177e1ccd06ce6d1018)
- Fixed multiple related issues in MDS export/import subtree tasks, including status clearing, race conditions and session management. (Architecture event: Ceph_Client_VFS_Core module change)
  ↳ [#61514](https://github.com/ceph/ceph/pull/61514): [626f3a7](https://github.com/ceph/ceph/commit/626f3a78cadffc07cbfd74adc042f1f002b7c210), [a138a43](https://github.com/ceph/ceph/commit/a138a435192c9d4be9c059aad892f39cc9c445cd), [e9d3225](https://github.com/ceph/ceph/commit/e9d3225babc19aece406c1c72438572f1a51a5ed)
- Fixed multiple issues related to RGW multi-part upload, including response with partNumber of 1 when uploading in non-parts and status query error when only one part is included. (Architecture event: Core_Utilities_and_Messaging module change)
  ↳ [#62544](https://github.com/ceph/ceph/pull/62544): [b2db3bb](https://github.com/ceph/ceph/commit/b2db3bbc8ceafc3572781a3fe81b1d6a1570c5f1), [8ec0a95](https://github.com/ceph/ceph/commit/8ec0a955380701c45ed7bbd87110844846a51413), [b18c860](https://github.com/ceph/ceph/commit/b18c860b9c186a55503e66687fe12a1b35f1bdf8)
- Fix RGW bucket attribute deletion and storage logic to ensure that attribute updates are persisted correctly. (Architecture event: Core_Utilities_and_Messaging module change)
  ↳ [#61996](https://github.com/ceph/ceph/pull/61996): [901a9a6](https://github.com/ceph/ceph/commit/901a9a6a42568768c8af41c322aee7591495f57b), [49fa8f0](https://github.com/ceph/ceph/commit/49fa8f0c2b8a8122b1eacdf7120c3c983b157bb9), [c84463e](https://github.com/ceph/ceph/commit/c84463e59fce82f5b245d6a4c74bfa67d8c08ce5) | [#64488](https://github.com/ceph/ceph/pull/64488): [4b41e20](https://github.com/ceph/ceph/commit/4b41e209a0d88a392bdbf1f05411e14eb9bf16ba)
- Fixed the problem that repeated acquisition of file lock write lock in a single request may lead to deadlock. (Architecture event: Ceph_Client_VFS_Core module change)
  ↳ [#61839](https://github.com/ceph/ceph/pull/61839): [375c295](https://github.com/ceph/ceph/commit/375c29537e78d758f74a0366a2b27ed021a34d2b)
- Fixed the issue where the read operation in the CephFS client hangs when obtaining Fc permissions because the permissions are revoked by MDS and the reference count is non-zero. (Architecture event: Ceph_Client_VFS_Core module change)
  ↳ [#60695](https://github.com/ceph/ceph/pull/60695): [93a1b56](https://github.com/ceph/ceph/commit/93a1b5635db333542655105fba822e297ba78ac7)
- Fixed the chownat() function's handling of empty path names, directly operates the files referenced by dirfd when the AT_EMPTY_PATH flag is specified, and added corresponding test cases. (Architecture-related: public API)
  ↳ [#61165](https://github.com/ceph/ceph/pull/61165): [1cc9fd8](https://github.com/ceph/ceph/commit/1cc9fd874daccf3131a49a92edf1e534a636f51d)
- Handle empty path names gracefully in statxat(): when the AT_EMPTY_PATH flag is set and the path name is empty, directly operate the file referenced by dirfd, otherwise return ENOENT. (Architecture-related: public API)
  ↳ [#61165](https://github.com/ceph/ceph/pull/61165): [770a580](https://github.com/ceph/ceph/commit/770a580d281e1c0b18b1b69ad1a3ab3cfe39d7f1)
- Fix ETag output format, add double quotes for ETag values in multiple S3 response methods, to make it consistent with AWS S3 API. (Schema related: public API)
  ↳ [#62608](https://github.com/ceph/ceph/pull/62608): [7c428f5](https://github.com/ceph/ceph/commit/7c428f58b725c9b7a71348eda63f34196beaf5f9)
- Modify Keystone token verification logic so that admin token is no longer mandatory, and user token verification will use its own token. (Architecture-related: public API)
  ↳ [#64200](https://github.com/ceph/ceph/pull/64200): [8ac23fd](https://github.com/ceph/ceph/commit/8ac23fd720135e56181360dcc5c9f16b99f0273d)
- Fixed an issue where using merge_and_store_attrs() when rebuilding a bucket caused the Swift API to be unable to delete container metadata. Instead, directly set attributes and call put_info() storage. (Architecture-related: public API)
  ↳ [#64411](https://github.com/ceph/ceph/pull/64411): [ebee7fa](https://github.com/ceph/ceph/commit/ebee7fa53b3c9e084897e076faaaf0ee2cc7223f)
- Add missing last_modified field to Swift API bucket list response. (Schema related: public API)
  ↳ [#61553](https://github.com/ceph/ceph/pull/61553): [19a05d0](https://github.com/ceph/ceph/commit/19a05d021bd971313f734cd3225342bfd7f3d2ee), [3557295](https://github.com/ceph/ceph/commit/35572950d76f18858240c1b1138ee68eccb36e2c)
- Fix ARN-based condition matching issue in IAM policy evaluation and make it case-sensitive to comply with AWS specifications. (Schema related: public API)
  ↳ [#62434](https://github.com/ceph/ceph/pull/62434): [d578ab0](https://github.com/ceph/ceph/commit/d578ab0439d7ff6feb732dd50e4d4ac1ef1339e6), [f4010e6](https://github.com/ceph/ceph/commit/f4010e6624191869fbce2775d3cf2fa6f50a39fc)
- Fixed the problem of group_snap_create() not using rbd_default_snapshot_quiesce_mode configuration, making its behavior consistent with other snapshot creation APIs. (Architecture-related: public API)
  ↳ [#62962](https://github.com/ceph/ceph/pull/62962): [396acc9](https://github.com/ceph/ceph/commit/396acc957e6fea09ce3b48558fd59197e434f4b7)
- Disable moving images belonging to the group to the recycle bin (except in migration scenarios), and provide clearer prompt information for this error. (Architecture-related: public API)
  ↳ [#62967](https://github.com/ceph/ceph/pull/62967): [8d740b1](https://github.com/ceph/ceph/commit/8d740b1119ab9459bdceb8c84305782f8dd1f06d)
- Fixed the issue where the rbd info command was incorrectly displayed as 'unknown' during image creation, and is now correctly displayed as 'creating'. (Architecture-related: public API)
  ↳ [#62939](https://github.com/ceph/ceph/pull/62939): [596aef3](https://github.com/ceph/ceph/commit/596aef3a5eb3c1f31e553278dfab3a4f1ff44eb7)
- Fixed the issue where readdir cannot list all directory entries when the OSD is full in a multi-MDS cluster. (Architecture-related: public API)
  ↳ [#65348](https://github.com/ceph/ceph/pull/65348): [e0d7837](https://github.com/ceph/ceph/commit/e0d7837a86e36bc2c37812015d47fbc112ff0592)
- Remove the default follow_olh=true overload of get_obj_state(), forcing the caller to pass parameters explicitly. (Architecture-related: public API)
  ↳ [#62544](https://github.com/ceph/ceph/pull/62544): [fba5c11](https://github.com/ceph/ceph/commit/fba5c115ec80b179a4e81858d7f0e19f8bb26417)
- Use internal flags instead of public API flags in Group::snap_create(), and fix local variable types. (Architecture-related: public API)
  ↳ [#62962](https://github.com/ceph/ceph/pull/62962): [30cab5c](https://github.com/ceph/ceph/commit/30cab5c0c62e20304a3c6b40f8c0bd471a2aa302)
- Added cluster fsid for remote metadata cache key to solve the problem of insufficient pool ID when using multi-cluster mirroring. (Architecture-related: public API)
  ↳ [#66272](https://github.com/ceph/ceph/pull/66272): [ca7b7ad](https://github.com/ceph/ceph/commit/ca7b7ad25a4a1a67182fc73f613dd9dfaccdc705)
- Added configuration option mds_allow_async_dirops for MDS, used to enable or disable asynchronous directory operations, as a temporary solution to the lock cache bug. (Architecture-related: public configuration)
  ↳ [#61839](https://github.com/ceph/ceph/pull/61839): [3fb9319](https://github.com/ceph/ceph/commit/3fb9319d6d313c6c25d08cf982e3442e1cacad06)
- Added verification of JWKS URI certificates in OIDC token verification, supported the use of modulus (n) and exponent (e) for signature verification, and changed error handling from throwing integers to throwing standard exceptions. (Architecture-related: public API)
  ↳ [#63053](https://github.com/ceph/ceph/pull/63053): [8c39f5e](https://github.com/ceph/ceph/commit/8c39f5e397a7067c576f613d5a096f748de7ae4f)
- Modified the description of the flags parameter in the ceph_statxat() API documentation to clarify that it only accepts two flags, AT_STATX_DONT_SYNC and AT_SYMLINK_NOFOLLOW. (Architecture-related: public API)
  ↳ [#61165](https://github.com/ceph/ceph/pull/61165): [c06fc10](https://github.com/ceph/ceph/commit/c06fc10dd2728ed8a26cfda6a89f76bf93f7fdd1)

### Storage Backend Layer
- Preload all compressor plug-ins when mounting, avoid loading on demand at runtime, and simplify related option selection logic. (Architecture-related: build and installation methods)
  ↳ [#62145](https://github.com/ceph/ceph/pull/62145): [d16b15a](https://github.com/ceph/ceph/commit/d16b15a809ad89d07250562ece4eef9e6ff500f7)
- Added read-only mode mount support for read-only operations of ceph-objectstore-tool and ceph-kvstore-tool so that data can still be accessed when the object store is damaged. (Architecture-related: build and installation methods)
  ↳ [#62122](https://github.com/ceph/ceph/pull/62122): [78e8f35](https://github.com/ceph/ceph/commit/78e8f355e70385bed61bd4bb2781af6660864b84), [4bbc4cf](https://github.com/ceph/ceph/commit/4bbc4cf017b7ad79e7b0ca4b3f8713e8521e6ab8)
- Fix issues related to BlueStore allocator, including HybridAllocator's ENOSPC false positives and the introduction of new allocators, and unify the error handling logic of BlueFS and BlueStore. (Architecture event: Core_Utilities_and_Messaging module changes)
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [c2e6d7b](https://github.com/ceph/ceph/commit/c2e6d7b56bb3f3984ab89b7532f97007c7a714f9), [2d6dca3](https://github.com/ceph/ceph/commit/2d6dca32ef3dd183e0d3aa591dfdb0896855248e), [7bc78aa](https://github.com/ceph/ceph/commit/7bc78aa857738a69f0e4c2ad81d702c6f5e7dffd), [d72be3e](https://github.com/ceph/ceph/commit/d72be3e99c794887a59ef264fa12642717f6ba1b), [dd95fca](https://github.com/ceph/ceph/commit/dd95fca5af5b5faed5d5c73ee9f5998411765a24)
- Fixed "Invalid read" error reported by valgrind in mixed btree2 allocator, adjusted return type and internal implementation of _remove_from_tree method. (Architecture event: CloneRequest module change)
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [7240441](https://github.com/ceph/ceph/commit/72404417c6c915048f577b08b70831a0b8872cf0)
- BlueFS becomes the only selector for volume reserved block size, removing the parameter for the caller to pass the reserved size. (Architecture-related: BlueFS interface changes)
  ↳ [#62721](https://github.com/ceph/ceph/pull/62721): [350b422](https://github.com/ceph/ceph/commit/350b42254dc8374489a51ee6dbfeb9beb862d409)
- Add device type name parameter in BlueStore's block device creation interface. (Architecture-related: public API)
  ↳ [#62481](https://github.com/ceph/ceph/pull/62481): [2dd9e05](https://github.com/ceph/ceph/commit/2dd9e05adf34be3520f16f67c5e7887743eb2b50)
- Introduced KernelDevice discard queue upper limit configuration to prevent OSD capacity problems. (Architecture-related: construction and installation methods)
  ↳ [#62220](https://github.com/ceph/ceph/pull/62220): [861d327](https://github.com/ceph/ceph/commit/861d327968049ee9c7b931df5f9a3c4dcf7cfbcb)
- Restore bdev_async_discard configuration parameter to ensure backward compatibility. (Architecture-related: configuration compatibility)
  ↳ [#62481](https://github.com/ceph/ceph/pull/62481): [844cef2](https://github.com/ceph/ceph/commit/844cef23a0caa8dd9683ff6a1c706288e23deda1)

### Cross-cutting / Other Architecture-related Changes
- Added p2aligned() function in include/intarith.h, which is used to determine whether a value is aligned as specified. (Architecture-related: public API)
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [95bdff7](https://github.com/ceph/ceph/commit/95bdff7d534d10f54713864312ff01048794e12f)
- Added IPv6 support to is_addr_in_subnet function so that it can handle both IPv4 and IPv6 addresses. (Architecture-related: Platform compatibility)
  ↳ [#62814](https://github.com/ceph/ceph/pull/62814): [23a110b](https://github.com/ceph/ceph/commit/23a110bfbaf886aeb14f3a3147f429a9cf86b70c)
- Modify the return type of interval_set::erase function from void to iterator, so that it returns the next iterator of the erased element. (Architecture-related: public API)
  ↳ [#62481](https://github.com/ceph/ceph/pull/62481): [082a1f3](https://github.com/ceph/ceph/commit/082a1f36905297d89b00d3ab79a61c8fc5c8af1d)
- Update the release process document to explain that release builds will not automatically build container images and need to be completed manually after package signing and uploading. (Architecture-related: build and installation methods)
  ↳ [#61818](https://github.com/ceph/ceph/pull/61818): [812cac9](https://github.com/ceph/ceph/commit/812cac9f56b625d4447222b5946601c5b39708d6)

## Routine Changes

### New features
- Added a general scheduled event scheduling interface and ScrubMachineListener's log/node ID interface to OSD scrubber, simplifying scrub scheduling logic.
  ↳ [#63558](https://github.com/ceph/ceph/pull/63558): [55b1f86](https://github.com/ceph/ceph/commit/55b1f869aa0af91ff808bcef0e4313753ced3a3d), [d57bf59](https://github.com/ceph/ceph/commit/d57bf59968e40e47cab3e11684b2f76dbc4d43c6), [7c19046](https://github.com/ceph/ceph/commit/7c19046c68c5bf20d9536d605c43c158b966a1a7), [5b35551](https://github.com/ceph/ceph/commit/5b35551d9b336c7ca0398a40b5f80c87dfdba6f9), [d806867](https://github.com/ceph/ceph/commit/d8068670f1d05b5afb1da6e72dac3dadbe85e046), [7c02d0e](https://github.com/ceph/ceph/commit/7c02d0e03fe95683be574c8d2e090a5cadec4af4)
- Added --no-superblock and --force options to ceph-objectstore-tool's pg export command, allowing to skip superblock reading and continue exporting if data reading errors occur.
  ↳ [#62122](https://github.com/ceph/ceph/pull/62122): [5fe22a2](https://github.com/ceph/ceph/commit/5fe22a29b1f529f58d0a0bdff7ad8bc88b9a0a94), [70e9ebd](https://github.com/ceph/ceph/commit/70e9ebdd1d505f49f00fc7e1994e854cf6068c97)
- Call set_pool_full_try() when deleting head and tail objects, allowing deletion operations to still be performed when the RADOS pool quota limit is reached.
  ↳ [#62094](https://github.com/ceph/ceph/pull/62094): [c5fa9fe](https://github.com/ceph/ceph/commit/c5fa9fe9746044c010ad2fcef5c21bd85040058c), [d33771e](https://github.com/ceph/ceph/commit/d33771ef6706938d57c1dc57fc740b65439f9570), [de1332c](https://github.com/ceph/ceph/commit/de1332cf649744ce73471b64470f7e1f55292e66), [1ecce5d](https://github.com/ceph/ceph/commit/1ecce5dafa61a688f7370b248eab51712255ee1b)
- Improve the radoslist subcommand, when the head object is missing, it will no longer ignore it, but output its OID and related information.
  ↳ [#62418](https://github.com/ceph/ceph/pull/62418): [c9069e4](https://github.com/ceph/ceph/commit/c9069e4ce0b7a55a09d08fcc54db7518a27d64e8)
- Introduced --data-path and --op aliases for the --path and --command options of ceph-bluestore-tool respectively.
  ↳ [#62122](https://github.com/ceph/ceph/pull/62122): [4852fda](https://github.com/ceph/ceph/commit/4852fda05067422b5df79b2076b01939e05922ab)
- Added importing_count field to MDS session dump output.
  ↳ [#61514](https://github.com/ceph/ceph/pull/61514): [f08a263](https://github.com/ceph/ceph/commit/f08a263a2e299a2b3721fdef93300e62af2eefde)

### bug fixes
- When checking dead CRUSH zones in stretch mode, ignore non-existent CRUSH buckets to avoid assertion failures.
  ↳ [#62040](https://github.com/ceph/ceph/pull/62040): [60e196d](https://github.com/ceph/ceph/commit/60e196de6182473da1f4c0ebc61a53c765c188d6) | [#62212](https://github.com/ceph/ceph/pull/62212): [d4afccc](https://github.com/ceph/ceph/commit/d4afcccf14cdcf3352941e97e36628fa44ea15b3)
- Fixed the problem of multiple asynchronous discard threads waking up each other when running, instead notifying only when discard_drain waits for conditions.
  ↳ [#62152](https://github.com/ceph/ceph/pull/62152): [3a901ad](https://github.com/ceph/ceph/commit/3a901add5236835f37480a205cc86e9ea24d161b)
- Fixed an issue where the client did not return the EOPNOTSUPP error when passing mode 0 in the fallocate call.
  ↳ [#60657](https://github.com/ceph/ceph/pull/60657): [d9f1ef5](https://github.com/ceph/ceph/commit/d9f1ef5eac13f3a200ebb6583c0258d6a9651c92)
- Fixed the problem in life cycle management that the non-current object instance could not be accessed correctly when it was empty, and adjusted the processing logic of the instance field to be compatible with object entries after version control is enabled or suspended.
  ↳ [#63031](https://github.com/ceph/ceph/pull/63031): [5228a0b](https://github.com/ceph/ceph/commit/5228a0b05b144da24a26644e0b1d7b1ff1a78a16)
- Fixed the issue where the storage class is empty when displaying multipart uploads. Now the normalized storage class will be used for output.
  ↳ [#64312](https://github.com/ceph/ceph/pull/64312): [5ce2ed7](https://github.com/ceph/ceph/commit/5ce2ed72ab7eef1548ad9bbc41aa59bc4fdcca42)
- Warn about possible temporary EIO errors when deleting a file system if there is an active snapshot schedule.
  ↳ [#61187](https://github.com/ceph/ceph/pull/61187): [411f041](https://github.com/ceph/ceph/commit/411f04166f194af1a156c0ebb3965544f8d020af)
- Fixed a segfault that may occur when cephfs-journal-tool imports journal from an invalid or empty dump file, and added checks for file read errors and missing necessary header fields.
  ↳ [#62114](https://github.com/ceph/ceph/pull/62114): [17fe94e](https://github.com/ceph/ceph/commit/17fe94e6f01e92afefd5af30a8fcac05b489dee4)
- Fixed the invalid access problem in handle_client_getattr caused by not checking whether the array is empty before accessing mdr->dn[0].back().
  ↳ [#61450](https://github.com/ceph/ceph/pull/61450): [72fa4f6](https://github.com/ceph/ceph/commit/72fa4f6403cd267c6655ef1a40bcd6c96b1ebdcf)
- Fixed a race condition in reset_recv_state caused by log output not being executed under lock protection to avoid hang when the connection is closed.
  ↳ [#65786](https://github.com/ceph/ceph/pull/65786): [8d1a589](https://github.com/ceph/ceph/commit/8d1a5892a36d9b69d1748ab480a37a671b149cb0)
- Fixed regression in radosgw-admin bucket radoslist command when handling SLO inventory buckets.
  ↳ [#62418](https://github.com/ceph/ceph/pull/62418): [e61591b](https://github.com/ceph/ceph/commit/e61591b706fb47e2c871440712abb59fa10b7a91)
- Fix path handling error in ll_walk function to avoid handling path relative to non-existent inode 0.
  ↳ [#62500](https://github.com/ceph/ceph/pull/62500): [abb1bea](https://github.com/ceph/ceph/commit/abb1bea4158e189c40610cf84880aae208fbe4ee), [8862e60](https://github.com/ceph/ceph/commit/8862e60e6bacbf21906a6340a39ce69cb1a3e749)
- Fixed an issue where Monitors were unable to ping each other after the election because quorum_mon_feature was empty, resulting in incorrect connection scores.
  ↳ [#62925](https://github.com/ceph/ceph/pull/62925): [f8aac3c](https://github.com/ceph/ceph/commit/f8aac3c743c8d006507ab2bac715700e9d07060a)
- Fixed the problem of iterator failure after erasing elements in discard_queued traversal.
  ↳ [#62481](https://github.com/ceph/ceph/pull/62481): [b2ab1e7](https://github.com/ceph/ceph/commit/b2ab1e7f76c74129893b6348ebcf8642c81fde2e)
- Fix issue where changes could be lost when mon_memory_target is set in the metabase but mon_memory_autotune is left at its default value.
  ↳ [#63805](https://github.com/ceph/ceph/pull/63805): [dd1fb27](https://github.com/ceph/ceph/commit/dd1fb273d5ee6e49c3dfb072cbc7cbd5a5ffd974)
- Fixed the issue where the tail data was mistakenly deleted when the object was copied from itself.
  ↳ [#62656](https://github.com/ceph/ceph/pull/62656): [fdea7f3](https://github.com/ceph/ceph/commit/fdea7f34829010aaf77e8bb7ae979b07887abe78)
- Fix race condition between truncate() and unlink() in BlueFS.
  ↳ [#62840](https://github.com/ceph/ceph/pull/62840): [4f83038](https://github.com/ceph/ceph/commit/4f83038f13e60f02d2a14c59df232b392b57a904)
- Fix session tracker to include killing sessions in load statistics.
  ↳ [#65253](https://github.com/ceph/ceph/pull/65253): [3ed812e](https://github.com/ceph/ceph/commit/3ed812e51b02ebbf93e964969cd2579bbb00a463)
- Fixed recovery delay counter calculation error for PGRecovery, PGRecoveryContext and PGRecoveryMsg.
  ↳ [#62801](https://github.com/ceph/ceph/pull/62801): [be1c15f](https://github.com/ceph/ceph/commit/be1c15fe8fa9e1077ded70fceb8a7bea2b6f87ee)
- Fixed the issue in the radosgw-admin bucket object shard command that caused division by zero to crash due to passing in a non-positive number of shards.
  ↳ [#62885](https://github.com/ceph/ceph/pull/62885): [176b3c8](https://github.com/ceph/ceph/commit/176b3c8ea844efc354e6defa02ec8617df31eacf)
- Fixed a deadlock issue in rbd-mirror that could be caused by calling the asynchronous operation tracker's finish_op while holding a lock.
  ↳ [#64091](https://github.com/ceph/ceph/pull/64091): [43edec8](https://github.com/ceph/ceph/commit/43edec80d2de231011d3abc687bffd3e4c2f0f94)
- When the mirror status is CREATING, the mirror mirror status is also allowed to be written to reduce the status synchronization delay of newly created mirrors.
  ↳ [#63236](https://github.com/ceph/ceph/pull/63236): [ea72e06](https://github.com/ceph/ceph/commit/ea72e066df74086a7003fb1a3f39723356af4219)
- Correct the way the notification manager worker thread name is set, move the thread naming operation inside the thread and add error handling.
  ↳ [#63095](https://github.com/ceph/ceph/pull/63095): [86ca4ba](https://github.com/ceph/ceph/commit/86ca4ba39081abeba25d68777b244ff1142a7d3d)
- Fixed the issue of incorrectly deleting the local mirror when the remote mirror is no longer the primary mirror in snapshot-based mirroring mode.
  ↳ [#64738](https://github.com/ceph/ceph/pull/64738): [2f58883](https://github.com/ceph/ceph/commit/2f58883806583ccb8360c3a437334c4f6c1a02f5)
- Fixed compilation error in rgw_torrent.h caused by conflict between OpenSSL SHA1 macro and ceph::crypto::SHA1 alias.
  ↳ [#63053](https://github.com/ceph/ceph/pull/63053): [6172edc](https://github.com/ceph/ceph/commit/6172edcf5d09433b17d6233e229476cfe17161f8)
- Fixed URL decoding-related crashes in RGW, including empty string checking and invalid hex character handling.
  ↳ [#64052](https://github.com/ceph/ceph/pull/64052): [d000e56](https://github.com/ceph/ceph/commit/d000e56ba846a8e36c6f42d11a4c8c52a688c63c), [e595370](https://github.com/ceph/ceph/commit/e5953705671787b930754f1590572846528200dc), [f1f9925](https://github.com/ceph/ceph/commit/f1f9925eb3e628cb2199f570761ba6e12c3ba877)
- Fixed MDS lock management and log advancement issues, including lock release delay after early_reply and has_any_waiter bitmask overflow.
  ↳ [#64540](https://github.com/ceph/ceph/pull/64540): [74ff0e4](https://github.com/ceph/ceph/commit/74ff0e483574793d4bd719eb277f4bc7d37ef698) | [#67495](https://github.com/ceph/ceph/pull/67495): [0199784](https://github.com/ceph/ceph/commit/0199784ab931d02e1a704ab4676bf1a3442dac97)
- Fixed the problem that rgw_servers filtering in RGW Overview Grafana panel does not take effect.
  ↳ [#62268](https://github.com/ceph/ceph/pull/62268): [a55d424](https://github.com/ceph/ceph/commit/a55d424c9ebc4dcad345248ce7d0fcf57b720e18)
- Fixed the issue where the heartbeat address sent when OSD starts may be an old value.
  ↳ [#56520](https://github.com/ceph/ceph/pull/56520): [fa6bdea](https://github.com/ceph/ceph/commit/fa6bdea4ed55afcfe0d994ef196cce65ec4fb10a)
- Fixed the serial number advancement logic when extending the BlueFS log to avoid serial number status errors.
  ↳ [#61653](https://github.com/ceph/ceph/pull/61653): [0210f57](https://github.com/ceph/ceph/commit/0210f57a5ec8a8c0ea76a72984f39dae24986cb0)
- Fix the calculation of the d_reclen field in readdir so that it correctly calculates the record size based on the returned name length.
  ↳ [#61519](https://github.com/ceph/ceph/pull/61519): [15774e5](https://github.com/ceph/ceph/commit/15774e5d41b55d8cbbc447dc5e2056d849a07d69)
- Fixed an issue in BlueStore where ExtentDecoderPartial::_consume_new_blob may dereference invalid iterators when data is corrupted.
  ↳ [#62054](https://github.com/ceph/ceph/pull/62054): [1cb9a68](https://github.com/ceph/ceph/commit/1cb9a684778450289d4f7d6430471f02eb775e3e)
- After the journal is restored, check whether the dump file header contains the necessary layout fields, and if missing, an error will be returned.
  ↳ [#62114](https://github.com/ceph/ceph/pull/62114): [7858101](https://github.com/ceph/ceph/commit/7858101da290f4310ec8aeeb7b79a38a6fbe2767)
- Fixed the invalid access issue where the container is not checked before accessing mdr->dn[0].back() in handle_client_getattr.
  ↳ [#61516](https://github.com/ceph/ceph/pull/61516): [fb03da7](https://github.com/ceph/ceph/commit/fb03da7ddc0bd8d7e96cfaca80f0b6defdec97c8)
- Fixed an issue that caused 403 errors when sending internal headers when getting objects from cloud endpoints.
  ↳ [#63031](https://github.com/ceph/ceph/pull/63031): [c3f8c35](https://github.com/ceph/ceph/commit/c3f8c359c28e44576b0bfbc59dc71a2ebfd0239e)
- Fix the discard_op performance counter so that it counts the number of operations instead of the number of bytes.
  ↳ [#62481](https://github.com/ceph/ceph/pull/62481): [f66eb67](https://github.com/ceph/ceph/commit/f66eb6733f9ada37c6831cac580ae364a9379670)
- Fixed extent alignment exception in BlueFS::truncate caused by allocation unit change or rollback.
  ↳ [#66056](https://github.com/ceph/ceph/pull/66056): [87c9099](https://github.com/ceph/ceph/commit/87c90994b2f0c4274208028367cc8f376d0b1d6e)
- Fixed the issue where the main block device label was not updated when the device was expanded, make sure to use the correct device path to set the label.
  ↳ [#62216](https://github.com/ceph/ceph/pull/62216): [89013c8](https://github.com/ceph/ceph/commit/89013c810a09df5ef60cda7fb8c802d8797fbfec)
- Fixed an issue where a non-versioned list may loop infinitely when skipping the version suffix.
  ↳ [#62591](https://github.com/ceph/ceph/pull/62591): [ca4f283](https://github.com/ceph/ceph/commit/ca4f28326a59797c510a241e5cbcf7f2d8492ed9)
- Fixed a logic error in forward progress detection when using multi-version object lists.
  ↳ [#62591](https://github.com/ceph/ceph/pull/62591): [c79b289](https://github.com/ceph/ceph/commit/c79b28910aa2b93786cdf2fcc40bf45762713420)
- Reduce the log level of undecoded bdev label and CRC check failure from error to normal to avoid false positives in non-error scenarios.
  ↳ [#62216](https://github.com/ceph/ceph/pull/62216): [51d47a5](https://github.com/ceph/ceph/commit/51d47a5f088968e67c728fb3fc9ebffe896fea96)
- Improve watch reconnection logic, stop renewal when encountering -ENOENT error, and increase the upper limit of retries.
  ↳ [#62403](https://github.com/ceph/ceph/pull/62403): [c95ea88](https://github.com/ceph/ceph/commit/c95ea88269dfdc4d6a5550786ebe223cf9d465c8)
- Fixed the lock violation problem caused by inline completion callback when QCOWFormat reads the cluster.
  ↳ [#64195](https://github.com/ceph/ceph/pull/64195): [37c9921](https://github.com/ceph/ceph/commit/37c99211d5ce448301381eee68f7145eaf0a7b7a)
- Fix failure handling during indicator parsing, and remove the dump_asok_metric method that is no longer used.
  ↳ [#65595](https://github.com/ceph/ceph/pull/65595): [6a6b850](https://github.com/ceph/ceph/commit/6a6b85033a30e87a57b3295b809d72a22804b4c4)
- Improve the life cycle management of DiscardThread, eliminate the race condition between thread startup and removal, and increase the capacity limit of the asynchronous discard queue.
  ↳ [#65216](https://github.com/ceph/ceph/pull/65216): [e0d0ed0](https://github.com/ceph/ceph/commit/e0d0ed0477a79b8f805a2c815c2f89f795dc3b15)
- Fixed rollback processing when multiple entries with the same name cannot be placed into the same fragment when snapdiff results are fragmented.
  ↳ [#65364](https://github.com/ceph/ceph/pull/65364): [08f4489](https://github.com/ceph/ceph/commit/08f44891a2e4f99def175843f1541885d019f658)
- Fix cephfs-journal-tool resetting log pruning position after log recovery reset to free up metadata pool space.
  ↳ [#65603](https://github.com/ceph/ceph/pull/65603): [21449be](https://github.com/ceph/ceph/commit/21449be087aabba09fd45efe4063aa5786e08872)
- Fix radosgw-admin bucket rm --bypass-gc's handling of copied objects.
  ↳ [#66002](https://github.com/ceph/ceph/pull/66002): [023c373](https://github.com/ceph/ceph/commit/023c373d972956f48409a74ed4d2eb79a1c97436)
- Fixed the issue where incomplete non-primary demote snapshots cannot be synchronized after the rbd-mirror daemon is restarted.
  ↳ [#66163](https://github.com/ceph/ceph/pull/66163): [771ad84](https://github.com/ceph/ceph/commit/771ad84db25214ee893afaa4a7684b32d18a10a7)
- Improved the format of a log message in MgrMonitor to make it easier to read.
  ↳ [#60563](https://github.com/ceph/ceph/pull/60563): [b63b462](https://github.com/ceph/ceph/commit/b63b46227e5f7c12def20399125a52ca050c41a2)
- Add debug event flags to MDS batch operation headers to help debug slow request or deadlock issues.
  ↳ [#61518](https://github.com/ceph/ceph/pull/61518): [c6ac3a8](https://github.com/ceph/ceph/commit/c6ac3a824803ced6ff1825b10f78be22c3e59080)
- Added clear_shards_repaired command, which is used to clear the shard repair count to clear related alarms.
  ↳ [#60566](https://github.com/ceph/ceph/pull/60566): [69e75cd](https://github.com/ceph/ceph/commit/69e75cd622bf013be095f50224bdb6fbed0cf7ca)

### Refactoring optimization
- Refactor the BlueStore allocator, including adding assertions, unifying logging, extracting template base classes, and adding a new Btree2 hybrid allocator implementation.
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [5722b74](https://github.com/ceph/ceph/commit/5722b749ae025ed7e4da5a2d9c3cbbb91e4fcad8), [71ced83](https://github.com/ceph/ceph/commit/71ced83e8829294762ebd9d4ddd5f1b3718bc9ce), [19692b8](https://github.com/ceph/ceph/commit/19692b88f119fc1cae6e06168e632051deeb05e4), [3568cd6](https://github.com/ceph/ceph/commit/3568cd6f5cad845f635f27f6b2c8356bbc914f90)
- Remove the repair_oinfo_oid() function that is called every scrub, and migrate the relevant verification logic to possible_auth_shard() for explicit error handling.
  ↳ [#62569](https://github.com/ceph/ceph/pull/62569): [5ce6bf7](https://github.com/ceph/ceph/commit/5ce6bf7729b30d8709ac7c33f46688ee4c7bf43c)
- Optimize bluefs-bdev-expand command output, reconstruct device expansion logic and add read-only mount function.
  ↳ [#62216](https://github.com/ceph/ceph/pull/62216): [fd5394e](https://github.com/ceph/ceph/commit/fd5394eaf88ee7d9f407505ebaf03851dd579e26)
- ioctx creation in RGWRadosRemoveCR instead calls rgw_init_ioctx(), to support global flag setting.
  ↳ [#62094](https://github.com/ceph/ceph/pull/62094): [0bf3ae8](https://github.com/ceph/ceph/commit/0bf3ae847be88c5af54fa7bf2bb9cb24748b78b1)
- Add csum_type field in BlueStore's WriteContext and move checksum type selection logic to _choose_write_options.
  ↳ [#62145](https://github.com/ceph/ceph/pull/62145): [93c781d](https://github.com/ceph/ceph/commit/93c781d19ddded39464b824ac040cdb749ea774e)
- Move and rename ExtentCache to a new structure in the Allocator class, and introduce related auxiliary components.
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [a3fa9da](https://github.com/ceph/ceph/commit/a3fa9daa22abf72fed6322447a915759b16e9c4d)
- Add a constructor that supports custom timeout for mClockScheduler to facilitate unit testing.
  ↳ [#62364](https://github.com/ceph/ceph/pull/62364): [ed9cb86](https://github.com/ceph/ceph/commit/ed9cb86bb11173af1509167aedfc6894e2f5ee5b)
- Simplify the match_policy() function, remove the unused MATCH_POLICY_STRING flag, and update related calls and tests.
  ↳ [#62434](https://github.com/ceph/ceph/pull/62434): [e303667](https://github.com/ceph/ceph/commit/e3036679b4b37509667e079fc4b10aec28ff24c3)
- Optimize the cleaning logic of radoslist, calculate bucket names and object keys in advance, and correct SLO list attribute checking.
  ↳ [#62418](https://github.com/ceph/ceph/pull/62418): [a3d367e](https://github.com/ceph/ceph/commit/a3d367ee61fa5c419c0df4c882f0419ce8e61539)
- Remove the keep_tail field from RGWObjState and transfer its management responsibilities inside the object handler.
  ↳ [#62656](https://github.com/ceph/ceph/pull/62656): [b94fcdf](https://github.com/ceph/ceph/commit/b94fcdfb6a2e01fd471e8c6ebd34145bebb78e20)
- Rename the handle_read_cluster callback function to handle_read_clusters, and modify its asynchronous execution logic.
  ↳ [#64195](https://github.com/ceph/ceph/pull/64195): [5e473c0](https://github.com/ceph/ceph/commit/5e473c0c5e5b87356257987f728197849a3e4639)
- Cleaned up usage of librbd::IoCtx to librados::IoCtx in Group.cc.
  ↳ [#64620](https://github.com/ceph/ceph/pull/64620): [1700ebb](https://github.com/ceph/ceph/commit/1700ebbeba5382cc3dcffc558d80a68177452532)
- Skip freeing of empty collections when freeing the allocator to avoid unnecessary calls.
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [c760786](https://github.com/ceph/ceph/commit/c76078660ec18c8dead2298068835b332e2153f9)
- Remove unnecessary return statements in OSD statistics repair function.
  ↳ [#60566](https://github.com/ceph/ceph/pull/60566): [98f50aa](https://github.com/ceph/ceph/commit/98f50aa61c1aa1a3bf74216a272f53de86be78e5)
- Adjusted RGW frontend discard buffer size from 1KB to 1MB.
  ↳ [#63711](https://github.com/ceph/ceph/pull/63711): [b81cf7a](https://github.com/ceph/ceph/commit/b81cf7aec15dfe8618e718e74fdf92d676b61f5e)
- Moved mClockScheduler constructor from source file to header file.
  ↳ [#62364](https://github.com/ceph/ceph/pull/62364): [6b04d7b](https://github.com/ceph/ceph/commit/6b04d7bc6cc38496279bc7cf0a29501c8209d31f)

### Test related
- Fixed multiple broken test cases in hybrid_allocator_test and added a new edge case test.
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [7b7550a](https://github.com/ceph/ceph/commit/7b7550a51e0aa6af12f0771613f3400169e25157)
- Improved allocator_replay_test, including adding assess_free command, fixing command line parameter initialization, optimizing debugging output and adding time-consuming printing for try_alloc command.
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [273c5fa](https://github.com/ceph/ceph/commit/273c5fae375cb6979af1688d1153296904a355cb), [48fa9fc](https://github.com/ceph/ceph/commit/48fa9fc96eec7d582183e937cb3ed8a009b72834), [791c3e5](https://github.com/ceph/ceph/commit/791c3e524569b1f07e8d2a9a9e2b5b9ef55c208b)
- Enhanced store_test, including adding deferred ops replay tests, test fixture helper methods, and waiting for collection removal to complete in CompressionTest.
  ↳ [#62122](https://github.com/ceph/ceph/pull/62122): [c812bf5](https://github.com/ceph/ceph/commit/c812bf57739bb69625910e55379889f36f130843) | [#62145](https://github.com/ceph/ceph/pull/62145): [0baa0dd](https://github.com/ceph/ceph/commit/0baa0dd2f6964490c079941a28a33bda6d495721)
- Improved mClock scheduler testing, including adding slow dequeue scenario testing, correcting priority parameters and specifying categories for multi-client operations.
  ↳ [#62364](https://github.com/ceph/ceph/pull/62364): [8965d23](https://github.com/ceph/ceph/commit/8965d23ccb3a1ea23bf7ade2b45f727a4a82a4d4), [cda7cb1](https://github.com/ceph/ceph/commit/cda7cb11c14cd54252d4599b2a1aaab0107891c1), [ffa7637](https://github.com/ceph/ceph/commit/ffa76372dc880fd2795584eb34c8b70688e63e14)
- Removed unit tests for deprecated cache tiering functionality.
  ↳ [#64588](https://github.com/ceph/ceph/pull/64588): [3d7787d](https://github.com/ceph/ceph/commit/3d7787d3b09fca9e4525b8831b512ecb24f27e28)
- Fixed a race condition in the test case and adjusted the number of wait notifications to correctly synchronize events.
  ↳ [#64738](https://github.com/ceph/ceph/pull/64738): [3a06f80](https://github.com/ceph/ceph/commit/3a06f80e089d34125ae53f104617a1b849fa05b1)
- Adjusted and enhanced the SnapdiffDeletionRecreation test case of LibCephFS to reproduce the snapdiff result fragmentation problem.
  ↳ [#65364](https://github.com/ceph/ceph/pull/65364): [2c2785b](https://github.com/ceph/ceph/commit/2c2785b6969959d7358ca29ee38e8078fa887ff1), [af04ac4](https://github.com/ceph/ceph/commit/af04ac464cf5b5800842f7bc2ac968879757aa44), [ae7c19a](https://github.com/ceph/ceph/commit/ae7c19afa7e1d2ade509ad509b89423dae3f02f3)

### Performance optimization
- Optimize RGW bucket operation performance, including incomplete multi-part upload checks and list operations.
  ↳ [#64464](https://github.com/ceph/ceph/pull/64464): [09567c8](https://github.com/ceph/ceph/commit/09567c8c290d52eb21e66cc1702d90379a032b3f) | [#62234](https://github.com/ceph/ceph/pull/62234): [a1d0058](https://github.com/ceph/ceph/commit/a1d0058ea2097a93efde635964bf7e0df861a2aa)
- Optimize MDS shutdown and reconnection performance, including actively waking up waiting threads and adjusting indicator message distribution.
  ↳ [#61513](https://github.com/ceph/ceph/pull/61513): [eeacf55](https://github.com/ceph/ceph/commit/eeacf55550c775441f004daa270696deb9be04cd) | [#61339](https://github.com/ceph/ceph/pull/61339): [b6f39f6](https://github.com/ceph/ceph/commit/b6f39f6f86784c23ae3cee52d4b5efd57e8992ff)
- Optimize DaemonStateIndex lock holding time to reduce GIL competition and thread delay.
  ↳ [#65463](https://github.com/ceph/ceph/pull/65463): [7afcdfb](https://github.com/ceph/ceph/commit/7afcdfbfd92f486296f44a86de8c782933791a79)
- Fixed memory leak in group_snap_remove_by_record and group_snap_rollback_by_record due to incorrect path not closing the image.
  ↳ [#64620](https://github.com/ceph/ceph/pull/64620): [b5406fe](https://github.com/ceph/ceph/commit/b5406fe232f0302b5278aee1d723d630dab4762e)
- Fixed an issue where the bytes_written_slow counter was incorrectly reported as 0 when writing asynchronously to BlueFS.
  ↳ [#66353](https://github.com/ceph/ceph/pull/66353): [95c0293](https://github.com/ceph/ceph/commit/95c029356536e81432869632daefd086c85af15c)
- Added performance counters for block device asynchronous discard operations to monitor the asynchronous discard status and the number of running discard threads.
  ↳ [#62481](https://github.com/ceph/ceph/pull/62481): [71bc601](https://github.com/ceph/ceph/commit/71bc60170e4e9e24677eb2d6df05aaadc7ffd9c2), [3850cb4](https://github.com/ceph/ceph/commit/3850cb4419fa9f4997d25f8c67ae1385dbe57683)

### Security related
- Replace variable length arrays with std::vector in CrushWrapper::do_rule to eliminate Clang compilation warnings and avoid potential stack overflow issues.
  ↳ [#62014](https://github.com/ceph/ceph/pull/62014): [344ffb4](https://github.com/ceph/ceph/commit/344ffb45914c3f592ac4a57ddb801ab34cf5d91c)
- Fixed a context cleanup issue in the persistent write log cache that could lead to memory leaks.
  ↳ [#64093](https://github.com/ceph/ceph/pull/64093): [733d14f](https://github.com/ceph/ceph/commit/733d14f5d988469eb46817a807f5be695f79867e)

### Documentation
- Added a man page to the rgw-restore-bucket-index tool and integrated it into the RPM packaging and documentation build system. The tool added -r, -g, -z, -t command line options to support multi-site configuration and specifying temporary file directories, and provide clear error prompts when there is insufficient disk space.
  ↳ [#64514](https://github.com/ceph/ceph/pull/64514): [75d2089](https://github.com/ceph/ceph/commit/75d2089b8e74d0005db7710019a8b19140fb0a64), [43492ed](https://github.com/ceph/ceph/commit/43492edfe40487387541e5c64404f62014c09871), [8b2343c](https://github.com/ceph/ceph/commit/8b2343cf88060f4381cdf9a59abb6f7d8e688b60) | [#64622](https://github.com/ceph/ceph/pull/64622): [2ef74b1](https://github.com/ceph/ceph/commit/2ef74b14bc1a4c36642052a5496ae43832a2c22c)
- Improved the formatting consistency of RADOS Gateway documentation, including uniform use of inline code tags, corrected indentation, removal of extra spaces, unified spelling and case of terms, and fixed command prompt and newline formatting.
  ↳ [#62910](https://github.com/ceph/ceph/pull/62910): [1a3f3c9](https://github.com/ceph/ceph/commit/1a3f3c9a8d2cd20821ebf3d45a452e18ccad4a64)
- Improved appearance and formatting of the vault.rst document, including unifying case, using automatic table of contents, adding code blocks and correcting language presentation.
  ↳ [#63230](https://github.com/ceph/ceph/pull/63230): [e8909de](https://github.com/ceph/ceph/commit/e8909deab655c8ff1d3ee9e897d7b6dfeb81f3c7)
- Fixed Sphinx warnings in documentation due to missing blank lines and indentation errors.
  ↳ [#63338](https://github.com/ceph/ceph/pull/63338): [60d6b5b](https://github.com/ceph/ceph/commit/60d6b5b713c87bdc8cbbdecccbfd4c6be1759ce5)
- Edited the prompt and indentation format in the Ceph Dashboard feature switch documentation.
  ↳ [#63397](https://github.com/ceph/ceph/pull/63397): [d30400e](https://github.com/ceph/ceph/commit/d30400e563fc764c99f3975cf73c16c92437282b)
- Format corrections were made to the cloud-transition.rst document, including indenting list items, filling in missing periods, adjusting inline preformatted text, and unifying the format of S3 API operation names.
  ↳ [#63449](https://github.com/ceph/ceph/pull/63449): [eea9d42](https://github.com/ceph/ceph/commit/eea9d42307635cffc5d032602fe33369466f1ecd)
- Fixed syntax errors in the placement-groups.rst document, and improved the description of PG autoscaling, target size, deviation value, recommended number of PGs per OSD, and data persistence. At the same time, the cache tiering document was updated to strengthen the warning that cache tiering should not be deployed in versions after Reef, and improved the English expression and format of the telemetry document.
  ↳ [#63650](https://github.com/ceph/ceph/pull/63650): [c3b988a](https://github.com/ceph/ceph/commit/c3b988aa9f603f4711fca43a7915b0286a83e21c) | [#63647](https://github.com/ceph/ceph/pull/63647): [457195a](https://github.com/ceph/ceph/commit/457195af07c2497ea5cae777a11b85fd43669b3b) | [#63831](https://github.com/ceph/ceph/pull/63831): [9223e3e](https://github.com/ceph/ceph/commit/9223e3e733a82ea1791b1d16be3a6a7dd3411020) | [#63769](https://github.com/ceph/ceph/pull/63769): [c1bcc79](https://github.com/ceph/ceph/commit/c1bcc7958f978b9240201007eb6c026ae5fa3f9a) | [#63772](https://github.com/ceph/ceph/pull/63772): [d10bfe3](https://github.com/ceph/ceph/commit/d10bfe3ce3fa28c0f143d8d150a603ffef2f27db)
- Rolled back the documentation changes on persistent_topic_size, and added a description of the pubsub_event_triggered counter in the notification performance statistics section.
  ↳ [#64179](https://github.com/ceph/ceph/pull/64179): [66c5146](https://github.com/ceph/ceph/commit/66c51461dadf4e79220f7e54d590100a6099bf90)
- Made a number of small improvements to the ceph-conf.rst document: fixed spelling errors, unified the case of section titles, used cross-reference links instead, changed the command prompt to privileged mode, and adjusted the code block format. At the same time, the description was clarified, the examples were updated, the wording was optimized, and the description of the ceph config show-with-defaults command was added, and ceph-conf was marked as a legacy command.
  ↳ [#64288](https://github.com/ceph/ceph/pull/64288): [b7d89f0](https://github.com/ceph/ceph/commit/b7d89f03411033e0f0f95e8b943129eedadf77d1) | [#63943](https://github.com/ceph/ceph/pull/63943): [b81a251](https://github.com/ceph/ceph/commit/b81a2515e03dc1f77a406d810fc1ead9794126b4) | [#65207](https://github.com/ceph/ceph/pull/65207): [65e01a4](https://github.com/ceph/ceph/commit/65e01a4d3bc925b79e9b7ad66db7f7e02390da76)
- Added a comment to the erasure-code.rst document to remind future maintainers not to add the "Erasure Coding Enhancements" chapter to the document before Tentacle version. At the same time, the content of the erasure coding document about overhead, recommended configuration and cache tiering instructions was improved.
  ↳ [#64868](https://github.com/ceph/ceph/pull/64868): [bdc22ba](https://github.com/ceph/ceph/commit/bdc22ba660e6bf81c5ecc5d0d0876a4013ebceeb) | [#62574](https://github.com/ceph/ceph/pull/62574): [7210906](https://github.com/ceph/ceph/commit/721090601590bacd3adbfa7f45a873aeb34609a6)
- Removed RGW metrics documentation page not applicable to reef version.
  ↳ [#66320](https://github.com/ceph/ceph/pull/66320): [339976f](https://github.com/ceph/ceph/commit/339976f65ed4adfb8af758d217bf13be6c7efef9)
- Updated the documentation on GDB debugging in the Developer Guide, and corrected the description of Teuthology test run descriptions and compilation optimization suggestions.
  ↳ [#63994](https://github.com/ceph/ceph/pull/63994): [881529c](https://github.com/ceph/ceph/commit/881529cd0b10d7dbfb858f5b6606b841a704bf8f)
- Added a note in the documentation: If there is an active snapshot schedule when deleting a volume, it may cause a Python traceback. It is recommended to disable and re-enable the snap_schedule Manager module to restore a stable state.
  ↳ [#61187](https://github.com/ceph/ceph/pull/61187): [14f3f4c](https://github.com/ceph/ceph/commit/14f3f4cb899b2eecc4cead4c2279ea3035d5be21)
- Added documentation for the ceph auth rotate command on how to rotate an entity's keys.
  ↳ [#58236](https://github.com/ceph/ceph/pull/58236): [df0863f](https://github.com/ceph/ceph/commit/df0863f781cd859d88e0af99cbda3b75a236b0a2)
- Added description of the --client_fs option in the ceph-fuse usage help, which is used to specify the file system to be mounted in a multi-file system cluster.
  ↳ [#61275](https://github.com/ceph/ceph/pull/61275): [5cacc45](https://github.com/ceph/ceph/commit/5cacc45afda4e4e69a1fca7ee29938888ff4d55f)
- Added health check instructions about the non-existent CRUSH location of the monitor in stretch mode in the documentation.
  ↳ [#62040](https://github.com/ceph/ceph/pull/62040): [bcf65ad](https://github.com/ceph/ceph/commit/bcf65adbabf06a0d4a0a21a9db1406eb408f07df)
- Added configuration instructions for pausing and resuming asynchronous cleaning threads (pause_purging) and cloning threads (pause_cloning) in the CephFS documentation, and supplemented the operation guide in failure recovery scenarios.
  ↳ [#62436](https://github.com/ceph/ceph/pull/62436): [7e31611](https://github.com/ceph/ceph/commit/7e316117c4127841a2161df98e6b96387b5da0d5)
- Added OAuth2 SSO configuration instructions to the Ceph Dashboard documentation, updated the reference and title of the SAML2 SSO chapter, and added instructions for using the --enable-auth flag.
  ↳ [#64034](https://github.com/ceph/ceph/pull/64034): [cb5687c](https://github.com/ceph/ceph/commit/cb5687caa37f0dc982a5edede0a353741ea54ad2)
- Fixed the description of the osd_max_scrubs option, removing the incorrect description that this option was ignored when using the mClock scheduler.
  ↳ [#62378](https://github.com/ceph/ceph/pull/62378): [0f960bd](https://github.com/ceph/ceph/commit/0f960bdba6263e5cf0d7a3cee5965c735812460a)
- Change the title of the "Monitoring OSD State" chapter in the document to "Monitoring OSD State During OSD Removal", and adjust the related description to more clearly point to the status query during the OSD removal process.
  ↳ [#61665](https://github.com/ceph/ceph/pull/61665): [6a5cadf](https://github.com/ceph/ceph/commit/6a5cadf70d581d5bbb440349a604781f11c9cd97)
- Clarified the description of S3 access methods in the documentation, replaced "vhost-style" with "path-style" and "virtual-hosted-style", and fixed an incorrect statement about AWS deprecated methods.
  ↳ [#61987](https://github.com/ceph/ceph/pull/61987): [b467489](https://github.com/ceph/ceph/commit/b467489b002ab4e1fc855b8daa1cdad1a79026d6)
- Updated documentation to note that the ceph fs volume create command has added --data-pool and --meta-pool options, allowing users to specify existing data pool and metadata pool names.
  ↳ [#63069](https://github.com/ceph/ceph/pull/63069): [af68a73](https://github.com/ceph/ceph/commit/af68a73d6ecc88ef08d57c59f3c60f5075a936c7)
- Added link reference to the section on pausing asynchronous threads in the CephFS documentation, and added instructions on disabling the volumes plugin section.
  ↳ [#62875](https://github.com/ceph/ceph/pull/62875): [226df3e](https://github.com/ceph/ceph/commit/226df3e3d72e8cbf1604c430497de1e3154d440a)
- Added suggestions about PG autoscaler in the upgrade documentation, and corrected some formats and links.
  ↳ [#62380](https://github.com/ceph/ceph/pull/62380): [0ff712f](https://github.com/ceph/ceph/commit/0ff712f9819c95cf5be59cfed129f8fee70cab45)
- Corrected the description of the many-to-many relationship between topics and notifications in the notification document, and clarified the issue of repeated statements.
  ↳ [#62405](https://github.com/ceph/ceph/pull/62405): [de37dfa](https://github.com/ceph/ceph/commit/de37dfa9b543ab1e33de04bbb60661c34c27f141)
- Added release notes for the `ceph osd rm-pg-upmap-primary` command, and added a troubleshooting section to the `read-balancer.rst` document to explain how to manually remove the pg-upmap-primary mapping.
  ↳ [#62468](https://github.com/ceph/ceph/pull/62468): [1f8b920](https://github.com/ceph/ceph/commit/1f8b9205548f99d13e322b773fa47de540662f04)
- Corrected the indentation of the OSD service chapter in the cephadm documentation, and updated the related instructions for device scanning, encryption deployment and WAL+DB configuration.
  ↳ [#62428](https://github.com/ceph/ceph/pull/62428): [0eaa161](https://github.com/ceph/ceph/commit/0eaa1616bf01db3d6a37b4f6c7fe91c7715f9a8b)
- Added description of `--zap` option to OSD removal documentation.
  ↳ [#62444](https://github.com/ceph/ceph/pull/62444): [9e462aa](https://github.com/ceph/ceph/commit/9e462aa692378b66b03392d7719579deb466e815)
- Update the release process documentation to explain that the new Jenkins task is used to automatically build the release container, replacing the previous complicated steps that required manual operation on the arm64 host.
  ↳ [#62613](https://github.com/ceph/ceph/pull/62613): [8baaebc](https://github.com/ceph/ceph/commit/8baaebc59f9d9ceb7d4810f6c95573fa2f1a2b87)
- Improved cloud-restore and cloud-transition documentation, added object recovery instructions, and optimized configuration examples and descriptions.
  ↳ [#62667](https://github.com/ceph/ceph/pull/62667): [92cf798](https://github.com/ceph/ceph/commit/92cf7989a535be65ab858ebdeb1a3af118543aaf)
- Improve the documentation of RGW and SNMP gateway, correct the terminology and unify the code format.
  ↳ [#62695](https://github.com/ceph/ceph/pull/62695): [152eb0c](https://github.com/ceph/ceph/commit/152eb0c1b2d26b55ff33ade5df0e7f4d83f0beb4)
- Improve Prometheus module documentation, unify terminology and correct grammar and formatting.
  ↳ [#62931](https://github.com/ceph/ceph/pull/62931): [83aced5](https://github.com/ceph/ceph/commit/83aced5defd2fc02359afb17571a1aa5f98e6607)
- Improved stretch-mode documentation, updated terminology, wording and formatting to make the description clearer and more accurate.
  ↳ [#63816](https://github.com/ceph/ceph/pull/63816): [ac6df72](https://github.com/ceph/ceph/commit/ac6df72c71574abedbc5f7dd82aaacb7e43e77b1)
- Added documentation for the `getpath` command for CephFS subvolume snapshots.
  ↳ [#62917](https://github.com/ceph/ceph/pull/62917): [5e07b5d](https://github.com/ceph/ceph/commit/5e07b5dc7ac6ccf6c22f2787065e93717dd4997a)
- Added man documentation for `rgw-gap-list` tool.
  ↳ [#63997](https://github.com/ceph/ceph/pull/63997): [c3676b9](https://github.com/ceph/ceph/commit/c3676b90eae3afcb8a313467b421151c626909d8)
- Added tips on security risks to be aware of when restarting the OSD service in the cephadm documentation.
  ↳ [#62797](https://github.com/ceph/ceph/pull/62797): [6d50dae](https://github.com/ceph/ceph/commit/6d50daecb4ce673331c9e56cbd7b976416c10695)
- Updated mClock configuration documentation to explain how to set or override the OSD's maximum IOPS capacity.
  ↳ [#63072](https://github.com/ceph/ceph/pull/63072): [8513761](https://github.com/ceph/ceph/commit/851376126d8f11d4e1929a628ea1beacdf9d7899)
- Updated `cephfs-journal-tool` documentation, corrected command syntax and added option descriptions.
  ↳ [#63109](https://github.com/ceph/ceph/pull/63109): [e288edb](https://github.com/ceph/ceph/commit/e288edb37284dc78639713e91e6dda06467e4522)
- Added link to Admin Ops API in Admin Capabilities section of RGW documentation.
  ↳ [#62882](https://github.com/ceph/ceph/pull/62882): [8eb0659](https://github.com/ceph/ceph/commit/8eb065941df581c644da69c070c45104ae1733cc)
- Added instructions for Admin and System users in RGW documentation.
  ↳ [#62882](https://github.com/ceph/ceph/pull/62882): [5bd90d0](https://github.com/ceph/ceph/commit/5bd90d038de71ada5e28d69df2631254591a34b0)
- Fixed RST syntax issues in `oidc.rst` document and added API document content.
  ↳ [#62990](https://github.com/ceph/ceph/pull/62990): [dd52983](https://github.com/ceph/ceph/commit/dd5298336377fa7115d7fab8dab7a6816ed80aa9)
- Improved the description text of `mgr_data` configuration item.
  ↳ [#63765](https://github.com/ceph/ceph/pull/63765): [8c4dacd](https://github.com/ceph/ceph/commit/8c4dacd7ad1459c5a7aeec3d69f20aca2df6b923)
- Improved CephFS image documentation, added command prompt and fixed syntax errors.
  ↳ [#63299](https://github.com/ceph/ceph/pull/63299): [8761783](https://github.com/ceph/ceph/commit/8761783af65a3466959d161c33d602d5f6dd805a) | [#63274](https://github.com/ceph/ceph/pull/63274): [0c30240](https://github.com/ceph/ceph/commit/0c30240649e2768f105a3e32ba1fd0df95e2a1cb) | [#63548](https://github.com/ceph/ceph/pull/63548): [687b438](https://github.com/ceph/ceph/commit/687b43847c925e42a6f787de288cc233e03cc909)
- Replace external links with `:ref:` hyperlinks in the document and fix broken links.
  ↳ [#63312](https://github.com/ceph/ceph/pull/63312): [697d093](https://github.com/ceph/ceph/commit/697d0935a229212ce9f40575b973e48c4a2cc9ec)
- Edit the `dashboard.rst` document, change the command prompt from `$` to `#` and add a new RGW command.
  ↳ [#63316](https://github.com/ceph/ceph/pull/63316): [e0369bd](https://github.com/ceph/ceph/commit/e0369bdbc91c0ba432d50c0e302e6910faad0bfb)
- Updated `x-amz-delete-if-unmodified-since` request header documenting S3 delete operations.
  ↳ [#64316](https://github.com/ceph/ceph/pull/64316): [aa30656](https://github.com/ceph/ceph/commit/aa3065671ac235c32d837604f96984133c6a0576)
- Improve STS configuration options documentation, use `confval` directive to render and add descriptions.
  ↳ [#63442](https://github.com/ceph/ceph/pull/63442): [a818cd2](https://github.com/ceph/ceph/commit/a818cd29f734ae26d5c00499b51583151e06b087)
- Improve the syntax and format of hello module documentation.
  ↳ [#63508](https://github.com/ceph/ceph/pull/63508): [4f9bca6](https://github.com/ceph/ceph/commit/4f9bca63d3bef784490636afdbad3195c56b7068)
- Fixed command prompt and formatting in Influx module documentation.
  ↳ [#63455](https://github.com/ceph/ceph/pull/63455): [03bb3f2](https://github.com/ceph/ceph/commit/03bb3f211a5131b5360490f905680243584f6d97)
- Improve the English expression of insights module documentation.
  ↳ [#63511](https://github.com/ceph/ceph/pull/63511): [f931bb2](https://github.com/ceph/ceph/commit/f931bb20f8d879898c5a0c18110dfa8a9a5ab468)
- Improved English description of iostat module documentation.
  ↳ [#63514](https://github.com/ceph/ceph/pull/63514): [77b68c5](https://github.com/ceph/ceph/commit/77b68c5fd98b8d8ad066d948375f5e3317f7349e)
- Improve the English expression and format of localpool module documentation.
  ↳ [#63551](https://github.com/ceph/ceph/pull/63551): [c06ecfd](https://github.com/ceph/ceph/commit/c06ecfd79c53fbba332e7a4a9177e01024496ead)
- Improved English description of MDS Autoscaler module documentation.
  ↳ [#63493](https://github.com/ceph/ceph/pull/63493): [25dabc4](https://github.com/ceph/ceph/commit/25dabc4b40166cda5eaea5899b5dc4e34d4fef60)
- Fixed command prompt and format errors in Prometheus module documentation.
  ↳ [#63590](https://github.com/ceph/ceph/pull/63590): [7a3e622](https://github.com/ceph/ceph/commit/7a3e622812c72c8eb0ece77c1ca77d0f6242dfcd)
- Improve format and description of command examples in rgw module documentation.
  ↳ [#63593](https://github.com/ceph/ceph/pull/63593): [cef2eab](https://github.com/ceph/ceph/commit/cef2eabe144dc319988f15291b35211eb1b69441)
- Improve command example formatting and indentation of telegraf module documentation.
  ↳ [#63612](https://github.com/ceph/ceph/pull/63612): [7370e3f](https://github.com/ceph/ceph/commit/7370e3f3ccc4b652f07681995e372b3fd1958cee)
- Improve the English expression and command example format of telemetry module documentation.
  ↳ [#63693](https://github.com/ceph/ceph/pull/63693): [5c20817](https://github.com/ceph/ceph/commit/5c20817a93074fca712b08997d7874d5a6413024)
- Several textual improvements to the RGW module documentation, including unifying terminology and correcting capitalization.
  ↳ [#63626](https://github.com/ceph/ceph/pull/63626): [8a11811](https://github.com/ceph/ceph/commit/8a11811df3590b527a70d6c4f1c439923234fe1f)
- Add suggestions about balancer settings to balancer documentation.
  ↳ [#63536](https://github.com/ceph/ceph/pull/63536): [a0ee8b6](https://github.com/ceph/ceph/commit/a0ee8b6b48a81cdfbbedd88fbaa6001f459b4263)
- Strengthen warning about deploying cache layering in versions after Reef.
  ↳ [#63696](https://github.com/ceph/ceph/pull/63696): [357d5cc](https://github.com/ceph/ceph/commit/357d5cc167743d337b44d029db0dd658f64b29aa)
- Updated dashboard feature toggle documentation to add nvmeof to the list of enabled features.
  ↳ [#63705](https://github.com/ceph/ceph/pull/63705): [008b06a](https://github.com/ceph/ceph/commit/008b06aa62901825f3a689cbc8008da35d89d845)
- Improve the English description of cli_api documentation.
  ↳ [#63744](https://github.com/ceph/ceph/pull/63744): [6da6265](https://github.com/ceph/ceph/commit/6da626537b0b9c0fa6138301119fc957dccecf8c)
- Improve the English description, format and privacy instructions of the telemetry module documentation.
  ↳ [#63775](https://github.com/ceph/ceph/pull/63775): [8a1cccc](https://github.com/ceph/ceph/commit/8a1cccc9fa291d880e0e724854c0848b82f837fa) | [#63778](https://github.com/ceph/ceph/pull/63778): [0ba6124](https://github.com/ceph/ceph/commit/0ba61248919ace88b5312b635c080faf1998dcde) | [#64344](https://github.com/ceph/ceph/pull/64344): [4bdbcf1](https://github.com/ceph/ceph/commit/4bdbcf15cfd9bdf771f458b4fbfd4007398f4700) | [#63810](https://github.com/ceph/ceph/pull/63810): [12b3e71](https://github.com/ceph/ceph/commit/12b3e719da634362efb11f85a11e8fd3906862b1)
- Clarify description of rgw-multitenancy behavior in RADOSGW documentation.
  ↳ [#63813](https://github.com/ceph/ceph/pull/63813): [ef06a20](https://github.com/ceph/ceph/commit/ef06a2085c3c454bb192b0dc4a2667bf514436a3)
- Updated stretch-mode documentation, adopted suggestions and corrected many descriptions.
  ↳ [#63850](https://github.com/ceph/ceph/pull/63850): [2b4e3a2](https://github.com/ceph/ceph/commit/2b4e3a25d0c18abcc1688d767c1d7892bf64494f)
- Improve the English expression of the osd_deep_scrub_interval_cv configuration item description.
  ↳ [#63956](https://github.com/ceph/ceph/pull/63956): [84daca4](https://github.com/ceph/ceph/commit/84daca4bf8dc6aeace4f30a935d29410c2163841)
- Improve the English expression, format and description of telemetry module documentation.
  ↳ [#63865](https://github.com/ceph/ceph/pull/63865): [ee9c739](https://github.com/ceph/ceph/commit/ee9c7392e6b69f3e7b1c59060ac2d4da9c9be723) | [#63868](https://github.com/ceph/ceph/pull/63868): [d37fdc6](https://github.com/ceph/ceph/commit/d37fdc6d20583c8fd80e2b536bd2c17c10228975) | [#63906](https://github.com/ceph/ceph/pull/63906): [ee81992](https://github.com/ceph/ceph/commit/ee81992ee331b0af795d21ef2252d0bce18160ef)
- Unify the description format of key rotation commands in user management documents.
  ↳ [#63893](https://github.com/ceph/ceph/pull/63893): [f73a033](https://github.com/ceph/ceph/commit/f73a03325de643872247e04803ae359143b68583)
- Added troubleshooting tips and related links to pools.rst documentation.
  ↳ [#63847](https://github.com/ceph/ceph/pull/63847): [bf2f30e](https://github.com/ceph/ceph/commit/bf2f30e9302400a4889dc15fc7804b1dbe8638cc) | [#63862](https://github.com/ceph/ceph/pull/63862): [91acd1a](https://github.com/ceph/ceph/commit/91acd1abf99a3985afd06e8b21b41e960ed06fd5)
- Updated cache layering documentation to recommend migrating legacy deployments.
  ↳ [#64497](https://github.com/ceph/ceph/pull/64497): [8a3da6e](https://github.com/ceph/ceph/commit/8a3da6e580adec6ab976bb11f6b37362a9d0f6c4)
- Polish the first hundred lines of the cloud-transition documentation.
  ↳ [#64025](https://github.com/ceph/ceph/pull/64025): [6eb1829](https://github.com/ceph/ceph/commit/6eb18290e7619753c6ae26b981997a9b5a82b1ea)
- Updated deprecation notes for the inline data feature in the CephFS experimental features documentation.
  ↳ [#63949](https://github.com/ceph/ceph/pull/63949): [2ad8a3c](https://github.com/ceph/ceph/commit/2ad8a3c7a944099d34b0725abc3359f9af171c90)
- Added instructions for using first-damage.py in CephFS disaster recovery documentation.
  ↳ [#63978](https://github.com/ceph/ceph/pull/63978): [6295f0b](https://github.com/ceph/ceph/commit/6295f0b8efd8c57c9beef7d64195681c40adcda1)
- Clarify the behavior of the --bucket and --uid options when setting bucket quota.
  ↳ [#64022](https://github.com/ceph/ceph/pull/64022): [0658154](https://github.com/ceph/ceph/commit/06581548c64b3f4a01e98ed1cea5418f5f16a927)
- Updated performance statistics metric list and description in RADOS Gateway notification documentation.
  ↳ [#64156](https://github.com/ceph/ceph/pull/64156): [7dfe147](https://github.com/ceph/ceph/commit/7dfe1470e1b82b28f6da0830a90bf223511636ca) | [#64127](https://github.com/ceph/ceph/pull/64127): [fb6ec67](https://github.com/ceph/ceph/commit/fb6ec675cd47ed3c0c194e5b087d36a1c618cdbf) | [#64140](https://github.com/ceph/ceph/pull/64140): [c25d52a](https://github.com/ceph/ceph/commit/c25d52a28fc4984d7e42df599026bc7b2064f139) | [#64114](https://github.com/ceph/ceph/pull/64114): [c981ee5](https://github.com/ceph/ceph/commit/c981ee577fa731385a23feeede3f91873418f421)
- Added comprehensive documentation for configuration options of the ceph-mgr module.
  ↳ [#64397](https://github.com/ceph/ceph/pull/64397): [868ae02](https://github.com/ceph/ceph/commit/868ae0201606b093b8eaaf7623f8b450f9e340e3)
- Removed outdated manual enablement instructions from the crash module documentation.
  ↳ [#64285](https://github.com/ceph/ceph/pull/64285): [e8ebf28](https://github.com/ceph/ceph/commit/e8ebf28688b2ee8afc9329edd0e5741a0c1f989c)
- Added command instructions for restoring client.admin permissions in the documentation.
  ↳ [#64322](https://github.com/ceph/ceph/pull/64322): [5bfbe0d](https://github.com/ceph/ceph/commit/5bfbe0d446571c31508680d5463a6f52b3388535)
- Added descriptions of rgw_enable_lc_threads and rgw_enable_gc_threads configuration items in the document.
  ↳ [#64339](https://github.com/ceph/ceph/pull/64339): [39078e8](https://github.com/ceph/ceph/commit/39078e8b724ba50eb78b658287d5dfe75faa180e)
- Removed the deprecated clonedata command from the rados man page.
  ↳ [#64394](https://github.com/ceph/ceph/pull/64394): [b097f0d](https://github.com/ceph/ceph/commit/b097f0d3baf6c0ab02d56d8555e48cf20c22ce9c)
- Updated documentation to clarify that MS Windows client support is "best effort" and the future is uncertain.
  ↳ [#64482](https://github.com/ceph/ceph/pull/64482): [3e1a07f](https://github.com/ceph/ceph/commit/3e1a07ff4318da6093ef42dac87635cce18529cf)
- Updated the description of notification types in the mgr module documentation to emphasize that the module needs to explicitly declare the NOTIFY_TYPES list to receive notifications.
  ↳ [#64531](https://github.com/ceph/ceph/pull/64531): [2b5bb44](https://github.com/ceph/ceph/commit/2b5bb44ce2fd2073e349a6f2fc65c2181ee7d688)
- Improved CephFS FUSE mounting documentation, updated command line parameter descriptions and uninstallation prompts.
  ↳ [#64473](https://github.com/ceph/ceph/pull/64473): [b521651](https://github.com/ceph/ceph/commit/b521651bb9233710191c6418efe0f9b0c23ab5f9)
- In the Windows client documentation for CephFS and RBD, added note block for operating system recommended client package support notes.
  ↳ [#64493](https://github.com/ceph/ceph/pull/64493): [a72c9f5](https://github.com/ceph/ceph/commit/a72c9f5820289c51571844fb978a44025c955ab7)
- Edited the "Datapool Corruption" chapter in the CephFS Disaster Recovery documentation.
  ↳ [#64609](https://github.com/ceph/ceph/pull/64609): [5a0f5f9](https://github.com/ceph/ceph/commit/5a0f5f90985743a2131c4ad437cfdc2a3870066e)
- Based on community feedback, edited the description of life cycle settings in the RGW configuration reference document.
  ↳ [#64648](https://github.com/ceph/ceph/pull/64648): [dc013c7](https://github.com/ceph/ceph/commit/dc013c789af121392e5c5d6f8c1a3ed2e36c6669)
- Edited CephFS disaster recovery documentation to improve the description of the impact of losing the data pool PG.
  ↳ [#64645](https://github.com/ceph/ceph/pull/64645): [3c7e633](https://github.com/ceph/ceph/commit/3c7e6333173b21320bfbaad56ddb9919cb8730d5)
- Edited the instructions for using ceph-dokan in the CephFS documentation, improving the wording and format.
  ↳ [#64736](https://github.com/ceph/ceph/pull/64736): [4ed6e4e](https://github.com/ceph/ceph/commit/4ed6e4e5a56e1ed326f66a4f6ef0ea01dc1e919d)
- Improved description of dirstat and nodirstat options in mount.ceph man page.
  ↳ [#65184](https://github.com/ceph/ceph/pull/65184): [65fc158](https://github.com/ceph/ceph/commit/65fc158c80e344d5b624696038560054e06b6a57)
- Edited the ceph-dokan section of the CephFS documentation, improving the description of credentials, offloading and restrictions.
  ↳ [#64760](https://github.com/ceph/ceph/pull/64760): [241e892](https://github.com/ceph/ceph/commit/241e892edc670d441a2c127dc8226c47c5b1f001)
- Updated CephFS disaster recovery documentation, added notes on offline file systems before using the metadata repair tool, and improved recovery step instructions.
  ↳ [#65058](https://github.com/ceph/ceph/pull/65058): [c39401b](https://github.com/ceph/ceph/commit/c39401b8de7205e2c580f2d0a04e2423ef73bb07)
- Revised the CephFS troubleshooting document based on feedback, optimizing wording and readability.
  ↳ [#64879](https://github.com/ceph/ceph/pull/64879): [e49ed6b](https://github.com/ceph/ceph/commit/e49ed6bdca15e4dc55536730a2627eedab9d31f2)
- Edited the "Avoiding Recovery Roadblocks" section of the "Stuck During Recovery" chapter in the CephFS Troubleshooting Documentation for text polish and clarification.
  ↳ [#64904](https://github.com/ceph/ceph/pull/64904): [d69cb62](https://github.com/ceph/ceph/commit/d69cb623cccf91694ba41f3ef66014dc90140d8f)
- Edited the "Slow/Stuck Operations" section of the CephFS troubleshooting documentation.
  ↳ [#64901](https://github.com/ceph/ceph/pull/64901): [a2f95a9](https://github.com/ceph/ceph/commit/a2f95a9c2ac43859099582d7d48709bf21129735)
- Edited the section on MDS slow requests in the CephFS troubleshooting documentation.
  ↳ [#65088](https://github.com/ceph/ceph/pull/65088): [6d0be8d](https://github.com/ceph/ceph/commit/6d0be8d4b6a437181279a49f576127c4110a6ebd)
- Edited the section on accelerating MDS log pruning in the CephFS troubleshooting documentation, improving the description and adding a cross-reference.
  ↳ [#65037](https://github.com/ceph/ceph/pull/65037): [beae0cf](https://github.com/ceph/ceph/commit/beae0cf14b463b3bb36bd79b8087bf100fdfbdb2)
- Updated the description of the "RADOS Health" section in the CephFS troubleshooting documentation and added a cross-reference tag to the RADOS troubleshooting index page.
  ↳ [#65041](https://github.com/ceph/ceph/pull/65041): [75bbda3](https://github.com/ceph/ceph/commit/75bbda3c5146677c1c2eb2216595e72351e966b4)
- Improved description of the MDS section in the CephFS troubleshooting documentation.
  ↳ [#65091](https://github.com/ceph/ceph/pull/65091): [92607ab](https://github.com/ceph/ceph/commit/92607abfbe55313dc94d7be7f42c158027665c96)
- Added instructions and cross-references about ceph-fuse in the CephFS troubleshooting documentation.
  ↳ [#65126](https://github.com/ceph/ceph/pull/65126): [6bed6f6](https://github.com/ceph/ceph/commit/6bed6f69bcf3b52c2607d0fa6cfa032e39d157e4)
- Edited description of the debug output section in the CephFS troubleshooting documentation.
  ↳ [#65044](https://github.com/ceph/ceph/pull/65044): [7f87b04](https://github.com/ceph/ceph/commit/7f87b04f2073f198a28e6d434bf111518ed112ec)
- Clarified the diagnostic steps in the "Kernel mount debugging" section of the CephFS troubleshooting documentation.
  ↳ [#65094](https://github.com/ceph/ceph/pull/65094): [4b7305f](https://github.com/ceph/ceph/commit/4b7305f6b403d68a9bbaab48354928969f7b9f67)
- Edited the content of the "Slow requests" chapter in the CephFS troubleshooting document.
  ↳ [#65078](https://github.com/ceph/ceph/pull/65078): [0f6b10a](https://github.com/ceph/ceph/commit/0f6b10a55dcd4c59eae62f84cefc4d142bce111c)
- Edited wording and formatting of the "Disconnected+Remounted FS" section in the CephFS troubleshooting documentation.
  ↳ [#65097](https://github.com/ceph/ceph/pull/65097): [0309727](https://github.com/ceph/ceph/commit/0309727544abd087c0d95339534fe436f4097629)
- Edited the description of the "Mount 5 Error" and "Mount 12 Error" sections in the CephFS troubleshooting documentation.
  ↳ [#65047](https://github.com/ceph/ceph/pull/65047): [c2d9687](https://github.com/ceph/ceph/commit/c2d9687ad92bc3584cfa5d2a461a746bad30dbdd)
- Added kernel driver debug log instructions in the "Dynamic Debugging" chapter of the CephFS Troubleshooting Document.
  ↳ [#65026](https://github.com/ceph/ceph/pull/65026): [ed04866](https://github.com/ceph/ceph/commit/ed04866060de183cba30f3abbdd0407c30540e67)
- Edited the "In-memory log dumps" section of the CephFS troubleshooting documentation.
  ↳ [#65123](https://github.com/ceph/ceph/pull/65123): [d536ec3](https://github.com/ceph/ceph/commit/d536ec3b7ab04267992367d3dcf81ba7b4940d7f)
- Updated the CephFS quota document to remind users to set the client authentication capability flag when configuring quotas.
  ↳ [#65083](https://github.com/ceph/ceph/pull/65083): [aadb1e9](https://github.com/ceph/ceph/commit/aadb1e9e70332465114a45fad7a2752df8b79ef7)
- Added NVMe-oF Monitor Client chapter and its configuration items in the document.
  ↳ [#65138](https://github.com/ceph/ceph/pull/65138): [9ea615d](https://github.com/ceph/ceph/commit/9ea615d35c44df9557dcc8c581c0cf58bad6ba89)
- Updated the blkin.rst document, adding instructions that package-based deployment requires installing packages to avoid coredump.
  ↳ [#65212](https://github.com/ceph/ceph/pull/65212): [3bcbcee](https://github.com/ceph/ceph/commit/3bcbceefa990fe591e432c1d3b58fcc869c94918)
- Adjusted the position of the "Slow Requests (MDS)" chapter in the CephFS troubleshooting document.
  ↳ [#65201](https://github.com/ceph/ceph/pull/65201): [4c97952](https://github.com/ceph/ceph/commit/4c97952fc4cc268bfe2e2eebc21b3a5b5e8e92be)
- Improved health check documentation, updated descriptions of multiple alarms and command examples.
  ↳ [#65239](https://github.com/ceph/ceph/pull/65239): [d836c71](https://github.com/ceph/ceph/commit/d836c7167e5a9b48467f89f9b6a197a5db529040)
- Updated description of the "Disconnect and remount the file system" section in the CephFS troubleshooting documentation.
  ↳ [#65380](https://github.com/ceph/ceph/pull/65380): [c8dd355](https://github.com/ceph/ceph/commit/c8dd355bd00cbd4adeae73df0824c37320bdcf39)
- Added explanation and troubleshooting steps to the documentation about the kernel client not supporting pg-upmap-primary.
  ↳ [#65440](https://github.com/ceph/ceph/pull/65440): [60984d4](https://github.com/ceph/ceph/commit/60984d44e4a7f15262c23f6673c8eaeeb40513ec)
- Removed cloud-restore documentation from reef branch.
  ↳ [#65638](https://github.com/ceph/ceph/pull/65638): [f1ef88a](https://github.com/ceph/ceph/commit/f1ef88ad126063880d2c8691eb4ea3f674e1443f)
- Added a new chapter on cloning settings in the RBD configuration reference document and updated related option descriptions.
  ↳ [#66173](https://github.com/ceph/ceph/pull/66173): [d4bbdcd](https://github.com/ceph/ceph/commit/d4bbdcd34f0d21238851f890828ec52289aa7d03)
- Rolled back OAuth2 SSO documentation and updated SSO related documentation references.
  ↳ [#66796](https://github.com/ceph/ceph/pull/66796): [0038b1b](https://github.com/ceph/ceph/commit/0038b1b5746027013fd08f42fe4bfe958b664044)
- Rolled back the configuration section in rgw.rst that does not apply to the Reef version.
  ↳ [#66971](https://github.com/ceph/ceph/pull/66971): [cb131d0](https://github.com/ceph/ceph/commit/cb131d00450fe06c96d441c073de8c894ee1e0a8)

### Build/CI
- Repair CentOS/RPM build environment: add git dependency, enable CRB repository, fix build failure caused by missing manpage.
  ↳ [#64658](https://github.com/ceph/ceph/pull/64658): [7c05f07](https://github.com/ceph/ceph/commit/7c05f07cf6cd98e01f2668bf3b8eef6a8ce7b997) | [#63999](https://github.com/ceph/ceph/pull/63999): [bbe8005](https://github.com/ceph/ceph/commit/bbe80059ef005fa762f6a2a05107f55b84f25cc4) | [#64130](https://github.com/ceph/ceph/pull/64130): [48b7d75](https://github.com/ceph/ceph/commit/48b7d75d18ebd4ec969ca9a065b3b472fc42efb6)
- Add optional NPM cache directory support for dashboard front-end builds to improve build efficiency.
  ↳ [#65188](https://github.com/ceph/ceph/pull/65188): [5777cc5](https://github.com/ceph/ceph/commit/5777cc5dabcdf8c175668a047d35555733091e7c)
- Fixed cheroot dependency version to solve test timeout issue in Python 3.10 environment.
  ↳ [#65637](https://github.com/ceph/ceph/pull/65637): [a1b0c4f](https://github.com/ceph/ceph/commit/a1b0c4fa7a4356ced67c4c1de1a49a2b8afe8106), [f345817](https://github.com/ceph/ceph/commit/f34581771395b4a05350de34e7861a65bb429845)
- Improve the security and reproducibility of GitHub Actions workflows by fixing action references to SHA hashes.
  ↳ [#65759](https://github.com/ceph/ceph/pull/65759): [afafbf0](https://github.com/ceph/ceph/commit/afafbf0e336856630a5b8c466ea768c68ed2acd1)
- Adjust unit test build configuration, replace unittest_deferred with test_corrupt_deferred and remove its registration.
  ↳ [#66359](https://github.com/ceph/ceph/pull/66359): [cdce7df](https://github.com/ceph/ceph/commit/cdce7dfb4618bfaf1003210c4591fd351297a621)
- Improved the CI workflow of Read the Docs document building, supporting retries triggered by comments and simplifying steps.
  ↳ [#63616](https://github.com/ceph/ceph/pull/63616): [daf67f1](https://github.com/ceph/ceph/commit/daf67f158fa516cc54260092bd4bb14d071c4afd), [5404cc5](https://github.com/ceph/ceph/commit/5404cc54718e4f5b8b4b743816f99529555dfb0b)
- Fallback fix on lxml version to revert to using system packages.
  ↳ [#64612](https://github.com/ceph/ceph/pull/64612): [955df9d](https://github.com/ceph/ceph/commit/955df9d1c13c8e1c78fcff067e34d35a68243126)
- Fixed the ownership issue of nodeenv downloaded files and the CMake command escaping issue in the dashboard front-end build.
  ↳ [#65188](https://github.com/ceph/ceph/pull/65188): [4d779d8](https://github.com/ceph/ceph/commit/4d779d8e372d7a4882abb3095be83c0133955513), [bc2a565](https://github.com/ceph/ceph/commit/bc2a5652c7894692ee2bea99ea1003eb85c60161)
- Adjust the build configuration of unittest_fault_injector, remove unit-main dependency and use GTest::Main instead.
  ↳ [#63979](https://github.com/ceph/ceph/pull/63979): [a31a7ec](https://github.com/ceph/ceph/commit/a31a7ec5bd912a2b6959d600d7cd4399875efac8)
- Clean up document build dependencies, remove typed-ast and incompatible sphinxcontrib-seqdiag packages that have stopped maintaining maintenance.
  ↳ [#64400](https://github.com/ceph/ceph/pull/64400): [c3fa4a2](https://github.com/ceph/ceph/commit/c3fa4a2791bf6ba0e0a01d209fc8e38532baacb4) | [#67528](https://github.com/ceph/ceph/pull/67528): [4b9be37](https://github.com/ceph/ceph/commit/4b9be377cf32e93b371d58c91fb4a5b6069f1dc9)
- Fixed pip version below 25.3 to resolve an issue where Read the Docs build failed due to PEP 517 requirements.
  ↳ [#66118](https://github.com/ceph/ceph/pull/66118): [40c6049](https://github.com/ceph/ceph/commit/40c6049f5a0efa0e7516c04088142800ba3a903f)

### Maintenance
- Fixed an issue where the expired message was incorrectly printed when the rbd trash mv command failed.
  ↳ [#62967](https://github.com/ceph/ceph/pull/62967): [843b67f](https://github.com/ceph/ceph/commit/843b67fd949f59e219eebb333eb6a51e86b22412)
- Adjusted log output format in AvlAllocator and HybridAllocator to improve debugging readability.
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [a1d7e67](https://github.com/ceph/ceph/commit/a1d7e675581691c66a55fbea84ff20efac78efc4), [348bf03](https://github.com/ceph/ceph/commit/348bf030a5024887137e6270965393dc4924f78d)
- Added more detailed contextual information to multiple debug logs in MDS, Mon and RGW.
  ↳ [#61518](https://github.com/ceph/ceph/pull/61518): [7b25c66](https://github.com/ceph/ceph/commit/7b25c6641e05e4a1c39e22b24d899178d3486a73) | [#60563](https://github.com/ceph/ceph/pull/60563): [5c59df8](https://github.com/ceph/ceph/commit/5c59df841d75d7032288ad5a504f15a6a7df6312) | [#61978](https://github.com/ceph/ceph/pull/61978): [80551c2](https://github.com/ceph/ceph/commit/80551c23e8e5ee362ace5a990e80575392949d41) | [#62591](https://github.com/ceph/ceph/pull/62591): [9d84f25](https://github.com/ceph/ceph/commit/9d84f25514b9a7940d1ca077f65b9a739e1bc449)
- Adjusted the dump format of MonMap and pg_pool_t to support Python test script parsing, and added a stretch pool field.
  ↳ [#60630](https://github.com/ceph/ceph/pull/60630): [9a775a1](https://github.com/ceph/ceph/commit/9a775a1c90d3651f49d19cdb52ceb662c9cf752c)
- Updated the Ceph version number from 18.2.7 to 18.2.8, and updated the Debian packaging change log.
  ↳ [#67762](https://github.com/ceph/ceph/pull/67762): [efac5a5](https://github.com/ceph/ceph/commit/efac5a54607c13fa50d4822e50242b86e6e446df)

### Others
- Removed the scaling factor in PGMap when calculating the pool's maximum free space to avoid incorrectly reporting more free space when the OSD is marked down but not out.
  ↳ [#61320](https://github.com/ceph/ceph/pull/61320): [1ee12b4](https://github.com/ceph/ceph/commit/1ee12b467c9b923d8d091fe9a9198a402c034ebd)
- Explicitly specify the use of the AVL allocator in object storage test cases to ensure that test results depend on the behavior of that allocator.
  ↳ [#62539](https://github.com/ceph/ceph/pull/62539): [4a95620](https://github.com/ceph/ceph/commit/4a9562024920280d96eac22d97ac24146c7472e6)
- Added test cases for sequence number push for BlueFS log extension.
  ↳ [#61653](https://github.com/ceph/ceph/pull/61653): [e785ef2](https://github.com/ceph/ceph/commit/e785ef23339eba41bf786a68bba845f1916feb61)
- Fixed case error in bluestore configuration reference documentation.
  ↳ [#62261](https://github.com/ceph/ceph/pull/62261): [8ccd7ab](https://github.com/ceph/ceph/commit/8ccd7ab5969056eb5ee6fe0e18e5936099a04996) | [#62291](https://github.com/ceph/ceph/pull/62291): [a1483ab](https://github.com/ceph/ceph/commit/a1483aba6b965b432c4e6477e04e2a0d7155331e)
- Fixed the title format of the "Exiting Stretch Mode" chapter in stretch mode documentation.
  ↳ [#60630](https://github.com/ceph/ceph/pull/60630): [85e8927](https://github.com/ceph/ceph/commit/85e8927e78cb5ff90da339c46241aa0a7a75fb39)
- Updated link to backporter manual in development workflow documentation.
  ↳ [#63991](https://github.com/ceph/ceph/pull/63991): [cf96522](https://github.com/ceph/ceph/commit/cf96522940afdbc89282c32e540fd85c3864b5e9)
- Removed a marketing description from the architecture documentation.
  ↳ [#61615](https://github.com/ceph/ceph/pull/61615): [4ffc52c](https://github.com/ceph/ceph/commit/4ffc52ced6eee10525c11298a1fe0a3a5ceaf847)
- Delete redundant license files in the src/dmclock directory.
  ↳ [#62364](https://github.com/ceph/ceph/pull/62364): [a8b9865](https://github.com/ceph/ceph/commit/a8b9865cb02d5226aa9159140fe126b029ab00a7)
- Improved wording, formatting and content in RGW layout documentation.
  ↳ [#62450](https://github.com/ceph/ceph/pull/62450): [0e79260](https://github.com/ceph/ceph/commit/0e792608d0dfd0dabb4c326341311cd41896586a) | [#63000](https://github.com/ceph/ceph/pull/63000): [e817cbb](https://github.com/ceph/ceph/commit/e817cbb9cac5d751ccda9429cef1ba9abbe959f0)
- Added setting instructions for the configuration item mon_warn_pg_not_scrubbed_ratio to guide users to set this value on the Manager.
  ↳ [#62552](https://github.com/ceph/ceph/pull/62552): [0667efe](https://github.com/ceph/ceph/commit/0667efea8a0fd475638b430a351a66fa6828d189)
- Fixed wording in ceph-conf.rst document to be more accurate.
  ↳ [#62621](https://github.com/ceph/ceph/pull/62621): [e5f961f](https://github.com/ceph/ceph/commit/e5f961ff7f9f33edd0fb9535607f18648fc3926d)
- Improved the English description of the "Maintenance Mode" chapter in the cephadm documentation.
  ↳ [#63496](https://github.com/ceph/ceph/pull/63496): [bc39f0c](https://github.com/ceph/ceph/commit/bc39f0c19fe3d0dcf75964c1b3b5cafd110520d0)
- Fixed a typo in a command in the cephadm documentation, changing confg to config.
  ↳ [#62645](https://github.com/ceph/ceph/pull/62645): [d449ce2](https://github.com/ceph/ceph/commit/d449ce23973ca764684607fd5423c8254f929be0)
- Updated RadosGW related documents, fixed issues such as linking, formatting, typesetting, punctuation and indentation.
  ↳ [#62857](https://github.com/ceph/ceph/pull/62857): [b02acfe](https://github.com/ceph/ceph/commit/b02acfef02b9ced1b087b98593f5fbbe24ee2eb8) | [#62835](https://github.com/ceph/ceph/pull/62835): [a5d4a3e](https://github.com/ceph/ceph/commit/a5d4a3e4648f778896307e2d45cb0c7370e537f1) | [#62811](https://github.com/ceph/ceph/pull/62811): [65f95a3](https://github.com/ceph/ceph/commit/65f95a3d0334e691b343cef220c9669d1cc6a34e) | [#63701](https://github.com/ceph/ceph/pull/63701): [6d9bc49](https://github.com/ceph/ceph/commit/6d9bc49f98bd65f181172ba61a904b7e29f8293a)
- Fixed typo of BlueStore in option description.
  ↳ [#64218](https://github.com/ceph/ceph/pull/64218): [7c99e5f](https://github.com/ceph/ceph/commit/7c99e5ff3c5404d1712a0eeb02b238ebfe838e2a)
- Fixed CLI command formatting and rendering issues in RGW layout documentation.
  ↳ [#63916](https://github.com/ceph/ceph/pull/63916): [bd4e850](https://github.com/ceph/ceph/commit/bd4e850fb1ac38597a81334171e4b3f061604648)
- Fixed markup errors in Cephadm RGW documentation and eliminated build warnings.
  ↳ [#63074](https://github.com/ceph/ceph/pull/63074): [fccb609](https://github.com/ceph/ceph/commit/fccb60922e80b0a446759ddfc8d1266b491277be)
- Improve the format and chapter structure of RGW data cache documentation.
  ↳ [#64476](https://github.com/ceph/ceph/pull/64476): [2414bd8](https://github.com/ceph/ceph/commit/2414bd8ac88a9f0b8ea81385a118bb791569eb8f)
- Improved the command prompt and English expressions of the administrator guide documentation.
  ↳ [#63208](https://github.com/ceph/ceph/pull/63208): [e7e7847](https://github.com/ceph/ceph/commit/e7e7847d269a466c72ef59a7562cafee80583c8c)
- Fixed command format for disabling PG autoscaler in Cephadm upgrade documentation.
  ↳ [#63148](https://github.com/ceph/ceph/pull/63148): [6d23bcc](https://github.com/ceph/ceph/commit/6d23bcc188dbf6232627a951ad9a351ab79ea92b)
- Improved format, wording and linking of dynamic sharding documentation.
  ↳ [#64059](https://github.com/ceph/ceph/pull/64059): [0f0a9d6](https://github.com/ceph/ceph/commit/0f0a9d642c419374b168f52113a40e617cec0c31)
- Improved display format of curl command examples in Ceph API documentation.
  ↳ [#63198](https://github.com/ceph/ceph/pull/63198): [bb1f6c0](https://github.com/ceph/ceph/commit/bb1f6c052fe38cc9695e90ca7ab145eb59c0d7d1)
- Fixed English expression and formatting of Ceph Manager alert module documentation.
  ↳ [#63201](https://github.com/ceph/ceph/pull/63201): [aa8d4da](https://github.com/ceph/ceph/commit/aa8d4dab202585d6e6f04be63d899e21d751c12b)
- Improved description and command example format of CLI API module documentation.
  ↳ [#63690](https://github.com/ceph/ceph/pull/63690): [ea00c39](https://github.com/ceph/ceph/commit/ea00c399a89424d39182908a3aac6619bac2a2cd)
- Fixed formatting issues in CephFS image development documentation.
  ↳ [#63251](https://github.com/ceph/ceph/pull/63251): [7af2a78](https://github.com/ceph/ceph/commit/7af2a784620d1acf2d2e6bfa877c1292baa0a882)
- Corrected the list format in monitoring documents.
  ↳ [#63542](https://github.com/ceph/ceph/pull/63542): [b55afe4](https://github.com/ceph/ceph/commit/b55afe4d3a86dc3490ff57c66eda1e6bb16225e0)
- Fixed cross-reference link structure of directives in CephFS documentation.
  ↳ [#63545](https://github.com/ceph/ceph/pull/63545): [74a72a5](https://github.com/ceph/ceph/commit/74a72a548caf26f34001a0f130db2ff8da889869)
- Improved command prompt and English expression of crash.rst document.
  ↳ [#63539](https://github.com/ceph/ceph/pull/63539): [25790d4](https://github.com/ceph/ceph/commit/25790d428df50c620a4babd8577964cc16467c8d)
- Improve the format and text polish of CephFS image documentation.
  ↳ [#63468](https://github.com/ceph/ceph/pull/63468): [d9cb98a](https://github.com/ceph/ceph/commit/d9cb98af842d1d6f87e78b2c4f89358f63aeb9d3)
- Fix command prompt and output format for Ceph Manager debug plugin documentation.
  ↳ [#63394](https://github.com/ceph/ceph/pull/63394): [5137229](https://github.com/ceph/ceph/commit/513722973b234991efb74c15b15fa2c8cdf6b30d)
- Improved syntax and formatting of Ceph Dashboard MOTD documentation.
  ↳ [#63403](https://github.com/ceph/ceph/pull/63403): [b8fa478](https://github.com/ceph/ceph/commit/b8fa47849217c15ce976c3e73a961b9aa7db585e)
- Improved syntax and formatting of diskprediction module documentation.
  ↳ [#63424](https://github.com/ceph/ceph/pull/63424): [7996a9a](https://github.com/ceph/ceph/commit/7996a9a8ed00f9ed1b451967cf5615d1f3117672)
- Improve the English expression and format of the ceph-mgr module developer guide document.
  ↳ [#63578](https://github.com/ceph/ceph/pull/63578): [3322bf3](https://github.com/ceph/ceph/commit/3322bf38fa6a7ce54e4ca20f829942f1a0cb2b79)
- Improve the English expression and command example format of NFS management documents.
  ↳ [#63581](https://github.com/ceph/ceph/pull/63581): [c1c51cb](https://github.com/ceph/ceph/commit/c1c51cb6ee8a1773fd9b994c668ade66588558d4)
- Fixed typo in PG Calc documentation.
  ↳ [#63499](https://github.com/ceph/ceph/pull/63499): [b7605b2](https://github.com/ceph/ceph/commit/b7605b234224ea99ea4a0f1f19d4d160907333a7)
- Fixed a malformed command in the CephFS documentation, merging mount commands that were broken across lines into one line.
  ↳ [#63502](https://github.com/ceph/ceph/pull/63502): [133e342](https://github.com/ceph/ceph/commit/133e3428f8ebb2e9d670cc014635cbcf14cd587d)
- Fix formatting error in cache-tiering.rst document.
  ↳ [#63505](https://github.com/ceph/ceph/pull/63505): [969c9b4](https://github.com/ceph/ceph/commit/969c9b4273ea335187d4aec29c872065d71856b3)
- Modified orchestrator.rst document, changed command prompt from $ to # and adjusted code block indentation.
  ↳ [#63584](https://github.com/ceph/ceph/pull/63584): [a929ca7](https://github.com/ceph/ceph/commit/a929ca70b357ead2476d712c1755e1507c7a028f)
- Edit the doc/mgr/progress.rst document to correct formatting issues.
  ↳ [#63587](https://github.com/ceph/ceph/pull/63587): [b8e310d](https://github.com/ceph/ceph/commit/b8e310d17cef368eaca542b48da12e940fbfb361)
- Rewrote the first sentence in the iostat documentation.
  ↳ [#63681](https://github.com/ceph/ceph/pull/63681): [29d3406](https://github.com/ceph/ceph/commit/29d34064da75f0efd7b2bfa907a5e74fba2a5a16)
- Optimized the English expression of the balancer.rst document.
  ↳ [#63684](https://github.com/ceph/ceph/pull/63684): [b44401d](https://github.com/ceph/ceph/commit/b44401dbf42d1a84c68be130ca3cf872874ada01)
- Cleaned up redundant words in localpool.rst document.
  ↳ [#63670](https://github.com/ceph/ceph/pull/63670): [62061ae](https://github.com/ceph/ceph/commit/62061ae299856a6219e02c8bb4e4828d75c2ea7f)
- Unified terminology in the documentation, replacing called with named.
  ↳ [#63667](https://github.com/ceph/ceph/pull/63667): [8d1a4a0](https://github.com/ceph/ceph/commit/8d1a4a007af0a689e414c5f1c40985e9a74b2a79)
- Updated documentation on NFS cluster updates section.
  ↳ [#63664](https://github.com/ceph/ceph/pull/63664): [3085721](https://github.com/ceph/ceph/commit/30857211fde3c4377b16b9ec95a4da6971e775a5)
- Improved cephfs-mirroring.rst documentation, added hints and corrected syntax.
  ↳ [#63661](https://github.com/ceph/ceph/pull/63661): [ea5a050](https://github.com/ceph/ceph/commit/ea5a050492c77832f11552e2797de541cb06688e)
- Updated progress.rst documentation, corrected command description and clarified the optionality of PG recovery events and its impact on the Monitor's CPU overhead.
  ↳ [#63658](https://github.com/ceph/ceph/pull/63658): [ae5ea37](https://github.com/ceph/ceph/commit/ae5ea3730bfa70994f3c83550369231a20c2e55e)
- Corrected the expression and wording of the "Build the Source" chapter.
  ↳ [#63653](https://github.com/ceph/ceph/pull/63653): [1536bcc](https://github.com/ceph/ceph/commit/1536bcca8de5de4511e12c403f07d6e8a8a7277f)
- Updated "Building Sources for the First Time" section to remove obsolete references to RHEL7 and improve formatting.
  ↳ [#63708](https://github.com/ceph/ceph/pull/63708): [c16495e](https://github.com/ceph/ceph/commit/c16495ed1dbfffca4d2bb9a638d91fcf3b255fed)
- Fixed file name format quoted in HACKING.rst.
  ↳ [#63697](https://github.com/ceph/ceph/pull/63697): [f5bd029](https://github.com/ceph/ceph/commit/f5bd029334b440221728837a9e43d490e47d27bb)
- Unified the case of OMAP in the glossary and changed it to omap.
  ↳ [#63738](https://github.com/ceph/ceph/pull/63738): [1321fde](https://github.com/ceph/ceph/commit/1321fdefaeb4a182b7de3bb920244c672de28ddf)
- Fixed typos and cleaned up redundant whitespace in rgw_common.cc.
  ↳ [#64052](https://github.com/ceph/ceph/pull/64052): [6dd5e9a](https://github.com/ceph/ceph/commit/6dd5e9a1a08918b559afd3ea1f93f16b77d57d24)
- Fixed typo in log regarding replica reservation timeout.
  ↳ [#63940](https://github.com/ceph/ceph/pull/63940): [fe6dc09](https://github.com/ceph/ceph/commit/fe6dc0994c17ee2771c7246b1a1734ae91f7c5b5)
- Updated link to AWS specification format in documentation.
  ↳ [#64096](https://github.com/ceph/ceph/pull/64096): [40b68c2](https://github.com/ceph/ceph/commit/40b68c28cff55dfd56e0e75f93334a78a1ae5479)
- The upmap_max_deviation setting name is explicitly mentioned in the documentation.
  ↳ [#64119](https://github.com/ceph/ceph/pull/64119): [6dc0635](https://github.com/ceph/ceph/commit/6dc063577329bb1b1324954a312c976cbcb6dbe8)
- Fixed a typo in the documentation, correcting communicte to communicate.
  ↳ [#64148](https://github.com/ceph/ceph/pull/64148): [1e958de](https://github.com/ceph/ceph/commit/1e958de5ed4ec7ae89f6514bf623c6d8c1ed2d12)
- Fixed a typo in the balancer operation documentation.
  ↳ [#65740](https://github.com/ceph/ceph/pull/65740): [0ae90c5](https://github.com/ceph/ceph/commit/0ae90c5d345c7743fad700f578cbfea43ddb9b37)
- Fixed incorrectly closed inline literals in the ceph-conf.rst document, eliminating build warnings.
  ↳ [#64171](https://github.com/ceph/ceph/pull/64171): [64c1d3e](https://github.com/ceph/ceph/commit/64c1d3efaa99baeb067d1f3629b76ebea2214c7f)
- Added guidance to documenting configuration options using the :confval: directive in the development documentation.
  ↳ [#64167](https://github.com/ceph/ceph/pull/64167): [d1356b7](https://github.com/ceph/ceph/commit/d1356b7c7e37a14587fdaf7105e6483c11e02e78)
- Improved wording and syntax of Lifecycle Settings documentation section.
  ↳ [#64548](https://github.com/ceph/ceph/pull/64548): [44eff54](https://github.com/ceph/ceph/commit/44eff54e914721e6db588227e3bc413049366992)
- Fixed link to mClock configuration reference in documentation.
  ↳ [#64798](https://github.com/ceph/ceph/pull/64798): [9bd1d5e](https://github.com/ceph/ceph/commit/9bd1d5eeea923ca4647523dbb8ff09771a7e7988)
- Improved English description of CephFS Windows mount documentation.
  ↳ [#64786](https://github.com/ceph/ceph/pull/64786): [307048c](https://github.com/ceph/ceph/commit/307048cf9fd394dc226fca844bc90332deb4523e)
- Edited the content and formatting of the Stuck in up:replay section in the CephFS troubleshooting documentation.
  ↳ [#64853](https://github.com/ceph/ceph/pull/64853): [4239cf7](https://github.com/ceph/ceph/commit/4239cf7026989f3edc18d6f227cb480137e50941)
- Edited the "Avoiding recovery roadblocks" section in the CephFS troubleshooting documentation.
  ↳ [#64872](https://github.com/ceph/ceph/pull/64872): [f892b43](https://github.com/ceph/ceph/commit/f892b432492ef540cb0843dfe28ac4d61514a555)
