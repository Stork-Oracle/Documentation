# REST API

## Last Price

Use `v1/prices/latest` to retrieve the latest price update for one or more feeds. The following command retrieves the latest price update for BTCUSD.

```
curl 'https://<url>/v1/prices/latest?assets=BTCUSD' -H 'Authorization: Basic <your token>'
```

Example output

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
  }
}
```

## Historical Data

Stork offers OHLCV that conforms to TradingView's UDF to ensure easy integration in front ends. For reference: [https://www.tradingview.com/charting-library-docs/latest/connecting\_data/UDF/#bars](https://www.tradingview.com/charting-library-docs/latest/connecting_data/UDF/#bars) Historical data is available starting July 1, 2024 at a 15 second level granularity. Use `/v1/tradingview/history` with the following example command to retrieve OHLCV data:&#x20;

```
curl 'https://<url>/v1/tradingview/history?from=1719345000&to=1719345579&resolution=1&symbol=BTCUSD' -H "Authorization: <your token>"
```

Example output:&#x20;

```
{"t":[1721483460,1721483520],"o":[66490.0863555,66481.235863],"h":[66495.7889285,66499.19999950001],"l":[66473.2349995,66481.235863],"c":[66484.7385225,66495.1661915]} 
```
