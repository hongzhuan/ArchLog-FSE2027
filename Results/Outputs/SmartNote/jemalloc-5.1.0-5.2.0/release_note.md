# 5.2.0
## 🐛 fix
- Fix stats output (rate for total # of requests). [#1413](https://github.com/jemalloc/jemalloc/pull/1413) 
- Set huge_threshold to 8M by default. [#1412](https://github.com/jemalloc/jemalloc/pull/1412) 
- Add configure option --disable-libdl [#1244](https://github.com/jemalloc/jemalloc/pull/1244) 
- By @zoulasc: fix a missing unlock bug and a warning [#1472](https://github.com/jemalloc/jemalloc/pull/1472) 
- Two minor fixes [#1476](https://github.com/jemalloc/jemalloc/pull/1476) 
- Avoid taking large_mtx for auto arenas. [#1228](https://github.com/jemalloc/jemalloc/pull/1228) 
- Fall back to the default pthread_create if RTLD_NEXT fails. [#1242](https://github.com/jemalloc/jemalloc/pull/1242) 
- Fix tcaches_flush. [#1368](https://github.com/jemalloc/jemalloc/pull/1368) 
- Force purge on thread death only when w/o bg thds. [#1405](https://github.com/jemalloc/jemalloc/pull/1405) 
- Sanity check szind on tcache flush. [#1427](https://github.com/jemalloc/jemalloc/pull/1427) 
- Guard libgcc unwind init with opt_prof. [#1441](https://github.com/jemalloc/jemalloc/pull/1441) 
## 🧪 test
- Implement huge arena: opt.huge_threshold. [#1235](https://github.com/jemalloc/jemalloc/pull/1235)