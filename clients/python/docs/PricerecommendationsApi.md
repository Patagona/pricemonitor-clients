# pricemonitor_api_client.PricerecommendationsApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decide_price_recommendations_approvals_v3**](PricerecommendationsApi.md#decide_price_recommendations_approvals_v3) | **POST** /api/v3/vendor/contracts/{contractId}/pricerecommendations/approvals/decide | Set price recommendation approvals
[**delete_repricing_strategy_vendor_v2**](PricerecommendationsApi.md#delete_repricing_strategy_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/repricingstrategy | Delete repricing strategy
[**get_price_recommendation**](PricerecommendationsApi.md#get_price_recommendation) | **GET** /api/2/v/contracts/{contractId}/result/pricerecommendations | Get price recommendations for time range
[**get_price_recommendation_stats_vendor_v2**](PricerecommendationsApi.md#get_price_recommendation_stats_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/pricerecommendationstats | Get price reommendation stats
[**get_price_recommendations**](PricerecommendationsApi.md#get_price_recommendations) | **GET** /api/1/{contractId}/products/analysis/pricerecommendations | Get price recommendations
[**get_product_price_recommendation_history**](PricerecommendationsApi.md#get_product_price_recommendation_history) | **GET** /api/v3/vendor/contracts/{contractId}/products/{productId}/pricerecommendationhistory | Get price recommendations for one product
[**get_repricing_strategy_vendor_v2**](PricerecommendationsApi.md#get_repricing_strategy_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/repricingstrategy | Get repricing strategy
[**get_time_stamps**](PricerecommendationsApi.md#get_time_stamps) | **GET** /api/1/{contractId}/products/analysis/timestamps | Get time stamps
[**put_repricing_strategy_vendor_v2**](PricerecommendationsApi.md#put_repricing_strategy_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/repricingstrategy | Update repricing strategy
[**query_price_recommendations_approvals_v3**](PricerecommendationsApi.md#query_price_recommendations_approvals_v3) | **POST** /api/v3/vendor/contracts/{contractId}/pricerecommendations/approvals/query | Query price recommendation approvals
[**query_price_recommendations_vendor_v2**](PricerecommendationsApi.md#query_price_recommendations_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricerecommendations/query | Query price recommendations
[**simulate_price_recommendations_v3**](PricerecommendationsApi.md#simulate_price_recommendations_v3) | **POST** /api/v3/vendor/contracts/{contractId}/pricerecommendations/simulate | Simulate price recommendations


# **decide_price_recommendations_approvals_v3**
> BooleanBulkApiResponse decide_price_recommendations_approvals_v3(contract_id, com_patagona_pricemonitor_share_api_post_price_recommendation_approval_request_v3)

Set price recommendation approvals

Processes bulk decisions for price recommendation approvals. Only pending price recommendations can be decided.  ## Notes - *Approval* refers to the price approval flow concept in our business processes, covering all states of price recommendations within this flow (i.e., pending, approved, rejected). The term does not mean all price recommendations are approved. - We preserve a linear history: Once a price recommendation approval is **finalized** (i.e., no longer pending), it can no longer be changed. - If any user rejects, the entire price recommendation is rejected. - If a user has already submitted an active (not superseded) decision for a recommendation, they cannot submit another. - The endpoint is not idempotent, as submitting a decision changes the approval state. - If a price overwrite happens, we recalculate the new position of the offer with the new price in mind. We use the offers that were also used during the original price calculation, the current offer filters, the current vendor mappings, and the current product information for the position calculation. 

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_price_recommendation_approval_request_v3 = [pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostPriceRecommendationApprovalRequestV3()] # list[ComPatagonaPricemonitorShareApiPostPriceRecommendationApprovalRequestV3] | The request body contains a list of price decisions to process. 

    try:
        # Set price recommendation approvals
        api_response = api_instance.decide_price_recommendations_approvals_v3(contract_id, com_patagona_pricemonitor_share_api_post_price_recommendation_approval_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->decide_price_recommendations_approvals_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_price_recommendation_approval_request_v3 = [pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostPriceRecommendationApprovalRequestV3()] # list[ComPatagonaPricemonitorShareApiPostPriceRecommendationApprovalRequestV3] | The request body contains a list of price decisions to process. 

    try:
        # Set price recommendation approvals
        api_response = api_instance.decide_price_recommendations_approvals_v3(contract_id, com_patagona_pricemonitor_share_api_post_price_recommendation_approval_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->decide_price_recommendations_approvals_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_post_price_recommendation_approval_request_v3** | [**list[ComPatagonaPricemonitorShareApiPostPriceRecommendationApprovalRequestV3]**](ComPatagonaPricemonitorShareApiPostPriceRecommendationApprovalRequestV3.md)| The request body contains a list of price decisions to process.  | 

### Return type

[**BooleanBulkApiResponse**](BooleanBulkApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicating that at least one price recommendation approval decision has been applied.  Notes: - The response array preserves the order of the input request array. - An individual price decision might not be processed if:   - Multiple decisions for the same product are included in a single request: **none** of those decisions     will be processed, as it is ambiguous which decision should apply.   - The corresponding price recommendation approval is already processed (i.e., not in the &#39;pending&#39; status).   - The user has already submitted an active decision (not superseded) for that approval.  |  -  |
**400** | The request could not be processed due to validation errors in the provided body, or none of the pricing decisions could be applied.  Common issues include: - Malformed JSON. - The decision &#39;overwritten&#39; is provided for a product, but the overwrite price is missing. - A decision other than &#39;overwritten&#39; is provided for a product, but the overwrite price is provided. - An overwrite price lower than 0.01 is provided. - An unsupported decision is provided (only &#39;approved&#39;, &#39;rejected&#39;, and &#39;overwritten&#39; are supported). - All price recommendation approvals in the request have been already processed   (e.g., previously approved, rejected, overwritten, or outdated). - The user has already submitted decisions for all provided price recommendation approvals. - A referred price recommendation approval does not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repricing_strategy_vendor_v2**
> object delete_repricing_strategy_vendor_v2(contract_id)

Delete repricing strategy

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Delete repricing strategy
        api_response = api_instance.delete_repricing_strategy_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->delete_repricing_strategy_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Delete repricing strategy
        api_response = api_instance.delete_repricing_strategy_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->delete_repricing_strategy_vendor_v2: %s\n" % e)
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
**200** | Delete all strategy versions per provided contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_recommendation**
> GetPriceRecommendationApiResponse get_price_recommendation(contract_id, start_time, end_time, start, limit=limit, include_tags=include_tags)

Get price recommendations for time range

Retrieves all price recommendations for a contract within the specified time range.  This endpoint returns algorithmic pricing recommendations based on market analysis, competitor pricing, and configured pricing strategies. Only the most recent recommendations are returned when multiple recommendations exist for the same product.  **Key Features:** - Paginated results for efficient data retrieval - Optional product tag inclusion - Configurable time range filtering - Real-time market-based recommendations 

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_time = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for price recommendation retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`) 
end_time = '2024-01-16T23:59:59Z' # datetime | **End of time range** for price recommendation retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`) 
start = 0 # int | Starting index for pagination (0-based)
limit = 100 # int | Maximum number of price recommendations to return per page (optional) (default to 100)
include_tags = True # bool | Whether to include product tags in the response (optional) (default to True)

    try:
        # Get price recommendations for time range
        api_response = api_instance.get_price_recommendation(contract_id, start_time, end_time, start, limit=limit, include_tags=include_tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendation: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_time = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for price recommendation retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`) 
end_time = '2024-01-16T23:59:59Z' # datetime | **End of time range** for price recommendation retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`) 
start = 0 # int | Starting index for pagination (0-based)
limit = 100 # int | Maximum number of price recommendations to return per page (optional) (default to 100)
include_tags = True # bool | Whether to include product tags in the response (optional) (default to True)

    try:
        # Get price recommendations for time range
        api_response = api_instance.get_price_recommendation(contract_id, start_time, end_time, start, limit=limit, include_tags=include_tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start_time** | **datetime**| **Start of time range** for price recommendation retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-15T10:30:00Z&#x60;)  | 
 **end_time** | **datetime**| **End of time range** for price recommendation retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-16T10:30:00Z&#x60;)  | 
 **start** | **int**| Starting index for pagination (0-based) | 
 **limit** | **int**| Maximum number of price recommendations to return per page | [optional] [default to 100]
 **include_tags** | **bool**| Whether to include product tags in the response | [optional] [default to True]

### Return type

[**GetPriceRecommendationApiResponse**](GetPriceRecommendationApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of price recommendations for the specified time range.  Each recommendation includes the product information, recommended price, delivery costs, position data, and strategy information that determined the recommendation. Only the newest recommendations are returned when multiple exist for the same product.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_recommendation_stats_vendor_v2**
> object get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)

Get price reommendation stats

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 
max_positions = 56 # int | 

    try:
        # Get price reommendation stats
        api_response = api_instance.get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendation_stats_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 
max_positions = 56 # int | 

    try:
        # Get price reommendation stats
        api_response = api_instance.get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendation_stats_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 
 **max_positions** | **int**|  | 

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Where to start fetching the recommendations (optional) (default to 0)
limit = 10000 # int | Maximal number of results (optional) (default to 10000)
since = '2019-01-01T00:00:00.000Z' # datetime | Timestamp of the oldest results (optional)

    try:
        # Get price recommendations
        api_response = api_instance.get_price_recommendations(contract_id, start=start, limit=limit, since=since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendations: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Where to start fetching the recommendations (optional) (default to 0)
limit = 10000 # int | Maximal number of results (optional) (default to 10000)
since = '2019-01-01T00:00:00.000Z' # datetime | Timestamp of the oldest results (optional)

    try:
        # Get price recommendations
        api_response = api_instance.get_price_recommendations(contract_id, start=start, limit=limit, since=since)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_price_recommendations: %s\n" % e)
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

# **get_product_price_recommendation_history**
> GetPriceRecommendationHistoryApiResponse get_product_price_recommendation_history(contract_id, product_id, start_date=start_date, end_date=end_date)

Get price recommendations for one product

This endpoint returns all price recommendations for one product within a given time range.

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = '862342' # str | Internal product identifier in the pricemonitor system
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get price recommendations for one product
        api_response = api_instance.get_product_price_recommendation_history(contract_id, product_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_product_price_recommendation_history: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = '862342' # str | Internal product identifier in the pricemonitor system
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get price recommendations for one product
        api_response = api_instance.get_product_price_recommendation_history(contract_id, product_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_product_price_recommendation_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_id** | **str**| Internal product identifier in the pricemonitor system | 
 **start_date** | **datetime**| **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-15T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;endDate&#x60; is provided: &#x60;startDate&#x60; &#x3D; &#x60;endDate&#x60; - 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 
 **end_date** | **datetime**| **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-16T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;startDate&#x60; is provided: &#x60;endDate&#x60; &#x3D; &#x60;startDate&#x60; + 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 

### Return type

[**GetPriceRecommendationHistoryApiResponse**](GetPriceRecommendationHistoryApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of price recommendations |  -  |
**400** | E.g. when the time range spans more than 48h. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repricing_strategy_vendor_v2**
> object get_repricing_strategy_vendor_v2(contract_id, document_version=document_version)

Get repricing strategy

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
document_version = 5 # int |  (optional)

    try:
        # Get repricing strategy
        api_response = api_instance.get_repricing_strategy_vendor_v2(contract_id, document_version=document_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_repricing_strategy_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
document_version = 5 # int |  (optional)

    try:
        # Get repricing strategy
        api_response = api_instance.get_repricing_strategy_vendor_v2(contract_id, document_version=document_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_repricing_strategy_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **document_version** | **int**|  | [optional] 

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
**200** | In case a document version is provided, get that strategy version. Otherwise get latest strategy for this contract. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_stamps**
> object get_time_stamps(contract_id)

Get time stamps

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 56 # int | 

    try:
        # Get time stamps
        api_response = api_instance.get_time_stamps(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->get_time_stamps: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 56 # int | 

    try:
        # Get time stamps
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

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

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

Update repricing strategy

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update repricing strategy
        api_response = api_instance.put_repricing_strategy_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->put_repricing_strategy_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update repricing strategy
        api_response = api_instance.put_repricing_strategy_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->put_repricing_strategy_vendor_v2: %s\n" % e)
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
**200** | Save a new strategy version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_price_recommendations_approvals_v3**
> QueryPriceRecommendationsApprovalsV3ApiResponse query_price_recommendations_approvals_v3(contract_id, com_patagona_pricemonitor_share_api_price_recommendations_approval_query_request_v3)

Query price recommendation approvals

This endpoint queries price recommendation approvals for a specified set of filters.  Use cases include: - Retrieving pending price recommendation approvals. - Auditing historic pricing decisions.  Note: *Approval* refers to the price approval flow concept in our business processes, covering all states of price recommendations within this flow (e.g., pending, approved, rejected). The term does not mean all price recommendations are approved. 

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_recommendations_approval_query_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryRequestV3() # ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryRequestV3 | The request body contains all necessary filters to query the desired price recommendation approvals. 

    try:
        # Query price recommendation approvals
        api_response = api_instance.query_price_recommendations_approvals_v3(contract_id, com_patagona_pricemonitor_share_api_price_recommendations_approval_query_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->query_price_recommendations_approvals_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_recommendations_approval_query_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryRequestV3() # ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryRequestV3 | The request body contains all necessary filters to query the desired price recommendation approvals. 

    try:
        # Query price recommendation approvals
        api_response = api_instance.query_price_recommendations_approvals_v3(contract_id, com_patagona_pricemonitor_share_api_price_recommendations_approval_query_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->query_price_recommendations_approvals_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_price_recommendations_approval_query_request_v3** | [**ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryRequestV3**](ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryRequestV3.md)| The request body contains all necessary filters to query the desired price recommendation approvals.  | 

### Return type

[**QueryPriceRecommendationsApprovalsV3ApiResponse**](QueryPriceRecommendationsApprovalsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response containing a list of price approval meta information and associated price recommendations.  |  -  |
**400** | The request could not be processed due to validation errors in the provided body. Common issues include:  - Malformed JSON. - Invalid time range provided. - Invalid pagination parameters. - Invalid approval status values provided.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_price_recommendations_vendor_v2**
> QueryPriceRecommendationsV2ApiResponse query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)

Query price recommendations

This endpoint is used to query certain price recommendations. It supports a rather complex filtering structure. Most commonly it's used for querying by our internal product id.  Here you can find an example request body for querying one product id (here `123456`):  <details> <summary>Click to expand</summary>  ``` json {   \"pagination\": {     \"start\": 0,     \"limit\": 500   },   \"range\": {     \"start\": \"2023-01-07T12:05:01.000Z\",     \"end\": \"2023-01-09T12:05:01.000Z\"   },   \"filter\": {     \"filters\": [{       \"left\": {         \"attributeName\": \"productId\",         \"type\": \"StringValueProvider\"       },       \"right\": {         \"value\": \"123456\",         \"type\": \"StringConstantValueProvider\"       },       \"comparison\": {         \"type\": \"StringEquality\"       },       \"type\": \"ComparisonFilter\"     }],     \"type\": \"OrFilter\"   } } ``` </details>  If you want to query for multiple product ids, then you need to provide one object per product id in the filters-array.  It's recommended to query for at most 1000 price recommendations at once.

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
price_recommendation_api_query_v2 = pricemonitor_api_client.PriceRecommendationApiQueryV2() # PriceRecommendationApiQueryV2 | The request body specifies which price recommendations will be searched for. (optional)

    try:
        # Query price recommendations
        api_response = api_instance.query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->query_price_recommendations_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
price_recommendation_api_query_v2 = pricemonitor_api_client.PriceRecommendationApiQueryV2() # PriceRecommendationApiQueryV2 | The request body specifies which price recommendations will be searched for. (optional)

    try:
        # Query price recommendations
        api_response = api_instance.query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->query_price_recommendations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **price_recommendation_api_query_v2** | [**PriceRecommendationApiQueryV2**](PriceRecommendationApiQueryV2.md)| The request body specifies which price recommendations will be searched for. | [optional] 

### Return type

[**QueryPriceRecommendationsV2ApiResponse**](QueryPriceRecommendationsV2ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of price recommendations is returned for the specified timerange. &lt;br&gt; Only the newest price recommendations are returned in case of multiple price recommendations per product.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_price_recommendations_v3**
> SimulatePriceCalculationBulkV3ApiResponse simulate_price_recommendations_v3(contract_id, com_patagona_pricemonitor_share_api_price_simulation_bulk_request_v3)

Simulate price recommendations

This endpoint simulates price recommendations for a specified set of products. It is useful for:  - Explaining why certain price recommendations have been calculated. - Testing and evaluating pricing strategies before applying them.  The simulation process can be customized by including parameters such as a custom pricing strategy, custom time range, specific offers and more.  A maximum of 10 price recommendation simulations may be included in one request. 

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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_simulation_bulk_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3() # ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3 | The request body contains all the necessary data to simulate price recommendations for multiple products. Custom parameters, such as pricing strategies and time ranges, can be provided in order to simulate different scenarios. 

    try:
        # Simulate price recommendations
        api_response = api_instance.simulate_price_recommendations_v3(contract_id, com_patagona_pricemonitor_share_api_price_simulation_bulk_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->simulate_price_recommendations_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.PricerecommendationsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_simulation_bulk_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3() # ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3 | The request body contains all the necessary data to simulate price recommendations for multiple products. Custom parameters, such as pricing strategies and time ranges, can be provided in order to simulate different scenarios. 

    try:
        # Simulate price recommendations
        api_response = api_instance.simulate_price_recommendations_v3(contract_id, com_patagona_pricemonitor_share_api_price_simulation_bulk_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PricerecommendationsApi->simulate_price_recommendations_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_price_simulation_bulk_request_v3** | [**ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3**](ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3.md)| The request body contains all the necessary data to simulate price recommendations for multiple products. Custom parameters, such as pricing strategies and time ranges, can be provided in order to simulate different scenarios.  | 

### Return type

[**SimulatePriceCalculationBulkV3ApiResponse**](SimulatePriceCalculationBulkV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response containing a bulk result with simulated price recommendations for multiple products.  |  -  |
**400** | The request could not be processed due to validation errors in the provided body. Common issues include:  - Malformed JSON. - Unimported products specified in the request. - Too many simulation requests in the body. - Contract not compatible with simulation feature.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

