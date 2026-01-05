---
description: Listening to Fast data via Websocket
icon: tower-broadcast
layout:
  width: default
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
  metadata:
    visible: true
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

#### Example

```json
{
    "type": "signed_ecdsa",
    "p": "0x435766eac9298f4dcbfe8bdfe46361161d6eeca88f783e3cd215db90c0581cd1511382180840e70bfd43e5382aa4e4c2910aca251ee2c3a5e27d5343fb105556010001187d265fe630404b000100000000000000000de029bae7734fef000200000000000000000ddffc432d25cd5c000a0000000000000000b02db33d2f95811c0022000000000000009480fc8e62b51ff1ac"
}
```
