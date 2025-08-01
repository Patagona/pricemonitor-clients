# coding: utf-8

"""
    Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.7216
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pricemonitor_api_client
from pricemonitor_api_client.models.post_orders_bulk_api_response import PostOrdersBulkApiResponse  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestPostOrdersBulkApiResponse(unittest.TestCase):
    """PostOrdersBulkApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostOrdersBulkApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.post_orders_bulk_api_response.PostOrdersBulkApiResponse()  # noqa: E501
        if include_optional :
            return PostOrdersBulkApiResponse(
                data = [
                    pricemonitor_api_client.models.post_orders_bulk_api_response_data_1.PostOrdersBulkApiResponse_data_1(
                        data = pricemonitor_api_client.models.post_orders_bulk_api_response_data.PostOrdersBulkApiResponse_data(
                            orders = [
                                pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/customer_order_v2.com.patagona.pricemonitor.share.api.CustomerOrderV2(
                                    shipping_costs = 1.337, 
                                    order_id = '0', 
                                    items = [
                                        pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/customer_order_item_v2.com.patagona.pricemonitor.share.api.CustomerOrderItemV2(
                                            item_id = '0', 
                                            unit_price = 1.337, 
                                            quantity = 56, 
                                            tax_percentage = 1.337, )
                                        ], 
                                    total_price = 1.337, 
                                    product_mappings = [
                                        pricemonitor_api_client.models.com/patagona/pricemonitor/share/api/customer_order_product_mapping_v2.com.patagona.pricemonitor.share.api.CustomerOrderProductMappingV2(
                                            source = '0', 
                                            target = '0', )
                                        ], 
                                    origin = '0', 
                                    creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    currency = '0', 
                                    referrer = '0', )
                                ], 
                            version = '0', ), 
                        errors = [
                            pricemonitor_api_client.models.api_error.ApiError(
                                code = 'request.invalid', 
                                message = 'The provided email address is not in a valid format', )
                            ], )
                    ]
            )
        else :
            return PostOrdersBulkApiResponse(
        )

    def testPostOrdersBulkApiResponse(self):
        """Test PostOrdersBulkApiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
