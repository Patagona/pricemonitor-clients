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
from pricemonitor_api_client.models.product_and_offers2 import ProductAndOffers2  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestProductAndOffers2(unittest.TestCase):
    """ProductAndOffers2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductAndOffers2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.product_and_offers2.ProductAndOffers2()  # noqa: E501
        if include_optional :
            return ProductAndOffers2(
                offers = [
                    {"ignored":true,"gtin":6,"productId":"productId","retrievalDate":"2000-01-23T04:56:07.000+00:00","availability":true,"creationDate":"2000-01-23T04:56:07.000+00:00","vendorName":"vendorName","positionByTotalPrice":2,"productName":"productName","url":"url","minDeliveryTime":5,"vendorDomainId":"vendorDomainId","deliveryCosts":0.8008281904610115,"maxDeliveryTime":1,"price":7.061401241503109,"domain":"domain","contractId":"contractId","attributes":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"currency":"currency","positionByUnitPrice":5}
                    ], 
                product = {"customerProductId":"customerProductId","gtin":9,"referencePrice":4.145608029883936,"maxPriceBoundary":3.616076749251911,"name":"name","id":"id","minPriceBoundary":2.027123023002322,"tags":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
            )
        else :
            return ProductAndOffers2(
        )

    def testProductAndOffers2(self):
        """Test ProductAndOffers2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()