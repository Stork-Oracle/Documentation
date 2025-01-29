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
curl -x GET 'https://rest.jp.stork-oracle.network/prices/assets' -H "Authorization: Basic gmork123"
```

## Rate Limits

There is currently a universal rate limit of 5 requests/sec.

{% hint style="info" %}
Need a higher rate limit? Reach out to Stork.  [sales@stork.network](mailto:sales@stork.network) or [Twitter DMs](https://x.com/storkoracle) open.
{% endhint %}

## Note

This tool is meant to illustrate the structure of REST api responses, but unfortunately due to third party limitations, some loss of precision on large numbers may be experienced in the browser. If you wish to test the verifiability of Stork prices from the REST api, we recommend using CURL to view the raw response.

{% swagger src="../.gitbook/assets/stork-oracle-api-openapi.yaml" path="/prices/assets" method="get" %}
[stork-oracle-api-openapi.yaml](../.gitbook/assets/stork-oracle-api-openapi.yaml)
{% endswagger %}

{% swagger src="../.gitbook/assets/stork-oracle-api-openapi.yaml" path="/prices/latest" method="get" %}
[stork-oracle-api-openapi.yaml](../.gitbook/assets/stork-oracle-api-openapi.yaml)
{% endswagger %}

{% swagger src="../.gitbook/assets/stork-oracle-api-openapi.yaml" path="/tradingview/history" method="get" %}
[stork-oracle-api-openapi.yaml](../.gitbook/assets/stork-oracle-api-openapi.yaml)
{% endswagger %}

{% swagger src="../.gitbook/assets/stork-oracle-api-openapi.yaml" path="/deployments/evm" method="get" %}
[stork-oracle-api-openapi.yaml](../.gitbook/assets/stork-oracle-api-openapi.yaml)
{% endswagger %}

{% swagger src="../.gitbook/assets/stork-oracle-api-openapi.yaml" path="/options/implied_volatility" method="get" %}
[stork-oracle-api-openapi.yaml](../.gitbook/assets/stork-oracle-api-openapi.yaml)
{% endswagger %}

{% swagger src="../.gitbook/assets/stork-oracle-api-openapi.yaml" path="/options/underlying_future_price" method="get" %}
[stork-oracle-api-openapi.yaml](../.gitbook/assets/stork-oracle-api-openapi.yaml)
{% endswagger %}

