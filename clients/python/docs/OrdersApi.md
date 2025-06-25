# pricemonitor_api_client.OrdersApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_orders**](OrdersApi.md#delete_orders) | **DELETE** /api/v3/vendor/contracts/{contractId}/orders | Delete all orders
[**delete_orders_by_query_vendor_v3**](OrdersApi.md#delete_orders_by_query_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/orders/delete/query | Delete orders by query
[**get_orders_count_by_portal_by_contract**](OrdersApi.md#get_orders_count_by_portal_by_contract) | **GET** /api/1/{contractId}/products/orderscountbyportal | Get orders count by portal
[**get_orders_vendor_v3**](OrdersApi.md#get_orders_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/orders | Get all orders
[**post_orders**](OrdersApi.md#post_orders) | **POST** /api/2/v/contracts/{contractId}/orders | Add orders in bulk
[**put_orders_v3**](OrdersApi.md#put_orders_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/orders | PUT orders in bulk
[**query_orders_stats_vendor_v3**](OrdersApi.md#query_orders_stats_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/orders/stats/query | Query order statistics per product


# **delete_orders**
> DeletedItemsApiResponse delete_orders(contract_id)

Delete all orders

Delete all orders for this contract.

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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Delete all orders
        api_response = api_instance.delete_orders(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->delete_orders: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Delete all orders
        api_response = api_instance.delete_orders(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->delete_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

### Return type

[**DeletedItemsApiResponse**](DeletedItemsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted all orders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_orders_by_query_vendor_v3**
> DeletedItemsApiResponse delete_orders_by_query_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_delete_orders_by_query_request_v3)

Delete orders by query

This endpoint can be used to delete customer orders by an order query

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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_delete_orders_by_query_request_v3 = {"orders":[{"orderId":"123","creationDate":"2023-11-01T08:00:00Z"}]} # ComPatagonaPricemonitorShareApiDeleteOrdersByQueryRequestV3 | The request body should contain a list of order queries. Each query should contain an order id and creation date.  The allowed query pattern is structured as follows:  { <br> &nbsp;&nbsp;\"orders\": [ <br> &nbsp;&nbsp;&nbsp;{ <br> &nbsp;&nbsp;&nbsp;&nbsp;\"orderId\": ${orderId}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"creationDate\": ${creationDate} <br> &nbsp;&nbsp;} <br> &nbsp;&nbsp;&nbsp;] <br> } <br> <br> 

    try:
        # Delete orders by query
        api_response = api_instance.delete_orders_by_query_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_delete_orders_by_query_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->delete_orders_by_query_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_delete_orders_by_query_request_v3 = {"orders":[{"orderId":"123","creationDate":"2023-11-01T08:00:00Z"}]} # ComPatagonaPricemonitorShareApiDeleteOrdersByQueryRequestV3 | The request body should contain a list of order queries. Each query should contain an order id and creation date.  The allowed query pattern is structured as follows:  { <br> &nbsp;&nbsp;\"orders\": [ <br> &nbsp;&nbsp;&nbsp;{ <br> &nbsp;&nbsp;&nbsp;&nbsp;\"orderId\": ${orderId}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"creationDate\": ${creationDate} <br> &nbsp;&nbsp;} <br> &nbsp;&nbsp;&nbsp;] <br> } <br> <br> 

    try:
        # Delete orders by query
        api_response = api_instance.delete_orders_by_query_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_delete_orders_by_query_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->delete_orders_by_query_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_delete_orders_by_query_request_v3** | [**ComPatagonaPricemonitorShareApiDeleteOrdersByQueryRequestV3**](ComPatagonaPricemonitorShareApiDeleteOrdersByQueryRequestV3.md)| The request body should contain a list of order queries. Each query should contain an order id and creation date.  The allowed query pattern is structured as follows:  { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;orders\&quot;: [ &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;{ &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;orderId\&quot;: ${orderId}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;creationDate\&quot;: ${creationDate} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;] &lt;br&gt; } &lt;br&gt; &lt;br&gt;  | 

### Return type

[**DeletedItemsApiResponse**](DeletedItemsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the number of orders that have been deleted successfully  |  -  |
**400** | A &#x60;400&#x60; error is returned under the following conditions: - The request body JSON is unparsable. - The provided order queries exceeds 10,000.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_count_by_portal_by_contract**
> object get_orders_count_by_portal_by_contract(contract_id)

Get orders count by portal

Get the number of orders by portal for the given contract.

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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get orders count by portal
        api_response = api_instance.get_orders_count_by_portal_by_contract(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_orders_count_by_portal_by_contract: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get orders count by portal
        api_response = api_instance.get_orders_count_by_portal_by_contract(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_orders_count_by_portal_by_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_vendor_v3**
> object get_orders_vendor_v3(contract_id, start, limit, start_date=start_date, end_date=end_date)

Get all orders

Returns all orders for a given contract.

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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 56 # int | 
limit = 56 # int | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no lower time limit is considered.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no upper time limit is considered.  (optional)

    try:
        # Get all orders
        api_response = api_instance.get_orders_vendor_v3(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_orders_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 56 # int | 
limit = 56 # int | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no lower time limit is considered.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no upper time limit is considered.  (optional)

    try:
        # Get all orders
        api_response = api_instance.get_orders_vendor_v3(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_orders_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start** | **int**|  | 
 **limit** | **int**|  | 
 **start_date** | **datetime**| Timestamp of start of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no lower time limit is considered.  | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no upper time limit is considered.  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_orders**
> PostOrdersBulkApiResponse post_orders(contract_id, com_patagona_pricemonitor_share_api_post_customer_orders_request_v2)

Add orders in bulk

Imports multiple orders for a specific contract in a single operation.  This endpoint supports bulk order processing to efficiently manage large volumes of order data. All orders in the request are processed atomically. 

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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_customer_orders_request_v2 = {"version":"2","orders":[{"orderId":"ORDER-2024-001","origin":"webshop","referrer":"google","productMappings":[{"source":"itemId","target":"customerProductId"}],"items":[{"itemId":"ITEM-001","unitPrice":29.99,"quantity":2,"taxPercentage":19}],"creationDate":"2024-01-15T10:30:00Z","totalPrice":65.98,"shippingCosts":5.99,"currency":"EUR"}]} # ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2 | Orders to be imported, including order metadata and item details

    try:
        # Add orders in bulk
        api_response = api_instance.post_orders(contract_id, com_patagona_pricemonitor_share_api_post_customer_orders_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->post_orders: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_customer_orders_request_v2 = {"version":"2","orders":[{"orderId":"ORDER-2024-001","origin":"webshop","referrer":"google","productMappings":[{"source":"itemId","target":"customerProductId"}],"items":[{"itemId":"ITEM-001","unitPrice":29.99,"quantity":2,"taxPercentage":19}],"creationDate":"2024-01-15T10:30:00Z","totalPrice":65.98,"shippingCosts":5.99,"currency":"EUR"}]} # ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2 | Orders to be imported, including order metadata and item details

    try:
        # Add orders in bulk
        api_response = api_instance.post_orders(contract_id, com_patagona_pricemonitor_share_api_post_customer_orders_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->post_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_post_customer_orders_request_v2** | [**ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2**](ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2.md)| Orders to be imported, including order metadata and item details | 

### Return type

[**PostOrdersBulkApiResponse**](PostOrdersBulkApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders processed successfully (may include partial failures) |  -  |
**400** | Request validation failed. Common issues include: - Invalid order data format - Missing required fields - Invalid contract ID  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_orders_v3**
> PutItemsV3ApiResponse put_orders_v3(contract_id, com_patagona_pricemonitor_share_api_put_customer_orders_request_v3=com_patagona_pricemonitor_share_api_put_customer_orders_request_v3)

PUT orders in bulk

Saves orders in bulk. If an orderId was already used by this contract this order and all it's order-items will be overwritten.  - the `version` of the request body must be \"3\" - requests must not contain duplicated `orderId` - the number of orders in one request must not exceed 10,000 - each order must have at least one item - the `orders.items.itemId` fields should correspond to a `customerProductId` of a product definition inside   the contract 

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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_put_customer_orders_request_v3 = {"orders":[{"shippingCosts":5.9,"orderId":"2023-11_customer-a_001","items":[{"unitPrice":6.02,"itemId":"itemId","quantity":1,"taxPercentage":19}],"totalPrice":11.92,"origin":"Amazon.de","creationDate":"2023-11-23T11:20:21.034+01:00","currency":"EUR"}],"version":"3"} # ComPatagonaPricemonitorShareApiPutCustomerOrdersRequestV3 |  (optional)

    try:
        # PUT orders in bulk
        api_response = api_instance.put_orders_v3(contract_id, com_patagona_pricemonitor_share_api_put_customer_orders_request_v3=com_patagona_pricemonitor_share_api_put_customer_orders_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->put_orders_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_put_customer_orders_request_v3 = {"orders":[{"shippingCosts":5.9,"orderId":"2023-11_customer-a_001","items":[{"unitPrice":6.02,"itemId":"itemId","quantity":1,"taxPercentage":19}],"totalPrice":11.92,"origin":"Amazon.de","creationDate":"2023-11-23T11:20:21.034+01:00","currency":"EUR"}],"version":"3"} # ComPatagonaPricemonitorShareApiPutCustomerOrdersRequestV3 |  (optional)

    try:
        # PUT orders in bulk
        api_response = api_instance.put_orders_v3(contract_id, com_patagona_pricemonitor_share_api_put_customer_orders_request_v3=com_patagona_pricemonitor_share_api_put_customer_orders_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->put_orders_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_put_customer_orders_request_v3** | [**ComPatagonaPricemonitorShareApiPutCustomerOrdersRequestV3**](ComPatagonaPricemonitorShareApiPutCustomerOrdersRequestV3.md)|  | [optional] 

### Return type

[**PutItemsV3ApiResponse**](PutItemsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response provides the ids of the successfully imported orders |  -  |
**400** | Unable to add orders because of invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_orders_stats_vendor_v3**
> QueryOrderStatisticsV3ApiResponse query_orders_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_order_statistics_request_v3)

Query order statistics per product

This endpoint can be used to query order statistics grouped by product.

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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_order_statistics_request_v3 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-11-01T08:00:00Z","end":"2023-11-15T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOrderStatisticsRequestV3 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"customerProductId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000.  The allowed query pattern is structured as follows:  { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"range\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"end\": ${end} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> 

    try:
        # Query order statistics per product
        api_response = api_instance.query_orders_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_order_statistics_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->query_orders_stats_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OrdersApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_order_statistics_request_v3 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-11-01T08:00:00Z","end":"2023-11-15T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOrderStatisticsRequestV3 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"customerProductId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000.  The allowed query pattern is structured as follows:  { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"range\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"end\": ${end} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> 

    try:
        # Query order statistics per product
        api_response = api_instance.query_orders_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_order_statistics_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->query_orders_stats_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_post_order_statistics_request_v3** | [**ComPatagonaPricemonitorShareApiPostOrderStatisticsRequestV3**](ComPatagonaPricemonitorShareApiPostOrderStatisticsRequestV3.md)| The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \&quot;customerProductId\&quot;   - \&quot;productId\&quot; (Patagona&#39;s internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \&quot;customerProductId\&quot; for queries when a product query is utilized.  Pagination operates based on the provided products query. For chunked requests over a set of ids, it&#39;s straightforward to specify up to 10,000 customerProductId&#39;s in the query with pagination set at start: 0, limit: 10,000.  The allowed query pattern is structured as follows:  { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: ${start}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: ${limit} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;range\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: ${start}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;end\&quot;: ${end} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [${customerProductIds as a list of strings}] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt; &lt;br&gt;  | 

### Return type

[**QueryOrderStatisticsV3ApiResponse**](QueryOrderStatisticsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of order statistics per product. When a product has no sold items then no order statistics are returned for that product.  |  -  |
**400** | A &#x60;400&#x60; error is returned under the following conditions: - The request body JSON is unparsable. - An unsupported filter is provided. - The specified time range exceeds 30 days. - The pagination limit exceeds 10,000.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

