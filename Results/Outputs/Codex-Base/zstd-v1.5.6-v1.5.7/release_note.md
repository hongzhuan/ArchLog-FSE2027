# Release Note

## Important Changes

### Core Compression Engine

- Extract and unify the index overlap safety check for the dictionary matchfinder, for reuse across different compression strategies. [commit](https://github.com/facebook/zstd/commit/5e9a6c2fe4e4bfabeef750642871e3edcf6c6d79)

- Restrict the operation range on match indices in 32 bit mode to avoid index out-of-bounds/wraparound. [commit](https://github.com/facebook/zstd/commit/09cb37cbb1be014756fbc00d3c5db8eaec20f32d)

- The fast and double-fast matchers introduce a match candidate check path that uses conditional moves instead of hard-to-predict branches, reducing branch prediction cost, and are used for dictionary fast compression. [commit](https://github.com/facebook/zstd/commit/e8fce38954efd6bc58a5b0ec72dd26f41c8365e6) [commit](https://github.com/facebook/zstd/commit/1e7fa242f4aa71c3aec5e1e39ec69ad54e117051) [commit](https://github.com/facebook/zstd/commit/2cc600bab21657ccf966ceadfeb316e2eacff25c) [commit](https://github.com/facebook/zstd/commit/186b1324951f2505469a3415aaf8ddc3398b9fca) [commit](https://github.com/facebook/zstd/commit/197c258a79a94b60ec45020defc5fb6a2f570e80) [commit](https://github.com/facebook/zstd/commit/741b860fc1e8171519a72bf3d30cdd20995b00ce) [commit](https://github.com/facebook/zstd/commit/d45aee43f4b1ac8ee0fbb182310b9b7622f85d1c) [commit](https://github.com/facebook/zstd/commit/fa1fcb08ab447de8cdb4492d663779cad6841379) [commit](https://github.com/facebook/zstd/commit/83de00316c29a7f5245a67733f6208c699b686c2) [commit](https://github.com/facebook/zstd/commit/8e5823b65c6d0d1eb1c07be8428f427df5892d3a) [commit](https://github.com/facebook/zstd/commit/e63896eb5844cb246aad7959ab208aa0a8f152bd) [commit](https://github.com/facebook/zstd/commit/730d2dce41800d2850726cdb0eefbf5fcb10b3de)

- Improve candidate match comparison for double-fast at compression levels 3/4, improving compression ratio for dictionary data; update related regression results and tests. [commit](https://github.com/facebook/zstd/commit/c2abfc5ba40b2c7863080c937b728fb902b9cb5b) [commit](https://github.com/facebook/zstd/commit/632677516616434c312d2fff2d84dcf0c9b78012) [commit](https://github.com/facebook/zstd/commit/61d08b0e42e7397af479ca9d1b66fe7235508f34) [commit](https://github.com/facebook/zstd/commit/47d4f5662df83c1a84476ab6c6f7fcb1d415f4f1) [commit](https://github.com/facebook/zstd/commit/41d870fbbf594c1ee1c0ac4113d1278ebf8301da)

- Add an adaptive pre-splitter: sample fingerprints in 4 KB segments, select boundaries for full 128 KB input blocks; enabled for high-compression strategies, and skip splitting when estimated benefit is insufficient to control extra overhead on incompressible data. [commit](https://github.com/facebook/zstd/commit/a5bce4ae84daa5885e61753fa98903964c3348bd) [commit](https://github.com/facebook/zstd/commit/9e52789962bc5d47ee62bc3e499c52435c693e89) [commit](https://github.com/facebook/zstd/commit/586ca96fec794cde09f4aa01fe792a9779b62368) [commit](https://github.com/facebook/zstd/commit/e2d7d08888f915667c94e6dbbadaee38a5d50fa5) [commit](https://github.com/facebook/zstd/commit/6021b6663a4705f446f7cf856d944819caa575c3) [commit](https://github.com/facebook/zstd/commit/fa147cbb4d3fbd8c31b1f35c7984ae62f4c6ea03) [commit](https://github.com/facebook/zstd/commit/83a3402a928ef07700b1431c86534bec902ad11d) [commit](https://github.com/facebook/zstd/commit/f83ed087f6310a8cf51267ea431ec4a7b7ffd94f) [commit](https://github.com/facebook/zstd/commit/8b3887f579f7e98d09ec3823736b467ceaebbcd1) [commit](https://github.com/facebook/zstd/commit/dd38c677ebd680f29afdf4eab5c08d7a01eb8f39) [commit](https://github.com/facebook/zstd/commit/0d4b52065791a8e96faf8eb7665cb701b29d186e) [commit](https://github.com/facebook/zstd/commit/20c3d176cd8871d01fe8135bdc7693a208d739bc) [commit](https://github.com/facebook/zstd/commit/6dc52122e6e8b28b8477a202726dfff7d0ce0b9c) [commit](https://github.com/facebook/zstd/commit/80a912dec1e5ec1fad6e6a698cfe04685c0d865e) [commit](https://github.com/facebook/zstd/commit/6939235f010255bbe513dc5b18b1796cbee39d52) [commit](https://github.com/facebook/zstd/commit/cdddcaaec9111c4ab086a55e4d0337131ca13fd0) [commit](https://github.com/facebook/zstd/commit/76ad1d69039c4900e5a0dca8eec7f3da2bebc050) [commit](https://github.com/facebook/zstd/commit/31d48e9ffadde779e5fd9b290dee44f616b050fa) [commit](https://github.com/facebook/zstd/commit/7f015c2fd799d3c273c5986a63059ef9536b701e) [commit](https://github.com/facebook/zstd/commit/73a665365350668757ec542277472ca73267603a) [commit](https://github.com/facebook/zstd/commit/433f4598ad96a4e661cfd877b50c9000ea174897)

- Extend the adaptive pre-splitter with different sampling rates and boundary statistics paths, and select detection level based on compression strategy; the pre-splitting level can be explicitly adjusted via the experimental ZSTD_c_blockSplitterLevel parameter. [commit](https://github.com/facebook/zstd/commit/a167571db535377070c43098932a7747d859177c) [commit](https://github.com/facebook/zstd/commit/566763fdc9b54220e8e419446331dc15fb1c183b) [commit](https://github.com/facebook/zstd/commit/da2c0dffd8c3e6306fcf2e8e5bd5f8ef97d7a999) [commit](https://github.com/facebook/zstd/commit/e557abc8a0380b095b14623ca7c4105a38fdb981) [commit](https://github.com/facebook/zstd/commit/226ae73311d1ffd0c3488d8bc6a59576d910d6d4) [commit](https://github.com/facebook/zstd/commit/bbaba45589f233b91a310806d97ee7b4d9ee8320)

- Promote ZSTD_getErrorCode() to a stable API, making it easier for applications to handle function results based on error code enums. [commit](https://github.com/facebook/zstd/commit/d9553fd2180535a11dcb4e2f5a3197202befc2c0) [commit](https://github.com/facebook/zstd/commit/51eb7daf39c8e8a7c338ba214a9d4e2a6a086826)

- Add experimental static API ZSTD_compressSequencesAndLiterals(), allowing external sequence generators to pass sequences and extracted literals directly to the compressor, avoiding internal extraction and caching; now supports multi-block frames. Only explicit block delimiting is supported, requiring correct provision of decompressed size, literal capacity at least 8 bytes more than actual length, and sequence validation or frame checksum cannot be enabled; incompressible blocks return a dedicated error code. The advanced parameter ZSTD_c_repcodeResolution controls repcode resolution. [commit](https://github.com/facebook/zstd/commit/125f05282b0566790551e6756bdbc0290addfcb2) [commit](https://github.com/facebook/zstd/commit/a00f45a03751a90f620425f30690d86d872dfef1) [commit](https://github.com/facebook/zstd/commit/e9f8a119b4fcd44038dbb0d072aa44968d81bd9b) [commit](https://github.com/facebook/zstd/commit/0165eeb441de43ffe11b95b9073c0a694b66e6a4) [commit](https://github.com/facebook/zstd/commit/2d8710c4471ba7f2984b6553f9d3e2e0e7c2b89e) [commit](https://github.com/facebook/zstd/commit/14a21e43b31042b8cd67d4a757920735a8d33d94) [commit](https://github.com/facebook/zstd/commit/0b013b26884bb25149eedc6d78a5d8f5dc38739a) [commit](https://github.com/facebook/zstd/commit/e0f3aaee467bbcb7e1653756eb426a9b7adde5d8) [commit](https://github.com/facebook/zstd/commit/5164d44dabbbf2f3f1cd89bbf1244b7b73d69ef3) [commit](https://github.com/facebook/zstd/commit/31b5ef25393c3abf4bb9e290cf32b06d97c78b93) [commit](https://github.com/facebook/zstd/commit/12c47d32624df633b9dd3402273529cff7705228) [commit](https://github.com/facebook/zstd/commit/0a54f6f288bab194e1c4edcd03cedc8d084c2d6f) [commit](https://github.com/facebook/zstd/commit/b339efff2bc9d11ce091bca62328c1884a38b5f3) [commit](https://github.com/facebook/zstd/commit/76445bb379fe74b0a8cddcce2658c111a2e8d7b0) [commit](https://github.com/facebook/zstd/commit/b7a9e69d8dc8b61be9d341a4e7a56350fb1e545e) [commit](https://github.com/facebook/zstd/commit/f8725e80cc6089ec21903e292a58a21d322e302b) [commit](https://github.com/facebook/zstd/commit/92be4be8102eecedaa0d2a7c65b2d1088e01622a) [commit](https://github.com/facebook/zstd/commit/1d088ba55cccd9872ad3810ddf82e557d71bbd3d)

- Frame header queries now fill in type, headerSize, content size, and magic variant for skippable frames; documentation explains the return behavior of related frame APIs on skippable frames. [commit](https://github.com/facebook/zstd/commit/f8a2b352d62b1a2e41ff1715e1afe8771fe43abc) [commit](https://github.com/facebook/zstd/commit/a2ff6ea7846c598812be580026dfc63fd7229db3) [commit](https://github.com/facebook/zstd/commit/04a2a0219ca424595949d725fda5da5cf764b419)

- Accelerate external sequence conversion: provide AVX2 path to convert ZSTD_Sequence to internal sequence format, and use scalar/AVX2 paths to summarize block size and literals length. [commit](https://github.com/facebook/zstd/commit/886720442f712b6e94c13075edaec1f224c1ae1a) [commit](https://github.com/facebook/zstd/commit/b6a4d5a8ba29bc873c95098103f57f987cfacd23) [commit](https://github.com/facebook/zstd/commit/ed0a8b8be173fdd8fc0a05b60c1571d13c14b0a3) [commit](https://github.com/facebook/zstd/commit/6f8e6f3c97c8e95527a29c4667edca6b793f798f) [commit](https://github.com/facebook/zstd/commit/33747e256937340b07b14e9155cf317b47f7fdc9) [commit](https://github.com/facebook/zstd/commit/d1f0e5fb9738073150e7e5c25b03444b5a6a5389) [commit](https://github.com/facebook/zstd/commit/8d621645891a8ec8a114fe09e94f967f2049352b) [commit](https://github.com/facebook/zstd/commit/bfc58f5ba24a3c27edfbc61288e09d2837235456) [commit](https://github.com/facebook/zstd/commit/8eb2587432d70359f26ff98fd12db7e8c9be7515) [commit](https://github.com/facebook/zstd/commit/cd53924eff684146b67e890d7b48158c37eca32c) [commit](https://github.com/facebook/zstd/commit/db3d48823a75a12a5ad9221e5a39191ff0044d3a) [commit](https://github.com/facebook/zstd/commit/4aaf9cefe9bdda1fafb5f6a5ba13294d2b478bd7) [commit](https://github.com/facebook/zstd/commit/57a45541927180724712b651ed1fb3e125105f30) [commit](https://github.com/facebook/zstd/commit/aa2cdf964f93d96113c09028ad7354ca2debc849) [commit](https://github.com/facebook/zstd/commit/e3181cfd325db59dbdeadcaf91b8187f49c5546c) [commit](https://github.com/facebook/zstd/commit/debe3d20d9ea0aaa45fbb692302347d0ece9f2c0) [commit](https://github.com/facebook/zstd/commit/2f3ee8b5309958a2bc1fc7477e703fd8195a31ea) [commit](https://github.com/facebook/zstd/commit/8bff69af869fca1cc44172c2ae5d5f995322509b) [commit](https://github.com/facebook/zstd/commit/87f0a4fbe0a1ffcaab4618f2aa76545e225acf07) [commit](https://github.com/facebook/zstd/commit/9efb09749b85acfbc2299fb6dec6146b942c6b2e) [commit](https://github.com/facebook/zstd/commit/35edbc20dc31fcc64f7dfe0c256d5005879b1b59) [commit](https://github.com/facebook/zstd/commit/f0b5f65bca6587f6d9b642e3a95d58ae36b7cdea) [commit](https://github.com/facebook/zstd/commit/a0872a837294ae9b18967e9e80342587f3089fb0) [commit](https://github.com/facebook/zstd/commit/55c0c5bdcaf9d00803be396d63adef2b61d1cf47) [commit](https://github.com/facebook/zstd/commit/6c1d1cc600f0cc5dab40e16200f4d23eeaeb0c9f) [commit](https://github.com/facebook/zstd/commit/6e1d02f1f04f9c255108f84cc788b709e7871c2e) [commit](https://github.com/facebook/zstd/commit/bcf404c0ab73cb6cc822a1412b78ba7965f9d74d) [commit](https://github.com/facebook/zstd/commit/54e9d46db44c4832d031100800f54a397358f896) [commit](https://github.com/facebook/zstd/commit/8156a19caceec6e06e037c197ff6dc4aa3b9617f) [commit](https://github.com/facebook/zstd/commit/32dff04d320c2dc667380076dff5d575fcf73207) [commit](https://github.com/facebook/zstd/commit/c39424ea87288aec400305c3bc3cf1ec6ef7d803) [commit](https://github.com/facebook/zstd/commit/e117d79e22ae98be24d1867b0f2b8730e952c835)

- Long-distance matching (LDM) default hashRateLog, hashLog, minimum match length, and bucket size now adjust dynamically with compression strategy; when hashLog is explicitly set, hashRateLog is derived accordingly. [commit](https://github.com/facebook/zstd/commit/4609a40b89b94cc61cc6a6a833725d6f89bf9de6) [commit](https://github.com/facebook/zstd/commit/f26cc54f37c614d3351b6873f0ee6e3fff00f6f6) [commit](https://github.com/facebook/zstd/commit/72406b71c30efbfe865611a79f50117254820c40) [commit](https://github.com/facebook/zstd/commit/d5e4698267b970545c349b3ed30a9168bcd165c3) [commit](https://github.com/facebook/zstd/commit/09d7e34ed8c138e913d8c11724f2d5fb5a1436bd) [commit](https://github.com/facebook/zstd/commit/67fad95f7971b97085fb838e3aa47cd37e9d7908) [commit](https://github.com/facebook/zstd/commit/d84d70bd04076970407246ac1cb4a8f04f61e248) [commit](https://github.com/facebook/zstd/commit/bf218c142aade4aa842205e93bc8260dcbfb372d) [commit](https://github.com/facebook/zstd/commit/7c5b6002c9c40936fbfd13bd6e7737b059f16d4a) [commit](https://github.com/facebook/zstd/commit/339bca66066e4a099bc91d04265c9bfbf15001bb) [commit](https://github.com/facebook/zstd/commit/d2c562b803a4c49dbd5afb1717db095aae1557b1)

### Linux Kernel Integration Module

- Linux kernel integration module exposes compression/decompression context size estimation helper functions for callers to allocate static work areas. [commit](https://github.com/facebook/zstd/commit/3242ac598e6f17d8008f6110337a3b4c1205842b)

### Parallel Compression Module

- CLI compression and benchmark default to automatic thread count max(1, min(4, CPU cores/4)); adjustable via ZSTD_NBTHREADS, verbose mode reports the thread count used for benchmarking. [commit](https://github.com/facebook/zstd/commit/17beeb5d1a978cb7775d37ee5f2b184368262ef5)

### Cross-cutting / Other Architecture-related Changes

- Fix CPUID build condition judgment on Windows x86 under Clang 16 and above. [commit](https://github.com/facebook/zstd/commit/72c16b187d27016b7634f5c6b7290e7c66ba44b3)

- Extend IAR compiler support, supplement bit operation builtins and related attribute/memory interface compatibility handling. [commit](https://github.com/facebook/zstd/commit/2955d92ac02eb60b6d0d00e7c6cd3f013ac020e6) [commit](https://github.com/facebook/zstd/commit/5fadd8e6b1229e3116ba53a8cd34b678df403d97)

- Enable zstd trace weak symbol support on RISC-V. [commit](https://github.com/facebook/zstd/commit/6dbd49bcd04c42b0b4893d824b856563ae901b33)

### Dictionary Builder Module

- Make COVER dictionary training no longer depend on mutable global state, avoiding interference between concurrent/repeated calls. [commit](https://github.com/facebook/zstd/commit/345bcb5ff7001fbe2dfd59974808170c9e0f4d5d)


## Routine Changelog

### New Features

- Extend CLI benchmark usage to allow running benchmarks in dictionary mode, and supplement manual instructions. [commit](https://github.com/facebook/zstd/commit/039f404faa9230e389b360c80d6c842fae3f75a0)

- CLI adds --max, setting maximum compression parameters and enabling ultra-high compression and long-distance matching; this option is resource-intensive, 32-bit mode is unavailable. [commit](https://github.com/facebook/zstd/commit/630b47a158cc22002045494c7e0dc0f0672c2fca) [commit](https://github.com/facebook/zstd/commit/8ae1330708b42c7f5751e94e02970e7ccb5d9731) [commit](https://github.com/facebook/zstd/commit/41b719375778ca92978f406b44bdea06cffbf108) [commit](https://github.com/facebook/zstd/commit/39d1d82fa80bfbec6d894ccf8bf18137cedad5d6) [commit](https://github.com/facebook/zstd/commit/f86024ccd2b2fc4608be336594e073096405ac13) [commit](https://github.com/facebook/zstd/commit/468e1453a55d119c914843bff73af809cbe4ba79) [commit](https://github.com/facebook/zstd/commit/1603cbe83ef7140f0cd0412bea50e5bfc9dd6d1c) [commit](https://github.com/facebook/zstd/commit/e3a9351402da08227d8531255b034bbe64fbd965)

- CLI automatically enables --ultra when using --long or --patch-from. [commit](https://github.com/facebook/zstd/commit/aebffd66ec43a721b9d07e67e18f353bf2082430) [commit](https://github.com/facebook/zstd/commit/5b8575adaac7a937ed71d5fd0200e29be81ca548)

### Bug Fixes

- Decompression error messages retain and display the full source file name, no longer truncating long paths. [commit](https://github.com/facebook/zstd/commit/a2f145f059150744132639cf30a918ceadac9b77)

- Fix resource cleanup on allocation failure in large dictionary tests, and fully zero-initialize zlibWrapper minigzip output buffer. [commit](https://github.com/facebook/zstd/commit/1d5e9705db5933f5d89dc53d9312d6db5d3c423c) [commit](https://github.com/facebook/zstd/commit/b4ecf724b15f0ab21a996339112680d3f4ba33eb) [commit](https://github.com/facebook/zstd/commit/0b24fc0a113c92c5ba5ec78f7169a2ddfe0d700f)

- When legacy v0.6 decompression context creation fails at the underlying allocation, it releases allocated objects and returns a null pointer. [commit](https://github.com/facebook/zstd/commit/1872688e0adb630e8710cb3d17846ca49f596e46)

- Dictionary builder appends a newline at the end of the prompt when encountering sample files larger than 128 KB. [commit](https://github.com/facebook/zstd/commit/4c6a519fdd8caef500244b838beab7f7a160f70f)

- When the initial state of the Huffman weight table is truncated, the decoder now reports corrupted data and adds error samples. [commit](https://github.com/facebook/zstd/commit/0938308ff69b3a7679898d75403832bafe43ba89)

- Fix benchmark formatting function to fully display numbers exceeding two digits. [commit](https://github.com/facebook/zstd/commit/89451cafbd92a350b4a924d0020efbc775054378)

- Fix memory leak caused by ZSTD_generateSequence() not releasing resources when returning early. [commit](https://github.com/facebook/zstd/commit/a40bad8ec06aeb992e8d8e58648a4024261b2a54)

- Fix benchzstd file resource not calling fclose(). [commit](https://github.com/facebook/zstd/commit/8edd1476862222c4f0e88511241b83ab0e1948c4)

- Fix QNX build compatibility, adjust the location of headers required for FILE declaration. [commit](https://github.com/facebook/zstd/commit/b3035b36c631614e32707cce0ab04c72c79c49a7)

- Fix numeric truncation when CLI prints file sizes larger than 4 GB. [commit](https://github.com/facebook/zstd/commit/194062a4e73fef16e29e9175426fe1a3b9b23a73)

- Fix null pointer crash in seekable decompressor when seek table has not been created yet. [commit](https://github.com/facebook/zstd/commit/b683c0dbe278f71e371376847deebd44fdcf392f)

- Fix issue where 32-bit Clang/MSVC targets were mistakenly restricted by 64-bit Clang version and unable to use CPUID path. [commit](https://github.com/facebook/zstd/commit/5e0a83ec255a0f4bb6a3cf8c4abcae46bfc2c3c5)

- Fix optimal parser possibly generating match sequences shorter than minMatch when merging long-distance matches. [commit](https://github.com/facebook/zstd/commit/1548bfc3497f45399daab58bcec4ab06a0878af1)

- Fix pzstd not ending queue and stream on compression/decompression errors, potentially causing hangs. [commit](https://github.com/facebook/zstd/commit/80af41e08a630946a75a5cda9e4cdf192247f20a)

- Fix architecture macro judgment in MSVC x64 bitstream path to avoid mistakenly using 32-bit specific branch. [commit](https://github.com/facebook/zstd/commit/42d704ad5e286fe8ad8b8aca0af4c78543abd3f1) [commit](https://github.com/facebook/zstd/commit/92d1a7d07cabf9ccef89caa6c38e8f7fed9ae05a)

- External sequence input now returns validation errors when missing block separators or when sequence array reaches the end, avoiding out-of-bounds reads. [commit](https://github.com/facebook/zstd/commit/e490be895cda9d1d6f707eaa86f8a72995960053) [commit](https://github.com/facebook/zstd/commit/afff3d2cce1ad2e81b16459de5b572131949c44f) [commit](https://github.com/facebook/zstd/commit/19025f3da0f34a99e0eafe9bc2bf304f3b4036cd)

- Improve 32-bit x86 BMI2 bitstream handling and detection: static path selects _bzhi_u32/_bzhi_u64 based on bit container width, BMI2 detection and dynamic dispatch also cover 32-bit targets, and add corresponding compile checks. [commit](https://github.com/facebook/zstd/commit/ee17f4c6d295e82733673f824e7dba81a33e245b) [commit](https://github.com/facebook/zstd/commit/936927a427704ca21dfd07c666c4123737c8fb03) [commit](https://github.com/facebook/zstd/commit/26e5fb36149b9d155a3640ca0800199fc13711e8) [commit](https://github.com/facebook/zstd/commit/462484d5dcbab964474bf4704df4d188e5c31818) [commit](https://github.com/facebook/zstd/commit/fcd684b9b45917dbb90e8122faf782e4028fdb42) [commit](https://github.com/facebook/zstd/commit/a469e7c0832825a1f5b992ca9b000266f051bb78) [commit](https://github.com/facebook/zstd/commit/9efb09749b85acfbc2299fb6dec6146b942c6b2e) [commit](https://github.com/facebook/zstd/commit/050109589800be49d3840927b9e821d24622e1ea) [commit](https://github.com/facebook/zstd/commit/d2d74616c0bfaf9d76186398a23fffafbb591c52) [commit](https://github.com/facebook/zstd/commit/a556559841db607ede4e4e0a85773e5b214e66f1) [commit](https://github.com/facebook/zstd/commit/4bbf4a285d92e4cb5b37e0fd1d4af96c12c2c249) [commit](https://github.com/facebook/zstd/commit/82346b92bb5f02dea90907135f74cd77f0c9cb33) [commit](https://github.com/facebook/zstd/commit/48b186f76bb740d01b9d1bb63108bc215e04ea62) [commit](https://github.com/facebook/zstd/commit/6c1d1cc600f0cc5dab40e16200f4d23eeaeb0c9f) [commit](https://github.com/facebook/zstd/commit/12046261382422494d7423cd39df553f236270ee) [commit](https://github.com/facebook/zstd/commit/ea0aa030cdf31f7897c5bfc153f0d36e92768095) [commit](https://github.com/facebook/zstd/commit/1b15e888fc1a2f5f84583b0df014c6032eb3a162) [commit](https://github.com/facebook/zstd/commit/d486ccc9e90a9d2e0095f9a81cbf29f72bac4f37) [commit](https://github.com/facebook/zstd/commit/0a183620a3c21bce4ca3b10a12aba7d7f84c12b2) [commit](https://github.com/facebook/zstd/commit/283fbd2dca79a7ed681da5c4aa03d329686ed9ff) [commit](https://github.com/facebook/zstd/commit/086ddcd9bad48fae611ae9a93387d8170eca4c65) [commit](https://github.com/facebook/zstd/commit/f7e8fc339b1ce64bbbfe3dc149b8cc0a13644844) [commit](https://github.com/facebook/zstd/commit/0cda0100ea4b9d87eeaaf68e7d192fbbff4f2ab2) [commit](https://github.com/facebook/zstd/commit/26a2b5d5dfae463beab4374cd5cb70706ec3ed6c)

### Tests

- Fuzz builds no longer enable -Werror by default; can be explicitly enabled when strict warning checks are needed. [commit](https://github.com/facebook/zstd/commit/81a5e5d4384342c0312198f4db35b8cdabc30d96)

- Rename bigdict test program to largeDictionary and sync Makefile targets. [commit](https://github.com/facebook/zstd/commit/ff7a151f2e6c009b657d9f798c2d9962b0e3feb5)

- Add unit tests for external sequence producer with static CCtx and streaming compression. [commit](https://github.com/facebook/zstd/commit/be6a18200621dd21ce073b77fce7f57636a6f4f4)

- decodecorpus adds advanced options to configure decoding corpus test runs. [commit](https://github.com/facebook/zstd/commit/1f5df587fa3edbbf2faf24ef2f0941652663305f)

- Fix pointer offset handling in regression test result recording. [commit](https://github.com/facebook/zstd/commit/de6cc98e07e1770b9f4571ea25dd6bf61612c08f)

- Fix tests on GNU/Hurd for non-regular files to use portable /dev/zero input. [commit](https://github.com/facebook/zstd/commit/4a4786bef0b5b4b4fb190de6816b4d9df503a5d8)

- CI separately reports zlib wrapper normal tests and Valgrind tests; fix expected return status of zlib inflate test. [commit](https://github.com/facebook/zstd/commit/43626f1ce0ae4f7f3a9f6d5b7b04f54566d49b52) [commit](https://github.com/facebook/zstd/commit/0b96e6d42a9b22eb472a050fcd2cc4be3ffb8e2b) [commit](https://github.com/facebook/zstd/commit/72277079fbdb7bb95657c76c6ef6b87752c09708)

### Performance

- Benchmark level ranges load source data only once, and update benchmark manual for dictionary and synthetic input descriptions. [commit](https://github.com/facebook/zstd/commit/0079d515b1673a7deba3dfa46204a1af61d81dce) [commit](https://github.com/facebook/zstd/commit/f34bc9cee63759a85011db66e5cb9187c88ea843)

- fullbench default samples switch to Lorem Ipsum, and add compressSequences and compressSequencesAndLiterals benchmark scenarios. [commit](https://github.com/facebook/zstd/commit/8ab04097ed9736923405e4928f928e49654e2c9a) [commit](https://github.com/facebook/zstd/commit/ac05ea89a5e87cf9e9756790f08b9d21b349fd9e) [commit](https://github.com/facebook/zstd/commit/f281497aef87a0e6459eef28f695c437a3dec42d) [commit](https://github.com/facebook/zstd/commit/95ad9e47ffa930d2facb5d2dd2de511bf8171e5d) [commit](https://github.com/facebook/zstd/commit/12c47d32624df633b9dd3402273529cff7705228)

- Automatic row matchfinder enable threshold no longer depends on SSE2/NEON availability, avoiding different architectures selecting this path at different window sizes. [commit](https://github.com/facebook/zstd/commit/d88651e6041995243c8cd6884bbc44c279ab80d2)

- Windows x64 builds can now enable Huffman decoding assembly implementation. [commit](https://github.com/facebook/zstd/commit/46e17b805b1bb2982583208da3b9184e377c2dd5) [commit](https://github.com/facebook/zstd/commit/d60c4d75e9d29d76cc202f7a8341ab0bda1d6402) [commit](https://github.com/facebook/zstd/commit/167b00495dff3b7970eeaff19aba71453e147c0b)

- Improve speed and memory usage of --patch-from in high compression and multithreading paths: limit large dictionary processing to indexable suffix, omit temporary CDict, and advance multithreaded jobs in smaller blocks to improve parallel smoothness. [commit](https://github.com/facebook/zstd/commit/ffa66a6971010057a5918ddc54531bec7bf18842) [commit](https://github.com/facebook/zstd/commit/34ba14437aeeb5e678ae7f1dbdfa6333beb2723b) [commit](https://github.com/facebook/zstd/commit/85a44b233accb544d89c85b804182e3f34e8d4b1) [commit](https://github.com/facebook/zstd/commit/220abe6da857142305ab7337b346c826856bcfd1) [commit](https://github.com/facebook/zstd/commit/7406d2b6eb91851db6a1cef10121de2a4c5a794a) [commit](https://github.com/facebook/zstd/commit/f11bd19c7f7899840585a260688e969eb705a008) [commit](https://github.com/facebook/zstd/commit/c7cd7dc04bede050475da32fa019c2d0712ed6cf) [commit](https://github.com/facebook/zstd/commit/23e5f80390db9a3a65485933d255e163d2dab519) [commit](https://github.com/facebook/zstd/commit/ef2bf5781112a4cd6b62ac1817f7842bbdc7ea8f)

### Security

- CMake and Meson add non-executable stack compile/link flags for GCC/Clang builds; CMake enables x86_64 assembly decoder only when flags are supported. [commit](https://github.com/facebook/zstd/commit/f0937b83d9a32cb2b59f99bbc4db717ae6e83c9b) [commit](https://github.com/facebook/zstd/commit/7b856e3028518109eb34019e215802cda7cbafc1) [commit](https://github.com/facebook/zstd/commit/0396480109627a819134f3ab5791f24af4768663)

- Harden GitHub Actions: restrict Android NDK workflow permissions, and pin Java, Android SDK, and MSVC environment actions to commit versions. [commit](https://github.com/facebook/zstd/commit/5c465fcabeea65e642aaf70d1059958acd6acd69) [commit](https://github.com/facebook/zstd/commit/b14d76d88810f2984e0cd9ebd307269843a5d7d9) [commit](https://github.com/facebook/zstd/commit/ea027ab21c25b15b99457152e50e9b3d9c1232fb)

### Documentation

- Update benchmark results for zstd v1.5.6 in README. [commit](https://github.com/facebook/zstd/commit/e0ee0fccf8c591465be4c3f4872ef550e7939f73)

- Fix zstd format documentation: remove statement that FSE cumulative probability overflow is considered corrupted, as this situation cannot be produced by variable-length encoding. [commit](https://github.com/facebook/zstd/commit/8cff66f2f53fa41b8f5be65996600d88fbbe1a98)

- Update ZSTD_decompressStream() documentation to clarify that when output buffer is full, there may still be frame data pending output and how to determine completion. [commit](https://github.com/facebook/zstd/commit/a86f5f3f33f40945c0d1341827fabc6a22338499)

- Supplement explanation of ZSTD_decompress() behavior of processing multiple consecutive compressed frames in one call and return content. [commit](https://github.com/facebook/zstd/commit/2acf90431ab2ffdc7d85d1017cf344bac897e704)

- Fix spelling errors in manuals, headers, comments, and test code detected by codespell. [commit](https://github.com/facebook/zstd/commit/2d736d9c50057e6d1f33c175e126590816c54251) [commit](https://github.com/facebook/zstd/commit/44e83e9180ee326353f98e680a7769d4b76f4c25)

- README adds instructions for using zstd via Conan. [commit](https://github.com/facebook/zstd/commit/0986e1e630c0a4286ea07516bde3e6571c22274d)

- Clarify when --patch-from needs to be used with --single-thread. [commit](https://github.com/facebook/zstd/commit/b320d096a44b592d5f5bcda37e323b799c0cef57)

- Fix API documentation for ZDICT_DICTSIZE_MIN. [commit](https://github.com/facebook/zstd/commit/7a48dc230c42ba4d779fab4e68da14f44c92a7b3)

- Clarify that decoders may reject non-zero probabilities for offset codes beyond implementation support range. [commit](https://github.com/facebook/zstd/commit/c54f4783d0cd51d8aad1c0a4fd9fe564d461aae4)

- Rewrite FSE decoding table construction process description, clarifying the meaning of the three items in state table rows and decoding direction. [commit](https://github.com/facebook/zstd/commit/a8b86d024a2e5ca7029ab19f7638cd6ca42bde1a)

- Reorganize the Huffman prefix code specification description, and add symbol sorting examples. [commit](https://github.com/facebook/zstd/commit/3b343dcfb140ccb278a781faa8116d273f36e4a1) [commit](https://github.com/facebook/zstd/commit/3e7c66acd1b6dab2473a996adac027dacf648d0a)

- The generated HTML manual will indicate that its content is automatically generated from zstd.h. [commit](https://github.com/facebook/zstd/commit/2e02cd330dee3fcf9a8609b90ed7b965e0a6f9a1)

- Correct the input size boundary condition in the ZSTD_compressBound() documentation. [commit](https://github.com/facebook/zstd/commit/10beb7cb53ba328722d82c271d7b450b97869c92)

### Build / CI

- The Windows build script now uses vswhere to locate MSBuild, supports Visual Studio 2022, and adds an option to select the latest installed instance. [commit](https://github.com/facebook/zstd/commit/65ab6c267e74eb715f383763d8b9898c780ed5ab) [commit](https://github.com/facebook/zstd/commit/9c442d6fc28e55e5379598d18082f8a31dd4931b)

- Upgrade CodeQL GitHub Action to 3.24.9. [commit](https://github.com/facebook/zstd/commit/101e601c793e9d4dbdffaf05331774bca2aa12be)

- FreeBSD platform detection no longer uses the gmd5sum alias, and instead uses the system default MD5 tool. [commit](https://github.com/facebook/zstd/commit/103a85e6f64f305684db354a0eb9a10d5c586d5c)

- Update the MSYS2 action used in the Windows artifacts workflow to eliminate Node.js deprecation warnings. [commit](https://github.com/facebook/zstd/commit/ebf24b7b77ed3b4430e7dd3ef45104d05d3585a6)

- Fix the input length type in the zlibWrapper write path, restoring zlibWrapper build compatibility. [commit](https://github.com/facebook/zstd/commit/71def598906637866f1b165bc9113defdd36983c)

- Upgrade CodeQL GitHub Action to 3.24.10. [commit](https://github.com/facebook/zstd/commit/7968c661af8ec976782ddcfde3ea609d9353a0cf)

- Provide a separate pkg-config file for the multithreaded static library, along with corresponding private link parameter configuration, and add usage instructions. [commit](https://github.com/facebook/zstd/commit/f1f1ae369a4cefd3474b3528e8d1847b18750605)

- Add the zstd library header search path for the Windows resource compiler. [commit](https://github.com/facebook/zstd/commit/fd5f8106a58601a963ee816e6a57aa7c61fafc53)

- Fix the Meson configuration that should not add -pthread when statically linking on Windows, and add MinGW cross-compilation CI. [commit](https://github.com/facebook/zstd/commit/5be2a8721d527ae349539b459b35fb628467e00d)

- Fix multiple instances of empty brace initialization that do not conform to ISO C. [commit](https://github.com/facebook/zstd/commit/4f41631aa4fffffac511d484ad10d603650e0156) [commit](https://github.com/facebook/zstd/commit/01cea2e1e2cf1cafa4b61e1bc8eb85618cf18c76)

- Upgrade CodeQL GitHub Action to 3.25.1. [commit](https://github.com/facebook/zstd/commit/68a6d9b9f6ce605010ea1164590e4e015567dee7)

- Make the default memory allocator declaration in zstd.h compatible with Clang's -Wzero-as-null-pointer-constant diagnostic and different compiler versions. [commit](https://github.com/facebook/zstd/commit/d7cb47036cb78b3681aee4725107381a1b69abfc) [commit](https://github.com/facebook/zstd/commit/97291fc5020a8994019ab76cf0cda83a9824374c)

- Upgrade the msys2/setup-msys2 action to 2.23.0. [commit](https://github.com/facebook/zstd/commit/4356192cb2a16975720a04ac5681a495e7ef1acc)

- Remove 13.2 image from FreeBSD CI. [commit](https://github.com/facebook/zstd/commit/949689facf96c4bce6953d07f0658412077bcbf1)

- Fix the Makefile platform filtering logic, and improve build and test support under MSYS/Cygwin. [commit](https://github.com/facebook/zstd/commit/f19c98228f773413850736b3aab574a63f03f2bc)

- Add Cygwin installation tests to verify the make install process. [commit](https://github.com/facebook/zstd/commit/d7a84a683fe345342139660b9d3a36328ed5f4b3)

- Fix link parameters and CI configuration in the macOS build script. [commit](https://github.com/facebook/zstd/commit/80170f6aad9f48574b108584e7504b0f9254958f)

- Upgrade OSSF Scorecard GitHub Action to 2.4.0. [commit](https://github.com/facebook/zstd/commit/efbb5ef01596880cfd87d09a35c7599504ee3bce)

- Fix the Makefile build of the gen_html tool on Windows. [commit](https://github.com/facebook/zstd/commit/1f72f52bc1efd943f390a3dec3b569cf49f7a83a)

- Upgrade the msys2/setup-msys2 action to 2.24.0. [commit](https://github.com/facebook/zstd/commit/46a3135524b1ea9cd46ea5cd61529f1231606465)

- Fix build compatibility of the zstd dictionary training code with Android NDK r27. [commit](https://github.com/facebook/zstd/commit/c3c28c4d5a28bca93c97c4ce447f3c8ece42791d)

- Upgrade the msys2/setup-msys2 action to 2.24.1. [commit](https://github.com/facebook/zstd/commit/688a815c8643c8ea2475ac90bdd261bbcc43631b)

- Add an Android NDK build workflow, and adjust workspace alignment code to pass builds on that platform. [commit](https://github.com/facebook/zstd/commit/cb784edf5de07940c0f48bae6cf8c4b2f4993705)

- Fix comment style in benchzstd to be compatible with C90. [commit](https://github.com/facebook/zstd/commit/14b8d398fd0f9155203031239748537e7df2ad75)

- Upgrade actions/setup-java in the Android NDK workflow to v4. [commit](https://github.com/facebook/zstd/commit/aed3c7540a904b2dbb12fd88038bd09d743ca05d)

- Upgrade CodeQL GitHub Action to 3.26.2. [commit](https://github.com/facebook/zstd/commit/ec0c41414d5d41e6e49b5bd7402a7252ad91e7e7)

- Fix the runtime error of the zstd-pgo target in programs/Makefile. [commit](https://github.com/facebook/zstd/commit/bf4a43fcd45aea991d273160262a31925ea31ba3)

- Fix warning handling in pzstd under the combination of -Wunused-result and C++17 compilation options. [commit](https://github.com/facebook/zstd/commit/a8b544d460f3db9a79d630d95f1fa3564c29be12) [commit](https://github.com/facebook/zstd/commit/9215de52c7029bdad06d5fa59a4777edf0c92df9)

- Update the FreeBSD CI virtual machine image to 14.1. [commit](https://github.com/facebook/zstd/commit/a3b5c4521c954af9b2a2bf2b1df9a4bb70f0c46d)

- Remove the no longer used CircleCI nightly test configuration and container images. [commit](https://github.com/facebook/zstd/commit/3d5d3f5630acdb14ddd94721b2011dca8eaf496a)

- Meson restricts private header files to internal dependencies, and fixes dependency/include configuration for contrib and test targets. [commit](https://github.com/facebook/zstd/commit/d2d49a11618bd3958b0501942b3525d9431008c1) [commit](https://github.com/facebook/zstd/commit/ccc02a9a7786c7556d31cfd3d7b08ba8d6895eea)

- Fix the trigger conditions and dependency installation steps for nightly GitHub Actions. [commit](https://github.com/facebook/zstd/commit/b84653fc839367281481bc3fee9f9d7e8496701f)

- Adjust the 32-bit CI test configuration to attempt to shorten test duration. [commit](https://github.com/facebook/zstd/commit/1024aa9252ff02ebc03511a2c0311957511d0be9) [commit](https://github.com/facebook/zstd/commit/6f2e29a234c9f9ca63f1dd2748933a03f03ac731) [commit](https://github.com/facebook/zstd/commit/e6740355e35fa5695cb606e7bbda41b595175b3a)

- Enable regression tests in the pull request workflow. [commit](https://github.com/facebook/zstd/commit/ff8e98bebee144321d7c39234deff43f9211dfbc)

- Update the CodeQL action in GitHub Actions to v3.27.1. [commit](https://github.com/facebook/zstd/commit/2d1bbc37ebf4cbf48a2f107a3816f3e137fb5d49)

- Fix the issue where the macOS universal binary build overwrites existing CFLAGS. [commit](https://github.com/facebook/zstd/commit/d0fe334c8552edb764b853854037697c6710fa64)

- Update the MSYS2 setup action in Windows CI to v2.25.0. [commit](https://github.com/facebook/zstd/commit/a9d279c97c76f3d5018f96fd4f65b28cb501e3ad)

- Update the MSYS2 setup action in Windows CI to v2.26.0. [commit](https://github.com/facebook/zstd/commit/c254ea097b017cac8f9b33856370afb729048035)

- Raise the minimum required CMake version to 3.10. [commit](https://github.com/facebook/zstd/commit/e190e7944e42309a60b31c9d025c877219e7f878)

- ThreadSanitizer and MemorySanitizer CI jobs no longer pin to Ubuntu 20.04. [commit](https://github.com/facebook/zstd/commit/7236e05b0a4f5e9c9435661fe7b2bfedeba29ec4)

- Add the UNAME_TARGET_SYSTEM override value in lib/Makefile to select shared library extension and link parameters based on the target system; when not set, UNAME is still used. [commit](https://github.com/facebook/zstd/commit/d06e8778bc4b150507abe0a8b7eaed08f2d16a17)

- Add a fallback path for old Android/Bionic libc lacking fseeko()/ftello(), using fseek()/ftell() instead. [commit](https://github.com/facebook/zstd/commit/54c3d998a04a4002697a3a44293074cb01df54a5)

- Change the FreeBSD manual page installation directory to use the default man1dir layout. [commit](https://github.com/facebook/zstd/commit/0fd521048d9304e2e06020bebcfb0b481261b2fc)

- Fix multiple CI build checks: restore the Clang PGO environment, install the liblzma dependency, and update lib64gcc needed for PowerPC cross-compilation. [commit](https://github.com/facebook/zstd/commit/908a95889b2bbcdb30e945ac12e0b6b2e025fa4d) [commit](https://github.com/facebook/zstd/commit/0e819c9f933a6b1193cfa26453ba967eb198af13) [commit](https://github.com/facebook/zstd/commit/196e76efe16623c4a1aa5d636298b59f392671b5) [commit](https://github.com/facebook/zstd/commit/80ff61de1de352fb14d4bee6de7f7dd1e254da38) [commit](https://github.com/facebook/zstd/commit/d4ae5c3752c0f4a918cadcfb9489c91e59bb1f47) [commit](https://github.com/facebook/zstd/commit/72277079fbdb7bb95657c76c6ef6b87752c09708)

- CI splits short tests into named steps, reports success upon completion, and uses make check; Windows CI enables warning-as-error checks and fixes corresponding warnings. [commit](https://github.com/facebook/zstd/commit/642157cc450c5e2b1c5703ba0a164514ce29061a) [commit](https://github.com/facebook/zstd/commit/78275149ead3bfc068d58a67480653740da5a86b) [commit](https://github.com/facebook/zstd/commit/4f3311f245fedb99d65baca98cd33f6ec41a6589) [commit](https://github.com/facebook/zstd/commit/053e4bef2083e5b047d8b2a7670f445640ca9082) [commit](https://github.com/facebook/zstd/commit/30e0f29c4dbfac9f4df56310d70d4d904587e2f5) [commit](https://github.com/facebook/zstd/commit/f9c1850aa2df6024e930b257067401108fa268ef) [commit](https://github.com/facebook/zstd/commit/590c22454e24c0247f60a5fd939a1c4f1d49e896) [commit](https://github.com/facebook/zstd/commit/e87d15938c888011cdcc7aa6d45a85ea055a5da8) [commit](https://github.com/facebook/zstd/commit/294925292304b3c5b5e975f9036a684881dba469)

- Add a Visual Studio Preview build script that supports preview MSBuild/VS toolset and builds Win32 and x64. [commit](https://github.com/facebook/zstd/commit/7d63a1c7c3ceb5befd0839e8c50b91c3289019ce)

- CMake adds the Apple Framework build option ZSTD_FRAMEWORK, which can generate a zstd framework for Apple platforms; the minimum CMake version remains 3.10. [commit](https://github.com/facebook/zstd/commit/897cec38760d1bb41e690225ba07b91c568e7cc8) [commit](https://github.com/facebook/zstd/commit/03d5ad6fed5882a300289e5fa8a238f2fec29300) [commit](https://github.com/facebook/zstd/commit/becef672bb7c22af0fd723a4f8e4d279cf2a780a) [commit](https://github.com/facebook/zstd/commit/45c0e72c0a481be824cc12fe6032ac685205d187)

- Fix the resource compiler include parameter handling in CMake when the source path contains spaces, and add cross-platform override tests. [commit](https://github.com/facebook/zstd/commit/6cd4204ee30c9d3a1ae00ca4082bf4b5c7e3dd7d) [commit](https://github.com/facebook/zstd/commit/be1bf2469e44952efb318f80b781e82e8e9e5183) [commit](https://github.com/facebook/zstd/commit/6a65a43032e84eccccdf2d5aa3c2dfba20d5c95b)

- Update the Cygwin installation action in CI to v5, and the CodeQL action to v3.28.9. [commit](https://github.com/facebook/zstd/commit/e39ed414350313e8170d96c8fc82b3d0c2e67a6a) [commit](https://github.com/facebook/zstd/commit/056492e31b80fa746c187a5078e96163437c8739) [commit](https://github.com/facebook/zstd/commit/cf01bbf0053db99bf06aaf91f25b7b55b03cfddd) [commit](https://github.com/facebook/zstd/commit/5b9c5d4929cea7b3a134f44887bfffeefd448500) [commit](https://github.com/facebook/zstd/commit/f7c7553e4fc6f83834d5322196efdfb4878576ea) [commit](https://github.com/facebook/zstd/commit/7a2fce5a1fabcd28cc8c8ea5ef039dab32b24f0b) [commit](https://github.com/facebook/zstd/commit/071a4a09043e31496ea66113265609fa6aa6c650)

- CI updates to newer Ubuntu and FreeBSD environments, fixes ARM64 QEMU tests and speeds up execution, while removing x32 ABI checks and BTI tests not supported by the current environment. [commit](https://github.com/facebook/zstd/commit/815ca8c6784f59de825058b2b84bdb59b854feee) [commit](https://github.com/facebook/zstd/commit/fc1baf34637e7f230996cdc8ca259bf71809978a) [commit](https://github.com/facebook/zstd/commit/75bcae1272cbd6e417a9eb2c0e35e9f02828fba4) [commit](https://github.com/facebook/zstd/commit/2b7c661ad2c022a56f6d0c58cbafa6f3d637ad4f) [commit](https://github.com/facebook/zstd/commit/b73e06b83e0fc6f7f6999c2292b3250eb50b2084) [commit](https://github.com/facebook/zstd/commit/0b8119f0ad0b027faffb7955b835718e049399e6) [commit](https://github.com/facebook/zstd/commit/85c39b78cfabf64fe0d8859f3c4ac5f240d52fc8) [commit](https://github.com/facebook/zstd/commit/2a58b047529ca385867fea53b4077526bb10486e) [commit](https://github.com/facebook/zstd/commit/beccbc6f744f3fe4af57776a5c19bafd252f633a)

- CI adds make check for Intel oneAPI LLVM C compiler icx. [commit](https://github.com/facebook/zstd/commit/8df6155495548d5db02b494fd8be23fad8c6cdfc) [commit](https://github.com/facebook/zstd/commit/22c39b989102176e8db31cf85e2e353e4d74fdd6)

### Maintenance

- Fix the spelling of the LIB_BINDIR variable name in libzstd.mk. [commit](https://github.com/facebook/zstd/commit/5d63f186cce4bb21fde156492fe945f2ae69104c)

- Fix the scope of the C++ linkage guard in public headers, and clean up redundant extern "C" wrappers in internal headers, improving compatibility when C++ projects include headers. [commit](https://github.com/facebook/zstd/commit/fc726da7747b159520de2edb0febab30342d2744) [commit](https://github.com/facebook/zstd/commit/d0d5ce4c00469d4f11970e649e55217a659b4690) [commit](https://github.com/facebook/zstd/commit/c727d5cd675dc04e07c0113d168ce93dc5624e54) [commit](https://github.com/facebook/zstd/commit/10b9d81909f8631e3ac64bd45e3bdd04982e39d6) [commit](https://github.com/facebook/zstd/commit/a610550e2c05cd08842e173bbeb830f596fdfaeb) [commit](https://github.com/facebook/zstd/commit/c7af0428c6cceac32a192392d954dc8e6e1ba79a) [commit](https://github.com/facebook/zstd/commit/8f49db5a022f5f77ad2c9a468b5929855bb6f36b)

### Others

- The compression ratio column in benchmark output is now aligned by numeric digits. [commit](https://github.com/facebook/zstd/commit/60f84f73fed4cb94c166e1dadf3f96ec71a7792c)
