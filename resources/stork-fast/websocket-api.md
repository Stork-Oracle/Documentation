---
description: Listening to Fast data via Websocket
icon: tower-broadcast
---

# Websocket API

## Base URL <a href="#docs-internal-guid-d4cb22e5-7fff-2fca-bda6-6ebbd048997a" id="docs-internal-guid-d4cb22e5-7fff-2fca-bda6-6ebbd048997a"></a>

The base URL for Fast is dependent on which Fast instance you're using. The URL will be in the form:

```
wss://<fast-identifier>.fast.jp.stork-oracle.network
```

The main instance of fast is:

```
wss://fast.jp.stork-oracle.network
```

## Authentication <a href="#docs-internal-guid-f0db63fb-7fff-3116-d4a7-e3b22d6d2087" id="docs-internal-guid-f0db63fb-7fff-3116-d4a7-e3b22d6d2087"></a>

All WebSocket connection requests must include an Authorization header with the value set as `Basic <token>`. For example, if your token is gmork123:

```bash
wscat -c 'wss://fast.jp.stork-oracle.network/ws' -H "Authorization: Basic gmork123"
```

## Endpoints <a href="#docs-internal-guid-1e5f604e-7fff-dc92-44c2-ff9a56912358" id="docs-internal-guid-1e5f604e-7fff-dc92-44c2-ff9a56912358"></a>

### /ws

#### Description

Subscribe to listen to Stork Fast data streams.

#### Query Parameters

Stork Fast supports a number of query parameters to configure messages coming from Stork Fast.

**Channel**

The `channel` query parameter specifies the channel Fast should send data to you on. Latency does not differ between channels. The following channels are generally available:<br>

* `10ms`: Fixed rate messages every 10ms
* `20ms`:  Fixed rate messages every 20ms
* `50ms`: Fixed rate messages every 50ms
* `100ms`: Fixed rate messages every 100ms
* `500ms`: Fixed rate messages every 500ms
* `1s`: Fixed rate messages every 1s
* `real_time`: Messages only on value change, no faster than 1ms

**Message Type**

The `message_type` query parameter determines the structure of the data coming from Fast. Fast currently supports two message types:<br>

* `unsigned`: An unsigned message type, primarily intended for human readability
* `signed_ecdsa`: A verifiable message type including an ECDSA signature. Comprised of a single bit-packed payload for maximum on-chain efficiency. Not human-readable.

**Additional Attributes**

The `addtl_attrs` query parameter opts in to additional per-asset attributes beyond price. It accepts a comma-separated list of attribute names. The following attributes are supported:

* `ms`: Market status — the market status code in effect for each asset at the message's timestamp

For example, to receive market status alongside prices:

```bash
wscat -c 'wss://fast.jp.stork-oracle.network/ws?addtl_attrs=ms' -H "Authorization: Basic gmork123"
```

Market status codes are:

| Code | Status         |
| ---- | -------------- |
| 0    | Closed         |
| 1    | Regular hours  |
| 2    | Extended hours |
| 3    | After hours    |

Market status is only meaningful for assets with a market schedule (e.g. equities). Assets that trade continuously (e.g. crypto) have no market status: the `ms` field is omitted for those assets in `unsigned` messages, and set to `0xFF` in `signed_ecdsa` payloads.

The current market status is delivered inline with every price update. To also see the next upcoming status and the time at which it takes effect, use the `/v1/market_status` endpoint on the [REST API](rest-api.md).

## Messages <a href="#docs-internal-guid-b8749ed2-7fff-8573-9566-41fd1c1d5fbb" id="docs-internal-guid-b8749ed2-7fff-8573-9566-41fd1c1d5fbb"></a>

### Subscribe Message

```json
{
    "type": "subscribe",
    "assets": int[]
}
```

#### Description

Subscribe to receive updates for the specified assets.

**Fields**

* `type`: Type of the message. In this case, `subscribe`
* `assets`: An array of uint16 asset IDs

#### Example

```json
{
    "type": "subscribe",
    "assets": [1,2,10,34]
}
```

### Unsubscribe Message

```json
{
    "type": "usubscribe",
    "assets": int[]
}
```

#### Description

Unsubscribe from updates for a subset of subscribed assets.

#### Fields

* `type`: Type of the message. In this case, `unsubscribe`
* `data`: An array of uint16 asset IDs

#### Example

```json
{
    "type": "unsubscribe",
    "assets": [1,2,10]
}
```

### Unsigned Message

```json
{
    "type": "unsigned",
    "tax": int,
    "ts": int,
    "a": asset_value_pairs[]
}
```

#### Description

An unsigned non-verifiable message type containing human-readable asset updates.

#### Fields

