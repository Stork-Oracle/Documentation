---
description: Programming API reference for the Stork EVM contract.
icon: ethereum
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

# EVM

## SDK

EVM contracts can program against the [Stork contract'](https://github.com/Stork-Oracle/stork-external/tree/main/contracts/evm)s interface by creating an interface and contract to include aliases for the methods and structs required from the Stork contract.  The Stork contract can also be used via the [Pyth and Chainlink](../../resources/adapters.md) adapters. The Stork contract is built using [Hardhat](https://hardhat.org/).

## Getting Started

{% tabs %}
{% tab title="Solidity" %}
After setting up your Hardhat project, create an interface with aliases to your necessary Stork methods, and a contract to hold any necessary Stork structs. Then create an instance of the interface constructed with the Stork [contract address](../../resources/contract-addresses/).

```solidity
// YourContract.sol
contract YourContract {
    IStork public stork;
    // ...
    
    constructor (address _stork /*, ...*/) {
        stork = IStork(_stork);
        // ...
    }
    //...
}

// example: include getTemporalNumericValueUnsafeV1
interface IStork {
    function getTemporalNumericValueUnsafeV1(
        bytes32 id
    ) external view returns (StorkStructs.TemporalNumericValue memory value);
}

contract StorkStructs {
    struct TemporalNumericValue {
        // slot 1
        // nanosecond level precision timestamp of latest publisher update in batch
        uint64 timestampNs; // 8 bytes
        // should be able to hold all necessary numbers (up to 6277101735386680763835789423207666416102355444464034512895)
        int192 quantizedValue; // 8 bytes
    }
}
```

You can now interface with the Stork contract.
{% endtab %}
{% endtabs %}

## Concepts

### Upgradeability

The Stork contract is designed to be upgradeable using [OpenZeppelin's proxy pattern](https://docs.openzeppelin.com/upgrades-plugins/1.x/proxies). Ensure the proxy address remains consistent when interacting with the contract to avoid version mismatches.

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

* `string`: The version string (e.g., "1.0.2").

## Examples

Example usage can be found in the contract adapters in the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/contracts).

