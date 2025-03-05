---
icon: reflect-both
description: >-
  Understanding oracle models, Stork-specific data primitives, and Stork's
  advantages.
---

# Core Concepts

## Push vs Pull Oracles <a href="#docs-internal-guid-4b312e7b-7fff-1147-c04b-bbaadec1a82a" id="docs-internal-guid-4b312e7b-7fff-1147-c04b-bbaadec1a82a"></a>

Oracles are essential for providing on-chain applications access to off-chain data. Push and pull are the two primary oracle models in use across blockchains. From price and derivatives feeds for DeFi, to weather data for insurance, or outcomes of real-world events for prediction markets, data from oracles is critical to the existence of many of the most popular decentralized apps.

Stork's implementation of the pull oracle is exemplified by the following attributes:

* Update Frequency — Pull oracles allow for updates as often as needed.
* Latency — Because the update can happen whenever needed, the price age or latency is reduced from minutes to milliseconds.
* Efficiency — Without the need to continuously push unused data, pull oracles achieve much better gas (cost) efficiency.
* Ease of use — Whereas push oracles introduce reliance on the oracle provider to get data on-chain, pull oracles allow anyone to put data on chain without having to rely on the provider.

### Push Oracles

The older of the two oracle models, push oracles operate by periodically pushing data onto the blockchain in regular intervals, often called 'heartbeats'. This data is submitted to the oracle contract on-chain where it is then stored for use in other smart contracts. This method ensures that a continuous and predictable flow of data is present on-chain, however offers little in the way of flexibility. Furthermore, they are considered inefficient due to the inevitable periods of time where data is being pushed on-chain but going unused between updates. The heartbeat of data in a traditional push oracle also does not allow for scaling the frequency of updates to the demand of many real time applications, resulting in data that can become too stale to be useful. Due to the gas fees associated with putting data on-chain, push oracles often operate on very slow heartbeats (ex: 1-2 updates per hour) to conserve gas fees and remain economically viable.

### Pull Oracles

Originally called a hybrid oracle, Stork created the pull oracle model as an answer to the issues with push oracles. Pull oracles operate by only putting data on-chain exactly when it’s needed. In contrast to the heartbeat of data being pushed on-chain by the oracle operator in push oracles, Stork’s pull oracle operates by allowing subscribers to listen to signed data updates in an off-chain application, and post those updates to the official Stork contract whenever they need to. Anyone is able to post updates to the Stork contract because Stork data updates are verified for both signatures and recency before being stored. Gas costs are also minimized on a per application basis, as the onus of placing data on-chain can be shared. Upon updating the Stork contract, the relevant application logic can then be called. This logic flow can be achieved within a single transaction, meaning the on-chain data is updated in the same transaction as it's consumed in your smart-contract.

## Temporal Numeric Values

The prominent use-case for oracles on blockchains is for price feeds. Oracles facilitate the ability to get the price of a cryptocurrency, real-world asset, or any other asset or derivative for use in DeFi applications on chain. In some instances, there have been application-specific custom built oracles for more niche purposes, like putting outcomes of real-world events on-chain for prediction markets, or getting verifiable randomness on-chain. Stork takes these common use cases and merges them with the generic "Temporal Numeric Value" primitive. This primitive contains:

* A UNIX timestamp with nanosecond precision
* A signed integer, multiplied by `10^18` for 18 decimal places of precision

Out of the box, Stork supports continuous real-time, ephemeral, or one time use data on-chain, so long as it can be represented as a timestamped number.

Stork supports price feeds for [all your favorite assets](../resources/asset-id-registry.md), but can also be used for unique cases, ex: putting your fitness data on-chain, or virality metrics from a social media platform. The data you can put on-chain with Stork is only limited by what you can think of.

## Sub-Second Latency

One of Stork’s key differentiators in the oracle landscape is its ultra-low latency. This latency is sub-second, and depending on the specific application often closer to just several 10ths of a second. This means when an update lands on-chain in the Stork contract for applications to consume, it’s close to as fresh as it could possibly be without eliminating chain-latency. Not only are Stork price updates exceptionally fresh on-chain, but Stork’s aggregators also have fresh data at minimum every 500ms. This allows applications using Stork data to ensure they always have the most recent data.

## Signatures

Signatures are one of the core cryptographic primitives used in computing, from the traditional internet to crypto. Using asymmetric cryptography, signatures allow one party to "sign" a message by applying a mathematical (encryption) function to it using a secret key as an input. The message can then be sent to anyone, who can verify the sender by checking the signature against the supposed sender's public key (a number that the sender lets everyone know). The mathematical relationship between the public and private keys is such that if and only if a message was signed with the matching private key, you can verify it with the public key.

