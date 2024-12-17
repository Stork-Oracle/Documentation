---
description: Adapters for other standard oracle interfaces for Stork
icon: plug
---

# Adapters

For convenience, Stork has adapter contracts to make it easy to interact with Stork on chain if a contract is already using another oracle and wants to switch or use Stork in parallel.&#x20;

## EVM

### Chainlink

Stork provides a Chainlink adapter SDK that exposes interface functions for interacting with Stork's contract in the same way you would with Chainlink. This contract can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/contracts/stork_chainlink_adapter). Example usage of this contract can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/examples/stork_chainlink_adapter).

### Pyth

Stork provides a Pyth adapter SDK that exposes interface functions for interacting with Stork's in the same way you would with Pyth. This contract can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/contracts/stork_pyth_adapter). Example usage of this contract can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/examples/stork_pyth_adapter).



{% hint style="info" %}
Looking for an adapter for your current oracle and/or chain? Contact Stork Labs.  [sales@stork.network](mailto:sales@stork.network) or [Twitter DMs](https://twitter.com/StorkOracle) open.
{% endhint %}
