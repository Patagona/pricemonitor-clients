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
from pricemonitor_api_client.models.api_contract import ApiContract  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestApiContract(unittest.TestCase):
    """ApiContract unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiContract
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.api_contract.ApiContract()  # noqa: E501
        if include_optional :
            return ApiContract(
                active = True, 
                company_name = '0', 
                contract_id = '0', 
                contract_name = '0', 
                contract_type = '0', 
                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return ApiContract(
        )

    def testApiContract(self):
        """Test ApiContract"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()