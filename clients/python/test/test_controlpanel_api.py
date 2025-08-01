# coding: utf-8

"""
    Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.7216
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pricemonitor_api_client
from pricemonitor_api_client.api.controlpanel_api import ControlpanelApi  # noqa: E501
from pricemonitor_api_client.rest import ApiException


class TestControlpanelApi(unittest.TestCase):
    """ControlpanelApi unit test stubs"""

    def setUp(self):
        self.api = pricemonitor_api_client.api.controlpanel_api.ControlpanelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_company(self):
        """Test case for add_company

        Add company  # noqa: E501
        """
        pass

    def test_add_company_user(self):
        """Test case for add_company_user

        Add user to company  # noqa: E501
        """
        pass

    def test_add_user(self):
        """Test case for add_user

        Add a new user  # noqa: E501
        """
        pass

    def test_create_auth_token(self):
        """Test case for create_auth_token

        Create authentication token  # noqa: E501
        """
        pass

    def test_create_feature_flag(self):
        """Test case for create_feature_flag

        Create feature flag  # noqa: E501
        """
        pass

    def test_delete_auth_token(self):
        """Test case for delete_auth_token

        Delete authentication token  # noqa: E501
        """
        pass

    def test_delete_feature_flag(self):
        """Test case for delete_feature_flag

        Delete feature flag  # noqa: E501
        """
        pass

    def test_get_all_companies(self):
        """Test case for get_all_companies

        Get a list of all companies  # noqa: E501
        """
        pass

    def test_get_all_contracts(self):
        """Test case for get_all_contracts

        Get a list of all contracts  # noqa: E501
        """
        pass

    def test_get_all_feature_flags(self):
        """Test case for get_all_feature_flags

        Get all feature flags  # noqa: E501
        """
        pass

    def test_get_all_portals(self):
        """Test case for get_all_portals

        Get a list of all portals  # noqa: E501
        """
        pass

    def test_get_all_tasks(self):
        """Test case for get_all_tasks

        Get all tasks  # noqa: E501
        """
        pass

    def test_get_all_users(self):
        """Test case for get_all_users

        Get a list of all users  # noqa: E501
        """
        pass

    def test_get_feature_flag_by_key(self):
        """Test case for get_feature_flag_by_key

        Get feature flag by key  # noqa: E501
        """
        pass

    def test_get_tasks_stats(self):
        """Test case for get_tasks_stats

        Get all task stats  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user  # noqa: E501
        """
        pass

    def test_list_vendors(self):
        """Test case for list_vendors

        Get list of vendors  # noqa: E501
        """
        pass

    def test_post_admin_add_domain_v3(self):
        """Test case for post_admin_add_domain_v3

        Add domain  # noqa: E501
        """
        pass

    def test_put_admin_domain_control_panel_v3(self):
        """Test case for put_admin_domain_control_panel_v3

        Update or add domain  # noqa: E501
        """
        pass

    def test_update_auth_token(self):
        """Test case for update_auth_token

        Update authentication token  # noqa: E501
        """
        pass

    def test_update_feature_flag(self):
        """Test case for update_feature_flag

        Update feature flag  # noqa: E501
        """
        pass

    def test_vendor_data(self):
        """Test case for vendor_data

        Get vendor export data  # noqa: E501
        """
        pass

    def test_version(self):
        """Test case for version

        Get application version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
