# PIN_and_Hash
### Microservice for getting PIN code, salt and hash of SHA algorithm
##### Request format
`http://{host}:{port}/api/pin?pin_len={int}&salt_len={int}`

№ | Params | Required	| Description
--- | ------------ | ------------ | ------------
1 | pin_len | Yes | The length of PIN code
2 | salt_len | No | The length of salt (default=10)