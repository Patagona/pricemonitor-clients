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
from pricemonitor_api_client.models.query_products_request_v3 import QueryProductsRequestV3  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestQueryProductsRequestV3(unittest.TestCase):
    """QueryProductsRequestV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QueryProductsRequestV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.query_products_request_v3.QueryProductsRequestV3()  # noqa: E501
        if include_optional :
            return QueryProductsRequestV3(
                filter = {"comparison":"StringInSequence","left":"{}","right":"{}","type":"ComparisonFilter"}, 
                pagination = {"limit":0,"start":6}
            )
        else :
            return QueryProductsRequestV3(
                pagination = {"limit":0,"start":6},
        )

    def testQueryProductsRequestV3(self):
        """Test QueryProductsRequestV3"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()