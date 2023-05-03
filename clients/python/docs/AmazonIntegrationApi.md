# pricemonitor_api_client.AmazonIntegrationApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authorization_status_vendor_v3**](AmazonIntegrationApi.md#get_authorization_status_vendor_v3) | **GET** /api/v3/companies/{companyId}/amazon/authorization/status | Get OAuth authorization status for customer&#39;s Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 
[**post_activate_marketplace_vendor_v3**](AmazonIntegrationApi.md#post_activate_marketplace_vendor_v3) | **POST** /api/v3/companies/{companyId}/amazon/marketplace | Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer&#39;s Amazon shop. 
[**post_authorize_seller_vendor_v3**](AmazonIntegrationApi.md#post_authorize_seller_vendor_v3) | **POST** /api/v3/companies/{companyId}/amazon/authorization | Set up an OAuth authorization for a customer&#39;s Amazon Seller Central account. It establishes a connection between our system and the customer&#39;s Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer&#39;s Amazon shop, allowing them to benefit from our price recommendations. 


# **get_authorization_status_vendor_v3**
> GetAuthorizationStatusResponseV3ApiResponse get_authorization_status_vendor_v3(company_id)

Get OAuth authorization status for customer's Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 

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
    api_instance = pricemonitor_api_client.AmazonIntegrationApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        # Get OAuth authorization status for customer's Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 
        api_response = api_instance.get_authorization_status_vendor_v3(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmazonIntegrationApi->get_authorization_status_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AmazonIntegrationApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        # Get OAuth authorization status for customer's Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 
        api_response = api_instance.get_authorization_status_vendor_v3(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmazonIntegrationApi->get_authorization_status_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 

### Return type

[**GetAuthorizationStatusResponseV3ApiResponse**](GetAuthorizationStatusResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization status of a customer on Amazon. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_activate_marketplace_vendor_v3**
> PostActivateMarketplaceResponseV3ApiResponse post_activate_marketplace_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3=com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3)

Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer's Amazon shop. 

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
    api_instance = pricemonitor_api_client.AmazonIntegrationApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3() # ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3 | Marketplace of a customer to be activated. (optional)

    try:
        # Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer's Amazon shop. 
        api_response = api_instance.post_activate_marketplace_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3=com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmazonIntegrationApi->post_activate_marketplace_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AmazonIntegrationApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3() # ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3 | Marketplace of a customer to be activated. (optional)

    try:
        # Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer's Amazon shop. 
        api_response = api_instance.post_activate_marketplace_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3=com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmazonIntegrationApi->post_activate_marketplace_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 
 **com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3** | [**ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3**](ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3.md)| Marketplace of a customer to be activated. | [optional] 

### Return type

[**PostActivateMarketplaceResponseV3ApiResponse**](PostActivateMarketplaceResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully activated marketplace of a customer in our system. |  -  |
**400** | - Specified marketplace already activated. - Invalid marketplace country code is specified. - Given company is not registered with our system. One must register his seller central account with our system.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_authorize_seller_vendor_v3**
> PostAuthorizeSellerResponseV3ApiResponse post_authorize_seller_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3=com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3)

Set up an OAuth authorization for a customer's Amazon Seller Central account. It establishes a connection between our system and the customer's Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer's Amazon shop, allowing them to benefit from our price recommendations. 

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
    api_instance = pricemonitor_api_client.AmazonIntegrationApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3() # ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3 | Customer's Amazon seller central account to be authorized. (optional)

    try:
        # Set up an OAuth authorization for a customer's Amazon Seller Central account. It establishes a connection between our system and the customer's Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer's Amazon shop, allowing them to benefit from our price recommendations. 
        api_response = api_instance.post_authorize_seller_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3=com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmazonIntegrationApi->post_authorize_seller_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AmazonIntegrationApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3() # ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3 | Customer's Amazon seller central account to be authorized. (optional)

    try:
        # Set up an OAuth authorization for a customer's Amazon Seller Central account. It establishes a connection between our system and the customer's Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer's Amazon shop, allowing them to benefit from our price recommendations. 
        api_response = api_instance.post_authorize_seller_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3=com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmazonIntegrationApi->post_authorize_seller_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 
 **com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3** | [**ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3**](ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3.md)| Customer&#39;s Amazon seller central account to be authorized. | [optional] 

### Return type

[**PostAuthorizeSellerResponseV3ApiResponse**](PostAuthorizeSellerResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully authorized customer&#39;s Amazon seller central account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

