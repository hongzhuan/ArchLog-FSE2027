# Release Note

## Routine Changelog

### New Features

- After CephFS subvolume clone completes, retain source volume/group/subvolume/snapshot metadata, and output this source information via the `subvolume info` command; documentation and tests are updated accordingly. [commit](https://github.com/ceph/ceph/commit/2c9a84a8c949c7ace5d98780819f40ff2c19f544) [commit](https://github.com/ceph/ceph/commit/fbba4629cf6182fec31b8d3c391ed86b5b9f9d8f) [commit](https://github.com/ceph/ceph/commit/cf3347c8742097247c523126aa7f2ca7680320bd) [commit](https://github.com/ceph/ceph/commit/4a1c47909d3a10bf2645373528ec436ace6db466)

- Python RADOS interface adds `list_lockers()` and `break_lock()` to query object lock holders and interrupt specified locks. [commit](https://github.com/ceph/ceph/commit/263497f188537db886ca02f67878a2e5808bff2f)

- Client and libcephfs add `getlk`/`setlk` record lock interfaces, and add high-level API lock behavior tests. [commit](https://github.com/ceph/ceph/commit/942c6168688ee552f202b8493e25e68df9f9d647) [commit](https://github.com/ceph/ceph/commit/8c62062093c65cd594e360966d39dacc25291dc6) [commit](https://github.com/ceph/ceph/commit/612882aae1653ce9113edc6dd8a3b61137804ebd)

- `radosgw-admin bucket list` adds `--max-entries` and marker pagination parameters, and passes page size and cursor to list buckets page by page. [commit](https://github.com/ceph/ceph/commit/1d25b2b737cd61dd5a9c1093e1e84d083d004962) [commit](https://github.com/ceph/ceph/commit/d42b6b08a2d3e7a5c0aa568afb6ad00f1af0408d) [commit](https://github.com/ceph/ceph/commit/935136d45ff38f253dfb45c4d3386737cf014625) [commit](https://github.com/ceph/ceph/commit/5a7f239c33b8ca10019ba2047c2abf8c02a776be)

- Add `ceph-osd --run-benchmark` option to run throughput benchmark during OSD creation and output results. [commit](https://github.com/ceph/ceph/commit/d74f37773600284940c68e6a26f980c189e0db52)

- ceph-volume LVM batch supports passing additional LUKS formatting and opening parameters (`--dmcrypt-format-opts`, `--dmcrypt-open-opts`). [commit](https://github.com/ceph/ceph/commit/fbe2f910a6a23ffef6b580ebddc4f4c7e7fb9f08)

- CephFS subvolume group creation supports name mangling configuration, allowing setting directory case sensitivity and Unicode normalization, and is documented in commands and documentation. [commit](https://github.com/ceph/ceph/commit/a98dd780ed8742d191c4090fbdc5c2a94cec70ae) [commit](https://github.com/ceph/ceph/commit/7851ce10365706e7e558c340d34ea1ef12868ae8) [commit](https://github.com/ceph/ceph/commit/1dd92284ec0da636c156fd7c4ab7c66191ca38bd) [commit](https://github.com/ceph/ceph/commit/40196cf2af182111c9ee9a53d687b6296a2e7bc8)

- Generic performance counters support explicit service unique ID, and RGW writes this ID to ServiceMap metadata when configured. [commit](https://github.com/ceph/ceph/commit/1344d5028394f275e243fd1c9990614523d69d19) [commit](https://github.com/ceph/ceph/commit/3fe65f2d3270fcdfa01c1f0fd76f6a91e81f4e07)

- Dashboard editing NFS Export can also select and save CephFS subvolume group and subvolume. [commit](https://github.com/ceph/ceph/commit/3862c76be6d1ba9bb0e9d8d3bf67c8a3791c2349)

- Dashboard RGW tiering form moves advanced configurations such as placement target into the advanced area, and fixes the data for advanced option backfill. [commit](https://github.com/ceph/ceph/commit/4a46b495c0c51776bfb8e9d2d12c813c45e96223) [commit](https://github.com/ceph/ceph/commit/0b1ea488dbaa9cf9fca71f05f4adb04cb17c6d93)

- Dashboard supports deleting multiple Ceph users at once in the user list. [commit](https://github.com/ceph/ceph/commit/16cbb7588b378a802c0f4eebb29fc174e024cb61)

- Dashboard NVMe-oF namespace commands support NSID query and filtering, optional omission of NQN, passing gateway and read-only/auto-expand parameters; on creation, maximum namespace count is left to gateway default, and conflicting size parameters are rejected. [commit](https://github.com/ceph/ceph/commit/a7f0a22fb9d4d5a815ca6c8479cae7f9af1d79ee) [commit](https://github.com/ceph/ceph/commit/5aa2b4221043e898b7f5cf444383e4fc21e0d007) [commit](https://github.com/ceph/ceph/commit/c6e0727a738533ba5f4bb60f279fcc1a0d685fcb) [commit](https://github.com/ceph/ceph/commit/db7cd1a8b1aa0cc0901674e2d48d19c042156aee) [commit](https://github.com/ceph/ceph/commit/4be0ec60063c8616c5c4bcaa1bc6f565991e5f37)

- cephadm reads distribution `ID_LIKE` and falls back to matching base distribution, so customized/derived systems based on supported distributions can be recognized. [commit](https://github.com/ceph/ceph/commit/3de42f288e6ecdc79d932a5e0f10ff8495a4b707)

- Dashboard creating RGW local storage class supports creating required pools, and displays zone and pool information in details. [commit](https://github.com/ceph/ceph/commit/3ec58c0b007d07379b6cd3c2e2123676ef80ba2f)

- MDS provides `ceph.dir.subvolume` virtual xattr for directories: subvolume root returns `1`, other directories return `0`. [commit](https://github.com/ceph/ceph/commit/c90ffa0ec7ef455d46c790d9540c83fa4f7059c1)

- `ceph osd availability` output supports serialization in user-specified formats (including JSON), and corresponding documentation is added. [commit](https://github.com/ceph/ceph/commit/ec12abbe84755848b1eaaa85ac2c925f63e0994f) [commit](https://github.com/ceph/ceph/commit/e83bcac96cda00baf2ddbc5d9b8eacba9df1374c)

- Dashboard NVMe-oF supports querying gateway statistics and listener information. [commit](https://github.com/ceph/ceph/commit/62a4da787db0d606bb44b10bca2d6f6a4e0909cd)

- RGW adds pending and failed counters for Kafka/AMQP pubsub push. [commit](https://github.com/ceph/ceph/commit/df66f697d14343462b4eadc716031cf0b17a3607)

- Telemetry's `basic_pool_flags` adds `ec_optimizations` configuration item. [commit](https://github.com/ceph/ceph/commit/e766ac8bb42b18cc34216a55b3202bef94cc05fe)

- Dashboard generic table-actions supports custom menu layout and offset, for OSD and RGW pages to configure action menus. [commit](https://github.com/ceph/ceph/commit/0638483e466475177ce36caae10e39e1b05fe758)

- Dashboard supports deleting non-default RGW zones and zonegroups. [commit](https://github.com/ceph/ceph/commit/b90e37453d796a224b51d3db4f23016454d8e781)

- Dashboard adds an editable string label list component, used for SMB service custom DNS input. [commit](https://github.com/ceph/ceph/commit/90e1b9d061c1f379c0067689e4ff80453e5bd462) [commit](https://github.com/ceph/ceph/commit/fde11b4b46ef2c887cb9b84cf28217ab8a35f7c1)

- Dashboard RGW service form adds QAT compression option. [commit](https://github.com/ceph/ceph/commit/853d132bbbb43f54c851cb3d041bab9f98d83a6a)

- Prometheus adds cephadm orchestrator `ps` status metric for monitoring daemon status. [commit](https://github.com/ceph/ceph/commit/a7381e27c1f54e506c2f90d01e3136a23639c90b)

- BlueStore admin socket adds free space distribution histogram to check space fragmentation and allocator status. [commit](https://github.com/ceph/ceph/commit/6b897f248c4e3f29b55c666ae7031a457ef57ec8)

- BlueStore allocator adds configurable free-space lookup policy to select space lookup strategy based on media such as SSD/HDD. [commit](https://github.com/ceph/ceph/commit/6c5bd3dba55c7e53925529707f5d27b524995bf8)

- Dashboard NVMe-oF adds command and API to get subsystem information. [commit](https://github.com/ceph/ceph/commit/32cbd2248f6cba17d88817c9503b922b618c0004)

- Dashboard adds REST API for RBD consistency groups and group snapshots, supporting create/list/update/delete consistency groups, add/remove images, and manage snapshots (including rollback). [commit](https://github.com/ceph/ceph/commit/a972b506b14127b8f0d9ac733f74ce2105bcadd4) [commit](https://github.com/ceph/ceph/commit/96c1d22511ec2c314bf190ab08185336f6538a86) [commit](https://github.com/ceph/ceph/commit/bb1e684b2d37ee1a06e5d229d2b3ffb075b1d4ef) [commit](https://github.com/ceph/ceph/commit/86ad6c853ae4f2dc9493ead6070c193bcd2b405f) [commit](https://github.com/ceph/ceph/commit/9cca607ef187649ef3f96e2c83e8465f71e6a9ad) [commit](https://github.com/ceph/ceph/commit/defa6146a04c398a4e2cde019c9eee4f5733b3b7) [commit](https://github.com/ceph/ceph/commit/1b8620edcd2e798fe0e19cf384edab3d217edf20) [commit](https://github.com/ceph/ceph/commit/e5657ab645e37249ca66986437519f0bd98fc845) [commit](https://github.com/ceph/ceph/commit/53bab15e0a1e4007106ad081c3dcaa3d3449914b)

- Dashboard adds reusable step wizard and full-page tearsheet flow components, supporting creation process and cancellation confirmation. [commit](https://github.com/ceph/ceph/commit/c0a42f22bb30fdc19b8254493906c2b12e02bd62) [commit](https://github.com/ceph/ceph/commit/81e8b6258886ea88429140f55f6d1deb93d3f68b)

- cephadm NVMe-oF service spec adds gateway configuration fields and passes them to the generated configuration file. [commit](https://github.com/ceph/ceph/commit/a942bee07c3d4ab5a8509cd59dd27b8f8623aaf9)

- Dashboard RGW multisite supports creating archive zones or configuring existing zones as archive. [commit](https://github.com/ceph/ceph/commit/952420087f0fc781a1ca78e095b5712047b72f8f)

- Dashboard adds API to get all NVMe-oF namespaces by gateway group, avoiding compatibility limitations of the original subsystem interface; and unifies gateway address query parameter to `traddr`. [commit](https://github.com/ceph/ceph/commit/d33ffd3d814b675533c13a9ddff3e071c5d888f2) [commit](https://github.com/ceph/ceph/commit/ea41c2930c4f10ca094a897854e724bace4b0b0e)

- Dashboard adds optional Overview home page and generic card components, providing a new cluster overview layout, and names the side navigation entry Overview. [commit](https://github.com/ceph/ceph/commit/c83576707e4037cc92bfeb475aa998e10fbe1f15) [commit](https://github.com/ceph/ceph/commit/dff5e5507908c71febca2d3396de840e9f8d9510) [commit](https://github.com/ceph/ceph/commit/92d36970fb007b45f8c9e9c9156749158e17f152)

- Dashboard pool, CRUSH rule, and erasure-code profile forms adopt Carbon components and styles, updating related form interactions. [commit](https://github.com/ceph/ceph/commit/7620364e8e7bf0c46722ed15c94efcde69a32d7e)

- Add MON command `nvme-gw listeners` to list listeners in specified pool and gateway group, including automatic listeners not written to OMAP. [commit](https://github.com/ceph/ceph/commit/e4f6e6a7e0eeedd60a02e80ab97f7d0524c79e90)

- Dashboard RGW multisite export realm token dialog switches to Carbon modal, and updates corresponding interactions. [commit](https://github.com/ceph/ceph/commit/15e48ecd2de960b56b88c1a7197e0109a9d6b58e)

- librbd adds `RBD_LOCK_MODE_EXCLUSIVE_TRANSIENT` lock mode: during manual lock holding, writes from other peers wait for lock release instead of immediately failing due to permanent exclusive policy; the same image handle can switch between exclusive policies. [commit](https://github.com/ceph/ceph/commit/047692467af7c8e3cce967e439f7b02faead2b2f) [commit](https://github.com/ceph/ceph/commit/b8e1b4414ece83e331d6ba395b8e214f5728e5c2)

- RGW conditional MultiWrite passes `If-Match` / `If-None-Match` precondition to object write and multipart completion flows. [commit](https://github.com/ceph/ceph/commit/39dc94089f1c9f6b3b82cf8622b0b30dd6d5f388)

- BlueFS volume selector consistency check configuration changed to `bluefs_check_volume_selector_on_mount`, and checks are performed on mount and unmount. [commit](https://github.com/ceph/ceph/commit/de35c1da16bcee0ed65f4aaa876244a3f30416a8)

### Bug Fixes

- MDS releases `mds_lock` before waiting for ACK when shutting down Beacon, avoiding deadlock caused by dispatcher thread unable to process ACK. [commit](https://github.com/ceph/ceph/commit/b40e7c9dc435d2d52fe6a77ecfce88156785771b)

- MDS now skips client-facing charmap handler checks when processing internal requests, avoiding false validation due to missing client session metadata; added reintegration tests. [commit](https://github.com/ceph/ceph/commit/fd46d7080a2169411addd5832a7084c31f565c1d) [commit](https://github.com/ceph/ceph/commit/d667e48869c72275824a59cf81676bbb4066f26c)

- Fixed the reference count release method for Manager operation requests, avoiding double release after explicitly decrementing the request reference. [commit](https://github.com/ceph/ceph/commit/663e7a3418ed8064bb900ac825e1ffb0832d47e4)

- libcephfs `statfs` now calculates statistics based on the inode corresponding to the request path, and selects the applicable quota root based on the mount root and its visible parent directories. [commit](https://github.com/ceph/ceph/commit/b8949266cc33351c32385de462c73e9e6c10770a) [commit](https://github.com/ceph/ceph/commit/57bf683d45f95e091e942188e6a79a697ede0de4) [commit](https://github.com/ceph/ceph/commit/2275781d7f9fb8ec550925ba14e0ccc9ef3bb413) [commit](https://github.com/ceph/ceph/commit/e516079b36230b9d69c9f5f286a970e4fb0ab4f1) [commit](https://github.com/ceph/ceph/commit/808682a7e622c722767f7cb74f4b51cd644808b1)

- CephFS client now returns `ENOTDIR` when looking up/opening non-directory inodes, avoiding treating regular files as directories. [commit](https://github.com/ceph/ceph/commit/4a8ff5380330df1132121c02c487699d27ec6b14) [commit](https://github.com/ceph/ceph/commit/ad92bf02b33238858df0e1bd29a9c4c152bd0e64)

- CephFS client now limits the buffer/total length for synchronous read/write to no more than `INT_MAX`, and limits `bufferlist` to allocate based on actual write length, to correctly handle oversized I/O requests. [commit](https://github.com/ceph/ceph/commit/6f20746dbdccb3d41f7bf78fb7338a46df145f04) [commit](https://github.com/ceph/ceph/commit/52610131bacbc35d60ebd6a5045a169ca23e5f80) [commit](https://github.com/ceph/ceph/commit/83b19e441117b3d4fb6ee2c2876954ebf672fc92)

- CephFS volumes now retains MON capability when the same auth key still has MDS/OSD capabilities, allowing clients to continue querying filesystem information from the monitor. [commit](https://github.com/ceph/ceph/commit/95bc2305542a5bd6220e02a61b0b176f386f76d2) [commit](https://github.com/ceph/ceph/commit/d308d313c15bb86e110dfa339ec630100f96fbcd) [commit](https://github.com/ceph/ceph/commit/a408aaa36b18030cdbfd9fcef882cc0ef15f6f3d)

- Fixed the return value of supported authentication connection modes for the peer in msgr2 `AuthBadMethodFrame` handling. [commit](https://github.com/ceph/ceph/commit/03e71cf369c9a72e45ad898303ed82cd19292c8d)

- Fixed filesystem name matching for authentication capabilities between MDS and CephFS client in multi-filesystem environments, and covered cross-filesystem access and squid client upgrade scenarios. [commit](https://github.com/ceph/ceph/commit/5d94f0c83e9f318833fd6c9e6c1951fff704d9cc) [commit](https://github.com/ceph/ceph/commit/66fd5fdc935f05cb5590b277efd684d3a01dbc6a) [commit](https://github.com/ceph/ceph/commit/5f171156b55f7b555ae8cf6279ea28748f87ed71) [commit](https://github.com/ceph/ceph/commit/f9e4ad56008f432458c838b2b2c7762b543bcf62) [commit](https://github.com/ceph/ceph/commit/216c886c189b64823cbcac5662db58b147101430) [commit](https://github.com/ceph/ceph/commit/286480c017d85c8a715a8fed6e4adef68ed1414c)

- Fixed MDS handling of `readdir` when OSD is full, so related directory operations no longer abort early due to attempts to fetch non-resident inodes; added subvolume list regression tests. [commit](https://github.com/ceph/ceph/commit/aa339674471e2e26488252fc3c4bd458d37ccd42) [commit](https://github.com/ceph/ceph/commit/a08fb44e28ce7c37b91774909f89356ca3ab95dd)

- Fixed CephFS snapdiff missing records when rolling back old fragment entries after fragment changes for same-name directory entries. [commit](https://github.com/ceph/ceph/commit/c79cf1af29e786161916ae0aa411bdd891fa8d29) [commit](https://github.com/ceph/ceph/commit/a16e0395b9d8e1303617fda956c1d89c58c6f0fd) [commit](https://github.com/ceph/ceph/commit/0a9e33733c50aacac223bd409813b0a711b7b181) [commit](https://github.com/ceph/ceph/commit/04c34b62a7ebad9296593edfcc8132b1c7351513)

- `scrub_purged_snaps()` now follows `osd_beacon_report_interval` when sending OSD beacons, no longer ignoring the configured interval. [commit](https://github.com/ceph/ceph/commit/814b2766f4e696d38aab9b194ef445e1388e0529)

- Fixed the focus style of the Dashboard Carbon input box to avoid shadows obscuring input content. [commit](https://github.com/ceph/ceph/commit/53124bb75b889e8c0e48bf7e0aeef7361e9d04e8)

- Fixed Dashboard RBD image usage calculation: skip deleted snapshots and correctly display the usage bar for images supporting fast-diff. [commit](https://github.com/ceph/ceph/commit/d35b384d030114165b1d6fe261f78326c5e945b0)

- Dashboard now passes the snapshot schedule interval to the backend API when creating RBD images, avoiding loss of the schedule interval during creation. [commit](https://github.com/ceph/ceph/commit/bb9f126e4e590d8e7f1e44a71bed4d02efb1fafe)

- cephadm no longer misreports new-style NVMe-oF daemons that do not carry pool/group in the daemon name as stray. [commit](https://github.com/ceph/ceph/commit/f011669d8c9d5bb22e4f1c475420c79051997557)

- `cephfs-journal-tool` no longer rewrites the journal trim position when resetting the journal. [commit](https://github.com/ceph/ceph/commit/dc553c3fff6e4f96f874477dd420723e314f79ff) [commit](https://github.com/ceph/ceph/commit/42a9beee0741aaea2efeebc1d8bce956a2c5ff63)

- Kernel RBD re-compatible with `bdev_async_discard`: when the thread count is not set, whether to enable asynchronous discard is determined based on the old boolean configuration. [commit](https://github.com/ceph/ceph/commit/615ca9bfbc279bd0be7c0545b35d681dd168d088)

- Dashboard now uses the data pool of the selected storage class when updating an RGW zone, avoiding the fixed requirement for the `STANDARD` class that caused updates to fail for zones without that class defined. [commit](https://github.com/ceph/ceph/commit/9cf554ed9f7b3f3447fd81b8f1f434c0d269e5ee)

- Dashboard multi-cluster connection form now uses a generic URL validator, allowing Cluster API URLs with FQDN. [commit](https://github.com/ceph/ceph/commit/8e4a46065bfad65496e13ddd4358baf090639bcd)

- Dashboard cluster capacity chart uses the total cluster capacity as the upper limit of the vertical axis and displays the chart when capacity data is available. [commit](https://github.com/ceph/ceph/commit/97452279ce121b3980279d3fbb9a521a9dfb73c1)

- Dashboard RGW notification form no longer retains the editing state of the old notification when switching from edit to create. [commit](https://github.com/ceph/ceph/commit/da174509298da14857479515cf8e7c7ea9e541de)

- Dashboard SMB form only shows custom DNS operations in Active Directory mode and fills in the associated column data for standalone clusters. [commit](https://github.com/ceph/ceph/commit/766dbab7320949f7917ef60e26b1e5029ed59d9f)

- RGW migrates bucket ACL and bucket owner information when migrating users to accounts. [commit](https://github.com/ceph/ceph/commit/dc4f7e5d7ebbe397560d7e465c6b7b4c1c3ee166)

- Fixed the OSD status query expression and status color mapping in the Grafana Cluster / Advanced OSD panel. [commit](https://github.com/ceph/ceph/commit/5766d500c012875d38d631d0adbbaaa65770c28f)

- Dashboard Prometheus integration now obtains credentials based on secure monitoring status and skips inappropriate requests; it also safely returns empty data when Prometheus is not configured, the response is empty, or the JSON is invalid. [commit](https://github.com/ceph/ceph/commit/f6d0fa2f043df8c0f5b4f9b11026fcddcd734409) [commit](https://github.com/ceph/ceph/commit/4689bb4a039ac33353fbf386d1e4feb6254ffebf) [commit](https://github.com/ceph/ceph/commit/3cdb8c2ff87676e1113b71890fce87cf4b618e6f) [commit](https://github.com/ceph/ceph/commit/2140a8fcbe862187c15bac80a39074bdb841271c)

- Dashboard CephFS mount instructions now use the correct mount data field, fixing the issue where `undefined` was displayed in the Attach Command. [commit](https://github.com/ceph/ceph/commit/f79cc7bfecf795c359f6cb9c06833e69d24c9ff3)

- Dashboard NVMe-oF command's `no_group_append` default value is aligned with the old CLI to `false`, and the optional `force` of `ns add_host` is allowed to be left empty. [commit](https://github.com/ceph/ceph/commit/5ba4b7cd2fd6bfe2e73e7b4de3dd642d6e9b9ed2) [commit](https://github.com/ceph/ceph/commit/80d160a4f4cfb49f863acbfaafc3003fae682408)

- OSD rechecks full status after receiving a new OSDMap while waiting for local or remote recovery reservation, avoiding recovery stalls. [commit](https://github.com/ceph/ceph/commit/d2225b28868bbbd693239e5a7139b9b43bbb076d)

- Fixed the blank display of Storage Capacity information on the Dashboard extended cluster audit page. [commit](https://github.com/ceph/ceph/commit/5e5b0fd9d169eb0e7c108c8ad23668f576e158ac)

- Fixed the PromQL expression for MTU inconsistency alerts and improved the display of related information in the Dashboard active alerts list. [commit](https://github.com/ceph/ceph/commit/2e75347958d499465a586581f4bf14cd66ef12d5)

- OSD now allows deletion of CephFS subvolumes with retained snapshots when full. [commit](https://github.com/ceph/ceph/commit/12100050a46f6b271cff33d1810aa827c2107f01)

- Dashboard alert view merges similar alerts and hides silenced alerts from the home page. [commit](https://github.com/ceph/ceph/commit/4701b11e1bc65591dcdbf60b5ab5d3be9b99dc1a) [commit](https://github.com/ceph/ceph/commit/caed5ffca7207cd7887c1d749d19ae1c7bddc2a5)

- When deleting a CephFS filesystem, the `join_fscid` of active MDS in other filesystems is preserved, avoiding incorrect clearing. [commit](https://github.com/ceph/ceph/commit/4a8ee645c90cded9eca9f9353402d022ed881abb)

- Fixed the issue where rank 0 was incorrectly marked as damaged when replaying only the remaining ELid events after shutdown log trim. [commit](https://github.com/ceph/ceph/commit/0a3445f2e83c93acc49f2b93a78b2a8f6c9123eb)

- Fixed the registration boundary of Dashboard NVMe-oF CLI/API commands, ensuring that API-only commands and CLI command aliases are correctly distinguished and registered. [commit](https://github.com/ceph/ceph/commit/c746e7f811ca5f5866ba781c786fa181bb504596) [commit](https://github.com/ceph/ceph/commit/e47b422ed4e04c0f924e55a21984a05c221cb3e8)

- Restored the OSD peering peer state update logic, fixing cluster statistics mismatch errors during scrubbing. [commit](https://github.com/ceph/ceph/commit/8f1ff0822cda1f4741fc3e7ed8626d2f33f72dc9)

- Dashboard now shows a loading state during pagination and limits rapid repeated page turns; search only submits the last entered keyword, avoiding repeated requests for each keystroke. [commit](https://github.com/ceph/ceph/commit/bb81d3366d5fb7785021bc20f8c2388b52a80996) [commit](https://github.com/ceph/ceph/commit/aa1b1eba918759a4631cf7d02768e8dcc03d6269)

- OSD relaxes the assertion for missing PG log entries during EC partial writes, accommodating cases where subsequent log entries still exist. [commit](https://github.com/ceph/ceph/commit/bb3c77d2f415fa2c00ab0459480b9760fb83a9b9)

- Dashboard safely reads navigation permissions when SMB permission data is missing, avoiding page freezes. [commit](https://github.com/ceph/ceph/commit/1520e3a2f52952a9133425233c32b3e5b38e4d22)

- Dashboard fixes the mirroring switch state when editing the RBD image form, and correctly updates/disables mirroring mode when changing pool or selecting namespace. [commit](https://github.com/ceph/ceph/commit/63e7555a1f3d877faf54047a46e6499ed2cc05e3) [commit](https://github.com/ceph/ceph/commit/90bdd0c640ba5597d33c9ba55ac8b6ad5a9822bb)

- Dashboard fixes the display of the image usage progress bar for secondary site RBD mirroring. [commit](https://github.com/ceph/ceph/commit/87fc968391636cf294cf878e71a5b21357ff564f)

- Fixed BlueStore ExtentMap reshard handling of cross-shard extent/blob, and ensured deletion operations cover the full dirty range. [commit](https://github.com/ceph/ceph/commit/6434621466f544d3427133c74db4db023699a4c8) [commit](https://github.com/ceph/ceph/commit/ff352acc227fef2c87796008bafabbc443d0b7e5) [commit](https://github.com/ceph/ceph/commit/726743eb93f355be7cd5ea16df5f0b066989a58a) [commit](https://github.com/ceph/ceph/commit/28e2b76b51ce21a8a986ae7ab1533e84c437a9d9)

- RGW lifecycle now checks delete marker expiration days based on object modification time, avoiding premature deletion of markers. [commit](https://github.com/ceph/ceph/commit/511205af30e254d40eab26313d52a7fdb067c05d)

- RGW conditional Delete and MultiDelete now check ETag, last modification time, and object size preconditions, supporting zero-byte and versioned objects. [commit](https://github.com/ceph/ceph/commit/f28f0d9147d79cf0e08dc0e953760b755cf0ee3f)

- RGW cloud-S3 restore state is now persisted so that ongoing tasks can resume after service restart; retrying restored objects updates the temporary copy expiration time and fixes the initial enqueue state. [commit](https://github.com/ceph/ceph/commit/050c591e1b5316875b661674a972424024a437bf) [commit](https://github.com/ceph/ceph/commit/6d3f151dc2d8c1b6fae1ecd0c50875b25fc24c25) [commit](https://github.com/ceph/ceph/commit/d37b70f4c73b2a6dd183cb351a2961c6b3ae1af1) [commit](https://github.com/ceph/ceph/commit/2799cfe2bba1944eec5a2c3d865dc149dc2fcab2)

- RGW now correctly enqueues old objects into the GC queue when overwriting objects. [commit](https://github.com/ceph/ceph/commit/8045fe66e9e480755b1c75b4b1382da070caa1a1)

- Dashboard RGW multisite wizard can now select an existing realm that meets the conditions for replication configuration. [commit](https://github.com/ceph/ceph/commit/ae895062fd1cd70ebbfed457add75c31eba3e051)

- Fixed the metric unit display in CephFS and SMB Grafana dashboards. [commit](https://github.com/ceph/ceph/commit/917433784522895f1294a001679b7d1f984d9b51) [commit](https://github.com/ceph/ceph/commit/97002532ca93e8a714e9f7c736a84a1320bbc37a)

- cephadm now mounts the Loki data directory to a persistent volume, avoiding data loss after container restart. [commit](https://github.com/ceph/ceph/commit/0cb9acf8f4098219240ef7c24f5bb8be1ad1d4c4)

- Dashboard RBD API timestamps now uniformly use datetime values with UTC timezone, avoiding old timezone-less formats and deprecated time APIs. [commit](https://github.com/ceph/ceph/commit/d6282398de584baa74b7a57e832163f4c8b95521)

- Dashboard fixes the creation error when the OAuth2 service does not fill in the allowlist domain. [commit](https://github.com/ceph/ceph/commit/b52504abcba2ac9cab046b4c973f2e7807f18d5c)

- Dashboard now uses default values when editing an RGW user without rate limit configured, avoiding server errors in interface requests. [commit](https://github.com/ceph/ceph/commit/0675ff6f1e7c847a2b1451da72801eb7af01b797)

- Fixed `radosgw-admin object unlink` handling of unsharded bucket index (shard count 0, actually containing one shard). [commit](https://github.com/ceph/ceph/commit/8ecc59e4c406a40c9d6c088255c60e624b8fdfeb)

- CephFS client's `dump_mds_requests` output is now valid JSON, avoiding duplicate `request` keys. [commit](https://github.com/ceph/ceph/commit/69b8e4b238fdf8deec12d2a25a30e466ac954dd7)

- RBD mirroring can now continue syncing incomplete demote snapshots after restart on the secondary. [commit](https://github.com/ceph/ceph/commit/d8f73e67894cb0dabb28d4258b32536f77f2c0a9)

- OSD scrub now correctly calculates object size based on the object backend and fixes minimum chunk handling during preemption; added performance counters for scrub blocking and I/O preemption. [commit](https://github.com/ceph/ceph/commit/e2c5630b0b2fbfe3cf23ed9832f93984bfb4aabb) [commit](https://github.com/ceph/ceph/commit/cdd5bd59e7f205b6f3a3cba8b25f8b05399d383d) [commit](https://github.com/ceph/ceph/commit/b10444054abecbb9080d8eb0ec97594025978741) [commit](https://github.com/ceph/ceph/commit/776716ace38456bff1ccde6f787948ffe655913e)

- NVMe-oF Overview dashboard now uses cephadm daemon status metrics to accurately display stopped gateways. [commit](https://github.com/ceph/ceph/commit/e39795d9f7667d04d9eb14bc541008d6613c8bcb)

- Fixed the issue where `cephadm version --verbose` could not list the contents of the zipapp root directory. [commit](https://github.com/ceph/ceph/commit/6f19802fb457b66e60f81a1e4a545944a5f87cee)

- Dashboard About modal tooltip now has the correct positioning container and no longer displays abnormally. [commit](https://github.com/ceph/ceph/commit/457c7b74cb981c3a3bea6e9a664a09d26d8db32d)

- Dashboard NVMe-oF subsystem maximum count default changed to 512, and removed frontend hardcoded validation that varied with gateway version. [commit](https://github.com/ceph/ceph/commit/f0d73f1b8e79e61e8025d1a66d5b5381bd37aa14)

- Dashboard now hides duplicate sub-alert details when the same alert contains multiple sub-alerts. [commit](https://github.com/ceph/ceph/commit/9b336e2c49b21cfcb88f6de406f88b13b34418f8)

- RBD mirror remote metadata cache key now includes the cluster FSID, avoiding conflicts when mirroring multiple clusters with the same pool ID. [commit](https://github.com/ceph/ceph/commit/006e887359b305507e1bbe9133d33200bf2a5fc2)

- Dashboard fixes the illegible text label in the menu overflow control. [commit](https://github.com/ceph/ceph/commit/25446489004b2f378cc7c603a4d0156f3297ae31)

- Fixed `ceph pg repeer` proposing replica counts matching the pool for PG temporary mappings. [commit](https://github.com/ceph/ceph/commit/d5d37bcf35617898c872aa041b217bc5d96d8a22)

- Fixed the issue where the group mode disable option in the Dashboard RGW account form did not take effect. [commit](https://github.com/ceph/ceph/commit/f4879b87ba5f1abd210008d763f0ce4a80efeb08)

- Fixed the issue where the `bytes_written_slow` performance counter was always 0 when BlueFS uses aio_write. [commit](https://github.com/ceph/ceph/commit/b23d203ddf2d12f1318fe5f43a87f440f202c231)

- Fixed the issue where the Dashboard CephFS Authorize Modal could not correctly save when updating authorization information. [commit](https://github.com/ceph/ceph/commit/a9df5d09c37561b7da8aa36213d91737eb947e28)

- Fixed the issue where `radosgw-admin bucket rm --bypass-gc` incorrectly handled tail object reference counts when deleting replicated objects. [commit](https://github.com/ceph/ceph/commit/515f7341ec8a2a812553fb203750124a2aeb13b4)

- Dashboard now allows service names to be the same as service types when creating services. [commit](https://github.com/ceph/ceph/commit/658bc5211d43dd1cc1614e99f0a0113e4d60f2ae)

- Fixed the route reload logic in the Dashboard multi-cluster view. [commit](https://github.com/ceph/ceph/commit/e1678d27040b7da395da4b81f537b632fdb18473)

- `ceph_objectstore_tool` identifies `get-attr` as a read-only operation. [commit](https://github.com/ceph/ceph/commit/02e4c2d87d63fe23141f6f269695b057ede68b7c)

- Fixed `frag_t` network/storage byte order conversion and can now recognize corrupted values caused by old byte order; MDS structured output returns dirfrag as an object. [commit](https://github.com/ceph/ceph/commit/8b9320f27156c2a4ae68d66caac78a7387af7ed9) [commit](https://github.com/ceph/ceph/commit/191aa45e8077cad5daf355725bfbfcf755a02e63) [commit](https://github.com/ceph/ceph/commit/761ca316f885f340fd77e94b72c1c9b50439066d) [commit](https://github.com/ceph/ceph/commit/73fd7c009c058a4e45ce74abfcf8ca28ad5ae7d6)

- Fixed the issue where EC fast truncate triggered key-not-found when the length was exactly a full stripe. [commit](https://github.com/ceph/ceph/commit/2a4e41d64fb15d7dfa12e45a1bd57fa17ea7b5a9)

- Fixed the use of incorrect structure types in BlueFS/BlueStore encoding debug macros. [commit](https://github.com/ceph/ceph/commit/7fc9412525406d50b6fa586ee34525eaf9d9bc99)

- Fixed issues with Dashboard host label editing and form label handling. [commit](https://github.com/ceph/ceph/commit/930bbe251338a5bf60e5d6a1363522cac16a7676)

- Restored OSD compatibility with write requests carrying both `balance_reads` and `rwordered` flags. [commit](https://github.com/ceph/ceph/commit/cbed99dcc30f16ce00127fc48b91dc7a8419792f)

- Fixed librbd `ExclusiveLock::accept_request()` returning an error rejection reason when the lock is not in a stable held state. [commit](https://github.com/ceph/ceph/commit/d24d4f0f8d2b348b549db937b8715da67d5e25a6) [commit](https://github.com/ceph/ceph/commit/d605db04d3ab7d543d2f46d6060618ed8c04412a)

- OSD no longer incorrectly deletes objects when encountering divergent logs in partial writes scenarios. [commit](https://github.com/ceph/ceph/commit/4a93e92cd77c33f2dfa58d306217f7a9cecc9506)

- Fixed the CephPGImbalance alert expression to consider OSD device class, avoiding false positives in mixed-capacity disk scenarios. [commit](https://github.com/ceph/ceph/commit/be72a9d9147719464e6eb880d259ce31cd69429d)

- systemd installation now correctly generates and installs the `ceph-volume@` service unit. [commit](https://github.com/ceph/ceph/commit/a3d1b8de00616b2b80313cc505a0ff08b7ea96bb)

- Fixed concurrency between MonClient's `tick()` and shutdown flow, avoiding shutdown races. [commit](https://github.com/ceph/ceph/commit/35ca4c81ce96d21df58d8b5725ea174f5caee322)

- Fixed Objecter map subscription overriding higher epoch subscriptions, avoiding OSD preboot hanging while waiting for the wrong map. [commit](https://github.com/ceph/ceph/commit/e1a1815bbac15d171e40591a0cb62cc65bbb1d99)

- Fix memory growth caused by EC idle PG generated `ECDummyOp` not being reclaimed in time. [commit](https://github.com/ceph/ceph/commit/cff98c4e5a3f6b48760ac57a083e0d094f64c984)

- Grafana dashboard matcher is compatible with historical Prometheus metrics that lack the `cluster` label before the upgrade. [commit](https://github.com/ceph/ceph/commit/8ae4f82b58210f07986ce0ebb394b53bcd0e6679)

- Fix the daemon filter condition in the RGW Sync Overview dashboard. [commit](https://github.com/ceph/ceph/commit/51f292fd314fab027df4f8c7ce06b85402553d24)

- Fix the inheritance order of the Dashboard RBD mirror schedule API so that image, pool, and cluster schedules are correctly returned by hierarchy. [commit](https://github.com/ceph/ceph/commit/abf7f7cbdc03bc8a30fb557d1c2f577dee72940e)

- When OSD peering merges object logs from non-primary shards, if the primary shard's clone update is not reflected on the peer, mark the PG statistics as invalid and recalculate after recovery; also add an invalidation counter to facilitate observation of related statistics invalidation. [commit](https://github.com/ceph/ceph/commit/30c5de8ae202b227c474d2684d09a0d9db43aa7f) [commit](https://github.com/ceph/ceph/commit/d67279ab83ac0d4360383afd1e46dab7746768ac)

- Fix the IP address display issue on the Dashboard host page. [commit](https://github.com/ceph/ceph/commit/cc60143c59eaa07a906183219d2e5a31bbdc8779)

- Fix the error in the read-offset range length calculation for EC shard extent cleanup, avoiding objects smaller than the stripe width leaving shard data that should have been cleared during recovery. [commit](https://github.com/ceph/ceph/commit/09c8fbd2e8d1c92da0b5f9e4dfff1026785e3118)

- MON refuses to enable fast EC optimization for EC pools whose chunk size is not aligned to 4 KiB, avoiding known problematic encoding configurations; related default enable requests are also ignored. [commit](https://github.com/ceph/ceph/commit/1195a583d829c6b706df111159cc5c02172a2f88)

- Fix the issue where the actual file size is not updated after indexing the BlueFS WAL envelope file, so that `stat()` returns the correct file size. [commit](https://github.com/ceph/ceph/commit/ebb9a4edd44d04c24e0222b3a751f05cd3cce0b7)

- Fix the issue where BlueFS does not synchronize volume selector usage after recovery from the WAL envelope, avoiding inconsistency between selector state and the recovered file size. [commit](https://github.com/ceph/ceph/commit/20b6ce66d30ebabaedf4b31334a8b17bdc179dc6)

- Withdraw the incompatible NVMe-oF beacon feature-bit change to avoid Monitor crashes during cluster upgrades due to feature negotiation. [commit](https://github.com/ceph/ceph/commit/ddef0d1e6cc6de05f4cb424d4ff0f00c4d30fc18)

- Determine the ISA EC plugin build option before processing common/options configuration, fixing the issue where the default `osd_erasure_code_plugins` configuration misses the ISA plugin on first build. [commit](https://github.com/ceph/ceph/commit/51a0c2a3db38178def99d05715e958fb88fa0493)

### Refactoring

- The manager delegates TLS certificate verification, certificate generation, and password hashing to a standalone `ceph.cryptotools` helper; uses structured JSON communication, optional crypto caller, and unified error handling to avoid repeated PyO3 module initialization and correctly report TLS verification errors. [commit](https://github.com/ceph/ceph/commit/8ba69fff36136fd7ffddea77b64607ff32ca30c5) [commit](https://github.com/ceph/ceph/commit/370e2a5b769fee26ca9e8043eea4212199073637) [commit](https://github.com/ceph/ceph/commit/9d40424a7aec78fc5558e47fdbf8ab072b3d9c83) [commit](https://github.com/ceph/ceph/commit/c84301afe93484dcd97b5a668382ce398aacdb7f) [commit](https://github.com/ceph/ceph/commit/574faf578fddb49a2ba2c40eb1ad6b10b968866b) [commit](https://github.com/ceph/ceph/commit/f5bde031df24cce9d7ebfc231e1c65b9027b7de2) [commit](https://github.com/ceph/ceph/commit/89538405082cb4df69e4de3c9f80be72b862dd56) [commit](https://github.com/ceph/ceph/commit/824be4ca0d58455bb828e04d9ddf21b78d24f840) [commit](https://github.com/ceph/ceph/commit/1a0ae2871175644b8e9e1ed5ee220e6311a3ba56) [commit](https://github.com/ceph/ceph/commit/4ff3d4e53d6646108519460fac51bffbcd544a02) [commit](https://github.com/ceph/ceph/commit/fa209addb865c0b00f7a20cd140985116c33a7e2) [commit](https://github.com/ceph/ceph/commit/fd6a72a1831b6aaab64caa74fb83756df854d66b) [commit](https://github.com/ceph/ceph/commit/f9b897406f1b5d5e7ebae09252d562b543c6f0e0) [commit](https://github.com/ceph/ceph/commit/f83d383889288d4ee81d8b7d48752d0ac6ddf4fe) [commit](https://github.com/ceph/ceph/commit/ea218346f36454f8b06924a082a0ca2a008c8821) [commit](https://github.com/ceph/ceph/commit/16d8eed1881a8ad9d7dda0459033e78dd239025f) [commit](https://github.com/ceph/ceph/commit/20ddf9b5f9e11ac2acfa920dbc179182078817cc) [commit](https://github.com/ceph/ceph/commit/89c1814d2868bb1f72e430ca05b208d4f03ce2a5) [commit](https://github.com/ceph/ceph/commit/ca9d971e3b141d4c065852a90592627f61b89a37) [commit](https://github.com/ceph/ceph/commit/e1949ed6b6321a82d63212950b659c05fcd397a1) [commit](https://github.com/ceph/ceph/commit/6f45a56fc16e1aae072ec7e9449fa0712a02b532)

### Tests

- Add NVMe-oF upgrade QA suite covering gateway/initiator cluster deployment, upgrade steps, and post-upgrade workloads. [commit](https://github.com/ceph/ceph/commit/55e29b4eea741dc9b3e356f81077e7b7a49f67df)

### Performance

- Shorten the time the Manager holds the shared lock when querying DaemonStateIndex: first copy the index data, then execute the callback outside the lock. [commit](https://github.com/ceph/ceph/commit/2d227ab51fd72313fb359a0bf7b53722fe793fbc)

- RGW multi-object delete batch deletion only updates the OLH object on the last item, reducing duplicate index updates. [commit](https://github.com/ceph/ceph/commit/0e13c8740c20067baaffcdd4d3a3c28f490e7bd9)

- Monitoring dashboard uses `rate()` and `$__rate_interval` to improve chart precision across different time ranges, and restores the automatic sampling point count to 10. [commit](https://github.com/ceph/ceph/commit/4111a5c1090ccde14a99e29de17bcff037cdceae) [commit](https://github.com/ceph/ceph/commit/52773af2e10ec3387bfcebf21f64d606ebc38466)

- ceph-volume uses udev data to determine whether a disk belongs to LVM, avoiding starting LVM subprocesses when scanning each disk; and correctly handles empty udev data files. [commit](https://github.com/ceph/ceph/commit/05e8672887d61a0fa3c4f78bbe5b1c9294607a60) [commit](https://github.com/ceph/ceph/commit/8ac65948b9d167fd9cfc3548c63d1e405c593813)

- NVMe-oF gateway monitor timer uses absolute time and corrects drift to maintain a stable polling frequency. [commit](https://github.com/ceph/ceph/commit/411a493a0cdbdd8b3f3a2b1fb8b06453422a0210)

- PG autoscaler dynamically adjusts the scaling threshold based on the target PG count, making it more sensitive for small pools and more robust for large pools. [commit](https://github.com/ceph/ceph/commit/b907e0b2ebf001b67f0e7d1851d1415576d46a07)

- NVMe-oF gateway beacon supports sequence-number-based delta updates; Monitor validates order and is upgrade-compatible, and ignores late beacons from deleted gateways to avoid state graph corruption. [commit](https://github.com/ceph/ceph/commit/3b5d28bfa51e3bf024ee0d66acd5cf6eec78eb52) [commit](https://github.com/ceph/ceph/commit/d87ff9590be3ea91514c8e7b5b868f124597a6bf) [commit](https://github.com/ceph/ceph/commit/5467ad93a5bfbe6dfb73e585111a21003acabe91) [commit](https://github.com/ceph/ceph/commit/5059a1b8457da0f53e6a60f5a1e9b7d9ef1def56)

- NVMe-oF gateway speeds up failover detection: default beacon interval shortened to 1 seconds, failure detection grace period adjusted to 7 seconds, and timeout checks when processing beacons. [commit](https://github.com/ceph/ceph/commit/5dacff4c136cd9eac02b623044467f1a0d5e0683) [commit](https://github.com/ceph/ceph/commit/724b09262bb7d39b04d1aca06d73e516b30f747a)

### Security

- Pin the GitHub Actions checkout used by the QA symlink workflow to an immutable commit SHA. [commit](https://github.com/ceph/ceph/commit/2e73bd34e14441f7ce2da823f15a6c4cf367745a)

- Alert emails establish TLS connections constrained by SSL context via `SMTP_SSL`, fixing a disclosed security issue. [commit](https://github.com/ceph/ceph/commit/1167b9de50c8e79e8f3d09014e4d78004abf7547)

- Dashboard upgrades validator frontend dependencies to fix known security vulnerabilities. [commit](https://github.com/ceph/ceph/commit/bbc8af8e94f3588907e5b25bd4b7f26bd74ce01e)

### Documentation

- Expose and document the `rbd_default_clone_format` configuration option, explaining the differences between clone v1 and v2. [commit](https://github.com/ceph/ceph/commit/e6bd2d07e5e0b922f3599398f606c4c167075b97)

- Correct the documentation for CephFS `pause_purging` and `pause_cloning` configuration options. [commit](https://github.com/ceph/ceph/commit/d5172c7100c7915ca0e0304474a50f7989052262) [commit](https://github.com/ceph/ceph/commit/4e15e0c9d1cfee471449380992b72aa1e4f6303a)

- Update the supported operating system recommendation table, remove distributions that have ended support, and list systems currently supported by Tentacle. [commit](https://github.com/ceph/ceph/commit/901b52277573af79d7f88094521c4b2eced44f7f) [commit](https://github.com/ceph/ceph/commit/6b06788d6eeb15e393bd14fefa10d6acbc6f51df) [commit](https://github.com/ceph/ceph/commit/3724ce801ca52bcff01662e16289797f219762b5) [commit](https://github.com/ceph/ceph/commit/38bf3ba891eb02ab2ec8cd489224c9109578a140) [commit](https://github.com/ceph/ceph/commit/94f66c66bd86618ca96d4d56cb60b9f794e27576) [commit](https://github.com/ceph/ceph/commit/61b9bb5be4890076a66ae6fa02048eb3d2a31131)

- Adjust Sphinx documentation build dependencies to remove the seqdiag extension incompatible with newer setuptools; documentation build prioritizes reading release status data from the main branch, falling back to local files on network access failure. [commit](https://github.com/ceph/ceph/commit/5f53ebc5686202b938008c58abab5579445f7fa6) [commit](https://github.com/ceph/ceph/commit/442b409177632d31372fb9f265c2bad8a7fc2b92)

### Build / CI

- cephadm RPM build no longer depends on `top_level.txt` from wheels, and adds build container coverage for CentOS Stream 10, Ubuntu 24.04, etc. [commit](https://github.com/ceph/ceph/commit/fdc1b9a80f3af7bc11ba46226d1399903e220d5f) [commit](https://github.com/ceph/ceph/commit/0148b5f146718e5df2a11534418748be8fb9e4b9) [commit](https://github.com/ceph/ceph/commit/eda0d5b64217df2ec0f97716561c64465aeda890) [commit](https://github.com/ceph/ceph/commit/3441c109f3d371c78797f2959a4cb0f91b8319d6) [commit](https://github.com/ceph/ceph/commit/b79cc22ac73b407759f72acfa06271957d9ecc3d) [commit](https://github.com/ceph/ceph/commit/349b9415a7848d51336c70cb5b53a62287a753aa)

- cephadm Tentacle default container image switched to `quay.io/ceph/ceph:v20`. [commit](https://github.com/ceph/ceph/commit/028de28ce6d4430bde331189e58feae903562f7d)

- RPM build defaults to GCC toolset 13 (EL10 uses system GCC), requires GCC 13.3 in applicable environments to restore LTO, and switches to Python RPM shebang macro to support EL10. [commit](https://github.com/ceph/ceph/commit/e027fef7f9d076d3cdd39ab7c618ce77694ead94) [commit](https://github.com/ceph/ceph/commit/f1cbe2dee92547a0153f39cfbee34b7614cc64ea) [commit](https://github.com/ceph/ceph/commit/865274f898bdce04645db7bacc8d29e0e422f08e) [commit](https://github.com/ceph/ceph/commit/13f1279a66e533eaa17295e891d52659d6b913f0) [commit](https://github.com/ceph/ceph/commit/c6440bb47d0872b8641af5e9915e5e61337635a2) [commit](https://github.com/ceph/ceph/commit/8752d7dc4e3c62c7ec31f1592d6674a2a8361b36) [commit](https://github.com/ceph/ceph/commit/0a8676911e2cf7d521ecd99988f71064cfa805a1)

- build-with-container fixes the initialization order of the npm cache directory, supports Debian Bookworm, Trixie, Ubuntu Focal, and newer Fedora, and gives readable errors for invalid distribution arguments. [commit](https://github.com/ceph/ceph/commit/6acdbeb7f1f69df1c3d48a70a8abd87486d1a248) [commit](https://github.com/ceph/ceph/commit/edef7081064ede1534121e822fbe218aca8cc803) [commit](https://github.com/ceph/ceph/commit/326869e2eda73395bb6d8123807dbd1cba1f107b) [commit](https://github.com/ceph/ceph/commit/71441f924da940136cdc3e5e6d20cb1b247b0c34) [commit](https://github.com/ceph/ceph/commit/72de801c315cc3d292b2acfa2d0ebb119b192f79) [commit](https://github.com/ceph/ceph/commit/7dc6566635432c93d7680785f865f5a17113b831) [commit](https://github.com/ceph/ceph/commit/9fb5174282973b52e321c4b00d6ece2a5121aef3) [commit](https://github.com/ceph/ceph/commit/eaffd777fd163dd8698c3ec776de67302fa9292a) [commit](https://github.com/ceph/ceph/commit/0250f261df68ba67f4cc1dc6e98ce05686763ba8) [commit](https://github.com/ceph/ceph/commit/5f95944fc2b5f7f0bb0befe02b5f13cb816bcd6c) [commit](https://github.com/ceph/ceph/commit/2a2abf1bbf19296167abc8e9f518f5ec2632256d) [commit](https://github.com/ceph/ceph/commit/9b635c8b943179d00e0e6ae656c4cc215d55dac5) [commit](https://github.com/ceph/ceph/commit/6a904557d92ba1579bdea5a2f995bb881f45aa59)

- Build containers support on-demand installation of make-check dependencies, selection of minimal/crimson image variants, and improved sccache, Docker compatibility, and Debian/Ubuntu compiler installation. [commit](https://github.com/ceph/ceph/commit/503ec0c294c49a32d958e6e5a093efc6c8f92434) [commit](https://github.com/ceph/ceph/commit/bf35cf87637c7aa622a5a1f144a69b4496a9cfc3) [commit](https://github.com/ceph/ceph/commit/2b190179037c031560a8bb41f71a04d44626e87d) [commit](https://github.com/ceph/ceph/commit/56396e14da9730563a656644db083630fa32bb44) [commit](https://github.com/ceph/ceph/commit/a628348e9677d6a9991129f47b4e7fa1427cc117) [commit](https://github.com/ceph/ceph/commit/e3550d6fe95b02f19d2f3d52c3649023af7e158a) [commit](https://github.com/ceph/ceph/commit/4ab5a5eb4ca862c92090b0c037fe17642559d815) [commit](https://github.com/ceph/ceph/commit/603e8875493a6ca834e69abe34015d24941ff335)

- Read the Docs build pins pip to `<25.3` to avoid pybind documentation build compatibility issues. [commit](https://github.com/ceph/ceph/commit/8dc9af74bfe58cca649d27bf46b1b6273fe852e5)

- CMake automatically detects Arrow's xsimd dependency and completes dependencies for Debian package builds. [commit](https://github.com/ceph/ceph/commit/b4fa423669675bcf800fc42c0920207fa2ee5f68) [commit](https://github.com/ceph/ceph/commit/e64dc861c008d9f05dd208b7f32188fba6a81e06)

- cephadm Debian build supports packaging dependencies directly from system Debian packages, suitable for restricted network environments without access to PyPI. [commit](https://github.com/ceph/ceph/commit/248295a89d3f4b72e4928ea88e03140d51fe25ee) [commit](https://github.com/ceph/ceph/commit/9d1fd077e8d45326477d12ee5b0492da5f2215e4)

- Debian's ceph-volume package adds `python3-packaging` runtime dependency. [commit](https://github.com/ceph/ceph/commit/45b4470b0edd9504a1b3cd4ad962e1d95c251c90)

- Build dependencies switch to TLS-enabled apt mirror and complete `iproute2` dependencies required for Debian builds. [commit](https://github.com/ceph/ceph/commit/b40768ff5bdc0b00792ed86cdfd64e6c97c78b1c) [commit](https://github.com/ceph/ceph/commit/b56db22597157753d3b4e0e2b0dd76b0ca103f64)

- Fix RHEL version detection condition in RPM build. [commit](https://github.com/ceph/ceph/commit/bdfef2d0a4690d0ad59c66a1cdd1ee934e3bb4b1)

### Maintenance

- MDS session dump adds `auth_name` field to facilitate viewing the authenticated user corresponding to the session. [commit](https://github.com/ceph/ceph/commit/8ad2d96dfb143408eec9de6b7eab817f2ae5202e)

- Dashboard updates Topic, Tiering, and Users names in RGW navigation, and fixes list refresh after Storage Class deletion. [commit](https://github.com/ceph/ceph/commit/79c4abd9a2521fdb6a373eb205d5a3a74d04e417)

- Dashboard removes duplicate time picker outside the Grafana iframe. [commit](https://github.com/ceph/ceph/commit/fe218974727d3f4b79c272e90fe15d60e3b5a4e4)

- cephadm updates default versions of Prometheus, node-exporter, Alertmanager, and Grafana (later Grafana updated to 12.3.1). [commit](https://github.com/ceph/ceph/commit/bf1e40e580e54904f27e12ff7f4e11fd1c547495) [commit](https://github.com/ceph/ceph/commit/f7b67ad29908bde9ccefa3b4a4e674a3c8f77f0c)

- Dashboard's Report an Issue modal completes Carbon component adaptation, fixing feedback form display and interaction. [commit](https://github.com/ceph/ceph/commit/f02d94efdfc64636371053be7d85b745cd427e50)

- cephadm disables Grafana's online update check for offline environments. [commit](https://github.com/ceph/ceph/commit/3878143bfe199031972af42155696d2a85b92e2f)

- Dashboard RGW multisite sync policy form adapts to Carbon components and fixes related form interactions. [commit](https://github.com/ceph/ceph/commit/257ba5a7a1e3135857e3c42b78fceeaad1fde996)

- Dashboard Change Password form migrated to Carbon components. [commit](https://github.com/ceph/ceph/commit/c00dfd275b0ca5abd16ef72663818a8a65c59ccc)

- Dashboard global status badges migrated to Carbon Tags, unifying badge display in cluster, CephFS, RBD, RGW, and alert lists. [commit](https://github.com/ceph/ceph/commit/ce6b0c34905d52bcb2950695b832f88cdb39ef22)

- MDS status output adds system information including CPU architecture and byte order. [commit](https://github.com/ceph/ceph/commit/46c3b2170e1b598fb3a36a4a05608df965a41b68)

- Dashboard shows clear empty state prompts when NVMe-oF gateway, namespace, and subsystem lists have no data. [commit](https://github.com/ceph/ceph/commit/0aad65395d50512c61dea167b28fb5b4b6630c85)

- Dashboard forms use a common validation directive and uniformly display validation errors. [commit](https://github.com/ceph/ceph/commit/19b7bbeca04518a62e60e7c252b0d0de95c1c645)

- NVMe-oF service defaults to allowing up to 16 hosts per namespace. [commit](https://github.com/ceph/ceph/commit/4aa3cdfadb7487e4e7723993dd6f9ff25b94eace)

- Update the NVMeoFTooManyNamespaces alert threshold from 2048 to 4096 to match the supported number of namespaces. [commit](https://github.com/ceph/ceph/commit/2e9b72f4f01c48a83df04897833db723e0c08a8d)

- Dashboard RGW multisite zone delete/create forms and common service forms migrate to Carbon components; use Carbon meter chart to display usage/progress, and fix related table displays. [commit](https://github.com/ceph/ceph/commit/8477dc0566688ed1430bd515841b579ae3de70ab) [commit](https://github.com/ceph/ceph/commit/fa25dd415b22339411a89593a74f80c82941b7f7) [commit](https://github.com/ceph/ceph/commit/ad20f870e7717c476e69004ece45edd0850d99d3) [commit](https://github.com/ceph/ceph/commit/0879475a23bbaecb052410bd00a588934204ade9) [commit](https://github.com/ceph/ceph/commit/d119c0fb492731ad8f551f78499fdf7b837198ba) [commit](https://github.com/ceph/ceph/commit/e103a874df18f4a15e62cfe152659994c20a27de) [commit](https://github.com/ceph/ceph/commit/70f3f3fc57673451928f426c32e2513ed3e42911)

### Others

- Dashboard NVMe-oF CLI commands output JSON in indented format for easier viewing of command results. [commit](https://github.com/ceph/ceph/commit/69d36b230c41e3e474a37f1af9185a025cde4242)
