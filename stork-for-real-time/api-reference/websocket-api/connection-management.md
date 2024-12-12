# Connection Management

## Subscribing

After connecting, users should send a subscription message containing a list of assets to subscribe to.

* For better throughput and resource utilization, we recommended subscribing to all desired assets on a single connection.

Example `subscribe` message:

```
{
  "type": "subscribe", 
  "trace_id": "123",   // optional, will be echoed back in the response
  "data": [
    "BTCUSD", 
    "ETHUSD", 
    "BTCUSDMARK"
  ]
}  
```

A subscription response will contain your connection's current list of subscribed assets.

An example subscription response:

```
{
  "type": "subscribe",
  "trace_id": "123",
  "data": {
    "subscriptions": [
      // includes all current subscriptions, not just those in the request (e.g. ARBUSDMARK)
      "BTCUSD",
      "ETHUSD",
      "ARBUSDMARK",   
      "BTCUSDMARK"
    ]
  }
}
```

### Unsubscribing

To unsubscribe from receiving price updates for certain assets, send an unsubscription message:

```
{
  "type": "unsubscribe", 
  "data": [
    "BTCUSD", 
    "ETHUSD"
  ]
}  
```

An unsubscription response will contain the connections resulting list of subscriptions:

```
{
  "type": "unsubscribe",
  "data": {
    "subscriptions": [
      "ARBUSDMARK",
      "BTCUSDMARK"
    ]
  }
}
```

## Aggregated price updates

After subscribing to assets (and possibly before receiving the response) users should expect to receive messages with `"type": "aggregated_signed_prices"` with following format:

```
{
  "type": "oracle_prices",
  "data": {
    "BTCUSD": {
      "timestamp": 1710793460536000000,
      "asset_id": "BTCUSD",
      "signature_type": "evm",
      "trigger": "clock",
      "price": "67102388324000000000000",
      "signed_prices": [
        {
          "publisher_key": "0x99e295e85cb07c16b7bb62a44df532a7f2620237",
          "external_asset_id": "BTCUSD",
          "signature_type": "evm",
          "price": "67103323593999999000000",
          "timestamped_signature": {
            "signature": {
              "r": "0xddf82a82acdd8c8e6013e11bc7ce48dde448ee7dd45afcc7624c48fd353c19fb",
              "s": "0x357394c65988ae3b8a8c842e1b58644cdf2eaa71ba264667428e12bb57d2bf7b",
              "v": "0x1b"
            },
            "timestamp": 1710793460536000000,
            "msg_hash": "0x54b8509f1adb8b14a198b563e19c885ba6b399e36f68b86a587d666460ccca8f"
          }
        },
        {
          "publisher_key": "0xa63f5c960e57f6f0dda4fdb7e452e4dfc5e332dd",
          "external_asset_id": "BTCUSD",
          "signature_type": "evm",
          "price": "67094088774999999000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x71a8073e64a70becd98ee70800fd52b1fd9f5b286ce25a3f86f6931d8c457694",
              "s": "0x773cdc496cf6965e6bbccade7fa816133829db5e141b857e92bf015dfb738c5d",
              "v":"0x1c"
            },
            "timestamp": 1710793460536000000,
            "msg_hash": "0x9ceec9a17c4d8974d435b0129a605878be09db7679a1c6ada99ffa3479371963"
          }
        },
        // ... more signed prices
      ]
    },
    // ... more assets
  }
}
```

