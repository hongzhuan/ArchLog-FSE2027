# Release Note

## Important Changes

### Provider Subsystem
- Ensure that FIPS internal providers are actively loaded during initialization to avoid problems that cannot be found due to delayed loading. (Architecture-related: core module behavior)
  ↳ No PR: [6ff4c1d](https://github.com/openssl/openssl/commit/6ff4c1d87468fdd18deeebbb01fbf049bd6cec1f)
- Added LMS signature algorithm support, including public key decoding, signature verification, FIPS provider integration and key management. (Architecture-related: public API)
  ↳ No PR: [c64558e](https://github.com/openssl/openssl/commit/c64558ede85ed296753b42f74478b99bd89e7c34), [7be3137](https://github.com/openssl/openssl/commit/7be3137fb5dd44c97def5d1d6279ffa7218dc643), [48af66a](https://github.com/openssl/openssl/commit/48af66aef72d482d41beafaf919b71e1dcb491b8), [2a6a2ad](https://github.com/openssl/openssl/commit/2a6a2adc8d9ec7476613f035f91877e5a65ab6f5), [25171e0](https://github.com/openssl/openssl/commit/25171e08031b63b5eb4dd2e1d79eac4e8deca3d6)
- Add hardware acceleration support for the SM4 encryption algorithm for the x86-64 platform, including key settings, encryption and decryption functions, and integrate into CCM, GCM, XTS and other modes. (Architecture-related: platform compatibility)
  ↳ No PR: [b12cd40](https://github.com/openssl/openssl/commit/b12cd40e8bdf74b8eacaf2dc638e43986ae13b8d)
- Add detailed output to the openssl list -store-loaders command to display the settable parameters of the provider-based STORE loader; also add the OSSL_STORE_LOADER_settable_ctx_params function. (Architecture-related: public API)
  ↳ No PR: [9123684](https://github.com/openssl/openssl/commit/9123684c817c48681aa1998e789c4dae6617c4de)
- ML-DSA, ML-KEM, SLH-DSA algorithm enhancements: expose internal functions, add msg_update support, and add security category parameters. (Architecture-related: public API)
  ↳ No PR: [5c16db8](https://github.com/openssl/openssl/commit/5c16db8cdcd1c1519eb533538fcd6180b40f0fd2), [341f1b7](https://github.com/openssl/openssl/commit/341f1b7f70567aab668452c824d978768ea765b4), [6432843](https://github.com/openssl/openssl/commit/64328438f6c8ac4440167d89cbdacd8f8e02d7d0), [32bc8e3](https://github.com/openssl/openssl/commit/32bc8e3434be2611a8d9f7959805a370377502ff), [3b9f957](https://github.com/openssl/openssl/commit/3b9f957c790b1dc1261f61bdb419f9b792fd9b04), [2f1890e](https://github.com/openssl/openssl/commit/2f1890eb181d3c13219d8c0991cbd6209338cf63), [27eea04](https://github.com/openssl/openssl/commit/27eea04b0616847022847f6737e53704becae4c4), [dfc0367](https://github.com/openssl/openssl/commit/dfc03679f516fa7c16c85d075ae19e880eac6569), [1f000a4](https://github.com/openssl/openssl/commit/1f000a411259cdc06e91375e09f30dab021eedd1), [0bc71fd](https://github.com/openssl/openssl/commit/0bc71fd5195053a9c7087a5338af8a7acc89c5ab), [bb05bf7](https://github.com/openssl/openssl/commit/bb05bf76dc97ace5c7a38c081321fe28a5c953eb)
- Updated FIPS indicator functions, providing unlocated and positioned versions of set_ctx_param and get_ctx_param. (architecture-related: public API)
  ↳ No PR: [dd266b4](https://github.com/openssl/openssl/commit/dd266b442681201db5b50de669a592526412a1e9)
- provider_util adds set_propq, set_engine and other auxiliary functions, and restructures the loading functions of cipher, digest, macctx to directly accept individual parameter pointers. (Architecture-related: public API)
  ↳ No PR: [688d0bc](https://github.com/openssl/openssl/commit/688d0bc590514a164b19f5569ba09695925ddf62)
- Pass the ERR_count_to_mark function to the provider through the in dispatch array when the provider is initialized. (Architecture-related: public API)
  ↳ No PR: [f77fafd](https://github.com/openssl/openssl/commit/f77fafd16e92699544466556d368ed7722f49dd8)
- Add pairing compliance testing required by FIPS 140-3 during DH key generation. (Architecture-related: FIPS compliance)
  ↳ No PR: [b561837](https://github.com/openssl/openssl/commit/b561837ee9bb9393cd3ada325180130fda2613bc), [88a1309](https://github.com/openssl/openssl/commit/88a13095667228c2361361c97704ea992d837ade)
- Added FIPS module to import PCT error codes and their corresponding error description strings. (Architecture-related: public API)
  ↳ No PR: [9013cca](https://github.com/openssl/openssl/commit/9013cca925836ff092cf31acd6edadbbee0c6858)
- Added Pairing Conformance Test (PCT) for Ed25519, Ed448, EC and RSA key import in FIPS mode to meet FIPS 140-3 requirements. (Architecture-related: FIPS Compliance)
  ↳ No PR: [58ab3b0](https://github.com/openssl/openssl/commit/58ab3b0ffeea2b4c30f8794d281650ce7bfec6d2), [a177798](https://github.com/openssl/openssl/commit/a177798e0b8f3c7ff66b2a609924aafeb66b8b12), [57230da](https://github.com/openssl/openssl/commit/57230da2bd0be6b219cec2995832034b1e09e0e9), [32ff539](https://github.com/openssl/openssl/commit/32ff539daf83cccc15a159fe214cac66acc80fec)
- Fixed the problem of obtaining the parameter list in ECX key management, removing the OSSL_PKEY_PARAM_MANDATORY_DIGEST parameter from the general ECX parameters and leaving it only in the parameter list of Ed25519/Ed448. (Architecture-related: public API)
  ↳ No PR: [482d3f9](https://github.com/openssl/openssl/commit/482d3f9338b3d4c7537a1d112dce9c8e370c8d9f)
- Fixed the problem of obtaining updated IV in ChaCha20 cipher, and adjusted the counter increment logic to ensure that the updated IV is returned correctly. (Architecture-related: ChaCha20 cipher behavior)
  ↳ No PR: [67ad6a0](https://github.com/openssl/openssl/commit/67ad6a089804c3e78a2d9cd7058c8f2ddd86347c)
- Fixed the problem of HKDF with fixed summary being incorrectly restricted when setting the summary. Parameters can now be obtained and set correctly, and related tests have been updated. (Architecture-related: public API)
  ↳ No PR: [c6a1d8e](https://github.com/openssl/openssl/commit/c6a1d8ea744abac1c467642dba0bbea88293ffef), [df98182](https://github.com/openssl/openssl/commit/df981828f1bf8a28990798e79434148d3b767653)
- In the FIPS module, when the pairwise conformance test of ML-DSA or SLH-DSA fails, the module will enter an error state. (Architecture-related: FIPS compliance behavior)
  ↳ No PR: [17cacc1](https://github.com/openssl/openssl/commit/17cacc1a1c85b65ba94f76890810d2ada6243f38)
- Relaxed the strict check on absolute paths in the file: URI scheme, now allowing relative paths to improve user experience. (Architecture-related: external behavior)
  ↳ No PR: [6683c88](https://github.com/openssl/openssl/commit/6683c886f27d1f21a3a893af994160b1b26fe2c1)
- Refactored the parameter processing of ciphercommon, removed the obsolete and incorrect AEAD parameters, and switched to the new parameter processing method; fixed the settable context parameter list of ChaCha20-Poly1305 password. (Architecture-related: public API)
  ↳ No PR: [b0dcb39](https://github.com/openssl/openssl/commit/b0dcb391d2d966a541f4b563deea1abe54f7b89a), [d521ed9](https://github.com/openssl/openssl/commit/d521ed9ea5632f00b01ac111864fedcbfd2fb7a6)
- Fixed multiple bugs in LMS signature implementation, including W=1 truncation digest checksum error, code review issues (error handling, endian conversion, resource release), and added NIST ACVP-based test coverage. (Architecture-related: public API)
  ↳ No PR: [e6c8110](https://github.com/openssl/openssl/commit/e6c8110483490de9fcc2ad20411a1a6e224685b6), [6b5fd48](https://github.com/openssl/openssl/commit/6b5fd48ee4fccb78a21e7dbc039b2d0847609a1a)
- Reconstructed the parameter acquisition function of the ECX/ED key manager, and fixed the problem of the ED algorithm missing security categories and FIPS indicators. (Architecture-related: public API)
  ↳ No PR: [bde55d4](https://github.com/openssl/openssl/commit/bde55d421b1f49e31248c240efe50ff1f0d24141)
- Added repeated parameter error code PROV_R_REPEATED_PARAMETER and its corresponding error description string. (Architecture-related: public API)
  ↳ No PR: [5614c6f](https://github.com/openssl/openssl/commit/5614c6f7e4c20388b775aa27676df85683bed220)
- In FIPS mode, the use of SHA512-224 and SHA512-256 for ECDSA/DSA signatures is prohibited because these algorithms have no corresponding OID. (Architecture-related: FIPS compliance)
  ↳ No PR: [a7f9f31](https://github.com/openssl/openssl/commit/a7f9f31664103ae370b688fdd468c18ad9744c21)
- In the default provider, an error is now also thrown when the number of PBKDF2 iterations is zero and lower bound checking is disabled. (Architecture-related: PBKDF2 behavior change)
  ↳ No PR: [53ea500](https://github.com/openssl/openssl/commit/53ea500c49d41f516755aab0f03d8f5066c8623b)
- Fixed PEM format decoding of SM2 private keys and added support for SM2 private key PEM identification. (Architecture-related: public API)
  ↳ No PR: [bd172dd](https://github.com/openssl/openssl/commit/bd172dd0e1b76116402534aa4bb5c89d039e7762)
- In ML-KEM wrapper function, corrected error code when shared key buffer is NULL. (Architecture-related: public API)
  ↳ No PR: [5d0c6c5](https://github.com/openssl/openssl/commit/5d0c6c52e722f37f0254f8d5bfaf9b5c6b0df68b)
- In SSKDF and X9.42 KDF, the parameter names key and ukm are used as aliases for secret and uinfo respectively, and the independent reference to the key parameter is removed. (Architecture-related: public API parameter alias)
  ↳ No PR: [d847a47](https://github.com/openssl/openssl/commit/d847a4722254d25e23c6a8dc5b3aa8173cefcab3)
- Removed two unsupported parameters in HMAC. (Architecture-related: public API parameter removal)
  ↳ No PR: [d02ece1](https://github.com/openssl/openssl/commit/d02ece1f5a22d7f182ad9e1f6432e4ed0aacb624)
- Removed the FIPS pairing consistency check for DH, EC and RSA algorithms when importing keys, and rolled back the previously exposed RSA key pairing consistency test API. (Architecture-related: API rollback)
  ↳ No PR: [32e9437](https://github.com/openssl/openssl/commit/32e9437c563f45318a75416f243d18cb4c52d285), [18597ff](https://github.com/openssl/openssl/commit/18597ff4ec3cbad4e9611f10f8d8b2d96b81e816), [b20da23](https://github.com/openssl/openssl/commit/b20da2328018107414fe896e59e7d4d6c8af8174)
- Reconstruct the cryptographic algorithm header file, remove the old TRIE parameter parsing function declaration, and add the general OSSL_PARAM structure and auxiliary function declaration. (Architecture-related: Internal API: OSSL_PARAM structure)
  ↳ No PR: [fa92dd9](https://github.com/openssl/openssl/commit/fa92dd9427665428d5132a395b71833bdf779b13), [f9865ab](https://github.com/openssl/openssl/commit/f9865ab9eedfd6907e0e45649f1600a88449e04f)
- Added a new self-test function for LMS signature verification in the FIPS module. (Architecture-related: FIPS self-test)
  ↳ No PR: [d3a29ad](https://github.com/openssl/openssl/commit/d3a29ad1354aa446c09fac615beee7da36ead853)
- Reintroduced the RSA Encryption/Decryption Known Answer Test (KAT) to meet FIPS-140-3 certification requirements. (Architecture-related: FIPS Self-Test)
  ↳ No PR: [1fd7ebe](https://github.com/openssl/openssl/commit/1fd7ebe7e420b6c754e84e76db913119b1d48a23)
- Add FIPS 140-3 Pairing Conformance Test (PCT) when importing DH keys, and adjust related verification functions to support null value return. (Architecture-related: public API)
  ↳ No PR: [db969c3](https://github.com/openssl/openssl/commit/db969c3ab08240cf9652cb621fbf1936d056464c)
- Fixed the signed integer overflow problem in RAND_load_file caused by oversized files, and exited early before iterations that may trigger overflow. (Architecture-related: public API)
  ↳ No PR: [d4f65dc](https://github.com/openssl/openssl/commit/d4f65dc909c15a1cf2423453050c6308c44f1a3a)
- Add transient error status to OSSL_SELF_TEST_TYPE_PCT_IMPORT to avoid denial of service attacks. (Architecture-related: public API)
  ↳ No PR: [1dc1de7](https://github.com/openssl/openssl/commit/1dc1de78617a3ef817d845329ad9c7b8c96362a2)

### Core/Crypto Layer
- Separate the memory allocation of public keys and private keys in ML-KEM and ML-DSA key structures: the private key part uses secure memory, and the public key part uses ordinary memory to reduce secure memory usage. (Architecture-related: secure memory allocation)
  ↳ No PR: [b4fedba](https://github.com/openssl/openssl/commit/b4fedba43caab2980e9d329422e7b0127d603949)
- Implement KEMRecipientInfo (RFC 9629) in CMS, add ML-KEM support, and add -recip_kdf and -recip_ukm command line parameters. (Architecture-related: public API)
  ↳ No PR: [d0899ab](https://github.com/openssl/openssl/commit/d0899abb1b7654922b2272070d8fb593d8b13cff)
- Add kekcipher option to CMS password recipient information, and disable the use of AEAD cipher as key encryption algorithm. (Architecture-related: public API)
  ↳ No PR: [f3867bb](https://github.com/openssl/openssl/commit/f3867bb25bee6267eb292ebdb0528de17710828f)
- Added z17 machine generation support for the s390x architecture, allowing z17 to be specified as the machine generation through the environment variable OPENSSL_s390xcap. (Architecture-related: platform compatibility)
  ↳ No PR: [bab1e88](https://github.com/openssl/openssl/commit/bab1e882a99c59b2822d7a3d55e98c1e2a32c98e)
- Added CRYPTO_THREAD_get_local_ex and CRYPTO_THREAD_set_local_ex API, used enumeration fixed key ID to implement thread local storage based on key and libctx value, and updated the FIPS self-test cleaning function. (Architecture-related: public API)
  ↳ No PR: [c1c2a33](https://github.com/openssl/openssl/commit/c1c2a333d34871f6210f2b5fb21ee631c4fb319e)
- Add MD5 assembly implementation to RISC-V architecture, support rv64gc and Zbb instruction set, performance improved by 10%–50% compared to compiler-generated code. (Architecture-related: platform compatibility)
  ↳ No PR: [80c664d](https://github.com/openssl/openssl/commit/80c664db430d882be22cd237f3e0a313ae3b15a3)
- Implement deterministic ECDSA signing functionality in the FIPS provider and add self-test descriptors. (Architecture-related: FIPS compliance)
  ↳ No PR: [c281a73](https://github.com/openssl/openssl/commit/c281a7303c43dcbd2456c04e463de832f2fded6a), [0b9f788](https://github.com/openssl/openssl/commit/0b9f7885700a99b6acc122ff7debb3d35829200d), [833a34d](https://github.com/openssl/openssl/commit/833a34dac360328a1db0968d7d483597ea9990dc)
- Improved conflict detection of OBJ_create(), checks for duplicate objects after writing the lock, and returns NID_undef when duplicated; at the same time, restructured OBJ_add_object() to support duplicate detection. (Architecture-related: public API)
  ↳ No PR: [e70c3ef](https://github.com/openssl/openssl/commit/e70c3efd7c387cb32d8efc0b594e02d0dbca737b)
- Optimize RCU implementation, reduce the number of queue pairs and adjust memory barriers. (Architecture-related: RCU implementation optimization)
  ↳ No PR: [a532f23](https://github.com/openssl/openssl/commit/a532f2302d9eac7a2ba52b9929b790c20347c9ba)
- Fixed compilation errors and runtime detection issues in Windows platform registry configuration, corrected buffer types and API calls. (Architecture-related: platform compatibility)
  ↳ No PR: [0e38f78](https://github.com/openssl/openssl/commit/0e38f78dca2ececcce4d0179b7d111452e7878ea), [908e0f3](https://github.com/openssl/openssl/commit/908e0f37288b76132c166364c75cbac9f46deb9f)
- Fixed the issue of missing ports and paths containing ISO 8601 timestamps in URL parsing. (Architecture-related: public API)
  ↳ No PR: [56910e7](https://github.com/openssl/openssl/commit/56910e7211363de26d3975635f4968c55de08eb6)
- Fix the memory order problem on weakly ordered systems, add virtual atomic release operation in update_qp to ensure visibility. (Architecture-related: platform compatibility)
  ↳ No PR: [4a1a7fe](https://github.com/openssl/openssl/commit/4a1a7fe5ce088964010779e1f5a90560903ecc76)
- Fixed the memory leak problem caused by UI_dup_* series functions not releasing the copied string when memory allocation fails. (Architecture-related: public API)
  ↳ No PR: [8f06efe](https://github.com/openssl/openssl/commit/8f06efe234ca875eb09af7f35f1ad3d62be696aa)
- When importing ML-KEM private key, if the public key hash does not match, the corresponding error message will now be added to the error stack instead of just parsing failure. (Architecture-related: public API)
  ↳ No PR: [8721def](https://github.com/openssl/openssl/commit/8721def7fce8f895fa3e7b0eae9e577e5ecf32bb)
- Add error checking for BIO_printf, BIO_puts and asn1_write_micalg calls in the SMIME_write_ASN1_ex function to ensure that the function returns correctly when writing fails. (Architecture-related: public API)
  ↳ No PR: [d8e87f9](https://github.com/openssl/openssl/commit/d8e87f9c2f1f87bfd18d164e62442595a68766a0)
- Improve the I/O error checking in the PEM_write_bio_ASN1_stream function and ensure that the return value is also checked when writing the PEM header and tail. (Architecture-related: public API)
  ↳ No PR: [7084d16](https://github.com/openssl/openssl/commit/7084d167aae16ad7f7a69c3907ba284665b458bf)
- Add missing I/O error checking to SMIME_crlf_copy and SMIME_text functions to ensure correct handling of errors when write operations fail. (Architecture-related: public API)
  ↳ No PR: [1d5d463](https://github.com/openssl/openssl/commit/1d5d4634ee290c5e0776428454a7c9b1a6dd30d2)
- Add missing I/O error checking to the SMIME_text function to ensure that the error status is returned correctly when BIO_write fails to write. (Architecture-related: public API)
  ↳ No PR: [3f95318](https://github.com/openssl/openssl/commit/3f953185b2ae0c9c7c2d018ac5b230c59e059cc5)
- Fixed P-384 curve crash caused by incorrect use of accelerated implementation on PPC64 targets lower than Power9, which will now fall back to the generic implementation. (Architecture-related: Platform compatibility)
  ↳ No PR: [29864f2](https://github.com/openssl/openssl/commit/29864f2b0f1046177e8048a5b17440893d3f9425)
- Treat 0 values returned by DH key calculations as errors, and add checks for empty DH objects. (Architecture-related: DH key calculation behavior)
  ↳ No PR: [1c1ce2a](https://github.com/openssl/openssl/commit/1c1ce2a6eeb18b3102e0618a988b2dfe96b709aa)
- Added parameter precondition checking for ASN1_STRING_TABLE_get and ASN1_STRING_TABLE_add functions, and an error will be returned when invalid parameters are passed in. (Architecture-related: public API)
  ↳ No PR: [4a341e0](https://github.com/openssl/openssl/commit/4a341e083011c5329dc327745cb671eef917cb0f)
- Fixed an issue on the s390x platform where HMAC did not return an error when calling update or final after the context has been terminated. (Architecture-related: platform compatibility)
  ↳ No PR: [339ced7](https://github.com/openssl/openssl/commit/339ced70da1206bf090c3de981093b99cfa0d39a)
- Migrate the thread local storage management of the random number generator to the new API to avoid exhausting the operating system thread local storage space. (Architecture-related: public API)
  ↳ No PR: [ce990ce](https://github.com/openssl/openssl/commit/ce990ce83b55754df70b5abcb82e738fe3fc5c06)
- Migrate the thread event handler in the FIPS module to the new thread-local API to avoid space exhaustion caused by independently allocating thread-local storage keys for each context. (Architecture-related: public API)
  ↳ No PR: [2e74a30](https://github.com/openssl/openssl/commit/2e74a3045b47ae9db721614fa1283b3e8de46c51)
- Introduce the CRYPTO_THREAD_NO_CONTEXT special context flag to avoid stack overflow caused by recursive calls to the thread local storage API; also fix the parameter type conversion and size check in ASYNC_init_thread. (Architecture-related: thread API)
  ↳ No PR: [24f0715](https://github.com/openssl/openssl/commit/24f0715e00a6ec1d33cf9bc602444b465bafcbb6)
- Fixed the problem that OSSL_STORE did not consider cache information in the EOF check, and moved the cache information check to the OSSL_STORE_eof function. (Architecture-related: public API)
  ↳ No PR: [1f3af48](https://github.com/openssl/openssl/commit/1f3af48c312a5f94612e9a822b78a3afdadc27c1)
- Fixed the problem of memory allocation failure not being reported in CRYPTO_realloc and CRYPTO_aligned_alloc, and added error reporting and parameter verification. (Architecture-related: public API)
  ↳ No PR: [a83b853](https://github.com/openssl/openssl/commit/a83b85333ce797c47743ac2fb7beadf58c1b3219), [26dc3d9](https://github.com/openssl/openssl/commit/26dc3d98369f290bd61e0fb41eb0f2ec91d686b6)
- Fix the problem that the return value of ASN1_OCTET_STRING_set is not checked in the CMS_RecipientInfo_kemri_set_ukm function, and avoid calling OPENSSL_cleanse when keklen exceeds the buffer size. (Architecture-related: public API)
  ↳ No PR: [e729d7c](https://github.com/openssl/openssl/commit/e729d7c7329200ab9152ad4817d09f0a65dec2d6)
- Add an error reporting mechanism for the CRYPTO_realloc function when memory allocation fails. (Architecture-related: public API)
  ↳ No PR: [313c121](https://github.com/openssl/openssl/commit/313c12125e37fabcb7eca57da5bc3d00b1a356dd)
- Fixed the problem that OSSL_sleep may return early due to signals on POSIX systems, and check the remaining time in a loop to ensure that the actual sleep duration reaches the specified value. (Architecture-related: public API)
  ↳ No PR: [760929f](https://github.com/openssl/openssl/commit/760929f6ba18952c052e92acb2f0c0163ab7720a)
- Removed OSSL_CRYPTO_ALLOC attribute from CRYPTO_memdup, CRYPTO_strdup and CRYPTO_strndup function declarations, as this attribute does not apply to functions that return initialized copy results. (Architecture-related: public API)
  ↳ No PR: [85bba74](https://github.com/openssl/openssl/commit/85bba74789f82daca7482a9274c6d02843fb2dbb)
- Fixed the OBJ_create function returning NID_undef when an error occurs and the newly created NID when successful. (Architecture-related: public API)
  ↳ No PR: [5e34d64](https://github.com/openssl/openssl/commit/5e34d6476016db7630aed77e927d95dd94fc67b0), [174c992](https://github.com/openssl/openssl/commit/174c992b15e9c91f4d888625eb1728019037b9a3)
- Fix for S390 platform deterministic ECDSA signature failure in FIPS mode, by creating the correct BN_CTX context for reverse order operations. (Architecture-related: Platform compatibility)
  ↳ No PR: [546c5b3](https://github.com/openssl/openssl/commit/546c5b3eadd202fb59127cba1856287fcc772383)
- Fixed the issue where the public_from_private() function incorrectly returns success on the wrong path, and now correctly returns 0 when it fails. (Architecture-related: public API)
  ↳ No PR: [c5c70f3](https://github.com/openssl/openssl/commit/c5c70f370c0de953201b3ce0ca4e26ffd86aef46)
- Disable read and write mutexes on RISC-V architecture to resolve glibc implementation issues. (Architecture-related: Platform compatibility)
  ↳ No PR: [3c28b59](https://github.com/openssl/openssl/commit/3c28b5938068aed0cf7d3f0a489a23dcc19fd440)
- Expose internal API for RSA key pair conformance testing in FIPS module. (Architecture-related: public API)
  ↳ No PR: [dc5cd6f](https://github.com/openssl/openssl/commit/dc5cd6f70a0eeb30e272fe885a64f3e3d76b5e42)
- Split the ML-DSA internal signature verification function into mu calculation and actual signature/verification, and add a public mu calculation auxiliary function to support input messages in blocks. (Architecture-related: public API)
  ↳ No PR: [90f0137](https://github.com/openssl/openssl/commit/90f0137453aaec5f09d26fda91c6025ae25e4130), [8f99bcd](https://github.com/openssl/openssl/commit/8f99bcdbb80103b7cbdc4269c607142549e2d678)
- Change OPENSSL_cpuid_setup from a constructor to a non-constructor, removing its automatic initialization behavior. (Architecture-related: platform compatibility)
  ↳ No PR: [1d770fc](https://github.com/openssl/openssl/commit/1d770fc6a9a0a7d6e20f3232180b80c366c2d4df)
- Deprecate the ASN1_METH related code used internally, protect the old interface through conditional compilation, and add RSA-PSS aliases to be compatible with older versions. (Architecture-related: public API compatibility)
  ↳ No PR: [af2aaf3](https://github.com/openssl/openssl/commit/af2aaf3271c0b0a193f33d5c0be07754b846759e)
- Implemented interleaved AES-CBC-HMAC-SHA1/256 and AES-CBC-HMAC-SHA512 encryption post-authentication modes on aarch64, only supporting non-padding mode and input lengths in multiples of 16 bytes to improve performance. (Architecture-related: platform compatibility)
  ↳ No PR: [86408fa](https://github.com/openssl/openssl/commit/86408fa8de640ebf09b08cb5fce8173d2dbc5702), [24f32f1](https://github.com/openssl/openssl/commit/24f32f14e963fd2d73816e3c5c0bdef1a68be47a)
- Enable optimized implementation based on SM3 ISA extensions for x86-64 platforms. (Architecture-related: Platform Compatibility)
  ↳ No PR: [e1eb6fd](https://github.com/openssl/openssl/commit/e1eb6fdb3a42eb62b9606b208bb0d2c710c30a9c)
- Enable AES-GCM's unroll8 and unroll12 optimizations for Neoverse N3 and V3 processors. (Architecture-related: Platform compatibility)
  ↳ No PR: [b6dceb3](https://github.com/openssl/openssl/commit/b6dceb36e8f46c7f74db5882322eda062227ab6e)
- Enable AES and SHA3 optimization on Qualcomm Snapdragon
  ↳ No PR: [fda4777](https://github.com/openssl/openssl/commit/fda4777c140e47d7ae7115e5bcccb8f439e2ed41)
- Add optimized implementation based on Intel AVX-512 and VAES instruction set for AES-CFB128 mode. (Architecture-related: public API)
  ↳ No PR: [055dd1d](https://github.com/openssl/openssl/commit/055dd1d8bb24ba307981091524fdf06da3771641)
- Replace the blinding structure of the RSA key with a sparse array indexed by thread ID, eliminating dependence on write locks and significantly reducing lock competition under multi-threads. (Architecture-related: RSA blinding lock elimination)
  ↳ No PR: [902568b](https://github.com/openssl/openssl/commit/902568bbd98a61d03495498b56e95e67e42cc71b)
- Added SM3 optimization implementation based on Zbb extension for RISC-V platform, automatically detects and utilizes Zbb instruction set acceleration in SM3 hash calculation. (Architecture-related: RISC-V platform optimization)
  ↳ No PR: [4dbb537](https://github.com/openssl/openssl/commit/4dbb537bd1ea1fcc5ea19f6214e5f84cab9d0e94)
- The SM2 curve uses constant time modular inversion operation to fix the CVE-2025-9231 security vulnerability. (Architecture-related: SM2 curve behavior)
  ↳ No PR: [3b66c97](https://github.com/openssl/openssl/commit/3b66c974c45422dfe2bb9ef8db9653e0539dd05b)
- Fix the memory allocation function to comply with C11 and POSIX specifications and solve compatibility issues. (Architecture-related: platform compatibility)
  ↳ No PR: [648803a](https://github.com/openssl/openssl/commit/648803a17e4c1511ebc90a78542d0e649b6eb318), [ff3caae](https://github.com/openssl/openssl/commit/ff3caae4d288c27b4268a3e55fb94a5abeff5881)
- Fix asn1_write_micalg function, add support for SHAKE algorithm and add I/O error checking. (Architecture-related: ASN1 core function)
  ↳ No PR: [ea7b971](https://github.com/openssl/openssl/commit/ea7b971563c9692c27b926e29f32d4da2385f258)
- Increased PKCS12 default MAC salt length from 8 bytes to 16 bytes to comply with NIST SP 800-132. (Architecture-related: public API)
  ↳ No PR: [995e948](https://github.com/openssl/openssl/commit/995e9489e62ff1965553c4e127183565ccfe4265)
- Add CPU information printing support for PowerPC architecture. (Architecture-related: Platform compatibility)
  ↳ No PR: [f8f3573](https://github.com/openssl/openssl/commit/f8f3573a061f7675c6b9277d715483a3a3405e90)

### SSL/TLS/QUIC Layer
- Separate the storage of handshake traffic hashes from tls13_change_cipher_state, and store it explicitly by the state machine at the appropriate time. (Architecture-related: TLS 1.3 state machine reconstruction)
  ↳ No PR: [4579a18](https://github.com/openssl/openssl/commit/4579a18cf5129479e781bf05e168204ca739fa3c), [c7f9c4d](https://github.com/openssl/openssl/commit/c7f9c4d7d184cec988251b2a9c697302774fbe77)
- Add OCSP multi-staple support for TLS 1.3 server certificates, allowing independent OCSP responses to be provided for each certificate in the certificate chain. (Architecture-related: public API)
  ↳ No PR: [b1b4b15](https://github.com/openssl/openssl/commit/b1b4b154fd389ac6254d49cfb11aee36c1c51b84)
- Added SSL_CTX_set_ec_point_formats and SSL_set_ec_point_formats interfaces for configuring EC point formats, and added SSL_OP_LEGACY_EC_POINT_FORMATS option. (Architecture-related: public API)
  ↳ No PR: [03541d7](https://github.com/openssl/openssl/commit/03541d7302d016aa28d436364d72d58baa3e2114)
- Introduced the SSL_OP_SERVER_PREFERENCE option to replace the inaccurately named SSL_OP_CIPHER_SERVER_PREFERENCE. (Architecture-related: public API)
  ↳ No PR: [51ce549](https://github.com/openssl/openssl/commit/51ce5499f9bd1f12cf08f511faaf163b0c4448bb)
- Fixed an issue where the client failed to correctly save the signature algorithm extension during TLS post-handshake authentication. (Architecture-related: TLS handshake behavior)
  ↳ No PR: [ddd99d5](https://github.com/openssl/openssl/commit/ddd99d52d30e2fdae08f9684947cba45ce53898b)
- Adjusted the cleaning order when SSL connection is released, ensured that SSL_get_app_data() in the callback can be accessed normally, and fixed OCSP resource release. (Architecture-related: public API)
  ↳ No PR: [2100cf2](https://github.com/openssl/openssl/commit/2100cf2ee0d377976d28c9e04eefae4e1b5373ea), [2ebae65](https://github.com/openssl/openssl/commit/2ebae654d5baf1c3781d1228ce0fd9d28e02d08b), [f2488a5](https://github.com/openssl/openssl/commit/f2488a567ba3376c7d2e2cb4567a20111c6df23b)
- Fixed the usage issue of CCM cipher suites in QUIC TLS API, introduced internal flags to distinguish internal QUIC connections, and ensured that cipher suite restrictions take effect correctly. (Architecture-related: QUIC TLS API)
  ↳ No PR: [207cd5b](https://github.com/openssl/openssl/commit/207cd5bb975f1cda542757b9695ac4e5bdb71576), [366b264](https://github.com/openssl/openssl/commit/366b2643cb6f63c9e73b95c22b979c77e93625ec)
- Change the QUIC 0-RTT handshake read key in advance to SSL_set_accept_state to avoid the need for the application to additionally call SSL_do_handshake when there is no data to read. (Architecture-related: SSL_set_accept_state)
  ↳ No PR: [9505105](https://github.com/openssl/openssl/commit/95051052b319d346a8aa3d34d6105d683bb77294)
- Fixed edge case for signature algorithm negotiation: allow self-signed certificates to use signature algorithms not declared in the extension, and correct memory allocation calls; also avoid sending TLS 1.3 signature algorithms to TLS 1.2 clients. (Architecture-related: Signature algorithm negotiation behavior)
  ↳ No PR: [a5f98e6](https://github.com/openssl/openssl/commit/a5f98e6da521934455898d49c8b2152a60b46925)
- Fixed a problem that may cause a crash when the SSL_CONNECTION pointer in SSL_do_handshake is null, and added a null pointer check. (Architecture-related: external behavior)
  ↳ No PR: [7f6cc86](https://github.com/openssl/openssl/commit/7f6cc862c69800a72c49fcfe89e2931ee4ca2e7a)
- Fixed the problem of calling SSL_new() when using QUIC server method. (Architecture-related: QUIC public API)
  ↳ No PR: [5341e27](https://github.com/openssl/openssl/commit/5341e271d9eb211d3b61d370a68ee4ce4147cd12)
- Fixed the problem of calling SSL_accept() on the QUIC server connection object, which can now be used normally. (Architecture-related: QUIC public API)
  ↳ No PR: [38bf6f3](https://github.com/openssl/openssl/commit/38bf6f3036d1baddbe4618a219aaf17d460091d9), [44af96b](https://github.com/openssl/openssl/commit/44af96b9c57573e20b52d2204dfe0ff3bd53dc39), [b637fbe](https://github.com/openssl/openssl/commit/b637fbe781ab40afca700a44fa78b8748f5892dd)
- Fixed an issue where SSL_poll incorrectly reported that the stream was writable when it was actually not writable, and added a check on the sending credit limit. (Architecture-related: public API)
  ↳ No PR: [4efd1a2](https://github.com/openssl/openssl/commit/4efd1a26822a05e900a9dcffc0d6554efece7923), [85a8eba](https://github.com/openssl/openssl/commit/85a8eba56769c4d25a66e0b52e8fb3e76bbe4afe)
- Fixed the issue where SSL_accept() and SSL_get_error() incorrectly added errors to the error stack when passing in an error object type, and ensured that SSL_set_accept_state() and SSL_set_connect_state() no longer generate false errors. (Architecture-related: public API)
  ↳ No PR: [cb5bb89](https://github.com/openssl/openssl/commit/cb5bb8916fa0e044e6658c8b3db6d7c672cb25fe)
- Fix the processing logic of host names and IP addresses in the SSL_set1_host and SSL_add1_host functions, and update related documents. (Architecture-related: public API)
  ↳ No PR: [1eee02d](https://github.com/openssl/openssl/commit/1eee02d3e710e01d864c37708f64e83511627e28)
- Add a dummy field to the poll builder structure to solve the Microsoft compiler's compatibility issue with empty structures. (Architecture-related: platform compatibility)
  ↳ No PR: [04b59c4](https://github.com/openssl/openssl/commit/04b59c419933adca4cde1d97e2c7522cb21c3468)
- Fix the handling of error downgrade signals to ensure that connections are correctly rejected when non-compliant servers send error downgrade signals. (Architecture-related: external behavior)
  ↳ No PR: [290fd4a](https://github.com/openssl/openssl/commit/290fd4a0c87b5f777e928a80503ee20ca6e768de)
- Fixed two problems in application data record processing in DTLS: discarding empty records to avoid misjudgment failure of SSL_read(), and repairing the pointer not advancing after the buffer record is released, resulting in repeated reading of empty data. (Architecture-related: external behavior)
  ↳ No PR: [a23d5e2](https://github.com/openssl/openssl/commit/a23d5e20f162564d8c13bda50ea358caaa7b047c), [d2a33ef](https://github.com/openssl/openssl/commit/d2a33efd394f216e04a28a3ce69526dbbec2385a), [1afcc27](https://github.com/openssl/openssl/commit/1afcc27f945272f29905c32ba725757470fb0e6e)
- Fixed behavioral issues related to renegotiation and session reuse in DTLS and TLS protocols: DTLS terminates the connection when receiving a no_renegotiation warning, and the TLSv1.3 server no longer sends PSK extensions incorrectly after SSL_clear(). (Architecture-related: external behavior)
  ↳ No PR: [e5feca0](https://github.com/openssl/openssl/commit/e5feca0659ef6119f6cedfab1b6af034735723ff), [aa8bca2](https://github.com/openssl/openssl/commit/aa8bca2e81030560d690cb68bbcbe8b7d00d1d29), [df5dff2](https://github.com/openssl/openssl/commit/df5dff26efb6cdc96ebe50c35af394a1121e77fe), [7f6e66b](https://github.com/openssl/openssl/commit/7f6e66b048cb50dd5381211ef2006ae5e912a914)
- On SSL connection reset, reset the local transport parameter consumed flag of QUIC TLS to 0. (Architecture-related: QUIC TLS internal behavior)
  ↳ No PR: [9bad2b8](https://github.com/openssl/openssl/commit/9bad2b86e892b70ea65e87c409ae90f625d3c12c)
- Fixed the problem of overwriting the connection custom extension when SSL_set_SSL_CTX() switches context, and retains the connection custom extension by adding a new flag to avoid the loss of QUIC transmission parameters. (Architecture-related: public API)
  ↳ No PR: [403ba31](https://github.com/openssl/openssl/commit/403ba31a02e47d37070036529966d5a94d98c6fd)
- Fixed the inconsistency between the SSL_select_next_proto function parameter name between the header file and the document. (Architecture-related: public API)
  ↳ No PR: [0fe6c21](https://github.com/openssl/openssl/commit/0fe6c21a7dac34e346be778fdf080a1a8cdc246c)
- Fixed the problem of QUIC ACK manager infinite probe timeout before client handshake confirmation, keeping probe timeout until receiving HANDSHAKE_DONE frame according to RFC 9002 requirements; added is_server parameter to distinguish client and server behavior. (Architecture-related: public API)
  ↳ No PR: [cdbface](https://github.com/openssl/openssl/commit/cdbfacead0d07ed47fa1087d633acf6f6399aa2c)
- Fixed the problem of cooperation between SSL_poll() and SSL_shutdown() in QUIC connection. When all streams are refreshed, the channel is notified so that SSL_poll() can return the event correctly, so that SSL_shutdown() can continue to complete the shutdown. (Architecture-related: public API)
  ↳ No PR: [1d92f3b](https://github.com/openssl/openssl/commit/1d92f3b8b0e580f761a1d2789e2b81624420b098)
- Add SSLfatal call to ensure SSL fatal error assertion is triggered when key logging fails. (Architecture-related: SSL error handling behavior)
  ↳ No PR: [7d78cd7](https://github.com/openssl/openssl/commit/7d78cd722b63e53a668c7ec13b9eeb6e13e32f13)
- Add CRYPTO_FREE_REF call in ossl_quic_free_token_store, which fixes a memory leak that may occur on platforms that do not support atomic operations. (Architecture-related: platform compatibility)
  ↳ No PR: [d2a71ed](https://github.com/openssl/openssl/commit/d2a71ed94e82f96a589fbc017d525d415b427337)
- When the client has no key to share, immediately abort the connection. (Architecture-related: TLS 1.3 handshake behavior)
  ↳ No PR: [47b0f17](https://github.com/openssl/openssl/commit/47b0f172aa60a0faa3428cc739e3efd71f756aa7)
- Fix the OPENSSL_VERSION_NUMBER macro so that its status bit is always zero, consistent with the document description. (Architecture-related: version and compatibility)
  ↳ No PR: [7232f24](https://github.com/openssl/openssl/commit/7232f2449565e1756bf3e3c4e8af23ff7d5033a6)
- Fixed the problem of incorrect value when passing inner content type on big-endian platform, ensuring that only the lowest byte is passed. (Architecture-related: platform compatibility)
  ↳ No PR: [ea373a3](https://github.com/openssl/openssl/commit/ea373a3e533eb8752cf980dd7dcf627e3fb25557)
- Removed unused JSON floating point encoding functions to avoid dependence on the libm math library. (Architecture-related: build dependencies)
  ↳ No PR: [0e41862](https://github.com/openssl/openssl/commit/0e418628998d0337599643c1e4054c60e5f21ec4)
- Change the boolean parameter in JSON encoding from int to stdbool type. (Architecture-related: public API)
  ↳ No PR: [52dba1c](https://github.com/openssl/openssl/commit/52dba1c098d9b0388afa4db2fbe3461df67461c6)
- Add verification in QUIC TLS test to confirm that BIO does not need to be set when using QUIC TLS API. (Architecture-related: QUIC TLS API behavior)
  ↳ No PR: [445c094](https://github.com/openssl/openssl/commit/445c0942cd19d78a96ea5c351c25c2613ab76c56)
- Force the permissions of the SSLKEYLOGFILE log file to 0600, ensuring that only the owner can read and write. (Architecture-related: public API)
  ↳ No PR: [e7e7950](https://github.com/openssl/openssl/commit/e7e79509986a3b6134ce3bbf30d7afcfd117c7eb)
- Changed the is_server parameter type of the QUIC ACK manager creation function ossl_ackm_new from char to int, and corrected the type conversion in the implementation. (Architecture-related: QUIC internal API)
  ↳ No PR: [92330c8](https://github.com/openssl/openssl/commit/92330c8f80e4dbfc45b7718d9ed526f196daba0a), [d777def](https://github.com/openssl/openssl/commit/d777deffbae3dc27f57c3086f385f91a62b1e5bd)
- Adjust the error type when SSL key derivation and ML-KEM encapsulation fails to illegal parameter alert. (Architecture-related: external behavior)
  ↳ No PR: [5da4ea1](https://github.com/openssl/openssl/commit/5da4ea10be8cf8ca66dff95c9997966f21c82029), [e66097f](https://github.com/openssl/openssl/commit/e66097fc6687750ac792986a71375b23793766c2)

### EVP Layer
- Added symmetric key management (SKEYMGMT) support in the FIPS provider, including algorithm support, EVP_SKEY_import_SKEYMGMT function and the key_type parameter of the derive_skey function. (Architecture-related: public API)
  ↳ No PR: [71d3703](https://github.com/openssl/openssl/commit/71d3703e5d3715b23554a4818a2d480f9d306bdb), [f289c45](https://github.com/openssl/openssl/commit/f289c45b16a34938f8aebb6fb3afc8bf92f2708b), [1351299](https://github.com/openssl/openssl/commit/1351299d601bd85b96b82ffec37d3700a6296616), [f5fe236](https://github.com/openssl/openssl/commit/f5fe2366af5a2758f88a13a08e86bd5db2a6c3e3), [034cd83](https://github.com/openssl/openssl/commit/034cd8389386cd1507d7c1430f17b86f89185d46), [e8b03fb](https://github.com/openssl/openssl/commit/e8b03fbcdab154e3b253e72af0207a017b0fe229), [d1d94e0](https://github.com/openssl/openssl/commit/d1d94e0fbe2fe2b99314bfcddad092d1d00f01b0)
- Added EVP_PKEY_derive_SKEY and EVP_KDF_derive_SKEY series APIs to support directly deriving security key objects through key exchange and KDF. (Architecture-related: public API)
  ↳ No PR: [7d42bec](https://github.com/openssl/openssl/commit/7d42becc0d3ec1d1f16054288ea897b3cd85961d), [b5d0d06](https://github.com/openssl/openssl/commit/b5d0d061d1c5468bb45bcf3495a1b9d8d3943264), [55b2bf1](https://github.com/openssl/openssl/commit/55b2bf1abc38d851357b486a9db951f3c0793c4d)
- Added HKDF algorithms with fixed digests: HKDF-SHA256, HKDF-SHA384 and HKDF-SHA512. The digests of these algorithms cannot be changed, and the corresponding RFC 8619 algorithm identifiers are defined. (Architecture-related: public API)
  ↳ No PR: [d1a8d5a](https://github.com/openssl/openssl/commit/d1a8d5a8330a8c9d939e18a22f7382af090cf108)
- HKDF function enhancement: allow the salt parameter to be set to null, and extend the available parameters to support digest algorithms and modes. (Architecture-related: public API)
  ↳ No PR: [12eb6c5](https://github.com/openssl/openssl/commit/12eb6c58ff2a8d857924b3020d30c8d485ace0a7), [5b80019](https://github.com/openssl/openssl/commit/5b800192f2f9b7b0d3a8add2117fb1ecdd029684), [7271179](https://github.com/openssl/openssl/commit/727117960c0a47073290de936fb517db12351174)
- ECX, EC, DSA key management has added security category parameter support. (Architecture-related: public API)
  ↳ No PR: [077ed48](https://github.com/openssl/openssl/commit/077ed48edf66ffb5cbb29d3a0e6773f55d73a82c), [5dcf380](https://github.com/openssl/openssl/commit/5dcf3806e2503d40b7efc450ef8dbcf3b27373dd), [3851771](https://github.com/openssl/openssl/commit/38517717920ac265a5cf94b496070b6387c980e5), [6cc9a3f](https://github.com/openssl/openssl/commit/6cc9a3fd0bd1aa137ecb57af7738042abc2d4924), [ae36afe](https://github.com/openssl/openssl/commit/ae36afee1157dd1f9fdffa99ef14791e07f97d94), [fdc0c8a](https://github.com/openssl/openssl/commit/fdc0c8a3ab2958739e54b733f8904a166bf7a360), [4577a4a](https://github.com/openssl/openssl/commit/4577a4a59f5ec368f3bb062ed34abdf08dbbbd27), [4da326a](https://github.com/openssl/openssl/commit/4da326af2a7c71fbc791614e36c8acd42c47521d)
- Expose the configurable parameters of the symmetric key management module, support passing raw byte data through the OSSL_SKEY_PARAM_RAW_BYTES parameter; add the EVP_PKEY_get_security_category function. (Architecture-related: public API)
  ↳ No PR: [273ceaa](https://github.com/openssl/openssl/commit/273ceaa7c323fc5c9be8fd0b303972058de4a1ed), [8bdb122](https://github.com/openssl/openssl/commit/8bdb1228770df311fb059ee8cf52d11a93e37142), [c3215ac](https://github.com/openssl/openssl/commit/c3215ac5738c9d2be846a7146cb5373702d47e6d), [17e7e85](https://github.com/openssl/openssl/commit/17e7e85d1539ef1202151ce519497d7ced5157ad), [1d4d18d](https://github.com/openssl/openssl/commit/1d4d18daae575c2874587ee8ca6e3ec9d57c5dbb), [fa2e4f7](https://github.com/openssl/openssl/commit/fa2e4f7badaf736aa09807feea77572366f8976c)
- Allow key generation to be performed after copying the PKEY context without setting the operation. (Schema related: public API)
  ↳ No PR: [2c74a8d](https://github.com/openssl/openssl/commit/2c74a8d1ef4e9c4b4468afefedb1f72425772a37)
- Fixed the silent error in EVP_CIPHER_CTX_get_updated_iv, added the OSSL_PARAM_set_octet_string_or_ptr API function, and used this function in the get_ctx_params implementation of multiple ciphers to correctly set the IV parameters. (Architecture-related: OSSL_PARAM_set_octet_string_or_ptr)
  ↳ No PR: [a0ff819](https://github.com/openssl/openssl/commit/a0ff819e537854e7e96d26a0deb56d703006b40f), [418609e](https://github.com/openssl/openssl/commit/418609e115bd694438171ca1f491b04aa3605a43)
- Fixed the problem of EVP_PKEY_CTX_dup() not copying the keymgmt pointer, to avoid segfault caused by accessing the null pointer when subsequently calling EVP_PKEY_CTX_derive_set_peer_ex(). (Architecture-related: public API)
  ↳ No PR: [3c22da7](https://github.com/openssl/openssl/commit/3c22da73465f5dd211299e64f0de8786dcaf86c3)
- Add error queue entries for keymgmt, signature verification and asynchronous encryption operations, and add more detailed error messages when the provider operation fails. (Architecture-related: public API)
  ↳ No PR: [72351b0](https://github.com/openssl/openssl/commit/72351b0d18078170af270418b2d5e9fc579cb1af)
- Add error queue entries for providers when signing and verification operations fail, to compensate for situations where they may not add errors. (Architecture-related: public API)
  ↳ No PR: [3a57fb1](https://github.com/openssl/openssl/commit/3a57fb1386df87481233ed046fc16bf3332de046)
- Fixed the EVP_RAND_nonce function to correctly return actual results and added parameter error checking to improve API robustness. (Architecture-related: public API)
  ↳ No PR: [a2b9120](https://github.com/openssl/openssl/commit/a2b9120d15073ab596452fc361d01bb26ee13773), [a2cd7ec](https://github.com/openssl/openssl/commit/a2cd7ecd75dcd0de214319ec11bf5b3701bec7a3)
- Fixed the error handling in the signature verification operation to avoid general errors overwriting provider-specific errors. (Architecture-related: public API)
  ↳ No PR: [b9ff440](https://github.com/openssl/openssl/commit/b9ff440dd613e0c65527ef7eaf565f618979ecce)
- Fixed the memory leak problem caused by xalg->parameter not being released when EVP_CIPHER_param_to_asn1 fails in PKCS7_dataInit. (Architecture-related: public API)
  ↳ No PR: [bda2473](https://github.com/openssl/openssl/commit/bda2473a44e4534c3c640ce89a0971874165c6df)
- Fix the initialization error of the output buffer length during RSA public key encryption in EVP_SealInit, ensuring that the RSA module length is used instead of the input KEK length. (Architecture-related: public API)
  ↳ No PR: [f815ee1](https://github.com/openssl/openssl/commit/f815ee19e066ddb0896041c92844e3c7fd36e3fd), [75c7aae](https://github.com/openssl/openssl/commit/75c7aae5fc8fe4c8d280613bff8d8bf3da0e8c40)
- Fix the processing of EVP_PKEY_can_sign when query_operation_name returns NULL, and add corresponding tests. (Architecture-related: public API)
  ↳ No PR: [9bb53c7](https://github.com/openssl/openssl/commit/9bb53c7f04d8903e78ce39a3080eb7708f1516ed)
- Deprecated function declarations and definitions related to EVP_PKEY_ASN1_METHOD. (Architecture-related: public API deprecated)
  ↳ No PR: [52d212d](https://github.com/openssl/openssl/commit/52d212dd700f7600ea3454faff4e799caf7c736e)
- Change the evp_skey_alloc function to non-static and add a declaration so that it can be called by multiple source files. (Architecture-related: internal interface adjustment)
  ↳ No PR: [3425da5](https://github.com/openssl/openssl/commit/3425da502dd9f2568c96fa20d63b92f1c41288f8)
- Added i2d_PKCS8PrivateKey API, used to output PKCS#8 format private key encoding, and refactored i2d_PrivateKey implementation. (Architecture-related: public API)
  ↳ No PR: [8d2e4d6](https://github.com/openssl/openssl/commit/8d2e4d6d8c927f05948e048fcbf62982feaf11b4)

### X.509 & PKI Layer
- Support parsing private key information in PKCS#8 V2 format, verifying version numbers only allows v1 and v2, and rejects v1 containing public keys. (Architecture-related: parsing behavior)
  ↳ No PR: [064bb16](https://github.com/openssl/openssl/commit/064bb16454ec4d55a1e40cb673232c54e9f28196)
- Added public API X509_CRL_get0_tbs_sigalg, used to obtain the TBSCertList signature algorithm identifier of CRL. (Architecture-related: public API)
  ↳ No PR: [21f1b67](https://github.com/openssl/openssl/commit/21f1b677d54ef50fe4e262e032372dfaff88fbf4)
- Add the alias contentCommitment (corresponding to nonRepudiation) for the X.509 keyUsage extension, and update the output logic to avoid displaying the alias repeatedly. (Architecture-related: public API)
  ↳ No PR: [6b93db7](https://github.com/openssl/openssl/commit/6b93db7bfd572e81fac581c5be7b0d7509febb80)
- Fix the error of multi-line output in crl command, make sure to use global variables for setting. (Architecture-related: public API)
  ↳ No PR: [7bf52a6](https://github.com/openssl/openssl/commit/7bf52a6f6f0d22c3a1aba39d21aabf0c8a818ba7)
- Fixed the problem that the extension list was not cleared correctly after deleting the certificate, CRL and the last extension in the CRL entry; restructured the deletion logic and added an auxiliary function to automatically clear the empty extension list. (Architecture-related: public API)
  ↳ No PR: [30930f8](https://github.com/openssl/openssl/commit/30930f861578852dfbb10ad14440e1696172e68c), [4620e09](https://github.com/openssl/openssl/commit/4620e09c54c8bee62040e4f84a50391e8ee60981)
- Add error checking for i2d_X509_NAME return value in X509_ocspid_print, and jump to error handling when failure occurs. (Architecture-related: public API)
  ↳ No PR: [d650e96](https://github.com/openssl/openssl/commit/d650e962d8f2d6ba57b2cd76ecd0c31906fd2d5a)
- Fixed the memory leak caused by the extension object not being released in the X509V3_EXT_add_alias function. (Architecture-related: public API)
  ↳ No PR: [5f661e4](https://github.com/openssl/openssl/commit/5f661e4e96bc3bfa52b4e0735f407cb41f162869)
- Fixed the issue where the -addreject option in the x509 command incorrectly adds trust instead of rejection (CVE-2025-4575). (Architecture-related: public API)
  ↳ No PR: [0eb9acc](https://github.com/openssl/openssl/commit/0eb9acc24febb1f3f01f0320cfba9654cf66b0ac)
- Fix the race condition caused by not holding the read lock when acquiring the X509_STORE object; expose the internal read lock function and call it correctly in related functions. (Architecture-related: public API)
  ↳ No PR: [07f65e1](https://github.com/openssl/openssl/commit/07f65e16c209e06be9887c2d5f943f528e3f0139), [994774b](https://github.com/openssl/openssl/commit/994774b4ca61cf7ecf42750a7d374dd2865f1ce3)

### Cross-cutting / Other Architecture-related Changes
- Introduced a thunk mechanism for the OPENSSL_sk interface, allowing to set a custom release function and call the function in OPENSSL_sk_pop_free to avoid UBSan warnings. (Architecture-related: public API)
  ↳ No PR: [21b170d](https://github.com/openssl/openssl/commit/21b170df9fd2c6080da119144eac969a940dee38)
- Reconstruct the parameter auxiliary code and add the OSSL_PARAM_set_octet_string_or_ptr function. (Architecture-related: public API)
  ↳ No PR: [ac01b9a](https://github.com/openssl/openssl/commit/ac01b9a9fdd33529ed576bbcbb8f8cdb30da2ea2)
- Added array memory allocation routine, automatically performs integer overflow checking, and makes allocation semantics clearer. (Architecture-related: public API)
  ↳ No PR: [fa9b7b9](https://github.com/openssl/openssl/commit/fa9b7b930e3e59f5b30de0e8a6755bfaafdd5c49), [5fab189](https://github.com/openssl/openssl/commit/5fab189ddd042643f1d148dd9e704d3b1154d0da), [f3a4d05](https://github.com/openssl/openssl/commit/f3a4d05c5889b571d8b99c645fa41533b27ec44b), [bd1c597](https://github.com/openssl/openssl/commit/bd1c59739d57ca27162bd582161a5cbddba21999), [351caeb](https://github.com/openssl/openssl/commit/351caebeac7a71896012222d10b9364e4a8c3e94), [354e78c](https://github.com/openssl/openssl/commit/354e78c1771eac33b62c732975c72af7f2190ab4), [5398d5c](https://github.com/openssl/openssl/commit/5398d5cbd90507a29167a4d7f4174f8474fd3a7b)
- Fix default private key DER output format to PKCS#8, and extend -traditional option to support DER output. (Architecture-related: CLI behavior)
  ↳ No PR: [f492649](https://github.com/openssl/openssl/commit/f492649b99012b0b8ab5c83b66b20aa65bee1f1c)
- Removed the deprecated _strlen31 function with potentially serious side effects and its strlen macro redefinition on the Win64 platform. (Architecture-related: Platform compatibility)
  ↳ No PR: [b0d363a](https://github.com/openssl/openssl/commit/b0d363a2cb039eac2908b7cb00b395235373193e)
- Allows reuse of thread-local storage keys in threadless configurations, breaking the hard limit of 256 LIB_CTX values. (Architecture-related: Platform compatibility)
  ↳ No PR: [b6d01d1](https://github.com/openssl/openssl/commit/b6d01d1b1fef2e98a956b7ba4e8443cf7d916dcb)
- Correct the synthesis logic of the pre-release version identifier in the OPENSSL_VERSION_NUMBER macro to ensure that 0xfL is correctly generated when there is no pre-release version. (Architecture-related: version and compatibility)
  ↳ No PR: [ba2c314](https://github.com/openssl/openssl/commit/ba2c314a60d9f42d1d2e63ea0f791cc04e03005b)
- Add conditional compilation to FIPS-specific parameters in multiple KDF and encryption algorithm implementations, making them available only in FIPS mode, enhancing FIPS compliance. (Architecture-related: FIPS compliance)
  ↳ No PR: [004077b](https://github.com/openssl/openssl/commit/004077be1bd3aa68818c51e2879c2d8ffd841f02), [472ead8](https://github.com/openssl/openssl/commit/472ead8be38f0101e7ccdc6764868f1fc0e4b55b), [88d544c](https://github.com/openssl/openssl/commit/88d544c83066783527b59878682c006e6d464ed8), [ba2b292](https://github.com/openssl/openssl/commit/ba2b292e96677c4dbff3662c87061dc5b03c8c7b), [c098acb](https://github.com/openssl/openssl/commit/c098acb0542173380a63e62e37090c42628e34f4), [fd3a6a4](https://github.com/openssl/openssl/commit/fd3a6a49ee9e37fdae69e43ad2b44d84115b773d), [1b71051](https://github.com/openssl/openssl/commit/1b71051b864fb956b7201ccd1a51f4e7124e4334), [b411ef0](https://github.com/openssl/openssl/commit/b411ef0b530b78e68cffb76fd3e77b8f3b178e6a), [b27f840](https://github.com/openssl/openssl/commit/b27f8403517b461006729f7720ca20dcef2ba9cc), [f9bf224](https://github.com/openssl/openssl/commit/f9bf224ef980a7c93ee699dabda354d3b32b426a), [3473f69](https://github.com/openssl/openssl/commit/3473f699fdc4d0951e82349f56e68ec1c035be51), [2d1280e](https://github.com/openssl/openssl/commit/2d1280e5ee1c1589ab7c958206f6d97a5ae7be9f), [40dd58e](https://github.com/openssl/openssl/commit/40dd58e016430d0b5f481784ba0b3a7cb3c3c621), [60f8ff1](https://github.com/openssl/openssl/commit/60f8ff15112c1f74b2a069f9ea8abfee50ddb25c), [b830eba](https://github.com/openssl/openssl/commit/b830ebaf62cdbb7e572d4580b5569533dc15c88f), [2f205fc](https://github.com/openssl/openssl/commit/2f205fc496e32a59666f26b4fbb2774af06a86f4), [226b5a5](https://github.com/openssl/openssl/commit/226b5a5ea48ecf06aa985ef20da90bb99d57bb93), [4e1eaa1](https://github.com/openssl/openssl/commit/4e1eaa17c74a12bd732ecdf4f5683f88d6268b9b), [fc7a72d](https://github.com/openssl/openssl/commit/fc7a72db242a0ea808d2f65e2e3f54ac25ffbf55), [1aae0a4](https://github.com/openssl/openssl/commit/1aae0a4016127c8cf73b5d33866622529ec8aa8e), [a9d7e69](https://github.com/openssl/openssl/commit/a9d7e696ec9cd1b41ec54762e689c8a31dcc8c43), [ecc3491](https://github.com/openssl/openssl/commit/ecc3491d536c53668519216eea0c3480053268ce)
- Migrate thread-local storage of RCU, ERR library and asynchronous tasks to the new thread-local key management API. (Architecture-related: Internal API: Thread-local key management)
  ↳ No PR: [2cb068f](https://github.com/openssl/openssl/commit/2cb068fb2259fe8a92d8d67bff7486ded5a31cf2), [d6d5170](https://github.com/openssl/openssl/commit/d6d5170ed205838165dca1cf2f66c7d7a1176802), [21980b9](https://github.com/openssl/openssl/commit/21980b981395ab64edabb1432feb9f15798c68e7)
- Change parameter splitting to support spaces within quotes to avoid command injection, and use custom quotes to construct commands on Windows. (Architecture-related: platform compatibility)
  ↳ No PR: [287bbb2](https://github.com/openssl/openssl/commit/287bbb28b09e930a8691efc92a5087bb951edb6b)
- Update INSTALL.md to explain that LMS support is disabled by default and needs to be explicitly enabled through the enable-lms option. (Architecture-related: build and installation methods)
  ↳ No PR: [17a1637](https://github.com/openssl/openssl/commit/17a1637a3f002d7f8276947cc151440c64984451), [495f5fa](https://github.com/openssl/openssl/commit/495f5fa0ba67c03659dd5288f3f7aa6913771426)
- Fixed multiple build issues on UEFI platforms, including disabling OSSL_PARAM_REAL branch, adding stddef.h header file inclusion and adding RIO_POLL_METHOD_NONE method. (Architecture-related: platform compatibility)
  ↳ No PR: [57f9447](https://github.com/openssl/openssl/commit/57f94478060faeb688ebbd9fde1aa73abae00636), [44e9c5a](https://github.com/openssl/openssl/commit/44e9c5a3edd199ed7d7fe427fe0e1ef76dc52663), [7e53ffa](https://github.com/openssl/openssl/commit/7e53ffa144264024aa7e596c04c998946b4d85b8)
- Added nightly testing tasks for riscv64 architecture in the CI workflow. (Architecture-related: platform compatibility)
  ↳ No PR: [3513a83](https://github.com/openssl/openssl/commit/3513a830cc159c913b6c9bf1cbaf1577a1f47808)
- Fix build failure on OS X 10.4 Tiger, add PowerPC build configuration and adjust header files. (Architecture-related: Platform compatibility)
  ↳ No PR: [7eee9d5](https://github.com/openssl/openssl/commit/7eee9d543e467c4767ebbbd12517fe5c9565202a)
- Fixed the build problem of VC-WIN64-CLANGASM-ARM target on Windows ARM64, added the check of _M_ARM64 macro. (Architecture-related: platform compatibility)
  ↳ No PR: [c66d976](https://github.com/openssl/openssl/commit/c66d9760a77c5a8ec4b8bdb6000b4213384d0e3e)
- Add deprecated macros for OpenSSL 3.6.0. (Architecture-related: public API: deprecated macros)
  ↳ No PR: [1bc3191](https://github.com/openssl/openssl/commit/1bc3191b6845fa54f6962055df795fbbaefb12be)
- Pin GitHub Actions from untrusted vendors in CI workflows to specific commit hashes. (Architecture-related: Build Security)
  ↳ No PR: [9ee9a51](https://github.com/openssl/openssl/commit/9ee9a519be803f2b1a7a8b82167c7a883a0483fc)
- Add parentheses to the parameters of macros ossl_likely and ossl_unlikely to avoid priority issues. (Architecture-related: public API)
  ↳ No PR: [cdd01b5](https://github.com/openssl/openssl/commit/cdd01b5e0734b0324251b32a8edd97f42ba90429)
- Supplement the description of LMS signature algorithm in the FIPS self-test description. (Architecture-related: public API)
  ↳ No PR: [0c53442](https://github.com/openssl/openssl/commit/0c534426236e55bfe2222d742ff5f8cf32b4322e)

### BIO Layer
- Removed reference to poll.h on NonStop platforms to avoid including the header file. (Architecture-related: platform compatibility)
  ↳ No PR: [ff030ad](https://github.com/openssl/openssl/commit/ff030ad5bd1c6196e640b1338dac23c1ce3a3154)
- Fixed the problem that the i2d_ASN1_bio_stream() function always returns 1 when the SMIME_STREAM flag is not set, so that it correctly returns the actual result of ASN1_item_i2d_bio(). (Architecture-related: i2d_ASN1_bio_stream)
  ↳ No PR: [3edb1f0](https://github.com/openssl/openssl/commit/3edb1f09c62c058edf4039587ef35f6b074e0870)
- Fix the problem of BIO_printf when formatting negative numbers %e and INF/NAN, avoid infinite loops and standardize the display of invalid values. (Architecture-related: public API)
  ↳ No PR: [fb555eb](https://github.com/openssl/openssl/commit/fb555eb7a1d523e9df5584b44d16d0f72417bd19), [b56dd5b](https://github.com/openssl/openssl/commit/b56dd5bfec8e790cc2d5b1bdca6ecd350a3b7779)
- Fixed the unreleased memory leak in tmpout due to OPENSSL_malloc failure in the PKCS7_verify function, and moved the BIO_free call to a unified error handling path. (Architecture-related: public API)
  ↳ No PR: [9882d38](https://github.com/openssl/openssl/commit/9882d389df71ef7163c7769b4431a0dbe713ab65)
- Fixed the problem of cipher BIO not marking the finished status when encountering a non-retryable EOF, to avoid subsequent BIO_flush or read operations from incorrectly finalizing the encryption status again, resulting in decryption failure. (Architecture-related: cipher BIO behavior)
  ↳ No PR: [005fa3e](https://github.com/openssl/openssl/commit/005fa3e00e1ccfd83aa99d28e2eff55597dd5fc2)
- Fixed BIO_CTRL_DGRAM_QUERY_MTU processing of IPv4-mapped IPv6 addresses, by reusing the dgram_get_mtu_overhead function to correctly subtract the corresponding IP header size. (Architecture-related: BIO layer behavior)
  ↳ No PR: [a71b4fa](https://github.com/openssl/openssl/commit/a71b4fae432796a49c3b9d32ae29354b23809c1f)
- Fixed the handling of negative width parameters in bio_print.c to conform to the printf specification. Negative width is now correctly regarded as a left-aligned flag. (Architecture-related: external behavior)
  ↳ No PR: [7eb18e7](https://github.com/openssl/openssl/commit/7eb18e768dbec07dbac7e883629c5d5875c7f7b8)
- Fixed the problem of incorrectly adding a prefix when the value is zero in octal and hexadecimal formatting. (Architecture-related: external behavior)
  ↳ No PR: [0f6e826](https://github.com/openssl/openssl/commit/0f6e826f7b70770935b3766efad05d7755a74edc)
- Fixed the problem of OSSL_DECODER_CTX_new_for_pkey not releasing the write lock in the memory allocation failure path to avoid assertion failure caused by repeated locking by the same thread. (Architecture-related: public API)
  ↳ No PR: [c052725](https://github.com/openssl/openssl/commit/c0527256d2e6a148931e1d8b9b0ff4af7564caae)
- Fixed the problem of BIO_snprintf not terminating output with \0 in the wrong path, and adjusted related tests to verify this behavior. (Architecture-related: public API)
  ↳ No PR: [7777db8](https://github.com/openssl/openssl/commit/7777db81f89020e08ded92cde6c2da3139a5e200)

## Routine Changes

### New features
- Added -in option to prime command to support reading numbers from file for prime number detection.
  ↳ No PR: [d18526c](https://github.com/openssl/openssl/commit/d18526cb9422a5c7276776fb5f4c715c218df7d7), [0b7a16f](https://github.com/openssl/openssl/commit/0b7a16fe09ce7d78346587f84146a266a55b63e8)
- Add SHA256-192 digest algorithm support inside FIPS provider and create internal digest table.
  ↳ No PR: [1c2fc7c](https://github.com/openssl/openssl/commit/1c2fc7c3e04cc1334fa7a88454e5614e3b13dd6d)
- ML-DSA export function now supports exporting public keys individually.
  ↳ No PR: [3e82012](https://github.com/openssl/openssl/commit/3e82012b39e4d5999cc33655175f6473f923c26e)
- The x509 tools add the -multi option to support handling multiple certificates, fix the -addreject option misusing trust lists, and re-add the ERR queue printing on errors.
  ↳ No PR: [ac85974](https://github.com/openssl/openssl/commit/ac85974bc34dc18830fa9401a7d4756dbd2d9e35)
- Added one-way and two-way stream type flags to SSL_accept_stream, allowing callers to specify to accept specific types of streams.
  ↳ No PR: [74a0ec3](https://github.com/openssl/openssl/commit/74a0ec3c08e0bfbc22e8d15d982541934fe92776), [20c3988](https://github.com/openssl/openssl/commit/20c3988bcd3f9a71864f031d6e60906398a4e547), [e8d6e04](https://github.com/openssl/openssl/commit/e8d6e0460b91a08a6ce073082c1db1c4c6707914)
- The openssl application adds the ability to initialize secure memory at startup through the environment variables OPENSSL_SEC_MEM and OPENSSL_SEC_MEM_MINSIZE.
  ↳ No PR: [91d34f4](https://github.com/openssl/openssl/commit/91d34f408cd23aa38275a3ce9e8bb31c4cbbcd83)
- The openssl rand command now uses the loaded library context to generate random numbers.
  ↳ No PR: [e7d5398](https://github.com/openssl/openssl/commit/e7d5398aa1349cc575a5b80e0d6eb28e61cb4bfa)
- Add support for the hh length modifier in the _dopr function so that it can correctly handle signed char and unsigned char type parameters.
  ↳ No PR: [6f8beb7](https://github.com/openssl/openssl/commit/6f8beb7ce9be114dcb03d7dd7b1521235ec24958)
- Added pairing compliance testing in FIPS mode for SLH-DSA key import, and added helper functions for getting libctx and resetting keys.
  ↳ No PR: [7903702](https://github.com/openssl/openssl/commit/79037022801d6496bb8e1a8a29c21236084c8588)
- Added support for %t format specifier, used to handle ptrdiff_t type parameters in BIO printing functions.
  ↳ No PR: [779346f](https://github.com/openssl/openssl/commit/779346f2ec5ff86be47f3ebf01ab9eaa20d5e0b6)
- Added key size check before applying keys, and adjusted key initialization order.
  ↳ No PR: [4ea5644](https://github.com/openssl/openssl/commit/4ea5644a67e0767bf2fe6090e15ab931e31452e6)
- Added changelog and news items for the new openssl configutl tool.
  ↳ No PR: [8109618](https://github.com/openssl/openssl/commit/8109618a1ce0103045329ed44f9d7a4ded8654be)
- Added DN output design document in RFC4514 format.
  ↳ No PR: [da9a6c6](https://github.com/openssl/openssl/commit/da9a6c6ebd84d2910c04b0b546d58748c4b34185)
- Added change records about OSSL_PARAM name resolution reconstruction in CHANGES.md.
  ↳ No PR: [730c2d9](https://github.com/openssl/openssl/commit/730c2d9cccad11093bbb15c9fc739e68b7244247)
- Updated the parameter get and set functions in multiple provider implementations, and added checks on decoder return values and context pointers.
  ↳ No PR: [f5c3b94](https://github.com/openssl/openssl/commit/f5c3b94d7368ad7baf13c813a566226b6fec0360)
- Added a new HTTP/1.0 QUIC demo server based on SSL_poll for benchmark testing.
  ↳ No PR: [f426dd1](https://github.com/openssl/openssl/commit/f426dd1311eecd12f24190c94f56eb85e62aaa27)
- Added GENERIC SKEYMGMT algorithm support in legacy provider.
  ↳ No PR: [8c3c2f5](https://github.com/openssl/openssl/commit/8c3c2f5cd8f9ebfda36704e517238a9c7a1c2b4c)
- Added generated parametric decoder for BLAKE2.
  ↳ No PR: [d11c954](https://github.com/openssl/openssl/commit/d11c9541ef93baf6530de6ecd285220effc03a25)
- Added helper functions to copy custom extensions of old-style parameters, and refactored related copy logic.
  ↳ No PR: [f7b1000](https://github.com/openssl/openssl/commit/f7b10004dce1444a9712fc9e578e30576fcca6b6)
- Added a new utility function for reading 4-byte network-order data from packet.
  ↳ No PR: [19126fc](https://github.com/openssl/openssl/commit/19126fcf230dc0b7b2d2785ec5e851c97fb15f93)
- Added a new auxiliary function for the parameter module that does not perform parameter positioning and supports batch operations.
  ↳ No PR: [b5828db](https://github.com/openssl/openssl/commit/b5828dbbf2775fd04f112d95b92e3f78caa8d1a6)
- Move the initialization of the global ADDED_OBJ hash table out of the write lock and instead initialize it in advance through RUN_ONCE.
  ↳ No PR: [cff8031](https://github.com/openssl/openssl/commit/cff803116397c2c69649f8f69a62a0623a97d2c8)
- Unified the memory allocation method in EC functions, using OPENSSL_zalloc and OPENSSL_calloc.
  ↳ No PR: [1f859bb](https://github.com/openssl/openssl/commit/1f859bb5927632c823f08fe5f48239149aa4cdea)
- Removed the assertion in namemap_add_name and correctly handled memory allocation failure errors.
  ↳ No PR: [0a15d71](https://github.com/openssl/openssl/commit/0a15d71f6719c5195af9dbd258a52e0b73ed0acd)
- Simplified decoding logic for RSA padding mode and salt length parameters.
  ↳ No PR: [18f822f](https://github.com/openssl/openssl/commit/18f822f6a6d7c4f2792387cea76142d051fdcad7)
- Updated the keymgmt template to use the automatically generated parameter name decoder and added missing functions.
  ↳ No PR: [3f5561a](https://github.com/openssl/openssl/commit/3f5561a9f4274fa591af52099da8844c1e8cafb5)

### bug fixes
- Fixed the problem of string concatenation compilation failure due to incorrect use of preprocessing concatenation.
  ↳ No PR: [ed3876a](https://github.com/openssl/openssl/commit/ed3876adb1f0beb5fac8d564337ab949f227c563)
- Fixed an issue where Windows line terminators caused incorrect file reading, and now handles both Unix and Windows line breaks correctly.
  ↳ No PR: [f15a2a4](https://github.com/openssl/openssl/commit/f15a2a43ef2df3a6131156e0a88fa44238fb034e)
- Fixed boundary cases when processing short or empty files, added error prompts for empty files, and prevented out-of-bounds access.
  ↳ No PR: [585a1e6](https://github.com/openssl/openssl/commit/585a1e6f8ba5fcf2c17bf800744b2db4be40d0b0)
- During key exchange operations, ensure that a reference to the peer key is also kept in the provider path.
  ↳ No PR: [c8654f7](https://github.com/openssl/openssl/commit/c8654f79f4e40e6ca0e05cc111f515ca11248e29)
- Removed DAYS parameter from certificate request to avoid generating warnings, and fixed errors caused by uninitialized variables.
  ↳ No PR: [d890ad2](https://github.com/openssl/openssl/commit/d890ad2b96efea4f5f4b0db190017ce9a3897df7)
- Added null pointer checks in cms.c and ocsp.c to prevent potential null pointer dereferences.
  ↳ No PR: [952d9b8](https://github.com/openssl/openssl/commit/952d9b83b20359e9ed0fff8f18a84add29949f6f)
- Fixed an issue where legacy code paths were still incorrectly entered when the EVP_PKEY context had keymgmt bound.
  ↳ No PR: [27b8836](https://github.com/openssl/openssl/commit/27b88364e41f01cc1be6ff2941dd07919f286c89)
- Fixed an issue that incorrectly decremented the unreleased counter when freeing a record in a QUIC record layer failed.
  ↳ No PR: [4ad4596](https://github.com/openssl/openssl/commit/4ad45969b028dbf2521fa42ea463978402b3584b)
- Fixed missing default digest length in CMS when using SHAKE as digest algorithm, added specific digest length settings for SHAKE128 and SHAKE256.
  ↳ No PR: [c1d2778](https://github.com/openssl/openssl/commit/c1d27789e99543d366a8e0498cbab2d9543ef2cb)
- Fixed the null pointer dereference problem caused by unhandled V_ASN1_UNDEF type in asn1_ex_i2c(), and added the corresponding branch to avoid crashes.
  ↳ No PR: [8e08f9c](https://github.com/openssl/openssl/commit/8e08f9c5a013d9a9fb9e2db3c90a70eda50f78b5)
- Allow ECDSA to sign using digest without NID, and fix an invalid digest check in DSA signing.
  ↳ No PR: [6708df4](https://github.com/openssl/openssl/commit/6708df48d6e31a598df2fa24bbc907a762d9a371)
- Fixed a memory leak when ktls record layer creation failed, using the correct release function instead.
  ↳ No PR: [e5e4cf4](https://github.com/openssl/openssl/commit/e5e4cf41c7af9b533265efb05e81ce1c56d58601)
- Fixed the problem of incorrect multiplication by 8 when getting the number of safe parameters in ML_DSA.
  ↳ No PR: [3c1f50a](https://github.com/openssl/openssl/commit/3c1f50ad6f3d9dbbce095e83a59e6cd64cabe65e)
- When acquiring the random number method, first check whether the random method lock exists to avoid crashing due to the lock being released during the exit cleanup phase.
  ↳ No PR: [4eb3eea](https://github.com/openssl/openssl/commit/4eb3eea7a38eccfa2790020188d1d59dc68d8755)
- Fixed reporting of certificate chain public key algorithms in the s_client command to support supplied keys and show curve names instead of bit numbers for EC keys.
  ↳ No PR: [aeb7975](https://github.com/openssl/openssl/commit/aeb797594b28f8bd3e2cc1fa8a51ba7f1aea1b1d)
- Fixed the condition judgment error when skipping packets in qlog event recording, and corrected the wrong reverse condition to the correct comparison.
  ↳ No PR: [83b11af](https://github.com/openssl/openssl/commit/83b11af01738196b0ebde28a2f91df351c1c72fc)
- Added a null pointer check to the return value of OPENSSL_strdup() in the load_index function to ensure that it can correctly jump to the error handling path when memory allocation fails.
  ↳ No PR: [930c645](https://github.com/openssl/openssl/commit/930c645e6b74a09398f6345b2d265c38ff035afe)
- Fixed a possible double-release issue when copying hybrid ML-KEM keys, added deep copying of attribute strings and checked key material consistency.
  ↳ No PR: [02cada2](https://github.com/openssl/openssl/commit/02cada2e45a2867e304542f9c5440bfb29af0283)
- Fixed SHAKE algorithm identifier encoding so that it does not carry parameters.
  ↳ No PR: [bef03c6](https://github.com/openssl/openssl/commit/bef03c6a24f02df4e670697b16b6d7c8b1b604b4)
- Fixed length calculation errors and non-zero end of string in the parameter value output function, and added hexadecimal output for octet strings.
  ↳ No PR: [fad8c04](https://github.com/openssl/openssl/commit/fad8c04dedb18379d3dd51db8cce05011e3ff008)
- Fixed a segmentation fault in the pkeyutl command line tool caused by dereferencing a null pointer after failing to load the key, adding a null pointer check and outputting an error message.
  ↳ No PR: [3f0f723](https://github.com/openssl/openssl/commit/3f0f723b521b5138f9ac77ede45a77dc46a734d4)
- Fixed a potential null pointer dereference problem in the final_maxfragmentlen() function, advancing the NULL check of s->session to the beginning of the function.
  ↳ No PR: [28de1f5](https://github.com/openssl/openssl/commit/28de1f5004c1083d358e6934552124a201e0251e)
- Fixed an issue where the Windows Certificate Store Provider was not correctly creating decoder instances using the new API due to recent decoder changes.
  ↳ No PR: [8419baf](https://github.com/openssl/openssl/commit/8419baf31222c5f439b09ceb41f7a6e1916eab3b), [52e8814](https://github.com/openssl/openssl/commit/52e8814de3b35aa280b5323aa743229e0b61ddc8)
- Add missing error message when CMS output writing fails.
  ↳ No PR: [1beaf11](https://github.com/openssl/openssl/commit/1beaf112e53c5b6ea2a7c7564adb1374d7253e7e)
- Fixed a deadlock issue that could result from calling RAND_get0_primary() when only loading the FIPS provider, to avoid recursive locks by narrowing the lock holding range.
  ↳ No PR: [01ea080](https://github.com/openssl/openssl/commit/01ea08049815325bf7719499f58c3799aa3fb555), [273c75e](https://github.com/openssl/openssl/commit/273c75e8636fb28be3d56ef0bd7b67b7451a0bef)
- Fixed the operation type error when initializing ML-DSA signature messages, and improved the deep copy processing of signature data in context replication.
  ↳ No PR: [f9879c8](https://github.com/openssl/openssl/commit/f9879c864e343eb6882e2a6e0aa26f3ee47f794c)
- Add a check when initializing the signature algorithm to ensure that the update and final functions exist or do not exist at the same time to prevent the provider from providing only one of the functions.
  ↳ No PR: [8626a71](https://github.com/openssl/openssl/commit/8626a716b0776e4203dc89f2e81c54d078a7ad07)
- Fixed the FIPS provider compatibility regression and adjusted the check of the error queue in the test so that it is only performed on FIPS provider 3.6.0 and above.
  ↳ No PR: [6f26301](https://github.com/openssl/openssl/commit/6f26301c83bf7796240a484249510d625f968028)
- Fixed the zeroing problem of z and d values when resetting the ML-KEM key, ensuring that the zeroing operation covers the complete memory area.
  ↳ No PR: [5d44f67](https://github.com/openssl/openssl/commit/5d44f67aafb26ea3adcd33cd6d34bc17e40466cb)
- Fix memory leak in pkeyutl caused by EVP_PKEY_CTX_ctrl_str failure, release passwd before jumping.
  ↳ No PR: [0dc6ea5](https://github.com/openssl/openssl/commit/0dc6ea55a13dbe27af234b5328527d0a31ae68eb)
- Add a check for negative values returned by BIO_snprintf in BIO_dump_indent_cb to avoid potential undefined behavior.
  ↳ No PR: [56c7398](https://github.com/openssl/openssl/commit/56c739816f3dacbb024ceae29c546abe677ee02c)
- Fix the memory leak problem of BIGNUM in apps/prime.c.
  ↳ No PR: [573db12](https://github.com/openssl/openssl/commit/573db120795ced4750c8de2a7dccb1346dded6ff)
- Fix memory leak caused by not freeing ssl_bio in sconnect example and add BIO_free call on wrong path.
  ↳ No PR: [55d8d85](https://github.com/openssl/openssl/commit/55d8d859797e8229bc499bbc7c3c76821b654682)
- Fix the debug log printing in the OSSL_CMP_MSG_http_perform function: remove redundant format specifiers, and complete the missing colon in another log.
  ↳ No PR: [0873cd1](https://github.com/openssl/openssl/commit/0873cd1b680d2f54de3dbcc754ea6b1b397f112b)
- Fixed a memory leak in ossl_method_store_add caused by incorrect release of impl internal resources.
  ↳ No PR: [00c531a](https://github.com/openssl/openssl/commit/00c531a5e327320f0ec78ce4b153fac65ebca229)
- Add NULL check for ba_ret pointer in init_client() function to avoid potential null pointer dereference and simplify address saving logic.
  ↳ No PR: [3161f46](https://github.com/openssl/openssl/commit/3161f460fa7eacc7a93f8edf413c78b4dcf65823)
- Fixed possible leak of duplicate EVP_PKEY_CTX under wrong path, and improved error reporting in signing and verification operations.
  ↳ No PR: [52a2b3d](https://github.com/openssl/openssl/commit/52a2b3d82f37c87b5b2cff68abbc93861978a853)
- Fixed a possible double release of the EVP_MD variable after yield_secret_cb failed when using an external QUIC implementation.
  ↳ No PR: [258d3a6](https://github.com/openssl/openssl/commit/258d3a695e32828df7dbda6ee9ae67d31e128f62)
- Fixed the key switching sequence in the QUIC handshake to ensure that the writing key is set before the reading key to avoid being unable to confirm after reading the data.
  ↳ No PR: [86e7579](https://github.com/openssl/openssl/commit/86e75792622b39a9cf49c0915e58cca5c9d316d3), [098cfd2](https://github.com/openssl/openssl/commit/098cfd216b9b54106cbf9338a511c7dda972b8c1)
- Fixed issue with DTLS message callback displaying errors in messages that span multiple fragments (such as certificates).
  ↳ No PR: [de5a619](https://github.com/openssl/openssl/commit/de5a619aa015e7c8648e415975e5e2b722b2cbf7)
- Added verification of extra tail bytes in the TLS compression certificate extension processing function, and returns a decoding error alarm if there is unparsed data.
  ↳ No PR: [8e787b1](https://github.com/openssl/openssl/commit/8e787b102848e462a6d231883e2c42d91978c049)
- Added a check for null private key in the sm2_sig_gen function to prevent crashes caused by null pointer dereference due to unset private key.
  ↳ No PR: [c108ead](https://github.com/openssl/openssl/commit/c108ead2840a76a59fe02c049d08322a02b24761)
- Fixed the null pointer dereference and return value issues in the ecx_gen_init function, and enhanced keymgmt initialization robustness.
  ↳ No PR: [02f9c93](https://github.com/openssl/openssl/commit/02f9c9342d54c99981b0a83088982bf0d1083d7f), [443298e](https://github.com/openssl/openssl/commit/443298e0f0e2c8225f8c6d6fdc01c6c4d434028b)
- Fixed the problem of writing freed memory in the ossl_rio_poll_builder_add_fd function due to the local pointer not being updated after reallocation.
  ↳ No PR: [5ee8248](https://github.com/openssl/openssl/commit/5ee8248d083c00583d52350ed9464bfb58d2f60c)
- Unified so that all *_gen_cleanup functions can safely handle NULL context parameters to avoid crashes when NULL is passed in.
  ↳ No PR: [fcc5df5](https://github.com/openssl/openssl/commit/fcc5df53697a63d0f153b0086054f509aad8e6bb)
- Fixed issue with passing user SSL object instead of internal SSL object in SSL verification callback.
  ↳ No PR: [4b148eb](https://github.com/openssl/openssl/commit/4b148ebb66cdac8a095f22cbdfa475d68c947f7a)
- Added error handling when the master key thread local storage setting fails. When it fails, the memory is released and an error is returned.
  ↳ No PR: [4ed9a38](https://github.com/openssl/openssl/commit/4ed9a38a906fff536193d1bf686bec15501df6e9)
- Fixed a potential issue caused by missing null pointer checking when master key cleanup in FIPS mode.
  ↳ No PR: [32559a6](https://github.com/openssl/openssl/commit/32559a6035b7ec2155c0fe4e2199834c639a981b)
- Updated the CCM implementation to use improved parameter handling and fixed an issue where more parameters were claimed to be supported than actually supported.
  ↳ No PR: [e40d575](https://github.com/openssl/openssl/commit/e40d5752061a2640b2e27e6ff1b8f3b69586d731)
- Reduce the number of buckets in the name map hash table from 2048 to 512 to avoid memory allocation failure issues.
  ↳ No PR: [b3161bd](https://github.com/openssl/openssl/commit/b3161bd9a9329be3d6bf6b29a06835e2721898bb)
- Fixed the issue where the exit code of openssl s_time incorrectly returns 1 when using the -new switch. Now it returns 0 correctly.
  ↳ No PR: [b6ff559](https://github.com/openssl/openssl/commit/b6ff5598539bf91608246ed81b4b534cbea6539d)
- Fixed the use-after-release issue in LMS verification initialization to avoid incorrectly clearing existing keys when the key is empty.
  ↳ No PR: [43f4da9](https://github.com/openssl/openssl/commit/43f4da917ac15fb9685e969634534f3cd1eb9901)
- In the FIPS module, DH key import adds pairing check and changes the error status type of import failure from regular PCT to import-specific type.
  ↳ No PR: [e08b83c](https://github.com/openssl/openssl/commit/e08b83cbb3b853ae9dc364c32d927405172918ac), [c2ebeee](https://github.com/openssl/openssl/commit/c2ebeeeff67948cd4f44fc5e4a777cf9ea293f17), [1afc4e8](https://github.com/openssl/openssl/commit/1afc4e8baa3226ea6edb643180246201968d8958)
- Fix memory allocation and type issues in QUIC polling server example.
  ↳ No PR: [b692380](https://github.com/openssl/openssl/commit/b692380651d4a6e378aeb9acfe6ffaef94fdced9)
- Fix the alignment of OPENSSL_*alloc macro definitions to make them comply with the requirements of code format checking tools.
  ↳ No PR: [af6a8fd](https://github.com/openssl/openssl/commit/af6a8fdf750b3db7c93075fdd3a6c0c86dc5b625)
- Fix handling of empty IDNs to be consistent with incorrect IDN behavior and add test cases.
  ↳ No PR: [44ef69c](https://github.com/openssl/openssl/commit/44ef69cffbeb2de830916fd493567170cc566950)
- Fix CRYPTO_aligned_alloc failing to properly dereference pointer parameters under OPENSSL_SMALL_FOOTPRINT conditions.
  ↳ No PR: [35a3958](https://github.com/openssl/openssl/commit/35a3958dc6cdc404dd8af7f73ae755ea488e7a4c)
- Fixed a potential null pointer dereference problem in EVP_DigestSignUpdate due to unchecked pctx->pmeth being null, and added a null value check in the legacy path and returned an initialization error.
  ↳ No PR: [daa004d](https://github.com/openssl/openssl/commit/daa004d48438d67241b58592d43c3214dd3a903f)
- Fixed the printing problem of the uppercase prefix 0X in the X conversion specifier, and now correctly outputs 0X or 0x according to the format flag.
  ↳ No PR: [96e021d](https://github.com/openssl/openssl/commit/96e021dffff9a5382e3b9d68f55a0e538ae0dea1)
- Fixed a logic error in the null pointer check in the bring_oscp_resp_in_correct_order function. Now the content pointed to by the pointer is correctly checked instead of the pointer itself.
  ↳ No PR: [8ceae5a](https://github.com/openssl/openssl/commit/8ceae5a6226c6c909c7ce0b4582d0d698e5d1357)
- Fixed the dangling pointer problem caused by not setting the pointer to null after the OCSP response is released, to avoid subsequent use of the released memory.
  ↳ No PR: [bd1a14b](https://github.com/openssl/openssl/commit/bd1a14bcaf77426fa17c2acaff48fb9a612ce680)
- Fixed incorrect null pointer check in get_ocsp_resp_from_responder function, now correctly checks the allocation result pointed to by the pointer.
  ↳ No PR: [3c4f009](https://github.com/openssl/openssl/commit/3c4f009959c4b73b78219da51e49bb564a24ef48)
- Removed incorrect conditional compilation macros in fuzz/dtlsserver.c and fixed the problem of missing variable declarations under certain compilation configurations.
  ↳ No PR: [fd7fc90](https://github.com/openssl/openssl/commit/fd7fc90346306f49773866eddff90717e22b9181)
- Fixed an issue where the QUIC channel may fail when processing the second transmission parameter expansion in the HelloRetryRequest scenario. The server resets the local transmission parameters after receiving the HRR to avoid duplicate parameter errors.
  ↳ No PR: [4b6e655](https://github.com/openssl/openssl/commit/4b6e6554b290842314e2fe4d5e56f5290bb4b8df), [605eda6](https://github.com/openssl/openssl/commit/605eda60ae1c221e38710a3a83df2c4e24d0cc04)
- Fixed the issue where the largest_pn value of the temporary qrx in the QUIC connection was not migrated to the qrx of the new channel, causing decryption of subsequent frames to fail. Added migration logic for the largest_pn array in the port default packet processor.
  ↳ No PR: [0c1c243](https://github.com/openssl/openssl/commit/0c1c243a80eb2641058f9edc0f1a6c947d8d9205)
- Fixed byte order handling errors of supported versions in the QUIC version negotiation package, including byte order issues when sending and parsing.
  ↳ No PR: [2b24455](https://github.com/openssl/openssl/commit/2b24455a9fb253b6d26e81e83d6adc2a615ff4b9), [95efe41](https://github.com/openssl/openssl/commit/95efe41d2e76501f4900eb6a5dece159fb1312df)
- Fix possible extra zero padding in %#o format to make it POSIX compliant.
  ↳ No PR: [0f107c7](https://github.com/openssl/openssl/commit/0f107c709c7392e9cc472e9b82448880d9b3afb1)
- Fix issue with space padding calculation in bio_print.c so that sign, prefix and zero padding are correctly accounted for precision.
  ↳ No PR: [badbcc6](https://github.com/openssl/openssl/commit/badbcc663192d9599f8435c1392fae09924de0c7)
- Fix the processing logic of '-' flag taking precedence over '0' flag in formatted output to make it comply with POSIX standard.
  ↳ No PR: [95af148](https://github.com/openssl/openssl/commit/95af148e14862bb982530f090e5e04e5b977bac1)
- Fixed code issues with UKM settings and key cleanup in CMS KEM receiver information.
  ↳ No PR: [252046c](https://github.com/openssl/openssl/commit/252046cfc2c8e4c7ea40b78170d644d2787b44ff)
- Fixed the issue of unchecked thread-local storage allocation failure in rand_lib. Now the allocated random number generator is released and NULL is returned when the setting fails, thus handling the failure gracefully.
  ↳ No PR: [7f780be](https://github.com/openssl/openssl/commit/7f780be21608a2982cdf1c567e5afeb724b1e9a1)
- Fix an issue where RCU read locks trigger assertions when memory allocation fails, change the ossl_rcu_read_lock return value to int to indicate success or failure, and update all callers to handle lock failures gracefully.
  ↳ No PR: [036a46d](https://github.com/openssl/openssl/commit/036a46d2a4b00a004d05dc6a6d19be7184f8ecf1)
- Fixed the race condition caused by sharing OSSL_STORE_CTX in multi-threaded scenarios. The store is no longer kept open in by_store_ctrl_ex, but is reopened every time cache_objects is called.
  ↳ No PR: [08951fb](https://github.com/openssl/openssl/commit/08951fb27306ad9b4365103b8616b8545658ffcc)
- Fixed the wrong operation identifier being used in SKEYMGMT enumeration and added related tests.
  ↳ No PR: [f446bf7](https://github.com/openssl/openssl/commit/f446bf79515f55f55930c5340eb3eb981327f2ac)
- Add null pointer check for SSL_CONNECTION in quic_channel.c to prevent potential null pointer dereference.
  ↳ No PR: [c5ef06f](https://github.com/openssl/openssl/commit/c5ef06f4abcda15056f9316b3fb4697a0b289d9b)
- In the CMS KEM encryption function, when EVP_CIPHER_param_to_asn1 fails, release the allocated ASN1_TYPE parameter to prevent memory leaks.
  ↳ No PR: [fb295aa](https://github.com/openssl/openssl/commit/fb295aa65c1e78f2ef50e3a911f00bd9735cd702)
- Add a null pointer check in the HASH extended display function to prevent crashes caused by empty hashValue.
  ↳ No PR: [24f72a5](https://github.com/openssl/openssl/commit/24f72a5aaab0243c136e1402b54348fda9cdbc36)
- Fixed the issue in tls1_set_server_sigalgs that SSLfatal was not set when memory allocation failed, to avoid subsequent state machine checks triggering assertion failures.
  ↳ No PR: [3897288](https://github.com/openssl/openssl/commit/389728876b51de0df9f97b6a295948ebec1e0f0c)
- Fixed the bug in the null pointer check in the dtls1_shutdown function, and changed the check object from the original SSL object to the converted SSL_CONNECTION object.
  ↳ No PR: [bc28ca4](https://github.com/openssl/openssl/commit/bc28ca499ef37e5ab6e2676727a3db7f02c837ae)
- Fix null pointer check in pkey_dh_derive to ensure both keys are set when deriving DH keys.
  ↳ No PR: [fc84d46](https://github.com/openssl/openssl/commit/fc84d46d7227886152be00618889a521e9132ef3)
- Fix an issue where the precision value could be negative when providing an empty precision string, resetting it to zero to comply with POSIX specifications.
  ↳ No PR: [cbb0a56](https://github.com/openssl/openssl/commit/cbb0a561e64b25001039f0ac82170536b2ef4893)
- Fix the behavior of the %n format specifier so that it records the virtual write position rather than the actual number of bytes written, and restore length modifier support.
  ↳ No PR: [228ef5f](https://github.com/openssl/openssl/commit/228ef5f5472790e64c14596ef6d3d698875ffd61), [2b16781](https://github.com/openssl/openssl/commit/2b16781c5b84e13e1429d58e10c65a51bc6fc224)
- Fixed the precision processing logic in the fmtint function: negative precision is treated as omitted and the default precision is 1, and the '0' flag is ignored when specifying precision.
  ↳ No PR: [ac49202](https://github.com/openssl/openssl/commit/ac492027221eefcd2f015a20d3a1fd2680882a9a)
- Fixed an issue where when printing integers, the output is a null character when the value is zero and the explicit precision is zero.
  ↳ No PR: [c5e3e7b](https://github.com/openssl/openssl/commit/c5e3e7bfb678a847e509f73432da82745e03fd31)
- Fix memory leaks in several BIO examples, add release of ssl_bio at the end of the function.
  ↳ No PR: [f9afb3a](https://github.com/openssl/openssl/commit/f9afb3a07eb72428b98e3e31384380564a236700)
- Fixed a memory leak caused by not releasing the PKCS7 object in the PKCS12 password change function.
  ↳ No PR: [8563f27](https://github.com/openssl/openssl/commit/8563f27d49c87db1a60db983dde8057c9d3748e1)
- Fixed the OCSP_SINGLERESP double release problem to avoid repeatedly releasing the referenced single response when releasing OCSP_BASICRESP.
  ↳ No PR: [eaacf56](https://github.com/openssl/openssl/commit/eaacf56ba97e8089344bc85f8a50b00932cd3416)
- Fix the judgment of reallocation failure condition in qtx_resize_txe() to avoid misjudgment of returning the same pointer as failure, and ensure that NULL is correctly returned in case of failure.
  ↳ No PR: [220f5be](https://github.com/openssl/openssl/commit/220f5be6908631759d56c7a6458be8385d984260)
- In FIPS providers, transition to transient error state when ML-DSA key import fails.
  ↳ No PR: [56a7912](https://github.com/openssl/openssl/commit/56a791209c1e63222b1680151709fabd86948548)
- In FIPS modules, set the correct transient error state when ML-KEM key import fails; also changed the ml_kem_load function in non-FIPS modules to be static.
  ↳ No PR: [eaba675](https://github.com/openssl/openssl/commit/eaba675c4b300e18aa4a200a75ff9566653afda8), [162089a](https://github.com/openssl/openssl/commit/162089af7c6894cf65b70be1fc7e7091be482a71)
- Fix the reference counting problem when EVP_SKEY is allocated, ensuring that the reference count of the key management object is correctly incremented when allocated and released correctly when it fails.
  ↳ No PR: [0de951b](https://github.com/openssl/openssl/commit/0de951ba9a590d2cd856481bf56cd12b485c7b07)
- Fixed the issue of entering a FIPS error state if the pairwise test fails when importing the SLH-DSA key.
  ↳ No PR: [b22df65](https://github.com/openssl/openssl/commit/b22df6529a5667fe7f8d636ece92a4896b86f66c)
- Fix DER encoding length of SM3 digest information to make RSA-SM3 signatures compliant.
  ↳ No PR: [9403c7d](https://github.com/openssl/openssl/commit/9403c7d768f516988a6d4c4deffce190197961a6)
- Fix the missing unlock operation on specific error paths in the ossl_provider_new function to avoid potential deadlocks or resource leaks.
  ↳ No PR: [55209aa](https://github.com/openssl/openssl/commit/55209aab56da20f59f6c1b473f647990b1aa671d)
- Updated SSL tracing functionality to correctly display all MLKEM-based group names (MLKEM512, MLKEM768, MLKEM1024 and SecP384r1MLKEM1024) and added corresponding test cases.
  ↳ No PR: [bb04366](https://github.com/openssl/openssl/commit/bb04366d366701734e690ad07d11a91e54123f9f)
- Fixed the problem of too many loops caused by the user providing too large width or precision specifications, and added a new eob_ok function to terminate loops early in non-expandable buffers.
  ↳ No PR: [98e1729](https://github.com/openssl/openssl/commit/98e17292227661c8f261d83116b2953d639dcf1e)
- Fix the memory order issue between update_qp and get_hold_current_qp, add release/acquire barrier to ensure the visibility of reader_idx.
  ↳ No PR: [d19a67d](https://github.com/openssl/openssl/commit/d19a67d67fd359317b07a56ba98f11a5b0513337)
- Removed Pairing Consistency Test (PCT) when importing ECX keys, consistent with other algorithms.
  ↳ No PR: [588bc2e](https://github.com/openssl/openssl/commit/588bc2ebb39117b364c003d094e2490b879d8474)
- Fix ML-KEM key equality check to ensure correct comparison when one of the keys is not set.
  ↳ No PR: [3cf5e10](https://github.com/openssl/openssl/commit/3cf5e10317c266449885ff830a45681ecec6f410)
- Fix the race condition of the ossl_quic_conn_stream_conclude function in QUIC and move the error promotion operation to before unlocking.
  ↳ No PR: [34063df](https://github.com/openssl/openssl/commit/34063dff6016cab201bbc12ca34e33d64f678dbb)
- Fixed the double release problem of ossl_siv128_init() in the failed path, and then empty the relevant context after releasing it.
  ↳ No PR: [9f773c2](https://github.com/openssl/openssl/commit/9f773c24ff6ed1f589c7c16caa9b6ff206c084f5)
- Updated changelog to note that SSLv3 is disabled by default when building.
  ↳ No PR: [6509f18](https://github.com/openssl/openssl/commit/6509f18c9fdbf76a63e8c6056da989cd047a7fb2)
- Fix an issue in the sslecho example where client sockets could be closed repeatedly.
  ↳ No PR: [48e3fe0](https://github.com/openssl/openssl/commit/48e3fe08639d84bd557c0d5248f5600f2fb1f7de)
- Fixed build failure due to macro conflict on AIX platform.
  ↳ No PR: [e11fdd8](https://github.com/openssl/openssl/commit/e11fdd8293c5e13e09c817b89b9c3d4c1a46d857), [235092d](https://github.com/openssl/openssl/commit/235092d780857baf64cefae7eeb8e06e56e19147)
- Upgrade docker-compose and specify the network interface name to fix connection problems in CI caused by network uncertainty.
  ↳ No PR: [d7be888](https://github.com/openssl/openssl/commit/d7be888244faf1b42855406731a3880c76bca636)
- Fixed typo in command to test external rpki client in CI configuration.
  ↳ No PR: [abe1014](https://github.com/openssl/openssl/commit/abe1014d0de696f1a3f108f496d887585d39b68d)
- Fixed an issue in qlog logging where the skip length was not set correctly when frame header parsing failed.
  ↳ No PR: [9f85a03](https://github.com/openssl/openssl/commit/9f85a036e331d2837db604fc505062f7790a8b2b)
- Add I/O error checking in the multi_split function to ensure correct return when writing fails.
  ↳ No PR: [1a8cc7f](https://github.com/openssl/openssl/commit/1a8cc7fab0fe8d7f7d4d03a39a23fbb994924443)
- Fix tracing output of provider algorithm name, using correct index variable.
  ↳ No PR: [1094db3](https://github.com/openssl/openssl/commit/1094db3c4e57c4d537837912db3736299b50edef)
- Fixed a memory leak in the provider_conf_load function caused by unassigned return value.
  ↳ No PR: [9884f1d](https://github.com/openssl/openssl/commit/9884f1dc11675a5c4613339cfb92903c6ba6103f)
- Fixed a memory leak caused by push failure in the tls1_get0_implemented_groups function.
  ↳ No PR: [0ba71c0](https://github.com/openssl/openssl/commit/0ba71c0a24b185780a96b2c257653f4dcd3446c8)
- Fix the memory management problem in port_make_channel, and optimize the processing logic of port_new_handshake_layer.
  ↳ No PR: [d56f9b4](https://github.com/openssl/openssl/commit/d56f9b4d894d1a3ce92f1c308ef42398495943e7)
- Updated DSA, ECDSA and RSA signature algorithm macros to prevent macro parameters from being mistakenly treated as arithmetic expressions.
  ↳ No PR: [a6d5af4](https://github.com/openssl/openssl/commit/a6d5af4fb52b09b8bf701b9b508e724557791a67)
- Fixed the character encoding problem of subject, issuer and other DNs in CMP applications, and changed the parsing encoding from ASCII to UTF-8.
  ↳ No PR: [35e431e](https://github.com/openssl/openssl/commit/35e431ed6daa894ee5385363cf4cfe4954312e4d)
- Added check for empty ECDHE encoding keys in the tls_process_cke_ecdhe function to prevent decoding errors.
  ↳ No PR: [831cbbb](https://github.com/openssl/openssl/commit/831cbbb5dd4a569b12f3f1ae9a6688ccee8edd24)
- Added a null pointer check in the ossl_quic_get_peer_token function and returns failure when the peer address is not set.
  ↳ No PR: [99ea6b3](https://github.com/openssl/openssl/commit/99ea6b38430dc977ba63c832694cdb3c2cb3c2c9)
- Fixed a resource leak issue that could occur when configuration file options are passed multiple times.
  ↳ No PR: [7cc69ec](https://github.com/openssl/openssl/commit/7cc69ec4cf575232040ac776f405fb31f030e59a)
- Fixed the BIO_new_file return value check error in demos/cms/cms_ddec.c and use the correct variables to determine whether the file is opened successfully.
  ↳ No PR: [8a75456](https://github.com/openssl/openssl/commit/8a7545607e872ccaff3018e2cd201cce65e615ec)
- Unified the parameter processing of ML-KEM and EdDSA into a structure-based TRIE decoder, and fixed related parameter list issues.
  ↳ No PR: [cf13e66](https://github.com/openssl/openssl/commit/cf13e66522126f54e6673b8d546eec2207dfbcd3), [2e1b046](https://github.com/openssl/openssl/commit/2e1b046d9af20f9d1b981e5aa4a8b498155f5c0e)
- In FIPS providers, uniformly convert error states when RSA, EC and ECX key operations fail to transient error states.
  ↳ No PR: [864a5f6](https://github.com/openssl/openssl/commit/864a5f6641cd89bc38b28e821701b21957c96341), [d6f398c](https://github.com/openssl/openssl/commit/d6f398cc957b704d6af43c9c1f55a5f432226fd0), [811f68f](https://github.com/openssl/openssl/commit/811f68ffe2cb97ab997c11b0429236135eb437c0)
- Fixed potential crashes in several functions due to missing return value checks or null pointer dereferences.
  ↳ No PR: [2fccd17](https://github.com/openssl/openssl/commit/2fccd17e8feb91ef9b0cb949eb3fc04a384148ca), [36614fa](https://github.com/openssl/openssl/commit/36614faa98c5a947a635d3f44e78c7c36b722534), [f13abf3](https://github.com/openssl/openssl/commit/f13abf37fd889977d77959c2e4da6f1de7f1d30f), [63cb8f9](https://github.com/openssl/openssl/commit/63cb8f99a13fdc4c7c3b1e88d66a3ff70b72e642)
- Fixed DH private key length calculation error to ensure that the private key value does not exceed the group size when the q parameter is not specified.
  ↳ No PR: [d6510d9](https://github.com/openssl/openssl/commit/d6510d99ae4a8a23f54fdfb1473af6a920da8345)
- Improved the search logic of openssl executable files, checking file existence and executability at the same time.
  ↳ No PR: [fa0c67a](https://github.com/openssl/openssl/commit/fa0c67a28a5a7d6ebeae7cb14d036780485e2fcd)
- Fixed lock contention logging, conditionalized log file names based on FIPS_MODULE and restructured write lock detection logic.
  ↳ No PR: [1178184](https://github.com/openssl/openssl/commit/1178184e96b4748f552a7904682ae1b7804e3edc)
- Fixed QUIC receiver incorrectly sending ACK when unable to process a packet, ensuring only successfully processed packets are acknowledged.
  ↳ No PR: [e6c2058](https://github.com/openssl/openssl/commit/e6c20588efa755c246f52d56891a889b201a015a)
- Fixed RSA key size validation logic in EVP_PKEY_RSA_keygen example to ensure command line parameter values are used.
  ↳ No PR: [c79e1b2](https://github.com/openssl/openssl/commit/c79e1b212a616b8dca194a77e7698b886000fcb0)
- Unified the RSA_public_decrypt() return value checking method to ensure compliance with document conventions.
  ↳ No PR: [3e2f54a](https://github.com/openssl/openssl/commit/3e2f54a718f541b02b599bbf5109587189368e4d)
- Fixed a boundary case in the put_str() helper function in the internal attribute list to string function.
  ↳ No PR: [f4779b8](https://github.com/openssl/openssl/commit/f4779b86af6f3f330511e1d73a61f47104b6266a)
- Fixed a memory leak caused by incorrectly setting the object type in the x509_store_add function on the wrong path.
  ↳ No PR: [874f768](https://github.com/openssl/openssl/commit/874f7684beba74465f9454b1200f729f1d05db58)
- Fixed the use-after-free vulnerability caused by public_keys and private_keys not being cleared after release in evp_test.
  ↳ No PR: [81e8b5a](https://github.com/openssl/openssl/commit/81e8b5a5038b4952a22b2dc9fcf9994615ee8dc4)
- Improved error handling in cms.c: added missing error prompts, added I/O failure handling, and removed unnecessary error printing.
  ↳ No PR: [cc7084a](https://github.com/openssl/openssl/commit/cc7084a5ee2deaeb8882d4c60cf6e9f1caded632), [8877759](https://github.com/openssl/openssl/commit/88777599a6fa65cc812f60169784512798ca6395), [98b6df7](https://github.com/openssl/openssl/commit/98b6df79fb10202d1e2dc8ea093a56c833a76621)
- Cleaned up dead code, unused variables and unnecessary NULL checks in apps/prime.c, fixed issues reported by Coverity.
  ↳ No PR: [3847b49](https://github.com/openssl/openssl/commit/3847b4920a61f519be57b8594ac828456a845fbf), [6a6a098](https://github.com/openssl/openssl/commit/6a6a098bf1de21094e258906c51c67569db7c5a4), [0d3f087](https://github.com/openssl/openssl/commit/0d3f0876ac1addda7ce044063e08ac68b39ad8b9)
- Fixed multiple compilation warnings: declare base_id_conversion array as static, fix type conversion in ERR_raise_data().
  ↳ No PR: [c315f98](https://github.com/openssl/openssl/commit/c315f98f715fc6eb2170bb9e08bd3e138cc02f1a), [d6514ce](https://github.com/openssl/openssl/commit/d6514ce319a7284f8447a462aa3adfcb69c067f4)
- Fixed multiple issues reported by Coverity scans: added return value checks, removed dead code and unnecessary null pointer checks.
  ↳ No PR: [c45ab5b](https://github.com/openssl/openssl/commit/c45ab5b8de0c662917ec26e81bc1c87fa8095a4f), [677ded7](https://github.com/openssl/openssl/commit/677ded7547351bc3b1b6f72745e84b1287402ffb), [1e27fb5](https://github.com/openssl/openssl/commit/1e27fb5d5b1258605315aeea2236649432b7a522)
- Improved the error message when the certificate is not yet valid, and added a description that the system clock may be incorrect.
  ↳ No PR: [0efc439](https://github.com/openssl/openssl/commit/0efc439a3be54a6eb73015e997aa6a6f375b77ef)
- Fixed duplicate definition of cipher suite 0xC102 in ssl/t1_trce.c, keeping the first definition as the canonical version.
  ↳ No PR: [de67f90](https://github.com/openssl/openssl/commit/de67f90815f1dc1ec9f4a9670ae854b71933f7cc)
- Add more specific diagnostic error information when the provider lacks required functions during signature algorithm initialization and verification.
  ↳ No PR: [4a9a59c](https://github.com/openssl/openssl/commit/4a9a59cb075ee2fe0f76040f92f451e954ec8f64)
- Fixed the file name copy-paste error when outputting error messages in the genpkey command, and corrected the file name in the error prompt from outpubkeyfile to outfile.
  ↳ No PR: [a4c5096](https://github.com/openssl/openssl/commit/a4c5096d16a78d2c24f2880fba1ec7056eb3a96f)
- Fixed RCU related to-do items: changed the count parameter type of allocate_new_qp_group to unsigned integer, and optimized the order of fields in the rcu_lock_st structure to improve stack alignment.
  ↳ No PR: [7097d2e](https://github.com/openssl/openssl/commit/7097d2e00ea9f0119a5e42f13a51487fb1e67aa3)
- Removed the processing logic of the HARNESS_OSSL_PREFIX environment variable, which is no longer used by the test framework.
  ↳ No PR: [082a814](https://github.com/openssl/openssl/commit/082a81404cd8e4dfbc7a4cbda23b882a6f7488cb)
- Cleaned up and expanded the use of ERR_print_errors() in s_client: remove redundant calls in multiple error paths, and print accumulated error information uniformly before exiting.
  ↳ No PR: [1c1c9dc](https://github.com/openssl/openssl/commit/1c1c9dc11b574c7e034c553aef2c9472ecafca80)
- Add check for BIO_new_file() return value in CMS encryption example to fix potential null pointer dereference issue.
  ↳ No PR: [881ff0c](https://github.com/openssl/openssl/commit/881ff0c225356a0f28bd55cea5a4c5204b7b7b8a)
- Removed unexpectedly leftover debug output statements in ec.c.
  ↳ No PR: [2d97878](https://github.com/openssl/openssl/commit/2d978786f3e97a2701d5f62c26a4baab4a224e69)

### Refactoring optimization
- Reconstruct the boundary check logic of PBKDF2, unify the checks in FIPS and non-FIPS modes, and fix the type conversion problem.
  ↳ No PR: [cba510a](https://github.com/openssl/openssl/commit/cba510ab862cc179dd2499731c435d2012a89e50)
- Added lock contention reporting function, refactored and added stack output, and improved debugging capabilities.
  ↳ No PR: [e3d98f5](https://github.com/openssl/openssl/commit/e3d98f5bd4f64a18540d85a4ef3af9fc6d78c12b), [10ce7f4](https://github.com/openssl/openssl/commit/10ce7f45cd367674e41bbced3aedf523139bc4db), [c47c16e](https://github.com/openssl/openssl/commit/c47c16ee400f3b4e6900274760e968c145d2f0f0)
- The set_ctx_params and get_ctx_params interfaces of the DRBG module are switched to automatically generated parameter decoders to simplify the parameter processing process.
  ↳ No PR: [a6b9070](https://github.com/openssl/openssl/commit/a6b9070822d0e90b962761b30597afa30c29e1ec), [2044bc7](https://github.com/openssl/openssl/commit/2044bc76793670e894c5ec895a73d0a6a3aaef96)
- Change the ossl_slh_dsa_key_fromdata function parameters from a single OSSL_PARAM array to pass in the public key and private key parameters separately, and use ossl_slh_dsa_key_reset instead of manual cleaning.
  ↳ No PR: [4728227](https://github.com/openssl/openssl/commit/4728227992948a9aba8f9729f6ee208d3b269539)
- Changed the LMS public key parameter decoding to use the generated parameter decoding method.
  ↳ No PR: [326c36c](https://github.com/openssl/openssl/commit/326c36c418e83a959ee3d40193d5681435175959)
- Change the fromdata function of the ECX key to receive separate public and private key parameters, and the caller is responsible for parameter lookup.
  ↳ No PR: [accc7ce](https://github.com/openssl/openssl/commit/accc7ce60eab53b1597375cd1f811e7f4dfa65ee)
- The HMAC implementation no longer uses secure memory to store keys, instead uses normal memory allocation, and adds a null length check.
  ↳ No PR: [edbee2a](https://github.com/openssl/openssl/commit/edbee2a663454b7bd1f56222fee78bde94954694)
- Move system calls out of the write lock area to reduce lock holding time.
  ↳ No PR: [c4c1f6c](https://github.com/openssl/openssl/commit/c4c1f6c7e6b34de806f09a6207243d90a0c7a912)
- Moved internal functions and cleaned up duplicate macro definitions.
  ↳ No PR: [6d3202e](https://github.com/openssl/openssl/commit/6d3202e20f73f8d368004a90d743a613b51f0d62)
- Add comments and explicitly set return values to improve code clarity.
  ↳ No PR: [c3da4b5](https://github.com/openssl/openssl/commit/c3da4b584e0ee07c51914c11f2413e6f25df64a0)
- Clean up constant and function declarations that are no longer used.
  ↳ No PR: [0b968a3](https://github.com/openssl/openssl/commit/0b968a3572d2932e7e756fc9977dbf808510a958)
- Mark engine parameters in multiple KDF implementations as hidden.
  ↳ No PR: [f852b87](https://github.com/openssl/openssl/commit/f852b874653f359b7a5276f447d3f319d1440a6e)
- Changed the parameter parsing of multiple provider modules to use automatically generated code, and made related file renames and header file path adjustments.
  ↳ No PR: [14cb7e6](https://github.com/openssl/openssl/commit/14cb7e65717f9cd0b8b2589e0e3f387d9c444bc7), [2c21475](https://github.com/openssl/openssl/commit/2c214751fe7b84640224415fa46c3d920ffc4a73), [2849a80](https://github.com/openssl/openssl/commit/2849a80e3313b1f70cb92af7124a730cc5d1a88f), [33651be](https://github.com/openssl/openssl/commit/33651beaf7c0f22d6b9086a9beadf44ab3dc9457), [3f38832](https://github.com/openssl/openssl/commit/3f38832475e3363f099d6775ad580528867c6468), [0ff53ef](https://github.com/openssl/openssl/commit/0ff53efc990cf820b4708a1b3c87c087f5bb1a19), [ffe2368](https://github.com/openssl/openssl/commit/ffe236850c31ea882d70e3969002aff53c85b4e3), [fb96193](https://github.com/openssl/openssl/commit/fb96193b4b57ecdcfb1ae11778455b4ff58dbdcd), [1fd364b](https://github.com/openssl/openssl/commit/1fd364bd2924f7f89149487207b1a9f022b36da1), [6218a0a](https://github.com/openssl/openssl/commit/6218a0a82292cf1b4e84d7c3f409dc94004067b9), [0247b0a](https://github.com/openssl/openssl/commit/0247b0ada1c7c849b4172c515c1c8861997f8fee), [dc044f6](https://github.com/openssl/openssl/commit/dc044f616ee42e31fd45714566155d8405f962b1), [324fc17](https://github.com/openssl/openssl/commit/324fc17017ead12ae251c49dc25901ac9aa7d8e8), [360388e](https://github.com/openssl/openssl/commit/360388e55d9d8ce31f06137eec9815fcaedd3b28), [3b69c40](https://github.com/openssl/openssl/commit/3b69c40a276b2560d18285e13ba0f6d7bac1b864)
- Changed the parameter analysis of multiple encoding and decoding modules to automatic generation to simplify code maintenance.
  ↳ No PR: [6696830](https://github.com/openssl/openssl/commit/66968306093a1e45162976e9bd2129db9a91e4ba), [70e33ae](https://github.com/openssl/openssl/commit/70e33aef6eadf3b8d2cabd637a0bcf934ab6afb7), [f4de265](https://github.com/openssl/openssl/commit/f4de265c0f197726d8279b9930d02c1e21fa7537), [f9a5796](https://github.com/openssl/openssl/commit/f9a5796357688ae75730933e9ad590c1a8fbae82)
- Added null pointer checks to multiple KDF and key management implementations to improve robustness.
  ↳ No PR: [b508df7](https://github.com/openssl/openssl/commit/b508df7875b4947fbdf8326713fb891e74cff3eb)
- Removed three unused functions in ecp_sm2p256.c and cleaned up the code.
  ↳ No PR: [ed5ba48](https://github.com/openssl/openssl/commit/ed5ba489102ad4193e31f097925854634440a791)
- Clean up unnecessary #include directives in crypto/cmp and crypto/crmf directories.
  ↳ No PR: [ef63a77](https://github.com/openssl/openssl/commit/ef63a77758e769dd205069d881b0556e142e11b1)
- Replace OPENSSL_assert in b64_write and b64_ctrl with ossl_assert, and return an error on failure.
  ↳ No PR: [305bbc1](https://github.com/openssl/openssl/commit/305bbc1837ff31389e8330f14446286695e105fa)
- Use assertions instead of condition checks when read lock and write lock acquisition fails to ensure that the lock operation is successful.
  ↳ No PR: [606de50](https://github.com/openssl/openssl/commit/606de509e3828fd2fb65184500e6197c82a0efcf)
- Remove by_store_subject_ex function, simplify by_store_subject and by_store functions, and add lock protection.
  ↳ No PR: [af5952d](https://github.com/openssl/openssl/commit/af5952d533b772ef8a3d7c666ed918acfc1dd911)
- Switched the way cipher argument lists are generated to the new name/type code generator.
  ↳ No PR: [04e969d](https://github.com/openssl/openssl/commit/04e969d1f67b441c9f9474918c60085d20090ae8)
- Migrate the code generator for chacha20_poly1305 password from the old version of produce_decoder to the new version of produce_param_list.
  ↳ No PR: [83fa1b8](https://github.com/openssl/openssl/commit/83fa1b8b94d97371809cf23fb9a384a22581f3e4)
- Updated ML-KEM key management implementation, using TRIE decoder to optimize parameter lookup and fromdata call.
  ↳ No PR: [60f9c9d](https://github.com/openssl/openssl/commit/60f9c9d804d46d72ef37e6e87b06f25fc7b32a0e)
- Change parameter definition and lookup logic in ML-DSA key management to use machine-generated TRIE decoders.
  ↳ No PR: [3991ade](https://github.com/openssl/openssl/commit/3991ade5a5b57c0b81375e47e1ac502671177635)
- Rename the internal enumeration constants NONE, GET, and SET to OSSL_ACTION_ prefix to prevent name conflicts.
  ↳ No PR: [c37b9e3](https://github.com/openssl/openssl/commit/c37b9e3425c8576d089342c7cfdcc4dc0aedde54)
- The ML-KEM key management module uses an automatically generated parameter decoder instead of manual parameter search.
  ↳ No PR: [4fc0692](https://github.com/openssl/openssl/commit/4fc06921b7f3a5e2fe4caf74dfae5df37fb7824f)
- Updated the ML-DSA key management module to use the improved parameter decoder processing method.
  ↳ No PR: [61d2072](https://github.com/openssl/openssl/commit/61d20724a667e22c0ae3e2d2b37844f775cd0e16)
- Reconstruct the GCM implementation and use the parameter decoder instead of the original parameter table definition.
  ↳ No PR: [dce3a00](https://github.com/openssl/openssl/commit/dce3a00be60aa4197c8009d3e20ecb14bd28fe9d)
- Update the parameter processing of ChaCha20-Poly1305 to use the new parameter decoder mechanism.
  ↳ No PR: [e20800d](https://github.com/openssl/openssl/commit/e20800d744ba06e7d7afdeda98fde26e4ae4cc14)
- Reconstruct the init_get_thread_local function, split it into multiple auxiliary functions, and simplify the naming of thread local management functions.
  ↳ No PR: [d259b8b](https://github.com/openssl/openssl/commit/d259b8b85567410afa02acf2ba9dbbfb8ae53f61), [c09b867](https://github.com/openssl/openssl/commit/c09b86749b69d97c71037eb64c8638e41ce214da)
- Changed cipher parameter decoding to table-based implementation to simplify parameter processing.
  ↳ No PR: [d09a7ca](https://github.com/openssl/openssl/commit/d09a7cad9ab7403d3c40267bb5a62dfae3c13deb)
- Switch to using TRIE and struct-based parameter name decoders in the ML-DSA signature implementation.
  ↳ No PR: [3bb06ce](https://github.com/openssl/openssl/commit/3bb06ce79806d7e725244dd62212ef935112b82c)
- Convert algorithm-obtainable parameters to structure-based TRIE decoding method.
  ↳ No PR: [07399c2](https://github.com/openssl/openssl/commit/07399c25663c13dec835392cff2ac3aaafde6570)
- Convert parameter parsers for multiple KDF implementations (including HKDF, TLS1 PRF, SSKDF, etc.) to automatically generated versions.
  ↳ No PR: [dc29427](https://github.com/openssl/openssl/commit/dc294270c00f360d456c7ce05c45690dc62eb387), [a6fe570](https://github.com/openssl/openssl/commit/a6fe57013a234386c21df8252a97067508f19973), [682f0e1](https://github.com/openssl/openssl/commit/682f0e19d8bef15e8e5fcb86e476bc36a752867c), [fcc2dd2](https://github.com/openssl/openssl/commit/fcc2dd27321307edeb0efd4658cb23910f5c3b4e), [387c033](https://github.com/openssl/openssl/commit/387c033a702fccc44d3782903e3384fc4d844d12), [552f57e](https://github.com/openssl/openssl/commit/552f57e5e236fd752645016618dafdf57fc82543), [cb6ab5b](https://github.com/openssl/openssl/commit/cb6ab5b78a18ef2c1fb8211380ccd933019dfedc), [61e4e10](https://github.com/openssl/openssl/commit/61e4e10caa1e836a3747fce98a285239f76f58c3), [2ab5051](https://github.com/openssl/openssl/commit/2ab50514778ea4e13add99fef62d66f374797ea9), [1f6adcb](https://github.com/openssl/openssl/commit/1f6adcb9cce33850408bfbabf79494751f4eea6b)
- Simplify the ossl_param_get1_concat_octet_string function and remove the maxsize parameter and related checks.
  ↳ No PR: [f04db6a](https://github.com/openssl/openssl/commit/f04db6af459567348963759640988c5348061bc0)
- Migrate the parameter parsers of multiple KDF algorithms (PKCS12, pbkdf1, krb5kdf, etc.) to automatic generation.
  ↳ No PR: [ee3ada8](https://github.com/openssl/openssl/commit/ee3ada89b779665bbae972df4e3f50f072f72563), [d77651b](https://github.com/openssl/openssl/commit/d77651bc099711fcb0a8752363fbccbda082909b), [c30b677](https://github.com/openssl/openssl/commit/c30b67748a7f2fa31299fe9e50ada0681c0108a6), [9aec76e](https://github.com/openssl/openssl/commit/9aec76e6f9ce4349cf6262ca8e365a34a8853cec), [e5d7e4f](https://github.com/openssl/openssl/commit/e5d7e4f42a26df4770a07e7f3bc16fe3336696ad)
- Convert parameter processing of multiple MAC algorithms (HMAC, KMAC, CMAC, etc.) to using automatically generated parameter decoders.
  ↳ No PR: [aad2304](https://github.com/openssl/openssl/commit/aad2304aa9001846480c790f4efb2c2fd74afd2e), [483a18a](https://github.com/openssl/openssl/commit/483a18ae9ed90691d022b42d4ea20821934f8465), [404f198](https://github.com/openssl/openssl/commit/404f19838fa38fa3435b942d3cc356da8da10512), [5de2b13](https://github.com/openssl/openssl/commit/5de2b13b2dadf40323919557b616e0c389174faf), [969011c](https://github.com/openssl/openssl/commit/969011c3c5708c56a1950e09ee0202371cb0d2a8), [acb316b](https://github.com/openssl/openssl/commit/acb316bc20fe26b2f1042fd620a0c7c89d53eeeb), [96e9628](https://github.com/openssl/openssl/commit/96e96280ae8a8121aab20bfd5cc19910dcf80624)
- Change the parameter decoder of DH, ECDH and ECX key exchange to automatically generated mode.
  ↳ No PR: [fa4545f](https://github.com/openssl/openssl/commit/fa4545f4218df3b7b0a9a60f33ea23bbab21ee52), [fcb7e77](https://github.com/openssl/openssl/commit/fcb7e772fbe68a416c85cb083ba1ba6f56e1e87d), [213135a](https://github.com/openssl/openssl/commit/213135a758c2914ce1c983b1feb89f28f2082400)
- Change the parameter decoders of ML-KEM and EC KEM to automatic generation.
  ↳ No PR: [af841ad](https://github.com/openssl/openssl/commit/af841adf9fb0aedbc047ba8b59a5437ed21a89b8), [c90eb15](https://github.com/openssl/openssl/commit/c90eb152687f0f6023b14c05faef887a1fa225fd)
- Update the header file reference path in KEM implementation to prepare for automatic generation of parameter parsing.
  ↳ No PR: [47a305b](https://github.com/openssl/openssl/commit/47a305bc78273eae0320738f6bb66643a343dbcf)
- Extract lock competition record logic into an independent function to simplify read-write lock competition processing.
  ↳ No PR: [b1303b1](https://github.com/openssl/openssl/commit/b1303b115ef2bf7f8f0caf46341b20e634213dfb)
- Updated the call to ossl_prov_set_macctx in mac_digest_sign_init to remove redundant parameters.
  ↳ No PR: [0b8c7b9](https://github.com/openssl/openssl/commit/0b8c7b936eb0235aebdeff96dae51fd7c6c08ecd)
- Unify the parameter decoders of multiple algorithms (including ecx KEM, RSA KEM, ECDSA, etc.) into automatic generation.
  ↳ No PR: [d6d2cc7](https://github.com/openssl/openssl/commit/d6d2cc750969ede5c2368b4d72fcd3df2d151705), [ea5c3c2](https://github.com/openssl/openssl/commit/ea5c3c284e39ca3c60a3745bd20e98e32c5bec45), [3c9ad1d](https://github.com/openssl/openssl/commit/3c9ad1dba946c5e6abbdf3fbda46ab1cbf746b7b), [74ccf8c](https://github.com/openssl/openssl/commit/74ccf8ce976e0874d357e4c1564c9aaed751b7ac), [7919746](https://github.com/openssl/openssl/commit/79197465e3bfc4992a884bc9c21716931c2e4536), [c1fd9a4](https://github.com/openssl/openssl/commit/c1fd9a4f8b582f4fc27b7f0533d9f7673d99513c), [a14e2f4](https://github.com/openssl/openssl/commit/a14e2f417eb4f7d673b1f39f5202ace2f688b7d5), [1c5780e](https://github.com/openssl/openssl/commit/1c5780ee52164e90399e206099fe2ba3b2f21d31)
- Simplified handling of OPENSSL_SMALL_FOOTPRINT branch in CRYPTO_aligned_alloc.
  ↳ No PR: [1b74208](https://github.com/openssl/openssl/commit/1b742083e37f4d9674f0bf1078cc1cada46d8108)
- Simplify the logic of padding type decoding in RSA asymmetric cipher implementation.
  ↳ No PR: [e676a87](https://github.com/openssl/openssl/commit/e676a87a279573b536e2f8cdd810abcf561dfd13)
- Simplify HKDF's pattern decoding logic.
  ↳ No PR: [c33bce6](https://github.com/openssl/openssl/commit/c33bce644052e272c3836daec29c0f865ec3a0fd)
- Integrate buffer parameters dispersedly passed in multiple functions into a structure to simplify the function interface.
  ↳ No PR: [fff4b18](https://github.com/openssl/openssl/commit/fff4b181bf3d7a53a24b7d975b4b6af4facd1045)
- Re-added OSSL_ prefix to parameter names.
  ↳ No PR: [106bb67](https://github.com/openssl/openssl/commit/106bb67f783f3dcad891f7f48c76e09e5a762fea)

### Test related
- Allow brace blocks to be used in case and default branches of switch statements, and related tests updated.
  ↳ No PR: [560ea7f](https://github.com/openssl/openssl/commit/560ea7ffbf5abac871a8d53f6aa3a44ac0349619)
- Added FIPS version and availability flags to ECDSA deterministic test data.
  ↳ No PR: [cfc2a07](https://github.com/openssl/openssl/commit/cfc2a07fdaba82afd3d7cd8a837f90829924df60)
- Added test cases for the combination of ECDSA and KECCAK-256 hash algorithms.
  ↳ No PR: [69fa61b](https://github.com/openssl/openssl/commit/69fa61b08253a991e5553f35bd9fdaf8dc9aec43)
- Fixed infinite loop, incomplete frame processing and qlog empty frame issues in quic_multistream_test test.
  ↳ No PR: [ad684e1](https://github.com/openssl/openssl/commit/ad684e1a6a925c7fbadad7d309f0204f49e67105), [8ed3eee](https://github.com/openssl/openssl/commit/8ed3eee3b416d0bff4890bba24af4a7a1839bf78), [0162f75](https://github.com/openssl/openssl/commit/0162f75fb1ae4adfb56f022884d8325521bcc141)
- Made the backoff period of noisy dgram BIO configurable, and adjusted the relevant test code.
  ↳ No PR: [131fff1](https://github.com/openssl/openssl/commit/131fff1b09e07eeb5db8b99d7e8f502d8c4fb1e5)
- Relaxed the timeout value in tests to avoid test timeout failures.
  ↳ No PR: [46e1417](https://github.com/openssl/openssl/commit/46e14174da24a5f4fd5c480f1906371e2edd62cb)
- Added multiple expected output configuration files for configuration tool testing, covering scenarios such as escape characters, spaces, sequences and variables.
  ↳ No PR: [b43913b](https://github.com/openssl/openssl/commit/b43913be7ea11306b74fab000902a53345bc2b49)
- Introduced a corruption mechanism in ML-DSA pairing consistency testing to support testing of verification failure scenarios.
  ↳ No PR: [89b5a9b](https://github.com/openssl/openssl/commit/89b5a9b8bcf6bfc6d210a8078c43e6f8f77c1377)
- Added test support for ML-DSA, SLH-DSA and ML-KEM algorithms in pairwise failure testing.
  ↳ No PR: [3f28cc6](https://github.com/openssl/openssl/commit/3f28cc6e63cdafdea08921abf12066ddfc68e6ec)
- Updated certificate data in test files.
  ↳ No PR: [1dc52b4](https://github.com/openssl/openssl/commit/1dc52b4f7d8f14ec892a91663b797a39b80c7d35)
- Fixed the problem of incorrect use of X509_get_subject_name in the test_store_open_winstore function, which has been replaced by X509_get_issuer_name.
  ↳ No PR: [934086f](https://github.com/openssl/openssl/commit/934086fb9161e2f4967ad8577a1f3e489cff73d2)
- Fixed an issue where uninitialized pointers in test functions could lead to undefined behavior.
  ↳ No PR: [4dca928](https://github.com/openssl/openssl/commit/4dca928a29cbe413f2416ac5e1ba2fe4e073f608)
- Fixed memory leak in test file, added memory release in error handling path.
  ↳ No PR: [f4d9904](https://github.com/openssl/openssl/commit/f4d9904763e59db031007f4a938f1f8b96fdcee7)
- Fixed memory leak when SSL_new fails in qtest_create_quic_objects function.
  ↳ No PR: [de1e498](https://github.com/openssl/openssl/commit/de1e4989d564ea9a6d2960204806a1f3537419ad)
- Fixed possible memory leak when setting trace callback in test harness.
  ↳ No PR: [3818f77](https://github.com/openssl/openssl/commit/3818f7779ef4bf4d4ccacd13506ec92885e45553)
- Fixed memory leak in evp_test.c caused by OPENSSL_zalloc failure.
  ↳ No PR: [e8deb32](https://github.com/openssl/openssl/commit/e8deb32af4874c781838c1596c6355712b5d0ed0)
- Added regression test to verify that HMAC_Update should return an error after HMAC_Final.
  ↳ No PR: [a5d1ead](https://github.com/openssl/openssl/commit/a5d1eadde1d566b528cfe495953300cd9f9fe1e9)
- A thread synchronization mechanism for condition variables and mutex locks was introduced in the QUIC API test helper function to fix occasional race condition failures.
  ↳ No PR: [864333b](https://github.com/openssl/openssl/commit/864333b455eb36ba84562d6482547bf4c8b49581)
- Added a failing test case for QUIC double release issue.
  ↳ No PR: [9ed90fd](https://github.com/openssl/openssl/commit/9ed90fd44cc1b8039d82610d90f56275d519c204)
- Added negative test cases for the LMS signing function, covering scenarios such as key generation, signature and parameter generation.
  ↳ No PR: [dff3695](https://github.com/openssl/openssl/commit/dff36957a42593f51a1af2be8be4fcb5126c7060), [57267e2](https://github.com/openssl/openssl/commit/57267e2bcf67cec937ca3c5dbb08c7d9ea944dd4), [34520fd](https://github.com/openssl/openssl/commit/34520fd5452c2c5180aba86496a13d1cc515a449)
- Added tests for QUIC connections, verifying write key order and SSL_set_verify callback behavior.
  ↳ No PR: [9a5ac06](https://github.com/openssl/openssl/commit/9a5ac06921357bdfd4e2f74b5b32955464bf9b75), [fbb2a20](https://github.com/openssl/openssl/commit/fbb2a20732277ebf185ecaadb9e8570f8e9771d7)
- Fixed memory leaks, type comparison errors and null pointer checks in QUIC tests.
  ↳ No PR: [b63b019](https://github.com/openssl/openssl/commit/b63b019f6605ffbdf7cfedb7f9ad7d3ad37686a8), [ac6178c](https://github.com/openssl/openssl/commit/ac6178c3f1835e7b1f640daaadc937ab202fda13), [efa2d85](https://github.com/openssl/openssl/commit/efa2d85571a50c5a697677e3568007eb0d8dcbe7)
- Fixed memory leak in EVP test and BIO test.
  ↳ No PR: [d9b0230](https://github.com/openssl/openssl/commit/d9b02304602d61e35570bd990faad89ee0ae7140), [53a83a7](https://github.com/openssl/openssl/commit/53a83a7921763aa6637e875aec55f504aa5f5df2), [2ad09ef](https://github.com/openssl/openssl/commit/2ad09ef41396c22ade94a2cd3257843f0439b044)
- Fixed the parameter acquisition error in the EVP KDF test and added a new test case.
  ↳ No PR: [1c0c200](https://github.com/openssl/openssl/commit/1c0c2008f28795072ec9a83ce97b7a4ed47cbee7), [5a4a43a](https://github.com/openssl/openssl/commit/5a4a43a60ac8da63e60e68f6607cd5e7fc71b7ea)
- Added a new test to verify that thread-local keys can be repeatedly created and destroyed without leaking.
  ↳ No PR: [b994ce4](https://github.com/openssl/openssl/commit/b994ce4088fb52e769ee5e3e49bdde3030fadaf7)
- Added unit test cases in the random number test to verify memory out-of-bounds scenarios.
  ↳ No PR: [6d490a9](https://github.com/openssl/openssl/commit/6d490a92fe49ea6e41cb7874086dbad5462078c6)
- Added second macro indentation test to test file and updated comment instructions.
  ↳ No PR: [e925b99](https://github.com/openssl/openssl/commit/e925b99f9435826aca3fa41b7661e6e9fa7e10b6)
- Added null pointer check for BIO_new, SSL_CTX_new and EVP_PKEY_new return values in fuzz tests.
  ↳ No PR: [be7467f](https://github.com/openssl/openssl/commit/be7467f5a0aa098531597b95a71be6d7c2a463c7)
- Deprecated tests related to ASN1_METH and adjusted key type parsing logic in SSL test context.
  ↳ No PR: [3a90d5f](https://github.com/openssl/openssl/commit/3a90d5f83cbcc151a04b994856fc22c85b52d8f3)
- Fixed compilation warning on s390 platform due to improper use of copy length parameter.
  ↳ No PR: [837592d](https://github.com/openssl/openssl/commit/837592dcd994a22a7c8d08bf3cf421f6b2e51280)
- Fixed check-ansi job failure, updated PEM private key data in test files.
  ↳ No PR: [0d5c776](https://github.com/openssl/openssl/commit/0d5c7766946f0bb423e9256ccdaf194e6befd619)
- Improved SM2 testing: cleaned test data and added signed test cases.
  ↳ No PR: [7bf4b30](https://github.com/openssl/openssl/commit/7bf4b30bcc8eb576790abc68a741d9687bd79853), [499f655](https://github.com/openssl/openssl/commit/499f65533708318af57f0190315672aaeaf10f84)
- Improved test random number generator: added deterministic random input instructions, and updated parameter handling for generator and CRNG tests.
  ↳ No PR: [d73d40a](https://github.com/openssl/openssl/commit/d73d40af3757e29460076d6a3c997298f5263527), [fbdde4c](https://github.com/openssl/openssl/commit/fbdde4c799b43750cbc65a24d3fc874ed67bd351), [e77b362](https://github.com/openssl/openssl/commit/e77b362e87b4db2554824e19ba15bdb07f02cc08)
- Added SSL handshake memory allocation failure test and memory allocation function sanity test.
  ↳ No PR: [437cde8](https://github.com/openssl/openssl/commit/437cde84a7ef23602abbf95adf24a26ee9635c0c), [d090695](https://github.com/openssl/openssl/commit/d090695101a96fedd5457d1d867726ba5e92ddee)
- Fixed memory leaks and logic errors in multiple tests.
  ↳ No PR: [fcb5e20](https://github.com/openssl/openssl/commit/fcb5e20ac74071bda4fc8b5ca6e3b115d8d683e5), [d6fcaa5](https://github.com/openssl/openssl/commit/d6fcaa5658bca18474a5e55d7c4807efcc242173), [abebeb1](https://github.com/openssl/openssl/commit/abebeb1bb008452f9d0524509627d015dc69fbd1), [2b76895](https://github.com/openssl/openssl/commit/2b76895152fe7c7bcd11b9ae6e712c0437aee8c3), [a0a73f5](https://github.com/openssl/openssl/commit/a0a73f52ad5a33576fec69ab9d74c29fa4621aea)
- Enhanced bioprinttest test: added comparison test with libc, integer format test and print format check.
  ↳ No PR: [f5bb949](https://github.com/openssl/openssl/commit/f5bb94918f28ad939398e7a739cce68c2b191da5), [8d8a8aa](https://github.com/openssl/openssl/commit/8d8a8aac533139a56bb8b15234a412e96b3486dc), [9deaf83](https://github.com/openssl/openssl/commit/9deaf83833382d909bde1ddceb0d2a80b775bc7f)
- Fixed an issue in the test program where the file handle was not closed when file reading failed.
  ↳ No PR: [d3e781b](https://github.com/openssl/openssl/commit/d3e781b764bcbbca16dd53e0677edcfad72afb77)
- Reorganize the test code, fix Coverity false positives, and make the process clearer.
  ↳ No PR: [ac87f6b](https://github.com/openssl/openssl/commit/ac87f6b3a36ee3beac9e806c33127269edb6ca20)
- Adjust the timeout parameters in QUIC testing, increase the number of idle detection rounds and reduce the time step.
  ↳ No PR: [076f7b2](https://github.com/openssl/openssl/commit/076f7b24fee1b80a5cda898f385ae813217c823f)
- Fixed the usage of setitimer to cancel the timer in the test.
  ↳ No PR: [1b1a859](https://github.com/openssl/openssl/commit/1b1a859d3d8aafbdda2977f9955ceee6f32f7ea4)
- Adjust the test initialization order and advance global_init call before test_open_streams.
  ↳ No PR: [39029a1](https://github.com/openssl/openssl/commit/39029a1bb0cd10de986239c9fc58228c2501a5f4)
- Add checking of sk_sint_push return value to enhance test reliability.
  ↳ No PR: [257ac12](https://github.com/openssl/openssl/commit/257ac1279877f05a997c76f58fc0c7af08e02718)
- Fix buffer size calculation in BIO_snprintf test, use full buffer size.
  ↳ No PR: [dc415d9](https://github.com/openssl/openssl/commit/dc415d9ff18dbde023f8518505fec323881e566a)
- Added TLSv1.3 group selection test case to verify the behavior of the client when sending disallowed key shares.
  ↳ No PR: [9226b3e](https://github.com/openssl/openssl/commit/9226b3e8f4cb4dfb8a43fd2790ef506f75a11e76)
- Fixed the missing length modifier of the format specifier in the test case, and added the negative floating point test.
  ↳ No PR: [e489bfb](https://github.com/openssl/openssl/commit/e489bfbcd58b8ac91e108c6bb669bf5f07217b2c)
- Fixed the inconsistency between the %n result assignment and the check field in the test, and updated the expected value.
  ↳ No PR: [0b00e23](https://github.com/openssl/openssl/commit/0b00e23df82af08ba04f482745bd7ddbff2da34b)
- Simplify the SLH-DSA test process and remove conditional judgments.
  ↳ No PR: [2550035](https://github.com/openssl/openssl/commit/255003535b35f26bb7bdb33c246726dfdc0cfa60)
- Modify the memory allocation method in the torture_rcu_high test to facilitate problem detection.
  ↳ No PR: [a09a68c](https://github.com/openssl/openssl/commit/a09a68cef79bcf4f91da1b3b28410a4d317bfb94)
- Fixed the problem of incorrectly calling the cleanup function when RAND_bytes fails in test_WPACKET_quic_vlint_random.
  ↳ No PR: [732a0a5](https://github.com/openssl/openssl/commit/732a0a5df8324240e115d599c79487844d64efec)
- Fixed TERP_run function accessing uninitialized structures on wrong paths.
  ↳ No PR: [84432e9](https://github.com/openssl/openssl/commit/84432e9b6cb88767a8225a53baa812efd22aaa1b)
- Fix the logic error of rwreader_fn function in torture_rw_high/low test.
  ↳ No PR: [8ca9655](https://github.com/openssl/openssl/commit/8ca96550ad79daa76d010bb110ba558286636de9)
- Skip related tests when the LMS algorithm is unavailable, and add multiple failure scenario test cases.
  ↳ No PR: [ba0062e](https://github.com/openssl/openssl/commit/ba0062ee23c54069654aaadb91c33cc6afed8d6b)
- Skip tests based on FIPS provider version in ssl_trace tests.
  ↳ No PR: [19c96a8](https://github.com/openssl/openssl/commit/19c96a8d61c80eb00e738993a4f0d7d1e07cc450)
- Re-enable ssl_trace_test testing.
  ↳ No PR: [b9cb0b2](https://github.com/openssl/openssl/commit/b9cb0b2dbe26a0fc95d9e5521a1e4e9b61381c95)
- Added boundary case test case for converting attribute list to string.
  ↳ No PR: [a518be8](https://github.com/openssl/openssl/commit/a518be8aa82123b8d04e574272db20d93df4ed30)
- Add test case for KRB5KDF using wrong key size.
  ↳ No PR: [2dbcae3](https://github.com/openssl/openssl/commit/2dbcae3b08436c578fe47b3d721c3c9f806fa07a)
- Fixed check-format.pl's false positives on spaces and left brackets in typedef, and added corresponding test cases.
  ↳ No PR: [4a3809f](https://github.com/openssl/openssl/commit/4a3809f7056b78031e72fc4e90eec3e708ca27e1)

### Performance optimization
- Added an optimized SHA-256 implementation based on the Zbb extension for the RISC-V platform, and automatically selected the implementation at runtime based on hardware support.
  ↳ No PR: [08c8dd6](https://github.com/openssl/openssl/commit/08c8dd6b8cede3cdbe5b1866c1a7544e0fe7a378), [49a3e7a](https://github.com/openssl/openssl/commit/49a3e7adc392a45c3fba93f5759df6797fcd8238)
- Added optimized SHA-512 implementation based on Zbb extension for RISC-V platform.
  ↳ No PR: [a41f913](https://github.com/openssl/openssl/commit/a41f9135f0824a0ff81e2e6b59158ee5dd529662)
- Updated the parameter decoding of CCM mode AEAD password to use the TRIE decoder to improve the performance of setting and obtaining authentication tags.
  ↳ No PR: [3f5dc06](https://github.com/openssl/openssl/commit/3f5dc064d0219237655dac940272892b35f3ffad), [bf0f1b5](https://github.com/openssl/openssl/commit/bf0f1b5d6f3d32ff2ee4d5b3bb5f4909acc0b82c), [0d96937](https://github.com/openssl/openssl/commit/0d969379cb22f62bb7d43ce83d43f2b8eb18b927)
- Reconstruct master_key from a sparse array to a top-level fixed array, and instead search directly through the index to improve performance.
  ↳ No PR: [bbd886c](https://github.com/openssl/openssl/commit/bbd886c501ed38d1256cf5eb445737a25aeb28f2)
- Restore the use of operating system-level thread-local storage keys to manage the default OpenSSL context to improve the performance of frequently switching default contexts.
  ↳ No PR: [5466197](https://github.com/openssl/openssl/commit/5466197f16f61e08af70c73e622534f2b984c419)
- Add lock competition detection function to pthreads implementation, enable it through REPORT_RWLOCK_CONTENTION macro, and record lock blocking time and call stack.
  ↳ No PR: [ab021b6](https://github.com/openssl/openssl/commit/ab021b624f1d09378bb5115ccfa01517a5ea0bdc)
- Added ossl_likely and ossl_unlikely macros for common conditional branches in the summary function to optimize branch prediction performance.
  ↳ No PR: [112f3af](https://github.com/openssl/openssl/commit/112f3afd21e7a93cc950d05cc3f0050ea7bcf2db), [d1facb4](https://github.com/openssl/openssl/commit/d1facb485810f0db9ae21b5b1ff3abb080d5084e), [704a210](https://github.com/openssl/openssl/commit/704a2108ab988456900bdf4c7079c1ca7d49360b)
- Add branch prediction hints (ossl_likely/ossl_unlikely) to multiple functions in bn_lib.c, and uniformly change memory allocation calls to OPENSSL_calloc form for micro-optimization.
  ↳ No PR: [6c9712e](https://github.com/openssl/openssl/commit/6c9712e6b73bc798368a424291b47843de6dd665)
- Optimize branch prediction in CRYPTO_malloc, use ossl_likely and ossl_unlikely macros, and extract error reporting logic into ossl_report_alloc_err function calls.
  ↳ No PR: [296e4d3](https://github.com/openssl/openssl/commit/296e4d3c95b43922affa1407350c03184d6b59f5)
- Optimize the branch prediction in the OPENSSL_init_crypto function and use the ossl_likely and ossl_unlikely macros to improve performance.
  ↳ No PR: [340827c](https://github.com/openssl/openssl/commit/340827c819f905a772dce1c41da4d9f07bd16b02)
- Introduce the ossl_likely macro into the OSSL_PARAM_locate and OSSL_PARAM_get_uint64 functions to optimize branch prediction to improve performance.
  ↳ No PR: [682f701](https://github.com/openssl/openssl/commit/682f701985282be4c4ee4ce21db15bf86a44e90d)
- Changed the lock competition data storage to be managed independently by thread ID, eliminating the locking overhead when writing reports and significantly improving performance.
  ↳ No PR: [99d0d23](https://github.com/openssl/openssl/commit/99d0d23e05b0011c25b31b2b0e8254f544163a92)
- Change the write lock in the CRYPTO_secure_actual_size function to a read lock, because no writing operations are required in the critical section.
  ↳ No PR: [8253b58](https://github.com/openssl/openssl/commit/8253b58d60eec11fdb5e5dbf9cc61f78a9b7095d)
- Reconstruct the lock mechanism for object addition and search to reduce lock competition and improve concurrency performance.
  ↳ No PR: [88a1fbb](https://github.com/openssl/openssl/commit/88a1fbb8d1b22a7c54483e50eed9ca77d28ee441)
- Adjust signature algorithm support in the speed tool, disable composite signature algorithms and increase the upper limit of the number of algorithms to 256.
  ↳ No PR: [dab850f](https://github.com/openssl/openssl/commit/dab850f4999e47182cbc1539795049a52e029b70), [39e286b](https://github.com/openssl/openssl/commit/39e286bd26c1e24fb354b30d729fb87015fc3bb3), [7bdc0d1](https://github.com/openssl/openssl/commit/7bdc0d13d2b9ce1c1d0ec1f89dacc16e5d045314)
- Add branch prediction optimization macros in BN_GF2m_mod_arr and CRYPTO_THREAD_run_once functions.
  ↳ No PR: [d083024](https://github.com/openssl/openssl/commit/d083024b733ab8d406d2630338bd1363259f732b), [e740864](https://github.com/openssl/openssl/commit/e740864976565964fbbbb62e01f18306b1fa8206)
- Documented x86-64 SHA-512 family optimization, using SHA512 ISA extension to improve digest algorithm performance.
  ↳ No PR: [196b36f](https://github.com/openssl/openssl/commit/196b36f0d0c8bc9d227cb6ef2cc48fd6f4ed8c7e)
- Added a new build type based on profile guided optimization, and updated the INSTALL.md document.
  ↳ No PR: [d8277a6](https://github.com/openssl/openssl/commit/d8277a6fba7afe6155884dd1c5300dbc829638a7)
- Switched ChaCha20-Poly1305 parameter name decoder to TRIE based implementation.
  ↳ No PR: [b87f440](https://github.com/openssl/openssl/commit/b87f4407c72bea7044ef86f6ef7a3eb9bd746606)
- Optimize thread local context data storage, change CTX_TABLE_ENTRY to a sparse array to reduce memory overhead.
  ↳ No PR: [68c1fcc](https://github.com/openssl/openssl/commit/68c1fcc99e344444f0e0885bfd27d3a776dd4ebf)
- Enable branch coverage reporting in Coveralls runs.
  ↳ No PR: [1187df5](https://github.com/openssl/openssl/commit/1187df53287dcb1ba04479a1cd2dd0547dc14354)
- Suppress potentially irrelevant error queue entries when calling OSSL_STORE_find() in cache_objects().
  ↳ No PR: [a6f858b](https://github.com/openssl/openssl/commit/a6f858b1912b68d98a45fb3cebc832519dea7c85)
- Fixed the memory leak caused by the save_template and save_keyspec functions in the CMP application not releasing the BIO object when writing the file failed.
  ↳ No PR: [e0ae801](https://github.com/openssl/openssl/commit/e0ae801728776b53e2be0972846072ce32bea304)
- Fixed the memory leak problem caused when PKCS7_add_signed_attribute() fails.
  ↳ No PR: [6543f34](https://github.com/openssl/openssl/commit/6543f34dda8908db56372581eef6eafa0ae4add4)
- Fixed the memory out-of-bounds problem when testing nonce copy in RNG.
  ↳ No PR: [da585e2](https://github.com/openssl/openssl/commit/da585e214cf98468e28f4c12ec96ecc7a6192746)
- Fix memory leak in test file: move BIO_free() call to error handling label, and add null pointer check.
  ↳ No PR: [13259a7](https://github.com/openssl/openssl/commit/13259a758ada910aec10313cd063ce54dacfc4a5)
- Fixed the memory leak caused by trace_data not being released in the setup_trace_category function.
  ↳ No PR: [b2e7c4e](https://github.com/openssl/openssl/commit/b2e7c4e2baa92255c57413113e96d67c23b39a34)
- Fixed memory leak in abnormal branch of ssl_set_cert_and_key function.
  ↳ No PR: [7a8cbd1](https://github.com/openssl/openssl/commit/7a8cbd1c4ffd04ad458cd27da2c9f3a9b7d378c0)
- Optimize the argon2 KDF implementation to avoid repeated searches for the size parameter during the derivation process.
  ↳ No PR: [b7a38a1](https://github.com/openssl/openssl/commit/b7a38a14ef82db91dc2caa2c0df8554f61bef9b0)
- Reorder bn_mont_ctx_st structure members to save 8 bytes of memory space.
  ↳ No PR: [3f540b6](https://github.com/openssl/openssl/commit/3f540b6def5218aca11564e8b6c7169e34b1c68d)
- Replace strdup() with OPENSSL_strdup(), making sure to be paired with OPENSSL_free().
  ↳ No PR: [7fa5104](https://github.com/openssl/openssl/commit/7fa51041e4d68838b2c7ddf4f77d6bba0edf2735)
- Reconstruct the by store method of X509_LOOKUP, optimize the cache data structure and open the store in advance to report errors as early as possible.
  ↳ No PR: [0c48ee2](https://github.com/openssl/openssl/commit/0c48ee2bf513cbc2f1de2ff8bc11750e4b593620)
- Optimize the processing of multiple seed parameters in TLS1-PRF, and merge multiple reallocs to improve efficiency.
  ↳ No PR: [35cc673](https://github.com/openssl/openssl/commit/35cc673927d72acce1a0cb1a45b6fcab04184f1c)

### Security related
- Security hardening of the CRYPTO_aligned_alloc function: added verification that the alignment parameter must be a power of 2, fixed the problem of possible overflow in size calculation, added overflow check and error reporting.
  ↳ No PR: [1104e80](https://github.com/openssl/openssl/commit/1104e80c8dff7d04eb482ddc315947268c251384), [89f1f9b](https://github.com/openssl/openssl/commit/89f1f9bd73351e5f4fe16bcd8062d71e8f1fe5a7)
- Fixed multiple integer overflow vulnerabilities in BIO print functions: limit format string width and precision to INT_MAX, and fix signed integer overflows in fmtstr and doapr_outch.
  ↳ No PR: [a8d02c5](https://github.com/openssl/openssl/commit/a8d02c5ca706384c53c941b3041c326c62a6f09e), [7ff5df1](https://github.com/openssl/openssl/commit/7ff5df1014205bc0b45a12163b2e0b31492bf641), [cffbccf](https://github.com/openssl/openssl/commit/cffbccf5eafbc351fc9a9f019810e1dfe04eeb17)
- Fixed Minerva timing side channel vulnerability for P-384 curves on PPC platform: use bn_mul_mont_int() for Montgomery multiplication instead, and add assembly implementation of P-384 field operations to reduce timing dependencies.
  ↳ No PR: [85cabd9](https://github.com/openssl/openssl/commit/85cabd94958303859b1551364a609d4ff40b67a5)
- Use RAND_priv_bytes_ex instead of RAND_bytes_ex in QUIC port initialization to enhance key isolation, and use OPENSSL_clear_free instead of OPENSSL_free to wipe sensitive data before releasing.
  ↳ No PR: [50f9451](https://github.com/openssl/openssl/commit/50f945117c12219f52fc76d17154663fc749812d)
- Change the shell command calling method in the CA.pl script from string concatenation to array form to avoid executing commands through the shell and improve security.
  ↳ No PR: [0b1bdef](https://github.com/openssl/openssl/commit/0b1bdef38ef1e3369a7bcde1b9a6eabe44b10e54)
- Add value barriers to constant-time conditional exchange functions to prevent compiler optimization and fix potential timing safety issues.
  ↳ No PR: [8a9e0d0](https://github.com/openssl/openssl/commit/8a9e0d0f499a288cf3363668870806d5e7be3924)
- Switch to secure memory allocation for ML-KEM and ML-DSA private key storage areas to prevent sensitive data leakage.
  ↳ No PR: [815dde3](https://github.com/openssl/openssl/commit/815dde3e2058eadad0e86cfaf9cb68fc3f597ddb)
- Add integer overflow check in ossl_param_buf_alloc, and improve the overflow detection logic of ossl_size_add; at the same time, replace realloc in txp_el_ensure_iovec with a safer array allocation function.
  ↳ No PR: [731fc62](https://github.com/openssl/openssl/commit/731fc629085d9dfc43c073e3e2e0ce6ce5e16349)
- Uniformly replace memory allocation calls with array allocation routines to improve safety and consistency.
  ↳ No PR: [7867bf1](https://github.com/openssl/openssl/commit/7867bf1523bcb12796a5d9c3c7fe598837591991)
- Fixed an integer overflow vulnerability in the BIO_f_reliable record parser to prevent out-of-bounds reads.
  ↳ No PR: [3718a89](https://github.com/openssl/openssl/commit/3718a89e0bd2fa3147ff71b53cdb39611fe35209)
- Fixed an offset error (CVE-2025-9230) in the unwrap key size check in the kek_unwrap_key() function to prevent up to 8-byte out-of-bounds reads and 4-byte out-of-bounds writes due to incorrect check conditions.
  ↳ No PR: [caa664e](https://github.com/openssl/openssl/commit/caa664ea5bb57b387fe59cee021fc745d473b6cf)
- Fixed missing terminating NUL byte after strncpy() call in use_proxy() function, fixes CVE-2025-9232.
  ↳ No PR: [506451c](https://github.com/openssl/openssl/commit/506451cb6b00dc1c3ed51f710cfc18a21942f081)
- Fixed a signed integer overflow problem in the indent_printf() function that may be caused by the addition of two BIO_printf return values.
  ↳ No PR: [651abe1](https://github.com/openssl/openssl/commit/651abe1eb550eb482d98425c979193d5f5e39582)
- When loading credentials fails, add the name of the failed provider and a prompt to load the default provider to the error queue.
  ↳ No PR: [1fc96a3](https://github.com/openssl/openssl/commit/1fc96a3cff124777597ed18c2405dc7181bda2ef)

### Documentation
- Updated links in the documentation: moved the Wiki link to GitHub, moved the documentation link from www.openssl.org/docs to docs.openssl.org, and updated some version numbers.
  ↳ No PR: [da8de0e](https://github.com/openssl/openssl/commit/da8de0e8dd3e09655cd17ef700359c63acdc9cd4), [f014892](https://github.com/openssl/openssl/commit/f014892d9f073b9f73635180c4157d9f892df669)
- Updated NEWS.md and CHANGES.md release notes documents for OpenSSL 3.5 version, and added known issue descriptions.
  ↳ No PR: [21f4bd9](https://github.com/openssl/openssl/commit/21f4bd986b7739f24f67270d533412065c7af0fc), [30adecd](https://github.com/openssl/openssl/commit/30adecd7258b1c657466f1ecf0c1d29491aac0b4)
- Updated the HACKING.md document and added instructions for adding new C source files.
  ↳ No PR: [8bd89f1](https://github.com/openssl/openssl/commit/8bd89f15c967db43e34d9d2986b6fa9614a0a9ac)
- Updated CHANGES.md and NEWS.md, and added fix instructions for CVE-2025-4575.
  ↳ No PR: [f6c400f](https://github.com/openssl/openssl/commit/f6c400f4ccaf6b36f5430aa3f6c94b704e335738)
- Fixed the description of the block cipher padding method in the documentation, correcting PKCS#5 to PKCS#7.
  ↳ No PR: [43cd377](https://github.com/openssl/openssl/commit/43cd3773a33d88d3d53ba61eb4aebdae0f239843)
- Fixed formatting issues in CHANGES.md and NEWS.md: added missing periods, unified project name to OpenSSL, fixed EVP_SKEY format, adjusted line width.
  ↳ No PR: [d72ab74](https://github.com/openssl/openssl/commit/d72ab74243043b580a083e830d4484d1008ddb9a)
- Updated the design document for explicitly obtaining the signature algorithm, changing the API solution from modifying the DigestSign/DigestVerify initializer to extending the EVP_PKEY_sign/verify function.
  ↳ No PR: [66454bf](https://github.com/openssl/openssl/commit/66454bf8bac860212bb959c1e847a0483a053025)
- Improved documentation for the -cipher option in openssl genpkey command, providing clearer instructions and examples.
  ↳ No PR: [bf4c852](https://github.com/openssl/openssl/commit/bf4c852893485689ae6ea660b7bb3b1819d85774)
- Removed duplicate options in several man pages and fixed formatting issues in documentation.
  ↳ No PR: [2c8103e](https://github.com/openssl/openssl/commit/2c8103e468fa6463ef503a3dd8e6e20d1b1afec9)
- Updated the FIPS-README.md document to reflect the latest FIPS validated versions and sample versions, and added that any FIPS validated version can be used with other OpenSSL libraries.
  ↳ No PR: [50316c1](https://github.com/openssl/openssl/commit/50316c18a0468bb0191904d7615955c9b47f061f)
- Updated README-QUIC.md, added information about OpenSSL 3.5 server-side QUIC support, and added command instructions for running the sample QUIC server.
  ↳ No PR: [c66e003](https://github.com/openssl/openssl/commit/c66e00398c9feabc02ff6e678089a3dc95f985d2)
- Updated the README document to remove the description that the QUIC protocol is client-only to reflect that it now also supports the server.
  ↳ No PR: [648366a](https://github.com/openssl/openssl/commit/648366ad010b3b22c1f298d39934d72702b3fd55)
- Added man page documentation for openssl-configutl command.
  ↳ No PR: [08616b0](https://github.com/openssl/openssl/commit/08616b09e02f896dc67f1602e1fa17f2eb5f1a66)
- Updated the keys.txt document: removed the content related to the deprecated algorithms DES3 and DSA, updated the key generation example (use AES256 instead of DES3), and adjusted the document structure.
  ↳ No PR: [86a6d1f](https://github.com/openssl/openssl/commit/86a6d1f9b45a8a79740222821d8bcf66c34f2839)
- Updated Windows build instructions to recommend turning off the build dependency feature for new builds to speed up the build.
  ↳ No PR: [afd32bc](https://github.com/openssl/openssl/commit/afd32bcb5456a9e33b0f4e07f572263b404d4d4b)
- Explicitly state in the documentation of s_client that the -ign_eof and -quiet options implicitly enable -nocommands, to more clearly reflect their impact on command processing.
  ↳ No PR: [20fb5dc](https://github.com/openssl/openssl/commit/20fb5dcb1e2b762545aa127058cc11efe09d6700)
- Improved the link of the GitHub Actions workflow badge in README.md to make it clickable to jump to the corresponding workflow page, and updated the CI status link.
  ↳ No PR: [8ad3705](https://github.com/openssl/openssl/commit/8ad37051e28417b8e851ef7a62904ad9df0f6394)
- Updated documentation to reflect the transition from ANSI-C to C-99 compilers: Renamed NOTES-ANSI.md to NOTES-C99.md and updated the content, and modified related notes in INSTALL.md, NEWS.md and CHANGES.md.
  ↳ No PR: [53e5071](https://github.com/openssl/openssl/commit/53e5071f3402ef0ae52f583154574ddd5aa8d3d7)
- Updated FIPS provider documentation to mark -hkdf_digest_check and -sskdf_digest_check options as deprecated.
  ↳ No PR: [b63adfc](https://github.com/openssl/openssl/commit/b63adfc58acba09f06050553957261aa19b58f0b)
- Added a description of the SSL_CIPHER environment variable in the documentation of the s_time command.
  ↳ No PR: [0afaa27](https://github.com/openssl/openssl/commit/0afaa27df791eb5dc996309e14ba8ba319fa99aa)
- Added description of PATH environment variable in openssl-rehash documentation.
  ↳ No PR: [dcf009c](https://github.com/openssl/openssl/commit/dcf009cd897aa64a69ef82621fe70d89abf0d5c5)
- Updated CHANGES.md and NEWS.md to prepare for the release of OpenSSL 3.6 and 3.5.x patch versions, including version marking, changelog synchronization and release notes.
  ↳ No PR: [145e909](https://github.com/openssl/openssl/commit/145e909a69821b96115b657cf0d9fa374bf8c695), [c51691b](https://github.com/openssl/openssl/commit/c51691b1a34ef3a465def736f69f80c4d9f68f0f), [8d509b0](https://github.com/openssl/openssl/commit/8d509b0326e146d8f44899e78c0cfeff732080f9), [34c61a5](https://github.com/openssl/openssl/commit/34c61a5df27d72e97f89bbed3f48aa8603c81d9b), [630352a](https://github.com/openssl/openssl/commit/630352ad88bb0bc7c52c22977dd1bb3b078d8fd1)
- Removed entry about SLH-DSA key import into PCT from release notes.
  ↳ No PR: [d06993c](https://github.com/openssl/openssl/commit/d06993cb89686107a4c6e2134d330419e9d09785)
- Added a note in NOTES-C99.md that the C99 features <complex.h> and variable-length arrays are not supported.
  ↳ No PR: [1d35a9e](https://github.com/openssl/openssl/commit/1d35a9e8709a278b068837e238ad70dc6327e7ca)
- Updated CHANGES.md and NEWS.md to record changes in OpenSSL version 3.5.4 and fix bugs in preparation for version 3.6.0.
  ↳ No PR: [deef067](https://github.com/openssl/openssl/commit/deef067261e5085bc9b246cc2c4ddfa33f7eebf4), [2735778](https://github.com/openssl/openssl/commit/27357781e0a90bd07d6e9506be73968883ff7f24), [f3ade11](https://github.com/openssl/openssl/commit/f3ade11ef240ffd2eccdf43dd98a74f16494d938)

### Build/CI
- Enabled LMS support in CI build configuration and added related CI support for 3.6 stable branch and FIPS provider compatibility builds.
  ↳ No PR: [2bcfff8](https://github.com/openssl/openssl/commit/2bcfff8509b9a054ce84d768c96f6fd4ca7b9d6f), [ea3ee7e](https://github.com/openssl/openssl/commit/ea3ee7e083251602fff34e6d659f2c0f401b6a5e), [567cbe4](https://github.com/openssl/openssl/commit/567cbe4e2ab51624da5feceefea1b9d5a61d7f36)
- Fixed the release process: when the tag name contains alpha or beta, the release will be correctly marked as a pre-release version.
  ↳ No PR: [1bf328e](https://github.com/openssl/openssl/commit/1bf328edf93a25e7b7bf8d2b5b75aa5e03793dc1)
- CI process now uploads build products even if tests fail.
  ↳ No PR: [289dcbe](https://github.com/openssl/openssl/commit/289dcbe008018b3cf81053cba2b36825a1f49b74)
- Disabled the stringop-overflow warning in CI builds for the s390 platform to resolve gcc 12 false positives; the warning has subsequently been fixed and the related compilation options have been removed.
  ↳ No PR: [69acfa3](https://github.com/openssl/openssl/commit/69acfa358f945b6abb2003fc96f5ed57e183b4fe), [d56e245](https://github.com/openssl/openssl/commit/d56e2450c16217735ebdbc7bc625b3fe6128da9c)
- Prevented CI tasks containing secrets from running in fork repositories and only allowed execution in upstream repositories.
  ↳ No PR: [ee52d7d](https://github.com/openssl/openssl/commit/ee52d7d327e237ce3e45ba736e2e20b7793c4254)
- Separated pkcs11-provider external tests into Fedora containers to run to support kryoptic tokens, and updated the container image to fedora:latest.
  ↳ No PR: [29e7e1d](https://github.com/openssl/openssl/commit/29e7e1dcb6bb532f9c956b9b98bde62ae1f8c182), [402380d](https://github.com/openssl/openssl/commit/402380d3e1f2a3dfd1e717bc8e5ea5f8d282ccd7)
- Replace Windows 2019 runner in CI with Windows 2022 and Windows 2025 to cope with runner image deprecation.
  ↳ No PR: [19dfc46](https://github.com/openssl/openssl/commit/19dfc4672a3e7d152195c890edfdb9bd81d878a7)
- Fixed type warnings in Win64 builds: Eliminated signed/unsigned mismatch issues by adding appropriate type conversions and overflow checks.
  ↳ No PR: [bb86c43](https://github.com/openssl/openssl/commit/bb86c43fa88ce485b13f94514dddb08ce8f60280)
- Added explicit type conversions for multiple functions in providers to eliminate compiler warnings in Win64 builds.
  ↳ No PR: [6f9683d](https://github.com/openssl/openssl/commit/6f9683d651905816f0ecf73e0a0045ddf25c4d3a)
- Added explicit type conversion in libssl to eliminate type mismatch warnings in Win64 builds.
  ↳ No PR: [abdbad3](https://github.com/openssl/openssl/commit/abdbad370cdf6afb8ab6504fee200c4a8a84d3a8)
- Added cross-compilation CI workflow for RISC-V extensions.
  ↳ No PR: [ff9d70b](https://github.com/openssl/openssl/commit/ff9d70b9ee3df2107299c8a40e5eada66bff9407)
- Removed temporary optimization reduction solution for old ppc64le compiler bug.
  ↳ No PR: [c658a60](https://github.com/openssl/openssl/commit/c658a60aae5b3ac5a22cc11ad59d687bafcc6fbf)
- Fixed YAML configuration for interoperability CI: corrected wrong field clients in exclusion list to servers.
  ↳ No PR: [5db7b99](https://github.com/openssl/openssl/commit/5db7b99914c9a13798e9d7783a02e68ae7e411d8)
- Updated provider compatibility CI configuration: added support for the 3.5 branch, removed the discontinued 3.1 branch, and fixed branch list regression.
  ↳ No PR: [725f55e](https://github.com/openssl/openssl/commit/725f55e235057c463feadabbb4d23450126117fd), [bf4c9b7](https://github.com/openssl/openssl/commit/bf4c9b7b663e03e81fe0291e03b814bafd409d1b)
- Updated the Rust toolchain in the CI configuration to the stable version, and added the necessary system dependency installation.
  ↳ No PR: [94b34ee](https://github.com/openssl/openssl/commit/94b34ee67af04f0b403bb0e22439e764475ffe6e)
- Added test matrix for OpenSSL 3.5 branch in Coveralls CI configuration.
  ↳ No PR: [b3955ea](https://github.com/openssl/openssl/commit/b3955eaa26f25fc43bdb6b2f299c89f685b5b7b6)
- Enabled --strict-warnings option by default in CI builds, and removed redundant -Wall and -Werror options.
  ↳ No PR: [dad4704](https://github.com/openssl/openssl/commit/dad4704a5dcfa28755822efd802476e4e06acde2), [d04ea9a](https://github.com/openssl/openssl/commit/d04ea9af7907934e49e37e77ea4cbcb1105f444e)
- Temporarily disabled gost-engine external tests to resolve build failures caused by cmake-4.0, and later re-enabled them.
  ↳ No PR: [db9771b](https://github.com/openssl/openssl/commit/db9771b5a056d939b6112cdc099fbf4f86d184ee), [1720760](https://github.com/openssl/openssl/commit/172076029c0bbb188e321f5832f6a15971834e90)
- Re-enabled pkcs11-provider external testing.
  ↳ No PR: [016d6de](https://github.com/openssl/openssl/commit/016d6deb850dc618f8ddd86911c3012f32976d61)
- Replaced the NASM installation method in Windows CI from ilammy/setup-nasm to installation via choco.
  ↳ No PR: [1ad1869](https://github.com/openssl/openssl/commit/1ad186986c8c90dfc58666531c0554641e022dbb)
- Added retry mechanism for apt commands in CI workflow for QUIC interoperability testing.
  ↳ No PR: [5810149](https://github.com/openssl/openssl/commit/5810149e6566564a790bd6d3279159528015f915)
- Fixed Docker installation in QUIC interoperability CI: updated docker-compose installation path and added installation and restart of Docker Engine 28.1.1.
  ↳ No PR: [a0d1af6](https://github.com/openssl/openssl/commit/a0d1af6574ae6a0e3872d20ff302a78793c05a85)
- Added RPKI client testing step to CI workflow.
  ↳ No PR: [f50e069](https://github.com/openssl/openssl/commit/f50e0694245634d9deeed9aaa41a5ff7cac064e9)
- Installed the libtls package in the CI workflow and replaced libretls with libtls-dev as a dependent package.
  ↳ No PR: [fa43c8c](https://github.com/openssl/openssl/commit/fa43c8c059d9a119e70ae9d1dbbecd68bd0b96a0), [eee2d06](https://github.com/openssl/openssl/commit/eee2d0610b72683c031dd3a765ddde203a8a202c)
- CI tasks for custom runners in forked repositories are skipped to avoid timeouts caused by unavailability of the runner.
  ↳ No PR: [a9cb68e](https://github.com/openssl/openssl/commit/a9cb68ee8faa6f303374303bfc48950abf05eda5)
- Added --strict-warnings option to Configure command for all Windows CI builds.
  ↳ No PR: [9f08f30](https://github.com/openssl/openssl/commit/9f08f30f1dd70225159602540016e83b4c6cbcf3)
- Added CI workflow to automatically run backport.
  ↳ No PR: [2b56a00](https://github.com/openssl/openssl/commit/2b56a00eb9d24a085db7f144414e5b8cc1794a87)
- Added CI workflow for checking Perl core module compatibility.
  ↳ No PR: [b89ab15](https://github.com/openssl/openssl/commit/b89ab15f133a37188c175d070c1de6188d705aa9)
- Limit LMS feature enablement to the master branch.
  ↳ No PR: [4337989](https://github.com/openssl/openssl/commit/4337989667b003bbf7ddc10984129d3cba298e8b)
- Updated container images in the OS Zoo CI workflow to the latest version.
  ↳ No PR: [a9a7e01](https://github.com/openssl/openssl/commit/a9a7e017b8cde8ea33918a63eec392b0f98979fe)
- Added the construction and testing of msquic-openssl container, and fixed related construction issues.
  ↳ No PR: [9665baf](https://github.com/openssl/openssl/commit/9665baf0f981d068a36350873450cf3d9d0217d7), [4a518ce](https://github.com/openssl/openssl/commit/4a518cebffec347226682b2c831ce2460ef444bb)
- Upgraded Windows CI runner to windows-2022 and updated Visual Studio paths.
  ↳ No PR: [d217b49](https://github.com/openssl/openssl/commit/d217b499948eff3fc5d05c669338bffa835f84c7)
- Enabled memory allocation failure testing and debugging options in CI.
  ↳ No PR: [3c3f0da](https://github.com/openssl/openssl/commit/3c3f0da9bdb504a8c6005fa52f815a9b243855b8), [22d7d1d](https://github.com/openssl/openssl/commit/22d7d1d7d0f8cfc3c6d8b890a4460bddc4887483)
- Swapping no-sm2 and no-ssl-trace options in CI configuration.
  ↳ No PR: [1a1c10f](https://github.com/openssl/openssl/commit/1a1c10f5d74c3ff69b698d9ef1cd0dbd6dc969fe)
- Added wget dependency for rpki-client external tests.
  ↳ No PR: [b5157f2](https://github.com/openssl/openssl/commit/b5157f29a928f61bf67e08d006fd39623c10fc39)
- Installed gpg tool for verifying packages in CI workflow.
  ↳ No PR: [001ce7c](https://github.com/openssl/openssl/commit/001ce7c281b0f9edffba114562c29162621256f5)
- Removed unnecessary Docker Compose patch step and git history depth setting from CI workflow.
  ↳ No PR: [1bbb0d7](https://github.com/openssl/openssl/commit/1bbb0d7b530ab86b83e207ae8ab84dac2692d065), [141ad51](https://github.com/openssl/openssl/commit/141ad51b46424cca5df825840ac02581eeaaddc5)
- Disabled SSL_TRACE_TEST to fix CI pipeline issues.
  ↳ No PR: [3dd0e25](https://github.com/openssl/openssl/commit/3dd0e254db8de7aa06b199fe62e68940ec05f2eb)

### Maintenance
- Added CODEOWNERS file, specifying the /.github/workflows/ directory is responsible for @quarckster.
  ↳ No PR: [b3187ab](https://github.com/openssl/openssl/commit/b3187ab5a757496e588ea9bdb7fabd12d194e66a)
- Improved the output of signature algorithm names in the s_client tool, prioritizing the use of IANA registered names and uniformly using the long name format to match X509_signature_print.
  ↳ No PR: [681528c](https://github.com/openssl/openssl/commit/681528cbc41278a7bdc662cdb1ab286e07170a90), [dc246ce](https://github.com/openssl/openssl/commit/dc246cec87793843d5a725abf2c89a6e134e7939)
- Add automatically generated files such as ciphercommon.c and cipher_chacha20_poly1305.c to .gitignore to avoid being tracked by errors.
  ↳ No PR: [6c3e111](https://github.com/openssl/openssl/commit/6c3e11101682ffc7ee2c36d0e1293de0e18181a4), [a1a08a4](https://github.com/openssl/openssl/commit/a1a08a4a254474b27041c998f16d113cff5e8eb1), [b622ae3](https://github.com/openssl/openssl/commit/b622ae3917b4e27885ce0a6f08be9f2bd7e3ae0d), [6474359](https://github.com/openssl/openssl/commit/64743597ecfc51940f3c91f3bf3bf6b78a0144db), [ff9fb92](https://github.com/openssl/openssl/commit/ff9fb929151902305d7948bc31fdb118ca6313b6), [bf5c21a](https://github.com/openssl/openssl/commit/bf5c21ae1614bd43aef95a1a64ef2bd18a86de4e), [bd9497f](https://github.com/openssl/openssl/commit/bd9497f527f5f6c982327d5516878f87e401ac7e), [431e85e](https://github.com/openssl/openssl/commit/431e85edeab452b7725630c1ff409afa2645c2cb), [fbb0a74](https://github.com/openssl/openssl/commit/fbb0a743739eb4e3c0b55086d18dbd5c99db1267), [1996a28](https://github.com/openssl/openssl/commit/1996a28f7f3b7d9a0a75287d8dfdf38cab5c3929), [4e18365](https://github.com/openssl/openssl/commit/4e183652cb4f9d2888b5d72a0fff0eb10a25a6f8)
- Fixed type mismatch warnings for multiple demos in Win64 builds.
  ↳ No PR: [8067e71](https://github.com/openssl/openssl/commit/8067e713a161adc18e47cf46bdaf9ced34bc63d0)
- Remove the template file that builds the global parameter name TRIE.
  ↳ No PR: [9d80e50](https://github.com/openssl/openssl/commit/9d80e50df5f700dcf7390c3701f69af72c0d0596)
- Removed third-party GitHub Actions and Cygwin from Windows CI jobs and used native commands instead.
  ↳ No PR: [d9044da](https://github.com/openssl/openssl/commit/d9044daf1eea8e1672820446e2955a52919fe934)
- Changed ANSI C checks in CI to C99 standard checks.
  ↳ No PR: [8571569](https://github.com/openssl/openssl/commit/857156910d85cbe55fe0bd01554c3da80e15a946)
- Replace dependency package libtls with libretls in CI workflow.
  ↳ No PR: [f92157d](https://github.com/openssl/openssl/commit/f92157d340d3104742785cd289b539fa3675e825)
- Add strlen. to the list of allowed symbols on Windows platforms.
  ↳ No PR: [c296e1c](https://github.com/openssl/openssl/commit/c296e1ce24d192d7ba52df4cd74eaec1a00ca7de)
- Delete the redundant compilation file pbkdf2_fips.c of pbkdf2.
  ↳ No PR: [c07da07](https://github.com/openssl/openssl/commit/c07da07ebb59deacc3ebb7a8b01c27723c97c204)
- Mark FIPS related parameters in DH key exchange implementation as only available in FIPS mode.
  ↳ No PR: [d01910a](https://github.com/openssl/openssl/commit/d01910a4f9afefc62d407d61938fecc86a0bb1f3)
- Add detailed error message and der_len bounds check in file_set_ctx_params().
  ↳ No PR: [9636f9a](https://github.com/openssl/openssl/commit/9636f9a43183f46204fc25e15722a691948513f8)
- Renamed parameter type from bool to flag to avoid conflict with C23 standard.
  ↳ No PR: [81ce3d3](https://github.com/openssl/openssl/commit/81ce3d3ae8f6c4021e0dce86891e869efa1710db)
- Remove unchecked conditions in storeutl command and fix indent_printf return value handling.
  ↳ No PR: [00480f1](https://github.com/openssl/openssl/commit/00480f1def86aab882f2bd4d15d2d03862009718)
- Add length bounds checking and explicit type conversion for multiple fuzz test functions in Win64 builds to eliminate compilation warnings.
  ↳ No PR: [c2482c6](https://github.com/openssl/openssl/commit/c2482c68e5ce21bc36287103e1b527ab329a8a3d)
- Fixed a large number of type mismatch warnings in Win64 builds, and unified the parameters and return values of mixed size_t and int.
  ↳ No PR: [a3af1c0](https://github.com/openssl/openssl/commit/a3af1c036cd25da58017d59a375f7de8ccbd9fd8)
- Always create and set an empty BIO during the configuration phase when using the QUIC TLS API to avoid repeated creation.
  ↳ No PR: [228a26f](https://github.com/openssl/openssl/commit/228a26fde43e63a46b0f4c16031d08c6a9dd04c7)
- Fixed the indentation of many goto labels to match the code style, and corrected some variable types and memory allocation functions.
  ↳ No PR: [60f2a71](https://github.com/openssl/openssl/commit/60f2a714002365256dba1c55bb4dd46802ea14d6)
- Fix unused function warnings on FreeBSD and NetBSD due to imprecise version checking.
  ↳ No PR: [0fe8784](https://github.com/openssl/openssl/commit/0fe8784131f786de8fa4a52fe559eae0c32903ca)
- Remove the obsolete ossl_param_find_pidx function declaration and adjust the way parameter name definition files are generated.
  ↳ No PR: [b747a48](https://github.com/openssl/openssl/commit/b747a48bb17e5e1cda594dd8fcbb8f7ca3bf4eaf)
- Add explicit length check in ctr_XOR function to eliminate GCC 14 compilation warning on s390x.
  ↳ No PR: [9a78828](https://github.com/openssl/openssl/commit/9a788281d91f698d6a229d588b9cb36987549669)
- Removed header file template param_names.h.in for parameter name definition.
  ↳ No PR: [ddf1f14](https://github.com/openssl/openssl/commit/ddf1f14105b437918ff68a67b017cff4d7e977dc)
- Added type conversion and length checking in engine and application code to eliminate Win64 compilation warnings.
  ↳ No PR: [a0fcbcb](https://github.com/openssl/openssl/commit/a0fcbcb282ca934bc2fb05059b65dc6ee74966ee), [c62cd07](https://github.com/openssl/openssl/commit/c62cd07d142574973646c17a177541446350a9e9)
- Updated .gitignore file to reflect changes to automatically generated files.
  ↳ No PR: [85cfd18](https://github.com/openssl/openssl/commit/85cfd18d1c96be8311bd07c99b2f873035ca928d), [91b7d04](https://github.com/openssl/openssl/commit/91b7d047073168c7f1489436795bba122797c5c0), [861eea4](https://github.com/openssl/openssl/commit/861eea4738111b6311ddc64fdafc4f1b4ac03248)
- Remove unnecessary parameters from algorithm implementation.
  ↳ No PR: [2d226c3](https://github.com/openssl/openssl/commit/2d226c389ce0e1809656d4c2c2af16a8799611ac), [7cd7592](https://github.com/openssl/openssl/commit/7cd75929f1690c48771cdf6423fdb9131748c398)
- Declare the ERR_str_libraries array as const, moving it to the read-only data section.
  ↳ No PR: [215167f](https://github.com/openssl/openssl/commit/215167fe7e42e0dca7ae5754a5600ecbcf0940ea)
- Remove redundant sizeof(char) multiplication in memory allocation expressions in the SSL module.
  ↳ No PR: [c4a91d5](https://github.com/openssl/openssl/commit/c4a91d5c26141a9bc786870ba9e58f59e3b23f96)
- Move the drbg_local.h header file location and update the reference path to support automatic file generation.
  ↳ No PR: [404da0b](https://github.com/openssl/openssl/commit/404da0b5e7904e2f33cd229c144a506b35640af4)
- Include additional error headers in skey management implementation.
  ↳ No PR: [8821d02](https://github.com/openssl/openssl/commit/8821d0205002a02052c16fd0d03bfd3167aa3c22)
- Fixed rsa_get_blinding to only perform the unlock operation when the lock is successfully acquired.
  ↳ No PR: [8601472](https://github.com/openssl/openssl/commit/860147225e92c6e927984427f61321a163dcd09c)

### Others
- Added ignore rules for ml_dsa_kmgmt.c and ml_kem_kmgmt.c in .gitignore.
  ↳ No PR: [0ecaf81](https://github.com/openssl/openssl/commit/0ecaf8191e638b00b6c2b95daf50704e4187cadc)
- Fixed the issue where the public key was not returned correctly when requesting the SLH-DSA public key.
  ↳ No PR: [c1ab573](https://github.com/openssl/openssl/commit/c1ab5734ab504b500ef2f00b0f268496ef3a7bf5)
- Update prime command, use BIO_get_line() to read files line by line, support multiple prime numbers per line and increase buffer size.
  ↳ No PR: [d6dc0f1](https://github.com/openssl/openssl/commit/d6dc0f1cacd4a21a0de5b58d0ec4139629c66b7a)
- Added configutl tool for dumping configuration file contents.
  ↳ No PR: [78ca45c](https://github.com/openssl/openssl/commit/78ca45cef0971394522848f49ae397aad5f9e55d)
- Added -multi option to x509 command to support outputting all found certificates from input.
  ↳ No PR: [dca67c0](https://github.com/openssl/openssl/commit/dca67c0aa17010f2315bc5bf1915ad4509ff8e52)
- Adjusted the format of the memory release call in the aes_freectx function.
  ↳ No PR: [8863964](https://github.com/openssl/openssl/commit/886396462dd55c1085cf3337c4bef0a76157bc1f)
- Fixed code style issues in test/quicapitest.c.
  ↳ No PR: [ba46275](https://github.com/openssl/openssl/commit/ba46275556ae93e44f27fece2d25655b42ce2842)
- Removed an unused variable assignment in cms_pwri.c.
  ↳ No PR: [cb3fde9](https://github.com/openssl/openssl/commit/cb3fde9728b9deed1ab2fb37dbe1021a471066e0)
- Replaced indented tabs with spaces in C source files and header files, and adjusted code formatting.
  ↳ No PR: [eea6315](https://github.com/openssl/openssl/commit/eea6315408827ed5b490935022b314973383950e)
- Updated .gitignore rules to ignore generated cpuid assembly files under all architectures.
  ↳ No PR: [dfaea0a](https://github.com/openssl/openssl/commit/dfaea0aa4bd789dd7e51d94643f403afb0dd532a)
- Added Software Bill of Materials (SBOM) template files in CycloneDX format.
  ↳ No PR: [6545de9](https://github.com/openssl/openssl/commit/6545de9bbe44145b4c35f12d6e4dad1f3df5f0cf)
- Removed reference to VxWorks platform, which is no longer supported.
  ↳ No PR: [3f98e94](https://github.com/openssl/openssl/commit/3f98e949d3eb829dfa0a10a6ac9a035877c71708)
- Move crypto/bn/README.pod to doc/internal/man3/bn_mul_words.pod as an internal man page and remove obsolete information.
  ↳ No PR: [78b1fdf](https://github.com/openssl/openssl/commit/78b1fdf4a101ae4909038e90b2c3c961be5a7064)
- Adjusted the msquic interop test configuration in CI to exclude retry tests and re-add the Chrome client.
  ↳ No PR: [2fb4cfe](https://github.com/openssl/openssl/commit/2fb4cfe143daa4644cf10b9f1ed3cdd940c5e1f8)
- Added placeholder entries in CHANGES.md and NEWS.md for OpenSSL 3.6 versions.
  ↳ [#27038](https://github.com/openssl/openssl/pull/27038): [b276276](https://github.com/openssl/openssl/commit/b2762763e9015e778eff0d303a38f0b6082c8591)
- Updated broken links and expired email addresses in the source code, and cleaned up related comments.
  ↳ No PR: [4943ac7](https://github.com/openssl/openssl/commit/4943ac7b88dc9004ec24510bf5f8f3a75f5f71f0)
- Fixed C++ style comments in ec code and Windows builds, changed to C style to resolve compilation issues.
  ↳ No PR: [ea77608](https://github.com/openssl/openssl/commit/ea77608920e88812a5278be351e3ebbfdb81d992), [b886059](https://github.com/openssl/openssl/commit/b8860598d2f7eab14fcf63c22579d879615465c8)
- Removed redundant NULL check for key in xor_freekey function in test/tls-provider.c.
  ↳ No PR: [511cfac](https://github.com/openssl/openssl/commit/511cfacf8c15737a63e944b8faf044dea7505263)
- Reduced the dependency scope of pkcs11-provider external testing to only use tools such as kryoptic and opensc.
  ↳ No PR: [edd3f47](https://github.com/openssl/openssl/commit/edd3f47fd76e50b96685b95bb9a63e6e23e51348)
- Fixed typo in test data file evpciph_des3_common.txt.
  ↳ No PR: [29464b4](https://github.com/openssl/openssl/commit/29464b4c15db4c4063633743254986a91b91dd33)
- Updated comments to explicitly reference the ossl_quic_stream_has_recv_buffer() and ossl_quic_stream_has_send_buffer() functions.
  ↳ No PR: [e8df1d1](https://github.com/openssl/openssl/commit/e8df1d12455939d01e21b4650a966e4eb7549436)
- Adjusted comments in check-format-test-positives.c to reflect line length threshold changes, and optimized related comment descriptions.
  ↳ No PR: [e6476de](https://github.com/openssl/openssl/commit/e6476de58d8e3440e3585843fd9ee62dd187f957), [58eb089](https://github.com/openssl/openssl/commit/58eb08985c485bf2fe010fb59c13ad0df2e0faa3)
- Fixed typo in demos/guide/tls-client-block.c.
  ↳ No PR: [10bd6fa](https://github.com/openssl/openssl/commit/10bd6fa8ca93b4cf53f005f110c827ed923c89a4)
- Updated reference to obsolete RFC 2459 in code comments to correct RFC 3370.
  ↳ No PR: [7c6d9da](https://github.com/openssl/openssl/commit/7c6d9da45f3a3b3a247d647f497e46c1e5f3d285)
- Fixed URL of NIST ACVP server in SLH-DSA test file, updated FIPS204 to FIPS205.
  ↳ No PR: [07c7728](https://github.com/openssl/openssl/commit/07c772847de682412448daea07582f566d30f7ac)
- Adjust the default behavior of check-format.pl, no longer report "{ 1 stmt }" warning for else if branch.
  ↳ No PR: [f21a839](https://github.com/openssl/openssl/commit/f21a8391dd0ec3a0dbdc5dc5fa8b44a0b07abf6d)
- Renamed multiple parameter list variable names from _ettable to _list.
  ↳ No PR: [effba0e](https://github.com/openssl/openssl/commit/effba0ee654f9f2edbd62de92d43b569e7ea4a72)
- Updated .gitignore to ignore generated files for HKDF, KBKDF, SSKDF, SSH KDF and PVK KDF.
  ↳ No PR: [575fcf5](https://github.com/openssl/openssl/commit/575fcf5bae1e335ae9df2739f7c760bf969cd9d5), [b00941c](https://github.com/openssl/openssl/commit/b00941ceb1a3d5b127106cac8473a9ef54cfd41b), [0c5bb0f](https://github.com/openssl/openssl/commit/0c5bb0feff4cd86352bf184cd55d0dc67d99938c), [290173c](https://github.com/openssl/openssl/commit/290173caa4d3d4d3d6f147e8e6853568b451cfca)
- Updated .gitignore to ignore generated and renamed files.
  ↳ No PR: [a4bd3d1](https://github.com/openssl/openssl/commit/a4bd3d171974b399d398d9239311e5cf9abcaf50), [4761aea](https://github.com/openssl/openssl/commit/4761aea3fe15c5eea6caea0da723f6d357742b9c), [3af4c99](https://github.com/openssl/openssl/commit/3af4c99cd458ff453afc11878faa19e10bdd0757), [dbe9a68](https://github.com/openssl/openssl/commit/dbe9a6825f1e0316806cff93875a830b896e97d6), [6928f97](https://github.com/openssl/openssl/commit/6928f97b7c17dba12dd79a1b28e643177c93979e), [b7c3a0c](https://github.com/openssl/openssl/commit/b7c3a0c3fc82d007f54396dc505dcad6b7f5f2c3), [9edc474](https://github.com/openssl/openssl/commit/9edc4746767e3c3164134bbcf996f355bd3a9c67), [ef77afe](https://github.com/openssl/openssl/commit/ef77afe58be015d294926aa95fc9f4a99d2efa22), [851b0c8](https://github.com/openssl/openssl/commit/851b0c886809fea3a5d1a2545c47df882807778b)
- Fixed comment errors in QUIC ACK module, including brackets, spelling and citations.
  ↳ No PR: [4a3c954](https://github.com/openssl/openssl/commit/4a3c954a0cdb9fa1f511ce43bb4833303a6067e2), [b083613](https://github.com/openssl/openssl/commit/b0836134764817fb8b20ceb432d8dff4fd58c2aa), [a43b926](https://github.com/openssl/openssl/commit/a43b926fd2c73349c9eb6167f08a4d435e6f04a6)
- Fixed English syntax errors in endian.h header file comments.
  ↳ No PR: [5286b17](https://github.com/openssl/openssl/commit/5286b175adbea96c6aeef718867ef50d70232cdf)
- Fixed variable type typo, correct stack_info to stack_traces.
  ↳ No PR: [bd0b53a](https://github.com/openssl/openssl/commit/bd0b53a32c213d45b5c12eef06200a241fb609be)
- Fixed typos and formatting issues in multiple documents.
  ↳ No PR: [084a627](https://github.com/openssl/openssl/commit/084a62734702caadbaf0507d580201bcb3486eaf), [0b091c8](https://github.com/openssl/openssl/commit/0b091c88d7d50c542ee393ed31ef5a1b92eea476), [9968040](https://github.com/openssl/openssl/commit/996804019490c9d5a2ed2bd188860fd7d6940676)
- Fixed help text order for -genstr option in asn1parse command.
  ↳ No PR: [eac588a](https://github.com/openssl/openssl/commit/eac588ac360ca16e0f9979b6c70708f1e8991b4f)
- Updated copyright year of multiple source files to 2025.
  ↳ No PR: [e663324](https://github.com/openssl/openssl/commit/e66332418f84144478df43df91cf4cedf412fc85)
- Update version date and status in CHANGES.md and NEWS.md for OpenSSL 3.6 alpha1 version.
  ↳ No PR: [eccb480](https://github.com/openssl/openssl/commit/eccb480c11c0220ab39acc3b06923979a7df1a9f)
- Update version titles in CHANGES.md and NEWS.md for 3.6 alpha2 version.
  ↳ No PR: [a3e30b8](https://github.com/openssl/openssl/commit/a3e30b835437dab57e5a602d76205c43af20179c)
- Clean up the format of CHANGES.md and NEWS.md, and wrap API names and terms in backticks.
  ↳ No PR: [fe92375](https://github.com/openssl/openssl/commit/fe923758ffa7dd7aa0deffa8278f3ad3cbdec517)
- Fixed typo in incorrectly referenced field in error message.
  ↳ No PR: [2be1b40](https://github.com/openssl/openssl/commit/2be1b400e77ef4ce57f14b9fa15e4afe18d0a7fd)
- Updated copyright year of multiple source files to 2025.
  ↳ No PR: [681e563](https://github.com/openssl/openssl/commit/681e5631f7556b35274a48d5562490aa93272472), [5de8d3e](https://github.com/openssl/openssl/commit/5de8d3eb6d4643c8ef6300cc87e9788ae2b1e91a)
- Update version numbers and release dates in CHANGES.md and NEWS.md for the release of OpenSSL 3.6.0.
  ↳ No PR: [7b371d8](https://github.com/openssl/openssl/commit/7b371d80d959ec9ab4139d09d78e83c090de9779)
