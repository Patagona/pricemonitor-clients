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
from pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_price_approval_decision_v3 import ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestComPatagonaPricemonitorShareApiPriceApprovalDecisionV3(unittest.TestCase):
    """ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_price_approval_decision_v3.ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3()  # noqa: E501
        if include_optional :
            return ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3(
                user_email = '0', 
                decision = '0', 
                comment = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user_id = 56, 
                superseded = True, 
                overwrite_price = 1.337
            )
        else :
            return ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3(
                user_email = '0',
                decision = '0',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_id = 56,
                superseded = True,
        )

    def testComPatagonaPricemonitorShareApiPriceApprovalDecisionV3(self):
        """Test ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
