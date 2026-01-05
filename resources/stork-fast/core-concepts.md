---
description: Understanding  Fast-specific primitives and advantages.
icon: reflect-both
---

# Core Concepts

Built with backwards compatibility in mind, Fast reuses a number of concepts from [Stork Core.](../../introduction/core-concepts.md) Critically, Fast reuses [Temporal Numeric Values](../../introduction/core-concepts.md#temporal-numeric-values), allowing for existing code integrations - including on-chain contracts - to largely reuse existing code if switching from Core to Fast. The [Push vs Pull Oracles](../../introduction/core-concepts.md#docs-internal-guid-4b312e7b-7fff-1147-c04b-bbaadec1a82a), [Data Aggregation,](../../introduction/core-concepts.md#data-aggregation) and [Prices](../../introduction/core-concepts.md#prices) sections are also all largely relevant to Fast.

## Asset IDs

Asset IDs in Fast are 16-bit unsigned integers acting as an ID for a data feed. They are used throughout Fast to identify data. Bounded size numeric IDs were chosen over text or hex-encoded hashed IDs for efficiency. Due to the extreme frequencies Fast operates at, minimizing data footprint is critical for over-the-wire efficiency, both to and from Fast and to and from any downstream recipients (e.g. an RPC node when submitting data on-chain). Reducing data size is also critical for maximizing memory, computational, and on-chain gas efficiency when working with Fast data.&#x20;

The 16-bit unsigned integer provides an ID space of 0-65536, inclusive. Example Asset IDs are:

* BTC/USD: 1
* JPY/USD: 12001

These are hypothetical examples, For a full list of asset IDs and corresponding encodings, please reach out to Stork.

## Taxonomies

Designed for both general use and bespoke applications, Fast uses Taxonomy to logically separate Asset ID spaces. A Taxonomy is a mapping of assets to Asset IDs (see above) uniquely identified by a numerical Taxonomy ID.  Fast Taxonomy IDs, like Asset IDs, are 16-bit unsigned integers.

Ultimately, in Fast, an asset can be uniquely identified by the (Taxonomy ID, Asset ID) pair. Any given Asset ID may correspond to a different asset on any given Taxonomy,  and thus both are necessary to globally identify an asset within Fast.&#x20;

The benefit of the Taxonomy system is to enable flexible and bespoke use-cases. While 65536 unique Asset IDs is a large space, and has room to spare for traditional asset classes (crypto, equities, RWA, etc..), there are instances where having distinct Asset ID spaces can provide additional flexibility.

## Millisecond Latency&#x20;

Fast is fast. Really Fast. The latency between data entering fast, undergoing aggregation, and being ready for delivery to a subscriber is on the order of 1 millisecond. Even at slower frequencies, when requested by the subscriber, the latency through Fast remains unchanged. Fast continues to aggregate new data to ensure any data delivered has the same latency guarantees regardless of frequency or channel.

## Message Types and Signatures <a href="#docs-internal-guid-8ba37e95-7fff-6e92-1819-f1b365a60d1a" id="docs-internal-guid-8ba37e95-7fff-6e92-1819-f1b365a60d1a"></a>

Fast is capable of packaging the same data in a number of different ways. These are called message types and define the structure and contents of the message. Messages can include fields like:

* signatures for verifiability
* bit-packed payloads for maximum on-chain efficiency
* pricing data in a human-readable message

Message type is determined by the subscriber at subscribe time. This system allows for flexibility when interacting with Fast and ensures subscribers get data as it suits them.

For currently available Message Types, see the Websocket API Documentation.

## Subscription Channels

For data delivery Fast uses websockets and offers multiple channels of two primary types:

* &#x20;Fixed
* &#x20;Real Time

Fixed channels are channels in which updates are pushed out by Fast at fixed intervals. Fixed channels are flexible, and can range down from the millisecond level up to seconds, depending on subscriber needs. Fixed channels are simply named as the period of updates, so the channel for receiving a message every 10ms is called "10ms".

The real time channel, designated "real\_time", is a major efficiency gain in Fast where messages are only sent when new prices are available. Critically, latency guarantees for real time are identical to fixed, meaning real time is strictly more efficient than fixed. Rather than receiving the latest values at a fast fixed interval, where many updates may have duplicated data due to no upstream price movement, real time allows for only receiving new data when it's relevant, without adding any lag time.

<br>
