# pricemonitor_api_client.OrdersApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_vendor_contracts_contract_id_orders_stats_query_post**](OrdersApi.md#api_v3_vendor_contracts_contract_id_orders_stats_query_post) | **POST** /api/v3/vendor/contracts/{contractId}/orders/stats/query | Query order statistics per product
[**delete_orders**](OrdersApi.md#delete_orders) | **DELETE** /api/v3/vendor/contracts/{contractId}/orders | Delete all orders for this contract
[**get_orders_count_by_portal_by_contract**](OrdersApi.md#get_orders_count_by_portal_by_contract) | **GET** /api/1/{contractId}/products/orderscountbyportal | 
[**get_orders_vendor_v3**](OrdersApi.md#get_orders_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/orders | 
[**post_orders**](OrdersApi.md#post_orders) | **POST** /api/2/v/contracts/{contractId}/orders | Add orders in bulk


# **api_v3_vendor_contracts_contract_id_orders_stats_query_post**
> QueryOrderStatisticsV3ApiResponse api_v3_vendor_contracts_contract_id_orders_stats_query_post(contract_id, com_patagona_pricemonitor_share_api_post_order_statistics_request_v3)

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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_order_statistics_request_v3 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-11-01T08:00:00Z","end":"2023-11-15T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOrderStatisticsRequestV3 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"customerProductId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000.  The allowed query pattern is structured as follows:  { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"range\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"end\": ${end} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> 

    try:
        # Query order statistics per product
        api_response = api_instance.api_v3_vendor_contracts_contract_id_orders_stats_query_post(contract_id, com_patagona_pricemonitor_share_api_post_order_statistics_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->api_v3_vendor_contracts_contract_id_orders_stats_query_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_order_statistics_request_v3 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-11-01T08:00:00Z","end":"2023-11-15T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOrderStatisticsRequestV3 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"customerProductId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000.  The allowed query pattern is structured as follows:  { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"range\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"end\": ${end} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> 

    try:
        # Query order statistics per product
        api_response = api_instance.api_v3_vendor_contracts_contract_id_orders_stats_query_post(contract_id, com_patagona_pricemonitor_share_api_post_order_statistics_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->api_v3_vendor_contracts_contract_id_orders_stats_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **delete_orders**
> DeleteOrdersApiResponse delete_orders(contract_id)

Delete all orders for this contract

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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Delete all orders for this contract
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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Delete all orders for this contract
        api_response = api_instance.delete_orders(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->delete_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**DeleteOrdersApiResponse**](DeleteOrdersApiResponse.md)

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

# **get_orders_count_by_portal_by_contract**
> object get_orders_count_by_portal_by_contract(contract_id)



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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_orders_count_by_portal_by_contract(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_orders_count_by_portal_by_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

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
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no lower time limit is considered.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no upper time limit is considered.  (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no lower time limit is considered.  (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range for fetching orders. Formatted as ISO 8601 format with timezone with reference to UTC (e.g. for [Europe/Berlin] in winter time: 2023-11-01T14:50:45.495+01:00. In summer time: 2023-11-01T14:50:45.495+02:00). If this value is omitted then no upper time limit is considered.  (optional)

    try:
        api_response = api_instance.get_orders_vendor_v3(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_orders_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_customer_orders_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2() # ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2 | Orders to be added

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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_customer_orders_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2() # ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2 | Orders to be added

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
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_customer_orders_request_v2** | [**ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2**](ComPatagonaPricemonitorShareApiPostCustomerOrdersRequestV2.md)| Orders to be added | 

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
**200** | Successfully added orders |  -  |
**400** | Unable to add orders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

