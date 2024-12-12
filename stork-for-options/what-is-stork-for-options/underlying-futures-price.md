# Underlying Futures Price

Example query:

```
curl 'https://{url}/v1/options/underlying_future_price?symbol={symbol}&expiry={YYYY-MM-DD}&strike={strike}&type={type}' -H 'Authorization: Basic {token}'
```

Example output:&#x20;

```
{"symbol":"BTC","expiry":"2024-08-23","strike":"52000","type":"CALL","timestamp":1723666987674359659,"signed_underlying_future_prices":[{"underlying_future_price":"59143112000000007000000","timestamped_signature":{"signature":{"r":"0xa56b13945262499626b23e96ad21748f2040b676fef998f9f72ae6cae326dd2d","s":"0x5898eda4549c8386c1a58d3bec6391b5a6b2db5cb2dce98168bea599ed87e1e0","v":"0x1b"},"timestamp":1723666987674232594,"msg_hash":"0x7fb21a290c88d7c55b3a8f2072b11e81979425c74e2e526e791438ee984edbaa"},"external_asset_id":"BTC-2024-08-23-52000-CALL","public_key":"0xF024A9AA110798e5CD0d698FBA6523113Eaa7FB2"}]}
```



**Path Parameters**

<table><thead><tr><th width="348">Name</th><th>Description</th></tr></thead><tbody><tr><td>symbol</td><td>BTC, ETH, MATIC, SOL, XRP</td></tr><tr><td>expiry</td><td>Expiry date for the contract in the format YYYY-MM-DD</td></tr><tr><td>strike</td><td>Option strike price in USD</td></tr><tr><td>type</td><td>CALL or PUT</td></tr></tbody></table>
