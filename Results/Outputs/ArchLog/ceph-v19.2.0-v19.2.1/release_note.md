# Release Note

## Important Changes

### Core Storage Engine Layer
- Added block device multi-tag support for BlueStore/BlueFS, including reading/checking tags, upgrade mode, public API, fsck checking and device compatibility handling. (Architecture-related: BlueStore block device tags)
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [dca32d4](https://github.com/ceph/ceph/commit/dca32d4126f81092253a3681c2c4a505969e358d), [6a5d9c7](https://github.com/ceph/ceph/commit/6a5d9c7861892f59281342d2da6a8d21b0229f69), [33a6880](https://github.com/ceph/ceph/commit/33a6880009536432d18a0025885c79009a8f466c), [d4224aa](https://github.com/ceph/ceph/commit/d4224aae3973089898db405686b095e9cbac063c), [316587a](https://github.com/ceph/ceph/commit/316587a42b831bd61fd6fce8a71d5eee9664c975), [bf8e253](https://github.com/ceph/ceph/commit/bf8e253bcee765bb21d3811694d8fc84600347fc), [9a359e6](https://github.com/ceph/ceph/commit/9a359e66b8d2c9e3008e01a823a37c8c5c56af0f), [54cbe2f](https://github.com/ceph/ceph/commit/54cbe2f88f58c2caacb57086a35fa5016f6bd45f), [7f6ec55](https://github.com/ceph/ceph/commit/7f6ec55b3c2650aef855b396a4e1cd33fd03092b)
- Changed the manual compression operation to asynchronous execution, and updated the ObjectStore::compact interface. (Architecture-related: public API)
  ↳ [#58740](https://github.com/ceph/ceph/pull/58740): [38380a3](https://github.com/ceph/ceph/commit/38380a37be659d175fb912ced687ef6ed8d3b8f1)
- Fixed the problem of BlueStore NCB space leakage when bdev_async_discard is enabled. (Architecture-related: build and installation methods)
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [cf86152](https://github.com/ceph/ceph/commit/cf861523cf42f034ce4f0b128cc48e100d1bf486)
- Fixed the error in the enabling conditions and feature mask usage of the CRUSH_MSR feature in OSDMap. (Architecture-related: public API)
  ↳ [#59492](https://github.com/ceph/ceph/pull/59492): [c275ad8](https://github.com/ceph/ceph/commit/c275ad87e7a48bb68fa36991ed23e72898eeff9c), [148c572](https://github.com/ceph/ceph/commit/148c572f067f5be315c50c25d78cd9482c754fda)
- Fixed the problem of inaccurate acquisition of asynchronous operation version number and decryption of encrypted multi-part objects in RGW. (Architecture-related: public API)
  ↳ [#60065](https://github.com/ceph/ceph/pull/60065): [ac6f659](https://github.com/ceph/ceph/commit/ac6f659f6c0b94a82c4a0da4a24d9a84f233026e) | [#60130](https://github.com/ceph/ceph/pull/60130): [dfd078a](https://github.com/ceph/ceph/commit/dfd078a4d4d802b84655ffb222e568192cb82193)
- Added crush feature check when creating erasure coding crush rules, and adjusted the parameter type of validate_crush_against_features function from stringstream& to ostream&. (architecture-related: public API)
  ↳ [#59492](https://github.com/ceph/ceph/pull/59492): [e8f5b90](https://github.com/ceph/ceph/commit/e8f5b905f0f4887a7515e97799f43a2893e26f4c)
- Removed the zap_size parameter in ceph-bluestore-tool to make the device wipe operation more precise for block device labels. (Architecture-related: build and installation methods)
  ↳ [#59967](https://github.com/ceph/ceph/pull/59967): [32d0549](https://github.com/ceph/ceph/commit/32d05492503b75711b082e45ac048f0997017fe8)
- Adjust the default sharding configuration of the mClock scheduler for HDD-based OSD clusters, and update related documents. (Architecture-related: Configuration default values)
  ↳ [#59973](https://github.com/ceph/ceph/pull/59973): [3fad64d](https://github.com/ceph/ceph/commit/3fad64dbdddee8d014a446e876301fba4b3f2c73) | [#60671](https://github.com/ceph/ceph/pull/60671): [3c5606b](https://github.com/ceph/ceph/commit/3c5606b6134c56f7d084631af1cb8f74ab8cd1b1)
- Added a configuration option for the number of discard threads for the block device discard function. (Architecture-related: build and installation methods)
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [1239568](https://github.com/ceph/ceph/commit/1239568e18f5f46e0e17910c520febbadb60418e)
- Removed the bdev_async_discard configuration option and changed the default value of bdev_async_discard_threads from 1 to 0. (Architecture-related: configuration changes)
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [519730b](https://github.com/ceph/ceph/commit/519730b0b11124cad52e23f37bc1c5f059eaefdf)

### Management and Control Layer
- Added new options to set and view stretch mode parameters in the `ceph osd pool stretch` command. (Architecture-related: public API)
  ↳ [#59084](https://github.com/ceph/ceph/pull/59084): [072b08e](https://github.com/ceph/ceph/commit/072b08eddccd4654d42b1d65b36ed4d3f12c126c)
- Added `osd pool force-remove-snap` monitoring command, which is used to forcefully remove snapshots within a specific range in the specified pool. (Architecture-related: public API)
  ↳ [#59402](https://github.com/ceph/ceph/pull/59402): [c002ea6](https://github.com/ceph/ceph/commit/c002ea6d9740c3bf3681b00a56983d8feb2e561f)
- Change the return type of the ms_handle_fast_authentication method from integer to Boolean to fix logic errors in authentication processing. (Architecture-related: public API)
  ↳ [#59306](https://github.com/ceph/ceph/pull/59306): [22cd0d4](https://github.com/ceph/ceph/commit/22cd0d42a15e19d9ca3b6bd99e108993d3fd2263)
- Fixed client/session eviction command, requiring filter parameters to be provided and supporting the use of id=* to evict all clients. (Architecture-related: Management interface)
  ↳ [#58727](https://github.com/ceph/ceph/pull/58727): [ef712ce](https://github.com/ceph/ceph/commit/ef712ceecd018fc3d407b5f9a4f4ffd537c657f6)
- Modified the encoding method of MDS silent database messages, changing the payload encoding to on-demand execution to support recalculation when the message is retried. (Architecture-related: Message Encoding Contract)
  ↳ [#59517](https://github.com/ceph/ceph/pull/59517): [a4b16ad](https://github.com/ceph/ceph/commit/a4b16ad847762ac1874877b23c9fb67f6c542dca), [2972b3f](https://github.com/ceph/ceph/commit/2972b3fbc50d55dd02c984f742bad7ba329c0ecc)
- Removed the deprecated --pool option from the rbd group image add and rbd group image rm commands. (Architecture-related: public API)
  ↳ [#61172](https://github.com/ceph/ceph/pull/61172): [6725c65](https://github.com/ceph/ceph/commit/6725c65473531314a0f9e38c20923467c6ee9681)
- Fixed the encoding logic of the monitoring node address in the MonMap::encode method to ensure that the old version of librbd client will not panic when the address is inconsistent. (Architecture-related: version and compatibility)
  ↳ [#60751](https://github.com/ceph/ceph/pull/60751): [b6b5395](https://github.com/ceph/ceph/commit/b6b53951218c9c1cb9f26b040d9ae0f058138090)

### Service and API Layer
- Added the version_t parameter to the completion callback signature of librados asynchronous operations, allowing the caller to obtain the version number generated by the operation. (Architecture-related: public API)
  ↳ [#60065](https://github.com/ceph/ceph/pull/60065): [da39012](https://github.com/ceph/ceph/commit/da390122289fd948a68b07b4f693ca03bd7d7076)
- Fixed a crash caused by uint16 overflow by removing the aios_size parameter of the submit_batch function and instead submitting in batches based on the maximum I/O depth. (Architecture-related: public API)
  ↳ [#58676](https://github.com/ceph/ceph/pull/58676): [82acbb6](https://github.com/ceph/ceph/commit/82acbb63852f7c9cbd06d39727fd70471393239e)
- Fixed an issue where the "ceph fs authorize" command caused the monitor to crash when passing multiple permissions. (Architecture-related: public API)
  ↳ [#59672](https://github.com/ceph/ceph/pull/59672): [41593e9](https://github.com/ceph/ceph/commit/41593e9f3411dd1f32bafde09ac78de246cbad52)
- Fixed the problem that the IoCtxImpl::remove method in librados does not correctly use the CEPH_OSD_FLAG_FULL_FORCE flag when calling operate. (Architecture-related: public API)
  ↳ [#59284](https://github.com/ceph/ceph/pull/59284): [9297c9b](https://github.com/ceph/ceph/commit/9297c9b0f30216b806fd2a5b39baf075971abb22)
- Fixed the core dump problem caused by the client not checking the offline status of MDS when parsing MDS. (Architecture-related: public API)
  ↳ [#58587](https://github.com/ceph/ceph/pull/58587): [24fe39a](https://github.com/ceph/ceph/commit/24fe39a3b7ab9e9d3515b645b5c26aced929dd71)
- Fix the processing of HEAD requests to comply with RFC standards and solve the problem of persistent connection clients being unable to correctly parse subsequent HTTP responses. (Architecture-related: HTTP HEAD request processing)
  ↳ [#59123](https://github.com/ceph/ceph/pull/59123): [2974d05](https://github.com/ceph/ceph/commit/2974d05f31a37e78b7f595a48779d379efd6342d)
- The cls_cxx_gather and cls_cxx_get_gathered_data public functions that are not maintained and have no usage scenarios are abandoned. (Architecture-related: public API is abandoned)
  ↳ [#57819](https://github.com/ceph/ceph/pull/57819): [9ba3d51](https://github.com/ceph/ceph/commit/9ba3d51aab475b2088a618aad7c10d5124a6d245)
- Improved the usage safety of IOInterruptCondition, removed the error-prone single-parameter constructor, and changed the remaining users to explicitly specify the epoch. (Architecture-related: public API)
  ↳ [#58839](https://github.com/ceph/ceph/pull/58839): [a343d6d](https://github.com/ceph/ceph/commit/a343d6d69b73f12ac5df7566d7d3e35bdcbb104a), [dd92287](https://github.com/ceph/ceph/commit/dd92287b976a2a9767530daf6678aaf6287d441f)
- Change the return type of the read() method of the librbd migration format interface from bool to void to be consistent with the list_snaps() method. (Architecture-related: public API)
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [2df83de](https://github.com/ceph/ceph/commit/2df83de6d559fda43a772bef0234cd874581d541)

### Infrastructure Layer
- Modify the tri_mutex::get_name method and change the return type from hobject_t reference to std::string to avoid formatting problems. (Architecture-related: public API)
  ↳ [#58905](https://github.com/ceph/ceph/pull/58905): [f762a57](https://github.com/ceph/ceph/commit/f762a57fd99f491cac01af3de78e87b8767b5e04)
- Unified the asynchronous operation modes of RGW and related modules from the old API (such as async_completion) to the standard boost::asio::async_initiate, and updated the coroutine generation mechanism. (Architecture-related: Unification of asynchronous operation modes)
  ↳ [#60133](https://github.com/ceph/ceph/pull/60133): [9e0ac0d](https://github.com/ceph/ceph/commit/9e0ac0d35a96c078a3095f2888e589906577d631), [a1d8c2e](https://github.com/ceph/ceph/commit/a1d8c2ec3b63bf685fc24e5fd87d11bbf7a3cafb), [fb6b587](https://github.com/ceph/ceph/commit/fb6b587a03e8dc51042bb459cf61bb79a3cf948f), [cdbe2c1](https://github.com/ceph/ceph/commit/cdbe2c1bb4731395423ab77f3edd2ee4bd053148), [c174149](https://github.com/ceph/ceph/commit/c174149d384e0fdde3b36b9287eada400367af5f), [80aa798](https://github.com/ceph/ceph/commit/80aa798bb653599c691c636571b96644546e91d2), [631d14a](https://github.com/ceph/ceph/commit/631d14a92047088884055c6bb013ddb94580cc36), [51ec4c4](https://github.com/ceph/ceph/commit/51ec4c4021d0732e74ed2f0fb75c220edbdb310e)
- Reconstructed the source image opening logic of the RBD migration engine, changed the parsing method of SourceSpecBuilder to static, and split the opening method of OpenSourceImageRequest. (Architecture-related: public API)
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [8857cae](https://github.com/ceph/ceph/commit/8857cae3c0d5766d86e7d8b5eac3821e430ecdd5) | [#60171](https://github.com/ceph/ceph/pull/60171): [6d42d18](https://github.com/ceph/ceph/commit/6d42d18e112fe09ea72e14de69ff5cd2afd6a56c)

### Cross-cutting / Other Architecture-related Changes
- Extend jsonnet build dependencies to all distributions to ensure build checks run properly. (Architecture-related: build and installation methods)
  ↳ [#60075](https://github.com/ceph/ceph/pull/60075): [bfd5d35](https://github.com/ceph/ceph/commit/bfd5d3503ade1f1b9861737c1dc8d072c4bb4d36)

## Routine Changes

### New features
- Added statistics and output of S3Select data processing volume and return volume to the RGW log function.
  ↳ [#59120](https://github.com/ceph/ceph/pull/59120): [c84b790](https://github.com/ceph/ceph/commit/c84b7902edcdbecf655fa7a52645e53d2adb3f27)
- The snapdiff API was introduced in cephfs_mirror to implement incremental synchronization and only synchronize the file differences between two snapshots, thereby improving synchronization efficiency.
  ↳ [#58984](https://github.com/ceph/ceph/pull/58984): [8cb960e](https://github.com/ceph/ceph/commit/8cb960e9760df587015c43a46ea550946cc86a12)
- Added multi-thread discard support for kernel devices, allowing the number of threads to be dynamically adjusted and respond to configuration changes.
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [91b0fe4](https://github.com/ceph/ceph/commit/91b0fe4d51cebb5667f3e58093ecc1346071f1f0), [a776b6e](https://github.com/ceph/ceph/commit/a776b6e9250808be7b8d4ac945352ad0ffe09791)
- Added new metrics for monitoring snapshot synchronization performance for the CephFS mirroring tool, including synchronization time, duration and number of synchronized bytes.
  ↳ [#59070](https://github.com/ceph/ceph/pull/59070): [5e572b9](https://github.com/ceph/ceph/commit/5e572b9f71068457c091d5c2d56604c2c221637d), [e7e8a2b](https://github.com/ceph/ceph/commit/e7e8a2b28ca5b6f5f65a639dfe7040dded7aaec7), [a63e5d2](https://github.com/ceph/ceph/commit/a63e5d2884260c7aaa27c17b6c54ed529a00ee5b), [65df0b4](https://github.com/ceph/ceph/commit/65df0b46b5e239cf8bf2ec31cc44babf02151c25)
- Added end-to-end data protection support for Seastore engine's random block devices.
  ↳ [#59298](https://github.com/ceph/ceph/pull/59298): [6373b6d](https://github.com/ceph/ceph/commit/6373b6d253aaa628f47cb74921e34d8cdf6b4473), [9989ecf](https://github.com/ceph/ceph/commit/9989ecf119ccf5393f0c1e4b5b016592c187fad5)
- Added an alarm mechanism for slow operations and read stagnation for BlueStore and BlueFS. Users can control the duration and triggering threshold of the alarm through configuration.
  ↳ [#59464](https://github.com/ceph/ceph/pull/59464): [fff1105](https://github.com/ceph/ceph/commit/fff1105ab82fcae5a3ecc383006cf94d4dd4e06e)
- Added "refresh" capability to LBA mapping and optimized parent node mapping acquisition.
  ↳ [#58957](https://github.com/ceph/ceph/pull/58957): [636e3da](https://github.com/ceph/ceph/commit/636e3dab4b3d8f37265445816c982c525495f3b0)
- Allow the IOInterruptCondition constructor to accept the specified epoch parameter.
  ↳ [#58839](https://github.com/ceph/ceph/pull/58839): [f2aea46](https://github.com/ceph/ceph/commit/f2aea46f704e30782c50f0b829c1645996e46f2e)
- When end-to-end data protection is enabled, CRC check calculation is disabled.
  ↳ [#59298](https://github.com/ceph/ceph/pull/59298): [8c25951](https://github.com/ceph/ceph/commit/8c25951d76d7612ae929bc283a601da76bac9198)
- When the device supports end-to-end data protection, the CRC check of the circular log space header is skipped.
  ↳ [#59298](https://github.com/ceph/ceph/pull/59298): [0887cbc](https://github.com/ceph/ceph/commit/0887cbc5c40ae9828aa1e15d90c32880f6df930a)
- Added 'realm default rm' command to radosgw-admin, which is used to clear the current default realm.
  ↳ [#59445](https://github.com/ceph/ceph/pull/59445): [e352264](https://github.com/ceph/ceph/commit/e352264128ed15dbf89338859d68cc4697870663)
- Added zap-device command to bluestore-tool, and updated tag reading and writing logic to support multi-device tags.
  ↳ [#59967](https://github.com/ceph/ceph/pull/59967): [2d56165](https://github.com/ceph/ceph/commit/2d56165fc70f17cfbb294f5ea4631dcb4fe7531e)
- Allow ceph-bluestore-tool to execute show-label command while OSD is running.
  ↳ [#59967](https://github.com/ceph/ceph/pull/59967): [9901166](https://github.com/ceph/ceph/commit/9901166964422caf0352a450b42198eda7230a4d)
- Introduced thread name saving and retrieval infrastructure for the logging system so that thread names can be read directly when dumping logs.
  ↳ [#60279](https://github.com/ceph/ceph/pull/60279): [151cce1](https://github.com/ceph/ceph/commit/151cce14f5c45fc2511b76799e5b07851a1cdc07)
- Added statistics collection functionality for the random block device writer.
  ↳ [#58828](https://github.com/ceph/ceph/pull/58828): [8d816e1](https://github.com/ceph/ceph/commit/8d816e125015c87ff568f79d97f1a5e6f76722fb)
- Added new member variables to the Onode class to improve log display.
  ↳ [#58830](https://github.com/ceph/ceph/pull/58830): [4b6bd5c](https://github.com/ceph/ceph/commit/4b6bd5c4cbdd57767ccb98eab38d9d9f40bb1763)
- Added TPM2 token registration support for encrypted OSDs to ceph-volume and cephadm.
  ↳ [#59196](https://github.com/ceph/ceph/pull/59196): [73e9c6c](https://github.com/ceph/ceph/commit/73e9c6ce45be1b1d990b530e5639e0aa2c003e01)
- Added documentation for the `ceph orch device replace` command.
  ↳ [#60486](https://github.com/ceph/ceph/pull/60486): [07c7356](https://github.com/ceph/ceph/commit/07c7356fd36c4931cdb0a385d39b6750afa80754)

### bug fixes
- Fixed multiple logic errors related to block device tag reading and writing, checking, fsck and configuration in BlueStore to ensure data consistency and operational correctness.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [fe6e7eb](https://github.com/ceph/ceph/commit/fe6e7eb1127a2098fc2245cdc01ab6b0fdd3d4c4), [1118b27](https://github.com/ceph/ceph/commit/1118b272f73cd8a101ab9c109def91bae8496131), [9fa091b](https://github.com/ceph/ceph/commit/9fa091bd01a7ed40668edd6d0df71cf9ea2d6a61), [ac08809](https://github.com/ceph/ceph/commit/ac088096b7f625e7012c5317b2b18172920104fb), [1376e43](https://github.com/ceph/ceph/commit/1376e4322a44d5556fbe281510e19151d9103761), [806f615](https://github.com/ceph/ceph/commit/806f6152c548f6b6050b566519978d3358f80544), [dd43c6d](https://github.com/ceph/ceph/commit/dd43c6d1ac13750b48f458bd724f597f73cb839d), [619cc7b](https://github.com/ceph/ceph/commit/619cc7b14d2478f20aa1039bd9d317fc43bdd8d6), [17fcb9a](https://github.com/ceph/ceph/commit/17fcb9a92f8b8bc7161dc6966ab7a81cb26c6547), [ee362b8](https://github.com/ceph/ceph/commit/ee362b8e59a57fbe51b3b721d7264b9e17514838), [8a36e77](https://github.com/ceph/ceph/commit/8a36e77c8e079c4d743e94c000f70d6bd2f1ed4b), [ea19a18](https://github.com/ceph/ceph/commit/ea19a1814b91cff2b969699300237d19b234c264), [07feffe](https://github.com/ceph/ceph/commit/07feffe6ce5ff4172fcd5f1f3ff0ed3d362d6a96), [0700b92](https://github.com/ceph/ceph/commit/0700b9277260840a12013adbcad94b8be22c04b3), [b4c08aa](https://github.com/ceph/ceph/commit/b4c08aac9650d3914134fdfff727110aa002bb71), [995ba2c](https://github.com/ceph/ceph/commit/995ba2c4576f3de0ebfebccf9669d5162fab9fa6), [9a7c25e](https://github.com/ceph/ceph/commit/9a7c25e46ff1bb592fafb313401f0fe610840c54), [f4799e0](https://github.com/ceph/ceph/commit/f4799e046f335b5ba3833038da20952db5987499), [f34a60b](https://github.com/ceph/ceph/commit/f34a60b1db13c34913e443f7726f95acb53f3214), [db7502d](https://github.com/ceph/ceph/commit/db7502d37bc812f5ff7a986e9bf7b1f6b4e22881)
- Fixed an issue where SSL streams could not be reused after being closed, by adding a method to reset the stream.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [c7d1975](https://github.com/ceph/ceph/commit/c7d197520c383314de6091c888a26e575ce972d5), [4e1a805](https://github.com/ceph/ceph/commit/4e1a80584c4626c9dc31bbb66eb0ae0149732cab)
- Fixed a race condition in multi-site metadata log polling to avoid polling judgment errors by saving and comparing the previous tag value.
  ↳ [#60792](https://github.com/ceph/ceph/pull/60792): [b04d3cf](https://github.com/ceph/ceph/commit/b04d3cfb33e416846301264c36793409548374b3)
- Fix the insertion logic of osd_epochs in OSDMonitor::prepare_beacon to ensure that OSD only adds version information when it is marked in.
  ↳ [#55865](https://github.com/ceph/ceph/pull/55865): [d480ef5](https://github.com/ceph/ceph/commit/d480ef56d81d752f528db8f541e425285266d02d)
- Fixed an issue where when updating the entity keyring, the update is only triggered when the last permission needs to be updated.
  ↳ [#59672](https://github.com/ceph/ceph/pull/59672): [560f3cd](https://github.com/ceph/ceph/commit/560f3cdf26d021651612d4169a63f0db64dfa098)
- Modify BlueStore's _write_bdev_label function to support writing device labels at any disk location.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [02f4936](https://github.com/ceph/ceph/commit/02f493668ba60181ee49f21e7ea55e388e45aa2a)
- Fixed bugs in permission merging, data structure usage and request processing flow in MDS.
  ↳ [#59672](https://github.com/ceph/ceph/pull/59672): [2b96fdc](https://github.com/ceph/ceph/commit/2b96fdc8d5bbf12f68653dd8339fd0ec7fe616b8) | [#56887](https://github.com/ceph/ceph/pull/56887): [92e0ed9](https://github.com/ceph/ceph/commit/92e0ed912280688adf8a4c4ad77c8ad89efc5587), [ee77667](https://github.com/ceph/ceph/commit/ee77667211e9a18d60cc78d56079a89840b244ff) | [#57494](https://github.com/ceph/ceph/pull/57494): [3224385](https://github.com/ceph/ceph/commit/3224385086cbc94e7ba0fb60d46afe66aa64645b)
- Fixed bugs in device shutdown, batch commit and asynchronous I/O operations in the block device layer.
  ↳ [#58676](https://github.com/ceph/ceph/pull/58676): [8b519de](https://github.com/ceph/ceph/commit/8b519de87c7ce2030d2bfdaefe6f2cbceb047521), [fa775e2](https://github.com/ceph/ceph/commit/fa775e24cb5ff7511c62a45aabc71faed449b72c), [54d1a00](https://github.com/ceph/ceph/commit/54d1a00632e41a7ebbde30ac9ef1321ec9c4cf78)
- Fixed an issue where the CephFS mirror tool did not correctly update the peer status when the remote snapshot metadata was invalid.
  ↳ [#59406](https://github.com/ceph/ceph/pull/59406): [276dba8](https://github.com/ceph/ceph/commit/276dba8484324c4ad738eeec50db5a55b2e4be2e)
- Fixed the JSON output format of the dump function of ConnectionTracker and ConnectionReport to avoid duplicate keys.
  ↳ [#60003](https://github.com/ceph/ceph/pull/60003): [24693e3](https://github.com/ceph/ceph/commit/24693e3ad229b148af7232cd1cd8b1efc29c1c5d)
- Fixed a logic error in the upper limit check of OSD ancestors in OSD peering status calculation.
  ↳ [#59083](https://github.com/ceph/ceph/pull/59083): [4eedc6c](https://github.com/ceph/ceph/commit/4eedc6c9df6d406b4b929cae70478b29d65c66b1)
- Fixed the issue of monitor election being stuck in network partition scenarios to ensure that the cluster remains accessible during the partition.
  ↳ [#58669](https://github.com/ceph/ceph/pull/58669): [5d17185](https://github.com/ceph/ceph/commit/5d17185522a519d678ac2d0e1bb539908b1594ec)
- Fixed the issue of pg_upmap_primary mapping not being cleaned up after deleting the storage pool to ensure the correctness and consistency of cluster state management.
  ↳ [#58914](https://github.com/ceph/ceph/pull/58914): [d876992](https://github.com/ceph/ceph/commit/d87699238bac9f57f6fb22833848f94a447fd688)
- It is forbidden to remove the root_squash setting in the MDS authentication capability through the "fs authorize" command, only adding it is allowed.
  ↳ [#59672](https://github.com/ceph/ceph/pull/59672): [a8198ac](https://github.com/ceph/ceph/commit/a8198ace710f7ce0af6219df2674b226f87f4f87)
- Fix validation logic for MSR rules when setting require_min_compat_client to ensure client compatibility is correctly checked in Squid versions and above.
  ↳ [#59492](https://github.com/ceph/ceph/pull/59492): [f79b799](https://github.com/ceph/ceph/commit/f79b799b138b7658a501f97211d4b570c0e6fae0)
- Fixed possible numerical anomalies in the active connection counter in asynchronous messaging to prevent the counter from becoming negative.
  ↳ [#60447](https://github.com/ceph/ceph/pull/60447): [d6c225d](https://github.com/ceph/ceph/commit/d6c225d2b712b96f0e729cf18362cad5812077a0)
- Fix an issue in the _readdir_cache_cb function where freed memory may be used after the _getattr operation returns.
  ↳ [#58804](https://github.com/ceph/ceph/pull/58804): [f6e7c9f](https://github.com/ceph/ceph/commit/f6e7c9f04a55acb33f59de6f82cfb4b20fdb8a95)
- Fixed the issue where QuiesceDbManager did not obtain the request status before traversing members when calculating quiesce map.
  ↳ [#58912](https://github.com/ceph/ceph/pull/58912): [08d4596](https://github.com/ceph/ceph/commit/08d4596d130a07ff002506da409c59ad3d43a383)
- Fixed an issue caused by not marking the repaired location as a "good label" when repairing multiple block device labels, ensuring that this area is correctly excluded when saving the allocator state.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [cf4d671](https://github.com/ceph/ceph/commit/cf4d671836b9ba799b738d2c74d25775a2a2f8bd)
- Fixed the problem of not responding correctly to the bdev_enable_discard setting when configuration changes are made, and multiple problems when stopping discarding threads.
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [d58c5c8](https://github.com/ceph/ceph/commit/d58c5c861ab80583b6878e5bce759d64b1991561), [78a804c](https://github.com/ceph/ceph/commit/78a804ce8254d0dbfc6cef09d42b7ef528503ded)
- Fixed the null pointer error in the crimson::osd::scrub::evaluate_object_shard function and adjusted the logical order of object missing checks.
  ↳ [#58885](https://github.com/ceph/ceph/pull/58885): [4621d82](https://github.com/ceph/ceph/commit/4621d82ea59a9d46f03203102aca9d50a7866713)
- Fixed the problem that when starting the main recovery operation, the iteration was not advanced correctly after encountering an object not found, to avoid the recovery process being stuck.
  ↳ [#58958](https://github.com/ceph/ceph/pull/58958): [c986a9b](https://github.com/ceph/ceph/commit/c986a9b612596a8d9498919ffb86bba3a89d020a)
- Fixed the concurrency issue when accessing coll_map in AlienStore::stop method, ensuring that coll_map is traversed and cleared under lock protection.
  ↳ [#58841](https://github.com/ceph/ceph/pull/58841): [99ea3f6](https://github.com/ceph/ceph/commit/99ea3f65f3c1b40c1b1c295f7f213943326cbb55)
- Add exception handling to the NVMeBlockDevice::pass_through_io() function, record error logs and return input and output errors when the ioctl call fails.
  ↳ [#59298](https://github.com/ceph/ceph/pull/59298): [db2876c](https://github.com/ceph/ceph/commit/db2876c63337dfcd36632b0e9571a18bcda97644)
- Modify BlueStore's read_meta() function to first try to open a temporary block device for reading when the block device is not open, instead of immediately falling back to file-based values.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [35b835c](https://github.com/ceph/ceph/commit/35b835c082001f486411b7868fa3be1792c1d579)
- Fixed the transaction manager's handling of inconsistencies between backreferences and logical block addresses when cleaning up segments so that they are considered acceptable in certain concurrency scenarios.
  ↳ [#58837](https://github.com/ceph/ceph/pull/58837): [64ebf23](https://github.com/ceph/ceph/commit/64ebf230be61dd94531c728a6295af8ad20488c0)
- Verify that the connection is available before sending statistics to avoid problems caused by sending data when the connection is reset or empty.
  ↳ [#58887](https://github.com/ceph/ceph/pull/58887): [7de2bc5](https://github.com/ceph/ceph/commit/7de2bc553add0599ce388cc6ef5467ad08cb232b)
- Fixed the unit test infinite loop problem caused by the initialization of performance counters in the mClock scheduler.
  ↳ [#59035](https://github.com/ceph/ceph/pull/59035): [16f0e1f](https://github.com/ceph/ceph/commit/16f0e1f2301a66cac889e4aefdfcdbb56c730b9e)
- Fix the compilation problem when HAVE_LIBURING is not defined, and remove the redundant parameters in the ioring_queue_t::submit_batch function.
  ↳ [#58676](https://github.com/ceph/ceph/pull/58676): [1e0ee27](https://github.com/ceph/ceph/commit/1e0ee274192f850630980da75fb3d5f7be638d5f)
- Fixed the problem of incorrect authorization fixing of local locks when acquiring write locks to avoid unnecessary overhead.
  ↳ [#59097](https://github.com/ceph/ceph/pull/59097): [51dad2f](https://github.com/ceph/ceph/commit/51dad2fab17d3dea76b4b88c904b2f990a01d3fa)
- Fixed the resource leak that may occur when opening the source image during the migration process, and moved the closing operation to OpenSourceImageRequest for processing.
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [5423bcc](https://github.com/ceph/ceph/commit/5423bcccc96dbd20f5539a77a4e0186bf2e8f6e1)
- Fixed an issue where all PGs in a newly created pool start cleaning immediately regardless of the concurrency limit, now only operator-initiated cleanups are allowed to be exempt from the maximum number of cleanups limit.
  ↳ [#59020](https://github.com/ceph/ceph/pull/59020): [a3f1662](https://github.com/ceph/ceph/commit/a3f16627fde5426b19b932b9ef41c167e029d30f)
- Fixed the migration layer's handling of encrypted images in non-native formats to ensure correct handling of encrypted data when performing live migration from encrypted export.
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [8bd3063](https://github.com/ceph/ceph/commit/8bd3063197d21d145bd417b5d2074e2fe322eb3e)
- Fixed the issue that the discard_stop variable in the KernelDevice constructor was not initialized.
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [46d33cc](https://github.com/ceph/ceph/commit/46d33cc096f92bae7050feb1496a4bf1e05aac12)
- Fix the compiler warning that the visit() function in the rgw notification module may cause a dangling reference by returning a temporary string reference, and instead return a copy of the string.
  ↳ [#59226](https://github.com/ceph/ceph/pull/59226): [bdd78ac](https://github.com/ceph/ceph/commit/bdd78ac9a21eb3118cc7147d617815ebb3cbce73)
- Fixed the issue where the get_iam_policy_from_attr() function did not correctly distinguish buckets in different tenant namespaces during policy evaluation, ensuring that the IAM policy can correctly match the ARN containing tenant information.
  ↳ [#59221](https://github.com/ceph/ceph/pull/59221): [f850c30](https://github.com/ceph/ceph/commit/f850c30fe138177a7863d289fa2fcd044841b953)
- Fix missing JSON structure closing brackets in radosgw-admin notification JSON output, ensure notification filter's JSON format is correct.
  ↳ [#59302](https://github.com/ceph/ceph/pull/59302): [bc0d35f](https://github.com/ceph/ceph/commit/bc0d35fe8563c33643a742da70c49421a892459e)
- Fixed an issue where the HTTP manager background thread could access freed memory when calling finish_request() after logging an error.
  ↳ [#59439](https://github.com/ceph/ceph/pull/59439): [3486587](https://github.com/ceph/ceph/commit/3486587be853837ef096d6308404b313b6b14c77)
- Fixed the issue where the source bucket attributes were not loaded in the PutObj operation to ensure that the associated policies and permissions can be evaluated correctly.
  ↳ [#59413](https://github.com/ceph/ceph/pull/59413): [770bb39](https://github.com/ceph/ceph/commit/770bb39ace8862582fd62adadfaab1bf75b0cd51)
- Fixed the concurrency problem of client_lock not being held when calling _ll_fh_exists() in multiple functions on the client, ensuring that the file handle is properly locked before checking the validity.
  ↳ [#59487](https://github.com/ceph/ceph/pull/59487): [576f0e4](https://github.com/ceph/ceph/commit/576f0e40ca4bcc767134fce289b13ba12809cba7)
- Fixed an issue where qlen and qactive performance counters were not properly decremented when an error occurred during request processing.
  ↳ [#59670](https://github.com/ceph/ceph/pull/59670): [55f7798](https://github.com/ceph/ceph/commit/55f7798bb8d103f7f8b29b807060ef1817f8fb1f)
- Fixed an issue where rbd-mirror used the wrong ioctx when checking the namespace mirroring enablement status. Make sure to create a separate ioctx for each namespace for querying.
  ↳ [#59771](https://github.com/ceph/ceph/pull/59771): [ad5e3d6](https://github.com/ceph/ceph/commit/ad5e3d63749ba27c676928eda5e914821afdc74c)
- Fix the default behavior logic of realm and zone groups when creating and starting, ensuring that the default realm is only set when parameters are specified, and correctly falling back when the configuration is incomplete.
  ↳ [#59445](https://github.com/ceph/ceph/pull/59445): [e76f271](https://github.com/ceph/ceph/commit/e76f2718879b8d63faefbee99e4502cef214faff), [358a197](https://github.com/ceph/ceph/commit/358a197370b8ce527e28800246003d3e6c00027d)
- Fixed multiple issues in ceph-bluestore-tool and BlueStore related to block device tags, allocation mapping and database open processes.
  ↳ [#60335](https://github.com/ceph/ceph/pull/60335): [8835d07](https://github.com/ceph/ceph/commit/8835d07c235e141f26fead706dfb13a8f4d15f47) | [#59969](https://github.com/ceph/ceph/pull/59969): [950a060](https://github.com/ceph/ceph/commit/950a06076a080801491a4f4c793613d23124baa0) | [#60336](https://github.com/ceph/ceph/pull/60336): [7570b34](https://github.com/ceph/ceph/commit/7570b3423b472f109910bc05baf9864180856240)
- Fixed the segmentation fault caused by the empty bucket pointer in RGWPSListTopicsOp::execute(), and optimized the topic list logic.
  ↳ [#60774](https://github.com/ceph/ceph/pull/60774): [de3e443](https://github.com/ceph/ceph/commit/de3e443217557ab479155f30f16f8b9d2e9e6fa0)
- Fix RGWAccessKey::decode_json() incorrectly resetting the active field to false when it is not included in the JSON data.
  ↳ [#60823](https://github.com/ceph/ceph/pull/60823): [7c19709](https://github.com/ceph/ceph/commit/7c197094b004e281030db421f20e2336edec9234)
- Fixed an issue where flatten operation may cause data corruption when object mapping is inconsistent.
  ↳ [#61168](https://github.com/ceph/ceph/pull/61168): [5d5ea4e](https://github.com/ceph/ceph/commit/5d5ea4e159612728db441072bec62599b9aa534a)
- Remove redundant socket closing calls in resolve_host() and add assertions in connect() to ensure socket status.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [aac2046](https://github.com/ceph/ceph/commit/aac2046e88b55513ae90c90c3fec4eee1f1961e8)
- Fixed an issue where disconnect() was incorrectly called when HttpClient handshake failed.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [1e66e09](https://github.com/ceph/ceph/commit/1e66e09e0f6c0cb3ed3de8ad3d98d61d7bf2a8d8)
- Fixed SSL handshake error handling, passing the error code directly to the handle_handshake function.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [17b35b3](https://github.com/ceph/ceph/commit/17b35b3d3c87f166d41bf0887df0b9acbc2712fc)
- Ignore stream_truncated errors when closing SSL connections to avoid false positive failures.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [2c48503](https://github.com/ceph/ceph/commit/2c485039deba81ecb231b2685411f7a475dab4fe)
- Fixed an issue where HttpClient may trigger assertions during shutdown.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [1fd1bd6](https://github.com/ceph/ceph/commit/1fd1bd600f446a307028d024a32c855695ece3a5)
- Fixed an issue where HttpClient did not close the socket correctly during certain state transitions.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [03e08b0](https://github.com/ceph/ceph/commit/03e08b0e6237dfc50238d9cb256c45d21e041f9c)
- Fixed the issue where the --group-namespace and --image-namespace options in the rbd group command were not recognized correctly.
  ↳ [#61172](https://github.com/ceph/ceph/pull/61172): [5a5f0f0](https://github.com/ceph/ceph/commit/5a5f0f03aa59682c1d69828f8ac90045da42b809)
- Fixed an issue where the rgw_list_pool function may crash due to an exception during pool enumeration iteration.
  ↳ [#61667](https://github.com/ceph/ceph/pull/61667): [110da90](https://github.com/ceph/ceph/commit/110da90012cb8cfaf9f68bed421b19f0bc35ab9c)
- Fix the epoch value used by interrupt conditions in background recovery operations.
  ↳ [#58839](https://github.com/ceph/ceph/pull/58839): [61ecaee](https://github.com/ceph/ceph/commit/61ecaee487b78d80e7e9d351e8fb9c9c08807d9b)
- Fixed the memory management problem of mismatch between new[] and delete[] in the read_bdev_label function in BlueStore.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [9aa72c9](https://github.com/ceph/ceph/commit/9aa72c90a425524ee87a8231ecd1c12d5d4f6ee2)
- Fixed the problem that the random number seed in the rbd bench command was not initialized correctly.
  ↳ [#59502](https://github.com/ceph/ceph/pull/59502): [07dc1c5](https://github.com/ceph/ceph/commit/07dc1c5534224797bb38799b8e9d43327a12d00a)
- Fixed the memory management issue of completion pointer in RGW notification.
  ↳ [#59671](https://github.com/ceph/ceph/pull/59671): [cf6b046](https://github.com/ceph/ceph/commit/cf6b046248bdd3dfa18632c7b5d1f446662aa210)
- Fixed the parsing problem of --yes-i-really-really-mean-it option in ceph-bluestore-tool.
  ↳ [#59967](https://github.com/ceph/ceph/pull/59967): [bc0f089](https://github.com/ceph/ceph/commit/bc0f0897ce1d1451258d6c32b6ca80361cfe1cc7)
- Restore sync duration timing units in cephfs_mirror from milliseconds to seconds.
  ↳ [#59406](https://github.com/ceph/ceph/pull/59406): [886ed93](https://github.com/ceph/ceph/commit/886ed935051a65a7b5d217e861c55d8ff72127d1)
- In the global_init function, replace the stack buffer with a buffer allocated on the heap to fix potential buffer overflow issues.
  ↳ [#60127](https://github.com/ceph/ceph/pull/60127): [a039bc5](https://github.com/ceph/ceph/commit/a039bc5101a029db8a80253288c8ec8d98070069)
- Fixed the issue where the lifecycle policy does not take effect when bucket version control is suspended.
  ↳ [#61138](https://github.com/ceph/ceph/pull/61138): [5e43fa1](https://github.com/ceph/ceph/commit/5e43fa1baf415a9fbe91a89ae647d51851914801)
- Removed bluestore_debug_prefill, an outdated and useless debugging configuration item.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [b50fd4e](https://github.com/ceph/ceph/commit/b50fd4ec6c5f000896ec05f040d2f4804d0f6abc)
- Fixed the issue of missing dpp parameter in debug statements in object_context_loader.
  ↳ [#58905](https://github.com/ceph/ceph/pull/58905): [8d8bcd9](https://github.com/ceph/ceph/commit/8d8bcd9f87304cfbb6017e2292233104c1e5f60d)
- In the SeaStore statistical report, a record of the pending IO details of each shard has been added.
  ↳ [#58835](https://github.com/ceph/ceph/pull/58835): [9e25855](https://github.com/ceph/ceph/commit/9e25855f476f27c18445ff162126831ba531b056)

### Refactoring optimization
- Reconstructed BlueStore's block device tag reading and writing logic to directly operate BlockDevice objects and support multi-tag reading and writing on the main block device.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [abca1e8](https://github.com/ceph/ceph/commit/abca1e8fb2199d175046c0dbae0f98ad5a98ebab), [2814180](https://github.com/ceph/ceph/commit/2814180c2b287d0b415e4d5a38f6a461988b8862), [ad9571a](https://github.com/ceph/ceph/commit/ad9571aa839d7d423412e4571fa8517ba628f8b6), [a872a87](https://github.com/ceph/ceph/commit/a872a87a2caba1de302599aa8606d12a83ab1a41), [675d39d](https://github.com/ceph/ceph/commit/675d39d1dbfe4714847156c385dd858ac64be1ee)
- Optimized the discard queue processing logic when BlueStore is closed, distinguishing graceful shutdown and fast shutdown scenarios, and limiting the thread private queue size.
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [d65eebc](https://github.com/ceph/ceph/commit/d65eebc478d0a9bd366f3b5cc38fb4c84aa00dc8), [1f0031e](https://github.com/ceph/ceph/commit/1f0031e52dce525dae6769bd4dee381f35aac397)
- Refactored the logic related to OSD status and epoch management in OSDMonitor, including renaming public methods and fixing their internal implementation.
  ↳ [#55865](https://github.com/ceph/ceph/pull/55865): [08fd2e7](https://github.com/ceph/ceph/commit/08fd2e7a5d941dd2b8652e17d5801e29cda4b421), [ac7793e](https://github.com/ceph/ceph/commit/ac7793ebe2ad023f16fad2707581fd8c34d45ca6)
- Optimized the discard thread management logic of the kernel device (KernelDevice), including adjusting the upper limit of the number of discards, unified start/stop/configuration change processing, and simplifying the discard queue processing process during fast shutdown.
  ↳ [#59065](https://github.com/ceph/ceph/pull/59065): [c3dc1c4](https://github.com/ceph/ceph/commit/c3dc1c4f1b3d048fd3409b0bbc69ee81638298be), [aa601fc](https://github.com/ceph/ceph/commit/aa601fcdc213eda276b82dda16096656d37185e9)
- Optimized the LBA mapping allocation process of the Seastore engine, allowing allocation of non-contiguous sections, and implemented batch allocation of mapping information to improve performance.
  ↳ [#58820](https://github.com/ceph/ceph/pull/58820): [a637390](https://github.com/ceph/ceph/commit/a637390b0456d423197754f469d9e5a1d342c4d6), [3621649](https://github.com/ceph/ceph/commit/36216493f69d5721de86c24c9b25b99e47f8a38e) | [#58828](https://github.com/ceph/ceph/pull/58828): [4d3ed5d](https://github.com/ceph/ceph/commit/4d3ed5de7962ce56f127249ff3f78636187a2dd8)
- Reconstructed the loading and locking mechanism of the object context (ObjectContext), introduced a new loading method, removed the lock promotion function, simplified the lock interface of tri_mutex, and adjusted the constructor parameter type.
  ↳ [#58905](https://github.com/ceph/ceph/pull/58905): [d315d67](https://github.com/ceph/ceph/commit/d315d6756ea7d773fa7d1c377a3e8f2ac573f470), [1eed640](https://github.com/ceph/ceph/commit/1eed640afaa2c6b0f1b2b6ba5655b485f6303b8e), [a31aa9a](https://github.com/ceph/ceph/commit/a31aa9ac05f8fbc73d44c0995077708b98e82c83), [7b067b9](https://github.com/ceph/ceph/commit/7b067b93792de82077f26bd617c49dbbc6c54c28), [9452d5e](https://github.com/ceph/ceph/commit/9452d5e68b1ae828dd1df8fd65a5366d900ca23f), [ecb6c0d](https://github.com/ceph/ceph/commit/ecb6c0dc60935473e9de3234c8126129b4f55434), [a175904](https://github.com/ceph/ceph/commit/a17590486e11063a1db90aaca591792d6b9dbfe7), [92e8e2d](https://github.com/ceph/ceph/commit/92e8e2d4ee52a6d86369d0df17be94e51db54c8f)
- Reconstructed the collection management logic of AlienStore, extracted an independent collection reference acquisition method and added lock protection. At the same time, the collection mapping operation was moved to the thread pool for execution to improve concurrency security.
  ↳ [#58841](https://github.com/ceph/ceph/pull/58841): [3171945](https://github.com/ceph/ceph/commit/3171945115aca6e093618cb6b74d57d0ad822b31), [0a3c02b](https://github.com/ceph/ceph/commit/0a3c02b847ee0994af3b09eed3a6a87773a42824)
- Reconstruct the listening loop of the RGW Beast front-end into a cancelable coroutine, and automatically retry when encountering resource limit errors, while optimizing the cancellation signal processing when stopping and pausing.
  ↳ [#60244](https://github.com/ceph/ceph/pull/60244): [fb32cb8](https://github.com/ceph/ceph/commit/fb32cb833117bf5bc73f0e4b2dd4ab2888232609)
- Optimized the management logic of discarded threads in the kernel device, ensuring the order of resource release by using join() to wait for the thread to end, thereby avoiding potential race conditions.
  ↳ [#60616](https://github.com/ceph/ceph/pull/60616): [64e7e33](https://github.com/ceph/ceph/commit/64e7e3302db4d3d7ac31d9466ad16eb91dcf5532)
- Refactored Kafka topic creation logic, used unique_ptr to manage topic object memory, and removed dependence on rd_kafka_topic_name().
  ↳ [#59754](https://github.com/ceph/ceph/pull/59754): [9f8c1d6](https://github.com/ceph/ceph/commit/9f8c1d60a5c15844121b91719d3a365a767b7b2a)
- Fixed an issue in the RGW PubSub module where waiters were not properly unlocked before suspending.
  ↳ [#60133](https://github.com/ceph/ceph/pull/60133): [1dfa333](https://github.com/ceph/ceph/commit/1dfa3331cc7f0eb42de037bf001b5f4edae59356)
- Fixed the epoch used for interrupts in multiple OSD operations to ensure the correct epoch is used when the operation is scheduled.
  ↳ [#58839](https://github.com/ceph/ceph/pull/58839): [d36c9f7](https://github.com/ceph/ceph/commit/d36c9f797fdc86017f3c551aec432895a684982f), [5dfb1ac](https://github.com/ceph/ceph/commit/5dfb1acef200b4642112239ed1e1bdc7af95833a), [35e9e7e](https://github.com/ceph/ceph/commit/35e9e7edc8ad3bdba86f21b965bbef6800bcaa71)
- Optimized the parameter passing of the C_ImageReadRequest constructor in librbd to avoid unnecessary copying of image_extents.
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [950253e](https://github.com/ceph/ceph/commit/950253ef90686b40e2ba691d9516ecb5ba5700f3)
- Removed code related to multistream functionality in NVMe block devices and marked multistream support as a backlog.
  ↳ [#59298](https://github.com/ceph/ceph/pull/59298): [d66d23d](https://github.com/ceph/ceph/commit/d66d23da188f18058ec944bd0e61534f59e4a2c4)
- Replaced the random block manager's metadata header type rbm_metadata_header_t with rbm_superblock_t, and updated the read and write function names and related tests accordingly.
  ↳ [#59298](https://github.com/ceph/ceph/pull/59298): [36acb05](https://github.com/ceph/ceph/commit/36acb0598cfdcd1ecaf77a16890715e69ff7ccc7)
- Removed the waiter_name field of the waiter_t structure in tri_mutex, and simplified the related log output.
  ↳ [#58905](https://github.com/ceph/ceph/pull/58905): [10b0b92](https://github.com/ceph/ceph/commit/10b0b92cecd0b73c9399d95ec176e1ebc22fd1b6)
- Improved seastore statistical reporting, calculating averages and removing redundant per-shard data.
  ↳ [#58835](https://github.com/ceph/ceph/pull/58835): [a8fda95](https://github.com/ceph/ceph/commit/a8fda95ebafa186f940668a154525c779fc5f542)
- Replaced the deprecated get0 and unsafe_get0 method calls in the crimson code base with get and unsafe_get, and removed the definition of the unsafe_get0 method.
  ↳ [#58955](https://github.com/ceph/ceph/pull/58955): [da923da](https://github.com/ceph/ceph/commit/da923da751c3c67b4f38955889ae1ba6d1c43afd)
- Cleaned up redundant code in librbd Migration::prepare_import(), removed useless code blocks and unused variables after the return statement.
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [8a9cf5d](https://github.com/ceph/ceph/commit/8a9cf5da50f7982ea7cac51ce6993019e2ae0362)
- Removed unnecessary ImageState.h header file inclusion in the migration format implementation file.
  ↳ [#59661](https://github.com/ceph/ceph/pull/59661): [f66dbf2](https://github.com/ceph/ceph/commit/f66dbf21f8abc67fef4e08b3c609a74ead1ee66c)
- The asynchronous lock implementation of SharedMutex uses async_initiate for initialization instead.
  ↳ [#60133](https://github.com/ceph/ceph/pull/60133): [0169522](https://github.com/ceph/ceph/commit/0169522c7f842717ff9f4acf64a3acfdb1651a2b)
- Rename PhysicalNodeMapping::is_parent_valid() to is_parent_viewable(), and add a new is_parent_valid() method to distinguish the validity and visibility checks of parent nodes.
  ↳ [#58957](https://github.com/ceph/ceph/pull/58957): [b5414ed](https://github.com/ceph/ceph/commit/b5414ed1060178e357917ea4555d0851ef5b093b)
- Renamed the OpenSourceImageRequest constructor and create static factory method parameter io_ctx to dst_io_ctx to more clearly represent its purpose as a target I/O context.
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [32a9595](https://github.com/ceph/ceph/commit/32a9595413f3ce49649d94d8b6d6e8bbbc957128)
- Extract the pruning logic in prune_parent_extents() into an independent prune_extents() utility function to improve code reusability.
  ↳ [#59661](https://github.com/ceph/ceph/pull/59661): [6953807](https://github.com/ceph/ceph/commit/69538072a876cf6341fd8c2aa4bb7dd6eed12596)
- Removed the deprecated cls_remote_reads test class and its related test cases.
  ↳ [#57819](https://github.com/ceph/ceph/pull/57819): [b3d1716](https://github.com/ceph/ceph/commit/b3d17162c5e80ec1725998337bbe875e65c1964d)

### Test related
- Added new test cases for store_test, including verification of large extent object reads and simplified readv tests.
  ↳ [#58676](https://github.com/ceph/ceph/pull/58676): [2878491](https://github.com/ceph/ceph/commit/28784916cad1498ccb48dd46d00356e1d4e202f2), [c8b5a43](https://github.com/ceph/ceph/commit/c8b5a430e36cfb82b33eca71908989c5b174dfc4)
- Added fsck checks in multiple test cases of store_test to verify the repair effect, and removed some unnecessary mount() calls.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [e48be4f](https://github.com/ceph/ceph/commit/e48be4f1f53e17375655f103b0bbd51cba6e4700)
- Removed the deprecated RemoteReads class test case to solve problems caused by referencing non-existing files.
  ↳ [#58144](https://github.com/ceph/ceph/pull/58144): [f5de2ff](https://github.com/ceph/ceph/commit/f5de2ff5ebc474120fa0077e866962dca5dcd02f)
- Added test case TestInternal.FlattenInconsistentObjectMap, used to verify the correctness of performing flatten operation when there is inconsistency in object mapping.
  ↳ [#61168](https://github.com/ceph/ceph/pull/61168): [efb8f29](https://github.com/ceph/ceph/commit/efb8f295a9fbbc04dd3efd896277e5c7d0df18b1)

### Performance optimization
- Optimize BlueStore metadata operations by caching bdev_label to avoid repeated reading to improve efficiency.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [38ba41e](https://github.com/ceph/ceph/commit/38ba41ebfb3519fcde3095a37a75fb7f2f53c2b5)
- Optimize the bluefs_transaction_t::bound_encode method to simplify buffer size estimation and skip useless calculations.
  ↳ [#59217](https://github.com/ceph/ceph/pull/59217): [132a641](https://github.com/ceph/ceph/commit/132a6414394d01c4adb4a1ad2f5b225ee201be61)
- Added performance counters to RocksDBStore to track compression operations.
  ↳ [#58740](https://github.com/ceph/ceph/pull/58740): [84be701](https://github.com/ceph/ceph/commit/84be701271f341e4019ea2f08db80eceddd975ef)
- Add queue length performance counter for mClock scheduler.
  ↳ [#59035](https://github.com/ceph/ceph/pull/59035): [097c434](https://github.com/ceph/ceph/commit/097c434fedb0b71d79183cdfc10c29e944d46827)
- Optimize the insertion logic of the message distributor to avoid sorting after each insertion and solve potential memory warnings.
  ↳ [#58991](https://github.com/ceph/ceph/pull/58991): [dcac0d0](https://github.com/ceph/ceph/commit/dcac0d0927a26756ba4144c8e0b37226e1ff63fe)
- Optimize the accept behavior of the RGW Beast front-end when monitoring errors occur, and introduce a backoff retry mechanism to improve service stability.
  ↳ [#60244](https://github.com/ceph/ceph/pull/60244): [29a9975](https://github.com/ceph/ceph/commit/29a9975aeda891d538b6621e0c2d963933e37e66)
- Lower the default block size for deep cleans to reduce the impact on client operation latency.
  ↳ [#59791](https://github.com/ceph/ceph/pull/59791): [0841603](https://github.com/ceph/ceph/commit/0841603023ba53923a986f2fb96ab7105630c9d3)
- Fallback to the last valid value when measured OSD IOPS values are unrealistically low, and introduce a new low threshold configuration option.
  ↳ [#60660](https://github.com/ceph/ceph/pull/60660): [bca9920](https://github.com/ceph/ceph/commit/bca9920b003f5dd1bdb431ac76071756dc008ee1)
- Optimize bucket list operations, skip contiguous areas to improve performance when there is no need to list namespace entries.
  ↳ [#61070](https://github.com/ceph/ceph/pull/61070): [8f8cc9a](https://github.com/ceph/ceph/commit/8f8cc9a57b17621cdaec2c8a995f5850b362dc52)

### Security related
- Fixed the heap buffer overflow problem of the sb_info_space_efficient_map_t::find method in bluestore, and improved the security of the core storage engine.
  ↳ [#58816](https://github.com/ceph/ceph/pull/58816): [262e1ad](https://github.com/ceph/ceph/commit/262e1ad2e82dcb657b858c9bda6b6e03e55ae12a)
- Fixed the issue in RawFormat::list_snaps() that the snapshot range was not clipped to prevent out-of-bounds reads from occurring when importing snapshots of different sizes.
  ↳ [#59661](https://github.com/ceph/ceph/pull/59661): [bf584c2](https://github.com/ceph/ceph/commit/bf584c2c94065fa4c5f77e9a30a81d4fcfbdfeb3)
- Fixed an issue where the user statistics reset operation still returned tokens when the response was not truncated to avoid errors caused by the response data exceeding the 64-byte limit.
  ↳ [#60164](https://github.com/ceph/ceph/pull/60164): [8bf6a70](https://github.com/ceph/ceph/commit/8bf6a70b0b704cebc00a1832a773d192d3cb6390)
- Fixed the problem of encrypted format processing of the migration source image, so that the format can be automatically cloned during the migration preparation stage without the need for the user to manually specify it.
  ↳ [#60171](https://github.com/ceph/ceph/pull/60171): [7196790](https://github.com/ceph/ceph/commit/7196790b998cb21cff064cea965dc5aa953036a1)

### Documentation
- Added detailed comments to key data structures and methods in the crimson module, improving code readability and maintainability.
  ↳ [#58839](https://github.com/ceph/ceph/pull/58839): [da8f89b](https://github.com/ceph/ceph/commit/da8f89b914d636b910bcc432abf899d738752f73) | [#58841](https://github.com/ceph/ceph/pull/58841): [5751fe8](https://github.com/ceph/ceph/commit/5751fe8f2d5f0a182f17c6e07b85dc79dcb635a4)
- Improved the text description in the CephFS cache configuration documentation section about handling cache pressure warnings, and added instructions for handling the "Client failed to respond to cache pressure" message.
  ↳ [#59214](https://github.com/ceph/ceph/pull/59214): [a19e52b](https://github.com/ceph/ceph/commit/a19e52bf52df926747ab4ac65c251b018df0a0a1) | [#59148](https://github.com/ceph/ceph/pull/59148): [f8a0aab](https://github.com/ceph/ceph/commit/f8a0aab8cdbf0b4ff9270ac8e23869e159001291)
- Added basic definitions of "object storage" and "ceph-ansible" to the glossary.
  ↳ [#59424](https://github.com/ceph/ceph/pull/59424): [dc20d6e](https://github.com/ceph/ceph/commit/dc20d6ec76ced2e819257be45c3c90346bda7d43) | [#59007](https://github.com/ceph/ceph/pull/59007): [b355f4e](https://github.com/ceph/ceph/commit/b355f4e61f9b3642a611b397b808e4f49b135d9d)
- Added step-by-step instructions on how to activate the latest release version on Read the Docs in the "First Stable Release" checklist of the developer documentation.
  ↳ [#59654](https://github.com/ceph/ceph/pull/59654): [9bef7d4](https://github.com/ceph/ceph/commit/9bef7d48744fac309db500c98d7f39dbc03a535b)
- Updated the command format in the "Building Ceph" section of README.md so that it can be copied with a single mouse click.
  ↳ [#59834](https://github.com/ceph/ceph/pull/59834): [f37285f](https://github.com/ceph/ceph/commit/f37285f3ea33ad78a829886610dfeb29ccc4dc80)
- In the release checklist, mark "Activate ReadTheDocs for Squid versions" as completed.
  ↳ [#59812](https://github.com/ceph/ceph/pull/59812): [1fa7990](https://github.com/ceph/ceph/commit/1fa7990eb67a18d0534185bdfbf4836e60eedb6b)
- In the health-checks document, the reference format of multiple configuration parameters was updated from plain text to the confval instruction format, which improved the standardization and readability of the document.
  ↳ [#59871](https://github.com/ceph/ceph/pull/59871): [8c61104](https://github.com/ceph/ceph/commit/8c611041553fb8ced4c81a7a802eea7d6f43f7cc)
- Updated the "Getting Started" link in the documentation to point to the "Start" page instead of the "Installation" page.
  ↳ [#59907](https://github.com/ceph/ceph/pull/59907): [c9ccab5](https://github.com/ceph/ceph/commit/c9ccab55f8d0f80c90c133a2d2648d7f38f342f0)
- Updated Zac Dover's email address in governance documentation.
  ↳ [#60134](https://github.com/ceph/ceph/pull/60134): [0a68fc5](https://github.com/ceph/ceph/commit/0a68fc50aebc17f253b6ed150c765d0953209975)
- Added comments for the get_min_last_epoch_clean function and its related member variables in OSDMonitor.
  ↳ [#55865](https://github.com/ceph/ceph/pull/55865): [66a559c](https://github.com/ceph/ceph/commit/66a559c28c9b8cf66efc4f9e0607641821b89b02)
- Updated the CephFS mirroring function document, added performance indicator descriptions and configuration items, and explained that manually creating snapshots on the remote file system will cause synchronization failure and read-only restrictions.
  ↳ [#59070](https://github.com/ceph/ceph/pull/59070): [eff5d2c](https://github.com/ceph/ceph/commit/eff5d2c4d65a02e01d3ffefbdab7fc896bf10155) | [#59406](https://github.com/ceph/ceph/pull/59406): [0ed8dbe](https://github.com/ceph/ceph/commit/0ed8dbeaa3c7b89ae0556f4623541c04ffc06eab)
- Updated the restful module documentation and added instructions on how to configure the maximum request size (max_requests).
  ↳ [#59372](https://github.com/ceph/ceph/pull/59372): [b1fba19](https://github.com/ceph/ceph/commit/b1fba19b71d68d13c2f6fcb15b09dc607615ff2b)
- Added documentation for stretch pool's set, unset and show commands for RADOS pools, and updated stretch-mode documentation to introduce the concept of independent stretch pools.
  ↳ [#59084](https://github.com/ceph/ceph/pull/59084): [cc66f62](https://github.com/ceph/ceph/commit/cc66f62bd06ebbd9e173af1f465e588d53539059) | [#59099](https://github.com/ceph/ceph/pull/59099): [8539ac9](https://github.com/ceph/ceph/commit/8539ac90e6006a743eb6a401cd124530603fb8f0)
- Updated the QAT acceleration document and added QATlib related information, including its download address, system requirements and installation configuration instructions.
  ↳ [#58874](https://github.com/ceph/ceph/pull/58874): [b8f764f](https://github.com/ceph/ceph/commit/b8f764fdbb558e229280b0517f801d6bde9fb2e2)
- Added instructions to the CephFS documentation on how to disable the mgr/volumes plugin, and added guidance to the troubleshooting section.
  ↳ [#60496](https://github.com/ceph/ceph/pull/60496): [8868ecc](https://github.com/ceph/ceph/commit/8868ecc6ce70603986c0c59a6cc0d3d695dbecaa)
- Updated documentation to state that when repairing file system corruption, scrub will automatically clear the repaired entries from the corruption table.
  ↳ [#59078](https://github.com/ceph/ceph/pull/59078): [643c298](https://github.com/ceph/ceph/commit/643c298e0dd1208eb4a3d84486d8db3240a5ed7a)
- Updated the documentation on the behavior when the persistent notification queue is full to explain that when the notification endpoint is unavailable for a long time and the persistent storage fills up, the triggering operation will return a 503 error.
  ↳ [#59233](https://github.com/ceph/ceph/pull/59233): [3c3d0e7](https://github.com/ceph/ceph/commit/3c3d0e7a161128bb4ff2f417e26eb9ee708ce495)
- Added "Flapping OSD" entry to the glossary, and added corresponding cross-references.
  ↳ [#60864](https://github.com/ceph/ceph/pull/60864): [ef1dfd9](https://github.com/ceph/ceph/commit/ef1dfd9fbcdca7d2f980be6f1eb5b4bcb2a58032)
- Added troubleshooting documentation for object not found issues in cache tiering scenarios, explaining how to handle such situations when restarting the OSD.
  ↳ [#59380](https://github.com/ceph/ceph/pull/59380): [d8acf1b](https://github.com/ceph/ceph/commit/d8acf1b6ee6c2b75991360bf057de6ec6977596b)
- Added a new section "Migrating Notification Topics" to the "Migrating Existing Users to Accounts" documentation section, detailing how to handle notification topics after migration.
  ↳ [#59491](https://github.com/ceph/ceph/pull/59491): [f93d9b6](https://github.com/ceph/ceph/commit/f93d9b605ca4c783fc5590e67f5e4ac612072db3)
- Added instructions on how to obtain the exact size of a block device, including command examples and calculation methods, in the cephadm OSD documentation.
  ↳ [#59430](https://github.com/ceph/ceph/pull/59430): [e301fcb](https://github.com/ceph/ceph/commit/e301fcb29f67ebf05875b5d5d20fe74bf0e919b4)
- Updated documentation to add configuration instructions for mounting cache directories as volumes for containerized deployments.
  ↳ [#59767](https://github.com/ceph/ceph/pull/59767): [4c6fa44](https://github.com/ceph/ceph/commit/4c6fa44cc77cd777608fe965a9d7462cc4ec094f)
- Updated the documentation for CephFS NFS export, added a description of the --cmount_path parameter, and updated related JSON examples.
  ↳ [#59896](https://github.com/ceph/ceph/pull/59896): [07ef567](https://github.com/ceph/ceph/commit/07ef56781cce43bbc1c382b8596de3c1312d0f4b)
- Clarified the description of rbd related commands (including rename, mirror pool commands), and clearly stated their scope and limitations.
  ↳ [#59602](https://github.com/ceph/ceph/pull/59602): [b74f65f](https://github.com/ceph/ceph/commit/b74f65fbb0108362bc0c383b9308edffca45a82b), [e42bbd6](https://github.com/ceph/ceph/commit/e42bbd6bdc401797104edd5c97081180a54e2f29) | [#60269](https://github.com/ceph/ceph/pull/60269): [e3290d3](https://github.com/ceph/ceph/commit/e3290d3589034efd36089c80212b3fdbf642edcf)
- Marked the Squid version as stable and updated the related release checklist document.
  ↳ [#59537](https://github.com/ceph/ceph/pull/59537): [7f0eea2](https://github.com/ceph/ceph/commit/7f0eea2b3d39876252ac6e1793dbd871fcf8ff2a)
- Added steps to migrate BlueFS data from slow devices back to fast devices in the ceph-volume documentation.
  ↳ [#59540](https://github.com/ceph/ceph/pull/59540): [733b4be](https://github.com/ceph/ceph/commit/733b4be60a2d8b4eec688cdd784b2ab56bf5494f)
- Improved description of QoS, D4N and topic persistence settings in the RADOS gateway configuration reference documentation.
  ↳ [#59578](https://github.com/ceph/ceph/pull/59578): [ba67155](https://github.com/ceph/ceph/commit/ba67155fad81d1d83bedaf8bbdff755487fa58e3)
- Updated Teuthology integration testing workflow documentation, added an infrastructure chapter and adjusted the content structure.
  ↳ [#59548](https://github.com/ceph/ceph/pull/59548): [211513f](https://github.com/ceph/ceph/commit/211513fd4021c50884e12b722294aa5715b5f5af)
- Improved the wording and description of multiple health check descriptions in the health-checks.rst document.
  ↳ [#59582](https://github.com/ceph/ceph/pull/59582): [8ff3985](https://github.com/ceph/ceph/commit/8ff3985a9c20068c90fc980bb91409508e715531)
- Improved wording in MDS documentation regarding multi-active MDS versus single overloaded MDS.
  ↳ [#59585](https://github.com/ceph/ceph/pull/59585): [90bba4a](https://github.com/ceph/ceph/commit/90bba4a6bb188a5c4cc1f5921789cbe3bac7e829)
- Added instructions and handling steps for the "X PGs not deep-scrubbed in time" health warning in the documentation.
  ↳ [#59733](https://github.com/ceph/ceph/pull/59733): [da7e333](https://github.com/ceph/ceph/commit/da7e33323cb4a254ca6f2debcb0ef2b53b5dc949)
- Added instructions to the cephadm upgrade documentation for removing malformed JSON that caused module startup failure.
  ↳ [#59663](https://github.com/ceph/ceph/pull/59663): [78c8df8](https://github.com/ceph/ceph/commit/78c8df84dec6ff3f4d229a51b23a972f0ed2e739)
- Updated ceph-bluestore-tool documentation, added instructions for bluefs-bdev-migrate operations and corrected syntax.
  ↳ [#59682](https://github.com/ceph/ceph/pull/59682): [d1687a6](https://github.com/ceph/ceph/commit/d1687a6fc446e2d1876ae97fe5ed87034d2a0b1b)
- Added description about Docker Live Restore function in cephadm installation documentation.
  ↳ [#59933](https://github.com/ceph/ceph/pull/59933): [f882fa8](https://github.com/ceph/ceph/commit/f882fa82fa1bac9d1c8743e2b0d2f654cf9afbb7)
- Added zap-device command documentation and updated show-label command description for ceph-bluestore-tool.
  ↳ [#59967](https://github.com/ceph/ceph/pull/59967): [b505035](https://github.com/ceph/ceph/commit/b5050352a3f69ed4667dfa1b4eee571d10b82325)
- Corrected the command to create RADOSGW user in the installation document so that its user name is consistent with the node name.
  ↳ [#59756](https://github.com/ceph/ceph/pull/59756): [d266bd4](https://github.com/ceph/ceph/commit/d266bd4630fcf7aa7af9a01fd64be45fc39213f5)
- Added a second way to set osd_deep_scrub_interval in the documentation to resolve specific warnings.
  ↳ [#59802](https://github.com/ceph/ceph/pull/59802): [1d02e2d](https://github.com/ceph/ceph/commit/1d02e2d2649e72e93c91f9fc9aad484a7e59bee5)
- Added earmark option description for subvolumes and added related command documentation.
  ↳ [#59894](https://github.com/ceph/ceph/pull/59894): [5055a3c](https://github.com/ceph/ceph/commit/5055a3c5f681797da53874f18cb9dbfccf52ba50)
- Corrected the synchronization duration unit in the documentation from milliseconds to seconds, and updated the example values.
  ↳ [#59406](https://github.com/ceph/ceph/pull/59406): [74d062b](https://github.com/ceph/ceph/commit/74d062b3c17a450a4366f1b8e47c9039bea698d6)
- Added documentation for Windows CI jobs, describing its execution steps and common problems.
  ↳ [#60033](https://github.com/ceph/ceph/pull/60033): [fd1291e](https://github.com/ceph/ceph/commit/fd1291e73c93b0924b1147208e1143dbf695c3ef)
- Added a description of the Ceph Executive Committee's responsibilities to the governance documentation.
  ↳ [#60139](https://github.com/ceph/ceph/pull/60139): [c2d016f](https://github.com/ceph/ceph/commit/c2d016f2e28a1372828e59dd7f1edc2c282f3081)
- Removed mention of the "stable releases and rollbacks" team from the developer guide, and updated the rollback process instructions.
  ↳ [#60272](https://github.com/ceph/ceph/pull/60272): [1747b00](https://github.com/ceph/ceph/commit/1747b00eed2a1f7e912251ecb5401c29ca8e69e9)
- Updated description and link to the snapshot diffing feature in the cephfs-mirroring documentation.
  ↳ [#60343](https://github.com/ceph/ceph/pull/60343): [099cb60](https://github.com/ceph/ceph/commit/099cb6012100fdc2ad1fd1d6d23b0e6645c47d05)
- Fixed the Samba container example command in the cephadm documentation and completed the missing command prefix.
  ↳ [#60432](https://github.com/ceph/ceph/pull/60432): [a160ef5](https://github.com/ceph/ceph/commit/a160ef5feea021a557fe2fc01ab83f6cfe172b4f)
- Added a new entry for PLP in the glossary and explained its technical principles.
  ↳ [#60503](https://github.com/ceph/ceph/pull/60503): [8252a0d](https://github.com/ceph/ceph/commit/8252a0d3235fd4ec8650580ab0e8d4d05494f718)
- Unified the mark format of "clean" status in documents.
  ↳ [#60500](https://github.com/ceph/ceph/pull/60500): [cb7f77c](https://github.com/ceph/ceph/commit/cb7f77c3cd64c628c41fb63a47daf1eaff09ff3f)
- Added installation and configuration steps for vstart cluster in Beginner's Guide.
  ↳ [#60461](https://github.com/ceph/ceph/pull/60461): [f62da6d](https://github.com/ceph/ceph/commit/f62da6d4b7408c9a0c04935a0d551a5bf7952b48)
- Updated documentation to note that enabling mirroring via the monitor command causes the mirror daemon to enter a "failed" state, so the module command should be used instead.
  ↳ [#60525](https://github.com/ceph/ceph/pull/60525): [6fdc942](https://github.com/ceph/ceph/commit/6fdc942d0b4f6846c19fbf38ce617029ac1a6e38)
- Updated CephFS documentation, in the File Layout and Quota Limits section, to remind users that the 'p' flag must be used when writing to the layout.
  ↳ [#60482](https://github.com/ceph/ceph/pull/60482): [30c9e12](https://github.com/ceph/ceph/commit/30c9e12ea0d9e9d7ff1cba7ce5517e018454c146)
- Improved wording in the "Disabling Volume Plugins" section in the CephFS troubleshooting documentation, and updated examples in the volume management documentation.
  ↳ [#60467](https://github.com/ceph/ceph/pull/60467): [dbcfe7c](https://github.com/ceph/ceph/commit/dbcfe7c93cf84b6dde2041e1311600b354f63b7a)
- New guidance on blaum_roth encoding has been added to the documentation, and administrators are advised to adjust the default word size when creating configuration files.
  ↳ [#60537](https://github.com/ceph/ceph/pull/60537): [19454b0](https://github.com/ceph/ceph/commit/19454b0ea72f211d4b55d71fdf35ae8551724060)
- Added distribution information that supports Squid to the operating system recommendation table.
  ↳ [#60557](https://github.com/ceph/ceph/pull/60557): [daa6c69](https://github.com/ceph/ceph/commit/daa6c69bcfd4692d6300335eff59dc39623860e9)
- Split the "Packages and Containers" diagram in the documentation into two separate diagrams.
  ↳ [#60698](https://github.com/ceph/ceph/pull/60698): [5c8e90f](https://github.com/ceph/ceph/commit/5c8e90f5434b0ffb772b79c95b06b61ffee9a527)
- Added documentation for the balancer's update_pg_upmap_activity configuration item.
  ↳ [#60718](https://github.com/ceph/ceph/pull/60718): [c427886](https://github.com/ceph/ceph/commit/c4278865010e4e964c42039006e87ac5aaf97bc2)
- Updated RGW notification related documentation, added missing management commands and removed obsolete commands.
  ↳ [#60609](https://github.com/ceph/ceph/pull/60609): [9444c0c](https://github.com/ceph/ceph/commit/9444c0c46df0953bedb5a0b64deff4f4b6024a2d)
- Clarified that when the notification_v2 feature is enabled after an upgrade, existing metadata will trigger a migration, while brand new deployments will use the new format directly.
  ↳ [#60662](https://github.com/ceph/ceph/pull/60662): [e85e62a](https://github.com/ceph/ceph/commit/e85e62a8e1e73616afb343a39476e2b08335c42a)
- Added cross-reference link to the "Placement by Pattern Matching" chapter in the Advanced Specifications section of the OSD service documentation.
  ↳ [#60644](https://github.com/ceph/ceph/pull/60644): [a4b0e2a](https://github.com/ceph/ceph/commit/a4b0e2aedba8a5864212ac87a23cb9a4f2dd8326)
- Fixed the warning about "full ratio" in the documentation.
  ↳ [#60737](https://github.com/ceph/ceph/pull/60737): [ad002b7](https://github.com/ceph/ceph/commit/ad002b7cf5dbf94b211f573987139a06dac29a00)
- Updated the operating system recommendation information in the document and moved the operating system information that supports Ceph official container images to a dedicated table.
  ↳ [#60766](https://github.com/ceph/ceph/pull/60766): [80eb0c7](https://github.com/ceph/ceph/commit/80eb0c7b5c6bbc17ae4deacc0f39f14f0396e0de)
- Updated the title of the "Deploy a new cluster" section in the documentation to "Deploy a new Ceph cluster using cephadm".
  ↳ [#60809](https://github.com/ceph/ceph/pull/60809): [3dd143b](https://github.com/ceph/ceph/commit/3dd143b0a9e1269e2706fd9c11a371ec28be91c3)
- Improved instructions for logging and debugging in the RADOS troubleshooting documentation.
  ↳ [#60824](https://github.com/ceph/ceph/pull/60824): [2006e1f](https://github.com/ceph/ceph/commit/2006e1f26d2fbd6ca1411aea17b62afcc504c095)
- Improved presentation of archive-sync-module.rst documentation.
  ↳ [#60852](https://github.com/ceph/ceph/pull/60852): [dd79be3](https://github.com/ceph/ceph/commit/dd79be33dc80c07476027c9133561b39b4b96041)
- Improved documentation description of BlueStore related health checks.
  ↳ [#60893](https://github.com/ceph/ceph/pull/60893): [2e26279](https://github.com/ceph/ceph/commit/2e262791dd66627fd75a7d7dd3e7d2fec3237758)
- Updated RGW documentation to explain how to configure access to virtual hosted buckets by setting rgw_dns_name, and added information about the AWS S3 path deprecation plan.
  ↳ [#60885](https://github.com/ceph/ceph/pull/60885): [1e9c785](https://github.com/ceph/ceph/commit/1e9c785366f6783af50acab31fc0956b25e05557)
- Added Dashboard Plugin entry to glossary.
  ↳ [#60896](https://github.com/ceph/ceph/pull/60896): [9043ef6](https://github.com/ceph/ceph/commit/9043ef66494a7bcdb5735efe3c16fa490da173ce)
- Updated the release process documentation to detail the container build and release process.
  ↳ [#60971](https://github.com/ceph/ceph/pull/60971): [6dae68b](https://github.com/ceph/ceph/commit/6dae68b543f21c7901cde7692b6dc689020024db)
- Fixed the syntax of the health check document and added health check instructions about the NVMeoF gateway.
  ↳ [#60949](https://github.com/ceph/ceph/pull/60949): [7282257](https://github.com/ceph/ceph/commit/728225746bb23a624ce1b757a82e557a52e21d34)
- Added instructions to the development workflow documentation requiring developers to be responsible for backporting appropriate commits to the relevant stable branch.
  ↳ [#61063](https://github.com/ceph/ceph/pull/61063): [93d2d49](https://github.com/ceph/ceph/commit/93d2d49047adae2f3abf6985566efedf20ad88c4)
- Edited the CephFS kernel driver mounting document and optimized the English description.
  ↳ [#61080](https://github.com/ceph/ceph/pull/61080): [a34881c](https://github.com/ceph/ceph/commit/a34881cf2e4aa1f43349c01d522e53b65e8dbb8a)

### Build/CI
- Fixed compilation failure caused by macro implementation under GCC 14.
  ↳ [#59055](https://github.com/ceph/ceph/pull/59055): [70f9aca](https://github.com/ceph/ceph/commit/70f9aca79d4f44310ec93fdc12290d1cd1b94d1a)
- Changed the way the isa-l_crypto library is built to use CMake ExternalProject.
  ↳ [#60107](https://github.com/ceph/ceph/pull/60107): [c7c93fa](https://github.com/ceph/ceph/commit/c7c93fa0f354afd348951d37e7acf3b4cdfc8de3)
- Change the way the isa-l library is built to use the CMake ExternalProject mechanism.
  ↳ [#60107](https://github.com/ceph/ceph/pull/60107): [d199d36](https://github.com/ceph/ceph/commit/d199d369746f8de62caab726de5fec2aa4477616)
- Removed build configuration for spawn submodule.
  ↳ [#60133](https://github.com/ceph/ceph/pull/60133): [df65738](https://github.com/ceph/ceph/commit/df657381b3c161608aab71c1228c932b8bdf565b)
- Removed setting of Seastar_STD_OPTIONAL_VARIANT_STRINGVIEW option in CMake build configuration.
  ↳ [#58955](https://github.com/ceph/ceph/pull/58955): [026b4d1](https://github.com/ceph/ceph/commit/026b4d100dc2068dcf58237ada462353d1e9bfd0)
- In the CMake build configuration, set Seastar's DEPRECATED_OSTREAM_FORMATTERS option to off.
  ↳ [#58955](https://github.com/ceph/ceph/pull/58955): [78ab247](https://github.com/ceph/ceph/commit/78ab247a5dce8df6fef526fb5307300719a9e63b)
- Moved ceph-volume's packaging runtime dependency from the RPM spec file to setup.py.
  ↳ [#59202](https://github.com/ceph/ceph/pull/59202): [4232567](https://github.com/ceph/ceph/commit/42325673135b988f2fbbfec9ad2174ba24af8cf9)
- Updated the project version number from 19.2.0 to 19.2.1, and updated the Debian package change log.
  ↳ [#61667](https://github.com/ceph/ceph/pull/61667): [58a7fab](https://github.com/ceph/ceph/commit/58a7fab8be0a062d730ad7da874972fd3fba59fb)

### Maintenance
- Enhanced the monitoring and statistical reporting functions of SeaStore, including the introduction of transaction statistics tracking, new transaction IOPS, periodic monitoring of the number of conflicts and the number of pending transactions, and outputting detailed pending transaction status in shard 0.
  ↳ [#58835](https://github.com/ceph/ceph/pull/58835): [4535537](https://github.com/ceph/ceph/commit/4535537044f44ed11293e2bf4819568f021a5191), [7333ec1](https://github.com/ceph/ceph/commit/7333ec1dbbc938967256a535e8bfc925ff2a7aa3)
- Lowered the default value of osd_requested_scrub_priority from 120 to 5 to ensure it has a lower priority than client operation messages.
  ↳ [#59885](https://github.com/ceph/ceph/pull/59885): [490255e](https://github.com/ceph/ceph/commit/490255e760089ce487f3c22d7872cd914a658b69)
- When OSD starts, the log will now output the average reactor utilization of each shard.
  ↳ [#58835](https://github.com/ceph/ceph/pull/58835): [b11b061](https://github.com/ceph/ceph/commit/b11b061b4930235b540dae3aa316797e55563929)
- In AlienStore::stop(), clear coll_map after stopping to ensure that resources are released correctly.
  ↳ [#58841](https://github.com/ceph/ceph/pull/58841): [c150ff6](https://github.com/ceph/ceph/commit/c150ff6e2390c1f7243abf7d4eb1fb162dbae504)
- Removed unused variable declarations in the FixedKVBtree::rewrite_extent method and updated the call to the rewrite method to pass transaction parameters.
  ↳ [#58957](https://github.com/ceph/ceph/pull/58957): [d462202](https://github.com/ceph/ceph/commit/d4622027a389fe3840fd2b3bb88748785cc5a8cc)
- Changed the container image source in the cephadm example configuration from docker.io to quay.io.
  ↳ [#60354](https://github.com/ceph/ceph/pull/60354): [2eec145](https://github.com/ceph/ceph/commit/2eec145c406fe2d860ca13ad482edbfb10a99873)
- Updated the dashboard front-end internationalization configuration and switched the translation resources from the main branch to the Squid version.
  ↳ [#60367](https://github.com/ceph/ceph/pull/60367): [83614f9](https://github.com/ceph/ceph/commit/83614f9246f106c64daed6917da67a87187ffa71)
- Improved the detail and accuracy of error logs in the librbd migration client to facilitate issue tracking.
  ↳ [#61095](https://github.com/ceph/ceph/pull/61095): [ee52159](https://github.com/ceph/ceph/commit/ee52159c90f96578244b460a915c1a651168e35a), [6b2f69d](https://github.com/ceph/ceph/commit/6b2f69db4f192ae093d27494e82852db6c6514c8)
- Fixed a minor problem with the _check_or_set_main_bdev_label function in BlueStore, and moved the declaration of the bluestore_bdev_label_t variable into the conditional branch.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [4840e22](https://github.com/ceph/ceph/commit/4840e225fbf8ab3d67563e8c703f5546ed1ad324)

### Others
- Added executor_type type alias for context_pool class.
  ↳ [#60133](https://github.com/ceph/ceph/pull/60133): [e55d923](https://github.com/ceph/ceph/commit/e55d92317c6894440e3d82ea015b56fbbc2da134)
- Fixed formatting and wording of various error log messages in the librbd migration module.
  ↳ [#59145](https://github.com/ceph/ceph/pull/59145): [fa041c8](https://github.com/ceph/ceph/commit/fa041c89c83ac1eebd6af78d568fddec826f6201)
- Updated the format of the "Building Ceph" section in the README.md document, changing the build steps to an ordered list.
  ↳ [#59798](https://github.com/ceph/ceph/pull/59798): [4c10a93](https://github.com/ceph/ceph/commit/4c10a939f67c355a2d72694be1c6ca8540c399af)
- Updated the email addresses of three members in the governance document.
  ↳ [#60084](https://github.com/ceph/ceph/pull/60084): [413c49b](https://github.com/ceph/ceph/commit/413c49b76b8a345493a8d20bcba6a0e11e676852)
- Corrected sentence tone and expressions in several sections of the doc/rados/operations/health-checks.rst file.
  ↳ [#60931](https://github.com/ceph/ceph/pull/60931): [20a4743](https://github.com/ceph/ceph/commit/20a47430db00a7f1d1573889b46714737438b91e)
- Fixed wrong macro name in BlueFS tests, corrected DB_SUPER_RESERVED to SUPER_RESERVED.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [d4ea190](https://github.com/ceph/ceph/commit/d4ea1905c33b11484c5d9d345a2efb2c371fd975)
- Adapt to the unit test of multiple device labels, and change the call to read the device label in the test to use an auxiliary function.
  ↳ [#59106](https://github.com/ceph/ceph/pull/59106): [c586db8](https://github.com/ceph/ceph/commit/c586db867907ce58e0170bb4046dd21fb3ee4ae0)
- Fixed a typo in the cephadm documentation, changing no to not.
  ↳ [#60637](https://github.com/ceph/ceph/pull/60637): [53cd344](https://github.com/ceph/ceph/commit/53cd344a15437468bcb5b2ed352850ab4b2b04aa)
- Fixed a typo in the documentation about TLS, correcting SSL/TSL to SSL/TLS.
  ↳ [#59031](https://github.com/ceph/ceph/pull/59031): [ff3fd81](https://github.com/ceph/ceph/commit/ff3fd819a4aa4da3cc64584dcec03d7250e070d5)
- Add the seastar submodule path to the GitHub tag configuration so that it is tagged as crimson.
  ↳ [#58955](https://github.com/ceph/ceph/pull/58955): [f2d329d](https://github.com/ceph/ceph/commit/f2d329d5e03289b6ba945ceffc3044141893405b)
- Fixed compilation issues with incorrect return values of two void functions in test files.
  ↳ [#58955](https://github.com/ceph/ceph/pull/58955): [cb187ba](https://github.com/ceph/ceph/commit/cb187bae5d4c3ea7a171c7e45c624eba0fa22437)
- Improved the English description of the "Layout Fields" section in the CephFS file layout documentation.
  ↳ [#59021](https://github.com/ceph/ceph/pull/59021): [16e20a5](https://github.com/ceph/ceph/commit/16e20a5e63f16077cdc8813da54b4779902bc703)
- Fixed typo of ObjectSizeGreaterThan in LCFilter_S3::dump_xml method.
  ↳ [#59223](https://github.com/ceph/ceph/pull/59223): [545f7b5](https://github.com/ceph/ceph/commit/545f7b5e0cb11b2a4fc0d20ba1c11a05341a147c)
- Updated the acting set example in the peering development documentation, correcting [2,1,2] to [3,1,2].
  ↳ [#59062](https://github.com/ceph/ceph/pull/59062): [090a109](https://github.com/ceph/ceph/commit/090a109cd45724d06946775ac04faba21c3afd59)
- Improved wording and syntax of QAT acceleration documentation.
  ↳ [#59179](https://github.com/ceph/ceph/pull/59179): [f4d2cc2](https://github.com/ceph/ceph/commit/f4d2cc2331f83a53dba7d3d71ccb5d4f96d496c7)
- Improved the description of layout fields in the CephFS file layout documentation, corrected the wording of the pool field and rewritten the description of the stripe_unit field.
  ↳ [#59250](https://github.com/ceph/ceph/pull/59250): [fd33760](https://github.com/ceph/ceph/commit/fd33760ab2a0bd4498678e16dcde28540842d85c)
- Corrected the "mountpoint" in the English text of the document to "mount point".
  ↳ [#59289](https://github.com/ceph/ceph/pull/59289): [9f72d25](https://github.com/ceph/ceph/commit/9f72d25bbffa10c91b96580fcd0c932c356160d4)
- Unify the spelling of the word mountpoint in the document and change it to mount point.
  ↳ [#59291](https://github.com/ceph/ceph/pull/59291): [1a42b19](https://github.com/ceph/ceph/commit/1a42b19f9d9661213ff51560146bf6be1e4d2d26)
- Corrected the link to the Prometheus configuration document in the documentation, removing the extra slash at the end of the anchor link.
  ↳ [#59559](https://github.com/ceph/ceph/pull/59559): [ea8a0b9](https://github.com/ceph/ceph/commit/ea8a0b97579fdd42f55e07649e27e486647cd8d0)
- Fixed spelling and formatting issues in NFS documentation, changed ceph filesystem to CephFS.
  ↳ [#59896](https://github.com/ceph/ceph/pull/59896): [02bfd27](https://github.com/ceph/ceph/commit/02bfd27317336c58bdf432a71243ddad9104f261)
- Added link to Messenger v2 information at end of mon-lookup-dns documentation.
  ↳ [#59794](https://github.com/ceph/ceph/pull/59794): [d5c19cc](https://github.com/ceph/ceph/commit/d5c19ccb10094a9b9f023c5b47139d7280b7b81b)
- Optimized the expression of the "Build Prerequisites" section in README.md.
  ↳ [#59637](https://github.com/ceph/ceph/pull/59637): [0866b71](https://github.com/ceph/ceph/commit/0866b7186647aff4e19ded9db979689664465b80)
- Improved documentation formatting and styling of the "Building Ceph" section in the README.md file.
  ↳ [#59700](https://github.com/ceph/ceph/pull/59700): [3d12652](https://github.com/ceph/ceph/commit/3d126521ac0c8c9b8df19c08ed635d223b280e16) | [#59785](https://github.com/ceph/ceph/pull/59785): [9965290](https://github.com/ceph/ceph/commit/9965290f5d7676a1d4941cfbd0ea4f6b532061e9)
- Update the release checklist and mark telemetry verification related check items as completed.
  ↳ [#59813](https://github.com/ceph/ceph/pull/59813): [ea0fbd1](https://github.com/ceph/ceph/commit/ea0fbd1917fc266e681f9c51616555a4ee50445a)
- Updated NFS documentation to add external links to Ganesha's Kerberos setup.
  ↳ [#59939](https://github.com/ceph/ceph/pull/59939): [325dd88](https://github.com/ceph/ceph/commit/325dd885bfb0507d82e7f472a337c02d4a16b498)
- Fixed typo in Jaeger trace documentation.
  ↳ [#59991](https://github.com/ceph/ceph/pull/59991): [ab7de41](https://github.com/ceph/ceph/commit/ab7de4162b91f1cb9a917cf7f96a735bcb1f751a)
- Improved syntax in the "Placement Groups Never Get Clean" section of the documentation.
  ↳ [#60046](https://github.com/ceph/ceph/pull/60046): [8675b7c](https://github.com/ceph/ceph/commit/8675b7c39e5f5011a2a89967ed7e3e04b83e6628)
- Fixed an error in the "Configuring Secondary Zone" chapter in the multisite documentation, correcting "Update Primary Zone Configuration" to "Update Secondary Zone Configuration".
  ↳ [#60332](https://github.com/ceph/ceph/pull/60332): [257c5b4](https://github.com/ceph/ceph/commit/257c5b4e2b687d84f117ffb56dc98942789d2c9f)
- Updated email addresses in governance documentation.
  ↳ [#60233](https://github.com/ceph/ceph/pull/60233): [8b8ef52](https://github.com/ceph/ceph/commit/8b8ef5213a4758e081f6ee5caa963042498ebf47) | [#60338](https://github.com/ceph/ceph/pull/60338): [88f5ad9](https://github.com/ceph/ceph/commit/88f5ad93de9ec683985014564fb3fc47f10ba17b)
- Removed reference to the defunct "Stable Release and Backport Team" in the documentation.
  ↳ [#60297](https://github.com/ceph/ceph/pull/60297): [09e362f](https://github.com/ceph/ceph/commit/09e362f17b64ce7764157a23e5837cd8e4ef9aa4)
- Rearranged information about subvolume groups in CephFS documentation for consistency.
  ↳ [#60435](https://github.com/ceph/ceph/pull/60435): [ed8e701](https://github.com/ceph/ceph/commit/ed8e7017985330175e73bad79185b8e4f390d186)
- Fixed many grammatical errors in the document and replaced inappropriate subordinating conjunctions with more accurate words.
  ↳ [#60593](https://github.com/ceph/ceph/pull/60593): [e193c95](https://github.com/ceph/ceph/commit/e193c954c2011d2dc5a1bb6e1401cea423f07fe1)
- Cleaned up syntax and formatting of the "Advanced OSD Service Specifications" section in the Cephadm documentation.
  ↳ [#60679](https://github.com/ceph/ceph/pull/60679): [1d30da1](https://github.com/ceph/ceph/commit/1d30da109356b816183d252e09c4c2bf4787740d)
- Fixed the spelling error of "are are" in the documentation.
  ↳ [#60708](https://github.com/ceph/ceph/pull/60708): [5081739](https://github.com/ceph/ceph/commit/5081739d1a50402962d1a3344e2f7bff701ee506)
- Fixed typos in multiple IAM policy action names in the documentation, correcting Poliicy to Policy.
  ↳ [#60707](https://github.com/ceph/ceph/pull/60707): [f08400c](https://github.com/ceph/ceph/commit/f08400cd03dad1629b997d1cc6222f1e85be3c87)
- Improved wording in Archive Sync module documentation to improve clarity.
  ↳ [#60867](https://github.com/ceph/ceph/pull/60867): [22a1e88](https://github.com/ceph/ceph/commit/22a1e882b64e1dbf40f2a91daa4171011313bc3d)
- Unified the tone of the sentences at the beginning of each section in the health-checks document.
  ↳ [#60920](https://github.com/ceph/ceph/pull/60920): [ea69ebe](https://github.com/ceph/ceph/commit/ea69ebe25beadfa0809f9172e19424c2e5a843cd)
