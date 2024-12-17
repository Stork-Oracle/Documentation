---
description: Listening to data from a Stork Aggregator via WebSocket.
icon: download
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Subscriber

## Base Endpoint

The standard endpoint for interacting with Stork via websocket is:

```url
wss://api.jp.stork-oracle.network
```

## Authentication

All websocket connection requests must include an `Authorization` header with the value set as `Basic <token>` . For example if your token is `gmork123`:

```bash
wscat -c 'wss://api.jp.stork-oracle.network/evm/subscribe' -H "Authorization: Basic gmork123"
```

## Endpoints

### /evm/subscribe

Subscribe to listen to EVM signed data. This is data is signed using the Stork EVM private key, and is compatible with **any chain stork supports** other than StarkEx.

#### **Example:**

```bash
wscat -c 'wss://api.jp.stork-oracle.network/evm/subscribe' -H "Authorization: Basic fakeToken123"
```

### /stark/subscribe

Subscribe to listen to Stark signed data. This is data is signed to be natively compatible with StarkEx.

#### Example:

```bash
wscat -c 'wss://api.jp.stork-oracle.network/stark/subscribe' -H "Authorization: Basic fakeToken123"
```

## Messages

### Subscribe Message

```json
{
   "type": "subscribe"
   "trace_id": string
   "data": string[]
}
```

#### **Description:**

Subscribe to receive the stream of signed updates for assets.

#### **Fields:**

