---
icon: tower-broadcast
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Websocket API

Stork [Aggregators](../../introduction/how-it-works.md#aggregators) expose websocket endpoints for both [Publishers](../../introduction/how-it-works.md#publishers) and [Subscribers](../../introduction/how-it-works.md#subscribers). Publishers use this to continuously push their signed data to the Aggregators, while Subscribers can use this to listen to the ultra low-latency stream of signed aggregated data from Stork.\
\
These docs use wscat, a common CLI tool for interacting with websockets, for examples. This is just for legibility and the websockets can be interacted with using any tool or library that supports the standard websocket spec.\


{% content-ref url="publisher.md" %}
[publisher.md](publisher.md)
{% endcontent-ref %}

{% content-ref url="subscriber.md" %}
[subscriber.md](subscriber.md)
{% endcontent-ref %}

