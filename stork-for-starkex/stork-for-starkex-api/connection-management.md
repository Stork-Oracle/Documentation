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
      "timestamp": 1710793255893000000,
      "asset_id": "BTCUSD",
      "signature_type": "stark",
      "trigger": "clock",
      "price": "67136003187500004000000",
      "signed_prices": [
        {
          "publisher_key": "0x2af6b47b91065e079b4481923bfef55b9bee017824e87a07c6b93826938cc15",
          "external_asset_id": "0x4254435553440000000000000000000064656f787973",
          "signature_type": "stark",
          "price": "67139662309000004000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x21831260ced1f96ad9668feed5952f3d8c12d4a83c091c46028c5c78b11b86d",
              "s": "0x4c93a0d64388c48e02fc5c6a9380e79f0ef59bae595757f91a86b12e2f6d1d3"
            },
            "timestamp": 1710793255662000000,
            "msg_hash": "0x157f10eb4871a08dd447fd19919551375c1a23cc69ae4f77acf9f53d42ca0b9"
          }
        },
        {
          "publisher_key": "0x7884106fe3eb409b15060046ff09c8b12795c1e7b1dd5dce4356c73d460d0d3",
          "external_asset_id": "0x42544355534400000000000000000000616e6f72697468",
          "signature_type": "stark",
          "price": "67130784981000006000000",
          "timestamped_signature": {
            "signature": {
              "r": "0x7ee801acb04d23869406db1eb32028c3a622e92a8514facd6f1a81448eef80e",
              "s": "0x24effc9f672086978cf2bea500bc0b61f700d68b7d2e8623186542bdc6e93e4"
            },
            "timestamp": 1710793255662000000,
            "msg_hash": "0xfe646785414b61892b18da221d27a28c9cd2724aaaaddf8e94dde92e2c04cf"
          }
        },
        // ... more signed prices
      ]
    },
    // ... more assets
  }
}
```

