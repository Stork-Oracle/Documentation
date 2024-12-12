# What is Stork for Real Time?

## Welcome to _Fast (whoosh!)_&#x20;

{% hint style="info" %}
The Stork model maintains all the same guarantees of traditional decentralized "oracles": Stork data is fully verifiable, manipulation-resistant, and offered across decentralized infrastructure.
{% endhint %}

Stork for Real Time is an ultra low-latency (sub millisecond), decentralized off and on-chain price feed designed for any chain. Stork for Real Time is powered by a decentralized network of data publishers, and signed in a way compatible with signature verification on EVM, StarkEx, Starknet, and Move chains. We prioritize performance, using ultra-fast websockets, to ensure data is available at the millisecond level, similar to the data used for trading in TradFi.&#x20;

Using an off-chain, decentralized feed gives protocols the ability to perform initial processing off-chain, and elect to only push on-chain the price updates that are relevant to your product. Since prices are signed in a chain-compatible way protocols can use Stork’s Verifier Contract, or their own smart contract, to verify the feed on-chain, proving that the data is legitimate.&#x20;

{% hint style="warning" %}
Have questions? Documentation unclear? [info@stork.network](mailto:info@stork.network) or [Twitter DMs](https://twitter.com/StorkOracle) open.
{% endhint %}

## Use Cases

* Derivatives protocols, such as decentralized perpetual swaps
* Low latency chains
