# pricemonitor_api_client.MonitoringSchedulesApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#delete_monitoring_schedule_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete monitoring schedule for contract [manufacturer]
[**delete_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#delete_monitoring_schedule_vendor_v3) | **DELETE** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete monitoring schedule for contract [vendor]
[**execute_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#execute_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger monitoring pipeline for schedule [manufacturer]
[**execute_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#execute_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger monitoring pipeline for schedule [vendor]
[**get_monitoring_schedules_manufacturer_v3**](MonitoringSchedulesApi.md#get_monitoring_schedules_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Get all monitoring schedules for contract [manufacturer]
[**get_monitoring_schedules_vendor_v3**](MonitoringSchedulesApi.md#get_monitoring_schedules_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Get all monitoring schedules for contract [vendor]
[**post_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#post_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Add monitoring schedule for contract [manufacturer]
[**post_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#post_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Add monitoring schedule for contract
[**put_monitoring_schedule_manufacturer_v3**](MonitoringSchedulesApi.md#put_monitoring_schedule_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update monitoring schedule for contract [manufacturer]
[**put_monitoring_schedule_vendor_v3**](MonitoringSchedulesApi.md#put_monitoring_schedule_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update monitoring schedule for contract [vendor]


# **delete_monitoring_schedule_manufacturer_v3**
> ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)

Delete monitoring schedule for contract [manufacturer]

Delete a monitoring schedule for a given manufacturer contract.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule

    try:
        # Delete monitoring schedule for contract [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule

    try:
        # Delete monitoring schedule for contract [manufacturer]
        api_response = api_instance.delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->delete_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **schedule_id** | **int**| Unique identifier of a monitoring schedule | 

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

Delete monitoring schedule for contract [vendor]

Delete a monitoring schedule for a given vendor contract.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule

    try:
        # Delete monitoring schedule for contract [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule

    try:
        # Delete monitoring schedule for contract [vendor]
        api_response = api_instance.delete_monitoring_schedule_vendor_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->delete_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **schedule_id** | **int**| Unique identifier of a monitoring schedule | 

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

Trigger monitoring pipeline for schedule [manufacturer]

Trigger a monitoring pipeline task for a manufacturer for a configured monitoring schedule.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
trigger_follow_up_task = True # bool | Flag to trigger follow-up tasks once the current task is completed (optional) (default to True)

    try:
        # Trigger monitoring pipeline for schedule [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
trigger_follow_up_task = True # bool | Flag to trigger follow-up tasks once the current task is completed (optional) (default to True)

    try:
        # Trigger monitoring pipeline for schedule [manufacturer]
        api_response = api_instance.execute_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->execute_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **schedule_id** | **int**| Unique identifier of a monitoring schedule | 
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
**200** | Monitoring task was successfully created and is executing |  -  |
**404** | Couldn&#39;t find any monitoring schedules for given schedule id. No monitoring task was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_monitoring_schedule_vendor_v3**
> EmptyApiResponse execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)

Trigger monitoring pipeline for schedule [vendor]

Trigger a monitoring pipeline task for a vendor for a configured monitoring schedule.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
trigger_follow_up_task = True # bool | Flag to trigger follow-up tasks once the current task is completed (optional) (default to True)

    try:
        # Trigger monitoring pipeline for schedule [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
trigger_follow_up_task = True # bool | Flag to trigger follow-up tasks once the current task is completed (optional) (default to True)

    try:
        # Trigger monitoring pipeline for schedule [vendor]
        api_response = api_instance.execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->execute_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **schedule_id** | **int**| Unique identifier of a monitoring schedule | 
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
**200** | Monitoring task was successfully created and is executing |  -  |
**404** | Couldn&#39;t find any monitoring schedules for given schedule id. No monitoring task was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_schedules_manufacturer_v3**
> GetMonitoringSchedulesApiResponse get_monitoring_schedules_manufacturer_v3(contract_id)

Get all monitoring schedules for contract [manufacturer]

Get all the monitoring schedules for a specified manufacturer contract.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all monitoring schedules for contract [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all monitoring schedules for contract [manufacturer]
        api_response = api_instance.get_monitoring_schedules_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->get_monitoring_schedules_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

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

Get all monitoring schedules for contract [vendor]

Get all the monitoring schedules for a specified vendor contract.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all monitoring schedules for contract [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all monitoring schedules for contract [vendor]
        api_response = api_instance.get_monitoring_schedules_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->get_monitoring_schedules_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

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

Add monitoring schedule for contract [manufacturer]

Add a monitoring schedule for a given manufacturer contract.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add monitoring schedule for contract [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add monitoring schedule for contract [manufacturer]
        api_response = api_instance.post_monitoring_schedule_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->post_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Add monitoring schedule for contract

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add monitoring schedule for contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add monitoring schedule for contract
        api_response = api_instance.post_monitoring_schedule_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->post_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Update monitoring schedule for contract [manufacturer]

Update a monitoring schedule for a given manufacturer contract.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update monitoring schedule for contract [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update monitoring schedule for contract [manufacturer]
        api_response = api_instance.put_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->put_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **schedule_id** | **int**| Unique identifier of a monitoring schedule | 
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

Update monitoring schedule for contract [vendor]

Update a monitoring schedule for a given vendor contract.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update monitoring schedule for contract [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
schedule_id = 123 # int | Unique identifier of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update monitoring schedule for contract [vendor]
        api_response = api_instance.put_monitoring_schedule_vendor_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitoringSchedulesApi->put_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **schedule_id** | **int**| Unique identifier of a monitoring schedule | 
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

