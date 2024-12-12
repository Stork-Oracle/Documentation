---
description: Stork for Real Time Design
---

# Architecture

### Design

Stork is architected to address the most common problems that arise from using an on-chain oracle for low-latency applications: infrequent price updates, high costs, and limited asset availability. Since putting every price update for every asset on chain is prohibitive is terms of cost and performance, we maintain a decentralized, cryptographically signed network of publishers off-chain. We make their price updates available to protocols off-chain, enabling them to make the determination of which prices and how often they need to be posted on-chain. Updates can be posted a shared Stork contract that will verify and store updates, making them available to the blockchain's ecosystem.

### Components

Stork for Realtime is composed of a few components:

1. **Decentralized Publisher Network**: publishers are trusted or staked data providers that provide market data to Stork. This information is signed by the publisher in a manner compatible with the chains supported by Stork.
2. **Stork Off-Chain High Frequency Oracle:** Stork operates a redundant, geo-distributed infrastructure that powers a low-latency websocket. The websocket enables access to all price feeds provided by the publisher network, including each publisher's signature. Where applicable, Stork calculates a recommended median price that is included alongside each publisher's individual signature.&#x20;
3. **dApp Off-Chain Component:** the off-chain component of the dApp integrates with the Stork websocket; the component is able to make a determination of whether a particular price update should be sent into the dApp's on-chain smart contract, for example if the price would trigger a liquidation.&#x20;
4. **dApp On Chain Contract:** the smart contract uses the Stork On Chain Verifier to verify the signature of the price, ensuring only approved publisher prices are considered.
5. **Stork On Chain Verifier:** the Stork on-chain verifier can be used to verify the published prices are valid – as in, they have been signed by the appropriate contracts.
