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
from pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_api_price_recommendation import ComPatagonaPricemonitorShareApiApiPriceRecommendation  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestComPatagonaPricemonitorShareApiApiPriceRecommendation(unittest.TestCase):
    """ComPatagonaPricemonitorShareApiApiPriceRecommendation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComPatagonaPricemonitorShareApiApiPriceRecommendation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_api_price_recommendation.ComPatagonaPricemonitorShareApiApiPriceRecommendation()  # noqa: E501
        if include_optional :
            return ComPatagonaPricemonitorShareApiApiPriceRecommendation(
                old_price = 1.337, 
                delivery_costs = 1.337, 
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                old_delivery_costs = 1.337, 
                tags = [
                    {"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}
                    ], 
                price = 1.337, 
                old_position = 56, 
                gtin = 1.337, 
                relative_price_change_percentage = 1.337, 
                new_position = 56, 
                customer_product_id = '0', 
                original_max_price_boundary = 1.337, 
                relevant_domain = '0', 
                original_min_price_boundary = 1.337, 
                currency = '0', 
                product_id = '0', 
                original_tags = [
                    {"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}
                    ]
            )
        else :
            return ComPatagonaPricemonitorShareApiApiPriceRecommendation(
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tags = [
                    {"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}
                    ],
                price = 1.337,
                original_max_price_boundary = 1.337,
                original_min_price_boundary = 1.337,
                currency = '0',
                product_id = '0',
                original_tags = [
                    {"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}
                    ],
        )

    def testComPatagonaPricemonitorShareApiApiPriceRecommendation(self):
        """Test ComPatagonaPricemonitorShareApiApiPriceRecommendation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()