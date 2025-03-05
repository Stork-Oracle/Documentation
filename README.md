---
icon: bird
description: Welcome to Stork!
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

# Welcome to Stork

Stork is an oracle protocol that enables ultra low latency connections between data providers and both on and off-chain applications. The most common use-case for Stork is pulling and consuming market data in the form of real time price feeds for DeFi.

The core technical principles of Stork are:

* Modularity
* Low latency / high throughput
* Cost efficiency
* Arbitrary data support
* Transparency, verifiability, and security

Stork is implemented as a [pull oracle](introduction/core-concepts.md#docs-internal-guid-4b312e7b-7fff-1147-c04b-bbaadec1a82a). Stork continuously aggregates, verifies, and audits data from trusted publishers, and makes that aggregated data available at sub-second latency and frequency. This data can then be pulled into any on or off-chain application as often as needed.

Stork was created with the principle of trustlessness in mind. As such, all data inputs and outputs to Stork are cryptographically verifiable. This includes the underlying publisher data as well as Stork’s aggregated results. Stork currently supports 370+ assets on 60+ chains, including[ EVM](resources/contract-addresses/evm.md) chains, [Solana](resources/contract-addresses/solana.md), [Sui](resources/contract-addresses/sui.md), [Aptos](resources/contract-addresses/aptos.md), and [more](resources/contract-addresses/), and is easily deployed on any other chain not yet supported.&#x20;

Chain deployments and asset additions are available upon request. For a full list of supported chains, see the [Contract Addresses](resources/contract-addresses/) page. For a full list of supported assets, see the [Asset ID Registry](resources/asset-id-registry.md) page.

To learn more about how Stork works, visit [Core Concepts](introduction/core-concepts.md) and [How It Works](introduction/how-it-works.md).

{% hint style="info" %}
Interested? Contact Stork Labs to determine appropriate feeds that meet your requirements.  [sales@stork.network](mailto:sales@stork.network) or [Twitter DMs](https://twitter.com/StorkOracle) open.
{% endhint %}

