# Release Note

## Important Changes

### FIPS Provider
- Refactor the way FIPS options are generated, use macros and unified header files to keep naming consistent, and rename security detection functions to clarify their FIPS configuration attributes. (Architecture-related: public API)
  ↳ No PR: [f6a296c](https://github.com/openssl/openssl/commit/f6a296c3867f53cd005069292d512280835bcdae)
- Add FIPS indicator for CMAC, allow TDES to be enabled in FIPS mode via configuration or settable parameters, and refactor initialization functions to support parameter passing. (Architectural event: CMAC internal header file change)
  ↳ No PR: [4f5febe](https://github.com/openssl/openssl/commit/4f5febe2c684a803553171940634c1b6f4b7ba40)
- Disable the use of SHA1 in DH and ECDH key exchange, and rename the FIPS indicator function to ossl_fips_ind_digest_exch_check. (Architecture event: FIPS indicator change)
  ↳ No PR: [391f4a0](https://github.com/openssl/openssl/commit/391f4a04118bae01f4c1f72496b2b32aa31dfbbb)
- Add limit checks for digest algorithms and key lengths in FIPS mode for HKDF, SSHKDF, SSKDF, X963KDF, TLS1-PRF and TLS1.3 KDF. (Architecture-related: FIPS compliance)
  ↳ No PR: [6d47e81](https://github.com/openssl/openssl/commit/6d47e819f2101f0219ddee67e855701e7bc3a716), [1b83862](https://github.com/openssl/openssl/commit/1b838621c329dcbd32b29e65084d74efe431d060), [5e25b8a](https://github.com/openssl/openssl/commit/5e25b8afc0f964a3f178549d00fbe6a9295188e8)
- Added the no-short-mac option to the FIPS module and fipsinstall tool, which controls whether to perform runtime checks for short MAC output. This option is enabled by default. (Architecture-related: FIPS configuration options)
  ↳ No PR: [00231a6](https://github.com/openssl/openssl/commit/00231a6ae9dfe806bdc1107f2c5ae86015a2a9e0), [d791c2c](https://github.com/openssl/openssl/commit/d791c2c486aa7d14c7ac5e2da08e3a303bbc4f07), [98fbe67](https://github.com/openssl/openssl/commit/98fbe6792458f767617e4a96b09215427d61ee4b), [fc98a2f](https://github.com/openssl/openssl/commit/fc98a2f6ad8f8afe5f0e32d2ae66d09d39b1ff9d), [50a91de](https://github.com/openssl/openssl/commit/50a91de440f05e369f02e10c34aaf16fca4dbc62), [3762a56](https://github.com/openssl/openssl/commit/3762a56b872b4346cbfa23bfc10507e654094abb)
- Add explicit FIPS indicator support to PBKDF2 KDF, allowing configuration of lower bound checking behavior in FIPS mode, and disabling the use of XOF digests. (Architecture-related: FIPS compliance)
  ↳ No PR: [a7f8378](https://github.com/openssl/openssl/commit/a7f8378e8cbbc1cfadabd0e5bc9a2e85c740c943)
- Added signature digest checking support for the fipsinstall tool and FIPS provider, allowing configuration of signature digest checking options. (Architecture-related: public API)
  ↳ No PR: [c613f08](https://github.com/openssl/openssl/commit/c613f080ca482ebfcb94bb64eb9a567a77187ab8), [fc5c86b](https://github.com/openssl/openssl/commit/fc5c86b8c1f986c3692d275a38ed131e4fb67c36), [5d6e692](https://github.com/openssl/openssl/commit/5d6e692c36d6ecf1427c2a7c5fc37c501a251c03)
- Added eddsa_no_verify_digested option in fipsinstall tool and FIPS provider to disable Ed25519/Ed448 verification of pre-hashed data. (Architecture-related: public API)
  ↳ No PR: [70b6d57](https://github.com/openssl/openssl/commit/70b6d57fd94fe11fa2510bc8026fa6a6ead51d68), [889277e](https://github.com/openssl/openssl/commit/889277effb65b7f276e375cf0176c4c8597f4203), [b00ea9a](https://github.com/openssl/openssl/commit/b00ea9a6a2a72f5ac7b38e82c9a7b6796972fc36), [a6aa2d1](https://github.com/openssl/openssl/commit/a6aa2d1f031f9940969a479a3e6f9c04ad922ebb), [54933db](https://github.com/openssl/openssl/commit/54933db9f0e1a03b644cecc6735f8f2025b748b5)
- Added an option to disable RSA PKCS#1 v1.5 padding in the fipsinstall tool and FIPS module, which is turned off by default. (Architecture-related: public API)
  ↳ No PR: [dd43e8a](https://github.com/openssl/openssl/commit/dd43e8a9ec344182540cfb64ecb032c94ec6874e), [2c73d92](https://github.com/openssl/openssl/commit/2c73d92b203dec3dcded29aaf247b19efc15aafa), [08bd84b](https://github.com/openssl/openssl/commit/08bd84b2e424999ff617fb9ac687d30ea9b94647)
- Added KBKDF key check option in fipsinstall tool and FIPS module, allowing configuration of KBKDF key check. (Architecture-related: public API)
  ↳ No PR: [090247b](https://github.com/openssl/openssl/commit/090247b2e29a71f49c12a753ca9204c30d14a0f8), [6cb6b17](https://github.com/openssl/openssl/commit/6cb6b1717151c83a5046bef9ce46adeb60a3b22a), [8d52cf5](https://github.com/openssl/openssl/commit/8d52cf525b91668bb9eb7bac0331f455899fc7c2)
- Added FIPS indicator support for Triple-DES encryption, allowing default use of Triple-DES for decryption but disabling encryption in FIPS mode, and disabling CMAC using Triple-DES in FIPS mode. (Architecture-related: FIPS Compliance)
  ↳ No PR: [bc43158](https://github.com/openssl/openssl/commit/bc43158797a7f8bc36cb736524bf812db7d8635e)
- Added a new configurable item pbkdf2-lower-bound-check in the FIPS installation tool, which is enabled by default to match the default behavior of FIPS provider v3.0. (Architecture-related: build and installation methods)
  ↳ No PR: [aa3830c](https://github.com/openssl/openssl/commit/aa3830c3fc0f087d65a05fd0ea4fc03e26add002), [21bcae6](https://github.com/openssl/openssl/commit/21bcae6561d73e629f11e19975f24283559d36c0)
- Avoid using decryption-only passwords when obtaining 3DES passwords in FIPS mode, and add the decrypt_only parameter for detection. (Architecture-related: public API)
  ↳ No PR: [ed7a8bf](https://github.com/openssl/openssl/commit/ed7a8bfd7409ac4a516581f1711d98a9362a70d5)
- Add key length check for HMAC in the FIPS module, and introduce an internal schedule to enable KDF to bypass the check when using HMAC. (Architecture-related: public API)
  ↳ No PR: [390f00a](https://github.com/openssl/openssl/commit/390f00a1e95f241b4a104c323020c7bc90d5e829)
- Add key size compliance check for KMAC algorithm in FIPS mode and ensure relevant FIPS indication status is passed when copying context. (Architecture-related: public API)
  ↳ No PR: [ea396c7](https://github.com/openssl/openssl/commit/ea396c7024dec784c76e05d531db41f98788f1e9)
- Add key length check for KBKDF in FIPS mode, compliant with SP 800-131a revision 2. (Architecture-related: FIPS compliance)
  ↳ No PR: [ae87c48](https://github.com/openssl/openssl/commit/ae87c488956c84795fd35cb9cc8024d620cf06c6), [fd39d1c](https://github.com/openssl/openssl/commit/fd39d1c80cd5bd9cb5c64e3fc96102397e5e860f), [3416c0b](https://github.com/openssl/openssl/commit/3416c0bff9749fc3a4e654ce9919e318663e165d)
- Added a new FIPS indicator in ECDH cofactor mode to ensure that non-1 cofactor curves are correctly multiplied by the private key during key derivation, and added FIPS compliance checks. (Architecture-related: FIPS compliance)
  ↳ No PR: [05681e0](https://github.com/openssl/openssl/commit/05681e0e3e47e0abc5ec3a4c12ddb0afcd66db37), [81f438d](https://github.com/openssl/openssl/commit/81f438d4f654143766f54ec865aab36bc61355cf)
- Added FIPS validation message parameter support for ECDSA signature verification context. (Architecture-related: FIPS Compliance)
  ↳ No PR: [b80e2dd](https://github.com/openssl/openssl/commit/b80e2ddb66ad1bb5e14bea62d72127b0732b19f3), [fe1ce91](https://github.com/openssl/openssl/commit/fe1ce91f7feb4a6be7ba1616dad442d5d7796b96)
- Added FIPS indicator support for X25519 and X448 key generation and key exchange operations, and added a parameter interface to obtain FIPS approval status. (Architecture-related: public API)
  ↳ No PR: [c37e217](https://github.com/openssl/openssl/commit/c37e21763b1d460b06a4f94baf6682f96000810f)
- Add public key verification function for ED25519 and ED448, support checking whether the public key is a valid point on the curve through EVP_PKEY_public_check() in FIPS mode. (Architecture-related: public API)
  ↳ No PR: [bb1aab3](https://github.com/openssl/openssl/commit/bb1aab38a6a3751bf61319c2aa40a6ffd4ea910c)
- Implemented key length checking for X9.42 KDF, requiring the input key to be at least 112 bits, and added corresponding FIPS configuration options. (Architecture-related: FIPS configuration)
  ↳ No PR: [12d0f07](https://github.com/openssl/openssl/commit/12d0f0789a3f518581ecada4f3fba899c0b387db)
- Removed X25519 and X448 curves from FIPS approval, modified FIPS provider attribute to unapproved and excluded from capability advertising. (Architecture-related: FIPS Compliance)
  ↳ No PR: [52ca560](https://github.com/openssl/openssl/commit/52ca56090cb651ffa8ef9b5cd155742ee35117d1), [fccd161](https://github.com/openssl/openssl/commit/fccd1615eea5f81f2a12b2fb953e6606edbc59c8)
- In FIPS mode, RSA-OAEP padding and verification functions now prevent the use of XOF digest algorithms such as SHAKE, and corresponding test cases have been added. (Architecture-related: external behavior)
  ↳ No PR: [1bfc8d1](https://github.com/openssl/openssl/commit/1bfc8d17f349fbe1c849bf362b24ca0af4a8977d), [973ddaa](https://github.com/openssl/openssl/commit/973ddaa03f39ef6d3c890918afbeb0ea9cbe8b07), [0285160](https://github.com/openssl/openssl/commit/0285160ffa3b8c2b5491222243042593808298c4)
- Explicitly call OPENSSL_cpuid_setup when initializing the FIPS provider to ensure that the capability vector is set correctly. (Architecture-related: platform compatibility)
  ↳ No PR: [a192b24](https://github.com/openssl/openssl/commit/a192b2439c0207ce1b04ba6137329b68f9e23680)
- Fixed the initialization of the FIPS indicator structure, changed the field type to a smaller integer type, and replaced memset with circular assignment to make the initialization more robust. (Architecture-related: public API: FIPS indicator structure)
  ↳ No PR: [98afa01](https://github.com/openssl/openssl/commit/98afa01f3e02fba18f9203b2451113df8f247f7c)
- Added restrictions for X9.31 padding in FIPS provider: disables use of this padding for RSA signing (only allows verification), and forces RSA modulus size to be a multiple of 1024 + 256*s. (Architecture-related: FIPS compliance)
  ↳ No PR: [07e4d7f](https://github.com/openssl/openssl/commit/07e4d7f4747005e3ce56423182ad047eb05d8e16)
- Disabled the use of pregenerated hashes for EdDSA validation in FIPS mode, and added an indicator to bypass this restriction via configuration or parameters. (Architecture-related: FIPS Compliance)
  ↳ No PR: [2d75993](https://github.com/openssl/openssl/commit/2d759937e2ee78c27c83f1433f79b33256ab1a39)
- Rolled back incorrect validation indicator limitations and options for EdDSA in FIPS mode, ensuring FIPS compliance. (Architecture-related: FIPS compliance)
  ↳ No PR: [ca112fc](https://github.com/openssl/openssl/commit/ca112fccdd34a8538f14ddf8c3569b8331eae357), [1348f4b](https://github.com/openssl/openssl/commit/1348f4b5cff93025713157eea1f5ed228a5c61d6), [7de4770](https://github.com/openssl/openssl/commit/7de4770234582c9e95ea78e5a9ee51cce01faa1d), [f1b1724](https://github.com/openssl/openssl/commit/f1b17245b6b56ad064fe10508d6192262a0a3b15), [c140035](https://github.com/openssl/openssl/commit/c14003578a3ea24daf03c76719db7c0c1fb11097), [f9e1117](https://github.com/openssl/openssl/commit/f9e1117cca58a146c53aa7802f59f0424534fc5a)
- Fixed the value of larger index in FIPS indicator macro definition. (Architecture-related: public API)
  ↳ No PR: [ea3888a](https://github.com/openssl/openssl/commit/ea3888a39749d90c8fb32f4bc5544cda22a75a76)
- Moved the KDF key check in the FIPS module from the derive function to the set_ctx_params function to ensure that the key parameters are verified when setting them. (Architecture-related: FIPS module behavior change)
  ↳ No PR: [81bb884](https://github.com/openssl/openssl/commit/81bb88481d972ffe56c2432fdf41d7644e9d7b90)
- Removed the ability to bypass the FIPS self-test, deleted the verification logic related to the indicator, and ensured that the self-test must be executed. (Architecture-related: FIPS self-test behavior change)
  ↳ No PR: [4b7b40f](https://github.com/openssl/openssl/commit/4b7b40f2f79ea4d3cb205660690382b8b9e9291f)
- Upgrade the security check mechanism of the FIPS provider: Change the configurable security check to use FIPS indicators and always execute it, while disabling DSA signing in the FIPS provider and adding the corresponding indicator check. (Architecture event: FIPS indicator mechanism change)
  ↳ No PR: [c13ddf0](https://github.com/openssl/openssl/commit/c13ddf0a6c71efac8ef546f0d3632341afab3f07), [85caa41](https://github.com/openssl/openssl/commit/85caa417e0915aaae9fa6f87ccfa6c4c79b41dbb)
- Restrict EC key generation in FIPS mode to only allow curves with a security strength of no less than 112 bits, and add a FIPS indicator. (Architecture event: FIPS indicator mechanism change)
  ↳ No PR: [e3a453c](https://github.com/openssl/openssl/commit/e3a453c83810e6f7a128d2f472b8c71b7eceedb6)
- Changed the memory release operation of multiple key functions in the FIPS module to clear and then release, in line with the ISO 19790 standard. (Architecture-related: public API security compliance)
  ↳ No PR: [fa338aa](https://github.com/openssl/openssl/commit/fa338aa7cd1e893679c3e1c47465dcb11f90abfb)
- Disable RSA encryption using PKCS#1 v1.5 padding in FIPS mode. (Architecture-related: FIPS mode encryption behavior)
  ↳ No PR: [e928684](https://github.com/openssl/openssl/commit/e92868432018ebd7063c5dfe7594a5c58780038e)
- Limit the salt length of RSA-PSS in the FIPS provider and add corresponding verification logic. (Architecture-related: FIPS provider RSA-PSS salt length limit)
  ↳ No PR: [f3c03be](https://github.com/openssl/openssl/commit/f3c03be3adb9bd0e37c2f0267f4b53d5e056b684)
- Force OpenSSL internal DRBG to use derivation functions to meet FIPS validation requirements. (Architecture-related: FIPS compliance: DRBG uses derivation functions)
  ↳ No PR: [0ab796e](https://github.com/openssl/openssl/commit/0ab796ef9674b378ac644ad8d477685619a2ff37)
- Added a new build configuration for Windows platform, enabling FIPS and disabling thread pool and QUIC. (Architecture-related: Windows build configuration)
  ↳ No PR: [d1f4f3e](https://github.com/openssl/openssl/commit/d1f4f3e5fe9691f9dbfefbb57e42e2057b735a2c)
- Added no-fips-post configuration option for debugging only, used to disable FIPS self-test. (Architecture-related: Configuration option: FIPS self-test)
  ↳ No PR: [250a7ad](https://github.com/openssl/openssl/commit/250a7adbea455051da09c24fdb669ef6133e493a)

### Core Microkernel
- Added internal default value API for OpenSSL: query the installation path through the registry on Windows, and return compile-time constants on Unix. (Architecture-related: platform compatibility)
  ↳ No PR: [dd2b22d](https://github.com/openssl/openssl/commit/dd2b22d88c9c974f4ca6bce2550f89ac7fb76839)
- Replace the core hash table from LHASH to the new lock-free read hash table, and apply it to core_namemap to support lock-free read operations. (Architecture event: The core hash table is replaced by a lock-free hashtable)
  ↳ No PR: [71fe7f0](https://github.com/openssl/openssl/commit/71fe7f09831682e0dafe49e927da195792cff385), [4cad608](https://github.com/openssl/openssl/commit/4cad608509855a7c181a856d64084c97aee80589)
- Added the definitions of OID id-kp-wisun-fan-device and id-on-hardwareModuleName. (Architecture-related: public API)
  ↳ No PR: [387491d](https://github.com/openssl/openssl/commit/387491d53744384317806168668f3febb739a117)
- Added CRYPTO_atomic_store and CRYPTO_atomic_add64 atomic operation APIs to solve the false positive problem of thread cleaner. (Architecture-related: public API)
  ↳ No PR: [7e45ac6](https://github.com/openssl/openssl/commit/7e45ac6891ade57cb0141402745d144c4ce342cb)
- Added FIPS indicator callback mechanism, which can be set through OSSL_INDICATOR_set_callback(), which is used to record or process non-approved algorithms when non-approved algorithm checks occur. (Architecture-related: public API)
  ↳ No PR: [0557d6c](https://github.com/openssl/openssl/commit/0557d6c62b7d1f46f6f51e0dca87ad9409236164), [d484893](https://github.com/openssl/openssl/commit/d4848934a61a668d16078f3118786c9a741b7efd)
- Replaced and deprecated the TS_VERIFY_CTX_set_data, TS_VERIFY_CTX_set_store, TS_VERIFY_CTX_set_certs and TS_VERIFY_CTX_set_imprint functions, and added the corresponding set0 version to improve memory management. (Architecture-related: API deprecation and replacement)
  ↳ No PR: [6f811d8](https://github.com/openssl/openssl/commit/6f811d839fd637fa5dea0ee4286722847ab74b98)
- Added OPENSSL_strtoul wrapper function for reliable error checking of strtoul conversion. (Architecture-related: public API)
  ↳ No PR: [04f7729](https://github.com/openssl/openssl/commit/04f7729c409afad235737ee6b4edcb78efdc1bfd), [863e44c](https://github.com/openssl/openssl/commit/863e44c1e0841b7c46f3fa1ddf75870c60105303), [ec1d8ea](https://github.com/openssl/openssl/commit/ec1d8ead2855f6cd529f9a1ace0a667f34eefc58)
- Reconstruct the ECDSA signature and verification implementation, and add support for the ECDSA+hash composite signature algorithm. (Architecture-related: public API)
  ↳ No PR: [f68ba38](https://github.com/openssl/openssl/commit/f68ba38e189088cae4c625c995dd3fcec01d657c)
- Add verify_message parameter support for RSA signature and verification initialization, and refactor related functions. (Architecture-related: public API)
  ↳ No PR: [f5c8000](https://github.com/openssl/openssl/commit/f5c8000c0afb3643302db79a6d056e450b73430b), [8736de5](https://github.com/openssl/openssl/commit/8736de5e77fe1ccb52efd84e1d93372f57420495)
- Added error codes and corresponding error descriptions for continuous entropy source test failures. (Architecture-related: public API)
  ↳ No PR: [4f27f1a](https://github.com/openssl/openssl/commit/4f27f1a54a3ac151e294a583146f882943daea26)
- Implemented SP 800-90B Continuous Random Bit Generator Test (CRNGT) for FIPS modules, replacing the original crngt implementation. (Architecture-related: FIPS compliance)
  ↳ No PR: [ec4a2ff](https://github.com/openssl/openssl/commit/ec4a2fffa5c5f6d786519fd9b1c7528b8acfa621), [6be3a76](https://github.com/openssl/openssl/commit/6be3a764bafd3737046fe8e9ee9851318d408603), [6262ee5](https://github.com/openssl/openssl/commit/6262ee57105a8699a3c3a822940a74df7e1d92ec)
- Correct OSSL_sleep function for NonStop PUT model, introduce sleep() call, and remove deprecated SPT model support. (Architecture-related: public API and platform compatibility)
  ↳ No PR: [4a9e48f](https://github.com/openssl/openssl/commit/4a9e48f727ce7ad924c53a55b301e426d7e43863), [0d2a5f6](https://github.com/openssl/openssl/commit/0d2a5f600c7b6bef6fa6cf720204876560a6194b)
- Corrected the OID name, corrected ac-auditEntity to ac-auditIdentity. (Architecture-related: public API)
  ↳ No PR: [bce3a8d](https://github.com/openssl/openssl/commit/bce3a8d57e7512abb217cfab0c7671396fe0dae1)
- Fixed the deadlock problem that may be caused by not releasing the global lock when up_ref fails in the ENGINE_get_first, ENGINE_get_last, ENGINE_get_next and ENGINE_get_prev functions. (Architecture-related: public API)
  ↳ No PR: [e6174ca](https://github.com/openssl/openssl/commit/e6174ca4d48f6f4f954dd87f2cdf3718af14f064)
- Fixed the build error caused by reader_idx type mismatch under mingw64, changed the field type to uint32_t and corrected related comments. (Architecture-related: platform compatibility)
  ↳ No PR: [a2c74d7](https://github.com/openssl/openssl/commit/a2c74d7af66e6eff9b4355b27e760e8517746f08)
- Implemented an error handling mechanism for the jitter random number generator and added a retry mechanism, which can retry up to 3 times to handle intermittent failures and improve reliability. (Architecture-related: external behavior)
  ↳ No PR: [f8c510c](https://github.com/openssl/openssl/commit/f8c510cd20a43f7ac7705aca40fd38aacd5febeb), [f41b5ff](https://github.com/openssl/openssl/commit/f41b5ffe33bed336827096788b593e87927ae906)
- Removed the option to allow X9.31 padding in RSA encryption, as this padding mode only applies to signatures and should not be used in encryption. (Architecture-related: RSA encryption: Remove X9.31 padding option)
  ↳ No PR: [53b0527](https://github.com/openssl/openssl/commit/53b0527dd7f15350ed80fdcffa15e34e1ef0b9eb)
- Fixed the lock type error in CRYPTO_atomic_store, changing the read lock to a write lock. (Architecture-related: public API)
  ↳ No PR: [3190f5c](https://github.com/openssl/openssl/commit/3190f5c06bd23ae4ddc659409e77070a6caa1539)
- Fixed the type mismatch problem of reader_idx in InterlockedExchange call on Windows to avoid MinGW compilation warning. (Architecture-related: platform compatibility)
  ↳ No PR: [a46abbd](https://github.com/openssl/openssl/commit/a46abbd66eecdbfba84c81eca8911f5d9564c8a8)
- Due to problems with the read-write lock implementation of the Non-Stop KLT thread model, read-write lock support under this model is temporarily disabled. (Architecture-related: platform compatibility)
  ↳ No PR: [7408d58](https://github.com/openssl/openssl/commit/7408d58714e3235f58c4d7eba42207c83b55e6bd)
- Replaced the compile-time default path macro with the runtime query API, and added a unit test for Windows registry key lookup. (Architecture-related: Platform compatibility: Default path changed to runtime query)
  ↳ No PR: [e6c77f2](https://github.com/openssl/openssl/commit/e6c77f26855661ec4bfe0a91fcf1c718ac48967f)
- Add validity check of digest size in OSSL_STORE_SEARCH_by_key_fingerprint function to prevent integer overflow. (Architecture-related: public API)
  ↳ No PR: [18a30b5](https://github.com/openssl/openssl/commit/18a30b5637cfaed0830183c1572cac76cfa40b4b)
- Fixed remaining issues on RISC-V platforms that caused build failures due to missing OPENSSL_CPUID_OBJ checks, and added this macro judgment in conditional compilation of multiple AES hardware implementations. (Architecture-related: Platform compatibility: RISC-V build fixes)
  ↳ No PR: [347f05e](https://github.com/openssl/openssl/commit/347f05e893e7b17f8e7ae5995aa7521705821080)

### EVP Abstraction Layer
- Added complete support for RFC 5755 attribute certificates, covering ASN.1 definition, I/O API, configuration file loading, getter/setter, signature verification, attribute management and printing functions. (Architecture-related: public API)
  ↳ No PR: [7dcee34](https://github.com/openssl/openssl/commit/7dcee34c8f921ad65277e9a75fca4a7337fbed6d), [dab96a4](https://github.com/openssl/openssl/commit/dab96a4f60f12b162f02ce2ddf4f70bb1e24bd5b), [0e8020a](https://github.com/openssl/openssl/commit/0e8020a45b2f24e85769cd2c66c41f0b7ffa21e4), [9e1a8b5](https://github.com/openssl/openssl/commit/9e1a8b5ecce7bcf706f48805f2999bbc3d4ef09a), [b97fb22](https://github.com/openssl/openssl/commit/b97fb22f596bfb528e69402b1bdcdf144a563918), [62960b8](https://github.com/openssl/openssl/commit/62960b8710a39d58fe386a51dccbd35bd973220f), [6b16731](https://github.com/openssl/openssl/commit/6b167313f422b8744c1f4edc8688f7e6923a3a73), [1eeec94](https://github.com/openssl/openssl/commit/1eeec94f1fd7de60248d1093d5552dc1f05c2fc9), [f892397](https://github.com/openssl/openssl/commit/f892397c52ab6db813f40a0e8de3b89bffd93f66)
- Add FIPS self-testing to EDDSA, and expose relevant APIs through conditional compilation to support FIPS modules. (Architecture-related: FIPS self-testing)
  ↳ No PR: [5f04124](https://github.com/openssl/openssl/commit/5f04124aab4a477d4e58149d8f04871ff7e5ea4b)
- In CMS_verify and PKCS7_verify, the certificate passed in the -certfile option is used to build the certificate chain, and the search priority of PKCS7_get0_signers is adjusted. (Architecture-related: public API)
  ↳ No PR: [29bbe7d](https://github.com/openssl/openssl/commit/29bbe7d0086aec1f0fec1ffc03d05aa4610c4a12)
- Added init, update and final functions to the three API groups EVP_PKEY_sign, EVP_PKEY_verify and EVP_PKEY_verify_recover to support the direct use of explicitly obtained composite signature algorithms. (Architecture-related: public API)
  ↳ No PR: [e675aab](https://github.com/openssl/openssl/commit/e675aabb8747d0f2da5691945f1a429558ebc34d)
- Reconstructed the EdDSA signature algorithm implementation, added support for the EVP_PKEY_sign/verify_message series of functions, and added initialization and operation functions for ph and ctx variants for Ed25519 and Ed448. (Architecture-related: public API)
  ↳ No PR: [1751334](https://github.com/openssl/openssl/commit/1751334f59816d675a1ea85e98434a8231a58efe)
- Added support for X.509 v3 extensions such as targetingInformation, acceptable certificate policy, acceptable privilege policy, delegatedNameConstraints, holderNameConstraints, subjectDirectoryAttributes and associatedInformation. (Architecture-related: public API)
  ↳ No PR: [58301e2](https://github.com/openssl/openssl/commit/58301e24f66aa74b13b85a171dd14e6088c35662), [2b735fe](https://github.com/openssl/openssl/commit/2b735fe2195938ea6cafbef37c8bcf8a33b04c4b), [a7ed61c](https://github.com/openssl/openssl/commit/a7ed61ce8b0565483e6b0e44ed9b13682305e609), [be5adfd](https://github.com/openssl/openssl/commit/be5adfd6e36817fe8d5b5793f8c23189dc412045)
- Added support for X.509v3 auditIdentity, userNotice and basicAttConstraints extensions. (Architecture-related: public API)
  ↳ No PR: [9216859](https://github.com/openssl/openssl/commit/9216859f7b2d68f819d9b8a8ad53c2f59f3e263f), [2ef6fa1](https://github.com/openssl/openssl/commit/2ef6fa1cdda8dc79ee520d129a87bd3525a37a1f), [7f5db0c](https://github.com/openssl/openssl/commit/7f5db0c9a9360dc62155bbe42b97d02040738d8b), [34e8ddf](https://github.com/openssl/openssl/commit/34e8ddfc442654b05d0602d7a156bba92a4fd97f)
- Reconstruct the RSA EVP_SIGNATURE implementation, adding support for the RSA+hash composite algorithm (sigalg), by wrapping the hash function and adding the corresponding initialization, signature, verification and context parameter processing functions. (Architecture-related: public API)
  ↳ No PR: [572a837](https://github.com/openssl/openssl/commit/572a8371ab600cfcf89284b692625dbfb7627f2d)
- Added X509v3_add_extensions function, which is used to add an extension list to the extension stack, and update the calls in the CMP module to use the new function. (Architecture-related: public API)
  ↳ No PR: [4925af7](https://github.com/openssl/openssl/commit/4925af7bb88dbe11c323813fd91740dcd813bfd8)
- Extended X509_REQ_add_extensions_nid function to support appending or overwriting existing extensions in certificate requests. (Architecture-related: public API)
  ↳ No PR: [eaf577c](https://github.com/openssl/openssl/commit/eaf577c865c41946b478b4da5f8c477e132d470d)
- Reconstruct the EVP_PKEY operation type checking macro, make the internal macros reuse public macros, and supplement the missing public operation type macros. (Architecture-related: public API)
  ↳ No PR: [b96e10b](https://github.com/openssl/openssl/commit/b96e10b9f9bfaba3c373d3d5716fe0408eb0aa8c)
- Added EVP_CIPHER_CTX_set_algor_params and EVP_CIPHER_CTX_get_algor_params API, as well as the algorithm parameter setting and acquisition functions of EVP_PKEY_CTX, to replace the old PKCS7/CMS related control commands. (Architecture-related: public API)
  ↳ No PR: [258aaa9](https://github.com/openssl/openssl/commit/258aaa97b86aab7fef3c6170d59053842ce2e253), [033dcce](https://github.com/openssl/openssl/commit/033dcce2bae2d1d261f2460f5b9217682e03a7cf)
- Add ED25519 and ED448 support to EVP_PKEY_sign_init_ex2() and EVP_PKEY_verify_init_ex2(). Only pre-hash mode is supported and the instance needs to be explicitly specified through parameters. (Architecture-related: public API)
  ↳ No PR: [6696682](https://github.com/openssl/openssl/commit/66966827740a04249300b0b25735e9d4c9bcab26)
- Added key generation parameter acquisition and obtainable parameter query functions, allowing parameter query after key generation. (Architecture-related: public API)
  ↳ No PR: [d9346c5](https://github.com/openssl/openssl/commit/d9346c59f4bf91d5bfab23813f6f9d752b67397b)
- Expose the EVP_DigestSignFinal and EVP_DigestVerifyFinal interfaces in the FIPS module, and update the self-test. (Architecture-related: public API)
  ↳ No PR: [96de408](https://github.com/openssl/openssl/commit/96de408228031511e38f8b14a9b7af26f988e72d)
- Added support for issuedOnBehalfOf X.509v3 extension. (Architecture-related: public API)
  ↳ No PR: [2546932](https://github.com/openssl/openssl/commit/254693280d1a93f5c1ab81f0f8d171b980ac0664)
- Added EVP_MD_CTX_get_size_ex() function to correctly handle XOF digest size acquisition, and added get_ctx_params() support for SHAKE implementation. (Architecture-related: public API)
  ↳ No PR: [c48e568](https://github.com/openssl/openssl/commit/c48e56874c5c7d3af3d522e4cae7cb9069143667)
- Increase the maximum response length limit for CRL download. (Architecture-related: public API: CRL download response length limit)
  ↳ No PR: [e9d5ed8](https://github.com/openssl/openssl/commit/e9d5ed8f3de2e9b7879f06dbdead633960ba3012), [2d5fae4](https://github.com/openssl/openssl/commit/2d5fae4d48c466f3cf3ea0180fc58729e7587a55)
- Fixed the X509v3_get_ext_by_critical and X509_EXTENSION_set_critical functions, changed the default value of the extended critical attribute from -1 to 0, and optimized the comparison logic of critical values. (Architecture-related: public API)
  ↳ No PR: [50f2e21](https://github.com/openssl/openssl/commit/50f2e2146aa1092bdf3435a3543e8a5d0b4c4d4c)
- Fixed the problem that when setting the provider signature algorithm through the SignatureAlgorithms configuration command, the provider signature algorithm is not used and falls back to the default value. (Architecture-related: public API)
  ↳ No PR: [4169d58](https://github.com/openssl/openssl/commit/4169d58c855718d90424fd5da632cf2f2b46e691)
- Fixed the behavior of EVP_PKEY_CTX_add1_hkdf_info so that it correctly performs the append operation instead of overwriting. (Architecture-related: public API)
  ↳ No PR: [6b56668](https://github.com/openssl/openssl/commit/6b566687b58fde08b28e3331377f050768fad89b)
- Reject setting of invalid CSR version number, enhanced input validation. (Architecture-related: public API behavior change)
  ↳ No PR: [397051a](https://github.com/openssl/openssl/commit/397051a40db2d68433b842e7505e8cf3c9effb36)
- Made EVP_DigestFinal fail for SHAKE128 and SHAKE256 when OSSL_DIGEST_PARAM_XOFLEN is not set, and updated related initialization functions and tests. (Architecture-related: public API behavior changes)
  ↳ No PR: [b911fef](https://github.com/openssl/openssl/commit/b911fef216d1386210ec24e201d54d709528abb4)
- Fixed the problem of repeatedly searching the default CA path. When the URI is not specified, the default certificate directory is no longer automatically used to avoid repeated loading. (Architecture-related: public API behavior change)
  ↳ No PR: [6d01857](https://github.com/openssl/openssl/commit/6d018570407606acc1eabe68921496d77f27aeb9)
- Fixed the processing of empty parameters in EVP_PKEY_CTX_add1_hkdf_info, and added related test cases. (Architecture-related: public API behavior changes)
  ↳ No PR: [299996f](https://github.com/openssl/openssl/commit/299996fb1fcd76eeadfd547958de2a1b822f37f5)
- Add null pointer check to EVP_CIPHER_CTX_get_key_length function, return 0 when ctx->cipher is null. (Architecture-related: public API behavior fix)
  ↳ No PR: [46f5523](https://github.com/openssl/openssl/commit/46f55238d2dc39725873de308e1e727556cb33bd)
- Fixed a regression when measuring SHAKE128/SHAKE256 using the -evp parameter, now EVP_Digest_loop() will use the correct initialization, update and expandable output functions for XOF mode. (Architecture-related: public API)
  ↳ No PR: [184d29d](https://github.com/openssl/openssl/commit/184d29dbabbb6c7a5cc829d3ac4b966f781d2b2e)
- Fixed the problem that the fallback mechanism of EVP_PKEY_CTX_add1_hkdf_info() fails when the old provider does not implement the get parameter interface. Instead, it decides whether to perform rollback by checking the obtainable parameter list. (Architecture-related: public API behavior)
  ↳ No PR: [663dbc9](https://github.com/openssl/openssl/commit/663dbc9c9c897392a9f9d18aa9a8400ca024dc5d)
- Fixed a crash problem that may occur when the EVP_DigestUpdate function is empty when ctx->update is empty. (Architecture-related: public API)
  ↳ No PR: [ad33d62](https://github.com/openssl/openssl/commit/ad33d62396b7e9db04fdf060481ced394d391688)
- Fixed the problem that when searching for the EVP algorithm by name, it cannot be found if the name has not been registered. Now it will try to automatically load the algorithm before searching. (Architecture-related: public API: EVP algorithm search behavior)
  ↳ No PR: [454ca90](https://github.com/openssl/openssl/commit/454ca902c7d5337249172b38efc5e4fd63f483f4)
- Fixed the alias problem of audit entity OID, correctly mapping ac-auditEntity to ac-auditIdentity. (Architecture-related: public API)
  ↳ No PR: [91432b9](https://github.com/openssl/openssl/commit/91432b9ea040a0b11e85875a555dc1f4dcfc02dc)
- Fixed the processing of PBMAC1 algorithm in PKCS12 MAC verification in FIPS mode, and implemented the support of PBMAC1 defined in RFC 9579 in PKCS#12. (Architecture-related: PBMAC1 support)
  ↳ No PR: [d7b659e](https://github.com/openssl/openssl/commit/d7b659e18510771450b7e4794313902815f9e206), [fe79159](https://github.com/openssl/openssl/commit/fe79159be0c6a576b475001ca111185901637692)
- Fixed base64 BIO incorrect handling of internal blanks under the BIO_FLAGS_BASE64_NO_NL flag, abnormal decoding behavior after skipping invalid input, buffer lines not being decoded in time during retryable reading, and inconsistent return values after reading, and improved related documentation and testing. (Architecture-related: public API)
  ↳ No PR: [0cd9dd7](https://github.com/openssl/openssl/commit/0cd9dd703ea575699b2d3cd74f1b8224447f4352)
- Updated the EVP_MD_size() return value check, changing the judgment of less than zero to less than or equal to zero to correctly handle the situation where the SHAKE algorithm returns zero. (Architecture-related: public API)
  ↳ No PR: [14c4533](https://github.com/openssl/openssl/commit/14c45338e986d5827f1e944d0cffe54a7f4697ea)
- Fixed the problem in EVP_CIPHER_CTX_get_algor_params that the array may be accessed out of bounds due to incorrect handling of i as a negative value. (Architecture-related: public API)
  ↳ No PR: [bbe4571](https://github.com/openssl/openssl/commit/bbe4571f570ec28b4709746b6d4d624ca5394cc6)
- Replaced the EVP_MD_get_flags and EVP_MD_FLAG_XOF macros in the code with the new EVP_MD_xof() function call, and fixed the boundary check of mdlen in PKCS1_MGF1 and the resource leak problem of cipher_test_init in the test. (Architecture-related: public API)
  ↳ No PR: [976dd35](https://github.com/openssl/openssl/commit/976dd3581a00c5006bd696ac9ba7289de4d137d5)
- Add a version number check in the CSR verification function and reject certificate requests with a version number other than 1. (Architecture-related: public API behavior changes)
  ↳ No PR: [7fab3c7](https://github.com/openssl/openssl/commit/7fab3c7d61b0064dcf50db39fb490970c60d9a34)
- Add verification to the client ALPN extension parsing whether the protocol selected by the server belongs to the client's initial announcement list. (Architecture-related: external behavior)
  ↳ No PR: [238fa46](https://github.com/openssl/openssl/commit/238fa464d6e38aa2c92af70ef9580c74cff512e4)

### Cross-cutting / Other Architecture-related Changes
- The CMP client has added support for requesting CRL updates through genm messages, receiving CRLs through genp messages, and adding corresponding command line options. (Architecture-related: CMP protocol)
  ↳ No PR: [40a200f](https://github.com/openssl/openssl/commit/40a200f9e781381d72d234c886e38bcfce36bbc8), [ee28152](https://github.com/openssl/openssl/commit/ee28152e86641e0299fdb3151716bb0451b2bc53), [6a3579e](https://github.com/openssl/openssl/commit/6a3579e190fd52f49b1e5eafb4d002684eb0ff42)
- Added integrity-only cipher suite support for TLS v1.3, including adding ssl_cipher_get_evp_md_mac() API, extending the record layer to support MAC-only operations, adding build options and test vectors. (Architecture-related: TLS 1.3 integrity suite)
  ↳ No PR: [b6a5e80](https://github.com/openssl/openssl/commit/b6a5e801679663c13875cf6e18f475f8700d72a9)
- Enable support for POSIX context functions on FreeBSD to be compatible with asynchronous operations. (Architecture-related: platform compatibility)
  ↳ No PR: [9aad59c](https://github.com/openssl/openssl/commit/9aad59c224e6b490dbd9a7b93bd3dee2ad42bae3)
- Added a function for QUIC stream reception to determine whether there is data waiting to be read. (Architecture-related: public API)
  ↳ No PR: [26dd6ba](https://github.com/openssl/openssl/commit/26dd6ba070fdc2566c1a51d29e57e55c9ec7c78b)
- Added CPU capability detection and CPUINFO printing support on the RISC-V platform, so that OpenSSL can also output CPU capability information on the RISC-V architecture. (Architecture-related: platform compatibility)
  ↳ No PR: [66ad636](https://github.com/openssl/openssl/commit/66ad636b979554ddde5cd5908feabda79d07317b), [c1bf576](https://github.com/openssl/openssl/commit/c1bf576037ef8fe665abb47c11336e91f007e34c)
- Make the conf_diagnostics configuration also apply to SSL configuration errors, automatically set the SSL_CONF_FLAG_SHOW_ERRORS flag to display error messages when configuration diagnostics are enabled. (Architecture-related: Configuration diagnostics behavior)
  ↳ No PR: [21819f7](https://github.com/openssl/openssl/commit/21819f78b057c254254646a7854bfad0cd40ed83), [af0561d](https://github.com/openssl/openssl/commit/af0561d7e7769504356e04f4b591ce79aace3ac2), [a0d37e2](https://github.com/openssl/openssl/commit/a0d37e200fee7e7eb1176370aedbc32764edc737), [3e191f4](https://github.com/openssl/openssl/commit/3e191f487907a474b6bd6e497043d1560972e7d7)
- Abandoned the SSL_SESSION_get_time and SSL_SESSION_set_time functions, and introduced corresponding new functions; at the same time, deprecated SSL_CTX_flush_sessions, and introduced SSL_CTX_flush_sessions_ex to solve Y2038 compatibility issues. (Architecture-related: version and compatibility)
  ↳ No PR: [00a6d07](https://github.com/openssl/openssl/commit/00a6d0743a38e179f5f9b5de4b73be9fcec0bb4c), [86c9bb1](https://github.com/openssl/openssl/commit/86c9bb137836036f2c95a2b2ee7abfd564b49708), [f7ded92](https://github.com/openssl/openssl/commit/f7ded920f3f7311ebe2a5bcff256ba8719d19dfd)
- Added an independent jitter entropy source provider, which can replace SEED-SRC, and provides sample configuration. (Architecture-related: entropy source provider)
  ↳ No PR: [b28b312](https://github.com/openssl/openssl/commit/b28b3128048a83ba036c9d8a789badac9b1a2804)
- Added the function of listing TLS signature algorithms, supports displaying built-in algorithms and provider-registered algorithms, and added the --tls-signature-algorithms option to the openssl list command. (Architecture-related: public API)
  ↳ No PR: [38a7183](https://github.com/openssl/openssl/commit/38a7183102eb496436f0616884a3c82a22857ce5)
- Extended TLSv1.3 record layer padding API, added SSL_set_block_padding_ex() and SSL_CTX_set_block_padding_ex(), supporting setting different padding block sizes for handshake messages and application data messages respectively. (Architecture-related: public API)
  ↳ No PR: [21dfb97](https://github.com/openssl/openssl/commit/21dfb975968d73b9cd40835d2cd436602079e853)
- Extend the mask field in the ssl_method_st structure to 64 bits to support more than 32 bits of SSL operation option flags. (Architecture-related: SSL option extension)
  ↳ No PR: [89c9c3b](https://github.com/openssl/openssl/commit/89c9c3b857b5d68d835c3c3d371dc74a26f568fd)
- Add support for encapsulation and decapsulation operations in the pkeyutl command, and add corresponding command line options. (Architecture-related: public API)
  ↳ No PR: [12b2e55](https://github.com/openssl/openssl/commit/12b2e5552b98071a91e5fe1721820ad5c9934dc5), [14fa2f5](https://github.com/openssl/openssl/commit/14fa2f5f474c8fe8cd09b513692a42a0a57467d2)
- Add elf_aux_info() support for OpenBSD, extending conditional compilation in CPU feature detection code for ARM and PowerPC. (Architecture-related: Platform compatibility)
  ↳ No PR: [01f4b44](https://github.com/openssl/openssl/commit/01f4b44e075a796d62d3b007a80c5c04d0e77bfb)
- Added windowscontext option to openssl info command, used to display Windows installation context information. (Architecture-related: Platform compatibility: Windows installation context)
  ↳ No PR: [5b1909d](https://github.com/openssl/openssl/commit/5b1909d1d0fbbea46042f34459345619e7f889f6), [165038b](https://github.com/openssl/openssl/commit/165038be62092f3efbf9b7104e2a4abf638e8667)
- Fixed the CMS_get1_certs and CMS_get1_crls functions to ensure that they only return NULL when an error occurs, rather than when the certificate or CRL list is empty. (Schema related: public API)
  ↳ No PR: [cc31db1](https://github.com/openssl/openssl/commit/cc31db1eb6ccdfa3028b21a4a6236d721e0ca36b), [96b59ec](https://github.com/openssl/openssl/commit/96b59ec4b61e10b1b2eb705a4f8f06ea5f976d08)
- Fixed a memory leak in OBJ_add_object when replacing an existing object, and improved error handling to roll back changes when the insertion fails. (Architecture-related: public API)
  ↳ No PR: [e91384d](https://github.com/openssl/openssl/commit/e91384d5b0547bf797e2b44976f142d146c4e650)
- Fixed an issue where setting msg_name on a connected UDP socket caused sendmsg to fail on macOS and OpenBSD, by detecting the socket connection status to avoid setting the peer address. (Architecture-related: Platform compatibility)
  ↳ No PR: [c062403](https://github.com/openssl/openssl/commit/c062403abd71550057b3647b01cc8af4cc2fc18c)
- Fixed the Windows platform RCU callback linked list appending logic to avoid linked list loops and make it behave consistent with the pthread version. (Architecture-related: platform compatibility)
  ↳ No PR: [f39a862](https://github.com/openssl/openssl/commit/f39a86281883bd7ff0b3791ed203756d055c001b)
- Fixed the error type being changed from SSL error to system call error when SSL_sendfile fails, with system error information attached. (Architecture-related: public API behavior change)
  ↳ No PR: [3dcd851](https://github.com/openssl/openssl/commit/3dcd85139f30625f2e4d072fe2b0f211f76f819c)
- Disable recvmmsg datagram method in versions below Android 5 to be compatible with old API. (Architecture-related: Platform compatibility)
  ↳ No PR: [24109dc](https://github.com/openssl/openssl/commit/24109dca5a793d58c68a346db5b21746079ec317)
- Fixed the check logic in OSSL_CMP_validate_msg, making the OSSL_CMP_OPT_PERMIT_TA_IN_EXTRACERTS_FOR_IR option available again. (Architecture-related: public API)
  ↳ No PR: [b893cee](https://github.com/openssl/openssl/commit/b893ceef2feb6b64504446f984ee5a57d2b69d1f)
- Fixed an issue with sending errors when no root CA certificate updates are available, and adjusted the behavior of related CMP functions. (Architecture-related: public API behavior changes)
  ↳ No PR: [fc9649f](https://github.com/openssl/openssl/commit/fc9649f61a8ac5f980da6807214fcbbbae1c45aa)
- Fixed the possible out-of-order problem of RCU pointer dereference when compiling with clang on Apple M1 virtualized CPU, and used the ldar instruction to ensure the correct memory barrier through inline assembly. (Architecture-related: platform compatibility)
  ↳ No PR: [f5b5a35](https://github.com/openssl/openssl/commit/f5b5a35c84626823364b0c8535b968c106690a56)
- Fixed an issue in BIO_s_connect where keepalive was incorrectly set for datagram sockets. Now only keepalives are enabled for streaming sockets. (Architecture-related: public API)
  ↳ No PR: [5673680](https://github.com/openssl/openssl/commit/56736800224eff5783e314fd334c047224081c58)
- Fixed the checking logic of socket descriptors on Windows platform to correctly identify invalid sockets. (Architecture-related: platform compatibility)
  ↳ No PR: [c89baf8](https://github.com/openssl/openssl/commit/c89baf871030c811ba316ccbdcea26c294f605ae)
- For connections with TLS version higher than 1.0, use the empty renegotiate extension instead of SCSV to indicate renegotiation support. (Architecture-related: TLS protocol behavior)
  ↳ No PR: [972ee92](https://github.com/openssl/openssl/commit/972ee925b16fc3bc7ec71080c439e669754235ab)
- Fixed the processing logic when the -certout and -chainout parameters specify the same file name, and added support for certReqTemplate type genm response. (Architecture-related: CMP command line interface)
  ↳ No PR: [5aec3f4](https://github.com/openssl/openssl/commit/5aec3f4a72604d76970581f1ea445b331beda608)
- Fixed undefined behavior that could occur when the session ID length is zero, to avoid performing a memory copy of a null pointer when the length is 0. (Architecture-related: public API behavior fix)
  ↳ No PR: [97c6489](https://github.com/openssl/openssl/commit/97c6489b39c966c6e5169b9b92ec5fa9a35c7ba3)
- Fixed an issue where configuration diagnostic values were overwritten when not set in the configuration file, ensuring that diagnostic settings are only updated when explicitly specified in the configuration file. (Architecture-related: public API behavior fix)
  ↳ No PR: [64bfdeb](https://github.com/openssl/openssl/commit/64bfdebdc049ee2ad5ca6456b87abbd67e6d5479)
- Added reason codes with correct offsets for two TLS alarms, and added corresponding error strings, fixing the problem that the reason strings could not be found correctly. (Architecture-related: public API error code correction)
  ↳ No PR: [a401aaf](https://github.com/openssl/openssl/commit/a401aaf9ed6eb34842cdedfcc35448bdc4174df3)
- On QNX systems, a check for the __QNX__ macro is added in conditional compilation to avoid using the ipi_spec_dst field in the in_pktinfo structure. (Architecture-related: platform compatibility)
  ↳ No PR: [3682f27](https://github.com/openssl/openssl/commit/3682f27430ccbd25abff755ad0bf67d057768a81)
- Enhanced the strictness of IPv4 address parsing in the ipv4_from_asc function, rejecting invalid input formats. (Architecture-related: external behavior)
  ↳ No PR: [3fc7848](https://github.com/openssl/openssl/commit/3fc784835cdb8489117c2680e867cd32b3b70fbe)
- Fixed the cpuid_obj conditional compilation check for SM3 and SM4 on RISC-V to ensure that the relevant hardware acceleration code is only enabled when OPENSSL_CPUID_OBJ is defined. (Architecture-related: Platform compatibility)
  ↳ No PR: [6cf42ad](https://github.com/openssl/openssl/commit/6cf42ad392241c9fee586d99b53d9bfa74130b0b)
- Fixed a bug in the handling of the max_fragment_length extension in PSK sessions, ensuring new sessions correctly initialize the field and no longer incorrectly requesting the extension when resuming a session. (Architecture-related: public API)
  ↳ No PR: [fa49560](https://github.com/openssl/openssl/commit/fa495604516a610d988f02298c8d97a6ac4777bb)
- Fixed the SSL_select_next_proto function and added non-empty and format verification of the client protocol list to prevent unverified lists from causing security issues (CVE-2024-5535). (Architecture-related: public API)
  ↳ No PR: [2ebbe2d](https://github.com/openssl/openssl/commit/2ebbe2d7ca8551c4cb5fbb391ab9af411708090e), [0d883f6](https://github.com/openssl/openssl/commit/0d883f6309b6905d29ffded6d703ded39385579c), [9925c97](https://github.com/openssl/openssl/commit/9925c97a8e8c9887765a0979c35b516bc8c3af85), [de71058](https://github.com/openssl/openssl/commit/de71058567b84c6e14b758a383e1862eb3efb921)
- Fixed the problem of pointer width mismatch caused by using CRYPTO_atomic_load when the hash table is looked up on non-64-bit systems. Use ossl_rcu_deref for safe loading instead. (Architecture-related: platform compatibility)
  ↳ No PR: [2c7cae5](https://github.com/openssl/openssl/commit/2c7cae53bc61f40baff70af0495cf3d976ed7d14)
- Fixed the processing of configuration paths returning NULL, ensuring that commands such as openssl version return empty strings instead of NULL when there is no configuration file, to avoid crashes. (Architecture-related: public API behavior)
  ↳ No PR: [917f371](https://github.com/openssl/openssl/commit/917f37195ac95252a4c90e86d7d7414c5569aed8), [97bfbb9](https://github.com/openssl/openssl/commit/97bfbb98b0f9f2a381a47a01ae4e20f511adae05), [a8f99f9](https://github.com/openssl/openssl/commit/a8f99f98d601efdc212d958a79af78bbbb0f12e0)
- Fixed the problem that OSSL_LIB_CTX_free(NULL) does not handle null pointers correctly, and added related documentation. (Architecture-related: public API)
  ↳ No PR: [981d129](https://github.com/openssl/openssl/commit/981d129a5609ee2e031367c34c67a9f61a5bfd66), [d38f62e](https://github.com/openssl/openssl/commit/d38f62ea118170fc40e10f6f95b180cccbaa7581)
- Fixed conditional compilation indentation and logic in defaults code to ensure that the run_once routine is only defined when OSSL_WINCTX is defined to avoid compiler errors. (Architecture-related: platform compatibility)
  ↳ No PR: [bf74cf3](https://github.com/openssl/openssl/commit/bf74cf35cf47bfa44a89a6f8c3e52a3ec76d828f)
- Fixed VS2010 x86 build error, added CRYPTO_atomic_add64 and CRYPTO_atomic_and atomic operation functions, and updated RCU lock implementation. (Architecture-related: public API)
  ↳ No PR: [16beec9](https://github.com/openssl/openssl/commit/16beec98d26644b96d57bd8da477166d0bc7d05c)
- Fixed OPENSSL_hexstr2buf_ex() writing a byte before the output buffer and incorrect length reporting when handling zero-length input. (Architecture-related: public API)
  ↳ No PR: [3f7b355](https://github.com/openssl/openssl/commit/3f7b355733407cf777bfad5ce5b79610588bacc5)
- The error message has been expanded in the duplicate attribute error entry, and will now be accompanied by the name of the duplicate attribute. (Schema related: public API)
  ↳ No PR: [7760021](https://github.com/openssl/openssl/commit/77600210e20b566f746fcc7fc18f44f1b01a2313)
- Disabled the use of XOF digests in multiple KDFs (PBKDF2,
  ↳ No PR: [a582791](https://github.com/openssl/openssl/commit/a5827910da30b6793d3df06df8db0a167416afe1), [14e4660](https://github.com/openssl/openssl/commit/14e46600c68ece74970462a60ad20703221747a1), [efba3f1](https://github.com/openssl/openssl/commit/efba3f1351f2dc68890287cb9d5185d131eacd87)
- After calling ASN1_item_i2d, check whether the return length is negative and whether the pointer is empty, which enhances the robustness of error handling. (Architecture-related: public API)
  ↳ No PR: [391334d](https://github.com/openssl/openssl/commit/391334dd8ca7374c17e0a616ff539c84ec99eddb)
- Fixed the problem of sending wrong alert when key_share is missing in TLS 1.3, instead sending illegal_parameter; and added a check for missing supported_versions extension to comply with RFC specifications. (Architecture-related: TLS 1.3 protocol behavior)
  ↳ No PR: [60358f2](https://github.com/openssl/openssl/commit/60358f2c5e3a26e516ece2e075d0fd4198665412), [293d0a0](https://github.com/openssl/openssl/commit/293d0a0052166222a4b8a0bdd12e6ceca812f6ab)
- Fixed the check of error return codes in http_server_init(), and added a call to BIO_set_accept_ip_family to support IPv4/IPv6 dual stack. (Architecture-related: platform compatibility)
  ↳ No PR: [5de917e](https://github.com/openssl/openssl/commit/5de917ef9c3a3772ad6f06dc6a1072ad752dd484), [44b6211](https://github.com/openssl/openssl/commit/44b6211e1f144fd51722f50b9c22b9113f29eb5b)
- Fixed the problem of incorrectly starting a connection through SSL_pending() or _has_pending(), and added an early return check when the connection is not started in the QUIC implementation. (Architecture-related: public API)
  ↳ No PR: [b7f93c7](https://github.com/openssl/openssl/commit/b7f93c7fcb37c81b88895c3e8d22ad69c2576cd4)
- Fixed the problem of SSL_handle_events() and SSL_poll() implicitly starting the connection when the connection is not started, and instead only perform related operations when the connection is started. (Architecture-related: public API)
  ↳ No PR: [ca1d2db](https://github.com/openssl/openssl/commit/ca1d2db291530a827555b40974ed81efb91c2d19)
- Fixed the issue where OSSL_HTTP_open() could not correctly set the default port under IPv6 host address. (Architecture-related: public API)
  ↳ No PR: [fad8a58](https://github.com/openssl/openssl/commit/fad8a58eae0dd7515c542e099aa7bff4ea9c99f9)
- Fixed the message callback function and related assertions and error codes that are called when receiving Change Cipher Spec records in TLSv1.3. (Architecture-related: TLS protocol implementation)
  ↳ No PR: [8781087](https://github.com/openssl/openssl/commit/8781087a69934cf45e201ac425d593b0e12a1538)
- Fixed the TLS alert type sent when PSK binder verification fails, changed to DECRYPT_ERROR to comply with RFC 8446 specification. (Architecture-related: Protocol compliance)
  ↳ No PR: [02b8b7b](https://github.com/openssl/openssl/commit/02b8b7b83698d1c7ddfef274f16c039c8cca7988)
- Fixed an issue where redundant data was ignored in TLS CertificateVerify messages, such messages will now be detected and rejected. (Architecture-related: protocol behavior)
  ↳ No PR: [b4e4bf2](https://github.com/openssl/openssl/commit/b4e4bf29ba3c67662c60ceed9afa2dd301e93273)
- Fixed the type conversion error when calling InterlockedExchangeAdd in the Windows thread code, changing the incorrect long * and long to LONG * and LONG. (Architecture-related: platform compatibility)
  ↳ No PR: [8048a8a](https://github.com/openssl/openssl/commit/8048a8a8a069a3fb3ac687719e9174608ee7f052)
- Fixed the build failure caused by undeclared gcm_ghash_4bit when compiling with OPENSSL_SMALL_FOOTPRINT under ARM architecture, and setting the ghash function pointer to blank through conditional compilation. (Architecture-related: platform compatibility)
  ↳ No PR: [43e804a](https://github.com/openssl/openssl/commit/43e804acc6dedff53e65376a16e229680b51bae7)
- Fixed the S/MIME type of AuthEnvelopedData to correctly set authEnveloped-data when writing. (Architecture-related: public API)
  ↳ No PR: [87bb277](https://github.com/openssl/openssl/commit/87bb2770e5b5371efbe068735d80b5c223d90dcf)
- Fixed the null pointer dereference problem that may be triggered when using non-standard pkcs11 parameters, and added checks for null pointers in i2o_ECPublicKey and EC_POINT_point2oct. (Architecture-related: public API)
  ↳ No PR: [13e33f3](https://github.com/openssl/openssl/commit/13e33f3d4b3232f19298c3e1ec982603176c923f)
- Fixed the potential double release problem in SRP_user_pwd_set1_ids caused by not clearing the pointer in time after releasing it. (Architecture-related: public API)
  ↳ No PR: [711cd7c](https://github.com/openssl/openssl/commit/711cd7c200f66f4a2970413b941fa53b732e4542)
- When the application provides a custom memory allocation function through CRYPTO_set_mem_functions, CRYPTO_aligned_alloc no longer uses posix_memalign or aligned_alloc, but instead uses CRYPTO_malloc and manually aligns the memory to ensure the consistency of allocation and release. (Architecture-related: public API)
  ↳ No PR: [8936052](https://github.com/openssl/openssl/commit/893605280e5794320d3c8205cd807e9704468145)
- Rolled back the API changes of OPENSSL_version and restored its original behavior. (Architecture-related: public API)
  ↳ No PR: [61c996f](https://github.com/openssl/openssl/commit/61c996f291c17bbfa2d18c1ac34668d2f3b854ca)
- Fixed the issue where SSL_get_event_timeout returns infinite timeout when the connection is not started. (Architecture-related: public API behavior fix)
  ↳ No PR: [b1f4aeb](https://github.com/openssl/openssl/commit/b1f4aebb74192afb197487bf6f4998fbb87cd1c1)
- Change the KU_constant to be defined by the corresponding X509v3_KU_constant, and add a comment to explain the bit order; at the same time, mark X509v3_KU_UNDEF as obsolete. (Architecture-related: public API: constant definition changes and obsolescence)
  ↳ No PR: [14bed67](https://github.com/openssl/openssl/commit/14bed67221c9fc7cef1cf2c1360f487ff2a78dd0)
- Migrate the implementation of OSSL_sleep() from the obsolete usleep() to nanosleep() on Unix platforms, retain the use of usleep() on DJGPP and TANDEM platforms, and provide the OPENSSL_USE_USLEEP macro as a fallback option. (Architecture-related: Platform compatibility: OSSL_sleep migrated to nanosleep)
  ↳ No PR: [f352c80](https://github.com/openssl/openssl/commit/f352c808edaaced8ba6a95cb440825094f2bb842)
- Migrate the compression method stack from the global variable of libssl to the OSSL library context to eliminate atexit calls in libssl. (Architecture-related: Architecture reconstruction: Migrate the compression method stack to the OSSL library context)
  ↳ No PR: [da9342e](https://github.com/openssl/openssl/commit/da9342ed5edabfbbd658e35f6bad1831682cc7e7)
- Added OSSL_ prefix to QUIC internal linked list operation macros to avoid conflicts with BSD API in system header files. (Architecture-related: internal API naming conflict)
  ↳ No PR: [009b2e2](https://github.com/openssl/openssl/commit/009b2e2a4c968b87d1f0dea02251a17e8103aeca)
- Add and update provider configuration tests, verify modulepath loading, and skip when the library does not exist. (Architecture-related: provider loading behavior)
  ↳ No PR: [91a77cb](https://github.com/openssl/openssl/commit/91a77cbf66c575345cf1eab31717e8edafcd1633), [b80fed3](https://github.com/openssl/openssl/commit/b80fed3f27ebe156b17246f7c12c5178cbe6834e)
- Enabled AES-XTS optimization on AIX systems. (Architecture-related: Platform compatibility: AIX)
  ↳ No PR: [dda1635](https://github.com/openssl/openssl/commit/dda1635cbff44d8d1b41a08e53c936ccb6c41acd)
- Optimized SSL certificate loading performance, using hash tables instead of linear searches in SSL_add_file_cert_subjects_to_stack and SSL_add_dir_cert_subjects_to_stack for certificate name deduplication, significantly improving the speed when loading a large number of certificates. (Architecture-related: public API: SSL certificate loading)
  ↳ No PR: [5cec58b](https://github.com/openssl/openssl/commit/5cec58bdfffeff89cce3cfc64e8e2cb709a8fa8e)
- Optimized the handling of conflicting entries when lock-free reading in the hash table, using the entire hash table instead of just the neighborhood for lookup, and updated related tests to support lock-free reading mode. (Architecture-related: core hash table implementation)
  ↳ No PR: [9f74898](https://github.com/openssl/openssl/commit/9f7489835d30d60e6a0365935c7009237710d96a)
- Disable DSA key generation in the FIPS provider, implemented through FIPS indicators. (Architecture event: FIPS indicator mechanism change)
  ↳ No PR: [49a35f0](https://github.com/openssl/openssl/commit/49a35f0f9283d13495941c47bb27ed1a0c32b109), [f98e49b](https://github.com/openssl/openssl/commit/f98e49b326fe1fda5efadc10e7905b09a394591c)
- Added enable-pie configuration option to support building location-independent executables to enhance ASLR security. (Architecture-related: build and installation methods)
  ↳ No PR: [1c4f968](https://github.com/openssl/openssl/commit/1c4f9684696bad3a602b388a414f2051f0365b3d)
- Fix multiple build issues on the VMS platform, including replacing incompatible function calls, adding necessary macro definitions, and handling compiler warnings. (Architecture-related: Platform Compatibility: VMS build fixes)
  ↳ No PR: [a19553c](https://github.com/openssl/openssl/commit/a19553cd872047289d6fc730a864bf9d984283ce)
- Removed all references to FLOSS in NonStop builds, because the SPT threading model build has been deprecated and FLOSS is no longer a dependency. (Architecture-related: Platform compatibility: NonStop build dependency changes)
  ↳ No PR: [0339382](https://github.com/openssl/openssl/commit/0339382abad578ccb3989799ea2fb99dfb2d099b)
- Fix VS2010 compilation error, replace static inline with ossl_inline macro to be compatible with older compilers. (Architecture-related: platform compatibility)
  ↳ No PR: [d8dd1df](https://github.com/openssl/openssl/commit/d8dd1dfdf5cf2343f6afd43dad4ce37045218624)
- Added type definition of uintptr_t for UEFI platform. (Architecture-related: public API)
  ↳ No PR: [7b33501](https://github.com/openssl/openssl/commit/7b33501a74ec2db4e54ddcd751dd42ded32bfd5b)
- Adapt all exporter files to use new variables in util/mkinstallvars.pl, making pkg-config files better utilize relative directory values. (Architecture-related: build and install methods)
  ↳ No PR: [30dc37d](https://github.com/openssl/openssl/commit/30dc37d798a0428fd477d3763086e7e97b3d596f)
- Modify the path acquisition function under the Windows platform: remove the fallback processing of OPENSSLDIR, ENGINESDIR, MODULESDIR and use macro definitions directly; change the default return value of ossl_get_wininstallcontext to UNDEFINED; and fix the wrong WININSTALLCONTEXT macro in the Windows CI configuration. (Architecture-related: platform compatibility)
  ↳ No PR: [4edcf0b](https://github.com/openssl/openssl/commit/4edcf0b450cd42d2037155d520b7e6323b624b6a), [525f2bf](https://github.com/openssl/openssl/commit/525f2bf564b3d04680ab5722fff575ce690d7aee)
- Update the Windows registry key path to be based on the major and minor version numbers instead of the full version string, allowing patch versions to share the same key. Also add a registry key setting step to the Windows CI workflow, and add a unit test to verify the registry key lookup function. (Architecture-related: version and compatibility)
  ↳ No PR: [caaea8f](https://github.com/openssl/openssl/commit/caaea8f343c63a828a5861650038b25de2d5983b), [1730918](https://github.com/openssl/openssl/commit/17309181613ae99b9a3d5cfefe76fd09e32d341b), [4fc9e5e](https://github.com/openssl/openssl/commit/4fc9e5e0110e7199eaca43f54d604e36ce579567), [aa4fc5e](https://github.com/openssl/openssl/commit/aa4fc5ea4a0da5f5f2c1fedf1f2727047d3a6eff)
- Fixed the problem in CMake export configuration that the directory resolution was empty due to the change of environment variable name, and updated the variable name to match the new build information. (Architecture-related: CMake export configuration)
  ↳ No PR: [c1a27bd](https://github.com/openssl/openssl/commit/c1a27bdeb9a4f915aa92ed0e74ed48a1f9b94176)
- Fix the calculation error of the internal variable _ossl_prefix in the OpenSSLConfig.cmake.in template so that it can work correctly under the build configuration. (Architecture-related: CMake export configuration)
  ↳ No PR: [a82d9e5](https://github.com/openssl/openssl/commit/a82d9e572cc757e4fa50d484bfbb7115f2d027dd)
- Repair and synchronize the export configurations of CMake and pkg-config, ensure that the include directory is correctly included when the build directory is separated from the source directory, and the variable naming is unified. (Architecture-related: build and installation methods)
  ↳ No PR: [accd835](https://github.com/openssl/openssl/commit/accd835f8d6ed946eb540a3e2e82f9723093f094), [15b7484](https://github.com/openssl/openssl/commit/15b748496faeebb3b6d8021049bccc93903ee322)
- Add NO_INTERLOCKEDOR64 macro detection for 32-bit MinGW builds and fix build failure issues. (Architecture-related: platform compatibility)
  ↳ No PR: [c94d13a](https://github.com/openssl/openssl/commit/c94d13a06965d4a3d9abf15d3cf5dc90c9d7c49c)
- Add openssl-3.3 and openssl-3.2 branch support to Coveralls build. (Architecture-related: build and installation methods)
  ↳ No PR: [7394de9](https://github.com/openssl/openssl/commit/7394de95b6856123808b70a492fa5b1e9ec3405d)
- Modify the macro definition of ANSI C compatibility check in CI workflow to improve compatibility. (Architecture-related: platform compatibility)
  ↳ No PR: [34f3547](https://github.com/openssl/openssl/commit/34f35473c06a91b82ce65cae952405a1bdb04dac)
- Included <sys/types.h> header file in e_os2.h to correctly use POSIX type ssize_t. (Architecture-related: platform compatibility)
  ↳ No PR: [8cf9ac9](https://github.com/openssl/openssl/commit/8cf9ac9c2034eb383b72bb7a849b5db96ff593f6)
- Deprecation macros defined for OpenSSL version 3.4. (Architecture-related: Versions and Compatibility)
  ↳ No PR: [0ce2a09](https://github.com/openssl/openssl/commit/0ce2a09ae6987901337187d89164edeb003a834c)
- Replaced many sprintf() calls with BIO_snprintf() and added a buffer size parameter to avoid compiler warnings and improve code safety. (Architecture-related: platform compatibility)
  ↳ No PR: [703f550](https://github.com/openssl/openssl/commit/703f55083189f1cc24adbf4a20787a4657ea7713)

### Legacy Provider
- Reconstruct DSA signature and verification implementation, add DSA+hash composite algorithm support, and enhance FIPS compliance check. (Architecture-related: public API)
  ↳ No PR: [bb2be4f](https://github.com/openssl/openssl/commit/bb2be4f066b73890207d19ed46f86cfb8e0f3ef0)
- Removed the alias relationship between DSA and dsaWithSHA1, and corrected the confusion between key algorithm and signature scheme. (Architecture event: ASN1_Core module change)
  ↳ No PR: [6eb6489](https://github.com/openssl/openssl/commit/6eb648941e3ca0fff08876d1d8b849ad2a6b300a)
- Replaced PKCS#1 v1.5 padding in the RSA key pair conformance test to no padding mode, and added corresponding self-test description constants. (Architecture-related: public API)
  ↳ No PR: [6c39d21](https://github.com/openssl/openssl/commit/6c39d21a4844cab997164454ece9b21186881f2a)
- Fixed the issue where the ASN1_item_verify_ctx function returns -1 instead of continuing execution when encountering an internal error or ASN1 library error. (Architecture-related: public API)
  ↳ No PR: [8d380f8](https://github.com/openssl/openssl/commit/8d380f85da215012570347f156e642d69909877a)
- Make the BN_generate_dsa_nonce function realize constant-time and unbiased random number generation, and add related internal auxiliary functions. (Architecture-related: constant-time implementation)
  ↳ No PR: [d7d1bdc](https://github.com/openssl/openssl/commit/d7d1bdcb6aa3d5000bf7f5ebc5518be5c91fd5a5)
- Change the ossl_gen_deterministic_nonce_rfc6979 function to constant time implementation to eliminate timing side channel risks. (Architecture-related: public API constant time implementation)
  ↳ No PR: [2d285fa](https://github.com/openssl/openssl/commit/2d285fa873028f6cff9484a0cdf690fe05d7fb16)
- Add strength parameter passing in the bnrand_range function to support safer random number generation. (Architecture-related: public API parameter changes)
  ↳ No PR: [13b3ca5](https://github.com/openssl/openssl/commit/13b3ca5c998e6db4f7251a56c43541cb1a422bd0)
- Optimize the calculation of shared power of 2 in BN_gcd, adopt constant time method, and add a new constant time selection function. (Architecture-related: constant time implementation)
  ↳ No PR: [aaa1bda](https://github.com/openssl/openssl/commit/aaa1bda7187c8d920cf9e426c2cf8ec7c1c65576)
- Strengthen the BN_GF2m_poly2arr function, reject invalid polynomials and correct the return value semantics, add tests. (Architecture-related: public API: BN_GF2m_poly2arr return value semantics correction)
  ↳ No PR: [c47d9d7](https://github.com/openssl/openssl/commit/c47d9d7ec81bbab339d102bded809a558d0ebe6a)
- Added CPACF function code and its required MSA level macro definitions for the s390x architecture. (Architecture-related: Platform compatibility: s390x CPACF support)
  ↳ No PR: [518b53b](https://github.com/openssl/openssl/commit/518b53b139d7b4ac082ccedd401d2ee08fc66985)
- Move the macro definitions of _XOPEN_SOURCE and _XOPEN_SOURCE_EXTENDED from the source file to the configuration target to avoid conflicts with definitions on other platforms. (Architecture-related: Build configuration: _XOPEN_SOURCE macro definition migration)
  ↳ No PR: [491bbb4](https://github.com/openssl/openssl/commit/491bbb444c4b654de14adc7031eb44e88a101edb)

### Default Provider
- Added parameter for AES GCM indicating whether IV is supported by internal generation. (Architecture-related: public API)
  ↳ No PR: [563c51c](https://github.com/openssl/openssl/commit/563c51cea0ad26f39a1acb5ef06f3c50c02fb265), [4c37778](https://github.com/openssl/openssl/commit/4c37778a4e8d59124b761a63a08ca0512b7067d2)
- Fixed a problem in SM2 encryption and decryption implementation: if KDF outputs all zeros during encryption, random numbers will be regenerated, and if KDF outputs all zeros during decryption, an error will be reported and exited. (Architecture-related: public API)
  ↳ No PR: [1706206](https://github.com/openssl/openssl/commit/170620675dfd74f34bdcf8aba71dffeb07f3d533)
- Fixed the problem that ECDSA_sign, DSA_sign and other functions may cause memory corruption due to non-deterministic signature length when passing in NULL as the sig parameter, and uniformly handled the situation where sig is NULL in the internal API. (Architecture-related: public API)
  ↳ No PR: [1fa2bf9](https://github.com/openssl/openssl/commit/1fa2bf9b1885d2e87524421fea5041d40149cffa)
- The use of XOF digest is prohibited in SM2 signature implementation. (Architecture-related: SM2 signature)
  ↳ No PR: [5ab9f7e](https://github.com/openssl/openssl/commit/5ab9f7e249f4b562a26809577d3aecfb4a1a9549)
- The 3DES cipher suite is no longer allowed for use in FIPS mode and has been removed from the FIPS flag for the associated cipher suite. (Architecture-related: FIPS Compliance)
  ↳ No PR: [3bbcd0c](https://github.com/openssl/openssl/commit/3bbcd0c537765dff63bb77774caa9331569cc6ae), [78f4374](https://github.com/openssl/openssl/commit/78f4374de165ca31582d337aad12c8d8572afd80)
- Added plausibility checks for parameters such as p, q, e, d relative to the modulus n for the RSA decoder, rejecting invalid keys and preventing timeouts. (Architecture-related: public API)
  ↳ No PR: [6dacee4](https://github.com/openssl/openssl/commit/6dacee485fad2c4d334e08af48891636205ddb6b)
- On s390x platforms, when HMAC calculations use digests provided by the engine, disable hardware acceleration to ensure that the engine's digest implementation is used correctly. (Architecture-related: Platform compatibility)
  ↳ No PR: [a75d626](https://github.com/openssl/openssl/commit/a75d62637aa165a7f37e39a3a36e2a8b089913bc)
- Fixed the HMAC digest detection on the s390x platform, using EVP_MD_is_a() instead of EVP_MD_get_type() to avoid skipping the HMAC acceleration path due to returning zero under the FIPS provider. (Architecture-related: platform compatibility)
  ↳ No PR: [d5b3c0e](https://github.com/openssl/openssl/commit/d5b3c0e24bc56614e92ffafdd705622beaef420a)
- Fixed prehash-by-caller processing of ED25519 and ED448 signatures and verification on the s390x platform, correctly falling back to the non-accelerated path when prehash or prehash-by-caller is enabled. (Architecture-related: Platform compatibility)
  ↳ No PR: [c23ce35](https://github.com/openssl/openssl/commit/c23ce3522540735e51e047f81a171c9261a1ed23)
- Fixed an error in the SHAKE squeeze operation on the s390x platform when data is not absorbed first, ensuring that the NIP flag is correctly set during the first squeeze; and added corresponding test cases. (Architecture-related: platform compatibility)
  ↳ No PR: [2b553ec](https://github.com/openssl/openssl/commit/2b553ec546716b3609c909f57cf42a0acbd01fce)
- Fixed an issue where the SHA3 absorption operation on the s390x platform caused subsequent hash output errors when zero-length data was used, skipping KIMD instruction calls without data and delaying state switching. (Architecture-related: platform compatibility)
  ↳ No PR: [bf4acc8](https://github.com/openssl/openssl/commit/bf4acc800c45a9f608dba8cafde83e6b59e18c54)
- Fixed incorrect detection of ECDH cofactor FIPS indicator and added test case covering all parameter combinations. The test is skipped when the curve is not supported by the FIPS provider. (Architecture-related: FIPS indicator behavior)
  ↳ No PR: [a9fe6f0](https://github.com/openssl/openssl/commit/a9fe6f05e9b23e6d2e5f6100c628396d4c659971), [eaae0c3](https://github.com/openssl/openssl/commit/eaae0c313f25fd0c11867fdf03c292275c8b0309)
- Fixed the handling of PBMAC1 when the PRF field in PBKDF2-params is missing, using hmacWithSHA1 by default. (Architecture-related: PKCS12 parsing behavior)
  ↳ No PR: [7aa93a6](https://github.com/openssl/openssl/commit/7aa93a6008f2828fe96d8c126038e9dd6c8171b5)
- Change the public key verification of known secure prime groups to partial verification to avoid unnecessary complete verification overhead. (Architecture event: Providers_Implementation module change)
  ↳ No PR: [e70e34d](https://github.com/openssl/openssl/commit/e70e34d857d4003199bcb5d3b52ca8102ccc1b98)
- Optimized the performance of the ChaCha20 stream cipher on the RISC-V platform, using both scalar ALU and vector ALU for acceleration, and added an implementation that only uses vector instructions (not relying on Zvkb extensions), and the runtime scheduling logic was adjusted accordingly to give priority to the Zvkb version. (Architecture-related: Platform compatibility: RISC-V)
  ↳ No PR: [da8b630](https://github.com/openssl/openssl/commit/da8b6308bd7ad5b7c779aa2d9123bf5faacaec7f), [03ce37e](https://github.com/openssl/openssl/commit/03ce37e11729bbe9964bd613c0eed6156b920208)
- Added HMAC hardware acceleration support to the s390x platform, using the CPACF instruction KMAC to accelerate SHA-224, SHA-256, SHA-384 and SHA-512 algorithms, and the performance can be improved by up to two times. (Architecture-related: Platform compatibility: s390x)
  ↳ No PR: [0499de5](https://github.com/openssl/openssl/commit/0499de5adda26b1ef09660f70c12b4710b5f7c8a)
- Introduced new modification bits for CPACF SHA3/SHAKE instructions on s390x platforms and conditionally skips ICV initialization to optimize short message processing performance and maintain backward compatibility. (Architecture-related: Platform compatibility: s390x)
  ↳ No PR: [25f5d7b](https://github.com/openssl/openssl/commit/25f5d7b85f6657cd2f9f1ab7ae87f319d9bafe54)
- Enabled SHA3 loop unrolling and EOR3 optimization for Ampere processors. (Architecture-related: Platform compatibility: Ampere)
  ↳ No PR: [e7f1afe](https://github.com/openssl/openssl/commit/e7f1afe4f7e799394684ce86bd98f2445031eb7f)
- On Windows platforms, return UNDEFINED when WININSTALLCONTEXT is not defined to avoid security risks. (Architecture-related: Platform compatibility)
  ↳ No PR: [f4540c1](https://github.com/openssl/openssl/commit/f4540c1b14cb6928daffc53f0db332cd741fe91d)

## Routine Changes

### New features
- Added -not_before and -not_after options for ca, req and x509 applications to explicitly set the start and end dates of certificate validity.
  ↳ No PR: [8120223](https://github.com/openssl/openssl/commit/8120223773d4c707dd43d9cc42a7fcab19609813)
- In s_client output, add a new line after the password line to show the protocol version alone.
  ↳ No PR: [dc6993a](https://github.com/openssl/openssl/commit/dc6993a625c3050125d8b69bcca05ef37555ebb3)
- Enable RSA-SM3 signature combination in default provider.
  ↳ No PR: [523187d](https://github.com/openssl/openssl/commit/523187df47cf6082004e872c6c47b202fce5d574)
- Added log tracking support for early data messages.
  ↳ No PR: [cc37ef7](https://github.com/openssl/openssl/commit/cc37ef7d90871f64a3f6bb5f42d20a7b88ebc6a3)
- Added ECDH key exchange demonstration program.
  ↳ No PR: [56e4d11](https://github.com/openssl/openssl/commit/56e4d112ae226d5fa0210cd1f0dd96e6857805fd)
- Added an MVP-level TLS server example that supports blocking mode and minimized session recovery.
  ↳ No PR: [f4b4a18](https://github.com/openssl/openssl/commit/f4b4a185b546044150821f1929e5cd6fd0dfba99)
- Added session_secret_cb callback test to ensure the connection is successfully established.
  ↳ No PR: [c8dddc6](https://github.com/openssl/openssl/commit/c8dddc61d49f84d1667de97e9548f07ccc92dddf)
- Add additional test cases for bn_gcd.
  ↳ No PR: [a6afe2b](https://github.com/openssl/openssl/commit/a6afe2b29a7b77956ef888653849f8cc38e39106)
- Removed SHAKE128 OAEP test cases that are no longer applicable and fixed build failures.
  ↳ No PR: [a0da3cb](https://github.com/openssl/openssl/commit/a0da3cb46848c3c5eb0c05e852662fea9a9a8502)

### bug fixes
- Fixed build failure caused by missing const qualifiers for function parameters when --strict-warnings is enabled, const qualifiers have been added for relevant parameters.
  ↳ No PR: [544fd23](https://github.com/openssl/openssl/commit/544fd23f0f95eea484850fe63835939aeb2bd824), [b0ebb87](https://github.com/openssl/openssl/commit/b0ebb87ab5cfdee3e272f5ff9596e8beba4571a6)
- Fixed the undefined behavior that may be caused by char type parameters when using the ctype.h function. By adding unsigned char cast, ensure that the parameters comply with the C standard requirements.
  ↳ No PR: [f2ddcf9](https://github.com/openssl/openssl/commit/f2ddcf9aaa032fccdc2be79c7bdc46cbce256e67)
- Fixed error handling in CMS_EncryptedData_encrypt and related functions to avoid memory leaks under abnormal paths.
  ↳ No PR: [6d2a01c](https://github.com/openssl/openssl/commit/6d2a01cdfb56fdb8ea5d5dd417724e6906c8b8e2)
- Allow handling of short reads in asn1_d2i_read_bio: when the actual number of bytes read is less than expected, continue the loop instead of reporting an error directly.
  ↳ No PR: [202ef97](https://github.com/openssl/openssl/commit/202ef97edc8e5561a6f4db28919d5ed73d411cc7)
- Fixed a double-free issue in the add_attribute function due to improper ownership transfer, moving the X509_ATTRIBUTE_create call to the end of the function to avoid subsequent errors.
  ↳ No PR: [82a13a1](https://github.com/openssl/openssl/commit/82a13a1f5053462f826bfb90061f0f77e3cc98a5)
- In ossl_ecdsa_deterministic_sign, the old processing of the sig parameter being NULL is removed, an error is returned directly, and a new check is added for the digestname parameter being NULL.
  ↳ No PR: [294782f](https://github.com/openssl/openssl/commit/294782f3b5c4b81d682e6e8608bb6e851177494d)
- Fixed crash due to null pointer when accessing PKCS7 encryption algorithm.
  ↳ No PR: [a4cbffc](https://github.com/openssl/openssl/commit/a4cbffcd8998180b98bb9f7ce6065ed37d079d8b)
- Fixed the syntax check failure of subjectAltName=dirName for the -addext parameter in the openssl req command, now using the correct configuration file for extended syntax verification.
  ↳ No PR: [3874188](https://github.com/openssl/openssl/commit/387418893e45e588d1cbd4222549b5113437c9ab)
- Fixed an error caused by AEAD password decryption not setting fake tag when running openssl speed -evp -decrypt. Added fake tag setting for decryption operation in default loop function.
  ↳ No PR: [b3be6cc](https://github.com/openssl/openssl/commit/b3be6cc89e4dcfafe8f8be97e9519c26af2d19f5)
- Added a null pointer check in the provider store API to prevent exceptions from being thrown when the open or attach methods are not provided at the same time.
  ↳ No PR: [bd73e1e](https://github.com/openssl/openssl/commit/bd73e1e62c4103e0faffb79cb3d34a2a92a95439)
- Fixed the problem in the PKCS#12 tool that the private key file was written before password verification, and the writing operation was postponed until after the imported password verification passed.
  ↳ No PR: [f546257](https://github.com/openssl/openssl/commit/f5462572a1873482ce38646cbf00dfc483f02068)
- Fixed the problem of unlimited growth of session cache in TLSv1.3: when copying a session, avoid copying the cache linked list pointer that may be modified concurrently, and add a dedicated copy function to ensure that the copy is recoverable; at the same time, when caching a session, check whether it has been marked as unrecoverable to prevent unrecoverable sessions from being added to the cache.
  ↳ No PR: [7984fa6](https://github.com/openssl/openssl/commit/7984fa683e9dfac0cad50ef2a9d5a13330222044), [03c4b0e](https://github.com/openssl/openssl/commit/03c4b0eab6dcbb59e3f58baad634be8fc798c103)
- Fixed crl and req commands not exiting with non-zero status when certificate verification fails.
  ↳ No PR: [6af739b](https://github.com/openssl/openssl/commit/6af739b79ba50bd42ac8934747ab5c8b996f16b6)
- Fixed the problem that the d2i function did not set the incoming pointer to null after the reference counting object was released in error handling to ensure that the caller can correctly determine the object status.
  ↳ No PR: [d550d2a](https://github.com/openssl/openssl/commit/d550d2aae531c6fa2e10b1a30d2acdf373663889)
- In tls_retry_write_records, log error information and trigger errors when system calls fail.
  ↳ No PR: [933f57d](https://github.com/openssl/openssl/commit/933f57dfe21657f7aba8f13e0cdb3b02dd64fcc3)
- The duality test for RSA key generation was replaced from PKCS#1 v1.5 encryption/decryption to PKCS#1 v1.5 signature generation and verification to comply with the NIST SP 800-131Ar2 standard.
  ↳ No PR: [9341e66](https://github.com/openssl/openssl/commit/9341e6683c341e809acca984e74728810586cba6)
- Fixed the error handling when EVP_MD_get_size returns a negative value in the create_digest function, treating non-positive numbers as errors and returning 0; at the same time, the memory release logic is merged into the err label to avoid *md_value leaks.
  ↳ No PR: [beb8217](https://github.com/openssl/openssl/commit/beb82177ddcd4b536544ceec92bb53f4d85d8e91)
- Added public key existence check when signing SM2 to avoid null pointer crash.
  ↳ No PR: [d6a8ade](https://github.com/openssl/openssl/commit/d6a8adeccdb8188517c5a84d35b79ef826176472)
- Fixed a null pointer dereference issue in the readbuffer_gets function due to missing argument checking.
  ↳ No PR: [c215d75](https://github.com/openssl/openssl/commit/c215d75f94fcaa598817e739221f33b71b53fb39)
- Fixed the integer overflow problem that may be caused by type mismatch in the ssl_cipher_get_overhead function, changed the local variable type from size_t to int, and added a validity check on the return value of the encryption algorithm.
  ↳ No PR: [4a50882](https://github.com/openssl/openssl/commit/4a5088259e78127354f497931568de409ac905fc)
- Fixed integer overflow and type conversion issues in TLS 1.3 PSK extension processing, changed the EVP_MD_get_size return value type to int and added validity check, and also corrected the error handling path.
  ↳ No PR: [48e3cf2](https://github.com/openssl/openssl/commit/48e3cf25a80db9a2991daccb0d8d1848065bca63)
- Fixed the integer overflow problem in the DANE TLSA addition function, by checking whether the return value of EVP_MD_get_size is negative or zero to avoid overflow during unsigned integer conversion.
  ↳ No PR: [165797c](https://github.com/openssl/openssl/commit/165797c7d829aa699f5cfdea4969cad0916e8cdf)
- In tls13_generate_master_secret, change the variable type that receives the return value of EVP_MD_get_size from size_t to int, and add a return value legality check to avoid integer overflow.
  ↳ No PR: [bcf81f7](https://github.com/openssl/openssl/commit/bcf81f742dded19321dc7f76c1d729f615f8656c)
- Fixed potential integer overflow issues caused by EVP_MD_get_size returning negative numbers in multiple modules, involving SSL/TLS, DRBG, KMAC, ECDSA, DSA, X509, SM2, timestamp, FFC parameter generation, RSA PSS and other components.
  ↳ No PR: [9f6a487](https://github.com/openssl/openssl/commit/9f6a48749afdcd5f35fb671651fc6af2b0b7d97a), [68d6dd3](https://github.com/openssl/openssl/commit/68d6dd3354597de01e7a9534be813756004e1351), [81f2b04](https://github.com/openssl/openssl/commit/81f2b0420abab47a7fd9fc9ef69309578115d342), [e97f468](https://github.com/openssl/openssl/commit/e97f468589e807e7f4722b150458edd53f374cd0), [df0ee35](https://github.com/openssl/openssl/commit/df0ee35b53a6cde959c119a165814d88e4492bb1), [f4174b6](https://github.com/openssl/openssl/commit/f4174b6db41650363e41af42e82de9cc7ef09a5e), [56e63f5](https://github.com/openssl/openssl/commit/56e63f570bd5a479439bc6f6a2499f6b86ded341), [64963c8](https://github.com/openssl/openssl/commit/64963c8b7a11728b5d252420f56f82532c14076d), [f5fde94](https://github.com/openssl/openssl/commit/f5fde94c54a1ad49663391750fd1b2f47550a4b6), [309c7ff](https://github.com/openssl/openssl/commit/309c7ffd17334a9f9f5b04286892f10a9aca8a2e), [e582b2b](https://github.com/openssl/openssl/commit/e582b2b22bcfbf5ed2b38de5fd1417013028614f)
- Fixed a memory leak in the OSSL_STORE_SEARCH_by_key_fingerprint function caused by not releasing allocated memory.
  ↳ No PR: [99fe4c1](https://github.com/openssl/openssl/commit/99fe4c10664c2287d34145457823edff3782e413)
- Fixed the issue where the module failed to load due to not being activated during configuration loading. Make sure the module path is set correctly from the template.
  ↳ No PR: [bc95959](https://github.com/openssl/openssl/commit/bc9595963a45e28e6a8b2de45a6719c252bd3a3d)
- Fixed a memory leak during provider initialization and an issue where resources were not released when module path setting failed.
  ↳ No PR: [4e3c1e6](https://github.com/openssl/openssl/commit/4e3c1e6206251c59855362d6d2edab4621c31dec)
- Always allocate and release locks for the provider's activatecnt_lock, ensuring that CRYPTO_atomic_add does not fail silently when a lock is needed.
  ↳ No PR: [2fd6c12](https://github.com/openssl/openssl/commit/2fd6c12e85ec7558cbdee08033f822c42ee0f5d4)
- Fixed an issue with duplicate allocation of mutex locks during RCU lock creation in Windows threads.
  ↳ No PR: [8e5918f](https://github.com/openssl/openssl/commit/8e5918fb8eb90289a0c89f6a4c6d623ecf49cf43)
- Fixed the memory leak problem of ossl_provider_new function on the wrong path.
  ↳ No PR: [875db35](https://github.com/openssl/openssl/commit/875db35ac63beb0e5a3d520743fa55ad2e5ccd1d)
- Fixed a memory leak caused by the list_provider_info function not releasing the providers collection on the wrong path.
  ↳ No PR: [993c240](https://github.com/openssl/openssl/commit/993c2407d04956ffdf9b32cf0a7e4938ace816dc)
- Fixed a memory leak in the CONF_modules_unload function caused by early creation of to_delete when new_modules allocation failed.
  ↳ No PR: [5bbdbce](https://github.com/openssl/openssl/commit/5bbdbce856c7ca132e039a24a315618484874c81)
- Fixed the reservation calculation of PING frames in QUIC TXP, added the txp_need_ping function to uniformly determine whether PING needs to be sent, and correctly applied this logic in the initialization and generation phases.
  ↳ No PR: [c3542b2](https://github.com/openssl/openssl/commit/c3542b22fa3f14d7b6c970d4b2c38a737d6ed8a4)
- Fixed the issue in HKDF that the key length was not set correctly when the initial key was empty, ensuring that the key length is valid and preparing for subsequent mandatory minimum key length requirements.
  ↳ No PR: [15d6114](https://github.com/openssl/openssl/commit/15d6114d99d93468876697b62d543b0e2efd45d5)
- Fixed an issue where the read buffer was incorrectly released when there are still unprocessed records or the application has not released all records, preventing potential security vulnerabilities.
  ↳ No PR: [38690ca](https://github.com/openssl/openssl/commit/38690cab18de88198f46478565fab423cf534efa)
- Fixed the use-after-free vulnerability: after releasing rl->packet, its pointer is nulled and the length is reset, and an assertion is added in the read function to ensure that the pointer is not null.
  ↳ No PR: [bfb8128](https://github.com/openssl/openssl/commit/bfb8128190632092b3a66465838b87b469455cec)
- Fixed potential null pointer dereference issue in hashtable caused by not checking pointer for null.
  ↳ No PR: [badda78](https://github.com/openssl/openssl/commit/badda78325dd961fa41a107796f2744ffbe8b265)
- Fixed the double release problem within the module_add function in conf_mod.c.
  ↳ No PR: [3059052](https://github.com/openssl/openssl/commit/3059052992ab61b0ba560ddf48111cecb5158ae2)
- Fixed a data race problem caused by checking the sorting status of X509 storage objects in the get_cert_by_subject_ex function without locking it correctly.
  ↳ No PR: [af75373](https://github.com/openssl/openssl/commit/af75373eeab6040aba243dd7629fb6f8244f2f5d)
- In BN_DEBUG mode, the top value of BIGNUM during EC/DSA nonce generation is corrected to avoid assertion failure in subsequent operations due to incorrect top.
  ↳ No PR: [a380ae8](https://github.com/openssl/openssl/commit/a380ae85be287045b1eaa64d23942101a426c080), [9c85f6c](https://github.com/openssl/openssl/commit/9c85f6cd2d6debe5ef6ef475ff4bf17e0985f7a2), [c0088b9](https://github.com/openssl/openssl/commit/c0088b993711a37516060abd42243feaf27c65b0)
- Fixed the timing issue of setting the server signature algorithm, moving it ahead of time before calling session_secret_cb to ensure that the certificate validity flag is correctly set; at the same time, the client compression method checking logic was optimized.
  ↳ No PR: [91c7ab2](https://github.com/openssl/openssl/commit/91c7ab27cebe4e6f6a6376e0a691736a2534fdd0)
- Add size pre-check before DSA parameter verification to avoid long calculations caused by too large parameters and fix the security vulnerability CVE-2024-4603.
  ↳ No PR: [85ccbab](https://github.com/openssl/openssl/commit/85ccbab216da245cf9a6503dd327072f21950d9b)
- On RSA key generation failure, clear and free the p and q members in the rsa structure to meet FIPS 186-5 standard requirements.
  ↳ No PR: [fb323b2](https://github.com/openssl/openssl/commit/fb323b27754089a34dc2a6a96a9b48cd4d0ee936)
- Fixed a memory leak caused by pkey_ctx not being released when initialization failed.
  ↳ No PR: [3e9d933](https://github.com/openssl/openssl/commit/3e9d933882407a0792dc3466ba9a0d53d40677a7)
- Added key matching support for hash tables to prevent errors caused by hash collisions.
  ↳ No PR: [435531e](https://github.com/openssl/openssl/commit/435531ec24ecdf00a5904f277bf3d2d9c6d63dd9)
- Fixed possible memory leak in OSSL_IETF_ATTR_SYNTAX_add1_value when handling unknown types.
  ↳ No PR: [cfaa79f](https://github.com/openssl/openssl/commit/cfaa79f837968cdf1b988e0f39cf2c31179c5740)
- Fixed potential memory leak in PKCS12_add_key_ex function.
  ↳ No PR: [7301759](https://github.com/openssl/openssl/commit/7301759afedffaf2f106495b3b171de9abfa2d2a)
- Fixed an issue that caused an internal error when selected_len was 0 in NPN extension processing, and instead returned a handshake failure alert.
  ↳ No PR: [c6e1ea2](https://github.com/openssl/openssl/commit/c6e1ea223510bb7104bf0c41c0c45eda5a16b718)
- Fixed the memory leak problem of frame_ack function in quic_trace.c to ensure that allocated memory is released correctly on the wrong path.
  ↳ No PR: [1977c00](https://github.com/openssl/openssl/commit/1977c00f00ad0546421a5ec0b40c1326aee4cddb)
- Fixed a crash caused by the RNG context being released after FIPS on-demand self-testing. Increase the reference count before self-testing to prevent early release.
  ↳ No PR: [42a8ef8](https://github.com/openssl/openssl/commit/42a8ef844e5fca55abb608beb62695abe80c6b6d)
- Fixed issues in RCU thread code: add OSSL_LIB_CTX parameter to ossl_rcu_lock_new function, and add operation to clear local keys in ossl_rcu_free_local_data.
  ↳ No PR: [f7252d7](https://github.com/openssl/openssl/commit/f7252d736da65ffa41cd81c6e0ec5ee58160eeb4)
- Fixed the data race caused by concurrent modification of the prev pointer during SSL_SESSION copying, and changed to copying only the security fields.
  ↳ No PR: [79886c8](https://github.com/openssl/openssl/commit/79886c85b378d73aec4d96f8e258f12915faddf7), [8d934a7](https://github.com/openssl/openssl/commit/8d934a75929d058bbc4566a6ebc9f804e1dd081f)
- Correct the return value when the extension is not sent in NPN extension negotiation so that it correctly returns the unsent status.
  ↳ No PR: [e10a3a8](https://github.com/openssl/openssl/commit/e10a3a84bf73a3e6024c338b51f2fb4e78a3dee9)
- Fixed the issue of incorrectly calling SSL_shutdown when SSL BIO is released during the initialization phase.
  ↳ No PR: [57b83ed](https://github.com/openssl/openssl/commit/57b83edc46926662491d63666231ba7ddc954a38)
- Fixed multiple style and error issues in the ossl_print_attribute_value function, including correcting the return value, avoiding modification of the attribute pointer, and simplifying BIO_printf return code conversion.
  ↳ No PR: [41c1b6f](https://github.com/openssl/openssl/commit/41c1b6f0a549f2a6401bf06c52badd482b6bd7bc)
- Fixed the problem that the context action type was not correctly set in the evp_pkey_ctx_setget_params_to_ctrl function to ensure that the value can be assigned correctly in a bidirectional translation scenario.
  ↳ No PR: [55c1458](https://github.com/openssl/openssl/commit/55c1458303c0fef88e4b2b35a090e9145f3e07eb)
- Fixed an issue where the OPENSSL_config function did not release appname memory after initializing encryption.
  ↳ No PR: [fbd6609](https://github.com/openssl/openssl/commit/fbd6609bb21b125c9454d07c484d166a33b4815b)
- Add error checking in ECDSA signature settings and signature functions when obtaining the group order result is empty, and replace some internal function calls for random number generation and zero value judgment.
  ↳ No PR: [16311db](https://github.com/openssl/openssl/commit/16311dbf53c464726d73b76d77ecf6275c9f9d08)
- Fix print_hex() function: correctly handle input of length 0, and use OPENSSL_buf2hexstr() instead of OPENSSL_buf2hexstr_ex() to solve the problem of insufficient buffer length.
  ↳ No PR: [b24a820](https://github.com/openssl/openssl/commit/b24a8200ab3e135c84dbf1054b92ffb713a7b5ad)
- Fixed the key type error used in the RSA encryption operation in the OpenSSL speed test and corrected the private key to the public key.
  ↳ No PR: [bb90a78](https://github.com/openssl/openssl/commit/bb90a7861cbf27e29790b66077c23a2e9805014b)
- Fixed the issue in ossl_engine_table_select where unlock is incorrectly called after the write lock fails.
  ↳ No PR: [3f4da93](https://github.com/openssl/openssl/commit/3f4da93678497fe64d262d03c388932f7ecfe74e)
- Fix data race between ossl_method_store_do_all and ossl_method_store_insert, store via clone algorithm and iterate in lock-free state.
  ↳ No PR: [d8def79](https://github.com/openssl/openssl/commit/d8def79838cd0d5e7c21d217aa26edb5229f0ab4)
- Avoid unnecessary -help prompts when adding duplicate extensions via -addext.
  ↳ No PR: [39424d9](https://github.com/openssl/openssl/commit/39424d960190706c913c7db2b97ec256aeba6173)
- Fix build errors under VS2010, move variable definitions to the beginning of functions to conform to coding style, and add null pointer checks.
  ↳ No PR: [20da3da](https://github.com/openssl/openssl/commit/20da3dabc43ee8c664090981336ec11605ff174b)
- Fixed the problem in ssl_conf.c that errors could not be correctly detected when using atoi to parse the input string. Instead, use OPENSSL_strtoul for safe conversion and verify whether the entire string is parsed correctly.
  ↳ No PR: [0b67643](https://github.com/openssl/openssl/commit/0b67643ade24286dddb0ce1b44a8a8c366e85ecb)
- Fixed a memory leak in the rsa_cms_sign function caused by a failed X509_ALGOR_set0 call, explicitly freeing the allocated ASN1_STRING object in the wrong path.
  ↳ No PR: [d0ee8ad](https://github.com/openssl/openssl/commit/d0ee8ada4dd12c17f7990feac17493ec1f931849)
- Fixed the line continuation logic in the configuration parser to ensure that backslash line continuations are correctly processed only in non-retry mode and avoid incorrect deletion of backslash characters in the middle of the line.
  ↳ No PR: [f54e4bc](https://github.com/openssl/openssl/commit/f54e4bc51b78c10dc99a61c087861ee2c11d7a41)
- Fixed the problem in KBKDF that the is_kmac flag cannot be reset after the MAC is set to KMAC, ensuring that it can work properly when subsequently switching to HMAC or CMAC.
  ↳ No PR: [f35fc4f](https://github.com/openssl/openssl/commit/f35fc4f184fa8a2088cd16648c4017fa321d6712), [90c3db9](https://github.com/openssl/openssl/commit/90c3db9e6a2bfbc1086d6d4b90d4fc7c7e565b93)
- Fixed a type conversion error in the opt_uintmax function, correcting a potential signed overflow problem to an unsigned type conversion.
  ↳ No PR: [a753547](https://github.com/openssl/openssl/commit/a753547eefc9739f341824a0cb0642afe7a06fcc)
- Fixed the problem that the negative return value of EVP_CIPHER_CTX_get_iv_length() was not checked in the tls13_cipher function to avoid potential errors.
  ↳ No PR: [a988704](https://github.com/openssl/openssl/commit/a98870414773baa9e8983d98ce61ad46d60c00ff)
- Fix possible memory leaks during reconnection, and clean up redundant null checks.
  ↳ No PR: [4fa9d1f](https://github.com/openssl/openssl/commit/4fa9d1f40fc85d8c70c93168dc812217db349359)
- Fix TLS extension label list, add missing early_data entry, and change array declaration to constant.
  ↳ No PR: [2432a9d](https://github.com/openssl/openssl/commit/2432a9da0334aa2385e86a47ccaff93b346e3fd3)
- Fixed an integer overflow problem that may be caused by BIO_write returning an error in the i2a_ASN1_OBJECT function. The subsequent dump operation will only be performed after the write is successful.
  ↳ No PR: [86fd4c1](https://github.com/openssl/openssl/commit/86fd4c1df91e58d316c863b5160d18c0f80dc6ac)
- Fix macro name error in fipsinstall for disabling DRBG truncate summary option.
  ↳ No PR: [d8783a1](https://github.com/openssl/openssl/commit/d8783a1807babff23e263386f97e361f4908616a)
- Fixed a memory leak problem in the show_digests function where the digest object obtained through EVP_MD_fetch was not released.
  ↳ No PR: [871c534](https://github.com/openssl/openssl/commit/871c534d39efecc2087da0fd24ff72e2712031a4)
- In deterministic ECDSA signatures, a clearer error message is now given when no digest is provided.
  ↳ No PR: [2f5308c](https://github.com/openssl/openssl/commit/2f5308cd4c40b50dc5d770cadfbeeed53376bafe)
- Removed unnecessary restrictions on settable parameters in ECDSA signature context, all settable parameters are now always allowed.
  ↳ No PR: [de98493](https://github.com/openssl/openssl/commit/de984934ddc2574acc304183d4e8b68b8123f87a)
- Fixed the issue of repeated colons in the display of otherName, and the extra colons have now been removed.
  ↳ No PR: [de8861a](https://github.com/openssl/openssl/commit/de8861a7e3100053542ec020aadd3f4fc88b7a02)
- Fixed issues with IPv6 address escaping processing in the proxy function and whitespace character matching in the no_proxy list.
  ↳ No PR: [55f0890](https://github.com/openssl/openssl/commit/55f089062bf6d1e15a6437bbb1ed759c4f3be575)
- Fixed the problem in RAND_write_file that may cause file descriptor leakage due to fdopen failure. Now the file descriptor will be closed and returned early when it fails.
  ↳ No PR: [d604834](https://github.com/openssl/openssl/commit/d6048344398ec75996fee1f465abb61ab3aa377e)
- Fixed a crash in ossl_print_attribute_value() due to unchecked ASN.1 types, now limiting DN syntax processing to sequence types.
  ↳ No PR: [7bcfb41](https://github.com/openssl/openssl/commit/7bcfb41489903543546d25ec13f8c58f36a147b3)
- In the RSA encryption implementation of the FIPS module, replace unapproved-checked function calls with corresponding macros so that macros are used correctly for instructions.
  ↳ No PR: [8e316ed](https://github.com/openssl/openssl/commit/8e316edd71a4cc480620b4c52e37114ca174f168)
- Fixed memory leak in speed application, make sure to release ecdsa_key object after using it.
  ↳ No PR: [8e82304](https://github.com/openssl/openssl/commit/8e82304adb8f51ed243ab1e57d8a4006bdbc0336)
- Fixed the req command no longer outputs a warning about reading certificate requests from standard input when standard input is redirected.
  ↳ No PR: [1d2cbd9](https://github.com/openssl/openssl/commit/1d2cbd9b5a126189d5e9bc78a3bdb9709427d02b)
- Fixed the problem of being unable to check the policy when the certificate stack is empty, and added early return to the empty stack.
  ↳ No PR: [8d28402](https://github.com/openssl/openssl/commit/8d28402ce38842e8aca9e0ce26ae44fa10c7b62e)
- Fixed a memory leak caused by not releasing the object when printing X509_NAME failed.
  ↳ No PR: [223e002](https://github.com/openssl/openssl/commit/223e0020e47e6e8eb6079258ea9d563d1d115132)
- Fixed the issue where the -async_jobs option in test mode would report an error when the system does not support asynchronous operation. It now returns success.
  ↳ No PR: [5111eac](https://github.com/openssl/openssl/commit/5111eacd50cf9a415b5891567fc6a930e7beeeff)
- Fixed a possible memory leak when the list of built-in signature algorithms in the list_tls_signatures function is an empty string.
  ↳ No PR: [47645bf](https://github.com/openssl/openssl/commit/47645bf7c63aaf08b764bfeaaa611c6673bb03a8)
- Fixed a memory leak in s390x_HMAC_CTX_copy caused by the buffer not being released when the target context already has one.
  ↳ No PR: [19b87d2](https://github.com/openssl/openssl/commit/19b87d2d2b022c20dd9043c3b6d021315011b45f)
- Fixed error handling when compression method is missing in client Hello, now returns the correct alert code according to the protocol specification.
  ↳ No PR: [c026101](https://github.com/openssl/openssl/commit/c026101be0c3c1a66b64d21d0e8c1ba39bcfd254)
- Fixed the alert type returned when receiving an invalid Change Cipher Spec value in TLS 1.3 and changed it to SSL_AD_UNEXPECTED_MESSAGE in compliance with RFC 8446.
  ↳ No PR: [c07a34e](https://github.com/openssl/openssl/commit/c07a34e18b098b77ce7ecb14273b7c75f59b5871)
- Fixed SM2 private key decoding bug, allowed SM2 private keys to be decoded using the id_ecPublicKey algorithm identifier, and added SM2 test cases.
  ↳ No PR: [25bd0c7](https://github.com/openssl/openssl/commit/25bd0c77bfa7e8127faafda2b082432ea58f9570)
- Fixed the problem that TLS keys were not recycled correctly in the thread event handling function, and added cleanup operations when creation failed and released.
  ↳ No PR: [20eb848](https://github.com/openssl/openssl/commit/20eb8485e7782687850aa6bda55f883acc432292)
- Fixed the digest validity check logic, corrected the incorrect condition md_nid < 0 or md_nid <= 0 to md_nid == NID_undef, ensuring that DSA, ECDSA and RSA signature providers correctly recognize invalid digests.
  ↳ No PR: [d1c2c05](https://github.com/openssl/openssl/commit/d1c2c054a4b585eed8c883367d80e2a972c4846f)
- Fixed edge cases in password callback processing: reserve a byte at the end of the buffer for a null terminator, and verify that the length returned by the callback does not exceed the buffer size to prevent out-of-bounds access from causing a crash.
  ↳ No PR: [f60bd99](https://github.com/openssl/openssl/commit/f60bd9992d35ef81513fcc92bac027d5eda82cd7)
- Fixed null pointer dereference and memory leak issues when EVP_MD_fetch() returns a null pointer in the PKCS#12 PBMAC1 implementation.
  ↳ No PR: [1425857](https://github.com/openssl/openssl/commit/142585706b0976591890895ce8d14f837fb55e01)
- Added missing error messages for tag length verification in the AES-OCB algorithm. When the tag length exceeds the maximum value, an invalid pointer is passed in encryption mode, or the custom tag length does not match the context, an explicit error code will now be returned.
  ↳ No PR: [ceee552](https://github.com/openssl/openssl/commit/ceee552964e4e1771cdff2ecaf94e011f6dff73b)
- Fixed the duplicate engine reference problem in ossl_ec_key_dup and removed unnecessary engine initialization and assignment.
  ↳ No PR: [a707a46](https://github.com/openssl/openssl/commit/a707a46b5a9fa50dd4a033a0a9dfe8a0994c38e4)
- Fixed the problem that the output length was not verified and incorrectly set in the RSASVE recovery operation, and added output length verification in the encapsulation operation.
  ↳ No PR: [9432935](https://github.com/openssl/openssl/commit/9432935b7a4599ce410e0dedc26f00915a42e857)
- Fixed the salt length parameter in TLS 1.3 HKDF key derivation, using the correct prevsecretlen instead of mdlen to avoid potential errors or crashes.
  ↳ No PR: [797691f](https://github.com/openssl/openssl/commit/797691f7d165d0efa86dbfaf1e961f08eb0a9875)
- Added ossl_prov_is_running checks for multiple FIPS provider functions to prevent output when the provider is in an error state.
  ↳ No PR: [5d2936a](https://github.com/openssl/openssl/commit/5d2936adda826b87ea7cfb7bad762bda5af3e56f)
- Fix potential memory leaks in the PKCS7_signatureVerify function to ensure that error paths correctly release the abuf buffer.
  ↳ No PR: [a6a3f9c](https://github.com/openssl/openssl/commit/a6a3f9c64b37a6db2804801a7b97c5bab1cdeaca)
- Fixed the memory leak caused by sk_ASN1_UTF8STRING_push failure in the save_statusInfo function, and added duplicate string release processing.
  ↳ No PR: [eb0430c](https://github.com/openssl/openssl/commit/eb0430c6ec006cdfc9346720df0f99c8dc984e7a)
- Fixed the memory leak caused by the incorrect path not releasing sess in the tls_parse_ctos_psk function.
  ↳ No PR: [93b9ba0](https://github.com/openssl/openssl/commit/93b9ba0a907952f662668a184398f9a319f9eeea)
- Fixed build failure of demos/sslecho example on OpenBSD, adding missing netinet/in.h header file.
  ↳ No PR: [01eaf20](https://github.com/openssl/openssl/commit/01eaf203856bfbb63051f8ecf56eae2d21132496)
- Fixed checking of zero-length digest values, treating them as errors.
  ↳ No PR: [e53a7cc](https://github.com/openssl/openssl/commit/e53a7ccd11c6aef965c50335187a473540819390)
- Fixed compilation warnings in multiple demo examples, changed functions and global variables to static and added error checking.
  ↳ No PR: [7a7fbeb](https://github.com/openssl/openssl/commit/7a7fbeb924a0b94459211ed3122050c07ebd20de)
- Fix uninitialized variable warning found by clang in CI, initialize readbytes to 0.
  ↳ No PR: [f2f13cf](https://github.com/openssl/openssl/commit/f2f13cff210a1b19cdd76dfab8739567535e2632)
- Fix the signal processing of the saccept example under the Windows platform, use signal() instead of sigaction, and declare the relevant functions as static.
  ↳ No PR: [7acdd77](https://github.com/openssl/openssl/commit/7acdd776e322814238c2c58296ecfcf0d16d5cf7)
- Fix the symbolic type of the addr_len variable in the sslecho example so that it matches correctly on platforms such as Cygwin.
  ↳ No PR: [6195c08](https://github.com/openssl/openssl/commit/6195c08d10484a79128cfba6cdbe9121f4247398)
- Fix the memory leak of the tls_provider_init function on the wrong path and ensure that resources are released correctly.
  ↳ No PR: [2a5d733](https://github.com/openssl/openssl/commit/2a5d733e64f009f758163da852f1e7fee6aea0a2)
- Fixed potential errors caused by unaligned memory access in the hashtable fuzzer and used memcpy to read data safely.
  ↳ No PR: [c04901b](https://github.com/openssl/openssl/commit/c04901be78768eb698d575d0b046940a5cb2aa5b)
- Fixed the reference to the wrong library in the error message, changing ERR_LIB_CMS to ERR_LIB_ESS.
  ↳ No PR: [2d29a8a](https://github.com/openssl/openssl/commit/2d29a8a7e8ef42050d2b08ca8cec9e4d9f0a0bb7)
- Fixed the memory leak of the test_thread_internal function in threadpool_test.c, and changed the failure path to jump to a unified cleanup label.
  ↳ No PR: [4dbd492](https://github.com/openssl/openssl/commit/4dbd4925dfc61d93df678df607504f62b0ac3dcc)
- Add validity check to the return value of EVP_MD_get_size in the add_entry function, and explicitly convert int to size_t.
  ↳ No PR: [45cada1](https://github.com/openssl/openssl/commit/45cada1339bacc81765b02367bdbaf878445081d)
- Fix the RC2 implementation so that it can handle both old and new algorithm identification parameter key names at the same time.
  ↳ No PR: [3b1ea04](https://github.com/openssl/openssl/commit/3b1ea04650edc113679e12ec8df49299ba6a60de)
- Add error checking for atomic load and store operations in hash tables to ensure correct returns or interruptions when operations fail.
  ↳ No PR: [9bd5e92](https://github.com/openssl/openssl/commit/9bd5e92aff83c24e0c6fdab1846340fae226dbb3)
- Fixed thread availability error message in Argon2 KDF to correctly display the number of requested threads and the number of available threads.
  ↳ No PR: [538d36e](https://github.com/openssl/openssl/commit/538d36e6572648c6cf33c552fdba93cbcb62cc67)
- Fixed old GCC build issues, and updated NonStop platform build documentation.
  ↳ No PR: [571ee17](https://github.com/openssl/openssl/commit/571ee17222a2343fa352a6b3dbac039a2d688cbc)
- Add NULL check for module_path in prov_config_test to fix the potential null pointer dereference problem discovered by coverage.
  ↳ No PR: [6ee369c](https://github.com/openssl/openssl/commit/6ee369cd6ec751c03879da56178e75e2691e08cb)
- Call tear_down in the early exit path of the test function test_encode_tls_sct to properly release resources.
  ↳ No PR: [264ff64](https://github.com/openssl/openssl/commit/264ff64b9443e60c7c93af0ced2b22fdf622d179)
- Add a null pointer check for the return value of CRYPTO_THREAD_lock_new in the test code to avoid potential null pointer dereferences.
  ↳ No PR: [327261c](https://github.com/openssl/openssl/commit/327261c076b8468382e1effea14d79446cc22b4d)
- Fix the link error caused by undefined snprintf in quic_multistream_test and use BIO_snprintf instead.
  ↳ No PR: [c02f952](https://github.com/openssl/openssl/commit/c02f952b48927af9fc4e991d7ead89a4cd1636bc)
- Fixed the problem of spurious error output in sysdefault tests, by adding options to handle and simplify test settings.
  ↳ No PR: [50153ad](https://github.com/openssl/openssl/commit/50153ad2bb767a6e79e5c0c569f136f723a32700)
- Add explicit sleep operation to QUIC test scripts to support cooperative threads.
  ↳ No PR: [b9e084f](https://github.com/openssl/openssl/commit/b9e084f139c53ce133e66aba2f523c680141c0e6)
- Add a check that the output pointer is NULL in the null_cipher function to avoid memory copying when the output buffer is empty.
  ↳ No PR: [61f3239](https://github.com/openssl/openssl/commit/61f32392dd67d47018ce46f427339e7191426e45)
- Change digest_size variable type from size_t to int, and add validity check for EVP_MD_get_size return value.
  ↳ No PR: [87e7470](https://github.com/openssl/openssl/commit/87e747000fef07c9ec43877bc5e9f2ca34f76a3b)
- Fixed multiple compilation warnings, including missing function prototype, unused variables, possibly uninitialized, and undefined behavior.
  ↳ No PR: [f94d773](https://github.com/openssl/openssl/commit/f94d773f9455a7b48158738106c5b676f1fd04ff), [7bc10f6](https://github.com/openssl/openssl/commit/7bc10f6ce2f91714d39a0410bfc545d79913e343), [d7af3f7](https://github.com/openssl/openssl/commit/d7af3f7aa7c0d311c472e65b00928771192e6a06), [c45ca06](https://github.com/openssl/openssl/commit/c45ca0656f8d1fe43b8cf444c88d295a063341ca)
- Unify the code style of threads_pthread.c and threads_win.c, unify the variable types to uint32_t, and fix a type conversion error.
  ↳ No PR: [ce6b2f9](https://github.com/openssl/openssl/commit/ce6b2f98263712b2ccb4559117cbd480c552894b)

### Refactoring optimization
- Optimize the processing logic of SSL_pending and SSL_has_pending in the QUIC protocol, correct the default stream creation behavior when writing with zero length, adjust the read wait function to support peek mode, and modify the write operation to return a WANT_READ error when no data is written.
  ↳ No PR: [da01235](https://github.com/openssl/openssl/commit/da01235692de643c990a34cae0f523a126be7573), [8cd3f34](https://github.com/openssl/openssl/commit/8cd3f34758b292e137ce112a09f566821549115d)
- Remove unnecessary underscores in the SSL alarm description string to make it consistent with other alarm description formats.
  ↳ No PR: [0af048e](https://github.com/openssl/openssl/commit/0af048e4c3113582329644fb2fb0abc596436c2e)
- Refactor the atomic operation fallback implementation, implement it separately by type to enhance type safety, and introduce the USE_ATOMIC_FALLBACKS macro for test builds.
  ↳ No PR: [a02077d](https://github.com/openssl/openssl/commit/a02077d4d7aeb0c99cc88cdfc7c131e48f98c4de)
- Hide the -w option and its related output in non-Windows builds, and adjust the display format of directory paths.
  ↳ No PR: [290452f](https://github.com/openssl/openssl/commit/290452f2bd7ba220a4a38a68371bfcd39765b1e9)
- Unified array size calculations to OSSL_NELEM macro.
  ↳ No PR: [001b92d](https://github.com/openssl/openssl/commit/001b92d68d61250c88b355773142af31675ca0ab)
- Remove function calls with unused return values.
  ↳ No PR: [940059d](https://github.com/openssl/openssl/commit/940059d545981017fffba9e8eeb9e52ee7f4cda0), [90849b5](https://github.com/openssl/openssl/commit/90849b520b3eef012e65075988b6538da39e2fa4)
- Replaced RSA multi-prime upper limit hardcoded value with macro RSA_MAX_PRIME_NUM.
  ↳ No PR: [a5e93f1](https://github.com/openssl/openssl/commit/a5e93f1c5b88528645d34ae176ad9a0dd94edd2b)
- Renamed internal variables to enhance code readability.
  ↳ No PR: [d534976](https://github.com/openssl/openssl/commit/d53497670d8a567fd6cb3687a1d6981ad2892870), [3de3d48](https://github.com/openssl/openssl/commit/3de3d481b269e9831d0b9abd3598b262647ae050)
- Remove unused SSL_ENC_FLAG_EXPLICIT_IV flag and related macro definitions.
  ↳ No PR: [125719b](https://github.com/openssl/openssl/commit/125719ba1190d2f3e0587221514ddfb8c5e11ef7)
- Clean up the code style in threads_pthread.c, including preprocessing directive alignment and unification of inline function declarations.
  ↳ No PR: [81f3934](https://github.com/openssl/openssl/commit/81f393498b333534111e320a33e3b244db06bbe9), [36ba419](https://github.com/openssl/openssl/commit/36ba419286843bcaeb497b3451540ab7587cf9d2)
- Change the context data flag variable from bit field type to integer type, and update the parameter types of related setting functions.
  ↳ No PR: [a008494](https://github.com/openssl/openssl/commit/a0084946f5fae86170d0169bdf1e5cc121531c22)
- Removed unimplemented librandom stub code.
  ↳ No PR: [05faa4f](https://github.com/openssl/openssl/commit/05faa4ffee7f20fcee129f77d153f2dcc609bdc8)
- Remove dead storage assignment in EVP_DecryptFinal_ex.
  ↳ No PR: [9fcf57b](https://github.com/openssl/openssl/commit/9fcf57b45985336b04579dd317d0dc990a9c062b)
- Remove redundant non-negative checks for block_padding and hs_padding.
  ↳ No PR: [32185d5](https://github.com/openssl/openssl/commit/32185d513cf8732ee0a85875ac61ee4389a86bbb)
- Increase the number of hash table expansion retries from 2 to 4.
  ↳ No PR: [8951ee0](https://github.com/openssl/openssl/commit/8951ee06b4344ddefd7758e0faf140e2bb64831a)
- Remove the unused parent_dispatch field in the DRBG structure.
  ↳ No PR: [2ddfef2](https://github.com/openssl/openssl/commit/2ddfef283d1f0e39238705c3fcdbcd343609cb9c)
- Optimize SSL_read buffer size usage in s_client to make full use of the allocated buffer.
  ↳ No PR: [03448ba](https://github.com/openssl/openssl/commit/03448ba21b5e720f59f7d349fcffd26c53323414)
- Add thread sanitizer compatibility for RCU locks to avoid false positives.
  ↳ No PR: [3bcac46](https://github.com/openssl/openssl/commit/3bcac46035d16e777c6651c18078bbcab27ad17a)
- Split the conditional judgment to avoid repeated calls to EVP_MD_get_size.
  ↳ No PR: [2b6f307](https://github.com/openssl/openssl/commit/2b6f307721db97d9bd7ca5ad4abf12b90ef581cd)
- Adjust reference count field position in SSL session structure and add lock protection annotation.
  ↳ No PR: [af82623](https://github.com/openssl/openssl/commit/af82623d32962b3eff5b0f0b0dedec5eb730b231)
- Remove sprintf call in nss_keylog_int, use memcpy instead, and eliminate dependence on stdio.h.
  ↳ No PR: [668fdb5](https://github.com/openssl/openssl/commit/668fdb593a9dcfe75718da6d59df67df87a92311)
- Optimize atomic reading in hash table deletion operations and use read-once semantics to reduce repeated calculations.
  ↳ No PR: [8e5cc43](https://github.com/openssl/openssl/commit/8e5cc43e74b32aca030a33e092b748addc564cd4)
- Simplified verification of DRBG allowed digests in FIPS mode, removing extra checks for XOF digests.
  ↳ No PR: [9c57eb7](https://github.com/openssl/openssl/commit/9c57eb736e9f4d63380d31f37c6c2a1fa267df9b)
- Extract the byte to hexadecimal code into a public function and optimize it for inline implementation to reduce duplicate code.
  ↳ No PR: [ca3c6f3](https://github.com/openssl/openssl/commit/ca3c6f38292ab1326af9fa414cfa8de4e30a4e82), [f21eded](https://github.com/openssl/openssl/commit/f21ededc3c04a5c899ee8522f7162abf637849a1)
- Delete unused internal event queue code and corresponding tests to reduce the size of libssl.
  ↳ No PR: [c0c4e6b](https://github.com/openssl/openssl/commit/c0c4e6ba0af309371cb7eb2a9f910829a8c01a70)
- Declare the four signature/verification functions in eddsa_sig.c as static to limit their scope.
  ↳ No PR: [dcc118c](https://github.com/openssl/openssl/commit/dcc118cde0fb9c90b973f9eb90006cec5bbeaa35)
- Refactor the signature provider context and change the algorithm identifier field from pointer to buffer storage.
  ↳ No PR: [8c9322e](https://github.com/openssl/openssl/commit/8c9322ea4df0fff93643419ae54583c2d5d1aae9)

### Test related
- Added -chunk option to evp_test test, supports processing data in chunks of specified size, overrides chunking logic in cipher, digest, signature, verification, encoding and MAC tests, and adds FIPS approval indicator checks.
  ↳ No PR: [0bfd744](https://github.com/openssl/openssl/commit/0bfd744f8d2b593455b11066cff59f3764bd313c), [2c8dc43](https://github.com/openssl/openssl/commit/2c8dc43bff22e0ce221157738cc1d6d31f3125f5), [1208d52](https://github.com/openssl/openssl/commit/1208d526d340b5869d5369d0d4930cc3576aabbb), [5f4983f](https://github.com/openssl/openssl/commit/5f4983f99b50b02392336da93ada70ea4f77b1eb), [fedbfff](https://github.com/openssl/openssl/commit/fedbfff42d790c7b7824351c35b4823c75da6417), [06da147](https://github.com/openssl/openssl/commit/06da14737369e7c90899aed4bb21cce9a0910d29)
- Added test cases for session buffer overflow and size limit.
  ↳ No PR: [4a3e8f0](https://github.com/openssl/openssl/commit/4a3e8f08306c64366318e26162ae0a0eb7b1a006), [0447cd6](https://github.com/openssl/openssl/commit/0447cd690f86ce52ff760d55d6064ea0d08656bf)
- Extended multi_resume test, adding the scenario of resuming the same session at the same time and marking it as unrecoverable.
  ↳ No PR: [cfeaf33](https://github.com/openssl/openssl/commit/cfeaf33a26c53c526128df96db2d2ec105b43aec)
- Fixed divide-by-zero errors, counter overflows and missing atomic operation locks in RCU and read-write lock tests.
  ↳ No PR: [d092208](https://github.com/openssl/openssl/commit/d092208bd694c9f9b276965bcf2d33f164535b2f), [b50c174](https://github.com/openssl/openssl/commit/b50c174ee3b11f916285046d52574ba653745083), [5f8b812](https://github.com/openssl/openssl/commit/5f8b812931e5da24df08913c05ff8e4f4494f014)
- Disable RCU tests on macOS to avoid random failures, and remove test_lib_ctx_load_config test.
  ↳ No PR: [1967539](https://github.com/openssl/openssl/commit/1967539e212c17139dc810096da987c8100b1ba2)
- Added attribute certificate, hash table and provider fuzz tester.
  ↳ No PR: [d10b020](https://github.com/openssl/openssl/commit/d10b020e2e389f4e5f5c84ce8d4512536dd3027a), [f597acb](https://github.com/openssl/openssl/commit/f597acb71b67bfa8f2e342301ebce2059408ac27), [f3b988d](https://github.com/openssl/openssl/commit/f3b988dc29512d6575ff435e1ff7c1b66d97051e)
- Moved the internal test function ossl_asn1_string_to_time_t to the test tool library and renamed it to test_asn1_string_to_time_t.
  ↳ No PR: [57bb112](https://github.com/openssl/openssl/commit/57bb112c07116d1cdbf5bc8562ebb3e7990f291c)
- Use OSSL_TIME functions instead of direct time_t arithmetic in test code.
  ↳ No PR: [afb6ce0](https://github.com/openssl/openssl/commit/afb6ce0d0f5b8e88f8b4f420aba0a8e59f58934f)
- Expand test cases for CRL reuse scenarios to cover more failure modes.
  ↳ No PR: [83951a9](https://github.com/openssl/openssl/commit/83951a9979784ffa701e945b86f2f0bc2caead8e)
- Add test cases for HMAC for multiple update calls and improve buffer safety for helper functions.
  ↳ No PR: [e113a92](https://github.com/openssl/openssl/commit/e113a92e290b31aaeab9a3f24b2cd6011c5ee670)
- Added multi-threaded hash table test case.
  ↳ No PR: [2a54ec0](https://github.com/openssl/openssl/commit/2a54ec0bdd76e93d2c1d92fc0b8e261ac0cea12d)
- Fix memory leak under wrong path in x509_test.
  ↳ No PR: [7cbca5a](https://github.com/openssl/openssl/commit/7cbca5a6d6e792c75c414e1f3fb22e2afae67988)
- Fixed occasional failures due to time sensitivity in early data testing and added a timeout detection mechanism.
  ↳ No PR: [1848c56](https://github.com/openssl/openssl/commit/1848c561ec39a9ea91ff1bf740a554be274f98b0)
- Add a check on the return value of EVP_MD_CTX_get_size() in bad_dtls_test to prevent integer overflow.
  ↳ No PR: [ef9ac2f](https://github.com/openssl/openssl/commit/ef9ac2f9b8b648406424c7c002fb94b0fae0434a)
- Add simple API tests for x509_acert, covering reading, printing, signing and verifying attribute certificates.
  ↳ No PR: [f90d97c](https://github.com/openssl/openssl/commit/f90d97caab451a49613742c09d3ec1e4e2dcf6bc)
- Fixed potential memory leaks in test files, and added path configuration test cases.
  ↳ No PR: [1405401](https://github.com/openssl/openssl/commit/140540189c67ba94188165b1144fdfb5b248bc02)
- In fuzz testing, parameter checking is also limited for DHX keys to avoid taking too long due to large parameters.
  ↳ No PR: [8d8a014](https://github.com/openssl/openssl/commit/8d8a0144303374f69f73fc944dd55c68600d15e5)
- Skip test cases relying on X25519 and X448 in FIPS mode.
  ↳ No PR: [0977eac](https://github.com/openssl/openssl/commit/0977eac5655138318a60a459a0d8de108dc614b5), [f6e4698](https://github.com/openssl/openssl/commit/f6e469808501f52c7e8f8679d6c3290cf1c258b3)
- Removed concurrent call test for OSSL_LIB_CTX_load_config.
  ↳ No PR: [fb65849](https://github.com/openssl/openssl/commit/fb6584987a43553b161b44fe9ede06651d4042f0)
- Fixed the memory leak caused by the SSL_SESSION object not being released in the wrong path in the test_bad_dtls test function.
  ↳ No PR: [abe05fd](https://github.com/openssl/openssl/commit/abe05fda8bdbfb35de7420cab31d5e459fabc874)
- Skip QUIC multi-stream testing when building OpenSSL with PUT threading model.
  ↳ No PR: [0e2567d](https://github.com/openssl/openssl/commit/0e2567d7293d3204de66acca0ed55bda4f0c0768)
- Fix memory leak in wrong path of test_curve function in ecstresstest.c.
  ↳ No PR: [434e7f7](https://github.com/openssl/openssl/commit/434e7f7cb4259f8c8c1463fd38fe723b3efca887)
- Fixed the resource leak problem of multiple test functions in cmp_hdr_test.c under wrong paths.
  ↳ No PR: [0986e12](https://github.com/openssl/openssl/commit/0986e128ff258d482cab712aa617a533db5588ea)
- Fixed ALPN data format error in QUIC test server, use correct ALPN data length.
  ↳ No PR: [fc8ff75](https://github.com/openssl/openssl/commit/fc8ff75814767d6c55ea78d05adc72cd346d0f0a)
- Add a new test case for ASN1_item_verify() and register it in the test framework.
  ↳ No PR: [2f0b497](https://github.com/openssl/openssl/commit/2f0b4974dfbd9bc71e1164e0742fc7fdb2b2b70e)
- Add test for X509 request version verification failure.
  ↳ No PR: [895ecd0](https://github.com/openssl/openssl/commit/895ecd0ce86c17fc696ad58c9f4b2ac1b821c5d4)
- Moved the inline PEM certificate in x509_req_test to an external file and added command line options to support specifying the certificate directory.
  ↳ No PR: [7d2c0a4](https://github.com/openssl/openssl/commit/7d2c0a4b1feb152ee1190dfedc65dfd1c928f9e5)
- Fix memory leak in x509_req_test.
  ↳ No PR: [a906436](https://github.com/openssl/openssl/commit/a9064366e8dcff56c722d0c8f1306d84d6c3f255)
- Lower the threshold for key checks in fuzz testing to avoid timeouts.
  ↳ No PR: [29696af](https://github.com/openssl/openssl/commit/29696af689df734cae05181d85ee04470c3839d3)
- Fix the validity of commands in quic-srtm fuzzer, add a limit on the maximum number of commands, and avoid timeouts.
  ↳ No PR: [4f619ca](https://github.com/openssl/openssl/commit/4f619ca622b6c36626ddc9a04b0b8589d7802dc0)
- Limit the number of commands that can be used in quic-lcidm fuzzer to avoid timeouts.
  ↳ No PR: [939dd47](https://github.com/openssl/openssl/commit/939dd479ac2c819da6cee21d00a21bfdb28d6eb2)
- Added Sign-Message and Verify-Message test types in the test framework, and added test cases for the RSA signature algorithm.
  ↳ No PR: [b02cf2f](https://github.com/openssl/openssl/commit/b02cf2fc8fc5ae2cef8313bac26b9a8fdbb98b2d)
- Add FIPS approval indicator support for TEST-RAND random number generator and always return non-FIPS status.
  ↳ No PR: [924321a](https://github.com/openssl/openssl/commit/924321a519861c3e78826c68909c2fe3481421c7)
- Added FIPS approval checks for random number generation, KDF and MAC testing.
  ↳ No PR: [df32ba9](https://github.com/openssl/openssl/commit/df32ba9e921f8cc06da94f414b437c8896520a58), [ba97722](https://github.com/openssl/openssl/commit/ba977226cf97724bd4f591a10ff6d4149e35b5e2), [4a002f5](https://github.com/openssl/openssl/commit/4a002f51f0e7e75b3b31b5e11df641bdbf4fcb4b)
- Fixed problems that may be caused by unchecked function return values in tests, including OSSL_PARAM_get_size_t, BIO_read and SSL_new return value checks.
  ↳ No PR: [9884568](https://github.com/openssl/openssl/commit/9884568569feb559cea2496a3326259a53db0860), [4811efe](https://github.com/openssl/openssl/commit/4811efe12fd1af9554718ae15996470a5c2ecd70), [18d491a](https://github.com/openssl/openssl/commit/18d491a6820e240a4ed4224c764a7c93b526e45f)
- Fixed memory leak caused by not releasing provider in test.
  ↳ No PR: [6e8a103](https://github.com/openssl/openssl/commit/6e8a1031ed11af9645769f9e019db9f032a220b8), [55662b6](https://github.com/openssl/openssl/commit/55662b674543c9385600bc9b7c46277ef69b4dba)
- Fix KDF tests failing due to behavior change, add version and availability condition markers in test data.
  ↳ No PR: [8fe150c](https://github.com/openssl/openssl/commit/8fe150cce805aa538a8d51d9f9fb932d23db9c90)
- Added a new test file to verify configuration lines that exceed 512 characters and contain backslashes.
  ↳ No PR: [2dd74d3](https://github.com/openssl/openssl/commit/2dd74d3acb9425251a2028504f07623bd97bfe87)
- Add unit tests for XOF digests that are not allowed.
  ↳ No PR: [db9eb0f](https://github.com/openssl/openssl/commit/db9eb0f96c24e2c6e739ab5a0f02bb9cf3dc81f3)
- Refactor the key generation test in evp_test to defer EVP_PKEY_CTX creation to runtime, change control parameters to settable parameters, and add EC key generation test support.
  ↳ No PR: [2a53830](https://github.com/openssl/openssl/commit/2a53830958b1e90231742e1d8ae0523d463560e3)
- Updated the EdDSA test to expect the OneShotDigestVerify operation without prehashing to return a verification error in FIPS 3.4.0 and above, and added a FIPS indicator test.
  ↳ No PR: [09eaf16](https://github.com/openssl/openssl/commit/09eaf16771fe5b5b57cac0ddfd6bf8ca3584134b)
- Add meaningful description messages for skip conditions in test_large_app_data tests.
  ↳ No PR: [449bc10](https://github.com/openssl/openssl/commit/449bc104c80e6c3cbf0ff991ef9dd4ac67c02798)
- Fixed an issue in evp_test where the FIPS approval check failed when the FIPS provider had no parameters available.
  ↳ No PR: [7f8ff7a](https://github.com/openssl/openssl/commit/7f8ff7ab140549a768a531d15189e54d56e52822)
- Fixed the padding mode setting when generating signatures in acvp_test, and added a verification message checking function.
  ↳ No PR: [878f74e](https://github.com/openssl/openssl/commit/878f74eb080bf3c7c05df138fb61d9e08f7da5b3)
- Limit input split length to no more than 512 bytes in fuzz testing to prevent infinite loops caused by large number operations.
  ↳ No PR: [f076837](https://github.com/openssl/openssl/commit/f0768376e1639d12a328745ef69c90d584138074)
- Fixed an integer overflow problem that may occur when reading large files in the read_all function in cmsapitest.
  ↳ No PR: [31cd9cd](https://github.com/openssl/openssl/commit/31cd9cd830f847c0effc7c15b814f890228c3739)
- Fix duplicate free and unused variables issues for KeyGen tests in evp_test.
  ↳ No PR: [a595d62](https://github.com/openssl/openssl/commit/a595d624c896ace0eae017ad88268fa4c686b374)
- Fix provider compatibility CI, add FIPS version check in rand_test.c, and skip tests of incompatible versions.
  ↳ No PR: [d357e54](https://github.com/openssl/openssl/commit/d357e5476a08d1eb5fe5461eb9b60d6b366dc6ba)
- Add error cause descriptions and enhanced diagnostic information for multiple test data files (RSA, KMAC, HKDF, PBKDF2, SSHKDF, Single Step KDF, TLS 1.2 PRF, TLS 1.3 KDF, X9.42, X9.63 KDF, TLS 1 PRF).
  ↳ No PR: [068c9be](https://github.com/openssl/openssl/commit/068c9bee37c0a9ed99b30abe7718eae007b07455), [77915ae](https://github.com/openssl/openssl/commit/77915ae8eb55469852eb7269b674eb979c479b15), [8c24acd](https://github.com/openssl/openssl/commit/8c24acda1801a99f1aa69d9ff90019301606266e), [bb3b3ab](https://github.com/openssl/openssl/commit/bb3b3abfd5d54812f67c5090b28b4599d0d3f17a), [2028490](https://github.com/openssl/openssl/commit/20284908c449c2544861ad6df325d616263c62f8), [3cccd17](https://github.com/openssl/openssl/commit/3cccd17eed36fc9e87f53576c0831e67d7e35770), [a969c46](https://github.com/openssl/openssl/commit/a969c466b1bbf899166db2bc1cc663b961e16ee1), [41a9aeb](https://github.com/openssl/openssl/commit/41a9aeb6722b63031ef6319170751f5f92bba5b6), [0acf9f8](https://github.com/openssl/openssl/commit/0acf9f89344aea7cef0372753849bc464d1358ad), [90f64d0](https://github.com/openssl/openssl/commit/90f64d064ece725f832dbd8ded300ac0dbeea5c6), [dc16db6](https://github.com/openssl/openssl/commit/dc16db61f1018a2357bfd8ba78b58762f3eb00fe)
- Added forward test cases for DRBG for FIPS indicator failures and adjusted the order of version tags in the test data files.
  ↳ No PR: [fb51e4f](https://github.com/openssl/openssl/commit/fb51e4f61158a78995cd0f950e6f3d8a6f3d3d8b)
- Undo the changes that skipped specific tests due to the FIPS provider version and resume normal execution of the tests.
  ↳ No PR: [357e326](https://github.com/openssl/openssl/commit/357e3265a4280bb644f1ea6d164934b68f68f302)
- Add default value to greeting variable in test function to avoid printing null pointer.
  ↳ No PR: [34877db](https://github.com/openssl/openssl/commit/34877dbcd467efb4e2dbf45d2fcb44c5a4b4926a)
- Roll back the changes in evp_test that caused FIPSversion to skip the default provider and use Availablein instead.
  ↳ No PR: [f2a5c80](https://github.com/openssl/openssl/commit/f2a5c80ca41e5b5b744cf3485c23366404861e3e)
- Added Availablein=fips attribute for FIPS related test cases in multiple EVP test data files.
  ↳ No PR: [32b43b9](https://github.com/openssl/openssl/commit/32b43b9160cfcbb2940a0666869a680db827b892)
- During fuzz testing, hash table insertion is allowed to return -1 due to too many collisions and exit early to enhance robustness.
  ↳ No PR: [3c1713a](https://github.com/openssl/openssl/commit/3c1713aeed4dc7d1ac25e9e365b8bd98afead638)
- Avoid running SM2 tests under the 3.0.0 FIPS provider to prevent test failures.
  ↳ No PR: [0b97a55](https://github.com/openssl/openssl/commit/0b97a5505efa8833bb7b8cabae45894ad6d910a2)
- Added BIO password callback function test suite, covering boundary scenarios such as negative return values, zero-length passwords, buffer boundaries and passwords containing null bytes.
  ↳ No PR: [750028c](https://github.com/openssl/openssl/commit/750028cc51af1713aff815373e19807160b8d0b7)
- Fixed the FIPS 3.0.0 version checking logic in the test to avoid incorrectly skipping the SM2 test when the FIPS provider is not loaded.
  ↳ No PR: [c6c6af1](https://github.com/openssl/openssl/commit/c6c6af18ea5f8dd7aa2bd54b63fcb813ee6c2394)
- Clean up redundant non-negativity checks in test code and remove unnecessary checks on unsigned variables.
  ↳ No PR: [934f9a0](https://github.com/openssl/openssl/commit/934f9a0224697a82f1f36f7c1c5588316e69a1f9)
- Fixed the null pointer dereference problem that may occur in the test, and moved the certificate assignment operation to the conditional branch to ensure safety.
  ↳ No PR: [0f6ff92](https://github.com/openssl/openssl/commit/0f6ff92e67f2bbb1cda222dbe333cdf3cbaf4989)
- Adjust the EVP_PKEY encapsulation/decapsulation test case to ensure that the output length is correctly obtained and add related tests.
  ↳ No PR: [e6d404c](https://github.com/openssl/openssl/commit/e6d404c9078e77239ba2230bb74dab770b780320)
- Added KMAC, FIPS indicator and short salt length test cases for SSKDF, and fixed a typo in a function declaration in fipscommon.h.
  ↳ No PR: [95994de](https://github.com/openssl/openssl/commit/95994ded9596e920c5d81dd7b4d13d95c88be268)
- Added test mode to the speed application so that it only runs one iteration and returns an error code on failure.
  ↳ No PR: [9309b0b](https://github.com/openssl/openssl/commit/9309b0b8c778fcdb0e1bd08522f694be1e963eb5)
- Refactor the callback test code, use local structures instead of global variables, and refactor password variables into const char[] arrays.
  ↳ No PR: [db39748](https://github.com/openssl/openssl/commit/db3974808181e300053bd37458adfb1706f4c91f), [66e6809](https://github.com/openssl/openssl/commit/66e6809c100b3755d538a410fb90c1772a9ef6c9)

### Performance optimization
- Allow custom initialization of group methods and add a precomputed implementation for the P256 curve, avoiding expensive Montgomery arithmetic structure initialization, thereby significantly speeding up the TLS handshake.
  ↳ No PR: [23b6ef4](https://github.com/openssl/openssl/commit/23b6ef4894679aa0278c93de29007d1e695856ee)
- Optimize the public key check function to skip unnecessary expensive calculations when the cofactor is 1, because the point on the curve already implies that the factorial point is infinity.
  ↳ No PR: [b916940](https://github.com/openssl/openssl/commit/b916940752e4de5922553b1cf482687dfc653f7a)
- Fixed memory leak on wrong path in module_init and make_addressPrefix functions in conf_mod module.
  ↳ No PR: [a928f26](https://github.com/openssl/openssl/commit/a928f26813e41018d364a5178c53ebb6d49d3e59), [682ed1b](https://github.com/openssl/openssl/commit/682ed1b86ebe97036ab37897d528343d0e4def69)
- Fix memory leaks and use-after-free issues in evp_test.
  ↳ No PR: [deaa83a](https://github.com/openssl/openssl/commit/deaa83af700113c99835a1db7d45d33baba05bd3)
- Performance optimization of the hash table implementation, including adding memory prefetch instructions and reducing the number of buckets of the namemap hash table from 4096 to 2048 to save memory.
  ↳ No PR: [14efc05](https://github.com/openssl/openssl/commit/14efc05314ce1bd8e8988d02f69a819a4e0a56ab), [f0b1d4d](https://github.com/openssl/openssl/commit/f0b1d4d1b055bc87b26bb9bbfee437b12f0a4c89)

### Security related
- Strengthen the handling of unrecoverable sessions to prevent accidental use of unrecoverable sessions.
  ↳ No PR: [21df7f0](https://github.com/openssl/openssl/commit/21df7f04f6c4a560b4de56d10e1e58958c7e566d)
- Add a check on the return value of the digest size acquisition function in the RSA signature implementation to prevent integer overflow.
  ↳ No PR: [6c0f154](https://github.com/openssl/openssl/commit/6c0f154750a3380cced8ddab44d7ad100b6ab984)
- Add checking and type conversion for the return value of EVP_MD_get_size() in the hmac_drbg_kdf_set_ctx_params function to avoid integer overflow.
  ↳ No PR: [7638f40](https://github.com/openssl/openssl/commit/7638f4016a9438dccaf183a3ae7353d363dfc25a)
- Add checks on the return value of EVP_MD_get_size() in RSA signature, verification, control and PSS initialization functions to avoid integer overflow.
  ↳ No PR: [882a387](https://github.com/openssl/openssl/commit/882a387d0dc12afe8612c4d3f6b9cae5c04611d7)
- Add checks on the return value of EVP_MD_get_size() in DSA signature and verification functions to avoid integer overflow.
  ↳ No PR: [15e06b1](https://github.com/openssl/openssl/commit/15e06b12ee9df6347433398cb3f732c4458d4218)
- Added lower bound checking for plaintext and ciphertext in RSA padding-free mode, compliant with SP800-56Br2 specification.
  ↳ No PR: [4514e02](https://github.com/openssl/openssl/commit/4514e02cdfc96589d5e8ab0a08942fafa8e418ae)
- Fixed a type error in certificate name checking to prevent denial of service vulnerability (CVE-2024-6119).
  ↳ No PR: [0890cd1](https://github.com/openssl/openssl/commit/0890cd13d40fbc98f655f3974f466769caa83680)
- Fixed the heap buffer overflow problem caused by shrinkage during hash table iteration, and prevented shrinkage by temporarily setting the load factor to 0.
  ↳ No PR: [01753c0](https://github.com/openssl/openssl/commit/01753c09bbfdffcefd555b4c21e50e68af346129)
- Fixed potential integer underflow issue caused by negative unchecked digest length return value in RSA OAEP padding check.
  ↳ No PR: [22e08c7](https://github.com/openssl/openssl/commit/22e08c7cdc596d4f16749811d1022fb8b07a8e41)
- Fixed the problem in asn1parse_main that the length value may overflow due to loop reading of BIO, and added overflow check.
  ↳ No PR: [5006623](https://github.com/openssl/openssl/commit/50066236eb3b31c93aaa935ca38f5cc1ec056696)
- Add integer overflow check when length accumulation in i2d_name_canon function.
  ↳ No PR: [b2deefb](https://github.com/openssl/openssl/commit/b2deefb9d262f0f9eae6964006df98c2fa24daac)
- Fixed the integer overflow problem that may occur in the do_print_ex function, and added overflow check for output length calculation.
  ↳ No PR: [e3e15e7](https://github.com/openssl/openssl/commit/e3e15e77f14cc4026fd456cc8a2b5190b2d79610)
- Fix integer overflow problem in RSA-PSS salt length calculation, add validity check, and set verification message flag in FIPS mode.
  ↳ No PR: [217e215](https://github.com/openssl/openssl/commit/217e215e99dd526ad2e6f83601449742d1d03d6a)
- Allow customization of FIPS provider vendor name prefix via VERSION.dat.
  ↳ No PR: [8945f40](https://github.com/openssl/openssl/commit/8945f406a73a01862695a424679f9440f592604b)
- Update CHANGES.md and NEWS.md to record security fixes for CVE-2024-4741 and CVE-2024-4603.
  ↳ No PR: [ae20c42](https://github.com/openssl/openssl/commit/ae20c423f9b86956267ea82bd678179e9d648bad)
- Add regression test cases that trigger CVE-2011-4354 for ECC test data.
  ↳ No PR: [77a30b7](https://github.com/openssl/openssl/commit/77a30b70ebe4dc8fbcb9ed718201d26114b86ebd)
- Expand the SSL_free_buffers test and add test cases for scenarios where buffers should not be released and pipelining scenarios.
  ↳ No PR: [566f306](https://github.com/openssl/openssl/commit/566f3069169b9fab4fbb23da98c3c91730dd5209), [c1bd38a](https://github.com/openssl/openssl/commit/c1bd38a003fa19fd0d8ade85e1bbc20d8ae59dab)
- Migrate the auxiliary function for loading dasync engine to the public test library so that it can be reused by other tests.
  ↳ No PR: [0575247](https://github.com/openssl/openssl/commit/05752478df623a9ddf849f897b630c1e0728cb7c)
- Modify variable types to avoid integer overflow and improve security.
  ↳ No PR: [f13ddaa](https://github.com/openssl/openssl/commit/f13ddaab69def0b453b75a8f2deb80e1f1634f42)

### Documentation
- Added a documentation policy link to the contribution guide to help contributors understand documentation writing practices.
  ↳ No PR: [e817766](https://github.com/openssl/openssl/commit/e817766c0f46f371fabe344fba60d13afcfc3da9)
- Synchronously updated CHANGES.md and NEWS.md to record changes in OpenSSL 3.4, including new features, improvements, FIPS 140-3 indicators, and removal of obsolete entries.
  ↳ [#25626](https://github.com/openssl/openssl/pull/25626): [ec6991f](https://github.com/openssl/openssl/commit/ec6991fce08711b4c1737474d4ef1cd4c784fa47), [51b2e16](https://github.com/openssl/openssl/commit/51b2e16475d0fb7195993271518f7565235ada08) | [#25766](https://github.com/openssl/openssl/pull/25766): [98acb6b](https://github.com/openssl/openssl/commit/98acb6b02839c609ef5b837794e08d906d965335) | No PR: [eb33768](https://github.com/openssl/openssl/commit/eb33768e879554884b34f640e8c14ba3738a8eff), [5139b51](https://github.com/openssl/openssl/commit/5139b51cea6791c68630fbd0cb1d263a48674a96), [5650289](https://github.com/openssl/openssl/commit/56502897431d785ab93cdffd6857a667fe2b6d20), [a1d2fd0](https://github.com/openssl/openssl/commit/a1d2fd06655d41a6b1d000f86e942ead9e3297ca), [3f2d16f](https://github.com/openssl/openssl/commit/3f2d16fe972cdc837493d8439a33769e87c13b01)
- Updated the Valgrind usage documentation, improved the list format, added hyperlinks, and updated the command substitution syntax to $() form.
  ↳ No PR: [35950ce](https://github.com/openssl/openssl/commit/35950cea02292ad63b24a928e40ec1d35542bcd1)
- Updated documentation for the crl and req commands to note that the -verify option exits with exit code 1 when verification fails and is implicitly enabled when -CApath, -CAfile or -CAstore is specified.
  ↳ No PR: [15585af](https://github.com/openssl/openssl/commit/15585af97ec682182f40f815741e66f1ec40f941), [a16f2e7](https://github.com/openssl/openssl/commit/a16f2e7651b22ee992bb0c279e25164b519c1e80)
- Updated the Windows platform documentation to explain that OPENSSLDIR, ENGINESDIR and MODULESDIR paths can be defined through the registry at runtime, and added a registry behavior summary table.
  ↳ No PR: [7c58769](https://github.com/openssl/openssl/commit/7c58769a036057f7a595c83db65e74175c116477), [62dd0f1](https://github.com/openssl/openssl/commit/62dd0f1762c9c5dd1df5f4220adec0fe5661c7c9)
- Added badges for daily check status and provider compatibility status in README.
  ↳ No PR: [f965632](https://github.com/openssl/openssl/commit/f96563297ee04d57efd45f56bd6b897d809214b4)
- CVE-2024-6119 security fix documented in CHANGES and NEWS documentation.
  ↳ No PR: [ca979e8](https://github.com/openssl/openssl/commit/ca979e854b2ac847c3abdf10a6c61b569611b6ae)
- Added CVE-2024-5535 security advisory entry to CHANGES and NEWS documents.
  ↳ No PR: [03b22b4](https://github.com/openssl/openssl/commit/03b22b4d7370a3ddf2c1723c2ff4dc3d169ea897)
- Added missing link to OpenSSL 3.4 version chapter in NEWS.md.
  ↳ No PR: [465925d](https://github.com/openssl/openssl/commit/465925d781ac5725ab24693aa3d26bdc3aa08683)
- Added comment to RSA KEM's encapsulation and decapsulation operations stating that the outlen parameter must report the length of the output buffer to ensure the buffer size is sufficient.
  ↳ No PR: [20e9e51](https://github.com/openssl/openssl/commit/20e9e51e5399fa8df96bb8ad63e0d19364c59df0)
- Improved documentation of newline handling for base64 encoding/decoding in openssl-enc command.
  ↳ No PR: [b1e7bc5](https://github.com/openssl/openssl/commit/b1e7bc5bdfc73ef841afa30ac321975b0d63219a)
- Added design documentation for FIPS indicator requirements.
  ↳ No PR: [a8e6aaa](https://github.com/openssl/openssl/commit/a8e6aaada3350fe0a864d1153f8939cde90b0b76)
- Updated documentation for the string_mask option of the openssl req command to be consistent with actual behavior.
  ↳ No PR: [2410cb4](https://github.com/openssl/openssl/commit/2410cb42e62c3be69dcf1aad1bdf1eb0233b670f)
- Fixed a description error in the FIPS HMAC key documentation regarding default key values.
  ↳ No PR: [53ef123](https://github.com/openssl/openssl/commit/53ef123f48d402aff7c27f8ec15191cb1cde4105)
- Added design documentation to discuss how to handle certain MAX macro definitions.
  ↳ No PR: [de8e79e](https://github.com/openssl/openssl/commit/de8e79e06436d8d0b48c785e24c5d07e0ba641e3)
- Make it clear in the documentation that the -keys option is only used to select private keys, there is no public key selector.
  ↳ No PR: [693c479](https://github.com/openssl/openssl/commit/693c479a2ca671e0dfca8d1ad14e789169b982ff)
- Added fingerprints for future OpenSSL release keys to documentation.
  ↳ No PR: [4ffef97](https://github.com/openssl/openssl/commit/4ffef97d3755a0425d5d72680daebfa07383b05c)
- Added installation documentation and instructions for ANSI C and POSIX dependencies.
  ↳ No PR: [4e8c4b7](https://github.com/openssl/openssl/commit/4e8c4b77ef7480b80de1971d8862300c366015e9)
- Documented that SHAKE-128 and SHAKE-256 no longer have a default digest length, and the xoflen parameter must be set before use.
  ↳ No PR: [ad3f28c](https://github.com/openssl/openssl/commit/ad3f28c5fbd5dcbc763a650313fd666b0e339cca)
- Removed the SSL_set_session_secret_cb function from the missing documentation list, indicating that documentation has been added for this function.
  ↳ No PR: [aecaacc](https://github.com/openssl/openssl/commit/aecaaccaf93c4b36dd830accf08f2175059c5782)
- Synchronously updated the OpenSSL 3.3 branch version change record in the CHANGES.md file.
  ↳ No PR: [e91579d](https://github.com/openssl/openssl/commit/e91579db0972bc8fe89e1060369c58f3dcfaafe7)
- Added documentation for PBMAC1 support for PKCS#12, including instructions for the new -pbmac1_pbkdf2 and -pbmac1_pbkdf2_md command line options.
  ↳ No PR: [38aa61e](https://github.com/openssl/openssl/commit/38aa61e5a7f923d93f5c7a48c71d57938a929289)
- Updated documentation for openssl-version command, corrected description of -w option and added historical explanation.
  ↳ No PR: [c7dae9c](https://github.com/openssl/openssl/commit/c7dae9c263fe507adc59e9ba2f34d473de04bbe9)
- Clarified the range of supported curves (groups) in the documentation for s_client and s_server, including named EC parameters, X25519, X448, FFDHE groups as well as groups implemented by third-party providers.
  ↳ No PR: [7751887](https://github.com/openssl/openssl/commit/775188702574dcd6cc53b7a9d3501a639c146121)
- Added a new man page for the deprecated CMAC_CTX function and updated the build dependencies.
  ↳ No PR: [b544047](https://github.com/openssl/openssl/commit/b544047c99c4a7413f793afe82ab1c165f85b5b6)
- Revised the design document for AlgorithmIdentifier parameter passing, and updated the relevant API declaration and parameter key description.
  ↳ No PR: [0941666](https://github.com/openssl/openssl/commit/0941666728c44d701496004ebd5bf96ac7b715fb)
- In the man pages for the ca and dgst commands, added a link to the provider-signature(7) man page for the signature option parameter.
  ↳ No PR: [1985ba6](https://github.com/openssl/openssl/commit/1985ba60bba272d5780c498461f2b1171f10aa21)
- Fixed the format description of IPv6 host address in multiple documents, and corrected the syntax description of -proxy and other options.
  ↳ No PR: [6de44a3](https://github.com/openssl/openssl/commit/6de44a3ef0090d58e0e499c9ab59cdf35798ca63)
- Added Dockerfile for building QUIC interoperability test containers and instructions for using it.
  ↳ No PR: [8ffdfea](https://github.com/openssl/openssl/commit/8ffdfea6395b7795b8f149ca572326d6cac392a0)
- Added description of the -testmode option to the documentation for the speed command.
  ↳ No PR: [1867aac](https://github.com/openssl/openssl/commit/1867aac808ec26f8319677d6a9e2996e6ca03185)
- Added documentation for non-interactive usage of s_client, guiding the use of the -ign_eof option and input redirection to avoid premature closing of TLS connections.
  ↳ No PR: [2b37aab](https://github.com/openssl/openssl/commit/2b37aab596f3ccb4c30cb6377da158774197808c)
- Updated openssl-fipsinstall command documentation, adding new options and HISTORY chapters for each version (3.0, 3.1, 3.2, 3.4).
  ↳ No PR: [c06f596](https://github.com/openssl/openssl/commit/c06f5966d023354d2c87178c22fba814978a7204), [7cdd0aa](https://github.com/openssl/openssl/commit/7cdd0aa0457998afbd74822733abbecda7db2cb8), [265caeb](https://github.com/openssl/openssl/commit/265caebe78da6365c36aca08d0d46382a3801c7d), [e1925d2](https://github.com/openssl/openssl/commit/e1925d2cbabe62c9c6dc75f89d7f8b6fbb8c6b11)

### Build/CI
- Added macOS 14 (M1) runner support to the CI workflow, and changed some tasks to matrix strategies to run on both macOS 13 and macOS 14.
  ↳ No PR: [ada9d8c](https://github.com/openssl/openssl/commit/ada9d8c785cce8e75a88675622dd5ec79e9aa6d7)
- Add -mxgot compilation option for m68k cross-compilation to solve the relocation truncation problem.
  ↳ No PR: [81b7aa7](https://github.com/openssl/openssl/commit/81b7aa7186bf48fa5c2eaf0c7fe3bd05880e4dbb)
- Downgrade the upload-artifact and download-artifact operations in GitHub Actions from v4 to v3 to be compatible with GitHub Enterprise Server.
  ↳ No PR: [0892716](https://github.com/openssl/openssl/commit/089271601a1d085f33ef7b7d8c3b6879045be370), [65fe3e8](https://github.com/openssl/openssl/commit/65fe3e846f7c34f68ce82c6e9501d7309d196e06)
- For CI builds on hppa architecture, reduce optimization level from -O2 to -O1 to circumvent random crashes that may be caused by the compiler or emulator.
  ↳ No PR: [067fbc0](https://github.com/openssl/openssl/commit/067fbc01b9e867b31c71091d62f0f9012dc9e41a)
- Removed macOS-11 runtime environment from CI configuration as GitHub will stop supporting this system.
  ↳ No PR: [93a644d](https://github.com/openssl/openssl/commit/93a644d14aeed02a33a1191c0de540103e6cf307)
- Changed the random seed source name to a macro definition under certain build configurations to support execution of all tests via JITTER seeds in CI.
  ↳ No PR: [1e7ff7b](https://github.com/openssl/openssl/commit/1e7ff7be23c6fc8a88a698a57107a0e0c6db2435)
- Added OpenSSL version 3.4 support in CI's provider compatibility test and prov-compat-label test.
  ↳ No PR: [9ff0ca3](https://github.com/openssl/openssl/commit/9ff0ca36a822d6d321761f0f8484c5284f674ed5), [f38b08b](https://github.com/openssl/openssl/commit/f38b08b19e9fce83ef5b5455dbbad0d605cce243), [887572b](https://github.com/openssl/openssl/commit/887572b85d3714e968bd21e0cf847fdbf1b775a2), [8a79f5b](https://github.com/openssl/openssl/commit/8a79f5bc184939aeaff4479d48fda92d0d33aa96)
- Integrate the sample program into the main build system, fix error checking for HTTP/3 samples, and enable demos build and HTTP/3 demo options in CI.
  ↳ No PR: [2000281](https://github.com/openssl/openssl/commit/2000281dad3111407092e8ea4b23996d65988500), [44f05de](https://github.com/openssl/openssl/commit/44f05ded99cab8436f8413efa8b71b8c33e00501), [693071c](https://github.com/openssl/openssl/commit/693071c088c0a93d84d3327a2477ab456fd8ca8e)
- Improve the CI artifact upload process, including introducing experimental qlog support, migrating upload scripts, packaging optimization, and fixing matrix variable issues.
  ↳ No PR: [f2db709](https://github.com/openssl/openssl/commit/f2db70962cacc2602bc614d51e0610085c99e999), [9abcf11](https://github.com/openssl/openssl/commit/9abcf116962e9a117717c751de93846f11da16cd), [58ffcbb](https://github.com/openssl/openssl/commit/58ffcbbdc3302a35cea317aeee6b76987907ee60), [395ab20](https://github.com/openssl/openssl/commit/395ab201a7f99ebe2b1598890c9a43081867d226)
- Added debuginfo build target, which is used to separate DWARF debugging information in shared libraries into separate files on Unix platforms.
  ↳ No PR: [a5d5662](https://github.com/openssl/openssl/commit/a5d56626b97dd06d02d02821485df99e2068696d)
- Fixed the detection problem of single statement if block in check_format.pl script.
  ↳ No PR: [f35c089](https://github.com/openssl/openssl/commit/f35c0894130e34ff46a429f4373c14ca98437405)
- Fixed the nested reference issue of jitter tests in GitHub workflow.
  ↳ No PR: [20bf3fe](https://github.com/openssl/openssl/commit/20bf3fe236d36734a17a08252ed19c9e1bc161cd)
- Fixed the issue where the failure message and success message formats in the FIPS installation command are inconsistent.
  ↳ No PR: [8574fa5](https://github.com/openssl/openssl/commit/8574fa5f400eb235d7f3cb1a88715de85d1caf4a)
- DSA speed test code is no longer compiled when DSA support is not enabled.
  ↳ No PR: [096a54e](https://github.com/openssl/openssl/commit/096a54ee45d6dc1f68989c0bcf86855b42fab822)
- Fixed syntax error in conditional expressions in CI workflow.
  ↳ No PR: [0fff6a2](https://github.com/openssl/openssl/commit/0fff6a2cf4c00bc7ead235099af350db61413bd2)
- Added static analysis workflow for local Coverity Connect.
  ↳ No PR: [417dad1](https://github.com/openssl/openssl/commit/417dad1e370b19f94682d1006cb54d10ac90b8ec)
- Added Provider compatibility checking workflow in PR CI.
  ↳ No PR: [94567d6](https://github.com/openssl/openssl/commit/94567d6889b8b48ac618cd8a90911e6732d0e4df)
- Fix use of environment variables in Windows CI workflows to conform to PowerShell syntax.
  ↳ No PR: [c1c6756](https://github.com/openssl/openssl/commit/c1c67561566d8d2ce0a378af110278778b9901d8)
- Removed the compilation option that forcibly disables IPv6 in the CI build configuration, allowing it to be automatically enabled based on the runtime environment.
  ↳ No PR: [68c7575](https://github.com/openssl/openssl/commit/68c7575afc5ec33fd44c9c1c571d882d6095c8ef)
- Add -Wno-switch-default compilation option to clang compiler in CI configuration to temporarily disable clang-18 warnings.
  ↳ No PR: [1597489](https://github.com/openssl/openssl/commit/15974897b7b94014e0165d7d906e31ca010e2861)
- Fixed the compatibility issue of sed/awk command in Windows CI and used PowerShell command to extract the version number instead.
  ↳ No PR: [aa08335](https://github.com/openssl/openssl/commit/aa08335852a3714075c26690a6eeab456e813a54)
- Remove unnecessary compile option -Wno-switch-default from CI workflow configuration.
  ↳ No PR: [7b1e008](https://github.com/openssl/openssl/commit/7b1e008d383a7860490b110ee46609e65bf8a9b4)
- Added and optimized code style check CI workflow, supports checking affected files in PR, and allows individual submission of fixes.
  ↳ No PR: [fc22d74](https://github.com/openssl/openssl/commit/fc22d74c53720d14f99fd880b767d8a3e4986ae2), [edb5dd5](https://github.com/openssl/openssl/commit/edb5dd56fcbeff335f2ab59e8b76780043695814)
- Adjust the Windows compilation workflow, move the configuration and build steps before version information collection, and add the vcpkg bin directory to PATH.
  ↳ No PR: [850bd09](https://github.com/openssl/openssl/commit/850bd09cf9f8c44a7c6b1fdcdde8a147748ee513)
- Added GitHub Actions workflow to automatically trigger docs.openssl.org deployment when the document directory changes.
  ↳ No PR: [8b591dc](https://github.com/openssl/openssl/commit/8b591dceeff52965dbde14a0e455c5d3548a2609)
- Enable weak SSL cipher suite support in full-featured CI jobs.
  ↳ No PR: [3bc097d](https://github.com/openssl/openssl/commit/3bc097d80ab834a3f83c1404f8fbdfebbf648c51)
- Added a workflow for nightly building QUIC interop containers and pushing them to quay.io, and updated related README links.
  ↳ No PR: [4c2242b](https://github.com/openssl/openssl/commit/4c2242b67cd864ac9f5584febda71f52cbe41395)
- Stop running tests in parallel in Coveralls workflow.
  ↳ No PR: [33adc07](https://github.com/openssl/openssl/commit/33adc0767ef8a404013e5b59bd2e7fbd47d54027)
- Add debug info in CI configuration to generate tests, install gdb and verify debuginfo file is loaded.
  ↳ No PR: [0fdbcf4](https://github.com/openssl/openssl/commit/0fdbcf4c3ca5fe91f735f9a4cb2c630af76781c4)
- Move the Docker files from the interop directory to the test directory.
  ↳ No PR: [7c3c737](https://github.com/openssl/openssl/commit/7c3c7374ce8676331770a8f9bbc1452bbdacf3be)
- Upgrade download-artifact in CI workflow to v4.1.7 and upload-artifact to v4.
  ↳ No PR: [2a6305d](https://github.com/openssl/openssl/commit/2a6305dfcd89632b69e49f8b3efe98b7e0daa1aa), [c4a5d70](https://github.com/openssl/openssl/commit/c4a5d70d98cf57434cd4f7a1ae890a2e3d09c434)
- Streamline Windows CI configuration, remove legacy operating systems, and move operating system selection to the platform matrix.
  ↳ No PR: [77bf98e](https://github.com/openssl/openssl/commit/77bf98e8fa92552d2fd07cf011f3bdf3c676a34f)
- Add conditional judgments to the cleanup step in the CI workflow to avoid task failure due to non-existence of artifacts.
  ↳ No PR: [0bb2a98](https://github.com/openssl/openssl/commit/0bb2a9863900b02401801241e739e2e99d6e7cb5)
- Upgraded Coveralls GitHub Action from v2.3.0 to v2.3.2.
  ↳ No PR: [8448fd2](https://github.com/openssl/openssl/commit/8448fd29ee6b78f8c3dc9a8e891c59ba0843e3c7)
- Combine no-ec2m configuration with enable-fips in CI workflow to expose more errors.
  ↳ No PR: [4daf4dc](https://github.com/openssl/openssl/commit/4daf4dc4d66b740aa2f66e70e16c07c23953a08d)

### Maintenance
- Removed extra spaces in error message output.
  ↳ No PR: [aececda](https://github.com/openssl/openssl/commit/aececda752d182f271bf2263f5ef9020a64668c5)
- Fixed typos in comments and adjusted blank lines to match code style.
  ↳ No PR: [fa4ee40](https://github.com/openssl/openssl/commit/fa4ee4043473185a5894274a2fa7fa2c4dc15a3c)
- Removed old PGP key fingerprint, new key information is included in the document.
  ↳ No PR: [a9fa07f](https://github.com/openssl/openssl/commit/a9fa07f47cea6a43d5ac4a3aa336ab34756c2e9b)
- Add comp.h to .gitignore.
  ↳ No PR: [2e9cd40](https://github.com/openssl/openssl/commit/2e9cd409c0411e890cabf3827770ac3d4a235b82)
- Add a comment in DRBG seed generation to indicate that the legacy code path is only for compatibility with older applications and will not be called during normal use.
  ↳ No PR: [1eb122a](https://github.com/openssl/openssl/commit/1eb122aa0ca152dc564e61674caf3f11acd85b57)
- Fix extra blank lines in apps/speed.c.
  ↳ No PR: [cfe0bbd](https://github.com/openssl/openssl/commit/cfe0bbdecadaebc6ad7ba5a3335b7a03522c434f)
- Upgrade the actions/setup-python dependency version used in CI.
  ↳ No PR: [0016337](https://github.com/openssl/openssl/commit/00163371fa502df62465163185a9a434574d6746), [de85587](https://github.com/openssl/openssl/commit/de85587911dcd41dc3546b348acf9c9f15dd7c3d), [8efd56b](https://github.com/openssl/openssl/commit/8efd56bec8cf390d08ae3b7e2a1df15742afb2a2)
- Fixed code style issues in EVP related header files.
  ↳ No PR: [787e1dd](https://github.com/openssl/openssl/commit/787e1dd941b695c957df2e2d587730a6de3df9ab)
- Add ignore rules for macOS system files .DS_Store in .gitignore.
  ↳ No PR: [10c36d2](https://github.com/openssl/openssl/commit/10c36d2f8d81a6f2b9a75f914fe094300835ba01)
- Adjust the code style of hashtable.c to standardize the spaces around macro definitions and operators.
  ↳ No PR: [d2739fc](https://github.com/openssl/openssl/commit/d2739fc350227ab17636bcb4b8209ca320b53094)
- Fix coding style issue in crypto/evp/evp_err.c.
  ↳ No PR: [873f269](https://github.com/openssl/openssl/commit/873f269697df848d13dc012a265759baa8eed8cd)
- Fix the infinite loop problem in ossl_ht_insert that may be caused by the failure of grow_hashtable.
  ↳ No PR: [6cdca7b](https://github.com/openssl/openssl/commit/6cdca7b9febe35d993b6b3e3cd3c276e2387677b)
- Adjust the connect and sslecho examples to support compiling and running on Windows platform.
  ↳ No PR: [3b56cd4](https://github.com/openssl/openssl/commit/3b56cd4f041cc78035aafd0f9afe50dd4a6dc1ed), [4ad6e54](https://github.com/openssl/openssl/commit/4ad6e549fadde344cbbe9d7f4aafb4d3a2a67094), [793a405](https://github.com/openssl/openssl/commit/793a4056ad94e5f3076b7988ddee3af2aece09f2)
- Rename macro WININSTALLCONTEXT to OSSL_WINCTX.
  ↳ No PR: [630e3a1](https://github.com/openssl/openssl/commit/630e3a168446ab7e269176bad5b1bf79ea54301a)
- Explicitly ignore the unchecked return value of ossl_quic_rxfc_on_retire to suppress compiler warnings.
  ↳ No PR: [35b1472](https://github.com/openssl/openssl/commit/35b1472f0764c8691e0cfcd6a2e0265aafd08f93)
- Replaced strnlen() in fuzz/provider.c with OPENSSL_strnlen() to enhance portability.
  ↳ No PR: [1b2ab42](https://github.com/openssl/openssl/commit/1b2ab42ed788f09dd0ab3be7abf7276635568c48)
- Add null pointer check and return value verification in rehash_main function.
  ↳ No PR: [b134f1e](https://github.com/openssl/openssl/commit/b134f1e7debe737ad1629420a4a2b63f01d30994)
- Explicitly include the e_os.h header file in randfile.c to support the close() function.
  ↳ No PR: [a6c9378](https://github.com/openssl/openssl/commit/a6c9378e43749cc75c47af0b7f1c9c9a1257e271)
- Updated actions/download-artifact dependency in GitHub Actions to v4.1.8.
  ↳ No PR: [5132a5d](https://github.com/openssl/openssl/commit/5132a5df6b4c8b0ca7655b71988d37c7479f058e)
- Fixed indentation syntax error in dependabot.yml.
  ↳ No PR: [84756fe](https://github.com/openssl/openssl/commit/84756fe206db36f41de96b0d9aa2ddc1a7ecd564)
- Add exception rules in .gitattributes to include the .ctags.d directory in the generated tarball.
  ↳ No PR: [e1fd043](https://github.com/openssl/openssl/commit/e1fd043ad7fa865a8ef9160c892b49a098d23c71)
- Upgraded Coveralls GitHub Action from v2.2.3 to v2.3.0.
  ↳ No PR: [13d37d8](https://github.com/openssl/openssl/commit/13d37d8f7557ee7935032ea832eab3e3c5540158)

### Others
- Adjust the code style: remove trailing whitespace, unify the curly brace position and array initialization format, and replace sprintf with BIO_snprintf.
  ↳ No PR: [1cf2f82](https://github.com/openssl/openssl/commit/1cf2f8231ea8c3c1dd73a6f5bdf1404ecd503c4d), [962431d](https://github.com/openssl/openssl/commit/962431d58bdf7fcdb3db11f17cea878b83292243), [f83707d](https://github.com/openssl/openssl/commit/f83707dc6df306e2ed07eafe518b19e8e3c427ca)
- Fixed typos and duplicate words in multiple file comments.
  ↳ No PR: [15eb7b6](https://github.com/openssl/openssl/commit/15eb7b6875e5d717c1bb47a4e6022fd8a9fa3adb), [5962c71](https://github.com/openssl/openssl/commit/5962c717c4c00654bc8120e81db9978c3efd91fd), [3c0bb68](https://github.com/openssl/openssl/commit/3c0bb68c75bc517224d57b973dce0cd016342faf), [4174f26](https://github.com/openssl/openssl/commit/4174f26141a7db3e29dc1f96bc873d357f6ca824), [96939f1](https://github.com/openssl/openssl/commit/96939f1e2c6ac1264142ef62c9925786f5723649), [5454ef7](https://github.com/openssl/openssl/commit/5454ef7cb38290196758f72e16b598e970ef5ecb)
- Fix spelling and grammatical errors in the document, delete duplicate entries and add explanations.
  ↳ No PR: [f1c14f1](https://github.com/openssl/openssl/commit/f1c14f1853d2df94e339208eed1df823c2238389), [5a0c92c](https://github.com/openssl/openssl/commit/5a0c92cf093b4f0aa65f4fdbff88d7bdc83491f3), [d4188f2](https://github.com/openssl/openssl/commit/d4188f24866f88b4269110ce86f9545edd44c846), [5d218b0](https://github.com/openssl/openssl/commit/5d218b0e447da20d44d75ab8105ee1d742ca8d09), [c81b7b0](https://github.com/openssl/openssl/commit/c81b7b059f614a6c43ad6a6907b1a740b783fbfd)
- Updated the copyright year of multiple source files to 2024.
  ↳ No PR: [b646179](https://github.com/openssl/openssl/commit/b646179229927601bad3ec305fbd12dae98eb9b9), [496bc12](https://github.com/openssl/openssl/commit/496bc128fdc994388c8ec956c4b5ebcb90459ae0)
- Update version label of perl-actions/install-with-cpanm in CI workflow.
  ↳ No PR: [599bc92](https://github.com/openssl/openssl/commit/599bc929baa3c5496342641e028e4c482aed7449)
- Ignore newly generated header file include/openssl/x509_acert.h in .gitignore.
  ↳ No PR: [51fd52b](https://github.com/openssl/openssl/commit/51fd52b8a791528971ca13aa4db94e5d50804b29)
- Limit DH key parameter checking in fuzz testing, and expand handling of DHX key types.
  ↳ No PR: [9fc61ba](https://github.com/openssl/openssl/commit/9fc61ba0a74dfd910c4e96e711291555ac64b2b4)
- Add security fix entries in CHANGES.md and NEWS.md for CVE-2024-9143.
  ↳ No PR: [233034b](https://github.com/openssl/openssl/commit/233034bc5a294b26d37186dc68d7d6d8357d889a)
- Fixed comment errors in multiple source files, including spelling, grammatical and content errors.
  ↳ No PR: [7c30519](https://github.com/openssl/openssl/commit/7c305197658cb9a337d34f58ca43c0713bec2213), [8f25098](https://github.com/openssl/openssl/commit/8f250985ad1ac4efc25621ce2504c52ef0cbe283), [d14e5c9](https://github.com/openssl/openssl/commit/d14e5c964ae81f1cab6298963a48040f492727e2), [620ecb2](https://github.com/openssl/openssl/commit/620ecb2e10672b9710cca599fa74d044b430d9da)
- Fixed multiple spelling and grammatical errors in documentation and help messages.
  ↳ No PR: [45f5d51](https://github.com/openssl/openssl/commit/45f5d51b72a262bf85c4461fbded91485ce6b9da), [0813ffe](https://github.com/openssl/openssl/commit/0813ffee2fe6d1a4fe4ec04b7b18fe91cc74a34c), [901e279](https://github.com/openssl/openssl/commit/901e27982c6bcd5ac94e455d2ef87e80398cd474), [d0a49ee](https://github.com/openssl/openssl/commit/d0a49eea4a8bb50f7d2269bac390a0ce2cddeb1f)
- Updated links in CONTRIBUTING.md to point to the correct resources.
  ↳ No PR: [ad3d57d](https://github.com/openssl/openssl/commit/ad3d57d27141c09fe07ef39c49af5afe69c59383), [5854b76](https://github.com/openssl/openssl/commit/5854b764a762598b662a5166be8d0030af06c1c0)
- Update the version information in CHANGES.md and NEWS.md to prepare for release.
  ↳ [#25390](https://github.com/openssl/openssl/pull/25390): [2648f68](https://github.com/openssl/openssl/commit/2648f68f4c33b1a5b89ed6ba20051d7c5e7f8f0e), [5472786](https://github.com/openssl/openssl/commit/5472786907dd1b4a8a15c9088432c1ae28fd8578)
- Updated the copyright year of multiple source files to 2024.
  ↳ [#25390](https://github.com/openssl/openssl/pull/25390): [7ed6de9](https://github.com/openssl/openssl/commit/7ed6de997f62466271ef7ff6016026e1fdc76963) | [#25626](https://github.com/openssl/openssl/pull/25626): [544e561](https://github.com/openssl/openssl/commit/544e56196944d3d8f930360500ce3a02f92a5ab0)
- Remove duplicate header file inclusions in demos/sslecho/main.c.
  ↳ No PR: [3472732](https://github.com/openssl/openssl/commit/3472732cd23f97fbe367f50bf0bdc0a7d762fbba)
- Removed configuration target for Guardian build and updated related documentation.
  ↳ No PR: [929fcc5](https://github.com/openssl/openssl/commit/929fcc57125b8ed3cc58b254bdc1790a8136247e)
- Updated CI badge in README, replacing it with OS Zoo CI.
  ↳ No PR: [fccefa7](https://github.com/openssl/openssl/commit/fccefa7016b12dfcf362e6169ec3b3b4d0634498)
- Fixed typos in several source files.
  ↳ No PR: [7d91d5b](https://github.com/openssl/openssl/commit/7d91d5ba35a69808f6083695ed1f83570ae0a43e)
- Document new debuginfo Makefile target in CHANGES.md.
  ↳ No PR: [1fb3952](https://github.com/openssl/openssl/commit/1fb39522a241d7ddaab48e20ec0d6ca383188d38)
- Fixed formatting issues with code examples in openssl-ts documentation.
  ↳ No PR: [178e920](https://github.com/openssl/openssl/commit/178e920c868c06f511e46beac6e3be09b844a0f4)
- Updated the copyright year of multiple source files to 2024.
  ↳ [#25766](https://github.com/openssl/openssl/pull/25766): [246a348](https://github.com/openssl/openssl/commit/246a348d04dddf97265c9e94d810341ade8f37c6)
