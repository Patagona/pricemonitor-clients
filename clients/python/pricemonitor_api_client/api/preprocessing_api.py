# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.5935
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


class PreprocessingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def publish_preprocessing_task_vendor_v3(self, retrospective_in_minutes, contract_id, **kwargs):  # noqa: E501
        """Publish a preprocessing task for vendor.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_preprocessing_task_vendor_v3(retrospective_in_minutes, contract_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int retrospective_in_minutes: The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10800 (required)
        :param str contract_id: ID of the contract (required)
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
        return self.publish_preprocessing_task_vendor_v3_with_http_info(retrospective_in_minutes, contract_id, **kwargs)  # noqa: E501

    def publish_preprocessing_task_vendor_v3_with_http_info(self, retrospective_in_minutes, contract_id, **kwargs):  # noqa: E501
        """Publish a preprocessing task for vendor.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_preprocessing_task_vendor_v3_with_http_info(retrospective_in_minutes, contract_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int retrospective_in_minutes: The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10800 (required)
        :param str contract_id: ID of the contract (required)
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
            'retrospective_in_minutes',
            'contract_id'
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
                    " to method publish_preprocessing_task_vendor_v3" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'retrospective_in_minutes' is set
        if self.api_client.client_side_validation and ('retrospective_in_minutes' not in local_var_params or  # noqa: E501
                                                        local_var_params['retrospective_in_minutes'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `retrospective_in_minutes` when calling `publish_preprocessing_task_vendor_v3`")  # noqa: E501
        # verify the required parameter 'contract_id' is set
        if self.api_client.client_side_validation and ('contract_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['contract_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `contract_id` when calling `publish_preprocessing_task_vendor_v3`")  # noqa: E501

        if self.api_client.client_side_validation and 'retrospective_in_minutes' in local_var_params and local_var_params['retrospective_in_minutes'] > 10800:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `retrospective_in_minutes` when calling `publish_preprocessing_task_vendor_v3`, must be a value less than or equal to `10800`")  # noqa: E501
        if self.api_client.client_side_validation and 'retrospective_in_minutes' in local_var_params and local_var_params['retrospective_in_minutes'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `retrospective_in_minutes` when calling `publish_preprocessing_task_vendor_v3`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'retrospective_in_minutes' in local_var_params:
            path_params['retrospectiveInMinutes'] = local_var_params['retrospective_in_minutes']  # noqa: E501
        if 'contract_id' in local_var_params:
            path_params['contractId'] = local_var_params['contract_id']  # noqa: E501

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
            '/api/v3/vendor/contracts/{contractId}/tasks/preprocessing', 'POST',
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