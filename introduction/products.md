---
icon: shelves
description: Stork for Real Time, Options, StarkEx, and the Composite Oracle Service.
---

# Products

### Stork for Real Time <a href="#docs-internal-guid-3dcde64a-7fff-735c-30d3-8dbb57e505e2" id="docs-internal-guid-3dcde64a-7fff-735c-30d3-8dbb57e505e2"></a>

Stork for Real Time is an ultra low-latency, decentralized off and on-chain price feed designed for any chain. Stork for Real Time is powered by a decentralized network of data publishers, and signed with a cross-chain compatible signature.  Stork for Real Time prioritizes performance, using ultra-fast websockets to ensure data is available at the millisecond level, similar to the data used for trading in TradFi.

Using an off-chain, decentralized feed gives protocols the ability to perform initial processing off-chain, and elect to only push on-chain the price updates that are relevant to their product. Since prices are signed in a chain-compatible way, protocols can use Stork’s Contract, or their own smart contract, to verify the feed on-chain, proving that the data is legitimate.

### Stork for Options

Stork for Options is a just-in-time derivative oracle. Queried via REST API, derivatives such as

* Implied Volatility
* Underlying Futures Prices

among others are calculated upon API request based on Storks real time prices. For more information on using Stork for Options, see [REST API](../api-reference/rest-api.md).

### Stork for StarkEx

Stork maintains a first class partnership with StarkEx. This enables Stork to provide oracle services that are accepted natively by StarkEx. The key difference between Stork for Real Time and Stork for StarkEx is that the signatures used are compatible with StarkEx, and present only in the publisher messages. Also, publishers use StarkEX's native signatures when providing data for StarkEX users.

### Composite Oracle Service

A Composite Oracle Service (COS) allows for modular and configurable custom [Aggregators](how-it-works.md#aggregators) enabled by Storks core architecture. A COS is a tuned oracle that provides aggregated data leveraging Stork's decentralized publisher network, while creating a composite of the specific assets and aggregation methods required by a [Subscriber](how-it-works.md#subscribers).

For more information about how Stork’s core architecture enables COS, see [How It Works](how-it-works.md).

{% hint style="info" %}
Interested? Contact Stork Labs to determine appropriate feeds that meet your requirements.  [sales@stork.network](mailto:sales@stork.network) or [Twitter DMs](https://twitter.com/StorkOracle) open.
{% endhint %}



