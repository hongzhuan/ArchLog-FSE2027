# Release Note

## Important Changes

### Distribution & Logic Layer

- Allow disabling the default always-enabled Manager module via Monitor configuration; add corresponding enable/disable tests. [PR](https://github.com/ceph/ceph/pull/60563)
- The CephFS volumes module adds pause/resume mechanisms for asynchronous tasks and provides `pause_purging`, `pause_cloning` configurations to control purge and clone work. [PR](https://github.com/ceph/ceph/pull/62436)
- Added `mds_allow_async_dirops` configuration to enable or disable asynchronous directory operations; the same group of fixes avoids repeatedly acquiring write locks for a single request. [PR](https://github.com/ceph/ceph/pull/61839)
- Added `mds_allow_batched_ops` configuration to control batch operations; also added a warning log for unstable locks after early replies. [PR](https://github.com/ceph/ceph/pull/64540)

### Interface Layer

- RGW’s S3 `GetObject` supports the `partNumber` parameter to read a specific part of a multipart object; the response also returns the corresponding part information. [PR](https://github.com/ceph/ceph/pull/62544)
- RGW STS extends Web Identity JWT validation: supports `n`/`e` signature verification using RSA JWK, prioritizes keys by signing purpose, and allows configuring JWKS URL certificate verification; when the token lacks `aud`, uses `client_id`. [PR](https://github.com/ceph/ceph/pull/63053) [PR](https://github.com/ceph/ceph/pull/64937)
- Added `ceph auth rotate` command to rotate authentication keys for a specified entity. [PR](https://github.com/ceph/ceph/pull/58236)
- Stretch mode adds `disable_stretch_mode` command to exit stretch mode; accompanying documentation and tests cover the exit process. [PR](https://github.com/ceph/ceph/pull/60630)
- `ceph fs volume create` supports specifying metadata pool and data pool; when the caller passes self-created pools, the creation process retains these pools and no longer deletes them. [PR](https://github.com/ceph/ceph/pull/63069)
- Added subvolume snapshot path query command `subvolume snapshot getpath`, and supplemented command documentation and tests. [PR](https://github.com/ceph/ceph/pull/62917)
- `radosgw-admin object rm` adds `--force` option to explicitly request forced object deletion in the command. [PR](https://github.com/ceph/ceph/pull/64311)
- Added OSD management command `clear_shards_repaired`, and explained its purpose in the health check documentation. [PR](https://github.com/ceph/ceph/pull/60566)
- cephfs-shell adds an operation to remove extended attributes, and adds corresponding tests. [PR](https://github.com/ceph/ceph/pull/62409)
- Dashboard’s service creation form adds NVMe/TCP (`nvmeof`) service type, and includes its required pool fields in validation and service specification submission. [PR](https://github.com/ceph/ceph/pull/63304)

### Storage Backend Layer

- BlueStore adds an optional `hybrid_btree2` allocator and reorganizes related allocator implementations into reusable components; adds corresponding tests and benchmark code. [PR](https://github.com/ceph/ceph/pull/62539)
- The kernel block device asynchronous discard queue adds a pending range limit (`bdev_async_discard_max_pending`, default 1,000,000, 0 means unlimited); when the queue is full, items are not enqueued and the range is returned to the allocator. Related commits also restore compatibility mapping for the old `bdev_async_discard` parameter, and add discard counters and thread count metrics. [PR](https://github.com/ceph/ceph/pull/62220) [PR](https://github.com/ceph/ceph/pull/62481) [PR](https://github.com/ceph/ceph/pull/62152)
- mClock adds recovery throttling configurations differentiated by whether a PG is degraded: `osd_recovery_sleep_degraded`, `osd_recovery_sleep_degraded_ssd`, and `osd_recovery_sleep_degraded_hdd`, used to control data movement rate during degraded recovery. [PR](https://github.com/ceph/ceph/pull/62399)

## Routine Changelog

### New Features

- Added Manager `status` command, and added tests for this command. [PR](https://github.com/ceph/ceph/pull/62505)
- Enhanced Monitor’s historic ops command output and improved its error handling. [PR](https://github.com/ceph/ceph/pull/64843)
- Added MDS Admin Socket command `dump_export_states` to export subtree export status, and added tests. [PR](https://github.com/ceph/ceph/pull/61512)
- S3 `PutObjectLockConfiguration` can now enable Object Lock for existing, versioning-enabled buckets. [PR](https://github.com/ceph/ceph/pull/62063)
- RGW bucket notification can send messages to Kafka clusters configured with multiple brokers, and adds failover tests. [PR](https://github.com/ceph/ceph/pull/61825)
- Enhanced `rgw-restore-bucket-index`: supports additional parameters and multisite specification, and improves exception recovery and temporary directory usage; added man page and package installation configuration. [PR](https://github.com/ceph/ceph/pull/64514) [PR](https://github.com/ceph/ceph/pull/64622)
- RGW IAM policy adds Arn condition evaluation and keeps ARN matching case-sensitive. [PR](https://github.com/ceph/ceph/pull/62434)

### Bug Fixes

- Validate the path before updating a CephFS NFS export, rejecting invalid CephFS paths; added negative test cases. [PR](https://github.com/ceph/ceph/pull/62278)
- Dashboard’s RGW overview now displays sync status for non-default realms. [PR](https://github.com/ceph/ceph/pull/65002)
- Fixed the issue where Dashboard forced storage class to `STANDARD` when updating an RGW zone. [PR](https://github.com/ceph/ceph/pull/65621)
- Fixed Dashboard's cluster_mgr Prometheus read permission, and corrected Dashboard role permission related display logic. [PR](https://github.com/ceph/ceph/pull/62651) [PR](https://github.com/ceph/ceph/pull/62455)
- Added `ceph_daemon` filter condition to RGW overview Grafana panel queries to avoid cross-daemon aggregated display. [PR](https://github.com/ceph/ceph/pull/62268)
- `ceph node ls` no longer lists destroyed OSDs. [PR](https://github.com/ceph/ceph/pull/62326)
- After Monitor election completes, it tracks and processes ping backlog accumulated during election. [PR](https://github.com/ceph/ceph/pull/62925)
- In stretch mode, when monitors are located in a non-existent CRUSH bucket, added `NONEXISTENT_MON_CRUSH_LOC_STRETCH_MODE` health check and ignore non-existent buckets. [PR](https://github.com/ceph/ceph/pull/62040)
- Ensure `pcm` is initialized when initializing OSD map, fixing issue in Monitor memory target handling path. [PR](https://github.com/ceph/ceph/pull/63805)
- Corrected PGMap calculation of pool capacity and available space, removed logic that scaled `max_avail` by degraded replica ratio. [PR](https://github.com/ceph/ceph/pull/61320)
- Fixed time difference direction in OSD recovery queue delay counter to avoid negative delay metrics. [PR](https://github.com/ceph/ceph/pull/62801)
- OSD startup message no longer carries stale heartbeat messenger address. [PR](https://github.com/ceph/ceph/pull/56520)
- Restored `new_object` flag for delete-missing entries to avoid losing this state when deleting missing objects. [PR](https://github.com/ceph/ceph/pull/63152)
- Maximum time scrub waits for replica responses can be adjusted via `osd_scrub_replica_scrub_timeout` to accommodate slower replicas. [PR](https://github.com/ceph/ceph/pull/63940)
- Fixed BlueStore/BlueFS device expansion flow: process in order of WAL, DB, shared devices, identify cases where no expansion needed and abnormal label sizes, and check expansion metadata write results. [PR](https://github.com/ceph/ceph/pull/62216)
- Fixed race condition between BlueFS file `truncate()` and `unlink()` concurrency; moved deletion state check under file lock protection. [PR](https://github.com/ceph/ceph/pull/62840)
- BlueFS `truncate()` now accepts abnormal allocation unit sizes to avoid assertion in such cases. [PR](https://github.com/ceph/ceph/pull/66056)
- Fixed the issue where the `aio_write` counter was not correctly accumulated when BlueFS uses `bytes_written_slow`. [PR](https://github.com/ceph/ceph/pull/66353)
- Fixed sequence number advancement error when extending BlueFS log, and added regression test covering log runway scenario. [PR](https://github.com/ceph/ceph/pull/61653)
- Fixed issue in BlueStore partial extent decoder where invalid iterator was dereferenced when shared blob not found. [PR](https://github.com/ceph/ceph/pull/62054)
- BlueStore preloads compression plugins at mount, and caches and uses compression, checksum, and related parameters when collection updates pool options; selects algorithm from loaded plugins during decompression. [PR](https://github.com/ceph/ceph/pull/62145)
- ceph-volume zap flow now allows processing partitions on multipath devices. [PR](https://github.com/ceph/ceph/pull/62178)
- ceph-volume no longer converts logical volume symlinks to real paths, avoiding loss of symlink semantics during migration and device identification. [PR](https://github.com/ceph/ceph/pull/59989)
- Fixed regex usage in ceph-volume when setting `dmcrypt_no_workqueue`. [PR](https://github.com/ceph/ceph/pull/62791) [PR](https://github.com/ceph/ceph/pull/62855)
- BlueFS is now the sole selector of volume reserved block size, avoiding BlueStore and BlueFS using different sources for reserved block size. [PR](https://github.com/ceph/ceph/pull/62721)
- Scrub no longer silently rewrites object info when building scrub map; mismatched object-info OIDs are now identified as corruption by scrub verification path. [PR](https://github.com/ceph/ceph/pull/62569)
- Fixed BlueStore hybrid allocator possibly incorrectly returning `ENOSPC` in boundary allocation scenarios, and added allocator tests. [PR](https://github.com/ceph/ceph/pull/62539)
- Fixed issue where garbage collection might delete tail objects still referenced by target object after RGW copies multipart object to itself. [PR](https://github.com/ceph/ceph/pull/62656)
- Fixed inconsistency between attribute merging and persistence when RGW creates, updates, or deletes buckets; dbstore's `put_info()` synchronously updates bucket attributes. [PR](https://github.com/ceph/ceph/pull/61996) [PR](https://github.com/ceph/ceph/pull/64411) [PR](https://github.com/ceph/ceph/pull/64488)
- Fixed RGW bucket listing progress determination and version suffix handling for non-versioned objects, and made namespaced entries list query skip processed regions. [PR](https://github.com/ceph/ceph/pull/62234) [PR](https://github.com/ceph/ceph/pull/62591)
- Fixed `radosgw-admin bucket radoslist` SLO manifest handling and improved error message collection; added `rgw-gap-list` man page and included it in documentation build and RPM install manifest. [PR](https://github.com/ceph/ceph/pull/62418) [PR](https://github.com/ceph/ceph/pull/62723) [PR](https://github.com/ceph/ceph/pull/63997) [COMMIT](https://github.com/ceph/ceph/commit/c3676b90eae3afcb8a313467b421151c626909d8) [COMMIT](https://github.com/ceph/ceph/commit/bbe80059ef005fa762f6a2a05107f55b84f25cc4)
- RGW returned ETag format adjusted to quoted format compliant with AWS S3 API. [PR](https://github.com/ceph/ceph/pull/62608)
- Fixed read boundary for multipart `GetObject?partNumber=` when only one part exists, and made `partNumber=1` for non-multipart objects return full object range. [PR](https://github.com/ceph/ceph/pull/62544)
- Swift API completed `last_modified` field and propagated bucket modification time from bucket entity. [PR](https://github.com/ceph/ceph/pull/61553)
- Cloud restore no longer sends RGW internal headers to cloud endpoint; also fixed lifecycle handling for non-current objects with empty instance. [PR](https://github.com/ceph/ceph/pull/63031)
- Fixed duplicate decoding and empty string decoding handling for S3 copy-source URL. [PR](https://github.com/ceph/ceph/pull/64052)
- Fixed crash that might be triggered when executing `radosgw-admin bucket object shard ...`. [PR](https://github.com/ceph/ceph/pull/62885)
- When pool is full, RGW object deletion uses I/O initialization path that can handle pool-full state; S3 corresponding `ENOSPC` mapped to 507 `InsufficientCapacity`. [PR](https://github.com/ceph/ceph/pull/62094)
- RGW notification service added handling logic for unwatch errors to avoid errors directly breaking subsequent cleanup. [PR](https://github.com/ceph/ceph/pull/62403)
- Fixed issue where storage class was empty when displaying multipart upload. [PR](https://github.com/ceph/ceph/pull/64312)
- Fixed deletion handling when executing `bucket rm --bypass-gc` on replicated objects. [PR](https://github.com/ceph/ceph/pull/66002)
- Fixed Keystone authentication not working without admin token (service account configuration). [PR](https://github.com/ceph/ceph/pull/64200)
- Mirror status is now written during image creation, and added `CREATING` status value so callers can display accurate image status. [PR](https://github.com/ceph/ceph/pull/63236) [PR](https://github.com/ceph/ceph/pull/62939)
- RBD group snapshot creation follows `rbd_default_snapshot_quiesce_mode`; internal calls no longer pass public API flags directly. [PR](https://github.com/ceph/ceph/pull/62962)
- Prohibited moving images still belonging to a group into trash, and added corresponding exception for Python bindings. [PR](https://github.com/ceph/ceph/pull/62967)
- Fixed resource leak in librbd group snapshot operation where opened image was not closed on failure. [PR](https://github.com/ceph/ceph/pull/64620)
- Fixed memory leak in librbd persistent write log cleanup of SyncPoint persist context. [PR](https://github.com/ceph/ceph/pull/64093)
- rbd-mirror no longer deletes remote image when it is not primary. [PR](https://github.com/ceph/ceph/pull/64738)
- rbd-mirror remote metadata cache key now includes cluster FSID to avoid cache key conflicts between clusters. [PR](https://github.com/ceph/ceph/pull/66272)
- rbd-mirror daemon can continue syncing unfinished demote snapshot after restart. [PR](https://github.com/ceph/ceph/pull/66163)
- rbd-mirror releases lock before ending async operation to avoid holding lock during tracker completion callback. [PR](https://github.com/ceph/ceph/pull/64091)
- libcephfs `chownat()` and `statxat()` now safely handle empty pathname. [PR](https://github.com/ceph/ceph/pull/61165)
- Fixed issue where client might hang in `Client::get_caps` when waiting for Fc caps revoked by MDS. [PR](https://github.com/ceph/ceph/pull/60695)
- Fixed the length of `d_reclen` returned by CephFS `readdir`. [PR](https://github.com/ceph/ceph/pull/61519)
- Fixed snapdiff handling when same-name dentry is deleted/recreated across fragments: rollback fragment entry when necessary, and added regression scenario. [PR](https://github.com/ceph/ceph/pull/65364)
- Fixed MDS `readdir` path when OSD is full, and added full pool test for `subvolume_ls`. [PR](https://github.com/ceph/ceph/pull/65348)
- CephFS volumes now handles dangling symlinks recoverably and added tests. [PR](https://github.com/ceph/ceph/pull/62109)
- volumes module retains required mon caps when access key still contains MDS/OSD caps. [PR](https://github.com/ceph/ceph/pull/65297)
- Fixed error message when subvolume metadata file name is too long, and added creation command test. [PR](https://github.com/ceph/ceph/pull/62050)
- `cephfs-journal-tool journal import` validates dump header and returns error for empty/invalid dump instead of crashing. [PR](https://github.com/ceph/ceph/pull/62114)
- Fixed issue where journal reset flow accidentally reset trim position. [PR](https://github.com/ceph/ceph/pull/65603)
- When deleting CephFS volume, snap-schedule state is handled and warning issued if active schedules exist; `fs rm` also adds corresponding warning. [PR](https://github.com/ceph/ceph/pull/61187)
- Fixed snap-schedule handling of duplicate retention specs and its message format. [PR](https://github.com/ceph/ceph/pull/65295)
- Restricted renaming to only when the filesystem is offline; `fs fail` must be enabled before executing `client_refuse_session`. [PR](https://github.com/ceph/ceph/pull/61410)
- MDS outputs path depth in diagnostic logs and records events of creating batch head. [PR](https://github.com/ceph/ceph/pull/61518)
- Fixed cleanup of importing sessions and client eviction handling when subtree export is interrupted, and display `importing_count` in session dump. [PR](https://github.com/ceph/ceph/pull/61514)
- MDS session tracker includes sessions being killed in statistics. [PR](https://github.com/ceph/ceph/pull/65253)
- CephFS volumes module periodically checks async tasks to avoid task status being left unhandled for long time. [PR](https://github.com/ceph/ceph/pull/61230)
- MDS SimpleLock wait mask switched to `WAIT_ALL`. [PR](https://github.com/ceph/ceph/pull/67495)
- Discard client metrics messages during MDS recovery to avoid processing data not applicable to the recovery phase. [PR](https://github.com/ceph/ceph/pull/61299)
- Client path resolution can handle paths without inode anchor, and added `ll_walk` tests covering cwd/root. [PR](https://github.com/ceph/ceph/pull/62500)
- `fallocate` returns `EOPNOTSUPP` for mode 0, and added API and Python bindings tests. [PR](https://github.com/ceph/ceph/pull/60657)
- Fixed invalid access when MDS accesses empty `mdr->dn[0]`. [PR](https://github.com/ceph/ceph/pull/61450) [PR](https://github.com/ceph/ceph/pull/61516)
- MDS no longer processes client metrics messages via fast dispatch. [PR](https://github.com/ceph/ceph/pull/61339)
- cephadm reports success/failure only when a progress event exists, avoiding notifications for non-existent progress IDs. [PR](https://github.com/ceph/ceph/pull/58450)
- Fixed the issue where msgr2 might return an incorrect `allowed_modes` in the `AuthBadMethodFrame` path. [PR](https://github.com/ceph/ceph/pull/65334)
- Fixed race between `reset_recv_state` and connection close in async messenger. [PR](https://github.com/ceph/ceph/pull/65786)
- Fixed exception handling when daemon metric parsing fails. [PR](https://github.com/ceph/ceph/pull/65595)
- Corrected MTU Mismatch alert rule and expression. [PR](https://github.com/ceph/ceph/pull/65710)
- Manager processes MonMap and FSMap before notifying module listeners, ensuring subscribers see updated map state. [PR](https://github.com/ceph/ceph/pull/57065)
- LogMonitor no longer sends replies to forwarded MLog commands, and decides whether to continue processing based on whether there are new log entries. [PR](https://github.com/ceph/ceph/pull/62212)
- PG export for `ceph-objectstore-tool` adds `--no-superblock` support, and opens BlueStore database read-only for allowed read-only operations to improve chances of reading corrupted storage. [PR](https://github.com/ceph/ceph/pull/62122)
- Subnet judgment in public address selection logic supports IPv6 addresses. [PR](https://github.com/ceph/ceph/pull/62814) [PR](https://github.com/ceph/ceph/pull/62855)
- Fixed Dashboard Object/Overview area chart not displaying correctly. [PR](https://github.com/ceph/ceph/pull/62664)
- Dashboard host API fills `ceph_version` with Manager current version for hosts that do not report a separate version. [PR](https://github.com/ceph/ceph/pull/62730)
- Fixed parsing of interval and start_time when removing RBD mirror schedule. [PR](https://github.com/ceph/ceph/pull/62964)
- MDS Beacon wakes its worker threads on shutdown to avoid shutdown flow waiting for threads to wake up on their own. [PR](https://github.com/ceph/ceph/pull/61513)
- Improved lifecycle management of kernel device discard thread. [PR](https://github.com/ceph/ceph/pull/65216)

### Refactoring

- BlueStore allocator implementation has been cleaned up and reused, adding `hybrid_btree2` implementation, error handling, and benchmark/regression tests. [PR](https://github.com/ceph/ceph/pull/62539)
- OSD scrubber unifies delayed event scheduling into a common timer-event interface, and uses it to schedule range-block alerts, reservation timeout, and scrub sleep. [PR](https://github.com/ceph/ceph/pull/63558)
- Adjusted cluster read completion path for librbd QCOW format migration to avoid `read_clusters()` inline completion callbacks. [PR](https://github.com/ceph/ceph/pull/64195)
- Incorporated dmclock source into Ceph repository, and adjusted mClock scheduler constructor parameters and client request cleanup logic. [PR](https://github.com/ceph/ceph/pull/62364)
- CRUSH rule calculation changed variable-length stack arrays to `std::vector` to avoid reliance on compiler extensions, and C++ containers manage temporary workspace. [PR](https://github.com/ceph/ceph/pull/62014)

### Tests

- Updated Reef cross-version upgrade tests: pinned old version test tags, restored non-container distro coverage, limited Pacific test distros, and added handling for old OSD feature-bit and alert compatibility. [PR](https://github.com/ceph/ceph/pull/67657)
- Adjusted cluster size and timeouts for RADOS API tests, and allowed verify tests to choose 2 node or 4 node clusters. [PR](https://github.com/ceph/ceph/pull/62473)
- Cleaned up tests for deprecated cache tier and deprecated `cls_cxx_gather`; removed no longer available RGW Hadoop S3A subtest. [PR](https://github.com/ceph/ceph/pull/62210) [PR](https://github.com/ceph/ceph/pull/60195) [PR](https://github.com/ceph/ceph/pull/64588) [PR](https://github.com/ceph/ceph/pull/64669)
- Test and CI maintenance updates: fixed environment, dependencies, timeouts, alert filtering, and test target configuration for CephFS, RGW, RBD, OSD, and Dashboard tests. [PR](https://github.com/ceph/ceph/pull/60901) [PR](https://github.com/ceph/ceph/pull/62492) [PR](https://github.com/ceph/ceph/pull/62396) [PR](https://github.com/ceph/ceph/pull/63055) [PR](https://github.com/ceph/ceph/pull/61508) [PR](https://github.com/ceph/ceph/pull/62953) [PR](https://github.com/ceph/ceph/pull/63927) [PR](https://github.com/ceph/ceph/pull/63979) [PR](https://github.com/ceph/ceph/pull/61773) [PR](https://github.com/ceph/ceph/pull/62116) [PR](https://github.com/ceph/ceph/pull/64281) [PR](https://github.com/ceph/ceph/pull/63343) [PR](https://github.com/ceph/ceph/pull/64340) [PR](https://github.com/ceph/ceph/pull/64596) [PR](https://github.com/ceph/ceph/pull/64588) [PR](https://github.com/ceph/ceph/pull/64666) [PR](https://github.com/ceph/ceph/pull/64669) [PR](https://github.com/ceph/ceph/pull/62473) [PR](https://github.com/ceph/ceph/pull/64918) [PR](https://github.com/ceph/ceph/pull/64761) [PR](https://github.com/ceph/ceph/pull/65418) [PR](https://github.com/ceph/ceph/pull/65473) [PR](https://github.com/ceph/ceph/pull/65251) [PR](https://github.com/ceph/ceph/pull/63017) [PR](https://github.com/ceph/ceph/pull/62092) [PR](https://github.com/ceph/ceph/pull/61297) [PR](https://github.com/ceph/ceph/pull/65630) [PR](https://github.com/ceph/ceph/pull/61279) [PR](https://github.com/ceph/ceph/pull/63129) [PR](https://github.com/ceph/ceph/pull/65837) [PR](https://github.com/ceph/ceph/pull/63717) [PR](https://github.com/ceph/ceph/pull/65663) [PR](https://github.com/ceph/ceph/pull/66252) [PR](https://github.com/ceph/ceph/pull/66243) [PR](https://github.com/ceph/ceph/pull/66359) [PR](https://github.com/ceph/ceph/pull/64748) [PR](https://github.com/ceph/ceph/pull/67067) [PR](https://github.com/ceph/ceph/pull/67529)
- Improved stability of librbd notification tests: handle transient errors as expected, and flush test output line by line. [PR](https://github.com/ceph/ceph/pull/62688) [PR](https://github.com/ceph/ceph/pull/62751)

### Performance

- Versioned bucket resharding trigger timing advanced to handle shard growth earlier. [PR](https://github.com/ceph/ceph/pull/63598)
- Optimized incomplete multipart upload query in bucket checks to reduce scan overhead. [PR](https://github.com/ceph/ceph/pull/64464)
- Shortened hold time of `DaemonStateIndex` lock to reduce lock contention on daemon state index. [PR](https://github.com/ceph/ceph/pull/65463)
- Adjusted discard buffer size for RGW Beast frontend. [PR](https://github.com/ceph/ceph/pull/63711)

### Security

- CephFS client prohibits non-privileged users from setting SGID/SUID bits via `fallocate` path. [PR](https://github.com/ceph/ceph/pull/66040)
- Manager alerts use explicit SSL context for `SMTP_SSL` connection. [PR](https://github.com/ceph/ceph/pull/66142)
- GitHub Actions workflow pinned to SHA-1 commit reference. [PR](https://github.com/ceph/ceph/pull/65759)

### Documentation

- Added or clarified deep scrub, unscubbed PG alerts, scrub interval, `osd_deep_scrub_interval_cv`, and general configuration options. [PR](https://github.com/ceph/ceph/pull/62503) [PR](https://github.com/ceph/ceph/pull/62552) [PR](https://github.com/ceph/ceph/pull/63490) [PR](https://github.com/ceph/ceph/pull/63956) [PR](https://github.com/ceph/ceph/pull/64218)
- Updated RGW administration, STS, NFS, Lifecycle, bucket quota, user caps, and Manager module configuration documentation. [PR](https://github.com/ceph/ceph/pull/62468) [PR](https://github.com/ceph/ceph/pull/62882) [PR](https://github.com/ceph/ceph/pull/62613) [PR](https://github.com/ceph/ceph/pull/63442) [PR](https://github.com/ceph/ceph/pull/64022) [PR](https://github.com/ceph/ceph/pull/64322) [PR](https://github.com/ceph/ceph/pull/64339) [PR](https://github.com/ceph/ceph/pull/64167) [PR](https://github.com/ceph/ceph/pull/64397)
- Improved CephFS troubleshooting and recovery documentation, adding expected journal replay completion time, MDS journal trim, and recovery troubleshooting steps. [PR](https://github.com/ceph/ceph/pull/63978) [PR](https://github.com/ceph/ceph/pull/64872) [PR](https://github.com/ceph/ceph/pull/64879) [PR](https://github.com/ceph/ceph/pull/64901) [PR](https://github.com/ceph/ceph/pull/64904) [PR](https://github.com/ceph/ceph/pull/65058) [PR](https://github.com/ceph/ceph/pull/65026) [PR](https://github.com/ceph/ceph/pull/65037) [PR](https://github.com/ceph/ceph/pull/65041) [PR](https://github.com/ceph/ceph/pull/65044) [PR](https://github.com/ceph/ceph/pull/65047) [PR](https://github.com/ceph/ceph/pull/65088) [PR](https://github.com/ceph/ceph/pull/65083) [PR](https://github.com/ceph/ceph/pull/65078) [PR](https://github.com/ceph/ceph/pull/65097) [PR](https://github.com/ceph/ceph/pull/65123) [PR](https://github.com/ceph/ceph/pull/65126) [PR](https://github.com/ceph/ceph/pull/65091) [PR](https://github.com/ceph/ceph/pull/65201) [PR](https://github.com/ceph/ceph/pull/65094) [PR](https://github.com/ceph/ceph/pull/65380) [PR](https://github.com/ceph/ceph/pull/64853)
- Added Dashboard OAuth2 SSO documentation; this documentation was later withdrawn within the interval, so the final version no longer includes this description. [PR](https://github.com/ceph/ceph/pull/64034)
- Withdrew the Dashboard OAuth2 SSO documentation added in this interval; the final documentation set no longer includes this content. [PR](https://github.com/ceph/ceph/pull/66796)
- Updated support status and usage documentation for Windows CephFS, RBD, and CephFS Dokan clients. [PR](https://github.com/ceph/ceph/pull/64482) [PR](https://github.com/ceph/ceph/pull/64493) [PR](https://github.com/ceph/ceph/pull/64736) [PR](https://github.com/ceph/ceph/pull/64760) [PR](https://github.com/ceph/ceph/pull/64786)
- S3 Object Operations documentation added `delete-if-unmodified-since` request header description. [PR](https://github.com/ceph/ceph/pull/64316)
- Enhanced pool documentation with pool descriptions and management guidance. [PR](https://github.com/ceph/ceph/pull/63862)
- Read balancer documentation added kernel client usage steps. [PR](https://github.com/ceph/ceph/pull/65440)
- User management documentation describes new `ceph auth rotate` command. [PR](https://github.com/ceph/ceph/pull/58236)
- RBD configuration reference documentation added clone-related configuration section. [PR](https://github.com/ceph/ceph/pull/66173)
- cephadm upgrade guide recommends temporarily disabling active PG autoscaler during upgrade to avoid PG split/merge prolonging upgrade, and adds steps to disable and restore. [PR](https://github.com/ceph/ceph/pull/62380)
- cephadm OSD removal documentation states that `ceph orch osd rm --zap` clears LVM and partition information on OSD disks. [PR](https://github.com/ceph/ceph/pull/62444)
- cephadm documentation reminds: directly executing `ceph orch restart` on OSD service does not respect CRUSH failure domain, which may affect data availability. [PR](https://github.com/ceph/ceph/pull/62797)
- RGW documentation clearly distinguishes S3 path-style and virtual-hosted-style requests, and notes that path-style has been deprecated by AWS. [PR](https://github.com/ceph/ceph/pull/61987)
- Release process documentation clarifies that release build is not responsible for building containers, and updates signing and release steps. [PR](https://github.com/ceph/ceph/pull/61818)
- CephFS troubleshooting guide explains that volumes module's asynchronous purge/clone threads can be paused, and warns not to arbitrarily adjust `max_mds` during failure recovery. [PR](https://github.com/ceph/ceph/pull/62875)
- Manager Prometheus module documentation updated exporter data collection, endpoints, and configuration. [PR](https://github.com/ceph/ceph/pull/62931)
- PG and balancer documentation added autoscaler setting recommendations, single-phase migratable PG ratio, and name and default behavior of `upmap_max_deviation`. [PR](https://github.com/ceph/ceph/pull/63536) [PR](https://github.com/ceph/ceph/pull/63647) [PR](https://github.com/ceph/ceph/pull/64119)
- mClock configuration guide updated on how to set or override OSD's `osd_mclock_max_capacity_iops_[hdd,ssd]`. [PR](https://github.com/ceph/ceph/pull/63072)
- CephFS mirroring documentation added peer bootstrap, mirror daemon lifecycle, and sync allocation descriptions. [PR](https://github.com/ceph/ceph/pull/63274) [PR](https://github.com/ceph/ceph/pull/63299) [PR](https://github.com/ceph/ceph/pull/63548) [PR](https://github.com/ceph/ceph/pull/63661)
- RGW notification documentation revised pubsub counter description, and clarified that `pubsub_push_pending` does not include notifications waiting to be sent in persistent queue. [PR](https://github.com/ceph/ceph/pull/64127) [PR](https://github.com/ceph/ceph/pull/64156) [PR](https://github.com/ceph/ceph/pull/64114)
- Stretch mode documentation updated two-site network partition, tiebreaker selection, and recovery behavior after single-site loss. [PR](https://github.com/ceph/ceph/pull/63816) [PR](https://github.com/ceph/ceph/pull/63850) [PR](https://github.com/ceph/ceph/pull/61654)
- RBD mirroring troubleshooting documentation explains that pools in peer clusters must have the same name, and links to steps for renaming pools. [PR](https://github.com/ceph/ceph/pull/63847)
- Health check documentation updates Monitor low disk space threshold and Monitor DB path examples. [PR](https://github.com/ceph/ceph/pull/65239)
- Configuration documentation supplements the purposes of `ceph config show-with-defaults` and legacy `ceph-conf --show-config`. [PR](https://github.com/ceph/ceph/pull/65207)
- Telemetry documentation updates licensing parameters for enabling data sharing, channel management, report content, and anonymized device data descriptions. [PR](https://github.com/ceph/ceph/pull/63769) [PR](https://github.com/ceph/ceph/pull/63810) [PR](https://github.com/ceph/ceph/pull/63772) [PR](https://github.com/ceph/ceph/pull/64344) [PR](https://github.com/ceph/ceph/pull/63775) [PR](https://github.com/ceph/ceph/pull/63778) [PR](https://github.com/ceph/ceph/pull/63906) [PR](https://github.com/ceph/ceph/pull/63693) [PR](https://github.com/ceph/ceph/pull/63865) [PR](https://github.com/ceph/ceph/pull/63868)
- cephadm OSD removal documentation supplements the state transition description of Monitor during OSD removal. [PR](https://github.com/ceph/ceph/pull/61665)
- Stretch mode documentation supplements handling of site loss and network partition, connectivity-based Monitor election, and peering protection to prevent single-site acting set from activating PGs. [PR](https://github.com/ceph/ceph/pull/61654)
- Update CephFS journal-tool documentation, supplementing current journal checking and repair instructions. [PR](https://github.com/ceph/ceph/pull/63109)
- Improve RGW and SNMP Gateway configuration descriptions in cephadm service documentation. [PR](https://github.com/ceph/ceph/pull/62695)
- mount.ceph manual explains that directory statistics returned by `dirstat` are updated lazily, so they may be temporarily stale after directory changes; and clarifies the purpose of `nodirstat`. [PR](https://github.com/ceph/ceph/pull/65184)
- Removed the obsolete `clonedata` command entry from the `rados` command manual. [PR](https://github.com/ceph/ceph/pull/64394)
- Cache tiering documentation adds note: it is not recommended to deploy new cache tiers in versions after Reef, and migration from existing deployments is recommended. [PR](https://github.com/ceph/ceph/pull/63831) [PR](https://github.com/ceph/ceph/pull/63696) [PR](https://github.com/ceph/ceph/pull/64497)

### Build / CI

- Dashboard tests switch to system Python packages, skipping corresponding tests when SAML dependencies are missing; backend API test scripts switch to teuthology's actual dependencies. [PR](https://github.com/ceph/ceph/pull/64612) [PR](https://github.com/ceph/ceph/pull/65418) [PR](https://github.com/ceph/ceph/pull/63186) [PR](https://github.com/ceph/ceph/pull/63313)
- Container build scripts add dependency and build support for Rocky Linux 9/10, CentOS Stream 10, etc., and extend container build parameters. [PR](https://github.com/ceph/ceph/pull/64658)
- Improve container and source package builds: support skipping duplicate make-dist, sccache, different distro/build variants, FOR_MAKE_CHECK parameter, and compiler selection, and adjust sudo and resource allocation handling in build scripts. [PR](https://github.com/ceph/ceph/pull/65066) [PR](https://github.com/ceph/ceph/pull/65188) [PR](https://github.com/ceph/ceph/pull/65250) [PR](https://github.com/ceph/ceph/pull/65845) [PR](https://github.com/ceph/ceph/pull/65837) [PR](https://github.com/ceph/ceph/pull/65944) [PR](https://github.com/ceph/ceph/pull/66012) [PR](https://github.com/ceph/ceph/pull/66014)
- Adjust build dependencies: replace apt mirror, add iproute2, and include mgr/rgw in ceph-mgr-modules-core package. [PR](https://github.com/ceph/ceph/pull/66669) [PR](https://github.com/ceph/ceph/pull/66738) [PR](https://github.com/ceph/ceph/pull/57874)
- Fix test invocation in container build scripts, ensure build containers have curl, and adjust in-container documentation installation and Python generated file cleanup behavior. [PR](https://github.com/ceph/ceph/pull/62339) [PR](https://github.com/ceph/ceph/pull/62345)
- Pin cheroot version range in Manager dependencies and update Dashboard constraint versions. [PR](https://github.com/ceph/ceph/pull/65637)

### Maintenance

- Set identifiable thread names for RGW notification worker threads. [PR](https://github.com/ceph/ceph/pull/63095)
- Output `next_snap` when checking dentry corruption to facilitate diagnosis of MDS dentry state. [PR](https://github.com/ceph/ceph/pull/61978)
- Improve usage hints for ceph-fuse mount parameters. [PR](https://github.com/ceph/ceph/pull/61275)

