# pricemonitor_api_client.MonitoringSchedulesApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#delete_monitoring_schedule_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete a monitoring schedule for a given contract.
[**delete_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#delete_monitoring_schedule_vendor_v3) | **DELETE** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete a monitoring schedule for a given contract.
[**execute_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#execute_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule
[**execute_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#execute_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger a monitoring pipeline task for vendor for configured monitoring schedule
[**get_monitoring_schedules_manufacturer_v3**](MonitoringSchedulesApi.md#get_monitoring_schedules_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Get all the monitoring schedules for a specified contract.
[**get_monitoring_schedules_vendor_v3**](MonitoringSchedulesApi.md#get_monitoring_schedules_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Get all the monitoring schedules for a specified contract.
[**post_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#post_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Add a monitoring schedule for a given contract.
[**post_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#post_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Add a monitoring schedule for a given contract.
[**put_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#put_monitoring_schedule_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update a monitoring schedule for a given contract.
[**put_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#put_monitoring_schedule_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update a monitoring schedule for a given contract.


# **delete_monitoring_schedule_manufacturer_v3**
> ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)

Delete a monitoring schedule for a given contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->delete_monitoring_schedule_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->delete_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 

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
**200** | Monitoring schedule has been deleted successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitoring_schedule_vendor_v3**
> ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse delete_monitoring_schedule_vendor_v3(contract_id, schedule_id)

Delete a monitoring schedule for a given contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_vendor_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->delete_monitoring_schedule_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_vendor_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->delete_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 

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
**200** | Monitoring schedule has been deleted successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |
**503** | Monitoring schedule could not be deleted due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_monitoring_schedule_manufacturer_v3**
> EmptyApiResponse execute_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)

Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->execute_monitoring_schedule_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->execute_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **trigger_follow_up_task** | **bool**|  | [optional] 

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
**200** | Monitoring task was successfully created and is executing |  -  |
**404** | Couldn&#39;t find any monitoring schedules for given schedule id. No monitoring task was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_monitoring_schedule_vendor_v3**
> EmptyApiResponse execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)

Trigger a monitoring pipeline task for vendor for configured monitoring schedule

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for vendor for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->execute_monitoring_schedule_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for vendor for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->execute_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **trigger_follow_up_task** | **bool**|  | [optional] 

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
**200** | Monitoring task was successfully created and is executing |  -  |
**404** | Couldn&#39;t find any monitoring schedules for given schedule id. No monitoring task was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_schedules_manufacturer_v3**
> GetMonitoringSchedulesApiResponse get_monitoring_schedules_manufacturer_v3(contract_id)

Get all the monitoring schedules for a specified contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->get_monitoring_schedules_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->get_monitoring_schedules_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetMonitoringSchedulesApiResponse**](GetMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of monitoring schedules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_schedules_vendor_v3**
> GetMonitoringSchedulesApiResponse get_monitoring_schedules_vendor_v3(contract_id)

Get all the monitoring schedules for a specified contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->get_monitoring_schedules_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->get_monitoring_schedules_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetMonitoringSchedulesApiResponse**](GetMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of monitoring schedules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_monitoring_schedule_manufacturer_v3**
> PutMonitoringSchedulesApiResponse post_monitoring_schedule_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Add a monitoring schedule for a given contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->post_monitoring_schedule_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->post_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for creating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring schedule has been created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_monitoring_schedule_vendor_v3**
> PutMonitoringSchedulesApiResponse post_monitoring_schedule_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Add a monitoring schedule for a given contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->post_monitoring_schedule_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->post_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for creating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring schedule has been created successfully. |  -  |
**503** | Monitoring schedule could not be created due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_schedule_manufacturer_v3**
> PutMonitoringSchedulesApiResponse put_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Update a monitoring schedule for a given contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->put_monitoring_schedule_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->put_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for updating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Monitoring schedule has been updated successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_schedule_vendor_v3**
> PutMonitoringSchedulesApiResponse put_monitoring_schedule_vendor_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Update a monitoring schedule for a given contract.

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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_vendor_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->put_monitoring_schedule_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.MonitoringSchedulesApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_vendor_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->put_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for updating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Monitoring schedule has been updated successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |
**503** | Monitoring schedule could not be updated due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

