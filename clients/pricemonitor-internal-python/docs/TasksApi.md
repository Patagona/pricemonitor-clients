# openapi_client.TasksApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /api/1/{contractId}/tasks | 
[**create_task_manufacturer_v2**](TasksApi.md#create_task_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/tasks | 
[**create_task_vendor_v2**](TasksApi.md#create_task_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/tasks | 
[**get_task**](TasksApi.md#get_task) | **GET** /api/1/{contractId}/tasks/{taskId} | 
[**get_task_data_manufacturer_v2**](TasksApi.md#get_task_data_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks/{taskId}/data | 
[**get_task_data_vendor_v2**](TasksApi.md#get_task_data_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/tasks/{taskId}/data | 
[**get_task_manufacturer_v2**](TasksApi.md#get_task_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks/{taskId} | 
[**get_task_state**](TasksApi.md#get_task_state) | **GET** /api/1/{contractId}/tasks/{taskId}/state | 
[**get_task_vendor_v2**](TasksApi.md#get_task_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/tasks/{taskId} | Find task by ID
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /api/1/{contractId}/tasks | 
[**get_tasks_manufacturer_v2**](TasksApi.md#get_tasks_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks | 
[**get_tasks_vendor_v2**](TasksApi.md#get_tasks_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/tasks | Find all tasks
[**update_task_vendor_v2**](TasksApi.md#update_task_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/tasks/{taskId} | 


# **create_task**
> object create_task(contract_id, body=body)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_task(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_manufacturer_v2**
> GenericTaskWithUrl create_task_manufacturer_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)



Create a new task

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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_create_task_body_v2 = openapi_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_task_manufacturer_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->create_task_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_create_task_body_v2** | [**ComPatagonaPricemonitorShareApiCreateTaskBodyV2**](ComPatagonaPricemonitorShareApiCreateTaskBodyV2.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

[**GenericTaskWithUrl**](GenericTaskWithUrl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new task was successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_vendor_v2**
> object create_task_vendor_v2(contract_id, body=body)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_task_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->create_task_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> object get_task(contract_id, task_id)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_data_manufacturer_v2**
> object get_task_data_manufacturer_v2(contract_id, task_id)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_data_manufacturer_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task_data_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payload data of the requested task is returned |  -  |
**404** | The task with the given ID could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_data_vendor_v2**
> object get_task_data_vendor_v2(contract_id, task_id)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_data_vendor_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task_data_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_manufacturer_v2**
> GenericTask get_task_manufacturer_v2(contract_id, task_id)



Get the task designated by the taskId parameter

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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_manufacturer_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

[**GenericTask**](GenericTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The task was found and is returned |  -  |
**404** | No task with given taskId was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_state**
> object get_task_state(contract_id, task_id)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_state(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_vendor_v2**
> TaskWithContractResourceApiResponse get_task_vendor_v2(contract_id, task_id)

Find task by ID

Returns a task, associated with a certain contract and identified by its ID

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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | Id of the task

    try:
        # Find task by ID
        api_response = api_instance.get_task_vendor_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**| Id of the task | 

### Return type

[**TaskWithContractResourceApiResponse**](TaskWithContractResourceApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> object get_tasks(contract_id, tasks, attributes, limit, task_type=task_type)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
tasks = 'tasks_example' # str | 
attributes = 'attributes_example' # str | 
limit = 56 # int | 
task_type = 'task_type_example' # str |  (optional)

    try:
        api_response = api_instance.get_tasks(contract_id, tasks, attributes, limit, task_type=task_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **tasks** | **str**|  | 
 **attributes** | **str**|  | 
 **limit** | **int**|  | 
 **task_type** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_manufacturer_v2**
> list[GenericTask] get_tasks_manufacturer_v2(contract_id, task_type_filter, task_state, limit, include_failures, task_ids_filter=task_ids_filter, min_creation_date=min_creation_date, max_creation_date=max_creation_date)



Returns a list of task objects for the given contract

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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_type_filter = ['task_type_filter_example'] # list[str] | A list of task types to filter for
task_state = ['task_state_example'] # list[str] | A list of task states to filter for
limit = 100 # int | The maximum number of tasks returned (default to 100)
include_failures = True # bool | Include failed tasks (default to True)
task_ids_filter = 'task_ids_filter_example' # str | Comma separated list of task IDs to filter for (optional)
min_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Ignore all tasks created earlier than this date (ISO 8601) (optional)
max_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Ignore all tasks created later than this date (ISO 8601) (optional)

    try:
        api_response = api_instance.get_tasks_manufacturer_v2(contract_id, task_type_filter, task_state, limit, include_failures, task_ids_filter=task_ids_filter, min_creation_date=min_creation_date, max_creation_date=max_creation_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_tasks_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_type_filter** | [**list[str]**](str.md)| A list of task types to filter for | 
 **task_state** | [**list[str]**](str.md)| A list of task states to filter for | 
 **limit** | **int**| The maximum number of tasks returned | [default to 100]
 **include_failures** | **bool**| Include failed tasks | [default to True]
 **task_ids_filter** | **str**| Comma separated list of task IDs to filter for | [optional] 
 **min_creation_date** | **datetime**| Ignore all tasks created earlier than this date (ISO 8601) | [optional] 
 **max_creation_date** | **datetime**| Ignore all tasks created later than this date (ISO 8601) | [optional] 

### Return type

[**list[GenericTask]**](GenericTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tasks for the given contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_vendor_v2**
> list[TaskWithContractResourceApiResponse] get_tasks_vendor_v2(contract_id, task_ids_filter=task_ids_filter, task_type_filter=task_type_filter, limit=limit, include_failures=include_failures, task_state=task_state, min_creation_date=min_creation_date, max_creation_date=max_creation_date)

Find all tasks

The search can be narrowed down by providing the IDs of the tasks, separated by comma

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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_ids_filter = 'task_ids_filter_example' # str | Ids of the tasks (optional)
task_type_filter = 'task_type_filter_example' # str | Desired task type (optional)
limit = 100 # int | Maximal number of results (optional) (default to 100)
include_failures = True # bool | Flag whether to include failures in the response (optional) (default to True)
task_state = 'task_state_example' # str | Comma separated task state filter (optional)
min_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Oldest returned creation date in UTC (optional)
max_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Newest returned creation date in UTC (optional)

    try:
        # Find all tasks
        api_response = api_instance.get_tasks_vendor_v2(contract_id, task_ids_filter=task_ids_filter, task_type_filter=task_type_filter, limit=limit, include_failures=include_failures, task_state=task_state, min_creation_date=min_creation_date, max_creation_date=max_creation_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_tasks_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_ids_filter** | **str**| Ids of the tasks | [optional] 
 **task_type_filter** | **str**| Desired task type | [optional] 
 **limit** | **int**| Maximal number of results | [optional] [default to 100]
 **include_failures** | **bool**| Flag whether to include failures in the response | [optional] [default to True]
 **task_state** | **str**| Comma separated task state filter | [optional] 
 **min_creation_date** | **datetime**| Oldest returned creation date in UTC | [optional] 
 **max_creation_date** | **datetime**| Newest returned creation date in UTC | [optional] 

### Return type

[**list[TaskWithContractResourceApiResponse]**](TaskWithContractResourceApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_vendor_v2**
> object update_task_vendor_v2(contract_id, task_id, body=body)



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
    api_instance = openapi_client.TasksApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_task_vendor_v2(contract_id, task_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->update_task_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

