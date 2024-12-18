---
icon: sliders-simple
description: >-
  This document describes the structure and usage of the config JSON file used
  by the Stork Publisher Agent.
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

# Config JSON

## Overview

The `config.json` file contains non-secret configuration settings for the Publisher Agent.

## JSON Structure

```
{
  "SignatureTypes": [<string>],
  "IncomingWsPort": <integer>,
  "SignEveryUpdate": <boolean>,
  "PullBasedWsUrl": <string>,
  "PullBasedWsSubscriptionRequest": <object>,
  "ClockPeriod": <string>,
  "DeltaCheckPeriod": <string>,
  "ChangeThresholdPercent": <float>,
  "StorkRegistryBaseUrl": <string>,
  "StorkRegistryRefreshInterval": <string>,
  "BrokerReconnectDelay": <string>,
  "PublisherMetadataRefreshInterval": <string>,
  "PublisherMetadataBaseUrl": <string>,
  "PullBasedWsReconnectDelay": <string>,
  "PullBasedWsReadTimeout": <string>,
}
```

## Configuration Fields

### **`SignatureTypes`**

* **Type**: Array of Strings
* **Description**: Specifies the signature types to be used. Valid values are `"evm"` and `"stark"`.
* **Example**: `["evm"]`
* **Required**: Yes

### **`IncomingWsPort`**

* **Type**: Integer
* **Description**: The port number on which the agent listens for incoming websocket connections.
* **Example**: `5216`
* **Required**: Conditional (required if `PullBasedWsUrl` is not set)

### **`SignEveryUpdate`**

* **Type**: Boolean
* **Description**: Enables signing and sending of every update received, bypassing clock and delta update logic.
* **Example**: `true`
* **Required**: No

### **`PullBasedWsUrl`**

* **Type**: String
* **Description**: The URL of an external websocket server used for pull-based updates.
* **Example**: `"wss://example.com/ws"`
* **Required**: Conditional (required if `IncomingWsPort` is not set)

### **`PullBasedWsSubscriptionRequest`**

* **Type**: Object
* **Description**: The subscription request payload sent to the external websocket server.
* **Example**: `{"type": "subscribe", "data": ["BTCUSD"]}`
* **Required**: No

### **`ClockPeriod`**

* **Type**: String
* **Description**: The interval for clock-based updates.
* **Default**: `"500ms"`
* **Example**: `"1s"`
* **Required**: No

### **`DeltaCheckPeriod`**

* **Type**: String
* **Description**: The interval for checking delta-based updates.
* **Default**: `"10ms"`
* **Example**: `"50ms"`
* **Required**: No

### **`ChangeThresholdPercent`**

* **Type**: Float
* **Description**: The percentage change required to trigger an update.
* **Default**: `0.1`
* **Example**: `1.5`
* **Required**: No

### **`StorkRegistryBaseUrl`**

* **Type**: String
* **Description**: The base URL for the Stork Registry.
* **Default**: `"https://rest.jp.stork-oracle.network"`
* **Required**: No

### **`StorkRegistryRefreshInterval`**

* **Type**: String
* **Description**: The interval for refreshing the Stork Registry.
* **Default**: `"10m"`
* **Example**: `"15m"`
* **Required**: No

### **`BrokerReconnectDelay`**

* **Type**: String
* **Description**: The delay interval for reconnecting to the broker.
* **Default**: `"5s"`
* **Required**: No

### **`PublisherMetadataRefreshInterval`**

* **Type**: String
* **Description**: The interval for refreshing publisher metadata.
* **Default**: `"1h"`
* **Required**: No

### **`PublisherMetadataBaseUrl`**

* **Type**: String
* **Description**: The base URL for fetching publisher metadata.
* **Default**: `"https://rest.jp.stork-oracle.network"`
* **Required**: No

### **`PullBasedWsReconnectDelay`**

* **Type**: String
* **Description**: The delay interval for reconnecting to the pull-based websocket.
* **Default**: `"5s"`
* **Required**: No

### **`PullBasedWsReadTimeout`**

* **Type**: String
* **Description**: The timeout interval for reading from the pull-based websocket.
* **Default**: `"10s"`
* **Required**: No

## Example `config.json`

```json
{
  "SignatureTypes": ["evm"],
  "IncomingWsPort": 5216,
  "SignEveryUpdate": true,
  "PullBasedWsUrl": "wss://example.com/ws",
  "PullBasedWsSubscriptionRequest": {"type": "subscribe", "data": ["BTCUSD"]},
  "ClockPeriod": "500ms",
  "DeltaCheckPeriod": "10ms",
  "ChangeThresholdPercent": 0.1,
  "StorkRegistryBaseUrl": "https://rest.jp.stork-oracle.network",
  "StorkRegistryRefreshInterval": "10m",
  "BrokerReconnectDelay": "5s",
  "PublisherMetadataRefreshInterval": "1h",
  "PublisherMetadataBaseUrl": "https://rest.jp.stork-oracle.network",
  "PullBasedWsReconnectDelay": "5s",
  "PullBasedWsReadTimeout": "10s",
}
```



