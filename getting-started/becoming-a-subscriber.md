---
icon: download
description: Consuming data from Stork.
---

# Becoming a Subscriber

Subscribers on Stork are the consumers of Stork aggregated data.

### Who Can Become a Subscriber?

Anyone who has a need for high-frequency, high-accuracy, low-latency data can become a Subscriber. Storks data feeds are measurably faster, more efficient and more stable than contemporary oracles.

### Using Data Off-Chain

Using data off-chain is as simple as listening to the [Aggregator](../introduction/how-it-works.md#aggregators) [websocket](../api-reference/websocket-api/) or hitting it's [REST API](../api-reference/rest-api.md), and then using the update data in your application. Both APIs respond with JSON messages that have a top level field called `data` with the following structure:

<pre><code><strong>{
</strong><strong>    "data": [
</strong>        "&#x3C;plain-text asset id>": {
            "timestamp": &#x3C;unix timestamp>,
            "asset_id": "&#x3C;plain-text asset id>,
            "signature_type": "&#x3C;signature type - evm | stark>",
            "trigger": "&#x3C;trigger>",
            "price": "&#x3C;price multiplied by 10^18>",
            "stork_signed_price": {
                "public_key": "&#x3C;stork aggregator public key>",
                "encoded_asset_id": "&#x3C;keccak256 encoded asset id>",
                "price": "&#x3C;price multiplied by 10^18>",
                "timestamped_signature": {
                    "signature": {
                        "r": "&#x3C;r component of ECDSA secp256k1 signature>",
                        "s": "&#x3C;r component of ECDSA secp256k1 signature>",
                        "v": "&#x3C;s component of ECDSA secp256k1 signature"
                    },
                    "timestamp": &#x3C;unix timestamp>,
                    "msg_hash": "keccak256 message hash"
                },
                "publisher_merkle_root": "&#x3C;publisher merkle root",
                "calculation_alg": {
                    "type": "&#x3C;aggregation function name>",
                    "version": "&#x3C;aggregation function version",
                    "checksum": "&#x3C;checksum for aggregation function>"
                }
            },
            "signed_prices": [
                {
                    "publisher_key": "&#x3C;publishers public key>",
                    "external_asset_id": "&#x3C;plain-text asset id",
                    "signature_type": "&#x3C;signature type - evm | stark>",
                    "price": "price multiplied by 10^18",
                    "timestamped_signature": {
                        "signature": {
                            "r": "&#x3C;r component of ECDSA secp256k1 signature>",
                            "s": "&#x3C;r component of ECDSA secp256k1 signature>",
                            "v": "&#x3C;s component of ECDSA secp256k1 signature"
                        },
                        "timestamp": &#x3C;unix timestamp>,
                        "msg_hash": "&#x3C;keccak256 message hash>"
                    }
                },
                ...
            ]
        }
    }
}
</code></pre>

## Using Data On-Chain

For information on putting data on-chain and accessing it from your smart-contract, see the following sections:

{% content-ref url="putting-data-on-chain.md" %}
[putting-data-on-chain.md](putting-data-on-chain.md)
{% endcontent-ref %}

{% content-ref url="accessing-data-on-chain.md" %}
[accessing-data-on-chain.md](accessing-data-on-chain.md)
{% endcontent-ref %}

{% hint style="info" %}
Interested in becoming a Subscriber? Contact Stork Labs! Email: [sales@stork.network](mailto:sales@stork.network) Twitter: [@StorkOracle](https://x.com/StorkOracle)
{% endhint %}
