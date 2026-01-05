---
icon: gear-complex
layout:
  width: default
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
  metadata:
    visible: true
---

# REST API

Instance level information for Stork Fast

## Authentication

All REST requests must include an `Authorization` header with the value set as `Basic <token>` . For example if your token is `gmork123`:

```bash
curl -X GET 'https://fast.jp.stork-oracle.network/v1/prices/assets' -H "Authorization: Basic gmork123"
```

## Rate Limits

There is currently a universal rate limit of 5 requests/sec.

{% hint style="info" %}
Need a higher rate limit? Reach out to Stork. [sales@stork.network](mailto:sales@stork.network) or [Twitter DMs](https://x.com/storkoracle) open.
{% endhint %}

## Note

This tool is meant to illustrate the structure of REST api responses, but unfortunately due to third party limitations, some loss of precision on large numbers may be experienced in the browser. If you wish to test the verifiability of Stork prices from the REST api, we recommend using CURL to view the raw response.



coming soon...
