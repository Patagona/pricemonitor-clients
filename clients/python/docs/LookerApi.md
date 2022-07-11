# pricemonitor_api_client.LookerApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_embed_sso_url_manufacturer**](LookerApi.md#post_embed_sso_url_manufacturer) | **POST** /api/v3/manufacturer/contracts/{contractId}/looker/sso/embed/url | Retrieve an embed SSO url for Looker.
[**post_embed_sso_url_vendor**](LookerApi.md#post_embed_sso_url_vendor) | **POST** /api/v3/vendor/contracts/{contractId}/looker/sso/embed/url | Retrieve an embed SSO url for Looker.


# **post_embed_sso_url_manufacturer**
> EmbedSSOUrlResponseV3ApiResponse post_embed_sso_url_manufacturer(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)

Retrieve an embed SSO url for Looker.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.LookerApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_manufacturer(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LookerApi->post_embed_sso_url_manufacturer: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.LookerApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_manufacturer(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LookerApi->post_embed_sso_url_manufacturer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3** | [**ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3**](ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3.md)| Payload for retrieving a signed embed SSO url using Looker API. | [optional] 

### Return type

[**EmbedSSOUrlResponseV3ApiResponse**](EmbedSSOUrlResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed embed SSO url for Looker. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_embed_sso_url_vendor**
> EmbedSSOUrlResponseV3ApiResponse post_embed_sso_url_vendor(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)

Retrieve an embed SSO url for Looker.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.LookerApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_vendor(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LookerApi->post_embed_sso_url_vendor: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.LookerApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_vendor(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LookerApi->post_embed_sso_url_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3** | [**ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3**](ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3.md)| Payload for retrieving a signed embed SSO url using Looker API. | [optional] 

### Return type

[**EmbedSSOUrlResponseV3ApiResponse**](EmbedSSOUrlResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed embed SSO url for Looker. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

