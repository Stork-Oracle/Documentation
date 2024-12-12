# Getting Started

### Authentication

The websocket connection request must include an `Authorization` header with a valid token value.

For example:

```
wscat -c '[WEBSOCKET URL]' --auth 'user:password'

wscat -c '[WEBSOCKET URL]' -H "Authorization: Basic $(echo -n 'user:password' | base64)"
```

### Compression

Only compressed websocket streams are supported. Clients can enable compression by including the permessage-deflate extension in the websocket handshake request. The wscat tool does this by default, but here is an explicit example:

```
wscat -c '[WEBSOCKET URL]' --auth 'user:password' -H 'Sec-Websocket-Extensions: permessage-deflate'
```

