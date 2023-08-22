# pricemonitor_api_client.OffersApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_manufacturer_contracts_contract_id_offers_get**](OffersApi.md#api_v3_manufacturer_contracts_contract_id_offers_get) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers | 
[**api_v3_manufacturer_contracts_contract_id_offers_shops_get**](OffersApi.md#api_v3_manufacturer_contracts_contract_id_offers_shops_get) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/shops | Returns all shops which have at least one offer for a given time range per domain.
[**api_v3_vendor_contracts_contract_id_offers_get**](OffersApi.md#api_v3_vendor_contracts_contract_id_offers_get) | **GET** /api/v3/vendor/contracts/{contractId}/offers | 
[**api_v3_vendor_contracts_contract_id_offers_query_post**](OffersApi.md#api_v3_vendor_contracts_contract_id_offers_query_post) | **POST** /api/v3/vendor/contracts/{contractId}/offers/query | 
[**api_v3_vendor_contracts_contract_id_offers_shops_get**](OffersApi.md#api_v3_vendor_contracts_contract_id_offers_shops_get) | **GET** /api/v3/vendor/contracts/{contractId}/offers/shops | Returns all shops which have at least one offer for a given time range per domain.
[**get_cheapest_vendors_manufacturer_v2**](OffersApi.md#get_cheapest_vendors_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/cheapest | 
[**get_complex_offer_filters_vendor_v2**](OffersApi.md#get_complex_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Get all complex filters for the given contract.
[**get_offer_filters_vendor_v2**](OffersApi.md#get_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Get all the vendor filters for the given contract.
[**get_offer_statistics_manufacturer_v3**](OffersApi.md#get_offer_statistics_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/stats | Get offer statistics per product of a contract. Only the latest offers per product and domain the are taken into account.
[**get_price_cutters_manufacturer_v2**](OffersApi.md#get_price_cutters_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricecutters | 
[**get_price_cutters_vendor_v2**](OffersApi.md#get_price_cutters_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricecutters | 
[**get_product_filters_by_id_vendor_v2**](OffersApi.md#get_product_filters_by_id_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/offerfilters/:listType/products/query | 
[**get_product_filters_by_range_vendor_v2**](OffersApi.md#get_product_filters_by_range_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products | Get all the filters product-wise for the given contract.
[**get_product_metrics_by_contract**](OffersApi.md#get_product_metrics_by_contract) | **GET** /api/1/{contractId}/products/articlescountbyportal | 
[**get_product_price_violations_manufacturer_v2**](OffersApi.md#get_product_price_violations_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/priceviolations | 
[**get_product_price_violations_vendor_v2**](OffersApi.md#get_product_price_violations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/priceviolations | 
[**get_vendors_by_domain_manufacturer_v2**](OffersApi.md#get_vendors_by_domain_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/list | 
[**position_distribution**](OffersApi.md#position_distribution) | **POST** /api/1/{contractId}/vendors/{vendor}/positions | 
[**post_offers_in_a_bulk_vendor_v2**](OffersApi.md#post_offers_in_a_bulk_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/offers | Add offers in bulk
[**prices_by_day_by_product_id_manufacturer_v2**](OffersApi.md#prices_by_day_by_product_id_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricesbyday/productid/{productId} | 
[**put_complex_offer_filters_vendor_v2**](OffersApi.md#put_complex_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Add the complex filters for the given contract.
[**put_offer_filters_vendor_v2**](OffersApi.md#put_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Store the vendor filters for the given contract.
[**query_offers_manufacturer_v3**](OffersApi.md#query_offers_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/query | 
[**raw_offers**](OffersApi.md#raw_offers) | **GET** /api/1/{contractId}/products/offers | 
[**segment_offers_manufacturer_v2**](OffersApi.md#segment_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/offersegmentation | 
[**segment_offers_vendor_v2**](OffersApi.md#segment_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/offersegmentation | 
[**stats_manufacturer_v2**](OffersApi.md#stats_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/contract/stats | 
[**timestamps_manufacturer_v2**](OffersApi.md#timestamps_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/timestamps | 
[**validate_offers_manufacturer_v2**](OffersApi.md#validate_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/validation | 
[**validate_offers_vendor_v2**](OffersApi.md#validate_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/validation | 


# **api_v3_manufacturer_contracts_contract_id_offers_get**
> GetOffersApiResponse api_v3_manufacturer_contracts_contract_id_offers_get(contract_id, start=start, limit=limit, start_date=start_date, end_date=end_date)



Returns the newest offers for a given time range.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 0 # int | Where to start fetching the products (optional) (default to 0)
limit = 1000 # int | Maximum number of results (optional) (default to 1000)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_get(contract_id, start=start, limit=limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_manufacturer_contracts_contract_id_offers_get: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 0 # int | Where to start fetching the products (optional) (default to 0)
limit = 1000 # int | Maximum number of results (optional) (default to 1000)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_get(contract_id, start=start, limit=limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_manufacturer_contracts_contract_id_offers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**| Where to start fetching the products | [optional] [default to 0]
 **limit** | **int**| Maximum number of results | [optional] [default to 1000]
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 

### Return type

[**GetOffersApiResponse**](GetOffersApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of products with their corresponding offers. |  -  |
**400** | Returned in case of invalid time range or a limit greater than 10000. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_manufacturer_contracts_contract_id_offers_shops_get**
> GetShopsByDomainResponseV3ApiResponse api_v3_manufacturer_contracts_contract_id_offers_shops_get(contract_id, start_date=start_date, end_date=end_date)

Returns all shops which have at least one offer for a given time range per domain.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Returns all shops which have at least one offer for a given time range per domain.
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_shops_get(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_manufacturer_contracts_contract_id_offers_shops_get: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Returns all shops which have at least one offer for a given time range per domain.
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_shops_get(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_manufacturer_contracts_contract_id_offers_shops_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 

### Return type

[**GetShopsByDomainResponseV3ApiResponse**](GetShopsByDomainResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shops which have at least one offer for a given time range per domain. |  -  |
**400** | Specified time range is invalid (&gt; 7 days). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_vendor_contracts_contract_id_offers_get**
> GetOffersApiResponse api_v3_vendor_contracts_contract_id_offers_get(contract_id, start=start, limit=limit, start_date=start_date, end_date=end_date)



Returns the newest offers for a given time range.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 0 # int | Where to start fetching the products (optional) (default to 0)
limit = 1000 # int | Maximum number of results (optional) (default to 1000)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_get(contract_id, start=start, limit=limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_vendor_contracts_contract_id_offers_get: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 0 # int | Where to start fetching the products (optional) (default to 0)
limit = 1000 # int | Maximum number of results (optional) (default to 1000)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_get(contract_id, start=start, limit=limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_vendor_contracts_contract_id_offers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**| Where to start fetching the products | [optional] [default to 0]
 **limit** | **int**| Maximum number of results | [optional] [default to 1000]
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 

### Return type

[**GetOffersApiResponse**](GetOffersApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of products with their corresponding offers. |  -  |
**400** | Returned in case of invalid time range or a limit greater than 10000. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_vendor_contracts_contract_id_offers_query_post**
> QueryOffersApiResponse api_v3_vendor_contracts_contract_id_offers_query_post(contract_id, product_offers_api_query)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_offers_api_query = pricemonitor_api_client.ProductOffersApiQuery() # ProductOffersApiQuery | The request body specifies which offers will be searched for.<br> Warning: It's highly recommended to not use this endpoint since it is error-prone due to complex query structure! Supported are queries with three different types of filters:<br> 1. Filtering for offers of a certain product<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"productId\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual pricemonitor product ID to filter offers for   * the `comparison` being a `StringEquality`  2. Filtering for valid offers of a certain product<br> This can be done by an AndFilter with   * a) A product filter (see first supported filter)   * b) A NotFilter which contains a ComparisonFilter     * the `left` side being a `NumberValueProvider` with the `attributeName` value \"ignoredBy\"     * the `right` side being a `NumberConstantValueProvider` with the `value` being the numeric contract id to filter offers for     * the `comparison` being a `NumberEquality`  3. Filtering for offers of a certain vendor<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"reseller_name\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual vendor name to filter offers for   * the `comparison` being a `StringEquality`  Note: This endpoint will only return the newest offers for each product for a given time range.

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_query_post(contract_id, product_offers_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_vendor_contracts_contract_id_offers_query_post: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_offers_api_query = pricemonitor_api_client.ProductOffersApiQuery() # ProductOffersApiQuery | The request body specifies which offers will be searched for.<br> Warning: It's highly recommended to not use this endpoint since it is error-prone due to complex query structure! Supported are queries with three different types of filters:<br> 1. Filtering for offers of a certain product<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"productId\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual pricemonitor product ID to filter offers for   * the `comparison` being a `StringEquality`  2. Filtering for valid offers of a certain product<br> This can be done by an AndFilter with   * a) A product filter (see first supported filter)   * b) A NotFilter which contains a ComparisonFilter     * the `left` side being a `NumberValueProvider` with the `attributeName` value \"ignoredBy\"     * the `right` side being a `NumberConstantValueProvider` with the `value` being the numeric contract id to filter offers for     * the `comparison` being a `NumberEquality`  3. Filtering for offers of a certain vendor<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"reseller_name\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual vendor name to filter offers for   * the `comparison` being a `StringEquality`  Note: This endpoint will only return the newest offers for each product for a given time range.

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_query_post(contract_id, product_offers_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_vendor_contracts_contract_id_offers_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_offers_api_query** | [**ProductOffersApiQuery**](ProductOffersApiQuery.md)| The request body specifies which offers will be searched for.&lt;br&gt; Warning: It&#39;s highly recommended to not use this endpoint since it is error-prone due to complex query structure! Supported are queries with three different types of filters:&lt;br&gt; 1. Filtering for offers of a certain product&lt;br&gt; This can be done by a ComparisonFilter with   * the &#x60;left&#x60; side being a &#x60;StringValueProvider&#x60; with the &#x60;attributeName&#x60; value \&quot;productId\&quot;   * the &#x60;right&#x60; side being a &#x60;StringConstantValueProvider&#x60; with the &#x60;value&#x60; being the actual pricemonitor product ID to filter offers for   * the &#x60;comparison&#x60; being a &#x60;StringEquality&#x60;  2. Filtering for valid offers of a certain product&lt;br&gt; This can be done by an AndFilter with   * a) A product filter (see first supported filter)   * b) A NotFilter which contains a ComparisonFilter     * the &#x60;left&#x60; side being a &#x60;NumberValueProvider&#x60; with the &#x60;attributeName&#x60; value \&quot;ignoredBy\&quot;     * the &#x60;right&#x60; side being a &#x60;NumberConstantValueProvider&#x60; with the &#x60;value&#x60; being the numeric contract id to filter offers for     * the &#x60;comparison&#x60; being a &#x60;NumberEquality&#x60;  3. Filtering for offers of a certain vendor&lt;br&gt; This can be done by a ComparisonFilter with   * the &#x60;left&#x60; side being a &#x60;StringValueProvider&#x60; with the &#x60;attributeName&#x60; value \&quot;reseller_name\&quot;   * the &#x60;right&#x60; side being a &#x60;StringConstantValueProvider&#x60; with the &#x60;value&#x60; being the actual vendor name to filter offers for   * the &#x60;comparison&#x60; being a &#x60;StringEquality&#x60;  Note: This endpoint will only return the newest offers for each product for a given time range. | 

### Return type

[**QueryOffersApiResponse**](QueryOffersApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns either an Error or a list of ApiOffers matching the given filter. |  -  |
**400** | Returned in case of unparsable request JSON or unsupported filter/sorting. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_vendor_contracts_contract_id_offers_shops_get**
> GetShopsByDomainResponseV3ApiResponse api_v3_vendor_contracts_contract_id_offers_shops_get(contract_id, start_date=start_date, end_date=end_date)

Returns all shops which have at least one offer for a given time range per domain.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Returns all shops which have at least one offer for a given time range per domain.
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_shops_get(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_vendor_contracts_contract_id_offers_shops_get: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Returns all shops which have at least one offer for a given time range per domain.
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_shops_get(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->api_v3_vendor_contracts_contract_id_offers_shops_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 

### Return type

[**GetShopsByDomainResponseV3ApiResponse**](GetShopsByDomainResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shops which have at least one offer for a given time range per domain. |  -  |
**400** | Specified time range is invalid (&gt; 7 days). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cheapest_vendors_manufacturer_v2**
> object get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_cheapest_vendors_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_cheapest_vendors_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**|  | 
 **include_delivery_costs** | **bool**|  | 
 **com_patagona_pricemonitor_share_api_tag_filtered_vendors_request** | [**ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest**](ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest.md)| This is a generated entry and needs to be described. | [optional] 

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

# **get_complex_offer_filters_vendor_v2**
> OfferFilterApiResponse get_complex_offer_filters_vendor_v2(contract_id, list_type)

Get all complex filters for the given contract.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all complex filters for the given contract.
        api_response = api_instance.get_complex_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_complex_offer_filters_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all complex filters for the given contract.
        api_response = api_instance.get_complex_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_complex_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 

### Return type

[**OfferFilterApiResponse**](OfferFilterApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters to ignore the individual offers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_filters_vendor_v2**
> object get_offer_filters_vendor_v2(contract_id, list_type)

Get all the vendor filters for the given contract.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all the vendor filters for the given contract.
        api_response = api_instance.get_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offer_filters_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all the vendor filters for the given contract.
        api_response = api_instance.get_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 

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
**200** | List of the filters to ignore the individual offers. Offers are filtered against vendor name either for all the domain or for a specific domain. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_statistics_manufacturer_v3**
> GetOfferStatisticsV3ApiResponse get_offer_statistics_manufacturer_v3(contract_id, include_delivery_costs, start_date=start_date, end_date=end_date)

Get offer statistics per product of a contract. Only the latest offers per product and domain the are taken into account.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
include_delivery_costs = True # bool | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        # Get offer statistics per product of a contract. Only the latest offers per product and domain the are taken into account.
        api_response = api_instance.get_offer_statistics_manufacturer_v3(contract_id, include_delivery_costs, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offer_statistics_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
include_delivery_costs = True # bool | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        # Get offer statistics per product of a contract. Only the latest offers per product and domain the are taken into account.
        api_response = api_instance.get_offer_statistics_manufacturer_v3(contract_id, include_delivery_costs, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offer_statistics_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **include_delivery_costs** | **bool**|  | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 

### Return type

[**GetOfferStatisticsV3ApiResponse**](GetOfferStatisticsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. |  -  |
**400** | Specified time range is invalid (&gt; 48h). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_cutters_manufacturer_v2**
> object get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_price_cutters_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_price_cutters_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**|  | 
 **limit** | **int**|  | 
 **include_delivery_costs** | **bool**|  | 
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

# **get_price_cutters_vendor_v2**
> object get_price_cutters_vendor_v2(contract_id, session, limit, include_delivery_costs, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_vendor_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_price_cutters_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_vendor_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_price_cutters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**|  | 
 **limit** | **int**|  | 
 **include_delivery_costs** | **bool**|  | 
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

# **get_product_filters_by_id_vendor_v2**
> object get_product_filters_by_id_vendor_v2(contract_id, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_product_filters_by_id_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_filters_by_id_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_product_filters_by_id_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_filters_by_id_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **get_product_filters_by_range_vendor_v2**
> object get_product_filters_by_range_vendor_v2(contract_id, list_type, start, limit)

Get all the filters product-wise for the given contract.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
start = 56 # int | 
limit = 56 # int | 

    try:
        # Get all the filters product-wise for the given contract.
        api_response = api_instance.get_product_filters_by_range_vendor_v2(contract_id, list_type, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_filters_by_range_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
start = 56 # int | 
limit = 56 # int | 

    try:
        # Get all the filters product-wise for the given contract.
        api_response = api_instance.get_product_filters_by_range_vendor_v2(contract_id, list_type, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_filters_by_range_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **start** | **int**|  | 
 **limit** | **int**|  | 

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
**200** | List of the filters per product to ignore the individual offers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_metrics_by_contract**
> object get_product_metrics_by_contract(contract_id, start, end)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        api_response = api_instance.get_product_metrics_by_contract(contract_id, start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_metrics_by_contract: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        api_response = api_instance.get_product_metrics_by_contract(contract_id, start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_metrics_by_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

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

# **get_product_price_violations_manufacturer_v2**
> object get_product_price_violations_manufacturer_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_manufacturer_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_price_violations_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_manufacturer_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_price_violations_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 
 **include_delivery_costs** | **bool**|  | 
 **reference_price_delta** | **float**|  | 

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

# **get_product_price_violations_vendor_v2**
> object get_product_price_violations_vendor_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_vendor_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_price_violations_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_vendor_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_price_violations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 
 **include_delivery_costs** | **bool**|  | 
 **reference_price_delta** | **float**|  | 

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

# **get_vendors_by_domain_manufacturer_v2**
> ComPatagonaPricemonitorShareApiPostVendorsByDomainResponse get_vendors_by_domain_manufacturer_v2(contract_id, domain, start, include_delivery_costs, session, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
domain = 'domain_example' # str | 
start = 56 # int | 
include_delivery_costs = True # bool | 
session = '2013-10-20T19:20:30+01:00' # datetime | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_vendors_by_domain_manufacturer_v2(contract_id, domain, start, include_delivery_costs, session, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_vendors_by_domain_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
domain = 'domain_example' # str | 
start = 56 # int | 
include_delivery_costs = True # bool | 
session = '2013-10-20T19:20:30+01:00' # datetime | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_vendors_by_domain_manufacturer_v2(contract_id, domain, start, include_delivery_costs, session, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_vendors_by_domain_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **domain** | **str**|  | 
 **start** | **int**|  | 
 **include_delivery_costs** | **bool**|  | 
 **session** | **datetime**|  | 
 **com_patagona_pricemonitor_share_api_tag_filtered_vendors_request** | [**ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest**](ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

[**ComPatagonaPricemonitorShareApiPostVendorsByDomainResponse**](ComPatagonaPricemonitorShareApiPostVendorsByDomainResponse.md)

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

# **position_distribution**
> object position_distribution(contract_id, vendor, day, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor = 'vendor_example' # str | 
day = '2013-10-20T19:20:30+01:00' # datetime | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.position_distribution(contract_id, vendor, day, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->position_distribution: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor = 'vendor_example' # str | 
day = '2013-10-20T19:20:30+01:00' # datetime | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.position_distribution(contract_id, vendor, day, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->position_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor** | **str**|  | 
 **day** | **datetime**|  | 
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

# **post_offers_in_a_bulk_vendor_v2**
> PostOffersResponse post_offers_in_a_bulk_vendor_v2(contract_id, com_patagona_pricemonitor_share_api_post_product_offer_request)

Add offers in bulk

This endpoint can be used to provide external offers to Pricemonitor. It's a bulk endpoint which accepts an array of individual POST offers requests each based on a \"snapshot\" - a unique combination of product, domain, and timestamp for a list of offers. Please note the following consistency checks performed before offers are stored: 1. Offers can only be stored if the corresponding products exist in the contract. 2. Offers can only be stored if they are more recent than existing offers. This means that only newer snapshots are eligible for storage. 3. Offers can only be stored if the currency is consistent. In other words, a single domain must use only one currency. 4. Duplicated individual POST offers requests are stored only once. 5. If different offers are provided for the same snapshots, then all conflicting snapshots will be rejected. 6. An individual POST offers request may be rejected if the offer ID is not unique. 

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_product_offer_request = [pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostProductOfferRequest()] # list[ComPatagonaPricemonitorShareApiPostProductOfferRequest] | List of individual POST offers requests which should be added in bulk.

    try:
        # Add offers in bulk
        api_response = api_instance.post_offers_in_a_bulk_vendor_v2(contract_id, com_patagona_pricemonitor_share_api_post_product_offer_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->post_offers_in_a_bulk_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_product_offer_request = [pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostProductOfferRequest()] # list[ComPatagonaPricemonitorShareApiPostProductOfferRequest] | List of individual POST offers requests which should be added in bulk.

    try:
        # Add offers in bulk
        api_response = api_instance.post_offers_in_a_bulk_vendor_v2(contract_id, com_patagona_pricemonitor_share_api_post_product_offer_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->post_offers_in_a_bulk_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_product_offer_request** | [**list[ComPatagonaPricemonitorShareApiPostProductOfferRequest]**](ComPatagonaPricemonitorShareApiPostProductOfferRequest.md)| List of individual POST offers requests which should be added in bulk. | 

### Return type

[**PostOffersResponse**](PostOffersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The server understood and processed the request. Offers were processed, but not necessarily stored successfully. The &#39;data&#39; field in the response body contains a detailed report of the operation outcome for each individual POST offers requests. Each item in the &#39;data&#39; array is **either** a &#39;data&#39; object with value true (indicating successful storage), or an ApiErrorResponse (indicating a storage failure).  |  -  |
**400** | The server could not understand the request due to invalid syntax. For example, a required field might be missing in the request body.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prices_by_day_by_product_id_manufacturer_v2**
> list[ComPatagonaPricemonitorShareApiPricesByDayByProductIdResponseV2] prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | The product ID to filter for
com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2() # ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2 | Query all known prices for a given day & product ID. Can be filtered by using the selectors. (optional)

    try:
        api_response = api_instance.prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->prices_by_day_by_product_id_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | The product ID to filter for
com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2() # ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2 | Query all known prices for a given day & product ID. Can be filtered by using the selectors. (optional)

    try:
        api_response = api_instance.prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->prices_by_day_by_product_id_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **str**| The product ID to filter for | 
 **com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2** | [**ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2**](ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2.md)| Query all known prices for a given day &amp; product ID. Can be filtered by using the selectors. | [optional] 

### Return type

[**list[ComPatagonaPricemonitorShareApiPricesByDayByProductIdResponseV2]**](ComPatagonaPricemonitorShareApiPricesByDayByProductIdResponseV2.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all known prices for the queried day &amp; product ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_complex_offer_filters_vendor_v2**
> OfferFilterApiResponse put_complex_offer_filters_vendor_v2(contract_id, list_type, and_offer_filter=and_offer_filter)

Add the complex filters for the given contract.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Add the complex filters for the given contract.
        api_response = api_instance.put_complex_offer_filters_vendor_v2(contract_id, list_type, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->put_complex_offer_filters_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Add the complex filters for the given contract.
        api_response = api_instance.put_complex_offer_filters_vendor_v2(contract_id, list_type, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->put_complex_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **and_offer_filter** | [**list[AndOfferFilter]**](AndOfferFilter.md)| List of the filter that needs to be considered to ignore the individual offers. | [optional] 

### Return type

[**OfferFilterApiResponse**](OfferFilterApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters that have been sent as the request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_offer_filters_vendor_v2**
> object put_offer_filters_vendor_v2(contract_id, list_type, body=body)

Store the vendor filters for the given contract.

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
body = None # object | List of the filters that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the vendor filters for the given contract.
        api_response = api_instance.put_offer_filters_vendor_v2(contract_id, list_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->put_offer_filters_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
body = None # object | List of the filters that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the vendor filters for the given contract.
        api_response = api_instance.put_offer_filters_vendor_v2(contract_id, list_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->put_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **body** | **object**| List of the filters that needs to be considered to ignore the individual offers. | [optional] 

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
**200** | List of the filters that have been sent as the request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_manufacturer_v3**
> object query_offers_manufacturer_v3(contract_id, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.query_offers_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.query_offers_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **raw_offers**
> object raw_offers(contract_id, start, limit, since=since, until=until)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.raw_offers(contract_id, start, limit, since=since, until=until)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->raw_offers: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.raw_offers(contract_id, start, limit, since=since, until=until)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->raw_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**|  | 
 **limit** | **int**|  | 
 **since** | **datetime**|  | [optional] 
 **until** | **datetime**|  | [optional] 

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

# **segment_offers_manufacturer_v2**
> object segment_offers_manufacturer_v2(contract_id, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->segment_offers_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->segment_offers_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **segment_offers_vendor_v2**
> object segment_offers_vendor_v2(contract_id, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->segment_offers_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->segment_offers_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **stats_manufacturer_v2**
> ComPatagonaPricemonitorShareApiContractStats stats_manufacturer_v2(contract_id, session)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected

    try:
        api_response = api_instance.stats_manufacturer_v2(contract_id, session)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->stats_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected

    try:
        api_response = api_instance.stats_manufacturer_v2(contract_id, session)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->stats_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**| A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected | 

### Return type

[**ComPatagonaPricemonitorShareApiContractStats**](ComPatagonaPricemonitorShareApiContractStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the contract statistics: product count, vendor count, found offers count (filters applied), active portals count, found offers count (no filters applied) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timestamps_manufacturer_v2**
> object timestamps_manufacturer_v2(contract_id, limit)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
limit = 56 # int | 

    try:
        api_response = api_instance.timestamps_manufacturer_v2(contract_id, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->timestamps_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
limit = 56 # int | 

    try:
        api_response = api_instance.timestamps_manufacturer_v2(contract_id, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->timestamps_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **limit** | **int**|  | 

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

# **validate_offers_manufacturer_v2**
> object validate_offers_manufacturer_v2(contract_id, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->validate_offers_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->validate_offers_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **validate_offers_vendor_v2**
> object validate_offers_vendor_v2(contract_id, body=body)



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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->validate_offers_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->validate_offers_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

