---
description: Various methods for putting off-chain Stork signed data on-chain.
icon: grid-dividers
---

# Putting Data On-Chain

In order for Stork signed data feeds to be usable in on-chain smart contracts, the data must be written to the [Stork contract](../introduction/how-it-works.md#on-chain-contracts) on the relevant blockchain. There are two primary methods to achieve this:

* Running the open-source Chain Pusher
* Updating per-interaction in your dApp client

### Running the Chain Pusher

The Chain Pusher is an application that handles the communication with an Aggregator and the on-chain stork contract automatically. Using a simple [asset config](../api-reference/chain-pusher-configs/asset-config-yaml.md) that defines which assets to write, and the triggers for writing them (time intervals, price change %s), the Chain Pusher allows a continuous stream of updates to be put on-chain with a single command. The Chain Pusher, and instructions for getting it running, can be found in the[ stork-external github repo](https://github.com/Stork-Oracle/stork-external/blob/main/apps/chain_pusher/README.md).

It's important to note that when using the Chain Pusher, the Subscriber is responsible for the gas fees associated with putting Stork data on-chain. These gas fees are split between all Subscribers running the Chain Pusher for the same asset based on percentage of update volume. Depending on the popularity of the asset(s), gas fees may vary.

### Updating on a Per-Interaction Basis

The second method of using Stork data on-chain is baking the data feed update call into your smart contracts client interface. This is the most efficient usage of a [pull oracle](../introduction/core-concepts.md#pull-oracles), and follows this pattern:

1. User Interacts with your dApp front-end (client) that will call a smart-contract method that consumes Stork data.
2. The client hits the Stork [REST API](../api-reference/rest-api.md) for the latest update for the relevant data, or uses most recent data from the [websocket](../api-reference/websocket-api/).
3. The client crafts a transaction that first includes an instruction to update the value on the Stork contract, then an instruction to interact with your smart-contracts method that will consume the price update. (for information on writing data to the Stork contract, see the [Contract APIs](../api-reference/contract-apis/))

Because of atomic and ordered transaction processing, which is the standard for most blockchain architectures, the price the dApp's smart-contract uses is empirically as fresh as it possibly could be. If something is wrong with the price update (an invalid signature or contents), the Stork contract will catch this and refuse to update the price and the transaction will fail. If for some reason a newer update already exists on-chain (ex: a user tries to maliciously inject an old but validly signed price), the Stork contract will reject the update and the transaction will proceed with the most recent price.

In this model, the user interacting with your dApp is responsible for paying the gas fees associated with putting Stork data on-chain.
