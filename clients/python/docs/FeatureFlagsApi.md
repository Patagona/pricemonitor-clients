# pricemonitor_api_client.FeatureFlagsApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feature_flag**](FeatureFlagsApi.md#create_feature_flag) | **POST** /controlpanel/api/feature-flags | Create feature flag
[**delete_feature_flag**](FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /controlpanel/api/feature-flags/{key} | Delete feature flag
[**get_all_feature_flags**](FeatureFlagsApi.md#get_all_feature_flags) | **GET** /controlpanel/api/feature-flags | Get all feature flags
[**get_feature_flag_by_key**](FeatureFlagsApi.md#get_feature_flag_by_key) | **GET** /controlpanel/api/feature-flags/{key} | Get feature flag by key
[**update_feature_flag**](FeatureFlagsApi.md#update_feature_flag) | **PUT** /controlpanel/api/feature-flags/{key} | Update feature flag


# **create_feature_flag**
> CreateFeatureFlagApiResponse create_feature_flag(com_patagona_pricemonitor_share_api_post_feature_flag_request)

Create feature flag

**🔒 INTERNAL:** Creates a new feature flag in the system.  Feature flags must have a unique key that follows the pattern `[a-zA-Z0-9._-]+` and cannot exceed 128 characters in length. 

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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    com_patagona_pricemonitor_share_api_post_feature_flag_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostFeatureFlagRequest() # ComPatagonaPricemonitorShareApiPostFeatureFlagRequest | The feature flag to be created

    try:
        # Create feature flag
        api_response = api_instance.create_feature_flag(com_patagona_pricemonitor_share_api_post_feature_flag_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->create_feature_flag: %s\n" % e)
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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    com_patagona_pricemonitor_share_api_post_feature_flag_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostFeatureFlagRequest() # ComPatagonaPricemonitorShareApiPostFeatureFlagRequest | The feature flag to be created

    try:
        # Create feature flag
        api_response = api_instance.create_feature_flag(com_patagona_pricemonitor_share_api_post_feature_flag_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->create_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_feature_flag_request** | [**ComPatagonaPricemonitorShareApiPostFeatureFlagRequest**](ComPatagonaPricemonitorShareApiPostFeatureFlagRequest.md)| The feature flag to be created | 

### Return type

[**CreateFeatureFlagApiResponse**](CreateFeatureFlagApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feature flag created successfully |  -  |
**400** | Request validation failed. Common reasons include: - Invalid flag key format (must be alphanumeric, dot, underscore, or dash) - Flag key already exists - Flag name is empty or too long - Description exceeds maximum length  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_flag**
> EmptyApiResponse delete_feature_flag(key)

Delete feature flag

**🔒 INTERNAL:** Deletes a feature flag from the system (soft delete).  The feature flag is marked as deleted but preserved in the database for audit purposes. Once deleted, the flag key becomes unavailable for new flags. 

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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    key = 'api.v2.enabled' # str | Feature flag key identifier

    try:
        # Delete feature flag
        api_response = api_instance.delete_feature_flag(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->delete_feature_flag: %s\n" % e)
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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    key = 'api.v2.enabled' # str | Feature flag key identifier

    try:
        # Delete feature flag
        api_response = api_instance.delete_feature_flag(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->delete_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Feature flag key identifier | 

### Return type

[**EmptyApiResponse**](EmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feature flag deleted successfully |  -  |
**404** | Feature flag with the specified key was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_feature_flags**
> GetAllFeatureFlagsApiResponse get_all_feature_flags()

Get all feature flags

**🔒 INTERNAL:** Retrieves a list of all feature flags configured in the system.  Feature flags are used to control the availability of application features and can be managed through the control panel interface. 

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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    
    try:
        # Get all feature flags
        api_response = api_instance.get_all_feature_flags()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_all_feature_flags: %s\n" % e)
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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    
    try:
        # Get all feature flags
        api_response = api_instance.get_all_feature_flags()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_all_feature_flags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAllFeatureFlagsApiResponse**](GetAllFeatureFlagsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all feature flags |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_by_key**
> GetFeatureFlagByKeyApiResponse get_feature_flag_by_key(key)

Get feature flag by key

**🔒 INTERNAL:** Retrieves a specific feature flag by its key.  Returns the feature flag configuration including metadata such as creation and update timestamps. 

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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    key = 'api.v2.enabled' # str | Feature flag key identifier

    try:
        # Get feature flag by key
        api_response = api_instance.get_feature_flag_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_by_key: %s\n" % e)
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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    key = 'api.v2.enabled' # str | Feature flag key identifier

    try:
        # Get feature flag by key
        api_response = api_instance.get_feature_flag_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Feature flag key identifier | 

### Return type

[**GetFeatureFlagByKeyApiResponse**](GetFeatureFlagByKeyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feature flag details retrieved successfully |  -  |
**404** | Feature flag with the specified key was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feature_flag**
> UpdateFeatureFlagApiResponse update_feature_flag(key, com_patagona_pricemonitor_share_api_put_feature_flag_request)

Update feature flag

**🔒 INTERNAL:** Updates an existing feature flag's name and description.  The feature flag key cannot be changed after creation. Only the display name and description can be updated. 

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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    key = 'api.v2.enabled' # str | Feature flag key identifier
com_patagona_pricemonitor_share_api_put_feature_flag_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutFeatureFlagRequest() # ComPatagonaPricemonitorShareApiPutFeatureFlagRequest | The feature flag updates to be applied

    try:
        # Update feature flag
        api_response = api_instance.update_feature_flag(key, com_patagona_pricemonitor_share_api_put_feature_flag_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->update_feature_flag: %s\n" % e)
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
    api_instance = pricemonitor_api_client.FeatureFlagsApi(api_client)
    key = 'api.v2.enabled' # str | Feature flag key identifier
com_patagona_pricemonitor_share_api_put_feature_flag_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutFeatureFlagRequest() # ComPatagonaPricemonitorShareApiPutFeatureFlagRequest | The feature flag updates to be applied

    try:
        # Update feature flag
        api_response = api_instance.update_feature_flag(key, com_patagona_pricemonitor_share_api_put_feature_flag_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeatureFlagsApi->update_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Feature flag key identifier | 
 **com_patagona_pricemonitor_share_api_put_feature_flag_request** | [**ComPatagonaPricemonitorShareApiPutFeatureFlagRequest**](ComPatagonaPricemonitorShareApiPutFeatureFlagRequest.md)| The feature flag updates to be applied | 

### Return type

[**UpdateFeatureFlagApiResponse**](UpdateFeatureFlagApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feature flag updated successfully |  -  |
**400** | Request validation failed. Common reasons include: - Flag name is empty or too long - Description exceeds maximum length  |  -  |
**404** | Feature flag with the specified key was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

