# Release Note

## Important Changes

### Ceph Metadata Server (MDS)
- Added the `charmap_md_t` class and its related methods in the public header file, and added an interface to access and operate the metadata in the core structure `inode_t`, extending the public API and core data structure. (Architecture-related: public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [2e7426f](https://github.com/ceph/ceph/commit/2e7426f7ed468e5fa2c686b51a1db3dfb4123a31)
- Removed the mgr module's direct link to the CephFS client library to resolve conflicts between dynamically linked Python modules and the boost::locale library. The module should now send commands to MDS via the cephfs Python library. (Architecture-related: build vs. install method)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [8016769](https://github.com/ceph/ceph/commit/801676931591d87773880af4281afe4add4277f9)
- Added file block difference (blockdiff) function to the libcephfs client, including initialization, execution, buffer release and operation completion API. At the same time, blockdiff operation support was added to MDS, and the API was integrated for regular file transfer, and the synchronization mechanism of the cephfs-mirror daemon was optimized. (Architecture event: ScrubBackend module change)
  ↳ [#63241](https://github.com/ceph/ceph/pull/63241): [841ec94](https://github.com/ceph/ceph/commit/841ec9467fea99cce7b5685519471f3ae94030a3), [98edb02](https://github.com/ceph/ceph/commit/98edb020538e383258edf0fae3bea4969d6152a0), [486d742](https://github.com/ceph/ceph/commit/486d742ea27a6bab7bb91b3d1af025f50f4b0d54)
- Add character mapping function bits to the client, and add a new wrapper function for handling directory entry name character mapping to support case-insensitive directory trees. (Architecture-related: CephFS client public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [f83838a](https://github.com/ceph/ceph/commit/f83838a71e41c679f4031c3682e6a70e2cecddcb), [7428697](https://github.com/ceph/ceph/commit/7428697c82bcb9d0a1aa0921ec14cafe8ca193b1)
- Introduced a new hybrid allocator `hybrid_btree2`, and updated the allocator factory to support this type. (Architecture-related: allocator public interface)
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [d5deca0](https://github.com/ceph/ceph/commit/d5deca013283d0d379f5ccf402170dda0cd59b8d)
- Add asynchronous MDS command interface `ceph_mds_command2` to libcephfs, and introduce `CommandCContext` class to support callbacks. (Architecture-related: public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [2a22041](https://github.com/ceph/ceph/commit/2a22041c3124f8f0ea99bcbecc6288d5d53acbd3)
- Introduce the `BLOCKDIFF` feature bit for CephFS clients and enable this feature in file block difference requests. (Architecture-related: public API)
  ↳ [#63241](https://github.com/ceph/ceph/pull/63241): [d73e904](https://github.com/ceph/ceph/commit/d73e904d65a1f7d98633b07abf74fc8bcd658d8a)
- Add deletion support for Ceph extended attributes (vxattrs), and fix the problem of returning "no such attribute" error when deleting. (Architecture-related: public API)
  ↳ [#60752](https://github.com/ceph/ceph/pull/60752): [73a65c7](https://github.com/ceph/ceph/commit/73a65c769751207964cff14d0969bd1ad0b53c5e)
- Re-export macro `CEPH_CONF_FILE_DEFAULT` to prevent use of `CEPH_CONF` environment variable. (Architecture-related: configuration parsing behavior)
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [5d9e5c0](https://github.com/ceph/ceph/commit/5d9e5c08a401d61ed28226be07040b9eefb43c22)
- Fixed the configuration observer registration problem caused by static variable sharing in the `md_config_cacher_t` template class, ensuring that each cache object can independently track its configuration item changes. (Architecture-related: configuration management)
  ↳ [#61398](https://github.com/ceph/ceph/pull/61398): [2dfa89e](https://github.com/ceph/ceph/commit/2dfa89e24364138776a75ea469c29702f53c0a7a)
- Fixed the problem of inaccurate mirror status summary statistics of `rbd mirror pool status` command in custom namespace. (Architecture-related: public API)
  ↳ [#61832](https://github.com/ceph/ceph/pull/61832): [10b1971](https://github.com/ceph/ceph/commit/10b19719f32a68d4a66ddea8138e7eb749975800)
- Fix the behavior of `chdir` and `getcwd` functions in libcephfs to ensure that the working directory path is correctly refreshed after directory switching. (Architecture-related: libcephfs public API behavior)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [f94bdb4](https://github.com/ceph/ceph/commit/f94bdb4ead271c17633d2405e63990fb182f4e0c), [2edaafd](https://github.com/ceph/ceph/commit/2edaafdf1da61561a237bdb5685a3061cd46074e)
- Add the `status` management socket command to the mgr daemon to fix the missing command problem caused by removing the static link library. (Architecture-related: Management interface)
  ↳ [#62504](https://github.com/ceph/ceph/pull/62504): [6ba1a7a](https://github.com/ceph/ceph/commit/6ba1a7a6dab64283189e00f8b043fbe8fb3405f5)
- Removed the `alternate_name` parameter from the client public API and moved it to the test scaffolding class to prevent the application from accidentally modifying the metadata meaning. (Architecture-related: public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [0382166](https://github.com/ceph/ceph/commit/0382166f77aa81bd40043e70837fcac5a4d7487d)
- Moved the `fuse_default_permissions` member variable from the public area to the protected area, and added the `walk_dentry_result` structure definition. (Architecture-related: public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [2f3f473](https://github.com/ceph/ceph/commit/2f3f473c48eeb51430dd043fcb179f83d7263088)
- In preparation for replacing CEPHFS error codes, refactor the error code mapping and `errorcode32_t` type for Windows platforms. (Architecture-related: platform compatibility)
  ↳ [#61994](https://github.com/ceph/ceph/pull/61994): [78ffd61](https://github.com/ceph/ceph/commit/78ffd61f0b0d6824cfa5b14c803ee61206db1493)
- Replace `CEPHFS_XXX` error codes in CephFS clients and MDS with standard system error codes. (Architecture-related: Error code standardization)
  ↳ [#61994](https://github.com/ceph/ceph/pull/61994): [4947033](https://github.com/ceph/ceph/commit/4947033bbb6b3041167ab6860b09e58a58de3aad)
- Changed the storage method of `fscrypt_last_block` in MDS from `bufferlist` to `vector` to optimize memory pool usage. (Architecture-related: public data structure changes)
  ↳ [#59616](https://github.com/ceph/ceph/pull/59616): [8d9b561](https://github.com/ceph/ceph/commit/8d9b561370dc4b2a890a7d506bd47488dd702c80)

### Object Storage Daemon (OSD)
- Copy the dmclock submodule code to the ceph repository to fix the OSD mclock queue item leakage problem. (Architecture-related: build and installation methods)
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [628814b](https://github.com/ceph/ceph/commit/628814b0531cf9334631f935022c6ffcee807d9e)
- Introduced a lightweight OMAP iteration mechanism in ObjectStore, BlueStore added a new lightweight OMAP iteration interface omap_iterate, and added corresponding methods to MemStore and KStore to support traversing the key-value pairs of objects starting from a specified position. (Architecture event: ScrubBackend module change)
  ↳ [#61363](https://github.com/ceph/ceph/pull/61363): [4f8a631](https://github.com/ceph/ceph/commit/4f8a631f8589e48cdcf78f433aeb6b2583050daf), [7b99c04](https://github.com/ceph/ceph/commit/7b99c04e5c50c3d527b47bae14e75f4f12feb41c), [11559dd](https://github.com/ceph/ceph/commit/11559dd7cd237f1c9d94ae2b3a04583c0964698d), [d893f1c](https://github.com/ceph/ceph/commit/d893f1cd243d9976ff61cc4f252d91a58b3683dd), [5c9537b](https://github.com/ceph/ceph/commit/5c9537b19d1d68e9d881795d0dfc424224bbdaba)
- Add a general --daemon-output-file parameter to the management socket interface, allowing command output to be written directly to a local file to reduce memory usage and improve performance. (Architecture event: Data_Formatting_and_Crypto_Utils module removed)
  ↳ [#57675](https://github.com/ceph/ceph/pull/57675): [b550bf6](https://github.com/ceph/ceph/commit/b550bf60adf14b38db2b29adb565e1469afdc2cb)
- Added the function of mounting object storage in read-only mode to the ceph-objectstore-tool tool, so as to access possibly damaged object storage in scenarios where read-only operations are allowed. (Architecture-related: Object Storage Public Interface)
  ↳ [#62123](https://github.com/ceph/ceph/pull/62123): [310c484](https://github.com/ceph/ceph/commit/310c4849c1b57d0fa386532dbfeee4cd2f2a7133)
- Added rbd_diff_iterate3() API, which allows specifying the starting snapshot of the difference iteration through the snapshot ID (instead of the name) to support the difference calculation of non-user snapshots. (Architecture-related: public API)
  ↳ [#62130](https://github.com/ceph/ceph/pull/62130): [67ebbb6](https://github.com/ceph/ceph/commit/67ebbb66ca7ce7cbc7411ee7974b69a47e8c6559)
- Added IPv6 support to the is_addr_in_subnet function so that it can handle both IPv4 and IPv6 addresses. (Architecture-related: Platform compatibility)
  ↳ [#61323](https://github.com/ceph/ceph/pull/61323): [1f011ae](https://github.com/ceph/ceph/commit/1f011aeb549fdeb52d82786b172ab502a971474d)
- Added disk fragmentation health warning function to BlueStore, added configuration item bluestore_warn_on_free_fragmentation to control when fragmentation score is used as a health warning, and improved the calculation method of fragmentation score. (Architecture-related: configuration item)
  ↳ [#61910](https://github.com/ceph/ceph/pull/61910): [6bcba24](https://github.com/ceph/ceph/commit/6bcba24896df1d7fbcebb1d3f724c925d55b0c59)
- Added show-label-at command to bluestore-tool, which is used to read the label information of the specified disk location, and improved the label verification logic. (Architecture-related: construction and installation methods)
  ↳ [#62202](https://github.com/ceph/ceph/pull/62202): [6b3a7b4](https://github.com/ceph/ceph/commit/6b3a7b46c0c9f9f12fd0ceb2a7bb0b22a5343b2a), [6457c53](https://github.com/ceph/ceph/commit/6457c53a82d10f2df23cb1c3be5b434c3ac7d2f7)
- Added osd rm-pg-upmap-primary-all command, which is used to clear all pg-upmap-primary mappings in OSDMap at once. (Architecture-related: public API)
  ↳ [#62421](https://github.com/ceph/ceph/pull/62421): [9a4e930](https://github.com/ceph/ceph/commit/9a4e9305bf732dc6f9db9a9423342fd23a40fd84)
- Introduced a mechanism for locking the first DB/WAL allocation unit for BlueFS, added the bluefs_locked_extents_t structure and its related methods, and added corresponding unit tests. (Architecture-related: public API)
  ↳ [#62514](https://github.com/ceph/ceph/pull/62514): [ab3dedb](https://github.com/ceph/ceph/commit/ab3dedbd5bce3ce5047993f462ace8365c27da1b)
- Fixed the problem that user-specified location constraints were not correctly applied when creating a bucket in a multi-zone group scenario, and removed the has_zonegroup_api method that is no longer needed. (Architecture-related: storage backend public interface)
  ↳ [#62420](https://github.com/ceph/ceph/pull/62420): [f3f74f4](https://github.com/ceph/ceph/commit/f3f74f43822c450f4ce5feec26e72f15402a60d9)
- Added osd_scrub_interval_randomize_ratio and osd_deep_scrub_interval parameters to the list of configuration options that trigger OSD to recalculate the next scrub schedule. (Architecture-related: configuration options)
  ↳ [#62956](https://github.com/ceph/ceph/pull/62956): [060b264](https://github.com/ceph/ceph/commit/060b264d5d7b85c0008b87392c800e7b159780c5)
- Migrate Objecter's message distribution interface to ms_dispatch2 and ms_fast_dispatch2 to support the message confirmation mechanism. (Architecture-related: message distribution interface)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [b3cede5](https://github.com/ceph/ceph/commit/b3cede5524bdbd8fa2b6c4ddcbb5e3046de8e1ff)
- Added value_as_sv method to KeyValueDB's OMAP iterator to avoid unnecessary memory copies during the iteration process, thereby improving performance. (Architecture-related: public API new)
  ↳ [#61363](https://github.com/ceph/ceph/pull/61363): [db5a9dd](https://github.com/ceph/ceph/commit/db5a9dd002bf272798ea3bd3a728441d718122c4)
- Introduce an upper limit on the number of pending discards for asynchronous discard operations to prevent OSD capacity exhaustion due to too long discard queues. New configuration item bdev_async_discard_max_pending is added to control the maximum number of pending discards. The default value is 1000000. (Architecture-related: Configuration item changes)
  ↳ [#62221](https://github.com/ceph/ceph/pull/62221): [37e1e72](https://github.com/ceph/ceph/commit/37e1e723a93dc2d3da2e36f971baa9e3f4311534)

### RADOS Gateway (RGW)
- Added NBD stream support to the librbd migration function, allowing external mirror data to be read through the NBD protocol. At the same time, a sparse range query interface was added to all stream types, and the error handling and URI connection methods of NBD streams were improved. In addition, support for external Ceph clusters was added to the migration function (currently only in import mode). (Architecture event: ImageStateApplier module is added)
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [5a2c11c](https://github.com/ceph/ceph/commit/5a2c11c579f9a3516c8b532f9d2a79ba2990e03e), [83ab7ae](https://github.com/ceph/ceph/commit/83ab7ae9dc8e9812a70378c4493f6851af2251d8)
- Added SASL authentication support for RGW Kafka integration, allowing configuration of usernames and passwords. It also supports sending messages to Kafka clusters with multiple brokers, and supports broker list configuration through new parameters. (Architecture-related: RGW Kafka integration public API)
  ↳ [#60952](https://github.com/ceph/ceph/pull/60952): [5f4cbdd](https://github.com/ceph/ceph/commit/5f4cbdd82d5f9cf7e891f005f5c683539deded71) | [#61764](https://github.com/ceph/ceph/pull/61764): [e8638a1](https://github.com/ceph/ceph/commit/e8638a13255afd5a8849538b9f1b180f7a5b2420)
- Add the flags parameter to the RGW object attribute operation interface to support replication status logging, and implement the automatic update logic of the x-amz-replication-status header between the PENDING and COMPLETED states. (Architecture-related: Storage abstraction layer public interface)
  ↳ [#60785](https://github.com/ceph/ceph/pull/60785): [79d3d6f](https://github.com/ceph/ceph/commit/79d3d6fa9d5067748fb58716b4a38ae1f94733fc)
- Added support for the --account-id parameter to radosgw-admin's bucket link and bucket unlink commands, allowing buckets to be associated or unassociated with accounts rather than individual users. (Architecture-related: CLI API)
  ↳ [#60982](https://github.com/ceph/ceph/pull/60982): [ee641d9](https://github.com/ceph/ceph/commit/ee641d9f7f876d2f038fe39f1accfdf743ae2f06)
- Added support for ARN-based conditions (such as ArnEquals, ArnLike) for RGW IAM policy evaluation, and added corresponding unit tests. (Architecture-related: public API)
  ↳ [#62435](https://github.com/ceph/ceph/pull/62435): [7bbd731](https://github.com/ceph/ceph/commit/7bbd7318f1e81da274f5b78f4688a2ef5d068ce6)
- Add boolean parameters to the set_atomic method to support explicit control of atomic state, and apply prefetch data settings when getting versioned object instance headers. (Architecture-related: public API)
  ↳ [#63193](https://github.com/ceph/ceph/pull/63193): [25b39af](https://github.com/ceph/ceph/commit/25b39aff162086451cad23b14091397ccb4d107c)
- In RGW multi-site synchronization, add RGW_BILOG_NULL_VERSION flag to bilog_flags to fix issues when deleting objects with null version IDs. (Architecture-related: RGW multi-site synchronization)
  ↳ [#62309](https://github.com/ceph/ceph/pull/62309): [c860a39](https://github.com/ceph/ceph/commit/c860a3966971ef8ed3e15635ae8344929931aa3f)
- In multi-site setups, STS authentication now bypasses temporary credential verification and instead uses system user credentials for signature verification when requests are forwarded from a secondary site. (Architecture-related: STS authentication behavior)
  ↳ [#63065](https://github.com/ceph/ceph/pull/63065): [c734fc1](https://github.com/ceph/ceph/commit/c734fc109e2f4665640dd5f22e3c8ca8627e4b83)
- Repair the S3Select error response process, unify the error response API, add new configuration options, and ensure that the error response complies with the AWS S3 API specification. (Architecture-related: public API)
  ↳ [#62959](https://github.com/ceph/ceph/pull/62959): [09cba1d](https://github.com/ceph/ceph/commit/09cba1d9fcde93aaaa03f855d9e9512fa362ebee), [d44c926](https://github.com/ceph/ceph/commit/d44c92630ae7c01be02ddc65e3e0d4152d09e532)
- Fix the issue of inconsistent ETag output format in RGW and ensure it complies with AWS S3 API specification. (Architecture-related: public API)
  ↳ [#62607](https://github.com/ceph/ceph/pull/62607): [8ea5739](https://github.com/ceph/ceph/commit/8ea573985c5323021b2e161487a6703786d43d1a)
- Fixed the problem caused by the behavior change of merge_and_store_attrs() when deleting container metadata in Swift API, instead directly setting attributes and storing bucket information. (Architecture-related: public API)
  ↳ [#64552](https://github.com/ceph/ceph/pull/64552): [397e5d5](https://github.com/ceph/ceph/commit/397e5d5dfc4655eb3cfeb71a02c473710d5a4c71)
- Add missing last_modified field to Swift API bucket list response to comply with Swift API specification. (Schema related: public API)
  ↳ [#61546](https://github.com/ceph/ceph/pull/61546): [7749bba](https://github.com/ceph/ceph/commit/7749bbaae8d464d8e5898cd490e93f8c1ca0785b)
- Added the function of using the modulus and exponent of the RSA algorithm group for JWT signature verification, and fixed related signature calculation issues. (Architecture-related: public API)
  ↳ [#63052](https://github.com/ceph/ceph/pull/63052): [b8720c8](https://github.com/ceph/ceph/commit/b8720c86c9125b7f14e88571867ace322ae7b90b)
- Fixed the issue that the /admin/user API does not contain account-related user information, now the account_id, path, create_date, tags and group_ids fields will be output. (Architecture-related: public API)
  ↳ [#61430](https://github.com/ceph/ceph/pull/61430): [b09cc63](https://github.com/ceph/ceph/commit/b09cc634bf21485b06869cbea7e55e1c3d553d40)
- Fixed the return status code of S3 deletion bucket policy interface, changed from 200 to 204 No Content. (Architecture-related: public API)
  ↳ [#61431](https://github.com/ceph/ceph/pull/61431): [40c8735](https://github.com/ceph/ceph/commit/40c873546a50f6c1de026c52bc344f171b1a983c)
- Fixed a parsing issue with the quota limit parameter in the /admin/account API so that it can accept negative values to indicate unlimited. (Architecture-related: public API)
  ↳ [#62131](https://github.com/ceph/ceph/pull/62131): [2626006](https://github.com/ceph/ceph/commit/2626006ca1de1499acde21a9bf50c2213cd3ba71)
- Fixed a crash that occurred during shutdown when ops-log was enabled, by adjusting the lifecycle management of log objects. (Architecture-related: runtime behavior)
  ↳ [#62134](https://github.com/ceph/ceph/pull/62134): [fc9bed6](https://github.com/ceph/ceph/commit/fc9bed691b8deb684893483f4ab045b79a5b03d9)
- Allow PutObjectLockConfiguration operation on existing buckets, even if object locking is not enabled when created. (Schema related: public API)
  ↳ [#62064](https://github.com/ceph/ceph/pull/62064): [3a5750d](https://github.com/ceph/ceph/commit/3a5750d20c7e92c2ec7667840e8a136e5ac890dd)
- Fixed the permission verification of the InitMultipart operation, now using the object ARN instead of the default bucket ARN for permission checking. (Architecture-related: public API)
  ↳ [#62154](https://github.com/ceph/ceph/pull/62154): [26ea1ae](https://github.com/ceph/ceph/commit/26ea1ae5700b27f3c12f4b107e38470d0ed89e85)
- Map ENOSPC and EDQUOT errors to the 507 InsufficientCapacity response code of S3 API. (Architecture-related: S3 API error code mapping)
  ↳ [#62559](https://github.com/ceph/ceph/pull/62559): [14f593b](https://github.com/ceph/ceph/commit/14f593bcd775a2e22093c4a7cc214ed546935705)
- Fixed the configuration option compliance and flag usage issues of the Group snapshot creation interface in librbd. (Architecture-related: librbd public API consistency)
  ↳ [#62963](https://github.com/ceph/ceph/pull/62963): [395f0fa](https://github.com/ceph/ceph/commit/395f0fa548686398d55cd20634390f3f3d520c66), [0535bd0](https://github.com/ceph/ceph/commit/0535bd0b6bab72618cc6352ef7a49b7a417b9c7f)
- Fixed access control and policy matching issues in the RGW service, including case sensitivity of Swift interface cross-tenant ACL access and policy ARN comparison. (Architecture-related: RGW access control and policy matching)
  ↳ [#62586](https://github.com/ceph/ceph/pull/62586): [b5e1196](https://github.com/ceph/ceph/commit/b5e1196f1369b4bd17952cf5db943848a35b6471) | [#62435](https://github.com/ceph/ceph/pull/62435): [b79c612](https://github.com/ceph/ceph/commit/b79c612d98770a70438b9094bd775f55bd5e825e)
- Fixed the permission check of OIDC Provider in RGW IAM, and corrected the checked permission type from roles to oidc-provider. (Architecture-related: public API)
  ↳ [#62892](https://github.com/ceph/ceph/pull/62892): [245aaeb](https://github.com/ceph/ceph/commit/245aaeba0ad3b966fa5d09892a2fe5f8322255d0)
- Fixed the processing logic for null version ID when deleting objects, ensuring that the null_verid parameter is correctly set and passed. (Architecture-related: public API)
  ↳ [#62309](https://github.com/ceph/ceph/pull/62309): [012d8eb](https://github.com/ceph/ceph/commit/012d8ebd71f01fa8e61ad07dae806e643ffc881f)
- Modify the erase function of interval_set so that it returns an iterator instead of void to fix the problem of invalid iterator usage. (Architecture-related: public API changes)
  ↳ [#62576](https://github.com/ceph/ceph/pull/62576): [92705d8](https://github.com/ceph/ceph/commit/92705d8a65a96864a9fd489896adbb6e3c93babf)

### Monitor (MON)
- Introduce the common cluster log level configuration item mon_cluster_log_level to uniformly control the detail level of log output to standard error, syslog and graylog, replacing the original mon_cluster_log_file_level and mon_cluster_log_to_syslog_level configuration. (Architecture-related: cluster log configuration)
  ↳ [#61069](https://github.com/ceph/ceph/pull/61069): [b0e8138](https://github.com/ceph/ceph/commit/b0e813887fe583cf17fe733cda37a41fef77bdcf)
- Call the flush() method in the destructor of JSONFormatterFile to ensure that the pending string is correctly refreshed when the object is destroyed, and two new flush method overloads are added to comply with API specifications. (Architecture-related: public API)
  ↳ [#57675](https://github.com/ceph/ceph/pull/57675): [fb2c784](https://github.com/ceph/ceph/commit/fb2c7846d52c798ffcf1ccd6eb1d1f86982fd0d4)

### Cross-cutting / Other Architecture-related Changes
- If the flatten flag is set during migration, the target image will be created independently, and the parent-child relationship will no longer be established through cloning. (Architecture-related: Image migration behavior)
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [73191f3](https://github.com/ceph/ceph/commit/73191f37f7ac70d601be35b3d9160d7fab1c8c8a)
- Added a new level attribute for module options, allowing you to specify the level when loading options, such as options used to distinguish development purposes. (Architecture-related: module option configuration)
  ↳ [#57189](https://github.com/ceph/ceph/pull/57189): [52bb097](https://github.com/ceph/ceph/commit/52bb097f863959d555d4f9b0915a4643191b7a1e)
- Added ceph_pthread_setname and ceph_pthread_getname functions to cache thread names and reduce system calls, while removing the old pthread_t parameter interface. (Architecture-related: thread management interface)
  ↳ [#61287](https://github.com/ceph/ceph/pull/61287): [6255143](https://github.com/ceph/ceph/commit/6255143a06c0d6f84c7c3539a810a8a36f8f97b8)
- Add begin, rbegin, end and rend iterator methods to the filepath class to support traversal of path components. (Architecture-related: public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [9cb1fb9](https://github.com/ceph/ceph/commit/9cb1fb94208150139e4a8688ab4fb14a371b16c8)
- Fixed the out-of-bounds access problem of the filepath::set_path method when processing empty strings. Now it will first check whether the string is empty. (Architecture-related: public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [26ecf7c](https://github.com/ceph/ceph/commit/26ecf7c4a5680431c4bc3b5a260ba2df3a5ca6a2)
- Abstract the direct call of libnbd in NBDStream into the NBDClient interface, and add a new unit test for NBDStream. (Architecture-related: public API)
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [5e0a348](https://github.com/ceph/ceph/commit/5e0a3484098370e53f9b7ddef8aa92aa7482fdec)
- The version field in the BlueFS superblock structure was renamed to seq, and all related serialization, deserialization, dump and test code were updated. (Architecture-related: BlueFS superblock format changes)
  ↳ [#62514](https://github.com/ceph/ceph/pull/62514): [0fb06f8](https://github.com/ceph/ceph/commit/0fb06f8bc972c880e894ac86354e4daf5130ba6d)
- Added Boost.Locale and ICU dependencies for client builds. (Architecture-related: build dependency changes)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [569ed13](https://github.com/ceph/ceph/commit/569ed13df37a524d4a05f7b3408d4de85930ace7)
- Restored the bdev_async_discard configuration parameter to maintain backward compatibility, and added performance counters for discarded threads in kernel devices. (Architecture-related: Configuration and Compatibility)
  ↳ [#62254](https://github.com/ceph/ceph/pull/62254): [7b914cb](https://github.com/ceph/ceph/commit/7b914cb49d50241b2ed7811d8660fce27a80ae39)

### AsyncMessenger (Messaging & Transport Layer)
- Introduced a new return type for message dispatchers to support the "acknowledged but allowed other dispatchers to continue processing" state. (Architecture-related: public API)
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [7607633](https://github.com/ceph/ceph/commit/7607633db942f79bb2d489ac207b452f41206d41)
- Remove the filtering logic for specific error codes in librbd asynchronous request processing, so that the operation directly returns the underlying error. (Architecture-related: public API)
  ↳ [#61645](https://github.com/ceph/ceph/pull/61645): [3016e00](https://github.com/ceph/ceph/commit/3016e000ab3636f652dea4fe98f69bf8db1d584d)
- Modify the processing method of the result field in the MClientReply message and use errorcode32_t to automatically convert error codes. (Architecture-related: cross-platform error codes)
  ↳ [#61994](https://github.com/ceph/ceph/pull/61994): [f3824ad](https://github.com/ceph/ceph/commit/f3824ad6cc3ded205dec3b89c801e92839152216)

## Routine Changes

### New features
- Added a print method to the client Dentry class, which is used to format and output directory entry information, including details such as alternative names and reference counts.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [5c1eddb](https://github.com/ceph/ceph/commit/5c1eddbd8c6e13f29de7b73f79aa88a023c8ed3a), [b33fbeb](https://github.com/ceph/ceph/commit/b33fbeb4eae27f4be3d3b0c845a8e6be1dd5dd2e)
- Added the asok command for dumping the export status to diagnose when the export subtree task is blocked. At the same time, the export status management was restructured, and the status history record and waiter counting functions were added.
  ↳ [#60836](https://github.com/ceph/ceph/pull/60836): [abeafaa](https://github.com/ceph/ceph/commit/abeafaa0fe4cc30a9378ad4b29b4c9de059bfc53)
- Added a copy of the csum_type field in the BlueStore::WriteContext::fork method so that the checksum type information can be retained when the context is forked.
  ↳ [#62143](https://github.com/ceph/ceph/pull/62143): [eddcf68](https://github.com/ceph/ceph/commit/eddcf686b3b724e1e871079fbf5b31c0465fbbef)
- Added p2aligned template function in intarith.h, which is used to check whether a value is aligned with the given alignment value.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [96730b4](https://github.com/ceph/ceph/commit/96730b417e57376224c61d67bdb5e307a13bb688)
- Added yield_waiter template class in common/async module, and added corresponding unit tests.
  ↳ [#62337](https://github.com/ceph/ceph/pull/62337): [836b967](https://github.com/ceph/ceph/commit/836b967aa76127d96ca74d76afe361e8245f035a)
- Added support for the environment variable TMPDIR in configuration parsing, which is used to set the directory for temporary files of the daemon process.
  ↳ [#57675](https://github.com/ceph/ceph/pull/57675): [2369180](https://github.com/ceph/ceph/commit/2369180fd41d3bd8e15d07dae3d6e0d58595f2a3)
- Added a rotate subcommand to the ceph auth command set, which is used to rotate the permanent key of the specified entity, avoiding the need to delete and re-create the key when the key is leaked, lost or rotated regularly.
  ↳ [#58235](https://github.com/ceph/ceph/pull/58235): [f7b279b](https://github.com/ceph/ceph/commit/f7b279bf23caf2d45927cf17f18090b0e26fc9b8)
- New configuration item mds_allow_async_dirops is added to control whether asynchronous directory operations are allowed to avoid lock cache defects.
  ↳ [#61840](https://github.com/ceph/ceph/pull/61840): [f9f6bf9](https://github.com/ceph/ceph/commit/f9f6bf94457d9ccd979691b5124e1001e67fd596)
- Added ceph mgr module force disable command, which allows forcibly disabling the always-on Mgr module, mainly used in cluster recovery scenarios.
  ↳ [#60562](https://github.com/ceph/ceph/pull/60562): [67ce0c5](https://github.com/ceph/ceph/commit/67ce0c5ee9a4403115c0a91f9489646b32f97077)
- Add a device name parameter when creating a block device and pass it to the kernel device instance.
  ↳ [#62254](https://github.com/ceph/ceph/pull/62254): [54af1f6](https://github.com/ceph/ceph/commit/54af1f6d48ecdf52a8b1d4a86def8a1afedfb3cd)
- Added copy and append helper template functions for uint8_t vectors in buffer.h.
  ↳ [#59616](https://github.com/ceph/ceph/pull/59616): [e683315](https://github.com/ceph/ceph/commit/e68331598e01b22fde7eb75afb5f9da226c812d1)
- Access character mapping (charmap) support for metadata extended attributes (vxattr), allowing the directory's character mapping, normalization, encoding and case-sensitive settings to be modified through attributes such as ceph.dir.charmap.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [76daedc](https://github.com/ceph/ceph/commit/76daedca651079b3f488937a220bd84f38f62317)
- Added ceph mon disable_stretch_mode command to allow users to exit stretch mode gracefully and restore to normal cluster state.
  ↳ [#60629](https://github.com/ceph/ceph/pull/60629): [882b506](https://github.com/ceph/ceph/commit/882b506644c87eeb6da4604fdc8cee870b219f96)
- Added the osd_recovery_sleep_degraded series of configuration items, which are used to independently control the throttling of data movement when recovering a degraded PG, and automatically select the corresponding sleep time during the recovery process based on whether the PG has been degraded.
  ↳ [#62400](https://github.com/ceph/ceph/pull/62400): [2a556f0](https://github.com/ceph/ceph/commit/2a556f06647c0ed2781dea0bab5c9632cc5c7418)
- Switched the configuration of NBDStream from TCP based URLs and ports to support NBD URIs, allowing the use of transports such as Unix domain sockets and specifying export names.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [e9e2cee](https://github.com/ceph/ceph/commit/e9e2ceefc9a89b8d3ff080ff7649feb0017396a5)
- When notification_v2 is enabled, the creation, modification, and deletion requests of Topic and Notification will be forwarded to the master node.
  ↳ [#61242](https://github.com/ceph/ceph/pull/61242): [ad8f136](https://github.com/ceph/ceph/commit/ad8f13695f9e7270124b75f88ab60a6128283c0a)
- Allow deletion of buckets from non-primary zone groups by executing the radosgw-admin bucket rm command, and support the --purge-objects and --bypass-gc options when deleting.
  ↳ [#62994](https://github.com/ceph/ceph/pull/62994): [dfe08b5](https://github.com/ceph/ceph/commit/dfe08b55889e5f9d55a118ae8064e5a28b9f83ad)
- Introduced the time_guard template class in ceph_time.h, which is used to automatically calculate the time difference through RAII style.
  ↳ [#61363](https://github.com/ceph/ceph/pull/61363): [4324074](https://github.com/ceph/ceph/commit/432407450c2c17789f40e8e1b476de98c20d3494)
- Added key_as_sv, raw_key_as_sv and value_as_sv methods that return string_view for KeyValueDB iterators to avoid unnecessary memory copies in OMAP iterations.
  ↳ [#61363](https://github.com/ceph/ceph/pull/61363): [e1487e3](https://github.com/ceph/ceph/commit/e1487e3f28b10d3de497b05fadd36ef36876d7d2)
- Added printing support for the alternate_name field when the client dumps directory entry information.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [bfe0831](https://github.com/ceph/ceph/commit/bfe08312602252bd00fdb381722bb6d1f60b1975)
- Encoded optmetadata in InodeStat sent to the client, and updated InodeStat's decoding logic to support the new version structure.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [88e1639](https://github.com/ceph/ceph/commit/88e16394186134a788ba622ab90b89a7d213b113)
- The logging system will now cache the thread name mapping within the last day, and display multiple thread names of the same process together when dumping.
  ↳ [#61287](https://github.com/ceph/ceph/pull/61287): [ff4565a](https://github.com/ceph/ceph/commit/ff4565ac3f2d8c1f32b6dc3b917f4d30b114f1d4)
- Sorted the client configuration key list and added tracking of the fuse_default_permissions configuration item.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [a114d1b](https://github.com/ceph/ceph/commit/a114d1bdeaef3e019847a21787f7deb85a90ca7e)
- Allow RGW users to manage accounts user permissions to support account-related REST operations.
  ↳ [#61782](https://github.com/ceph/ceph/pull/61782): [bf68d77](https://github.com/ceph/ceph/commit/bf68d77ab677f83a40a5ecc85cb6edf70328c82b)
- Added the --purge-data option to the radosgw-admin account rm command, allowing all buckets and objects owned by the account to be automatically purged when the account is deleted.
  ↳ [#62365](https://github.com/ceph/ceph/pull/62365): [3ee5183](https://github.com/ceph/ceph/commit/3ee5183bca4b65a85a5e2ea7bea7cbd59d6fe9bb)
- Added ceph_notify_all method to MgrModule for sending notifications to support MDS command completion signals.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [9aefed1](https://github.com/ceph/ceph/commit/9aefed1dd87acf780fb94bd2c2cba6bf6ab37afa)
- Added signature verification using modulus and exponent to JWT validation for RGW STS, and improved error handling.
  ↳ [#63052](https://github.com/ceph/ceph/pull/63052): [db80d32](https://github.com/ceph/ceph/commit/db80d32b0ccecd6fcefc7bf28acf45944d4cc0ca)
- In the metadata collection functions of BlueFS and BlueStore, a new record of the allocator type is added to display the allocator information when metadata is dumped.
  ↳ [#62514](https://github.com/ceph/ceph/pull/62514): [b16e796](https://github.com/ceph/ceph/commit/b16e796d71e2b6023dfe8829c2ec7012dc969ac6)
- Introduced bluefs-super-dump command for ceph-bluestore-tool, used to dump BlueFS super block information.
  ↳ [#62514](https://github.com/ceph/ceph/pull/62514): [e793ee2](https://github.com/ceph/ceph/commit/e793ee28e050a42601502a8eaa2456ed9566c3d4)
- Added support for dumping optional metadata (optmetadata) in the output of the dump tree command, and fixed formatting issues.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [82ef5fb](https://github.com/ceph/ceph/commit/82ef5fbdaf30d0b65435aec1a497f9e9b842e611)
- Modify the radoslist command so that it can also output relevant information when the header object cannot be found to better support the rgw-gap-list tool to find missing rados objects.
  ↳ [#62417](https://github.com/ceph/ceph/pull/62417): [2916104](https://github.com/ceph/ceph/commit/2916104a5b97750a03f8c9874972874221c71148)
- Added --yes-i-really-mean-it option to radosgw-admin object rm command to enable force mode to remove bucket index entries even if there is a problem with the header object.
  ↳ [#62748](https://github.com/ceph/ceph/pull/62748): [4f21298](https://github.com/ceph/ceph/commit/4f212980318eafd8480a6c0297f98ae9ad116cee), [23093aa](https://github.com/ceph/ceph/commit/23093aac029e811ebcaee8592b7b419601399dac)
- Refactor the logic of creating the source image context in the migration module NativeFormat, use the rados_ptr method instead and remove the related header file dependencies.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [6d32ae6](https://github.com/ceph/ceph/commit/6d32ae673953a17367c7f8c23a86fb87d3497edd)
- Clean up RGW object deletion logic, add forced deletion options to handle missing header objects, and adjust code format and comments.
  ↳ [#62748](https://github.com/ceph/ceph/pull/62748): [974393b](https://github.com/ceph/ceph/commit/974393b9e5e4c9f2aa21447188d5eb911aface88)
- Added debug trace point auxiliary template class debug_point_t to BlueFS to support more lightweight debugging functions.
  ↳ [#62839](https://github.com/ceph/ceph/pull/62839): [a35f00a](https://github.com/ceph/ceph/commit/a35f00ae024439aaed244c0fd3654af4a0dabf11)
- Add string mapping for GETVXATTR and FILE_BLOCKDIFF operations in ceph_mds_op_name function.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [94c2aee](https://github.com/ceph/ceph/commit/94c2aeeaffde168504393f2c3b8e9161543dff90)
- Improve the debug log output when bdev tag decoding fails in BlueStore, remove useless information and add the failure location display.
  ↳ [#61671](https://github.com/ceph/ceph/pull/61671): [150e1c7](https://github.com/ceph/ceph/commit/150e1c7467cf05d569423547accda9d854ed709c)

### bug fixes
- Fixed the issue where data_digest was not cleared during the truncate operation, resulting in CRC check failure for full object reading.
  ↳ [#57586](https://github.com/ceph/ceph/pull/57586): [6246a16](https://github.com/ceph/ceph/commit/6246a16e5e16bab6a4e7345b6bc55a5f66b5e93e), [c2cad9d](https://github.com/ceph/ceph/commit/c2cad9db7a694ed1f0c64291f530868a7afed1b0), [41e2d08](https://github.com/ceph/ceph/commit/41e2d08a798e21cb4723c5ea8d06729fe4de0bc8)
- Unify the error handling logic of the BlueFS allocator and fix the conditional judgment of releasing allocated space when allocation fails.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [721a960](https://github.com/ceph/ceph/commit/721a9600f30dba9902af2a0c2514370e4fa9cf4c)
- Fixed an issue where the new_attrs parameter was incorrectly used in the RadosBucket::merge_and_store_attrs method, causing overwriting of existing attributes.
  ↳ [#61995](https://github.com/ceph/ceph/pull/61995): [606ef83](https://github.com/ceph/ceph/commit/606ef838a800d362d7451fb7828583a9bd9f6ae5)
- Improve ceph_objectstore_tool's pg export command to ignore read errors when the --force flag is supplied to allow partial data to be exported.
  ↳ [#62123](https://github.com/ceph/ceph/pull/62123): [0f237d3](https://github.com/ceph/ceph/commit/0f237d37e74c4ecf1e2166a0b09c41f9d73327ee)
- Roll back the check logic for deletion markers in the rgw_bucket_link_olh function to allow the creation of multiple deletion markers.
  ↳ [#62740](https://github.com/ceph/ceph/pull/62740): [9cca4fd](https://github.com/ceph/ceph/commit/9cca4fd435a5470be42c863ce791476efde0327f)
- Added get_shared_blob method in BlueStore, and used this method in the shared blob repair test case to verify the repaired reference mapping.
  ↳ [#60240](https://github.com/ceph/ceph/pull/60240): [2ee8053](https://github.com/ceph/ceph/commit/2ee8053998f2f66415999318079af895e4a3141a)
- Fixed the problem of file cache capability reference leakage in client-side asynchronous reading to prevent asynchronous reading calls from stalling.
  ↳ [#60218](https://github.com/ceph/ceph/pull/60218): [0fe9a14](https://github.com/ceph/ceph/commit/0fe9a14c9e2949cad8c771575a2036de28c00c3e)
- Fixed an issue where expired deletion markers were not properly deleted when processing expired lifecycle operations for a specified number of days.
  ↳ [#60783](https://github.com/ceph/ceph/pull/60783): [9b4d66a](https://github.com/ceph/ceph/commit/9b4d66ab9afdf25b57de94091c2ec0042c26709c)
- Fixed the error code propagation problem caused by missing data pools when updating traceback information in batches by pool ID when expired log segments.
  ↳ [#60688](https://github.com/ceph/ceph/pull/60688): [94c8d02](https://github.com/ceph/ceph/commit/94c8d024f853cf779508cea21070a7d339d21004)
- Adjust the message processing order to process MonMap, FSMap and OSDMap before notifying the module to ensure that the module reads the latest map data.
  ↳ [#57064](https://github.com/ceph/ceph/pull/57064): [573937c](https://github.com/ceph/ceph/commit/573937c4621e6402d85d0768c204441fb659626d)
- Fixed an issue where when the same client's setattr request holds xlock, the getattr request may use projected inode, resulting in inconsistent file modes between multiple clients.
  ↳ [#60691](https://github.com/ceph/ceph/pull/60691): [c6ce4c1](https://github.com/ceph/ceph/commit/c6ce4c1f379fddb2ae3bdadb0bbc0b3dccace6a3)
- Fixed an error in calculating the total directory size in the BlueFS::_estimate_log_size_N function, and corrected the addition operation to a multiplication operation.
  ↳ [#61891](https://github.com/ceph/ceph/pull/61891): [2fb10e9](https://github.com/ceph/ceph/commit/2fb10e92f69c5df1bbb2ba52ba991a892b84d97a)
- Fixed an issue where properties were not saved correctly to backend storage after erasing during operations such as deleting bucket tags, CORS, public access blocks and encryption configurations.
  ↳ [#61995](https://github.com/ceph/ceph/pull/61995): [c236424](https://github.com/ceph/ceph/commit/c2364240e0e50159d95155826b968bfa6872ad2e)
- Fixed DBBucket::merge_and_store_attrs method to correctly store updated attributes into the backend storage.
  ↳ [#61995](https://github.com/ceph/ceph/pull/61995): [57e1adb](https://github.com/ceph/ceph/commit/57e1adb29aa783f54b913c03a7783b271be506f8)
- Add a null value check for the open_collection call in ceph_objectstore_tool, and return an error and output a prompt message when the collection does not exist to fix potential crash issues.
  ↳ [#58732](https://github.com/ceph/ceph/pull/58732): [844bba0](https://github.com/ceph/ceph/commit/844bba0bd3c05ce03987193e284f9d48f51cdc8b) | [#60861](https://github.com/ceph/ceph/pull/60861): [ffdfc80](https://github.com/ceph/ceph/commit/ffdfc8032e2f13e53f05bf6fcdbc3f7a94fcdf1c)
- Improved the access check logic of snapshot deleted directories in MDS to ensure that files can use the correct path of the parent directory for permission check, and corrected related error codes.
  ↳ [#59518](https://github.com/ceph/ceph/pull/59518): [76f5728](https://github.com/ceph/ceph/commit/76f5728d3a5219b94318e4afe24c938ab4060c86), [b6d097b](https://github.com/ceph/ceph/commit/b6d097b0e679328d812df85b24106c9c5f7dcabe)
- Fix the parsing logic of strict_iec_cast function for unit strings with suffix 'B' (such as KB, MB).
  ↳ [#60581](https://github.com/ceph/ceph/pull/60581): [5fea214](https://github.com/ceph/ceph/commit/5fea214eb9bbaf05392a016986f3965361ddd58e), [87ee0f1](https://github.com/ceph/ceph/commit/87ee0f160ea802fb19d644aaf5992d13b30e7abf)
- Fixed the read operation hanging problem in Client::get_caps caused by non-zero Fc capability reference count.
  ↳ [#60694](https://github.com/ceph/ceph/pull/60694): [b333c18](https://github.com/ceph/ceph/commit/b333c18f8ea779047142ef8cb55d05303d942166)
- Fixed an issue that caused assertion failure when a non-existent bucket was encountered when checking an invalid CRUSH area.
  ↳ [#62039](https://github.com/ceph/ceph/pull/62039): [ba1a1ad](https://github.com/ceph/ceph/commit/ba1a1ad2a644bab454cd8df51a54e3707b9307b5)
- In Stretch mode, warn when monitor CRUSH position does not exist, but exclude arbiter.
  ↳ [#62039](https://github.com/ceph/ceph/pull/62039): [f937604](https://github.com/ceph/ceph/commit/f937604a75e0883f1b5953d9897f534c9724eaf9)
- Fix a race condition that may occur when printing Inode in the ll_sync_inode function.
  ↳ [#59621](https://github.com/ceph/ceph/pull/59621): [c5966a2](https://github.com/ceph/ceph/commit/c5966a29bbb8a783b9cf68d4fbbdd11cf3d140dd)
- Fixed the problem of incorrectly setting the zone group ID when forwarding requests to the main zone group when creating a bucket in a multi-zone group scenario.
  ↳ [#62420](https://github.com/ceph/ceph/pull/62420): [c19b02c](https://github.com/ceph/ceph/commit/c19b02cfc9644710964cba689a272782b7064a12)
- Migrate fscrypt_auth and fscrypt_file metadata to mds_co memory pool and adapt the assignment method.
  ↳ [#59616](https://github.com/ceph/ceph/pull/59616): [b20e89d](https://github.com/ceph/ceph/commit/b20e89dc201158302ae98d5a144af351f1da417a), [4fe4f2d](https://github.com/ceph/ceph/commit/4fe4f2dc55f7e581e4f2ed6d57019f07d158cf99)
- Improve the processing logic of nbd_block_status() callback in NBDStream to avoid data corruption.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [ac8d61a](https://github.com/ceph/ceph/commit/ac8d61a41934dd6d8200d0a827be270a3f3ad69a)
- Fixed the issue where the readlinkat function could not correctly resolve symbolic links when the path name was empty.
  ↳ [#60372](https://github.com/ceph/ceph/pull/60372): [acf6717](https://github.com/ceph/ceph/commit/acf6717bad7d3e6440c28f5f776dbbe53dec9cda)
- Updated s3select submodule, adjusted Parquet read buffer options in RGW and fixed missing return bytes indicator.
  ↳ [#62959](https://github.com/ceph/ceph/pull/62959): [c2fdcaa](https://github.com/ceph/ceph/commit/c2fdcaa1d6f3002dba77751fc3e4bd69023977ab)
- Fixed an issue on Linux systems where opening a symbolic link using the O_PATH and O_NOFOLLOW flags would return an ELOOP error.
  ↳ [#60372](https://github.com/ceph/ceph/pull/60372): [d887a29](https://github.com/ceph/ceph/commit/d887a29fec4553e8170b18e724953a4c2ddee7e0)
- Fixed an issue where errors were not handled correctly when the first shard synchronization failed in multi-site data synchronization.
  ↳ [#62307](https://github.com/ceph/ceph/pull/62307): [71aa9f6](https://github.com/ceph/ceph/commit/71aa9f65e24ec41c9c2a99dd675fd303fb7cc284), [4cfa58b](https://github.com/ceph/ceph/commit/4cfa58be4c41ad6e83f77e7a667c83e90cb17147)
- Fixed the problem of unnecessary mutual awakening between threads when discard_drain wait condition.
  ↳ [#62151](https://github.com/ceph/ceph/pull/62151): [ce3906e](https://github.com/ceph/ceph/commit/ce3906e16b8cca87c4f445a0fd451d55bb4e3b6a)
- Fixed the issue where the client returns an EOPNOTSUPP error when the fallocate mode parameter is 0.
  ↳ [#60656](https://github.com/ceph/ceph/pull/60656): [e32d50c](https://github.com/ceph/ceph/commit/e32d50ccaf0a35a5676bf788c5bd635407dff8f4)
- Modify the MonMap::dump function output format to comply with Python test script parsing requirements.
  ↳ [#60629](https://github.com/ceph/ceph/pull/60629): [88a559d](https://github.com/ceph/ceph/commit/88a559dbe44cf310b71daffc84e13509d6af36cb)
- Fixed handling logic for invalid IDs in client eviction operations, treating them as successful.
  ↳ [#60059](https://github.com/ceph/ceph/pull/60059): [d6f034e](https://github.com/ceph/ceph/commit/d6f034eca853e9160ffbbb8934e06b6389e772b4)
- Fixed the issue where the non-primary region request body was not forwarded correctly when creating a bucket in a multi-region group scenario.
  ↳ [#62420](https://github.com/ceph/ceph/pull/62420): [526735e](https://github.com/ceph/ceph/commit/526735e33be73bfec0664443b59d49021be097ea)
- Fix the error of transition rule check in life cycle operation and adjust the default value of transition_action constructor.
  ↳ [#61532](https://github.com/ceph/ceph/pull/61532): [9eb0b5d](https://github.com/ceph/ceph/commit/9eb0b5d896423d3ccb1027fa0e5348e2c5fac587)
- Modify the BlueFS truncate() and BlueRocksEnv Close() methods to ensure that unused space allocations are properly released when truncating files or closing the environment.
  ↳ [#60240](https://github.com/ceph/ceph/pull/60240): [d69cc42](https://github.com/ceph/ceph/commit/d69cc42e4a5eaaad61d296b132075b9b68ba94da)
- Fixed the issue where non-current objects cannot be accessed correctly during lifecycle conversion operations when bucket versioning is enabled.
  ↳ [#63030](https://github.com/ceph/ceph/pull/63030): [22b2c37](https://github.com/ceph/ceph/commit/22b2c37164ebe6a8c2d80def703a4d87e412d7dc)
- Fixed the issue where RGW incorrectly performs an empty bucket check when deleting a bucket that is not owned by this zone group. Now the relevant operation is only performed when the bucket belongs to the current zone group.
  ↳ [#62994](https://github.com/ceph/ceph/pull/62994): [8238730](https://github.com/ceph/ceph/commit/8238730f0096a3b11ddb75639cce3473439a6d08)
- Fixed a possible segfault caused by the zone_placement member not being initialized when creating a bucket in a multi-zone group scenario.
  ↳ [#62420](https://github.com/ceph/ceph/pull/62420): [d37535b](https://github.com/ceph/ceph/commit/d37535ba3132a977116374282fbd561d0c6aaa2a)
- Fixed the issue where when multiple devices are specified in the ceph-bluestore-tool show-label command, if any device label fails to be read, no result will be output. Now the result will be output regardless of whether the label is readable or not.
  ↳ [#60543](https://github.com/ceph/ceph/pull/60543): [19589c5](https://github.com/ceph/ceph/commit/19589c560c12471ccfedfd163141c999273411bf)
- Fixed an issue where when a block device is expanded, the device label copy location may be crossed, causing the new label to be uninitialized.
  ↳ [#61671](https://github.com/ceph/ceph/pull/61671): [ec48444](https://github.com/ceph/ceph/commit/ec48444fc5db8ae7d785599bc04c840fc5cd2d15)
- Fixed the validation logic of the sync group pipe modify command when specifying a user, allowing the command to be used when the user has been set.
  ↳ [#60979](https://github.com/ceph/ceph/pull/60979): [1706d3c](https://github.com/ceph/ceph/commit/1706d3c6da2442b445b139caef0e72015ce5119c)
- Fixed an issue where MDS logs frequently create new segments causing delays when exporting a large number of subtrees. A new primary segment will now be started after the configured number of secondary segments threshold is reached.
  ↳ [#60838](https://github.com/ceph/ceph/pull/60838): [58472d2](https://github.com/ceph/ceph/commit/58472d2d786e2d50092bac58a2edd81176137c03)
- Add fscrypt metadata length to inode stat size calculation, fix related calculation issues.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [70f2263](https://github.com/ceph/ceph/commit/70f2263ddab50dda70f9921de96adaa7e40c8d38)
- Fixed the issue where the character mapping of the parent directory was not inherited when creating a directory, ensuring that the newly created directory can correctly inherit the character mapping settings.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [74c2501](https://github.com/ceph/ceph/commit/74c2501ab035c1396d86b490f6c73530b0dc8e2f)
- Added check for character mapping capabilities when handling client symlink requests.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [409525b](https://github.com/ceph/ceph/commit/409525b530adafa75a534bf16caac791bc12b3a6)
- Use DentryRef in MetaRequest for reference counting to fix related resource management issues.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [156849b](https://github.com/ceph/ceph/commit/156849b2e7ed7dd04945d6187bd2b7a16aba1cfa)
- Fix redundant ceph_close() calls in cephfs-mirror to avoid file descriptor conflicts, and refactor synchronization logic to properly close file descriptors.
  ↳ [#61100](https://github.com/ceph/ceph/pull/61100): [c4ce3c0](https://github.com/ceph/ceph/commit/c4ce3c06617a2ee12f80a5c2bce6dc2942f62491)
- Fix missing file descriptor reset operation in dir_result_t::reset() method, ensure fd is set to -1 when resetting directory results.
  ↳ [#61100](https://github.com/ceph/ceph/pull/61100): [442e645](https://github.com/ceph/ceph/commit/442e64586612e463a310d1b2ab6f60c108455d48)
- Add a lock mechanism to the AbortMultipartUpload operation to resolve potential race conditions.
  ↳ [#61134](https://github.com/ceph/ceph/pull/61134): [adb3aa7](https://github.com/ceph/ceph/commit/adb3aa7cdadf7fa07e6cce89df181f7cd7ca82ac)
- Rollback fix for AuthStrategy return codes to resolve a regression with EC2 authentication when rgw_s3_auth_order is configured to prioritize local over external.
  ↳ [#61162](https://github.com/ceph/ceph/pull/61162): [f289b91](https://github.com/ceph/ceph/commit/f289b91f080a8e3ffb8cb4b0a29b948d0302738b)
- Fixed RGW bucket linking operation, now allowing unassociated buckets to be linked.
  ↳ [#61051](https://github.com/ceph/ceph/pull/61051): [b202a5f](https://github.com/ceph/ceph/commit/b202a5fcad338c79c2e916379f57bdb6927f101f)
- Fixed an issue where a RADOS operation timeout or file non-existence error when deleting an object may cause the bucket index to be incorrectly updated, ensuring that index entries can be correctly restored by subsequent operations.
  ↳ [#61062](https://github.com/ceph/ceph/pull/61062): [84bfb1b](https://github.com/ceph/ceph/commit/84bfb1b9d5aa0e6b212e52f5b35da53dd608fa1e)
- Fixed the problem of data corruption that may be caused by RADOS operation timeout. The object collection written in RadosWriter will now be cleared when a timeout error is encountered.
  ↳ [#61092](https://github.com/ceph/ceph/pull/61092): [6350558](https://github.com/ceph/ceph/commit/63505589868855553843346e257b74cc7e794e89)
- Fixed an issue where the redirect URL did not add the question mark correctly when it contained the query string, now the question mark and parameters are only appended when the query parameters are non-empty.
  ↳ [#61159](https://github.com/ceph/ceph/pull/61159): [13ad910](https://github.com/ceph/ceph/commit/13ad910798c7b4d5f9c76131eac7d7bf68db095e)
- Fix to avoid calling index_op->cancel() when a RADOS operation times out, to prevent data corruption and allow index recovery with subsequent checks.
  ↳ [#61092](https://github.com/ceph/ceph/pull/61092): [f884b59](https://github.com/ceph/ceph/commit/f884b591631db9af58173ba118b35b3e0d8392f8)
- Fixed the 403 error caused by sending internal headers when getting objects from the cloud endpoint, and removed unnecessary RGW internal request parameters.
  ↳ [#63030](https://github.com/ceph/ceph/pull/63030): [6f9dca5](https://github.com/ceph/ceph/commit/6f9dca5bd3e7d577e467b0bc2b3e2f33795f8087)
- Fixed an issue where NoSuchKey was incorrectly mapped to NoSuchUpload in RGWAbortMultipart.
  ↳ [#61134](https://github.com/ceph/ceph/pull/61134): [ca9fd12](https://github.com/ceph/ceph/commit/ca9fd124bbcd1aa6207c26dba9337bb2c86c0534)
- Register for the OSD module to monitor changes in the osd_max_scrubs configuration item to ensure that the asynchronous cleaning reserved parameters can be updated in time.
  ↳ [#61185](https://github.com/ceph/ceph/pull/61185): [ae1bb40](https://github.com/ceph/ceph/commit/ae1bb4012266a7f11f301600bdb6eca677b8d460)
- Fixed the issue of crash caused by exception when enumerating storage pools. Related errors will now be captured and handled.
  ↳ [#61306](https://github.com/ceph/ceph/pull/61306): [84d7d71](https://github.com/ceph/ceph/commit/84d7d71b43fe5d3c90ec7078ebecd5a1fcb58fc4)
- Fixed the problem of extents_index not being updated synchronously in BlueFS::truncate() to prevent seek operations from accessing invalid indexes after file truncation.
  ↳ [#60240](https://github.com/ceph/ceph/pull/60240): [d010016](https://github.com/ceph/ceph/commit/d010016f5cb098037ffa6da329d356942729f819), [b8e62e7](https://github.com/ceph/ceph/commit/b8e62e700a9ad7a10be3d4957613f49791dc1c8a), [bbe2837](https://github.com/ceph/ceph/commit/bbe2837053f4ecdbbf281a4bbbf0bbb347920e1e)
- Fixed Invalid group uri error in s3cmd setacl command, which was introduced by account change in squid version.
  ↳ [#62526](https://github.com/ceph/ceph/pull/62526): [bc7dfb4](https://github.com/ceph/ceph/commit/bc7dfb42b04e2548f402d4cb8475ae478ead5dc6)
- Fixed the problem of compression plug-in preloading and option acquisition logic when BlueStore is mounted.
  ↳ [#62143](https://github.com/ceph/ceph/pull/62143): [1b29659](https://github.com/ceph/ceph/commit/1b29659628714fe33ebbea2644474ae43d13040a)
- Fixed an issue where tenant information was not forwarded correctly when a system user requested to create a bucket with a tenant in a multi-site scenario.
  ↳ [#62310](https://github.com/ceph/ceph/pull/62310): [5972152](https://github.com/ceph/ceph/commit/597215293442f8d17a56ee52cfd87c3c79f60dea)
- Fixed the issue where DBStore did not correctly update the bucket attributes when performing the put_info operation, ensuring that the updated attributes can be correctly saved to the backend storage after deleting the attributes.
  ↳ [#61995](https://github.com/ceph/ceph/pull/61995): [3967b6a](https://github.com/ceph/ceph/commit/3967b6a7eaba9e990cd511c8724e9ad666ea0379)
- Fixed the problem of incorrect multi-tag processing code position when BlueStore expanded the block device, and moved the relevant logic to the correct code block.
  ↳ [#61671](https://github.com/ceph/ceph/pull/61671): [10d4453](https://github.com/ceph/ceph/commit/10d4453488bae8008ab40428a20ddcaea0e1ca52)
- Fixed potential memory access issues with librbd Image::close() and Image::aio_close(), ensuring that the ctx pointer is cleared before the close operation to prevent the callback function from closing the image repeatedly.
  ↳ [#61527](https://github.com/ceph/ceph/pull/61527): [aba7c2a](https://github.com/ceph/ceph/commit/aba7c2a54fb58dd71e7672394cd938c26f00ef36)
- Fixed the handling of health check requests by Lua scripts in RGW to avoid forwarding them to backend storage.
  ↳ [#62034](https://github.com/ceph/ceph/pull/62034): [9fbbf6e](https://github.com/ceph/ceph/commit/9fbbf6ea47a109f4ecb56120fb40054d1b2c7a22)
- Fixed the permission check logic for unmanaged snapshots in OSDMonitor and relaxed the judgment conditions of the is_osd_writable function.
  ↳ [#61603](https://github.com/ceph/ceph/pull/61603): [346ab84](https://github.com/ceph/ceph/commit/346ab845796d3ff5160d213130dfbc0fb5a82d7a)
- Fixed misleading description of pool names and namespace restrictions in OSDCap syntax comments.
  ↳ [#61603](https://github.com/ceph/ceph/pull/61603): [f0e8d50](https://github.com/ceph/ceph/commit/f0e8d50b7c4176dd27c23767eff0e76880c481e2)
- Fixed a function in the CephFS mirror tool to avoid taking into account the latest changes to the source file system when the mirror already has a snapshot.
  ↳ [#63241](https://github.com/ceph/ceph/pull/63241): [6c78a52](https://github.com/ceph/ceph/commit/6c78a52f989c00a3d5281f4119dd5de096168f59)
- When deleting objects, set the option to allow retries when the pool quota is full to support deleting objects when the quota limit is reached.
  ↳ [#62093](https://github.com/ceph/ceph/pull/62093): [192777d](https://github.com/ceph/ceph/commit/192777d5e62f800313baed9ae09d3efdfffc4d13), [4478bb4](https://github.com/ceph/ceph/commit/4478bb419cc92c84ed4f80a7c7c3d718572294dc)
- Fixed a race condition in the RadosBucket::create method when handling concurrent bucket deletion requests.
  ↳ [#62741](https://github.com/ceph/ceph/pull/62741): [fc07745](https://github.com/ceph/ceph/commit/fc07745146b0613be8b09484d52ce676bce44e5b)
- Fixed an issue where the dmclock server may incorrectly remove clients that still have queued requests when cleaning them up.
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [ef4f0d5](https://github.com/ceph/ceph/commit/ef4f0d5369e85209da5b18a3ad5ee0177590018d)
- Fixed logic error when creating federated users in the OIDC namespace, replacing load_stats calls with list_buckets.
  ↳ [#62386](https://github.com/ceph/ceph/pull/62386): [bd9b975](https://github.com/ceph/ceph/commit/bd9b9752e81081f0ae8591cd20e49b2227d61afe)
- Fix possible recursive lock issues with ImageReplayer::m_lock.
  ↳ [#62042](https://github.com/ceph/ceph/pull/62042): [f9c17ce](https://github.com/ceph/ceph/commit/f9c17ce38fd708f7a0c7f58b3e90cba607d4b2e7)
- Fixed BlueStore bdev label size not being updated correctly when extending the device, and an assertion error that could be raised by performing fsck when the device volume was not fully extended.
  ↳ [#62202](https://github.com/ceph/ceph/pull/62202): [60c87f3](https://github.com/ceph/ceph/commit/60c87f3724509c38bada11af85563179550c93bb), [828b402](https://github.com/ceph/ceph/commit/828b4022ed186493d887e33aa60d38c5092ccf41)
- In STS AssumeRoleWithWebIdentity responses, client_id is now used as the audience value when the JWT does not provide an aud field.
  ↳ [#63052](https://github.com/ceph/ceph/pull/63052): [9343a5c](https://github.com/ceph/ceph/commit/9343a5cd6236adb5abe9230d01744a8bb059e2c4)
- Fixed multiple issues in BlueStore/BlueFS during device expansion, tag verification and allocator update.
  ↳ [#62202](https://github.com/ceph/ceph/pull/62202): [b567f85](https://github.com/ceph/ceph/commit/b567f85c56f681f77586fe2b5a12440b4d58dbfc), [3b7f16e](https://github.com/ceph/ceph/commit/3b7f16ec84c781503e829e52887dbbbfdf3d4ed1), [5c5aa44](https://github.com/ceph/ceph/commit/5c5aa44208599d1f4902be8b643bb07fdbb9dae3), [dc23cf4](https://github.com/ceph/ceph/commit/dc23cf4474e2a7effc784377361ec615cded8df1)
- Modify the message distribution logic and change the processing result of map messages from "unprocessed" to "confirmed" to avoid unnecessary unprocessed message logs.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [018255a](https://github.com/ceph/ceph/commit/018255a164189463ebc2e212705686c75c2bdfd8)
- Modify the client's logic for processing command replies so that it returns false instead of directly when encountering an unknown transaction ID; at the same time, the timeout error code when closing the session is changed from CEPHFS_ETIMEDOUT to ETIMEDOUT.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [e91a2d0](https://github.com/ceph/ceph/commit/e91a2d04c4625b2b6620cfd48cea5ec0f4f74346)
- Initialize the shared algebra of directory entries to an invalid value to more accurately identify placeholder directory entries.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [944ef3b](https://github.com/ceph/ceph/commit/944ef3bcbac78adc169ac44572ca95757cc6ca30)
- Fixed a crash in the `get_rollback_snap_id` function caused by not checking whether the snapshot is a mirror snapshot.
  ↳ [#62044](https://github.com/ceph/ceph/pull/62044): [2b0ffb1](https://github.com/ceph/ceph/commit/2b0ffb18a6417449c3a6f87095fb93733be054be)
- Fixed an issue where LogMonitor did not correctly set the no_reply flag when forwarding MLog commands to avoid slow operations in OSD removal and add operations.
  ↳ [#62213](https://github.com/ceph/ceph/pull/62213): [1bf93fc](https://github.com/ceph/ceph/commit/1bf93fc10c676d3a3706a457b6dd8527868f8ce3)
- Modify BlueFS's `_get_total` method so that it no longer subtracts reserved space from the total size of the block device.
  ↳ [#62514](https://github.com/ceph/ceph/pull/62514): [d6ef23c](https://github.com/ceph/ceph/commit/d6ef23cfad55982485047927697dce6743230206), [48fdc4c](https://github.com/ceph/ceph/commit/48fdc4c84f6bf60413cb9e02f7f71e6cebf3e6ba), [7a317c4](https://github.com/ceph/ceph/commit/7a317c4550cc42a5d20ef79fc232e1b391ad520a)
- Fixed an issue where BlueFS was not aligned to the minimum allocation unit when allocating space on DB/WAL volumes.
  ↳ [#62514](https://github.com/ceph/ceph/pull/62514): [47091d1](https://github.com/ceph/ceph/commit/47091d1732b98881ca4a75fb2cf096418ea9eb7b)
- Fixed a deadlock problem in `Mirror::image_disable()` caused by holding the `image_lock` write lock.
  ↳ [#62128](https://github.com/ceph/ceph/pull/62128): [0d0bfc6](https://github.com/ceph/ceph/commit/0d0bfc69b37b10d54ed1c0f73b3ab3b58b48b643)
- Added set_pool_full_try() call to rgw_init_ioctx() function to return an error immediately when the storage pool reaches the quota limit.
  ↳ [#62559](https://github.com/ceph/ceph/pull/62559): [15dea26](https://github.com/ceph/ceph/commit/15dea26afd86c7170c099cc19a4957baf11ef09e)
- Fixed snapshot difference (snapdiff) related functions, including the issue that deleted files are not included when directory reading.
  ↳ [#63241](https://github.com/ceph/ceph/pull/63241): [36c8cb5](https://github.com/ceph/ceph/commit/36c8cb5f60483066d7b6a2f6d7be809bc63307ed), [196c79a](https://github.com/ceph/ceph/commit/196c79aa316079a10c858720d1a094cc4e69072b)
- Fixed the error handling and reconnection logic of RGW related components, including the reconnection condition of the synchronization fairness monitor and the unwatch error handling of the RGW monitor.
  ↳ [#62356](https://github.com/ceph/ceph/pull/62356): [61c8a1c](https://github.com/ceph/ceph/commit/61c8a1c9c37d42afa243358b2bc8c1b9d5584642) | [#62402](https://github.com/ceph/ceph/pull/62402): [ff248d7](https://github.com/ceph/ceph/commit/ff248d7ed94cc441a2e7f3254cb8c0d53d3997d1)
- Fixed output issues with the `ceph` command line tool, including the `ceph node ls` command listing destroyed OSDs.
  ↳ [#62327](https://github.com/ceph/ceph/pull/62327): [6dcf12b](https://github.com/ceph/ceph/commit/6dcf12b3ae714f7c96e0cc43a863dcdb1ada04a9) | [#62534](https://github.com/ceph/ceph/pull/62534): [6839d2d](https://github.com/ceph/ceph/commit/6839d2d5af2e26d693f57b59faec5db5d05549ba)
- Fixed concurrency and regression issues in RGW bucket operations, including error handling of bucket creation operations when buckets are deleted concurrently.
  ↳ [#62741](https://github.com/ceph/ceph/pull/62741): [0422945](https://github.com/ceph/ceph/commit/04229454bc192414f7d89befb68b6d8d3f89ced7) | [#62417](https://github.com/ceph/ceph/pull/62417): [260bd9c](https://github.com/ceph/ceph/commit/260bd9c7500bce2246d440f75b994c49a62fdd2b)
- Fixed a possible infinite loop issue in non-versioned lists when skipping versioned entries.
  ↳ [#62590](https://github.com/ceph/ceph/pull/62590): [b49828d](https://github.com/ceph/ceph/commit/b49828d5a1d30feb578f2282b217567fb519c522)
- Fix logic for detecting "forward progress" in `list_objects_ordered()` to correctly handle multiple versions of the same object name.
  ↳ [#62590](https://github.com/ceph/ceph/pull/62590): [a025b04](https://github.com/ceph/ceph/commit/a025b04c534c916204623503e0173a8e2d4cc4bb)
- Set and verify alternative names for newly created full bit directory entries during metadata log replay.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [4f71a93](https://github.com/ceph/ceph/commit/4f71a93109e55d6a06cfc1a2988fc5d4d4958164)
- Fixed the problem of iterator invalidation after erase operation during discard_queued traversal in KernelDevice.
  ↳ [#62576](https://github.com/ceph/ceph/pull/62576): [04b9a32](https://github.com/ceph/ceph/commit/04b9a327f3d00e970d226b7b1f6a53a1dcc3e374)
- Fixed invariant check failure due to missing new_object tag when deleting log entries.
  ↳ [#63154](https://github.com/ceph/ceph/pull/63154): [57c0c20](https://github.com/ceph/ceph/commit/57c0c20cfb00cd6a8a081ba3968fd7f24a90bbea)
- Fixed the issue of retaining tail data when an object is copied to itself, by adjusting the metadata writing logic to correctly handle timeout situations.
  ↳ [#62711](https://github.com/ceph/ceph/pull/62711): [31a9ec0](https://github.com/ceph/ceph/commit/31a9ec02e69df3cf277116b06e1a3de661786f34)
- Fixed the race condition between truncate() and unlink() in BlueFS, by checking whether the file has been deleted under the file lock, avoiding repeated operations and allocation release of deleted files.
  ↳ [#62839](https://github.com/ceph/ceph/pull/62839): [8c54196](https://github.com/ceph/ceph/commit/8c541963b60ce957f112f3a5ae0da68b8a7ccd47)
- Fixed a potential segfault issue in CephContext::_refresh_perf_values() caused by not checking whether the _mempool_perf pointer was null.
  ↳ [#62852](https://github.com/ceph/ceph/pull/62852): [2972b20](https://github.com/ceph/ceph/commit/2972b204b3595617281463b7bd7d17c2d7a05fc3)
- Fixed an issue where metadata and data synchronization shard notifications failed to retry when encountering any errors (including timeouts) and will now continue to retry in a loop.
  ↳ [#62356](https://github.com/ceph/ceph/pull/62356): [0d9ee21](https://github.com/ceph/ceph/commit/0d9ee21d0714b2f347e0794b107957b2ae689f94)
- Fixed an issue where the radosgw-admin bucket object shard command might cause a crash when the number of shards parameter is zero or negative. It will now return an error code instead of triggering a divide-by-zero exception.
  ↳ [#62884](https://github.com/ceph/ceph/pull/62884): [456a5e6](https://github.com/ceph/ceph/commit/456a5e661d1356f1cee87783179385996183f63d)
- It is forbidden to move the images belonging to the group into the recycle bin, except in migration scenarios; the relevant error message has also been improved.
  ↳ [#62968](https://github.com/ceph/ceph/pull/62968): [c31ec02](https://github.com/ceph/ceph/commit/c31ec028c987b647b56401cd1c8d024eba49b872)
- Fixed the lock competition problem of the start_image_replayers function in rbd-mirror. Release the mutex lock before calling m_async_op_tracker.finish_op() to avoid deadlock caused by non-recursive lock reentrancy.
  ↳ [#64092](https://github.com/ceph/ceph/pull/64092): [7e38b56](https://github.com/ceph/ceph/commit/7e38b56bb58365713d773190bb7b9809442ce5f3)
- Fixed an issue where the image will expire at message was incorrectly printed when the trash_move() operation failed.
  ↳ [#62968](https://github.com/ceph/ceph/pull/62968): [663054e](https://github.com/ceph/ceph/commit/663054e73c833848e445341df4a1e1b3a7e8e17a)
- Fixed the issue where the mirror status displayed by the rbd info command was incorrect when creating a mirror on a secondary node. It will now be correctly displayed as "creating".
  ↳ [#62940](https://github.com/ceph/ceph/pull/62940): [14213e3](https://github.com/ceph/ceph/commit/14213e37140bce47acd35fae10fdf8c8e7a78ad7)
- Fixed the duration calculation of the OSD scrub report and changed it to round up to comply with test expectations and improve user readability.
  ↳ [#62995](https://github.com/ceph/ceph/pull/62995): [5d47ec1](https://github.com/ceph/ceph/commit/5d47ec198af675bfc0e92e5853f4d0445a843110)
- Fixed an issue where the mirror image status was not written when the mirror status was CREATING to reduce the delay in status writing of newly created mirrors on the secondary node.
  ↳ [#63234](https://github.com/ceph/ceph/pull/63234): [9a0763e](https://github.com/ceph/ceph/commit/9a0763ec96fe34cdaa23b42f2c6ed114c9d8b797)
- Fixed an issue where the error code returned by the management API was incorrect when deleting a non-existing bucket.
  ↳ [#63405](https://github.com/ceph/ceph/pull/63405): [97c51f5](https://github.com/ceph/ceph/commit/97c51f5796780eeb7771002b619b89769d493110)
- Fixed the logic for the RGW REST interface to determine the domain name URI prefix when using an SSL termination proxy. Instead, use the rgw_transport_is_secure function to determine connection security instead of relying solely on the SERVER_PORT_SECURE environment variable.
  ↳ [#63363](https://github.com/ceph/ceph/pull/63363): [1f03941](https://github.com/ceph/ceph/commit/1f039419c5136daff56d3fb5c3272c6c749b821f)
- Fixed the aio_idle_time configuration value of libaio in D3nDataCache::init, reducing it from 5 seconds to 2 seconds to alleviate Valgrind false positives caused by possible memory read race conditions on exit.
  ↳ [#63438](https://github.com/ceph/ceph/pull/63438): [71c95b8](https://github.com/ceph/ceph/commit/71c95b8c65701ddd2e021c325fbbdb2ba42fa00c)
- Add empty string check after URL decoding to prevent RGW from crashing due to malformed x-amz-copy-source.
  ↳ [#64049](https://github.com/ceph/ceph/pull/64049): [cc10fd6](https://github.com/ceph/ceph/commit/cc10fd69eaa9d8838dc73757d3930e9e23bc3fb9)
- Fixed the processing logic of the url_decode function when encountering invalid hexadecimal encoding to avoid RGW crash due to repeated decoding.
  ↳ [#64049](https://github.com/ceph/ceph/pull/64049): [b20a71f](https://github.com/ceph/ceph/commit/b20a71f9c8800cf5749c8aff3e08ba62ad51cc79)
- Fixed a memory leak issue during SyncPoint persistence context cleanup in the librbd cache layer, ensuring that all allocated contexts are properly released on shutdown.
  ↳ [#64097](https://github.com/ceph/ceph/pull/64097): [97f2434](https://github.com/ceph/ceph/commit/97f2434d23836b8032dceeed76d73d3ec77f386d)
- Restored the old behavior of the url_decode function, which directly returned an empty string when encountering an invalid hex encoding.
  ↳ [#64049](https://github.com/ceph/ceph/pull/64049): [80b044e](https://github.com/ceph/ceph/commit/80b044e202a8b7ebd21b5c498946d9bd59b282bb)
- Fixed a potential deadlock issue in QCOWFormat migration where read_clusters() was completed inline in special cases, now done asynchronously via ASIO.
  ↳ [#64196](https://github.com/ceph/ceph/pull/64196): [308101c](https://github.com/ceph/ceph/commit/308101c68c3abffa573c779d05332052a45f7e1a)
- Fixed wrong keyword for free-fragmentation command in ceph-bluestore-tool.
  ↳ [#62125](https://github.com/ceph/ceph/pull/62125): [0268341](https://github.com/ceph/ceph/commit/026834181bf4491635fac933bd777304c2aa17c9)
- Added OSDService::fast_shutdown method to avoid segfault when OSD is shut down quickly.
  ↳ [#57613](https://github.com/ceph/ceph/pull/57613): [f1abf5c](https://github.com/ceph/ceph/commit/f1abf5c3423fa4c540bf5f31ad2765fc98e50d78)
- Fixed the issue where the request payment information was incorrectly recorded when processing a 403 error request.
  ↳ [#62305](https://github.com/ceph/ceph/pull/62305): [f9ba21a](https://github.com/ceph/ceph/commit/f9ba21a87f31c907a43efe5fd7b608a10cd68f3d)
- Removed the scaling factor used in calculating max_avail in PGMap to correct the available space reported when the OSD is down but not out.
  ↳ [#62437](https://github.com/ceph/ceph/pull/62437): [720ec8c](https://github.com/ceph/ceph/commit/720ec8c439f7caa8320b1d6963ba3f76ede4ef33)
- Discard client metric messages during MDS recovery to fix related issues.
  ↳ [#59866](https://github.com/ceph/ceph/pull/59866): [819a7a2](https://github.com/ceph/ceph/commit/819a7a20ec9d5e2e1947bd6bf30ac7807d1a80ed)
- Fixed a potential issue in the logback_generations function where locks were used after being moved, and fixed a situation where locks were held during I/O operations.
  ↳ [#61330](https://github.com/ceph/ceph/pull/61330): [c9e9744](https://github.com/ceph/ceph/commit/c9e9744e9faf145289526c72d53d46ab75a04f01)
- Fixed an issue where invalid iterators may be dereferenced when data is corrupted, improving the robustness of the code.
  ↳ [#62053](https://github.com/ceph/ceph/pull/62053): [04a2763](https://github.com/ceph/ceph/commit/04a2763a9379a96d4f3e886c46dc5e3257e12c3c)
- In the Monitor::_scrub function, when an error occurs in getting data from storage, detailed error information will now be printed and execution will be aborted.
  ↳ [#61346](https://github.com/ceph/ceph/pull/61346): [62a9e41](https://github.com/ceph/ceph/commit/62a9e41f3a5192160ac4fd799fafaf6b38923115)
- Fixed fs set down false command incorrectly setting max_mds to 1 when the cluster is online.
  ↳ [#59704](https://github.com/ceph/ceph/pull/59704): [318e583](https://github.com/ceph/ceph/commit/318e5831098265405567fea947541bbb1720ccc7)
- Fixed the return value and iterator type of the _remove_from_tree method in the mixed btree2 allocator to resolve an "invalid read" error reported by valgrind.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [715a081](https://github.com/ceph/ceph/commit/715a0810e303dc165a1dba8edfdf572f5153faba)
- In the client file system synchronization operation, a new step is added to explicitly refresh the capability release to solve the race condition between the capability release and the withdrawal request.
  ↳ [#59395](https://github.com/ceph/ceph/pull/59395): [60ace3d](https://github.com/ceph/ceph/commit/60ace3d97f953d13d9f5938cd1b639d763640d89)
- Fixed extra newlines in the output of getxattr command in rados tool.
  ↳ [#60687](https://github.com/ceph/ceph/pull/60687): [a528a0d](https://github.com/ceph/ceph/commit/a528a0dcda1834d80f351303db83488e8a9ca442)
- Introduced auxiliary functions in librbd's NBDStream migration module to fix error code conversion issues.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [8e0b87d](https://github.com/ceph/ceph/commit/8e0b87dd06439ddbf2d41fc124103fbbc5a45e8a)
- Fixed the issue where alternate_name in Client::insert_readdir_results was repeatedly moved and caused to be cleared.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [bbe6d9c](https://github.com/ceph/ceph/commit/bbe6d9c1ecfee76b3e88f7b08aefe921ebc64a77)
- Fixed an issue in BlueStore where ceph::time_guard objects may be destroyed immediately because they are not assigned to named variables.
  ↳ [#61971](https://github.com/ceph/ceph/pull/61971): [f81aaf0](https://github.com/ceph/ceph/commit/f81aaf09dbd60c442dbb8dc252b23eada9aea12e)
- Fixed an issue where the discard operation performance counter counted the number of operations instead of the number of bytes.
  ↳ [#62254](https://github.com/ceph/ceph/pull/62254): [967d0d0](https://github.com/ceph/ceph/commit/967d0d04ee224097e482c50095e13b376b8a9ad4)
- Fixed the label checking logic of the bucket_exports_object function, declared it as a const member function and adjusted the parameter passing when calling.
  ↳ [#60785](https://github.com/ceph/ceph/pull/60785): [0a67cd2](https://github.com/ceph/ceph/commit/0a67cd259891b1a7831c9221c8e47426f509d19e)
- Removed redundant error capture callbacks in RGWDataFullSyncShardCR.
  ↳ [#62307](https://github.com/ceph/ceph/pull/62307): [936099a](https://github.com/ceph/ceph/commit/936099af41d7f87388b463741612a30eacd09ffc)
- Optimized BlueFS's truncate() function, removed unused assertions and improved code logic.
  ↳ [#60240](https://github.com/ceph/ceph/pull/60240): [c9b9066](https://github.com/ceph/ceph/commit/c9b90664f87941db3cf122f92bbd8e4dd77b6b37)
- Moved Inode dumping logic from global functions to member methods.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [7cf2a57](https://github.com/ceph/ceph/commit/7cf2a5740959eeff06de3c90ea10277025443303)
- Change the encode_lease function from a static method to a normal member method of the class.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [12ae0bf](https://github.com/ceph/ceph/commit/12ae0bfbc98bb8d09c4bf6999b0545c14073aabf)
- In FUSE initialization, direct access to member variables is changed to calling accessor functions.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [9fd4cd3](https://github.com/ceph/ceph/commit/9fd4cd3def59037653e6c9f95f04ad84798716e0)
- Shortened the name prefix of RGW lifecycle manager worker threads.
  ↳ [#61484](https://github.com/ceph/ceph/pull/61484): [3b3ceac](https://github.com/ceph/ceph/commit/3b3ceacee0263084b19db8b9c2969ff4c10a41af)
- Removed redundant default namespace IoCtx copy operations in rbd mirror status and pool status commands.
  ↳ [#61832](https://github.com/ceph/ceph/pull/61832): [0d1bdaf](https://github.com/ceph/ceph/commit/0d1bdaf3408df9766a7cbd22e143fefde17919c9)
- Removed a redundant condition check in the client code, simplifying the judgment logic of directory entry sharing capabilities.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [1bba7fc](https://github.com/ceph/ceph/commit/1bba7fcf548a530b794907389c95869b4a68d8c6)
- Improved the log output format in the MgrMonitor::create_initial function to improve readability.
  ↳ [#60562](https://github.com/ceph/ceph/pull/60562): [8048687](https://github.com/ceph/ceph/commit/80486871eb95a24cd8a5d4926e40137d11fd03e4)
- Added debug log in MgrMonitor module disable action.
  ↳ [#60562](https://github.com/ceph/ceph/pull/60562): [53d607f](https://github.com/ceph/ceph/commit/53d607f735c139464ac3565edc4d2e4bb970653c)
- Removed the unused btrfs_ioctl.h header file and its related test files.
  ↳ [#60613](https://github.com/ceph/ceph/pull/60613): [13ee6fc](https://github.com/ceph/ceph/commit/13ee6fce017f41a77e943e3d18b222247497341d)
- Fixed a compilation warning where the return value of write() in the signal_shutdown function in the rgw/posix driver was not correctly ignored.
  ↳ [#61147](https://github.com/ceph/ceph/pull/61147): [26a2b2c](https://github.com/ceph/ceph/commit/26a2b2c8b93bef6c2140dbff0ace309bf6932bab)
- Updated the graph panel in the CephFS overview dashboard from the legacy SimpleGraphPanel to the TimeSeries panel.
  ↳ [#62381](https://github.com/ceph/ceph/pull/62381): [004e1f2](https://github.com/ceph/ceph/commit/004e1f2aef4ad9e8efb1d76c82bb74ada9a6d363)
- Improved the error log message of the Processor::accept function in AsyncMessenger.cc to make it clearer and more accurate.
  ↳ [#61401](https://github.com/ceph/ceph/pull/61401): [efe59b4](https://github.com/ceph/ceph/commit/efe59b4ea78fc4e4cdb1772890e16cf8eaf08841)
- Downgrade the log level of undecoded bdev tags in BlueStore from error to normal log.
  ↳ [#62202](https://github.com/ceph/ceph/pull/62202): [af72ad9](https://github.com/ceph/ceph/commit/af72ad93325373ddfbed7aec60adbb2c9aabeb4c)
- Updated multiple chart panels in the Host Details and Host Overview dashboards from the old SimpleGraphPanel format to the new TimeSeries panel format.
  ↳ [#62382](https://github.com/ceph/ceph/pull/62382): [0614b2c](https://github.com/ceph/ceph/commit/0614b2c70482b98ef10f38c1b9aa68b909a5b343)
- Added debug logging for client configuration change handling functions.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [371dce4](https://github.com/ceph/ceph/commit/371dce40104660cd9a7a992ec1dd7c696ee109db)
- Added debugging logs in the client mounting function to record mounting parameters.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [afd2c77](https://github.com/ceph/ceph/commit/afd2c776701acdd993d05984c6e9b4c17e0adf53)

### Refactoring optimization
- Refactor the mix allocator implementation to support alternative mix allocator implementations based on the same code base.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [73231b7](https://github.com/ceph/ceph/commit/73231b70c49fd209af2835a426d3d7c352888725)
- Moved and renamed ExtentCache related functions to the Allocator class, and added a new allocation method of Btree2Allocator.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [81774d3](https://github.com/ceph/ceph/commit/81774d36a7231e05fb724542008c0163ef87f92a)
- Refactored the histogram statistics logic of the Bluestore allocator to use ExtentCollectionTraits for more general interval collection, and optimized the verification of allocation units.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [ea29bac](https://github.com/ceph/ceph/commit/ea29baca3d269c0fcc3f5a69fe8e5c97d275a744), [fe4bea7](https://github.com/ceph/ceph/commit/fe4bea71462bd71ce268c9a7e77217b2f5a65a18), [bc2e61a](https://github.com/ceph/ceph/commit/bc2e61af66789fee5abb9eff02deaaf1f8f6655c)
- In RGW's pubsub push module, the custom Waiter class was removed, a general asynchronous waiter was used instead, and relevant unit tests were added to verify coroutine recovery in multi-threaded scenarios.
  ↳ [#62337](https://github.com/ceph/ceph/pull/62337): [3b13a0e](https://github.com/ceph/ceph/commit/3b13a0ee98844ed8710b6d270b1b44c68451710e)
- Refactor AlienStore::omap_get_values() implementation, removing Seastar specific overloads in BlueStore and MemStore.
  ↳ [#61363](https://github.com/ceph/ceph/pull/61363): [0c9809c](https://github.com/ceph/ceph/commit/0c9809c6493cf6d0b28da68b8403df192ebf15df)
- Reconstruct the client path traversal logic, handle it uniformly through the path_walk function, and fix the readlink permission check problem.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [de04ceb](https://github.com/ceph/ceph/commit/de04ceb2c2ce78bcfebad479751fccdb8bb9db84)
- Reconstruct the RGWOp_Bucket_Remove::execute function, unify the bucket deletion logic and add support for tenants and bypass garbage collection parameters.
  ↳ [#62994](https://github.com/ceph/ceph/pull/62994): [e2a2aba](https://github.com/ceph/ceph/commit/e2a2aba08832709ae82f247c631b3af0b917c012)
- Remove the fast distribution related methods of the ClusterWatcher class in the cephfs_mirror tool.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [61f1b20](https://github.com/ceph/ceph/commit/61f1b204874e9f5684a0f6abd1fe9a43ef3ef711)
- Changed ioctx_create() call in RGWRadosRemoveCR::send_request to rgw_init_ioctx().
  ↳ [#62559](https://github.com/ceph/ceph/pull/62559): [697a07b](https://github.com/ceph/ceph/commit/697a07b10e287d5b4486a42805e770f274f189a8)
- Reconstruct the client directory operation function and unify the path search logic in do_mkdirat and do_symlinkat.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [e635fb0](https://github.com/ceph/ceph/commit/e635fb0cc532d687af742aedb2f2d505264f46d9)
- Refactor the client's chdir and getcwd functions to remove unnecessary getcwd calls and improve error handling.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [2d4c5e5](https://github.com/ceph/ceph/commit/2d4c5e5bc8a9992bb6ebdc8660516965c970d849)
- In the RGWRados::copy_obj function, the implementation method of retaining tail data when copying an object is changed, from directly setting the keep_tail field of RGWObjState to using write_op.meta.keep_tail.
  ↳ [#62711](https://github.com/ceph/ceph/pull/62711): [5ff220f](https://github.com/ceph/ceph/commit/5ff220fbc9fae93d561057b7f785200bbe632230)
- Optimize MgrMonitor's standby manager promotion logic when the down flag is unset.
  ↳ [#57189](https://github.com/ceph/ceph/pull/57189): [6cdf010](https://github.com/ceph/ceph/commit/6cdf010c81ae3a7647c31aeff7abdbf342bb1a50)
- Changed object tag storage in RGWPutObj from unique_ptr to using RGWObjTags by value.
  ↳ [#60785](https://github.com/ceph/ceph/pull/60785): [28e802e](https://github.com/ceph/ceph/commit/28e802e4aca39888d2bb096cdfc91d8b019707fe)
- Remove the unused m_parent_snap_id member variable in RefreshParentRequest.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [b75d884](https://github.com/ceph/ceph/commit/b75d884e547e72580fb639ae78d635b7f2d65105)
- Add assertion checks for the parent member in the ImageCtx destructor, and change some member variables to in-class initialization.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [f27314b](https://github.com/ceph/ceph/commit/f27314b2c23f0aa2dab0bf70fa5dfce7197fd8fa)
- Reconstruct Onode's omap key decoding logic in BlueStore, and add new methods to reduce circular dependencies.
  ↳ [#61363](https://github.com/ceph/ceph/pull/61363): [8e08d32](https://github.com/ceph/ceph/commit/8e08d32dcf4146f749bf800c7544643e1a4879f7)
- Move the log pruning status detection logic from Beacon to MDLog, and encapsulate the judgment conditions.
  ↳ [#60838](https://github.com/ceph/ceph/pull/60838): [8bc65ef](https://github.com/ceph/ceph/commit/8bc65efa28134ff038bd248ce2d80c62dfb4b13d)
- Removed code that checks offset and length bounds in S3select's Parquet processing.
  ↳ [#62959](https://github.com/ceph/ceph/pull/62959): [14211ef](https://github.com/ceph/ceph/commit/14211ef84bce1a5d77c61f7f40683b06180df6a2)
- Modify the processing results and subsequent behavior of map messages in the client message distribution function.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [2a8a036](https://github.com/ceph/ceph/commit/2a8a036dd997d95c6fc8860dce93fcbc3b14b281)
- Add detailed logging of input parameters in the rgw_bucket_list function and optimize internal logic.
  ↳ [#62590](https://github.com/ceph/ceph/pull/62590): [aa444d1](https://github.com/ceph/ceph/commit/aa444d124a8f074121bda4836e53260ba32fa3d6)
- Simplify the match_policy() function, remove unused flags and optimize the call.
  ↳ [#62435](https://github.com/ceph/ceph/pull/62435): [04a52df](https://github.com/ceph/ceph/commit/04a52dfe96b43aec10d89521afb56b411b0e2d4b)
- Optimize the RGWRadosList::handle_stat_result function, determine names in advance and correct attribute lookup.
  ↳ [#62417](https://github.com/ceph/ceph/pull/62417): [9d15a8c](https://github.com/ceph/ceph/commit/9d15a8c82424755aed66c17274672c6364916b34)
- Renamed handle_read_cluster() method to handle_read_clusters() to more accurately reflect usage.
  ↳ [#64196](https://github.com/ceph/ceph/pull/64196): [d631951](https://github.com/ceph/ceph/commit/d631951a3a53289c495d92d541645f49b6687521)
- Add defensive check in MgrMonitor to only try to discard the state of an active manager if there is one.
  ↳ [#57189](https://github.com/ceph/ceph/pull/57189): [2b8da10](https://github.com/ceph/ceph/commit/2b8da1000eae855b228fb3371e127e82d0eb576e)
- Add debug logs in the log segment expiration callback to record segment information and operation results.
  ↳ [#60688](https://github.com/ceph/ceph/pull/60688): [b604b83](https://github.com/ceph/ceph/commit/b604b833f6486e5eb7d7b11e71aa713860f6a6c6)
- Explicitly add std:: namespace qualifier for standard library types in the manager module.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [996c926](https://github.com/ceph/ceph/commit/996c9261c5748ec7d54a172053c4303c2149f13d)
- Move mClockScheduler's constructor implementation from source file to header file.
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [48fdc19](https://github.com/ceph/ceph/commit/48fdc19d5178b85adcf51e9502017e6e81bf6123)

### Test related
- Added test cases to expose race conditions between truncate and remove operations in BlueFS.
  ↳ [#62839](https://github.com/ceph/ceph/pull/62839): [b0ff2b3](https://github.com/ceph/ceph/commit/b0ff2b3aae0b9262ce911ee47839bf71d7441051)
- Added the time-consuming printing function of allocation operations in the allocator_replay test tool.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [d336e5c](https://github.com/ceph/ceph/commit/d336e5c7f8c7a69130b4beeeb21258fc3c0dc7d6)
- Fixed allocator to avl in object storage tests to ensure test stability.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [27976e8](https://github.com/ceph/ceph/commit/27976e89e7181e404156e9aaf64da560fd8bab4b)
- Added CRC check failure check test and EC pool override option helper functions for C++ tests that append zero length data.
  ↳ [#57586](https://github.com/ceph/ceph/pull/57586): [d9f1d53](https://github.com/ceph/ceph/commit/d9f1d536c126b8e911e51dc68ae7b73b23ed4c02)
- Added test cases for delayed operation replay in mount and read-only mount scenarios for store_test.
  ↳ [#62123](https://github.com/ceph/ceph/pull/62123): [c91ec6f](https://github.com/ceph/ceph/commit/c91ec6f503f94a39e60d8c735f7790ac6fc562bb)
- Added test cases to verify the correctness of continuous reading after non-contiguous memory writing.
  ↳ [#60218](https://github.com/ceph/ceph/pull/60218): [3edfacc](https://github.com/ceph/ceph/commit/3edfacca3501efd80a3828bd7781345b59e80318)
- Fixed the error handling logic of timeout scenarios in watch-notify tests.
  ↳ [#61110](https://github.com/ceph/ceph/pull/61110): [324ed5e](https://github.com/ceph/ceph/commit/324ed5ed94c3b47240fab1b065d1d53a2e650629)
- Fixed issue with bufferlist operation in CrcZeroWrite test.
  ↳ [#57586](https://github.com/ceph/ceph/pull/57586): [f032a12](https://github.com/ceph/ceph/commit/f032a12cb25ba36ebc2152a857aaba76fabdd059)
- Updated the set_allow_ec_overwrites test method and added retry logic waiting for the configuration application.
  ↳ [#57586](https://github.com/ceph/ceph/pull/57586): [9981296](https://github.com/ceph/ceph/commit/9981296bf0433eab346094426cb96da5489ccfbd)
- Fixed the EC overwrite cleanup logic in the CrcZeroWrite test and moved the pool reconstruction to the TearDown stage.
  ↳ [#57586](https://github.com/ceph/ceph/pull/57586): [652c502](https://github.com/ceph/ceph/commit/652c5025a957ea4dc4a0a5ee333b7d24da1e18da)
- Adjust wait logic in compression tests to ensure collection removal is complete before continuing.
  ↳ [#62143](https://github.com/ceph/ceph/pull/62143): [e53cf78](https://github.com/ceph/ceph/commit/e53cf780e36c867c4599955f802351554746fdf0)
- Added constructor for mClockScheduler to facilitate unit testing.
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [0e26bb3](https://github.com/ceph/ceph/commit/0e26bb3173574f000f2574eb902058f207b3c6cc)
- Added test cases for extremely slow dequeue scenarios for mClock scheduler testing.
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [8c92eb7](https://github.com/ceph/ceph/commit/8c92eb7dad1736889b9fc37f8969c9169f7fba79)
- Fixed priority parameter error of create_item function in mClock scheduler test.
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [ef851de](https://github.com/ceph/ceph/commit/ef851de888913de0ac6d7f13c7d01dc9fbbaa606)
- Fixed issue with scheduler class not specified in mClock scheduler test.
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [f8f9936](https://github.com/ceph/ceph/commit/f8f993671bcdc283298d31a7eb9e52715bf874b0)
- Fixed use-after-free issues in rbd_mirror tests caused by Namespace objects not being cleaned up.
  ↳ [#61960](https://github.com/ceph/ceph/pull/61960): [a54c691](https://github.com/ceph/ceph/commit/a54c69152af0a499b5164833e9914c74c02a4377)
- Updated error codes and test procedures for root directory operations in libcephfs testing.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [eef245f](https://github.com/ceph/ceph/commit/eef245fcb18c15f27a00421b7fcd0a2213ef356c)
- Added test case to verify that the cap_shared_gen value does not cause unexpected ENOENT errors when creating files in parallel.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [a1e2621](https://github.com/ceph/ceph/commit/a1e2621621a494f927f7474de443c7adc98adf65)
- Added test cases and auxiliary functions to find failure problems after readdir in the libcephfs test, and corrected the error code.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [8197f32](https://github.com/ceph/ceph/commit/8197f322e11472d987dccdbead6bef1739038848)
- Added a test scenario for inode type changes to the snapdiff test case of libcephfs.
  ↳ [#63241](https://github.com/ceph/ceph/pull/63241): [199b8f3](https://github.com/ceph/ceph/commit/199b8f3cf722877f5c6115c98df1372abd851dcd)
- Added BlueFS reserved space test case in store_test.cc.
  ↳ [#62514](https://github.com/ceph/ceph/pull/62514): [a2fc2b5](https://github.com/ceph/ceph/commit/a2fc2b5bf3a9a1f720e3f0e8e3b3c4a16db4de7f)
- Refactored and added test cases for ManyNestedDirs and case-insensitive directories in libcephfs tests.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [b3c9d32](https://github.com/ceph/ceph/commit/b3c9d3272708309854fa34fe0a95ee30833add8c), [bacde03](https://github.com/ceph/ceph/commit/bacde038a179c96a0c77a81831827c80448587db)
- Added flag parameter to d4n_filter unit test case.
  ↳ [#60785](https://github.com/ceph/ceph/pull/60785): [6bc469e](https://github.com/ceph/ceph/commit/6bc469ed76f8cf04051e92354fee9fe4762f0bf0)

### Performance optimization
- On Linux systems, when the file descriptor limit is set very large, the process of closing file descriptors is optimized by directly calling the close_range system call, thus fixing a performance issue that could cause the process to be busy waiting.
  ↳ [#61639](https://github.com/ceph/ceph/pull/61639): [52a658e](https://github.com/ceph/ceph/commit/52a658e8395f487c0011499edfa7ee53d05f44c3)
- In CRC32C calculations, when the CPU supports the PCLMUL instruction set, the more efficient ISA-L crc32_iscsi_01 implementation is preferred to improve performance and reduce cache pollution.
  ↳ [#59389](https://github.com/ceph/ceph/pull/59389): [47961ec](https://github.com/ceph/ceph/commit/47961ecb5dad04db13edcfcef9ca1d63f75649b0)
- Increase the drop buffer size used by the RGW ASIO frontend when handling connections from 1024 bytes to 1024*1024 bytes.
  ↳ [#63710](https://github.com/ceph/ceph/pull/63710): [f7751de](https://github.com/ceph/ceph/commit/f7751de92a158ce9dadd1b9718c07c19b98eebfa)
- Add performance counters for block device asynchronous discard operations to track the running status and number of discard threads.
  ↳ [#62254](https://github.com/ceph/ceph/pull/62254): [d0f30e1](https://github.com/ceph/ceph/commit/d0f30e168abf5467e2a59e2d81f6ad0bbedac157), [d16f268](https://github.com/ceph/ceph/commit/d16f2686464cacbbc3c9c4b8f37150b0994aca77)
- Add condition variable notification in Beacon::shutdown() to eliminate wait delays and speed up the MDS shutdown process.
  ↳ [#60837](https://github.com/ceph/ceph/pull/60837): [18e67b2](https://github.com/ceph/ceph/commit/18e67b22b22f0eb27567cfe3d2a424f96d83632c)
- MDS no longer uses fast dispatch for client metric messages to speed up entry into the up:active state after reconnection.
  ↳ [#62058](https://github.com/ceph/ceph/pull/62058): [f940622](https://github.com/ceph/ceph/commit/f940622df6379951923682cf127f42790028c9ee)
- Cached client permission configuration to improve performance, and fixed related errors.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [c79b57a](https://github.com/ceph/ceph/commit/c79b57abf1ee7e558a9fd111d1b024bb226ec3d4)
- Optimize the performance of the PrimaryLogPG::finish_extent_cmp function, reducing the complexity from O(M*N) to O(M) by using the bufferlist iterator instead of the array access operator.
  ↳ [#61337](https://github.com/ceph/ceph/pull/61337): [86de9e9](https://github.com/ceph/ceph/commit/86de9e903d689b8170409b2dc4fc25bf0dbc71b6)
- Add the function of opening the mirror in read-only mode to the rbd mirror pool status --verbose command to improve command execution efficiency and avoid establishing unnecessary monitoring.
  ↳ [#61170](https://github.com/ceph/ceph/pull/61170): [e640c38](https://github.com/ceph/ceph/commit/e640c3800c29ead528ec20de5ce70c6c0b933790)
- Removed the repair_oinfo_oid() function called during each data scan to improve performance. This function was originally used to repair object ID inconsistencies in object information attributes, but due to its limited functionality and high overhead, it has been removed and related error conditions are handled directly in ScrubBackend::possible_auth_shard.
  ↳ [#61935](https://github.com/ceph/ceph/pull/61935): [aa22f19](https://github.com/ceph/ceph/commit/aa22f19831731185e3c115a2b4e5603e8ef2634f)
- Reduce the default thread pool size for the radosgw-admin command from 512 to 8 to reduce thread starting and stopping overhead.
  ↳ [#62155](https://github.com/ceph/ceph/pull/62155): [d693207](https://github.com/ceph/ceph/commit/d693207987149e485a9d6ed8e200f090adc78776)
- Fixed recovery delay performance counter calculation error for PGRecovery, PGRecoveryContext and PGRecoveryMsg objects in OSD scheduler.
  ↳ [#62802](https://github.com/ceph/ceph/pull/62802): [8981512](https://github.com/ceph/ceph/commit/898151270d22b0db86cad84f05f6c1be2bb5bfc2)
- Fixed the key value issue of Kafka connection pool to ensure that new connections can be created when connection properties are changed.
  ↳ [#62495](https://github.com/ceph/ceph/pull/62495): [82b385a](https://github.com/ceph/ceph/commit/82b385aef86128a0187c3b49e213a20893e8ff85)
- Fixed the problem of repeatedly acquiring the file lock write lock in a single request, avoiding possible deadlock.
  ↳ [#61840](https://github.com/ceph/ceph/pull/61840): [d5d6233](https://github.com/ceph/ceph/commit/d5d623382da886a008f87a570e631b4ba4a6b7f5)
- Optimized the passing of the alternate_name parameter in the client's open and openat functions to avoid unnecessary copying by using std::move.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [18f7fb3](https://github.com/ceph/ceph/commit/18f7fb31a42f8b646900482a442c222b7b1b5e0e)
- Added delay logging to BlueStore's omap_iterate() function to track operation time.
  ↳ [#61363](https://github.com/ceph/ceph/pull/61363): [b4b8508](https://github.com/ceph/ceph/commit/b4b85088a56dc6791ca15779f600fdcf862ba9c9)
- In config_cacher.h, replaced changed.count() with changed.contains() to use more modern C++ collection member functions.
  ↳ [#61398](https://github.com/ceph/ceph/pull/61398): [21691f2](https://github.com/ceph/ceph/commit/21691f2fa1ffc97bf22dc8c8e75eb5722f2bb233)

### Security related
- Replace variable-length arrays in the CrushWrapper::do_rule method with std::vector to eliminate Clang compilation warnings and avoid potential stack overflow risks.
  ↳ [#61956](https://github.com/ceph/ceph/pull/61956): [4f60e8d](https://github.com/ceph/ceph/commit/4f60e8d9ff039fbc9fda3cea88f81f1796e90b1f)
- When creating S3 notification topics, added checks for sending usernames/passwords over unencrypted connections, and optimized related parameter processing logic.
  ↳ [#60952](https://github.com/ceph/ceph/pull/60952): [563db18](https://github.com/ceph/ceph/commit/563db184d345f9e307b3b71f3eaf09e2639b7515)
- Fixed the security vulnerability of unprivileged users elevating to root privileges by modifying directory permissions, and added corresponding test cases.
  ↳ [#63458](https://github.com/ceph/ceph/pull/63458): [f9220cc](https://github.com/ceph/ceph/commit/f9220cc27bdf3b08cd1c1ee536cc9cd38a204b38)
- Fixed the issue of using heap memory after it is released in StackStringBuf::overflow() to ensure that the data pointer and insertion position of the stream buffer are updated after vector expansion.
  ↳ [#57361](https://github.com/ceph/ceph/pull/57361): [ed5ab75](https://github.com/ceph/ceph/commit/ed5ab7554fb3ba9b50f3af35785912091fe7eac2)
- In the log output, the full endpoint address is no longer logged, but the hostname and username are parsed and logged separately to avoid leaking possible proxy passwords.
  ↳ [#60784](https://github.com/ceph/ceph/pull/60784): [dede04b](https://github.com/ceph/ceph/commit/dede04b2870a7774615d7c71e8fe7541a73011ad)
- Removed the logic of printing the POST request body in the Kafka message callback to avoid leaking password information associated with the topic.
  ↳ [#60952](https://github.com/ceph/ceph/pull/60952): [b38f149](https://github.com/ceph/ceph/commit/b38f149e688b10b175f4128accd1e8df97664b74)
- Added sensitive information filtering logic to the RGWHTTPArgs::parse method. When the parameter name contains password, the corresponding value will be replaced with **** in the log output to prevent the password from being recorded in plain text.
  ↳ [#60784](https://github.com/ceph/ceph/pull/60784): [0289c4b](https://github.com/ceph/ceph/commit/0289c4bd7fd4de7380bfd87659ccf9de725145d3)
- Fixed the buffer out-of-bounds problem of the dump_format_va method in Formatter. When the output content exceeds the pre-allocated buffer size, the buffer is dynamically adjusted to avoid truncation. At the same time, test cases for large string output were added for JSON, XML and Table formatters.
  ↳ [#61104](https://github.com/ceph/ceph/pull/61104): [2cd364d](https://github.com/ceph/ceph/commit/2cd364d11bcd0454c394459389b9e5a07a074827)
- Fixed the out-of-bounds problem in HTMLFormatter caused by too small buffer, now use boost::small_vector to dynamically adjust the buffer size to accommodate long content, and added related unit tests.
  ↳ [#61104](https://github.com/ceph/ceph/pull/61104): [70e6e82](https://github.com/ceph/ceph/commit/70e6e82dbb806d0aee71faeb3f15402970c9e493)
- Fixed a security vulnerability where unsupported JWT algorithms were not rejected during AssumeRoleWithWebIdentity authentication with JWT obtained through an external identity provider.
  ↳ [#62137](https://github.com/ceph/ceph/pull/62137): [e502e35](https://github.com/ceph/ceph/commit/e502e35f366af08bc71bbf6cba99c630b70d9df8)
- When creating a user, the verification of the user ID format is added, and user IDs with the same format as the account ID are refused to be used to avoid ambiguity.
  ↳ [#60980](https://github.com/ceph/ceph/pull/60980): [c16dc7e](https://github.com/ceph/ceph/commit/c16dc7ed8c2224ea72ede3bff10bdf2ca7810828)
- Fixed an issue where JWK keys of type sig were not correctly selected during JWT token signature verification in the STS service.
  ↳ [#63052](https://github.com/ceph/ceph/pull/63052): [2d21287](https://github.com/ceph/ceph/commit/2d212878ddd76fb641fe9be6c3b4c9861beadb78)
- Added checking for nbd_get_size() call errors in the get_size method of NBDStream to improve robustness.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [8a4d259](https://github.com/ceph/ceph/commit/8a4d25979e56c4b4846d5437ab54f0f24e43496a)
- Upgrade and unlock some Python dependency versions to fix security vulnerabilities and update documentation build dependencies.
  ↳ [#61931](https://github.com/ceph/ceph/pull/61931): [7678d0f](https://github.com/ceph/ceph/commit/7678d0fc07c17153251e20bea5f8f048e14225ae)

### Documentation
- When dumping a log segment, its end offset is now also output.
  ↳ [#60688](https://github.com/ceph/ceph/pull/60688): [2e187d0](https://github.com/ceph/ceph/commit/2e187d09857768dc86d828d406c7771b13e407c5)
- Improved the format, spelling and consistency of radosgw documentation, including using modern prompt blocks, fixing JSON examples, unifying title case, fixing hyperlink and list formats, unifying inline code format, etc.
  ↳ [#62856](https://github.com/ceph/ceph/pull/62856): [227c7a4](https://github.com/ceph/ceph/commit/227c7a45f08f8236e825cec3cd70cce27a8df859) | [#62909](https://github.com/ceph/ceph/pull/62909): [b72f917](https://github.com/ceph/ceph/commit/b72f917fce1e5d8b612da4caa3f3d57831dbd93c)
- Improved the format and wording of the RGW module documentation, uniformly used double backticks, corrected capitalization, and deleted irrelevant paragraphs.
  ↳ [#63625](https://github.com/ceph/ceph/pull/63625): [0e5c5ba](https://github.com/ceph/ceph/commit/0e5c5ba3b3389c66da52ff139760c1d7ed39d56f)
- Fixed syntax errors in placement-groups.rst documentation, and improved descriptions of auto-scaling, PG number selection, target size and ratio, etc.
  ↳ [#63649](https://github.com/ceph/ceph/pull/63649): [f8f3e3d](https://github.com/ceph/ceph/commit/f8f3e3d53dc601c3eb5f6609c5a9743bc62cf494) | [#63646](https://github.com/ceph/ceph/pull/63646): [27feec9](https://github.com/ceph/ceph/commit/27feec963b0c70a851231b9ea57f6d636b5f2616) | [#63683](https://github.com/ceph/ceph/pull/63683): [41840b9](https://github.com/ceph/ceph/commit/41840b9e68d6567000d3556cacd68cf303749293)
- Unified the imperative tone of key rotation instructions in user management documents.
  ↳ [#63828](https://github.com/ceph/ceph/pull/63828): [20e6304](https://github.com/ceph/ceph/commit/20e630460a0368d8e08120b0e7cf523248a06040)
- In the pools.rst documentation, added a link to the relevant how-to guide for instructions on updating user permissions after renaming a pool.
  ↳ [#63861](https://github.com/ceph/ceph/pull/63861): [254ae63](https://github.com/ceph/ceph/commit/254ae636fe8b06f9af6e2131016f5a166d29a832)
- Updated CephFS quota documentation to note that quotas can now be removed or disabled by removing the extended attribute or setting its value to 0.
  ↳ [#60752](https://github.com/ceph/ceph/pull/60752): [8c9b075](https://github.com/ceph/ceph/commit/8c9b075404a9443cbc7f24f338cb3ea69b12b67b)
- Updated S3 notification documentation, adding descriptions of user-name and password topic attributes for Kafka SASL authentication.
  ↳ [#60952](https://github.com/ceph/ceph/pull/60952): [2a607ff](https://github.com/ceph/ceph/commit/2a607ffe894f5a2586529bf8fa12a33ef992278f)
- Added documentation for the --daemon-output-file option for the ceph command, and added documentation on temporary directory configuration.
  ↳ [#57675](https://github.com/ceph/ceph/pull/57675): [befc202](https://github.com/ceph/ceph/commit/befc202415ccd23838a0117952f7b57fa929f816)
- Added documentation for the ceph auth rotate command describing how to rotate the key for a user credential.
  ↳ [#58235](https://github.com/ceph/ceph/pull/58235): [d010bc6](https://github.com/ceph/ceph/commit/d010bc60580ba56b4ff7c44b2c01a6e01af5ece9)
- Added NONEXISTENT_MON_CRUSH_LOC_STRETCH_MODE warning entry to the health check documentation, stating that when stretch mode is enabled, the monitor's CRUSH position must belong to a split bucket.
  ↳ [#62039](https://github.com/ceph/ceph/pull/62039): [5056866](https://github.com/ceph/ceph/commit/50568668ede86e48f16325605b735edecd2b0b8d)
- Clarified the description of the image_id parameter in the RBD live migration documentation to clarify that it needs to be specified when the image is in the recycle bin.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [34c1310](https://github.com/ceph/ceph/commit/34c1310839fc071b9e6d0569d507b61d7dffe230)
- Added instructions on how to exit stretch mode in the stretch-mode.rst document, including steps and parameter descriptions for using the ceph mon disable_stretch_mode command.
  ↳ [#60629](https://github.com/ceph/ceph/pull/60629): [bb84237](https://github.com/ceph/ceph/commit/bb842372b06209cc8ac61fcb19ef6abe71ba623e)
- Improved the usage help information of ceph-exporter, optimized the wording of option descriptions, and added descriptions of HTTPS-related certificate options.
  ↳ [#61331](https://github.com/ceph/ceph/pull/61331): [99f4ecc](https://github.com/ceph/ceph/commit/99f4eccb6bef444f86e6d6cbf579dc3ba975af98)
- Updated documentation to correct mount.ceph's default option from wsync to nowsync, and to state that this default is effective as of kernel version 5.16.
  ↳ [#60199](https://github.com/ceph/ceph/pull/60199): [ed529c1](https://github.com/ceph/ceph/commit/ed529c13934309910ed2e18113358d1c258aedef)
- Added configuration instructions for OAuth2 single sign-on (SSO) to the dashboard documentation and updated the title and references of the SAML2 SSO section.
  ↳ [#64033](https://github.com/ceph/ceph/pull/64033): [2af5800](https://github.com/ceph/ceph/commit/2af5800f5a20ecc1fd592e024a8d03806ab67f89)
- Update the documentation to remove the reference to the mds_log_major_segment_event_ratio configuration item and replace it with the description of mds_log_minor_segments_per_major_segment.
  ↳ [#60838](https://github.com/ceph/ceph/pull/60838): [74de11c](https://github.com/ceph/ceph/commit/74de11c7812e01202c24d4a3994892eb7343caca)
- Added description of Purge Queue and its performance counters to CephFS documentation.
  ↳ [#61193](https://github.com/ceph/ceph/pull/61193): [89b1f99](https://github.com/ceph/ceph/commit/89b1f9901c62d136d13d8d7a434b8b7dd306c971)
- Added descriptions of I/O operation limits during network partitions and OSD failure threshold behavior to the stretch pool configuration documentation.
  ↳ [#61629](https://github.com/ceph/ceph/pull/61629): [489b9a7](https://github.com/ceph/ceph/commit/489b9a7c33039d47343f19e3d9e9e0e488d4c6f5) | [#61006](https://github.com/ceph/ceph/pull/61006): [4cb07f5](https://github.com/ceph/ceph/commit/4cb07f5675b59fde695a26c3e945a6708074a585)
- Edited the CephFS kernel driver mounting document, corrected the grammar and wording, and optimized the English expression.
  ↳ [#61056](https://github.com/ceph/ceph/pull/61056): [971321a](https://github.com/ceph/ceph/commit/971321ad893495a0efadb8d46cfba21c0c40318e) | [#61058](https://github.com/ceph/ceph/pull/61058): [2a7ea38](https://github.com/ceph/ceph/commit/2a7ea38560dd1f119caab41b6485f76279ceda1e)
- Fixed the description of the osd_max_scrubs configuration item and removed the error description about this setting being ignored under the mClock scheduler.
  ↳ [#62377](https://github.com/ceph/ceph/pull/62377): [96006e9](https://github.com/ceph/ceph/commit/96006e96c45080c63be06c15c5566a98bc56610f)
- Added documentation for CephFS character mapping configuration, introducing the normalization and case folding functions of directory entry names.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [2ff6a6b](https://github.com/ceph/ceph/commit/2ff6a6bc93eb59032297bb1c312693eec43192b0)
- Corrected the description of the if-none-match request header in the S3 object operation documentation, from "get only if the object ETag matches" to "get only if the object ETag does not match".
  ↳ [#61308](https://github.com/ceph/ceph/pull/61308): [8a07c59](https://github.com/ceph/ceph/commit/8a07c5936d7fe1d27aa8964f386a674042bff61e)
- Added a new chapter about snapshots to the CephFS concepts documentation and updated the document index to include the chapter.
  ↳ [#61246](https://github.com/ceph/ceph/pull/61246): [338c340](https://github.com/ceph/ceph/commit/338c340b944178be788674b3d4a7b985537f96ad)
- Improved stretch-mode documentation, rewritten and expanded the content about network partition handling, monitor election strategy, and exiting stretch mode.
  ↳ [#61629](https://github.com/ceph/ceph/pull/61629): [8928fc9](https://github.com/ceph/ceph/commit/8928fc97bff5d779b0dd20082369dd4bf2ed1c15)
- Fixed incorrect advice on lifecycle settings in the RGW configuration reference document, correcting "Reduce parallel threads" to "Increase parallel threads" for more aggressive lifecycle handling.
  ↳ [#61437](https://github.com/ceph/ceph/pull/61437): [60a2c8a](https://github.com/ceph/ceph/commit/60a2c8ad4747d7dfbc944e9771831cd4188502bd)
- Added to the documentation that when migrating users to accounts, the UserName must comply with the format requirements of the IAM User API to resolve the "UserName contains invalid characters" error that may occur during migration.
  ↳ [#61333](https://github.com/ceph/ceph/pull/61333): [7389e74](https://github.com/ceph/ceph/commit/7389e74145541eb6834471aa6c3c8e48a77331aa)
- Improved the integration test Teuthology workflow documentation, added a new workflow overview chapter and diagram, and added detailed subsections on how to push to the ceph-ci repository.
  ↳ [#61342](https://github.com/ceph/ceph/pull/61342): [67fa96f](https://github.com/ceph/ceph/commit/67fa96fa97fe6e8dfa4fea538c8217b7ce357200)
- Updated documentation on RADOS gateway management capabilities, adding accounts option.
  ↳ [#61782](https://github.com/ceph/ceph/pull/61782): [36968cf](https://github.com/ceph/ceph/commit/36968cf47da91e9838d8682410dec0cb0274560d)
- Edited and optimized several parts of the CephFS Disaster Recovery Expert documentation, including rewriting sentences, organizing step formats, and optimizing text presentation.
  ↳ [#61423](https://github.com/ceph/ceph/pull/61423): [30344c5](https://github.com/ceph/ceph/commit/30344c5cacd63d9c36619dfd85a73f75d04c72da) | [#61443](https://github.com/ceph/ceph/pull/61443): [f6e42cb](https://github.com/ceph/ceph/commit/f6e42cb129ae0612f4ca94a246c951414bea5d3c) | [#61453](https://github.com/ceph/ceph/pull/61453): [42239f8](https://github.com/ceph/ceph/commit/42239f8d556834d281b1c10dade42b91201deb2b) | [#61499](https://github.com/ceph/ceph/pull/61499): [5f16310](https://github.com/ceph/ceph/commit/5f163104a1a0814fa7ba370ec6f445cdca85e021) | [#61521](https://github.com/ceph/ceph/pull/61521): [0881344](https://github.com/ceph/ceph/commit/0881344b830f6b356d56d5fb1e491b194571dab9)
- Corrected description of OSD capability syntax in RADOS user management documentation to clarify that pool and namespace restrictions are independent of each other, and added multiple alternative forms of optional matching specifications.
  ↳ [#61523](https://github.com/ceph/ceph/pull/61523): [4fa4fd2](https://github.com/ceph/ceph/commit/4fa4fd2f91404649ddb42beb9785770f0c213e3a)
- Updated the example URL in the RBD live migration documentation to change the HTTP link to an HTTPS link to avoid confusion when using the HTTP stream type.
  ↳ [#61605](https://github.com/ceph/ceph/pull/61605): [5bf2f48](https://github.com/ceph/ceph/commit/5bf2f48ec70f38d6648fd9dd65e8077e6b063211)
- Removed a description from the architecture document that was more marketing than reference.
  ↳ [#61614](https://github.com/ceph/ceph/pull/61614): [ee846a0](https://github.com/ceph/ceph/commit/ee846a07b43ef4a5ea49e699e347fe816534a8f3)
- Updated the Monitoring Status document title and description during OSD removal to more clearly refer to the operational process being discussed.
  ↳ [#61664](https://github.com/ceph/ceph/pull/61664): [fe21b2a](https://github.com/ceph/ceph/commit/fe21b2a89774ab84b991f4e606eb3e7e196715aa)
- Improved documentation on setting pg_num and pgp_num, clarifying that since Nautilus versions pgp_num is automatically adjusted and administrators usually do not need to set it manually.
  ↳ [#62056](https://github.com/ceph/ceph/pull/62056): [12caa66](https://github.com/ceph/ceph/commit/12caa66dba24ad9004204a9df6241189c00c9136)
- Improved the description of storage pools in the RADOS operation documentation, including updated descriptions, corrected examples, supplemented configuration details and clarified related concepts.
  ↳ [#61728](https://github.com/ceph/ceph/pull/61728): [e493fee](https://github.com/ceph/ceph/commit/e493fee63144e6d0e2d9cb2ce9b1c9db42815796)
- Update the release process documentation to clearly state that the release build will not automatically build the container image and needs to be done manually after the package is signed and uploaded to download.ceph.com.
  ↳ [#61817](https://github.com/ceph/ceph/pull/61817): [3eeb21d](https://github.com/ceph/ceph/commit/3eeb21de66e8a83aa1fda4dfade983d62da3eda0)
- Updated the document to clarify that there is no third OSD in the OSD copy process, and corrected the relevant description and diagram.
  ↳ [#61730](https://github.com/ceph/ceph/pull/61730): [695eb99](https://github.com/ceph/ceph/commit/695eb9937af1a941c30834b841ef026f03e91aeb)
- Improved the "Activating an Existing OSD" section in the cephadm documentation and added detailed steps for reactivating an OSD after reinstalling the host operating system.
  ↳ [#61725](https://github.com/ceph/ceph/pull/61725): [58289ee](https://github.com/ceph/ceph/commit/58289eec7972d87ab10afa74f5e90ebb484990cc)
- Added documentation for the charmap functionality of the CephFS volume interface, including how to configure charmap for subvolume groups and subvolumes.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [887e8ed](https://github.com/ceph/ceph/commit/887e8ed078797c521643e3ee523ddbc5493f1c75)
- Added new documentation about container build tools and added a link to the documentation in the project README.
  ↳ [#62161](https://github.com/ceph/ceph/pull/62161): [779bc8b](https://github.com/ceph/ceph/commit/779bc8bcab8be746a895b77fada788f2cc053ff2)
- Added description of the show-label-at subcommand to the documentation for the ceph-bluestore-tool command, and updated the description of the main device label location.
  ↳ [#62202](https://github.com/ceph/ceph/pull/62202): [d015f81](https://github.com/ceph/ceph/commit/d015f81b978fe25219f49195db776904c15f6d48)
- Added instructions for upgrading the root CA certificate to the documentation, and improved the related syntax and format.
  ↳ [#61884](https://github.com/ceph/ceph/pull/61884): [3ab36c6](https://github.com/ceph/ceph/commit/3ab36c65f1f595a4caa1d3ab9c55678843bf15c5)
- In the Ceph Getting Started documentation, added RGW (Ceph Object Gateway) to the component list and architecture diagram, and updated the description of Crimson in the glossary.
  ↳ [#61926](https://github.com/ceph/ceph/pull/61926): [0b9b0e8](https://github.com/ceph/ceph/commit/0b9b0e84a7a2fea38e829c04bfa1faafc68febc0)
- Improved the presentation and example descriptions of OSD service documents, including correcting wording, updating example values, and clarifying the use of configuration parameters.
  ↳ [#61952](https://github.com/ceph/ceph/pull/61952): [9239439](https://github.com/ceph/ceph/commit/9239439ca750780c6e98317fd80b3d893abfc568)
- Updated documentation to clarify terminology for S3 access methods, changed "vhost-style" to "path-style" and "virtual-hosted-style", and corrected the description of AWS deprecated methods.
  ↳ [#61986](https://github.com/ceph/ceph/pull/61986): [626dc87](https://github.com/ceph/ceph/commit/626dc872c6d24ae6ea26caa22f93ae75700fb209)
- Fixed an issue with the OSDs panel in the host-details Grafana dashboard so that when filtering for a specific host, it only displays the number of OSDs for that host, rather than the sum of all hosts.
  ↳ [#62625](https://github.com/ceph/ceph/pull/62625): [bb5d0b7](https://github.com/ceph/ceph/commit/bb5d0b7d2bf741ed1b4434eeba7be37bf47d7553)
- Clarified that stretch mode does not support the restriction of device categories specified in CRUSH rules, and updated related documentation.
  ↳ [#62077](https://github.com/ceph/ceph/pull/62077): [c19f36c](https://github.com/ceph/ceph/commit/c19f36cb3cf90358b9b0286285bea48a9d456dc5)
- Updated S3 bucket policy documentation, adding description of SSE-C IAM condition keys.
  ↳ [#62297](https://github.com/ceph/ceph/pull/62297): [303014d](https://github.com/ceph/ceph/commit/303014dc4b457c7294195c0ffe859bb10af5d8c3)
- The index.rst file of the monitoring document has been improved, and the text expression, format and example description have been optimized.
  ↳ [#62265](https://github.com/ceph/ceph/pull/62265): [5f57b8e](https://github.com/ceph/ceph/commit/5f57b8eb30d1051d49a55510fcd7dc7f39af863e)
- In the CephFS documentation, added a link to the chapter on pausing asynchronous threads to the section on disabling volume plugins, and added detailed instructions on pausing asynchronous cleanup and clone threads.
  ↳ [#62874](https://github.com/ceph/ceph/pull/62874): [c08339c](https://github.com/ceph/ceph/commit/c08339c9815b80d014cd2b28ae0798b9d77fd54e)
- Improved the example description in the CRUSH mapping editing documentation to make it clearer and easier to understand.
  ↳ [#62317](https://github.com/ceph/ceph/pull/62317): [01df74e](https://github.com/ceph/ceph/commit/01df74e248f4e124ead1f31b4d60dcc5084a80c0)
- Improved the wording and formatting of the layout.rst file in the radosgw documentation to make the description clearer and more accurate.
  ↳ [#62449](https://github.com/ceph/ceph/pull/62449): [1e7b586](https://github.com/ceph/ceph/commit/1e7b5863d9474d7715435d932b69dcd0880757df)
- Added a description to the cephadm upgrade documentation about the recommendation to disable the PG autoscaler during the upgrade, and corrected some document formats and wordings.
  ↳ [#62379](https://github.com/ceph/ceph/pull/62379): [8c19647](https://github.com/ceph/ceph/commit/8c1964707c985964e28ff791b4bad6291d6b29f3)
- Updated the instructions for subscribing to the Ceph development mailing list in the Developer Guide, replacing the outdated subscription method with a link to the corresponding web form.
  ↳ [#62375](https://github.com/ceph/ceph/pull/62375): [01f5775](https://github.com/ceph/ceph/commit/01f5775d0a5b8d2ee26d4515d20f69ceebee0056)
- Fixed the description of the many-to-many relationship between topics and notifications in the radosgw notification document to make it clearer and more accurate.
  ↳ [#62404](https://github.com/ceph/ceph/pull/62404): [e217009](https://github.com/ceph/ceph/commit/e2170098b3a4205ad5872682f1058f4e9e0f56df)
- Added documentation for ceph osd rm-pg-upmap-primary and rm-pg-upmap-primary-all commands, and documented this feature in the v19.2.2 release notes.
  ↳ [#62467](https://github.com/ceph/ceph/pull/62467): [06fd4bc](https://github.com/ceph/ceph/commit/06fd4bc9be650ad1873665097e4a137063307f77)
- Corrected indentation and wording in OSD service documentation, optimized device scanning, --wide option and description of OSD specification examples.
  ↳ [#62427](https://github.com/ceph/ceph/pull/62427): [69d8e22](https://github.com/ceph/ceph/commit/69d8e22fd59db4c8a299a144a605dd055ddfac6e)
- Added description and usage examples of --zap option to OSD removal documentation.
  ↳ [#62443](https://github.com/ceph/ceph/pull/62443): [b01e748](https://github.com/ceph/ceph/commit/b01e7483df98dac6aeb6f7a7e7458a0b9c5b788b)
- Added setting instructions to the description of the configuration item mon_warn_pg_not_deep_scrubbed_ratio to guide users to set this value on the Manager through the ceph config set mgr command.
  ↳ [#62502](https://github.com/ceph/ceph/pull/62502): [6767c49](https://github.com/ceph/ceph/commit/6767c495f949d95d1045f0a1c44797cc31c3e01e)
- Improved erasure coding documentation, fixed description errors and expanded the cost factor table, and updated the description of cache tiering deprecation.
  ↳ [#62573](https://github.com/ceph/ceph/pull/62573): [163e139](https://github.com/ceph/ceph/commit/163e139a2f4f05267501d4f074c49675705e4875)
- Improved documentation for the Prometheus module, polishing and clarifying descriptions, configuration instructions and examples.
  ↳ [#62930](https://github.com/ceph/ceph/pull/62930): [f5dd9e7](https://github.com/ceph/ceph/commit/f5dd9e7dfe1115e2f66775a46fdd02597ad9f674)
- Improved stretch-mode.rst documentation, optimizing wording, terminology consistency and description accuracy.
  ↳ [#63815](https://github.com/ceph/ceph/pull/63815): [22c17f4](https://github.com/ceph/ceph/commit/22c17f4e8f9be39306e9273ada942a07478dc7b2)
- Added a note about restarting the OSD service in the cephadm documentation, reminding users that directly restarting the OSD service may result in data unavailability or loss due to failure to consider the CRUSH fault domain.
  ↳ [#62796](https://github.com/ceph/ceph/pull/62796): [91c9762](https://github.com/ceph/ceph/commit/91c97628a51ed2132111f763ffad7cc67af07c37)
- Updated mClock configuration documentation to detail how to set or override the maximum IOPS capacity configuration for an OSD, including steps for using global values and overriding individual OSD values.
  ↳ [#63071](https://github.com/ceph/ceph/pull/63071): [d2f8d79](https://github.com/ceph/ceph/commit/d2f8d793a188153c7c5da2b92fedeba15b148ef3)
- Updated the documentation of cephfs-journal-tool, corrected the command syntax format, added the description of the --force option, the pool_id attribute of header set, the description of the event recover_dentries operation, and added the description of the --rank and --journal options.
  ↳ [#63108](https://github.com/ceph/ceph/pull/63108): [08e4318](https://github.com/ceph/ceph/commit/08e4318e5c430237681f3410104f0ffb3692d649)
- Updated RGW administrator capabilities documentation to link the "Admin API" description to the "Admin Ops API" reference documentation.
  ↳ [#62881](https://github.com/ceph/ceph/pull/62881): [f29bc2e](https://github.com/ceph/ceph/commit/f29bc2e48d721e706ec9bf403f83dd54029f5738)
- Added a new "Administrator and System User" chapter to the RGW document to explain its global permissions, usage scenarios and security precautions, and added cross-references for multi-site configuration.
  ↳ [#62881](https://github.com/ceph/ceph/pull/62881): [5fb3a06](https://github.com/ceph/ceph/commit/5fb3a06a742118df922f4f79ae72afa2bcd4f432)
- Improved the format and content of the radosgw layout documentation, including updating terminology, adding metadata type list examples, and optimizing the clarity of command descriptions.
  ↳ [#62999](https://github.com/ceph/ceph/pull/62999): [6993d30](https://github.com/ceph/ceph/commit/6993d30e5d801b3f4191df9d59e501303f83c380)
- Edited the documentation file doc/mgr/dashboard.rst, changed a large number of command prompts from bash $ to bash #, and added new command instructions about RGW hostname configuration.
  ↳ [#63315](https://github.com/ceph/ceph/pull/63315): [04f4172](https://github.com/ceph/ceph/commit/04f4172b947d1b7cb0cd54dead572e0a5a22fbc4)
- Fixed a rendering issue with unordered lists in the health-checks.rst document and added missing periods for list items.
  ↳ [#63958](https://github.com/ceph/ceph/pull/63958): [36c4939](https://github.com/ceph/ceph/commit/36c4939b4e9aea513898f46606e9be0c4a30393d)
- Fixed warnings in Sphinx documentation builds due to missing blank lines after explicit tags, and fixed indentation formatting errors in list items.
  ↳ [#63337](https://github.com/ceph/ceph/pull/63337): [eb74789](https://github.com/ceph/ceph/commit/eb7478901be6f476d767e150da2695fa18745efe)
- Updated RGW STS configuration documentation to use the confval directive to render configuration options and improved the description of rgw_sts_key, including key format requirements, generation commands and multi-gateway/multi-site sharing instructions.
  ↳ [#63441](https://github.com/ceph/ceph/pull/63441): [175ebc0](https://github.com/ceph/ceph/commit/175ebc06a7c509a517129df2172231af3b4d7db4)
- Format correction and content clarification were made to the CephFS mirror document, including uniformly using double backticks to mark commands and file names, fixing invalid section references, adjusting capitalization and punctuation, and unifying tool names to cephfs-mirror.
  ↳ [#63467](https://github.com/ceph/ceph/pull/63467): [9b1ff40](https://github.com/ceph/ceph/commit/9b1ff40d08489d4f4c697d909f0a674ecde5f0c6)
- Edited the documentation for the dashboard debugging plug-in, corrected the command prompt and output format.
  ↳ [#63393](https://github.com/ceph/ceph/pull/63393): [aa03230](https://github.com/ceph/ceph/commit/aa03230f77d067f58c843b0e6063b3503200e6f5)
- Edited the documentation file doc/mgr/dashboard_plugins/feature_toggles.inc.rst, adjusted the prompt and output format of the example command.
  ↳ [#63396](https://github.com/ceph/ceph/pull/63396): [5df3098](https://github.com/ceph/ceph/commit/5df30988da27209412c9444ded2472b25ac5f9f8)
- Edited the documentation of the MDS autoscaler module, improved the English description and corrected the format.
  ↳ [#63492](https://github.com/ceph/ceph/pull/63492): [e284c41](https://github.com/ceph/ceph/commit/e284c41923c82274c50f18c67552c7dabb82c51a)
- The document cloud-transition.rst has been formatted, including correcting list item indentation, adding missing periods, adjusting inline code format, and unifying the presentation of S3 API operation names.
  ↳ [#63448](https://github.com/ceph/ceph/pull/63448): [be0ae07](https://github.com/ceph/ceph/commit/be0ae077bc8a7f8a17c681b84532e53bd4b2df1a)
- Edited the documentation file doc/mgr/modules.rst, improving the English expression and grammar.
  ↳ [#63577](https://github.com/ceph/ceph/pull/63577): [3192cf0](https://github.com/ceph/ceph/commit/3192cf0cffee1fa9373b3739ed28b36b1825cac0)
- Improved the English expression and format of the NFS manager document (nfs.rst), including correcting grammatical errors, changing the code block mark from code:: bash to prompt:: bash #, and adjusting the line breaks and punctuation of some paragraphs.
  ↳ [#63580](https://github.com/ceph/ceph/pull/63580): [59fa3b8](https://github.com/ceph/ceph/commit/59fa3b89dae8e5b0bd5a8a756612fa3870d4df8f)
- Fixed a malformed mount command in the CephFS documentation, merging command lines that were originally separated by line breaks into one line to avoid option parameters being mistaken for independent commands.
  ↳ [#63501](https://github.com/ceph/ceph/pull/63501): [949595c](https://github.com/ceph/ceph/commit/949595c954b70fa1e393035b7dac1990dae929dd)
- Fixed formatting errors in the cache layering documentation and removed statements that might mislead users into deploying cache layers before the Reef version. Added clear community advice against deploying new cache layers.
  ↳ [#63504](https://github.com/ceph/ceph/pull/63504): [64783ce](https://github.com/ceph/ceph/commit/64783ce51305a101063f68cd8808445e35c431e4) | [#63830](https://github.com/ceph/ceph/pull/63830): [eabd78a](https://github.com/ceph/ceph/commit/eabd78a1bb0a5f97fed2fccffe672d05a5ae7771)
- Edited the orchestrator.rst document, changed the command prompt from bash $ to bash #, and adjusted the indentation format of some commands.
  ↳ [#63583](https://github.com/ceph/ceph/pull/63583): [0a4556c](https://github.com/ceph/ceph/commit/0a4556cd6eb24cbbc47056bfce4878eb761e2f6d)
- Added suggestions on balancer settings to the balancer.rst document, including instructions for adjusting parameters such as the target_max_misplaced_ratio threshold.
  ↳ [#63535](https://github.com/ceph/ceph/pull/63535): [2fbf990](https://github.com/ceph/ceph/commit/2fbf9901f5b6e14cbc317c7fcc1516452a46b8ff)
- Updated dashboard plugin feature switch documentation, added nvmeof to the list of enabled features, and fixed extra spaces and spelling errors in the text.
  ↳ [#63704](https://github.com/ceph/ceph/pull/63704): [a7fdd96](https://github.com/ceph/ceph/commit/a7fdd9687345cc97555cd4f6689da5d7bdaf0e9a)
- Rewrote the first description sentence of the iostat module documentation.
  ↳ [#63680](https://github.com/ceph/ceph/pull/63680): [e6813da](https://github.com/ceph/ceph/commit/e6813da92b8519013ab3a06c838aa3b1328fed05)
- Edited the "Updating NFS Cluster" section of the documentation doc/mgr/nfs.rst, adjusting wording and example commands based on feedback.
  ↳ [#63663](https://github.com/ceph/ceph/pull/63663): [5720970](https://github.com/ceph/ceph/commit/5720970acf3d91ffac5af5257b219759183413d4)
- The fourth part of the CephFS image development document has been edited, grammatical errors have been corrected and command prompt formatting has been added to improve the readability and accuracy of the document.
  ↳ [#63660](https://github.com/ceph/ceph/pull/63660): [9516793](https://github.com/ceph/ceph/commit/951679396b67f7a91814079f8d1ee7c80ba27b88)
- Edited the documentation file doc/mgr/progress.rst, revised the description of the ceph -s command as suggested, and adjusted the description of the optionality of the PG recovery event.
  ↳ [#63657](https://github.com/ceph/ceph/pull/63657): [2fc0569](https://github.com/ceph/ceph/commit/2fc0569705cb0b3362f5499e80ff9393cc900ac4)
- Edited the "Building the source code for the first time" section in the document doc/start/documenting-ceph.rst, removed outdated references to RHEL7, improved sentence expressions and optimized RST format.
  ↳ [#63707](https://github.com/ceph/ceph/pull/63707): [c006de8](https://github.com/ceph/ceph/commit/c006de8eb016ca75cec503810e844d99e0da6f54)
- Improved the English description of the doc/mgr/cli_api.rst document and corrected the module name and description.
  ↳ [#63743](https://github.com/ceph/ceph/pull/63743): [a3d651f](https://github.com/ceph/ceph/commit/a3d651f4e2e940af3d065aaeff18ee19d39489a4)
- Improved the English presentation and formatting of the telemetry module documentation to make it clearer and easier to read, and updated the instructions for sending telemetry data through a proxy.
  ↳ [#63768](https://github.com/ceph/ceph/pull/63768): [b3e3549](https://github.com/ceph/ceph/commit/b3e3549ccb143d559f3e56696292b17ea677b2de) | [#63771](https://github.com/ceph/ceph/pull/63771): [158a65f](https://github.com/ceph/ceph/commit/158a65f39d78cec624cdcbc52b12758332a9c901) | [#63774](https://github.com/ceph/ceph/pull/63774): [9ff680d](https://github.com/ceph/ceph/commit/9ff680dd4591b949095547eff77f9987ab24d4b6) | [#63777](https://github.com/ceph/ceph/pull/63777): [fbfcc9a](https://github.com/ceph/ceph/commit/fbfcc9a97e05541a34aea25e44d18b234425945f) | [#63864](https://github.com/ceph/ceph/pull/63864): [1eaba67](https://github.com/ceph/ceph/commit/1eaba675cf923f3d6cdf8862981ac37e26bcdd55) | [#63867](https://github.com/ceph/ceph/pull/63867): [b0cc861](https://github.com/ceph/ceph/commit/b0cc86131a4f7a0e2f006234838bc7121a94a092)
- Updated the stretch-mode.rst document, fixing typos and improving clarity and accuracy in many places.
  ↳ [#63849](https://github.com/ceph/ceph/pull/63849): [aee2ef9](https://github.com/ceph/ceph/commit/aee2ef94d34315cf9422843ad3a72c43a33db8c4)
- Improved the description text of the osd_deep_scrub_interval_cv variable in the osd.yaml.in configuration file to make its English description clearer.
  ↳ [#63955](https://github.com/ceph/ceph/pull/63955): [440d0e2](https://github.com/ceph/ceph/commit/440d0e22e143d4d6ed8e68d5a2147aaa7a8e6639)
- Added troubleshooting instructions to the RBD mirror documentation, stating that when encountering a failed to import peer bootstrap token error, you should ensure that the pool name is the same at both sites, and providing guidance on renaming the pool.
  ↳ [#63846](https://github.com/ceph/ceph/pull/63846): [32b804b](https://github.com/ceph/ceph/commit/32b804b8e2ba29901c3b22b4da857665d0540ca1)
- Updated the deprecation instructions for the "inline data" feature in the CephFS experimental feature documentation, changing the removal time from "Q version" to "future version".
  ↳ [#63948](https://github.com/ceph/ceph/pull/63948): [d007eda](https://github.com/ceph/ceph/commit/d007edad660375ae2d14c0d27db2180bdecd7b88)
- Improved the Ceph configuration document ceph-conf.rst, optimizing text expression, terminology consistency and example explanations.
  ↳ [#63942](https://github.com/ceph/ceph/pull/63942): [a1a43bd](https://github.com/ceph/ceph/commit/a1a43bd45a2d53dad6e5f1ffb4db25c666496730)
- Added instructions on how to use the first-damage.py tool to the CephFS disaster recovery documentation.
  ↳ [#63977](https://github.com/ceph/ceph/pull/63977): [2d9840d](https://github.com/ceph/ceph/commit/2d9840d113b0106cbb558dc703d57c0f3cc3a6c1)
- Updated documentation to clarify the behavior of the --bucket and --uid flags when setting bucket quotas.
  ↳ [#64021](https://github.com/ceph/ceph/pull/64021): [1dd7da3](https://github.com/ceph/ceph/commit/1dd7da390d7a2476bcd8af579c32223f0b4945cc)
- Corrected the comment of the osd_scrub_auto_repair_num_errors configuration item to clarify that it limits the number of damaged objects attempted to be repaired during automatic repair, not the number of errors.
  ↳ [#64073](https://github.com/ceph/ceph/pull/64073): [6a824c9](https://github.com/ceph/ceph/commit/6a824c9649036bd9ee02c218afd5383389252d78)
- In the balancer operation documentation, it is supplemented that the name of the setting item that controls the uniformity of PG distribution is upmap_max_deviation.
  ↳ [#64118](https://github.com/ceph/ceph/pull/64118): [dd62d9d](https://github.com/ceph/ceph/commit/dd62d9da06c19da74003326304c0413b3b92af4b)
- Updated notification performance statistics documentation: removed obsolete pubsub_event_triggered and pubsub_event_lost metrics, added persistent_topic_size field, and improved description of pubsub_push_pending counter.
  ↳ [#64155](https://github.com/ceph/ceph/pull/64155): [30c84a0](https://github.com/ceph/ceph/commit/30c84a06e3928cbe334e5d3e4659558c21f82746) | [#64126](https://github.com/ceph/ceph/pull/64126): [9829d71](https://github.com/ceph/ceph/commit/9829d71bb2a5eb1ea8f57425b31f9826a1a2dae4) | [#64139](https://github.com/ceph/ceph/pull/64139): [83f627f](https://github.com/ceph/ceph/commit/83f627f2231db41d2392bb9e2faad241eba87463) | [#64113](https://github.com/ceph/ceph/pull/64113): [5add4c8](https://github.com/ceph/ceph/commit/5add4c8b72f31ab7b1d21df85c175913f1575062)
- Removed deprecated Jenkins command trigger phrases from PR templates, including jenkins retest this please, jenkins render docs and jenkins test ceph-volume tox.
  ↳ [#62035](https://github.com/ceph/ceph/pull/62035): [c434e8d](https://github.com/ceph/ceph/commit/c434e8d4068414311b7a00a346ded9bae69835dc)

### Build/CI
- Added systemd service unit files for ceph-exporter and integrated it into RPM packages and build systems.
  ↳ [#62270](https://github.com/ceph/ceph/pull/62270): [5ef8cc2](https://github.com/ceph/ceph/commit/5ef8cc280ca3e0f3e8a6d76c50a677b8b0931e58)
- Added btree mode to BlueStore's allocator configuration options, allowing users to choose to use BtreeAllocator.
  ↳ [#59497](https://github.com/ceph/ceph/pull/59497): [31ed605](https://github.com/ceph/ceph/commit/31ed6050a3292adf369551acc9bb1adcf6bb22e9)
- Fixed build failure caused by the client target and its dependencies not being correctly associated with the WITH_FUSE option when configuring CMake with -DWITH_LIBCEPHFS=OFF.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [30ae9e3](https://github.com/ceph/ceph/commit/30ae9e3a516aef69aafc8b087a9f25b69819220f)
- Fixed an RPM build error caused by not packaging the rgw-gap-list man page file when building CentOS.
  ↳ [#63728](https://github.com/ceph/ceph/pull/63728): [b02edf2](https://github.com/ceph/ceph/commit/b02edf24af4cdbab9be9098bc6af98fb9a604076) | [#63998](https://github.com/ceph/ceph/pull/63998): [ef95207](https://github.com/ceph/ceph/commit/ef95207ef32174e064eae676ba91970d59ce2e20)
- Added man page documentation for rgw-gap-list tool.
  ↳ [#63728](https://github.com/ceph/ceph/pull/63728): [13abdbd](https://github.com/ceph/ceph/commit/13abdbde02f17e9d57462966f532832c6deda65d) | [#63996](https://github.com/ceph/ceph/pull/63996): [24b68e2](https://github.com/ceph/ceph/commit/24b68e25a4485c600a4c1d2b5975ff356049cce3)
- Fixed lxml dependency version to fix dashboard test failure issue.
  ↳ [#62257](https://github.com/ceph/ceph/pull/62257): [8651046](https://github.com/ceph/ceph/commit/8651046c36b76b22548714b5423780ea9390a0ec)
- Deprecate the transifex-i18ntool tool and use transifex CLI for international translation management.
  ↳ [#63287](https://github.com/ceph/ceph/pull/63287): [f2dd32b](https://github.com/ceph/ceph/commit/f2dd32b5674c5f8ee8eb0eb3f63afac171051a67)
- In the build configuration, added link dependency on libfmt for the os library.
  ↳ [#61910](https://github.com/ceph/ceph/pull/61910): [d5b2749](https://github.com/ceph/ceph/commit/d5b2749f35e542291aa743efd7b68a95afa05cea)
- Fixed compilation errors caused by missing standard library header files under GCC 14.
  ↳ [#62337](https://github.com/ceph/ceph/pull/62337): [b578675](https://github.com/ceph/ceph/commit/b5786751e5260dd54cbf2e7f84acd251b12f022e)
- Added xmltodict dependency for dashboards.
  ↳ [#62393](https://github.com/ceph/ceph/pull/62393): [215ffeb](https://github.com/ceph/ceph/commit/215ffebd693cbbb70fa9843730113060682cc03d)
- Removed client test dependency on libcephfs library.
  ↳ [#64552](https://github.com/ceph/ceph/pull/64552): [887609c](https://github.com/ceph/ceph/commit/887609c2386e45cb859b5397306cb3be965c2a30)
- Fixed linking error in libcephfs tests on Ubuntu 22.04.
  ↳ [#64552](https://github.com/ceph/ceph/pull/64552): [af037ea](https://github.com/ceph/ceph/commit/af037ea48b4b861809f28acd072ff666f71adb09)
- Simplified test build configuration and removed redundant ceph-common dependency.
  ↳ [#64552](https://github.com/ceph/ceph/pull/64552): [85afd5e](https://github.com/ceph/ceph/commit/85afd5e65a931f73362c8ab95e647be7331046c6)
- Fixed GitHub Actions workflow to allow Read the Docs builds to be retriggered via PR comment command.
  ↳ [#63211](https://github.com/ceph/ceph/pull/63211): [de0c7aa](https://github.com/ceph/ceph/commit/de0c7aa864c7e3ce74ae21b91ca3788e10bd3f61)
- Updated project version number from 19.2.2 to 19.2.3.
  ↳ [#64552](https://github.com/ceph/ceph/pull/64552): [c92aebb](https://github.com/ceph/ceph/commit/c92aebb279828e9c3c1f5d24613efca272649e62)

### Maintenance
- Improve ceph-kvstore-tool to open the database in read-only mode when performing read-only operations to avoid unnecessary writes.
  ↳ [#62123](https://github.com/ceph/ceph/pull/62123): [799f361](https://github.com/ceph/ceph/commit/799f361e11bb1fbda6264965849bd0c09480789d)
- Add a dedicated debug log subsystem for the RGW notification module and output event details in the log.
  ↳ [#60784](https://github.com/ceph/ceph/pull/60784): [bc2bca9](https://github.com/ceph/ceph/commit/bc2bca96222ecdc9c55ab2b0a6d1619fb44da7a5)
- Fixed extra spaces before the return statement of the url_decode function in the src/rgw/rgw_common.cc file.
  ↳ [#64049](https://github.com/ceph/ceph/pull/64049): [b166abe](https://github.com/ceph/ceph/commit/b166abef501868f55c09775198be07ce239f637d)
- Added display of the latest snapshot sequence number (seq) in the listsnaps command output of the rados tool.
  ↳ [#63241](https://github.com/ceph/ceph/pull/63241): [afcc1c8](https://github.com/ceph/ceph/commit/afcc1c8da8d140630930d1a94f502c1ba760ab14)
- Fixed documentation error for ceph_exporter command line options, restored --prio-limit option description and removed incorrect --cert-file option description.
  ↳ [#61419](https://github.com/ceph/ceph/pull/61419): [4240aff](https://github.com/ceph/ceph/commit/4240aff25056791f409d6b5c83ae5bcd69d10a2a) | [#61448](https://github.com/ceph/ceph/pull/61448): [3049768](https://github.com/ceph/ceph/commit/3049768e698e30603e449cec95c3699361599ecb)
- Allow the pg export command of ceph-objectstore-tool to use the --no-superblock option.
  ↳ [#62123](https://github.com/ceph/ceph/pull/62123): [1a07a8d](https://github.com/ceph/ceph/commit/1a07a8d227ed1751b35de0e897259bcbfec64169)
- Added --data-path and --op options to ceph-bluestore-tool, as aliases of --path and --command respectively.
  ↳ [#62123](https://github.com/ceph/ceph/pull/62123): [da5b1ec](https://github.com/ceph/ceph/commit/da5b1ecd161751e00cc9ddf30abeba338c129fa8)
- In the close() method of NBDStream, call nbd_shutdown() before closing the connection to avoid unexpected disconnection warnings from the server.
  ↳ [#63406](https://github.com/ceph/ceph/pull/63406): [5ddbfc3](https://github.com/ceph/ceph/commit/5ddbfc363e31deb373e1b628811b8d86c6d9f56f)
- Removed unused header file sync_filesystem.h.
  ↳ [#60613](https://github.com/ceph/ceph/pull/60613): [c148d0f](https://github.com/ceph/ceph/commit/c148d0f18e75b560d2aa1dbd0fac51e042524d26)
- Added debug log in MDS's Locker::encode_lease function to output encoding lease details.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [1e3e4c0](https://github.com/ceph/ceph/commit/1e3e4c0fd7fc6980487f41f9c66882358729bc5d)
- Fixed the printing method of thread names in log dumps, combining multiple thread names of the same process into one line of output to avoid repeated printing.
  ↳ [#61287](https://github.com/ceph/ceph/pull/61287): [6d31238](https://github.com/ceph/ceph/commit/6d312389b4d60c3d259250bc49a69146546fb2cb)
- Added or updated unified thread names for multiple threads in the MDS subsystem to improve consistency and readability.
  ↳ [#61287](https://github.com/ceph/ceph/pull/61287): [c3b7dc1](https://github.com/ceph/ceph/commit/c3b7dc116a1f40fde1119164c2d55dc81ec67f4c)
- In the insert_trace function that handles metadata requests on the client, a new debug log is added to output InodeStat information.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [69f14fc](https://github.com/ceph/ceph/commit/69f14fcebc5ff583eae80c9acce95202f1799469)
- Hide parquet related dependencies when the parquet-select option is disabled.
  ↳ [#62959](https://github.com/ceph/ceph/pull/62959): [ce96a89](https://github.com/ceph/ceph/commit/ce96a894875dce305a6a662cdc9de4de965dfc78)
- Added print method to UserPerm class for debugging output.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [edb4074](https://github.com/ceph/ceph/commit/edb4074d8dbe0740d3b1470ebd5c5904f3f1ac84)
- Added ceph_daemon filter to query in RGW Overview Grafana panel to fix issue where all RGW service data is still displayed when filtering by service.
  ↳ [#62267](https://github.com/ceph/ceph/pull/62267): [9c6dd2c](https://github.com/ceph/ceph/commit/9c6dd2c86d316ded049a7514505c531b50789adb)
- Adjusted logging level of data read in RGWPutACLs_ObjStore::get_params from 0 to 20 to avoid logging input data by default.
  ↳ [#61161](https://github.com/ceph/ceph/pull/61161): [383661b](https://github.com/ceph/ceph/commit/383661be400fc4de2cd33c932fe42e4eef4d0a62)
- Updated multiple chart panels in the monitoring dashboard from the old SimpleGraphPanel format to the TimeSeries panel format to fix inconsistent line chart display issues.
  ↳ [#62383](https://github.com/ceph/ceph/pull/62383): [0443fbb](https://github.com/ceph/ceph/commit/0443fbb9b8aac1cc58df1dc270c696d5c0e754ee) | [#62384](https://github.com/ceph/ceph/pull/62384): [007ff30](https://github.com/ceph/ceph/commit/007ff30beafda999a0a9c1839c9a62c9c01140fe)
- Added multiple log outputs to the client's _lookup debugging path to assist in diagnosing the directory entry search process.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [250264b](https://github.com/ceph/ceph/commit/250264be832be1ded7cdf38312326e46ccbbc52f)
- When the client sets the file mode, change the mode value in the log output to be displayed in octal format.
  ↳ [#62095](https://github.com/ceph/ceph/pull/62095): [8564b1c](https://github.com/ceph/ceph/commit/8564b1cfd8ae61e0251c536e2807c1802196ee1b)
- Updated the list of Jenkins commands in the PR template, adding corresponding Jenkins job links and job definition links for each command.
  ↳ [#62035](https://github.com/ceph/ceph/pull/62035): [0ef706e](https://github.com/ceph/ceph/commit/0ef706ee1031aa46fe9e8c13845c291a9b871f99)

### Others
- Comprehensive formatting and wording fixes to the vault.rst documentation.
  ↳ [#63229](https://github.com/ceph/ceph/pull/63229): [e5844fb](https://github.com/ceph/ceph/commit/e5844fb3cb81d5489f15e102a8e8c8e54fb2c6d5)
- Fixed two typos in debugging documentation.
  ↳ [#63993](https://github.com/ceph/ceph/pull/63993): [d32e36c](https://github.com/ceph/ceph/commit/d32e36c83f07bbf66a426738b28c94438ebe49f8)
- Removed unnecessary formatting in HybridAllocator log output.
  ↳ [#62540](https://github.com/ceph/ceph/pull/62540): [9863ea5](https://github.com/ceph/ceph/commit/9863ea5113a6372a68b2cb81187fde9c6fe2bb89)
- Fix initialization order of ParallelPGMapper objects in test cases to avoid potential crashes.
  ↳ [#58919](https://github.com/ceph/ceph/pull/58919): [fef1fed](https://github.com/ceph/ceph/commit/fef1fed194e6fe9d3c82853a2f590351d40864f0)
- Fixed multi-threaded access to non-atomic variables in tests to ensure thread safety.
  ↳ [#62311](https://github.com/ceph/ceph/pull/62311): [66f38ba](https://github.com/ceph/ceph/commit/66f38baf3bce5272f7add32340381e2fa3ab50c8)
- Updated the dashboard front-end dependency package configuration file.
  ↳ [#62353](https://github.com/ceph/ceph/pull/62353): [0b5d436](https://github.com/ceph/ceph/commit/0b5d43618ea3660563eec520b0cf5f8cf89c6345)
- Updated link to backporter manual in development workflow documentation.
  ↳ [#63990](https://github.com/ceph/ceph/pull/63990): [1f07aed](https://github.com/ceph/ceph/commit/1f07aed784ae2c1fdd177bcacf6fd7c2d0b9c606)
- Fixed typos in HACKING.rst documentation and cleaned up whitespace formatting.
  ↳ [#61377](https://github.com/ceph/ceph/pull/61377): [e6cf729](https://github.com/ceph/ceph/commit/e6cf7299a3cac5b11bfd1254cbf7e3e185a06605)
- Fixed a typo in the controller section of the hardware recommendations document.
  ↳ [#61178](https://github.com/ceph/ceph/pull/61178): [1339b4c](https://github.com/ceph/ceph/commit/1339b4c0c7fc6ddf9a40c2c2642e314608caaa02)
- Fixed syntax and notation in CephFS snapshot documentation.
  ↳ [#61459](https://github.com/ceph/ceph/pull/61459): [559153f](https://github.com/ceph/ceph/commit/559153f1a7e273e3f06d04d93b8cd52217473131)
- Clean up formatting issues and clarify terminology in Disaster Recovery Expert documentation.
  ↳ [#61446](https://github.com/ceph/ceph/pull/61446): [816b59e](https://github.com/ceph/ceph/commit/816b59e281b6ba82ac31f7d539a4a5e683450d6d)
- Optimized the text description of the backup metadata pool recovery section in the disaster recovery expert documentation.
  ↳ [#61479](https://github.com/ceph/ceph/pull/61479): [890bd61](https://github.com/ceph/ceph/commit/890bd6173d46f40d60a15a5c696d4d4f8b248148)
- Fixed the English description of a note about host management in the Cephadm documentation.
  ↳ [#61528](https://github.com/ceph/ceph/pull/61528): [cd81646](https://github.com/ceph/ceph/commit/cd81646c1af7e62513ee6978007fa9278ccfad36)
- Fixed terminology in multisite documentation, correcting "zonegroup" to "pools".
  ↳ [#61556](https://github.com/ceph/ceph/pull/61556): [b5cdff3](https://github.com/ceph/ceph/commit/b5cdff322eda09a607a8019e51d8d76821cbb9f5)
- Fixed mathematical representation of device size description in cephadm documentation.
  ↳ [#61574](https://github.com/ceph/ceph/pull/61574): [3cb6e9b](https://github.com/ceph/ceph/commit/3cb6e9b5be7f87724dba71a3a9a1daba89712592)
- Improved description of the "Activate an existing OSD" section in the Cephadm documentation.
  ↳ [#61747](https://github.com/ceph/ceph/pull/61747): [c13c3e3](https://github.com/ceph/ceph/commit/c13c3e33e12ea76d15579682e87de4d7f7606940)
- Removed redundant license files in the src/dmclock directory.
  ↳ [#62363](https://github.com/ceph/ceph/pull/62363): [be78098](https://github.com/ceph/ceph/commit/be780984314b4faf598eaa1916f9863ec4418fd9)
- Fixed a potential segfault issue caused by the watch/notify callback in TestImageReplayer not being fully refreshed.
  ↳ [#61958](https://github.com/ceph/ceph/pull/61958): [c2f4345](https://github.com/ceph/ceph/commit/c2f43453f1dd49dd0e9063a0a8255171e6045a5c)
- Added unit tests for file block-level diffing for the CephFS snapshot diffing feature.
  ↳ [#63241](https://github.com/ceph/ceph/pull/63241): [4944946](https://github.com/ceph/ceph/commit/49449469eeec68bd0d328c731b89f1836af9b739)
- Fixed an incorrect subcommand for radosgw-admin in the documentation.
  ↳ [#62004](https://github.com/ceph/ceph/pull/62004): [8a18a37](https://github.com/ceph/ceph/commit/8a18a37a4ed845e722fa322404223b641117286b)
- Fixed typo in BlueStore configuration reference documentation.
  ↳ [#62290](https://github.com/ceph/ceph/pull/62290): [428b9c2](https://github.com/ceph/ceph/commit/428b9c2d5cfe7ee592fe9a1fdae8708c5f535cc8)
- Improved instructions for PG in the RADOS troubleshooting documentation, removing redundant dollar sign prompts.
  ↳ [#62320](https://github.com/ceph/ceph/pull/62320): [0ee9930](https://github.com/ceph/ceph/commit/0ee99306426b61e2de5ee7e566644f5f49b4e0d5)
- Fixed a syntax error in the image filter query statement in the RBD details Grafana panel.
  ↳ [#62531](https://github.com/ceph/ceph/pull/62531): [c89aa90](https://github.com/ceph/ceph/commit/c89aa90c3e5b63d92ba90fcf4cf8cf8cea171ead)
- Fixed wording in ceph-conf.rst document and description of configuration command return values.
  ↳ [#62620](https://github.com/ceph/ceph/pull/62620): [9316a64](https://github.com/ceph/ceph/commit/9316a645562a977d8a446c7e9f8323ede0a73afc)
- Improved the English description of the "Maintenance Mode" section in the Cephadm documentation.
  ↳ [#63495](https://github.com/ceph/ceph/pull/63495): [f441626](https://github.com/ceph/ceph/commit/f4416263f3554f4d7947e1dabcc9c2056f987aa0)
- Fixed a misspelled command in the cephadm upgrade documentation.
  ↳ [#62644](https://github.com/ceph/ceph/pull/62644): [4c475dd](https://github.com/ceph/ceph/commit/4c475dd391994337b919b7b1a1c20dbbe9bdff94)
- Improved wording and formatting of radosgw cloud-restore and cloud-transition documentation.
  ↳ [#62666](https://github.com/ceph/ceph/pull/62666): [c534ee2](https://github.com/ceph/ceph/commit/c534ee267a616390c2a89844b956694fd374a592)
- Improved the terminology, format and presentation of Cephadm RGW service documentation.
  ↳ [#62694](https://github.com/ceph/ceph/pull/62694): [da31314](https://github.com/ceph/ceph/commit/da31314e2a496c2b292bb94275a06c869c8104c8)
- Fixed link formatting errors and code block formatting in cloud storage transition documents.
  ↳ [#62834](https://github.com/ceph/ceph/pull/62834): [10a5a0c](https://github.com/ceph/ceph/commit/10a5a0c00ecbd7a7663b3ced5c1b17191fbdabb7)
- Fixed formatting issue with device availability description in OSD documentation.
  ↳ [#62810](https://github.com/ceph/ceph/pull/62810): [7fe53ec](https://github.com/ceph/ceph/commit/7fe53ec65f1a26131b2060b9758ba9c1882a870d)
- Modified wording of sentences in documentation regarding multi-tenant metric description.
  ↳ [#63700](https://github.com/ceph/ceph/pull/63700): [6be9ab9](https://github.com/ceph/ceph/commit/6be9ab9bba71ffc56fa6463278e211c0dad48a49)
- Fixed RST syntax error in documentation and added bash prompt for example commands.
  ↳ [#62989](https://github.com/ceph/ceph/pull/62989): [e779658](https://github.com/ceph/ceph/commit/e779658bc0c351056058a0407d7e910e06d9c491)
- Updated layout instructions in radosgw documentation, corrected formatting and RST syntax of CLI command examples.
  ↳ [#63915](https://github.com/ceph/ceph/pull/63915): [c038c70](https://github.com/ceph/ceph/commit/c038c70f695158d16407d7604ce3f252e8fdebf5)
- Fixed markup error in Cephadm RGW service documentation to eliminate warnings.
  ↳ [#63073](https://github.com/ceph/ceph/pull/63073): [4949311](https://github.com/ceph/ceph/commit/49493112d5dcf871d5a2a9d1d71ef6d265729c32)
- Edited the administrator documentation, added a command prompt and corrected the English description.
  ↳ [#63207](https://github.com/ceph/ceph/pull/63207): [28ca1f0](https://github.com/ceph/ceph/commit/28ca1f0fa536e35a233bdd458e5d6e52bea33d7c)
- Corrected formatting in cephadm upgrade documentation, changing command examples to the correct code block style.
  ↳ [#63147](https://github.com/ceph/ceph/pull/63147): [7300fb2](https://github.com/ceph/ceph/commit/7300fb24bb1cb781f26dfa0e2d8fd0f7b61053bf)
- Multiple format and content optimizations have been made to dynamic resharding documents.
  ↳ [#64058](https://github.com/ceph/ceph/pull/64058): [c8d58c9](https://github.com/ceph/ceph/commit/c8d58c9cf31f6bd4288679469105e45bccdd8ec5)
- Edited the index.rst file in the Ceph API documentation and adjusted the format of the authentication example.
  ↳ [#63197](https://github.com/ceph/ceph/pull/63197): [d202bbd](https://github.com/ceph/ceph/commit/d202bbd0c5f82dc26e4cbb247cc69d7881eff90f)
- Edited the document file doc/mgr/alerts.rst and corrected the English description.
  ↳ [#63200](https://github.com/ceph/ceph/pull/63200): [3aeffe6](https://github.com/ceph/ceph/commit/3aeffe6effd4293a03ea297a2a2e4335718a60f8)
- Edited the documentation file doc/mgr/cli_api.rst and corrected the text expression and format.
  ↳ [#63689](https://github.com/ceph/ceph/pull/63689): [0c997db](https://github.com/ceph/ceph/commit/0c997db69f2c40b4f2b10c7bbcccb28b0049b548)
- Fixed punctuation format issues in cephfs-mirroring development documentation.
  ↳ [#63250](https://github.com/ceph/ceph/pull/63250): [02ada2e](https://github.com/ceph/ceph/commit/02ada2e96c0ff662c29c82aff329a7f5b8aa18fc)
- Modified the format of the list in the monitoring document to make it clearer and easier to read.
  ↳ [#63541](https://github.com/ceph/ceph/pull/63541): [f3102f1](https://github.com/ceph/ceph/commit/f3102f1d9a1e3fca5522d8a3ea17eb6023c94682)
- Fixed cross-reference link formatting in CephFS documentation regarding paused cloning threads and paused cleanup threads.
  ↳ [#63544](https://github.com/ceph/ceph/pull/63544): [a23983e](https://github.com/ceph/ceph/commit/a23983ead7ef97272920a631c92d97d80b81f4cc)
- Added command prompt format to mgr/crash documentation and corrected some English expressions.
  ↳ [#63538](https://github.com/ceph/ceph/pull/63538): [5b8ebd0](https://github.com/ceph/ceph/commit/5b8ebd01ef4eea151f2325de1a7ffebde07ff276)
- Several grammatical and formatting corrections have been made to the CephFS image development documentation to improve readability.
  ↳ [#63298](https://github.com/ceph/ceph/pull/63298): [86b67fa](https://github.com/ceph/ceph/commit/86b67faa311dd19b813e0734eb159acd33fd630e) | [#63273](https://github.com/ceph/ceph/pull/63273): [8214281](https://github.com/ceph/ceph/commit/82142819f6aa2b15b7c54b69b4a0bdaa247551bd) | [#63547](https://github.com/ceph/ceph/pull/63547): [95384f5](https://github.com/ceph/ceph/commit/95384f5a3572e2730af40c0ef3e2acb6c425fadc)
- Updated hyperlinks in Ceph documentation, replacing external links with internal reference tags and fixing broken links.
  ↳ [#63311](https://github.com/ceph/ceph/pull/63311): [b853864](https://github.com/ceph/ceph/commit/b853864154894f4bdf5ee702df3a4ae6aaa4825c)
- Improved text formatting and punctuation of Ceph Dashboard MOTD documentation.
  ↳ [#63402](https://github.com/ceph/ceph/pull/63402): [3df7a99](https://github.com/ceph/ceph/commit/3df7a997450e88fecb2fcc428d933073f2419f08)
- Fixed syntax and improved formatting of disk prediction module documentation.
  ↳ [#63423](https://github.com/ceph/ceph/pull/63423): [cad3539](https://github.com/ceph/ceph/commit/cad3539a33d44ea1183850a5490d5b9dde7d2026)
- Rewrote sentences in mgr/hello documentation to improve grammar.
  ↳ [#63507](https://github.com/ceph/ceph/pull/63507): [c6d0110](https://github.com/ceph/ceph/commit/c6d011087f5aa18d0cf4fbea130af1e58225e2f7)
- Fixed command line prompt formatting, code block tags and text formatting in influx module documentation.
  ↳ [#63454](https://github.com/ceph/ceph/pull/63454): [a025fd9](https://github.com/ceph/ceph/commit/a025fd978cc32a934bdb94b7e8f151bdd4d1240b)
- Improved English description of mgr/insights documentation.
  ↳ [#63510](https://github.com/ceph/ceph/pull/63510): [02f4ee7](https://github.com/ceph/ceph/commit/02f4ee74510b66f41ad42618b90d8cd945cd87e7)
- Improved the English description of the iostat module documentation and optimized the format.
  ↳ [#63513](https://github.com/ceph/ceph/pull/63513): [f090a2e](https://github.com/ceph/ceph/commit/f090a2ed25aeb59866183ab41c3154d26f6e3740)
- Improved the English description of the localpool module documentation and optimized the format.
  ↳ [#63550](https://github.com/ceph/ceph/pull/63550): [b6a5f55](https://github.com/ceph/ceph/commit/b6a5f553c2d81f30500352d59e3168ad38269a24)
- Fixed a typo in the pgcalc documentation.
  ↳ [#63498](https://github.com/ceph/ceph/pull/63498): [03b2ee2](https://github.com/ceph/ceph/commit/03b2ee2bd9c40ad3e101a041dcb7a868b7b43d20)
- Fixed punctuation and code example indentation formatting in mgr/progress documentation.
  ↳ [#63586](https://github.com/ceph/ceph/pull/63586): [f5ca755](https://github.com/ceph/ceph/commit/f5ca7550ee3dab3cefafca4270388a5cb5f9618b)
- Unified the command prompt format of the Prometheus module documentation and corrected the IP address in the example.
  ↳ [#63589](https://github.com/ceph/ceph/pull/63589): [55931d0](https://github.com/ceph/ceph/commit/55931d0d531a9405d4c736b658feb9f47dad3ff5)
- Updated command line example format and description text for mgr/rgw documentation.
  ↳ [#63592](https://github.com/ceph/ceph/pull/63592): [79e4e8b](https://github.com/ceph/ceph/commit/79e4e8b9f1b92cf97ad36e4b150a4de4ef341962)
- Updated command example format in telegraf module documentation to prompt blocks with syntax highlighting.
  ↳ [#63611](https://github.com/ceph/ceph/pull/63611): [891fed6](https://github.com/ceph/ceph/commit/891fed65947aed4cfe6aef897d8ad12ef03a9cb6)
- Improved the English description of the telemetry module documentation and unified the command line example format.
  ↳ [#63692](https://github.com/ceph/ceph/pull/63692): [62d5f02](https://github.com/ceph/ceph/commit/62d5f0263661f5945092732372c57df5ea2f940c)
- Removed an extra word in the local pool documentation example.
  ↳ [#63669](https://github.com/ceph/ceph/pull/63669): [6ada5f5](https://github.com/ceph/ceph/commit/6ada5f527ee14477619d3910819bd00dbe612f5e)
- Changed the word "called" to "named" in the module development guide.
  ↳ [#63666](https://github.com/ceph/ceph/pull/63666): [4752b97](https://github.com/ceph/ceph/commit/4752b9739ca20890c3d1f6dad9b50fdda900c20d)
- Fixed the expression in the "Build the Source" section of the documentation and the misuse of the word "presently".
  ↳ [#63652](https://github.com/ceph/ceph/pull/63652): [bf32df3](https://github.com/ceph/ceph/commit/bf32df39ef9288e6b840a0f9d69dfe8b30f85869)
- Change "OMAP" in the document glossary to the lowercase form "omap".
  ↳ [#63737](https://github.com/ceph/ceph/pull/63737): [c85285e](https://github.com/ceph/ceph/commit/c85285efaef2e40755d0a1cd6c9e1540b5676721)
- Adjusted wording of license parameter description in telemetry documentation.
  ↳ [#63905](https://github.com/ceph/ceph/pull/63905): [dfd60f5](https://github.com/ceph/ceph/commit/dfd60f550babbba784c359f80185808b89413ab2)
- Optimized the text expression and format of the first 100 lines of the cloud conversion document.
  ↳ [#64024](https://github.com/ceph/ceph/pull/64024): [d597f73](https://github.com/ceph/ceph/commit/d597f73049f21e8f2901087db649b4a454310e69)
- Updated link to AWS specification format in documentation.
  ↳ [#64095](https://github.com/ceph/ceph/pull/64095): [76c579f](https://github.com/ceph/ceph/commit/76c579fbf5749997efb3c6c81fcf6604d59520fe)
