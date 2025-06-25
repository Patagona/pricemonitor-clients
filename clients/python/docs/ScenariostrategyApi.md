# pricemonitor_api_client.ScenariostrategyApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pricing_strategy_scenario**](ScenariostrategyApi.md#add_pricing_strategy_scenario) | **POST** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios | Add scenario strategy
[**get_all_scenarios_metadata**](ScenariostrategyApi.md#get_all_scenarios_metadata) | **GET** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios | Get all scenario strategies
[**get_scenario_by_id**](ScenariostrategyApi.md#get_scenario_by_id) | **GET** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios/{scenarioId} | Get scenario strategy


# **add_pricing_strategy_scenario**
> PostScenarioStrategyResponseApiResponse add_pricing_strategy_scenario(contract_id, post_scenario_strategy_request=post_scenario_strategy_request)

Add scenario strategy

**🔒 INTERNAL:** Creates a new scenario strategy for pricing simulations.  Scenario strategies allow for \"what-if\" pricing analysis and testing different pricing approaches before applying them to live products. 

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
    api_instance = pricemonitor_api_client.ScenariostrategyApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
post_scenario_strategy_request = pricemonitor_api_client.PostScenarioStrategyRequest() # PostScenarioStrategyRequest | The scenario strategy to be created, including the necessary metadata and configuration. (optional)

    try:
        # Add scenario strategy
        api_response = api_instance.add_pricing_strategy_scenario(contract_id, post_scenario_strategy_request=post_scenario_strategy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScenariostrategyApi->add_pricing_strategy_scenario: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ScenariostrategyApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
post_scenario_strategy_request = pricemonitor_api_client.PostScenarioStrategyRequest() # PostScenarioStrategyRequest | The scenario strategy to be created, including the necessary metadata and configuration. (optional)

    try:
        # Add scenario strategy
        api_response = api_instance.add_pricing_strategy_scenario(contract_id, post_scenario_strategy_request=post_scenario_strategy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScenariostrategyApi->add_pricing_strategy_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **post_scenario_strategy_request** | [**PostScenarioStrategyRequest**](PostScenarioStrategyRequest.md)| The scenario strategy to be created, including the necessary metadata and configuration. | [optional] 

### Return type

[**PostScenarioStrategyResponseApiResponse**](PostScenarioStrategyResponseApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scenario strategy created successfully |  -  |
**400** | Request validation failed. Common reasons include: - Strategy configuration is invalid or inconsistent with the schema version - Required fields are missing or empty - Invalid JSON structure  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scenarios_metadata**
> list[ScenarioStrategyMetadataResponseApiResponse] get_all_scenarios_metadata(contract_id)

Get all scenario strategies

**🔒 INTERNAL:** Retrieves a list of all scenario strategy metadata for a specific contract.  Scenario strategies are used for pricing simulations and \"what-if\" analysis. Each strategy contains metadata including creation date, version information, and configuration details. 

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
    api_instance = pricemonitor_api_client.ScenariostrategyApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all scenario strategies
        api_response = api_instance.get_all_scenarios_metadata(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScenariostrategyApi->get_all_scenarios_metadata: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ScenariostrategyApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract

    try:
        # Get all scenario strategies
        api_response = api_instance.get_all_scenarios_metadata(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScenariostrategyApi->get_all_scenarios_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 

### Return type

[**list[ScenarioStrategyMetadataResponseApiResponse]**](ScenarioStrategyMetadataResponseApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all scenario strategy metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_by_id**
> ScenarioStrategyResponse get_scenario_by_id(contract_id, scenario_id)

Get scenario strategy

**🔒 INTERNAL:** Retrieves a specific scenario strategy by its ID.  Returns the complete scenario strategy configuration including metadata, creation details, and the strategy definition. 

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
    api_instance = pricemonitor_api_client.ScenariostrategyApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
scenario_id = 56 # int | ID of the required scenario strategy

    try:
        # Get scenario strategy
        api_response = api_instance.get_scenario_by_id(contract_id, scenario_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScenariostrategyApi->get_scenario_by_id: %s\n" % e)
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
    api_instance = pricemonitor_api_client.ScenariostrategyApi(api_client)
    contract_id = 'qbcxvb' # str | Unique identifier of the contract
scenario_id = 56 # int | ID of the required scenario strategy

    try:
        # Get scenario strategy
        api_response = api_instance.get_scenario_by_id(contract_id, scenario_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScenariostrategyApi->get_scenario_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Unique identifier of the contract | 
 **scenario_id** | **int**| ID of the required scenario strategy | 

### Return type

[**ScenarioStrategyResponse**](ScenarioStrategyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scenario strategy details retrieved successfully |  -  |
**404** | Scenario strategy with the provided ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

