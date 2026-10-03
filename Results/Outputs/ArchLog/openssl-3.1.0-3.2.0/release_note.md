# Release Note

## Important Changes

### Core Cryptographic and Protocol Library
- Reconstruct the QUIC record layer, add complete implementations of the sender (QTX) and receiver (QRX), support shared encryption level management, key updates and AEAD restrictions. (Architecture event: QUIC record layer reconstruction)
  ↳ No PR: [1957148](https://github.com/openssl/openssl/commit/1957148384c72ea7bc33a5c415d8f84526ed6480), [043a41d](https://github.com/openssl/openssl/commit/043a41ddeeaabc192c25aa0b46ccfc4546e4d3df)
- Added QUIC I/O reactor framework, which provides initialization, polling, network read and write status judgment, tick callback and blocking waiting functions. (Architecture event: QUIC I/O reactor framework)
  ↳ No PR: [6952321](https://github.com/openssl/openssl/commit/69523214ee5a718a0f24803a93bedf0795578173)
- Added the record method header file recordmethod.h to define the record/packet protection interface. (Architecture-related: public API)
  ↳ No PR: [79a1f3e](https://github.com/openssl/openssl/commit/79a1f3e4bb62c10d9604718f6814bb8bdde4ffd6)
- Added header file e_ostime.h to ensure that struct timeval is correctly defined when including ssl.h. (Architecture-related: public API)
  ↳ No PR: [6cf23ce](https://github.com/openssl/openssl/commit/6cf23ce54d4b9e3b11c8b4807c62ecba27e3aa16)
- Allow the use of empty passwords in PEM_write_bio_PKCS8PrivateKey_nid. (Architecture-related: public API)
  ↳ No PR: [1d28ada](https://github.com/openssl/openssl/commit/1d28ada1c39997c10fe5392f4235bbd2bc44b40f)
- Support password-based PKCS12 files without MAC. (Architecture-related: public API)
  ↳ No PR: [cfd24cd](https://github.com/openssl/openssl/commit/cfd24cde81aa5f63dba41ddcde0fa3c5d64e1db0)
- Added the general atomic addition macro tsan_add, and reconstructed the existing macro. (Architecture-related: public API)
  ↳ No PR: [b0b456f](https://github.com/openssl/openssl/commit/b0b456f8c8b628c3d7e212339e31cbfd06ac4ec8)
- Prevent the HPKE sender from setting the sequence number unreasonably and require the role to be explicitly specified when creating the context. (Architecture-related: public API)
  ↳ No PR: [cae72ee](https://github.com/openssl/openssl/commit/cae72eefc3fbdd2f7a1a065f237bf3943619bca2)
- Fix CertReqId usage of p10cr transaction in CMP protocol to make it comply with RFC 4210 specification. (Architecture-related: CMP protocol behavior)
  ↳ No PR: [25b18e6](https://github.com/openssl/openssl/commit/25b18e629d5cab40f88b33fd9ecf0d69e08c7707)
- When the system is not configured with a random source, RAND_add uses the entropy data provided by the user directly for reseeding. (Architecture-related: public API: RAND_add)
  ↳ No PR: [56547da](https://github.com/openssl/openssl/commit/56547da9d3fa24f54b439497d322b12beb004c80)
- Removed the old QUIC virtual handshake implementation, which has been replaced by the real TLS handshake. (Architecture-related: QUIC handshake implementation replacement)
  ↳ No PR: [c28f1a8](https://github.com/openssl/openssl/commit/c28f1a8bb9ccfecb76bcf3b7987e2a526b427bca)
- Separate the SSL/TLS record layer from the SSL object, migrate it to the new record layer module, reconstruct the reading and writing, encryption, MAC calculation, key derivation and other functions of TLS 1.0/1.1/1.2/1.3, DTLS and SSLv3, remove the direct dependence on the SSL object, introduce a new record layer method interface, and adjust the relevant public header files and function signatures. (Architecture event: Record layer reconstruction)
  ↳ No PR: [8577312](https://github.com/openssl/openssl/commit/85773128d0e80cd8dcc772a6931d385b8cf4acd1), [e2d5742](https://github.com/openssl/openssl/commit/e2d5742b1460c45bf39094ea08e4e85a8f507ea8), [4030869](https://github.com/openssl/openssl/commit/4030869d24309bfb5292e7bec41cd2b3012ba99d), [aedbb71](https://github.com/openssl/openssl/commit/aedbb71b6334a6cb616cf31cbb5de02109a2c5ed), [10560ae](https://github.com/openssl/openssl/commit/10560aed15dd71601b89c8f0308f30b70744c914), [2b891e3](https://github.com/openssl/openssl/commit/2b891e30ce1839a27f6a47f4c668d5810a15f847), [50023e9](https://github.com/openssl/openssl/commit/50023e9b7e2253c27e1a731c8bace64224aae0b8), [5b24990](https://github.com/openssl/openssl/commit/5b24990ba4b81ea576aac6c8711f7e9420bbee50), [1853d20](https://github.com/openssl/openssl/commit/1853d20a008a85d327f4faa9e07be40a85549f8e), [9cd9e09](https://github.com/openssl/openssl/commit/9cd9e0978b237ebb6cc4110532d95903b1c6bf5c), [88d6168](https://github.com/openssl/openssl/commit/88d616805cab4fd052bcff890627668a8f4bae33), [7f2f0ac](https://github.com/openssl/openssl/commit/7f2f0ac7bfdd676cd919dd94b971874eade41830), [9dd9023](https://github.com/openssl/openssl/commit/9dd90232d537f0ccd457fe1e23f4cbe83917c70a), [3c7b9ef](https://github.com/openssl/openssl/commit/3c7b9ef9c56a8066e0e6f4c61bc2ac2648bb1e42), [6366bdd](https://github.com/openssl/openssl/commit/6366bdd9be281984d675865ed5467bcf523640c5), [eddb067](https://github.com/openssl/openssl/commit/eddb067e2ce82bc2ea104b3ab5286fe334c0525d), [222cf41](https://github.com/openssl/openssl/commit/222cf410d5e7bdd58dd50a0a3f1f0805707808ef), [38b051a](https://github.com/openssl/openssl/commit/38b051a1fedc79ebf24a96de2e9a326ad3665baf), [cffafb5](https://github.com/openssl/openssl/commit/cffafb5f57da07d90b23d0bc215371078d1ecbef), [a566864](https://github.com/openssl/openssl/commit/a566864b607317fc95cbe190bbf0b8b928fcfa77), [19d0044](https://github.com/openssl/openssl/commit/19d00444488c0a5861911ac8ba6b71c5c1f6c19a), [9b7fb65](https://github.com/openssl/openssl/commit/9b7fb65e1520f398344ea8b7f3b4b097ae2617d7), [3105901](https://github.com/openssl/openssl/commit/310590139e45116d86627dcc85e83f2e3fcbb6b4), [b5cf81f](https://github.com/openssl/openssl/commit/b5cf81f7c9775d2502730ba126893ce8af4db90e), [f2892e2](https://github.com/openssl/openssl/commit/f2892e21619a2c59e957f7f9121f24713bcad3e9), [2f6e24e](https://github.com/openssl/openssl/commit/2f6e24eb5bd6a3ea4c5e18ff003acc4e812b527f), [4bf610b](https://github.com/openssl/openssl/commit/4bf610bdce3b0e474c5ce7db5be77e152f3649b6)
- Reconstruct the writing record layer logic into independent record layer objects and methods, and migrate the relevant code. (Architecture event: Record layer reconstruction)
  ↳ No PR: [2b71b04](https://github.com/openssl/openssl/commit/2b71b042202d11854801682d48ccf4e4e34cd5cf)
- Move the alarm sending check out of the record layer and move it to the upper layer write function for processing. (Architecture event: Record layer reconstruction)
  ↳ No PR: [3eaead7](https://github.com/openssl/openssl/commit/3eaead7166ef5aff027e571a9be0def6581ef20c)
- Migrate the write buffer management logic from the SSL connection layer to the write record layer, and reconstruct the related functions to use the record layer internal data structure. (Architecture event: Record layer reconstruction)
  ↳ No PR: [151f313](https://github.com/openssl/openssl/commit/151f313e53c1515f2730b3b36e3fc966e1a8010b)
- The calculation logic of the record version number is moved out of the record layer, and is instead calculated by the upper-layer state machine and passed to the record layer through the template, and a new auxiliary function is added to set the record protocol version. (Architecture event: Record layer reconstruction)
  ↳ No PR: [1d36767](https://github.com/openssl/openssl/commit/1d3676778c280ef05044c4c9e696a4f8096530ea)
- Move the need_empty_fragments flag into the record layer structure, and set the flag according to conditions when the record layer is initialized, removing the old location and setting logic. (Architecture event: Record layer reconstruction)
  ↳ No PR: [b9e4e78](https://github.com/openssl/openssl/commit/b9e4e78342df6575b358def3d951227e9c6cebda)
- Move the record filling callback completely into the record layer, pass it through the dispatch array, and avoid direct access to SSL_CONNECTION. (Architecture Event: Record Layer Reconstruction)
  ↳ No PR: [5f95eb7](https://github.com/openssl/openssl/commit/5f95eb77e780cc0b90a7da6cc4f79c7bb153ca64)
- Migrate the callback function and block size parameters related to TLS 1.3 record filling from the SSL_CONNECTION structure to the OSSL_RECORD_LAYER structure, and add corresponding parameter definitions. (Architecture event: Record layer reconstruction)
  ↳ No PR: [eb7d6c2](https://github.com/openssl/openssl/commit/eb7d6c2a9b3b9d1582e3e1b65c9d431cf3209207)
- Re-enabled multiple blocks of code and migrated them to the record layer, restructured buffer management and write-related functions. (Architecture event: Record layer reconstruction)
  ↳ No PR: [23bf52a](https://github.com/openssl/openssl/commit/23bf52a4b40deb033de0a257b724012afe32b169)
- Migrated the pipeline related code from the SSL layer to the record layer, added the tls_free method to support resource release of the record layer; migrated the number of write pipelines to the new record layer structure. (Architecture event: Record layer reconstruction)
  ↳ No PR: [c618679](https://github.com/openssl/openssl/commit/c6186792b98e93cf2d5d2a9fb85e4aeab31db890), [e7694c6](https://github.com/openssl/openssl/commit/e7694c69b5fed37f5cdf72b70f507c7188db7e3d)
- Refactor the writing code, move the multi-block writing function to a separate file, and adjust related functions to use the new record layer structure. (Architecture event: Record layer refactoring)
  ↳ No PR: [bafe524](https://github.com/openssl/openssl/commit/bafe524b5ce425105ac321f9fffa23e2d5b06845)
- Added QUIC receiving stream management function, introducing SFRAME_LIST structure and QUIC_RSTREAM object for managing received stream data. (Architecture event: QUIC protocol support)
  ↳ No PR: [bbf902c](https://github.com/openssl/openssl/commit/bbf902c34a90435bacea8a551ac39a559c8df6b2)
- Migrate record filling logic from tls_common.c to tls13_meth.c. Only TLS 1.3 methods need to handle record filling, other methods are ignored. (Architecture event: Record layer reconstruction)
  ↳ No PR: [2582de2](https://github.com/openssl/openssl/commit/2582de25902510cdb934c5ff59845fc26a7f2e28)
- Added a new encryption preparation step, extracted logic such as MAC calculation and encryption space reservation from the record writing function into an independent function, and registered this step in each protocol method. (Architecture event: Record layer reconstruction)
  ↳ No PR: [757ef3b](https://github.com/openssl/openssl/commit/757ef3bab02e976500ffd2b1ae2229ed62f85a61)
- Change the way of saving retransmission status in dtls1_buffer_message to use standard record layer functions, and change the parameters of dtls1_retransmit_message and dtls1_set_message_header from SSL* to SSL_CONNECTION*. (Architecture event: Record layer reconstruction)
  ↳ No PR: [b9e37f8](https://github.com/openssl/openssl/commit/b9e37f8f573de1951655f6d8684f2f65ffc6905b)
- The old buffer management code has been removed, and related functions have been migrated to the new record layer. (Architecture event: Record layer reconstruction)
  ↳ No PR: [e158ada](https://github.com/openssl/openssl/commit/e158ada6a74e5903354fdd5a6f56a32bbbba69fd)
- Create internal SSL objects for QUIC-TLS to represent TLS connections, and refactor the SSL initialization process to support passing in method parameters. (Architecture Event: QUIC-TLS Integration)
  ↳ No PR: [a7f4188](https://github.com/openssl/openssl/commit/a7f41885b368c7fb63e52aadaa0a5b5bd239b876)
- Separate QUIC related code from FIPS source files, and add QUIC packet processing functions. (Architecture event: QUIC supports reconstruction)
  ↳ No PR: [25624c9](https://github.com/openssl/openssl/commit/25624c9087d5422c3bb93cd987a066cb7c883a16)
- Reconstruct OSSL_LIB_CTX internal object management, change from dynamic CRYPTO_EX_DATA to hard-coded static members and initialize them in advance to reduce lock competition; add decoder_cache support. (Architecture-related: core module reconstruction)
  ↳ No PR: [927d056](https://github.com/openssl/openssl/commit/927d0566ded0dff9d6c5abc8a40bb84068446b76)
- Centralize ARM SHA3 CPU detection logic to armcap.c, add ARMV8_WORTH_USING_SHA3 flag and enable it for Apple M1/M2; unify SHA3 capability detection macro to ARMV8_HAVE_SHA3_AND_WORTH_USING. (Architecture-related: platform compatibility)
  ↳ No PR: [08e6eb2](https://github.com/openssl/openssl/commit/08e6eb216c9d65d502dc136a40e1c0adaefab759), [ba9472c](https://github.com/openssl/openssl/commit/ba9472c1c121b13e48f7c198d3fe9871a86e664c)
- Move the TLS1_FLAGS_QUIC macro definition from the public header file to the internal header file, making it private. (Architecture-related: public API)
  ↳ No PR: [d492e34](https://github.com/openssl/openssl/commit/d492e34351ae49e899a7c66f1882703a4fedced2)
- Reconstruct the legacy blake2 EVP structure, directly use base blake2 to implement it, avoid relying on the provider-specific init function, and change the corresponding init function in the provider to static. (Architecture-related: Separation of responsibilities between EVP and Provider)
  ↳ No PR: [df9ecd2](https://github.com/openssl/openssl/commit/df9ecd2ef3907ec0a7bf9c54d9273d5342329bf9)
- Removed the unused reset function and its related implementation in OSSL_RECORD_METHOD. (Architecture-related: public API)
  ↳ No PR: [e5103df](https://github.com/openssl/openssl/commit/e5103dfc1200c2f4a450f8b4ff234ad84342d4b6)
- Reconstruct the QUIC congestion control abstract interface and change the packet loss and confirmation notification logic to pass each data packet to the congestion control module separately. (Architecture-related: QUIC congestion control interface)
  ↳ No PR: [9069917](https://github.com/openssl/openssl/commit/90699176b07469e0b6b688ed88bc3f1deb5ccc26)
- Reconstruct the option processing mechanism of QUIC connections to separate connection-level and stream-level options, allowing streams to inherit and update options independently. (Architecture-related: QUIC option processing mechanism)
  ↳ No PR: [db2f98c](https://github.com/openssl/openssl/commit/db2f98c4ebb17a60307f70c330834beffb8f1253)
- Migrate OSSL_TIME related code to libcrypto, and adjust conditional compilation to support UEFI environment. (Architecture-related: platform compatibility)
  ↳ No PR: [02d0f87](https://github.com/openssl/openssl/commit/02d0f87a8ba143eaeaee3334a2f63543b10148a9)
- The signature verification module supports re-initialization and fixes the state cleanup problem. (Architecture-related: signature verification re-initialization)
  ↳ No PR: [ae6b68b](https://github.com/openssl/openssl/commit/ae6b68b761b9c5f30897747487ea943ccfab53ba)
- Added OSSL_STACK_OF_X509_free() function to simplify X509 stack release. (Architecture-related: public API)
  ↳ No PR: [79b2a2f](https://github.com/openssl/openssl/commit/79b2a2f2eedb9d6b24a3f6748332328cf54568fb)
- New copy functions for digest and password context. (Architecture-related: public API)
  ↳ No PR: [4e62f1a](https://github.com/openssl/openssl/commit/4e62f1a3af36512a1f5e1273d2dc54e3ce7f5fca)
- Added -no_ems option for s_client and s_server. (Architecture-related: public API)
  ↳ No PR: [a829d53](https://github.com/openssl/openssl/commit/a829d53a14eeae2b0bc783b7952b4212cf31d918)
- POSIX asynchronous context adds support for custom stack allocation and release functions. (Architecture-related: public API)
  ↳ No PR: [f6f56f4](https://github.com/openssl/openssl/commit/f6f56f4776727e18d4dd5490e3b507bae068013a)
- No longer add a write lock when releasing the last reference of EVP_PKEY. (Architecture-related: Concurrency behavior)
  ↳ No PR: [3642480](https://github.com/openssl/openssl/commit/36424806d699233b9a90a3a97fff3011828e2548)
- Undo the change of SSL_get_version returning QUICv1 for QUIC connections. (Architecture-related: public API)
  ↳ No PR: [0651e05](https://github.com/openssl/openssl/commit/0651e0547490af29b33ce9fd55eb20b2f1499c51)
- Make s_client -quic -debug work properly, and extend debugging callbacks to support QUIC's sendmmsg and recvmmsg operations. (Architecture-related: public API)
  ↳ No PR: [1a91fda](https://github.com/openssl/openssl/commit/1a91fda1839bc745e8359f82d19a5ef44ca36f7e)
- Fix EVP_PKEY_CTX_set0_rsa_oaep_label function to accept NULL label parameter for backward compatibility. (Architecture-related: public API)
  ↳ No PR: [21b98da](https://github.com/openssl/openssl/commit/21b98da9d80c561b6273b0c51c259196d6740e70)
- Add parameter alias checking in BN_nnmod and BN_mod_sub_quick to prevent errors. (Architecture-related: public API)
  ↳ No PR: [29c0d81](https://github.com/openssl/openssl/commit/29c0d8156629a988db5a4af30704736579f7c313)
- Added QUIC stream status query API, including SSL_get_stream_type, SSL_get_stream_id, SSL_is_connection, SSL_is_stream_local and SSL_stream_reset, used to obtain stream identifier, type and connection status. (Architecture event: QUIC protocol integration)
  ↳ No PR: [19cb088](https://github.com/openssl/openssl/commit/19cb0887722b66e5db7ec0d339526608444a11ef), [e1dee2e](https://github.com/openssl/openssl/commit/e1dee2e37971e068d6aff25dbfc92ef4db5adbd9), [1bca3f1](https://github.com/openssl/openssl/commit/1bca3f1b2d139c2306fd65d23583e4d16bdc11f9), [c3a04ea](https://github.com/openssl/openssl/commit/c3a04ea2fdd073e55b57e70e4f17f3ccbaa8c8a6), [ca5b030](https://github.com/openssl/openssl/commit/ca5b030306b8b4c98afca5dca216bc59c24e6aca)
- Add SHA-3 based PRF support to PBES2, integrate SHA-3 hashing into PBKDF2 as an alternative to HMAC. (Architecture event: Added SHA-3 PRF support)
  ↳ No PR: [c73ba81](https://github.com/openssl/openssl/commit/c73ba81899c291d60851321e6de8913d4800c456), [5702392](https://github.com/openssl/openssl/commit/5702392f73e679fd9ed9dd912cf4c9dc613c4d71)
- Added Brotli compression support (RFC7924), implemented the corresponding BIO and COMP methods, and displayed Brotli disabled status in the command line tool. (Architecture event: Compression module added Brotli compression support)
  ↳ No PR: [12e96a2](https://github.com/openssl/openssl/commit/12e96a23604a7aa1cd8f83486b02f1bcab6d468f)
- Added ZSTD compression support, including compression/decompression methods, BIO filters and related tests. (Architecture event: Compression module adds ZSTD compression support)
  ↳ No PR: [caf9317](https://github.com/openssl/openssl/commit/caf9317d7d75213990014e07048384be15688889)
- Enable KTLS receive function in TLS 1.3, and fix the sequence number and BIO usage of the receive path. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [7c78932](https://github.com/openssl/openssl/commit/7c78932b9a4330fb7c8db72b3fb37cbff1401f8b)
- Added SSL_get0_iana_groups() and SSL_client_hello_get_extension_order() functions, allowing users to obtain the groups and extension order in the TLS handshake without memory allocation, for low-cost calculation of SSL fingerprints (JA3). (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [13a53fb](https://github.com/openssl/openssl/commit/13a53fbf13bc6fa09c95ad4bdc6ec70fa15aa16d)
- Added QUIC protocol basic support: Added OSSL_QUIC method declaration, empty implementation and auxiliary functions, as well as variable length integer encoding/decoding and WPACKET subpackage operation interface. (Architecture event: QUIC protocol support)
  ↳ No PR: [770ea54](https://github.com/openssl/openssl/commit/770ea54b58769bae07e22a92e0c12ece9bdbc8e2), [99e1cc7](https://github.com/openssl/openssl/commit/99e1cc7bcae2e3707913881d7108c92b7a9bf7a1), [416d0a6](https://github.com/openssl/openssl/commit/416d0a638c1635a182e57fe80c7c065dd76818c0)
- Ensure various SSL options are passed to the record layer, and update relevant test functions. (Architecture Event: Record Layer Change)
  ↳ No PR: [79eebb0](https://github.com/openssl/openssl/commit/79eebb08434e31aede316d934b53e4096c131b8f)
- Implement event queue in SSL, supporting the creation, addition, removal and acquisition of events. (Architecture events: SSL protocol engine module changes)
  ↳ No PR: [e6be47e](https://github.com/openssl/openssl/commit/e6be47e427fb6650f274c418947e7665fbe08889)
- Implement KTLS support in the new read record layer code, and reconstruct the encryption status switching and key update functions. (Architecture event: SSL protocol engine module change)
  ↳ No PR: [cc110a0](https://github.com/openssl/openssl/commit/cc110a0aaebd627a9e61e2c8d68b02e3e0a4e76b), [ff3e450](https://github.com/openssl/openssl/commit/ff3e4508bde0d7f7ab211ca9f027bef820ba1d70)
- Supports passing data from one epoch to the next epoch, and adds record layer parameter parsing and cleanup logic when the connection is released. (Architecture event: SSL protocol engine module change)
  ↳ No PR: [359affd](https://github.com/openssl/openssl/commit/359affdead3af497f1673204c5c34061d28dfa7b)
- Reimplement brainpool curve support in TLSv1.3, simplify processing logic and create new TLS_GROUP_ENTRY value. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [16f0e91](https://github.com/openssl/openssl/commit/16f0e91cf82e13c327f0b0402459dfbf78ef787c), [c9ee6e3](https://github.com/openssl/openssl/commit/c9ee6e3646258f79a9970be96394cb2b93b7eddd)
- Renamed the internal function ossl_sleep to the public function OSSL_sleep and moved it to crypto/sleep.c to solve the problem that dependent functions cannot be found when linking shared libraries. (Architecture event: HPKE module added)
  ↳ No PR: [82d28c6](https://github.com/openssl/openssl/commit/82d28c6b3cbd8074faaa34cc2ce57dacc580792f)
- Introduce BIO preparation steps before writing, and add KTLS buffer allocation and release functions. (Architecture event: SSL protocol engine module reconstruction)
  ↳ No PR: [ace3819](https://github.com/openssl/openssl/commit/ace3819506d8d6bd298dd8448fefcbd62b63580c)
- Integrate QUIC_RSTREAM into the RX unpacker, replacing the previous placeholder implementation, so that the received data can be queued and flow controlled through the flow controller. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [a17c713](https://github.com/openssl/openssl/commit/a17c713a7ad394b08646bbb0f0ba1a16e1cc8799)
- Add pseudo packet loss support to QUIC ACKM, allowing specified packets to be forced to be marked as pseudo loss during connection retries and avoid triggering congestion control. (Architecture event: QUIC protocol engine changes)
  ↳ No PR: [e5d5756](https://github.com/openssl/openssl/commit/e5d575686efb280af08c3fd307a649ed2a942ce3)
- Added ossl_quic_demux_set_bio function for QUIC demuxer, allowing to change the BIO for reading data at runtime. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [964f0de](https://github.com/openssl/openssl/commit/964f0deb81f3025c11e451dc37f8e2f1c85548ed)
- Support the calculation and verification of QUIC Retry Integrity Tag, and add the unused field in the QUIC packet header structure to ensure serialization consistency. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [70d4589](https://github.com/openssl/openssl/commit/70d45893d0decc1ac2431a20db6750bc70cbaea5)
- Added new transmission parameters and related constants to the QUIC protocol, and added a connection ID comparison function; at the same time, reject integer transmission parameters with extra bytes at the end to enhance parsing robustness. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [56a1a0a](https://github.com/openssl/openssl/commit/56a1a0ad2438d8cacdedb9413cc5dd8823e7b805), [cecc05c](https://github.com/openssl/openssl/commit/cecc05c2935ef2c93753f126b71103bc6c0c2c7a)
- The QUIC record layer now allows rekeying of the INITIAL encryption layer on connection retries, other encryption layers still do not. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [b2c94b9](https://github.com/openssl/openssl/commit/b2c94b93994bc079ed3aa7f700adc7782bd0bb64)
- Implement front-end I/O API for QUIC, including connection and stream management, read and write operations, error handling and blocking mode support, and connect it to SSL API functions to enable QUIC connections to use SSL read and write, handshake and event timeout interfaces. (Architecture event: QUIC protocol engine integration)
  ↳ No PR: [22d53c8](https://github.com/openssl/openssl/commit/22d53c88838d5899383af6955ae62ca4094308c3), [03bacce](https://github.com/openssl/openssl/commit/03bacce81e3d3b3caba6d3c30edb548d0f5bc364)
- Added QUIC-TLS record layer implementation, including record reading and writing, status management, transmission parameter callback and other functions, and replaced the virtual handshake layer with the real QUIC TLS implementation, adding necessary TLS parameters and extended support. (Architecture event: QUIC-TLS record layer implementation)
  ↳ No PR: [19863d4](https://github.com/openssl/openssl/commit/19863d497dd1f74099998d4e5788d270de6423d6), [2723d70](https://github.com/openssl/openssl/commit/2723d705b55bd0c3f1806ff42b9eed379cfee4c0)
- Implement the complete functions of QUIC channel, including connection initialization, handshake management, key update, flow control, transmission parameter processing and state machine management; at the same time, complete the implementation of the receiving unpacker based on QUIC_CHANNEL, reconstruct the frame processing function and add protocol error checking and stream state management. (Architecture event: QUIC channel and unpacker implementation)
  ↳ No PR: [f538b42](https://github.com/openssl/openssl/commit/f538b42155283879d1a55708292105437a96700d), [3a37c92](https://github.com/openssl/openssl/commit/3a37c9235de465fe8d557b32f0178bfad0c09908)
- QUIC TXP no longer sends STREAM frames before the handshake is completed, adds an API to notify the handshake completion and updates related tests. (Architecture event: QUIC transmission behavior change)
  ↳ No PR: [cda88ba](https://github.com/openssl/openssl/commit/cda88bafe7532083a1e7c5bc08a9971735724c10)
- Allow MTU to change over time and automatically detect MTU, improve URXE status management and return handling. (Architecture event: QUIC MTU automatic detection)
  ↳ No PR: [d7668ff](https://github.com/openssl/openssl/commit/d7668ff21328c03f137d665b37f228e7c1f7a32a)
- Add an internal API for setting a custom TLS record layer, add a new parameter in the record layer method, allowing custom record layer methods to be specified through internal functions; extend the new_record_layer function to support passing the master key, length and KDF digest parameters, and update related calls. (Architecture event: TLS record layer interface extension)
  ↳ No PR: [bea8d70](https://github.com/openssl/openssl/commit/bea8d70498c9ad0e2cca3652c748d327be7b841e), [3f9175c](https://github.com/openssl/openssl/commit/3f9175c7a46b13a3528d9b5776030a78eb1f9454), [34a4068](https://github.com/openssl/openssl/commit/34a4068cc402c38e2134a6b46d9633ad3112bfa5)
- Added KTLS zero-copy sendfile support that is disabled by default on Linux, added the KTLSTxZerocopySendfile option to enable this feature, and updated related documentation and unit tests. (Architecture event: SSL protocol engine KTLS support)
  ↳ No PR: [cd715b7](https://github.com/openssl/openssl/commit/cd715b7e7fdd2aeb0fd80220d2df5187b291f87a)
- Add internal support for SSL objects, allowing custom extensions to be registered at the SSL level instead of just the SSL_CTX level. (Architecture Event: SSL Protocol Engine Custom Extension Support)
  ↳ No PR: [f6da3bb](https://github.com/openssl/openssl/commit/f6da3bbfb7342f3931d36e0c67bd9f79169fac2b)
- Added BIO polling descriptor API to support obtaining read and write polling descriptors, and updated SSL related functions to adapt to QUIC connections. (Architecture event: SSL protocol engine QUIC adaptation)
  ↳ No PR: [68801bc](https://github.com/openssl/openssl/commit/68801bcb766806a04e95e8ef714a0b836b1d7069), [7e1b0dc](https://github.com/openssl/openssl/commit/7e1b0dc1ef3cf0a7b02af0a09ab8aa5608134990)
- Add TLS server support for QUIC, including error handling improvements and ALPN negotiation callbacks. (Architecture event: SSL_Protocol_Engine module adds QUIC TLS server support)
  ↳ No PR: [4e3a55f](https://github.com/openssl/openssl/commit/4e3a55fd14cb4424fd62516345d918cdf0d9cdcc)
- Implement zero-copy reading for QUIC receive streams, add ossl_quic_rstream_get_record and ossl_quic_rstream_release_record APIs, and introduce a ring buffer as side storage for stream frame data. (Architecture event: SSL_Protocol_Engine module adds QUIC zero-copy reading API)
  ↳ No PR: [2113ea5](https://github.com/openssl/openssl/commit/2113ea584cdfd59892bbeb7acd78d8b1a825a156)
- Added the ability to query connection termination reasons for QUIC channels and test servers, introduced the QUIC_TERMINATE_CAUSE structure and expanded related APIs. (Architecture events: SSL_Protocol_Engine module added connection termination reason query)
  ↳ No PR: [149a8e6](https://github.com/openssl/openssl/commit/149a8e6c0a279b0dbbced72ffa6c5ed870a1bbc0)
- Added a callback function to set the TLS handshake message mutator, allowing the handshake message to be modified before it is written. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [d03fe5d](https://github.com/openssl/openssl/commit/d03fe5de8d1b78dd8190a9bce04bb228719b9947)
- Optimize QUIC's SSL_shutdown implementation, add SSL_shutdown_ex API, and support passing application error codes when shutting down locally. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [e804322](https://github.com/openssl/openssl/commit/e8043229ead9b44e2883a80ce256c219a1171cbb), [cbf965b](https://github.com/openssl/openssl/commit/cbf965b4f3ba8567624767239aebe4d04c62558a)
- Add support for detecting end of stream and sending end of stream signal to QUIC front-end I/O API. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [a997996](https://github.com/openssl/openssl/commit/a9979965bf2b74ca79e4bf3fa13539ab90728eeb)
- QUIC TXP adds the ability to generate probe packets, and adjusts the congestion control check logic to allow probe packets to be sent even when they cannot be sent. (Architecture event: SSL_Protocol_Engine module change (QUIC support)
  ↳ No PR: [fee8f48](https://github.com/openssl/openssl/commit/fee8f48e35f7009065227ae76c50672632ea5c40)
- Implement memory-based datagram BIO (BIO_s_dgram_mem), reuse BIO_s_dgram_pair code and add tests. (Architecture event: SSL_Protocol_Engine module change (QUIC support)
  ↳ No PR: [3a857b9](https://github.com/openssl/openssl/commit/3a857b9532169b1ffaa739ba29cd67a5d93cbe8a)
- Added the TLS1_FLAGS_QUIC flag bit, which is set when the QUIC connection is initialized, and provides the SSL_IS_QUIC_HANDSHAKE macro to detect whether the SSL connection is used for QUIC handshake. (Architecture event: SSL_Protocol_Engine module change (QUIC support)
  ↳ No PR: [43788fb](https://github.com/openssl/openssl/commit/43788fb3ac7221a699e56c38c1e9b8b4f8de4071)
- Implement SSL_rstate_string and SSL_rstate_string_long functions for QUIC connections, and adjust related functions to correctly support QUIC. (Architecture event: SSL_Protocol_Engine module change (QUIC support)
  ↳ No PR: [9ea0e72](https://github.com/openssl/openssl/commit/9ea0e7299223d10f61eee4db62ed0d4aec8f52e4), [79ee017](https://github.com/openssl/openssl/commit/79ee017220651d50d345af0e3093f091d5155890)
- Implemented the SSL_has_pending function in QUIC, and added an internal interface to check pending data. (Architecture event: SSL_Protocol_Engine module change (QUIC support)
  ↳ No PR: [9280d26](https://github.com/openssl/openssl/commit/9280d26a3a14e2aa79ad26cc25e4f41fbaa828ec)
- Add HelloRetryRequest support for QUIC connections, modify SSL_stateless function to correctly handle QUIC SSL. (Architecture events: QUIC support integration)
  ↳ No PR: [a1c56bb](https://github.com/openssl/openssl/commit/a1c56bbe79bcafb25880ce1deb7b75e2c6f5e0ce), [2f563dc](https://github.com/openssl/openssl/commit/2f563dc3efa7ece9197aaf44cf099bf516ac7421), [5ac7ee4](https://github.com/openssl/openssl/commit/5ac7ee4d5a38e4f163ed6a7c9c283d45038625a8)
- Add SSL_set_fd support for BIO_s_datagram for QUIC SSL, and extend test cases. (Architecture event: QUIC support integration)
  ↳ No PR: [5e6015a](https://github.com/openssl/openssl/commit/5e6015af4df7c4b3ef2e6c3c2f3657bafde88805)
- Add version setting restrictions to QUIC SSL connections, force the minimum protocol version to be TLS1.3, and add tests. (Architecture event: QUIC support integration)
  ↳ No PR: [0eecf84](https://github.com/openssl/openssl/commit/0eecf8418a7bdff1b19c319b4c5973ce8d53b92e)
- Added channel-only tick mode, which only processes the state synchronized by the channel mutex in thread-assisted mode. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [ccd3103](https://github.com/openssl/openssl/commit/ccd31037713ad1cdfd88c85a169bd18b08579813)
- Add thread-assisted front-end support for QUIC connections, including initialization, startup and cleanup functions. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f2f7c4f](https://github.com/openssl/openssl/commit/f2f7c4f15ab1d8dc36b668877253c0e497da8ca6)
- Support rstream's get/release recording mode at the QUIC TLS layer to avoid internal data copying when reading. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [7257188](https://github.com/openssl/openssl/commit/7257188b7054cf8acfc4837e38486459e0930718)
- Allow partial release of TLS records so that cleartext sanitization can be done at the record level and avoid forcing removal of const qualifications. (Architecture event: SSL_Protocol_Engine module changes)
  ↳ No PR: [7a4e109](https://github.com/openssl/openssl/commit/7a4e109ebe5af83bad6447889e43ac2612375070)
- Implement the NewReno congestion control algorithm for QUIC and switch its use in QUIC channels. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f68fd1c](https://github.com/openssl/openssl/commit/f68fd1cebcc8dfbd57e3c1c7afd2bf1a5b26cbe9), [f6f45c5](https://github.com/openssl/openssl/commit/f6f45c55ea0f597387005c429beba80d76484389), [ab11c16](https://github.com/openssl/openssl/commit/ab11c165f6d9ba1b98c85d4c9d1a906de0fcd13c)
- Add validation of preferred_addr transport parameter for QUIC conformance. (Architecture Event: QUIC Protocol Implementation)
  ↳ No PR: [54bd1f2](https://github.com/openssl/openssl/commit/54bd1f24d48c668c125f59e4c63bf9af3fb2f954)
- Allow applications to trigger QUIC key updates (TXKU) through SSL_key_update, and added corresponding internal interfaces and tests. (Architecture events: QUIC protocol implementation)
  ↳ No PR: [2525109](https://github.com/openssl/openssl/commit/2525109f90cf3a91a909621266ec6854a83805e2), [692a3ca](https://github.com/openssl/openssl/commit/692a3cab11932d2aaa7b1b628cacc513ba73a5e5)
- Support the SSL_OP_CLEANSE_PLAINTEXT option, set the plaintext clear flag when initializing the QUIC stream, and add a data erasure function for the send stream. (Architecture event: QUIC protocol implementation)
  ↳ No PR: [a02571a](https://github.com/openssl/openssl/commit/a02571a02473889d13fe7996e0d2d052328f3199), [6ba2edb](https://github.com/openssl/openssl/commit/6ba2edb7143472e306cbb4cbee9bae3094bc01ef)
- Implements RFC 9000 10.1 requirement to set the QUIC idle timeout period to at least three times the current probe timeout (PTO). (Architecture Event: QUIC Protocol Integration)
  ↳ No PR: [b056e9f](https://github.com/openssl/openssl/commit/b056e9fcf58502f6bff513768b38f82c42059e7c)
- Added a new public function for calculating the ciphertext payload length for QUIC QTX. (Architecture event: QUIC protocol integration)
  ↳ No PR: [41d3998](https://github.com/openssl/openssl/commit/41d39984e948322700a9b48ed6c6e8426bed3a9d)
- Added QUIC channel ping and stateless reset functions, adjusted the server shutdown interface to support application error codes. (Architecture event: QUIC protocol integration)
  ↳ No PR: [9ff3a99](https://github.com/openssl/openssl/commit/9ff3a99ea625c116833c950f51bff2554f6f7d1b)
- Implement rate limiting in the QUIC closed state, ensuring that the closed transmission size does not exceed three times the received size, enhancing protocol compliance. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [50e7684](https://github.com/openssl/openssl/commit/50e76846bf2d431d431b0b026f63d0b708d6e960)
- Added an internal interface to set the QUIC send buffer size, and an auxiliary function to obtain the connection and stream type. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [3415677](https://github.com/openssl/openssl/commit/3415677eec8e0b474973115ad871430f11ced3fd)
- Implemented the stream refresh function when the QUIC connection is closed, and added an interface to obtain the polling descriptor and network read and write status. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [8a2e9ab](https://github.com/openssl/openssl/commit/8a2e9abac8dbdab154461484a19261daf05926f7)
- Support most control commands for QUIC-based BIO_SSL, adjust the internal read-write BIO acquisition method and add QUIC compatibility check. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [a2ca189](https://github.com/openssl/openssl/commit/a2ca189e273584a7af3fcb90d893df9439e96659)
- Add unreliable transmission support to QUIC control frame queue (CFQ) so that PATH_RESPONSE and other frames will no longer be retransmitted when lost. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [371c295](https://github.com/openssl/openssl/commit/371c29582aa683ab10d58ec448aef1bded208076)
- Introduce addressed mode in QUIC, support disabling the peer address mode by setting NULL or AF_UNSPEC address, and adjust the processing logic at the connection layer. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [617b459](https://github.com/openssl/openssl/commit/617b459ddfabe5c2fbfc28808126999d936218fe), [62665fc](https://github.com/openssl/openssl/commit/62665fc2430cb3d3c9e59a133e67ab9941222017)
- Improve QUIC blocking configuration: automatically set network BIO to non-blocking mode, reconstruct blocking support detection logic, and add infinite timeout parameters. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [0818c17](https://github.com/openssl/openssl/commit/0818c17007bbda000e9c6329a1104d09cc614517), [51e671e](https://github.com/openssl/openssl/commit/51e671e204ede3a56c3e1c38d834240020800dfa)
- QUIC implements automatic reply to PATH_RESPONSE frame after receiving PATH_CHALLENGE frame. (Architecture event: QUIC protocol integration)
  ↳ No PR: [7eb330f](https://github.com/openssl/openssl/commit/7eb330ff7aa5580d7d97f2d183606c2d6bbbb449)
- Add a receiver flow control mechanism for the CRYPTO stream of the QUIC channel. (Architecture event: QUIC protocol integration)
  ↳ No PR: [098914d](https://github.com/openssl/openssl/commit/098914d0b768c090d443a46b66e4875969bee1e6), [ab6c634](https://github.com/openssl/openssl/commit/ab6c63456f30a849e3046532c582b4eaff7716d6)
- QUIC QRX Added functions to allow processing of 1-RTT packets after the handshake is completed and rejoining the delay queue. (Architecture event: QUIC protocol integration)
  ↳ No PR: [2a6f1f2](https://github.com/openssl/openssl/commit/2a6f1f2f6e321abe6deb2ce89084ece4aa50b3de), [869ab3e](https://github.com/openssl/openssl/commit/869ab3e70708c391ac49fe0fc4f671781c381e3d)
- In the QUIC TLS tick function, it no longer returns directly after the handshake is completed, but continues to call SSL_read() to process possible post-handshake messages. (Architecture event: QUIC protocol integration)
  ↳ No PR: [f85d343](https://github.com/openssl/openssl/commit/f85d343208bd944b88891feba200259b4cd0ba7c)
- Added support for QUIC servers to use pre-existing SSL_CTX contexts instead of always creating new ones. (Architecture Event: QUIC Protocol Integration)
  ↳ No PR: [829eec9](https://github.com/openssl/openssl/commit/829eec9f86f94ca81de920a1b61e9b636792d3c2)
- Added stateless reset processing support for QUIC channels. (Architecture events: QUIC protocol integration)
  ↳ No PR: [cdd9163](https://github.com/openssl/openssl/commit/cdd916313a89def99493e00b49958ced894ca209)
- In QUIC, if the NewSessionTicket message contains the early_data extension, its max_early_data value must be 0xffffffff, otherwise it will be regarded as a protocol violation; new verification logic. (Architecture event: QUIC protocol verification logic change)
  ↳ No PR: [04c7fb5](https://github.com/openssl/openssl/commit/04c7fb53e0437f83e2476e5d55a1af61959fadf5)
- Added minimal version negotiation packet processing logic for QUIC connections. (Architecture event: QUIC version negotiation processing)
  ↳ No PR: [777a8a7](https://github.com/openssl/openssl/commit/777a8a7f5d5b80919da906cdaf8825f502bcad4e)
- Optimize the TLS 1.3 handshake key switching timing, and switch the client write key as early as possible when early data is not used to support QUIC requirements. (Architecture event: TLS 1.3 key switching optimization)
  ↳ No PR: [84a1492](https://github.com/openssl/openssl/commit/84a149254f977f502dd2314169812fc6eae8c309)
- Implement a backpressure mechanism for flow creation for the QUIC application layer, add flow count flow control check, block or reject new flow creation when the peer flow limit is reached. (Architecture event: QUIC flow control backpressure mechanism)
  ↳ No PR: [9d6bd3d](https://github.com/openssl/openssl/commit/9d6bd3d30f8068a5558efa0bda2db570500ff364)
- QUIC APL supports waiting for shutdown initiated by the peer, and adds related flags and waiting mechanisms. (Architecture event: QUIC shutdown waiting mechanism)
  ↳ No PR: [25a0c4b](https://github.com/openssl/openssl/commit/25a0c4b907b0dbef4f0e70bf35cd84c85aaee3ad)
- Add the function of querying local initiation status for QUIC flow, and enhance the cleanup operation to support sending flow. (Architecture event: QUIC flow function enhancement)
  ↳ No PR: [d2e9e12](https://github.com/openssl/openssl/commit/d2e9e12b23fe331b71abe8c201f2610266090dde)
- Added SSL_inject_net_dgram, quic_get_stream_error_code, ossl_quic_get_stream_read_error_code and ossl_quic_set_write_buffer_size functions, and added frame_type field in the connection closing information. (Architecture event: QUIC new public API function)
  ↳ No PR: [56df4cf](https://github.com/openssl/openssl/commit/56df4cf24fad554e173d950a79a516e730096055)
- Implemented the SSL_want function for QUIC connections, supporting returning the desired I/O status. (Architecture event: SSL_Protocol_Engine module change (QUIC protocol support)
  ↳ No PR: [5debf07](https://github.com/openssl/openssl/commit/5debf070103131cff97a2fc78c93cae391099842)
- Added SSL_net_read_desired and SSL_net_write_desired functions for TLS/DTLS connections so that they can correctly return the expected read and write status in non-QUIC scenarios. (Architecture event: SSL_Protocol_Engine module change (QUIC protocol support)
  ↳ No PR: [3432157](https://github.com/openssl/openssl/commit/3432157ba1e0e29bab8bdd31d7ae728930e57c42)
- Added the function of setting PSK lookup session callback for QUIC server. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [1e4fc0b](https://github.com/openssl/openssl/commit/1e4fc0b2e57d08a90a6d8e30981fce2007d21109)
- SSL_get_rpoll_descriptor and SSL_get_wpoll_descriptor now also support TLS/DTLS connections, no longer limited to QUIC. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f262443](https://github.com/openssl/openssl/commit/f26244336f2a1b0d3040fe1db5d1024ec40e0b8b)
- Add support for SSL_get_shutdown() for QUIC connections, enabling it to return SSL_SENT_SHUTDOWN and SSL_RECEIVED_SHUTDOWN status. (Architecture event: SSL_Protocol_Engine module changes (QUIC support)
  ↳ No PR: [7757f5e](https://github.com/openssl/openssl/commit/7757f5ef731ad4e8d6c0f59ef752e4f726ba4f90)
- The QUIC record layer adds message callback support and adds a callback mechanism before data packets are written. (Architecture event: QUIC record layer callback mechanism)
  ↳ No PR: [1d57dba](https://github.com/openssl/openssl/commit/1d57dbac190ac6082de7865ed9205cd1f41bfd97), [14e3140](https://github.com/openssl/openssl/commit/14e314093943ffd89633746179c2c8f0b5c631a4)
- Enable brainpool curve support for TLS 1.3, and add related signature algorithms and group ID mappings. (Architecture-related: TLS 1.3 curve support)
  ↳ No PR: [0a10825](https://github.com/openssl/openssl/commit/0a10825a009c830125fef94c81d34e41300a24a5), [3f76339](https://github.com/openssl/openssl/commit/3f76339a3fe7be412b754ffe7b0a5438a1297f28)
- Add Chacha20-Poly1305 encryption algorithm support to FreeBSD's kernel TLS. (Architecture-related: Platform compatibility)
  ↳ No PR: [77f3936](https://github.com/openssl/openssl/commit/77f3936928068bee9d7e0c6939709ac179cb1059)
- Implement RFC7250 Raw Public Key (RPK) support, allowing TLS connections to be established using only private keys, and add related API, unit testing, documentation and command line tool support. (Architecture-related: Raw Public Key (RPK) support)
  ↳ No PR: [3c95ef2](https://github.com/openssl/openssl/commit/3c95ef22df55cb2d9dc64ce1f3be6e5a8ee63206)
- Added -digest option to openssl cms command to support using precomputed digest for signing; also added CMS_final_digest() API function. (Architecture-related: public API)
  ↳ No PR: [07342ba](https://github.com/openssl/openssl/commit/07342bad1bf850657e1a1f21188ee9a8a75e3a19)
- In CMP certificate path verification, when the certificate is found to be expired or not yet valid, it will no longer reject it directly, but first call the verification callback set by the user to decide whether to accept it. (Architecture-related: CMP certificate verification behavior)
  ↳ No PR: [080bd08](https://github.com/openssl/openssl/commit/080bd08fd32608b4f2edfa4b1e87e199b08a8835)
- Add a global read-write lock for object database operations to make OBJ series calls thread-safe. (Architecture-related: public API)
  ↳ No PR: [397065c](https://github.com/openssl/openssl/commit/397065c621e733fff80dedb28252120ec143693e)
- Added multiple registered OIDs for CMPv2 extension, including CMP module identification, information type and registration control identification. (Architecture-related: public API)
  ↳ No PR: [34959f7](https://github.com/openssl/openssl/commit/34959f7a2256eadd23d56f0efe855be7fde282b2)
- Enable BIO_gets() function for BIO_s_connect(), and refactor HTTP tests to support testing of text content. (Architecture-related: public API)
  ↳ No PR: [7a9b09f](https://github.com/openssl/openssl/commit/7a9b09feaa07f79522f7affccbca4236da2443e5)
- CMP mock server adds the -ref_cert option and the ossl_cmp_mock_srv_set1_refCert() function, which is used to verify the certificate information in the revocation request based on the reference certificate. (Architecture-related: public API)
  ↳ No PR: [b971d41](https://github.com/openssl/openssl/commit/b971d4198def0b29654e8fbf7987f7157741aed2)
- Allow specifying cipher strings using the standard name of the cipher suite, and add corresponding tests. (Architecture-related: external behavior)
  ↳ No PR: [d1b26dd](https://github.com/openssl/openssl/commit/d1b26ddbf6a9165c71884eff228300e3d83be1b1)
- Implement the optional hashAlg field for CMPv3's certConf message, set this field when using the fallback hashing algorithm and set the protocol version to 3. (Architecture-related: external behavior)
  ↳ No PR: [74107c4](https://github.com/openssl/openssl/commit/74107c4428edbe8d6797ac6a700e0ea2c9e14952)
- Added support for RFC8879 compressed certificate extension, including compressed sending and receiving of server and client certificates, and added related APIs and configuration options. (Architecture-related: public API)
  ↳ No PR: [b67cb09](https://github.com/openssl/openssl/commit/b67cb09f8ddf258cf326f3e7b20be095fb53457c)
- Add TCP Fast Open (TFO) support for socket BIO and s_client/s_server, support Linux, macOS and FreeBSD. It is disabled by default and can be enabled through the enabled-tfo option. (Architecture-related: platform compatibility)
  ↳ No PR: [a3e53d5](https://github.com/openssl/openssl/commit/a3e53d56831adb60d6875297b3339a4251f735d2)
- Added necessary OIDs defined in the ETSI specification for CAdES processing. (Architecture-related: public API)
  ↳ No PR: [5f7d4e9](https://github.com/openssl/openssl/commit/5f7d4e9111dcd2a91429ecab807c4f282164ea46)
- Added preemptive thread support, providing internal APIs for thread creation and synchronization primitives for POSIX and Windows platforms, and supporting compile-time disabling and runtime enabling. (Architecture-related: public API, platform compatibility)
  ↳ No PR: [4574a7f](https://github.com/openssl/openssl/commit/4574a7fd8dda070b129d76defca07703cab53842)
- Added codesign purpose support in X.509 certificate verification, and added the corresponding verification parameter code_sign. (Architecture-related: public API)
  ↳ No PR: [178696d](https://github.com/openssl/openssl/commit/178696d6020878361a088086243d56203e0beaa9)
- Added signed BIGNUM conversion functions, including BN_signed_bin2bn, BN_signed_bn2bin, etc., and restructured the internal implementation to uniformly handle signed and unsigned data. (Architecture-related: public API)
  ↳ No PR: [c2cab43](https://github.com/openssl/openssl/commit/c2cab43574dbb65094d6caf4dc1bf691e826a4fc), [4e26fe5](https://github.com/openssl/openssl/commit/4e26fe508bf18732983212ca4749eabb1f02e142), [f5e8050](https://github.com/openssl/openssl/commit/f5e8050fdcf2083825ef450d51bfacac21d2730e), [5288303](https://github.com/openssl/openssl/commit/5288303da96084b41b062d99eb37177fb4cf471e)
- Add support for signed BIGNUM in OSSL_PARAM and OSSL_PARAM_BLD APIs, and fix zero value boundary cases. (Architecture-related: public API)
  ↳ No PR: [f171985](https://github.com/openssl/openssl/commit/f1719858a05a9568ccbd052f160746cf4c027a9e), [17898ec](https://github.com/openssl/openssl/commit/17898ec6011cc583c5af69ca8f25f5d165ff3e6a), [748a296](https://github.com/openssl/openssl/commit/748a2967ffd52cf86696582fb1074d513493f469)
- Added support for id-it-caCerts to the CMP module, added related API functions and internal functions, and added the -srvcertout command line option. (Architecture-related: public API)
  ↳ No PR: [d477484](https://github.com/openssl/openssl/commit/d477484d33b7b3572150e21562cf4209c8dd9ef5), [b6fbef1](https://github.com/openssl/openssl/commit/b6fbef1159c9aeb1590c116a9426e169d2203506)
- Added assembly architecture support for RISC-V 64-bit platform, including cpuid runtime detection, bit operation extension Zb[abcs] and byte swap macros BSWAP4/BSWAP8, and repaired SHA macro conditional judgment. (Architecture-related: platform compatibility)
  ↳ No PR: [cb2764f](https://github.com/openssl/openssl/commit/cb2764f2a8165421dc5ab52159af99cbf766fa2c), [360f6dc](https://github.com/openssl/openssl/commit/360f6dcc5aa1a86ec3ff9a94612b88e3d960ee2e), [e4fd3fc](https://github.com/openssl/openssl/commit/e4fd3fc379d76d9cd33ea6699268485606447737)
- Added asn1_string_to_time_t function and added tests, and modified OBJ_find_sigid_by_algs to allow digest-free search for signature algorithms and added tests. (Architecture-related: public API)
  ↳ No PR: [065121f](https://github.com/openssl/openssl/commit/065121ff198a84106023013420dedd57ac4ff53a), [0654421](https://github.com/openssl/openssl/commit/065442165a3d339a7de469b4cd18a3f902c73443), [6097eb2](https://github.com/openssl/openssl/commit/6097eb215266a825c9eedfab8f9c8482567ad4ab)
- Enhance SSL thread safety and verification mechanism: add locks for platforms that do not support TSAN, change retry verification to SSL_set_retry_verify function, add StrictCertCheck configuration option. (Architecture-related: public API)
  ↳ No PR: [acce055](https://github.com/openssl/openssl/commit/acce055778ecbf72e06a254b3a9bf2a2907e5170), [dfb39f7](https://github.com/openssl/openssl/commit/dfb39f73132edf56daaad189e6791d1bdb57c4db), [336d92e](https://github.com/openssl/openssl/commit/336d92eb206946293a50db667fdc44ab7d69f8ad), [d8ed9e4](https://github.com/openssl/openssl/commit/d8ed9e4a9079b55a84bdbbc3172d36aa3be8bed7), [e6b8f35](https://github.com/openssl/openssl/commit/e6b8f359e79cdbe09033d02eaad7ecb4e24adb73), [5c41cee](https://github.com/openssl/openssl/commit/5c41cee225094e6298799b709278b0431643fb1f)
- Added functions to obtain the verification certificate storage and chain certificate storage of SSL and SSL_CTX. (Architecture-related: public API)
  ↳ No PR: [948cf52](https://github.com/openssl/openssl/commit/948cf521798a801cfde47a137343e6f958d71f04)
- Added more SRTP protection configuration files, including RFC 8723 dual AEAD configuration and ARIA series configuration. (Architecture-related: public API)
  ↳ No PR: [a425c0f](https://github.com/openssl/openssl/commit/a425c0fec6eb74c942ca5bca8e27ff0c9f126d48)
- Added public string case-insensitive comparison functions OPENSSL_strcasecmp and OPENSSL_strncasecmp. (architecture-related: public API)
  ↳ No PR: [4b2bd27](https://github.com/openssl/openssl/commit/4b2bd2722b8294a6b27c9e1fcf7d76f7d9de9b44), [fba140c](https://github.com/openssl/openssl/commit/fba140c73541c03e22b4fdb219a05d129bf0406d)
- Introduce CMP protocol version 3, while keeping version 2 as the default version. (Architecture-related: version and compatibility)
  ↳ No PR: [c4ad4e5](https://github.com/openssl/openssl/commit/c4ad4e5bf67dae6f7729de5438c9a96a2abd0f92)
- Added support for BIO_sendmmsg and BIO_recvmmsg to BIO_dgram. (Architecture-related: new functions of BIO layer)
  ↳ No PR: [664e096](https://github.com/openssl/openssl/commit/664e096cf94b1a2f72b3c562dd93db7e13b235f4)
- Export CMS_EnvelopedData type, add CMS_EnvelopedData_decrypt function. (Architecture-related: public API)
  ↳ No PR: [e2f6960](https://github.com/openssl/openssl/commit/e2f6960fc5fe1d6eb2178adf51db1ed206ff9e90), [98b183d](https://github.com/openssl/openssl/commit/98b183d3c65e56b0f21f4e77b2cd3d2aa62374f2)
- Added d2i_PUBKEY_ex_fp and d2i_PUBKEY_ex_bio functions to support passing in library context and attribute query when reading public keys from files or BIO. (Architecture-related: public API)
  ↳ No PR: [820723d](https://github.com/openssl/openssl/commit/820723dde0c9ec9a4fc68406a0e5aee1dc83f836)
- Added two new BIO types, BIO_s_dgram_pair and BIO_s_dgram_mem, providing ring buffer-based datagram pair and memory datagram functions. (Architecture-related: public API)
  ↳ No PR: [b88ce46](https://github.com/openssl/openssl/commit/b88ce46ee88c4128f72694e42160622844971d04)
- Added datagram mode support for BIO_s_mem, switched through new BIO control commands, and introduced the BIO_s_dgram_mem method. (Architecture-related: public API)
  ↳ No PR: [5a4ba72](https://github.com/openssl/openssl/commit/5a4ba72f00f9b336a4d65abff822699ceb9617c6), [3bfc58a](https://github.com/openssl/openssl/commit/3bfc58ad6f150e343c75565e2b162b80ec39a28d), [ce602bb](https://github.com/openssl/openssl/commit/ce602bb0a20589e5a84c48a55ce13219ab881e84)
- Added CMS_SignedData_verify function as an extended variant of CMS_verify. (Architecture-related: public API)
  ↳ No PR: [d7d3dae](https://github.com/openssl/openssl/commit/d7d3dae694fa4611c1cd953dccf81b3d2b4121c6)
- Added X509_PUBKEY_set0_public_key function, extracting and optimizing the public key setting logic from X509_PUBKEY_set0_param. (Architecture-related: public API)
  ↳ No PR: [9df7158](https://github.com/openssl/openssl/commit/9df71587f1897c3b282b3fe1b47c01656b58531e)
- Added partial string matching support for Content-Type values to OSSL_HTTP_REQ_CTX_nbio, allowing parameters after semicolons to be ignored. (Architecture-related: public API)
  ↳ No PR: [52f6169](https://github.com/openssl/openssl/commit/52f616990537b22b0ec81475207caef25fdc0886)
- Added OSSL_trace_string function and OSSL_TRACE_STRING_MAX constant, used to format the output trace string. (Architecture-related: public API)
  ↳ No PR: [0243e82](https://github.com/openssl/openssl/commit/0243e821473ef6dedc8d5f3d6ebefc1b06f2e46f)
- RISC-V rev8 instruction support has been extended to the zbkb extension, and early breakage constraints have been added for the two-instruction bswap. (Architecture-related: Platform Compatibility: RISC-V zbkb extension)
  ↳ No PR: [48b6776](https://github.com/openssl/openssl/commit/48b6776678d794406c625dcb5767102b73081962)
- Removed the unused 1-bit GCM implementation, and added the ossl_gcm_ghash_4bit function. (Architecture-related: public API: added ossl_gcm_ghash_4bit)
  ↳ No PR: [7b6e19f](https://github.com/openssl/openssl/commit/7b6e19fc4e6cc1a7000f71789ef50636dacdbb85)
- The -CAfile parameter now supports certificate files in DER format. When loading, PEM format will be tried first, and DER format will be automatically tried after failure. (Architecture-related: public API: -CAfile supports DER format)
  ↳ No PR: [57c0205](https://github.com/openssl/openssl/commit/57c0205b4df7d612a0333415dfc0a845c22e7458)
- Improved error handling in X509_STORE_CTX_init, and added X509_STORE_CTX_init_rpk function. (Architecture-related: public API)
  ↳ No PR: [4fdc16a](https://github.com/openssl/openssl/commit/4fdc16af05d5e1e79ffebbae2b427f3a388227e3)
- Added BIO_sendmmsg and BIO_recvmmsg series APIs, including method setting/getting, sending/receiving functions, error judgment and debugging callback support. (Architecture-related: public API)
  ↳ No PR: [e0c4e43](https://github.com/openssl/openssl/commit/e0c4e43e40390e44614d14817e34b47e1c17d630)
- Added CRMF API function OSSL_CRMF_CERTTEMPLATE_get0_publicKey(), used to obtain the public key in the certificate template. (Architecture-related: public API)
  ↳ No PR: [c0f6792](https://github.com/openssl/openssl/commit/c0f6792b81784be05c5e51156767a873bca1b374)
- Allows setting arbitrary bag attributes through callback functions when exporting PKCS12, adding PKCS12_create_ex2 and PKCS12_SAFEBAG_set0_attrs interfaces. (Architecture-related: public API)
  ↳ No PR: [e869c86](https://github.com/openssl/openssl/commit/e869c867c1c405de3b6538586f17b67937556a4b), [af63793](https://github.com/openssl/openssl/commit/af6379368f81025808689e843a5d86c6402a63a7)
- Allow accepting private key input when a public key is expected, and refactored the loading logic to support silent mode. (Architecture-related: public API)
  ↳ No PR: [0e89b39](https://github.com/openssl/openssl/commit/0e89b396197f75993c8d64c07b4af6aa2d97e2af)
- Added the for_comp flag to the certificate compression process to skip unnecessary error handling during the compression process. (Architecture-related: certificate compression behavior)
  ↳ No PR: [72620ac](https://github.com/openssl/openssl/commit/72620ac79133ca7a4553b70573fd100257e8269d)
- Introduced the OSSL_CRYPTO_ALLOC macro to provide the compiler with a hint for returning pointers without aliases. (Architecture-related: public API)
  ↳ No PR: [e103595](https://github.com/openssl/openssl/commit/e1035957eba1e6ebdefd0e18dcbad5cbfa7a969a)
- Added support for Password-Based Encryption (PBE) using hmacWithSM3. (Architecture-related: public API)
  ↳ No PR: [48963ff](https://github.com/openssl/openssl/commit/48963ff6d0d07648e09e63d2dca9fb6069241f42)
- Added id-ct-signedTAL content type OID for RPKI's Trust Anchor Key signed object, and added OID definition for ASPA object. (Architecture-related: public API)
  ↳ No PR: [fcae2ae](https://github.com/openssl/openssl/commit/fcae2ae4f675def607d338b7945b9af1dd9bb746), [b0c1214](https://github.com/openssl/openssl/commit/b0c1214e1e82bc4c98eadd11d368b4ba9ffa202c)
- Use the public type COMP_METHOD instead of the internal type SSL_COMP in the record layer, and add the ability to query the current compression method through the record layer. (Architecture-related: public API)
  ↳ No PR: [1e76110](https://github.com/openssl/openssl/commit/1e76110b7214a4fb39dc1397cbc4771538d06f39)
- CMP adds support for rootCaCert in genm messages and rootCaKeyUpdate in genp messages, involving client API, server simulation and command line tool implementation. (Architecture-related: public API)
  ↳ No PR: [01b0485](https://github.com/openssl/openssl/commit/01b048513153bdbee3efc82389d38d353352a7f1)
- Added two new API functions, OSSL_CMP_CTX_get0_libctx() and OSSL_CMP_CTX_get0_propq(). (Architecture-related: public API)
  ↳ No PR: [2da163c](https://github.com/openssl/openssl/commit/2da163cb73eabac7af093747ecee26ed76aa364a)
- Certificates generated by default now use the X.509 V3 version, unless the -x509v1 option is specified in the req command. (Architecture-related: external behavior)
  ↳ No PR: [342e365](https://github.com/openssl/openssl/commit/342e3652c791bdb06e08abcc169b4456c83ccd00)
- Added CPU feature detection support for LoongArch64 architecture, and defined cpuid related macros and variables. (Architecture-related: platform compatibility)
  ↳ No PR: [7f2d618](https://github.com/openssl/openssl/commit/7f2d6188c7b16ef7a4deeeedb56f42014156b9f8)
- Added protocol version compatibility check in key_share extension processing of TLS 1.3. (Architecture-related: protocol compatibility)
  ↳ No PR: [247b8e5](https://github.com/openssl/openssl/commit/247b8e52527ed4facd9ff07cdef0df819193c0c3)
- Added option to disable implicit deny for RSA decryption, allowing users to choose whether to use implicit deny padding mode via control parameters. (Architecture-related: public API)
  ↳ No PR: [5ab3ec1](https://github.com/openssl/openssl/commit/5ab3ec1bb1eaa795d775f5896818cfaa84d33a1a)
- Added a new API for the QUIC congestion control module, which is used to query the next time to release the sending budget. (Architecture-related: internal API)
  ↳ No PR: [97c5c52](https://github.com/openssl/openssl/commit/97c5c52d6c2c5d13db0cc59b3dbf4d75c40ec3ba)
- Add OID 1.2.156.10197.1.104.10 and its corresponding NID, short name and long name for SM4-XTS algorithm. (Architecture-related: public API)
  ↳ No PR: [de8f6a3](https://github.com/openssl/openssl/commit/de8f6a3e293a43f364cddefdf734b13486ec4cc9)
- Added zlib one-time compression/decompression function, provided COMP_zlib_oneshot method, and adjusted the compilation conditions of COMP_zlib. (Architecture-related: public API)
  ↳ No PR: [3840271](https://github.com/openssl/openssl/commit/3840271e984010132380892817c1e1173f4a1576)
- Add libctx support for X9.31 key generation function, and add coverage test. (Architecture-related: public API)
  ↳ No PR: [bcd94b6](https://github.com/openssl/openssl/commit/bcd94b6335e37304a170d89977a2382fae370a97)
- Add manual URXE injection support for QUIC QRX, refactor the internal receive callback into a public injection interface, and adjust related cleanup and initialization logic. (Architecture-related: public API)
  ↳ No PR: [4e392f6](https://github.com/openssl/openssl/commit/4e392f601db9a5a131d0db8fa3fa2e3808d2770a)
- EVP_PKEY_Q_keygen now supports SM2 key generation. (Architecture-related: public API)
  ↳ No PR: [3f32d29](https://github.com/openssl/openssl/commit/3f32d29ad464591ed968a1e430111e1525280f4c), [b807c2f](https://github.com/openssl/openssl/commit/b807c2fbab2128cf3746bb2ebd51cbe3bb6914a9)
- Reconstructed the HPKE context initialization to obtain the AEAD encryption algorithm in advance and save the algorithm information to avoid repeated acquisition; at the same time, the parameter verification of the exported function was enhanced. (Architecture-related: public API)
  ↳ No PR: [d9ed306](https://github.com/openssl/openssl/commit/d9ed3068df038811211b1f9c9f2f4ee2a6840aa3)
- Updated QUIC version string from QUIC to QUICv1. (Architecture-related: protocol version identifier)
  ↳ No PR: [6848e5e](https://github.com/openssl/openssl/commit/6848e5eeeeae8ae28bfe7dcaa8d24673923a6ee8)
- Allow OBJ_create to accept NULL OID parameters to create objects and NIDs. (Architecture-related: public API)
  ↳ No PR: [b79da97](https://github.com/openssl/openssl/commit/b79da97cf8751d7b196a87cc8bced0bb3334a0d3)
- Add additional libctx and propq support to PKCS12, add related APIs and fix memory release issues. (Architecture-related: public API)
  ↳ No PR: [fe2a734](https://github.com/openssl/openssl/commit/fe2a7341b50450dc6acd6f8a17d4420511a5aefe)
- Support processing signedAndEnveloped type content in PKCS7_decrypt. (Architecture-related: public API)
  ↳ No PR: [35da6af](https://github.com/openssl/openssl/commit/35da6af1f82e3d02338aabe28cab744a63728fd8)
- Add support for IgnoreUnexpectedEOF option in SSL configuration command. (Architecture-related: SSL behavior option)
  ↳ No PR: [51cf034](https://github.com/openssl/openssl/commit/51cf034433d528876f3c235c5150c5acfe88f24d)
- Support incoming password callback when store is opened for early authentication of PKCS11 module. (Architecture-related: public API)
  ↳ No PR: [96e6780](https://github.com/openssl/openssl/commit/96e678087de25c4bb19ef01492bd04002c3fe315)
- Added EC_GROUP_to_params function, used to convert elliptic curve group to OSSL_PARAM array. (Architecture-related: public API)
  ↳ No PR: [a8aad91](https://github.com/openssl/openssl/commit/a8aad913ecc632405096b2b61942b2c782cc74f4)
- Fix -reqin option, add OSSL_CMP_MSG_update_recipNonce function. (Architecture-related: public API)
  ↳ No PR: [4b0c27d](https://github.com/openssl/openssl/commit/4b0c27d44514abb4ad2bb1153db96f106910fc04)
- Allows overriding the time source of the QUIC channel, and adds a callback function pointer for debugging or testing. (Architecture-related: public API)
  ↳ No PR: [b212d55](https://github.com/openssl/openssl/commit/b212d554e70930d8ebe425e535b0c3621b961541)
- To support Windows XP, add the condition variable signal function ossl_crypto_condvar_signal, adjust the timeout waiting interface, and remove the timeout_expired parameter. (Architecture-related: platform compatibility)
  ↳ No PR: [1dd04a0](https://github.com/openssl/openssl/commit/1dd04a0fe2ffc4104db5198543ed0ec5895e9651)
- Added SSL_get_handshake_rtt function, used to obtain handshake round-trip time. (Architecture-related: public API)
  ↳ No PR: [cee0628](https://github.com/openssl/openssl/commit/cee0628e0d53be82bd644ce258c3d3e90e64eced)
- Enable POSIX thread support on VMS platform and remove unused memory barrier functions. (Architecture-related: Platform compatibility)
  ↳ No PR: [ac21c17](https://github.com/openssl/openssl/commit/ac21c1780a63a8d9a3a6217eb52fe0d188fa7655)
- Added SSL_R_CONN_USE_ONLY error code definition, and removed the old number. (Architecture-related: public API)
  ↳ No PR: [71e5551](https://github.com/openssl/openssl/commit/71e55512631332085f10fd3b02eb351383b230da)
- Added selected Microsoft OIDs, introduced ms-corp alias for OID 1.3.6.1.4.1.311, updated all related OID definitions. (Architecture-related: public API)
  ↳ No PR: [f3afe15](https://github.com/openssl/openssl/commit/f3afe15fb7d3a1ed4397252d7615e7d788be662a)
- Added SSL_get0_group_name() function, used to obtain the group name used for key exchange. (Architecture-related: public API)
  ↳ No PR: [6866824](https://github.com/openssl/openssl/commit/68668243b176cd2bc53a83c6768d4f39930ba8ed)
- Add missing PKI/PMI object identifiers, including related OID definitions and macros. (Architecture-related: public API)
  ↳ No PR: [bac2f6d](https://github.com/openssl/openssl/commit/bac2f6db06e1e606a3f26c8667aebe4d1a0dc583)
- Supports all X.509v3 extensions of NULL syntax, and adds corresponding parsing and printing functions. (Architecture-related: public API)
  ↳ No PR: [91bc783](https://github.com/openssl/openssl/commit/91bc783a93a2a695fe6a2f8da93cf5b5e086ba42)
- Added OSSL_trace_string public API function. (Architecture-related: public API)
  ↳ No PR: [bbaeadb](https://github.com/openssl/openssl/commit/bbaeadb068c3289c7df3b7bea0049f70a648ba00)
- Add datagram mode support to BIO_s_connect, and support configuring non-blocking mode in datagram mode. (Architecture-related: BIO_s_connect datagram mode)
  ↳ No PR: [533254e](https://github.com/openssl/openssl/commit/533254eeb31efa46a9011665712e47b56a2fe720), [7841dba](https://github.com/openssl/openssl/commit/7841dbabec50eb701022154d9639a01c2a875eaa)
- Enhanced BIO_s_datagram: supports non-blocking mode configuration, adds peer address detection API and capability negotiation control command. (Architecture-related: public API extension)
  ↳ No PR: [f3295bd](https://github.com/openssl/openssl/commit/f3295bd80c44f0e202026ec856c73d8c9bb04670), [000ef78](https://github.com/openssl/openssl/commit/000ef7818b24a61611825670299ab82b283e0501), [1bd35ed](https://github.com/openssl/openssl/commit/1bd35edc6603523953db24321df10d41c7a37923)
- Added two new setting functions, X509_STORE_CTX_set_get_crl and X509_STORE_CTX_set_current_reasons, to support custom CRL verification. (Architecture-related: public API)
  ↳ No PR: [4a469cb](https://github.com/openssl/openssl/commit/4a469cba27cf778f1d97ddeefd3a3a80cd623553)
- EVP_PKEY_can_sign() and EVP_PKEY_assign() now support the RSA-PSS key type, treating it the same as standard RSA. (Schema-related: public API)
  ↳ No PR: [e297298](https://github.com/openssl/openssl/commit/e2972982c64f3f1ac10b3ebe1086d99ec67631bd)
- In the polling descriptor structure, the type field is changed to unsigned integer, and a custom value member of the integer type is added to support third parties using integers instead of pointers. (Architecture-related: public API)
  ↳ No PR: [2619d10](https://github.com/openssl/openssl/commit/2619d10ace8ee8e56425771bac48aa12769421f2)
- Added new public function BIO_ADDR_copy(), used to copy BIO_ADDR objects. (Architecture-related: public API: BIO_ADDR_copy)
  ↳ No PR: [a18c9f8](https://github.com/openssl/openssl/commit/a18c9f80916134bd7122cc1ba204bb5cdca752a3), [d058ae6](https://github.com/openssl/openssl/commit/d058ae6e0397faaa60c18c6ae3aecaff64dca47b), [30224a2](https://github.com/openssl/openssl/commit/30224a248495ad604a06b8977fa3aa1cc75b9d0d)
- Added unbiased random integer generation functions ossl_rand_uniform_uint32 and ossl_rand_range_uint32. (Architecture-related: public API: New random number generation function)
  ↳ No PR: [3fe56ba](https://github.com/openssl/openssl/commit/3fe56baf936373daa39b944e3194a6f234fbe8bf)
- Added OSSL_CMP_CTX_reset_geninfo_ITAVs function, used to reset geninfo ITAVs in CMP context. (Architecture-related: public API)
  ↳ No PR: [a2ede03](https://github.com/openssl/openssl/commit/a2ede0396addd13f7fe9a629b450a14892152a83)
- Fixed an issue in the QUIC transport packetizer where CONNECTION_CLOSE frames were generated simultaneously on multiple encryption levels, and will now only be generated on the lowest non-dropping encryption level. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [7f9d124](https://github.com/openssl/openssl/commit/7f9d12495e3782fa384d9de3516478a490abc177)
- Disabled the use of non-QUIC cipher suites in QUIC connections, and added related test cases. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [09d56d2](https://github.com/openssl/openssl/commit/09d56d20a2db3170b97ec98dcde9862ee7e00e78)
- Disable the use of NPN (Next Protocol Negotiation) in QUIC context. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [68dbff4](https://github.com/openssl/openssl/commit/68dbff4c040e6f1b65f84b649185aa466c4fba24)
- Disabled post-handshake authentication during QUIC connection initialization. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [7163617](https://github.com/openssl/openssl/commit/7163617f3310a2d8579388866a156df62b78bd69)
- Disable setting the maximum fragment length in non-disabled mode on QUIC SSL connections. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [d0638fd](https://github.com/openssl/openssl/commit/d0638fd5f0296ea84ff6fc314e9bfea8b5f06392)
- Disable the early data function of QUIC SSL and add related test cases. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [82a2bec](https://github.com/openssl/openssl/commit/82a2becab332c35b53c31d3f8a743fba66bef869)
- Disabled the execution of pipeline-related operations such as setting the maximum send fragmentation, splitting the send fragmentation and the maximum number of pipelines on QUIC SSL connections, and added corresponding tests. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [38c0ff1](https://github.com/openssl/openssl/commit/38c0ff1f404a25bc6711a2055efd92a20820ec38)
- Restrict the use of SSL_CTX_set_ssl_version and SSL_set_ssl_method in QUIC context. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [3ea30e7](https://github.com/openssl/openssl/commit/3ea30e76d788a4f1982785c0f29853cf1211d37e)
- Updated QUIC's SSL_set_quiet_shutdown and SSL_get_quiet_shutdown implementations to clarify that QUIC is not currently supported, and adjusted the internal structure to use SSL_CONNECTION. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f66f0d3](https://github.com/openssl/openssl/commit/f66f0d3ce1667c04d08f158565320237a59593f6)
- Prevent the SSL_clear operation in QUIC SSL implementation, make it return failure, and add corresponding tests. (Architecture event: SSL_Protocol_Engine module change (QUIC SSL implementation)
  ↳ No PR: [5f69db3](https://github.com/openssl/openssl/commit/5f69db396c61165b25c38a7506d608200561f228)
- Fixed a possible segfault when calling SSL_shutdown on a QUIC connection. (Architecture event: SSL_Protocol_Engine module change (QUIC protocol integration)
  ↳ No PR: [4e15b44](https://github.com/openssl/openssl/commit/4e15b44864df0d3c6306a9bf354fea92147834df)
- Update QUIC scheduling method, use SSL object pointer instead of QUIC_CONNECTION pointer, and fix an error code. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [6d495cc](https://github.com/openssl/openssl/commit/6d495cc4de9efac980df0a70be5981fd94831d33)
- Delay creation of default XSO to support QUIC application protocol sent first by client or server. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [21c8069](https://github.com/openssl/openssl/commit/21c80696e51c2b183dad3b19aeb50fe26920f0aa)
- Fixed multiple issues in QUIC protocol implementation, including role identification, stream state management, flow control, locking, callback mechanism, STOP_SENDING processing, FIN detection, stream release behavior, one-way stream detection, list usage errors and time callback parameter passing, etc. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [dfb9ae1](https://github.com/openssl/openssl/commit/dfb9ae14a44251553d4f4046ff1eb41608b3cca4), [e8fe7a2](https://github.com/openssl/openssl/commit/e8fe7a21ea253408930d570ce00e6d3a78652162), [13ac037](https://github.com/openssl/openssl/commit/13ac037d0148b6e461ca635bb1c627a4b759318a), [5d27e7e](https://github.com/openssl/openssl/commit/5d27e7e9ae7135f8ba92498e3c4e7f9b77f2f8e3), [b89c81e](https://github.com/openssl/openssl/commit/b89c81e43b88c48d7cb5ce48665bab6c36ae02ac), [2289401](https://github.com/openssl/openssl/commit/228940168529ba7c10b86934849b19818f79f74e), [8b52789](https://github.com/openssl/openssl/commit/8b5278942be94b5764b93c0633ea4162685264ac), [9aaafc2](https://github.com/openssl/openssl/commit/9aaafc26e0f301fe07d7141dc4a575ef9a4eb4d9), [acc6fde](https://github.com/openssl/openssl/commit/acc6fde0d44d22c7fa4578c967aee69c3fbcf350), [93651dc](https://github.com/openssl/openssl/commit/93651dc245353ceda661b55332f0b163c4a3e8e9), [66ec534](https://github.com/openssl/openssl/commit/66ec534861cc278bfb074a8fa3fa1fe3385723f8)
- Fix multiple issues in QUIC multi-stream support: correct SSL_get_stream_type function logic, handle multi-stream count references, manage send stream buffer space, optimize receive buffer check and fix variable uninitialization problem. (Architecture event: QUIC protocol implementation)
  ↳ No PR: [22b1a96](https://github.com/openssl/openssl/commit/22b1a96ff798cf73f4b573bff1d9f80236d3f102), [59c5c01](https://github.com/openssl/openssl/commit/59c5c016e53256e949225a2dd751b3450129cd72), [9cab4bd](https://github.com/openssl/openssl/commit/9cab4bd52396275338a027c02b3a52fbcede6aa5), [433d107](https://github.com/openssl/openssl/commit/433d107a9b2b0250d6806ed6fdc147117637fed5)
- Fixed multiple issues in QUIC protocol implementation, including confirmation handling, flow control, flow mapping, BIO acquisition and thread safety. (Architecture Event: QUIC Protocol Implementation)
  ↳ No PR: [bb7f370](https://github.com/openssl/openssl/commit/bb7f3701cecb49ca0faacb5e46d11fd07cf2ee02), [3dde343](https://github.com/openssl/openssl/commit/3dde3435abab4524e62af31d87bd795543822e54), [e8142d2](https://github.com/openssl/openssl/commit/e8142d2ce8383329e6a71639d154191c1515ba55), [0f06e7f](https://github.com/openssl/openssl/commit/0f06e7f5a6a7451a6cbf4eb0d86ebc9bbd95c55b), [45b7c7e](https://github.com/openssl/openssl/commit/45b7c7e06e8d28ad9a7ea0f7662ec04f283f7c36)
- Fix issues related to QUIC key update: prevent the old key from processing new data packets, correctly execute the key update process, and strictly implement the verification of ACK packet sequence number and key epoch. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [54fb007](https://github.com/openssl/openssl/commit/54fb0072c6f14a35808f3bb837517f053aff3847), [8a65e7a](https://github.com/openssl/openssl/commit/8a65e7a529020b50716f08acc82816b95765914b), [c93f766](https://github.com/openssl/openssl/commit/c93f766860cd4e13aea7253c2d807f6048aa635e)
- Adjust QUIC connection ID processing logic to comply with RFC 9000 specifications, strictly limit the number of active connection IDs, and close the connection when the peer limit is exceeded. (Architecture event: QUIC connection ID processing)
  ↳ No PR: [985429f](https://github.com/openssl/openssl/commit/985429f4f4423de71cae270330586da990e6797f)
- Fixed QUIC network error handling, returning SSL_ERROR_SYSCALL when encountering a network error. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [5c3474e](https://github.com/openssl/openssl/commit/5c3474ea563ed95bb7c86c08867139613655276b)
- Implement error state saving and recovery for the QUIC channel, save the thread error state when encountering a permanent error, and restore it to the user after the protocol is closed. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [9c3ea4e](https://github.com/openssl/openssl/commit/9c3ea4e1d7580fc061dfb754b620adb3439e683f)
- Follow RFC 9000 section 3.3, correct the consistency of stream status and allowed frame types: ensure that STREAM frames are no longer sent in the Reset Sent state, and correct the final_size calculation of RESET_STREAM frames. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [01715f2](https://github.com/openssl/openssl/commit/01715f2b41cac2e02663056d99901457db9b3eab)
- Repair QUIC protocol consistency: add packet type auxiliary function, improve transmission parameter parsing, and add packet verification and empty packet payload detection required by RFC 9000. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [0911cb4](https://github.com/openssl/openssl/commit/0911cb4a072f55b5f982635faeaa7a992a14181f)
- Release QUIC stream send and receive buffers that are no longer needed, and correctly calculate the final size of RESET_STREAM frames. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [28d0e35](https://github.com/openssl/openssl/commit/28d0e35cd675c67355d91caf65aa180df49f9db4)
- The QUIC flow state machine model now correctly handles the final size, and optimized the processing logic of STOP_SENDING frames. (Architectural event: QUIC protocol implementation change)
  ↳ No PR: [418e122](https://github.com/openssl/openssl/commit/418e122cd43c29c795de1e1af666d3ad5e4e99e9)
- Force QUIC frame type encoding to use a minimum number of bytes, and add related detection and testing. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [6c1d0e2](https://github.com/openssl/openssl/commit/6c1d0e28650164d782909abfea92ba834d0babd5)
- Forced checking of reserved bits in QUIC encrypted packet headers, if non-zero, it is considered a protocol violation and triggers a connection error. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [08cb9a8](https://github.com/openssl/openssl/commit/08cb9a83277e5cd847742c048345fb6c9daf8170)
- According to the requirements of RFC 9000 section 17.2.5.1, add verification of Retry packets in the QUIC channel: if its SCID is the same as the DCID of the initial packet, the Retry packet is discarded. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [212616e](https://github.com/openssl/openssl/commit/212616ed098bcf1190b6f687b234393b33168ba9)
- Per RFC 9000 section 13.3, restrict MAX_STREAM_DATA frames to be generated only when the receive stream is in RECV state. (Architectural event: QUIC protocol implementation change)
  ↳ No PR: [22f21fb](https://github.com/openssl/openssl/commit/22f21fbdd6ed7032f28d4f22ef1abc98e1c5d325)
- According to RFC 9000 section 19.8, there is an enforced limit on the maximum stream size, and stream frames exceeding 2^62 - 1 will trigger a protocol error. (Architectural event: QUIC protocol implementation change)
  ↳ No PR: [283938f](https://github.com/openssl/openssl/commit/283938fca59a7930a28e748e8ab7c2d15281c681)
- Fix the handling of the final size of the RESET_STREAM frame in the QUIC protocol to make it comply with the RFC 9000 specification. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [7e3fa44](https://github.com/openssl/openssl/commit/7e3fa44f2445b5cbf6a6bf5ebf3cf96a40775951)
- Per RFC 9000 section 12.5, CFQ is prohibited from sending disallowed frame types in a specific PN space. (Architectural event: QUIC protocol implementation change)
  ↳ No PR: [8d2e353](https://github.com/openssl/openssl/commit/8d2e353df48c141305327c43226aeb0d9a7e5aa8)
- Follow RFC 9000 Section 12.5, mask the application layer CONNECTION_CLOSE frame to ensure that it is converted into a transport layer CONNECTION_CLOSE frame when sent at a non-1-RTT encryption level to avoid leaking application data. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [96fa10f](https://github.com/openssl/openssl/commit/96fa10f36fce9016491f587e4c3032ff90adcdf7)
- Fixed the problem in the QUIC protocol that when processing NEW_TOKEN frames with empty Tokens, errors were not reported as required by RFC 9000. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [b5b40c4](https://github.com/openssl/openssl/commit/b5b40c4e183bf9a00ed086b72aa16369172a0054)
- Fix handling of STREAM_DATA_BLOCKED frames to comply with RFC 9000 specification: ignore frames for deleted streams, and return protocol errors for send-only streams. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f084a8f](https://github.com/openssl/openssl/commit/f084a8f7615c64cb55cb9de5669025eaa50eef6a)
- According to RFC 9000 section 19.14, add verification of the maximum stream ID encoding value when parsing STREAMS_BLOCKED frames, and trigger a connection error when the limit is exceeded. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f80e61b](https://github.com/openssl/openssl/commit/f80e61b61f660e721d5cc7325a1a2bacbc7f34a6)
- Implement RFC 9000 specification for QUIC clients and reject Initial packets sent by the server containing non-zero token length. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [fd0d593](https://github.com/openssl/openssl/commit/fd0d593220dd259ab9d327782eae28a07a537712)
- Fix the retirement processing logic of FIN and reset status in QUIC streams to ensure that the stream mapping is correctly notified when the read is completed or a reset is received. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [08d4b7e](https://github.com/openssl/openssl/commit/08d4b7eb7dac5d1c4d270f60d421a20e5df3c39a)
- QUIC no longer processes received data packets after the connection is terminated. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [8a6a00e](https://github.com/openssl/openssl/commit/8a6a00e3b8108c51e0facf30d2942176e72ad079)
- Added send stream state verification in QUIC APL to ensure that write operations are only performed in valid stream states, and fixed related error handling. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [abfe3d5](https://github.com/openssl/openssl/commit/abfe3d5128b4c04f4bf288d03833481dbe52ee4c)
- According to the RFC 9000 specification, when a client receives a zero-length connection ID, it treats the RETIRE_CONNECTION_ID frame as a protocol violation and triggers error handling. (Architectural event: QUIC protocol implementation change)
  ↳ No PR: [f37befa](https://github.com/openssl/openssl/commit/f37befa0480ec5d8362a5894e610a676987215b7)
- Fixed the problem that SSL_connect() failed to block correctly in blocking mode for QUIC connections. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [fb4a2bb](https://github.com/openssl/openssl/commit/fb4a2bba7115d1d1d5ac0ab8829e9659199ef77d)
- Set the ping deadline to infinite when initializing the QUIC channel to prevent timeout immediately before the connection is accepted. (Architectural event: QUIC protocol implementation change)
  ↳ No PR: [2719568](https://github.com/openssl/openssl/commit/27195689a8e123be356209d90000f49def13a0b9)
- Fixed QUIC handling in SSL status string functions, added helper functions for selecting BIO methods based on connection type, and cleaned up code related to multi-block transfers and version checking. (Architecture event: SSL_Protocol_Engine module changes)
  ↳ No PR: [d6e7ebb](https://github.com/openssl/openssl/commit/d6e7ebba3370e06ea4dfae6381dfe0e1c21070e3)
- Fix early data attribute inheritance problem in QUIC context, disable block filling, normalize header file protection macro. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [6e5550a](https://github.com/openssl/openssl/commit/6e5550a1045bb03afb40dac29f82cbc7158dbfc3)
- Corrected QUIC acknowledgment delay behavior according to RFC 9000, including correctly initializing the maximum acknowledgment delay and setting it to 0 in the Initial/Handshake package space. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [76908b4](https://github.com/openssl/openssl/commit/76908b45823f958f29b6bdf11efab6eac47f61ca), [f13868d](https://github.com/openssl/openssl/commit/f13868def28ee532631a1dec0322a3ff51b3d7c8)
- Improve the processing logic of QUIC connection closing and draining status according to RFC 9000, including adjusting ACK deadline calculation, adding connection closing reason copy function and optimizing polling descriptor update. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [afe4a79](https://github.com/openssl/openssl/commit/afe4a7978d2cff7852b46e8f23218ec6c41b8bf0)
- Uniformly use SSL_R_QUIC_PROTOCOL_ERROR error cause and record detailed error information. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [2b8126d](https://github.com/openssl/openssl/commit/2b8126d8a8ded94ce010234a37d059f8d3b71b1b)
- Fix the error return value when the QUIC connection is closed, automatically drain the stream that does not end normally, and optimize the congestion control wake-up time. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [63fac76](https://github.com/openssl/openssl/commit/63fac76c2485c7c675fcbd5bc719c969c76ecc01)
- Fixed the error code sent by the QUIC channel when the transmission parameters are not received, and changed it to the correct encryption extension missing alarm. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [3ad5711](https://github.com/openssl/openssl/commit/3ad5711e484736c7383b43d03f83e5700e589dfa)
- Fixed the problem in the QUIC channel that the client did not correctly discard the Initial encryption level after sending the Handshake packet for the first time. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [3eb0f9a](https://github.com/openssl/openssl/commit/3eb0f9a7027c635b7c162f936ecb76d95146c62e)
- Correctly convert TLS handshake errors into QUIC protocol errors, add error codes and error reporting interfaces, and trigger protocol error processing at the channel layer. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [80bcc4f](https://github.com/openssl/openssl/commit/80bcc4f1aeb67f0a05dbff04372e0b9563d4a779)
- Enforce PN monotonicity after key update at the QUIC receiving end, discarding packets that use the old key and PN is greater than or equal to the starting PN of the new key. (Architectural event: QUIC protocol implementation change)
  ↳ No PR: [0c1cc36](https://github.com/openssl/openssl/commit/0c1cc36bbb3b29a43cf08572b1176e5ee8e37ce2)
- Fixed the missing unlock call issue detected by Coverity in QUIC APL, and introduced lock management reconstruction. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [4669a3d](https://github.com/openssl/openssl/commit/4669a3d79b59d037ccb5b4a30bc522ebe55d3eec)
- Ensure that the underlying TLS SSL object is marked as closed when the QUIC connection is closed so that the session is available for recovery. (Schema event: SSL_Protocol_Engine module change)
  ↳ No PR: [f219abe](https://github.com/openssl/openssl/commit/f219abef51fd47fa5945d23bbdc379778e512dc5)
- Improve the error reporting mechanism of the QUIC channel, add error status recovery and more detailed error information, and optimize error handling during the TLS handshake. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [741170b](https://github.com/openssl/openssl/commit/741170bef340b31a32a94a4ea86cc0d7744c01b2)
- Fixed error handling when the server sends post-handshake CertificateRequest in the QUIC protocol, treating it as a protocol violation instead of an unexpected message. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [b644a93](https://github.com/openssl/openssl/commit/b644a9323f0060e27b3e45101856dc9e3bec0ac4)
- In QUIC connections, receiving TLS KeyUpdate messages is treated as an unexpected message and triggers a connection error. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [50a0af2](https://github.com/openssl/openssl/commit/50a0af2e41ea61a79c19c17f9e87541e283ba8bf)
- Fixed an issue with missing QUIC flags when clearing SSL connection data, ensuring QUIC status is retained after cleanup operations. (Architecture Event: QUIC Protocol Integration)
  ↳ No PR: [0f2add9](https://github.com/openssl/openssl/commit/0f2add9e8d4c1dc09848ea12aaad2eb4c5358bf2)
- Fixed the address mode judgment logic in QUIC connection, processing read and write capabilities separately. (Architecture event: QUIC protocol integration)
  ↳ No PR: [3760747](https://github.com/openssl/openssl/commit/3760747ff452fcb3e29190e670073253c5b47d49)
- Fixed the processing logic of control commands in QUIC mode, added internal functions to correctly route QUIC and non-QUIC ctrl calls, and adjusted the QUIC compatibility of control commands such as version checking and fragmented sending. (Architecture event: QUIC control command processing reconstruction)
  ↳ No PR: [c5b882a](https://github.com/openssl/openssl/commit/c5b882a80b9f5811e45e29f4492bf335e870eb35)
- Fixed multiple issues in QUIC protocol implementation: Added QUIC cipher suite lookup function, handled repeated transmission parameters, correctly passed TLS errors. (Architecture event: QUIC protocol implementation change)
  ↳ No PR: [547ea58](https://github.com/openssl/openssl/commit/547ea58821644bdc9089b2dcb163286d789f732a), [70e809b](https://github.com/openssl/openssl/commit/70e809b08a3fe70fed7f7ecdad88e5bb9fc3af1c), [982dae8](https://github.com/openssl/openssl/commit/982dae89d8d19fcb9cc2c3b8ba74afef352ecc41)
- Fixed the problem of not using BIO_free_all when releasing the BIO chain in QUIC connection to ensure consistent behavior with TLS. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [18fd0ea](https://github.com/openssl/openssl/commit/18fd0ea04d6bd37809a4e9a669c49cf9bc146bfb)
- Fixed the encoding and decoding problem of SM2 public key in d2i_PublicKey and i2d_PublicKey functions. (Architecture event: HPKE module change)
  ↳ No PR: [8582dcc](https://github.com/openssl/openssl/commit/8582dccc4dd1f1667b0e91a098e2cc78c7146dd7)
- If the peer transmission parameters are not received after the TLS handshake is completed, a protocol error will now be triggered and the connection will be terminated. (Architecture event: QUIC protocol error handling change)
  ↳ No PR: [62d0da1](https://github.com/openssl/openssl/commit/62d0da12e397811e26be5b5be8a1cfe54de5031e)
- Improved the error distinction of X509 storage lookup, now the function returns -1 to indicate internal error, 0 to indicate not found, and added lock check and sorting optimization. (Architecture-related: public API)
  ↳ No PR: [0ce8271](https://github.com/openssl/openssl/commit/0ce8271c20c95d21d9641c0ead76a86f818c45e9)
- The memory allocation function now reports the ERR_R_MALLOC_FAILURE error when it fails, and exposes the OSSL_ERR_STATE_free function. (Architecture-related: public API)
  ↳ No PR: [5639ee7](https://github.com/openssl/openssl/commit/5639ee79bdc905c1b7ed308fcd29e515e4f01a50)
- Add a global lock to the OBJ_add_sigid function to ensure thread safety when adding signature algorithms concurrently. (Architecture-related: public API)
  ↳ No PR: [c568900](https://github.com/openssl/openssl/commit/c568900c9ac02e92c54bd3168773d54d7350a580)
- New NID allocation uses atomic operations when TSAN is supported, otherwise uses locks; refactors lock management and allows creation of OID-less ASN1_OBJECT. (Architecture-related: public API)
  ↳ No PR: [29c80c6](https://github.com/openssl/openssl/commit/29c80c6004de8bfd1792e421bbe03ab5f075f21d)
- Enable checking of the return value of the EVP operation in the encryption performance test, and fix the conditional judgment in the error handling logic. (Architecture-related: public API)
  ↳ No PR: [98283a6](https://github.com/openssl/openssl/commit/98283a61f5b792dde0f0e1d9a616ec6e232b57b6)
- Correct the error checking logic of PBM calculation in CRMF, adjust the const qualifier of the template getter function, and add relevant comments. (Architecture-related: public API)
  ↳ No PR: [084d3af](https://github.com/openssl/openssl/commit/084d3afd26cc20b41241b70b6c709b76d2a334a5)
- Public and private DRBG no longer use derived functions, clean up parameter passing, and avoid passing unknown parameters. (Architecture-related: public API)
  ↳ No PR: [505d44c](https://github.com/openssl/openssl/commit/505d44c623c2a883cf015f26a499842cea0161f0)
- Fix the handling of memory allocation failure in X509_ALGOR_set0(), add return value checking to ensure error propagation, simplify the code and update the documentation. (Architecture-related: public API)
  ↳ No PR: [04bc3c1](https://github.com/openssl/openssl/commit/04bc3c1277b8b20dc29f96933f7be592c0535aa8)
- Improve the v2i_AUTHORITY_KEYID function's parsing error report of configuration values/options, and add unknown options, error values and other error reasons. (Architecture-related: public API)
  ↳ No PR: [6e98b7f](https://github.com/openssl/openssl/commit/6e98b7f153fcf9dfad1053fbb3a592166837c6fc)
- Prefer issuer certificates in DANE TLSA records over peer certificates to build certificate chains correctly. (Architecture-related: external behavior)
  ↳ No PR: [661de44](https://github.com/openssl/openssl/commit/661de442e4231a9b0411dc8562f9e465d1d7fabc)
- Fixed compatibility issues with random APIs in versions below macOS 10.12, and raised the minimum supported version to 10.12. (Architecture-related: platform compatibility)
  ↳ No PR: [24cdb1b](https://github.com/openssl/openssl/commit/24cdb1bfecbd765e829b9932a5a60ff63a7dff4b)
- Roll back unnecessary performance optimizations in PKCS7_verify(), remove temporary read-only memory BIO, simplify logic and fix error handling. (Architecture-related: public API)
  ↳ No PR: [30adf6d](https://github.com/openssl/openssl/commit/30adf6d209002fab688aa76e313ac077e4b2f88c)
- Fixed the issue where the BIO_free function returns a value of 0 when the callback returns a non-positive number. (Architecture-related: public API)
  ↳ No PR: [d8f6c53](https://github.com/openssl/openssl/commit/d8f6c533cfcbcad350c9cfb2c112eb9f938ba83c)
- Fixed that BIO_ctrl, BIO_callback_ctrl, BIO_pop and BIO_next functions no longer log errors when passing in NULL parameters. (Architecture-related: public API)
  ↳ No PR: [398ae82](https://github.com/openssl/openssl/commit/398ae8231650c4bd8ddff0e5efd38233c23b1ca0)
- Optimize the acquisition logic of the EVP_PKEY operation, give priority to obtaining the operation implementation from the key's KEYMGMT, and add a fallback mechanism. When the key cannot be exported from the current provider, try to obtain the operation implementation from the provider to which the key belongs. (Architecture-related: external behavior)
  ↳ No PR: [5246183](https://github.com/openssl/openssl/commit/5246183e7a9f9fb1819d50ab40e2fecc68235e0d), [839ffdd](https://github.com/openssl/openssl/commit/839ffdd11cd48d329a1d89565d62e0be082f9d08)
- Fix X509_PUBKEY_dup function so that it attempts to copy the key instead of just incrementing the reference count. (Architecture-related: public API behavior change)
  ↳ No PR: [7e35458](https://github.com/openssl/openssl/commit/7e35458b511f042d9a37d49227b01096c444e575)
- Fixed an error in the return value check of BN_bn2binpad and BN_bn2nativepad functions to ensure correct judgment of negative or zero values. (Architecture-related: public API)
  ↳ No PR: [098f262](https://github.com/openssl/openssl/commit/098f2627c8d283a518a6e6e60e7893664c7510e0), [944fcfc](https://github.com/openssl/openssl/commit/944fcfc69d16dfd20decdd9cd105436f0043dbe0)
- Fix the problem of d2i_PublicKey when handling the EC parameters in the provided key, and add corresponding test cases. (Architecture-related: public API)
  ↳ No PR: [615a9b8](https://github.com/openssl/openssl/commit/615a9b8798e6ec58f1b2e1ec08a0f6b3c8cb7f60)
- OSSL_PARAM_BLD_push_BN and OSSL_PARAM_BLD_push_BN_pad now return errors for negative parameters, and update related documentation. (Architecture-related: public API)
  ↳ No PR: [db65eab](https://github.com/openssl/openssl/commit/db65eabefe76e44818ff8bd19c68990e7dcc70d3)
- Fixed feature detection failure on ARMv7 and ARM64 CPUs on FreeBSD, by correctly using AT_HWCAP and AT_HWCAP2 constants instead of hardcoded values. (Architecture-related: Platform compatibility)
  ↳ No PR: [c1dabe2](https://github.com/openssl/openssl/commit/c1dabe26e3e96cdce0ffc929e9677840ad089ba5)
- Fixed a parsing error in the OSSL_HTTP_proxy_connect() function when parsing HTTP response headers. (Architecture-related: public API)
  ↳ No PR: [2490d10](https://github.com/openssl/openssl/commit/2490d10d5cca0163cad8045857248b175bdf83e7)
- Fix the problem of HTTP client cleaning up TLS BIO through callback function when disconnecting, and ensure that OSSL_HTTP_close handles the cleanup correctly. (Architecture-related: public API)
  ↳ No PR: [cdaf072](https://github.com/openssl/openssl/commit/cdaf072f90399efb9e8e19ee4f387d1425f12274)
- Fixed the problem of not rejecting negative input of unsigned integer type during parameter parsing, and now correctly reporting the error; and allowing sign extension of OSSL_PARAM_INTEGER type in OSSL_PARAM_allocate_from_text(). (Architecture-related: public API)
  ↳ No PR: [8585b5b](https://github.com/openssl/openssl/commit/8585b5bc62d0bf394ca6adf24f8590e9b9b18402), [946bc0e](https://github.com/openssl/openssl/commit/946bc0e3ec19ca019fcfa95f93c37f34e12fe0bd)
- Allow copying of uninitialized digest contexts, and fix EVP_DigestFinalXOF error handling on finalized contexts. (Architecture-related: public API)
  ↳ No PR: [9ece832](https://github.com/openssl/openssl/commit/9ece8323ea2230092227bf20e5d93012d15d92e9)
- Fixed the issue where EVP_PKEY_CTX_get_rsa_pss_saltlen() failed to return correctly when specifying an integer value, and added a regression test. (Architecture-related: public API)
  ↳ No PR: [6f87463](https://github.com/openssl/openssl/commit/6f87463b62f9b2849510d74ff0fd6a62955ea947)
- Disable the post-cryptographic MAC extension for the GOST cipher suite in TLS 1.2. (Architecture-related: TLS protocol behavior)
  ↳ No PR: [d724da6](https://github.com/openssl/openssl/commit/d724da69389196cdb9ef8db036656882fbc5a6ab)
- Fix OSSL_HTTP_get() timeout processing during redirection, add timeout check, and add retry timeout error code. (Architecture-related: public API)
  ↳ No PR: [f0d5a3b](https://github.com/openssl/openssl/commit/f0d5a3b6ea1bbe4e5dac5b69d853c015db635621)
- Fixed an issue in libssl that incorrectly returned SSL_ERROR_WANT_RETRY_VERIFY when handling
  ↳ No PR: [c1c1bb7](https://github.com/openssl/openssl/commit/c1c1bb7c5e2baa109baec62d2af09d24caae5557)
- Fixed the todata and fromdata operations of EVP_PKEY, so that the private key data is no longer incorrectly included when selecting the public key, and related tests were added. (Architecture-related: public API)
  ↳ No PR: [944f822](https://github.com/openssl/openssl/commit/944f822aadc88b2e25f7695366810c73a53a00c8)
- Re-enable CCM mode of KTLS, because the kernel has fixed the decryption failure problem of CCM mode in TLS 1.3. (Architecture-related: platform compatibility)
  ↳ No PR: [34c2f90](https://github.com/openssl/openssl/commit/34c2f90d8ed325a892618ce0e42ebe916966d4d8)
- Fixed a memory leak caused by the OSSL_CMP_MSG_read function not releasing the allocated message object when file reading failed. (Architecture-related: public API)
  ↳ No PR: [d580c27](https://github.com/openssl/openssl/commit/d580c2790f9f304533a3eda2a9cf6b8eb22830c3)
- Ensure that digest methods created through EVP_MD_meth_new() take the traditional path when initialized, and add tests for custom digests created through EVP_MD_meth_new() to verify that their init and cleanup functions are called correctly. (Architecture-related: external behavior)
  ↳ No PR: [d9ad5b1](https://github.com/openssl/openssl/commit/d9ad5b16b32172df6f7d02cfb1c339cc85d0db01), [fbbe720](https://github.com/openssl/openssl/commit/fbbe7202eba9fba243c18513f4f0316dafb3496d)
- Fix the memory leak problem that may occur when reusing EVP_MD_CTX in EVP_DigestInit_ex(), ensure that the old md_data is correctly released and the cleanup function is called before initialization. (Architecture-related: public API)
  ↳ No PR: [357bccc](https://github.com/openssl/openssl/commit/357bccc8ba64ec8a5f587b04b5d6b6ca9e8dcbdc)
- Fix the problem of null pointer dereference in the BN_hex2bn function, and add a check for the static data flag to prevent errors when passing in static BIGNUM. (Architecture-related: public API)
  ↳ No PR: [f050745](https://github.com/openssl/openssl/commit/f050745fe69a538952f3e12af3718d19ef2df2e2), [7c78bd4](https://github.com/openssl/openssl/commit/7c78bd4be810ddceb8f13585a921946cc98f5fbd)
- Fixed the issue where EVP_PKEY_fromdata incorrectly returns the newly allocated pkey when it fails. It is now released and empty correctly. (Architecture-related: public API)
  ↳ No PR: [5b03b89](https://github.com/openssl/openssl/commit/5b03b89f7f925384c2768874c95f1af7053fd16f)
- Fixed the problem in EVP_PKEY_derive_set_peer_ex that the peer key is exported to the wrong keymgmt. Make sure to use the keymgmt corresponding to the operation for export. (Architecture-related: public API)
  ↳ No PR: [64a8f60](https://github.com/openssl/openssl/commit/64a8f6008acce93d0bf184559c63e66c0cc0e23d)
- Fixed compilation errors caused by SSE disabling in UEFI environment, and added EFIAPI calling convention for abs_val() and pow_10() functions. (Architecture-related: platform compatibility)
  ↳ No PR: [328bf5a](https://github.com/openssl/openssl/commit/328bf5adf9e23da523d4195db309083aa02403c4)
- Added multiple error codes and corresponding error description strings to the CRYPTO module. (Architecture-related: public API)
  ↳ No PR: [826da14](https://github.com/openssl/openssl/commit/826da1451b2525b70f93fcc57ed5dbab61a19591)
- Add detailed error messages for built-in parameter conversion functions, including error conditions such as range overflow, negative unsigned, imprecise real number, error type, buffer too small, empty function parameter and unknown real number size. (Architecture-related: public API)
  ↳ No PR: [ac1082f](https://github.com/openssl/openssl/commit/ac1082f00f991aca1c6e8282717fece16e9bb41f)
- Add error reporting for the failure return path of the OSSL_PARAM_merge function, and uniformly use OPENSSL_strcasecmp instead of strcasecmp. (Architecture-related: public API)
  ↳ No PR: [a10a576](https://github.com/openssl/openssl/commit/a10a576090022e583a06271ceced8e38dd509657)
- Fixed the problem of incorrectly reading *siglen in EVP_DigestSignFinal when sigret is NULL. (Architecture-related: public API)
  ↳ No PR: [a4e0118](https://github.com/openssl/openssl/commit/a4e01187d3648d9ce99507097400902cf21f9b55)
- Fixed the problem of incomplete temporary data cleaning on the s390x platform, ensuring that the entire parameter buffer is cleared correctly. (Architecture-related: platform compatibility)
  ↳ No PR: [79c7acc](https://github.com/openssl/openssl/commit/79c7acc59bb98c2b8451b048ed1dd8cc517df76e)
- Fixed the problem that EVP_PKEY_CTX_set_dh_nid and EVP_PKEY_CTX_set_dhx_rfc5114 did not return errors correctly during parameter conversion, added error handling for invalid values, and added related tests. (Architecture-related: public API)
  ↳ No PR: [f58bb2d](https://github.com/openssl/openssl/commit/f58bb2dd00c3004552c5c1e8d0f2c1390c004cf8), [59d3fd1](https://github.com/openssl/openssl/commit/59d3fd1cc8c938daa6384783a7e5847d6f5201f7)
- Fixed an issue where record length checks may be missed when KTLS is enabled, and added KTLS test support. (Architecture-related: KTLS compatibility)
  ↳ No PR: [8fff986](https://github.com/openssl/openssl/commit/8fff986d52606e1a33f9404504535e2e2aee3e8b)
- Fixed the malloc failure problem caused by zero-byte memory allocation when PEM_write_bio_PKCS8PrivateKey() passes in an empty password string, and added related test cases. (Architecture-related: public API)
  ↳ No PR: [59ccb72](https://github.com/openssl/openssl/commit/59ccb72cd5cec3b4e312853621e12a68dacdbc7e)
- Fixed the counter overflow problem in the PPC AES GCM implementation, added a new wrapper function and adjusted the macro definition to correctly handle the counter. (Architecture-related: platform compatibility)
  ↳ No PR: [345c99b](https://github.com/openssl/openssl/commit/345c99b6654b8313c792d54f829943068911ddbd)
- Include internal/numbers.h in speed.c to solve the problem that SIZE_MAX is not defined on platforms such as z/OS. (Architecture-related: platform compatibility)
  ↳ No PR: [25a0a44](https://github.com/openssl/openssl/commit/25a0a44dc6223e515f5e91e41798cccf09c5612b)
- Restored the check of DH public key size, and added verification of ECDHE uncompressed point format to comply with TLS 1.3 specification; at the same time, the relevant security check logic was adjusted. (Architecture-related: TLS 1.3 protocol behavior)
  ↳ No PR: [d5530ef](https://github.com/openssl/openssl/commit/d5530efada83825ef239a8458db541adc4b422ec), [2c0f7d4](https://github.com/openssl/openssl/commit/2c0f7d46b8449423446cfe1e52fc1e1ecd506b62)
- When compiling with clang on aarch64 architecture and enabling BTI, fall back to the swapcontext implementation to fix setjmp/longjmp compatibility issues. (Architecture-related: platform compatibility)
  ↳ No PR: [d2d2401](https://github.com/openssl/openssl/commit/d2d2401aed7ff45f4c013201944e1218dce12da7)
- Fix the processing logic of obtaining default values from CSR and reference certificates in OSSL_CMP_CTX_setup_CRM(), and update related documents. (Architecture-related: public API)
  ↳ No PR: [c8c9234](https://github.com/openssl/openssl/commit/c8c923454b52d64234c941553d81143918e502ea)
- Treat SSL_kDHEPSK and SSL_kECDHEPSK cipher suites as forward security (PFS) cipher suites at security level ≥ 3. (Architecture-related: Security Behavior)
  ↳ No PR: [b139a95](https://github.com/openssl/openssl/commit/b139a95665eb023b38695d62d9dfc28f3fb89972)
- Use timegm on FreeBSD instead of mktime and timezone variables, fix compilation error in asn1_string_to_time_t, and add memory allocation failure check. (Architecture-related: platform compatibility)
  ↳ No PR: [0176fc7](https://github.com/openssl/openssl/commit/0176fc78d090210cd7e231a7c2c4564464509506)
- Make ASYNC_set_mem_functions thread-safe, and protect the setting and use of custom memory allocation functions by adding read-write locks. (Architecture-related: public API)
  ↳ No PR: [43ed242](https://github.com/openssl/openssl/commit/43ed2429566f27a2fb030316201c0c7af5a2b966)
- Removed the call to pthread_atfork, because the related function is a no-op, and some platforms do not support this function, causing the link to fail. (Architecture-related: platform compatibility)
  ↳ No PR: [5979596](https://github.com/openssl/openssl/commit/5979596247a73d1aec7310e4da0b6023ffd79623)
- Fixed the build warning caused by time_t being a 64-bit type on OpenBSD, and adjusted the printing format of SSL session time value. (Architecture-related: platform compatibility)
  ↳ No PR: [9362638](https://github.com/openssl/openssl/commit/9362638b080e328ccab43f89048bed27bcf2f11d)
- Disable duplicate HelloRetryRequest messages. (Architecture-related: TLS protocol behavior)
  ↳ No PR: [d204a50](https://github.com/openssl/openssl/commit/d204a50b898435fbf937316d5693008cebf62eef)
- In TLSv1.3, limit the lifetime hint of session tickets to at most 1 week to comply with RFC 8446 specification, and add corresponding test cases. (Architecture-related: TLS protocol behavior)
  ↳ No PR: [0089cc7](https://github.com/openssl/openssl/commit/0089cc7f9d42f6e39872161199fb8b6a99da2492)
- Fixed the problem of OSSL_PARAM_get_*_ptr series functions incorrectly retaining the wrong state when the pointer does not match the string type, and added the ossl_param_get1_octet_string function to extract parameters to the allocated buffer. (Architecture-related: public API)
  ↳ No PR: [327a720](https://github.com/openssl/openssl/commit/327a720d5dd011b853acbdd0223933f6ecd22928)
- Allows DH parameters to be specified anywhere in the SSL configuration command, and adds corresponding test cases. (Architecture-related: external behavior)
  ↳ No PR: [b2b8d18](https://github.com/openssl/openssl/commit/b2b8d1883a3b7e64006b0b4ada0cbcf3eb6dba1a)
- Fixed the compilation problem in recordmethod.h caused by the conflict between the function pointer name new and C++ reserved words, and renamed it to new_record_layer. (Architecture-related: public API)
  ↳ No PR: [11653dc](https://github.com/openssl/openssl/commit/11653dcd6ecbc7ff3c53f694474ece08ce4473aa)
- Fixed a logical error in the memory allocation failure that may occur due to not checking the return value of X509V3_add_value in the X509V3_parse_list function. (Architecture-related: public API)
  ↳ No PR: [bcd5645](https://github.com/openssl/openssl/commit/bcd5645b34c319b8e4d72d6850ead80e85f18921)
- Repair DH private key check: when the q parameter is missing, it no longer directly fails, but instead performs a reasonable range check based on p and length; at the same time, the boundary conditions of the public key check are enhanced. (Architecture-related: external behavior)
  ↳ No PR: [0615ced](https://github.com/openssl/openssl/commit/0615cedecda7ed18300db48b0bb56cec6d3527bd)
- Move the call of ossl_deinit_casecmp to the end of OPENSSL_cleanup to ensure that the cleanup function that relies on OPENSSL_strcasecmp can be executed normally. (Architecture-related: external behavior)
  ↳ No PR: [1d64b06](https://github.com/openssl/openssl/commit/1d64b068ca74b68394c96fd2e3020235d32928f2)
- Fix BIO_get_ktls_send and BIO_get_ktls_recv macros to ensure that their return value is only 0 or 1. (Architecture-related: public API)
  ↳ No PR: [524bac5](https://github.com/openssl/openssl/commit/524bac570702a79366b85ff1f66e07d3e002370c)
- Fixed the problem of KTLS being enabled prematurely resulting in connection failure when using BIO_new_connect. It will be enabled after the connection is successful. (Architecture-related: public API)
  ↳ No PR: [598bd77](https://github.com/openssl/openssl/commit/598bd7741568a1aae678e5472f18aae1ab991e8d)
- Make OSSL_LIB_CTX_load_config thread-safe and add read-write lock protection for configuration module list operations. (Architecture-related: public API)
  ↳ No PR: [ef7a9b4](https://github.com/openssl/openssl/commit/ef7a9b44f04ef18b652cb47cd9eb3826301cca9e)
- Implement UnsafeLegacyServerConnect configuration options to make them consistent with the documentation description. (Architecture-related: public API)
  ↳ No PR: [65b2bb9](https://github.com/openssl/openssl/commit/65b2bb9ca0cff5e65938dc0d9dcd71c251bd67db)
- Add missing declarations for the random seed function, correct parameter types to match the core schedule definition, and add a new user entropy acquisition function. (Architecture-related: Random seed function interface)
  ↳ No PR: [9574842](https://github.com/openssl/openssl/commit/9574842e90e29015daa2b071e965cec9aa885c17)
- Check expected Content-Type only when HTTP status code is 200. (Architecture-related: HTTP response handling)
  ↳ No PR: [e3477d3](https://github.com/openssl/openssl/commit/e3477d3e5ccd971da3d8a90a7d5096b47372d288)
- Fixed undefined behavior caused by seed length being 0 in EC_GROUP_new_from_ecparameters, added length check and returned error. (Architecture-related: public API behavior fix)
  ↳ No PR: [97de614](https://github.com/openssl/openssl/commit/97de6145851922a33f7afd9c308adfc1b2e5732b)
- Fixed the return value checking defect in the EVP_PKEY_get_params function to ensure correct judgment of whether the parameter acquisition is successful. (Architecture-related: public API behavior repair)
  ↳ No PR: [7e5e911](https://github.com/openssl/openssl/commit/7e5e91176b770a68bdaf73a5c647f1fc0d7f2900)
- Upgraded the serverinfo format in SSL_CTX_use_serverinfo() to v2, and fixed related error handling. (Architecture-related: public API)
  ↳ No PR: [555dd93](https://github.com/openssl/openssl/commit/555dd9390ba56f1c400d3f067a2dfe7b00fbf7d3)
- Fixed the problem of incomplete check of return values of functions such as EVP_CIPHER_CTX_set_key_length to ensure that negative return values can be handled correctly. (Architecture-related: public API)
  ↳ No PR: [8d9fec1](https://github.com/openssl/openssl/commit/8d9fec1781751d2106d899c6076eeb3da6930bfe)
- Fixed the issue of incorrect return value checking of EVP_PKEY_CTX_set_rsa_pss_saltlen and EVP_PKEY_CTX_get_rsa_pss_saltlen functions. (Architecture-related: public API)
  ↳ No PR: [7263a7f](https://github.com/openssl/openssl/commit/7263a7fc3d0c0c17616c2e5309e0fd52ed654ecc)
- Repair the return value check of the EVP_PKEY_CTX_set/get_* series of functions, and change the original Boolean value judgment to the correct <=0 comparison to ensure that failure situations can be captured correctly. (Architecture-related: public API)
  ↳ No PR: [2cba2e1](https://github.com/openssl/openssl/commit/2cba2e160d5b028e4a777e8038744a8bc4280629)
- Improved RSA key generation behavior: in non-FIPS mode, fallback to multi-prime key generation method when public key exponent e is less than 65537; explicitly throw error "no prime candidate" when no prime candidate is found. (Architecture-related: public API)
  ↳ No PR: [27c1cfd](https://github.com/openssl/openssl/commit/27c1cfd7653b7204af3301f93ccd2a3decfc309b), [d2399d8](https://github.com/openssl/openssl/commit/d2399d8cd29f56e6614f0b3db4e7e563a745902a)
- Fixed "defined but not used" warning/error caused by conditional compilation macro error in OPENSSL_atexit function. (Architecture-related: public API)
  ↳ No PR: [979575c](https://github.com/openssl/openssl/commit/979575c6ef10ab9b8d74d8c00852b2250eb78f29)
- Fixed the problem that the handshake sequence number is not reset correctly when retransmitting ClientHello in DTLS. (Architecture-related: DTLS handshake behavior)
  ↳ No PR: [81926c9](https://github.com/openssl/openssl/commit/81926c91567cd5d11eec38b9980438f45b276d72)
- Improve the use of the use_ssl parameter in the OSSL_HTTP_open function to ensure that a clear Boolean value is passed to the callback function. (Architecture-related: public API)
  ↳ No PR: [35750cb](https://github.com/openssl/openssl/commit/35750cb9af007702dad92d62da57200fdf9ddaf4)
- Fixed a memory leak caused by X509V3_add1_i2d not releasing memory when deleting the extension under the X509V3_ADD_DELETE flag. (Architecture-related: public API)
  ↳ No PR: [4798e06](https://github.com/openssl/openssl/commit/4798e0680b112993815098ca21d7d68ff31ebc6e)
- Make all EVP _is_a functions accept and handle NULL parameters safely, avoiding null pointer dereference. (Architecture-related: public API)
  ↳ No PR: [ee8db8c](https://github.com/openssl/openssl/commit/ee8db8c5fb5b091f48d29914126d35a7e29cdcf2)
- Fixed the signed displacement problem detected by UBSAN under the aarch64 architecture, and added U suffix to the integer constants in the relevant macro definitions to ensure unsigned operations. (Architecture-related: platform compatibility)
  ↳ No PR: [1efd853](https://github.com/openssl/openssl/commit/1efd8533e1ccc5c5e69795eb393a6b79b62e48e2)
- When initializing the DTLS record layer, make sure to use datagram memory BIO instead of ordinary memory BIO. (Architecture-related: DTLS record layer behavior)
  ↳ No PR: [db1a505](https://github.com/openssl/openssl/commit/db1a505ced696b104b03a072079e663cceecf692)
- Remove the reference to rlayer.rstate, and fix the ssl3_pending function to correctly return the length of pending application data. (Architecture-related: public API behavior)
  ↳ No PR: [8bbf7ef](https://github.com/openssl/openssl/commit/8bbf7ef63f95e0ef99e235eab777878d134ed302)
- Add manual locking mechanism for VC++ 2008 and earlier x86 compilers to solve Windows XP 32bit compatibility issues caused by the lack of InterlockedOr64 inline implementation. (Architecture-related: Platform compatibility)
  ↳ No PR: [2d46a44](https://github.com/openssl/openssl/commit/2d46a44ff24173d2cf5ea2196360cb79470d49c7)
- Fixed the issue in DTLS that SSL_pending() and SSL_has_pending() did not consider buffering application data. (Architecture-related: public API behavior)
  ↳ No PR: [6d6b295](https://github.com/openssl/openssl/commit/6d6b295ac39fcb0461f25fda69983d2dbb75f8f1)
- Fixed a segmentation fault in PEM_write() caused by calling strlen() when the header parameter is NULL. (Architecture-related: public API)
  ↳ No PR: [2059574](https://github.com/openssl/openssl/commit/205957405d08ef199e6ab654e333a627bbca9ccc)
- Fix the regression problem in the CMS_final function that ignores the result of CMS_dataFinal, and ensure that the error is returned correctly when the signature fails. (Architecture-related: public API)
  ↳ No PR: [b037561](https://github.com/openssl/openssl/commit/b03756130dadb3732b460a6efd930f1b226acdad)
- Fixed the issue in EVP_CIPHER_CTX_get_iv_length() that may return out-of-bounds values due to lack of range check, and improved the default logic to fall back to the cipher's IV length when the cipher context does not support obtaining the IV length. (Architecture-related: public API)
  ↳ No PR: [e0e338c](https://github.com/openssl/openssl/commit/e0e338c8c50c226efc92fe79c788c9cdc03fc01f)
- Fixed the problem of SMIME_crlf_copy return value being ignored, now the error can be returned correctly when memory allocation fails. (Architecture-related: external behavior)
  ↳ No PR: [67c0460](https://github.com/openssl/openssl/commit/67c0460b89cc1b0644a1a59af78284dfd8d720af)
- Fixed a regression in EC_KEY_set_private_key(), which now allows setting the private key to NULL and maintains backward compatibility. (Architecture-related: public API)
  ↳ No PR: [b304b3e](https://github.com/openssl/openssl/commit/b304b3e8f7397c3e949e3664e6ceaee5dc811b32), [d93f154](https://github.com/openssl/openssl/commit/d93f154d5a524e6ed71ff276447de7fe11d85949)
- Check whether the IV length is less than zero. If EVP_CIPHER_CTX_get_iv_length returns -1, it is regarded as an error and processed. (Architecture-related: public API)
  ↳ No PR: [83ab43d](https://github.com/openssl/openssl/commit/83ab43da0c9f67c5069605552b1332ca5fadecf1)
- Fix the regression introduced by GCM mode reconstruction, adjust the default implementation of each platform and improve the RISC-V instruction set branch support. (Architecture-related: RISC-V support)
  ↳ No PR: [186be8e](https://github.com/openssl/openssl/commit/186be8ed26f5561faf91d6da3ed14cd9cb6617dd)
- Fixed the problem in the session cache that new entries were accidentally deleted due to the order of addition, adjusted the addition logic, and supplemented related tests. (Architecture-related: public API behavior)
  ↳ No PR: [4842a27](https://github.com/openssl/openssl/commit/4842a27b902660b672d72d2ed23e941461ca481c)
- Fixed the problem that the PKCS7_dataVerify function did not use the Certificate Revocation List (CRL) when verifying the PKCS#7 signature, and also cleaned up the related variable naming. (Architecture-related: public API behavior)
  ↳ No PR: [2b44565](https://github.com/openssl/openssl/commit/2b44565476d9d6d86f5af0ec736a7bf6f77a839e)
- Improved error checking and error reporting of X.509 attribute-related functions, and optimized code style. (Architecture-related: public API)
  ↳ No PR: [ba9e372](https://github.com/openssl/openssl/commit/ba9e3721febb073397248154a846f2088efd6409)
- Fixed the processing logic of fallback theme in OSSL_CMP_CTX_setup_CRM(), giving priority to using the theme name from CSR as the default value. (Architecture-related: public API)
  ↳ No PR: [7af110f](https://github.com/openssl/openssl/commit/7af110f9f5fb9b039cc09b63768a0b989a7bf5ad)
- Directly return the error of insertion failure in X509_VERIFY_PARAM_add0_table, and add sorting in X509_VERIFY_PARAM_lookup to ensure the correctness of the lookup, while improving the coding style. (Architecture-related: public API)
  ↳ No PR: [38ebfc3](https://github.com/openssl/openssl/commit/38ebfc3f5f83cbbd01011636d159ad3ed23e9765)
- Added missing direct error reporting and improved coding style in stack.c, and also corrected the loose use of stack API in multiple files. (Architecture-related: public API)
  ↳ No PR: [30eba7f](https://github.com/openssl/openssl/commit/30eba7f35983a917f1007bce45040c0af3442e42)
- Fixed the setting logic of the modified flag in the X509 and
  ↳ No PR: [39d356e](https://github.com/openssl/openssl/commit/39d356e084f6a4e48decf0644961255e6777b071), [9249a34](https://github.com/openssl/openssl/commit/9249a34b076df9a9d55ab74ab465d336980cae6a), [8e39049](https://github.com/openssl/openssl/commit/8e39049d38ebe8b8398d6c4aa8a6f7cef9712132)
- Unify ZLIB conditional compilation macros to the OPENSSL_NO_ZLIB prefix, and make the BIO_f_zlib() function always available. (Architecture-related: public API and build configuration)
  ↳ No PR: [59d2129](https://github.com/openssl/openssl/commit/59d21298df9176b64b41cc8583c7024f7f5895d4)
- Fixed the return type of the rlayer_skip_early_data callback function, corrected it from pointer type to int, and solved the test failure problem caused by copy and paste errors. (Architecture-related: public API)
  ↳ No PR: [e921882](https://github.com/openssl/openssl/commit/e921882d57201e14cc6a48765b2281065d6f5c65)
- Fixed an issue in TLSv1.3 that caused the connection to a defective server to fail due to strict checking of legacy_record_version. Now the client will ignore the wrong record version. (Architecture-related: TLS compatibility)
  ↳ No PR: [2093428](https://github.com/openssl/openssl/commit/2093428834151ea4788aa773b5aa2d35e0bbc90a)
- Fixed the problem that the key length was not set correctly when deriving ECX keys on the s390x platform, and adjusted the derivation logic to make it consistent with the universal code. (Architecture-related: s390x compatibility)
  ↳ No PR: [3cca05c](https://github.com/openssl/openssl/commit/3cca05cc194c0528865deea57d9e60ca3fb0e5d3)
- Fixed issues with BIO_sendmmsg and BIO_recvmmsg on FreeBSD, including handling the situation where the loopback socket does not support local addresses on BSD systems, and corrected the way to obtain the address parameter in sendmmsg. (Architecture-related: FreeBSD compatibility)
  ↳ No PR: [0768779](https://github.com/openssl/openssl/commit/07687790a055a039bba93ee00ac970c9710f0669)
- Fixed the fallback logic of AES-GCM on Power 8 CPU, correctly using the default implementation when necessary instructions are missing. (Architecture-related: platform compatibility)
  ↳ No PR: [9ab6b64](https://github.com/openssl/openssl/commit/9ab6b64ac856157a31a54c0d12207c2338bfa8e2)
- Fixed that CMS_add0_cert no longer reports an error when the certificate already exists, but instead silently ignores and returns success; also fixed the resource leak problem when reference counting fails in CMS_add1_cert and CMS_add1_crl. (Architecture-related: public API)
  ↳ No PR: [65def9d](https://github.com/openssl/openssl/commit/65def9de8088ae39d8f251e0b57f1a0f204daa14)
- Fixed the compatibility issue between the EVP_PKEY_eq function and the 3.0.0 FIPS provider, adjusting the selection parameters when comparing according to whether the key contains a public key. (Architecture-related: public API)
  ↳ No PR: [c342004](https://github.com/openssl/openssl/commit/c342004e07fd2c03a672f79353d13554fe0ffdaf), [e5202fb](https://github.com/openssl/openssl/commit/e5202fbd461cb6c067874987998e91c6093e5267)
- Fixed the problem of omitting to reset ctx->genm_ITAVs in OSSL_CMP_CTX_reinit() to avoid errors in subsequent OSSL_CMP_exec_GENM_ses() calls. (Architecture-related: public API)
  ↳ No PR: [1c04866](https://github.com/openssl/openssl/commit/1c04866c671db4a6db0a1784399b351ea061bc16)
- Fixed the code format problem in the CMP and CRMF modules, and corrected the parameter checking logic of the certificate revocation request and the conditional judgment when printing PKIStatusInfo. (Architecture-related: public API)
  ↳ No PR: [357bfe7](https://github.com/openssl/openssl/commit/357bfe73453b018c7aee94cbb4f6eeca8b85695a)
- Fixed the problem that BIO_ctrl_pending and BIO_ctrl_wpending may return wrong values when the underlying error is returned, and set the upper limit of the return value to SIZE_MAX to prevent overflow. (Architecture-related: public API)
  ↳ No PR: [e9809f8](https://github.com/openssl/openssl/commit/e9809f8a09147bc27f974caa908b04439c006625), [c6be0aa](https://github.com/openssl/openssl/commit/c6be0aa8ac3c172ad998ce33f392143312bfe760)
- Fixed an incorrectly reported error in d2i_CMS_ContentInfo and adjusted related test cases. (Architecture-related: public API)
  ↳ No PR: [678b489](https://github.com/openssl/openssl/commit/678b489a2ae8af289cef939a538235686b448c0e)
- Added a solution for DJGPP platform to convert UTC timestamp to time_t by setting environment variable TZ=UTC. (Architecture-related: platform compatibility)
  ↳ No PR: [cffb65f](https://github.com/openssl/openssl/commit/cffb65f2ff85f19418ed121275901674824e52ca)
- Fixed the problem of missing IP address family length check, and added length check in the normalization and normalization functions. (Architecture-related: public API)
  ↳ No PR: [9351f67](https://github.com/openssl/openssl/commit/9351f675fab42abbc321f0994bff7e0b27cfbe57)
- Fixed the marking and return value issues of modified fields in X509, X509_CRL and X509_REVOKED related set and sign functions. (Architecture-related: public API)
  ↳ No PR: [7e0013d](https://github.com/openssl/openssl/commit/7e0013d9736db005695bdc7524295c3b52d711d3)
- Fixed the issue where the cached TBSCertificate is no longer implicitly refreshed when signing the certificate. Ensure that the modified flag is correctly set before signing to ignore the cached encoding. (Architecture-related: public API: X509_sign_ctx)
  ↳ No PR: [963e0bc](https://github.com/openssl/openssl/commit/963e0bc43369a6dbe6644f709630f6c9f63dccf9)
- Fixed SCTP compilation error, added ossl_statem_get_state function, and changed the parameter type of SSL_in_before and ossl_statem_clear from SSL* to SSL_CONNECTION*. (Architecture-related: public API: parameter type change)
  ↳ No PR: [846975f](https://github.com/openssl/openssl/commit/846975f367f75f3503b44c12e49d980dca181647)
- Added missing default fallback implementation for ghash on x86_64 platform. (Architecture-related: Platform compatibility)
  ↳ No PR: [be0161f](https://github.com/openssl/openssl/commit/be0161ff100bf10c9549fc09ce4513681011da1c)
- Fixed the implementation of SSL_tick and SSL_get_tick_timeout in the QUIC front-end I/O API so that it returns the success status correctly. (Architecture-related: public API)
  ↳ No PR: [fbe2573](https://github.com/openssl/openssl/commit/fbe2573d3b54dcaab1eab3401f2948a0f01ee49a)
- Adjusted error returns and error codes in QUIC handshake processing, added cleaning support for send streams, and modified the timeout query interface to accept SSL objects. (Architecture-related: interface changes)
  ↳ No PR: [ca41f6b](https://github.com/openssl/openssl/commit/ca41f6b7e974e7a8e814705cbf693bd9ea3a10cc)
- Treat received unknown frame types as protocol violations, triggering protocol errors directly instead of ignoring and continuing processing. (Architecture-related: QUIC protocol behavior)
  ↳ No PR: [ce3106b](https://github.com/openssl/openssl/commit/ce3106baba7601bfaf1d1412221e18dec4878e18)
- Fixed the handling of zero-valued BIGNUM in the parameter API, ensuring that zero-valued BIGNUM allocates at least one data byte when building parameters via OSSL_PARAM_BLD, and correctly represents zero in OSSL_PARAM_set_BN. (Architecture-related: public API)
  ↳ No PR: [c455f87](https://github.com/openssl/openssl/commit/c455f87aebf245814ba58d6a398b45ca4e80d1d7), [c2ae891](https://github.com/openssl/openssl/commit/c2ae89148343750e420b72ef1b709ebbc16e47b8)
- Fix the constant error in name printing flag comparison in X509_REQ_print_ex and
  ↳ No PR: [d7f20c7](https://github.com/openssl/openssl/commit/d7f20c79920ba0e74a775bb145bfa9d4a3606492), [e176569](https://github.com/openssl/openssl/commit/e17656948663adb14b9030aeae70171da5588179)
- Disable enabling partial write mode (EPW) while AON write operations are in progress, and remove related repair functions. (Architecture-related: QUIC write operation behavior)
  ↳ No PR: [dfc227b](https://github.com/openssl/openssl/commit/dfc227bd245c356aea11dfdec9fe0f3d66bca16e)
- Modify the conditions for judging read completion in the QUIC front-end I/O API to ensure that the completion status is correctly returned when the write length is zero. (Architecture-related: public API)
  ↳ No PR: [3f0c310](https://github.com/openssl/openssl/commit/3f0c310b80626f6286022f30a7a280b3306587ca)
- Fall back to the change of adding datagram support to BIO_s_mem() and restore the original streaming memory BIO behavior. (Architecture-related: external behavior)
  ↳ No PR: [6e193d4](https://github.com/openssl/openssl/commit/6e193d4d03f6c7bdf95e82e226c5fccbd67562f2)
- Fix the bin2bn function: when the input length is zero, directly return the cleared BIGNUM, making calls with s==NULL and len==0 safer. (Architecture-related: public API)
  ↳ No PR: [1b24b5a](https://github.com/openssl/openssl/commit/1b24b5a1b43c2af0a6c1cb2d196f5132ee723488)
- Fix the problem that the bn2bin function does not accept negative lengths, and add related tests. (Architecture-related: public API)
  ↳ No PR: [c9466f3](https://github.com/openssl/openssl/commit/c9466f38e0191aa86e0bd49267b0c4ef33e3a3d2)
- Disable calling SRTP related functions in QUIC TLS connections. (Architecture-related: public API)
  ↳ No PR: [f082205](https://github.com/openssl/openssl/commit/f082205bcfc8e361e53bb2f39f46b46097ec784a)
- Fixed the problem of incomplete EVP_CIPHER_asn1_to_param return value check, changed the two conditions that only check <0 to <=0, and correctly handled EVP_CIPHER_get_asn1_iv to return zero as success. (Architecture-related: public API)
  ↳ No PR: [114d99b](https://github.com/openssl/openssl/commit/114d99b46bfb212ffc510865df317ca2c1542623)
- Fix PKCS12_newpass() to support PBES2 encrypted PKCS12 files, and add libctx and propq parameter support. (Architecture-related: public API)
  ↳ No PR: [9191dfb](https://github.com/openssl/openssl/commit/9191dfb0ef48f95002aecfa8e11d9db434b4093d)
- Fix the regression problem in OSSL_CMP_certConf_cb when checking newly registered certificates, improve the certificate verification logic, and add corresponding tests. (Architecture-related: public API: CMP certificate verification)
  ↳ No PR: [6b58f49](https://github.com/openssl/openssl/commit/6b58f498b3f5d8e4c9197c3c5228fb450e33aaaf)
- Fixed the problem of status setting in transaction processing between CMP server and client, including correctly setting recipNonce when message verification fails, and supplementing the missing rejection status when the client rejects a new certificate. (Architecture-related: public API)
  ↳ No PR: [036a444](https://github.com/openssl/openssl/commit/036a444fdc77b36e0bfcc8b765acf96036f5a0b3), [e7041bf](https://github.com/openssl/openssl/commit/e7041bfea77cc7e6bab1fe8d2745b6969a8c78aa)
- Fixed the problem of an error being reported when only two keys are set when randomly generating keys with dual-key triple DES; fixed the error checking of RSA_public_decrypt, ASN1_item_i2d and other functions; fixed the possible null pointer dereference problem in EVP_PKEY related functions. (Architecture-related: public API)
  ↳ No PR: [587e040](https://github.com/openssl/openssl/commit/587e0407803af330c0b04238fcbce78521ce35d7), [8195e59](https://github.com/openssl/openssl/commit/8195e59986031f6f33e2569551d771904433fa04), [5df5032](https://github.com/openssl/openssl/commit/5df5032ab02d7a17e07435de777d730bae190253), [ab5a172](https://github.com/openssl/openssl/commit/ab5a172f1b41b12133b95822d5bf004c322965cb)
- Fixed a possible double free problem in CMS_add1_crl, and a use-after-free memory error in the SSL library. (Architecture-related: public API)
  ↳ No PR: [6f9e531](https://github.com/openssl/openssl/commit/6f9e531003fd736e8e96d9a1a57f7763da9722b8), [c4a44e7](https://github.com/openssl/openssl/commit/c4a44e7b84c5371e6f1ac1e0a80d5fc737b2dc1c)
- Fixed the memory leak problem caused by repeated calls to SSL_CTX_set1_groups_list. Release the original memory before overwriting the pointer. (Architecture-related: public API)
  ↳ No PR: [62ea5ff](https://github.com/openssl/openssl/commit/62ea5ffa7c8882ba90b26ab1deb0d977dcb5165c)
- Fixed skipping subdirectories in the SSL_add_dir_cert_subjects_to_stack function to avoid loading the directory as a certificate file. (Architecture-related: public API)
  ↳ No PR: [1dc35d4](https://github.com/openssl/openssl/commit/1dc35d44f355a7371a1ff8a457586938cc7b168a)
- Fixed the double release vulnerability of the OSSL_HTTP_get function, by initializing the request context pointer to NULL and leaving it empty after release to avoid repeated release. (Architecture-related: public API)
  ↳ No PR: [7fed519](https://github.com/openssl/openssl/commit/7fed5193d242938d9ac5a0c1cb32b22b33379a06)
- Fixed multiple minor issues in thread-assisted mode: added an interface to check whether the client is connected, ensured that thread-assisted resources are properly cleaned up when released, and corrected the condition variable release method. (Architecture-related: public API)
  ↳ No PR: [dbe7b51](https://github.com/openssl/openssl/commit/dbe7b51a8e3c0e20c3412fe4ff8309730a135255)
- When context copying fails in signing and verification operations, an error will no longer be returned immediately. Instead, the original context will continue to be used to avoid interrupting the process due to copying failure. (Architecture-related: public API behavior)
  ↳ No PR: [0fc00fc](https://github.com/openssl/openssl/commit/0fc00fc0e3867fc5f95fab1046ad7d2a85db06f8)
- Fixed the infinite loop problem caused by invalid parameters (such as q=1 or priv=0) during the DSA signing process, and added retry limit and parameter verification. (Architecture-related: public API behavior)
  ↳ No PR: [3a4e09a](https://github.com/openssl/openssl/commit/3a4e09ab42654b3d223f0f8dd1a9c58b2902ddcc)
- Fix the problem in ECDSA signature that may cause infinite loop due to invalid group parameters, add minimum order number check and maximum retry limit. (Architecture-related: public API behavior)
  ↳ No PR: [5f820bd](https://github.com/openssl/openssl/commit/5f820bd7535b871fdfdc0303c3af23ba4be901f0)
- Fixed typos in certificate verification error strings, and added support for Raw public key untrusted error codes. (Architecture-related: public API)
  ↳ No PR: [1caa483](https://github.com/openssl/openssl/commit/1caa4835eb140682ba091bf328758fc6535e70bc)
- Fixed the type conversion error when assigning size in EVP_DigestFinal_ex. (Architecture-related: public API)
  ↳ No PR: [b1cd268](https://github.com/openssl/openssl/commit/b1cd268c034268f4d37c665ee4b5148f9d8700bb)
- Fixed the problem in EVP_PBE_CipherInit_ex that the fallback mechanism failed due to not assigning the return value of EVP_get_digestbynid to md. (Architecture-related: public API)
  ↳ No PR: [c09c202](https://github.com/openssl/openssl/commit/c09c202e9bc66f0300ee598ca94f2b3fa5a5899d)
- Handle the case where EVP_PKEY_get_default_digest_name returns UNDEF, allowing specific algorithms to not specify a digest. (Architecture-related: public API)
  ↳ No PR: [af99d55](https://github.com/openssl/openssl/commit/af99d55078582fb2ac35787043d56e0c10b1fe97)
- Add the finalized flag to the EVP summary context to prevent the completed context from being incorrectly reused. (Architecture-related: public API)
  ↳ No PR: [3fc2b7d](https://github.com/openssl/openssl/commit/3fc2b7d6b8f961144905330dfd4689f5bd515199)
- Provide more specific error codes for QUIC handshake failures, such as SSL_R_REMOTE_PEER_ADDRESS_NOT_SET when the peer address is not set, and SSL_R_BIO_NOT_SET when the BIO is not set. (Architecture-related: public API)
  ↳ No PR: [44a1ac5](https://github.com/openssl/openssl/commit/44a1ac5de0cb422bc65089e1e3bf1b46bb8ab141)
- Fix the behavior of the SSL_has_pending function under QUIC connection so that it can correctly detect whether there is pending data. (Architecture-related: public API)
  ↳ No PR: [560470b](https://github.com/openssl/openssl/commit/560470b5d97ea5f122d53d1b85e9f384f8ba9023)
- Fix the regression problem of OBJ_nid2obj function returning NULL for NID_undef, so that it returns UNDEF object. (Architecture-related: public API behavior change)
  ↳ No PR: [908ba3e](https://github.com/openssl/openssl/commit/908ba3ed9adbb3df90f7684a3111ca916a45202d)
- Adjust the order of HPKE API parameters, moving libctx and propq to the end as optional parameters to maintain consistency with other HPKE APIs. (Architecture-related: public API)
  ↳ No PR: [8b7b9aa](https://github.com/openssl/openssl/commit/8b7b9aac444625195486efd10273694830c41398)
- Modify SM4 capability detection conditions, restrict it to __aarch64__ architecture, remove checks for __arm__ and __ARM_MAX_ARCH__. (Architecture-related: platform compatibility)
  ↳ No PR: [09cb871](https://github.com/openssl/openssl/commit/09cb8718fd65dc7126247808cb96b05147bb923f)
- Fixed the problem that OPENSSL_die did not call abort() correctly in UEFI environment. (Architecture-related: platform compatibility)
  ↳ No PR: [c0e090b](https://github.com/openssl/openssl/commit/c0e090bd61d2e46a1d8f60f39f10152c87e87753)
- Fix the return type of the OSSL_CRMF_CERTTEMPLATE_get0_publicKey function and remove the const qualifier. (Architecture-related: public API)
  ↳ No PR: [09f30b0](https://github.com/openssl/openssl/commit/09f30b0c96e39e3a07f8e6854c5468332534c585)
- Fixed a regression in SSL certificate directory loading when building without POSIX IO: skip the current directory and parent directory when reading the directory, avoid using stat() to check whether the file is a directory. (Architecture-related: platform compatibility)
  ↳ No PR: [3155b5a](https://github.com/openssl/openssl/commit/3155b5a90e6ad9c7369d09e70e81686f4b321a73)
- No longer send empty renegotiation info SCSV in TLS 1.3 and above; copy minimum and maximum protocol versions only if the SSL object's method type is the same as SSL_CTX; tighten the determination of valid DTLS versions. (Architecture-related: protocol behavior)
  ↳ No PR: [1eef26b](https://github.com/openssl/openssl/commit/1eef26bd8924058b9ba0e52786b6afab80db23a9), [4f373a9](https://github.com/openssl/openssl/commit/4f373a9773efa63fdb73f3972f13ab78b9342b70), [861cd89](https://github.com/openssl/openssl/commit/861cd8964bfeb955408e93048d118e1826e12d0c)
- Initialize the rstate variable of the record layer, ensure that the SSL_rstate_string*() API returns a value consistent with the old version; adjust the QUIC record layer state string return value to make it consistent with the TLS version. (Architecture-related: public API)
  ↳ No PR: [73bac6e](https://github.com/openssl/openssl/commit/73bac6e28014bfecc322c67aa8b09077e34da299), [5758245](https://github.com/openssl/openssl/commit/57582450318e955632d8fb09f42bd90f2ed5d3b4)
- Fixed the issue where the CMP client returns an error response when using the -csr option when no private key is provided; restructured the private key acquisition logic and added a new public key acquisition function; fixed the issue of checking the new certificate when the old certificate has no private key. (Architecture-related: public API)
  ↳ No PR: [2d65859](https://github.com/openssl/openssl/commit/2d6585986f3b754750b25e7a296a08e7129a5320), [e0f1ec3](https://github.com/openssl/openssl/commit/e0f1ec3b2ec1b137695abc3199a62def5965351f)
- Fixed the retry flag copying problem in the flush operation of zlib and ok BIO, making the flush operation retryable. (Architecture-related: BIO behavior)
  ↳ No PR: [bcbc7d6](https://github.com/openssl/openssl/commit/bcbc7d60679b79fa4347e33c865306dce41ed985)
- Fix the stack corruption problem in the UI module, ensure that UI_new returns NULL and handle it correctly to avoid stack corruption caused by uninitialized password buffer. (Architecture-related: public API)
  ↳ No PR: [a64c48c](https://github.com/openssl/openssl/commit/a64c48cff88e032cf9513578493c4536df725a22)
- Fix the parameter type of macsaltlen option so that it accepts positive integers instead of no parameters. (Architecture-related: command line interface)
  ↳ No PR: [26cf076](https://github.com/openssl/openssl/commit/26cf0767a71743de00cd20f90526052358d67d03)
- Optimize the OSSL_sleep function, use sleep() and usleep() combination on Unix systems to solve long-latency compatibility issues, and simplify sleep implementation on Windows platforms. (Architecture-related: platform compatibility)
  ↳ No PR: [2631a94](https://github.com/openssl/openssl/commit/2631a941469864a35258130082096876e7243225)
- Correct the implementation of QUIC time callback coverage, change the function return value from void to int, and add thread safety lock protection, while ensuring that the callback is used correctly to obtain the time when the channel is created. (Architecture-related: public API)
  ↳ No PR: [e3e9794](https://github.com/openssl/openssl/commit/e3e9794aa49f61e5b034608488034daa01125c85)
- Fix the memory leak of encrypted content key in CMS_ContentInfo_free, and enhance the defensive check of null pointer in ossl_cms_get0_env_enc_content. (Architecture-related: public API)
  ↳ No PR: [7a18574](https://github.com/openssl/openssl/commit/7a1857483938b6b6eec5b8760c68c71a71296cd2)
- Fixed the problem that the RAND_poll function failed to reseed correctly in non-deprecated builds, ensuring that it can call RAND_seed for reseeding. (Architecture-related: public API: RAND_poll reseeding behavior fixed)
  ↳ No PR: [cc343d0](https://github.com/openssl/openssl/commit/cc343d047c147e0a395fb101efbe9dedf458aa17)
- Fixed OSSL_CMP_MSG_http_perform(), added OSSL_CMP_OPT_USE_TLS option to control whether to use TLS, and optimized the judgment logic of TLS usage. (Architecture-related: public API: added OSSL_CMP_OPT_USE_TLS option)
  ↳ No PR: [ac0677b](https://github.com/openssl/openssl/commit/ac0677bd2394c04632f7ad526879a866b6ed149f)
- Fixed the problem that the BN_RECP_CTX_set function did not check whether the parameter d is zero, and failed to return early when d was zero. (Architecture-related: public API)
  ↳ No PR: [43596b3](https://github.com/openssl/openssl/commit/43596b306b1fe06da3b1a99e07c0cf235898010d)
- Fixed the problem of incorrect use of supported_groups that is only applicable to TLSv1.3 in TLSv1.2, and added a check for group version compatibility. (Architecture-related: TLS version compatibility)
  ↳ No PR: [e609a45](https://github.com/openssl/openssl/commit/e609a4565f9ededc5c982175c297bb08058f767c)
- Fixed the problem of CONF_modules_load_file_ex function trying to load an empty file name when the default configuration file path is empty, and instead directly returns success without reporting an error. (Architecture-related: public API)
  ↳ No PR: [8b7d5ea](https://github.com/openssl/openssl/commit/8b7d5ea7dd602eb7c2c4bc5ad45489dc5fc711f6)
- Fixed the error in the return value of the ossl_config_int() function in UEFI systems to ensure that the correct value is returned in the UEFI environment. (Architecture-related: platform compatibility)
  ↳ No PR: [500e479](https://github.com/openssl/openssl/commit/500e479db1beae5fa5691d40b866329d2fdc62e7)
- Automatically disable tick suppression in QUIC blocking operations to avoid indefinite hangs. (Architecture-related: QUIC behavior)
  ↳ No PR: [cae02d2](https://github.com/openssl/openssl/commit/cae02d2b0a650f07d29c9072a159b70035ae6c07)
- Shield most mutable API operations when the QUIC connection is in the shutdown flush phase to prevent unsafe read and write, handshake or stream creation operations during the shutdown process. (Architecture-related: QUIC shutdown behavior)
  ↳ No PR: [6d6b3a0](https://github.com/openssl/openssl/commit/6d6b3a032dfac23207f475b5bfe692e290f83c85)
- Fix LSX detection on LoongArch, use getauxval(AT_HWCAP) instead of cpucfg instruction to check both hardware and kernel support. (Architecture-related: platform compatibility)
  ↳ No PR: [c612289](https://github.com/openssl/openssl/commit/c612289b77c37f7295d5af0d0e6b6c04e6ba727c)
- When the modulus is too large, the DH_check function will not only return the error code, but also set the corresponding error bit in the output parameter to improve the robustness of the caller's error handling. (Architecture-related: public API: DH_check error handling)
  ↳ No PR: [81d10e6](https://github.com/openssl/openssl/commit/81d10e61a4b7d5394d08a718bf7d6bae20e818fc)
- Fixed unreachable and redundant codes in x509 certificate and CRL loading functions, and optimized error handling logic. (Architecture-related: public API)
  ↳ No PR: [ae29622](https://github.com/openssl/openssl/commit/ae29622f39f7deb0599624cc7a771bfc05f1353f)
- Fix the return value regression problem of X509_VERIFY_PARAM_add0_policy and
  ↳ No PR: [e3d897d](https://github.com/openssl/openssl/commit/e3d897d3fa3b48bb835fab0665a435469beea7ae)
- Fixed an issue where SSL_has_pending() may generate an error when called before the connection is established, ensuring that it returns 0. (Architecture-related: public API)
  ↳ No PR: [c31f061](https://github.com/openssl/openssl/commit/c31f06120fa8411da3cd779dfe881325204745ac)
- Fixed the conflict between the error return value in the ossl_cmp_asn1_get_int() function and the OSSL_CMP_CERTREQID_NONE constant, changed the error return value from -1 to -2, and updated the caller ossl_cmp_pkisi_get_status() to correctly handle the change. (Architecture-related: external behavior)
  ↳ No PR: [2c8d9f1](https://github.com/openssl/openssl/commit/2c8d9f19e351a84d4329fbe2f68a4a8a49cad3ef)
- Fixed the problem that the PEM_read_bio_Parameters function should not prompt for a password when reading parameters. It will now fail directly instead of asking for a password. (Architecture-related: public API)
  ↳ No PR: [0d0791e](https://github.com/openssl/openssl/commit/0d0791eedff7f0747503d816184810aa093f523e)
- Fixed an error caused by certificate auxiliary data when creating PKCS#12, giving priority to the friendly name and local key ID passed by the caller. (Architecture-related: public API)
  ↳ No PR: [388a8e7](https://github.com/openssl/openssl/commit/388a8e731445d190a46ec27b2ff5b4bf334d526b)
- Fixed the recursive deadlock problem caused by memory allocation failure in OPENSSL_init_crypto(OPENSSL_INIT_LOAD_CRYPTO_STRINGS), and avoided recursive calls by introducing the temporary storage and recovery mechanism of the error string loading area. (Architecture-related: initialization behavior)
  ↳ No PR: [6b1a127](https://github.com/openssl/openssl/commit/6b1a1275b3f3f8af0b4e0603d529a7bb2da4402a)
- Fixed the backward compatibility issue of OSSL_HTTP_REQ_CTX_set_request_line function, now allows path parameters to start with http:// for proxy scenarios. (Architecture-related: public API behavior)
  ↳ No PR: [45c0218](https://github.com/openssl/openssl/commit/45c02183c65f0e1abf59909c2900764606334664)
- Add checks on i2d_X509_NAME return value in X509_NAME_hash_ex and X509_NAME_hash_old to avoid continuing to use invalid data when encoding fails. (Architecture-related: public API behavior)
  ↳ No PR: [945fde5](https://github.com/openssl/openssl/commit/945fde53a3db5011940a059fd1407b81197c9e14)
- Fix configuration of BIO helper functions in QUIC context: avoid using buffering, and set datagram socket type. (Architecture-related: public API)
  ↳ No PR: [573f16c](https://github.com/openssl/openssl/commit/573f16c99719c9439a66a82fa256662d7cd32d47)
- Added two missing entries of privilegeWithdrawn and aACompromise in the OCSP CRLReason table. (Architecture-related: public API)
  ↳ No PR: [1c8a7f5](https://github.com/openssl/openssl/commit/1c8a7f5091e2c5aebc043be86bcbedc6947e1c6f)
- Fix the retry flag passing of dgram_bio in BIO connection, add TCP Fast Open support, simplify the release logic, and adjust the IPv6 detection macro. (Architecture-related: TCP Fast Open support)
  ↳ No PR: [abeb41b](https://github.com/openssl/openssl/commit/abeb41b42fa3cdca99d3f3fef48ea6ee04023d68)
- Fixed an issue where the assembler reported an error when loongarch_arch.h was included in the assembly file, and protected external variable declarations through conditional compilation. (Architecture-related: platform compatibility)
  ↳ No PR: [84a0b1b](https://github.com/openssl/openssl/commit/84a0b1b169197e3afdadcdafc9fea65361ff672f)
- Fixed OPENSSL_init_crypto loading configuration into the current default library context instead of the initial global default library context during implicit initialization. (Architecture-related: public API)
  ↳ No PR: [ecb6cdf](https://github.com/openssl/openssl/commit/ecb6cdf02a302af18fe4bc20097a9ea3177f897c)
- Fixed the regression problem in the OSSL_PARAM_BLD_push_BN_pad() function that does not allow NULL BIGNUM to be passed in, and now supports NULL parameters again. (Architecture-related: public API)
  ↳ No PR: [2ce79d9](https://github.com/openssl/openssl/commit/2ce79d97e338c8eaacf67ce2e1a1b0fb1c639f11)
- Change the HTTP server listening address from IPv6 wildcard to universal wildcard, fix test failure on IPv4-only machines. (Architecture-related: Platform compatibility)
  ↳ No PR: [b0da24b](https://github.com/openssl/openssl/commit/b0da24bd2dc64e3a01df24e01aba37fe4c269230)
- Fix bio_dgram_test failure on NonStop platform, adjust default buffer size. (Architecture-related: Platform compatibility)
  ↳ No PR: [572f290](https://github.com/openssl/openssl/commit/572f290c9c2d892d5f891c6b8dcebf4e1ac65aed)
- Fix the problem that linear search does not work properly in the CHARSET_EBCDIC environment, and improve the error handling and locking mechanism in OBJ_create. (Architecture-related: platform compatibility)
  ↳ No PR: [a47fc4e](https://github.com/openssl/openssl/commit/a47fc4ed401da4e2d84e035cc4add566e85b03d0)
- Added an error code for invalid attribute query for the random number module. (Architecture-related: public API)
  ↳ No PR: [a9483b8](https://github.com/openssl/openssl/commit/a9483b8aa00753a2a9665273c0e376f3c1d36e65)
- Remove the initialization of FFC parameters in the init method of DH and DSA to maintain behavior consistent with version 1.1.1 and support methods of intercepting existing keys. (Architecture-related: external behavior)
  ↳ No PR: [706512e](https://github.com/openssl/openssl/commit/706512ecbc31585d447b53c3aa89acdf6951f996)
- Modify the semantics of the FFC public key verification function so that it no longer returns failure when encountering a non-fatal error, but sets an error code and returns success, thereby preventing DH_check_pub_key from failing due to non-fatal problems. (Architecture-related: external behavior)
  ↳ No PR: [eaee176](https://github.com/openssl/openssl/commit/eaee1765a49c6a8ba728e3e2d18bb67bff8aaa55)
- Fixed CVE-2023-5363: The key length and IV length parameters are processed in advance when the EVP cipher is initialized, to avoid security issues in the AEAD cipher where the IV is truncated or uses uninitialized bytes due to parameter processing too late. (Architecture-related: public API)
  ↳ No PR: [f3a7e6c](https://github.com/openssl/openssl/commit/f3a7e6c057b5054aa05710f3d528b92e3e885268), [a2fe10c](https://github.com/openssl/openssl/commit/a2fe10ca39f9a8e251b98bc03c3b1bbb6ad1496f)
- Fixed the problem of ssl.h compilation failure due to using gets as the parameter name in the MingW environment. Change the parameter name in the BIO_meth_set_gets function prototype to ossl_gets. (Architecture-related: platform compatibility)
  ↳ No PR: [2e471a7](https://github.com/openssl/openssl/commit/2e471a740b621481b3f3236f82fdd677414900a1)
- Fix missing error reporting call in CMS_add1_signer, and correct algorithm OID check. (Architecture-related: public API)
  ↳ No PR: [72a99ef](https://github.com/openssl/openssl/commit/72a99ef665b26fa207c0eee6e7e4842d1e42752c), [bd16091](https://github.com/openssl/openssl/commit/bd160912dcc5e39bcdc925d9aa6538f20e37ad16)
- Add a length check for excessively large Q parameters in the DH key calculation and generation function, and unify the behavior of DH_check_pub_key. (Architecture-related: public API)
  ↳ No PR: [d73028b](https://github.com/openssl/openssl/commit/d73028b75b416ccabdc267553dcce241e831eaf3)
- Fixed an issue where EVP_PKEY_get_bits, EVP_PKEY_get_security_bits and EVP_PKEY_get_size functions did not add error entries to the error queue when they failed. (Architecture-related: public API)
  ↳ No PR: [51f4115](https://github.com/openssl/openssl/commit/51f4115dcc818a35e2c8838c01b3b08740d0c1e1)
- Repair the drainage calculation logic in QUIC transmission and use more accurate send buffer judgment conditions. (Architecture-related: QUIC transmission behavior)
  ↳ No PR: [18a431b](https://github.com/openssl/openssl/commit/18a431b6f17204ed2790f5a4fec265ffa5ca061d)
- Fixed the socket non-blocking mode setting issue on the Nonstop platform, using fcntl(F_GETFL) instead of FIONBIO; also fixed the error handling when host or port in BIO_accept is NULL. (Architecture-related: platform compatibility)
  ↳ No PR: [0ef3e13](https://github.com/openssl/openssl/commit/0ef3e1305db3f77bb0b0702c9b45bb39d165f28a)
- Fix the ASN1_TIME object memory leak that may be caused when PKCS7_add_signed_attribute fails in PKCS7_add0_attrib_signing_time. (Architecture-related: public API)
  ↳ No PR: [1ad7f4b](https://github.com/openssl/openssl/commit/1ad7f4bf979fcb5fb50013b0c9106e26c6ed2fac)
- Fix a possible memory leak in PKCS7_add_attrib_smimecap when PKCS7_add_signed_attribute fails. (Architecture-related: public API)
  ↳ No PR: [f06d408](https://github.com/openssl/openssl/commit/f06d4082394d4fd6d9ba96a441bbb1c6ef524020)
- Fixed a memory leak in CMS_sign_receipt caused by the incorrect path not releasing the ASN1_OCTET_STRING object. (Architecture-related: public API)
  ↳ No PR: [757d649](https://github.com/openssl/openssl/commit/757d6491ebebc541f54c0aa8043b8e5b31a58a7e)
- Change the scope of the no_legacy_server_connect option from server to client. (Architecture-related: external behavior)
  ↳ No PR: [d1b3b67](https://github.com/openssl/openssl/commit/d1b3b6741380a1d7607da671b97f3fe5f54fa657)
- The ARMV7_TICK feature is no longer automatically detected, it is only used when the user explicitly enables it via OPENSSL_armcap. (Architecture-related: platform compatibility)
  ↳ No PR: [f2ec24c](https://github.com/openssl/openssl/commit/f2ec24c9e7c3df55fba97336594a5e815c342b01)
- Added a new auxiliary function to simplify the use of EVP_PKEY_decrypt, and clean up unnecessary calls in obtaining CRMF encrypted values. (Architecture-related: public API)
  ↳ No PR: [36b91a1](https://github.com/openssl/openssl/commit/36b91a198ae027c054ef128a35a268bc3c307f00)
- Fixed the infinite loop problem that BN_mod_sqrt() may cause when it is a non-prime number p (CVE-2022-0778). (Architecture-related: public API)
  ↳ No PR: [9eafb53](https://github.com/openssl/openssl/commit/9eafb53614bf65797db25f467946e735e1b43dc9)
- Added output buffer size check in EVP_MAC_final. (Architecture-related: public API)
  ↳ No PR: [b97f4dd](https://github.com/openssl/openssl/commit/b97f4dd73b4711eebf731ae0efa6e9b77c7f3304)
- Added missing checks for SM2 signature generation to ensure standard compliance. (Architecture-related: SM2 signature compliance)
  ↳ No PR: [e81c81c](https://github.com/openssl/openssl/commit/e81c81c9af8a5d22658110d2dc753582eb87a58e)
- Modified the DES_set_key function so that it always sets the key schedule and returns the verification result. (Architecture-related: DES_set_key behavior)
  ↳ No PR: [6450ea2](https://github.com/openssl/openssl/commit/6450ea27ffdc22194f27e90796ce5538af2d81e2)
- Fixed carry overflow error in bn_sqr_comba4/8 on MIPS 32-bit. (Architecture-related: Platform compatibility: MIPS 32-bit)
  ↳ No PR: [336923c](https://github.com/openssl/openssl/commit/336923c0c8d705cb8af5216b29a205662db0d590)
- Fixed the problem of point objects not being released when memory allocation fails in the EC_POINT_hex2point function. (Architecture-related: public API: EC_POINT_hex2point memory repair)
  ↳ No PR: [dd2fcc1](https://github.com/openssl/openssl/commit/dd2fcc1f7c44c5fb5aa2d33aecdc699c7018ce01)
- Fixed the resource cleanup problem in error handling to avoid calling OSSL_LIB_CTX_free on an incompletely initialized context. (Architecture-related: public API: OSSL_LIB_CTX_free usage fix)
  ↳ No PR: [7ca3bf7](https://github.com/openssl/openssl/commit/7ca3bf792a4a085e6f2426ad51a41fca4d0b1b8c)
- Added verification of the incoming category parameter to OSSL_trace_end(), and returns it directly if it is invalid. (Architecture-related: public API)
  ↳ No PR: [ee8a61e](https://github.com/openssl/openssl/commit/ee8a61e158c42c327c3303101083422b9a7cc504)
- Fixed code to detect aarch64 capabilities when getauxval() is missing. (Architecture-related: Platform compatibility)
  ↳ No PR: [f97ddfc](https://github.com/openssl/openssl/commit/f97ddfc3059ff568919e92597b2691d5366fd34b)
- Change the error reason when disabling the old signature algorithm to a more specific error message. (Architecture-related: public API)
  ↳ No PR: [97b8db1](https://github.com/openssl/openssl/commit/97b8db1af2f71059ecea986e4d12fc6a23699a74)
- Fixed the problem that the lock is not initialized when calling OBJ_new_nid externally. (Architecture-related: public API)
  ↳ No PR: [cd920f8](https://github.com/openssl/openssl/commit/cd920f8fa1bb603a620bea697027f5573fadc12e)
- Moved the maximum fragment length check from the SSL object to the record layer. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [ffbd6e6](https://github.com/openssl/openssl/commit/ffbd6e67874475e025e942e0ee9f51badfea42b5)
- Migrate the encryption code, record type processing, buffer allocation and other logic of each version of TLS/SSL from the general module to the record layer methods specific to each protocol, remove the DTLS special processing, and reconstruct the record layer write path. (Architecture event: Record layer method reconstruction)
  ↳ No PR: [9251c3c](https://github.com/openssl/openssl/commit/9251c3c4c7695b6268fcd122e18643d61f02b5dd), [a857267](https://github.com/openssl/openssl/commit/a8572674f12ceb39f7e66ccbaa8918b922c76739), [2c50d7f](https://github.com/openssl/openssl/commit/2c50d7fb06e34c5ab562bf890c49cc00cbd52a56), [bfda3ae](https://github.com/openssl/openssl/commit/bfda3aeec5986d9374e1ceb33b823a2d82bd29ca), [91fe8ff](https://github.com/openssl/openssl/commit/91fe8ff02a323eddb0404f975d5c9a03c024593b), [7ca61d6](https://github.com/openssl/openssl/commit/7ca61d63e99726ef7874b88b96892dae75f51156), [aca70ca](https://github.com/openssl/openssl/commit/aca70ca81c6fcf38554aa95a3a2c75e1eeb1a085)
- The discard_enc_level implementation of QUIC TXP no longer automatically notifies QTX to discard the encryption level, the caller needs to handle it by itself. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [df03868](https://github.com/openssl/openssl/commit/df038685644eb1bc4618f678b52fc22f0101235f)
- Optimize the receiving processing logic of QUIC channel: only reprocess the receiving queue after receiving a new receiving end key. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [92282a1](https://github.com/openssl/openssl/commit/92282a17c9959bc61e012e93517320df1ec8ace8)
- Connect the SSL_CTX control function and callback control function in the QUIC front-end I/O API to the standard SSL implementation, and remove the no longer needed ossl_quic_conn_from_ssl function. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [8a1a6d6](https://github.com/openssl/openssl/commit/8a1a6d6d9e9a6bc091f0dc21503da214e2614209)
- Rename the want_net_read and want_net_write fields in the QUIC internal API, add protocol error handling logic, and improve transmission parameter handling. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [b639475](https://github.com/openssl/openssl/commit/b639475a9433c827675b8154ea9e0ce361403c76)
- Reconstruct QUIC's SSL option setting mechanism: add ossl_quic_set_options, ossl_quic_clear_options and ossl_quic_get_options functions, and limit QUIC connections to only allow some options. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f0d9757](https://github.com/openssl/openssl/commit/f0d9757cafef98a346088b9f7fa988964e301c67), [18ca1c8](https://github.com/openssl/openssl/commit/18ca1c8fc074e5b0fe52c91c52ade23e1f14cd0e)
- Optimize QUIC channel lock management: move mutex locks out of the connection structure to support flexible initialization and destruction, and support releasing and reacquiring mutex locks during polling wait. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [4847599](https://github.com/openssl/openssl/commit/4847599b54ca3fffe0da21cdccaefd74015d9d67), [c019e1e](https://github.com/openssl/openssl/commit/c019e1efe9b5dbb43c52f516e76b3f535158aaae)
- Refactor the QUIC API: change the get_record() data field to const, change the front-end API parameter from QUIC_CONNECTION to SSL, introduce the QUIC_XSO type to replace QUIC_STREAM, and rename SSL_tick and SSL_get_tick_timeout to SSL_handle_events and SSL_get_event_timeout respectively. (Architecture events: SSL_Protocol_Engine module changes)
  ↳ No PR: [2eb91b0](https://github.com/openssl/openssl/commit/2eb91b0ec325924ae4b7dc596617a6fff71d7ae6), [072328d](https://github.com/openssl/openssl/commit/072328dddb8371b865bd18caca9a77698e883c80), [f8636c7](https://github.com/openssl/openssl/commit/f8636c7e85229bf780da7cf61c234695952f8cad), [6084e04](https://github.com/openssl/openssl/commit/6084e04b25378a4590798a034633e90791cf74a3), [cb5c208](https://github.com/openssl/openssl/commit/cb5c208bf2e39bf2367b051136c599cff1fc3683), [a35e38a](https://github.com/openssl/openssl/commit/a35e38a2128163209db76eb9135e29b1bbe54c9e), [a1660c9](https://github.com/openssl/openssl/commit/a1660c9422c8fef9e7c74d1dedd249106d4be18b)
- Enhanced QUIC functionality: Forward unknown control commands to underlying SSL; Termination reason function returns constant pointer and adds status check; Congestion control option interface migrates to OSSL_PARAM; Reconstructs error promotion mechanism to support per-stream error handling. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [f8ffab0](https://github.com/openssl/openssl/commit/f8ffab0d52fc5e37d92c99e4463d76174e869930), [723cbe8](https://github.com/openssl/openssl/commit/723cbe8a73fe3644bb4d8f20d475e57f44955b54), [878df9b](https://github.com/openssl/openssl/commit/878df9be67df14c90ef584e5762a8c1f5c8f9749), [faa3a18](https://github.com/openssl/openssl/commit/faa3a180efcf17c8fc7db354367d2b03d89f3042), [b864110](https://github.com/openssl/openssl/commit/b864110a82096c6b824406a3f8686a5099ea17c4)
- Rename the API and fields related to the incoming stream denial policy, and remove SSL_attach_stream and SSL_detach_stream from the public API and change them to internal functions. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [83df44a](https://github.com/openssl/openssl/commit/83df44ae53c3c3bb1e79785af38ab52bb4f865cb), [de52162](https://github.com/openssl/openssl/commit/de521629c1f296a6eb50a84ab2d2b200fc766bc6)
- Reconstruct QUIC flow state management: define flow status based on RFC, add status query function, remove recv_fin_retired field and use state machine instead. (Architecture event: QUIC protocol integration)
  ↳ No PR: [2f018d1](https://github.com/openssl/openssl/commit/2f018d14f06d54c9528ac41d40e95d7638371e50), [5ed3a43](https://github.com/openssl/openssl/commit/5ed3a435d5f84e296330595985c7adb2575ecba5)
- NewReno The wake-up deadline of congestion control is changed to immediate, without waiting. (Architecture event: QUIC protocol integration)
  ↳ No PR: [b49d9de](https://github.com/openssl/openssl/commit/b49d9de0e66a5fe7570652186e3bb8c4a4d9f556)
- Reconstruct QUIC TLS error handling: Add raise_error function to uniformly record handshake layer errors and save error status, adjust ossl_quic_tls_get_error interface to return error status object. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [7a2bb21](https://github.com/openssl/openssl/commit/7a2bb2101be4f4dfd9f437ebe1d7fd5dbc14b894)
- Reconstruct DTLS record writing logic: Create new functions and migrate to record layer method interface. (Architecture event: Record layer method reconstruction)
  ↳ No PR: [88bf978](https://github.com/openssl/openssl/commit/88bf978eb1766bec720c198deabe8d0a5de157bb), [fc938db](https://github.com/openssl/openssl/commit/fc938db6cc46c6b59ab9da39f3c5b9c9a97ad33a), [bf04cbf](https://github.com/openssl/openssl/commit/bf04cbfafe77ddc67f1a9c06ffb044f9bf44057c), [602ee1f](https://github.com/openssl/openssl/commit/602ee1f672a41f984e8923ad7430ca51ca42abde)
- Update SSL error code definition: Renumber stream-related error codes and add error description strings. (Architecture-related: public API: Error code definition)
  ↳ No PR: [bac3f4d](https://github.com/openssl/openssl/commit/bac3f4da5579887d6e203020e83298676cc982ba)
- Migrate the load_csr_autofmt function to a shared library and update the call, adding verification option parameters. (Architecture-related: public API: load_csr_autofmt migration)
  ↳ No PR: [200d844](https://github.com/openssl/openssl/commit/200d844782956b4c6db9bdd92a53113d9c2dc3c7)
- Rename OSSL_CMP_CTX_get0_trustedStore to OSSL_CMP_CTX_get0_trusted, and update related test cases. (Architecture-related: public API: function rename)
  ↳ No PR: [6be83cc](https://github.com/openssl/openssl/commit/6be83cc655af819be0e3f2701c726a2550357953)
- Modify X509_http_nbio and X509_CRL_http_nbio macro definitions to avoid including ocsp.h, and adjust header file dependencies. (Architecture-related: public API: header file dependency adjustments)
  ↳ No PR: [f593f32](https://github.com/openssl/openssl/commit/f593f32eede30ead69e0a16e47a564a664171283)
- Change the parameter types of settings and options in recordmethod.h to const. (architecture-related: public API)
  ↳ No PR: [0c974fc](https://github.com/openssl/openssl/commit/0c974fc754e4b0525819ca9f6c3e124141b690ad)
- Removed ossl_namemap_add_name_n API to simplify internal implementation. (Architecture-related: public API removed)
  ↳ No PR: [b00cf0e](https://github.com/openssl/openssl/commit/b00cf0e790661636e1df1026554f712cc513592d)
- Refactor the ASN1_item_pack function: use ASN1_STRING_set0 instead of manual memory management, and correct error codes and length checks. (Architecture-related: public API behavior changes)
  ↳ No PR: [3384750](https://github.com/openssl/openssl/commit/33847508d5605d8dbe868d7694a4eff79d785404)
- Extract GCM function pointers into independent structures, and add dedicated functions to initialize these function pointers. (Architecture-related: public API structure changes)
  ↳ No PR: [92c9086](https://github.com/openssl/openssl/commit/92c9086e5c2b63606cd28a7f13f09b9ff35a0de3)
- Clean and refactor the implementation of X509_check_private_key and X509_REQ_check_private_key, and mark the parameters of X509_REQ_get0_pubkey and X509_REQ_check_private_key as const. (architecture-related: public API)
  ↳ No PR: [aaabe58](https://github.com/openssl/openssl/commit/aaabe58072924c24c862a0660cdfe78de63099c2)
- Remove the const qualifier of the second parameter of the PKCS12_SAFEBAG_set0_attrs function. (Architecture-related: public API)
  ↳ No PR: [9eaf07f](https://github.com/openssl/openssl/commit/9eaf07ffe39e76aca2dfb8e22b8060c75fcbd8e0)
- Rename record layer types SSL3_BUFFER and SSL3_RECORD to TLS_BUFFER and TLS_RL_RECORD respectively. (Architecture-related: Record layer type rename)
  ↳ No PR: [e9189cc](https://github.com/openssl/openssl/commit/e9189cc4af045523f91b2d9265add1ab1326fcdf), [22094d1](https://github.com/openssl/openssl/commit/22094d11a780f7485f0929ccfac806e0d02f82a9), [1704961](https://github.com/openssl/openssl/commit/1704961cf085a64b0e104bd0c9cb81188f061698)
- Simplify the custom interface of QUIC BIO polling descriptor: change the custom field from an array to a single pointer. (Architecture-related: public API)
  ↳ No PR: [692df8d](https://github.com/openssl/openssl/commit/692df8d34401c95ee446e26033711030e471e7e7)
- Rename the QUIC probe request API function name from ossl_ackm_get_probe_request to ossl_ackm_get0_probe_request, and remove the to-do annotation in the document. (Architecture-related: public API)
  ↳ No PR: [2477e99](https://github.com/openssl/openssl/commit/2477e99f1055194902dc4864124316ea57ac3efa)
- Refactor the aarch64 feature detection code, remove the SIGILL-based detection method, use more reliable methods such as getauxval and sysctl, and fix the HWCAP macro redefinition warning on FreeBSD. (Architecture-related: platform compatibility)
  ↳ No PR: [52a3814](https://github.com/openssl/openssl/commit/52a38144b019cfda6b0e5eaa0aca88ae11661a26)
- Rename OSSL_CMP_get_caCerts to OSSL_CMP_get1_caCerts, and improve OSSL_CMP_exec_certreq documentation. (Architecture-related: public API)
  ↳ No PR: [ec5a9cd](https://github.com/openssl/openssl/commit/ec5a9cd11b92e75f097dbaa41c512f29cf8625e7)
- Partially rolled back support for Windows CA certificate storage and restored the original certificate directory search logic. (Architecture-related: platform compatibility)
  ↳ No PR: [dfdbc11](https://github.com/openssl/openssl/commit/dfdbc113eefb80712fefc3187367fe6050610da5)
- Change BIO's reference counting from lock-based atomic operations to structure-based atomic operations. (Architecture-related: public API)
  ↳ No PR: [a22d196](https://github.com/openssl/openssl/commit/a22d1966bb230c335602ff79ca3356137d16b3e6)
- Migrate the reference counting of ECX keys from lock-based atomic operations to structure-based atomic operations. (Architecture-related: public API)
  ↳ No PR: [99b7bea](https://github.com/openssl/openssl/commit/99b7beafd212144fc3c77a6c09fc48f06f245c29)
- Update the reference count and lock release in SSL_SESSION_free to be atomic operations, and add the release of peer_rpk. (Architecture-related: public API)
  ↳ No PR: [43a07d6](https://github.com/openssl/openssl/commit/43a07d6dd44cc9594a6cfecc464b69a7c4142d5f)
- Update the reference counting implementation of encoders and decoders to structure-based atomic operations. (Architecture-related: public API)
  ↳ No PR: [7d6ab12](https://github.com/openssl/openssl/commit/7d6ab1210603c23a4f2cbfb5c542726afe3b08cc)
- Update X509_STORE_free to use structure-based atomic operations. (Architecture-related: public API)
  ↳ No PR: [a903a13](https://github.com/openssl/openssl/commit/a903a132a4256d34f20cb2f7636247b41fd85965)
- Migrate the reference counting mechanism of various objects in the EVP module from atomic operations based on independent locks to atomic reference counting based on internal structures. (Architecture-related: public API)
  ↳ No PR: [6be83ac](https://github.com/openssl/openssl/commit/6be83ac172aac93b49ae0b847fd5ac9de6ab3ff5)
- Remove unused QUIC server method declarations and implementations, and clean up related test code. (Architecture-related: public API)
  ↳ No PR: [3f7b67f](https://github.com/openssl/openssl/commit/3f7b67fb21e31b4262bb0c0dd83c01c221f3278c)
- Change the BIO_CONNECT_free function to static, and clean up the error handling of memory allocation. (Architecture-related: public API)
  ↳ No PR: [ed28cb8](https://github.com/openssl/openssl/commit/ed28cb8140f1de81eca0f90b169af2b783abfe16)
- Renamed QUIC function SSL_set_initial_peer_addr to SSL_set1_initial_peer_addr. (architecture-related: public API)
  ↳ No PR: [ce7a9e2](https://github.com/openssl/openssl/commit/ce7a9e23fb1ea249e08c3dfa9c9f701a701f2719)
- Change the rectype parameter type of the write_record function from int to uint8_t to unify TLS record type representation. (Architecture-related: public API)
  ↳ No PR: [eb1eaa9](https://github.com/openssl/openssl/commit/eb1eaa9af4c241baea00cb16557f41811ed9e097)
- Revised the QUIC connection close information API, merging the is_local and is_transport fields in SSL_get_conn_close_info into the flags field. (Architecture-related: public API)
  ↳ No PR: [7d9e447](https://github.com/openssl/openssl/commit/7d9e447ab812df34bba581c5918721cc704fdacb)
- Advance the deprecated version of lh_stats related functions from OpenSSL 3.2 to 3.1, and correct the relevant deprecated macro definitions. (Architecture-related: public API compatibility)
  ↳ No PR: [6a92159](https://github.com/openssl/openssl/commit/6a92159d01116495e5e642e55fe0f6e4c821696e), [6f66602](https://github.com/openssl/openssl/commit/6f66602eaa0a034847e9b1347c108b82c60b41d7)
- Added internal hardening checks for HPKE implementation, including stricter parameter validation and more accurate error reporting. (Architecture-related: public API behavior)
  ↳ No PR: [2a4f8da](https://github.com/openssl/openssl/commit/2a4f8da45c73cff771ae45de46ef73095a6ca29e)
- Migrate string comparison related functions from ctype.c to o_str.c to avoid repeated implementation in legacy.so. (Architecture-related: Internal reconstruction: Function migration)
  ↳ No PR: [71c17c3](https://github.com/openssl/openssl/commit/71c17c36d913a82742c7d4ecd91ad047906cdae0)
- Update the tls13encryptiontest test to adapt to the new record layer structure and use the OSSL_RECORD_LAYER API instead. (Architecture event: Record layer API reconstruction)
  ↳ No PR: [a16f9d3](https://github.com/openssl/openssl/commit/a16f9d3366a4b4e8c8014bbf39b86baaf1a04047)
- Fixed the problem of SSL_trace() in QUIC API test on big-endian platform, changing the type field of record template structure to unsigned character type. (Architecture-related: platform compatibility)
  ↳ No PR: [b6bf1cb](https://github.com/openssl/openssl/commit/b6bf1cbf1d48bd02f3fae2fb0bf922100efd0be5)
- Add multi-stream support to QUIC test server, add tick, connection status and termination status query functions, and modify the read and write interface to support specified stream ID. (Architecture-related: Internal API: QUIC test server)
  ↳ No PR: [b757beb](https://github.com/openssl/openssl/commit/b757beb5f326ce4a7da021d0f4c52e03e37e1945), [97f30fd](https://github.com/openssl/openssl/commit/97f30fd5d84d3409a4720226f61e94b6442fb3c9), [274bb48](https://github.com/openssl/openssl/commit/274bb489cb800552cdf6d15ef5e7481551c14544), [a350db7](https://github.com/openssl/openssl/commit/a350db7318cba3566014ac02a5caa5f4884f00ba), [0554f72](https://github.com/openssl/openssl/commit/0554f723c1b13f66e56d892b332ccd36aee498ad), [fca44cf](https://github.com/openssl/openssl/commit/fca44cfc1c930afab94fac08ad5a3a303f1724fe), [4f2d32d](https://github.com/openssl/openssl/commit/4f2d32d6b6b4b80ff5f55c5462b545516d252d11), [7ba8f79](https://github.com/openssl/openssl/commit/7ba8f79a0ff5f085c9f1b4471496180c052360f5), [0345cac](https://github.com/openssl/openssl/commit/0345cac6d29da328739e8b06b02260b63d4a91e9)
- Add internal API for white-box testing key updates for QUIC, including setting TXKU threshold coverage, getting send and receive key epochs, and fixing idle timeout calculations and retry token handling. (Architecture-related: Internal API: QUIC key update testing)
  ↳ No PR: [16f3b54](https://github.com/openssl/openssl/commit/16f3b542f89dbdd6029400c740a55d49d4af8e53)
- Added a lock alternative path for platforms that do not support tsan in the threadstest test, and added a write lock check. (Architecture-related: platform compatibility)
  ↳ No PR: [3d4d530](https://github.com/openssl/openssl/commit/3d4d5305c292f5db62b4abf732f6682b2ada6f44), [1fc9780](https://github.com/openssl/openssl/commit/1fc97807d3a3b5e3065a7df80d1ad3601ccc5e2f)
- Allow qtestlib to use simulation time implementation, and modify test cases to use this feature, removing sleep calls that may fail. (Architecture-related: Test framework changes: Simulation time)
  ↳ No PR: [f9fcc7c](https://github.com/openssl/openssl/commit/f9fcc7c727f0589fcd1f28ef09c8e10deee4f229)
- Optimize the modulo exponential operation function, remove unused variables, adjust the initialization order, add parameter alias checking, and expand the acceleration path to support more modulus sizes. (Architecture-related: public API)
  ↳ No PR: [f9a4e2b](https://github.com/openssl/openssl/commit/f9a4e2b663ab97de718e016b29644d0c2bd9b7c3)
- Optimize dual 1536/2048-bit modular exponentiation operation for Intel IceLake CPU, adopt AVX512_IFMA256 ISA, and extend related functions to support multiple modulus bit widths. (Architecture-related: platform compatibility)
  ↳ No PR: [f87b4c4](https://github.com/openssl/openssl/commit/f87b4c4ea67393c9269663ed40a7ea3463cc59d3)
- Add runtime feature detection for ARM platforms to enable EOR3 instructions and loop unrolling optimizations to improve AES-GCM performance. (Architecture-related: Platform compatibility)
  ↳ No PR: [954f45b](https://github.com/openssl/openssl/commit/954f45ba4c504570206ff5bed811e512cf92dc8e)
- Enable vectorized AES-GCM implementation based on AVX512 vAES and vPCLMULQDQ instructions, and update structure member order annotations to match new assembly module dependencies. (Architecture-related: Platform compatibility)
  ↳ No PR: [63b996e](https://github.com/openssl/openssl/commit/63b996e752ac698186c38177232280e6515d571b)
- Optimize ChaCha20 performance for ppc64le architecture, add support for POWER10 processor, and achieve about 50% performance improvement through 8-way parallel processing. (Architecture-related: platform compatibility)
  ↳ No PR: [f596bbe](https://github.com/openssl/openssl/commit/f596bbe4da779b56eea34d96168b557d78e1149a)
- Add RISC-V hardware acceleration support to the SHA512 algorithm, and introduce macro definitions based on RISC-V extension instructions through conditional compilation. (Architecture-related: platform compatibility)
  ↳ No PR: [611685a](https://github.com/openssl/openssl/commit/611685adc04a7c7e9612d51e743044fdcd9d1846)
- Add MD5 assembly implementation for aarch64 architecture, enable it by modifying the conditional compilation macro, significantly improve performance. (Architecture-related: Platform compatibility: aarch64 MD5 assembly)
  ↳ No PR: [04904a0](https://github.com/openssl/openssl/commit/04904a0fff639c058d38b355d75485ca5dde0a89)
- Use SM3 hardware instructions to accelerate the SM3 algorithm on the aarch64 platform, and automatically detect hardware support. Unsupported platforms still use the original C implementation. (Architecture-related: Platform compatibility: aarch64 SM3 hardware acceleration)
  ↳ No PR: [71396cd](https://github.com/openssl/openssl/commit/71396cd048072b69559b46d98cfebfd4474cd712)
- Add clmul instruction-based GCM multiplication acceleration for RISC-V 64-bit architecture, support implementation selection through runtime detection of Zbb and Zbc extensions, and retain the C language fallback implementation. (Architecture-related: Platform compatibility: RISC-V GCM multiplication acceleration)
  ↳ No PR: [999376d](https://github.com/openssl/openssl/commit/999376dcf33986c468361ede16fa9de409dc4e2e)
- Add support for SVE extension on aarch64, and use SVE instructions to accelerate ChaCha20 encryption, improving performance by up to 20%. (Architecture-related: Platform compatibility: aarch64 SVE ChaCha20 acceleration)
  ↳ No PR: [b1b2146](https://github.com/openssl/openssl/commit/b1b2146ded9ce5a84c62f30c6c4a922b449f6c90)
- Optimize the EVP_MD_CTX_copy_ex function to reduce frequent writes to the EVP_MD object reference count and alleviate cache competition issues when multi-threads are used frequently. (Architecture-related: public API)
  ↳ No PR: [c0b7dac](https://github.com/openssl/openssl/commit/c0b7dac66edde45b8da80918f5b5b62d1e766a0c)
- Add assembly implementation based on RISC-V Zksh extension for SM3 algorithm, supporting both RV32 and RV64 architecture. (Architecture-related: RISC-V support)
  ↳ No PR: [7ae2bc9](https://github.com/openssl/openssl/commit/7ae2bc9df6e0916a8f16183f07dfa1815dd4b66d)
- Add ROTATE inline assembly support for SM3, and move ROTATE inline assembly to header files to simultaneously optimize SM3, SHA and other hash functions. (Architecture-related: core header file changes)
  ↳ No PR: [eea820f](https://github.com/openssl/openssl/commit/eea820f3e239a4c11d618741fd5d00a6bc877347)
- Enable AES-GCM loop unrolling and EOR3 optimization for Neoverse N2 processor to improve performance. (Architecture-related: Platform compatibility: Neoverse N2)
  ↳ No PR: [9224a40](https://github.com/openssl/openssl/commit/9224a407f9bb4c2af087ecf6e691c9027b594ec0)
- Optimize the implementation of tolower and related character judgment functions, use direct ASCII range comparison instead of table lookup to avoid memory access to improve performance; at the same time, change some macro definitions to function declarations and adjust the interface signature. (Architecture-related: public API: interface signature adjustment)
  ↳ No PR: [286053f](https://github.com/openssl/openssl/commit/286053fc8f78e34828a576830ef879c021640aee)
- Reintroduced fixed-length (n=6) PPC Montgomery multiplication optimization, and added support for Power10 MADD300 instructions. (Architecture-related: Platform compatibility: Power10)
  ↳ No PR: [eae7010](https://github.com/openssl/openssl/commit/eae70100fadbc94f18ba7a729bf065cb524a9fc9)
- Add AES's VPAES vector extension optimization to LoongArch64 architecture, and define corresponding capability detection macros. (Architecture-related: platform compatibility)
  ↳ No PR: [ef91754](https://github.com/openssl/openssl/commit/ef917549f5867d269d359155ff67b8ccb5e66a76)
- Add SM4 optimization support to the Kunpeng-920 platform, enabling related acceleration by identifying HiSilicon CPU models. (Architecture-related: platform compatibility)
  ↳ No PR: [88c53cf](https://github.com/openssl/openssl/commit/88c53cf17d21b06b05043af49af3498665357a6f)
- Optimize the performance of FIPS RSA key generation, use modular inversion operation to replace the greatest common divisor test, and add the BN_are_coprime function; at the same time, adjust the number of Miller-Rabin prime number test rounds to the value specified by FIPS 186-5, replacing the original fixed 64 rounds. (Architecture-related: public API)
  ↳ No PR: [dd1d7bc](https://github.com/openssl/openssl/commit/dd1d7bcb69994d81662e709b0ad838880b943870), [d2f6e66](https://github.com/openssl/openssl/commit/d2f6e66d2837bff1f5f7636bb2118e3a45c9df61)
- Optimize GCM mode performance for the RISC-V platform, choose different implementations according to the extensions supported by the runtime (Zbc, Zbkb, Zbb), use the clmul instruction and reduce register usage; at the same time, integrate GHASH hardware acceleration to enable the GCM mode to obtain complete hardware acceleration capabilities on RISC-V. (Architecture-related: platform compatibility)
  ↳ No PR: [b246843](https://github.com/openssl/openssl/commit/b24684369b76df8b226fe9aa95fca2bccfc6a175), [f3fed0d](https://github.com/openssl/openssl/commit/f3fed0d5fc11a3406951884b9739a93639697a56)
- On PowerPC64LE platforms, enable assembly implementations of felem_square and felem_mul when Altivec and ISA 3.0 (Power 9 and above) support is detected. (Architecture-related: Platform compatibility)
  ↳ No PR: [966047e](https://github.com/openssl/openssl/commit/966047ee13188e8634af25af348940acceb9316d)
- Enabled additional optimizations for GHASH, RAND and AES for Arm64 platforms on Windows. (Architecture-related: Windows Arm64 optimizations)
  ↳ No PR: [636ee1d](https://github.com/openssl/openssl/commit/636ee1d0b864f29a70573a4894958958e940c01e)
- Added a new doubly linked list type that does not require dynamic memory allocation and is used for internal data structures. (Architecture-related: internal data structures)
  ↳ No PR: [f5eac25](https://github.com/openssl/openssl/commit/f5eac259a03c68c96c77f9b998b1b9c16a8439e7)
- Added hardware offload support for modular exponentiation and CRT operations to the S390x platform, and implemented optimized RSA and DH algorithms. (Architecture-related: Platform compatibility: S390x hardware offload support)
  ↳ No PR: [79040cf](https://github.com/openssl/openssl/commit/79040cf29e011c21789563d74da626b7465a0540)
- Enabled AES optimization for Apple M2 system, performance increased by 16-38%. (Architecture-related: Platform compatibility: Apple M2 AES optimization)
  ↳ No PR: [d79bb53](https://github.com/openssl/openssl/commit/d79bb5316e1318bd776d6b2d6723a36778e07f9d)
- Enable unroll8+eor3 optimization of AES-GCM for Neoverse V2 processor. (Architecture-related: Platform compatibility: Neoverse V2 AES-GCM optimization)
  ↳ No PR: [513e103](https://github.com/openssl/openssl/commit/513e103f14e8473fb6810aa216ab3fb7b724ca5d)
- Add MSVC built-in support for RSA multiplication, using __umulh on non-x64 platforms. (Architecture-related: Platform compatibility: MSVC built-in support)
  ↳ No PR: [075652f](https://github.com/openssl/openssl/commit/075652f224479dad2e64b92e791b296177af8705)
- Replace pointer bit operations with ternary conditional operators to eliminate implementation-defined behavior and improve performance. (Architecture-related: Platform compatibility)
  ↳ No PR: [326af4a](https://github.com/openssl/openssl/commit/326af4ad171b849ba1e76fd425d8f337718c4108)
- Change the write lock in RAND_get_rand_method() to a read lock, and fall back to the write lock only when the default random method needs to be set, thereby reducing lock competition. (Architecture-related: RAND API)
  ↳ No PR: [7f2c22c](https://github.com/openssl/openssl/commit/7f2c22c1b9ec46070aa588d7f4a5ad5fe4a60bf4)
- Fixed memory security issues in the EVP module caused by too small buffers or integer overflows, involving signed integer overflows in EVP_EncryptUpdate and EVP_DecryptUpdate. (Architecture-related: EVP interface security fixes)
  ↳ No PR: [43da9a1](https://github.com/openssl/openssl/commit/43da9a14f0e73f42f28ae34219929b44df5d1a11), [1832bb0](https://github.com/openssl/openssl/commit/1832bb0f02e519a48f06a10467c7ce5f7f3feeeb)
- Introduced an implicit rejection mechanism in RSA PKCS#1 v1.5 decryption: when the padding check fails, a random message generated based on the private key and ciphertext is returned to prevent Bleichenbacher side-channel attacks. (Architecture-related: RSA PKCS#1 v1.5 implicit rejection)
  ↳ No PR: [7fc67e0](https://github.com/openssl/openssl/commit/7fc67e0a33102aa47bbaa56533eeecb98c0450f7), [8ae4f0e](https://github.com/openssl/openssl/commit/8ae4f0e68ebb7435be494b58676827ae91695371), [ddecbef](https://github.com/openssl/openssl/commit/ddecbef6e389d263b728b7fa30fd3d9ce13feddb), [c3aed7e](https://github.com/openssl/openssl/commit/c3aed7e4e6f1960eaa43ecbea2178b82481887af)
- Fixed the out-of-bounds access problem caused by IV length check in CBC and CTR modes, switched to more secure boundary verification and returned errors. (Architecture-related: CBC/CTR mode security fixes)
  ↳ No PR: [d1592f2](https://github.com/openssl/openssl/commit/d1592f21c0d4c2c94a8c6004cf7b5cad2dcb2637)
- Fix the problem of returning positive value when signature verification error in OCSP_basic_verify, to avoid incorrectly trusting OCSP response under OCSP_NOCHECKS flag. (Architecture-related: public API)
  ↳ No PR: [21f89f5](https://github.com/openssl/openssl/commit/21f89f542d745adbf1131338929ae538e200d50d)
- Disable SSL3, TLS1.0, TLS1.1 and DTLS1.0 at security level 1 and above, allowing the use of these protocols only at security level 0. (Architecture-related: Security policy and protocol compatibility)
  ↳ No PR: [7bf2e4d](https://github.com/openssl/openssl/commit/7bf2e4d7f0c7ae19b7a8c416910886a7171e9820)
- Enable and implement security callback functions in the record layer to replace the original compression security detection logic. (Architecture-related: Record layer security callback)
  ↳ No PR: [ed0e298](https://github.com/openssl/openssl/commit/ed0e298fb8a3864b232e1d3801e849935a7a7f7e)
- Add a default private key length based on RFC7919 for the DH named group, and automatically set a smaller key length when generating security prime parameters to improve performance; at the same time, modify the private key generation logic to require that security strength parameters must be provided. (Architecture-related: DH private key generation behavior)
  ↳ No PR: [ddb13b2](https://github.com/openssl/openssl/commit/ddb13b283be84d771deba1e964610b1670641f03)
- Fix the use of custom EVP_CIPHER and EVP_MD objects, ensure that custom objects are used first during initialization, and fix possible null pointer dereferences in summary processing. (Architecture-related: public API)
  ↳ No PR: [25d47cc](https://github.com/openssl/openssl/commit/25d47cccf203c3b71171e78865e48ea061a039a8)
- Add a second verification in the public key check function to ensure that the public key complies with the requirements of SP 800-56A. (Architecture-related: public key verification)
  ↳ No PR: [5b234be](https://github.com/openssl/openssl/commit/5b234be4c44f5b178bc69da3d610ae1b70441873)
- Fixed the protection type mismatch problem in CMP message verification, rejecting mismatched protection methods. (Architecture-related: public API)
  ↳ No PR: [fc93335](https://github.com/openssl/openssl/commit/fc93335760686ad7cf3633d457caf18b0ac83ea2)
- Fix the comparison method of x400Address in GENERAL_NAME_cmp and replace ASN1_TYPE_cmp with ASN1_STRING_cmp to fix CVE-2023-0286. (Architecture-related: public API behavior change)
  ↳ No PR: [7880536](https://github.com/openssl/openssl/commit/7880536fe17c2b5450e279155bedd51771d28c9f)
- In EVP_PKEY_get_bn_param() ensure that the temporary buffer filled successfully is erased before being released to prevent sensitive data from remaining. (Architecture-related: public API)
  ↳ No PR: [34e4a96](https://github.com/openssl/openssl/commit/34e4a962bca998cc2d6eb4be721153fbde2f4c35)
- Add negative integer checks to ASN1_BIT_STRING_set_bit and ASN1_BIT_STRING_get_bit functions to prevent potential overflow issues. (Architecture-related: public API)
  ↳ No PR: [1258a8e](https://github.com/openssl/openssl/commit/1258a8e4361320cd3cfaf9ede692492ce01034c8)
- Limit the length of OBJECT IDENTIFIER that can be processed by the OBJ_obj2txt function to no more than 586 bytes to prevent performance issues caused by over-long sub-identifiers (CVE-2023-2650). (Architecture-related: public API)
  ↳ No PR: [d63b3e7](https://github.com/openssl/openssl/commit/d63b3e7959e79f98d60760a739f7876dc5adc838)
- Fixed the denial of service vulnerability in DH_check() when handling extremely large modulus, added a maximum modulus check (32768 bits), and directly returned an error when this limit was exceeded. (Architecture-related: public API: DH_check added a maximum modulus check)
  ↳ No PR: [9e0094e](https://github.com/openssl/openssl/commit/9e0094e2aa1b3428a12d5095132f133c078d3c3d)
- Fix CVE-2023-3817, add a check on the validity of the q parameter in DH_check to avoid denial of service attacks caused by invalid q values. (Architecture-related: public API: DH_check adds a new q parameter check)
  ↳ No PR: [1c16253](https://github.com/openssl/openssl/commit/1c16253f3c3a8d1e25918c3f404aae6a5b0893de), [1e398be](https://github.com/openssl/openssl/commit/1e398bec538978b9957e69bf9e12b3c626290bea), [4ec53ad](https://github.com/openssl/openssl/commit/4ec53ad6e1791daafbe26bdbd539f2ba9172959a), [4b29762](https://github.com/openssl/openssl/commit/4b29762802c05fa871f0e1efcf804e86db0ddaa2)
- Change the default algorithm of TSA's ess_cert_id_alg option from sha1 to sha256 to improve security. (Architecture-related: public API: ess_cert_id_alg default value is changed to SHA256)
  ↳ No PR: [10536b7](https://github.com/openssl/openssl/commit/10536b7f5b07aab3dc9631e94a56258155a1d942), [305dc68](https://github.com/openssl/openssl/commit/305dc68add0e6b8e52cb5208d5803ac94f90bfb6)
- Changed the default salt length of PBES2 KDF from 8 bytes to 16 bytes to meet FIPS compliance requirements. (Architecture-related: external behavior)
  ↳ No PR: [3859a02](https://github.com/openssl/openssl/commit/3859a027259b5b571eaf5e8cf4c0704611950c2c)
- Change the parameter type of the gf_serialize function to a fixed-size array to take advantage of compiler bounds checking to enhance security. (Architecture-related: public API)
  ↳ No PR: [a7f58bd](https://github.com/openssl/openssl/commit/a7f58bdc1abe245dd09790e8f97d91df271578f4)
- Changed AES constant time code path from enabled by default to optional, now requires explicit definition of OPENSSL_AES_CONST_TIME to enable. (Architecture-related: compile time configuration)
  ↳ No PR: [e180bf6](https://github.com/openssl/openssl/commit/e180bf641ed23010073b0882d63d5dfd48409602)
- Add a key not set check for all operations using EVP_PKEY. If the key is not set, an error will be reported and the operation will be terminated to prevent the use of uninitialized keys. (Architecture-related: EVP behavior change)
  ↳ No PR: [433e134](https://github.com/openssl/openssl/commit/433e13455ede1a39d415b690b8a564b4f36b8dee)
- Add man pages for SSL_get_certificate and SSL_get_privatekey, and update the missing documentation list. (Architecture-related: public API)
  ↳ No PR: [2a92195](https://github.com/openssl/openssl/commit/2a9219514263454896bdda800b4b811843338bc7)
- Update QUIC API design document, add multi-stream operation API definition, and rename some APIs (such as SSL_tick to SSL_handle_events). (Architecture-related: public API rename)
  ↳ No PR: [e4c2988](https://github.com/openssl/openssl/commit/e4c2988dc5f70f15a9cd88e8fa047325c1e41cd2), [64aa8ea](https://github.com/openssl/openssl/commit/64aa8eaf125a33c573d47067849e3cfe89d23070)
- Add comments to OPENSSL_INIT_set_config_filename and OPENSSL_INIT_set_config_appname functions to explain why standard strdup is used instead of OPENSSL_strdup. (Architecture-related: public API)
  ↳ No PR: [26f75c2](https://github.com/openssl/openssl/commit/26f75c2d604014069b5ff32cdf7f13f9e6aec5e6)
- Disable P10-specific Chacha20 and AES-GCM assembly implementations on AIX systems to avoid build issues. (Architecture-related: Platform compatibility)
  ↳ No PR: [abfc152](https://github.com/openssl/openssl/commit/abfc152126616d6f7c1cb1b9cbe8def9f18a1a96), [50d9b2b](https://github.com/openssl/openssl/commit/50d9b2b5f1236f185b2e360b6f4d640e75ddb07f)
- In aarch64 assembly code, add optional support for Armv8.3-A Pointer Authentication and Armv8.5-A Branch Target Identification through compiler macros. (Architecture-related: ARM security feature support)
  ↳ No PR: [19e277d](https://github.com/openssl/openssl/commit/19e277dd19f2897f6a7b7eb236abe46655e575bf)
- Removed explicit inclusion of synchapi.h which does not exist in WinSDK 7.1, and instead used windows.h which already includes this header file. (Architecture-related: Windows platform compatibility)
  ↳ No PR: [eeb6120](https://github.com/openssl/openssl/commit/eeb612021e220de734e1ff08499f42bb962c3916)
- Enable USE_SWAPCONTEXT on IA64 architecture, use swapcontext instead of setjmp/longjmp to correctly save the register stack engine, thereby fixing asynchronous interface test failure. (Architecture-related: IA64 architecture support)
  ↳ No PR: [d26b376](https://github.com/openssl/openssl/commit/d26b3766a0a35668ee62b839a62acbdcd9ff2a98)
- On s390x architecture, mark internal cpuid symbol OPENSSL_s390xcap_P and function OPENSSL_cpuid_setup as hidden to avoid accidentally becoming global symbols in static libraries. (Architecture-related: symbol visibility)
  ↳ No PR: [37816ef](https://github.com/openssl/openssl/commit/37816ef5757e458be9648481e56bf698ee3bfbb1)
- Fix compilation failure on macOS 10.7 and 10.8 due to incompatibility of clang's __atomic_is_lock_free parameter by disabling the __atomic_* built-in functions on these systems. (Architecture-related: Platform compatibility)
  ↳ No PR: [d39de47](https://github.com/openssl/openssl/commit/d39de4792dbdb6ab5f78c79d52d0210b44584538)
- Add compilation configuration option OPENSSL_NO_UNIX_SOCK to control Unix domain socket support, and adjust related conditional compilation logic. (Architecture-related: build configuration)
  ↳ No PR: [081f348](https://github.com/openssl/openssl/commit/081f3484593cdd3be2b7fdd8818c3f928ce729bc)
- Fix UWP build, manually declare VirtualLock function in memory safety related code. (Architecture-related: Platform compatibility)
  ↳ No PR: [ff1efe6](https://github.com/openssl/openssl/commit/ff1efe6e261598c3f71727b796767a8e716bcbe2)
- For HP-UX platform, avoid including non-existent sys/select.h and use sys/time.h instead. (Architecture-related: platform compatibility)
  ↳ No PR: [737e849](https://github.com/openssl/openssl/commit/737e849fd938a943cad207cde1c711e961f92294)
- Added Windows on Arm build target, supports clang-cl as assembler and compiler, and updated armcap source code to adapt to Windows platform feature detection. (Architecture-related: Platform compatibility: Windows on Arm)
  ↳ No PR: [b863e1e](https://github.com/openssl/openssl/commit/b863e1e4c69068e4166bdfbbf9f04bb07991dd40), [4a3b626](https://github.com/openssl/openssl/commit/4a3b6266604ca447e0b3a14f1dbc8052e1498819), [e9460bb](https://github.com/openssl/openssl/commit/e9460bb45b38e9edb6a57b79daeefdc80eb9e81f)
- Support building OpenSSL with QUIC feature disabled, add conditional compilation protection for internal functions and test cases, and add no-quic option in CI configuration for m68k cross-compilation. (Architecture-related: Build and installation mode: Support disabling QUIC build)
  ↳ No PR: [6292519](https://github.com/openssl/openssl/commit/6292519cd8102983e9924b6b0d3f298ac5f93e80), [d001006](https://github.com/openssl/openssl/commit/d001006e50e6ca591459f6b63d2365532578a36a)
- Disable atomic reference counting to support threadless builds, fallback to normal addition. (Architecture-related: Build and installation mode: Support threadless builds)
  ↳ No PR: [b484c62](https://github.com/openssl/openssl/commit/b484c6268ce38ccbc1bf5ee95bbd36f76fba994f)
- Fix strict warning issues in Windows builds, remove unnecessary const qualifiers in CMP API to keep declarations consistent with definitions. (Architecture-related: public API)
  ↳ No PR: [6f792f4](https://github.com/openssl/openssl/commit/6f792f4d27b47213166e0fa9c9b10a3eab85b8f6)
- Fix the OPENSSL_armcap_P symbol duplication problem on the ARM platform, limit its definition to 64-bit architecture, and ensure that only one copy is kept in libcrypto.a. (Architecture-related: platform compatibility)
  ↳ No PR: [93370db](https://github.com/openssl/openssl/commit/93370db1fc76ad37bd53cfbeb948d1ded43d3b2a), [7b508cd](https://github.com/openssl/openssl/commit/7b508cd1e18f04d509af4df6c2ab4709c4389d19)
- Disable P10-specific AES-GCM assembly code builds on macOS. (Architecture-related: Platform Compatibility)
  ↳ No PR: [175645a](https://github.com/openssl/openssl/commit/175645a1a695017a312155a2c1d864ad8bff4eaa)
- Fixed a build error caused by missing InterlockedOr64 in the Visual Studio 2010 x86 compiler and extended conditional macro coverage to this compiler version. (Architecture-related: Platform compatibility)
  ↳ No PR: [8bdc370](https://github.com/openssl/openssl/commit/8bdc3708964814ea0b7002df020fbd459e3a813f)
- Fixed compilation errors caused by incompatible function pointer types when using clang-cl 16 or higher. (Architecture-related: Platform compatibility)
  ↳ No PR: [fae5a15](https://github.com/openssl/openssl/commit/fae5a15573fb314d0a5bc06f3929fd5ec6ffe5a5)
- Introduced the compile option no-ecx, which is used to remove ECX related features, thereby reducing the binary size for platforms that do not require this feature. (Architecture-related: build option no-ecx)
  ↳ No PR: [4032cd9](https://github.com/openssl/openssl/commit/4032cd9a1434610e4dc2bbde01f98d04faa615e5)
- Introduced HAVE_MADVISE and NO_MADVISE macro definitions, allowing builders to explicitly control whether to call the madvise function in environments that lack it. (Architecture-related: Build configuration: madvise control)
  ↳ No PR: [78634e8](https://github.com/openssl/openssl/commit/78634e8ac253a8edf338d329965724dfa8e033ab)
- Disable floating point related code in UEFI environment to avoid build issues caused by floating point operations. (Architecture-related: Platform compatibility: UEFI floating point disabled)
  ↳ No PR: [2c50057](https://github.com/openssl/openssl/commit/2c500578fc68871eca7fabc7ee36b4027891671b)
- Allows disabling HTTP support at compile time, and conditional compilation protection has been added to the relevant code. (Architecture-related: Build configuration: HTTP support can be disabled)
  ↳ No PR: [3ca28c9](https://github.com/openssl/openssl/commit/3ca28c9e81fae36b0b44dc39beecd2b5a7561975)
- Fix WebAssembly/WASI build, force use of timegm, and add WASI support for base implementation OPENSSL_issetugid. (Architecture-related: platform compatibility)
  ↳ No PR: [66f61ec](https://github.com/openssl/openssl/commit/66f61ece724a54253da36f70274bc320faf9f4e2)
- Fixed the problem of build failure when IPv6 is disabled, and added conditional compilation protection for IPv6 related code. (Architecture-related: platform compatibility)
  ↳ No PR: [9c8d04d](https://github.com/openssl/openssl/commit/9c8d04dbec03172d6ffe4eaa38ea4b1ac2741f26)
- Fix compilation errors caused by missing SIZE_MAX definition on HP-UX, add necessary header file references in ssl/priority_queue.c. (Architecture-related: platform compatibility)
  ↳ No PR: [7f14656](https://github.com/openssl/openssl/commit/7f14656e1cc002a09b2d6148302a1fc71a30f7cd)
- Moved the ALIGN32 and ALIGN64 macro definitions to common.h, and fixed the compilation problem caused by the lack of __GNUC__ definition under clang-cl.exe. (Architecture-related: platform compatibility)
  ↳ No PR: [12d08fe](https://github.com/openssl/openssl/commit/12d08fe3a50f28fe80ff591e05d7f8253148afb4)
- Add necessary header file inclusions in ssl/quic/quic_cfq.c to support platforms that do not define macros such as UINT64_MAX. (Architecture-related: platform compatibility)
  ↳ No PR: [cfbdc5d](https://github.com/openssl/openssl/commit/cfbdc5dd14bf9fc969c9eb76216ab59a4ae64ba4)
- Fixed the build failure caused by the lack of sendmmsg in the old version of glibc, and added glibc version check to ensure that both recvmmsg and sendmmsg are supported. (Architecture-related: platform compatibility)
  ↳ No PR: [5d96106](https://github.com/openssl/openssl/commit/5d96106c43d5b4e2d97406e5d3934323ae5bd1b4)
- Remove the legacy compatibility code of the VxWorks platform and uniformly use the standard sys/un.h header file. (Architecture-related: platform compatibility)
  ↳ No PR: [a668012](https://github.com/openssl/openssl/commit/a6680123643bc3289ecbcbd6bce844a814c1510a)
- Fixed the compilation problem of thread library functions on non-UNIX platforms, limiting the function definitions in threads_lib.c to only compile under UNIX systems. (Architecture-related: platform compatibility)
  ↳ No PR: [523e54c](https://github.com/openssl/openssl/commit/523e54c15cfadb8c19f6a181b9a69aabd9f58453)
- Revised the field types in the SSL_get_conn_close_info related structure, changing is_local and is_transport from char to int. (Architecture-related: public API)
  ↳ No PR: [bb9b8a3](https://github.com/openssl/openssl/commit/bb9b8a333ffaf998e60016819ee1e8c2da58f0fd)
- Replace the conditional compilation macro of IPv6 related code with OPENSSL_USE_IPV6 to improve platform compatibility. (Architecture-related: platform compatibility)
  ↳ No PR: [836bb08](https://github.com/openssl/openssl/commit/836bb0890dc4d139215824cc9ac35591361f8117)
- Change the function parameter name template to templ to avoid conflict with C++ reserved words. (Architecture-related: public API)
  ↳ No PR: [420a087](https://github.com/openssl/openssl/commit/420a0874db8a6b0070d4820e81e82bf48412d7da)
- Under Unix systems, ensure that internal/sockets.h correctly contains errno.h and sys/poll.h. (Architecture-related: platform compatibility)
  ↳ No PR: [16b220d](https://github.com/openssl/openssl/commit/16b220dde3ffa0cfaf71dc3bd37a35187f8099fb)
- Update the number of SSL error code SSL_R_STREAM_COUNT_LIMITED. (Architecture-related: public API: error code number update)
  ↳ No PR: [ade3baa](https://github.com/openssl/openssl/commit/ade3baa6629b152185383605fb14d7b09483b409)
- Add srandom() compatible macro definition for memory allocation failure debugging function on Windows platform. (Architecture-related: Platform compatibility: Windows memory debugging)
  ↳ No PR: [3b107b8](https://github.com/openssl/openssl/commit/3b107b86ca7d1c6309bc7071ead59acb8c098f3b)

### Provider Plugin Framework
- Removed DES cryptographic algorithm from FIPS provider. (Architecture-related: FIPS provider algorithm removed)
  ↳ No PR: [fc0bb34](https://github.com/openssl/openssl/commit/fc0bb3411bd0c6ca264f610303933d0bf4f4682c)
- Added the ability to obtain EVP methods by specified provider: introduce provider parameters in the underlying constructor, add multiple internal functions for obtaining signatures, asymmetric cryptography, key exchange and KEM methods by provider, and support cache acquisition. (Architecture-related: Provider method acquisition)
  ↳ No PR: [cfce50f](https://github.com/openssl/openssl/commit/cfce50f791511c8fee7dec90c57f02d9410d039f), [ff77814](https://github.com/openssl/openssl/commit/ff7781462dd04ab99c159136b47672252bad7fa8), [dc010ca](https://github.com/openssl/openssl/commit/dc010ca6ec01d313a84c3c4b040232655a1772ad)
- Allow providers to override error mark functions: move ERR_set_mark, ERR_pop_to_mark and ERR_clear_last_mark to independent source files, and add a new ERR_count_to_mark function; legacy providers use the upcall mechanism to reimplement ERR related functions. (Architecture-related: public API)
  ↳ No PR: [fbe8870](https://github.com/openssl/openssl/commit/fbe88706a4f93f9e1940a07062d77c81b7fdf04d), [8c2e588](https://github.com/openssl/openssl/commit/8c2e588bcf0de61880ec8a956ef57ad6b8a50163)
- Added an interface to remove all registered methods by provider; modified the cleanup behavior when the provider is deactivated or fails self-test, and changed to directly clear the associated methods instead of just refreshing the cache; at the same time, the activation and deactivation logic was optimized. (Architecture-related: Provider method cleanup)
  ↳ No PR: [2e4d067](https://github.com/openssl/openssl/commit/2e4d0677ea858c619a33235265dbee19520a9d35), [c59fc87](https://github.com/openssl/openssl/commit/c59fc87b338880893286934f02c446854f5baabf)
- Removed AES SIV cryptographic algorithm from FIPS provider. (Architecture-related: public API)
  ↳ No PR: [c3f985c](https://github.com/openssl/openssl/commit/c3f985cfd6fb4b8ab1765403d65fed3d006b2163)
- Remove redundant internal header files include/internal/decoder.h, migrate function declarations to include/crypto/decoder.h, and update the include paths of related source files. (Architecture-related: public API)
  ↳ No PR: [98d8117](https://github.com/openssl/openssl/commit/98d81174d3763053b32b8cfd7225acd0a111d456)
- Adjust sub-provider reference counting logic: self-referential sub-providers no longer increase or release the reference count of the parent provider to avoid hindering parent provider unloading; non-self-referential sub-providers retain reference count propagation. (Architecture-related: provider reference counting)
  ↳ No PR: [4da7663](https://github.com/openssl/openssl/commit/4da7663b02bf05542830e85db6f74cf90daf1f49)
- Added empty digest implementation to default provider to maintain compatibility with version 1.1.1. (Architecture-related: compatibility)
  ↳ No PR: [bef9b48](https://github.com/openssl/openssl/commit/bef9b48e5071cdd2b41a4f486d1bcb5e14b2a5c3)
- KBKDF supports different R_BITS length configurations. (Architecture-related: KBKDF configuration)
  ↳ No PR: [0e9a265](https://github.com/openssl/openssl/commit/0e9a265e42890699dfce82f1ff6905de6aafbd41)
- CMS signing and verification now supports provider-implemented key types and unifies signature processing logic. (Architecture-related: public API)
  ↳ No PR: [d15d561](https://github.com/openssl/openssl/commit/d15d561844d8989e50896724d89681ae7ba81a74)
- Fixed the problem of obtaining seeds from weak entropy sources, using rand_get_seed and rand_clear_seed methods instead. (Architecture-related: public API)
  ↳ No PR: [7998e7d](https://github.com/openssl/openssl/commit/7998e7dc07d8f1f516af32887f2490c03cd8c594)
- Added the implementation of PVK KDF (PIN Verification Key key derivation function) in providers. (Architecture event: Added PVK KDF implementation)
  ↳ No PR: [722fe8e](https://github.com/openssl/openssl/commit/722fe8edf224ecc0921481b47fdd06a54d82e4ff), [2d34e5b](https://github.com/openssl/openssl/commit/2d34e5b2ecf6a5db982c53bb56c62249b7791051), [1ffac6c](https://github.com/openssl/openssl/commit/1ffac6ca174d25a61f2e1e70dd0fd1eb7eaacbf5), [fe01052](https://github.com/openssl/openssl/commit/fe01052f775d1b5dff86ff9b405b6b0df5efd3cf), [a632bfa](https://github.com/openssl/openssl/commit/a632bfaa4ee3339749f7a6a07ab4d0abee4eaaef), [8df9f34](https://github.com/openssl/openssl/commit/8df9f34384cf1a9b8bc8748ea594b07fb5525899)
- Added SM4-GCM and SM4-CCM algorithm support, including implementation and OID definition. (Architecture event: Provider_Crypto_Implementations added SM4-GCM/CCM algorithm)
  ↳ No PR: [c2ee608](https://github.com/openssl/openssl/commit/c2ee608a234340aa735f894f8d84ead0ce58286e), [a596d38](https://github.com/openssl/openssl/commit/a596d38a8cddca4af3416b2664e120028d96e6a9)
- Added default provider support for Keccak-224, 256, 384 and 512 algorithms, including s390x hardware acceleration, provider registration, function implementation and name definition. (Architecture event: Provider_Crypto_Implementations module change)
  ↳ No PR: [524f126](https://github.com/openssl/openssl/commit/524f12611040de64cda13dd148ad1b8ca559c730)
- Added Argon2 key derivation function (KDF) implementation, supporting three modes: Argon2d, Argon2i and Argon2id. (Architecture event: Provider_Crypto_Implementations module change)
  ↳ No PR: [6dfa998](https://github.com/openssl/openssl/commit/6dfa998f7ea150f9c6d4e4727cf6d5c82a68a8da), [a901b31](https://github.com/openssl/openssl/commit/a901b31e99442f087051ae7efdcbc9ad6e6a5b33), [c77fb9a](https://github.com/openssl/openssl/commit/c77fb9af5595fa416637f775e51722699ea3c78b)
- Add XOF (Extensible Output Function) support for blake2b512 digest algorithm, allowing the output length to be set through context parameters. (Architecture event: Provider_Crypto_Implementations module changes)
  ↳ No PR: [786b9a8](https://github.com/openssl/openssl/commit/786b9a8d3f8e203c5536e36b9a9bab83bde0311a), [0be4b04](https://github.com/openssl/openssl/commit/0be4b0403d2f65adf0d037581223dbebd0fa135e)
- Added support for loading root certification authorities (CA) from Windows Crypto API. (Architecture event: Added Windows storage support)
  ↳ No PR: [606e042](https://github.com/openssl/openssl/commit/606e0426a148034c8c131de9f31f7d3e38be99ea)
- Implemented the AES-GCM-SIV algorithm defined in RFC8452 in the default provider. (Architecture event: Added AES-GCM-SIV algorithm)
  ↳ No PR: [0113ec8](https://github.com/openssl/openssl/commit/0113ec8460a918f8bc782130db8f75540b3b1ab2)
- Added a declaration of the receiving end depacketizing function ossl_quic_depacketize in the QUIC header file. (Architecture event: QUIC protocol engine module change)
  ↳ No PR: [d7fed97](https://github.com/openssl/openssl/commit/d7fed97e37a4a66e8c7d53015684790951f6e943)
- Implement the initial version of QUIC ACK manager, statistics manager and congestion control API, and add supporting testing and design documents. (Architecture event: QUIC protocol engine module change)
  ↳ No PR: [fa4e92a](https://github.com/openssl/openssl/commit/fa4e92a70a5f363fbbee192c0ecab697e3aa1248), [422368a](https://github.com/openssl/openssl/commit/422368aebd908d6966639597aab786ee12eb62f1), [79a80f8](https://github.com/openssl/openssl/commit/79a80f8b58bed854eb30a22e1643869dcc29e005), [fd6c147](https://github.com/openssl/openssl/commit/fd6c1476a09b4766ce6c435d50ad16acebcd46df), [891b639](https://github.com/openssl/openssl/commit/891b639377af8be10f5e41616db6afabceae7cef)
- Added QUIC frame encoding and decoding functions, and added corresponding test cases. (Architecture event: QUIC protocol engine module change)
  ↳ No PR: [dffafaf](https://github.com/openssl/openssl/commit/dffafaf48174497a724d546c3483d2493fc9b64c), [b09e246](https://github.com/openssl/openssl/commit/b09e246aba584cd17d1d027f735f238b1b7f082c)
- Implemented deterministic ECDSA and DSA signatures based on RFC6979, added HMAC_DRBG KDF implementation, and introduced the nonce_type parameter in the signature API. (Architecture event: Encryption provider implementation module change)
  ↳ No PR: [f3090fc](https://github.com/openssl/openssl/commit/f3090fc710e30a749acaf9e5dfbe20dd163cf15d), [6b3d287](https://github.com/openssl/openssl/commit/6b3d28757620e0781bb1556032bb6961ee39af63)
- Support decoding SM2 parameters, adjust the elliptic curve key text output function to correctly display the parameter type when the curve is SM2. (Architecture event: Crypto provider implementation module change)
  ↳ No PR: [08ae9fa](https://github.com/openssl/openssl/commit/08ae9fa627e858b9f8e96e0c6d3cf84422a11d75)
- Added QUIC receiving end depacketizer, which implements frame processing functions, flow management logic and frame validity checking based on packet type. (Architecture event: QUIC receiving end depacketizer is added)
  ↳ No PR: [69ed676](https://github.com/openssl/openssl/commit/69ed6760f938975d9cdcc12ec756d58c83ac6b90), [8a16364](https://github.com/openssl/openssl/commit/8a163641c1d94c877a46ade8ff2ecefdf5cbbeeb)
- Added QUIC demultiplexer and record layer receiver, supporting packet parsing, header protection, key derivation and related testing. (Architecture event: QUIC demultiplexer and record layer receiver added)
  ↳ No PR: [ec279ac](https://github.com/openssl/openssl/commit/ec279ac21105a85d9f11eed984eb64405811425d), [ecc920b](https://github.com/openssl/openssl/commit/ecc920b3277311e859282b6d400ba8566d7ea8c1)
- Implemented the function of obtaining human-readable status string for the record layer. (Architecture events: Record layer status string function)
  ↳ No PR: [d0b17ea](https://github.com/openssl/openssl/commit/d0b17ea025477ce13ebe5d802ada232a57e1a2f2)
- Record layer object's options, mode and read-ahead settings can now be updated after instantiation. (Architecture events: Record layer settings can be updated after instantiation)
  ↳ No PR: [4566dae](https://github.com/openssl/openssl/commit/4566dae7236b5c90364e963fd02b2ee533e0d712)
- Added a custom recording layer setting function, and optimized the recording layer error handling logic. (Architecture event: Custom recording layer setting function)
  ↳ No PR: [d3192c2](https://github.com/openssl/openssl/commit/d3192c2643e4de2e2c36e107b7759f845a6e2bff)
- Added receiving time field and decoded packet sequence number field, and supports sending end key update. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [948c656](https://github.com/openssl/openssl/commit/948c656c66a3846337a0262197766c80ec7c9e59)
- Implemented QUIC flow control function, added sender and receiver flow control controllers. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [508e087](https://github.com/openssl/openssl/commit/508e087c4c9e0f6548816e0044022b257f179585), [c4abf9e](https://github.com/openssl/openssl/commit/c4abf9ebb023248046604588692f50a9eee5d6b8)
- Implemented DHKEM algorithm for EC, X25519 and X448 curves at the provider layer, and added authentication encapsulation and decapsulation API. (Architecture event: Provider_Crypto_Implementations module change)
  ↳ No PR: [78c44b0](https://github.com/openssl/openssl/commit/78c44b05945be07eae86f0164b9b777e2de2295b), [d7b5f06](https://github.com/openssl/openssl/commit/d7b5f06ede163851d39f5a8b507bd0670deeaa21)
- Implemented QUIC send stream management functions, including ACK processing and integer collection data structures. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [8302259](https://github.com/openssl/openssl/commit/830225901365b7076eaa5afc580529394e2a137f)
- Added QUIC congestion feedback queue (CFQ) implementation, including queue management, frame addition, tag sending/loss, release and other core functions. (Architecture event: QUIC protocol module is added)
  ↳ No PR: [c282da8](https://github.com/openssl/openssl/commit/c282da8bc77500cb40ec63754b5230b4bc883242)
- Implemented QUIC Transport Packet Information Manager (TXPIM). (Architecture event: QUIC protocol module added)
  ↳ No PR: [d77aea5](https://github.com/openssl/openssl/commit/d77aea591650cd3bfe7c25cbb6955011bb21b416)
- Added implementation of QUIC frame loss detection (FIFD) module. (Architecture event: QUIC protocol module is added)
  ↳ No PR: [0ede517](https://github.com/openssl/openssl/commit/0ede517cfa73fd3566d2ecd32215b4b12dd1d3b5)
- Added RAND_set0_public and RAND_set0_private functions for public and private DRBGs, and modified DRBG creation logic to support injection of entropy in FIPS known answer tests. (Architectural event: Provider_Crypto_Implementations module changes)
  ↳ No PR: [7c8187d](https://github.com/openssl/openssl/commit/7c8187d43d043c6a66559ed341ff1e01b8711093), [8ff861d](https://github.com/openssl/openssl/commit/8ff861dcee38a41ce93374753e8c462e4b9012e2)
- Added implementation of QUIC TX packet packer and stream mapper, including frame generation, acknowledgment, loss handling, stream state management. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [a73078b](https://github.com/openssl/openssl/commit/a73078b79fc6f229b95312dcb20e4f61120a108c)
- Implemented preliminary support for loading signature algorithms from providers, and restructured signature algorithm-related data structures and functions in certificates and SSL contexts. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [ee58915](https://github.com/openssl/openssl/commit/ee58915cfd9d0ad67f52d43cc1a2ce549049d248), [3ffd23e](https://github.com/openssl/openssl/commit/3ffd23e9529d725903bc97fd45489a77b831876f)
- Implements hybrid public key encryption (HPKE) defined by RFC9180, supports all modes, suites and export mechanisms, and provides corresponding APIs, documentation and tests. (Architecture event: Added HPKE module)
  ↳ No PR: [ad06248](https://github.com/openssl/openssl/commit/ad062480f7490197b174edad8625ce40d74f6e68)
- Added XTS mode implementation for SM4 algorithm, supporting encryption/decryption, context management and parameter settings. (Architecture event: Provider_Crypto_Implementations module added SM4-XTS encryption mode)
  ↳ No PR: [2788b56](https://github.com/openssl/openssl/commit/2788b56f0c8306c89c97a6599484120afddfa14a)
- Added support for AES-128/192/256 GCM-SIV mode in FIPS provider. (Architecture event: Provider_Crypto_Implementations module added AES-GCM-SIV encryption mode)
  ↳ No PR: [edaab86](https://github.com/openssl/openssl/commit/edaab86dc001603741f5b5e406afc1cc3a1c4e6e)
- Added datagram injection support for QUIC connections, added SSL_inject_net_dgram function. (Architecture event: SSL_Protocol_Engine module change (QUIC)
  ↳ No PR: [553a4e0](https://github.com/openssl/openssl/commit/553a4e00aab3e2cc04f47678cba3cd8345e7b0e3)
- Added SSL_is_tls() and SSL_is_quic() functions to determine the protocol type. (Architecture event: SSL_Protocol_Engine module change (Protocol Type API)
  ↳ No PR: [50769b1](https://github.com/openssl/openssl/commit/50769b15ea76123406b5ccebe85b2402e64e9fc6), [3e5a47d](https://github.com/openssl/openssl/commit/3e5a47d4de5754a2d2f42b3402bfe887010357ae), [843f6e2](https://github.com/openssl/openssl/commit/843f6e277f2905d95f0c2d0804deb3ea62cef1c1)
- Add QUIC stream creation and management API, support any number of streams, including local and remote stream creation, and implement flow control and error handling. (Architecture event: SSL_Protocol_Engine module change (QUIC stream API)
  ↳ No PR: [26ad16e](https://github.com/openssl/openssl/commit/26ad16ea84c58d91375491c0872e43dc27915b4a), [2dbc39d](https://github.com/openssl/openssl/commit/2dbc39deacf9d5850eecef515cbc50331750dd22), [f20fdd1](https://github.com/openssl/openssl/commit/f20fdd16d817a095f58f9c016044abef24e50e58), [ed83567](https://github.com/openssl/openssl/commit/ed835673ae5d99cac39d0bef6677597a68d1e248), [9715e3a](https://github.com/openssl/openssl/commit/9715e3aacffece002f94725fb2105601111f6fa6)
- Implement the SSL_get0_connection function for QUIC connections, allowing to obtain the underlying SSL object. (Architecture event: SSL_Protocol_Engine module change (SSL_get0_connection API)
  ↳ No PR: [020d038](https://github.com/openssl/openssl/commit/020d0389396d0ee01041188a3d1b211a1d6b6c6a)
- Added processing of OSSL_PKEY_PARAM_EC_PUB_X,Y requests for EC legacy keys to support tpm2-tss loading legacy EC keys. (Architecture event: Provider_Crypto_Implementations module changes (EC key parameters)
  ↳ No PR: [9adbce7](https://github.com/openssl/openssl/commit/9adbce74933b87dd4fe776b70fef55f2f468f5f7)
- Refactor the FIPS option processing code, introduce a unified option structure, and add new options to limit the summaries available to DRBG. (Architecture event: Provider_Crypto_Implementations module changes (FIPS option refactoring)
  ↳ No PR: [83ccf81](https://github.com/openssl/openssl/commit/83ccf81b1dd8886d54c570354ef8c532af4c514f)
- Added QUIC stream setting and acceptance API, including SSL_set_default_stream_mode, SSL_accept_stream and SSL_get_accept_queue_len. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [8b7be3a](https://github.com/openssl/openssl/commit/8b7be3aa7e90d85441f5012624cece4dca33291e), [cb68ce9](https://github.com/openssl/openssl/commit/cb68ce9fa7e2312afd8e5346a799d32024b67d02)
- Added QUIC incoming stream rejection policy API and automatic rejection implementation, supporting SSL_set_incoming_stream_reject_policy. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [8a90df3](https://github.com/openssl/openssl/commit/8a90df343edb194920b7a01c8b5e47d8b6e952c5), [995ff28](https://github.com/openssl/openssl/commit/995ff282103d444844a476ae6aba4a05936284fa)
- Implement QUIC MAX_STREAMS flow control, including receive stream controller support and receive path implementation. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [5bd9ddd](https://github.com/openssl/openssl/commit/5bd9ddd86e714705840215b8d2bbb0aedc598e96), [90cecc4](https://github.com/openssl/openssl/commit/90cecc406f58b229ffa9c8e8473eaa6924c4a5d5), [a6b6ea1](https://github.com/openssl/openssl/commit/a6b6ea17376572e3c0227b98f21dedc48215aa9a)
- Implement QUIC implicit stream creation, automatically create streams when receiving remote STREAM frames, and comply with RFC requirements. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [999e13f](https://github.com/openssl/openssl/commit/999e13f40eda5a2ca39d1efb407b96f81d2b9535), [dea57ec](https://github.com/openssl/openssl/commit/dea57ecf3d0729abb964bfc1ff687b2cbb9845de)
- Added QUIC stream garbage collection mechanism, including stream full confirmation judgment and sending partial ID guarantee function. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [0847e63](https://github.com/openssl/openssl/commit/0847e63ee5d58d824390aadcbcf10281c45900c4)
- Add frame confirmation and stream update callback support to QUIC FIFD initialization function. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [9cacba4](https://github.com/openssl/openssl/commit/9cacba434b027bc6f3a3f3c4255c2453935e5357)
- Added the function of querying the STOP_SENDING and RESET_STREAM status of the peer for QUIC TSERVER. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [f0e22d1](https://github.com/openssl/openssl/commit/f0e22d1be8a66106932f6f7c069087372ff33789), [d63b8cb](https://github.com/openssl/openssl/commit/d63b8cbb1be215bab4bea34e4a17c7fd13f8da49), [cbe7f58](https://github.com/openssl/openssl/commit/cbe7f586ad42b7cf6d16b11a6d614798df0a5d29)
- Added the function of popping up new inbound streams for the QUIC test server, and improved stream reset detection. (Architecture event: QUIC protocol engine change)
  ↳ No PR: [1df479a](https://github.com/openssl/openssl/commit/1df479a9f95d2862e32c43c89d17d3e094fb2292)
- The QUIC stream mapping initialization function extends parameters to be aware of the server role, and initializes more internal states. (Architecture event: QUIC stream mapping interface change)
  ↳ No PR: [5915a90](https://github.com/openssl/openssl/commit/5915a900af86db8625caa77a02fd50cf9a3b3e1b)
- Add initial QUIC support for msg_callback, currently only supports triggering callback when datagram is received. (Architecture event: msg_callback QUIC support)
  ↳ No PR: [63dfde8](https://github.com/openssl/openssl/commit/63dfde87c46f8ad037ad5b5e635e609f4909578e), [bfcf135](https://github.com/openssl/openssl/commit/bfcf1356f9fdc6ad939f73f2d4e505bd519c33d2)
- Add tracing support for QUIC datagrams, extending SSL_trace to dump QUIC datagram reception information. (Architecture event: SSL_trace QUIC datagram tracing)
  ↳ No PR: [45aac10](https://github.com/openssl/openssl/commit/45aac10717479b5c2445e7704cd742b0d754aaa8)
- Modify the SSL_get_event_timeout API, add the is_infinite parameter to distinguish whether the timeout is infinite, and add support for DTLSv1 timeout control commands in the QUIC implementation to maintain compatibility. (Architecture event: SSL_get_event_timeout API changes)
  ↳ No PR: [7ea4971](https://github.com/openssl/openssl/commit/7ea497134733f8197f359fe3243ad24e97df0f1a), [2f90ea3](https://github.com/openssl/openssl/commit/2f90ea3daef94ab9806ae20eab1f37986d53eade), [b626a0f](https://github.com/openssl/openssl/commit/b626a0f1fdd306845e5ff7632329d32d5f9e2fba)
- Add SSL_trace support for QUIC packets, extend tracing capabilities to support multiple frame types and sent frames, and add trace callback support for sent QUIC packets. (Architecture Event: SSL_trace QUIC Packet Tracing)
  ↳ No PR: [2a35a1b](https://github.com/openssl/openssl/commit/2a35a1bec0845d314f06a88d703a9eb30dbed10e), [70f0ea2](https://github.com/openssl/openssl/commit/70f0ea280af0bed9fb48b20b61c7a12c7f03e6d9), [45454cc](https://github.com/openssl/openssl/commit/45454cccf8172b5a2d7c1342067a1d8dc8396fc9), [e8528c9](https://github.com/openssl/openssl/commit/e8528c95a0543a218b432d2ea02e6bd0c1e7ab19)
- Add NEW_CONNECTION_ID frame processing, adjust active connection ID limits, support recording key periods, add a new ACK send callback interface, allow encoding and decoding to retain header bits, and implement RFC 9000 Section 9.6 requirements to discard packets from new server addresses that have not been migrated. (Architectural event: QUIC protocol implements multiple changes)
  ↳ No PR: [eff0465](https://github.com/openssl/openssl/commit/eff046524b970243196d4622d20ffb8e0aeb208b), [754d228](https://github.com/openssl/openssl/commit/754d2282cd50fef14971605d7151623bb11e3fd6), [8f9c921](https://github.com/openssl/openssl/commit/8f9c9213a1ba034de3140a0d0c0c3b1e46afe457), [5b9452e](https://github.com/openssl/openssl/commit/5b9452e03797e623681d64a0dae6ed1e2cc99f27), [3ffb7d1](https://github.com/openssl/openssl/commit/3ffb7d104f618262175283f26275b8be61e27467)
- The Store module adds a new deletion API OSSL_STORE_delete, and extends the loader registration to support deletion and opening extended functions. (Architecture event: the Store module adds a new deletion API)
  ↳ No PR: [0a8807b](https://github.com/openssl/openssl/commit/0a8807b4a838ec6e6a84b2a28781e821ede90480), [3f8b7b9](https://github.com/openssl/openssl/commit/3f8b7b98759553336dbdfc29f9cc4118046afede)
- Added support for random number generation based on RNDR/RNDRRS instructions for the ARM64 platform and used it as the default seed source. (Architecture-related: platform compatibility)
  ↳ No PR: [eb28fda](https://github.com/openssl/openssl/commit/eb28fda79748c303d88a8af48de5187100f2c64c), [efa1f22](https://github.com/openssl/openssl/commit/efa1f22483ee43d84e1aee01b08c0bda04060c1c), [e8b597f](https://github.com/openssl/openssl/commit/e8b597f33143410fb50bdeba8722c249524bc0b9)
- Added support for EncryptedPrivateKeyInfo output for ECX key encoding, and fixed related error codes. (Architecture-related: public API)
  ↳ No PR: [0195cdd](https://github.com/openssl/openssl/commit/0195cdd28fde7d0897e368fdcd4e92509425faad), [602bfb8](https://github.com/openssl/openssl/commit/602bfb8b98125f6745cd40dbc5fce9614ae5e418)
- Add AES hardware acceleration support for RISC-V 64-bit and 32-bit platforms, covering ZKND/ZKNE/Zbkb instruction sets and multiple encryption modes. (Architecture-related: platform compatibility)
  ↳ No PR: [77d29ff](https://github.com/openssl/openssl/commit/77d29ff041edcdc6a3d33251d6270a4cfe0be9b3), [ee11118](https://github.com/openssl/openssl/commit/ee11118deb65d2b22b94721125a5649d05591e7b), [cbb15b3](https://github.com/openssl/openssl/commit/cbb15b31b98f47276cf9e87453831d96274baf66), [5ccee69](https://github.com/openssl/openssl/commit/5ccee69b1384fa9377986a6f7730e0d9a372b42b)
- Add RIPEMD160 digest algorithm to the default provider. (Architecture-related: public API)
  ↳ No PR: [ecd8314](https://github.com/openssl/openssl/commit/ecd831469919215b0a45693b00ec0fd7d42d5d61)
- Supports all five EdDSA instances in RFC 8032 (Ed25519, Ed25519ctx, Ed25519ph, Ed448, Ed448ph), specify the instance through the EVP API and OSSL_PARAM, and allows passing in the context string. (Architecture-related: public API)
  ↳ No PR: [836080a](https://github.com/openssl/openssl/commit/836080a89a1f5e45dac4e0df76b9270587f65d5b)
- Updated the KAT test of FIPS 140-3, modified the signature self-test function to set the DRBG status before each test, and added functions to reset and set the main DRBG; also added test cases for RSA, EC and DSA key generation self-test failure in FIPS mode, and fixed the problem that the buffer size parameter in the signature self-test was not set correctly. (Architecture-related: FIPS self-test behavior)
  ↳ No PR: [a11064c](https://github.com/openssl/openssl/commit/a11064c83b58f9e1b3741704a11cfec2d91aac0e), [dcd20cc](https://github.com/openssl/openssl/commit/dcd20cc139d1a26cd94c66cc5ebc8ab85d928356), [61adb6c](https://github.com/openssl/openssl/commit/61adb6cf950b65a7bfce9a8d78a7744dfae9f978)
- Added the -self_test_oninstall option to the fipsinstall command, which is used to run self-tests during installation; at the same time, the default behavior is changed to be controlled by the -self_test_onload option. (Architecture-related: FIPS installation behavior)
  ↳ No PR: [7057ddd](https://github.com/openssl/openssl/commit/7057dddbcb5e053470121adeff0b6595fa6da0d8)
- Rejoin 3DES into the FIPS provider and provide it as a non-approved algorithm for backward compatibility; update related documentation and testing at the same time. (Architecture-related: FIPS provider)
  ↳ No PR: [a0ea8ac](https://github.com/openssl/openssl/commit/a0ea8ac134e8f503876f19bdc04da69e8862f3a7), [464c101](https://github.com/openssl/openssl/commit/464c1011b02936850fc779739013dba52650840a), [ccc860a](https://github.com/openssl/openssl/commit/ccc860a77e542bee24f64e44f7bcea5706068866), [d4e105f](https://github.com/openssl/openssl/commit/d4e105f6d53002ebaac2caf0c723bbf734f4a21a), [4072a76](https://github.com/openssl/openssl/commit/4072a762664020524f536361a6de43e8de19a4f8)
- Implement OSSL_PROVIDER_get0_default_search_path function, and add documentation and tests. (Architecture-related: public API)
  ↳ No PR: [d3db25f](https://github.com/openssl/openssl/commit/d3db25f568087bc9dc89b6720f0b4213cd5585c3)
- Added two error codes PROV_R_INVALID_MEMORY_SIZE and PROV_R_INVALID_THREAD_POOL_SIZE and their corresponding error description strings in the provider error system. (Architecture-related: public API)
  ↳ No PR: [232dd87](https://github.com/openssl/openssl/commit/232dd87c55f66ecae906299cbea1ea7782241b64)
- Add KMAC support to KBKDF, and extend the input key and context size limit to 512 bytes. (Architecture-related: external behavior)
  ↳ No PR: [211c47c](https://github.com/openssl/openssl/commit/211c47ca1b1ac129dcee59d383cae44e36532bb9), [bbbd121](https://github.com/openssl/openssl/commit/bbbd1210b43d7a7aff60ccc3c92561beaf6b2bb3)
- ECDSA and DSA signing contexts can now retrieve the OSSL_SIGNATURE_PARAM_NONCE_TYPE parameter. (Architecture-related: public API)
  ↳ No PR: [1d85794](https://github.com/openssl/openssl/commit/1d857945324810f43a302c9d062c617207093387)
- Add option to force EMS check in TLS1_PRF KDF for FIPS module. (Architecture-related: FIPS configuration)
  ↳ No PR: [50ea5cd](https://github.com/openssl/openssl/commit/50ea5cdcb735916591e35a04c1f5a659bf253ddc)
- Add keymgmt import/export type function extension with provider context, so that provider can dynamically return parameter array according to configuration and maintain backward compatibility. (Architecture-related: public API)
  ↳ No PR: [5e3b845](https://github.com/openssl/openssl/commit/5e3b84505e44377b183e7529dab7585674b83936)
- Add macro OSSL_DISPATCH_END as the end marker of OSSL_DISPATCH array. (Architecture-related: public API)
  ↳ No PR: [23e6489](https://github.com/openssl/openssl/commit/23e648962e04af132c0841bec950b8a89b87fb2d), [1e6bd31](https://github.com/openssl/openssl/commit/1e6bd31e58dba0bb5d7f21cf1fe1e0d9e4ee3c30)
- Added support for SHA256/192 hash algorithm, which is a variant of SHA256 output truncated to 192 bits. (Architecture-related: public API)
  ↳ No PR: [81bafac](https://github.com/openssl/openssl/commit/81bafac5cbbd195ff9c53a06aaca7c3eacbb2fc0)
- Add limited random number support to WebAssembly WASI target, based on getentropy implementation. (Architecture-related: platform compatibility)
  ↳ No PR: [d88a0f5](https://github.com/openssl/openssl/commit/d88a0f5f3944535dd83d55bedc4d239544c5678d)
- Added OSSL_PROVIDER_load_ex function, which supports passing parameters when loading provider; reconstructed related loading functions. (Architecture-related: public API)
  ↳ No PR: [9d2f7e1](https://github.com/openssl/openssl/commit/9d2f7e1f611f03e65f25adf08b76e08821b315da)
- Add dupctx support for aes-gcm, aes-ccm, aria-gcm and aria-ccm cryptographic implementations, by copying the context and fixing the internal key pointer. (Architecture-related: public API)
  ↳ No PR: [0239fb3](https://github.com/openssl/openssl/commit/0239fb3db77e9de2031c5054854cba8e417c1b72)
- FIPS self-test uses test RNG instead, avoids relying on real random number generators, and keeps DRBG settings original for subsequent replacement of seed sources. (Architecture-related: FIPS self-test)
  ↳ No PR: [fffa78c](https://github.com/openssl/openssl/commit/fffa78c2fd01accd97c9229018d4c380f7a20335)
- Add the association of ECDSA and SHA3 hash functions in the object cross-reference table to support the ECDSA with SHA3 signature algorithm. (Architecture-related: public API: ECDSA with SHA3 signature algorithm support)
  ↳ No PR: [98e0755](https://github.com/openssl/openssl/commit/98e0755511fbb5e2563dfe0017f011803d57f51d), [de4aa81](https://github.com/openssl/openssl/commit/de4aa81faaaddcacf0608166406d07bcd641e92b)
- Add user cleaning callbacks for random number entropy and nonce, and update the cleaning function to give priority to user-provided callbacks. (Architecture-related: public API: Nonce entropy cleaning callback)
  ↳ No PR: [5516d20](https://github.com/openssl/openssl/commit/5516d20226c496c2b22fa741698b4d48dad0428f)
- Changed the settable parameters of BLAKE2b digest from OSSL_DIGEST_PARAM_XOFLEN to OSSL_DIGEST_PARAM_SIZE, added digest size validity check, and added support for retrievable parameters. (Architecture-related: public API parameter changes)
  ↳ No PR: [6a0ae39](https://github.com/openssl/openssl/commit/6a0ae393dd554eb718e5148696e8f437d4faae5b)
- Reconstruct the check logic for the consistency of the destination connection ID of the data packet in the QUIC receiving path to avoid use-after-free vulnerabilities caused by incorrect format of the first data packet. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [0f7b5cc](https://github.com/openssl/openssl/commit/0f7b5cc9f3d487641dd5f4003e0be88fb2111e98)
- Fixed an issue where QUIC channels failed to properly handle delayed packets after generating a new key at the handshake layer, making sure to recheck the receive queue after getting the new key. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [4e64437](https://github.com/openssl/openssl/commit/4e64437a5fdf5c8ff1b5c2cede6c358a19a28e85)
- Fixed the reference counting and release logic of BIO in the QUIC front-end I/O API, transferred the release responsibility from QUIC_CHANNEL to QUIC_CONNECTION, and renamed related functions to reflect the ownership change. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [d1ac77b](https://github.com/openssl/openssl/commit/d1ac77b1a50b070aa55384f4c5eff3df71adb2c7)
- Fixed the implementation of SSL_get_error in the QUIC front-end I/O API and adjusted the order of QUIC error checking. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [e30c502](https://github.com/openssl/openssl/commit/e30c502ae930295b889cce7375a83a8c742c68b4)
- Fixed the WANT_READ signal problem of SSL_read in the QUIC front-end I/O API to ensure that the WANT_READ error is correctly returned when no data is read in non-blocking mode. (Architecture event: SSL_Protocol_Engine module change)
  ↳ No PR: [af8b52c](https://github.com/openssl/openssl/commit/af8b52cffe303c41510d1228605f9fcff9af0ee3)
- Fixed the problem of false errors caused by unregistered scheme in OSSL_STORE_open_ex(). (Architecture-related: public API)
  ↳ No PR: [7c64ca7](https://github.com/openssl/openssl/commit/7c64ca71c2ceeb1d47e8499bd351de7d0078ce37)
- Fixed the type incompatibility problem of VMS code under x86_64 cross-compiler. (Architecture-related: platform compatibility)
  ↳ No PR: [9150ca6](https://github.com/openssl/openssl/commit/9150ca6017f8654e671bd7d7d1b494ce1ce3fa0d)
- When SM2 uses an invalid digest, an error will now be reported correctly to avoid silent failure. (Architecture-related: External behavior: SM2 signature)
  ↳ No PR: [d5d95da](https://github.com/openssl/openssl/commit/d5d95daba59adc41ab60ea86acd513f255fca3c0)
- Fixed the DER encoder output structure of EC and SM2, removing incorrect public key serialization logic. (Architecture-related: DER encoding behavior)
  ↳ No PR: [2d49519](https://github.com/openssl/openssl/commit/2d49519210ed60ed16778b4b1097b4c6880541e5)
- Change the OSSL_provider_init function declaration from extern to OPENSSL_EXPORT to ensure correct export on Windows systems. (Architecture-related: public API)
  ↳ No PR: [d977a26](https://github.com/openssl/openssl/commit/d977a26ed8ca5066d4d72a6d73f1669c8619f4a1)
- Fixed scope of extern "C" blocks in C++ wrappers to ensure function declarations are wrapped correctly. (Architecture-related: public API)
  ↳ No PR: [1bfd20f](https://github.com/openssl/openssl/commit/1bfd20f08c042072cae44a9eb81626cbfff81116)
- The EC_GROUP_new_from_params function in the FIPS module no longer supports explicit elliptic curve parameters, only accepts named curves, and returns the new error code EC_R_EXPLICIT_PARAMS_NOT_SUPPORTED. (Architecture-related: public API)
  ↳ No PR: [638c3a2](https://github.com/openssl/openssl/commit/638c3a28af45bd81a1c90b81efd8e10449eace1b), [5313746](https://github.com/openssl/openssl/commit/53137462f42f8673fbd5b0831f8ea051ddea509f)
- Fix the processing logic of URI in the SSL_CERT_DIR environment variable, and add the SSL_CERT_URI environment variable as the default certificate URI source. (Architecture-related: certificate loading behavior)
  ↳ No PR: [021859b](https://github.com/openssl/openssl/commit/021859bf810a3614758c2f4871b9cd7202fac9b2)
- Fix undefined behavior of CMAC, GMAC, HMAC and SipHash when EVP_MAC is reinitialized, ensure correct reinitialization, and disable Poly1305 from reusing keys. (Architecture-related: external behavior)
  ↳ No PR: [c9ddc5a](https://github.com/openssl/openssl/commit/c9ddc5af5199909d196ee80ccd7abcff2eb42a34)
- Introduce a reservation mechanism for OSSL_METHOD_STORE, and solve the race conditions in multi-threaded concurrent construction methods by adding independent large locks. (Architecture-related: internal architecture)
  ↳ No PR: [e1eafe8](https://github.com/openssl/openssl/commit/e1eafe8c87612a94552e9ad5df56c489cb6f0ff2)
- Fix the locale initialization problem and ensure that the string comparison function works correctly; remove the dependence on the locale code and directly implement the strcasecmp and strncasecmp functions. (Architecture-related: platform compatibility)
  ↳ No PR: [92d0501](https://github.com/openssl/openssl/commit/92d050167713f9a094c149c38435b07512c68936), [f505be9](https://github.com/openssl/openssl/commit/f505be999f00232702aeb6918e4a1ffa0b9b588b), [fb4cdca](https://github.com/openssl/openssl/commit/fb4cdca053fb9d3f0e11eeaf31f4b4ff87f69a95)
- Fixed default key length regression for Blowfish CFB and OFB ciphers, corrected from 64 bits to 128 bits. (Architecture-related: Blowfish default key length)
  ↳ No PR: [7a9e93d](https://github.com/openssl/openssl/commit/7a9e93dda58118c0fb1bade8fe915306b845325b)
- Fix DSA, DH, EC and RSA key export routines to ensure success is not incorrectly returned when parameter assignment fails. (Architecture-related: Key Management Module)
  ↳ No PR: [46c1c2d](https://github.com/openssl/openssl/commit/46c1c2d7fa9153da4eb5e1aefd7b0139dc507c00)
- Fixed the build failure caused by the lack of SIZE_MAX macro definition in kdf_exch.c, and added the necessary header file inclusion. (Architecture-related: platform compatibility)
  ↳ No PR: [c6010d1](https://github.com/openssl/openssl/commit/c6010d1a1020223274de39e3ce25643b33dac80d)
- Adjust the random number seed generation method for the OpenVMS platform, using timestamp plus sequence number instead of high-precision time function. (Architecture-related: platform compatibility)
  ↳ No PR: [7056dc9](https://github.com/openssl/openssl/commit/7056dc9c50baa4af5152c625c4735806d51c67cd)
- Fix the padding problem of Keccak implementation on s390x platform, use intermediate message digest calculation instead and manually handle Keccak padding. (Architecture-related: platform compatibility)
  ↳ No PR: [086d88a](https://github.com/openssl/openssl/commit/086d88a637ecf537af62260e16d4e0011dbb8d1b)
- Fixed the endianness problem in the AES-GCM-SIV implementation, replaced the byte exchange function and corrected the mulx_ghash processing logic under the big-endian architecture. (Architecture-related: Platform compatibility: Big-endian architecture)
  ↳ No PR: [6f74677](https://github.com/openssl/openssl/commit/6f74677911de87f3271721073bd360806a93733f)
- Limit the maximum block size of symmetric ciphers to 2^30 bytes, and fix possible crashes and infinite loops caused by differences in sizeof(long) and sizeof(size_t). (Architecture-related: public API behavior restrictions)
  ↳ No PR: [709d4be](https://github.com/openssl/openssl/commit/709d4be78f64a8ba0707fb5682b90039e848dad4)
- Fixed an issue on s390x where IKM was not used correctly when generating X25519 and
  ↳ No PR: [d12b824](https://github.com/openssl/openssl/commit/d12b824ddaee502400c19bf8c32e1ada3111fc50)
- Make CRYPTO_secure_malloc() correctly trigger the ERR_R_MALLOC_FAILURE error when memory allocation fails. (Architecture-related: public API)
  ↳ No PR: [9167a47](https://github.com/openssl/openssl/commit/9167a47f78159b0578bc032401ab1d66e14eecdb)
- Stopped reporting ERR_R_MALLOC_FAILURE directly in most places, instead reported more specific subsystem error codes, and fixed related custom malloc wrapper issues. (Architecture-related: public API)
  ↳ No PR: [e077455](https://github.com/openssl/openssl/commit/e077455e9e57ed4ee4676996b4a9aa11df6327a6)
- Fixed the propagation of error return values in BN_check_prime(), ensuring that internal functions correctly return -1 when returning an error, allowing callbacks to abort primality testing or key generation. (Architecture-related: public API)
  ↳ No PR: [0b38676](https://github.com/openssl/openssl/commit/0b3867634f74f6cb7b60b3a0adde396421207214)
- Fixed an issue where the CMS_decrypt_set1_* series of functions incorrectly added misleading error queue entries in case of non-receiver mismatch. (Architecture-related: public API: CMS_decrypt_set1_*)
  ↳ No PR: [60ea150](https://github.com/openssl/openssl/commit/60ea150b1f535e4f0c76e23af4130b3861fabf54)
- Add a check for memory allocation failure in the SRP_VBASE_init function to catch potential memory errors in time. (Architecture-related: public API: SRP_VBASE_init)
  ↳ No PR: [f44d32f](https://github.com/openssl/openssl/commit/f44d32fdfbd2a249dae74dc24478f31fca69d288)
- Fixed the problem of make update failure due to error code number conflict, and adjusted the error code number of SSL_R_SEQUENCE_CTR_WRAPPED. (Architecture-related: public API)
  ↳ No PR: [3c153d8](https://github.com/openssl/openssl/commit/3c153d8722d52ac6faa0d98873060272e5f160ea)
- Fix SSL_alloc_buffers and SSL_free_buffers functions to make them work properly again. (Architecture-related: public API)
  ↳ No PR: [7eb39ec](https://github.com/openssl/openssl/commit/7eb39ecb299db3eade11946f9385f5dee1d458d3)
- Check whether the private key exists before calling the eddsa signature function, and add relevant test cases to cover scenarios such as missing private keys, short keys, etc. (Architecture-related: external behavior)
  ↳ No PR: [f5a10d5](https://github.com/openssl/openssl/commit/f5a10d5cc19215ab22be55b4a2ee1e41bd38fb14)
- Fixed the problem that the selection parameters were not propagated correctly when exporting the key, ensured that no attempt was made to export the private key when only the public key was required, and the caching mechanism was updated to avoid misuse of incomplete information in subsequent operations. (Architecture-related: public API)
  ↳ No PR: [98642df](https://github.com/openssl/openssl/commit/98642df4ba886818900ab7e6b23703544e6addd4)
- Fixed the problem of obtaining the PSS salt length from the provider, resolved the inconsistency between the provider's interpretation of magic constants and the OpenSSL core, and added related tests. (Architecture-related: provider and core compatibility)
  ↳ No PR: [5a3bbe1](https://github.com/openssl/openssl/commit/5a3bbe1712435d577bbc5ec046906979e8471d8b)
- Fixed the issue where EVP_KDF_CTX_get_kdf_size() incorrectly returns 0 when SSKDF is used in combination with KMAC, and now returns SIZE_MAX correctly. (Architecture-related: public API)
  ↳ No PR: [e8add4d](https://github.com/openssl/openssl/commit/e8add4d379075a6daef2591edd830297d469b9f4)
- Fixed an issue when implementing Keccak XOF via CPACF on the s390x platform, simulating XOF behavior by using empty input blocks for single block operations. (Architecture-related: Platform compatibility)
  ↳ No PR: [76aa4f3](https://github.com/openssl/openssl/commit/76aa4f3ac0d76e58f2111cbf87ae7f25c8766190)
- It is forbidden to create DSA and DH keys with missing parameters. Parameters must be provided when importing the key; the decoder no longer creates DSA keys with missing parameters. (Architecture-related: external behavior)
  ↳ No PR: [9ac82e2](https://github.com/openssl/openssl/commit/9ac82e2e7225759c21e712cba6dfe8da22ef7e47), [604247b](https://github.com/openssl/openssl/commit/604247bf75571c1c3fb6a1723346c61acd957221)
- Fixed the Ed448 pre-hash function on the S390X platform, which falls back to the non-accelerated implementation when pre-hashing is performed. (Architecture-related: platform compatibility)
  ↳ No PR: [f225fbf](https://github.com/openssl/openssl/commit/f225fbf9521395aff86e85883db9bcb083eab154)
- Remark X25519 and X448 as FIPS-approved algorithms, restoring their use in FIPS mode. (Architecture-related: FIPS compliance)
  ↳ No PR: [8948b57](https://github.com/openssl/openssl/commit/8948b5749410084ed1dfabf17a90df65efcf0f82)
- The IV length of ChaCha20-Poly1305 must now be 12 bytes, truncation is no longer supported, and passing in other lengths will return an error. (Architecture-related: public API: IV length constraints)
  ↳ No PR: [a011523](https://github.com/openssl/openssl/commit/a01152370676e7e11fb461cff8628eb50fa41b81)
- Fixed the issue where when setting the key length and IV length in EVP_CIPHER_CTX_ctrl, if the value is the same as the current one, the call to the underlying provider will be skipped. (Architecture-related: public API)
  ↳ No PR: [eb52450](https://github.com/openssl/openssl/commit/eb52450f5151e8e78743ab05de21a344823316f5)
- Sort related stacks before multiple lookup operations to ensure correctness, involving X509 storage, EVP_PBE_find_ex, provider lookup, X509_policy_check, X509V3_EXT_get_nid and X509_TRUST_get_by_id. (Architecture-related: public API)
  ↳ No PR: [3ef5b60](https://github.com/openssl/openssl/commit/3ef5b6009767aeff2fea47144af36cd13bd19d6d), [fb7a7f0](https://github.com/openssl/openssl/commit/fb7a7f099ecbabbf65c42856ec9fb9d898b15907), [07f9c81](https://github.com/openssl/openssl/commit/07f9c81d20f2c972dd454e2343634586d3aa88a1), [efe0222](https://github.com/openssl/openssl/commit/efe0222f5c9e07167aeac80d4d5e3d67aa8f1f36)
- Fixed the parameter verification error in the EVP_MD_CTX_get_params function, and corrected the incorrectly called function pointer to the correct get_ctx_params. (Architecture-related: public API)
  ↳ No PR: [b501df3](https://github.com/openssl/openssl/commit/b501df3cefebcdaaeb7d6480b7a7b82d68927873)
- In PBKDF2 key derivation and PKCS12 MAC generation, ignore EVP_MD_fetch fetch errors when using legacy algorithms to avoid error stack contamination. (Architecture-related: external behavior)
  ↳ No PR: [dc4ccc7](https://github.com/openssl/openssl/commit/dc4ccc70245be870e2ef2e382d16234673bf28cf)
- Fixed the problem that the decoder did not pass the property query parameters (propq) correctly, and added a settable context parameter interface for all decoders to ensure that internal functions can use the incoming property query parameters. (Architecture-related: decoder interface)
  ↳ No PR: [39ed763](https://github.com/openssl/openssl/commit/39ed7636e0d8a90512e7ccb811cd0bfcb7a79650)
- Disable the spliced AES-GCM implementation on the PPC32 architecture, as this implementation is not available. (Architecture-related: Platform compatibility)
  ↳ No PR: [44957a4](https://github.com/openssl/openssl/commit/44957a49329135163a4138b1877ccf7f899d19b9)
- Fixed the problem of data loss caused by selecting value 0 when exporting/importing keys after decoding. Now all selection flags will be used. (Architecture-related: External behavior: Key export)
  ↳ No PR: [2acb0d3](https://github.com/openssl/openssl/commit/2acb0d363c0032b5b97c4f6596609f40bd7d842f)
- Fixed the memory leak problem of OSSL_DECODER_CTX_new_for_pkey() function in the wrong path. (Architecture-related: public API)
  ↳ No PR: [3d254b3](https://github.com/openssl/openssl/commit/3d254b31344e82b8f10fda8bab196757a377eb63)
- Avoid sending CONNECTION_CLOSE frames repeatedly and clear the pending flag after sending. (Architecture-related: QUIC protocol behavior)
  ↳ No PR: [0b31072](https://github.com/openssl/openssl/commit/0b31072e086dc9a53f62cec60ea8d565320e640a)
- Fixed the problem of failing to return SSL_ERROR_ZERO_RETURN correctly when FIN has been received but the buffer is empty in QUIC reading, to avoid SSL_read blocking for too long. (Architecture-related: public API: SSL_read behavior fix)
  ↳ No PR: [72622c0](https://github.com/openssl/openssl/commit/72622c0b9637667cfef3692e5a63b90d637f0c72)
- Adjusted the error handling when creating QUIC streams, updated the error code value of the stream count limit, and changed the related error reporting from non-IO errors to abnormal errors. (Architecture-related: public API)
  ↳ No PR: [96fe5e5](https://github.com/openssl/openssl/commit/96fe5e5f964d44dfff8667fb3c0111a25be58c87)
- Fixed the QUIC stream backpressure condition, changed the related error type from abnormal error to non-I/O error, and updated the corresponding error code; added QUIC_RAISE_NON_IO_ERROR error macro. (Architecture-related: public API)
  ↳ No PR: [7a5f58b](https://github.com/openssl/openssl/commit/7a5f58b2cf0d7b2fa0451603a88c3976c657dae9), [8ee3ee1](https://github.com/openssl/openssl/commit/8ee3ee10e39fd6fe1323187c63ce41460bd4f9d4)
- Fixed a merge error caused by function renaming in the quic-multi-stream.c example, updated SSL_set_initial_peer_addr() to SSL_set1_initial_peer_addr(). (Architecture-related: public API)
  ↳ No PR: [dac42bd](https://github.com/openssl/openssl/commit/dac42bdce1ed19e646c2adf04b27fc92a9d0e374)
- Implemented dupctx method for chacha20 cipher, supports EVP_PKEY_CTX_copy function, and correctly handles deep copies of tlsmac pointers to avoid double free. (Architecture-related: public API)
  ↳ No PR: [61cfc22](https://github.com/openssl/openssl/commit/61cfc22b60e33bc77b1e1944759af48c8e58f0d2), [df93b3c](https://github.com/openssl/openssl/commit/df93b3c9e72571876bd01e5a50a5ba8368c6c77f)
- SSL_clear in QUIC is no longer a no-op, instead it returns an error and reports that it is not supported. (Architecture-related: public API)
  ↳ No PR: [b139f7a](https://github.com/openssl/openssl/commit/b139f7a26d0158e42b0f4b9e7364111a8fd17fa2)
- Fix the problem of seed source usage in the FIPS module, ensuring that the seed source requested by the user is used instead of the default value. (Architecture-related: FIPS seed source behavior)
  ↳ No PR: [4cde758](https://github.com/openssl/openssl/commit/4cde7585ce8eb53682256ba79e6af1949498fbfe)
- Remove C11 _Static_assert related macro definitions and their usage to solve compatibility issues on some platforms. (Architecture-related: Platform compatibility)
  ↳ No PR: [fc785a5](https://github.com/openssl/openssl/commit/fc785a554cc37dfa94710b28ced45b03006f0300)
- Fixed a memory leak issue caused when the FIPS provider is used in different threads, ensuring that the main thread is registered to receive thread stop notifications. (Architecture-related: FIPS provider thread safety)
  ↳ No PR: [be203ea](https://github.com/openssl/openssl/commit/be203ea3d3a60a881993d1f7552084996d34ba0a)
- Fixed an issue with inconsistent printing behavior of EVP_PKEY_print_private in OpenSSL 3.0, now only prints the part that the backend considers a private key component, and adjusted the output logic of DSA and ECX encoders to match expected behavior. (Architecture-related: public API)
  ↳ No PR: [1296c2e](https://github.com/openssl/openssl/commit/1296c2ec7866a4f2f4d210432c771142e8de33a0)
- Fixed an issue where encryption operations did not return errors correctly after the key was not set or the key length was changed. (Architecture-related: Encryption behavior)
  ↳ No PR: [e7cb211](https://github.com/openssl/openssl/commit/e7cb2117c9ccc0d531d521e45ae780be669e4ffc)
- Corrected the value of macro definition OSSL_SIGNATURE_PARAM_NONCE_TYPE to make it consistent with the document. (Architecture-related: public API)
  ↳ No PR: [a534200](https://github.com/openssl/openssl/commit/a5342007e7832cbd427fb62af24998f81d20c5f6)
- Removed the redundant copy of the key scheduling pointer in PROV_GCM_CTX, and fixed the failure problem of evp_test under new CPUs on Windows. (Architecture-related: platform compatibility)
  ↳ No PR: [143ca66](https://github.com/openssl/openssl/commit/143ca66cf00c88950d689a8aa0c89888052669f4)
- Add RC4 macro definition and rc4_md5_enc function prototype for libcrypto and liblegacy. (Architecture-related: public API)
  ↳ No PR: [58e8af4](https://github.com/openssl/openssl/commit/58e8af4cecd23dbea2e6b061ab68190b38d64145)
- Update the reference counting operation in the store module to a structure-based atomic operation. (Architecture-related: public API)
  ↳ No PR: [2a1f467](https://github.com/openssl/openssl/commit/2a1f467cb9e00d7b6c437443d6414370f3e6ff40)
- Extract declarations of FIPS option functions into separate header files. (Architecture-related: public API)
  ↳ No PR: [30ab774](https://github.com/openssl/openssl/commit/30ab774770a7e8547b0d6363b63a73cc80f33a7b)
- Avoid dynamically loading old providers on the NonStop platform to prevent crashes, and adjust test conditions. (Architecture-related: platform compatibility)
  ↳ No PR: [8bb5568](https://github.com/openssl/openssl/commit/8bb55680e46c868b0aa09682c2bef954231841b5)
- Add tests for OSSL_PROVIDER_load_ex, and update existing tests to support the new API parameters. (Architecture-related: public API)
  ↳ No PR: [4f3e3d9](https://github.com/openssl/openssl/commit/4f3e3d9d3cb9632a8263cfe27ff11f342bf93351)
- Optimize AES-GCM performance for p9+ ppc64le platform, introduce splicing method and add relevant macro definitions and function declarations. (Architecture-related: platform compatibility)
  ↳ No PR: [44a563d](https://github.com/openssl/openssl/commit/44a563dde1584cd9284e80b6e45ee5019be8d36c)
- Use SM4 hardware instructions on ARM processors to optimize SM4 algorithms, improving performance by about 8 to 40 times. (Architecture-related: Platform compatibility: ARM SM4 hardware acceleration)
  ↳ No PR: [15b7175](https://github.com/openssl/openssl/commit/15b7175f558bf9eb057ec3266685486f727dd70f)
- Added an optimized implementation of SM4 based on ASIMD instructions for the ARM platform (N1/V1 microarchitecture), which can improve performance in parallel modes such as ECB, CTR, GCM and CBC decryption, and added VPSM4-related key settings and encryption and decryption functions. (Architecture-related: Platform compatibility: ARM ASIMD SM4 acceleration)
  ↳ No PR: [4908787](https://github.com/openssl/openssl/commit/4908787f21f4f5fa24b721ed3ebbc4d3e93ef70c)
- Optimize the KMAC algorithm on the s390x architecture, by manually filling the last data block and using the kimd instruction to achieve hardware acceleration, improving performance by 2 to 3 times; at the same time, using the klmd instruction to optimize keccak XOF processing, accelerating multi-result block scenarios. (Architecture-related: Platform compatibility: s390x)
  ↳ No PR: [affc070](https://github.com/openssl/openssl/commit/affc070aabc930aeaba50f0dd6b3e0b7a2ddc399), [de13699](https://github.com/openssl/openssl/commit/de13699370183ab565f548267afa57e25a921ca9)
- Enable hardware-accelerated SHA3 absorption function on ARMv8.2-compatible Apple CPU, and the performance of large block data processing is improved by about 36%. (Architecture-related: ARMv8.2 hardware acceleration)
  ↳ No PR: [f6484de](https://github.com/openssl/openssl/commit/f6484de23df5f04e1f9fa8418e942c45c1a65578)
- Added AESE instruction optimization and VPSM4 hardware acceleration support for the SM4 algorithm on the ARMv8 platform, and reconstructed the key initialization logic of XTS mode. (Architecture-related: Platform compatibility: ARMv8 SM4 hardware acceleration)
  ↳ No PR: [c007203](https://github.com/openssl/openssl/commit/c007203b94b6921ebc8103cb7ae51af554c86afe)
- Optimize GCM context parameter acquisition and setting, use TRIE-based fast search to replace linear search, and enhance status verification when IV length changes. (Architecture-related: GCM parameter API)
  ↳ No PR: [e84b5fc](https://github.com/openssl/openssl/commit/e84b5fcc1b1d599173eaab07790c06a532981e50)
- Introduced a new option RSA_PSS_SALTLEN_AUTO_DIGEST_MAX for RSA-PSS signature and set it as the default value to comply with FIPS 186-4. (Architecture-related: public API)
  ↳ No PR: [6c73ca4](https://github.com/openssl/openssl/commit/6c73ca4a2f4ea71f4a880670624e7b2fdb6f32da)
- According to the release of FIPS 186-5, update the approval status of EdDSA (Ed25519 and Ed448) in FIPS mode: first marked as unapproved, and then remarked as approved. (Architecture-related: FIPS compliance)
  ↳ No PR: [9fa5532](https://github.com/openssl/openssl/commit/9fa553247874728cee8ca0ece9aaed476eb0f303), [09627a8](https://github.com/openssl/openssl/commit/09627a8ceb69e19d2855b36228f44a3660af177a), [8c02b98](https://github.com/openssl/openssl/commit/8c02b98fab688b0ccacbb2de5816a5d5fc7fb23b)
- Rolled back the change that marked EdDSA as a FIPS-approved algorithm, re-marking it as unapproved in the FIPS provider. (Architecture-related: FIPS algorithm status change)
  ↳ No PR: [759ab59](https://github.com/openssl/openssl/commit/759ab5984eb981f2dd165979a7abb950ddad81ae)
- Limit the digest algorithms that can be used by HMAC and Hash DRBG in FIPS mode, allowing only SHA1, SHA2-256, SHA2-512, SHA3-256, SHA3-512. (Architecture-related: FIPS digest algorithm restrictions)
  ↳ No PR: [f553c0f](https://github.com/openssl/openssl/commit/f553c0f0dd24f037f31d971a99a1ffe7a11f64e6), [7a3d32a](https://github.com/openssl/openssl/commit/7a3d32ae4602eb4d09c6d998b2b1ba4b81ec1f54)
- When changing the IV length, the previously set IV is invalidated, which enhances the security of password implementation. (Architecture-related: external behavior)
  ↳ No PR: [6941eb4](https://github.com/openssl/openssl/commit/6941eb4d86661488faa3b5c07fc80cfc84ed8934)
- Updated FIPS build instructions to guide how to build a compliant FIPS provider and use it with the latest version. (Architecture-related: FIPS build instructions)
  ↳ No PR: [2b42290](https://github.com/openssl/openssl/commit/2b42290f08c0a75695021aeb7d5cd16068b3edc3)
- Repair VMS installation, add check for the existence of built-in provider in IVP script. (Architecture-related: VMS installation verification repair)
  ↳ No PR: [0c5307e](https://github.com/openssl/openssl/commit/0c5307ef4b1dea6dc2796cf08e84035e3d3a4510)
- Fixed the build problem in Cygwin environment by conditionally including the Windows.h header file. (Architecture-related: Platform compatibility: Cygwin build fix)
  ↳ No PR: [9b9c42d](https://github.com/openssl/openssl/commit/9b9c42db3b7e7807e0d3311356fb0316af085171)
- Added continuous integration support to the Cygwin environment, and corrected the reference format of Windows header files. (Architecture-related: Platform compatibility: Cygwin CI support)
  ↳ No PR: [e3b01eb](https://github.com/openssl/openssl/commit/e3b01eb6b25e76d4832d81023d056948edc2cb36)
- Fixed the problem of SHA3 build failure when there is no assembly mode on the ARM64 platform. (Architecture-related: platform compatibility)
  ↳ No PR: [46b43c9](https://github.com/openssl/openssl/commit/46b43c9f98771139735656e541c8f4c8018c2667)
- Fixed extra semicolons in ossl_rsa_pss_get_param_unverified, dh_validate_private and dh_validate_public, and used DH_check_pub_key_ex instead of DH_check_pub_key in dh_validate_public. (Architecture-related: public API changes)
  ↳ No PR: [d715dbd](https://github.com/openssl/openssl/commit/d715dbd8e566e7827ce8b2e9b6687c2bcd8a89a0)
- Give priority to using the GNU library initialization mechanism, and advance the definition of __attribute__((constructor)) and __attribute__((destructor)) to improve platform compatibility. (Architecture-related: platform compatibility)
  ↳ No PR: [2dc3a4a](https://github.com/openssl/openssl/commit/2dc3a4a4a57eca0d9bebd87234c7d682506188fc)
- Reconstruct the internal header file structure, clean up inclusion and migrate common macros. (Architecture-related: internal interface reconstruction)
  ↳ No PR: [f2a6f83](https://github.com/openssl/openssl/commit/f2a6f83862be3e20260b708288a8f7d0928e9018), [af16097](https://github.com/openssl/openssl/commit/af16097febcd4fa31cd5fcd05ad09cf8b53659ea)
- Limit #pragma comment(lib, "bcrypt.lib") to the MSVC compiler to avoid unknown pragma warnings generated by other compilers. (Architecture-related: platform compatibility)
  ↳ No PR: [695cb63](https://github.com/openssl/openssl/commit/695cb63c744bab090144a86949b68324ee3094d6)
- Adjust the preprocessor conditions of the xlclang compiler on the AIX platform to ensure that the correct initialization and cleanup mechanism is used. (Architecture-related: platform compatibility)
  ↳ No PR: [df1e33b](https://github.com/openssl/openssl/commit/df1e33bc8ae67573a3f3488eff82e02fc0310203)

### Cross-cutting / Other Architecture-related Changes
- Migrate the logging function in the HTTP server to an independent log module and clean up the related code. (Architecture-related: log module is independent)
  ↳ No PR: [8a2ec00](https://github.com/openssl/openssl/commit/8a2ec00d7f4bc34ca9111561699ec5ac03a3923e)
- Default security level increased from 1 to 2. (Architecture-related: security level)
  ↳ No PR: [b3a33da](https://github.com/openssl/openssl/commit/b3a33dac8880b88038083b64d234506659921436)
- Fixed aarch64 endian macro definition error in arm_arch.h. (Architecture-related: platform compatibility)
  ↳ No PR: [40c24d7](https://github.com/openssl/openssl/commit/40c24d74deaad8a0ad7566a68ea5ea757bc3ccef)
- Normalize the return values of multiple encryption and X.509 APIs to ensure that non-negative integers are returned. (Architecture-related: public API)
  ↳ No PR: [dd1f284](https://github.com/openssl/openssl/commit/dd1f28427b375931fda45180619c8f5971cd6bca)
- The asn1parse command adds three new input formats: PEM, DER and B64. PEM is used by default, and the original -strictpem option is abandoned to maintain backward compatibility. (Architecture-related: command line input format)
  ↳ No PR: [ca857d7](https://github.com/openssl/openssl/commit/ca857d7332d042142ced23b37fdd1d52dbf152b9), [34df960](https://github.com/openssl/openssl/commit/34df960a75aeb85b97e5ac70465275c2057ee1a3)
- Added checks for multiple unknown options in option initialization, and added a function to set unknown_name. (Architecture-related: public API)
  ↳ No PR: [2c27244](https://github.com/openssl/openssl/commit/2c2724476ef50b8926b033f009bdfc85ac3f1816)
- Added app_conf_try_number function to simplify the acquisition of configuration values and unify error handling mode. (Architecture-related: new public function app_conf_try_number)
  ↳ No PR: [b778268](https://github.com/openssl/openssl/commit/b77826877be3bdd56e3e86887cb78ea010db90be)
- Allow clients to connect to HTTP servers via IPv6. (Architecture-related: Platform compatibility)
  ↳ No PR: [830b6a1](https://github.com/openssl/openssl/commit/830b6a13f9aecd42da61b79c93f236575cc58793)
- Removed restriction on cross-signing self-signed certificates, now allows cross-signing self-signed certificates. (Architecture-related: Certificate behavior)
  ↳ No PR: [7f4cc3b](https://github.com/openssl/openssl/commit/7f4cc3bc34e2fc1acf2abf1f2d791855c446c611)
- Added fallback implementations for UINT32_C and UINT64_C macros to support different 64-bit processor ABIs. (Architecture-related: Platform compatibility)
  ↳ No PR: [09a4b4b](https://github.com/openssl/openssl/commit/09a4b4b72204f973804d60096c513f5ed6b39e4f)
- Added support for BSD-ppc, BSD-ppc64, BSD-ppc64le and s390 z16 architectures. (Architecture-related: Platform compatibility)
  ↳ No PR: [f5485b9](https://github.com/openssl/openssl/commit/f5485b97b6c9977c0d39c7669b9f97a879312447), [42f111a](https://github.com/openssl/openssl/commit/42f111ad41141e2ecd67f0a6954625a5ad01890b)
- When OPENSSL_NO_QUIC_THREAD_ASSIST is defined, the quic_thread_assist.c file is no longer compiled. (Architecture-related: build and installation methods)
  ↳ No PR: [1a2a0e1](https://github.com/openssl/openssl/commit/1a2a0e1dc88bf905a7997e12de08a4b45f9db53c)
- Introduce HAS_PREFIX() and CHECK_AND_SKIP_PREFIX() macros, replace manual string prefix checking, fix boundary processing and add auxiliary functions. (Architecture-related: public API)
  ↳ No PR: [2ff286c](https://github.com/openssl/openssl/commit/2ff286c26c29b69b02ca99656d26d2f8cfd54682)
- Fix the HTTP server port output format, reconstruct the socket address acquisition logic, adjust the OCSP responder function signature to remove the port parameter. (Architecture-related: public API)
  ↳ No PR: [4599ea9](https://github.com/openssl/openssl/commit/4599ea9fe31953c0c50738ed4b91ade76a693356)
- Fixed the problem of handling AKID and SKID extensions according to configuration, refactored logic to support none option and suppression of self-signed certificates. (Architecture-related: configuration option changes)
  ↳ No PR: [adbd77f](https://github.com/openssl/openssl/commit/adbd77f6d7cc4efb7b4bde483036fab8e48ce870)
- Fixed compilation errors caused by AT_SECURE not being declared on Debian's kfreebsd kernel. (Architecture-related: Platform compatibility)
  ↳ No PR: [3a1fa01](https://github.com/openssl/openssl/commit/3a1fa0116a92235ba200228e4bb60d6a3a7f4113)
- Fixed the problem of EC public key export using compressed format by default, changing it to uncompressed format by default, and following the format parameters set by the user. (Architecture-related: public API)
  ↳ No PR: [a16e866](https://github.com/openssl/openssl/commit/a16e86683e8d76c4b9268d757c584b5c971db728)
- Fix the EVP_PKEY_eq() function to correctly handle keys containing only the private key component, and adjust the match function of the DH, DSA, EC, ECX and RSA key management implementations to relax selector bit interpretation. (Architecture-related: public API)
  ↳ No PR: [f3ba626](https://github.com/openssl/openssl/commit/f3ba62653815b2f7991103cdbea1ac155c8c916a), [ee22a37](https://github.com/openssl/openssl/commit/ee22a3741e3fc27c981e7f7e9bcb8d3342b0c65a), [edc8566](https://github.com/openssl/openssl/commit/edc8566f475d63278d5f85cd25f324cf2fe9aaf9)
- Fixed an issue reported by Coverity: check the return value during zlib compression/decompression initialization and return an error on failure; fixed logical dead code in EVP_DigestSignFinal. (Architecture-related: public API)
  ↳ No PR: [73a815d](https://github.com/openssl/openssl/commit/73a815defe428e42ccc27fdc9d5be507f980278b), [182cc64](https://github.com/openssl/openssl/commit/182cc644b3a3690bddfecba925486fefa421d6ec)
- The x509 tool returns a non-zero exit code when the certificate IP/Email/host name verification fails, and the verification logic is restructured to unify error handling. (Architecture-related: exit code behavior)
  ↳ No PR: [9567fd3](https://github.com/openssl/openssl/commit/9567fd3819398c6be70508dd6316046da0955b71)
- Fixed the problem of proxy environment variables being ignored due to callback design flaws in the use of HTTPS proxy, and adjusted the proxy judgment logic. (Architecture-related: proxy behavior)
  ↳ No PR: [068549f](https://github.com/openssl/openssl/commit/068549f8db6d792a88bb888118001c4582f79074)
- Fixed the problem of incorrectly canceling keep-alive when parsing non-200 status code responses in OSSL_HTTP_REQ_CTX_nbio(), and adjusted the error checking order. (Architecture-related: public API)
  ↳ No PR: [38288f4](https://github.com/openssl/openssl/commit/38288f424faa0cf61bd705c497bb1a1657611da1)
- Fix the check of port parameters in proxy mode in the OSSL_HTTP_set1_request() function to make it consistent with the documentation: when using HTTP proxy, the server address must be provided, and the port is an optional parameter. (Architecture-related: public API)
  ↳ No PR: [266383b](https://github.com/openssl/openssl/commit/266383b44c4ebce5ddf551547e73ab6eec47805b)
- Fixed the bug that openssl req -x509 cannot generate certificates from CSR, now supports using the -CA and -CAkey options to generate CA-signed certificates, and added regression tests. (Architecture-related: external behavior)
  ↳ No PR: [df5c86e](https://github.com/openssl/openssl/commit/df5c86e9f80d14d699bad4c8889292fd9b4bd7ba)
- Fix wincrypt.h symbol conflict, adjust preprocessing instructions in types.h and add build test. (Architecture-related: platform compatibility)
  ↳ No PR: [3c58d44](https://github.com/openssl/openssl/commit/3c58d447497b37f7b4f458aaa2956a7e226c6d65)
- Add necessary header include for NonStop platform to support fixed size integer types. (Architecture-related: Platform compatibility)
  ↳ No PR: [ec26144](https://github.com/openssl/openssl/commit/ec26144288fd6dce6dd76bd9e2b192b495033723)
- Fixed the problem of incorrect EVP_CIPHER_CTX_ctrl return value check, and changed the original Boolean value judgment to the correct numerical comparison. (Architecture-related: public API behavior repair)
  ↳ No PR: [d649c51](https://github.com/openssl/openssl/commit/d649c51a5388912277dffb56d921eb720db54be1)
- Fix dsaparam and gendsa commands to support -provider and -propquery options, and update related help text. (Architecture-related: command line interface)
  ↳ No PR: [30b2c35](https://github.com/openssl/openssl/commit/30b2c3592e8511b60d44f93eb657a1ecb3662c08), [4380686](https://github.com/openssl/openssl/commit/438068674b95b38892d2d1790b3fd14e3112d0cb)
- Fixed the issue where the decoded-from-explicit flag of the EC group was lost when moving across providers. Now the flag will be exported correctly during serialization. (Architecture-related: cross-provider behavior)
  ↳ No PR: [95a6fbd](https://github.com/openssl/openssl/commit/95a6fbdf0d112582b9ad56f8d42ec92b1ec4787d)
- Fixed the problem that the -provider and -propquery options in multiple command line tools (dhparam, ecparam, pkeyparam, dgst, genrsa) did not take effect. (Architecture-related: public command line interface)
  ↳ No PR: [ae3c30a](https://github.com/openssl/openssl/commit/ae3c30acac17271693e91dcae42c804cd96e8f93), [2b8f687](https://github.com/openssl/openssl/commit/2b8f687d7627a4b15bba6a820825944185980376), [0185538](https://github.com/openssl/openssl/commit/0185538799803a1a98823f42ac2402ede04f56da), [653a770](https://github.com/openssl/openssl/commit/653a7706781ebbe8a6a4b84d29b39d001c395ffe), [b2ccfd8](https://github.com/openssl/openssl/commit/b2ccfd81025fa115f1138123b9aa61657e779352)
- Clarify that six operations are mutually exclusive in the smime command, and add a check to prevent multiple operations from being specified at the same time. (Architecture-related: smime command behavior)
  ↳ No PR: [2786160](https://github.com/openssl/openssl/commit/2786160731257540a957216aeb6431970bbce95f)
- Fix SHUT_RD and SHUT_WR macro definitions on Windows platform, and add missing header file references. (Architecture-related: platform compatibility)
  ↳ No PR: [4ccb89b](https://github.com/openssl/openssl/commit/4ccb89bba76655d72285f94619f2f4014319d3d9)
- Replace BIO_free(bio_err) with BIO_free_all(bio_err) to correctly handle the BIO chain that may be returned in a VMS environment. (Architecture-related: platform compatibility)
  ↳ No PR: [a73bdc2](https://github.com/openssl/openssl/commit/a73bdc24e14760413a65d478d7c88356b4b95bb5)
- Fixed an issue where the public key was mistakenly considered required when using PEM_read_bio_PrivateKey_ex, now the public key becomes optional when requesting a private key. (Architecture-related: public API behavior)
  ↳ No PR: [adb408d](https://github.com/openssl/openssl/commit/adb408dc791e83f59f3a86bd90d8e804c814ac30)
- Change the thread pool support function to be compiled only when the thread pool is enabled, and fix related issues. (Architecture-related: build and installation methods)
  ↳ No PR: [f5a3669](https://github.com/openssl/openssl/commit/f5a3669c8bc9cd1ea00f2bb7d058a752e6d2f152)
- Fix the compilation warning caused by using OSSL_PARAM_construct_uint on platforms where uint32_t is defined as unsigned long int, use OSSL_PARAM_construct_uint32 instead. (Architecture-related: platform compatibility)
  ↳ No PR: [1e065a1](https://github.com/openssl/openssl/commit/1e065a15119520e13a2d68d003c4c06869208a32)
- Remove unnecessary cancellation status and type settings in POSIX threads, and fix Android compilation failure problem. (Architecture-related: platform compatibility)
  ↳ No PR: [14c593e](https://github.com/openssl/openssl/commit/14c593e0034ddb9ca68f4a8e06b251afa127c6d0)
- Fix the problem of HPKE test failure when chacha20 or poly1305 is disabled, fix the conditional compilation macro. (Architecture-related: build conditions)
  ↳ No PR: [36b4d7a](https://github.com/openssl/openssl/commit/36b4d7a69836fdf0ede1ea00879b26047bf93056)
- Fixed multiple issues related to EC and RSA encryption algorithms, including buffer size, key type conversion, parameter translation and digest initialization. (Architecture-related: public API)
  ↳ No PR: [9107087](https://github.com/openssl/openssl/commit/91070877adb905f51eb4b19b730d42fc257bae13), [43d5dac](https://github.com/openssl/openssl/commit/43d5dac9d00ac486823d949f85ee3ad650b62af8), [be6497a](https://github.com/openssl/openssl/commit/be6497aa208948c960a28363bac98a429677bd9d), [c5aa719](https://github.com/openssl/openssl/commit/c5aa719502f1ef456b27347e5f7b15c07817da4e), [3410a72](https://github.com/openssl/openssl/commit/3410a72dce57651e08d5d2143409cde0205a8f3b)
- Fixed bugs related to atomic operations and thread disabling, and added atomic loading function. (Architecture-related: internal API)
  ↳ No PR: [5da3e02](https://github.com/openssl/openssl/commit/5da3e02c5eaac2bec9c14165d62874b1232213fe), [629b408](https://github.com/openssl/openssl/commit/629b408c12c56b2c9e3279de8658718e8dd658a2)
- Fix the macro attribute conflict with cmocka, replace __attribute__((malloc)) in OSSL_CRYPTO_ALLOC macro with __attribute__((__malloc__)). (Architecture-related: public API)
  ↳ No PR: [0bf7e94](https://github.com/openssl/openssl/commit/0bf7e94c10f1b00510b8a36cdcbedc02a66468be)
- Fix the no-autoload-config option so that it no longer automatically loads the configuration during engine and provider lookup, and correct the locking mechanism of provider lookup. (Architecture-related: Engine and provider lookup)
  ↳ No PR: [cb8e641](https://github.com/openssl/openssl/commit/cb8e64131e7ce230a9268bdd7cc4664868ff0dc9)
- Fixed warnings caused by using the %n format specifier when cross-compiling, and rewritten path splicing logic. (Architecture-related: platform compatibility)
  ↳ No PR: [2e40770](https://github.com/openssl/openssl/commit/2e40770aa55cde037fd4ef63e1a3de09cd5ca124)
- Add conditional compilation in test files to support CHACHA-free build environments. (Architecture-related: build compatibility)
  ↳ No PR: [681c461](https://github.com/openssl/openssl/commit/681c461910b1b72af263ec735bac1310b2fadcd0)
- Deprecated OPENSSL_LH_stats series of functions, and migrated internal LHASH definitions to new macros. (Architecture-related: public API: OPENSSL_LH_stats deprecated)
  ↳ No PR: [5317b6e](https://github.com/openssl/openssl/commit/5317b6ee1fc3db20de5976fbb46cc49a45c0768a)
- Standardize the progress callbacks of dhparam, dsaparam and other tools, and delete their independent callback implementations. (Architecture-related: public API: Standardization of progress callbacks)
  ↳ No PR: [e1cd94f](https://github.com/openssl/openssl/commit/e1cd94f2dca4056ce042c62b89c468dffc088033)
- Move the e_os.h header file to the include/internal directory, and update the include paths in all source files. (Architecture-related: internal header file migration)
  ↳ No PR: [d5f9166](https://github.com/openssl/openssl/commit/d5f9166bacfb3757dfd6117310ad54ab749b11f9)
- Unified RISC-V extended test macros, replacing RV32I_* and RV64I_* macros with unified RISCV_HAS_* macros. (Architecture-related: platform compatibility)
  ↳ No PR: [86c69fe](https://github.com/openssl/openssl/commit/86c69fe84118f0dca656d9bfc1131052e2a8e9b8)
- Document the unexpected behavior of shared library pinning during static builds in the installation documentation, and provide solutions using the no-shared and no-pinshared configuration options. (Architecture-related: build and installation methods)
  ↳ No PR: [ce451fb](https://github.com/openssl/openssl/commit/ce451fb86141fedad607bd68840639b06616047e)
- Updated RC4_CHAR and RC4_INT documentation to indicate that they should no longer be used for new configuration targets. (Architecture-related: Configuration Contract)
  ↳ No PR: [c2a8226](https://github.com/openssl/openssl/commit/c2a8226cba2757b251729620aedffeed23d73623)
- Optimize the configuration script and only update the file when the content of configdata.pm changes to avoid unnecessary source code reconstruction. (Architecture-related: Build configuration optimization)
  ↳ No PR: [764cf5b](https://github.com/openssl/openssl/commit/764cf5b26306a8712e8b3d41599c44dc5ed07a25)
- Fix the VMS installation script and uniformly use platform->shlib_version_as_filename() to obtain the shared library version file name. (Architecture-related: VMS platform compatibility)
  ↳ No PR: [93b670a](https://github.com/openssl/openssl/commit/93b670abd104468db4478b79221c9c70613ba2f1)
- Fixed the problem of logical name undefinition and definition mismatch in VMS installation, ensuring that the shutdown script correctly cancels the engine directory logical name defined by the startup script. (Architecture-related: VMS installation script repair)
  ↳ No PR: [0df8e71](https://github.com/openssl/openssl/commit/0df8e71a6e32d0a993530b7f813603da3e7a6c4c)
- To support C++20 header-units, fixed the self-contained issue of header files: conditionally include stdio.h in multiple header files, and adjust the inclusion order of some header files to avoid including other header files within extern "C" blocks. (Architecture-related: public API)
  ↳ No PR: [eab9dbb](https://github.com/openssl/openssl/commit/eab9dbbdd1f102dc1a26549a77fcc5c167385cd5)
- Fix build issues on TANDEM and older POSIX systems, and allow locale support to be disabled via the -DOPENSSL_NO_LOCALE configuration option. (Architecture-related: Platform compatibility)
  ↳ No PR: [b98f989](https://github.com/openssl/openssl/commit/b98f989e0c741d7534a58ba3fb22f5af0f016ca4)
- Change the C version detection macro from __STRICT_ANSI__ to __STDC_VERSION__, and define the internal macro OSSL_NO_C99 based on this to handle pre-C99 compatibility issues. (Architecture-related: Build compatibility)
  ↳ No PR: [b1104a3](https://github.com/openssl/openssl/commit/b1104a3a2dd4351af85cf48f677691a414ffc3a2)
- Added test support for Alpine Linux (musl) in CI. (Architecture-related: Platform compatibility: Alpine Linux (musl)
  ↳ No PR: [e8cec34](https://github.com/openssl/openssl/commit/e8cec34c39cd2f30b98d1d98e9a297066c918ab3)
- Added a new Hybrid CRT (Hybrid CRT) build target for the Windows platform, and updated related documentation. (Architecture-related: build and installation methods)
  ↳ No PR: [18891ef](https://github.com/openssl/openssl/commit/18891efdf4813547bc4e5b3791ac7af72fa277c8)
- Added support for Clang 16 compiler in CI workflow. (Architecture-related: Platform compatibility)
  ↳ No PR: [6de73f5](https://github.com/openssl/openssl/commit/6de73f5d795b74815740088274069b8778264bb8)
- Modify the util/wrap.pl.in script to unify the behavior of platforms such as VMS, and remove the no longer needed util/local_shlib.com.in and util/unlocal_shlib.com.in files. (Architecture-related: build and installation methods)
  ↳ No PR: [1939ee7](https://github.com/openssl/openssl/commit/1939ee7f252ffebd91c29384db4133290489e026)
- Added no-apps build option to disable the building of applications (such as openssl program), and updated related documentation and CI configuration. (Architecture-related: Build configuration: no-apps option)
  ↳ No PR: [ff88545](https://github.com/openssl/openssl/commit/ff88545e02ab48a52952350c52013cf765455dd3)
- Added an alternate definition of socklen_t for the VMS platform to address the lack of this type in the current VMS C header files. (Architecture-related: Platform compatibility)
  ↳ No PR: [3ae4686](https://github.com/openssl/openssl/commit/3ae4686bf6cfb9889efeecbc8e80b279afbe1e28)
- When building on NonStop platforms, exclude references to the poll.h header file because it is not defined for that platform. (Architecture-related: Platform compatibility)
  ↳ No PR: [aff9922](https://github.com/openssl/openssl/commit/aff99225f946d8f538b5e0cb95fc65d5cd36b99b)
- Improve coverage mapping, remove support for OpenSSL 1.1.1 stable version, and expand compilation configurations for other branches to enhance test coverage. (Architecture-related: build and installation methods)
  ↳ No PR: [798d69c](https://github.com/openssl/openssl/commit/798d69c8670283bdea5c39b03ff573d0c6a6b9fc)
- Add support for win-arm64 platform in Windows build instructions. (Architecture-related: Platform compatibility: win-arm64)
  ↳ No PR: [288e968](https://github.com/openssl/openssl/commit/288e9680399d3a755861d309058dda2fb48af8bf)
- Added build tasks using brotli and zstd in the CI configuration, and added Windows compression test workflow. (Architecture-related: build dependency: brotli/zstd)
  ↳ No PR: [b540aae](https://github.com/openssl/openssl/commit/b540aae97d6b80f9040874b9c56259a85ba46f36)
- Made multiple adjustments to the cross-compilation CI workflow, including disabling specific tests, adjusting optimization levels, disabling warnings, adding CPU capability settings and adding RISC-V extension configuration. (Architecture-related: platform compatibility)
  ↳ No PR: [fecae60](https://github.com/openssl/openssl/commit/fecae608a9ad366a1bc740ad94628520cdf38d25), [200d952](https://github.com/openssl/openssl/commit/200d9521a0d406a7d02778d1c6c5a5230caeecf5), [8b63a30](https://github.com/openssl/openssl/commit/8b63a305bf2db0e980cb76040fa66a17f781d6c7), [af0a4c4](https://github.com/openssl/openssl/commit/af0a4c46846323fc33f713b5ccd758a526c19ed0), [e787c57](https://github.com/openssl/openssl/commit/e787c57c538d0922004e49a10be0d403af773272)
- Adjusted multiple build options and configurations in the CI workflow, including enabling QUIC, adding no-rfc3779, enabling more options, adding thread pool options, falling back to no-modules, and adding ubsan support. (Architecture-related: QUIC support)
  ↳ No PR: [b7873f9](https://github.com/openssl/openssl/commit/b7873f92b0f79bdf576795c86d6520656568d672), [a09adac](https://github.com/openssl/openssl/commit/a09adac311975afcb5ad099b2e1cfc7eb1e72865), [c267588](https://github.com/openssl/openssl/commit/c267588fd400593c090ebb24643c2be5158bfbcc), [b137219](https://github.com/openssl/openssl/commit/b1372197496650c3cb318cade911a3bd6af14adc), [b71b953](https://github.com/openssl/openssl/commit/b71b9534c423eaae79378556337e466a7dec8e35), [1ca61aa](https://github.com/openssl/openssl/commit/1ca61aa56090356bbdbb16cf48916fbd9886c78d)
- Add extern "C" declaration to hpke.h and thread.h header files to support correct inclusion in C++ code. (Architecture-related: public API: C++ compatibility)
  ↳ No PR: [ed5c0df](https://github.com/openssl/openssl/commit/ed5c0dfdf4f2d386fadfadcd8692a521061c772d)
- Removed the call to the internal function err_free_strings_int() and left the empty implementation to maintain compatibility. (Architecture-related: Compatibility: public API compatibility)
  ↳ No PR: [1c8787d](https://github.com/openssl/openssl/commit/1c8787d5e0b01bedfc3cbe5eab5b85290221d8c1)
- Update OpenSSL version references, update all references to OpenSSL 3.1 in the master branch to 3.2, including deprecated macros and API level checks. (Architecture-related: public API compatibility)
  ↳ No PR: [45ada6b](https://github.com/openssl/openssl/commit/45ada6b92bc7e31772d95ab9dcb0e7d2a764cf20)
- Disable printf format checking on the MinGW platform and fix related compilation issues. (Architecture-related: platform compatibility)
  ↳ No PR: [a1de5eb](https://github.com/openssl/openssl/commit/a1de5eb88479515535e5de090ded800455c3d4a7)
- Replaced header include from <stdint.h> to <openssl/e_os2.h> to be compatible with older compilers that do not support C99. (Architecture-related: Platform compatibility)
  ↳ No PR: [7bc5ce4](https://github.com/openssl/openssl/commit/7bc5ce4a79c61ab7238b188f9af48f41ff1392f9)

### Engine Plugin Framework
- Added {lib}_R_{lib}_LIB error library reference support for external modules such as engines, and implemented the corresponding error library initialization function in the e_capi engine. (Architecture-related: public API)
  ↳ No PR: [79c8dcf](https://github.com/openssl/openssl/commit/79c8dcf3985a7b75eac8e53eb8652728af6c5d3d)
- Remove the conditional compilation of ENGINE related categories in trace categories, so that all categories always exist, and optimize the category search logic. (Architecture-related: public API)
  ↳ No PR: [78bd646](https://github.com/openssl/openssl/commit/78bd646b2f6a18cf8515e05a5f3efadff03b3920)
- Add SP800-56Br2 6.4.1.2.1 (3.c) requirement for RSA key pair checking, ensuring key length is a positive even number. (Architecture-related: RSA key pair checking standard)
  ↳ No PR: [8b26854](https://github.com/openssl/openssl/commit/8b268541d9aabee51699aef22963407362830ef9)
- Add comments for deprecated macros to indicate that they are no longer valid starting from OpenSSL 3.0. (Architecture-related: public API: deprecated macro description)
  ↳ No PR: [79704a8](https://github.com/openssl/openssl/commit/79704a88eb5aa70fa506e3e59a29fcda21f428af)
- Fixed the problem that EVP_CIPHER_CTX_copy in the dasync engine cannot correctly copy the cipher context. (Architecture-related: public API: EVP_CIPHER_CTX_copy)
  ↳ No PR: [a0cbc2d](https://github.com/openssl/openssl/commit/a0cbc2d222743fc4ffd276b97bd5f8aeacf01122)
- Fixed an issue where the engine would crash when using a different OpenSSL runtime due to applying static linking to libcrypto/libssl, by preventing the engine's libcrypto from installing the atexit handler. (Architecture-related: Platform compatibility)
  ↳ No PR: [9362a1b](https://github.com/openssl/openssl/commit/9362a1b32b7330e24d3bca230b412557caea095b)
- When dynamically loading the engine, detect whether the engine is linked to OpenSSL 1.1.x (by checking the EVP_PKEY_base_id symbol), and if so, abort the load to avoid a crash. (Architecture-related: Platform compatibility)
  ↳ No PR: [14db620](https://github.com/openssl/openssl/commit/14db620282bea38dc44479e562cf9bb61a716444)
- Improved the detection logic of traditional keys when the engine loads private keys. (Architecture-related: public API)
  ↳ No PR: [2b74e75](https://github.com/openssl/openssl/commit/2b74e75331a27fc89cad9c8ea6a26c70019300b5)
- Update the reference counting operation of the engine module to a structure-based atomic operation, and add inline functions. (Architecture-related: public API)
  ↳ No PR: [e362070](https://github.com/openssl/openssl/commit/e3620700a7d7dd772508768f51e892788e39a950)
- Fixed enginetest failure when compiling with deprecated API disabled and specified API version 1.1.1, added missing header include. (Architecture-related: platform compatibility)
  ↳ No PR: [29af9fb](https://github.com/openssl/openssl/commit/29af9fba64fd3e4e086808f2360501b463627ea2)

## Routine Changes

### New features
- Socket now displays the target address when connecting.
  ↳ No PR: [994fa5f](https://github.com/openssl/openssl/commit/994fa5f9861df94c07699cb118ad5c5470a868b2)
- Enable UTF-8 name option by default, set -nameopt utf8 as default behavior.
  ↳ No PR: [86cfd13](https://github.com/openssl/openssl/commit/86cfd132ffc4f6198cc640a29c293850c0a59914)
- Added -ktls command line option to s_client to enable Kernel TLS functionality.
  ↳ No PR: [e396c11](https://github.com/openssl/openssl/commit/e396c114eb7233e24ba6a920606cfdd6bc6cff7c)
- Added -ktls option to s_server to enable KTLS, and made -sendfile option dependent on -ktls; also added -tfo, -cert_comp, -enable_server_rpk, -enable_client_rpk and -zerocopy_sendfile options.
  ↳ No PR: [e2ef7f1](https://github.com/openssl/openssl/commit/e2ef7f1265e727567e8963aa2756a387a621ef71)
- Support for sending new extensions in the certificate request message, and the client can echo these extensions in the certificate message.
  ↳ No PR: [cbb862f](https://github.com/openssl/openssl/commit/cbb862fbaaa1ec5a3e33836bc92a6dbea97ceba0)
- Allow empty or missing summary parameters to be passed in core_obj_add_sigid, and updated related documentation and tests.
  ↳ No PR: [4f71624](https://github.com/openssl/openssl/commit/4f716249643fe97a2bdf59a11cc10e1bef8103e9)
- Enable the -sans option of CMP applications to support email addresses (rfc822Name type).
  ↳ No PR: [03ee2e5](https://github.com/openssl/openssl/commit/03ee2e5b1ecd1832d99d07fc459ecf62f5a0b168)
- Add wrap mode to enc command, brotli/zstd compression support, configurable salt length, and allow printing only keys and IVs when no input file is available.
  ↳ No PR: [7850cc8](https://github.com/openssl/openssl/commit/7850cc8307b9105f37dde864d5c8c881c522b28a), [f4f397a](https://github.com/openssl/openssl/commit/f4f397a5cb5b6eec3045047b9406a43fdd6d6602)
- Implemented AES-256-CTR encryption algorithm in dasync engine.
  ↳ No PR: [bd363ef](https://github.com/openssl/openssl/commit/bd363ef32403d58a8b41553b5abd602b30073b10)
- Enable tracing for HTTP clients, output request and response headers, and dump response content on error.
  ↳ No PR: [e8fdb06](https://github.com/openssl/openssl/commit/e8fdb0603572bf051dad6abc56291cdf1313a905)
- Added request and response tracking logging functionality to the APPS HTTP server, restructured log output and normalized error messages.
  ↳ No PR: [8aff29f](https://github.com/openssl/openssl/commit/8aff29f020752c96cc2ab7d111d9c33aaf55c671)
- x509 tools generate random serial numbers when using the -CA option without specifying -CAserial or -CAcreateserial, and improve serial number loading error handling.
  ↳ No PR: [ec8a340](https://github.com/openssl/openssl/commit/ec8a3409487c871b440fa52bff7c3ef33378494a)
- Add a warning for x509 applications when the -CA option is not specified and when options such as -CAkey are ignored.
  ↳ No PR: [c54a6a4](https://github.com/openssl/openssl/commit/c54a6a4b0ef664313fb07617d6a8c26a808719e0)
- Add the function of printing the recommended private key length in the DH key text output, and change the key selection condition from public key to key pair.
  ↳ No PR: [ff54094](https://github.com/openssl/openssl/commit/ff54094cb9e1e5033f6e3e72717e741cf24f5c29)
- Added -macsaltlen option to pkcs12 command, allowing user to specify MAC salt length, and updated default salt length.
  ↳ No PR: [e393064](https://github.com/openssl/openssl/commit/e393064ee78a7ea07e2d63493579eab95384afe4), [4c56539](https://github.com/openssl/openssl/commit/4c56539cb338f1583289f93379ee254b45b66568)
- Added interactive reconnect command C to s_client, allowing users to disconnect and reconnect to the server at any time during the session.
  ↳ No PR: [511c491](https://github.com/openssl/openssl/commit/511c49189ef600d41f44cd7c5d204e9ea27b5f48)
- Add configuration option support for speed command, and introduce CONF variable for reading configuration.
  ↳ No PR: [8403c73](https://github.com/openssl/openssl/commit/8403c7350fd836ea44baf69c0b7dc3af1189253f)
- Added ossl_time_muldiv utility function in time module.
  ↳ No PR: [364c3b7](https://github.com/openssl/openssl/commit/364c3b7b1ac3172dbe2108be23ae215b86ef8e08)
- Added -mlock option to speed command, which locks the throughput measurement buffer to memory to reduce paging effects. This feature is only supported on Linux and Windows.
  ↳ No PR: [9710d72](https://github.com/openssl/openssl/commit/9710d72b95f4fc218ed613f42dc90ad0d263b14f)
- Added --all-algorithms option to list command to list all available algorithm categories.
  ↳ No PR: [35b6707](https://github.com/openssl/openssl/commit/35b670702466b91b3baa724635e5aecbc2061fa7)
- Added a limit on the number of delayed datagrams for the QUIC record layer receiver, and added related configuration parameters.
  ↳ No PR: [0ff9813](https://github.com/openssl/openssl/commit/0ff98137445ec63249eed3c1e40cf01dc5190c65)
- Applied the configured maximum send fragment length in the write record layer, and adjusted the buffer allocation logic.
  ↳ No PR: [435d88d](https://github.com/openssl/openssl/commit/435d88d70813825533c8789faa71c6287e0d43c9)
- Added a new encryption post-processing step function, which is used to add MAC and other operations after encryption, and reconstructed the related write record function to call this new function.
  ↳ No PR: [2a354d5](https://github.com/openssl/openssl/commit/2a354d54632cccf7d76130712d068a3ef188a356)
- Added is_empty function for list data structure and added corresponding tests.
  ↳ No PR: [b6f1b05](https://github.com/openssl/openssl/commit/b6f1b059eefb493d02913e9b32bd267d9017ee73)
- Added a function to obtain PTO duration for QUIC ACKM.
  ↳ No PR: [4ed9e0a](https://github.com/openssl/openssl/commit/4ed9e0a1e36eaa8f07a4a5371f9d13912a3f9da8)
- Added encoder/decoder for connection ID to QUIC transport parameters and made the ID field optional.
  ↳ No PR: [a64d824](https://github.com/openssl/openssl/commit/a64d82485d52c6ae1075217e611a92522fbe6560)
- Add the function of re-injecting URXE and checking pending URXE to QUIC demux, fix the return value logic of the injected function, and reconstruct the operation logic of the pending URXE list.
  ↳ No PR: [93e9b6c](https://github.com/openssl/openssl/commit/93e9b6cc4e2b47a5fb32f093c38b7963e9c270aa), [64222fc](https://github.com/openssl/openssl/commit/64222fc0274a88a6f42d5600c4bfdf57eeb40155)
- Add server-side state machine support to QUIC DHS, refactor the original client-side state machine code into an independent function, and introduce error status handling.
  ↳ No PR: [b83cf3f](https://github.com/openssl/openssl/commit/b83cf3fcf1149326f215cffd37f5c9725a4b61de)
- Added error reason text for QUIC channel transmission parameter processing, and added server-side support.
  ↳ No PR: [3c567a5](https://github.com/openssl/openssl/commit/3c567a52c25980f99a7353457d6285dc633f366b)
- Add basic server-side support for QUIC channels, including functions such as handling new connections, reset tokens, TLS clocks, receive preprocessing and forged packet limit checks.
  ↳ No PR: [b1b06da](https://github.com/openssl/openssl/commit/b1b06da2a3968abc552c1a440cba1b91bd6e34c2)
- Implemented the QUIC test server module, added interfaces for creation, release, connection status and handshake status query, and optimized resource release logic.
  ↳ No PR: [51a168b](https://github.com/openssl/openssl/commit/51a168b804be963e320c5515656301d25ea48322)
- Add the option to specify the number of subprime q bits during DSA key generation through command line parameters for the dsaparam command, and optimize the context initialization and error handling of parameter generation and key generation.
  ↳ No PR: [535ddd3](https://github.com/openssl/openssl/commit/535ddd37524217143eb710bc880ee8c60b7a6cf8)
- Add a help function for the genpkey command line tool that displays the pkeyopt parameter type and value.
  ↳ No PR: [2c1ec72](https://github.com/openssl/openssl/commit/2c1ec72a7abb29f2d91eda6f93942670f1cbdb9e)
- Change HKDF's info buffer to dynamic allocation, remove the fixed size limit and increase the upper limit.
  ↳ No PR: [e8115bd](https://github.com/openssl/openssl/commit/e8115bd1654d5cd7718109679b2047ca573083a8)
- Public key checking is implicitly enabled when the -pubin option is specified.
  ↳ No PR: [3b1c0c8](https://github.com/openssl/openssl/commit/3b1c0c8f3cd66e80f81a9b7c9810bdada39363f2)
- Added condition variable waiting function ossl_crypto_condvar_wait_timeout with timeout, supporting POSIX and Windows platforms.
  ↳ No PR: [2b2b267](https://github.com/openssl/openssl/commit/2b2b26788e7e46abb8fb340d49a088184fbc0b9b)
- Add a lock mechanism to the QUIC front end to ensure multi-thread safety.
  ↳ No PR: [a848925](https://github.com/openssl/openssl/commit/a8489257e69fab643d22932dfa27afb945e78c5a)
- Allow the caller to determine whether an ACK-eliciting packet has been sent, and add related tests.
  ↳ No PR: [134b79c](https://github.com/openssl/openssl/commit/134b79c0568457415bdceba03cb355fd746166fc)
- Implement QUIC thread auxiliary core functions, including stopping, waiting for stopping, cleaning and notification of deadline changes.
  ↳ No PR: [9f7acf0](https://github.com/openssl/openssl/commit/9f7acf071c363ed8cb5012e122e1e60447b45c78)
- Add QUIC protocol support to the s_client tool, including command line options, I/O multiplexing and sending FIN functions.
  ↳ No PR: [f34e5d7](https://github.com/openssl/openssl/commit/f34e5d7a12775ce2fb84e4c5d8b830b5a9f06566), [c4f74e7](https://github.com/openssl/openssl/commit/c4f74e7fc90b02cbee59b46783222467b48491ff)
- Optimize the timing of QUIC channel creation, create channels in advance, and store initial flow control parameters.
  ↳ No PR: [23c0470](https://github.com/openssl/openssl/commit/23c047090cde899059fb7489e1a35124ca7b5e8a), [0815b72](https://github.com/openssl/openssl/commit/0815b725a83da10f60c60d679a88b616da01cecf)
- The fipsinstall tool adds -no_drbg_truncated_digests and -pedantic options to control DRBG digest and strict FIPS mode.
  ↳ No PR: [b345dbe](https://github.com/openssl/openssl/commit/b345dbed28701f8aab06b0271603186127499928), [bc2a422](https://github.com/openssl/openssl/commit/bc2a4225a4a03f70bb0154a72c2889aa80c1b0f6), [d30fec6](https://github.com/openssl/openssl/commit/d30fec6ff438f73f4e255b0b9c6af3ea57ec122a), [c88e01a](https://github.com/openssl/openssl/commit/c88e01a961dacf638203017f922b27c3e23690fc)
- The openssl dgst -list command now also lists digest algorithms that are not available through the new API but are available through the old API.
  ↳ No PR: [7eab768](https://github.com/openssl/openssl/commit/7eab7680ee61c64b2ae7acd9dd199ab6734f3d1f)
- The CMP tool supports specifying the certificate to be revoked by the issuer and serial number, and improves the verification and warning logic of related options.
  ↳ No PR: [1d32ec2](https://github.com/openssl/openssl/commit/1d32ec20feae7320ddb2b929441688377b912a40)
- Added two auxiliary functions to the params module, which are used to allocate buffers and copy matching parameters, and allocate buffers and splice all matching parameters.
  ↳ No PR: [79523d5](https://github.com/openssl/openssl/commit/79523d55923e7f61104cc7269131fd6a975b579f)
- Added advanced command mode to s_client, commands are enclosed in curly braces {} and support parameters, while improving connection information output and user data processing.
  ↳ No PR: [d07b763](https://github.com/openssl/openssl/commit/d07b763bb9073945ba5e9912e56bc51fe18bdcb5)
- Added CRYPTO_GET_REF function to support querying the current reference count value and reconstructing related reference counting operations.
  ↳ No PR: [008a61a](https://github.com/openssl/openssl/commit/008a61a544e16d20595731f614b2fbc1d20f793e)
- Added support for --version and its synonyms for the openssl command line tool, and fixed the resource release method of the wrong output stream.
  ↳ No PR: [831ef53](https://github.com/openssl/openssl/commit/831ef5347253a9381c2ab6bd3ca74cbe10995939)
- Add setter functions for message callbacks and callback parameters to ensure that these values can be correctly propagated to QRX, QTX and TXP after channel creation.
  ↳ No PR: [5cf99b4](https://github.com/openssl/openssl/commit/5cf99b4040eb1ef63b3254090d16299cad690b1e)
- Add ERR_raise() calls to QUIC related functions to record errors in scenarios such as EVP call failure and improve error tracking capabilities.
  ↳ No PR: [cb19528](https://github.com/openssl/openssl/commit/cb19528b932d66e4e90c9365ed67acaec79fe9ad)
- Added the ability to set SSL_trace as a message callback for tserver, and restructured the internal structure to support SSL objects and thread safety.
  ↳ No PR: [cb93128](https://github.com/openssl/openssl/commit/cb931288730d3ad3e3a6ad9a9db13a8180d31ed9)
- The RSA key generation controls rsa_keygen_pubexp and rsa_keygen_primes now also apply to RSA-PSS keys.
  ↳ No PR: [e2c2cca](https://github.com/openssl/openssl/commit/e2c2cca4b2fd1ad946d93507e9ca4f9ea910a114)
- Functions get_rsa_payload_n, get_rsa_payload_e and get_rsa_payload_d now also support RSA-PSS keys.
  ↳ No PR: [cf71283](https://github.com/openssl/openssl/commit/cf712830b7b5a20a768a1fc5f78dc48841b7617f)
- Implemented broadcast support for condition variables on Windows XP, and added the creation, release, wait, timeout wait, signal and broadcast functions of condition variables.
  ↳ No PR: [425a780](https://github.com/openssl/openssl/commit/425a780462d387a81c83fd2b87d0efd91d6b154b)
- Added -saltlen option to OpenSSL's pkcs8 command line tool, allowing users to specify the salt value length.
  ↳ No PR: [9f679bd](https://github.com/openssl/openssl/commit/9f679bdc71aac83e89cc5aacb42855f3657ace39)
- Added -saltlen option to the OpenSSL enc command line tool, allowing users to customize the salt value length of PBKDF2 (default 16 bytes), replacing the previous fixed upper limit of 8 bytes.
  ↳ No PR: [e399458](https://github.com/openssl/openssl/commit/e3994583a1e4bde9a589c379520d216bc0a0c515)
- Added the -quiet option to the req command, and adjusted the progress point display behavior: displayed when -verbose, hidden when -quiet.
  ↳ No PR: [c1673a6](https://github.com/openssl/openssl/commit/c1673a60e40f6dcd110d1a4ff3e11a3297ada2da)
- Implemented polling descriptor-related control command processing in BIO_s_sock.
  ↳ No PR: [b79e73c](https://github.com/openssl/openssl/commit/b79e73cfba2f17cc810bde3c50a2a1d4f03b8cae)
- Added -outpubkey option to genpkey command to support outputting public key files separately.
  ↳ No PR: [6c03fa2](https://github.com/openssl/openssl/commit/6c03fa21ed4bbc9fd6d3013fdf9f4646d231f831)
- Replaced the jdkTrustedKeyUsage configuration option with the new -jdktrust command line option, which automatically enables -nokeys when specified.
  ↳ No PR: [21f7a09](https://github.com/openssl/openssl/commit/21f7a09ca256eee0ccc9a8fc498e8427469ab506)
- In QUIC connection closure information query, add support for the frame type that caused the closure.
  ↳ No PR: [55abe74](https://github.com/openssl/openssl/commit/55abe7486089ffa24b52e68a56b7eaed9a60a8ee)
- Updated the QUIC sample program to support specifying hostname and port via command line arguments, and added support for IPv6 addresses.
  ↳ No PR: [3b60efa](https://github.com/openssl/openssl/commit/3b60efa109a4637bf30d8d2b6067a5ea7151eff3), [3b86698](https://github.com/openssl/openssl/commit/3b866985ba8a85b85034eb01d6ad286db678bb13)
- Add fallback mechanism for key loading in store_result: when loading from the global key management object fails, try to get the key management object from the storage provider.
  ↳ No PR: [4cfcc7e](https://github.com/openssl/openssl/commit/4cfcc7e1213d39c78852a614894ebcd2e2be095c)
- Added --no-interactive option to s_client to support non-interactive mode operation.
  ↳ No PR: [bb2fb5d](https://github.com/openssl/openssl/commit/bb2fb5d7cc6c4abc888c3fd6df4366b6dfde25a6)
- Added -verbose and -quiet flags to dhparam, dsaparam, gendsa, genpkey and ca commands.
  ↳ No PR: [a414fd6](https://github.com/openssl/openssl/commit/a414fd6765bbc9bb0d630dbb4d780f44f825c8a2)
- Added -quiet parameter to -print_certs option of pkcs7 command.
  ↳ No PR: [632e8be](https://github.com/openssl/openssl/commit/632e8be2b570959dc3781c6956171e7e49f1aa58)
- Added -trace command line option to quicserver to enable communication tracing and output to standard error.
  ↳ No PR: [f430713](https://github.com/openssl/openssl/commit/f430713c8c5e579b513ffa16133b8c178978c5b6)
- Added priority queue implementation.
  ↳ No PR: [c8003ad](https://github.com/openssl/openssl/commit/c8003ad5e939a6c5fc0049c9b7ed1e99fbe9511b)
- Added ossl_quic_tx_packetiser_has_pending function for QUIC TXP.
  ↳ No PR: [04e5226](https://github.com/openssl/openssl/commit/04e5226f6549683a8362ae1af2445987d699540a)
- Add mutex lock for QUIC channel to support synchronous access in thread-assisted mode.
  ↳ No PR: [fb2245c](https://github.com/openssl/openssl/commit/fb2245c44b58b41a378eb47422221edd49ba9091)
- The tracing function now supports logging of sent datagrams.
  ↳ No PR: [8aff8f8](https://github.com/openssl/openssl/commit/8aff8f89f7bec3865b14b550a4c1a7ec7786e3f3)
- Changed the random output size parameter to long integer, and added block size selection.
  ↳ No PR: [2aa645b](https://github.com/openssl/openssl/commit/2aa645bca435759fa01e4e5827b7d93ad4e06673)
- The CMS demo program adds a prompt for operation success, and cms_ver.c adds a print signature time attribute.
  ↳ No PR: [7dc833c](https://github.com/openssl/openssl/commit/7dc833c2f659dfcd7ea4af951f045f93a0dbe30c)
- The DTLS test adds the cache and use of next epoch data packets, and a handshake scenario including HelloVerifyRequest.
  ↳ No PR: [e1c153d](https://github.com/openssl/openssl/commit/e1c153d31d4f913ebe2202a4bc20305919274d1f), [a29ad91](https://github.com/openssl/openssl/commit/a29ad912b82f50ef876bef99c66522dccd41b6f8)
- Added test case for all-zero RSA keys.
  ↳ No PR: [995eccb](https://github.com/openssl/openssl/commit/995eccb611431a4857cac3283e2442c01109d428)
- Fuzz testing adds checking of ASN1_item_i2d return value.
  ↳ No PR: [1cb35ce](https://github.com/openssl/openssl/commit/1cb35ce06a968dc82e7cd9502ecce8e89eca9580)
- Add unit tests to the event queue, and add an auxiliary function to simulate the current time.
  ↳ No PR: [0eb2765](https://github.com/openssl/openssl/commit/0eb27659435768d1a2370858d340a9c6793ed244)
- Add HMAC-SM3 test cases based on GM/T 0042-2015.
  ↳ No PR: [0648ec1](https://github.com/openssl/openssl/commit/0648ec1c35a54fb2b7ead34a215691fe9e38516d)
- The evp_test test framework adds thread support, and the maximum number of threads can be set through the Threads configuration item.
  ↳ No PR: [ae1792e](https://github.com/openssl/openssl/commit/ae1792e3d94bbd9f6c535f1784438011097adb4a)
- QUIC test extension supports session recovery functionality.
  ↳ No PR: [cf355bd](https://github.com/openssl/openssl/commit/cf355bd6e5564694e589d3f96e8bde192519649c)
- Added test to verify that PEM_read_bio_Parameters does not require a password when reading parameters.
  ↳ No PR: [df3d609](https://github.com/openssl/openssl/commit/df3d609030bdb0868d1ccca14227bb6829ad954c)
- qtest_shutdown adds blocking mode support, and test cases are used uniformly.
  ↳ No PR: [c9fb65b](https://github.com/openssl/openssl/commit/c9fb65b8c8b82a8aa60a118342ec4ee58352db89)
- Updated the ssltraceref reference file and added the function of saving new traces to ssltraceref-new.txt.
  ↳ No PR: [b7278ee](https://github.com/openssl/openssl/commit/b7278eea441cb70debfbbba350026e58ad41cb83)
- evp_test adds --provider and --propquery command line options.
  ↳ No PR: [1bebf4b](https://github.com/openssl/openssl/commit/1bebf4b0417303895a6cc350da97beb0d1534b60)
- Defer cipher context replication support in specific FIPS versions, update test version checks.
  ↳ No PR: [19937db](https://github.com/openssl/openssl/commit/19937db0f2769bc9e4882b476901e446eaadb384)
- Add test verification open_ex password checking function.
  ↳ No PR: [6412900](https://github.com/openssl/openssl/commit/64129008fb822758778f7dd29cec6a0a4582e4d2)
- QUIC test library adds timeout handling support.
  ↳ No PR: [a2026db](https://github.com/openssl/openssl/commit/a2026db2643db1e34cc25960e9ef74d08bcdee5a)
- Add BIO filter to split multiple packets in QUIC datagram, remove old read and write methods.
  ↳ No PR: [35bd8a6](https://github.com/openssl/openssl/commit/35bd8a60043bde500f777e465530076524d2534a)
- Added internal function ossl_X509_ALGOR_from_nid to simplify X509_ALGOR creation.
  ↳ No PR: [9944df1](https://github.com/openssl/openssl/commit/9944df112ffbe4b6855b6a9bf88720803277cc23)
- Added new internal function evp_generic_fetch_from_prov to get the EVP method from the specified provider.
  ↳ No PR: [2fd3392](https://github.com/openssl/openssl/commit/2fd3392c8f4e2f3481fa4d7e6a683dc19c6c1cd2)
- Added internal function evp_keymgmt_fetch_from_prov to obtain the key management method from the specified provider.
  ↳ No PR: [33561e0](https://github.com/openssl/openssl/commit/33561e0d5b89a06d1c03b952196d008b5014914a)
- Implement context copy operations for multiple KDF algorithms (PBKDF1, PBKDF2, HKDF, KBKDF, KRB5 KDF, scrypt, SSH KDF, SS KDF).
  ↳ No PR: [6585d3a](https://github.com/openssl/openssl/commit/6585d3aa7638c8cea2d4bb9f10e7298002f652e5), [0a10f71](https://github.com/openssl/openssl/commit/0a10f71d3071bae0183cd4277da64d100f6b48eb), [95bd5ff](https://github.com/openssl/openssl/commit/95bd5ff65985e992827f7178deda84d95b1e6f66), [d54c52c](https://github.com/openssl/openssl/commit/d54c52c28ebb780e2ffc5b7752d35359215cf0a6), [4c1a841](https://github.com/openssl/openssl/commit/4c1a841c3de645674ed2af92da25f7f5736fae1c), [cdcdcf5](https://github.com/openssl/openssl/commit/cdcdcf5c6fa382c879cb3503609519d56fa62e81), [59558f9](https://github.com/openssl/openssl/commit/59558f9d8824747024b6ab756f3798a577ecae48), [2722eec](https://github.com/openssl/openssl/commit/2722eeceaa993f4488b295a22d2e1178f5ba1ce1)
- Implement context replication for X942, PKCS12 and TLS1 PRF KDF, and add safe memory copy function.
  ↳ No PR: [769cd46](https://github.com/openssl/openssl/commit/769cd46540b2ec2a2d91ee3886b9e4f9d78e9a51), [d3aaf4e](https://github.com/openssl/openssl/commit/d3aaf4e9e71944d869ae47821d7b5a8402234ee8), [b9d8ad3](https://github.com/openssl/openssl/commit/b9d8ad3f157fa816c423bec6f7b4328ef894577c), [5b030ec](https://github.com/openssl/openssl/commit/5b030ec0800d4ad6022ecd00e18a19f77ada0b04)
- CRMF signature generation adds public key and private key matching check.
  ↳ No PR: [293ab82](https://github.com/openssl/openssl/commit/293ab820812b3979161c5f018c2e753bcd3b11a4)
- QUIC virtual handshake layer adds delay setting transmission parameter function ossl_quic_dhs_set_transport_params.
  ↳ No PR: [462d81d](https://github.com/openssl/openssl/commit/462d81dd73480fe349594d2b65698ddc84583d32)
- QUIC tracking function extension, adding detailed output of more frame types.
  ↳ No PR: [cc87010](https://github.com/openssl/openssl/commit/cc87010d27f4dc3645ea718144bf387d8833e14c)
- QUIC implementation adds default maximum acknowledgment delay, minimum active connection identifier limit and default idle timeout constant.
  ↳ No PR: [198d97c](https://github.com/openssl/openssl/commit/198d97c14e60ef112d443a619378233bd789e743)
- PATH_RESPONSE frames allow forced padding of datagrams to meet minimum size requirements.
  ↳ No PR: [c5cb85b](https://github.com/openssl/openssl/commit/c5cb85b6651256fcdd0cf15c14f4d082f73c1abb)
- The quicserver tool extension supports processing multiple streams, each stream handles HTTP requests.
  ↳ No PR: [f6225f4](https://github.com/openssl/openssl/commit/f6225f4f692ab45c0e891f83a7782a7dcd211204)
- Added internal static assertion macro ossl_static_assert_type_eq for compile-time type checking.
  ↳ No PR: [0e200d2](https://github.com/openssl/openssl/commit/0e200d2a19185dab9d73eee90bd6cd0246416a9e)
- Added internal zero time macro, indicating the current or earlier time.
  ↳ No PR: [16612c1](https://github.com/openssl/openssl/commit/16612c19290d712de65a7adcb043ba91165f3e0f)
- Added portable EINTR error detection macro to internal sockets header file.
  ↳ No PR: [8c94cf3](https://github.com/openssl/openssl/commit/8c94cf38a2a82d8b4f7ebab2e75c2110f16c9e2f)
- internal/asn1.h Added missing openssl/bio.h header include.
  ↳ No PR: [f511695](https://github.com/openssl/openssl/commit/f51169514d71115f610c9e216dcab03b89b17340)
- x509 applications have removed legacy calls to OBJ_create.
  ↳ No PR: [51024f7](https://github.com/openssl/openssl/commit/51024f75591d00a52dd867906a763b4e2107e288)
- ossl_kdf_ctx_create adds null pointer check for KDF acquisition failure.
  ↳ No PR: [0510f79](https://github.com/openssl/openssl/commit/0510f79265bf18fea5f13c1391a12397339db8b7)
- ASN1 string generation and x509 extension parsing added checks for ASN1_STRING_set return values.
  ↳ No PR: [c791e39](https://github.com/openssl/openssl/commit/c791e399abba8394833a2f88abaeb69f27f33b42), [46e9590](https://github.com/openssl/openssl/commit/46e95903762f0cc478d8a3c252390fa7312bba6e)
- Added RSA encryption and decryption demonstration example.
  ↳ No PR: [35530b1](https://github.com/openssl/openssl/commit/35530b117fcf54cf733c485e9e2e267963c081ee)
- The NEWS and CHANGES documents supplement the OSSL_DECODER description and improve the OSSL_ENCODER description.
  ↳ No PR: [0264910](https://github.com/openssl/openssl/commit/0264910413ff7a85348cc3c35e9c59cb7906278b)
- NEWS documentation has added an entry about the enhanced openssl list command.
  ↳ No PR: [e567367](https://github.com/openssl/openssl/commit/e567367afd2e3339597e984fa3ae2fecad4d6735)
- Mentioned providers pluggability concept in NEWS and CHANGES documentation.
  ↳ No PR: [8e7d941](https://github.com/openssl/openssl/commit/8e7d941ade3a86e352d9c3d601f61c033dc6788b)
- Updated the release notes of OpenSSL version 3.0, recording new APIs, deprecated items and functional changes.
  ↳ No PR: [95a444c](https://github.com/openssl/openssl/commit/95a444c9adcad04035704ab3b5d749a185ef0960)
- The subject or issuer name of an X.509 object is now displayed as a UTF-8 string by default.
  ↳ No PR: [537976d](https://github.com/openssl/openssl/commit/537976defe0775c016b9dbb36406bee1e96d0edb)
- OBJ_* functions have been implemented as thread-safe.
  ↳ No PR: [63d0f4d](https://github.com/openssl/openssl/commit/63d0f4d2b04ed334e534c9f6d0b18262161b0050)
- Added a simple SSL Echo client/server demonstration example.
  ↳ No PR: [801c638](https://github.com/openssl/openssl/commit/801c638c50406c93d683c1ab8bd1d430cff4b6d0)
- Updated the version change record in CHANGES.md, and added the change entries from 3.0.1 and 1.1.1l to 1.1.1m.
  ↳ No PR: [0e4e4e2](https://github.com/openssl/openssl/commit/0e4e4e27df3ff7c1b1c07be4a518c03acf2513ee)
- Added initial QUIC technical requirements document.
  ↳ No PR: [cb62955](https://github.com/openssl/openssl/commit/cb629550cdab518c925e9b402e11b86497a03845)
- Added documentation for BN_mod_sqrt() function.
  ↳ No PR: [03eccd2](https://github.com/openssl/openssl/commit/03eccd2663e36f8b95ba3ae8c30a63313a38ec0a)
- Added non-blocking connection management example file ddd-02-conn-nonblocking-threads.c to QUIC DDD design documentation.
  ↳ No PR: [e1d0c93](https://github.com/openssl/openssl/commit/e1d0c930c1a7913a2d67c3b8426cd6376d26bd46)
- Added QUIC multi-stream client demo example to demonstrate how to use QUIC multi-stream API.
  ↳ No PR: [584140f](https://github.com/openssl/openssl/commit/584140fa4b0a037c85b58722a08ba6fd0ee086ce)
- Updated reference to migration guide in README to new ossl-guide-migration man page.
  ↳ No PR: [27315a9](https://github.com/openssl/openssl/commit/27315a978e280a20c7f3ea0bfe05f6c186137625)
- Added a new TLS non-blocking client demonstration example to demonstrate how to write a TLS client using a non-blocking socket.
  ↳ No PR: [0295364](https://github.com/openssl/openssl/commit/0295364548bbab92b7002451c432489b55229ab8)
- Added a new HTTP/3 demo program based on nghttp3, and added SNI support.
  ↳ No PR: [e33af80](https://github.com/openssl/openssl/commit/e33af8000f2e2f4700d9845dce5bbcad9bf77c92), [f92d4a0](https://github.com/openssl/openssl/commit/f92d4a07ccdcce9c446db26e8ad01e880f007f39)

### bug fixes
- Fixed an issue where spurious errors could be generated when loading private keys, which could be avoided by properly managing the error stack.
  ↳ No PR: [da198ad](https://github.com/openssl/openssl/commit/da198adb9c5626f31c52613fe2ae59a7066c3366)
- Fixed the issue where fingerprint calculation failure was incorrectly regarded as an invalid certificate, and updated the test cases.
  ↳ No PR: [2c05607](https://github.com/openssl/openssl/commit/2c05607cd91fc5aab6d61f0324104d63a091d705)
- Fix the description and diagnostic information of -key, -in and other options in openssl req and openssl x509 commands, and add clearer warning prompts.
  ↳ No PR: [611ef4f](https://github.com/openssl/openssl/commit/611ef4f3737cc5812bdefe381403fdf1bacfba06), [cc0d1b0](https://github.com/openssl/openssl/commit/cc0d1b03a94b71dd9d8ee9aa11ee22fdc3659821)
- Fix the problem when generating AKID through v2i_AUTHORITY_KEYID(), and correctly handle the AKID suppression logic in the self-signed certificate scenario.
  ↳ No PR: [9bf1061](https://github.com/openssl/openssl/commit/9bf1061c44c81059102cd4749f6078b6ce71da9d)
- Improve the diagnostic information of the OpenSSL command line tool for missing/redundant parameters and unknown ciphers or digests, making error reporting clearer and more accurate.
  ↳ No PR: [d9f0735](https://github.com/openssl/openssl/commit/d9f073575fdb07b486cd1b38974cd177687ccc1e)
- Improved file access error prompts for load_key_certs_crls related functions and removed redundant load_key_certs_crls_suppress functions.
  ↳ No PR: [6e24994](https://github.com/openssl/openssl/commit/6e2499474cb96b28a51df1da25cc72f1cf342fad)
- Moved the decoder input structure match check to the processing stage, ensuring that it is only skipped if the first decoder in the chain that specifies an input structure does not match the user-specified structure.
  ↳ No PR: [73dd5d6](https://github.com/openssl/openssl/commit/73dd5d67c506cfeb9bf6183f0c19832c7d3f174d)
- Explicitly specify data structure names for certificate and CRL objects in PEM to DER decoders, and add support for SM2 parameters.
  ↳ No PR: [9840885](https://github.com/openssl/openssl/commit/98408852c167d895a662dcda824fd5170cad3f7d)
- In OSSL_STORE's file: scheme, set the decoder context input structure name based on the type of certificate or CRL the user expects to load, avoiding password prompts for unrelated password-protected objects.
  ↳ No PR: [821b395](https://github.com/openssl/openssl/commit/821b3956ec698927281a5b29c55cd87eb7b2793d)
- Fixed resource cleanup issue when BIO creation fails.
  ↳ No PR: [f11c01a](https://github.com/openssl/openssl/commit/f11c01a666e9d5b97e859cbc74586802549dee00)
- Fixed the double free problem in EVP_PKEY_CTX_dup() due to failure to empty the pointer that failed to be released.
  ↳ No PR: [85407b7](https://github.com/openssl/openssl/commit/85407b77543a2d4330dbb40f6b8520ea0894a716)
- Fix reference counting error when copying DH key exchange context.
  ↳ No PR: [21a0d9f](https://github.com/openssl/openssl/commit/21a0d9f3edda78d27d12cd7704de9e32976393ba)
- Improve the bounds check of parameter num_ in bio_write function to correctly handle negative input.
  ↳ No PR: [a04b065](https://github.com/openssl/openssl/commit/a04b06573e2b3c6a5c703a60bd95354c6c6e91dc)
- Fix the nc_email function and add checking for null bytes in the middle of ASN1 strings.
  ↳ No PR: [485d079](https://github.com/openssl/openssl/commit/485d0790ac1a29a0d4e7391d804810d485890376)
- Fix the parameter comparison logic in the dh_cmp_parameters function so that it correctly compares the parameters of the two keys.
  ↳ No PR: [cf1a231](https://github.com/openssl/openssl/commit/cf1a231d44db81f8565ecae5498a4f1f6f0168c9)
- Fixed a double-free issue that could occur when obtaining the PRNG seed fails.
  ↳ No PR: [52dcc01](https://github.com/openssl/openssl/commit/52dcc011191ad1a40fd52ae92ef009309deaca52)
- Fixed an issue where pointers may be released incorrectly when DRBG instantiation fails.
  ↳ No PR: [caf569a](https://github.com/openssl/openssl/commit/caf569a5b3271c2860732ee44509f3825a179fd5)
- Fixed the problem of incomplete return value checking of EVP_PKEY_fromdata_init and EVP_PKEY_fromdata to ensure correct handling of negative value error returns.
  ↳ No PR: [5e199c3](https://github.com/openssl/openssl/commit/5e199c356d09aca3b625b5ea16966b36d24b0201), [d11cab4](https://github.com/openssl/openssl/commit/d11cab47810715ba472070300b180944a1d93633), [884400d](https://github.com/openssl/openssl/commit/884400d78992d1da1573a3677876b06421b797eb)
- Fixed BN_CTX leak issue and added missing memory allocation failure check.
  ↳ No PR: [9224221](https://github.com/openssl/openssl/commit/922422119df1f6aabd2a15e6e4108d98b6143adf)
- Fixed possible BIO resource leak issues in cmp_vfy.c and encoder_lib.c.
  ↳ No PR: [374d5cf](https://github.com/openssl/openssl/commit/374d5cf2f6b8bdf87c04b5e293a7d291f2c23203)
- Fixed a memory leak caused by unreleased path string during configuration loading.
  ↳ No PR: [74b4858](https://github.com/openssl/openssl/commit/74b485848a608383d8d37c04480821ea7b613110)
- Fixed a memory leak that may occur when processing the includedir field in the configuration file.
  ↳ No PR: [19b30f1](https://github.com/openssl/openssl/commit/19b30f1c596a8df2a522f9d6dfc1c1782790fc78)
- Fix the handling of ENGINE references in the pkey_set_type function to ensure correct reference counting.
  ↳ No PR: [f7d6868](https://github.com/openssl/openssl/commit/f7d6868d0d48fedd5d9daad0c3e0cbcaef423ff3)
- Fixed a lock leak problem in evp_keymgmt_util_export_to_provider caused by not releasing the lock when cache failed.
  ↳ No PR: [fb0f65f](https://github.com/openssl/openssl/commit/fb0f65fff831d9294e34b6ef6f579c157db54b04)
- Change the -reqexts option to an alias of -extensions to unify extension configuration processing.
  ↳ No PR: [251e941](https://github.com/openssl/openssl/commit/251e941283f554f0dc4b315e3a8fb82ef5b71982)
- Fixed the issue of repeated copying and embedding of EVP_PKEY in X509_dup.
  ↳ No PR: [e0c5184](https://github.com/openssl/openssl/commit/e0c5184a56b6580127b39774f9e4e0f2caef696e), [bf585c9](https://github.com/openssl/openssl/commit/bf585c9c071ec606ebb4606e749e63354140ca30)
- Fixed double free issue of memory BIO in OCSP_sendreq_bio.
  ↳ No PR: [f99b349](https://github.com/openssl/openssl/commit/f99b34957f4173f68d6f19d0d9fac37d797b7e0c)
- Added checks on the return values of BN_new, sk_RSA_PRIME_INFO_new_reserve and other functions to prevent memory errors caused by allocation failures.
  ↳ No PR: [9dddcd9](https://github.com/openssl/openssl/commit/9dddcd90a1350fa63486cbf3226c3eee79f9aff5)
- Fixed an issue that would cause a crash if the public key value was empty when encoding the EC public key, and instead returned an error.
  ↳ No PR: [6187d9e](https://github.com/openssl/openssl/commit/6187d9eac2738e873d23c0c91f9769333b1bb6af)
- Fixed a memory leak caused by Post-Handshake Auth digest not being released when saving the handshake digest failed.
  ↳ No PR: [963eb12](https://github.com/openssl/openssl/commit/963eb12dbd551df71d7eb054e095c1b85f4aaab9)
- Fixed a segmentation fault caused by ctx->p2 being a null pointer when calling fix_dh_rfc5114.
  ↳ No PR: [09d9126](https://github.com/openssl/openssl/commit/09d91264c8ee1fdfcbe41f326a96a21cd85eb732)
- When setting up TLSv1.3 cipher suites, disabled cipher suites are no longer included.
  ↳ No PR: [6cb814d](https://github.com/openssl/openssl/commit/6cb814de6f276106eea39dbb813b9134b1b72041)
- Fixed a memory leak in the SSL module, including the ssl_create_cipher_list and tls_parse_stoc_key_share functions.
  ↳ No PR: [3a069c1](https://github.com/openssl/openssl/commit/3a069c1b0b4857b838186aeb55378195dfa50823), [b3c3440](https://github.com/openssl/openssl/commit/b3c34401c088dc247b8b54ea812e7cdde6caf361)
- Removed the isinited variable in child_prov_globals and always acquires the lock; also fixed the resource release and function call parameters during child provider creation.
  ↳ No PR: [464c2b9](https://github.com/openssl/openssl/commit/464c2b988ea149badabaf958a96fdc480df89dc7)
- Fixed the problem that deactivation cannot be performed correctly when the provider is not associated with a store, ensuring that the cleanup operation can be completed even if the store is empty.
  ↳ No PR: [e39bd62](https://github.com/openssl/openssl/commit/e39bd6215123f375ddcfe92fa2b2550294da0b73), [1e8ed3e](https://github.com/openssl/openssl/commit/1e8ed3e596162d7490b26fb12e58af5208f52402)
- Actively unregister the sub-callback before releasing the sub-libctx to avoid receiving callbacks when libctx is half-released.
  ↳ No PR: [cad2220](https://github.com/openssl/openssl/commit/cad22202a32a94059e351d9819e6c9ed5c66605a)
- Change the read lock to a write lock in ossl_provider_find to correctly synchronize stack sorting operations that may occur under multi-threading.
  ↳ No PR: [4aced11](https://github.com/openssl/openssl/commit/4aced11785f2e54875ad56f30c05bdee02b6e4e2)
- Fixed the problem of concurrency count confusion caused by not holding flag_lock when calling the sub-provider callback, and adjusted the lock release timing to ensure correctness.
  ↳ No PR: [addbd7c](https://github.com/openssl/openssl/commit/addbd7c9d784e1cb630d43487b0572e867bfc86d)
- Fixed the do_X509_REQ_verify and do_X509_verify functions to correctly return -1 when initialization fails, and added the cert_matches_key function to replace X509_check_private_key to optimize key matching logic.
  ↳ No PR: [bc42cf5](https://github.com/openssl/openssl/commit/bc42cf51c8b2a22282bb3cdf6303e230dc7b7873)
- Adjusted the priority to use the public key of subject_cert when calculating SKID, and only use the public key of subject_req when the certificate is empty to clarify the parameter semantics.
  ↳ No PR: [15ac84e](https://github.com/openssl/openssl/commit/15ac84e603678140ba32832c288e5f1745a258f8)
- Fixed OBJ_obj2txt return value checking, use TEST_int_gt in tests instead to correctly validate return values.
  ↳ No PR: [2349d7b](https://github.com/openssl/openssl/commit/2349d7ba57c9327290df6f7bc18b7f0c3976ca9e)
- Added missing return value null pointer checks in multiple functions to fix potential null pointer dereference issues.
  ↳ No PR: [ed5b26c](https://github.com/openssl/openssl/commit/ed5b26ce0b34ec00bdd53d15854a22bccbb4d415)
- Reset rwstate to SSL_NOTHING before calling ASYNC_start_job, which fixes the problem that the state is not reset correctly when an asynchronous job resumes after being paused.
  ↳ No PR: [07f620e](https://github.com/openssl/openssl/commit/07f620e3acf0dd76a3a03ada9911c544aa483aa7)
- Fixed an issue with incomplete EVP_Cipher return value checking, ensuring all error conditions are handled correctly in CMAC_Final.
  ↳ No PR: [6d77473](https://github.com/openssl/openssl/commit/6d774732517f1d63b7999c5691fc0bf046023faf), [dc19f2f](https://github.com/openssl/openssl/commit/dc19f2f6223db0578be826d03ba8012cca076d28)
- Fixed asn1_item_embed_d2i return value checking logic to ensure correct identification of error conditions.
  ↳ No PR: [7f608e4](https://github.com/openssl/openssl/commit/7f608e4b1d9473258445144ba66216fb0e63aebe)
- Fixed return value checking of random byte generation function to ensure correct handling of error conditions.
  ↳ No PR: [a8f4cdd](https://github.com/openssl/openssl/commit/a8f4cdd70c9d9ebe4553d7a72c67f73eaf0c169d)
- Fixed the return value check of the EVP_PKEY_paramgen_init function to ensure that initialization failure is correctly detected.
  ↳ No PR: [6e0b05f](https://github.com/openssl/openssl/commit/6e0b05f3008a3f22105fd2bed9314b0bfa381f93)
- Fixed the return value check of EVP_PKEY_keygen_init to correctly handle error conditions that may return negative values.
  ↳ No PR: [bf4ceed](https://github.com/openssl/openssl/commit/bf4ceeded1497c79e72fba4f9ff15febae58108d)
- Fixed the RAND_bytes_ex function return value check, changing the incorrect logical NOT judgment to the correct <=0 judgment.
  ↳ No PR: [c9007bd](https://github.com/openssl/openssl/commit/c9007bda79291179ed2df31b3dfd9f1311102847)
- Fixed the return value check of SSL_export_keying_material, changing the logical negation judgment to compare with zero to ensure correct detection of failure.
  ↳ No PR: [40649e3](https://github.com/openssl/openssl/commit/40649e36c4c0c9438f62e1bf2ccb983f6854c662)
- Fix BIO_read_filename return value check, change condition from !BIO_read_filename to <=0 to correctly detect errors.
  ↳ No PR: [e3f0362](https://github.com/openssl/openssl/commit/e3f0362407f6f40e413d6dcb35888514dbaed6f8)
- Fixed the issue where SSL BIO does not support the BIO_gets method, resulting in the HTTP client being unable to load non-ASN.1 content under TLS. Now, fallback to the BIO_get_line function is used as an alternative.
  ↳ No PR: [606c79e](https://github.com/openssl/openssl/commit/606c79e29bbc26c27c3b85cc52fe7d72051184de)
- Introduce dynamic engine identification and dedicated linked list to prevent repeated loading of the same dynamic engine and repair the resulting memory damage.
  ↳ No PR: [e2571e0](https://github.com/openssl/openssl/commit/e2571e02d2b0cd83ed1c79d384fe941f27e603c0)
- Fixed the problem of PSS parameter setting sequence in RSA signature verification initialization. By default, unrestricted PSS parameters are used until the key setting is completed.
  ↳ No PR: [eaae5d6](https://github.com/openssl/openssl/commit/eaae5d69eb5a8cd9c054b23cc388397cbb4ffb98)
- Fix logical dead code reported by Coverity: adjust exponent bit calculation in RSAZ_mod_exp_x2_ifma256 function and add assertion to ensure rem is not zero.
  ↳ No PR: [23effeb](https://github.com/openssl/openssl/commit/23effeb81fbcdc436b1e871e7fff34456d6bfbaf)
- Fixed multiple issues where the return value of ossl_bio_new_from_core_bio() was not checked, and added the msblob2key_does_selection function.
  ↳ No PR: [352a0bc](https://github.com/openssl/openssl/commit/352a0bcaab8eda18cce786d2871e8d4ec6f9cbfe)
- Fixed the diagnostic output and return value of parse_http_line1 in error conditions, added the retry timeout check function may_still_retry, and added tracking of text content types in OSSL_HTTP_REQ_CTX_nbio.
  ↳ No PR: [e2b7dc3](https://github.com/openssl/openssl/commit/e2b7dc353b353efccd1d228f743baa7c2d2f9f49)
- Check the return value of BN_dup() to avoid using a null pointer when memory allocation fails.
  ↳ No PR: [9d1a270](https://github.com/openssl/openssl/commit/9d1a27051dcd4e7a621df54a073587c6c4486476)
- Add checks on the return value of BIO_new() in cmp_vfy.c and t_x509.c, log an error and return it when memory allocation fails; and remove redundant ERR_raise calls.
  ↳ No PR: [318e979](https://github.com/openssl/openssl/commit/318e97997a514b16ca497cedb49730bc75764a05), [ecf60b9](https://github.com/openssl/openssl/commit/ecf60b9e27c041e7c95669b52a399fc2f20fd0fe)
- Fix the signature algorithm type acquisition function, and return the algorithm name instead of a null pointer for unknown algorithms; fix the certificate release function, use the new stack release interface, and unify the code style.
  ↳ No PR: [5fae09f](https://github.com/openssl/openssl/commit/5fae09f3d8da7c182c6cfb6a295dcfd15ae828ae)
- Fixed the issue that the passphrase callback in the PVK encoder was not initialized correctly, reconstructed the password acquisition logic, improved error handling and memory cleaning.
  ↳ No PR: [baa88d9](https://github.com/openssl/openssl/commit/baa88d9d170b95fd6f177b3e5f8d8818e024a55d)
- Fixed the issue where the caller key was incorrectly released in the wrong path when setting a temporary DH key.
  ↳ No PR: [e819b57](https://github.com/openssl/openssl/commit/e819b5727312477f8c1f56bf928e611ad7e78315)
- Fixed the error handling of network-related options (such as -server) in the CMP tool under no-socket compilation, and carried out multiple code cleanups and feature enhancements; optimized the documentation descriptions of multiple options in the openssl-cmp command; added instructions on the criticality of server authentication when receiving trust anchor certificates in the CMP application and API documentation.
  ↳ No PR: [83b424c](https://github.com/openssl/openssl/commit/83b424c3f60a4401fa3e6e41ff7f08e85ee9df94), [168d93a](https://github.com/openssl/openssl/commit/168d93a21d512028572777ea5bc96994f2df6c36), [1a9e286](https://github.com/openssl/openssl/commit/1a9e28607e29a1dc996024f03f445ca67b49a44f)
- Fix -rspin option so that it works properly when -reqin is not also used.
  ↳ No PR: [7ee0954](https://github.com/openssl/openssl/commit/7ee0954a086ee3b4e0a8c6736600e3d6362485c0)
- Fix the mutually exclusive logic of -server, -use_mock_srv, -port and -rspin options, and improve related documentation.
  ↳ No PR: [a56bb5d](https://github.com/openssl/openssl/commit/a56bb5d64e7599140117f935eeeb34ba94c83aea)
- Fixed an issue where s_server could not correctly skip the GET/ prefix when returning a file path in -WWW mode.
  ↳ No PR: [2e3b829](https://github.com/openssl/openssl/commit/2e3b82926a8cdae5a1bfbf3ac47a6012c270391b)
- Fixed an issue where s_client did not send SNI data correctly when using the -proxy option.
  ↳ No PR: [ea24196](https://github.com/openssl/openssl/commit/ea24196ef224d3aa3aaecb8000004bb7a0a100a2)
- Fix the error handling in the shacrypt function, change the direct return to jump to the error cleanup path, and ensure that allocated resources are released on failure.
  ↳ No PR: [ea4d16b](https://github.com/openssl/openssl/commit/ea4d16bc60dee53feb71997c1e78379eeb69b7ac)
- Fixed an issue where resources allocated via CRYPTO_malloc were not released correctly under certain wrong paths.
  ↳ No PR: [1b87116](https://github.com/openssl/openssl/commit/1b87116a0c43b8b4e1ad88b851d5bcf27c1a5f64)
- Fixed multiple issues with incomplete EVP_PKEY_CTX_ctrl return value checking, and changed the condition from <0 to <=0 to correctly capture all error conditions.
  ↳ No PR: [7b1264b](https://github.com/openssl/openssl/commit/7b1264baab7edd82fea8b27d9ddec048bafc0048)
- Fixed the problem that the EVP_MD_CTX resource is not released correctly in the tls1_mac function, ensuring that the resource can also be released on the wrong path.
  ↳ No PR: [949e4f7](https://github.com/openssl/openssl/commit/949e4f79d202d43519d373b2af6b1a4948bf1a74)
- Fixed resource leak issues in multiple core modules and optimized string comparison methods.
  ↳ No PR: [10481d3](https://github.com/openssl/openssl/commit/10481d33844218694929a7bad57314411a33ab74)
- Fix indentation issues in providers/implementations/digests/sha3_prov.c and providers/implementations/kdfs/pbkdf2.c.
  ↳ No PR: [2c9da41](https://github.com/openssl/openssl/commit/2c9da416a608e2aaf19c16d920baddf2473c8392)
- Fixed the problem of Decoder, Encoder and Store loader failing due to internal assertion error when retrieving with query string, and added related test cases.
  ↳ No PR: [cd1981a](https://github.com/openssl/openssl/commit/cd1981a0dc165ab6af5e2945beaaa9efe4484cee), [f5e97b3](https://github.com/openssl/openssl/commit/f5e97b3702916e69873746108ac7c100a31d2241)
- Fixed the regression problem of the -kdflen option in the pkeyutl command, and adjusted the parameter checking method and the buffer size for input data reading.
  ↳ No PR: [b82fd89](https://github.com/openssl/openssl/commit/b82fd89d8bae1445c89ec90d1a6145fe3216d2d7)
- Fixed the pointer setting logic when clearing old MD data, ensuring that md_data is set to NULL only after the memory is released.
  ↳ No PR: [8086b26](https://github.com/openssl/openssl/commit/8086b267fb3395c53cd5fc29eea68ba4826b333d)
- Fixed a conditional judgment error when counting unprocessed records in the kTLS RX offload path.
  ↳ No PR: [d73a7a3](https://github.com/openssl/openssl/commit/d73a7a3a71270aaadb4e4e678ae9bd3cef8b9cbd)
- Fixed the evp_keymgmt_util_match function so that it correctly attempts cross-export in the other direction after the first cross-export attempt fails.
  ↳ No PR: [37b8507](https://github.com/openssl/openssl/commit/37b850738cbab74413d41033b2a4df1d69e1fa4a)
- Fixed the null pointer dereference problem and added null value checks in the load_cert_certs and next_item functions.
  ↳ No PR: [8c870f6](https://github.com/openssl/openssl/commit/8c870f6bed241ec80c67453e60592461f0d8f2b8)
- Fixed an issue in s_server that caused 2^14 byte long records to be incorrectly processed due to BIO_gets null termination, and adjusted buffer allocation and read size to support the full record length.
  ↳ No PR: [148b592](https://github.com/openssl/openssl/commit/148b592db7ea18e0209078fe313514fb7c7553f5)
- Fix BIO_FLAGS macro definition conflict, fix duplicate macro definitions and add comments in public header files to avoid future conflicts.
  ↳ No PR: [e278f18](https://github.com/openssl/openssl/commit/e278f18563dd3dd67c00200ee30402f48023c6ef)
- Add return value check for X509_STORE_lock to prevent dirty data when lock acquisition fails.
  ↳ No PR: [814999c](https://github.com/openssl/openssl/commit/814999cb44135fd197945693a7c00cf0af784206)
- Added checks on whether the global pointer is NULL in multiple BIO core operation functions to avoid null pointer dereference.
  ↳ No PR: [7f1cb46](https://github.com/openssl/openssl/commit/7f1cb465c1f0e45bde8c1ee54a37e6f7641c70c6)
- Add a null pointer check for memory allocation failure in the UI data copy function, and return 0 in case of failure.
  ↳ No PR: [3f6a12a](https://github.com/openssl/openssl/commit/3f6a12a07f52c55dc3f4b0def42680f589f89ed4)
- Fixed undefined behavior problem caused by hash function in lhash caused by 32-bit right shift of 32-bit value.
  ↳ No PR: [2ce0a3d](https://github.com/openssl/openssl/commit/2ce0a3d19005271e7e3c351b562d9da93e2d4c80)
- Fix the IV length of the DES EDE ECB implementation, setting it to 0 to comply with the specification that ECB mode does not use IVs.
  ↳ No PR: [d450eb8](https://github.com/openssl/openssl/commit/d450eb84c802b2f78971f905b251a0fb89ebb7d1)
- Fixed the issue where the ciphers command ignores the -propquery option and ensures that this option takes effect correctly.
  ↳ No PR: [4ed3817](https://github.com/openssl/openssl/commit/4ed381736b063284bdbd5d302988617aa4366a3f)
- Cache IV length in EVP encryption context to avoid expensive parameter lookup every time and fix related bugs.
  ↳ No PR: [b30b45b](https://github.com/openssl/openssl/commit/b30b45b7247d056b569e2b5139f8b503d36e646c)
- Use opt_int_arg() in the speed command to parse integer arguments to avoid hexadecimal input processing errors, and update the help information to explain the input format.
  ↳ No PR: [78212c6](https://github.com/openssl/openssl/commit/78212c6472ed3ade565ebcde0330d6eca7785fd6)
- Fixed an issue where default_context_thread_local thread local data was not cleaned up correctly.
  ↳ No PR: [8e012cd](https://github.com/openssl/openssl/commit/8e012cdc896ec6a98b45119b127b230cbbb6e93b)
- Output auxiliary messages to standard error stream, fix output target for self-signed verification of certificate requests.
  ↳ No PR: [2a6994c](https://github.com/openssl/openssl/commit/2a6994cfa08368a710d66caaae4fc07ad35631bf)
- Fix the problem of unchecked memory allocation failure in openssl rehash, add a check for OPENSSL_strdup return value and release the memory on failure.
  ↳ No PR: [79cda38](https://github.com/openssl/openssl/commit/79cda38cff834224fb9d86dc7433b4f60688ce49)
- Add a null pointer check to the return value of rand_get_global to avoid potential null pointer dereferences and return an error if the get fails.
  ↳ No PR: [09dca55](https://github.com/openssl/openssl/commit/09dca557332a2187598932388ac7bd7bbf16172b)
- Add missing null pointer checks for BIO_new and other calls to avoid null pointer dereference problems caused by returning NULL.
  ↳ No PR: [ba0b60c](https://github.com/openssl/openssl/commit/ba0b60c632ae9c5590b59184281baaf0a39f0c24)
- During CMP initialization, if no protection certificate or old certificate is provided, the subject of the CSR is used as the default message sender.
  ↳ No PR: [cd7ec0b](https://github.com/openssl/openssl/commit/cd7ec0bca00ceb6e8d4af46a57c6c096a7ed8947)
- Check the return value of CRYPTO_strdup() and fix the null pointer dereference problem caused by possible memory allocation failure.
  ↳ No PR: [37be6fe](https://github.com/openssl/openssl/commit/37be6feeebfec87733e5cb4762fc12bebba9f124)
- In async_posix, memory allocation error reporting is now triggered when stack memory allocation fails.
  ↳ No PR: [83c48d9](https://github.com/openssl/openssl/commit/83c48d96ff24728d94e0890f320b0d1220d9cba3)
- Rename the function parameter name strlen to strlength to avoid conflict with C++ reserved words.
  ↳ No PR: [28e141c](https://github.com/openssl/openssl/commit/28e141c45d36757e052b72685fb874968f013d43)
- Fix a null pointer dereference problem that may occur in BN_mod_exp2_mont when parameter m is zero, and add a regression test.
  ↳ No PR: [43135a5](https://github.com/openssl/openssl/commit/43135a5d2274c24e97f50e16ce492c22eb717ab2)
- Fixed an issue in openssl s_server -WWW where trying to call SSL_sendfile when KTLS is not actually enabled causes the request to fail, add KTLS availability check and give a warning when unavailable.
  ↳ No PR: [aea68b0](https://github.com/openssl/openssl/commit/aea68b0ddb7113b982ab503bf830d641e8425759)
- In s_client and s_server, added a check on the return value of BIO_new_file(), output an error message and exit when the file fails to open.
  ↳ No PR: [625b099](https://github.com/openssl/openssl/commit/625b0990a069a18917341e2f0fbe36327b0883b7)
- Fixed a memory leak caused by not releasing the allocated stack when memory allocation failed in the append_ia5 function.
  ↳ No PR: [1753559](https://github.com/openssl/openssl/commit/175355923046921a689b500f7a72455f7095708f)
- Fixed the problem of unchecked BIO_read return value in PEM_read_bio_ex, added failure handling and optimized error paths.
  ↳ No PR: [2823e2e](https://github.com/openssl/openssl/commit/2823e2e1d39479a7835d176862ec15e47a1bdecd)
- Fixed the TCP protocol detection logic in the init_client() function, using BIO_ADDRINFO_protocol() to correctly obtain the protocol type to set the NODELAY option.
  ↳ No PR: [54b6755](https://github.com/openssl/openssl/commit/54b6755702309487ea860e1cc3e60ccef4cf7878)
- Fixed the problem of invalid IV length cache in EVP encryption code to avoid cache invalidation due to excessive invalidation.
  ↳ No PR: [b9a2f24](https://github.com/openssl/openssl/commit/b9a2f24e44f53c7c3a63a7f7b165e8267cbdda42)
- Fixed an issue where DH key exchange padding was not always enabled when using X9.42 KDF, padding is now forced to be enabled.
  ↳ No PR: [01b1877](https://github.com/openssl/openssl/commit/01b18775676115945956f4de0eb0cafedaf027ab), [4413fe3](https://github.com/openssl/openssl/commit/4413fe3520da3ad42c417828b1785eeedcde50d3)
- Fixed a bug caused by incorrect parameter type in the dup method of scrypt KDF provider, reconstructed the function signature and added correct parameter conversion.
  ↳ No PR: [e04c2c0](https://github.com/openssl/openssl/commit/e04c2c02e8e6b9ec71d93c26c14167ceb2165ce8), [1e7479e](https://github.com/openssl/openssl/commit/1e7479e8a4f33b1afa7d62b07c682f6987e6a515)
- Added a new detection function in dynamic engine loading to avoid false errors caused by misjudgment of the OpenSSL 1.1.x engine.
  ↳ No PR: [bd5c91c](https://github.com/openssl/openssl/commit/bd5c91c82cdc4b6ffe4a2970f9512fc5ec7d2d06)
- Fixed uninitialized reads in SSL_shutdown and SSL_do_handshake.
  ↳ No PR: [09134f1](https://github.com/openssl/openssl/commit/09134f183f76539aa1294adfef10fcc694e90267)
- Fixed the issue of inconsistent parameter declaration in Camellia decryption function.
  ↳ No PR: [a12a71f](https://github.com/openssl/openssl/commit/a12a71fafbe9b0ce90a51098fbf166d9da62b111)
- Fixed openssl check -rsa command to support checking of both RSA and RSA-PSS keys.
  ↳ No PR: [388d6f4](https://github.com/openssl/openssl/commit/388d6f4506892a47e69d28232c4b7ebd43706478)
- Fixed the problem that the -proxy and -starttls options in openssl s_client cannot be used at the same time, and the HTTP proxy connection processing is advanced before the STARTTLS protocol is selected.
  ↳ No PR: [802cacf](https://github.com/openssl/openssl/commit/802cacf34f2db9111becb4f0d3aa00460df13a19)
- Fixed a null pointer dereference issue caused by unchecked when evp_pkey_get_legacy() returned NULL, added null pointer checks in multiple Ed25519/Ed448 signature and verification functions.
  ↳ No PR: [b9a86d5](https://github.com/openssl/openssl/commit/b9a86d5dd8b5bd33be42390bcbb5121fe0ae71a1)
- Fixed the crash problem of ERR_load_strings() when no-err is configured, skipping the initialization and cleaning of the error string hash table through conditional compilation.
  ↳ No PR: [11e85b8](https://github.com/openssl/openssl/commit/11e85b8941cb6f728e37f15502f26e67231db6b6)
- Fixed the issue of incorrect error reporting in CMS I/O functions and added relevant test cases.
  ↳ No PR: [45a3c59](https://github.com/openssl/openssl/commit/45a3c592b94b66cab72e5bffbaf9d810c3fb29c0)
- Fixed an issue where the client certificate chain check failed due to ca_dn being NULL when the server did not send the CA name under TLS-1.3.
  ↳ No PR: [89dd854](https://github.com/openssl/openssl/commit/89dd85430770d39cbfb15eb586c921958ca7687f)
- Fixed a null pointer dereference problem that may occur when memory allocation fails in sshkdf.
  ↳ No PR: [148176c](https://github.com/openssl/openssl/commit/148176ca323e3dfce5d5cdb5578c113c8d2440bb)
- Fixed the unchecked return value issue in Coverity reporting, explicitly ignoring the return value of EVP_CipherInit_ex.
  ↳ No PR: [b11183b](https://github.com/openssl/openssl/commit/b11183be0cd3ad675248804922bb240fbbd448e4)
- Fixed an issue where the return value of bn_rshift_fixed_top was not checked, correctly jumping to error handling when the function fails.
  ↳ No PR: [bc6bac8](https://github.com/openssl/openssl/commit/bc6bac8561ead83d6135f376ffcbbb0b657e64fe)
- Allow setting the SM2 distributed ID parameter to an empty string.
  ↳ No PR: [2904d0a](https://github.com/openssl/openssl/commit/2904d0a2ae0ec6ce23d5cec66ce8c7bdb005d4e5), [707d4e0](https://github.com/openssl/openssl/commit/707d4e06eba71fb8a8b2faa77a2072511189544d)
- Fix the null pointer dereference problem in the create_cert_store function caused by X509_STORE_new possibly returning NULL, add a null value check and return an error in case of failure.
  ↳ No PR: [3f07596](https://github.com/openssl/openssl/commit/3f075967f664aac12951a1d7aa3124d9235cd299)
- Fixed the null pointer dereference problem that may be caused by EVP_KDF_fetch returning a null pointer in the PBKDF2 implementation, and added return value checking.
  ↳ No PR: [5f1424c](https://github.com/openssl/openssl/commit/5f1424c6bdca8ddb9d5d88a78a1d738be19c4ea8)
- Fix the null pointer dereference problem that may be caused by not checking the return value of EVP_PKEY_copy_parameters in the ssl_set_cert_and_key function.
  ↳ No PR: [6646e01](https://github.com/openssl/openssl/commit/6646e015a50e5455117c22a27032011689db710f)
- Fixed the assertion failure problem in the DTLS server caused by the MTU exceeding the maximum fragment length, and added a regression test.
  ↳ No PR: [e915c3f](https://github.com/openssl/openssl/commit/e915c3f5381cd38ebdc1824c3ba9896ea7160103)
- Fixed the wild pointer dereference problem that may be caused by not checking the return value of OCSP_basic_add1_status in the make_ocsp_response function.
  ↳ No PR: [4d50a54](https://github.com/openssl/openssl/commit/4d50a5467b0a208c61d163239a3544bae06343ea)
- Fixed an issue in the RC4-MD5 cipher suite where TLS AAD data was incorrectly used as the MAC key due to a copy-paste error.
  ↳ No PR: [3321993](https://github.com/openssl/openssl/commit/33219939c782cf363b30e9e899b9997fb1ced440)
- Delete the misused function ossl_provider_clear_all_operation_bits and all its calls, and fix the problem of operation bits being cleared incorrectly when the method cache is refreshed.
  ↳ No PR: [20b6d85](https://github.com/openssl/openssl/commit/20b6d85ab2b9cfa4cd29d2422d69c3e3f4db0a41)
- Fixed bug in OPENSSL_LH_flush function where num_items counter was not reset.
  ↳ No PR: [e5da681](https://github.com/openssl/openssl/commit/e5da68183410c06f7b350a0721bc2bd6057e438e)
- Fixed a possible error when calling finalization in an uninitialized SipHash context, failure is now correctly returned.
  ↳ No PR: [650b142](https://github.com/openssl/openssl/commit/650b142c2e4c1d57868bdbbe1f7f4549ee77f8eb)
- Fixed the problem of incorrectly setting the mac size of sipcopy when siphash copies, and ensures complete copy context.
  ↳ No PR: [905fec4](https://github.com/openssl/openssl/commit/905fec4f4d6bb8a978476cbce0f293ffc683b5fd)
- Fixed the problem of incomplete copying of the entire structure during poly1305 context copy, and reset the update flag during initialization.
  ↳ No PR: [bbe909d](https://github.com/openssl/openssl/commit/bbe909d00e9a593bd5954dfca4d3020467977565)
- Fixed the problem of incorrectly clearing method storage when refreshing the query cache, renamed related functions and adjusted internal fields to clarify their purpose.
  ↳ No PR: [60640d7](https://github.com/openssl/openssl/commit/60640d79ca7ea0980dc09c71fe6a297b5f8588a2)
- Fixed issue where locale was not initialized before calling evp_pkey_name2type.
  ↳ No PR: [e560655](https://github.com/openssl/openssl/commit/e560655f72dc27bcea973c6abfe99af75d313ad7)
- Distinguish between fatal errors and non-fatal errors when creating a record layer, so that non-fatal errors can be tried to be handled by other record layers.
  ↳ No PR: [7c29399](https://github.com/openssl/openssl/commit/7c2939999f8e43d996d846867ba326b052f821d6)
- Add cache flushing and removal functionality to method stores for encoders, decoders and storage loaders to ensure proper cleanup when providers are deactivated or modified.
  ↳ No PR: [32e3c07](https://github.com/openssl/openssl/commit/32e3c071373280b69be02ba91fc3204495e2e1bf)
- Fixed an issue where optional properties could be incorrectly ignored when a new provider was added, constructor methods are now always tried.
  ↳ No PR: [4b1b629](https://github.com/openssl/openssl/commit/4b1b629725970384d6cf4dafe9e83e54859574cd)
- Fixed compilation failure caused by disabling compression function, and added conditional compilation protection to related code.
  ↳ No PR: [976b263](https://github.com/openssl/openssl/commit/976b263d0a8581059c21fb34653df3375667f050)
- Fixed the problem of incorrectly passing digest when signing Ed25519/Ed448 in CRMF, and ensure that such keys do not use digest when signing POPO.
  ↳ No PR: [de56f72](https://github.com/openssl/openssl/commit/de56f726e163e99128ff93a04d74a8461f5a724b)
- In s_server, when initializing the connection fails and no read is attempted, an error is now reported to distinguish configuration errors from errors caused by the client.
  ↳ No PR: [a6d52f1](https://github.com/openssl/openssl/commit/a6d52f178c4cb4665d0bf235001b5c9c1ff03da7)
- Fixed the crash problem of fix_dh_paramgen_type function caused by invalid parameter types, added checking for invalid values and returned an error.
  ↳ No PR: [359dad5](https://github.com/openssl/openssl/commit/359dad5178285d5471f2a57a5aa99c1f588dffcb)
- Adjust the order of header file inclusion and place internal/e_os.h before string.h to fix compilation issues.
  ↳ No PR: [cf91a2b](https://github.com/openssl/openssl/commit/cf91a2b3c196ee4d7be93ab9f8fc8e097128ad68)
- Fixed the problem of clang-14 compiler incorrectly optimizing code due to strict alias rules, and changed related functions to inline macros to avoid accidental removal of code.
  ↳ No PR: [8712db5](https://github.com/openssl/openssl/commit/8712db5e4e0c508de10e887aebf639384dc20710)
- Adjust loop conditions to make the risk of zero-length loops more clear and fix related issues.
  ↳ No PR: [36c269c](https://github.com/openssl/openssl/commit/36c269c3023f5eb626ec79777ed8b285ef939be2)
- Fixed the problem that the -CAfile option was ignored in x509 applications. Now -CAfile can take effect correctly when using the -new or -in option.
  ↳ No PR: [10c7887](https://github.com/openssl/openssl/commit/10c7887330bb6ca136cd16fe081639f4462a072e)
- Fixed a memory leak in the crl_set_issuers function that caused the temporary object not to be released when allocating or inserting the issuers stack failed.
  ↳ No PR: [e9007e0](https://github.com/openssl/openssl/commit/e9007e09792e3735d4973743634ff55d354fc7d8)
- Fixed a leak problem in the X509_issuer_and_serial_hash function caused by incorrect memory release.
  ↳ No PR: [b7e28c0](https://github.com/openssl/openssl/commit/b7e28c0bb1cdc07e36c7dc2467083236b931de31)
- Fixed security issue with buffer size determination in GOST key exchange, use dynamic buffer allocation instead to avoid overflow.
  ↳ No PR: [2b5e899](https://github.com/openssl/openssl/commit/2b5e89992e3ada1131beebb2a22722168b9389c2)
- Fixed a crash in ssl_security_cert_chain caused by a null pointer in the certificate chain, and added a null pointer check.
  ↳ No PR: [dc0ef29](https://github.com/openssl/openssl/commit/dc0ef292f7df4ce0c49c64b47726a6768f9ac044)
- Fixed the issue of incorrect EVP_CIPHER_CTX_rand_key return value check to ensure correct judgment of whether the key generation is successful.
  ↳ No PR: [f15e3f3](https://github.com/openssl/openssl/commit/f15e3f3aa95df743f0da793da952f87370efb4ff)
- Fixed UI_method_set_ex_data return value check bug, the function returns 0 or 1 instead of negative number, so change the condition from < 0 to logical negation.
  ↳ No PR: [1aef2c1](https://github.com/openssl/openssl/commit/1aef2c10f10e0685298008be596c80e148c71a51)
- Fixed the EVP_PKEY_CTX_set_group_name return value check error and changed the error condition from logical negation to less than or equal to zero.
  ↳ No PR: [56876ae](https://github.com/openssl/openssl/commit/56876ae952b96b4a83266f6b2ec1393f599015d6)
- Fix the return value check of X509_LOOKUP_* series functions, and change the judgment of equal to 0 to less than or equal to 0 to correctly handle error conditions.
  ↳ No PR: [e22ea36](https://github.com/openssl/openssl/commit/e22ea36fa8296b402348da8f5ab5e258be8402cf)
- Fix memory leak in decoder on wrong path, ensure reference count is released correctly.
  ↳ No PR: [9ec9b96](https://github.com/openssl/openssl/commit/9ec9b968f93e4a8e7c90eb1e717f0d7cd4ab722d), [da31939](https://github.com/openssl/openssl/commit/da3193976380b8bd697a472025ff9f384cbca7af)
- Fix the return value processing of EVP_PKEY_check and EVP_PKEY_param_check so that it correctly handles the case where the return value is 0 or a negative value.
  ↳ No PR: [92d0d7e](https://github.com/openssl/openssl/commit/92d0d7ea9be40909ee79fb8861641a61eead2431), [e85bef9](https://github.com/openssl/openssl/commit/e85bef981c037a6ebc0ca39f61c11bd79ed89fb3)
- Fix memory leaks in EVP_PKEY related functions: correctly release pkey when evp_pkey_copy_downgraded() fails, and fix the problem that tmp_keymgmt is not released when keymgmt is empty in evp_pkey_export_to_provider.
  ↳ No PR: [d873280](https://github.com/openssl/openssl/commit/d8732803c493cba7a863c5c16da62ee9d611c5ca), [115eb94](https://github.com/openssl/openssl/commit/115eb945acd9a27bf81c6c8923f43768f9e487a8)
- Fix the UI_add_input_string return value checking logic to ensure correct judgment of execution results.
  ↳ No PR: [5755c11](https://github.com/openssl/openssl/commit/5755c11fd6e50028946e6e17c835afcd56995699)
- Fixed a memory leak in ossl_provider_doall_activated: when the callback fails, correctly release the provider that was previously pushed onto the stack and increment the reference count.
  ↳ No PR: [b4be10d](https://github.com/openssl/openssl/commit/b4be10dfcd370960cecfda9773e1bfcc568a7390)
- Fixed the problem of calling the release function before the reference count is initialized when creating a provider. Make sure that the reference count is correctly initialized before calling ossl_provider_free.
  ↳ No PR: [c4ed6f6](https://github.com/openssl/openssl/commit/c4ed6f6f0ee700e0473def049659061dd52fd3fc)
- Fixed a memory leak in ossl_method_store_add() caused by ossl_prop_defn_set() failure.
  ↳ No PR: [fed8dbe](https://github.com/openssl/openssl/commit/fed8dbea27b7e01ee934951b25c6ffd40ad1d5c3)
- Fixed an issue where CONF_modules_unload still tried to use the lock even if it failed to initialize the lock inside CONF_modules_finish, now checks the initialization result and returns early if it fails.
  ↳ No PR: [697d0b5](https://github.com/openssl/openssl/commit/697d0b5ba146c232f5b2aa87f4e847a5495c1735)
- Fixed an issue where the add_provider_groups function did not clean up the algorithm pointer on failure.
  ↳ No PR: [a7863f9](https://github.com/openssl/openssl/commit/a7863f994955c45fb7ce29e30b81a6206994c3dd)
- Fix the use-after-free problem in error handling of hmac_dup function to ensure that the digest field is cleared when copying fails.
  ↳ No PR: [cec1699](https://github.com/openssl/openssl/commit/cec1699f1f54ba8b87f055776dc77b48dd37d5fa), [27f7f52](https://github.com/openssl/openssl/commit/27f7f527652e403177335eb2e3ba1ff6df13f193)
- Fix potential use-after-free issue with md in sm2_dupctx, clearing the md field of the target context after copying the context.
  ↳ No PR: [926c698](https://github.com/openssl/openssl/commit/926c698c6f0a197e0322d4617db0ecd0d40f6e06)
- Fixed a bug where BN_mod_exp_mont_consttime on x86_64 could incorrectly return the modulus m instead of zero, by uniformly using the standard Montgomery reduction instead of the internal function bn_from_montgomery to complete the final step.
  ↳ No PR: [0ae365e](https://github.com/openssl/openssl/commit/0ae365e1f80648f4c52aa3ac9bbc279b6192b23e)
- Add an additional reduction step to the RSAZ modular exponentiation implementation to ensure that the result is fully reduced to the modulus range.
  ↳ No PR: [6d702ce](https://github.com/openssl/openssl/commit/6d702cebfce3ffd9d8c0cb2af80a987d3288e7a3)
- Fallback of fixed-length unrolled Montgomery multiplication optimization for PPC architecture, as this implementation would produce incorrect results.
  ↳ No PR: [712d9cc](https://github.com/openssl/openssl/commit/712d9cc90e355b2c98a959d4e9398610d2269c9e)
- Fixed a crash in X509v3_asid_subset() caused by the asnum or rdi field being a null pointer, and added corresponding test cases.
  ↳ No PR: [01fc9b6](https://github.com/openssl/openssl/commit/01fc9b6bce82f0534d6673659a0e59a71f57ee82)
- Fixed the crash of v2i_IPAddrBlocks() caused by the IP address prefix length being too large, and added a legality check on the prefix length.
  ↳ No PR: [b91ad3c](https://github.com/openssl/openssl/commit/b91ad3c69c27c35be4fd7f1e8811c33c31b02afd)
- Fix the flaw in the range_should_be_prefix() function that incorrectly determines whether the IP address range should be represented as a prefix, and add corresponding test cases.
  ↳ No PR: [30532e5](https://github.com/openssl/openssl/commit/30532e59f475e0066c030693e4d614311a9e0cae)
- Fixed the problem of insufficient adaptation of the input buffer length parameter when calling EVP_KDF_derive() in the kdf_derive() function, and added an error check for an output buffer that is too small.
  ↳ No PR: [0feb138](https://github.com/openssl/openssl/commit/0feb138fbeeec9ae09e63b212a0a6e345ed0dc30)
- In order to avoid recursive locking, the lock used to protect initialization state variables is separated from init_lock and a new independent lock is added.
  ↳ No PR: [e9a806b](https://github.com/openssl/openssl/commit/e9a806b2c265da3a4ca472acb4a4286d9c1b5c9d)
- Fixed an issue where the c_rehash tool incorrectly retained the prefix when calculating the CRL hash, and now correctly removes the prefix.
  ↳ No PR: [87eee75](https://github.com/openssl/openssl/commit/87eee75010f7efaa617ff32163359bf81513a619)
- Fix the set_dateopt() function return value so that the -dateopt option works properly.
  ↳ No PR: [55b7fa2](https://github.com/openssl/openssl/commit/55b7fa2609e1fe354517a745b78182323bce24ed)
- Add a check on the return value of OPENSSL_malloc() in ASN1_TIME_to_tm() to prevent the use of a null pointer when memory allocation fails.
  ↳ No PR: [8547cd6](https://github.com/openssl/openssl/commit/8547cd6790881cbba0f20aa4ce048243065a24bf)
- Improve error diagnostics when setting up TLS groups: clear error messages and explicitly report invalid groups.
  ↳ No PR: [ce8822b](https://github.com/openssl/openssl/commit/ce8822b7e5f4fdf836677faee336a5cf996d4363)
- Fixed the problem that negative return values in the dh_priv_encode function were not handled correctly to avoid error propagation.
  ↳ No PR: [be54ad8](https://github.com/openssl/openssl/commit/be54ad88a67d2fba3b4fd51bef0fe7db0c01b99a)
- Fixed the handling of negative return values when encoding DSA private keys, and added length checks to prevent errors.
  ↳ No PR: [3ee2611](https://github.com/openssl/openssl/commit/3ee2611677e7e9f90e270f3ee4f343c9d3d86835)
- Add a null pointer check for the return value of OPENSSL_strdup in the by_store_ctrl_ex function, and return an error immediately if the allocation fails.
  ↳ No PR: [e163969](https://github.com/openssl/openssl/commit/e163969d3580e5b797fcebde0d3000302912ef18)
- In s_server's UNIX socket option handling, add a null pointer check for the return value of OPENSSL_strdup and jump to error handling on failure.
  ↳ No PR: [a6a2dd9](https://github.com/openssl/openssl/commit/a6a2dd9f60b3f3e93de1337ee84f9e8f33bc86a8)
- Add validity check for saltlen and trailerfield parameters to RSA key writer to prevent invalid parameters from causing errors.
  ↳ No PR: [4832099](https://github.com/openssl/openssl/commit/48320997b49b07b5abadec89c7fbe5d5f3d41da4)
- Fix memory leak in EC_GROUP_new_from_ecparameters: when parsing elliptic curve parameters, allocated BIGNUM objects were not properly released after ASN1_INTEGER_to_BN failed.
  ↳ No PR: [be50862](https://github.com/openssl/openssl/commit/be50862e72d96e599f1111bbb69f41b5af651c97)
- Fixed the problem of wrong parameter unit when calling bn_reduce_once_in_place in rsaz_mod_exp_avx512_x2, converting the modulo bit size to the number of words.
  ↳ No PR: [4d8a88c](https://github.com/openssl/openssl/commit/4d8a88c134df634ba610ff8db1eb8478ac5fd345)
- Fixed an issue where KDF objects did not return errors correctly when memory allocation failed.
  ↳ No PR: [7260709](https://github.com/openssl/openssl/commit/7260709e9ef155c8b3fccaa32e8ba496a3059905)
- Fix lock competition and resource release logic in provider storage to avoid double unlocking and potential memory leaks.
  ↳ No PR: [61f5106](https://github.com/openssl/openssl/commit/61f510600e2c7cdee6e61f8b7075fb0e939eb179)
- Fixed an issue where negative return values in the RSA key pair verification function were not correctly regarded as verification failures.
  ↳ No PR: [518f1ee](https://github.com/openssl/openssl/commit/518f1ee81d5a6910365ef404888d0e119a87fd81)
- Fixed a memory leak in ossl_rsa_fromdata caused by collect_numbers memory allocation failure.
  ↳ No PR: [28adea9](https://github.com/openssl/openssl/commit/28adea95975c3ea53fc590efda35dee13efd4767)
- Use OPENSSL_zalloc to allocate the EVP_PBE_CTL structure and fix the problem of uninitialized memory.
  ↳ No PR: [3211266](https://github.com/openssl/openssl/commit/3211266aa23253ce8af2b98c4fd94a12a4afa7e4)
- Fix code format issues in crypto/x509/v3_addr.c, and adjust the order of IPAddressFamily length checks.
  ↳ No PR: [30d398a](https://github.com/openssl/openssl/commit/30d398ad375bb4b15eae6497d67d54c03be2660d)
- Fixed Content-Length calculation logic in HTTP client, including BIO_CTRL_INFO return value based on file BIO and calculation in set1_content().
  ↳ No PR: [243465f](https://github.com/openssl/openssl/commit/243465fd556837402bff52b7bf3d59420b68a02e), [8c65e1f](https://github.com/openssl/openssl/commit/8c65e1f719ecf7ec7ed3094bbd763f88708d26eb)
- Fixed the crash caused when use_ssl is not set but SSL_CTX is provided, and adds parameter consistency check.
  ↳ No PR: [96e13a1](https://github.com/openssl/openssl/commit/96e13a1679872d879683346c1e09ca227f77efb0)
- Fixed parameter errors caused by copy-paste errors in the OSSL_HTTP_REQ_CTX_nbio function, and corrected the retry check object from rbio to req.
  ↳ No PR: [059a4ad](https://github.com/openssl/openssl/commit/059a4ad0999dd6dbd7340b5e4f7566812d51bb1e)
- Fixed a possible crash caused by calling CONF_modules_unload() after calling OPENSSL_cleanup().
  ↳ No PR: [d840f07](https://github.com/openssl/openssl/commit/d840f07bcdfc3910de5aa327a245866a67f94799)
- Fixed the problem that the return value of BN_one() call in bn_gcd was not checked to avoid potential errors when memory allocation fails.
  ↳ No PR: [7fe7cc5](https://github.com/openssl/openssl/commit/7fe7cc57af3db1e497877f0329ba17609b2efc8b)
- Fixed parameter passing error in SSL_set_srp_server_param_pw function, corrected GN->N and GN->g to s->srp_ctx.N and s->srp_ctx.g.
  ↳ No PR: [12e4883](https://github.com/openssl/openssl/commit/12e488367d34657a5c0e1bc322e66c48463d2a0c)
- Fix the release order of HTTP TLS information in CMP context, avoid crashes, and add null pointer protection.
  ↳ No PR: [8c09474](https://github.com/openssl/openssl/commit/8c094747d78bb8627e9ca5241fed0550a3de2fdb)
- Fixed a memory leak in EVP_PKEY_get1_encoded_public_key caused by the failure of the second call to EVP_PKEY_get_octet_string_param.
  ↳ No PR: [4e9a499](https://github.com/openssl/openssl/commit/4e9a4997c540e64647d4e1708a1dbda51fb59a68)
- Rollback core changes to chain_build() error reporting, no longer setting errors in check_issued.
  ↳ No PR: [1f00dc4](https://github.com/openssl/openssl/commit/1f00dc4f8c0ef0101368de2adf22495e5e295114)
- Fixed a segfault in SSL code caused by the EVP_MD pointer being NULL.
  ↳ No PR: [b740012](https://github.com/openssl/openssl/commit/b740012f77aed97cb4b3cd8a4f1fb2f668542795)
- Fixed the issue where the keylength field was not copied when copying FFC parameters.
  ↳ No PR: [5f311b1](https://github.com/openssl/openssl/commit/5f311b10ab3dd6417a3247c62b4ec072751459db)
- Fix the possible null pointer dereference problem in the ossl_provider_ctx function and add null value check.
  ↳ No PR: [f809103](https://github.com/openssl/openssl/commit/f80910390cb882f346fe59c9803fc914b9c367c2)
- Fixed the issue where the verify_callback function in openssl s_client/s_server does not check whether the certificate is empty before printing the wrong certificate information.
  ↳ No PR: [fad0f80](https://github.com/openssl/openssl/commit/fad0f80eff188ef938fed614245a56ed56110deb)
- Fix memory leak in PKCS12_pbe_crypt_ex function, ensure out variable is released on wrong path.
  ↳ No PR: [af801ec](https://github.com/openssl/openssl/commit/af801ec89205aaf6ebf8522d510d0b1fc29e3233)
- Fix the null pointer dereference problem in the ossl_provider_ctx function, check whether prov is NULL before accessing prov->provctx.
  ↳ No PR: [f913c3c](https://github.com/openssl/openssl/commit/f913c3cd7e22eecbcc8f84b72c645081fa37fdf4)
- Fixed the problem of null pointer dereference in ossl_sa_free function, and added null value check for input parameters.
  ↳ No PR: [93429fc](https://github.com/openssl/openssl/commit/93429fc0ce9468242a463ff5878cd53b97e7f13f)
- Fixed the null pointer dereference problem caused by incorrect function pointer setting in GCM operations on the s390x platform.
  ↳ No PR: [48e35b9](https://github.com/openssl/openssl/commit/48e35b99bd0071207cfe39da22eb2502db5c09dc)
- Fixed the issue where the record limit counter in GCM mode was incorrectly reset when the AAD changed. It is now only reset when the key changes.
  ↳ No PR: [3ebcb2f](https://github.com/openssl/openssl/commit/3ebcb2fff56bda788ab1f363eb0023715018a4e5)
- Fixed a potential double release problem caused by not making the rrl object empty after releasing it.
  ↳ No PR: [efc84ea](https://github.com/openssl/openssl/commit/efc84eacb7a500306c7cb55e4e2d707dfd9d1ac1)
- Fixed the crash caused by the public key not being set when obtaining the encoded public key parameters, and added an error report when the group was not set, and also corrected the data size parameter.
  ↳ No PR: [b5db237](https://github.com/openssl/openssl/commit/b5db237def7e22ccea1a540ec777045b3ce4600e)
- Fixed the problem of no null check before dereference found by Coverity.
  ↳ No PR: [76ad9ae](https://github.com/openssl/openssl/commit/76ad9ae6fa459af0bd804c01d3d681ec02cddb4b)
- Fixed the resource leak caused by direct return in the do_ssl3_write function, and instead jumped to the error handling path.
  ↳ No PR: [771fef7](https://github.com/openssl/openssl/commit/771fef7793ae572be7567e408a07bfefe6a09ea0)
- Fixed an issue where the X509_REQ_get_extensions function did not log an error when encountering a malformed extension attribute, and will now add the corresponding entry to the error queue.
  ↳ No PR: [e128eaa](https://github.com/openssl/openssl/commit/e128eaa094fc0e95c93081c914c85bd6962a9a42)
- Fixed an issue where the Ed25519 and Ed448 signature operations on the s390x platform did not set the signature length correctly and returned an error when the signature failed.
  ↳ No PR: [bbedc05](https://github.com/openssl/openssl/commit/bbedc052973b1c2fab7d7fb891d02aea393ff579)
- Fixed a crash that may occur when the actual parameter in the check_transactionID_or_nonce() function is NULL.
  ↳ No PR: [aeadd29](https://github.com/openssl/openssl/commit/aeadd2981b214d5e2a8f578179c17b0dccc77042)
- Add test cases for the trace API, and add parameter validity checks in the function that obtains category names and numbers.
  ↳ No PR: [fcff5bd](https://github.com/openssl/openssl/commit/fcff5bd43c85418cc4aa8052e3dc3dba344d763e)
- Fixed the return values of CRYPTO_mem_debug_push() and CRYPTO_mem_debug_pop() so that they correctly return 0 instead of -1.
  ↳ No PR: [f868454](https://github.com/openssl/openssl/commit/f868454257560c78570549f6a34d5918f03898a0)
- Fixed a memory leak problem that may occur when passing in NULL parameters in BN_rand_range(), the error will now be returned immediately.
  ↳ No PR: [70f589a](https://github.com/openssl/openssl/commit/70f589ae41928edda18470ba1c3df82af02a92b3)
- Fixed an issue in TLSv1.3 where session tickets were not sent when the ticket key callback returned 0, and adjusted the state machine to support constructor decisions not to send messages.
  ↳ No PR: [3e93c5f](https://github.com/openssl/openssl/commit/3e93c5fe1eab677500448e18e4274b26e4b246ae)
- Fixed cookie and PSK age calculation errors caused by flipping the low 32 bits of time_t, extending the timestamp field to 64 bits to avoid overflow.
  ↳ No PR: [e8a557d](https://github.com/openssl/openssl/commit/e8a557dc3c1ed16faff4aeb39268f8f5a3f8b81d)
- Fixed the problem of incorrectly calling RLAYERfatal when the record layer pointer is NULL or is about to be released. Use ERR_raise to record errors instead.
  ↳ No PR: [7b7ad9e](https://github.com/openssl/openssl/commit/7b7ad9e578470fe2b20db230638cfc20e3acf252)
- Fixed a possible null pointer dereference issue in the ssl3_cipher function when the encryption context is empty or no password is set.
  ↳ No PR: [35bcac1](https://github.com/openssl/openssl/commit/35bcac131ce5605c504d48a077f33f69660b660c)
- Fixed memory leak in TLS 1.2 compression functionality, properly freeing the SSL3_RECORD structure when releasing the record layer.
  ↳ No PR: [6b5c7ef](https://github.com/openssl/openssl/commit/6b5c7ef7713d913002f94068a3ef1f41b22eafdb)
- Fixed out-of-bounds access issue due to type mismatch in DH key derivation.
  ↳ No PR: [eb7a5cc](https://github.com/openssl/openssl/commit/eb7a5cc3454174094c0c09f1d00aec464ce0f786)
- Fixed the issue where the speed tool did not wait for child processes in multi-process mode, resulting in incorrect statistics, and added child process waiting and status checks.
  ↳ No PR: [56233ba](https://github.com/openssl/openssl/commit/56233ba8574c01b3912cf662335fedaabc7faec2)
- Fixed the bug of prematurely discarding the Initial key during Handshake packet processing in QUIC. The Initial key is now only discarded after successfully decrypting and authenticating the Handshake packet.
  ↳ No PR: [45e7ef5](https://github.com/openssl/openssl/commit/45e7ef5fe34b3f519f1454c47dc08aa4563e4247)
- Fixed handling of status fields in CMP context, used mnemonic constants instead of magic numbers, and updated related documentation.
  ↳ No PR: [19ddcc4](https://github.com/openssl/openssl/commit/19ddcc4cbb43464493a4b82332a1ab96da823451)
- Fixed the record layer memory leak, adjusted the release order to ensure that the record layer is cleaned before releasing the connection BIO.
  ↳ No PR: [9ff5195](https://github.com/openssl/openssl/commit/9ff519542387d32ab1c3a8b1f45a375e1712a383)
- Fixed the processing logic when failInfo PKI status information is not set or missing.
  ↳ No PR: [cba0e2a](https://github.com/openssl/openssl/commit/cba0e2afd6a222aa041e05f8455e83c9e959d05b)
- Fixed logic errors and memory leaks in the CMS_decrypt* series of functions.
  ↳ No PR: [25dd780](https://github.com/openssl/openssl/commit/25dd78048b69c2a780ab1a5378b62447c77a5e75)
- Fixed an issue with checking for wrong ITAVs in the gen_new function.
  ↳ No PR: [7e30349](https://github.com/openssl/openssl/commit/7e3034939b40ee15013bdba9ff6178de6bcc26d4)
- Added a non-null check for the return value of sk_SSL_CIPHER_value in the ciphers command to avoid potential null pointer dereference issues.
  ↳ No PR: [630d312](https://github.com/openssl/openssl/commit/630d31219b343d2654ab03d2e2c7884e764936ab)
- Always use binary format for input files (including standard input).
  ↳ No PR: [4689fe1](https://github.com/openssl/openssl/commit/4689fe1bfd390db591ad5ab5479f06b52ac6f337)
- Enhanced the robustness of pipeline data parsing in speed.c, by adding safe conversion functions and fixing parsing logic to avoid potential parsing errors.
  ↳ No PR: [18af4d1](https://github.com/openssl/openssl/commit/18af4d154cc563a5b02409215a576276caece0f4)
- Fixed an issue where parsing errors were not reported correctly in the duplicated function, and simplified the function implementation.
  ↳ No PR: [66fc90f](https://github.com/openssl/openssl/commit/66fc90f18c44cdac0126c35ffedb99ba7a8b9825)
- Fixed the resource leak problem in the pkcs12 command caused by not jumping out of the loop in time.
  ↳ No PR: [8bc703c](https://github.com/openssl/openssl/commit/8bc703c2886c2104f1d472ab681bc7a8c081427a)
- Fixed the problem of missing null pointer check when strchr returns NULL to avoid undefined behavior caused by this.
  ↳ No PR: [b85d53c](https://github.com/openssl/openssl/commit/b85d53c1670e47273827bba508daff310c3263ab)
- Fixed the problem in the dgram_pair_read_inner function that the pointer is still moved when the buf pointer is NULL.
  ↳ No PR: [9643ddb](https://github.com/openssl/openssl/commit/9643ddb13af88c153c150c91ae538ff04808577e)
- When an asynchronous encryption operation fails, add the error code returned by the kernel to the OpenSSL error queue, along with detailed error information.
  ↳ No PR: [bd19999](https://github.com/openssl/openssl/commit/bd19999b396d03d39eab4a86c6402a970191c9e1)
- Fixed issue with cipher specific cleanup functions not being called when cleaning EVP_CIPHER_CTX.
  ↳ No PR: [f817a74](https://github.com/openssl/openssl/commit/f817a7439eaa705429cf699dd0485e665b0ffc49)
- Fixed regression in i2d_re_X509_REQ_tbs(), removed redundant i2d_X509_REQ_INFO calls and returned their results directly.
  ↳ No PR: [928f15e](https://github.com/openssl/openssl/commit/928f15e71b0bccabb10cbdcbb9b2d4e85eeb5906)
- Fixed possible divide-by-zero exception in division operations.
  ↳ No PR: [3189e12](https://github.com/openssl/openssl/commit/3189e12733e676fbbc30b1b2d98952a6a9f78073)
- Fixed a recursion problem that err_set_debug() could cause when malloc fails.
  ↳ No PR: [ed49476](https://github.com/openssl/openssl/commit/ed49476a16b8ff2688a53a2ba7e011e6911620f8)
- Fix the infinite recursion problem that CRYPTO_THREAD_lock_new may cause when memory allocation fails, use CRYPTO_zalloc instead and avoid setting errors when allocation fails.
  ↳ No PR: [894f216](https://github.com/openssl/openssl/commit/894f2166ef2c16d8e4533e1c09e05ff31ea2f1d8)
- Fix MGF1 digest setting bug for RSA, ensure digest names and attributes are passed correctly when setting OAEP and MGF1 digests, and add support for implicitly rejecting parameters.
  ↳ No PR: [e5a7536](https://github.com/openssl/openssl/commit/e5a7536eaeaacd18d1aea59edeb295fb4eb2dfca)
- Fixed type overflow issues in QUIC congestion control and ACK management on 32-bit Windows, changing size_t in related shift operations and delay calculations to uint64_t.
  ↳ No PR: [5506fbe](https://github.com/openssl/openssl/commit/5506fbeafb888751710f25e8658cf54136702e02)
- Fixed the problem that the old version of EVP_PKEY_CTX object does not support the group parameters of X25519 and X448, and added parameter conversion processing to avoid error reports.
  ↳ No PR: [c048779](https://github.com/openssl/openssl/commit/c048779520d47962316ddb436d08a050d5659666)
- Fixed the problem of returning an error code when receiving a record with only header and no data in DTLS scenario.
  ↳ No PR: [f78c519](https://github.com/openssl/openssl/commit/f78c51995e35889d39cb0bdadcbfa3e144bd8a29)
- Fix for subtraction result in QUIC stream code not being explicitly converted to size_t type on 32-bit Windows.
  ↳ No PR: [44bc72a](https://github.com/openssl/openssl/commit/44bc72a0f2edc343a7b46de8c1b1fc829fef90f7)
- Fixed type conversion and length checking issues with QUIC line format decoding functions on 32-bit Windows.
  ↳ No PR: [e251e7b](https://github.com/openssl/openssl/commit/e251e7ba1ce85d11f3c342b3ae1326a35b7d0b4a)
- Correct the return value of dtls_write_records, use the standard record layer return value instead, and migrate error handling from SSLfatal to RLAYERfatal.
  ↳ No PR: [4cdd198](https://github.com/openssl/openssl/commit/4cdd198ec204a4c2ec6b3ec728ebcc8af04abc86)
- Fix incorrect memory free in EC key encoding functions, ensure ASN1_STRING_free is only called on ASN1_STRING types, and remove unnecessary ASN1_OBJECT_free calls on OBJ_nid2obj return objects.
  ↳ No PR: [8b5424e](https://github.com/openssl/openssl/commit/8b5424eae5577809264e73a229fcc4c384611fae)
- Fix the total_timeout processing logic of RR and GENM transactions in the CMP client to ensure that the timeout check is correctly applied to all transaction types.
  ↳ No PR: [d7d1d09](https://github.com/openssl/openssl/commit/d7d1d0928af2f14e7e187fa8c78115d0d1aa28eb)
- Fixed the problem of the resource release sequence of DRBG and engine in the global default context, releasing DRBG in advance before the engine is released.
  ↳ No PR: [a88e97f](https://github.com/openssl/openssl/commit/a88e97fcace01ecf557b207f04328a72df5110df)
- Fixed a possible memory leak in the CMS_decrypt_set1_password function, clearing the previously set decryption key before setting a new password.
  ↳ No PR: [911045a](https://github.com/openssl/openssl/commit/911045afda06bec038ccd15e9f849bff05b6f1ee)
- Moved the sequence number increment operation when writing DTLS records from post-writing processing to post-encryption processing stage, and added corresponding processing functions.
  ↳ No PR: [421386e](https://github.com/openssl/openssl/commit/421386e392151c267ac7d3de6a2dd23c0ab62aed)
- Refactor thread join and cleanup logic, introduce a universal synchronization wrapper to serialize concurrent join operations, fix race conditions, and remove unsupported force termination functionality.
  ↳ No PR: [4e43bc0](https://github.com/openssl/openssl/commit/4e43bc06f7673597a99f61325543449e72070c8c)
- Delay the release operation of BIO to the final stage of connection cleanup, and ensure that all record layer objects are released before releasing BIO to avoid memory leaks.
  ↳ No PR: [cd6e89b](https://github.com/openssl/openssl/commit/cd6e89b6b6ebe204cc442da9b563213bd67eb27f)
- Fixed the regular expression error in file extension matching in the c_rehash tool to prevent non-certificate files from being mismatched.
  ↳ No PR: [706fc5f](https://github.com/openssl/openssl/commit/706fc5f6ebd63e1fcd18d4764248206ab3c18a0a)
- Fix the tainted scalar problem discovered by Coverity, and add zero value checks for compressed length and uncompressed length when printing compressed certificates to avoid division by zero and null pointer risks.
  ↳ No PR: [5e569f0](https://github.com/openssl/openssl/commit/5e569f0a2e11a59cab7b6f525865232e7770e2f0)
- Fixed an issue reported by Coverity to check whether the buffer is empty before cleaning up temporary packages to avoid uninitialized access.
  ↳ No PR: [d06d5d6](https://github.com/openssl/openssl/commit/d06d5d6b68f39c7f75f1130f984efa78c291fb57)
- Add a check on the return value of BIO_new_fp when creating a BIO output chain. If NULL is returned, NULL will be returned directly to avoid building an invalid BIO chain.
  ↳ No PR: [fb03e61](https://github.com/openssl/openssl/commit/fb03e6145961005a6db011d2f36660d2eed734e2)
- Fixed the problem caused by reseeding after forking when using EGD random source, and adjusted related test conditions to avoid running fork security tests in EGD mode.
  ↳ No PR: [04d07ff](https://github.com/openssl/openssl/commit/04d07ffbed483660c96d3b197df28ab3b1420637)
- Fix asan errors caused by insufficient input/output buffer array lifetime in pipeline mode, declare the array in advance to ensure it is still accessible during the EVP_Cipher call.
  ↳ No PR: [3961af3](https://github.com/openssl/openssl/commit/3961af375e1522a3d37d2af8628bff43103ab4f5)
- Re-enable TLS 1.3 encryption testing, and fix null pointer check in tls_free function.
  ↳ No PR: [50bed93](https://github.com/openssl/openssl/commit/50bed93a7655dc6d990aa42e52b316a97e2dc820)
- Fixed the lock type error in provider_remove_store_methods and changed the read lock to a write lock.
  ↳ No PR: [6962e21](https://github.com/openssl/openssl/commit/6962e21b7c51480343db1a275f52525754dcbe44)
- Fix calculation of encryption growth limit, allowing stitched cipher suites to grow more when encrypting, and add assertions to verify that the reserve space is sufficient.
  ↳ No PR: [830eae6](https://github.com/openssl/openssl/commit/830eae60a61876a5bcd267f47e224269852dcc29)
- Fix insufficient buffer size issue when reading is pipelined, and remove unnecessary early data movement logic.
  ↳ No PR: [8ccde3f](https://github.com/openssl/openssl/commit/8ccde3fc78b8db0acf8c11454b5dc4fb01485f4c)
- Fix the dtls_get_max_record_overhead function so that it returns a more accurate maximum record overhead value and ignores compression.
  ↳ No PR: [b05fbac](https://github.com/openssl/openssl/commit/b05fbac1fc4f9c54a4e7a71728396e8f1b18707e)
- Fixed the problem in the ssl3_dispatch_alert function that the alert cannot be sent when there is pending data writing, and correctly handles the retry scenario.
  ↳ No PR: [7324350](https://github.com/openssl/openssl/commit/732435026b0141063084fb68c076bc1c9fd9bee8)
- Fix memory leak caused by PEM_write_bio_PrivateKey_traditional not releasing the key copy on the wrong path.
  ↳ No PR: [608aca8](https://github.com/openssl/openssl/commit/608aca8ed2becccfe9c238846834ea2b162fc98b)
- Fix the segmentation fault caused by EVP_PKEY being a null pointer when PEM writes the private key, and add corresponding test cases.
  ↳ No PR: [373d901](https://github.com/openssl/openssl/commit/373d90128042cb0409e347827d80b50a99d3965a)
- Unified the use of cryptographic growth macros and fixed the calculation of reserved bytes when MAC is added independently of the cryptographic algorithm, avoiding buffer overflows.
  ↳ No PR: [ecacbc5](https://github.com/openssl/openssl/commit/ecacbc5e3c48901417e8e05bbf1d29df78610607)
- Limits the maximum length of the modulus in large number modulo operations to prevent exceptions caused by excessive allocation on the stack.
  ↳ No PR: [30667f5](https://github.com/openssl/openssl/commit/30667f5c306dbc11ac0e6fddc7d26fd984d546ab)
- Fixed null pointer dereference and resource leak issues in X.509 v3 address validation.
  ↳ No PR: [26cfa4c](https://github.com/openssl/openssl/commit/26cfa4cd85f6b26dd7a48c2ff06bfa4a2cea4764)
- Allow passing NULL pointer when calling ossl_quic_rstream_free to avoid null pointer dereference.
  ↳ No PR: [2124779](https://github.com/openssl/openssl/commit/21247795c0c981299efd02bd1dc0034e4c008f67)
- Fixed handling of zero-length parameters in QUIC transport parameter encoding.
  ↳ No PR: [6946f11](https://github.com/openssl/openssl/commit/6946f1184aa4b0e42cc9c502115bf6c5dd72fa90)
- Fixed the parsing width of the certificate compression algorithm field, changing it from single-byte to double-byte reading.
  ↳ No PR: [ce74e3f](https://github.com/openssl/openssl/commit/ce74e3fb50e1756b14e394acf9dff7362099bb66)
- In the dgst command, when the first argument is a built-in hash name, set it to the digest algorithm name.
  ↳ No PR: [1e5780d](https://github.com/openssl/openssl/commit/1e5780dbc79dab14c1ec1584313755fc2fd2cf55)
- Fixed a memory leak when releasing the DTLS record layer, ensuring that old record layer objects are released correctly when the send message queue is empty.
  ↳ No PR: [20c7feb](https://github.com/openssl/openssl/commit/20c7febc860ae8e67f52912ee205d2e324e7beed)
- Fixed double locking issue in X.509 policy map, removed redundant flag settings.
  ↳ No PR: [4d0340a](https://github.com/openssl/openssl/commit/4d0340a6d2f327700a059f0b8f954d6160f8eef5)
- Fixed undefined behavior caused by left-shifting signed integers in init_info_strings, converting related types to unsigned long integers.
  ↳ No PR: [ee17dcc](https://github.com/openssl/openssl/commit/ee17dcc7ffbd6621f82838c75792f19aa97bd5d7)
- Fixed error checking for ECDH and FFDH performance tests in apps/speed.c, changing return value comparison to less than or equal to zero to correctly handle error conditions.
  ↳ No PR: [9dd009d](https://github.com/openssl/openssl/commit/9dd009dd513276e602b6592bc337a8563a1a82a1)
- Fixed the checking logic of the return value of the EC_GROUP_check_named_curve function to ensure correct validation of named curves.
  ↳ No PR: [3b6154c](https://github.com/openssl/openssl/commit/3b6154ccaf3e64bcdfda4859f2b98ef21b08c5b2)
- In PKCS7 decryption, the implicit reject mechanism is disabled for RSA keys and a new decryption assignment function is used instead to fix the key matching assumption.
  ↳ No PR: [056dade](https://github.com/openssl/openssl/commit/056dade341d2589975a3aae71f81c8d7061583c7)
- Fixed the assertion failure caused by concurrent access to attribute cache in a multi-storage environment. Now when caching attribute definitions, it will check whether entries already exist and reuse them.
  ↳ No PR: [92a25e2](https://github.com/openssl/openssl/commit/92a25e24e6ec9735dea9ec645502cb075a5f8d24)
- Added tests for RR/GENM messages, verifying end_time is properly initialized, and adjusted internal handling of total_timeout.
  ↳ No PR: [b908ec0](https://github.com/openssl/openssl/commit/b908ec0f217da0a23f9d81442f81d44c94c98f23)
- Fixed multiple Coverity issues in HPKE: removed redundant null pointer checks, changed goto to return; added checks for RAND_bytes_ex and KEM_INFO_find return values; removed unused variables and logging code.
  ↳ No PR: [450f96e](https://github.com/openssl/openssl/commit/450f96e965f0d5e89737755364df5933b5085639)
- Fixed bug using wrong encryption level index during handshake key negotiation in QUIC channel, and code cleanup (using assertions and simplified memory copying).
  ↳ No PR: [e28f512](https://github.com/openssl/openssl/commit/e28f512f045b91d4c52b8b9f2ea0800b24203a76), [d8a4451](https://github.com/openssl/openssl/commit/d8a4451fa76c83ba08b42b38848ba9705fbe71a2)
- Added a null pointer parameter check in the ossl_gen_deterministic_nonce_rfc6979 function, and changed the goto end in the error handling path to return directly to fix the resource leak problem reported by Coverity.
  ↳ No PR: [5e42118](https://github.com/openssl/openssl/commit/5e42118de2c8001b3b5fa0cae138950d5b2e1cf1)
- Fixed an issue where errors were incorrectly raised in retryable read operations of BIO_s_dgram_pair, avoiding spurious errors in normal operation.
  ↳ No PR: [3f968ec](https://github.com/openssl/openssl/commit/3f968ecf479ed6ab8a2b25bd1077300baf2287a7)
- Improved QUIC network error handling: Explicitly handle network errors in the demuxer, including detecting stateless reset tokens and returning permanent failure results; distinguish permanent failures from temporary errors in QTX; treat network errors in the channel as connection fatal events, terminate the connection directly when the network BIO fails permanently, and fix related transport parameter parsing and idle timeout handling.
  ↳ No PR: [66eab5e](https://github.com/openssl/openssl/commit/66eab5e08e3a5c7026a3468915ef2e42a43a1479), [0550829](https://github.com/openssl/openssl/commit/0550829f53fe74f884e382ec0ec323342f77d181), [df15e99](https://github.com/openssl/openssl/commit/df15e990ff2557fd43fe4d661c8e1988a3d0ffcc)
- Fixed a divide-by-zero error in the ssl3_mac function caused by a hash size of zero.
  ↳ No PR: [624efd2](https://github.com/openssl/openssl/commit/624efd2ba6f1dabdcdecf17c77bd206c421efdaf)
- Fixed the problem of incorrectly returning FIN when infinite skipping in QUIC send stream processing, and added auxiliary functions and cleanup code.
  ↳ No PR: [05f9735](https://github.com/openssl/openssl/commit/05f97354bb6fe29731a8a25a475a115a2c44720a)
- Fixed the double free problem that may be caused by the failure of OPENSSL_strdup() in set_trace_data(), and adjusted the order of setting channel data to avoid accidental release.
  ↳ No PR: [0fec212](https://github.com/openssl/openssl/commit/0fec2121c0c40d8b098896c9bdf629a48fbafa63)
- Fixed a possible null pointer dereference crash in the CMS decryption function when handling unsupported content types.
  ↳ No PR: [69b995c](https://github.com/openssl/openssl/commit/69b995c6fbc38163d69573803b7aa38ca64b074a)
- Fixed the QUIC server connection status judgment, changing the status from "Handshake Completed" to "Handshake Confirmed" to ensure that the server is not considered connected before handshake confirmation.
  ↳ No PR: [ce8f20b](https://github.com/openssl/openssl/commit/ce8f20b6ae8f95493d86ed2f521ad2c371974f45)
- Fixed an issue where RSA_generate_multi_prime_key would segfault when passing in a NULL index, and added corresponding test cases.
  ↳ No PR: [7efc653](https://github.com/openssl/openssl/commit/7efc653c43851dcbc3ec043baded029c7d31ab9f)
- Fixed the TLS hostname selection problem in CMP applications, ensuring that hostnames without ports are obtained correctly, and adding parameter verification and proxy adaptation; at the same time, the diagnostic information of TLS options was improved, warnings when necessary options were missing, and the verification order and flag bit processing were adjusted.
  ↳ No PR: [30b9a6e](https://github.com/openssl/openssl/commit/30b9a6ec89d97152b5a564b3acf3a94ee57185a7), [ad1a1d7](https://github.com/openssl/openssl/commit/ad1a1d715dcab875dafd6e792b8eb65eb84d6b9f)
- Fixed the issue where the host and port fields in the APP_HTTP_TLS_INFO structure in CMP applications were released prematurely to ensure correct memory management.
  ↳ No PR: [20d4dc8](https://github.com/openssl/openssl/commit/20d4dc8898edc12806ead2100ac09b907662aff6)
- Fixed a null pointer dereference issue in EC key generation due to memory allocation failure, ensuring that parameters are only set after successful context allocation.
  ↳ No PR: [235ef96](https://github.com/openssl/openssl/commit/235ef96049dbe337a3c3c5d419dacbb5a81df1b3)
- Fixed corruption caused by not adding a write lock to OPENSSL_STACK when searching for CRLs in hashed directories, avoiding sk_find mutations by sorting the stack after each modification, and optimizing the handling of installations without CRLs.
  ↳ No PR: [3147785](https://github.com/openssl/openssl/commit/3147785eb23bb27080a0b7accbbff46ac471e86c)
- Fixed bug check for RAND_bytes_ex() in generate_q_fips186_4(), changing condition from <0 to <=0 to properly capture failure cases returning 0.
  ↳ No PR: [a2b01ae](https://github.com/openssl/openssl/commit/a2b01ae1c84ccc250d5d5cb5f2f8714573e3f11b)
- Fixed an issue where errors were not reported correctly when calling BIO_recvmmsg() using dgram pair, ensuring that the cause of the error can be recorded via ERR_raise when an error occurs.
  ↳ No PR: [533390e](https://github.com/openssl/openssl/commit/533390e46f8e2ea55d66d35fd54e724c2fb77571)
- Fixed an issue in the padlock engine where key byte exchange was skipped due to conditional compilation.
  ↳ No PR: [849ed51](https://github.com/openssl/openssl/commit/849ed515c7838943eab42de5c29d6a1f91079a11)
- Fixed the issue of cipher suites being sent repeatedly in QUIC, removed the QUIC-specific TLSv1.3 cipher suite list, and adjusted the cipher suite list creation logic to avoid allocating memory when the list is empty.
  ↳ No PR: [d518854](https://github.com/openssl/openssl/commit/d518854cef2acc8bdc510746898f153ad628d4dc)
- For applications such as storeutl and gendsa, an error message is given when additional parameters appear after the file/URI parameter, and the documentation is improved to indicate that the option must be given before the file/URI parameter.
  ↳ No PR: [323c475](https://github.com/openssl/openssl/commit/323c47532ea7fc79d5e28a0fa58ea0cc4d5196b8)
- Fixed the problem of incomplete X509V3_add1_i2d() return value check, now it can capture both -1 and 0 error codes.
  ↳ No PR: [ecd4454](https://github.com/openssl/openssl/commit/ecd445464a73bb3f125327a604dd13ad16303ebc)
- Fixed error checking in default_fixup_args() on the return value of default_check(), changing the condition from less than zero to less than or equal to zero to correctly handle internal error conditions.
  ↳ No PR: [650f047](https://github.com/openssl/openssl/commit/650f0474282330e3eb2a3df0eff5864bbdcf5845)
- Fixed an issue with incomplete return value checking of EVP_CIPHER_param_to_asn1(), changing the condition from < 0 to <= 0 to correctly capture the error return value.
  ↳ No PR: [e366371](https://github.com/openssl/openssl/commit/e3663717fc16bd140f54ee7f1600bdced7f9ea66)
- Fixed the problem of incomplete check of CMS_SharedInfo_encode return value, and now correctly determines error conditions less than or equal to zero.
  ↳ No PR: [ba06181](https://github.com/openssl/openssl/commit/ba061818e9d76f332e8914dfe9168577b2378dde)
- Fix BIO_set_indent() return value check, change the error condition from less than zero to less than or equal to zero.
  ↳ No PR: [8263749](https://github.com/openssl/openssl/commit/826374921a6b92293fd87655416eda8ef07301c8), [a9ed63f](https://github.com/openssl/openssl/commit/a9ed63f1d1d8993a8b30fc978ce09674f97f061d)
- Fixed two return value errors in ossl_cmp_msg_check_update(), and expanded the CMP version number check to support PVNO_2 and PVNO_3; also corrected the error reason code when recipNonce does not match.
  ↳ No PR: [7f7dafe](https://github.com/openssl/openssl/commit/7f7dafe98b10ef54593df175b901654a0f9890a7), [ed9c6f3](https://github.com/openssl/openssl/commit/ed9c6f363ef2e9e5a7de6a1639e0518f86419c2d)
- Fixed the problem of incomplete return value checking of multiple BIO related functions (BIO_dup_state, BIO_set_md, BIO_set_accept_name) to ensure correct capture of error conditions.
  ↳ No PR: [89601c7](https://github.com/openssl/openssl/commit/89601c72471a4b6bbb9e877f5c54f20eceba5f01), [abf6546](https://github.com/openssl/openssl/commit/abf654645dee168b229f3fa6a365f6a8e4dd7c31), [a811b63](https://github.com/openssl/openssl/commit/a811b6305b1f98e8ec66b8a426d359150fea69b2)
- Fix the handling of -reqin and -rspin options in the CMP client, ensure that the parameters take effect correctly and add necessary nonce updates; also fix the typo in the -newkeypass warning and improve the help text.
  ↳ No PR: [f1e144f](https://github.com/openssl/openssl/commit/f1e144f277fd98a0fde73b884aae541fdc73d063), [1f757df](https://github.com/openssl/openssl/commit/1f757df1f3de0c18cc22a4992d66e9a7b113f61d), [bbaabd1](https://github.com/openssl/openssl/commit/bbaabd16e9fd090ecdc9688f3364c3dbc56512d4), [77aa006](https://github.com/openssl/openssl/commit/77aa00697623bab31b312451855c36789204ed60)
- Fixed multiple bugs in tools in the apps directory: memory leaks in psk_find_session_cb in s_server, incorrect diagnosis of encryption loops in speed testing tools, and crashes in commands such as openssl chacha20.
  ↳ No PR: [8e2552b](https://github.com/openssl/openssl/commit/8e2552b1eac4957214fed55457f64d7d5164ca37), [07626ea](https://github.com/openssl/openssl/commit/07626ea9e5400bd857a58a4da06756748701e9ed), [a8cc0ef](https://github.com/openssl/openssl/commit/a8cc0efe0d8fdd7bfa1d40b3c008d7d6ddf970db)
- Fix idle timeout handling for QUIC channels, preventing transport parameters from setting idle timeout to 0.
  ↳ No PR: [4648eac](https://github.com/openssl/openssl/commit/4648eac53385c5e04bd4ec9dcefe04a74d4221c3)
- Fixed the lock problem during the QUIC handshake process, refactored the handshake function to correctly acquire and release locks, and added an option mask helper function.
  ↳ No PR: [4a53018](https://github.com/openssl/openssl/commit/4a530180e5b9921bc3d1b5228d9be96f2a0b4b07)
- Fix typos in QUIC Thread Assisted Mode, correct mutex type from CRYPTO_RWLOCK to CRYPTO_MUTEX, and adjust compilation conditions.
  ↳ No PR: [c4208a6](https://github.com/openssl/openssl/commit/c4208a6a983278316c6615980f335f685c0be472)
- Fixed the time unit error in early data age calculation, and corrected the misused second granularity to millisecond granularity.
  ↳ No PR: [0513a38](https://github.com/openssl/openssl/commit/0513a38364a7a45c946fdd8f7d87b8a3ae01ffbb)
- Fixed the setting and copying issues of digest property in FFC parameters.
  ↳ No PR: [3307338](https://github.com/openssl/openssl/commit/3307338e26862070eaacad6ec7537a63a63b8a90)
- Fixed an issue where irrelevant error entries remained in the error queue when early data decryption failed.
  ↳ No PR: [79abf0d](https://github.com/openssl/openssl/commit/79abf0dff90d54840b8afa6270ea816ee2edd345)
- Fixed the problem of certStatus memory leak in CMP message construction, releasing certStatus when push fails.
  ↳ No PR: [c9c9901](https://github.com/openssl/openssl/commit/c9c99018a887bfac1fe5a5ae6dcd8a5647494504)
- Added null pointer check for memory allocation failure in stream_frame_new function to prevent potential null pointer dereference.
  ↳ No PR: [bf762f9](https://github.com/openssl/openssl/commit/bf762f9203d3b5541c21f2b376750e32ebf36651)
- Check the return value of DSA_set0_key in the ossl_dsa_key_from_pkcs8 function and generate an error message if it fails.
  ↳ No PR: [dd573a2](https://github.com/openssl/openssl/commit/dd573a2fc1e8806c67420a5d6df0de175745aaf8)
- Fixed sendto problem caused by address family size mismatch in dgram_sendmmsg, use BIO_ADDR_sockaddr and BIO_ADDR_sockaddr_size to obtain address and size instead.
  ↳ No PR: [a868170](https://github.com/openssl/openssl/commit/a8681703d48d062c2fc1736179218063275f8e33)
- Fixed the error of misuse of local instead of peer when initializing time field and clearing address in QUIC DEMUX.
  ↳ No PR: [29fb7f0](https://github.com/openssl/openssl/commit/29fb7f087994b5cffe1613da25bb8c3231e59e15)
- Fixed the mismatch between size_t and int types in cms_ec.c, and improved error handling.
  ↳ No PR: [559e078](https://github.com/openssl/openssl/commit/559e078d94f1213318105b03f4e88b848fc28314)
- Fix segfault caused by passing wrong context when cleaning parent random number generator.
  ↳ No PR: [6d45fd4](https://github.com/openssl/openssl/commit/6d45fd47f4849c8dc55b8dd5fa1e1b8a158774a0)
- Fixed an error in the key pair verification logic in the rsa_has function to ensure that the presence of modulus n is correctly verified when checking the private key.
  ↳ No PR: [a320716](https://github.com/openssl/openssl/commit/a3207163ef3d30658a41a9c9e3750ca4c5b16677)
- Fix the comparison logic of pkeyid in tls12_check_peer_sigalg, use EVP_PKEY_KEYMGMT instead of hard-coded -1.
  ↳ No PR: [a2a543e](https://github.com/openssl/openssl/commit/a2a543e0e3ec277d136772b4b0e0bb3d1181d337)
- Fixed the resource leak problem caused by memory allocation failure in the ssl_cert_dup function.
  ↳ No PR: [b36e677](https://github.com/openssl/openssl/commit/b36e677f8f563301207ea658e29b3a8f88c2951b)
- Fix Windows macro name detection error in quic_reactor, and use INVALID_SOCKET instead of -1 as invalid socket value.
  ↳ No PR: [d293ebd](https://github.com/openssl/openssl/commit/d293ebde01fc14dabbd64fd6e42dc837be7b1fad)
- Limit the maximum sleep time of the sleep function to avoid long loop waiting caused by passing in too large values.
  ↳ No PR: [bea92b8](https://github.com/openssl/openssl/commit/bea92b8c3d61960a2d06f8d342ef01d30a2fa195)
- Fix the compatibility issue of UINT64_C macro in argon2 KDF implementation under old compilers and use explicit UL suffix instead.
  ↳ No PR: [4b738c1](https://github.com/openssl/openssl/commit/4b738c1ac945a3f1a985df79ff8c37a23d2f2fe0)
- KDF context is no longer released in the derive error path to avoid problems caused by premature release.
  ↳ No PR: [6ec3d31](https://github.com/openssl/openssl/commit/6ec3d3125f76aa9f11c133333f868c42b9b585c4)
- Fixed mutex operation and lock release issues in QUIC thread-assisted mode, and introduced NAT timeout macro.
  ↳ No PR: [9cf091a](https://github.com/openssl/openssl/commit/9cf091a3c5f34277dca1cac979c7d632c7236d7b)
- Fix DSA_sign's bounds checking for negative p, q, g values and add related tests.
  ↳ No PR: [9559ad0](https://github.com/openssl/openssl/commit/9559ad0e8d433a2a212b63cc848fa2ac82a9b048)
- Fix the memory leak caused by ECDSA_sign calling i2d_ECDSA_SIG when the signature pointer is NULL, and add test cases.
  ↳ No PR: [4befe81](https://github.com/openssl/openssl/commit/4befe81a99b89c52b749a87eece82c1cba4fab12)
- Fixed a segfault caused by missing null pointer check in EVP_PKEY_CTX_dup, and added null value judgment for dupctx function pointer when copying signature, key exchange, asymmetric cipher and key encapsulation context.
  ↳ No PR: [864c70e](https://github.com/openssl/openssl/commit/864c70e43ea5f1d7fe20bfea457e53e79fd46b6e)
- It is forbidden to use QUIC connection when ALPN is not specified, otherwise an error will be reported and terminated; related test cases will be added.
  ↳ No PR: [d98f421](https://github.com/openssl/openssl/commit/d98f4212b778e3b6b7c15b9fce0a3531f59777a2), [122d4e2](https://github.com/openssl/openssl/commit/122d4e20cd2e88daa64d8bfcd7b8a6e39a0260e4)
- Fix the lock contention issue during QUIC datagram injection and ensure correct locking when calling SSL_inject_net_dgram.
  ↳ No PR: [5129e59](https://github.com/openssl/openssl/commit/5129e59494cb057bf8f744d7a5d390efa7914c67)
- Fixed the problem in DTLS that application data records were not processed correctly due to out-of-order, and now allow buffering of application data records from the next epoch.
  ↳ No PR: [5c47697](https://github.com/openssl/openssl/commit/5c476976ab8ef057ddbd8f110249d7c796a7f1b1)
- Fix condition variable wait logic, use correct functions for signaling and adjust wait state masks.
  ↳ No PR: [7123606](https://github.com/openssl/openssl/commit/712360631ff95b412883fbcd56dd44752d427565)
- Fixed a potential null pointer dereference issue in the get_payload_public_key_ec function, which returns directly when checking eckey for null.
  ↳ No PR: [bbe9d2d](https://github.com/openssl/openssl/commit/bbe9d2de6c643a2c6758fae4274c307943a59624)
- Fix incorrect null pointer check in evp_keymgmt_gen_cleanup function, change the condition from checking gen to checking gen_cleanup.
  ↳ No PR: [6469043](https://github.com/openssl/openssl/commit/6469043bbabc9728aed61d7708c32e2ae319be1d)
- Move the initialization call of configuration loading out of RUN_ONCE to avoid initialization problems caused by recursive calls.
  ↳ No PR: [540c2d1](https://github.com/openssl/openssl/commit/540c2d175d3c7c28bb969a74f6fe0396f0addc1a)
- Fixed the problem of incorrectly using the public key operation during ECX key generation, and changed it to the correct key generation operation.
  ↳ No PR: [40f4884](https://github.com/openssl/openssl/commit/40f4884990a1717755df366e2aa06d01a1affd63)
- Fixed an error in least common multiple (LCM) calculation in RSA multi-prime key verification.
  ↳ No PR: [efbff4d](https://github.com/openssl/openssl/commit/efbff4de3e259cee71a4e1bbd86b30ebd86bbdae)
- Fixed an issue where the set decryption key function was incorrectly used in SM4-GCM hardware acceleration initialization on Kunpeng-920.
  ↳ No PR: [524c2ca](https://github.com/openssl/openssl/commit/524c2cab6a64f408a5444188c2052b4d76b06775)
- Fixed parameter checking and memory allocation issues in EVP and X509 modules, including check_curve return value judgment, curve name string space allocation and ctrl_cmd default settings.
  ↳ No PR: [4e5f3d6](https://github.com/openssl/openssl/commit/4e5f3d691343a691ddae739c51f7ae71e9893c98), [ac52fe5](https://github.com/openssl/openssl/commit/ac52fe5f5ae7a1d062f09adab7744e3a3b2ddbcf), [1009940](https://github.com/openssl/openssl/commit/1009940c14716ac03d5f161bdb4ae626ec6fe729)
- Fixed self-signed warning when loading a CSR file with the -vfyopt option, by passing the validation options argument to the CSR load function.
  ↳ No PR: [a75f707](https://github.com/openssl/openssl/commit/a75f707fcaaed5c9b26e0ddfc0e0529957a11a1d)
- Fixed a memory leak caused by not releasing memory when insertion failed in engine_cleanup_add_first().
  ↳ No PR: [8c63b14](https://github.com/openssl/openssl/commit/8c63b14296f117b07781509ced529a8955d78fb9)
- Fixed the issue where SSL_trace could not print certificate data under non-default libctx, and corrected the certificate parsing logic to correctly use the specified libctx and attribute query.
  ↳ No PR: [b946a3e](https://github.com/openssl/openssl/commit/b946a3eed5c40230955d5acc67884c3fd2fd6b18)
- Fixed the problem of unstable rehash results, and ensured that file entries are sorted correctly by implementing a comparison function.
  ↳ No PR: [31c94b5](https://github.com/openssl/openssl/commit/31c94b5e1159b5435b2354e6525355ec33683ecc)
- Fix the use of time callback in QUIC TXP to ensure that the time callback function is called correctly.
  ↳ No PR: [b98c38d](https://github.com/openssl/openssl/commit/b98c38d40a9d27a155d88208640430fffa47e28c)
- Fixed the use-after-free issue caused by memory allocation failure when adding x509 policy nodes.
  ↳ No PR: [de53817](https://github.com/openssl/openssl/commit/de53817ec386ea9e943d8f33716945dd9dbe1f31)
- Fix the error handling of ossl_policy_level_add_node and sk_X509_POLICY_NODE_push in the tree_calculate_user_set function to prevent memory leaks and correctly return the failure status when user_policies allocation fails.
  ↳ No PR: [95a8aa6](https://github.com/openssl/openssl/commit/95a8aa6dc0e283b1560dd3258d2e9115c02659b1)
- The SMIME_crlf_copy function adds a null pointer check for input parameters and returns an error when a null pointer is passed in.
  ↳ No PR: [23450cf](https://github.com/openssl/openssl/commit/23450cfb9204615e97467e8be6a709141523a59e)
- Improve the management of CMP client HTTP callback parameter pointers, release the old value before setting the new value, and make it empty during cleanup to avoid memory leaks or dangling pointers.
  ↳ No PR: [dea5e26](https://github.com/openssl/openssl/commit/dea5e2632ca7f3ab48f947359501a7e3f28db178)
- Fixed the issue of pport_num not being initialized in OSSL_parse_url, and added the init_pint auxiliary function to initialize the integer value pointed to by the pointer.
  ↳ No PR: [ba189e0](https://github.com/openssl/openssl/commit/ba189e0a4bdea86b6142da36adc7f054b6f08c6e)
- Fixed the problem that parameters are not converted to unsigned char type when calling functions such as isdigit.
  ↳ No PR: [8229874](https://github.com/openssl/openssl/commit/8229874476cc2955e6947cf6d3fee09e13b8c160)
- Fixed a memory leak that could occur in the ASN1_TIME_normalize function when the input pointer is null.
  ↳ No PR: [a33842e](https://github.com/openssl/openssl/commit/a33842efa51ca3f021310e10f444afef1e779fee)
- Fixed an issue where X509_NAME_cmp might incorrectly return -2 when handling empty names.
  ↳ No PR: [ec59752](https://github.com/openssl/openssl/commit/ec59752835f616860cd9451d6cfcea16bfc3ad05)
- Fix an issue where inappropriate groups are requested in HelloRetryRequest, ensuring that groups that the client has sent but do not comply with TLSv1.3 requirements are not requested again.
  ↳ No PR: [7a949ae](https://github.com/openssl/openssl/commit/7a949ae5f1799a6629cf6deb44ae0f38455a73dd)
- Fixed int_ctx_new() error when using 1.1.1n SM2 key and EC method engine.
  ↳ No PR: [4c4fefa](https://github.com/openssl/openssl/commit/4c4fefa5c78a49b63113aec35a2bc8d6d9432436)
- Fixed an issue that caused a busy loop due to miscalculation of the next tick deadline when an ACK could not actually be sent.
  ↳ No PR: [ca71165](https://github.com/openssl/openssl/commit/ca711651c19530b54f0dd6f7ff6b24b5c8d016a2)
- When trying to decode a PKCS#12 object, first check if a MAC exists for authentication, to avoid always prompting for a password without a MAC.
  ↳ No PR: [7a52061](https://github.com/openssl/openssl/commit/7a520619c997146639f42ce8595162ac34c2ad41)
- Fixed the issue where the openssl speed -multi -evp command outputs incorrect algorithm name. The specified algorithm name can now be displayed correctly.
  ↳ No PR: [33c0934](https://github.com/openssl/openssl/commit/33c09341bb081682535be0450ff6032df47ea141)
- Fixed the problem of input data being truncated during pkeyutl decryption, now allowing the complete input data to be read.
  ↳ No PR: [8494507](https://github.com/openssl/openssl/commit/849450746f38a5658ef783abb0a8c79ae2861464)
- Fixed memory allocation and reference counting issues in EC_KEY, EVP_RAND and SSL_CTX, including correctly initializing reference counting, releasing allocated resources when allocation fails, and adding error logs.
  ↳ No PR: [97beb77](https://github.com/openssl/openssl/commit/97beb77f319f119957235233396627bb22283da0)
- Fix the processing logic of non-ACK triggered packets in QUIC TXP, ensure that the probe request count is decremented correctly, and optimize the flow frame generation and filling behavior.
  ↳ No PR: [178c104](https://github.com/openssl/openssl/commit/178c104de68ebf981ae1813a3e0548bbb1051a75)
- QUIC ACKM no longer records non-transmitting data packets to congestion control to avoid incorrect notification to CC in pseudo packet loss scenarios.
  ↳ No PR: [427a02a](https://github.com/openssl/openssl/commit/427a02ad0a71a50c9be125d860a84d4e07d09f1e)
- Remove the unreachable type checking code in SSL_CTX_use_certificate_file and fix the error code.
  ↳ No PR: [33ef5fc](https://github.com/openssl/openssl/commit/33ef5fc2c2bf0b0587bfcba28f61329abd83be70)
- Fixed an issue in QUIC packet encoding where pointers may become invalid when the dynamic buffer grows.
  ↳ No PR: [69aef72](https://github.com/openssl/openssl/commit/69aef722645a6b0b2708ca3f08dde1599e2998a4)
- Fixed the conditional judgment when handling write retry in ssl3_do_write(), and changed the return value check from less than 0 to less than or equal to 0 to correctly handle the situation where BIO returns 0.
  ↳ No PR: [404fb99](https://github.com/openssl/openssl/commit/404fb9965ed0dc7752d80f72c93358dfb45125c8)
- Fixed parameter handling errors when setting/getting tags in RSA OAEP in older versions of the engine.
  ↳ No PR: [64b1d2f](https://github.com/openssl/openssl/commit/64b1d2fb06c9a5233dcabfe130036ff95c3fdaae)
- Fixed the problem of incorrect generation of forced PING frames in QUIC TXP, ensuring that PING is generated correctly when forced confirmation is required.
  ↳ No PR: [1e2e683](https://github.com/openssl/openssl/commit/1e2e683aa289849483ea9d48e9fcdda9559028ec)
- Use safe multiplication and division functions in QUIC flow control calculations to expand the range of possible results.
  ↳ No PR: [24ae2d7](https://github.com/openssl/openssl/commit/24ae2d79d57dd60f2617502d751d0ef78c571307)
- Fix the unreachable code in cms_main(), adjust the processing logic of recipient certificate parameters during non-encrypted operations, and add corresponding warning information.
  ↳ No PR: [8c34367](https://github.com/openssl/openssl/commit/8c34367e434c6b9555f21cc4fc77a18d6ef84a85)
- Fixed a bug generated by STREAM FIN in QUIC TXP, correctly clearing the FIN flag when the data block is truncated.
  ↳ No PR: [553122c](https://github.com/openssl/openssl/commit/553122cd7cefaad68826f37455c7644dc6cd72b9)
- Fixed typo in QUIC channel status enumeration name, correct QUIC_CSM_STATE_ACTIVE to QUIC_CHANNEL_STATE_ACTIVE.
  ↳ No PR: [6861f5a](https://github.com/openssl/openssl/commit/6861f5a703ebd6547bbe598d7fe4c7de9912e384)
- Fixed the problem of X509at_add1_attr function searching the wrong stack when checking duplicate attributes, and changed it to correctly search the target stack.
  ↳ No PR: [7551264](https://github.com/openssl/openssl/commit/7551264186f176ca5801aa84d60c7b91d8fba31f)
- Fixed the problem of mac_export function exporting empty data when empty selection, and added checking of private key selection flag.
  ↳ No PR: [1ae4678](https://github.com/openssl/openssl/commit/1ae4678cebaa13604c0f31bdf2c64cd28bdaf287)
- Add offset bounds checking to QUIC protocol decoding function, compliant with RFC 9000 section 19.6 specification.
  ↳ No PR: [67e72ed](https://github.com/openssl/openssl/commit/67e72ed575f6be1a29a8be8f785b1a1150588b44)
- Added QUIC test case to verify malformed encrypted stream data, and fixed type conversion issues in related code.
  ↳ No PR: [de56eeb](https://github.com/openssl/openssl/commit/de56eebd6ac0805172d74c5d5679ca7425ccc631)
- Added a fault injection test case for NEW_CONN_ID frames for QUIC testing, and fixed the processing logic for non-1-RTT packets when injecting ordinary frames.
  ↳ No PR: [ed75eb3](https://github.com/openssl/openssl/commit/ed75eb32f3712b80a47ad783d0082c66164c732f)
- Fixed the bug in QUIC TXP that the TXPIM package may still be used after being released, and introduced a reference counting flag to avoid access after release.
  ↳ No PR: [6a2b70e](https://github.com/openssl/openssl/commit/6a2b70e21b0ae4a6d1550a86833f3996b78b6755), [6db5cb8](https://github.com/openssl/openssl/commit/6db5cb844852f8f13753caf26dea7750f701e4d9)
- Added fault injection test cases for QUIC multi-stream testing for STREAM, MAX_DATA and MAX_STREAM_DATA, and fixed the injection function's check of packet type.
  ↳ No PR: [1623bf3](https://github.com/openssl/openssl/commit/1623bf374d4ee3119629c33938fcd075bd79e6a8)
- Fixed the issue in the QUIC protocol that the handshake was not advanced when writing with null length, ensuring that the handshake can be completed normally even if zero bytes are written.
  ↳ No PR: [33f6ad1](https://github.com/openssl/openssl/commit/33f6ad1724b2f32a370d01b61ef12120a75d8049)
- Fix quicserver not properly tracking buffer write locations when handling requests arriving in chunks.
  ↳ No PR: [747b51f](https://github.com/openssl/openssl/commit/747b51f48338e3b7e53d0b7a87002edefc7e8439)
- Fixed the regression problem in QUIC UINT_SET removal operation, corrected the range overlap judgment condition and added range truncation processing.
  ↳ No PR: [dc5e5c5](https://github.com/openssl/openssl/commit/dc5e5c51e2ffa8e6f472eeb13efea3b3e113a6d1)
- Fixed a memory leak problem caused by memory allocation failure in the event queue.
  ↳ No PR: [77a6611](https://github.com/openssl/openssl/commit/77a66117ab0c5bdd885d13dc302ace7010aca826)
- Fixed an issue with handling negative IV length values in QUIC QRX to avoid assertion errors caused by type mismatch.
  ↳ No PR: [b538ae4](https://github.com/openssl/openssl/commit/b538ae4fbf1d9c800d2ed1cc6c317b36572ec7bb)
- Fix possible null pointer dereference issue in QUIC QTLS.
  ↳ No PR: [4d6ca88](https://github.com/openssl/openssl/commit/4d6ca885998f7c397d8224290a32a27967a97c0b)
- Fixed type conversion problem when handling negative IV length in QUIC QTX, ensuring nonce is constructed correctly.
  ↳ No PR: [a2d4915](https://github.com/openssl/openssl/commit/a2d4915ab2730797f97c90a127084a668733c96c)
- Fixed the problem that the return value of block_until_pred is not checked when the QUIC connection is closed, to avoid errors caused by continued execution after the blocking wait fails.
  ↳ No PR: [23406e3](https://github.com/openssl/openssl/commit/23406e304f4d2406e6aa51c44b8f8dc2612e63fc)
- Fixed the problem that the return value of ossl_quic_rstream_read in QUIC TSERVER was not handled correctly, and related variables were correctly cleared when the read failed.
  ↳ No PR: [f540b6b](https://github.com/openssl/openssl/commit/f540b6b4f6608fa5edfa2ec77fce6d3c92bb9a1f)
- Fixed a null pointer dereference problem in QUIC UINT_SET due to unchecked memory allocation results.
  ↳ No PR: [8761efb](https://github.com/openssl/openssl/commit/8761efb2ccc96f81201af279ec66e8ceeee9c7a3)
- Add selection checks for msblob and pvk decoders, ensuring they are only used if the requested key selection matches.
  ↳ No PR: [6207f2b](https://github.com/openssl/openssl/commit/6207f2b657b5ba1823681b49c7c34c619da0dd00)
- Fix the error message format in the load_key_certs_crls function: add missing newlines and remove redundant error prompts.
  ↳ No PR: [81d037b](https://github.com/openssl/openssl/commit/81d037b8adb0232c8a4d4654f79c883dafb102bc)
- Improve the warning text when skipping unknown name attributes in parse_name(), and fix the processing logic when maxlen is -1 in bio_to_mem().
  ↳ No PR: [49e0973](https://github.com/openssl/openssl/commit/49e097344ba51a8b25016794d482813b9c1e137f)
- Fixed an issue where -csr and -serial option values could not be reset.
  ↳ No PR: [374945a](https://github.com/openssl/openssl/commit/374945a9aa545d4d6f015de0b48cbed6a90258e0)
- Fixed the problem of incorrectly triggering the wrong envelope content type when releasing the signature content, and added a dedicated function to clean up the envelope content.
  ↳ No PR: [13342ef](https://github.com/openssl/openssl/commit/13342efbb9e16ec8f97b1ac5ab4aa2b3b3490596)
- Fixed the problem of not clearing the el->md pointer under the wrong path to avoid potential memory errors.
  ↳ No PR: [9d005ba](https://github.com/openssl/openssl/commit/9d005bafacbaf9e8ac8c2e1bf90b124c4254022b)
- Fixed the life cycle management problem of dummybio in the QUIC record layer to avoid use-after-free errors.
  ↳ No PR: [643f542](https://github.com/openssl/openssl/commit/643f542a89bee93e043d0899b2a1ca700d1cc418)
- Fixed the problem of reason_len not being set in QUIC protocol error handling, and corrected the return value logic of has_read_ended function when reading fails.
  ↳ No PR: [f260900](https://github.com/openssl/openssl/commit/f2609004df4d91a365338e11d04ff67589f2d3e3)
- Fixed a divide-by-zero error in kmac_setkey caused by a block size of zero, returning an error instead.
  ↳ No PR: [91895e3](https://github.com/openssl/openssl/commit/91895e39b10033178e662fc7427a09d7562cf8e1)
- Added appropriate error promotion in multiple locations in QUIC, including protocol errors and parameter errors, and optimized the validation logic of polling descriptors.
  ↳ No PR: [9601484](https://github.com/openssl/openssl/commit/96014840b69b3ec2f82e230a27cc5c1fa3bfb1bc)
- Improved QUIC application layer error reporting, changed some non-protocol errors to non-I/O error types, and restructured the channel configuration process to use a unified context; also added the transmission of the connection closure reason and its length.
  ↳ No PR: [2e17601](https://github.com/openssl/openssl/commit/2e1760118b5ba316cdf0b144a21fb4c21f796c71), [40c8c75](https://github.com/openssl/openssl/commit/40c8c756c86fc17751b989426aa66fb33319c4ca)
- QUIC channels now only handle the first protocol error, subsequent protocol errors will be ignored.
  ↳ No PR: [549d0a7](https://github.com/openssl/openssl/commit/549d0a700be311d9a65560cb9eed3f725546b5ed)
- Improved the error message of QUIC TLS, returning a more clear error code and prompt when ALPN is not configured.
  ↳ No PR: [881e329](https://github.com/openssl/openssl/commit/881e3299dcadd65cc4a2843ba47abc6548ced8f4)
- Fixed the implementation of the BIO_CTRL_DGRAM_GET_LOCAL_ADDR_ENABLE control command in BIO_s_dgram_pair so that it correctly returns the result through the pointer parameter.
  ↳ No PR: [c20b78d](https://github.com/openssl/openssl/commit/c20b78d59960c523c4de02e7bd62fcd4c0a5a4f7)
- Added return value check for RAND_bytes(), calling app_bail_out to exit when failed; at the same time, changed the output buffer parameter to inp.
  ↳ No PR: [8d120ae](https://github.com/openssl/openssl/commit/8d120aef951d7bb7deac0b8b559f8003f5ea6384)
- Fixed the problem of premature discarding of the INITIAL encryption level in the QUIC protocol. Now the discarding is only triggered when the server successfully decrypts the HANDSHAKE packet, and the client discards when the HANDSHAKE packet is successfully sent.
  ↳ No PR: [b6125b5](https://github.com/openssl/openssl/commit/b6125b54ededb83ca930174718157d73561523ad)
- Fixed the problem of incorrect use of ossl_assert when bn_wexpand memory allocation fails, and instead directly checks whether the return value is NULL.
  ↳ No PR: [69b9a99](https://github.com/openssl/openssl/commit/69b9a992961c27ac6d0f0bec259806ac953a81d4)
- Fixed a memory leak caused by process_data_dest in the wrong path being not released when copying OSSL_DECODER_CTX.
  ↳ No PR: [e16c010](https://github.com/openssl/openssl/commit/e16c0103083af676af8c5564bb21585d4574f992)
- Fixed premature release of the previous BIO when setting up a new record layer, avoiding release while it was still referenced.
  ↳ No PR: [92e3f43](https://github.com/openssl/openssl/commit/92e3f43aec553145b4d4cbb4dbd3df9658a05bb4)
- Fixed a memory leak in tls_new_record_layer: when setting encryption status fails, tls_int_free is now correctly called to free the partially allocated record layer structure.
  ↳ No PR: [0577dba](https://github.com/openssl/openssl/commit/0577dbad0709f1b3717297420069c6160245e74d)
- Added check for ASN1_STRING_set return value in spkac_main function, fixing potential unchecked return value problem.
  ↳ No PR: [20baa24](https://github.com/openssl/openssl/commit/20baa24f9f3997a96db7cd176a6ef609afe80cea)
- Removed a redundant NULL check in cmp_genm.c that would not actually trigger. This change should eliminate Coverity false positives.
  ↳ No PR: [2b2eedf](https://github.com/openssl/openssl/commit/2b2eedfdd614e4c5e2104acf44da0bcdd5b90ade)
- Fixed an issue where the return value of X509_STORE_lock() was not checked in ossl_x509_store_ctx_get_by_subject().
  ↳ No PR: [6404d06](https://github.com/openssl/openssl/commit/6404d064b8012a2c353603a3b3effa6289313d61)
- Fixed the problem that when sending data, when the amount of data exceeds the capacity of a single datagram, datagrams will continue to be generated and sent until all data is sent.
  ↳ No PR: [aa43301](https://github.com/openssl/openssl/commit/aa433014bb36bfff0af17c0eb9d25b6fb2d7d068)
- All fields of RXE are correctly initialized for QUIC unencrypted packets.
  ↳ No PR: [413a427](https://github.com/openssl/openssl/commit/413a427c2a7743474f57d5799f42de5357ceace2)
- Fixed the QUIC channel sending logic to ensure that the sent packets can still be refreshed when packet generation fails; at the same time, an error reason parameter was added for closing the local connection.
  ↳ No PR: [64fd699](https://github.com/openssl/openssl/commit/64fd69911e04cec45f65b396a4e91d6caa4fdc9a)
- Fixed a memory leak caused by the incorrect path in the ossl_encode_ctx_setup_for_pkey function not releasing the allocated name stack.
  ↳ No PR: [8ef63b6](https://github.com/openssl/openssl/commit/8ef63b6ff8301a0139c00df6c40173a63fd2db01)
- Changed TLS record type from int to uint8_t, avoiding endianness issues in SSL_trace().
  ↳ No PR: [1cc8c53](https://github.com/openssl/openssl/commit/1cc8c53b0fc06d148a9f62e5d2d5bcd859f948cf)
- Repair the PING frame processing logic in QUIC, adjust the unknown frame error code and optimize the frame callback mechanism.
  ↳ No PR: [de85ec0](https://github.com/openssl/openssl/commit/de85ec03f5c6044fae8f2d1812d59aab0687b12a)
- Dynamically determine I/O errors, improve QUIC error classification and processing logic; reconstruct QUIC I/O error processing, add a new auxiliary function to uniformly set last_error, and initialize the error status to no error when entering I/O operations.
  ↳ No PR: [a954f76](https://github.com/openssl/openssl/commit/a954f761feb9ace245ea425d3b746ec6602580f3), [72ca0b8](https://github.com/openssl/openssl/commit/72ca0b88fc8cd97a20528d2f92e145e181194a98)
- Generalize the CMP protection calculation function to correctly support Edwards curves, and add corresponding test cases.
  ↳ No PR: [e664ef7](https://github.com/openssl/openssl/commit/e664ef78b92532bf94c7976b181d88c4abf83074)
- Added data availability check when peeking at the range number of ACK frames to prevent memory over-allocation caused by declaring too many ranges.
  ↳ No PR: [a31601c](https://github.com/openssl/openssl/commit/a31601cc3ffca7de688aabcd34d83ff2c4496e17)
- Handle non-IO retry errors during TLS handshake in QUIC connections (such as SSL_ERROR_WANT_RETRY_VERIFY, SSL_ERROR_WANT_X509_LOOKUP, etc.) and propagate these errors up to QCSO.
  ↳ No PR: [3a0012c](https://github.com/openssl/openssl/commit/3a0012cb52bef4df54bd46946d7ff783c24b4305)
- Fixed the condition judgment error in the dupctx function of the aes_gcm_siv cipher family so that it can correctly copy data when aad is not empty.
  ↳ No PR: [c32c3f2](https://github.com/openssl/openssl/commit/c32c3f2653e6c6ac42e09a83a2f51f8667827a04)
- Fixed possible memory leaks in CRYPTO_zalloc and CRYPTO_realloc when OPENSSL_MALLOC_FAILURES is enabled, and adjusted the fault injection check location.
  ↳ No PR: [e2cf38d](https://github.com/openssl/openssl/commit/e2cf38d5751d6b48c8625b622c3765d0a39958d7)
- Fix ossl_param_build_set_multi_key_bn function to avoid setting NULL BIGNUM value to zero incorrectly.
  ↳ No PR: [15a39e7](https://github.com/openssl/openssl/commit/15a39e7025e0ed4e31664c499894006e41582068)
- Fix error handling in engine cleanup function, resolve memory leaks and adjust rollback logic.
  ↳ No PR: [00f2efc](https://github.com/openssl/openssl/commit/00f2efccf5b9671a7af2b12571068258e9c255a5)
- Fix the clearing and setting logic of error flags in OSSL_STORE.
  ↳ No PR: [17dd9a2](https://github.com/openssl/openssl/commit/17dd9a2c6262c00800301fddd9441a9c590a630e)
- In several demos and tools, NULL is explicitly returned when creating BIO fails.
  ↳ No PR: [11b7d46](https://github.com/openssl/openssl/commit/11b7d46fa7e2684e0ad0f12a7806163dba99983d)
- Fixed the memory leak caused by users_pwd not being released in the SRP_VBASE_new function.
  ↳ No PR: [68e95f7](https://github.com/openssl/openssl/commit/68e95f7840d0d8ac4e5e03381cf9d305578dd1c7)
- Fixed the valtype value of the dkeyform option from uppercase F to lowercase f to support engine functionality.
  ↳ No PR: [b9a189c](https://github.com/openssl/openssl/commit/b9a189ce87fde1de4bf691031624538262f005c5)
- Fixed the checking method of error return value in cms_sd_asn1_ctrl() function.
  ↳ No PR: [00a413e](https://github.com/openssl/openssl/commit/00a413e2483257a17239cef5dde52df14926284c)
- Fix memory leak when RSA-PSS parameter encoding fails in rsa_pub_encode function.
  ↳ No PR: [285eb16](https://github.com/openssl/openssl/commit/285eb1688f05ad477fefc681bf05d0afedc46d40)
- Fix for corrupted output in the req command when used with the -out and -modulus options.
  ↳ No PR: [d287394](https://github.com/openssl/openssl/commit/d2873946dfaff5537ea3d1adf3890e33a3f276ff)
- Fixed a memory leak in OpenSSL applications to ensure proper cleanup when key generation and parameter generation failed.
  ↳ No PR: [8c040c0](https://github.com/openssl/openssl/commit/8c040c086ca11a519975c58961a5dc933aa6524a)
- Fix memory leak in prepare_rsa_params function when negative salt length or out of memory.
  ↳ No PR: [46def82](https://github.com/openssl/openssl/commit/46def829afa4d8bed8f53d484bdf842d65f0e176)
- Fixed the issue where ccm and gcm variants of sm4, aes, aria miss redirecting key pointers when dupctx.
  ↳ No PR: [0ca5cf9](https://github.com/openssl/openssl/commit/0ca5cf989101cae6ffeaef3518e99839fbccb9ba)
- Fixed a build issue when SSL tracing support is disabled, and a warning message is output when the -trace option is specified.
  ↳ No PR: [b12c07c](https://github.com/openssl/openssl/commit/b12c07cfba9651ae80b7020ffe8e634f47581389)
- Fixed the issue where the error message falsely reported bad decrypt when the encryption operation failed. Now the error message will correctly display bad encrypt if the encryption fails.
  ↳ No PR: [0e138b7](https://github.com/openssl/openssl/commit/0e138b7b591f160a50aff22f662254d1b39c9cac)
- Fixed the null pointer dereference problem caused by missing jump in engine_table_register.
  ↳ No PR: [be01f60](https://github.com/openssl/openssl/commit/be01f609f98a8930f2c91b813715e515a88f4d54)
- Fix the error handling when there is insufficient memory in CRYPTO_get_ex_new_index to ensure that the meth stack is correctly released and reset when the reserved index fails to avoid subsequent data overwriting.
  ↳ No PR: [d4f22a9](https://github.com/openssl/openssl/commit/d4f22a915ac50570015a23ad794032c4fb9496cb)
- Fixed the problem that the contract function in lhash returns directly when realloc fails, resulting in inconsistent hash table status. Instead, the contract function continues to perform the shrink operation and only updates the internal pointer when realloc succeeds.
  ↳ No PR: [5fbfd64](https://github.com/openssl/openssl/commit/5fbfd641aeebdf4b29a0749e13a79a1e59502878)
- Fixed the issue where the special processing of foreign key does not take effect correctly when signing using legacy key based on application method under no-engine build.
  ↳ No PR: [1acc3e8](https://github.com/openssl/openssl/commit/1acc3e8cc3c69187b55cc557c1bc03278ab38063)
- Fixed string quotation processing in the ossl_property_list_to_string function to ensure that the generated property string can be parsed correctly.
  ↳ No PR: [fb20e66](https://github.com/openssl/openssl/commit/fb20e66c6b2651067f50bab8cf098c71e2caed4b)
- Fixed the order issue of global structure pointer null value checking when initializing random number seeds.
  ↳ No PR: [1541083](https://github.com/openssl/openssl/commit/15410839c668f97b5c03ee1a1bc1a2bf4315715f)
- Fixed use-after-free vulnerability in random number seed generation function.
  ↳ No PR: [6bd0794](https://github.com/openssl/openssl/commit/6bd07949e54f9958eb8a0f9a597ceb3910753ab0)
- Fixed undefined behavior in the BN_gcd function due to shifting of negative values, avoided by explicitly converting the relevant shift operand to an unsigned type.
  ↳ No PR: [0f7a3b0](https://github.com/openssl/openssl/commit/0f7a3b0caa33a87c900536dc1c02fa553d2193cc)
- Fixed a segfault caused by inconsistency in private data structures in the SCTP BIO implementation, embedding common dgram data into the SCTP data structure.
  ↳ No PR: [4bad474](https://github.com/openssl/openssl/commit/4bad474746472f08b0247b5afa81ddc71df98d5f)
- Fixed the problem of using wrong time for condition variable wait timeout in QUIC auxiliary thread, ensuring that the real time is passed in to avoid test hangs; at the same time, the lock operation and thread stop signal methods were adjusted.
  ↳ No PR: [2b8d815](https://github.com/openssl/openssl/commit/2b8d81534479b161dda063477272363fb2caef08)
- Fixed multiple package processing-related bugs in the QUIC channel, including default stream pop-up, tick deadline calculation error, and assertion failure caused by Retry package processing.
  ↳ No PR: [cd138c3](https://github.com/openssl/openssl/commit/cd138c33d82cc889fe6a16d18806fbe939279d25), [098f27f](https://github.com/openssl/openssl/commit/098f27f9ef8be2a418f76896ee3c824e8709fcf7), [56e3032](https://github.com/openssl/openssl/commit/56e303259ed48884c914fe24b354e9cc7b7532c3), [1f8a8c1](https://github.com/openssl/openssl/commit/1f8a8c1de90ebdb4f3c9dbbf3d1329e3f025e946)
- Fixed memory leaks and asynchronous task parameter setting issues in KEM and signature algorithm performance tests in the speed command.
  ↳ No PR: [4e09305](https://github.com/openssl/openssl/commit/4e09305ee092dea14b7d4feb3fac2889b41428f3), [df5f419](https://github.com/openssl/openssl/commit/df5f419b14de9ff47082c42f2a2db6557ceca84f), [cc7e2b2](https://github.com/openssl/openssl/commit/cc7e2b20de02959c328f96e464e5fb8b256a00e0)
- Fixed multiple QUIC related issues, including initial token length check, time conversion truncation, protocol violation handling, URXE order, ACK timeout calculation, packet loss detection and null pointer release.
  ↳ No PR: [461d411](https://github.com/openssl/openssl/commit/461d41174b33e365677d21bf176d6959b15c2468), [c239bc9](https://github.com/openssl/openssl/commit/c239bc9e960b866093dbc666c78c78935233750c), [82b7a0e](https://github.com/openssl/openssl/commit/82b7a0eee90e3280bd0e2dd4a9812b3873a7f462), [86e11b1](https://github.com/openssl/openssl/commit/86e11b1e78ad6937ef32d64ca34013306c9abc28), [4d100bb](https://github.com/openssl/openssl/commit/4d100bb76ad43da75660fa8661d258eaa78fb1c3), [9d67bd5](https://github.com/openssl/openssl/commit/9d67bd5ffd9514b791917804f7b839a5b3fb6da2), [e99c771](https://github.com/openssl/openssl/commit/e99c771985cbaf6ae55912b581d115f5097fe2fd), [457678d](https://github.com/openssl/openssl/commit/457678d68238433b321805eb158a2e15d9331195)
- Fix possible error handling in CMS and PKCS7 due to unchecked EVP_PKEY_get_size returning zero.
  ↳ No PR: [7eab00e](https://github.com/openssl/openssl/commit/7eab00ec470693bd44c9de7ab5c06fe691aa3077)
- Add multiple null pointer checks in ossl_ctrl_internal to prevent null pointer dereference.
  ↳ No PR: [54fa5b3](https://github.com/openssl/openssl/commit/54fa5b3911ead0e1ba7d32bc5732ed2a60b38a99), [6f1d3e1](https://github.com/openssl/openssl/commit/6f1d3e130ed9f79335e5c9bd518f835b71417564), [1c03353](https://github.com/openssl/openssl/commit/1c03353511238251f48152c09b523322c1de54ad), [4230172](https://github.com/openssl/openssl/commit/4230172a0556e1d99dea9469905d18cb64e7c799)
- Fix memory leak when creating tag octet string fails in RSA OAEP encryption.
  ↳ No PR: [f770578](https://github.com/openssl/openssl/commit/f77057815be474528ad0e798e08bc9b36a7d4a4d)
- Fixed an issue where the HTTP client did not return 0 correctly when the response length check failed.
  ↳ No PR: [e63c1a1](https://github.com/openssl/openssl/commit/e63c1a1eab6fac262f0d107e058ff02aa1fef065)
- Fix use of uninitialized variables in TLS extension parsing.
  ↳ No PR: [96e58e3](https://github.com/openssl/openssl/commit/96e58e32ffd7deaf5184d5e502b476554d39216b)
- Fixed the problem that quicserver cannot bind when there are duplicate host name mappings. Now it will try all addresses and start as long as one is successfully bound.
  ↳ No PR: [28932ab](https://github.com/openssl/openssl/commit/28932ab1acc4372fbb4f0050fa7748f1fa079d0d)
- Fixed the problem of quicserver getting stuck in an infinite loop when handshake or receiving request fails, it will now terminate the server and return an error.
  ↳ No PR: [bb8ecea](https://github.com/openssl/openssl/commit/bb8ecea8ed22862184b431f5185c23f0f6cfd9c2)
- Fixed the issue where s_client received an error when receiving data that is exactly equal to BUFSIZZ.
  ↳ No PR: [b4a33ba](https://github.com/openssl/openssl/commit/b4a33ba9aaf8022589dd15261f41d35729277a68)
- Fixed the resource leak problem caused by wrong injection in ossl_quic_new.
  ↳ No PR: [b45d053](https://github.com/openssl/openssl/commit/b45d053fcd124854ea5bb7a24bea6a67d31489b0)
- Fixed an issue where the want_ack flag was not checked correctly when generating ACK frames.
  ↳ No PR: [4febab7](https://github.com/openssl/openssl/commit/4febab7d808c2c746ded9424ceff4163bdae3278)
- Fixed the issue where ossl_quic_sstream_is_totally_acked incorrectly returns 0 when no data is appended to the stream.
  ↳ No PR: [d6b7545](https://github.com/openssl/openssl/commit/d6b7545b60e72a11894a9fc043325256495473cf)
- Fixed a memory leak that could occur when loading built-in compression algorithms.
  ↳ No PR: [21f1c2d](https://github.com/openssl/openssl/commit/21f1c2d9d513010f3585d5215b373ac4bef67c29)
- Fixed usage error of likely macro in ossl_rand_uniform_uint32.
  ↳ No PR: [173dca8](https://github.com/openssl/openssl/commit/173dca8ea144d9fde41bd129a6a7890fbe3157d1)
- Fixed the problem of original length tracking error due to flow control when generating QUIC stream frames.
  ↳ No PR: [61a468b](https://github.com/openssl/openssl/commit/61a468bfaff43893763f555511300f069ae78746)
- Fix possible keyslot leak under wrong conditions.
  ↳ No PR: [478d14c](https://github.com/openssl/openssl/commit/478d14cc3fde378fe722374bc1023c1e0cf00bec)
- Fixed the null pointer dereference problem caused by memory allocation failure in ossl_quic_new.
  ↳ No PR: [e2c6a1d](https://github.com/openssl/openssl/commit/e2c6a1d9a0df7a468f73a7ba62a33a860daa9bb6)
- Fixed usage of implicit length STREAM frames when PATH_RESPONSE frames are present, and refactored padding logic.
  ↳ No PR: [ab3b836](https://github.com/openssl/openssl/commit/ab3b83636e02a12ee678eac8efc1515abe54b687)
- Fixed the problem of padding processing of ACK_ONLY type packets in QUIC TXP.
  ↳ No PR: [68ed191](https://github.com/openssl/openssl/commit/68ed191f6b6541631dd8e298017e83b9b16d5413)
- Fixed possible memory leak of PSK temporary keys in ssl3_free.
  ↳ No PR: [0fdf6e0](https://github.com/openssl/openssl/commit/0fdf6e0a1b16c9f359c63fd94aaa7648dc8ef24c)
- Fixed a possible memory leak under specific error paths in the custom_ext_add function, ensuring that the custom extension's release callback is called on failure.
  ↳ No PR: [9f9dc85](https://github.com/openssl/openssl/commit/9f9dc855adf7e9a65b4a0de7fa1ea19d0a55094f)
- Fixed the problem in the priority queue removal function that the free slot was not properly reclaimed when removing the last element in the heap.
  ↳ No PR: [f5f4bc3](https://github.com/openssl/openssl/commit/f5f4bc30f303a229d29dea148bc2d289f6fe04e3)
- Fixed an issue in QUIC transport where packets were not marked as full when the stream had taken an implicit length.
  ↳ No PR: [fc0dce3](https://github.com/openssl/openssl/commit/fc0dce399aed2c8d2aea8ea675aa3d50f51b6ef4)
- Fixed upper limit check on variable output size in BLAKE2 algorithm so that it is correctly limited to the default output size of the algorithm.
  ↳ No PR: [aa95fb1](https://github.com/openssl/openssl/commit/aa95fb14003121d0b6c86e564c31cb95424d4bed)
- Fixed the problem in dtls1_hm_fragment_new that the msg_header field was not initialized when allocating hm_fragment, and instead used zero-initialized allocation to avoid referencing undefined data when freeing.
  ↳ No PR: [1ea038b](https://github.com/openssl/openssl/commit/1ea038bfa2726ad1bfbc220c8955c0fead9393d5)
- Fixed an issue where the DTLS record layer may incorrectly release the current record layer under certain error conditions, and moved the release logic to dtls1_clear_sent_buffer.
  ↳ No PR: [2bb8394](https://github.com/openssl/openssl/commit/2bb83945bb99c98b1a67c5ba6307ad8b0dde5370)
- Fixed the label length boundary check when calculating the plaintext payload length in the QUIC record layer, correctly returning no free space when the available space is equal to the label length.
  ↳ No PR: [2aba954](https://github.com/openssl/openssl/commit/2aba9548c4a0a3f8359ab5476df3ad58f1cbcf06)
- Fixed QUIC connection level credit consumption tracking issue, ensuring that streaming data stops being added after connection credits are exhausted.
  ↳ No PR: [915ec62](https://github.com/openssl/openssl/commit/915ec623eca7b413db6f54ec4aa64585e81ac4df)
- Fixed EVP_PKEY_decrypt output length handling to use the actual decryption output length when generating master keys.
  ↳ No PR: [fdef957](https://github.com/openssl/openssl/commit/fdef95716dbcc6127d05f8cfc90f389a84acaf9b)
- Changed the output of successful self-signed verification of the certificate request in the openssl req -verify command from standard error to standard output.
  ↳ No PR: [c154f53](https://github.com/openssl/openssl/commit/c154f537c34c80e42915f32e97c6ba90d9fd4037)
- Removed the dependence on the NDEBUG compilation condition in the test, making the test always available.
  ↳ No PR: [574246a](https://github.com/openssl/openssl/commit/574246ae02a206b49957b63b0d4f53992e855e13)
- Fixed return value bug in documentation, and corrected return value checking in tests.
  ↳ No PR: [8b7d778](https://github.com/openssl/openssl/commit/8b7d7789dc4ea0de11331cb4045bcb03ab0864fc)
- Fixed an issue where test-rand incorrectly returns success when there is insufficient data, and ignores failures when specifying a parent.
  ↳ No PR: [d4dfd98](https://github.com/openssl/openssl/commit/d4dfd983e32b32b633aaa9edec422cc30419c6f7)
- Fixed the problem of the null pointer checking order being reversed in test/ssl_old_test.c.
  ↳ No PR: [8c590a2](https://github.com/openssl/openssl/commit/8c590a219fe30b97cfde2efdd8ea94c03a90a8c6)
- Fixed an issue with incomplete BIO_gets return value checking.
  ↳ No PR: [7264068](https://github.com/openssl/openssl/commit/7264068a15e7c4955efa25753430595a45caa16f)
- Fixed EVP_PKEY_decrypt return value check, and corrected related test cases.
  ↳ No PR: [0650ac4](https://github.com/openssl/openssl/commit/0650ac437b529274aca094c516a5a0127bbaf48c)
- Fixed test function and return value checking of EVP_DigestVerifyFinal.
  ↳ No PR: [e2e5e72](https://github.com/openssl/openssl/commit/e2e5e72d5aec4d8d633cc5e9930f762da7973ab6)
- Fixed return value checking of TXT_DB_write function.
  ↳ No PR: [aba9943](https://github.com/openssl/openssl/commit/aba9943fef8dcc8416ac9a219c97c616c1fd6344)
- Fixed return value checking of BIO_set_prefix.
  ↳ No PR: [ac6568e](https://github.com/openssl/openssl/commit/ac6568ecc6050bc526adc6a7245835fd95d8dfed)
- Added checks for return values of memory allocation functions such as OPENSSL_strdup.
  ↳ No PR: [5203a8d](https://github.com/openssl/openssl/commit/5203a8dfdc209f05c7dbd9c1e5208743fcaa6752)
- Fixed the error handling problem reported by Coverity and added null pointer check.
  ↳ No PR: [f80cdee](https://github.com/openssl/openssl/commit/f80cdee7c1eee93d13c7dcbeda32dfca3e1e4059)
- In evp_test, skip MAC test when digest or cryptographic algorithms are disabled.
  ↳ No PR: [c8a016c](https://github.com/openssl/openssl/commit/c8a016cac44d5402df3106f46c9725aa1b480e40)
- Fixed test cases for check-format.pl script, corrected empty line detection and false positives in for loop format.
  ↳ No PR: [23757b6](https://github.com/openssl/openssl/commit/23757b61d49ac3e46440dc34e56b83201106e440), [4e9fa07](https://github.com/openssl/openssl/commit/4e9fa07121abf3ebaaf7e0367bd9be3a8b273ebf)
- Fixed coding style and other minor issues in test files.
  ↳ No PR: [45479dc](https://github.com/openssl/openssl/commit/45479dcee1672661e4f5b6d8b6c9a50453581e65)
- Added documentation and tests for EVP_PBE_alg_add, and fixed related issues.
  ↳ No PR: [181167b](https://github.com/openssl/openssl/commit/181167b6d0e5cd896847f7538adf28878b81b0b2)
- Fixed default padding regression for 3.0.0 FIPS provider, and updated test data.
  ↳ No PR: [9684335](https://github.com/openssl/openssl/commit/9684335839fcdeac06d21b06628c4c37117b5478)
- Fixed random failures and compiler warnings in BIO_dgram_pair tests.
  ↳ No PR: [8e90a12](https://github.com/openssl/openssl/commit/8e90a12ad82dec6d8b683eaa2e4feafa9796d377), [19b6b5f](https://github.com/openssl/openssl/commit/19b6b5f4791e3531cd6d3aabc8706d590ade14b7)
- Added test for TLSv1.3 client-only scenario, verifying its correct fallback to P-256 curve.
  ↳ No PR: [7b141d4](https://github.com/openssl/openssl/commit/7b141d4934ab1254d65fd1859ca1c6eff1113b50)
- Fixed compilation errors caused by missing DH header files in tests.
  ↳ No PR: [bbaa24b](https://github.com/openssl/openssl/commit/bbaa24b7c5ca4d712ad539d4c5ed16af0dd908f4)
- Fixed dead code warning detected by Coverity in tests.
  ↳ No PR: [dc45bfb](https://github.com/openssl/openssl/commit/dc45bfb4b452ba5a876ebf48791217b69d092ff9)
- Fixed Clang 15 compilation warning caused by unused variables in test driver.
  ↳ No PR: [6a94c58](https://github.com/openssl/openssl/commit/6a94c5849ea7d1f08d4fcaa9a6fc0a947e19da66)
- Fixed build failure in QUIC tests due to wrong parameter order.
  ↳ No PR: [1e7cc86](https://github.com/openssl/openssl/commit/1e7cc86b7516bb035b91c23a38f2d9e6323d33c9)
- Fixed missing wait_until_sock_readable function in tests when POSIX IO or sockets are disabled.
  ↳ No PR: [a5df3fc](https://github.com/openssl/openssl/commit/a5df3fc093c8ef17152e6c645be6fa9a77c56679)
- Fixed the algorithm enablement check condition in QUIC recording tests to avoid incorrectly running tests that require ChaCha20-Poly1305 when only Poly1305 is disabled.
  ↳ No PR: [4cc16b0](https://github.com/openssl/openssl/commit/4cc16b0557875829041547dc63c7600b1ca57a14)
- Added check for SSL_get0_alpn_selected return value in tests.
  ↳ No PR: [8b940b6](https://github.com/openssl/openssl/commit/8b940b69457f0dd43496c16afaa01f510f0d8a19)
- Fixed the processing logic of connection failure or retry in QUIC multi-stream test.
  ↳ No PR: [a1d2a9d](https://github.com/openssl/openssl/commit/a1d2a9d12d269ba551b1d2d3bc825aedad8984c9)
- Fixed buffer size calculation in bio_dgram_test to take header overhead into account to avoid insufficient buffer on certain platforms.
  ↳ No PR: [58165d8](https://github.com/openssl/openssl/commit/58165d8da493d4271b8a026ef4056ecaeefd3916)
- Increased wait time in tests on slow machines to ensure threads have enough time to process QUIC ticks.
  ↳ No PR: [556f338](https://github.com/openssl/openssl/commit/556f33837af8691f9b03c716e47d6d06186a6752)
- Fixed a regression in evp_test caused by ignoring old FIPS provider replication failure.
  ↳ No PR: [bbb6d62](https://github.com/openssl/openssl/commit/bbb6d620f6014274cb00a8186225447a2a114543)
- Added client tracing functionality to the test library, added QTEST_FLAG_CLIENT_TRACE flag to enable debug trace output.
  ↳ No PR: [8d8c0a9](https://github.com/openssl/openssl/commit/8d8c0a901e5d65d68070fbe812d7e8c1449381e1)
- Fixed GCC compilation warning in apps/cmp.c to avoid negative index dereference by rewriting the loop.
  ↳ No PR: [767db67](https://github.com/openssl/openssl/commit/767db672c429aeb98a68b0e310dea15f1b48eb84)
- Renamed the MIN macro to ossl_min to avoid naming conflicts with OpenSSL 3.0.
  ↳ No PR: [f4f77c2](https://github.com/openssl/openssl/commit/f4f77c2d9756cee12875397276799a93f057d412)
- Fixed the risk of gctx being passed to rsa_gen_set_params in the gen_init function when it might be NULL.
  ↳ No PR: [22778ab](https://github.com/openssl/openssl/commit/22778abad905536fa6c93cdc6fffc8c736dfee79)
- Removed the empty_fragment_done field and related logic, because the prefix fragment is added every time a record is written, and this flag is no longer needed.
  ↳ No PR: [91141aa](https://github.com/openssl/openssl/commit/91141aa1b0ff9d92323e2545bb9f6f0d1e2a8844)
- Fixed a dead code issue caused by incorrectly checking variables in the DTLSv1_listen function.
  ↳ No PR: [7ccccb2](https://github.com/openssl/openssl/commit/7ccccb26d6de39eced5b16ffce6040c9547bfe74)
- Removed the explicit check of the engine in the opt_legacy_okay function, simplifying the internal logic.
  ↳ No PR: [2fea568](https://github.com/openssl/openssl/commit/2fea56832780248af2aba2e4433ece2d18428515)
- Added context duplication (dupctx) support for multiple algorithm implementations, including AES WRAP, aes_cbc_hmac_sha1, aes_cbc_hmac_sha256 and rc4_hmac_md5.
  ↳ No PR: [2c021e7](https://github.com/openssl/openssl/commit/2c021e7d11f03ede2330398c4fd8e8c7bd8768ee), [123c858](https://github.com/openssl/openssl/commit/123c85864fa7fe97d8ae3a09989d410501d957a5)
- Optimize the internal lock mechanism, change write locks to read locks or avoid unnecessary lock operations, reduce lock competition and improve concurrency performance.
  ↳ No PR: [6d15357](https://github.com/openssl/openssl/commit/6d15357aeb893c6e8b4c7a8188c18f4db54c0612), [b8fa5be](https://github.com/openssl/openssl/commit/b8fa5be5506e43b405c9a3ecc3d65c77044777be), [50001e0](https://github.com/openssl/openssl/commit/50001e0e15d4a96213c2eea7c56f80087afa89fd), [80935bf](https://github.com/openssl/openssl/commit/80935bf5ad309bf6c03591acf1d48fe1db57b78f)
- Fixed multiple code quality issues reported by Coverity, including constant expression results and loop variable type issues.
  ↳ No PR: [7cc5738](https://github.com/openssl/openssl/commit/7cc5738a561933e38ad0e724f4df7b503c3c8e73), [0bcae98](https://github.com/openssl/openssl/commit/0bcae9893b99666158dd8b35fb674e6188b0b5c3)
- Fixed multiple resource leaks, including hostname memory leak in init_client() and missing resource release in crl_set_issuers function.
  ↳ No PR: [2342d9b](https://github.com/openssl/openssl/commit/2342d9b650ed3dafd65b7edadbe805e04a4966ba), [cb0c36d](https://github.com/openssl/openssl/commit/cb0c36d124991e35a9e778056ec8fce23a14dad5)
- Renamed intrinsic functions to avoid symbol conflicts with Intel ISA-L library.
  ↳ No PR: [15e041b](https://github.com/openssl/openssl/commit/15e041b751c96ecf668a701d09a373d517610eae)
- Add a null pointer check for the evp_ctx parameter in the shake_ctrl function to prevent null pointer dereference.
  ↳ No PR: [410c80d](https://github.com/openssl/openssl/commit/410c80dc7bf2085167553ab9fa517189eed2b3a6)
- Fix the conflict between DH check flag and FFC check flag, adjust the value of internal FFC flag bit.
  ↳ No PR: [6061fd5](https://github.com/openssl/openssl/commit/6061fd58a30f181c956e5ba5a06932f99d2c9a18)
- Remove outdated comments about ERR_clear_error() in cmp_http.c.
  ↳ No PR: [3179995](https://github.com/openssl/openssl/commit/3179995f114fca4cb9958116e353ad6b686b7ecd)
- Make the error cause string array in err.c consistent with err.h, and fix the printing problem of common error cause strings.
  ↳ No PR: [3ae5528](https://github.com/openssl/openssl/commit/3ae55288387a3ff9cf9b1cba2da22bd1aafbc66e)
- Fix typos in ossl_kdf_data_up_ref and ossl_mac_key_up_ref functions, and remove redundant parameters in CRYPTO_UP_REF call.
  ↳ No PR: [e304aa8](https://github.com/openssl/openssl/commit/e304aa87b35fac5ea97c405dd3c21549faa45e78)
- Add missing CMP trace category entries in trace.c.
  ↳ No PR: [e06c0a2](https://github.com/openssl/openssl/commit/e06c0a2870c55aa4e66108ca071e7da7fd00b922)
- Add preliminary verification of input numbers to the openssl prime command, checking whether the parameters are valid numbers before parsing.
  ↳ No PR: [3b74fdc](https://github.com/openssl/openssl/commit/3b74fdcf1d5eb311e44b7eaa293df6caf54ae70b)
- Replace strncpy with memcpy in the put_str function to eliminate compilation warnings for new versions of GCC.
  ↳ No PR: [5ad3e76](https://github.com/openssl/openssl/commit/5ad3e76c23576b2e216463bfe43d005a3e09defc)
- Improved multiple error messages and logging to help diagnose problems.
  ↳ No PR: [2d23ba1](https://github.com/openssl/openssl/commit/2d23ba14630551ee347acafcab81fa1a290c6504), [ec6cbda](https://github.com/openssl/openssl/commit/ec6cbda0f2e435ae0efaec308dc5569c75bb759b), [4085ba8](https://github.com/openssl/openssl/commit/4085ba874ee0f76eda412a8820a379f27664d763), [f52aec3](https://github.com/openssl/openssl/commit/f52aec35260627c37f114352843dc0bc22311a17)
- Fixed multiple minor issues in QUIC code, including header file inclusion, comment corrections and adding assertions.
  ↳ No PR: [394f6f2](https://github.com/openssl/openssl/commit/394f6f246af23876f3d7a0332eb194aaa5127643), [571aff4](https://github.com/openssl/openssl/commit/571aff4bfaf0407cadba2e304b60c0364684cee5), [3a61a96](https://github.com/openssl/openssl/commit/3a61a96c1e43694199f5ec0887d0ad21a4650e3f)
- Fixed the for loop space reporting defect in check-format.pl, and updated the test cases.
  ↳ No PR: [0a8a9f8](https://github.com/openssl/openssl/commit/0a8a9f8f634306bbfaed8f924d71536f1ff50677)
- Fixed typo in PROV_RC5_CTX structure name.
  ↳ No PR: [53ef02b](https://github.com/openssl/openssl/commit/53ef02baf80130a81d019e85c528fdc13af9db33)
- Fix sporadic CI test failures due to unaligned memory access.
  ↳ No PR: [8511520](https://github.com/openssl/openssl/commit/8511520842b744d1794ea794c032ce5f78cd874b)
- Roll back a commit that fixed CI failure for unaligned access.
  ↳ No PR: [f83490f](https://github.com/openssl/openssl/commit/f83490fb9ce4dd1c09d4f94526fbcad14bd2fd85)
- Removed printf statements for debugging in evp_test.c.
  ↳ No PR: [12c20c5](https://github.com/openssl/openssl/commit/12c20c5486b6440a9b667c93f130a8fdea029b81)
- Fixed the return type of compute_pqueue_growth() function from int to size_t.
  ↳ No PR: [6a94535](https://github.com/openssl/openssl/commit/6a9453572533e4a22e6f60fe8f6b7ef0823d9c1f)
- Fix Coverity warning: add null pointer check and fix operator precedence.
  ↳ No PR: [1dbfd7f](https://github.com/openssl/openssl/commit/1dbfd7fe24bcd50117bc57942b2046e483a3c5a5)
- Remove remaining ossl_crypto_mem_barrier function declaration and implementation in Win32 and other architectures.
  ↳ No PR: [41c3c71](https://github.com/openssl/openssl/commit/41c3c71382f31a5a913bd09a74295d101d837055)
- Change the return value of the main function in the demo code to the EXIT_SUCCESS/EXIT_FAILURE macro, and unify the variable naming.
  ↳ No PR: [09ff84b](https://github.com/openssl/openssl/commit/09ff84bd2752cac649f57cfbf95b49dbce1c69ee)
- Fixed the compilation problem caused by #warning directive in build_wincrypt_test.c under MSVC.
  ↳ No PR: [b5a635d](https://github.com/openssl/openssl/commit/b5a635dc2113e1bc807ea358a670146c813df989)
- To resolve function name conflicts under DJGPP, rename the lock/unlock functions in test output.
  ↳ No PR: [6dea91f](https://github.com/openssl/openssl/commit/6dea91f56dcbcb0979dd36790664808ad960faf9)
- Fixed header file inclusion, replacing incorrect <sys/poll.h> with correct <poll.h>.
  ↳ No PR: [c4ce0e3](https://github.com/openssl/openssl/commit/c4ce0e3303d586bc4ec41f380c94ccb4fb84e2d5)
- Check the return value of CRYPTO_atomic_add and return early on failure.
  ↳ No PR: [7efc073](https://github.com/openssl/openssl/commit/7efc073dd7ddaed732c35e84efc865463db7ffbc)
- Fixed typos found by codespell, and corrected some function calls and buffer boundaries.
  ↳ No PR: [a024ab9](https://github.com/openssl/openssl/commit/a024ab984e540bff65d25407496c34b3567b55a7)
- Added openssl/err.h header file reference in refcount.h.
  ↳ No PR: [bdcaa47](https://github.com/openssl/openssl/commit/bdcaa47ddb86bfef8bbdebc02a7b72df49920b6d)
- Adjusted the RXFC default parameters of the QUIC channel and fixed a comment.
  ↳ No PR: [89b0948](https://github.com/openssl/openssl/commit/89b0948e534c1522e7d00b60cf55f5ada0bb39da)
- Fixed an issue where error information was not added correctly when construction failed during decoding.
  ↳ No PR: [564e5b7](https://github.com/openssl/openssl/commit/564e5b754a4680dfad38585dd73bcf025567b448)
- Improved the output and tracing functions of quicserver, added the -trace option.
  ↳ No PR: [4dec928](https://github.com/openssl/openssl/commit/4dec9285d3c833c26cfc589f31d896e93a36f498)
- Removed unused read_iv member in ossl_record_layer_st.
  ↳ No PR: [20a54aa](https://github.com/openssl/openssl/commit/20a54aa21fc34ded577daf0bc91808b68a3b3c95)
- Removed redundant dot multiplication operations in ossl_ec_key_public_check.
  ↳ No PR: [3961991](https://github.com/openssl/openssl/commit/3961991593f788b3efb2a27563d358c7c58f854c)
- Fixed minor bugs in type conversion and parameter passing, and corrected documentation terminology.
  ↳ No PR: [8d7f034](https://github.com/openssl/openssl/commit/8d7f034622c0235d06f4d6526f71dcab2f71b0c6)
- Fixed a warning about uninitialized data in the BLAKE2b parameter initialization function.
  ↳ No PR: [31fc8a8](https://github.com/openssl/openssl/commit/31fc8a83bc9aa435ae40c3eff713ced441eaa011)
- Added algorithm comments for random uniform distribution function, and corrected probability description.
  ↳ No PR: [7a78528](https://github.com/openssl/openssl/commit/7a78528bc540db41ca6834810766a62b640a09c7)
- Fixed verbosity option handling for CMP client diagnostics.
  ↳ No PR: [92df521](https://github.com/openssl/openssl/commit/92df52119eb33ea980e8f02f9cdfe194ad6c04e1)
- Fixed position of overlong section name warning so that it is emitted correctly before truncation.
  ↳ No PR: [39a8d4e](https://github.com/openssl/openssl/commit/39a8d4e13219580c8c89a234d6db5d261408cadb)
- Fixed the behavior of ssl_free when the BIO_NOCLOSE flag is set.
  ↳ No PR: [dce910a](https://github.com/openssl/openssl/commit/dce910af3bb135bd6d7c5a4cc512043b3ad4acc1)
- Added detection of duplicate names and returning errors in attribute parsing.
  ↳ No PR: [8e61832](https://github.com/openssl/openssl/commit/8e61832ed7f59c15da003aa86aeaa4e5f44df711)
- Fixed parameter length flag and duplicate release issues for RSA methods in dasync engine.
  ↳ No PR: [59cd0bc](https://github.com/openssl/openssl/commit/59cd0bc1364b5ea817af7f6d36df89c93610cdb5)
- Fixed a possible null pointer dereference when printing the hostname after a successful connection.
  ↳ No PR: [e8655e1](https://github.com/openssl/openssl/commit/e8655e16cab9cd14ebfe9f2214c2f2aa39c67a26)
- Fixed memory leak in afalg engine and added regression tests.
  ↳ No PR: [6f6a5e0](https://github.com/openssl/openssl/commit/6f6a5e0c7c41b6b3639e51f435cd98bb3ae061bc)
- Fixed order of self-signed certificate checks in x509 tools.
  ↳ No PR: [18e0c54](https://github.com/openssl/openssl/commit/18e0c544b01ed61e7eab61a6cd187c2f4eaa78bd)
- Fixed unsafe issue with BIO_get_md_ctx return value checking.
  ↳ No PR: [59a3e7b](https://github.com/openssl/openssl/commit/59a3e7b29574ff45f62e825f6e9923f45060f142)
- Fixed error handling in X509 name canonicalization and certificate addition.
  ↳ No PR: [0923528](https://github.com/openssl/openssl/commit/09235289c377ff998964bb6b074bb2a3ad768fd2), [64c428c](https://github.com/openssl/openssl/commit/64c428c35053a101a452c42d5d0a9a8342493606)
- Fixed race conditions in DSO methods and initialization thread.
  ↳ No PR: [e6a10b0](https://github.com/openssl/openssl/commit/e6a10b074e90f1ce3d8e9ae0ca740a835ff29bb9), [3b9de0c](https://github.com/openssl/openssl/commit/3b9de0c9aa791bd9e6f0534ec091accbdf15292f)
- Fixed MAC output buffer size calculation error in SSKDF.
  ↳ No PR: [7be8ba5](https://github.com/openssl/openssl/commit/7be8ba546267787c1b0df8a4fddaf9cb29944cbb)
- Fixed an issue where warnings were incorrectly printed when generating new certificate requests.
  ↳ No PR: [5860848](https://github.com/openssl/openssl/commit/58608487a44b3991ecc6d431d6273b2ca8c980a6)
- Fixed memory leak of bindhost and bindport variables in s_client.
  ↳ No PR: [0ce0c45](https://github.com/openssl/openssl/commit/0ce0c455862ed29bd7f2acdbddbe8d0b1783c1c9)
- Fixed the problem of PSK server callback connection failure under DTLS.
  ↳ No PR: [8b09a9c](https://github.com/openssl/openssl/commit/8b09a9c76d873f62c2507fa9628a9c96c1d66d5c)
- Fixed the ENGINE reference leak and double release issues in the provider tool.
  ↳ No PR: [86c15ba](https://github.com/openssl/openssl/commit/86c15ba87488f88e6191f098ff154f79ce91847b)
- Fixed undefined behavior caused by pointer subtraction in bss_mem.c.
  ↳ No PR: [a98b265](https://github.com/openssl/openssl/commit/a98b26588b683eb024ab81f3bb3549c43acd5188)
- Fixed security renegotiation prompts in s_client and s_server.
  ↳ No PR: [af5e63e](https://github.com/openssl/openssl/commit/af5e63e1e3300f784f302a5d3309bf673cc08894)
- Fixed an issue where the key length could be negative in RC5 key initialization.
  ↳ No PR: [fe41253](https://github.com/openssl/openssl/commit/fe4125382301201e42a3251544cda429bba0c9d7)
- Fixed the checking logic of the return value of the ossl_do_blob_header function.
  ↳ No PR: [546b9f6](https://github.com/openssl/openssl/commit/546b9f6b5cf6d0fde60aa37084eec1bb7d0fbc72)
- Fixed dead code issue reported by Coverity.
  ↳ No PR: [f0fc3c1](https://github.com/openssl/openssl/commit/f0fc3c10d0617821a476b34aba1ee77d47a2a64a)
- Fixed the problem of X509_STORE_new memory not being released in the sample program.
  ↳ No PR: [c81eed8](https://github.com/openssl/openssl/commit/c81eed84e4e9025e933778f5e8326b1e4435e094)
- Fixed possible use-after-free issue when copying HMAC and MD.
  ↳ No PR: [ad2fcee](https://github.com/openssl/openssl/commit/ad2fcee1632d3f21a37e8e108d4c0dcf9099686d)
- Fixed the null pointer dereference problem when ctx is NULL in the file_open_dir function.
  ↳ No PR: [68b78dd](https://github.com/openssl/openssl/commit/68b78dd7e40f57064b0f24728d8b544fe583599c)
- Fixed use-after-free issue in ossl_provider_add_to_store.
  ↳ No PR: [33df7cb](https://github.com/openssl/openssl/commit/33df7cbe5e38feb0cf962386bcac061c3743ecf2)
- Fixed a possible null pointer dereference issue when looking up non-legacy passwords or message digests.
  ↳ No PR: [7a85dd4](https://github.com/openssl/openssl/commit/7a85dd46e0b2f67b341c777509f0126e3252938d)
- Fixed a buffer problem in the do_ui_passphrase function caused by the UI method automatically adding a NUL terminator.
  ↳ No PR: [ef65bbb](https://github.com/openssl/openssl/commit/ef65bbb96352650bf9ce4ff46c60c71d9f138d08)
- Fixed openssl speed command failing with MD5 in FIPS mode, now skipping unavailable digest algorithms.
  ↳ No PR: [c63e863](https://github.com/openssl/openssl/commit/c63e8637fd79c826b3c438cf99cf7f1b293e8318)
- Fixed incorrect usage of NULL check in random number EGD transport layer.
  ↳ No PR: [ff7cdc1](https://github.com/openssl/openssl/commit/ff7cdc15875293a330831a80d83edbafd25a9d36)
- Fixed NUL termination handling of PKCS12 passphrases, ensuring they are passed correctly to PKCS12_parse.
  ↳ No PR: [1dfef92](https://github.com/openssl/openssl/commit/1dfef929e43ebfa3a7f1108317f75747f92effb6)
- Fixed the problem that the lock was not released correctly in the close_console function to ensure that it can also be unlocked under the wrong path.
  ↳ No PR: [5bea0e2](https://github.com/openssl/openssl/commit/5bea0e2ee9bda4d9be6e88c79f2c1b411bb65351)
- Fixed an issue where the X509_STORE_CTX_purpose_inherit function might return incorrectly when the default purpose is 0.
  ↳ No PR: [4aa8285](https://github.com/openssl/openssl/commit/4aa82850267defd772ddf74a88d515ef4fb566b8)
- Fixed a double-free issue that could occur when TLS was not used.
  ↳ No PR: [97b8c85](https://github.com/openssl/openssl/commit/97b8c859c64bc60fcf5bb27ed51489c81fde41b3)
- Added error logging for failure cases in parameter build functions.
  ↳ No PR: [3831351](https://github.com/openssl/openssl/commit/3831351da50b7ce07edba88056394a7a33c5e5d5), [3ee3a2b](https://github.com/openssl/openssl/commit/3ee3a2bd1e5763b0df5c0a2cba3b06edc26f5276)
- Fixed the list of available parameters for DH key exchange, removing irrelevant EC parameters and adding missing CEK algorithm parameters.
  ↳ No PR: [c1167f0](https://github.com/openssl/openssl/commit/c1167f09d840b109ef1c1c1485e3de64be2fc625)
- Added check for OPENSSL_strdup return value in s_server and OCSP applications.
  ↳ No PR: [0c59055](https://github.com/openssl/openssl/commit/0c5905581e9d1d79d62cac56a0e3c2ed487afecf), [8f084b4](https://github.com/openssl/openssl/commit/8f084b43803d53e15d83ed130210f026f84679ff)
- Fixed garbage echo and memory free errors in the sslecho example caused by getline's use of static buffers.
  ↳ No PR: [3c0e8bc](https://github.com/openssl/openssl/commit/3c0e8bc4a797d29b2152aebc6e687ddfa941160b)
- In the dhparam command, a warning message is now printed when an input file parameter is specified but is ignored.
  ↳ No PR: [6d95229](https://github.com/openssl/openssl/commit/6d952291762246f6533e19ca413277390db4aae2)
- Fixed return value checking or error handling logic in DTLS, PKCS7, address inclusion and SRP.
  ↳ No PR: [639e576](https://github.com/openssl/openssl/commit/639e576023aa2492ca87e1e6503c40d2e8c9a24e)
- Fixed the return value checking logic in the EVP_PKEY_CTX_set0_rsa_oaep_label function.
  ↳ No PR: [00d5193](https://github.com/openssl/openssl/commit/00d5193b688019a85d1bd0196f2837a4476394bb)
- Fixed return value check in X509_REVOKED_add1_ext_i2d function.
  ↳ No PR: [c540a82](https://github.com/openssl/openssl/commit/c540a82767954a616934ba6caa6ddc736502c574)
- Fixed the return value check of BIO_get_cipher_status in the cms_copy_content function and corrected the error code.
  ↳ No PR: [48b571f](https://github.com/openssl/openssl/commit/48b571fe771f283d547ca2a5999ce5dd9a5509d0)
- Fixed copy-paste error when setting propq in CTLOG_new_ex function.
  ↳ No PR: [163bf68](https://github.com/openssl/openssl/commit/163bf682fd93971d07e66e3da339c229b86dc849)
- Checked the return value of ossl_parse_property(), and fixed resource leaks and null pointer checks in decoder and encoder initialization.
  ↳ No PR: [4fa5ed5](https://github.com/openssl/openssl/commit/4fa5ed5ce5c345eaeaec8b86eda265add467f941)
- Fixed an unexpected NULL assignment problem caused by misuse of the assignment operator in the ternary operator.
  ↳ No PR: [1a01e5c](https://github.com/openssl/openssl/commit/1a01e5c29dfaf09af3960b4c8e6ec0f8171eda80)
- Fixed memory leak in evp_pkey_copy_downgraded(), ensuring automatically allocated EVP_PKEY is released on failure.
  ↳ No PR: [ae4d957](https://github.com/openssl/openssl/commit/ae4d9573ac783dcf26279f461d42d0e261e978f7)
- Fixed a bug in ec_export where OSSL_PARAM_BLD_to_param still returned success when it failed.
  ↳ No PR: [7d6aad8](https://github.com/openssl/openssl/commit/7d6aad832b4cebb181c53ab80a3f61dc8549be08)
- Added null pointer check for integer conversion function return values in SXNET extension handling.
  ↳ No PR: [9ef1f84](https://github.com/openssl/openssl/commit/9ef1f848a646565d4dd86e56542cf921d4921ad9)
- Avoided including unnecessary header files in FIPS modules to fix compilation issues.
  ↳ No PR: [b8fd15a](https://github.com/openssl/openssl/commit/b8fd15a8dc50020360862290ace7f34b6ef0e92d)
- Added check for OPENSSL_strdup return value in HTTP client redirection handling.
  ↳ No PR: [816d6e5](https://github.com/openssl/openssl/commit/816d6e578ccc4d8ae41de77e3069762d03079d18)
- Fixed a memory leak caused by memory allocation failure in the cmp_calc_protection() function.
  ↳ No PR: [74c929d](https://github.com/openssl/openssl/commit/74c929d00dce3a4755164859c600aabb3838a87b)
- Reset the output length variable in the key derivation loop to prevent calculation errors caused by too small length values.
  ↳ No PR: [ab8d56d](https://github.com/openssl/openssl/commit/ab8d56d05b773e499c86be874fd3f11f5950213c)
- Added check for OBJ_new_nid() return value in OBJ_create function.
  ↳ No PR: [a0ff8e4](https://github.com/openssl/openssl/commit/a0ff8e413e94ba46720a4bf3a5032c50531c526c)
- Fixed the issue of unchecked return value of gettimeofday and added error handling.
  ↳ No PR: [358103b](https://github.com/openssl/openssl/commit/358103b4a651ab3f392f088d86cd30469dccce2e)
- Fixed missing inclusion issue in internal header files, added reference to internal/time.h to ensure OSSL_TIME is correctly defined.
  ↳ No PR: [eb51673](https://github.com/openssl/openssl/commit/eb51673e522855400a11de4569a3612c98c7b685)
- Added missing BN_CTX_end call at the end of SM2 signature verification function.
  ↳ No PR: [050dddb](https://github.com/openssl/openssl/commit/050dddb06162a8016c004317273f8f01b72ac20a)
- Fixed compilation issue in crypto/dso/dso_vms.c due to preprocessor condition error.
  ↳ No PR: [c007f46](https://github.com/openssl/openssl/commit/c007f466aaebd8ef07111c8560e039d8bcb5fa7b)
- CMAC's set_ctx_params function now checks whether the cipher mode is CBC, and returns failure if not.
  ↳ No PR: [94976a1](https://github.com/openssl/openssl/commit/94976a1e8d9b127999df14c2e0c38e918c2badda)
- Fixed compilation warnings caused by unused variables in multiple functions.
  ↳ No PR: [71bc497](https://github.com/openssl/openssl/commit/71bc497dc321adeb08e7541556dea019c81c9a87), [f9e8e2c](https://github.com/openssl/openssl/commit/f9e8e2c0ab73409862bb78a9285c1b72e0511750), [c713186](https://github.com/openssl/openssl/commit/c71318668571b3680fe10035a1a350ff46e459af)
- Fixed incorrect library identification used in error reporting in OPENSSL_sk_set function.
  ↳ No PR: [3a09dfb](https://github.com/openssl/openssl/commit/3a09dfb4f9aace93d2c20d6d1b4968cc583884d6)
- Fixed potential undefined behavior due to strict aliasing violation in rsaz_exp_x2.c.
  ↳ No PR: [9506a2e](https://github.com/openssl/openssl/commit/9506a2e274c643b94a2c265019ea9288f99a521a)
- Added null pointer checks in several functions to prevent potential crashes.
  ↳ No PR: [c9a542e](https://github.com/openssl/openssl/commit/c9a542e41837ea65671dcd75c448d7113d34a4fd), [93e1271](https://github.com/openssl/openssl/commit/93e1271eedfe3af0a1c1b14d26899d2c8bde98e9)
- Fixed an issue with uninitialized variables in QUIC TXP.
  ↳ No PR: [24c1be5](https://github.com/openssl/openssl/commit/24c1be5cff94d6d92d78a11c6584deb7047b4ab6)
- Fixed the return value checking logic in multiple functions to ensure that error status is reported correctly.
  ↳ No PR: [4c3fadf](https://github.com/openssl/openssl/commit/4c3fadfe57b94f71fa83786726046b8833997c7c), [b794476](https://github.com/openssl/openssl/commit/b794476df71441a6d30740ab9fadcc0f6d18d3d6), [25d02f3](https://github.com/openssl/openssl/commit/25d02f333b9a5531fa88db294f69a8347f275858), [9e5bd89](https://github.com/openssl/openssl/commit/9e5bd8923bff3e4f0cbba05c7dadfe289c66eb6f), [0f48050](https://github.com/openssl/openssl/commit/0f48050b5a8881870b8e25382f817b3a3dc14f16), [bf3f8f2](https://github.com/openssl/openssl/commit/bf3f8f2c0ea7bdfb007079aade8e01a06e79874f)
- Fixed an issue where loading keys failed due to buffering issues when getting passwords from stdin.
  ↳ No PR: [efec0f4](https://github.com/openssl/openssl/commit/efec0f4611ee854f2b0b3da0c135e839bf8e7d04)
- Fixed the problem that the issuer and serial parameters in the storeutl tool cannot be used at the same time.
  ↳ No PR: [abdf351](https://github.com/openssl/openssl/commit/abdf35158e4398deedcf160c28bd07c7080edf47)
- Fixed an issue where more FIN blocks could be incorrectly filled when processing FIN stream blocks in QUIC transports.
  ↳ No PR: [cf06f34](https://github.com/openssl/openssl/commit/cf06f34727447fad04cbcbce2b8b3f269c1b9307)
- Fixed an issue with file output processing in CMP applications when the certificate does not exist.
  ↳ No PR: [60c3d73](https://github.com/openssl/openssl/commit/60c3d732b7b634290e4ec5d7ca6fb9b0a37592bf)
- Improved error messages under different stream conditions in QUIC unpacking processing to more precisely indicate the cause of the protocol error.
  ↳ No PR: [2d2fd15](https://github.com/openssl/openssl/commit/2d2fd151d4e699da269e586713e785a758f45157)
- Fixed compilation issues caused by simultaneously checking a macro definition and using that macro in a single preprocessor condition.
  ↳ No PR: [a509b97](https://github.com/openssl/openssl/commit/a509b97d2c4efd96e231913d49544ac7cb36b51b)
- Fixed the issue where the i2r_ADMISSION_SYNTAX() function returned -1 on error and changed to return 0 to maintain consistency.
  ↳ No PR: [53b5d6c](https://github.com/openssl/openssl/commit/53b5d6c30f3b8eaf7a582da2265c0d1cfe14d54f)
- Fixed multiple issues with the transport package generator in the QUIC test server.
  ↳ No PR: [091f532](https://github.com/openssl/openssl/commit/091f532e0ef57cff71ab710c07eb5f6f9bb88b22)
- Fixed the wrong branch jump in ossl_bn_rsa_fips186_4_derive_prime() to ensure that the function returns the failure status correctly.
  ↳ No PR: [835b90a](https://github.com/openssl/openssl/commit/835b90a19cdb2901cdba8a26955ccaacf0d73062)
- Fixed kbkdf_dup function pointer type, corrected from OSSL_FUNC_kdf_newctx_fn to OSSL_FUNC_kdf_dupctx_fn.
  ↳ No PR: [344d3b3](https://github.com/openssl/openssl/commit/344d3b326d573a0eeb5dcbffa643bc06f00023ed)
- Optimized calling OPENSSL_init_crypto only under the default libctx to avoid unnecessary initialization when using non-default libctx.
  ↳ No PR: [7a6a0ba](https://github.com/openssl/openssl/commit/7a6a0baa591e3d04831ed0f468c72dc45feba452)
- Fixed minor issues in QUIC congestion control: removed unused variables and added integer overflow protection in tests.
  ↳ No PR: [0f1c43c](https://github.com/openssl/openssl/commit/0f1c43c441acd23ba2c14c93f9ce059348a617b0)
- Fixed a possible race condition when searching in an unsorted stack.
  ↳ No PR: [eb0935f](https://github.com/openssl/openssl/commit/eb0935fd21220708e4321374380db497e9c5ecdf)
- Fixed undefined behavior caused by calling pthread_key_delete on uninitialized data.
  ↳ No PR: [31295ca](https://github.com/openssl/openssl/commit/31295ca02c0a2d7209a33047c7f6dd1dabc12c93)
- Fixed the infinite loop problem caused by the zero-length handshake fragment record not being released.
  ↳ No PR: [c20d923](https://github.com/openssl/openssl/commit/c20d923b46641030cb2946a1922ee344b9d27e43)
- Fixed an issue where p < q may occur when generating RSA keys, automatically swap p and q to ensure p > q.
  ↳ No PR: [dc231eb](https://github.com/openssl/openssl/commit/dc231eb598460aec239c7f597f560bca47d9f72a)
- Removed spurious error message when certain configuration file entries are not provided.
  ↳ No PR: [c8aec16](https://github.com/openssl/openssl/commit/c8aec16383c7a9aec76b28e6eb95d36bef6f7e56)
- Fixed conditional compilation issue when DTLS and TLS are disabled at the same time.
  ↳ No PR: [fb32f6e](https://github.com/openssl/openssl/commit/fb32f6ea42e6916ff88cc44cf5de6e63ba596aca)
- Fixed format string mismatch in QUIC TLS error handling.
  ↳ No PR: [5ad3cc1](https://github.com/openssl/openssl/commit/5ad3cc19282e2f98189467cd6aeae8d0389b999b)
- Fixed the problem of missing io parameters when calling the ossl_quic_is_stream_local function.
  ↳ No PR: [7b1ca59](https://github.com/openssl/openssl/commit/7b1ca59995a0d0ad933b5d475face79b8ec99828)
- Fixed an issue in several QUIC sample programs where sockets were not closed when setting non-blocking mode failed.
  ↳ No PR: [cdedecd](https://github.com/openssl/openssl/commit/cdedecd50351a3624b074e6a425d8dfb3af5fa6a)
- The application now outputs an appropriate error message when a store cannot be opened or loaded.
  ↳ No PR: [edc2b6e](https://github.com/openssl/openssl/commit/edc2b6e3b1950ab0fb71e2d7dca0836b43a9ec3b)
- In fuzz testing mode, ignore invalid signatures in QUIC handshake certificate verification.
  ↳ No PR: [702bb16](https://github.com/openssl/openssl/commit/702bb16b9f38c4b17879b0d22bd08ea495c578e2)
- Removed a redundant error printing statement in apps.c.
  ↳ No PR: [1d76885](https://github.com/openssl/openssl/commit/1d768852e938ea1b4c6076df0c5a1e59f9027f8c)
- It is no longer mandatory that RSA keys must contain CRT parameters, allowing setting RSA parameters without reporting an error when CRT parameters are missing.
  ↳ No PR: [2647726](https://github.com/openssl/openssl/commit/2647726bd3ca63dc5f07ae3f10e16dff35d95626)
- Updated the documentation of openssl passwd command and deleted duplicate option descriptions.
  ↳ No PR: [116799f](https://github.com/openssl/openssl/commit/116799ff6a8fc803ec4685fc432c7329d0511e23)
- Re-added documentation for the four functions d2i_X509_bio, d2i_X509_fp, i2d_X509_bio and i2d_X509_fp.
  ↳ No PR: [4db1df8](https://github.com/openssl/openssl/commit/4db1df8e824733b6289dc86dcc78bfe325031969)
- Fixed the off-by-one error in the OBJ_obj2txt function return value documentation, and removed the outdated BUGS chapter.
  ↳ No PR: [67890a7](https://github.com/openssl/openssl/commit/67890a738c0eb5e92c41189ba3c744fbc98a97ac)
- Fixed documentation of -list option in openssl-dgst man page, fixed command to list digest algorithms.
  ↳ No PR: [5719dd4](https://github.com/openssl/openssl/commit/5719dd461fc2cc5d5d29fc3d7e9a6deca3130a7e)
- Fixed incorrect handling of SSL read return values from the on_rx_push function in the QUIC DDD example.
  ↳ No PR: [b1cb067](https://github.com/openssl/openssl/commit/b1cb0675e5c76c6dd78863e6857b5456718da7b5)
- Updated example code to differentiate between streaming errors and connection errors.
  ↳ No PR: [02e36ed](https://github.com/openssl/openssl/commit/02e36ed3525a2f0fda1b21e948ec5f522cf9379c)
- Fixed default value of ess_cert_id_alg option in openssl-ts(1) manual.
  ↳ No PR: [5ffad4b](https://github.com/openssl/openssl/commit/5ffad4bad9bd701cc3d14c96304484884ace0831)
- Fixed issues in the QUIC example code to make it consistent with the TLS example, and fixed several typos.
  ↳ No PR: [59d8a33](https://github.com/openssl/openssl/commit/59d8a338edca98e5bb077a2a364d82e53e7cce77)
- Updated the Makefile and source code of the QUIC DDD demonstration to fix the newline character issue in the host-port format string.
  ↳ No PR: [0d4a866](https://github.com/openssl/openssl/commit/0d4a8667e25406b39785c6d4a25b34a825eb798a)
- Fix build failure caused by uninitialized variables when compiling with -Wconditional-uninitialized.
  ↳ No PR: [abc4345](https://github.com/openssl/openssl/commit/abc4345a19430869b9a8925c6defc9e9ce977429)
- Fix compilation error caused by incorrect checking of OPENSSL_CPUID_OBJ macro when building with no-asm.
  ↳ No PR: [a8251a3](https://github.com/openssl/openssl/commit/a8251a32a0dc449fc39f44a1768e091fcc077227)
- Fixed build failure issue without SRTP support and added conditional compilation protection in test code.
  ↳ No PR: [9f3cd80](https://github.com/openssl/openssl/commit/9f3cd808b33767ae65e29461ce17a091049e7364)
- Adjust the structure initialization method to eliminate compilation warnings when clang 6/7/8 strictly builds.
  ↳ No PR: [6cac1ce](https://github.com/openssl/openssl/commit/6cac1ce47128f5095b1f0b99f304589db034c305)
- Removed loop waiting for QUIC server to shut down in util/quicserver.c.
  ↳ No PR: [bd3b026](https://github.com/openssl/openssl/commit/bd3b026faab3b5ee5aa6b52ba6eb4080bc144b28)

### Refactoring optimization
- When processing TLS 1.3 records under KTLS, skip steps such as depadding, outer type checking and inner type extraction, and adjust record length checking and type pointer passing in message callbacks.
  ↳ No PR: [a5fb960](https://github.com/openssl/openssl/commit/a5fb9605329fb939abb536c1604d44a511741624), [64da15c](https://github.com/openssl/openssl/commit/64da15c40d15aac58e211fd25d00e9ae84d0379b), [b6f7519](https://github.com/openssl/openssl/commit/b6f7519bc4b645809b3dcf97478fabbb3037f3e2)
- Clarify the logic of the subject/req parameter in X509V3_set_ctx used to construct the SAN email address from the subject DN, and improve the coding style and error codes.
  ↳ No PR: [317acac](https://github.com/openssl/openssl/commit/317acac5cc0a2cb31bc4b91353c2b752a3989d8a)
- Improve diagnostic information for transactionID mismatch in CMP, uniformly use the i2s_ASN1_OCTET_STRING function to handle the string representation of ASN1_OCTET_STRING, and adjust the recipNone check to maintain consistency.
  ↳ No PR: [a3ea35c](https://github.com/openssl/openssl/commit/a3ea35c2936acbe6a53b1d52d2d7addbfb6bbd5a), [e469971](https://github.com/openssl/openssl/commit/e46997111af3a11632df411b01d62fd39cc3faaf)
- Replace unsigned long type in DER writer with uint32_t, and rename related functions and update call sites.
  ↳ No PR: [5919625](https://github.com/openssl/openssl/commit/59196250cb45ecd128d2f8bbc47de612167606d3)
- When the DTLS record layer is closed, push unprocessed records in the buffer to the next record layer object and adjust the epoch setting of the unprocessed record queue.
  ↳ No PR: [7a15ed6](https://github.com/openssl/openssl/commit/7a15ed64fa5387dfbf1db391b84ddc7b1bf25571)
- Use OSSL_TRACE_STRING output message body instead in OSSL_HTTP_REQ_CTX_nbio, and optimize Content-Type matching, error status handling and trace output format.
  ↳ No PR: [35b76bc](https://github.com/openssl/openssl/commit/35b76bc818ebeb9d36bed22ea0a7b4f03204619a)
- Migrate the read buffer release logic of SSL_MODE_RELEASE_BUFFERS to the record layer, and clean up the legacy TODO code.
  ↳ No PR: [3de7695](https://github.com/openssl/openssl/commit/3de7695928478bce22dcf6bf87883688d895dc43)
- Renamed the DTLS1_BITMAP structure and related functions to DTLS_BITMAP, and adjusted bit operations to support 64-bit systems.
  ↳ No PR: [f6aab7b](https://github.com/openssl/openssl/commit/f6aab7b1e1410cf28ec45410aa4ee54f40baf13d)
- Renamed require_ca parameter to non_leaf to more accurately reflect the meaning.
  ↳ No PR: [8a2f9a7](https://github.com/openssl/openssl/commit/8a2f9a7cc8ab588d23fb96afd696f9da2c61c2c7)
- Migrated the internal time representation of libssl and crypto modules from time_t and struct timeval to OSSL_TIME, the public API keeps the original type but performs conversion internally.
  ↳ No PR: [f0131dc](https://github.com/openssl/openssl/commit/f0131dc04a39afcb1629f5bec2814ef3a4925bbf), [5d1bb4f](https://github.com/openssl/openssl/commit/5d1bb4fc47582b06dd224a788bdfaaced60e72a0), [4d32f53](https://github.com/openssl/openssl/commit/4d32f5332fa69ac949feec54c273fe63639ad891), [d6bfdf6](https://github.com/openssl/openssl/commit/d6bfdf6789f65b1b503f0cdd56010705f7c632d0), [340fe50](https://github.com/openssl/openssl/commit/340fe504e42e3e4b6399caff165097cedc994c5e), [4fc04c7](https://github.com/openssl/openssl/commit/4fc04c71acf180dad0b4418d12b3ed31ba46179a)
- Change the parameter type of the COMP_METHOD structure and related functions from unsigned int to size_t, change the return value to ossl_ssize_t, add NULL pointer checking, and remove non-functional COMP_METHODS.
  ↳ No PR: [7e3caca](https://github.com/openssl/openssl/commit/7e3cacac943d298348d97c8f7f980ca0916378c5)
- Refactor the write record layer to provide correct return values, and replace SSLfatal calls with RLAYERfatal.
  ↳ No PR: [320145d](https://github.com/openssl/openssl/commit/320145d5b3a11492427fe1cab9ca4de52402c72d)
- Call get_max_records in the record layer code, decide how to divide the data to be written into records based on the returned data, and adjust the record release and write functions accordingly.
  ↳ No PR: [02719d5](https://github.com/openssl/openssl/commit/02719d5c4c1e64350b4dddb17e703864809e130a)
- Moved the QUIC_CONNECTION type definition to an internal header file, and added functions to get the QUIC_CONNECTION pointer from the SSL pointer, as well as setters/getters for the QRX and ACKM fields.
  ↳ No PR: [d5ab48a](https://github.com/openssl/openssl/commit/d5ab48a192d45ec51355ef2a186125961331eb9b)
- Remove legacy TODO comments and adjust alignment calculation logic when writing TLS records.
  ↳ No PR: [4fed6ee](https://github.com/openssl/openssl/commit/4fed6ee1ce4a3374d7223654db13132144275c05)
- Removed two no-op function pointers from OSSL_RECORD_METHOD that were never called.
  ↳ No PR: [fba0206](https://github.com/openssl/openssl/commit/fba0206da7c0cc68854bb63a6ee9b96a74f4ed7a)
- QUIC RX adds reference counting support, no longer requires the caller to manage reference counting, and removes the OSSL_QRX_PKT_WRAP wrapping structure.
  ↳ No PR: [6d5d5fc](https://github.com/openssl/openssl/commit/6d5d5fc9a9f6b701fc5e17f05d3df464fe0bc56e)
- Removed the logic of automatically discarding the Initial encryption layer in the QUIC receiver, and left this operation to the upper layer for processing.
  ↳ No PR: [203b0d0](https://github.com/openssl/openssl/commit/203b0d00e00f524f786f5e911f889cc96e32402d)
- QUIC TX no longer manages BIO reference counting internally, and changes ossl_qtx_set1_bio to ossl_qtx_set_bio. The caller needs to ensure the BIO life cycle by itself.
  ↳ No PR: [cdd3f73](https://github.com/openssl/openssl/commit/cdd3f7323613aaaf316b0b2d3a7700fbc602c8ef)
- Removed several no longer used fields in the SSL_CONNECTION structure, including encryption context, compression/expansion, IV and MAC keys, etc., to clean up the internal structure.
  ↳ No PR: [f471f60](https://github.com/openssl/openssl/commit/f471f60a8adcbb72314be974f6bc320943786b96), [6d814fd](https://github.com/openssl/openssl/commit/6d814fd6074b5f293abc3f19a190d3e34c426b6a), [b83eac4](https://github.com/openssl/openssl/commit/b83eac48ed44afecd0d392c2fa055d345578078d), [1e42708](https://github.com/openssl/openssl/commit/1e42708e175f1453bd12f4632fbc0c61bade4e81), [e95d6e1](https://github.com/openssl/openssl/commit/e95d6e1eec2f080713aa91c12e411cea4cffee65)
- Roll back the timing attack fix in RSA decryption, but keep the change to move derive_kdk to a separate function.
  ↳ No PR: [4209ce6](https://github.com/openssl/openssl/commit/4209ce68d8fe8b1506494efa03d378d05baf9ff8)
- Added CERTIFICATE_VERIFY_MAX_LENGTH constant, which is used to limit the maximum length of CertificateVerify message and is applied in the state machine.
  ↳ No PR: [c6d14bf](https://github.com/openssl/openssl/commit/c6d14bfd5f16a103181c04614492be03e137d1a4)
- Refactor the DRBG implementation so that it manages the acquisition and release of locks by itself and no longer relies on the lock/unlock prompts of the EVP layer.
  ↳ No PR: [189ad3a](https://github.com/openssl/openssl/commit/189ad3ab2028babd39241015fc3975e8334c87eb)
- Improve the checking logic of -tls_used option in CMP client: automatically enable -tls_used when -server URL is HTTPS.
  ↳ No PR: [4a9299a](https://github.com/openssl/openssl/commit/4a9299ac5090dc7997bd1f2cbc56e5e11c6277ff)
- Update the reference counting operation of DH objects to structure-based atomic operations.
  ↳ No PR: [9015cbb](https://github.com/openssl/openssl/commit/9015cbb6eb7a50b04352d625e3907dfbb70684d0)
- Update DSA's reference counting operations to structure-based atomic operations.
  ↳ No PR: [495e6d3](https://github.com/openssl/openssl/commit/495e6d3b6266176b92ea20dbc6541ca724fa07ff)
- Updated the reference counting operation of the DSO module to be a structure-based atomic operation.
  ↳ No PR: [aaab365](https://github.com/openssl/openssl/commit/aaab365c5afb950b9ffaa2916635a18e0d34fa98)
- Updated ASN1 locking functions to use structure-based atomic operations to manage reference counting.
  ↳ No PR: [420ad86](https://github.com/openssl/openssl/commit/420ad86a0e35ddbd65dae7e9458e36223af5f140)
- Updated the EC module's reference counting operations to a struct-based atomic implementation.
  ↳ No PR: [1353736](https://github.com/openssl/openssl/commit/1353736b3e6f33a9f6e47f837c5de05cc0dd3647)
- Change provider's reference counting and activation counting operations to structure-based atomic operations.
  ↳ No PR: [8752694](https://github.com/openssl/openssl/commit/8752694bad830a91ba508451b220c23a99f182f1)
- Updated RSA's reference counting to struct-based atomic operations.
  ↳ No PR: [97937cf](https://github.com/openssl/openssl/commit/97937cfcd8b5a011dd54e74eb2cc3cc26a533b10)
- When sending congestion control probe packets, full-size packets are no longer generated, but only small packets containing PING and ACK frames are generated.
  ↳ No PR: [d56b564](https://github.com/openssl/openssl/commit/d56b564b25f9cafacdd57ac43b8b6618202047a5)
- Major refactoring of QUIC TXP to properly handle fill logic and introduce a new package generation geometry calculation and submission process.
  ↳ No PR: [faebafd](https://github.com/openssl/openssl/commit/faebafda9fa232dc84fee2bbf16d478425703490), [c206f2a](https://github.com/openssl/openssl/commit/c206f2aa62ace93ce06a940e6992ffb4f3316bb5)
- Removed extra parentheses in felem_reduce method in secp384r1.
  ↳ No PR: [670e73d](https://github.com/openssl/openssl/commit/670e73d9084465384b11ef24802ca4a313e1d2f4)
- Removed the integrity check of private key parameters in ossl_rsa_todata so that it only returns the parameters that have been set.
  ↳ No PR: [4ad3a44](https://github.com/openssl/openssl/commit/4ad3a44ba45a4026170336161228d435f6784564)
- Pass the DTLS record version to the message callback function.
  ↳ No PR: [b31597d](https://github.com/openssl/openssl/commit/b31597d989f422a0d341be4946d4d64a9251047f), [5f79670](https://github.com/openssl/openssl/commit/5f79670f7b9b0354a5f6ccac9474f7a12f86407e)
- Added internal function ossl_ackm_get_largest_acked, which is used to query the largest confirmed packet number in the specified packet space.
  ↳ No PR: [81b400c](https://github.com/openssl/openssl/commit/81b400cf900c530e170a1488222191c5568f6b2d)
- Reconstructed DTLS timeout processing, extracted the BIO_CTRL_DGRAM_SET_NEXT_TIMEOUT call into an independent function, and simplified the return type and timeout judgment logic.
  ↳ No PR: [24a3225](https://github.com/openssl/openssl/commit/24a322544373f7acda05e19f64a6c3120d459d5b)
- Introduce macros HAS_CASE_PREFIX, CHECK_AND_SKIP_CASE_PREFIX and HAS_CASE_SUFFIX to replace manual case prefix/suffix comparison and simplify the code.
  ↳ No PR: [747adb6](https://github.com/openssl/openssl/commit/747adb6a0134e3b707fbc47d0f0c52d6ff9c4223)
- Rename the variable enc_flag to enc_name, and simplify the related assignment logic to improve readability.
  ↳ No PR: [870871e](https://github.com/openssl/openssl/commit/870871e5df4f47611c38e81d3f50e38cbf362082)
- Simplify the macro definition of the ARIA AEAD cipher, removing the fixed NID, block size and IV length parameters, leaving only the key length and mode name.
  ↳ No PR: [e6b1c22](https://github.com/openssl/openssl/commit/e6b1c22b41b5feaffe7fe2bb24996fb6763586af)
- Unify the coding style and use interface functions instead of direct references to the fields of the EVP_CIPHER_CTX structure.
  ↳ No PR: [b134300](https://github.com/openssl/openssl/commit/b134300a342476398c11c19af602d7b2aa6b7f8a)
- Avoid using global EVP_CIPHER and EVP_MD in providers, only accept non-global algorithms, and update tests to load the default provider.
  ↳ No PR: [e59bfba](https://github.com/openssl/openssl/commit/e59bfbaa2dbd680f77e1121e382502bd522a466c)
- Change the strength checking of TLS RC4 ciphers to be data-driven, adjust the strength value and remove the hard-coded security check.
  ↳ No PR: [c3b5fa4](https://github.com/openssl/openssl/commit/c3b5fa4ab7d19e35311a21fec3ebc0a333c352b6)
- Remove the redundant check on whether type is NULL, and move the engine-related conditional judgment to the preprocessing guard.
  ↳ No PR: [10cf46c](https://github.com/openssl/openssl/commit/10cf46c4ef93e22f999b7b6d2c3aadc4db965e5a)
- No longer use the global variables ossl_property_true and ossl_property_false, instead use predefined macro constants, and verify that their values are consistent with the constants during initialization.
  ↳ No PR: [6de9214](https://github.com/openssl/openssl/commit/6de9214a5062e9d015c84cbbab681184e16fccaa)
- Remove the unused fallback flag field flag_fallback and its setting function ossl_provider_set_fallback.
  ↳ No PR: [90c3113](https://github.com/openssl/openssl/commit/90c311315c15a4fea895fd317d9c8fe801ba04a0)
- Simplified provider existence check logic, no longer attempts to check whether the provider exists in ossl_provider_new, and leaves the confirmation responsibility to the caller.
  ↳ No PR: [dc6d9ed](https://github.com/openssl/openssl/commit/dc6d9ede6241e6858f8fa78435d6c8eb9cf85aa1)
- Extract provider activation logic from the configuration loading function into an independent function, and optimize error handling.
  ↳ No PR: [07ba694](https://github.com/openssl/openssl/commit/07ba69483a7d8005a53284cbde55b9dac8c5c554)
- Reconstruct the bin2bn() function, change the processing order from the most significant chunk to the least significant chunk, and simplify the internal calculation logic to prepare for supporting signed input.
  ↳ No PR: [c30de60](https://github.com/openssl/openssl/commit/c30de601850f367e4c16ad91c0168a2e0dc647c0)
- In the key_to_type_specific_pem_bio_cb function, use the passed password callback parameter instead of the internal default callback.
  ↳ No PR: [c22b659](https://github.com/openssl/openssl/commit/c22b6592135bfba95a315e438ac7bfc6db461407)
- Improve the print_itavs() function so that it returns an integer value to indicate the execution status and handles error conditions accordingly at the call site.
  ↳ No PR: [d965064](https://github.com/openssl/openssl/commit/d9650648821aadabf2d9f3de321f344230b13a4a)
- Simplify the read_write_req_resp() function, removing the non-null check on the req parameter, as this parameter is not expected to be NULL.
  ↳ No PR: [61fa00a](https://github.com/openssl/openssl/commit/61fa00a4d03f6808389bc1847937f72d184f0627)
- Introduced macro definitions in cmp_ctx.c, simplified the implementation of a large number of getter and setter functions, and removed redundant code.
  ↳ No PR: [08dfbe0](https://github.com/openssl/openssl/commit/08dfbe0798f57ac9e9793fdfcaff54cfdf6b3359)
- Removed unused WPACKET *pkt parameters in get_construct_message_f function pointer and its related implementation.
  ↳ No PR: [e1c1227](https://github.com/openssl/openssl/commit/e1c122711edc3b9d64e506a51c3c0482569b7498)
- Fixed the code style of multiple functions in apps/lib/apps.c, and reconstructed the macros and functions related to certificate loading.
  ↳ No PR: [8cdb993](https://github.com/openssl/openssl/commit/8cdb993d8b1ad9fd58fb5f41cc43df97014f00c9)
- Remove unused callback variables in EVP_PKEY_generate.
  ↳ No PR: [64a6445](https://github.com/openssl/openssl/commit/64a644530e023d3064db9027b0977d33b1d2ad9a)
- Use the progress_cb callback in the genrsa command instead, and remove the original genrsa_cb function.
  ↳ No PR: [261b399](https://github.com/openssl/openssl/commit/261b399fd7b1f4339e6d0fa3ee37b32b81d9d9e0)
- Avoid direct access to the key length field, use the API to obtain the key length instead, and use this value uniformly when initializing the key in AES-GCM.
  ↳ No PR: [80ce874](https://github.com/openssl/openssl/commit/80ce874a093087b919e1c722427df30f81f5dad5)
- Restored the use of thiswr variable in do_ssl3_write, added record layer related functions and adjusted the schedule.
  ↳ No PR: [b375a8a](https://github.com/openssl/openssl/commit/b375a8ac9b672bba8e651c11afd2e0a466563742)
- Unify the macro naming of SSL key exchange algorithms, replacing the old aliases SSL_kEDH and SSL_kEECDH with the more commonly used SSL_kDHE and SSL_kECDHE.
  ↳ No PR: [66914fc](https://github.com/openssl/openssl/commit/66914fc024cfe0fec00dc0f2c7bd8a7957da5ec4)
- Introduce using_ktls auxiliary variable in ssl3_get_record() to simplify the conditional judgment of KTLS receiving path.
  ↳ No PR: [031132c](https://github.com/openssl/openssl/commit/031132c297e54cbc20404a0bf8de6ed863196399)
- Move the Record layer method code to a subdirectory and update the relevant header file reference paths.
  ↳ No PR: [4840c2a](https://github.com/openssl/openssl/commit/4840c2a5e6c412a09dbb1c3c76f3117e5721bb76)
- Refactor the pre- and post-conditions of method construction to pass the no_store flag to the pre-condition function so that it can distinguish between permanent and temporary storage.
  ↳ No PR: [10937d5](https://github.com/openssl/openssl/commit/10937d5867039afbf869c8514245ed7599b61307)
- Remove unused variable m and related release calls in the X509_print_ex function, and simplify the conditional logic.
  ↳ No PR: [36699c1](https://github.com/openssl/openssl/commit/36699c12d37c5bef000cbe3d9b4b2b89bee4e17e)
- Unify locale initialization logic, eliminating duplicate code in FIPS providers.
  ↳ No PR: [26ccb0e](https://github.com/openssl/openssl/commit/26ccb0e4e0b100423184636457cd6aab4cc779ab)
- Optimize the internal name lookup function to avoid unnecessary string copying and reduce memory allocation and release overhead.
  ↳ No PR: [dab5098](https://github.com/openssl/openssl/commit/dab5098eacb9e264c32a33332ba047f234a3de68)
- Remove the dependence on SSL object status check in the record layer, and instead directly check whether the alarm code has been set in the record layer.
  ↳ No PR: [651216d](https://github.com/openssl/openssl/commit/651216dd54199c64bf9afd1256bbdde3990e1dfc)
- Move the sequence number into the OSSL_RECORD_LAYER object, removing the sequence number reference to the SSL object in the record layer.
  ↳ No PR: [0755722](https://github.com/openssl/openssl/commit/0755722c28309a52f29573221e411a2b37175e37)
- Remove the last reference to the SSL object in the record layer and refactor the related functions to directly use the internal structure of the record layer.
  ↳ No PR: [8124ab5](https://github.com/openssl/openssl/commit/8124ab56d4e8985151c5a0c4dca6af128fa89f2c)
- Renamed variable name multi to n_responders to improve code clarity.
  ↳ No PR: [5e87fdd](https://github.com/openssl/openssl/commit/5e87fddc971210ebb6df3fe77eeb858cd0bc4dea)
- Remove redundant early returns in BN_consttime_swap when a and b are the same pointer, and add related tests.
  ↳ No PR: [a644cb7](https://github.com/openssl/openssl/commit/a644cb7c1c19c78e2ca393c8ca36989e7ca61715)
- Replace SSL object references in state machine functions with SSL_CONNECTION, and clean up internal state access methods.
  ↳ No PR: [bfc0f10](https://github.com/openssl/openssl/commit/bfc0f10d0640fddbe63c0828389247691ab617f0)
- Clean up unused code and legacy logic in the record layer, and remove redundant functions and fields.
  ↳ No PR: [81c9ebd](https://github.com/openssl/openssl/commit/81c9ebd9099e7aac92a8c855a9ae1a30bad1d9cc), [51ccad3](https://github.com/openssl/openssl/commit/51ccad3f40e5f000da8364b1bb4bddd41657c96e), [b0a9042](https://github.com/openssl/openssl/commit/b0a9042e0f1e6bc18d1d945771903d0132766909), [2f90f85](https://github.com/openssl/openssl/commit/2f90f85cc018c55d2b73c691f192909e402d1416), [5bc226a](https://github.com/openssl/openssl/commit/5bc226ab3217525584a553ff1729567219d00e78), [22d6e85](https://github.com/openssl/openssl/commit/22d6e8547f11dae2e4c026be93331e9acfe9b940)
- Clean up the macros in GCM implementation and uniformly use function pointers for multiplication operations.
  ↳ No PR: [95201ef](https://github.com/openssl/openssl/commit/95201ef45711220455e8abf1cc6b334393384af2), [d50e093](https://github.com/openssl/openssl/commit/d50e0934e5b1537db0ea43986464b8f8f8b4e9fd)
- Standardize the naming of DTLS record layer functions, remove the dtls1_ prefix, and use the dtls_ prefix uniformly.
  ↳ No PR: [3a7a539](https://github.com/openssl/openssl/commit/3a7a539ec542b239efd375f63da070a5230f4ae0)
- Introduced the ossl_asn1_string_set_bits_left function, and reconstructed related functions to uniformly set the remaining bits flag of ASN1_STRING.
  ↳ No PR: [7c310e8](https://github.com/openssl/openssl/commit/7c310e872e72977432b3520c5d27641e13815548)
- Code cleanup and refactoring of app_http_tls_cb and tls_error_hint functions.
  ↳ No PR: [db30255](https://github.com/openssl/openssl/commit/db302550d32c0a450a47ab17990dd1b66551186a)
- Unify the type of epoch fields to uint16_t to eliminate the mixing of multiple integer types in internal representation.
  ↳ No PR: [279754d](https://github.com/openssl/openssl/commit/279754d4199f6e80e17b3e08fa261fbfd3e646c5)
- Change the return value of the constructor from a Boolean value to an enumeration type, supporting three return states.
  ↳ No PR: [67ec6d2](https://github.com/openssl/openssl/commit/67ec6d2b747810db609330003dcf08c8c584105b)
- Uniformly rename ossl_sleep to OSSL_sleep, and remove redundant header file inclusions.
  ↳ No PR: [5139dec](https://github.com/openssl/openssl/commit/5139dec255d0e2f991083cba9d9c62dbe6637046)
- Change OSSL_TIME type from simple integer to structure, and update related operation functions.
  ↳ No PR: [d13c8b7](https://github.com/openssl/openssl/commit/d13c8b7725437490be8c1a2b438936af10f808d0)
- Reconstruct the stream frame list insertion function in QUIC receiving stream management, remove manual error checking and optimize the insertion logic.
  ↳ No PR: [e77396f](https://github.com/openssl/openssl/commit/e77396f6f508f604b69f795e624896c427fe8b06)
- Replace the internal linked list implementation in the QUIC transport record layer, confirmation module, demux and record RX modules with list.h, and rename the linked list structure fields.
  ↳ No PR: [e32fc5a](https://github.com/openssl/openssl/commit/e32fc5ad0ea1a2d69f12d9208f2de489f7ee9737), [dead135](https://github.com/openssl/openssl/commit/dead13551c6661d34af3e5ddf1bc53c9efdb5647), [3fb172e](https://github.com/openssl/openssl/commit/3fb172ef0a635c2e705d3d1cb58624cfc6afd502), [ccdcb08](https://github.com/openssl/openssl/commit/ccdcb08d05725673a3c416f221905fb362dcf1a6)
- Change the uint_set data structure to use the list data type, and update the relevant calling code.
  ↳ No PR: [c5ca718](https://github.com/openssl/openssl/commit/c5ca718003e69ea0ef98392ce0abd4b6bfedeac8)
- Removed error reporting due to empty stack or out-of-bounds access in stack operation functions and returned NULL instead.
  ↳ No PR: [a8086e6](https://github.com/openssl/openssl/commit/a8086e6bfc37355626393751a94bc5c92df7e9d3)
- Use WPACKET in DTLS write record code instead of direct buffer writing, and unify error handling paths.
  ↳ No PR: [248a9bf](https://github.com/openssl/openssl/commit/248a9bf21ad5a61d911765964e2758e0da3c554c)
- Unified the code for incrementing the sequence counter into a new function, removing duplicate implementations scattered everywhere.
  ↳ No PR: [bed07b1](https://github.com/openssl/openssl/commit/bed07b187506ded20ef39dcbed56dc323ae44ff4)
- Delete the redundant dtls_write_records function and use tls_write_records_default uniformly.
  ↳ No PR: [43dfa5a](https://github.com/openssl/openssl/commit/43dfa5a9319f67cd652fdc3a8711fc53859cd11e)
- Removed several redundant functions in the SSL record layer.
  ↳ No PR: [b92fc4a](https://github.com/openssl/openssl/commit/b92fc4ae189fb0d5b0a2f34bc28e59cd7e1eed5a)
- Remove the thread termination function ossl_crypto_thread_native_terminate and its related status macros and test code.
  ↳ No PR: [4f32754](https://github.com/openssl/openssl/commit/4f32754f79d697e3af78d821296fd02fbba6e186)
- Migrate record layer declarations to ssl/record/methods and remove declarations that are no longer needed.
  ↳ No PR: [23c57f0](https://github.com/openssl/openssl/commit/23c57f001d997b939f9b7c76ffbf9e81a16b0141)
- Make DH parameter generation and checking functions use library context.
  ↳ No PR: [990d280](https://github.com/openssl/openssl/commit/990d280da95d3c955b86f38b01f5b95ea88d42bb), [7c639f0](https://github.com/openssl/openssl/commit/7c639f0b8e97b8290b9f935e83d5e948614c5bf7)
- Separate the QUIC channel receiving and sending encryption processing logic, and add a new channel cleaning function.
  ↳ No PR: [45ecfc9](https://github.com/openssl/openssl/commit/45ecfc9b52b2d1c9a810cefafe0e8bdd403b6b66)
- Adjust QUIC channel data pumping position to ensure it is only pumped once per tick.
  ↳ No PR: [3bf4dc8](https://github.com/openssl/openssl/commit/3bf4dc8c2106982d4ae6ada0650383e60f96d6e6)
- Remove redundant assignment statements in felem_inv function.
  ↳ No PR: [3d4dfeb](https://github.com/openssl/openssl/commit/3d4dfeb28a5cb944b8300b4cf807e19ab97d04f5)
- Refactor the hpke_aead_enc and hpke_aead_dec functions to directly pass in the OSSL_HPKE_CTX context object and simplify the parameter list.
  ↳ No PR: [9102214](https://github.com/openssl/openssl/commit/910221454bfcabf1917fa65462f4cae48be5a624)
- Replace the assert call in the QUIC module with ossl_assert to enhance error checking consistency.
  ↳ No PR: [7953444](https://github.com/openssl/openssl/commit/79534440c5ff2ab0a6233457531e903fbe2968b7)
- Renamed probe type fields and functions in QUIC ACKM and added comments to clarify usage.
  ↳ No PR: [8ca3baa](https://github.com/openssl/openssl/commit/8ca3baa9bdf972b963a70769780db67ebcbdf779)
- Refactor the QUIC ACKM detection reporting mechanism for accounting purposes.
  ↳ No PR: [e2212b2](https://github.com/openssl/openssl/commit/e2212b20bcf96c62c17a5e124c3bd61a98b8fcfd)
- Optimize QUIC SSL connection buffer management, directly return fixed state when releasing and allocating, and add corresponding tests.
  ↳ No PR: [fe33e2c](https://github.com/openssl/openssl/commit/fe33e2c8c1a99b82509e1119235dd106118c3f84)
- Renamed QUIC fault injection test functions and types from OSSL_QUIC_FAULT to QTEST_FAULT.
  ↳ No PR: [c12e111](https://github.com/openssl/openssl/commit/c12e11133625569f5b92a2a78486ecb70cd23df7)
- Switch the QUIC channel's mutex from CRYPTO_RWLOCK to CRYPTO_MUTEX.
  ↳ No PR: [ffce294](https://github.com/openssl/openssl/commit/ffce2946c7f59ad14ffeeef16a82bf7f04e8cd9c)
- Clean up FFC code: remove unnecessary null pointer checks, change ossl_ffc_set_digest return value to void, and limit peer testing of DSA key generation to FIPS modules.
  ↳ No PR: [a76ccb9](https://github.com/openssl/openssl/commit/a76ccb9d0ddc24f6551afbc220b41fb3c4e64c6a)
- Reconstruct the lock mechanism in QUIC thread-assisted mode to make the locking operation non-failable and remove return value checking and debugging output.
  ↳ No PR: [20f4574](https://github.com/openssl/openssl/commit/20f457436d0240f07835e098a6508668da9b02a4)
- Update KDF implementation: use shared functions to handle parameter information, remove duplicate buffer setting functions, unify string comparisons, add copy context support for HKDF and SSKDF, add R parameters for KBKDF.
  ↳ No PR: [345b42b](https://github.com/openssl/openssl/commit/345b42be90448523a335b9369452ea1159a1282a)
- Enhance the SSL object unpacking function in QUIC distribution, introduce the QCTX structure to uniformly extract connection and stream object information, and improve the protection of null pointers in error handling.
  ↳ No PR: [e88cdb8](https://github.com/openssl/openssl/commit/e88cdb8eb7b719803aaaef853db16abf3a4e73d1)
- Clean up the processing of SEND_STREAM/RECV_STREAM in QUIC QSM, reconstruct the reject stream function, and adjust the local variable declaration of the send function.
  ↳ No PR: [e8b9f63](https://github.com/openssl/openssl/commit/e8b9f63235e82403b7e144ff9a1a3985d44f1c4e)
- During the QUIC reception and unpacking process, application error codes are recorded for STOP_SENDING and RESET_STREAM frames to ensure the consistency of event AEC codes.
  ↳ No PR: [b6fc229](https://github.com/openssl/openssl/commit/b6fc2294a1a5bd6053647afea02180147018112b)
- In ASN1_STRING_TABLE_get and mime_parse_hdr, sort stack before lookup and fix conditional compilation of autoload configuration.
  ↳ No PR: [0feb90b](https://github.com/openssl/openssl/commit/0feb90ba6093a59dcea0279d699169f604600d49)
- Change the struct_ref field of ENGINE to an atomic operation, use atomic primitives to increase or decrease the reference count, and no longer rely on global locks.
  ↳ No PR: [e568d64](https://github.com/openssl/openssl/commit/e568d64f9fd3505454704f333bc1e58286f3419d)
- Introduced app_conf_try_string() and app_conf_try_number() auxiliary functions to simplify configuration item existence checking and error handling.
  ↳ No PR: [da7f81d](https://github.com/openssl/openssl/commit/da7f81d39308f9ecab6fde1f9116ff673ef3f3b3)
- Rename the message callback parameter msg_callback_s to msg_callback_ssl, and migrate the ossl_msg_cb type definition to the new header file internal/ssl.h.
  ↳ No PR: [c2786c8](https://github.com/openssl/openssl/commit/c2786c8ea732592f708e588f0f5849716914a313), [674b61e](https://github.com/openssl/openssl/commit/674b61ebd982d6a6564ac1f90d8cde22371564bc)
- Reconstruct QUIC TXP status output, using the extensible QUIC_TXP_STATUS structure instead of the original int *sent_ack_eliciting parameter.
  ↳ No PR: [a3a51d6](https://github.com/openssl/openssl/commit/a3a51d6ec38a8c2fd88e7c64c2f21632e55cbbdf)
- QUIC channel notifies ACKM after handshake confirmation.
  ↳ No PR: [29a541f](https://github.com/openssl/openssl/commit/29a541fe3643921462997856c46998f9b99f440f)
- Centralize the judgment of ACK trigger frames into depack_process_frames, and remove the scattered judgments in each frame processing function.
  ↳ No PR: [6cdb672](https://github.com/openssl/openssl/commit/6cdb672d0f65aa82044cedb9a96d46fa7da865f7)
- Optimize QUIC send stream state transition: add acceptance queue operation and stream limit check functions, adjust garbage collection conditions to support DATA_RECVD state.
  ↳ No PR: [7c88302](https://github.com/openssl/openssl/commit/7c88302b0120c22339a283947409b17bd349b075)
- Add DATA_SENT state transition logic for QUIC streams.
  ↳ No PR: [c068f4d](https://github.com/openssl/openssl/commit/c068f4d1e91e04b9da5c430b1e18c190c2460aad)
- Changed increment operation of error rate limit in FIPS self-test module from tsan_add to tsan_counter.
  ↳ No PR: [ff934cf](https://github.com/openssl/openssl/commit/ff934cfdc85a7b8ddb4bdebf9ab68d518bf68b7f)
- Add namemap null pointer check in ossl_namemap_doall_names and clean up internal auxiliary functions.
  ↳ No PR: [d808fa0](https://github.com/openssl/openssl/commit/d808fa015132d63f06f555649bc4b3f0e2e5124e)
- Updated the atomic operation interface in the QUIC implementation and removed the lock parameters that are no longer needed.
  ↳ No PR: [4eecc6a](https://github.com/openssl/openssl/commit/4eecc6aa5dee91b7ac1b8a40ab07bc6bc5930a5d)
- Refactor the reference counting type to structure, and migrate the reference counting management of KDF and MAC key data in the legacy provider.
  ↳ No PR: [7599d17](https://github.com/openssl/openssl/commit/7599d17d9385a7fd7489b81dfe560d319931f125), [99fd5b2](https://github.com/openssl/openssl/commit/99fd5b2b103f701151f4eb3fe0500ae0388e5136)
- Change the link attributes of the wrapper functions felem_select, felem_square_wrapper and felem_mul_wrapper in ecp_nistp521.c to static.
  ↳ No PR: [3e47a28](https://github.com/openssl/openssl/commit/3e47a286dc3274bda72a196c3a4030a1fc8302f1)
- Replace the macro definitions of QUIC encryption level and packet number space with enumeration types and add comments.
  ↳ No PR: [157c40e](https://github.com/openssl/openssl/commit/157c40e4d0a2c901e2dc0ee29b80a079a548d008)
- Delete the conditional judgment and unreachable code that are always false in the fmtfp function.
  ↳ No PR: [8ae4b23](https://github.com/openssl/openssl/commit/8ae4b236347d82226b6d86e02a9717e6a51d58a0)
- Removed several unused internal functions.
  ↳ No PR: [926601d](https://github.com/openssl/openssl/commit/926601dc0feab2def91ad5a98213436779864459)
- Simplified QUIC API masking and removed redundant QUIC connection checks.
  ↳ No PR: [9562842](https://github.com/openssl/openssl/commit/9562842b336c885b79385f2f6d65d0b2ff22a826)
- Removed redundant digest algorithm check in CMS_add1_signer function.
  ↳ No PR: [85b89a8](https://github.com/openssl/openssl/commit/85b89a8c6da76c241b2f62cf2944b5cf35dfcc24)
- Removed the unused sending parameter in derive_secret_key_and_iv() function and updated the call site.
  ↳ No PR: [fbd23b9](https://github.com/openssl/openssl/commit/fbd23b929609c0b2fe22da97ac349fae5a385027)
- Moved the QUIC frame type to string function to the source file, and corrected the access method of the stateless_reset field in preferred_addr decoding.
  ↳ No PR: [3989224](https://github.com/openssl/openssl/commit/398922463fd2fb0df52443932ca3e140554e5334)
- Moved the can-poll flag into the reactor structure, and added a new query function.
  ↳ No PR: [0b8b75e](https://github.com/openssl/openssl/commit/0b8b75e242e95db034e8026f462a799c0dafaefc)
- Cleaned up the management of polling descriptors in QUIC channels, extracted public functions and unified the termination reason copying method.
  ↳ No PR: [be96180](https://github.com/openssl/openssl/commit/be96180aa65fbf620eaf3ca8965a814b04e99130)
- Removed unused ssl3_comp_st structure definition.
  ↳ No PR: [2de153d](https://github.com/openssl/openssl/commit/2de153dc5a2565bd922b9a15955f2abca02b215e)
- Fixed fixed size handling in dgram_pair and dgram_mem, renamed field grows_on_write and reversed semantics.
  ↳ No PR: [b56b034](https://github.com/openssl/openssl/commit/b56b034e9afc980c846a61dbf581da3c46e67952)
- Changed the separator used in OPENSSL_buf2hexstr() function to DEFAULT_SEPARATOR constant.
  ↳ No PR: [861027f](https://github.com/openssl/openssl/commit/861027ffd06019baf82148837e30a992ca9b055e)
- When decoding DTLS records, store the protocol version field into the record structure.
  ↳ No PR: [4b5b223](https://github.com/openssl/openssl/commit/4b5b2239d8752f8dd413872057c57ef9e1a1a591)
- Cleaned up duplicate macro definitions and unused fields in SSL module.
  ↳ No PR: [226ed5f](https://github.com/openssl/openssl/commit/226ed5fb390f8cfc8b80cea79f57ae7837bc9b96), [7f7b0be](https://github.com/openssl/openssl/commit/7f7b0be8e3d452ecf5154203c5669f72683fde3f), [9007412](https://github.com/openssl/openssl/commit/9007412c1e1fd4bb9298901dae36064cd279c02a)
- Removed useless code, functions and statistical tracking functions in multiple internal modules.
  ↳ No PR: [a18cdd2](https://github.com/openssl/openssl/commit/a18cdd28077be05ec88538be84a761469f3f20c4), [17cca0e](https://github.com/openssl/openssl/commit/17cca0e85e83eac23069ddc5c5ebab6d7dd13ee1), [ed7c64f](https://github.com/openssl/openssl/commit/ed7c64fc540c5808efe4092465af1147c76555a1), [77d7b6e](https://github.com/openssl/openssl/commit/77d7b6eebb411fdb2c3d1390ac779300757aa9dc)
- Removed duplicate #include header files in multiple source files.
  ↳ No PR: [e257d3e](https://github.com/openssl/openssl/commit/e257d3e76ffb848b7607b04057257323dc51c3b4)
- Added checking of function return values to enhance error handling.
  ↳ No PR: [26997d6](https://github.com/openssl/openssl/commit/26997d66059432e1fa5bf946249a0bf6086dd716), [f91568e](https://github.com/openssl/openssl/commit/f91568eb50e847d0db2441fd9b9c5ffc8c4fe934)
- Improved coding style, comments and error handling for X.509 and OCSP modules.
  ↳ No PR: [c34e787](https://github.com/openssl/openssl/commit/c34e78766f9f89831d7ed684e411091bf7bfd3e7), [87943b9](https://github.com/openssl/openssl/commit/87943b933e52ffe59c7ba929ccaaccbe49a7be9e)
- Adjusted the header file inclusion relationship and moved the inclusion of internal header files to the source file.
  ↳ No PR: [80f3296](https://github.com/openssl/openssl/commit/80f32964a5388f5a313ced88f17a41f17794e369)
- Removed redundant OPENSSL_init_crypto() calls and corrected header file reference paths.
  ↳ No PR: [615525b](https://github.com/openssl/openssl/commit/615525bd4d6bbc56601fbdc82e7ac20344f48872)
- Added post_process_record callback call in DTLS record processing flow.
  ↳ No PR: [1d3f266](https://github.com/openssl/openssl/commit/1d3f266446eb5b12a4162804536b7356024977e3)
- Renamed types and functions in the HTTP/3 demo code, and added SNI configuration.
  ↳ No PR: [17b8f40](https://github.com/openssl/openssl/commit/17b8f405a212a01f9258eb7edcfb687a90cc8d28)
- Make ping and idle deadline calculations consistent for QUIC channels.
  ↳ No PR: [e401723](https://github.com/openssl/openssl/commit/e401723baf89b1f201a59fdd679f7ae6b5c123a2)
- Adjusted the stack memory reallocation ratio from 1.5 to 1.6, and optimized the growth calculation logic.
  ↳ No PR: [8347bfa](https://github.com/openssl/openssl/commit/8347bfa04fc62dcf684b8a43905709fa18f6a3b1)
- Adjusted the volatile qualifier in the TSAN auxiliary header file and added new macros.
  ↳ No PR: [e22cbe5](https://github.com/openssl/openssl/commit/e22cbe5e67461470590e6fb8858c95285fcdea0e)
- Added locale object initialization and cleanup functions in FIPS provider.
  ↳ No PR: [c5e7de5](https://github.com/openssl/openssl/commit/c5e7de5dee9995cbc7247e37ccd0a6ddd1f7db56)
- Removed unused internal functions ossl_a2ucompare and ossl_rsa_pss_params_30_set_maskgenalg.
  ↳ No PR: [23e6556](https://github.com/openssl/openssl/commit/23e65561e28f705f8f59128470aaf89bdbdb84fa), [1735531](https://github.com/openssl/openssl/commit/1735531c8ba7542e5fb2fe2f0becddb595955ace)
- Unified error reporting mechanism, using ERR_raise to replace legacy ECerr, EVPerr and perror calls.
  ↳ No PR: [bd07cc1](https://github.com/openssl/openssl/commit/bd07cc1c7e3ca38689e59868b5945dc223235a49), [5121783](https://github.com/openssl/openssl/commit/5121783b49327767c35ca39623734e586259c9dc)
- Clean up the use of SSL_CONNECTION macro, remove duplicate declarations and replace them with equivalent fields in the record layer structure.
  ↳ No PR: [5361a5a](https://github.com/openssl/openssl/commit/5361a5a9664046aefcd1a72858826bcb4c93ad9f), [d6cf4b5](https://github.com/openssl/openssl/commit/d6cf4b59a0f3c32d61828ee82c193494e13ff969)
- Removed many duplicate assignments, useless settings, unnecessary checks and unused unions.
  ↳ No PR: [6b08b78](https://github.com/openssl/openssl/commit/6b08b786ccba8fb84759a487cca439566a8678c2), [f659f7a](https://github.com/openssl/openssl/commit/f659f7a1c70709caa1727bb0b7f836d170d35bb5), [6c6e9d4](https://github.com/openssl/openssl/commit/6c6e9d4a18954f9aa4e7e153a4430cc935c18a90), [01a17b2](https://github.com/openssl/openssl/commit/01a17b24f6649fc192ba6bb9ea34e28ce9678e6c), [3abc0d3](https://github.com/openssl/openssl/commit/3abc0d3e8504f730117e3b68dfb1aab81c5e51fe)
- Improve QUIC code quality, clean up channel code and add const qualifiers to test server functions.
  ↳ No PR: [9f0ade7](https://github.com/openssl/openssl/commit/9f0ade7c470b0ee9be3c25d38bbec7d05ca4237e), [45bb98b](https://github.com/openssl/openssl/commit/45bb98bfa223efd3258f445ad443f878011450f0)
- Add non-null check for message callback function in the record layer.
  ↳ No PR: [b85ebc4](https://github.com/openssl/openssl/commit/b85ebc4b279ff0abe81c3a64eafc4f3c6c00605e)
- Fixed the writing of pointer comparison in elliptic curve implementation, changing the implicit Boolean check to explicit NULL comparison.
  ↳ No PR: [e1e93f7](https://github.com/openssl/openssl/commit/e1e93f7a07dfc7a8dddd4ddbb79d1d9bc9760d32)
- Clean up EBCDIC string definitions and uniformly use hexadecimal escape sequences to represent protocol strings.
  ↳ No PR: [44e4732](https://github.com/openssl/openssl/commit/44e47328178328198018c23e6918884af5e8ce4b)
- Add assertion in DTLS write function to ensure MTU size is not exceeded in non-compressed case.
  ↳ No PR: [351ad22](https://github.com/openssl/openssl/commit/351ad225b3758f96a5875eb11ac3acda006a1c00)
- Roll back the submission of the modulus size limit in the BN_mod_exp_mont_consttime function and remove the related test cases.
  ↳ No PR: [92d306b](https://github.com/openssl/openssl/commit/92d306b32b63dd502531a89fb96c4172be0ddb49)
- Internally declare DSA types in non-deprecated builds.
  ↳ No PR: [03fd2dc](https://github.com/openssl/openssl/commit/03fd2dcb3431898e54e24b3021e9106257e0fdf0)
- Remove unused variable assignments and adjust variable scopes to eliminate compilation warnings.
  ↳ No PR: [0c6c378](https://github.com/openssl/openssl/commit/0c6c3782870663dd190009103f22263f9a99c82e), [82b8116](https://github.com/openssl/openssl/commit/82b81161de41fde034f0d19e2ccddf190e4d8baf), [c71b72a](https://github.com/openssl/openssl/commit/c71b72acf24f1a3b4d9d07fe552fe1d5f76a2e35), [265920f](https://github.com/openssl/openssl/commit/265920f2a78ff295264824b5d8294dd45173ae42), [ef1ed41](https://github.com/openssl/openssl/commit/ef1ed411e1d526cdf6b87613d1b6021ab07d0f2e), [ade969e](https://github.com/openssl/openssl/commit/ade969e27b71a57e4d44ebada093929cc8f4193c)
- Renamed QUIC internal fields and functions to more accurately reflect their purpose.
  ↳ No PR: [54562e8](https://github.com/openssl/openssl/commit/54562e899c5394505417adc1e0c6410f6a0677f3), [1051b4a](https://github.com/openssl/openssl/commit/1051b4a0b9e307e51fdf491e6824e6610007824d)
- Remove unused macro definitions in bn_local.h.
  ↳ No PR: [dcfeb61](https://github.com/openssl/openssl/commit/dcfeb617477dd957f69e713cbc61fd4dca0f2db4)
- Remove specific initialization and cleanup code for stream 0 in QUIC channel.
  ↳ No PR: [c6c0432](https://github.com/openssl/openssl/commit/c6c0432cca9c46bde56a9480796762f25d2a18a7)
- Remove the key update processing in QUIC TXP and introduce an auxiliary function to verify the validity of the packet number.
  ↳ No PR: [b65b0d4](https://github.com/openssl/openssl/commit/b65b0d4ebe67ba9d53b96887b54ca9a0f5bf523e)
- Added a new utility function to determine whether the packet number is in the ACK frame.
  ↳ No PR: [dfd8176](https://github.com/openssl/openssl/commit/dfd8176f2556ca7ad0029012a048a3adc840bca5)
- Added a new query for QUIC TXP to specify the interface of the next available PN in the PN space.
  ↳ No PR: [007f9e9](https://github.com/openssl/openssl/commit/007f9e99ea92989d304584803e693fc90fb6af94)
- Reconstruct the QUIC RX key update callback so that it passes in the packet sequence number that triggers the update.
  ↳ No PR: [256eee3](https://github.com/openssl/openssl/commit/256eee3f3f500a50a434615a054b35a42a2f78b1)
- Optimize the error handling path of QUIC stream reset and fix comment spelling errors.
  ↳ No PR: [1d547f8](https://github.com/openssl/openssl/commit/1d547f8fc4fa2bc16fca935703ec90cfdf3fefd4)
- Add check for X509_STORE_lock return value to handle lock failure.
  ↳ No PR: [bc5d9cc](https://github.com/openssl/openssl/commit/bc5d9cc8711e86d5c25b81c58dfae531536e61fc)
- Add failure assertion in mutex lock and unlock operations.
  ↳ No PR: [17a0e93](https://github.com/openssl/openssl/commit/17a0e930d2607e1d571c82912d5e1fa3393b2053)
- Updated comments and replaced ssl3_get_message with tls_get_message_header and tls_get_message_body.
  ↳ No PR: [5318c01](https://github.com/openssl/openssl/commit/5318c012885a5382eadbf95aa9c1d35664bca819)
- Remove redundant release calls for NULL pointers and simplify error handling paths.
  ↳ No PR: [c37184f](https://github.com/openssl/openssl/commit/c37184f502eb7341e3095ef358a9ebd21facbc46)
- Cast the isspace parameter to unsigned char, and replace NCONF_get_string with app_conf_try_string.
  ↳ No PR: [8a2e74d](https://github.com/openssl/openssl/commit/8a2e74d0536c91585fbe789e0ab7b06cab0289c2)
- Add lock protection for lhash statistics collection to prevent data races.
  ↳ No PR: [43f1327](https://github.com/openssl/openssl/commit/43f132778b138870120d965f2fb61aa7411b78b2)
- Fixed the problem that the hash table leaf nodes were not cleared correctly when cleaning the OSSL_METHOD_STORE algorithm.
  ↳ No PR: [03454ba](https://github.com/openssl/openssl/commit/03454ba2a234197c961920f1bac37cc9f4cf3f54)
- Added null pointer check in EC key parameter export and use actual conversion format instead.
  ↳ No PR: [467b049](https://github.com/openssl/openssl/commit/467b0492c1e597857b30b91ed72605387aa9825b)

### Test related
- Added QUIC test server tool, extended test server API, supports flow status query, local connection ID update and network activity waiting functions.
  ↳ No PR: [37f27b9](https://github.com/openssl/openssl/commit/37f27b91deda5b6537883c06e845f0d2c28c5d5c), [1a0de4c](https://github.com/openssl/openssl/commit/1a0de4c1eea1f32a3e1113add26625d49b3854d8), [bbc9754](https://github.com/openssl/openssl/commit/bbc9754026e815429b55c92cf2a70e4ac59464cf), [80b9eca](https://github.com/openssl/openssl/commit/80b9eca279772185c32bb8d639af874b00217d6f), [219db5e](https://github.com/openssl/openssl/commit/219db5e43c4f030a1c9c4a2f28249fd89b05ea0d), [17340e8](https://github.com/openssl/openssl/commit/17340e87855fb785a986f09208af4279f74a201f), [614c08c](https://github.com/openssl/openssl/commit/614c08c23999e39945b556851eabff157aef833f), [644ef0b](https://github.com/openssl/openssl/commit/644ef0bb696eeaf3572e858b2beeca17b0621a3f)
- Replace the bitwise OR operator in the test code with a logical OR operator to eliminate Clang's -Wbitwise-instead-of-logical warning.
  ↳ No PR: [6162a24](https://github.com/openssl/openssl/commit/6162a2402d6b47c597c271bfb6a67d64bf183383)
- Add missing string.h header file in test file test/v3ext.c.
  ↳ No PR: [f9e578e](https://github.com/openssl/openssl/commit/f9e578e720bb35228948564192adbe3bc503d5fb)
- Added a new test to verify the order of TLS extensions, and added helper functions and related macro definitions to obtain the extension type.
  ↳ No PR: [ac44dea](https://github.com/openssl/openssl/commit/ac44deaf00ad24fd18b9d74de4a23d98a2b75c8d)
- Added a new fuzzer in PEM format to discover the CVE-2022-4450 vulnerability.
  ↳ No PR: [bc07d37](https://github.com/openssl/openssl/commit/bc07d371865095643ec4f7190f26b174830a2f02)
- Add provider-based speed testing functionality for KEM and SIG algorithms.
  ↳ No PR: [4557e28](https://github.com/openssl/openssl/commit/4557e280086d9e300c56183b8ad0671857530dc5)
- Added decoder fuzzer for discovering CVE-2023-0217.
  ↳ No PR: [a9e6100](https://github.com/openssl/openssl/commit/a9e6100bc98439ca787aa1fce541550ad1ff3e84)
- Add multiple info field splicing test cases for KBKDF, SSKDF and X963KDF.
  ↳ No PR: [8d18f20](https://github.com/openssl/openssl/commit/8d18f20800077913231c6b1d5c6630ff56047036)
- Added the OPENSSL_TEST_RAND_SEED environment variable, which allows the test random number seed to be set independently without affecting the test order, and displays the correct seed environment variable when the test fails.
  ↳ No PR: [44fbe0d](https://github.com/openssl/openssl/commit/44fbe0de34137c7834dc81c1116d7538a2b4f773)
- Introduce richer noise patterns in noisy dgram BIO, support random packet loss, delay and repeated datagrams, and add debug output to track the noise processing process.
  ↳ No PR: [d3a8dac](https://github.com/openssl/openssl/commit/d3a8daca587157dda52991448258800e9cf1f657), [43b94c7](https://github.com/openssl/openssl/commit/43b94c7fe4a427ad95f7401dd24f42d2ae094dfb), [c6bb25f](https://github.com/openssl/openssl/commit/c6bb25fab062738d22bea38462d14bd1c7de22e5), [19d79bb](https://github.com/openssl/openssl/commit/19d79bb2ba45729a49cbac9f98bd916190be0b4b), [5d3933e](https://github.com/openssl/openssl/commit/5d3933eef0d937a4845a439d5fbfa76738592fc0), [b1584a8](https://github.com/openssl/openssl/commit/b1584a85d07fdf1cfaa7423392fba439f7b6b0ac), [0a2369f](https://github.com/openssl/openssl/commit/0a2369fd446e27f59f0025d8d885c07a107df615), [21d2041](https://github.com/openssl/openssl/commit/21d2041da02c67218c94cef6792d8b84d810710b), [6dfc57f](https://github.com/openssl/openssl/commit/6dfc57f8a901f2cb40664a9f2060a91943a7982c), [8f67c6b](https://github.com/openssl/openssl/commit/8f67c6bb7cab70bbcc231ee3e18d140a2857ebdb)
- Improve malloc failure test: allow the percentage value in OPENSSL_MALLOC_FAILURES to support two decimal places, and add OPENSSL_MALLOC_SEED environment variable to support randomization.
  ↳ No PR: [3df5736](https://github.com/openssl/openssl/commit/3df5736cf303d2c69654ba1c295a9772b738608e)
- Fix potential array overflow issue reported by Coverity, increase parameter array size in digest_test_run from 3 to 4.
  ↳ No PR: [f205958](https://github.com/openssl/openssl/commit/f205958d9f9a2ead9edc088b0d3f060ee7c5b8c4)
- Added RFC 6979 deterministic ECDSA known answer test data.
  ↳ No PR: [5375fd8](https://github.com/openssl/openssl/commit/5375fd8e948234e8b8a10ded94badf6f59b53608)
- Added independent timing program.
  ↳ No PR: [6212fc6](https://github.com/openssl/openssl/commit/6212fc6814e8a8968bb35239cd454afd22b6a083)
- Added tests for ARM architecture's RNDR/RNDRRS instructions and merged shared logic with x86's RDRAND/RDSEED tests.
  ↳ No PR: [1f8ce0c](https://github.com/openssl/openssl/commit/1f8ce0c9faee59ac51a5db7a8ec42c38866be090)
- Added thread-safe object creation tests, and refactored multi-threaded tests to use common code.
  ↳ No PR: [0855591](https://github.com/openssl/openssl/commit/0855591e1f3559313641c13e4b7ce900ce42321c)
- Add tests for DANE cross-certificate fix, and increase test buffer to avoid overflow.
  ↳ No PR: [305c77a](https://github.com/openssl/openssl/commit/305c77aa8211beefe9c4081a8ffea4280c9765fc)
- Added SM2 encryption test cases based on GM/T 0003.5-2012 standard.
  ↳ No PR: [8ba65c3](https://github.com/openssl/openssl/commit/8ba65c35ea3af347c3b2adc8e665066b541a1c35)
- Expand custom extension testing, add custom extension test scenarios in certificate requests, and adjust related test configurations.
  ↳ No PR: [0db3a99](https://github.com/openssl/openssl/commit/0db3a9904fa00569905be130854a31dab7b8f49d)
- Skip KTLS testing for CHACHA cipher suites in FIPS mode to avoid FIPS incompatibility issues.
  ↳ No PR: [a5d8a2f](https://github.com/openssl/openssl/commit/a5d8a2f8f10b83e5afb297698fe72cee77b1837f)
- Fixed memory leak in asynctest, calling ASYNC_cleanup_thread() at the end of the test to release thread resources.
  ↳ No PR: [c5d0612](https://github.com/openssl/openssl/commit/c5d061290baa9466182b6d1a5b88aa9e5a4b2386)
- Added failure test cases for attribute parsing to cover error scenarios such as duplicate names, illegal characters, unterminated strings and invalid names.
  ↳ No PR: [747d142](https://github.com/openssl/openssl/commit/747d142318c5c9ecd80de3f061f54d7af4189039)
- Adjust the test cases to adapt to the change of the default security level from 1 to 2, and fix the problem of DH automatic test failure caused by the security level increase.
  ↳ No PR: [61cab65](https://github.com/openssl/openssl/commit/61cab65029e787d59d3f3138e0160adb8df85f99)
- To test the behavior of obtaining the correct signing provider for non-exportable keys, add a helper function to restore the stored state, and add an alternative key initialization test case.
  ↳ No PR: [0512283](https://github.com/openssl/openssl/commit/051228353a9842eede597294603cc06a55e3a22c)
- Added short output buffer tests for functions such as EVP_DigestSign, and added test cases for obtaining EC public key coordinates.
  ↳ No PR: [15ff7d7](https://github.com/openssl/openssl/commit/15ff7d7c2569a1aceaf6e85b61aee62422628fc9)
- Fix CMAC keygen test to ensure buffer size is passed correctly to EVP_DigestSignFinal.
  ↳ No PR: [cff7d58](https://github.com/openssl/openssl/commit/cff7d58eb4c8e0ef43e2fd0b12bc067bd3540e2c)
- Fixed an issue where the signature buffer size was not set correctly before calling EVP_DigestSign when generating signatures in the ACVP test.
  ↳ No PR: [1b32743](https://github.com/openssl/openssl/commit/1b327433e52c8acd6db0a69bc772d4bd1800a109)
- Added SM2 signature test cases based on GM/T 0003.5-2012 standard.
  ↳ No PR: [f087ebc](https://github.com/openssl/openssl/commit/f087ebcb2eb516a424245fcb93642e57ba024cc4)
- Fixed a possible resource leak problem in the write_session function in test/ssl_old_test.c when the session is empty.
  ↳ No PR: [34563be](https://github.com/openssl/openssl/commit/34563be5368fb8e6ade7d06d8376522ba83cd6ac)
- Add tests for ENGINE related issues and improve assertion checking in existing tests.
  ↳ No PR: [0299094](https://github.com/openssl/openssl/commit/0299094c52ddb66f9a22cfff4e7d70c139112832)
- Skip related test cases in builds without CMAC support.
  ↳ No PR: [ef2fb64](https://github.com/openssl/openssl/commit/ef2fb64f9dfde1965cb0b8a5f8765c4f467c1604)
- Add a test after the EVP_PKEY_fromdata call to verify whether the generated key can be used for PEM write operations.
  ↳ No PR: [fd19fc4](https://github.com/openssl/openssl/commit/fd19fc4c2726b08282b8db15f9bace2f04712498)
- Clean up test code, remove unused variables and clean up operations.
  ↳ No PR: [f541419](https://github.com/openssl/openssl/commit/f541419c792600f6ebe476168587d2a1436d87a3)
- Remove redundant RAND_get0_private() calls in tests.
  ↳ No PR: [a87c324](https://github.com/openssl/openssl/commit/a87c3247ca641f2593391bf44d47e3dccc7f8d73)
- Added unit test for integer overflow helper function.
  ↳ No PR: [bc4efcb](https://github.com/openssl/openssl/commit/bc4efcb0d0740467f1b8b536677a2886c2445c80)
- Check the return values of BN_new() and BN_dup() to avoid using null pointers when memory allocation fails.
  ↳ No PR: [d99004f](https://github.com/openssl/openssl/commit/d99004fe5de934120765d342586f08d22131b8ed)
- Added unit tests for DES weak keys and parity checking.
  ↳ No PR: [cc350c8](https://github.com/openssl/openssl/commit/cc350c882218b1053a636d01eb36573b3e7b20c2)
- Added reinitialization test cases for EVP_DigestSignInit, extending the number of tests from 15 to 30.
  ↳ No PR: [816f72d](https://github.com/openssl/openssl/commit/816f72d08834ee35ba2615f624b4a29f2717d1c7)
- Added SIPHASH MAC digestsign test to support re-initialization scenarios.
  ↳ No PR: [8cbfc4f](https://github.com/openssl/openssl/commit/8cbfc4f67b4e97d423ab4784dbbb54d454c6342a)
- Extend multi-threaded testing, increase the number of threads and try to load legacy providers to cover more competing paths.
  ↳ No PR: [293e251](https://github.com/openssl/openssl/commit/293e251e6f0367a9aa0d3d46037b19d1a6c91b20)
- Added unit test for priority queue.
  ↳ No PR: [f0a4935](https://github.com/openssl/openssl/commit/f0a4935827db5527d23da61805a1e73f0c660d39)
- Added test verifying that creating ECX private keys that are too short fails as expected.
  ↳ No PR: [8c08c8b](https://github.com/openssl/openssl/commit/8c08c8b37cab0eb66ca74fc65a40af3ccec77c00)
- Add RSA PSS padding mode test case for EVP_PKEY_sign_init_ex.
  ↳ No PR: [5321333](https://github.com/openssl/openssl/commit/5321333520b95a4f355916923af6c24dd10ed5dc)
- Add test case for copying uninitialized EVP_MD_CTX.
  ↳ No PR: [8c86529](https://github.com/openssl/openssl/commit/8c86529fe1b9ade0794c6f557ca8936f0c0de431)
- Fix and enable test_bn2padded test function, updated to use current API.
  ↳ No PR: [23750f6](https://github.com/openssl/openssl/commit/23750f677ef61b6bea4e81f23f335ad08fc49b51)
- Add memory allocation check in bio_enc_test.c to ensure BIO_new returns a valid pointer.
  ↳ No PR: [684326d](https://github.com/openssl/openssl/commit/684326d3bd3131debcdc410790e8dcf16f96103f)
- Refactor test functions in evp_extra_test.c, split test_fromdata and adjust other tests to support more comprehensive checking of key attributes.
  ↳ No PR: [5fbe15f](https://github.com/openssl/openssl/commit/5fbe15fd3b7c90a0cfb9f00be16225d8ed18b0dd)
- Fix resource release order in cmp_vfy_test.c and update trust store API calls.
  ↳ No PR: [869b7dd](https://github.com/openssl/openssl/commit/869b7dd00046951efb06dbb13c052ff9d7c87113)
- Fixed a memory leak in acvp_test.c caused by not releasing the memory allocated by d2i_ECDSA_SIG.
  ↳ No PR: [ec9135a](https://github.com/openssl/openssl/commit/ec9135a62320c861ab17f7179ebe470686360c64)
- Improve the test cases and add tests for the null digest algorithm and independent signature algorithm triplet addition.
  ↳ No PR: [2080da8](https://github.com/openssl/openssl/commit/2080da84a49b0c52fc8c6e6caef5d373235bd3e4)
- Added unit tests for property name and value to string functions, and adjusted tests to use independent library context.
  ↳ No PR: [9f6841e](https://github.com/openssl/openssl/commit/9f6841e9d8964943cf5f616543750cee85c4911c)
- Add a new test to verify that the size parameter of the pem_password_cb callback is equal to PEM_BUFSIZE, and change the test key file to an encrypted version.
  ↳ No PR: [c7debe8](https://github.com/openssl/openssl/commit/c7debe811123951a60cdfe73716184ca8fdd79d2)
- Added null pointer checks for memory allocation or function return values in multiple test files to improve the robustness of the test code.
  ↳ No PR: [2208ba5](https://github.com/openssl/openssl/commit/2208ba56ebefe4cf7d924e2ac7044ccd3307250b), [7625d70](https://github.com/openssl/openssl/commit/7625d70ad9e7be0588dd9453e89892c2b24b8175), [b2f90e9](https://github.com/openssl/openssl/commit/b2f90e93a07d992515782511a5770aa7cf7dc28f), [09030ee](https://github.com/openssl/openssl/commit/09030ee73693411c19b596cb0e0f43eb512ac0e6), [d43597c](https://github.com/openssl/openssl/commit/d43597c718dd6e4f2b18d5cec1eb791503a18988), [17da5f2](https://github.com/openssl/openssl/commit/17da5f2af833ef16cc2e431359139a4a2e3775b9), [18cb174](https://github.com/openssl/openssl/commit/18cb1740cc0fd11940836fa2fcaf6d3634c00e90), [78c5f12](https://github.com/openssl/openssl/commit/78c5f1266fdd859df04b0ce89e4dd849d9b590d7), [cf21d1c](https://github.com/openssl/openssl/commit/cf21d1c62dcd92be624ea0fb8a86d91e4fbeed93)
- Add support for context copy operations in KDF tests, and adjust related tests from failure scenarios to success scenarios.
  ↳ No PR: [c8adf19](https://github.com/openssl/openssl/commit/c8adf19d2da318cd7b007753d6c8a7f9dc94d4ed), [43332e4](https://github.com/openssl/openssl/commit/43332e405bea83a2d553e0519fdb04170879bc96)
- Add error checking and fix endianness issues in parameter conversion and parameter API tests.
  ↳ No PR: [291c5b3](https://github.com/openssl/openssl/commit/291c5b3e39f4c98e61cf7f65056fe49780d1f0ac), [9927749](https://github.com/openssl/openssl/commit/9927749ec2b8fc4b6146f0bd54cb6a44b8295974)
- Add test cases for the password context duplication (EVP_CIPHER_CTX_dup) function in evp_test.
  ↳ No PR: [ed16b0f](https://github.com/openssl/openssl/commit/ed16b0fc282d29f755e656043e8a70553ef7bea5)
- Add test case for EVP_PKEY_set1_encoded_public_key.
  ↳ No PR: [eafd3e9](https://github.com/openssl/openssl/commit/eafd3e9d07e99583a1439bb027e4d6af43e2df27)
- Add test cases for X509_STORE_CTX_set_purpose, covering the X509_PURPOSE_ANY scenario, and refactor the test framework to support loading certificates from directories.
  ↳ No PR: [8447f2e](https://github.com/openssl/openssl/commit/8447f2e3912c810a02ed1c8641db27ff70ded5ba)
- Added test cases for error handling of imported EC key parameters with invalid curve names in the test, and removed unused macro definitions.
  ↳ No PR: [d4d8f16](https://github.com/openssl/openssl/commit/d4d8f163db1d32c98d8f956e6966263a7a22fac1)
- Added TLS Fuzzer test infrastructure and added test configuration files.
  ↳ No PR: [db87f89](https://github.com/openssl/openssl/commit/db87f89b7393eea395b82050c7fc4e1869ef112e)
- Add a null pointer check on the return value of SSL/TLS related functions in the fuzz test to prevent memory allocation failure from causing undefined behavior.
  ↳ No PR: [885d97f](https://github.com/openssl/openssl/commit/885d97fbf84fb9de7548a5f6d4e90798f719022a), [edba197](https://github.com/openssl/openssl/commit/edba19760fa682ed095ca26ba89ba95530003bfe)
- Added null pointer check for SSL_CTX_new and OSSL_LIB_CTX_new return values in the test file to improve test robustness.
  ↳ No PR: [b0317df](https://github.com/openssl/openssl/commit/b0317df2311769e02d9ceb4e7afe19521f8ffbf1), [8d21573](https://github.com/openssl/openssl/commit/8d215738a05350baa583c47a2c52371d9cff3197)
- Fixed SNI test failure in sslapitest caused by using SSL_CTX_new instead of SSL_CTX_new_ex.
  ↳ No PR: [7e1eda4](https://github.com/openssl/openssl/commit/7e1eda483ec9ead36c05066b45ecad618475544c)
- Add test cases for Perfect Forward Security (PFS) in SECLEVEL >= 3 scenarios, and extend the test tool to support new DH parameters and TLS version options.
  ↳ No PR: [d71151a](https://github.com/openssl/openssl/commit/d71151ae704847f4ac3f4a5f394ea64f1d229815)
- Add a negative test case for BN_mod_sqrt to verify that a null pointer is returned when a negative input is entered.
  ↳ No PR: [3469282](https://github.com/openssl/openssl/commit/3469282ed2faee747868150089e07a187891b5ee)
- Fixed the resource leak problem when configuring the handshake context in the do_handshake_internal function fails.
  ↳ No PR: [6889ebf](https://github.com/openssl/openssl/commit/6889ebff01fa8cd7e5905f3f242edfed55fca443)
- Fix issue with uninitialized values reported by Coverity, explicitly initializing uninitialized local arrays to zero in test files.
  ↳ No PR: [3e35d3a](https://github.com/openssl/openssl/commit/3e35d3a4808526b9586bb87d423d488cf1b18d95)
- In the endecode_test test, add expected failure handling for non-FIPS elliptic curve keys, causing the test to skip encoding/decoding verification of non-FIPS keys in FIPS mode.
  ↳ No PR: [e8a4145](https://github.com/openssl/openssl/commit/e8a4145968eea576788761f39c5e4cb68b7c4a42)
- Fixed issue in testing when TLS 1.2 is disabled, added conditional skip logic.
  ↳ No PR: [40fb5a4](https://github.com/openssl/openssl/commit/40fb5a4ce3e90c9e8702aad0fcf43eb9f6edf419)
- Added fake_rsa_sig_dupctx function and related store support in the test file, which is used to test the fallback processing of try_key_ref.
  ↳ No PR: [dca637f](https://github.com/openssl/openssl/commit/dca637f50cf71372c46a9cf6022ad4eb9970ab7f)
- Added a DTLSv1_listen test to verify that the connection initiated through this function can complete the handshake; at the same time, the test auxiliary function was modified to support DTLSv1_listen mode and improve error handling.
  ↳ No PR: [26dad42](https://github.com/openssl/openssl/commit/26dad42e9ca609569073463165263173ab2a27ab)
- Added a new test case to verify the function of obtaining the public key in the Turkish environment.
  ↳ No PR: [c29cf39](https://github.com/openssl/openssl/commit/c29cf39449f78008e39af8f83760f2464815248b)
- Add a test for MAC reinitialization in evp_test to support verification of reinitialization failure through the NoReinit flag.
  ↳ No PR: [e58ba18](https://github.com/openssl/openssl/commit/e58ba181de6b0dfad0dc371f8d962c82138a906e)
- Added validation in tests that calling SipHash_Final in an uninitialized context should return failed validation.
  ↳ No PR: [4b694f2](https://github.com/openssl/openssl/commit/4b694f29ea78ab8a94e67c89d4d81df18c5e3bf1)
- Add test case to verify the behavior of calling EVP_PKEY_CTX_new_from_name without pre-initialization.
  ↳ No PR: [2d96bfd](https://github.com/openssl/openssl/commit/2d96bfd957149e491feba55a3d04afb26b2668b5)
- Fix memory leak when no-legacy is configured in test/provider_test.c.
  ↳ No PR: [49d874e](https://github.com/openssl/openssl/commit/49d874e0b7514cb270e817103ff0e13d4689e1f0)
- Improve the localization test and add skip processing when setting the locale fails.
  ↳ No PR: [93983e5](https://github.com/openssl/openssl/commit/93983e555531a8d9bf70d12e4cfdb5ce2f337e3b)
- Add test case for full validity of OSSL_PROVIDER_unload().
  ↳ No PR: [4b4d0de](https://github.com/openssl/openssl/commit/4b4d0ded6df357f76f580b7218abb3fe55f64463)
- Add test cases for query failure scenarios after adding a provider.
  ↳ No PR: [70dc0b6](https://github.com/openssl/openssl/commit/70dc0b6d27a11a7f64fe914a3f376988ad1b1720)
- Add test cases in the test configuration to verify the presence of the UnsafeLegacyServerConnect option.
  ↳ No PR: [abe9010](https://github.com/openssl/openssl/commit/abe90105ba0908d5a2f500997f2bf2fceb263acd)
- Added empty protocol test and handshake test for QUIC protocol.
  ↳ No PR: [e44795b](https://github.com/openssl/openssl/commit/e44795bd5db081260ef05c7be6fd17c080ed9437), [08e4901](https://github.com/openssl/openssl/commit/08e4901298df12931b45c7115254a0e159727683)
- Add test cases for the behavior of the read_ahead function in cross-key change scenarios.
  ↳ No PR: [f756534](https://github.com/openssl/openssl/commit/f7565348c22785f69239883feb1f3c91d1cfd675)
- Added test cases for default key length for Blowfish ciphers.
  ↳ No PR: [091e60c](https://github.com/openssl/openssl/commit/091e60c42c5d2a194936da7f4de3ce82527b27a3)
- Fixed API return value checking in multiple tests, using correct integer comparison macros instead of boolean assertions.
  ↳ No PR: [c2f7614](https://github.com/openssl/openssl/commit/c2f7614fb7b93fe3792068077ff01384f42f39bc), [d016758](https://github.com/openssl/openssl/commit/d016758706d0a7a104ff09db94448aeec1b38193), [bba14c6](https://github.com/openssl/openssl/commit/bba14c6e28e9519b2d40fc5c551893996f2db246), [babc818](https://github.com/openssl/openssl/commit/babc818c3f669214fa192229003953e3dead1926)
- Changed SCT issuer key to RSA 2048, removed SECLEVEL=1 setting which is no longer needed in test configuration.
  ↳ No PR: [479b9ad](https://github.com/openssl/openssl/commit/479b9adb88b9050186c1e9fc94879906f378b14b)
- Added test cases for PPC64 fixed-length Montgomery multiplicative regression problem.
  ↳ No PR: [14f9512](https://github.com/openssl/openssl/commit/14f95126c098358c434d59835834f9f0be7ea498)
- Added testing for overly large output buffers in PKEYKDF tests.
  ↳ No PR: [f68283c](https://github.com/openssl/openssl/commit/f68283c18eaf015e7500e59a6adf3dbb3ee74f59)
- Fixed the null pointer dereference problem in tests and added null pointer checking.
  ↳ No PR: [4f4942a](https://github.com/openssl/openssl/commit/4f4942a133bd57c4940fb1bc6ed7c8b67da4d8f0), [d768f85](https://github.com/openssl/openssl/commit/d768f853bb05b5a49a2aeb5b5702776834e68d06)
- Add test vectors for AES OCB for x86 AES-NI 96 byte multiples issue.
  ↳ No PR: [2f19ab1](https://github.com/openssl/openssl/commit/2f19ab18a29cf9c82cdd68bc8c7e5be5061b19be)
- Use TEST_true macro to wrap function calls in OCSP API tests to improve error reporting.
  ↳ No PR: [180c8d7](https://github.com/openssl/openssl/commit/180c8d7ae56378992b90ace9626d6df6ab1d4de8)
- Added tests for known DH primes to verify that the length of the generated private key does not exceed 225 bits.
  ↳ No PR: [2266d1c](https://github.com/openssl/openssl/commit/2266d1cad008ef03cb0791397b1cca9aaa6a4428)
- Added a new test case to verify the buffering processing when the first application data record arrives before Finished, and added a DTLSv1_listen connection test.
  ↳ No PR: [4000827](https://github.com/openssl/openssl/commit/4000827fdbf3f6d70949186fdd2bc57638500885)
- Add positive and negative test cases for EVP_PKEY_get1_encoded_public_key function.
  ↳ No PR: [3a1596f](https://github.com/openssl/openssl/commit/3a1596f4e3d710c163279a20e6b844d371886e73)
- Added verification that EVP_DigestSign sets the signature length correctly in EVP tests.
  ↳ No PR: [fc5888c](https://github.com/openssl/openssl/commit/fc5888ccb60f33b366972299f30b976c4dc12162)
- Fixed memory/resource leak issue in test files.
  ↳ No PR: [d272ef5](https://github.com/openssl/openssl/commit/d272ef5372a16924a5804b74a76491b1bc8529b5), [9690b97](https://github.com/openssl/openssl/commit/9690b9737d46cc52cc93682a63b110f5513e7671)
- Fixed an issue in sslapitest where the multiblock write test was always skipped due to incorrect parameters.
  ↳ No PR: [7c82a7a](https://github.com/openssl/openssl/commit/7c82a7a8f3a66f47f727d31691d6298d88ed158b)
- Add a test case for ticket key callback returning 0 in SSL test.
  ↳ No PR: [3b7a324](https://github.com/openssl/openssl/commit/3b7a3241c225b152ba8519f540bcac5b680312c2)
- Add API tests for TLSv1.3 record population.
  ↳ No PR: [f3f8e53](https://github.com/openssl/openssl/commit/f3f8e53c852f07d38c124e45f7c678e854be4a54)
- Fixed the problem of test failure on MinGW and changed the file opening mode to binary mode.
  ↳ No PR: [856f2aa](https://github.com/openssl/openssl/commit/856f2aa7be6bb59bc72493845d92e31ef0523c79)
- Add explicit null pointer checking in test functions to fix null pointer dereference issues reported by Coverity.
  ↳ No PR: [fbeb486](https://github.com/openssl/openssl/commit/fbeb4866f4250a4a23e7afb884a0aa0456d152f8), [82d46d1](https://github.com/openssl/openssl/commit/82d46d14462491681f25d016508715e85c1dc4d1)
- Fixed warnings about structure initialization syntax in older versions of clang compiler.
  ↳ No PR: [18274e1](https://github.com/openssl/openssl/commit/18274e1d6e10081fb7974e40f595e9a1d3224296)
- Fixed an issue where OPENSSL_USE_IPV6 was incorrectly used in testing, resulting in attempts to test IPv6 even after IPv6 was explicitly disabled.
  ↳ No PR: [ce41a53](https://github.com/openssl/openssl/commit/ce41a53dc647184119876fee53afef66be6c7f4b)
- Add FIPS version awareness to tests and refactor version checking functions.
  ↳ No PR: [eaac058](https://github.com/openssl/openssl/commit/eaac0584db6e7452fdb627502527fb0678bb9a93), [e1289d9](https://github.com/openssl/openssl/commit/e1289d90d0069ea1c3ea8ae80bfc3916077ec24e)
- Added FIPS version conditional judgment for EVP test and DES-EDE3-ECB test.
  ↳ No PR: [54a7bbe](https://github.com/openssl/openssl/commit/54a7bbedf43a1ade98c8f47eb8896d75f3db0165), [4d0249c](https://github.com/openssl/openssl/commit/4d0249c2d1d0f81c211354d8a36738595936fad8)
- Removed FIPS conditional compilation restrictions in SM2 tests and IV generation tests.
  ↳ No PR: [919adfc](https://github.com/openssl/openssl/commit/919adfcf6683d82f876060b6cf9f57e875d547b2), [3fd255a](https://github.com/openssl/openssl/commit/3fd255acb7b65a30afd1b23e17db2163fb9ffd8d)
- Change the use of FIPS RNG to runtime detection in the test, replacing compile-time conditional judgment.
  ↳ No PR: [c91f972](https://github.com/openssl/openssl/commit/c91f972c9fba61c5db761a49e13df4dadcba068a)
- Skip test/rsa_complex.c test on djgpp platform.
  ↳ No PR: [2de00f4](https://github.com/openssl/openssl/commit/2de00f4f1e20d3dd4cb8e3165f30146c1294f6d4)
- Add test cases for DH parameter generation and checking.
  ↳ No PR: [10119e7](https://github.com/openssl/openssl/commit/10119e7475bb198e13b1722b186303b8a7528dfe), [5e38e0a](https://github.com/openssl/openssl/commit/5e38e0acf4e1681ae32fa1b164adbc08719bd613)
- Fixed compilation warnings in test code, including static declaration issues in bio_comp_test.c and buffer length issues in packettest.c.
  ↳ No PR: [bb2bbd5](https://github.com/openssl/openssl/commit/bb2bbd53d49c510c2ae705d86e8fd2ed829cbd92), [91b7520](https://github.com/openssl/openssl/commit/91b7520e2385a513ad879dfa8fe8e45466315a27)
- Adjust QUIC test suite: remove RX unpacker standalone test, and temporarily disable front-end API tests.
  ↳ No PR: [6a80019](https://github.com/openssl/openssl/commit/6a8001986265ce9ce91469b6fa735cf95dd7b4bf), [b940f94](https://github.com/openssl/openssl/commit/b940f943a245ae5a5ea6f62417a21fe05933e973)
- Add custom EVP_CIPHER usage tests, including negative tests.
  ↳ No PR: [8c7d847](https://github.com/openssl/openssl/commit/8c7d847e2e6ac6bfded210c19fd8461254bb2be3)
- Replaced ECB cipher with CBC cipher in CMAC key generation test.
  ↳ No PR: [a0783b8](https://github.com/openssl/openssl/commit/a0783b83a3bd05a07ea64567995c7642621b4aa6)
- Added test files to verify X509 signature TBS cache regression issue.
  ↳ No PR: [29d4d8e](https://github.com/openssl/openssl/commit/29d4d8e80e72c458501888d41bdfa00f51914909)
- Added test cases for TLS pipelining functionality.
  ↳ No PR: [b718f6f](https://github.com/openssl/openssl/commit/b718f6fcc4bbf48cfc6ab3fa64e6cb95453299b3)
- Fixed an issue on macOS where thread cancellation could cause tests to hang, replacing lock-based blocking with infinite loop sleep.
  ↳ No PR: [6ca4bd2](https://github.com/openssl/openssl/commit/6ca4bd2e4c92531e74acba3e1ff08e6fbb664b20)
- Move the error queue cleaning operation from each test case to the test framework for unified execution.
  ↳ No PR: [d8eb0e1](https://github.com/openssl/openssl/commit/d8eb0e1988aba5d86aa6570357853cad0ab3f532)
- Add verification of actual buffer allocation and deallocation status in sslbuffertest.
  ↳ No PR: [ee05588](https://github.com/openssl/openssl/commit/ee05588dabeac7b9d034bf16dad122a93d1688a4)
- Fix potential null pointer reference in custom_params_test function in ectest.c.
  ↳ No PR: [15c8df8](https://github.com/openssl/openssl/commit/15c8df81083f31dd35aedbe2d58ec702d0c0dc65)
- Fix unused variables in QUIC send stream tests.
  ↳ No PR: [8f59328](https://github.com/openssl/openssl/commit/8f5932834c99c74dadc9ae23d89bfe0704b091de)
- Fixed the array length calculation method in the test code to avoid potential out-of-bounds memory access.
  ↳ No PR: [ce0a7ca](https://github.com/openssl/openssl/commit/ce0a7cadadb973216399e70d3a69f352b0843deb)
- Added two comparison options of less than and greater than or equal to the FIPS version test tool code.
  ↳ No PR: [fe84acc](https://github.com/openssl/openssl/commit/fe84acc22757e77d48fb6ccc31abe4c72264c877)
- Added test cases to verify that the IPAddressFamily_check_len function can correctly capture invalid lengths.
  ↳ No PR: [7489ada](https://github.com/openssl/openssl/commit/7489ada9f3fd902c5bc3c58cc03a90de2800d0ab)
- Split thread pool tests into independent files and add multiple thread-related test cases.
  ↳ No PR: [c48c328](https://github.com/openssl/openssl/commit/c48c32807f2d945a9672c48b59bff4083885a5bc)
- Add test case for RSA's implicit reject disable option.
  ↳ No PR: [455db0c](https://github.com/openssl/openssl/commit/455db0c94c0b83083ce8b792982c03aa56fc866f)
- Added basic echo server tests for QUIC test server.
  ↳ No PR: [f42781a](https://github.com/openssl/openssl/commit/f42781ad16598ed0d2d23ce8c67a6bea3d7fe0f0)
- Added test case for OSSL_CMP_CTX_get_status.
  ↳ No PR: [6ea44d0](https://github.com/openssl/openssl/commit/6ea44d07a7d0acb4af9eab15d9b4a76227f55f4e)
- Added QUIC client fuzzer.
  ↳ No PR: [ee7729e](https://github.com/openssl/openssl/commit/ee7729ed4cfcfb95a3fc0aaa184ed624f3fb7eaa)
- Added test cases for EVP_PKEY_Q_keygen.
  ↳ No PR: [667a850](https://github.com/openssl/openssl/commit/667a8501f0b6e5705fd611d5bb3ca24848b07154)
- Added SM4 XTS test cases.
  ↳ No PR: [6cdf83e](https://github.com/openssl/openssl/commit/6cdf83eaabda63f7c5cf9d69d51d931308da471e)
- Updated FIPS version checking logic to enhance robustness.
  ↳ No PR: [abff8bd](https://github.com/openssl/openssl/commit/abff8bd842b802c09b981b7552bd92ef1d0ced64)
- Added digest XOF length support to evp_test.
  ↳ No PR: [c8ebdd6](https://github.com/openssl/openssl/commit/c8ebdd6a85a0cefe5542dba41180571fa5f198a0)
- Added QUIC fault injection test framework, supports fault injection into plaintext and encrypted data packets, and added unknown frame processing tests.
  ↳ No PR: [adef87a](https://github.com/openssl/openssl/commit/adef87a2c6a0136aa3d965162932f961daf28411), [2f1d8f8](https://github.com/openssl/openssl/commit/2f1d8f858decda2d604abf3347c8e17237f90387), [71587f2](https://github.com/openssl/openssl/commit/71587f2b6a711bc8cd18521575910291f637dfcf), [de60deb](https://github.com/openssl/openssl/commit/de60deb258c4b52502da372a61344b83428fc970)
- Fixed compilation problem of timing_load_creds tool on platforms missing timersub macro, and added POSIX version check.
  ↳ No PR: [f2e4629](https://github.com/openssl/openssl/commit/f2e4629608c3a2f5d93a91ef95abc25726eec44c), [adf289b](https://github.com/openssl/openssl/commit/adf289b5b67ecb414ab709a2c25b0c6f0d463d31)
- Added new test cases for QUIC receive stream, covering simple and random data scenarios.
  ↳ No PR: [330ce4a](https://github.com/openssl/openssl/commit/330ce4a39bd6d0c1fd5ba7426574fb1f36cef961)
- Added new interfaces to QUIC test server and adjusted function signatures to support more test scenarios.
  ↳ No PR: [f10e588](https://github.com/openssl/openssl/commit/f10e5885f01582c449eff8df70b61c916d9224cf)
- Fixed SM4-CBC decryption regression on Armv8 and added test cases.
  ↳ No PR: [d89e036](https://github.com/openssl/openssl/commit/d89e0361d5ff5b32c24edac6c60c5ae38714e6c3)
- Fixed compilation errors caused by unused test functions when FUZZING_BUILD_MODE is enabled.
  ↳ No PR: [97446da](https://github.com/openssl/openssl/commit/97446da7e05bd7164f5c36b68b8bef13a63e06a5)
- Expanded test header file comments and fixed typos.
  ↳ No PR: [da81f1e](https://github.com/openssl/openssl/commit/da81f1e563c80a1d4ab82e545f3f5ba6e715267e)
- Fixed compatibility of merged CI with old FIPS provider, updated test data version conditions.
  ↳ No PR: [dc45d4c](https://github.com/openssl/openssl/commit/dc45d4c6faeb53bb68401141d899b9f857bbc51d)
- Added testing of stream end conditions during reading and writing in the QUIC test server.
  ↳ No PR: [c0f6940](https://github.com/openssl/openssl/commit/c0f694039a863a7f8999695e30fd93de23c9ae43)
- Added a new test case for CVE-2022-4450 to verify that PEM_read_bio_ex returns failure and there is no memory leak under empty payload.
  ↳ No PR: [dc341a4](https://github.com/openssl/openssl/commit/dc341a46677fe19f055bd2eea0e3a2af21053903)
- Add test cases for OSSL_trace_set_callback() and extend trace tests to cover OSSL_TRACE_CATEGORY_TRACE category.
  ↳ No PR: [e64a169](https://github.com/openssl/openssl/commit/e64a169fc678b5e57db28d06c25020d69bc61e4c)
- Fix the logic flaw in the test_mod_exp_zero test to ensure that test failures can be captured correctly.
  ↳ No PR: [4206126](https://github.com/openssl/openssl/commit/42061268ee8f9ae0555d522870740fc91b744f4f)
- Updated the X509 fuzzer to support certificate chain verification, including CA signature verification, CRL and OCSP status checks.
  ↳ No PR: [399c2da](https://github.com/openssl/openssl/commit/399c2da08ab9c6a382f8e9950742a022e847fec0)
- Fixed non-deterministic failure in QUIC test server caused by differences in network stack timing between different operating systems, allowing errors to be waited for while reading rather than asserted immediately.
  ↳ No PR: [c8e7f84](https://github.com/openssl/openssl/commit/c8e7f842b002f6c5081ff1519a9fe40d81cdeadd)
- Add a test case for zero value BIGNUM as the only parameter in the parameter construction test, and add the corresponding single zero value test function.
  ↳ No PR: [b49cf27](https://github.com/openssl/openssl/commit/b49cf273883c8d3f47542941fe5cc6cb51aec9c9)
- Added test cases for damaged encrypted packets and datagrams.
  ↳ No PR: [be5b3b3](https://github.com/openssl/openssl/commit/be5b3b3787271d6b9057639ce42145fc66c11732)
- Added the function of monitoring datagrams, including setting datagram listener callbacks and adjusting datagram size, and added corresponding test auxiliary functions.
  ↳ No PR: [e4cb658](https://github.com/openssl/openssl/commit/e4cb6583efa11decfa8d4d539c6cc2f08c99a067)
- Extended QUIC corruption testing, added datagram truncation test cases, and refactored test helper functions to support simulation time.
  ↳ No PR: [6a9ab9b](https://github.com/openssl/openssl/commit/6a9ab9bc6879b11110183704ca6364bafe794764)
- Added a new test auxiliary function qtest_check_server_transport_err, which is used to verify whether the server receives the specified transmission error code, and reconstructed the original protocol error checking function to use this new function.
  ↳ No PR: [c88de56](https://github.com/openssl/openssl/commit/c88de5607829f8d98427ba3fa3d465c4e66e07fb)
- Add tests for the public variant of bn2bin(), covering length 1, 0 and NULL input cases.
  ↳ No PR: [1519233](https://github.com/openssl/openssl/commit/15192335c8bbfb78bc02086bcd77a0d82efffbce)
- Add negative test cases for unquoted attributed strings.
  ↳ No PR: [543ac2f](https://github.com/openssl/openssl/commit/543ac2f0191f10d8a3774727fa691543de8b15bb)
- Prevent the use of SSL_dup in QUIC SSL, and add a test to ensure that a null pointer is returned.
  ↳ No PR: [764817c](https://github.com/openssl/openssl/commit/764817c4aa1b7f9aa188cab0d3b2033e08025c73)
- Added a new auxiliary function in the test, used to add a frame to the front of the data packet.
  ↳ No PR: [7eaaaaa](https://github.com/openssl/openssl/commit/7eaaaaaa559d56edc9732d768dc374a4f829b187)
- Add test cases for functionality of sending maximum amount of application data.
  ↳ No PR: [3ff0a48](https://github.com/openssl/openssl/commit/3ff0a48af4135feeae83f8888fac88298f55d921)
- Added DTLS protocol support for large application data testing.
  ↳ No PR: [2fda45d](https://github.com/openssl/openssl/commit/2fda45d5eb85e5d939fbbba0dd6562ebf01abd2a)
- Fixed a possible null pointer dereference problem in tests caused by not checking pointer validity.
  ↳ No PR: [00407fb](https://github.com/openssl/openssl/commit/00407fbf0b25d65f5e6d99defdb081432e810449)
- Fix missing error checking in test code to ensure resources are released and returned correctly when ASN1_INTEGER_set fails.
  ↳ No PR: [a4347a9](https://github.com/openssl/openssl/commit/a4347a9a57dcb985283bba03dd3b16294b55945b)
- Add test cases validating the default cipher suite list in QUIC tests.
  ↳ No PR: [0c9646e](https://github.com/openssl/openssl/commit/0c9646ec373e7f3f9b07f218a348ecb82219eaa7)
- Fixed an issue where the test_get_libctx function may crash when the provider parameter is NULL.
  ↳ No PR: [13cb541](https://github.com/openssl/openssl/commit/13cb5416f4dbbf50690fe129894e2856623af21c)
- Add test cases for server return errors for CMP client testing, and refactor the mock server and test framework.
  ↳ No PR: [6f88876](https://github.com/openssl/openssl/commit/6f88876d4ea66d1f0b9217fec18b9dcc760a451a)
- Add error path coverage test for ossl_rsa_sp800_56b_derive_params_from_pq function, and optimize the assertion method.
  ↳ No PR: [b1ce6a2](https://github.com/openssl/openssl/commit/b1ce6a23f8f61cc2f2f48368a97493498c026aa7)
- Add test cases for RSA_sign_ASN1_OCTET_STRING and RSA_verify_ASN1_OCTET_STRING.
  ↳ No PR: [416a928](https://github.com/openssl/openssl/commit/416a9286859d444e5a77bbdcc73f0c35b34e574b)
- Add fuzzer for SMIME.
  ↳ No PR: [359d6a2](https://github.com/openssl/openssl/commit/359d6a26d64c32e7c2bebf5655c70c074f6c805b)
- Added a new test case to verify that the default configuration file will not be initialized when using custom libctx.
  ↳ No PR: [0aa7d7f](https://github.com/openssl/openssl/commit/0aa7d7f42bc757a0993739b6cfdc8819a70d22ef)
- Add mutex support for QUIC test server.
  ↳ No PR: [e053505](https://github.com/openssl/openssl/commit/e053505f0ce1a6d15cbcd42e49dabc844610b65a)
- Added and enhanced tests for QUIC thread assist mode, refactored test functions to support thread assist and injection mode combinations.
  ↳ No PR: [3b1ab5a](https://github.com/openssl/openssl/commit/3b1ab5a3a0a10798ea9a1547b6cb50182edaeb5b), [bbc646e](https://github.com/openssl/openssl/commit/bbc646e91a2fccf45b0cd2030b2de7f0ef828c58)
- Fix the race condition of multi-threaded access to fake_time in the test code, and add read-write lock protection.
  ↳ No PR: [99ed85b](https://github.com/openssl/openssl/commit/99ed85bba9de5d9983d3796c18e62041d3ce6575)
- Artificially added non-zero times for tickets in early data tests to expose potential issues in age calculations.
  ↳ No PR: [2be5065](https://github.com/openssl/openssl/commit/2be5065b0a5a4bfab7424fd8de07b62441be6468)
- Add tests for spurious errors that may remain on the error stack after rejecting earlier data.
  ↳ No PR: [1083692](https://github.com/openssl/openssl/commit/10836921e52ff9110c12b4b9f984e7c5ef1c89cc)
- Added test support for final empty frame in QUIC stream reception test.
  ↳ No PR: [7fa2160](https://github.com/openssl/openssl/commit/7fa216095a7ebcfa8fbf9f6143b0fb336e77c964)
- Added tests for context replication failure scenarios, verifying that the first operation completes successfully and subsequent operations return errors.
  ↳ No PR: [f3c0dd4](https://github.com/openssl/openssl/commit/f3c0dd4f0cd3bc282575a98181f8190d81189a78)
- In the BIO_dgram test, skip the test when BIO_bind() fails, to accommodate platforms that do not support a specific address family.
  ↳ No PR: [12c4e67](https://github.com/openssl/openssl/commit/12c4e67675e691d7556a526aa062effff05a6532)
- Add test cases for the QUIC datagram injection API, extending the existing test framework to cover injection modes.
  ↳ No PR: [3cc376c](https://github.com/openssl/openssl/commit/3cc376c91e0e9d55fd3903f203dc38d0a5788380)
- Added blocking mode support for QUIC tests, refactored test helper functions to support UDP sockets and blocking waits.
  ↳ No PR: [0c59332](https://github.com/openssl/openssl/commit/0c593328fe811583da68d25b0c8bf87ba842acbb)
- Added interoperability test with Cloudflare quiche, and adjusted timeout and event handling functions.
  ↳ No PR: [fc11028](https://github.com/openssl/openssl/commit/fc11028089c374bb24655895c90eaf069c3cee6f)
- Add a sanity test for OSSL_sleep() to verify whether its sleep duration is within a reasonable range.
  ↳ No PR: [6821acb](https://github.com/openssl/openssl/commit/6821acbffda908ec69769ed7f110cfde57d8ca58)
- Added test for reading EC public key affine coordinates for EVP extra tests, with support for legacy keys.
  ↳ No PR: [1ffb6e1](https://github.com/openssl/openssl/commit/1ffb6e19eeee95784456831da329cbccaa59fbcf)
- Fixed possible failures in QUIC tests due to empty read data, adding a loop to wait until data is received.
  ↳ No PR: [54b86b7](https://github.com/openssl/openssl/commit/54b86b7fa313789e7cc79317c692410c8f336660)
- Added test cases for DTLS that apply data records appearing before epoch changes.
  ↳ No PR: [8189fe2](https://github.com/openssl/openssl/commit/8189fe242bba319dfccd8805fd7703d973bf9649)
- Expanded min/max protocol testing, adding test cases for DTLS and QUIC protocols.
  ↳ No PR: [f612673](https://github.com/openssl/openssl/commit/f612673049b93387eb7f93c207aca821496da861)
- Added provider uninstall call in cleanup function of cmp_ test.
  ↳ No PR: [8835940](https://github.com/openssl/openssl/commit/8835940db58229fc467cdea1eebf3f064352a086)
- Updated evprand test data to add FIPS version constraints for each test case.
  ↳ No PR: [cf3d5c2](https://github.com/openssl/openssl/commit/cf3d5c2fbaf734731b1ccbd3a84e21eeb6d0f30d)
- Updated TLS PRF testing, adding FIPS version restrictions to comply with strict FIPS policies.
  ↳ No PR: [e079993](https://github.com/openssl/openssl/commit/e07999369a13a29243f34cbd5d24281783984299)
- Added release handling of FIPS version field in SSL test context to support test condition checking based on OpenSSL version.
  ↳ No PR: [4454c20](https://github.com/openssl/openssl/commit/4454c20f026bb47f158ea05c207f143c81d674d8)
- Fix how streams are used in QUIC failure tests to ensure tests create and use new streams correctly.
  ↳ No PR: [9caf981](https://github.com/openssl/openssl/commit/9caf981237c3e655c18ebef7193153238f2855db)
- To fix the AES-XTS bug in aarch64 big-endian environment, test cases covering the assembly code branch have been added.
  ↳ No PR: [4df13d1](https://github.com/openssl/openssl/commit/4df13d1054e143f1cbf13fa347491807289f87b7)
- Cleaned up the usage of WPACKET in quic_txp_test.c, optimized the error handling path and resource release logic.
  ↳ No PR: [dbca844](https://github.com/openssl/openssl/commit/dbca844cb3e74b19acf46eb9a2222d30802ad642)
- Fix the constraint that the sequence number of the NEW_CONNECTION_ID frame in the test case must be greater than or equal to the pre-retirement sequence, and add a new negative test case that violates this constraint.
  ↳ No PR: [c301149](https://github.com/openssl/openssl/commit/c301149ad43ee2c611e7b8d4f2826f524f3385aa)
- Added tests for new QUIC tracing capabilities.
  ↳ No PR: [2e1da96](https://github.com/openssl/openssl/commit/2e1da9693a7de72643acdf3da4816c4edf96ca29)
- Updated SSL_tick calls in QUIC test code to SSL_handle_events.
  ↳ No PR: [041d48c](https://github.com/openssl/openssl/commit/041d48c9636478563b5dcd936c1fe816d1628732)
- Make the testutil text output function thread-safe, and add read-write locks to protect all output operations.
  ↳ No PR: [2fa9044](https://github.com/openssl/openssl/commit/2fa90442984349b41401e008df26ee707b6c851d)
- Added test cases for SM4-CBC in the CMAC test, and added test cases for AES-128-CBC, AES-192-CBC, AES-256-CBC and DES-EDE3-CBC with data lengths exceeding four block lengths.
  ↳ No PR: [fd54fad](https://github.com/openssl/openssl/commit/fd54fadba6bc138fb35a82c033c540f7e97322c8)
- Added time skipping mechanism and test scripts for QUIC key update tests, and extended test harness macros to support int64_t comparisons.
  ↳ No PR: [693b23e](https://github.com/openssl/openssl/commit/693b23e3d07813985de510a00b1db58070439a51)
- Add test cases for OSSL_ERR_STATE_save/restore functionality.
  ↳ No PR: [ff0de16](https://github.com/openssl/openssl/commit/ff0de1637b5e25719a976c85f969598086d80358)
- Added QUIC frame processing consistency tests, including fault injection tests and dynamic frame type tests, and optimized the test framework to support the injector.
  ↳ No PR: [e26dc8e](https://github.com/openssl/openssl/commit/e26dc8e3d54a414ba9dc85f54e13112617e32556)
- Added FIPS version restriction for KDF connection test, only supports FIPS provider 3.2.0 and above.
  ↳ No PR: [45fefe1](https://github.com/openssl/openssl/commit/45fefe172aa630686561e5a3cfcb25262db23edc)
- Check the return value of sscanf() and adjust the test initialization logic.
  ↳ No PR: [a3fcafb](https://github.com/openssl/openssl/commit/a3fcafb34994c4864d8dc92a88f9d8e354230d12)
- Updated and fixed CMAC test cases, including using short string padding instead, optimizing comments, adding conditional compilation protection, and fixing build failure when DES or SM4 is disabled and using the OSSL_NELEM macro instead.
  ↳ No PR: [e8dc77f](https://github.com/openssl/openssl/commit/e8dc77f85f251752258203cf9cbfa077fd8b3173), [fbff5b5](https://github.com/openssl/openssl/commit/fbff5b57715471910ea99d28f03ba6a417b45135)
- Skip or disable QUIC SSL trace testing based on compilation configuration conditions (specific options, no-ecx, DH disabled) to avoid test failure due to option interference.
  ↳ No PR: [1be2ee6](https://github.com/openssl/openssl/commit/1be2ee683c3cbd8690728a05e05b778d5f7674b8), [47ef3b9](https://github.com/openssl/openssl/commit/47ef3b9fc03c92f6a387927f1b8b0fe1014eb646), [61cc84d](https://github.com/openssl/openssl/commit/61cc84d9f9d8ad3f918d5bd908096d39b72c3969)
- Fixed the random failure of QUIC multi-stream test script 19, added interactive steps, adjusted the operation sequence and check conditions, and optimized the timeout parameters.
  ↳ No PR: [9289e59](https://github.com/openssl/openssl/commit/9289e59c9581d76f2c3e570d3d8eed6aea598bb8), [76696a5](https://github.com/openssl/openssl/commit/76696a5413db0a93e374f9f0f55e5694f93ecc0e), [de9564b](https://github.com/openssl/openssl/commit/de9564bdd72142ab9353f84cc2f186ad559a8eed)
- Fix multistream test script 18, adjust timeout waiting time parameters.
  ↳ No PR: [0e1da9d](https://github.com/openssl/openssl/commit/0e1da9d7ec3c7dd2af49be0d9be3e0848c167608)
- Fix bugs in QUIC multi-stream testing, adjust stream types and operation sequences in test scripts.
  ↳ No PR: [70cafc4](https://github.com/openssl/openssl/commit/70cafc4479e7faf005068580d0354d5ab1c8c0d4)
- Fixed error handling related to WPACKET usage in QUIC tests to ensure that resources are released correctly.
  ↳ No PR: [7eebc35](https://github.com/openssl/openssl/commit/7eebc3546fa5738a807722345006fe97fcad3013)
- Corrected type conversion and conditional judgment logic in QUIC minimum frame encoding test.
  ↳ No PR: [49a38de](https://github.com/openssl/openssl/commit/49a38dee0d65c6fb7ddcf9dbf76e9afa0ed3c776)
- Fixed comparison issues caused by type mismatch in test code.
  ↳ No PR: [709ef40](https://github.com/openssl/openssl/commit/709ef4093520a91f4d723aef29c857c6fd625cad)
- Fix the condition of the blocking mode flag in QUIC test cases to ensure that test 2 runs correctly in blocking mode.
  ↳ No PR: [ff9728c](https://github.com/openssl/openssl/commit/ff9728c6d5d23ebaa73cb729c8110c0582e66280)
- Added QUIC SSL BIO test, and adjusted test registration and conditional compilation.
  ↳ No PR: [0a3733b](https://github.com/openssl/openssl/commit/0a3733babbbb4e297ccfbc3ece29e95cafca5f2d)
- Add new test cases for ffdhe group, update test configuration and add key type processing logic.
  ↳ No PR: [2c59d54](https://github.com/openssl/openssl/commit/2c59d54cd7cb741c4547311ca1b8479e08dce0b7)
- Add new object identifier entry to OID list for fuzz testing.
  ↳ No PR: [58cd83f](https://github.com/openssl/openssl/commit/58cd83f83cb0fb4c0eaf97aef1c65996c0936a7d)
- Added test cases for AES-SIV with empty associated data entries.
  ↳ No PR: [3993bb0](https://github.com/openssl/openssl/commit/3993bb0c0c87e3ed0ab4274e4688aa814e164cfc)
- Update reference counting implementation in tests to use struct-based atomic operations instead.
  ↳ No PR: [59a9670](https://github.com/openssl/openssl/commit/59a967030ec1cccf6eb4031a4531c8f555a393ec)
- Added packet size boundary test cases for QUIC TXP tests.
  ↳ No PR: [d49c6ca](https://github.com/openssl/openssl/commit/d49c6ca7b95902655e200b34876d5ad965428722)
- Added a test case for multi-threaded loading of PEM files to verify the correctness of the lock mechanism.
  ↳ No PR: [29f25a1](https://github.com/openssl/openssl/commit/29f25a10e505d7b5cabadf457a1be7a5c75a8b80)
- Add handshake retry test function and refactor test code to support configurable retry error values.
  ↳ No PR: [149c4f9](https://github.com/openssl/openssl/commit/149c4f98168ba19432986e82d30d15bd41bae475)
- Update QUIC TXP test, remove archetype parameter.
  ↳ No PR: [9441624](https://github.com/openssl/openssl/commit/9441624ee91705bf9f7a35ba06ec336a9d63868e)
- Corrected script references in test files and added test scripts.
  ↳ No PR: [8aa6a43](https://github.com/openssl/openssl/commit/8aa6a436dce7c8139909d9a694c6ce2afea4e416)
- Added command line options to evp_test to support in-place and both-mode password testing.
  ↳ No PR: [d57d0b8](https://github.com/openssl/openssl/commit/d57d0b818935c20a7b468c0e717773ea8a3373e6)
- Change TODO comments in QUIC failure tests to normal comments and adjust function visibility.
  ↳ No PR: [40e2857](https://github.com/openssl/openssl/commit/40e28577dd81d1b3e775240c4815ebce5d56f868)
- Allows suppressing the tick operation of the QUIC channel, and adds a function to set the suppression flag.
  ↳ No PR: [03b3859](https://github.com/openssl/openssl/commit/03b3859501b69d48c8710b6a0754842c7166a7c1)
- QUIC test server allows reading from the stream after the connection has been terminated, and adds connection liveness checks.
  ↳ No PR: [5904a0a](https://github.com/openssl/openssl/commit/5904a0a71f5730c2f1e3028e092ea986b603081d)
- Improve the failure log of QUIC multi-stream test, output the script name for easy location.
  ↳ No PR: [0786483](https://github.com/openssl/openssl/commit/0786483adffec3ce0f2e77133388b7f119df4975)
- Added shutdown flush test case for QUIC multi-stream test, and expanded the test script opcode.
  ↳ No PR: [cd5e438](https://github.com/openssl/openssl/commit/cd5e438065a8de960b2581db9ba5a18e406d187e)
- Add additional tests for QUIC TXP to verify the interaction and padding boundaries of multiple packets in the same datagram.
  ↳ No PR: [833840b](https://github.com/openssl/openssl/commit/833840be9784205691105e197d71529ed0ddfdc4)
- Add test cases for decoding using 0 selection in endecode_test.c.
  ↳ No PR: [4c50610](https://github.com/openssl/openssl/commit/4c50610bdadbcf7aa6bbd968df67b8874234677b)
- Added QUIC conformance test to verify that CRYPTO frames with illegal offset and length are correctly rejected.
  ↳ No PR: [27c2f62](https://github.com/openssl/openssl/commit/27c2f62f96287d7bbe2aade5fc3e3c86e88c4496)
- Added a check for the q = p + 1 scenario in the DH test, and the verification returns DH_CHECK_INVALID_Q_VALUE.
  ↳ No PR: [ad5d355](https://github.com/openssl/openssl/commit/ad5d35572695d7b5748b2bd4fb1afaa189b29e28)
- Added fault injection script for QUIC tests to ensure that fake BLOCKED frames are ignored.
  ↳ No PR: [477944b](https://github.com/openssl/openssl/commit/477944b67b26287e1eee0d315f52c5761c71ef84)
- Add PADDING frame fault injection function to QUIC test, and improve the injection function's check of packet type.
  ↳ No PR: [97684a1](https://github.com/openssl/openssl/commit/97684a1517ec07300cb87cebe107fa7a709a04ba)
- Added fault injection tests for QUIC multi-stream testing to ensure PATH_RESPONSE frames are ignored.
  ↳ No PR: [a1aff2c](https://github.com/openssl/openssl/commit/a1aff2c63f84ddfdb656302653a29aa5035d7275)
- Added connection closing reason test support to the QUIC test framework, and added test cases to verify the closing reason truncation behavior.
  ↳ No PR: [d49a163](https://github.com/openssl/openssl/commit/d49a1634f4efd21807c5c785d2b0d6ef8683e91d)
- Added a fault injection test case for repeated HANDSHAKE_DONE frames in the QUIC test, and added a connection closure reason truncation test.
  ↳ No PR: [d56b81a](https://github.com/openssl/openssl/commit/d56b81ac9f02dd55ecf3281d16fdb156897b4d8d)
- Added test cases for ACK frame generation for QUIC protocol, including fault injection scenarios.
  ↳ No PR: [ed0d6ba](https://github.com/openssl/openssl/commit/ed0d6ba4589acc4da38c4197910aed9705eba5e1)
- Re-enable unexpectedly disabled index 18 tests in QUIC TXP tests, and fix test initialization to allow 1-RTT processing.
  ↳ No PR: [ec2b45f](https://github.com/openssl/openssl/commit/ec2b45f59bda565bc1b8525ab8d508325dc612de)
- Fixed the loop variable and parameter passing in the QUIC flow test function to ensure that the test case is fully executed.
  ↳ No PR: [839f6ac](https://github.com/openssl/openssl/commit/839f6ac32f844164dcb965f4ee429188f0bf141f)
- Add non-null check for stream_name in QUIC multi-stream test, fix potential null pointer dereference found by Coverity.
  ↳ No PR: [dbf247a](https://github.com/openssl/openssl/commit/dbf247ad1dd0fc4c7b365593a9a5c69fc94a3732)
- Fixed the problem of uninitialized variables found by Coverity scan in QUIC FC test, and added connection initialization status check.
  ↳ No PR: [451055d](https://github.com/openssl/openssl/commit/451055d2882eb81c8d620eb7736a4c1236e30935)
- Fixed memory leak in QUIC congestion control test and added error handling path in net_sim_send function.
  ↳ No PR: [3887546](https://github.com/openssl/openssl/commit/3887546dcf98f1369d5a03eae9772a7deb0c9b89)
- Fixed repeated closing issue in QUIC test due to file descriptor not being reset.
  ↳ No PR: [410a90f](https://github.com/openssl/openssl/commit/410a90f598a77546b847ba28b4bd8559ac57ab31)
- Allow setup_tests to not print help information when it returns failure, and control the help output by distinguishing the return value.
  ↳ No PR: [badf3c1](https://github.com/openssl/openssl/commit/badf3c162d2b67635beee3fc948db32f13d274af)
- Manually load and unload legacy and default providers in PBE tests when autoloading configuration is turned off.
  ↳ No PR: [52ea255](https://github.com/openssl/openssl/commit/52ea255d9d560513f69c3f7f3f21513a693c865c)
- Skip configuration-based test cases when the configuration is not loaded.
  ↳ No PR: [a9dde74](https://github.com/openssl/openssl/commit/a9dde749504065e6e66b63cc12c25381465ec721)
- In QUIC tests, ensure that both client and server are running during the connection and clean up unused variables.
  ↳ No PR: [608a95f](https://github.com/openssl/openssl/commit/608a95f4969202083eccd4c1c7e91dec021ea79b)
- Add version negotiation test for QUIC.
  ↳ No PR: [69169cd](https://github.com/openssl/openssl/commit/69169cd9faf68e6d8fb83895233c184543151168)
- In QUIC tests, make both client and server use fake time, and make sure the fake time is non-zero; also have the test_ssl_trace test enable the fake time flag.
  ↳ No PR: [617cab0](https://github.com/openssl/openssl/commit/617cab094f0f0d4e71f8b9da5663be8ab06cba92)
- Added a new test case to verify that the thread blocked in SSL_read_ex will be awakened when receiving FIN.
  ↳ No PR: [0fa6612](https://github.com/openssl/openssl/commit/0fa6612ed69411ddbfca9e7a2e28e263b7b6d346)
- Add a new test case to verify that multiple datagrams are sent at once when the data is sufficient, and adjust related test functions.
  ↳ No PR: [8c5284f](https://github.com/openssl/openssl/commit/8c5284ff194f444877ae25012d3d07ee46e46219)
- Added new stream creation backpressure test in QUIC multi-stream test, and fixed packet type checking in injection function.
  ↳ No PR: [14551f1](https://github.com/openssl/openssl/commit/14551f1effa80a773e029d4ae6cb7657eef74bc2)
- Added WAIT_PEER test case for QUIC multi-stream testing, and adjusted related auxiliary functions.
  ↳ No PR: [3bc38ba](https://github.com/openssl/openssl/commit/3bc38ba0712283bbbd57994af0259791dc42e704)
- Added blocking and non-blocking mode support for QUIC multi-stream testing, and added multiple test scripts.
  ↳ No PR: [5881dd2](https://github.com/openssl/openssl/commit/5881dd2c080c10ab9f9ca38a2db64deaa79f853a)
- Fix the synchronization problem of script_20 in QUIC multi-stream test, add mutex lock and condition variable, and adjust the script logic to correctly synchronize threads.
  ↳ No PR: [99d6b9f](https://github.com/openssl/openssl/commit/99d6b9f9e2fbf272160a07bed5f4ab7ce2b3e20e)
- Increase timeout for QUIC client tests to resolve timeout issues in Coveralls CI.
  ↳ No PR: [0f9caad](https://github.com/openssl/openssl/commit/0f9caad5b95e901b87fe45cf85c9582071ca0b23)
- Add test cases for Store deletion API, including test_pkey_delete.
  ↳ No PR: [b8aca10](https://github.com/openssl/openssl/commit/b8aca10d8efac1611cfcb739202c34da39f7e3d0)
- Treat the failure to copy the password as an error in the test, and make conditional judgments based on the FIPS provider version.
  ↳ No PR: [39d857b](https://github.com/openssl/openssl/commit/39d857bb610d25b3de4e414264246ec41753c446)
- Adjusted spin behavior in QUIC multi-stream testing, split spin logic into common macros and added server tick calls.
  ↳ No PR: [769c9b1](https://github.com/openssl/openssl/commit/769c9b1a99b4bb7878a7b4d031d928376de1b8c3)
- Add missing call failure check in the test_provider_ex test function to improve the error handling path.
  ↳ No PR: [50b3c47](https://github.com/openssl/openssl/commit/50b3c47b65e47a4f52ed1c47a0f248beb890193e)
- Added consistency check in QUIC multi-stream test to ensure that SSL_want return value matches SSL_get_error error code.
  ↳ No PR: [9ff8161](https://github.com/openssl/openssl/commit/9ff816106c2b2ccbffe5c4e3619a840547088674)
- Add tests for QUIC connections to verify correct handling of non-IO retry errors (such as SSL_ERROR_WANT_RETRY_VERIFY).
  ↳ No PR: [48724e8](https://github.com/openssl/openssl/commit/48724e8a205c732705c3f54a3bd43d7049e77774)
- Add test case supporting NULL BIGNUM parameter for OSSL_PARAM_BLD_push_BN.
  ↳ No PR: [a535e5b](https://github.com/openssl/openssl/commit/a535e5b73fc374dbbef54d2629728e9602ecf6be)
- Replaced the CPUID_OBJ macro with OPENSSL_CPUID_OBJ in chacha internal tests to fix compilation issues.
  ↳ No PR: [e6b6b18](https://github.com/openssl/openssl/commit/e6b6b18af3e85a6b5f0d8ea1070f7070557d6357)
- Fixed the problem of hardcoding the server port in the test_quic_multistream test, and changed the port to dynamic allocation to support concurrent running.
  ↳ No PR: [84f371a](https://github.com/openssl/openssl/commit/84f371a130dbe7a46595fbabd274f152a0e6385f)
- Add test cases for SSL_CIPHER_find for QUIC SSL objects.
  ↳ No PR: [9912dfb](https://github.com/openssl/openssl/commit/9912dfb98c9c2b10c83c5ca4b5136232568ad664)
- Added command line option to evp_test to set propquery and pass this option in multiple test initialization functions.
  ↳ No PR: [f34878d](https://github.com/openssl/openssl/commit/f34878d846de43a6f760e506f440b5fef85afba6)
- Fixed a small bug in QUIC multi-stream testing.
  ↳ No PR: [e501e8b](https://github.com/openssl/openssl/commit/e501e8b606a2398d9b860eb10344113e9d1d375b)
- Added verification of handling of ALPN extensions not sent by the server in QUIC tests to ensure that this situation is correctly treated as an error.
  ↳ No PR: [d012319](https://github.com/openssl/openssl/commit/d012319145b1c95ecb9ada29f4f03a3b30cf0f41)
- Fixed a memory leak in ssl_old_test.c caused by SSL_CTX_set0_tmp_dh_pkey failure, releasing the temporary DH key object when the call fails.
  ↳ No PR: [21f0b80](https://github.com/openssl/openssl/commit/21f0b80cd4b32ba80843b812b01a6056daf14093)
- Increase the reference count of sbio before passing it to tserver, and fix the way fisbio is released.
  ↳ No PR: [f13f9b7](https://github.com/openssl/openssl/commit/f13f9b716e8b148b97dbe49e823b9dc3f235de1f)
- Adjust the FIPS version check conditions of cipher dupctx in evp_test to simplify the version judgment logic.
  ↳ No PR: [1a18596](https://github.com/openssl/openssl/commit/1a18596149a325a679f8244bac52b6796dfcc48e)
- Added regression test for signing using legacy application method keys in evp_extra test.
  ↳ No PR: [860e36d](https://github.com/openssl/openssl/commit/860e36d0dd72f4aa4791e88aa185cb42065a30c4)
- Fix no-ssl-trace problem, add OPENSSL_NO_SSL_TRACE conditional compilation protection in test auxiliary code.
  ↳ No PR: [7f5b29c](https://github.com/openssl/openssl/commit/7f5b29c4bf909964f1a73d80af1474f0e4a95624)
- Added client certificate authentication test case for QUIC test, including loading related configurations of client certificate and CA certificate.
  ↳ No PR: [9f6eb62](https://github.com/openssl/openssl/commit/9f6eb62221358fe84b3d70e63378ae651bbc9705)
- Optimize the idle loop in QUIC tests to avoid unnecessary waiting and fix timeout hang issues.
  ↳ No PR: [2e62b07](https://github.com/openssl/openssl/commit/2e62b07a41cca299f7abb69c892053b99ec762b2), [79997a9](https://github.com/openssl/openssl/commit/79997a919f6cf3823d04fa9b34adaaa5aadd871a)
- Enhance QUIC fuzz testing capabilities, including skipping encryption and decryption, handling retry errors, relaxing transmission parameter checks and introducing time control.
  ↳ No PR: [5415383](https://github.com/openssl/openssl/commit/5415383d2c7e8ee8147eb01361f3f952ceec3761), [acee7d6](https://github.com/openssl/openssl/commit/acee7d68e1037d18f34d03bcd70af6b1b6e48299), [b62ac1a](https://github.com/openssl/openssl/commit/b62ac1abfcac4091cdf8e5e4194c9e3bcc6d382d), [9252efd](https://github.com/openssl/openssl/commit/9252efdb8d1b21ef05aedef2cc40eee46dd72b96)
- Fixed buffer overflow issue in BIO address test and renamed variables to avoid symbol conflicts.
  ↳ No PR: [7ae3158](https://github.com/openssl/openssl/commit/7ae31586a77c09d45838fff73b589b2958fbd18b), [581c87b](https://github.com/openssl/openssl/commit/581c87b088105db0bddaf80a572b45a23b74e929)
- Increase the timeout of test scripts to prevent timeouts on low-power platforms or slower performance options.
  ↳ No PR: [ad4af6d](https://github.com/openssl/openssl/commit/ad4af6dfca8344516bb658b1745a530635af9433)
- Allow the test_ssl_trace test to be run when zlib is enabled, and select the corresponding reference file based on the zlib enablement status.
  ↳ No PR: [d2751ee](https://github.com/openssl/openssl/commit/d2751ee3932e72b848c22ee2ebddce2e9c93a7ed)
- Removed the call to the unsafe function rand() in the test random number generator and used the xor-shift algorithm instead with a fixed seed.
  ↳ No PR: [eaf0879](https://github.com/openssl/openssl/commit/eaf08794398ac3caaadffcfd670854bf51f610fa)
- Added helper functions for QUIC tests to support connection testing with large client and server certificate chains.
  ↳ No PR: [3860ef2](https://github.com/openssl/openssl/commit/3860ef2ae69ad9187acc17e0d1c78261dbc63125)
- Added tests to verify legacy RSA keys work properly.
  ↳ No PR: [e62097f](https://github.com/openssl/openssl/commit/e62097f48c3d0b8b61ca6a061b8098b0086b3fbc)
- Add a null pointer check in the test function tear_down to prevent problems when a null pointer is passed in.
  ↳ No PR: [91a5c0e](https://github.com/openssl/openssl/commit/91a5c0e40cf272d18b65c9e4c9a0268f244758a8)
- Add tests for the new OSSL_ERR_STATE_save_to_mark() function, covering both saving methods.
  ↳ No PR: [d3bb8fe](https://github.com/openssl/openssl/commit/d3bb8fe73df16e5a96dc94f1ab770b35b6694931)
- Fix potential NULL pointer dereference problem in ssl_old_test.c, and adjust error handling process.
  ↳ No PR: [a595e90](https://github.com/openssl/openssl/commit/a595e90032a246276c441cf7276a9cf8811a2aa4)
- Add test for converting OSSL_TIME to struct timeval.
  ↳ No PR: [039119a](https://github.com/openssl/openssl/commit/039119a0f3eeb610689f21834ea04cc1f0efe8df)
- Add test cases for QUIC for post-connect session ticket handling.
  ↳ No PR: [055f3dd](https://github.com/openssl/openssl/commit/055f3dd140f124df6f2d8f3f910f00928224b04f)
- Add test cases for retry behavior when sending application data.
  ↳ No PR: [dbbdb94](https://github.com/openssl/openssl/commit/dbbdb940d421daca4a65e765b5244bde6aed3f61)
- Add type conversion in sslapitest test to avoid compiler errors.
  ↳ No PR: [74efc54](https://github.com/openssl/openssl/commit/74efc5477c8a78ca80187a1332e5b89ce5ed6c16)
- Allow QUIC testing tools to output removed TLS extensions.
  ↳ No PR: [0561c3c](https://github.com/openssl/openssl/commit/0561c3cfe6c0623a9e7c8a0e062bdbb78b94ccf9)
- Add tests for missing, formatted, duplicate and other abnormal situations for QUIC transmission parameters.
  ↳ No PR: [bcff823](https://github.com/openssl/openssl/commit/bcff823ca7a9a35772b2ac84f2ae291ca8b0ba27)
- Added test case for uniform random number generator.
  ↳ No PR: [2bdf45d](https://github.com/openssl/openssl/commit/2bdf45d875234a9b203a60e2143e4fe977ec5ff9)
- Fixed random failures in QUIC multi-stream tests on Windows, by ensuring frames are injected into the correct packet type and fixing condition variable signal ordering.
  ↳ No PR: [6366192](https://github.com/openssl/openssl/commit/6366192d56d22f44992aa891634085865b12d418), [6aa921f](https://github.com/openssl/openssl/commit/6aa921f27bba5c55acd4ea83d4f221b6c876c59d), [b4cf49c](https://github.com/openssl/openssl/commit/b4cf49cb634d283abffaaec6db682af9eeae3261)
- Added state machine and stream support to the QUIC client fuzzer to send data and process streams after the handshake is complete.
  ↳ No PR: [8dd7ee8](https://github.com/openssl/openssl/commit/8dd7ee8665a2e9f5bab570998426d3eedbdc6128), [5d726f9](https://github.com/openssl/openssl/commit/5d726f9392475205e7c8bc99e8f7603aa093d0ce)
- Add negative tests for changes in IV length and key length.
  ↳ No PR: [de46fe6](https://github.com/openssl/openssl/commit/de46fe6f3386f2a1c31fc124784825c97c9ca6e9), [57fc999](https://github.com/openssl/openssl/commit/57fc9992584a7b9bede4b5eb40a1074f7e7e0df4)
- Remove dead code from test files.
  ↳ No PR: [1ee0a9d](https://github.com/openssl/openssl/commit/1ee0a9d8d3f351813e9db1d528c569c4c8ac3eac)
- Add read-write lock protection to the fake_now variable in quictestlib and fix multi-threaded data race.
  ↳ No PR: [d025b22](https://github.com/openssl/openssl/commit/d025b228fe4c05d4307d245cc888d881e5555858)
- Added additional tests for new flow control parameters.
  ↳ No PR: [50c5676](https://github.com/openssl/openssl/commit/50c56768e184f1c0559d1c88d09d5db001221f28)
- Add debug sanity checks and updated tests for linked list operations.
  ↳ No PR: [3077341](https://github.com/openssl/openssl/commit/30773411264dca0a791a068759ec625bd0d4f34b)
- Add support for TLS handshake messages to QUIC fault injector.
  ↳ No PR: [6d1f693](https://github.com/openssl/openssl/commit/6d1f6933595ea66c2e8367fef01e2824b4f3ce6b)
- Simplified structure initialization in http_test.c to be compatible with gcc-4.8.x.
  ↳ No PR: [a497a90](https://github.com/openssl/openssl/commit/a497a90213b50c499f2a385e63e1fa6e13ef283a)
- Improve the check scope of the check-format.pl script, report constant conditions and operator blanks, and add new test cases.
  ↳ No PR: [6549041](https://github.com/openssl/openssl/commit/6549041704a4827af5ccc01b0552afb6fb7a442b), [521f07e](https://github.com/openssl/openssl/commit/521f07eb08cc267001ecb4be67d46ea79dbb62b1), [3e139f3](https://github.com/openssl/openssl/commit/3e139f3d85396cab0bac5d263472b3223a51b76a)
- Rename the test program and clean up the compilation comments.
  ↳ No PR: [c02036e](https://github.com/openssl/openssl/commit/c02036e1ad759fca228a2201f1c4752670ad59bd)
- Disable the test file timing_load_creds.c on the VMS platform, and add a platform not supported prompt.
  ↳ No PR: [81929ac](https://github.com/openssl/openssl/commit/81929ac49aa583b2347348953d8399ad775c6fd1)
- Use the OPENSSL_SYS_ macro in the test file timing_load_creds.c for platform detection to make the platform judgment clearer and more consistent.
  ↳ No PR: [83c1220](https://github.com/openssl/openssl/commit/83c1220ad137bb4b651478444c3666c66ec9d640)
- Add a check for OPENSSL_malloc allocation failure in the test files ssl_old_test.c and v3nametest.c, and output an error and terminate when it fails.
  ↳ No PR: [b2feb9f](https://github.com/openssl/openssl/commit/b2feb9f0e394da6570346598837f1b01eb58c028), [b147b9d](https://github.com/openssl/openssl/commit/b147b9daf17744d529f23b5da40397a6071a88aa)
- Fixed the compilation problem of test file v3ext.c when RFC3779 is disabled, and protects related test functions through conditional compilation.
  ↳ No PR: [b76efe6](https://github.com/openssl/openssl/commit/b76efe61ea9710a8f69e1cb8caf1aeb2ba6f1ebe)
- Updated test examples and algorithm links in external testing documentation.
  ↳ No PR: [f3f3f86](https://github.com/openssl/openssl/commit/f3f3f86a14dac76f3079fb50cabd14fdab418bb0)
- Document usage of OPENSSL_TEST_RAND_SEED environment variable in test documentation.
  ↳ No PR: [7251b2e](https://github.com/openssl/openssl/commit/7251b2eb14427341630881cf10e4be3fa8661e8c)
- Static link legacy provider to endecode_test test to avoid multiple libcrypto version conflicts caused by dynamic linking.
  ↳ No PR: [7ee992a](https://github.com/openssl/openssl/commit/7ee992a5d931ab5ad9df00d2d8e47e1b7a72d7ac)
- Fix build failure with KTLS enabled when EC is disabled, excluding test cipher suites using ECDHE via conditional compilation.
  ↳ No PR: [2dded44](https://github.com/openssl/openssl/commit/2dded44a4911250acb989a535d2bad0bcf0ccc78)

### Performance optimization
- Added inline assembly acceleration support based on RISC-V Zknh extension for SHA256 algorithm.
  ↳ No PR: [657d192](https://github.com/openssl/openssl/commit/657d1927c68bdc3fb0250d16df2a8439e8e043f1)
- Simplify Ed25519 square root calculation, replace the formula from u*v^3 * (u * v^7)^((p-5)/8) to u * (u*v)^((p-5)/8), reducing 3 multiplications and 2 square operations.
  ↳ No PR: [a822a0c](https://github.com/openssl/openssl/commit/a822a0cb3c8466adbcee510a6234c0fe95ff4bfe)
- Cache key length and IV length to avoid expensive parameter lookups on every query and skip provider calls if parameters have not changed.
  ↳ No PR: [70f39a4](https://github.com/openssl/openssl/commit/70f39a487d3f7d976a01e0ee7ae98a82ceeea7a0)
- Optimize SM4 encryption and decryption performance in non-assembly mode, and introduce table lookup method to replace the original rotation operation.
  ↳ No PR: [13ba91c](https://github.com/openssl/openssl/commit/13ba91cb02479a91b0743d2bf5f5ec7ce42860d0)
- Convert NULL attribute queries to empty strings to fix performance degradation caused by non-caching.
  ↳ No PR: [af788ad](https://github.com/openssl/openssl/commit/af788ad6c3624ccc4b49778a9ded2487b9dbeedd)
- Optimize SM4-GCM encryption/decryption performance on the ARM platform, reuse the existing high-performance CTR encryption interface to replace single-block encryption, and achieve up to 4 times performance improvement.
  ↳ No PR: [26efd0b](https://github.com/openssl/openssl/commit/26efd0b37714dd1f3557c6b6c32822fc99fe1d9b)
- Reconstruct the internal logic of the decoder, reduce repeated calls to OSSL_DECODER_is_a and EVP_KEYMGMT_is_a, and improve the performance of repeated decoding operations.
  ↳ No PR: [2475544](https://github.com/openssl/openssl/commit/247554458435eaab175cdc9d36878158b9eb6f6e)
- Optimize the evp_md_init_internal function: avoid reallocating the algorithm context when the digest algorithm has not changed, and reconstruct the release logic of the algorithm context.
  ↳ No PR: [fe5c5cb](https://github.com/openssl/openssl/commit/fe5c5cb85197aec7d68ab095b866ed22076850d0)
- Added ROTATE inline assembly implementation based on RISC-V zbb/zbkb extension for DES.
  ↳ No PR: [6136408](https://github.com/openssl/openssl/commit/6136408e6abf10672e399bf95be064868f2f7ca6)
- Optimize the ossl_lh_strcasehash function, and the running time is approximately halved.
  ↳ No PR: [a4e21d1](https://github.com/openssl/openssl/commit/a4e21d18d5b7cb4fef66c10f13b1b3b55945439f)
- Ensure that prefix records use small buffers to avoid allocating full-size write buffers when only prefixes are needed.
  ↳ No PR: [85b358b](https://github.com/openssl/openssl/commit/85b358b01a36757d07da118795a0ad13c9c2b4d7)
- Optimize the SM4 key setting function, and improve the performance by about 48% by reconstructing nonlinear transformation and loop expansion.
  ↳ No PR: [704e809](https://github.com/openssl/openssl/commit/704e8090b4a789f52af07de9a3ebbe11db8e19f8)
- Optimize DRBG parameter acquisition, allowing security parameters such as max_request to be read without locking, improving concurrency performance.
  ↳ No PR: [61f11ca](https://github.com/openssl/openssl/commit/61f11cad7a0dffc7abd234164a0e74c6ae8e7c2a)
- Optimize the key update in the QUIC channel, and add a mechanism to force the generation of ACK to speed up the completion of the key update.
  ↳ No PR: [37ba2bc](https://github.com/openssl/openssl/commit/37ba2bc72281c196534e265c34be94beb760393e)
- The state access of the FIPS module is changed from the lock mechanism to the use of memory sorting operations to improve performance and reduce synchronization overhead; at the same time, HMAC-SHA-256 known answer test and RNG recovery verification are added.
  ↳ No PR: [8e9ca33](https://github.com/openssl/openssl/commit/8e9ca334528e0a923c4deb0af250a60510974be0)
- In non-blocking mode, when SSL_read fails, increase the reactor tick and retry reading to improve the success rate of data delivery.
  ↳ No PR: [780b252](https://github.com/openssl/openssl/commit/780b2527476a60f4a2bb791c2d4b1b72f6f0b423)
- Introduce a caching mechanism for the PKEY decoder and reuse OSSL_DECODER_CTX objects with the same parameters to improve performance.
  ↳ No PR: [32d3c3a](https://github.com/openssl/openssl/commit/32d3c3abf3b74df1d9ebe562ba90f4dc3bdf2d4f)
- Introduce branch prediction hints in EVP_EncryptUpdate and EVP_DecryptUpdate, and optimize input length conversion and division operations to improve performance under GCC/Clang.
  ↳ No PR: [ed6dfd1](https://github.com/openssl/openssl/commit/ed6dfd1e3694b3438249f3d0117bc314afa6b240)
- Adopt the Solinas reduction strategy of 56-bit redundant limbs for the secp384r1 curve to achieve efficient modular multiplication operations, increasing the digital signature speed by 446% and the verification speed by 106%.
  ↳ No PR: [01d901e](https://github.com/openssl/openssl/commit/01d901e470d9e035a3bd78e77b9438a4cc0da785)
- Optimize SM2 performance on aarch64 architecture, and add a dedicated SM2 P-256 elliptic curve implementation.
  ↳ No PR: [6399d78](https://github.com/openssl/openssl/commit/6399d7856c75abde9ed23782d10960013de03810)
- Reuse memory allocation between ACK frame processing in QUIC RXDP, and add improvements such as key update checks and flow control notifications.
  ↳ No PR: [8c792b0](https://github.com/openssl/openssl/commit/8c792b0ccd41657d9972efbcc997a0c39d49121f)
- In the QUIC mode of s_client, when there is user data to be written, set the select timeout to 0 to avoid unnecessary waiting.
  ↳ No PR: [95420a2](https://github.com/openssl/openssl/commit/95420a2500fe0d96fb44cf7d826a156433c50589)
- Added performance testing for arbitrary sized integers to tests, and updated minimum buffer size validation.
  ↳ No PR: [b556713](https://github.com/openssl/openssl/commit/b556713a6f2884eadc7f56428bc82a844e9a49e0)
- Correctly check return values of memory allocation functions in ocspapitest.
  ↳ No PR: [ea80951](https://github.com/openssl/openssl/commit/ea809510f69e5aebc2ab95aa7530e01060e8a960)
- Removed DSA 512-bit key test from speed test.
  ↳ No PR: [7c966ab](https://github.com/openssl/openssl/commit/7c966ab6b332d3666870856edb122d67cb09ead5)
- Added performance measurement of RSA encryption and decryption operations to the speed test tool.
  ↳ No PR: [0195df8](https://github.com/openssl/openssl/commit/0195df8baa12ac2f1364f55db09ba7fabb67df93)
- Added QUIC backpressure test to verify the backpressure behavior when data is sent too fast.
  ↳ No PR: [a1c87f6](https://github.com/openssl/openssl/commit/a1c87f64dd6d6b0f1c8b276dc415f69e1102f930)
- Fixed an issue where the EdDSA performance test failed due to premature termination of the context.
  ↳ No PR: [0c85bcb](https://github.com/openssl/openssl/commit/0c85bcbaeabe3a695831bec44ab87964725a51a6)
- Fixed a crash in pipelining tests due to improper error handling leading to the release of read-only memory.
  ↳ No PR: [06a0d40](https://github.com/openssl/openssl/commit/06a0d40322e96dbba816b35f82226871f635ec5a)
- Use a stack structure to efficiently convert attribute indexes into strings, replacing the hash table lookup method.
  ↳ No PR: [2e3c593](https://github.com/openssl/openssl/commit/2e3c59356f847a76a90f9f837d4983428df6eb19)
- Removed unused and inefficient function for getting method by numeric ID, and simplified internal retrieval logic.
  ↳ No PR: [16ff70a](https://github.com/openssl/openssl/commit/16ff70a58cfb5c40197e6a940cf4666226f31b79)
- Automatically optimized the QUIC write buffer size, introduced the maximum buffer limit and restructured the data append logic.
  ↳ No PR: [96040e5](https://github.com/openssl/openssl/commit/96040e539e5ecdf1002e737cb29042f9a065460d)
- Replace OPENSSL_cleanse with memset in the bn2binpad function to improve performance and avoid false positives in fuzz testing.
  ↳ No PR: [858d5ac](https://github.com/openssl/openssl/commit/858d5ac16d256db24f78b8c84e723b7d34c8b1ea)
- Reduced the block size of sparse arrays to improve the performance of the ossl_sa_doall_arg function.
  ↳ No PR: [514bd51](https://github.com/openssl/openssl/commit/514bd51a8cb901a7351ecdc45a680d6aba720b5a)
- Adjusted the order of IV and buffer members in the prov_cipher_ctx_st structure to optimize memory alignment and improve performance.
  ↳ No PR: [2787a70](https://github.com/openssl/openssl/commit/2787a709c984d3884e1726383c2f2afca428d795)
- Added ROTATE inline assembly implementation based on RISC-V zbb/zbkb extension for ChaCha encryption.
  ↳ No PR: [ca6286c](https://github.com/openssl/openssl/commit/ca6286c382a7eb527fac9aba2a018354acb27b16)
- Optimized the performance of the encoder collection process, reducing duplicate conversions by caching name mapping IDs.
  ↳ No PR: [c3b4640](https://github.com/openssl/openssl/commit/c3b46409559c18f103ebb2221c6f8af3cd7db00d)
- Introduced new faster parameter positioning mechanism in GCM implementation.
  ↳ No PR: [79d7022](https://github.com/openssl/openssl/commit/79d702250b76cb88947158d4f4d0786fbe96eeac)
- Optimize the performance of the EVP_PKCS82PKEY_ex function to avoid traversing all decoders by obtaining the key type in advance.
  ↳ No PR: [52ce351](https://github.com/openssl/openssl/commit/52ce351a674bf459c836ffd01afb09917889f047)
- Optimize the performance of d2i_PrivateKey_decoder and related functions, and improve decoding efficiency by first detecting the PKCS8 file format.
  ↳ No PR: [dba97d4](https://github.com/openssl/openssl/commit/dba97d4c7142621fb279ef2074cd5c0a04eca7d3)
- Enable hardware acceleration for SM4-CCM, benchmark based on KunPeng920.
  ↳ No PR: [fdfa63d](https://github.com/openssl/openssl/commit/fdfa63dfd6f1e6d7aff175fba56486a0cf79713f)
- Enable VPSM4_EX_CAPABLE optimization for the SM4-GCM algorithm to improve encryption and decryption performance.
  ↳ No PR: [738d436](https://github.com/openssl/openssl/commit/738d43634a5192b1be0869f151682bb8e9157d5a)
- Optimize the ossl_provider_doall_activated function, change the write lock to a read lock, and use atomic operations to manage activation counts to reduce lock competition.
  ↳ No PR: [fc570b2](https://github.com/openssl/openssl/commit/fc570b2605b8eb18c3903543aaf0234b1f698c8e)
- Optimize the lock mechanism of rsa_get_blinding(), give priority to using read locks, and only upgrade to write locks when modifications are needed to improve multi-threading performance.
  ↳ No PR: [f53479f](https://github.com/openssl/openssl/commit/f53479f98a2f2a6149192c5e3ef4ddf0926dceba)
- Optimize the reference counting operation in EVP_CIPHER initialization to reduce unnecessary up_ref and free calls.
  ↳ No PR: [8ed76c6](https://github.com/openssl/openssl/commit/8ed76c62b5d3214e807e684c06efd69c6471c800)
- Fixed the repeated prefix in the openssl speed command version information printing, and optimized the option information output format.
  ↳ No PR: [9e1b6f3](https://github.com/openssl/openssl/commit/9e1b6f3cdc9258b6759d00cd23819925c9e4c391)
- When defining OPENSSL_SMALL_FOOTPRINT, remove the fast lookup stack for attribute names and attribute values and use hash table traversal instead to reduce memory consumption.
  ↳ No PR: [5764533](https://github.com/openssl/openssl/commit/57645339ab645fe5abffe14fc005b5402ce03b84)
- Adjust the attribute cache refresh behavior. When there is no timer, use the global seed instead and update it after each refresh.
  ↳ No PR: [56d4ff6](https://github.com/openssl/openssl/commit/56d4ff6cd7fc200943197dff65146a8864b7df98)
- Suppress warnings due to ENXIO errors when opening /dev/crypto fails.
  ↳ No PR: [1636b35](https://github.com/openssl/openssl/commit/1636b355ade558d01f5a826494264ca31d6aeeb7)
- Restrict the RSA algorithm name format in the speed tool to only allow rsa followed by a number, and adjust related parameter types.
  ↳ No PR: [316d5a9](https://github.com/openssl/openssl/commit/316d5a982b2534af2238af3560db8fa103a9169a)
- Fix the resource leak of do_multi function in apps/speed.c, and increase the release of fds array.
  ↳ No PR: [a167e04](https://github.com/openssl/openssl/commit/a167e048a40151f9884014680c9a765ef79c3b44)
- Fixed a memory leak in crypto/provider_child.c caused by resources not being released when activating the provider fails.
  ↳ No PR: [e788c77](https://github.com/openssl/openssl/commit/e788c772b12eea5ced4ce46619e13acf0e0eb6ba)
- Fixed a memory leak caused by not releasing lock resources when initializing extended data failed in ossl_ssl_init().
  ↳ No PR: [c10ded8](https://github.com/openssl/openssl/commit/c10ded8c2c862992c98b83909a679aa0bb448a55)
- Clean up unused parameters and variables in speed.c, fix issues such as RSA digit parsing, random number generation error checking and encryption operation error reporting.
  ↳ No PR: [a8eb81c](https://github.com/openssl/openssl/commit/a8eb81ccd2d3daeb92c0842a02dc688eae298250)
- Fixed the issue where the ERR_raise() call in v3_purp.c uses the wrong library identifier, so that the error message is correctly classified into the X509 V3 module.
  ↳ No PR: [959c150](https://github.com/openssl/openssl/commit/959c150a1dcc4535c2d94ac6f3310566723911f1)
- Fixed a memory leak caused by multiple wrong paths in the dane_tlsa_add function.
  ↳ No PR: [7f943d4](https://github.com/openssl/openssl/commit/7f943d40bda4539d63da34ecfbbc8556f2603fb3)
- Fix the use-after-free problem that may occur in custom_exts_free, clear relevant pointers and counters after release.
  ↳ No PR: [54e1786](https://github.com/openssl/openssl/commit/54e178640dee143742a11842469591dc315d5b5f)

### Security related
- Increased the security strength rating of the CCM8 cipher suite from 64 bits to 80 bits, while lowering its security level to level 0 to reflect the lower security strength of the short tag.
  ↳ No PR: [1a473d1](https://github.com/openssl/openssl/commit/1a473d1cc67e04ae9fea517b36dc332143250cf5), [56ffcce](https://github.com/openssl/openssl/commit/56ffcce492ffc6f36b2f0d9431e23febe054dd04), [e071022](https://github.com/openssl/openssl/commit/e07102220afe4059bc45aa3d7073b7678329e26e)
- Fixed potential out-of-bounds issue in help output caused by width exceeding buffer size; refactored output logic to use dynamic length calculation, and added width upper limit check.
  ↳ No PR: [0d1a0ed](https://github.com/openssl/openssl/commit/0d1a0ed63d1b4faa3711a69a19f7029947524cfa), [aac6ae3](https://github.com/openssl/openssl/commit/aac6ae3774f341412bc45583ef9358df5b76a008)
- Add range checking for the -multi parameter in apps/speed.c, fix the buffer length overflow problem caused by MAX_MISALIGNMENT, and unify the loop upper limit to INT_MAX.
  ↳ No PR: [7220085](https://github.com/openssl/openssl/commit/7220085f22cf6c49933ea8287eb15db57f7ab0db), [378c50f](https://github.com/openssl/openssl/commit/378c50f63dceb3a85bb4937a3499283b10d295b6)
- Use safe math functions to calculate rounding sizes to prevent integer overflow.
  ↳ No PR: [330ff7e](https://github.com/openssl/openssl/commit/330ff7e67d2ecc1c298fe7c4347c2109b4a979de)
- Fix address leak and RAND_bytes_ex return value checking issues in CBC_MAC_ROTATE_IN_PLACE, and use constant time loading instead.
  ↳ No PR: [3b83638](https://github.com/openssl/openssl/commit/3b836385679504579ee1052ed4b4ef1d9f49fa13)
- Fixed multiple security vulnerabilities in the c_rehash tool (CVE-2022-1292, CVE-2022-2068): openssl is no longer called through the shell, and the security of file operations is improved.
  ↳ No PR: [7c33270](https://github.com/openssl/openssl/commit/7c33270707b568c524a8ef125fe611a8872cb5e8), [ce60b13](https://github.com/openssl/openssl/commit/ce60b13707add7e6b54c5817376234c4043506ed)
- Add assertions when reusing algorithm context to ensure that the summary object is provided to prevent security issues caused by implicit acquisition.
  ↳ No PR: [221d65b](https://github.com/openssl/openssl/commit/221d65ba534d23a240ccadd0c2679b222aae35b1)
- Disable the SSL2_VERSION version number from appearing in the SSLv3 record header to prevent ambiguity when verifying the record format.
  ↳ No PR: [014baa8](https://github.com/openssl/openssl/commit/014baa8a6dec5956416baad5af4ddda13bf74341)
- Fixed a crash issue that may occur when creating an ASN1 template object when there is insufficient memory. Make sure to check whether the object has been initialized correctly before calling the release callback.
  ↳ No PR: [557825a](https://github.com/openssl/openssl/commit/557825acd622f98fc21423aba092e374db84f483)
- Fixed the memory leak problem caused by BN_bin2bn failure in the ec_key_simple_oct2priv function.
  ↳ No PR: [22a96c6](https://github.com/openssl/openssl/commit/22a96c6be41897d11a18455b2ab142422bc57f3f)
- Increased iteration factor for calculating auxiliary primes in RSA key generation from 5 to 20 to match updates to the FIPS 186-5 standard.
  ↳ No PR: [ad7e0fd](https://github.com/openssl/openssl/commit/ad7e0fd550a9eb2946edf38003ebc6d5b988dac7)
- Add sensitive memory cleaning and error checking in DH, DSA, EC, RSA private key encoding functions.
  ↳ No PR: [1624934](https://github.com/openssl/openssl/commit/16249341bb64329c2542c3d1e23b97ed3c44fad3)
- Securely erase MAC keys for SSLv3 when clearing the record layer.
  ↳ No PR: [c77d455](https://github.com/openssl/openssl/commit/c77d4556732e2e41e975211498406c777136fbaa)
- Fixed the heap buffer overflow problem in BIO_ADDR_dup caused by copying the entire structure, and copied the correct union members instead.
  ↳ No PR: [278b0d8](https://github.com/openssl/openssl/commit/278b0d8b674eba6f6e1ec51a18c3ccaf8db02701)
- Fixed the out-of-bounds reading problem in the ssl_cipher_process_rulestr function when the rule string ends with '-'.
  ↳ No PR: [428511c](https://github.com/openssl/openssl/commit/428511ca66670e169a0e1b12e7540714b0be4cf8)
- Verify that the random number generator (RNG) is restored correctly after the FIPS self-test.
  ↳ No PR: [33290c5](https://github.com/openssl/openssl/commit/33290c534750f031cbf384f0ad8c05555a16f726)
- Fixed out-of-bounds write vulnerability in punycode decoder (CVE-2022-3602), fixed off-by-one error in buffer bounds check.
  ↳ No PR: [3b421eb](https://github.com/openssl/openssl/commit/3b421ebc64c7b52f1b9feb3812bdc7781c784332), [a0af4a3](https://github.com/openssl/openssl/commit/a0af4a3c8b18c435a5a4afb28b3ad1a2730e6ea8), [8aa82b3](https://github.com/openssl/openssl/commit/8aa82b337081b7a22c35dddad8d62fb1ca9ea884)
- Fixed the buffer overflow vulnerability (CVE-2022-3786) in the punycode decoder and solved the potential buffer overflow issue in the ossl_a2ulabel function.
  ↳ No PR: [680e65b](https://github.com/openssl/openssl/commit/680e65b94c916af259bfdc2e25f1ab6e0c7a97d6)
- Fix the tainted scalar issue reported by Coverity and add an upper limit check on the variable uclen in compressed certificate processing.
  ↳ No PR: [00e38ed](https://github.com/openssl/openssl/commit/00e38edcfb95b556a59de96e0c18343828929c8f)
- Fixed the security issue in BN_mod_exp_mont_consttime where the modulus is too large causing buffer length overflow, and added invalid parameter check.
  ↳ No PR: [4378e3c](https://github.com/openssl/openssl/commit/4378e3cd2a4d73a97a2349efaa143059d8ed05e8)
- Fixed the timing side channel vulnerability in RSA decryption by adjusting blinding processing, error reporting and padding check logic to eliminate exploitable timing differences.
  ↳ No PR: [b1892d2](https://github.com/openssl/openssl/commit/b1892d21f8f0435deb0250f24a97915dc641c807)
- Fixed a type confusion vulnerability in nc_match_single caused by incorrect assumption of OtherName type, which may cause certificate name constraint check errors.
  ↳ No PR: [748f478](https://github.com/openssl/openssl/commit/748f478f814bc8e418542c68599ec7dbcbac97b2)
- Fixed PEM_read_bio_ex not clearing the header and data pointers on failure, resulting in a potential double free.
  ↳ No PR: [ee6243f](https://github.com/openssl/openssl/commit/ee6243f3947107d655f6dee96f63861561a5aaeb)
- Fixed the use-after-free vulnerability in the BIO_new_NDEF function caused by invalid BIO chain due to callback failure.
  ↳ No PR: [9cc8500](https://github.com/openssl/openssl/commit/9cc85002a1138235bdc272b837d7eb32d6b7aa95)
- Clean the internal buffer used to generate k in the BN_generate_dsa_nonce function to prevent leakage of sensitive data.
  ↳ No PR: [177d433](https://github.com/openssl/openssl/commit/177d433bda2ffd287d676bc53b549b6c246973e6)
- Fixed the null pointer dereference vulnerability in the FFC public key and private key verification functions, added parameter null value checking and returned the corresponding error code.
  ↳ No PR: [bcec03c](https://github.com/openssl/openssl/commit/bcec03c33cc00a7b5eb89ebeeee59e604570a86a)
- Fixed the security vulnerability of dereferencing null pointers when PKCS7 object data is not set (CVE-2023-0216).
  ↳ No PR: [80253db](https://github.com/openssl/openssl/commit/80253dbdc92bec584f4a9866b43f8674156d838a)
- Fixed the issue in pk7_doit.c that the return value of BIO_set_md() was not checked, preventing null pointer dereference due to digest algorithm initialization failure, and fixed CVE-2023-0401.
  ↳ No PR: [6eebe6c](https://github.com/openssl/openssl/commit/6eebe6c0238178356114a96a7858f36b24172847)
- Adjusted session ID generation and renegotiation check logic in fuzz testing mode so that the post-handshake phase can be triggered to support discovery of CVE-2021-3449.
  ↳ No PR: [2b9e2af](https://github.com/openssl/openssl/commit/2b9e2afc382490592078cdb69d06f54f0fefd4c6)
- Fixed the timing leak vulnerability in RSA private key decryption, and added the constant time function bn_correct_top_consttime to eliminate side channel risks.
  ↳ No PR: [f06ef16](https://github.com/openssl/openssl/commit/f06ef1657a3d4322153b26231a7afa3d55724e52)
- Fixed a security vulnerability where invalid policy extension flags in leaf certificates were not checked, ensuring that all certificates are correctly verified.
  ↳ No PR: [e4142ec](https://github.com/openssl/openssl/commit/e4142ec43bcc08ffdb090580e24c24a7da302a32)
- Fixed the resource overuse vulnerability (CVE-2023-0464) in X.509 certificate policy constraint verification to prevent denial of service attacks by limiting the number of policy tree nodes.
  ↳ No PR: [3a81370](https://github.com/openssl/openssl/commit/3a81370f75b832102e9969533a25ca53fe0b254e)
- Fixed use-after-free vulnerability in argon2 KDF caused by not releasing MAC context.
  ↳ No PR: [7c45b7c](https://github.com/openssl/openssl/commit/7c45b7cbb04e297c3342fcc50bf7b0a9e36df1dd)
- Use safe multiplication functions to replace original calculations in QUIC NewReno congestion control to prevent integer overflow.
  ↳ No PR: [d235f65](https://github.com/openssl/openssl/commit/d235f657f89a6cdce93806bb4e965dfd865a7a13)
- Replaced getenv() with ossl_safe_getenv() in HTTP proxy handling for safe reading of environment variables.
  ↳ No PR: [e7cbb09](https://github.com/openssl/openssl/commit/e7cbb09fdf8d835bd0d88b4b288edfd525be569c)
- Fixed the stack use-after-free problem caused by local variables on the callback function stack in QUIC, and changed the protocol string in the ALPN selection callback to a static constant.
  ↳ No PR: [ca9ef8e](https://github.com/openssl/openssl/commit/ca9ef8ebf5908a6115990967df648d8f29e66f42)
- Fixed an integer operation that may overflow in the HKDF_Expand function, and changed the addition comparison to a subtraction comparison to avoid potential overflow risks.
  ↳ No PR: [56a51b5](https://github.com/openssl/openssl/commit/56a51b5a1ecd54eadc80bed4bfe5044a340787c1)
- Added a check for the receive packet forgery limit in QUIC channels and enforced the limit when processing receive packets.
  ↳ No PR: [48120ea](https://github.com/openssl/openssl/commit/48120ea5e3648a581ec8011594641178d85b17c4)
- Fixed the check of the final size in the RESET_STREAM frame to ensure that the received final size is consistent with the previously recorded value to prevent illegal modification.
  ↳ No PR: [2cc0e2d](https://github.com/openssl/openssl/commit/2cc0e2dddfe02c5fad74524bc975051021413ea5)
- Ensure QUIC packet number duplication suppression occurs after AEAD verification to avoid side channel attacks.
  ↳ No PR: [dfe5e7f](https://github.com/openssl/openssl/commit/dfe5e7fa987c0e79c165a677d6572a04105528e3)
- Updated legacy authentication strength checks for DSA keys, tightening security conditions per SP 800-131Ar2.
  ↳ No PR: [71cf587](https://github.com/openssl/openssl/commit/71cf587ea21c1422640847e358019a51806d2811)
- Added data clearing function in release, resize and pop operations of send and receive ring buffers.
  ↳ No PR: [292c9df](https://github.com/openssl/openssl/commit/292c9df2662b6bd54fea233964d908de5c63db7a)
- Fixed the vulnerability of ignoring empty associated data in AES-SIV mode, ensuring that zero-length associated data can also be correctly authenticated.
  ↳ No PR: [c426c28](https://github.com/openssl/openssl/commit/c426c281cfc23ab182f7d7d7a35229e7db1494d9)
- Strengthened the QUIC ring buffer, added safe mathematical operations and offset upper limit checks to prevent integer overflow caused by internal misuse.
  ↳ No PR: [6042189](https://github.com/openssl/openssl/commit/60421893a286bb9eb7fb7c2454b84af9778ffca4)
- Added test cases for CVE-2021-4044, CVE-2023-0286 and CVE-2023-3446 to verify the correctness of related security fixes.
  ↳ No PR: [752aa4a](https://github.com/openssl/openssl/commit/752aa4a6f0f3098258fb6be5592fd18929da59c0), [55aab29](https://github.com/openssl/openssl/commit/55aab29c1ea2b8103aa0f0ecb20c058ff200fe27), [ede782b](https://github.com/openssl/openssl/commit/ede782b4c8868d1f09c9cd237f82b6f35b7dba8b)
- Added safe math functions and integer overflow auxiliary functions, and applied safe math operations in x509 certificate processing to enhance overflow detection capabilities.
  ↳ No PR: [4157a32](https://github.com/openssl/openssl/commit/4157a32867e6643da8daee94e836aaa18b9feed6), [b037e36](https://github.com/openssl/openssl/commit/b037e3637a492fefe22b5fb12d7206afe6754ccd), [87fd67d](https://github.com/openssl/openssl/commit/87fd67d997b236d1202546345d18384a968c9206)
- Adjusted the security level of DTLS testing, lowering the security level to allow DTLSv1 testing when DTLSv1.2 is disabled, ensuring test coverage.
  ↳ No PR: [a6843e6](https://github.com/openssl/openssl/commit/a6843e6ae8ae0551aae8555783f06dab7951f112)
- Updated punycode implementation, using WPACKET instead of custom range check, and fixed punycode string termination processing in x509, improving code security and correctness.
  ↳ No PR: [905ba92](https://github.com/openssl/openssl/commit/905ba924398f474e647de70345b4ae4089fedba7)
- Use OPENSSL_strnlen and memcpy in SSL_get_shared_ciphers instead of unsafe string functions, and optimize boundary checking to improve code security.
  ↳ No PR: [2743594](https://github.com/openssl/openssl/commit/2743594d73e65c38375c619e89ec62579e2c24a9)
- Change DES weak key detection and key parity check to constant time implementation to eliminate timing side channel risks.
  ↳ No PR: [8db9d07](https://github.com/openssl/openssl/commit/8db9d07508e201d95e40f8006ede3a76494bbef3)
- Fixed the memory security issue caused by private key length mismatch during ECX key creation. Now when a length error is detected, the private key will be cleared immediately and failure will be returned.
  ↳ No PR: [50938ae](https://github.com/openssl/openssl/commit/50938aec35fd57fb3bec707ead2eee381fcfaf04)
- Fixed an infinite verification loop issue caused by the has_san_id function returning -1 when the certificate lacks SAN extension (CVE-2021-4044).
  ↳ No PR: [6894e20](https://github.com/openssl/openssl/commit/6894e20b50c1204bfc990093b4e7ccd10f92865d)
- Clear the password buffer before releasing the PKCS12 structure to avoid passwords remaining on the stack.
  ↳ No PR: [da7db7a](https://github.com/openssl/openssl/commit/da7db7ae6d7d1929893a58e41335c88e472fc364)
- Improved error message when random pool overflows, now includes details such as entropy factor, required entropy and number of bytes for safe debugging.
  ↳ No PR: [0a8faac](https://github.com/openssl/openssl/commit/0a8faac3c7cc2e88f46a8bdce5bd039dc22abdec)
- Adjusted BIO_f_cipher refresh logic and added progress check to avoid infinite loop.
  ↳ No PR: [e51dd6e](https://github.com/openssl/openssl/commit/e51dd6ee1bac6b54debea3f48c6f58b761229b73)
- Limit the number of includes in the configuration file in fuzz testing mode to prevent timeouts.
  ↳ No PR: [5f3adf3](https://github.com/openssl/openssl/commit/5f3adf396b06ee3b81938468995e69cff4ca64d1)
- Added receive stream status verification in QUIC APL, and fixed related status check logic.
  ↳ No PR: [e0bd282](https://github.com/openssl/openssl/commit/e0bd282517f5853f2cfc73e90fc04be7a70dfd66)
- Updated CHANGES.md and NEWS.md, and added multiple security fix instructions.
  ↳ No PR: [5eef9e1](https://github.com/openssl/openssl/commit/5eef9e1deb11d769dff3b76a21634e39bd533336), [de85a9d](https://github.com/openssl/openssl/commit/de85a9de3f56aaf8c55c28fe495b900e50752a5a), [0be7510](https://github.com/openssl/openssl/commit/0be7510f49e498532708fd03628fc3fc62ee7875)
- Added explicit token permission settings for multiple GitHub Actions workflows, restricting them to read-only.
  ↳ No PR: [c6e7f42](https://github.com/openssl/openssl/commit/c6e7f427c82dfa17416a39af7661c40162d57aaf)

### Documentation
- Add comments to the chunk order of the BIGNUM structure.
  ↳ No PR: [99d3349](https://github.com/openssl/openssl/commit/99d3349d6f4b62c89d0cbcd6200cbc9bda388c52)
- Updated CHANGES.md, adding change entries for version 3.0.1 and adjusting the version title format.
  ↳ No PR: [c868d1f](https://github.com/openssl/openssl/commit/c868d1f9ca923fa4ea57a46e823c280233e254ea)
- Add version title in CHANGES.md for upcoming 1.1.1n release.
  ↳ No PR: [522a32e](https://github.com/openssl/openssl/commit/522a32ef1ecba100a63d547bafc3391ceac7220a)
- Updated the upgrade guide link to the migration_guide man page in README, and updated the copyright year.
  ↳ No PR: [96a7766](https://github.com/openssl/openssl/commit/96a77661723b4ba8fe9eb7cef009d735c97e2aa6)
- Add missing link to OpenSSL 3.0 man page in README.
  ↳ No PR: [a20c9b6](https://github.com/openssl/openssl/commit/a20c9b6c13afb71e1dd03bf122673e3093d6c437)
- Fixed the NOTES-Windows.md document format problem and resolved the document check failure.
  ↳ No PR: [bd28a23](https://github.com/openssl/openssl/commit/bd28a23eb120b4fdfd45d18a1f05cd7366ed8058)
- Added Tomáš Mráz's key fingerprint to the release key fingerprint document.
  ↳ No PR: [2c0a944](https://github.com/openssl/openssl/commit/2c0a944c69dc92cb280147997696cd88acd7b395)
- Added design requirements document for QUIC packet demultiplexer.
  ↳ No PR: [6347b86](https://github.com/openssl/openssl/commit/6347b86778a392c955b60b1ce107951d3552aec2)
- Explain in CHANGES.md that case-insensitive string comparison no longer uses locale and has been implemented directly.
  ↳ No PR: [8a66b2f](https://github.com/openssl/openssl/commit/8a66b2f9fc5dd8a357b6008221883bbd73af4f72)
- Added design documentation for QUIC connection ID caching, and updated related descriptions to support many-to-one matching.
  ↳ No PR: [538ee4e](https://github.com/openssl/openssl/commit/538ee4e0977492009f8ca39d577d8a1aeb8d27fd), [4efc969](https://github.com/openssl/openssl/commit/4efc969852cdb7883d240e423e887a57504dcd36), [5be1543](https://github.com/openssl/openssl/commit/5be15438fc0bcb81fdf22dee6c7801ca3089fb74)
- Updated CHANGES.md and NEWS.md to add multiple change entries for OpenSSL 3.1 version, and document security fixes and version changes.
  ↳ No PR: [cbb1cda](https://github.com/openssl/openssl/commit/cbb1cda67f61b34c89fb49c8e2267ec6217bc33f), [79edcf4](https://github.com/openssl/openssl/commit/79edcf4da7d4525acf0db894bc6af6f9ca2b9b9b), [e0fbaf2](https://github.com/openssl/openssl/commit/e0fbaf2a4add8dd012b92923b0f23e87b1d28482), [3c53032](https://github.com/openssl/openssl/commit/3c53032a13fe48421e04d6314ad473f24dbb08a8)
- Remove outdated ssl/record/README.md file.
  ↳ No PR: [df60982](https://github.com/openssl/openssl/commit/df60982574338309856d4f746a2b641c108b1276)
- Add missing documentation for X509_REQ_get_extensions() and X509_REQ_add_extensions{,_nid}().
  ↳ No PR: [47dc828](https://github.com/openssl/openssl/commit/47dc828c6b652feb9cef5b0e4186d010986f197c)
- Add missing documentation for X509_gmtime_adj() function.
  ↳ No PR: [425e972](https://github.com/openssl/openssl/commit/425e972dfaf867affb5b3d438d9ca67bb6aeed65)
- Fix missing closing bracket in rsa command help text.
  ↳ No PR: [3c1f8fb](https://github.com/openssl/openssl/commit/3c1f8fb13e064ad7f42e9b65c601c68e1aa79f7d)
- Added design documentation for QUIC Stream Receive Buffers module.
  ↳ No PR: [fb8bdbe](https://github.com/openssl/openssl/commit/fb8bdbe3eba83265586a44cda2ffc783611680d7)
- Organize RIPEMD160 in CHANGES.md, add the version record of the default provider, and remove duplicate entries.
  ↳ No PR: [ce9317a](https://github.com/openssl/openssl/commit/ce9317a4cfc01541964a14745c4d09e2a846981c), [b655379](https://github.com/openssl/openssl/commit/b6553796190ad7401b89c6cd0499bae77b39d1a6), [fba3242](https://github.com/openssl/openssl/commit/fba324204f3bdd8ba9e99d42db030aaf6482d896)
- Added and improved the QUIC API overview design document, describing the API design goals, new and changed interfaces, and updated the glossary.
  ↳ No PR: [5c0356a](https://github.com/openssl/openssl/commit/5c0356a240d095ca7084d2ec2436a664f3c05156), [88e3a64](https://github.com/openssl/openssl/commit/88e3a640d90943db051bea427afbf86eec79e80e), [aef2496](https://github.com/openssl/openssl/commit/aef249612759a12683c472a1032629ad90f8fd4a), [2b54270](https://github.com/openssl/openssl/commit/2b5427027b74d6ea14638c25c1efe028a99aaf54), [5633a32](https://github.com/openssl/openssl/commit/5633a323df5a533e003163b9f556a476b9f9df45)
- Added and improved the QUIC I/O architecture design document, added block diagrams and adjusted wording.
  ↳ No PR: [aed7082](https://github.com/openssl/openssl/commit/aed7082419465d1c74a0b96cbdc9ae938deaff06), [dda8647](https://github.com/openssl/openssl/commit/dda864793e2de00159f268d910b95e98f21525ae)
- Add documentation for EVP_ASYM_CIPHER-RSA, and update the missing documentation list.
  ↳ No PR: [ad60cd5](https://github.com/openssl/openssl/commit/ad60cd522b4f717a69c690f68f1591371a048591)
- Add documentation and danger warnings for BIO_s_dgram related functions, and update the missing documentation list.
  ↳ No PR: [408622b](https://github.com/openssl/openssl/commit/408622b73a18dd1d8eeb6629bdd91b06715823cc)
- Added records for KMAC support in KBKDF in CHANGES.md.
  ↳ No PR: [ec3342e](https://github.com/openssl/openssl/commit/ec3342e76f31b2d5146313fd03f0c8d65977c799)
- Add a comment to the QUIC test fault injector's buffer adjustment function stating that the buffer is over-allocated.
  ↳ No PR: [47d905f](https://github.com/openssl/openssl/commit/47d905fdc635dcf92a2de4d1d4eb4cb47a4adcec)
- Added design documentation for QUIC thread-assisted mode.
  ↳ No PR: [27c49c0](https://github.com/openssl/openssl/commit/27c49c06f173ce009a00778206a95dfc81618470)
- Display the default number of iterations of PBKDF2 (10000) in the enc command's help information and documentation.
  ↳ No PR: [dc43f08](https://github.com/openssl/openssl/commit/dc43f080c5d60ef76df4087c1cf53a4bbaad93bd), [6678b08](https://github.com/openssl/openssl/commit/6678b0868b7660177f8b5af299894e2e99330a21)
- Document the new -no_drbg_truncated_digests option, which disables the use of truncated digests in Hash and HMAC DRBGs, in the FIPS schema documentation and change log.
  ↳ No PR: [e14fc22](https://github.com/openssl/openssl/commit/e14fc22c90ce5a9e6d66d8658fc6bb37f95019da), [808b30f](https://github.com/openssl/openssl/commit/808b30f6b60da3e92283e315f2e6f0e574a62080)
- Add documentation for advanced command mode (-adv option) and QUIC mode for s_client.
  ↳ No PR: [b21306b](https://github.com/openssl/openssl/commit/b21306b9300996b0e69947d6b4cfa64e4c62ec07), [90ae2c1](https://github.com/openssl/openssl/commit/90ae2c13c1cc318568c65d6ad18409741cc54eae)
- Updated CHANGES.md and NEWS.md, recorded security fixes (CVE-2023-0465, CVE-2023-0464, CVE-2023-1255) and corrected related documentation.
  ↳ No PR: [5ab3f71](https://github.com/openssl/openssl/commit/5ab3f71a33cb0140fc29ae9244cd4f8331c2f3a5), [986f9a6](https://github.com/openssl/openssl/commit/986f9a674d49d1e13459e04bd721237c721c44f4), [72dfe46](https://github.com/openssl/openssl/commit/72dfe46550ee1f1bbfacd49f071419365bc23304), [5f14b5b](https://github.com/openssl/openssl/commit/5f14b5bc25d78384d239428f0d255d1ea7c4a6d1), [83ff6cb](https://github.com/openssl/openssl/commit/83ff6cbd9a02ed713bf66f960ab9aea5fced49a3)
- Add comments in Windows thread related code stating that LONG type is the same size as int.
  ↳ No PR: [a2c61e4](https://github.com/openssl/openssl/commit/a2c61e414332fa7162bb0f9ab991983e0d8cb438)
- Add RFC 9000 compliance annotation in NEW_CONNECTION_ID frame processing to indicate that the current implementation meets relevant requirements.
  ↳ No PR: [5cc7369](https://github.com/openssl/openssl/commit/5cc73695df371bac2769bebb0ef2cc70665c486e)
- Added a non-blocking QUIC client example, and improved the socket creation function to support non-blocking mode and error handling.
  ↳ No PR: [23fe02e](https://github.com/openssl/openssl/commit/23fe02e59785f0cfaa6d50aa3fa0d82bffe22a8d), [92db6d6](https://github.com/openssl/openssl/commit/92db6d628016baa146bfce8b645c13f64ad4bf68), [b3e71db](https://github.com/openssl/openssl/commit/b3e71dbf6863343cfabdbe2ba0443fcb69343874)
- Fix missing comma in option list in openssl-rsautl man page.
  ↳ No PR: [83f9d03](https://github.com/openssl/openssl/commit/83f9d03e7c4913c3eb34edd4a8feb3833650b58f)
- Updated comments in QUIC transport code, adding reference to RFC 9000 section 10.2.3 to clarify compliance.
  ↳ No PR: [d15d5ea](https://github.com/openssl/openssl/commit/d15d5ea6a6dbc98dce76ea40287d5e65fe3c0be8)
- Added comments to the sample code and added a non-blocking QUIC client sample guide page.
  ↳ No PR: [8d74a13](https://github.com/openssl/openssl/commit/8d74a1316025a4730f18674ccf187c3d630d7c92), [e8a5b06](https://github.com/openssl/openssl/commit/e8a5b06bdc280355f5c6703849868708ba83454c)
- Expand instructions on how to do other useful work in non-blocking examples, and fix wrong protocol type in comments.
  ↳ No PR: [38c3c1d](https://github.com/openssl/openssl/commit/38c3c1dbefa8b8333e78e0d9d38fac7c4359f826)
- Rename the design document OSSL_PROVIDER_load_ex to ossl-provider-load-ex.md, and update the document title simultaneously.
  ↳ No PR: [0988de2](https://github.com/openssl/openssl/commit/0988de278c2f861e47d63cd284992befa686e4a8)
- Added design documentation describing how to allow AlgorithmIdentifier parameter data to be passed to cryptographic operations and providing convenience functions for all algorithms.
  ↳ No PR: [11f69aa](https://github.com/openssl/openssl/commit/11f69aa50771d50151fa24c55fd0858db30517df)
- Added a link to the nghttp3 library in the README document of the HTTP/3 examples, and updated build and run instructions.
  ↳ No PR: [10c0424](https://github.com/openssl/openssl/commit/10c04246be386b88fb98129b43b454ebf2d633e6), [0f96c6e](https://github.com/openssl/openssl/commit/0f96c6e39ad6f60c3166b8356fa46756b20226d0)
- Add comments to the HTTP/3 demo code to explain the design intent of key functions and processes.
  ↳ No PR: [47f8cfe](https://github.com/openssl/openssl/commit/47f8cfead0fbacc9151e4ade72bc00427eaf62b7)
- Add a reference to the demos subfolder in the README document to guide users to view the sample code.
  ↳ No PR: [5e3735b](https://github.com/openssl/openssl/commit/5e3735b60082794e4c389990bb4c3f2aa121dd8b)
- Added reference to RFC 9114 for HTTP/3 in QUIC documentation and added a link to the IANA standards list of ALPN protocol IDs.
  ↳ No PR: [a214e06](https://github.com/openssl/openssl/commit/a214e06640ce5d889a688ef4df0282a07a491ac3)
- Add a separate README for the guide examples, explaining how to set LD_LIBRARY_PATH to run, and update the links and descriptions in the main README and QUIC README.
  ↳ No PR: [0564778](https://github.com/openssl/openssl/commit/056477860c0da50d6723e324214a3a9cfbae29ad), [70de526](https://github.com/openssl/openssl/commit/70de52650d9aeab475745edcfa268112ed2a3eff), [f7f40db](https://github.com/openssl/openssl/commit/f7f40db44bf045389ee7d2f60e4416374dc3f2e8)
- Publish update changelog and news documentation for OpenSSL 3.2 beta 1.
  ↳ No PR: [26ecab1](https://github.com/openssl/openssl/commit/26ecab1fd7fa7f5103ac57ef41ee0dd38fbe2ddc)
- Modify the TLS sample program to accept hostname and port from command line arguments and add support for IPv6 options.
  ↳ No PR: [151af35](https://github.com/openssl/openssl/commit/151af35f560a696ddb2793e4b8a5e675dc5994ac)
- Documented in CHANGES.md that the BLAKE2b hash algorithm supports configuring the output length by setting the size parameter.
  ↳ No PR: [676f6e2](https://github.com/openssl/openssl/commit/676f6e2320f917bdd697deea69b6110507e9d81a)
- Add link to OpenSSL 3.2 manual page in README.
  ↳ No PR: [1b83adc](https://github.com/openssl/openssl/commit/1b83adc065130fcea913b4f7b1e13176d4aa1074)
- Updated CHANGES.md and NEWS.md to document CVE-2023-5678, OpenSSL 3.0.2 and 3.0.3 version changes, OPENSSL_str[n]casecmp function changes, and PVK KDF migration.
  ↳ No PR: [4ee71b4](https://github.com/openssl/openssl/commit/4ee71b4c302a06c24b46a5def1cff2096bd57f0b), [a40398a](https://github.com/openssl/openssl/commit/a40398a15ea9c218f4a6db8fef2b925ca4d39451), [73e044b](https://github.com/openssl/openssl/commit/73e044bd1aa3ff00e189624b4807e15e8de8f8e4), [8b97bfc](https://github.com/openssl/openssl/commit/8b97bfcccc4328c65156bff6886db8733df39fde), [c8ffd22](https://github.com/openssl/openssl/commit/c8ffd2201b8685e149dd3244d6772339263d4a17)
- Added multiple EVP API demonstration examples, covering ARIA-256-CBC, SipHash, Poly1305-AES, X25519 key exchange, RSA-PSS signature verification, SHAKE256 XOF, RSA key generation and RSA key encoding/decoding.
  ↳ No PR: [3769727](https://github.com/openssl/openssl/commit/376972773469e59a19acb9ebdecd3ddc290e391b), [8648539](https://github.com/openssl/openssl/commit/864853988e80517a563d2423d4fb742323995433), [3dafeac](https://github.com/openssl/openssl/commit/3dafeacef8d7bf82e462cc52659681108db42e43), [2cc7c9b](https://github.com/openssl/openssl/commit/2cc7c9b6981d683711e76c3483f813701b686eb9), [e9492d1](https://github.com/openssl/openssl/commit/e9492d1cecf459261f1f5ac0eb03e9c631600537), [4c8cdcd](https://github.com/openssl/openssl/commit/4c8cdcd1cf74747a80b4f7dd323cd83ea6c985d8), [ad083f9](https://github.com/openssl/openssl/commit/ad083f9b0ab81d094c2dbb8f5e2a5fb7738a0bfe), [1483b37](https://github.com/openssl/openssl/commit/1483b37e7a2c952eed5f6c7f5c0be9635aa3a6ea)
- Added multiple documents: HOWTO for writing public functions and macros, QUIC record layer design, dgram API design and QUIC high-level overview.
  ↳ No PR: [c3637ca](https://github.com/openssl/openssl/commit/c3637cafd378f2dacc70018499fec4619082051b), [14b5447](https://github.com/openssl/openssl/commit/14b54475d141bf92390934a30ff406a0551e36e9), [b80395e](https://github.com/openssl/openssl/commit/b80395efc91e97fdd0ec724c3e3b814195affe21), [4c149cf](https://github.com/openssl/openssl/commit/4c149cf9f6a2ba665d74dbd4cf44f080816c900b)
- Add initial demo-driven design sample code to demonstrate interaction with libssl under different usage modes (blocking, non-blocking, memory BIO, libuv integration).
  ↳ No PR: [ec36534](https://github.com/openssl/openssl/commit/ec36534cbbf57999b90cbb36404d9daa599a9ae4)
- Added multibin option description in the configuration document to support the coexistence of multiple binary variants.
  ↳ No PR: [d793a32](https://github.com/openssl/openssl/commit/d793a3253bada9b61e5ccd5f8caaa4bfc4f4faa6)
- Removed entries for the X509_STORE_CTX_set_purpose, X509_STORE_CTX_set_trust and X509_STORE_CTX_purpose_inherit functions from the missing documentation list, indicating that these functions are already documented.
  ↳ No PR: [7b75b97](https://github.com/openssl/openssl/commit/7b75b973fbd9087714daa19e07bb92b2101eba28)
- Added sample programs for calculating HMAC and CMAC using EVP_MAC, EC key encoding using EVP, and AES key wrap, and corrected the algorithm name in the CMAC example.
  ↳ No PR: [e269d8a](https://github.com/openssl/openssl/commit/e269d8af79de7b0dcc1b72687eed340cc3822a9e), [cdf0a5c](https://github.com/openssl/openssl/commit/cdf0a5c46032ba4c39d93a7bec52494b4808830f), [a4b7136](https://github.com/openssl/openssl/commit/a4b7136ebfd154636f607c50aaeec778a75b2d26), [bebc6c8](https://github.com/openssl/openssl/commit/bebc6c899943cc3f519501aee221c9d0eb10fcfd), [9270f67](https://github.com/openssl/openssl/commit/9270f67059e0291a2ef73acfba5a4ac54f732ef9)
- Added design documents for QUIC TX Packetiser, Frame-in-Flight Manager, connection state machine and thread pool, and expanded the frame type table of the RX Depacketizer document.
  ↳ No PR: [fabce80](https://github.com/openssl/openssl/commit/fabce8090c3ba49527d434a4621c660eedad2aaa), [d55fc02](https://github.com/openssl/openssl/commit/d55fc027b9af85b1054cdbc017046a9070935086), [66a6659](https://github.com/openssl/openssl/commit/66a6659a244f9c1da301a675c6013db4db71d39e), [9be2693](https://github.com/openssl/openssl/commit/9be2693438756b5f1b789f1b8db76c3b987063dc), [269ad8d](https://github.com/openssl/openssl/commit/269ad8d571e68513175fdc66227943786353cfa8)
- Corrected the documentation description of certificate serial number file storage and usage.
  ↳ No PR: [aa73b7d](https://github.com/openssl/openssl/commit/aa73b7d352c383e415d4d7567b79ce074c6762cd)
- Updated documentation for SHAKE algorithm, modified help text for xoflen option and added comments.
  ↳ No PR: [b7cf9dd](https://github.com/openssl/openssl/commit/b7cf9dd2393de8e90a15e83466d9b8b781b18385)
- Add missing entry for cmp command in openssl-cmds documentation.
  ↳ No PR: [33478ae](https://github.com/openssl/openssl/commit/33478aedafaff1f414cabd67fb30970c41996f5c)
- Fixed documentation error in the default value of the elliptic curve point conversion format, correcting the default value from compressed to uncompressed.
  ↳ No PR: [df274c3](https://github.com/openssl/openssl/commit/df274c334c523f7375d5aa60ff4b9a846c3e2a6c)
- Fixed incorrect description of default MAC algorithm in pkcs12 help text, corrected SHA1 to SHA256.
  ↳ No PR: [72a85c1](https://github.com/openssl/openssl/commit/72a85c17aae602e881c917c3f6e93bd7f7260093)
- Updated the documentation for the OCSP command to clearly state that the option supports multiple input formats, and changed the description of the -CA option to plural form.
  ↳ No PR: [9748e61](https://github.com/openssl/openssl/commit/9748e6127634e26483ff796d6572a303b1d514b7)
- Update documentation to note that standard input is also expected to be in binary format.
  ↳ No PR: [054189b](https://github.com/openssl/openssl/commit/054189bf7a9e68a7374744e7eaea344ba1784e68)
- Add documentation for the OPENSSL_gmtime family of functions.
  ↳ No PR: [28a5aa0](https://github.com/openssl/openssl/commit/28a5aa0cbdddfdf4d82a437d72407d4f52d4e54a)
- Add CHANGES.md entry for libssl record layer refactoring.
  ↳ No PR: [4a532de](https://github.com/openssl/openssl/commit/4a532de98d6100d9e0643d5b61d8716539c8a7cd)
- Add code of conduct file (CODE-OF-CONDUCT.md).
  ↳ No PR: [63df86b](https://github.com/openssl/openssl/commit/63df86b041aaafba3e4998b2e3872fa8695a2377)
- Added sample code for DSA signature and parameter generation, loading, verification and key generation.
  ↳ No PR: [858b5d1](https://github.com/openssl/openssl/commit/858b5d12b85b0639519d21206c9da7e1bb976a00), [de11641](https://github.com/openssl/openssl/commit/de1164102083730298e4f53eb465c9324aa6a0c0)
- Updated FIPS build instructions to add links to new locations for certificates and security policies.
  ↳ No PR: [e8241fb](https://github.com/openssl/openssl/commit/e8241fb6fe4e73bb337c9068e5a2421948ee40ad)
- Updated QUIC record layer design documentation based on implementation experience.
  ↳ No PR: [48cc4e0](https://github.com/openssl/openssl/commit/48cc4e0c2046624c28d431ac51cdfce1a6e6a597)
- Updated QUIC stream receive buffer design document to add implementation details.
  ↳ No PR: [6f30722](https://github.com/openssl/openssl/commit/6f3072212c2d56cae598bc1d180b2673b3df9be0)
- Clarified the description of the message timeout and total timeout values in the CMP documentation, and corrected the command line option documentation.
  ↳ No PR: [5acd400](https://github.com/openssl/openssl/commit/5acd4007a0646ef1f9d0015ce438b891d1b24a62)
- Update the error code generation document. It is recommended to use make update instead of manually editing openssl.txt.
  ↳ No PR: [2ee2b74](https://github.com/openssl/openssl/commit/2ee2b74cc7b78d2fd3c15dab08adb76fee6249f9)
- Added a new SSL function behavior classification list to the QUIC API overview document and updated the directory structure.
  ↳ No PR: [b795685](https://github.com/openssl/openssl/commit/b7956859cca7f4fe9dfed8e319da1bf5112fe206)
- Minor adjustments to the QUIC API design document, including correcting the macro name, refining the description of quick shutdown behavior, and splitting the flow reset state.
  ↳ No PR: [0a3fb1f](https://github.com/openssl/openssl/commit/0a3fb1fb05ee55c2bb477071b376c3a180eb474b)
- Added QUIC fault injector design document, used to simulate abnormal peer behavior in the test framework.
  ↳ No PR: [55ff8fb](https://github.com/openssl/openssl/commit/55ff8fb4ed4d48cb819ff5ae5d74cc08256e7ed1)
- Updated CHANGES.md to move the dot conversion format parameter change record for EC and SM2 keys from version 3.1 to version 3.0.8.
  ↳ No PR: [f66c127](https://github.com/openssl/openssl/commit/f66c1272f92bed6bc8aa17f6a8956d9e2e5b7798)
- Updated the QUIC I/O architecture design document, supplemented the requirement description, adjusted the chapter structure and improved the discussion of blocking and non-blocking I/O.
  ↳ No PR: [c48cc76](https://github.com/openssl/openssl/commit/c48cc764ed57e49456d5b90a7d885e8af196df78)
- Improve the description text of trusted and untrusted certificate options in CMP application to make it more accurate.
  ↳ No PR: [260878f](https://github.com/openssl/openssl/commit/260878f7aab7b077f4ef9496e3541ec8c19c9d1c)
- Add documentation for static linking and dynamic loading restrictions for HPE NonStop platform.
  ↳ No PR: [7b26252](https://github.com/openssl/openssl/commit/7b2625274f5d5ec90aee522ec4e4f3aa08fa5b70)
- Updated documentation to clarify the behavior of the -S option of the enc command in OpenSSL 3.0: the explicit salt value is no longer automatically prepended when encrypting, and must be provided explicitly again when decrypting.
  ↳ No PR: [a4aa977](https://github.com/openssl/openssl/commit/a4aa977d3a8049d5386dc583e16c17727c712eaa)
- Added QUIC glossary document to define related abbreviations and concepts.
  ↳ No PR: [0af6523](https://github.com/openssl/openssl/commit/0af6523ead9764d7899067b87b9525cc9fc5e19f)
- Add information about ias assembler port to OpenVMS documentation.
  ↳ No PR: [d500f04](https://github.com/openssl/openssl/commit/d500f04400d0acc83fe5270da860764a7d19deee)
- Add OpenSSL OMC's PGP key fingerprint in documentation.
  ↳ No PR: [f925bfe](https://github.com/openssl/openssl/commit/f925bfebbb287321133b9251e72bee869a0f58b4)
- Fixed issue in openssl-genrsa documentation incorrectly listing it as a deprecated command for OpenSSL 3.0.
  ↳ No PR: [4ad2dd4](https://github.com/openssl/openssl/commit/4ad2dd43d0959b850c06c5a681d34aeb78d7c4b9)
- Added a simple blocking TLS client example, and improved the socket connection helper function to support address family parameters and fix resource leaks.
  ↳ No PR: [a5a0c6a](https://github.com/openssl/openssl/commit/a5a0c6a372d2cb9fbcec627e5a338c6f79aa0b16)
- Fixed unnecessary socket closing operation when BIO_lookup_ex fails in TLS client example.
  ↳ No PR: [edd5b9d](https://github.com/openssl/openssl/commit/edd5b9d708d03ce1bdc1cbfc026ccc9183d586ad)
- Modify the issue template to guide users to use GitHub Discussions instead of submitting issues.
  ↳ No PR: [bd38c6b](https://github.com/openssl/openssl/commit/bd38c6b61be589e97495742a33d4e38dfbd63bb0)
- Add salt and info parameter descriptions to the openssl-kdf document, and improve the descriptions of hexkey and hexpass.
  ↳ No PR: [7b2a3a1](https://github.com/openssl/openssl/commit/7b2a3a1e9d5246fb0f2935f152d0daec715f79f9)
- Updated the description of the shutdown process in the QUIC client blocking tutorial, and added instructions for peer sending FIN.
  ↳ No PR: [b7f3d5d](https://github.com/openssl/openssl/commit/b7f3d5d67d17aa1a384811014e79b461ce0e23ca)
- Added final report documentation for the QUIC Demonstration Driven Design (DDD) process.
  ↳ No PR: [277880e](https://github.com/openssl/openssl/commit/277880e754c5a19cc456165560344204373a6b40)
- Added a QUIC non-blocking client example to show how to write a QUIC client using non-blocking sockets.
  ↳ No PR: [b71784f](https://github.com/openssl/openssl/commit/b71784f741d5a90712607f57a45912292fba9573)
- Allow specifying target host and port via command line arguments (QUIC DDD example).
  ↳ No PR: [30302c6](https://github.com/openssl/openssl/commit/30302c66bd47220f6fa65f32bc510d3e679ec3d9)
- Updated API calls in QUIC sample code to use new QUIC client methods, BIO pair creation functions, and added ALPN configuration and dynamic polling flag calculations.
  ↳ No PR: [47eceab](https://github.com/openssl/openssl/commit/47eceab67aef371c00504354939f7b5aff211c60)
- Added ALPN configuration support to QUIC DDD examples, and updated method naming to comply with namespace requirements.
  ↳ No PR: [24e5836](https://github.com/openssl/openssl/commit/24e583619c6f4bb1e7659b6b4f06cea920710688), [b96e5cc](https://github.com/openssl/openssl/commit/b96e5cc60b6c9b4985eab829fd7b1161481da428)
- Add conditional compilation to the QUIC DDD example to support selecting QUIC or TLS client methods based on the USE_QUIC macro.
  ↳ No PR: [37f1210](https://github.com/openssl/openssl/commit/37f12107ee98670bae4b967110370a2bdb171c16), [43f4b8a](https://github.com/openssl/openssl/commit/43f4b8a80ead05900a3a23196c3c4bbb3ed045b1), [70dc50c](https://github.com/openssl/openssl/commit/70dc50c2659f70c47f20e45939b0b43fe9436610)
- Enhanced QUIC non-blocking connection example, added timeout processing, polling descriptor acquisition, internal state advancement function, and added QUIC support (including datagram buffering BIO and ALPN configuration).
  ↳ No PR: [e6ad003](https://github.com/openssl/openssl/commit/e6ad003d73b3021790f486ded07fe038a6d30335), [f379207](https://github.com/openssl/openssl/commit/f3792076597a8e9003f61333e5e9a84818f12529)
- Improve the QUIC non-blocking connection thread example, add conditional compilation to support QUIC mode, and add non-blocking connection management functions and ALPN configuration.
  ↳ No PR: [1ed2d79](https://github.com/openssl/openssl/commit/1ed2d7929a3f3fe86242116b0bc1366d36c3782d), [c276217](https://github.com/openssl/openssl/commit/c276217e4bc9db08f0741882af837355f50c18ab)
- Improve the mem-uv file in the QUIC DDD example, add ALPN configuration, timer callback, write function, and replace the BIO creation function.
  ↳ No PR: [5e73999](https://github.com/openssl/openssl/commit/5e73999803a90126386c78eb68164192ca0d76ce), [74d588c](https://github.com/openssl/openssl/commit/74d588ca1581924e51e9bc72d26d372cdcd269f2)
- Added ED25519 signature demonstration example to show how to use EVP_DigestSign and EVP_DigestVerify for message signing and verification.
  ↳ No PR: [b544c72](https://github.com/openssl/openssl/commit/b544c72f3755c0ea51408d3118821a1ac126c070)
- Updated API implementation status table in QUIC API design document.
  ↳ No PR: [0c125b6](https://github.com/openssl/openssl/commit/0c125b611d55b2d3a79a977614431745f149afbe)
- Added a new design document to explain how to support the use of explicitly obtained signature implementations.
  ↳ No PR: [e8e2b13](https://github.com/openssl/openssl/commit/e8e2b131ca253f9e28c511c8294e27ddbd0b60c6)
- Added QUIC instruction document README-QUIC.md.
  ↳ No PR: [514430c](https://github.com/openssl/openssl/commit/514430c3747292edf864bf9d60b54dc3fed02685)
- Updated README.md to add instructions and related links for DTLS and QUIC protocol support.
  ↳ No PR: [4da702b](https://github.com/openssl/openssl/commit/4da702b61e7a2180eda4de5a922c68a7c0b48f51)
- Update the format, header description and reference links of NEWS.md and CHANGES.md to make them more consistent with the release notes specification.
  ↳ No PR: [5e07ea4](https://github.com/openssl/openssl/commit/5e07ea4f82b5250d64183ddda2b56ebf37df126a), [d330fef](https://github.com/openssl/openssl/commit/d330fef1f1446c968e31803778bc7b3d067c7e99)
- Update the Makefile of the QUIC DDD design document to add TLS and QUIC build variants for each test case.
  ↳ No PR: [be4c344](https://github.com/openssl/openssl/commit/be4c3446a475a8449aa00e550de9de887ec44a70)

### Build/CI
- Fix the shebang of the test script to /usr/bin/env perl, and correct trailing spaces and spelling errors in the documentation and configuration files.
  ↳ No PR: [473664a](https://github.com/openssl/openssl/commit/473664aafdff1f60db99929bdd43c2a9b26d14cd)
- Fix linking errors caused by missing AArch64 specific symbols when building on non-AArch64 Armv8 systems.
  ↳ No PR: [3841d0f](https://github.com/openssl/openssl/commit/3841d0f6f02e1ad3a54beabf1d5395bd1c383254)
- Replaced the Windows 2016 environment in CI with Windows 2022 and added a Perl installation step.
  ↳ No PR: [c87a4dd](https://github.com/openssl/openssl/commit/c87a4dd7a728288da943cb4e2e51150df5dfd1b8)
- Fix the header file protection macro name in include/crypto/dsa.h to avoid duplication with the protection macro in dsaerr.h.
  ↳ No PR: [7db69a3](https://github.com/openssl/openssl/commit/7db69a35f9d2c7ac8029de11115b18a57d341bf5)
- Disable floating point formatting support in UEFI builds to avoid compilation issues; and roll back previous fixes to remove conditional compilation and header file inclusion.
  ↳ No PR: [f59d72f](https://github.com/openssl/openssl/commit/f59d72f027da90edcccad5cc78c94d3099fadecf), [619c9ba](https://github.com/openssl/openssl/commit/619c9bad41d041bab2ac6ba3933d526b48ceee2a)
- Fix build failure for XLC/XLCLANG compiler on AIX: check both _ARCH_PPC64 and __ILP32__ macros in 32-bit builds to avoid false positives.
  ↳ No PR: [cfbb5fc](https://github.com/openssl/openssl/commit/cfbb5fcf4424395a1a23751556ea12c56b80b57e)
- Fix DJGPP compilation issue: add support for MSDOS platform in conditional compilation to provide in_addr_t definition, and add necessary Watt-32 header files in sockets.h.
  ↳ No PR: [b9b211f](https://github.com/openssl/openssl/commit/b9b211fcb6b9068ef1d8729a4971fbe693fd2cde)
- Added test support for GCC 11, GCC 12, Clang 13 and Clang 14 compilers in CI, and upgraded the CI environment to Ubuntu 22.04.
  ↳ No PR: [6332f4c](https://github.com/openssl/openssl/commit/6332f4c4a2c153869b169d250d9736962abe12c6), [712c13c](https://github.com/openssl/openssl/commit/712c13c57b97e2e25ca23048f3ba6f50115cacd7)
- When the child process terminates due to a signal, the signal will now be resent to the own process so that the upper shell can correctly capture and output the information.
  ↳ No PR: [bf16ee4](https://github.com/openssl/openssl/commit/bf16ee4f95c31a66e76056c691f25a0d2b4a39c4)
- Fixed build failure on FreeBSD due to missing data declarations, adjusted variable scope and added skip logic when matching addresses.
  ↳ No PR: [ed82261](https://github.com/openssl/openssl/commit/ed822619f5c051dba7b73c5e2eebe7c790351893)
- Fixed a compilation error in Cygwin builds caused by the missing ipi_spec_dst field in struct in_pktinfo, and skipping the assignment of this field through conditional compilation.
  ↳ No PR: [7f4c657](https://github.com/openssl/openssl/commit/7f4c65749f7e9e687d5aa38e9b3fb548705511b9)
- Enable the usleep-based ossl_sleep() implementation for the djgpp platform to solve the problem of compilation failure caused by circular dependencies.
  ↳ No PR: [6512559](https://github.com/openssl/openssl/commit/651255941c49a5089dfc011f2abd636433da8b82)
- Fixed the problem of compilation failure due to undefined WATT32_NO_OLDIES on the DJGPP platform, which caused conflict in Watt-32 library declaration. Define this macro before including the socket header file.
  ↳ No PR: [8ae74c5](https://github.com/openssl/openssl/commit/8ae74c5bc091e7388c082f090c1fde992c31320f)
- Removed explicit MSVC target architecture name in Windows CI configuration and replaced it with automatic detection by the compiler.
  ↳ No PR: [0747f94](https://github.com/openssl/openssl/commit/0747f94b5f7b7f07f21384507ba1adaea6f99e88)
- Added DJGPP build support for CI cross-compilation workflow.
  ↳ No PR: [f9171a0](https://github.com/openssl/openssl/commit/f9171a06416c6dd9b7b8cd7e4bc08e23a4fab242)
- Enable QUIC support in Windows CI builds.
  ↳ No PR: [7622835](https://github.com/openssl/openssl/commit/76228352d80250801a00d50beeab7dc786336689)
- Added Clang 15 compilation tests in CI configuration, and added steps to install Clang 15 from LLVM PPA for Ubuntu 22.04.
  ↳ No PR: [75ecda9](https://github.com/openssl/openssl/commit/75ecda930e0a961f9605ce090af64d95c98ed161)
- Separate SCTP testing from daily CI workflow into a separate workflow to fix daily build errors.
  ↳ No PR: [41e4f72](https://github.com/openssl/openssl/commit/41e4f72d4cead8caf65f046aea706fe307be1c1e)
- Improved the definition of DSO_MALLOC macro to cover all possible compilation scenarios.
  ↳ No PR: [89d7231](https://github.com/openssl/openssl/commit/89d72311327735ef15c804d2adea84a0fb1bfa0a)
- Make sure SIZE_MAX is defined when defining OSSL_SSIZE_MAX, by including internal/numbers.h to compensate for operating system differences.
  ↳ No PR: [1a298b0](https://github.com/openssl/openssl/commit/1a298b00112e50718acc1fdd40b9bce482112cbf)
- Fixed build issues on NonStop platforms, adjusted conditional compilation header inclusion.
  ↳ No PR: [d861bc0](https://github.com/openssl/openssl/commit/d861bc03ee2ea9945f2a52f04548398ea0b92f94)
- Replace no-shared with no-modules in CI configuration to fix ASAN memory leak detection issue.
  ↳ No PR: [d569654](https://github.com/openssl/openssl/commit/d5696547e46e9ea85fcb7581b9d49c58b7c24eeb)
- Replaced snprintf calls with BIO_snprintf in several source files to fix Windows build issues.
  ↳ No PR: [4a6e5a1](https://github.com/openssl/openssl/commit/4a6e5a11c72a4f3ec082cc065b44906409ad8fae)
- Fallback of previously added cross-compilation CI configuration for RISC-V Zb* and Zk* extensions, as they are not supported by the current QEMU version.
  ↳ No PR: [4597200](https://github.com/openssl/openssl/commit/45972000b44ce0d97adacfddb38f28710b49cfec)
- Fix the build file selection logic and use the correct configuration variables; also update the documentation to explain how to specify a custom build file template through environment variables.
  ↳ No PR: [aa2d7e0](https://github.com/openssl/openssl/commit/aa2d7e0ee15d1b7015479c38f370a25ceec690fc)
- In the argon2 KDF implementation, stdint.h and limits.h were replaced with openssl/e_os2.h and internal/numbers.h respectively to enhance compatibility with old compilers, and the header file inclusion order was adjusted.
  ↳ No PR: [46ce085](https://github.com/openssl/openssl/commit/46ce0854db51e373ab6ed4982431349107cd9b6d)
- Removed CI workflow for FIPS cross-version compatibility checks for 3.0.0 providers with current versions.
  ↳ No PR: [5303608](https://github.com/openssl/openssl/commit/5303608523e40f4328f56755a775f9b5dc0da321)
- Upgrade the actions/setup-python action version used in CI to v4.7.0.
  ↳ No PR: [3ac96c8](https://github.com/openssl/openssl/commit/3ac96c8f715672ff77025d48b5773f5de4f84215), [a1c8edc](https://github.com/openssl/openssl/commit/a1c8edcfc907a84d2595bc52ea7a43f4b33c7339), [dbe3635](https://github.com/openssl/openssl/commit/dbe36351dc3fcb5bd3582075b40d34e0b103b15c)
- Fix OS Zoo CI failure: Update OS matrix, remove obsolete versions and add new versions; install git in Alpine Linux step and remove fuzz/corpora submodule checkout; enable QUIC support in all configurations; optimize workflow configuration.
  ↳ No PR: [ab77026](https://github.com/openssl/openssl/commit/ab77026cecb7fed31e8df99655da1d0f302c4ccc), [467e5c1](https://github.com/openssl/openssl/commit/467e5c1fb7efee2541b8ce7e5bce39f1b4614079), [597ff76](https://github.com/openssl/openssl/commit/597ff76e2886df55c0f56ea31ddd4b15f9606429), [e900942](https://github.com/openssl/openssl/commit/e900942587a18cdd6e3b064d6b21c9ce36a7b640)
- Added no-docs build option, which is used to skip the generation and installation of documentation (such as man pages) during build.
  ↳ No PR: [956b4c7](https://github.com/openssl/openssl/commit/956b4c75dc3f8710bf7b4e1cf01b4ef6d5ca2b45)
- Enable QUIC support by default, update build configuration and documentation, and add related change records.
  ↳ No PR: [8a76420](https://github.com/openssl/openssl/commit/8a7642023884ccfbb17a929698dab8e3fc03cdc9)
- Provide a default definition for SSL_OP_CISCO_ANYCONNECT in the internal header file when it is not defined in the public header file to fix compilation issues.
  ↳ No PR: [f7b2942](https://github.com/openssl/openssl/commit/f7b2942c041ee803557a009a4554760c56484c9d)
- Removed the setting of PTHREAD_MUTEX_NORMAL to resolve build failures caused by this macro being undefined in some glibc configurations.
  ↳ No PR: [e4d8086](https://github.com/openssl/openssl/commit/e4d808652b0a1a19cfe615a6659e65ead0245108)
- Add a warning annotation in the provider cross-version compatibility check workflow to indicate that the PR branch will not be used when a pull request is triggered, but the master branch will be used.
  ↳ No PR: [54e60d2](https://github.com/openssl/openssl/commit/54e60d2a05f86e947dface08e5c20b831be17bf8)
- Added steps to obtain CPU information in multiple CI workflows and continue execution in case of configuration errors in Windows workflows.
  ↳ No PR: [2d374e1](https://github.com/openssl/openssl/commit/2d374e1c665a79af6e0939afe37fcc657af91357), [4ace824](https://github.com/openssl/openssl/commit/4ace824852f385002facf077c5be2815b0780032)
- Fix the warning when compiling test files in GCC 11.2.0 to avoid build failure in strict warning mode.
  ↳ No PR: [37467b2](https://github.com/openssl/openssl/commit/37467b2752f75ce80437120f704452982b7c1998)
- Added explanation in the openssl-fipsinstall document about the situation where the self-test callback may not take effect.
  ↳ No PR: [8d257d0](https://github.com/openssl/openssl/commit/8d257d0dc6ed9d5aeb8366de6be0af01538557ea)
- Document fix for VMS installation issues in CHANGES.md.
  ↳ No PR: [32a3b9b](https://github.com/openssl/openssl/commit/32a3b9b766315a799982ddda82dc40c338b614f7)
- Add description of QUIC support option in installation documentation, disabled by default.
  ↳ No PR: [30b0132](https://github.com/openssl/openssl/commit/30b013291a502dce406708474a60fe58d5803e66)
- Added no-http configuration option to disable HTTP support, and updated related documentation.
  ↳ No PR: [6b1f763](https://github.com/openssl/openssl/commit/6b1f763c698cd9967250dacb1aadca6a6a9e9afe)
- Optimize the build script, move the configuration.h generation logic to configdata.pm, and only update it when the content changes to avoid unnecessary recompilation.
  ↳ No PR: [2522889](https://github.com/openssl/openssl/commit/2522889620446f1e56338367d1b6b028ea952bb4)
- Add fuzz-checker CI workflow in GitHub Actions.
  ↳ No PR: [f92bfdd](https://github.com/openssl/openssl/commit/f92bfddc1d4c4957c57337d7f4192c586cc09a5c)
- Added CI build workflows for multiple legacy operating systems.
  ↳ No PR: [a16ba5f](https://github.com/openssl/openssl/commit/a16ba5f37547eb6ef38a9e623e42b21b35ce47fb)
- Fixed multiple issues in the VMS installation script: corrected version number, pointer size variable reference, and defined logical name OSSL$MODULES.
  ↳ No PR: [bc0ac16](https://github.com/openssl/openssl/commit/bc0ac16417b326abbe295cf359f47922d3b6b05c), [59cf754](https://github.com/openssl/openssl/commit/59cf75435d45a678c81df246c1e8283dc60c4c39), [a3a79ab](https://github.com/openssl/openssl/commit/a3a79ab3221a6484e89cd1321402f40395a05178)
- Added CI workflow for daily Coverity static analysis builds.
  ↳ No PR: [7267769](https://github.com/openssl/openssl/commit/7267769c28fb90d990a9d789093e83699bf4c5a0)
- Added compile option to CI daily check workflow for testing safe_math functionality without compiler built-in overflow check support.
  ↳ No PR: [d362db7](https://github.com/openssl/openssl/commit/d362db7cd1cc46462e0dd3bbccd5c279f2b2ccc8)
- Explicitly specify the Windows CI build environment from windows-latest to windows-2019.
  ↳ No PR: [c37ebbd](https://github.com/openssl/openssl/commit/c37ebbd6f97d23b291c49c4ae2b94c27d732de30)
- Add TLSfuzzer test task in CI workflow.
  ↳ No PR: [e66c417](https://github.com/openssl/openssl/commit/e66c41725f03dae2b295df048312fe6d28729e98)
- Added CI workflow for testing compatibility of FIPS provider and master build.
  ↳ No PR: [3fdf4b9](https://github.com/openssl/openssl/commit/3fdf4b9365900889b54734a348012eae38dedce5)
- Added a task to build and test the FIPS provider using OpenSSL 3.0 from the master branch in the CI workflow, and changed the trigger condition to push events only.
  ↳ No PR: [0c47b8a](https://github.com/openssl/openssl/commit/0c47b8a879c6cd2d553831f930af5ee9df291eca)
- Added oqsprovider external test in CI and updated related test documents.
  ↳ No PR: [fa66f62](https://github.com/openssl/openssl/commit/fa66f62ebbb878bef5c34591efc82b24b9b88dff)
- Upgrade the version of setup-python action in GitHub Actions.
  ↳ No PR: [7176c1a](https://github.com/openssl/openssl/commit/7176c1af1077e1740f9d5e0dfc1028cf8a422792), [43a9e68](https://github.com/openssl/openssl/commit/43a9e682d80d0abe4ffd0c76d18c43cf059a2bcc), [c4edfa2](https://github.com/openssl/openssl/commit/c4edfa220e6d3705a0c6299463c83e61fd5f9d2c)
- Adjusted -DPEDANTIC compilation flag in UBSan build configuration.
  ↳ No PR: [17b94de](https://github.com/openssl/openssl/commit/17b94de3df327e6619e52529e345a340d4a0a100), [83529f0](https://github.com/openssl/openssl/commit/83529f07ca66ec288f1c506a673569b9d8de8368)
- Added CI workflow for testing compatibility of legacy FIPS providers.
  ↳ No PR: [65080a3](https://github.com/openssl/openssl/commit/65080a3e1ebced54af838481e6d40e1c0cb7991e)
- Added Dependabot configuration to automatically keep GitHub Actions versions updated.
  ↳ No PR: [225f94e](https://github.com/openssl/openssl/commit/225f94e818d9f8cb9e272fb9128b4b0ef88a0cbc)
- Fix the fips-label.yml script to adapt to the upgraded API of actions/github-script.
  ↳ No PR: [ada6f05](https://github.com/openssl/openssl/commit/ada6f0533d3299833b27e623ff1bfe3134e8e466)
- Update the include directory path of libFuzzer in fuzz testing CI.
  ↳ No PR: [aef6b82](https://github.com/openssl/openssl/commit/aef6b82882750594b7f8e50ad734d9fe1d70f049)
- Upgraded Coveralls GitHub Action to v2.2.1.
  ↳ No PR: [d0a3b9d](https://github.com/openssl/openssl/commit/d0a3b9d1eb1fc510ec3447b44803bbf5520a0c47), [c4cb151](https://github.com/openssl/openssl/commit/c4cb151b4d19f5f2eb302baafac65e36e4408381), [37ae854](https://github.com/openssl/openssl/commit/37ae8549f03be5ec6478c8f8028668ef477d457d), [0e1b7c8](https://github.com/openssl/openssl/commit/0e1b7c816dcfa4655f443ae5dd8eea4fb42f3493), [ac083de](https://github.com/openssl/openssl/commit/ac083de6513324a5ea9aecbaeccd17ed32716b8e), [bdff325](https://github.com/openssl/openssl/commit/bdff3258310a30e216b9c5620fd2f4eaf4b90438)
- Added multi-branch support in Coveralls workflow.
  ↳ No PR: [e8ca529](https://github.com/openssl/openssl/commit/e8ca529feb0d062ab9f869ac25a37cc4c6b8b329)
- Add make help step to CI workflow.
  ↳ No PR: [d108082](https://github.com/openssl/openssl/commit/d108082377aa5f1c5420ec76ca2e9a5b8fb12a32)
- Added CI workflow for cross-validating compatibility with FIPS and legacy providers.
  ↳ No PR: [3b38f3d](https://github.com/openssl/openssl/commit/3b38f3d86923530be80e73175abfa07ad6dd2d4a)
- Added step to check out fuzz/corpora submodule in CI workflow.
  ↳ No PR: [1ac0464](https://github.com/openssl/openssl/commit/1ac0464d4c9cac7294b8fe739600ffbf8b8c7195)
- Add support for GCC 13 compiler in CI configuration.
  ↳ No PR: [5d16169](https://github.com/openssl/openssl/commit/5d16169964b66ddedd078ce0bc959bdb92a62827)
- Add no-threads build option to CI configuration.
  ↳ No PR: [d4cb369](https://github.com/openssl/openssl/commit/d4cb369f2dae284fa30df7d84616c150f8f03a01)
- Enable QUIC functionality in thread cleaner CI and add related tests.
  ↳ No PR: [5cccc0a](https://github.com/openssl/openssl/commit/5cccc0afdb67a77f9c6eeeba2140748782c011c9)
- Updated OpenSSL version tested in CI workflow to 3.1.1.
  ↳ No PR: [67fc06a](https://github.com/openssl/openssl/commit/67fc06a776b6c1767caae2893e2782301a1936b2)
- Added OpenSSL 3.0.9 to the FIPS version list in CI configuration.
  ↳ No PR: [247f307](https://github.com/openssl/openssl/commit/247f307f7201b5cf7ebfc17758f4cc7ffae14536)
- Reorganize the runchecker job and adjust the triggering conditions of compilation options.
  ↳ No PR: [6497ad5](https://github.com/openssl/openssl/commit/6497ad58588492901838654a36445ad90497ef61)
- Changed CI trigger condition from push to pull_request.
  ↳ No PR: [86051eb](https://github.com/openssl/openssl/commit/86051eb2bb86e3a89e69abfb6419409aa701bcf7)
- Fix wrong build target in demos/encrypt/Makefile.
  ↳ No PR: [67bfdfa](https://github.com/openssl/openssl/commit/67bfdfa17bc4ca8e2b819316299bb82748394c45)
- Add hierarchical Makefile for demo program.
  ↳ No PR: [66f4782](https://github.com/openssl/openssl/commit/66f4782f1452d6fbfab78822b340a99aaeacc2f0)
- Adjust the structure initialization syntax and add compilation options to be compatible with older clang compilers.
  ↳ No PR: [d848520](https://github.com/openssl/openssl/commit/d848520afed1d3a4e4c38307d3bf21e14bff096f)
- Upgrade actions/checkout, actions/setup-python, coverallsapp/github-action, suisei-cn/actions-download-file and actions/github-script in multiple GitHub Actions workflows to the latest version.
  ↳ No PR: [d4231af](https://github.com/openssl/openssl/commit/d4231af60a8d04196b3b873c2fa8638daff36173), [ebce766](https://github.com/openssl/openssl/commit/ebce766bb82b472eb3b796c5ee5ee2c19beb71f5), [f7e7bbc](https://github.com/openssl/openssl/commit/f7e7bbcd7850b96d02dd0f4dd49b3365b320776c), [456e6ca](https://github.com/openssl/openssl/commit/456e6ca5d73972cdb4228e6c5ec9acdf19237308), [9a7a076](https://github.com/openssl/openssl/commit/9a7a076565f8feaae532d35646a0f8171c03c4a5)
- Updated OpenSSL version used in FIPS compliance testing to 3.1.2.
  ↳ No PR: [09d73d7](https://github.com/openssl/openssl/commit/09d73d7ba13b868db96476d265c8d99616ca7809), [8f51b22](https://github.com/openssl/openssl/commit/8f51b2279eda1e0cffb3400c2e5b5c3771f62ea7)
- Fall back the CI trigger condition from pull_request to push, and limit cross-compilation tests to be executed only under push events.
  ↳ No PR: [975f372](https://github.com/openssl/openssl/commit/975f372a6f7ae20e0c4c55a930a6844f2585ee6d)
- Exclude files in the test directory and fuzz directory from coverage reports.
  ↳ No PR: [febe8cf](https://github.com/openssl/openssl/commit/febe8cf4dee9939ee3e5523b6f14d9dc1ec74153)
- Remove no-shared and fuzzing compilation options in Coveralls CI workflow, simplifying configuration.
  ↳ No PR: [4a1bdb0](https://github.com/openssl/openssl/commit/4a1bdb0b7a3d04c1f18a27a10a1aab354eef608b)
- Fixed the calling method of lcov command in coveralls workflow to resolve recent regression issues.
  ↳ No PR: [0782940](https://github.com/openssl/openssl/commit/07829409b6fb40ce4f5c4ec633180280909c732b)
- Correct the directory where opensslwrap.sh is run in the provider-compatibility workflow and add conditional checks.
  ↳ No PR: [2989041](https://github.com/openssl/openssl/commit/29890415487b04b965e47aee21f00a7f6a2e7268)
- Enable multiple non-default compilation options in Windows CI builds and remove duplicate options, verify usability.
  ↳ No PR: [10767fd](https://github.com/openssl/openssl/commit/10767fd9db14b6eedfb0827f9e404c0d4b94424b)
- Remove inappropriate FUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION macro definition from non-fuzzing CI builds.
  ↳ No PR: [d8bf5ea](https://github.com/openssl/openssl/commit/d8bf5ea19d388028004f06f2ffcd40dbd80c1845)
- Added a new fuzz test job, adjusted the static analysis configuration, and removed the fuzz test compilation option.
  ↳ No PR: [27d8827](https://github.com/openssl/openssl/commit/27d8827052ae3c43316582424e9311aea0255bde)
- In the daily check workflow, run the version check command only if openssl has been built.
  ↳ No PR: [bde5411](https://github.com/openssl/openssl/commit/bde541104908421a46268a88c211c02f71343765)
- Skip quic_record, quicapi and quicfaults tests in fuzz builds.
  ↳ No PR: [fac61ea](https://github.com/openssl/openssl/commit/fac61ea4618c83826b51aebf03cbc2bc3ac7b8c8)
- Roll back an unintentional change in the fuzz-checker workflow, removing test configuration items.
  ↳ No PR: [dc1cc3e](https://github.com/openssl/openssl/commit/dc1cc3e4836e4135c1bf0b5bdd14ff86ff62acd6)
- Reorganize CI jobs, move some tasks to run daily or when pushed, adjust configuration options and version information acquisition commands.
  ↳ No PR: [4391906](https://github.com/openssl/openssl/commit/43919068a406de60b6c172eefc171a8ec965b902)

### Maintenance
- Fixed the tab character and indentation formatting issues in the two Perl scripts and unified them to 4 spaces indentation.
  ↳ No PR: [ea0d79d](https://github.com/openssl/openssl/commit/ea0d79db9be9066de350c44c160bd8b17f2be666)
- Fixed the indentation format problem of tls13_hkdf_expand function parameters.
  ↳ No PR: [1b9e467](https://github.com/openssl/openssl/commit/1b9e467887d7852d79270c73cb88383c50460b0a)
- Added Apache 2.0 copyright headers to CI workflow scripts.
  ↳ No PR: [08d8c2d](https://github.com/openssl/openssl/commit/08d8c2d87ec782e95c28ff795e096c2f6f590d63)
- Fixed coding style issues in 113 files, involving multiple modules.
  ↳ No PR: [1287dab](https://github.com/openssl/openssl/commit/1287dabd0b23326be491125698dd982e4ae28887)
- Add missing empty lines in NEWS.md.
  ↳ No PR: [1f8ca9e](https://github.com/openssl/openssl/commit/1f8ca9e3d3fa674da4ab6694cef2f266e6ab0f20)
- Fix coding style issue reported by check-format.pl in apps/cmp.c.
  ↳ No PR: [fd989c7](https://github.com/openssl/openssl/commit/fd989c734dc3f9e15d700ff9ced15125a23d4359)
- Fixed indentation issue in providers/common/provider_util.c.
  ↳ No PR: [1751356](https://github.com/openssl/openssl/commit/1751356267f64d5db8824cf4ff5b3496e15972da)
- Updated .gitignore to ignore test generated files /test/evp_pkey_ctx_new_from_name.
  ↳ No PR: [ac23650](https://github.com/openssl/openssl/commit/ac23650c1e53658227436aecc8de03a7ac3d1b9a)
- Fixed the indentation problem of code format for BLOCK_CIPHER_custom macro call.
  ↳ No PR: [1c5a4e3](https://github.com/openssl/openssl/commit/1c5a4e3b5e05494876ebba9d8272d2cbca1e20a3)
- Fixed spelling errors and terminology inconsistencies in multiple files, including changing fall thru to fall through, host name to hostname, time zone to timezone, etc., to align with the LDP standard.
  ↳ No PR: [c734058](https://github.com/openssl/openssl/commit/c7340583097a80a4fe42bacea745b2bbaa6d16db), [9929c81](https://github.com/openssl/openssl/commit/9929c81702381bff54f833d6fe0a3304f4e2b635)
- Improve the output format of openssl list command, add a blank line at the end of each command and algorithm list to make the output clearer.
  ↳ No PR: [ec1d597](https://github.com/openssl/openssl/commit/ec1d5970be596daed15a3fa723cfa2ac726b0dba)
- Add TODO comments in the QUIC implementation to mark currently no-op sections as well as protocol errors and cache optimizations that need to be handled in the future.
  ↳ No PR: [c8b3fdc](https://github.com/openssl/openssl/commit/c8b3fdc2e4833b065c0f7f0ff6ab771c6ff6b1a9)
- Fix style issues in QUIC code, including adding blank lines and adjusting preprocessor directive indentation.
  ↳ No PR: [d50e750](https://github.com/openssl/openssl/commit/d50e750e13f5a8f615da56ee73ddbd1a23007ebe)
- Add TODO comment about CCM support in QUIC implementation.
  ↳ No PR: [c41c7ee](https://github.com/openssl/openssl/commit/c41c7ee976aad76f63ce42c1ea883e4d075e2f0e)
- Make style fixes to the QUIC connection state machine code, including indentation adjustment, comment updates and conditional judgment standardization.
  ↳ No PR: [75b2920](https://github.com/openssl/openssl/commit/75b2920a219f9ec222e663ec5d2bb6101dc612f9)
- Add missing copyright header to crypto/bn/rsa_sup_mul.c file.
  ↳ No PR: [93b0a1e](https://github.com/openssl/openssl/commit/93b0a1ea614f9ce3931373fd3d1d1af04795e6d7)
- Adjust the code format and fix a spelling error.
  ↳ No PR: [f42d6b7](https://github.com/openssl/openssl/commit/f42d6b7ae62a2b2914b144153af56096f9b4a6d5)
- Fixed comment punctuation errors in QUIC test files.
  ↳ No PR: [03fa512](https://github.com/openssl/openssl/commit/03fa5127ded6ba0dc9f178090eca0dbe70769c0e)
- Add a comment in the do_X509_sign() function to indicate that RFC 5280 compliance measures may be considered in the future.
  ↳ No PR: [586b540](https://github.com/openssl/openssl/commit/586b5407d6138ce23416d4101168ab0c2b1651b6)
- Add comments to cert_response and initial_certreq functions, mark unused parameters, and adjust status constants to enhance readability.
  ↳ No PR: [afe7a43](https://github.com/openssl/openssl/commit/afe7a4311d7c0350bc65764b6f642149099a3e0a)
- Update the .gitignore file to add ignore entries related to LSP support to prevent developers from accidentally committing these files.
  ↳ No PR: [9e87e4e](https://github.com/openssl/openssl/commit/9e87e4e8ac2c5c75eae0ef1d4208e2aa12ff57dc)
- Add note about RFC 9000 section 10.2 persistence time in QUIC channel termination status.
  ↳ No PR: [a441d08](https://github.com/openssl/openssl/commit/a441d08b1b10f259c8fa9eb9cd836ffe19b23b0f)
- Fixed the indentation format problem of function code in QUIC server.
  ↳ No PR: [f36504c](https://github.com/openssl/openssl/commit/f36504cc393e10abd35a8b6a25d8965cddcacf98)
- Make maintenance improvements to the noisy dgram BIO test assistant, including adding optional debug output, removing unused redundant read and write functions, and unifying terminology naming.
  ↳ No PR: [fbfcc3f](https://github.com/openssl/openssl/commit/fbfcc3fe3458c50a11aa414a1e499a2eee0eb2e9), [c29b13a](https://github.com/openssl/openssl/commit/c29b13a7356432a0f177dd838afbec963f1d6212), [523c5a0](https://github.com/openssl/openssl/commit/523c5a06c590b7f2950043a6b8308c3f3e49cb51)
- Update CHANGES.md and NEWS.md files to synchronize version change records and prepare for the OpenSSL 3.2.0 release.
  ↳ [#22805](https://github.com/openssl/openssl/pull/22805): [cf28777](https://github.com/openssl/openssl/commit/cf2877791ce7508684109664f467c9e40987692f) | No PR: [2d0d3ed](https://github.com/openssl/openssl/commit/2d0d3edb04ab0fa53e30e3cbdd114de9933d5361)
- Add check on OPENSSL_strdup return value to avoid null pointer dereference.
  ↳ No PR: [dc7e42c](https://github.com/openssl/openssl/commit/dc7e42c6a12637bae1660561d3f4cef039001475), [b9648f3](https://github.com/openssl/openssl/commit/b9648f31a4917b8594caebda3e6d8d313514fe24), [3e04415](https://github.com/openssl/openssl/commit/3e0441520b9a349dc50662919ea18f03dfc0d624)
- Add checks on the return values of functions such as EVP_MD_fetch, OSSL_PARAM_BLD_new and BIO_new.
  ↳ No PR: [04e3ab6](https://github.com/openssl/openssl/commit/04e3ab64d58bb43efc4392d12c607bb4b5a2c562), [0da3b39](https://github.com/openssl/openssl/commit/0da3b39af3d961486758262ca71d2135d7013048), [fa17f5c](https://github.com/openssl/openssl/commit/fa17f5c98783949a702ab9bb1e780c4e9f15566b)
- Performed multiple code cleanups, including avoiding empty statements, deleting duplicate declarations, adjusting variable declaration positions and repairing redundant semicolons.
  ↳ No PR: [a09a342](https://github.com/openssl/openssl/commit/a09a342ffb459d0913954111b7802815e9a3481a), [7d7a8d4](https://github.com/openssl/openssl/commit/7d7a8d416529c4d560fbd5ca73bb3b24383a419c), [2437832](https://github.com/openssl/openssl/commit/2437832be1d0e11e6a601c19a18d7247aff22f0e), [1e33172](https://github.com/openssl/openssl/commit/1e3317278e4890e812a032b39c7c9dc43ca01458)
- Add error handling in o_names_init, but may introduce minor memory leaks.
  ↳ No PR: [c50bf14](https://github.com/openssl/openssl/commit/c50bf14450f3cd242f2211ca7e500191053d8050)
- Optimize KTLS related function calls, cache BIO_get_ktls_send and BIO_get_ktls_recv results, and avoid repeated calls.
  ↳ No PR: [ad2f4cd](https://github.com/openssl/openssl/commit/ad2f4cdcb1875b16e0f5581ab1ee0bae572c68e6)
- Abstract the certificate extension and policy parameters in the CA.pl script into variables to improve maintainability.
  ↳ No PR: [3066cf2](https://github.com/openssl/openssl/commit/3066cf2614d22182ae0dafd4557a96ab6b698d4f)
- Adjust the CMP server logging order to advance request type logging before message verification.
  ↳ No PR: [ae8ff10](https://github.com/openssl/openssl/commit/ae8ff109c1d80399a6a1c9f50aa37381bc3a1c5f)
- Exclude flags in reason codes from error string fallback printing.
  ↳ No PR: [9350aaa](https://github.com/openssl/openssl/commit/9350aaa41db8fcb0b55dadbd5fbe807ef5288557)
- In several KDF implementations, the length field is reset after clearing the buffer to avoid using the freed buffer length.
  ↳ No PR: [d2217c8](https://github.com/openssl/openssl/commit/d2217c88df6e65c756013417e5ee4f470dd12470)
- PVK decoder now prompts for PVK passphrase instead of PEM passphrase.
  ↳ No PR: [28257d6](https://github.com/openssl/openssl/commit/28257d60577932e66934096d0ee8a5dfaca1191e)
- Add checks for blank lines inside and after local declarations to the check_format.pl script, and update the test file.
  ↳ No PR: [d8662f2](https://github.com/openssl/openssl/commit/d8662f2f8716645164a9d4d8795a9c353fe315fb)
- Clean up redundant semicolons and empty statements in code.
  ↳ No PR: [e52698f](https://github.com/openssl/openssl/commit/e52698f9e33d77419dca827774e5d0bc1815100d), [14951ef](https://github.com/openssl/openssl/commit/14951ef01f9b54d804baf2fabdf0a715c630827b)
- Fixed compiler false positive warnings to avoid false warnings in GCC12 and VS2022.
  ↳ No PR: [649999d](https://github.com/openssl/openssl/commit/649999dc57419ddd9329f7062b048dee5ecd9306), [b84c6e8](https://github.com/openssl/openssl/commit/b84c6e86dd8ca88444207080808d1d598856041f)
- Add return value checks for multiple functions to enhance code robustness.
  ↳ No PR: [4dd085c](https://github.com/openssl/openssl/commit/4dd085c03a885580cc945f71187131ea7fb39b70), [aefbcde](https://github.com/openssl/openssl/commit/aefbcde29166caf851cf388361d70fd0dcf17d87), [c920020](https://github.com/openssl/openssl/commit/c920020f0bb13f0d2bf0fcad5c7ee63458b633b4), [366a162](https://github.com/openssl/openssl/commit/366a16263959c0b6599f0b9ec18124d75560c6ef), [5266af8](https://github.com/openssl/openssl/commit/5266af87379aecb0ae6036dee88c1a0b8083a432), [02119fa](https://github.com/openssl/openssl/commit/02119faee397565525151eb2ce39c424d129d287)
- Fix multiple uninitialized variables and integer overflow issues reported by the Coverity static analysis tool.
  ↳ No PR: [a0238b7](https://github.com/openssl/openssl/commit/a0238b7ed87998c48b1c92bad7fa82dcbba507f9), [81487b6](https://github.com/openssl/openssl/commit/81487b65b9eb8148471e729b8c1959521d62c69e), [4e720f1](https://github.com/openssl/openssl/commit/4e720f12fade8d433e5a0eb3ead9017193dac6e7), [2e3e9b4](https://github.com/openssl/openssl/commit/2e3e9b4887b5077b949cdee490ecc1526b2c5509), [70cd9a5](https://github.com/openssl/openssl/commit/70cd9a51911e9a4e2f24e29ddd84fa9fcb778b63)
- Add multiple inclusion protection to header files and unify the indentation format of internal preprocessing directives.
  ↳ No PR: [3d27ac8](https://github.com/openssl/openssl/commit/3d27ac8d92ef89c202b518cf6c4e15477eb594b2)
- Unify the checking method of X509_TRUST_get_by_id() return value.
  ↳ No PR: [7b3041e](https://github.com/openssl/openssl/commit/7b3041eba1c6e177eede0d6311d53a6b9ff58051)
- Allow export of additional parameters for EC keys when only additional parameters are selected, no longer requiring key pair selection at the same time.
  ↳ No PR: [e20af37](https://github.com/openssl/openssl/commit/e20af37d063514c27567c64e975fa5b3208707a9)
- Add assertions and error handling in property definition cache to avoid potential crashes.
  ↳ No PR: [5f4b3db](https://github.com/openssl/openssl/commit/5f4b3db624a83b812f23412e698ffd9c4284f87a)
- Improve checking for invalid saltlen in DER writer, add range checking and add explicit type conversion.
  ↳ No PR: [08f876d](https://github.com/openssl/openssl/commit/08f876d0dea184b071a5aded4c55317e5a63c80e)
- Clean up system call parameter types in bss_dgram.c, avoid using union as parameter, and add error checking.
  ↳ No PR: [8e949b3](https://github.com/openssl/openssl/commit/8e949b35d396005d63f3a2c944c36a1c94e41019), [8eca686](https://github.com/openssl/openssl/commit/8eca6864e080c9b8197fec81cd6f327be43bb14c)
- Add stdlib.h header file inclusion for priority_queue.h.
  ↳ No PR: [924c814](https://github.com/openssl/openssl/commit/924c814a8a6a9dcfeb8e366705c6ef5f078d0628)
- Fixed coding style and format issues of multiple functions in cms_sd.c, and adjusted variable declarations and error codes.
  ↳ No PR: [8fc120b](https://github.com/openssl/openssl/commit/8fc120bda21b7ebe24db2283aa501ac0c396c026)
- Removed unused GCM implementations (8-bit and 4bit) and related code.
  ↳ No PR: [a8b5128](https://github.com/openssl/openssl/commit/a8b5128fd724bc23f7454d64e401d15129634a01), [7da952b](https://github.com/openssl/openssl/commit/7da952bcc54604141ea8ed40ec5ed1fd2f74cc25)
- Update .gitignore and add the file /test/timing_load_creds generated by the test to the ignore list.
  ↳ No PR: [6a92550](https://github.com/openssl/openssl/commit/6a9255054b345026bc847ddad72f2da93f30ce4c)
- Remove unused dtls1_bitmap.c file.
  ↳ No PR: [3d62389](https://github.com/openssl/openssl/commit/3d623896eb50f5b15d3ef8f53b9f1e5c7546695a)
- Add comments to PKCS7 header files and clean up constant usage and parameter naming in CMS and PKCS7 code.
  ↳ No PR: [f69ec4b](https://github.com/openssl/openssl/commit/f69ec4b484c08e67e863707eab4af4a4e6f4fc95)
- Fix the negative return value problem found by Coverity: add validity check for the return value of EVP_MD_get_size in tls13_update_key.
  ↳ No PR: [1d15370](https://github.com/openssl/openssl/commit/1d1537067304b8c8d87b2df393363b40370ad640)
- Clean up legacy TODO comments in ssl/record/rec_layer_s3.c, remove obsolete code and update related comments.
  ↳ No PR: [c6d5f34](https://github.com/openssl/openssl/commit/c6d5f343336532a7aba4368099b0631a457194a6)
- When the TLS 1.3 key is updated, new logging of the updated traffic key is added.
  ↳ No PR: [2f7e61b](https://github.com/openssl/openssl/commit/2f7e61b8b21ed472a3667b8922843851f94a3d93)
- Remove explicit zero-initialization of static constant variable zero_addr to be compatible with older versions of Clang compiler.
  ↳ No PR: [31fbf11](https://github.com/openssl/openssl/commit/31fbf119f396cf67e808cb95e28302dbe45174cb)
- Removed unused local variable totlen in tls_write_records_default() function.
  ↳ No PR: [3c9ffd0](https://github.com/openssl/openssl/commit/3c9ffd0273b7e1e1e425be03c5e8a58ef07c4625)
- Fix printf format warnings caused by type mismatch, add explicit type conversions in multiple functions.
  ↳ No PR: [1555c86](https://github.com/openssl/openssl/commit/1555c86e5f7e3c46b4f696ed665c2f988976b81f)
- Fix compilation warning triggered by socklen_t being a signed type on Watt32 platform: Explicitly convert socklen_t in assert comparison to size_t.
  ↳ No PR: [71faab7](https://github.com/openssl/openssl/commit/71faab72b8b49819d8bcf065b039d1d840e8b76c)
- Skip checking for negative timeval values on DJGPP platforms to avoid compilation warnings due to tv_sec being an unsigned type.
  ↳ No PR: [d8bcd64](https://github.com/openssl/openssl/commit/d8bcd64170e8b6fb66da293a95ff21b25d1a357e)
- Fixed compilation warning of unused variables in DJGPP environment.
  ↳ No PR: [b9179ae](https://github.com/openssl/openssl/commit/b9179ae5552ab59fa46bad5721125a84c76f8ab4)
- Fix loop variable type issue reported by Coverity, change loop index to signed type.
  ↳ No PR: [9ab57f2](https://github.com/openssl/openssl/commit/9ab57f29c78d8d69b6ba9c579521594d7170ca44)
- Removed TODO comments and temporary code that are no longer needed after DTLS migration.
  ↳ No PR: [faa3e66](https://github.com/openssl/openssl/commit/faa3e66c27a5e88f048f3ed30cfca297eda13eb6)
- Removed unused ossl_rand_pool_add_additional_data() function and its auxiliary functions.
  ↳ No PR: [da7db83](https://github.com/openssl/openssl/commit/da7db83cc44d2c8761e9074caf8befd443ea8be8)
- Add a virtual handshake layer for QUIC for prototyping and disable related compiler warnings.
  ↳ No PR: [f71ae05](https://github.com/openssl/openssl/commit/f71ae05a4d22d52780fc7cfc7e60710b74fd3dd7)
- Update versions of multiple Actions in GitHub Actions workflows based on Dependabot recommendations.
  ↳ No PR: [4ff6634](https://github.com/openssl/openssl/commit/4ff66347f0ab3c054c5622dd862f36c731c889ed)
- Remove unused ALIGN64 macro definition in rsaz_exp_x2.c.
  ↳ No PR: [4b65d79](https://github.com/openssl/openssl/commit/4b65d79d7132d6e46bfb385a76082f6502ef617b)
- Removed unused header include from pkcs7 module.
  ↳ No PR: [2a5c0d9](https://github.com/openssl/openssl/commit/2a5c0d93cfe65b5fbb9bd91ec62371256eb26e12)
- Improved HTTP server diagnostic information, optimized log output and error handling.
  ↳ No PR: [4603242](https://github.com/openssl/openssl/commit/46032426e42238ca8662b98752f9bc8d44512f29)
- Remove redundant __NR_getrandom macro definition and add relevant comments.
  ↳ No PR: [c8a9b26](https://github.com/openssl/openssl/commit/c8a9b26d6ed7a62d26a013c21e62ba4a0a2d6dd1)
- Remove unused macro definitions in rc2_local.h and rc5_local.h.
  ↳ No PR: [bb4a32b](https://github.com/openssl/openssl/commit/bb4a32ba24ab186aba0b45150934d9eae68d78d5)
- Removed unused macros in cast_local.h and des_local.h.
  ↳ No PR: [2fb5fa4](https://github.com/openssl/openssl/commit/2fb5fa468613a3472d148deaf0991fa7e78c83a6)
- Improve diagnostic information in load_key_certs_crls function when expected content is not found.
  ↳ No PR: [fedab10](https://github.com/openssl/openssl/commit/fedab100a4b8f4c3b81de632f29c159fb46ac3f2)
- Adjust write buffer allocation size to reserve enough space for explicit IV.
  ↳ No PR: [626618a](https://github.com/openssl/openssl/commit/626618a09d057db6eee34c3fdd81525b9e3cbc68)
- Ensure QRX and QTX are associated to the channel's libctx on initialization.
  ↳ No PR: [c2212dc](https://github.com/openssl/openssl/commit/c2212dc19eb280e22bda7d0538b23eef0be040e9)
- Ignore the SIGPIPE signal and add SSL_read error message printing when the client suddenly disconnects.
  ↳ No PR: [f309b3f](https://github.com/openssl/openssl/commit/f309b3f6087db6c83126f8f227f1fc4984cf24b1)
- Replaced strstr with strchr in apps/s_client.c to improve code accuracy.
  ↳ No PR: [a80840c](https://github.com/openssl/openssl/commit/a80840c663e3409203b0235764e53d8624f74cb8)
- Remove unused variables in ring_buf_push function to eliminate clang 16 compilation warnings.
  ↳ No PR: [abbbc06](https://github.com/openssl/openssl/commit/abbbc06a94cafa7e212bfe7dcbf818ac33d986d3)
- Improved warning messages when using options in CMP client.
  ↳ No PR: [6ed117b](https://github.com/openssl/openssl/commit/6ed117b32c40992d3211b65cfe1b9aec23652a7d)
- Clarify the meaning of is_inflight field in QUIC ACKM and add validation.
  ↳ No PR: [85bbef2](https://github.com/openssl/openssl/commit/85bbef270c1d15ec34e152c13f41ec0c298f5459)
- QUIC skips the stream being reset when retransmitting to avoid meaningless retransmissions.
  ↳ No PR: [c407d5e](https://github.com/openssl/openssl/commit/c407d5e568ee0755d0c96c09a832af9760349c00)
- Add MemorySanitizer false positive circumvention for get_random_bytes function.
  ↳ No PR: [2c4124a](https://github.com/openssl/openssl/commit/2c4124a3a1373036141ee8f07fdd5806cab12aeb)
- Removed unused variable assignments and fixed issues reported by Coverity.
  ↳ No PR: [4bcbf8d](https://github.com/openssl/openssl/commit/4bcbf8d4445e763857563d9ca016972e095c622d)
- Optimize the structure initialization method in s390xcap.c to prevent old compilers from copying read-only data.
  ↳ No PR: [32d2b5f](https://github.com/openssl/openssl/commit/32d2b5fdd93ceee192abefb3fd0ce8f9a1b329c2)
- Fix uint64_t format specifier incompatibility in QUIC trace and test code.
  ↳ No PR: [0cea6df](https://github.com/openssl/openssl/commit/0cea6df239fc5c5c5902b4c660305bf953f03eb1)
- Fixed comments and spelling errors in QUIC internal code, improved address family checking logic, and fixed cleanup of wrong paths in tests.
  ↳ No PR: [96b7df6](https://github.com/openssl/openssl/commit/96b7df60b3e54641c6046fea31c7a5cb535c2eeb)
- Replaced the stateless reset token array size magic number in QUIC internal header files with a defined constant.
  ↳ No PR: [029ddd1](https://github.com/openssl/openssl/commit/029ddd1eadd3218017de5e6256363d09b7e015f8)
- Added APPLINK_NO_INCLUDES macro to applink.c to suppress internal include preprocessor directives.
  ↳ No PR: [fafb7d3](https://github.com/openssl/openssl/commit/fafb7d30038678bffba739eaa933b926d2ee194f)
- Add comments to internal flags stating their reserved use.
  ↳ No PR: [d5c3f4b](https://github.com/openssl/openssl/commit/d5c3f4b2dba0202c589d1d733e88e392794dce41)
- Remove unused Appveyor profiles.
  ↳ No PR: [8ac32e1](https://github.com/openssl/openssl/commit/8ac32e1e1b1a786366333acf897d332339610e6b)
- Remove duplicate trace_data_stack variable definition in apps/openssl.c.
  ↳ No PR: [46ea548](https://github.com/openssl/openssl/commit/46ea5486f34ff8c2fed67674da2a363bbd66691b)
- Adjust the order of header file inclusion in quictestlib.c and add e_os.h to ensure symbol definition consistency.
  ↳ No PR: [b07107e](https://github.com/openssl/openssl/commit/b07107e31149bf870bc1ae17e59444859fe4e23a)
- Adjust QUIC channel encryption buffer initial size to 16384 bytes.
  ↳ No PR: [29f6338](https://github.com/openssl/openssl/commit/29f633840df49f29e71a57cc9682d9f3703bfe3b)
- In QUIC channels, update ping deadline when there is no congestion control budget to avoid busy loops.
  ↳ No PR: [c7ed5e4](https://github.com/openssl/openssl/commit/c7ed5e4697a71012e0a2d9dd5eaf997754ae5156)
- Set more explicit error cause strings for duplicate transport parameter extensions in QUIC channels.
  ↳ No PR: [3c7c486](https://github.com/openssl/openssl/commit/3c7c4866464cfb872b91ba204e3c64d4da9e2fdf)
- Fixed false positives in the check-format.pl script regarding constants on the left side of comparison operators, scientific notation, spaces before semicolons and spaces after brackets.
  ↳ No PR: [15ae69f](https://github.com/openssl/openssl/commit/15ae69fa7bc0f367edded19bc48e6d9a5ce8d547), [d45c0e1](https://github.com/openssl/openssl/commit/d45c0e1a5e89f01d83f6059c788524e901a11604), [c30bc4e](https://github.com/openssl/openssl/commit/c30bc4e2093f47a37736944da548653bc08d774d)
- Fix null pointer check for ossl_ffc_name_to_dh_named_group when parameter is NULL.
  ↳ No PR: [3b53f88](https://github.com/openssl/openssl/commit/3b53f88c008d288e86d2bbdc0c4e2d16c29fcee8)
- Adjust the order of notification operations in CRL time check and move it to be executed after no time check.
  ↳ No PR: [c92c3df](https://github.com/openssl/openssl/commit/c92c3dfb99485eb2cfb840e92bd0ece8cdd72d0c)
- Fixed the unexpected control flow problem caused by continue in do...while(0) loop in apps/s_client.c, use for(;;) loop instead and add break.
  ↳ No PR: [6799fc2](https://github.com/openssl/openssl/commit/6799fc2409823939cde5b4a0da909e16ef78d3a8)
- Update the ping deadline when receiving data packets to ensure accurate timeout judgment.
  ↳ No PR: [8fd32a0](https://github.com/openssl/openssl/commit/8fd32a0eda994527668a1e19a29ca9c85b4a35d8)
- Fixed the issue where the amount of sent data was not correctly recorded during retry, ensuring that the sent byte count can be restored after retrying.
  ↳ No PR: [b9b9f48](https://github.com/openssl/openssl/commit/b9b9f4886f87abd39535721243d4297fd45e558a)
- Fix GCC build warnings, avoid unused variables through conditional compilation, and update configuration loading functions.
  ↳ No PR: [8ae080b](https://github.com/openssl/openssl/commit/8ae080bf851a25187b93803b8c6a93e82dd97437)
- Fixed the ambiguity problem of kill function parameters in Perl script, and added parentheses to ensure that the parameters are passed correctly.
  ↳ No PR: [ef6d6e4](https://github.com/openssl/openssl/commit/ef6d6e452dc57ef4a55d7a6ec0693be650009bb5)
- Updated Dependabot configuration to add CLA: trivial tags, tags and reviewer settings for automatic dependency updates.
  ↳ No PR: [f973077](https://github.com/openssl/openssl/commit/f9730779eb4f7896f54627c8364af3f30904fe2b)

### Others
- Allow printing the modulus of RSA-PSS keys in req and x509 commands.
  ↳ No PR: [e4cdcb8](https://github.com/openssl/openssl/commit/e4cdcb8bc44250aa4e0893dc4a7d64668f0fb949)
- Added comments explaining the cause of short sleeps in QUIC multi-stream tests.
  ↳ No PR: [025535e](https://github.com/openssl/openssl/commit/025535ecd11bdebd8eb28ed4f0f6b509b1b54577)
- Clear the owner pointer when copying an SSL session, and add tests accordingly.
  ↳ No PR: [9fdf9a4](https://github.com/openssl/openssl/commit/9fdf9a44bbe3827fe653165a07281ccae8ab0947)
- Fixed the problem of inconsistency between data flag and data pointer in error state.
  ↳ No PR: [94300d8](https://github.com/openssl/openssl/commit/94300d8de224e2135e75439e6b9c63eb7ad61fdf)
- Add OpenSSL copyright header to demos/http3 sample files.
  ↳ No PR: [444d18f](https://github.com/openssl/openssl/commit/444d18fc7a3d2ddaef9ed51d90cad06a97af4939)
- Fixed code format issues in multiple source files.
  ↳ No PR: [1a68a3e](https://github.com/openssl/openssl/commit/1a68a3e42142a2c188f4b69c7337438c89502143), [d4ee345](https://github.com/openssl/openssl/commit/d4ee3456e98b1137a1ba013cf01f1052891dd3db), [0f4be8a](https://github.com/openssl/openssl/commit/0f4be8a14a2bcb8a92cf78d94d157152c0a03d88), [016a80d](https://github.com/openssl/openssl/commit/016a80dcf441189ac6d84533f1951506116a3b98), [da57c0e](https://github.com/openssl/openssl/commit/da57c0eaf22c390f9b38c42ca1bd7daca4effd2f), [6935101](https://github.com/openssl/openssl/commit/6935101354e1ebcb43aa8afb158603f94c0f9bc6), [b49cafd](https://github.com/openssl/openssl/commit/b49cafd86b295aa5e177d6c1368b06a1202ec2b3)
- Updated documentation and release notes, corrected IPv6 loopback address example.
  ↳ No PR: [7542bdb](https://github.com/openssl/openssl/commit/7542bdbff70623e1f116a15b6c44fe76014c03cd), [7a12e7a](https://github.com/openssl/openssl/commit/7a12e7af0fccb51b0a569a1b27de5cd877c966b1)
- Adjust internal error handling, including null pointer checking, resource release and buffer size handling.
  ↳ No PR: [e741463](https://github.com/openssl/openssl/commit/e7414634a59aa61c7917193a31382ced95d40eeb), [ab547fc](https://github.com/openssl/openssl/commit/ab547fc005307ecf48451638e947cdabca147159), [1b4d996](https://github.com/openssl/openssl/commit/1b4d9967a24154f1dc00f471eb843203ec7bb7d4), [680827a](https://github.com/openssl/openssl/commit/680827a15f12c3b37a6335fcb992555cf300730e)
- Fixed typos in multiple comments.
  ↳ No PR: [91b968b](https://github.com/openssl/openssl/commit/91b968bc8e4125a1202e7955961f8e7dfcd17513), [105af0a](https://github.com/openssl/openssl/commit/105af0ad923a665ca5fee296b52dbf34b524a2aa), [44fde44](https://github.com/openssl/openssl/commit/44fde441937fc8db8ea6a7ac2e7c683ad9d5f8e0), [07c5465](https://github.com/openssl/openssl/commit/07c5465e9855cc485c4a84da8a4251a843bec258)
- Update and add comments in multiple files to improve accuracy.
  ↳ No PR: [d040a1b](https://github.com/openssl/openssl/commit/d040a1b9a028e89f0a33b36fb99f0151d2fdd4c3), [1d8f18d](https://github.com/openssl/openssl/commit/1d8f18dce1c8ba99693dfaeb1696d625d9f4b7e0), [7c7c356](https://github.com/openssl/openssl/commit/7c7c3561ebfb26799e2d12b5f9f0826731a6a06b)
- Update and fix copyright information and licenses of multiple files.
  ↳ No PR: [a8d9bd8](https://github.com/openssl/openssl/commit/a8d9bd8114510d3a1708da3922f07e7f707674bc), [0088ef4](https://github.com/openssl/openssl/commit/0088ef48c3e7d9c68e5b3c75cb077da601d22f37), [fd84b9c](https://github.com/openssl/openssl/commit/fd84b9c3e94be1771d1b34ad857081f7693318aa), [9d987de](https://github.com/openssl/openssl/commit/9d987de3aabe54e65a55649a61953966f33b070b)
- Remove trailing whitespace in documentation and demo code.
  ↳ No PR: [57cd10d](https://github.com/openssl/openssl/commit/57cd10dd1ee9659b94cfa8a8e74c5a151632975e), [b461aff](https://github.com/openssl/openssl/commit/b461aff257e57b8ba8e72667078fdf6d5047bc91)
- Added chapter titles and placeholders for OpenSSL 3.1 version.
  ↳ No PR: [2727265](https://github.com/openssl/openssl/commit/2727265752c66690d79c4cbe6956746977b1df4c)
- Update manual to reference the IANA TLS cipher suite registry.
  ↳ No PR: [0865200](https://github.com/openssl/openssl/commit/0865200fe59e7b18fbef07077897e09ab39741dc)
- Modify optional parameter notation format in installation documentation.
  ↳ No PR: [a4ffb33](https://github.com/openssl/openssl/commit/a4ffb33ea8b7bcf04b8181dafce7ac512081d0ab)
- Fixed file name error in README document.
  ↳ No PR: [8b6a7da](https://github.com/openssl/openssl/commit/8b6a7da304d4fdd0de38ddd6037d8a02491e3e4e)
- Update CHANGES.md to document default SSL/TLS security level changes.
  ↳ No PR: [a4c4090](https://github.com/openssl/openssl/commit/a4c4090c21058a75e8bf1ffcc469b6d9755c55ce)
- Fix Markdown link in SUPPORT.md.
  ↳ No PR: [3410f10](https://github.com/openssl/openssl/commit/3410f1045af1913c89f5dc06ad4998a60e57fd90)
- Updated SSL error strings to use a more generic protocol description.
  ↳ No PR: [81b741f](https://github.com/openssl/openssl/commit/81b741f68984b2620166d0d6271fbd946bab9e7f)
- Updated file path references in comments to reflect actual locations.
  ↳ No PR: [1cc94e2](https://github.com/openssl/openssl/commit/1cc94e2fa7fd1d5c24ad4cc01f363ff9ba5a4f13)
- Fixed multiple typos in code, tests and documentation.
  ↳ No PR: [7585073](https://github.com/openssl/openssl/commit/7585073892af9cffd28b7b5872c2b102b99af807), [ef9909f](https://github.com/openssl/openssl/commit/ef9909f3c6471ba39be1e3d18a366044cbf30a19), [930a7bd](https://github.com/openssl/openssl/commit/930a7bd9128fd5e184c8a60153de5b8a16159b05), [1ab8b7c](https://github.com/openssl/openssl/commit/1ab8b7cd3bef5ae3bcb516a1c2f2fff4abd63c5b)
- Fixed multiple errors in the documentation, including dates, links, parameter names, syntax and contributor attribution.
  ↳ No PR: [e0d00d7](https://github.com/openssl/openssl/commit/e0d00d79ddce5d145569c9e104068d3728c1e86d), [0bc2fda](https://github.com/openssl/openssl/commit/0bc2fda3d3b76bd07243aef3eb7f824da3820b2d), [31ff363](https://github.com/openssl/openssl/commit/31ff3635371b51c8180838ec228c164aec3774b6), [cac2507](https://github.com/openssl/openssl/commit/cac250755efd0c40cc6127a0e4baceb8d226c7e3), [50d1d92](https://github.com/openssl/openssl/commit/50d1d92de9a4cf62723a3c1ea2f39501feea7d6e), [ac55928](https://github.com/openssl/openssl/commit/ac5592812d921ab90a11572e5254bdab4d6671cf)
- Added multiple Coverity annotations to suppress false positives.
  ↳ No PR: [766a7d4](https://github.com/openssl/openssl/commit/766a7d4676f08f815dd5070409e94954f4b64c6c), [588080c](https://github.com/openssl/openssl/commit/588080cbf8e254ca2c033224146bc29fddea75a7), [66cb4fc](https://github.com/openssl/openssl/commit/66cb4fcdc5039fe5b1476ed48a936137a307a58b), [71b7f34](https://github.com/openssl/openssl/commit/71b7f34978c7332562300487af497559b67f600a), [a381897](https://github.com/openssl/openssl/commit/a381897470f5c6ac2f4e71f48d33d71cde7873dd)
- Update the missing documentation list, marking functions such as SSL_CTX_get_ssl_method as having documentation.
  ↳ No PR: [e12bee7](https://github.com/openssl/openssl/commit/e12bee78d4e64da2176dd9a7ec19ec680dd3bebf), [eb27a90](https://github.com/openssl/openssl/commit/eb27a90e41a62d3337c5e21e24ee72f1e49a445c)
- Updated Paul Dale's PGP key signing.
  ↳ No PR: [60e9380](https://github.com/openssl/openssl/commit/60e938057439b7b6a1ff542a34209657007d2d17)
- Updated copyright year of all source files to 2022.
  ↳ No PR: [fecb3aa](https://github.com/openssl/openssl/commit/fecb3aae22aeda493f348739ebf7943071ecdbe1)
- Add annotation to suppress Coverity static analysis warnings.
  ↳ No PR: [6d5f636](https://github.com/openssl/openssl/commit/6d5f636ce1ff6b57846e0e0fc82f7ed56aee2ac5)
- Updated test documentation to add instructions for running a single SSL test via the make command.
  ↳ No PR: [eec204f](https://github.com/openssl/openssl/commit/eec204f4b19f86e726aa09c5c919a57bdf2ee1d0)
- Corrected comment on parameter type in OSSL_PARAM sample code.
  ↳ No PR: [809526a](https://github.com/openssl/openssl/commit/809526a06c1305d67a8f231ca15cd27ec800efce)
- Clarify comments in rand_egd.c regarding the use of EGD on HPE NonStop platforms.
  ↳ No PR: [93ed4b5](https://github.com/openssl/openssl/commit/93ed4b5fb40a8ece9d9c67041c4187d63dbfbd51)
- Add documentation for PEM_X509_INFO_read() and PEM_X509_INFO_read_bio().
  ↳ No PR: [9454423](https://github.com/openssl/openssl/commit/9454423bf1eac4c75e70ff4fd67456e4cfb05a92)
- Remove redundant conditions in RSA salt length check.
  ↳ No PR: [05e51bc](https://github.com/openssl/openssl/commit/05e51bc79bac45e194dd6f0bf73c99ed5ca06272)
- Corrected comment on memory BIO usage in http_client.c.
  ↳ No PR: [7d5019c](https://github.com/openssl/openssl/commit/7d5019c15af8f88443a7edddd4b150a7dafeda5d)
- Fix typos and terminology inconsistencies, including correcting OSCP to OCSP in ocsp help text.
  ↳ No PR: [2837b19](https://github.com/openssl/openssl/commit/2837b19fcba4bf4ff2ecdc8435c650bf18c27552), [1567a82](https://github.com/openssl/openssl/commit/1567a821a4616f59748fa8982724f88e542867d6)
- Extended comments in keep_alive() to explain that polling may be required even if acknowledgments are disabled.
  ↳ No PR: [93d9d60](https://github.com/openssl/openssl/commit/93d9d6097685dc29e654db15c091c550aef16d5b)
- Improved code style in multiple source files.
  ↳ No PR: [a2db4e6](https://github.com/openssl/openssl/commit/a2db4e6cd6478c3ae633d9919d0a88f1eb5678f7), [c633b97](https://github.com/openssl/openssl/commit/c633b973f669948a22bb5e3e3085f54d8d00a90a), [f95fec2](https://github.com/openssl/openssl/commit/f95fec293800b47e5eff0f08daefcf1397a24423)
- Corrected description of -dsaparam option in openssl-dhparam command documentation.
  ↳ No PR: [2885b2c](https://github.com/openssl/openssl/commit/2885b2ca4eee5586baa50208e41a1ca54532eb3a)
- Improve the documentation of the -CAserial and -CAcreateserial options to clarify that they need to be used in conjunction with the -CA option.
  ↳ No PR: [7a16f17](https://github.com/openssl/openssl/commit/7a16f179ab0bc2c474a754c0ad7e35b40534a38e)
- Clean up redundant TODO comments about RECLAYER in the SSL record layer.
  ↳ No PR: [4564b47](https://github.com/openssl/openssl/commit/4564b47d7546a2225e1565715030981387b8e393), [499b2c4](https://github.com/openssl/openssl/commit/499b2c4654a28838924b60cab754fffa7b9f5609), [1b285ac](https://github.com/openssl/openssl/commit/1b285ac13726f443d1d737a1e2389ba6e17ba98f)
- Remove non-existent no-{ssl|tls|tls1_3|dtls}-method build option from INSTALL.md.
  ↳ No PR: [5f18dc7](https://github.com/openssl/openssl/commit/5f18dc7facc9bd477173ae97a1bd84f21758da58)
- Fixed inconsistent markup formats in documents such as CMS_verify() and PKCS7_verify(), and cleaned up the list of missing documents.
  ↳ No PR: [cae1d08](https://github.com/openssl/openssl/commit/cae1d08f2c967cba960163075bda39f33d41c156)
- Fixed spelling and grammatical errors in multiple documents.
  ↳ No PR: [d7f3a2c](https://github.com/openssl/openssl/commit/d7f3a2cc8691c062ef5bdeef28b66f80c8f7d5c3), [af33b20](https://github.com/openssl/openssl/commit/af33b200da8040c78dbfd8405878190980727171), [5d32acf](https://github.com/openssl/openssl/commit/5d32acf0f53c85e5da787035e47f775221486c64), [0b7ad5d](https://github.com/openssl/openssl/commit/0b7ad5d928f9ee749cfc670ad08067a961217fea), [0e4e03c](https://github.com/openssl/openssl/commit/0e4e03c8528ab54a5b125582afdf2cdadfb6c9bb)
- Cleaned up and corrected many comment errors and outdated comments in the code.
  ↳ No PR: [3fa6dbd](https://github.com/openssl/openssl/commit/3fa6dbd1be0791210853b0367b8483d4e6291e4f), [f93c0f5](https://github.com/openssl/openssl/commit/f93c0f546423eab65be3bc50a8cdfc3d5eb6b2e1), [27003aa](https://github.com/openssl/openssl/commit/27003aa6ebcb9f3a03c253dbd26fc152e1481fab), [055d029](https://github.com/openssl/openssl/commit/055d029610712a281aed0c23ddd3c8f4dbf40f80), [a63fa5f](https://github.com/openssl/openssl/commit/a63fa5f711f1f97e623348656b42717d6904ee3e), [9bbc5b5](https://github.com/openssl/openssl/commit/9bbc5b54b0f0c64d21eaea35ee3f9722aa77a56e)
- Updated description of default MAC digest algorithm in PKCS12 man page.
  ↳ No PR: [d9aca2d](https://github.com/openssl/openssl/commit/d9aca2dd9b56dbfa6a0566cc3ad8b7c713ac61b2)
- Document fix to RSA CRT parameter names in FIPS self-test in CHANGES.md.
  ↳ No PR: [c7424fe](https://github.com/openssl/openssl/commit/c7424fe68c65aa2187a8e4028d7dea742b95d81a)
- Added QUIC-TLS integration design document.
  ↳ No PR: [88113f5](https://github.com/openssl/openssl/commit/88113f5dc6828694820d39612c3a760e386a0aa5)
- Updated QUIC API design document to improve shutdown processing, flow status query and error handling.
  ↳ No PR: [9532c51](https://github.com/openssl/openssl/commit/9532c517591c7e4cfa43dfdd1bff76e5ce1593cd)
- Fix description of BUILD_METADATA plus sign prefix in NOTES-NONSTOP.md.
  ↳ No PR: [83a5bd8](https://github.com/openssl/openssl/commit/83a5bd80708adc6726deac390e405a7b50dec540)
- Corrected the help text of the -cipher-algorithms option in the openssl list command to clearly indicate symmetric cipher algorithms.
  ↳ No PR: [2eb7529](https://github.com/openssl/openssl/commit/2eb75291c1357cdaf852e0da613edc14f3d5ae4f)
- Unify the coding style of pubin variables in DSA, EC and RSA commands, and simplify the assignment logic of private variables.
  ↳ No PR: [091fef4](https://github.com/openssl/openssl/commit/091fef4936da93deee585dadd994144b330485d4)
- Fixed GCC strict prototype warning in trace_api_test.c triggered by missing void parameter in function declaration.
  ↳ No PR: [1fcd84c](https://github.com/openssl/openssl/commit/1fcd84c7017416a3c9461914d7a943591ad87a82)
- Fixed the SSL error code value in openssl.txt to make it consistent with the header file definition.
  ↳ No PR: [cab5b3a](https://github.com/openssl/openssl/commit/cab5b3a344199d54dd4432dbc6d4b361e10e11d1)
- Fixed typo in timersub macro definition in test file.
  ↳ No PR: [1cf2557](https://github.com/openssl/openssl/commit/1cf2557063b142db3684b780c301f8ed609f1e84)
- Fixed comment errors in QUIC related header files and implementation.
  ↳ No PR: [81b6b43](https://github.com/openssl/openssl/commit/81b6b43c4a56e4158ee4059fc03c10f970423506)
- Added SSL/TLS alert related error strings to error status.
  ↳ No PR: [a2a09af](https://github.com/openssl/openssl/commit/a2a09af086e97da35225ec952f2ae75c833b19e7)
- Removed trailing spaces in INSTALL.md.
  ↳ No PR: [98663af](https://github.com/openssl/openssl/commit/98663afce7a909be1518921a9995540308a52462)
- Added documentation for EVP_PKEY_CTX_get0_pkey() and EVP_PKEY_CTX_get0_peerkey(), and updated the missing documentation list.
  ↳ No PR: [3be7674](https://github.com/openssl/openssl/commit/3be76745e55eab9ea976f7a23e6c8ecd3bb8136c)
- Fixed multiple spelling errors in documentation and comments.
  ↳ No PR: [a53d4f8](https://github.com/openssl/openssl/commit/a53d4f83fcfc3e12581da29f55ca5867d1e47ae0)
- Fixed typos in seed macro names and description strings.
  ↳ No PR: [9c3de01](https://github.com/openssl/openssl/commit/9c3de015121fb4ebbecccfbbda9eed8d4a3cb2d5)
- Added util/ctags.sh script for generating tags files with macro expansion, and updated .gitignore.
  ↳ No PR: [859521e](https://github.com/openssl/openssl/commit/859521e57970027c2ec763928753a1e5f843cf69)
- Fixed annotation errors in QUIC shutdown process and cleaned up code formatting.
  ↳ No PR: [1d40b15](https://github.com/openssl/openssl/commit/1d40b151e252490e2187235d50228119c2b6f6d5)
- Added comments to aarch64's unroll8_eor_aes_gcm kernel function explaining the input length unit.
  ↳ No PR: [4596c20](https://github.com/openssl/openssl/commit/4596c20b86871b2bb0f9a7f6b855c0b7f0d4fbf3)
- Fixed comments for OSSL_CMP_CTX_set1_recipient and OSSL_CMP_CTX_set1_issuer.
  ↳ No PR: [8c29fa2](https://github.com/openssl/openssl/commit/8c29fa21a7983862f0bd4744523ffee61f17ca22)
- Fixed copy-paste error of CVE-2022-2097 links in CHANGES.md and NEWS.md.
  ↳ No PR: [1472127](https://github.com/openssl/openssl/commit/1472127d9d6bc4866ab26b503e0d5937b40dca37)
- Added comment markers for QUIC functions that require locking.
  ↳ No PR: [d7b1fad](https://github.com/openssl/openssl/commit/d7b1faddab2817c6b73f18f84f8ad6cc9d2f563a)
- Removed CI workflow documentation for old FIPS provider cross-version checking.
  ↳ No PR: [3254f7b](https://github.com/openssl/openssl/commit/3254f7b66695f09d16f27a0b057446415ff81921)
- Fixed typo in ssl_load_ciphers function comment in ssl/ssl_ciph.c.
  ↳ No PR: [e35a213](https://github.com/openssl/openssl/commit/e35a21334172997c40928933e1f44e3ba4d2317c)
- Cleaned up the comments of OSSL_CRMF_CERTTEMPLATE related functions and adjusted the return type declaration.
  ↳ No PR: [8b6bbca](https://github.com/openssl/openssl/commit/8b6bbcaa7bd2f0b44d7d0d867acc6002ba09a6fd)
- Fixed entry description for CVE-2023-1255 in CHANGES file.
  ↳ No PR: [e699007](https://github.com/openssl/openssl/commit/e6990079c2413625d2039ebed49ea17a5b8cf935)
- Updated QUIC congestion control design documentation, revised configuration parameters and diagnostic output descriptions.
  ↳ No PR: [1c44ed7](https://github.com/openssl/openssl/commit/1c44ed7bd3546d12fc95d8624e292412e357f789)
- Added initial design documentation for QUIC error handling.
  ↳ No PR: [95d3c14](https://github.com/openssl/openssl/commit/95d3c148ca3818a8773f293e9a886a3ec4185353)
- Removed unused macro l2n6 in include/internal/common.h.
  ↳ No PR: [6aeb42e](https://github.com/openssl/openssl/commit/6aeb42eca97227c8235af0986d1525ee4a916504)
- Fixed multiple typos in code and tests.
  ↳ No PR: [2913b5c](https://github.com/openssl/openssl/commit/2913b5c09fcc4e5d493589ded2c22a3116127ed0), [eb4129e](https://github.com/openssl/openssl/commit/eb4129e12cdf7fe64b3ce352f539e3dbeb1b1321), [060f370](https://github.com/openssl/openssl/commit/060f370ebc21b4d334a71ca8b8ab54f22199f177), [6ea4da6](https://github.com/openssl/openssl/commit/6ea4da6e4d03cd9591805e166cfd94a374c33628), [55d3a6b](https://github.com/openssl/openssl/commit/55d3a6be6ba3af9781631e74833ea1dcbd4008e6), [4409e15](https://github.com/openssl/openssl/commit/4409e1522f026defaf326a65c0887dfd31ca4e13), [13069d0](https://github.com/openssl/openssl/commit/13069d0144096ef8cecc82fb7fcd1a1eed93d7a8)
- Fixed and updated comments in the code, including formatting corrections, additional explanations and improvements.
  ↳ No PR: [5fc256c](https://github.com/openssl/openssl/commit/5fc256cd6b991cf0fb5f7cb1da7be14c7e90653f), [5def4bb](https://github.com/openssl/openssl/commit/5def4bbb4be5477146a0fbb4f14ee02df026419c), [5a1b1d2](https://github.com/openssl/openssl/commit/5a1b1d2be3854581171addfe48bd6457a88c76b3), [b369515](https://github.com/openssl/openssl/commit/b3695154b5cfd8ac528b8c2794d2dc446899caae), [73ef6e6](https://github.com/openssl/openssl/commit/73ef6e6f0f14c2cf2231ee72f3d98757310f1e31)
- Fixed spelling, links and copyright information in the document.
  ↳ No PR: [89ed128](https://github.com/openssl/openssl/commit/89ed128d7a871b627693bfc1a89703d1a12cb402), [18f82df](https://github.com/openssl/openssl/commit/18f82df5b14b3fba078c6c5f0f4a0bb8eee6c954), [7197abd](https://github.com/openssl/openssl/commit/7197abddb891933f52ec84dafb41b685d4a1d122), [c5f55a4](https://github.com/openssl/openssl/commit/c5f55a4605a56655b2706c72388c1d59141fd243), [6a2b826](https://github.com/openssl/openssl/commit/6a2b8269a8fb31a0c04b5f4f1ac1074c53319135)
- Added design proposal document for quick parameter positioning.
  ↳ No PR: [15821a4](https://github.com/openssl/openssl/commit/15821a48e558d595895fc8cf1c9c038d7c455550)
- Unify the printing format of uint64_t in QUIC trace logs.
  ↳ No PR: [7802170](https://github.com/openssl/openssl/commit/7802170f7c1d2b89c2610b7affddb3d1b26fc87d)
- Updated .gitignore to ignore autogenerated files.
  ↳ No PR: [944ee2c](https://github.com/openssl/openssl/commit/944ee2c30b1e87d4636aeef2ea9bf1adc647e0d9)
- Fixed typo in QUIC channel code.
  ↳ No PR: [7c793cd](https://github.com/openssl/openssl/commit/7c793cd343cd1fad50091f8eb264e5ce7ddcc6e9), [604a607](https://github.com/openssl/openssl/commit/604a607222933aebba0b5fbb09e9839d4e37faad)
- Clean up duplicate words and unnecessary error reports in comments.
  ↳ No PR: [ad31628](https://github.com/openssl/openssl/commit/ad31628cfef5893b2198077752302a7d9b58135c)
- Add RFC 9000 compliant closed connection status annotation for QUIC channels.
  ↳ No PR: [6b3b5f9](https://github.com/openssl/openssl/commit/6b3b5f9d28d267f7c63be859d8617bf1205e4d68)
- Fine-tune the code format of the QUIC receiving record processing function.
  ↳ No PR: [d11b901](https://github.com/openssl/openssl/commit/d11b901b0b19d2044d15cf4e5a7a41e7e2d9acfa)
- Unify the expression format after the algorithm name in the speed command output.
  ↳ No PR: [eb2ff04](https://github.com/openssl/openssl/commit/eb2ff04cc75934fed2d8b6f3085d262978ae6033)
- Add compliance annotation about dropping illegal packets in QUIC channel.
  ↳ No PR: [bed2087](https://github.com/openssl/openssl/commit/bed20874870da6cf5fa60734964072504563fdac)
- Corrected spelling errors in database prompt information, and adjusted AKID fallback logic for self-signed certificates.
  ↳ No PR: [ccb2f30](https://github.com/openssl/openssl/commit/ccb2f3080d84a271f17458a60e0d7ccd77929e95)
- Updated the TODO comment classification in QUIC code to clarify future plans.
  ↳ No PR: [44cb36d](https://github.com/openssl/openssl/commit/44cb36d04adb737be1aee32908232003deeb67dd)
- Add Coverity annotation in QUIC FIFD to explain failure situations that cannot be handled.
  ↳ No PR: [565d298](https://github.com/openssl/openssl/commit/565d2987cd99a32249050b666d052d963b248d75)
- Adjust the indentation format of conditional inclusion instructions in ms/applink.c.
  ↳ No PR: [bdb1f6b](https://github.com/openssl/openssl/commit/bdb1f6b74486daa1971b928528109a4c67cf2eb9)
- Fixed labeling of TODO comments in QUIC unpacking code.
  ↳ No PR: [828c9c6](https://github.com/openssl/openssl/commit/828c9c6690dc2791cee7873cf6793db187b558bb)
- Fixed the issue of missing explicit void parameter in function definition to comply with coding style.
  ↳ No PR: [e22ebb8](https://github.com/openssl/openssl/commit/e22ebb893e2f44bd08f69f9ce4ccfc5e4d2990e2)
- Remove resolved backlog annotation in QUIC TLS.
  ↳ No PR: [68b9a32](https://github.com/openssl/openssl/commit/68b9a32aa397030d9e49ee1ae84ca1ce6b58efd3)
- Added design documentation on runtime parameter activation.
  ↳ No PR: [9f5102b](https://github.com/openssl/openssl/commit/9f5102bffc8bb3a9b02a0a5e3c1de4326622fe04)
- Updated TODO comments in QUIC code to QUIC FUTURE.
  ↳ No PR: [79cdbe8](https://github.com/openssl/openssl/commit/79cdbe893da0c613db97356d05c0b088e885707f)
- Removed unused variables and updated related comments.
  ↳ No PR: [d561fe5](https://github.com/openssl/openssl/commit/d561fe5a0aabb4d0a9400b5086441bb4f4b4dca4)
- Fixed misspelled macro names in comments.
  ↳ No PR: [4d5cfb2](https://github.com/openssl/openssl/commit/4d5cfb229be8a52cdf961d9b7c5f6c1c0fa3b4f7)
- Update the missingcrypto.txt file to remove entries from recorded documents.
  ↳ No PR: [84364b9](https://github.com/openssl/openssl/commit/84364b9dc693a30fa55c22e684b45978a5bcc77b)
- Fix typo in openssl-pkeyutl documentation.
  ↳ No PR: [59d87f6](https://github.com/openssl/openssl/commit/59d87f6e7eb41018a2a17fef2198d3fcf04e63f4)
- Updated the copyright year of multiple source files to 2023.
  ↳ [#21995](https://github.com/openssl/openssl/pull/21995): [da1c088](https://github.com/openssl/openssl/commit/da1c088f599af3755aaeed1c447a39621ef12e1f) | [#22213](https://github.com/openssl/openssl/pull/22213): [556009c](https://github.com/openssl/openssl/commit/556009c596e0242689df4c26dd7fccdb7f0e1add)
- Fixed typos in code comments and multiple files.
  ↳ No PR: [23def9d](https://github.com/openssl/openssl/commit/23def9d37156cc3b2c00fb45ec3b8e271a5d4563), [10fe5e2](https://github.com/openssl/openssl/commit/10fe5e29cad9a9dbaeda3cdc7c62470b21dd7d38)
- Update version information in CHANGES.md and NEWS.md for multiple alpha releases of OpenSSL 3.2.
  ↳ [#21995](https://github.com/openssl/openssl/pull/21995): [6262ff7](https://github.com/openssl/openssl/commit/6262ff748fe7e3487c86d6feeebd92f61c9ae76a), [7570802](https://github.com/openssl/openssl/commit/75708029ad693fb541be65f9ac1841c47a27648d) | [#22213](https://github.com/openssl/openssl/pull/22213): [1e6b4ba](https://github.com/openssl/openssl/commit/1e6b4baf546f46211e4f5c389c961d9878bbd198), [219bd6a](https://github.com/openssl/openssl/commit/219bd6ac7061c40bd24f896f8652994d62d109de)
- Improve the wording and description of the OSSL_PROVIDER_load_ex design document.
  ↳ No PR: [54fbb9e](https://github.com/openssl/openssl/commit/54fbb9e416524e09d6125ffc551cefba83306992)
- Synchronize change records between 3.2 and 3.1 branches, update CHANGES.md and NEWS.md.
  ↳ No PR: [02f84b0](https://github.com/openssl/openssl/commit/02f84b02e889fce0033174238cbd0b653ee9af2c)
- Add documentation for the SSL_CONF_CTX_finish function and update the missing documentation list.
  ↳ No PR: [955c133](https://github.com/openssl/openssl/commit/955c133ccccd2b6e3f5a1b1342045111fe8b3e86)
- Remove redundant sparse array header file inclusions in ssl/event_queue.c.
  ↳ No PR: [442d08f](https://github.com/openssl/openssl/commit/442d08f215c48896f59e9c09a14773058f9e56bf)
- Fixed the issue of inconsistent table formats in QUIC design documents.
  ↳ No PR: [5995dc3](https://github.com/openssl/openssl/commit/5995dc37197dd85baa749325ba23f5aa8ccbe1f6)
- Updated changelog and news files for CVE-2023-5363.
  ↳ No PR: [1e6e682](https://github.com/openssl/openssl/commit/1e6e682ac27abd9d028f5a7876f7da1a176c175a)
- Split multiple test statements in trace_api_test.c into independent assignment statements to improve code readability.
  ↳ No PR: [0496d2d](https://github.com/openssl/openssl/commit/0496d2dc35b6165873ce4fe4ffbef2458bdd8a0f)
- Updated fuzz documentation and added instructions for libstdc++ dependencies.
  ↳ No PR: [3714a73](https://github.com/openssl/openssl/commit/3714a735acba3a0b3c18259950fc80e9940a3e3d)
- Correct the usage of brackets in INSTALL.md and use colons instead.
  ↳ No PR: [008ca01](https://github.com/openssl/openssl/commit/008ca01e506d85acf0cc06ea8f219a883328344c)
- Clean up redundant header file references, fixed time functions and commented out code in QUIC client fuzzer.
  ↳ No PR: [f762055](https://github.com/openssl/openssl/commit/f7620555189edb94cc5840814c0ab1864041c148)
- Add comments to the digest_enc_alg and enc_digest fields in the PKCS7_SIGNER_INFO structure to explain their confusing names and practical uses.
  ↳ No PR: [e15891b](https://github.com/openssl/openssl/commit/e15891b477fe9c3d3dc6f331812c9e8afc48dc05)
- Correct the Markdown format in demos/http3/README.md and add shell language identifiers to code blocks.
  ↳ No PR: [9f54da4](https://github.com/openssl/openssl/commit/9f54da4136063aa1c2aba8a80c15363ab9517997)
- Update TODO comments to mark their nature more accurately.
  ↳ No PR: [8e520d2](https://github.com/openssl/openssl/commit/8e520d2714abf4c6254ceec24b57f238433541ee)
- Fixed padding value bug in test files.
  ↳ No PR: [0bf1814](https://github.com/openssl/openssl/commit/0bf18140f491024232beca4e139c8feecfe207e9)
- Added header file references to support struct usage.
  ↳ No PR: [fa9e6ad](https://github.com/openssl/openssl/commit/fa9e6ad46860ea92aa2e1ba997b20c6dff76b42c)
- Added diagnostic output for connection closed reasons in QUIC multi-stream tests.
  ↳ No PR: [8c11031](https://github.com/openssl/openssl/commit/8c110311fd5e7f04e2c152b17d44acfd4a279ea6), [687326c](https://github.com/openssl/openssl/commit/687326ce0ac56c405029cfedd435b2e6625a22e3)
- Increase initial timeout limit in QUIC tests to resolve intermittent failures.
  ↳ No PR: [d732991](https://github.com/openssl/openssl/commit/d73299136ef85d83b221364201619e7342523ad7)
- Updated README-QUIC.md document, reorganized content and clarified examples.
  ↳ No PR: [a904462](https://github.com/openssl/openssl/commit/a9044628c8cddfdf0686215b2c61dcbea61f95a4)
- Reorganized and supplemented the description of the demo directory in demos/README.txt.
  ↳ No PR: [7380e6b](https://github.com/openssl/openssl/commit/7380e6b54b141eb05893c9a107ad7c5b6196c97a)
- Updated copyright year of multiple source files to 2023.
  ↳ [#22805](https://github.com/openssl/openssl/pull/22805): [8bee92a](https://github.com/openssl/openssl/commit/8bee92a80174b233a7f4071c57bf14c55c7983aa) | No PR: [2699ffe](https://github.com/openssl/openssl/commit/2699ffe5fa686c35e1ea1c176817a6bbc2dbcd86)
- Updated version stamps and date placeholders in CHANGES.md and NEWS.md for 3.2 beta 2 releases.
  ↳ No PR: [135cd97](https://github.com/openssl/openssl/commit/135cd97395f9b3a91cee17bc7c72d1177d9ed396)
- Updated the README of the QUIC DDD design document, expanded the abbreviations and added libuv installation instructions.
  ↳ No PR: [97750ca](https://github.com/openssl/openssl/commit/97750ca0b2c2fe7fd94e82ae841fec92f7173a35)
