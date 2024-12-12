# Implied Volatility

Implied volatility feeds are calculated based on the mark implied volatilities across major options CEXs, such as Deribit, Binance, Bybit, and OKX.&#x20;

Example query

```
curl 'https://{url}/v1/options/implied_volatility?symbol={symbol}&expiry={expiry}&strike={strike}&type={type}' -H 'Authorization: Basic {token}'
```

Example output

```
{"symbol":"BTC","expiry":"2024-08-23","strike":"52000","type":"CALL","timestamp":1723578794789377178,"signed_implied_volatilities":[{"external_asset_id":"BTC-2024-08-23-52000-CALL","implied_volatility":"68834721046622000000","timestamped_signature":{"signature":{"r":"0x197aac72c14d2a53b58827ebae5a4046af33c8fcf55093d427f6024b42c7b69a","s":"0x2aacc17b1a1f17d085fe9cdee361b67752f0711906c8a2afe459abe6fd203661","v":"0x1b"},"timestamp":1723578794497305464,"msg_hash":"0xe474226b1eae19fe49eeba1cf721b71b64282d3292b03b86385c79b6874aedc5"},"public_key":"0xF024A9AA110798e5CD0d698FBA6523113Eaa7FB2"}]}
```



**Path Parameters**

<table><thead><tr><th width="348">Name</th><th>Description</th></tr></thead><tbody><tr><td>symbol</td><td>BTC, ETH, MATIC, SOL, XRP</td></tr><tr><td>expiry</td><td>Expiry date for the contract in the format YYYY-MM-DD</td></tr><tr><td>strike</td><td>Option strike price in USD</td></tr><tr><td>type</td><td>CALL or PUT</td></tr></tbody></table>