* `type`: Type of the message. In this case, `unsigned`
* `tax`: Taxonomy ID the Fast instance is using
* `ts`: The UNIX nanosecond timestamp for the message
* `a`: An array of asset value pairs in the form of `{"id": int, "v": string}`&#x20;
  * `id`: uint16 asset ID
  * `v`: 10^18 scaled value as a string
  * `ms`: The asset's current market status code (see [Additional Attributes](websocket-api.md#query-parameters)). Only present when the connection was opened with `addtl_attrs=ms`, and omitted for assets with no market schedule

#### Example

```json
{
    "type": "unsigned",
    "tax": 1,
    "ts": 1764608698685038908,
    "a": [
        {
            "id": 1,
            "v": "999875000000000069"
        },
        {
            "id": 2,
            "v": "999825006250000036"
        },
        {
            "id": 10,
            "v": "12693413125000001073"
        },
        {
            "id": 34,
            "v": "2739391501743055414408"
        }
    ]
}
```

When connected with `addtl_attrs=ms`, assets with a market schedule additionally include the `ms` field:

```json
{
    "type": "unsigned",
    "tax": 1,
    "ts": 1764608698685038908,
    "a": [
        {
            "id": 1,
            "v": "999875000000000069"
        },
        {
            "id": 12001,
            "v": "6540000000000000",
            "ms": 1
        }
    ]
}
```



### Signed ECDSA Message

```json
{
    "type": "signed_ecdsa",
    "p": string
}
```

#### Description

An ECDSA signed verifiable message type containing a bitpacked payload for submission on-chain.

#### Fields

* `type`: Type of the message. In this case, `signed_ecdsa`
* `p`: The bitpacked verifiable payload in the form of a hex string. The first 65 bytes of this payload are the signature

#### Payload Layout

When connected without `addtl_attrs`, the payload after the 65-byte signature is laid out as:

```
taxonomy ID (2 bytes) || timestamp ns (8 bytes) || N x [ asset ID (2 bytes) || quantized value (16 bytes) ]
```

When connected with `addtl_attrs` (e.g. `addtl_attrs=ms`), the payload after the signature uses a versioned layout that carries the additional attributes in each asset record:

```
0xFF (1 byte) || version 0x02 (1 byte) || attribute mask (2 bytes) || taxonomy ID (2 bytes) || timestamp ns (8 bytes) || N x [ asset ID (2 bytes) || quantized value (16 bytes) || ms (1 byte) ]
```

* All multi-byte fields are big-endian
* The leading `0xFF` byte unambiguously distinguishes the versioned layout from the legacy layout
* The attribute mask is a uint16 bitmask declaring which attributes each asset record contains: bit 0 is price (always set) and bit 1 is market status (`ms`). Attribute bytes appear within each record in ascending mask-bit order
* `ms` is the asset's market status code, or `0xFF` for assets with no market schedule

#### Example

A message using the legacy layout (connected without `addtl_attrs`):

```json
{
    "type": "signed_ecdsa",
    "p": "0x435766eac9298f4dcbfe8bdfe46361161d6eeca88f783e3cd215db90c0581cd1511382180840e70bfd43e5382aa4e4c2910aca251ee2c3a5e27d5343fb105556010001187d265fe630404b000100000000000000000de029bae7734fef000200000000000000000ddffc432d25cd5c000a0000000000000000b02db33d2f95811c0022000000000000009480fc8e62b51ff1ac"
}
```

A message using the versioned layout (connected with `addtl_attrs=ms`):

```json
{
    "type": "signed_ecdsa",
    "p": "0xc8a24321a3f048143b54784ce120006b188cd2c6ff10100a24e655253bb870b3398a898330b3a8e25e222c2300660e77b6e66065878893d7af2f8ff92822c99e01ff0200030001187d26431cafa13c000100000000000000000de04503d2cb3045ff2ee1000000000000000000173c1868d4c00001"
}
```

Broken down after the 65-byte signature, this payload reads as:

| Bytes                                | Field                                     |
| ------------------------------------ | ----------------------------------------- |
| `ff`                                 | Versioned layout magic byte               |
| `02`                                 | Layout version                            |
| `0003`                               | Attribute mask (price + market status)    |
| `0001`                               | Taxonomy ID (1)                           |
| `187d26431cafa13c`                   | Timestamp (1764608698685038908 ns)        |
| `0001`                               | Asset ID (1)                              |
| `00000000000000000de04503d2cb3045`   | Quantized value (999875000000000069)      |
| `ff`                                 | Market status (no market schedule)        |
| `2ee1`                               | Asset ID (12001)                          |
| `000000000000000000173c1868d4c000`   | Quantized value (6540000000000000)        |
| `01`                                 | Market status (regular hours)             |
