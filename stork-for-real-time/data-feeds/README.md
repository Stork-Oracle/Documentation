# Data Feeds

Stork publishers and data sources are chosen for their demonstrated ability to reliably provide low latency price updates. The methodologies are chosen to enable Stork clients to achieve specific results, and will evolve over time.&#x20;

### Available Stork Indices

{% content-ref url="index-price.md" %}
[index-price.md](index-price.md)
{% endcontent-ref %}

{% content-ref url="perpetual-future-mark-price-index.md" %}
[perpetual-future-mark-price-index.md](perpetual-future-mark-price-index.md)
{% endcontent-ref %}

### Available Markets&#x20;

{% content-ref url="available-markets.md" %}
[available-markets.md](available-markets.md)
{% endcontent-ref %}

## Using Stork in a Perpetual Exchange

#### Calculating Funding Rate

We recommend using the spot index price and your exchange’s contract price, to calculate the funding rate. If you elect to calculate the funding rate in discrete interval, we recommend using a time-weighted average.

#### Calculating Liquidations

We recommend using the mark price for liquidations, as it is meant to reflect the prevailing market price of the underlying contract.
