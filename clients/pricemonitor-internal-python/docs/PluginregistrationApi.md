# openapi_client.PluginregistrationApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_plugin_registration**](PluginregistrationApi.md#delete_plugin_registration) | **DELETE** /api/v3/vendor/contracts/{contractId}/plugin | Delete the plugin registration for given contract
[**get_plugin_registration**](PluginregistrationApi.md#get_plugin_registration) | **GET** /api/v3/vendor/contracts/{contractId}/plugin | Return the plugin registration for given contract
[**put_plugin_registration**](PluginregistrationApi.md#put_plugin_registration) | **PUT** /api/v3/vendor/contracts/{contractId}/plugin | Create and/or update the plugin registration for given contract


# **delete_plugin_registration**
> PluginRegistrationEmptyApiResponse delete_plugin_registration(contract_id)

Delete the plugin registration for given contract

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginregistrationApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Delete the plugin registration for given contract
        api_response = api_instance.delete_plugin_registration(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginregistrationApi->delete_plugin_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**PluginRegistrationEmptyApiResponse**](PluginRegistrationEmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin registration for given contract deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_registration**
> PluginRegistrationApiResponse get_plugin_registration(contract_id)

Return the plugin registration for given contract

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginregistrationApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Return the plugin registration for given contract
        api_response = api_instance.get_plugin_registration(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginregistrationApi->get_plugin_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**PluginRegistrationApiResponse**](PluginRegistrationApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a plugin registration for given contract. |  -  |
**404** | Given plugin registration does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_plugin_registration**
> PluginRegistrationEmptyApiResponse put_plugin_registration(contract_id, put_plugin_registration_request)

Create and/or update the plugin registration for given contract

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginregistrationApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
put_plugin_registration_request = openapi_client.PutPluginRegistrationRequest() # PutPluginRegistrationRequest | 

    try:
        # Create and/or update the plugin registration for given contract
        api_response = api_instance.put_plugin_registration(contract_id, put_plugin_registration_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginregistrationApi->put_plugin_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **put_plugin_registration_request** | [**PutPluginRegistrationRequest**](PutPluginRegistrationRequest.md)|  | 

### Return type

[**PluginRegistrationEmptyApiResponse**](PluginRegistrationEmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin registration for given contract stored successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

