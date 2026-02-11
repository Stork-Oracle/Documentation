---
description: Programming API reference for the Stork Fast EVM contract.
icon: file-signature
---

# Contract API

### SDK <a href="#sdk" id="sdk"></a>

EVM contracts can program against the [Stork Fast contract'](https://github.com/Stork-Oracle/stork-external/tree/main/chains/evm/contracts/stork_fast)s interface by using the stork-fast-evm-sdk npm package available on [npmjs.com](https://www.npmjs.com/package/@storknetwork/stork-fast-evm-sdk). This SDK provides an interface and useful struct for interacting with the Stork contract. The Stork contract is built using [Hardhat](https://hardhat.org/).

### Getting Started <a href="#getting-started" id="getting-started"></a>

Solidity

After setting up your Hardhat project, add the stork-fast-evm-sdk to your project dependencies by adding the following line to the `"dependencies"` section of the programs `package.json`

<a class="button secondary">Copy</a>

```json
// package.json
"dependencies": {
    "@storknetwork/stork-fast-evm-sdk": "^1.0.0"
}
```

or with the following command:

<a class="button secondary">Copy</a>

```bash
npm i @storknetwork/stork-fast-evm-sdk
```

You can now import the SDK's interface and types with:

<a class="button secondary">Copy</a>

```solidity
// YourContract.sol
import "@storknetwork/stork-fast-evm-sdk/IStorkFast.sol";
import "@storknetwork/stork-fast-evm-sdk/StorkFastStructs.sol";
```

### Concepts <a href="#concepts" id="concepts"></a>

#### Upgradeability <a href="#upgradeability" id="upgradeability"></a>

The Stork contract is designed to be upgradeable using [OpenZeppelin's proxy pattern](https://docs.openzeppelin.com/contracts/5.x/learn/upgrading-smart-contracts). Ensure the proxy address remains consistent when interacting with the contract to avoid version mismatches.

#### Usage

In contrast to the Stork Core contract, there is no expectation that users store data on the StorkFast contract. Instead, users should verify a stork update as part of the same transaction used in their application, and only proceed if verification is successful.

### Methods <a href="#methods" id="methods"></a>

#### Verify Signed ECDSA Payload <a href="#update-temporal-numeric-values-v1" id="update-temporal-numeric-values-v1"></a>

```solidity
function verifySignedECDSAPayload(
    bytes calldata payload
) external payable returns (bool);
```

**Description**

Receives a stork batch update and returns a `bool` whether the update is verified or not.

**Parameters**

* `payload`: Packed bytes receivable via the StorkFast [websocket](https://docs.stork.network/resources/stork-fast/websocket-api#signed-ecdsa-message).

**Behavior**

* Verifies the signature of the update batch using the stored EVM public key.
* Only requires one signature verification as the entire batch is signed once.
* Requires sufficient fee based on the number of updates.

**Errors**

* `InvalidPayload (``0x7c6953f9)`: If the update itself is malformed.
* `InsufficientFee (0x025dbdd4)`: If the provided fee is less than the required amount.

#### Verify And Deserialize Signed ECDSA Payload

**Description**

Receives a stork batch update and returns deserialized `StorkAssets` if the update is verifiable.

**Parameters**

* `payload`: Packed bytes receivable via the StorkFast [websocket](https://docs.stork.network/resources/stork-fast/websocket-api#signed-ecdsa-message).

**Behavior**

* Same as Verify Signed ECDSA Payload
* Also returns deserialized data, but reverts on verification failure

**Errors**

* `InvalidPayload (0x7c6953f9)`: If the update itself is malformed.
* `InvalidSignature (0x8baa579f)` : If the signature verification failes.
* `InsufficientFee (0x025dbdd4)`: If the provided fee is less than the required amount.

#### Version <a href="#version" id="version"></a>

```solidity
function version() public pure returns (string memory);
```

**Description**

Retrieves the current version of the contract.

**Returns**

* `string`: The version string (e.g., "1.0.0").

### Examples <a href="#examples" id="examples"></a>

An example contract can be found in the the [stork-external github repo](https://github.com/Stork-Oracle/stork-external/tree/main/chains/evm/examples/stork_fast).
