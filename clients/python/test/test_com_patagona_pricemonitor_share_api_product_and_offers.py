# coding: utf-8

"""
    Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.7039
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pricemonitor_api_client
from pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_product_and_offers import ComPatagonaPricemonitorShareApiProductAndOffers  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestComPatagonaPricemonitorShareApiProductAndOffers(unittest.TestCase):
    """ComPatagonaPricemonitorShareApiProductAndOffers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComPatagonaPricemonitorShareApiProductAndOffers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_product_and_offers.ComPatagonaPricemonitorShareApiProductAndOffers()  # noqa: E501
        if include_optional :
            return ComPatagonaPricemonitorShareApiProductAndOffers(
                product = pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/api_product.com.patagona.pricemonitor.share.api.ApiProduct(
                    name = '0', 
                    tags = [
                        pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/tag.com.patagona.pricemonitor.share.api.Tag(
                            key = '0', 
                            value = '0', )
                        ], 
                    min_price_boundary = 1.337, 
                    gtin = 1.337, 
                    customer_product_id = '0', 
                    id = '0', 
                    max_price_boundary = 1.337, 
                    reference_price = 1.337, ), 
                offers = [
                    pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/api_offer.com.patagona.pricemonitor.share.api.ApiOffer(
                        position_by_total_price = 56, 
                        delivery_costs = 1.337, 
                        max_delivery_time = 56, 
                        url = '0', 
                        vendor_domain_id = '0', 
                        domain = '0', 
                        price = 1.337, 
                        min_delivery_time = 56, 
                        gtin = 1.337, 
                        position_by_unit_price = 56, 
                        availability = True, 
                        attributes = [
                            pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/offer_attribute.com.patagona.pricemonitor.share.api.OfferAttribute(
                                name = '0', 
                                value = '0', )
                            ], 
                        vendor_name = '0', 
                        retrieval_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        product_name = '0', 
                        currency = '0', 
                        product_id = '0', 
                        ignored = True, )
                    ]
            )
        else :
            return ComPatagonaPricemonitorShareApiProductAndOffers(
                product = pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/api_product.com.patagona.pricemonitor.share.api.ApiProduct(
                    name = '0', 
                    tags = [
                        pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/tag.com.patagona.pricemonitor.share.api.Tag(
                            key = '0', 
                            value = '0', )
                        ], 
                    min_price_boundary = 1.337, 
                    gtin = 1.337, 
                    customer_product_id = '0', 
                    id = '0', 
                    max_price_boundary = 1.337, 
                    reference_price = 1.337, ),
                offers = [
                    pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/api_offer.com.patagona.pricemonitor.share.api.ApiOffer(
                        position_by_total_price = 56, 
                        delivery_costs = 1.337, 
                        max_delivery_time = 56, 
                        url = '0', 
                        vendor_domain_id = '0', 
                        domain = '0', 
                        price = 1.337, 
                        min_delivery_time = 56, 
                        gtin = 1.337, 
                        position_by_unit_price = 56, 
                        availability = True, 
                        attributes = [
                            pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/offer_attribute.com.patagona.pricemonitor.share.api.OfferAttribute(
                                name = '0', 
                                value = '0', )
                            ], 
                        vendor_name = '0', 
                        retrieval_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        product_name = '0', 
                        currency = '0', 
                        product_id = '0', 
                        ignored = True, )
                    ],
        )

    def testComPatagonaPricemonitorShareApiProductAndOffers(self):
        """Test ComPatagonaPricemonitorShareApiProductAndOffers"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()