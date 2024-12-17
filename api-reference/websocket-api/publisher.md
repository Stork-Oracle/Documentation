---
description: Publishing data to a Stork Aggregator via WebSocket.
icon: upload
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

# Publisher

## Base Endpoint

The standard endpoint for interacting with Stork via websocket is:

```url
wss://api.jp.stork-oracle.network
```

## Authentication

All websocket connection requests must include an `Authorization` header with the value set as `Basic <token>` . For example:

```bash
wscat -c 'wss://api.jp.stork-oracle.network/evm/publish' -H "Authorization: Basic fakeToken123"
```

## Endpoints

### /evm/publish

Publish signed data updates using EVM-compatible signatures.

#### Example:

```bash
wscat -c 'wss://api.jp.stork-oracle.network/evm/publish' -H "Authorization: Basic fakeToken123"
```

### /stark/publish

Publish signed data updates using Stark-compatible signatures

#### Example:

```bash
wscat -c 'wss://api.jp.stork-oracle.network/stark/publish' -H "Authorization: Basic fakeToken123"
```

## Messages

### Publish Message

```
{
  "type": "signed_prices",
  "trace_id": string,
  "data": {
    string: {
      "oracle_id": string,
      "asset_id": string,
      "trigger": string,
      "signed_price": {
        "publisher_key": string,
        "external_asset_id": string,
        "signature_type": string,
        "price": string,
        "timestamped_signature": {
          "signature": {
            "r": string,
            "s": string,
            "v": string
          },
          "timestamp": string,
          "msg_hash": string
        },
        "metadata": object // optional
      }
    }
  }
}
```

#### **Description:**

Publish signed price updates for one or more assets.

#### **Fields:**

* `"type"`: Type of the message. Always `"signed_prices"`.
* `"trace_id"`: A unique identifier for debugging purposes.
* `"data"`: An object containing updates for each asset. Each key represents an asset ID, and the value is the signed price update:
  * `"oracle_id"`: ID of the oracle.
  * `"asset_id"`: The asset being updated.
  * `"trigger"`: The event triggering this update.
  * `"signed_price"`:
    * `"publisher_key"`: The public key of the publisher.
    * `"external_asset_id"`: The external representation of the asset ID.
    * `"signature_type"`: Signature type (e.g., `evm` or `stark`).
    * `"price"`: The updated price.
    * `"timestamped_signature"`:
      * `"signature"`: The cryptographic signature of the update.
        * `"r"`: R-component of the signature.
        * `"s"`: S-component of the signature.
        * `"v"`: V-component of the signature (only for EVM signatures).
      * `"timestamp"`: Timestamp of the signed update.
      * `"msg_hash"`: The hash of the message being signed.
    * `"metadata"`: Any additional information related to the update. Optional.

#### **Example:**

<details>

<summary>EVM message</summary>

```json
{
  "type": "signed_prices",
  "trace_id": "a607510a-dd9e-4f3a-991e-79622da7705a",
  "data": {
    "BTCUSD": {
      "oracle_id": "anorith",
      "asset_id": "BTCUSD",
      "trigger": "delta",
      "signed_price": {
        "publisher_key": "0x99e295e85cb07c16b7bb62a44df532a7f2620237",
        "external_asset_id": "BTCUSD",
        "signature_type": "evm",
        "price": "65162563534000004000000",
        "timestamped_signature": {
          "signature": {
            "r": "0xce902399d68a0a28daace3ee18f91484331b18f420243f3421d34ba9f28f8e8a",
            "s": "0x7396001963580285b4d1d9dc58880ee447b89e118c89736d079dc56f52455353",
            "v": "0x1b"
          },
          "timestamp": 1711048112688000000,
          "msg_hash": "0x94d25a6173f3914ae4a9d728669460de5f2866a525d6718587929e6c669c033b"
        },
        "metadata": {}
      }
    }
  }
}
```

</details>

<details>

<summary>Stark message</summary>

```json
{
  "type": "signed_prices",
  "trace_id": "c8a91317-e9fb-450b-89b2-311f0f7ae6b4",
  "data": {
    "BTCUSD": {
      "oracle_id": "anorith",
      "asset_id": "BTCUSD",
      "trigger": "delta",
      "signed_price": {
        "publisher_key": "0x7884106fe3eb409b15060046ff09c8b12795c1e7b1dd5dce4356c73d460d0d3",
        "external_asset_id": "0x42544355534400000000000000000000616e6f72697468",
        "signature_type": "stark",
        "price": "65223032635000000000000",
        "timestamped_signature": {
          "signature": {
            "r": "0x42d558a94fa02c23cc2d7919db7da0f9e892f023f51b31f20cdf0be171ddbb4",
            "s": "0x79f718337da68f6157f008fc22d7678180c45f0ac158451e35571760b922c30"
          },
          "timestamp": 1711048368688000000,
          "msg_hash": "0x879028c00132d8e5ad03796bf684b918c61a6c625d76164c56fc910600762c"
        },
        "metadata": {}
      }
    }
  }
}
```

</details>

