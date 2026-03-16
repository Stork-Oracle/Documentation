---
icon: gear-complex
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
Need a higher rate limit? Reach out to Stork. [sales@stork.network](mailto:sales@stork.network) or [Twitter DMs](https://x.com/storkoracle) open.
{% endhint %}

## Note

This tool is meant to illustrate the structure of REST api responses, but unfortunately due to third party limitations, some loss of precision on large numbers may be experienced in the browser. If you wish to test the verifiability of Stork prices from the REST api, we recommend using CURL to view the raw response.

{% openapi-operation spec="rest-api-2" path="/v1/prices/assets" method="get" %}
[OpenAPI rest-api-2](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/584e7e5c1957fcf41eb4705c636f2742173cf076810e8870cc4252271c95608f.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260316%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260316T180923Z&X-Amz-Expires=172800&X-Amz-Signature=bf2027c9e878208dd3e8e68ec7d40f618da959fb113a985dba03cdcbf68fa72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-2" path="/v1/prices/latest" method="get" %}
[OpenAPI rest-api-2](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/584e7e5c1957fcf41eb4705c636f2742173cf076810e8870cc4252271c95608f.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260316%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260316T180923Z&X-Amz-Expires=172800&X-Amz-Signature=bf2027c9e878208dd3e8e68ec7d40f618da959fb113a985dba03cdcbf68fa72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-2" path="/v1/prices/recent" method="get" %}
[OpenAPI rest-api-2](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/584e7e5c1957fcf41eb4705c636f2742173cf076810e8870cc4252271c95608f.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260316%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260316T180923Z&X-Amz-Expires=172800&X-Amz-Signature=bf2027c9e878208dd3e8e68ec7d40f618da959fb113a985dba03cdcbf68fa72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-2" path="/v1/tradingview/history" method="get" %}
[OpenAPI rest-api-2](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/584e7e5c1957fcf41eb4705c636f2742173cf076810e8870cc4252271c95608f.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260316%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260316T180923Z&X-Amz-Expires=172800&X-Amz-Signature=bf2027c9e878208dd3e8e68ec7d40f618da959fb113a985dba03cdcbf68fa72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-2" path="/v1/deployments/evm" method="get" %}
[OpenAPI rest-api-2](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/584e7e5c1957fcf41eb4705c636f2742173cf076810e8870cc4252271c95608f.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260316%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260316T180923Z&X-Amz-Expires=172800&X-Amz-Signature=bf2027c9e878208dd3e8e68ec7d40f618da959fb113a985dba03cdcbf68fa72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-2" path="/v0/deployments/stork_pushed_assets" method="get" %}
[OpenAPI rest-api-2](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/584e7e5c1957fcf41eb4705c636f2742173cf076810e8870cc4252271c95608f.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260316%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260316T180923Z&X-Amz-Expires=172800&X-Amz-Signature=bf2027c9e878208dd3e8e68ec7d40f618da959fb113a985dba03cdcbf68fa72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

{% openapi-operation spec="rest-api-2" path="/v1/market_status" method="get" %}
[OpenAPI rest-api-2](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/584e7e5c1957fcf41eb4705c636f2742173cf076810e8870cc4252271c95608f.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260316%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260316T180923Z&X-Amz-Expires=172800&X-Amz-Signature=bf2027c9e878208dd3e8e68ec7d40f618da959fb113a985dba03cdcbf68fa72f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}
