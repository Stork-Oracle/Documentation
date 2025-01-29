---
icon: s
description: Programming API reference for the Stork Solana contract.
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

Solana contracts can program against [Stork's contract](https://github.com/Stork-Oracle/stork-external/tree/main/contracts/solana) using the stork-sdk rust crate available on [crates.io](https://crates.io/crates/stork-solana-sdk).  This SDK provides useful methods and structs for **reading** from stork price feed account. The Stork contract and SDK are built on top of [Anchor](https://github.com/coral-xyz/anchor).

### Installation

{% tabs %}
{% tab title="Rust" %}
After setting up your Anchor project, add the stork-solana-sdk to your project dependencies by adding the following line to the `[dependencies]` section of the programs `Cargo.toml` :

```toml
// Cargo.toml
[dependencies]
stork-solana-sdk = ">0.0.5"
```

or the following command:

```bash
cargo add stork-solana-sdk
```

You can now import the stork-sdk's interfaces with:

<pre class="language-rust"><code class="lang-rust"><strong>// your_module.rs
</strong><strong>use stork_solana_sdk::{&#x3C;...>};
</strong></code></pre>
{% endtab %}
{% endtabs %}

### Documentation

Documentation for the methods, structs, and constants provided by the stork\_solana\_sdk can be found on [doc.rs](https://docs.rs/stork-solana-sdk).

### Examples

Example usage of the stork-solana-sdk for consuming Stork prices can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/examples/solana).

## Contract

Stork's contract depends on the [stork-solana-sdk crate](https://crates.io/crates/stork-solana-sdk) and [Anchor](https://github.com/coral-xyz/anchor), and contains useful methods for **writing** to the Stork Config account, as well as Temporal Numeric Value Feed PDA accounts that represent Stork data feeds. The full source-code can be found in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/contracts/solana). For the official deployments, please see the [Solana Contract Addresses](../../resources/contract-addresses/solana.md).
