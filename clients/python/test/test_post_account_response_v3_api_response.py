# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.5838
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pricemonitor_api_client
from pricemonitor_api_client.models.post_account_response_v3_api_response import PostAccountResponseV3ApiResponse  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestPostAccountResponseV3ApiResponse(unittest.TestCase):
    """PostAccountResponseV3ApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostAccountResponseV3ApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.post_account_response_v3_api_response.PostAccountResponseV3ApiResponse()  # noqa: E501
        if include_optional :
            return PostAccountResponseV3ApiResponse(
                data = {"name":"name","id":0.8008281904610115,"email":"email"}
            )
        else :
            return PostAccountResponseV3ApiResponse(
                data = {"name":"name","id":0.8008281904610115,"email":"email"},
        )

    def testPostAccountResponseV3ApiResponse(self):
        """Test PostAccountResponseV3ApiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()