---
description: >-
  This document describes the structure of the YAML configuration file used to
  define assets and their associated parameters for the Chain Pusher.
icon: sliders-simple
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

# Asset Config YAML



## Overview

The `asset-config.yaml` configuration file contains a root key `assets`, which is a mapping of asset identifiers (`asset_id`) to their respective configurations. Each asset configuration includes essential metadata and thresholds required by the program.

## YAML Structure

```yaml
assets:
  <asset_id>:
    asset_id: <string>
    fallback_period_sec: <integer>
    percent_change_threshold: <float>
    encoded_asset_id: <string>
```

## Root Key: `assets`

* **Type**: Object
* **Description**: A mapping of `asset_id` to its configuration. Each entry is an Asset Entry keyed by the `asset_id`.

## Asset Entry

Each asset entry contains the following keys:

### **`asset_id`**

* **Type**: String
* **Description**: The plain-text identifier for the asset.
* **Example**: `BTCUSD`

### **`fallback_period_sec`**

* **Type**: Integer
* **Description**: The maximum time in seconds between updates if the `percent_change_threshold` is not met.
* **Example**: `60`

### **`percent_change_threshold`**

* **Type**: Float
* **Description**: The percentage change threshold required to trigger an update.
* **Example**: `1.0`

### **`encoded_asset_id`**

* **Type**: String
* **Description**: The Keccak256 hash of the plain-text `asset_id`. This is used as a unique, encoded identifier for the asset.
* **Example**: `0x7404e3d104ea7841c3d9e6fd20adfe99b4ad586bc08d8f3bd3afef894cf184de`

## Example Configuration

Below is an example YAML configuration file with a single asset entry:

```
assets:
  BTCUSD:
    asset_id: BTCUSD
    fallback_period_sec: 60
    percent_change_threshold: 1.0
    encoded_asset_id: 0x7404e3d104ea7841c3d9e6fd20adfe99b4ad586bc08d8f3bd3afef894cf184de
```

## Usage

This configuration file is read by the [Chain Pusher](https://github.com/Stork-Oracle/stork-external/blob/main/apps/docs/chain_pusher.md) to determine which assets to pull from the aggregator and submit on-chain. Ensure that each `asset_id` is unique and correctly encoded using the Keccak256 hash to derive the `encoded_asset_id`. Supported Assets and their IDs are available in the [Asset ID Registry](../../resources/asset-id-registry.md). Misconfiguration can lead to unexpected behavior.
