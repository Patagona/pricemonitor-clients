# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.6088
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pricemonitor_api_client
from pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_embed_sso_url_response_v3 import ComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3(unittest.TestCase):
    """ComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.com_patagona_pricemonitor_share_api_embed_sso_url_response_v3.ComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3()  # noqa: E501
        if include_optional :
            return ComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3(
                url = '0'
            )
        else :
            return ComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3(
                url = '0',
        )

    def testComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3(self):
        """Test ComPatagonaPricemonitorShareApiEmbedSSOUrlResponseV3"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()