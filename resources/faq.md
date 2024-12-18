---
icon: message-question
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

# FAQ



<details>

<summary>What kind of data can I use with Stork?</summary>

Stork is designed to be used with any data that can be represented as a number and timestamp. For more information on this, please see [Core Concepts](../introduction/core-concepts.md#temporal-numeric-values).

</details>

<details>

<summary>How can I estimate gas fees for running the Chain Pusher?</summary>

Estimating gas fees for putting data on chain with the Chain Pusher can be difficult. This is due to a couple reasons:

* Gas prices vary chain-to-chain, even Testnet-to-Mainnet of the same chain.
* Gas prices can vary based on block-to-block or epoch-to-epoch network conditions on some chains.

That being said, Stork has written our contracts to be optimized for gas efficiency, so you can be sure the gas to put an update on-chain is the lowest you can get with any oracle.

</details>

<details>

<summary>How does Stork ensure data security and integrity?</summary>

Stork ensures data security and integrity via two methods.

Firstly, Stork uses a series of signatures and verifications to validate that data is always coming from where it says it is, ensuring security. For more information, see [How It Works](../introduction/how-it-works.md#verifiability).

Secondly, Stork uses multiple decentralized publishers feeding data to the Aggregator, which are then aggregated in a way to protect against errant publishers feed bad or malicious data. For More information, see [How It Works](../introduction/how-it-works.md#aggregators).

</details>

<details>

<summary>How often do price feeds update in the Aggregator?</summary>

Stork Aggregators are blazingly fast. Though configurable through the [COS](../introduction/products.md#composite-oracle-service), Aggregators typically update every 500ms at the slowest, and on the order of sub 10ms at the fastest during periods of high volatility. For more information, see [How It Works.](../introduction/how-it-works.md#aggregators)&#x20;

</details>

<details>

<summary>How is Stork decentralized?</summary>

Stork uses a decentralized network of independent publishers that contribute data to Stork. This enables decentralization and protects against pitfalls of a single point of failure.&#x20;

Stork also supports direct access to publisher data in the unlikely event of downtime. For details, please reach out to [sales@stork.network](mailto:sales@stork.network). &#x20;

For more information, see [How It Works](../introduction/how-it-works.md#publishers).

</details>
