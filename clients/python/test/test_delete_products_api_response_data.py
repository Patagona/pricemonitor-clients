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
from pricemonitor_api_client.models.delete_products_api_response_data import DeleteProductsApiResponseData  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestDeleteProductsApiResponseData(unittest.TestCase):
    """DeleteProductsApiResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeleteProductsApiResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.delete_products_api_response_data.DeleteProductsApiResponseData()  # noqa: E501
        if include_optional :
            return DeleteProductsApiResponseData(
                deleted = 56
            )
        else :
            return DeleteProductsApiResponseData(
        )

    def testDeleteProductsApiResponseData(self):
        """Test DeleteProductsApiResponseData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()