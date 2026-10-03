# Release Note

## Important Changes

### Protocol Layer (SSL/TLS/DTLS/QUIC)
- Added QUIC local connection ID manager (LCIDM), which supports the generation, registration, search and decommissioning of connection IDs. (Architecture event: QUIC internal support module adds LCIDM)
  ↳ No PR: [8489a0a](https://github.com/openssl/openssl/commit/8489a0a1f246e2f8bb1d98fc550b7a0fd341ef51)
- Added QUIC Remote Connection ID Manager (RCIDM), which supports the creation, release, switching, rotation and update of connection IDs. (Architecture event: QUIC internal support module adds RCIDM)
  ↳ No PR: [63f77f0](https://github.com/openssl/openssl/commit/63f77f0454791acbcd150b186988c11a3235882b)
- Added QUIC_PORT object, providing creation, destruction, state management and sub-component access interface. (Architecture event: SSL_Protocol_Core module added QUIC_PORT)
  ↳ No PR: [154131d](https://github.com/openssl/openssl/commit/154131da112ed28b619dc6a7a0bec255e2a79316)
- Migrated QUIC channel routing from QRX-DEMUX to PORT-LCIDM, updated the registration and removal logic of local connection IDs, and used new idle timeout error code constants. (Architecture event: QUIC channel routing migration)
  ↳ No PR: [52dfe6f](https://github.com/openssl/openssl/commit/52dfe6f1c1bf10f4e8c33c0e6735744e2f0c5907)
- Completed the migration of the stateless reset token processing logic in the QUIC channel to the SRTM module, and adjusted the libctx reference and initialization order. (Architecture event: The stateless reset token processing was migrated to the SRTM module)
  ↳ No PR: [5f86ae3](https://github.com/openssl/openssl/commit/5f86ae32c29713aac559626c416cc1672d036cfc)
- Started to use the QUIC_ENGINE object to reconstruct the life cycle management of QUIC connections, and changed the creation and attribute access of ports and channels to the engine object. (Architecture event: QUIC engine object introduced to reconstruct the connection life cycle)
  ↳ No PR: [22739cc](https://github.com/openssl/openssl/commit/22739cc3acf2412829a1b0e54d1033efe9679e60)
- Introduced engine and port management for QUIC TSERVER, delegated channel creation and network IO settings to ports, and improved the corresponding resource release logic. (Architecture-related: QUIC TSERVER engine and port management)
  ↳ No PR: [167e5f3](https://github.com/openssl/openssl/commit/167e5f34c8f4e7c414c6e48376987160bc23c7df)
- Added SSL_CTX field in QUIC port parameters and port structure, used to construct handshake layer object when creating a new channel. (Architecture-related: QUIC port structure extension)
  ↳ No PR: [2954287](https://github.com/openssl/openssl/commit/29542870412cea69f9430d8322c9e6f19c1f9dce)
- Changed the access method of resources such as libctx, propq, mutex and now_cb in the QUIC channel to indirect access through QUIC_PORT, restructured related functions, added an interface to obtain the number of remote available streams, and improved the channel cleanup logic. (Architecture-related: QUIC channel resource access reconstruction)
  ↳ No PR: [34fa182](https://github.com/openssl/openssl/commit/34fa182e1d8fa2f1d4016e13e7b6500fd117f781)
- Migrated QUIC's DEMUX and default packet processing logic from CHANNEL to PORT, and added port-level connection management, timing and network reception functions. (Architecture-related: QUIC DEMUX migrated to PORT)
  ↳ No PR: [4ed6b48](https://github.com/openssl/openssl/commit/4ed6b48d9dd469d43d810fa285257043e9ce9779)
- Migrate the stateless reset processing logic from the QUIC channel to the port layer, and integrate the processing in the port's default packet processor. (Architecture-related: Migrate stateless reset to PORT)
  ↳ No PR: [6107619](https://github.com/openssl/openssl/commit/6107619899e50b307e9644625a8050de88c603cc)
- Migrated the network I/O part of the timing processing code of the QUIC channel to the QUIC port layer, and restructured the related function calls. (Architecture-related: migration of timing processing network I/O to PORT)
  ↳ No PR: [632b0c7](https://github.com/openssl/openssl/commit/632b0c7e8c9700b4f3fe49ccccda9caa1fbd390f)
- Reconstruct the QUIC packet routing mechanism: introduce the QUIC_PORT object, remove the old demultiplexer route, and instead inject packets directly through the channel. (Architecture event: QUIC packet routing reconstruction)
  ↳ No PR: [f767101](https://github.com/openssl/openssl/commit/f76710122599731dd9e023f9786b0f3f8863db25), [0df8973](https://github.com/openssl/openssl/commit/0df897321dc146e7ece7b23516cf24b5975f9dc0), [da15093](https://github.com/openssl/openssl/commit/da15093a31cc32cfffb2767fb51fce6f4212d913)
- Added the creation and release of the local connection ID manager in the initialization and cleanup process of the QUIC port. (Architecture event: New local connection ID manager for the QUIC port)
  ↳ No PR: [bbae4bb](https://github.com/openssl/openssl/commit/bbae4bb325554f30e03b5aabc1d99ff49d1babe3)
- Added a counter function for QUIC RCIDM to obtain the number of active and retired connection identifiers. (Architecture event: QUIC RCIDM added a counter function)
  ↳ No PR: [9575b21](https://github.com/openssl/openssl/commit/9575b21851e3dcb53d713dc4051a989c856f53b1)
- Add QUIC engine object and its initialization, destruction, reactor acquisition and other functions. (Architecture event: QUIC engine module change)
  ↳ No PR: [53f78eb](https://github.com/openssl/openssl/commit/53f78eb7216e107102766636024d552f3c42b26d), [26624ca](https://github.com/openssl/openssl/commit/26624caf175e3451090867271c973e66b38dd2c6)
- Added -no_cache_extracerts option and OSSL_CMP_OPT_NO_CACHE_EXTRACERTS constant, used to control CMP extra certificate caching behavior. (Architecture-related: public API)
  ↳ No PR: [1caaf07](https://github.com/openssl/openssl/commit/1caaf073b071dcd184f10bd9cfbdb6ff73b9e945)
- Add support for delayed delivery of all types of responses to CMP clients and servers, and refactor transaction cleanup and polling logic. (Architecture-related: public API)
  ↳ No PR: [192bfec](https://github.com/openssl/openssl/commit/192bfec487b27ee9398138ce5f0c5b00f536dc95)
- Added optional certProfile request header and -profile option to CMP library and command line, and added OSSL_CMP_{HDR,CTX}_get0_geninfo_ITAVs acquisition function. (Architecture-related: public API)
  ↳ No PR: [7c6577b](https://github.com/openssl/openssl/commit/7c6577ba9f5eb348476a53d822a4db6af0d36d36)
- Added OSSL_CMP_MSG_get0_certreq_publickey function to obtain the public key in the certificate request. (Architecture-related: public API)
  ↳ No PR: [bcd3707](https://github.com/openssl/openssl/commit/bcd3707dba1cceffba56ee3226105b64575f2b14)
- Allow ignoring unknown signature algorithms and groups via ? prefix in configuration, and ignoring duplicates. (Architecture-related: configuration behavior)
  ↳ No PR: [10f65f7](https://github.com/openssl/openssl/commit/10f65f7282d07c308cba5e26488bc504f56abc8a)
- Added optimized FIN API, including SSL_write_ex2 function and SSL_WRITE_FLAG_CONCLUDE flag, allowing the stream to be ended while writing data. (Architecture-related: public API)
  ↳ No PR: [2695f7b](https://github.com/openssl/openssl/commit/2695f7b19b3dba8a89b7081e2427cdf2f66d232f), [113be15](https://github.com/openssl/openssl/commit/113be15a5ee9aa79a70098e27071c46175cbbb18), [4991d86](https://github.com/openssl/openssl/commit/4991d86753391121ef0bf1eb5a4e526893132294), [f231cc8](https://github.com/openssl/openssl/commit/f231cc8576a6353baebe2c7a9cd8cefa3537e26e), [c18c301](https://github.com/openssl/openssl/commit/c18c301deb44deb27f35c199e8bf44ca8b80e579)
- Added QUIC tuning API, providing functions for getting and setting uint type values, and adding related error codes. (Architecture-related: public API)
  ↳ No PR: [d51398b](https://github.com/openssl/openssl/commit/d51398b9984d31eab275250a650c2621f3ebdf0d), [e203d1b](https://github.com/openssl/openssl/commit/e203d1b542eba8dd7ae53b3def2abf8482acc4d8)
- Enable SSL_clear_options to pass new options to the record layer, and ensure that SSL_set_options synchronously updates the options written to the record layer. (Architecture-related: public API)
  ↳ No PR: [e8e95f2](https://github.com/openssl/openssl/commit/e8e95f20a9b00ca62d407263110663eba7614683)
- Added idle timeout configuration and flow counting related APIs for QUIC channels, and adjusted the local connection ID replacement implementation. (Architecture-related: public API)
  ↳ No PR: [ecff7ca](https://github.com/openssl/openssl/commit/ecff7ca4c1043265a7af09d7f9286a08779dd098), [898e1f1](https://github.com/openssl/openssl/commit/898e1f1353682222efe96cd4dd5ac6a73e2cc8b3), [a1446ff](https://github.com/openssl/openssl/commit/a1446ff2060c6bad71ef79f16e7894e83fd5fb82)
- Add feature query function to QUIC connection, support idle timeout, stream availability, automatic tick and event processing mode. (Architecture-related: public API)
  ↳ No PR: [57eee46](https://github.com/openssl/openssl/commit/57eee469f72b449c124c93513e573582bcef1166)
- Added the function of recording implementation versions in QUIC QLOG, and supports customizing log output by overriding the implementation name and process ID. (Architecture-related: public API)
  ↳ No PR: [26e4bac](https://github.com/openssl/openssl/commit/26e4bac4db5be2eefd894c102b1a65a752ebaefd)
- Added SSL_poll function, supports QUIC polling, covering error codes, front-end implementation, back-end flags, automatic tick and compatibility of non-QUIC builds. (Architecture-related: public API)
  ↳ No PR: [2a5ee0a](https://github.com/openssl/openssl/commit/2a5ee0a08d2c074db741da99d29abb73386e00c7), [ab05f13](https://github.com/openssl/openssl/commit/ab05f13cedb6cb1f058381676ae28652f7e4534d), [6ba77d6](https://github.com/openssl/openssl/commit/6ba77d674335c92c29dcabab2682d2ecdd1ceb5a), [9387bd4](https://github.com/openssl/openssl/commit/9387bd4c25cf37613bcecc173e63f93327eb47ec), [6d7b0e0](https://github.com/openssl/openssl/commit/6d7b0e06a24592790a5b75945ab24e941e3c7cec), [06d70d9](https://github.com/openssl/openssl/commit/06d70d94981b3c572cdfd62df5fdb3806eda2cc5)
- Migrate QUIC transmission error codes from internal header files to public header files, making it a public API. (Architecture-related: public API)
  ↳ No PR: [02f5ab7](https://github.com/openssl/openssl/commit/02f5ab77854647e4f34cdd340d57bb071afb997d)
- Define dedicated error code for idle timeout, and rename QLOG setting function. (Architecture-related: public API)
  ↳ No PR: [5f02bbd](https://github.com/openssl/openssl/commit/5f02bbd5a6e7157faefb944ac5f11e0f6b024740), [b58abf9](https://github.com/openssl/openssl/commit/b58abf982218c704801d8a7b0f5725b730c94671)
- Introduced a default header line limit (256) for HTTP responses, and added a new OSSL_HTTP_REQ_CTX_set_max_response_hdr_lines API to adjust this limit. (Architecture-related: public API)
  ↳ No PR: [7f8aba2](https://github.com/openssl/openssl/commit/7f8aba2f44e9ca65b8a95987fa6c46020e1bdd6d), [103952d](https://github.com/openssl/openssl/commit/103952d4392e5f637a1dc98053890e132a2ba027)
- Modified the callback interface of the default packet processor in the QUIC demultiplexer to receive the parsed target connection ID, and removed the stateless reset detection logic. (Architecture-related: public API)
  ↳ No PR: [d743afe](https://github.com/openssl/openssl/commit/d743afe7e83df9473058d68a7fa89649741e6814), [b71046b](https://github.com/openssl/openssl/commit/b71046b4a4eab5239e656138faf50f9022227729)
- Add the consumed credit parameter to the QUIC transport stream credit control function to correctly track connection-level credit consumption when a single packet contains multiple stream data and prevent overuse. (Architecture-related: public API)
  ↳ No PR: [e57bf6b](https://github.com/openssl/openssl/commit/e57bf6b3bfa2f0b18e5cad7fd3c5fdd7c51516b9), [aa6ac60](https://github.com/openssl/openssl/commit/aa6ac60728207ba18779d7cbe71893c066bcbc28)
- Add a retry mechanism and length verification for generating connection IDs in QUIC LCIDM, and rename related fields to improve code clarity. (Architecture-related: QUIC connection ID management)
  ↳ No PR: [4c62c56](https://github.com/openssl/openssl/commit/4c62c566486bac73dc6ffb665e5b5262bac5dd90), [1f29585](https://github.com/openssl/openssl/commit/1f2958536eff61984b4746410cd3e4fe8f0383dd), [4760116](https://github.com/openssl/openssl/commit/4760116f5a1d30ad57819eec993c8cce61192477)
- Fixed the problem that the default buffer length calculation under TLSv1.3 does not include content type bytes. (Architecture-related: external behavior)
  ↳ No PR: [e07b5e1](https://github.com/openssl/openssl/commit/e07b5e1a0a76f25c633a468d4f7945b82ae436bd)
- Allow CMS attributes to be added repeatedly, fixing the regression problem introduced previously. (Architecture-related: public API)
  ↳ No PR: [d7e707c](https://github.com/openssl/openssl/commit/d7e707cb4983a35b1a265c6042da410d829f3b19)
- Unify error handling in SSL_CONF_cmd, and record internal errors when the index is out of bounds, etc. (Architecture-related: public API)
  ↳ No PR: [430dcbd](https://github.com/openssl/openssl/commit/430dcbd0463573fece704263648cc15e891c3d49)
- Fixed the value conflict of CMP_R_UNEXPECTED_SENDER error code and adjusted it to 106. (Architecture-related: public API)
  ↳ No PR: [c930ee5](https://github.com/openssl/openssl/commit/c930ee52a4b0853fa42f0ca5942e59a68c6bca80), [5003aba](https://github.com/openssl/openssl/commit/5003abae023e59f82add1d77d4b5739f9976c29c)
- Fixed the error code conflict and adjusted the value of SSL_R_FEATURE_NEGOTIATION_NOT_COMPLETE to avoid duplication. (Architecture-related: public API)
  ↳ No PR: [07e66f3](https://github.com/openssl/openssl/commit/07e66f3c3d758619d8594e51afea80d7d23908db)
- Fixed incorrect internal pointer reference in SSL_export_keying_material function in QUIC scenario, and added corresponding test cases. (Architecture-related: public API)
  ↳ No PR: [12c0d72](https://github.com/openssl/openssl/commit/12c0d72c4a82804f3c2d234ea9ea4e3a2fbb257b)
- Fix the processing order of SSL_ctrl operations in QUIC connections, ensuring that they are routed to the QUIC method first and then check whether the connection object is empty. (Architecture-related: public API)
  ↳ No PR: [5c16e9d](https://github.com/openssl/openssl/commit/5c16e9d384d1d0f4784352633044610a1f264027), [28c7f52](https://github.com/openssl/openssl/commit/28c7f52612805c4ec0816ff1310222acd069de7d)
- Fixed the memory corruption problem of SSL_set1_groups_list() when setting 40 or more groups, and added corresponding test cases. (Architecture-related: public API)
  ↳ No PR: [f4ed6ee](https://github.com/openssl/openssl/commit/f4ed6eed2c8fcb1852938683669218655fe4f894)
- Updated the SSL error code definition and adjusted the number of SSL_R_POLL_REQUEST_NOT_SUPPORTED. (Architecture-related: public API error code changes)
  ↳ No PR: [f945986](https://github.com/openssl/openssl/commit/f945986a180d0af7cc3029ffbae0c826f06e5c9d)
- Uniformly renamed QUIC error code macros, changing QUIC_ERR_* to OSSL_QUIC_ERR_*, which is a destructive change. (Architecture-related: public API macro rename (destructive change)
  ↳ No PR: [4b4b9c9](https://github.com/openssl/openssl/commit/4b4b9c9eb3e677de6276c94758cb554c8f560697)
- Fixed build failure when KTLS is enabled on FreeBSD, added empty implementation for unsupported zero-copy sending file functionality. (Architecture-related: Platform compatibility)
  ↳ No PR: [2cac2fe](https://github.com/openssl/openssl/commit/2cac2feff2612c0a324675d8151fea3e2d03397c)
- Rename QUIC QLOG's environment variable QFILTER to OSSL_QFILTER. If not set, the wildcard character * is used by default. (Architecture-related: environment variable renaming)
  ↳ No PR: [9dcad79](https://github.com/openssl/openssl/commit/9dcad79795a74b1fe7ecb001f9f65f940cfd4848)
- Adjusted the macro definition of QUIC idle timeout value. (Architecture-related: public API: macro definition changes)
  ↳ No PR: [01690a7](https://github.com/openssl/openssl/commit/01690a7ff36c4d18c48b301cdf375c954105a1d9)
- Add deprecation notices in the QUIC DEMUX and QRX header files, mark some functions as being removed, and recommend using QUIC_PORT and QUIC_LCIDM for explicit routing instead. (Architecture-related: Internal interface deprecation: QUIC DEMUX/QRX)
  ↳ No PR: [08c7cae](https://github.com/openssl/openssl/commit/08c7caebbe425e272d00310363d8826c9ba300c9)

### Provider and Engine Framework
- Formalize the status management of QUIC ports, add a stateless reset processing function, and optimize the packet processing process. (Architecture event: QUIC port management module change)
  ↳ No PR: [0225d42](https://github.com/openssl/openssl/commit/0225d42bceca561a5d678b0cc4fa982b6afabfea)
- QUIC_PORT is now responsible for the creation of all channels, and has added functions for updating polling descriptors and setting up network read and write BIO. (Architecture-related: QUIC_PORT responsibility extension)
  ↳ No PR: [2d80e45](https://github.com/openssl/openssl/commit/2d80e459017d7744e6a5438422ed36fe1d448adb)
- Added QUIC stateless reset token support, including generators, managers and their integration in ports. (Architecture event: QUIC stateless reset token support)
  ↳ No PR: [2db3fdb](https://github.com/openssl/openssl/commit/2db3fdb4578ca43624acda81b72bc02b08c8ce3a), [abc06d5](https://github.com/openssl/openssl/commit/abc06d53a968f9072a2d026a776f3b66944ae7f3), [a4be37b](https://github.com/openssl/openssl/commit/a4be37b8ce8ed4cc809b45c0177cb47670ed4224), [69055b2](https://github.com/openssl/openssl/commit/69055b2ceca9e86e536ab17c862e46734c1a61de), [e64ad80](https://github.com/openssl/openssl/commit/e64ad80c72b0743871f02badfe199d713b0cdadd)
- Added SM4 encryption implementation based on Zvksed extension for RISC-V 64-bit platform. (Architecture-related: Platform compatibility)
  ↳ No PR: [7543bb3](https://github.com/openssl/openssl/commit/7543bb3a69c021edbe73bb38a8cc4d3708a68c5d)
- Added SHA256 implementation based on Zvknha extension for RISC-V platform, and adjusted SHA512 conditions to support Zvkb extension. (Architecture-related: Platform compatibility)
  ↳ No PR: [1707306](https://github.com/openssl/openssl/commit/17073066520dbbf1ef3ce4856c570d61e9548083)
- Provide SHA-512 hardware acceleration implementation for the RISC-V Zvknhb extension, which is automatically enabled when the extension is supported and the vector length meets the conditions. (Architecture-related: platform compatibility)
  ↳ No PR: [9c22a24](https://github.com/openssl/openssl/commit/9c22a240dab51dc9a5583d36726b81073f9c8d34)
- Added SM3 implementation based on Zvksh extension for RISC-V platform, and adjusted enabling conditions to support lower vector length. (Architecture-related: platform compatibility)
  ↳ No PR: [f20ee1f](https://github.com/openssl/openssl/commit/f20ee1f4908f1da9ebc072043b3cfbb90eba2508)
- Extended the SSL_SESSION time-related function, added the _ex version using time_t, and changed the original function to call the new function. (Architecture-related: public API)
  ↳ No PR: [ffc853b](https://github.com/openssl/openssl/commit/ffc853bcb5f431d57b8a24dd062ff76d52891e63)
- Enhanced RSA provider, supports automatic generation of CRT coefficients (dmp1/dmq1/iqmp) through new parameters in EVP_PKEY_fromdata(). (Architecture-related: public API)
  ↳ No PR: [f3be536](https://github.com/openssl/openssl/commit/f3be536686654016adc9e22024c06036f949f2b0)
- Extend SHA-512 family support on RISC-V platforms to platforms with vector lengths of at least 128 bits, and use the Zvkb extension instead. (Architecture-related: Platform compatibility)
  ↳ No PR: [837f7df](https://github.com/openssl/openssl/commit/837f7df8c0a4122ae95b0859329c9327a44e1764)
- Add EVP_DigestSqueeze() support for the digest provider of the s390x platform. (Architecture-related: public API: EVP_DigestSqueeze)
  ↳ No PR: [9489892](https://github.com/openssl/openssl/commit/94898923538f686b74b6ddef34571f804d9b3811)
- Remove the hard-coded limit of TLS 1.2 exporter context length, instead dynamically allocate memory and add length verification. (Architecture-related: External behavior: TLS 1.2 exporter context length)
  ↳ No PR: [ef9d8f2](https://github.com/openssl/openssl/commit/ef9d8f2f1fd6d0f66184457bd97ab51ce6092745)
- Added key setting status tracking in the password context, and the encryption operation returns an error when the key is not set. (Architecture-related: External behavior: Password context key status check)
  ↳ No PR: [3a95d1e](https://github.com/openssl/openssl/commit/3a95d1e41abf2e8eb0f6f07003bac844950bfaae)
- Added SSL_OP_PREFER_NO_DHE_KEX option, allowing the server to prefer non-DHE mode in PSK key exchange. (Architecture-related: public API)
  ↳ No PR: [b8590b2](https://github.com/openssl/openssl/commit/b8590b2f365a963965d799c438c5c92659c2fcae), [7158339](https://github.com/openssl/openssl/commit/715833935b27a058c6af3c0f104b4e265527ae6c), [dfc836c](https://github.com/openssl/openssl/commit/dfc836c346cc6001534eaf9ed3a151b7aa658335)
- Adjust provider activation logic: the activate parameter must be set to yes/true/1 to activate, maintaining backward compatibility. (Architecture-related: external behavior)
  ↳ No PR: [506ff20](https://github.com/openssl/openssl/commit/506ff20662a228b17840f0b49865a927a45c2908)
- Added QUIC event processing mode API, including getting and setting functions and constant definitions, and implementing mode control and automatic tick triggering. (Architecture-related: public API)
  ↳ No PR: [8c13e08](https://github.com/openssl/openssl/commit/8c13e0851319ac99413044ac83e7e4a66fb23277), [965f68f](https://github.com/openssl/openssl/commit/965f68f3e94267e0d19e45c2028386906331b051), [9d90b65](https://github.com/openssl/openssl/commit/9d90b65888740b8f8fea6fb359d2314c607a86d7), [8c09d69](https://github.com/openssl/openssl/commit/8c09d69883120d2a9fbe3fadf5f198b77fe901e3), [4a2e39d](https://github.com/openssl/openssl/commit/4a2e39dc1ce52bbee6571f48548a47f04bd857b4)
- Fix the status handling of SHA-3 related functions on the s390x platform, ensuring that absorb, final, shake_final and keccak_final correctly support the extensible output function (XOF). (Architecture-related: platform compatibility)
  ↳ No PR: [7aa45b8](https://github.com/openssl/openssl/commit/7aa45b8bb3269e881d0378aa785ff344efdd2897), [017acc5](https://github.com/openssl/openssl/commit/017acc58f6b67d5b347db411a7a1c4e890434f42), [288fbb4](https://github.com/openssl/openssl/commit/288fbb4b71343516cee6f6a44b9ec55d82fb1532), [1022131](https://github.com/openssl/openssl/commit/1022131d16e30cfbf896e02419019de48e8e1149)
- Unify the return value of CRYPTO_gcm128_decrypt to be consistent with CRYPTO_gcm128_encrypt, and return 0 instead of -1 on failure. (Architecture-related: public API)
  ↳ No PR: [7468a3d](https://github.com/openssl/openssl/commit/7468a3db137bd22dacbcced379b0711986b57067)
- Fix encoding of SM2 keys to correctly use ECC key type instead of SM2 OID in PrivateKeyInfo and SubjectPublicKeyInfo. (Schema related: public API: SM2 key encoding)
  ↳ No PR: [1d49069](https://github.com/openssl/openssl/commit/1d490694dfa790d8e47f8f2ea62ea1d9b1251179)
- Fixed the problem that the SignatureAlgorithms configuration command cannot use the provider signature algorithm. Now when parsing the configuration, the provider signature algorithm list will be loaded correctly. (Architecture-related: external behavior)
  ↳ No PR: [f24ac74](https://github.com/openssl/openssl/commit/f24ac74b7d4ec16992f652fa75cb0ff26a1624cb)
- Fixed the detection conditions of riscv64/riscv32 architecture and added judgment on OPENSSL_CPUID_OBJ macro. (Architecture-related: platform compatibility)
  ↳ No PR: [ff27959](https://github.com/openssl/openssl/commit/ff279597692f9f19dca5b147944d3d96f2e109f8)
- Rolled back previous "classic" key detection improvements for engine-provided private keys, removing code that coerced legacy keys. (Architecture-related: public API)
  ↳ No PR: [39ea783](https://github.com/openssl/openssl/commit/39ea78379826fa98e8dc8c0d2b07e2c17cd68380)
- Fixed the problem that the soft_load directive in the provider configuration must be a clear Boolean value, requiring that its value must be a clear Boolean value (such as 1/0, yes/no, on/off, true/false), and adding documentation for it. (Architecture-related: configuration behavior)
  ↳ No PR: [9277ed0](https://github.com/openssl/openssl/commit/9277ed0a4fc082807ad8d8f66925fb7968437cf6)
- Merged two functions with similar functions, RECORD_LAYER_clear() and clear_record_layer(), added RECORD_LAYER_reset() to replace the original clear_record_layer(), and fixed the bug that some data may not be released correctly when using RECORD_LAYER_clear(). (Architecture-related: public API)
  ↳ No PR: [4a0e484](https://github.com/openssl/openssl/commit/4a0e4849af1588dfe9d7e01738acc96799b83447)
- Fixed build failure on RISC-V platform due to missing OPENSSL_CPUID_OBJ check. (Architecture-related: Platform Compatibility)
  ↳ No PR: [daf1f8d](https://github.com/openssl/openssl/commit/daf1f8d64fff4a395ee7cf032484dc022a27e748)
- Removed unnecessary INT_MAX size check in param_build.c, and changed the size parameter type of param_push function from int to size_t, making the code more consistent with params.c. (Architecture-related: public API parameter type change)
  ↳ No PR: [5a40a27](https://github.com/openssl/openssl/commit/5a40a2728ab8d8f25f70d9c00c47676ac6e9fbca)
- Fixed the security vulnerability of reading random stack memory when the requested key length exceeds the maximum digest size in the pbkdf1 key derivation function, added a length check and returned an error. (Architecture-related: key derivation behavior)
  ↳ No PR: [8d89050](https://github.com/openssl/openssl/commit/8d89050f0f676b429043fd5445e5a570d54ad225)

### I/O Abstraction Layer (BIO)
- Remove the legacy calls in QUIC CHANNEL that have been migrated to QUIC_PORT, and transfer the network read and write BIO setting functions to QUIC_PORT. (Architecture-related: QUIC module responsibility migration)
  ↳ No PR: [073e5bc](https://github.com/openssl/openssl/commit/073e5bc781786078d3f838cecefbe9c4918c2a71)
- Add a new SSL type to the BIO polling descriptor, and add corresponding macro definitions and structure members. (Architecture-related: public API)
  ↳ No PR: [d4999f2](https://github.com/openssl/openssl/commit/d4999f2b746a6845536e720252791601acd6bdad)
- Fixed the problem that the BIO_socket_nbio function under the Nonstop platform cannot correctly set the socket non-blocking mode, and adjusted the conditional compilation logic to use the fcntl(F_GETFL) method. (Architecture-related: platform compatibility)
  ↳ No PR: [f63e1b4](https://github.com/openssl/openssl/commit/f63e1b48ac893dd6110452e70ed08f191547cd89)
- Fixed the problem of dgram_sendmmsg failure on GNU/Hurd platform due to lack of IP_PKTINFO, and avoid immediate error reporting by disabling the recvmsg method. (Architecture-related: platform compatibility)
  ↳ No PR: [2f85736](https://github.com/openssl/openssl/commit/2f85736e9c66248528f132d46508f06a0bb8dd88)
- Fixed the issue where BIO_get_new_index() returns an error when the index is exhausted. (Architecture-related: public API)
  ↳ No PR: [d60b375](https://github.com/openssl/openssl/commit/d60b37506da65f3aebc5043984b3ec78fd53f75f)

### Cross-cutting / Other Architecture-related Changes
- Add fuzz testing support for DTLS and update the corpus. (Architecture event: Fuzzing_Tests module change)
  ↳ No PR: [7649b55](https://github.com/openssl/openssl/commit/7649b5548e5c0352b91d9d3ed695e42a2ac1e99c)
- Added QLOG logging function, supports connection startup, status update, parameter setting, connection closure, packet loss recovery, packet_sent and packet_received events, and supports custom titles. (Architecture-related: QLOG logging)
  ↳ No PR: [00b27f3](https://github.com/openssl/openssl/commit/00b27f33e6a2b7f5270f3a3e6edf69121a4dc209), [c127e76](https://github.com/openssl/openssl/commit/c127e764451fa8b0493ade5a696ccdad08deff04), [9c89b9f](https://github.com/openssl/openssl/commit/9c89b9fe1b157f8d10529a07d30c333b799c12e1), [2031c0e](https://github.com/openssl/openssl/commit/2031c0e928f19d2fbdc88d4f5ac4424d700099d9), [4cecbc5](https://github.com/openssl/openssl/commit/4cecbc5400aa2f8172865b368b41c3df50b5a64d), [8fbac4d](https://github.com/openssl/openssl/commit/8fbac4d70eff157b081933bee88fabedfec47b0b), [da6a9a2](https://github.com/openssl/openssl/commit/da6a9a2e336e217dd4bf239078868c8e00ecdcd3), [a0a3a94](https://github.com/openssl/openssl/commit/a0a3a94912dc0eed52fe9dce403065760c380030), [3e52878](https://github.com/openssl/openssl/commit/3e5287803972de26d0ccbb912bf26e4fd42e39e1), [faf0912](https://github.com/openssl/openssl/commit/faf0912a2f0ef4450f0f7082b177b1990662b809), [407bcc8](https://github.com/openssl/openssl/commit/407bcc8d55c06d556a1026aa83c62f10f923ebb2), [fff66ad](https://github.com/openssl/openssl/commit/fff66adfc885c3d229333e28aa2cf225d3be098c), [5849dbe](https://github.com/openssl/openssl/commit/5849dbe52e6657db0b653b93d1eb5bab34f43351), [7698937](https://github.com/openssl/openssl/commit/76989370bc3b48575c556ce37c3cb0381443ed6a), [f8fdc73](https://github.com/openssl/openssl/commit/f8fdc73e5be4d595e745a2c4f525c53558d00bf3)
- When changing the IV length, invalidate the previously set IV. (Architecture-related: External behavior: IV invalidation)
  ↳ No PR: [eddbb78](https://github.com/openssl/openssl/commit/eddbb78f4e5196eee33b2fd3d6adeabb69d52eb7), [82750a0](https://github.com/openssl/openssl/commit/82750a0826cd4728f40df9ef31b3294d83aaafe0)
- Fixed the problem of X509_REQ_delete_attr function incorrectly returning an integer value when the parameter is empty, and instead returns a NULL pointer. (Architecture-related: public API)
  ↳ No PR: [f1f0731](https://github.com/openssl/openssl/commit/f1f0731ddf6cb31d62a2c0f406b009ae9817ed7f)
- Fixed possible release after use issue in X509v3_asid_add_id_or_range, and cleaned up partially created choice objects. (Architecture-related: public API)
  ↳ No PR: [49e9436](https://github.com/openssl/openssl/commit/49e9436af3d85963fd6156b7d6f33e0734bf5ba9)
- Fixed macro definition issues on PowerPC architecture and enhanced platform compatibility, including macro support in Darwin PowerPC and poly1305_ieee754.c. (Architecture-related: Platform compatibility)
  ↳ No PR: [df04e81](https://github.com/openssl/openssl/commit/df04e81794ac3083804c34c173eb2b2fa55d373d), [7068e5e](https://github.com/openssl/openssl/commit/7068e5e2dcc9a6e0c1cd3fab6d8a903681fe6b07)
- Fixed VMS build issues, replacing snprintf with BIO_snprintf to improve cross-platform compatibility. (Architecture-related: cross-platform compatibility)
  ↳ No PR: [1a4b029](https://github.com/openssl/openssl/commit/1a4b029af51ba6128a37959796381ca5b8b7ac00), [c71bde1](https://github.com/openssl/openssl/commit/c71bde1e47020b5d533bf4f14548d8f3e2b030e5)
- Improved the handling of delayed delivery in the CMP protocol, including client and server polling support, sender random number saving, error handling and test case optimization, and moved the polling status check logic from the simulation server to the CMP server core. (Architecture-related: CMP protocol behavior)
  ↳ No PR: [bedffe1](https://github.com/openssl/openssl/commit/bedffe1731e8c587d3d854e05535175863447dc3), [b14ec83](https://github.com/openssl/openssl/commit/b14ec830f5ec99b83dbf3c6f9180dbaa14698a5f)
- Migrated the RISC-V vector encryption extension from zvbb to its subset zvkb, improving flexibility; updated ghash and SM4 related functions and macro definitions. (Architecture-related: Platform compatibility: RISC-V vector encryption extension)
  ↳ No PR: [3645eb0](https://github.com/openssl/openssl/commit/3645eb0be22a4cea4300ab5afbf248d195d0f45b)
- Changed the RLAYER_USE_EXPLICIT_IV macro to directly check the DTLS version number to enhance future compatibility. (Architecture-related: public API)
  ↳ No PR: [709637c](https://github.com/openssl/openssl/commit/709637c8764e153f77c1d55d00b37fb08634aca9)
- Added C code fallback mechanism for assembly implementation of SHA-256 and SHA-512, controlling and renaming C functions through macros. (Architecture-related: Core implementation: SHA assembly/C fallback mechanism)
  ↳ No PR: [204a1c9](https://github.com/openssl/openssl/commit/204a1c9854193bd7fcc3ea1baaf685c9a67d17bb), [db44a69](https://github.com/openssl/openssl/commit/db44a69aa5ce4bdc3e232ad9d7216af0eda65836)
- Added accelerated implementation based on RISC-V vector extensions (rvv and zvbb) for CHACHA20 cipher, and adjusted the original C implementation to support conditional compilation selection. (Architecture-related: public API)
  ↳ No PR: [fcf6812](https://github.com/openssl/openssl/commit/fcf68127e2e171fc0bf1889071768279410fdb80)
- Added AES-128/256-XTS multi-block implementation based on vector encryption extensions for the RISC-V platform, and updated the hardware selection logic to prioritize the use of this acceleration solution. (Architecture-related: public API)
  ↳ No PR: [3e56c0e](https://github.com/openssl/openssl/commit/3e56c0efe72aad6d4246149d9461af48072b681b)
- Add MD5 assembly implementation for loongarch64, improving performance by about 5-7% by optimizing instruction sorting. (Architecture-related: platform compatibility)
  ↳ No PR: [3d68e29](https://github.com/openssl/openssl/commit/3d68e2937ee5c50eacef5f4c34abdf7c0e4dc479)
- Limit the key size during RSA public key checking to no more than 16384 bits, and set the number of Miller-Rabin primality test rounds to 5 to fix long calculation problems caused by too large keys or too many rounds (CVE-2023-6237). (Architecture-related: RSA public key checking behavior change)
  ↳ No PR: [e09fc1d](https://github.com/openssl/openssl/commit/e09fc1d746a4fd15bb5c3d7bbbab950aadd005db), [38b2508](https://github.com/openssl/openssl/commit/38b2508f638787842750aec9a75745e1d8786743)
- Fixed the security vulnerability of infinite growth of session cache in TLSv1.3 (CVE-2024-2511), and enhanced the security of unrecoverable sessions to ensure that unrecoverable sessions are not misused. (Architecture-related: SSL session behavior)
  ↳ No PR: [d30922a](https://github.com/openssl/openssl/commit/d30922ad15a61815b568b684b685d0afa54f1679), [1222c4e](https://github.com/openssl/openssl/commit/1222c4e62d063573a7953bd7d70dc2cc3854d952), [16e2b10](https://github.com/openssl/openssl/commit/16e2b1080aae827878315dc7124d471d24c80783)
- Documented a change in the behavior of the -verify option in crl and req applications: since OpenSSL 3.3, the exit code when verification fails is 1. Also, when the -CApath, -CAfile or -CAstore option is specified, the -verify option is implicitly enabled. (Architecture-related: Command line option behavior)
  ↳ No PR: [c8e4570](https://github.com/openssl/openssl/commit/c8e45709dcbbf0c3dbecfce25960882d9d4f0f33), [2f78e01](https://github.com/openssl/openssl/commit/2f78e01eb5d670b87508509ba9bebc67672d4aba)
- Refactored the pkg-config exporter, adopting a templated approach, adding a .pc.in template file, and updating .gitignore to ignore the generated .pc file. (Architecture-related: pkg-config configuration)
  ↳ No PR: [2ac569a](https://github.com/openssl/openssl/commit/2ac569a67b9d0980efa2d8061a6a61e0645f37a7)
- Added CMake configuration file exporter for OpenSSL, generated OpenSSLConfig.cmake and OpenSSLConfigVersion.cmake, and updated .gitignore to ignore these files. Also updated CHANGES.md and NEWS.md to record the change. (Architecture-related: CMake configuration)
  ↳ No PR: [c768cce](https://github.com/openssl/openssl/commit/c768ccebc718ea0ed6afc5147fe4079fff632cd6), [10264b5](https://github.com/openssl/openssl/commit/10264b534b366785bb560be77913fdbf9f0f4f8f)
- Introduced libabigail tool in CI for checking ABI compatibility of libcrypto and libssl, and fixed CI failure due to ABI differences, synchronized symbol version files, added EVP_DigestSqueeze symbol to ABI configuration. Added debug symbols in CI build to support verification, and updated ABI XML file. Automatically output XML diff for debugging when check fails. (Architecture-related: ABI Compatibility)
  ↳ No PR: [4ede274](https://github.com/openssl/openssl/commit/4ede274cf9b7b9f946fa243c798c961213d1f053), [9e75a0b](https://github.com/openssl/openssl/commit/9e75a0b911ffb2ad99190a72a3d740d100edf61f), [dcfd8cf](https://github.com/openssl/openssl/commit/dcfd8cfd4abf4a9fd26aef290dcdd5b4bb1c7f7a), [40a24c2](https://github.com/openssl/openssl/commit/40a24c20a809916b43116c2bb16a36bdc40221f3)
- Added a check for the existence of the sharedlib_import method in the CMake configuration file of OpenSSL to avoid errors on platforms that lack this method. (Architecture-related: platform compatibility)
  ↳ No PR: [dd5fe94](https://github.com/openssl/openssl/commit/dd5fe94a61b4455630cbb2988da71949e88f8b6a)
- Modified the out-of-source-and-install task in CI to support read-only source trees, and added the enable-quic configuration option. (Architecture-related: build configuration)
  ↳ No PR: [266a355](https://github.com/openssl/openssl/commit/266a3553d743f5335ccdff196a07916f03d34d0d)
- Changed the ABI difference check from CI failure to using label marking, and restructured the related CI workflow. (Architecture-related: ABI compatibility)
  ↳ No PR: [5cd0042](https://github.com/openssl/openssl/commit/5cd004222d3772c54fe4f6e2e4cbea996625411d)
- Fixed the shared library detection condition in the VMS installation script, replacing $config{no_shared} with $disabled{shared} to maintain consistency with configuration data. (Architecture-related: platform compatibility)
  ↳ No PR: [3077bfb](https://github.com/openssl/openssl/commit/3077bfb78e6fcca006359dc9e3f2b37ad104222d)
- Added _dclass to the Windows platform symbol allowed list to support calls to isnan() and isinf() in JSON encoding. (Architecture-related: Platform compatibility)
  ↳ No PR: [bdba075](https://github.com/openssl/openssl/commit/bdba075c1962b7c69b6f40ebef9e0bf1f1325dd8)
- qlog support is enabled by default, the documentation has been updated, and the explicit enable option in the CI configuration has been removed. (Architecture-related: build and installation methods)
  ↳ No PR: [e98940d](https://github.com/openssl/openssl/commit/e98940d6f6da8347ca7a8c5cb9f7c528c6133c8d)
- Added -mxgot option to m68k cross-compilation to solve relocation truncation issue. (Architecture-related: platform compatibility)
  ↳ No PR: [f601ab7](https://github.com/openssl/openssl/commit/f601ab7758bcfcc968571270a04ffee164993f04)
- Downgrade the upload-artifact operation in GitHub Actions from v4 to v3 to be compatible with GitHub Enterprise Server. (Architecture-related: Platform compatibility)
  ↳ No PR: [86d2bbd](https://github.com/openssl/openssl/commit/86d2bbd7c1b6366024a5368f3ea3d4e7d9e8d48c)
- Added macOS 14 (M1) runner support for some CI workflows. (Architecture-related: Platform compatibility)
  ↳ No PR: [fdef881](https://github.com/openssl/openssl/commit/fdef881657f1f9db8ea0d6ddea5d2ee49eb7e694)

### Algorithm Abstraction Layer (EVP)
- Added GCM acceleration implementation based on Zvbb and Zvbc extensions for the RISC-V platform, which will be detected and used first at runtime. (Architecture-related: platform compatibility)
  ↳ No PR: [003f569](https://github.com/openssl/openssl/commit/003f5698146b81f3185d7f17d60a7351c69e236d)
- Added GCM acceleration implementation for RISC-V Zvkg extension, giving priority to vector instructions. (Architecture-related: platform compatibility)
  ↳ No PR: [5191bcc](https://github.com/openssl/openssl/commit/5191bcc81650c34a4660a0921124e4195e18e4b0)
- Added EVP_DigestSqueeze() API, which supports multiple squeezing and outputting data of different lengths for XOF algorithms such as SHAKE. (Architecture-related: public API)
  ↳ No PR: [5366490](https://github.com/openssl/openssl/commit/536649082212e7c643ab8d7bab89f620fbcd37f0), [04b5387](https://github.com/openssl/openssl/commit/04b53878ea498582a6c2cfa93c570584818bbe47)
- Limit RSA-OAEP related functions to only be valid for RSA keys, and an error will be returned when called for non-RSA keys. (Architecture-related: public API)
  ↳ No PR: [0c3eb31](https://github.com/openssl/openssl/commit/0c3eb31b55d3c1544e4e044c2e3c939655bac93d)
- EVP_PKEY_get_bits, EVP_PKEY_get_security_bits and EVP_PKEY_get_size functions now add corresponding error entries to the error queue when they fail. (Architecture-related: public API)
  ↳ No PR: [ae643b3](https://github.com/openssl/openssl/commit/ae643b32f91affe61dd411a58b76c8a44cbd7f50)
- Fixed the error in the return value of BLAKE2s's EVP_MD_get_size() so that it correctly returns the output size of BLAKE2s. (Architecture-related: public API)
  ↳ No PR: [11e61b3](https://github.com/openssl/openssl/commit/11e61b3174762ec21ce0875a6449c61e316b4a0b)
- Added necessary null pointer check to EVP_CIPHER API to prevent segfault caused by accessing null pointer when cipher is not initialized. (Architecture-related: public API)
  ↳ No PR: [6f22bcd](https://github.com/openssl/openssl/commit/6f22bcd631ab622c2436bc5b299ba2677c388375)
- Removed support for OSSL_MAC_PARAM_DIGEST_NOINIT and OSSL_MAC_PARAM_DIGEST_ONESHOT flags, marked them as deprecated and ignored, fixed segfault caused by calling EVP_MAC_init. (Architecture-related: public API)
  ↳ No PR: [62457fd](https://github.com/openssl/openssl/commit/62457fd9415d707baf76f219bbb9a29106ba092b)
- Fixed some block encryption issues in CFB and OFB modes on the s390x platform, using the processed bytes information in the common cipher context instead to ensure that the information can be correctly reset when the context is reinitialized. (Architecture-related: platform compatibility)
  ↳ No PR: [576a357](https://github.com/openssl/openssl/commit/576a3572bebf6115df1c03527114cbf74d06f861), [f9ccd20](https://github.com/openssl/openssl/commit/f9ccd209c3d121668c51a992613c698f2a774cb3)
- Fixed the error reporting of EVP_PKEY_sign, EVP_PKEY_verify and EVP_PKEY_verify_recover functions when passing in an empty context, now correctly returning an empty parameter error, and returning an operation not supported error when provider support is missing. (Architecture-related: public API)
  ↳ No PR: [5a25177](https://github.com/openssl/openssl/commit/5a25177d1b07ef6e754fec1747b57ee90ab1e028)
- Fixed the problem that memory corruption may occur due to changes in signature length when passing in a NULL signature buffer in ECDSA_sign, DSA_sign and other functions. Instead, the required signature length is returned directly; at the same time, the SM2 internal signature function returns an error when sig is NULL. (Architecture-related: public API)
  ↳ No PR: [be47176](https://github.com/openssl/openssl/commit/be4717602dbd387ef4de6ab0a2311881fe31a67a)
- Implemented Pairwise Consistency Test (PCT) for EDDSA, performs signing and verification operations after key generation, and unified it for EVP_PKEY_keygen and EVP_PKEY_pairwise_check. (Architecture-related: public API)
  ↳ No PR: [fbce6eb](https://github.com/openssl/openssl/commit/fbce6ebf706cdd273f2569edfea7ade106426e0b)
- Based on the code audit results, additional hardening checks have been added to HPKE internal implementation, including stricter parameter verification, improved error code usage, and optimization of randomly selected functions. (Architecture-related: HPKE interface hardening)
  ↳ No PR: [a1c0306](https://github.com/openssl/openssl/commit/a1c0306895bf6cf28056aaf9cd22cb3b65d4bb0a)

### Core Services (Memory, Error Handling, Threading)
- Added AES implementation based on Zvkned extension for RISC-V 64-bit architecture, supporting OCB and XTS modes. (Architecture-related: platform compatibility)
  ↳ No PR: [f6631e3](https://github.com/openssl/openssl/commit/f6631e38f901e2a439604fac2bd62933f9dbb8ad)
- Add vector extension support to RISC-V, detect and cache vector register lengths at runtime. (Architecture-related: platform compatibility)
  ↳ No PR: [cdea671](https://github.com/openssl/openssl/commit/cdea67193da8aab0f1a49d2b7ce144ad21bfc51d)
- Added settable parameter OSSL_ASYM_CIPHER_PARAM_OAEP_DIGEST_PROPS for RSA asymmetric encryption. (Architecture-related: public API)
  ↳ No PR: [2618361](https://github.com/openssl/openssl/commit/26183614ed1dc03f509f26839b8a465684ca0f84)
- Add AES-ECB, AES-CTR encryption function and AES-GCM vector encryption implementation based on Zvkned and Zvkb extensions for RISC-V platform. (Architecture-related: platform compatibility)
  ↳ No PR: [18ed3a5](https://github.com/openssl/openssl/commit/18ed3a58b01f8f1affdedced1f4f62447b7df9f9), [d056e90](https://github.com/openssl/openssl/commit/d056e90ee58a039263b843e8fa330fa71b4d4835)
- Added unbiased random integer range generation functions ossl_rand_uniform_uint32 and ossl_rand_range_uint32. (Architecture-related: public API: ossl_rand_uniform_uint32, etc.)
  ↳ No PR: [55755fb](https://github.com/openssl/openssl/commit/55755fbf42ec073e86651065c5cce6f64662c9e6), [dfb26e0](https://github.com/openssl/openssl/commit/dfb26e03c26b9234d04cb9fcaf6391d6bfb44dc4)
- Added ERR_pop function to pop the top error entry from the error status stack. (Architecture-related: public API)
  ↳ No PR: [5304d56](https://github.com/openssl/openssl/commit/5304d563359648ae2910cad4f9badc5dd1fc0210)
- Added thread-safe X509_STORE_get1_objects function, which returns a reference-counted copy of the stored object. (Architecture-related: public API)
  ↳ No PR: [08cecb4](https://github.com/openssl/openssl/commit/08cecb4448e990f7914ec1df97b1ee0ca9031643)
- Introduced RCU lock implementation as an alternative lock mechanism for OpenSSL, and added corresponding test cases. (Architecture-related: RCU lock mechanism)
  ↳ No PR: [d0e1a0a](https://github.com/openssl/openssl/commit/d0e1a0ae701cfaca7f3dd3bf28a3f934a6408813), [c4e6046](https://github.com/openssl/openssl/commit/c4e6046db73b451ffb8c20374b22c5732ed512c7), [d2514d5](https://github.com/openssl/openssl/commit/d2514d5ef28a76bfe0f87711dad0f1a5924e7e00)
- Add content type OID (id-ct-rpkiSignedPrefixList) to the RPKI signature prefix list, and update the related object identifier table. (Architecture-related: public API)
  ↳ No PR: [c5e097d](https://github.com/openssl/openssl/commit/c5e097dec5e93828837f4208c6968a0b7f38291e)
- Fix %n format specifier warning when cross-compiling, optimize path length calculation and buffer allocation. (Architecture-related: platform compatibility)
  ↳ No PR: [ec0d22f](https://github.com/openssl/openssl/commit/ec0d22fe1571508c08b714715cfdb6ac60c53f78)
- Added read lock protection to the CRYPTO_secure_used function, and fixed the problem of unlocked access to shared variables. (Architecture-related: public API)
  ↳ No PR: [7eae6ee](https://github.com/openssl/openssl/commit/7eae6ee0e503b0961d4f2e75baac981f2766b892)
- Introduce hash thunking function, fix ubsan undefined behavior warning caused by function pointer type mismatch by wrapping callback call. (Architecture-related: public API)
  ↳ No PR: [5c42ced](https://github.com/openssl/openssl/commit/5c42ced0ff974a59af98b75e54136f4282718266)
- Fixed the problem that the BN_GF2m_mod_inv function caused an infinite loop when the parameter p was 1, and added input validity check. (Architecture-related: public API)
  ↳ No PR: [9c1b8f1](https://github.com/openssl/openssl/commit/9c1b8f17ce2471ca37ee3936d07aed29aab10975), [b83c719](https://github.com/openssl/openssl/commit/b83c719ecb884f609ade7ad7f52bd5e09737585b)
- Fixed the length overflow problem that may be caused by the strlen() return value being stored in int in the OSSL_PARAM_BLD_push_utf8_string and OSSL_PARAM_BLD_push_utf8_ptr functions in param_build.c, and added a length check. (Architecture-related: public API)
  ↳ No PR: [d4d6694](https://github.com/openssl/openssl/commit/d4d6694aa710c9970410a6836070daa6486a0ac0)
- Added a null pointer check to the integer type getter function of OSSL_PARAM to prevent dereference crashes when the parameter data is NULL, and added corresponding test cases. (Architecture-related: public API)
  ↳ No PR: [806bbaf](https://github.com/openssl/openssl/commit/806bbafe2df5b699feac6ef26e50c14e701950cf)
- Fixed the issue where OSSL_PARAM_allocate_from_text() failed to correctly report an error when inputting an odd number of hexadecimal digits, and added related tests. (Architecture-related: public API)
  ↳ No PR: [ea6268c](https://github.com/openssl/openssl/commit/ea6268cfceaba24328d66bd14bfc97c4fac14a58)
- Fixed the problem of incorrect parameter list of CRYPTO_DOWN_REF function when compiling with Intel C++ compiler on Windows. (Architecture-related: Platform compatibility)
  ↳ No PR: [20ddfe7](https://github.com/openssl/openssl/commit/20ddfe78e9ddc0aba8208616e1b0b33cb12f77f5)
- Fixed the problem of QUIC QLOG getting process ID on Windows, use GetCurrentProcessId() instead. (Architecture-related: platform compatibility)
  ↳ No PR: [1548e3c](https://github.com/openssl/openssl/commit/1548e3cdaa3d478bdfbb214855a537be184db89f)
- The recvmmsg datagram method is disabled in versions below Android 5, because this API is only supported from API Level 21. (Architecture-related: platform compatibility)
  ↳ No PR: [f2de18a](https://github.com/openssl/openssl/commit/f2de18a30d25bf19236963ff72c02833ae41be40)
- Fixed the issue where crl and req commands did not exit correctly and returned non-zero status when verification failed, and will now exit with exit code 1. (Architecture-related: external behavior)
  ↳ No PR: [8aa52c1](https://github.com/openssl/openssl/commit/8aa52c1185e5ec540c7f2f0cb3d5b1f9a0070871)
- Fixed the OSSL_sleep implementation of the NonStop PUT model, introduced sleep() and removed the deprecated SPT model support. (Architecture-related: platform compatibility)
  ↳ No PR: [10ea99b](https://github.com/openssl/openssl/commit/10ea99bb4b65aba7e0fd139c40c0782b73dd66d6)
- Fixed the issue where sleep(0) on NonStop platform caused abnormal thread context switching. (Architecture-related: platform compatibility)
  ↳ No PR: [c89fe57](https://github.com/openssl/openssl/commit/c89fe574493f438dd0e94bb9a89227e4ca84c0b7)
- Changed the return value of OPENSSL_sk_push from -1 to 0 when NULL is passed in, simplifying the calling logic. (Architecture-related: public API behavior changes)
  ↳ No PR: [98d6016](https://github.com/openssl/openssl/commit/98d6016afec4c0bc7bb8f33b5061beb8528cc74a)
- Replace the read-write lock implementation of CONF_MOD API with RCU lock to demonstrate the use of RCU lock. (Architecture-related: thread safety model changes)
  ↳ No PR: [504e72f](https://github.com/openssl/openssl/commit/504e72fc1a1432d5266bd6e8909648c49884a36c)
- Optimize AES-CTR performance for ARM Neoverse V1 and V2, expand loops to up to 12 blocks to fully utilize AES pipeline resources, and add support for Apple M3 and Microsoft Cobalt 100 processors. (Architecture-related: Platform compatibility)
  ↳ No PR: [cc82b09](https://github.com/openssl/openssl/commit/cc82b09cbde0b809d37c23cb1ef9f1f41fc7f959)
- Enable AES-GCM unroll8 optimization for Microsoft Azure Cobalt 100 platform, improving performance by 18% to 32%. (Architecture-related: platform compatibility)
  ↳ No PR: [11adf9a](https://github.com/openssl/openssl/commit/11adf9a75d6b34723d1a20a0da4e4100ea6ca593)
- Removed support for the SPT thread model from the NonStop platform and rolled back the changes previously introduced to support this model. (Architecture-related: Platform compatibility)
  ↳ No PR: [5cd1792](https://github.com/openssl/openssl/commit/5cd17920167a8b4f7a81722a1ed3b514115702de)
- Fixed the struct timeval header file inclusion conflict under Windows platform, only including winsock2.h when winsock.h or winsock2.h is not included (architecture-related: platform compatibility)
  ↳ No PR: [b0e9d03](https://github.com/openssl/openssl/commit/b0e9d0370262ade64c55f2385fbb09ec6aa81e76)
- Added a build-time configuration option to control whether to use atexit() to register OPENSSL_cleanup() to solve compatibility issues on specific platforms; also updated related documentation and CI configuration. (Architecture-related: Build Configuration)
  ↳ No PR: [99fb31c](https://github.com/openssl/openssl/commit/99fb31c167e322186c6f576cfaa8f433f4fed117)
- Fixed build failure on FreeBSD variants due to missing ipi_spec_dst field in in_pktinfo structure, setting of which is skipped by conditional compilation. (Architecture-related: Platform compatibility)
  ↳ No PR: [b5e076b](https://github.com/openssl/openssl/commit/b5e076bee3c0445c108a6a35f077083ee42f9d80)

### Low-Level Cryptographic Implementations
- Corrected AES-GCM related function and macro definitions, changed the dependent RISC-V vector extension from zvbb to zvkb. (Architecture-related: platform compatibility)
  ↳ No PR: [ebecf32](https://github.com/openssl/openssl/commit/ebecf322e52bf3cabaf36335c138712ae658503f)
- Fix an issue in DSA parameter generation where invalid gen_type values may be assigned to the context, and add assertions in the generation function to verify the valid range of gen_type. (Architecture-related: public API)
  ↳ No PR: [5056133](https://github.com/openssl/openssl/commit/5056133cc7d6c52033c25b2e1f7762bcafcce760)
- Fixed the build error when disabling assembly (disable-asm) on the s390x platform to avoid link failure caused by defining the S390X_MOD_EXP macro. (Architecture-related: platform compatibility)
  ↳ No PR: [a5b0c56](https://github.com/openssl/openssl/commit/a5b0c568dbefddd154f99011d7ce76cfbfadb67a)
- Added optimized AES-128/192/256-CBC encryption and decryption function declarations for the RISC-V platform, replacing the old implementation. (Architecture-related: public API)
  ↳ No PR: [562b4eb](https://github.com/openssl/openssl/commit/562b4eb4c131b7c639abbc1a93d40de497f32a0f)
- Added security checks for excessively large modulus P and Q to DH_check_pub_key() and DH_generate_key(), and added corresponding error codes. (Architecture-related: DH interface security enhancement)
  ↳ No PR: [ec061bf](https://github.com/openssl/openssl/commit/ec061bf8ff2add8050599058557178c03295bcc0)
- Disabled hardware accelerated AES builds on PPC Mac platforms. (Architecture-related: Platform Compatibility)
  ↳ No PR: [493ad48](https://github.com/openssl/openssl/commit/493ad484e9312b54d177d85e2f4aa0b636e708f0)

### Data Encoding and Parsing Layer (ASN.1, PEM, DER)
- Fixed an error in X509_load_cert_file_ex() due to reference counting issues when loading multiple PEM format certificates. (Schema related: public API)
  ↳ No PR: [20c680d](https://github.com/openssl/openssl/commit/20c680de9c435534be48fa85b2a975067a4e7c9d)
- Added a null pointer check for the cleanup and construct functions in the OSSL_ENCODER_to_bio function. If it is not set, it returns 0 and reports an initialization failure. (Architecture-related: public API)
  ↳ No PR: [cf57c3e](https://github.com/openssl/openssl/commit/cf57c3ecfa416afbc47d36633981034809ee6792)
- Fixed multiple memory leaks in X.509 SXNET extensions, including leaks in SXNET_add_id_asc, SXNET_add_id_ulong and sxnet_v2i functions. (Architecture-related: public API)
  ↳ No PR: [7054fc1](https://github.com/openssl/openssl/commit/7054fc1ca3945342777f588fba43b77f669509ad), [0151e77](https://github.com/openssl/openssl/commit/0151e772195fc03cce0f12e5e266e51dc15243a0), [3980118](https://github.com/openssl/openssl/commit/398011848468c7e8e481b295f7904afc30934217)
- Fixed the null pointer dereference crash problem in PKCS12 and PKCS7 due to the possible null content of ContentInfo data. (Architecture-related: public API)
  ↳ No PR: [041962b](https://github.com/openssl/openssl/commit/041962b429ebe748c8b6b7922980dfb6decfef26)
- Added minimum length check for GeneralizedTime and UTCTime to prevent too short time strings from being parsed incorrectly. (Architecture-related: parsing behavior)
  ↳ No PR: [eadd8c4](https://github.com/openssl/openssl/commit/eadd8c4727b703049e4d2764751cb04f3108434d)
- Fixed the problem that the ASN1_mbstring_ncopy function did not correctly clean up the output parameters in the error handling path to avoid potential use-after-free vulnerabilities. (Architecture-related: ASN1_mbstring_ncopy fix)
  ↳ No PR: [73ebaac](https://github.com/openssl/openssl/commit/73ebaac827180bb51ccf807673758d7d06d5db21)

## Routine Changes

### New features
- The -geninfo option for CMP applications now supports multiple ITAV and string type values.
  ↳ No PR: [0739dd0](https://github.com/openssl/openssl/commit/0739dd0022cc747cd7c8a2de043e1f513472310c)
- Added support for AES-192 to RISC-V vector AES implementation and fallback to universal key generation in OCB and XTS modes.
  ↳ No PR: [94474e0](https://github.com/openssl/openssl/commit/94474e02fa217c037ece9d819a9b12025f65cdb9)
- Added -reqout_only option for CMP client applications to only dump or save the initial request without actually sending it.
  ↳ No PR: [2fbe23b](https://github.com/openssl/openssl/commit/2fbe23bbbe52bd35fb85abde50e538fb92e5e2b1)
- Improved the -reqin option so that it can read the alternate public key from the first request message file, and optimized error prompts and warnings.
  ↳ No PR: [d6d9277](https://github.com/openssl/openssl/commit/d6d9277b2e61a99aaa01a6c1f89ceb10a1422249), [904ee65](https://github.com/openssl/openssl/commit/904ee652902e157a921881bf844c57b4dd4bfdd9)
- Added monotonically increasing datagram ID support to QUIC demultiplexing and receive paths and exposed them to upper layers.
  ↳ No PR: [266a827](https://github.com/openssl/openssl/commit/266a827d816c204d85ef04ce5d028a61d8e2b187), [285a76b](https://github.com/openssl/openssl/commit/285a76bda02192818cedc2a7db8ff54bbd6a3586)
- The openssl rand command now supports specifying the number of bytes using the k, m, g suffixes.
  ↳ No PR: [ae9fe65](https://github.com/openssl/openssl/commit/ae9fe65d9f85e027bd7428e0f84aa46ab368880e)
- Added the ability to dynamically change QLOG instances for QUIC's FIFD, QTX and TXP components, allowing QLOG to be set after instantiation.
  ↳ No PR: [484b8bd](https://github.com/openssl/openssl/commit/484b8bd0f550da8728000dc4c9e36cb273296f73), [4a3a925](https://github.com/openssl/openssl/commit/4a3a9257db012adbfbc7b854f18dc00fad23c6c4), [572c449](https://github.com/openssl/openssl/commit/572c449a10697d8424a6117df807700a688d753d), [434d52a](https://github.com/openssl/openssl/commit/434d52a4b693c1f9fc008826ba2c7cceedb74964)
- Added new RCID creation function to QUIC remote connection ID manager, increased maximum connection ID limit, and adjusted retirement counting logic.
  ↳ No PR: [9eabb30](https://github.com/openssl/openssl/commit/9eabb30ab4491bdcf49c5bfeef659ca846da5160)
- Use untrusted certificate chains in OCSP requests instead to generate valid certificate IDs.
  ↳ No PR: [d6aafeb](https://github.com/openssl/openssl/commit/d6aafeb1076ed4eeda1b0ced11207e05b0e32b0d)
- Added -set_issuer option to the openssl x509 command to override the certificate issuer name and use -subj as an alias for -set_subject.
  ↳ No PR: [4e5bf93](https://github.com/openssl/openssl/commit/4e5bf933131863e0459d7b39931d464fef77b078)
- Added missing -rand option support to genpkey command.
  ↳ No PR: [7698f80](https://github.com/openssl/openssl/commit/7698f80ab17190be8d6950d8836222a375245ed8)
- Added ossl_qtx_set_qlog_cb callback interface, allowing QLOG instances to be obtained through callbacks.
  ↳ No PR: [9f2349a](https://github.com/openssl/openssl/commit/9f2349aebe04c0af54a5ba7ede6b1dcd6bee2124)
- Added query capabilities for write buffer size, used space and free space for QUIC streams.
  ↳ No PR: [b317583](https://github.com/openssl/openssl/commit/b317583f4ad8a8e742781381fa10db5bcd072585), [7b4436a](https://github.com/openssl/openssl/commit/7b4436a7cb23bd9ee2736336f40d2f2834c4965a), [bf7ae25](https://github.com/openssl/openssl/commit/bf7ae259a405a642dee93b18ffe5b875a056045a)
- Added support for UTF-8 multibyte sequences in the JSON encoder.
  ↳ No PR: [bc3eb7b](https://github.com/openssl/openssl/commit/bc3eb7b52789bdea457e4fdff6e25da340c88901), [b3706fd](https://github.com/openssl/openssl/commit/b3706fd7e23c59e0f2e737ec29a5df77e585d878)
- Added bandwidth limiting support for noisy datagram BIO filter.
  ↳ No PR: [37ffd4a](https://github.com/openssl/openssl/commit/37ffd4a1fa02b37919b5c7a8059ba57d3c49b1f0)
- Added Known Answer Test (KAT) support for KBKDF and KMAC128 combination.
  ↳ No PR: [3cb0755](https://github.com/openssl/openssl/commit/3cb0755323281267211fbe951b94a2552e99d32a)
- Added credit accessor for QUIC Receive Flow Control (RXFC), and adjusted the related interface to const pointer.
  ↳ No PR: [a774062](https://github.com/openssl/openssl/commit/a774062466d3d2d2908c4f076a9cbbd2cb00738a)
- Added several new term definitions to the QUIC glossary, including ODCID, QUIC_CHANNEL, QUIC_ENGINE and QUIC_PORT.
  ↳ No PR: [cd4edeb](https://github.com/openssl/openssl/commit/cd4edeb2f75dd12bb42c1b8886204a7a4029323b), [f41ab29](https://github.com/openssl/openssl/commit/f41ab29c787cf438ef58e97c5b308dac8470de52)
- Added riscv64 architecture target in Android configuration support.
  ↳ No PR: [2d32144](https://github.com/openssl/openssl/commit/2d321448b245a239c49a54e31cbd9d97a14b5d4e)

### bug fixes
- Fixed the problem of using wrong constants in nmflag comparison in X509_print_ex and X509_REQ_print_ex functions, corrected the return value judgment logic, and removed useless assignments.
  ↳ No PR: [da2dd3b](https://github.com/openssl/openssl/commit/da2dd3b51ddd69aae0fd840c0d23afa954c24ded), [2b5e028](https://github.com/openssl/openssl/commit/2b5e028a2f70de216458a5140bcf4ec3d9236eeb), [2126ca3](https://github.com/openssl/openssl/commit/2126ca3dba3907f49b232442c06db1cae8bee0c3)
- Make the CMP application's -ignore_keyusage option effective also for impersonated servers.
  ↳ No PR: [fd51437](https://github.com/openssl/openssl/commit/fd514375e22d3039ab0ab12e3017aadf2c38b761)
- Fix the memory leak caused by the failed call of EVP_PKEY_CTX_set0_rsa_oaep_label in the rsa_cms_decrypt function, and ensure that the label is released when it fails.
  ↳ No PR: [d32dd65](https://github.com/openssl/openssl/commit/d32dd65053431ee744d213b336b9a03a035807e6)
- Fix the logic of request ID validity check in CMP to avoid conflict between OSSL_CMP_CERTREQID_NONE and error return value.
  ↳ No PR: [1d61a03](https://github.com/openssl/openssl/commit/1d61a03794326fc4e4605e98343b784058cb453e)
- Add release logic of QLOG header field for SSL_CTX to support header setting function.
  ↳ No PR: [fb1a0bb](https://github.com/openssl/openssl/commit/fb1a0bb97aa630cd303d9c7c30214483538a57f6)
- Fix the AES-XTS key length check condition to correctly match key lengths containing two sets of keys, and correct the hardware declaration macro definition.
  ↳ No PR: [a5871e9](https://github.com/openssl/openssl/commit/a5871e951d3f3c3f0c498a0420c5ce1f53c425a5)
- Fix undefined behavior that may result when session->cipher is empty, add assertion check.
  ↳ No PR: [9890cc4](https://github.com/openssl/openssl/commit/9890cc42daff5e2d0cad01ac4bf78c391f599a6e)
- Fixed errors that may occur when the return value is aliased with the modulus or exponential parameter in modular arithmetic, and added related tests.
  ↳ No PR: [af0025f](https://github.com/openssl/openssl/commit/af0025fc40779cc98c06db7e29936f9d5de8cc9e)
- Adjust the bit value of FFC internal check flag to avoid conflict with the public DH check flag.
  ↳ No PR: [bc224e7](https://github.com/openssl/openssl/commit/bc224e7edf87bbb353d51e9cb5c5999af8828856)
- Fixed the issue in CMS and PKCS7 that EVP_PKEY_get_size() returns zero value incorrectly to avoid allocating zero-length memory causing errors.
  ↳ No PR: [d7ad09d](https://github.com/openssl/openssl/commit/d7ad09da778bcc0090a7cdfd87edb56eea22382b)
- Fix the null value check of the SSL_CONNECTION pointer in ossl_ctrl_internal to prevent null pointer dereference.
  ↳ No PR: [8dc82c0](https://github.com/openssl/openssl/commit/8dc82c02559545fabe15fd95d55623f4f7fc0f08), [24844be](https://github.com/openssl/openssl/commit/24844be16f0e4c30ae3386760ff571592b14b02f), [b9788ce](https://github.com/openssl/openssl/commit/b9788ce6a869185f040df4c98d2e7143110aa517)
- Fix memory leak when X509_ALGOR creation fails in RSA OAEP encryption.
  ↳ No PR: [83efd71](https://github.com/openssl/openssl/commit/83efd7170bfa48a3263fcf8c771a6029646e8ad2)
- Fix the error handling of HTTP client response length check to ensure that failure is returned correctly when the length exceeds the limit or is inconsistent.
  ↳ No PR: [e2f69d4](https://github.com/openssl/openssl/commit/e2f69d435bdc263fa4c30ee77484a0d2f6a8ff46)
- Reject integer transmission parameters with extra trailing bytes to enhance parsing robustness.
  ↳ No PR: [05937a7](https://github.com/openssl/openssl/commit/05937a70a14520a70e830af63aba4283ac6f3878)
- Fix use of uninitialized variables in TLS extension parsing.
  ↳ No PR: [f62fec6](https://github.com/openssl/openssl/commit/f62fec64049959cee6b80043cd697d0e7357a24a)
- Fixed the problem of not checking the null pointer when QUIC_TLS object is released, so that the release function can tolerate null pointers.
  ↳ No PR: [8d13d9e](https://github.com/openssl/openssl/commit/8d13d9e7305643c28c69c57df798b553b78c2876)
- Fixed the problem that packet loss may be misjudged when the packet loss detection timer is triggered. Packet loss processing will only be performed when packet loss is actually detected.
  ↳ No PR: [10dfd79](https://github.com/openssl/openssl/commit/10dfd796c9c25dd78aa88cf84629a0418b8f0866)
- Fixed an issue where quicserver was unable to bind a socket when a duplicate address entry existed, causing it to skip the address and continue trying if the binding failed.
  ↳ No PR: [fe26b6b](https://github.com/openssl/openssl/commit/fe26b6b4961b1d5a560b52463923f6fb014f5068)
- Fixed quicserver getting stuck in an infinite loop when handshake or receiving request fails, it will now terminate the server and report an error.
  ↳ No PR: [ddf84fc](https://github.com/openssl/openssl/commit/ddf84fc47e3a01047e2a4001289143cc689eed84)
- Fixed an issue where s_client received an error when receiving data that was exactly equal to the maximum capacity of the buffer. Now it is allowed to receive the full size without triggering an error.
  ↳ No PR: [74ff15e](https://github.com/openssl/openssl/commit/74ff15e1a1987686812c465ee3200bc25efa0e8f)
- Repair the drainage calculation logic in QUIC TXP, remove the obsolete parameters, and directly judge based on the status of the stream buffer.
  ↳ No PR: [2665289](https://github.com/openssl/openssl/commit/266528965f716be809a6e15bb5adfa659b56f9bb)
- Fixed the memory leak in the ossl_quic_new function and optimized the error handling path.
  ↳ No PR: [55936ee](https://github.com/openssl/openssl/commit/55936eee86ce31e80fa49d11757f61fe9e20821e)
- Fixed an issue where the want_ack flag for a specific pn_space was not properly checked when generating ACK frames, to avoid creating ACK frames when not expected.
  ↳ No PR: [d13488b](https://github.com/openssl/openssl/commit/d13488b93690121bd50c97599760a19ead6bcd1f)
- Fixed the issue where ossl_quic_sstream_is_totally_acked incorrectly returns 0 when no data is appended to the stream, and added a test.
  ↳ No PR: [115ee28](https://github.com/openssl/openssl/commit/115ee28263c28c78a34ce4e40a9e4be8361deee6)
- Fix a memory leak that could occur when loading built-in compression methods.
  ↳ No PR: [daf26c2](https://github.com/openssl/openssl/commit/daf26c2d7a4d29ec1040fc0d5d4215cfc2dcf4a7)
- Fixed the misuse of likely macro in rand_uniform, corrected the incorrect unlikely to likely.
  ↳ No PR: [b90662b](https://github.com/openssl/openssl/commit/b90662b4b0a6c7b6979a96581388ace7c217b470)
- Fix and strengthen QUIC connection ID length validation to prevent out-of-bounds access and ensure compliance with specifications.
  ↳ No PR: [a35956b](https://github.com/openssl/openssl/commit/a35956b2f7749a8c7a199bdb416a02912d6e33e3), [935aa14](https://github.com/openssl/openssl/commit/935aa14344470d8a6936c8f174c15767cbd5f402)
- Fixed the problem of incorrect original length tracking due to flow control in stream frame generation, ensuring correct judgment on whether to continue serializing the next data block.
  ↳ No PR: [e718b24](https://github.com/openssl/openssl/commit/e718b248f94fa41562b740482813716a2ff13db5)
- Fixed an issue where key slots may be leaked under error conditions, ensuring that the corresponding key slots are properly cleared during error handling.
  ↳ No PR: [0c2aabb](https://github.com/openssl/openssl/commit/0c2aabbaeacf1cc9864daaed11fae755fe7bc025)
- Fixed a potential problem with null pointer dereference in ossl_quic_new(), which directly returns NULL in the cleanup path instead of jumping to error handling.
  ↳ No PR: [0e2e4b3](https://github.com/openssl/openssl/commit/0e2e4b3e69d4012f47b6908c2d8a13ec4e2d40e0)
- Fixed bug when implicit length STREAM frames coexist with PATH_RESPONSE frames in QUIC transport, adjusted padding generation logic and stream-related frame generation.
  ↳ No PR: [3bef14c](https://github.com/openssl/openssl/commit/3bef14c5367b4e2d7aded4f80e78e8f19b74f710)
- Fixed the problem of incorrect padding processing of ACK_ONLY type packets in QUIC transmission, avoided incorrectly adding padding in ACK_ONLY mode, and adjusted the handshake status update logic.
  ↳ No PR: [e1c15a8](https://github.com/openssl/openssl/commit/e1c15a8abeb87a387cc7c64a424ca5f282b00632)
- Enhanced the robustness of QUIC SRTM when memory allocation fails, adding failure checks and returning errors in add, remove and clean operations.
  ↳ No PR: [8fff2e3](https://github.com/openssl/openssl/commit/8fff2e39bc77ec53020942daf16821961df86939), [f328adf](https://github.com/openssl/openssl/commit/f328adff43c5916e149abd598f06898ecd4762f5)
- Fixed a possible memory leak problem in ssl->s3.tmp.psk.
  ↳ No PR: [a2b1ab6](https://github.com/openssl/openssl/commit/a2b1ab6100d5f0fb50b61d241471eea087415632)
- Fixed a memory leak caused by custom extension resources not being released on the wrong path in the custom_ext_add function.
  ↳ No PR: [668a144](https://github.com/openssl/openssl/commit/668a144f0a6dcfb9f904043c29372cbf19856c39)
- Fixed the defect in the priority queue removal function that the free slot was not properly reclaimed when the element was the last one in the heap.
  ↳ No PR: [a031087](https://github.com/openssl/openssl/commit/a03108778044cc0d428ce38084ef6f318446fbe3)
- Fixed null pointer checking logic in QUIC RCIDM and ensures the current RCID is retired correctly when handling retirement.
  ↳ No PR: [3fe0899](https://github.com/openssl/openssl/commit/3fe0899ab7c1c1727a9fe0d3981f658262283690)
- Fixed the upper limit on output size in the BLAKE2 algorithm so that it uses the default number of output bytes of the corresponding variant.
  ↳ No PR: [66c27d0](https://github.com/openssl/openssl/commit/66c27d06e0e9a1bb716c67390ad9e5ac613d45d3)
- Fixed an issue where packets were not correctly marked as full when QUIC streams used implicit length, resulting in the possible incorrect addition of more stream-related frames.
  ↳ No PR: [7fe3010](https://github.com/openssl/openssl/commit/7fe3010471a3263b2469ae35589357089050ce62)
- Fixed the issue in DTLS that hm_fragment was not initialized when allocated, to avoid crashes caused by accessing garbage data during release.
  ↳ No PR: [e59ed0b](https://github.com/openssl/openssl/commit/e59ed0bfeece9db433809af2cebbe271a402d59b)
- Extracted the duplicate connection ID generation function and adjusted the call, and fixed the condition check when qlog is initialized.
  ↳ No PR: [29fbdfa](https://github.com/openssl/openssl/commit/29fbdfafafcc5fa705f445a9f63ddd8207bf9f06)
- Allow errors to be tracked at the port level, and fixed a duplicate trigger issue in network error handling.
  ↳ No PR: [4df4add](https://github.com/openssl/openssl/commit/4df4add22d8acf09cdd8bd58614a9dc69284a1bb)
- Fixed the problem that the current write record layer may be released incorrectly when clearing the sent message queue, and moved the logic of releasing the old write record layer to dtls1_clear_sent_buffer.
  ↳ No PR: [a091bc6](https://github.com/openssl/openssl/commit/a091bc6022b23c0b1caf1c7acbb1f15bdf290816)
- Fixed the problem of recvfrom failure due to unbound socket on QUIC port under Windows. By adding sending status and server flag, it ensures that the client does not receive data before sending it.
  ↳ No PR: [3051339](https://github.com/openssl/openssl/commit/305133988742829f49e4d552f16ef09914317bdb)
- Fixed the tag length check logic in QUIC record sending, correctly returning zero when the available space is equal to the tag length.
  ↳ No PR: [46376fc](https://github.com/openssl/openssl/commit/46376fcf4b6d11ec417c2a530475037d4d09fcbf)
- Fixed possible memory leak in PKCS7_add0_attrib_signing_time: when internally created ASN1_TIME object was not released when adding signing attribute failed.
  ↳ No PR: [7d52539](https://github.com/openssl/openssl/commit/7d52539f00144cb410c4e9d8da0b9574c0badb19)
- Fixed a possible memory leak in the make_receipt_request function when CMS_ReceiptRequest creation failed, ensuring that rct_to and rct_from are released correctly.
  ↳ No PR: [bed7a87](https://github.com/openssl/openssl/commit/bed7a878107818c297301c6602013d364b266c67)
- Fixed a possible memory leak of X509 objects, public keys or TLSA records under multiple wrong paths in the dane_tlsa_add function.
  ↳ No PR: [e4a94bc](https://github.com/openssl/openssl/commit/e4a94bcc77f3fda0f185e62a73a66d9b9b9388f5)
- Fixed a memory leak in the PKCS7_add_attrib_smimecap function due to the ASN1_STRING object not being released.
  ↳ No PR: [ed3d277](https://github.com/openssl/openssl/commit/ed3d2771278cfa1c355b40c681f5acc8404156c6)
- Fixed possible memory leak in CMS_sign_receipt function, ensuring ASN1_OCTET_STRING object is released during error handling.
  ↳ No PR: [3e3aadd](https://github.com/openssl/openssl/commit/3e3aadd51cae1fbfb512cf4a0999d16c6a2888bd)
- Fixed a possible memory leak in the ct_move_scts function: no longer attempts to put the SCT object back to the source stack on failure, but directly releases the object.
  ↳ No PR: [a435d78](https://github.com/openssl/openssl/commit/a435d786046fabc85acdb89cbf47f154a09796e1)
- Fix the post-use release problem caused by repeated release in custom_exts_free, and reset the pointer and count after release.
  ↳ No PR: [bc0773b](https://github.com/openssl/openssl/commit/bc0773bbbd4d3ace6957385f1f22a5cda25dc94f)
- Fix memory leak for propq field in SM2 signing context: properly free propq in release function, and copy the field safely in copy function.
  ↳ No PR: [e7d34d7](https://github.com/openssl/openssl/commit/e7d34d7ae32f16abbd79a49072cff580bee32269)
- Fixed the double release problem in DANE certificate processing, and adjusted the certificate release logic in specific scenarios.
  ↳ No PR: [f636e7e](https://github.com/openssl/openssl/commit/f636e7e6bd8e06c6d84e42729b4131b4f5df488f)
- Fix strict alias violation due to type pun in NIST prime modulo arithmetic, by introducing memcpy helper function to safely load/store 32-bit words.
  ↳ No PR: [990d9ff](https://github.com/openssl/openssl/commit/990d9ff508070757912c000f0c4132dbb5a0bb0a)
- Fix incorrect static variable declaration in QUIC TSERVER.
  ↳ No PR: [eadebcc](https://github.com/openssl/openssl/commit/eadebcc863f8ff4c7bfa140dc9fdf8c2d21b899d)
- Fix implementation of PreferNoDHEKEX option, handle it correctly in tls_parse_ctos_psk_kex_modes.
  ↳ No PR: [f290663](https://github.com/openssl/openssl/commit/f290663148ddddaffc0dc8737b08a244b49a76ba)
- Fix QUIC LCIDM robustness when LHASH operations fail, ensuring resources are properly cleaned up when memory allocation or hash table insertion fails.
  ↳ No PR: [2773749](https://github.com/openssl/openssl/commit/2773749772a385e3e7e8c0286c258f57534f385f)
- Fixed the issue where CMAC calls EVP_MAC_CTX_get_mac_size() before initialization causing a segfault, and adds a null pointer check.
  ↳ No PR: [ff18196](https://github.com/openssl/openssl/commit/ff181969e28c1503b077b47a9ded3683524b3fd8)
- Fixed issue where provider parameters were incorrectly set on ENGINE-based ciphers when the SSL context used ENGINE.
  ↳ No PR: [afcc12c](https://github.com/openssl/openssl/commit/afcc12c41ad82c5b63194502592de015604dbd47)
- Fix the crash caused by the output schedule being empty when the provider is initialized, and add a null pointer check.
  ↳ No PR: [8fa65a6](https://github.com/openssl/openssl/commit/8fa65a6648554087a67102372e5e6c8b0fae0158)
- Fixed the problem that the rehash tool could not handle long file names due to the use of NAME_MAX limit, and instead dynamically calculated the actual file name length to allocate a buffer.
  ↳ No PR: [de8e085](https://github.com/openssl/openssl/commit/de8e0851a1c0d22533801f081781a9f0be56c2c2)
- Fixed a memory leak problem that may be caused by not checking the sk_X509_push return value in the cms_main function.
  ↳ No PR: [3457a55](https://github.com/openssl/openssl/commit/3457a550c64ab8009c7cd0175675ac140cab33c2)
- Fix possible memory leak in smime_main: add check for sk_X509_push return value, jump to cleanup code on failure.
  ↳ No PR: [ba4d833](https://github.com/openssl/openssl/commit/ba4d833f6e24a83bc3e74ba55f52d8916b70fb59)
- Fixed the issue in the opt_verify function that caused the ASN1_OBJECT object to leak due to the failure of X509_VERIFY_PARAM_add0_policy.
  ↳ No PR: [d6688e4](https://github.com/openssl/openssl/commit/d6688e45fa2f987f3ffd324e19922468beee5ddc)
- Fixed ossl_decoder_cache_flush() no longer raising an error when the cache has been released to avoid false positives during the cleanup process.
  ↳ No PR: [0541fa7](https://github.com/openssl/openssl/commit/0541fa7802cf0c3a9b28d126066c909736fc5ec8)
- Fixed the priority issue of the -genstr/-genconf option in the asn1parse command to avoid blocking caused by trying to read PEM data from the standard input when the generated string is specified.
  ↳ No PR: [749fcc0](https://github.com/openssl/openssl/commit/749fcc0e3ce796474a15d6fac221e57daeacff1e)
- Fixed the uninitialized read problem caused by sscanf returning -1 when the input string is empty, and changed the return value check from == 0 to <= 0.
  ↳ No PR: [322517d](https://github.com/openssl/openssl/commit/322517d817ecb5c1a3a8b0e7e038fa146857b4d4)
- Fixed a segfault that caused null pointer dereference due to null values when parsing the stable section in the configuration file, and added corresponding test cases.
  ↳ No PR: [0981c20](https://github.com/openssl/openssl/commit/0981c20f8efa68bf9d68d7715280f83812c19a7e)
- Fixed the problem of improper use of LHASH in QUIC LCIDM, disabling shrinkage before traversing the hash table to avoid memory leaks caused by heavy hashing.
  ↳ No PR: [708b4fb](https://github.com/openssl/openssl/commit/708b4fb7088a3ffe5341c522e1763f5398631631)
- Fixed the problem that gen_type may be set to the invalid value -1 in DH parameter generation, by checking the search results before assigning the value, and adding assertions to verify the gen_type range.
  ↳ No PR: [b697864](https://github.com/openssl/openssl/commit/b697864cb85145ba39a1ef1192c0b8812947e8a3)
- Fix possible memory leaks in a2i_GENERAL_NAME and do_othername functions to ensure allocated resources are properly released on failed paths.
  ↳ No PR: [1c07821](https://github.com/openssl/openssl/commit/1c078212f1548d7f647a1f0f12ed6df257c85cc3)
- The pkcs12 command no longer forces configuration files to be loaded, and unnecessary configuration loading logic is removed.
  ↳ No PR: [58eeb43](https://github.com/openssl/openssl/commit/58eeb4350ca89c52d603b42119a0893129a25c09)
- When copying an ECX key, first check whether the public key exists, and then decide whether to copy the public key data.
  ↳ No PR: [aac531e](https://github.com/openssl/openssl/commit/aac531e5daa2edec5d47e702a7f115cf77fe07f9)
- Fixed the problem in SSL configuration processing that when a certain configuration item is wrong, the remaining configuration items will be skipped. Now all configuration items will continue to be applied and errors will be summarized.
  ↳ No PR: [69c067f](https://github.com/openssl/openssl/commit/69c067ffbc2c02295e20c90e557b6fcb2f7da69c)
- During the connection process, change the host name information from standard output to standard error output to avoid interfering with pipe forwarding.
  ↳ No PR: [8a1694f](https://github.com/openssl/openssl/commit/8a1694f22588c0777d642253ffdc307a61245d51)
- Fixed declspec alignment syntax, moving the alignment attribute from after the variable name to before the type.
  ↳ No PR: [dfd986b](https://github.com/openssl/openssl/commit/dfd986b6f5402e5646e42425d14f098ed6bc4544)
- Updated the comment tags in the QUIC port header file and fixed the port initialization logic to ensure that the port is always added to the engine's port list.
  ↳ No PR: [33ca076](https://github.com/openssl/openssl/commit/33ca07637246c832b91d60935a1a2fdf02653a02)
- Fixed an issue where the lack of default case in the IPAddressOrRange_cmp function may cause garbage data to be used for comparison.
  ↳ No PR: [a8df565](https://github.com/openssl/openssl/commit/a8df5651153e8e81fbaa8408dd1137232168997d)
- Repair and optimize QLOG module, including initialization timing, connection ID usage, buffer calculation and frame log parsing.
  ↳ No PR: [43a1288](https://github.com/openssl/openssl/commit/43a128875d8fe26aec35aef093d78fbcd06fd1ca), [29bd1e2](https://github.com/openssl/openssl/commit/29bd1e2d24603827da52ce664244fd871b59d1f2)
- Fixed an issue that caused assertion failure when calling EVP_<OBJ>_fetch with colon-separated names, instead returning an error; and added corresponding test cases.
  ↳ No PR: [94be985](https://github.com/openssl/openssl/commit/94be985cbcc1f0a5cf4f172d4a8d06c5c623122b)
- Added null value checking for configuration options during x509 extension creation to prevent crashes or undefined behavior caused by invalid settings.
  ↳ No PR: [bac7e68](https://github.com/openssl/openssl/commit/bac7e687d71b124b09ad6ad3e15be9b38c08a1ba)
- Fixed the length check error when the maximum fragment length extension is not negotiated in the KTLS scenario to avoid errors caused by the default value.
  ↳ No PR: [c1decd6](https://github.com/openssl/openssl/commit/c1decd62460072082833909a962892e5042b16bb)
- Corrected the conditional judgment of method cache settings in evp_fetch.c, using meth_id instead of name_id for checking.
  ↳ No PR: [da840c3](https://github.com/openssl/openssl/commit/da840c3775f52fc9766c654b5ad6ee031ffc9fd9)
- Fixed assertion failure in tls_common.c caused by incomplete record layer cleanup.
  ↳ No PR: [5fb0655](https://github.com/openssl/openssl/commit/5fb065589d3a4dfeeb6d48b0561ab3145ceb2127)
- Add a check on the return value of ASN1_OBJECT_new in the OBJ_create function. If the allocation fails, an error will be reported and returned.
  ↳ No PR: [6b92a96](https://github.com/openssl/openssl/commit/6b92a966e0de3ad848fcf11fbcab7ee8cae24ba1)
- Fixed undefined behavior causing arithmetic expressions to overflow due to left shifting of signed integers.
  ↳ No PR: [486ab0f](https://github.com/openssl/openssl/commit/486ab0fb003d05f89620662260486d31bd3faa8c)
- Fixed an error caused by the -rev option in s_server when used with DTLS.
  ↳ No PR: [575117e](https://github.com/openssl/openssl/commit/575117efe1e0eb8073c2d26ae3dff8926be00591)
- Fixed the bit clearing logic of the bit_set function in QLOG, and corrected the incorrectly used mask to the inverted mask.
  ↳ No PR: [0e6eb43](https://github.com/openssl/openssl/commit/0e6eb431e89fd733daece4997448b83df80185b4)
- Fixed using the wrong client/server version when selecting a method, preventing subsequent calls to SSL_set_accept_state() from unexpectedly failing.
  ↳ No PR: [a867140](https://github.com/openssl/openssl/commit/a86714041d8a5868c629e9027e28c6d1dacde5f9)
- Delayed QUIC channel transmission parameter generation, and fixed state transition and error code usage.
  ↳ No PR: [6961601](https://github.com/openssl/openssl/commit/69616017a613c7442fa51794d51f167b0de2fc9c)
- Fixed an error in idle timeout calculation in QUIC channels, and added a helper function to correctly handle timeout values.
  ↳ No PR: [693d9af](https://github.com/openssl/openssl/commit/693d9afef46dbde2f41464052bda994821f536ad)
- Fixed a memory leak in req_main caused by using BIO_free instead of BIO_free_all. When the private key is output to standard output through HARNESS_OSSL_PREFIX, out is the BIO stack. The entire stack is now released correctly.
  ↳ No PR: [ff78d94](https://github.com/openssl/openssl/commit/ff78d94b131d7bb3b761509d3ce0dd864b1420e3)
- Treat the QLOG environment variable as an empty string as the default filter.
  ↳ No PR: [a706658](https://github.com/openssl/openssl/commit/a70665852c72a1b6c3f5960ce48f51b83755276d)
- In the QUIC port receive path, advance the stateless reset check before the connection lookup to ensure that the client can correctly handle the stateless reset token frame.
  ↳ No PR: [d2e7855](https://github.com/openssl/openssl/commit/d2e7855f5bdb2f817f6adb7ce6562505ec244474)
- Fixed off-by-one error in EBCDIC encoding conversion in buf2hexstr_sep() function.
  ↳ No PR: [c5cc9c4](https://github.com/openssl/openssl/commit/c5cc9c419a0a8d97a44f01f95f0e213f56da4574)
- Fixed a memory leak caused by not cleaning up allocated resources when bind_afalg failed, calling afalg_destroy on the failed path to clean up.
  ↳ No PR: [729a149](https://github.com/openssl/openssl/commit/729a1496cc4cda669dea6501c991113c78f04560)
- Fixed the correct use of QLOG instances in QUIC channels on the server side, changing from directly setting QLOG to setting it through a callback function.
  ↳ No PR: [c55e144](https://github.com/openssl/openssl/commit/c55e144b89fc8f917a897bf0756d85d3ce372160)
- Fix default setting of wrong values when initializing JSON encoder.
  ↳ No PR: [67f9976](https://github.com/openssl/openssl/commit/67f997697a6a5fcb6996944a2732f65b5b83643b)
- Fix issues in QLOG filter lexical analysis, refresh JSON output on release, and correct length calculation of extracted strings.
  ↳ No PR: [3c067dc](https://github.com/openssl/openssl/commit/3c067dcb2c06278ea528f39337a405181df4a5cf)
- Allow overriding process ID for QUIC QLOG, and fix return value of event enablement check.
  ↳ No PR: [6cb0026](https://github.com/openssl/openssl/commit/6cb0026c634139b0e0aecb57691330b3bd7a475b)
- Fixed code indentation issue in QUIC QLOG.
  ↳ No PR: [f26feac](https://github.com/openssl/openssl/commit/f26feac7605c5c4f5626b857ab8308fc3c2fada9), [6d42be3](https://github.com/openssl/openssl/commit/6d42be3af76aa16586b3f32a176837ee4a4bb65b)
- Fixed missing spaces in error message.
  ↳ No PR: [0c2333d](https://github.com/openssl/openssl/commit/0c2333d3bd04fa09a16048816120da706612474d)
- Fixed the memory leak under the wrong path during DRBG initialization process, and ensured the correct release of resources by introducing a dedicated release function pointer.
  ↳ No PR: [cb4f7a6](https://github.com/openssl/openssl/commit/cb4f7a6ee053e8c51cf3ac35fee333d1f25552c0)
- Fixed an array index calculation error in the ossl_gf_mul function to prevent potential segfaults.
  ↳ No PR: [76cecff](https://github.com/openssl/openssl/commit/76cecff5e9bedb2bafc60062283f99722697082a)
- Fixed an issue where the x509 command still printed a "read from stdin" warning when input was redirected, which was only displayed when used in an interactive terminal.
  ↳ No PR: [5c846d3](https://github.com/openssl/openssl/commit/5c846d32d4a1dc7ee7934bc867b9941809b76beb)
- Fixed the processing problem when the sig parameter in the ossl_ecdsa_deterministic_sign function is NULL, and instead returns an error directly.
  ↳ No PR: [e4308e7](https://github.com/openssl/openssl/commit/e4308e7a98947c24e17a93de92147ee6815da581)
- The openssl engine -c command now correctly displays whether the engine supports the EC algorithm.
  ↳ No PR: [5d70f11](https://github.com/openssl/openssl/commit/5d70f11823e3d8b7214a1e094b8a4f744ad396f5)
- Fixed the ossl_json_flush() function to ensure it actually flushes the underlying BIO.
  ↳ No PR: [5fd1f46](https://github.com/openssl/openssl/commit/5fd1f46fb054ef583e070dd15d1b76e0f0fc910b)
- Modified the judgment logic of QUIC automatic tick, changing the check originally based on implicit event processing mode to non-explicit event processing mode.
  ↳ No PR: [a768a79](https://github.com/openssl/openssl/commit/a768a796f26ecebc12ac0bd9b86c5c30bfd9370b)
- Fixed a crash caused by not checking the null pointer when printing invalid PKCS12 certificates, and added a NULL judgment before accessing the encryption algorithm.
  ↳ No PR: [89ffd55](https://github.com/openssl/openssl/commit/89ffd5593124c90e36d8624ec269efa73add8d9e)
- Fixed an issue where subjectAltName=dirName syntax check failed in the -addext parameter of the openssl req command.
  ↳ No PR: [996ccb5](https://github.com/openssl/openssl/commit/996ccb5b1cdc4e041cad871a77126348810ba2f5)
- Fixed a possible memory leak when loading a CRL successfully.
  ↳ No PR: [6134e8e](https://github.com/openssl/openssl/commit/6134e8e6ddc25c403fd1fab3f510a850a8843e62)
- Fixed wrong function call in dasync_rsa_decrypt, corrected EVP_PKEY_meth_get_encrypt to EVP_PKEY_meth_get_decrypt.
  ↳ No PR: [c91f0ca](https://github.com/openssl/openssl/commit/c91f0ca95881d03a54aedee197bbf5ffffc02935)
- Fixed the problem of infinite memory growth caused by imperfect operation cache matching logic in no-cached-fetch compilation mode.
  ↳ No PR: [dc9bc6c](https://github.com/openssl/openssl/commit/dc9bc6c8e1bd329ead703417a2235ab3e97557ec)
- Fixed possible memory leak when module initialization fails.
  ↳ No PR: [707b54b](https://github.com/openssl/openssl/commit/707b54bee2abbfe94a80361ab97cf77e1e4746bb)
- Fixed the digest_length variable type conversion problem to avoid integer overflow caused by EVP_MD_get_size() returning negative numbers.
  ↳ No PR: [22a24b7](https://github.com/openssl/openssl/commit/22a24b793162154bffa6db266124fd031c10a144)
- Fixed digest_size type conversion issue and added validity check for EVP_MD_get_size() return value.
  ↳ No PR: [022249e](https://github.com/openssl/openssl/commit/022249e95bad97eb838e75f949876c760a9a0c24)
- Fixed build failure of demos/sslecho/main.c on OpenBSD, added missing netinet/in.h header file.
  ↳ No PR: [1256250](https://github.com/openssl/openssl/commit/1256250b5c08f618131d7ef11454a5bc6330163b)
- Fixed BIO_s_connect incorrectly setting keepalive on datagram sockets, now only enabling keepalives on streaming sockets.
  ↳ No PR: [bf2944a](https://github.com/openssl/openssl/commit/bf2944a6a71a29e664083ad7bfc3d2a1664c2586)
- Fixed bug in SM4-XTS's aarch64 assembly implementation.
  ↳ No PR: [2a25617](https://github.com/openssl/openssl/commit/2a2561709ab316584d8b0a6220e244094fe507f5)
- Fixed potential null pointer dereference issue in KDF test control functions.
  ↳ No PR: [6ca1d3e](https://github.com/openssl/openssl/commit/6ca1d3ee81b61bc973e4e1079ec68ac73331c159)
- Fixed the issue of inconsistent script numbers in multi-stream testing.
  ↳ No PR: [37228de](https://github.com/openssl/openssl/commit/37228ded0faab6c10f7438f812ce611e0a41830b)
- Fixed the compilation problem of unit tests under MSVC, changing the script name and title from pointers to arrays.
  ↳ No PR: [1260d0f](https://github.com/openssl/openssl/commit/1260d0f5792b5253ecd8ca23eee848ab2c50c1ea)
- Avoid printing too long ASN1 data in fuzz testing to prevent false positive timeouts.
  ↳ No PR: [4a6f70c](https://github.com/openssl/openssl/commit/4a6f70c03182b421d326831532edca32bcdb3fb1)
- Fix intermittent CI test failure: add group ID range assertion in tls_prov_get_capabilities, and fix virtual group ID assignment.
  ↳ No PR: [a24f29b](https://github.com/openssl/openssl/commit/a24f29bbb4e7c2c73b0b3b2193b81c9b444b0864)
- Fixed ANSI C compatibility issues in QUIC QLOG tests: changed overly long string literals to arrays, and fixed commas in enumeration definitions.
  ↳ No PR: [8d8866a](https://github.com/openssl/openssl/commit/8d8866aff39399dbee2d49c59aca466794c53ba7)
- Fixed openssl list command: when a provider cannot return parameters, treat it as a warning instead of an error, and continue to list other providers.
  ↳ No PR: [7ebaab7](https://github.com/openssl/openssl/commit/7ebaab7689f66ede1f960c42be3446922e3f5e21)
- Fixed a memory leak caused by OPENSSL_DIR_end not being called under the wrong path in apps/rehash.c.
  ↳ No PR: [01709fc](https://github.com/openssl/openssl/commit/01709fcb8b609cfc47e277d20492c333bafb113e)
- Fix the memory leak caused by conn not being released when SSL_set_alpn_protos fails in the new_conn function of the documentation example code.
  ↳ No PR: [1635d7a](https://github.com/openssl/openssl/commit/1635d7a078b21d8fc3078f6115a4d8f7e18ad1ab)
- Fixed the issue of inconsistent use of size_t and uint64_t types in QUIC QLOG.
  ↳ No PR: [2c63ec6](https://github.com/openssl/openssl/commit/2c63ec6fd3ade0c37a68ed2d2054477d86155922)
- Type-safe CRYPTO_MUTEX and CRYPTO_CONDVAR, and fix bugs caused by type mismatch in QUIC code.
  ↳ No PR: [62cb7c8](https://github.com/openssl/openssl/commit/62cb7c810e882895a71ba2cc479f482df0aa8e32)
- Fix clang compiler warning in QUIC SRTM: Initializing uninitialized local variables.
  ↳ No PR: [044fd04](https://github.com/openssl/openssl/commit/044fd04cb4005dbb08c556dcf1e87fda9b7a45ba)
- Organize the Makefile in the demo directory: fix compilation warnings, unify the output format and add error handling.
  ↳ No PR: [86db958](https://github.com/openssl/openssl/commit/86db958835d1f8ba9ce49a9f93b5309c3d13b91c)
- Fix ANSI compatibility issue in QUIC RCIDM module: remove trailing commas in enum definitions.
  ↳ No PR: [3ba9345](https://github.com/openssl/openssl/commit/3ba9345eb9ccae3bf7204f3f6418c61e9aebe31d)
- Fix condition judgment errors in JSON testing, and simplify JSON operations in the QLOG cleaning process.
  ↳ No PR: [1cc04b7](https://github.com/openssl/openssl/commit/1cc04b777dd7febf767e4dcbd4ace014d5521f47)
- Added XOF state check in universal SHA3 absorb implementation to ensure absorb operations are only performed in the initial or absorbed state.
  ↳ No PR: [1337b50](https://github.com/openssl/openssl/commit/1337b50936ed190a98af1ee6601d857b42a3d296)

### Refactoring optimization
- Refactored BLAKE2s implementation using macros, eliminating code duplication and supporting variable output length.
  ↳ No PR: [6d1e730](https://github.com/openssl/openssl/commit/6d1e730a1ea2c64bdffa88c6b3bee4c3f5bed602)
- Unified the calculation logic of ping timeout and idle timeout in QUIC channel, and restructured the implementation of local connection ID replacement.
  ↳ No PR: [758e9b5](https://github.com/openssl/openssl/commit/758e9b537ac59680b4eaed77a81f5399cb38c0ae)
- Added sub-channel list for QUIC_PORT, which is maintained when the channel is created and destroyed.
  ↳ No PR: [ce503f5](https://github.com/openssl/openssl/commit/ce503f5c85bff7521eefa023d6f865fd2074de37)
- Removed the deprecated stateless reset handling code in QUIC DEMUX and added datagram ID allocation when receiving datagrams. Also removed the old DEMUX-QRX routing code in QUIC QRX.
  ↳ No PR: [6d76d13](https://github.com/openssl/openssl/commit/6d76d13e543bb9f5644737ca479baed1624abe43), [ef95d8d](https://github.com/openssl/openssl/commit/ef95d8ddcaaa95ef4f2a072767fffcc1ca0f095e)
- Saved a reference to LCIDM when initializing the QUIC channel, added a reference to the QUIC port for the channel, and adjusted the acquisition method of the demultiplexer.
  ↳ No PR: [cce6fcc](https://github.com/openssl/openssl/commit/cce6fccd4ebf21e6107590c4700808eb72d198e5), [12ab8af](https://github.com/openssl/openssl/commit/12ab8afcebf7eba3c79cfc8bdaf24c998b379e2a), [f98bc5c](https://github.com/openssl/openssl/commit/f98bc5c95b7389015e11cd2102e2a6a09b3c9e36)
- Switched QUIC SRTM's blinding mechanism from MAC-based to AES-128-ECB, removed assertions that were no longer needed, and replaced safe memory comparisons in comparison functions with normal memory comparisons.
  ↳ No PR: [4e3d481](https://github.com/openssl/openssl/commit/4e3d4819802a572bea6788c8a0eef79933213a5c)
- Change the return type and local variables of ssl_cert_info related search and disable checking functions to const, making them read-only accessible.
  ↳ No PR: [5fb4433](https://github.com/openssl/openssl/commit/5fb443360603069396e081d36330fcd44d3945a0)
- Unified the server version selection logic of TLS and DTLS, removed the special processing of DTLS, and instead called the version negotiation function uniformly.
  ↳ No PR: [f4ad7c2](https://github.com/openssl/openssl/commit/f4ad7c2f73c6a1b0d4f28caced249fc88a938c5e), [78ef740](https://github.com/openssl/openssl/commit/78ef7409995b053f21ee4333facae94cce57ff3e)
- Simplified the SSL protocol version comparison logic, introduced a unified ssl_version_cmp function to replace the original static version_cmp, and used it uniformly in multiple functions.
  ↳ No PR: [6fd3794](https://github.com/openssl/openssl/commit/6fd37948144b9f0702260fc4aae6bff325e34132)
- Reconstructed QLOG instance management, changing the direct storage of QLOG pointers to dynamic acquisition through callback functions, and delaying instantiation until the first event is triggered.
  ↳ No PR: [410270d](https://github.com/openssl/openssl/commit/410270d1ac7f9a089d63d68be2e7c714045191fc), [6f09c80](https://github.com/openssl/openssl/commit/6f09c8071af8328b1dac1914bea4533cac182204), [e825599](https://github.com/openssl/openssl/commit/e825599213119b8ff56b4bb4df40b898dd68572e)
- Improved diagnostic information for expected sender name in CMP message inspection, making log output clearer.
  ↳ No PR: [f21409f](https://github.com/openssl/openssl/commit/f21409fadf0e50130023656acc3ab72f8f72ff64)
- Removed unnecessary trace output in check_msg_all_certs function when 3GPP mode is not enabled.
  ↳ No PR: [2464d8d](https://github.com/openssl/openssl/commit/2464d8dc1907b832222ec19d1d0500d9306c47d5)
- Renamed likely and unlikely macros to ossl_likely and ossl_unlikely to comply with coding specifications.
  ↳ No PR: [f1e0c94](https://github.com/openssl/openssl/commit/f1e0c94545a6eb02914a31c3d94bf96387ebc68d)
- Removed outdated QUIC SRT structure and list macro definitions.
  ↳ No PR: [3e4b8e8](https://github.com/openssl/openssl/commit/3e4b8e8c53508b8c6d7355ef18d966a995197cb7)
- Declare several internal data structures (bitmask table, nid_to_group array, SCSV cipher suite) as read-only constants.
  ↳ No PR: [a87b6d1](https://github.com/openssl/openssl/commit/a87b6d1377e7b18ec17edf0f34d5cd797ce947c5), [3392a56](https://github.com/openssl/openssl/commit/3392a5690bf304ad7938e69a80f39f349e61ab7c), [c30aee7](https://github.com/openssl/openssl/commit/c30aee71f9b93dddd33dc81b70b6ad4cb76e5dfd)
- Removed unused variable assignments, conditional branch code and function definitions (including ssl_bad_method and its macros).
  ↳ No PR: [afd8e29](https://github.com/openssl/openssl/commit/afd8e29c360376420ea676581aa5d50b6027d069), [ffeae4c](https://github.com/openssl/openssl/commit/ffeae4c4e7d779746c661e7fe17a0a21cc36c974), [7f7a910](https://github.com/openssl/openssl/commit/7f7a910b6e8d5e564f5ce174236e44de0725f801)
- Replaced multiple strstr() calls for matching single characters with the more precise strchr(), improving code accuracy and readability.
  ↳ No PR: [0f644b9](https://github.com/openssl/openssl/commit/0f644b96d209443b4566f7e86e3be2568292e75b)
- Reconstructed the setup_srv_ctx function in apps/cmp.c, corrected coding style issues, and improved the convenience of source code level debugging.
  ↳ No PR: [a143e4e](https://github.com/openssl/openssl/commit/a143e4e3c9aa51f16b0d4c7857cf4b06be64f121)
- Extract BLAKE2B provider definitions into macros, eliminating duplicate function implementations.
  ↳ No PR: [8349c02](https://github.com/openssl/openssl/commit/8349c02e86310d0263b97a26fefd24ab83571ae8)
- Split the list macro into declaration and implementation parts, allowing separation of declaration and function definition.
  ↳ No PR: [3f0be2c](https://github.com/openssl/openssl/commit/3f0be2c206498b3fa3dd0a4dd94e31eb43d04c4a)
- Added iterator macros to internal linked lists, supporting forward, reverse and safe deletion traversal.
  ↳ No PR: [70a7e54](https://github.com/openssl/openssl/commit/70a7e543a1bf9ff6d404b6897bc53fd2e5349b9c)
- Centralize the forward declaration of QUIC structures into the new header file quic_predef.h, and fix the duplicate definition problem.
  ↳ No PR: [e801455](https://github.com/openssl/openssl/commit/e801455446cb9144224b424f930ee81977eeab22), [ff3a26b](https://github.com/openssl/openssl/commit/ff3a26b24f0bf7f0b24e97453ea138dd167adcb5)
- Removed redundant functions that are no longer called after the record layer is reconstructed.
  ↳ No PR: [e46a6b1](https://github.com/openssl/openssl/commit/e46a6b1a5de0759023c5c9c2143ead4621f20d20)
- Removed the unused wpend_ret field and related code in the record layer.
  ↳ No PR: [0a40b23](https://github.com/openssl/openssl/commit/0a40b23cb86d41b27aea67c648e35cd420d39674)
- Move the increment operation of DTLS epoch to the change cipher state function.
  ↳ No PR: [4897bd2](https://github.com/openssl/openssl/commit/4897bd202245a6fc068692ecc75dca52ce9ff5fa)
- Removed unused Xpout and Xqout parameters and related logic in the ossl_rsa_fips186_4_gen_prob_primes function.
  ↳ No PR: [d8184e9](https://github.com/openssl/openssl/commit/d8184e982c65eee674d045da827c253c30fb59ff)
- Adjust the QUIC release order to release the TLS object first and then the channel to avoid problems caused by calling back QUIC during TLS cleanup.
  ↳ No PR: [fa4b115](https://github.com/openssl/openssl/commit/fa4b1151c829b8be1d83cb49c9809d3a4f59fb03), [f7f2b66](https://github.com/openssl/openssl/commit/f7f2b665cf91650deb28beb1145ea3eca7df67aa)
- Rename the sink setting function of the JSON encoder to ossl_json_set0_sink, and simplify the return value of the initialization function.
  ↳ No PR: [39b9345](https://github.com/openssl/openssl/commit/39b9345234aacfcf5dbdf4ec5afc14bf0c6d9d2e)
- Reconstruct the QUIC QTX writing process, extract the package mutation and qlog logging logic into independent functions, so that the injected frames can also be recorded by qlog.
  ↳ No PR: [2acc1eb](https://github.com/openssl/openssl/commit/2acc1ebbd96afb5377af10cad6572617c906b06b)
- Change some global variable structures in libssl to constants to improve code safety and correctness.
  ↳ No PR: [89dd87e](https://github.com/openssl/openssl/commit/89dd87e1e86ee23a1582ec558abd2eb27d68505d)
- Split the inbound flow queue in QUIC flow mapping into bidirectional and unidirectional tracking, and add an interface to obtain the total queue length.
  ↳ No PR: [a5d16ac](https://github.com/openssl/openssl/commit/a5d16ac371245bd87e9ec264763a16db7015d59b)
- Moved the NULL pointer check in SSL_get_value_uint to the QUIC-specific implementation function ossl_quic_get_value_uint.
  ↳ No PR: [99a5cfc](https://github.com/openssl/openssl/commit/99a5cfc13a0a8b1ebf51d0193ac78f64a48c87e1)
- Remove unused parameters in tls_int_new_record_layer and its calling functions.
  ↳ No PR: [cfabddf](https://github.com/openssl/openssl/commit/cfabddfb9f6f54b3f3b8e90ccb918967390a7fb2)
- Remove the no longer used record_queue structure, and change related queue operations directly to use the pqueue_st pointer.
  ↳ No PR: [715a74a](https://github.com/openssl/openssl/commit/715a74a6ad1b24e3a07cc483379573d3d0e3b20c)
- Removed duplicate condition checks in PKCS7_verify function.
  ↳ No PR: [8211ca4](https://github.com/openssl/openssl/commit/8211ca45e41efd4224705848f1de3c2d6aa7b07a)

### Test related
- Added additional test vectors for AES-128-CBC, AES-XTS and AES-ECB modes to enhance test coverage.
  ↳ No PR: [7914a0d](https://github.com/openssl/openssl/commit/7914a0de113b1861a0ce5ff1bcbc602a42abe8da), [fbe6348](https://github.com/openssl/openssl/commit/fbe634836383cff2d01128530f1aa86a1a280a33), [f03ce9e](https://github.com/openssl/openssl/commit/f03ce9e0194ab1b5422bc582eb81b8babaef49c5)
- Fixed race conditions in QUIC multi-stream testing, frame injection logic and random failures on Windows, and enhanced QLOG diagnostics.
  ↳ No PR: [b7c7997](https://github.com/openssl/openssl/commit/b7c7997375e1bd0dcbbddb1b800c1eed3410056f), [a6eb287](https://github.com/openssl/openssl/commit/a6eb287a667ccbc241c59b23b151672e450bda4b), [660718e](https://github.com/openssl/openssl/commit/660718ee5bafce9c5ca7604801a59f53df28f202), [22b482a](https://github.com/openssl/openssl/commit/22b482a8b6f0c0e422c9b926c26d906ac6909106)
- Enhanced QUIC client fuzzer to support post-handshake write and stream operations.
  ↳ No PR: [d3dcf88](https://github.com/openssl/openssl/commit/d3dcf88cc5dead2ecaf29714f40cba586d6188ca), [3fa274c](https://github.com/openssl/openssl/commit/3fa274ca815335e198cf36a1062c59a9f4c00510)
- Added a new session buffer overflow test case to verify the behavior when the buffer overflows.
  ↳ No PR: [29ef379](https://github.com/openssl/openssl/commit/29ef379adef960df5317eb93f9aec2302e4c7208)
- Added test files for JSON encoder and fixed logic errors in test helper functions.
  ↳ No PR: [1b39eab](https://github.com/openssl/openssl/commit/1b39eab7aaa955c3a6cd24c864e714c32725861c)
- Added provider profile support for configuration testing and a new test option to verify provider activation status.
  ↳ No PR: [e389f56](https://github.com/openssl/openssl/commit/e389f56faeecad6b80f06695c0b753b355b0a5fc)
- Fixed potential NULL pointer dereference issue in ssl_old_test.c.
  ↳ No PR: [42772df](https://github.com/openssl/openssl/commit/42772df59bef7422060fbe70551c72d804bc669a)
- Fixed the problem of possible overflow of params array in digest_test_run.
  ↳ No PR: [497a781](https://github.com/openssl/openssl/commit/497a7810bcee48781aa12d4db870f6a565bd0592)
- Allow the deleted extension content to be output to the buffer when a TLS extension is removed, and related functions have been updated.
  ↳ No PR: [1d8a399](https://github.com/openssl/openssl/commit/1d8a399f7bdbe9798cea9dc28bb6ee321f0f24f7)
- Added a new bandwidth limit test, and expanded the transmission parameter test to cover missing, deformed, repeated and other scenarios.
  ↳ No PR: [8cb4a47](https://github.com/openssl/openssl/commit/8cb4a47dbb7fb5249c4ab9511d8f2e2f1cc4b445)
- Added test cases for uniform random number generator.
  ↳ No PR: [d05e0e4](https://github.com/openssl/openssl/commit/d05e0e40d712b9246c6e9db5b579fcce69dafa98)
- Added negative test for key length changes.
  ↳ No PR: [1aa0864](https://github.com/openssl/openssl/commit/1aa08644ecd4005c0f55276b2e8dabd8a2a758f0)
- Removed dead code in test functions, simplifying WPACKET cleanup process.
  ↳ No PR: [3150dbe](https://github.com/openssl/openssl/commit/3150dbe7cb71de1ee7040c6fdeb254c88e775b7c)
- Added test cases for the QUIC SRTM module to verify the generation and release of stateless reset tokens.
  ↳ No PR: [90a1115](https://github.com/openssl/openssl/commit/90a111579984c84255f3b3698736f876516aa5ed)
- Added a thread-safe lock to the fake_now variable in the test library to prevent multi-threaded data competition.
  ↳ No PR: [11179b3](https://github.com/openssl/openssl/commit/11179b3e8de8cd566af1215093db793ac3ed0f91)
- Added fuzz and unit tests for QUIC local connection ID manager.
  ↳ No PR: [3d7f83e](https://github.com/openssl/openssl/commit/3d7f83ebdca1d66f7ddb2ad1d23866d3a6c4e3cf), [9855408](https://github.com/openssl/openssl/commit/985540839abab03eed0eb0232ef00e34bddd70d9)
- Added unit tests for specific issues.
  ↳ No PR: [0efcf13](https://github.com/openssl/openssl/commit/0efcf1384fd320a6235e90d7b078ad89ea504d16)
- Added fuzz and unit tests for QUIC remote connection ID manager.
  ↳ No PR: [d0bac94](https://github.com/openssl/openssl/commit/d0bac943c99fa73ce0c6c879d269fc1cf42c16ad), [433ef94](https://github.com/openssl/openssl/commit/433ef94187b096a4e108845bb64007371a2341a0)
- Added OP_POP_ERR operation to QUIC multi-stream tests and changed error checking to non-destructive.
  ↳ No PR: [499aacd](https://github.com/openssl/openssl/commit/499aacdc82c700bc381e21d16703607e323bbb9e), [f12ea1f](https://github.com/openssl/openssl/commit/f12ea1f1e0f11686be8abad608b56a8357c688bb)
- Removed dependency on old DEMUX-QRX routing in QUIC recording tests and TXP tests, using default handler instead.
  ↳ No PR: [56f9828](https://github.com/openssl/openssl/commit/56f98283827ec57c794e849d0bdf3dd90f740805), [5d49f9e](https://github.com/openssl/openssl/commit/5d49f9ef9a4e45c87d00d40b2ef29649f006f088)
- Imported recurring issues from specific issues as HKDF test cases, added BLAKE2S-256 test data.
  ↳ No PR: [56aa3e8](https://github.com/openssl/openssl/commit/56aa3e8d1a286e11e56d9a9f6373c33a87a69ff4)
- Avoided potential double-free issue in cmp_ctx tests.
  ↳ No PR: [c8ca810](https://github.com/openssl/openssl/commit/c8ca810da9c47d8cb6988fd14e1cb4e20b0877e8)
- Added missing TLSA record combination test case in danetest.in.
  ↳ No PR: [c8fe4b5](https://github.com/openssl/openssl/commit/c8fe4b5948486e792016208f7c8ccea9c380f354)
- Added ENGINE lazy loading test for TLS.
  ↳ No PR: [7765d25](https://github.com/openssl/openssl/commit/7765d25ffe4f2a60b2082d469dec3b40f3418024)
- Added a new minimal test provider, and statically linked the legacy provider in evp_extra_test to avoid crashes.
  ↳ No PR: [31c2c12](https://github.com/openssl/openssl/commit/31c2c12f2dada75c334f6a9aa60c8424cf4fd040), [f529a2e](https://github.com/openssl/openssl/commit/f529a2eb75374946b60ed686ca6f90fdf244e787)
- Add test case for X509_load_cert_file().
  ↳ No PR: [d6961af](https://github.com/openssl/openssl/commit/d6961af1acbdf29b684f3307578bd03890a26a9c)
- Add test case for OSSL_HTTP_parse_url with empty port value.
  ↳ No PR: [a36d10d](https://github.com/openssl/openssl/commit/a36d10dfb7e77614c8d3da602ff3800a2e9f4989)
- Modify the test case to verify that EVP_CIPHER_CTX_get_iv_length returns the expected error code when incorrect input is made.
  ↳ No PR: [72062fc](https://github.com/openssl/openssl/commit/72062fca2870af4ef789cd5fc3442b3569f52c9b)
- Fixed a crash in evp_test caused by calling EVP_MAC_CTX_get_mac_size on an older version of the FIPS provider.
  ↳ No PR: [e454233](https://github.com/openssl/openssl/commit/e4542332fa36eab6d6bbf33815bde433ade3b547)
- Added test for long context export key material, only executed when FIPS provider version is not lower than 3.3.0.
  ↳ No PR: [5df160f](https://github.com/openssl/openssl/commit/5df160f116fbe49eff5c938cf184f84bf4cc3952)
- Added a new test case to verify that unknown signature algorithms and groups marked with question marks are ignored.
  ↳ No PR: [2b4cea1](https://github.com/openssl/openssl/commit/2b4cea1edfc0db486b3824ffbf3e520752ce05d1)
- Add OCSP test cases for s_server's -cert_chain option.
  ↳ No PR: [cf84224](https://github.com/openssl/openssl/commit/cf8422480acf10146d0bc6bec40e3efeb12a2d5a)
- Set the maximum protocol version for DTLS renegotiation testing to DTLSv1.2.
  ↳ No PR: [59b5950](https://github.com/openssl/openssl/commit/59b59505893a51bd52541da738693e963bef171f)
- Add tests for writing long application data records for KTLS to verify the functionality of writing and reading extremely long records.
  ↳ No PR: [563f4be](https://github.com/openssl/openssl/commit/563f4be8976ea776ec4fb90d084e2ce80c92f0d1)
- Fixed a crash in ssl_old_test caused by bypassing the test framework's bio_err management.
  ↳ No PR: [2995be5](https://github.com/openssl/openssl/commit/2995be50e8c2f2ef907866e35347be1e200558a2)
- Added test cases for reusing password context to verify correctness of hardware specific context reset.
  ↳ No PR: [3cb1b51](https://github.com/openssl/openssl/commit/3cb1b51dddf4deaf5e3886b827f3245d81670bc7)
- Fixed issue with test cases running on duplicate keys.
  ↳ No PR: [387b93e](https://github.com/openssl/openssl/commit/387b93e14907cd8203d6f2c9d78e49df01cb6e1f)
- Fix the problem that the array variable key is not initialized in the test_siphash_basic function.
  ↳ No PR: [a0826b1](https://github.com/openssl/openssl/commit/a0826b184eed2dccc56cdf80e3e0bc061cc89ddc)
- Expand the test of SSL connection reset/clearance, cover the use of SSL_set_accept_state and SSL_set_connect_state, and add more resume tests.
  ↳ No PR: [5de8c49](https://github.com/openssl/openssl/commit/5de8c49d6c019ad93149871989b755b5cc7b821c)
- Added new test functions in the QUIC multi-stream test to verify the number of available streams API and write buffer status API.
  ↳ No PR: [7048339](https://github.com/openssl/openssl/commit/7048339158a9ccfbbbeaa4d88baf74f06d41392e)
- Enhance the random platform adaptability of QUIC multi-stream testing, and adjust the test script operation to improve stability.
  ↳ No PR: [9b35ce2](https://github.com/openssl/openssl/commit/9b35ce2ba0aaa005199b7d84edc7ddeac8478475)
- Added unit test for QUIC QLOG function to verify log output format.
  ↳ No PR: [2413250](https://github.com/openssl/openssl/commit/24132503b3921ad6844bd64a9303f658f583f30c)
- Enhance the robustness of the poll test in QUIC multi-stream testing, correct the result count type and add error mark management, and add synchronization operations.
  ↳ No PR: [32a728d](https://github.com/openssl/openssl/commit/32a728d4e4722dbd8b419f449544cc68b87ea6f9)
- Added test cases and helper functions for the bandwidth limit filter.
  ↳ No PR: [b7de38e](https://github.com/openssl/openssl/commit/b7de38e84c13bbf56a9703fb600f925b86a9a28d)
- Extended multi_resume test to verify the behavior when the same session is resumed multiple times at the same time and one of them is marked as unrecoverable.
  ↳ No PR: [1bee528](https://github.com/openssl/openssl/commit/1bee5281e374af3bd7287ce9b2be1044ad888fb2)
- Add a check on the return value of xor_get_aid() in the xor_sig_setup_md function to avoid null pointer dereference.
  ↳ No PR: [bc930be](https://github.com/openssl/openssl/commit/bc930bed20d7462afecbb9d947286a335975c04a)
- Remove duplicate invalid value checking code in test_tls13ccs function.
  ↳ No PR: [3920283](https://github.com/openssl/openssl/commit/39202836d6272a2dc44de8797fb34146f0eea51b)
- Adjust the CI configuration for interop testing, switch the test repository to a specific tag and copy openssl.cnf to support TLS 1.3 testing.
  ↳ No PR: [f38d9b7](https://github.com/openssl/openssl/commit/f38d9b74c918ce06567585844404dd8d7459f7e7)
- Add a step to adjust ASLR in the CI workflow and set mmap_rnd_bits to 28 to fix the problem of random failures in asan/tsan/ubsan operations.
  ↳ No PR: [37cd49f](https://github.com/openssl/openssl/commit/37cd49f57f9ce4128381ca122b0ac8ca21395265)
- Fixed an issue where single quotes in Windows test documents caused tests to not be recognized correctly.
  ↳ No PR: [cf424d1](https://github.com/openssl/openssl/commit/cf424d1da05b3cd928c97596af08e260429b308c)

### Performance optimization
- Optimize RISC-V SHA-256 implementation, support zvknhb extension, move constant loading to independent subroutines and simplify the initialization process.
  ↳ No PR: [a166866](https://github.com/openssl/openssl/commit/a1668660a76e180af5fe1510a4c01c0c2854cdcf)
- On the RISC-V platform, reduce the vector length required for SM3 hardware acceleration from 256 bits to 128 bits, and update the corresponding extended check conditions.
  ↳ No PR: [1c25bc2](https://github.com/openssl/openssl/commit/1c25bc2e3f5e9db90a1d7bc4f0bae1b59e5f2c4c)
- Mark the ossl_assert macro as likely to prompt the compiler to optimize non-failure paths.
  ↳ No PR: [6874003](https://github.com/openssl/openssl/commit/6874003e96b64b665acc20f65a5bcb3e4d315ce4)
- Automatically optimize QUIC write buffer size, add maximum buffer limit and free space guarantee mechanism, and adjust write operation path to use new wrapper functions.
  ↳ No PR: [b119f8b](https://github.com/openssl/openssl/commit/b119f8b892ea1dc5ee75f01a4632e7bc2b67323b)
- Enable AES and SHA3 optimization on Apple Silicon M3: AES performance improves by 19-36%, SHA3 improves by 4-7% on buffers of 256 bytes and above.
  ↳ No PR: [7602bf8](https://github.com/openssl/openssl/commit/7602bf871564df86005f6c4c989f1d7cc2393878)
- Optimize the circular buffer logic in the BIO_hex_string function to avoid using modulo operations to improve performance.
  ↳ No PR: [d6e4056](https://github.com/openssl/openssl/commit/d6e4056805f54bb1a0ef41fa3a6a35b70c94edba)
- Move discovery of legacy algorithm types from each time EVP_PKEY_CTX is created to EVP_KEYMGMT build time to improve performance.
  ↳ No PR: [8aa3781](https://github.com/openssl/openssl/commit/8aa3781bfc7f21b9add1f7ad3f25c78670ec182a)
- Optimize the implementation of ec_field_size(): instead of creating and copying BIGNUM objects by directly calling EC_GROUP_get0_field, simplify the code and improve performance.
  ↳ No PR: [9170cc0](https://github.com/openssl/openssl/commit/9170cc0398222778065e098e396b8eb8cd0de1d3)
- Removed an unnecessary memcpy operation in the DTLS message reassembly function, and used pointers to directly reference buffer data instead.
  ↳ No PR: [f08be09](https://github.com/openssl/openssl/commit/f08be096517f9bdae8a9d1d837748237db4d13a9)
- Added performance test support for KMAC128 and KMAC256 algorithms.
  ↳ No PR: [55ca75d](https://github.com/openssl/openssl/commit/55ca75dd8fc4cbceb65f4ef40c921b0f5b8f7b90)
- Optimize the field order of QUIC channel structures to reduce memory filling.
  ↳ No PR: [827475f](https://github.com/openssl/openssl/commit/827475fc8b255f912a90295b3dac5864a0a7614a)

### Security related
- Added overflow checks to parse_number, parse_hex and parse_oct functions, and fixed a bug with hexadecimal character conversion in parse_hex.
  ↳ No PR: [986c48c](https://github.com/openssl/openssl/commit/986c48c4eb26861f25bc68ea252d8f2aad592735)
- Detect and prevent recursive references in configuration files from causing stack overflow crashes, and also fixed the issue where error messages were incorrectly cleared when configuration parsing failed.
  ↳ No PR: [682fd21](https://github.com/openssl/openssl/commit/682fd21afb5428b5716e62eaefb09a7419f9cfd7)
- Fixed a heap buffer overflow vulnerability in the ASN1 OID loader when handling invalid input starting with a comma, leading commas will now be correctly detected and processed.
  ↳ No PR: [a552c23](https://github.com/openssl/openssl/commit/a552c23c6502592c1b3c67d93dd7e5ffbe958aa4)
- Fixed the integer overflow problem in the ossl_asn1_time_from_tm function to prevent overflow from being triggered by constructing special time values.
  ↳ No PR: [5b2d8bc](https://github.com/openssl/openssl/commit/5b2d8bc28a8ff59689da98f31459819db09a9099), [017fd46](https://github.com/openssl/openssl/commit/017fd465a4f01323465823a3dcf318553365dfdd)
- Fixed an issue where the stack buffer in the final functions of blake2b and blake2s was not cleared, leading to potential key data leakage. When the output length is not a multiple of 8, the temporary stack variable is cleared immediately after copying the result.
  ↳ No PR: [8b9cf1b](https://github.com/openssl/openssl/commit/8b9cf1bc2c3085b6e9493a057209ffd0bddf48a6)
- Fixed a potential key leak issue caused by stack variables not being cleared in PBKDF1 derived functions.
  ↳ No PR: [5963aa8](https://github.com/openssl/openssl/commit/5963aa8c196d7c5a940a979299a07418527932af)
- Fixed the unsafe sprintf call in QUIC QLOG and used BIO_snprintf with length limit instead, improving security.
  ↳ No PR: [63aaa51](https://github.com/openssl/openssl/commit/63aaa51b151c86339c3b21655504adc6d4343d34), [6a11cd5](https://github.com/openssl/openssl/commit/6a11cd50d52694353d7bb11421490939d92df1b6)
- Added tests for session cache handling to verify that the cache size does not exceed expectations when creating sessions multiple times.
  ↳ No PR: [6e32300](https://github.com/openssl/openssl/commit/6e3230045ccf8a220e998018c7ffbab3f1fc92d0)
- Updated documentation for TLS record compression to note that the feature is turned off by default and is only available at security level 1 or lower.
  ↳ No PR: [2462e43](https://github.com/openssl/openssl/commit/2462e431ffe75027f253d8f1aab44ba09129c628)
- Removed references to CVE-2023-5678 from CHANGES.md and NEWS.md, and adjusted the order of related entries.
  ↳ No PR: [afb19f0](https://github.com/openssl/openssl/commit/afb19f07aecc84998eeea56c4d65f5e0499abb5a)

### Documentation
- Added -6 option to QUIC and TLS client example programs to support IPv6 connections.
  ↳ No PR: [5091aad](https://github.com/openssl/openssl/commit/5091aadc223315ce115ee12f62df2af173bf5efb)
- Added a separate README file for the guide examples, updated the related README, and corrected the link and description.
  ↳ No PR: [ada33e9](https://github.com/openssl/openssl/commit/ada33e98f53ab02dc4d6e8259c9e9edb6cd5c90c)
- Documented in CHANGES.md The BLAKE2s hash algorithm now supports BLAKE2b-like configurable output length.
  ↳ No PR: [7cf75e5](https://github.com/openssl/openssl/commit/7cf75e5caa71a54539d4559c3fb6b0a48b92243f)
- Documented in CHANGES.md that the BLAKE2b hash algorithm supports configuring the output length through the size parameter.
  ↳ No PR: [19641b4](https://github.com/openssl/openssl/commit/19641b48afb57b48c8d67b44d3ed7054ee2c6bab)
- Added link to OpenSSL 3.2 man page in README.
  ↳ No PR: [4f0172c](https://github.com/openssl/openssl/commit/4f0172c543dd0f5582d52185bfe2c132faee9c8e)
- Synchronized CHANGES.md and NEWS.md files, updated version number and release notes.
  ↳ No PR: [96ee2c3](https://github.com/openssl/openssl/commit/96ee2c38ad9b1c878a11bf629499867777c18055)
- Modify NEWS.md to a format closer to the release notes.
  ↳ No PR: [36eb3cf](https://github.com/openssl/openssl/commit/36eb3cfb092382d04cec2df0fec720952ab3a4ca)
- Added proposed editing convention documentation for NEWS.md.
  ↳ No PR: [036de8d](https://github.com/openssl/openssl/commit/036de8d4faceb0cef7b0730f0d0cb9ba9f85b497)
- Synchronized the CHANGES.md and NEWS.md files, and merged the change records of the 3.2 branch into the main branch.
  ↳ No PR: [5dc2b72](https://github.com/openssl/openssl/commit/5dc2b72df76cf21095bd6a34449feb8474d85368)
- Added RIO (Reactive I/O subsystem) terminology to the glossary of QUIC design documentation.
  ↳ No PR: [125c7c1](https://github.com/openssl/openssl/commit/125c7c11a31a1645ac4b8da9c9fc367b1d080294)
- Fixed syntax error in CONTRIBUTING.md, changed 'Guidelines how to' to 'Guidelines on how to', and added link to documentation policy.
  ↳ No PR: [ea15508](https://github.com/openssl/openssl/commit/ea15508b4ffa77d440e3f2c817998271bfeb3b9c), [1956f09](https://github.com/openssl/openssl/commit/1956f09e58e912ff3fd040beff25bf773bc7b60c)
- Updated the build and running instructions for the QUIC HTTP/3 example, including adding shared library path settings, recommended installation of dependency packages, and cleaning up the build script.
  ↳ No PR: [22fa160](https://github.com/openssl/openssl/commit/22fa1602da91af2194997e0576582bb4f0cdd7e0)
- Documented build configuration changes that disable the QUIC server tools when configuring the no-apps option.
  ↳ No PR: [f60559e](https://github.com/openssl/openssl/commit/f60559eb957b53d7fd5c8c9ab566fe353ea2d9f8)
- Added QUIC debugging and tracing guide document, introducing two debugging methods: QLOG and packet capture.
  ↳ No PR: [0f4f990](https://github.com/openssl/openssl/commit/0f4f9902cceacd9739c0eceae6f1926545ad8e42)
- Updated README.md and added instructions for DTLS and QUIC protocol support.
  ↳ No PR: [0181a1a](https://github.com/openssl/openssl/commit/0181a1a49c6a63a0b23eb15558336660f5833002)
- Updated README-QUIC.md, adjusted the content structure and clarified the examples of s_client and QUIC.
  ↳ No PR: [355fd1f](https://github.com/openssl/openssl/commit/355fd1f45b707d2b066d6dff555dd53928e55627)
- Updated demos/README.txt, reorganized the sample directory structure and added new chapter descriptions.
  ↳ No PR: [aefb529](https://github.com/openssl/openssl/commit/aefb529422dc029efecd5d9a192b9ffa600fc5db)
- Added reference to demos subfolder in README document.
  ↳ No PR: [899c910](https://github.com/openssl/openssl/commit/899c910e3480e80dc1e6740217de86af39ac606e)
- Added references to HTTP/3 and ALPN protocol identifiers in QUIC documentation.
  ↳ No PR: [f666599](https://github.com/openssl/openssl/commit/f666599f8dae9a892c28765cfbfe561fff52e213)
- Updated the Makefile and source code of the QUIC demo example, and fixed format and type issues.
  ↳ No PR: [d1338fc](https://github.com/openssl/openssl/commit/d1338fcf12672ef4a3d417f5dd03e342710ee5b3)
- Updated QUIC design glossary, adding LCID and RCID concepts.
  ↳ No PR: [1184157](https://github.com/openssl/openssl/commit/11841571ff04d3c67e58caf3ca0ca02ec5e3812a)
- Added change description entries in CHANGES.md and NEWS.md for CVE-2023-5678.
  ↳ No PR: [4d4657c](https://github.com/openssl/openssl/commit/4d4657cb6ba364dfa60681948b0a30c40bee31ca)
- Updated the contribution guide, added 'CLA: trivial' example at the bottom of the commit message, and fixed the force push command.
  ↳ No PR: [cad48c5](https://github.com/openssl/openssl/commit/cad48c5b0f7180c5fab8db70feb07e0846d80d67)
- Updated the CHANGES.md header description and added a reference to NEWS.md.
  ↳ No PR: [addbd74](https://github.com/openssl/openssl/commit/addbd743b5ceeca93dafd59600ba92b87f916e12)
- Added a new section listing known issues in NEWS-FORMAT.md.
  ↳ No PR: [4f41334](https://github.com/openssl/openssl/commit/4f41334b4aee2160c4f292164b7467532402c53b)
- Removed guidance from CONTRIBUTING.md requiring adding change records in NEWS.md.
  ↳ No PR: [870f26e](https://github.com/openssl/openssl/commit/870f26e66ad6c52af6ec6100fb9f5d5ce67c6586)
- Added description of -prefer_no_dhe_kex option to s_client and s_server command documentation.
  ↳ No PR: [55d894b](https://github.com/openssl/openssl/commit/55d894bbfbb992482d4fbeac3b03f3bb5b2b258b)
- Updated CONTRIBUTING.md, added a reference to the code format checking tool util/check-format.pl, and corrected text details.
  ↳ No PR: [260d972](https://github.com/openssl/openssl/commit/260d97229c467d17934ca3e2e0455b1b5c0994a6)
- Added documentation for LHASH's down_load related functions and removed it from the missing documentation list.
  ↳ No PR: [75caab2](https://github.com/openssl/openssl/commit/75caab2718aecc8eea78945083e9d3d671f2be53)
- Records of unknown TLS group and signature algorithm configuration entries marked with ? will be ignored, and an error will be returned if the result list is empty.
  ↳ No PR: [cd2cdb6](https://github.com/openssl/openssl/commit/cd2cdb6158086c4904d186c718c887cc693b906d)
- Add documentation comment for SSL_R_UNEXPECTED_EOF_WHILE_READING, explaining that this error code can be used for control flow decisions.
  ↳ No PR: [ead44e1](https://github.com/openssl/openssl/commit/ead44e19fa3ff7d189876081880f1adb3dfdf30b)
- Updated CHANGES.md and NEWS.md, adding change records for feature enhancements and security fixes for the upcoming new version.
  ↳ No PR: [0873e6f](https://github.com/openssl/openssl/commit/0873e6f61a4f2841a7a4cf6b4f331132946c04bc)
- Updated CHANGES.md and NEWS.md to reflect that spaces around equal signs have been removed in DN output.
  ↳ No PR: [d8d1910](https://github.com/openssl/openssl/commit/d8d19107618dd89c4584996b2bbed32b983d3890)
- Improved documentation for -cert_chain and -status_verbose options.
  ↳ No PR: [7ceb770](https://github.com/openssl/openssl/commit/7ceb770883d5bbb60868df46a699dff928f865aa)
- Improved documentation on standard IANA cipher suite names, explaining that either standard names or OpenSSL names can be used in cipher lists, and noting that support starts with OpenSSL 3.2.0.
  ↳ No PR: [2d70cc9](https://github.com/openssl/openssl/commit/2d70cc9cecf8b322d795985efecee06242b203b3)
- Updated documentation for the string_mask option in openssl req command to be consistent with actual behavior.
  ↳ No PR: [f670040](https://github.com/openssl/openssl/commit/f670040b8623cfd5163dfc80cffbaa6de0e3f718)
- Fix formatting issues in the examples section in openssl-mac documentation.
  ↳ No PR: [52a75f4](https://github.com/openssl/openssl/commit/52a75f4088f2b2c59721152d9ec6ecf4d17c7e43)
- Fixed an error in the description of default key values in the FIPS HMAC key documentation.
  ↳ No PR: [e10aa4b](https://github.com/openssl/openssl/commit/e10aa4bb83d21bfd2dc6923f4f34a5f2329029db)
- Updated version date information in the changelog and news documents for the OpenSSL 3.3 alpha release.
  ↳ [#23902](https://github.com/openssl/openssl/pull/23902): [9010cc0](https://github.com/openssl/openssl/commit/9010cc0eeec6c80cc04ce09985bdcc69f4b8317b), [0c33b1c](https://github.com/openssl/openssl/commit/0c33b1c65383eb833f4e59732b160f9b0e91d041)
- Added clarification in the documentation that the -keys option is only used to select private keys, and there is no corresponding option to select only public keys.
  ↳ No PR: [6f73b45](https://github.com/openssl/openssl/commit/6f73b452d0b7b2d017f29e84fa741ea9ffcd42a6)
- Updated CHANGES.md and NEWS.md to document new features and improvements since OpenSSL 3.2.
  ↳ No PR: [5a088e1](https://github.com/openssl/openssl/commit/5a088e10047bfac59e1c597a5a8eb1ad90bff4d2)

### Build/CI
- Upgraded actions/github-script in GitHub Actions from v6 to v7.
  ↳ No PR: [5f6b08e](https://github.com/openssl/openssl/commit/5f6b08e218974d4fbbd77ffedc2d94a08a194cc2)
- Allows running EVP tests on pull requests, and removes the restriction that some steps are limited to push events only.
  ↳ No PR: [0414f89](https://github.com/openssl/openssl/commit/0414f89d5c5187260cca63c2066580ba90c44426)
- Cleaned FIPS artifacts before downloading and unpacking ABIDIFF artifacts.
  ↳ No PR: [d177754](https://github.com/openssl/openssl/commit/d177754686cac5025ffb6e994523ad624d3c1fd7)
- Fixed Visual Studio 2008 compilation error, added missing header file reference.
  ↳ No PR: [c3e8d67](https://github.com/openssl/openssl/commit/c3e8d67885c0c4295cfd1df35a41bf1f3fa9dc37)
- Fixed the name of artifacts upload in parameterized jobs to be dynamically generated based on matrix variables.
  ↳ No PR: [708e4ca](https://github.com/openssl/openssl/commit/708e4caa5939797f33d04ba79475fc6382d3b58f)
- Added platform symbol checking script and integrated into CI workflow.
  ↳ No PR: [796e5f9](https://github.com/openssl/openssl/commit/796e5f96488643755a18570a4907da78ee46131a)
- Removed the step to install Perl in the Windows CI workflow, since Windows runner already has Perl pre-installed.
  ↳ No PR: [d030bac](https://github.com/openssl/openssl/commit/d030bac57c5e8b539836acc1320fc62a9a96f055)
- Added Clang 17 compiler support in CI configuration.
  ↳ No PR: [bdcaa80](https://github.com/openssl/openssl/commit/bdcaa80fd596ae1aae18d93c7784cc7ed8fa504a)
- Added CI workflow for interoperability testing with GnuTLS and NSS.
  ↳ No PR: [337eb99](https://github.com/openssl/openssl/commit/337eb99c8474ed380f3aa6fbd6b2a4ab5d39aa26), [83783dd](https://github.com/openssl/openssl/commit/83783dd16e767483020e5b2dc3b1c0ac26520917)
- Added freebsd-x86_64 and ubuntu-aarch64 self-hosted runners to CI workflow.
  ↳ No PR: [6b7a11d](https://github.com/openssl/openssl/commit/6b7a11d8aa7abe50e6ebdd09a238e0a0df8cd228)
- Add a test configuration using an alternative SSL3_ALIGN_PAYLOAD value to daily tests.
  ↳ No PR: [5ccd4de](https://github.com/openssl/openssl/commit/5ccd4dec6f732b4144e16cc6c9e73f07fb506279)
- Adjusted AFL_MAP_SIZE environment variable in AFL fuzz testing CI jobs to avoid crashes, and raised to 300000 to support future growth.
  ↳ No PR: [13ee569](https://github.com/openssl/openssl/commit/13ee569d415fe2a70482395c022613bb4a27eff7), [12f5f26](https://github.com/openssl/openssl/commit/12f5f26e1e71fe0375d82df70df338b8666ef38f)
- Upgraded actions/setup-python in GitHub Actions from v5.0.0 to v5.1.0.
  ↳ No PR: [c3e0ea5](https://github.com/openssl/openssl/commit/c3e0ea50a80d5fcf0ecb96db8afb15d8e94f9040)
- Added instructions to enable QUIC protocol QLOG output support in INSTALL.md.
  ↳ No PR: [000e72e](https://github.com/openssl/openssl/commit/000e72ecda60867c920e3c3f06747395d903bd99)

### Maintenance
- Adjusted the format of SSL_CONNECTION pointer declaration in ossl_ctrl_internal().
  ↳ No PR: [b419fcc](https://github.com/openssl/openssl/commit/b419fccad7e88ff3d7c9fd74b2990952dd09b57a)
- Add missing copyright notice to QUIC port local header files.
  ↳ No PR: [f61a37d](https://github.com/openssl/openssl/commit/f61a37d17bae26133765018b1370078d4de14cbe)
- Initialize the mgf1_md field in rsa_dupctx to a null pointer.
  ↳ No PR: [f95e3a0](https://github.com/openssl/openssl/commit/f95e3a09173b13dcfae668be6103e64c02222f08)
- Added packet type field to QUIC TXPIM structure for diagnostic purposes.
  ↳ No PR: [40c835d](https://github.com/openssl/openssl/commit/40c835dac7e68528bfdc9322041ac93ef274c37d)
- Check whether the provider's insertion into the stack operation is successful, and output an error message if it fails.
  ↳ No PR: [8286e63](https://github.com/openssl/openssl/commit/8286e63271c94fb815f007cb6ecd0fe20647253a)
- Set more explicit error reason strings for duplicate transport parameter extensions.
  ↳ No PR: [f94cacb](https://github.com/openssl/openssl/commit/f94cacb70b677462ecca79314a3d9714f8c0faba)
- Updated TLS and QUIC sample programs to support specifying hostname and port via command line parameters.
  ↳ No PR: [2ec4e73](https://github.com/openssl/openssl/commit/2ec4e73c0188425890329ae7f0372c66fb0c1234), [420037c](https://github.com/openssl/openssl/commit/420037c82c4b2bfea952cbe00730930844969438)
- Add BIO_reset error check in CMS decryption example, and output prompt information after successful decryption.
  ↳ No PR: [9257a89](https://github.com/openssl/openssl/commit/9257a89b6f25dfa5aeee7114baec8ea992fcf5e5)
- When initializing the QUIC channel, if the port is not set, an error will be returned.
  ↳ No PR: [496f0be](https://github.com/openssl/openssl/commit/496f0beb99aa378867e69cfd98374dcbab0cd153)
- Change the default HMAC algorithm from MD5 to SHA256, remove the logic of skipping HMAC, and directly exit with an error when the specified hash function cannot be found.
  ↳ No PR: [e580f06](https://github.com/openssl/openssl/commit/e580f06deceee8f4ca780b871c712bc6e5ec3a3f)
- IANA assigns numbers to the two hybrid post-quantum key exchange protocols for testing and adds corresponding entries in the tracking table.
  ↳ No PR: [e9241d1](https://github.com/openssl/openssl/commit/e9241d16b47f24e27966bee0f8664a6b88994164)
- Unify the naming of variables pointing to QUIC_LCID objects in QUIC LCIDM code, and correct syntax errors in comments.
  ↳ No PR: [e6cf72c](https://github.com/openssl/openssl/commit/e6cf72c525494d95f58e8c17db2c003eba8ffd87)
- Remove duplicate u64 type definition in aes_x86core.c.
  ↳ No PR: [84356a0](https://github.com/openssl/openssl/commit/84356a02fe248cfd490b6ee2fa269c09410a5afb)
- Add explicit type conversion for parameters in get_time wrapper function.
  ↳ No PR: [04c561c](https://github.com/openssl/openssl/commit/04c561ce4b51a00ddd24d2e5d66d2c12a82639c2)
- Removed unnecessary cast for cipher_ctx->blocksize.
  ↳ No PR: [6e15585](https://github.com/openssl/openssl/commit/6e155858d785297bd8b51f667bc440f4e7c17bfb)
- Update comments in QUIC engine related header files and source files, correct descriptions and add TODO comments.
  ↳ No PR: [fdd60da](https://github.com/openssl/openssl/commit/fdd60dacc436b68229139a1c1f95d0dbc8bee315)
- Removed the legacy abort code macro definition in QLOG.
  ↳ No PR: [5b8f7ae](https://github.com/openssl/openssl/commit/5b8f7ae3542b6de0edde958de66544cdf45af2f4)
- Fixed uninitialized variable warning, corrected literal type in test.
  ↳ No PR: [39a387f](https://github.com/openssl/openssl/commit/39a387f46c1b4f85af4a3a9cf98e50772d117485)
- Perform minor maintenance updates on the QLOG module, including adding header files, adjusting platform compatibility, optimizing character checking functions, and correcting comments and code formats.
  ↳ No PR: [ba8b093](https://github.com/openssl/openssl/commit/ba8b093be78a0822e0f55335b9c4fd31265b2f22)
- Add a check on the return value of the certificate store setting function in the ssl_load_stores function, and jump to error handling when it fails.
  ↳ No PR: [db51157](https://github.com/openssl/openssl/commit/db511578f7822ed6aa47760adfdc08ef84a17698)
- Reorganize CI tasks, move less useful tasks to run daily or when pushing, and keep tasks that are more likely to trigger failure and take a shorter time in the PR's CI.
  ↳ No PR: [456b32b](https://github.com/openssl/openssl/commit/456b32ba4f85000d168230b8cc5f58571699ed63)
- Configure cross-compilation, main CI and Windows CI workflows to support running on a self-hosted runner.
  ↳ No PR: [625287b](https://github.com/openssl/openssl/commit/625287bc80129deedab7484ee4c0ac112ae874a0), [834a2d7](https://github.com/openssl/openssl/commit/834a2d7088a042a4f8f95fa2b8327fd388556151), [ce42b72](https://github.com/openssl/openssl/commit/ce42b72cb1ca2ba8669bc28a70ed9dca28b7a551)
- Upgrade actions/upload-artifact and actions/download-artifact in CI workflow from v3 to v4.
  ↳ No PR: [1ee0560](https://github.com/openssl/openssl/commit/1ee0560f43a38d3a2de6c2cd2cacb0879c75cf46), [c4496b8](https://github.com/openssl/openssl/commit/c4496b8f5ec8c23c3d072efa8e5c0f443c64dc71)
- Updated CI workflow to use GITHUB_WORKSPACE environment variable instead of hardcoded paths.
  ↳ No PR: [638ad52](https://github.com/openssl/openssl/commit/638ad52ae53ece2e870984430493e454f75d048a)
- Upgraded actions/setup-python in CI workflow from v4.7.1 to v5.0.0.
  ↳ No PR: [51c8549](https://github.com/openssl/openssl/commit/51c85496dc227f277adbe0748d596e07d9a34bc2)
- Replaced deprecated Rust toolchain actions actions-rs/toolchain with dtolnay/rust-toolchain in CI.
  ↳ No PR: [cd5911a](https://github.com/openssl/openssl/commit/cd5911a6b300453eefb4b6d9d797c9d1cdefb956)
- Add and rename the CI test environment variable RUN_CI_TESTS to OSSL_RUN_CI_TESTS to enable CI testing and achieve namespace isolation.
  ↳ No PR: [1a74f32](https://github.com/openssl/openssl/commit/1a74f32de711f5bc16fa7858d7029e6c1b5abf4a), [d1fe573](https://github.com/openssl/openssl/commit/d1fe5738d393ace037c1f5f674125ad06a7e576d)
- Adjust the enabling configuration of the qlog feature in CI: enable it in Windows builds, and remove duplicate options to avoid duplication of tests.
  ↳ No PR: [2b5a5c8](https://github.com/openssl/openssl/commit/2b5a5c87df23ee5b0344197174bf1219b04d2ebe), [ace3afa](https://github.com/openssl/openssl/commit/ace3afa087bc52d9613fd0dcd2dae758d43bde2c)
- Introduced experimental qlog product upload support, and moved the upload logic to shell scripts to optimize processing.
  ↳ No PR: [74447f8](https://github.com/openssl/openssl/commit/74447f84f18efc5a51a1d4440dea95e807fcff13), [6c23c72](https://github.com/openssl/openssl/commit/6c23c726bb87b499f30a9ec9e91ea72433c83f21)
- Add warehouse condition judgment for self-hosted workflow, which will only run when the warehouse is openssl/openssl.
  ↳ No PR: [74fd682](https://github.com/openssl/openssl/commit/74fd6823884e27c18ec3fe7bd99b9bc02e6f31f3)
- Upgraded suisei-cn/actions-download-file action used in CI workflow from v1.4.0 to v1.6.0.
  ↳ No PR: [62ecad5](https://github.com/openssl/openssl/commit/62ecad5378067ab1f702ef2381c2f4a279d15250)

### Others
- Fixed comment errors in multiple source files, including misspellings of function names and inaccurate descriptions.
  ↳ No PR: [c61fda2](https://github.com/openssl/openssl/commit/c61fda2ff88a5dc8d71a6b848008d6f01bfd7fa2), [3ffc6c6](https://github.com/openssl/openssl/commit/3ffc6c644c3494b3d5237073cc22c35737f9698a), [766603a](https://github.com/openssl/openssl/commit/766603a9a5297c804e04a82e041097c404e0f24b), [963cf3a](https://github.com/openssl/openssl/commit/963cf3a49a0083e9e14972b7e37eed3cbbf965dd), [de61dba](https://github.com/openssl/openssl/commit/de61dba39059825bd9dfe9dad1532d6ef6c110d4)
- Fixed typos in several source files, including macro names and description strings.
  ↳ No PR: [164a541](https://github.com/openssl/openssl/commit/164a541b9384cf4f2bee84c2b9b9feede6d65cca), [d8fa4cf](https://github.com/openssl/openssl/commit/d8fa4cf76308924daaf2335c6c0ff2f7334a5b26), [45d16a4](https://github.com/openssl/openssl/commit/45d16a44eb64df3c7df918520b828be4d41b35cb)
- Fixed spelling errors and grammatical issues in the man manual.
  ↳ No PR: [aa3347b](https://github.com/openssl/openssl/commit/aa3347ba9d670a747b46974ce46f2ed9ecb38662), [7deb2b4](https://github.com/openssl/openssl/commit/7deb2b433a08706337d8520793702f78765ecf90)
- Updated demos/guide/README.md to add instructions for running the TLS and QUIC examples.
  ↳ No PR: [a2b8247](https://github.com/openssl/openssl/commit/a2b824730ef12cda4e018f5f7cde2ab52a4d255c), [cb8107b](https://github.com/openssl/openssl/commit/cb8107b632661d2ae538961424768f0ed074fcf6)
- Updated CHANGES.md and NEWS.md to record version releases and security fixes.
  ↳ No PR: [186b3f6](https://github.com/openssl/openssl/commit/186b3f6a016de8fcf8573be111e3d174ca20f1bc), [858c7bc](https://github.com/openssl/openssl/commit/858c7bc210a406cc7f891ac2aed78692d2e02937)
- Updated QUIC design documentation, corrected README wording and added glossary definitions.
  ↳ No PR: [bcc04ab](https://github.com/openssl/openssl/commit/bcc04ab287d59e4f680c1a5eb768c19c5f74bea5), [1468247](https://github.com/openssl/openssl/commit/1468247b7a3f8140a87325b30990e55870657193)
- Added internal header file design of JSON encoder for QLOG function.
  ↳ No PR: [8a123d4](https://github.com/openssl/openssl/commit/8a123d43428dfc4b9bccd1c883206d8e653b2ec8)
- Fixed syntax error in openssl-cmp.pod.in documentation.
  ↳ No PR: [cb03eef](https://github.com/openssl/openssl/commit/cb03eef1a612212148690ca4ea6260cbb451fdee)
- Fixed named anchor links in NOTES-WINDOWS.md.
  ↳ No PR: [cf6342b](https://github.com/openssl/openssl/commit/cf6342bc024868f5a55f2225f2e083415fb1329a)
- Added comment description in CI workflow configuration for interoperability testing.
  ↳ No PR: [b062a3c](https://github.com/openssl/openssl/commit/b062a3c552bf283319dede3437598f1747730053)
- Clarified documentation for QUIC QLOG filters, updated examples and clarified rules for sequential application of filter items.
  ↳ No PR: [613917e](https://github.com/openssl/openssl/commit/613917ea0c5074700990851cb98b07f38c5b82b7)
- Adjusted the description of QLOG support in CHANGES.md to maintain editorial consistency.
  ↳ No PR: [d8b405a](https://github.com/openssl/openssl/commit/d8b405a27c49a375da2962e4dd2387b42a9feed0)
- Corrected the spelling of QLOG in code comments, using lowercase qlog uniformly.
  ↳ No PR: [de60b12](https://github.com/openssl/openssl/commit/de60b122b2f1082d5346f3f51fb7641c47391d71)
- Fixed typo in JSON encoding comments.
  ↳ No PR: [ae300c0](https://github.com/openssl/openssl/commit/ae300c0d5e8f39329a44236c6e6bf364f42cd771)
- Corrected the comments and array names of the script numbers in the test file, and cleaned up excess blank lines.
  ↳ No PR: [2cd09e0](https://github.com/openssl/openssl/commit/2cd09e0075cbe2427825c0a7e7cffcb57e408032)
- Fixed a typo in CHANGES.md, corrected the parameter name OSSL_PKEY_PARAM_DERIVE_FROM_PQ to OSSL_PKEY_PARAM_RSA_DERIVE_FROM_PQ.
  ↳ No PR: [de18dc3](https://github.com/openssl/openssl/commit/de18dc3a635c3a82c365b3f2beeb491c78b01b11)
- Updated documentation comments in QUIC QLOG related header files to remove inaccurate statements.
  ↳ No PR: [1aeab15](https://github.com/openssl/openssl/commit/1aeab15f46c79792e1f6ac270ec46840f70f48cc)
- Fixed typos in several source files.
  ↳ No PR: [f7241ed](https://github.com/openssl/openssl/commit/f7241edda4d9fc76f0ee134e6a07a76c6414b70a)
- Fixed syntax issues in code comments.
  ↳ No PR: [39fe3e5](https://github.com/openssl/openssl/commit/39fe3e5de159ef193590be70fabc8c9560b53a1a)
- Fixed SSL_export_keying_material not working on QUIC connections documented in CHANGES.md.
  ↳ No PR: [d597b46](https://github.com/openssl/openssl/commit/d597b46f9bdb533761e36fcf1d96ce83f3f6f04d)
- Changed the license of crypto/hpke/hpke.c and include/openssl/hpke.h from OpenSSL License to Apache 2 License.
  ↳ No PR: [e5313f2](https://github.com/openssl/openssl/commit/e5313f20486f86be42059fce6b0d9e43a35e8655)
- Fixed wording error in INSTALL.md regarding no-atexit option.
  ↳ No PR: [9dc2269](https://github.com/openssl/openssl/commit/9dc2269829726a10806c4e9f951074b6529e2529)
- Removed FAQ.md file because the link to the FAQ page referenced in it no longer works.
  ↳ No PR: [8545398](https://github.com/openssl/openssl/commit/854539889d31ed2ea63280256fd7aab66e828ae5)
- Updated copyright year in several source files to 2024.
  ↳ [#23902](https://github.com/openssl/openssl/pull/23902): [0ce7d1f](https://github.com/openssl/openssl/commit/0ce7d1f355c1240653e320a3f6f8109c1f05f8c0) | [#23999](https://github.com/openssl/openssl/pull/23999): [3764f20](https://github.com/openssl/openssl/commit/3764f200f9d44622faa8ac1b15d2f3eb7c39e473) | [#24073](https://github.com/openssl/openssl/pull/24073): [73941e7](https://github.com/openssl/openssl/commit/73941e73041541abc2494667906d830a65a465b9)
- Fixed spelling and grammatical errors in openssl-ts.pod documentation.
  ↳ No PR: [178ab8d](https://github.com/openssl/openssl/commit/178ab8d9da0942ba50016f319f991060ce95861c)
- Updated version dates and status in CHANGES.md and NEWS.md for release builds.
  ↳ [#23999](https://github.com/openssl/openssl/pull/23999): [5bf7b79](https://github.com/openssl/openssl/commit/5bf7b7975f342032883ebf4cf2302870337c2fb3), [efb87dd](https://github.com/openssl/openssl/commit/efb87dd7936dd970d0477180f9e3ba174e960e6e) | [#24073](https://github.com/openssl/openssl/pull/24073): [4cb3112](https://github.com/openssl/openssl/commit/4cb31128b5790819dfeea2739fbde265f71a10a2)
