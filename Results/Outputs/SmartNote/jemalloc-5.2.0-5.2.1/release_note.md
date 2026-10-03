# 5.2.1
## ✨ feat
- Add nonfull_slabs to bin_stats_t. [#1486](https://github.com/jemalloc/jemalloc/pull/1486) 
## 🐛 fix
- Implement retain on Windows. [#1545](https://github.com/jemalloc/jemalloc/pull/1545) 
- Ensure page alignment on extent_alloc. [#1470](https://github.com/jemalloc/jemalloc/pull/1470) 
- Enforce TLS_MODEL attribute. [#1482](https://github.com/jemalloc/jemalloc/pull/1482) 
- Remove best fit [5679751](https://github.com/jemalloc/jemalloc/commit/56797512083fe1457163170dfa44ee5ec12abe5f) 
- Fix assert in free fastpath [#1506](https://github.com/jemalloc/jemalloc/pull/1506) 
- Avoid blocking on background thread lock for stats. [#1510](https://github.com/jemalloc/jemalloc/pull/1510) 
- Fix logic in printing [#1520](https://github.com/jemalloc/jemalloc/pull/1520) 
- Fix posix_memalign with input size 0. [#1554](https://github.com/jemalloc/jemalloc/pull/1554) 
- Track the leaked VM space via the abandoned_vm counter. [#1553](https://github.com/jemalloc/jemalloc/pull/1553) 
- Optimize max_active_fit in first_fit. [#1562](https://github.com/jemalloc/jemalloc/pull/1562) 
- Update manual for opt.retain (new default on Windows). [#1567](https://github.com/jemalloc/jemalloc/pull/1567) 
- Add indent to individual options for confirm_conf. [#1568](https://github.com/jemalloc/jemalloc/pull/1568) 
- Limit to exact fit on Windows with retain off. [#1573](https://github.com/jemalloc/jemalloc/pull/1573) 
- Sanity check on prof dump buffer size. [#1579](https://github.com/jemalloc/jemalloc/pull/1579) 
## ♻️ refactor
- Add a feature to do redzone checks for small sampled allocations [#1465](https://github.com/jemalloc/jemalloc/pull/1465) 
## 🔧 chore
- Revert "Refactor profiling" [#1574](https://github.com/jemalloc/jemalloc/pull/1574) 
- Lower nthreads in test/unit/retained on 32-bit to avoid OOM. [#1566](https://github.com/jemalloc/jemalloc/pull/1566) 
## 🧪 test
- Improve memory utilization tests [#1505](https://github.com/jemalloc/jemalloc/pull/1505)