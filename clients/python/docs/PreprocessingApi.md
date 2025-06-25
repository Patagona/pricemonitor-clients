# pricemonitor_api_client.PreprocessingApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publish_preprocessing_task_vendor_v3**](PreprocessingApi.md#publish_preprocessing_task_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/tasks/preprocessing | Publish preprocessing task [vendor]


# **publish_preprocessing_task_vendor_v3**
> EmptyApiResponse publish_preprocessing_task_vendor_v3(retrospective_in_minutes, contract_id, trigger_follow_up_task=trigger_follow_up_task)

Publish preprocessing task [vendor]

Publish a preprocessing task for a vendor.

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
    api_instance = pricemonitor_api_client.PreprocessingApi(api_client)
    retrospective_in_minutes = 56 # int | The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10080
contract_id = 'qbcxvb' # str | Unique identifier of the contract
trigger_follow_up_task = True # bool | Flag to trigger follow-up tasks once the current task is completed (optional) (default to True)

    try:
        # Publish preprocessing task [vendor]
        api_response = api_instance.publish_preprocessing_task_vendor_v3(retrospective_in_minutes, contract_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PreprocessingApi->publish_preprocessing_task_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PreprocessingApi(api_client)
    retrospective_in_minutes = 56 # int | The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10080
contract_id = 'qbcxvb' # str | Unique identifier of the contract
trigger_follow_up_task = True # bool | Flag to trigger follow-up tasks once the current task is completed (optional) (default to True)

    try:
        # Publish preprocessing task [vendor]
        api_response = api_instance.publish_preprocessing_task_vendor_v3(retrospective_in_minutes, contract_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PreprocessingApi->publish_preprocessing_task_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrospective_in_minutes** | **int**| The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10080 | 
 **contract_id** | **str**| Unique identifier of the contract | 
 **trigger_follow_up_task** | **bool**| Flag to trigger follow-up tasks once the current task is completed | [optional] [default to True]

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
**200** | Preprocessing task created successfully |  -  |
**400** | - Invalid retrospective value. - No retrospective value is specified.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