* `"type"`: Type of the message. In this case `"subscribe"`
* `"data"`: An array of plain-text [assets ids](../../introduction/core-concepts.md#asset-ids).&#x20;

#### **Example:**

```json
{
  "type": "subscribe", 
  "data": [
    "BTCUSD", 
    "ETHUSD", 
    "BTCUSDMARK"
  ]
}  
```

### **Subscribe Response**

```json
{
    "type": "oracle_prices"
    "trace_id": string
    "data": stork_signed_data[]
}
```

#### **Description:**

A response containing the data for subscribed assets.

#### **Fields:**

* `"type"` : Type of the message. In this case `"subscribe"`
* `"trace_id"`: Trace id for debugging
* `"data"`: An array of stork\_signed\_data updates, its structure can be found in [Becoming a Subscriber](../../getting-started/becoming-a-subscriber.md#using-data-off-chain).

#### **Example:**

<details>

<summary>EVM Response</summary>

<pre class="language-json"><code class="lang-json"><strong>{
</strong>  "type": "oracle_prices",
  "trace_id": "b83cd210-d954-4851-9df8-c3561a8e764a",
  "data": {
    "BTCUSD": {
      "timestamp": 1734390439136872400,
      "asset_id": "BTCUSD",
      "signature_type": "evm",
      "trigger": "unspecified",
      "price": "105753153499499996000000",
      "stork_signed_price": {
        "public_key": "0x0a803F9b1CCe32e2773e0d2e98b37E0775cA5d44",
        "encoded_asset_id": "0x7404e3d104ea7841c3d9e6fd20adfe99b4ad586bc08d8f3bd3afef894cf184de",
        "price": "105753153499499996000000",
        "timestamped_signature": {
          "signature": {
            "r": "0x4b2fa6f575cb90e523af9638aae42ee1b6d62d61d8ca7bc4e8466c9c1e8543e6",
            "s": "0x584901b829ebe8210441d563e9bb2201c49963769702a03e4f72f72e380d3162",
            "v": "0x1c"
          },
          "timestamp": 1734390439161122000,
          "msg_hash": "0x207a6868e12c2cf210edd7cac9da34bd6e29a05cb2758abfc67dc8819998400c"
        },
        "publisher_merkle_root": "0x88b53be6a9df81c281153c157279be049ac7c26659cd44bc1222c13581be9656",
        "calculation_alg": {
          "type": "median",
          "version": "v1",
          "checksum": "9be7e9f9ed459417d96112a7467bd0b27575a2c7847195c68f805b70ce1795ba"
        }
      },
      "signed_prices": [
        {
          "publisher_key": "0xb91C675E0c0Ecfd4c16f97B110376C3C224061d8",
          "external_asset_id": "BTCUSD",
          "signature_type": "evm",
          "price": "105753153499499996000000",
          "timestamped_signature": {
            "signature": {
              "r": "0xa03f90bc38411d9d217058a3527b6178a9c777e741bc152eef98cd7d0584ccc4",
              "s": "0x5df3ba35f2cfdb7f0428c0efdfae6ea9977bf681908fe1021c3a8d4b8655e117",
              "v": "0x1b"
            },
            "timestamp": 1734390439136872400,
            "msg_hash": "0x76dd6821034b711949c88b1b780da7892df065aee26b40c04789666a89e1abfa"
          }
        },
        {
          "publisher_key": "0x51aa9e9C781F85a2C0636A835EB80114c4553098",
          "external_asset_id": "BTCUSD",
          "signature_type": "evm",
          "price": "105753153499499996000000",
          "timestamped_signature": {
            "signature": {
              "r": "0xb2c80fa3ef5319c33ff79ee889e0225905c17bb84e96f0813d04969ef7a08a25",
              "s": "0x2009c828ffd6785a7598bb0eac5c10b29bdbacfc240f3160e4411ee5133ef5bd",
              "v": "0x1c"
            },
            "timestamp": 1734390439091587000,
            "msg_hash": "0xd45c7ed8cd2aaaa588eb7b91e70ac41fd61e343523243c524f4769c7403e6b78"
          }
        },
        {
          "publisher_key": "0xa3C28D4e939cE2927D3B29b7bF53d3AeaAb09350",
          "external_asset_id": "BTCUSD",
          "signature_type": "evm",
          "price": "105748830591000005000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x67bd1a65b7eed016fba5ef0444eb9b29047018b3f875ba5a9cdbeaa43e1172ed",
              "s": "0x6708dd50d07e3a9ed9eda1b1ac274640c00bb1a55baf197d79770a42ecac736e",
              "v": "0x1b"
            },
            "timestamp": 1734390438743000000,
            "msg_hash": "0x05777a133448c88f745988e0e300c6f199260e8f60e16eba5f42f5366ae54d80"
          }
        },
        {
          "publisher_key": "0xF024A9AA110798e5CD0d698FBA6523113Eaa7FB2",
          "external_asset_id": "BTCUSD",
          "signature_type": "evm",
          "price": "105753153499499996000000",
          "timestamped_signature": {
            "signature": {
              "r": "0xf6977f9b912daaf9f675160a870000e1a905c90aac93950082f13a1618788ee4",
              "s": "0x59ac0878fc8316ed598a84b5425d1eb40aa5df7fb6384ce5c2dc179e63423bff",
              "v": "0x1b"
            },
            "timestamp": 1734390439091587000,
            "msg_hash": "0x0d9024136a7339801cb27c13e30e1ad0e4712446012846510eef4cea4b082aba"
          }
        }
      ]
    },
    "BTCUSDMARK": {
      "timestamp": 1734390439136874500,
      "asset_id": "BTCUSDMARK",
      "signature_type": "evm",
      "trigger": "unspecified",
      "price": "105742801326000015000000",
      "stork_signed_price": {
        "public_key": "0x0a803F9b1CCe32e2773e0d2e98b37E0775cA5d44",
        "encoded_asset_id": "0x6b5b1c26f98c489ea35e449ccba14d6153182646efc9d09e56b4302e41be548d",
        "price": "105742801326000015000000",
        "timestamped_signature": {
          "signature": {
            "r": "0x14821ceaf8188964687facf142b13a2ed1ada0067176746e6199236500ff4f44",
            "s": "0x57387011781b447be1818cf52f74b5f1fc55e3c014a0870b349c104e52b5e010",
            "v": "0x1c"
          },
          "timestamp": 1734390439164351700,
          "msg_hash": "0xe09a41f3cd8bfed6507a2c0cfe9aa542a450ecb297cd712392d3bb7c23a11571"
        },
        "publisher_merkle_root": "0x611104c9af0444461f49fd3b58f1a1e9ef3ca6c1c47abfa87cf4a8bd2cccb39d",
        "calculation_alg": {
          "type": "median",
          "version": "v1",
          "checksum": "9be7e9f9ed459417d96112a7467bd0b27575a2c7847195c68f805b70ce1795ba"
        }
      },
      "signed_prices": [
        {
          "publisher_key": "0xa3C28D4e939cE2927D3B29b7bF53d3AeaAb09350",
          "external_asset_id": "BTCUSDMARK",
          "signature_type": "evm",
          "price": "105722787702999994000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x9c999394eb2801985922eacdc3f22d74335f393d67936d426825758ab0312b7e",
              "s": "0x7f119dec7ca2c663b0d98d0c3ed43e4d9f11906eb557a196120c8b7122a0bd6c",
              "v": "0x1b"
            },
            "timestamp": 1734390438743000000,
            "msg_hash": "0xa0d2a518341beed15147340c6b46549c50cb93030d652392e61447466c0c84e4"
          }
        },
        {
          "publisher_key": "0x51aa9e9C781F85a2C0636A835EB80114c4553098",
          "external_asset_id": "BTCUSDMARK",
          "signature_type": "evm",
          "price": "105742801326000015000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x50415eab9570f915d926c84688f45412ba9f4b7031043f6f4cdac05dc849e914",
              "s": "0x036192d0ad8932836f8d7208d5d0688772a552bf53710c33b70ed50f5e3fbe57",
              "v": "0x1b"
            },
            "timestamp": 1734390439091594000,
            "msg_hash": "0x2e255da7afbe7aba7e3d9e0a2c3db1e0cec7ed95589a6d52c2da310659d8969f"
          }
        },
        {
          "publisher_key": "0xF024A9AA110798e5CD0d698FBA6523113Eaa7FB2",
          "external_asset_id": "BTCUSDMARK",
          "signature_type": "evm",
          "price": "105742801326000015000000",
          "timestamped_signature": {
            "signature": {
              "r": "0xa321f1a692df0ac77c60e77af7e5329f4d9121e94cd072d6cd280470c9159890",
              "s": "0x585ebb19dcdd87fb8ae7fd6c2be2f32e7e0da8a7d0d36be72fde8e626eaa5f95",
              "v": "0x1b"
            },
            "timestamp": 1734390439091594000,
            "msg_hash": "0xae28b7ae7a5724506e7ed5e27803300521be10154b9719b0a4e23f8e4a4486ca"
          }
        },
        {
          "publisher_key": "0xb91C675E0c0Ecfd4c16f97B110376C3C224061d8",
          "external_asset_id": "BTCUSDMARK",
          "signature_type": "evm",
          "price": "105742801326000015000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x5f5cf14ba3018204c94e061f1edaee83320e0d898a8e195d1ce470d863b3f937",
              "s": "0x5699b723cd9358375217085cc502da15371c500fdbe3389d91007837635fa35c",
              "v": "0x1c"
            },
            "timestamp": 1734390439136874500,
            "msg_hash": "0x4a80d94527189740799419b3846ac33dd560ee3804ad8b973de1f6b4440ffa73"
          }
        }
      ]
    },
    "ETHUSD": {
      "timestamp": 1734390439136875800,
      "asset_id": "ETHUSD",
      "signature_type": "evm",
      "trigger": "unspecified",
      "price": "4027870675250000000000",
      "stork_signed_price": {
        "public_key": "0x0a803F9b1CCe32e2773e0d2e98b37E0775cA5d44",
        "encoded_asset_id": "0x59102b37de83bdda9f38ac8254e596f0d9ac61d2035c07936675e87342817160",
        "price": "4027870675250000000000",
        "timestamped_signature": {
          "signature": {
            "r": "0xc5bc5f6b374e5941e07d90b0813229a9b1466c5a59d7703c0d7f2fcb8d4d798e",
            "s": "0x29f4fb3477062e6ab7d8997b0a0304160e887a4e21948fde49a27a4a696886eb",
            "v": "0x1b"
          },
          "timestamp": 1734390439163362600,
          "msg_hash": "0x9a34f99fc7d5739a3d0be92accafece840c82ca804ab875a684d8f54c112f14d"
        },
        "publisher_merkle_root": "0xa2f5ad766250f3375766b6c2a684a83d13c1cab6ebe7be16eb4808523551cae3",
        "calculation_alg": {
          "type": "median",
          "version": "v1",
          "checksum": "9be7e9f9ed459417d96112a7467bd0b27575a2c7847195c68f805b70ce1795ba"
        }
      },
      "signed_prices": [
        {
          "publisher_key": "0xF024A9AA110798e5CD0d698FBA6523113Eaa7FB2",
          "external_asset_id": "ETHUSD",
          "signature_type": "evm",
          "price": "4027870675250000000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x3bf00ef505251fe89615b8040c7771727569821eebca81f86a1d7a8bd100a58f",
              "s": "0x1abbf372f55e24b3375b5e55f0503cd2fd17e8e7bc05594fc4d94507884698ac",
              "v": "0x1b"
            },
            "timestamp": 1734390439091595500,
            "msg_hash": "0xa55e533e8ccdd548fad8f6033a3319b355a64bcdbf482680a89f3bb1da8f866b"
          }
        },
        {
          "publisher_key": "0xa3C28D4e939cE2927D3B29b7bF53d3AeaAb09350",
          "external_asset_id": "ETHUSD",
          "signature_type": "evm",
          "price": "4027554896999999000000",
          "timestamped_signature": {
            "signature": {
              "r": "0xfb7b8a57eb8ca0b65eb890e5a85b40c7d079a11b066196b0d7423f1107b4d6d4",
              "s": "0x33f16c274a77f6e795b23bc5183e0901010b8986bfaccb21e36d98d2df5343f2",
              "v": "0x1c"
            },
            "timestamp": 1734390438743000000,
            "msg_hash": "0xf9b21284cf80d7f031f1da35a4baafc20ba9a6d11be9563cb8ffb009b2fb591c"
          }
        },
        {
          "publisher_key": "0xb91C675E0c0Ecfd4c16f97B110376C3C224061d8",
          "external_asset_id": "ETHUSD",
          "signature_type": "evm",
          "price": "4027870675250000000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x77097de985dd2f45f7345589c3895e8d63bb6b75161d80d1b1c82eb618219cbf",
              "s": "0x5d1ea4313d1a43ced440724c3e1da707373db2b16c630c5834090fe53e85f5a5",
              "v": "0x1c"
            },
            "timestamp": 1734390439136875800,
            "msg_hash": "0x68e56181d07099b8e8e8d2ae09f3a4a1eb7b6b18d4507819080c2d7e5c7290bd"
          }
        },
        {
          "publisher_key": "0x51aa9e9C781F85a2C0636A835EB80114c4553098",
          "external_asset_id": "ETHUSD",
          "signature_type": "evm",
          "price": "4027870675250000000000",
          "timestamped_signature": {
            "signature": {
              "r": "0xef4f2fb85046c395d68b01d59e42df37c77825a4796844ad3b2787c55ca1b5ed",
              "s": "0x4d48ad4d80ec8d9c597039f43449039095372dd836c823690861c2337a5ae6a3",
              "v": "0x1c"
            },
            "timestamp": 1734390439091595500,
            "msg_hash": "0xe27a3e15a5d081df8a2e9697f7f6c3483f559dd7610c625fc3e5b0efc336c60e"
          }
        }
      ]
    }
  }
}
</code></pre>

