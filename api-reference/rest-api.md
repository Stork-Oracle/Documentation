---
icon: gear-complex
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# REST API

Real-Time and historical Data API for Stork signed data.

## Authentication

All REST requests must include an `Authorization` header with the value set as `Basic <token>` . For example if your token is `gmork123`:

```bash
curl -X GET 'https://rest.jp.stork-oracle.network/v1/prices/assets' -H "Authorization: Basic gmork123"
```

## Rate Limits

There is currently a universal rate limit of 5 requests/sec.

{% hint style="info" %}
Need a higher rate limit? Reach out to Stork.  [sales@stork.network](mailto:sales@stork.network) or [Twitter DMs](https://x.com/storkoracle) open.
{% endhint %}

## Note

This tool is meant to illustrate the structure of REST api responses, but unfortunately due to third party limitations, some loss of precision on large numbers may be experienced in the browser. If you wish to test the verifiability of Stork prices from the REST api, we recommend using CURL to view the raw response.

{% openapi-operation spec="rest-api-1" path="/v1/prices/assets" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-1" path="/v1/prices/latest" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-1" path="/v1/prices/recent" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-1" path="/v1/tradingview/history" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-1" path="/v1/deployments/evm" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-1" path="/v0/deployments/stork_pushed_assets" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-1" path="/v1/options/implied_volatility" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-1" path="/v1/options/underlying_future_price" method="get" %}
[Broken link](broken-reference)
{% endopenapi-operation %}
