---
description: Programming API reference for the Stork Aptos contract.
icon: circle-waveform-lines
---

# Aptos

## SDK

Aptos contracts can integrate with the [Stork contract](https://github.com/Stork-Oracle/stork-external/tree/main/chains/aptos/contracts) including it as a project dependency.

## Installation

{% tabs %}
{% tab title="Move" %}
After setting up your Aptos Move project, add the Stork contract to your project dependencies by adding the following lines to your projects `Move.toml` :

```toml
// Move.toml
[addresses]
// other addresses ...
stork = "<stork-address>"

[dependencies.stork]
git = "https://github.com/stork-oracle/stork-external.git"
rev = "main"
subdir = "chains/aptos/contracts"
```

For the official Stork contract addresses, see [Aptos Contract Addresses](../../resources/contract-addresses/aptos.md).\
\
You can now import the Stork interfaces with:

```rust
// your_module.move
use stork::{<...>}
```
{% endtab %}
{% endtabs %}

## stork::stork Methods

### Update Single Temporal Numeric Value EVM

```rust
public entry fun update_single_temporal_numeric_value_evm(
        // signer of the transaction to pay the fee
        signer: &signer,
        // asset id
        asset_id: vector<u8>,
        // temporal numeric value timestamp ns
        temporal_numeric_value_timestamp_ns: u64,
        // temporal numeric value magnitude
        temporal_numeric_value_magnitude: u128,
        // temporal numeric value negative
        temporal_numeric_value_negative: bool,
        // publisher's merkle root
        publisher_merkle_root: vector<u8>,
        // value compute algorithm hash
        value_compute_alg_hash: vector<u8>,
        // signature r
        r: vector<u8>,
        // signature s
        s: vector<u8>,
        // signature v
        v: u8,
    ) 
```

#### Description

Updates the latest value in the relevant feed object based on the provided update values.

#### Parameters

* `signer: &signer`: A reference to the signer of the transaction, automatically provided by the MoveVM.
* `asset_id: vector<u8>`: Encoded asset ID as a byte vector for the update .
* `temporal_numeric_value_timestamp_ns: u64`: Timestamp of the temporal numeric value.
* `temporal_numeric_value_magnitude: u128`: The magnitude of the numeric value.
* `temporal_numeric_value_negative: bool`: Indicates whether the value is negative.
* `publisher_merkle_root: vector<u8>`: The publisher's Merkle root.
* `value_compute_alg_hash: vector<u8>`: Hash of the compute algorithm.
* `r: vector<u8>`: R component of the signature.
* `s: vector<u8>`: S component of the signature.
* `v: u8`: V component of the signature.

#### Behavior

* Verifies the update data's signature using the Stork EVM public key stored in the `StorkState` resource.
* Verifies that the update is more recent than the data currently in the feed.
* If the signature is invalid, the function errors with `E_INVALID_SIGNATURE`.
* If the update is not recent, the function does not error but does no update the feed object.
* If both verification pass, updates the `TemporalNumericValue` for the asset and emits a `TemporalNumericValueUpdateEvent`.

#### Errors

* `E_INVALID_SIGNATURE:` If the signature verification fails.

### Update Multiple Temporal Numeric Values EVM

```rust
public entry fun update_multiple_temporal_numeric_values_evm(
        // signer of the transaction to pay the fee
        signer: &signer,
        // asset ids
        ids: vector<vector<u8>>,
        // temporal numeric value timestamp ns
        temporal_numeric_value_timestamp_ns: vector<u64>,
        // temporal numeric value magnitude
        temporal_numeric_value_magnitude: vector<u128>,
        // temporal numeric value negative
        temporal_numeric_value_negative: vector<bool>,
        // publisher's merkle roots
        publisher_merkle_roots: vector<vector<u8>>,
        // value compute algorithm hashes
        value_compute_alg_hashes: vector<vector<u8>>,
        // signatures r
        rs: vector<vector<u8>>,
        // signatures s
        ss: vector<vector<u8>>,
        // signatures v
        vs: vector<u8>,
    )
```

#### Description

Efficiently updates the latest values for multiple assets based on the proved update data vectors, where the corresponding update data is keyed by index. For example:

* `ids[i]`
* `temporal_numeric_value_timestamp_nss[i]`
* `temporal_numeric_value_magnitudes[i]`
* ...

all belong to the same update.

#### Parameters

* `signer: &signer`: A reference to the signer of the transaction, automatically provided by the MoveVM.
* `ids: vector<vector<u8>>`: Asset IDs for the updates.
* `temporal_numeric_value_timestamp_nss: vector<u64>`: Timestamps for the updates.
* `temporal_numeric_value_magnitudes: vector<u128>`: Magnitudes of the numeric values.
* `temporal_numeric_value_negatives: vector<bool>`: Indicates whether each value is negative.
* `publisher_merkle_roots: vector<vector<u8>>`: Publisher Merkle roots.
* `value_compute_alg_hashes: vector<vector<u8>>`: Hashes of the compute algorithms.
* `rs: vector<vector<u8>>`: R components of the signatures.
* `ss: vector<vector<u8>>`: S components of the signatures.
* `vs: vector<u8>`: V components of the signatures.

#### Behavior

* Validates that all input vectors have the same length.
* Verifies the signature for each update using the Stork EVM public key.
* Verifies that each update is more recent than the current asset data.
* If any signature fails verification, the function errors with `E_INVALID_SIGNATURE` for all updates.
* If some updates are not recent, those updates are skipped without erroring.
* Successfully verified and recent updates are applied.
* Emits a `TemporalNumericValueUpdateEvent` for each successful update.

#### Errors

* `E_INVALID_SIGNATURE:` If any update's signature verification fails.
* `E_NO_UPDATES`: If the ids vector is empty
* `E_INVALID_LENGTHS`: If not all the input vectors are the same length.

### Get Temporal Numeric Value Unchecked

<pre class="language-rust"><code class="lang-rust"><strong>#[view]
</strong><strong>public fun get_temporal_numeric_value_unchecked(
</strong>        // The asset id
        asset_id: vector&#x3C;u8>,
    ): TemporalNumericValue {
        let encoded_asset_id = encoded_asset_id::from_bytes(asset_id);
        temporal_numeric_value_feed_registry::get_latest_canonical_temporal_numeric_value_unchecked(encoded_asset_id)
    }
</code></pre>

#### Description

View function that retrieves the latest value for a specified asset without additional checks.

#### Parameters

* `asset_id: vector<u8>`: The [encoded asset ID](../../introduction/core-concepts.md#asset-ids) of the feed to read.

#### Returns

* `TemporalNumericValue`: The latest value for the relevant asset.

#### Errors

* `E_FEED_NOT_FOUND`: If the specified feed does exist.

## stork::state Methods

### Get Owner

```rust
#[view]
public fun get_owner(): address acquires StorkState
```

#### Description

View function that retrieves the stored address of the owner of the Stork contract from the the `StorkState` .

#### Returns

* `address`: The value of the `owner` field of the state.

### Get Stork EVM Public Key

```rust
#[view]
public fun get_stork_evm_public_key(): EvmPubKey acquires StorkState
```

#### Description

View function that retrieves the stored EVM public key from the `StorkState`.

#### Returns

* `EvmPubkey`: The value of the `stork_evm_public_key` field of the state.

### Get Single Update Fee in Octas

```rust
#[view]
public fun get_single_update_fee_in_octas(): u64 acquires StorkState
```

#### Description

View function that retrieves the fee required to update a single value from the StorkState.

#### Returns

* `u64`: The value of the `single_update_fee_in_octas` field of the state.

### State Exists

```rust
 #[view]
 public fun state_exists(): bool
```

#### Description

View function that checks whether or not the `StorkState` resource exists. This can be used as a proxy for whether or not the Stork contract has been initialized.

#### Returns

* `bool`: Whether or not the `StorkState` resource exists.

## Examples

Example usage of the Stork Aptos contract can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/chains/aptos/examples).
