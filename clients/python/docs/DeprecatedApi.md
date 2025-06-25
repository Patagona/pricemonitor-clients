# pricemonitor_api_client.DeprecatedApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_domains_v2**](DeprecatedApi.md#get_all_domains_v2) | **GET** /api/2/domains | Gets a list of all available domains (V2)
[**get_offers**](DeprecatedApi.md#get_offers) | **GET** /api/2/v/contracts/{contractId}/result/offers | Get all offers for all products
[**get_price_recommendations**](DeprecatedApi.md#get_price_recommendations) | **GET** /api/1/{contractId}/products/analysis/pricerecommendations | Get price recommendations
[**get_strategy_history**](DeprecatedApi.md#get_strategy_history) | **GET** /api/v3/vendor/contracts/{contractId}/settings/repricingstrategy/history | Get metadata of all strategy versions for contract
[**post_log_message**](DeprecatedApi.md#post_log_message) | **POST** /api/2/log/messages | Log a message
[**put_csv_products**](DeprecatedApi.md#put_csv_products) | **PUT** /api/2/v/contracts/{contractId}/products/csv | Set products via CSV file (V2)
[**put_products_vendor_v2**](DeprecatedApi.md#put_products_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/products | Update products in bulk (JSON)


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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    
    try:
        # Gets a list of all available domains (V2)
        api_response = api_instance.get_all_domains_v2()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_all_domains_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    
    try:
        # Gets a list of all available domains (V2)
        api_response = api_instance.get_all_domains_v2()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_all_domains_v2: %s\n" % e)
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

# **get_offers**
> GetOffersResponse get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)

Get all offers for all products

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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 56 # int | Start product index for pagination
limit = 56 # int | Number of products for pagination
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get all offers for all products
        api_response = api_instance.get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_offers: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 56 # int | Start product index for pagination
limit = 56 # int | Number of products for pagination
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get all offers for all products
        api_response = api_instance.get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start** | **int**| Start product index for pagination | 
 **limit** | **int**| Number of products for pagination | 
 **start_date** | **datetime**| **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-15T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;endDate&#x60; is provided: &#x60;startDate&#x60; &#x3D; &#x60;endDate&#x60; - 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 
 **end_date** | **datetime**| **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-16T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;startDate&#x60; is provided: &#x60;endDate&#x60; &#x3D; &#x60;startDate&#x60; + 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 

### Return type

[**GetOffersResponse**](GetOffersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_recommendations**
> GetPriceRecommendationsResponse get_price_recommendations(contract_id, start=start, limit=limit, since=since)

Get price recommendations

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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Where to start fetching the recommendations (optional) (default to 0)
limit = 10000 # int | Maximal number of results (optional) (default to 10000)
since = '2019-01-01T00:00:00.000Z' # datetime | Timestamp of the oldest results (optional)

    try:
        # Get price recommendations
        api_response = api_instance.get_price_recommendations(contract_id, start=start, limit=limit, since=since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_price_recommendations: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Where to start fetching the recommendations (optional) (default to 0)
limit = 10000 # int | Maximal number of results (optional) (default to 10000)
since = '2019-01-01T00:00:00.000Z' # datetime | Timestamp of the oldest results (optional)

    try:
        # Get price recommendations
        api_response = api_instance.get_price_recommendations(contract_id, start=start, limit=limit, since=since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_price_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start** | **int**| Where to start fetching the recommendations | [optional] [default to 0]
 **limit** | **int**| Maximal number of results | [optional] [default to 10000]
 **since** | **datetime**| Timestamp of the oldest results | [optional] 

### Return type

[**GetPriceRecommendationsResponse**](GetPriceRecommendationsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strategy_history**
> GetPricingStrategyHistoryApiResponse get_strategy_history(contract_id)

Get metadata of all strategy versions for contract

**⚠️ DEPRECATED:** This endpoint is deprecated and should no longer be used.  Retrieves a list of metadata for all pricing strategy versions associated with a specific contract. Use `/api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/history` instead. 

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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get metadata of all strategy versions for contract
        api_response = api_instance.get_strategy_history(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_strategy_history: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get metadata of all strategy versions for contract
        api_response = api_instance.get_strategy_history(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_strategy_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

### Return type

[**GetPricingStrategyHistoryApiResponse**](GetPricingStrategyHistoryApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of metadata of all strategy versions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_log_message**
> object post_log_message()

Log a message

Logs a message.

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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    
    try:
        # Log a message
        api_response = api_instance.post_log_message()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->post_log_message: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    
    try:
        # Log a message
        api_response = api_instance.post_log_message()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->post_log_message: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **put_csv_products**
> put_csv_products(contract_id, body)

Set products via CSV file (V2)

Warning: Deletes all existing products.         <br/>Note that this will not happen immediately. Instead, you receive the ID of a task that has been created.         <br/>Furthermore you receive an URL which you can use to check if the task was executed successfully.         <br>The csv file must contain following columns:         <ul>           <li>productId - arbitrary string, can be used for the systems product id.</li>           <li>gtin - the GTIN of the product           <li>description - name or short description of the product           <li>referencePrice - arbitrary decimal number, usually the current price or recommended retail price (gross)           <li>minPriceBoundary - decimal number defining the lower price boundary (gross)           <li>maxPriceBoundary - decimal number defining the upper price boundary (gross)           <li>Additional columns are added as product tags. Tags are used for repricing strategies and several other           purpose.         </ul>         <br/>Column separator must be semicolon, the decimal separator must be dot. File encoding must be UTF-8.

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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file (V2)
        api_instance.put_csv_products(contract_id, body)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->put_csv_products: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file (V2)
        api_instance.put_csv_products(contract_id, body)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->put_csv_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **body** | **str**| CSV file containing the products | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | - |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_vendor_v2**
> object put_products_vendor_v2(contract_id, body=body)

Update products in bulk (JSON)

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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update products in bulk (JSON)
        api_response = api_instance.put_products_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->put_products_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.DeprecatedApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update products in bulk (JSON)
        api_response = api_instance.put_products_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->put_products_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