Stork utilizes signatures to make assurances in a number of places. When sending data to the aggregators, publishers sign their messages first. After receiving and aggregating the publisher signed data, the Stork aggregator then signs the aggregated price to be consumed by subscribers. These signatures are then verified in Stork contracts on-chain to make the following assurances:

1. The original publisher data is coming from the correct publishers.
2. The Stork aggregated data is coming from a Stork aggregator.
3. The Stork aggregator is using the aggregation method asserted.

Stork utilizes ECDSA with `secp256k1` keypairs for signing, which is the same elliptic curve cryptography used by Ethereum. More information on Stork’s use of signatures can be found in [How It Works](how-it-works.md#verifiability).

## Data Aggregation

Data aggregation is the process of collecting multiple discrete data streams representing the same asset and combining them deterministically to output a consolidated distinct output. Stork's data aggregation is resilient to failures of a single source.

Using just one data source leaves the consumer of that data vulnerable to:

* Interruptions in data flow due to unforeseen (or planned) issues in the publisher
* Inconsistencies and inaccuracies due to the publishers specific data collection methods
* Malicious manipulation of critical data, whether by the publisher themselves or a hostile actor who's gained access to the publishers systems

By using a network of independent decentralized data publishers and aggregating their feeds - much like using a network of independent nodes in a blockchain - the consumer of the data is protected against the pitfalls associated with a single source of truth and single point of failure.

## Asset IDs

Asset IDs are names for specific feeds of data. They are used throughout Stork to identify data, and are often seen in both plain-text and encoded form. An encoded asset ID is just the `keccak256` hash of the plaintext asset ID, and is commonly used to identify an asset on-chain. For example, the BTC/USD price pair would be identified as:

* Asset ID: `BTCUSD`
* Encoded Asset ID: `keccak256("BTCUSD") => 0x7404e3d104ea7841c3d9e6fd20adfe99b4ad586bc08d8f3bd3afef894cf184de`

For a full list of asset IDs and corresponding encodings, please see the[ Asset ID Registry](https://docs.stork.network/~/changes/suDzkkK15gqdfmjDKr9z/resources/asset-id-registry).

## Prices

### Spot Prices

The spot price of an asset is the current price in the marketplace.

An example of this calculation (used in Storks in-house publisher) is:

1. Take the order book midpoint price of the asset from all of the highest volume exchanges
2. Calculate the median of those prices

### Perpetual Future Mark Price

The perpetual future mark price of an asset is the underlying mark price of the perp contract. This, like the spot price of an asset, is an aggregate of from the publisher calculated prices.

An example of this calculation (used in Storks in-house publisher) is:

$$
Mark Price_{t} = \frac{median(Perp Price_{0t},Perp Price_{1t},...,Perp Price_{nt})}{USDT/USD_{t}}
$$

where:

* PerpPrice(it): Price of asset on exchange i at time t

and:

$$
USDT/USD_{t} = median(SpotPrice_{0t},SpotPrice_{1t},...,SpotPrice_{nt})
$$

where:

* SpotPrice(it): Price of USDT-USD exchange i at time t

### EMA Garman-Klass Volatility

[Garman-Klass](https://portfolioslab.com/tools/garman-klass) is a common estimator of price volatility based on OHLC prices, improving on the basic volatility by considering extreme prices within a period instead of just the start and end of a period.

Traditionally Garman-Klass volatility is computed over a fixed period and gives every period an equal weight. Since Stork deals with real time data we'd prefer to weigh recent volatility more heavily. We use the Garman-Klass formula's computation for each OHLC period, but rather than taking an average over a fixed number of periods, we apply an exponential moving average so that we can quickly report sudden increases in volatility.

We compute the EMA volatility for period n+1 given the EMA volatility for period n, the open, high, low and close prices for period n, and a fixed decay parameter lambda using the formula:

$$
\left(\hat\sigma^{GK}_{n+1}\right)^2 = \lambda \left[\frac{1}{2}\log\left(\frac{H_n}{L_n}\right)^2-(\log(4)-1) \log \left( \frac{C_n}{O_n}\right)^2\right] + (1-\lambda)\left(\hat\sigma^{GK}_{n}\right)^2
$$

EMA Garman-Klass Volatility feed names are suffixed with `_VGK`.
