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
from pricemonitor_api_client.api.internal_api import InternalApi  # noqa: E501
from pricemonitor_api_client.rest import ApiException


class TestInternalApi(unittest.TestCase):
    """InternalApi unit test stubs"""

    def setUp(self):
        self.api = pricemonitor_api_client.api.internal_api.InternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_company(self):
        """Test case for add_company

        """
        pass

    def test_add_company_user(self):
        """Test case for add_company_user

        """
        pass

    def test_add_user(self):
        """Test case for add_user

        Add a new user  # noqa: E501
        """
        pass

    def test_api_v3_manufacturer_contracts_contract_id_offers_shop_query_post(self):
        """Test case for api_v3_manufacturer_contracts_contract_id_offers_shop_query_post

        """
        pass

    def test_api_v3_manufacturer_contracts_contract_id_offers_stats_query_post(self):
        """Test case for api_v3_manufacturer_contracts_contract_id_offers_stats_query_post

        """
        pass

    def test_api_v3_vendor_contracts_contract_id_offers_shop_query_post(self):
        """Test case for api_v3_vendor_contracts_contract_id_offers_shop_query_post

        """
        pass

    def test_api_v3_vendor_contracts_contract_id_offers_stats_query_post(self):
        """Test case for api_v3_vendor_contracts_contract_id_offers_stats_query_post

        """
        pass

    def test_controlpanel_api_companies_get(self):
        """Test case for controlpanel_api_companies_get

        Get a list of all companies  # noqa: E501
        """
        pass

    def test_create_alert_settings(self):
        """Test case for create_alert_settings

        """
        pass

    def test_create_auth_token(self):
        """Test case for create_auth_token

        """
        pass

    def test_create_task(self):
        """Test case for create_task

        """
        pass

    def test_create_task_manufacturer_v2(self):
        """Test case for create_task_manufacturer_v2

        """
        pass

    def test_create_task_vendor_v2(self):
        """Test case for create_task_vendor_v2

        """
        pass

    def test_delete_alert_settings(self):
        """Test case for delete_alert_settings

        """
        pass

    def test_delete_auth_token(self):
        """Test case for delete_auth_token

        """
        pass

    def test_delete_callback_settings_manufacturer_v2(self):
        """Test case for delete_callback_settings_manufacturer_v2

        """
        pass

    def test_delete_callback_settings_vendor_v2(self):
        """Test case for delete_callback_settings_vendor_v2

        """
        pass

    def test_delete_contract_vendor_v2(self):
        """Test case for delete_contract_vendor_v2

        """
        pass

    def test_delete_dynamic_monitoring_settings(self):
        """Test case for delete_dynamic_monitoring_settings

        """
        pass

    def test_delete_feed_vendor_v2(self):
        """Test case for delete_feed_vendor_v2

        """
        pass

    def test_delete_import_settings_vendor_v2(self):
        """Test case for delete_import_settings_vendor_v2

        """
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

    def test_delete_products_manufacturer_v3(self):
        """Test case for delete_products_manufacturer_v3

        """
        pass

    def test_delete_repricing_strategy_vendor_v2(self):
        """Test case for delete_repricing_strategy_vendor_v2

        """
        pass

    def test_delete_user_role(self):
        """Test case for delete_user_role

        """
        pass

    def test_delete_vendor_shop_mapping_manufacturer_v3(self):
        """Test case for delete_vendor_shop_mapping_manufacturer_v3

        Delete a vendor and associated shops for a given contract.  # noqa: E501
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

    def test_get_active_ebay_token_vendor_v2(self):
        """Test case for get_active_ebay_token_vendor_v2

        """
        pass

    def test_get_alert_settings(self):
        """Test case for get_alert_settings

        """
        pass

    def test_get_all_contracts(self):
        """Test case for get_all_contracts

        Get a list of all contracts  # noqa: E501
        """
        pass

    def test_get_all_ebay_authorizations_vendor_v2(self):
        """Test case for get_all_ebay_authorizations_vendor_v2

        """
        pass

    def test_get_all_ebay_tokens_vendor_v2(self):
        """Test case for get_all_ebay_tokens_vendor_v2

        """
        pass

    def test_get_all_portals(self):
        """Test case for get_all_portals

        Get a list of all portals  # noqa: E501
        """
        pass

    def test_get_all_tasks(self):
        """Test case for get_all_tasks

        """
        pass

    def test_get_all_users(self):
        """Test case for get_all_users

        Get a list of all users  # noqa: E501
        """
        pass

    def test_get_callbacks_vendor_v2(self):
        """Test case for get_callbacks_vendor_v2

        """
        pass

    def test_get_cheapest_vendors_manufacturer_v2(self):
        """Test case for get_cheapest_vendors_manufacturer_v2

        """
        pass

    def test_get_company(self):
        """Test case for get_company

        """
        pass

    def test_get_complex_offer_filters_vendor_v2(self):
        """Test case for get_complex_offer_filters_vendor_v2

        Get all complex filters for the given contract.  # noqa: E501
        """
        pass

    def test_get_contracts_vendor_v2(self):
        """Test case for get_contracts_vendor_v2

        """
        pass

    def test_get_currency_vendor_v2(self):
        """Test case for get_currency_vendor_v2

        """
        pass

    def test_get_customer_contract_settings_manufaturer_v3(self):
        """Test case for get_customer_contract_settings_manufaturer_v3

        """
        pass

    def test_get_customer_contract_settings_vendor_v3(self):
        """Test case for get_customer_contract_settings_vendor_v3

        """
        pass

    def test_get_domains_vendor_v2(self):
        """Test case for get_domains_vendor_v2

        """
        pass

    def test_get_dynamic_monitoring_settings(self):
        """Test case for get_dynamic_monitoring_settings

        """
        pass

    def test_get_ebay_authorizations_vendor_v2(self):
        """Test case for get_ebay_authorizations_vendor_v2

        """
        pass

    def test_get_extended_tags_manufacturer_v3(self):
        """Test case for get_extended_tags_manufacturer_v3

        """
        pass

    def test_get_feed_export_delta_vendor_v2(self):
        """Test case for get_feed_export_delta_vendor_v2

        """
        pass

    def test_get_feed_export_vendor_v2(self):
        """Test case for get_feed_export_vendor_v2

        """
        pass

    def test_get_import_settings_vendor_v2(self):
        """Test case for get_import_settings_vendor_v2

        """
        pass

    def test_get_manufacturer_manufacturer_v2(self):
        """Test case for get_manufacturer_manufacturer_v2

        """
        pass

    def test_get_manufacturer_v3(self):
        """Test case for get_manufacturer_v3

        Get the contract information  # noqa: E501
        """
        pass

    def test_get_mappings_vendor_v2(self):
        """Test case for get_mappings_vendor_v2

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

    def test_get_monitoring_settings_manufacturer_v2(self):
        """Test case for get_monitoring_settings_manufacturer_v2

        """
        pass

    def test_get_monitoring_settings_manufacturer_v3(self):
        """Test case for get_monitoring_settings_manufacturer_v3

        """
        pass

    def test_get_monitoring_settings_vendor_v2(self):
        """Test case for get_monitoring_settings_vendor_v2

        """
        pass

    def test_get_monitoring_settings_vendor_v3(self):
        """Test case for get_monitoring_settings_vendor_v3

        """
        pass

    def test_get_offer_filters_vendor_v2(self):
        """Test case for get_offer_filters_vendor_v2

        Get all the vendor filters for the given contract.  # noqa: E501
        """
        pass

    def test_get_offer_retention_settings_manufacturer_v3(self):
        """Test case for get_offer_retention_settings_manufacturer_v3

        """
        pass

    def test_get_offer_retention_settings_vendor_v3(self):
        """Test case for get_offer_retention_settings_vendor_v3

        """
        pass

    def test_get_offer_statistics_manufacturer_v3(self):
        """Test case for get_offer_statistics_manufacturer_v3

        Get offer statistics per product of a contract. Only the latest offers per product and domain the are taken into account.  # noqa: E501
        """
        pass

    def test_get_orders_count_by_portal_by_contract(self):
        """Test case for get_orders_count_by_portal_by_contract

        """
        pass

    def test_get_orders_vendor_v3(self):
        """Test case for get_orders_vendor_v3

        """
        pass

    def test_get_price_cutters_manufacturer_v2(self):
        """Test case for get_price_cutters_manufacturer_v2

        """
        pass

    def test_get_price_cutters_vendor_v2(self):
        """Test case for get_price_cutters_vendor_v2

        """
        pass

    def test_get_price_recommendation_stats_vendor_v2(self):
        """Test case for get_price_recommendation_stats_vendor_v2

        """
        pass

    def test_get_product_filters_by_id_vendor_v2(self):
        """Test case for get_product_filters_by_id_vendor_v2

        """
        pass

    def test_get_product_filters_by_range_vendor_v2(self):
        """Test case for get_product_filters_by_range_vendor_v2

        Get all the filters product-wise for the given contract.  # noqa: E501
        """
        pass

    def test_get_product_filters_vendor_v2(self):
        """Test case for get_product_filters_vendor_v2

        Get all the filters of a given product for the given contract.  # noqa: E501
        """
        pass

    def test_get_product_metrics_by_contract(self):
        """Test case for get_product_metrics_by_contract

        """
        pass

    def test_get_product_monitoring_status_stats_vendor_v3(self):
        """Test case for get_product_monitoring_status_stats_vendor_v3

        """
        pass

    def test_get_product_price_violations_manufacturer_v2(self):
        """Test case for get_product_price_violations_manufacturer_v2

        """
        pass

    def test_get_product_price_violations_vendor_v2(self):
        """Test case for get_product_price_violations_vendor_v2

        """
        pass

    def test_get_repricing_strategy_vendor_v2(self):
        """Test case for get_repricing_strategy_vendor_v2

        """
        pass

    def test_get_settings(self):
        """Test case for get_settings

        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        """
        pass

    def test_get_tag_values_manufacturer_v2(self):
        """Test case for get_tag_values_manufacturer_v2

        """
        pass

    def test_get_tag_values_vendor_v2(self):
        """Test case for get_tag_values_vendor_v2

        """
        pass

    def test_get_tags_manufacturer_v2(self):
        """Test case for get_tags_manufacturer_v2

        """
        pass

    def test_get_tags_vendor_v2(self):
        """Test case for get_tags_vendor_v2

        """
        pass

    def test_get_task(self):
        """Test case for get_task

        """
        pass

    def test_get_task_data_manufacturer_v2(self):
        """Test case for get_task_data_manufacturer_v2

        """
        pass

    def test_get_task_data_vendor_v2(self):
        """Test case for get_task_data_vendor_v2

        """
        pass

    def test_get_task_manufacturer_v2(self):
        """Test case for get_task_manufacturer_v2

        """
        pass

    def test_get_task_state(self):
        """Test case for get_task_state

        """
        pass

    def test_get_tasks(self):
        """Test case for get_tasks

        """
        pass

    def test_get_tasks_manufacturer_v2(self):
        """Test case for get_tasks_manufacturer_v2

        """
        pass

    def test_get_tasks_stats(self):
        """Test case for get_tasks_stats

        """
        pass

    def test_get_time_stamps(self):
        """Test case for get_time_stamps

        """
        pass

    def test_get_user(self):
        """Test case for get_user

        """
        pass

    def test_get_users(self):
        """Test case for get_users

        """
        pass

    def test_get_vendor_settings_v2_vendor_v2(self):
        """Test case for get_vendor_settings_v2_vendor_v2

        """
        pass

    def test_get_vendor_shop_mapping_manufacturer_v3(self):
        """Test case for get_vendor_shop_mapping_manufacturer_v3

        Get vendor along with their associated shop for given vendor id and contract.  # noqa: E501
        """
        pass

    def test_get_vendor_shop_mappings_manufacturer_v3(self):
        """Test case for get_vendor_shop_mappings_manufacturer_v3

        Get all the vendors along with their associated shops for a specified contract.  # noqa: E501
        """
        pass

    def test_get_vendor_v3(self):
        """Test case for get_vendor_v3

        """
        pass

    def test_get_vendor_vendor_v2(self):
        """Test case for get_vendor_vendor_v2

        """
        pass

    def test_get_vendors_by_domain_manufacturer_v2(self):
        """Test case for get_vendors_by_domain_manufacturer_v2

        """
        pass

    def test_list_vendors(self):
        """Test case for list_vendors

        """
        pass

    def test_login_by_auth_token(self):
        """Test case for login_by_auth_token

        """
        pass

    def test_monitoring_pipeline_post_request_manufacturer_v3(self):
        """Test case for monitoring_pipeline_post_request_manufacturer_v3

        """
        pass

    def test_monitoring_pipeline_post_request_vendor_v3(self):
        """Test case for monitoring_pipeline_post_request_vendor_v3

        """
        pass

    def test_monitoring_pipeline_upsert_search_attempts_manufacturer_v3(self):
        """Test case for monitoring_pipeline_upsert_search_attempts_manufacturer_v3

        """
        pass

    def test_monitoring_pipeline_upsert_search_attempts_vendor_v3(self):
        """Test case for monitoring_pipeline_upsert_search_attempts_vendor_v3

        """
        pass

    def test_patch_product_manufacturer_v3(self):
        """Test case for patch_product_manufacturer_v3

        """
        pass

    def test_patch_product_vendor_v3(self):
        """Test case for patch_product_vendor_v3

        """
        pass

    def test_position_distribution(self):
        """Test case for position_distribution

        """
        pass

    def test_post_ebay_authorization_vendor_v2(self):
        """Test case for post_ebay_authorization_vendor_v2

        """
        pass

    def test_post_feed_vendor_v2(self):
        """Test case for post_feed_vendor_v2

        """
        pass

    def test_post_mappings_vendor_v2(self):
        """Test case for post_mappings_vendor_v2

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

    def test_post_offers_in_a_bulk_vendor_v2(self):
        """Test case for post_offers_in_a_bulk_vendor_v2

        """
        pass

    def test_post_offers_vendor_v2(self):
        """Test case for post_offers_vendor_v2

        """
        pass

    def test_post_vendor_shop_mapping_manufacturer_v3(self):
        """Test case for post_vendor_shop_mapping_manufacturer_v3

        Add a new vendor for a given contract and associate shops with the given vendor.  # noqa: E501
        """
        pass

    def test_prices_by_day_by_product_id_manufacturer_v2(self):
        """Test case for prices_by_day_by_product_id_manufacturer_v2

        """
        pass

    def test_put_callbacks_vendor_v2(self):
        """Test case for put_callbacks_vendor_v2

        """
        pass

    def test_put_complex_offer_filters_vendor_v2(self):
        """Test case for put_complex_offer_filters_vendor_v2

        Add the complex filters for the given contract.  # noqa: E501
        """
        pass

    def test_put_currency_vendor_v2(self):
        """Test case for put_currency_vendor_v2

        """
        pass

    def test_put_customer_contract_settings_manufacturer_v3(self):
        """Test case for put_customer_contract_settings_manufacturer_v3

        """
        pass

    def test_put_customer_contract_settings_vendor_v3(self):
        """Test case for put_customer_contract_settings_vendor_v3

        """
        pass

    def test_put_dynamic_monitoring_settings(self):
        """Test case for put_dynamic_monitoring_settings

        """
        pass

    def test_put_feed_vendor_v2(self):
        """Test case for put_feed_vendor_v2

        """
        pass

    def test_put_image_tag_manufacturer_v2(self):
        """Test case for put_image_tag_manufacturer_v2

        """
        pass

    def test_put_image_tag_vendor_v2(self):
        """Test case for put_image_tag_vendor_v2

        """
        pass

    def test_put_import_settings_vendor_v2(self):
        """Test case for put_import_settings_vendor_v2

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

    def test_put_monitoring_settings_manufacturer_v2(self):
        """Test case for put_monitoring_settings_manufacturer_v2

        """
        pass

    def test_put_monitoring_settings_manufacturer_v3(self):
        """Test case for put_monitoring_settings_manufacturer_v3

        """
        pass

    def test_put_monitoring_settings_vendor_v2(self):
        """Test case for put_monitoring_settings_vendor_v2

        """
        pass

    def test_put_monitoring_settings_vendor_v3(self):
        """Test case for put_monitoring_settings_vendor_v3

        """
        pass

    def test_put_offer_filters_vendor_v2(self):
        """Test case for put_offer_filters_vendor_v2

        Store the vendor filters for the given contract.  # noqa: E501
        """
        pass

    def test_put_offer_retention_settings_manufacturer_v3(self):
        """Test case for put_offer_retention_settings_manufacturer_v3

        """
        pass

    def test_put_offer_retention_settings_vendor_v3(self):
        """Test case for put_offer_retention_settings_vendor_v3

        """
        pass

    def test_put_product_filters_vendor_v2(self):
        """Test case for put_product_filters_vendor_v2

        Store the filters of a given product for the given contract.  # noqa: E501
        """
        pass

    def test_put_products_csv_manufacturer_v2(self):
        """Test case for put_products_csv_manufacturer_v2

        """
        pass

    def test_put_products_vendor_v2(self):
        """Test case for put_products_vendor_v2

        """
        pass

    def test_put_repricing_strategy_vendor_v2(self):
        """Test case for put_repricing_strategy_vendor_v2

        """
        pass

    def test_put_settings(self):
        """Test case for put_settings

        """
        pass

    def test_put_vendor_settings_vendor_v2(self):
        """Test case for put_vendor_settings_vendor_v2

        """
        pass

    def test_put_vendor_shop_mapping_manufacturer_v3(self):
        """Test case for put_vendor_shop_mapping_manufacturer_v3

        Update an existing vendor for a given contract and associate shops with the given vendor.  # noqa: E501
        """
        pass

    def test_query_offers_manufacturer_v3(self):
        """Test case for query_offers_manufacturer_v3

        """
        pass

    def test_query_price_recommendations_vendor_v2(self):
        """Test case for query_price_recommendations_vendor_v2

        """
        pass

    def test_query_products_by_filter_manufacturer_v3(self):
        """Test case for query_products_by_filter_manufacturer_v3

        """
        pass

    def test_query_products_by_filter_vendor_v3(self):
        """Test case for query_products_by_filter_vendor_v3

        """
        pass

    def test_raw_offers(self):
        """Test case for raw_offers

        """
        pass

    def test_remove_user(self):
        """Test case for remove_user

        """
        pass

    def test_request_new_password(self):
        """Test case for request_new_password

        Request a new password  # noqa: E501
        """
        pass

    def test_reset_password(self):
        """Test case for reset_password

        Reset the password  # noqa: E501
        """
        pass

    def test_save_include_delivery_costs(self):
        """Test case for save_include_delivery_costs

        """
        pass

    def test_save_sales(self):
        """Test case for save_sales

        """
        pass

    def test_scheduler_delete_request_manufacturer_v3(self):
        """Test case for scheduler_delete_request_manufacturer_v3

        """
        pass

    def test_scheduler_delete_request_vendor_v3(self):
        """Test case for scheduler_delete_request_vendor_v3

        """
        pass

    def test_scheduler_get_request_manufacturer_v3(self):
        """Test case for scheduler_get_request_manufacturer_v3

        """
        pass

    def test_scheduler_get_request_vendor_v3(self):
        """Test case for scheduler_get_request_vendor_v3

        """
        pass

    def test_scheduler_post_request_manufacturer_v3(self):
        """Test case for scheduler_post_request_manufacturer_v3

        """
        pass

    def test_scheduler_post_request_vendor_v3(self):
        """Test case for scheduler_post_request_vendor_v3

        """
        pass

    def test_scheduler_put_request_manufacturer_v3(self):
        """Test case for scheduler_put_request_manufacturer_v3

        """
        pass

    def test_scheduler_put_request_vendor_v3(self):
        """Test case for scheduler_put_request_vendor_v3

        """
        pass

    def test_segment_offers_manufacturer_v2(self):
        """Test case for segment_offers_manufacturer_v2

        """
        pass

    def test_segment_offers_vendor_v2(self):
        """Test case for segment_offers_vendor_v2

        """
        pass

    def test_shop_integration_get_request(self):
        """Test case for shop_integration_get_request

        """
        pass

    def test_shop_integration_post_request(self):
        """Test case for shop_integration_post_request

        """
        pass

    def test_shop_integration_post_request_vendor_v2(self):
        """Test case for shop_integration_post_request_vendor_v2

        """
        pass

    def test_stats_manufacturer_v2(self):
        """Test case for stats_manufacturer_v2

        """
        pass

    def test_timestamps_manufacturer_v2(self):
        """Test case for timestamps_manufacturer_v2

        """
        pass

    def test_update_alert_settings(self):
        """Test case for update_alert_settings

        """
        pass

    def test_update_auth_token(self):
        """Test case for update_auth_token

        """
        pass

    def test_update_task_manufacturer_v2(self):
        """Test case for update_task_manufacturer_v2

        """
        pass

    def test_update_task_vendor_v2(self):
        """Test case for update_task_vendor_v2

        """
        pass

    def test_update_user_role(self):
        """Test case for update_user_role

        """
        pass

    def test_validate_offers_manufacturer_v2(self):
        """Test case for validate_offers_manufacturer_v2

        """
        pass

    def test_validate_offers_vendor_v2(self):
        """Test case for validate_offers_vendor_v2

        """
        pass

    def test_vendor_data(self):
        """Test case for vendor_data

        """
        pass

    def test_vendors_per_domain_manufacturer_v2(self):
        """Test case for vendors_per_domain_manufacturer_v2

        """
        pass

    def test_version(self):
        """Test case for version

        Get the current application version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()