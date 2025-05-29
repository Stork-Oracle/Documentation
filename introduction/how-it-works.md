---
description: >-
  Understanding the layers of Stork's core architecture and how they work
  together.
icon: arrows-spin
---

# How It Works

## Architecture <a href="#docs-internal-guid-847a2b18-7fff-81d7-ee61-fee4a32d94d3" id="docs-internal-guid-847a2b18-7fff-81d7-ee61-fee4a32d94d3"></a>

Stork can be cleanly divided into 4 core layers:

* [Publishers](how-it-works.md#publishers)
* [Subscribers](how-it-works.md#subscribers)
* [Aggregators](how-it-works.md#aggregators)
* [On-Chain Contracts](how-it-works.md#on-chain-contracts)

<div data-full-width="false"><figure><img src="../.gitbook/assets/Architecture for docs.png" alt=""><figcaption><p>Stork Architecture Diagram</p></figcaption></figure></div>

These layers all work together to make up the core architecture of Stork. At a high level, the interaction between these layers is as follows:

* Publishers provide signed streams of data via websocket to Aggregators.
* Aggregators listen to streams of Publisher data via websocket, aggregate and sign those streams, then push the aggregated data streams to Subscribers.
* Subscribers consume streams of data via websocket (or REST requests) from Aggregators based on their needs.
* Subscribers can then do whatever they want with the aggregated data, but most commonly use this data in smart-contracts by sending it to the Stork oracle contract on their chain of choice whenever necessary, or leverage it off-chain in a decentralized exchange.
* Signatures are verified in the Aggregator, in the on-chain contracts, and optionally by the subscribers.

Continue reading for more specifics on how these components work.

### Publishers

Where the data starts its journey, Publishers are decentralized independent firms and organizations that contribute data to Stork. Most often, Publishers are organizations that already have data that would be useful on-chain, and choose to contribute that data to Stork as a secondary outlet. Some examples of publishers are:

* High Frequency Trading firms
* Decentralized and Centralized Exchanges
* Predictions markets

Publishers make their data available to Aggregators, and by extension Subscribers, by running the[ Stork Publisher Agent](https://github.com/Stork-Oracle/stork-external/blob/main/apps/docs/publisher_agent.md), an open-source application that can easily be deployed via a pre-built docker container. The publisher agent also handles signing and sending the data to Aggregators.

Have data you want to contribute? Check out[ Becoming a Publisher](../getting-started/becoming-a-publisher.md) for more information.

### Aggregators

If Stork was a sandwich, Aggregators would be the meat. This is where the heavy lifting happens, and data is consolidated into its final form to be sent along its way. Aggregators simply listen to data from relevant Publishers, aggregate this data using an aggregation function, sign the data (proving not only the source, but also the aggregation method), and then push data containing the aggregate, its signature, as well as all of the original publisher data and their signatures, to subscribers via websocket. They also make this data available via a REST endpoint.

For interacting with Aggregator APIs, see the[ websocket API](../api-reference/websocket-api/) and[ REST API](../api-reference/rest-api.md) docs

Stork Aggregators can use one of several aggregation functions. The available functions are:

* Median - The median of the constituent Publisher data.
* Average - The average of the constituent Publisher data.
* Weighted Average - A custom weighted average of the constituent Publisher data.

The most commonly used aggregation method is median, which provides a good balance of simplicity, speed, and protections against subsets of errant Publishers.

Aggregators are run by Stork Labs in redundant sets. They are highly configurable to the specific needs of individual applications. Though configurable, Aggregators typically provide fresh data every 500ms, or whenever the aggregate data moves by 0.1%, whichever happens first. This achieves a blazingly fast sub-second update frequency.

### Subscribers

Subscribers are the consumers in the system. After selecting a suitable Aggregator with a specific method and Publishers of the necessary data feeds, the Subscriber listens to the Aggregator's [websocket](../api-reference/websocket-api/) to continuously receive the latest data as soon as it's available. The latest data can also be retrieved in one-off calls to the Aggregator's [REST API](../api-reference/rest-api.md).

What the Subscriber does with this data is up to the Subscriber, however the common use-cases can be broadly categorized into two major categories: on-chain and off-chain.

#### **Off-Chain**

While oracles are typically thought of as being used for putting data on-chain, there is no rule that the data feeds must ultimately end up on a blockchain. Off-chain applications can benefit from low-latency, high-frequency, and high-accuracy data feeds as much as any smart-contract. Some examples of off-chain uses are:

* Decentralized exchanges
* Price analytics
* High frequency trading execution platforms
* Generation of derivatives to be repackaged in the form of a new Publisher on Stork

#### **On-Chain**

A common use of Stork data by a Subscriber is to put the data on-chain for use in smart contracts. Commonly, these are lending protocols, DEXes, or prediction markets.

To use data on-chain, there are two strategies.

* Running the open-source Chain Pusher
* Updating per-interaction in your dApp client

For more information on using these strategies to put data on-chain, please see [Putting Data On-Chain.](../getting-started/putting-data-on-chain.md)

Interested in becoming a subscriber? Check out [Becoming a Subscriber](../getting-started/becoming-a-subscriber.md) for more info.

### On-Chain Contracts

The official Stork contracts are the on-chain components of Stork. These contracts are responsible for the following:

* Maintaining a registry of [temporal numeric value](core-concepts.md#temporal-numeric-values) (TNV) feeds that associate an [encoded asset ID](core-concepts.md#asset-ids) with the most recent data for that asset.
* Accepting and verifying TNV updates for recency and signature validity.
* Updating relevant feeds upon submission and verification of a posted update.
* Providing public interface functions to easily read the latest value for a feed from another smart contract.

For more information on Stork’s smart-contracts, see the [API Reference](../api-reference/contract-apis/), the[ stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/contracts), or the [Contract Addresses](../resources/contract-addresses/) page.

## Verifiability

Stork is built with the principles of trustlessness and decentralization enshrined, and as such, makes thorough use of cryptographic primitives throughout the system.

Stork follows the lead of Ethereum and Bitcoin in using `secp256k1` keypairs with ECDSA asymmetric signatures. Stork and its publishers sign messages using an implementation of the[ EIP-712](https://eips.ethereum.org/EIPS/eip-712) signing spec, and use official EVM keypairs for this purpose. This offers several advantages, including leveraging the extensive real world testing this method has gone through, as well as the near universal support by blockchain VMs, even in cases where it is not the primary curve or signature method on that chain.

Signatures in Stork are included in the following places:

1. [Publishers](how-it-works.md#publishers) sign their data updates using their private key
2. [Aggregators](how-it-works.md#aggregators) sign their data updates using their private key

It's important to remember that Aggregator signatures are signatures for the entire update, including the:

* Temporal Numeric Value (Data point in the form of timestamp + number)
* Aggregation Function
* Constituent Publisher data and their signatures

These signatures allow cryptographic verification in the following instances:

1. Aggregators verify the signatures of their constituent Publishers data to determine which updates to verify, maintaining trustlessness while optimizing for throughput
2. The [on-chain contracts](how-it-works.md#on-chain-contracts) verify the Aggregators signatures to ensure only valid updates can ever be posted on-chain
3. [Subscribers](how-it-works.md#subscribers) can optionally verify both the Aggregators and Publishers signatures before utilizing the data.

This series of signatures and verifications enables end-to-end trustlessness in Stork intrinsically.

## Scalability

Stork has been designed to scale virtually infinitely. Due to Stork’s architecture, and the ability to segregate aggregation responsibility between multiple Aggregators, Stork’s latency does not meaningfully change depending on the number of assets. Scaling of your application is not and will never be limited by Stork.

## Extensibility

As touched upon in the [TNV section of Core Concepts](core-concepts.md#temporal-numeric-values), one of Stork’s unique traits is its Temporal Numeric Value primitive. This is primitive that includes a (unix) timestamp and a number. Commonly, this would be an asset price and timestamp of aggregation. It can also represent any sort of timestamped data, allowing for much greater extensibility than other oracles.

The specific data you want your app to use on-chain is not prescribed by Stork. Everything from real world prediction market data, personal data like fitness metrics, or social media metrics, and other first party data can and should go on-chain with Stork.
