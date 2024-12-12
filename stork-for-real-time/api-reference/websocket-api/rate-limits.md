# Rate Limits

Rate limits are tied to authentication tokens.

### Connection rate limits

Users are allowed 10 live connections total, and up to 10 connection attempts a second. Connection attempts after violating either of these rate limits will be rejected with a 429 HTTP response code until the user is no longer in violation.

### Message rate limits

Each websocket connection is allowed to send up to 5 messages a second. Connections that violate this rate limit will be disconnected.
