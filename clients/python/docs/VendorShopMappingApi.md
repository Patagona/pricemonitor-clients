# pricemonitor_api_client.VendorShopMappingApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vendor_shop_mapping_manufacturer_v3**](VendorShopMappingApi.md#delete_vendor_shop_mapping_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Delete a vendor and associated shops for a given contract.
[**get_vendor_shop_mapping_manufacturer_v3**](VendorShopMappingApi.md#get_vendor_shop_mapping_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Get vendor along with their associated shop for given vendor id and contract.
[**get_vendor_shop_mappings_manufacturer_v3**](VendorShopMappingApi.md#get_vendor_shop_mappings_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/vendors | Get all the vendors along with their associated shops for a specified contract.
[**post_vendor_shop_mapping_manufacturer_v3**](VendorShopMappingApi.md#post_vendor_shop_mapping_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/vendors | Add a new vendor for a given contract and associate shops with the given vendor.
[**put_vendor_shop_mapping_manufacturer_v3**](VendorShopMappingApi.md#put_vendor_shop_mapping_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Update an existing vendor for a given contract and associate shops with the given vendor.


# **delete_vendor_shop_mapping_manufacturer_v3**
> ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse delete_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)

Delete a vendor and associated shops for a given contract.

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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Delete a vendor and associated shops for a given contract.
        api_response = api_instance.delete_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->delete_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Delete a vendor and associated shops for a given contract.
        api_response = api_instance.delete_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->delete_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor_id** | **int**| ID of vendor shop mapping | 

### Return type

[**ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse**](ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A vendor and associated shops have been deleted successfully. |  -  |
**404** | Specified vendor does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_shop_mapping_manufacturer_v3**
> VendorShopMappingV3ApiResponse get_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)

Get vendor along with their associated shop for given vendor id and contract.

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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Get vendor along with their associated shop for given vendor id and contract.
        api_response = api_instance.get_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->get_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Get vendor along with their associated shop for given vendor id and contract.
        api_response = api_instance.get_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->get_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor_id** | **int**| ID of vendor shop mapping | 

### Return type

[**VendorShopMappingV3ApiResponse**](VendorShopMappingV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get vendor along with their associated shop for given vendor id and contract. |  -  |
**404** | Vendor doesn&#39;t exist for given vendor id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_shop_mappings_manufacturer_v3**
> GetVendorShopMappingsApiResponse get_vendor_shop_mappings_manufacturer_v3(contract_id)

Get all the vendors along with their associated shops for a specified contract.

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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the vendors along with their associated shops for a specified contract.
        api_response = api_instance.get_vendor_shop_mappings_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->get_vendor_shop_mappings_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the vendors along with their associated shops for a specified contract.
        api_response = api_instance.get_vendor_shop_mappings_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->get_vendor_shop_mappings_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetVendorShopMappingsApiResponse**](GetVendorShopMappingsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of vendors along with their associated shops. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vendor_shop_mapping_manufacturer_v3**
> VendorShopMappingV3ApiResponse post_vendor_shop_mapping_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)

Add a new vendor for a given contract and associate shops with the given vendor.

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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for creating a new vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Add a new vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.post_vendor_shop_mapping_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->post_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for creating a new vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Add a new vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.post_vendor_shop_mapping_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->post_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3** | [**ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3**](ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3.md)| Request body for creating a new vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. | [optional] 

### Return type

[**VendorShopMappingV3ApiResponse**](VendorShopMappingV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor shop mapping has been successfully created. |  -  |
**400** | The specified vendor name is empty. Or the specified shops are empty. |  -  |
**409** | The specified vendor name already exists in our system. |  -  |
**422** | The specified shops do not exist in our system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vendor_shop_mapping_manufacturer_v3**
> VendorShopMappingV3ApiResponse put_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)

Update an existing vendor for a given contract and associate shops with the given vendor.

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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for updating an existing vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Update an existing vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.put_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->put_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.VendorShopMappingApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for updating an existing vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Update an existing vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.put_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VendorShopMappingApi->put_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor_id** | **int**| ID of vendor shop mapping | 
 **com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3** | [**ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3**](ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3.md)| Request body for updating an existing vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. | [optional] 

### Return type

[**VendorShopMappingV3ApiResponse**](VendorShopMappingV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor shop mapping has been successfully updated. |  -  |
**400** | The specified vendor name is empty. Or the specified shops are empty. |  -  |
**409** | The specified vendor name already exists in our system. |  -  |
**422** | The specified shops do not exist in our system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

