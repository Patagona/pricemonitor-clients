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
from pricemonitor_api_client.models.get_price_recommendations_response import GetPriceRecommendationsResponse  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestGetPriceRecommendationsResponse(unittest.TestCase):
    """GetPriceRecommendationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetPriceRecommendationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.get_price_recommendations_response.GetPriceRecommendationsResponse()  # noqa: E501
        if include_optional :
            return GetPriceRecommendationsResponse(
                next = '0', 
                price_recommendations = [
                    {"identifier":"identifier","gtin":6,"recommendedPrice":1.4658129805029452,"currentPrice":0.8008281904610115,"currency":"currency"}
                    ]
            )
        else :
            return GetPriceRecommendationsResponse(
        )

    def testGetPriceRecommendationsResponse(self):
        """Test GetPriceRecommendationsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()