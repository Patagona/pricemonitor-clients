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
    contract_id = 'qbcxvb' # str | ID of the contract
post_scenario_strategy_request = pricemonitor_api_client.PostScenarioStrategyRequest() # PostScenarioStrategyRequest | The scenario strategy to be stored. Including the necessary metadata. (optional)

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
    contract_id = 'qbcxvb' # str | ID of the contract
post_scenario_strategy_request = pricemonitor_api_client.PostScenarioStrategyRequest() # PostScenarioStrategyRequest | The scenario strategy to be stored. Including the necessary metadata. (optional)

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
 **contract_id** | **str**| ID of the contract | 
 **post_scenario_strategy_request** | [**PostScenarioStrategyRequest**](PostScenarioStrategyRequest.md)| The scenario strategy to be stored. Including the necessary metadata. | [optional] 

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
**200** | A new scenario strategy was added |  -  |
**400** | Strategy must be valid and consistent with the schema version. Required fields need to be filled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scenarios_metadata**
> list[ScenarioStrategyMetadataResponseApiResponse] get_all_scenarios_metadata(contract_id)

Get all scenario strategies

Get a list of all scenario strategy metadata for a contract.

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
    contract_id = 'qbcxvb' # str | ID of the contract

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
    contract_id = 'qbcxvb' # str | ID of the contract

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
 **contract_id** | **str**| ID of the contract | 

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

Get a scenario strategy with the provided scenario id.

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
    contract_id = 'qbcxvb' # str | ID of the contract
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
    contract_id = 'qbcxvb' # str | ID of the contract
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
 **contract_id** | **str**| ID of the contract | 
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
**200** | A scenario strategy |  -  |
**404** | Scenario strategy with the provided Id was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

