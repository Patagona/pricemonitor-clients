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
from pricemonitor_api_client.models.query_products_by_filter_vendor_v3_api_response import QueryProductsByFilterVendorV3ApiResponse  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestQueryProductsByFilterVendorV3ApiResponse(unittest.TestCase):
    """QueryProductsByFilterVendorV3ApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QueryProductsByFilterVendorV3ApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.query_products_by_filter_vendor_v3_api_response.QueryProductsByFilterVendorV3ApiResponse()  # noqa: E501
        if include_optional :
            return QueryProductsByFilterVendorV3ApiResponse(
                data = [
                    {"customerProductId":"customerProductId","gtin":6.027456183070403,"referencePrice":5.962133916683182,"maxPriceBoundary":1.4658129805029452,"name":"name","id":"id","minPriceBoundary":0.8008281904610115,"tags":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
                    ]
            )
        else :
            return QueryProductsByFilterVendorV3ApiResponse(
                data = [
                    {"customerProductId":"customerProductId","gtin":6.027456183070403,"referencePrice":5.962133916683182,"maxPriceBoundary":1.4658129805029452,"name":"name","id":"id","minPriceBoundary":0.8008281904610115,"tags":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
                    ],
        )

    def testQueryProductsByFilterVendorV3ApiResponse(self):
        """Test QueryProductsByFilterVendorV3ApiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()