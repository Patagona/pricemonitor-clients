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
from pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_get_contract_settings_response_v1 import ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestComPatagonaPricemonitorShareApiGetContractSettingsResponseV1(unittest.TestCase):
    """ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_get_contract_settings_response_v1.ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1()  # noqa: E501
        if include_optional :
            return ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1(
                name = '0', 
                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                portals = [
                    '0'
                    ], 
                include_delivery_costs = True, 
                features = {"disabled":["disabled","disabled"],"enabled":["enabled","enabled"]}, 
                image_tag = '0', 
                company = '0', 
                id = 1.337, 
                monitoring_priority = 56, 
                currency = '0', 
                type = '0', 
                sid = '0', 
                msrp_tag = '0', 
                map_tag = '0', 
                active = True
            )
        else :
            return ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1(
                name = '0',
                portals = [
                    '0'
                    ],
                include_delivery_costs = True,
                features = {"disabled":["disabled","disabled"],"enabled":["enabled","enabled"]},
                company = '0',
                id = 1.337,
                monitoring_priority = 56,
                currency = '0',
                type = '0',
                sid = '0',
                active = True,
        )

    def testComPatagonaPricemonitorShareApiGetContractSettingsResponseV1(self):
        """Test ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()