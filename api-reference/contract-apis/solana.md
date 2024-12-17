---
description: Programming API reference for the Stork Solana contract.
icon: s
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Solana

## SDK

Solana contracts can program against [Stork's contract](https://github.com/Stork-Oracle/stork-external/tree/main/contracts/solana) using the stork-sdk rust crate available on [crates.io](https://crates.io/crates/stork-sdk).  This SDK provides useful methods and structs for **reading** from stork price feed account. For thorough documentation, please also see the [docs.rs page](https://docs.rs/stork-sdk/0.0.5/stork_sdk/). The Stork contract and SDK are built on top of [Anchor](https://github.com/coral-xyz/anchor).

### Installation

{% tabs %}
{% tab title="Rust" %}
After setting up your Anchor project, add the stork-sdk to your project dependencies by adding the following line to the `[dependencies]` section of the programs `Cargo.toml` :

```toml
// Cargo.toml
[dependencies]
stork-sdk = ">0.0.5"
```

or the following command:

```bash
cargo add stork-sdk
```

You can now import the stork-sdk's interfaces with:

<pre class="language-rust"><code class="lang-rust"><strong>// your_module.rs
</strong><strong>use stork-sdk::{&#x3C;...>};
</strong></code></pre>
{% endtab %}
{% endtabs %}

### Documentation

Documentation for the methods, structs, and constants provided by the stork-sdk can be found on [doc.rs](https://docs.rs/stork-sdk/0.0.5/stork_sdk/index.html).

### Examples

Example usage of the stork-sdk for consuming Stork prices can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/examples/solana).

## Contract

Stork's contract depends on the [stork-sdk crate](https://docs.rs/stork-sdk/0.0.5/stork_sdk/index.html) and [Anchor](https://github.com/coral-xyz/anchor), and contains useful methods for **writing** to the Stork Config account, as well as Temporal Numeric Value Feed PDA accounts that represent Stork data feeds. The full source-code can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/contracts/solana). For the official deployments, please see the [Solana Contract Addresses](../../resources/contract-addresses/solana.md).

## Methods

### Initialize

```rust
pub fn initialize(
        ctx: Context<Initialize>,
        stork_sol_public_key: Pubkey,
        stork_evm_public_key: EvmPubkey,
        single_update_fee_in_lamports: u64,
    ) -> Result<()>
```

**Description**

Initializes the Stork configuration by creating the `StorkConfig` PDA account. The signer is set as the owner in the `owner` field.

**Parameters**

* `ctx: Context<Initialize>`: Context containing the accounts and required for initialization.
* `stork_sol_public_key: Pubkey`: The Stork Solana public key.
* `stork_evm_public_key: EvmPubkey`: The Stork EVM public key.
* `single_update_fee_in_lamports: u64`: The fee for a single update in lamports.

**Behavior**

* Creates the `StorkConfig` PDA account.
*   Sets the signer as the owner in the `ow`

    **Description**

    Updates the latest value in the feed account for a specific asset using data signed by the Stork EVM private key.

    **Parameters**

    * `ctx: Context<UpdateTemporalNumericValue>`: Context containing the accounts required for the update.
    * `update_data: TemporalNumericValueEvmInput`: Signed data for a single asset update.

    **Behavior**

    1. Verifies the signature of the update data using the `stork_evm_public_key` stored in the config account.
    2. Checks if the new update is more recent than the current feed data.
    3. Transfers the update fee from the payer to the treasury.
    4. Updates the feed account with the new data if all checks pass.

    **Errors**

    * `StorkError::InvalidSignature`: If the update data signature verification fails.
    * `StorkError::InsufficientFunds`: If the payer does not have enough lamports to cover the update fee.

    **Returns**

    * `Result<()>`: Is `Ok(())` if the update is successful.

    `ner` field.

**Errors**

* `StorkError::Unauthorized`: If the signer is not the owner of the contract.

**Returns**

* `Result<()>`: Is `Ok(())` on success or a `StorkError` on failure.

### Update Temporal Numeric Value EVM

```rust
pub fn update_temporal_numeric_value_evm(
        ctx: Context<UpdateTemporalNumericValue>,
        update_data: TemporalNumericValueEvmInput,
    ) -> Result<()>
```

**Description**

Updates the latest value in the feed account for a specific asset using data signed by the Stork EVM private key.

**Parameters**

* `ctx: Context<UpdateTemporalNumericValue>`: Context containing the accounts required for the update.
* `update_data: TemporalNumericValueEvmInput`: Signed data for a single asset update.

**Behavior**

1. Verifies the signature of the update data using the `stork_evm_public_key` stored in the config account.
2. Verifies if the new update is more recent than the current feed data.
3. Does not error, but does not update if the recency verification fails.
4. Transfers the update fee from the payer to the treasury.
5. Updates the feed account with the new data if all verifications pass.

**Errors**

* `StorkError::InvalidSignature`: If the update data signature verification fails.
* `StorkError::InsufficientFunds`: If the payer does not have enough lamports to cover the update fee.

**Returns**

* `Result<()>`: Is `Ok(())` if the update is successful.

### Update Single Update Fee

```rust
pub fn update_single_update_fee_in_lamports(
        ctx: Context<AdminUpdate>,
        new_single_update_fee_in_lamports: u64,
    ) -> Result<()> 
```

**Description**

Updates the fee required to perform a single feed update.

**Parameters**

* `ctx: Context<AdminUpdate>`: Context containing the config PDA account.
* `new_single_update_fee_in_lamports: u64`: The new single update fee in lamports.

**Behavior**

* Updates the `single_update_fee_in_lamports` field in the `StorkConfig` PDA account.

**Errors**

* `StorkError::Unauthorized`: If the signer is not the owner defined in the `owner` field of the `StorkConfig` PDA account.

**Returns**

* `Result<()>`: Is `Ok(())` on success or a `StorkError` on failure.

### Update Stork Sol Pub Key

<pre class="language-rust"><code class="lang-rust"><strong>pub fn update_stork_sol_public_key(
</strong>        ctx: Context&#x3C;AdminUpdate>,
        new_stork_sol_public_key: Pubkey,
    ) -> Result&#x3C;()>
</code></pre>

**Description**

Updates the Stork Solana public key in the `StorkConfig` PDA account.

**Parameters**

* `ctx: Context<AdminUpdate>`: Context containing the config PDA account.
* `new_stork_sol_public_key: Pubkey`: The new Stork Solana public key.

**Behavior**

* Updates the `stork_sol_public_key` field in the `StorkConfig` PDA account.

**Errors**

* `StorkError::Unauthorized`: If the signer is not the owner defined in the `owner` field of the `StorkConfig` PDA account.

**Returns**

* `Result<()>`: Is `Ok(())` on success or a `StorkError` on failure.

### Update Stork EVM Pub Key

```rust
  pub fn update_stork_evm_public_key(
        ctx: Context<AdminUpdate>,
        new_stork_evm_public_key: EvmPubkey,
    ) -> Result<()>
```

**Description**

Updates the Stork EVM public key in the `StorkConfig` PDA account. This key is used to verify the signatures of update data passed to the `update_temporal_numeric_value_evm` function.

**Parameters**

* `ctx: Context<AdminUpdate>`: Context containing the config PDA account.
* `new_stork_evm_public_key: EvmPubkey`: The new Stork EVM public key.

**Behavior**

* Updates the `stork_evm_public_key` field in the `StorkConfig` PDA account.

**Errors**

* `StorkError::Unauthorized`: If the signer is not the owner defined in the `owner` field of the `StorkConfig` PDA account.

**Returns**

* `Result<()>`: Is `Ok(())` on success or a `StorkError` on failure.
