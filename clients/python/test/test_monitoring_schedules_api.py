# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.5838
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pricemonitor_api_client
from pricemonitor_api_client.api.monitoring_schedules_api import MonitoringSchedulesApi  # noqa: E501
from pricemonitor_api_client.rest import ApiException


class TestMonitoringSchedulesApi(unittest.TestCase):
    """MonitoringSchedulesApi unit test stubs"""

    def setUp(self):
        self.api = pricemonitor_api_client.api.monitoring_schedules_api.MonitoringSchedulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_monitoring_schedule_manufacturer_v3(self):
        """Test case for delete_monitoring_schedule_manufacturer_v3

        Delete a monitoring schedule for a given contract.  # noqa: E501
        """
        pass

    def test_delete_monitoring_schedule_vendor_v3(self):
        """Test case for delete_monitoring_schedule_vendor_v3

        Delete a monitoring schedule for a given contract.  # noqa: E501
        """
        pass

    def test_execute_monitoring_schedule_manufacturer_v3(self):
        """Test case for execute_monitoring_schedule_manufacturer_v3

        Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule  # noqa: E501
        """
        pass

    def test_execute_monitoring_schedule_vendor_v3(self):
        """Test case for execute_monitoring_schedule_vendor_v3

        Trigger a monitoring pipeline task for vendor for configured monitoring schedule  # noqa: E501
        """
        pass

    def test_get_monitoring_schedules_manufacturer_v3(self):
        """Test case for get_monitoring_schedules_manufacturer_v3

        Get all the monitoring schedules for a specified contract.  # noqa: E501
        """
        pass

    def test_get_monitoring_schedules_vendor_v3(self):
        """Test case for get_monitoring_schedules_vendor_v3

        Get all the monitoring schedules for a specified contract.  # noqa: E501
        """
        pass

    def test_post_monitoring_schedule_manufacturer_v3(self):
        """Test case for post_monitoring_schedule_manufacturer_v3

        Add a monitoring schedule for a given contract.  # noqa: E501
        """
        pass

    def test_post_monitoring_schedule_vendor_v3(self):
        """Test case for post_monitoring_schedule_vendor_v3

        Add a monitoring schedule for a given contract.  # noqa: E501
        """
        pass

    def test_put_monitoring_schedule_manufacturer_v3(self):
        """Test case for put_monitoring_schedule_manufacturer_v3

        Update a monitoring schedule for a given contract.  # noqa: E501
        """
        pass

    def test_put_monitoring_schedule_vendor_v3(self):
        """Test case for put_monitoring_schedule_vendor_v3

        Update a monitoring schedule for a given contract.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()