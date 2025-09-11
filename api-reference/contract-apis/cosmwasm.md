---
description: Programming API reference for the Stork CosmWasm contract.
icon: solar-system
---

# CosmWasm

## SDK

CosmWasm contracts can integrate with the [Stork contract](https://github.com/Stork-Oracle/stork-external/tree/main/chains/cosmwasm/contracts) using the stork-cw rust crate available on [crates.io](https://crates.io/crates/stork-cw). This crate contains the full contract code, which can be used as an SDK by enabling the `library` feature. For more documentation, please also see the [docs.rs page](https://docs.rs/stork-cw/0.1.1/stork_cw/). The Stork contract / SDK are built on top of [Sylvia](https://docs.cosmwasm.com/sylvia). &#x20;

## Installation

{% tabs %}
{% tab title="Rust" %}
After setting up your CosmWasm project, add the stork-cw crate to your project dependencies by adding the following line to the `[dependencies]` section of the programs `Cargo.toml`:&#x20;

```toml
// Cargo.toml
[dependencies]
stork-cw = { version = ">0.1.2", features = ["library"]
```

or the following command:

```bash
cargo add stork-cw --features library
```

You can now import the stork-cw's interfaces with:

```rust
// contract.rs
use stork_cw::{<...>}
```
{% endtab %}
{% endtabs %}

## Query Messages

```rust
pub enum QueryMsg {
    GetLatestCanonicalTemporalNumericValueUnchecked {
        id: EncodedAssetId,
    },
    GetSingleUpdateFee {},
    GetStorkEvmPublicKey {},
    GetOwner {},
}
```

### Get Latest Canonical Temporal Numeric Value Unchecked

#### Description

Retrieves the latest value for a specified asset without additional checks.

#### Parameters

* `id: EncodedAssetId`: The [encoded asset ID](../../introduction/core-concepts.md#asset-ids) of the feed to read.

#### Response

```rust
pub struct GetTemporalNumericValueResponse {
    pub temporal_numeric_value: TemporalNumericValue,
}
```

Contains a `TemporalNumericValue` instance representing the latest timestamped value for the relevant asset.

#### Errors

* `StorkError::FeedNotFound` : If the specified feed does not exist.

### Get Single Update Fee

#### Description

Retrieves the fee required to update a single feed.

#### Response

```rust
pub struct GetSingleUpdateFeeResponse {
    pub fee: Coin,
}
```

Contains a `Coin` instance representing the amount and denomination of the fee.

### Get Stork EVM Public Key

#### Description

Retrieves the stored EVM public key used for message verification.

#### Response

```rust
pub struct GetStorkEvmPublicKeyResponse {
    pub stork_evm_public_key: EvmPubkey,
}
```

Contains an `EvmPubkey`.

## Get Owner

#### Description

Retrieves the stored address of the owner of the Stork contract.

#### Response

```rust
pub struct GetOwnerResponse {
    pub owner: Addr,
}
```

Contains the `Addr` of the owner.

## Execution Messages

```rust
pub enum ExecMsg {
        UpdateTemporalNumericValuesEvm { update_data: Vec<UpdateData> },
        // admin functions ..
    }
```

### Update Temporal Numeric Values EVM

Update the latest value of one or more assets based on the provided update values.

#### Parameters

* `update_data: Vec<UpdateData>` : A vector of updates, where each update contains:
  * `id: EncodedAssetId` : Encoded asset ID (byte array) of the asset to update
  * `temporal_numeric_value: TemporalNumericValue` : Struct containing the value and timestamp of the update.
  * `publisher_merkle_root: [u8; 32]` : The publisher's Merkle root.
  * `value_compute_alg_hash: [u8; 32]`:  Hash of the compute algorithm.
  * `r: [u8; 32]` : R component of the signature.
  * `s: [u8; 32]` : S component of the signature.
  * `v: u8`: V component of the signature.

#### Behavior&#x20;

* Verifies the update data's signature using the Stork EVM public key stored in the contracts state.
* Verifies that the update is more recent than the data currently in the feed.
* If the signature is invalid, the function errors with `StorkError::InvalidSignature`.
* If the update is not recent, the function does not error but does no update the feed object.
* If both verification pass, updates the `TemporalNumericValue` for the asset and emits a `temporal_numeric_value_update`  event.

#### Errors

* `StorkError::InsufficientFunds`: If an insufficient fee is included with the message for the number of updates.
* `StorkError::InvalidSignature`: If the signature verification fails.

## Examples

Example usage of the Stork CosmWasm contract in both Sylvia and CosmWasm Core contracts can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/chains/cosmwasm/examples).