</details>

<details>

<summary>Stark Response</summary>

```json
{
  "type": "oracle_prices",
  "trace_id": "1b90ac7f-da98-4c74-ab71-7c7a4aac5ea2",
  "data": {
    "BTCUSDMARK": {
      "timestamp": 1734390877237000000,
      "asset_id": "BTCUSDMARK",
      "signature_type": "stark",
      "trigger": "unspecified",
      "price": "105897536209874990000000",
      "signed_prices": [
        {
          "publisher_key": "0x1f191d23b8825dcc3dba839b6a7155ea07ad0b42af76394097786aca0d9975c",
          "external_asset_id": "0x4254435553444d41524b00000000000053746b6169",
          "signature_type": "stark",
          "price": "105897536209874990000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x227165075a3b85b346c210244c90166a291574639071a0338a261dd2db87d9b",
              "s": "0x387a3fa3612c55b342a05dc9e7aebfe3c630ac641ae44143c61253beba927bf"
            },
            "timestamp": 1734390877091601200,
            "msg_hash": "0x1ac738e06b388b97f7422134da036eab8c7768439146fc5151da46ffa995d28"
          }
        },
        {
          "publisher_key": "0xcc85afe4ca87f9628370c432c447e569a01dc96d160015c8039959db8521c4",
          "external_asset_id": "0x4254435553444d41524b00000000000053746f726b",
          "signature_type": "stark",
          "price": "105897536209874990000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x1cd69bad5dacf4686560a75db6344d74577509c0c8e15262a37b40787f48f24",
              "s": "0x228ae7421c03c3562140a7f51c0253ef4dbbc52c9f54da8d0ad59e921033367"
            },
            "timestamp": 1734390877091601200,
            "msg_hash": "0x48f4bc9eaeafeb2d781de784ee8ef3aa25ec797b168d235c24f996b5ee77277"
          }
        },
        {
          "publisher_key": "0x41dbe627aeab66504b837b3abd88ae2f58ba6d98ee7bbd7f226c4684d9e6225",
          "external_asset_id": "0x4254435553444d41524b0000000000005374437277",
          "signature_type": "stark",
          "price": "105897536209874990000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x75d144fe6cab2f7a43c7a225640ef25586038ce7d353f6b5410176af37495de",
              "s": "0x48754c536eac05423abe09bd080e063bd6508ad8daf7eecc220a55236bb2f49"
            },
            "timestamp": 1734390877136659200,
            "msg_hash": "0x5589d94799b72858c12f96c7f41b4f9668fa76c6718b5b67e83d2524546edd6"
          }
        },
        {
          "publisher_key": "0x6ee80350406f9e753797c3f0e1303a63ea2ae1f1adb86340e52722f41b31b64",
          "external_asset_id": "0x4254435553444d41524b0000000000006465787472",
          "signature_type": "stark",
          "price": "105876059122000006000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x3f09d5f01c78821eac28b229bd17db4d16950e10ebe55bb8927cc5dd201f19f",
              "s": "0x49e1e593afe189f5852bdaa8c26e9feaae060632508c8083e858c4acff0b7c1"
            },
            "timestamp": 1734390877237000000,
            "msg_hash": "0x6b7df61e6ee244a0c8451890f4953189a630b87c6520e7866f1e4b97e7d6475"
          }
        }
      ]
    },
    "ETHUSD": {
      "timestamp": 1734390877237000000,
      "asset_id": "ETHUSD",
      "signature_type": "stark",
      "trigger": "unspecified",
      "price": "4021139601187499000000",
      "signed_prices": [
        {
          "publisher_key": "0x41dbe627aeab66504b837b3abd88ae2f58ba6d98ee7bbd7f226c4684d9e6225",
          "external_asset_id": "0x455448555344000000000000000000005374437277",
          "signature_type": "stark",
          "price": "4021139601187499000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x6095485232570b1542511003cb0317c2eca891f913c079ccf1ad6823adc428e",
              "s": "0x406610914a813b101665f681c7a8207e22f7850b9ede5d504ae8927271154b3"
            },
            "timestamp": 1734390877136660700,
            "msg_hash": "0x692591526a6e8fe75042edcfee91b5b618bc50df6d7b62fb393bac8529a9bf0"
          }
        },
        {
          "publisher_key": "0x1f191d23b8825dcc3dba839b6a7155ea07ad0b42af76394097786aca0d9975c",
          "external_asset_id": "0x4554485553440000000000000000000053746b6169",
          "signature_type": "stark",
          "price": "4021139601187499000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x7ce01b6ef048f23b27a135c30e482feeab9506ab7adc2ead921c037680f1496",
              "s": "0x7a57496c674d8b23c39a2945c464406709cf0cb046c77e803118be171c89800"
            },
            "timestamp": 1734390877091606000,
            "msg_hash": "0x36b03ac79ef4b92a75cd53340b5efe8353a6ba57617e82af75cd14b13f4ec78"
          }
        },
        {
          "publisher_key": "0x6ee80350406f9e753797c3f0e1303a63ea2ae1f1adb86340e52722f41b31b64",
          "external_asset_id": "0x455448555344000000000000000000006465787472",
          "signature_type": "stark",
          "price": "4020807834000000000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x2f499d90a3975b400f489b4be35e74619b3ad9a454041417fe3781c6d31aa32",
              "s": "0x77cdb441ed66ece311490b710c2491255255a83abb05ed2e17b39a3da35cc32"
            },
            "timestamp": 1734390877237000000,
            "msg_hash": "0x62e7cb530499b2bfea2991f627bd400c73c84ff832587c0b1877f34973d7f7"
          }
        },
        {
          "publisher_key": "0xcc85afe4ca87f9628370c432c447e569a01dc96d160015c8039959db8521c4",
          "external_asset_id": "0x4554485553440000000000000000000053746f726b",
          "signature_type": "stark",
          "price": "4021139601187499000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x75108318337aa45f5be5751efae4c73a02bebdb72e1369eef8b60d088d0b20e",
              "s": "0x2abe50ca49f5b17f8cacde3e22201b0b0c344592af4c7501ea8108dcec699ff"
            },
            "timestamp": 1734390877091606000,
            "msg_hash": "0xb23b72178cfad0ac3d44a2069492928afc44f0441ec3292a52c54897d70b1f"
          }
        }
      ]
    }
  }
}
```

</details>

### Unsubscribe Message

```json
{
  "type": "unsubscribe", 
  "data": string[]
  ]
}  
```

#### **Description:**

Unsubscribe from updates for a subset of subscribed assets.

#### **Fields:**

* `"type"`: Type of the message. In this case `"unsubscribe"`.
* `"data"`: An array of plain-text [asset ids](../../introduction/core-concepts.md#asset-ids).

#### **Example:**

```json
{
  "type": "unsubscribe", 
  "data": [
    "BTCUSD", 
    "ETHUSD"
  ]
}  
```

### Unsubscribe Response

```
{
  "type": "unsubscribe",
  "data": {
    "subscriptions": string[]
  }
}

```

#### **Description:**

Response containing the resulting list of subscriptions.

#### **Fields:**

* `"type"`: Type of message. In this case `"unsubscribe"`.
* `"data"`:&#x20;
  * `"subscriptions"`: Updated list of plain-text asset ids you are subscribed to.

#### **Example:**

```json
{
  "type": "unsubscribe",
  "data": {
    "subscriptions": [
      "BTCUSDMARK"
    ]
  }
}
```
