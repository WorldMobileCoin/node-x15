{
    "targets": [
        {
            "target_name": "x15",
            "sources": [
                "x15hash.cc",
                "x15.c",
                "x15module.c",
                "sha3/aes_helper.c",
                "sha3/blake.c",
                "sha3/bmw.c",
                "sha3/cubehash.c",
                "sha3/echo.c",
                "sha3/fugue.c",
                "sha3/groestl.c",
                "sha3/hamsi.c",
                "sha3/hamsi_helper.c",
                "sha3/jh.c",
                "sha3/keccak.c",
                "sha3/luffa.c",
                "sha3/shabal.c",
                "sha3/shavite.c",
                "sha3/simd.c",
                "sha3/skein.c",
                "sha3/whirlpool.c",
            ],
            "include_dirs": [
              "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],"conditions": [
                ["OS=='win'", {
                    "libraries": [
                        "C:/Python27/libs/python27.lib"
                    ],
                    "include_dirs": [
                       "C:/Python27/include"
                    ]
                }, {
                    "include_dirs": [
                       "/usr/include/python2.7"
                    ]
                }]
            ]
        }
    ]
}
