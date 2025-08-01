# coding: utf-8

"""
    Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.7216
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pricemonitor_api_client.api_client import ApiClient
from pricemonitor_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FeatureFlagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_feature_flag(self, com_patagona_pricemonitor_share_api_post_feature_flag_request, **kwargs):  # noqa: E501
        """Create feature flag  # noqa: E501

        **🔒 INTERNAL:** Creates a new feature flag in the system.  Feature flags must have a unique key that follows the pattern `[a-zA-Z0-9._-]+` and cannot exceed 128 characters in length.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feature_flag(com_patagona_pricemonitor_share_api_post_feature_flag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ComPatagonaPricemonitorShareApiPostFeatureFlagRequest com_patagona_pricemonitor_share_api_post_feature_flag_request: The feature flag to be created (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreateFeatureFlagApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_feature_flag_with_http_info(com_patagona_pricemonitor_share_api_post_feature_flag_request, **kwargs)  # noqa: E501

    def create_feature_flag_with_http_info(self, com_patagona_pricemonitor_share_api_post_feature_flag_request, **kwargs):  # noqa: E501
        """Create feature flag  # noqa: E501

        **🔒 INTERNAL:** Creates a new feature flag in the system.  Feature flags must have a unique key that follows the pattern `[a-zA-Z0-9._-]+` and cannot exceed 128 characters in length.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feature_flag_with_http_info(com_patagona_pricemonitor_share_api_post_feature_flag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ComPatagonaPricemonitorShareApiPostFeatureFlagRequest com_patagona_pricemonitor_share_api_post_feature_flag_request: The feature flag to be created (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CreateFeatureFlagApiResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'com_patagona_pricemonitor_share_api_post_feature_flag_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_feature_flag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'com_patagona_pricemonitor_share_api_post_feature_flag_request' is set
        if self.api_client.client_side_validation and ('com_patagona_pricemonitor_share_api_post_feature_flag_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['com_patagona_pricemonitor_share_api_post_feature_flag_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `com_patagona_pricemonitor_share_api_post_feature_flag_request` when calling `create_feature_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'com_patagona_pricemonitor_share_api_post_feature_flag_request' in local_var_params:
            body_params = local_var_params['com_patagona_pricemonitor_share_api_post_feature_flag_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/controlpanel/api/feature-flags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateFeatureFlagApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_feature_flag(self, key, **kwargs):  # noqa: E501
        """Delete feature flag  # noqa: E501

        **🔒 INTERNAL:** Deletes a feature flag from the system (soft delete).  The feature flag is marked as deleted but preserved in the database for audit purposes. Once deleted, the flag key becomes unavailable for new flags.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_feature_flag(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: Feature flag key identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EmptyApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_feature_flag_with_http_info(key, **kwargs)  # noqa: E501

    def delete_feature_flag_with_http_info(self, key, **kwargs):  # noqa: E501
        """Delete feature flag  # noqa: E501

        **🔒 INTERNAL:** Deletes a feature flag from the system (soft delete).  The feature flag is marked as deleted but preserved in the database for audit purposes. Once deleted, the flag key becomes unavailable for new flags.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_feature_flag_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: Feature flag key identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EmptyApiResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_feature_flag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `delete_feature_flag`")  # noqa: E501

        if self.api_client.client_side_validation and ('key' in local_var_params and  # noqa: E501
                                                        len(local_var_params['key']) > 128):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `key` when calling `delete_feature_flag`, length must be less than or equal to `128`")  # noqa: E501
        if self.api_client.client_side_validation and 'key' in local_var_params and not re.search(r'^[a-zA-Z0-9._-]+$', local_var_params['key']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `key` when calling `delete_feature_flag`, must conform to the pattern `/^[a-zA-Z0-9._-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/controlpanel/api/feature-flags/{key}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_feature_flags(self, **kwargs):  # noqa: E501
        """Get all feature flags  # noqa: E501

        **🔒 INTERNAL:** Retrieves a list of all feature flags configured in the system.  Feature flags are used to control the availability of application features and can be managed through the control panel interface.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_feature_flags(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetAllFeatureFlagsApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_all_feature_flags_with_http_info(**kwargs)  # noqa: E501

    def get_all_feature_flags_with_http_info(self, **kwargs):  # noqa: E501
        """Get all feature flags  # noqa: E501

        **🔒 INTERNAL:** Retrieves a list of all feature flags configured in the system.  Feature flags are used to control the availability of application features and can be managed through the control panel interface.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_feature_flags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetAllFeatureFlagsApiResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_feature_flags" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/controlpanel/api/feature-flags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAllFeatureFlagsApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feature_flag_by_key(self, key, **kwargs):  # noqa: E501
        """Get feature flag by key  # noqa: E501

        **🔒 INTERNAL:** Retrieves a specific feature flag by its key.  Returns the feature flag configuration including metadata such as creation and update timestamps.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feature_flag_by_key(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: Feature flag key identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetFeatureFlagByKeyApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_feature_flag_by_key_with_http_info(key, **kwargs)  # noqa: E501

    def get_feature_flag_by_key_with_http_info(self, key, **kwargs):  # noqa: E501
        """Get feature flag by key  # noqa: E501

        **🔒 INTERNAL:** Retrieves a specific feature flag by its key.  Returns the feature flag configuration including metadata such as creation and update timestamps.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feature_flag_by_key_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: Feature flag key identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetFeatureFlagByKeyApiResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_flag_by_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `get_feature_flag_by_key`")  # noqa: E501

        if self.api_client.client_side_validation and ('key' in local_var_params and  # noqa: E501
                                                        len(local_var_params['key']) > 128):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `key` when calling `get_feature_flag_by_key`, length must be less than or equal to `128`")  # noqa: E501
        if self.api_client.client_side_validation and 'key' in local_var_params and not re.search(r'^[a-zA-Z0-9._-]+$', local_var_params['key']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `key` when calling `get_feature_flag_by_key`, must conform to the pattern `/^[a-zA-Z0-9._-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/controlpanel/api/feature-flags/{key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFeatureFlagByKeyApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_feature_flag(self, key, com_patagona_pricemonitor_share_api_put_feature_flag_request, **kwargs):  # noqa: E501
        """Update feature flag  # noqa: E501

        **🔒 INTERNAL:** Updates an existing feature flag's name and description.  The feature flag key cannot be changed after creation. Only the display name and description can be updated.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_feature_flag(key, com_patagona_pricemonitor_share_api_put_feature_flag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: Feature flag key identifier (required)
        :param ComPatagonaPricemonitorShareApiPutFeatureFlagRequest com_patagona_pricemonitor_share_api_put_feature_flag_request: The feature flag updates to be applied (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UpdateFeatureFlagApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_feature_flag_with_http_info(key, com_patagona_pricemonitor_share_api_put_feature_flag_request, **kwargs)  # noqa: E501

    def update_feature_flag_with_http_info(self, key, com_patagona_pricemonitor_share_api_put_feature_flag_request, **kwargs):  # noqa: E501
        """Update feature flag  # noqa: E501

        **🔒 INTERNAL:** Updates an existing feature flag's name and description.  The feature flag key cannot be changed after creation. Only the display name and description can be updated.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_feature_flag_with_http_info(key, com_patagona_pricemonitor_share_api_put_feature_flag_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key: Feature flag key identifier (required)
        :param ComPatagonaPricemonitorShareApiPutFeatureFlagRequest com_patagona_pricemonitor_share_api_put_feature_flag_request: The feature flag updates to be applied (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UpdateFeatureFlagApiResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key',
            'com_patagona_pricemonitor_share_api_put_feature_flag_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_feature_flag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in local_var_params or  # noqa: E501
                                                        local_var_params['key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key` when calling `update_feature_flag`")  # noqa: E501
        # verify the required parameter 'com_patagona_pricemonitor_share_api_put_feature_flag_request' is set
        if self.api_client.client_side_validation and ('com_patagona_pricemonitor_share_api_put_feature_flag_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['com_patagona_pricemonitor_share_api_put_feature_flag_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `com_patagona_pricemonitor_share_api_put_feature_flag_request` when calling `update_feature_flag`")  # noqa: E501

        if self.api_client.client_side_validation and ('key' in local_var_params and  # noqa: E501
                                                        len(local_var_params['key']) > 128):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `key` when calling `update_feature_flag`, length must be less than or equal to `128`")  # noqa: E501
        if self.api_client.client_side_validation and 'key' in local_var_params and not re.search(r'^[a-zA-Z0-9._-]+$', local_var_params['key']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `key` when calling `update_feature_flag`, must conform to the pattern `/^[a-zA-Z0-9._-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'com_patagona_pricemonitor_share_api_put_feature_flag_request' in local_var_params:
            body_params = local_var_params['com_patagona_pricemonitor_share_api_put_feature_flag_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/controlpanel/api/feature-flags/{key}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateFeatureFlagApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
