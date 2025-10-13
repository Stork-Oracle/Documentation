---
description: Programming API reference for the Stork EVM contract.
icon: ethereum
---

# EVM

## SDK

EVM contracts can program against the [Stork contract'](https://github.com/Stork-Oracle/stork-external/tree/main/chains/evm/contracts/stork)s interface by using the stork-evm-sdk npm package available on [npmjs.com](https://www.npmjs.com/package/@storknetwork/stork-evm-sdk). This SDK provides an interface and useful struct for interacting with the Stork Contract.\
\
The Stork contract can also be used via the [Pyth and Chainlink](../../resources/adapters.md) adapters. \
\
The Stork contract is built using [Hardhat](https://hardhat.org/).

## Getting Started

{% tabs %}
{% tab title="Solidity" %}
After setting up your Hardhat project, add the stork-evm-sdk to your project dependencies by adding the following line to the `"dependencies"` section of the programs `package.json`

```json
// package.json
"dependencies": {
    "@storknetwork/stork-evm-sdk": "^1.0.0"
  }
```

or with the following command:

```bash
npm i @storknetwork/stork-evm-sdk
```

You can now import the sdk's interface and types with:

```solidity
// YourContract.sol
import "@storknetwork/stork-evm-sdk/IStork.sol";
import "@storknetwork/stork-evm-sdk/StorkStructs.sol";
```
{% endtab %}
{% endtabs %}



## Concepts

### Upgradeability

The Stork contract is designed to be upgradeable using [OpenZeppelin's proxy pattern](https://docs.openzeppelin.com/contracts/5.x/learn/upgrading-smart-contracts). Ensure the proxy address remains consistent when interacting with the contract to avoid version mismatches.

## Methods

### Update Temporal Numeric Values V1

```solidity
function updateTemporalNumericValuesV1(
    StorkStructs.TemporalNumericValueInput[] calldata updateData
) public payable;
```

**Description**

Updates multiple temporal numeric values by verifying signatures and ensuring freshness.

**Parameters**

* `updateData`: Array of `TemporalNumericValueInput` structs containing feed updates.

**Behavior**

* Verifies the signature of each feed update using the stored EVM public key.
* Updates the feed value if the signature is valid and the value is fresher than the current state.
* Requires sufficient fee based on the number of updates.

**Errors**

* `InvalidSignature (0x8baa579f)`: If any feed update fails signature verification.
* `NoFreshUpdate (0xde2c57fa)`: If none of the provided updates are fresher than current values.
* `InsufficientFee (0x025dbdd4)`: If the provided fee is less than the required amount.

### Get Temporal Numeric Value V1

```solidity
function getTemporalNumericValueV1(
    bytes32 id
) public view returns (StorkStructs.TemporalNumericValue memory value);
```

**Description**

Retrieves the latest temporal numeric value for the specified feed ID. Checks for the staleness threshold set in the state, which varies between chains but is typically 3600 seconds.

**Parameters**

* `id`: The identifier of the feed.

**Returns**

* `value`: The latest `TemporalNumericValue` struct for the feed.

**Errors**

* `NotFound (0xc5723b51)`: If no value exists for the given feed ID.
* `StaleValue (0x24c4fe43)`: If the value is older than the valid time period.

### Get Temporal Numeric Value Unsafe V1

```solidity
function getTemporalNumericValueUnsafeV1(
    bytes32 id
) public view returns (StorkStructs.TemporalNumericValue memory value);
```

**Description**

Retrieves the latest temporal numeric value for the specified feed ID without checking its freshness.

**Parameters**

* `id`: The identifier of the feed.

**Returns**

* `value`: The latest `TemporalNumericValue` struct for the feed.

**Errors**

* `NotFound (0xc5723b51)`: If no value exists for the given feed ID.

### Get Update Fee V1

```solidity
function getUpdateFeeV1(
    StorkStructs.TemporalNumericValueInput[] calldata updateData
) public view returns (uint feeAmount);
```

**Description**

Calculates the total fee required for the given updates.

**Parameters**

* `updateData`: Array of `TemporalNumericValueInput` structs representing updates.

**Returns**

* `feeAmount`: The total fee required for the updates.

### Verify Publisher Signatures V1

```solidity
function verifyPublisherSignaturesV1(
    StorkStructs.PublisherSignature[] calldata signatures,
    bytes32 merkleRoot
) public pure returns (bool);
```

**Description**

Verifies multiple publisher signatures against the provided Merkle root.

**Parameters**

* `signatures`: Array of `PublisherSignature` structs.
* `merkleRoot`: The Merkle root to validate against.

**Returns**

* `bool`: True if all signatures are valid and match the Merkle root.

### Version

```solidity
function version() public pure returns (string memory);
```

**Description**

Retrieves the current version of the contract.

**Returns**

* `string`: The version string (e.g., "1.0.3").

## Examples

An example contract can be found in the the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/chains/evm/examples/stork).

