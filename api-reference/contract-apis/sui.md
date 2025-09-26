---
description: Programming API reference for the Stork Sui contract.
icon: droplet
---

# Sui

## SDK

Sui contracts can integrate with the [Stork contract](https://github.com/Stork-Oracle/stork-external/tree/main/sui/contracts) by including it as a project dependency.

## Installation

{% tabs %}
{% tab title="Move" %}
After setting up your Sui Move project, add the Stork contract to your project dependencies by adding the following line to the `[dependencies]` section of your projects `Move.toml`:

```toml
// Move.toml
[dependencies]
stork = { git = "https://github.com/stork-oracle/stork-external.git", subdir = "chains/sui/contracts", rev = "main" }
```

You can now import the Stork interfaces with:

```rust
// your_module.move
use stork::{<...>}
```
{% endtab %}
{% endtabs %}

## Concepts&#x20;

### Version Gating

Some functions, especially if they interact with the `StorkState` object, are considered "version gated". If the number in the version field if the passed `StorkState` is not the same as the `Version` constant in the code, the function will fail will `EIncorrectVersion`. This can occur when the Stork contract address being used is not pointing to the most recent update of the contract, and is a mechanism to protect against issues that may be present in old versions of the contract. Functions that are not directly version gated, but call version gated functions, are considered version gated.



### Stork State Object

Many functions require passing a reference to the `StorkState` object. We recommend deriving this address from the contract address in code, rather than hardcoding it anywhere. An example of this derivation can be found in the app in the example in [#examples](sui.md#examples "mention"). Though we recommend derivation, we also provide the address of the state object in the [Sui Contract Addresses page](../../resources/contract-addresses/sui.md).

## stork::stork Methods

### Update Single Temporal Numeric Value EVM

```rust
public fun update_single_temporal_numeric_value_evm(
        // stork state object
        stork_state: &mut StorkState,
        // the input data
        update_data: UpdateTemporalNumericValueEvmInput,
        // fee
        fee: Coin<SUI>,
        // context
        ctx: &mut TxContext,
    )
```

**Description**

Updates the latest value in the relevant feed object based on the provided update data object.

**Parameters**

* `stork_state: &mut StorkState`: A mutable reference to the `StorkState` object.
* `update_data: UpdateTemporalNumericValueEvmInput`: Update data object for a single asset.
* `fee: Coin<SUI>`: The fee to pay for the update.
* `ctx: &mut TxContext`: Transaction context.

**Behavior**

* Verifies the update data's signature using the Stork EVM public key stored on the state object.
* Verifies that the update is more recent than the data currently in the feed object.
* If the signature is invalid, the function errors with `EInvalidSignature`.
* If the signature is valid but the update is not fresher, the function does not error but does not update the feed object.
* If both verifications pass, updates the feed object and emits a `TemporalNumericValueFeedUpdateEvent`

**Errors**

* `EInvalidSignature`: If the signature verification fails.
* `EInsufficientFee`: If the fee provided is less than the required amount.

This function is version gated.

### Update Multiple Temporal Numeric Values EVM

```rust
public fun update_multiple_temporal_numeric_values_evm(
        // stork state object
        stork_state: &mut StorkState,
        // the input data
        update_data: UpdateTemporalNumericValueEvmInputVec,
        // fee
        fee: Coin<SUI>,
        // context
        ctx: &mut TxContext,
    )
```

**Description**

Efficiently updates the latest values in multiple feed objects based on the provided update data object.

**Parameters**

* `stork_state: &mut StorkState`: A mutable reference to the `StorkState` object.
* `update_data: UpdateTemporalNumericValueEvmInputVec`: Update data object for multiple assets.
* `fee: Coin<SUI>`: The fee to pay for the updates.
* `ctx: &mut TxContext`: Transaction context.

**Behavior**

* Verifies the signature for each update using the Stork EVM public key.
* Verifies that each update is fresher than the current feed data.
* If any signature fails verification, the function errors with `EInvalidSignature` for all updates.
* If some updates are not fresher, those specific feed objects are skipped without erroring.
* Successfully verified and fresher updates are applied to their respective feed objects.
* Emits a `TemporalNumericValueFeedUpdateEvent` for each successful update.

**Errors**

* `EInvalidSignature`: If any update's signature verification fails.
* `EInsufficientFee`: If the fee provided is less than the required total amount.

This function is more efficient than multiple calls to [`Update Single Temporal Numeric Value EVM`](sui.md#update-single-temporal-numeric-value-evm) for updating multiple assets.

This function is version gated

### Get Temporal Numeric Value Unchecked

<pre class="language-rust"><code class="lang-rust">public fun get_temporal_numeric_value_unchecked(
    // stork state object
    stork_state: &#x26;StorkState,
    // encoded asset id
    feed_id: vector&#x3C;u8>
<strong>    ): TemporalNumericValue
</strong></code></pre>

**Description**

Retrieves the latest value for a specified feed without additional checks.

**Parameters**

* `stork_state: &StorkState`: A reference to the `StorkState` object.
* `feed_id: vector<u8>`: The [encoded asset ID](../../introduction/core-concepts.md#asset-ids) of the feed to read.

**Returns**

* `TemporalNumericValue`: The latest value for the relevant feed.

**Errors**

* `EFeedNotFound`: If the specified feed ID does not exist.

This function is version gated.

## stork::state Methods

### Get Stork EVM Public Key

```rust
public fun get_stork_evm_public_key(
    stork_state: &StorkState
    ): EvmPubkey 
```

**Description**

Retrieves the stored EVM public key from the `StorkState`.

**Parameters**

* `stork_state: &StorkState`: A reference to the `StorkState` object.

**Returns**

* `EvmPubkey`: The value of the `stork_evm_public_key` field of the state.

This function is version gated.

### Get Single Update Fee in Mist

```rust
public fun get_single_update_fee_in_mist(
    stork_state: &StorkState
    ): u64
```

**Description**

Retrieves the fee required to update a single value from the `StorkState`.

**Parameters**

* `stork_state: &StorkState`: A reference to the `StorkState` object.

**Returns**

* `u64`: The value of the `single_update_fee_in_mist` field of the state.

This function is version gated.

### Get Stork Sui Address

```rust
public fun get_stork_sui_address(
    stork_state: &StorkState
    ): address
```

**Description**

Retrieves the stored Sui address of the Stork program from the `StorkState`.

**Parameters**

* `stork_state: &StorkState`: A reference to the `StorkState` object.

**Returns**

* `address`: The value of the `stork_sui_address` field of the state.

This function is version gated.

### Get Version

```rust
public fun get_version(
    stork_state: &StorkState
    ): u64
```

Retrieves the version of the `StorkState`.

**Parameters**

* `stork_state: &StorkState`: A reference to the `StorkState` object.

**Returns**

* `u64`: The value of the `version` field of the state.

This function is version gated.

## stork::temporal\_numeric\_value\_evm\_vec Methods

### New

```rust
public fun new(
        id: vector<u8>,
        temporal_numeric_value_timestamp_ns: u64,
        temporal_numeric_value_magnitude: u128,
        temporal_numeric_value_negative: bool,
        publisher_merkle_root: vector<u8>,
        value_compute_alg_hash: vector<u8>,
        r: vector<u8>,
        s: vector<u8>,
        v: u8,
    ): UpdateTemporalNumericValueEvmInput
```

**Description**

Constructs an object representing an update for a single asset for passing to [`Update Single Temporal Numeric Value EVM`](sui.md#update-single-temporal-numeric-value-evm).

**Parameters**

* `id: vector<u8>`: The asset ID to update.
* `temporal_numeric_value_timestamp_ns: u64`: Timestamp of the temporal numeric value.
* `temporal_numeric_value_magnitude: u128`: The magnitude of the numeric value.
* `temporal_numeric_value_negative: bool`: Indicates whether the value is negative.
* `publisher_merkle_root: vector<u8>`: The publisher's Merkle root.
* `value_compute_alg_hash: vector<u8>`: Hash of the compute algorithm.
* `r: vector<u8>`: R component of the signature.
* `s: vector<u8>`: S component of the signature.
* `v: u8`: V component of the signature.

**Returns**

* `UpdateTemporalNumericValueEvmInput`: The constructed update object.

## stork::temporal\_numeric\_value\_evm\_input Methods

### New

```rust
public fun new(
        ids: vector<vector<u8>>,
        temporal_numeric_value_timestamp_nss: vector<u64>,
        temporal_numeric_value_magnitudes: vector<u128>,
        temporal_numeric_value_negatives: vector<bool>,
        publisher_merkle_roots: vector<vector<u8>>,
        value_compute_alg_hashes: vector<vector<u8>>,
        rs: vector<vector<u8>>,
        ss: vector<vector<u8>>,
        vs: vector<u8>,
    ): UpdateTemporalNumericValueEvmInputVec
```

**Description**

Creates a vector of update objects, each representing an update for a specific asset, where the corresponding update data is keyed by index. For example:&#x20;

* `ids[i]`
* `temporal_numeric_value_timestamp_nss[i]`
* `temporal_numeric_value_magnitudes[i]`
* ...

&#x20;all belong to the same update.

**Parameters**

* `ids: vector<vector<u8>>`: Asset IDs for the updates.
* `temporal_numeric_value_timestamp_nss: vector<u64>`: Timestamps for the updates.
* `temporal_numeric_value_magnitudes: vector<u128>`: Magnitudes of the numeric values.
* `temporal_numeric_value_negatives: vector<bool>`: Indicates whether each value is negative.
* `publisher_merkle_roots: vector<vector<u8>>`: Publisher Merkle roots.
* `value_compute_alg_hashes: vector<vector<u8>>`: Hashes of the compute algorithms.
* `rs: vector<vector<u8>>`: R components of the signatures.
* `ss: vector<vector<u8>>`: S components of the signatures.
* `vs: vector<u8>`: V components of the signatures.

**Behavior**

* Constructs an `UpdateTemporalNumericValueEvmInput` object for each set of inputs and bundles them into one object.
* Validates that all input vectors have the same length.

**Errors**

* `EInvalidLengths`: If input vectors do not have the same length.
* `ENoUpdates`: If the input vector is empty.

**Returns**

* `UpdateTemporalNumericValueEvmInputVec`: The constructed object containing multiple updates.

## Examples

Example usage of the Stork Sui contract can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/chains/sui/examples).&#x20;
