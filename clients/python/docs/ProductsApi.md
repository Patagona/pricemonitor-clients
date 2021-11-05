# pricemonitor_api_client.ProductsApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post**](ProductsApi.md#api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/pricedumpingstats | 
[**api_v3_manufacturer_contracts_contract_id_offers_shop_query_post**](ProductsApi.md#api_v3_manufacturer_contracts_contract_id_offers_shop_query_post) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/shop/query | 
[**api_v3_manufacturer_contracts_contract_id_offers_stats_query_post**](ProductsApi.md#api_v3_manufacturer_contracts_contract_id_offers_stats_query_post) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/stats/query | 
[**api_v3_manufacturer_contracts_contract_id_products_put**](ProductsApi.md#api_v3_manufacturer_contracts_contract_id_products_put) | **PUT** /api/v3/manufacturer/contracts/{contractId}/products | Set products via CSV file
[**api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post**](ProductsApi.md#api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post) | **POST** /api/v3/vendor/contracts/{contractId}/offers/pricedumpingstats | 
[**api_v3_vendor_contracts_contract_id_offers_shop_query_post**](ProductsApi.md#api_v3_vendor_contracts_contract_id_offers_shop_query_post) | **POST** /api/v3/vendor/contracts/{contractId}/offers/shop/query | 
[**api_v3_vendor_contracts_contract_id_offers_stats_query_post**](ProductsApi.md#api_v3_vendor_contracts_contract_id_offers_stats_query_post) | **POST** /api/v3/vendor/contracts/{contractId}/offers/stats/query | 
[**api_v3_vendor_contracts_contract_id_products_post**](ProductsApi.md#api_v3_vendor_contracts_contract_id_products_post) | **POST** /api/v3/vendor/contracts/{contractId}/products | Add products in bulk
[**api_v3_vendor_contracts_contract_id_products_put**](ProductsApi.md#api_v3_vendor_contracts_contract_id_products_put) | **PUT** /api/v3/vendor/contracts/{contractId}/products | Set products via CSV file
[**delete_products**](ProductsApi.md#delete_products) | **DELETE** /api/v3/vendor/contracts/{contractId}/products | Delete products
[**delete_products_manufacturer_v3**](ProductsApi.md#delete_products_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/products | 
[**get_extended_tags**](ProductsApi.md#get_extended_tags) | **GET** /api/v3/vendor/contracts/{contractId}/products/{productId}/extendedtags | Return the extended tags for the given product
[**get_extended_tags_manufacturer_v3**](ProductsApi.md#get_extended_tags_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/products/{productId}/extendedtags | 
[**get_mappings_vendor_v2**](ProductsApi.md#get_mappings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/productidentifiermapping | 
[**get_offers**](ProductsApi.md#get_offers) | **GET** /api/2/v/contracts/{contractId}/result/offers | Get all offers for all products
[**get_product_filters_vendor_v2**](ProductsApi.md#get_product_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Get all the filters of a given product for the given contract.
[**get_product_monitoring_status_stats_vendor_v3**](ProductsApi.md#get_product_monitoring_status_stats_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/monitoringstatus/stats | 
[**get_product_monitoring_status_vendor_v3**](ProductsApi.md#get_product_monitoring_status_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/monitoringstatus | 
[**get_product_price_recommendation_history**](ProductsApi.md#get_product_price_recommendation_history) | **GET** /api/v3/vendor/contracts/{contractId}/products/{productId}/pricerecommendationhistory | 
[**get_products**](ProductsApi.md#get_products) | **GET** /api/2/v/contracts/{contractId}/products | Get all products
[**get_tag_values_manufacturer_v2**](ProductsApi.md#get_tag_values_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags/{key} | 
[**get_tag_values_vendor_v2**](ProductsApi.md#get_tag_values_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags/{key} | 
[**get_tags_manufacturer_v2**](ProductsApi.md#get_tags_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags | 
[**get_tags_vendor_v2**](ProductsApi.md#get_tags_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags | 
[**monitoring_pipeline_upsert_search_attempts_manufacturer_v3**](ProductsApi.md#monitoring_pipeline_upsert_search_attempts_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/monitoringpipeline/v1/searchattempts | 
[**monitoring_pipeline_upsert_search_attempts_vendor_v3**](ProductsApi.md#monitoring_pipeline_upsert_search_attempts_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/monitoringpipeline/v1/searchattempts | 
[**patch_product_manufacturer_v3**](ProductsApi.md#patch_product_manufacturer_v3) | **PATCH** /api/v3/manufacturer/contracts/{contractId}/products/{productId} | 
[**patch_product_vendor_v3**](ProductsApi.md#patch_product_vendor_v3) | **PATCH** /api/v3/vendor/contracts/{contractId}/products/{productId} | 
[**post_amazon_buybox_product_stats_v3**](ProductsApi.md#post_amazon_buybox_product_stats_v3) | **POST** /api/v3/vendor/contracts/{contractId}/products/amazon/buybox/stats | Retrieve latest Amazon Buybox statistics per product and amazon domain for a given time range.
[**post_mappings_vendor_v2**](ProductsApi.md#post_mappings_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/productidentifiermapping | 
[**put_csv_products**](ProductsApi.md#put_csv_products) | **PUT** /api/2/v/contracts/{contractId}/products/csv | Set products via CSV file
[**put_product_filters_vendor_v2**](ProductsApi.md#put_product_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Store the filters of a given product for the given contract.
[**put_products_csv_manufacturer_v2**](ProductsApi.md#put_products_csv_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/products/csv | 
[**put_products_vendor_v2**](ProductsApi.md#put_products_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/products | 
[**query_products_by_filter_manufacturer_v3**](ProductsApi.md#query_products_by_filter_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/products/query | 
[**query_products_by_filter_vendor_v3**](ProductsApi.md#query_products_by_filter_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/products/query | 
[**query_products_manufacturer_v3**](ProductsApi.md#query_products_manufacturer_v3) | **POST** /api/v3.1/manufacturer/contracts/{contractId}/products/query | 
[**query_products_vendor_v3**](ProductsApi.md#query_products_vendor_v3) | **POST** /api/v3.1/vendor/contracts/{contractId}/products/query | 
[**save_sales**](ProductsApi.md#save_sales) | **POST** /api/1/{contractId}/products/sales | 
[**shop_integration_post_request_vendor_v2**](ProductsApi.md#shop_integration_post_request_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/products/import | 


# **api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post**
> QueryPriceDumpingStatsApiResponse api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)



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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_offers_pricedumpingstats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **api_v3_manufacturer_contracts_contract_id_offers_shop_query_post**
> QueryOffersOfShopV3ApiResponse api_v3_manufacturer_contracts_contract_id_offers_shop_query_post(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)



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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_shop_query_post(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_offers_shop_query_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_shop_query_post(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_offers_shop_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **api_v3_manufacturer_contracts_contract_id_offers_stats_query_post**
> PostOfferStatisticsApiResponse api_v3_manufacturer_contracts_contract_id_offers_stats_query_post(contract_id, post_offer_statistics_request)



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
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_stats_query_post(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_offers_stats_query_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_offers_stats_query_post(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_offers_stats_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **api_v3_manufacturer_contracts_contract_id_products_put**
> PutProductsApiResponse api_v3_manufacturer_contracts_contract_id_products_put(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)

Set products via CSV file

This operation is used to import products into the pricemonitor. This process is represented by a task, which is processed asynchronously. In the response you will receive a url which is used to check the status of the import process. <br>  When the process is done all products in csv file from the request body will be in the pricemonitor. Products that were already present before have been updated and new products have been added. <br>  Warning: All products that were in the pricemonitor before but are not present in the new import will be deleted.  Identification of the products is done based on the identifying attributes (see parameter: patagona-product-identifying-attributes)

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
    contract_id = 'qbcxvb' # str | ID of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | Comma separated list of csv columns that identify a product uniquely
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products
patagona_product_gtin = 'gtin-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_products_put(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_products_put: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | Comma separated list of csv columns that identify a product uniquely
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products
patagona_product_gtin = 'gtin-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file
        api_response = api_instance.api_v3_manufacturer_contracts_contract_id_products_put(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_manufacturer_contracts_contract_id_products_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **content_type** | **str**|  | 
 **patagona_product_identifying_attributes** | **str**| Comma separated list of csv columns that identify a product uniquely | 
 **patagona_product_name** | **str**| Csv column that contains the product name | 
 **patagona_product_reference_price** | **str**| Csv column that contains the reference price | 
 **patagona_decimal_separator** | **str**| Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \&quot;,\&quot;, \&quot;.\&quot; | 
 **patagona_csv_column_separator** | **str**| The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **patagona_csv_quotation_character** | **str**| The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **body** | **str**| CSV file containing the products | 
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

# **api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post**
> QueryPriceDumpingStatsApiResponse api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)



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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_offers_pricedumpingstats_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **api_v3_vendor_contracts_contract_id_offers_shop_query_post**
> QueryOffersOfShopV3ApiResponse api_v3_vendor_contracts_contract_id_offers_shop_query_post(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)



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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_shop_query_post(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_offers_shop_query_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_shop_query_post(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_offers_shop_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **api_v3_vendor_contracts_contract_id_offers_stats_query_post**
> PostOfferStatisticsApiResponse api_v3_vendor_contracts_contract_id_offers_stats_query_post(contract_id, post_offer_statistics_request)



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
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_stats_query_post(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_offers_stats_query_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.api_v3_vendor_contracts_contract_id_offers_stats_query_post(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_offers_stats_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **api_v3_vendor_contracts_contract_id_products_post**
> BulkedPostProductsApiResponse api_v3_vendor_contracts_contract_id_products_post(contract_id, content_type, patagona_tags_decimal_separator, post_products_request)

Add products in bulk

This operation is used to import products into the pricemonitor:<br> Products that are already present will be updated and new products will be added. Identification of the products is done based on the identifying attributes, which need to be provided via the request body.<br><br> Attention:<br> This endpoint should only be used when dealing with large number of products at your side is an issue. Otherwise please use the PUT-counterpart of this endpoint which accepts products via a csv file.<br><br> Note:<br> This endpoint should be used in conjunction with: DELETE  /api/v3/vendor/contracts/{contractId}/products.<br><br> Procedure:<br> 1. Add your products in bulks with multiple requests via this endpoint.<br> 2. Send a DELETE request to /api/v3/vendor/contracts/{contractId}/products    and set the parameter updatedMax to a date which is older or equal to your first request from step 1.

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
    contract_id = 'qbcxvb' # str | ID of the contract
content_type = 'application/json' # str | 
patagona_tags_decimal_separator = '.' # str | The decimal separator is used for parsing numbers in tags. English and German number formats are supported: dot and comma.
post_products_request = pricemonitor_api_client.PostProductsRequest() # PostProductsRequest | The body contains the products which should be added

    try:
        # Add products in bulk
        api_response = api_instance.api_v3_vendor_contracts_contract_id_products_post(contract_id, content_type, patagona_tags_decimal_separator, post_products_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_products_post: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
content_type = 'application/json' # str | 
patagona_tags_decimal_separator = '.' # str | The decimal separator is used for parsing numbers in tags. English and German number formats are supported: dot and comma.
post_products_request = pricemonitor_api_client.PostProductsRequest() # PostProductsRequest | The body contains the products which should be added

    try:
        # Add products in bulk
        api_response = api_instance.api_v3_vendor_contracts_contract_id_products_post(contract_id, content_type, patagona_tags_decimal_separator, post_products_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **api_v3_vendor_contracts_contract_id_products_put**
> PutProductsApiResponse api_v3_vendor_contracts_contract_id_products_put(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_product_min_price, patagona_product_max_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)

Set products via CSV file

This operation is used to import products into the pricemonitor. This process is represented by a task, which is processed asynchronously. In the response you will receive a url which is used to check the status of the import process. <br>  When the process is done all products in csv file from the request body will be in the pricemonitor. Products that were already present before have been updated and new products have been added. <br>  Warning: All products that were in the pricemonitor before but are not present in the new import will be deleted.  Identification of the products is done based on the identifying attributes (see parameter: patagona-product-identifying-attributes)

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
    contract_id = 'qbcxvb' # str | ID of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | Comma separated list of csv columns that identify a product uniquely
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_product_min_price = 'min-price-column' # str | Csv column that contains the min price
patagona_product_max_price = 'max-price-column' # str | Csv column that contains the max price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ It can be provided either as text or as Base64 encoded string (e.g. needed for tab as separator). \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products
patagona_product_gtin = 'max-price-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file
        api_response = api_instance.api_v3_vendor_contracts_contract_id_products_put(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_product_min_price, patagona_product_max_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_products_put: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | Comma separated list of csv columns that identify a product uniquely
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_product_min_price = 'min-price-column' # str | Csv column that contains the min price
patagona_product_max_price = 'max-price-column' # str | Csv column that contains the max price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ It can be provided either as text or as Base64 encoded string (e.g. needed for tab as separator). \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products
patagona_product_gtin = 'max-price-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file
        api_response = api_instance.api_v3_vendor_contracts_contract_id_products_put(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_product_min_price, patagona_product_max_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->api_v3_vendor_contracts_contract_id_products_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **content_type** | **str**|  | 
 **patagona_product_identifying_attributes** | **str**| Comma separated list of csv columns that identify a product uniquely | 
 **patagona_product_name** | **str**| Csv column that contains the product name | 
 **patagona_product_reference_price** | **str**| Csv column that contains the reference price | 
 **patagona_product_min_price** | **str**| Csv column that contains the min price | 
 **patagona_product_max_price** | **str**| Csv column that contains the max price | 
 **patagona_decimal_separator** | **str**| Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \&quot;,\&quot;, \&quot;.\&quot; | 
 **patagona_csv_column_separator** | **str**| The csv column separator \\ It can be provided either as text or as Base64 encoded string (e.g. needed for tab as separator). \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **patagona_csv_quotation_character** | **str**| The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **body** | **str**| CSV file containing the products | 
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

# **delete_products**
> DeleteProductsApiResponse delete_products(contract_id, updated_max=updated_max)

Delete products

Delete all products or delete products by a last updated timestamp.

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
    contract_id = 'qbcxvb' # str | ID of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Last updated timestamp of products, formatted as ISO Date (i.e. 2019-11-20T13:46:13Z) in UTC.<br> Products can be deleted which haven't been updated since the specified timestamp.<br> If the query parameter is missing all products are deleted. (optional)

    try:
        # Delete products
        api_response = api_instance.delete_products(contract_id, updated_max=updated_max)
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
    contract_id = 'qbcxvb' # str | ID of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Last updated timestamp of products, formatted as ISO Date (i.e. 2019-11-20T13:46:13Z) in UTC.<br> Products can be deleted which haven't been updated since the specified timestamp.<br> If the query parameter is missing all products are deleted. (optional)

    try:
        # Delete products
        api_response = api_instance.delete_products(contract_id, updated_max=updated_max)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->delete_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **updated_max** | **datetime**| Last updated timestamp of products, formatted as ISO Date (i.e. 2019-11-20T13:46:13Z) in UTC.&lt;br&gt; Products can be deleted which haven&#39;t been updated since the specified timestamp.&lt;br&gt; If the query parameter is missing all products are deleted. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_products_manufacturer_v3**
> object delete_products_manufacturer_v3(contract_id, updated_max=updated_max)



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
    contract_id = 'qbcxvb' # str | ID of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.delete_products_manufacturer_v3(contract_id, updated_max=updated_max)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->delete_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
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
    contract_id = 'qbcxvb' # str | ID of the contract
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
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 

    try:
        api_response = api_instance.get_extended_tags_manufacturer_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_extended_tags_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
input_type = 'input_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
input_type = 'input_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

    try:
        api_response = api_instance.get_mappings_vendor_v2(contract_id, input_type, identifiers)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_mappings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    api_instance = pricemonitor_api_client.ProductsApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | Start product index for pagination
limit = 56 # int | Number of products for pagination
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{endDate} - 48 hours to {endDate}' if {endDate} is given or NOW - 48 hours if both are omitted. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{startDate} to {startDate} + 48 hours' if {startDate} is given or NOW - 48 hours if both are omitted. (optional)

    try:
        # Get all offers for all products
        api_response = api_instance.get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_offers: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | Start product index for pagination
limit = 56 # int | Number of products for pagination
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{endDate} - 48 hours to {endDate}' if {endDate} is given or NOW - 48 hours if both are omitted. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{startDate} to {startDate} + 48 hours' if {startDate} is given or NOW - 48 hours if both are omitted. (optional)

    try:
        # Get all offers for all products
        api_response = api_instance.get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**| Start product index for pagination | 
 **limit** | **int**| Number of products for pagination | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is &#39;{endDate} - 48 hours to {endDate}&#39; if {endDate} is given or NOW - 48 hours if both are omitted. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is &#39;{startDate} to {startDate} + 48 hours&#39; if {startDate} is given or NOW - 48 hours if both are omitted. | [optional] 

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
    contract_id = 'qbcxvb' # str | ID of the contract
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
    contract_id = 'qbcxvb' # str | ID of the contract
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
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_product_monitoring_status_stats_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_monitoring_status_stats_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

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
    contract_id = 'qbcxvb' # str | ID of the contract
product_ids = [56] # list[int] | The product ids for which the monitoring state should be returned

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_ids = [56] # list[int] | The product ids for which the monitoring state should be returned

    try:
        api_response = api_instance.get_product_monitoring_status_vendor_v3(contract_id, product_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_monitoring_status_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = '862342' # str | ID of the product in pricemonitor
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{endDate} - 48 hours to {endDate}' if {endDate} is given or NOW - 48 hours if both are omitted. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{startDate} to {startDate} + 48 hours' if {startDate} is given or NOW - 48 hours if both are omitted. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = '862342' # str | ID of the product in pricemonitor
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{endDate} - 48 hours to {endDate}' if {endDate} is given or NOW - 48 hours if both are omitted. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is '{startDate} to {startDate} + 48 hours' if {startDate} is given or NOW - 48 hours if both are omitted. (optional)

    try:
        api_response = api_instance.get_product_price_recommendation_history(contract_id, product_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_product_price_recommendation_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **str**| ID of the product in pricemonitor | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is &#39;{endDate} - 48 hours to {endDate}&#39; if {endDate} is given or NOW - 48 hours if both are omitted. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted, the range is &#39;{startDate} to {startDate} + 48 hours&#39; if {startDate} is given or NOW - 48 hours if both are omitted. | [optional] 

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

# **get_products**
> list[Product] get_products(contract_id, attributes)

Get all products

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
    contract_id = 'qbcxvb' # str | ID of the contract
attributes = 'attributes_example' # str | null

    try:
        # Get all products
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
    contract_id = 'qbcxvb' # str | ID of the contract
attributes = 'attributes_example' # str | null

    try:
        # Get all products
        api_response = api_instance.get_products(contract_id, attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **attributes** | **str**| null | 

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
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_tag_values_manufacturer_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tag_values_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_tag_values_vendor_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tag_values_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_tags_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tags_manufacturer_v2: %s\n" % e)
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

# **get_tags_vendor_v2**
> object get_tags_vendor_v2(contract_id)



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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_tags_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->get_tags_vendor_v2: %s\n" % e)
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

# **monitoring_pipeline_upsert_search_attempts_manufacturer_v3**
> object monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->monitoring_pipeline_upsert_search_attempts_manufacturer_v3: %s\n" % e)
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

# **monitoring_pipeline_upsert_search_attempts_vendor_v3**
> object monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->monitoring_pipeline_upsert_search_attempts_vendor_v3: %s\n" % e)
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

# **patch_product_manufacturer_v3**
> object patch_product_manufacturer_v3(contract_id, product_id, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.patch_product_manufacturer_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->patch_product_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.patch_product_vendor_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->patch_product_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

# **post_amazon_buybox_product_stats_v3**
> AmazonBuyboxProductStatsV3ApiResponse post_amazon_buybox_product_stats_v3(contract_id, com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3=com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3)

Retrieve latest Amazon Buybox statistics per product and amazon domain for a given time range.

Provides latest Amazon Buybox statistics - product is in Amazon Buybox for Prime users - product is in Amazon Buybox for Non-Prime users per product on Amazon domain for a given time range. 

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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAmazonBuyboxProductsStatsRequestV3() # ComPatagonaPricemonitorShareApiPostAmazonBuyboxProductsStatsRequestV3 | Request body contains list of product identifiers, start date time and end date time. Endpoint searches for latest Amazon Buybox product statistics with product identifiers in the given time range defined by [start date, end date].  (optional)

    try:
        # Retrieve latest Amazon Buybox statistics per product and amazon domain for a given time range.
        api_response = api_instance.post_amazon_buybox_product_stats_v3(contract_id, com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3=com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_amazon_buybox_product_stats_v3: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAmazonBuyboxProductsStatsRequestV3() # ComPatagonaPricemonitorShareApiPostAmazonBuyboxProductsStatsRequestV3 | Request body contains list of product identifiers, start date time and end date time. Endpoint searches for latest Amazon Buybox product statistics with product identifiers in the given time range defined by [start date, end date].  (optional)

    try:
        # Retrieve latest Amazon Buybox statistics per product and amazon domain for a given time range.
        api_response = api_instance.post_amazon_buybox_product_stats_v3(contract_id, com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3=com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_amazon_buybox_product_stats_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_amazon_buybox_products_stats_request_v3** | [**ComPatagonaPricemonitorShareApiPostAmazonBuyboxProductsStatsRequestV3**](ComPatagonaPricemonitorShareApiPostAmazonBuyboxProductsStatsRequestV3.md)| Request body contains list of product identifiers, start date time and end date time. Endpoint searches for latest Amazon Buybox product statistics with product identifiers in the given time range defined by [start date, end date].  | [optional] 

### Return type

[**AmazonBuyboxProductStatsV3ApiResponse**](AmazonBuyboxProductStatsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Amazon Buybox statistics per product |  -  |
**400** | Returned if: - The request body is not a valid JSON string. - More than 10,000 product statistics are requested. - The start date is after the end date. - The time range [startDate,endDate] is larger than 48h. - The contract has more than one amazon domain configured.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mappings_vendor_v2**
> object post_mappings_vendor_v2(contract_id, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.post_mappings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->post_mappings_vendor_v2: %s\n" % e)
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

# **put_csv_products**
> put_csv_products(contract_id, body)

Set products via CSV file

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
    contract_id = 'qbcxvb' # str | ID of the contract
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file
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
    contract_id = 'qbcxvb' # str | ID of the contract
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file
        api_instance.put_csv_products(contract_id, body)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_csv_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
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
    contract_id = 'qbcxvb' # str | ID of the contract
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
 **contract_id** | **str**| ID of the contract | 
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

# **put_products_csv_manufacturer_v2**
> object put_products_csv_manufacturer_v2(contract_id, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_products_csv_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_csv_manufacturer_v2: %s\n" % e)
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

# **put_products_vendor_v2**
> object put_products_vendor_v2(contract_id, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_products_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->put_products_vendor_v2: %s\n" % e)
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

# **query_products_by_filter_manufacturer_v3**
> QueryProductsByFilterManufacturerV3ApiResponse query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)



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
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        api_response = api_instance.query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_by_filter_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        api_response = api_instance.query_products_by_filter_vendor_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_by_filter_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
        api_response = api_instance.query_products_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_api_query** | [**ComPatagonaPricemonitorShareApiApiQuery**](ComPatagonaPricemonitorShareApiApiQuery.md)| The body contains the products query. &lt;br&gt; Currently, it supports only product queries for two attributes:&lt;br&gt; &lt;ul&gt;   &lt;li&gt; by \&quot;customerProductId\&quot;&lt;/li&gt;   &lt;li&gt; by \&quot;productId\&quot; (Patagona&#39;s internal product id). Allowed values for &#39;productId&#39; are numerical integer values&lt;/li&gt; &lt;/ul&gt; The maximum allowed limit in the pagination is 10000. &lt;br&gt; Pagination works with respective to the given products query. &lt;br&gt; This is most relevant when querying for a set of customerProductId&#39;s. &lt;br&gt; When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId&#39;s in the query and keep the pagination at start: 0, limit: 10000. &lt;br&gt; The only allowed pattern is currently: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: ${start}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: ${limit} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [${customerProductIds as a list of strings}] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt; &lt;br&gt; example: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: 0, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: 10 &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [\&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot;, \&quot;4\&quot;, \&quot;5\&quot;, \&quot;6\&quot;, \&quot;7\&quot;, \&quot;8\&quot;, \&quot;9\&quot;, \&quot;10\&quot;] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt;  | [optional] 

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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
        api_response = api_instance.query_products_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->query_products_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_api_query** | [**ComPatagonaPricemonitorShareApiApiQuery**](ComPatagonaPricemonitorShareApiApiQuery.md)| The body contains the products query. &lt;br&gt; Currently, it supports only product queries for two attributes:&lt;br&gt; &lt;ul&gt;   &lt;li&gt; by \&quot;customerProductId\&quot;&lt;/li&gt;   &lt;li&gt; by \&quot;productId\&quot; (Patagona&#39;s internal product id). Allowed values for &#39;productId&#39; are numerical integer values&lt;/li&gt; &lt;/ul&gt; The maximum allowed limit in the pagination is 10000. &lt;br&gt; Pagination works with respective to the given products query. &lt;br&gt; This is most relevant when querying for a set of customerProductId&#39;s. &lt;br&gt; When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId&#39;s in the query and keep the pagination at start: 0, limit: 10000. &lt;br&gt; The only allowed pattern is currently: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: ${start}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: ${limit} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [${customerProductIds as a list of strings}] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt; &lt;br&gt; example: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: 0, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: 10 &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [\&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot;, \&quot;4\&quot;, \&quot;5\&quot;, \&quot;6\&quot;, \&quot;7\&quot;, \&quot;8\&quot;, \&quot;9\&quot;, \&quot;10\&quot;] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt;  | [optional] 

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

# **save_sales**
> object save_sales(contract_id, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.save_sales(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->save_sales: %s\n" % e)
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
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.save_sales(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->save_sales: %s\n" % e)
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

# **shop_integration_post_request_vendor_v2**
> object shop_integration_post_request_vendor_v2(contract_id, path, body=body)



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
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
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
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.shop_integration_post_request_vendor_v2(contract_id, path, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductsApi->shop_integration_post_request_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
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

