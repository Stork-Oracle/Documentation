---
description: Programming API reference for the Stork Fuel contract.
icon: f
---

# Fuel

## SDK

Fuel contracts can program against [Stork's contract](https://github.com/Stork-Oracle/stork-external/tree/main/chains/fuel/contracts) using the stork\_sway\_sdk rust crate available on [forc.pub](https://forc.pub/package/stork_sway_sdk). This SDK provides useful methods and structs for interacting with the stork contract. The Stork contract and SDK are built with [Sway](https://docs.fuel.network/docs/sway/).

## Installation

{% tabs %}
{% tab title="Sway" %}
After setting up your sway project, add the stork\_sway\_sdk to your project dependencies by adding the following line to the `[dependencies]` section of the programs `Forc.toml`

```toml
// Forc.toml
[dependencies]
stork_sway_sdk = "0.0.5"
```

or the following command:

```bash
forc add stork_sway_sdk@0.0.5
```

You can now import the stork sdk's interfaces with:

```rust
// your_contract.sw
use stork_sway_sdk::{<...>}
```
{% endtab %}
{% endtabs %}

## Methods

These methods are all defined in the contract abi, which is defined in the `interface` module of the stork\_sway\_sdk.

### Update Temporal Numeric Values V1

```rust
#[storage(read, write), payable]
fn update_temporal_numeric_values_v1(
    // vector of input data
    update_data: Vec<TemporalNumericValueInput>
)
```

#### Description

Updates multiple temporal numeric values by verifying signatures and ensuring freshness.

#### Parameters

* `update_data`: Vector of `TemporalNumericValueInput` structs containing feeding updates.

#### Behavior

* Verifies the signature of each feed update using the stored EVM public key.
* Updates the feed value if the signature is valid and the value is more fresh then the current state.
* Requires sufficient fee based on the number of updates (in the base asset).

#### Errors

* `InvalidSignature`: If any feed update fails signature verification.
* `NoFreshUpdate`: If none of the provided updates are fresher than current values.
* `IncorrectFeeAsset`: If the payed asset is not the base asset of the chain.
* `InsufficientFee`: If the provided fee is less than the required amount.

### Get Temporal Numeric Value Unchecked V1

```rust
#[storage(read)]
fn get_temporal_numeric_value_unchecked_v1(
    // encoded asset id
    id: b256
) -> TemporalNumericValue;
```

#### Description

Retrieves the latest temporal numeric value for the specified asset ID without checking its freshness.

#### Parameters

* `id`: The encoded asset id of the feed.

#### Returns

* `TemporalNumericValue` : The latest value for the relevant feed.

#### Errors

* `FeedNotFound`: If no value exists for the given asset ID.

### Get Update Fee V1

```rust
#[storage(read)]
fn get_update_fee_v1(
    // vector of input data
    update_data: Vec<TemporalNumericValueInput>
) -> u64;
```

#### Description

Calculates the total fee required for the given updates.

#### Parameters

* `update_data`: Array of 'TemporalNumericValueInput\` structs representing updates.

#### Returns

* `u64`: The total fee required for the updates.

### Version

```rust
fn version() -> String;
```

#### Description

Retrieves the current version of the contract.

#### Returns&#x20;

* `String`: The version string (e.g. "1.0.0")

## Examples

Example usage of the Stork Fuel contract and sdk can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/chains/fuel/examples).
