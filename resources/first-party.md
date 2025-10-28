---
description: Directly push self-sourced data on-chain with Stork tools.
icon: arrow-turn-left-up
---

# First Party

## What Is It?

Want to run everything in-house? Stork First Party allows anyone to push custom data to a First Party Contract by running Stork tools themselves. With no code and minimal configuration, anyone can easily sign and push their own data on-chain. From there, it becomes publicly readable and verifiable by anyone.

## How It Works

Stork First Party ingests [temporal numeric](../introduction/core-concepts.md#temporal-numeric-values) data — such as prices, metrics, or analytics — and pushes it on-chain. Each data point is [signed](../introduction/core-concepts.md#signatures), validated, batched, and stored immutably for downstream consumption. What differentiates First Party from our other offerings is independence. Users can run Stork tools themselves to push data directly on-chain, without relying on Stork Network's live infrastructure.

### Under the Hood

To run First Party Stork, the user must provide their own custom data feed. The user then runs two distinct processes:&#x20;

1. Publisher Agent
   1. Ingests data from the provided custom data stream via WebSocket
   2. Signs each message with a private key
   3. Forwards signed messages to local First Party Pusher sibling process
2. First Party Pusher
   1. Receives signed updates from Publisher Agent via WebSocket
   2. Pushes signed updates to the configured chain based on customizable staleness and delta thresholds

Finally, the FirstPartyStork Contract verifies the signature, checks if the Publisher's public key is authorized, and stores the temporal numeric values. These values are keyed by the publisher's public key and the Keccak-256 hash of the asset name.

## Get Started

### Running Stork First Party

Stork First Party is an application that bundles the [Publisher Agent](https://github.com/Stork-Oracle/stork-external/blob/main/apps/publisher_agent/README.md) and the First Party Pusher.&#x20;

Configuration is simple:

* `publisher-config.json`: defines the data source port and where signed data is forwarded
* `pusher-asset-config.yaml`: defines expected assets-publisher pairs and triggers (intervals, % changes)
* `.env`: defines keys, oracle identifiers, and blockchain connection details

&#x20;An `.env.example` is included for reference.

It is recommended to run Stork First Party via Docker. All components are split into separate services. Docker profiles are included for convenience in the `docker-compose.yml`:

* `first-party`: runs a Publisher and Pusher
* `local`: runs a toy Data Provider, Publisher, Pusher, and local Contract

### Using Stork First Party Data

Stork provides a [Solidity SDK](https://www.npmjs.com/package/@storknetwork/first-party-stork-evm-sdk) for working directly with First Party Contracts. Access to the on-chain data will involve calling `getLatestTemporalNumericValue` with the appropriate publisher and asset information.

_Full chain support documentation coming soon._

_Expanded contract interaction guide coming soon._

{% hint style="info" %}
Want to get started with First Party? Push data to a new chain? Learn more?

Email us at [sales@stork.network](mailto:sales@stork.network) or DM us on [X (formerly Twitter)](https://x.com/StorkOracle)
{% endhint %}

