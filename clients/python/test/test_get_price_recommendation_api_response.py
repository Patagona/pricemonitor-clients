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
from pricemonitor_api_client.models.get_price_recommendation_api_response import GetPriceRecommendationApiResponse  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestGetPriceRecommendationApiResponse(unittest.TestCase):
    """GetPriceRecommendationApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetPriceRecommendationApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.get_price_recommendation_api_response.GetPriceRecommendationApiResponse()  # noqa: E501
        if include_optional :
            return GetPriceRecommendationApiResponse(
                data = [
                    {"relativePriceChangePercentage":3.616076749251911,"customerProductId":"customerProductId","gtin":9.301444243932576,"productId":"productId","originalTags":[{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"},{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}],"oldPrice":0.8008281904610115,"tags":[{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"},{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}],"originalMaxPriceBoundary":4.145608029883936,"newPosition":2,"originalMinPriceBoundary":7.386281948385884,"oldDeliveryCosts":1.4658129805029452,"deliveryCosts":6.027456183070403,"price":2.3021358869347655,"relevantDomain":"relevantDomain","currency":"currency","oldPosition":7,"timestamp":"2000-01-23T04:56:07.000+00:00"}
                    ], 
                meta = {"totalSize":1,"start":1,"limit":1,"nextUrl":"nextUrl"}
            )
        else :
            return GetPriceRecommendationApiResponse(
                data = [
                    {"relativePriceChangePercentage":3.616076749251911,"customerProductId":"customerProductId","gtin":9.301444243932576,"productId":"productId","originalTags":[{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"},{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}],"oldPrice":0.8008281904610115,"tags":[{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"},{"stringValue":"stringValue","integerValue":5,"booleanValue":true,"doubleValue":5.962133916683182,"label":"label"}],"originalMaxPriceBoundary":4.145608029883936,"newPosition":2,"originalMinPriceBoundary":7.386281948385884,"oldDeliveryCosts":1.4658129805029452,"deliveryCosts":6.027456183070403,"price":2.3021358869347655,"relevantDomain":"relevantDomain","currency":"currency","oldPosition":7,"timestamp":"2000-01-23T04:56:07.000+00:00"}
                    ],
        )

    def testGetPriceRecommendationApiResponse(self):
        """Test GetPriceRecommendationApiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()