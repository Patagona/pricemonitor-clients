# pricemonitor_api_client.DomainsApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_domains_v2**](DomainsApi.md#get_all_domains_v2) | **GET** /api/2/domains | Gets a list of all available domains (V2)
[**get_all_domains_v3**](DomainsApi.md#get_all_domains_v3) | **GET** /api/v3/domains | Get all available domains


# **get_all_domains_v2**
> list[str] get_all_domains_v2()

Gets a list of all available domains (V2)

Gets a list of all available domains for monitoring.

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
    api_instance = pricemonitor_api_client.DomainsApi(api_client)
    
    try:
        # Gets a list of all available domains (V2)
        api_response = api_instance.get_all_domains_v2()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->get_all_domains_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DomainsApi(api_client)
    
    try:
        # Gets a list of all available domains (V2)
        api_response = api_instance.get_all_domains_v2()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->get_all_domains_v2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all available domains for monitoring. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_domains_v3**
> GetAllDomainsV3ApiResponse get_all_domains_v3()

Get all available domains

Retrieves all domains supported by the system for market data collection.  Each domain includes: - Available offer sources for market data collection - Configuration parameters  **Note:** Only domains with the `DEFAULT_MONITORING` offer source are supported out-of-the-box by the monitoring pipeline. 

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
    api_instance = pricemonitor_api_client.DomainsApi(api_client)
    
    try:
        # Get all available domains
        api_response = api_instance.get_all_domains_v3()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->get_all_domains_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DomainsApi(api_client)
    
    try:
        # Get all available domains
        api_response = api_instance.get_all_domains_v3()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->get_all_domains_v3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAllDomainsV3ApiResponse**](GetAllDomainsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all supported domains with their configurations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

