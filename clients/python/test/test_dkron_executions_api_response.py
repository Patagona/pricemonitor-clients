# coding: utf-8

"""
    Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.6822
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pricemonitor_api_client
from pricemonitor_api_client.models.dkron_executions_api_response import DkronExecutionsApiResponse  # noqa: E501
from pricemonitor_api_client.rest import ApiException

class TestDkronExecutionsApiResponse(unittest.TestCase):
    """DkronExecutionsApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DkronExecutionsApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pricemonitor_api_client.models.dkron_executions_api_response.DkronExecutionsApiResponse()  # noqa: E501
        if include_optional :
            return DkronExecutionsApiResponse(
                data = [
                    pricemonitor_api_client.models.execution.Execution(
                        job_name = 'job_1', 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        success = True, 
                        output = 'Hello from Dkron', 
                        node_name = 'dkron1', )
                    ]
            )
        else :
            return DkronExecutionsApiResponse(
                data = [
                    pricemonitor_api_client.models.execution.Execution(
                        job_name = 'job_1', 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        success = True, 
                        output = 'Hello from Dkron', 
                        node_name = 'dkron1', )
                    ],
        )

    def testDkronExecutionsApiResponse(self):
        """Test DkronExecutionsApiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()