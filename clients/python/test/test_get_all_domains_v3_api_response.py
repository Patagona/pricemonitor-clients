# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.6248
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pricemonitor_api_client
from pricemonitor_api_client.models.get_all_domains_v3_api_response import GetAllDomainsV3ApiResponse  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestGetAllDomainsV3ApiResponse(unittest.TestCase):
    """GetAllDomainsV3ApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetAllDomainsV3ApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.get_all_domains_v3_api_response.GetAllDomainsV3ApiResponse()  # noqa: E501
        if include_optional :
            return GetAllDomainsV3ApiResponse(
                data = {"domains":[{"domain":"domain","name":"name","domainId":0.8008281904610115,"offerSources":["offerSources","offerSources"]},{"domain":"domain","name":"name","domainId":0.8008281904610115,"offerSources":["offerSources","offerSources"]}]}
            )
        else :
            return GetAllDomainsV3ApiResponse(
                data = {"domains":[{"domain":"domain","name":"name","domainId":0.8008281904610115,"offerSources":["offerSources","offerSources"]},{"domain":"domain","name":"name","domainId":0.8008281904610115,"offerSources":["offerSources","offerSources"]}]},
        )

    def testGetAllDomainsV3ApiResponse(self):
        """Test GetAllDomainsV3ApiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()