---
description: >-
  This document describes the structure and usage of the keys. JSON file used by
  the Stork Publisher Agent.
icon: key
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

# Keys JSON

{% hint style="info" %}
The fields in `keys.json` can be overridden or substituted with environment variables.
{% endhint %}

## Overview

The `keys.json` file contains sensitive configuration settings, including private and public keys, and is used for signing updates and identifying the publisher.

## JSON Structure

```
{
  "EvmPrivateKey": <string>,
  "EvmPublicKey": <string>,
  "StarkPrivateKey": <string>,
  "StarkPublicKey": <string>,
  "OracleId": <string>,
  "PullBasedAuth": <string>
}
```

## Configuration Fields

### **`EvmPrivateKey`**

* **Type**: String
* **Description**: The private key for signing updates on the Ethereum Virtual Machine (EVM).
* **Required**: Yes (if `evm` is included in `SignatureTypes` in `config.json`)
* **Example**: `"0x8b558d5fc31eb64bb51d44b4b28658180e96764d5d5ac68e6d124f86f576d9de"`

### **`EvmPublicKey`**

* **Type**: String
* **Description**: The public key corresponding to the EVM private key.
* **Required**: Yes (if `evm` is included in `SignatureTypes` in `config.json`)
* **Example**: `"0x99e295e85cb07c16b7bb62a44df532a7f2620237"`

### **`StarkPrivateKey`**

* **Type**: String
* **Description**: The private key for signing updates on the Starkware platform.
* **Required**: Yes (if `stark` is included in `SignatureTypes` in `config.json`)
* **Example**: `"0x66253bdeb3c1a235cf4376611e3a14474e2c00fd2fb225f9a388faae7fb095a"`

### **`StarkPublicKey`**

* **Type**: String
* **Description**: The public key corresponding to the Stark private key.
* **Required**: Yes (if `stark` is included in `SignatureTypes` in `config.json`)
* **Example**: `"0x418d3fd8219a2cf32a00d458f61802d17f01c5bcde5a4f82008ee4a7c8e9a06"`

### **`OracleId`**

* **Type**: String
* **Description**: The 5 character unique identifier for the oracle.
* **Required**: Yes
* **Example**: `"oracl"`

### **`PullBasedAuth`**

* **Type**: String
* **Description**: The authentication token or key used to access pull-based websocket servers.
* **Required**: No
* **Example**: `"Bearer abc123"`
