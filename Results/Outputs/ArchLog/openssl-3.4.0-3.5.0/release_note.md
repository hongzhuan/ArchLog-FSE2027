# Release Note

## Important Changes

### Platform Abstraction Layer
- Added QUIC object basic types and QUIC Domain SSL object definitions, including object initialization, engine/port/SSL object acquisition, blocking mode support and other core functions, providing infrastructure for QUIC support. (Architecture event: SslProtocolStack module adds QUIC support)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [1137f3f](https://github.com/openssl/openssl/commit/1137f3f9ae82e6ac84c96012228fae853b55f770), [9077598](https://github.com/openssl/openssl/commit/907759818e9263b4227d426be983d2bad2d6f50a)
- Reconstruct the QUIC context (QCTX) to support listener and domain type SSL objects, add new APIs to obtain listener and domain, and migrate the locking mechanism from the channel level to the domain level. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [3a9cedc](https://github.com/openssl/openssl/commit/3a9cedc20fe6ce58c6fb1020b090509586a2ae92)
- Centralized time coverage processing from QUIC connections to QUIC engine, and unified interface settings. Time coverage can now be set on any QUIC SSL object. (Architecture-related: external behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [ac69d06](https://github.com/openssl/openssl/commit/ac69d0649a4cb92b79efd1b7ae8eda413468ef9d)
- Before creating a QUIC channel, the port first creates a QRX object to perform AEAD verification on the initial data packet. After the verification passes, the channel is created and the pre-created QRX is passed to the channel constructor. (Architecture-related: external behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [c82c1db](https://github.com/openssl/openssl/commit/c82c1dbbbbb9c8c152bbd7ec61930f3f245b98e1)
- On s390x platforms, delay encryption card detection until the first exponentiation or CRT operation, and improve error handling. (Architecture-related: platform compatibility)
  ↳ No PR: [f928304](https://github.com/openssl/openssl/commit/f928304a9db3772a6047462599384fb57d878ccb)
- Enable AES and SHA3 optimization for Apple Silicon M4 systems. (Architecture-related: Platform compatibility)
  ↳ No PR: [ea58178](https://github.com/openssl/openssl/commit/ea5817854cf67b89c874101f209f06ae016fd333)
- Added QUIC listener SSL object type and complete API, including creation, accepting connections, getting queue length, monitoring, blocking connection acceptance, discarding pending connections, getting listener objects, etc. (Architecture event: QUIC listener API new)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [e0ffd21](https://github.com/openssl/openssl/commit/e0ffd21e22182bbf3d13c2d61efbb9cda5261a5e), [b67be72](https://github.com/openssl/openssl/commit/b67be72a5d9da5064f542632a11861e779c38d38), [a68287a](https://github.com/openssl/openssl/commit/a68287adeba990be0fd07ec3d4be0635a918043a), [15f9df4](https://github.com/openssl/openssl/commit/15f9df40ff32f40681f38d73ddbdf0ccd83b1e94), [56b59e7](https://github.com/openssl/openssl/commit/56b59e78376dfd43e6bdc052cfc1f9c422257669), [e3ba554](https://github.com/openssl/openssl/commit/e3ba554d7351a05ee6338e1d60d0b0bebeadb60c), [99e4a1e](https://github.com/openssl/openssl/commit/99e4a1e3ce4713d8cc373de949e93490f3f39865), [1e73a3c](https://github.com/openssl/openssl/commit/1e73a3ca9f244d97fbc091265321f3627f9e033f), [87d4746](https://github.com/openssl/openssl/commit/87d474660c5d1d468e09551c94cffa60c8c7c8ee), [68537fc](https://github.com/openssl/openssl/commit/68537fceaede9ec242db5a5f8799c33c985a37c8)
- Added QUIC Domain SSL objects and related APIs, including creating, releasing, obtaining domain objects, creating connections from listeners, and supporting configuring domain flags through SSL_CTX_set_domain_flags. (Architecture event: QUIC Domain API new)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f75b3d1](https://github.com/openssl/openssl/commit/f75b3d1db6d5d7eef347c19f3597692a8a20b7b9), [50c7796](https://github.com/openssl/openssl/commit/50c779626757070653ceda70b7f18caa8257c989), [8110737](https://github.com/openssl/openssl/commit/8110737e42149e8fec74d248d9a9b323118a38e4), [db59092](https://github.com/openssl/openssl/commit/db590923c140da82f06b5fa88925ff8ff493ca01)
- Add the operating system notifier (OS notifier) function to the RIO subsystem, and improve socket error handling and resource cleanup under the Windows platform. (Architecture event: RIO notifier is added)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [14516cd](https://github.com/openssl/openssl/commit/14516cd5a4f9464df1accafd40d6825449c34a05)
- Added QUIC blocking operation support: The reactor layer adds external registration blocking operation functions (entering/leaving the blocking area), and the application layer adds obtaining the notifier file descriptor and blocking area API. (Architecture event: QUIC blocking operation support)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [5d3720d](https://github.com/openssl/openssl/commit/5d3720dcb6d281238e7376a92ee4d6cac44d31f9), [643d149](https://github.com/openssl/openssl/commit/643d1496966cf044def833d1528e7b27542a3cda), [7f2adb8](https://github.com/openssl/openssl/commit/7f2adb82b1ec465fd4a754fc5a04f368a7e8bbd2)
- Modify SSL_poll to support blocking QUIC objects, and add QUIC polling translation and cleanup functions. (Architecture event: SSL_poll supports QUIC blocking)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [67df6bd](https://github.com/openssl/openssl/commit/67df6bd9362b96072b853ec8e62103028ecbb55f)
- Add blocking mode support for QUIC objects, and add null pointer checking to enhance robustness. (Architecture event: QUIC object blocking mode)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [8b4b504](https://github.com/openssl/openssl/commit/8b4b5048ee06a7e4b10be5b888de493ea72d4814)
- Added poll builder module and QUIC polling mechanism, supporting immediate mode polling API and third-party QUIC stack reuse TLS implementation. (Architecture event: SslProtocolStack module change)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [caa3446](https://github.com/openssl/openssl/commit/caa3446eef277318fa465c3f6c2dc2b575995d74), [f2fff14](https://github.com/openssl/openssl/commit/f2fff144d722d80af640ed2ef4ca9119cc35f459) | No PR: [3cf1555](https://github.com/openssl/openssl/commit/3cf15554f290a3c004d36dfdb16b66619395615d), [198e5a8](https://github.com/openssl/openssl/commit/198e5a847ad3914ea90df15bc20f9d7e839b736a)
- Implement the QUIC server address verification function based on the retry package, including sending the retry package, generating verification tokens, binding new connections, and updating the channel creation logic to support the retry package. (Architecture event: SslProtocolStack module change (QUIC))
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [6ba0457](https://github.com/openssl/openssl/commit/6ba0457c926e19928d39e4800d7f929bc86f525f), [6654f8b](https://github.com/openssl/openssl/commit/6654f8bb42fc3b936c495732545b8ac8a3679e69), [e814831](https://github.com/openssl/openssl/commit/e8148315ca6d44157afc882460e17cc9d9c3ffe2)
- Added public flag SSL_LISTENER_FLAG_NO_VALIDATE for QUIC listener, allowing address verification to be skipped. (Architecture event: OpenSSL_Core_Headers module change)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [60762be](https://github.com/openssl/openssl/commit/60762be09bbe05683cd24aabd0d0551900b99428), [78f7141](https://github.com/openssl/openssl/commit/78f7141c12d58f0cbf9dde193b23857023700146)
- Added sslkeylog configuration option, which is disabled by default. When enabled, key logs are recorded according to the SSLKEYLOGFILE environment variable. (Architecture-related: configuration interface)
  ↳ No PR: [4a69a6d](https://github.com/openssl/openssl/commit/4a69a6d171cafe4b3dee81215f0640fc42a8aff9), [8458f87](https://github.com/openssl/openssl/commit/8458f873a082654ecab1bf6dea495398233f5d02), [825bb7f](https://github.com/openssl/openssl/commit/825bb7f4bdd05dbf2983d4d190eb9b220924d373), [43ba601](https://github.com/openssl/openssl/commit/43ba601723ecd10ecc598091b4d72469767eb5f4)
- Extend OPENSSL_ia32cap to support more CPUID bits, and increase environment variable buffer size. (Architecture-related: Platform compatibility)
  ↳ No PR: [acc2655](https://github.com/openssl/openssl/commit/acc26552369bb39de6d30737fc30a6bc4f2ebbae)
- Added __isoc23_strtol symbol in symbol export file. (Architecture-related: platform compatibility)
  ↳ No PR: [ada0265](https://github.com/openssl/openssl/commit/ada0265aab7f6e24547d6fb2b1035e2dfd5a4cff)
- Fixed the symbol usage problem in RIO notifier, using platform-related socket read and write functions instead. (Architecture-related: platform compatibility)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [9c1bd44](https://github.com/openssl/openssl/commit/9c1bd44f1d68b5673b94d0788aed0dfa34c7959d)
- On Windows platforms, added necessary type conversions for the use of socketpair and WSASocketA, and fixed parameter type mismatch in setsockopt calls. (Architecture-related: Platform compatibility)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [269409c](https://github.com/openssl/openssl/commit/269409c75bd7bb3f02333ff3e6d227311750df40)
- Added conditional compilation check for QNX systems to avoid using ipi_spec_dst field in in_pktinfo structure. (Architecture-related: platform compatibility)
  ↳ No PR: [4450171](https://github.com/openssl/openssl/commit/445017152b6806b6b02235f72244150115c08cee)
- Added getsockname call and error handling in notifier initialization on Windows platform. (Architecture-related: platform compatibility)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [54fd5e1](https://github.com/openssl/openssl/commit/54fd5e113b57df1e05516b72a434af9f5d56881a)
- Fixed the InterlockedExchangeAdd parameter type conversion error in the Windows thread code, changing the incorrect long * and long to the correct LONG * and LONG to ensure the correctness of atomic operations under cross-platform. (Architecture-related: platform compatibility)
  ↳ No PR: [71ae466](https://github.com/openssl/openssl/commit/71ae46618108a095e6e10a875a59afb526548d3b)
- Fixed an issue where the default port of OSSL_HTTP_open() was not set correctly under IPv6 host address. (Architecture-related: public API)
  ↳ No PR: [1c90d36](https://github.com/openssl/openssl/commit/1c90d36ab1fbfccd584aa82d879f26881e25b023)
- Correct the implementation of the maximum number of response header lines function, adjust the function declaration position and clean up the debugging tracking code. (Architecture-related: public API)
  ↳ No PR: [91114d5](https://github.com/openssl/openssl/commit/91114d53b02b684e07cf0671ec88be78f398dd00)
- Fix OSSL_trace_begin function: return NULL when the corresponding trace category is not enabled, to correctly follow the setting of disabled categories. (Architecture-related: public API)
  ↳ No PR: [72d3e9b](https://github.com/openssl/openssl/commit/72d3e9bac41302e5bc00db1bef014b0ca810d2cf)
- When an application provides custom memory allocation functions through CRYPTO_set_mem_functions, posix_memalign or aligned_alloc is no longer used, but instead a custom malloc is used and the memory is manually aligned. (Architecture-related: public API)
  ↳ No PR: [50e9d2b](https://github.com/openssl/openssl/commit/50e9d2b188b8dce070f388640c06a7dc04417390)
- Fix the blocking behavior of SSL_poll when there are no poll items: if the timeout is specified, sleep and wait. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [6cb1b4e](https://github.com/openssl/openssl/commit/6cb1b4e89eb29a90c7a98575abe27d86d29c44bd)
- Fixed a memory leak in OSSL_HPKE_CTX_new caused by incorrect paths not releasing duplicate strings. (Architecture-related: public API memory leak repair)
  ↳ No PR: [8ff6edb](https://github.com/openssl/openssl/commit/8ff6edb9da6199b130bfb50bc27b2e58cc815932)
- Fixed the memory leak in BIO_get_accept_socket caused by the failure of BIO_parse_hostserv, ensuring that the allocated host name and service name memory is correctly released when parsing fails. (Architecture-related: public API memory leak repair)
  ↳ No PR: [3247695](https://github.com/openssl/openssl/commit/32476957ead4151dceaf873306fc7e79cd262812)
- Fixed the error alarm type in certificate compression processing, changed the unsupported compression algorithm error to an illegal parameter alarm, and added a check that the decompression length is zero. (Architecture-related: SSL certificate compression behavior)
  ↳ No PR: [a590a7e](https://github.com/openssl/openssl/commit/a590a7e3bc9229ba49f6e8828f85baaaf024607d)
- Fixed the problem of the callback function using the wrong SSL object in the QUIC scenario, ensuring that the user-visible SSL object passed in the callback is not the internal SSL object only used for QUIC. (Architecture-related: QUIC callback behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a477b4e](https://github.com/openssl/openssl/commit/a477b4ec168f04ac0df315d122c436b39dd3c4ca) | No PR: [dc84829](https://github.com/openssl/openssl/commit/dc84829cc5a905cd402979d8c64791f7277a39e6)
- Fixed the problem of incorrect ORIG_DCID parameter selection when the QUIC server sends Server Hello in the retry scenario, ensuring that the correct original connection ID is used. (Architecture-related: QUIC connection ID behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [1c6e1e1](https://github.com/openssl/openssl/commit/1c6e1e1c9cfe0e45d0c467714772d8c5567b9e9e)
- Fixed the problem of falsely reporting no cipher match error when the QUIC object calls the cipher list setting function. Now the error is only reported when the method supports passwords and has no TLSv1.2 cipher. (Architecture-related: public API)
  ↳ No PR: [40237bf](https://github.com/openssl/openssl/commit/40237bf97aeb855856e7b74ed393e1767631e1a2)
- Fixed the problem that SSL_write_ex and SSL_write_ex2 may repeatedly transmit data on blocking QUIC streams, and corrected the recording logic of the number of written bytes. (Architecture-related: QUIC writing behavior)
  ↳ No PR: [2de7e1d](https://github.com/openssl/openssl/commit/2de7e1d69851a363cadd9d6bdd95302b89a4383b)
- Fixed the variable name error in the CRYPTO_atomic_store function in the Solaris build, and corrected the use of the atomic memory ordering macro in the CRYPTO_atomic_load function. (Architecture-related: Platform compatibility: Solaris atomic operations)
  ↳ No PR: [4c04a19](https://github.com/openssl/openssl/commit/4c04a19860d1a6cfaa234463cc0b8e28740d9acb)
- Fixed the problem of callback function signature mismatch in the evp_generic_fetch series of functions, and solved the alarm reported by UBSan. (Architecture-related: public API)
  ↳ No PR: [3ffa64c](https://github.com/openssl/openssl/commit/3ffa64cd4566cb2d14f6b871e02460f54e1d4da1)
- Fixed the problem that when the library context is not initialized, ossl_lib_ctx_get_concrete() returns NULL, causing related locking and random number generation functions to possibly crash. Now a null pointer check has been added. (Architecture-related: public API)
  ↳ No PR: [dfce0d7](https://github.com/openssl/openssl/commit/dfce0d7418d6d5b54d74fa80fc50392f00270c53)
- Fixed the problem of incorrect use of OPENSSL_HTTP_PROXY and OPENSSL_HTTPS_PROXY environment variables in the proxy adaptation function. The corresponding proxy variables will now be read correctly depending on whether SSL is used. (Architecture-related: public API)
  ↳ No PR: [6a2472f](https://github.com/openssl/openssl/commit/6a2472fb3e958c029989286d9272bd2b23738f85)
- Fixed issues with error status handling in the OSSL_HTTP_REQ_CTX_nbio() state machine, non-fatal HTTP status code return content, and HTTP redirection space-time string checking. (Architecture-related: public API)
  ↳ No PR: [c8932aa](https://github.com/openssl/openssl/commit/c8932aa94f8600cc6b11df1784f53e3ca6c2bdcc), [64b4784](https://github.com/openssl/openssl/commit/64b478419aeff9e4771a5ac9640715da3d70eba9), [6de09eb](https://github.com/openssl/openssl/commit/6de09ebe13b99bc9f97e8616a10b121ee99d36c3)
- Added a pending count check during QUIC connection cleanup to prevent the port from being released when there are still pending operations, thereby avoiding use after free. (Architecture-related: QUIC protocol implementation)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [56b6ab0](https://github.com/openssl/openssl/commit/56b6ab094ee7353e86ce13793ce44d3ed5d87cc8)
- Fixed an issue where QUIC could send a NEW_TOKEN frame prematurely before the handshake is complete, now only dispatches the frame and lifts the amplification limit after the handshake is completed. (Architecture-related: QUIC protocol behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [647fdf6](https://github.com/openssl/openssl/commit/647fdf65c9ab20886fdd01040bc4ab2afa4ac68f)
- Removed inclusion of poll.h header file to avoid compilation errors on NonStop platforms. (Architecture-related: Platform compatibility)
  ↳ No PR: [dbb5c73](https://github.com/openssl/openssl/commit/dbb5c73f90ba0956fdc69e503f7b05db879eaf77)
- In order to be compatible with old compilers that do not support __ATOMIC_ACQ_REL, the RCU callback chain list operation was changed from atomic exchange to mutex protection, and the synchronization order was adjusted. (Architecture-related: platform compatibility)
  ↳ No PR: [7d28456](https://github.com/openssl/openssl/commit/7d284560a0624206356d46a948ab3a0b6f670c0e)
- Made signature algorithm name matching case-insensitive, and fixed the logic in related functions. (Architecture-related: public API)
  ↳ No PR: [d5a4665](https://github.com/openssl/openssl/commit/d5a4665a21eb6974872e67b2257b6429d7cdf84a)
- Changed the warning type of zero-length cipher suite list from illegal_parameter to decode_error to comply with RFC 8446 specification. (Architecture-related: external behavior)
  ↳ No PR: [2ce46ad](https://github.com/openssl/openssl/commit/2ce46ad8cef8909ae9162a429daf8e3d5fc8cb03)
- Changed keyshare order checking from fatal errors to only logging trace messages to improve compatibility with some clients. (Architecture-related: external behavior)
  ↳ No PR: [84694d2](https://github.com/openssl/openssl/commit/84694d2baa964abcd4f3d57a2a85a8369743476c)
- Fixed the issue where the EVP_PKEY_derive_set_peer_ex function incorrectly releases the peer key when an error occurs, and restores the original behavior: no longer releases and clears the peer key after the control operation fails. (Architecture-related: public API)
  ↳ No PR: [b4fab70](https://github.com/openssl/openssl/commit/b4fab70bfb6829e4904120769b8e24a99a91cc43)
- Change "No valid group" from error to allowed, fix the processing logic when the group list is empty or just blank, and optimize the memory allocation and reference count check in SSL connection initialization. (Architecture-related: external behavior)
  ↳ No PR: [a3143c2](https://github.com/openssl/openssl/commit/a3143c24009ab7336d7e477cfb3bc862f50f14d8)
- Fix Windows atomic operation support, add lock protection fallback implementation for CRYPTO_atomic_add when InterlockedExchangeAdd64 is missing. (Architecture-related: Platform compatibility)
  ↳ No PR: [bcb8eae](https://github.com/openssl/openssl/commit/bcb8eae1afe243a7c514b988289b06b838764fb6)
- Fixed the problem of writing unallocated memory due to zero bytes generated by filling the equal sign when decoding EVP_DecodeUpdate. Control the filling processing by adding the eof parameter, and update related documents and tests. (Architecture-related: public API)
  ↳ No PR: [f86acc9](https://github.com/openssl/openssl/commit/f86acc9434e3b1ff8bc11bac6210dbef25cbb4b1)
- Fixed compilation failure on AIX 7.1 due to conflict between system macro definition and variable name in code. (Architecture-related: platform compatibility)
  ↳ No PR: [5eb55ad](https://github.com/openssl/openssl/commit/5eb55ad8a70ef948432ba17e0985c7b4d3b13c25)
- Fixed an issue where libctx was not passed correctly in CMS password receiver information operations, ensuring that key derivation and password initialization use the correct library context. (Architecture-related: public API)
  ↳ No PR: [5045712](https://github.com/openssl/openssl/commit/5045712d3dbe6abdfffcb4f518c67409ec85535e)
- Fixed a build error on Windows XP caused by the socket handle non-inheritable flag, which falls back to a call without this flag when the WSASocketA call fails. (Architecture-related: platform compatibility)
  ↳ No PR: [c0251d7](https://github.com/openssl/openssl/commit/c0251d7b0fb835c6f043fa389b448d0d880d60a7)
- Fixed the problem of incorrectly entering the legacy code path when EVP_PKEY_CTX is associated with keymgmt. (Architecture-related: public API)
  ↳ No PR: [ac20f5c](https://github.com/openssl/openssl/commit/ac20f5c90c8d46a9ea72802e6c44ae6f6957b616)
- Adjust the resource release order in SSL_free and ossl_ssl_connection_free to ensure that SSL_get_app_data() is still available during QUIC TLS callback. (Architecture-related: public API)
  ↳ No PR: [d8ce455](https://github.com/openssl/openssl/commit/d8ce455a3d4b0be1199f34e41fdac6ef3c96b9c9), [948c776](https://github.com/openssl/openssl/commit/948c776ba7abf314de0f5d91bcfcdf4cc217d59d), [a9b8783](https://github.com/openssl/openssl/commit/a9b87830c9bce12be9a6f3fc8b097d335fe15502)
- Fixed the problem that the server-side handshake read key switching timing is too late in the QUIC 0-RTT scenario to avoid the application layer needing to call SSL_do_handshake() to obtain the key. (Architecture-related: public API)
  ↳ No PR: [fb55383](https://github.com/openssl/openssl/commit/fb55383c65bb47eef3bf5f73be5a0ad41d81bb3f)
- Fix signature algorithm edge case: allow RSA PSS certificate signing with the same digest, and avoid sending TLS 1.3 signature algorithm to TLS 1.2 clients. (Architecture-related: public API)
  ↳ No PR: [a7f3550](https://github.com/openssl/openssl/commit/a7f35508551dc2c3f77f59fd31cbb03da41f2b20)
- Fixed the behavior of SSL_new() when using the QUIC server method, and added a new test case to verify the correctness in this scenario. (Architecture-related: public API)
  ↳ No PR: [88ecf93](https://github.com/openssl/openssl/commit/88ecf93695b989c648a1ebed1db31f968c1d060c)
- Fixed the problem of OSSL_PARAM set function returning non-zero result size in error conditions. (Architecture-related: public API)
  ↳ No PR: [1dafff0](https://github.com/openssl/openssl/commit/1dafff06ca6a3c263e5e6222b92c6fbdbf31b8fe)
- Refactor the SSL keylog function, use BIO_up_ref and callback mechanism to manage reference counting, and return an error in SSL_CTX_new_ex when the keylog file setting fails; also updated the relevant function names and comments. (Architecture-related: public API)
  ↳ No PR: [3992add](https://github.com/openssl/openssl/commit/3992add1b712a470b733a57e4567a6348708c91b), [5b29c71](https://github.com/openssl/openssl/commit/5b29c71aa4083ad48fb9f1b10ef10429e8cf0392)
- Separated Windows Sockets related header files from e_os.h to dedicated header file e_winsock.h. (Architecture-related: platform compatibility)
  ↳ No PR: [b2ac9c7](https://github.com/openssl/openssl/commit/b2ac9c714e177950488e263a4a52b2b36abfdbd8)
- On systems that support poll, change the implementation of BIO_socket_wait from select to poll. (Architecture-related: platform compatibility)
  ↳ No PR: [38e8392](https://github.com/openssl/openssl/commit/38e8392ba0c8dcd975de47a3119d0051cf5e44a1)
- Reduce the required minimum number of queues from 3 to 2 in the RCU implementation, remove the default writer initialization logic, and lower the atomic load barrier level for read indexes. (Architecture-related: RCU implementation changes)
  ↳ No PR: [126d320](https://github.com/openssl/openssl/commit/126d3209b3934b9973a3ff786d9702418278cc8d)
- Add atoi to the Unix platform symbol list to resolve errors in the compilation check script. (Architecture-related: platform compatibility)
  ↳ No PR: [116c0ad](https://github.com/openssl/openssl/commit/116c0ad9520b0dff42b4683b704aa8264d8d3331)
- Added API to support the 0-RTT function of the third-party QUIC stack, including setting the interface for early data enablement. (Architecture event: SSL protocol stack QUIC support)
  ↳ No PR: [db2c54c](https://github.com/openssl/openssl/commit/db2c54cc9233dad8178fa750d369d4037a945d7d)

### Cryptographic Algorithms Layer
- Added the SLH-DSA post-quantum signature algorithm module, which supports signature, verification, key generation and import, and updated relevant function comments and test code. (Architecture-related: public API)
  ↳ No PR: [e240d39](https://github.com/openssl/openssl/commit/e240d39c6c9e78302b5d49555dcd2d6308ff0b43)
- The storage method of polynomials in ML-DSA keys is changed from arrays to pointers, the initialization logic of vectors and matrices is adjusted, a new signature initialization function is added, and the pre-key setting interface is reconstructed. (Architecture-related: public API)
  ↳ No PR: [efd7c96](https://github.com/openssl/openssl/commit/efd7c96856d45f85aed8ed68c71d2faf23aa9786)
- Added AVXIFMA ISA support for Intel Sierra Forest CPU and optimized RSA exponential operation. (Architecture-related: platform compatibility)
  ↳ No PR: [c18b6f4](https://github.com/openssl/openssl/commit/c18b6f4c52866d5514e53328667e542333d0977a)
- Added 512 and 1024 variant support for ML-KEM, and optimized the API and internal implementation. (Architecture event: Added ML-KEM header file)
  ↳ No PR: [d2136d9](https://github.com/openssl/openssl/commit/d2136d9e730ca13fe12d6ac4c9e093bb348331ce), [653fc21](https://github.com/openssl/openssl/commit/653fc2189dc913404203edb674ce4bb45fe5e177)
- Added support for X.509v3 extensions, including authorityAttributeIdentifier, roleSpecCertIdentifier and attributeDescriptor. (Architecture-related: public API)
  ↳ No PR: [a6e0d6d](https://github.com/openssl/openssl/commit/a6e0d6d5c064af19efa5f917715b0589626908f7), [bda7b3e](https://github.com/openssl/openssl/commit/bda7b3edbbfa43f2209654c89fc8d74ad59e277f), [cccdf41](https://github.com/openssl/openssl/commit/cccdf41010d0859a0d134ac45be7218d9ffd90d2)
- Added support for X.509v3 timeSpecification extension. (Architecture-related: public API)
  ↳ No PR: [70b17e5](https://github.com/openssl/openssl/commit/70b17e5a00dae537181e2722033f190cc1550139)
- Added digest_copyctx function to EVP_MD, optimized the performance of EVP_MD_CTX_copy_ex, implemented this function in the default provider, updated the documentation and added test cases. (Architecture-related: public API)
  ↳ No PR: [4c41aa4](https://github.com/openssl/openssl/commit/4c41aa4b338ca181a394483c8bb6aeb6366c6f96)
- Added X509_VERIFY_PARAM_get_purpose() function, used to obtain the purpose value of the verification parameter. (Architecture-related: public API)
  ↳ No PR: [24b7c27](https://github.com/openssl/openssl/commit/24b7c27250b099d631d428d5b913f0828595cd05)
- Added SLH-DSA post-quantum signature algorithm support, including key generation, signature verification, public key loading, encoder/decoder, FIPS support and self-testing and other complete functions. (Architecture-related: public API)
  ↳ No PR: [34f4cac](https://github.com/openssl/openssl/commit/34f4cacc8fea7fd4a9616c48e951e86c5cf8c006), [2f9e152](https://github.com/openssl/openssl/commit/2f9e152d86a750753ea729f8c9d79d764a73f20c), [8f53b9b](https://github.com/openssl/openssl/commit/8f53b9b59d6786168d10b022859e5d03467022f0), [e8457ce](https://github.com/openssl/openssl/commit/e8457ce07737c53bbc8d5f0abd81b687f12cceaf), [5901ca8](https://github.com/openssl/openssl/commit/5901ca87baf59ae966ee6cc4bee17b652b359898), [5c2b404](https://github.com/openssl/openssl/commit/5c2b404241139cb65d9990645a1b6437eef19301), [a25bcde](https://github.com/openssl/openssl/commit/a25bcde26a4553af5ffcd698c5d6f504806efc01), [b8b67b1](https://github.com/openssl/openssl/commit/b8b67b1907e9614933bde70814ea92bc52ed6f49), [eba0e11](https://github.com/openssl/openssl/commit/eba0e11c39dcacb14da1eda699d528eae829b0a2), [ed77201](https://github.com/openssl/openssl/commit/ed77201a26239509821c4bcd33045e3c417d0ccf), [148f4d2](https://github.com/openssl/openssl/commit/148f4d23e1a9becf8984ddc92fa8ebcb3b760bd9), [16395ee](https://github.com/openssl/openssl/commit/16395ee9cc10a32f1d523c085d1809e75206bc05), [6de4119](https://github.com/openssl/openssl/commit/6de411963f8749cc511c198f2918a3c061f1b0c1), [acdd2c8](https://github.com/openssl/openssl/commit/acdd2c8bff7952d17b3cd61143c7f0b6cb3d7398), [9531a1d](https://github.com/openssl/openssl/commit/9531a1de0fb381ad079680be898e5b8e889e5b6c), [8029960](https://github.com/openssl/openssl/commit/8029960bbc499dffff8d800d3b7825390169992e), [2440305](https://github.com/openssl/openssl/commit/2440305e8f1e6d7132be4a76d1acb2ba6a66633b), [3be71de](https://github.com/openssl/openssl/commit/3be71de4d925a4ef0a053327ff6a83728742c039), [ba90c49](https://github.com/openssl/openssl/commit/ba90c491254fd3cee8a2f791fc191dcff27036c1), [5b52a63](https://github.com/openssl/openssl/commit/5b52a6395c00a8a68dc6950b1a4645c59271a7ec), [237b761](https://github.com/openssl/openssl/commit/237b761ab4987c7d9b798de04ba25fea2af4e500)
- Added ML-KEM-768 post-quantum key encapsulation mechanism algorithm support, including underlying operations, public API, Provider interface and TLS group registration. (Architecture-related: public API)
  ↳ No PR: [96a079a](https://github.com/openssl/openssl/commit/96a079a03ff1239abbfd877b8dab91ba657fc4d1)
- Added EVP_SKEY secret key management interface, which supports key generation, import, export, reference counting and query operations. (Architecture-related: public API)
  ↳ No PR: [d46e010](https://github.com/openssl/openssl/commit/d46e010cd266288a5fb8a663f634c62a3990d6a0), [fc00d9b](https://github.com/openssl/openssl/commit/fc00d9b7b1a4f358fa25e0bc73a5da6763c8b6be), [9422ab6](https://github.com/openssl/openssl/commit/9422ab6a7e354510a049a7adcbad3b1e4b2e04fc)
- Improved the import and export of ML-KEM keys, supporting ASN.1 private key format and retain_seed parameter. (Architecture-related: public API)
  ↳ No PR: [869903c](https://github.com/openssl/openssl/commit/869903c07c56c8c44d4b7362fd56244e4de77d6b), [318994a](https://github.com/openssl/openssl/commit/318994a121daa479f9418514ccf0ac196792de3b)
- Added ML-DSA digital signature algorithm support, including key management, signature, FIPS integration and self-testing. (Architecture-related: new algorithm support)
  ↳ No PR: [c848506](https://github.com/openssl/openssl/commit/c848506cd4a0f978f22dbbba9826b11992afa33e), [a437ba2](https://github.com/openssl/openssl/commit/a437ba2c088558ba0870055571691945efda7bc1), [29d14ee](https://github.com/openssl/openssl/commit/29d14eeb2e71d212476d4f209f0c7976a1a28939), [a8956e2](https://github.com/openssl/openssl/commit/a8956e22d96f37bc15d63a53e285940138dc84ac), [5198146](https://github.com/openssl/openssl/commit/519814602ba4476f23057159cbb3d37dff39a4f3), [2b6dd88](https://github.com/openssl/openssl/commit/2b6dd886452166fb5983116bae012d2bde87f614), [cd430bf](https://github.com/openssl/openssl/commit/cd430bf5da18d56a9a4b59809756390b46d2f3dd), [aebcb36](https://github.com/openssl/openssl/commit/aebcb3658fb12bc9dc8155720de9f6528198d33e), [6184259](https://github.com/openssl/openssl/commit/6184259849900f3952ffebd87dd90809c9e744e2), [c0cf783](https://github.com/openssl/openssl/commit/c0cf783178f88601a40e86b8db4d44708ad3e131), [20599e4](https://github.com/openssl/openssl/commit/20599e480f3ba783d6554d3e078d08bdd8e92e66)
- Separated the ML-KEM encoding and decoding code into independent files, added seed/key preference decoding support, and updated related documents. (Architecture-related: public API)
  ↳ No PR: [5b2d996](https://github.com/openssl/openssl/commit/5b2d996f9145100f5e6d9fbf8ad2488022496931), [d70edce](https://github.com/openssl/openssl/commit/d70edce5bcf172856f67ba3128b85ea94ecbe3c8)
- Add support for directly passing μ values to the ML-DSA verification function to replace the message and skip some preprocessing steps. (Architecture-related: public API)
  ↳ No PR: [55738c1](https://github.com/openssl/openssl/commit/55738c152084857159541b89bf993ba08b0d1524)
- Added EVP_PKEY_CTX_dup support for SLH-DSA algorithm. (Architecture-related: public API)
  ↳ No PR: [0e43652](https://github.com/openssl/openssl/commit/0e436524899d58ceea807cf277d7fcffa14f9065)
- Support PKCS7 signature content of V_ASN1_SEQUENCE type, fix data copy issues, and add related tests. (Architecture-related: public API)
  ↳ No PR: [8cfc26e](https://github.com/openssl/openssl/commit/8cfc26e6c41205e5d932c69c0b29727fb40474c3)
- Fixed the null pointer dereference problem of the PKCS7_OP_SET_DETACHED_SIGNATURE command in PKCS7_ctrl. (Architecture-related: public API: PKCS7_ctrl)
  ↳ No PR: [f2348f1](https://github.com/openssl/openssl/commit/f2348f1f844a54c7a95c32e2354cd29f0860c803)
- Roll back the behavior changes of CMS_get1_certs() and CMS_get1_crls(), and fix related issues. (Architecture-related: public API)
  ↳ No PR: [e2ffc9e](https://github.com/openssl/openssl/commit/e2ffc9e7d086cd6819335c7f01726c900fad992f)
- Fix the redundant address fetching operation when passing x->acinfo in the X509_ACERT_sign_ctx function. (Architecture-related: public API)
  ↳ No PR: [5b33d3e](https://github.com/openssl/openssl/commit/5b33d3e158fc93d30c0dc50953a53b02623fe3c5)
- Fix the X509_PURPOSE_set() function to support clearing purpose requirements and adjusting purpose checking logic. (Architecture-related: public API)
  ↳ No PR: [b48ed24](https://github.com/openssl/openssl/commit/b48ed247370e03a75e1df5dcf41659def128aaa7)
- Fixed the X509_PURPOSE_add function, using the short name as the primary key and adding a new function to obtain unused IDs. (Architecture-related: public API)
  ↳ No PR: [3294dcd](https://github.com/openssl/openssl/commit/3294dcdbc2e3fc1e615b5e8c01813eefaf5a9f6f)
- Fixed a crash that may occur when passing in a NULL certificate in the X509_add_cert function. Now when the cert parameter is NULL, it returns 0 directly. (Architecture-related: public API)
  ↳ No PR: [3c7db9e](https://github.com/openssl/openssl/commit/3c7db9e0fdf4706d91cedf5fca70b609bdc1677e)
- Fixed AES-GCM-SIV algorithm support for zero-length messages, removed early return and length check restrictions. (Architecture-related: AES-GCM-SIV algorithm behavior)
  ↳ No PR: [f1a4f03](https://github.com/openssl/openssl/commit/f1a4f0368b7375762838f9f55c72b090c312cd69)
- Fixed multiple issues in SLH-DSA, and added the slh_dsa_key_dup() function. (Architecture-related: public API: added slh_dsa_key_dup)
  ↳ No PR: [0f0a836](https://github.com/openssl/openssl/commit/0f0a836abda4d391249466ecfe5ca600b92914ea), [92159b4](https://github.com/openssl/openssl/commit/92159b48e95b6e96b09d0efb4cb418c3497f5cf0)
- Add a null pointer check for pctx in the EVP_DigestSign function, and return an initialization error when pctx is empty. (Architecture-related: public API: EVP_DigestSign null pointer check)
  ↳ No PR: [93d366b](https://github.com/openssl/openssl/commit/93d366bea6b8175a9565501be992f41858ad44f3)
- Add a null pointer check to the X509v3_addr_canonize function, and return an error when the addr parameter is NULL. (Architecture-related: public API)
  ↳ No PR: [d3b6b81](https://github.com/openssl/openssl/commit/d3b6b81eab48c1b8ed4075a1818692f640fea999)
- Allow AES-SIV mode to handle zero-length plaintext and additional authentication data (AAD), and fix related return value issues. (Architecture-related: Cipher mode behavior)
  ↳ No PR: [f11c10d](https://github.com/openssl/openssl/commit/f11c10d83e95ecbff8a7670168a52495d2ee080f)
- Fix the SLH-DSA signature verification function, add algorithm short name and NID mapping to support OBJ_find_sigid_algs() and OBJ_sn2nid() calls, and fix the null pointer check when getting the key parameter. (Architecture-related: public API)
  ↳ No PR: [3fcefd5](https://github.com/openssl/openssl/commit/3fcefd51a11058ebf679f858608e419f807679b9)
- Fix the ML-DSA key management function so that it can return the seed parameters according to the document, and ensure that no error is reported when requesting unavailable parameters. (Architecture-related: ML-DSA key management behavior)
  ↳ No PR: [3138976](https://github.com/openssl/openssl/commit/3138976041e6637c732b11c1e0b3d57a1ebd4afb)
- Modify the ML-DSA private key to public key function, add verification of the consistency of the decoded t0 value and the calculated value, and add corresponding test cases. (Architecture-related: ML-DSA core verification)
  ↳ No PR: [bd8954b](https://github.com/openssl/openssl/commit/bd8954bfe50b3271475099bcb53565bcb1763e81)
- Limit the SLH-DSA key generation seed length to exactly 3*n, and add corresponding test cases. (Architecture-related: public API)
  ↳ No PR: [6e770d3](https://github.com/openssl/openssl/commit/6e770d38c72e15ab7d0f7ee0a5dd8deb88116571)
- Enhance the verification of ML-DSA key generation and decoding, check the consistency of the seed and the private key and the matching of the private key and the explicit public key, and fix the memory release sequence in the key reset function. (Architecture-related: public API)
  ↳ No PR: [64a27c2](https://github.com/openssl/openssl/commit/64a27c24d8f6964706ef25465ab5b83fba45766e)
- Add version field check for PKCS8 decoder to ensure compliance with RFC5958. (Architecture-related: external behavior)
  ↳ No PR: [6ab286f](https://github.com/openssl/openssl/commit/6ab286f9ebd970715cf21aa6cf8b3c20d95440bf)
- Optimize the certificate issuer search logic, simplify the cache search process of X509_STORE_CTX_get1_issuer, and unify the internal search functions. (Architecture-related: public API)
  ↳ No PR: [9ca66fc](https://github.com/openssl/openssl/commit/9ca66fc2731a7e76415282a0a8a6b60f0169b156)
- Change the condition for clearing sensitive data in RSA_free from the FIPS_MODULE macro to the OPENSSL_PEDANTIC_ZEROIZATION macro, and correct the parameters of the reference counting printing macro. (Architecture-related: public API)
  ↳ No PR: [e73c1fa](https://github.com/openssl/openssl/commit/e73c1faa530e7e0d32a8ff197ddb43e8ba7aa483)
- Refactor the SLH-DSA implementation, remove the reference counting of SLH_DSA_KEY, unify the type, add auxiliary functions, and limit the key text output to non-FIPS modules. (Architecture-related: Internal API)
  ↳ No PR: [79e7c83](https://github.com/openssl/openssl/commit/79e7c83711268265576c0429a1c378989a786834), [67d52a5](https://github.com/openssl/openssl/commit/67d52a555e31af84e0491023c835ab77fda952b7), [73e01df](https://github.com/openssl/openssl/commit/73e01df48d53ea620e513d2f654892de514e9e1f), [fa8d70b](https://github.com/openssl/openssl/commit/fa8d70bf7568026a72006ef3c8d8d2ea06f067f0)
- Added FIPS support for ML-KEM and ML-DSA, including adding new naked seed/naked private key formats, removing paired conformance testing for ML-DSA under FIPS, and adding conditional compilation for hybrid KEM. (Architecture-related: public API)
  ↳ No PR: [0fb5a78](https://github.com/openssl/openssl/commit/0fb5a78acd35ce41738631a60106701694bcab11), [2b7679b](https://github.com/openssl/openssl/commit/2b7679b16d970f99e76b631b62f51bdeffb14627), [b6c5342](https://github.com/openssl/openssl/commit/b6c5342613b50042b30ee48d16c781fb54074c77)
- Extract the duplicate fnv1a_hash function into a public ossl_fnv1a_hash function, and update the caller. (Architecture-related: Internal API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [35fb39d](https://github.com/openssl/openssl/commit/35fb39da76a802f068f24b418555d39700f6068c) | No PR: [87b5aa7](https://github.com/openssl/openssl/commit/87b5aa737d5abf738188cb8572754ff8e033de2f)
- Add ML-KEM-768 known answer tests from BoringSSL, and extend the test framework to support deterministic key generation, encapsulation and decapsulation, and key export/import functionality. (Schema related: public API)
  ↳ No PR: [42436eb](https://github.com/openssl/openssl/commit/42436eb53ed8b147835e3f6a17e7be25b972e457)
- Optimize the X509_STORE_CTX_get1_issuer function and introduce a fast path to give priority to returning certificates that are within the validity period or have recently expired. (Architecture-related: public API)
  ↳ No PR: [b45e035](https://github.com/openssl/openssl/commit/b45e035bf7a93df67d2b5fd96f818d02f977ec8a)
- Fixed the problem in ML-DSA that the security bit value returned by the OSSL_PKEY_PARAM_SECURITY_BITS getter is wrong (deviation is 8 times). (Architecture-related: public API)
  ↳ No PR: [43f07d1](https://github.com/openssl/openssl/commit/43f07d1bdb8b24d98213b9ccfde9e02b741191af)
- Make ML-KEM self-check configurable when importing, refactor key generation and copy functions. (Architecture-related: public API)
  ↳ No PR: [cab4e7c](https://github.com/openssl/openssl/commit/cab4e7cbd14f97ee4c3e5b9f900cb599ee454ee5)
- Make KEM operation mode optional, using DHKEM mode by default. (Architecture-related: external behavior)
  ↳ No PR: [ddd7ecb](https://github.com/openssl/openssl/commit/ddd7ecb04bcea5c13be3c73f3dc1a101087cdf24)
- Supports PKCS#8 V2 format, allows the structure to contain optional public key fields, and adds version number verification. (Architecture-related: public API)
  ↳ No PR: [d469233](https://github.com/openssl/openssl/commit/d46923327f6cf74431b601d82f04ff85a188fe56)

### Cross-cutting / Other Architecture-related Changes
- Removed the obsolete header file include/openssl/asn1_mac.h, which may affect the backward compatibility of code that relies on this header file. (Architecture event: Removed public header file asn1_mac.h)
  ↳ No PR: [d4430ef](https://github.com/openssl/openssl/commit/d4430ef9fc871c6e37e2121357b60f053d07525f)
- Moved the SSL object unpacking macro to a separate header file, and introduced QUIC_OBJ as the public header of the QUIC object. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [bf55326](https://github.com/openssl/openssl/commit/bf55326752eb213d01c88c8d644b341fb01e1dd1)
- Migrate the SSL error string loading function from libssl to libcrypto, so that libssl can be safely unloaded without generating dangling references. (Architecture-related: module responsibility)
  ↳ No PR: [aaad33c](https://github.com/openssl/openssl/commit/aaad33c5ac1ce574229066ca3ce47ef3510a6e8d)
- Added support for the DEFAULT keyword and '-' prefix to the SSL_CTX_set1_groups_list() function, allowing to specify a default group or remove a specific group in the group list, and fixed related error handling. (Architecture-related: public API)
  ↳ No PR: [357e273](https://github.com/openssl/openssl/commit/357e27342e9bbe8d45e8be079a11588e7905fc55)
- Improve the QUIC header decoding function and add the failure reason output parameter to distinguish version mismatch from other decoding errors. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2784112](https://github.com/openssl/openssl/commit/2784112e9a5d844b7a54ae6de5ab9d06a9822ef6)
- Added complete support for ML-DSA digital signature algorithm, including key generation, signature and verification functions. (Architecture-related: Added ML-DSA algorithm)
  ↳ No PR: [d3a7ae6](https://github.com/openssl/openssl/commit/d3a7ae64b337b494981a8868a63762db6a934fcf), [3ab7409](https://github.com/openssl/openssl/commit/3ab7409f3d9a05608e94b5351789fd85994b6511)
- Enhanced QUIC port binding function, supports connection establishment without odcid, and added address verification control flag. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [207892d](https://github.com/openssl/openssl/commit/207892d022d5c3b162031a22faf051bfa6b0997e), [0746d46](https://github.com/openssl/openssl/commit/0746d4628ecf5e6c990c320e255bb47fc274970e)
- Added support for multiple X.509v3 extensions: attributeMappings, allowedAttributeAssignments, aAissuingDistributionPoint. (architecture-related: public API)
  ↳ No PR: [93b5275](https://github.com/openssl/openssl/commit/93b5275f6bfc46091d30e263e8df3fdba1cbb44a), [9598bc1](https://github.com/openssl/openssl/commit/9598bc15e9bcc137182c709057b79aef1d347a06), [0d8cc7c](https://github.com/openssl/openssl/commit/0d8cc7c69904371c396a6c6eda58fde0201046c2)
- Added QUIC callback function SSL_CTX_set_new_pending_conn_cb, which is used to notify newly created SSL objects waiting to be accepted, and supports SSL object pre-allocation. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [dc04a11](https://github.com/openssl/openssl/commit/dc04a11ccacb507beed7de1e9301660d4a630adf), [a607146](https://github.com/openssl/openssl/commit/a607146904c9bb5d417806d480827e0389902adf), [7502df2](https://github.com/openssl/openssl/commit/7502df20bcc4fab6d292b54a7674356448a94d55)
- Added QUIC NEW_TOKEN token generation and cache management functions, including public API to create and manage token cache, and optimize sending strategy. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [e73f330](https://github.com/openssl/openssl/commit/e73f330e99031f53820a382cf3a0776375f5b719), [b1828dc](https://github.com/openssl/openssl/commit/b1828dc23ac8824365713f2d050ca2a180927686), [9a055c8](https://github.com/openssl/openssl/commit/9a055c89170b3e8a2a6e210ec7f7f3df8f67f8a7), [c266322](https://github.com/openssl/openssl/commit/c266322bd1e2842dd92e7e2fc1043d1ade987c57), [642fde8](https://github.com/openssl/openssl/commit/642fde861688581e0be672fe89735477102a562e)
- Made the quic-tls API work properly even when QUIC is not enabled, adjusted the error handling logic and added a new configuration function. (Architecture-related: public API)
  ↳ No PR: [c21e213](https://github.com/openssl/openssl/commit/c21e213b97098a1545248adc1681877cb1fc87ce), [0c3e1f2](https://github.com/openssl/openssl/commit/0c3e1f25b290722be3f2658c5a0d31c47d9c5806)
- Support multiple key shares (key shares), expand the group list definition and update the key_share extended processing logic on the client and server sides. (Architecture-related: TLS protocol)
  ↳ No PR: [d69c014](https://github.com/openssl/openssl/commit/d69c014608acdfa37839d49412e6d6974ac539a0)
- The EVP_CIPHER_CTX_get_block_size function now allows the NULL ctx parameter to be passed in and returns 0, and the related documentation has been updated. (Architecture-related: public API)
  ↳ No PR: [a69288d](https://github.com/openssl/openssl/commit/a69288d04aeac4927f092055a74e7d36c5847869)
- Support HTTP transmission through BIO set by OSSL_CMP_CTX_set_transfer_cb_arg, and adjust the connection management logic. (Architecture-related: public API)
  ↳ No PR: [5cba362](https://github.com/openssl/openssl/commit/5cba3629098a55a559a9bb177c095fc77b1e8b88)
- Signature algorithm configuration now accepts both IANA standard names and internal names for matching. (Architecture-related: Signature algorithm configuration)
  ↳ No PR: [9a6bbf6](https://github.com/openssl/openssl/commit/9a6bbf616957cf6fca543ba4604980953c9a3e01)
- Adjusted the default TLS group list, added a hybrid ML-KEM group, sent two key shares by default, and streamlined the default group list; also made the TLS elliptic curve group deprecated in RFC 8422 disableable, and moved the deprecated curve to the end of the list. (Architecture-related: TLS groups and key sharing)
  ↳ No PR: [63a70d6](https://github.com/openssl/openssl/commit/63a70d63e273cb419eb875ea30c2ac1864737c28), [fed9be3](https://github.com/openssl/openssl/commit/fed9be39ffecc734abfa93fdd8399ccd738b4346), [7e80b16](https://github.com/openssl/openssl/commit/7e80b16776a58aad8bfe5d81c2909757115545da)
- Fixed multiple issues in the ML-DSA implementation, including key encoding and decoding, signature verification logic and constant time auxiliary functions, and fixed the issue that the hint buffer part was not initialized. (Architecture event: OpenSSL_Core_Headers module change)
  ↳ No PR: [fcffbbe](https://github.com/openssl/openssl/commit/fcffbbe1920c8bc38fe79a8c67b2f37a5d8593a9), [2cb4b0c](https://github.com/openssl/openssl/commit/2cb4b0c78121e041e9ffeef60cfbfef027d178c6), [5a1caef](https://github.com/openssl/openssl/commit/5a1caef900373c552f28aba97221a16686207edf)
- Fixed spelling errors, adjusted the comment format, fixed the return value of SSL_get0_listener in non-QUIC scenarios, removed redundant header files, and fixed memory leaks in tests. (Architecture-related: public API behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [eda445e](https://github.com/openssl/openssl/commit/eda445e13d80d73f4ea13ea658991d2073fe0f03)
- Fixed the handling of SSL_pending and SSL_has_pending in QUIC applications to be compatible with s_client. (Architecture-related: public API behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2399678](https://github.com/openssl/openssl/commit/2399678797ba5210cd9a47f47943b0973e6be180)
- Fixed the issue where SSL_ERROR_WANT_READ was returned incorrectly when the number of written bytes was zero during QUIC non-blocking writing, and SSL_ERROR_WANT_WRITE was returned instead. (Architecture-related: public API behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [458018f](https://github.com/openssl/openssl/commit/458018f3e670155ea1259ebb1fc7a27c11cf0147)
- Fixed multiple issues in QUIC listener creation, including thread safety, memory release and port configuration, and implemented the function of creating new connections from listener. (Architecture-related: QUIC protocol support)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [b93fb2d](https://github.com/openssl/openssl/commit/b93fb2d17749b10e5c57ca4353b0d4a99936971f)
- Fixed an issue where the client signature algorithm was not saved correctly during post-handshake authentication (PHA), ensuring that the client always uses the signature algorithm in the current extension when receiving a PHA request. (Architecture-related: TLS handshake behavior)
  ↳ No PR: [d48c2cb](https://github.com/openssl/openssl/commit/d48c2cb6ec7579ccebfe8d8caf6638a7c5172edb)
- Fixed multiple minor issues in the QUIC concurrency API, including adjusting the structure field order, correcting comments, adding null pointer checks, optimizing error handling paths, and unifying socket invalid value judgment. (Architecture-related: QUIC concurrency API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [73d7de1](https://github.com/openssl/openssl/commit/73d7de128bd056213332732676e27498d7981d1e)
- Add checks for NULL file names in multiple file loading functions to avoid null pointer dereferences. (Architecture-related: public API)
  ↳ No PR: [3ef1b74](https://github.com/openssl/openssl/commit/3ef1b7426b05c18419ba0eb6495ec761c91834c1)
- Removed the restriction on key type names in the EVP_PKEY_Q_keygen function, and now accepts any unrecognized key type name. (Architecture-related: public API)
  ↳ No PR: [a57c6f8](https://github.com/openssl/openssl/commit/a57c6f84920bff522bca5fede73f1a3f132d7cff)
- When rejecting invalid FFDHE and ECDHE key shares, change the alert type sent from SSL_AD_INTERNAL_ERROR to SSL_AD_ILLEGAL_PARAMETER to comply with RFC 8446 specification. (Architecture-related: external behavior)
  ↳ No PR: [0f6caf7](https://github.com/openssl/openssl/commit/0f6caf740977fa25d0f05cd3c48a656efbd9a79e)
- Fixed build errors when OPENSSL_NO_SSLKEYLOG is not defined. (Architecture-related: build and installation methods)
  ↳ No PR: [a2b5e64](https://github.com/openssl/openssl/commit/a2b5e64907a87d603ff649eccd7fdf151e34e4ba)
- Fixed error handling when key log setting fails, key log cleaning logic in SSL_CTX_free, and ssl_cache_cipherlist error code value. (Architecture-related: public API)
  ↳ No PR: [6f7273a](https://github.com/openssl/openssl/commit/6f7273a9b0cb9891f72842bc88de561c83c4e7f8)
- Fix the SSL_inject_net_dgram function so that it correctly returns the return value of ossl_quic_demux_inject instead of always returning 1. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [41fe7a2](https://github.com/openssl/openssl/commit/41fe7a2b8e3ba7075aa34b9d2412037e87cfffb5)
- Fix the use-after-free problem that may be caused by the REF_PRINT_COUNT macro after the reference count is decremented, and instead pass the reference count return value instead of the object pointer. (Architecture-related: reference counting behavior)
  ↳ No PR: [dc10ffc](https://github.com/openssl/openssl/commit/dc10ffc2834e0d2f5ebc1c3e29bd97f1f43a0ead)
- Fix memory ordering guarantees for reference counting operations, change release operations from relaxed to release semantics, and use stronger acquire-release semantics in TSAN builds to eliminate false positives. (Architecture-related: thread safety guarantees)
  ↳ No PR: [3bf273b](https://github.com/openssl/openssl/commit/3bf273b21b3e21cca9cd143ed9016397bd7dbb57)
- Fix the error checking of EVP_PKEY_set1_encoded_public_key return value in multiple functions, and fix the parameter checking logic in DH CMS and the error code in TLS handshake. (Architecture-related: public API behavior fix)
  ↳ No PR: [1273fae](https://github.com/openssl/openssl/commit/1273fae170dd629990a3c65bfd5cf3f7a93c1477)
- Fixed compilation issue on arm64_32 platform, by restricting Apple M1 special handling to only 64-bit pointer environments. (Architecture-related: platform compatibility)
  ↳ No PR: [79c9cbb](https://github.com/openssl/openssl/commit/79c9cbbe1f9c3b8314312b6d8bb25b7138831e04)
- Fixed compiler warning in safe_math.h caused by __GNUC__ being undefined, by first checking whether the macro is defined and then comparing versions. (Architecture-related: platform compatibility)
  ↳ No PR: [53b3456](https://github.com/openssl/openssl/commit/53b34561b56b60a812f8f65c777d469e18151e8d)
- Add return value checking for up_ref calls of multiple modules to ensure that resources are released correctly and an error is returned when the reference counting operation fails. (Architecture-related: public API)
  ↳ No PR: [00fbc96](https://github.com/openssl/openssl/commit/00fbc969885a5721bc1b732f795fd8c09835b44f)
- Improved ASN1_TIME_print function, fixed printing of fractional seconds on EBCDIC platform, and added missing GMT time zone indication. (Architecture-related: Platform compatibility)
  ↳ No PR: [c81ff97](https://github.com/openssl/openssl/commit/c81ff978667e7c0d792e02db7a02b7bc12433abd)
- Fixed the no-ml-dsa configuration option, added it to bulk group and CI test, and added conditional compilation protection for ML-DSA related functions in self-test. (Architecture-related: Build configuration)
  ↳ No PR: [dd1d010](https://github.com/openssl/openssl/commit/dd1d010130c587c47d507ca501f6dc239798a97c)
- Reconstructed the creation logic of QUIC ports and channels, and optimized the connection acceptance process so that ossl_quic_accept_connection directly returns the TLS connection object. (Architecture-related: QUIC protocol stack)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f193e0e](https://github.com/openssl/openssl/commit/f193e0e9fb3f015b961607134609694dbbdfbe3c), [57f5af6](https://github.com/openssl/openssl/commit/57f5af6f4cf6ae0f7b23be3e46d1007502067912)
- Deprecated all BIO_meth_get_* functions, and added deprecated macro support for OpenSSL 3.5. (Architecture-related: API deprecation)
  ↳ No PR: [0bba821](https://github.com/openssl/openssl/commit/0bba821881868252bfca4400879682a1648da225)
- Added a new configuration to enable FIPS, disable thread pool and QUIC in Windows CI build. (Architecture-related: Build configuration)
  ↳ No PR: [ecab977](https://github.com/openssl/openssl/commit/ecab977464be75bc8b24e10e88d19b629fe6e0d4)
- Added GitHub Actions release workflow to automatically execute the release process. (Architecture-related: release process)
  ↳ No PR: [d8af77e](https://github.com/openssl/openssl/commit/d8af77e7368a72f75ad790350a322e8f6c3c2968)
- Added FIPS build option in daily CI check and turned off legacy transition function. (Architecture-related: Build configuration)
  ↳ No PR: [a08a145](https://github.com/openssl/openssl/commit/a08a145d4a7e663dd1e973f06a56e983a5e916f7)
- Added build and test support for Linux ppc64le and s390x platforms in CI. (Architecture-related: Platform compatibility)
  ↳ No PR: [8f0c8e3](https://github.com/openssl/openssl/commit/8f0c8e33bfdef3499e128b6c60a22844b80c481b), [8900cdf](https://github.com/openssl/openssl/commit/8900cdf2305c55aa3a1d4b0d6b4d33afdc72e756)
- Disabled FIPS support for multiple architectures in the cross-compilation workflow to resolve an issue where testing was too slow due to SLH-DSA post-quantum signatures. (Architecture-related: Build Configuration)
  ↳ No PR: [347de0a](https://github.com/openssl/openssl/commit/347de0ab1f870ead0349365db981989a58835a21)
- Dynamically select the ARM runner image based on the running warehouse in the CI configuration. (Architecture-related: CI configuration)
  ↳ No PR: [51597e2](https://github.com/openssl/openssl/commit/51597e2ee6ef4a384167bb1ed3528da1ab578d61)
- Added the ability to detect hardware through dl_hwcap and hwcap on the RISC-V platform, which is used to determine the availability of extensions such as ZVK*. (Architecture-related: platform compatibility)
  ↳ No PR: [7fb4a32](https://github.com/openssl/openssl/commit/7fb4a323f188ecaa22a823b22e5f39f049e70bc3)

### Protocol Layer
- Integrate an inter-thread notification mechanism for QUIC reactor, support waking up blocked waiting threads through notification file descriptors in multi-thread scenarios, and allow scheduling notifications when tick results are merged. (Architecture event: QUIC reactor thread notification)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [6bc47aa](https://github.com/openssl/openssl/commit/6bc47aa65f3d0ae84b04ecbd2d58498c6ecb24f6), [1c89357](https://github.com/openssl/openssl/commit/1c89357d75489ca890b3cf8a6f5691e2e8c1a491), [fa4a8e8](https://github.com/openssl/openssl/commit/fa4a8e8871770898a4ac7b79c6ed2578073878b0), [5dade08](https://github.com/openssl/openssl/commit/5dade08ed1eeb91d1db7c759baf01ed83eb2d081)
- Implement the QUIC version negotiation retry mechanism, including the server sending the RETRY_SCID parameter, the packager accepting the version parameter, and the client retrying the connection according to the server version list. (Architecture-related: QUIC version negotiation)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [35f1917](https://github.com/openssl/openssl/commit/35f1917f2da1dec62e665e30b44337bbe184b138), [5fdd623](https://github.com/openssl/openssl/commit/5fdd623df3ab5a4ed7dff0719851345b2de45d9d), [78702fb](https://github.com/openssl/openssl/commit/78702fb7d63b6dc423266672dbe605cc694bdb44)
- Implement the SSL_new_from_listener() function, used to create QUIC connection objects from the listener. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [0b15147](https://github.com/openssl/openssl/commit/0b15147a37c5eeab01862fc374eeac11d4fb173b), [7efebeb](https://github.com/openssl/openssl/commit/7efebeb172a934c1ef32b9f446ec02ff5e6f416c)
- Support QUIC token function, including NEW_TOKEN frame processing, token cache allocation, and initial token search and verification. (Architecture-related: QUIC protocol)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [0f71ebe](https://github.com/openssl/openssl/commit/0f71ebec26a4dc41c249a7d7ade1a8bfe43497fc), [38cb9ca](https://github.com/openssl/openssl/commit/38cb9ca1ad2869900acde4427e04cbe00c2e2c01), [29e861a](https://github.com/openssl/openssl/commit/29e861a5a6056aebe21af7d75d97caf2a8eff081), [a2fe643](https://github.com/openssl/openssl/commit/a2fe6435cac29b7d74595667bddfa11b4e0cba72), [725074f](https://github.com/openssl/openssl/commit/725074f4e7068220843bd0bb0db3b05c56fdb8d6), [d79ef11](https://github.com/openssl/openssl/commit/d79ef118db48cf599027064e341a80cdaca4e00a), [ebc52f1](https://github.com/openssl/openssl/commit/ebc52f1f02e789a7f2d98b4627fc325f33a2ea03)
- Added obtainable and settable context parameters for the ML-DSA signature algorithm, and added the algorithm identifier serialization function required to generate X.509 certificates. (Architecture-related: public API)
  ↳ No PR: [808fccb](https://github.com/openssl/openssl/commit/808fccb721f2fb621c3ffeb789dc4c13f2f37986)
- Added an API for obtaining the short connection ID length of the QUIC server. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [5b808e1](https://github.com/openssl/openssl/commit/5b808e1d804b8215254e52f01ea1928a905cb801)
- Added support for generating X.509 certificates through the OpenSSL command line for the SLH-DSA algorithm. (Architecture-related: public API)
  ↳ No PR: [7389cca](https://github.com/openssl/openssl/commit/7389cca07961871320afeae46d5ed8a45fe23145)
- Added SSL_NO_EOED macro, used to skip the processing of the EndOfEarlyData message in scenarios where the message is not required (such as QUIC). (Architecture-related: TLS protocol behavior)
  ↳ No PR: [1b3f27f](https://github.com/openssl/openssl/commit/1b3f27f9208a8d7576102b3bba6443885fb01e7c)
- Add an access interface for the IANA signature scheme name for TLS connections, and output the signature algorithm name in the connection summary; s_client preferentially uses the IANA registered name when reporting the peer signature algorithm. (Architecture-related: public API)
  ↳ No PR: [594cef4](https://github.com/openssl/openssl/commit/594cef49b4e85839983aea083ed9497330421abb), [4ace4a7](https://github.com/openssl/openssl/commit/4ace4a71665028507c70bbe9f3b81817be3e55d6)
- Fixed documentation and usage issues of X509v3_add_extensions when sk_X509_EXTENSION_num(exts) <= 0 and target is NULL. (Architecture-related: public API)
  ↳ No PR: [577ec49](https://github.com/openssl/openssl/commit/577ec498bd8106c022903dc90c9e30abe4accb3c)
- Fixed build failure when using musl on riscv64, by checking whether __NR_riscv_hwprobe is defined to determine whether to enable RISC-V hardware detection function. (Architecture-related: platform compatibility)
  ↳ No PR: [27fa9d3](https://github.com/openssl/openssl/commit/27fa9d33e1355ae1ef1c0a072f9b511858dfef85)
- When the server receives an unsupported QUIC version, it no longer discards the Initial packet, but replies with a version negotiation packet, and adds encryption and cleaning functions for verification tokens. (Architecture-related: QUIC protocol behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [bc4c7cf](https://github.com/openssl/openssl/commit/bc4c7cf554b1f0f004a8f925ffb7168bc1327d58)
- Version negotiation packets now use network byte order to send and receive a list of supported versions. (Architecture-related: QUIC version negotiation behavior)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [128619a](https://github.com/openssl/openssl/commit/128619a43b713b507abd211c9a149a5b16d22dff)
- Fixed coverage test issues in ML-DSA key handling, removed unused propq fields and corrected public key comparison conditions. (Architecture-related: public API)
  ↳ No PR: [30b6650](https://github.com/openssl/openssl/commit/30b6650e1d6262c02597e4c1b6c094accd99640e)
- Unified the default group lists of QUIC and TLS, and deleted the QUIC-specific default group list macro definition. (Architecture-related: QUIC/TLS default group list unified)
  ↳ No PR: [a89c99e](https://github.com/openssl/openssl/commit/a89c99e04bb9484058b70ff081e7e351044e4cb3)
- Introduced the internal public function ossl_bio_print_hex, replacing the original private print_hex implementation. (Architecture-related: internal API)
  ↳ No PR: [1f7d2a2](https://github.com/openssl/openssl/commit/1f7d2a28877dffdaf607a6fdcc5fcc5f5e030b1e)
- Fixed the buffer out-of-bounds problem caused by directly dereferencing BIO_ADDR in many places in the QUIC stack, using BIO_ADDR_copy() to safely copy addresses, and adding a clearing operation in BIO_ADDR_make. (Architecture-related: public API)
  ↳ No PR: [395a83a](https://github.com/openssl/openssl/commit/395a83a617a09c1ae02e8040386f9acb356d13c1)
- Add support for non-digest signature schemes (such as Ed25519, ML-DSA) to CMS. (Architecture-related: public API)
  ↳ No PR: [cad3520](https://github.com/openssl/openssl/commit/cad3520bf7b7ff0118cf743210d33a5632337183)
- Added ossl_qrx_pkt_orphan function to handle qrx packages that become orphans due to unused channels. (Architecture-related: public API)
  ↳ No PR: [9a308a8](https://github.com/openssl/openssl/commit/9a308a89a4f43ccfdcd9923e8951081a404b5fdc)

### Provider Framework
- Added a new random number generation API in the FIPS provider, and introduced RAND_set1_random_provider() to support external random provider replacement, while implementing FIPS 140-3 CRNG testing. (Architecture event: OpenSSL_Core_Headers module change)
  ↳ No PR: [37172e2](https://github.com/openssl/openssl/commit/37172e2ab8377706c6ce5c79e4bc700cff522f6f), [4636a39](https://github.com/openssl/openssl/commit/4636a39503ee077cb3c6ed23f3b6054469ff983c), [b1cca25](https://github.com/openssl/openssl/commit/b1cca2599938df2cec608d138851801565a81e78), [6f20c68](https://github.com/openssl/openssl/commit/6f20c6804e639230a2228810be0f682d452743e0), [6b518fe](https://github.com/openssl/openssl/commit/6b518fef381a36d655f2394da10e580099b5fc3a), [5ac48fd](https://github.com/openssl/openssl/commit/5ac48fd813768d7246529358bbee292e4632c4f9), [0081964](https://github.com/openssl/openssl/commit/0081964805421e81cfa804474b1005985d5c6278)
- Added EVP pipeline encryption API, including initialization, update and final processing functions. (Architecture event: OpenSSL_Core_Headers module change)
  ↳ No PR: [ef7967d](https://github.com/openssl/openssl/commit/ef7967d0b449c7492657549876bdaadd2e575f3c), [a055154](https://github.com/openssl/openssl/commit/a05515460743da8afd2f5e66b4ce56c23c4a0ea1)
- Added ML-KEM algorithm support, including self-test, DER encoder/decoder, text encoder and key management parameters, and added alias names without hyphens. (Architecture event: Added ML-KEM header file)
  ↳ No PR: [7057138](https://github.com/openssl/openssl/commit/7057138f0fb3fef022877bb85d0ea9131a01da46), [073b9f2](https://github.com/openssl/openssl/commit/073b9f2b1e276c362b3b93b6a3ea1389100c8781), [ff40a08](https://github.com/openssl/openssl/commit/ff40a08deeb2a24229f5d9074e9a57717a90edf6), [b818a99](https://github.com/openssl/openssl/commit/b818a99839ee85984e044bfeb1a3a0ca3307d52f), [ba20b3a](https://github.com/openssl/openssl/commit/ba20b3adeecc30c694e7c50780dd37b1b8c9b6c9), [9a79d40](https://github.com/openssl/openssl/commit/9a79d4088fe8dae05ffe55714c554b55b69f2da9), [78df1c1](https://github.com/openssl/openssl/commit/78df1c1f611796b6e86f5dbac6ffe45dca6f7c0f), [a5cc141](https://github.com/openssl/openssl/commit/a5cc141bbc2cc18d7696c2369ccdac7b31e27463), [1f5ac72](https://github.com/openssl/openssl/commit/1f5ac721e32805a475235f189dbdb784812f2ca6), [5a1819a](https://github.com/openssl/openssl/commit/5a1819a1506393ee9c313bb28e6816190541dfaf)
- Added public big and small endian loading and storage functions, supporting the reading and writing of 16/32/64-bit unsigned integers. (Architecture event: Added byteorder.h header file)
  ↳ No PR: [92c242e](https://github.com/openssl/openssl/commit/92c242e8ac26e1d4cb692c5258d0aefa14e5de84)
- Implemented a flexible encoder for ML-DSA, supported two private key formats of seed and expansion key, reconstructed the key management, encoding and decoding and parameter acquisition interfaces, and added ML-DSA-87 parameter set support. (Architecture event: ML-DSA encoder and key management reconstruction)
  ↳ No PR: [5421423](https://github.com/openssl/openssl/commit/5421423ef95c6c2ee352422d13bd515bebe815d6)
- Add central key generation support for CMP protocol, including client options and server-side processing logic. (Architecture-related: public API)
  ↳ No PR: [0048817](https://github.com/openssl/openssl/commit/0048817523b6b9d0bf514c90ad9c6a99167d0293), [253a380](https://github.com/openssl/openssl/commit/253a380bdbc6fb8d0f051196dca58b26ddb00067)
- Stop detecting getentropy(3) on FreeBSD, use getrandom(2) unconditionally instead, and keep the old version fallback. (Architecture-related: platform compatibility)
  ↳ No PR: [3d09057](https://github.com/openssl/openssl/commit/3d090579e329dbc4aae5b349855f66eeed3d984e)
- Added OID definitions related to TCG (Trusted Computing Group) and platform certificates. (Architecture-related: public API)
  ↳ No PR: [9183306](https://github.com/openssl/openssl/commit/91833068158caf866175a43a26fad9f4dc480a95)
- Added error codes and corresponding error descriptions for continuous entropy source test failures. (Architecture-related: public API)
  ↳ No PR: [ce27133](https://github.com/openssl/openssl/commit/ce27133708daf4eea71162af831216d2fe84b040)
- Added PROVIDER and QUERY tracking categories, added QUERY tracking points in the method store, and updated tests to support the new categories. (Architecture-related: public API)
  ↳ No PR: [193296e](https://github.com/openssl/openssl/commit/193296eaaa0e8deeef5bb72c451862395bb776d7), [3eed43f](https://github.com/openssl/openssl/commit/3eed43f8a12ef33d9788ef9476f76ff1a11dff87), [4fec10e](https://github.com/openssl/openssl/commit/4fec10eae71124a1c2ab08f4fadd7988b658d692)
- Added EVP_get1_default_properties function, used to obtain the default property string of the specified library context. (Architecture-related: public API)
  ↳ No PR: [54fb2fd](https://github.com/openssl/openssl/commit/54fb2fd0131ee6e7792bf7a65a89e090e28d4bd6)
- Added support for internal jitter entropy source in FIPS provider for random number seed source. (Architecture-related: FIPS provider)
  ↳ No PR: [3a01d5d](https://github.com/openssl/openssl/commit/3a01d5d65bdc95745e7ff762541b6394032e48a0), [61f032c](https://github.com/openssl/openssl/commit/61f032cc7b0692abfa608112dcd6d5ff1be2374c), [fc5fb3c](https://github.com/openssl/openssl/commit/fc5fb3c925258eb85c8802ea965ec4a5d389775c), [ed524da](https://github.com/openssl/openssl/commit/ed524da19a0b20d606c559d30580b99e56d66f6f)
- Increased the maximum response length limit for CRL downloads from 100KB to 32MB. (Architecture-related: public API)
  ↳ No PR: [cdbe47b](https://github.com/openssl/openssl/commit/cdbe47bf3c02979183d1f66b42c511a18a63c61d), [e647220](https://github.com/openssl/openssl/commit/e647220c00bb1da0518f8a31ed07b2a0977a3c9e)
- Exposed the internal parameter printing function as API function OSSL_PARAM_print_to_bio, and updated the implementation of provider-related internal functions. (Architecture-related: public API)
  ↳ No PR: [63b6716](https://github.com/openssl/openssl/commit/63b671626e32a8760872790aa2efc3455401ac9e)
- Added a macro definition for the maximum number of pipes in the password pipeline pipeline in the EVP header file. (Architecture-related: public API)
  ↳ No PR: [c44066b](https://github.com/openssl/openssl/commit/c44066bb4cfee9e21ee6406112daebac03775067)
- Added EVP_MAC_init_SKEY function, supports initializing MAC context through EVP_SKEY, and reconstructs MAC algorithm registration and error handling logic. (Architecture-related: public API)
  ↳ No PR: [759570b](https://github.com/openssl/openssl/commit/759570bfedbd897a390539c0b39603b060a4150a)
- Force FIPS 3.0.9 provider callbacks to use the jitter entropy source, and add an entropy acquisition function between the core and provider. (Architecture-related: FIPS compatibility)
  ↳ No PR: [aa5f1b4](https://github.com/openssl/openssl/commit/aa5f1b4cf562d7f0b65ae7ef93179ebc1102fbeb)
- Added a hybrid KEM provider for ML-KEM and ECDHE, supporting four hybrid groups (X25519+ML-KEM-768,
  ↳ No PR: [4b1c73d](https://github.com/openssl/openssl/commit/4b1c73d2dd748ec7dc8a82d517e1ff46db132e7b)
- Added the ossl_rand_pool_adin_mix_in function, which is used to XOR additional inputs into the existing entropy of the random pool, and reconstructed the related random pool entropy mixing logic. (Architecture-related: public API)
  ↳ No PR: [d992e87](https://github.com/openssl/openssl/commit/d992e8729ee38b082482dc010e090bb20d1c7bd5)
- Added ML-DSA-44 and ML-DSA-87 algorithm support, and fixed data encoding issues on big-endian systems. (Architecture-related: public API)
  ↳ No PR: [a2391f3](https://github.com/openssl/openssl/commit/a2391f3aa5c701c3b3d0d337d24181c8d55e87e7)
- Added public and private key DER encoders and text output functions for ML-DSA keys, and restructured the related encoders of ML-KEM and SLH-DSA. (Architecture-related: public API)
  ↳ No PR: [d9ffc11](https://github.com/openssl/openssl/commit/d9ffc11939e6d9b3cb7884f2c082f4c96dceb233), [df231a8](https://github.com/openssl/openssl/commit/df231a88abab21c31274b6dd0fb8ff90efebbbfe)
- Added new OID definitions for post-quantum cryptographic algorithms ML-KEM, ML-DSA and SLH-DSA. (Architecture-related: public API)
  ↳ No PR: [d31fce1](https://github.com/openssl/openssl/commit/d31fce1972f27fa990869b3044f015a6ef6bec98)
- libssl now accepts any key management that implements this group, no longer restricted to a specific provider. (Architecture-related: public API)
  ↳ No PR: [9fdb2a0](https://github.com/openssl/openssl/commit/9fdb2a0c2d58b7f95ceaddd477696afa133c5c36)
- Supports the setting of provider configuration parameters, acquisition and Boolean query, and adds related API and command line support. (Architecture-related: public API)
  ↳ No PR: [38a0926](https://github.com/openssl/openssl/commit/38a0926528791762cf8f0f4e3ed0e2f590b894b9), [e6855e1](https://github.com/openssl/openssl/commit/e6855e1d79088152a39df72cf0e67845095df7e3), [1397dc5](https://github.com/openssl/openssl/commit/1397dc59c608f0545fab11c8dc8ec3bd7ccc3eea), [95a3662](https://github.com/openssl/openssl/commit/95a3662626602c7298170849819e02002b7add42)
- Make provider context available in the encoder, and add PEM_ASN1_write_bio_ctx function to support passing provider context. (Architecture-related: public API)
  ↳ No PR: [35f6e7e](https://github.com/openssl/openssl/commit/35f6e7ea02b599d5aaf220b4720cbadd946d8023)
- Added ML-DSA key generation self-test for FIPS module. (Architecture-related: public API)
  ↳ No PR: [756527b](https://github.com/openssl/openssl/commit/756527b89ccc82eabb7db3012e63f84e52da07ca)
- Add a universal key management implementation to the default provider, supporting the import, export and encryption operations of symmetric keys. (Architecture-related: public API)
  ↳ No PR: [5c16da0](https://github.com/openssl/openssl/commit/5c16da0c1832af8a9d72080d9ec4855d91cc846b)
- Added TLS signature algorithm support for ML-DSA, and registered the signature algorithm constants of ML-DSA in the TLS group capabilities. (Architecture-related: TLS capabilities)
  ↳ No PR: [36f1092](https://github.com/openssl/openssl/commit/36f10925ff6e82dd12f6e4a05d53d360d5a475a7)
- Implemented the function of directly obtaining the algorithm (digest and mac) from the provider for DRBG_HASH and DRBG_HMAC. (Architecture-related: Provider internal interface)
  ↳ No PR: [d037551](https://github.com/openssl/openssl/commit/d037551ee3038c2625cbda65b5bc4ef290063a7b)
- Added hybrid KEM algorithms (X25519MLKEM768, X448MLKEM1024, SecP256r1MLKEM768, SecP384r1MLKEM1024) in FIPS provider. (Architecture-related: FIPS provider algorithm)
  ↳ No PR: [2e89849](https://github.com/openssl/openssl/commit/2e898497a61ee553c8e67782743feab7b62ae120)
- Enabled the ML-KEM capability in the FIPS provider, added long name identifiers for the ML-KEM-512, ML-KEM-768 and ML-KEM-1024 algorithms, and added aliases without dashes (such as MLDSA44) for the ML-DSA algorithm. (Architecture-related: Algorithm names and compatibility)
  ↳ No PR: [7c45e7a](https://github.com/openssl/openssl/commit/7c45e7a6c882f4949a12ced4b87527ba2e0be06d), [3d57bbb](https://github.com/openssl/openssl/commit/3d57bbb8ca0bfc20ca145965c1f115724a4d26c0), [c338c89](https://github.com/openssl/openssl/commit/c338c89d1616646fc34c90c48ebbac4ab691ed11)
- In deterministic ECDSA signatures, if no digest name is provided, an explicit error message is now returned instead of failing silently. (Architecture-related: external behavior)
  ↳ No PR: [8cc0a97](https://github.com/openssl/openssl/commit/8cc0a97d60f4b77def4df9fee41740ffb2fb5563)
- Removed unnecessary restrictions on ECDSA settable context parameters, now all settable parameters are always available. (Architecture-related: external behavior)
  ↳ No PR: [d244abb](https://github.com/openssl/openssl/commit/d244abb6515c3f1c68975c5d62417aff03f488b5)
- Fixed an issue with incorrect salt length parameter in TLS 1.3 HKDF key derivation, ensuring the correct prevsecretlen is used instead of mdlen to avoid potential crashes or output errors. (Architecture-related: TLS 1.3 key derivation)
  ↳ No PR: [5c91f70](https://github.com/openssl/openssl/commit/5c91f70ba8f07eeeb02b6c285479e4482443a6fe)
- Add provider running status check in the RSA KEM context creation function of the FIPS module, and correct the initialization operation type. (Architecture-related: FIPS module)
  ↳ No PR: [c262cc0](https://github.com/openssl/openssl/commit/c262cc0c0444f617387adac3ed4cad9f05f9c526), [a7c550f](https://github.com/openssl/openssl/commit/a7c550ff7696d65999891799482cbe0413907330)
- Fixed an issue where the SRP_user_pwd_set1_ids function may cause double release when memory allocation fails. (Architecture-related: public API)
  ↳ No PR: [792b2c8](https://github.com/openssl/openssl/commit/792b2c8da283d4230caa761ea6f5d050cb5795e7)
- Fix the memory leak in PKCS12_add_key_ex caused by the failure of PKCS8_add_keyusage, and ensure that the allocated PKCS#8 key information structure is released. (Architecture-related: public API memory leak repair)
  ↳ No PR: [f822a48](https://github.com/openssl/openssl/commit/f822a4866894ed8a752ad93c228fb76a8bb206e8)
- Fix DRBG's get_entropy function so that it can provide the entropy of the requested amount, not just its own strength value. (Architecture-related: DRBG entropy behavior)
  ↳ No PR: [3b7bd87](https://github.com/openssl/openssl/commit/3b7bd871c19056c8116b67dff68e0860785935eb)
- In FIPS mode, when a jitter entropy source encounters a permanent failure, the provider will now be set to an error state. (Architecture-related: FIPS behavior)
  ↳ No PR: [b9886a6](https://github.com/openssl/openssl/commit/b9886a6f3483e0525596d3b3956416282038da82)
- Fixed the problem of EVP_PKEY_print_private() failing when used with non-default provider. If only the private key is selected when exporting the key, the public key selection will be automatically supplemented. (Architecture-related: public API)
  ↳ No PR: [79c98fc](https://github.com/openssl/openssl/commit/79c98fc6ccab49f02528e06cc046ac61f841a753)
- Fixed the handling of extra input in jitter_generate, changing it to XOR mixing with the output instead of adding it directly to the entropy pool. (Architecture-related: random number generation behavior)
  ↳ No PR: [6bba373](https://github.com/openssl/openssl/commit/6bba373ec371f9706f61b1e4fe5c751809761202)
- Fixed the endianness issue of the polynomial sampling function in ML-DSA, and fixed the MSVC compilation error to support cross-platform compilation. (Architecture-related: Platform compatibility)
  ↳ No PR: [aabb69b](https://github.com/openssl/openssl/commit/aabb69b8ba13a398b75f0c86444b1cf3b8a52e4b), [5b589fc](https://github.com/openssl/openssl/commit/5b589fcdab19ab0019140a7f34c96440658ffc10)
- Fixed the problem of missing built-in provider configuration information. (Architecture-related: provider configuration behavior)
  ↳ No PR: [3a9e3b1](https://github.com/openssl/openssl/commit/3a9e3b1fb0d2d237631d40b0e4a62fb78462186a)
- Fixed Windows compilation error: changed the type of temporary registry buffer from LPCTCH to LPCTSTR in crypto/defaults.c, and added corresponding type conversion to be compatible with mingw-w64 environment. (Architecture-related: platform compatibility)
  ↳ No PR: [5c46165](https://github.com/openssl/openssl/commit/5c461650347c46fae36b449d66a893d74a1c3520)
- Fixed wide character handling and size checking issues in Windows registry configuration detection. (Architecture-related: Platform compatibility)
  ↳ No PR: [977cfc3](https://github.com/openssl/openssl/commit/977cfc3fa132a4990358e9ae0db92560d880f017)
- Fixed the problem of identifier lookup failure in ML-DSA signature verification, and added signature algorithm identifier mapping and short name alias for ML-DSA algorithm. (Architecture-related: public API)
  ↳ No PR: [1036be4](https://github.com/openssl/openssl/commit/1036be4384ba2af961fc4ce7289def47da2ec2b9)
- Updated the ASN.1 codec format of ML-KEM, changed the seed in the private key to the OCTET STRING type, and adjusted the related codec table structure. (Architecture-related: ASN.1 codec format)
  ↳ No PR: [096fde9](https://github.com/openssl/openssl/commit/096fde92e79d7d4b276b03e5b331f39b5e32de3d)
- Added two checks for ML-KEM private key import: when both seed and key are provided, check the consistency of the implicit rejection value z; when both public and private keys are provided, verify whether the redundant public key matches the copy in the private key. (Architecture-related: key import behavior)
  ↳ No PR: [b3dd681](https://github.com/openssl/openssl/commit/b3dd681f073817660ba4710516a033b6e1344b46)
- Fixed an error enumeration conflict and adjusted the serial number of SSL_R_MISSING_QUIC_TLS_FUNCTIONS from 421 to 423. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a903be9](https://github.com/openssl/openssl/commit/a903be9cae5094c8f1a04496445d41985f8f6624)
- Fixed an issue where the userinfo component was not handled correctly in the SAN URI name constraint check, now allowing URIs to contain the userinfo part. (Schema related: public API)
  ↳ No PR: [e599893](https://github.com/openssl/openssl/commit/e599893a9fec932701ca824d73a794a0c9ce02e9)
- Fixed the issue where CCM cipher suites were incorrectly allowed in the QUIC TLS API, and distinguished QUIC internal connections by adding internal flags to ensure that only the correct cipher suites are allowed. (Architecture-related: public API)
  ↳ No PR: [6e4ddab](https://github.com/openssl/openssl/commit/6e4ddabd98f6c611ab217e219d068b2b5ac1c622), [4c80bf5](https://github.com/openssl/openssl/commit/4c80bf56bb87836d9e164336919c7defb2d75a06)
- Allow default provider to use digest without NID for ECDSA signing, and fix invalid check issue in DSA signing. (Schema related: Provider behavior)
  ↳ No PR: [92540a5](https://github.com/openssl/openssl/commit/92540a5114e342afe09cb65db301654a274e1431)
- Remove the SSL_TOKEN_STORE_HANDLE type, use the opaque SSL_TOKEN_STORE instead, and remove the related public API functions SSL_CTX_get0_token_store and SSL_CTX_set1_token_store. (Architecture event: OpenSSL_Core_Headers module change)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [e732f44](https://github.com/openssl/openssl/commit/e732f4456afc67efe87fbebcc97a2c5e4cce1369), [9d6e5a6](https://github.com/openssl/openssl/commit/9d6e5a69dbaa1abb26a1b7fe1d3de74b5c15d457)
- Rename the EVP_SKEY_get_raw_key function to EVP_SKEY_get0_raw_key to follow the OpenSSL naming convention. (Architecture event: OpenSSL_Core_Headers module change)
  ↳ No PR: [17bbc16](https://github.com/openssl/openssl/commit/17bbc163831e4a936e4cca730d4fcc78e51922e4)
- In the FIPS provider, replace the signature verification API from EVP_DigestSign/Verify to EVP_PKEY_sign/verify, and remove the related API and conditional compilation logic. (Architecture-related: public API)
  ↳ No PR: [923baa1](https://github.com/openssl/openssl/commit/923baa12e149e92d2599dddbb490ed0201465bed), [ffa5465](https://github.com/openssl/openssl/commit/ffa5465e544704e56aaa895b0890a9fc7c917021)
- Reconstruct the internal implementation of the DER encoder/decoder, unify the signatures of PKCS8 and public key decoding functions, and migrate the encoding auxiliary functions to the crypto/encode_decode/ directory and expose them as public interfaces in preparation for supporting ML-KEM/ML-DSA. (Architecture-related: public API)
  ↳ No PR: [0f28638](https://github.com/openssl/openssl/commit/0f286386034b914e64ed9e60b26c49167062b13e), [c374f79](https://github.com/openssl/openssl/commit/c374f7954905643607a78a90bf09005f302637b6)
- Change the zeroing operation in the FIPS module to use the OPENSSL_PEDANTIC_ZEROIZATION macro to control it, involving scenarios such as HKDF, PBKDF2 and integrity verification. (Architecture-related: FIPS behavior)
  ↳ No PR: [f471061](https://github.com/openssl/openssl/commit/f471061721a2c36dc9ea7c3a4e685b29e00cccda), [db1d8c9](https://github.com/openssl/openssl/commit/db1d8c90d52a4f2be1afd9448368c012b8990f1e), [8d09e61](https://github.com/openssl/openssl/commit/8d09e61be6bf22bbaacda5ec53e02f938f40c76d), [01cfee2](https://github.com/openssl/openssl/commit/01cfee2cdfee8d572abc538836c2cab61069399c)
- Prefer configuring DRBG using cryptographic algorithms from the same provider as DRBG. (Architecture-related: external behavior)
  ↳ No PR: [c9a2ce6](https://github.com/openssl/openssl/commit/c9a2ce61118c7f73bc4898eedec64c2bde8bb7a0)
- Update FIPS self-test definition, change SLH_DSA to SLH-DSA, and remove redundant KEM key generation definition. (Architecture-related: public API)
  ↳ No PR: [92a54f4](https://github.com/openssl/openssl/commit/92a54f4d59ea81768af7dde9e9d9deb5ce0d6131)
- Reconstruct the signature algorithm processing logic: adjust the order of the default signature algorithm list (ML-DSA-65 takes priority), introduce min/max TLS and DTLS version range checks, add the tls_sigalg_compat function to unified version compatibility judgment, and add TLSv1.2 specific names for some algorithms. (Architecture-related: Signature algorithm processing logic reconstruction)
  ↳ No PR: [bcff020](https://github.com/openssl/openssl/commit/bcff020c36d7eecf00869261c17278bd9c54f48e)
- Removed redundant RSA encryption/decryption known answer tests in the FIPS module, because the existing RSA signature verification KAT already meets the test requirements of all RSA use cases, thereby reducing module startup overhead. (Architecture-related: FIPS self-test optimization)
  ↳ No PR: [635bf49](https://github.com/openssl/openssl/commit/635bf4946a7e948f26a348ddc3b5a8d282354f64)
- Added pairing compliance testing for ML-KEM key generation and import in FIPS mode to meet FIPS 140-3 requirements. (Architecture-related: FIPS Compliance)
  ↳ No PR: [d4f0bd3](https://github.com/openssl/openssl/commit/d4f0bd379f94e086bf6ea4d72cffc699fa667d4f)
- Add AES-XTS hardware acceleration support for x86_64 and s390x architectures, using AVX-512 and CPACF instructions to improve performance. (Architecture-related: Platform compatibility)
  ↳ No PR: [b4116b9](https://github.com/openssl/openssl/commit/b4116b93727dcc65639469828aff93f25bf281d4), [9cd4051](https://github.com/openssl/openssl/commit/9cd4051e47c8da8398f93f42f0f56750552965f4)
- Disable the use of SHA1 with strength lower than 112 bits in DH and ECDH key exchanges, and rename related FIPS directive checking functions, while skipping CMS test cases that rely on SHA1. (Architecture-related: external behavior)
  ↳ No PR: [ed68623](https://github.com/openssl/openssl/commit/ed6862328745c51c2afa2b6485cc3e275d543c4e)
- Refuse to import private keys that fail the PCT test, and add a validate method to the provider to encapsulate the PCT test. (Architecture-related: provider validate method)
  ↳ No PR: [2ea9903](https://github.com/openssl/openssl/commit/2ea9903c160fe4212b07ec8af630071e35098ceb)
- Update SSL error code definition, add DOMAIN_USE_ONLY error code and adjust the number of LISTENER_USE_ONLY. (Architecture-related: public API)
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [745a779](https://github.com/openssl/openssl/commit/745a779fb2aa971e85331d18cacac5ce89384aab)
- Update the error dock file and error string table, and remove error code definitions that are no longer used. (Architecture-related: public API)
  ↳ No PR: [605b82d](https://github.com/openssl/openssl/commit/605b82d7eedfb875a586f031286a87a73f0bad20)
- Updated error code definitions, adjusted numbers and added ML-DSA related error codes. (Architecture-related: public API)
  ↳ No PR: [cedc5bc](https://github.com/openssl/openssl/commit/cedc5bcce2d11607fca748fa089656fec0340649)

### Application Layer (CLI Tools)
- Added the CMS_NO_SIGNING_TIME flag to allow the creation of CMS SignedData signatures without signing time attributes, and added the -no_signing_time option to the cms command line tool. (Architecture-related: public API)
  ↳ No PR: [34ea176](https://github.com/openssl/openssl/commit/34ea176abfbd4349bc36179eb8a6b80536e820b2)
- Roll back the OPENSSL_version API changes, restore the original format of the returned directory path, and adjust the version command output. (Architecture-related: public API)
  ↳ No PR: [f4c4674](https://github.com/openssl/openssl/commit/f4c467452694e1211395d17c2c027d99c35ee1e1)
- Fixed memory leak and changed the default encryption algorithm from DES-EDE3-CBC to AES-256-CBC. (Architecture-related: public API)
  ↳ No PR: [d48874a](https://github.com/openssl/openssl/commit/d48874ab477be0fa3df11bfcc38c043b8f7ab8e2)
- Fix the order of QUIC encryption level enumeration to conform to the INITIAL, 0RTT, HANDSHAKE, 1RTT order specified by RFC 9000 and 9002. (Architecture-related: public API)
  ↳ No PR: [89e2c6f](https://github.com/openssl/openssl/commit/89e2c6f61ebbf2ee0b0b742eb66cba0583fc6813)
- Update the documentation to clarify that for the SHAKE algorithm, the xoflen parameter is now required, and adjust related instructions. (Architecture-related: External behavior: xoflen parameter is required)
  ↳ No PR: [ffa1cf6](https://github.com/openssl/openssl/commit/ffa1cf69aaf6a2eeabb96cc1326aa4ac24e7f0d9)
- When the fipsinstall tool detects that the loaded FIPS provider is version 3.0.x, it saves the status indicator by default to maintain backward compatibility, and adds support for the x942kdf_key_check option. (Architecture-related: FIPS configuration behavior)
  ↳ No PR: [01244ad](https://github.com/openssl/openssl/commit/01244adfc66aadc1fc3c6cfb8c96a0a6da3d4a3e)

## Routine Changes

### New features
- s_server now supports reading HTTP requests through early data, and removes conflicting restrictions between options such as -early_data and -www.
  ↳ No PR: [f37dea4](https://github.com/openssl/openssl/commit/f37dea418b777478bee7b1d812e3adb5fb71d0ee)
- Added new internal function ossl_serial_number_print, used to print certificate serial number (decimal and hexadecimal), and updated related calls and header file declarations.
  ↳ No PR: [935f6e6](https://github.com/openssl/openssl/commit/935f6e63c96b44a03e12a7272b01c23956f3d4f3), [c90451d](https://github.com/openssl/openssl/commit/c90451d89d55ba42f2be01065361030f26f3e852)
- Implemented key length checking in X9.42 KDF to ensure input keys meet the 112-bit length requirement (only in FIPS mode).
  ↳ No PR: [fc68cf2](https://github.com/openssl/openssl/commit/fc68cf21b572bc7fc76a39e4ec150d5d612f02e8)
- Added Windows installation context information item for openssl info command.
  ↳ No PR: [5f3fefe](https://github.com/openssl/openssl/commit/5f3fefe2f3b1103299eda85831908508d8bb2114), [6bb62ab](https://github.com/openssl/openssl/commit/6bb62ab82682b9e19d594eb8fd52a5a560ba65f3)
- Added a -cipher option to the req command, allowing users to specify the private key encryption algorithm, and changing the default encryption algorithm from DES-EDE3-CBC to AES-256-CBC.
  ↳ No PR: [bca1bb2](https://github.com/openssl/openssl/commit/bca1bb297778932c1e682166aa4780ecc96f0a0a)
- Changed the default encryption algorithm applied by req, cms and smime from DES-EDE3-CBC to AES-256-CBC, and removed the related conditional compilation protection.
  ↳ No PR: [539b17b](https://github.com/openssl/openssl/commit/539b17b6580f2ca235b5e1db529e87793b8a807c)
- Keep a reference to the user's original SSL object when creating a QUIC SSL connection.
  ↳ No PR: [f88c2f2](https://github.com/openssl/openssl/commit/f88c2f2d171871dce8b72fd2694cd061dff21f7d)
- Added the function of setting local address for BIO_dgram_pair, and fixed the processing of local address when destroying and writing.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [16a1900](https://github.com/openssl/openssl/commit/16a19002d8a1937493b28ae49e506460c0569c88)
- Add a high-level check for RSA keys only for the -verifyrecover option of pkeyutl.
  ↳ No PR: [abad748](https://github.com/openssl/openssl/commit/abad748da8d27508d4cfb74f86786167bd4ba0c4)
- Negotiated TLS 1.3 group information is now always shown when printing ephemeral keys, no longer client-only and only in -brief mode.
  ↳ No PR: [1a077b3](https://github.com/openssl/openssl/commit/1a077b38c98382e9997fe9565ddacb8b5c815418), [280c1d0](https://github.com/openssl/openssl/commit/280c1d0f3ed0e3d9043f5e031e2631f5a3f4e636)
- Enhanced QUIC address verification token functionality, including token generation, encryption, parsing and verification.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2b271d0](https://github.com/openssl/openssl/commit/2b271d0f85bd720f137abd55bbab247c6dd0d176), [f851d8d](https://github.com/openssl/openssl/commit/f851d8dfccf687086a608a22e1d32bd728d1fcfa), [73b49e6](https://github.com/openssl/openssl/commit/73b49e65fcb075d624db6bc637781b53408bd76f)
- Added IPv6 support to the QUIC interop demo program, the server uses a dual-stack socket to listen to both IPv4 and IPv6.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [e9aa0b6](https://github.com/openssl/openssl/commit/e9aa0b6c0efe65e712bf87a9b20acb46d13d7e85)
- Add opaque key support to openssl command line tools: enc command supports EVP_SKEY object, list command supports EVP_SKEYMGMT.
  ↳ No PR: [00bdee8](https://github.com/openssl/openssl/commit/00bdee8974dee8215231512d31ea2959e31bf64a), [b9d919f](https://github.com/openssl/openssl/commit/b9d919f697270ea38818239b18eb71eb6b5e4d8c)
- Check OSSL_PROVIDER_do_all return value and output error message in case of failure, and add list_tls_groups function to list TLS groups.
  ↳ No PR: [5b94140](https://github.com/openssl/openssl/commit/5b94140b52378c1160c1192c662de07b35aef92e)
- Added skeyutl command line tool for symmetric key management operations.
  ↳ No PR: [df93d13](https://github.com/openssl/openssl/commit/df93d1327a87e294fa8850aa83acd7305402e798)
- Increase the reference count for QUIC tokens to avoid being accidentally released while the client is waiting to send an Initial frame.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [fce82b6](https://github.com/openssl/openssl/commit/fce82b6ccc6b0461fa2f028fc32e8824dc7da0d1)
- In the FIPS module, perform ML-KEM self-test only when ML-KEM is enabled.
  ↳ No PR: [fc225d9](https://github.com/openssl/openssl/commit/fc225d9fb72be4689c6da3ededdd7974b2865947)
- Add support for ML-DSA signature algorithm in SSL tracking function.
  ↳ No PR: [a0fc1ff](https://github.com/openssl/openssl/commit/a0fc1ff3481375e710136bbd9a2c45cc8749875f)
- The dgst command adds support for one-time signature algorithms, and reconstructs the printing logic of output and verification results.
  ↳ No PR: [7cf5300](https://github.com/openssl/openssl/commit/7cf5300e6b7e2686f0794e4b7424d8171c1ecc52)
- Added tracking support for provider initialization, destruction and other operations, and reconstructed the random byte function interface.
  ↳ No PR: [11539fd](https://github.com/openssl/openssl/commit/11539fd7346736fe789dffe731bd311b8d59fc9d)
- Added QUIC interoperable ALPN client sample program.
  ↳ No PR: [2858149](https://github.com/openssl/openssl/commit/2858149e4450b7a7f7ecac94b462bc7eed074d0c)
- Added session recovery support to the hq-interop example, session caching can be enabled via the environment variable SSL_SESSION_FILE.
  ↳ No PR: [d978e5f](https://github.com/openssl/openssl/commit/d978e5fb06387fe923b564875714ff9bebdcc6e9)
- Added QUIC server support and HTTP3 demo server based on nghttp3, and fixed format conversion specifiers in summary demos.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [73977a0](https://github.com/openssl/openssl/commit/73977a04241e5bff87a86f0aa0f444b0c7c79492)
- Added a QUIC non-blocking server example program.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [d9d4d84](https://github.com/openssl/openssl/commit/d9d4d84ceb01e70b7d9fc01528a9f0d0ab6dd352)
- Added blocking QUIC server examples, and updated client examples to use the new SSL_write_ex2 interface.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [dad45ea](https://github.com/openssl/openssl/commit/dad45ea769dc51e45b3aee5a376a3ee306704ac7)
- Recorded support instructions for the new callback SSL_CTX_set_new_pending_conn_cb in CHANGES.md.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [55f3968](https://github.com/openssl/openssl/commit/55f3968a4972b0dc2bc88a70dc772474658714ac)
- The instructions for the new provider random hook are recorded in CHANGES.md.
  ↳ No PR: [d466672](https://github.com/openssl/openssl/commit/d46667284d193ceb3242ebf17422e62b1c837c60)
- Documented instructions for changes to the default DRBG implementation in CHANGES.md.
  ↳ No PR: [0ba139f](https://github.com/openssl/openssl/commit/0ba139f4b9db144df5c94bce9f6e70bedf182efb)
- Documented instructions for VAES/AVX-512 support for AES-XTS in CHANGES.md.
  ↳ No PR: [9688973](https://github.com/openssl/openssl/commit/96889735960260c6e4b5d9bc2d298e729c7f7269)
- Added Windows platform support to the QUIC server example, and added error checking for SSL_set_blocking_mode.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [1ed2ef0](https://github.com/openssl/openssl/commit/1ed2ef07b352c3f471337fe03bfbacd541dd4947)
- Added multiplexing tests to QUIC interop testing workflow.
  ↳ No PR: [e258454](https://github.com/openssl/openssl/commit/e258454479d5c253cb94a9f32a538d5792e4ebd0)
- Split the QUIC interop test CI job into two independent jobs, client and server, to limit the number of jobs.
  ↳ No PR: [4f37e54](https://github.com/openssl/openssl/commit/4f37e543d9e61b999a2c9905a1d89463b7964780)
- Added manual trigger parameters in coveralls CI workflow to support specified branches and additional configuration.
  ↳ No PR: [78d2528](https://github.com/openssl/openssl/commit/78d252889b7d126b9baf5075db6990658c87f85b)
- Enabled extended EVP testing in coveralls CI workflow.
  ↳ No PR: [de194a6](https://github.com/openssl/openssl/commit/de194a607435e5a109fe2ace0e6c8f7aa7c7a724)
- Added CI run check workflow for no-ml-dsa compile option.
  ↳ No PR: [4ad13c4](https://github.com/openssl/openssl/commit/4ad13c48d74a41bcb369b0cb0760699002f8e4e9)

### bug fixes
- Fixed compilation errors caused by missing winsock.h indirect inclusion, and added necessary header file references in relevant source files and header files.
  ↳ No PR: [0022bc8](https://github.com/openssl/openssl/commit/0022bc81a9408a82557f0af33852246d60ea48d3)
- Fixed undefined behavior caused by not converting char type parameters to unsigned char when using ctype.h functions.
  ↳ No PR: [99548cd](https://github.com/openssl/openssl/commit/99548cd16e9dfd850a3958e417b9e02950f208f4)
- Fixed two issues in EC parameters to legacy control conversion: fix_ecdh_cofactor correctly returns values in POST_PARAMS_TO_CTRL state, and evp_pkey_ctx_setget_params_to_ctrl allows returning 0 as a valid return value.
  ↳ No PR: [2aaef03](https://github.com/openssl/openssl/commit/2aaef03339a88e5d693f278406a889657b10fd2d)
- Fixed the problem of BIO reference counting processing during QUIC connection cleanup, which releases network read and write BIO objects before releasing the port.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [d2ee7ce](https://github.com/openssl/openssl/commit/d2ee7ceff05e9bcc00a0f88a4cf85e32464f4b9a)
- Fixed the release order of TLS objects during QUIC connection cleanup, ensuring that TLS is released before the channel is released.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [882c77e](https://github.com/openssl/openssl/commit/882c77e93e8659be6c15523fcd6c912c67135e90)
- Fixed the QUIC listener release problem, added a special release function, and solved the memory leak that caused the listener to be unable to be released when pre-allocating connection objects.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2e58264](https://github.com/openssl/openssl/commit/2e582648c50c9d5541301e353e76f1b910eb9fc5), [6f38c59](https://github.com/openssl/openssl/commit/6f38c59850105f5bf6f6780c73da6f0333f87582)
- Fixed multiple bugs in the QUIC server API, including memory leaks and inbound connection setup issues.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [88804f3](https://github.com/openssl/openssl/commit/88804f3181871e11c03ac6f0055c879708cba1f1)
- Fixed bug with QUIC server-side default XSO handling.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [c69ce7f](https://github.com/openssl/openssl/commit/c69ce7fcf1d991e54a2ade3d787029f978796443)
- Fixed reference counting issues with QUIC listeners, correctly releasing listener objects when cleaning up connections and adjusting lock operations.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f4cfa1b](https://github.com/openssl/openssl/commit/f4cfa1b9ccc0b98affa98abb95f36ca7ae4dd711)
- Fixed a conditional error in QUIC server-side default stream creation.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [bf8ce68](https://github.com/openssl/openssl/commit/bf8ce68c331f475630704eba17bcf86926b52777)
- Fixed the QUIC APL function to use the correct prologue, updated the context checking method of multiple functions, and added error handling for listener in the control function.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [38df4b1](https://github.com/openssl/openssl/commit/38df4b1976e2b6b316a0c343ede2b0419c4f8243)
- Fixed a possible assertion failure or deadlock in QUIC reactors when waiting cannot be done.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [390403a](https://github.com/openssl/openssl/commit/390403abf8d15d11ca953551bc4a6e0cee6b6b33)
- Fixed the assignment of net_read_desired in QUIC port subtick so that it is determined based on the port running status, ensuring that the reactor correctly waits for the listening port.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f1ade90](https://github.com/openssl/openssl/commit/f1ade90a662dc2bd1084307a639f964751127fce)
- Revised connection status check in QUIC write path to be compatible with s_client's SSL_pending and SSL_has_pending handling.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [8a6bb6b](https://github.com/openssl/openssl/commit/8a6bb6b639a47cca2b5a505737f7e23d6fdbbb39)
- Ensure incoming stream data can still be drained after the connection is closed.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [05e0eae](https://github.com/openssl/openssl/commit/05e0eae2020edd9318eeb7e2e2360481e4dbae43)
- Fixed an issue where a default stream could still be created after a QUIC connection was terminated, now immediately returning a protocol closed error.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2176e04](https://github.com/openssl/openssl/commit/2176e0467e5b382da2e663a30adb76fa289c0879)
- Added default domain flags support for the QUIC engine, deciding whether to enable the notifier based on domain flags, and passing reactor flags to reactor initialization.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [ae26f1e](https://github.com/openssl/openssl/commit/ae26f1eed69e6b24c1e8fd8663cc817eae97b1f4)
- Optimized the notification mechanism of the QUIC channel to other threads in scenarios such as termination and timeout, and fixed the encoding logic of the initial connection ID when retrying the connection.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [960b844](https://github.com/openssl/openssl/commit/960b8449cbe53f3d77cc7a59120a4e6c7c2828a9)
- QUIC objects now require the blocking support flag to be included in domain flags to use blocking mode.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2c70693](https://github.com/openssl/openssl/commit/2c70693e9267d6bbbe3645a7c8a2ee1c0bd70d80)
- Added thread-supported conditional compilation protection for mutex assignments in QUIC listener creation.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2c9953b](https://github.com/openssl/openssl/commit/2c9953bbd35bf0da36c224b0c8dbd3847adbe5db)
- Fixed the blocking operation registration logic of inter-thread notification in SSL_poll to ensure that outstanding items are properly cleaned up and the result count is returned.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [53225c9](https://github.com/openssl/openssl/commit/53225c9c3d7d0cf66748f012a2590fc668ef8414)
- Fixed memory leak with wrong path in rsa_cms_sign function, explicitly freeing allocated ASN1_STRING variable when X509_ALGOR_set0 call fails.
  ↳ No PR: [5efc57c](https://github.com/openssl/openssl/commit/5efc57caf229748fd4f85b05463f96b11679100d)
- Added a check on the null pointer returned by OPENSSL_strdup in rehash.c to prevent undefined behavior when memory allocation fails.
  ↳ No PR: [a5cd06f](https://github.com/openssl/openssl/commit/a5cd06f7fff3b4484946812191097b5e080b7610)
- Fixed an issue that could cause a null pointer dereference when checking a CRL due to issuer being a null pointer.
  ↳ No PR: [9d71a66](https://github.com/openssl/openssl/commit/9d71a6622be15592ad75dd4e6c5816c9042611e9)
- Fixed the check for error return codes in http_server_init(), changing the condition from < 0 to <= 0.
  ↳ No PR: [7ec5d59](https://github.com/openssl/openssl/commit/7ec5d5916bc8563935901c027fe56b6644787d10)
- Fix issue in OSSL_HTTP_adapt_proxy() handling escaping IPv6 host addresses and whitespace characters in no_proxy list.
  ↳ No PR: [fe004a0](https://github.com/openssl/openssl/commit/fe004a09acdf65557a1ddd6011a76374b3d9d3ec)
- Fixed the buffer boundary problem in password callback processing, ensuring space is reserved for the null terminator and verifying the callback return length to prevent out-of-bounds access from causing a crash.
  ↳ No PR: [5387b71](https://github.com/openssl/openssl/commit/5387b71acb833f1f635ab4a20ced0863747ef5c1)
- Fix the null pointer dereference and memory leak that may be caused by EVP_MD_fetch failure in the PBMAC1 implementation in PKCS#12, and add null value checking and resource release.
  ↳ No PR: [f60b3c5](https://github.com/openssl/openssl/commit/f60b3c5fdcf75fc3e9a257c2f67867ffae63006b)
- Fixed the problem of missing NIP flag when SHAKE empty message squeeze on s390x platform, and added corresponding tests.
  ↳ No PR: [dc5afb7](https://github.com/openssl/openssl/commit/dc5afb7e87ee448f4fecad0dc624c643505ba7f1)
- Fixed the processing logic of the s390x SHA3 absorption function when using zero-length data to avoid incorrect calls to the KIMD instruction causing subsequent hash output exceptions.
  ↳ No PR: [979dc53](https://github.com/openssl/openssl/commit/979dc530010e3c0f045edf6e38c7ab894ffba7f2)
- Fixed multiple issues with SSL_poll in QUIC, including stream completion detection, immediate mode polling and failure event result_count reporting, and optimized related implementations.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [84dbca4](https://github.com/openssl/openssl/commit/84dbca4df00ccc08ac7917d7dde05e58e85efd60), [8913420](https://github.com/openssl/openssl/commit/89134200b8f1c122fa4795ab3a69615d9bbab51d), [b7e1d37](https://github.com/openssl/openssl/commit/b7e1d375f1c14804882dbbc247a967cc32e1f61b) | No PR: [c8127df](https://github.com/openssl/openssl/commit/c8127df04cae8d6a0d913e6e5c760062817a202e)
- In issuer serial number output for AC target extension, print <none> when issuer name or UID is empty.
  ↳ No PR: [7a4f0c6](https://github.com/openssl/openssl/commit/7a4f0c6aeaaaf8c78dad518b0113288069c5d280)
- Fixed the issue where gcm_ghash_4bit was not declared when building using OPENSSL_SMALL_FOOTPRINT under ARM architecture and the ghash function pointer was set to NULL when defining this macro.
  ↳ No PR: [2a53df6](https://github.com/openssl/openssl/commit/2a53df6947e195ac08bc04c9d2fec1fed977668f)
- On Windows platforms, ensure WSAStartup is initialized before calling WSASocketA, and optimize error handling.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [44aab1f](https://github.com/openssl/openssl/commit/44aab1ff84abf1342bbb6dcbc5fea752b4f49de5)
- Added QUIC lock calls to functions called from poll_translate_ssl_quic to ensure thread safety.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [5031f1b](https://github.com/openssl/openssl/commit/5031f1b196446c6b41d5411443e04fd1d9a06aa7)
- Handle the situation where the connection object may be NULL in the QUIC server scenario, add NULL pointer checking and processing, and adjust the lock mechanism and timeout calculation logic.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f23da50](https://github.com/openssl/openssl/commit/f23da50318e26f1f7b7fe2d0615f08f89133795d), [48db230](https://github.com/openssl/openssl/commit/48db230a88975fd5b07da0e26f1fdb33c17c4bfc)
- Ensure that the QUIC engine is always scheduled, regardless of whether the connection has been started or terminated.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [4af6bcd](https://github.com/openssl/openssl/commit/4af6bcd69cfc6114c8eb195147537bd4518962da)
- Fixed the duplicate engine reference problem in ossl_ec_key_dup.
  ↳ No PR: [ffc5a29](https://github.com/openssl/openssl/commit/ffc5a29608fdbd346e340a65a43ebadc90bd4a33)
- Fix the SMIME type setting of AuthEnvelopedData so that it correctly outputs authEnveloped-data.
  ↳ No PR: [7f62ada](https://github.com/openssl/openssl/commit/7f62adaf2b088de38ad2e534d0bfae2ff7ae01f2)
- Fixed signed and unsigned comparison issues in jitter random number generation.
  ↳ No PR: [01ec59d](https://github.com/openssl/openssl/commit/01ec59defdbd6643ae881864097ec579ddf6dfb1)
- Fixed dereference issues caused by null pointers in EC public key encoding and point conversion functions.
  ↳ No PR: [8ac42a5](https://github.com/openssl/openssl/commit/8ac42a5f418cbe2797bc423b694ac5af605b5c7a)
- Fixed the issue where the set_ctx_params function in the RSA signature algorithm returns incorrect values for unknown parameters, making it consistent with other algorithms and always returns 1.
  ↳ No PR: [349815b](https://github.com/openssl/openssl/commit/349815b57f0d19b040ad8733975b7b5698570dc3)
- Add OSSL_ prefix to internal list macros to avoid conflicts with BSD macro definitions in system header files.
  ↳ No PR: [c4ec708](https://github.com/openssl/openssl/commit/c4ec708bd58715fab10b8a6085ac89d79615b250)
- Fixed the problem that the rsasve_recover function did not correctly set the output length after successful decryption, and added a validity check for the output buffer length.
  ↳ No PR: [0f95168](https://github.com/openssl/openssl/commit/0f9516855e3139ef999b58f2fa551afb3b6c2b15)
- Fixed the lock acquisition and release sequence issue in FIPS CRNG test.
  ↳ No PR: [348c928](https://github.com/openssl/openssl/commit/348c928d66e099f9814e7a63e4618e3aecf7286c)
- Fixed the problem of incorrect triggering of ECDH cofactor FIPS indicator, and fixed related memory leaks; also added test cases covering all parameter combinations.
  ↳ No PR: [2f362e9](https://github.com/openssl/openssl/commit/2f362e99a1178263c7102474f0190836166f416d), [12d14de](https://github.com/openssl/openssl/commit/12d14de641c299ec080edc521f7080acc44e366f), [1f0cb85](https://github.com/openssl/openssl/commit/1f0cb850473048eef5dc597d8cd42dd7c3cf5a5f)
- Fixed the processing order error in the pkey command when the input file and output file are the same file.
  ↳ No PR: [c8359ab](https://github.com/openssl/openssl/commit/c8359abb884daa6230cd1c1514ff188c93cfc914)
- Fixed the processing logic in the dhparam command when the input file and output file are the same file, ensuring that the input is read first and then the output is opened to avoid the file being cleared in advance.
  ↳ No PR: [9ae1e65](https://github.com/openssl/openssl/commit/9ae1e6596f04f93d1be99c08ccfcb54f39fcc093)
- Fixed a possible processing error in the dsaparam command when the input file and output file are the same file.
  ↳ No PR: [3218998](https://github.com/openssl/openssl/commit/32189981a3eb26b7172b4b917f37d301b8d5e65e)
- Fixed the processing problem in the OCSP tool when the requested input file and output file are the same file.
  ↳ No PR: [421e8d7](https://github.com/openssl/openssl/commit/421e8d7af8bad6a7d11c219fa48cb51fc1b6ffe9)
- Fixed the processing logic when the input and output of the ecparam and pkeyparam tools are the same file. Read the input first and then open the output to avoid overwriting; at the same time, correct the return value of the list curve function and the return value check of parameter printing.
  ↳ No PR: [1dbb67c](https://github.com/openssl/openssl/commit/1dbb67c4f1a3aec7f4026e43257b33ffad665ba5)
- Fix the error in the pkcs8 command when the input and output are the same file, adjust the opening timing of the output file, and ensure that the input is read first and then the output is written.
  ↳ No PR: [d5c4a8a](https://github.com/openssl/openssl/commit/d5c4a8aecca691506824326f43be06ad36216c11)
- Fixed the processing logic in the storeutl tool when the URI is the same as the output file path, delaying the opening of the output file until inside the process function.
  ↳ No PR: [187952d](https://github.com/openssl/openssl/commit/187952d449e4ec6c4fe71a537fa26005556e461a)
- Fix the processing when PBKDF2 PRF is missing in PBMAC1, use hmacWithSHA1 by default, and add null pointer check.
  ↳ No PR: [f3652df](https://github.com/openssl/openssl/commit/f3652dff2faab0c0a197fa140984103c0b0a5e88)
- Fixed the memory leak caused by not releasing the buffer when EVP_VerifyUpdate failed in the PKCS7_signatureVerify function, and moved the release operation to the error handling path.
  ↳ No PR: [d8b7a6e](https://github.com/openssl/openssl/commit/d8b7a6eae9383fced785b9f4e2f24da0dc0a082d)
- Fix the memory leak caused by the failure of sk_ASN1_UTF8STRING_push in the save_statusInfo function, and add the corresponding release operation.
  ↳ No PR: [0a2a8d9](https://github.com/openssl/openssl/commit/0a2a8d970f408af595fd699b2675ba45a26c169b)
- Fix the memory leak in the ossl_quic_calculate_retry_integrity_tag function to ensure that the wrong path correctly releases the allocated resources.
  ↳ No PR: [e8d9635](https://github.com/openssl/openssl/commit/e8d963594f8e2be6428e6244eee37e31ad7eca36)
- Repair the network read and write expectation judgment function in the QUIC listener, and use the reactor in ctx.obj instead of the channel reactor in ctx.qc.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [76af88a](https://github.com/openssl/openssl/commit/76af88a6218f6f4ed23cc38bcbc6a723fa74816c)
- Fixed a memory leak caused by the tls_parse_ctos_psk function not releasing sess in the wrong path.
  ↳ No PR: [b2474b2](https://github.com/openssl/openssl/commit/b2474b287fbc7a24f0aa15e6808c6e3ef8287f23)
- Fixed build failure caused by missing sendmmsg/recvmmsg on AIX platform.
  ↳ No PR: [c579568](https://github.com/openssl/openssl/commit/c5795689c93f95508e8da97d5c766a793bad3b58)
- Roll back the workaround previously introduced to circumvent the unreliability problem of ftell in Windows text mode.
  ↳ No PR: [ed3ce75](https://github.com/openssl/openssl/commit/ed3ce7545797e2c7202a6fcbf83c8bba3ead460d)
- Open PEM files in binary mode on Windows platforms, avoiding MSVCRT's ftell text mode issues.
  ↳ No PR: [4f20de0](https://github.com/openssl/openssl/commit/4f20de0c8adc9cdcd1475155d467f66980915ab3)
- Unify the calculation method of the maximum alignment value in the TLS read and write buffer, and fix the inconsistency between the two.
  ↳ No PR: [fc0e794](https://github.com/openssl/openssl/commit/fc0e79461f05406d52fca564204cb8a48f983eb5)
- Fix ambiguity in signature algorithm output, change ed25519 and ed448 to lowercase, and add unambiguous name output for algorithms such as RSA-PSS and brainpool.
  ↳ No PR: [f30d6ba](https://github.com/openssl/openssl/commit/f30d6ba455e06572250e75132045eedde5d1daf0)
- Fixed the logical error in the host name, email and IP matching check in the check_cert_attributes function to ensure correct judgment of the matching results.
  ↳ No PR: [1a93be1](https://github.com/openssl/openssl/commit/1a93be1eab54acc720a3e645c11dc84002285879)
- Fixed multiple incorrect uses of BN_check_prime: added error checking in the prime command, and fixed return value assertions in tests.
  ↳ No PR: [b2b995e](https://github.com/openssl/openssl/commit/b2b995ec2d95a67b9c21012a25cadd94e15e6a17)
- Fixed the issue of incorrect check of multiple function return values to ensure correct detection of failure situations.
  ↳ No PR: [8baf61d](https://github.com/openssl/openssl/commit/8baf61d51b6cdbb97ad1386cb38dd91769dbff3c)
- Add checks for empty passwords and invalid block sizes in the block size check function of speed.c to avoid division by zero errors.
  ↳ No PR: [59f5f6c](https://github.com/openssl/openssl/commit/59f5f6c73cd2e1e2bd8ef405fdb6fadf0711f639)
- Fixed the issue where the openssl speed -evp command fails when decrypting benchmark tests on AEAD ciphers (such as CCM, GCM, OCB, SIV). Now encryption and decryption (whether or not AAD is included) can be performed correctly.
  ↳ No PR: [607a46d](https://github.com/openssl/openssl/commit/607a46d003f472d4bce646f3df6e85725094d68a)
- Fixed the issue of missing line breaks after printing Full Name.
  ↳ No PR: [e899361](https://github.com/openssl/openssl/commit/e899361b982651dfa2316e06e56637bc21624ce2)
- Fixed the memory leak caused by the failure of sk_GENERAL_NAME_reserve in the copy_issuer function, and released ialt in the wrong path.
  ↳ No PR: [fa856b0](https://github.com/openssl/openssl/commit/fa856b0ce0f527d2f80c10c8c288201ace4a9efa)
- Add return value checking for SLH_DSA hash function and pass error status to all calling functions to enhance robustness.
  ↳ No PR: [30a55b0](https://github.com/openssl/openssl/commit/30a55b0cf19121e03c300b47e730e06d6e2311b3)
- Fixed a segmentation fault caused by accessing a released stream structure when calling SSL_stream_reset after receiving the FIN bit on a QUIC stream object. The state where the stream has received data is considered to be write complete, allowing correct reset.
  ↳ No PR: [bbfffbc](https://github.com/openssl/openssl/commit/bbfffbcaf38dff61fe7a1fcbfa6af9a818e1e188), [15c6580](https://github.com/openssl/openssl/commit/15c6580a76814fb67bff07b9247bb97d40240011)
- Fix an issue with the -verifyrecover operation in pkeyutl that incorrectly checks non-original input lengths, and enhance error messages when signing/verifying input is too long.
  ↳ No PR: [fe07cbf](https://github.com/openssl/openssl/commit/fe07cbf9c324a63f8141cfa6ef7f14a42bce4ef4), [1ee9061](https://github.com/openssl/openssl/commit/1ee906143c0b0ebb6bcbeb87277833a665e79836)
- Fixed a memory leak in the cmd_RecordPadding function caused by early exit without releasing the internal string copy.
  ↳ No PR: [0abbd3e](https://github.com/openssl/openssl/commit/0abbd3e5ac0a3a7af69849b1a5010b4f0616ca37)
- Fixed the problem that when generating stream frames, the header size under high stream id was calculated incorrectly due to the stream id being set too late, and the frame could not be put into the data packet.
  ↳ No PR: [ba6f115](https://github.com/openssl/openssl/commit/ba6f115ccfbb63fbeb2bc8df3c07918a7a59a186)
- Fix the check logic of the -peerkey option in pkeyutl: add verification of matching of peer public key and private key types, correct decapsulate calling parameters, and adjust the conditional judgment of raw key operation.
  ↳ No PR: [ddae593](https://github.com/openssl/openssl/commit/ddae593a92b7b451208de42a4b6f25ba30bb41e6)
- Fix memory leak in dsa_gen function, ensure local variable dsa is released on early exit.
  ↳ No PR: [f4550fb](https://github.com/openssl/openssl/commit/f4550fb5b518d2b910222bca2317d813cf092b53)
- Fix the problem in pkeyutl that pkey is released repeatedly on multiple wrong paths, and fix the memory leak in -verifyrecover error case.
  ↳ No PR: [47a80fd](https://github.com/openssl/openssl/commit/47a80fd2034cd4314d3b4958539dcd3106087109)
- Fixed the issue in the sm2_sig_verify function where BN_CTX_end was incorrectly called when memory allocation failed, and adjusted the allocation order of EC_POINT_new to ensure that BN_CTX_start is called first.
  ↳ No PR: [93bfe97](https://github.com/openssl/openssl/commit/93bfe97c5be0ca575411b39c9dec1103caa82f51)
- Fix potential memory leak in ecx_gen_init caused by not properly releasing copied parameter memory when ecx_gen_set_params fails.
  ↳ No PR: [98be2e8](https://github.com/openssl/openssl/commit/98be2e8fb60aaece2e4c3d42e87671fe22c081a2)
- Fixed a memory leak caused by incorrect cleaning of internal parameters during DSA key generation initialization.
  ↳ No PR: [d7e8f6f](https://github.com/openssl/openssl/commit/d7e8f6f7816f2be3ab5e498d180424940fd58695)
- Fixed a conditional error in parameter checking in dh_cms_set_peerkey() to ensure that only missing parameters are allowed to pass.
  ↳ No PR: [02e72cc](https://github.com/openssl/openssl/commit/02e72ccffacf2d01295810798ca1c86a438ee712)
- Fixed QUIC datagram length check logic, now correctly discards datagrams smaller than 1200 bytes.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2f01b09](https://github.com/openssl/openssl/commit/2f01b094080d2e468778ef028fa549975fd40901)
- Fixed the problem of discarding the wrong packet number when retrying after version negotiation. Ensure that packet 1 is discarded instead of packet 0 when retrying after version negotiation to trigger the initial packet retransmission.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [4d29127](https://github.com/openssl/openssl/commit/4d2912749e4e4c0c2ace3b95cc26a3d26f768316)
- Fixed an issue where the genpkey command could leave an empty file when the encryption password did not match, now the key is written to the memory buffer first and the actual output file is only written on success.
  ↳ No PR: [21f72fa](https://github.com/openssl/openssl/commit/21f72fa4c8534e918b5cb1b7612a6682d9932977)
- Improved jitter RNG's handling of additional inputs, adding additional inputs to the random pool before obtaining entropy, and fixed related error handling.
  ↳ No PR: [4d41cc9](https://github.com/openssl/openssl/commit/4d41cc910306868285b89bd4b95d79bac693a630)
- Fixed a duplicate release problem that may occur when the CRL reference count fails to increase in ossl_cms_get1_crls_ex().
  ↳ No PR: [c4b30d9](https://github.com/openssl/openssl/commit/c4b30d9c6d03ddc6e6f03708bc2c5528362cf03c)
- Fixed multiple issues in the QUIC demo server, including buffer overflows, uninitialized variables and resource leaks, and improved stream closing and URL handling logic.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [b8e462c](https://github.com/openssl/openssl/commit/b8e462c8e3ae7171912709a10cea505fa1fe62d3), [6bae611](https://github.com/openssl/openssl/commit/6bae611c99f97a956032da64d8b64e5ee7b53a2b)
- Fix memory leak caused by RAND_POOL not being released when entropy pool mixing fails.
  ↳ No PR: [c5257fd](https://github.com/openssl/openssl/commit/c5257fd8d0b37a615484e937289b28ebe2c87ac9)
- Fixed originator certificate leak issue in cms application.
  ↳ No PR: [24dd635](https://github.com/openssl/openssl/commit/24dd635efff48a24daf1e38a256550253225a28e)
- Fixed an issue that would cause a segfault if the initiator flag was set when using key negotiation for CMS encryption. A clear error message will now be returned.
  ↳ No PR: [894e69e](https://github.com/openssl/openssl/commit/894e69e747a93a1f166891f5f029b78c68088f50)
- Added a check for pctx being empty in EVP_DigestVerify to prevent crashes caused by null pointer dereference.
  ↳ No PR: [82e7a11](https://github.com/openssl/openssl/commit/82e7a1130a7d10f4e15c19676a680990b5e3f8fe)
- When pushing the algorithm, decide whether to set the store parameter to NULL based on the no_store flag to correctly handle the no-storage scenario.
  ↳ No PR: [b3bb214](https://github.com/openssl/openssl/commit/b3bb214720f20f3b126ae4b9c330e9a48b835415)
- Fixed the issue where the -naccept option in s_server caused the listening socket to not be closed in time.
  ↳ No PR: [113c12e](https://github.com/openssl/openssl/commit/113c12ee8cee2be232a361da277a2ab48807eeed)
- Fixed the memory leak problem of ossl_cmp_rp_new() function on the wrong path.
  ↳ No PR: [35b9712](https://github.com/openssl/openssl/commit/35b97122ea59fdaa56105482caf12f3ca594a2f4)
- Remove unnecessary realloc calls in ossl_property_merge to avoid memory leaks.
  ↳ No PR: [65db219](https://github.com/openssl/openssl/commit/65db21935a2add580eb35bdf0b0f37441549d54c)
- Fix the ikmlen length check in ossl_ec_dhkem_derive_private and correct the comparison object from Nsecret to Nsk.
  ↳ No PR: [c93f4a1](https://github.com/openssl/openssl/commit/c93f4a1e75efbb10153b2520a10e5a19a4479fdf)
- Fix the problem of using uninitialized values in ossl_quic_demux_inject to ensure that the datagram ID is correctly assigned before adding to the pending list.
  ↳ No PR: [9861be4](https://github.com/openssl/openssl/commit/9861be4eef925ec1751765f8138ad81e0632234f)
- Fixed the code logic of the encapsulation and decapsulation functions in pkeyutl, including correcting the key type setting, output file processing and parameter passing of the decryption operation.
  ↳ No PR: [63e9a3b](https://github.com/openssl/openssl/commit/63e9a3b1f34c42e759332a07468d21b52e89826d)
- Corrected the value of MARSHALLED_TOKEN_MAX_LEN macro and updated related comments.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [db1c857](https://github.com/openssl/openssl/commit/db1c857c07cb24153ba62a54c9ed95b7adb0b363)
- Fixed the concurrency issues of premature reuse of query processors and lost references in ID field updates in RCU locks, ensuring that the minimum number of query processors is 3, and introducing atomic operations to ensure update atomicity.
  ↳ No PR: [25f8e2c](https://github.com/openssl/openssl/commit/25f8e2c15b701514b7b2fe652634289b6fb8581f), [fbd34c0](https://github.com/openssl/openssl/commit/fbd34c03e3ca94d3805e97a01defdf8b6037f61c), [5949918](https://github.com/openssl/openssl/commit/5949918f9afa85d72535676f114346ed541e0b1e), [65787e2](https://github.com/openssl/openssl/commit/65787e2dc219685c30539c6f60eb6b64b890bf6f)
- Fixed a memory leak problem caused by mac_gen_init and cmac_gen_init functions when parameter setting fails.
  ↳ No PR: [2455ef2](https://github.com/openssl/openssl/commit/2455ef2112997d6a366623a209f1d0090ed2d847)
- Fixed a memory leak caused by the eddsa_signverify_init function not releasing WPACKET resources on the wrong path.
  ↳ No PR: [abbc407](https://github.com/openssl/openssl/commit/abbc4073145cb6b2ea221f3e34809e9aefece9ab)
- Fixed an issue where data size calculation in PEM_ASN1_write_bio used fixed values and instead used the maximum block size for allocation.
  ↳ No PR: [a59efbf](https://github.com/openssl/openssl/commit/a59efbfc7ecb0197a48655b27a6d7e808d4a3040)
- Fixed a possible leak of OSSL_STORE_INFO objects on the wrong path in the add_uris_recursive function.
  ↳ No PR: [be5965a](https://github.com/openssl/openssl/commit/be5965acad7a1c45e49411bcf4abad99d106a7c1)
- Fixed a memory leak problem in which the certificate object was not released under the wrong path in the cert_response() function.
  ↳ No PR: [56160f1](https://github.com/openssl/openssl/commit/56160f173d055486357b7a315ab4e9579b2538d5)
- Fixed the memory leak problem of the ossl_rsa_multiprime_derive function under the wrong path, ensuring that the newly created BIGNUM object is released correctly in case of exception.
  ↳ No PR: [8cdba24](https://github.com/openssl/openssl/commit/8cdba24ceea00de9c0cd8f90bf662d632c37e14b)
- Fixed the problem in the io_getevents function that when passing a structure to a system call, the value was incorrectly passed instead of a reference.
  ↳ No PR: [b6f2ff9](https://github.com/openssl/openssl/commit/b6f2ff93639d9c71aae62dfc72082dd0829c2170)
- Fixed the printf format error of the size_t type variable in template_kem.c used in debug_print, changing %d to %zu.
  ↳ No PR: [0bdb4a6](https://github.com/openssl/openssl/commit/0bdb4a67bdab74bc1629eb2ab7f8704f6ba221b3)
- Fixed processing order of -list_curves option in ecparam command, ensuring curves are listed before input is read.
  ↳ No PR: [8f416ba](https://github.com/openssl/openssl/commit/8f416ba9b0c21cac62ce55ee2797b7b75c000575)
- Fixed the problem that the ossl_serial_number_print() function may crash when the ASN1_INTEGER content is empty, it will now print (Empty) correctly and return safely.
  ↳ No PR: [6f1dbaf](https://github.com/openssl/openssl/commit/6f1dbaf7d2a5de5656ff243e5c570bc8da0ad423)
- Fixed build failure caused by misuse of preprocessor concatenation operator for string literals.
  ↳ No PR: [79225a3](https://github.com/openssl/openssl/commit/79225a3e17e070bb049f2bad89e47a1dde88b982)
- Fixed the memory leak caused by not releasing CRYPTO_REF when releasing QUIC token, and added error handling when building token.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [4f11f52](https://github.com/openssl/openssl/commit/4f11f520d730d5df986f300b8379f5cc6d4a5a1c)
- Fixed the problem that the ossl_quic_trace function failed to correctly obtain the connection ID length when parsing short packet headers. The actual length is now obtained through the API to correctly parse the packet headers.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [5177484](https://github.com/openssl/openssl/commit/5177484f19e6932a5f10fad33eff2fdd1535d1eb)
- Fixed a crash problem caused by the array being out of bounds due to the certificate key algorithm being dynamically added by the provider when configuring the certificate through the configuration file.
  ↳ No PR: [9cbaa87](https://github.com/openssl/openssl/commit/9cbaa8763c096bc91e09fc121583f90d93ecfc82)
- Avoided repeated calls to ssl_load_sigalgs in tls1_set_sigalgs_list, and fixed potential problems caused by loop condition errors in ssl_cert_lookup_by_pkey.
  ↳ No PR: [3252fe6](https://github.com/openssl/openssl/commit/3252fe646b17c1a3cebed4ff8fe35c19c523e222)
- Fixed issues reported by Coverity, added null pointer checks in tests and simplified conditional statements.
  ↳ No PR: [6f3ada8](https://github.com/openssl/openssl/commit/6f3ada8a14233e76d8c809659b81bddaa7be6db8)
- Fixed a crash that may be caused by the session being empty when obtaining the group ID, and added a null pointer check.
  ↳ No PR: [4ca80d3](https://github.com/openssl/openssl/commit/4ca80d39412bf1fe2da6ef7691d1263fa8b23cde)
- Rolled back QUIC initial packet validation changes, fixed interoperability testing issues and cleaned up the code.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [9eee58c](https://github.com/openssl/openssl/commit/9eee58cce487d223b6c4338d8508e2f39b82421c)
- Fixed the problem that quic_tls.c was missing necessary header files due to refactoring, and re-added quic_record_util.h to obtain the required macro definitions.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [b360611](https://github.com/openssl/openssl/commit/b360611ad6b840e7299d2e430b0cf0b6d05ee328)
- Fixed multiple Coverity reported issues, including correctly handling null key objects in encryption initialization, adding a memory allocation failure check, and adding an output buffer null pointer check.
  ↳ No PR: [83ced5e](https://github.com/openssl/openssl/commit/83ced5e6b1f19a3196b464d0a10f8dc44633df1e)
- Refactored the EVP_SKEY initialization logic to enforce that skeymgmt is not empty and added missing memory allocation checks, fixing issues found by Coverity.
  ↳ No PR: [560e586](https://github.com/openssl/openssl/commit/560e5863711d0eeef48d20d73bc1403f8003ccf3)
- Fixed an issue with initial packet AEAD validation on QUIC ports when skipping retry packets, ensuring proper discarding of old receivers and rescuing authenticated packets from them into new channels.
  ↳ No PR: [96075a6](https://github.com/openssl/openssl/commit/96075a6a4061eab8274fc27f5f10959ddae433e5)
- Improved consistency of ML-KEM key checking, cross-validating seed values when importing and loading, and setting hard errors on load failures to prevent key information leakage.
  ↳ No PR: [a4465bf](https://github.com/openssl/openssl/commit/a4465bf694ea4505c544a96f2cfb329d86e8b711)
- Fix the conditional judgment of the SSL_CTRL_GET_PEER_SIGNATURE_NAME branch in ssl3_ctrl to avoid null pointer dereference when peer_sigalg is empty.
  ↳ No PR: [76e3fdd](https://github.com/openssl/openssl/commit/76e3fdd0f6b9f838cad263dae35721d43400b5d1)
- Add null pointer check for SSL_CONNECTION_FROM_SSL return value in SSL_set1_client_cert_type and SSL_set1_server_cert_type functions to prevent potential null pointer dereference.
  ↳ No PR: [a1c6e2d](https://github.com/openssl/openssl/commit/a1c6e2d1b590dc6a3d2e1c7bd1bf61ffcf854104)
- Fix issues reported by Coverity and add provider reference count checks in key management methods to avoid potential null pointer dereferences.
  ↳ No PR: [c152a94](https://github.com/openssl/openssl/commit/c152a943957933e8aa621441a36e9951f7eff050)
- Fixed the problem of calling the wrong function when loading the certificate store in openssl-ts. Instead, use the added function to be compatible with org.openssl.winstore.
  ↳ No PR: [c9e56da](https://github.com/openssl/openssl/commit/c9e56da7774bbaca1597bbc754b4111729914e5c)
- Added null pointer checks to multiple SSL functions, fixed null pointer dereference issues reported by Coverity scans, and adjusted variable declaration order and function call parameters.
  ↳ No PR: [704c3d3](https://github.com/openssl/openssl/commit/704c3d3cd28efa8106bd85b354de1a03d68d9469), [afc64c2](https://github.com/openssl/openssl/commit/afc64c240f2a99a6cd30a0384b5296ad9f0f7597)
- Fixed the BIO reference counting problem discovered by Coverity scanning, and added a check for the BIO_up_ref return value in the SSL BIO setup function.
  ↳ No PR: [cec0659](https://github.com/openssl/openssl/commit/cec0659fa4f43d3be6c006be100378589a32b033)
- Fixed an error in the key sharing processing logic when the TLS client receives a HelloRetryRequest that does not request new key sharing.
  ↳ No PR: [0b40fac](https://github.com/openssl/openssl/commit/0b40fac3fb1a2207ef777c4f2c44eadc5cfcdef4)
- Fixed the problem of improper use of error codes in libssl, no longer throwing libconf error codes from the libssl code.
  ↳ No PR: [4c69cae](https://github.com/openssl/openssl/commit/4c69caef48cdaa6f25388613f225f6ed6974a501)
- Fix a dangling pointer issue that may occur when OSSL_ENCODER_to_data() is called multiple times in the FIPS provider, and add corresponding test cases.
  ↳ No PR: [c2f4d7a](https://github.com/openssl/openssl/commit/c2f4d7aae1c7c726eb1f8226d3d454dfd9754758)
- Improved ML-KEM key verification logic, when both seed and private key are provided, the complete ML-KEM private key encoding result is now compared, not just the public key hash.
  ↳ No PR: [6ef393b](https://github.com/openssl/openssl/commit/6ef393b89be1f329214ae07388812b245950095f)
- Fixed a possible crash caused by null pointers in QUIC implementation.
  ↳ No PR: [442f195](https://github.com/openssl/openssl/commit/442f1958e8f2c4f35a29a2e921e29aee1ceeccb3)
- Control characters in distinguished names are escaped by default.
  ↳ No PR: [2411f9b](https://github.com/openssl/openssl/commit/2411f9b662fa501c9eec257a30a7da0cfc2dc173)
- Fixed the race condition during RCU queue recycling to avoid use-after-free errors when allocating more than 3 QPs; and added test cases to cover high concurrency scenarios.
  ↳ No PR: [6e7be99](https://github.com/openssl/openssl/commit/6e7be995fd7fd24d38b95982cf90f801ac045743)
- Fix memory ordering issue in update_qp on weakly ordered systems, add a dummy atomic release operation to ensure the new value of reader_idx is visible in get_hold_current_qp.
  ↳ No PR: [82f7dbb](https://github.com/openssl/openssl/commit/82f7dbbf381b4b14116e2e20e249b6353176e267)
- Adjust reference counting and error handling when setting peer keys to ensure the provided EVP_PKEY is correctly held.
  ↳ No PR: [cb286b6](https://github.com/openssl/openssl/commit/cb286b6e09a5f3b7b99a03af7efaefe290ea1deb)
- Fixed the issue where the initial secret was not set when the server channel created its own qrx, ensuring that client hello across multiple datagrams can be decoded correctly.
  ↳ No PR: [8f74d8c](https://github.com/openssl/openssl/commit/8f74d8cee3630ede41a4dfa1a85c469d2200c58d)
- Fix the parameter list available in ECX key management, remove the mandatory digest parameter from the general ECX parameters, and only reserve it for Ed25519/Ed448.
  ↳ No PR: [0639c36](https://github.com/openssl/openssl/commit/0639c3618c98a0c090b6c26627f82be71b91b9fd)
- Added a null pointer check for the return value of OCSP_BASICRESP_new in the make_ocsp_response function to avoid potential crashes.
  ↳ No PR: [195d677](https://github.com/openssl/openssl/commit/195d67780e1b3ba42e31226b3e5b8bef0b05eee7)
- Fixed an issue where the QUIC record layer incorrectly decrements the unreleased counter when the record fails to be released, and only updates the counter after a successful release.
  ↳ No PR: [81789a0](https://github.com/openssl/openssl/commit/81789a05b7e2d8ba69955addaa413796007e3eb6)
- Fixed the problem caused by the lack of default length of the SHAKE digest algorithm in CMS, and set a fixed digest length for it during initialization.
  ↳ No PR: [c3d4303](https://github.com/openssl/openssl/commit/c3d43037b460c7a836073713b78e2c536a08714d)
- Fixed the null pointer dereference problem caused by uninitialized ASN1_TYPE element in asn1_ex_i2c, added processing of V_ASN1_UNDEF type and returned error code.
  ↳ No PR: [5782f08](https://github.com/openssl/openssl/commit/5782f0892011d3412771a8385c4a347f34425b8c)
- Fixed the report of certificate chain public key information in s_client to correctly display the group name of the elliptic curve key instead of the number of bits.
  ↳ No PR: [52413a7](https://github.com/openssl/openssl/commit/52413a7bb3357061cf7a4864e60fae14ffa966b3)
- Fixed a duplicate release issue caused by attribute strings not being copied correctly when copying hybrid ML-KEM keys.
  ↳ No PR: [428d290](https://github.com/openssl/openssl/commit/428d2901a21abef7739143f7641aa3a157762aeb)
- Fixed a segfault caused by a null pointer in the pkeyutl command line tool.
  ↳ No PR: [d11ba5d](https://github.com/openssl/openssl/commit/d11ba5d7805c4a47015e83f6ae14eb1fd61495fd)
- Use the safer ASN1_INTEGER_get_int64 API in serial number printing to eliminate return value ambiguity.
  ↳ No PR: [aa52ec9](https://github.com/openssl/openssl/commit/aa52ec9b0ae5c32bb4759b71117737002cbd1263)
- Fixed an issue where thread-local storage keys in thread event handlers were not recycled correctly.
  ↳ No PR: [36840ab](https://github.com/openssl/openssl/commit/36840ab577d547a35cbc7c72396dc7931712eb6e)
- Fix display of thread availability error messages in argon2.
  ↳ No PR: [60725f8](https://github.com/openssl/openssl/commit/60725f8511fc96043f1ee5cbbe81c3fce2b2c828)
- Fix fileprefix not preserved when h3ssl is reused in HTTP/3 demo server.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [66e1e60](https://github.com/openssl/openssl/commit/66e1e60a61fd3b023790a10bc09359f68f50cfc4)
- Fixed an issue in the demo server that caused output errors due to overlapping memory areas when setting URL values.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [861a322](https://github.com/openssl/openssl/commit/861a322400da021c524410452deaeefbf8d048fb)
- Fixed error handling and initialization memory leak of SSL_read in HTTP/3 demo server.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [eabdcad](https://github.com/openssl/openssl/commit/eabdcadefa31406d8a39b9d17617f9d1bb60e1c1)
- Fixed a memory leak caused by not releasing allocated memory when sk_OPENSSL_STRING_push failed.
  ↳ No PR: [2457fc4](https://github.com/openssl/openssl/commit/2457fc4816551a7e982117a4032fd1c259c493a7)
- Fixed the return type of the get_file_length function in the demo server to avoid sign issues.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [15f8594](https://github.com/openssl/openssl/commit/15f859403e5903d58a97d0d2086d27275d49d92f)
- Fixed the issue where the set_digest function in scrypt incorrectly releases the context when EVP_MD_fetch fails.
  ↳ No PR: [2dded72](https://github.com/openssl/openssl/commit/2dded720223c6b84dcbeadbbcd1c6307fe815832)
- Fixed the risk of double release caused by not setting a null pointer after the kdf_scrypt_reset function in scrypt is released.
  ↳ No PR: [901b108](https://github.com/openssl/openssl/commit/901b108154fd8d28516b9b4bebde93ac5bc2a224)
- Allow fallback to generic key management when importing unknown key types.
  ↳ No PR: [71debb7](https://github.com/openssl/openssl/commit/71debb7b84f16e268237707931bfff90052a133e)
- Fix factor size and modulus bit size checks, only allow 1024, 1536 or 2048.
  ↳ No PR: [b41e0bf](https://github.com/openssl/openssl/commit/b41e0bf168d855789e287553e873f4ccff28bfb5)
- Fixed memory leak caused by sk_POLICYQUALINFO_push failure in policy_section().
  ↳ No PR: [ececabd](https://github.com/openssl/openssl/commit/ececabd9adb4b4def9c044491f993b94ba0c618f)
- Added stream limit retry mechanism and adjusted the number of parallel stream batches in the QUIC client example.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [17dc32c](https://github.com/openssl/openssl/commit/17dc32c51bb317acefdb123ac5f8fa34b3826985)
- Fixed typos in comments in QUIC code, removed redundant null pointer assignments and added null pointer checks.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [5569e17](https://github.com/openssl/openssl/commit/5569e170ee04267114fff18bff788bad967ff799)
- Added null pointer check in template_kem.c to fix issues reported by Coverity.
  ↳ No PR: [2581ff6](https://github.com/openssl/openssl/commit/2581ff619bbba7232ca5f6db200bab42ef72c33f)
- Add null pointer check for ossl_quic_tls_is_cert_request function in QUIC code.
  ↳ No PR: [3820f2d](https://github.com/openssl/openssl/commit/3820f2da7cb76ad48b3078d9e705176088a04c99)
- Fixed an issue in qlog logging where frame header parsing failed and was not skipped correctly.
  ↳ No PR: [1e6bd53](https://github.com/openssl/openssl/commit/1e6bd53cfccda02f6ceca138c57e527f41957ca4)
- Fix the problem that the i2d_ASN1_bio_stream() function ignores the return value and ensures that the result of ASN1_item_i2d_bio() is returned correctly.
  ↳ No PR: [7d659ca](https://github.com/openssl/openssl/commit/7d659ca2d2412445ddb80831ab7dce9be35122bd)
- Fix the memory leak of ktls_new_record_layer function on the failed path, use tls_free to correctly release the OSSL_RECORD_LAYER object.
  ↳ No PR: [070856e](https://github.com/openssl/openssl/commit/070856e952ae857955e562ef351a775ef464a5be)
- Fix the conditional inversion of the log_frames function in qlog_event_helpers.c to ensure that the number of skipped bytes does not exceed the remaining length of the packet.
  ↳ No PR: [56e00f1](https://github.com/openssl/openssl/commit/56e00f129607ab7eb5df9ff6dca023211336dd34)
- Add a check on the return value of OPENSSL_strdup in load_index to ensure that it correctly jumps to error handling when memory allocation fails.
  ↳ No PR: [1201a1c](https://github.com/openssl/openssl/commit/1201a1cd14dfef62e646c5ac22780aecf0f7db6c)
- In pkcs12 command, add warning when MAC is missing.
  ↳ No PR: [8ad98cc](https://github.com/openssl/openssl/commit/8ad98cce41aa8a6278f7ade6ad2f70b80b194b72)
- Fixed QUIC demo server compatibility issues, adjusted timeout handling, stream closing logic and added ALPN selection function; also simplified initialization, corrected spelling and bitwise OR operation.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a31dfb0](https://github.com/openssl/openssl/commit/a31dfb0ee655b1b9a181d05f32975a9a42fd9785), [43ccd96](https://github.com/openssl/openssl/commit/43ccd96da687d2bdc361356f39e4fbfbb0355fca)
- Fix code issues in the quic-hq-interop example, improve error handling, use safe string functions, optimize session cache logic, and unify buffer size macro definitions.
  ↳ No PR: [0fdf965](https://github.com/openssl/openssl/commit/0fdf965bf0b1f87d4a5d52c71994ffdda5235718)
- Fix the logic of the echo loop in the QUIC blocking server example so that it continues to process more data after a successful echo.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [9dfacaa](https://github.com/openssl/openssl/commit/9dfacaa82a518c8c459dd6e33a7dd205129692f4)
- Update the error code file and correct the error code definitions related to brotli compression.
  ↳ No PR: [3cfcf82](https://github.com/openssl/openssl/commit/3cfcf820bd667d0b0253dacda5af533c99f5631d)
- In random number context initialization, replace strdup with OPENSSL_strdup to fix Coverity issue.
  ↳ No PR: [dfd177b](https://github.com/openssl/openssl/commit/dfd177b776ce95a435fc1653e328380c7f1a638c)
- Disable debug output (BIO_printf call) in property.c when compiling the FIPS module.
  ↳ No PR: [e9aac2c](https://github.com/openssl/openssl/commit/e9aac2c2f35f85019db91871a5ea2b1f85cbf787)
- Fix RCU lock-related to-do items: change the count parameter type of allocate_new_qp_group to unsigned integer, adjust the order of the rcu_lock_st structure fields to optimize stack alignment.
  ↳ No PR: [3cd8141](https://github.com/openssl/openssl/commit/3cd814171586e2426a741962435e57304ab1c0df)
- Fixed compilation problems caused by C++ style comments and changed comments to C style.
  ↳ No PR: [01b6d4a](https://github.com/openssl/openssl/commit/01b6d4a39b0805bd3dcadf709ce6f05b5162fd96), [49ec8cf](https://github.com/openssl/openssl/commit/49ec8cff04c8d0ff8b5bb604acd98c3eb6c7cced)
- Fix filter provider to return correct provider context.
  ↳ No PR: [29d0220](https://github.com/openssl/openssl/commit/29d02206f387cdc1f9c3091239c0bdfc23fe3610)
- Add the --ignore-errors mismatch option to the coveralls.yml configuration to ignore lcov's error mismatch issues.
  ↳ No PR: [75416c0](https://github.com/openssl/openssl/commit/75416c098e0e21f1e24fba99e28773f8b25a8d01)
- Exclude mvfst client combination with amplificationlimit testing in QUIC interop testing workflow.
  ↳ No PR: [cfc62a3](https://github.com/openssl/openssl/commit/cfc62a3c467b73207315060de1fe9af90c82d863)
- Merged QUIC client and server interoperability CI testing, removing separate server build and run workflows, and unified workflow supports both client and server side testing.
  ↳ No PR: [c55114f](https://github.com/openssl/openssl/commit/c55114f680a1b7a88ed2f502342780b913d55018)
- Adjust the enablement status of ssl-trace in the CI configuration: the checker-ci job is explicitly disabled, and the checker-daily job removes explicit disablement to enable by default.
  ↳ No PR: [20ca6d4](https://github.com/openssl/openssl/commit/20ca6d47433636ff016041bcf25afae5bf8a9ad3)
- Adjust the daily CI checker job list, remove the default disabled options and enable some previously disabled options.
  ↳ No PR: [612e3e8](https://github.com/openssl/openssl/commit/612e3e8340436b90d3545ffb16eaaa036ff2446f)

### Refactoring optimization
- Adjusted SLH-DSA's key generation and signature verification processes, updated internal context types, and corrected the distribution table of signature functions.
  ↳ No PR: [db5846a](https://github.com/openssl/openssl/commit/db5846a7e094101117543fa5f2d668fb308f508c)
- When verifying the server X.509 certificate, the ERR marking mechanism is also used, and the certificate reference count and the order of the verification process are adjusted.
  ↳ No PR: [739c4b2](https://github.com/openssl/openssl/commit/739c4b2e92116952e4baf3e14d219b82f871ec6a)
- Reorganized the inclusion relationship of e_os.h in the SSL module, removing it from ssl_local.h and including it explicitly where needed.
  ↳ No PR: [2bb8382](https://github.com/openssl/openssl/commit/2bb83824bba50c0c37952cf9217f3676d2f0c94d)
- Removed the inclusion of e_os.h from the public header file apps.h and introduced it directly in the required source files instead.
  ↳ No PR: [23b795d](https://github.com/openssl/openssl/commit/23b795d34f81a83b3273b50a76eaf2e4879cdbe2)
- Refactored the load_key_certs_crls() function, cleaned up the code and added comments.
  ↳ No PR: [dd73b45](https://github.com/openssl/openssl/commit/dd73b45e289e02d4fa9c7be0c72581b833ac9219)
- Unified migration of QUIC connection internal data structures, parent references, blocking modes and event handling to QUIC_OBJ infrastructure.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [6d1d52c](https://github.com/openssl/openssl/commit/6d1d52cef5e11c30b64868eb383d60ba14fd4896), [63984f2](https://github.com/openssl/openssl/commit/63984f276c8b707e62b8a98684e3efdb456ce9a5), [fdc13a9](https://github.com/openssl/openssl/commit/fdc13a9e4e277bf0076599aeb1c1f78215aa630c), [60c9ce7](https://github.com/openssl/openssl/commit/60c9ce78f56cb677e968560eef9a5edb23d61892)
- Reconstructed QUIC connection internal functions, adjusted parameter types, renamed functions, unified lock calls and optimized initialization logic.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [1aea7a2](https://github.com/openssl/openssl/commit/1aea7a2429d37a43f0ddef7e76995084ca150cc0), [67d43a7](https://github.com/openssl/openssl/commit/67d43a7af530c98f0a98d72de1db9b0cfad98be0), [a55d8b8](https://github.com/openssl/openssl/commit/a55d8b8b718226d078c20ea0a1d077dd69763f9d), [5a6898d](https://github.com/openssl/openssl/commit/5a6898db3a03ae1198b522d1e04a143c93a32903)
- Centralized QUIC type definitions into dedicated header files, and renamed lock-related functions.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [d1e81ca](https://github.com/openssl/openssl/commit/d1e81ca94cb02062dc49bbe49343ae2e902afe0b), [477ff82](https://github.com/openssl/openssl/commit/477ff82236517f0d5dc0e1d2dd73224d27ba7426)
- Optimized the processing of transmission parameters before QUIC connection establishment, and added assertions in the stream receiving state machine.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [1772784](https://github.com/openssl/openssl/commit/17727841d1ee97fe1932eb371dea1f03af08667e), [0723a3a](https://github.com/openssl/openssl/commit/0723a3ac0c897bdd2344efbcd22765615939366a)
- Cleaned up unused functions and macros in ssl_local.h, and removed the obsolete ssl_undefined_const_function.
  ↳ No PR: [2478d3b](https://github.com/openssl/openssl/commit/2478d3b7f5c4c2da9828e05308b34a4b078035f8)
- Added ossl_param_is_empty() utility function, and unified the null pointer check of set_ctx_params in provider.
  ↳ No PR: [f5981c9](https://github.com/openssl/openssl/commit/f5981c9629667a5a5d63cf1f88903ee6b54a45e3)
- Removed the aid field in the signature provider context and instead used an internal buffer to store algorithm identification data.
  ↳ No PR: [b69ca92](https://github.com/openssl/openssl/commit/b69ca92a5e61745dc0e74bb5c1eef75e8b45f83f)
- Added initial skeleton implementation of KEM and key management.
  ↳ No PR: [51921b8](https://github.com/openssl/openssl/commit/51921b87379c6619765020d64bdb8da28f810006)
- In PKCS7_set_signed_attributes and PKCS7_set_attributes, use sk_X509_ATTRIBUTE_deep_copy() instead of manually looping through the attribute stack.
  ↳ No PR: [a64d26a](https://github.com/openssl/openssl/commit/a64d26ac0222d10f3b9cdced4a18aeb4d5092f0f)
- Removed two unused union members in the x509_object_st structure and adjusted the related code.
  ↳ No PR: [8f4cd8e](https://github.com/openssl/openssl/commit/8f4cd8e305ad2e918fc0c5680d0ff94ee25f42c3)
- Convert a redundant condition check in the md5crypt function to an assertion.
  ↳ No PR: [fdded23](https://github.com/openssl/openssl/commit/fdded23b4481449edd8972fd60265a9f33e43e22)
- Refactored the stream removal logic to support batch removal, and create new h3conn during the process of reading the stream when there is a new connection.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [1b11d7c](https://github.com/openssl/openssl/commit/1b11d7cf679e1a2faca5684877573ab290891a9e)
- Refactored the HTTP/3 demo server code based on review comments, added the wait_for_activity function and adjusted the connection management logic.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [53ceb45](https://github.com/openssl/openssl/commit/53ceb451b62c3be4106c9d6881e104a298f225f8)
- Removed NULL check before SSL_free call, since the function already handles null pointers internally.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [9fc0d25](https://github.com/openssl/openssl/commit/9fc0d25b09367ad8899ae8a0b9a66f2f8f4ccc81)
- Checked the return value of CRYPTO_atomic_add() in provider_deactivate(), and unlocked it and returned an error if it failed.
  ↳ No PR: [8fb6c81](https://github.com/openssl/openssl/commit/8fb6c8154b552d0d7d8f160e7a6260f899b94263)
- Removed useless argc assignment in cms_main function.
  ↳ No PR: [c5e17e8](https://github.com/openssl/openssl/commit/c5e17e8cb72a560eeb502cfb11ed318de10b2832)
- Refactor the MAKE_ENCODER macro, remove the unused evp_type parameter, and update all call sites.
  ↳ No PR: [0cacf9b](https://github.com/openssl/openssl/commit/0cacf9be9746b9240fecda9a729776331d70ced0)
- Clean up QUIC connection state management, remove the no longer used accepted flag and simplify the pending check in the release logic.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [943b137](https://github.com/openssl/openssl/commit/943b137c2c1e3b2f186285e5483a92fd44bd7804), [c85c572](https://github.com/openssl/openssl/commit/c85c572206f43c3f39aba0c46223d5e8d9cfa0fa)
- Remove redundant ossl_provider_prov_ctx calls and use ossl_provider_ctx directly.
  ↳ No PR: [de578a8](https://github.com/openssl/openssl/commit/de578a8a6ad89d035cb82dc3f7d4511f1bb77bd7)
- Replaced QUIC LCIDM's hash function from custom bin_hash to SipHash implementation, and added related hash key support.
  ↳ No PR: [3e3942b](https://github.com/openssl/openssl/commit/3e3942b42fe45d83070f67bbe8451ed02a47ec96), [6a9a948](https://github.com/openssl/openssl/commit/6a9a9480a7b7c526d93e2355662d31b98219d4ab), [17d2fd0](https://github.com/openssl/openssl/commit/17d2fd075251a799eb0538cb155ecd147444368e)
- Make group names ignore case when comparing.
  ↳ No PR: [91c6e15](https://github.com/openssl/openssl/commit/91c6e157c696e8fee7320408ddb959ecf233fbaf)
- In QUIC TLS initialization, moved the creation and setting of NULL BIO from ossl_quic_tls_tick to ossl_quic_tls_configure, and added null pointer checking and conditional compilation protection.
  ↳ No PR: [688cea7](https://github.com/openssl/openssl/commit/688cea710de3baea9cf2cde91d274fe447acbf81)
- Removed unused parent_dispatch field in DRBG structure.
  ↳ No PR: [59eaa8c](https://github.com/openssl/openssl/commit/59eaa8c4af3b160bff739cc5b8a0df716ee33406)
- Replaced many sprintf() calls with BIO_snprintf() to eliminate compiler warnings.
  ↳ No PR: [2c536c8](https://github.com/openssl/openssl/commit/2c536c8b1554da273103235adabf946fb7f5a041)
- Removed unnecessary calls to sk_GENERAL_NAME_free in v2i_issuer_alt, v2i_subject_alt and v2i_GENERAL_NAMES functions.
  ↳ No PR: [83b62d4](https://github.com/openssl/openssl/commit/83b62d41b2b96a71051a2f46f6e97769b3b0d5da)
- Changed the copy method of OPENSSL_MALLOC_FAILURES environment variable from dynamic allocation to fixed-length static array, and limited the maximum length.
  ↳ No PR: [740668f](https://github.com/openssl/openssl/commit/740668f0b5917adea159eae3cd3c8b0de21ecb34)
- The zeroing operation in FFC parameter cleaning is changed to be controlled by the OPENSSL_PEDANTIC_ZEROIZATION macro, and is no longer limited to FIPS modules.
  ↳ No PR: [de22c10](https://github.com/openssl/openssl/commit/de22c10b97b5ef32087ce350d1062518a8a623de)
- Optimize the ML-KEM provider implementation, add operation type tracking, clean up the context structure, and standardize the parameter naming of encapsulated and unpacked functions.
  ↳ No PR: [b99e1a9](https://github.com/openssl/openssl/commit/b99e1a9736014f0ad4d887fab5085f2fa896cc49)
- Removed unused variable group in ec_gen_set_params function.
  ↳ No PR: [27b324f](https://github.com/openssl/openssl/commit/27b324f90a7fab330bcaff60967e377f577b8b64)
- Added tracing logs for provider algorithm fetch, cache and store operations.
  ↳ No PR: [40c01d8](https://github.com/openssl/openssl/commit/40c01d8ddc41dc9b1eb41da2c4bd759d98dd5005)
- Rename token store related functions to get0 and set1 to keep the naming style consistent.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [e521131](https://github.com/openssl/openssl/commit/e521131c60e25e6fb2269f4ff9c2619d89ac95a3)
- Modified the ossl_quic_get_peer_token function to return the QUIC_TOKEN structure, removed the QTOK type, and updated the related internal implementation.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f0e5165](https://github.com/openssl/openssl/commit/f0e516522cbf50f3b58eed461375f37ac842eed1)
- Refactor the get0_best_issuer_sk function, replace the trusted parameter with check_signing_allowed, and remove the find_issuer function.
  ↳ No PR: [5ebd6d2](https://github.com/openssl/openssl/commit/5ebd6d26a805631230d8f8ea80a83034f7b65b2b)
- Ignore attribute queries when obtaining algorithms internally in the FIPS module.
  ↳ No PR: [236d5d8](https://github.com/openssl/openssl/commit/236d5d8f72cd2cfcddf0e01bd7dfa7960c9d9e14)
- Added conditional compilation protection for one-time key generation functions in the EVP library for internal FIPS usage.
  ↳ No PR: [53e3a54](https://github.com/openssl/openssl/commit/53e3a54b6027da737ef1b82b08fe066eed9d514f)
- Optimize the attribute query logic of the random number generator and remove unnecessary attribute operations.
  ↳ No PR: [21f92ec](https://github.com/openssl/openssl/commit/21f92ecf7ce4121f27204e43e93d68760a98888c)
- Removed redundant check of EC_get_builtin_curves return value in list_builtin_curves function.
  ↳ No PR: [e1a501a](https://github.com/openssl/openssl/commit/e1a501a433b59d3c57f3ab37ea202f5f1f19a054)
- Removed a redundant macro definition.
  ↳ No PR: [340f50b](https://github.com/openssl/openssl/commit/340f50b01fd33106e3348fd6f9b2066b1a268d25)
- Removed unused atomic operation fallback functions in threads_pthread.c to eliminate clang warnings.
  ↳ No PR: [eacf145](https://github.com/openssl/openssl/commit/eacf14594dd93c971ff6480094bc23e63b87f628)
- Unify preprocessor guards for CRYPTO_atomic_store to make them consistent with other CRYPTO_atomic functions.
  ↳ No PR: [3240427](https://github.com/openssl/openssl/commit/3240427a8530f5aa6070f135e954e20e591fa132)
- Replace strdup with OPENSSL_strdup in test code to ensure consistent memory allocation function with OPENSSL_free().
  ↳ No PR: [6666389](https://github.com/openssl/openssl/commit/6666389e0c9fea706437947324881acfba4d23ac)

### Test related
- Added test coverage for issue #25298 and unified the indentation format of JSON test configuration files.
  ↳ No PR: [144b9eb](https://github.com/openssl/openssl/commit/144b9ebc3e444803643d90fee45d588be83361dd)
- Reconstructed the FIPS self-test code and unified the conversion logic from ST_KAT_PARAM to OSSL_PARAM.
  ↳ No PR: [b330d59](https://github.com/openssl/openssl/commit/b330d590b4c0784ed188ab4a24501111d2a18b47)
- Fixed compilation issues and warnings in QUIC RADIX tests, and removed debug breakpoints.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [cbfc09d](https://github.com/openssl/openssl/commit/cbfc09d99480d94316cabf007a87489f200135f1), [646c20d](https://github.com/openssl/openssl/commit/646c20d034d92a12f8b8053c2bea5590695dcd8c), [fe1029d](https://github.com/openssl/openssl/commit/fe1029d16bfa1896846ead102a2c0c306e204dbf)
- Fixed test output flushing issue, flushing stdout buffer in test_note().
  ↳ No PR: [c37f564](https://github.com/openssl/openssl/commit/c37f564bb8e25f825ff722642aaf735e8d74abb4)
- Fixed release order in lhash_test.c to avoid using freed memory.
  ↳ No PR: [1636ae1](https://github.com/openssl/openssl/commit/1636ae1a9022bad2fd5cf20f45e2729a55e688b7)
- Made beautification adjustments to http_test.c, including simplifying macro definitions, adding blank lines and comments.
  ↳ No PR: [920dd8a](https://github.com/openssl/openssl/commit/920dd8a72ecb854319c9ea5536a61a55841ca58c)
- Removed unused buffers from test harness structures.
  ↳ No PR: [0da8140](https://github.com/openssl/openssl/commit/0da8140214dd932b4c8558cf9402c7d969f1b61c)
- Added thread local override output BIO function in the test tool, allowing each thread to set output and error BIO independently.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [ea23662](https://github.com/openssl/openssl/commit/ea236623c820251df4799abb3d28faa9eee18cf1)
- Added the implementation of RADIX test framework, including core modules such as test entry, QUIC binding operation, QUIC operation auxiliary function and script interpreter.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [4a2d5fe](https://github.com/openssl/openssl/commit/4a2d5fe812f8ab1f07c86ca1bc9d79081c70531d)
- Added multi-threaded test scripts, key log support, domain function testing, SSL_poll testing and enhanced blocking support to the QUIC RADIX testing framework.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [08c5d85](https://github.com/openssl/openssl/commit/08c5d856b63c5ab558b182088b077e71e076d40a), [05f0960](https://github.com/openssl/openssl/commit/05f0960e1f5d00ef7800cfb0f0656192a5e4fd91), [ccbf3f6](https://github.com/openssl/openssl/commit/ccbf3f6ecb0050704653af486670a81edb66f70b), [381a2b5](https://github.com/openssl/openssl/commit/381a2b5789460a08dd54c781e564a9e5ee6b3ca7), [567a9ee](https://github.com/openssl/openssl/commit/567a9eed6502e559f5c375bc218b9689ee37c271)
- Fixed the format of the status string in the test file, changing wrong dir to wrong-dir.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a3b1982](https://github.com/openssl/openssl/commit/a3b1982e8a7a75b186e2292a2cc62a4a054f00b4)
- Ensure connection accept operations do not block in QUIC RADIX tests.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [01b151f](https://github.com/openssl/openssl/commit/01b151fbca5250e1a00c31f1f19d38c0c3517dac)
- Fixed QUIC test case simple_conn, adding verification of reading expected data after connection is established.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [cbd10ff](https://github.com/openssl/openssl/commit/cbd10ff618cabdfaf3d9c32d685b0e0f0bda6546)
- Added basic domain flags test for QUIC.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [62f91f2](https://github.com/openssl/openssl/commit/62f91f2f25d03bd9d074485bb23525d2349b5367)
- Removed use cases in tests where verification blocking SSL_poll did not work.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [0601469](https://github.com/openssl/openssl/commit/0601469dd6eee0b2873d071a515d4fbe2b1ef951)
- Added listener polling support for QUIC RADIX tests.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [7b2eb52](https://github.com/openssl/openssl/commit/7b2eb52473a8cdc0710f9d174eb15beb76f2e735)
- Fixed undefined behavior in wpacket tests to avoid direct dereferencing of unaligned data.
  ↳ No PR: [f096fe4](https://github.com/openssl/openssl/commit/f096fe4b9803a7e037a33e4e1bd78f96b482017c)
- Added test cases for the BIO password callback function, covering edge scenarios such as negative return values, zero-length passwords, buffer filling and null bytes.
  ↳ No PR: [fa6ae88](https://github.com/openssl/openssl/commit/fa6ae88a47a37678e8f8567ec2622bef515ac286)
- Refactored the callback test code, replaced global variables with local structures, improved memory management and reduced redundant cleanup logic.
  ↳ No PR: [9808ccc](https://github.com/openssl/openssl/commit/9808ccc53f066f5aedcd6ea847f790ea64e72e76)
- Removed redundant non-negativity checks for unsigned values and cleaned up related conditional judgments in test code.
  ↳ No PR: [8439337](https://github.com/openssl/openssl/commit/8439337036bbfd940657b95e01e5bc08dc63d331)
- Refactored the password variables in the test file from char* to const char[] array, removed the predefined length variable, used sizeof to calculate the length instead, and renamed key_password to weak_password.
  ↳ No PR: [d52e92f](https://github.com/openssl/openssl/commit/d52e92f835d8f64e207747cefe12cd1fc0423326)
- Added test cases for the EVP_get_default_properties function to verify that the default property strings returned are consistent with expectations.
  ↳ No PR: [d817093](https://github.com/openssl/openssl/commit/d81709316fc8f5703768c2ab4957a58dcea27872)
- Added tests to verify that connections are not started unexpectedly on early calls to SSL_handle_events() or SSL_get_event_timeout().
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [034fa85](https://github.com/openssl/openssl/commit/034fa85ced5bef3e6291cb1027135a31ca9b8df8)
- Fixed null pointer dereference issue in test files.
  ↳ No PR: [5bc13d5](https://github.com/openssl/openssl/commit/5bc13d5d8c8b65b09031baa954a245c889c0b19a)
- Adjusted the KEM RSA parameter test, corrected the calling method of EVP_PKEY_encapsulate and EVP_PKEY_decapsulate to obtain the output length first and then perform the operation.
  ↳ No PR: [796b2ca](https://github.com/openssl/openssl/commit/796b2caa9e2f0c1cc0a5421d553178ff80c06d51)
- Fix the compatibility regression caused by not checking the FIPS provider version in the test, and limit the execution of relevant tests to provider version >= 3.4.0.
  ↳ No PR: [73e720c](https://github.com/openssl/openssl/commit/73e720c3a5164d28ffbcbf06aa88ecdfd8b2fe7f)
- Added a test to release shared EVP_PKEY across threads, and removed the conditional compilation restriction of RCU tests on macOS.
  ↳ No PR: [420d5d6](https://github.com/openssl/openssl/commit/420d5d6294449527f4dd986b4fed8681bd4ae8fb)
- Use test_random() to replace random number generation in hash table multi-thread testing, improve test repeatability, and adjust test parameters and concurrency control logic.
  ↳ No PR: [9abd6ca](https://github.com/openssl/openssl/commit/9abd6ca6351f49f6e2c9ebd41c40c273e058bc32)
- Enhanced multi-threaded hash table testing, using macros to define the number of worker threads, and adding additional locks and resource cleanup.
  ↳ No PR: [837f05f](https://github.com/openssl/openssl/commit/837f05fc303fb335e9b107b6da8d3839e238485d)
- Fixed the problem that the int parameter was not correctly converted to size_t in the EVP_PKEY_Q_keygen call, ensuring that the variable parameter types match.
  ↳ No PR: [ccaa754](https://github.com/openssl/openssl/commit/ccaa754b5f66cc50d8ecbac48b38268e2acd715e)
- Add tests for QUIC objects to verify that setting the new_session_cb callback works properly.
  ↳ No PR: [e545264](https://github.com/openssl/openssl/commit/e54526413d5ef7c665e25f552f2f01d4352bd33d)
- Add test case for setting TLSv1.2 cipher suites for QUIC objects.
  ↳ No PR: [b10cfd9](https://github.com/openssl/openssl/commit/b10cfd93fd58cc1e9c876be159253b5389dc11a5)
- Added QUIC server-side interoperability test support, added server implementation files and adjusted container configuration to support server role running.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [fd50924](https://github.com/openssl/openssl/commit/fd50924d0107f77e0d220a0eb9c6216285fa5f39)
- Fix the version negotiation test, use the version modifier instead of the injector, and ensure that the version field in the header of the version negotiation package is correct.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [c7b82a7](https://github.com/openssl/openssl/commit/c7b82a725070061a67b4fae4825ac837d4daa163)
- Add a new keytype test for EVP_PKEY_Q_keygen to verify the key generation behavior of non-standard keytypes.
  ↳ No PR: [0c64b1c](https://github.com/openssl/openssl/commit/0c64b1ca0315edf6c3e947b53ea13fecc6da7dad)
- Initialize the parameter array correctly in the test code and ensure it is cleared appropriately.
  ↳ No PR: [5510d96](https://github.com/openssl/openssl/commit/5510d96f82a07d6245ffb817f1315fe515df7b94)
- Fix intermittent failure of lhash_test on Windows, avoid race condition by setting pending_delete flag.
  ↳ No PR: [be4ce01](https://github.com/openssl/openssl/commit/be4ce01f9f51d4ec64b53626834905a8a1de96ca)
- Add p_query function in the test and register it in the schedule, which is used to test the nocache provider behavior.
  ↳ No PR: [f6097c7](https://github.com/openssl/openssl/commit/f6097c7c5da84a6bd354c57fd6e0ffb2b549f30d)
- Fix the memory leak in the test_evp_cipher_pipeline test and ensure that the wrong path releases resources correctly.
  ↳ No PR: [009fa4f](https://github.com/openssl/openssl/commit/009fa4f924d0c89fa16ac487fa2d3f5ba60adc1c)
- Fix the test case so that it can still pass when the OpenSSL default security level is modified.
  ↳ No PR: [2986908](https://github.com/openssl/openssl/commit/2986908cc729768f540596df356279a7ba52bc7e)
- Fix memory cleaner warning caused by uninitialized pointers in tests.
  ↳ No PR: [e63e889](https://github.com/openssl/openssl/commit/e63e889b32a3503a992ed0d0d2d1138e06be0209)
- Declare test variables as volatile to prevent the compiler from optimizing out memory leak detection.
  ↳ No PR: [eeb3266](https://github.com/openssl/openssl/commit/eeb3266ebba6d70df31f20e4ebd46065fc917ce5)
- Fixed occasional test failures in test/evp_extra_test.c and adjusted the provider filtering conditions of EVP_CIPHER_fetch.
  ↳ No PR: [2f67a3d](https://github.com/openssl/openssl/commit/2f67a3dc3253b2fee472719eb5b8b02864848179)
- Fixed potential memory alignment access issues in tests, changing direct pointer dereference to memcpy safe copy.
  ↳ No PR: [94f95ef](https://github.com/openssl/openssl/commit/94f95efce93555f65d3582558e39866e9f074ca2)
- Enable ML-KEM testing in FIPS builds and add FIPS version requirements for test data.
  ↳ No PR: [3c9b0ca](https://github.com/openssl/openssl/commit/3c9b0ca13c35e90151d37ac8e4b2ef913dc0277a)
- Add evp_test support for ACVP test vectors to ML-DSA and extend the line buffer to 32K.
  ↳ No PR: [f928554](https://github.com/openssl/openssl/commit/f92855441f482b092bc7c1a89c7e44d5ce4382cc)
- Add validation of KDF context reset functionality in scrypt KDF tests.
  ↳ No PR: [4f7d2b4](https://github.com/openssl/openssl/commit/4f7d2b48093fd5147c652da319e43baea61a6218)
- Add coverage tests for ML-DSA, including key generation, signature verification, key replication, etc.
  ↳ No PR: [d711ea9](https://github.com/openssl/openssl/commit/d711ea967d8bf376d58f4dc8d7cac9f28d087389)
- Added quic-server fuzz testing and updated the fuzz testing corpus.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [029d858](https://github.com/openssl/openssl/commit/029d85869f9fdf4cb9fe5c7586d77ed9402440f3)
- Updated endecode tests to mark the ML-DSA test suite as FIPS mode.
  ↳ No PR: [f56dc1f](https://github.com/openssl/openssl/commit/f56dc1f9688cd44972489430345c98aa587f1473)
- Added digest signature verification test and key replication test for ML-DSA.
  ↳ No PR: [1cacc56](https://github.com/openssl/openssl/commit/1cacc56137e7c5be05b95d43126b88f1a6c31fe7)
- Introduce short connection ID length logging in QUIC tests, and use that length to decode packet headers.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a55b689](https://github.com/openssl/openssl/commit/a55b6894992429ac944ea4d8d0c3825216327e0c), [164d3a6](https://github.com/openssl/openssl/commit/164d3a6b59eea4d2fc48d14b2e17004e8ab27e13)
- Added FIPS version check for ML-DSA tests, only run if FIPS version is no lower than 3.5.
  ↳ No PR: [f207938](https://github.com/openssl/openssl/commit/f2079387119c57cdbe2702cb393c33212a23007a)
- Added ML-KEM fuzz tester, random test key generation, encapsulation/decapsulation and other API operations.
  ↳ No PR: [f440e81](https://github.com/openssl/openssl/commit/f440e816d07f62f2ab9640184556d4e1b075ab29)
- Updated ML-DSA signature generation, signature verification and key generation test data, added μ parameter coverage and set FIPS version requirements.
  ↳ No PR: [4e94dc0](https://github.com/openssl/openssl/commit/4e94dc07a90be0cb73038294f86701924c40b572), [fb15378](https://github.com/openssl/openssl/commit/fb15378fe7fe135868a25af330d3230f1f47ff65), [6797e02](https://github.com/openssl/openssl/commit/6797e0290713d794aac5ddacecfd68111fe1befb)
- Extended fuzz testing: Added ML-KEM seed corpus, and added SLH-DSA fuzz tester.
  ↳ No PR: [f0be052](https://github.com/openssl/openssl/commit/f0be0521d1b3a51c35c0d9db28fecfb95a1161bf), [75bc132](https://github.com/openssl/openssl/commit/75bc132dec23ac43e8baa85ee1d37c13d52f2f09)
- Remove the session and PSK test cases in clienthellotest, and limit the key sharing group to avoid ClientHello being too long.
  ↳ No PR: [cc699ac](https://github.com/openssl/openssl/commit/cc699ace927acf2e05cefff4f50e4f0a6c5d0a8d)
- Added a new test case for configuring the provider certificate through the configuration file, covering the crash scenario caused by the previous configuration.
  ↳ No PR: [e2bfb61](https://github.com/openssl/openssl/commit/e2bfb61f617fa0f3acf88263a9afc702320660db)
- Add TLS 1.3 certificate testing for ML-DSA.
  ↳ No PR: [7d2d153](https://github.com/openssl/openssl/commit/7d2d153f9d480cbd2a58aeb71d29db1b84026d93)
- Increase test_fin_only_blocking timeout from 20ms to 40ms to reduce concurrency pressure on high-load systems.
  ↳ No PR: [0e93f64](https://github.com/openssl/openssl/commit/0e93f64723894e6420faa8b95055ce637894abc1)
- Adjust the skip and enable conditions for testing in FIPS mode, and conditionally execute test cases based on the FIPS provider version.
  ↳ No PR: [9fef9b1](https://github.com/openssl/openssl/commit/9fef9b194c2cf95fe9c825f8550fd86dca784e49), [c59f5f1](https://github.com/openssl/openssl/commit/c59f5f121075f94cf131cdc6d02437fa1fdc7151)
- Enable automatic DH parameters for server context in ssl_test.c, supporting DHE handshake for TLS-1.2 and earlier.
  ↳ No PR: [0575755](https://github.com/openssl/openssl/commit/0575755eaf9e35406e4e27a00a7505b72465c08d)
- Added test to verify the behavior of QUIC TLS early data without END_OF_EARLY_DATA message.
  ↳ No PR: [966c9d3](https://github.com/openssl/openssl/commit/966c9d3e98af9ad20dcd1f80abe5b99665ecb701)
- Add extended test support (controlled via the environment variable EVP_TEST_EXTENDED) and public key verification test types to evp_test.
  ↳ No PR: [740e43f](https://github.com/openssl/openssl/commit/740e43f074a9328415092402fe6a5398fc79aa4c), [f0417c6](https://github.com/openssl/openssl/commit/f0417c6ebc46cbde7906b3e209b2d56119dafb11)
- Increase the line length limit for reading stanza in the test tool to support long data lines for PQC algorithms (such as SLH-DSA).
  ↳ No PR: [4439b8d](https://github.com/openssl/openssl/commit/4439b8d3cc5c9a224884c17984d43efc29225e3f)
- Fix ssltrace test, update frame length value in test reference file.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [b684545](https://github.com/openssl/openssl/commit/b684545e7354eab1f974890a8e17813bff9f5bd9)
- Fix memory leak in ecdsa_keygen_knownanswer_test function, optimize EC_POINT allocation logic.
  ↳ No PR: [20a2f3b](https://github.com/openssl/openssl/commit/20a2f3beba9be6e226a0633b60c29e8a928ccd21)
- Fix quicapitest.c build issue when SSL trace is disabled.
  ↳ No PR: [9d8b18c](https://github.com/openssl/openssl/commit/9d8b18c74e9984e522bcbe161a8033cc9c57e81a)
- Fix the logic of memory allocation failure check in xor_gen_init function to ensure correct return.
  ↳ No PR: [c5eb70d](https://github.com/openssl/openssl/commit/c5eb70de753605cda978fda9a4eddbdb1fc692be)
- Use OPENSSL_strdup and BIO_snprintf to replace the standard library functions in the test code to improve code consistency.
  ↳ No PR: [8d69f40](https://github.com/openssl/openssl/commit/8d69f4005b51794255b255d676932107873c346e), [7e431da](https://github.com/openssl/openssl/commit/7e431da4d869dce76d0ad88215a82281f19562af)
- Fix buffer growth calculation and stream acknowledgment issues in QUIC tests.
  ↳ No PR: [3947982](https://github.com/openssl/openssl/commit/3947982e3aea0815bf45771c23abd82603c1177d), [4f2f517](https://github.com/openssl/openssl/commit/4f2f5179a11920d36381fef299259e51953d72e9)
- Improve QUIC testing: add wildcard matching, advance simulation time to ensure handshake completion, and use fake time to resolve Windows platform instability.
  ↳ No PR: [b665a13](https://github.com/openssl/openssl/commit/b665a13ac0631ed94a7893ce035e976c6af51154), [f9aaeac](https://github.com/openssl/openssl/commit/f9aaeacbf983b63696eb2dc0be63bdac2a0199bf), [192f096](https://github.com/openssl/openssl/commit/192f096afd4935599233efadff0a8d8d57f2075e)
- Add memory allocation failure handling for x509 fuzz testing.
  ↳ No PR: [6d42072](https://github.com/openssl/openssl/commit/6d42072e0b9e52fbeee28cb451e2ec269b329708)
- Correct the initial value of the operation counter in the test to correctly record the number of operations.
  ↳ No PR: [6b662bf](https://github.com/openssl/openssl/commit/6b662bf0d6c527584e29ba909e9e5820a3fedd1f)
- Re-enable RCU stress testing on macOS.
  ↳ No PR: [4d16d2f](https://github.com/openssl/openssl/commit/4d16d2f40a135830ee667e1588c75293a7b23480)
- Enable the required groups in the test configuration for high security level testing.
  ↳ No PR: [bcc3648](https://github.com/openssl/openssl/commit/bcc364896e0afe822ba83485d8fc9d47cd75d009)
- Fix the result code prediction logic in slh-dsa fuzz testing.
  ↳ No PR: [c0eb5c5](https://github.com/openssl/openssl/commit/c0eb5c57f77c5a158b989285b1344297e0186235)
- Added logging overflow test cases for tlsfuzzer external tests.
  ↳ No PR: [83dbfde](https://github.com/openssl/openssl/commit/83dbfde6aaf7a384cfc7bab6608943a56ac4ebed)
- Adjust tests to be compatible with older FIPS modules to avoid expecting success from outdated modules.
  ↳ No PR: [18f2091](https://github.com/openssl/openssl/commit/18f2091ad14c33721fc6de3e0f9b1cdfe5bffcf6)
- Remove RSA KEM test cases from evp_test test data file.
  ↳ No PR: [982a967](https://github.com/openssl/openssl/commit/982a9676cf30799d18708714060aea66bc0572ad)
- In EVP test data files, add default provider conditions for SHA1 and MD5 tests.
  ↳ No PR: [e0b7790](https://github.com/openssl/openssl/commit/e0b779098dbd058c7327c5b1a369aa8d2bc5bb87)
- Fix the incorrect path processing of encapsulate and decapsulate in evp_test so that the test can still pass correctly in expected error situations.
  ↳ No PR: [8e874d0](https://github.com/openssl/openssl/commit/8e874d09d88ffbfed6f9918d89028b44c2f947dd)
- Add evp_test test data for ECX KEM.
  ↳ No PR: [9adf538](https://github.com/openssl/openssl/commit/9adf53889b7bca6f342b1d3dc856c88f777a49d7)
- Added test to verify that BIO does not need to be set up when using the QUIC TLS API.
  ↳ No PR: [c25f078](https://github.com/openssl/openssl/commit/c25f0780a5f4f2fc710f44847ebd1457b9a495c4)
- Added EVP_DigestSignInit test case for ECDSA and KECCAK-256 hashes.
  ↳ No PR: [ab7a159](https://github.com/openssl/openssl/commit/ab7a15998f5ac2714f10f8b7de1e1186de0b1662)
- Fixed infinite loop and empty frame issues in quic_multistream_test caused by incomplete QUIC frame type processing.
  ↳ No PR: [6df6496](https://github.com/openssl/openssl/commit/6df6496e3e9ef6f8fa6fc864dcb9b5d1d007e792), [9fbfb28](https://github.com/openssl/openssl/commit/9fbfb28ac6e5e4ad05735fa295dec12e11216a9a), [9bd5633](https://github.com/openssl/openssl/commit/9bd563321b4782bfcd4862d591edeeba25466908)
- Change the backoff period of noisy dgram BIO to configurable, and specify backoff 1 frame in the test callback to fix the connection failure problem caused by ML-KEM key sharing.
  ↳ No PR: [5ee86b8](https://github.com/openssl/openssl/commit/5ee86b8be22ec89703f6a1310e735bff2e5a6f93)
- Reduce the detailed file list output of tar archives in the make-test CI workflow to reduce log clutter.
  ↳ No PR: [5ae74ab](https://github.com/openssl/openssl/commit/5ae74ab47c62088644d3e543ee409a965016205f)
- Adjust the client list for QUIC interop testing, exclude msquic's retry test, and re-add Chrome to the server test.
  ↳ No PR: [97fbbc2](https://github.com/openssl/openssl/commit/97fbbc2f1f023d712d38263c824b6c5c8ffe6e61)
- Improved QUIC demo server to support testing in Chrome browser, including allowing sending files, adjusting poll logic and adding create_socket function.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [76d8bf6](https://github.com/openssl/openssl/commit/76d8bf6f5844abbc30634c215097a764df425229), [fe3e4bb](https://github.com/openssl/openssl/commit/fe3e4bbb4f597c56b8bdadc2d39276b0f1d236f1)

### Performance optimization
- Improve decoder performance by more accurately tracking input types (DER, PVK, MSBLOB) and algorithms, reducing unnecessary decoder attempts.
  ↳ No PR: [44a6402](https://github.com/openssl/openssl/commit/44a64029c3c5357c5b32dbe45b7f55ab7866ad3f), [31b5f3f](https://github.com/openssl/openssl/commit/31b5f3f38225e0b694bd564e8e77d9fefb51ff65)
- Optimize the ossl_namemap_name2num_n function and use hash table lookup instead to avoid strndup, thereby improving performance.
  ↳ No PR: [0baa3ac](https://github.com/openssl/openssl/commit/0baa3ac736520c9457c5ef05614fdd54b8dc5515), [054f6c0](https://github.com/openssl/openssl/commit/054f6c0fc15e9c11ec4a94b08a9528844005b449)
- Add internal helper function for efficiently obtaining EVP_SKEYMGMT from specified provider.
  ↳ No PR: [787a083](https://github.com/openssl/openssl/commit/787a083d4225dce06da0f7447255df2cd83f37af)
- Reconstruct the logic of removing empty tuples, adopt a more efficient traversal method, and optimize the parameter passing of the signature algorithm search function.
  ↳ No PR: [0554bdd](https://github.com/openssl/openssl/commit/0554bddd4feaa3f7bd0366d9592902548e4acc74)
- Fixed IV passing issue for non-AEAD passwords in speed tool, ensuring IV is always passed when setting keys.
  ↳ No PR: [b8028d4](https://github.com/openssl/openssl/commit/b8028d489037033a6eaa02b11755e5be0e688523)
- Updated CHANGES.md to document performance optimization of AVX_IFMA parallel modular exponentiation on Intel Sierra Forest processors.
  ↳ No PR: [78991c9](https://github.com/openssl/openssl/commit/78991c9e37e373fae4680886eae36044c932b4e6)
- Add block size check in speed command, skip benchmark test if not met.
  ↳ No PR: [a366072](https://github.com/openssl/openssl/commit/a3660729e68dc11c01edb4a349ff2610b6b59ee0)
- Change aead_ivlen from a runtime variable to a compile-time constant macro to simplify the code.
  ↳ No PR: [604411f](https://github.com/openssl/openssl/commit/604411f8861e950d2da2564d730bc5e9fbb750eb)
- Rollback atomic loading fix for macOS Apple M1 virtualized CPU to avoid potential performance impact.
  ↳ No PR: [a6f512a](https://github.com/openssl/openssl/commit/a6f512a1e6c1c2e3e1efaad51a6fcf65f260bbb1)
- Clean up and optimize performance of ML-KEM implementation, rewrite number theory transformation (NTT) related functions and adjust loop structure.
  ↳ No PR: [003309c](https://github.com/openssl/openssl/commit/003309c376a50ab08ee3a4c23c34373f69538210)

### Security related
- The BN_GF2m_poly2arr function now rejects polynomials whose constant terms are zero or whose degree exceeds the limit, and the return value meaning is clarified to prevent memory out-of-bounds and CPU exhaustion attacks.
  ↳ No PR: [8e008cb](https://github.com/openssl/openssl/commit/8e008cb8b23ec7dc75c45a66eeed09c815b11cd2)
- Forced OpenSSL internal DRBG to always use derived functions, and removed the optional use_df parameter to meet FIPS validation requirements.
  ↳ No PR: [260ecea](https://github.com/openssl/openssl/commit/260ecea0d4e46d63464636405f9925ef65d0747e)
- Added zeroing of public keys when releasing ECX keys to comply with FIPS security requirements.
  ↳ No PR: [04812ed](https://github.com/openssl/openssl/commit/04812ed1de6db39f2a5cc758151ddb167afe4965)
- In the FROS and WOTS implementations of SLH_DSA, added zeroing operations for secret keys and temporary buffers, and adjusted error handling paths to ensure sensitive data is cleared correctly.
  ↳ No PR: [ce3acbd](https://github.com/openssl/openssl/commit/ce3acbd07e4c3ea83ca7fb3629e8a0de3c8d7d8a)
- In the FIPS self-test module, temporary output variables are cleared to meet the ISO/IEC 19790 security standard requirements.
  ↳ No PR: [5946465](https://github.com/openssl/openssl/commit/5946465a8745069afc6db1135e42a3cd718a37dc)
- Fixed a heap buffer overflow that could occur in the ossl_i2c_ASN1_BIT_STRING function when the data is all zero.
  ↳ No PR: [bf2dea0](https://github.com/openssl/openssl/commit/bf2dea0e2c6f1cfe1a8222088052ebcc63ab1004)
- Adjusted server address validation logic to only be disabled for new connections without a token, ensuring that tokens provided via NEW_TOKEN frames are still validated.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f443b40](https://github.com/openssl/openssl/commit/f443b4048d0cd8ec17df09b08b9cb04fc293d6de)
- Added send and receive credit tracking functionality for QUIC unauthenticated connections, logging and adjusting credit checking and consumption logic before connection verification is complete.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [eaa1a14](https://github.com/openssl/openssl/commit/eaa1a143aebba30c6f2a3fdb05b92ef0706c8abd), [d1c3bb2](https://github.com/openssl/openssl/commit/d1c3bb2f74845568d09b83fc8eb6cf9811482925)
- Fixed the security vulnerability (CVE-2024-12797) where the SSL_VERIFY_PEER flag did not take effect when using RPK. Now the client will abort the connection when the server X.509 verification fails, and relevant test cases have been added.
  ↳ No PR: [6ae8e94](https://github.com/openssl/openssl/commit/6ae8e947d8e3f3f03eeb7d9ad993e341791900bc)
- Added constant-time verification macros to ML-KEM's key generation, encapsulation and decapsulation functions to support detection of secret data-dependent side channels under Valgrind.
  ↳ No PR: [95d764a](https://github.com/openssl/openssl/commit/95d764a0440edcf88737061f8a7bd829ea329642)
- Fixed the timing side channel vulnerability (CVE-2024-13176) in ECDSA signature calculation, eliminating timing signals by introducing a fixed top modular exponentiation function.
  ↳ No PR: [63c40a6](https://github.com/openssl/openssl/commit/63c40a66c5dc287485705d06122d3a6e74a6a203), [c3144e1](https://github.com/openssl/openssl/commit/c3144e102571517df6c15ccc049fa3660ab3cb0a)
- Fixed a multi-threaded data race issue in the asn1_str2tag() function caused by the tntmp variable being incorrectly declared as static.
  ↳ No PR: [7262c0b](https://github.com/openssl/openssl/commit/7262c0bcc468ab8e43ba96ca219acdb4667e45e0)
- Rejected incorrect public key hashes in private keys, and refactored key management functions to enhance security and correctness.
  ↳ No PR: [8cc7ebf](https://github.com/openssl/openssl/commit/8cc7ebf6fed2a6c49dd71a090988d68390d0563c)
- Fixed the Minerva timing side channel vulnerability of the P-384 curve on the PPC platform: use bn_mul_mont_int in Montgomery multiplication instead, and rewrite the felem operation function implemented in assembly.
  ↳ No PR: [080c6be](https://github.com/openssl/openssl/commit/080c6be0b102934bf66daeac70f0863f209f8d0f)
- Before creating a QUIC channel, perform initial AEAD packet verification through the pre-created QRX object. After passing the verification, create the channel and pass in the QRX.
  ↳ No PR: [c14ae04](https://github.com/openssl/openssl/commit/c14ae04613528f42f31a6fff1c0fa5ae3be887bb)
- Expanded HTTP method checking in TLS record header verification, adding detection of PATCH, DELETE, OPTIONS and TRACE methods.
  ↳ No PR: [30fbc68](https://github.com/openssl/openssl/commit/30fbc68dd45107951f6c15ff0f0f5215202d6d84)
- Refactored the FIPS indicator check in keymgmt, using ossl_fips_ind_ec_key_check uniformly.
  ↳ No PR: [7ffb656](https://github.com/openssl/openssl/commit/7ffb65666f2bb29b8d747db1ac49a4352acf6e1e)
- Updated documentation to note that the SSLKEYLOGFILE mechanism allows decryption of application payloads.
  ↳ No PR: [5dffe6a](https://github.com/openssl/openssl/commit/5dffe6afb098bb74c204ebbb021af016591d32b3)
- Security fixes for CVE-2024-9143 and CVE-2024-12797 are documented in the CHANGES and NEWS files.
  ↳ No PR: [36254fd](https://github.com/openssl/openssl/commit/36254fda37fe169e136079404a3c32aeea35cbd4), [cf9d668](https://github.com/openssl/openssl/commit/cf9d6685fda656c07fab8527750284f4446a7372)
- Added missing error messages for cases where tag length validation fails in the AES-OCB algorithm.
  ↳ No PR: [645edf5](https://github.com/openssl/openssl/commit/645edf50f0274448174d9739543bf01b1708b2f5)
- Added amplification limit test case to QUIC interoperability test CI workflow.
  ↳ No PR: [e0ea913](https://github.com/openssl/openssl/commit/e0ea913f11cf64d000556bbf7cb9f8acdf6be4cb)
- Added a test to the daily run check test to verify that the test still passes after lowering the default TLS security level.
  ↳ No PR: [0958f5a](https://github.com/openssl/openssl/commit/0958f5a5bc47e2cca907a3bfaf14059c020324fd)
- Migrated fuzz-checker workflow to ubuntu-24.04, and fixed missing afl++-clang package.
  ↳ No PR: [c45fddd](https://github.com/openssl/openssl/commit/c45fddd5975797dab656849968fa010c2207a722)
- Enhanced the thread cleaner CI test, adjusted the configuration and added the test_lhash test item.
  ↳ No PR: [00a173a](https://github.com/openssl/openssl/commit/00a173af77c878065c1370a40782aac04c4c83a8)
- Disabled SLH-DSA algorithm support in memory sanitizer builds.
  ↳ No PR: [2ecc87f](https://github.com/openssl/openssl/commit/2ecc87fc94a58cc75551208dbd494a806a70f4b2)
- Added SLH-DSA enabled memory sanitizer run to daily check workflow.
  ↳ No PR: [03e9718](https://github.com/openssl/openssl/commit/03e9718a50c8273f52f161a47ec861ef69d9717e)

### Documentation
- Added a table of contents to the QUIC polling design document, and fixed a format indentation issue.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [9b149bb](https://github.com/openssl/openssl/commit/9b149bb20190328210369ca651ec5f096082c69c), [bf52454](https://github.com/openssl/openssl/commit/bf52454f2dc76b49ac43ba6aeabf604a3ca85054)
- Many text corrections have been made to Windows-related documents, including optimization of grammar, punctuation and wording.
  ↳ No PR: [85eb4f3](https://github.com/openssl/openssl/commit/85eb4f303f4fc9eb8edfd9be0f6f67d435af9972)
- Added status badges for QUIC interoperability tests to README, and fixed format issues with existing badges.
  ↳ No PR: [e7e48e7](https://github.com/openssl/openssl/commit/e7e48e7f6cbe34f7bbfdeee453eec184dd9b1fa1)
- Added detailed Doxygen documentation comments to QUIC client interop demo files.
  ↳ No PR: [1b114e3](https://github.com/openssl/openssl/commit/1b114e39ae52446b36b3615a545d66c605db1f17)
- Added missing OpenSSL 3.4 chapter link in NEWS.md.
  ↳ No PR: [314c327](https://github.com/openssl/openssl/commit/314c327b140fe5ba1a1fbd1bc8719875b6d3b39b)
- Added OpenSSL 3.5 version chapters to CHANGES.md and NEWS.md, and updated related release notes.
  ↳ No PR: [5c82588](https://github.com/openssl/openssl/commit/5c82588173d33222b33693f698bc9c7614675e9f), [0c6656a](https://github.com/openssl/openssl/commit/0c6656a7a31492ddd61e3d0d8b0e66645f4b2d6f), [d6ace59](https://github.com/openssl/openssl/commit/d6ace599edfba7f1487725993531578bfeb9663a)
- Changes to DRBG in the FIPS provider and the new PKCS#7 internal content verification feature are documented in CHANGES.md.
  ↳ No PR: [c788f1c](https://github.com/openssl/openssl/commit/c788f1c6be92d63ae4ec71776bc17e3e7b0b912f), [256f580](https://github.com/openssl/openssl/commit/256f580dcd2ea208b9f3e5dc357e893a21e683d2)
- Updated the wiki link in the documentation to point to the new GitHub Wiki location.
  ↳ No PR: [653f175](https://github.com/openssl/openssl/commit/653f1757822fd9aa084ec1b53c4c1a9a595e06b0)
- Added design documentation for using opaque objects to represent symmetric keys.
  ↳ No PR: [45f9d27](https://github.com/openssl/openssl/commit/45f9d271cd715f5acf9522ea807b2df3a9678bcc)
- Added and updated QUIC Server API design documentation, including function name modification and addition documentation.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f07ba7b](https://github.com/openssl/openssl/commit/f07ba7bccdca0182bfa50110549c48ff02881ca3), [4e63896](https://github.com/openssl/openssl/commit/4e63896f5acb7a67eca3ba8069ac7bc8ef443429)
- Several updates have been made to the QUIC polling design documentation, including new documentation, simplified cookie types, new SSL_CTX level settings, etc.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [c996bdc](https://github.com/openssl/openssl/commit/c996bdcd91e1d250e93dec32223c87d568766786), [1599def](https://github.com/openssl/openssl/commit/1599defd74784a5748435503540fa0304d20bc92), [0288567](https://github.com/openssl/openssl/commit/0288567452f28925a247c32e4b4a678e4a006d94), [e0a6626](https://github.com/openssl/openssl/commit/e0a66263c2a549a5ca0a28c418ffc10a21591b5f), [1be9378](https://github.com/openssl/openssl/commit/1be93781e8e6624042a2b32c1646581e05ad6ac1), [51771da](https://github.com/openssl/openssl/commit/51771dad69a37fb1285e6e11d9ed976bfe80d4e9)
- Updated the QUIC design glossary, adding and correcting several term definitions.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [332cc89](https://github.com/openssl/openssl/commit/332cc89bb8cbd6450a3cac88ef8c4e78b74bc3aa), [0c7063b](https://github.com/openssl/openssl/commit/0c7063bb6f85aeaac45a2a69b74fcef4298692e2)
- Added QUIC concurrency architecture design documentation.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [3686d21](https://github.com/openssl/openssl/commit/3686d215fe6da344e1190d7027f0c007662c7698)
- Updated the QUIC TLS design document, adjusting the callback function parameter names to match the new third-party QUIC stack API.
  ↳ No PR: [e6bb7ea](https://github.com/openssl/openssl/commit/e6bb7eaee057c195f2f512bd5e28d094b36d6855)
- Added EVP pipeline API design document.
  ↳ No PR: [81af0b0](https://github.com/openssl/openssl/commit/81af0b04cb61e4b3414e931fb1060ce39753af00)
- Fixed details about IPv6 host addresses in the documentation, clarifying that IPv6 addresses must be enclosed in square brackets, and fixing whitespace issues in the no_proxy option.
  ↳ No PR: [ac91bd8](https://github.com/openssl/openssl/commit/ac91bd88d9c6d37767f1a7941c0df8d92466572b)
- Added instructions to the documentation for non-interactive use of s_client, including using the -ign_eof option and input redirection.
  ↳ No PR: [26521fd](https://github.com/openssl/openssl/commit/26521fdcf4047d6b6c5a7cf14ac34323a6197266)
- Added detailed usage instructions, environment variable descriptions and code comments to the sample program quic-hq-interop.c.
  ↳ No PR: [e4bfcee](https://github.com/openssl/openssl/commit/e4bfcee240564fdf8479e63cedc8f8bf4e7479dc)
- Updated RADIX test README to note that QUIC connections no longer need to explicitly set ALPN and explicitly use OP_END.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [2b21d3a](https://github.com/openssl/openssl/commit/2b21d3ac183d9f319cd198afe89d48bdf020c2e1)
- Added README documentation to the QUIC examples directory, stating that this directory contains examples of the OpenSSL QUIC API.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [03ca681](https://github.com/openssl/openssl/commit/03ca681728c64d2defce971d0ed51215de799381)
- Added configuration support for Embarcadero-Borland Clang Compiler 64 (BCC64), and updated Windows build documentation.
  ↳ No PR: [bbd1811](https://github.com/openssl/openssl/commit/bbd181166391e4e1fd0a647f43b8b239609298ea)
- Added documentation comment for RSA KEM's encapsulation and decapsulation operations stating that the output buffer length parameter must be set correctly.
  ↳ No PR: [1c1223f](https://github.com/openssl/openssl/commit/1c1223ff535944de880a23cbf0ef9bba6092b0d9)
- Added HISTORY chapter and description of options added in multiple versions to the documentation of openssl-fipsinstall command.
  ↳ No PR: [634d843](https://github.com/openssl/openssl/commit/634d84324a463317cea52510c62d8bafc2ff1eb0), [1b52b24](https://github.com/openssl/openssl/commit/1b52b24aa4deb76831a56afb0aa7a101877cd457), [9331a20](https://github.com/openssl/openssl/commit/9331a202fe85cba18aae54b52bcfcf71c2a4469f), [3be6387](https://github.com/openssl/openssl/commit/3be63875881f823f3eba38e7674d64bc28f771c8)
- Uniformly change app and apps in CHANGES.md to command and commands to maintain terminology consistency.
  ↳ No PR: [7086332](https://github.com/openssl/openssl/commit/70863325507a4dbb991f35c3f71b4fc3099433cf)
- Updated openssl-pkeyutl documentation to correct inaccuracies in default operations, option descriptions, and default digest algorithms.
  ↳ No PR: [26a826c](https://github.com/openssl/openssl/commit/26a826c2d1345ce51bda0faf929a54ff803984dc), [012353b](https://github.com/openssl/openssl/commit/012353bdf21b98def920ac317b94c4a9ed501b79), [cbb1609](https://github.com/openssl/openssl/commit/cbb16094c32235e7d85b663e45e21efdce6a9ea2), [0a08629](https://github.com/openssl/openssl/commit/0a0862969f954dddaae12cf7b598bed6016a55d7)
- Fixed incorrect order of arguments for the encryption example command in openssl-smime documentation.
  ↳ No PR: [1d160db](https://github.com/openssl/openssl/commit/1d160dbf39fbdba89389ddff54e45bacf278b04a)
- Fixed an issue where the default_md example in the openssl ca documentation incorrectly used md5, corrected to sha256.
  ↳ No PR: [d1669a1](https://github.com/openssl/openssl/commit/d1669a14d129c9b12c8ef5ccd3545273e50aad0f)
- Removed reference to git.openssl.org from README.md, and updated download link and repository description.
  ↳ No PR: [5f9814d](https://github.com/openssl/openssl/commit/5f9814d95cc16a6e45e45cc2afe8b98c1eeead25)
- Added description of the purpose of default certificate chain verification in the man pages of openssl-cms, openssl-s_client and openssl-s_server.
  ↳ No PR: [a82c2bf](https://github.com/openssl/openssl/commit/a82c2bf5c9db9d00f16281b48c1e1430a6cfd76e)
- Fixed missing HISTORY entries in documentation and added checking for HISTORY chapters in the find-doc-nits tool.
  ↳ No PR: [50ef944](https://github.com/openssl/openssl/commit/50ef944cd66135d90ab71d9dcce0ca7cfbc44aca)
- Added ML-DSA design document.
  ↳ No PR: [2ca3196](https://github.com/openssl/openssl/commit/2ca319684c11a913e526a290722d77d3c3a41485)
- Moved crypto/bn/README.pod to the internal manpage directory doc/internal/man3/bn_mul_words.pod, and removed obsolete information.
  ↳ No PR: [6812bbc](https://github.com/openssl/openssl/commit/6812bbcf9455b23f7c54dea1ca6dd5e2341686c7)
- Updated the OpenSSL documentation link in the documentation README and removed the obsolete standards.txt section.
  ↳ No PR: [da44eb2](https://github.com/openssl/openssl/commit/da44eb2901bd541f86547d814f45ab305b918611)
- Minor revisions to the documentation of the CMP command, including revised wording, updated descriptions of CRL-related options, and adjustments to example commands.
  ↳ No PR: [1d3da36](https://github.com/openssl/openssl/commit/1d3da367ab404dd0129277b6b9518d50175269d6)
- Updated NEWS.md before release, adding missing change notes and new feature list.
  ↳ No PR: [2df40ea](https://github.com/openssl/openssl/commit/2df40ea6ffde5937f7eeb3473f1066b4e57d3463)
- Updated documentation to describe new QUIC server support, including README and CHANGES/NEWS.
  ↳ No PR: [0895873](https://github.com/openssl/openssl/commit/089587394219c351ee86c8f96717123637d57332), [828361e](https://github.com/openssl/openssl/commit/828361eff8f627864b49fb66a20dd83b55c53dd5), [b48145c](https://github.com/openssl/openssl/commit/b48145cd189734de287afae79a0723361a05ddca)
- Updated version number examples and descriptions in the FIPS-README.md document to reflect the latest FIPS validated version.
  ↳ No PR: [3e2f1a8](https://github.com/openssl/openssl/commit/3e2f1a8d4a3deee0e70965710ab35a967aa8dbd0)
- Added OpenSSL 3.5.0 known issues list in NEWS.md.
  ↳ No PR: [3e80d1f](https://github.com/openssl/openssl/commit/3e80d1f3344cdd1cb1e58d79960a753790ce9915)

### Build/CI
- Fixed incorrect variable reference in die statement in build script configdata.pm.in.
  ↳ No PR: [578760b](https://github.com/openssl/openssl/commit/578760bb6aae6a9d7f3805eea66bab124d06c9b0)
- Add conditional compilation protection for the ossl_rand_jitter_get_seed function, excluding this function when OPENSSL_NO_FIPS_JITTER is defined.
  ↳ No PR: [a7c0fa6](https://github.com/openssl/openssl/commit/a7c0fa601ec29d7a42890aae1e3bccfa0eac896f)
- Fix the generated format of hash files in published assets to make it consistent with the coreutils format.
  ↳ No PR: [808a086](https://github.com/openssl/openssl/commit/808a0861716e6dd5e1c9f08cebec93084f028fd8)
- Removed temporary optimization level reduction for an old ppc64le compiler bug that was fixed in the Ubuntu 20.04 update.
  ↳ No PR: [3e9790a](https://github.com/openssl/openssl/commit/3e9790a2556ee67dffa5f1aeb102caa4e0364982)
- Fix release process: GitHub Release is correctly marked as a pre-release version when the tag name contains alpha or beta.
  ↳ No PR: [2a6d875](https://github.com/openssl/openssl/commit/2a6d875c9017497e9fc26e385ea84f2716d85e1c)
- Allow build products to be uploaded even when tests fail.
  ↳ No PR: [3dd5147](https://github.com/openssl/openssl/commit/3dd514757e55ea13059f22e242ce998ff436fded)
- Fix compilation error caused by mismatched printf format specifiers on macOS.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [7492a44](https://github.com/openssl/openssl/commit/7492a44391b44a790b2df37428ea821f50fd6511)
- Updated the build configuration and documentation of the NonStop platform, added KLT kernel-level threading model support, and fixed the circular dependency problem of the old version of GCC.
  ↳ No PR: [ad1d0cc](https://github.com/openssl/openssl/commit/ad1d0cc99909b93b150ef197034ec05f428b74f9), [6288aa4](https://github.com/openssl/openssl/commit/6288aa440c1ba111eaf52cf79659a25329205022)
- Update version of actions/setup-python action in CI workflow.
  ↳ No PR: [06aa41a](https://github.com/openssl/openssl/commit/06aa41a5f529fc2081793c8bfb36c7e2727665d5), [8af4c02](https://github.com/openssl/openssl/commit/8af4c02ea952ca387691c4a077c260ba045fe285)
- Added GitHub Actions workflow for running QUIC interoperability tests.
  ↳ No PR: [36d5b38](https://github.com/openssl/openssl/commit/36d5b38d2bc01ee8a910060a32b806fab0584b78)
- Adjust Windows CI configuration and reduce the operating scope.
  ↳ No PR: [a4954ea](https://github.com/openssl/openssl/commit/a4954ea01a5665df2963d0e8e7d86997793c37c6)
- Updated actions/download-artifact dependency in CI workflow to v4.1.8.
  ↳ No PR: [65e32c6](https://github.com/openssl/openssl/commit/65e32c6867bb0a3905f07dfd5edb484e65269eb9)
- Modify implementations.json to use jq command instead in QUIC interoperability testing workflow.
  ↳ No PR: [d677482](https://github.com/openssl/openssl/commit/d677482b7e3d586a2fb31861b69db37cf6210ed7)
- Added recovery and multiplexing test cases to the QUIC interoperability test matrix, and removed redundant operations.
  ↳ No PR: [67b739f](https://github.com/openssl/openssl/commit/67b739fba178f1336a00d3147e0cae89905cb128)
- Added fips-jitter test configuration to CI daily checks.
  ↳ No PR: [b448cc1](https://github.com/openssl/openssl/commit/b448cc1ac4456b080900b39deb58973e13d1c7c1)
- Adjust the triggering method of daily check CI, including temporarily changing to push/PR triggering, and returning to scheduled scheduling.
  ↳ No PR: [4c44603](https://github.com/openssl/openssl/commit/4c44603d555ece65cb635ebe191f4000c88bb429), [6afaa3f](https://github.com/openssl/openssl/commit/6afaa3f41f5b65432b6700064b077032b9e0c625)
- Temporarily disable QUIC multiplexing tests to avoid failures in CI environments.
  ↳ No PR: [a941f5d](https://github.com/openssl/openssl/commit/a941f5d52e874a6d854e2e49290f69ec3048cc7a)
- Add external tests for pkcs11-provider and configure them to run in CI.
  ↳ No PR: [e9af1ea](https://github.com/openssl/openssl/commit/e9af1eaa54d020b407e1224b544053231fe16399)
- Made the Cleanup artifact step in fips-label.yml only execute when workflow_run succeeds.
  ↳ No PR: [27af422](https://github.com/openssl/openssl/commit/27af422b1c2be9fe588a80e6159d5a4758bd6c44)
- Added testing support for OpenSSL 3.4 version in CI, including provider compatibility testing and tag testing.
  ↳ No PR: [3cc2992](https://github.com/openssl/openssl/commit/3cc299258c5739853eb9d4a269b55f00bde7fa39), [c477fa5](https://github.com/openssl/openssl/commit/c477fa5a22ff27081b1725ecef21c61ae0d7a587)
- Add compilation options to Alpine edge's GCC to suppress false positive warnings generated by the new version of fortify-headers.
  ↳ No PR: [93d1bb6](https://github.com/openssl/openssl/commit/93d1bb6dff0f0126ef1a5cac7b8693308763eb8a)
- Reorganize external test jobs in CI, including renaming, integrating and adjusting test steps.
  ↳ No PR: [00776cb](https://github.com/openssl/openssl/commit/00776cba0405008b1bbfc9c52bbfabf4c44220c9)
- Upgrade multiple GitHub Actions to the latest versions: Coveralls Action to v2.3.2, upload/download artifact to v4.
  ↳ No PR: [e524ac5](https://github.com/openssl/openssl/commit/e524ac548a628e4cef9fd5e722720c0fd48f41a8), [5dbcfbf](https://github.com/openssl/openssl/commit/5dbcfbff166e9f1d8ff15a15ecab7af6d11f9cf0)
- Update provider compatibility CI branch support, add openssl-3.5 branch, and remove the discontinued 3.1 branch.
  ↳ No PR: [c0d57de](https://github.com/openssl/openssl/commit/c0d57de67407ac40ef6361e9e2357fdc46bf8039), [090ef92](https://github.com/openssl/openssl/commit/090ef925d0bb17ed9729f1773b0b3c76343460c0)
- Added support for openssl-3.5 branch in coveralls CI workflow.
  ↳ No PR: [208aa3e](https://github.com/openssl/openssl/commit/208aa3e65d05a298db92763d8cfd301fcc4d9fa7)
- Improved QUIC interoperability test CI: added server workflow, introduced independent client list, added amplificationlimit test item, and fixed exclusion list configuration errors.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [d11c5b7](https://github.com/openssl/openssl/commit/d11c5b78af8ddb165a001457ae4970170d6b38b6) | No PR: [f7c4d45](https://github.com/openssl/openssl/commit/f7c4d4519cd5daad5335b39ba7a3c864c65bf6ee), [005721e](https://github.com/openssl/openssl/commit/005721e1a23d48558c3da816f093de4ea62bd265), [7c98290](https://github.com/openssl/openssl/commit/7c9829053de1918ab7cee0aa2d5178b95ab0a300)
- Adjust scheduled workflow execution time to after UTC 02:00; add workflow_dispatch manual trigger support for multiple workflows; add openssl-3.4 branch to coveralls workflow; remove hardcoded branch list from os-zoo workflow.
  ↳ No PR: [21f6c3b](https://github.com/openssl/openssl/commit/21f6c3b4fb35af03e1fedb3fc15d68846ed2235b)
- Replaced the macOS-12 runner in the os-zoo CI workflow with macOS-15 in anticipation of the runner's impending removal.
  ↳ No PR: [6a3d5b6](https://github.com/openssl/openssl/commit/6a3d5b6e62bf82639d0379e94e0581927251e638)
- Updated the Fedora base image in the CI workflow from 39 to 40, and fixed the provisioning outage issue.
  ↳ No PR: [0b234a2](https://github.com/openssl/openssl/commit/0b234a237c4dfe879dd83357c3933e34e9d4f166)
- Add -fno-sanitize=function to UBSan build options to disable sanitizer checking for function type mismatches.
  ↳ No PR: [5f0dab5](https://github.com/openssl/openssl/commit/5f0dab5e74b7cdb1b51217044966dc3927824a4d)
- Removed approval: otc review pending tag that no longer exists in Dependabot configuration.
  ↳ No PR: [76783a8](https://github.com/openssl/openssl/commit/76783a8286de8b86fbc48bc8a6976b79b33503d2)
- Simplify CI configuration: remove the ternary expression for selecting a runner based on the server URL and use fixed runner labels directly.
  ↳ No PR: [5c5b8d2](https://github.com/openssl/openssl/commit/5c5b8d2d7c59fc48981861629bb0b75a03497440)
- Swap jitter and no-ct jobs between daily CI and push CI.
  ↳ No PR: [5fce85e](https://github.com/openssl/openssl/commit/5fce85ec52a826d53665552b50e67f86c92dc394)
- Added test case for -DOPENSSL_PEDANTIC_ZEROIZATION compile option in daily CI check.
  ↳ No PR: [ce4b244](https://github.com/openssl/openssl/commit/ce4b2444156d834f620774d90ef94ffda66addb5)
- Fixed the removal problem of ABI change labels in fips-label.yml: corrected the label name from severity: fips change to severity: ABI change.
  ↳ No PR: [85f1758](https://github.com/openssl/openssl/commit/85f17585b0d8b55b335f561e2862db14a20b1e64)
- Merge no-ec2m with enable-fips options in CI configuration file run-checker-merge.yml to expose more potential errors.
  ↳ No PR: [dfc5ba8](https://github.com/openssl/openssl/commit/dfc5ba8afa39bdb8be430858425d6726c03aa515)
- Temporarily disable gost-engine external tests in CI to resolve compilation failures caused by build environment upgrades.
  ↳ No PR: [e2f6484](https://github.com/openssl/openssl/commit/e2f6484939f0075919c393d0c3c3c26d7505dab1)

### Maintenance
- Adjust the code format in the Windows thread atomic operation function, correct long line breaks and preprocessor directive indentation to comply with coding standards.
  ↳ No PR: [9f4d8c6](https://github.com/openssl/openssl/commit/9f4d8c63e8cd4968b04c7696467b6f29b90722ef)
- Fixed the indentation format of preprocessing directives in header files to comply with code style specifications.
  ↳ No PR: [5bda5de](https://github.com/openssl/openssl/commit/5bda5de88b9a9307fb2cd586b6fb77ac1e9cf5da)
- Clean up style issues in the demo code, including removing redundant blank lines, adjusting indentation, adding function declarations, correcting parameter passing and restructuring comments.
  ↳ No PR: [a62fb94](https://github.com/openssl/openssl/commit/a62fb94609308d14187808a19ae7c0eb8b7980ca)
- Corrected the indentation format of BN_secure_new function.
  ↳ No PR: [a1f07a0](https://github.com/openssl/openssl/commit/a1f07a0049cb33a880bfcc359c6a911cafb2b791)
- Add spaces to ASN1 macro definitions to make the code clearer.
  ↳ No PR: [282c405](https://github.com/openssl/openssl/commit/282c405818eaa1d075a517046812972748dc012f)
- Removed the debug code in the QUIC implementation that starts the SSL handshake when accepting the connection.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f420368](https://github.com/openssl/openssl/commit/f42036822ef299fdfed0712730e525eca9b5db4a)
- Added funding.json file to declare project funding information.
  ↳ No PR: [563f6b6](https://github.com/openssl/openssl/commit/563f6b65730fa4c2fd737e76c370930bfb205855)
- Clean up QUIC server-related TODO comments, update tags and remove outdated instructions.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [f13ef23](https://github.com/openssl/openssl/commit/f13ef23371a3d2453af601b2efbf5d9f5238d111)
- Fixed the indentation of goto tags in multiple functions to comply with code style.
  ↳ No PR: [c2f5086](https://github.com/openssl/openssl/commit/c2f50863b5c1cf71cd32dc8f2d156be8d89f069d)
- Fixed code format issues in quicapitest.c.
  ↳ No PR: [7ac924c](https://github.com/openssl/openssl/commit/7ac924c2ef5250e0424abc1587b56f70962a79a6)
- Added support for multiple stream polling and batching of stream requests in the QUIC hq-interop example.
  ↳ No PR: [34d6ec8](https://github.com/openssl/openssl/commit/34d6ec804b83eba213c5f5a13c9ab405c9832ed5), [1b6638b](https://github.com/openssl/openssl/commit/1b6638b1d83524b90d2e626b2050b173b3012ee7)
- Add support for SSL_CIPHER_SUITES environment variable in quic-hq-interop examples.
  ↳ No PR: [5f43a33](https://github.com/openssl/openssl/commit/5f43a3376bd3e9560141f390eee0e12a77279a83)
- Improve the HTTP/3 demo server, add file path prefix support, optimize content type handling, and adjust SSL event processing logic.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [887f6c0](https://github.com/openssl/openssl/commit/887f6c06a11fba4f99d01462c67bc5f9b3fb3c81), [2d080ca](https://github.com/openssl/openssl/commit/2d080ca544c416ed51210e6bbf679bcff3377d3d), [6ba49e3](https://github.com/openssl/openssl/commit/6ba49e30d8b241166880b738aa8809eb44c76400), [511c37b](https://github.com/openssl/openssl/commit/511c37b88cd4013be2b70a9d48e637da17417ddd)
- Add read retry mechanism for QUIC interop server.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a99c76d](https://github.com/openssl/openssl/commit/a99c76d94cc4744f94cfbe16cb9e465f9bf35582)
- Added QUIC server usage example, adjusted socket creation to use only IPv4 address family.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [368fc8d](https://github.com/openssl/openssl/commit/368fc8d486d4c427e5186e03dff14ffd9157c8a8), [20eb1b6](https://github.com/openssl/openssl/commit/20eb1b656b5e9b309bba7daa60e619f8a0d6168d)
- Improve the usability of the -rawin option in pkeyutl so that it is automatically implicit for algorithms such as Ed25519/Ed448.
  ↳ No PR: [c7764da](https://github.com/openssl/openssl/commit/c7764dacdf2d21d859b6f0b9c01500cda17f52c2)
- Clarify that the http_server_init() function supports both IPv4 and IPv6.
  ↳ No PR: [ec4b123](https://github.com/openssl/openssl/commit/ec4b123a96938162e7b926ffd7a0512c5d0b12f0)
- Add detailed error messages and error handling in ossl_rio_notifier_init and related functions.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [0e47037](https://github.com/openssl/openssl/commit/0e470373ad683cb523685931461f3076b7c3e9d5)
- Add IANA assigned numbers for new TLS supported groups (SecP256r1MLKEM768 and X25519MLKEM768).
  ↳ No PR: [22c2928](https://github.com/openssl/openssl/commit/22c2928a9a6e7c8e4f6f91e0557248b07ae03664)
- Removed redundant FD_SET calls in quic-server-non-block example.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [417a8e8](https://github.com/openssl/openssl/commit/417a8e8812e99420218e899ba06fe96ee7721f5f)
- Adjust the format of the namingAuthority part when printing the admission extension, correct the field names and increase the indentation.
  ↳ No PR: [85a52f7](https://github.com/openssl/openssl/commit/85a52f7292cb57662f823e4ac1a303f56d0531bf)
- Corrected the syntax error in comments and code that a SSL is an SSL, and used the correct SSL object pointer in client Hello processing instead.
  ↳ No PR: [ef39dd0](https://github.com/openssl/openssl/commit/ef39dd058ba2a0e24e92c1c5c97810bba9b6cbe0)
- Added sys/socket.h header file inclusion in sample programs for OpenBSD platform.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [ecf6701](https://github.com/openssl/openssl/commit/ecf67019075f6bb46b250e4850756cfe3c355015)
- Check the return values of multiple sk_*_push functions and perform appropriate error handling in case of failure.
  ↳ No PR: [bd0a2e0](https://github.com/openssl/openssl/commit/bd0a2e0c1eac69e83379dedbb80b348600daddcb), [c626fda](https://github.com/openssl/openssl/commit/c626fda8a66a203d9f1435c34fcd3f7bda89d068)
- Updated ML-DSA encoder implementation to adapt to master branch changes.
  ↳ No PR: [c83e6c0](https://github.com/openssl/openssl/commit/c83e6c0a2c796f5f733c1956a79cf290fe341ec9)
- Delay plans for several QUIC unimplemented features (RETIRE CONN ID, retry/version negotiation frame, SSL_LISTENER_FLAG_NO_ACCEPT, connection close frame boundary handling) to a future release.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a08e9ae](https://github.com/openssl/openssl/commit/a08e9aec1d0de813f1885e52dc8b1711ad803089), [a6f3110](https://github.com/openssl/openssl/commit/a6f3110318dda041461863d2830c3b356e7c6f0f), [3f06ebc](https://github.com/openssl/openssl/commit/3f06ebcfe39ea2d386061d264fa094eff4d533f3), [7d5426c](https://github.com/openssl/openssl/commit/7d5426c703d24a8a6867db4900a5a02f78619379)
- Move token store type definition to quic_predef.h header file.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [c536754](https://github.com/openssl/openssl/commit/c536754fd062a38dba31dbb069c3b5f623f6530f)
- Record the peer temporary key name and adjust the output information to distinguish the peer and server.
  ↳ No PR: [a39dc27](https://github.com/openssl/openssl/commit/a39dc27c2573da14e85ca8961970c82009bd4ff6)
- Add ssl_unwrap.h header file reference in quic_tls_api.c.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [8b0fbe2](https://github.com/openssl/openssl/commit/8b0fbe224abc75046cf2f365d6db7c86028387d5)
- Skip pairwise testing of ML-DSA, ML-KEM and SLH-DSA key generation during FIPS self-test.
  ↳ No PR: [50f995f](https://github.com/openssl/openssl/commit/50f995ff8c31bcdd2d812df8a842a3d83e089e2c), [5811c0e](https://github.com/openssl/openssl/commit/5811c0e8cf18aef271d75bc1d966c74efdd0b6b8), [ca26db3](https://github.com/openssl/openssl/commit/ca26db30a0bebbf491f5c976949c0645ceedabf4)
- The certificate signing algorithm name in s_client is now output using a long name.
  ↳ No PR: [d900467](https://github.com/openssl/openssl/commit/d900467b2a5abfaf4fab1241373894dca6d363f9)
- Update CI configuration: add no-shared option to sanitizer build, replace self-hosted runner with GitHub hosting, simplify coveralls exclusion rules, migrate compiler test environment to ubuntu-22.04.
  ↳ No PR: [01e657c](https://github.com/openssl/openssl/commit/01e657c5468a637959395b07b385e58785c486f2), [ea71f8c](https://github.com/openssl/openssl/commit/ea71f8cd40358bf11f2ef9a256bf99c5929379fb), [74cbe9d](https://github.com/openssl/openssl/commit/74cbe9d1a4613007968c2a320051fc6bb0f4081d), [4e9b542](https://github.com/openssl/openssl/commit/4e9b542868890428f0294a4ce53fcde68c1fcaf7)

### Others
- Optimize the tracking output of HTTP client request/response headers and bodies, and improve the processing of error response content.
  ↳ No PR: [efb6219](https://github.com/openssl/openssl/commit/efb621941a04a19e3975733679124b2618c47e91)
- Adjust pkeyutl command options: -digest implies -rawin, and can only be used with -sign or -verify.
  ↳ No PR: [50c0241](https://github.com/openssl/openssl/commit/50c0241de28ac53bdbc2fcb6b41688fff0add141)
- Add README documentation for QUIC RADIX testing framework.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [dc2bff5](https://github.com/openssl/openssl/commit/dc2bff5e583137facfd2b92826a646404b9ead05)
- Added FIPS indicator requirements document.
  ↳ No PR: [7845ff7](https://github.com/openssl/openssl/commit/7845ff7692ac3a2bc1f8bf1eb9fa1ec1119f9b79)
- Fixed description, spelling and macro definition errors in QUIC design documents.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [19c55d5](https://github.com/openssl/openssl/commit/19c55d559fb4cd6e9a1fb3bfac86e66836e50f73), [ce13151](https://github.com/openssl/openssl/commit/ce1315140babc8b062f938b0b1ddfca58feb8fbc), [362cc00](https://github.com/openssl/openssl/commit/362cc00d6aeed238a90360689a51fe41d6dc2422)
- Fix the Markdown format of code blocks in README.md and add language identifier.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [8df5b72](https://github.com/openssl/openssl/commit/8df5b725efea41f103f879b46c2be72ba45c79b2)
- Made comments for the QUIC context (QCTX) flag clearer.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [e88f03f](https://github.com/openssl/openssl/commit/e88f03f19338f5f407ae06ed08ea5d4f77fb4570)
- Add copyright header to demos/quic/server/server.c.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [6330a78](https://github.com/openssl/openssl/commit/6330a78638286526bcfa38b374dcfd096eb014bc)
- Adjust the code format of the two loops in the QUIC implementation, no functional changes.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [e6f0626](https://github.com/openssl/openssl/commit/e6f062601bb9df5225d46cd00d6379bc125e091c)
- Correct the comment about the default nonce length in demos/cipher/aesccm.c.
  ↳ No PR: [f2b7a00](https://github.com/openssl/openssl/commit/f2b7a00fbb372b0ea32f2cfea865ab407641b1fa)
- Fixed display problem of code examples in openssl-ts.pod.in document.
  ↳ No PR: [6fd9bc6](https://github.com/openssl/openssl/commit/6fd9bc65689cf62854797927121a580bed1565c4)
- Fixed typos in comments in drbg_local.h.
  ↳ No PR: [ff157ee](https://github.com/openssl/openssl/commit/ff157ee2f0b081d9f2dc2e8f7780f34c1e7e1c4f)
- Remove outdated comments.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [3a75cf8](https://github.com/openssl/openssl/commit/3a75cf8d9c0691240b1b00f94cab84471dcc1549)
- Correct parameter names in nc_match_single function declaration to maintain consistency.
  ↳ No PR: [4f48629](https://github.com/openssl/openssl/commit/4f48629c9d791c9105f2d68f4a4d0b0085e8e0ca)
- Clean up and correct formatting and spelling errors in the external test README document.
  ↳ No PR: [7832374](https://github.com/openssl/openssl/commit/7832374ffb127e268653e7ee4d753a3754c02c89)
- Fix code format and style issues to make it comply with inspection requirements.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [a50a6ef](https://github.com/openssl/openssl/commit/a50a6efd079d257aaa1724bcc5b5ba5f9024068f)
- Fixed typos in README document.
  ↳ No PR: [6f2c97d](https://github.com/openssl/openssl/commit/6f2c97d50a59033a78ac8edc7e72e7afb17e3c79)
- Add ignore rules for files generated in the demo directory in .gitignore.
  ↳ No PR: [69d0d93](https://github.com/openssl/openssl/commit/69d0d93954f00e3b3506c1fa530e345f10898a02)
- Fixed typos in engine.h header file comments.
  ↳ No PR: [0b05db0](https://github.com/openssl/openssl/commit/0b05db0e2000b9dc34feefe55c4093a14e31cfed)
- Delete a redundant break statement in the write_state_machine function in ssl/statem/statem.c.
  ↳ No PR: [764a876](https://github.com/openssl/openssl/commit/764a876b6410fda701b56b4d3abeb57e2b57194b)
- Remove redundant brackets to keep code style consistent.
  ↳ No PR: [c77d9fc](https://github.com/openssl/openssl/commit/c77d9fcf8ea847220990847e05b8d7b1d40e540c)
- The terminology of complement codes in unified code.
  ↳ No PR: [8a74ed5](https://github.com/openssl/openssl/commit/8a74ed56191b77151371b2ef6240e662ac671f5b)
- Add blank lines in async_wait.c to keep the code style consistent.
  ↳ No PR: [df6a69a](https://github.com/openssl/openssl/commit/df6a69a85024b4d96e367e40a3434f59ba68a3ff)
- Fixed typos in comments.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [fe2a51b](https://github.com/openssl/openssl/commit/fe2a51bfda7c8a718a5b0658c7c2a1a1a7c969b4)
- Adjust comment formatting and wording in ASN1 integer handling functions.
  ↳ No PR: [2e407ea](https://github.com/openssl/openssl/commit/2e407ea5c6d24c74531d99eb8c5a8f074542a98c)
- Fix duplicate words in comments in test files.
  ↳ No PR: [690bb51](https://github.com/openssl/openssl/commit/690bb5192c7ef36f427dddf9719b938d76837b23)
- Fixed typos in header file comments.
  ↳ No PR: [c8bee68](https://github.com/openssl/openssl/commit/c8bee6818520293171af44b197d057d839febf0a)
- Fix typo in comments in QUIC port code.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [6d25809](https://github.com/openssl/openssl/commit/6d25809cd0e599c5b17e46c042d25aba455a9c2a)
- Clean up comments for ASN1_STRING and improve documentation examples.
  ↳ No PR: [2e36bb0](https://github.com/openssl/openssl/commit/2e36bb07b50a1dc55f97aeccbec9fbc5048290d1)
- Updated ML-KEM design document, adjusted description and reference format.
  ↳ No PR: [7772dbb](https://github.com/openssl/openssl/commit/7772dbb17cbd3f7f2d666e414a3e03f7ad31ebb2)
- Maintain error code definitions, synchronize numbers and remove non-existent error codes.
  ↳ No PR: [5b81f94](https://github.com/openssl/openssl/commit/5b81f942d5011fbb05d0dc7016af05161b3ba010), [0b1d3eb](https://github.com/openssl/openssl/commit/0b1d3ebb70a13917cf28ed934150c29819d95997)
- Clean up QUIC related TODO comments, remove irrelevant items and update them for future plans.
  ↳ [#26802](https://github.com/openssl/openssl/pull/26802): [54dcb37](https://github.com/openssl/openssl/commit/54dcb3740b5c6a82fad1c1ba507d8041cd179edd), [1f23dbb](https://github.com/openssl/openssl/commit/1f23dbb62d69493fafdeb32958d8cb1834101478), [05ea152](https://github.com/openssl/openssl/commit/05ea15261c6d18df4345785ae1a15799f7a3bace)
- Fixed spelling, grammatical and arithmetic errors in code comments.
  ↳ No PR: [cc5403f](https://github.com/openssl/openssl/commit/cc5403f33ae9c3a367ca4a578baf86d1abb485d6), [edb3824](https://github.com/openssl/openssl/commit/edb3824604be4faada6eb028a0c624bcb1d56184), [7a8fe56](https://github.com/openssl/openssl/commit/7a8fe56da8a52a12100a0ee7f4a17eb6810a1c11)
- Updated documentation, added ML-KEM backlog comment and corrected description of X25519/X448/Ed25519/Ed448.
  ↳ No PR: [e04a604](https://github.com/openssl/openssl/commit/e04a604d0dbc6a50c48e21a4658afc2a6fb2d445)
- Fix misspelling of OSSL_WINCTX macro name in Windows build instructions.
  ↳ No PR: [c2ab75e](https://github.com/openssl/openssl/commit/c2ab75e30a211aa278f8da1f0f040f9368adb81d)
- Updated author attribution in SLH-DSA changelog.
  ↳ No PR: [11f4eaf](https://github.com/openssl/openssl/commit/11f4eaf1973e5945a5441cd4ce37cfe83051ea38)
- Updated the README for external tests, removed the environment variable description for skipping tests and added a link to oqsprovider operation restrictions.
  ↳ No PR: [c535b28](https://github.com/openssl/openssl/commit/c535b28baffdfe8606721443a1a5819cf529955c)
- Synchronize CHANGES.md file, update version number and date and fix format.
  ↳ No PR: [624a00e](https://github.com/openssl/openssl/commit/624a00ef41599a6b4db25b16bf21d730ec34f2e4)
- Fix documentation description of no-tls-deprecated-ec configuration option in CHANGES.md.
  ↳ No PR: [89dbc6a](https://github.com/openssl/openssl/commit/89dbc6a62cdfb9185527ef585a3d6c5f02763647)
- Adjust the case of variant letters in SLH-DSA algorithm OID definition.
  ↳ No PR: [b049ce0](https://github.com/openssl/openssl/commit/b049ce0e354011be075e620b9ba7cf4d7c8f9577)
- Remove unused tags in test file slh_dsa_test.c.
  ↳ No PR: [ecc1740](https://github.com/openssl/openssl/commit/ecc174065add643c8cb03b70672bfe92ea1333e5)
- Added missing entries in .gitignore to prevent demos directory build products from being tracked.
  ↳ No PR: [e8387ed](https://github.com/openssl/openssl/commit/e8387ed61c5f434e3436cc2950dded431246e226)
- Add binary attribute configuration for ML-KEM codec test data files.
  ↳ No PR: [1811f99](https://github.com/openssl/openssl/commit/1811f990f9349d75001c4c52f8d4694fab7c773f)
- Updated copyright year, added missing copyright header, and removed legacy TODO comments.
  ↳ No PR: [6ab8772](https://github.com/openssl/openssl/commit/6ab87724e6bdd51ddd4f63488bc1afc9d9e8243e)
- Fixed case error in sponsorship program status field in funding.json.
  ↳ No PR: [0f665e8](https://github.com/openssl/openssl/commit/0f665e87c7082d358e6ad709d048595f8df85fc2)
- Removed duplicate options and added duplicate option markers in multiple man pages.
  ↳ No PR: [380d7f3](https://github.com/openssl/openssl/commit/380d7f3c28734baf477530788bb93b1ebceac779)
- Fixed a double-free problem caused by missing pointer nulling in the quic-hq-interop test.
  ↳ No PR: [0cfbeba](https://github.com/openssl/openssl/commit/0cfbeba8ed5fea4e5a85e03c5ce33fe3e6cb07ab)
- Updated copyright year in multiple source files to 2025.
  ↳ [#27038](https://github.com/openssl/openssl/pull/27038): [0c679f5](https://github.com/openssl/openssl/commit/0c679f556669e32499a827a081afe3bcf973c9ad) | No PR: [b17e3bb](https://github.com/openssl/openssl/commit/b17e3bb6ce82cf01371eefd9f5ee45573b76ec47), [eb917f4](https://github.com/openssl/openssl/commit/eb917f429337c883c49f82270b1ced7b45c0adb7)
- Update version information in the changelog and news documentation for the OpenSSL 3.5 release.
  ↳ No PR: [8fabfd8](https://github.com/openssl/openssl/commit/8fabfd81094d1d9f8890df4bee083aa6f77d769d), [156e0f3](https://github.com/openssl/openssl/commit/156e0f345c37d82d1519322122205cd34517ed07), [2862323](https://github.com/openssl/openssl/commit/286232311647ab5b6350c11c5cb1f1fa1cfa9a39), [636dfad](https://github.com/openssl/openssl/commit/636dfadc70ce26f2473870570bfd9ec352806b1d)
