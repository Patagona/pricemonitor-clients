# openapi_client.PricerecommendationsApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_repricing_strategy_vendor_v2**](PricerecommendationsApi.md#delete_repricing_strategy_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/repricingstrategy | 
[**get_price_recommendation**](PricerecommendationsApi.md#get_price_recommendation) | **GET** /api/2/v/contracts/{contractId}/result/pricerecommendations | Get all price recommendations
[**get_price_recommendation_stats_vendor_v2**](PricerecommendationsApi.md#get_price_recommendation_stats_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/pricerecommendationstats | 
[**get_price_recommendations**](PricerecommendationsApi.md#get_price_recommendations) | **GET** /api/1/{contractId}/products/analysis/pricerecommendations | Get price recommendations (deprecated)
[**get_repricing_strategy_vendor_v2**](PricerecommendationsApi.md#get_repricing_strategy_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/repricingstrategy | 
[**get_stats**](PricerecommendationsApi.md#get_stats) | **GET** /api/1/{contractId}/products/analysis/pricerecommendations/stats/{portal} | 
[**get_time_stamps**](PricerecommendationsApi.md#get_time_stamps) | **GET** /api/1/{contractId}/products/analysis/timestamps | 
[**put_repricing_strategy_vendor_v2**](PricerecommendationsApi.md#put_repricing_strategy_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/repricingstrategy | 
[**query_price_recommendations_vendor_v2**](PricerecommendationsApi.md#query_price_recommendations_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricerecommendations/query | 


# **delete_repricing_strategy_vendor_v2**
> object delete_repricing_strategy_vendor_v2(contract_id)



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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_repricing_strategy_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->delete_repricing_strategy_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

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

# **get_price_recommendation**
> GetPriceRecommendationApiResponse get_price_recommendation(contract_id, start_time, end_time, start, limit=limit)

Get all price recommendations

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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_time = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC
end_time = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC
start = 56 # int | Start price-recommendation index for pagination
limit = 100 # int | Number of price-recommendations for pagination (optional) (default to 100)

    try:
        # Get all price recommendations
        api_response = api_instance.get_price_recommendation(contract_id, start_time, end_time, start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start_time** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC | 
 **end_time** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC | 
 **start** | **int**| Start price-recommendation index for pagination | 
 **limit** | **int**| Number of price-recommendations for pagination | [optional] [default to 100]

### Return type

[**GetPriceRecommendationApiResponse**](GetPriceRecommendationApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of price recommendations is returned for the specified timerange. Only the newest price recommendations are returned in case of multiple price recommendations per product. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_recommendation_stats_vendor_v2**
> object get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)



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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 
max_positions = 56 # int | 

    try:
        api_response = api_instance.get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendation_stats_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 
 **max_positions** | **int**|  | 

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

# **get_price_recommendations**
> GetPriceRecommendationsResponse get_price_recommendations(contract_id, start=start, limit=limit, since=since)

Get price recommendations (deprecated)

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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 0 # int | Where to start fetching the recommendations (optional) (default to 0)
limit = 10000 # int | Maximal number of results (optional) (default to 10000)
since = '2019-01-01T00:00:00.000Z' # datetime | Timestamp of the oldest results (optional)

    try:
        # Get price recommendations (deprecated)
        api_response = api_instance.get_price_recommendations(contract_id, start=start, limit=limit, since=since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**| Where to start fetching the recommendations | [optional] [default to 0]
 **limit** | **int**| Maximal number of results | [optional] [default to 10000]
 **since** | **datetime**| Timestamp of the oldest results | [optional] 

### Return type

[**GetPriceRecommendationsResponse**](GetPriceRecommendationsResponse.md)

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

# **get_repricing_strategy_vendor_v2**
> object get_repricing_strategy_vendor_v2(contract_id)



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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_repricing_strategy_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_repricing_strategy_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

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

# **get_stats**
> object get_stats(contract_id, portal, until=until)



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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
portal = 'portal_example' # str | 
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_stats(contract_id, portal, until=until)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **portal** | **str**|  | 
 **until** | **datetime**|  | [optional] 

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

# **get_time_stamps**
> object get_time_stamps(contract_id)



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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 56 # int | 

    try:
        api_response = api_instance.get_time_stamps(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_time_stamps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**|  | 

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

# **put_repricing_strategy_vendor_v2**
> object put_repricing_strategy_vendor_v2(contract_id, body=body)



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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_repricing_strategy_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->put_repricing_strategy_vendor_v2: %s\n" % e)
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

# **query_price_recommendations_vendor_v2**
> QueryPriceRecommendationsV2ApiResponse query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)



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
    api_instance = openapi_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
price_recommendation_api_query_v2 = openapi_client.PriceRecommendationApiQueryV2() # PriceRecommendationApiQueryV2 | The request body specifies which price recommendations will be searched for. (optional)

    try:
        api_response = api_instance.query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->query_price_recommendations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **price_recommendation_api_query_v2** | [**PriceRecommendationApiQueryV2**](PriceRecommendationApiQueryV2.md)| The request body specifies which price recommendations will be searched for. | [optional] 

### Return type

[**QueryPriceRecommendationsV2ApiResponse**](QueryPriceRecommendationsV2ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of price recommendations is returned for the specified timerange. &lt;br&gt; Only the newest price recommendations are returned in case of multiple price recommendations per product.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

