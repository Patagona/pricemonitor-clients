# ComPatagonaPricemonitorShareApiPostAccessTokenResponseV3

Access token response.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token_id** | **float** | Refresh token id. This id would be required, in addition to {{refreshToken}}, to obtain new access token. | 
**token_type** | **str** | Currently only one token type is supported: \&quot;bearer\&quot;. | 
**expires_in_seconds** | **int** | This specifies the time in seconds how long a token is valid. (Default: 900s) | 
**refresh_token** | **str** | If the access token will expire, then a refresh token is used to obtain new access token. Please note that refresh token has an expiration period of 1w. This means that after this period, one could not obtain new access token with expired refresh token. | 
**access_token** | **str** | Access token in JSON Web Token (JWT) format. It ensures that a customer application is authorized to access the protected resources. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


