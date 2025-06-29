# pricemonitor_api_client.ProductsApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_products**](ProductsApi.md#delete_products) | **DELETE** /api/v3/vendor/contracts/{contractId}/products | Delete products
[**delete_products_manufacturer_v3**](ProductsApi.md#delete_products_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/products | Delete products [manufacturer]
[**get_amazon_buybox_product_stats_v3**](ProductsApi.md#get_amazon_buybox_product_stats_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/amazon/buybox/stats | Get Amazon Buy Box statistics for time range
[**get_extended_tags**](ProductsApi.md#get_extended_tags) | **GET** /api/v3/vendor/contracts/{contractId}/products/{productId}/extendedtags | Return the extended tags for the given product
[**get_extended_tags_manufacturer_v3**](ProductsApi.md#get_extended_tags_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/products/{productId}/extendedtags | Get extended tags [manufacturer]
[**get_mappings_vendor_v2**](ProductsApi.md#get_mappings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/productidentifiermapping | Get product mappings
[**get_product_filters_vendor_v2**](ProductsApi.md#get_product_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Get all the filters of a given product for the given contract.
[**get_product_monitoring_status_stats_vendor_v3**](ProductsApi.md#get_product_monitoring_status_stats_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/monitoringstatus/stats | Get product monitoring status stats [vendor]
[**get_product_monitoring_status_vendor_v3**](ProductsApi.md#get_product_monitoring_status_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/monitoringstatus | Get monitoring status of queried products
[**get_product_price_recommendation_history**](ProductsApi.md#get_product_price_recommendation_history) | **GET** /api/v3/vendor/contracts/{contractId}/products/{productId}/pricerecommendationhistory | Get price recommendations for one product
[**get_product_properties_v3**](ProductsApi.md#get_product_properties_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/{productId}/properties | Get all product properties for a product
[**get_product_property_keys_v3**](ProductsApi.md#get_product_property_keys_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/properties/keys | Get all product properties keys
[**get_products**](ProductsApi.md#get_products) | **GET** /api/2/v/contracts/{contractId}/products | Get all products for a contract
[**get_tag_values_manufacturer_v2**](ProductsApi.md#get_tag_values_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags/{key} | Get product tag values [manufacturer]
[**get_tag_values_vendor_v2**](ProductsApi.md#get_tag_values_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags/{key} | Get tag values for key
[**get_tags_manufacturer_v2**](ProductsApi.md#get_tags_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags | Get product tags [manufacturer]
[**get_tags_vendor_v2**](ProductsApi.md#get_tags_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags | Get product tags [vendor]
[**monitoring_pipeline_upsert_search_attempts_manufacturer_v3**](ProductsApi.md#monitoring_pipeline_upsert_search_attempts_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/monitoringpipeline/v1/searchattempts | Update monitoring pipeline search attempts [manufacturer]
[**monitoring_pipeline_upsert_search_attempts_vendor_v3**](ProductsApi.md#monitoring_pipeline_upsert_search_attempts_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/monitoringpipeline/v1/searchattempts | Update monitoring pipeline search attempts [vendor]
[**patch_product_manufacturer_v3**](ProductsApi.md#patch_product_manufacturer_v3) | **PATCH** /api/v3/manufacturer/contracts/{contractId}/products/{productId} | Update product [manufacturer]
[**patch_product_vendor_v3**](ProductsApi.md#patch_product_vendor_v3) | **PATCH** /api/v3/vendor/contracts/{contractId}/products/{productId} | Update product [vendor]
[**post_mappings_vendor_v2**](ProductsApi.md#post_mappings_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/productidentifiermapping | Update product identifier mapping
[**post_offer_statistics_vendor_query**](ProductsApi.md#post_offer_statistics_vendor_query) | **POST** /api/v3/vendor/contracts/{contractId}/offers/stats/query | Get offer statistics per product
[**post_products_import_vendor_v3**](ProductsApi.md#post_products_import_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/products | Add products in bulk (JSON)
[**put_csv_products**](ProductsApi.md#put_csv_products) | **PUT** /api/2/v/contracts/{contractId}/products/csv | Set products via CSV file (V2)
[**put_csv_products_manufacturer_v3**](ProductsApi.md#put_csv_products_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/products | Set products via CSV file (V3)
[**put_product_filters_vendor_v2**](ProductsApi.md#put_product_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Store the filters of a given product for the given contract.
[**put_product_properties_v3**](ProductsApi.md#put_product_properties_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/products/{productId}/properties | Manage product properties for a product
[**put_products_csv_manufacturer_v2**](ProductsApi.md#put_products_csv_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/products/csv | Set products via CSV file [manufacturer]
[**put_products_import_vendor_v3**](ProductsApi.md#put_products_import_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/products | Add products in bulk (CSV)
[**put_products_vendor_v2**](ProductsApi.md#put_products_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/products | Update products in bulk (JSON)
[**query_offers_price_dumping_stats_manufacturer_v3**](ProductsApi.md#query_offers_price_dumping_stats_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/pricedumpingstats | Query price dumping statistics
[**query_offers_price_dumping_stats_vendor_v3**](ProductsApi.md#query_offers_price_dumping_stats_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/offers/pricedumpingstats | Query price dumping statistics
[**query_offers_shop_manufacturer_v3**](ProductsApi.md#query_offers_shop_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/shop/query | Get all offers [manufacturer]
[**query_offers_shop_vendor_v3**](ProductsApi.md#query_offers_shop_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/offers/shop/query | Get all offers [vendor]
[**query_offers_stats_manufacturer_v3**](ProductsApi.md#query_offers_stats_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/stats/query | Query offer statistics per product
[**query_products_by_filter_manufacturer_v3**](ProductsApi.md#query_products_by_filter_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/products/query | Get products of a contract
[**query_products_by_filter_vendor_v3**](ProductsApi.md#query_products_by_filter_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/products/query | Query products of a contract
[**query_products_manufacturer_v3**](ProductsApi.md#query_products_manufacturer_v3) | **POST** /api/v3.1/manufacturer/contracts/{contractId}/products/query | Query products for manufacturer
[**query_products_vendor_v3**](ProductsApi.md#query_products_vendor_v3) | **POST** /api/v3.1/vendor/contracts/{contractId}/products/query | Query products of a contract
[**shop_integration_post_request_vendor_v2**](ProductsApi.md#shop_integration_post_request_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/products/import | Update shop integration import


# **delete_products**
> DeleteProductsApiResponse delete_products(contract_id, updated_max=updated_max, tag_key=tag_key, tag_value=tag_value)

Delete products

Delete all products or delete products by a last updated timestamp and/or a tag.  **Note:** Avoid any product import requests concurrently with DELETE requests to prevent potential issues. 

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Last updated timestamp of products, formatted as ISO Date (i.e. 2019-11-20T13:46:13Z) in UTC.<br> Products can be deleted which haven't been updated since the specified timestamp.<br> If the query parameter is missing all products are deleted. (optional)
tag_key = 'tag_key_example' # str | Tag key to consider for deleting products. This parameter works in combination with tagValue. (optional)
tag_value = 'tag_value_example' # str | Tag value to consider for deleting products. This parameter works in combination with tagKey. (optional)

    try:
        # Delete products
        api_response = api_instance.delete_products(contract_id, updated_max=updated_max, tag_key=tag_key, tag_value=tag_value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->delete_products: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Last updated timestamp of products, formatted as ISO Date (i.e. 2019-11-20T13:46:13Z) in UTC.<br> Products can be deleted which haven't been updated since the specified timestamp.<br> If the query parameter is missing all products are deleted. (optional)
tag_key = 'tag_key_example' # str | Tag key to consider for deleting products. This parameter works in combination with tagValue. (optional)
tag_value = 'tag_value_example' # str | Tag value to consider for deleting products. This parameter works in combination with tagKey. (optional)

    try:
        # Delete products
        api_response = api_instance.delete_products(contract_id, updated_max=updated_max, tag_key=tag_key, tag_value=tag_value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->delete_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **updated_max** | **datetime**| Last updated timestamp of products, formatted as ISO Date (i.e. 2019-11-20T13:46:13Z) in UTC.&lt;br&gt; Products can be deleted which haven&#39;t been updated since the specified timestamp.&lt;br&gt; If the query parameter is missing all products are deleted. | [optional] 
 **tag_key** | **str**| Tag key to consider for deleting products. This parameter works in combination with tagValue. | [optional] 
 **tag_value** | **str**| Tag value to consider for deleting products. This parameter works in combination with tagKey. | [optional] 

### Return type

[**DeleteProductsApiResponse**](DeleteProductsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the number of deleted products. |  -  |
**400** | Tags specified for deleting products are specified partially (either tagKey or tagValue is provided).  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_products_manufacturer_v3**
> object delete_products_manufacturer_v3(contract_id, updated_max=updated_max)

Delete products [manufacturer]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Delete products [manufacturer]
        api_response = api_instance.delete_products_manufacturer_v3(contract_id, updated_max=updated_max)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->delete_products_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Delete products [manufacturer]
        api_response = api_instance.delete_products_manufacturer_v3(contract_id, updated_max=updated_max)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->delete_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **updated_max** | **datetime**|  | [optional] 

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

# **get_amazon_buybox_product_stats_v3**
> AmazonBuyboxProductStatsV3ApiResponse get_amazon_buybox_product_stats_v3(contract_id, start_date=start_date, end_date=end_date, start=start, limit=limit)

Get Amazon Buy Box statistics for time range

Provides latest Amazon Buy Box statistics, i.e., whether a - product is in Amazon Buy Box for Prime users - product is in Amazon Buy Box for Non-Prime users per product per Amazon domain for a given time range. 

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
start = 0 # int | Where to start fetching the Amazon Buy Box statistics. Must be positive. Default value is 0. (optional)
limit = 50000 # int | Maximum number of results. Must be positive and not bigger than 50,000. Default value is 50,000. (optional)

    try:
        # Get Amazon Buy Box statistics for time range
        api_response = api_instance.get_amazon_buybox_product_stats_v3(contract_id, start_date=start_date, end_date=end_date, start=start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_amazon_buybox_product_stats_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
start = 0 # int | Where to start fetching the Amazon Buy Box statistics. Must be positive. Default value is 0. (optional)
limit = 50000 # int | Maximum number of results. Must be positive and not bigger than 50,000. Default value is 50,000. (optional)

    try:
        # Get Amazon Buy Box statistics for time range
        api_response = api_instance.get_amazon_buybox_product_stats_v3(contract_id, start_date=start_date, end_date=end_date, start=start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_amazon_buybox_product_stats_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **start_date** | **datetime**| **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-15T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;endDate&#x60; is provided: &#x60;startDate&#x60; &#x3D; &#x60;endDate&#x60; - 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 
 **end_date** | **datetime**| **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., &#x60;2024-01-16T10:30:00Z&#x60;)  **Default behavior:** - If omitted and &#x60;startDate&#x60; is provided: &#x60;endDate&#x60; &#x3D; &#x60;startDate&#x60; + 48 hours - If both omitted: range is &#x60;NOW - 48 hours&#x60; to &#x60;NOW&#x60;  | [optional] 
 **start** | **int**| Where to start fetching the Amazon Buy Box statistics. Must be positive. Default value is 0. | [optional] 
 **limit** | **int**| Maximum number of results. Must be positive and not bigger than 50,000. Default value is 50,000. | [optional] 

### Return type

[**AmazonBuyboxProductStatsV3ApiResponse**](AmazonBuyboxProductStatsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Amazon Buybox statistics per product |  -  |
**400** | Returned if: - The request body is not a valid JSON string. - The start date is after the end date. - The time range [startDate,endDate] is larger than 48h. - The start parameter is negative - The limit parameter is negative and larger than 50,000 - The contract has more than one amazon domain configured.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_tags**
> GetExtendedTagsApiResponse get_extended_tags(contract_id, product_id)

Return the extended tags for the given product

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = '1' # str | ID of the product

    try:
        # Return the extended tags for the given product
        api_response = api_instance.get_extended_tags(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_extended_tags: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = '1' # str | ID of the product

    try:
        # Return the extended tags for the given product
        api_response = api_instance.get_extended_tags(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_extended_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_id** | **str**| ID of the product | 

### Return type

[**GetExtendedTagsApiResponse**](GetExtendedTagsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of ExtendedTags for the given product. |  -  |
**404** | Given product does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_tags_manufacturer_v3**
> object get_extended_tags_manufacturer_v3(contract_id, product_id)

Get extended tags [manufacturer]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | 

    try:
        # Get extended tags [manufacturer]
        api_response = api_instance.get_extended_tags_manufacturer_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_extended_tags_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | 

    try:
        # Get extended tags [manufacturer]
        api_response = api_instance.get_extended_tags_manufacturer_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_extended_tags_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_id** | **str**|  | 

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

# **get_mappings_vendor_v2**
> object get_mappings_vendor_v2(contract_id, input_type, identifiers)

Get product mappings

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
input_type = 'input_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

    try:
        # Get product mappings
        api_response = api_instance.get_mappings_vendor_v2(contract_id, input_type, identifiers)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_mappings_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
input_type = 'input_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

    try:
        # Get product mappings
        api_response = api_instance.get_mappings_vendor_v2(contract_id, input_type, identifiers)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_mappings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **input_type** | **str**|  | 
 **identifiers** | [**list[str]**](str.md)|  | 

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

# **get_product_filters_vendor_v2**
> OfferFilterApiResponse get_product_filters_vendor_v2(contract_id, list_type, product_id)

Get all the filters of a given product for the given contract.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 

    try:
        # Get all the filters of a given product for the given contract.
        api_response = api_instance.get_product_filters_vendor_v2(contract_id, list_type, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_filters_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 

    try:
        # Get all the filters of a given product for the given contract.
        api_response = api_instance.get_product_filters_vendor_v2(contract_id, list_type, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **list_type** | **str**|  | 
 **product_id** | **str**|  | 

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

# **get_product_monitoring_status_stats_vendor_v3**
> GetProductMonitoringStatusStatsVendorV3ApiResponse get_product_monitoring_status_stats_vendor_v3(contract_id)

Get product monitoring status stats [vendor]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get product monitoring status stats [vendor]
        api_response = api_instance.get_product_monitoring_status_stats_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_monitoring_status_stats_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get product monitoring status stats [vendor]
        api_response = api_instance.get_product_monitoring_status_stats_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_monitoring_status_stats_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

### Return type

[**GetProductMonitoringStatusStatsVendorV3ApiResponse**](GetProductMonitoringStatusStatsVendorV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains the monitoring status stats per domain |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_monitoring_status_vendor_v3**
> GetProductMonitoringStatusVendorV3ApiResponse get_product_monitoring_status_vendor_v3(contract_id, product_ids)

Get monitoring status of queried products

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_ids = [56] # list[int] | The product ids for which the monitoring state should be returned

    try:
        # Get monitoring status of queried products
        api_response = api_instance.get_product_monitoring_status_vendor_v3(contract_id, product_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_monitoring_status_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_ids = [56] # list[int] | The product ids for which the monitoring state should be returned

    try:
        # Get monitoring status of queried products
        api_response = api_instance.get_product_monitoring_status_vendor_v3(contract_id, product_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_monitoring_status_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_ids** | [**list[int]**](int.md)| The product ids for which the monitoring state should be returned | 

### Return type

[**GetProductMonitoringStatusVendorV3ApiResponse**](GetProductMonitoringStatusVendorV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring status of the queried products |  -  |

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = '862342' # str | Internal product identifier in the pricemonitor system
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get price recommendations for one product
        api_response = api_instance.get_product_price_recommendation_history(contract_id, product_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_price_recommendation_history: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = '862342' # str | Internal product identifier in the pricemonitor system
start_date = '2024-01-15T00:00:00Z' # datetime | **Start of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-15T10:30:00Z`)  **Default behavior:** - If omitted and `endDate` is provided: `startDate` = `endDate` - 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)
end_date = '2024-01-16T23:59:59Z' # datetime | **End of time range** for data retrieval.  Format: ISO 8601 date-time in UTC (e.g., `2024-01-16T10:30:00Z`)  **Default behavior:** - If omitted and `startDate` is provided: `endDate` = `startDate` + 48 hours - If both omitted: range is `NOW - 48 hours` to `NOW`  (optional)

    try:
        # Get price recommendations for one product
        api_response = api_instance.get_product_price_recommendation_history(contract_id, product_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_price_recommendation_history: %s\n" % e)
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

# **get_product_properties_v3**
> GetProductPropertiesV3ApiResponse get_product_properties_v3(contract_id, product_id)

Get all product properties for a product

This endpoint returns a list product properties for a certain product and contract. Product properties represent additional information for a product, independent of the imported products and tags.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 12345678 # int | ID of the product (Omnia's internal product id)

    try:
        # Get all product properties for a product
        api_response = api_instance.get_product_properties_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_properties_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 12345678 # int | ID of the product (Omnia's internal product id)

    try:
        # Get all product properties for a product
        api_response = api_instance.get_product_properties_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_properties_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_id** | **int**| ID of the product (Omnia&#39;s internal product id) | 

### Return type

[**GetProductPropertiesV3ApiResponse**](GetProductPropertiesV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of product properties |  -  |
**404** | Returned if the product does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_property_keys_v3**
> StringArrayResponse get_product_property_keys_v3(contract_id)

Get all product properties keys

This endpoint returns a list of distinct product property keys for all imported products of a contract.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all product properties keys
        api_response = api_instance.get_product_property_keys_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_property_keys_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all product properties keys
        api_response = api_instance.get_product_property_keys_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_property_keys_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

### Return type

[**StringArrayResponse**](StringArrayResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of distinct keys of all product properties. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> list[Product] get_products(contract_id, attributes)

Get all products for a contract

**⚠️ DEPRECATED:** This endpoint is deprecated and should no longer be used.  Retrieves all products for a contract without pagination support. This endpoint has performance limitations and lacks proper pagination. Use the newer product query endpoints instead.  **Note:** The `attributes` parameter is required but poorly documented in this legacy version. 

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
attributes = 'gtin,name,referencePrice,tags' # str | **REQUIRED:** Comma-separated list of product attributes to include in the response.  Available attributes: `gtin`, `identifier`, `name`, `referencePrice`, `minPriceBoundary`, `maxPriceBoundary`, `tags`, `strategy` 

    try:
        # Get all products for a contract
        api_response = api_instance.get_products(contract_id, attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_products: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
attributes = 'gtin,name,referencePrice,tags' # str | **REQUIRED:** Comma-separated list of product attributes to include in the response.  Available attributes: `gtin`, `identifier`, `name`, `referencePrice`, `minPriceBoundary`, `maxPriceBoundary`, `tags`, `strategy` 

    try:
        # Get all products for a contract
        api_response = api_instance.get_products(contract_id, attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **attributes** | **str**| **REQUIRED:** Comma-separated list of product attributes to include in the response.  Available attributes: &#x60;gtin&#x60;, &#x60;identifier&#x60;, &#x60;name&#x60;, &#x60;referencePrice&#x60;, &#x60;minPriceBoundary&#x60;, &#x60;maxPriceBoundary&#x60;, &#x60;tags&#x60;, &#x60;strategy&#x60;  | 

### Return type

[**list[Product]**](Product.md)

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

# **get_tag_values_manufacturer_v2**
> object get_tag_values_manufacturer_v2(contract_id, key)

Get product tag values [manufacturer]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
key = 'key_example' # str | 

    try:
        # Get product tag values [manufacturer]
        api_response = api_instance.get_tag_values_manufacturer_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tag_values_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
key = 'key_example' # str | 

    try:
        # Get product tag values [manufacturer]
        api_response = api_instance.get_tag_values_manufacturer_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tag_values_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **key** | **str**|  | 

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

# **get_tag_values_vendor_v2**
> object get_tag_values_vendor_v2(contract_id, key)

Get tag values for key

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
key = 'key_example' # str | 

    try:
        # Get tag values for key
        api_response = api_instance.get_tag_values_vendor_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tag_values_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
key = 'key_example' # str | 

    try:
        # Get tag values for key
        api_response = api_instance.get_tag_values_vendor_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tag_values_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **key** | **str**|  | 

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

# **get_tags_manufacturer_v2**
> object get_tags_manufacturer_v2(contract_id)

Get product tags [manufacturer]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get product tags [manufacturer]
        api_response = api_instance.get_tags_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tags_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get product tags [manufacturer]
        api_response = api_instance.get_tags_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tags_manufacturer_v2: %s\n" % e)
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

# **get_tags_vendor_v2**
> object get_tags_vendor_v2(contract_id)

Get product tags [vendor]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get product tags [vendor]
        api_response = api_instance.get_tags_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tags_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get product tags [vendor]
        api_response = api_instance.get_tags_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tags_vendor_v2: %s\n" % e)
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

# **monitoring_pipeline_upsert_search_attempts_manufacturer_v3**
> object monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)

Update monitoring pipeline search attempts [manufacturer]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update monitoring pipeline search attempts [manufacturer]
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->monitoring_pipeline_upsert_search_attempts_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update monitoring pipeline search attempts [manufacturer]
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->monitoring_pipeline_upsert_search_attempts_manufacturer_v3: %s\n" % e)
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

# **monitoring_pipeline_upsert_search_attempts_vendor_v3**
> object monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)

Update monitoring pipeline search attempts [vendor]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update monitoring pipeline search attempts [vendor]
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->monitoring_pipeline_upsert_search_attempts_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update monitoring pipeline search attempts [vendor]
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->monitoring_pipeline_upsert_search_attempts_vendor_v3: %s\n" % e)
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

# **patch_product_manufacturer_v3**
> object patch_product_manufacturer_v3(contract_id, product_id, body=body)

Update product [manufacturer]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update product [manufacturer]
        api_response = api_instance.patch_product_manufacturer_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->patch_product_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update product [manufacturer]
        api_response = api_instance.patch_product_manufacturer_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->patch_product_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_id** | **str**|  | 
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

# **patch_product_vendor_v3**
> object patch_product_vendor_v3(contract_id, product_id, body=body)

Update product [vendor]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update product [vendor]
        api_response = api_instance.patch_product_vendor_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->patch_product_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update product [vendor]
        api_response = api_instance.patch_product_vendor_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->patch_product_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_id** | **str**|  | 
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

# **post_mappings_vendor_v2**
> object post_mappings_vendor_v2(contract_id, body=body)

Update product identifier mapping

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update product identifier mapping
        api_response = api_instance.post_mappings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_mappings_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update product identifier mapping
        api_response = api_instance.post_mappings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_mappings_vendor_v2: %s\n" % e)
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

# **post_offer_statistics_vendor_query**
> PostOfferStatisticsApiResponse post_offer_statistics_vendor_query(contract_id, post_offer_statistics_request)

Get offer statistics per product

This operation is used to get offer statistics (e.g. offer count, average price) grouped by product and domain.  Warning: This endpoint contains complex filter structure and will be replaced in the future. Currently, we only allow filtering by a list of internal pricemonitor product ids. Please note that offer statistics can only be computed for at **maximum 2500** products at a time.  To use the example request body from below, you have to adjust the `ownShopNames`, the `range` and `filter.right.value`. Where `filter.right.value` has to be a list of internal pricemonitor product ids corresponding to the `contractId` provided as part of the URL.  All prices will be with or without delivery costs depending on the `includeDeliveryCosts` parameter in the body. 

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        # Get offer statistics per product
        api_response = api_instance.post_offer_statistics_vendor_query(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_offer_statistics_vendor_query: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        # Get offer statistics per product
        api_response = api_instance.post_offer_statistics_vendor_query(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_offer_statistics_vendor_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **post_offer_statistics_request** | [**PostOfferStatisticsRequest**](PostOfferStatisticsRequest.md)|  | 

### Return type

[**PostOfferStatisticsApiResponse**](PostOfferStatisticsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. ## How to use this endpoint&#39;s result to get Total Market statistics ### Minimum Price To calculate the minimum price in the total market, you have to take the minimum of the &#x60;minPrice&#x60; of each domain. In the example below, both products have the same min prices: &#x60;min(16.00,7.99) &#x3D; 7.99&#x60;. ### Average Price To calculate the average price in the total market, you have to calculate a **weighted average**, weighing the average price of each domain by its offer count. In the example below we get different results for the average price in the total market for product id &#x60;1001&#x60; and &#x60;1002&#x60; even though they have the same average price in each domain. This is due to the different offer counts:    - product id &#x60;1001&#x60;: &#x60;(20.00 * 4 + 10.00 * 12) / (4 + 12) &#x3D; 12.50&#x60;   - product id &#x60;1002&#x60;: &#x60;(20.00 * 12 + 10.00 * 4) / (12 + 4) &#x3D; 17.50&#x60;  ### Offer Count The offer count of one product in the total market is the sum of the offer counts for all its domains. In the example below, both products would have an offer count of &#x60;12 + 4 &#x3D; 16&#x60;. ### Market Position The market position of a product generally **can not be deduced** from the data provided in this endpoint.  |  -  |
**400** | Returned in case of unparsable request body JSON or unsupported filter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_products_import_vendor_v3**
> BulkedPostProductsApiResponse post_products_import_vendor_v3(contract_id, content_type, patagona_tags_decimal_separator, post_products_request)

Add products in bulk (JSON)

This operation is used to import products into the system from JSON formatted data:<br> Products that are already present will be updated and new products will be added. Identification of the products is done based on the identifying attributes, which need to be provided via the request body.<br><br>Note:<br> This endpoint should be used in conjunction with: DELETE  /api/v3/vendor/contracts/{contractId}/products.<br><br> Procedure:<br> 1. Add your products in bulks with multiple requests via this endpoint.<br> 2. Send a DELETE request to /api/v3/vendor/contracts/{contractId}/products    and set the parameter updatedMax to a date which is older or equal to your first request from step 1.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
content_type = 'application/json' # str | 
patagona_tags_decimal_separator = '.' # str | The decimal separator is used for parsing numbers in tags. English and German number formats are supported: dot and comma.
post_products_request = pricemonitor_api_client.PostProductsRequest() # PostProductsRequest | The body contains the products which should be added

    try:
        # Add products in bulk (JSON)
        api_response = api_instance.post_products_import_vendor_v3(contract_id, content_type, patagona_tags_decimal_separator, post_products_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_products_import_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
content_type = 'application/json' # str | 
patagona_tags_decimal_separator = '.' # str | The decimal separator is used for parsing numbers in tags. English and German number formats are supported: dot and comma.
post_products_request = pricemonitor_api_client.PostProductsRequest() # PostProductsRequest | The body contains the products which should be added

    try:
        # Add products in bulk (JSON)
        api_response = api_instance.post_products_import_vendor_v3(contract_id, content_type, patagona_tags_decimal_separator, post_products_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_products_import_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **content_type** | **str**|  | 
 **patagona_tags_decimal_separator** | **str**| The decimal separator is used for parsing numbers in tags. English and German number formats are supported: dot and comma. | 
 **post_products_request** | [**PostProductsRequest**](PostProductsRequest.md)| The body contains the products which should be added | 

### Return type

[**BulkedPostProductsApiResponse**](BulkedPostProductsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response provides sorted import results in respective to the order of the provided products. |  -  |
**400** | Unable to add products because of invalid request data |  -  |

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file (V2)
        api_instance.put_csv_products(contract_id, body)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_csv_products: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file (V2)
        api_instance.put_csv_products(contract_id, body)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_csv_products: %s\n" % e)
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

# **put_csv_products_manufacturer_v3**
> PutProductsApiResponse put_csv_products_manufacturer_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)

Set products via CSV file (V3)

This operation is used to import products into the pricemonitor. This process is represented by a task, which is processed asynchronously. In the response you will receive a url which is used to check the status of the import process. <br>  When the process is done all products in csv file from the request body will be in the pricemonitor. Products that were already present before have been updated and new products have been added. <br>  Warning: All products that were in the pricemonitor before but are not present in the new import will be deleted.  Identification of the products is done based on the identifying attributes (see parameter: patagona-product-identifying-attributes)'

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | A single CSV column that identify a product uniquely. Avoid using tags as an identifier, as this feature will soon be deprecated. By doing so, you may loose historical market data during product import.
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products. Note: The CSV file should be encoded in UTF-8.
patagona_product_gtin = 'gtin-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file (V3)
        api_response = api_instance.put_csv_products_manufacturer_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_csv_products_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | A single CSV column that identify a product uniquely. Avoid using tags as an identifier, as this feature will soon be deprecated. By doing so, you may loose historical market data during product import.
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products. Note: The CSV file should be encoded in UTF-8.
patagona_product_gtin = 'gtin-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file (V3)
        api_response = api_instance.put_csv_products_manufacturer_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_csv_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **content_type** | **str**|  | 
 **patagona_product_identifying_attributes** | **str**| A single CSV column that identify a product uniquely. Avoid using tags as an identifier, as this feature will soon be deprecated. By doing so, you may loose historical market data during product import. | 
 **patagona_product_name** | **str**| Csv column that contains the product name | 
 **patagona_product_reference_price** | **str**| Csv column that contains the reference price | 
 **patagona_decimal_separator** | **str**| Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \&quot;,\&quot;, \&quot;.\&quot; | 
 **patagona_csv_column_separator** | **str**| The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **patagona_csv_quotation_character** | **str**| The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **body** | **str**| CSV file containing the products. Note: The CSV file should be encoded in UTF-8. | 
 **patagona_product_gtin** | **str**| Csv column that contains the gtin | [optional] 
 **patagona_product_customer_id** | **str**| Csv column that contains an id (There is no requirement for this field to be unique) | [optional] 

### Return type

[**PutProductsApiResponse**](PutProductsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The field data.url in the returned object allows to check the status of the import process. It will point to the endpoint GET /api/2/v/contracts/{contractId}/tasks/{taskId}. \\ The field data.id is the task id corresponding to the product import. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_product_filters_vendor_v2**
> OfferFilterApiResponse put_product_filters_vendor_v2(contract_id, list_type, product_id, and_offer_filter=and_offer_filter)

Store the filters of a given product for the given contract.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the filters of a given product for the given contract.
        api_response = api_instance.put_product_filters_vendor_v2(contract_id, list_type, product_id, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_product_filters_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the filters of a given product for the given contract.
        api_response = api_instance.put_product_filters_vendor_v2(contract_id, list_type, product_id, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_product_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **list_type** | **str**|  | 
 **product_id** | **str**|  | 
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

# **put_product_properties_v3**
> EmptyApiResponse put_product_properties_v3(contract_id, product_id, com_patagona_pricemonitor_share_api_put_product_properties_request_v3)

Manage product properties for a product

This endpoint allows creating, updating, or deleting product properties for a certain product and contract. For deleting product properties, it's sufficient to provide an empty list of product properties. When providing dates, please use the ISO 8601 format. When providing numbers, please use dot as decimal separator.  Product properties represent additional information for a product, independent of imported products and tags. 

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 12345678 # int | ID of the product (Omnia's internal product id)
com_patagona_pricemonitor_share_api_put_product_properties_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3() # ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3 | 

    try:
        # Manage product properties for a product
        api_response = api_instance.put_product_properties_v3(contract_id, product_id, com_patagona_pricemonitor_share_api_put_product_properties_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_product_properties_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
product_id = 12345678 # int | ID of the product (Omnia's internal product id)
com_patagona_pricemonitor_share_api_put_product_properties_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3() # ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3 | 

    try:
        # Manage product properties for a product
        api_response = api_instance.put_product_properties_v3(contract_id, product_id, com_patagona_pricemonitor_share_api_put_product_properties_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_product_properties_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **product_id** | **int**| ID of the product (Omnia&#39;s internal product id) | 
 **com_patagona_pricemonitor_share_api_put_product_properties_request_v3** | [**ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3**](ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3.md)|  | 

### Return type

[**EmptyApiResponse**](EmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The product properties have been stored successfully for the product. |  -  |
**400** | Returned if the request body is invalid: - The request body is not a valid JSON string. - The provided product properties contain duplicated keys. - The provided product properties contain an empty key. - The provided product properties contain a key which is too long. - The provided product properties contain a value which is too long.  |  -  |
**404** | Returned if the product does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_csv_manufacturer_v2**
> object put_products_csv_manufacturer_v2(contract_id, body=body)

Set products via CSV file [manufacturer]

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Set products via CSV file [manufacturer]
        api_response = api_instance.put_products_csv_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_csv_manufacturer_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Set products via CSV file [manufacturer]
        api_response = api_instance.put_products_csv_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_csv_manufacturer_v2: %s\n" % e)
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

# **put_products_import_vendor_v3**
> PutProductsApiResponse put_products_import_vendor_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_product_min_price, patagona_product_max_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)

Add products in bulk (CSV)

This operation is used to import products into the system from CSV formatted data. This process is represented by a task, which is processed asynchronously. In the response you will receive a url which is used to check the status of the import process. <br>  When the process is done all products in csv file from the request body will be in the pricemonitor. Products that were already present before have been updated and new products have been added. <br>  Warning: All products that were in the pricemonitor before but are not present in the new import will be deleted.  Identification of the products is done based on the identifying attributes (see parameter: patagona-product-identifying-attributes)  Note: It is recommended to use the JSON variant to add products as it works synchronously and more efficient.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | A single CSV column that identify a product uniquely. Avoid using tags as an identifier, as this feature will soon be deprecated By doing so, you may loose historical market data during product import.
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_product_min_price = 'min-price-column' # str | Csv column that contains the min price
patagona_product_max_price = 'max-price-column' # str | Csv column that contains the max price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ It can be provided either as text or as Base64 encoded string (e.g. needed for tab as separator). \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products. Note: The CSV file should be encoded in UTF-8.
patagona_product_gtin = 'max-price-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Add products in bulk (CSV)
        api_response = api_instance.put_products_import_vendor_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_product_min_price, patagona_product_max_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_import_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | A single CSV column that identify a product uniquely. Avoid using tags as an identifier, as this feature will soon be deprecated By doing so, you may loose historical market data during product import.
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_product_min_price = 'min-price-column' # str | Csv column that contains the min price
patagona_product_max_price = 'max-price-column' # str | Csv column that contains the max price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ It can be provided either as text or as Base64 encoded string (e.g. needed for tab as separator). \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products. Note: The CSV file should be encoded in UTF-8.
patagona_product_gtin = 'max-price-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Add products in bulk (CSV)
        api_response = api_instance.put_products_import_vendor_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_product_min_price, patagona_product_max_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_import_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **content_type** | **str**|  | 
 **patagona_product_identifying_attributes** | **str**| A single CSV column that identify a product uniquely. Avoid using tags as an identifier, as this feature will soon be deprecated By doing so, you may loose historical market data during product import. | 
 **patagona_product_name** | **str**| Csv column that contains the product name | 
 **patagona_product_reference_price** | **str**| Csv column that contains the reference price | 
 **patagona_product_min_price** | **str**| Csv column that contains the min price | 
 **patagona_product_max_price** | **str**| Csv column that contains the max price | 
 **patagona_decimal_separator** | **str**| Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \&quot;,\&quot;, \&quot;.\&quot; | 
 **patagona_csv_column_separator** | **str**| The csv column separator \\ It can be provided either as text or as Base64 encoded string (e.g. needed for tab as separator). \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **patagona_csv_quotation_character** | **str**| The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **body** | **str**| CSV file containing the products. Note: The CSV file should be encoded in UTF-8. | 
 **patagona_product_gtin** | **str**| Csv column that contains the gtin | [optional] 
 **patagona_product_customer_id** | **str**| Csv column that contains an id (There is no requirement for this field to be unique) | [optional] 

### Return type

[**PutProductsApiResponse**](PutProductsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The field data.url in the returned object allows to check the status of the import process. It will point to the endpoint GET /api/2/v/contracts/{contractId}/tasks/{taskId}. \\ The field data.id is the task id corresponding to the product import. |  -  |

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update products in bulk (JSON)
        api_response = api_instance.put_products_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update products in bulk (JSON)
        api_response = api_instance.put_products_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_vendor_v2: %s\n" % e)
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

# **query_offers_price_dumping_stats_manufacturer_v3**
> QueryPriceDumpingStatsApiResponse query_offers_price_dumping_stats_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)

Query price dumping statistics

This operation is used to query price dumping statistics for a time range for a set of shops.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_price_dumping_stats_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_price_dumping_stats_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_price_dumping_stats_request** | [**ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest**](ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest.md)|  | 

### Return type

[**QueryPriceDumpingStatsApiResponse**](QueryPriceDumpingStatsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the price dumping statistics in the given time range. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_price_dumping_stats_vendor_v3**
> QueryPriceDumpingStatsApiResponse query_offers_price_dumping_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)

Query price dumping statistics

This operation is used to query price dumping statistics for a time range for a set of shops.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_price_dumping_stats_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_price_dumping_stats_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_price_dumping_stats_request** | [**ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest**](ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest.md)|  | 

### Return type

[**QueryPriceDumpingStatsApiResponse**](QueryPriceDumpingStatsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the price dumping statistics in the given time range. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_shop_manufacturer_v3**
> QueryOffersOfShopV3ApiResponse query_offers_shop_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)

Get all offers [manufacturer]

Get all offers of a shop. Please note that it might return offers for inactive products.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        # Get all offers [manufacturer]
        api_response = api_instance.query_offers_shop_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_shop_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        # Get all offers [manufacturer]
        api_response = api_instance.query_offers_shop_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_shop_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3** | [**ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3**](ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.md)|  | 

### Return type

[**QueryOffersOfShopV3ApiResponse**](QueryOffersOfShopV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns offers of the shop |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_shop_vendor_v3**
> QueryOffersOfShopV3ApiResponse query_offers_shop_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)

Get all offers [vendor]

Get all offers of a shop. Please note that it might return offers for inactive products.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        # Get all offers [vendor]
        api_response = api_instance.query_offers_shop_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_shop_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        # Get all offers [vendor]
        api_response = api_instance.query_offers_shop_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_shop_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3** | [**ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3**](ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.md)|  | 

### Return type

[**QueryOffersOfShopV3ApiResponse**](QueryOffersOfShopV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns offers of the shop |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_stats_manufacturer_v3**
> PostOfferStatisticsApiResponse query_offers_stats_manufacturer_v3(contract_id, post_offer_statistics_request)

Query offer statistics per product

This operation is used to get offer statistics (e.g. offer count, average price) grouped by product and domain. Warning: This endpoint contains complex query structure and will be replaced in the future. Please note that offer statistics can only be computed for at maximum 2500 products at a time.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_manufacturer_v3(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_stats_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_manufacturer_v3(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_offers_stats_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **post_offer_statistics_request** | [**PostOfferStatisticsRequest**](PostOfferStatisticsRequest.md)|  | 

### Return type

[**PostOfferStatisticsApiResponse**](PostOfferStatisticsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. |  -  |
**400** | Returned in case of unparsable request body JSON or unsupported filter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_products_by_filter_manufacturer_v3**
> QueryProductsByFilterManufacturerV3ApiResponse query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)

Get products of a contract

This endpoint can be used for querying either all products or certain products by product ids.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        # Get products of a contract
        api_response = api_instance.query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_by_filter_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        # Get products of a contract
        api_response = api_instance.query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_by_filter_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **query_products_request_v3** | [**QueryProductsRequestV3**](QueryProductsRequestV3.md)| The body contains the products query. | [optional] 

### Return type

[**QueryProductsByFilterManufacturerV3ApiResponse**](QueryProductsByFilterManufacturerV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of found products. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_products_by_filter_vendor_v3**
> QueryProductsByFilterVendorV3ApiResponse query_products_by_filter_vendor_v3(contract_id, query_products_request_v3=query_products_request_v3)

Query products of a contract

This endpoint can be used for querying either all products or certain products by product ids.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        # Query products of a contract
        api_response = api_instance.query_products_by_filter_vendor_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_by_filter_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        # Query products of a contract
        api_response = api_instance.query_products_by_filter_vendor_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_by_filter_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **query_products_request_v3** | [**QueryProductsRequestV3**](QueryProductsRequestV3.md)| The body contains the products query. | [optional] 

### Return type

[**QueryProductsByFilterVendorV3ApiResponse**](QueryProductsByFilterVendorV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of found products. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_products_manufacturer_v3**
> QueryProductsManufacturerV3ApiResponse query_products_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)

Query products for manufacturer

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
        # Query products for manufacturer
        api_response = api_instance.query_products_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_manufacturer_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
        # Query products for manufacturer
        api_response = api_instance.query_products_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_api_query** | [**ComPatagonaPricemonitorShareApiApiQuery**](ComPatagonaPricemonitorShareApiApiQuery.md)| The body contains the products query. &lt;br&gt; Currently, it supports only product queries for two attributes:&lt;br&gt; &lt;ul&gt;   &lt;li&gt; by \&quot;customerProductId\&quot;&lt;/li&gt;   &lt;li&gt; by \&quot;productId\&quot; (Patagona&#39;s internal product id). Allowed values for &#39;productId&#39; are numerical integer values&lt;/li&gt; &lt;/ul&gt; The maximum allowed limit in the pagination is 10000. &lt;br&gt; For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. &lt;br&gt; This is most relevant when querying for a set of customerProductId&#39;s. &lt;br&gt; When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId&#39;s in the query and keep the pagination at start: 0, limit: 10000. &lt;br&gt; The only allowed pattern is currently: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: ${start}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: ${limit} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [${customerProductIds as a list of strings}] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt; &lt;br&gt; example: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: 0, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: 10 &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [\&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot;, \&quot;4\&quot;, \&quot;5\&quot;, \&quot;6\&quot;, \&quot;7\&quot;, \&quot;8\&quot;, \&quot;9\&quot;, \&quot;10\&quot;] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt;  | [optional] 

### Return type

[**QueryProductsManufacturerV3ApiResponse**](QueryProductsManufacturerV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of found products. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_products_vendor_v3**
> QueryProductsVendorV3ApiResponse query_products_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)

Query products of a contract

This endpoint can be used for querying either all products or certain products by the 'customerProductId' or 'productId'.

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> It also contains a boolean optional parameter 'includeTags' which is used to include the tags of the products in the response. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"includeTags\": ${includeTags} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"includeTags\": true <br> } <br>  (optional)

    try:
        # Query products of a contract
        api_response = api_instance.query_products_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_vendor_v3: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> It also contains a boolean optional parameter 'includeTags' which is used to include the tags of the products in the response. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"includeTags\": ${includeTags} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"includeTags\": true <br> } <br>  (optional)

    try:
        # Query products of a contract
        api_response = api_instance.query_products_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **com_patagona_pricemonitor_share_api_api_query** | [**ComPatagonaPricemonitorShareApiApiQuery**](ComPatagonaPricemonitorShareApiApiQuery.md)| The body contains the products query. &lt;br&gt; Currently, it supports only product queries for two attributes:&lt;br&gt; &lt;ul&gt;   &lt;li&gt; by \&quot;customerProductId\&quot;&lt;/li&gt;   &lt;li&gt; by \&quot;productId\&quot; (Patagona&#39;s internal product id). Allowed values for &#39;productId&#39; are numerical integer values&lt;/li&gt; &lt;/ul&gt; The maximum allowed limit in the pagination is 10000. &lt;br&gt; For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. &lt;br&gt; This is most relevant when querying for a set of customerProductId&#39;s. &lt;br&gt; When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId&#39;s in the query and keep the pagination at start: 0, limit: 10000. &lt;br&gt; It also contains a boolean optional parameter &#39;includeTags&#39; which is used to include the tags of the products in the response. &lt;br&gt; The only allowed pattern is currently: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: ${start}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: ${limit} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [${customerProductIds as a list of strings}] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;includeTags\&quot;: ${includeTags} &lt;br&gt; } &lt;br&gt; &lt;br&gt; example: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: 0, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: 10 &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [\&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot;, \&quot;4\&quot;, \&quot;5\&quot;, \&quot;6\&quot;, \&quot;7\&quot;, \&quot;8\&quot;, \&quot;9\&quot;, \&quot;10\&quot;] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;includeTags\&quot;: true &lt;br&gt; } &lt;br&gt;  | [optional] 

### Return type

[**QueryProductsVendorV3ApiResponse**](QueryProductsVendorV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of found products. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shop_integration_post_request_vendor_v2**
> object shop_integration_post_request_vendor_v2(contract_id, path, body=body)

Update shop integration import

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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
path = 'path_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update shop integration import
        api_response = api_instance.shop_integration_post_request_vendor_v2(contract_id, path, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->shop_integration_post_request_vendor_v2: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
path = 'path_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        # Update shop integration import
        api_response = api_instance.shop_integration_post_request_vendor_v2(contract_id, path, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->shop_integration_post_request_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **path** | **str**|  | 
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

