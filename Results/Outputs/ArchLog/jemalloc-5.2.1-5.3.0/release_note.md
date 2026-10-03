# Release Note

## Important Changes

### Platform Abstraction Layer
- Added the initial file structure of the ehooks module. (Architecture event: Added ehooks module)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [ba8b9ec](https://github.com/jemalloc/jemalloc/commit/ba8b9ecbcbda3b975711e4bced4647afaa50c71e)
- Extract edata_t cache logic into an independent edata_cache module, and add initialization, acquisition, release and prefork interfaces. (Architecture event: edata_cache module extraction)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [7859184](https://github.com/jemalloc/jemalloc/commit/78591841798fa548feba468d1bb7338592039180)
- Added page allocator (PA) module stub code, including header files and source file basic framework. (Architecture event: Added PA module stub code)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [12be9f5](https://github.com/jemalloc/jemalloc/commit/12be9f5727e382c96656f9469e9702322ccd0c73)
- Added SEC module (small extent cache), which caches small extents to reduce pressure on the centralized allocator. (Architecture event: TSD_Test_Suite module removed)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [ea51e97](https://github.com/jemalloc/jemalloc/commit/ea51e97bb893f560c70f42478d67c8159ee09b3d)
- Added prof_sys module to separate the system thread name reading function from the core code. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [03ae509](https://github.com/jemalloc/jemalloc/commit/03ae509f325e952a1447d8b933ee57f3d116434d)
- Added hpa_central module as a centralized component of the large page allocator. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#1909](https://github.com/jemalloc/jemalloc/pull/1909): [21b70cb](https://github.com/jemalloc/jemalloc/commit/21b70cb540e0f9ff7d7ff20fa21772e96c2215b0)
- Added pageslab abstraction and psset collection, used to manage pageslab and implement initialization and statistical functions. (Architecture-related: added pageslab and psset)
  ↳ [#1904](https://github.com/jemalloc/jemalloc/pull/1904): [018b162](https://github.com/jemalloc/jemalloc/commit/018b162d673e64230b7d202075dca0e846e28e6a)
- Added multi-producer single-consumer queue module and its unit test. (Architecture-related: Added MPSC queue module)
  ↳ [#2066](https://github.com/jemalloc/jemalloc/pull/2066): [de033f5](https://github.com/jemalloc/jemalloc/commit/de033f56c08745500f98b590f5138ddc4a5c0732)
- Added flat_bitmap module to provide extended bitmap operation API. (Architecture-related: Added flat_bitmap module)
  ↳ [#1888](https://github.com/jemalloc/jemalloc/pull/1888): [ceee823](https://github.com/jemalloc/jemalloc/commit/ceee823519bb534c2609e1dadd9b923bd28853b4)
- The mutex_pool module was deleted, which involves core modules and public header files, affecting component boundaries and cross-module collaboration. (Architecture event: mutex_pool module deletion)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [7dc7752](https://github.com/jemalloc/jemalloc/commit/7dc77527ba1fa8a2764b975e9955a55cbb46d034)
- Remove the allocation and release functions of psset from the core code and keep it only as test code. (Architecture-related: core functions are migrated to testing)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [f7cf23a](https://github.com/jemalloc/jemalloc/commit/f7cf23aa4d7c266af512c599205b1fab80b26796)
- Reconstruct the statistical data structures of HPA and psset into a unified psset_stats_t, and migrate related functions to the psset module. (Architecture-related: unified statistical data structure)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [c1b2a77](https://github.com/jemalloc/jemalloc/commit/c1b2a77933135ebefa62a5ec4c7d9efa94b14592)
- Created the eset module, and migrated the extent module's initialization, status acquisition, statistical information, insertion and removal, fit function and other functions to the eset module. (Architecture event: eset module creation and extent responsibility split)
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [b416b96](https://github.com/jemalloc/jemalloc/commit/b416b96a397a2234d943d1e7e37e1dc208c971bc), [63d1b7a](https://github.com/jemalloc/jemalloc/commit/63d1b7a7a76b7294a7dd85599c24cd9b555ccf4e), [a428615](https://github.com/jemalloc/jemalloc/commit/a42861540e3a257259eb1c303c7750229ac62b71), [1210af9](https://github.com/jemalloc/jemalloc/commit/1210af9a4e26994c6f340085554f3519994ae682), [77bbb35](https://github.com/jemalloc/jemalloc/commit/77bbb35a92821858b9054aa88f2c3bc76b29cbdc), [e6180fe](https://github.com/jemalloc/jemalloc/commit/e6180fe1b485c6128de4169e86c178f3118dcde4), [e144b21](https://github.com/jemalloc/jemalloc/commit/e144b21e4be9a6353ff9fee1b10c90e4b1030879), [821dd53](https://github.com/jemalloc/jemalloc/commit/821dd53a1d46f07cc8252bea4b229a77caa4ca83) | [#2098](https://github.com/jemalloc/jemalloc/pull/2098): [252e094](https://github.com/jemalloc/jemalloc/commit/252e0942d0346f1cc700874b55d0c1fef95c40e7)
- Created the ehooks module, and migrated the allocation, release, destruction, commit, clear, split, merge and other hook functions in the extent module to the ehooks module. (Architecture event: ehooks module creation and hook responsibility split)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [9f6eb09](https://github.com/jemalloc/jemalloc/commit/9f6eb09585239c10bde86d68ed48f6fe113ef8f7), [ae0d8e8](https://github.com/jemalloc/jemalloc/commit/ae0d8e8591f749ee8fbe1d732984a63f900aaea3), [dc8b4e6](https://github.com/jemalloc/jemalloc/commit/dc8b4e6e13fd2a0497f3ab5c0ba9edb92a64f470), [bac8e2e](https://github.com/jemalloc/jemalloc/commit/bac8e2e5a65a361dec4598419dd10d2b119e8d24), [5459ec9](https://github.com/jemalloc/jemalloc/commit/5459ec9daeea3144e71abb3b0eb9417a56e7ae95), [d78fe24](https://github.com/jemalloc/jemalloc/commit/d78fe241acb79ab4b0b7cb5b48d07be8582fc60a), [368baa4](https://github.com/jemalloc/jemalloc/commit/368baa42ef76f1dd44950b5929dc5697c0ac7add), [a5b42a1](https://github.com/jemalloc/jemalloc/commit/a5b42a1a10048d9562d59e494c9e2cf3ab6943ba), [1fff4d2](https://github.com/jemalloc/jemalloc/commit/1fff4d2ee3f5ab9d288a2b56544c1c8c4d8736da), [2fe5108](https://github.com/jemalloc/jemalloc/commit/2fe5108263d013b07572f5aa597ba6ace86ed342), [09475bf](https://github.com/jemalloc/jemalloc/commit/09475bf8acfef36924df787deb0247a7b0456c66)
- Introduced a universal thread event initialization function, unified initialization of tcache GC and prof sample events, and removed the old global state and hard-coded calls. (Architecture events: unified thread event initialization)
  ↳ [#1657](https://github.com/jemalloc/jemalloc/pull/1657): [43f0ce9](https://github.com/jemalloc/jemalloc/commit/43f0ce92d881f945da54a498cadc654ddb9403a1) | [#1750](https://github.com/jemalloc/jemalloc/pull/1750): [5e50052](https://github.com/jemalloc/jemalloc/commit/5e500523a056d7330e2223627ecdfb565d88e070) | [#1646](https://github.com/jemalloc/jemalloc/pull/1646): [198f02e](https://github.com/jemalloc/jemalloc/commit/198f02e7972023d10c9e4c4c6ab162738d103707)
- Refactor the extent module into hermetic form, remove the direct dependence on arena, and split sub-functions such as locks, hook calls and implicit zeroing. (Architecture event: Refactoring of extent module hermetic)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [92a511d](https://github.com/jemalloc/jemalloc/commit/92a511d385d1a256a42c6bf8cfc3dd9adb1f5217) | [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [add6365](https://github.com/jemalloc/jemalloc/commit/add636596afecb87e220d31ae75a9ba0b4601fbc) | [#2048](https://github.com/jemalloc/jemalloc/pull/2048): [ce68f32](https://github.com/jemalloc/jemalloc/commit/ce68f326b0c6bc5f2ba126a9cc8afef3f8a70039), [9b523c6](https://github.com/jemalloc/jemalloc/commit/9b523c6c15814e6662a1f659576996e047b7f965)
- Merged the base_ind_get and metadata_thp_enabled inline functions from base_inlines.h to base.h, and deleted the base_inlines.h file to simplify the header file structure. (Architecture event: base header file merge and simplification)
  ↳ [#1770](https://github.com/jemalloc/jemalloc/pull/1770): [182192f](https://github.com/jemalloc/jemalloc/commit/182192f83c029a794ee3c32767f43e471a00bd26)
- Unified the page allocator interface, allowing block expansion to use the API of the page allocation module, and added szind and slab parameters to the pa_expand function to unify the API. (Architecture event: Unification of the page allocation module interface)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [0880c2a](https://github.com/jemalloc/jemalloc/commit/0880c2ab9756ddb59b55dea673b20bd80922b487), [5bcc2c2](https://github.com/jemalloc/jemalloc/commit/5bcc2c2ab9b46cc15c1bc054a74615daabfd3675)
- Migrate decay (decay) related logic from the arena module to the page allocation module, including the stash_decayed function, decay function, all decay paths and decay initialization logic. (Architecture event: Migrate the decay logic to the page allocation module)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [aef28b2](https://github.com/jemalloc/jemalloc/commit/aef28b2f8fc4031f970896b312127cda00bbc2d0), [f012c43](https://github.com/jemalloc/jemalloc/commit/f012c43be0c5a43267e145b05e69b974b60f5917), [2d6eec7](https://github.com/jemalloc/jemalloc/commit/2d6eec7b5cc2a537e5ff702778c0c15832b5f961), [faec721](https://github.com/jemalloc/jemalloc/commit/faec7219b23303ec812e9aee6fc35352f936d10b)
- Migrate statistics-related logic from the arena module to the page allocation module, including nactive counters, edata_avail statistics, mapped statistics, basic statistics merging, complete statistics merging and mutex statistics reading. (Architecture event: Statistics logic is migrated to the page allocation module)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [527dd4c](https://github.com/jemalloc/jemalloc/commit/527dd4cdb8d1ec440fefe894ada4ccbc1c3e437d), [3c28aa6](https://github.com/jemalloc/jemalloc/commit/3c28aa6f179421b23fd8795cbcaa4696aba99557), [e2cf3fb](https://github.com/jemalloc/jemalloc/commit/e2cf3fb1a3f064ba2c237620ca938e0e04c36d92), [506d907](https://github.com/jemalloc/jemalloc/commit/506d907e40e8b5b191b8bc5f2ee77d87e0684cfb), [238f3c7](https://github.com/jemalloc/jemalloc/commit/238f3c743067b1305f14ba4ddcf3b95ec7719ae7), [daefde8](https://github.com/jemalloc/jemalloc/commit/daefde88fe960e2ff0756fac82f82512025bdf1d)
- Migrate page allocation-related cleanup, destruction and internal access logic from the arena module to the page allocation module, including pa_shrink/pa_dalloc, remaining cleanup logic and internal access and destruction logic. (Architecture events: Migrate cleanup and destruction logic to the page allocation module)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [71fc0dc](https://github.com/jemalloc/jemalloc/commit/71fc0dc968189e72a4437fb38759ef380a02a7ab), [46a9d7f](https://github.com/jemalloc/jemalloc/commit/46a9d7fc0b0e5124cc8a1ca0e3caec85968a6842), [0767584](https://github.com/jemalloc/jemalloc/commit/07675840a5d41c2537de2bd16e8da1cd11ef48e9) | [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [862219e](https://github.com/jemalloc/jemalloc/commit/862219e461d642d860d2c9ddc122705b031b6d80)
- Added the pa_extra.c file, migrated the fork processing logic of the page allocation module from arena.c to it, and restructured the related initialization and interface. (Architecture event: the fork processing logic was migrated to pa_extra.c)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [f29f609](https://github.com/jemalloc/jemalloc/commit/f29f6090f589bbd1eda92f025e931e449fa9d621)
- Migrate the retain growth limit setting logic from the arena module to the new pa module, and add the corresponding API declaration and implementation. (Architecture event: retain growth setting logic is migrated to the pa module)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [45671e4](https://github.com/jemalloc/jemalloc/commit/45671e4a27740c85c83b248d0e7e3f45024fdc45)
- Migrate the profiling file processing logic from prof.c to the new file prof_sys.c, including the reconstruction of bt_init, prof_backtrace_impl and other functions. (Architecture event: profiling module file reorganization)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [767a2e1](https://github.com/jemalloc/jemalloc/commit/767a2e1790656f038123036772fed6656175c7e6)
- Migrated the implementation of Page Allocator Interface (PAI) from PA module to PAC module, and adjusted related dependencies, enumerations and data structures. (Architecture event: PAI interface migrated to PAC module)
  ↳ [#1856](https://github.com/jemalloc/jemalloc/pull/1856): [1b5f632](https://github.com/jemalloc/jemalloc/commit/1b5f632e0fbb28d162fbf70d1032434787269f1a), [7226522](https://github.com/jemalloc/jemalloc/commit/722652222a159c10f616d61b6dc145d07f84e025), [6580317](https://github.com/jemalloc/jemalloc/commit/65803171a7f441f567b5d7e3809df22bda871d62), [dee5d1c](https://github.com/jemalloc/jemalloc/commit/dee5d1c42de6e0908e1ee8e3c4c89cffcbee72ff), [72435b0](https://github.com/jemalloc/jemalloc/commit/72435b0aba3e121d598be10e865f43d9491c71e2), [4ee75be](https://github.com/jemalloc/jemalloc/commit/4ee75be3a3d549619930cf07b5bc8a3809eab008), [6041aab](https://github.com/jemalloc/jemalloc/commit/6041aaba9742c792cfa1d9ddbede6c646dd92d33), [6107857](https://github.com/jemalloc/jemalloc/commit/6107857b7b40cd3d5c64053aeaf44e275374e9e8)
- Migrate profiling tool functions, unwind implementation and unbiased sampling variables to prof_data and prof_sys modules. (Architecture event: profiling tool functions are migrated to prof_data and prof_sys)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [d128efc](https://github.com/jemalloc/jemalloc/commit/d128efcb6aeddec8d3f1220eda0251dcaa25bab8), [dad821b](https://github.com/jemalloc/jemalloc/commit/dad821bb2239a42517f6ba5e48a29f5f569ab38f) | [#1916](https://github.com/jemalloc/jemalloc/pull/1916): [8efcdc3](https://github.com/jemalloc/jemalloc/commit/8efcdc3f98d896c0a67cc2dc34ff0494639b6bf5)
- Push thread event processing logic to each module, and add a unified event processing function for each event type. (Architecture events: Thread event processing logic is pushed to each module)
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [b06dfb9](https://github.com/jemalloc/jemalloc/commit/b06dfb9ccc1fb942c6d871a8e184fed496b59fc1)
- Unified the signatures of write callback functions and migrated them to the malloc_io module. (Architecture event: Unified the signatures of write callback functions and migrated them to malloc_io)
  ↳ [#1823](https://github.com/jemalloc/jemalloc/pull/1823): [2097e19](https://github.com/jemalloc/jemalloc/commit/2097e1945b262f079d82bf6ef78330bf03ebdf08)
- Split edata list operations into active and inactive link modes, and adjust the cache and recycling functions accordingly to utilize free space. (Architecture event: edata list operations are split into active/inactive links)
  ↳ [#1857](https://github.com/jemalloc/jemalloc/pull/1857): [392f645](https://github.com/jemalloc/jemalloc/commit/392f645f4d850d2256443299183123258899bb3e)
- Added per-page dirty status tracking to hpdata, and implemented operation interfaces such as hugify, dehugify and purge. (Architecture event: hpdata added dirty page tracking and operation interfaces)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [2ae9662](https://github.com/jemalloc/jemalloc/commit/2ae966222f071929dd124d2953b35ca16feb2ba0), [68a1666](https://github.com/jemalloc/jemalloc/commit/68a1666e915382cec716247d3b5950a066ef0768)
- Defined the constructor for the buffer writer parameters and restructured the related call points. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#1725](https://github.com/jemalloc/jemalloc/pull/1725): [40a3914](https://github.com/jemalloc/jemalloc/commit/40a391408c6edbabac4e408c1cdfdda64c0cd356)
- Split the profiling logging function into an independent prof_log.c module, and expose a small number of internal functions to support modularity. (Architecture-related: module splitting)
  ↳ [#1550](https://github.com/jemalloc/jemalloc/pull/1550): [56126d0](https://github.com/jemalloc/jemalloc/commit/56126d0d2d0730acde6416cf02efdb9ed19d578b)
- Change the lock level of witness from macro definition to enumeration type to avoid manually incrementing the value. (Architecture-related: public API: change the lock level to enumeration)
  ↳ [#1868](https://github.com/jemalloc/jemalloc/pull/1868): [25e43c6](https://github.com/jemalloc/jemalloc/commit/25e43c60223c169ce7dc66982f9472aa6e33306b)
- Centralize prof dump buffer size definitions into the prof_types.h header file and minimize memory footprint for non-prof builds. (Architecture-related: public API)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [354183b](https://github.com/jemalloc/jemalloc/commit/354183b10d286876ef9811fd9e94758926e66927)
- Extract the reserved memory growth logic from the extent module into the geom_grow module and encapsulate it into a reusable function. (Architecture-related: module responsibility migration)
  ↳ [#1910](https://github.com/jemalloc/jemalloc/pull/1910): [ffe5522](https://github.com/jemalloc/jemalloc/commit/ffe552223cc3b50dd88458e46d531f970b45096e)
- Reconstruct the buffer writer into an independent module, add internal buffer allocation and release functions, reconstruct the callback mechanism, and add a pipeline writing function. (Architecture-related: modular reconstruction)
  ↳ [#1725](https://github.com/jemalloc/jemalloc/pull/1725): [6d8e616](https://github.com/jemalloc/jemalloc/commit/6d8e6169028f50ef9904692a0d4ecc0f21054925) | [#1748](https://github.com/jemalloc/jemalloc/pull/1748): [9cac3fa](https://github.com/jemalloc/jemalloc/commit/9cac3fa8f588c828a0a94bdc911383d2952b40e0)
- Remove the internal test functions and variables of the profiling module from JEMALLOC_JET conditional compilation, make them always visible to the outside world, and add comments to indicate their use; at the same time, a dedicated test version function is added for the prof_recent module. (Architecture-related: public API)
  ↳ [#1865](https://github.com/jemalloc/jemalloc/pull/1865): [b7858ab](https://github.com/jemalloc/jemalloc/commit/b7858abfc0c605c451027c5f0209680b25ec8891)
- Generalized the prof_cnt_all() function interface to accept the prof_cnt_t structure, and updated the declaration, implementation and test cases. (Architecture-related: public API)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [f58ebdf](https://github.com/jemalloc/jemalloc/commit/f58ebdff7a82ed68f3bc007b0d10ed02ba3d065a)
- Renamed ecache_grow to geom_grow and migrated to a separate file for use in other allocators. (Architecture-related: Module responsibility adjustment)
  ↳ [#1910](https://github.com/jemalloc/jemalloc/pull/1910): [131b1b5](https://github.com/jemalloc/jemalloc/commit/131b1b53383720de3ca8877c676e85d968205103)
- Integrate HPA components into PAI implementation, add multiple core functions and reconstruct the pa_shard structure, add global HPA options and test code. (Architecture-related: core module integration)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [1c7da33](https://github.com/jemalloc/jemalloc/commit/1c7da3331795970c6049e5b526637bf692a4243e)
- Introduce the hpdata_t structure, separate the explicit representation of huge pages from edata_t, and update HPA and psset related logic to use the new structure. (Architecture-related: data structure separation)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [ca30b5d](https://github.com/jemalloc/jemalloc/commit/ca30b5db2bbf51b9c4d5aefa2ec87490b7f93395)
- Reconstructed the interaction between HPA and psset, controlling allocation and merging through flag bits, simplifying concurrency control and maintaining statistical correctness. (Architecture-related: HPA and psset interaction)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [da63f23](https://github.com/jemalloc/jemalloc/commit/da63f23e68069e967e6759e2ffa578970243df9e)
- Moved the sequence number in the edata structure from the bit field as an independent field, and adjusted the related access functions and initialization parameters to support HPA's fragmentation avoidance strategy. (Architecture-related: edata sequence number adjustment)
  ↳ [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [d21d5b4](https://github.com/jemalloc/jemalloc/commit/d21d5b46b607542398440d77b5f5ba22116dad5a)
- Delegate the time of calculating delayed work from the background thread to the PAI layer, and add corresponding auxiliary functions and HPA implementation. (Architecture-related: background thread delegates PAI)
  ↳ [#2107](https://github.com/jemalloc/jemalloc/pull/2107): [b8b8027](https://github.com/jemalloc/jemalloc/commit/b8b8027f19d089821a19214f56cc9c1202df835d)
- Migrated multiple statistics and functions in arena (such as edata_cache, ecache_grow, decay related, mapped statistics, extent serial number, etc.) to the newly extracted pa_shard or pa module, introduced the decay module, and reconstructed the page allocator responsibility. (Architecture-related: Page allocator responsibility reconstruction)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [688fb3e](https://github.com/jemalloc/jemalloc/commit/688fb3eb8959db178922476ffcfa5e94a82c1511), [32cb7c2](https://github.com/jemalloc/jemalloc/commit/32cb7c2f0b4da21ed2b98b8fde7bba86309d1acd), [1ad368c](https://github.com/jemalloc/jemalloc/commit/1ad368c8b7443881f40bc84cba87259f1892a8ce), [ce8c0d6](https://github.com/jemalloc/jemalloc/commit/ce8c0d6c09e744f52f2ce01b93c77d9acf0cf1a8), [70d12ff](https://github.com/jemalloc/jemalloc/commit/70d12ffa055518326573c985cbc86a32a1f2de1d), [7b62885](https://github.com/jemalloc/jemalloc/commit/7b6288547637124088ef208fe667037b70bd3e01), [8f2193d](https://github.com/jemalloc/jemalloc/commit/8f2193dc8db26eba40f7948f7ce60c8584ab31a9), [9f93625](https://github.com/jemalloc/jemalloc/commit/9f93625c1438a4dadc60bda9e43c63bcadd21ebd) | [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [03d95cb](https://github.com/jemalloc/jemalloc/commit/03d95cba8868f99fa18683d1e82596467ed08c7e) | [#2140](https://github.com/jemalloc/jemalloc/pull/2140): [c9ebff0](https://github.com/jemalloc/jemalloc/commit/c9ebff0fd6ab90d5eed0d11f48dfedcc21222ab0)
- Removed the profiling module's dependence on the thread_event module, forwarded the sampling event judgment to the caller, and the caller calculated and passed in the sampling event flag. (Architecture-related: Module dependency adjustment)
  ↳ [#1779](https://github.com/jemalloc/jemalloc/pull/1779): [ba783b3](https://github.com/jemalloc/jemalloc/commit/ba783b3a0ff6d47d56a76ed298a1aaa2515d12d4)
- Share the arena bin offset as a global variable, reducing cache misses during tcache flush. (Architecture-related: core module public interface changes)
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [3967329](https://github.com/jemalloc/jemalloc/commit/39673298130bdeb95859c95fe314c0a1d7181329)
- Added extent_commit_zero function, which merges extent submission and zeroing; simplified extent_merge_wrapper interface. (Architecture-related: public API changes)
  ↳ [#2151](https://github.com/jemalloc/jemalloc/pull/2151): [d906553](https://github.com/jemalloc/jemalloc/commit/d90655390f5192d53723023667b57453ba23e676)
- Enhanced ehooks module: Added ehooks_zero zero hook, head tracking function, default zero initialization and guard tag, and adjusted related function signatures. (Architecture event: ehooks module change)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [4b2e5ee](https://github.com/jemalloc/jemalloc/commit/4b2e5ee8b9989a84a5c3665bada0973ab351d3d9), [0704516](https://github.com/jemalloc/jemalloc/commit/07045162459f1d5f529ca530f035157f97645b0d)
- Added initialization function pac_init and auxiliary function pac_decay_data_get. for the PAC module (architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#1856](https://github.com/jemalloc/jemalloc/pull/1856): [7efcb94](https://github.com/jemalloc/jemalloc/commit/7efcb946c4707f12728e38f82fae1344591b9757)
- Added zero parameter to arena batch allocation function arena_fill_small_fresh to support clearing memory during allocation. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#1828](https://github.com/jemalloc/jemalloc/pull/1828): [f805468](https://github.com/jemalloc/jemalloc/commit/f805468957343e0fb02c84c0548eb39f98b9e29c)
- Add emap batch search interface for tcache refresh path, providing a more flexible calling method. (Architecture event: emap interface extension)
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [181ba7f](https://github.com/jemalloc/jemalloc/commit/181ba7fd4d039a3acfc4d2b115be55d93ac8c406)
- Added a pluggable buffer writer, supports custom write callbacks, and is applied to prof_log_stop output; at the same time, the malloc_cprintf function signature has been updated to adapt to this writer. (Architecture-related: public API)
  ↳ [#1525](https://github.com/jemalloc/jemalloc/pull/1525): [7fc6b1b](https://github.com/jemalloc/jemalloc/commit/7fc6b1b259fd1c38a59341ad555a47790da6f773) | [#1526](https://github.com/jemalloc/jemalloc/pull/1526): [ad3f7db](https://github.com/jemalloc/jemalloc/commit/ad3f7dbfa0f6b510d6e1e0dbaf859506d5ad2a96)
- The thread_allocated and thread_deallocated statistics counters are now always updated, no longer rely on the config_stats compilation option, and the related documentation has been updated. (Architecture-related: external behavior)
  ↳ [#1595](https://github.com/jemalloc/jemalloc/pull/1595): [57b81c0](https://github.com/jemalloc/jemalloc/commit/57b81c078e24cf05025f51dddc7c1b9353999390), [49e6fbc](https://github.com/jemalloc/jemalloc/commit/49e6fbce78ee2541e41f9d587ae5f31110433ce7) | [#1682](https://github.com/jemalloc/jemalloc/pull/1682): [e4c36a6](https://github.com/jemalloc/jemalloc/commit/e4c36a6f30d5b393f05daa2850e2c03406c5c4c2)
- Added realloc(ptr, 0) behavior configurable option, and added a statistical counter for the number of zero-size realloc calls. (Architecture-related: public API)
  ↳ [#1643](https://github.com/jemalloc/jemalloc/pull/1643): [9cfa805](https://github.com/jemalloc/jemalloc/commit/9cfa8059475745c31c9c646144432174a2165ca4), [de81a4e](https://github.com/jemalloc/jemalloc/commit/de81a4eadabb85b4c911fc6301b69f093ad47b53)
- Added the Last-N recent allocation record mode, which supports recording the last N allocations and saving the request size and thread name in the record entries for analysis of allocation life cycle, remote release and OOM investigation. (Architecture-related: public API)
  ↳ [#1602](https://github.com/jemalloc/jemalloc/pull/1602): [9a60cf5](https://github.com/jemalloc/jemalloc/commit/9a60cf54ec4b825a692330a1c56932fa1b121e27) | [#1724](https://github.com/jemalloc/jemalloc/pull/1724): [2b604a3](https://github.com/jemalloc/jemalloc/commit/2b604a3016f2cbda9499e2533ebef43b6fa9b72e) | [#1956](https://github.com/jemalloc/jemalloc/pull/1956): [5ba8617](https://github.com/jemalloc/jemalloc/commit/5ba861715abde3a68f6ad73a54ccb41f39874ece) | [#1734](https://github.com/jemalloc/jemalloc/pull/1734): [cd6e908](https://github.com/jemalloc/jemalloc/commit/cd6e908241900640864b59a4dae835e9cecfc0cd)
- Force sampling allocations to be page-aligned, allowing sampling objects to be identified via alignment checks, and enabling fixed-length releases. (Architecture-related: sampling behavior)
  ↳ [#1749](https://github.com/jemalloc/jemalloc/pull/1749): [88d9eca](https://github.com/jemalloc/jemalloc/commit/88d9eca8483f39ded261c897e95e7d4459775c28)
- Implement release events, the event module supports two event types: allocation and release; use byte-based events to trigger tcache garbage collection, and remove the tcache timer. (Architecture-related: event mechanism)
  ↳ [#1750](https://github.com/jemalloc/jemalloc/pull/1750): [97dd79d](https://github.com/jemalloc/jemalloc/commit/97dd79db6c4f9b93bb83182afb191d8dbef49806) | [#1846](https://github.com/jemalloc/jemalloc/pull/1846): [10b96f6](https://github.com/jemalloc/jemalloc/commit/10b96f635190cd8e27ed73f6b44293a7357e4013) | [#1657](https://github.com/jemalloc/jemalloc/pull/1657): [97f93fa](https://github.com/jemalloc/jemalloc/commit/97f93fa0f2d7343d308bbcd5cf551492d5652d0a) | [#1760](https://github.com/jemalloc/jemalloc/pull/1760): [51bd147](https://github.com/jemalloc/jemalloc/commit/51bd147422d95bfcd3919f11a6a7dd7a574e05cd) | [#1780](https://github.com/jemalloc/jemalloc/pull/1780): [4a78c6d](https://github.com/jemalloc/jemalloc/commit/4a78c6d81b3f431070f362c29ab7b492ee0b9e70)
- Add support for obtaining ehooks in the pa module, by adding the base pointer to the pa_shard structure and implementing the corresponding obtaining function. (Architecture-related: ehooks obtaining interface)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [7624043](https://github.com/jemalloc/jemalloc/commit/7624043a41087bb5124e8dadb184f53dd8583def)
- Added thread event look-ahead reading API to support predicting whether an event is triggered without advancing the event counter. (Architecture-related: Thread event look-ahead API)
  ↳ [#1828](https://github.com/jemalloc/jemalloc/pull/1828): [c6f59e9](https://github.com/jemalloc/jemalloc/commit/c6f59e9bb450bbce279f256ed56c0780092473c4)
- Added a new pipeline API for buffer writers and added corresponding unit tests. (Architecture-related: public API)
  ↳ [#1795](https://github.com/jemalloc/jemalloc/pull/1795): [f9aad7a](https://github.com/jemalloc/jemalloc/commit/f9aad7a49b14097a945316f10d2abe179fd0a8a5) | [#1760](https://github.com/jemalloc/jemalloc/pull/1760): [0ceb311](https://github.com/jemalloc/jemalloc/commit/0ceb31184d145646ff30b03f566069307cd570d8)
- Added a new option to allow obtaining the system thread name in each performance analysis sample, and disable setting the thread name through mallctl to avoid conflicts. (Architecture-related: public API)
  ↳ [#1798](https://github.com/jemalloc/jemalloc/pull/1798): [2256ef8](https://github.com/jemalloc/jemalloc/commit/2256ef896177faf8af7b199595382348be054250)
- Added concat and split functions to the ql module, and added corresponding unit tests. (Architecture-related: public API)
  ↳ [#1807](https://github.com/jemalloc/jemalloc/pull/1807): [0dc95a8](https://github.com/jemalloc/jemalloc/commit/0dc95a882fee426a62cb93e7fe6a5b1ac171f9a2)
- Add rotate, concat_split and move functions to the ql module, and add corresponding test cases. (Architecture-related: public API)
  ↳ [#1807](https://github.com/jemalloc/jemalloc/pull/1807): [1dd24ca](https://github.com/jemalloc/jemalloc/commit/1dd24ca6d2daeaeb0b9d90f432809508a98b259b), [4b66297](https://github.com/jemalloc/jemalloc/commit/4b66297ea0b0ed2ec5c4421878a31f5b27448624)
- Added an empty list check function to the ql module, and added corresponding unit tests. (Architecture-related: public API)
  ↳ [#1807](https://github.com/jemalloc/jemalloc/pull/1807): [a62b7ed](https://github.com/jemalloc/jemalloc/commit/a62b7ed92841070932d6aea649ff40933c307cae)
- Added fork processing support to counter module, including prefork, postfork_parent and postfork_child functions. (Architecture-related: platform compatibility)
  ↳ [#1820](https://github.com/jemalloc/jemalloc/pull/1820): [4d970f8](https://github.com/jemalloc/jemalloc/commit/4d970f8bfca76e55abd34ba461a738744d71e879)
- Add fork processing to the stats module, and correctly manage the status of the counter module before and after fork. (Architecture-related: fork processing)
  ↳ [#1820](https://github.com/jemalloc/jemalloc/pull/1820): [f533ab6](https://github.com/jemalloc/jemalloc/commit/f533ab6da623303de5f6621b35e5ec73832a6d22)
- Added the atomic_load_sub_store macro to the atomic operation interface, which is used to implement atomic post-load subtraction and storage operations. (Architecture-related: public API)
  ↳ [#1856](https://github.com/jemalloc/jemalloc/pull/1856): [3cf19c6](https://github.com/jemalloc/jemalloc/commit/3cf19c6e5e8b49c3bbf84bbfeb9ab49b38f0546c)
- Add high-resolution timestamp option to performance analysis function, new configuration parameter prof_time_resolution. (architecture-related: configuration parameters)
  ↳ [#1830](https://github.com/jemalloc/jemalloc/pull/1830): [4aea743](https://github.com/jemalloc/jemalloc/commit/4aea7432795414a72034ef35959078c64c69078e)
- Enable MPSS support on Solaris/Illumos, reuse Linux configuration and adjust address range alignment to large pages. (Architecture-related: platform compatibility)
  ↳ [#1874](https://github.com/jemalloc/jemalloc/pull/1874): [00f06c9](https://github.com/jemalloc/jemalloc/commit/00f06c9beb2509fba2133677c17ec702446b2102)
- HPA central mutex now supports contention statistics. (Architecture-related: public API)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [484f047](https://github.com/jemalloc/jemalloc/commit/484f04733e5bd9908faf502fced6df66ca33f9f9)
- SEC implements thread affinity. Each thread randomly selects a shard when it is used for the first time and fixes it. (Architecture-related: public API)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [ea32060](https://github.com/jemalloc/jemalloc/commit/ea32060f9ca5e14077cda7fa2401a1f91f55ad82)
- Added support for using posix_madvise for page clearing, which will be used first when the system is available. (Architecture-related: platform compatibility)
  ↳ [#1972](https://github.com/jemalloc/jemalloc/pull/1972): [4e3fe21](https://github.com/jemalloc/jemalloc/commit/4e3fe218e90c125a3d9616a0b50e8ccb506e9a44)
- Added experimental thread activity callback function, allowing tracking statistics at a finer granularity than threads. (Architecture-related: public API)
  ↳ [#1970](https://github.com/jemalloc/jemalloc/pull/1970): [1b3ee75](https://github.com/jemalloc/jemalloc/commit/1b3ee75667dd7820808d35d16bfcebdd146be70a)
- Added equivalent support for MADV_DODUMP and MADV_DONTDUMP on FreeBSD, implemented using MADV_CORE and MADV_NOCORE. (Architecture-related: platform compatibility)
  ↳ [#1971](https://github.com/jemalloc/jemalloc/pull/1971): [d2d9410](https://github.com/jemalloc/jemalloc/commit/d2d941017b8a62ee7d835ccfb7b34c54ce32e371)
- Refactored HPA configuration options: removed the obsolete old options, added SEC options, and improved initialization logic and error handling. (Architecture-related: HPA configuration)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [fffcefe](https://github.com/jemalloc/jemalloc/commit/fffcefed338429b43ad29a185067f976fe564d11) | [#1996](https://github.com/jemalloc/jemalloc/pull/1996): [1e3b863](https://github.com/jemalloc/jemalloc/commit/1e3b8636ff02fa2150cd84720727d300455b4c63)
- HPA adds a hugepage eviction counter, and exposes this information through the CTL interface and statistical output. (Architecture-related: public API)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [3ed0b4e](https://github.com/jemalloc/jemalloc/commit/3ed0b4e8a3f53c099ba6b2989b1e38878b40ef9b) | [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [746ea3d](https://github.com/jemalloc/jemalloc/commit/746ea3de6f0c372aebb4d7d56172eb2614c83d2d)
- bit_util adds a new universal popcount implementation and adds corresponding unit tests. (Architecture-related: public API)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [734e72c](https://github.com/jemalloc/jemalloc/commit/734e72ce8fb897bdbcbd48bb994c3778dba50dc6)
- flat bitmap adds bitwise AND, OR, NOT operations and corresponding tests. (Architecture-related: public API)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [9b75808](https://github.com/jemalloc/jemalloc/commit/9b75808be171cc7c586e32ddb9d5dd86eca38669)
- The HPA cleaning mechanism has been expanded from cleaning only completely empty hugepages to cleaning partially empty hugepages, and related metadata management has been reconstructed. (Architecture-related: HPA cleaning mechanism)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [30b9e81](https://github.com/jemalloc/jemalloc/commit/30b9e8162b9127d5c352fc312dfdea5e07d51e56), [70692cf](https://github.com/jemalloc/jemalloc/commit/70692cfb13332678af49f9d3c7bfe1fde65ec1aa)
- HPA adds more fine-grained cleaning statistics, including cleaning rounds, cleaning times, largepages and de-largepages, and exposed through the console interface and statistical output. (Architecture-related: public API)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [b25ee5d](https://github.com/jemalloc/jemalloc/commit/b25ee5d88e07adcb3c085c19654039bb6b32dcf4)
- HPA adds dirty page statistics, and displays dirty page and reserved page information in the statistical output. (Architecture-related: public API)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [d3e5ea0](https://github.com/jemalloc/jemalloc/commit/d3e5ea03c5660ba46b6efcc10ad0b804140e2690)
- The return type of hpdata_purge_begin is changed from void to size_t, and now returns the number of pages to be purged. (Architecture-related: public API)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [dc886e5](https://github.com/jemalloc/jemalloc/commit/dc886e5608d553ff2b8f2538cb8d6595bc90e9ac)
- HPA switches to using the cleanup heuristic of the entire shard and no longer relies solely on local information to decide whether to clean up. (Architecture-related: HPA cleanup strategy)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [56e85c0](https://github.com/jemalloc/jemalloc/commit/56e85c0e47f0a4a19cc0f6c71771ece69ef10080)
- Added fxp_mul_frac function for safely multiplying size_t by fraction without overflow, and added FXP_INIT_PERCENT macro. (Architecture-related: public API)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [caef4c2](https://github.com/jemalloc/jemalloc/commit/caef4c2868fce6b0cc0087c20ba00a5d50b67c3a), [bdb7307](https://github.com/jemalloc/jemalloc/commit/bdb7307ff28cdee92861a32ecae16919cc9af614)
- HPA's hugepage trigger threshold, de-hugepage threshold and dirty page ratio threshold are now configurable through runtime options or configuration files. (Architecture-related: configuration interface)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [4790db1](https://github.com/jemalloc/jemalloc/commit/4790db15ed2bc751f1b96404358a42bd50c8a461), [32dd153](https://github.com/jemalloc/jemalloc/commit/32dd15379696429dc1807c3c05fe125428a6faac), [79f81a3](https://github.com/jemalloc/jemalloc/commit/79f81a3732c434e9b648561bf8ab6ab6bf74385a)
- Added optional internal fragmentation tracking function, records the request size and count of sampling allocation by size class, and provides tuple data through mallctl or statistics output. (Architecture-related: public API)
  ↳ [#1914](https://github.com/jemalloc/jemalloc/pull/1914): [40fa4d2](https://github.com/jemalloc/jemalloc/commit/40fa4d29d3e938765d0b608f92701410ce90b887)
- Global mutex performance analysis adds statistical support for recently allocated and recently dumped mutexes, and adds statistics collection and reset support for prof_stats mutexes. (Architecture-related: public API)
  ↳ [#2009](https://github.com/jemalloc/jemalloc/pull/2009): [8a56d6b](https://github.com/jemalloc/jemalloc/commit/8a56d6b6369487a9595dff69c28ccc88073d643e) | [#1914](https://github.com/jemalloc/jemalloc/pull/1914): [14d689c](https://github.com/jemalloc/jemalloc/commit/14d689c0f990f1f946eae5d4706008882d5457a8)
- Added batch allocation and batch release interfaces in the PAI layer, and implemented batch operations in HPA and SEC to reduce mutex lock competition and improve performance. (Architecture-related: public API)
  ↳ [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [f47b4c2](https://github.com/jemalloc/jemalloc/commit/f47b4c2cd8ed3e843b987ee972d187df45391b69), [1944ebb](https://github.com/jemalloc/jemalloc/commit/1944ebbe7f079e79fbeda836dc0333f7a049ac26), [480f3b1](https://github.com/jemalloc/jemalloc/commit/480f3b11cd61c1cf37c90d61701829a0cebc98da), [cdae670](https://github.com/jemalloc/jemalloc/commit/cdae6706a6dbe6ab75688ea24a82ef4165c3b0b1), [ce93863](https://github.com/jemalloc/jemalloc/commit/ce9386370ad67d4b12dc167600080fe17fcf3113)
- Implement the guard pages function: add mprotect protected pages for extents, and add a new allocation function with guard pages to support bump allocation and caching of small guarded extents. (Architecture-related: guard pages function)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [49b7d7f](https://github.com/jemalloc/jemalloc/commit/49b7d7f0a4731e060df095075bedf6391058a0cd) | [#2062](https://github.com/jemalloc/jemalloc/pull/2062): [deb8e62](https://github.com/jemalloc/jemalloc/commit/deb8e62a837b6dd303128a544501a7dc9677e47a)
- Added ticker_geom_t type, allowing a single ticker object to share state among multiple tick streams to drive events. (Architecture-related: ticker_geom_t type)
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [8edfc5b](https://github.com/jemalloc/jemalloc/commit/8edfc5b1700eab47d64d7cfa6a246ad88f832845)
- Added witness_assert_positive_depth_to_rank function, reconstructed witness_assert_depth_to_rank, and extracted auxiliary function witness_depth_to_rank. (architecture-related: public API)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [9ea235f](https://github.com/jemalloc/jemalloc/commit/9ea235f8feffc5f486f290b49a5a6752adbe70bf)
- Introducing the redesigned hpa_central_t framework, adjusting HPA configuration initialization logic, including dependency checking and HPA support checking. (Architecture-related: public API)
  ↳ [#2092](https://github.com/jemalloc/jemalloc/pull/2092): [d93eef2](https://github.com/jemalloc/jemalloc/commit/d93eef2f405b7c6e2a78f589a5037a26d4bd4d44)
- Add minimum allocation alignment support for ARC architecture, set quantum alignment value to 8 bytes. (Architecture-related: Platform compatibility)
  ↳ [#2070](https://github.com/jemalloc/jemalloc/pull/2070): [2381efa](https://github.com/jemalloc/jemalloc/commit/2381efab5754d13da5104b101b1e695afb442590)
- Changed the number of mutex spins to a configurable option, and added the mutex_max_spin runtime configuration item. (Architecture-related: public API)
  ↳ [#2101](https://github.com/jemalloc/jemalloc/pull/2101): [6f41ba5](https://github.com/jemalloc/jemalloc/commit/6f41ba55ee85ce505d61713650f49f8bbb5bee6b)
- Added min_purge_interval_ms configuration item for HPA to limit the minimum purge interval. (Architecture-related: public API)
  ↳ [#2107](https://github.com/jemalloc/jemalloc/pull/2107): [97da57c](https://github.com/jemalloc/jemalloc/commit/97da57c13afec4690a38adf7c94bf97ccd5bfdff)
- Added support for custom backtrace hook and dump hook, allowing users to inject callbacks to enhance stack traceback. (Architecture-related: public API)
  ↳ [#2119](https://github.com/jemalloc/jemalloc/pull/2119): [f7d46b8](https://github.com/jemalloc/jemalloc/commit/f7d46b81197b9879e1f572f9a4d3bfe3b8f850b9), [a9031a0](https://github.com/jemalloc/jemalloc/commit/a9031a0970df9c999873617423f789bd46bfe619)
- Add openat fallback for architectures that do not support open, and add MADV_NOCORE fallback. (Architecture-related: platform compatibility)
  ↳ [#1645](https://github.com/jemalloc/jemalloc/pull/1645): [6924f83](https://github.com/jemalloc/jemalloc/commit/6924f83cb21f75e1c892d8f469500e12f1a3f5a7)
- Added support for loongarch architecture. (Architecture-related: platform compatibility)
  ↳ [#2146](https://github.com/jemalloc/jemalloc/pull/2146): [2159615](https://github.com/jemalloc/jemalloc/commit/2159615419a90b5473cfd9d3a4cb4700259d8c0b)
- Added nstime_ns_since function, used to obtain the duration since the input time. (Architecture-related: public API)
  ↳ [#2182](https://github.com/jemalloc/jemalloc/pull/2182): [310af72](https://github.com/jemalloc/jemalloc/commit/310af725b0037870f70bf6b94426249f69ca4441)
- Allow setting security check abort hooks through mallctl to avoid calling abort() directly. (Architecture-related: public API)
  ↳ [#2258](https://github.com/jemalloc/jemalloc/pull/2258): [391bad4](https://github.com/jemalloc/jemalloc/commit/391bad4b95839e2c690879ca62b1e904a49a78df)
- In reentrant malloc calls, suppress the initialization of tdata and update the performance sampling threshold to comply with the principle of delayed creation of tdata and speed up control recovery. (Architecture-related: public API)
  ↳ [#1639](https://github.com/jemalloc/jemalloc/pull/1639): [66e07f9](https://github.com/jemalloc/jemalloc/commit/66e07f986d77e0b16fd236bbe3518790717d1a4d)
- Fix amd64 MSVC compilation warning, by adding explicit type conversion and adjusting function signature, eliminating potential data loss warning. (Architecture-related: Platform compatibility)
  ↳ [#1649](https://github.com/jemalloc/jemalloc/pull/1649): [4fe50bc](https://github.com/jemalloc/jemalloc/commit/4fe50bc7d05083d822a34068bdd75e34f067e5e4)
- Added zero value and address checks for debugging to the ehooks module to ensure that the returned memory is correctly zeroed. (Architecture-related: public API)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [a738a66](https://github.com/jemalloc/jemalloc/commit/a738a66b5c43849eb90deef11b391641ce382aa0)
- Changed the nstime_t parameter of profiling related functions from value passing to pointer passing, which is a destructive change. (Architecture-related: public API)
  ↳ [#1700](https://github.com/jemalloc/jemalloc/pull/1700): [45836d7](https://github.com/jemalloc/jemalloc/commit/45836d7fd3edca6e71031bce2291b48c4bb3cf76)
- Allow normal calling of dallocx and sdallocx functions after Thread Specific Data (TSD) destruction. (Architecture-related: public API)
  ↳ [#1707](https://github.com/jemalloc/jemalloc/pull/1707): [d5031ea](https://github.com/jemalloc/jemalloc/commit/d5031ea82441301693a30cad50e0d32d45997bc3)
- Disable memory merging across different mmap regions to maintain sequential allocation and sequence number integrity. (Architecture-related: allocation strategy)
  ↳ [#1717](https://github.com/jemalloc/jemalloc/pull/1717): [ca1f082](https://github.com/jemalloc/jemalloc/commit/ca1f08225134981eb74083e5143be4a9d544ff1a)
- Reconstruct the assertion logic in the malloc fast path, split the size index lookup function into two parts: implementation and assertion, to ensure that it can be executed correctly before malloc is initialized. (Architecture-related: public API)
  ↳ [#1730](https://github.com/jemalloc/jemalloc/pull/1730): [dab81bd](https://github.com/jemalloc/jemalloc/commit/dab81bd315e3eee19552ab68d331f693b205866a)
- Add security checks for size matching on the sdallocx slow path/sampling path, and output more detailed error messages when a size mismatch is detected. (Architecture-related: public API)
  ↳ [#1749](https://github.com/jemalloc/jemalloc/pull/1749): [974222c](https://github.com/jemalloc/jemalloc/commit/974222c626b351256f071d18994c70b79d10a627)
- Introduce the lockedint module, unify the locking access mode of statistical counters, and fix several missing update bugs caused by inconsistent access semantics. (Architecture-related: new module lockedint)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [356aaa7](https://github.com/jemalloc/jemalloc/commit/356aaa7dc65d554806287dfa1849a2d47be9b7a8)
- Rewrite the performance analysis thread event processing logic, fix the sampling threshold reset problem in prof_alloc_rollback(), and adjust the event rollback order in xallocx(). (Architecture-related: public API behavior changes)
  ↳ [#1779](https://github.com/jemalloc/jemalloc/pull/1779): [441d88d](https://github.com/jemalloc/jemalloc/commit/441d88d1c78ecc38a7ffad3f88ea50513dabc0f8) | [#1696](https://github.com/jemalloc/jemalloc/pull/1696): [7e36719](https://github.com/jemalloc/jemalloc/commit/7e3671911f9343a40702801fcbb3833bd98d0c46)
- System memory allocation functions are no longer declared as nothrow on macOS to avoid conflicts with system header files. (Architecture-related: platform compatibility)
  ↳ [#1799](https://github.com/jemalloc/jemalloc/pull/1799): [3b4a03b](https://github.com/jemalloc/jemalloc/commit/3b4a03b92b2e415415a08f0150fdb9eeb659cd52)
- Add atomic fence processing to the edata pointer in the prof_recent record to ensure the security of concurrent access. (Architecture-related: public API concurrency security)
  ↳ [#1722](https://github.com/jemalloc/jemalloc/pull/1722): [857ebd3](https://github.com/jemalloc/jemalloc/commit/857ebd3daf71963e522cdbc51725ad33b7368186)
- Change the initialization of the prof idump counter from when each arena is created to once when prof starts, and add fork processing. (Architecture-related: prof initialization behavior)
  ↳ [#1819](https://github.com/jemalloc/jemalloc/pull/1819): [8be5584](https://github.com/jemalloc/jemalloc/commit/8be558449446a5190bdf661da428ecd6b9fb2a8f) | [#1820](https://github.com/jemalloc/jemalloc/pull/1820): [5083030](https://github.com/jemalloc/jemalloc/commit/508303077b020ba369ab84e3cf233ae224da861b)
- Move the initial wait macro definition related to thread events from the tsd header file to the thread_event header file, and uniformly set the initial wait value of each event to 0. (Architecture-related: thread event initialization)
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [dcea2c0](https://github.com/jemalloc/jemalloc/commit/dcea2c0f8b91d045a58eed6b6b1935719c7acd4b)
- Correct the storage method of usize in the performance analysis last-N record, record the actual size directly, and add related unit tests. (Architecture-related: public API: performance analysis data structure)
  ↳ [#1917](https://github.com/jemalloc/jemalloc/pull/1917): [b549389](https://github.com/jemalloc/jemalloc/commit/b549389e4a491f48ea466dce4fda475bcd6b7936), [09eda2c](https://github.com/jemalloc/jemalloc/commit/09eda2c9b621ced9982514f2e69e4e572e06ca2d)
- Fixed an issue where the security check in the configuration incorrectly implicitly enabled the size check. Now the size check only takes effect when explicitly enabled. (Architecture-related: configuration behavior correction)
  ↳ [#1903](https://github.com/jemalloc/jemalloc/pull/1903): [9e18ae6](https://github.com/jemalloc/jemalloc/commit/9e18ae639f760d9c655e79baa2880e26b32c54db)
- Fixed recursive malloc issue during bootstrap on QNX platform, by disabling TLS and introducing recursion detection mechanism. (Architecture-related: platform compatibility)
  ↳ [#1972](https://github.com/jemalloc/jemalloc/pull/1972): [96a59c3](https://github.com/jemalloc/jemalloc/commit/96a59c3bb59a1d725c266019ca0acf0bc28ff1a5), [986cbe4](https://github.com/jemalloc/jemalloc/commit/986cbe4881609f46897915e75a1e58971a814d84)
- Change the thread name reading function to detect the existence of pthread_getname_np and pthread_get_name_np respectively to be compatible with musl libc. (Architecture-related: platform compatibility)
  ↳ [#1967](https://github.com/jemalloc/jemalloc/pull/1967): [95f0a77](https://github.com/jemalloc/jemalloc/commit/95f0a77fdef6573dc581cc92279f6d9acefa3ebf)
- Add runtime detection of whether MADV_DONTNEED actually clears the page to solve the assertion failure problem that may occur in the QEMU environment. (Architecture-related: platform compatibility)
  ↳ [#2005](https://github.com/jemalloc/jemalloc/pull/2005): [a943172](https://github.com/jemalloc/jemalloc/commit/a943172b732e65da34a19469f31cd3ec70cf05b0)
- In size mismatch release detection, report the wrong pointer address. (Architecture-related: public API)
  ↳ [#2024](https://github.com/jemalloc/jemalloc/pull/2024): [f3b2668](https://github.com/jemalloc/jemalloc/commit/f3b2668b3219e108348b9a28d00c4f805a1b5ab6)
- In fixed-length release error detection, report correct and incorrect memory size information. (Architecture-related: public API)
  ↳ [#2024](https://github.com/jemalloc/jemalloc/pull/2024): [041145c](https://github.com/jemalloc/jemalloc/commit/041145c272711b55f91aa42128b108674a12fd91)
- Fixed the return type error in the extent_can_acquire_neighbor function, changing the incorrect NULL to the correct false. (Architecture-related: public API)
  ↳ [#2079](https://github.com/jemalloc/jemalloc/pull/2079): [4fb93a1](https://github.com/jemalloc/jemalloc/commit/4fb93a18ee56795fab725c23cc0211b0198dda46)
- Fixed the non-monotonic clock processing exception caused by uninitialized nstime in HPA, added the first read flag to hpa_hooks_curtime and initialized the timestamp on the first read, added a millisecond interval calculation function, and added a consistency check to prevent uninitialized calls. (Architecture-related: public API)
  ↳ [#2160](https://github.com/jemalloc/jemalloc/pull/2160): [400c598](https://github.com/jemalloc/jemalloc/commit/400c59895a744068994025cf33f80b56bc960a35) | [#2103](https://github.com/jemalloc/jemalloc/pull/2103): [f58064b](https://github.com/jemalloc/jemalloc/commit/f58064b9321b30bdf9b31715acbe523e4a964adf) | [#2182](https://github.com/jemalloc/jemalloc/pull/2182): [837b37c](https://github.com/jemalloc/jemalloc/commit/837b37c4ce44a1c236e1657a6de80b064af98610)
- Add initialization status tracking for nstime_t in debug builds to prevent uninitialized input from causing silent failures that are difficult to debug, and fix the use of last_purge time in HPA. (Architecture-related: public API)
  ↳ [#2161](https://github.com/jemalloc/jemalloc/pull/2161): [cdabe90](https://github.com/jemalloc/jemalloc/commit/cdabe908d05ba68da248edf1dd9f522af1ec6024)
- Fixed the TSD cleanup problem of jemalloc in FreeBSD system to ensure that the cleanup callback can be called correctly when the thread exits. (Architecture-related: platform compatibility)
  ↳ [#2232](https://github.com/jemalloc/jemalloc/pull/2232): [eb65d1b](https://github.com/jemalloc/jemalloc/commit/eb65d1b07830b285bf7ac7678e964f080cd3916a)
- Fix the problem of SEC being disabled by default on 64k page size platform, adjust the default max_alloc value. (Architecture-related: platform compatibility)
  ↳ [#2245](https://github.com/jemalloc/jemalloc/pull/2245): [a939315](https://github.com/jemalloc/jemalloc/commit/a93931537e3845c8baca6965aded9a9683fa1481)
- Change the prof_backtrace function to accept the tsd parameter, and thread local data is passed in by the caller to support correct reentrancy protection. (Architecture-related: public API)
  ↳ [#1620](https://github.com/jemalloc/jemalloc/pull/1620): [93d6151](https://github.com/jemalloc/jemalloc/commit/93d61518005d868c08b597a2d39bdd1775b2a211)
- Changed the parameter type in the profiling code path from tsdn_t to tsd_t, and restructured the relevant function interface. (Architecture-related: public API)
  ↳ [#1689](https://github.com/jemalloc/jemalloc/pull/1689): [6945371](https://github.com/jemalloc/jemalloc/commit/694537177851b52851b89bf59f1692d2b9e348aa)
- Removed the usize parameter that is no longer needed in profiling related functions and simplified the interface. (Architecture-related: public API)
  ↳ [#1696](https://github.com/jemalloc/jemalloc/pull/1696): [5e0b090](https://github.com/jemalloc/jemalloc/commit/5e0b090992ba4399b65c177cd30d56cc69c96646)
- Renamed the prof_tctx field in the prof_info_t structure to alloc_tctx, and updated all related references simultaneously. (Architecture-related: public API)
  ↳ [#1696](https://github.com/jemalloc/jemalloc/pull/1696): [aa1d71f](https://github.com/jemalloc/jemalloc/commit/aa1d71fb7ab34ce96743753f08a761747b5449c8)
- Reconstructed profiling related functions, deleted prof_sample_check, simplified the interfaces of prof_sample_accum_update and prof_sample_should_skip, and removed the alloc_ctx parameter in prof_alloc_time_get/set. (Architecture-related: public API)
  ↳ [#1696](https://github.com/jemalloc/jemalloc/pull/1696): [dfdd46f](https://github.com/jemalloc/jemalloc/commit/dfdd46f6c1e136b57cc943a8569f7f95312f88c6)
- Reconstructed the prof_tctx destruction path, centralized the destruction judgment and execution logic into prof_data.c, and added the prof_tctx_try_destroy function. (Architecture-related: public API)
  ↳ [#1699](https://github.com/jemalloc/jemalloc/pull/1699): [7d2bac5](https://github.com/jemalloc/jemalloc/commit/7d2bac5a384a2fded203298c36ce91b24cbbd497)
- A new base_t pointer member is added to the edata_cache structure, the base parameter is passed in during initialization, and the base parameter in the edata_cache_get function is removed. (Architecture-related: public API)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [c792f3e](https://github.com/jemalloc/jemalloc/commit/c792f3e4abd856933d4043a2b8f5fc2477c5d93d)
- Moved the associated index fields from the base structure into the ehooks structure, and added an interface to obtain the index. (Architecture-related: public API)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [57fe99d](https://github.com/jemalloc/jemalloc/commit/57fe99d4be118a1f34b45013be962f31f7786703)
- Removed the arena_ind parameter from ehooks related functions and changed it to obtain it internally through ehooks_t. (Architecture-related: public API)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [9cad563](https://github.com/jemalloc/jemalloc/commit/9cad5639ff7bca9f33b161363252ae868cec1d34)
- Reconstructed the profiling information setting function, explicitly defining three setters: prof_tctx_reset, prof_tctx_reset_sampled and prof_info_set. (architecture-related: public API)
  ↳ [#1702](https://github.com/jemalloc/jemalloc/pull/1702): [4afd709](https://github.com/jemalloc/jemalloc/commit/4afd709d1f3ae7a727f144a96d8b834157d31e17)
- Reconstructed performance analysis-related header files, moved internal function implementations to source files and adjusted variable references, reducing external exposure. (Architecture-related: public API)
  ↳ [#1708](https://github.com/jemalloc/jemalloc/pull/1708): [ea42174](https://github.com/jemalloc/jemalloc/commit/ea42174d07c2cf496e407bfae74be866ee090b2f)
- Removed the commit parameter in the ecache allocation function, and all callers directly use committed memory. (Architecture-related: public API)
  ↳ [#1737](https://github.com/jemalloc/jemalloc/pull/1737): [bd3be8e](https://github.com/jemalloc/jemalloc/commit/bd3be8e0b169e8a3952cbed1a399cfffe9023862)
- Unified the internal synchronization mechanism of counter_accum_t into the LOCKEDINT macro, and added a fork processing function to make the counter module more universal. (Architecture-related: Universal counter module)
  ↳ [#1733](https://github.com/jemalloc/jemalloc/pull/1733): [d71a145](https://github.com/jemalloc/jemalloc/commit/d71a145ec1bb8153c3d69be27eea5b076d59abfe) | [#1817](https://github.com/jemalloc/jemalloc/pull/1817): [b543c20](https://github.com/jemalloc/jemalloc/commit/b543c20a9494eb8ace71742657f90d81e6df9f49), [fc052ff](https://github.com/jemalloc/jemalloc/commit/fc052ff7284ef3695b81b9127f7d8a7cb25ae0b2)
- Renamed buffer writer related type and function names from buf_write_arg_t to buf_writer_t, and updated all call points uniformly. (Architecture-related: public API)
  ↳ [#1748](https://github.com/jemalloc/jemalloc/pull/1748): [bdc08b5](https://github.com/jemalloc/jemalloc/commit/bdc08b51581d422189e32ee87724e668f0fa5ef2)
- The extent_dalloc_gap function signature has been modified to receive the ehooks parameter directly and no longer obtain it from within arena. (Architecture-related: public API: function signature change)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [3192d6b](https://github.com/jemalloc/jemalloc/commit/3192d6b77dae3b4aa36b95eea793fcdea6f5ffbd)
- Change the parameters of the pa_expand function from new_usize to old_size and new_size to simplify the statistical logic. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [7495856](https://github.com/jemalloc/jemalloc/commit/74958567a4fb1917cc6c1e9d5ee98378a8781f1a)
- Make the file opening and writing operations of the prof module replaceable to support simulating file operation failure scenarios in tests. (Architecture-related: public API)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [21e44c4](https://github.com/jemalloc/jemalloc/commit/21e44c45d994798d50df9fa77c905465a38a4675), [7455813](https://github.com/jemalloc/jemalloc/commit/7455813e5762c93fd2dcaf0672324dffa8aae5a2)
- Change the fit function parameter of the eset module from a Boolean value to the logarithmic value of the maximum fitting ratio, which enhances module independence and testability. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [7bb6e2d](https://github.com/jemalloc/jemalloc/commit/7bb6e2dc0d526bac72d2ed531ddb60fd10a5a5e4)
- Parameterize access to global variables in the eset module, and add the exact_only parameter to decouple module dependencies. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [f730577](https://github.com/jemalloc/jemalloc/commit/f730577277ace08287bb8eedce75e49d35aeb0ba)
- Removed redundant edata_cache parameters in multiple extent operation functions, and instead directly accessed its internal edata_cache through the passed in pa_shard_t, simplifying the interface. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [93b99dd](https://github.com/jemalloc/jemalloc/commit/93b99dd14054886f3d25305b08b8c0f75f289fc4)
- Simplified the emap splitting interface and removed the szind and slab parameters because they have become constants. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [bb6a418](https://github.com/jemalloc/jemalloc/commit/bb6a418523718c40e8f7c14eb677435911eb7a18)
- Move the thread event waiting time update function from the public header file to the source file and change it to internal implementation. (Architecture-related: public API)
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [6de7779](https://github.com/jemalloc/jemalloc/commit/6de77799de0d8a705c595aa11f9dc70f147501ad)
- Changed the parameter type of the thread name allocation function from tsdn to tsd, and updated the related call points. (Architecture-related: public API)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [adfd9d7](https://github.com/jemalloc/jemalloc/commit/adfd9d7b1d69a997a74193bf9d03951616f22ba6)
- Reconstructed the prof data dump interface, changed the global write callback to be passed explicitly through parameters, and simplified the relevant function signature. (Architecture-related: public API)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [1f5fe3a](https://github.com/jemalloc/jemalloc/commit/1f5fe3a3e38deaa75d32589a364163060e0ab3b3), [d4259ea](https://github.com/jemalloc/jemalloc/commit/d4259ea53bb842169688f5fcda1053fbbaf021a8)
- Changed the index of ffs series functions to start from 0, and adjusted the calling logic in bitmap operation and pages_map accordingly. (Architecture-related: public API)
  ↳ [#1888](https://github.com/jemalloc/jemalloc/pull/1888): [1ed0288](https://github.com/jemalloc/jemalloc/commit/1ed0288d9c471771eba98ad5c3f6981fa922e7c4)
- Removed the unused tsdn parameter in the geom_grow_init function and simplified the interface. (Architecture-related: public API)
  ↳ [#1910](https://github.com/jemalloc/jemalloc/pull/1910): [c574948](https://github.com/jemalloc/jemalloc/commit/c57494879fe12157470cefc44bbd121726ec363a)
- The atomic function of PRNG has been removed, all random number generation functions no longer support multi-thread safety, the state parameters have been changed from atomic types to ordinary pointers, and the API and testing have been simplified. (Architecture-related: public API)
  ↳ [#1909](https://github.com/jemalloc/jemalloc/pull/1909): [9e6aa77](https://github.com/jemalloc/jemalloc/commit/9e6aa77ab9d8dd5b00018bdca5adff23b03cbdb8)
- Removed repeated reentrancy checks in profiling, which are handled uniformly by the thread event module; at the same time, a size parameter was added to the prof_info_set function to pass the allocation size. (Architecture-related: public API)
  ↳ [#1922](https://github.com/jemalloc/jemalloc/pull/1922): [866231f](https://github.com/jemalloc/jemalloc/commit/866231fc6166b9c937ce071c5717844998a51413) | [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [703fbc0](https://github.com/jemalloc/jemalloc/commit/703fbc0ff584e00899b5b30aa927c55ecc89dabf)
- Rename geom_grow related functions and types to exp_grow. (architecture-related: public API)
  ↳ [#1975](https://github.com/jemalloc/jemalloc/pull/1975): [4ca3d91](https://github.com/jemalloc/jemalloc/commit/4ca3d91e96c316d3baf67ce4846c164819e2697c)
- Changed the allocation and release interface of hpdata to use address and byte size, simplifying the use by callers. (Architecture-related: public API)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [0971e1e](https://github.com/jemalloc/jemalloc/commit/0971e1e4e33edf1cd0d5be808d1eb092ffeab9f3)
- Change the extent_alloc_wrapper function to an internal static function, and set the is_head flag for its allocated extent when retain mode is enabled to maintain consistency. (Architecture-related: public API)
  ↳ No PR: [22be724](https://github.com/jemalloc/jemalloc/commit/22be724af4438014245c0336ac7212fe97ad004b)
- Renamed the prof.dump_prefix option to prof.prefix, and updated related function and variable names to comply with naming specifications. (Architecture-related: public API: configuration item renaming)
  ↳ [#2110](https://github.com/jemalloc/jemalloc/pull/2110): [5884a07](https://github.com/jemalloc/jemalloc/commit/5884a076fb858320e7bcf86b961dd1555a81a75e) | [#1623](https://github.com/jemalloc/jemalloc/pull/1623): [4b76c68](https://github.com/jemalloc/jemalloc/commit/4b76c684bb8d7f0b7960bfac84391e9fd51a234e)
- In the fixed-length release fast path, mark slab as true, and add compile-time and run-time assertions to ensure that the searchable size is small objects. (Architecture-related: allocator behavior)
  ↳ [#2168](https://github.com/jemalloc/jemalloc/pull/2168): [7dcf778](https://github.com/jemalloc/jemalloc/commit/7dcf77809c9886e3892e29954d90b838af1292c3)
- Refactored the CPU number deterministic check logic, extracted it into an independent function and called it only when necessary; also expanded support for FreeBSD and DragonFly systems, and optimized the handling of non-deterministic situations, allowing use cases where narenas has been set to not generate warnings. (Architecture-related: platform compatibility)
  ↳ [#2184](https://github.com/jemalloc/jemalloc/pull/2184): [60b9637](https://github.com/jemalloc/jemalloc/commit/60b9637cc0c5e88518d03e23de8538523757f060)
- Renamed function san_enabled() to san_guard_enabled(). (architecture-related: public API)
  ↳ [#2173](https://github.com/jemalloc/jemalloc/pull/2173): [dfdd756](https://github.com/jemalloc/jemalloc/commit/dfdd7562f55a409a1667a00595349804fe55cace)
- Added PAGE_FLOOR macro, replacing bit operations in sec.c to correctly calculate the page alignment lower limit of the maximum allocation size. (Architecture-related: internal interface)
  ↳ [#2236](https://github.com/jemalloc/jemalloc/pull/2236): [5bf03f8](https://github.com/jemalloc/jemalloc/commit/5bf03f8ce5802b90a16b595e962fe4f07ce7fe93)
- Renamed zero_realloc option name from strict to alloc to describe its behavior more accurately. (Architecture-related: public API)
  ↳ [#2253](https://github.com/jemalloc/jemalloc/pull/2253): [0e29ad4](https://github.com/jemalloc/jemalloc/commit/0e29ad4efa3d1c5ae9cd01afd32812dd18875200)
- Merge prof inline function header files to eliminate circular dependencies. (Architecture-related: dependency reorganization)
  ↳ [#1819](https://github.com/jemalloc/jemalloc/pull/1819): [e6cb691](https://github.com/jemalloc/jemalloc/commit/e6cb6919c0c1c94e387ccec79190647a44eb7180)
- Move retained statistics to the page allocation module, and change fields such as base, resident, metadata_thp from atomic types to ordinary integers, and calculate them on demand. (Architecture-related: Module responsibility adjustment)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [d0c4321](https://github.com/jemalloc/jemalloc/commit/d0c43217b5bbcf263a4505cad3eaeecc47ac6aa7)
- Remove the te_alloc_rollback() function, its declaration and corresponding tests. (Architecture-related: public API removal)
  ↳ [#1779](https://github.com/jemalloc/jemalloc/pull/1779): [a578059](https://github.com/jemalloc/jemalloc/commit/a5780598b3963648e217c89872e98b40d3e7b4ea)
- Change the two internal functions in the pa module from public declaration to static, hiding implementation details. (Architecture-related: module internal interface hiding)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [65698b7](https://github.com/jemalloc/jemalloc/commit/65698b7f2e3613be8e848053213a850dd5a2cf92)
- Move the mutex lock inside the geom_grow structure to the pac structure, and update the relevant code. (Architecture-related: Internal lock structure reorganization)
  ↳ [#1910](https://github.com/jemalloc/jemalloc/pull/1910): [5e90fd0](https://github.com/jemalloc/jemalloc/commit/5e90fd006e97d62d74c79ce67cbf0cae5429ecdc)
- Refactor HPA related code, extract hooks types and auxiliary functions, and adjust the type definition position. (Architecture-related: HPA hooks interface)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [94cd944](https://github.com/jemalloc/jemalloc/commit/94cd9444c5eecdeea871f008a1e2d805d48dfe5d) | [#2084](https://github.com/jemalloc/jemalloc/pull/2084): [113938b](https://github.com/jemalloc/jemalloc/commit/113938b6f43d528793e029d55ae51e21094b79bc)
- Added unit tests for the hpdata module, covering allocation, release and cleanup processes. (Architecture-related: Core module hpdata test)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [d9f7e6c](https://github.com/jemalloc/jemalloc/commit/d9f7e6c66899b29976cd6ec828ee0f14d4db3aac)
- Optimized the judgment logic of the default merge hook to avoid unnecessary iealloc overhead when the user only uses the default merge hook; at the same time, the relevant function signatures were simplified and redundant arena index parameters were removed. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [6342da0](https://github.com/jemalloc/jemalloc/commit/6342da0970257187f5fcc9504301eba75f92ccca)
- Made last-N profiling data export non-blocking, allowing sampling allocations to continue by batching and releasing locks between batches, and added independent mutex protection. (Architectural event: jemalloc_Memory_Allocator module changes)
  ↳ [#1722](https://github.com/jemalloc/jemalloc/pull/1722): [a835d9c](https://github.com/jemalloc/jemalloc/commit/a835d9cf85286cb0f05c644790df48461544c4d9), [3e19ebd](https://github.com/jemalloc/jemalloc/commit/3e19ebd2ea5372c2f5932af6bb268ae8cb5df354)
- edata_cache_small_t was introduced in HPA, replacing the original global edata_cache to reduce lock contention, and adding a new hpa_shard_disable function to disable the cache. (Architecture event: HPA module change)
  ↳ [#1969](https://github.com/jemalloc/jemalloc/pull/1969): [5896381](https://github.com/jemalloc/jemalloc/commit/589638182ae58ae8031eac2cd9ba9d5b05783b42)
- Switched the bitmap implementation of eset and psset from bitmap to flat bitmap, simplifying the code and improving performance. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [154aa5f](https://github.com/jemalloc/jemalloc/commit/154aa5fcc102172fcac0e111ff79df9d5ced7973), [6bddb92](https://github.com/jemalloc/jemalloc/commit/6bddb92ad64ee096a34c0d099736c237d46f1065) | [#1907](https://github.com/jemalloc/jemalloc/pull/1907): [b399463](https://github.com/jemalloc/jemalloc/commit/b399463fba68d7098d52123b513ab51a2e1ace49)
- Under the MSVC compiler, change the JEMALLOC_ALWAYS_INLINE macro to use the __forceinline keyword. (Architecture-related: platform compatibility)
  ↳ No PR: [c462753](https://github.com/jemalloc/jemalloc/commit/c462753cc8e1d70318b6fcc4ffa0b8498588205c)
- Add CPU spin wait instruction support for ARM32/64 architecture, detect yield instructions in configuration and set related macros. (Architecture-related: platform compatibility)
  ↳ [#1835](https://github.com/jemalloc/jemalloc/pull/1835): [33372cb](https://github.com/jemalloc/jemalloc/commit/33372cbd4075e70b1e365a6dd6708edd0d68c3a4)
- Add build support for DragonFlyBSD, adapting to the platform when the background thread settings name and profiling mapping file are opened. (Architecture-related: platform compatibility)
  ↳ [#1964](https://github.com/jemalloc/jemalloc/pull/1964): [ef6d51e](https://github.com/jemalloc/jemalloc/commit/ef6d51ed44ab864e6db8722a19758f67cc7b12d9)
- Added autoconf detection support for posix_madvise and POSIX_MADV_DONTNEED. (Architecture-related: build and installation methods)
  ↳ [#1972](https://github.com/jemalloc/jemalloc/pull/1972): [26c1dc5](https://github.com/jemalloc/jemalloc/commit/26c1dc5a3aa49e95bfdf5af0d01d784a67edf0cb)
- Fixed FreeBSD 14 build issues, detecting and adapting Linux CPU affinity API compatibility during configuration. (Architecture-related: platform compatibility)
  ↳ [#2169](https://github.com/jemalloc/jemalloc/pull/2169): [113e8e6](https://github.com/jemalloc/jemalloc/commit/113e8e68e1932065125acf66fa087a2e6e11b509)
- Apply fix for FreeBSD systems not to declare system functions as nothrow. (Architecture-related: Platform Compatibility: FreeBSD system functions nothrow declaration)
  ↳ [#2198](https://github.com/jemalloc/jemalloc/pull/2198): [c9946fa](https://github.com/jemalloc/jemalloc/commit/c9946fa7e679f9e9b739be83aff1b6a85cf8d78c)
- Fixed the -Wundef warning generated when LG_SLAB_MAXREGS is not defined, and changed the conditional compilation macro to CONFIG_LG_SLAB_MAXREGS. (Architecture-related: Conditional compilation macros and platform compatibility)
  ↳ [#1937](https://github.com/jemalloc/jemalloc/pull/1937): [7ad2f78](https://github.com/jemalloc/jemalloc/commit/7ad2f7866343265f570dc83b2f2df163ef0c03f9)
- Added multiple status fields and added consistency assertions in the hpdata initialization function, strengthening parameter verification and status checking at API boundaries. (Architecture-related: public API enhancement)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [a559caf](https://github.com/jemalloc/jemalloc/commit/a559caf74aa5421f608a59bd2d38da688b1f2572)
- Adjust LQ_QUANTUM on mips64 hardware to 4 to comply with ABI stack alignment requirements. (Architecture-related: Platform compatibility: mips64 ABI alignment)
  ↳ [#1840](https://github.com/jemalloc/jemalloc/pull/1840): [27f29e4](https://github.com/jemalloc/jemalloc/commit/27f29e424ba9c4f8208e9dd98cb3d39eeb76d5ee)
- Add labels to memory mapping pages on macOS so that analysis tools such as vmmap can identify the mapping source. (Architecture-related: platform compatibility)
  ↳ [#2017](https://github.com/jemalloc/jemalloc/pull/2017): [35a8552](https://github.com/jemalloc/jemalloc/commit/35a8552605be4fcbded961bf2dcbee5655401575)
- Removed undefined extent_size_quantize function declaration. (Architecture-related: public API)
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [ce5b128](https://github.com/jemalloc/jemalloc/commit/ce5b128f1006cb8bde04b633bfc43a4881e76490) | [#2145](https://github.com/jemalloc/jemalloc/pull/2145): [26f5257](https://github.com/jemalloc/jemalloc/commit/26f5257b88c925357bc524444a61049905e7bd19)
- Added static constant pages_can_hugify in pages.h, which is used to detect whether the system supports hugepage related operations at compile time. (Architecture-related: Platform compatibility: hugepage detection)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [63677dd](https://github.com/jemalloc/jemalloc/commit/63677dde631e089c4dc00b6cca5e6e03ac9fdc90)
- Reserve pointer fields in the edata structure to reserve space for subsequent support of large page allocators. (Architecture-related: reserved fields in the edata structure)
  ↳ [#1857](https://github.com/jemalloc/jemalloc/pull/1857): [ae541d3](https://github.com/jemalloc/jemalloc/commit/ae541d3fabd679c97326e81b652fa3979e734404)

### Metadata Lookup (Radix Tree)
- Separated the introspection function in the extent module into an independent module, and updated the relevant interfaces and type names. (Architecture-related: introspection function independent modularization)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [403f2d1](https://github.com/jemalloc/jemalloc/commit/403f2d1664acfae920e8e6ce51e2695d826a0628)
- Added emap module, which is used to extract operations related to addresses and edata, szind, slab status, and added lock tracking. (Architecture-related: new emap module)
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [01f2551](https://github.com/jemalloc/jemalloc/commit/01f255161c97fac5a64517a0366d59eb8afdeae0)
- Migrated multiple functions in the extent module (such as rtree writing, boundary registration, slab area management, splitting and merging, alloc_ctx search, etc.) to the emap module, and restructured the relevant interfaces to unify metadata management responsibilities. (Architecture event: Unification of emap module responsibilities)
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [ca21ce4](https://github.com/jemalloc/jemalloc/commit/ca21ce4071d14b3cbbb88697bfd76a30b9de7ac8), [d05b61d](https://github.com/jemalloc/jemalloc/commit/d05b61db4a4ac9ba498d2a478f65035935d776ba), [9b5ca0b](https://github.com/jemalloc/jemalloc/commit/9b5ca0b09df207de4abe02ccaedd018fc2deed77), [44f5f53](https://github.com/jemalloc/jemalloc/commit/44f5f5360598b57b9d701f6b544f5cd2acd4df9c), [7c7b702](https://github.com/jemalloc/jemalloc/commit/7c7b7020640488f26fb81143ab2ca7c74377580b), [0586a56](https://github.com/jemalloc/jemalloc/commit/0586a56f39845433faa54cea5be56b80e14b2570), [231d147](https://github.com/jemalloc/jemalloc/commit/231d1477e5d8dd591d2f51c1c884ac58fc7adb2c), [65a54d7](https://github.com/jemalloc/jemalloc/commit/65a54d771467df1d2144ae3da9ebf4ae2388bd4d), [f7d9c6c](https://github.com/jemalloc/jemalloc/commit/f7d9c6c42d51af2a06048e64b1a35a39c143eb4a)
- Removed the awareness of szind and slab from the extent module, and transferred the relevant responsibilities to the emap and pa modules, thus simplifying the extent interface. (Architecture event: The extent module responsibilities were transferred to the emap and pa modules)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [5028975](https://github.com/jemalloc/jemalloc/commit/50289750b369e50265b1f74fa3dd895552b30615)
- Changed jemalloc.c to use the emap interface, added fast search and update functions, and unified some function naming. (Architecture-related: interface changes)
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [06e4209](https://github.com/jemalloc/jemalloc/commit/06e42090f7ff42d944dbf318dd24eeac43e59255)
- Migrate the iealloc function to the emap module, replace all call points with emap_lookup or emap_edata_lookup, and remove direct access to the internal structure of emap, instead using encapsulated interfaces for metadata query. (Architecture-related: module responsibility migration)
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [9b5d105](https://github.com/jemalloc/jemalloc/commit/9b5d105fc36e719869f3e113d0d2dc16cf24a60c), [ac50c1e](https://github.com/jemalloc/jemalloc/commit/ac50c1e44b1a34b27ca72ada25a65d685253e2c2)
- Added tracking of extent is_head status in rtree leaf nodes, and reconstructed related bit encoding and decoding logic. (Architecture-related: rtree leaf node expansion)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [70d1541](https://github.com/jemalloc/jemalloc/commit/70d1541c5b60ffd3089d312f3e4e534c72738aaf)
- Store the status information of edata to rtree leaf nodes, and align the edata_t structure to 128 bytes. At the same time, the relevant test code is updated to support aligned allocation. (Architecture-related: edata alignment and status storage)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [4d8c22f](https://github.com/jemalloc/jemalloc/commit/4d8c22f9a57fb29d39394e2382628854542d1520)
- Replaced the dumpable bit with the ranged bit in the edata structure, which is used to mark whether it is currently owned by the range allocator, and updated the relevant access functions and initialization logic. (Architecture-related: edata structure bit field)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [12eb888](https://github.com/jemalloc/jemalloc/commit/12eb888e54572c417c68495fa5be75d9f8402f81) | [#1904](https://github.com/jemalloc/jemalloc/pull/1904): [e034500](https://github.com/jemalloc/jemalloc/commit/e034500698fe74d4a82cf44131eda0110862f4e8)
- Refactored the malloc_usable_size implementation, split it into inline and exported functions to support the Darwin platform, and added a new batch allocation function batch_alloc. (Architecture-related: platform compatibility)
  ↳ [#2138](https://github.com/jemalloc/jemalloc/pull/2138): [cf97245](https://github.com/jemalloc/jemalloc/commit/cf9724531af2864b243668d82aa63114e9737bfd)
- Added rtree_write_range function, supports batch writing of leaf nodes, and optimized the performance of emap_register_interior and emap_deregister_interior. (Architecture-related: public API)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [7c964b0](https://github.com/jemalloc/jemalloc/commit/7c964b03524de23eeff7fe203c764c7a0c0977ac)
- Added sized-delete size checking function, which checks the parameters of each sized delete while maintaining the fast path. (Architecture-related: allocator behavior)
  ↳ [#1898](https://github.com/jemalloc/jemalloc/pull/1898): [eaed1e3](https://github.com/jemalloc/jemalloc/commit/eaed1e39be8574b1a59d21824b68e31af378cd0f), [53084cc](https://github.com/jemalloc/jemalloc/commit/53084cc5c285954d576b2f4a19a230a853014f82)
- When opt_prof is closed, restrict access to prof-related mallctl and ensure that the global prof mutex is initialized. (Architecture-related: public API)
  ↳ [#2124](https://github.com/jemalloc/jemalloc/pull/2124): [523cfa5](https://github.com/jemalloc/jemalloc/commit/523cfa55c5b350decb5efc11083c4bc366cd98c4)
- Added ctl interface for experimental_infallible_new option. (Architecture-related: public API)
  ↳ [#2155](https://github.com/jemalloc/jemalloc/pull/2155): [37342a4](https://github.com/jemalloc/jemalloc/commit/37342a4d32797fdc029dde296cbef618c849608b)
- Added prof_leak_error option. If a memory leak is detected after enabling it, the process will exit with error code 1. (Architecture-related: public API)
  ↳ No PR: [b798fab](https://github.com/jemalloc/jemalloc/commit/b798fabdf7c86288f303b1e0bcf877c9ded67c18)
- Protect edata using metadata tracked in rtree leaves, replacing address-based mutex pools, verifying state and arena ownership before accessing neighbor edata. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [1784939](https://github.com/jemalloc/jemalloc/commit/1784939688b86e459ecb39615e463176dd609685)
- Fixed the bug of prof_active switch: when the application is closed, allocated, and then turned on prof_active in sequence, the sampling will be permanently invalid. The sampling counter is now reset correctly, and prof_active_get_unlocked() is used to obtain the status instead. (Architecture-related: public API)
  ↳ [#1604](https://github.com/jemalloc/jemalloc/pull/1604): [9e031c1](https://github.com/jemalloc/jemalloc/commit/9e031c1d1128af879589f5e5c37960edd87238c6)
- Fixed the base_ehooks_get_for_metadata function so that it returns the metadata extension hook correctly. (Architecture-related: public API)
  ↳ [#2180](https://github.com/jemalloc/jemalloc/pull/2180): [bb5052c](https://github.com/jemalloc/jemalloc/commit/bb5052ce90c6ad4b07c665d9ac96952de2f2b443)
- Migrated edata merging related functions from emap.h to extent.h, and updated the calling location. (Architecture event: Header file responsibility migration)
  ↳ [#2037](https://github.com/jemalloc/jemalloc/pull/2037): [3093d94](https://github.com/jemalloc/jemalloc/commit/3093d9455eb179d75ec8a17b1073ee605fb1f0a9)
- Extracted the comparison field of edata into a summary structure, added corresponding acquisition and comparison functions, and cleaned up the old comparison functions. (Architecture event: data structure reconstruction)
  ↳ [#2098](https://github.com/jemalloc/jemalloc/pull/2098): [dc0a4b8](https://github.com/jemalloc/jemalloc/commit/dc0a4b8b2f2daf17a27b4b1fc869ef48d40d3ef2)
- Optimized the rtree context management within the emap module, removed the explicitly passed rtree_ctx parameter, replaced it with automatic acquisition internally, and adjusted the related rtree writing interface. (Architecture-related: public API)
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [1d449bd](https://github.com/jemalloc/jemalloc/commit/1d449bd9a6aca25f3cdfc58545f4857f52f36b12)
- Standardized the naming of emap modules: uniformly use the emap_ prefix, clearly search for targets, change the alloc_ctx parameter type to emap_alloc_ctx_t, global variable arena_emap_global. (architecture-related: public API)
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [7e6c8a7](https://github.com/jemalloc/jemalloc/commit/7e6c8a72869d00e641404e962a830d635a3cd825)
- The emap_init function adds a Boolean parameter zeroed and passes it to the internal rtree_new call, and the call site has been updated accordingly. (Architecture-related: public API)
  ↳ [#1770](https://github.com/jemalloc/jemalloc/pull/1770): [7013716](https://github.com/jemalloc/jemalloc/commit/7013716aaab806dc6ed2de3437170cdfa2b15a4a)
- rtree's node allocation and deallocation functions now accept a base allocator argument, thus eliminating dependence on global base and simplifying testing. (Architecture-related: Internal interface: Eliminate global dependency)
  ↳ [#1770](https://github.com/jemalloc/jemalloc/pull/1770): [a0c1f4a](https://github.com/jemalloc/jemalloc/commit/a0c1f4ac57abe164cecc027efd697a7f1e0e2db4)
- Removed the field-based access interface in rtree, and instead used unified edata and metadata structures for reading and writing, and added functions such as rtree_contents_encode, rtree_leaf_elm_lookup_fast and emap_deregister_boundary to support the new access mode. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [79ae7f9](https://github.com/jemalloc/jemalloc/commit/79ae7f9211e367f0ecc8be24439af73bd3a4ebc4), [dc26b30](https://github.com/jemalloc/jemalloc/commit/dc26b3009450aadaffdf2f3e91ff5c41548796d4)
- Add documentation comments to the public interface of the emap module, and change functions that are no longer used externally to static hiding. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [08eb1e6](https://github.com/jemalloc/jemalloc/commit/08eb1e6c3164b90cebe0f28bb07c0586a74f3c9e)

### Arena Manager
- Introduce the ecache module, wrap eset and add a mutex lock, migrate arena related code. (Architecture-related: introduce the ecache module)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [bb70df8](https://github.com/jemalloc/jemalloc/commit/bb70df8e5babcf2779230d40b6a34fb04187c818)
- Introducing the PAC module, migrating core data structures such as ecache to the pac substructure, and adding new integrated functions. (Architecture-related: introducing the PAC module)
  ↳ [#1856](https://github.com/jemalloc/jemalloc/pull/1856): [777b0ba](https://github.com/jemalloc/jemalloc/commit/777b0ba9655f6b40b19a8a9c485c186ce9adb551)
- Parameterize the global emap and move it into the arena structure, so that the page allocation module can be tested independently. (Architecture-related: Parameterize emap and move it into the arena)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [294b276](https://github.com/jemalloc/jemalloc/commit/294b276fc7b03319bbc829cef5de7dfec71f997c)
- Remove the offset_state field in the arena structure and instead use stack local variables for PRNG randomization to avoid relying on the arena state when tsd is unavailable. (Architecture-related: dependency adjustment)
  ↳ [#1665](https://github.com/jemalloc/jemalloc/pull/1665): [19a51ab](https://github.com/jemalloc/jemalloc/commit/19a51abf337d35b3bdbbac22d8c513f4fd8b6c57), [bc774a3](https://github.com/jemalloc/jemalloc/commit/bc774a3519788bec8b18f0a5988767fc11d034fa)
- Move the percpu_arena_update function from arena_inlines_a.h to jemalloc_internal_inlines_b.h, and adjust the internal implementation to adapt to the new cache bin module. (Architecture-related: public API)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [da68f73](https://github.com/jemalloc/jemalloc/commit/da68f7329666a4375e9df04a0f441bb9ae2b4d6c)
- Migrate page allocation related fields and logic from arena and pa_shard to PAC module, including ecache_grow structure, decay logic, statistical information merging, decay rate setting, etc. (Architecture-related: module responsibility migration)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [acd0bf6](https://github.com/jemalloc/jemalloc/commit/acd0bf6a2697d47fcfd868f76583c9d0a5974af1) | [#1856](https://github.com/jemalloc/jemalloc/pull/1856): [c81e389](https://github.com/jemalloc/jemalloc/commit/c81e389996ef37c0d27b5a28bba0e04337d02a54), [db211ee](https://github.com/jemalloc/jemalloc/commit/db211eefbfe2e35441dad0a7857e073ba4e8130e), [7391382](https://github.com/jemalloc/jemalloc/commit/73913823491ef32a7ea1471de1ef185219e44d41), [6a27747](https://github.com/jemalloc/jemalloc/commit/6a2774719fe6b4cdae35c4a087afc2ef7f8c9110), [471eb59](https://github.com/jemalloc/jemalloc/commit/471eb5913cfdef1d102219ddab683066e3462f43)
- Remove the direct interaction between the extent structure and arena, migrate the page quantization function to the sz module, migrate the default hook implementation to the ehooks module, migrate the profiling test internal interface to the internal header file, and migrate the file processing logic in prof_data to prof_sys. (Architecture-related: module responsibility migration)
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [41187bd](https://github.com/jemalloc/jemalloc/commit/41187bdfb024dcadcb0c279572dd6440084655f3), [820f070](https://github.com/jemalloc/jemalloc/commit/820f070c6b5b7ff44902ddb45b4b8894075a5c96) | [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [c8dae89](https://github.com/jemalloc/jemalloc/commit/c8dae890c88162748c22acbc7885c9ebf8012e10) | [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [8118056](https://github.com/jemalloc/jemalloc/commit/8118056c034aae3b8d3d250bed36e95eae6676a3), [4736fb4](https://github.com/jemalloc/jemalloc/commit/4736fb4fc9c105320c71dad5425a535cebf390b3)
- Add the SEC component in front of the HPA shard, and implement related statistical merging and mutex statistics reading. (Architecture-related: new component)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [6599651](https://github.com/jemalloc/jemalloc/commit/6599651aee2b1b1ab0c52fdb03f23394bd683c47)
- Redesign the HPA implementation, change large page management from global fallback to localization, directly track the status of the entire large page and support cleaning and recycling by large page. (Architecture-related: core architecture reconstruction)
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [43af63f](https://github.com/jemalloc/jemalloc/commit/43af63fff496967bf2173c92737aea1cca4ca025)
- Extract HPA configuration options into the new structure hpa_shard_opts_t, and update related interfaces and test codes. (Architecture-related: HPA configuration extraction)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [b3df80b](https://github.com/jemalloc/jemalloc/commit/b3df80bc797f1578b0f51a6919e18049663ffae1)
- Extract SEC options into structures, add multiple configurable options, and add batch allocation/release interfaces and initialization, refresh, disable and statistical merging functions. (Architecture-related: SEC option extraction)
  ↳ [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [fb32736](https://github.com/jemalloc/jemalloc/commit/fb327368db39a2edca5f9659a70a53bd3bb0ed6c)
- Added pa_decay_stashed function in the page allocation module, and added multiple auxiliary interfaces. (Architecture-related: pa_decay_stashed function)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [3034f4a](https://github.com/jemalloc/jemalloc/commit/3034f4a508524e995864e485f03da3fb2792856a), [26e9a31](https://github.com/jemalloc/jemalloc/commit/26e9a3103d443c45e0fbc7e23754fefb12ea181e)
- Added a new independent mapped field for arena statistical information, and renamed the original page allocation statistical field to pa_mapped to avoid confusion. (Architecture-related: arena statistical field)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [81c6027](https://github.com/jemalloc/jemalloc/commit/81c6027592d59383107b3a7a26caddb787ed10c7), [436789a](https://github.com/jemalloc/jemalloc/commit/436789ad96fcc4a091790b9d380ee31570efa6cf)
- New batch allocation function, including batch allocation from new slab, public API batch_alloc and batch allocation API accessed through mallctl interface. (Architecture-related: public API)
  ↳ [#1828](https://github.com/jemalloc/jemalloc/pull/1828): [49e5c2f](https://github.com/jemalloc/jemalloc/commit/49e5c2fe7d35ffdeb2dc767ab7d3c569eb5c6a40), [978f830](https://github.com/jemalloc/jemalloc/commit/978f830ee300c15460085bdc49b4bdb9ef1a16d8), [f6cf5eb](https://github.com/jemalloc/jemalloc/commit/f6cf5eb388eefd1c48c04d6b8c550105b2ad8c17) | [#1896](https://github.com/jemalloc/jemalloc/pull/1896): [e032a1a](https://github.com/jemalloc/jemalloc/commit/e032a1a1de75cf7faf087406a21789ced2b2f650) | [#1962](https://github.com/jemalloc/jemalloc/pull/1962): [ac48013](https://github.com/jemalloc/jemalloc/commit/ac480136d76010243f50997a1c1231a5572548aa) | [#1992](https://github.com/jemalloc/jemalloc/pull/1992): [e827718](https://github.com/jemalloc/jemalloc/commit/e82771807ec33c6a7db7612158cbfb9af87818b9), [0dfdd31](https://github.com/jemalloc/jemalloc/commit/0dfdd31e0fc69206b7198b52f4bd4a8eb805d8be)
- Added the arenas_ratio configuration item, allowing the number of arenas per CPU to be dynamically set. (Architecture-related: Configuration items)
  ↳ [#1905](https://github.com/jemalloc/jemalloc/pull/1905): [ab274a2](https://github.com/jemalloc/jemalloc/commit/ab274a23b98c228c073f1dfef89d0323fbe8b4c2)
- Page-aligned memory allocation requests can now use small size classes to avoid unnecessary promotion to large sizes. (Architecture-related: core allocation behavior)
  ↳ [#1924](https://github.com/jemalloc/jemalloc/pull/1924): [b35ac00](https://github.com/jemalloc/jemalloc/commit/b35ac00d58529b266598322de2529414c91909cd)
- Add statistical functions to psset, including new purge list management function. (Architecture-related: public API)
  ↳ [#1904](https://github.com/jemalloc/jemalloc/pull/1904): [259c5e3](https://github.com/jemalloc/jemalloc/commit/259c5e3e8f4731f2e32ceac71c66f4bc7d078145) | [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [f51948d](https://github.com/jemalloc/jemalloc/commit/f51948d9e11046ed0b131767bad47879807e2d8b)
- hpa_shard adds statistical information of complete slab and incomplete slab, and integrates HPA related data in the statistical output. (Architecture-related: public API)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [1964b08](https://github.com/jemalloc/jemalloc/commit/1964b08394e01a5b6881013c0f34ee20073cc328)
- HPA's slab size and maximum allocation are now configurable, and two new configuration items, hpa_slab_goal and hpa_slab_max_alloc, have been added. (Architecture-related: configuration interface)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [bf025d2](https://github.com/jemalloc/jemalloc/commit/bf025d2ec8f68fa50c5eb8bdb303a684c3f9c544)
- HPA adds a size exclusion function, allowing only memory within a specific size range to be allocated. (Architecture-related: public API)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [534504d](https://github.com/jemalloc/jemalloc/commit/534504d4a7086084a46ac42c700e9429d2c72fd1)
- Added fixed-point math library to support non-integer narenas_ratio configuration, now narenas_ratio can accept fractional values. (Architecture-related: public API)
  ↳ [#1990](https://github.com/jemalloc/jemalloc/pull/1990): [ecd3941](https://github.com/jemalloc/jemalloc/commit/ecd39418aca14cddcf69acc86c2aa3cbb13a72e1), [d438296](https://github.com/jemalloc/jemalloc/commit/d438296b1fbb898653b9f3f454f3f84b33d30986)
- Each arena can now configure oversize_threshold independently, so that manual arena can trade off memory and CPU like automatic arena. (Architecture-related: public API)
  ↳ [#1980](https://github.com/jemalloc/jemalloc/pull/1980): [cf2549a](https://github.com/jemalloc/jemalloc/commit/cf2549a149dc27eefef1101500cd9ee743e477a0)
- Support any number of shards, cache shard size information, and add delayed work generation parameters for expansion and contraction functions. (Architecture-related: public API)
  ↳ [#2072](https://github.com/jemalloc/jemalloc/pull/2072): [36c6bfb](https://github.com/jemalloc/jemalloc/commit/36c6bfb963e8a36a8918eb841902e006466fb7c2)
- Introduced bump allocator for protected allocations, used to allocate guard extents as small object guard slabs. (Architecture-related: core allocator)
  ↳ [#2151](https://github.com/jemalloc/jemalloc/pull/2151): [800ce49](https://github.com/jemalloc/jemalloc/commit/800ce49c19bc105199cf645172f1e462d70d77c4), [0f6da12](https://github.com/jemalloc/jemalloc/commit/0f6da1257d7182777e47c78f47e0bb2aa28d259b)
- Add experimental experimental.arenas_create_ext mallctl, support configuring arena behavior through arena_config_t, and add metadata_use_hooks option. (Architecture-related: public API)
  ↳ [#2118](https://github.com/jemalloc/jemalloc/pull/2118): [7bb05e0](https://github.com/jemalloc/jemalloc/commit/7bb05e04be693b26536dc2335b4d230dacc5d7d2)
- Fix the crash caused by incorrectly passing pointers in prof_realloc, and reconstruct the profiling data structure to ensure safe delivery of post-free information. (Architecture-related: public API)
  ↳ [#1683](https://github.com/jemalloc/jemalloc/pull/1683): [3b5eecf](https://github.com/jemalloc/jemalloc/commit/3b5eecf102dcc3eb9a4a50346cdfa96917683e0a) | [#1684](https://github.com/jemalloc/jemalloc/pull/1684): [73510df](https://github.com/jemalloc/jemalloc/commit/73510dfd150d0c28d48b15f28f8329a108c53af0) | [#1689](https://github.com/jemalloc/jemalloc/pull/1689): [b55419f](https://github.com/jemalloc/jemalloc/commit/b55419f9b99ab416f035179593370401af8d213f)
- Allow setting the narenas configuration item to default to restore its default value. (Architecture-related: narenas configuration behavior)
  ↳ [#1847](https://github.com/jemalloc/jemalloc/pull/1847): [5dead37](https://github.com/jemalloc/jemalloc/commit/5dead37a9d38494341a6808bd09b8896282becc1)
- When requesting manual arena, it no longer falls back to automatic arena, but directly returns failure. (Architecture-related: arena allocation strategy)
  ↳ [#1849](https://github.com/jemalloc/jemalloc/pull/1849): [e128b17](https://github.com/jemalloc/jemalloc/commit/e128b170a0b884aa34ca7fe3f61e89fc54fce918)
- Huge extents will no longer be cleared when decay is turned off, and a function to determine whether decay is turned on will be added. (Architecture-related: public API)
  ↳ [#1729](https://github.com/jemalloc/jemalloc/pull/1729): [0f552ed](https://github.com/jemalloc/jemalloc/commit/0f552ed673b26b733a290bcac4c4d8ff4d0344e1)
- Disable percpu arena when the number of CPUs is uncertain (such as containers or taskset environments) to avoid assertion failures due to CPU index out-of-bounds. (Architecture-related: core module behavior)
  ↳ [#2181](https://github.com/jemalloc/jemalloc/pull/2181): [cafe9a3](https://github.com/jemalloc/jemalloc/commit/cafe9a315879b357ac3c6d00f3b7f9ad52c33087)
- Reconstruct the internal data structure, split the extent structure into independent header files, migrate the slab data structure and constants, and move the boundary unregistration function to the emap module. (Architecture event: jemalloc_Memory_Allocator module reorganization)
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [723ccc6](https://github.com/jemalloc/jemalloc/commit/723ccc6c2757974112d31d254bcf74bf2beac6ec), [e7cf84a](https://github.com/jemalloc/jemalloc/commit/e7cf84a8dd19af5957f2542934180fe95fdb0885) | [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [6513d9d](https://github.com/jemalloc/jemalloc/commit/6513d9d923d4e32775612614326ff1889807c840)
- Added current time parameters to the initialization and reinitialization functions of the decay module to improve testability. (Architecture-related: public API: Add parameters)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [f77cec3](https://github.com/jemalloc/jemalloc/commit/f77cec311e102a46a58402570b43aa74dc5d7ae7)
- The slab allocation strategy of psset is changed from address-based first-fit to slab age-based first-fit, giving priority to slabs with longer service life. At the same time, statistical maintenance and heap operations are reconstructed. (Architecture-related: public API)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [d16849c](https://github.com/jemalloc/jemalloc/commit/d16849c91da35c37359331195c6213421a17976a)
- Add the arena_get_from_edata auxiliary function, replace many codes that directly access the arenas array, and remove the large_prof_tctx_get function that is no longer needed. (Architecture-related: internal interface encapsulation)
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [3d84bd5](https://github.com/jemalloc/jemalloc/commit/3d84bd57f4954a17059bd31330ec87d3c1876411)
- Remove the rollback logic of prof idump counter, and clean up related code and tests. (Architecture-related: profiling behavior)
  ↳ [#1819](https://github.com/jemalloc/jemalloc/pull/1819): [039bfd4](https://github.com/jemalloc/jemalloc/commit/039bfd4e307df51bd46f164b2af0ffa62142ca5d)

### Thread Cache (tcache)
- Separate the fast path and slow path data of tcache, and optimize the layout of the cache bin in TSD. (Architecture event: tcache fast/slow path data separation)
  ↳ [#1813](https://github.com/jemalloc/jemalloc/pull/1813): [a13fbad](https://github.com/jemalloc/jemalloc/commit/a13fbad374f31a7e6e912c0260b442d134bb0f2e)
- Reconstruct the cache_bin module, restrict internal direct access, unify and simplify interface parameter transfer. (Architecture-related: public API)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [b66c097](https://github.com/jemalloc/jemalloc/commit/b66c0973cc7811498a97783283c8ef06f83d6b9f)
- Move the cache bin initialization code from the tcache module into the cache_bin module, and add low-water tracking and batch allocation/refresh functions. (Architecture-related: Module responsibility adjustment)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [60113df](https://github.com/jemalloc/jemalloc/commit/60113dfe3b0fe89df5b9661ce27754a5a96cb070)
- Explicitly hold dynamically allocated memory pointers in the tcache structure, and simplify related initialization, creation and destruction processes. (Architecture-related: public API)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [0a2fcfa](https://github.com/jemalloc/jemalloc/commit/0a2fcfac013e65a22548eeed09ebcaca1bdb63a3)
- Rewrite the cache bin module, integrate empty, full and low-water status tracking into the bin itself, simplify the status query logic, and add a non-fast path alignment check function; at the same time, change the flush operation from reverse order to forward order to speed up the flush path. (Architecture-related: module rewriting)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [397da03](https://github.com/jemalloc/jemalloc/commit/397da038656589cb3a263d1715ae27f90f6b30d1) | [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [2fcbd18](https://github.com/jemalloc/jemalloc/commit/2fcbd18115c93fb4649d2861dd2e0d3351bf6f6f)
- Build a general thread event processing framework, use thread allocation/release byte count as a general event accumulator, and reconstruct the processing logic of events such as sampling, cache GC and statistical intervals; at the same time, related functions and macros are abbreviated to the te prefix. (Architecture-related: thread event framework)
  ↳ [#1622](https://github.com/jemalloc/jemalloc/pull/1622): [152c0ef](https://github.com/jemalloc/jemalloc/commit/152c0ef954f19fc2bbe53fead9c62c9824f06109) | [#1756](https://github.com/jemalloc/jemalloc/pull/1756): [e896522](https://github.com/jemalloc/jemalloc/commit/e8965226168cdcb359f6db39fdf4c216b47a60cf)
- Decouple the cache_bin module from tcache, pass the cache_bin_info structure through a pointer instead, and change the calculation of ncached_max to a query based on cache_bin_info_t. (Architecture-related: module decoupling)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [909c501](https://github.com/jemalloc/jemalloc/commit/909c501b07c101890c264fd717b0bf8b5cf27156), [74d36d7](https://github.com/jemalloc/jemalloc/commit/74d36d78efdea846d577dea933e4bb06a18efa10)
- Added the ASSURED_WRITE macro in mallctl, forcing the caller to provide input, and migrated the tcache.flush and tcache.destroy interfaces to use this macro. (Architecture-related: ASSURED_WRITE macro)
  ↳ [#1758](https://github.com/jemalloc/jemalloc/pull/1758): [7014f81](https://github.com/jemalloc/jemalloc/commit/7014f81e172290466e1a28118b622519bbbed2b0)
- Added multiple tcache runtime configuration options, including slot number multiplier, slot size, GC interval, GC delay, refresh ratio, etc., and displayed in the statistical output. (Architecture-related: runtime configuration)
  ↳ [#1846](https://github.com/jemalloc/jemalloc/pull/1846): [634afc4](https://github.com/jemalloc/jemalloc/commit/634afc4124100b5ff11e892481d912d56099be1a), [1810931](https://github.com/jemalloc/jemalloc/commit/181093173d589569a846f2d5d4c9e8ca8fd57b5d), [d338dd4](https://github.com/jemalloc/jemalloc/commit/d338dd45d7402df287adb10e82ca98be831ac16b), [ee72bf1](https://github.com/jemalloc/jemalloc/commit/ee72bf1cfd236d6e076d9d9bdfcb09787016d62b), [7503b5b](https://github.com/jemalloc/jemalloc/commit/7503b5b33a9ea446c30e3c51f6ad68660fa6e931), [6cdac3c](https://github.com/jemalloc/jemalloc/commit/6cdac3c573de86c8d59d69fca8f1778bdbec25e0)
- Added thread peak memory tracking function, defined peak_t type and related functions, and exposed through two mallctls thread.peak.read and thread.peak.reset. (Architecture-related: public API)
  ↳ [#1853](https://github.com/jemalloc/jemalloc/pull/1853): [fe71083](https://github.com/jemalloc/jemalloc/commit/fe7108305a449df3d28f68e6bd9ff74dea68946b), [d82a164](https://github.com/jemalloc/jemalloc/commit/d82a164d0ddb5418de3b6a07dd302edddc347129)
- The name of the tcache maximum cache class configuration item is changed from opt.lg_tcache_max to opt.tcache_max, and allows accepting smaller size class values while retaining parsing support for the old configuration items. (Architecture-related: public API)
  ↳ [#1961](https://github.com/jemalloc/jemalloc/pull/1961): [c820915](https://github.com/jemalloc/jemalloc/commit/c8209150f9d219a137412b06431c9d52839c7272) | [#1963](https://github.com/jemalloc/jemalloc/pull/1963): [bf72188](https://github.com/jemalloc/jemalloc/commit/bf72188f80c59328b20441c79861f9373c22bccd) | [#2269](https://github.com/jemalloc/jemalloc/pull/2269): [a7d73dd](https://github.com/jemalloc/jemalloc/commit/a7d73dd4c9ba97bb033f7ae15f218a65d8b8ace6)
- Add proactive double free and sized dealloc detection for large size memory deallocation. (architecture-related: allocator behavior)
  ↳ [#1957](https://github.com/jemalloc/jemalloc/pull/1957): [3de19ba](https://github.com/jemalloc/jemalloc/commit/3de19ba401bd752af37e4f235878f764c8ba55fb)
- Added thread.idle mallctl interface, used to perform internal cleanup logic and release resources. (Architecture-related: public API)
  ↳ [#1743](https://github.com/jemalloc/jemalloc/pull/1743): [6a62286](https://github.com/jemalloc/jemalloc/commit/6a622867cac04d7cdd4cf9cf19b7a367f9108fa5), [d92f017](https://github.com/jemalloc/jemalloc/commit/d92f0175c75b5c9d9fc2bccabd2af0e6ebce7757)
- Add stashed bytes statistics function to tcache. (Architecture-related: public API)
  ↳ [#2173](https://github.com/jemalloc/jemalloc/pull/2173): [e491cef](https://github.com/jemalloc/jemalloc/commit/e491cef9abcc80de7c2648a0a244a5271848099a)
- Fix tcache bin stack alignment problem, set correct alignment for different sizes and pointer widths. (Architecture-related: platform compatibility)
  ↳ [#1624](https://github.com/jemalloc/jemalloc/pull/1624): [ac5185f](https://github.com/jemalloc/jemalloc/commit/ac5185f73e4dc6b8d9a48b7080d07b11ef231765)
- Fix the index type of cache_bin_alloc_easy function, change it from signed type to unsigned type. (Architecture-related: public API)
  ↳ [#1617](https://github.com/jemalloc/jemalloc/pull/1617): [23dc7a7](https://github.com/jemalloc/jemalloc/commit/23dc7a7fba904d3893c0f335dfc2d16439b7109c)
- Fixed the problem of assertion failure due to concurrent memory access, and eliminated the inconsistency by adjusting the stash pointer counting logic. (Architecture-related: public API)
  ↳ [#2226](https://github.com/jemalloc/jemalloc/pull/2226): [ca709c3](https://github.com/jemalloc/jemalloc/commit/ca709c3139f77f4c00a903cdee46d71e9028f6c6)
- Refactor the cache_bin unit test so that it is tested only through the public API and no longer relies on internal implementation details, and fixes related parameter errors and memory release issues. (Architecture-related: public API)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [370c1ea](https://github.com/jemalloc/jemalloc/commit/370c1ea007e152a0f8ede3aad7f69c45d2397e54) | [#1962](https://github.com/jemalloc/jemalloc/pull/1962): [4a65f34](https://github.com/jemalloc/jemalloc/commit/4a65f34930fb5e72b2d6ab55d23b5971a5efefbd)
- Optimized the memory locality of the tcache refresh path, and improved the parallelism when the cache is missing by reconstructing the batch search interface and adding auxiliary functions. (Architecture event: emap interface reconstruction)
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [9f9247a](https://github.com/jemalloc/jemalloc/commit/9f9247a62ed5ac1157519cd2b1f966cacf772aaa)
- Added data prefetching in the tcache flush path, loaded edata content in advance to reduce cache miss latency, and executed on paths that did not acquire locks to reduce lock holding time. (Architecture event: New prefetch function)
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [31a629c](https://github.com/jemalloc/jemalloc/commit/31a629c3dea4c903d16025b4fe5261d2f3db8bd6)
- Allow the fast path to adjust the low water mark after a flush, thus placing more allocations on paths that are nearly as fast, reducing malloc cycles by ~4%. (Architecture-related: allocation path behavior)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [d701a08](https://github.com/jemalloc/jemalloc/commit/d701a085c29df6f6afc9a0b15c4732c8662fe80c)
- Publicly defines the maximum number of cache items constant, and adds a legality check during initialization. (Architecture-related: public API: cache item constant)
  ↳ [#1846](https://github.com/jemalloc/jemalloc/pull/1846): [b58dea8](https://github.com/jemalloc/jemalloc/commit/b58dea8d1b6894eed1616a1264bb9c893194f770)
- Privatize the default value of opt_lg_tcache_max into the implementation file. (Architecture-related: privatization of configuration interface)
  ↳ [#1846](https://github.com/jemalloc/jemalloc/pull/1846): [ec0b579](https://github.com/jemalloc/jemalloc/commit/ec0b5795639fe96883366691e0380eeb0845836b)

### Cross-cutting / Other Architecture-related Changes
- Refactor the core profiling code into two logical parts: prof_data.c is responsible for internal data structure management and dumping, prof.c is responsible for mutex locks and external API. (Architecture-related: separation of module responsibilities)
  ↳ [#1575](https://github.com/jemalloc/jemalloc/pull/1575): [07ce243](https://github.com/jemalloc/jemalloc/commit/07ce2434bf45420ff9d9d22590f68540c6dd7b78)
- Remove the dependence of extent split related functions on arena and use edata_cache and ehooks parameters instead. (Architecture-related: interface changes)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [56cc56b](https://github.com/jemalloc/jemalloc/commit/56cc56b69214bf3dbcd64ad83aa63fe22be20d62)
- Change the extent module header file name from extent2 to extent, and update related references. (Architecture-related: public API changes)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [e210ccc](https://github.com/jemalloc/jemalloc/commit/e210ccc57ed165cc4308a09a9637f5d6e49b0dbd)
- Move page size index type and size class index type from jemalloc_internal_types.h to sz.h, and update related header file references. (Architecture-related: public API)
  ↳ [#1770](https://github.com/jemalloc/jemalloc/pull/1770): [34b7165](https://github.com/jemalloc/jemalloc/commit/34b7165fde9622afe75037a2c8862f53269f10bb)
- Remove the cache index randomization logic in the extent module, and simplify the extent interface so that it only focuses on page-level allocation. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [585f925](https://github.com/jemalloc/jemalloc/commit/585f92505521136157aad8ac2e9288609127f863)
- Migrate the arena_decay_extent function to the extent module. (Architecture-related: public API)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [22a0a7b](https://github.com/jemalloc/jemalloc/commit/22a0a7b93a192a07e9a3e5ba9f5adfa64036219e)
- Migrate caching, statistics and recycling logic related to page allocation from arena to pa_shard module, and remove arena's direct dependence on extent. (Architecture-related: Module responsibilities: Migrate page allocation to pa_shard)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [eba35e2](https://github.com/jemalloc/jemalloc/commit/eba35e2e486ab81f44126d86bbb6555a02072fe2)
- Migrate arena's decay time acquisition function to the pa module, and update related calls to use the new pa_shard interface. (Architecture-related: Module responsibility: Migrate decay time acquisition to pa)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [e77f47a](https://github.com/jemalloc/jemalloc/commit/e77f47a85a5e48894065852cbafef3d78724acef)
- Migrate slab allocation related code to the newly extracted page allocation (pa) module, use edata instead of extent type, and uniformly allocate and recycle through the pa_shard interface. (Architecture-related: Module responsibility: slab allocation is migrated to pa)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [7be3dea](https://github.com/jemalloc/jemalloc/commit/7be3dea82c8489e7e892c72b5f8d0a2901ff4695)
- Move extent statistics to the PA module, and remove atomic operations and replace them with direct assignment. (Architecture-related: Module responsibility: Migrate extent statistics to PA)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [f6bfa3d](https://github.com/jemalloc/jemalloc/commit/f6bfa3dccaa9bb6bfe97aecc32709680b1d47652)
- Move the in_hook field and tsd_link field in tcache into the TSD structure, and update the access methods of related functions. (Architecture-related: Module responsibility: Move the tcache field into TSD)
  ↳ [#1813](https://github.com/jemalloc/jemalloc/pull/1813): [40e7aed](https://github.com/jemalloc/jemalloc/commit/40e7aed59ea1ec8edbeabee71c288afdc2316d72)
- Change the cache filling function of arena from directly relying on tcache to being based on cache_bins, thereby decoupling the internal implementation of arena and tcache. (Architecture-related: Module responsibility: Decoupling arena and tcache)
  ↳ [#1813](https://github.com/jemalloc/jemalloc/pull/1813): [7099c66](https://github.com/jemalloc/jemalloc/commit/7099c66205a9a435edcf1d2c6da56d6a11deb7d8)
- Rename guard-related names to san to lay the foundation for subsequent sanitizer work. (Architecture-related: public API rename)
  ↳ [#2151](https://github.com/jemalloc/jemalloc/pull/2151): [62f9c54](https://github.com/jemalloc/jemalloc/commit/62f9c54d2a9035c6bfdbb4c41ecc0dcb040b509e)
- In the spin lock implementation of the ARM architecture, replace the yield instruction with the isb instruction to introduce a short delay closer to the x86 pause instruction. (Architecture-related: platform compatibility)
  ↳ No PR: [89fe8ee](https://github.com/jemalloc/jemalloc/commit/89fe8ee6bf7a23556350d883a310c0224a171879)
- Add overcommit support for NetBSD, and set alignment flags based on alignment and page size when memory mapping; also add runtime detection of MADV_DONTNEED clearing behavior to be compatible with QEMU. (Architecture-related: platform compatibility)
  ↳ [#1755](https://github.com/jemalloc/jemalloc/pull/1755): [536ea68](https://github.com/jemalloc/jemalloc/commit/536ea6858ecfcac49060c805231bd1722d84a0cf)
- Added a new mallctl interface for dumping the latest N performance analysis records, and added corresponding unit tests. (Architecture-related: mallctl interface)
  ↳ [#1759](https://github.com/jemalloc/jemalloc/pull/1759): [68e8ddc](https://github.com/jemalloc/jemalloc/commit/68e8ddcaffeee1f2a510e0fc00eb510001a4eff4) | [#1760](https://github.com/jemalloc/jemalloc/pull/1760): [9d2cc3b](https://github.com/jemalloc/jemalloc/commit/9d2cc3b0fa8365d69747bf0d04686fe41fe44d3e) | [#1808](https://github.com/jemalloc/jemalloc/pull/1808): [c4e9ea8](https://github.com/jemalloc/jemalloc/commit/c4e9ea8cc6c039af4f14f9e3ad7d92555693adbf)
- Added edata_cache_small_t type, used to amortize the synchronization overhead of edata_cache access; adjusted the naming and initialization logic of related functions. (Architecture-related: edata_cache_small_t type)
  ↳ [#1782](https://github.com/jemalloc/jemalloc/pull/1782): [99b1291](https://github.com/jemalloc/jemalloc/commit/99b1291d1760ad164346073b35ac03ce2eb35e68), [734109d](https://github.com/jemalloc/jemalloc/commit/734109d9c28beb2da12af34e1d2e4324e4895191)
- Added malloc_conf_2_conf_harder configuration source, allowing users to override the parameters of the configuration system settings. (Architecture-related: configuration override)
  ↳ [#1802](https://github.com/jemalloc/jemalloc/pull/1802): [d936b46](https://github.com/jemalloc/jemalloc/commit/d936b46d3a6320895ddd9a16dc4c5e79d5b9d8e9)
- Add output space verification before mallctl re-operation, implemented by adding a new search function and adjusting the control interface. (Architecture-related: public API)
  ↳ [#1885](https://github.com/jemalloc/jemalloc/pull/1885): [fb347dc](https://github.com/jemalloc/jemalloc/commit/fb347dc6186d5b1747f66075c9209c673d23720b)
- Added range iteration support for flat bitmap, and added corresponding unit tests. (Architecture-related: public API)
  ↳ [#1888](https://github.com/jemalloc/jemalloc/pull/1888): [ddb8dc4](https://github.com/jemalloc/jemalloc/commit/ddb8dc4ad0523e07ab0475d6c9583d8ca27de8dc)
- Introducing a heap analysis debiasing mechanism, which debiases the sampling count and byte count before outputting, so that the heap analysis tool can more accurately attribute stack traces; while retaining the old behavior as an optional setting. (Architecture-related: public API)
  ↳ [#1897](https://github.com/jemalloc/jemalloc/pull/1897): [6099369](https://github.com/jemalloc/jemalloc/commit/60993697d8bd3f8a07756091df397ed4044da921), [81c2f84](https://github.com/jemalloc/jemalloc/commit/81c2f841e5386294834d143fa66c32beb825e4b5)
- Expand the control interface, add ctl_mibnametomib and ctl_bymibname functions, support control query through partial names and partial MIBs. (Architecture-related: public API)
  ↳ [#1908](https://github.com/jemalloc/jemalloc/pull/1908): [006dd04](https://github.com/jemalloc/jemalloc/commit/006dd0414e6356ee76218ca6b2db960fc671df16), [4557c0a](https://github.com/jemalloc/jemalloc/commit/4557c0a67d8804945935b99b5c493d257be71b43), [6ab181d](https://github.com/jemalloc/jemalloc/commit/6ab181d2b72ece43cb6bcc706172ff8f0fe7dd51)
- The ctl_lookup function now supports searching from any node, and is no longer forced to start from the root node. (Architecture-related: public API)
  ↳ [#1908](https://github.com/jemalloc/jemalloc/pull/1908): [91e006c](https://github.com/jemalloc/jemalloc/commit/91e006c4c2c523f185077015e66d99f862165262), [3a627b9](https://github.com/jemalloc/jemalloc/commit/3a627b9674a9d12413b01be8c4e7d2d2bf4965e7)
- The range parameter of PRNG is now allowed to be 1, and the related function interface has been simplified. (Architecture-related: public API)
  ↳ [#1909](https://github.com/jemalloc/jemalloc/pull/1909): [0513047](https://github.com/jemalloc/jemalloc/commit/05130471701b7f42b545e2103f21fad61b67bfb0), [2a6ba12](https://github.com/jemalloc/jemalloc/commit/2a6ba121b5d7f83498265c3a630ba65e08f4b7e7)
- The profiling information now records the size of each allocation request. (Architecture-related: public API)
  ↳ [#1914](https://github.com/jemalloc/jemalloc/pull/1914): [afa489c](https://github.com/jemalloc/jemalloc/commit/afa489c3c5fd16bd31b2756c081c92e08937e6b7)
- Added --with-lg-slab-maxregs configuration option, used to customize the maximum number of regions in slab. (Architecture-related: construction and installation methods)
  ↳ [#1930](https://github.com/jemalloc/jemalloc/pull/1930): [1541ffc](https://github.com/jemalloc/jemalloc/commit/1541ffc76571d8a2a0baad4a13a379305b7df5f2)
- A new age field is added to the edata structure, and acquisition and setting functions are provided. At the same time, age-based comparison logic and corresponding heap types are added. (Architecture-related: public API)
  ↳ [#1942](https://github.com/jemalloc/jemalloc/pull/1942): [634ec6f](https://github.com/jemalloc/jemalloc/commit/634ec6f50abd57e6371e0c745ab699f2cf6d08e6)
- The slab_sizes configuration item has a new default option, which is used to reset to the default value. (Architecture-related: public API)
  ↳ [#1948](https://github.com/jemalloc/jemalloc/pull/1948): [b971f7c](https://github.com/jemalloc/jemalloc/commit/b971f7c4dda04ba26f9fb52709c7153cef27021c)
- Implement opt.cache_oblivious runtime configuration option, while retaining config.cache_oblivious to maintain backward compatibility. (Architecture-related: runtime configuration)
  ↳ [#2027](https://github.com/jemalloc/jemalloc/pull/2027): [a11be50](https://github.com/jemalloc/jemalloc/commit/a11be50332c5cdae7ce74d8e0551e7f3143630b8)
- Added summarize/filter function to red-black tree, supporting tracking additional information in nodes for filtering search. (Architecture-related: public API)
  ↳ [#2042](https://github.com/jemalloc/jemalloc/pull/2042): [5417938](https://github.com/jemalloc/jemalloc/commit/5417938215384d9373d290ba30d5dcccc5db5c80)
- Added the --debug-syms-by-id option to the jeprof tool to support finding debug symbol files by build ID on Linux. (Architecture-related: build and installation methods)
  ↳ [#2067](https://github.com/jemalloc/jemalloc/pull/2067): [11beab3](https://github.com/jemalloc/jemalloc/commit/11beab38bc5ede45f06af3c513efd003c9d32088)
- Added experimental option opt.experimental_infallible_new, which enables security checks to be triggered when allocation fails, and adds C++17 aligned allocation support. (Architecture-related: public API)
  ↳ [#2082](https://github.com/jemalloc/jemalloc/pull/2082): [4452a48](https://github.com/jemalloc/jemalloc/commit/4452a4812ff8bc2a5127a9b220de05999a0652f1) | [#1660](https://github.com/jemalloc/jemalloc/pull/1660): [8b2c2a5](https://github.com/jemalloc/jemalloc/commit/8b2c2a596da9bed11432ac703a6c0b0a76ec4dfd)
- Added opt.stats_interval and opt.stats_interval_opts configuration options to support interval statistics output based on the number of allocated active bytes. (Architecture-related: public API)
  ↳ [#1733](https://github.com/jemalloc/jemalloc/pull/1733): [88b0e03](https://github.com/jemalloc/jemalloc/commit/88b0e03a4e081d3d9c1bdf369345679f9e23b983)
- In mallctl, when the output buffer space is insufficient, update the output length pointer to reflect the actual copied data length. (Architecture-related: public API behavior)
  ↳ [#1885](https://github.com/jemalloc/jemalloc/pull/1885): [f5fb4e5](https://github.com/jemalloc/jemalloc/commit/f5fb4e5a970077e308d7e4e3f1cbbec4cf76a8d9)
- Fix the behavior consistency of ctl_nametomib in the reverse case, ensuring that it does not fail when the mib array length is larger than the name. (Architecture-related: public API: ctl_nametomib behavior consistency)
  ↳ [#1908](https://github.com/jemalloc/jemalloc/pull/1908): [f2e1a5b](https://github.com/jemalloc/jemalloc/commit/f2e1a5be776de0a4d12c03820bcb5fb0d475d756)
- Fixed an issue where abort was not triggered under abort_conf:true when the malloc_conf configuration string ended with a key, ended with a comma or was in the wrong format. (Architecture-related: configuration behavior)
  ↳ [#2171](https://github.com/jemalloc/jemalloc/pull/2171): [af6ee27](https://github.com/jemalloc/jemalloc/commit/af6ee27c0d6a87d0274b9e83a55f78176ab95da4)
- Fix the symbol conflict with musl libc, by detecting whether to link glibc and avoid using the irreplaceable malloc stub function in musl libc. (Architecture-related: platform compatibility)
  ↳ [#2190](https://github.com/jemalloc/jemalloc/pull/2190): [1851002](https://github.com/jemalloc/jemalloc/commit/18510020e75fd3f6a2c9e26057d9a188bee1fc21), [c91e62d](https://github.com/jemalloc/jemalloc/commit/c91e62dd375637e1d029af5385ce633a74f98712)
- Make the default behavior of zero reallocation consistent with the system allocator, which chooses to deallocate or allocate based on the compile configuration. (Architecture-related: allocator behavior)
  ↳ [#2270](https://github.com/jemalloc/jemalloc/pull/2270): [8cb8146](https://github.com/jemalloc/jemalloc/commit/8cb814629acc7c7a8c1008f47e35d3f40129f5fa)
- Simplified the time setting and acquisition interface of performance analysis logs, and removed parameters that are no longer needed. (Architecture-related: public API)
  ↳ [#1551](https://github.com/jemalloc/jemalloc/pull/1551): [4fbbc81](https://github.com/jemalloc/jemalloc/commit/4fbbc817c1130d3d6c066f132fb5a2b23803be89)
- Added conditional compilation protection for the C++ aligned allocation and deallocation API, which is only enabled when supporting the C++17 aligned new feature; refactored the C++ API order, and added the alignedSizedDeleteImpl inline function to eliminate compilation warnings. (Architecture-related: public API)
  ↳ [#1692](https://github.com/jemalloc/jemalloc/pull/1692): [5c47a30](https://github.com/jemalloc/jemalloc/commit/5c47a3022775080866fd37d74c0143d7ffec3915) | [#1787](https://github.com/jemalloc/jemalloc/pull/1787): [b30a5c2](https://github.com/jemalloc/jemalloc/commit/b30a5c2f9073b6f35f0023a443cd18ca406e972a)
- Rename the core type extent_t to edata_t to resolve the naming conflict. (Architecture-related: core type renaming)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [a7862df](https://github.com/jemalloc/jemalloc/commit/a7862df6169f27d9f347343ffef2bef3e167317c)
- Removed the extent merging function's dependence on arena, and instead passed in edata_cache through parameters to decouple the association between the extent module and arena. (Architecture-related: module decoupling)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [372042a](https://github.com/jemalloc/jemalloc/commit/372042a082347dd4c036f5cfeff3853d5eac4b91), [48ec5d4](https://github.com/jemalloc/jemalloc/commit/48ec5d4355c66c20d9143214c83823875ea91579)
- Removed the prof_lookup_global function, replaced the b0get call in prof_boot2 with the incoming base parameter, and renamed prof_dump_seq_mtx to prof_dump_filename_mtx. (Architecture-related: public API: removed function)
  ↳ [#1770](https://github.com/jemalloc/jemalloc/pull/1770): [29436fa](https://github.com/jemalloc/jemalloc/commit/29436fa056169389f3d76c74aae1465604bdd799) | [#1623](https://github.com/jemalloc/jemalloc/pull/1623): [242af43](https://github.com/jemalloc/jemalloc/commit/242af439b81044b2604a515ad5d3a8c2d6fbbdfd)
- Remove the memory filling (junking) logic from the allocation release path of tcache and arena, and change it to be processed at a higher level to simplify the internal logic and keep the fast path unaffected. (Architecture-related: External behavior: Memory filling logic movement)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [79f1ee2](https://github.com/jemalloc/jemalloc/commit/79f1ee2fc0163d3666f38cfc59f8c1a8ab07f056)
- Simplified the interface of cache_bin module, changed the functions that require index and info array to only accept a single info pointer, and the caller directly passes in the corresponding info. (Architecture-related: public API: interface simplification)
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [e1dcc55](https://github.com/jemalloc/jemalloc/commit/e1dcc557d68cfa1c7f1fab6c84a9e44e1d97e1d4)
- Moved edata attribute modification operations (szind, size, szind, sn, zeroed and state initialization) from the emap module back to the extent module, and adjusted the module responsibility boundaries. (Architecture-related: Module responsibility adjustment)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [dfef0df](https://github.com/jemalloc/jemalloc/commit/dfef0df71a956338c3bb4a902a288ee550409c3b), [0c96a2f](https://github.com/jemalloc/jemalloc/commit/0c96a2f03bcb741b1c29fd1a3af3044a03a8ac08), [883ab32](https://github.com/jemalloc/jemalloc/commit/883ab327cca593de320f781e3c654e8b716a4786)
- Reconstructed thread event processing, extracting waiting time calculation and delayed waiting time into independent functions, which are defined by each module to eliminate inter-module dependencies. (Architecture-related: cross-module interface reconstruction)
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [733ae91](https://github.com/jemalloc/jemalloc/commit/733ae918f0d848a64e88e622e348749fe6756d89), [abd4674](https://github.com/jemalloc/jemalloc/commit/abd467493110efbcf92f0e85a699f9cda47daff7)
- The caller is required to manually clear edata_t on the stack before using it to avoid undefined behavior; at the same time, the parameters of edata_init are modified and the edata_hugeified_set function is removed. (Architecture-related: public API)
  ↳ [#1848](https://github.com/jemalloc/jemalloc/pull/1848): [eda9c28](https://github.com/jemalloc/jemalloc/commit/eda9c2858f267961d7e88cb3f3e841f197372125)
- Migrate the thread name processing function from the prof module to the prof_data module. (Architecture-related: Module responsibility reorganization)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [841af2b](https://github.com/jemalloc/jemalloc/commit/841af2b4269b425c28b32c032340ac572d4773ae)
- Reconstruct psset statistical information processing, uniformly using huge status as array index to simplify logic. (Architecture-related: psset interface reconstruction)
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [55e0f60](https://github.com/jemalloc/jemalloc/commit/55e0f60ca1c154659b56ec90a85c8b53b580361e)
- Added assert_* macros and p_test_failed function in the test framework, which supports aborting the test immediately when the assertion fails, and has been applied to some test files. (Architecture-related: public API)
  ↳ [#1760](https://github.com/jemalloc/jemalloc/pull/1760): [fa61579](https://github.com/jemalloc/jemalloc/commit/fa615793821219f8ad62e40aa23c848e5136aa5c), [a88d22e](https://github.com/jemalloc/jemalloc/commit/a88d22ea114b4db398aad021aa1dcd1b33b4038d), [21dfa43](https://github.com/jemalloc/jemalloc/commit/21dfa4300dd372c11c7e1392225f58ae92c35eeb)
- Replaced the dump file opening function in the test with the new interception function, and adjusted the relevant test assertions accordingly. (Architecture-related: public API)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [f307b25](https://github.com/jemalloc/jemalloc/commit/f307b25804064eb26077f98b1481e6eb42f1dbad)
- Added performance benchmark test for large memory allocation, and migrated public timing tool functions to independent header files. (Architecture-related: public header files)
  ↳ [#1837](https://github.com/jemalloc/jemalloc/pull/1837): [2c09d43](https://github.com/jemalloc/jemalloc/commit/2c09d43494d1c2f0df41ef16b040acb86ad4b095)
- Reduce prof dump buffer size in debug builds to facilitate testing. (Architecture-related: debugging and profiling behavior)
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [f541871](https://github.com/jemalloc/jemalloc/commit/f541871f5df5d711df6fd13830496f86d72439ce)
- Added mallctl interface speed stress test. (Architecture-related: public API stress test)
  ↳ [#1901](https://github.com/jemalloc/jemalloc/pull/1901): [32d4673](https://github.com/jemalloc/jemalloc/commit/32d46732217ab592032567350c176850ba0249c6)
- Add alignment stress test for rallocx. (Architecture-related: public API stress test)
  ↳ [#1900](https://github.com/jemalloc/jemalloc/pull/1900): [8f9e958](https://github.com/jemalloc/jemalloc/commit/8f9e958e1e81342091b1178005c0dedfed5573dd)
- Cache summary information in heap edata, optimize first adaptation lookup to reduce cache misses, and adjust related function interfaces and types. (Architecture event: jemalloc_Memory_Allocator module change)
  ↳ [#2098](https://github.com/jemalloc/jemalloc/pull/2098): [dcb7b83](https://github.com/jemalloc/jemalloc/commit/dcb7b83facf4f7641cefc0fc7c11c3d88310dae0)
- Optimized the qr_meld macro, removed the a_type parameter and adjusted the order of internal pointer operations, and updated related test cases. (Architecture-related: public API)
  ↳ [#1807](https://github.com/jemalloc/jemalloc/pull/1807): [c9d56cd](https://github.com/jemalloc/jemalloc/commit/c9d56cddf27d52b77fc4e346fd841dcbf31ed671)
- Inline malloc fast path into operator new to reduce CPU overhead of C++ programs. (Architecture-related: public API)
  ↳ [#2026](https://github.com/jemalloc/jemalloc/pull/2026): [edbfe69](https://github.com/jemalloc/jemalloc/commit/edbfe6912c1b7e8b561dfee1b058425de6c06285)
- Reconstructed the ecache and eset data structures, migrated related fields and functions to ecache, and reduced dependence on arena. (Architecture-related: Module dependency adjustment)
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [98eb40e](https://github.com/jemalloc/jemalloc/commit/98eb40e563bd2c42bfd5d7275584a4aa69a2b3b7), [d8b0b66](https://github.com/jemalloc/jemalloc/commit/d8b0b66c6c0818f83661f69a5eba05924efe0755), [576d704](https://github.com/jemalloc/jemalloc/commit/576d7047ab93baf37d851136f6ccd4fb38810ded), [282a382](https://github.com/jemalloc/jemalloc/commit/282a382326fc4271f77df207074d73016fe8dcb0), [0aa9769](https://github.com/jemalloc/jemalloc/commit/0aa9769fb0cc73e1df6c728af10b45dfb4d1bc71), [2f4fa80](https://github.com/jemalloc/jemalloc/commit/2f4fa80414fc9e7374f0b784e0f925aa31d0e599) | [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [1ada4ae](https://github.com/jemalloc/jemalloc/commit/1ada4aef84246d3fc494d8064ee14d5ae62ec569), [a24faed](https://github.com/jemalloc/jemalloc/commit/a24faed56915df38c5ab67b66cefbb596c0e165c)
- Rename the edata_tree_t type to edata_avail_t. (Architecture-related: public API: Type renaming)
  ↳ [#1974](https://github.com/jemalloc/jemalloc/pull/1974): [b4c37a6](https://github.com/jemalloc/jemalloc/commit/b4c37a6e81ef2e0286b66a0bc9fc09060690c9a5)
- Add comments to the public API of the decay module to explain its purpose and parameter meaning. (Architecture-related: public API documentation)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [cdb916e](https://github.com/jemalloc/jemalloc/commit/cdb916ed3f76f348891d4f2a83f38bd70ed75067)
- Travis CI adds support for the Windows platform and adds platform-related build scripts for Linux and Windows. (Architecture-related: Platform compatibility)
  ↳ [#2185](https://github.com/jemalloc/jemalloc/pull/2185): [01a293f](https://github.com/jemalloc/jemalloc/commit/01a293fc08ba8b6df1824ffecd10d2be5879b980) | [#2207](https://github.com/jemalloc/jemalloc/pull/2207): [8a49b62](https://github.com/jemalloc/jemalloc/commit/8a49b62e788a5ae21a32a3a2caccf27b841c9bf8)
- Add --with-lg-page=16 build option in CI configuration and test generation script. (Architecture-related: Build configuration)
  ↳ [#1626](https://github.com/jemalloc/jemalloc/pull/1626): [d1be488](https://github.com/jemalloc/jemalloc/commit/d1be488cd8ceab285b93265ae70a258779ab8310)
- Fix Android platform build, distinguish platforms by introducing glibc variables, and avoid performing glibc-specific malloc hook detection on Android. (Architecture-related: platform compatibility)
  ↳ [#1831](https://github.com/jemalloc/jemalloc/pull/1831): [27ef02c](https://github.com/jemalloc/jemalloc/commit/27ef02ca9a21f2e6a432e67dd3d2bafc8a04371f)
- The complete size class table is no longer created under non-prof builds. Instead, only the minimum size is retained to save memory, and compile-time assertions are added to ensure that relevant functions are only executed in prof mode. (Architecture-related: core module behavior)
  ↳ [#1916](https://github.com/jemalloc/jemalloc/pull/1916): [20f2479](https://github.com/jemalloc/jemalloc/commit/20f2479ed79a8ef152c9ef50efdee2aec5dc5737)
- Added support for PPC64LE architecture in Travis CI configuration and build scripts. (Architecture-related: Platform compatibility)
  ↳ [#1933](https://github.com/jemalloc/jemalloc/pull/1933): [36ebb5a](https://github.com/jemalloc/jemalloc/commit/36ebb5abe319d473c8535488e2dc1f4f0bc4e9d4)
- Added JEMALLOC_HAS_ALLOCA_H macro definition in configure.ac for QNX platform. (Architecture-related: platform compatibility)
  ↳ [#1972](https://github.com/jemalloc/jemalloc/pull/1972): [063a767](https://github.com/jemalloc/jemalloc/commit/063a767ffe453624a1d4c5b26115efcc1ea5f2e1)
- Add make uninstall support to the build system, which is used to uninstall installed binaries, header files, libraries and pkg-config files. (Architecture-related: build and installation methods)
  ↳ [#2212](https://github.com/jemalloc/jemalloc/pull/2212): [640c3c7](https://github.com/jemalloc/jemalloc/commit/640c3c72e661ec0b3f20865ee4fd4363644c017a) | [#2220](https://github.com/jemalloc/jemalloc/pull/2220): [a4e8122](https://github.com/jemalloc/jemalloc/commit/a4e81221cceeb887708d53015d3d1f1f9642980a)
- Now when configuring --enable-prof-libunwind, you must also specify --enable-prof, otherwise an error will be reported. (Architecture-related: build requirements)
  ↳ [#2121](https://github.com/jemalloc/jemalloc/pull/2121): [26140dd](https://github.com/jemalloc/jemalloc/commit/26140dd24676a06293e105e0ac4e1f1fef04f337)
- Fixed the problem of document building when using install-suffix, and adjusted the naming rules of target files in HTML and man pages. (Architecture-related: build and installation methods)
  ↳ [#2209](https://github.com/jemalloc/jemalloc/pull/2209): [011449f](https://github.com/jemalloc/jemalloc/commit/011449f17bdddd4c9e0510b27a3fb34e88d072ca)
- It is forbidden to include spaces in the installation suffix. If a space is detected during configuration, an error will be reported. (Architecture-related: installation configuration)
  ↳ [#2212](https://github.com/jemalloc/jemalloc/pull/2212): [36a09ba](https://github.com/jemalloc/jemalloc/commit/36a09ba2c712612675f182fe879514a6078f5c77)
- It is forbidden to include spaces in prefix and exec_prefix, otherwise the configuration process will report an error. (Architecture-related: installation configuration)
  ↳ [#2212](https://github.com/jemalloc/jemalloc/pull/2212): [eafd2ac](https://github.com/jemalloc/jemalloc/commit/eafd2ac39fc4b608fc24b755670ff5138b9173ee)
- Correctly detect background thread support on Darwin platform by checking ABI types when cross-compiling. (Architecture-related: Platform compatibility)
  ↳ [#2225](https://github.com/jemalloc/jemalloc/pull/2225): [063d134](https://github.com/jemalloc/jemalloc/commit/063d134aeb4807872f45a3b7e6b43bed8f6320a2)
- When cross-compiling Apple M1, if the page size is not specified, 16K will be used by default and detection will be skipped. (Architecture-related: platform compatibility)
  ↳ [#2242](https://github.com/jemalloc/jemalloc/pull/2242): [7ae0f15](https://github.com/jemalloc/jemalloc/commit/7ae0f15c598258610dd3cfd9633301ffa8661c45)
- Added FreeBSD build tasks and corresponding installation, configuration and test scripts in Travis CI. (Architecture-related: platform compatibility)
  ↳ [#2207](https://github.com/jemalloc/jemalloc/pull/2207): [fdb6c10](https://github.com/jemalloc/jemalloc/commit/fdb6c101625060236732a6003116a129edda3687)
- Change the default JSON output format to compact format, which can save 20-50% of the output size. (Architecture-related: public API: compact JSON output)
  ↳ [#1590](https://github.com/jemalloc/jemalloc/pull/1590): [eb70fef](https://github.com/jemalloc/jemalloc/commit/eb70fef8ca86363a036a962852808675ed1598c1) | [#1577](https://github.com/jemalloc/jemalloc/pull/1577): [8c8466f](https://github.com/jemalloc/jemalloc/commit/8c8466fa6e413b08ce83c6f5ac96d2b1454e3afe)
- Unify the include guard style, and rename flat_bitmap.h to fb.h to match the naming convention. (Architecture-related: public API)
  ↳ [#2042](https://github.com/jemalloc/jemalloc/pull/2042): [aea91b8](https://github.com/jemalloc/jemalloc/commit/aea91b8c338594daed753c94f33ff32d4b23fdc9)

### Background Workers & Monitoring Hooks
- Add an access function to obtain the epoch duration in the decay module, and change the method of directly accessing the decay structure members in background_thread to use this function to encapsulate internal data access. (Architecture-related: module responsibility: encapsulate decay data access)
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [d1d7e10](https://github.com/jemalloc/jemalloc/commit/d1d7e1076b6132a1faacd10cafaebaee975edb98)
- Added mallctl interface for prof statistical information, and output the real-time and cumulative request size and count of each size class in statistical printing. (Architecture-related: public API)
  ↳ [#1914](https://github.com/jemalloc/jemalloc/pull/1914): [9f71b57](https://github.com/jemalloc/jemalloc/commit/9f71b5779be6d59d2a603b0270e4c0c896d49d1c), [54f3351](https://github.com/jemalloc/jemalloc/commit/54f3351f1f699a2d50f42da7f9a73a8d1a25ea30)
- Now supports CPU affinity settings for BSD platforms. (Architecture-related: Platform compatibility)
  ↳ No PR: [11b6db7](https://github.com/jemalloc/jemalloc/commit/11b6db7448f9c31502a7bcf7e59cd8913732c83d)
- Add a delay processing function to HPA, allowing partial release operations to be postponed to background thread execution, and introducing a hugification delay mechanism to prevent short-lived huge pages from being hugified. (Architecture-related: HPA delay processing)
  ↳ [#2084](https://github.com/jemalloc/jemalloc/pull/2084): [583284f](https://github.com/jemalloc/jemalloc/commit/583284f2d91f79b0174ee23e1b4d946b63845246), [6630c59](https://github.com/jemalloc/jemalloc/commit/6630c5989672cbbd5ec2369aaa46ce6f5ce1ed4e)
- Added the ability to notify the background thread of delayed work for the PAI allocator, and added the frequent_reuse parameter to indicate whether the allocation will be frequently reused. (Architecture-related: public API)
  ↳ [#2107](https://github.com/jemalloc/jemalloc/pull/2107): [8229cc7](https://github.com/jemalloc/jemalloc/commit/8229cc77c51109737774bcd053adab001de21e0e) | [#2151](https://github.com/jemalloc/jemalloc/pull/2151): [f56f5b9](https://github.com/jemalloc/jemalloc/commit/f56f5b9930a46f919ae40b04acef8200fdd216e9)
- Separate the calculation of the cleanup interval from the background thread logic and migrate it to a more appropriate file. (Architecture event: Internal responsibility migration)
  ↳ [#2089](https://github.com/jemalloc/jemalloc/pull/2089): [4b633b9](https://github.com/jemalloc/jemalloc/commit/4b633b9a81bb0fe1b234bd6243496d407cae8665)
- The background_thread_boot1 function changes to accept the base_t *base parameter, and no longer calls b0get() internally to obtain base. (Architecture-related: public API: function signature change)
  ↳ [#1770](https://github.com/jemalloc/jemalloc/pull/1770): [162c2bc](https://github.com/jemalloc/jemalloc/commit/162c2bcf319966b83e56a552b158d87a211bfcd1)
- Move HPA's delayed operations to background thread execution, and set the PA shard's delayed permission status when enabling/disabling background threads. (Architecture-related: cross-module responsibility migration)
  ↳ [#2084](https://github.com/jemalloc/jemalloc/pull/2084): [1d4a766](https://github.com/jemalloc/jemalloc/commit/1d4a7666d558b2c21e8cfc2b3e8981020db072fa)
- Removed the no longer used opt_background_thread_hpa_interval_max_ms configuration item and related functions, and migrated the time calculation logic of delayed work from the background thread to the PAI layer. (Architecture-related: public API: configuration item removal)
  ↳ [#2107](https://github.com/jemalloc/jemalloc/pull/2107): [6e848a0](https://github.com/jemalloc/jemalloc/commit/6e848a005e23d5eeb7f0b32424730d53f1d4edf3)
- Limit test hook macro definitions to test builds to solve Android build issues. (Architecture-related: Platform compatibility)
  ↳ [#2129](https://github.com/jemalloc/jemalloc/pull/2129): [8daac79](https://github.com/jemalloc/jemalloc/commit/8daac7958f6b9a3e10e5de83c2a1252e8977687f)

## Routine Changes

### New features
- Added the fls function family in the bit_util module, and simplified the implementation of bit operation functions such as ffs and popcount based on them.
  ↳ [#1888](https://github.com/jemalloc/jemalloc/pull/1888): [22da836](https://github.com/jemalloc/jemalloc/commit/22da836094f315b3fe1609e21c0e1092e7b0f2f5)
- Support zero padding formatting of unsigned numbers, and updated related test cases.
  ↳ [#1901](https://github.com/jemalloc/jemalloc/pull/1901): [7b18736](https://github.com/jemalloc/jemalloc/commit/7b187360e9641c8f664709d3ac50296e3a87b2e0)
- Flat bitmap adds the longest continuous range calculation function and adds corresponding tests.
  ↳ [#1904](https://github.com/jemalloc/jemalloc/pull/1904): [ed99d30](https://github.com/jemalloc/jemalloc/commit/ed99d300b93777787aad82549a4b0c4be129df35) | [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [54c94c1](https://github.com/jemalloc/jemalloc/commit/54c94c1679899db53c4a1002256e8604bc60eb36)
- cache_bin adds a new batch allocation function cache_bin_alloc_batch, and adds corresponding unit tests.
  ↳ [#1962](https://github.com/jemalloc/jemalloc/pull/1962): [be5e49f](https://github.com/jemalloc/jemalloc/commit/be5e49f4fa09247a91557690cdaef42a82a83d6a) | [#2173](https://github.com/jemalloc/jemalloc/pull/2173): [01d61a3](https://github.com/jemalloc/jemalloc/commit/01d61a3c6fa4664ba92f97bd75f4b513396b140e)
- Added insert and remove functions to psset, and added corresponding unit tests.
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [d0a991d](https://github.com/jemalloc/jemalloc/commit/d0a991d47b2717ac6abe6a7d8adc52c967ecd115), [5228d86](https://github.com/jemalloc/jemalloc/commit/5228d869ee9af9c547302abe3165bd63f6bdbbf5)
- Added sampling interval field to prof last-N dump output.
  ↳ [#1983](https://github.com/jemalloc/jemalloc/pull/1983): [9545c2c](https://github.com/jemalloc/jemalloc/commit/9545c2cd36e758f41857b93b8cb55355cf0bc508)
- The jeprof tool adds the --collapsed option to support generating collapsed stack output for building flame graphs.
  ↳ [#1984](https://github.com/jemalloc/jemalloc/pull/1984): [99c2d6c](https://github.com/jemalloc/jemalloc/commit/99c2d6c232eca19e29224f48425517ecebcc1ab0)
- HPA statistics have added indicator reports for empty slabs, including the number of huge and nonhuge pages, the number of active pages and the number of dirty pages, and the corresponding statistical nodes have been registered in the CTL interface.
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [0ea3d63](https://github.com/jemalloc/jemalloc/commit/0ea3d6307cb7eb899c90b86e286ee7b8368f9bb7)
- Optimized stats printing, replaced string name lookups in mutex statistics reading and arena extent printing with mib-based fast paths, and added HPA shard eviction counts and prof statistics output.
  ↳ [#1908](https://github.com/jemalloc/jemalloc/pull/1908): [74bd63b](https://github.com/jemalloc/jemalloc/commit/74bd63b2034c5f25bbc1fdf46095dfed08fdd2a5) | [#1914](https://github.com/jemalloc/jemalloc/pull/1914): [4352cbc](https://github.com/jemalloc/jemalloc/commit/4352cbc21c597d5147c352740fdeefdcc4af0f11)
- Optimize HPA's cleaning and hugify strategies, introduce a soft preference mechanism to prioritize cleaning of non-hugified pages, and use the dirtiest-first cleaning strategy instead.
  ↳ [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [0f6c420](https://github.com/jemalloc/jemalloc/commit/0f6c420f83a52c3927cc1c78d155622de05e3ba5), [73ca4b8](https://github.com/jemalloc/jemalloc/commit/73ca4b8ef81d2a54970804182c010b8c95a93587)
- Added typed_list module, providing type-safe list operation macros.
  ↳ [#1857](https://github.com/jemalloc/jemalloc/pull/1857): [129b727](https://github.com/jemalloc/jemalloc/commit/129b72705833658d87886781347548e0261fcaeb) | [#1828](https://github.com/jemalloc/jemalloc/pull/1828): [2bb8060](https://github.com/jemalloc/jemalloc/commit/2bb8060d572311e4a42a35fb52e78f78e42725ee)
- Added maximum value statistics for background thread mutex locks for debugging and sanity checking.
  ↳ [#1619](https://github.com/jemalloc/jemalloc/pull/1619): [b7c7df2](https://github.com/jemalloc/jemalloc/commit/b7c7df24ba7c3b76b4985084de6e20356b26547e)
- Implemented use-after-free detection function based on junk filling and stash mechanism.
  ↳ [#2173](https://github.com/jemalloc/jemalloc/pull/2173): [b75822b](https://github.com/jemalloc/jemalloc/commit/b75822bc6e5cbbf463c611d8dea32857f8de9d3e)
- Replaced utrace calls with the UTRACE_CALL macro to support tag-based signatures.
  ↳ [#1986](https://github.com/jemalloc/jemalloc/pull/1986): [520b75f](https://github.com/jemalloc/jemalloc/commit/520b75fa2daf3313d87780f40ca0101c83c10398)

### bug fixes
- Fix issue where prof_accumbytes was not cleared when flushing tcache causing allocations to be double counted and causing excessive performance dumps.
  ↳ [#1528](https://github.com/jemalloc/jemalloc/pull/1528): [a219cfc](https://github.com/jemalloc/jemalloc/commit/a219cfcda34e9916c14ff9f9e198b18b41b71fbc)
- Fixed the handling of tcaches mutex locks before and after fork, and now performs locking and unlocking operations unconditionally.
  ↳ [#1585](https://github.com/jemalloc/jemalloc/pull/1585): [87e2400](https://github.com/jemalloc/jemalloc/commit/87e2400cbb8b5a49f910b3c72b10297fcc9df839)
- Fix the error when accessing the big bin index through the cache bin descriptor, ensuring that the big bin index starts counting from 0.
  ↳ [#1591](https://github.com/jemalloc/jemalloc/pull/1591): [5934846](https://github.com/jemalloc/jemalloc/commit/593484661261c20f75557279931eb2d9ca165185)
- Fixed the problem of incorrect large.nflushes value in merged statistics, ensuring that this field correctly accumulates the corresponding values of all arenas.
  ↳ [#1609](https://github.com/jemalloc/jemalloc/pull/1609): [719583f](https://github.com/jemalloc/jemalloc/commit/719583f14acc3dc0d24287e18a80b280e46aebb3)
- Changed cache bin size type from signed 32-bit integer to unsigned 16-bit integer, removed negative value check assertion which is no longer needed, and added overflow protection assertion.
  ↳ [#1617](https://github.com/jemalloc/jemalloc/pull/1617): [785b84e](https://github.com/jemalloc/jemalloc/commit/785b84e60382515f1bf1a63457da7a7ab5d0a96b)
- Fixed the reentrancy level problem of prof_backtrace(), renamed the underlying backtrace implementation to prof_backtrace_impl, and added reentrancy protection.
  ↳ [#1620](https://github.com/jemalloc/jemalloc/pull/1620): [671f120](https://github.com/jemalloc/jemalloc/commit/671f120e2669f9574449d4ddad06e561ac8553c3)
- Add protection processing for slabcur being NULL in extent_util_stats_verbose_get, obtain the slab from the non-full extents heap when the bin is completely full, and update related comments and test assertions.
  ↳ [#1659](https://github.com/jemalloc/jemalloc/pull/1659): [bd6e28d](https://github.com/jemalloc/jemalloc/commit/bd6e28d6a3d0468e36d7da032966e0d786020bcc)
- During the muzzy decay process, when there are no pages to be cleaned or the decay time is set to a non-positive number, return early to avoid acquiring the mutex lock.
  ↳ [#1672](https://github.com/jemalloc/jemalloc/pull/1672): [04cb7d4](https://github.com/jemalloc/jemalloc/commit/04cb7d4d6b8cd2fb1c615aeb049e00a51c66083e)
- Relax the judgment conditions of arena_may_have_muzzy, remove the dependence on pages_can_purge_lazy, and only judge based on muzzy decay interval.
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [d0f187a](https://github.com/jemalloc/jemalloc/commit/d0f187ad3b2ea2e457a05217da4be23db5d915a5)
- Fixed the problem that base_new still uses transparent huge pages after setting thp:never. Add transparent huge page status settings in base_map.
  ↳ [#1704](https://github.com/jemalloc/jemalloc/pull/1704): [9226e1f](https://github.com/jemalloc/jemalloc/commit/9226e1f0d8ad691ef140bc0bf9340efadb96e5fe)
- Correctly handle the log mutex during fork, ensuring it is properly initialized in the child process.
  ↳ [#1708](https://github.com/jemalloc/jemalloc/pull/1708): [112dc36](https://github.com/jemalloc/jemalloc/commit/112dc36dd5cf3fc24e1bd9beda61b48cb1d6e9e3)
- Fixed a logical error in conditional judgment in the arena_prof_info_get() function.
  ↳ [#1602](https://github.com/jemalloc/jemalloc/pull/1602): [e98ddf7](https://github.com/jemalloc/jemalloc/commit/e98ddf7987b8e9556c269ca0829f438151b124b7)
- Fix assertion error regarding extent head state when using dss.
  ↳ [#1719](https://github.com/jemalloc/jemalloc/pull/1719): [a5d3dd4](https://github.com/jemalloc/jemalloc/commit/a5d3dd4059a19268e6c2916b4014e395442d5750)
- Fallback to unbuffered printing when memory allocation fails, and add stronger assertions in buffered write initialization.
  ↳ [#1728](https://github.com/jemalloc/jemalloc/pull/1728): [f81341a](https://github.com/jemalloc/jemalloc/commit/f81341a48b15e9257d573b80e8e45589137397ec)
- Add a check on whether the thread status is normal when creating prof_tctx to avoid creating tracking data for threads that are about to die.
  ↳ [#1732](https://github.com/jemalloc/jemalloc/pull/1732): [b8df719](https://github.com/jemalloc/jemalloc/commit/b8df719d5c10f6b52263ca4e7bb800c2796b6767)
- Set reentrancy level to 1 for tsd_state_purgatory state, and add assertions in tsd_nominal function to ensure consistency.
  ↳ [#1736](https://github.com/jemalloc/jemalloc/pull/1736): [38a48e5](https://github.com/jemalloc/jemalloc/commit/38a48e5741faf51548f5b750c0ab6eba8eb67a0c)
- Fix the race condition when deleting tdata, adjust the lock holding order and destruction logic to avoid lock overlap.
  ↳ [#1734](https://github.com/jemalloc/jemalloc/pull/1734): [84b28c6](https://github.com/jemalloc/jemalloc/commit/84b28c6a13d4d208e547bc50f7091107f5161957)
- Fixed undefined behavior caused by left shift operation in hash.h.
  ↳ [#1766](https://github.com/jemalloc/jemalloc/pull/1766): [7fd22f7](https://github.com/jemalloc/jemalloc/commit/7fd22f7b2ea5ce2540563ece8e2d30a5316ac857)
- Fixed problems that may occur when the length of a variable-length array is 0, ensuring that the array length is always greater than 0.
  ↳ [#1768](https://github.com/jemalloc/jemalloc/pull/1768): [0f686e8](https://github.com/jemalloc/jemalloc/commit/0f686e82a37e49af6caee2d469f2a2a88e1fbf7c)
- Fixed the problem that random number generation in geometric sampling may produce zero values resulting in log(0), and handle the boundary case as u=1.0 to ensure correct calculation.
  ↳ [#1776](https://github.com/jemalloc/jemalloc/pull/1776): [305b1f6](https://github.com/jemalloc/jemalloc/commit/305b1f6d962c5b5a76b7ddb4b55b14d88bada9ba)
- Fixed an issue where assignment was incorrectly used instead of accumulation when edata_cache size was merged.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [8164fad](https://github.com/jemalloc/jemalloc/commit/8164fad4045a1e30580da30294652e7c3b8a75f7)
- Unify the reading and selection logic of tcache and arena flags, simplify the allocation and release path, and fix problems in related statistical printing and fork post-processing.
  ↳ [#1849](https://github.com/jemalloc/jemalloc/pull/1849): [95a59d2](https://github.com/jemalloc/jemalloc/commit/95a59d2f72f4799b1d7aa07216c558408a91917a), [24bbf37](https://github.com/jemalloc/jemalloc/commit/24bbf376cee49691ff734eb5d0415e14fbbe72ca)
- Fixed the issue where the size of large objects was incorrectly reduced in the tcache_bytes statistical report, and added corresponding test cases.
  ↳ [#1786](https://github.com/jemalloc/jemalloc/pull/1786): [2e5899c](https://github.com/jemalloc/jemalloc/commit/2e5899c1299125c17fc428026a364368ff1531ed)
- Adjust the assignment order of prof_tctx_t pointers in the large_prof_info_set function to correctly implement atomic memory barriers.
  ↳ [#1800](https://github.com/jemalloc/jemalloc/pull/1800): [a166c20](https://github.com/jemalloc/jemalloc/commit/a166c20818e2f5a50c6f0b511ffc5b2ed66b81d2)
- Fixed macro naming errors in prof related header files.
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [f43ac85](https://github.com/jemalloc/jemalloc/commit/f43ac8543e8e6d38a0f0caf9afad22500118f75f)
- Treat delayed prof sampling events as new events to avoid sampling bias.
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [381c97c](https://github.com/jemalloc/jemalloc/commit/381c97caa41eb85b52afca40794b2223e7f36d33)
- Remove duplicate entries in witness error messages.
  ↳ [#1826](https://github.com/jemalloc/jemalloc/pull/1826): [0295aa3](https://github.com/jemalloc/jemalloc/commit/0295aa38a2206f3229f60a4105767e15ebdca797)
- Fixed the problem of incorrect control flow order when prof timestamp configuration is read.
  ↳ [#1864](https://github.com/jemalloc/jemalloc/pull/1864): [40fa667](https://github.com/jemalloc/jemalloc/commit/40fa6674a99a1bac85a4cb0f5cf10ce0e4878a5e)
- Correct the initialization sequence of prof_log_start: advance mutex initialization, delay hash table creation, and correct timestamp initialization and startup condition checking; at the same time, delay atexit registration until the first call to prof_log_start.
  ↳ [#1876](https://github.com/jemalloc/jemalloc/pull/1876): [4258402](https://github.com/jemalloc/jemalloc/commit/4258402047a1b1c9b78ff12dcb26bd869f6ae8cd) | [#2137](https://github.com/jemalloc/jemalloc/pull/2137): [ab0f160](https://github.com/jemalloc/jemalloc/commit/ab0f1604b4fc563158f142d41f6a3550463d7729)
- Fixed the tuning parameter error introduced by configuration and restored the nslots_max target value of tcache to twice the original value.
  ↳ [#1879](https://github.com/jemalloc/jemalloc/pull/1879): [f1f4ec3](https://github.com/jemalloc/jemalloc/commit/f1f4ec315a1831612f6d66b62be55a323fa94312)
- Fixed the problem of incorrect size calculation under specified alignment when reallocating.
  ↳ [#1900](https://github.com/jemalloc/jemalloc/pull/1900): [743021b](https://github.com/jemalloc/jemalloc/commit/743021b63fd06ad23a81af310d467e2e26108a9a)
- Fixed an issue where szind calculation used the wrong size in performance analysis.
  ↳ [#1926](https://github.com/jemalloc/jemalloc/pull/1926): [202f01d](https://github.com/jemalloc/jemalloc/commit/202f01d4f8b28237d9f349f9ee91691ec220425a)
- Fix the position of alloc_ctx check in free_fastpath, moving it after the threshold branch to ensure proper TSD functionality.
  ↳ [#1951](https://github.com/jemalloc/jemalloc/pull/1951): [a9aa6f6](https://github.com/jemalloc/jemalloc/commit/a9aa6f6d0fd695d57a0fd1123da6099bb85132c3)
- Fixed a race condition problem caused by locks not being continuously held during the creation of tcaches.
  ↳ [#1954](https://github.com/jemalloc/jemalloc/pull/1954): [be9548f](https://github.com/jemalloc/jemalloc/commit/be9548f2bef30b75294fdd0eb6721d1bf6e6a56a)
- Move n_search's increment operation out of assert to avoid side effects caused by assert being removed in non-debug builds.
  ↳ [#1994](https://github.com/jemalloc/jemalloc/pull/1994): [9522ae4](https://github.com/jemalloc/jemalloc/commit/9522ae41d6167ea32a4b30ffcf0b21fc4db80c2b)
- Fix assertion failure due to rtree null pointer check in certain edge cases.
  ↳ [#2003](https://github.com/jemalloc/jemalloc/pull/2003): [526180b](https://github.com/jemalloc/jemalloc/commit/526180b76d9e54f40d0fb9e58b0647a21a7e5f77)
- Separated local and remote access to cache_bin, fixed incorrect assertion caused by concurrent access in debug mode.
  ↳ [#2011](https://github.com/jemalloc/jemalloc/pull/2011): [a011c4c](https://github.com/jemalloc/jemalloc/commit/a011c4c22d3fd1da5415dd5001afd195f5cd7ad5)
- Fixed the time initialization function call when calculating duration in prof log.
  ↳ [#2016](https://github.com/jemalloc/jemalloc/pull/2016): [f669980](https://github.com/jemalloc/jemalloc/commit/f6699803e2772de2a4eb253d5b55f00c3842a950)
- Fix name and write type of tcache_max option in statistics output.
  ↳ [#2028](https://github.com/jemalloc/jemalloc/pull/2028): [8c5e5f5](https://github.com/jemalloc/jemalloc/commit/8c5e5f50a29d6ca636bf7394d93be1814de6d74c)
- Mark header status during dss allocation to ensure subsequent merge operations use the correct header status.
  ↳ [#2040](https://github.com/jemalloc/jemalloc/pull/2040): [3913077](https://github.com/jemalloc/jemalloc/commit/3913077146350bd1b720a757e33e8aa35a34e58b)
- Fix lock problem in arena_i_destroy_ctl, make sure to hold ctl_mtx during operation to prevent concurrency with arenas.create.
  ↳ [#2044](https://github.com/jemalloc/jemalloc/pull/2044): [61afb6a](https://github.com/jemalloc/jemalloc/commit/61afb6a40572adfd7b9f03817ff0e62005110212)
- Fixed an issue where setting the thread name was not allowed when prof_sys_thread_name was enabled, and updated unit tests to skip related scenarios.
  ↳ [#2047](https://github.com/jemalloc/jemalloc/pull/2047): [12cd13c](https://github.com/jemalloc/jemalloc/commit/12cd13cd418512d9e7596921ccdb62e25a103f87)
- Fixed printing error when hpa_dirty_mult is -1 due to missing one level of indirection.
  ↳ [#2065](https://github.com/jemalloc/jemalloc/pull/2065): [1f68849](https://github.com/jemalloc/jemalloc/commit/1f688490e176aafbc3e3529d3025df7fcbce725b)
- Fixed two spelling errors in HPA that seriously affected performance: configuration parsing incorrectly set the minimum value of hpa_sec_batch_fill_extra to PAGE, causing a large number of additional pages to be allocated for each allocation; at the same time, HPA used the default batch allocation implementation and did not obtain lock optimization.
  ↳ [#2076](https://github.com/jemalloc/jemalloc/pull/2076): [d202218](https://github.com/jemalloc/jemalloc/commit/d202218e865a14d8fcff5c41682719a07434518c)
- Fixed a type error in the void function incorrectly using the return statement in the pai_dalloc_batch function.
  ↳ [#2088](https://github.com/jemalloc/jemalloc/pull/2088): [3475235](https://github.com/jemalloc/jemalloc/commit/347523517bb90210ffeadf115730003531645394)
- Fixed the calculation method of retained pages in HPA so that it is correctly equal to the total number of hugepage pages minus the number of touched pages.
  ↳ [#2115](https://github.com/jemalloc/jemalloc/pull/2115): [c01a885](https://github.com/jemalloc/jemalloc/commit/c01a885e94b6edb8545113d3ba43248b4b75e90c)
- Fixed the problem that the default allocation hook cannot be used when the arena is created because it assumes that the arena has been initialized, and added corresponding test cases.
  ↳ [#2116](https://github.com/jemalloc/jemalloc/pull/2116): [8b24cb8](https://github.com/jemalloc/jemalloc/commit/8b24cb8fdf2bf210e243c1d676484a4ffa5c3f6c)
- When the arena is destroyed, perform an unprotection operation on the protected slab to prevent leakage of protected pages.
  ↳ [#2152](https://github.com/jemalloc/jemalloc/pull/2152): [6cb585b](https://github.com/jemalloc/jemalloc/commit/6cb585b13ad196ca2e4588ce984c269f3fdb4cea)
- Fixed the problem that last_event was not set correctly during thread event initialization to ensure that the event counter state is consistent after reinitialization.
  ↳ [#2159](https://github.com/jemalloc/jemalloc/pull/2159): [8b81d3f](https://github.com/jemalloc/jemalloc/commit/8b81d3f214cc9ef86210d731803fe39f2f3d54d9)
- Fix prof_leak initialization order problem, ensure that prof_leak is automatically set when prof_leak_error is enabled, and add configuration consistency check, move dependency check to independent function.
  ↳ [#2214](https://github.com/jemalloc/jemalloc/pull/2214): [efc539c](https://github.com/jemalloc/jemalloc/commit/efc539c040cf11b19ffc8af29a8cc3e5c3609092), [8c59c44](https://github.com/jemalloc/jemalloc/commit/8c59c44ffa83bab0f73d5cc8f7d0bbc8d649220b)
- Remove redundant return statements in void functions to fix build warnings.
  ↳ [#1772](https://github.com/jemalloc/jemalloc/pull/1772): [9f4fc27](https://github.com/jemalloc/jemalloc/commit/9f4fc273892f130fd81d26e7cb9e561fb5a10679)
- Add explicit integer type conversion in tcache related functions to fix build errors caused by implicit conversion.
  ↳ [#1854](https://github.com/jemalloc/jemalloc/pull/1854): [8da0896](https://github.com/jemalloc/jemalloc/commit/8da0896b7913470250a0220504822028e2aa8f2a)
- Fixed off-by-one problem of array out-of-bounds access in stress/sizes test.
  ↳ [#1859](https://github.com/jemalloc/jemalloc/pull/1859): [7e09a57](https://github.com/jemalloc/jemalloc/commit/7e09a57b395dc88af218873fd7f47c99c0542f4f)
- Fixed the issue of inconsistent output format when prof_recent and prof_sys_thread_name are enabled at the same time, and updated related unit tests.
  ↳ [#2047](https://github.com/jemalloc/jemalloc/pull/2047): [304cdbb](https://github.com/jemalloc/jemalloc/commit/304cdbb132b607cc22ca16eb0e37e4c6d8ecd201)
- Fixed the extent status check on the merge error path, and added a deactivate function with status check.
  ↳ [#2201](https://github.com/jemalloc/jemalloc/pull/2201): [d66162e](https://github.com/jemalloc/jemalloc/commit/d66162e032190d74a2071e93049751744975ce55)
- Fixed an assertion failure that may be triggered due to improper update order in arena_large_ralloc_stats_update.
  ↳ [#2234](https://github.com/jemalloc/jemalloc/pull/2234): [78b5837](https://github.com/jemalloc/jemalloc/commit/78b58379c854a639df79beb3289351129d863d4b)
- Fixed size class calculation error during sec initialization to avoid creating redundant free bins.
  ↳ [#2236](https://github.com/jemalloc/jemalloc/pull/2236): [52631c9](https://github.com/jemalloc/jemalloc/commit/52631c90f664ded0a5106a7d5fd906d46a7c1f81)
- Fix oversize_threshold test interaction with background thread, extract shared tools and update test cases.
  ↳ [#2068](https://github.com/jemalloc/jemalloc/pull/2068): [0808958](https://github.com/jemalloc/jemalloc/commit/08089589f74ac23268791be18742d031cc5dd041)

### Refactoring optimization
- Add an assertion in prof_active_get_unlocked to ensure that prof_active is always false when opt_prof is closed.
  ↳ [#1614](https://github.com/jemalloc/jemalloc/pull/1614): [beb7c16](https://github.com/jemalloc/jemalloc/commit/beb7c16e946d5a48ac6c3e7318aa24be4e787c0c)
- Reconstruct the sampling initialization logic of performance analysis: the sampling random number generator uses the random number state stored locally in the thread, and the thread data is created on demand.
  ↳ [#1665](https://github.com/jemalloc/jemalloc/pull/1665): [da50d8c](https://github.com/jemalloc/jemalloc/commit/da50d8ce87cb21963596825ebc5faf6d8abd4d2c)
- Unify the interfaces between extent_alloc_wrapper and other allocation functions, and extract the reserved area allocation path into an independent extents_alloc_grow function.
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [ae23e5f](https://github.com/jemalloc/jemalloc/commit/ae23e5f42676bc7c851c8ea8036dfa87763be11b)
- Reconstruct the bin lock logic in the tcache filling and flushing process: move the slab allocation and release operations to the same function level as the bin lock to reduce the lock holding time and prepare for flat combining.
  ↳ [#1763](https://github.com/jemalloc/jemalloc/pull/1763): [ba0e354](https://github.com/jemalloc/jemalloc/commit/ba0e35411cc39d57abb830c80eebde054b06241c) | [#1828](https://github.com/jemalloc/jemalloc/pull/1828): [f28cc2b](https://github.com/jemalloc/jemalloc/commit/f28cc2bc87199e031b9d035ccdff6a2d429274c9)
- Encapsulate the processing of buffer allocation failure, simplify the initialization logic of buffer writers, and use internal callback functions uniformly.
  ↳ [#1795](https://github.com/jemalloc/jemalloc/pull/1795): [09cd794](https://github.com/jemalloc/jemalloc/commit/09cd79495f947a7a2e271eb9bc6ff36b15cfc72f)
- Removed the reset_interval parameter in prof_tdata_init_impl, and no longer resets the sampling waiting time when thread data is reinitialized.
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [1e2524e](https://github.com/jemalloc/jemalloc/commit/1e2524e15a004af50fd79f79b4b6efcfce0164b8)
- Separate the error handling logic from the core dump function, and add tests for scenarios such as file opening and writing failure.
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [5d292b5](https://github.com/jemalloc/jemalloc/commit/5d292b56609ae2b85658f4c544b03d46b41e66be)
- Changed the maximum search constant from a magic number to a named constant to improve code readability and maintainability.
  ↳ [#1821](https://github.com/jemalloc/jemalloc/pull/1821): [46471ea](https://github.com/jemalloc/jemalloc/commit/46471ea32760a90ac3b860f96805901c78a34f62)
- Unify the processing method of small and large cache bins in tcache so that they are accessed through continuous arrays, and reconstruct the relevant internal data structures to support subsequent dynamic adjustments.
  ↳ [#1813](https://github.com/jemalloc/jemalloc/pull/1813): [cd29ebe](https://github.com/jemalloc/jemalloc/commit/cd29ebefd01be090a636e5560066d866209b141b) | [#1772](https://github.com/jemalloc/jemalloc/pull/1772): [6c3491a](https://github.com/jemalloc/jemalloc/commit/6c3491ad3105994f8b804fc6ddb1aa88024a4d4b)
- Clean up the tcache allocation logic, remove profiling and filling related processing, and simplify the cache bin allocation process.
  ↳ [#1819](https://github.com/jemalloc/jemalloc/pull/1819): [fef9abd](https://github.com/jemalloc/jemalloc/commit/fef9abdcc07227e9e9cb479c4799707c4efa86ad)
- Use psset's fit/insert/remove operations in HPA instead, remove alloc_new and alloc_reuse functions, and add new functions to update purge and hugify qualifications.
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [f9299ca](https://github.com/jemalloc/jemalloc/commit/f9299ca572e976597987a1786ac3c5a173a3dbce) | [#2084](https://github.com/jemalloc/jemalloc/pull/2084): [ace329d](https://github.com/jemalloc/jemalloc/commit/ace329d11bc397444e99ff81ff4b8d2ca26cc21c)
- Inactive pages are no longer tracked in HPA statistics, only relevant output is retained in human-readable statistics, and the rest is calculated by large page size and number of active pages.
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [be0d7a5](https://github.com/jemalloc/jemalloc/commit/be0d7a53f3ca361d68f9a820157e9af49c989398)
- Added emap_assert_not_mapped assertion, used to check that the specified edata has not been mapped to emap, and enhanced emap_do_assert_mapped's verification of metadata status.
  ↳ [#1909](https://github.com/jemalloc/jemalloc/pull/1909): [1ed7ec3](https://github.com/jemalloc/jemalloc/commit/1ed7ec369f44beeb2dcc0e2ca21d7e947d8dd1b7)
- Optimize cache bin internal functions, add cache_bin_full auxiliary function, and adjust related interfaces, including simplifying naming, encapsulating flush operations, etc.
  ↳ [#1962](https://github.com/jemalloc/jemalloc/pull/1962): [566c4a8](https://github.com/jemalloc/jemalloc/commit/566c4a8594d433ac40ebfd5a4736a53c431f81dd) | [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [ff6acc6](https://github.com/jemalloc/jemalloc/commit/ff6acc6ed503f9808efd74f9aca70ee201d9e87a), [44529da](https://github.com/jemalloc/jemalloc/commit/44529da8525ef811ea8cc7704ffa9910459656ce), [7f5ebd2](https://github.com/jemalloc/jemalloc/commit/7f5ebd211cd870e9c9a303e6145781bfca58e1bb), [6a7aa46](https://github.com/jemalloc/jemalloc/commit/6a7aa46ef753108f9b0c065572abff14c33eb5d2), [d498a4b](https://github.com/jemalloc/jemalloc/commit/d498a4bb08f1220c089b2c2c06c26b5ff937e30c), [fef0b1f](https://github.com/jemalloc/jemalloc/commit/fef0b1ffe4d1b92a38727449c802e24294284524), [9248503](https://github.com/jemalloc/jemalloc/commit/92485032b2e9184cada5a30e3df389fe164fbb4d)
- Rewrite edata_cache_small to edata_cache_fast, change it from a guaranteed non-failure cache to a mechanism only used to reduce contention, simplify the internal logic and update related tests.
  ↳ [#1969](https://github.com/jemalloc/jemalloc/pull/1969): [03a6047](https://github.com/jemalloc/jemalloc/commit/03a604711113c9d883242291ca11b77c83ba4c75)
- Reconstruct the insertion/removal semantics of psset: change the removal operation to an update operation, and the page is not available for new allocations during the update; the allocation function adds an output parameter for whether to generate delayed work.
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [99fc071](https://github.com/jemalloc/jemalloc/commit/99fc0717e653277c3d7fe77fe84316ad47381936)
- Prioritize cleaning of empty slabs in psset, and add aggregate statistics to assist cleaning decisions, and add corresponding unit tests.
  ↳ [#2084](https://github.com/jemalloc/jemalloc/pull/2084): [47d8a7e](https://github.com/jemalloc/jemalloc/commit/47d8a7e6b04a81f2938f1b18f66cb468870fa442) | [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [9fd9c87](https://github.com/jemalloc/jemalloc/commit/9fd9c876bb99acc957f8ec411837138a9b588a1e)
- Add check for prof_active status in batch_alloc().
  ↳ [#2157](https://github.com/jemalloc/jemalloc/pull/2157): [6bdb4f5](https://github.com/jemalloc/jemalloc/commit/6bdb4f5ab0358d0b4c53b2d18ec9422526042413)
- When the last thread migrates from the arena, immediately perform all clear operations on the arena; at the same time, adjust the arena_migrate function so that it directly receives the arena_t pointer instead of the index.
  ↳ [#2199](https://github.com/jemalloc/jemalloc/pull/2199): [61978bb](https://github.com/jemalloc/jemalloc/commit/61978bbe693c020ffa29dee17b81072ac52726e0) | [#2206](https://github.com/jemalloc/jemalloc/pull/2206): [ddb170b](https://github.com/jemalloc/jemalloc/commit/ddb170b1d92d90ecee9ce87545086da9b34839aa)
- Add comments and more meaningful variable names to sz_psz2ind, change reg_size_compute to a non-static function, remove the global variable sc_data_global, and add unit tests.
  ↳ No PR: [eaaa368](https://github.com/jemalloc/jemalloc/commit/eaaa368bab472a78e99a25c1641d24ad3c2283ad), [eb19681](https://github.com/jemalloc/jemalloc/commit/eb196815d670f0937d2117ff0f2b885bd23c80de)
- Rename the internal header files arena_structs_b.h to arena_structs.h, extent.h to edata.h, and update the references.
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [529cfe2](https://github.com/jemalloc/jemalloc/commit/529cfe2abc7d10272c218a2b9047a85a49a9cd2a) | [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [865debd](https://github.com/jemalloc/jemalloc/commit/865debda2276fee0257c90678bafd1bd2f73df6a)
- Rename extents_t type to eset_t, and update related function signatures and references.
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [4e5e43f](https://github.com/jemalloc/jemalloc/commit/4e5e43f22eead4d1e3fcb4422410e0100b9d8448)
- Add comments to the ehooks module, clean up the code, change the internal default hook function to static, and remove unused inline functions.
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [39fdc69](https://github.com/jemalloc/jemalloc/commit/39fdc690a0d3a49c1e36d79f625350426480b18f)
- Removed reentrant calls and protections already handled by ehooks in extent and base modules to simplify parameter passing.
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [e08c581](https://github.com/jemalloc/jemalloc/commit/e08c581cf1ae5fe8a6735f7b92b7780527125287), [ebbb973](https://github.com/jemalloc/jemalloc/commit/ebbb973271e26175c832a6ec5dfc515e7473a9af)
- Add assertions in the ehooks_init function to ensure that the alloc hook is not empty.
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [f2f2084](https://github.com/jemalloc/jemalloc/commit/f2f2084e79c3546b38fb635401588afdd0560392)
- Remove the _externs suffix from the name of the internal prof header file and update related references.
  ↳ [#1714](https://github.com/jemalloc/jemalloc/pull/1714): [3fa142c](https://github.com/jemalloc/jemalloc/commit/3fa142cf394d39f36d4bf7564251071f13527e4f)
- Unify the naming of buffer writer related types and functions, and use the buf_write_ prefix uniformly.
  ↳ [#1723](https://github.com/jemalloc/jemalloc/pull/1723): [6b6b470](https://github.com/jemalloc/jemalloc/commit/6b6b4709b34992940e112fbe5726472b37783ef2)
- Rename the field nflush in the cache_bin_ptr_array_t structure to n, and update related macros and initialization functions.
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [d303f30](https://github.com/jemalloc/jemalloc/commit/d303f30796f0aef7f7fc9d907ef240b93d3fc674)
- Mark the edata_avail field as a derived value in arena statistics, the actual number of which is maintained by edata_cache.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [497836d](https://github.com/jemalloc/jemalloc/commit/497836dbc8bd5badb0726a36fb5ce12779b15c6b)
- Unify type aliases, adjust code format, and update header file protection macros.
  ↳ [#2133](https://github.com/jemalloc/jemalloc/pull/2133): [83f3294](https://github.com/jemalloc/jemalloc/commit/83f3294027952710f35014cff1cffd51f281d785)
- Fixed the variable name masking problem, renamed local variables, and cleaned up unused functions.
  ↳ [#2187](https://github.com/jemalloc/jemalloc/pull/2187): [d038160](https://github.com/jemalloc/jemalloc/commit/d038160f3b76ac1e5203e11008169366629c81cd)
- Unify the parameter order of tcache_bin_flush_large function to make it consistent with tcache_bin_flush_small.
  ↳ [#1594](https://github.com/jemalloc/jemalloc/pull/1594): [9c5c2a2](https://github.com/jemalloc/jemalloc/commit/9c5c2a2c86d473a63806e534c39fb74a882fa558)
- Refactor the tcache_dalloc_large function and use cache_bin_dalloc_easy instead of manual cache management logic.
  ↳ [#1594](https://github.com/jemalloc/jemalloc/pull/1594): [e2c7584](https://github.com/jemalloc/jemalloc/commit/e2c7584361718ccb12c932d2236a16ec3a31f1a7)
- Merge the code paths of realloc and rallocx, reconstruct the reallocation process, and adjust the tcache acquisition and statistics counting logic in the free fast path.
  ↳ [#1643](https://github.com/jemalloc/jemalloc/pull/1643): [ee961c2](https://github.com/jemalloc/jemalloc/commit/ee961c23100ebbe1e6eb7390a03be5456bc8814c)
- Reconstruct the arena_bin_malloc_hard() function, clean up redundant operations, and adjust variable declaration and logical order.
  ↳ [#1670](https://github.com/jemalloc/jemalloc/pull/1670): [9a3c738](https://github.com/jemalloc/jemalloc/commit/9a3c73800991d3508516208127994a1fc3837de5)
- Move background thread status checks out of internal loops and core functions and instead execute them by the caller to reduce repeated checks.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [655a096](https://github.com/jemalloc/jemalloc/commit/655a09634347628abc6720ad1e2b6e1d08fdf8d9), [103f5fe](https://github.com/jemalloc/jemalloc/commit/103f5feda598ec5bd857db8d2f072724ef82ef46)
- Remove unnecessary alloc_ctx structure in free_fastpath and use separate variables instead.
  ↳ [#1686](https://github.com/jemalloc/jemalloc/pull/1686): [cb1a1f4](https://github.com/jemalloc/jemalloc/commit/cb1a1f4adadc85366e51afcf1a53b359828fba67)
- Simplify the sampling update logic during memory reallocation and remove the updated parameter that is no longer needed.
  ↳ [#1699](https://github.com/jemalloc/jemalloc/pull/1699): [055478c](https://github.com/jemalloc/jemalloc/commit/055478cca8ca8d00e74119ef6210ac64713b0ffb)
- Remove the extent_can_coalesce function's dependence on the arena parameter, and instead determine whether it can be merged by comparing the arena indexes of the inner and outer extents.
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [439219b](https://github.com/jemalloc/jemalloc/commit/439219be7e350113771a27c6fb19ce77f5d26e03)
- Delete the tdata status macro used for thread cleaning, and simplify the relevant checking logic to directly determine whether the pointer is empty.
  ↳ [#1602](https://github.com/jemalloc/jemalloc/pull/1602): [7a27a05](https://github.com/jemalloc/jemalloc/commit/7a27a05940d8eb0afc6ddbe32b420ce9e1452b91)
- Simplify the prof_gctx_try_destroy function, remove redundant parameters and calls, and clean up other redundant condition judgments.
  ↳ [#1734](https://github.com/jemalloc/jemalloc/pull/1734): [d331208](https://github.com/jemalloc/jemalloc/commit/d3312085603ab84e13e820be19f55f05e75a46ea)
- Immediately set the arena index to which edata belongs when creating it, simplifying parameter passing in subsequent operations such as segmentation.
  ↳ [#1761](https://github.com/jemalloc/jemalloc/pull/1761): [040eac7](https://github.com/jemalloc/jemalloc/commit/040eac77ccca6d07b8457237cfe939b7e182474b)
- Added pa_nactive_add and pa_nactive_sub helper functions in the page allocation module for atomically updating the active page count.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [8433ad8](https://github.com/jemalloc/jemalloc/commit/8433ad84eaac3b7ecb6ee01256ccb5766708ae3a)
- Changed some derived statistical fields in Arena from atomic operations or locked reads to direct access to simplify the way to obtain statistical data.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [565045e](https://github.com/jemalloc/jemalloc/commit/565045ef716586f93caf6c210905419be9ed6e25)
- Extract the contents of rtree leaf nodes into independent structures, and add encoding and decoding functions to support the new structures.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [bd4fdf2](https://github.com/jemalloc/jemalloc/commit/bd4fdf295ed5a56f433fa8d4a23d1273cc7ad156)
- Change the bool *zero parameter in the extent allocation related function interface to bool zero to simplify the interface.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [11c47cb](https://github.com/jemalloc/jemalloc/commit/11c47cb1336491b7f4d21f12eaba45a10af639c3)
- Remove the functions in ehooks that rely on the global arena_emap_global, simplify the merge check logic, and support the isolation of custom emaps in tests.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [a4759a1](https://github.com/jemalloc/jemalloc/commit/a4759a1911a6dbb5709302ab5ba94cc1b6322e63)
- Extract the utility function for opening maps files and reconstruct the relevant code.
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [4bb4037](https://github.com/jemalloc/jemalloc/commit/4bb4037dbe2450c985d09eabd29a1d8534e20641)
- Reconstruct the thread event processing logic and change the event threshold calculation from repeated calculation every time it is triggered to only calculation once.
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [f72014d](https://github.com/jemalloc/jemalloc/commit/f72014d09773c529e863eab653331461a740c60c)
- Unify the printing method of prof counting objects, extract public printing functions and replace multiple repeated counting output codes.
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [c8683be](https://github.com/jemalloc/jemalloc/commit/c8683bee80768c191b2e08f1fcef583bc17c9203)
- In the qr module, deduplicate insertion and deletion operations, and reuse existing meld and split logic.
  ↳ [#1807](https://github.com/jemalloc/jemalloc/pull/1807): [1ad06aa](https://github.com/jemalloc/jemalloc/commit/1ad06aa53bc5cca22dde934c3d46b6f683057346)
- Migrate the underlying data structure of the prof recent list from the custom linked list to the ql queue, and remove the custom iterator.
  ↳ [#1808](https://github.com/jemalloc/jemalloc/pull/1808): [a5ddfa7](https://github.com/jemalloc/jemalloc/commit/a5ddfa7d91f96cb1b648c6808488682e96880eb7), [2deabac](https://github.com/jemalloc/jemalloc/commit/2deabac079440f843f833f1fe121bc62dff8092c)
- Reconstruct the ql module, introduce auxiliary macros such as ql_first and ql_clear, and unify the linked list operation style.
  ↳ [#1807](https://github.com/jemalloc/jemalloc/pull/1807): [ce17af4](https://github.com/jemalloc/jemalloc/commit/ce17af422172b9d924bccfc5d08bb44a10fb0cac)
- Extract and split dumps in prof recent, allocate release, recovery and asynchronous cleanup and other auxiliary functions to prepare for subsequent non-blocking dumps.
  ↳ [#1722](https://github.com/jemalloc/jemalloc/pull/1722): [035be44](https://github.com/jemalloc/jemalloc/commit/035be448674b852637f04d86bd85d04b672d71b3), [730658f](https://github.com/jemalloc/jemalloc/commit/730658f72fd8b7eafabdb50ba83a4d04aa7afbb5), [264d89d](https://github.com/jemalloc/jemalloc/commit/264d89d6415be31ee00dd3dd2460140f46cea2e9)
- Use SC_LG_NGROUP macro instead of hardcoded values in size_classes function, and clean up comment formatting.
  ↳ [#1814](https://github.com/jemalloc/jemalloc/pull/1814): [3589571](https://github.com/jemalloc/jemalloc/commit/3589571bfd4b1fda1d3771f96a08d7d14b7813bd)
- Simplified the calculation method of SC_NPSIZES, instead accumulating matching size classes.
  ↳ [#1821](https://github.com/jemalloc/jemalloc/pull/1821): [79dd0c0](https://github.com/jemalloc/jemalloc/commit/79dd0c04ed88fcebe9f65905d65d6e7ae32c4940)
- Changed prof_idump_accum function from inline to non-inline implementation.
  ↳ [#1819](https://github.com/jemalloc/jemalloc/pull/1819): [e10e505](https://github.com/jemalloc/jemalloc/commit/e10e5059e87b8d9c6ec9910d803bd1a1ba55da85)
- Reconstruct the thread event initialization logic, merge the initialization function into event processing, and ensure that the event counter is always initialized.
  ↳ [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [7324c4f](https://github.com/jemalloc/jemalloc/commit/7324c4f85f8d3d9597a1942dffcc6bf98b02fb8c), [75dae93](https://github.com/jemalloc/jemalloc/commit/75dae934a167424f0dad663e9f96fefdac25ae1b)
- Unify the reading and setting logic of the alignment flag and zero flag bits, and simplify the flag processing process in the allocation function.
  ↳ [#1849](https://github.com/jemalloc/jemalloc/pull/1849): [2a84f9b](https://github.com/jemalloc/jemalloc/commit/2a84f9b8fcf2ff8d87f0f3246b4b6d897520b240), [4b0c008](https://github.com/jemalloc/jemalloc/commit/4b0c008489020bd9d66c21e1452fe8324d11b3f0)
- Removed redundant background thread inactivity checks in arena.
  ↳ [#1856](https://github.com/jemalloc/jemalloc/pull/1856): [cbf096b](https://github.com/jemalloc/jemalloc/commit/cbf096b05ee1b21ce4244f04870083c63798ad64)
- Split the macro for initializing the statistics header into two independent macros: declaration and initialization.
  ↳ [#1914](https://github.com/jemalloc/jemalloc/pull/1914): [1f1a023](https://github.com/jemalloc/jemalloc/commit/1f1a0231ed9909119db2d350a2b44e1b21bda60f)
- Enforce the stability of usize during realloc, change parameters to value passing and add assertions.
  ↳ [#1923](https://github.com/jemalloc/jemalloc/pull/1923): [ea013d8](https://github.com/jemalloc/jemalloc/commit/ea013d8fa4eaa0a3d1fa1c15e8506a32f4e70475)
- Avoid disabling, refreshing or destroying HPA shards that have never been started.
  ↳ [#1969](https://github.com/jemalloc/jemalloc/pull/1969): [c9757d9](https://github.com/jemalloc/jemalloc/commit/c9757d9e3ba6b53e7f4ecbe9c1872a74df51fe4b)
- Moved the bitmap logic of hpdata out of psset, added auxiliary functions and enhanced verification.
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [089f8fa](https://github.com/jemalloc/jemalloc/commit/089f8fa4429f5e9ee0e679411941ef180e446248)
- Reconstruct the assign operation of flat bitmap and use visitor mode to support subsequent reuse.
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [e6c057a](https://github.com/jemalloc/jemalloc/commit/e6c057ad35b0c83eef100bf0e125f75ebf8b5edc)
- Replaced free page count with active page count in hpdata, and updated related access functions to make naming more consistent.
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [ff4086a](https://github.com/jemalloc/jemalloc/commit/ff4086aa6b9b957409ccdc6d818490154decd343)
- Extract the tcache refresh core logic into an independent function tcache_bin_flush_bottom to prepare for subsequent reuse.
  ↳ [#2173](https://github.com/jemalloc/jemalloc/pull/2173): [06aac61](https://github.com/jemalloc/jemalloc/commit/06aac61c4b261e5d1c8dcf3c7dd7921e9e395d62)
- Rearrange the fast path data in the TSD structure into a continuous layout to improve cache locality.
  ↳ [#1813](https://github.com/jemalloc/jemalloc/pull/1813): [58a00df](https://github.com/jemalloc/jemalloc/commit/58a00df2383fbe714da3b8a3697d68c4064d4b4a)
- Add a fast path in the paired heap insertion operation, and directly replace the new node when it is smaller than the root node to reduce link operations.
  ↳ [#2098](https://github.com/jemalloc/jemalloc/pull/2098): [dae2458](https://github.com/jemalloc/jemalloc/commit/dae24589bc4e4bcb2a19844e3c5753b8c50d714a)
- Adjust the number of internal spins of the mutex lock and increase the maximum spin count from 250 to 600.
  ↳ [#2102](https://github.com/jemalloc/jemalloc/pull/2102): [27f7124](https://github.com/jemalloc/jemalloc/commit/27f71242b74ea402db45c1e6b3b79708b78762d4)

### Test related
- Fix issue with assertion macro aborting incorrectly when expectation check fails, and issue with prof_recent_alloc_max_ctl_read function missing tsd parameter, and adjust test calls accordingly.
  ↳ [#1792](https://github.com/jemalloc/jemalloc/pull/1792): [ccdc70a](https://github.com/jemalloc/jemalloc/commit/ccdc70a5ce7b9dd723d947025f99006e7e78d17e) | [#1722](https://github.com/jemalloc/jemalloc/pull/1722): [b8bdea6](https://github.com/jemalloc/jemalloc/commit/b8bdea6b26509b3fd06bb9b3344fca7b2f22dee9)
- Add const qualifiers to test macros and auxiliary functions and introduce new functions to avoid compiler false positives and enhance test code robustness.
  ↳ [#1613](https://github.com/jemalloc/jemalloc/pull/1613): [22bc75e](https://github.com/jemalloc/jemalloc/commit/22bc75ee3e98fb45058fbee45210ed3ab65da6f4) | [#1759](https://github.com/jemalloc/jemalloc/pull/1759): [bc05ece](https://github.com/jemalloc/jemalloc/commit/bc05ecebf66531ebed82ad630d096061087ea18d)
- Limit the number of iterations of test_bitmap_xfu test to avoid too slow testing under large page sizes.
  ↳ [#1625](https://github.com/jemalloc/jemalloc/pull/1625): [4094b7c](https://github.com/jemalloc/jemalloc/commit/4094b7c03fb5e814f6f4c85ff7e93b3228dc4d29)
- Rename the sleep function in the test tool to sleep_ns, and fix the nanosecond to millisecond conversion error on the Windows platform.
  ↳ [#1734](https://github.com/jemalloc/jemalloc/pull/1734): [a72ea0d](https://github.com/jemalloc/jemalloc/commit/a72ea0db60bc475415c13f1057408389bccb40a4)
- Fix inspect unit test to reduce checks on small allocations to accommodate slab count changes when profiling is enabled.
  ↳ [#1782](https://github.com/jemalloc/jemalloc/pull/1782): [e732344](https://github.com/jemalloc/jemalloc/commit/e732344ef18fa295c1ca77ffc40760f5873db1b8)
- Rename the decay test file to arena_decay and add basic test cases.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [bf55e58](https://github.com/jemalloc/jemalloc/commit/bf55e58e63af719ce52a1df08758fb3a64ab2589), [48a2cd6](https://github.com/jemalloc/jemalloc/commit/48a2cd6d7932b2a38baab2d5394db3141d41b12e)
- Use non-reentrant test functions in garbage tests to avoid reentrant tests.
  ↳ [#1809](https://github.com/jemalloc/jemalloc/pull/1809): [8da6676](https://github.com/jemalloc/jemalloc/commit/8da6676a029f128753941eedcf2a8b4389cd80f1)
- Added new tool for checking random number distribution.
  ↳ [#1845](https://github.com/jemalloc/jemalloc/pull/1845): [537a4be](https://github.com/jemalloc/jemalloc/commit/537a4bedb4d4ae6238762df85ae1ad2bc8d0ff47)
- Added micro-benchmark for testing fill/flush behavior.
  ↳ [#1846](https://github.com/jemalloc/jemalloc/pull/1846): [97b7a9c](https://github.com/jemalloc/jemalloc/commit/97b7a9cf7702371d5f9827f71b6daf7eafe890ec)
- Added a test program for printing data structure size, and expanded the size check of rtree_t, rtree_leaf_elm_t and slab_data_t.
  ↳ [#1852](https://github.com/jemalloc/jemalloc/pull/1852): [17a64fe](https://github.com/jemalloc/jemalloc/commit/17a64fe91c4b424d10c96c94051d562390471810) | [#1859](https://github.com/jemalloc/jemalloc/pull/1859): [dcfa6fd](https://github.com/jemalloc/jemalloc/commit/dcfa6fd507d29e4d686abb5263a195c22d187ca0)
- Migrated size check tests from stress test suite to analyze test suite.
  ↳ [#1845](https://github.com/jemalloc/jemalloc/pull/1845): [d8cea87](https://github.com/jemalloc/jemalloc/commit/d8cea8756242a3a50dde4baf4fb8bf38eddac55d)
- Remove the auxiliary functions and related variables used to intercept prof_dump_header in the test to simplify the test code.
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [c2e7a06](https://github.com/jemalloc/jemalloc/commit/c2e7a063923f43b66a58815ff85f9fcf1681cc76)
- Extract the bitmap counting macro definition to a separate header file, and add more non-power-of-2 test data.
  ↳ [#1888](https://github.com/jemalloc/jemalloc/pull/1888): [efeab1f](https://github.com/jemalloc/jemalloc/commit/efeab1f4985281fb7cb12ffd985a84317bfb3332), [7fde6ac](https://github.com/jemalloc/jemalloc/commit/7fde6ac490bd6a257023aafcbedcf422a9413b4f)
- Added the number of nanoseconds per iteration to the benchmark output to facilitate direct evaluation of performance.
  ↳ [#1901](https://github.com/jemalloc/jemalloc/pull/1901): [753bbf1](https://github.com/jemalloc/jemalloc/commit/753bbf1849caaf4f523567b2da6cb1de6147d811)
- Fixed the type error caused by copy and paste in mallctl stress test, and corrected the output variable from char * to uint64_t.
  ↳ [#1913](https://github.com/jemalloc/jemalloc/pull/1913): [b0ffa39](https://github.com/jemalloc/jemalloc/commit/b0ffa39cac2af955b8b39e5457e9ca8ed3e8748b)
- In HPA unit testing, the condition for skipping tests is changed from pointer size check to calling hpa_supported() function.
  ↳ [#1991](https://github.com/jemalloc/jemalloc/pull/1991): [4a15008](https://github.com/jemalloc/jemalloc/commit/4a15008cfbf414136f40a57fb1ceac80b22ea09f)
- In prof_log tests, put prof_log_dummy_set calls inside config_prof conditions and changed some assertions from assert to expect to save binary space when profiling is disabled.
  ↳ [#1999](https://github.com/jemalloc/jemalloc/pull/1999): [83cad74](https://github.com/jemalloc/jemalloc/commit/83cad746aeb7ed68bedec501b4cb6c0eff438c11)
- RB unit tests are changed to non-reentrant mode to avoid repeated runs.
  ↳ [#2042](https://github.com/jemalloc/jemalloc/pull/2042): [b2c08ef](https://github.com/jemalloc/jemalloc/commit/b2c08ef2e62a72951488c1603113b2d3881bd9d6)
- Added new unit tests for the decay module, and optimized assertion expressions in existing tests.
  ↳ [#2089](https://github.com/jemalloc/jemalloc/pull/2089): [c88fe35](https://github.com/jemalloc/jemalloc/commit/c88fe355e64fa18eef932b4446aae7296babcc06)
- Renamed the test auxiliary header file arena_decay.h to arena_util.h, and updated all test files that reference this header file.
  ↳ [#2151](https://github.com/jemalloc/jemalloc/pull/2151): [2c70e8d](https://github.com/jemalloc/jemalloc/commit/2c70e8d3513edc5417a1fa6808350083e5c40f7d)
- Add a retry mechanism for background thread sleep in the test unit, with a maximum of 100 retries to cope with scheduling delays under high concurrent loads.
  ↳ [#2200](https://github.com/jemalloc/jemalloc/pull/2200): [6230cc8](https://github.com/jemalloc/jemalloc/commit/6230cc88b6b3902902c58e4331ca6273e71b8e2e)
- Reduce the number of concurrent threads in the stress test from 16 to 8 to avoid resource exhaustion problems under high concurrency.
  ↳ [#2202](https://github.com/jemalloc/jemalloc/pull/2202): [648b3b9](https://github.com/jemalloc/jemalloc/commit/648b3b9f768674934c2bbf260bdc75301a63a314)
- Added max_test_narenas function to limit the upper limit of the number of arenas created in the test to avoid exhaustion of 32-bit platform resources.
  ↳ [#2273](https://github.com/jemalloc/jemalloc/pull/2273): [66c8895](https://github.com/jemalloc/jemalloc/commit/66c889500a20e6493a6768de6eaa7347daf61483)

### Performance optimization
- Add a buffered writing mechanism to the malloc_stats_print function to reduce expensive malloc_write_fd calls and improve performance.
  ↳ [#1560](https://github.com/jemalloc/jemalloc/pull/1560): [28ed9b9](https://github.com/jemalloc/jemalloc/commit/28ed9b9a5198ed866750361fe2c36f83742900ac)
- Reconstruct tcache bin metadata from counter-based to pointer-based, use pointer comparison to determine full/empty status, avoid access to tcache_bin_info, and improve fast path performance by about 15%.
  ↳ [#1592](https://github.com/jemalloc/jemalloc/pull/1592): [7599c82](https://github.com/jemalloc/jemalloc/commit/7599c82d48ffaa07ce934320f7256b56b200dace)
- The result of multiplying ncached_max by the pointer size is pre-stored in tcache_bin_info, and a new auxiliary function is added to obtain the ncached_max value to optimize direct access performance.
  ↳ [#1596](https://github.com/jemalloc/jemalloc/pull/1596): [937ca1d](https://github.com/jemalloc/jemalloc/commit/937ca1db9fa1f3c5c54e189049e181b6de5e7133)
- Explicitly track cache refill status, optimize fast path allocation checks, avoid entering slow path when the last item is allocated.
  ↳ [#1603](https://github.com/jemalloc/jemalloc/pull/1603): [0043e68](https://github.com/jemalloc/jemalloc/commit/0043e68d4c54a305d84ead95cae27a730540451b)
- Completely move processing when prof_active is turned off to the slow path, reducing register pressure on malloc's fast path.
  ↳ [#1611](https://github.com/jemalloc/jemalloc/pull/1611): [adce29c](https://github.com/jemalloc/jemalloc/commit/adce29c88597c97f46fd02e28ce2689872ac1b0a)
- Optimize the cache allocation function in the malloc fast path, save registers by reducing access to tcache_bin_info, and add a simplified version of the allocation function.
  ↳ [#1642](https://github.com/jemalloc/jemalloc/pull/1642): [05681e3](https://github.com/jemalloc/jemalloc/commit/05681e387a3202567ff95528dbc460e92e031a3c)
- Merge tsd status check into event threshold check to optimize fast path performance; when tsd becomes abnormal, reset the fast threshold to 0.
  ↳ [#1680](https://github.com/jemalloc/jemalloc/pull/1680): [dd649c9](https://github.com/jemalloc/jemalloc/commit/dd649c94859e2cdbe7b527cfb743b549c8d8bf50)
- Introduce the nstime initialization tool function, replace the original manual initialization and update mode, and optimize the mutex spin logic.
  ↳ [#1706](https://github.com/jemalloc/jemalloc/pull/1706): [1d01e4c](https://github.com/jemalloc/jemalloc/commit/1d01e4c770c3229041f1010037da2533568fef05)
- Replace the mutex-protected counting operation in edata_cache from atomic fetch-add to the more lightweight load-store to improve performance.
  ↳ [#1782](https://github.com/jemalloc/jemalloc/pull/1782): [0dcd576](https://github.com/jemalloc/jemalloc/commit/0dcd576600b7ad1b4a142eb993e4f7639ccc638c)
- Optimize large memory allocation functions to pass zero-valued arguments directly as booleans and remove debugging performance optimizations that are no longer needed.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [1a11244](https://github.com/jemalloc/jemalloc/commit/1a1124462e8c671809535a3dd617f08252a48ce5)
- Move rtree_ctx from the TSD fast path to the end of the slow path to improve performance when using the fixed-length release function.
  ↳ [#1813](https://github.com/jemalloc/jemalloc/pull/1813): [4f8efba](https://github.com/jemalloc/jemalloc/commit/4f8efba8248aaafa2200e3538bae126729e0407d)
- Migrate file write operations in profiling data dumps to use buffered writers, and introduce callback functions to handle mapped file reads.
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [1c6742e](https://github.com/jemalloc/jemalloc/commit/1c6742e6a04376928ce1d6755666ba6141f038d8)
- Advance the zero-initialization decision of opt.zero into the core allocation path to avoid repeated zeroing through memset after allocation, and simplify related code logic.
  ↳ [#1837](https://github.com/jemalloc/jemalloc/pull/1837): [f1f8a75](https://github.com/jemalloc/jemalloc/commit/f1f8a75496cfff34d14bf067c4af92c63d9a521e)
- Reduce the waiting time for peak event detection and change the default update interval from 100K bytes to 64K bytes.
  ↳ [#1881](https://github.com/jemalloc/jemalloc/pull/1881): [e6cb7a1](https://github.com/jemalloc/jemalloc/commit/e6cb7a1c9b31de3c6eca367d9164a1896bbb60ae)
- Add a hard limit for the maximum size class (8MB) for tcache, and adjust the cache bin array size and initialization logic accordingly to reduce thread local storage usage and simplify layout.
  ↳ [#1958](https://github.com/jemalloc/jemalloc/pull/1958): [5e41ff9](https://github.com/jemalloc/jemalloc/commit/5e41ff9b740258bddebcbd5575e1670a15f8b1ae)
- Small batch allocation requests are changed to be allocated through tcache first to improve performance, and the prefork/postfork lock order and test logic are adjusted accordingly.
  ↳ [#1962](https://github.com/jemalloc/jemalloc/pull/1962): [d96e452](https://github.com/jemalloc/jemalloc/commit/d96e4525adaefbde79f349d024eb5f94e72faf50)
- Reduce the holding time of SEC shard locks, only refresh part of the extent and release the lock during refresh.
  ↳ [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [bf448d7](https://github.com/jemalloc/jemalloc/commit/bf448d7a5a4c2aecbda7ef11767a75829d9aaf77)
- Eliminate redundant operations in the arena-level dalloc function by forcing inline division constants and operation counts to keep the common path state in registers; simultaneously reconstruct the dalloc bin lock path and introduce step-by-step functions and data structures to optimize register usage.
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [229994a](https://github.com/jemalloc/jemalloc/commit/229994a204f7d4712fe5ecd1508fbbe679c1baf6)
- Cache its index in arena to reduce pointer indirections on performance-sensitive paths.
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [4c46e11](https://github.com/jemalloc/jemalloc/commit/4c46e11365566ec03723c46356cd524f4abd7fd8)
- Change the arena tcache decay timer from ticker_t to ticker_geom_t, and remove the related per-arena state management to optimize memory locality.
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [c259323](https://github.com/jemalloc/jemalloc/commit/c259323ab3082324100c708109dbfff660d0f4b8)
- HPA supports purge across reserved extents to reduce the number of expensive system calls.
  ↳ [#2084](https://github.com/jemalloc/jemalloc/pull/2084): [41fd566](https://github.com/jemalloc/jemalloc/commit/41fd56605e95c40650ab1d012b5e09c273b19490)
- Replace macros in paired heaps with inline functions and introduce an auxiliary list counting mechanism to optimize performance.
  ↳ [#2098](https://github.com/jemalloc/jemalloc/pull/2098): [08a4cc0](https://github.com/jemalloc/jemalloc/commit/08a4cc0969edf054c8483efd35981eb8b66eb0c1)
- Change the limited cache of edata_cache_small to an unbounded cache, remove the fill/flush heuristic, simplify cache management and improve performance.
  ↳ [#2097](https://github.com/jemalloc/jemalloc/pull/2097): [92a1e38](https://github.com/jemalloc/jemalloc/commit/92a1e38f5286bcc8f206c02219cd6b703b39d80d)
- Add auxiliary list counting and pre-merge optimization for paired heap insertion operations, and directly replace the root node to delay the auxiliary list operation when the root node is better.
  ↳ [#2098](https://github.com/jemalloc/jemalloc/pull/2098): [40d53e0](https://github.com/jemalloc/jemalloc/commit/40d53e007c054f37a5666b2550304adc65c74c78)
- Optimize debug checks through conditional compilation, removing entire loops in non-debug builds to improve performance.
  ↳ No PR: [912324a](https://github.com/jemalloc/jemalloc/commit/912324a1acae4bfb6445825caad000aa295dcca8)
- Optimize release fast path: merge tsd_fast() checks into the event threshold branch, eliminate the two instructions at the beginning of the path, and improve tolerance for uninitialized TSDs.
  ↳ [#2149](https://github.com/jemalloc/jemalloc/pull/2149): [4d56aae](https://github.com/jemalloc/jemalloc/commit/4d56aaeca5883ae5f4b5550c528503fb51fdf479)
- Change the return value of the rtree fast path search function from a pointer to a boolean value to avoid NULL checking branches that the compiler cannot optimize, thus eliminating extra branches.
  ↳ [#2150](https://github.com/jemalloc/jemalloc/pull/2150): [b6a7a53](https://github.com/jemalloc/jemalloc/commit/b6a7a535b32a3298db5b3518bc1f52fccc1597a6)
- Reduce binary size by adding assertions, marking cold functions and removing forced inlining.
  ↳ [#1999](https://github.com/jemalloc/jemalloc/pull/1999): [5d8e70a](https://github.com/jemalloc/jemalloc/commit/5d8e70ab26baf712a8741f9ba2acb646fba4de45), [a9fa2de](https://github.com/jemalloc/jemalloc/commit/a9fa2defdbe98b849151688cb70e24ba55dc8587), [f9bb8de](https://github.com/jemalloc/jemalloc/commit/f9bb8dedef92fc00225c52546acfb58bd8e74217)
- Optimize the cache locality and operation order of the cache bin module.
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [2014062](https://github.com/jemalloc/jemalloc/commit/20140629b44f9a76241749b9c47e3905202d034c) | [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [1b00d80](https://github.com/jemalloc/jemalloc/commit/1b00d808d7bfb9ff41c643dcb32f96a078090932)
- Unify the edata search path when tcache is refreshed, and adjust the size check conditions.
  ↳ [#2021](https://github.com/jemalloc/jemalloc/pull/2021): [c007c53](https://github.com/jemalloc/jemalloc/commit/c007c537ff038538b9312cf110bc5d395da14000)
- Adjust the condition judgment order and tcache acquisition location in the je_malloc function.
  ↳ [#1666](https://github.com/jemalloc/jemalloc/pull/1666): [836d7a7](https://github.com/jemalloc/jemalloc/commit/836d7a7e69011321ba75620279a31d43a05bf0d6)
- Fix the test configuration related to performance analysis to avoid test failure caused by disabled options.
  ↳ [#2186](https://github.com/jemalloc/jemalloc/pull/2186): [bd70d8f](https://github.com/jemalloc/jemalloc/commit/bd70d8fc0f35fc7883fad18216d09e613867314b) | [#2195](https://github.com/jemalloc/jemalloc/pull/2195): [d660683](https://github.com/jemalloc/jemalloc/commit/d660683d3ddc2aaebf41a5662a6bc629be016e6d)

### Security related
- Skip protected memory allocation tests when profiling is enabled to avoid array overflow issues.
  ↳ [#2151](https://github.com/jemalloc/jemalloc/pull/2151): [34b00f8](https://github.com/jemalloc/jemalloc/commit/34b00f896966e3993b8570542dfe77c2002ce185)
- Added auxiliary functions to avoid compilation warnings when buffer overflow is written.
  ↳ [#2217](https://github.com/jemalloc/jemalloc/pull/2217): [20f9802](https://github.com/jemalloc/jemalloc/commit/20f9802e4f25922884448d9581c66d76cc905c0c)
- Add volatile keyword to variables to bypass false positives for buffer overflow detection.
  ↳ [#2244](https://github.com/jemalloc/jemalloc/pull/2244): [ed5fc14](https://github.com/jemalloc/jemalloc/commit/ed5fc14b28ca62a6ba57b65adf557e1ef09037f0)

### Documentation
- Add comments to the pa_shard_decay_stats_t structure to clarify its design reasons.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [6ca918d](https://github.com/jemalloc/jemalloc/commit/6ca918d0cfe54587376282ec85edf153c2ea0d5b)
- Add detailed documentation comments for linked list and ring queue modules.
  ↳ [#1812](https://github.com/jemalloc/jemalloc/pull/1812): [877af24](https://github.com/jemalloc/jemalloc/commit/877af247a87f6cb335a0f98aef62cd90afcfa520)
- Added comments to the critical path of the bulk allocation logic, explaining the lazy initialization behavior of the cache box and arena, and the mechanism for relying on the slow path to fill the cache when the cache box runs out of memory.
  ↳ [#1962](https://github.com/jemalloc/jemalloc/pull/1962): [92e189b](https://github.com/jemalloc/jemalloc/commit/92e189be8b725be1f4de5f476f410173db29bc7d)
- Add a comment to the hpdata_consistent function stating that this function is only for testing and consistency verification.
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [3624dd4](https://github.com/jemalloc/jemalloc/commit/3624dd42ffd88e63a8f7c2ee0a6ed3cbdfff81b7)
- Add detailed comments to key functions in decay.c and decay.h to explain the calculation logic and parameter meaning of each function.
  ↳ [#2089](https://github.com/jemalloc/jemalloc/pull/2089): [aaea4fd](https://github.com/jemalloc/jemalloc/commit/aaea4fd1e640690042b34755fd5e4714ebd0459b)
- Updated opt.trust_madvise documentation to remove quotes around enabled and disabled and state the default values directly.
  ↳ [#2267](https://github.com/jemalloc/jemalloc/pull/2267): [254b011](https://github.com/jemalloc/jemalloc/commit/254b011915c0c68549beb7a91be02cf56d81fa32)
- Updated ChangeLog to record the release notes of version 5.3.0.
  ↳ [#2266](https://github.com/jemalloc/jemalloc/pull/2266): [304c919](https://github.com/jemalloc/jemalloc/commit/304c919829f9f340669b61fa64867cfe5dba8021)
- Added documentation on the internal principles of performance analysis implementation, and updated .gitignore to ignore the generated PDF files.
  ↳ [#1902](https://github.com/jemalloc/jemalloc/pull/1902): [d243b4e](https://github.com/jemalloc/jemalloc/commit/d243b4ec487224248172547643630f7a5fb5e84d)
- Modify opt.prof_leak documentation to clarify that this option only takes effect when opt.prof_final is also enabled.
  ↳ [#2164](https://github.com/jemalloc/jemalloc/pull/2164): [3b3257a](https://github.com/jemalloc/jemalloc/commit/3b3257a7092f447fa6c9a3a7305cb346dfb37841)

### Build/CI
- Add a hint to the fake version string generated when the VERSION file is missing, and it is recommended to execute git fetch tags.
  ↳ [#1599](https://github.com/jemalloc/jemalloc/pull/1599): [d2dddfb](https://github.com/jemalloc/jemalloc/commit/d2dddfb82aac9f2212922eb90324e84790704bfe)
- Added a new script to check whether the code complies with the clang-format format specification.
  ↳ [#1938](https://github.com/jemalloc/jemalloc/pull/1938): [025d8c3](https://github.com/jemalloc/jemalloc/commit/025d8c37c93a69ec0aa5d8a55e3793cb480a5ac8)
- Fix the race condition between document installation and generation in the Makefile to ensure that the document has been built before installation.
  ↳ No PR: [e5062e9](https://github.com/jemalloc/jemalloc/commit/e5062e9fb91e5f531266e5691a5567e7cc8fab5f)
- Add compilation flags in configure.ac to make clang report errors for unknown warning options, thus fixing clang compilation warning issues.
  ↳ [#2111](https://github.com/jemalloc/jemalloc/pull/2111): [2c625d5](https://github.com/jemalloc/jemalloc/commit/2c625d5cd97e9cb133072feab2edb6b8c78861ef)
- Add initialization modifications to test functions to eliminate compilation warnings, and update Travis CI configuration to the latest release.
  ↳ [#2083](https://github.com/jemalloc/jemalloc/pull/2083): [0689448](https://github.com/jemalloc/jemalloc/commit/0689448b1e8c8c5ae2d1c216f86c88d22a124166)
- Fix help string for --enable-doc option in configure.ac for consistency.
  ↳ [#2209](https://github.com/jemalloc/jemalloc/pull/2209): [8b49eb1](https://github.com/jemalloc/jemalloc/commit/8b49eb132eae6fd3de081addb06d967470bfa2aa)
- Simplify the output of the Makefile installation target, use install -v instead of manual echo.
  ↳ [#2212](https://github.com/jemalloc/jemalloc/pull/2212): [f15d8f3](https://github.com/jemalloc/jemalloc/commit/f15d8f3b416f6812ac030bc1a7aacf05927a4d7f)
- Fix issues caused by je_ prefix in MSVC tests, add macro definition to disable symbol renaming.
  ↳ [#1635](https://github.com/jemalloc/jemalloc/pull/1635): [1df9dd3](https://github.com/jemalloc/jemalloc/commit/1df9dd35154ca460facbd74f779a13dcece78dac)
- Fixed test failures caused by compilation warnings under the new version of GCC, adjusted macro definitions and added auxiliary functions.
  ↳ [#1694](https://github.com/jemalloc/jemalloc/pull/1694): [1b1e76a](https://github.com/jemalloc/jemalloc/commit/1b1e76acfe281e5b27a2ce0e28342cbc04c01b37)
- Modify the build script to automatically detect GNU make and select the appropriate make command.
  ↳ [#1627](https://github.com/jemalloc/jemalloc/pull/1627): [e06658c](https://github.com/jemalloc/jemalloc/commit/e06658cb24e9f880570c5a44a5ad6b11b620efc5)
- Added -Wpointer-arith warning to GCC compile options to detect non-portable pointer arithmetic.
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [b428dce](https://github.com/jemalloc/jemalloc/commit/b428dceeaf87fb35a16c2337ac13105f7d18dfd3)
- Combine the list of common symbols in configure.ac into one line to simplify configuration.
  ↳ [#1806](https://github.com/jemalloc/jemalloc/pull/1806): [0d6d9e8](https://github.com/jemalloc/jemalloc/commit/0d6d9e85866b77b39d39e0957fd2a577b3091935)
- Removed the no longer used LG_QUANTA variable in the build configuration.
  ↳ [#1821](https://github.com/jemalloc/jemalloc/pull/1821): [fb6cfff](https://github.com/jemalloc/jemalloc/commit/fb6cfffd39ca50add3356c2e61242e13fff2ce1f)
- Add compile option to suppress warnings about missing field initializers, fix build errors caused by unified initialization.
  ↳ [#1854](https://github.com/jemalloc/jemalloc/pull/1854): [cd28e60](https://github.com/jemalloc/jemalloc/commit/cd28e60337d3e4ef183f407df734f0095a3c1352)
- Update keyring in Appveyor CI configuration and adjust package installation steps.
  ↳ [#1891](https://github.com/jemalloc/jemalloc/pull/1891): [786a27b](https://github.com/jemalloc/jemalloc/commit/786a27b9e5dfb732bc1d893cc236354c225c8f1c)
- Removed steps to update msys2 keyring in Appveyor CI.
  ↳ [#1949](https://github.com/jemalloc/jemalloc/pull/1949): [bdb60a8](https://github.com/jemalloc/jemalloc/commit/bdb60a8053dcac4eb39deaa17129b6e40ba6b17a)
- Fix Appveyor CI configuration, remove invalid remote mirror installation steps to resolve 404 errors.
  ↳ [#1966](https://github.com/jemalloc/jemalloc/pull/1966): [180b843](https://github.com/jemalloc/jemalloc/commit/180b84315933b7d986fff7539eeb262eb44bc75d)
- Remove duplicate JEMALLOC_DEBUG macro definition in configure.ac.
  ↳ [#2039](https://github.com/jemalloc/jemalloc/pull/2039): [1112724](https://github.com/jemalloc/jemalloc/commit/11127240caefb579a213ad075ab4f52910f333e2)
- Remove duplicate clang tests on OS X to speed up CI feedback.
  ↳ [#2087](https://github.com/jemalloc/jemalloc/pull/2087): [9c42ed2](https://github.com/jemalloc/jemalloc/commit/9c42ed2d1491451dcc8cdb429ecf9ee46070054d)
- Ported test script gen_run_tests.py to Python 3.
  ↳ [#2112](https://github.com/jemalloc/jemalloc/pull/2112): [9d02bdc](https://github.com/jemalloc/jemalloc/commit/9d02bdc8838d03b043de5017eaaa837f21dbc4c0)
- Reconstructed the Travis CI configuration generation script to decouple operating system configuration and task matrix generation logic.
  ↳ [#2154](https://github.com/jemalloc/jemalloc/pull/2154): [d9bbf53](https://github.com/jemalloc/jemalloc/commit/d9bbf539ff9cee5f138e03ad2e7f61263d381c7f)
- Fixed autoheader warning, added comment parameter for AC_DEFINE in configure.ac.
  ↳ No PR: [e491df1](https://github.com/jemalloc/jemalloc/commit/e491df1d2f686a1ba47036301693285a72d98ca2)
- Optimized the Travis CI build process, disabled Windows jobs that took too long and adjusted the job order.
  ↳ [#2185](https://github.com/jemalloc/jemalloc/pull/2185): [002f0e9](https://github.com/jemalloc/jemalloc/commit/002f0e939795991f3f30fd0a6b0470094890305f) | [#2207](https://github.com/jemalloc/jemalloc/pull/2207): [25517b8](https://github.com/jemalloc/jemalloc/commit/25517b852e76b429d4a97f4c96606263b2a9c209)
- Updated INSTALL.md to note that the default build target only builds documents when xsltproc is available.
  ↳ [#1600](https://github.com/jemalloc/jemalloc/pull/1600): [d6b7995](https://github.com/jemalloc/jemalloc/commit/d6b7995c1629768590366a6ff2170d65c4cc6d9b)
- Removed documentation for experimental configuration option --with-slab-maxregs from INSTALL.md.
  ↳ [#1937](https://github.com/jemalloc/jemalloc/pull/1937): [40cf71a](https://github.com/jemalloc/jemalloc/commit/40cf71a06d07faadc03b81f97697826c53b3fa62)
- Updated INSTALL.md, indicating that running ./autogen.sh requires installing autoconf.
  ↳ [#2031](https://github.com/jemalloc/jemalloc/pull/2031): [cde7097](https://github.com/jemalloc/jemalloc/commit/cde7097ecaba08b50c5594137175e0e1e567f4c4)

### Maintenance
- Added statistics reporting support for prof_dump_mtx and tdatas_mtx.
  ↳ [#1582](https://github.com/jemalloc/jemalloc/pull/1582): [3934355](https://github.com/jemalloc/jemalloc/commit/39343555d6ac84a105a2d5e8ba0059115eb20f93)
- Reconstructed the prof dump parameter structure, unified the type and adjusted the function interface.
  ↳ [#1794](https://github.com/jemalloc/jemalloc/pull/1794): [4556d3c](https://github.com/jemalloc/jemalloc/commit/4556d3c0c8ad4c00fd3c31762653e68fb2a701e0), [5d823f3](https://github.com/jemalloc/jemalloc/commit/5d823f3a910c7d737500b61ff8a00f6b634bc08b), [80d18c1](https://github.com/jemalloc/jemalloc/commit/80d18c18c9a39e534ecb080256cb00e652f3d863)
- In non-JSON output mode, optimize bin statistics output: omit rows without data and fix the processing of separator lines ending gaps.
  ↳ [#1921](https://github.com/jemalloc/jemalloc/pull/1921): [6c5a3a2](https://github.com/jemalloc/jemalloc/commit/6c5a3a24dd03e98c8b78178496c2a9756ec1490a), [22d62d8](https://github.com/jemalloc/jemalloc/commit/22d62d8cbd873fd3b2acb4bfccf6a06cd2e0d2e7)
- Fix unnecessary return statements in san_guard_pages_two_sided and san_unguard_pages_two_sided functions.
  ↳ [#2196](https://github.com/jemalloc/jemalloc/pull/2196): [067c2da](https://github.com/jemalloc/jemalloc/commit/067c2da07456660113bbb7bf76f0648c3c993a83)
- Updated the layout description of thread local storage (TSD), added new field representation and updated cache line occupancy description.
  ↳ [#1523](https://github.com/jemalloc/jemalloc/pull/1523): [56c8ecf](https://github.com/jemalloc/jemalloc/commit/56c8ecffc1f84f630e10f775bc29fcf4c743a3c9) | [#1756](https://github.com/jemalloc/jemalloc/pull/1756): [c6bfe55](https://github.com/jemalloc/jemalloc/commit/c6bfe55857230949ea2d6467c1dc3fce213fe9c3)
- Change the release function of nodes in the prof log from idalloc to idalloctm, and set tcache and internal flags correctly.
  ↳ [#1586](https://github.com/jemalloc/jemalloc/pull/1586): [22746d3](https://github.com/jemalloc/jemalloc/commit/22746d3c9fddd5486e9ec5c0c6b2e25230db9a8e)
- Removed a transitional temporary declaration in eset.h.
  ↳ [#1634](https://github.com/jemalloc/jemalloc/pull/1634): [c97d255](https://github.com/jemalloc/jemalloc/commit/c97d255752e3dd53dbfcb5c3fdf9d972da2b47f1)
- Increased the width of the global malloc/free rate statistics column to accommodate high values in large services.
  ↳ [#1654](https://github.com/jemalloc/jemalloc/pull/1654): [4786099](https://github.com/jemalloc/jemalloc/commit/4786099a3ad11dbf4027f453b8c6de1c1e8777db)
- Enable compiler implicit fallthrough checking and uniformly replace fallthrough annotations with the JEMALLOC_FALLTHROUGH macro.
  ↳ [#1661](https://github.com/jemalloc/jemalloc/pull/1661): [d01b425](https://github.com/jemalloc/jemalloc/commit/d01b425e5d1e1ed3d7f7c5571002681469acf601)
- Prioritize using the getaffinity method to detect the number of CPUs to more accurately reflect the number of available cores.
  ↳ [#1676](https://github.com/jemalloc/jemalloc/pull/1676): [a787d2f](https://github.com/jemalloc/jemalloc/commit/a787d2f5b35f8a28738e19efeea626c2a3999104)
- Fixed incorrect use of cassert macro, replacing it with the standard assert macro.
  ↳ [#1690](https://github.com/jemalloc/jemalloc/pull/1690): [1decf95](https://github.com/jemalloc/jemalloc/commit/1decf958d1dabc1d1d217889cdcea7edb2eefd3e)
- Introduce a stub C file for the decay module.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [4d090d2](https://github.com/jemalloc/jemalloc/commit/4d090d23f1518327ba1c5b1477d4f5a31a6cb745)
- Cleaned up and commented out the page allocation (PA) module, including changing pa_decay_to_limit to a static function and adjusting the lock holding position.
  ↳ [#1804](https://github.com/jemalloc/jemalloc/pull/1804): [c075fd0](https://github.com/jemalloc/jemalloc/commit/c075fd0bcb4a4de13204d26ff400bd315811e435)
- Increased dump buffer size for prof last-N list.
  ↳ [#1722](https://github.com/jemalloc/jemalloc/pull/1722): [fc8bc4b](https://github.com/jemalloc/jemalloc/commit/fc8bc4b5c04501f17f7a3c3a5f3efafbf9b2a82e)
- Removed unused prof_accum field from arena structure.
  ↳ [#1819](https://github.com/jemalloc/jemalloc/pull/1819): [d454af9](https://github.com/jemalloc/jemalloc/commit/d454af90f102c99eddb38909fc7822769c4213aa)
- Remove duplicate entry logging in malloc function.
  ↳ [#1861](https://github.com/jemalloc/jemalloc/pull/1861): [40672b0](https://github.com/jemalloc/jemalloc/commit/40672b0b78207f3b624bd20772b24865d208f215)
- Removed unused header file base_structs.h.
  ↳ [#2133](https://github.com/jemalloc/jemalloc/pull/2133): [3c4b717](https://github.com/jemalloc/jemalloc/commit/3c4b717ffc05012905fec0c4b49cda8f783c2727)
- Fixed compilation warnings in tcache, including variable uninitialized and type conversion warnings.
  ↳ [#2173](https://github.com/jemalloc/jemalloc/pull/2173): [8b34a78](https://github.com/jemalloc/jemalloc/commit/8b34a788b52c6410ef68f2dab6ebbf5079a0660e) | [#2196](https://github.com/jemalloc/jemalloc/pull/2196): [f509703](https://github.com/jemalloc/jemalloc/commit/f509703af59348496abdb0cb446e8d3d04bc085d)
- Move the decrement_recent_count call after the mutex is unlocked to avoid lock overlap.
  ↳ [#1734](https://github.com/jemalloc/jemalloc/pull/1734): [7b67ed0](https://github.com/jemalloc/jemalloc/commit/7b67ed0b5a90d5288c66c132f210883dece99181)
- Add branch prediction hints to free_fastpath, mark non-slab situations as unlikely, and optimize the execution efficiency of common paths.
  ↳ [#1686](https://github.com/jemalloc/jemalloc/pull/1686): [7160617](https://github.com/jemalloc/jemalloc/commit/7160617107af5f566902ea3d1281b3a3c3cb6eea)
- Delay the operation of getting the allocation time until after it is confirmed that it is a sample allocation, and only execute it when sampling, and adjust the condition for resetting the latest allocation record.
  ↳ [#1731](https://github.com/jemalloc/jemalloc/pull/1731): [ad3f3fc](https://github.com/jemalloc/jemalloc/commit/ad3f3fc561d5829a0a998c1b0650f6e7c7474a74)
- Optimize the performance of free range allocation in hpdata, exit the scan of the longest free range early when allocating, and add related assertions and consistency checks.
  ↳ [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [271a676](https://github.com/jemalloc/jemalloc/commit/271a676dcd2d5ff863e8f6996089680f56fa0656)

### Others
- Fixed multiple spelling errors in code, comments and build files.
  ↳ [#1679](https://github.com/jemalloc/jemalloc/pull/1679): [9c59abe](https://github.com/jemalloc/jemalloc/commit/9c59abe42afd044b742bd5c2ec8c1e01a4a8c1ca) | [#2029](https://github.com/jemalloc/jemalloc/pull/2029): [4b8870c](https://github.com/jemalloc/jemalloc/commit/4b8870c7dbfaeea7136a8e0b9f93a2ad85d31a55) | [#2064](https://github.com/jemalloc/jemalloc/pull/2064): [4f7cb3a](https://github.com/jemalloc/jemalloc/commit/4f7cb3a413a966056a6c23eb996ba1d51d0517a3) | [#2073](https://github.com/jemalloc/jemalloc/pull/2073): [2c0f4c2](https://github.com/jemalloc/jemalloc/commit/2c0f4c2ac3b6a78a849526be384a7a2349d1a09c) | [#2098](https://github.com/jemalloc/jemalloc/pull/2098): [0170dd1](https://github.com/jemalloc/jemalloc/commit/0170dd198ae0ef92ae923b454c02259802b78b76) | [#2260](https://github.com/jemalloc/jemalloc/pull/2260): [9a242f1](https://github.com/jemalloc/jemalloc/commit/9a242f16d9e4a6afcd53782a9427471f6d144f1f)
- Fixed link syntax, example value and name errors in the document.
  ↳ [#1746](https://github.com/jemalloc/jemalloc/pull/1746): [ea351a7](https://github.com/jemalloc/jemalloc/commit/ea351a7b52430de88007bf16f354a132da311c5b) | [#2045](https://github.com/jemalloc/jemalloc/pull/2045): [2ae1ef7](https://github.com/jemalloc/jemalloc/commit/2ae1ef7dbd9aadfc80db9692004b5052fd3b36ea) | [#2261](https://github.com/jemalloc/jemalloc/pull/2261): [ceca07d](https://github.com/jemalloc/jemalloc/commit/ceca07d2ca95f7c2680263f3c679ba3f611d5ffb)
- Clean up code format and unify indentation and comma styles.
  ↳ [#1705](https://github.com/jemalloc/jemalloc/pull/1705): [837119a](https://github.com/jemalloc/jemalloc/commit/837119a9489992e1c4326015ae21e16c246ed094), [f83fdf5](https://github.com/jemalloc/jemalloc/commit/f83fdf5336b6705bac027cb3f70b6ca4485cb0c1)
- Remove unnecessary module identification macros, header file includes, duplicate declarations and outdated comments.
  ↳ [#1866](https://github.com/jemalloc/jemalloc/pull/1866): [a795b19](https://github.com/jemalloc/jemalloc/commit/a795b1932780503cf5422920975a1c38994c7581), [092fcac](https://github.com/jemalloc/jemalloc/commit/092fcac0b4b3854c12c51d22174df00303a3fe6a) | [#2046](https://github.com/jemalloc/jemalloc/pull/2046): [a137a68](https://github.com/jemalloc/jemalloc/commit/a137a6825253da928b49149a81f82e73ed0d7b75) | [#1796](https://github.com/jemalloc/jemalloc/pull/1796): [855d20f](https://github.com/jemalloc/jemalloc/commit/855d20f6f3d79d00fad35d63456fbdc0e02a0747)
- Removed a test case that would fail in non-strict mode.
  ↳ [#1669](https://github.com/jemalloc/jemalloc/pull/1669): [a8b578d](https://github.com/jemalloc/jemalloc/commit/a8b578d538adced7506aec1179379eb541c0198d)
- Added initialization macros to eliminate compiler warnings.
  ↳ [#1784](https://github.com/jemalloc/jemalloc/pull/1784): [22657a5](https://github.com/jemalloc/jemalloc/commit/22657a5e65953c25531caf155d52ed43eb0c653f)
- Renamed internal variables to improve readability.
  ↳ [#2173](https://github.com/jemalloc/jemalloc/pull/2173): [eabe889](https://github.com/jemalloc/jemalloc/commit/eabe88916290fec452048eaa1abe1cd52a794339)
- Alphabetically sort the list of test tools in the Makefile.
  ↳ [#1901](https://github.com/jemalloc/jemalloc/pull/1901): [38867c5](https://github.com/jemalloc/jemalloc/commit/38867c5c1723efa7e42898e1737e1587b5c734e1)
- Changed the string in HPA shard statistics report from inactive to retained.
  ↳ [#1995](https://github.com/jemalloc/jemalloc/pull/1995): [061cabb](https://github.com/jemalloc/jemalloc/commit/061cabb7122d1fd63b8bfbe980a1fb1dcf3033f4)
- Fixed a spelling error in the document.
  ↳ [#2263](https://github.com/jemalloc/jemalloc/pull/2263): [f5e840b](https://github.com/jemalloc/jemalloc/commit/f5e840bbf0213d86ae3d0a915df8abd03d75cdf6)
