# pricemonitor_api_client.AccountApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AccountApi.md#authenticate) | **POST** /login | 
[**change_password**](AccountApi.md#change_password) | **PUT** /api/account/password | 
[**check_user_confirmation**](AccountApi.md#check_user_confirmation) | **HEAD** /api/account/confirm/{token} | Check if a specific confirmation token exists
[**confirm_user**](AccountApi.md#confirm_user) | **POST** /api/account/confirm/{token} | Confirm an unconfirmed user
[**delete_user_role**](AccountApi.md#delete_user_role) | **DELETE** /api/2/users/{userId}/role/{roleName} | 
[**login_by_auth_token**](AccountApi.md#login_by_auth_token) | **GET** /api/login/token/{token} | 
[**logout**](AccountApi.md#logout) | **POST** /logout | 
[**post_account_v3**](AccountApi.md#post_account_v3) | **POST** /api/v3/account | Create a new user account
[**refresh_access_token**](AccountApi.md#refresh_access_token) | **POST** /api/v3/account/token/refresh | Refresh an access token using the refresh token.
[**request_access_token**](AccountApi.md#request_access_token) | **POST** /api/v3/account/token/access | Issues a token which can be used to access protected resources of the Pricemonitor API.
[**request_new_password**](AccountApi.md#request_new_password) | **POST** /api/account/password/reset | Request a new password
[**reset_password**](AccountApi.md#reset_password) | **PUT** /api/account/password/reset | Reset the password
[**update_user_role**](AccountApi.md#update_user_role) | **PUT** /api/2/users/{userId}/role/{roleName} | 
[**user_info**](AccountApi.md#user_info) | **GET** /api/account | Details of the current user
[**user_signup**](AccountApi.md#user_signup) | **POST** /api/account | Create a new user account in the Pricemonitor


# **authenticate**
> object authenticate()



### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    
    try:
        api_response = api_instance.authenticate()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->authenticate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authenticate with the API and create a session |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> object change_password()



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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    
    try:
        api_response = api_instance.change_password()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->change_password: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    
    try:
        api_response = api_instance.change_password()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->change_password: %s\n" % e)
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
**200** | Change the current users password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_user_confirmation**
> check_user_confirmation(token)

Check if a specific confirmation token exists

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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    token = 'token_example' # str | 

    try:
        # Check if a specific confirmation token exists
        api_instance.check_user_confirmation(token)
    except ApiException as e:
        print("Exception when calling AccountApi->check_user_confirmation: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    token = 'token_example' # str | 

    try:
        # Check if a specific confirmation token exists
        api_instance.check_user_confirmation(token)
    except ApiException as e:
        print("Exception when calling AccountApi->check_user_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |
**204** | Confirmation token was found |  -  |
**404** | No such confirmation token was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_user**
> confirm_user(token, body)

Confirm an unconfirmed user

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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    token = 'token_example' # str | 
body = 'body_example' # str | The password that should be set on the confirmed user

    try:
        # Confirm an unconfirmed user
        api_instance.confirm_user(token, body)
    except ApiException as e:
        print("Exception when calling AccountApi->confirm_user: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    token = 'token_example' # str | 
body = 'body_example' # str | The password that should be set on the confirmed user

    try:
        # Confirm an unconfirmed user
        api_instance.confirm_user(token, body)
    except ApiException as e:
        print("Exception when calling AccountApi->confirm_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **body** | **str**| The password that should be set on the confirmed user | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |
**204** | User was confirmed &amp; logged in |  -  |
**400** | Unable to confirm the user because of bad request data |  -  |
**500** | Unable to confirm the user because of an unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_role**
> object delete_user_role(user_id, role_name)



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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 

    try:
        api_response = api_instance.delete_user_role(user_id, role_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->delete_user_role: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 

    try:
        api_response = api_instance.delete_user_role(user_id, role_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->delete_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **role_name** | **str**|  | 

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

# **login_by_auth_token**
> object login_by_auth_token(token)



### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    token = 'token_example' # str | 

    try:
        api_response = api_instance.login_by_auth_token(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->login_by_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> object logout()



### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    
    try:
        api_response = api_instance.logout()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deauthenticate with the API and destroy the current session |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_account_v3**
> PostAccountResponseV3ApiResponse post_account_v3(com_patagona_pricemonitor_share_api_post_account_request_v3=com_patagona_pricemonitor_share_api_post_account_request_v3)

Create a new user account

### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    com_patagona_pricemonitor_share_api_post_account_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAccountRequestV3() # ComPatagonaPricemonitorShareApiPostAccountRequestV3 | Request body for creating a new user account. It must contain name, email and password. (optional)

    try:
        # Create a new user account
        api_response = api_instance.post_account_v3(com_patagona_pricemonitor_share_api_post_account_request_v3=com_patagona_pricemonitor_share_api_post_account_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->post_account_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_account_request_v3** | [**ComPatagonaPricemonitorShareApiPostAccountRequestV3**](ComPatagonaPricemonitorShareApiPostAccountRequestV3.md)| Request body for creating a new user account. It must contain name, email and password. | [optional] 

### Return type

[**PostAccountResponseV3ApiResponse**](PostAccountResponseV3ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The account information of the newly created account. |  -  |
**400** | Returned if: - The Request body is not a valid JSON string - The user account name is empty - The email doesn&#39;t match a valid email format - The password length is less than 6 characters long - The enpoint was requested too often - The given email address already exists  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_access_token**
> PostAccessTokenResponseV3ApiResponse refresh_access_token(com_patagona_pricemonitor_share_api_post_refresh_access_token_request_v3=com_patagona_pricemonitor_share_api_post_refresh_access_token_request_v3)

Refresh an access token using the refresh token.

An access token, a refresh token and a refresh token id are issued upon valid credentials. See [/api/v3/account/token/access](#/account/requestAccessToken) for more details. When an access token expired, it can be re-issued (or refreshed) using the refresh token and refresh token id, the one obtained upon valid credentials. 

### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    com_patagona_pricemonitor_share_api_post_refresh_access_token_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostRefreshAccessTokenRequestV3() # ComPatagonaPricemonitorShareApiPostRefreshAccessTokenRequestV3 | Request body contains the refresh token (optional)

    try:
        # Refresh an access token using the refresh token.
        api_response = api_instance.refresh_access_token(com_patagona_pricemonitor_share_api_post_refresh_access_token_request_v3=com_patagona_pricemonitor_share_api_post_refresh_access_token_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->refresh_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_refresh_access_token_request_v3** | [**ComPatagonaPricemonitorShareApiPostRefreshAccessTokenRequestV3**](ComPatagonaPricemonitorShareApiPostRefreshAccessTokenRequestV3.md)| Request body contains the refresh token | [optional] 

### Return type

[**PostAccessTokenResponseV3ApiResponse**](PostAccessTokenResponseV3ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access token response |  -  |
**400** | Returned if: - The request body is not a valid JSON string. - The refresh token is invalid and/or expired.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_access_token**
> PostAccessTokenResponseV3ApiResponse request_access_token(com_patagona_pricemonitor_share_api_post_access_token_request_v3=com_patagona_pricemonitor_share_api_post_access_token_request_v3)

Issues a token which can be used to access protected resources of the Pricemonitor API.

### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    com_patagona_pricemonitor_share_api_post_access_token_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAccessTokenRequestV3() # ComPatagonaPricemonitorShareApiPostAccessTokenRequestV3 | Request body contains credentials i.e email address and password. (optional)

    try:
        # Issues a token which can be used to access protected resources of the Pricemonitor API.
        api_response = api_instance.request_access_token(com_patagona_pricemonitor_share_api_post_access_token_request_v3=com_patagona_pricemonitor_share_api_post_access_token_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->request_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_access_token_request_v3** | [**ComPatagonaPricemonitorShareApiPostAccessTokenRequestV3**](ComPatagonaPricemonitorShareApiPostAccessTokenRequestV3.md)| Request body contains credentials i.e email address and password. | [optional] 

### Return type

[**PostAccessTokenResponseV3ApiResponse**](PostAccessTokenResponseV3ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access token response |  -  |
**400** | Returned if: - The request body is not a valid JSON string. - The email address is invalid. - The given email address does not exist in our system. - Invalid credentials are specified.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_new_password**
> str request_new_password(com_patagona_pricemonitor_share_api_post_new_password_request=com_patagona_pricemonitor_share_api_post_new_password_request)

Request a new password

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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    com_patagona_pricemonitor_share_api_post_new_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostNewPasswordRequest() # ComPatagonaPricemonitorShareApiPostNewPasswordRequest | Request a new password. (optional)

    try:
        # Request a new password
        api_response = api_instance.request_new_password(com_patagona_pricemonitor_share_api_post_new_password_request=com_patagona_pricemonitor_share_api_post_new_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->request_new_password: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    com_patagona_pricemonitor_share_api_post_new_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostNewPasswordRequest() # ComPatagonaPricemonitorShareApiPostNewPasswordRequest | Request a new password. (optional)

    try:
        # Request a new password
        api_response = api_instance.request_new_password(com_patagona_pricemonitor_share_api_post_new_password_request=com_patagona_pricemonitor_share_api_post_new_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->request_new_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_new_password_request** | [**ComPatagonaPricemonitorShareApiPostNewPasswordRequest**](ComPatagonaPricemonitorShareApiPostNewPasswordRequest.md)| Request a new password. | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response upon password request |  -  |
**400** | Invalid request body is specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> str reset_password(com_patagona_pricemonitor_share_api_put_reset_password_request=com_patagona_pricemonitor_share_api_put_reset_password_request)

Reset the password

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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    com_patagona_pricemonitor_share_api_put_reset_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutResetPasswordRequest() # ComPatagonaPricemonitorShareApiPutResetPasswordRequest | Reset a password (optional)

    try:
        # Reset the password
        api_response = api_instance.reset_password(com_patagona_pricemonitor_share_api_put_reset_password_request=com_patagona_pricemonitor_share_api_put_reset_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->reset_password: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    com_patagona_pricemonitor_share_api_put_reset_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutResetPasswordRequest() # ComPatagonaPricemonitorShareApiPutResetPasswordRequest | Reset a password (optional)

    try:
        # Reset the password
        api_response = api_instance.reset_password(com_patagona_pricemonitor_share_api_put_reset_password_request=com_patagona_pricemonitor_share_api_put_reset_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_put_reset_password_request** | [**ComPatagonaPricemonitorShareApiPutResetPasswordRequest**](ComPatagonaPricemonitorShareApiPutResetPasswordRequest.md)| Reset a password | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password changed successfully. |  -  |
**400** | Password didn&#39;t change successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_role**
> object update_user_role(user_id, role_name, body=body)



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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_user_role(user_id, role_name, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->update_user_role: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_user_role(user_id, role_name, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->update_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **role_name** | **str**|  | 
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

# **user_info**
> ComPatagonaPricemonitorShareApiUserInfo user_info()

Details of the current user

Returns the current user with its companies and contracts

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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    
    try:
        # Details of the current user
        api_response = api_instance.user_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->user_info: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    
    try:
        # Details of the current user
        api_response = api_instance.user_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComPatagonaPricemonitorShareApiUserInfo**](ComPatagonaPricemonitorShareApiUserInfo.md)

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

# **user_signup**
> user_signup(user_signup_request)

Create a new user account in the Pricemonitor

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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    user_signup_request = pricemonitor_api_client.UserSignupRequest() # UserSignupRequest | The user signup data

    try:
        # Create a new user account in the Pricemonitor
        api_instance.user_signup(user_signup_request)
    except ApiException as e:
        print("Exception when calling AccountApi->user_signup: %s\n" % e)
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
    api_instance = pricemonitor_api_client.AccountApi(api_client)
    user_signup_request = pricemonitor_api_client.UserSignupRequest() # UserSignupRequest | The user signup data

    try:
        # Create a new user account in the Pricemonitor
        api_instance.user_signup(user_signup_request)
    except ApiException as e:
        print("Exception when calling AccountApi->user_signup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_signup_request** | [**UserSignupRequest**](UserSignupRequest.md)| The user signup data | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |
**201** | User was created and confirmation eMail was sent |  -  |
**400** | Unable to create the user because of bad request data |  -  |
**500** | Unable to create the user because of an unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

