# pricemonitor_api_client.OffersApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cheapest_vendors_manufacturer_v2**](OffersApi.md#get_cheapest_vendors_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/cheapest | Query cheapest offers
[**get_complex_offer_filters_vendor_v2**](OffersApi.md#get_complex_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Get all complex filters for the given contract.
[**get_offer_filters_vendor_v2**](OffersApi.md#get_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Get all vendor filters for contract
[**get_offer_statistics_manufacturer_v3**](OffersApi.md#get_offer_statistics_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/stats | Get offer statistics per product of a contract
[**get_offers**](OffersApi.md#get_offers) | **GET** /api/2/v/contracts/{contractId}/result/offers | Get all offers for all products
[**get_offers_manufacturer_v3**](OffersApi.md#get_offers_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers | Get offers for time range
[**get_offers_shops_manufacturer_v3**](OffersApi.md#get_offers_shops_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/shops | Get shops with offers for time range
[**get_offers_shops_vendor_v3**](OffersApi.md#get_offers_shops_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/offers/shops | Get shops with offers for time range per domain
[**get_offers_vendor_v3**](OffersApi.md#get_offers_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/offers | Get offers for timerange
[**get_price_cutters_manufacturer_v2**](OffersApi.md#get_price_cutters_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricecutters | Query price cutters [manufacturer]
[**get_price_cutters_vendor_v2**](OffersApi.md#get_price_cutters_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricecutters | Query price cutters [vendor]
[**get_product_filters_by_id_vendor_v2**](OffersApi.md#get_product_filters_by_id_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/offerfilters/:listType/products/query | Get filtered offers
[**get_product_filters_by_range_vendor_v2**](OffersApi.md#get_product_filters_by_range_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products | Get all the filters product-wise for the given contract.
[**get_product_metrics_by_contract**](OffersApi.md#get_product_metrics_by_contract) | **GET** /api/1/{contractId}/products/articlescountbyportal | Get product metrics for contract
[**get_product_price_violations_manufacturer_v2**](OffersApi.md#get_product_price_violations_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/priceviolations | Get product price violations [manufacturer]
[**get_product_price_violations_vendor_v2**](OffersApi.md#get_product_price_violations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/priceviolations | Get product price violations [vendor]
[**get_vendors_by_domain_manufacturer_v2**](OffersApi.md#get_vendors_by_domain_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/list | Get vendors by domain
[**position_distribution**](OffersApi.md#position_distribution) | **POST** /api/1/{contractId}/vendors/{vendor}/positions | Update position distribution
[**post_offers_in_a_bulk_vendor_v2**](OffersApi.md#post_offers_in_a_bulk_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/offers | Add offers in bulk
[**prices_by_day_by_product_id_manufacturer_v2**](OffersApi.md#prices_by_day_by_product_id_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricesbyday/productid/{productId} | Query prices by day by product
[**put_complex_offer_filters_vendor_v2**](OffersApi.md#put_complex_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Add the complex filters for the given contract.
[**put_offer_filters_vendor_v2**](OffersApi.md#put_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Store vendor filters for contract
[**query_offers_manufacturer_v3**](OffersApi.md#query_offers_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/query | Query offers [manufacturer]
[**query_offers_stats_manufacturer_v31**](OffersApi.md#query_offers_stats_manufacturer_v31) | **POST** /api/v3.1/manufacturer/contracts/{contractId}/offers/stats/query | Query offer statistics per product
[**query_offers_stats_vendor_v31**](OffersApi.md#query_offers_stats_vendor_v31) | **POST** /api/v3.1/vendor/contracts/{contractId}/offers/stats/query | Query offer statistics per product
[**query_offers_vendor_v3**](OffersApi.md#query_offers_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/offers/query | Query offers [vendor]
[**raw_offers**](OffersApi.md#raw_offers) | **GET** /api/1/{contractId}/products/offers | Get offers for contract
[**segment_offers_manufacturer_v2**](OffersApi.md#segment_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/offersegmentation | Update segment offers [manufacturer]
[**segment_offers_vendor_v2**](OffersApi.md#segment_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/offersegmentation | Update segment offers [vendor]
[**stats_manufacturer_v2**](OffersApi.md#stats_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/contract/stats | Get contract statistics [manufacturer]
[**timestamps_manufacturer_v2**](OffersApi.md#timestamps_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/timestamps | Get timestamps
[**validate_offers_manufacturer_v2**](OffersApi.md#validate_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/validation | Validate offers [manufacturer]
[**validate_offers_vendor_v2**](OffersApi.md#validate_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/validation | Validate offers [vendor]


# **get_cheapest_vendors_manufacturer_v2**
> object get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)

Query cheapest offers

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        # Query cheapest offers
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        # Query cheapest offers
        api_response = api_instance.get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_cheapest_vendors_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
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
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get all vendor filters for contract

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all vendor filters for contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all vendor filters for contract
        api_response = api_instance.get_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get offer statistics per product of a contract

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
include_delivery_costs = True # bool | 
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get offer statistics per product of a contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
include_delivery_costs = True # bool | 
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get offer statistics per product of a contract
        api_response = api_instance.get_offer_statistics_manufacturer_v3(contract_id, include_delivery_costs, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offer_statistics_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **include_delivery_costs** | **bool**|  | 
 **start_date** | **datetime**| **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-15T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;endDate&#x60; is provided: &#x60;startDate&#x60; &#x3D; &#x60;endDate&#x60; - 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 
 **end_date** | **datetime**| **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-16T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;startDate&#x60; is provided: &#x60;endDate&#x60; &#x3D; &#x60;startDate&#x60; + 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 

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
    api_instance = pricemonitor_api_client.OffersApi(api_client)
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
        print("Exception when calling OffersApi->get_offers: %s\n" % e)
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
        print("Exception when calling OffersApi->get_offers: %s\n" % e)
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

# **get_offers_manufacturer_v3**
> GetOffersApiResponse get_offers_manufacturer_v3(contract_id, start=start, limit=limit, include_tags=include_tags, start_date=start_date, end_date=end_date)

Get offers for time range

**🔒 INTERNAL:** Retrieves the most recent offers for all products within a specified time range.  This endpoint provides manufacturer contracts with access to offer data across all monitored domains and vendors. The data includes pricing, availability, and vendor information for competitive analysis.  **Performance Notes:** - Results are paginated based on products for optimal performance - Maximum limit of 1,000 products per request - Time range should be kept reasonable for best performance 

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Starting index for pagination (0-based) (optional) (default to 0)
limit = 1000 # int | Maximum number of offers to return (max 10,000) (optional) (default to 1000)
include_tags = True # bool | Whether to include product tags in the response (optional) (default to True)
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get offers for time range
        api_response = api_instance.get_offers_manufacturer_v3(contract_id, start=start, limit=limit, include_tags=include_tags, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_manufacturer_v3: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Starting index for pagination (0-based) (optional) (default to 0)
limit = 1000 # int | Maximum number of offers to return (max 10,000) (optional) (default to 1000)
include_tags = True # bool | Whether to include product tags in the response (optional) (default to True)
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get offers for time range
        api_response = api_instance.get_offers_manufacturer_v3(contract_id, start=start, limit=limit, include_tags=include_tags, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start** | **int**| Starting index for pagination (0-based) | [optional] [default to 0]
 **limit** | **int**| Maximum number of offers to return (max 10,000) | [optional] [default to 1000]
 **include_tags** | **bool**| Whether to include product tags in the response | [optional] [default to True]
 **start_date** | **datetime**| **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-15T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;endDate&#x60; is provided: &#x60;startDate&#x60; &#x3D; &#x60;endDate&#x60; - 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 
 **end_date** | **datetime**| **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-16T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;startDate&#x60; is provided: &#x60;endDate&#x60; &#x3D; &#x60;startDate&#x60; + 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 

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

# **get_offers_shops_manufacturer_v3**
> GetShopsByDomainResponseV3ApiResponse get_offers_shops_manufacturer_v3(contract_id, start_date=start_date, end_date=end_date)

Get shops with offers for time range

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range
        api_response = api_instance.get_offers_shops_manufacturer_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_shops_manufacturer_v3: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range
        api_response = api_instance.get_offers_shops_manufacturer_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_shops_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

# **get_offers_shops_vendor_v3**
> GetShopsByDomainResponseV3ApiResponse get_offers_shops_vendor_v3(contract_id, start_date=start_date, end_date=end_date)

Get shops with offers for time range per domain

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range per domain
        api_response = api_instance.get_offers_shops_vendor_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_shops_vendor_v3: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range per domain
        api_response = api_instance.get_offers_shops_vendor_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_shops_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

# **get_offers_vendor_v3**
> GetOffersApiResponse get_offers_vendor_v3(contract_id, start=start, limit=limit, include_tags=include_tags, start_date=start_date, end_date=end_date)

Get offers for timerange

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Where to start fetching the products (optional) (default to 0)
limit = 1000 # int | Maximum number of results (optional) (default to 1000)
include_tags = True # bool | Whether to return tags of products or not. (optional) (default to True)
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get offers for timerange
        api_response = api_instance.get_offers_vendor_v3(contract_id, start=start, limit=limit, include_tags=include_tags, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_vendor_v3: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 0 # int | Where to start fetching the products (optional) (default to 0)
limit = 1000 # int | Maximum number of results (optional) (default to 1000)
include_tags = True # bool | Whether to return tags of products or not. (optional) (default to True)
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get offers for timerange
        api_response = api_instance.get_offers_vendor_v3(contract_id, start=start, limit=limit, include_tags=include_tags, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_offers_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start** | **int**| Where to start fetching the products | [optional] [default to 0]
 **limit** | **int**| Maximum number of results | [optional] [default to 1000]
 **include_tags** | **bool**| Whether to return tags of products or not. | [optional] [default to True]
 **start_date** | **datetime**| **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-15T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;endDate&#x60; is provided: &#x60;startDate&#x60; &#x3D; &#x60;endDate&#x60; - 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 
 **end_date** | **datetime**| **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-16T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;startDate&#x60; is provided: &#x60;endDate&#x60; &#x3D; &#x60;startDate&#x60; + 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 

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

# **get_price_cutters_manufacturer_v2**
> object get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)

Query price cutters [manufacturer]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Query price cutters [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Query price cutters [manufacturer]
        api_response = api_instance.get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_price_cutters_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Query price cutters [vendor]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Query price cutters [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Query price cutters [vendor]
        api_response = api_instance.get_price_cutters_vendor_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_price_cutters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get filtered offers

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Get filtered offers
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Get filtered offers
        api_response = api_instance.get_product_filters_by_id_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_filters_by_id_vendor_v2: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
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
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get product metrics for contract

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get product metrics for contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Get product metrics for contract
        api_response = api_instance.get_product_metrics_by_contract(contract_id, start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_metrics_by_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get product price violations [manufacturer]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        # Get product price violations [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        # Get product price violations [manufacturer]
        api_response = api_instance.get_product_price_violations_manufacturer_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_price_violations_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get product price violations [vendor]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        # Get product price violations [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        # Get product price violations [vendor]
        api_response = api_instance.get_product_price_violations_vendor_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_product_price_violations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get vendors by domain

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
domain = 'domain_example' # str | 
start = 56 # int | 
include_delivery_costs = True # bool | 
session = '2013-10-20T19:20:30+01:00' # datetime | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        # Get vendors by domain
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
domain = 'domain_example' # str | 
start = 56 # int | 
include_delivery_costs = True # bool | 
session = '2013-10-20T19:20:30+01:00' # datetime | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        # Get vendors by domain
        api_response = api_instance.get_vendors_by_domain_manufacturer_v2(contract_id, domain, start, include_delivery_costs, session, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->get_vendors_by_domain_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Update position distribution

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
vendor = 'vendor_example' # str | 
day = '2013-10-20T19:20:30+01:00' # datetime | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update position distribution
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
vendor = 'vendor_example' # str | 
day = '2013-10-20T19:20:30+01:00' # datetime | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update position distribution
        api_response = api_instance.position_distribution(contract_id, vendor, day, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->position_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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
> BooleanBulkApiResponse post_offers_in_a_bulk_vendor_v2(contract_id, com_patagona_pricemonitor_share_api_post_product_offer_request)

Add offers in bulk

This endpoint can be used to provide external offers to Omnia 2.0. It's a bulk endpoint which accepts an array of individual POST offers requests each based on a \"snapshot\" - a unique combination of product, domain, and timestamp for a list of offers.  Validation rules before storage:  1. The product must exist in the contract. 2. Only snapshots newer than those already stored will be accepted. 3. Each domain must use a consistent currency. 4. Duplicate snapshots in the same request are stored once. 5. Conflicting snapshots for the same product + domain + timestamp are all rejected. 6. Offer IDs must be unique across all offers. 7. The domain field must not be empty. 8. Offer prices must be ≥ 0.01, delivery costs must be ≥ 0. 

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_product_offer_request = [pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostProductOfferRequest()] # list[ComPatagonaPricemonitorShareApiPostProductOfferRequest] | A list of individual POST offers requests (snapshots) to be stored.  Submit up to 1,000 snapshots per request for optimal performance. Snapshots are validated and processed in the order provided. The response follows the same order. 

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_product_offer_request = [pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostProductOfferRequest()] # list[ComPatagonaPricemonitorShareApiPostProductOfferRequest] | A list of individual POST offers requests (snapshots) to be stored.  Submit up to 1,000 snapshots per request for optimal performance. Snapshots are validated and processed in the order provided. The response follows the same order. 

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
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_post_product_offer_request** | [**list[ComPatagonaPricemonitorShareApiPostProductOfferRequest]**](ComPatagonaPricemonitorShareApiPostProductOfferRequest.md)| A list of individual POST offers requests (snapshots) to be stored.  Submit up to 1,000 snapshots per request for optimal performance. Snapshots are validated and processed in the order provided. The response follows the same order.  | 

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
**200** | The request was successfully processed. Each individual POST offers request was validated and handled separately. The &#39;data&#39; field in the response contains one entry per request item, in the same order as submitted.  Each entry is either: - &#x60;true&#x60;: The offer snapshot was accepted and stored. - &#x60;ApiErrorResponse&#x60;: The snapshot was rejected, including details about the reason.  |  -  |
**400** | The server could not understand the request due to invalid syntax. For example, a required field might be missing in the request body.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prices_by_day_by_product_id_manufacturer_v2**
> list[ComPatagonaPricemonitorShareApiPricesByDayByProductIdResponseV2] prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)

Query prices by day by product

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | The product ID to filter for
com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2() # ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2 | Query all known prices for a given day & product ID. Can be filtered by using the selectors. (optional)

    try:
        # Query prices by day by product
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | The product ID to filter for
com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2() # ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2 | Query all known prices for a given day & product ID. Can be filtered by using the selectors. (optional)

    try:
        # Query prices by day by product
        api_response = api_instance.prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->prices_by_day_by_product_id_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
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
 **contract_id** | **str**| Unique identifier of the contract | 
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

Store vendor filters for contract

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 
body = None # object | List of the filters that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store vendor filters for contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 
body = None # object | List of the filters that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store vendor filters for contract
        api_response = api_instance.put_offer_filters_vendor_v2(contract_id, list_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->put_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Query offers [manufacturer]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Query offers [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Query offers [manufacturer]
        api_response = api_instance.query_offers_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_manufacturer_v3: %s\n" % e)
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

# **query_offers_stats_manufacturer_v31**
> QueryOfferStatisticsV31ApiResponse query_offers_stats_manufacturer_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)

Query offer statistics per product

This endpoint can be used to query offer statistics (e.g. offer count, average price) grouped by product. Only the most recent market data is considered per product and domain. 

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-10-17T08:00:00Z","end":"2023-10-19T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"productId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId's. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: ``` json {   \"pagination\": {     \"start\": ${start},     \"limit\": ${limit}   },   \"range\": {     \"start\": ${start},     \"end\": ${end}   },   \"filter\": {     \"oneOf\": {       \"field\": \"customerProductId\",       \"values\": [${customerProductIds as a list of strings}]     }   } } ``` (optional)

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_manufacturer_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_stats_manufacturer_v31: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-10-17T08:00:00Z","end":"2023-10-19T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"productId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId's. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: ``` json {   \"pagination\": {     \"start\": ${start},     \"limit\": ${limit}   },   \"range\": {     \"start\": ${start},     \"end\": ${end}   },   \"filter\": {     \"oneOf\": {       \"field\": \"customerProductId\",       \"values\": [${customerProductIds as a list of strings}]     }   } } ``` (optional)

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_manufacturer_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_stats_manufacturer_v31: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31** | [**ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31**](ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31.md)| The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \&quot;customerProductId\&quot;   - \&quot;productId\&quot; (Patagona&#39;s internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \&quot;productId\&quot; for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId&#39;s. For chunked requests over a set of ids, it&#39;s straightforward to specify up to 10,000 customerProductId&#39;s in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: &#x60;&#x60;&#x60; json {   \&quot;pagination\&quot;: {     \&quot;start\&quot;: ${start},     \&quot;limit\&quot;: ${limit}   },   \&quot;range\&quot;: {     \&quot;start\&quot;: ${start},     \&quot;end\&quot;: ${end}   },   \&quot;filter\&quot;: {     \&quot;oneOf\&quot;: {       \&quot;field\&quot;: \&quot;customerProductId\&quot;,       \&quot;values\&quot;: [${customerProductIds as a list of strings}]     }   } } &#x60;&#x60;&#x60; | [optional] 

### Return type

[**QueryOfferStatisticsV31ApiResponse**](QueryOfferStatisticsV31ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. When a product has no market data then no offer statistics are returned for that product.  |  -  |
**400** | A &#x60;400&#x60; error is returned under the following conditions: - The request body JSON is unparsable. - An unsupported filter is provided. - The specified time range exceeds 48 hours. - The pagination limit exceeds 10,000.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_stats_vendor_v31**
> QueryOfferStatisticsV31ApiResponse query_offers_stats_vendor_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)

Query offer statistics per product

This endpoint can be used to query offer statistics (e.g. offer count, average price) grouped by product. Only the most recent market data is considered per product and domain.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-10-17T08:00:00Z","end":"2023-10-19T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"productId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId's. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: ``` json {   \"pagination\": {     \"start\": ${start},     \"limit\": ${limit}   },   \"range\": {     \"start\": ${start},     \"end\": ${end}   },   \"filter\": {     \"oneOf\": {       \"field\": \"customerProductId\",       \"values\": [${customerProductIds as a list of strings}]     }   } } ``` (optional)

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_vendor_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_stats_vendor_v31: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-10-17T08:00:00Z","end":"2023-10-19T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"productId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId's. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: ``` json {   \"pagination\": {     \"start\": ${start},     \"limit\": ${limit}   },   \"range\": {     \"start\": ${start},     \"end\": ${end}   },   \"filter\": {     \"oneOf\": {       \"field\": \"customerProductId\",       \"values\": [${customerProductIds as a list of strings}]     }   } } ``` (optional)

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_vendor_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_stats_vendor_v31: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31** | [**ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31**](ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31.md)| The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \&quot;customerProductId\&quot;   - \&quot;productId\&quot; (Patagona&#39;s internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \&quot;productId\&quot; for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId&#39;s. For chunked requests over a set of ids, it&#39;s straightforward to specify up to 10,000 customerProductId&#39;s in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: &#x60;&#x60;&#x60; json {   \&quot;pagination\&quot;: {     \&quot;start\&quot;: ${start},     \&quot;limit\&quot;: ${limit}   },   \&quot;range\&quot;: {     \&quot;start\&quot;: ${start},     \&quot;end\&quot;: ${end}   },   \&quot;filter\&quot;: {     \&quot;oneOf\&quot;: {       \&quot;field\&quot;: \&quot;customerProductId\&quot;,       \&quot;values\&quot;: [${customerProductIds as a list of strings}]     }   } } &#x60;&#x60;&#x60; | [optional] 

### Return type

[**QueryOfferStatisticsV31ApiResponse**](QueryOfferStatisticsV31ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. When a product has no market data then no offer statistics are returned for that product.  |  -  |
**400** | A &#x60;400&#x60; error is returned under the following conditions: - The request body JSON is unparsable. - An unsupported filter is provided. - The specified time range exceeds 48 hours. - The pagination limit exceeds 10,000.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_vendor_v3**
> QueryOffersApiResponse query_offers_vendor_v3(contract_id, product_offers_api_query)

Query offers [vendor]

Supports complex queries for offers.

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_offers_api_query = pricemonitor_api_client.ProductOffersApiQuery() # ProductOffersApiQuery | The request body specifies which offers will be searched for.<br> Warning: It's highly recommended to not use this endpoint since it is error-prone due to complex query structure! Supported are queries with three different types of filters:<br> 1. Filtering for offers of a certain product<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"productId\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual pricemonitor product ID to filter offers for   * the `comparison` being a `StringEquality`  2. Filtering for valid offers of a certain product<br> This can be done by an AndFilter with   * a) A product filter (see first supported filter)   * b) A NotFilter which contains a ComparisonFilter     * the `left` side being a `NumberValueProvider` with the `attributeName` value \"ignoredBy\"     * the `right` side being a `NumberConstantValueProvider` with the `value` being the numeric contract id to filter offers for     * the `comparison` being a `NumberEquality`  3. Filtering for offers of a certain vendor<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"reseller_name\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual vendor name to filter offers for   * the `comparison` being a `StringEquality`  Note: This endpoint will only return the newest offers for each product for a given time range.

    try:
        # Query offers [vendor]
        api_response = api_instance.query_offers_vendor_v3(contract_id, product_offers_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_vendor_v3: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_offers_api_query = pricemonitor_api_client.ProductOffersApiQuery() # ProductOffersApiQuery | The request body specifies which offers will be searched for.<br> Warning: It's highly recommended to not use this endpoint since it is error-prone due to complex query structure! Supported are queries with three different types of filters:<br> 1. Filtering for offers of a certain product<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"productId\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual pricemonitor product ID to filter offers for   * the `comparison` being a `StringEquality`  2. Filtering for valid offers of a certain product<br> This can be done by an AndFilter with   * a) A product filter (see first supported filter)   * b) A NotFilter which contains a ComparisonFilter     * the `left` side being a `NumberValueProvider` with the `attributeName` value \"ignoredBy\"     * the `right` side being a `NumberConstantValueProvider` with the `value` being the numeric contract id to filter offers for     * the `comparison` being a `NumberEquality`  3. Filtering for offers of a certain vendor<br> This can be done by a ComparisonFilter with   * the `left` side being a `StringValueProvider` with the `attributeName` value \"reseller_name\"   * the `right` side being a `StringConstantValueProvider` with the `value` being the actual vendor name to filter offers for   * the `comparison` being a `StringEquality`  Note: This endpoint will only return the newest offers for each product for a given time range.

    try:
        # Query offers [vendor]
        api_response = api_instance.query_offers_vendor_v3(contract_id, product_offers_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->query_offers_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

# **raw_offers**
> object raw_offers(contract_id, start, limit, since=since, until=until)

Get offers for contract

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 56 # int | 
limit = 56 # int | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get offers for contract
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start = 56 # int | 
limit = 56 # int | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get offers for contract
        api_response = api_instance.raw_offers(contract_id, start, limit, since=since, until=until)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->raw_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Update segment offers [manufacturer]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update segment offers [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update segment offers [manufacturer]
        api_response = api_instance.segment_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->segment_offers_manufacturer_v2: %s\n" % e)
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

# **segment_offers_vendor_v2**
> object segment_offers_vendor_v2(contract_id, body=body)

Update segment offers [vendor]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update segment offers [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update segment offers [vendor]
        api_response = api_instance.segment_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->segment_offers_vendor_v2: %s\n" % e)
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

# **stats_manufacturer_v2**
> ComPatagonaPricemonitorShareApiContractStats stats_manufacturer_v2(contract_id, session)

Get contract statistics [manufacturer]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected

    try:
        # Get contract statistics [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected

    try:
        # Get contract statistics [manufacturer]
        api_response = api_instance.stats_manufacturer_v2(contract_id, session)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->stats_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Get timestamps

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
limit = 56 # int | 

    try:
        # Get timestamps
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
limit = 56 # int | 

    try:
        # Get timestamps
        api_response = api_instance.timestamps_manufacturer_v2(contract_id, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->timestamps_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
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

Validate offers [manufacturer]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Validate offers [manufacturer]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Validate offers [manufacturer]
        api_response = api_instance.validate_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->validate_offers_manufacturer_v2: %s\n" % e)
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

# **validate_offers_vendor_v2**
> object validate_offers_vendor_v2(contract_id, body=body)

Validate offers [vendor]

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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Validate offers [vendor]
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
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Validate offers [vendor]
        api_response = api_instance.validate_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OffersApi->validate_offers_vendor_v2: %s\n" % e)
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

