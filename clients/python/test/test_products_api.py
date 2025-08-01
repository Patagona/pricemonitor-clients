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
from pricemonitor_api_client.api.products_api import ProductsApi  # noqa: E501
from pricemonitor_api_client.rest import ApiException


class TestProductsApi(unittest.TestCase):
    """ProductsApi unit test stubs"""

    def setUp(self):
        self.api = pricemonitor_api_client.api.products_api.ProductsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_products(self):
        """Test case for delete_products

        Delete products  # noqa: E501
        """
        pass

    def test_delete_products_manufacturer_v3(self):
        """Test case for delete_products_manufacturer_v3

        Delete products [manufacturer]  # noqa: E501
        """
        pass

    def test_get_amazon_buybox_product_stats_v3(self):
        """Test case for get_amazon_buybox_product_stats_v3

        Get Amazon Buy Box statistics for time range  # noqa: E501
        """
        pass

    def test_get_extended_tags(self):
        """Test case for get_extended_tags

        Return the extended tags for the given product  # noqa: E501
        """
        pass

    def test_get_extended_tags_manufacturer_v3(self):
        """Test case for get_extended_tags_manufacturer_v3

        Get extended tags [manufacturer]  # noqa: E501
        """
        pass

    def test_get_mappings_vendor_v2(self):
        """Test case for get_mappings_vendor_v2

        Get product mappings  # noqa: E501
        """
        pass

    def test_get_product_filters_vendor_v2(self):
        """Test case for get_product_filters_vendor_v2

        Get all the filters of a given product for the given contract.  # noqa: E501
        """
        pass

    def test_get_product_monitoring_status_stats_vendor_v3(self):
        """Test case for get_product_monitoring_status_stats_vendor_v3

        Get product monitoring status stats [vendor]  # noqa: E501
        """
        pass

    def test_get_product_monitoring_status_vendor_v3(self):
        """Test case for get_product_monitoring_status_vendor_v3

        Get monitoring status of queried products  # noqa: E501
        """
        pass

    def test_get_product_price_recommendation_history(self):
        """Test case for get_product_price_recommendation_history

        Get price recommendations for one product  # noqa: E501
        """
        pass

    def test_get_product_properties_v3(self):
        """Test case for get_product_properties_v3

        Get all product properties for a product  # noqa: E501
        """
        pass

    def test_get_product_property_keys_v3(self):
        """Test case for get_product_property_keys_v3

        Get all product properties keys  # noqa: E501
        """
        pass

    def test_get_products(self):
        """Test case for get_products

        Get all products for a contract  # noqa: E501
        """
        pass

    def test_get_tag_values_manufacturer_v2(self):
        """Test case for get_tag_values_manufacturer_v2

        Get product tag values [manufacturer]  # noqa: E501
        """
        pass

    def test_get_tag_values_vendor_v2(self):
        """Test case for get_tag_values_vendor_v2

        Get tag values for key  # noqa: E501
        """
        pass

    def test_get_tags_manufacturer_v2(self):
        """Test case for get_tags_manufacturer_v2

        Get product tags [manufacturer]  # noqa: E501
        """
        pass

    def test_get_tags_vendor_v2(self):
        """Test case for get_tags_vendor_v2

        Get product tags [vendor]  # noqa: E501
        """
        pass

    def test_monitoring_pipeline_upsert_search_attempts_manufacturer_v3(self):
        """Test case for monitoring_pipeline_upsert_search_attempts_manufacturer_v3

        Update monitoring pipeline search attempts [manufacturer]  # noqa: E501
        """
        pass

    def test_monitoring_pipeline_upsert_search_attempts_vendor_v3(self):
        """Test case for monitoring_pipeline_upsert_search_attempts_vendor_v3

        Update monitoring pipeline search attempts [vendor]  # noqa: E501
        """
        pass

    def test_patch_product_manufacturer_v3(self):
        """Test case for patch_product_manufacturer_v3

        Update product [manufacturer]  # noqa: E501
        """
        pass

    def test_patch_product_vendor_v3(self):
        """Test case for patch_product_vendor_v3

        Update product [vendor]  # noqa: E501
        """
        pass

    def test_post_mappings_vendor_v2(self):
        """Test case for post_mappings_vendor_v2

        Update product identifier mapping  # noqa: E501
        """
        pass

    def test_post_offer_statistics_vendor_query(self):
        """Test case for post_offer_statistics_vendor_query

        Get offer statistics per product  # noqa: E501
        """
        pass

    def test_post_products_import_vendor_v3(self):
        """Test case for post_products_import_vendor_v3

        Add products in bulk (JSON)  # noqa: E501
        """
        pass

    def test_put_csv_products(self):
        """Test case for put_csv_products

        Set products via CSV file (V2)  # noqa: E501
        """
        pass

    def test_put_csv_products_manufacturer_v3(self):
        """Test case for put_csv_products_manufacturer_v3

        Set products via CSV file (V3)  # noqa: E501
        """
        pass

    def test_put_product_filters_vendor_v2(self):
        """Test case for put_product_filters_vendor_v2

        Store the filters of a given product for the given contract.  # noqa: E501
        """
        pass

    def test_put_product_properties_v3(self):
        """Test case for put_product_properties_v3

        Manage product properties for a product  # noqa: E501
        """
        pass

    def test_put_products_csv_manufacturer_v2(self):
        """Test case for put_products_csv_manufacturer_v2

        Set products via CSV file [manufacturer]  # noqa: E501
        """
        pass

    def test_put_products_import_vendor_v3(self):
        """Test case for put_products_import_vendor_v3

        Add products in bulk (CSV)  # noqa: E501
        """
        pass

    def test_put_products_vendor_v2(self):
        """Test case for put_products_vendor_v2

        Update products in bulk (JSON)  # noqa: E501
        """
        pass

    def test_query_offers_price_dumping_stats_manufacturer_v3(self):
        """Test case for query_offers_price_dumping_stats_manufacturer_v3

        Query price dumping statistics  # noqa: E501
        """
        pass

    def test_query_offers_price_dumping_stats_vendor_v3(self):
        """Test case for query_offers_price_dumping_stats_vendor_v3

        Query price dumping statistics  # noqa: E501
        """
        pass

    def test_query_offers_shop_manufacturer_v3(self):
        """Test case for query_offers_shop_manufacturer_v3

        Get all offers [manufacturer]  # noqa: E501
        """
        pass

    def test_query_offers_shop_vendor_v3(self):
        """Test case for query_offers_shop_vendor_v3

        Get all offers [vendor]  # noqa: E501
        """
        pass

    def test_query_offers_stats_manufacturer_v3(self):
        """Test case for query_offers_stats_manufacturer_v3

        Query offer statistics per product  # noqa: E501
        """
        pass

    def test_query_products_by_filter_manufacturer_v3(self):
        """Test case for query_products_by_filter_manufacturer_v3

        Get products of a contract  # noqa: E501
        """
        pass

    def test_query_products_by_filter_vendor_v3(self):
        """Test case for query_products_by_filter_vendor_v3

        Query products of a contract  # noqa: E501
        """
        pass

    def test_query_products_manufacturer_v3(self):
        """Test case for query_products_manufacturer_v3

        Query products for manufacturer  # noqa: E501
        """
        pass

    def test_query_products_vendor_v3(self):
        """Test case for query_products_vendor_v3

        Query products of a contract  # noqa: E501
        """
        pass

    def test_shop_integration_post_request_vendor_v2(self):
        """Test case for shop_integration_post_request_vendor_v2

        Update shop integration import  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
